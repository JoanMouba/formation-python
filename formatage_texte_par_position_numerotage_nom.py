# Formatage de texte par position, numérotage et nommage

ordre_par_defaut = "{}, {} et {}".format("performance", 
                                         "compatibility", 
                                         "usability")


ordre_par_position = "{2}, {0} et{ 1}".format("performance",
                                              "compatibility", 
                                              "usability")

ordre_par_nom = "{co}, {us} et {perf}".format(perf="performance",
                                              co="compatibility", 
                                              us="usability")

print("ordre par défaut:", ordre_par_defaut)
print("ordre par position:", ordre_par_position)
print("ordre par nom:", ordre_par_nom)

 
