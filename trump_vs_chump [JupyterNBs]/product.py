# keep the list minimal
# I think the following list should do:
#   1. house
#   2. car
#   3. THE utility (phone, electric, water, sewer, internet ... all wrapped up into one)
#   4. fringe products (clothes, furniture, electronics, etc. all wrapped up into one)
class Product:

    # what is necessary to create this item
    creation_values = dict()
    creation_values['starstuff'] = 0 # how much star stuff was used to make it
    creation_values['energy'] = 0 # how much energy expended to make it

    # monetary values
    starcoin_values = dict()
    starcoin_values['new'] = 0
    starcoin_values['current'] = 0
    starcoin_values['depreciation'] = 0 # how quickly this depreciates

    # as close to "inherent" value as this can get
    deterioration_metrics = dict()
    # how strong it is right after manufacture?
    # Below 75% of it's starting quality will render it unusable
    deterioration_metrics['starting_quality'] = 0 # ranges from 0 to 100 percent
    deterioration_metrics['current_quality'] = 0 # ranges from 0 to 100 percent
    deterioration_metrics['wear_and_tear'] = 0 # accelerated wear and tear when in use

    # this catalogues how much more efficient some particular action is
    # when this particular products is in use
    # (ie: what this product was designed to help with)
    purpose = dict()
    purpose['action'] = '' # which agent action was this product manufactured to help with?
    purpose['temporal_efficiency'] = 0
    purpose['energetic_efficiency'] = 0
    purpose['material_efficiency'] = 0
