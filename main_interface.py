# main interface
import art.myVariant
import Ant.vr1
print("Выберите ученика:")
print("1. Корчагин")
print("2. Антонов")
print("3. Костин")
print("4. Столяров ")
choice = int(input())
match choice:
    case 1:
        art.myVariant.var2()
    case 2:
        Ant.vr1.var1()
    case 3:
        print()
    case 4:
        print()

