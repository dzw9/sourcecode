V0=float(float(input("请输入起始电压V0(E-6):"))/1000000)
V1=float(float(input("请输入终止电压V1(E-3):"))/1000)
R=((V1-V0)/0.1)
width=float(400/10000)
thickness=float(20/10000)
S=width*thickness
length=0.5
resistance=float(R*S)/length
print('样品的%r为:%E'%(chr(961).lower(),resistance))