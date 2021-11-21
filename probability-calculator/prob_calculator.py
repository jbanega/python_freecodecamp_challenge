import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, number in kwargs.items():
            for n in range(number):
                self.contents.append(color)
    

    def draw(self, number_of_balls):
        assert isinstance(number_of_balls, int),\
            "The number of balls must be an integer number"

        removed_balls = []
        if number_of_balls > len(self.contents):
            removed_balls = self.contents
        else:
            for n in range(number_of_balls):
                index = random.randrange(len(self.contents))
                ball_to_remove = self.contents[index]
                removed_balls.append(ball_to_remove)
                del self.contents[index]
        return sorted(removed_balls)
                
                
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    assert isinstance(hat, Hat),\
        "The first argument must be a hat object containing balls"
    assert isinstance(expected_balls, dict),\
        "Expected balls must be a dict indicating the exact group of balls to attempt to draw from the hat"
    assert isinstance(num_balls_drawn, int),\
        "The number of balls to drawn must be an integer number"
    assert isinstance(num_experiments, int),\
        "The number of experiments to run must be an integer number"
    
    expected_balls_list = []
    for color, number in expected_balls.items():
        for n in range(number):
            expected_balls_list.append(color)
    expected_balls_list = sorted(expected_balls_list)

    count = 0
    for n in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw_balls = hat_copy.draw(num_balls_drawn)

        ball_in_draw = False
        for ball in expected_balls_list:
            if ball in draw_balls:
                ball_in_draw = True
                index = draw_balls.index(ball)
                del draw_balls[index]
            else:
                ball_in_draw = False
                break
        if ball_in_draw:
            count += 1
    
    probability = count/num_experiments
    return probability


# Testing
if __name__ == "__main__":
    print("Test 1".center(30, "*"))
    hat = Hat(red=1, blue=2, yellow=4)
    print("Hat contents", hat.contents)
    print("List of draw balls:", hat.draw(6), "\n")

    print("Test 2".center(30, "*"))
    hat_2 = Hat(red=3, blue=4, yellow=4)
    probability = experiment(hat_2, {"red": 1, "blue": 1}, 3, 10)
    print("Probability:", probability, "\n")

    print("Test 3".center(30, "*"))
    hat_3 = Hat(blue=3,red=2,green=6)
    print(hat_3.contents)
    probability = experiment(hat=hat_3, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
    print("Probability:", probability, "\n")

    print("Test 4".center(30, "*"))
    hat_4 = Hat(yellow=5,red=1,green=3,blue=9,test=1)
    print(hat_4.contents)
    probability = experiment(hat=hat_4, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
    print("Probability:", probability)