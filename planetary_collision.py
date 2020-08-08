class Soulusion(object):
    def asteroidCollision(self, asteroids):
        """
        first collision
        :type asteroids: List[int]
        :rtype: List[int]
        """
        s = []
        for x in asteroids:
            s.append(x)
            while len(s) >= 2 and s[-1] < 0 and s[-2] > 0:
                if abs(s[-1]) > s[-2]:
                    s.pop(-2)
                elif abs(s[-1]) == s[-2]:
                    s.pop()
                    s.pop()
                elif abs(s[-1]) < s[-2]:
                    s.pop()
        return s


if __name__ == '__main__':
    ls = [10, 2, -5]
    solusion = Soulusion()

    print(solusion.asteroidCollision(ls))
