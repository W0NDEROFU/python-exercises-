numero_facture = int(input("Saisir le numero de la facture : "))
date = input("Saisir la date de la facture : ")
montant = float(input("Saisir le montant de la facture : "))
tva = montant*(20/100)
montant_remise = montant*(2/100)
montant_ttc = (montant+tva)-montant_remise
print("TVA =",tva,"DH\nMontant TTC =",montant_ttc,"DH\nMontant Remise =",montant_remise,"DH")