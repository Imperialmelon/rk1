from operator import itemgetter


class Lang:
    def __init__(self, id, name, cr_year, instr_id):
        self.id = id
        self.name = name
        self.cr_year = cr_year
        self.instr_id = instr_id


class Instr:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Lang_Instr:
    def __init__(self, instr_id, lang_id):
        self.instr_id = instr_id
        self.lang_id = lang_id


Langs = [Lang(1, 'C++', 1985, 1),
         Lang(2, 'Python', 1991, 2),
         Lang(3, 'Java', 1995, 3),
         Lang(4, 'C', 1972, 4),
         Lang(5, 'Go', 2003, 4),
         Lang(6, 'PhP', 1995, 5),
         Lang(7, 'JavaScript', 1995,4)
         ]
Instrs = [Instr(1, 'CLion'),
          Instr(2, 'PyCharm'),
          Instr(3, 'IntelliJ'),
          Instr(4, 'VSCode'),
          Instr(5, 'PhP_sreda')]

Lang_instrs = [Lang_Instr(1, 1),
               Lang_Instr(2, 2),
               Lang_Instr(3, 3),
               Lang_Instr(4, 1),
               Lang_Instr(4, 4),
               Lang_Instr(4, 5),
               Lang_Instr(5, 6),
               Lang_Instr(4,7)
               ]


def main():
    one_to_many = [(l.name, l.cr_year, i.name)
                   for l in Langs
                   for i in Instrs
                   if l.instr_id == i.id]
    many_to_many_temp = [(i.name, li.instr_id, li.lang_id)
                         for i in Instrs
                         for li in Lang_instrs
                         if i.id == li.instr_id
                         ]
    many_to_many = [(l.name, l.cr_year, instr_name)
                    for instr_name, instr_id, lang_id in many_to_many_temp
                    for l in Langs if l.id == lang_id]
    print('Task 1')
    res_11 = []
    for i in one_to_many:
        if i[0][0] == 'J':
            res_11.append(i)
    print(res_11)

    print('Task 2')
    res_12_unsorted = []
    for instr in Instrs:
        instr_langs = list(filter(lambda i: i[2] == instr.name, one_to_many))
        if len(instr_langs) > 0:
            years = [year for _, year, _ in instr_langs]
            min_ = min(years)
            res_12_unsorted.append((instr.name, min_))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1))
    print(res_12)

    print('Task 3')
    print(sorted(many_to_many, key=lambda item: (item[0], item[1])))


if __name__ == '__main__':
    main()
