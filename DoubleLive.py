"""
You are playing a computer game. Your army consists of B+H warriors: B bears and H humans. A bear has 2 hit points, and a human has 1 hit point.



There is an enemy archer equipped with T arrows. He shoots them one at a time, each time hitting a random warrior (chosen uniformly at random among your warriors that are still alive). A hit warrior loses 1 hit point, and dies immediately if his hit points become 0.



The strength of your army is defined as the product of three values: bears*humans*warriors. For example, if there are 3 bears and 10 humans still alive, the army strength is 3*10*13=390. It doesn't matter whether some bears are wounded (i.e. they have only 1 hit point).



Find the expected value of the army strength when the enemy archer runs out of arrows. Represent the answer as a reduced fraction P/Q. (That is, P and Q must be relatively prime.) For the constraints specified below Q will never be divisible by 10^9 + 7. Compute and return the value P*Q^{-1} modulo (10^9 + 7).


 Definition

        Class:DoubleLive
        Method:findEV
        Parameters:int, int, int
        Returns:int
        Method si               gnature:int findEV(int B, int H, int T)
        (be sure your method is public  )


             Constraints
             -B will be between 1 and 2000, inclusive.
             -H wil     l be between 1 and 2000, inclusive.
             -T will be between 0 and 2*B+H, in clusive.

              Examples
              0)

                    4
                    3
                    1
                    Returns: 571428644
                    The army consist    s of 4 bears and 3 humans. The enemy archer shoots 1 arrow.
                    With probability 4/7 the arrow will hit one of the bears. A bear loses 1 hit point but doesn't die. The army strength is 4*3*7=84.
                    With probability 3/7 the arrow will hit one of the humans. A human loses 1 hit point and dies. The army will have 4 bears and 2 humans, with total strength 4*2*6=48.
                    The answer is 4/7 * 84 + 3/7 * 48 = 480/7.
                    1)

                            3
                            10
                            0
                            R   eturns: 390
                            The enemy archer has no arrows, so your whole army survives. The strength is 3 * 10 * 13 = 390.
                            2)

                                    1
                                    2
                                    2
                                    Returns: 111111113
                                    The     army consists of 1 bear and 2 humans. There will be 2 arrows.
                                    With probability 1/3 the first arrow hits the only bear. He loses 1 hit point. Then with probability 1/3 the second arrows hits the same bear and thus he dies. The army strength is 0*2*2=0.
                                    With probability 1/3 the first arrow hits the only bear, and then with probability 2/3 the second arrow hits and kills one of two humans. The army strength is 1*1*2=2.
                                    With probability 2/3 the first arrow hits and kills one of two humans. Then, 1 bear and 1 human remain. The second arrow will hit and kill the human with probability 1/2, and otherwise it will wound the bear. The army strength will be 1*0*1=0 and 1*1*2=2, respectively.
                                    The answer is 1/9 * 0 + 2/9 * 2 + 1/3 * 0 + 1/3 * 2 = 0 + 4/9 + 0 + 2/3 = 10/9.
                                    3)

                                            1
                                            1
                                                1
                                                Returns: 1
                                                4)

                                                        1
                                                        1
                                                        2
                                                        Returns: 0
                                                        5)

                                                                3
                                                                10
                                                                16
                                                                Returns: 0
                                                                Ev      erybody will die :(
                                                                6)

                                                                        5
                                                                        2
                                                                        5
                                                                        Returns: 519487272
                                                                        7)

                                                                                1807
                                                                                1       234
                                                                                4040
                                                                                Returns: 373880953

"""
from collections import namedtuple

def get_average_strength(T, B, H):
    State = namedtuple("State", "T H halfB B")
    state = State(T, H, 0, B)
    def get_strength(state, memory=dict()):
        humans = state.H
        bears = state.halfB + state.B
        total = humans + bears
        if state.T == 0:
            return humans * bears * total
        elif state.H < 0 or state.halfB < 0 or state.B < 0:
            return 0
        else:
            army_number = state.H + state.halfB + state.B
            prob_H = state.H / army_number
            prob_halfB = state.halfB / army_number
            prob_B = state.B / army_number
            hit_H_state =  State(state.T-1, state.H-1, state.halfB, state.B)
            hit_halfB_state = State(state.T-1, state.H, state.halfB-1, state.B)
            hit_B_state = State(state.T-1, state.H, state.halfB+1, state.B-1)
            if hit_H_state not in memory:
                memory[hit_H_state] = get_strength(hit_H_state, memory)
            if hit_halfB_state not in memory:
                memory[hit_halfB_state] = get_strength(hit_halfB_state, memory)
            if hit_B_state not in memory:
                memory[hit_B_state] = get_strength(hit_B_state, memory)
            hit_H = memory[hit_H_state]
            hit_halfB = memory[hit_halfB_state]
            hit_B = memory[hit_B_state]
            return prob_H*hit_H + prob_halfB*hit_halfB + prob_B*hit_B

    return get_strength(state)


def main():
    print(get_average_strength(1, 1, 1))
    print(get_average_strength(2, 1, 1))
    print(get_average_strength(1, 4, 3))


if __name__ == "__main__":
    main()
