def find_hcf(a, b):
    hcf=1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf
def find_lcm(a,b,hcf):
    lcm=(a*b)//hcf
    return lcm
print("hcf and lcm calculator")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
hcf_result=find_hcf(num1,num2)
lcm_result=find_lcm(num1,num2,hcf_result)
print("\n results:")
print(f"HCF of {num1} and {num2} is: {hcf_result}")
print(f"LCM of {num1} and {num2} is: {lcm_result}")