class Settings():
    """ Use for processing and storing all game settings """

    def __init__(self):
        """ Initialise game settings """
        # Display settings
        self.screen_width = 1120;
        self.screen_height = 630;
        self.bg_colour = (230, 230, 230)
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.fire_interval = 5*self.bullet_speed_factor
        self.ammo_capacity = 20
        self.ammo_amount = 10
        self.reload_factor = 0.1
        self.fleet_speed_factor = 0.010
        self.fleet_drop_factor = 0.5
        self.fleet_moving_direction = 1
        self.ship_limit = 3