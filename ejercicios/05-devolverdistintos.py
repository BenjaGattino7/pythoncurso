def devolver_distintos(num1,num2,num3):
    suma=num1+num2+num3
    if  suma > 15:
        return max(num1,num2,num3)
    elif suma < 10:
        return min(num1,num2,num3)
    elif 10 < suma < 15:
        return num1 + num2 + num3 - max(num1, num2, num3) - min(num1, num2, num3)

res1 = devolver_distintos(5,2,7)
res2 = devolver_distintos(2,4,2)
res3 = devolver_distintos(8,8,4)

print(res1)
print(res2)
print(res3)