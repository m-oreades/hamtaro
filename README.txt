Proof of concept

Hamtaro has the following attributes:
-hunger
-thirst
-love

At startup, the attributes are given a value between 1 and 100.

Hamtaro is introduced and the player is told to type commands to take care of him.

The main loop will run so long as hamtaro is alive.

The player is prompted for input.
feed: raises hunger to 100
water: raises thirst to 100
cuddle or kiss: raises love to 100
kill: euthanizes hamtaro
time: debugging tool to test attributes going to zero

When hamtaro is killed or any of his attributes reach zero,
a message describing why he died is displayed.
the game loop exits because hamtaro is no longer alive.


Features to add:

passage of time
persistence of values(json for now)
gui of some kind
