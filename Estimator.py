Health = 6
Attack = 4
DamageFromEffects = 1
HealingFromEffects = 1
Cost = 5
DamageTaken = 0
ValueLost = 0
P1min = 0
P1max = 1
P2min = 0
P2max = 1


MinValueOfBenefitialEffects = DamageFromEffects * P1min + HealingFromEffects * P2min + AdditionalEffectsValue
MaxValueOfBenefitialEffects = DamageFromEffects * P1max + HealingFromEffects * P2max + AdditionalEffectsValue

Coefficient1 = ((Health + Attack)/2 + MinValueOfBenefitialEffects)/(Cost + DamageTaken + ValueLost)
Coefficient2 = ((Health + Attack)/2 + MaxValueOfBenefitialEffects)/(Cost + DamageTaken + ValueLost)

print("Coefficient1 is: " + str(Coefficient1))
print("Coefficient2 is: " + str(Coefficient2))