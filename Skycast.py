""" Author : Krishna Chaitanya Chavati
    Date   : 10.06.2014
    Problem: Skycast
    Description : The aim of the problem is to go from current channel to
    Destination channel in least possible number of steps. We have five things
    we have to check for minimum steps. They are:
    1) Pressing Up some number of times
    2) Pressing Down some number of times
    3) Checking if it's the immediate previously viewed channel
    4) INPUT the channel using number buttons
    5) Checking the combination of back with UP and DOWN

    First we are going to store the channel information in an object. After this
    calculate the costs for each approach discussed above and pick the least
    number of steps among them and output it. """ 

import sys

"""Channel_info class to store channel information"""
class Channel_info(object):

    def __init__(self):
        self.begin = None
        self.end   = None
        self.blocked_channels = []
        self.viewable_channels = None
        
    def build_list(self):
        self.viewable_channels = range(int(self.begin), int(self.end)+1)
        self.viewable_channels = [str(i) for i in self.viewable_channels]
        for each_blocked in self.blocked_channels:
            try:
                self.viewable_channels.remove(each_blocked)
            except ValueError:
                print each_blocked

""" Calculating the cost when we using the UP button only"""
def Up_cost(current, destination, obj):
    current_index = obj.viewable_channels.index(current)
    destination_index = obj.viewable_channels.index(destination)
    if current_index <= destination_index:
        return destination_index - current_index
    else:
        return len(obj.viewable_channels)-current_index+destination_index 

"""calculating the cost when we using the DOWN button only"""
def Down_cost(current, destination, obj):
    current_index = obj.viewable_channels.index(current)
    destination_index = obj.viewable_channels.index(destination)
    if current_index >= destination_index:
        return current_index - destination_index
    else:
        return len(obj.viewable_channels)-destination_index+current_index    

""" Check if it is the immediate previously visited channel""" 
def Is_previous(current, destination, back):
    if destination == back :
        return True
    return False

""" Cost to input the channel using number buttons"""
def Numpress_cost(destination):
    return len(destination)

""" Get the minimum number of steps from current channel to sestination channel
    by checking all the above possible approaches """
def Min_cost(current, destination, obj, back):
    if Is_previous(current, destination, back):
        return 1
    else:
        """Here we are also checking the combination of back with UP and DOWN buttons"""  
        return min(Up_cost(current, destination, obj), Down_cost(current, destination, obj), Numpress_cost(destination),
                   Up_cost(back, destination, obj)+1, Down_cost(back, destination, obj)+1)

""" The main method which gets the input from a file and returns the minimum number of steps """ 
def Skycast(File):
    lines = [line.strip() for line in open(File)]
    TV = Channel_info()
    TV.begin, TV.end = lines[0].split()
    blocked = lines[1].split()
    for i in range(1, len(blocked)):
        TV.blocked_channels.append(blocked[i])
    TV.build_list()
    ViewSequence = []
    sequence = lines[2].split()
    for i in range(1, len(sequence)):
        ViewSequence.append(sequence[i])
    steps = len(ViewSequence[0])
    back  = ViewSequence[0]
    for i in range(0, len(ViewSequence)-1):
        steps = steps + Min_cost(ViewSequence[i],ViewSequence[i+1], TV, back)
        back  = ViewSequence[i]
    return steps     

