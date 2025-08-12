import streamlit as st

# ---------------- Page Setup ----------------
st.set_page_config(page_title="Loan Eligibility Dashboard", layout="wide")
st.title("📊 Loan Eligibility Dashboard")

st.markdown("This tool evaluates an applicant's loan eligibility based on personal, income, and asset details.")

# ---------------- Personal Details ----------------
st.header("1️⃣ Personal Details")
col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("Applicant Name")
with col2:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
with col3:
    family_members = st.number_input("Family Members", min_value=0, step=1)

dependent_members = st.number_input("Dependent Members", min_value=0, step=1)
earning_members = st.number_input("Earning Members", min_value=0, step=1)

# ---------------- Income Details ----------------
st.header("2️⃣ Income Details")
income_type = st.radio("Income Type", ["Business", "Salaried"], horizontal=True)

if income_type == "Business":
    nature = st.selectbox("Nature of Business", ["Service", "Trading"])
    if nature == "Trading":
        trading_type = st.radio("Trading Type", ["Wholesale", "Retail"], horizontal=True)
    monthly_turnover = st.number_input("Monthly Turnover (₹)", min_value=0)
    margin = st.number_input("Profit Margin (%)", min_value=0.0, max_value=100.0)
    vintage = st.number_input("Business Vintage (Years)", min_value=0)
else:
    net_salary = st.number_input("Net Monthly Salary (₹)", min_value=0)
    employment_years = st.number_input("Years in Employment", min_value=0)

# ---------------- Financial Obligations ----------------
st.header("3️⃣ Financial Obligations & Assets")
col4, col5, col6 = st.columns(3)

with col4:
    obligations = st.number_input("Monthly Obligations (₹)", min_value=0)
with col5:
    household_exp = st.number_input("Household Expenditure (₹)", min_value=0)
with col6:
    rent = st.number_input("Monthly Rent (₹)", min_value=0)

asset_value = st.number_input("Value of Asset to Mortgage (₹)", min_value=0)
loan_amount = st.number_input("Required Loan Amount (₹)", min_value=0)

# ---------------- Eligibility Calculation ----------------
if st.button("Check Eligibility", use_container_width=True):
    if income_type == "Business":
        net_income = (monthly_turnover * (margin / 100)) - obligations - rent - household_exp
    else:
        net_income = net_salary - obligations - rent - household_exp

    score = 0
    if 21 <= age <= 60:
        score += 20
    if net_income > 25000:
        score += 30
    if asset_value >= loan_amount:
        score += 50

    st.subheader("📈 Eligibility Result")
    if asset_value < loan_amount:
        st.error("❌ Application Rejected: Loan amount exceeds asset value.")
    elif score >= 60:
        st.success(f"✅ Eligible for Loan. Score: {score}/100")
        st.info(f"💰 Estimated Maximum Loan Amount: ₹{net_income * 12:,.0f}")
    else:
        st.warning(f"⚠️ Low Eligibility Score ({score}/100). May require guarantor or additional collateral.")
