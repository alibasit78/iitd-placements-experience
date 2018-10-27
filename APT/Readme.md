## A.P.T Portfolio Private Limited

- Designation:
    + Software Engineer (Strategy)
    + Software Engineer (Infrastructure)
- Place of Posting: Delhi or Bengaluru.
- CTC: 24 INR Per Annum
- Gross: 24 INR Per Annum
- They shortlisted students into one of the above two categories.
- They had different tests for each profile.

---

### Online Round (Strategy)

- Platform: [Testdome](https://www.testdome.com/)
- Duration: 1 hour 40 Minutes
- Language: Python
- Number of Questions: 4

**Q1. Change Directory: 25 Minutes**

- Implement the change directory function.
- Should work on Relative and Absolute Path.
- Change to parent directory `../..`
- Complex paths
- All test case passed
- [Code](a.py) 

**Q2. Platform Game: 30 Minutes**

- A player stands on a array of tiles numbered from 1 to n.
- Initial position of the player is given by x.
- Implement two operations.
    + Jump Left and Jump Right
    - Player jumps over the tile next to it in the appropriate direction.
    - After the jump the original tile vanishes.
    - For e.g initial position 3.
      ```python
      [0,1,2,(3),4, 5]
      Jump Left
      [0,(1), 2, 4, 5]
      Jump Right
      [0, 2, (4), 5]
      ```
- Test cases were checking both the efficiency and correctness.
- Initially attempted it with list (O(n) delete operation)
    + Didn't know `set` has O(1) delete :disappointed:
    + Time Limit Exceeded on larger test cases.
- Second Approach was to maintain two auxiliary arrays to maintain pointers to non vanished lefts and rights for each existing tile.
- No TLE. yeyy! :yum:
- But failed on one case.
- [Code](b.py)

**Q3. GroupTravel: 25 Minute**

- Given a list of group sizes
    + `[1, 2, 1, 1, 1, 2, 1, 3]`
- Find all possible bus capacities provided
    + Each Group will travel as a whole. That is the group will only board the bus only collectively.
    + Group i will only board the bus if group i-1 has already boarded/traveled.
    + Multiple groups can enter the bus if the bus capacity allows.
    + Bus will not move unless its completely full.
    + Bus once completely filled will go to the destination and then come back for other groups.
- Sample answer. Possible bus capacities
    + [3, 4, 6, 12]
- [Code](c.py)
    + Naive Solution
    + Check for all capacities between maximum group size and sum of all group sizes.
- 4/5 test cases passed. One TLE.

**Q4. Splitting Game: 20 Minute**

- Play a Game
    + Given an array. Try to divide it into two contiguous sub-arrays with equal sum.
    + If possible to divide.
        * You get 1 point
        * Discard one of the two sub-arrays.
        * Play again on the remaining sub-array.
    + Else game ends.
- Simple Recursive Solution
- [Code](d.py)
- 3/5 test case Passed.
- Didn't have enough time remaining to implement DP.

