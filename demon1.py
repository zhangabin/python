'''
作者：zhangbin
data:2019.10.4  '''

# 汇率
USD_VS_RMB =6.77
 # 带单位的货币输入
currency_str_value= input('请输入带单位的货币金额(退出程序输入Q)：')
i=0
while currency_str_value!='Q':
    # 获取货币单位

    print('循环次数',i)
    i=i+1
    unit =currency_str_value[-3:]
    # print(unit)
    #占位符号
    if unit=='CNY':
        # 输入的是人民币
        rmb_str_value= currency_str_value[0:-3]
        #将字符串编程数字
        rmb_value=eval(rmb_str_value)
        # 汇率计算
        usd_value=rmb_value/USD_VS_RMB
        # 输出结果
        print('美元（USD）金额是:',usd_value)
    elif  unit=='USD':
        # 输入的是美元
        usd_str_value =currency_str_value[:-3]
         # 将字符串转换为数字
        usd_value=eval(usd_str_value)
        # 汇率计算
        rmb_value =usd_value * USD_VS_RMB
        # 输出结果
        print("人民币（RMB）金额是：",rmb_value)
    else:
        # 其他情况
       print('目前版本上不支持该种货币！')
    currency_str_value= input('请输入带单位的货币金额(退出程序输入Q)：')
print('程序已退出')


























