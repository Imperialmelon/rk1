import unittest
from main import *


class Rk2_test(unittest.TestCase):
    Langs = [Lang(1, 'C++', 1985, 1),
             Lang(2, 'Python', 1991, 2),
             Lang(3, 'Java', 1995, 3),
             Lang(4, 'C', 1972, 4),
             Lang(5, 'Go', 2003, 4),
             Lang(6, 'PhP', 1995, 5),
             Lang(7, 'JavaScript', 1995, 4)
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
                   ]

    def test_1(self):
        one_to_many = [(l.name, l.cr_year, i.name)
                       for l in self.Langs
                       for i in self.Instrs
                       if l.instr_id == i.id]
        res_11 = []
        for i in one_to_many:
            if i[0][0] == 'J':
                res_11.append(i)
        self.assertEqual(res_11, [('Java', 1995, 'IntelliJ')])

    def test_2(self):
        one_to_many = [(l.name, l.cr_year, i.name)
                       for l in self.Langs
                       for i in self.Instrs
                       if l.instr_id == i.id]
        res_12_unsorted = []
        for instr in self.Instrs:
            instr_langs = list(filter(lambda i: i[2] == instr.name, one_to_many))
            if len(instr_langs) > 0:
                years = [year for _, year, _ in instr_langs]
                min_ = min(years)
                res_12_unsorted.append((instr.name, min_))
        res_12 = sorted(res_12_unsorted, key=itemgetter(1))
        self.assertEqual(res_12, [('VSCode', 1972), ('CLion', 1985), ('IntelliJ', 1995), ('PhP_sreda', 1995)])

    def test_3(self):
        many_to_many_temp = [(i.name, li.instr_id,  li.lang_id)
                             for i in self.Instrs
                             for li in self.Lang_instrs
                             if i.id == li.instr_id
                             ]
        many_to_many = [(l.name, l.cr_year, instr_name)
                        for instr_name, instr_id, lang_id in many_to_many_temp
                        for l in Langs if l.id == lang_id]
        res = sorted(many_to_many, key=lambda item: (item[0], item[1]))
        self.assertEqual(res, [('C++', 1985, 'CLion'), ('C++', 1985, 'VSCode'),('Python', 1991, 'PyCharm')])

if __name__ == '__main__':
    unittest.main()
