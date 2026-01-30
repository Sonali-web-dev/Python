marks = {
    "sonali" : 100,
    "Himanshi" : 90,
    "Nisha" : 90,
    0: "sonali"
}
#print(marks.items())
#print(marks.keys())
#print(marks.values())
#marks.update({"sonali": 99 , " Renuka": 80}) # This happens becouse dictionary is mutable
print(marks.get("Himanshi"))# Prints none
print(marks["Himanshi"])# Returns error