import math
import os
import cv2
import json
import random

from ultralytics import YOLO
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Potholes, detectedImage



classNames = [
                "HighEdgeCracking",
                "HighPothole",
                "HighRavelling",
                "LowEdgeCracking",
                "LowPothole",
                "LowRavelling",
                "MediumEdgeCracking",
                "MediumRavelling",
                "MediumRutting",
            ]


class_set = {
        "HighEdgeCracking": 0,
        "HighPothole": 0,
        "HighRavelling": 0,
        "LowEdgeCracking": 0,
        "LowPothole": 0,
        "LowRavelling": 0,
        "MediumEdgeCracking": 0,
        "MediumRavelling": 0,
        "MediumRutting": 0,
}

class_area = {
     "HighEdgeCracking": 0,
        "HighPothole": 0,
        "HighRavelling": 0,
        "LowEdgeCracking": 0,
        "LowPothole": 0,
        "LowRavelling": 0,
        "MediumEdgeCracking": 0,
        "MediumRavelling": 0,
        "MediumRutting": 0,
}





@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        batch_no = random.randint(100000, 999999)
        images = request.FILES.getlist('images')
        print(images)
        for image in images:
            pothole = Potholes(batch_no=batch_no, image=image)
            pothole.save()
        return JsonResponse({
            'batch': batch_no,
            'uploaded': 'true',
            'status': 'true'
        })



@csrf_exempt
def detect_pothole(request):
    if(request.method == 'POST'):
        try:
            data = json.loads(request.body)
            batch_no = data.get('batch_no')
            files = Potholes.objects.filter(batch_no=batch_no)
           
            for file in files:
                file_path = os.path.join("media/models/best.pt")
                model = YOLO(file_path)
                print(file.image)
                image_path = f"static/media/{file.image}"
                cv2_image = cv2.imread(image_path)
                results = model.predict(cv2_image)
                for r in results:
                    boxes = r.boxes
                    for box in boxes:
                        # bounding box
                        x1, y1, x2, y2 = box.xyxy[0]
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                        # put box in cam
                        cv2.rectangle(cv2_image, (x1, y1), (x2, y2), (255, 0, 255), 3)

                        # confidence
                        confidence = math.ceil((box.conf[0]*100))/100
                        print("Confidence --->",confidence)

                        # class name
                        cls = int(box.cls[0])
                        print("Class name -->", classNames[cls])
                        print(file.image)
                        detected = detectedImage(batch_no=batch_no, image_name=file.image)
                        detected.save()

                        # ! Generate Report
                        generateReport(classNames[cls], x1, y1)

                        # object details
                        org = [x1, y1]
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        fontScale = 1
                        color = (255, 0, 0)
                        thickness = 2

                        cv2.putText(cv2_image, classNames[cls], org, font, fontScale, color, thickness)
                        if not os.path.exists(f"static/output/{batch_no}"): os.makedirs(f"static/output/{batch_no}")
                        output_path = f"static/output/{file.image}"
                        print(output_path)
                        cv2.imwrite(output_path, cv2_image)                  
                    list = []
                    list.append(class_set)
                    class_area_list = []
                    class_area_list.append(class_area)  
                    print(list)    
            return JsonResponse({
                "status": "true",
                'detected': 'true',
                'report': list,
                'area': class_area_list
            })    
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        # Return an error response for unsupported HTTP methods
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def generatedImages(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        batch_no = data.get('batch_no')
        filtered_objects = detectedImage.objects.filter(batch_no=batch_no)
        images_list = []
        for images in filtered_objects:
            # images_list.append(f"/static/output/{images.image_name}")
            images_list.append({
                "url": f"/static/output/{images.image_name}",
                "name": f"{images.image_name}"
            })
        return JsonResponse({
            "images": images_list

        })




def generateReport(class_name, xmin, ymin):
    print(class_name)
    if class_name == "HighEdgeCracking":
        class_set["HighEdgeCracking"] = class_set["HighEdgeCracking"] + 1
        class_area["HighEdgeCracking"] = class_set["HighEdgeCracking"] + (xmin * ymin)
        
    elif class_name == "HighPothole":
        class_set["HighPothole"] = class_set["HighPothole"] + 1
        class_area["HighPothole"] = class_set["HighPothole"] + (xmin * ymin)
        
    elif class_name == "HighRavelling":
        class_set["HighRavelling"] = class_set["HighRavelling"] + 1
        class_area["HighRavelling"] = class_set["HighRavelling"] + (xmin * ymin)
        
    elif class_name == "LowEdgeCracking":
        class_set["LowEdgeCracking"] = class_set["LowEdgeCracking"] + 1
        class_area["LowEdgeCracking"] = class_set["LowEdgeCracking"] + (xmin * ymin)
        
    elif class_name == "LowPothole":
        class_set["LowPothole"] = class_set["LowPothole"] + 1
        class_area["LowPothole"] = class_set["LowPothole"] + (xmin * ymin)
        
    elif class_name == "LowRavelling":
        class_set["LowRavelling"] = class_set["LowRavelling"] + 1
        class_area["LowRavelling"] = class_set["LowRavelling"] + (xmin * ymin)
        
    elif class_name == "MediumEdge Cracking":
        class_set["MediumEdgeCracking"] = class_set["MediumEdgeCracking"] + 1
        class_area["MediumEdgeCracking"] = class_set["MediumEdgeCracking"] + (xmin * ymin)
        
    elif class_name == "MediumRavelling":
        class_set["MediumRavelling"] = class_set["MediumRavelling"] + 1
        class_area["MediumRavelling"] = class_set["MediumRavelling"] + (xmin * ymin)
        
    elif class_name == "MediumRutting":
        class_set["MediumRutting"] = class_set["MediumRutting"] + 1
        class_area["MediumRutting"] = class_set["MediumRutting"] + (xmin * ymin)