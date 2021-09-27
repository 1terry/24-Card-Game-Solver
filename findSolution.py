import math
import itertools

num1 = input('enter number 1\n')
num2 = input('enter number 2\n')
num3 = input('enter number 3\n')
num4 = input('enter number 4\n')

numbers = [int(num1), int(num2), int(num3), int(num4)]

# solution is a brute-force method computing possible permutations, taken from LeetCode


class solution():
    def findOps(self, nums):
        if len(nums) == 1:
            # determines if the end result is close to 24
            if (math.isclose(nums[0], 24) == True):
                print(nums[0])

            return math.isclose(nums[0], 24)

        return any(self.findOps([x] + rest)
                   for a, b, *rest in itertools.permutations(nums)
                   for x in {a+b, a-b, a*b, b and a/b})


sol1 = solution()
print(sol1.findOps(numbers))

# displaying solution through brute forcing possible results
# I will probably change this into a more elegant solution in the future


class myShittySolution():
    def checkNumbers(self, a, b, c, d):
        for a, b, c, d in itertools.permutations(numbers, 4):
            sa = str(a)
            sb = str(b)
            sc = str(c)
            sd = str(d)
            # possible combinations of a,b,c,d
            #a + b + c + d
            #(a+b) * c + d
            #(a+b) * c * d
            #
            if (a + b + c + d > 23.99999 and a + b + c + d < 24.0000001):
                print("solution found: " + sa + " + " +
                      sb + " + " + sc + " + " + sd)
            if ((a+b) * c * d) == 24:
                print("solution found: (" + sa + " + " +
                      sb + ") * " + sc + " * " + sd)
            if (((a+b) * c/d) == 24):
                print("solution found: (" + sa + " + " +
                      sb + ") * " + sc + " / " + sd)
            if (a * b * c * d == 24):
                print("solution found: " + sa + " * " +
                      sb + " * " + sc + " * " + sd)
            if ((a+b+c)*d == 24):
                print("solution found: (" + sa + " + " +
                      sb + " + " + sc + ") + " + sd)
            if (a+b+c*d == 24):
                print("solution found: " + sa + " + " +
                      sb + " + " + sc + " * " + sd)
            if ((a*b)+(c*d) == 24):
                print("solution found: (" + sa + " * " +
                      sb + ") + " + sc + " * " + sd)
            if (a*b+c-d == 24):
                print("solution found: " + sa + " * " +
                      sb + " + " + sc + " - " + sd)
            if (a+b+c-d == 24):
                print("solution found: " + sa + " + " +
                      sb + " + " + sc + " - " + sd)
            if (a*b-c*d == 24):
                print("solution found: " + sa + " * " +
                      sb + " - " + sc + " * " + sd)
            if (a*b*(c-d) == 24):
                print("solution found: " + sa + " * " +
                      sb + " * (" + sc + " - " + sd + ")")
            if ((a - b) * c + d == 24):
                print("solution found: (" + sa + " - " +
                      sb + ") * " + sc + " + " + sd)
            if (a*b*c+d == 24):
                print("solution found: " + sa + " * " +
                      sb + " * " + sc + " + " + sd)
            if (a*b/c+d == 24):
                print("solution found: " + sa + " * " +
                      sb + " / " + sc + " + " + sd)
            if (c-d != 0 and a*b/c-d == 24):
                print("solution found: " + sa + " * " +
                      sb + " / " + sc + " - " + sd)
            if (c-d != 0 and a*b/(c-d) == 24):
                print("solution found: " + sa + " * " +
                      sb + " / (" + sc + " - " + sd + ")")
            if (a*b*c - d == 24):
                print("solution found: " + sa + " * " +
                      sb + " * " + sc + " + " + sd)
            if (b-d/c != 0 and a/(b-d/c) > 23.999 and a/(b-d/c) < 24.0001):
                print("solution found: " + sa + " / (" +
                      sb + " - (" + sc + " / " + sd + "))")
            if (b/c != 0 and a-(b/c) * d < 24.001 and a-(b/c) * d > 23.99):
                print("solution found: " + sa + " - (" +
                      sb + " / " + sc + ") * " + sd)
            if (b/c != 0 and (a-b/c) * d < 24.001 and (a-b/c) * d > 23.99):
                print("solution found: (" + sa + " - " +
                      sb + " / " + sc + ") * " + sd)


sol2 = myShittySolution()
print(sol2.checkNumbers(num1, num2, num3, num4))
