import streamlit as st
import streamlit_nested_layout
import pandas as pd
import pathlib
import base64
import os
from apps import manual_analysis, simulation_analysis


st.set_page_config(page_title="Paydar", page_icon="images/Favicon.png", layout="wide")

dirpath = os.path.dirname(__file__)

if "df_input_file" not in st.session_state or "df_input" not in st.session_state or "df_field_name_mapping_file" not in st.session_state or "df_field_name_mapping" not in st.session_state:
    st.session_state.df_input_file = 'TechHardware_WhatIfFields_Ccy_v2_short_test.csv'
    st.session_state.df_input = pd.read_csv(st.session_state.df_input_file)
    st.session_state.df_field_name_mapping_file = 'field_name_mapping_update.csv'
    st.session_state.df_field_name_mapping = pd.read_csv(st.session_state.df_field_name_mapping_file)

#primary_clr = st.get_option("theme.primaryColor")
primary_clr = "#25476A"
secondary_clr = "#03A9F4"

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-position: center;
        animation: animateBg 5s linear infinite;        
    }}
    <--@keyframes animateBg {{
        100% {{
            filter: hue-rotate(360deg);
        }}
    }}-->
    </style>
    """,
        unsafe_allow_html=True
    )

add_bg_from_local("images/background.jpg")


def img_to_bytes(img_path):
    img_bytes = pathlib.Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def reset1():
    st.session_state.user_sector = sector_options[0]
    st.session_state.user_country = country_options[0]
    st.session_state.user_entity_name = entity_name_options[0]
    st.session_state.user_reporting_period = reporting_period_options[0]
    st.session_state.submit1_confirm = False
    st.session_state.submit2_confirm = False
    st.session_state.manual_analysis_confirm = False
    st.session_state.simulation_analysis_confirm = False
    if "user_whatif_simulated_values" in st.session_state:
        del st.session_state.user_whatif_simulated_values
    st.session_state.next1_confirm = False
    st.session_state.next2_confirm = False

def reset2():
    st.session_state.user_whatif = analysis_options[0]
    st.session_state.submit2_confirm = False
    st.session_state.manual_analysis_confirm = False
    st.session_state.simulation_analysis_confirm = False
    if "user_whatif_simulated_values" in st.session_state:
        del st.session_state.user_whatif_simulated_values
    st.session_state.next1_confirm = False
    st.session_state.next2_confirm = False

def change_callback1():
    st.session_state.submit1_confirm = False

hide_st_style = """
                <style>
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

line1 = '<hr class="line1" style="height:0.3em; border:0em; background-color: #03A9F4; margin-top: 0em;">'
line2 = '<hr class="line2" style="height:0.1875em; border:0em; background-color: #25476A; margin-top: 0.2em;">'
line_media_query1 = '''
    <style>
    @media (max-width: 600px) {
        .line1 {
            padding: 0.5em;
        }
    }
    </style>
'''
line_media_query2 = '''
    <style>
    @media (max-width: 600px) {
        .line2 {
            padding: 0.3em;
            margin-bottom: 8em;
        }
    }
    </style>
'''

header = """
    <style>
        .header {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #25476A;
            color: #FAFAFA;
            text-align: justify;
            padding: 0px;
            padding-left: 30px;
            padding-right: 30px;
            z-index: 1;
        }}
        .left-column {{
            display: flex;
            align-items: center;
            justify-content: center;
            float: left;            
            width: 30%;
            padding: 10px;
        }}
        .right-column {{
            font-size: 64px;
            text-indent: 60px;
            float: left;
            width: 70%;
            padding: 10px;
        }}
        .left-column img {{
            max-width: 120%;
            display: inline-block;
            vertical-align: middle;

        }}
    .clear {{
        clear: both;
    }}
    body {{
        margin-top: 1px;
    }}
    </style>
    <div class="header">
        <div class="left-column">
            <img src="data:image/png;base64,{}" class="img-fluid" alt="comrate_logo" width="120%">
        </div>
        <div class="right-column">
            WarGame Scenario Analysis
        </div>
        <div class="clear"></div>
    </div>
"""

#st.markdown(header.format(img_to_bytes("images/comrate_logo_small_update2.png")), unsafe_allow_html=True)





header2 = """
    <style>
        .header {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-image: url('data:image/png;base64,{}');
            background-repeat: no-repeat;
            background-size: cover;
            filter: brightness(0.9) saturate(0.8);
            opacity: 1;
            color: #FAFAFA;
            text-align: justify;
            padding: 0px;
            padding-left: 30px;
            padding-right: 30px;
            z-index: 1;
        }}
        .left1-column {{
            display: flex;
            align-items: center;
            justify-content: center;
            float: left;            
            width: 15%;
            padding: 10px;
        }}
        .right1-column {{
            font-size: 64px;
            text-indent: 60px;
            float: left;
            width: 85%;
            padding: 10px;
        }}
        .left1-column img {{
            max-width: 120%;
            display: inline-block;
            vertical-align: middle

        }}
    .clear {{
        clear: both;
    }}
    body {{
        margin-top: 1px;
    }}
    </style>
    <div class="header">
        <div class="left1-column">
            <img src="data:image/png;base64,{}" class="img-fluid" alt="comrate_logo" width="100%">
        </div>
        <div class="right1-column">
            WarGame Scenario Analysis
        </div>
        <div class="clear"></div>
    </div>
"""

# Replace `image_file_path` with the actual path to your image file
#image_file_path = "images/digital_background_update2.jpg"
#with open(image_file_path, "rb") as image_file:
#    encoded_string = base64.b64encode(image_file.read()).decode()

#st.markdown(header2.format(encoded_string, img_to_bytes("images/comrate_logo_small_update2.png")), unsafe_allow_html=True)

header3A = """
    <style>
        .header {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-image: url('data:image/png;base64,{}');
            background-repeat: no-repeat;
            background-size: cover;
            filter: brightness(0.9) saturate(0.8);
            opacity: 1;
            color: #FAFAFA;
            text-align: justify;
            padding: 0px;
            padding-left: 30px;
            padding-right: 30px;
            z-index: 1;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .left1-column {{
            display: flex;
            align-items: center;
            justify-content: center;
            float: left;            
            width: 20%;
            padding: 10px;
        }}
        .right1-column {{
            font-size: 4rem;
            text-indent: 40px;
            float: left;
            width: 90%;
            padding: 10px;
        }}
        .left1-column img {{
            max-width: 200%;
            display: inline-block;
            vertical-align: middle
        }}
        .button-div {{
            display: flex;
            justify-content: flex-end;
            align-items: center;
            gap: 20px;
            }}
            /*             
            border: 3px solid #FAFAFA;
            padding: 8px;
            border-width: 3px;
            border-radius: 3px;
            */

        .button {{
            background-color: #25476A;
            border-color: #FAFAFA;
            border-width: 3px;
            border-radius: 3px;
            color: #FAFAFA;
            padding: 0px 0px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 10px;
            cursor: pointer;
            width:6em;
            height:2em;
        }}
        .button:hover {{
            background-color: #b8d9e8;
            border-color: #FAFAFA;
            color: #25476A;
        }}
    .clear {{
        clear: both;
    }}
    body {{
        margin-top: 1px;
    }}
    .welcome-text {{
        font-size: 24px;
        margin-right: 34px;
        color: #FAFAFA;
    }}
    .welcome-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 70%;
        padding: 10px 30px
    }}
    .welcome-container div {{
        color: #FAFAFA;
    }}
    </style>
    <div class="header">
        <div class="left1-column">
            <img src="data:image/png;base64,{}" class="img-fluid" alt="comrate_logo" width="100%">
        </div>
        <div class="right1-column">
            WarGame Scenario Analysis
        </div>
        <div class="clear"></div>
        <div class="welcome-container">
            <div class="welcome-text">Welcome John</div>
        <div class="button-div">
            <button class="button">Help</button>
            <button class="button">Contact</button>
            <button class="button">Logout</button>
        </div>
        <div class="clear"></div>
    </div>
"""

header3 = """
    <style>
        :root {{
            --base-font-size: 1vw;  /* Define your base font size here */
        }}

        .header {{
            font-family:sans-serif; 
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-image: url('data:image/png;base64,{}');
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
            filter: brightness(0.9) saturate(0.8);
            opacity: 1;
            color: #FAFAFA;
            text-align: left;
            padding: 0.4em;  /* Convert 10px to em units */
            z-index: 1;
            display: flex;
            align-items: center;
        }}
        .left1-column {{
            display: flex;
            align-items: center;
            justify-content: center;
            float: left;            
            width: 15%;
            padding: 0em;  /* Convert 10px to em units */
        }}
        .right1-column {{
            font-size: 3.2em;  /* Convert 40px to em units */
            text-indent: 1em;  /* Convert 40px to em units */
            float: left;
            width: 80%;
            padding: 0em;  /* Convert 10px to em units */
            margin-right: auto;
        }}
        .left1-column img {{
            max-width: 200%;
            display: inline-block;
            vertical-align: middle;
        }}
        .button-div {{
            display: flex;
            justify-content: flex-start;
            align-items: center;
            width: 40%;
            gap: 2em;  /* Convert 20px to em units */
        }}
        .button {{
            background-color: #25476A;
            border-color: #FAFAFA;
            border-width: 0.1875em;  /* Convert 3px to em units */
            border-radius: 0.1875em;  /* Convert 3px to em units */
            color: #FAFAFA;
            padding: 0em 0em;  /* Adjust padding as per your preference */
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 0.8em;  /* Convert 16px to em units */
            margin: 0em;  /* Adjust margin as per your preference */
            cursor: pointer;
            width: 5em;
            height: 2em;
        }}
        .button:hover {{
            background-color: #b8d9e8;
            border-color: #25476A;
            color: #25476A;
        }}
        .clear {{
            clear: both;
        }}
        body {{
            margin-top: 1px;
            font-size: var(--base-font-size);  /* Set the base font size */
        }}
        .welcome-text {{
            font-size: 1.2em;  /* Adjust font size as per your preference */
            margin-right: auto;  /* Adjust margin as per your preference */
            color: #FAFAFA;
        }}
        .welcome-container {{
            display: flex;
            align-items: center;
            width: 50%;  /* Adjust width as per your preference */
            padding: 0em 0em;  /* Convert 10px 30px to em units */
        }}
        .welcome-container div {{
            color: #FAFAFA;
        }}
        @media screen and (max-width: 600px) {{
        .header {{
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 0.8em;  /* Adjust padding for smaller screens */
       }}

        .left1-column {{
            width: 100%;  /* Set width to 100% for full width on smaller screens */
            justify-content: center;
            text-align: center;
            display: flex;
            align-items: center;
            float: left;
            margin-bottom: -1em;  /* Adjust margin for smaller screens */
        }}
        .left1-column img {{
            width: 30%;
            display: flex;
            align-items: center;
            justify-content: center;
            float: left;
          }}
        .right1-column {{
            width: 100%;  /* Set width to 100% for full width on smaller screens */
            font-size: 7em;
            display: flex;
            text-indent: 0em;
            align-items: center;
            justify-content: center;
            text-align: center;  /* Center align text on smaller screens */
            margin-bottom: 0.2em;  /* Adjust margin for smaller screens */
        }}
        .welcome-container {{
            width: 70%;  /* Set width to 100% for full width on smaller screens */
            display: flex;
            text-align: center;
            font-size: 2.4em;
            justify-content: center;  /* Center align items on smaller screens */
            margin-bottom: 0.5em;  /* Adjust margin for smaller screens */
        }}
        .button-div {{
            width: 50%;  /* Set width to 100% for full width on smaller screens */
            justify-content: center;  /* Center align items on smaller screens */
            gap: 2em;  /* Convert 20px to em units */
        }}
        .button {{
            border-width: 0.1875em;  /* Convert 3px to em units */
            border-radius: 0.1875em;  /* Convert 3px to em units */
            font-size: 1.6em;  /* Convert 16px to em units */
            width: 5em;
            height: 2em;
        }}
    }}
    </style>
    <div class="header">
        <div class="left1-column">
            <img src="data:image/png;base64,{}" class="img-fluid" alt="comrate_logo" width="120%">
        </div>
        <div class="right1-column">
            WarGame Scenario Analysis
        </div>
        <div class="clear"></div>
        <div class="welcome-container">
            <div class="welcome-text">Welcome John</div>
            <div class="button-div">
                <!--<button class="button">Help</button>
                <!--<button class="button">Contact</button>-->
                <button class="button">Logout</button>
            </div>
        </div>
        <div class="clear"></div>
    </div>
"""

# Replace `image_file_path` with the actual path to your image file
image_file_path = "images/digital_background_update2.jpg"
with open(image_file_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

st.markdown(header3.format(encoded_string, img_to_bytes("images/Paydar-logo-white-transparent.png")), unsafe_allow_html=True)

import streamlit as st

with st.spinner():
    st.markdown("""
    <style>
        #spinner-container {
            position: relative;
            width: 256px;
            height: 256px;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
        }
        #spinner-container span {
            display: inline-block;
            align-items: center;
            justify-content: center;
            position: fixed;
            left: 0;
            width: 32px;
            height: 6px;
            background: #2c4766;
            border-radius: 8px;
            transform-origin: 128px;
            transform: scale(2.2) rotate(calc(var(--i) * (360deg / 50)));
            animation: animateBlink 3s linear infinite;
            animation-delay: calc(var(--i) * (3s / 50));
            z-index: 9999;
        }
        @keyframes animateBlink {
            0% {
                background: #00eeff;
            }
            25% {
                background: #2c4766;
            }
        }
    </style>
    <div id="spinner-container">
        <span style="--i:0;"></span>
        <span style="--i:1;"></span>
        <span style="--i:2;"></span>
        <span style="--i:3;"></span>
        <span style="--i:4;"></span>
        <span style="--i:5;"></span>
        <span style="--i:6;"></span>
        <span style="--i:7;"></span>
        <span style="--i:8;"></span>
        <span style="--i:9;"></span>
        <span style="--i:10;"></span>
        <span style="--i:11;"></span>
        <span style="--i:12;"></span>
        <span style="--i:13;"></span>
        <span style="--i:14;"></span>
        <span style="--i:15;"></span>
        <span style="--i:16;"></span>
        <span style="--i:17;"></span>
        <span style="--i:18;"></span>
        <span style="--i:19;"></span>
        <span style="--i:20;"></span>
        <span style="--i:21;"></span>
        <span style="--i:22;"></span>
        <span style="--i:23;"></span>
        <span style="--i:24;"></span>
        <span style="--i:25;"></span>
        <span style="--i:26;"></span>
        <span style="--i:27;"></span>
        <span style="--i:28;"></span>
        <span style="--i:29;"></span>
        <span style="--i:30;"></span>
        <span style="--i:31;"></span>
        <span style="--i:32;"></span>
        <span style="--i:33;"></span>
        <span style="--i:34;"></span>
        <span style="--i:35;"></span>
        <span style="--i:36;"></span>
        <span style="--i:37;"></span>
        <span style="--i:38;"></span>
        <span style="--i:39;"></span>
        <span style="--i:40;"></span>
        <span style="--i:41;"></span>
        <span style="--i:42;"></span>
        <span style="--i:43;"></span>
        <span style="--i:44;"></span>
        <span style="--i:45;"></span>
        <span style="--i:46;"></span>
        <span style="--i:47;"></span>
        <span style="--i:48;"></span>
        <span style="--i:49;"></span>
    </div>
    """)

# Simulate some processing time
import time
time.sleep(5)

# Display the result
st.write("Success!")






spinner_css_update = """
<style>
    #spinner-container {
        position: relative;
        width: 256px;
        height: 256px;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
    }
    #spinner-container span {
        display: inline-block;
        align-items: center;
        justify-content: center;
        position: fixed;
        left: 0;
        width: 32px;
        height: 6px;
        background: #2c4766;
        border-radius: 8px;
        transform-origin: 128px;
        transform: scale(2.2) rotate(calc(var(--i) * (360deg / 50)));
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(var(--i) * (3s / 50));
        z-index: 9999;
    }
    @keyframes animateBlink {
        0% {
            background: #00eeff;
        }
        25% {
            background: #2c4766;
        }
    }

</style>
<div id="spinner-container">
    <span style="--i:0;"></span>
    <span style="--i:1;"></span>
    <span style="--i:2;"></span>
    <span style="--i:3;"></span>
    <span style="--i:4;"></span>
    <span style="--i:5;"></span>
    <span style="--i:6;"></span>
    <span style="--i:7;"></span>
    <span style="--i:8;"></span>
    <span style="--i:9;"></span>
    <span style="--i:10;"></span>
    <span style="--i:11;"></span>
    <span style="--i:12;"></span>
    <span style="--i:13;"></span>
    <span style="--i:14;"></span>
    <span style="--i:15;"></span>
    <span style="--i:16;"></span>
    <span style="--i:17;"></span>
    <span style="--i:18;"></span>
    <span style="--i:19;"></span>
    <span style="--i:20;"></span>
    <span style="--i:21;"></span>
    <span style="--i:22;"></span>
    <span style="--i:23;"></span>
    <span style="--i:24;"></span>
    <span style="--i:25;"></span>
    <span style="--i:26;"></span>
    <span style="--i:27;"></span>
    <span style="--i:28;"></span>
    <span style="--i:29;"></span>
    <span style="--i:30;"></span>
    <span style="--i:31;"></span>
    <span style="--i:32;"></span>
    <span style="--i:33;"></span>
    <span style="--i:34;"></span>
    <span style="--i:35;"></span>
    <span style="--i:36;"></span>
    <span style="--i:37;"></span>
    <span style="--i:38;"></span>
    <span style="--i:39;"></span>
    <span style="--i:40;"></span>
    <span style="--i:41;"></span>
    <span style="--i:42;"></span>
    <span style="--i:43;"></span>
    <span style="--i:44;"></span>
    <span style="--i:45;"></span>
    <span style="--i:46;"></span>
    <span style="--i:47;"></span>
    <span style="--i:48;"></span>
    <span style="--i:49;"></span>
</div>
"""
st.markdown(spinner_css_update, unsafe_allow_html=True)





spinner_css = """
<style>
    #spinner-container {
        display: flex;
        align-items: center;
        justify-content: center;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 9999;
    }

    #custom-spinner {
        display: inline-block;
        width: 20vmin;
        height: 20vmin;
        border: 8px solid #6f72de;
        border-left-color: rgba(0, 0, 0, 0);
        border-radius: 50%;
        animation: spin 1s ease-in-out infinite;
    }

    @keyframes spin {
        to {
            transform: rotate(360deg);
        }
    }

    @media (max-width: 600px) {
        #custom-spinner {
            display: inline-block;
            width: 20vmin;
            height: 20vmin;
            border: 6px solid #6f72de;
            border-left-color: rgba(0, 0, 0, 0);
            border-radius: 50%;
            animation: spin 1s ease-in-out infinite;
        }
    }

</style>
<div id="spinner-container">
    <div id="custom-spinner"></div>
</div>
"""

image_center = """
<style>
    .image-container {{
        display: inline-block;
        width: 36%;
        text-align: center;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 9999;
    }}

    @media (max-width: 600px) {{
        .image-container {{
            width: 50%;
        }}
    }}
</style>
<div class="image-container">
    <img src="data:image/png;base64,{}" class="img-fluid" alt="logo" width="30%">
</div>
"""

if "user_sector" not in st.session_state or "user_country" not in st.session_state or "user_entity_name" not in st.session_state or "user_reporting_period" not in st.session_state or "user_whatif" not in st.session_state:
    st.session_state["user_sector"] = ""
    st.session_state["user_country"] = ""
    st.session_state["user_entity_name"] = ""
    st.session_state["user_reporting_period"] = ""
    st.session_state["user_whatif"] = ""

if "submit1_confirm" not in st.session_state or "submit2_confirm" not in st.session_state or "submit3_confirm" not in st.session_state or "manual_analysis_confirm" not in st.session_state or "simulation_analysis_confirm" not in st.session_state or "simulation_run_confirm" not in st.session_state or "next1_confirm" not in st.session_state or "next2_confirm" not in st.session_state or "next3_confirm" not in st.session_state or "next4_confirm" not in st.session_state:
    st.session_state["submit1_confirm"] = False
    st.session_state["submit2_confirm"] = False
    st.session_state["submit3_confirm"] = False
    st.session_state["manual_analysis_confirm"] = False
    st.session_state["simulation_analysis_confirm"] = False
    st.session_state["simulation_run_confirm"] = False
    st.session_state["next1_confirm"] = False
    st.session_state["next2_confirm"] = False
    st.session_state["next3_confirm"] = False
    st.session_state["next4_confirm"] = False

if "user_whatif_manual_field_options" not in st.session_state or "user_whatif_iterations" not in st.session_state:
    st.session_state["user_whatif_manual_field_options"] = []
    st.session_state["user_whatif_iterations"] = ""
#    st.session_state["user_whatif_confidence_level"] = ""

if "df_income_statement_out" not in st.session_state or "df_cash_flow_statement_out" not in st.session_state or "df_balance_sheet_statement_out" not in st.session_state or "df_ratings_sim_out" not in st.session_state or "df_income_statement_sim_out" not in st.session_state or "df_cash_flow_statement_sim_out" not in st.session_state or "df_balance_sheet_statement_sim_out" not in st.session_state or "df_statement_sim_out" not in st.session_state or "df_summary" not in st.session_state:
    st.session_state["df_income_statement_out"] = pd.DataFrame()
    st.session_state["df_cash_flow_statement_out"] = pd.DataFrame()
    st.session_state["df_balance_sheet_statement_out"] = pd.DataFrame()
    st.session_state["df_ratings_sim_out"] = pd.DataFrame()
    st.session_state["df_income_statement_sim_out"] = pd.DataFrame()
    st.session_state["df_cash_flow_statement_sim_out"] = pd.DataFrame()
    st.session_state["df_balance_sheet_statement_sim_out"] = pd.DataFrame()
    st.session_state["df_statement_sim_out"] = pd.DataFrame()
    st.session_state["df_summary"] = pd.DataFrame()

if "default_whatif_sales_revenue_growth_user_out" not in st.session_state or "default_whatif_cost_of_goods_sold_margin_user_out" not in st.session_state or "default_whatif_sales_general_and_admin_expenses_user_out" not in st.session_state or "default_whatif_research_and_development_expenses_user_out" not in st.session_state or "default_whatif_depreciation_and_amortization_expenses_sales_user_out" not in st.session_state or "default_whatif_depreciation_and_amortization_split_user_out" not in st.session_state or "default_whatif_interest_rate_user_out" not in st.session_state or "default_whatif_tax_rate_user_out" not in st.session_state or "default_whatif_dividend_payout_ratio_user_out" not in st.session_state or "default_whatif_accounts_receivable_days_user_out" not in st.session_state or "default_whatif_inventory_days_user_out" not in st.session_state or "default_whatif_capital_expenditure_sales_user_out" not in st.session_state or "default_whatif_capital_expenditure_user_out" not in st.session_state or "default_whatif_capital_expenditure_indicator_user_out" not in st.session_state or "default_whatif_tangible_intangible_split_user_out" not in st.session_state or "default_whatif_accounts_payable_days_user_out" not in st.session_state or "default_whatif_sale_of_equity_user_out" not in st.session_state or "default_whatif_repurchase_of_equity_user_out" not in st.session_state or "default_whatif_proceeds_from_issuance_of_debt_user_out" not in st.session_state or "default_whatif_repayments_of_long_term_debt_user_out" not in st.session_state or "default_whatif_notes_other_split_user_out" not in st.session_state:
    st.session_state["default_whatif_sales_revenue_growth_user_out"] = ""
    st.session_state["default_whatif_cost_of_goods_sold_margin_user_out"] = ""
    st.session_state["default_whatif_sales_general_and_admin_expenses_user_out"] = ""
    st.session_state["default_whatif_research_and_development_expenses_user_out"] = ""
    st.session_state["default_whatif_depreciation_and_amortization_expenses_sales_user_out"] = ""
    st.session_state["default_whatif_depreciation_and_amortization_split_user_out"] = ""
    st.session_state["default_whatif_interest_rate_user_out"] = ""
    st.session_state["default_whatif_tax_rate_user_out"] = ""
    st.session_state["default_whatif_dividend_payout_ratio_user_out"] = ""
    st.session_state["default_whatif_accounts_receivable_days_user_out"] = ""
    st.session_state["default_whatif_inventory_days_user_out"] = ""
    st.session_state["default_whatif_capital_expenditure_sales_user_out"] = ""
    st.session_state["default_whatif_capital_expenditure_user_out"] = ""
    st.session_state["default_whatif_capital_expenditure_indicator_user_out"] = ""
    st.session_state["default_whatif_tangible_intangible_split_user_out"] = ""
    st.session_state["default_whatif_accounts_payable_days_user_out"] = ""
    st.session_state["default_whatif_sale_of_equity_user_out"] = ""
    st.session_state["default_whatif_repurchase_of_equity_user_out"] = ""
    st.session_state["default_whatif_proceeds_from_issuance_of_debt_user_out"] = ""
    st.session_state["default_whatif_repayments_of_long_term_debt_user_out"] = ""
    st.session_state["default_whatif_notes_other_split_user_out"] = ""

if "user_whatif_sales_revenue_growth" not in st.session_state or "user_whatif_cost_of_goods_sold_margin" not in st.session_state or "user_whatif_sales_general_and_admin_expenses" not in st.session_state or "user_whatif_research_and_development_expenses" not in st.session_state or "user_whatif_depreciation_and_amortization_expenses_sales" not in st.session_state or "user_whatif_depreciation_and_amortization_split" not in st.session_state or "user_whatif_interest_rate" not in st.session_state or "user_whatif_tax_rate" not in st.session_state or "user_whatif_dividend_payout_ratio" not in st.session_state or "user_whatif_accounts_receivable_days" not in st.session_state or "user_whatif_inventory_days" not in st.session_state or "user_whatif_capital_expenditure_sales" not in st.session_state or "user_whatif_capital_expenditure" not in st.session_state or "user_whatif_capital_expenditure_indicator" not in st.session_state or "user_whatif_tangible_intangible_split" not in st.session_state or "user_whatif_accounts_payable_days" not in st.session_state or "user_whatif_sale_of_equity" not in st.session_state or "user_whatif_repurchase_of_equity" not in st.session_state or "user_whatif_proceeds_from_issuance_of_debt" not in st.session_state or "user_whatif_repayments_of_long_term_debt" not in st.session_state or "user_whatif_notes_other_split" not in st.session_state:
    st.session_state["user_whatif_sales_revenue_growth"] = ""
    st.session_state["user_whatif_cost_of_goods_sold_margin"] = ""
    st.session_state["user_whatif_sales_general_and_admin_expenses"] = ""
    st.session_state["user_whatif_research_and_development_expenses"] = ""
    st.session_state["user_whatif_depreciation_and_amortization_expenses_sales"] = ""
    st.session_state["user_whatif_depreciation_and_amortization_split"] = ""
    st.session_state["user_whatif_interest_rate"] = ""
    st.session_state["user_whatif_tax_rate"] = ""
    st.session_state["user_whatif_dividend_payout_ratio"] = ""
    st.session_state["user_whatif_accounts_receivable_days"] = ""
    st.session_state["user_whatif_inventory_days"] = ""
    st.session_state["user_whatif_capital_expenditure_sales"] = ""
    st.session_state["user_whatif_capital_expenditure"] = ""
    st.session_state["user_whatif_capital_expenditure_indicator"] = ""
    st.session_state["user_whatif_tangible_intangible_split"] = ""
    st.session_state["user_whatif_accounts_payable_days"] = ""
    st.session_state["user_whatif_sale_of_equity"] = ""
    st.session_state["user_whatif_repurchase_of_equity"] = ""
    st.session_state["user_whatif_proceeds_from_issuance_of_debt"] = ""
    st.session_state["user_whatif_repayments_of_long_term_debt"] = ""
    st.session_state["user_whatif_notes_other_split"] = ""

st.markdown("""
<style>
/* The input itself */
div[data-baseweb="select"] > div,
input[type=number] {
  margin-top: 0;
  color: #25476A;
  background-color: rgba(3, 169, 244, 0.2);
  border: 0.1875em solid #25476A;
  font-size: 1em;
  font-weight: bold;
}

/* Hover effect */
div[data-baseweb="select"] > div:hover,
input[type=number]:hover {
  background-color: rgba(111, 114, 222, 0.4);
}
/* Media query for small screens */
@media (max-width: 600px) {
  div[data-baseweb="select"] > div,
  input[type=number] {
    font-size: 0.8em;
    height: 3em;
  }
  }
</style>
""", unsafe_allow_html=True)

introduction_text = '''
    <p class="introduction_text" style="margin-top: -1.25em; margin-bottom: 1.25em; text-align: justify;"><span style="color: #25476A; background-color: rgba(3, 169, 244, 0.2); border-radius: 0.375em; padding-left: 0.75em; padding-right: 0.75em; padding-top: 0.5em; padding-bottom: 0.5em; font-family: sans-serif; font-size: 1em; font-weight: bold; display: block; width: 100%; border: 0.1875em solid #25476A;">Welcome to the Paydar wargame scenario analysis application, empowering you to make informed decisions regarding the current and future financial performance of target companies based on manual and scenario-based financial statement and credit rating analyses.</span></p>
'''

text_media_query1 = '''
    <style>
    @media (max-width: 600px) {
        p.introduction_text {
            font-size: 3.2em;
            border-width: 0.5em;
            position: relative;
            top: 0.5em;
        }
    }
    </style>
'''
st.markdown(text_media_query1 + introduction_text, unsafe_allow_html=True)

subtext1A = '<p class="subtext" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 2em;">Company Details</span></p>'
text_media_query2 = '''
    <style>
    @media (max-width: 600px) {
        p.subtext {
            font-size: 3em;
        }
    }
    </style>
'''
st.markdown(text_media_query2 + subtext1A, unsafe_allow_html=True)
st.markdown(line_media_query2 + line2, unsafe_allow_html=True)
instructions_text = '<p class="instructions_text" style="margin-top: -1.8em; margin-bottom: 0.8em; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 1em;">Use the dropdown menus to select the sector, country, company name and reporting period of the company you want to analyze. Click "Run" once you have made your selections or click "Cancel" to reset.</span></p>'
text_media_query3 = '''
    <style>
    @media (max-width: 600px) {
        p.instructions_text {
            font-size: 3.2em;
        }
    }
    </style>
'''
st.markdown(text_media_query3 + instructions_text, unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
with col1:
    text = '<p class="heading_text" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 1em; font-weight: bold;">Sector</span></p>'
    text_media_query4 = '''
    <style>
    @media (max-width: 600px) {
        p.heading_text {
            font-size: 3.2em;
        }
    }
    </style>
'''
    st.markdown(text_media_query4 + text, unsafe_allow_html=True)
    sector_options = [""] + sorted(st.session_state.df_input['sector'].apply(str).unique())
    st.selectbox(label="", label_visibility="collapsed", options=sector_options,
                                format_func=lambda x: "Select Sector" if x == "" else x, key="user_sector", on_change=change_callback1)

    with col2:
        text = '<p class="heading_text" style="margin-bottom: 0em;"> <span style="font-family:sans-serif; color:#25476A; font-size: 1em; font-weight: bold;">Country</span></p>'
        st.markdown(text_media_query4 + text, unsafe_allow_html=True)
        country_options = [""] + sorted(st.session_state.df_input.loc[(st.session_state.df_input['sector'] == st.session_state.user_sector), 'country'].apply(str).unique())
        st.selectbox(label="", label_visibility="collapsed", options=country_options,
                     format_func=lambda x: "Select Country" if x == "" else x,  key="user_country", on_change=change_callback1)    
    with col3:
        text = '<p class="heading_text" style="margin-bottom: 0em;"> <span style="font-family:sans-serif; color:#25476A; font-size: 1em; font-weight: bold;">Entity Name</span></p>'
        st.markdown(text_media_query4 + text, unsafe_allow_html=True)
        entity_name_options = [""] + sorted(st.session_state.df_input.loc[(st.session_state.df_input['sector'] == st.session_state.user_sector) & (st.session_state.df_input['country'] == st.session_state.user_country), 'entity_name'].apply(str).unique())
        st.selectbox(label="", label_visibility="collapsed", options=entity_name_options,
                     format_func=lambda x: "Select Entity Name" if x == "" else x,  key="user_entity_name", on_change=change_callback1)
with col4:
    text = '<p class="heading_text" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 1em; font-weight: bold;">Reporting Period</span></p>'
    st.markdown(text_media_query4 + text, unsafe_allow_html=True)
    reporting_period_options = [""] + sorted(
        st.session_state.df_input.loc[(st.session_state.df_input['sector'] == st.session_state.user_sector) & (st.session_state.df_input['country'] == st.session_state.user_country) & (st.session_state.df_input['entity_name'] == st.session_state.user_entity_name), 'period'].apply(str).unique(), reverse=True)
    st.selectbox(label="", label_visibility="collapsed", options=reporting_period_options,
                   format_func=lambda x: "Select Reporting Period" if x == "" else x,  key="user_reporting_period", on_change=change_callback1)

 
    
with col5:
    
    def handle_button_click(button_value):
        if button_value == "submit1_button":
            st.write("Success")
        elif button_value == "cancel1_button":
            st.write("Cancel")
    
    button_css2 = """
    <style>
        :root {
            --base-font-size: 1vw;  /* Define your base font size here */
        }  
        .button-div2 {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            width: 200%;
            gap: 2em;  /* Convert 20px to em units */
            margin-top: 1.6em;  /* Add top margin */
        }
        .button2 {
            background-color: #25476A;
            border-color: #FAFAFA;
            border-width: 0.1875em;  /* Convert 3px to em units */
            border-radius: 0.1875em;  /* Convert 3px to em units */
            color: #FAFAFA;
            padding: 0em 0em;  /* Adjust padding as per your preference */
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 0.8em;  /* Convert 16px to em units */
            margin: 0em;  /* Adjust margin as per your preference */
            cursor: pointer;
            width: 5em;
            height: 2em;
        }
        .button2:hover {
            background-color: #b8d9e8;
            border-color: #25476A;
            color: #25476A;
         }
        @media screen and (max-width: 600px) {
        .button-div2 {
            width: 100%;  /* Set width to 100% for full width on smaller screens */
            justify-content: center;  /* Center align items on smaller screens */
            gap: 50em;
            margin-top: 0em;  /* Add top margin */
        }
        .button2 {
            border-width: 0.1875em;  /* Convert 3px to em units */
            border-radius: 0.1875em;  /* Convert 3px to em units */
            font-size: 4em;  /* Convert 16px to em units */
            width: 5em;
            height: 2em;
        }
        }
    </style>
    <div class="button-div2">
        <button class="button2" type="button" value="submit1_button" onclick="handleButtonClick('submit1_button')">Run</button>
        <button class="button2" type="button" value="cancel1_button" onclick="handleButtonClick('cancel1_button')">Cancel</button>
    </div>
    """
    st.markdown(button_css2, unsafe_allow_html=True)
    analysis_options = ["", "Run Manual Analysis", "Run Simulation Analysis"]
    
    st.markdown(
        """
    <script>
    function handleButtonClick(buttonValue) {
        const payload = {
            event: 'button_click',
            buttonValue: buttonValue
        };
        // Send the payload to the Streamlit backend
        Streamlit.connection.sendMessage(payload);
    }
    </script>
    """,
        unsafe_allow_html=True
    )

    # Handle the button click event
    if "button_click" in st.session_state:
        button_value = st.session_state.button_click["buttonValue"]
        handle_button_click(button_value)

#    submit1_button = st.button("Run", key="1", on_click=reset2)
#    cancel1_button = st.button("Cancel", key="cancel1", on_click=reset1)

  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#if submit1_button:
#    if st.session_state.user_sector == "" or if st.session_state.user_country == "" or st.session_state.user_entity_name == "" or st.session_state.user_reporting_period == "":
#        col1, col2, col3 = st.columns([1, 4, 1])
#        st.text("")
#        st.text("")
#        with col2:
#            st.error("**Error**: please complete selection.")
#    else:
#        st.session_state.submit1_confirm = True

if st.session_state.submit1_confirm == True:
    st.text("")
    st.text("")
    subtext1A = '<p class="subtext" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 2em;">Analysis Details</span></p>'
    st.markdown(text_media_query2 + subtext1A, unsafe_allow_html=True)
    st.markdown(line_media_query2 + line2, unsafe_allow_html=True)
    instructions_text = '<p class="instructions_text" style="margin-top: -1.8em; margin-bottom: 0.8em; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 1em;">Use the dropdown menu to select the type of analysis you want to perform. Click "Run" once you have made your selection or click "Cancel" to reset.</span></p>'
    st.markdown(text_media_query3 + instructions_text, unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6 = st.columns([1, 0.1, 3.8, 0.1, 0.5, 0.5])
    with col1:
        text = '<p class="heading_text" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 1em; font-weight: bold;">Analysis Type</span></p>'
        st.markdown(text_media_query4 + text, unsafe_allow_html=True)
        st.selectbox(label="", label_visibility="collapsed", options=analysis_options,
                   format_func=lambda x: "Select Analysis Type" if x == "" else x,  key="user_whatif")
    with col3:
        st.text("")
        st.text("")
        st.text("")
        information_text = st.empty()
        text1 = '''
    <p class="text1" style="margin-top: -2.2em; margin-bottom: 1.25em; text-align: justify;"><span style="color: #25476A; background-color: rgba(3, 169, 244, 0.2); border-radius: 0.375em; padding-left: 0.75em; padding-right: 0.75em; padding-top: 0.5em; padding-bottom: 0.5em; font-family: sans-serif; font-size: 1em; font-weight: bold; display: block; width: 100%; border: 0.1875em solid #25476A;">Manual analysis of financial statements involves predicting a company&apos;s financial performance based on expert judgement applied to financial drivers, providing valuable insights into a company&apos;s current financial position and trends by exploring "what-if" scenarios.</span></p>
'''
        text2 = '''
    <p class="text1" style="margin-top: -2.2em; margin-bottom: 1.25em; text-align: justify;"><span style="color: #25476A; background-color: rgba(3, 169, 244, 0.2); border-radius: 0.375em; padding-left: 0.75em; padding-right: 0.75em; padding-top: 0.5em; padding-bottom: 0.5em; font-family: sans-serif; font-size: 1em; font-weight: bold; display: block; width: 100%; border: 0.1875em solid #25476A;">Simulation analysis of financial statements involves a model that simulates a company&apos;s financial performance under multiple scenarios, assessing the risks and opportunities associated with different potential outcomes.</span></p>
'''
        text_media_query5 = '''
            <style>
            @media (max-width: 600px) {
                p.text1 {
                    font-size: 3.2em;
                    border-width: 0.5em;
                    position: relative;
                    top: -3em;
                }
            }
            </style>
        '''

        if st.session_state.user_whatif == "":
            information_text.empty()
        if st.session_state.user_whatif == "Run Manual Analysis":
            information_text.empty()
            information_text.markdown(text_media_query5 + text1, unsafe_allow_html=True)
        if st.session_state.user_whatif == "Run Simulation Analysis":
            information_text.empty()
            information_text.markdown(text_media_query5 + text2, unsafe_allow_html=True)
    with col5:
        st.text("")
        st.text("")
        submit2_button = st.button("Run", key="2")
    with col6:
        st.text("")
        st.text("")
        cancel2_button = st.button("Cancel", key="cancel2", on_click=reset2)
    if submit2_button:
        if "user_whatif_simulated_values" in st.session_state:
            del st.session_state.user_whatif_simulated_values
        st.session_state.next1_confirm = False
        st.session_state.next2_confirm = False
        st.session_state.submit3_confirm = False
        st.session_state.simulation_run_confirm = False
        st.session_state.next3_confirm = False
        st.session_state.next4_confirm = False
        if st.session_state.user_whatif == "":
            col1, col2, col3 = st.columns([1, 4, 1])
            st.text("")
            st.text("")
            with col2:
                st.error("**Error**: please complete selection.")
        else:
            st.session_state.submit2_confirm = True
    if (st.session_state.submit2_confirm == True and submit2_button) or st.session_state.manual_analysis_confirm == True:
        if st.session_state.user_whatif == "Run Manual Analysis":
            st.text("")
            manual_analysis.app()
    if (st.session_state.submit2_confirm == True and submit2_button) or st.session_state.simulation_analysis_confirm == True:
        if st.session_state.user_whatif == "Run Simulation Analysis":
            st.text("")
            simulation_analysis.app()

footer = """
<style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #25476A;
        color: #FAFAFA;
        text-align: left;
        padding: 1px;
        padding-left: 30px;
        padding-right: 30px;
    }
    .left-column {
        float: left;
        width: 15%;
        padding: 10px;
    }
    .middle-column {
        float: left;
        width: 85%;
        padding: 10px;
    }
    .clear {
        clear: both;
    }
    .content-container {
        /*padding-bottom: 100px;*/
#        /*margin-bottom: 100px;*/
    }
</style>

<div class="content-container">
    <div class="footer">
        <div class="left-column">
            <b>Copyright 2023 Comrate<br>All rights reserved</b>
        </div>
        <div class="middle-column">
            <b><strong>Disclaimer:</strong> All simulation and machine learning models employed in this application are based on historical financial data and are subject to uncertainties and risks. Past performance is not indicative of future results. All models may exhibit inherent limitations associated with their predictive accuracy.</b>
        </div>
        <div class="clear"></div>
    </div>
</div>
"""

#st.markdown(footer, unsafe_allow_html=True)

footer2 = """
    <style>
    .footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-image: url('data:image/png;base64,{}');
        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;
        opacity: 1;
        color: #FAFAFA;
        text-align: justify;
        padding: 1px;
        padding-left: 30px;
        padding-right: 30px;
    }}
    .left-column {{
        float: left;
        width: 15%;
        padding: 10px;
    }}
    .middle-column {{
        float: left;
        width:85%;
        padding: 10px;
    }}
    .clear {{
        clear: both;
    }}
    .content-container {{
        /*padding-bottom: 100px;*/
#        /*margin-bottom: 100px;*/
    }}
</style>

<div class="content-container">
    <div class="footer">
        <div class="left-column">
            <b>Copyright 2023 Comrate<br>All rights reserved</b>
        </div>
        <div class="middle-column">
            <b><strong>DISCLAIMER:</strong> All simulation and machine learning models employed in this application are based on historical financial data and are subject to uncertainties and risks. Past performance is not indicative of future results. All models may exhibit inherent limitations associated with their predictive accuracy.</b>
        </div>
        <div class="clear"></div>
    </div>
</div>
"""

footer2 = """
    <style>
        :root {{
            --base-font-size: 1vw;  /* Define your base font size here */
        }}
    
        .footer {{
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-image: url('data:image/png;base64,{}');
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
            filter: brightness(0.9) saturate(0.8);
            opacity: 1;
            color: #FAFAFA;
            text-align: justify;
            padding: 0em;
            padding-left: 1.875em;  /* Convert 30px to em units */
            padding-right: 1.875em;  /* Convert 30px to em units */
        }}
    
        .left-column {{
            font-size: 0.8em;
            float: left;
            width: 15%;
            padding: 0.625em;  /* Convert 10px to em units */
        }}
    
        .middle-column {{
            font-size: 0.8em;
            float: left;
            width: 85%;
            padding: 0.625em;  /* Convert 10px to em units */
        }}
    
        .clear {{
            clear: both;
        }}
    
        .content-container {{
            /*padding-bottom: 100px;*/
        }}
     @media screen and (max-width: 600px) {{
        .footer {{
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 0.8em;  /* Adjust padding for smaller screens */
       }}

        .left-column {{
            width: 100%;  /* Set width to 100% for full width on smaller screens */
            justify-content: center;
            text-align: center;
            display: flex;
            align-items: center;
            float: left;
            margin-bottom: 0em;  /* Adjust margin for smaller screens */
        }}
        .left-column {{
            font-size: 2.4em;
            float: left;
            width: 15%;
            padding: 0.625em;
            margin-bottom: 0.5em;
        }}
    
        .middle-column {{
            font-size: 2.4em;
            float: left;
            width: 85%;
            padding: 0.625em;
            margin-bottom: 0em;
        }}
    }}
    </style>
    
    <div class="content-container">
        <div class="footer">
            <div class="left-column">
                <b>&copy; 2023 Comrate<br>All rights reserved</b>
            </div>
            <div class="middle-column">
                <b><strong>DISCLAIMER:</strong> All simulation and machine learning models employed in this application are based on historical financial data and are subject to uncertainties and risks. Past performance is not indicative of future results. All models may exhibit inherent limitations associated with their predictive accuracy.</b>
            </div>
            <div class="clear"></div>
        </div>
    </div>
"""

image_file_path = "images/digital_background_update2.jpg"
with open(image_file_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

st.markdown(footer2.format(encoded_string), unsafe_allow_html=True)


footer3 = """
    <style>
    .footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-image: url('data:image/png;base64,{}');
        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;  
        filter: brightness(0.9) saturate(0.8);      
        opacity: 1;
        color: #FAFAFA;
        text-align: left;
        padding: 1px;
        padding-left: 30px;
        padding-right: 30px;
    }}
        .left-column {{
            float: left;
            width: 12%;
            padding: 10px;
        }}
        .middle1-column {{
            float: left;
            width: 78%;
            padding: 10px;
        }}
        .middle2-column {{
            float: left;
            width: 5%;
            padding-top: 23px;
            padding-bottom: 10px;
            padding-left: 5px;
            padding-right: 5px;
            text-align: right;     
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-end;
        }}
        .right-column {{
            float: left;
            width: 5%;
            padding: 10px;
        }}
        .right-column img {{
            max-width: 120%;
            display: inline-block;
            vertical-align: middle;

        }}
        .right-column img:hover {{
        filter: brightness(0.6) saturate(1.2) hue-rotate(20deg);
        }}
        .clear {{
            clear: both;
        }}
    </style>

    <div class="footer">
        <div class="left-column">
            <b>Copyright 2023 Comrate<br>All rights reserved</b>
        </div>
        <div class="middle1-column">
            <b><strong>Disclaimer:</strong> All simulation and machine learning models employed in this application are based on historical financial data and are subject to uncertainties and risks. Past performance is not indicative of future results. All models may exhibit inherent limitations associated with their predictive accuracy.</b>
        </div>
        <div class="middle2-column">
            <b>Created by</b>
        </div>
        <div class="right-column">        
            <a href="https://oxbrainsolutions.com">
                <img src="data:image/png;base64,{}" class="img-fluid" alt="oxbrain_logo" width="90%">
            </a>
            </div>
        </div>
        <div class="clear"></div>
    </div>
"""
#image_file_path = "images/digital_background_update2.jpg"
#with open(image_file_path, "rb") as image_file:
#    encoded_string = base64.b64encode(image_file.read()).decode()

#st.markdown(footer3.format(encoded_string, img_to_bytes("images/oxbrain_logo_trans.png")), unsafe_allow_html=True)

