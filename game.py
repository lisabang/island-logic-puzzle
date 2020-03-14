from .game import universe

Universe = universe.Universe


class Game:
    def __init__(self, num_blue_eyed):
        self.day = 0
        self.base_universe = Universe(num_blue_eyed=num_blue_eyed)

    def run_witch(self):
        self.base_universe.invalidate_imagined_universes(
            lambda u, m: u.num_blue_eyed != 0
        )

    def advance_one_day(self):
        num_left = self.base_universe.leave_phase()
        self.base_universe.everyone_sees_eachother_phase()

        self.day += 1

        return num_left
