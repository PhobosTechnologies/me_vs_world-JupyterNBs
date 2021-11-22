import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import pygame as pg

from trump_agent import TrumpAgent
from chump_agent import ChumpAgent
from product import Product


"""
Shout out to that insufferable, unstoppable, entropy-amplifying,
single vector movement in a positive temporal direction which we
are all deeply frustrated with absolutely love to hate ...
(**drum roll please**),
that gray-haired bastard, Father Time!
---

Only two agents will be spawned.
This will be a simple sim based on the
example I thought of when I was on my mission.
Only two agents exist in an entire universe with limited amount of
"starstuff".
Starstuff is used to make energy for the agent, to fashion into coinage, to create tools and materials
and to trade in commercial transactions.

Trump controls all of the starstuff and maintains full control over Chump for one simple reason: Trump possesses
the ability to convert starstuff into consumable energy which allows both of them to survive.

Chump works for Trump; performing several jobs in exchange for payment in starcoins.
Chump's jobs are:
    1. mine starstuff
    2. mint starcoins from starstuff
    3. construct usable machines and assemblies from starstuff (cars, homes, batteries, ... whatever)
"""


# STARTING VARIABLES
# ORBITS_PER_SIMULATION   = 100 # years
# REVOLUTIONS_PER_ORBIT   = 365 # days
# ARCS_PER_REVOLUTION     = 24 # hours
ORBITS_PER_SIMULATION   = 1 # years
REVOLUTIONS_PER_ORBIT   = 20 # days
ARCS_PER_REVOLUTION     = 24 # hours


miniverse_starstuff_total = 2985984 # 2985984 because it's a cubic number and that's how I imagined it ... deal with it


# agents' starting values
starting_values = dict()
starting_values['energy']       = 240
starting_values['food']         = 240
starting_values['stuff2food']   = 40 # 1 starstuff makes 40 starfoods


# PRE-LOOP PREPARATIONS
# instantiate agents and prepare the "board"
trump = TrumpAgent(starting_values)
chump = ChumpAgent(starting_values)


x = np.linspace(0, 2*np.pi, 100)
y = np.cos(x)

fig, ax = plt.subplots()



# GAME LOOP
# orbits    -> revolutions  -> arcs
# years     -> days         -> hours
for standard_orbit in range(ORBITS_PER_SIMULATION):
    for standard_revolution in range(REVOLUTIONS_PER_ORBIT):
        for standard_arc in range(ARCS_PER_REVOLUTION):

            trump.move(standard_arc)
            chump.move(standard_arc)
