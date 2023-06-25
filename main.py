import math 

p_statique = float(input("Quelle est la pression statique (hPa) que vous observez actuellement ?\n"))
current_altitude_ft = round((1-(p_statique/1013.25)**0.190284)*145366.45,3)
current_altitude_m = round(current_altitude_ft*0.3048,3)
print("Vous êtes à",current_altitude_m,"m d'altitude !")
anticipation_approche = current_altitude_m/math.tan(3*math.pi/180)
print("Vous devrez initier votre decente lorsque vous serez à",round(anticipation_approche),"m de votre point de toucher sur la piste !")