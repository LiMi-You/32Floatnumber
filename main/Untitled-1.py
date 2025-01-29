xiaoshu = input("输入一个小数：")
i = 0
u = 0 

cd = len(str(xiaoshu).split('.',1)[1])  

Integer_list = []

while(i == 0):
    u += 1
    jishaun = float(xiaoshu) * 2
    

    value_str = str(jishaun)

    print( "第" + str(u) + "次计算结果值:" + str(jishaun))

    if '.' in value_str:

        integer_part, fractional_part = value_str.split('.')
        
        ty = value_str.split('.')
        print(ty)

        

        print("整数值" + integer_part + ";" + "小数值" + fractional_part)

        Integer_list.append(integer_part)

        if (integer_part == "1" ) :
            print("当前数值：" + str(jishaun))
            # xiaoshu = jishaun % 1
            # print(str(xiaoshu) + " %运算结果" )
            # xiaoshu = "{:.cdf}".format(xiaoshu)
            # xiaoshu = f"{xiaoshu:.{cd}f}"
        
            # 截断小数部分
            truncated_fractional_part = fractional_part[:cd]
            # 组合成新的字符串
            truncated_value_str = '0' + '.' + truncated_fractional_part
            # 转换回浮点数
            xiaoshu = float(truncated_value_str)
        
            print(str(xiaoshu) + "处理后的值")
        else:
            print("计算数不满足大于1：" + str(jishaun))
            xiaoshu = jishaun
            # x = len(xiaoshu.split('.',1)[1])
            # print(str(xiaoshu))





        

    if(xiaoshu == 0 or u == 100) :
        i = 1
        
        print(i)
        print(Integer_list)
        break
    
    # print(str(jishaun)) 
    

    
pass



# changdu = str(xiaoshu).split('.')[1]
# print(changdu)
# print(jishaun)