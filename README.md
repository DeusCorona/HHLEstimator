# How to use HHL value estimator?

- The card value is primarily determined by body, and additionally by the effects it provides.

- The program is procedural, you can simply enter the body stats (Health/Attack) as well as Cost.

- Damage taken refers to a small number of cards that cause damage to both sides of the field

- Value lost refers to a small number of cards that consume another friendly troop to be played,
or gain extra stats/effects

- The main problem at determining the proper value of the card comes from calculating the best
and worst case scenario


# What is the meaning of coefficients?

To put it simply, coefficients are there to provide us with the information on how effectively our
energy spent was converted to value gained (damage dealth, healing gained, etc). A coefficient of 1.5
means that every point of energy spent was converted with 150% efficiency to value gained. For example,
a 2e tactic that deals 3 damage to the target has a 1.5 coefficient. He higher the coefficient, the
better the card.

# How to calculate coefficients in non-trivial cases

For this purpose we need to evaluate all the posible outcomes, both best case and worst case.
Probability is a number between 0 and 1. If your card has a Rally: deal 2 damage to random enemy,
probability of such an event is 1, with 2 damage dealt. A card that deals 4 damage to the target
and 2 to all enemy units if your primary target dies, would likely be calculated the following way:
4 * p(1) + 4 * p(0.5) in case there are 2 other enemy units in play. There is a lot of gameplay
experience to be accounted for when making these estimates, which is why you are provided with
best and worst case estimates. For example for the worst case estimate, it would just be 4 damage,
for best (realistic) case estimate it would be 4 + 6 damage dealt (in case enemy has 2 other troops).

# How to calculate additional effects value

Every effect can be estimated based on a tier-list. Rally is a solid +1, while things like Awakened
are -0.5. Essentially, the best way to do this estimate is to calculate the probability of the unit
using the trait and give it context. Berserk, Awakened and "Attack by itself" clearly take away the
full control of the unit, although they will deliver the damage. Combining any effect with Flank or
Fast automatically gives it a +1, as the effect becomes unavoidable. Shield is a tricky trait as in
cases it can lead to card having a double value, but this is where the best and worst case estimates
come into play once again.

# How to interpret the results

- If the coefficient is below 1, such card is subpar and usually not worth adding to any deck
- Coefficient at 1 means it's just a vanila card, but might be a staple burn tactic
- Coefficient > 1 and  < 1.3 means it can be considered as an addition to your deck. Likely an uncommon
- Coefficients > 1.3 and < 1.5 are usually epics and weak legos, usually worthy of adding to your deck
- Coefficients > 1.5 are usually staple cards. Strong epics and legos

- If the coefficients have a drastic value difference, it might indicate a niche, conditional or highly 
situational card.
