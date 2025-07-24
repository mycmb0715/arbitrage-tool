import streamlit as st

st.title("🎯 套利计算器（自定义投注金额 + 返水）")

odds_A = st.number_input("A平台赔率", value=2.10)
odds_B = st.number_input("B平台赔率", value=1.95)
rebate_A = st.number_input("A返水比例", value=0.03)
rebate_B = st.number_input("B返水比例", value=0.02)
stake_A = st.number_input("A平台投注金额", value=100.0)
stake_B = st.number_input("B平台投注金额", value=100.0)

if st.button("计算套利结果"):
    win_A_profit = stake_A * (odds_A - 1)
    lose_B_loss = stake_B
    rebate_total = stake_A * rebate_A + stake_B * rebate_B
    total_profit_A_win = win_A_profit - lose_B_loss + rebate_total

    win_B_profit = stake_B * (odds_B - 1)
    lose_A_loss = stake_A
    total_profit_B_win = win_B_profit - lose_A_loss + rebate_total

    st.write(f"👉 若A赢：净利润 = {total_profit_A_win:.2f}")
    st.write(f"👉 若B赢：净利润 = {total_profit_B_win:.2f}")

    if total_profit_A_win >= 0 and total_profit_B_win >= 0:
        st.success("✅ 套利成立！无论输赢都可盈利")
    else:
        st.error("❌ 套利失败，存在亏损方向")
