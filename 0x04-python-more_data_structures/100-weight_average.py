#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    
    my_weighted_score = 0
    total_weight = 0
    
    for score, weight in my_list:
        my_weighted_score += score * weight
        total_weight += weight
    
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero.")
    
    average = my_weighted_score / total_weight
    return average
