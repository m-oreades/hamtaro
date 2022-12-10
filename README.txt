Proof of concept

Hamtaro has the following attributes:
-hunger (0-100)
-thirst (0-100)
-love (0-100)
-alive (bool)
-birthday (time created, measured in (seconds since the epoch) / 10)
-last_checked (time last checked, measured in (seconds since the epoch) / 10)



At startup, if there is no saved information in the json file, Hamtaro's health attributes are given a default value of 50, arbitrarily.

if there is saved information in the json file, Hamtaro's attributes are taken from the json file.


Hamtaro is introduced and the player is told to type commands to take care of him.

The main loop will run so long as hamtaro is alive.

The player is prompted for input.
feed: raises hunger to 100
water: raises thirst to 100
cuddle or kiss: raises love to 100
kill: euthanizes hamtaro
quit: exits the game

every 10 seconds, each health attribute will decrease by 1.

every time the player inputs a command, the passed time is calculated and the attributes are updated.
whether hamtaro is alive is determined once before the player is prompted for input and immediately after.

When hamtaro is killed or any of his attributes reach zero,
a message describing why he died is displayed.
the game loop exits because hamtaro is no longer alive.


Features to add:

gui of some kind
