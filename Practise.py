def cal_dis_price(op, dp):
    da = (op * dp) / 100
    fp = op - da
    return round(fp, 2)

values = input().split()

op = int(values[0])
dp = int(values[1])

fp = cal_dis_price(op, dp)
print(f"Price: {fp:.2f}")
