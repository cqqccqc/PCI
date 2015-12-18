# coding=utf-8
critics = {
    'Lisa Rose': {
        'Lady in the water': 2.5,
        'Snake on a plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0
    },
    'Gene Seymour': {
        'Lady in the water': 3.0,
        'Snake on a plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.0,
        'The Night Listener': 3.5
    },
    'Micheal Philips': {
        'Lady in the water': 2.5,
        'Snake on a plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0
    },
    'Claudia Puig': {
        'Snake on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.0,
    }
}
if __name__ == "__main__":
    from math import sqrt

    def sim_distance(pref, person1, person2):
        # 相同评价过的电影列表
        si = {}
        for item in pref[person1]:
            if item in pref[person2]:
                si[item] = 1

        # 没有则返回0
        if len(si) == 0:
            return 0

        # 所有的差值平方和
        sum_of_squares = sum([pow(pref[person1][item] - pref[person2][item], 2)
                              for item in pref[person1] if item in pref[person2]])
        return 1/(1 + sqrt(sum_of_squares))

    print sim_distance(critics,  'Lisa Rose', 'Gene Seymour')