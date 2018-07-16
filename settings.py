class Settings():
    """ Use for processing and storing all game settings """

    def __init__(self):
        """ Initialise game settings """
        # Display settings
        self.game_title = "Alien Invasion"
        self.screen_width = 1120;
        self.screen_height = 630;
        self.bg_colour = (230, 230, 230)
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.ammo_capacity = 20
        self.ammo_amount = 10
        self.fleet_drop_factor = 0.5
        self.fleet_moving_direction = 1
        self.ship_limit = 3
        self.speed_incr_factor = 1.2
        self.score_incr_factor = 2
        
        self.dynamic_initialize()
        
    def dynamic_initialize(self):
        self.ship_speed_factor = 1.5
        self.fleet_speed_factor = 0.01
        self.bullet_speed_factor = 1.5
        self.reload_factor = 0.02
        self.score_value = 1
        self.fire_interval = 10*self.bullet_speed_factor
    
    def dynamic_change(self):
        self.ship_speed_factor *= self.speed_incr_factor
        self.fleet_speed_factor *= self.speed_incr_factor
        self.bullet_speed_factor *= self.speed_incr_factor
        self.reload_factor *= self.speed_incr_factor
        self.fire_interval = 10*self.speed_incr_factor*self.bullet_speed_factor
        self.score_value *= self.score_incr_factor
