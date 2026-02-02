from decimal import Decimal, getcontext, ROUND_CEILING

def compound_saving(monthly_amount, annual_rate, months):
    # 設定高精度小數計算
    getcontext().prec = 28

    # 型別轉換為 Decimal
    monthly_amount = Decimal(monthly_amount)
    annual_rate = Decimal(annual_rate)
    months = int(months)

    # 本金上限
    max_principal = Decimal('10000000')

    # 月利率
    monthly_rate = annual_rate / Decimal('12')

    total = Decimal('0')

    for month in range(1, months + 1):
        # 每月投入（不得超過上限）
        if total + monthly_amount > max_principal:
            monthly_amount = max_principal - total
            if monthly_amount <= 0:
                break

        # 加上當月投入
        total += monthly_amount

        # 計算複利
        total *= (Decimal('1') + monthly_rate)

        # 無條件進位取整數
        display_total = total.quantize(Decimal('1'), rounding=ROUND_CEILING)

        print(f"第 {month} 月存款總額：{display_total}")