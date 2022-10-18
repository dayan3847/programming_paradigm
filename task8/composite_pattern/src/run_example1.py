# Task8: Composite Pattern
from task8.composite_pattern.src.Directory import Directory
from task8.composite_pattern.src.File import File

if __name__ == '__main__':
    pp = File('Programming Paradigm')
    print(pp.show())

    dm = File('Discrete Mathematics')
    ct = File('Computational Theory')
    rs = File('Research Seminar')

    mcc = Directory('MCC')
    print(mcc.show())

    mcc.add_item(pp)
    mcc.add_item(dm)
    mcc.add_item(ct)
    mcc.add_item(rs)
    print(mcc.show())

    mia = Directory('MIA')

    uady = Directory('UADY')
    uady.add_item(mcc)
    uady.add_item(mia)
    print(uady.show())
