V0=float(float(input("请输入起始电压V0(E-6):"))/1000000)
V1=float(float(input("请输入终止电压V1(E-3):"))/1000)
R=((V1-V0)/0.1)
width=float(float(input('请输入样品宽度(微米):'))/10000)
thickness=float(float(input('请输入样品厚度(微米):'))/10000)
S=width*thickness
length=float(input('请输入测试长度(cm):'))
resistance=float(R*S)/length
print('样品的%r为:%E'%(chr(961).lower(),resistance))