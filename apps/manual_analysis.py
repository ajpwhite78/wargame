import streamlit as st
import pandas as pd
from apps.functions import get_default_fields, run_whatif, highlight_diff_by_row, FileDownloader, MultiFileDownloader

spinner_css = """
    <style>
        #custom-spinner {
            display: inline-block;
            width: 150px;
            height: 150px;
            border: 8px solid #6f72de;
            border-left-color: rgba(0, 0, 0, 0);
            border-radius: 50%;
            animation: spin 1s ease-in-out infinite;
            position: fixed;
            left: 50%;
            margin-left: -50px; /* half of the width of the spinner */
            top: 50%;
            margin-top: -50px; /* half of the height of the spinner */
            z-index: 9999; /* ensures that the spinner is on top of other elements */  
        }
        @keyframes spin {
            to {
                transform: rotate(360deg);
            }
        }
    </style>
    <div id="custom-spinner">
    </div>
"""
spinner_css = """
<style>
    #custom-spinner {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 150px;
        height: 150px;
        position: fixed;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        z-index: 9999;
    }

    #spinner-border {
        border: 8px solid #6f72de;
        border-left-color: rgba(0, 0, 0, 0);
        border-radius: 50%;
        width: 150px;
        height: 150px;
        animation: spin 1s linear infinite;
    }

    #spinner-text {
        position: absolute;
        font-family: sans-serif;
        font-size: 22px;
        font-weight: bold;
        color: #6f72de;
    }

    @keyframes spin {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
</style>
<div id="custom-spinner">
    <div id="spinner-border"></div>
    <div id="spinner-text">Please wait</div>
</div>
"""

def get_financials(datafame, user_entity_name, user_period):
    entity_financials = datafame.loc[
        (datafame['entity_name'] == user_entity_name) & (datafame['period'] == user_period)]
    return entity_financials

def app():
    line = '<hr style="height: 5px; border:0px; background-color: #03A9F4; margin-top: 0px;">'
    line2 = '<hr style="height: 2.5px; border:0px; background-color: #25476A; margin-top: -30px;">'
    line3 = '<hr style="height: 4px; border:0px; background-color: #03A9F4; margin-top: -5px; margin-bottom: -20px;">'
    spinner = st.markdown(spinner_css, unsafe_allow_html=True)
    st.session_state.default_whatif_sales_revenue_growth_user_out, st.session_state.default_whatif_cost_of_goods_sold_margin_user_out, st.session_state.default_whatif_sales_general_and_admin_expenses_user_out, st.session_state.default_whatif_research_and_development_expenses_user_out, st.session_state.default_whatif_depreciation_and_amortization_expenses_sales_user_out, st.session_state.default_whatif_depreciation_and_amortization_split_user_out, st.session_state.default_whatif_interest_rate_user_out, st.session_state.default_whatif_tax_rate_user_out, st.session_state.default_whatif_dividend_payout_ratio_user_out, st.session_state.default_whatif_accounts_receivable_days_user_out, st.session_state.default_whatif_inventory_days_user_out, st.session_state.default_whatif_capital_expenditure_sales_user_out, st.session_state.default_whatif_capital_expenditure_user_out, st.session_state.default_whatif_capital_expenditure_indicator_user_out, st.session_state.default_whatif_tangible_intangible_split_user_out, st.session_state.default_whatif_accounts_payable_days_user_out, st.session_state.default_whatif_sale_of_equity_user_out, st.session_state.default_whatif_repurchase_of_equity_user_out, st.session_state.default_whatif_proceeds_from_issuance_of_debt_user_out, st.session_state.default_whatif_repayments_of_long_term_debt_user_out, st.session_state.default_whatif_notes_other_split_user_out = get_default_fields(select_user_entity_name=st.session_state.user_entity_name, select_user_period=st.session_state.user_reporting_period)
    st.session_state.df_income_statement_out, st.session_state.df_cash_flow_statement_out, st.session_state.df_balance_sheet_statement_out = run_whatif(select_user_entity_name=st.session_state.user_entity_name, select_user_period=st.session_state.user_reporting_period, select_user_whatif_sales_revenue_growth=st.session_state.default_whatif_sales_revenue_growth_user_out,
select_user_whatif_cost_of_goods_sold_margin=st.session_state.default_whatif_cost_of_goods_sold_margin_user_out, select_user_whatif_sales_general_and_admin_expenses=st.session_state.default_whatif_sales_general_and_admin_expenses_user_out, select_user_whatif_research_and_development_expenses=st.session_state.default_whatif_research_and_development_expenses_user_out, select_user_whatif_depreciation_and_amortization_expenses_sales=st.session_state.default_whatif_depreciation_and_amortization_expenses_sales_user_out, select_user_whatif_depreciation_and_amortization_split=st.session_state.default_whatif_depreciation_and_amortization_split_user_out, select_user_whatif_interest_rate=st.session_state.default_whatif_interest_rate_user_out, select_user_whatif_tax_rate=st.session_state.default_whatif_tax_rate_user_out, select_user_whatif_dividend_payout_ratio=st.session_state.default_whatif_dividend_payout_ratio_user_out,select_user_whatif_accounts_receivable_days=st.session_state.default_whatif_accounts_receivable_days_user_out, select_user_whatif_inventory_days=st.session_state.default_whatif_inventory_days_user_out, select_user_whatif_capital_expenditure_sales=st.session_state.default_whatif_capital_expenditure_sales_user_out, select_user_whatif_capital_expenditure=st.session_state.default_whatif_capital_expenditure_user_out, select_user_whatif_capital_expenditure_indicator=st.session_state.default_whatif_capital_expenditure_indicator_user_out, select_user_whatif_tangible_intangible_split=st.session_state.default_whatif_tangible_intangible_split_user_out, select_user_whatif_accounts_payable_days=st.session_state.default_whatif_accounts_payable_days_user_out, select_user_whatif_sale_of_equity=st.session_state.default_whatif_sale_of_equity_user_out, select_user_whatif_repurchase_of_equity=st.session_state.default_whatif_repurchase_of_equity_user_out, select_user_whatif_proceeds_from_issuance_of_debt=st.session_state.default_whatif_proceeds_from_issuance_of_debt_user_out, select_user_whatif_repayments_of_long_term_debt=st.session_state.default_whatif_repayments_of_long_term_debt_user_out, select_user_whatif_notes_other_split=st.session_state.default_whatif_notes_other_split_user_out)

    df_financials = get_financials(st.session_state.df_input, st.session_state.user_entity_name, st.session_state.user_reporting_period)
    spinner.empty()
    if st.session_state.df_income_statement_out.empty == False:
        styles = """
            <style>
                .col {
                    background-color: #25476A;
                    padding-left: 100px;
                    padding: 1px;
                    border: 5px solid #03A9F4;
                    border-radius: 10px;
                    height: 100px;
                    margin: 0;
                    padding-left: 30px;
                    padding-right: 30px;
                }
                .left {
                    text-align: left;
                    float: left;
                    width: 40%;
                    padding-top: 10px;
                    padding-bottom: 0px;
#                    padding: 10px;
                }
                .right {
                    text-align: right;
                    float: right;
                    width: 60%;
                    padding-top: 10px;
                    padding-bottom: 0px;
#                    padding: 10px;
                }
            </style>
        """
        st.markdown(styles, unsafe_allow_html=True)

        left_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 44px;'>Manual Analysis</span>"
        right_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 44px;'>{}&nbsp;&nbsp;&nbsp;{}</span>".format(st.session_state.user_entity_name, st.session_state.user_reporting_period)

        html = f"<div class='col'><div class='left'>{left_text}</div><div class='right'>{right_text}</div></div>"
        st.markdown(html, unsafe_allow_html=True)
        st.session_state.manual_analysis_confirm = True
        st.session_state.simulation_analysis_confirm = False

        text = '<div style="margin-top: 20px; margin-bottom: 0px; border: 3px solid #25476A; background-color: rgba(3, 169, 244, 0.2); border-radius:6px; padding-left:12px; padding-right: 12px; padding-top:12px; padding-bottom:12px;">\
            <p style="margin-top: 0px; margin-bottom: 0px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Manual analysis of financial statements involves a detailed examination of a target company&apos;s financial statements and other relevant financial data to gain insights into its financial position and performance. This analysis involves the following steps:</span></p>\
            <ul style="color:#25476A; text-align: justify;">\
                <li style="font-family:sans-serif; font-size:18px;">Reviewing the company&apos;s income statement, balance sheet and cash flow statement to understand its financial performance over time and identify trends.</li>\
                <li style="font-family:sans-serif; font-size:18px;">Identifying key financial drivers, such as sales growth, COGS margin and operating expenses and analyzing how changes in these drivers can impact the company&apos;s financial performance.</li>\
                <li style="font-family:sans-serif; font-size:18px;">Conducting ratio analysis to evaluate the company&apos;s financial health and generate a credit rating. </li>\
                <li style="font-family:sans-serif; font-size:18px;">Conducting &quot;what-if&quot; scenario analysis to evaluate the potential impact of various events or changes on the company&apos;s financial performance, such as changes in interest rates, tax rates or market conditions. </li>\
            </ul>\
            <p style="margin-top: -10px; margin-bottom: 0px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">By performing a manual analysis of financial statements, Comrate&apos;s wargame scenario analysis application can provide valuable insights into a target company&apos;s financial position and trends, empowering you to make informed decisions regarding the current and future financial performance of target companies.</span></p>\
        </div>'

        st.markdown(text, unsafe_allow_html=True)

        st.text("")
        st.text("")
        col1, col2 = st.columns([5.8, 0.2])
        with col1:
            subtext1 = '<p style="margin-bottom: 0px;"><span style="font-family:sans-serif; color:#25476A; font-size:40px;">Income Statement Manual Input Fields</span></p>'
            st.markdown(subtext1, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                                <style>
                                /* Tooltip container */
                                .tooltip {
                                    position: relative;
                                    margin-bottom: 0px;
                                    display: inline-block;
                            #        border-bottom: 1px dotted black;
                                }

                                /* Tooltip text */
                                .tooltip .tooltiptext {
                                    visibility: hidden;
                                    width: 1000px;
                                    background-color: #b8d9e8;
                                    color: #25476A;
                                    text-align: justify;
                                    border-radius: 6px;
                                    padding: 10px 15px;
                                    white-space: normal;
                                    padding: 10px 10px 10px 10px;
                                    border: 2px solid #25476A;

                                    /* Position the tooltip text */
                                    position: absolute;
                                    z-index: 1;
                                    bottom: 125%;
                                    left: 50%;
                                    margin-left: -950px;

                                    /* Fade in tooltip */
                                    opacity: 0;
                                    transition: opacity 0.3s;
                                }

                                /* Tooltip arrow */
                                .tooltip .tooltiptext::after {
                                    content: "";
                                    position: absolute;
                                    top: 100%;
                                    left: 95%;
                                    margin-left: -5px;
                                    border-width: 5px;
                                    border-style: solid;
                                    border-color: #25476A transparent transparent transparent;
                                }

                                /* Show the tooltip text when you mouse over the tooltip container */
                                .tooltip:hover .tooltiptext {
                                    visibility: visible;
                                    opacity: 1;
                                }
                                /* Change icon color on hover */
                                .tooltip:hover i {
                                    color: rgba(111, 114, 222, 0.8);
                                }   
                                /* Set initial icon color */
                                .tooltip i {
                                    color: #25476A;
                                }
                                </style>
                                """,
                        unsafe_allow_html=True
                        )
            st.markdown(
                '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">',
                unsafe_allow_html=True)
            st.markdown(
                """
                <div class="tooltip">
                    <i class="fas fa-info-circle fa-2x""></i>
                    <span class="tooltiptext">
                        <ul>
                        Understanding financial metrics and ratios is essential for assessing a company&apos;s financial health and making informed investment decisions.                               
                            <li>Sales Growth: A measure of the percentage increase or decrease in revenue over a period of time.</li>
                            <li>COGS Margin: The percentage of revenue that is consumed by the cost of goods sold. It indicates how efficiently a company is using its resources to produce goods.</li>
                            <li>SG&A Expenses: The total operating expenses of a company that are not directly related to production, such as salaries, rent, utilities and marketing costs.</li>
                            <li>R&D Expenses: The amount of money a company spends on research and development activities. It indicates a company&apos;s commitment to innovation and growth.</li>
                            <li>D&A Expenses / Sales: Depreciation and amortization expenses as a percentage of revenue. It indicates how much a company is investing in its long-term assets and how much it is expensing in the current period.</li>
                            <li>D&A Split: The breakdown of depreciation and amortization expenses between tangible assets (D) and intangible assets (A). It indicates how much a company is investing in different types of assets.</li>
                            <li>Interest Rate: The cost of borrowing money. It indicates how much a company is paying to finance its operations and how much debt it has.</li>
                            <li>Tax Rate: The percentage of a company&apos;s income that is paid in taxes. It indicates how much income a company able to retain.</li>
                            <li>Dividend Payout Ratio: The percentage of earnings paid out as dividends to shareholders. It indicates how much a company is returning to its shareholders in the form of dividends and how much it is retaining for reinvestment.</li>                                    
                        These financial metrics and ratios can help provide a valuable insight into a company&apos;s financial position and performance.
                        </ul>
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(line, unsafe_allow_html=True)
        st.markdown(line2, unsafe_allow_html=True)
        instructions_text = '<p style="margin-top: -25px; margin-bottom: 20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Enter values for the income statement financial fields based on expectations for the company. Default values provided are based on the prior financial period.</span></p>'
        st.markdown(instructions_text, unsafe_allow_html=True)
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Sales Growth %</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_sales_revenue_growth_field = st.empty()
            st.session_state.user_whatif_sales_revenue_growth = user_whatif_sales_revenue_growth_field.number_input(label="", label_visibility="collapsed", min_value=None, max_value=None, step=None, format="%.2f", value=st.session_state.default_whatif_sales_revenue_growth_user_out, key="whatif_manual_1")
            st.text("")
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">COGS Margin %</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_cost_of_goods_sold_margin_field = st.empty()
            st.session_state.user_whatif_cost_of_goods_sold_margin = user_whatif_cost_of_goods_sold_margin_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=100.00, step=None, format="%.2f", value=st.session_state.default_whatif_cost_of_goods_sold_margin_user_out, key="whatif_manual_2")
        with col2:
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">SG&A Expenses $</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_sales_general_and_admin_expenses_field = st.empty()
            st.session_state.user_whatif_sales_general_and_admin_expenses = user_whatif_sales_general_and_admin_expenses_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_sales_general_and_admin_expenses_user_out, key="whatif_manual_3")
            st.text("")
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">R&D Expenses $</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_research_and_development_expenses_field = st.empty()
            st.session_state.user_whatif_research_and_development_expenses = user_whatif_research_and_development_expenses_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_research_and_development_expenses_user_out, key="whatif_manual_4")
        with col3:
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">D&A Expenses / Sales %</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_depreciation_and_amortization_expenses_sales_field = st.empty()
            st.session_state.user_whatif_depreciation_and_amortization_expenses_sales = user_whatif_depreciation_and_amortization_expenses_sales_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=None, format="%.2f", value=st.session_state.default_whatif_depreciation_and_amortization_expenses_sales_user_out, key="whatif_manual_5")
            st.text("")
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">D&A Split %</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_depreciation_and_amortization_split_field = st.empty()
            st.session_state.user_whatif_depreciation_and_amortization_split = user_whatif_depreciation_and_amortization_split_field.number_input(label="", label_visibility="collapsed", min_value=0, max_value=100, step=None, format="%i", value=st.session_state.default_whatif_depreciation_and_amortization_split_user_out, key="whatif_manual_6")
        with col4:
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Interest Rate %</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_interest_rate_field = st.empty()
            st.session_state.user_whatif_interest_rate = user_whatif_interest_rate_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=None, format="%.2f", value=st.session_state.default_whatif_interest_rate_user_out, key="whatif_manual_7")
            st.text("")
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Tax Rate %</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_tax_rate_field = st.empty()
            user_whatif_tax_rate_field = st.empty()
            st.session_state.user_whatif_tax_rate = user_whatif_tax_rate_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=None, format="%.2f", value=st.session_state.default_whatif_tax_rate_user_out, key="whatif_manual_8")
        with col5:
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Dividend Payout Ratio %</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_dividend_payout_ratio_field = st.empty()
            st.session_state.user_whatif_dividend_payout_ratio = user_whatif_dividend_payout_ratio_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=100.00, step=None, format="%.2f", value=st.session_state.default_whatif_dividend_payout_ratio_user_out, key="whatif_manual_9")
        st.text("")
        st.text("")

        col1, col2 = st.columns([5.8, 0.2])
        with col1:
            subtext2 = '<p style="margin-bottom: 0px;"><span style="font-family:sans-serif; color:#25476A; font-size: 40px;">Cash Flow Statement & Balance Sheet Manual Input Fields</span></p>'
            st.markdown(subtext2, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                                <style>
                                /* Tooltip container */
                                .tooltip {
                                    position: relative;
                                    margin-bottom: 0px;
                                    display: inline-block;
                            #        border-bottom: 1px dotted black;
                                }
    
                                /* Tooltip text */
                                .tooltip .tooltiptext {
                                    visibility: hidden;
                                    width: 1000px;
                                    background-color: #b8d9e8;
                                    color: #25476A;
                                    text-align: justify;
                                    border-radius: 6px;
                                    padding: 10px 15px;
                                    white-space: normal;
                                    padding: 10px 10px 10px 10px;
                                    border: 2px solid #25476A;
    
                                    /* Position the tooltip text */
                                    position: absolute;
                                    z-index: 1;
                                    bottom: 125%;
                                    left: 50%;
                                    margin-left: -950px;
    
                                    /* Fade in tooltip */
                                    opacity: 0;
                                    transition: opacity 0.3s;
                                }
    
                                /* Tooltip arrow */
                                .tooltip .tooltiptext::after {
                                    content: "";
                                    position: absolute;
                                    top: 100%;
                                    left: 95%;
                                    margin-left: -5px;
                                    border-width: 5px;
                                    border-style: solid;
                                    border-color: #25476A transparent transparent transparent;
                                }
    
                                /* Show the tooltip text when you mouse over the tooltip container */
                                .tooltip:hover .tooltiptext {
                                    visibility: visible;
                                    opacity: 1;
                                }
                                /* Change icon color on hover */
                                .tooltip:hover i {
                                    color: rgba(111, 114, 222, 0.8);
                                }   
                                /* Set initial icon color */
                                .tooltip i {
                                    color: #25476A;
                                }
                                </style>
                                """,
                        unsafe_allow_html=True
                        )
            st.markdown(
                '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">',
                unsafe_allow_html=True)
            st.markdown(
                """
                <div class="tooltip">
                    <i class="fas fa-info-circle fa-2x""></i>
                    <span class="tooltiptext">
                        <ul>
                        Understanding financial metrics and ratios is essential for assessing a company&apos;s financial health and making informed investment decisions.                               
                            <li>Accounts Receivable Days: The number of days it takes for a company to collect payment for goods or services sold. A lower number of days is generally seen as a positive sign, indicating that a company is efficient in its collections process.</li>
                            <li>Inventory Days: The number of days it takes for a company to sell its inventory. A lower number of days is generally seen as a positive sign, indicating that a company has a strong demand for its products.</li>
                            <li>Capital Expenditure / Sales: The ratio of capital expenditures to sales. This ratio indicates how much a company is investing in long-term assets relative to its revenue. A higher ratio may suggest that a company is investing more in its long-term growth and may have higher future earnings potential.</li>
                            <li>Capital Expenditure: The amount of money a company spends on acquiring or improving long-term assets such as property, plant and equipment. This investment is typically made to increase a company&apos;s production capacity, efficiency or competitiveness.</li>
                            <li>Capital Expenditure Type (Ratio or Dollar): An indicator of whether capital expenditure is expressed as a ratio of sales or as a dollar amount. A ratio may be more informative in evaluating a company&apos;s investment decisions relative to its size, while a dollar amount may be more informative in evaluating the company&apos;s overall investment in long-term assets.</li>
                            <li>CapEx Tangible / Intangible Split: The breakdown of capital expenditures between tangible assets, such as property and equipment and intangible assets, such as patents and intellectual property. This breakdown indicates how much a company is investing in different types of long-term assets.</li>
                            <li>Accounts Payable Days: The number of days it takes for a company to pay its bills to suppliers. A higher number of days may indicate that a company is using its suppliers&apos; money to finance its operations and may be seen as a positive sign for the company&apos;s cash flow management.</li>
                            <li>Sales of Equity: The total amount of equity sold by a company during a period. This may include common stock, preferred stock or other types of equity.</li>
                            <li>Repurchase of Equity: The total amount of equity repurchased by a company during a period. This may include buying back common stock, preferred stock or other types of equity.</li>                                    
                            <li>Proceeds from Issuance of Debt: The total amount of money a company receives from issuing debt. This may include bonds, notes or other forms of debt financing.</li>
                            <li>Repayments of Long-Term Debt: The total amount of money a company pays back to lenders for long-term debt. This may include interest payments as well as principal repayments.</li>
                            <li>Notes / Other Split: The breakdown of a company&apos;s short-term debt between notes and other types of short-term debt. Notes refer to short-term debt that is issued with a specific maturity date, while other types of short-term debt may not have a specific maturity date or may be payable on demand.</li>
                        These financial metrics and ratios can help provide a valuable insight into a company&apos;s financial position and performance.
                        </ul>
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(line, unsafe_allow_html=True)
        st.markdown(line2, unsafe_allow_html=True)
        instructions_text = '<p style="margin-top: -25px; margin-bottom: 20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Enter values for the cash flow statement and balance sheet financial fields based on expectations for the company. Default values provided are based on the prior financial period.</span></p>'
        st.markdown(instructions_text, unsafe_allow_html=True)
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Accounts Receivable Days</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_accounts_receivable_days_field = st.empty()
            st.session_state.user_whatif_accounts_receivable_days = user_whatif_accounts_receivable_days_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_accounts_receivable_days_user_out, key="whatif_manual_10")
            st.text("")
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Inventory Days</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_inventory_days_field = st.empty()
            st.session_state.user_whatif_inventory_days = user_whatif_inventory_days_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_inventory_days_user_out, key="whatif_manual_11")
        with col2:
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Capital Expenditure / Sales %</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_capital_expenditure_sales_field = st.empty()
            st.session_state.user_whatif_capital_expenditure_sales = user_whatif_capital_expenditure_sales_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=None, format="%.2f", value=st.session_state.default_whatif_capital_expenditure_sales_user_out, key="whatif_manual_12")
            st.text("")
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Capital Expenditure $</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_capital_expenditure_field = st.empty()
            st.session_state.user_whatif_capital_expenditure = user_whatif_capital_expenditure_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_capital_expenditure_user_out, key="whatif_manual_13")
        with col3:
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Capital Expenditure Type</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_capital_expenditure_indicator_field = st.empty()
            st.session_state.user_whatif_capital_expenditure_indicator = user_whatif_capital_expenditure_indicator_field.selectbox(label="", label_visibility="collapsed", options=["Dollar", "Sales %"], key="whatif_manual_14")
            st.text("")
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Capex Tangible / Intangible Split %</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_tangible_intangible_split_field = st.empty()
            st.session_state.user_whatif_tangible_intangible_split = user_whatif_tangible_intangible_split_field.number_input(label="", label_visibility="collapsed", min_value=0, max_value=100, step=None, format="%i", value=st.session_state.default_whatif_tangible_intangible_split_user_out, key="whatif_manual_15")
        with col4:
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Accounts Payable Days</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_accounts_payable_days_field = st.empty()
            st.session_state.user_whatif_accounts_payable_days = user_whatif_accounts_payable_days_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_accounts_payable_days_user_out, key="whatif_manual_16")
            st.text("")
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Sale of Equity $</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_sale_of_equity_field = st.empty()
            st.session_state.user_whatif_sale_of_equity = user_whatif_sale_of_equity_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_sale_of_equity_user_out, key="whatif_manual_17")
        with col5:
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Repurchase of Equity $</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_repurchase_of_equity_field = st.empty()
            st.session_state.user_whatif_repurchase_of_equity = user_whatif_repurchase_of_equity_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_repurchase_of_equity_user_out, key="whatif_manual_18")
            st.text("")
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Proceeds from Issuance of Debt $</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_proceeds_from_issuance_of_debt_field = st.empty()
            st.session_state.user_whatif_proceeds_from_issuance_of_debt = user_whatif_proceeds_from_issuance_of_debt_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_proceeds_from_issuance_of_debt_user_out, key="whatif_manual_19")
        with col6:
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Repayments of Long Term Debt $</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_repayments_of_long_term_debt_field = st.empty()
            st.session_state.user_whatif_repayments_of_long_term_debt = user_whatif_repayments_of_long_term_debt_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_repayments_of_long_term_debt_user_out, key="whatif_manual_20")
            st.text("")
            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Notes / Other Split %</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            user_whatif_notes_other_split_field = st.empty()
            st.session_state.user_whatif_notes_other_split = user_whatif_notes_other_split_field.number_input(label="", label_visibility="collapsed", min_value=0, max_value=100, step=None, format="%i", value=st.session_state.default_whatif_notes_other_split_user_out, key="whatif_manual_21")
        st.text("")
        col1, col2, col3, col4 = st.columns([4, 1.05, 0.5, 0.5])
        with col1:
            st.text("")
            st.text("")
            instructions_text = '<p style="margin-top: -25px; margin-bottom: 20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Click "ReRun" once you have made your selection or click "Reset" to reset to the default values.</span></p>'
            st.markdown(instructions_text, unsafe_allow_html=True)
        with col3:
            resubmit_button = st.button("ReRun", key="3")
        with col4:
            reset_button = st.button("Reset", key="4")
        if resubmit_button:
            st.session_state.df_income_statement_out, st.session_state.df_cash_flow_statement_out, st.session_state.df_balance_sheet_statement_out = run_whatif(
                select_user_entity_name=st.session_state.user_entity_name, select_user_period=st.session_state.user_reporting_period,
                select_user_whatif_sales_revenue_growth=st.session_state.user_whatif_sales_revenue_growth,
                select_user_whatif_cost_of_goods_sold_margin=st.session_state.user_whatif_cost_of_goods_sold_margin,
                select_user_whatif_sales_general_and_admin_expenses=st.session_state.user_whatif_sales_general_and_admin_expenses,
                select_user_whatif_research_and_development_expenses=st.session_state.user_whatif_research_and_development_expenses,
                select_user_whatif_depreciation_and_amortization_expenses_sales=st.session_state.user_whatif_depreciation_and_amortization_expenses_sales,
                select_user_whatif_depreciation_and_amortization_split=st.session_state.user_whatif_depreciation_and_amortization_split,
                select_user_whatif_interest_rate=st.session_state.user_whatif_interest_rate,
                select_user_whatif_tax_rate=st.session_state.user_whatif_tax_rate,
                select_user_whatif_dividend_payout_ratio=st.session_state.user_whatif_dividend_payout_ratio,
                select_user_whatif_accounts_receivable_days=st.session_state.user_whatif_accounts_receivable_days,
                select_user_whatif_inventory_days=st.session_state.user_whatif_inventory_days,
                select_user_whatif_capital_expenditure_sales=st.session_state.user_whatif_capital_expenditure_sales,
                select_user_whatif_capital_expenditure=st.session_state.user_whatif_capital_expenditure,
                select_user_whatif_capital_expenditure_indicator=st.session_state.user_whatif_capital_expenditure_indicator,
                select_user_whatif_tangible_intangible_split=st.session_state.user_whatif_tangible_intangible_split,
                select_user_whatif_accounts_payable_days=st.session_state.user_whatif_accounts_payable_days,
                select_user_whatif_sale_of_equity=st.session_state.user_whatif_sale_of_equity,
                select_user_whatif_repurchase_of_equity=st.session_state.user_whatif_repurchase_of_equity,
                select_user_whatif_proceeds_from_issuance_of_debt=st.session_state.user_whatif_proceeds_from_issuance_of_debt,
                select_user_whatif_repayments_of_long_term_debt=st.session_state.user_whatif_repayments_of_long_term_debt,
                select_user_whatif_notes_other_split=st.session_state.user_whatif_notes_other_split)
        if reset_button:
            user_whatif_sales_revenue_growth_field.empty()
            st.session_state.user_whatif_sales_revenue_growth = user_whatif_sales_revenue_growth_field.number_input(label="", label_visibility="collapsed", min_value=None, max_value=None, step=None, format="%.2f", value=st.session_state.default_whatif_sales_revenue_growth_user_out, key="whatif_manual_22")
            user_whatif_cost_of_goods_sold_margin_field.empty()
            st.session_state.user_whatif_cost_of_goods_sold_margin = user_whatif_cost_of_goods_sold_margin_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=100.00, step=None, format="%.2f", value=st.session_state.default_whatif_cost_of_goods_sold_margin_user_out, key="whatif_manual_23")
            user_whatif_sales_general_and_admin_expenses_field.empty()
            st.session_state.user_whatif_sales_general_and_admin_expenses = user_whatif_sales_general_and_admin_expenses_field.number_input(
                label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f",
                value=st.session_state.default_whatif_sales_general_and_admin_expenses_user_out, key="whatif_manual_24")
            user_whatif_research_and_development_expenses_field.empty()
            st.session_state.user_whatif_research_and_development_expenses = user_whatif_research_and_development_expenses_field.number_input(
                label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f",
                value=st.session_state.default_whatif_research_and_development_expenses_user_out, key="whatif_manual_25")
            user_whatif_depreciation_and_amortization_expenses_sales_field.empty()
            st.session_state.user_whatif_depreciation_and_amortization_expenses_sales = user_whatif_depreciation_and_amortization_expenses_sales_field.number_input(
                label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=None, format="%.2f",
                value=st.session_state.default_whatif_depreciation_and_amortization_expenses_sales_user_out, key="whatif_manual_26")
            user_whatif_depreciation_and_amortization_split_field.empty()
            st.session_state.user_whatif_depreciation_and_amortization_split = user_whatif_depreciation_and_amortization_split_field.number_input(
                label="", label_visibility="collapsed", min_value=0, max_value=100, step=None, format="%i",
                value=st.session_state.default_whatif_depreciation_and_amortization_split_user_out, key="whatif_manual_27")
            user_whatif_interest_rate_field.empty()
            st.session_state.user_whatif_interest_rate = user_whatif_interest_rate_field.number_input(label="", label_visibility="collapsed",
                                                                                     min_value=0.00, max_value=None,
                                                                                     step=None, format="%.2f",
                                                                                     value=st.session_state.default_whatif_interest_rate_user_out,
                                                                                     key="whatif_manual_28")
            user_whatif_tax_rate_field.empty()
            st.session_state.user_whatif_tax_rate = user_whatif_tax_rate_field.number_input(label="", label_visibility="collapsed", min_value=None,
                                                                           max_value=0.00, step=None, format="%.2f",
                                                                           value=st.session_state.default_whatif_tax_rate_user_out,
                                                                           key="whatif_manual_29")
            user_whatif_dividend_payout_ratio_field.empty()
            st.session_state.user_whatif_dividend_payout_ratio = user_whatif_dividend_payout_ratio_field.number_input(
                label="", label_visibility="collapsed", min_value=0.00, max_value=100.00, step=None, format="%.2f",
                value=st.session_state.default_whatif_dividend_payout_ratio_user_out, key="whatif_manual_30")
            user_whatif_accounts_receivable_days_field.empty()
            st.session_state.user_whatif_accounts_receivable_days = user_whatif_accounts_receivable_days_field.number_input(
                label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f",
                value=st.session_state.default_whatif_accounts_receivable_days_user_out, key="whatif_manual_31")
            user_whatif_inventory_days_field.empty()
            st.session_state.user_whatif_inventory_days = user_whatif_inventory_days_field.number_input(label="", label_visibility="collapsed",
                                                                                       min_value=0.00, max_value=None,
                                                                                       step=1.00, format="%.0f",
                                                                                       value=st.session_state.default_whatif_inventory_days_user_out,
                                                                                       key="whatif_manual_32")
            user_whatif_capital_expenditure_sales_field.empty()
            st.session_state.user_whatif_capital_expenditure_sales = user_whatif_capital_expenditure_sales_field.number_input(
                label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=None, format="%.2f",
                value=st.session_state.default_whatif_capital_expenditure_sales_user_out, key="whatif_manual_33")
            user_whatif_capital_expenditure_field.empty()
            st.session_state.user_whatif_capital_expenditure = user_whatif_capital_expenditure_field.number_input(
                label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f",
                value=st.session_state.default_whatif_capital_expenditure_user_out, key="whatif_manual_34")
            user_whatif_capital_expenditure_indicator_field.empty()
            st.session_state.user_whatif_capital_expenditure_indicator = user_whatif_capital_expenditure_indicator_field.selectbox(
                label="", label_visibility="collapsed", options=["Dollar", "Sales %"], key="whatif_manual_35")
            user_whatif_tangible_intangible_split_field.empty()
            st.session_state.user_whatif_tangible_intangible_split = user_whatif_tangible_intangible_split_field.number_input(
                label="", label_visibility="collapsed", min_value=0, max_value=100, step=None, format="%i",
                value=st.session_state.default_whatif_tangible_intangible_split_user_out, key="whatif_manual_36")
            user_whatif_accounts_payable_days_field.empty()
            st.session_state.user_whatif_accounts_payable_days = user_whatif_accounts_payable_days_field.number_input(
                label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f",
                value=st.session_state.default_whatif_accounts_payable_days_user_out, key="whatif_manual_37")
            user_whatif_sale_of_equity_field.empty()
            st.session_state.user_whatif_sale_of_equity = user_whatif_sale_of_equity_field.number_input(label="", label_visibility="collapsed",
                                                                                       min_value=0.00, max_value=None,
                                                                                       step=1.00, format="%.0f",
                                                                                       value=st.session_state.default_whatif_sale_of_equity_user_out,
                                                                                       key="whatif_manual_38")
            user_whatif_repurchase_of_equity_field.empty()
            st.session_state.user_whatif_repurchase_of_equity = user_whatif_repurchase_of_equity_field.number_input(
                label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f",
                value=st.session_state.default_whatif_repurchase_of_equity_user_out, key="whatif_manual_39")
            user_whatif_proceeds_from_issuance_of_debt_field.empty()
            st.session_state.user_whatif_proceeds_from_issuance_of_debt = user_whatif_proceeds_from_issuance_of_debt_field.number_input(
                label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f",
                value=st.session_state.default_whatif_proceeds_from_issuance_of_debt_user_out, key="whatif_manual_40")
            user_whatif_repayments_of_long_term_debt_field.empty()
            st.session_state.user_whatif_repayments_of_long_term_debt = user_whatif_repayments_of_long_term_debt_field.number_input(
                label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f",
                value=st.session_state.default_whatif_repayments_of_long_term_debt_user_out, key="whatif_manual_41")
            user_whatif_notes_other_split_field.empty()
            st.session_state.user_whatif_notes_other_split = user_whatif_notes_other_split_field.number_input(
                label="", label_visibility="collapsed", min_value=0, max_value=100, step=None, format="%i",
                value=st.session_state.default_whatif_notes_other_split_user_out, key="whatif_manual_42")
            st.session_state.default_whatif_sales_revenue_growth_user_out, st.session_state.default_whatif_cost_of_goods_sold_margin_user_out, st.session_state.default_whatif_sales_general_and_admin_expenses_user_out, st.session_state.default_whatif_research_and_development_expenses_user_out, st.session_state.default_whatif_depreciation_and_amortization_expenses_sales_user_out, st.session_state.default_whatif_depreciation_and_amortization_split_user_out, st.session_state.default_whatif_interest_rate_user_out, st.session_state.default_whatif_tax_rate_user_out, st.session_state.default_whatif_dividend_payout_ratio_user_out, st.session_state.default_whatif_accounts_receivable_days_user_out, st.session_state.default_whatif_inventory_days_user_out, st.session_state.default_whatif_capital_expenditure_sales_user_out, st.session_state.default_whatif_capital_expenditure_user_out, st.session_state.default_whatif_capital_expenditure_indicator_user_out, st.session_state.default_whatif_tangible_intangible_split_user_out, st.session_state.default_whatif_accounts_payable_days_user_out, st.session_state.default_whatif_sale_of_equity_user_out, st.session_state.default_whatif_repurchase_of_equity_user_out, st.session_state.default_whatif_proceeds_from_issuance_of_debt_user_out, st.session_state.default_whatif_repayments_of_long_term_debt_user_out, st.session_state.default_whatif_notes_other_split_user_out = get_default_fields(
                select_user_entity_name=st.session_state.user_entity_name, select_user_period=st.session_state.user_reporting_period)
            st.session_state.df_income_statement_out, st.session_state.df_cash_flow_statement_out, st.session_state.df_balance_sheet_statement_out = run_whatif(
                select_user_entity_name=st.session_state.user_entity_name, select_user_period=st.session_state.user_reporting_period,
                select_user_whatif_sales_revenue_growth=st.session_state.default_whatif_sales_revenue_growth_user_out,
                select_user_whatif_cost_of_goods_sold_margin=st.session_state.default_whatif_cost_of_goods_sold_margin_user_out,
                select_user_whatif_sales_general_and_admin_expenses=st.session_state.default_whatif_sales_general_and_admin_expenses_user_out,
                select_user_whatif_research_and_development_expenses=st.session_state.default_whatif_research_and_development_expenses_user_out,
                select_user_whatif_depreciation_and_amortization_expenses_sales=st.session_state.default_whatif_depreciation_and_amortization_expenses_sales_user_out,
                select_user_whatif_depreciation_and_amortization_split=st.session_state.default_whatif_depreciation_and_amortization_split_user_out,
                select_user_whatif_interest_rate=st.session_state.default_whatif_interest_rate_user_out,
                select_user_whatif_tax_rate=st.session_state.default_whatif_tax_rate_user_out,
                select_user_whatif_dividend_payout_ratio=st.session_state.default_whatif_dividend_payout_ratio_user_out,
                select_user_whatif_accounts_receivable_days=st.session_state.default_whatif_accounts_receivable_days_user_out,
                select_user_whatif_inventory_days=st.session_state.default_whatif_inventory_days_user_out,
                select_user_whatif_capital_expenditure_sales=st.session_state.default_whatif_capital_expenditure_sales_user_out,
                select_user_whatif_capital_expenditure=st.session_state.default_whatif_capital_expenditure_user_out,
                select_user_whatif_capital_expenditure_indicator=st.session_state.default_whatif_capital_expenditure_indicator_user_out,
                select_user_whatif_tangible_intangible_split=st.session_state.default_whatif_tangible_intangible_split_user_out,
                select_user_whatif_accounts_payable_days=st.session_state.default_whatif_accounts_payable_days_user_out,
                select_user_whatif_sale_of_equity=st.session_state.default_whatif_sale_of_equity_user_out,
                select_user_whatif_repurchase_of_equity=st.session_state.default_whatif_repurchase_of_equity_user_out,
                select_user_whatif_proceeds_from_issuance_of_debt=st.session_state.default_whatif_proceeds_from_issuance_of_debt_user_out,
                select_user_whatif_repayments_of_long_term_debt=st.session_state.default_whatif_repayments_of_long_term_debt_user_out,
                select_user_whatif_notes_other_split=st.session_state.default_whatif_notes_other_split_user_out)

        df_income_statement_out_png = st.session_state.df_income_statement_out.style.set_table_styles([{'selector': 'td',
                                                                                          'props': [('color', '#25476A')]}, {'selector': 'th:nth-child(1)',
                                                                                          'props': [
                                                                                              ('text-align', 'left'),
                                                                                              ('font-weight', 'bold'), (
                                                                                              'background-color',
                                                                                              '#25476A'),
                                                                                              ('color', '#FAFAFA')]}, {
                                                                                             'selector': 'th:nth-child(n+2)',
                                                                                             'props': [('text-align',
                                                                                                        'center'), (
                                                                                                       'font-weight',
                                                                                                       'bold'), (
                                                                                                       'background-color',
                                                                                                       '#25476A'), (
                                                                                                       'color',
                                                                                                       '#FAFAFA')]},
                                                                                         {'selector': 'tr:nth-child(7) td',
                                                                                          'props': [
                                                                                              ('text-align', 'left'),
                                                                                              ('font-weight', 'bold'), (
                                                                                              'background-color',
                                                                                              '#6d6e73'),
                                                                                              ('color', '#FAFAFA!important')]}, {
                                                                                            'selector': 'tr:nth-child(7) td:nth-child(2), tr:nth-child(7) td:nth-child(3)',
                                                                                            'props': [('text-align', 'center')]
                                                                                            },{'selector': 'tr:nth-child(12) td',
                                                                                          'props': [
                                                                                              ('text-align', 'left'),
                                                                                              ('font-weight', 'bold'), (
                                                                                              'background-color',
                                                                                              '#6d6e73'),
                                                                                              ('color', '#FAFAFA!important')]}, {
                                                                                            'selector': 'tr:nth-child(12) td:nth-child(2), tr:nth-child(12) td:nth-child(3)',
                                                                                            'props': [('text-align', 'center')]
                                                                                            }, {'selector': 'tr:nth-child(17) td',
                                                                                          'props': [
                                                                                              ('text-align', 'left'),
                                                                                              ('font-weight', 'bold'), (
                                                                                              'background-color',
                                                                                              '#6d6e73'),
                                                                                              ('color', '#FAFAFA!important')]}, {
                                                                                            'selector': 'tr:nth-child(17) td:nth-child(2), tr:nth-child(17) td:nth-child(3)',
                                                                                            'props': [('text-align', 'center')]
                                                                                            }, {'selector': 'tr:nth-child(20) td',
                                                                                          'props': [
                                                                                              ('text-align', 'left'),
                                                                                              ('font-weight', 'bold'), (
                                                                                              'background-color',
                                                                                              '#6d6e73'),
                                                                                              ('color', '#FAFAFA!important')]}, {
                                                                                            'selector': 'tr:nth-child(20) td:nth-child(2), tr:nth-child(20) td:nth-child(3)',
                                                                                            'props': [('text-align', 'center')]
                                                                                            },
                                                                                         {'selector': 'tr:nth-child(2)',
                                                                                          'props': [('font-style',
                                                                                                     'italic')]},
                                                                                         {'selector': 'tr:nth-child(4)',
                                                                                          'props': [('font-style',
                                                                                                     'italic')]},
                                                                                         {'selector': 'tr:nth-child(8)',
                                                                                          'props': [('font-style',
                                                                                                     'italic')]}, {
                                                                                             'selector': 'tr:nth-child(13)',
                                                                                             'props': [('font-style',
                                                                                                        'italic')]}, {
                                                                                             'selector': 'tr:nth-child(16)',
                                                                                             'props': [('font-style',
                                                                                                        'italic')]}, {
                                                                                             'selector': 'tr:nth-child(19)',
                                                                                             'props': [('font-style',
                                                                                                        'italic')]}, {
                                                                                             'selector': 'tr:nth-child(21)',
                                                                                             'props': [('font-style',
                                                                                                        'italic')]}, {
                                                                                             'selector': 'tr:nth-child(23)',
                                                                                             'props': [('font-style',
                                                                                                        'italic')]},
                                                                                         {'selector': 'td:hover',
                                                                                          'props': [('background-color',
                                                                                                     'rgba(111, 114, 222, 0.4)')]},
                                                                                         {'selector': 'td',
                                                                                          'props': [('border',
                                                                                                     '0.5px solid #25476A')]},
                                                                                         {'selector': '', 'props': [(
                                                                                                                    'border',
                                                                                                                    '3px solid #25476A')]}]).apply(
                lambda row: highlight_diff_by_row(row, color1=(3, 169, 244, 0.5), color2=(0, 0, 0, 0)),
                axis=1).set_properties(subset=["%s" % st.session_state.user_reporting_period, "Scenario"],
                                       **{'text-align': 'center'}, **{'width': '120px'}).set_properties(subset=[
                "%s" % st.session_state.user_entity_name + " (" + df_financials['currency_iso'].values[
                    0] + " Millions)"], **{'text-align': 'left'}, **{'width': '400px'}).hide_index()

        df_cash_flow_statement_out_png = st.session_state.df_cash_flow_statement_out.style.set_table_styles([{'selector': 'td',
                                                                                          'props': [('color', '#25476A')]},{
            'selector': 'th:nth-child(1)',
            'props': [('text-align',
                       'left'), (
                          'font-weight',
                          'bold'), (
                          'background-color',
                          '#25476A'), (
                          'color',
                          '#FAFAFA')]}, {
            'selector': 'th:nth-child(n+2)',
            'props': [('text-align',
                       'center'), (
                          'font-weight',
                          'bold'), (
                          'background-color',
                          '#25476A'), (
                          'color',
                          '#FAFAFA')]}, {'selector': 'tr:nth-child(5) td',
                                                                                          'props': [
                                                                                              ('text-align', 'left'),
                                                                                              ('font-weight', 'bold'), (
                                                                                              'background-color',
                                                                                              '#6d6e73'),
                                                                                              ('color', '#FAFAFA!important')]}, {
                                                                                            'selector': 'tr:nth-child(5) td:nth-child(2), tr:nth-child(5) td:nth-child(3)',
                                                                                            'props': [('text-align', 'center')]
                                                                                            }, {'selector': 'tr:nth-child(7) td',
                                                                                          'props': [
                                                                                              ('text-align', 'left'),
                                                                                              ('font-weight', 'bold'), (
                                                                                              'background-color',
                                                                                              '#6d6e73'),
                                                                                              ('color', '#FAFAFA!important')]}, {
                                                                                            'selector': 'tr:nth-child(7) td:nth-child(2), tr:nth-child(7) td:nth-child(3)',
                                                                                            'props': [('text-align', 'center')]
                                                                                            }, {'selector': 'tr:nth-child(11) td',
                                                                                          'props': [
                                                                                              ('text-align', 'left'),
                                                                                              ('font-weight', 'bold'), (
                                                                                              'background-color',
                                                                                              '#6d6e73'),
                                                                                              ('color', '#FAFAFA!important')]}, {
                                                                                            'selector': 'tr:nth-child(11) td:nth-child(2), tr:nth-child(11) td:nth-child(3)',
                                                                                            'props': [('text-align', 'center')]
                                                                                            }, {'selector': 'tr:nth-child(16) td',
                                                                                          'props': [
                                                                                              ('text-align', 'left'),
                                                                                              ('font-weight', 'bold'), (
                                                                                              'background-color',
                                                                                              '#6d6e73'),
                                                                                              ('color', '#FAFAFA!important')]}, {
                                                                                            'selector': 'tr:nth-child(16) td:nth-child(2), tr:nth-child(16) td:nth-child(3)',
                                                                                            'props': [('text-align', 'center')]
                                                                                            }, {'selector': 'tr:nth-child(17) td',
                                                                                          'props': [
                                                                                              ('text-align', 'left'),
                                                                                              ('font-weight', 'bold'), (
                                                                                              'background-color',
                                                                                              '#6d6e73'),
                                                                                              ('color', '#FAFAFA!important')]}, {
                                                                                            'selector': 'tr:nth-child(17) td:nth-child(2), tr:nth-child(17) td:nth-child(3)',
                                                                                            'props': [('text-align', 'center')]
                                                                                            }, {
            'selector': 'tr:nth-child(3)',
            'props': [('font-style',
                       'italic')]},
            {
                'selector': 'tr:nth-child(9)',
                'props': [('font-style',
                           'italic')]},
            {'selector': 'td:hover',
             'props': [(
                 'background-color',
                 'rgba(111, 114, 222, 0.4)')]},
            {'selector': 'td',
             'props': [('border',
                        '0.5px solid #25476A')]},
            {'selector': '', 'props': [(
                'border',
                '3px solid #25476A')]}]).apply(
            lambda row: highlight_diff_by_row(row, color1=(3, 169, 244, 0.5), color2=(0, 0, 0, 0)),
            axis=1).set_properties(subset=["%s" % st.session_state.user_reporting_period, "Scenario"],
                                   **{'text-align': 'center'}, **{'width': '120px'}).set_properties(subset=[
            "%s" % st.session_state.user_entity_name + " (" + df_financials['currency_iso'].values[
                0] + " Millions)"], **{'text-align': 'left'}, **{'width': '400px'}).hide_index()

        df_balance_sheet_out_png = st.session_state.df_balance_sheet_statement_out.style.set_table_styles([{'selector': 'td',
                                                                                          'props': [('color', '#25476A')]},{
            'selector': 'th:nth-child(1)',
            'props': [(
                'text-align',
                'left'), (
                'font-weight',
                'bold'), (
                'background-color',
                '#25476A'),
                ('color',
                 '#FAFAFA')]},
            {
                'selector': 'th:nth-child(n+2)',
                'props': [(
                    'text-align',
                    'center'),
                    (
                        'font-weight',
                        'bold'), (
                        'background-color',
                        '#25476A'),
                    ('color',
                     '#FAFAFA')]},
                                                                                                           {
                                                                                                               'selector': 'tr:nth-child(7) td',
                                                                                                               'props': [
                                                                                                                   (
                                                                                                                   'text-align',
                                                                                                                   'left'),
                                                                                                                   (
                                                                                                                   'font-weight',
                                                                                                                   'bold'),
                                                                                                                   (
                                                                                                                       'background-color',
                                                                                                                       '#6d6e73'),
                                                                                                                   (
                                                                                                                   'color',
                                                                                                                   '#FAFAFA!important')]},
                                                                                                           {
                                                                                                               'selector': 'tr:nth-child(7) td:nth-child(2), tr:nth-child(7) td:nth-child(3)',
                                                                                                               'props': [
                                                                                                                   (
                                                                                                                   'text-align',
                                                                                                                   'center')]
                                                                                                           },
                                                                                                           {
                                                                                                               'selector': 'tr:nth-child(10) td',
                                                                                                               'props': [
                                                                                                                   (
                                                                                                                   'text-align',
                                                                                                                   'left'),
                                                                                                                   (
                                                                                                                   'font-weight',
                                                                                                                   'bold'),
                                                                                                                   (
                                                                                                                       'background-color',
                                                                                                                       '#6d6e73'),
                                                                                                                   (
                                                                                                                   'color',
                                                                                                                   '#FAFAFA!important')]},
                                                                                                           {
                                                                                                               'selector': 'tr:nth-child(10) td:nth-child(2), tr:nth-child(10) td:nth-child(3)',
                                                                                                               'props': [
                                                                                                                   (
                                                                                                                   'text-align',
                                                                                                                   'center')]
                                                                                                           },
            {'selector': 'tr:nth-child(13) td',
                                                                                          'props': [
                                                                                              ('text-align', 'left'),
                                                                                              ('font-weight', 'bold'), (
                                                                                              'background-color',
                                                                                              '#6d6e73'),
                                                                                              ('color', '#FAFAFA!important')]}, {
                                                                                            'selector': 'tr:nth-child(13) td:nth-child(2), tr:nth-child(13) td:nth-child(3)',
                                                                                            'props': [('text-align', 'center')]
                                                                                            },
             {'selector': 'tr:nth-child(18) td',
              'props': [
                  ('text-align', 'left'),
                  ('font-weight', 'bold'), (
                      'background-color',
                      '#6d6e73'),
                  ('color', '#FAFAFA!important')]}, {
                 'selector': 'tr:nth-child(18) td:nth-child(2), tr:nth-child(18) td:nth-child(3)',
                 'props': [('text-align', 'center')]
             },
             {'selector': 'tr:nth-child(21) td',
              'props': [
                  ('text-align', 'left'),
                  ('font-weight', 'bold'), (
                      'background-color',
                      '#6d6e73'),
                  ('color', '#FAFAFA!important')]}, {
                 'selector': 'tr:nth-child(21) td:nth-child(2), tr:nth-child(21) td:nth-child(3)',
                 'props': [('text-align', 'center')]
             },
             {'selector': 'tr:nth-child(22) td',
              'props': [
                  ('text-align', 'left'),
                  ('font-weight', 'bold'), (
                      'background-color',
                      '#6d6e73'),
                  ('color', '#FAFAFA!important')]}, {
                 'selector': 'tr:nth-child(22) td:nth-child(2), tr:nth-child(22) td:nth-child(3)',
                 'props': [('text-align', 'center')]
             },
             {'selector': 'tr:nth-child(28) td',
              'props': [
                  ('text-align', 'left'),
                  ('font-weight', 'bold'), (
                      'background-color',
                      '#6d6e73'),
                  ('color', '#FAFAFA!important')]}, {
                 'selector': 'tr:nth-child(28) td:nth-child(2), tr:nth-child(28) td:nth-child(3)',
                 'props': [('text-align', 'center')]
             },
            {
                'selector': 'tr:nth-child(3)',
                'props': [(
                    'font-style',
                    'italic')]},
            {
                'selector': 'tr:nth-child(5)',
                'props': [(
                    'font-style',
                    'italic')]},
            {
                'selector': 'tr:nth-child(15)',
                'props': [(
                    'font-style',
                    'italic')]},
            {
                'selector': 'tr:nth-child(29)',
                'props': [(
                    'font-style',
                    'italic')]},
            {'selector': 'td:hover',
             'props': [(
                 'background-color',
                 'rgba(111, 114, 222, 0.4)')]},
            {'selector': 'td',
             'props': [('border',
                        '0.5px solid #25476A')]},
            {'selector': '',
             'props': [('border',
                        '3px solid #25476A')]}]).apply(
            lambda row: highlight_diff_by_row(row, color1=(3, 169, 244, 0.5), color2=(0, 0, 0, 0)),
            axis=1).set_properties(subset=["%s" % st.session_state.user_reporting_period, "Scenario"],
                                   **{'text-align': 'center'}, **{'width': '120px'}).set_properties(subset=[
            "%s" % st.session_state.user_entity_name + " (" + df_financials['currency_iso'].values[
                0] + " Millions)"], **{'text-align': 'left'}, **{'width': '400px'}).hide_index()

        st.text("")
        st.markdown(styles, unsafe_allow_html=True)
        left_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 44px;'>{}&nbsp;{}&nbsp;{}</span>".format(str(st.session_state.user_reporting_period), "Rating:", "XXX")
        right_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 44px;'>{}&nbsp;{}</span>".format("Scenario Rating:", "XXX")

        html = f"<div class='col'><div class='left'>{left_text}</div><div class='right'>{right_text}</div></div>"
        st.markdown(html, unsafe_allow_html=True)
        text = '<p style="margin-top: 20px; margin-bottom: 10px; text-align: justify;"><span style="color: #25476A; background-color: rgba(3, 169, 244, 0.2); border-radius:6px; padding-left:12px; padding-right: 12px; padding-top:12px; padding-bottom:12px; font-family:sans-serif; font-size: 24px; display: block; width: 100%; border: 3px solid #25476A; font-weight: bold;">Comrate&apos;s proprietary credit ratings model calculates a {} rating for {} at {} and predicts a {} rating based on the scenario provided.</span></p>'.format("XXX", st.session_state.user_entity_name, st.session_state.user_reporting_period, "XXX")
        st.markdown(text, unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
        with col1:
            st.text("")
            st.text("")
            text = '<p style="margin-bottom: 0px;"><span style="font-family:sans-serif; color:#25476A; font-size: 40px;">Financial Statements</span></p>'
            st.markdown(text, unsafe_allow_html=True)
        with col4:
            text = '<p style="margin-bottom: 2px; margin-top: 20px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Download Statements</span></p>'
            st.markdown(text, unsafe_allow_html=True)
            statement_out_download_typ_field = st.empty()
            statement_out_download_type = statement_out_download_typ_field.selectbox(label="", label_visibility="collapsed",
                                                       options=["Select Download Type", "CSV", "PNG"],
                                                       key="manual_download1")
            if resubmit_button or reset_button:
                statement_out_download_typ_field.empty()
                statement_out_download_type = statement_out_download_typ_field.selectbox(label="", label_visibility="collapsed",
                                                           options=["Select Download Type", "CSV", "PNG"],
                                                           key="manual_download2")
        with col5:
             if statement_out_download_type == "CSV":
                spinner = st.markdown(spinner_css, unsafe_allow_html=True)
                st.text("")
                st.text("")
                statements_out = [(st.session_state.df_income_statement_out.reset_index(drop=True).to_csv().encode(), "manual_analysis_income_statement", "csv"), (st.session_state.df_cash_flow_statement_out.reset_index(drop=True).to_csv().encode(), "manual_analysis_cashflow_statement", "csv"), (st.session_state.df_balance_sheet_statement_out.reset_index(drop=True).to_csv().encode(), "manual_analysis_balance_sheet", "csv")]
                downloader = MultiFileDownloader()
                downloader.download_manual_figures(statements_out, st.session_state.user_entity_name)
                spinner.empty()
             if statement_out_download_type == "PNG":
                spinner = st.markdown(spinner_css, unsafe_allow_html=True)
                st.text("")
                st.text("")
                statements_out = ([df_income_statement_out_png.to_html(), "manual_analysis_income_statement", "png", "Income Statement", 36], [df_cash_flow_statement_out_png.to_html(), "manual_analysis_cash_flow_statement", "png", "Cash Flow Statement", 36], [df_balance_sheet_out_png.to_html(), "manual_analysis_balance_sheet", "png", "Balance Sheet", 36])
                downloader = MultiFileDownloader()
                downloader.export_tables(statements_out, st.session_state.user_entity_name)
                spinner.empty()
        st.markdown(line, unsafe_allow_html=True)
        st.markdown(line2, unsafe_allow_html=True)
        instructions_text = '<p style="margin-top: -25px; margin-bottom: 20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Company financial statements for the reporting period and the expected scenario are shown below. The financial statements may be downloaded for your records.</span></p>'
        st.markdown(instructions_text, unsafe_allow_html=True)

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            subtext3 = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 24px;">Income Statement</span></p>'
            st.markdown(subtext3, unsafe_allow_html=True)
        with col2:
            subtext3A = '<p style="margin-bottom: 2px; margin-top: 7px; text-align: right"><span style="font-family:sans-serif; color:#25476A; font-size: 16px;">(blue fields indicate change)&nbsp;&nbsp;&nbsp;&nbsp;</span></p>'
            st.markdown(subtext3A, unsafe_allow_html=True)
        with col3:
            subtext4 = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 24px;">Cash Flow Statement</span></p>'
            st.markdown(subtext4, unsafe_allow_html=True)
        with col4:
            st.markdown(subtext3A, unsafe_allow_html=True)
        with col5:
            subtext5 = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 24px;">Balance Sheet</span></p>'
            st.markdown(subtext5, unsafe_allow_html=True)
        with col6:
            st.markdown(subtext3A, unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(line3, unsafe_allow_html=True)
            st.markdown('<div style="margin-top: -11px">' + df_income_statement_out_png.to_html(), unsafe_allow_html=True)
        with col2:
            st.markdown(line3, unsafe_allow_html=True)
            st.markdown('<div style="margin-top: -11px">' + df_cash_flow_statement_out_png.to_html(), unsafe_allow_html=True)
        with col3:
            st.markdown(line3, unsafe_allow_html=True)
            st.markdown('<div style="margin-top: -11px">' + df_balance_sheet_out_png.to_html(), unsafe_allow_html=True)
