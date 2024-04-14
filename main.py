from ultralytics import YOLO
from pathlib import Path
import cv2
import numpy
 
image_paths = [
            "./test_images/test_1.jpg",
            "./test_images/test_2.jpg",
            "./test_images/test_3.jpg",
            "./test_images/test_4.jpg",
            "./test_images/test_5.jpg",
            "./test_images/test_6.jpg",
            "./test_images/test_7.jpg",
            "./test_images/test_8.jpg",
            "./test_images/test_9.jpg",
            "./test_images/test_10.jpg",
            "./test_images/test_11.jpg",
            "./test_images/test_12.jpg",
            "./test_images/test_13.jpg",
            "./test_images/test_14.jpg",
            "./test_images/test_15.jpg",
            "./test_images/test_16.jpg",
            "./test_images/test_17.jpg",
            "./test_images/test_18.jpg",
            "./test_images/test_19.jpg",
            "./test_images/test_20.jpg",
            "./test_images/test_21.jpg",
            "./test_images/test_22.jpg",
            "./test_images/test_23.jpg",
            "./test_images/test_24.jpg",
            "./test_images/test_25.jpg",
            "./test_images/test_26.jpg",
            "./test_images/test_27.jpg",
            "./test_images/test_28.jpg",
            "./test_images/test_29.jpg",
            "./test_images/test_30.jpg",
            "./test_images/test_31.jpg",
            "./test_images/test_32.jpg",
            "./test_images/test_33.jpg",
            "./test_images/test_34.jpg",
            "./test_images/test_35.jpg",
            "./test_images/test_36.jpg",
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


def define_border_box(cv2_image, xmin, ymin, xmax, ymax):
    color = (0, 0, 255)
    thickness = 2
    cv2.rectangle(cv2_image, (xmin, ymin), (xmax, ymax), color, thickness)
    cv2.putText(cv2_image, class_id, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6,color, 2)
    # cv2.imshow('Image with Rectangle', cv2_image)
    
    
def save_output(single_path, cv2_image):
    file_name = single_path.split("/")
    output_path = f"./output/{file_name[2]}"
    cv2.imwrite(output_path, cv2_image)
    
def analysis(class_id):
    # print(class_id)
   
    
    if class_id == "High Edge Cracking":
        class_set["HighEdgeCracking"] = class_set["HighEdgeCracking"] + 1
        
    elif class_id == "High Pothole":
        class_set["HighPothole"] = class_set["HighPothole"] + 1
        
    elif class_id == "High Ravelling":
        class_set["HighRavelling"] = class_set["HighRavelling"] + 1
        
    elif class_id == "Low Edge Cracking":
        class_set["LowEdgeCracking"] = class_set["LowEdgeCracking"] + 1
        
    elif class_id == "Low Pothole":
        class_set["LowPothole"] = class_set["LowPothole"] + 1
        
    elif class_id == "Low Ravelling":
        class_set["LowRavelling"] = class_set["LowRavelling"] + 1
        
    elif class_id == "Medium Edge Cracking":
        class_set["MediumEdgeCracking"] = class_set["MediumEdgeCracking"] + 1
        
    elif class_id == "Medium Ravelling":
        class_set["MediumRavelling"] = class_set["MediumRavelling"] + 1
        
    elif class_id == "Medium Rutting":
        class_set["MediumRutting"] = class_set["MediumRutting"] + 1
        
def print_report():
    print("----------------------------")
    print("     POTHOLE ANALYSIS       ")
    print("----------------------------")
    print("----------------------------")
    print("High Edge Cracking", class_set["HighEdgeCracking"])
    print("____________________________")
    print("High Pothole",class_set["HighPothole"])
    print("____________________________")
    print("High Ravelling",class_set["HighRavelling"])
    print("____________________________")
    print("Low Edge Cracking",class_set["LowEdgeCracking"])
    print("____________________________")
    print("Low Pothole",class_set["LowPothole"])
    print("____________________________")
    print("Low Ravelling",class_set["LowRavelling"])
    print("____________________________")
    print("Medium Edge Cracking",class_set["MediumEdgeCracking"])
    print("____________________________")
    print("Medium Ravelling",class_set["MediumRavelling"])
    print("____________________________")
    print("Medium Rutting",class_set["MediumRutting"])
    print("____________________________")

for single in image_paths:
    # Load Image to CV2
    cv2_image = cv2.imread(single)
    # Load custom trained model
    model = YOLO("./best.pt")
    results = model.predict(single)
    result = results[0]
    box = result.boxes
    # print(box)

    
    for box in result.boxes:
        cords = box.xyxy[0].tolist()
        xmin, ymin, xmax, ymax = [round(x) for x in cords]
        class_id = result.names[box.cls[0].item()]
        conf = round(box.conf[0].item(), 2)
        # print("Object type:", class_id)
        # print("Coordinates:", cords)
        # print("Probability:", conf)
        # print(f"xmin: {round(xmin)}, ymin: {ymin}, xmax: {xmax}, ymax: {ymax}")
        # print("------")
        analysis(class_id)
        define_border_box(cv2_image, xmin, ymin, xmax, ymax)
    save_output(single, cv2_image)
print_report()
     


cv2.waitKey(0)
cv2.destroyAllWindows()


    