# Team Big Fit
# Created by: Serena Villacorta
# Big Fit Weight Tracker Class


class WeightTracker(object):
    def __init__(self, record_id, user_id, weight, record_date):
        self.record_id = record_id
        self.user_id = user_id
        self.weight = weight
        self.record_date = record_date

    def print_user(self):
        print("Record Id: ", self.record_id)
        print("User Id: ", self.user_id)
        print("Weight: ", self.weight)
        print("Record Date: ", self.record_date)
