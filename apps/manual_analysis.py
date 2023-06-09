import streamlit as st
import pandas as pd
import numpy as np
import pathlib
import base64
import matplotlib.colors as clr
import plotly.graph_objects as go
import plotly.subplots as sp
from apps.functions import get_default_fields, run_whatif, highlight_diff_by_row, FileDownloader, MultiFileDownloader

marker_spinner_css = """
<style>
    #spinner-container-marker {
        display: flex;
        align-items: center;
        justify-content: center;
        position: fixed;
        top: 0%;
        left: 0%;
        transform: translate(54%, 0%);
        width: 100%;
        height: 100%;
        z-index: 9999;
    }

    .marker0 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 0 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 0 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 0 / 50))), calc(5em * sin(2 * 3.14159 * 0 / 50)));        
    }
    
    .marker1 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 1 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 1 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 1 / 50))), calc(5em * sin(2 * 3.14159 * 1 / 50)));
    }
    
    .marker2 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 2 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 2 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 2 / 50))), calc(5em * sin(2 * 3.14159 * 2 / 50)));
    }
    
    .marker3 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 3 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 3 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 3 / 50))), calc(5em * sin(2 * 3.14159 * 3 / 50)));
    }
    
    .marker4 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 4 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 4 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 4 / 50))), calc(5em * sin(2 * 3.14159 * 4 / 50)));
    }
    
    .marker5 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 5 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 5 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 5 / 50))), calc(5em * sin(2 * 3.14159 * 5 / 50)));
    }
    
    .marker6 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 6 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 6 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 6 / 50))), calc(5em * sin(2 * 3.14159 * 6 / 50)));
    }
    
    .marker7 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 7 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 7 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 7 / 50))), calc(5em * sin(2 * 3.14159 * 7 / 50)));
    }
    
    .marker8 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 8 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 8 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 8 / 50))), calc(5em * sin(2 * 3.14159 * 8 / 50)));
    }
    
    .marker9 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 9 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 9 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 9 / 50))), calc(5em * sin(2 * 3.14159 * 9 / 50)));
    }
    
    .marker10 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 10 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 10 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 10 / 50))), calc(5em * sin(2 * 3.14159 * 10 / 50)));
    }
    
    .marker11 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 11 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 11 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 11 / 50))), calc(5em * sin(2 * 3.14159 * 11 / 50)));
    }
    
    .marker12 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 12 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 12 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 12 / 50))), calc(5em * sin(2 * 3.14159 * 12 / 50)));
    }
    
    .marker13 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 13 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 13 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 13 / 50))), calc(5em * sin(2 * 3.14159 * 13 / 50)));
    }
    
    .marker14 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 14 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 14 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 14 / 50))), calc(5em * sin(2 * 3.14159 * 14 / 50)));
    }
    
    .marker15 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 15 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 15 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 15 / 50))), calc(5em * sin(2 * 3.14159 * 15 / 50)));
    }
    
    .marker16 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 16 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 16 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 16 / 50))), calc(5em * sin(2 * 3.14159 * 16 / 50)));
    }
    
    .marker17 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 17 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 17 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 17 / 50))), calc(5em * sin(2 * 3.14159 * 17 / 50)));
    }
    
    .marker18 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 18 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 18 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 18 / 50))), calc(5em * sin(2 * 3.14159 * 18 / 50)));
    }
    
    .marker19 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 19 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 19 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 19 / 50))), calc(5em * sin(2 * 3.14159 * 19 / 50)));
    }
    
    .marker20 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 20 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 20 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 20 / 50))), calc(5em * sin(2 * 3.14159 * 20 / 50)));
    }
    
    .marker21 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 21 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 21 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 21 / 50))), calc(5em * sin(2 * 3.14159 * 21 / 50)));
    }
    
    .marker22 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 22 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 22 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 22 / 50))), calc(5em * sin(2 * 3.14159 * 22 / 50)));
    }
    
    .marker23 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 23 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 23 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 23 / 50))), calc(5em * sin(2 * 3.14159 * 23 / 50)));
    }
    
    .marker24 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 24 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 24 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 24 / 50))), calc(5em * sin(2 * 3.14159 * 24 / 50)));
    }
    
    .marker25 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 25 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 25 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 25 / 50))), calc(5em * sin(2 * 3.14159 * 25 / 50)));
    }
    
    .marker26 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 26 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 26 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 26 / 50))), calc(5em * sin(2 * 3.14159 * 26 / 50)));
    }
    
    .marker27 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 27 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 27 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 27 / 50))), calc(5em * sin(2 * 3.14159 * 27 / 50)));
    }
    
    .marker28 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 28 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 28 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 28 / 50))), calc(5em * sin(2 * 3.14159 * 28 / 50)));
    }
    
    .marker29 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 29 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 29 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 29 / 50))), calc(5em * sin(2 * 3.14159 * 29 / 50)));
    }
    
    .marker30 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 30 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 30 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 30 / 50))), calc(5em * sin(2 * 3.14159 * 30 / 50)));
    }
    
    .marker31 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 31 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 31 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 31 / 50))), calc(5em * sin(2 * 3.14159 * 31 / 50)));
    }
    
    .marker32 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 32 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 32 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 32 / 50))), calc(5em * sin(2 * 3.14159 * 32 / 50)));
    }
    
    .marker33 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 33 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 33 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 33 / 50))), calc(5em * sin(2 * 3.14159 * 33 / 50)));
    }
    
    .marker34 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 34 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 34 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 34 / 50))), calc(5em * sin(2 * 3.14159 * 34 / 50)));
    }
    
    .marker35 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 35 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 35 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 35 / 50))), calc(5em * sin(2 * 3.14159 * 35 / 50)));
    }
    
    .marker36 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 36 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 36 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 36 / 50))), calc(5em * sin(2 * 3.14159 * 36 / 50)));
    }
    
    .marker37 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 37 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 37 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 37 / 50))), calc(5em * sin(2 * 3.14159 * 37 / 50)));
    }
    
    .marker38 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 38 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 38 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 38 / 50))), calc(5em * sin(2 * 3.14159 * 38 / 50)));
    }
    
    .marker39 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 39 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 39 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 39 / 50))), calc(5em * sin(2 * 3.14159 * 39 / 50)));
    }
    
    .marker40 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 40 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 40 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 40 / 50))), calc(5em * sin(2 * 3.14159 * 40 / 50)));
    }
    
    .marker41 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 41 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 41 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 41 / 50))), calc(5em * sin(2 * 3.14159 * 41 / 50)));
    }
    
    .marker42 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 42 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 42 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 42 / 50))), calc(5em * sin(2 * 3.14159 * 42 / 50)));
    }
    
    .marker43 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 43 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 43 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 43 / 50))), calc(5em * sin(2 * 3.14159 * 43 / 50)));
    }
    
    .marker44 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 44 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 44 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 44 / 50))), calc(5em * sin(2 * 3.14159 * 44 / 50)));
    }
    
    .marker45 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 45 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 45 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 45 / 50))), calc(5em * sin(2 * 3.14159 * 45 / 50)));
    }
    
    .marker46 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 46 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 46 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 46 / 50))), calc(5em * sin(2 * 3.14159 * 46 / 50)));
    }
    
    .marker47 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 47 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 47 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 47 / 50))), calc(5em * sin(2 * 3.14159 * 47 / 50)));
    }
    
    .marker48 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 48 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 48 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 48 / 50))), calc(5em * sin(2 * 3.14159 * 48 / 50)));
    }
    
    .marker49 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 5s linear infinite;
        animation-delay: calc(5s * 49 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 49 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 49 / 50))), calc(5em * sin(2 * 3.14159 * 49 / 50)));
    }

    @keyframes animateBlink {
    0% {
        background: #9500FF;
    }
    25% {
        background: rgba(0, 0, 0, 0);
    }   
}
@media (max-width: 1024px) {
    #spinner-container-marker {
        transform: translate(57.4%, 0%);
    }
    .marker0 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 0 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 0 / 50))), calc(10em * sin(2 * 3.14159 * 0 / 50)));
    }
    .marker1 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 1 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 1 / 50))), calc(10em * sin(2 * 3.14159 * 1 / 50)));
    }
    .marker2 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 2 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 2 / 50))), calc(10em * sin(2 * 3.14159 * 2 / 50)));
    }
    .marker3 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 3 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 3 / 50))), calc(10em * sin(2 * 3.14159 * 3 / 50)));
    }
    .marker4 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 4 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 4 / 50))), calc(10em * sin(2 * 3.14159 * 4 / 50)));
    }
    .marker5 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 5 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 5 / 50))), calc(10em * sin(2 * 3.14159 * 5 / 50)));
    }
    .marker6 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 6 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 6 / 50))), calc(10em * sin(2 * 3.14159 * 6 / 50)));
    }
    .marker7 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 7 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 7 / 50))), calc(10em * sin(2 * 3.14159 * 7 / 50)));
    }
    .marker8 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 8 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 8 / 50))), calc(10em * sin(2 * 3.14159 * 8 / 50)));
    }
    .marker9 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 9 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 9 / 50))), calc(10em * sin(2 * 3.14159 * 9 / 50)));
    }
    .marker10 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 10 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 10 / 50))), calc(10em * sin(2 * 3.14159 * 10 / 50)));
    }
    .marker11 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 11 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 11 / 50))), calc(10em * sin(2 * 3.14159 * 11 / 50)));
    }
    .marker12 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 12 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 12 / 50))), calc(10em * sin(2 * 3.14159 * 12 / 50)));
    }
    .marker13 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 13 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 13 / 50))), calc(10em * sin(2 * 3.14159 * 13 / 50)));
    }
    .marker14 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 14 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 14 / 50))), calc(10em * sin(2 * 3.14159 * 14 / 50)));
    }
    .marker15 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 15 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 15 / 50))), calc(10em * sin(2 * 3.14159 * 15 / 50)));
    }
    .marker16 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 16 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 16 / 50))), calc(10em * sin(2 * 3.14159 * 16 / 50)));
    }
    .marker17 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 17 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 17 / 50))), calc(10em * sin(2 * 3.14159 * 17 / 50)));
    }
    .marker18 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 18 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 18 / 50))), calc(10em * sin(2 * 3.14159 * 18 / 50)));
    }
    .marker19 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 19 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 19 / 50))), calc(10em * sin(2 * 3.14159 * 19 / 50)));
    }
    .marker20 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 20 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 20 / 50))), calc(10em * sin(2 * 3.14159 * 20 / 50)));
    }    
    .marker21 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 21 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 21 / 50))), calc(10em * sin(2 * 3.14159 * 21 / 50)));
    }
    .marker22 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 22 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 22 / 50))), calc(10em * sin(2 * 3.14159 * 22 / 50)));
    }
    .marker23 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 23 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 23 / 50))), calc(10em * sin(2 * 3.14159 * 23 / 50)));
    }
    .marker24 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 24 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 24 / 50))), calc(10em * sin(2 * 3.14159 * 24 / 50)));
    }
    .marker25 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 25 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 25 / 50))), calc(10em * sin(2 * 3.14159 * 25 / 50)));
    }
    .marker26 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 26 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 26 / 50))), calc(10em * sin(2 * 3.14159 * 26 / 50)));
    }
    .marker27 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 27 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 27 / 50))), calc(10em * sin(2 * 3.14159 * 27 / 50)));
    }
    .marker28 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 28 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 28 / 50))), calc(10em * sin(2 * 3.14159 * 28 / 50)));
    }
    .marker29 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 29 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 29 / 50))), calc(10em * sin(2 * 3.14159 * 29 / 50)));
    }
    .marker30 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 30 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 30 / 50))), calc(10em * sin(2 * 3.14159 * 30 / 50)));
    }
    .marker31 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 31 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 31 / 50))), calc(10em * sin(2 * 3.14159 * 31 / 50)));
    }
    .marker32 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 32 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 32 / 50))), calc(10em * sin(2 * 3.14159 * 32 / 50)));
    }
    .marker33 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 33 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 33 / 50))), calc(10em * sin(2 * 3.14159 * 33 / 50)));
    }
    .marker34 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 34 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 34 / 50))), calc(10em * sin(2 * 3.14159 * 34 / 50)));
    }
    .marker35 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 35 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 35 / 50))), calc(10em * sin(2 * 3.14159 * 35 / 50)));
    }
    .marker36 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 36 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 36 / 50))), calc(10em * sin(2 * 3.14159 * 36 / 50)));
    }
    .marker37 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 37 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 37 / 50))), calc(10em * sin(2 * 3.14159 * 37 / 50)));
    }
    .marker38 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 38 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 38 / 50))), calc(10em * sin(2 * 3.14159 * 38 / 50)));
    }
    .marker39 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 39 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 39 / 50))), calc(10em * sin(2 * 3.14159 * 39 / 50)));
    }
    .marker40 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 40 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 40 / 50))), calc(10em * sin(2 * 3.14159 * 40 / 50)));
    }
    .marker41 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 41 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 41 / 50))), calc(10em * sin(2 * 3.14159 * 41 / 50)));
    }
    .marker42 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 42 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 42 / 50))), calc(10em * sin(2 * 3.14159 * 42 / 50)));
    }
    .marker43 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 43 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 43 / 50))), calc(10em * sin(2 * 3.14159 * 43 / 50)));
    }
    .marker44 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 44 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 44 / 50))), calc(10em * sin(2 * 3.14159 * 44 / 50)));
    }
    .marker45 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 45 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 45 / 50))), calc(10em * sin(2 * 3.14159 * 45 / 50)));
    }
    .marker46 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 46 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 46 / 50))), calc(10em * sin(2 * 3.14159 * 46 / 50)));
    }
    .marker47 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 47 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 47 / 50))), calc(10em * sin(2 * 3.14159 * 47 / 50)));
    }
    .marker48 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 48 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 48 / 50))), calc(10em * sin(2 * 3.14159 * 48 / 50)));
    }
    .marker49 {
        width: 5em;
        height: 1em;
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 49 / 50)) translate(calc(10em * (1 - cos(2 * 3.14159 * 49 / 50))), calc(10em * sin(2 * 3.14159 * 49 / 50)));
    }
</style>

<div id="spinner-container-marker">
    <div class="marker0"></div>
    <div class="marker1"></div>
    <div class="marker2"></div>
    <div class="marker3"></div>
    <div class="marker4"></div>
    <div class="marker5"></div>
    <div class="marker6"></div>
    <div class="marker7"></div>
    <div class="marker8"></div>
    <div class="marker9"></div>
    <div class="marker10"></div>
    <div class="marker11"></div>
    <div class="marker12"></div>
    <div class="marker13"></div>
    <div class="marker14"></div>
    <div class="marker15"></div>
    <div class="marker16"></div>
    <div class="marker17"></div>
    <div class="marker18"></div>
    <div class="marker19"></div>
    <div class="marker20"></div>
    <div class="marker21"></div>
    <div class="marker22"></div>
    <div class="marker23"></div>
    <div class="marker24"></div>
    <div class="marker25"></div>
    <div class="marker26"></div>
    <div class="marker27"></div>
    <div class="marker28"></div>
    <div class="marker29"></div>
    <div class="marker30"></div>
    <div class="marker31"></div>
    <div class="marker32"></div>
    <div class="marker33"></div>
    <div class="marker34"></div>
    <div class="marker35"></div>
    <div class="marker36"></div>
    <div class="marker37"></div>
    <div class="marker38"></div>
    <div class="marker39"></div>
    <div class="marker40"></div>
    <div class="marker41"></div>
    <div class="marker42"></div>
    <div class="marker43"></div>
    <div class="marker44"></div>
    <div class="marker45"></div>
    <div class="marker46"></div>
    <div class="marker47"></div>
    <div class="marker48"></div>
    <div class="marker49"></div>
</div>
"""

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

    @media (max-width: 1024px) {
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

spinner_image_css = """
<style>
    .image-container {{
        display: inline-block;
        width: 25%;
        text-align: center;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 9999;
    }}

    @media (max-width: 1024px) {{
        .image-container {{
            width: 50%;
        }}
    }}
</style>
<div class="image-container">
    <img src="data:image/png;base64,{}" class="img-fluid" alt="logo" width="30%">
</div>
"""

def img_to_bytes(img_path):
    img_bytes = pathlib.Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def get_financials(datafame, user_entity_name, user_period):
    entity_financials = datafame.loc[
        (datafame['entity_name'] == user_entity_name) & (datafame['period'] == user_period)]
    return entity_financials

def app():
    line1 = '<hr class="line1" style="height:0.3em; border:0em; background-color: #03A9F4; margin-top: 0em;">'
    line2 = '<hr class="line2" style="height:0.1875em; border:0em; background-color: #25476A; margin-top: 0.2em;">'
    line_media_query1 = '''
        <style>
        @media (max-width: 1024px) {
            .line1 {
                padding: 0.5em;
            }
        }
        </style>
    '''
    line_media_query2 = '''
        <style>
        @media (max-width: 1024px) {
            .line2 {
                padding: 0.3em;
                margin-bottom: 8em;
            }
        }
        </style>
    '''
    

    arrows_image_css = """
    <style>
        .image-container {{
            display: inline-block;
            width: 25%;
            text-align: center;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 9999;
        }}

        @media (max-width: 1024px) {{
            .image-container {{
                width: 50%;
            }}
        }}
    </style>
    <div class="image-container">
        <img src="data:image/png;base64,{}" class="img-fluid" alt="logo" width="30%">
    </div>
    """

    st.markdown(arrows_image_css.format(img_to_bytes("images/arrows.png")), unsafe_allow_html=True)
    
    st.session_state.default_whatif_sales_revenue_growth_user_out, st.session_state.default_whatif_cost_of_goods_sold_margin_user_out, st.session_state.default_whatif_sales_general_and_admin_expenses_user_out, st.session_state.default_whatif_research_and_development_expenses_user_out, st.session_state.default_whatif_depreciation_and_amortization_expenses_sales_user_out, st.session_state.default_whatif_depreciation_and_amortization_split_user_out, st.session_state.default_whatif_interest_rate_user_out, st.session_state.default_whatif_tax_rate_user_out, st.session_state.default_whatif_dividend_payout_ratio_user_out, st.session_state.default_whatif_accounts_receivable_days_user_out, st.session_state.default_whatif_inventory_days_user_out, st.session_state.default_whatif_capital_expenditure_sales_user_out, st.session_state.default_whatif_capital_expenditure_user_out, st.session_state.default_whatif_capital_expenditure_indicator_user_out, st.session_state.default_whatif_tangible_intangible_split_user_out, st.session_state.default_whatif_accounts_payable_days_user_out, st.session_state.default_whatif_sale_of_equity_user_out, st.session_state.default_whatif_repurchase_of_equity_user_out, st.session_state.default_whatif_proceeds_from_issuance_of_debt_user_out, st.session_state.default_whatif_repayments_of_long_term_debt_user_out, st.session_state.default_whatif_notes_other_split_user_out = get_default_fields(select_user_entity_name=st.session_state.user_entity_name, select_user_period=st.session_state.user_reporting_period)
    st.session_state.df_income_statement_out, st.session_state.df_cash_flow_statement_out, st.session_state.df_balance_sheet_statement_out = run_whatif(select_user_entity_name=st.session_state.user_entity_name, select_user_period=st.session_state.user_reporting_period, select_user_whatif_sales_revenue_growth=st.session_state.default_whatif_sales_revenue_growth_user_out,
select_user_whatif_cost_of_goods_sold_margin=st.session_state.default_whatif_cost_of_goods_sold_margin_user_out, select_user_whatif_sales_general_and_admin_expenses=st.session_state.default_whatif_sales_general_and_admin_expenses_user_out, select_user_whatif_research_and_development_expenses=st.session_state.default_whatif_research_and_development_expenses_user_out, select_user_whatif_depreciation_and_amortization_expenses_sales=st.session_state.default_whatif_depreciation_and_amortization_expenses_sales_user_out, select_user_whatif_depreciation_and_amortization_split=st.session_state.default_whatif_depreciation_and_amortization_split_user_out, select_user_whatif_interest_rate=st.session_state.default_whatif_interest_rate_user_out, select_user_whatif_tax_rate=st.session_state.default_whatif_tax_rate_user_out, select_user_whatif_dividend_payout_ratio=st.session_state.default_whatif_dividend_payout_ratio_user_out,select_user_whatif_accounts_receivable_days=st.session_state.default_whatif_accounts_receivable_days_user_out, select_user_whatif_inventory_days=st.session_state.default_whatif_inventory_days_user_out, select_user_whatif_capital_expenditure_sales=st.session_state.default_whatif_capital_expenditure_sales_user_out, select_user_whatif_capital_expenditure=st.session_state.default_whatif_capital_expenditure_user_out, select_user_whatif_capital_expenditure_indicator=st.session_state.default_whatif_capital_expenditure_indicator_user_out, select_user_whatif_tangible_intangible_split=st.session_state.default_whatif_tangible_intangible_split_user_out, select_user_whatif_accounts_payable_days=st.session_state.default_whatif_accounts_payable_days_user_out, select_user_whatif_sale_of_equity=st.session_state.default_whatif_sale_of_equity_user_out, select_user_whatif_repurchase_of_equity=st.session_state.default_whatif_repurchase_of_equity_user_out, select_user_whatif_proceeds_from_issuance_of_debt=st.session_state.default_whatif_proceeds_from_issuance_of_debt_user_out, select_user_whatif_repayments_of_long_term_debt=st.session_state.default_whatif_repayments_of_long_term_debt_user_out, select_user_whatif_notes_other_split=st.session_state.default_whatif_notes_other_split_user_out)

    df_financials = get_financials(st.session_state.df_input, st.session_state.user_entity_name, st.session_state.user_reporting_period)
    spinner.empty()
    spinner_image.empty()
    if st.session_state.df_income_statement_out.empty == False:
        styles = """
        <style>
            .col {
                background-color: #25476A;
                padding-left: 6.25em;
                padding: 1em;
                border: 0.3125em solid #03A9F4;
                border-radius: 0.625em;
                margin: 0;
                padding-left: 1.875em;
                padding-right: 1.875em;
                display: flex;
                align-items: center;
                vertical-align: middle;
            }
            .left {
                text-align: left;
                float: left;
                width: 40%;
                padding-top: 0em;
                padding-bottom: 0em;
            }
            .right {
                text-align: right;
                float: right;
                width: 60%;
                padding-top: 0em;
                padding-bottom: 0em;
            }
            .break-line {
                display: inline;
                white-space: normal;
            }

            @media (max-width: 1024px) {
                .col {
                    border: 0.5em solid #03A9F4;
                    font-size: 2.25em;
                    margin-top: -2em;
                    margin-bottom: 4em;
                }
                .break-line {
                    display: block;
                    white-space: pre-wrap;
                }
            }
        </style>
        """

        st.markdown(styles, unsafe_allow_html=True)
                
            
        styles2 = """
        <style>
            .col2 {
                margin: 0em;
                display: flex;
                align-items: center;
                vertical-align: middle;
                padding-right: 0.875em;
                margin-top: 0em;
                margin-bottom: 0em;
            }
            .left2 {
                text-align: left;
                width: 95%;
                padding-top: 0em;
                padding-bottom: 0em;
            }
            .right2 {
                text-align: right;
                width: 5%;
                padding-top: 0em;
                padding-bottom: 0em;
            }

            /* Tooltip container */
            .tooltip2 {
                position: relative;
                margin-bottom: 0em;
                display: inline-block;
                margin-top: 0em;
            }

            /* Tooltip text */
            .tooltip2 .tooltiptext2 {
                visibility: hidden;
                width: 80em;
                background-color: #b8d9e8;
                color: #25476A;
                text-align: justify;
                font-family: sans-serif;
                display: block; 
                border-radius: 0.375em;
                white-space: normal;
                padding-left: 0.75em;
                padding-right: 0.75em;
                padding-top: 0.5em;
                padding-bottom: 0em;
                border: 0.1875em solid #25476A;

                /* Position the tooltip text */
                position: absolute;
                z-index: 1;
                bottom: 125%;
                transform: translateX(-95%);

                /* Fade in tooltip */
                opacity: 0;
                transition: opacity 0.5s;
            }

            /* Tooltip arrow */
            .tooltip2 .tooltiptext2::after {
                content: "";
                position: absolute;
                top: 100%;
                left: 95.6%;
                border-width: 0.625em;
                border-style: solid;
                border-color: #25476A transparent transparent transparent;
            }

            /* Show the tooltip text when you mouse over the tooltip container */
            .tooltip2:hover .tooltiptext2 {
                visibility: visible;
                opacity: 1;
            }
            /* Change icon color on hover */
            .tooltip2:hover i {
                color: rgba(111, 114, 222, 0.8);
            }   
            /* Set initial icon color */
            .tooltip2 i {
                color: #25476A;
            }
            ul.responsive-ul2 {
                font-size: 0.8em;
            }
            ul.responsive-ul2 li {
                font-size: 1em;
            }

            /* Responsive styles */
            @media (max-width: 1024px) {
               .col2 {
                    padding-right: 1em;
                    margin-top: 0em;
                }
                p.subtext_manual2 {
                    font-size: 2.5em;
                }
            .tooltip2 .tooltiptext2 {
                border-width: 0.6em;
                border-radius: 1.6em;
                width: 98em;
                left: 50%;
            }
            .tooltip2 .tooltiptext2::after {
                border-width: 2em;
                left: 93.5%;
            }
            .tooltip2 {
                
            }
            .tooltip2 i {
                font-size: 8em;
                margin-bottom: 0.2em;
            }
            ul.responsive-ul2 {
                font-size: 3.2em;
            }
            ul.responsive-ul2 li {
                font-size: 1em;
            }
            }
        </style>

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
        """

        st.markdown(styles2, unsafe_allow_html=True)
        
        styles3 = """
        <style>
            .col3 {
                display: flex;
                align-items: center;
                vertical-align: middle;
            }
            .left3 {
                text-align: left;
                float: left;
                width: 60%;
                padding-top: 0em;
                padding-bottom: 0em;
            }
            .right3 {
                text-align: right;
                float: right;
                width: 40%;
                padding-top: 0em;
                padding-bottom: 0em;
            }
            @media (max-width: 1024px) {
                .col3 {
                    font-size: 3.25em;
                    margin-top: -2em;
                }
            }
        </style>
        """

        st.markdown(styles3, unsafe_allow_html=True)

        left_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 2.25em;'>Manual Analysis</span>"
        right_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 2.25em;'>{}<span class='break-line'>&nbsp;&nbsp;&nbsp;{}</span></span>".format(st.session_state.user_entity_name, st.session_state.user_reporting_period)

        html = f"<div class='col'><div class='left'>{left_text}</div><div class='right'>{right_text}</div></div>"
        st.markdown(html, unsafe_allow_html=True)
        st.session_state.manual_analysis_confirm = True
        st.session_state.simulation_analysis_confirm = False        
        
        text1 = '''
    <p class="text1" style="margin-top: 1em; margin-bottom: 1em; text-align: justify;"><span style="color: #25476A; background-color: rgba(3, 169, 244, 0.2); border-radius: 0.375em; padding-left: 0.75em; padding-right: 0.75em; padding-top: 0.5em; padding-bottom: 0.5em; font-family: sans-serif; font-size: 1em; font-weight: bold; display: block; width: 100%; border: 0.1875em solid #25476A;">Manual analysis of financial statements involves predicting a company&apos;s financial performance based on expert judgement applied to financial drivers, providing valuable insights into a company&apos;s current financial position and trends by exploring "what-if" scenarios.</span></p>
'''
        text_media_query_manual1 = '''
            <style>
            @media (max-width: 1024px) {
                p.text1 {
                    font-size: 3.2em;
                    border-width: 0.5em;
                    position: relative;
                    top: -1.5em;
                    margin-bottom: -5em;
                }
            }
            </style>
        '''
        st.markdown(text_media_query_manual1 + text1, unsafe_allow_html=True)

        html2 = """
        <div class="col2">
            <div class="left2">
                <p class="subtext_manual2" style="margin-bottom: 0em;"><span style="font-family: sans-serif; color: #25476A; font-size: 2em;">Income Statement Input Fields</span></p>
            </div>
            <div class="right2">
                <div class="tooltip2">
                    <i class="fas fa-info-circle fa-2x"></i>
                    <span class="tooltiptext2">
                        <ul class="responsive-ul2">
                            Understanding financial metrics and ratios is essential for assessing a company's financial health and making informed investment decisions.                               
                            <li>Sales Growth: A measure of the percentage increase or decrease in revenue over a period of time.</li>
                            <li>COGS Margin: The percentage of revenue that is consumed by the cost of goods sold. It indicates how efficiently a company is using its resources to produce goods.</li>
                            <li>SG&A Expenses: The total operating expenses of a company that are not directly related to production, such as salaries, rent, utilities, and marketing costs.</li>
                            <li>R&D Expenses: The amount of money a company spends on research and development activities. It indicates a company's commitment to innovation and growth.</li>
                            <li>D&A Expenses / Sales: Depreciation and amortization expenses as a percentage of revenue. It indicates how much a company is investing in its long-term assets and how much it is expensing in the current period.</li>
                            <li>D&A Split: The breakdown of depreciation and amortization expenses between tangible assets (D) and intangible assets (A). It indicates how much a company is investing in different types of assets.</li>
                            <li>Interest Rate: The cost of borrowing money. It indicates how much a company is paying to finance its operations and how much debt it has.</li>
                            <li>Tax Rate: The percentage of a company's income that is paid in taxes. It indicates how much income a company is able to retain.</li>
                            <li>Dividend Payout Ratio: The percentage of earnings paid out as dividends to shareholders. It indicates how much a company is returning to its shareholders in the form of dividends and how much it is retaining for reinvestment.</li>                                    
                            These financial metrics and ratios can help provide valuable insight into a company's financial position and performance.
                        </ul>    
                    </span>
                </div>
            </div>
        </div>
        """

        st.markdown(html2, unsafe_allow_html=True)



        st.markdown(line_media_query2 + line2, unsafe_allow_html=True)
        instructions_text = '<p class="instructions_text" style="margin-top: -1.8em; margin-bottom: 0.8em; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 1em;">Enter values for the income statement financial fields based on expectations for the company. Default values provided are based on the prior financial period.</span></p>'
        text_media_query_manual3 = '''
            <style>
            @media (max-width: 1024px) {
                p.instructions_text {
                    font-size: 3.2em;
                }
            }
            </style>
        '''
        st.markdown(text_media_query_manual3 + instructions_text, unsafe_allow_html=True)
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            text = '<p class="heading_text4" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Sales Growth</span></p>'
            text_media_query_manual4 = '''
            <style>
            @media (max-width: 1024px) {
                p.heading_text4 {
                    font-size: 3.5em;
                }
            }
            </style>
            '''
            text_media_query_manual4A = '''
            <style>
            @media (max-width: 1024px) {
                p.heading_text4A {
                    font-size: 3.5em;
                    margin-top: -2em;
                }
            }
            </style>
            '''
            st.markdown(text_media_query_manual4 + text, unsafe_allow_html=True)
            user_whatif_sales_revenue_growth_field = st.empty()
            st.session_state.user_whatif_sales_revenue_growth = user_whatif_sales_revenue_growth_field.number_input(label="", label_visibility="collapsed", min_value=None, max_value=None, step=None, format="%.2f", value=st.session_state.default_whatif_sales_revenue_growth_user_out, key="whatif_manual_1")
            text = '<p class="heading_text4A" style="margin-top: 0em; margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">COGS Margin %</span></p>'
            st.markdown(text_media_query_manual4A + text, unsafe_allow_html=True)
            user_whatif_cost_of_goods_sold_margin_field = st.empty()
            st.session_state.user_whatif_cost_of_goods_sold_margin = user_whatif_cost_of_goods_sold_margin_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=100.00, step=None, format="%.2f", value=st.session_state.default_whatif_cost_of_goods_sold_margin_user_out, key="whatif_manual_2")
        with col2:
            text = '<p class="heading_text4" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">SG&A Expenses $</span></p>'
            st.markdown(text_media_query_manual4 + text, unsafe_allow_html=True)
            user_whatif_sales_general_and_admin_expenses_field = st.empty()
            st.session_state.user_whatif_sales_general_and_admin_expenses = user_whatif_sales_general_and_admin_expenses_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_sales_general_and_admin_expenses_user_out, key="whatif_manual_3")
            text = '<p class="heading_text4A" style="margin-top: 0em; margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">R&D Expenses $</span></p>'
            st.markdown(text_media_query_manual4A + text, unsafe_allow_html=True)
            user_whatif_research_and_development_expenses_field = st.empty()
            st.session_state.user_whatif_research_and_development_expenses = user_whatif_research_and_development_expenses_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_research_and_development_expenses_user_out, key="whatif_manual_4")
        with col3:
            text = '<p class="heading_text4" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">D&A Expenses / Sales %</span></p>'
            st.markdown(text_media_query_manual4 + text, unsafe_allow_html=True)
            user_whatif_depreciation_and_amortization_expenses_sales_field = st.empty()
            st.session_state.user_whatif_depreciation_and_amortization_expenses_sales = user_whatif_depreciation_and_amortization_expenses_sales_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=None, format="%.2f", value=st.session_state.default_whatif_depreciation_and_amortization_expenses_sales_user_out, key="whatif_manual_5")
            text = '<p class="heading_text4A" style="margin-top: 0em; margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">D&A Split %</span></p>'
            st.markdown(text_media_query_manual4A + text, unsafe_allow_html=True)
            user_whatif_depreciation_and_amortization_split_field = st.empty()
            st.session_state.user_whatif_depreciation_and_amortization_split = user_whatif_depreciation_and_amortization_split_field.number_input(label="", label_visibility="collapsed", min_value=0, max_value=100, step=None, format="%i", value=st.session_state.default_whatif_depreciation_and_amortization_split_user_out, key="whatif_manual_6")
        with col4:
            text = '<p class="heading_text4" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Interest Rate %</span></p>'
            st.markdown(text_media_query_manual4 + text, unsafe_allow_html=True)
            user_whatif_interest_rate_field = st.empty()
            st.session_state.user_whatif_interest_rate = user_whatif_interest_rate_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=None, format="%.2f", value=st.session_state.default_whatif_interest_rate_user_out, key="whatif_manual_7")
            text = '<p class="heading_text4A" style="margin-top: 0em; margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Tax Rate %</span></p>'
            st.markdown(text_media_query_manual4A + text, unsafe_allow_html=True)
            user_whatif_tax_rate_field = st.empty()
            user_whatif_tax_rate_field = st.empty()
            st.session_state.user_whatif_tax_rate = user_whatif_tax_rate_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=None, format="%.2f", value=st.session_state.default_whatif_tax_rate_user_out, key="whatif_manual_8")
        with col5:
            text = '<p class="heading_text4" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Dividend Payout Ratio %</span></p>'
            st.markdown(text_media_query_manual4 + text, unsafe_allow_html=True)
            user_whatif_dividend_payout_ratio_field = st.empty()
            st.session_state.user_whatif_dividend_payout_ratio = user_whatif_dividend_payout_ratio_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=100.00, step=None, format="%.2f", value=st.session_state.default_whatif_dividend_payout_ratio_user_out, key="whatif_manual_9")


        html3 = """
        <div class="col2">
            <div class="left2">
                <p class="subtext_manual2" style="margin-bottom: 0em;"><span style="font-family: sans-serif; color: #25476A; font-size: 2em;">Cash Flow Statement & Balance Sheet Input Fields</span></p>
            </div>
            <div class="right2">
                <div class="tooltip2">
                    <i class="fas fa-info-circle fa-2x"></i>
                    <span class="tooltiptext2">
                        <ul class="responsive-ul2">
                            Understanding financial metrics and ratios is essential for assessing a company's financial health and making informed investment decisions.                               
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
                            These financial metrics and ratios can help provide valuable insight into a company's financial position and performance.
                        </ul>    
                    </span>
                </div>
            </div>
        </div>
        """

        st.markdown(html3, unsafe_allow_html=True)
        st.markdown(line_media_query2 + line2, unsafe_allow_html=True)
        instructions_text = '<p class="instructions_text" style="margin-top: -1.8em; margin-bottom: 0.8em; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 1em;">Enter values for the cash flow statement and balance sheet financial fields based on expectations for the company. Default values provided are based on the prior financial period.</span></p>'
        st.markdown(text_media_query_manual3 + instructions_text, unsafe_allow_html=True)
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            text = '<p class="heading_text4" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Accounts Receivable Days</span></p>'
            st.markdown(text_media_query_manual4 + text, unsafe_allow_html=True)
            user_whatif_accounts_receivable_days_field = st.empty()
            st.session_state.user_whatif_accounts_receivable_days = user_whatif_accounts_receivable_days_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_accounts_receivable_days_user_out, key="whatif_manual_10")
            text = '<p class="heading_text4A" style="margin-top: 0em; margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Inventory Days</span></p>'
            st.markdown(text_media_query_manual4A + text, unsafe_allow_html=True)
            user_whatif_inventory_days_field = st.empty()
            st.session_state.user_whatif_inventory_days = user_whatif_inventory_days_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_inventory_days_user_out, key="whatif_manual_11")
        with col2:
            text = '<p class="heading_text4" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Capital Expenditure / Sales %</span></p>'
            st.markdown(text_media_query_manual4 + text, unsafe_allow_html=True)
            user_whatif_capital_expenditure_sales_field = st.empty()
            st.session_state.user_whatif_capital_expenditure_sales = user_whatif_capital_expenditure_sales_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=None, format="%.2f", value=st.session_state.default_whatif_capital_expenditure_sales_user_out, key="whatif_manual_12")
            text = '<p class="heading_text4A" style="margin-top: 0em; margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Capital Expenditure $</span></p>'
            st.markdown(text_media_query_manual4A + text, unsafe_allow_html=True)
            user_whatif_capital_expenditure_field = st.empty()
            st.session_state.user_whatif_capital_expenditure = user_whatif_capital_expenditure_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_capital_expenditure_user_out, key="whatif_manual_13")
        with col3:
            text = '<p class="heading_text4" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Capital Expenditure Type</span></p>'
            st.markdown(text_media_query_manual4 + text, unsafe_allow_html=True)
            user_whatif_capital_expenditure_indicator_field = st.empty()
            st.session_state.user_whatif_capital_expenditure_indicator = user_whatif_capital_expenditure_indicator_field.selectbox(label="", label_visibility="collapsed", options=["Dollar", "Sales %"], key="whatif_manual_14")
            text = '<p class="heading_text4A" style="margin-top: 0em; margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Capex Tangible / Intangible Split %</span></p>'
            st.markdown(text_media_query_manual4A + text, unsafe_allow_html=True)
            user_whatif_tangible_intangible_split_field = st.empty()
            st.session_state.user_whatif_tangible_intangible_split = user_whatif_tangible_intangible_split_field.number_input(label="", label_visibility="collapsed", min_value=0, max_value=100, step=None, format="%i", value=st.session_state.default_whatif_tangible_intangible_split_user_out, key="whatif_manual_15")
        with col4:
            text = '<p class="heading_text4" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Accounts Payable Days</span></p>'
            st.markdown(text_media_query_manual4 + text, unsafe_allow_html=True)
            user_whatif_accounts_payable_days_field = st.empty()
            st.session_state.user_whatif_accounts_payable_days = user_whatif_accounts_payable_days_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_accounts_payable_days_user_out, key="whatif_manual_16")
            text = '<p class="heading_text4A" style="margin-top: 0em; margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Sale of Equity $</span></p>'
            st.markdown(text_media_query_manual4A + text, unsafe_allow_html=True)
            user_whatif_sale_of_equity_field = st.empty()
            st.session_state.user_whatif_sale_of_equity = user_whatif_sale_of_equity_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_sale_of_equity_user_out, key="whatif_manual_17")
        with col5:
            text = '<p class="heading_text4" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Repurchase of Equity $</span></p>'
            st.markdown(text_media_query_manual4 + text, unsafe_allow_html=True)
            user_whatif_repurchase_of_equity_field = st.empty()
            st.session_state.user_whatif_repurchase_of_equity = user_whatif_repurchase_of_equity_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_repurchase_of_equity_user_out, key="whatif_manual_18")
            text = '<p class="heading_text4A" style="margin-top: 0em; margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Proceeds from Issuance of Debt $</span></p>'
            st.markdown(text_media_query_manual4A + text, unsafe_allow_html=True)
            user_whatif_proceeds_from_issuance_of_debt_field = st.empty()
            st.session_state.user_whatif_proceeds_from_issuance_of_debt = user_whatif_proceeds_from_issuance_of_debt_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_proceeds_from_issuance_of_debt_user_out, key="whatif_manual_19")
        with col6:
            text = '<p class="heading_text4" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Repayments of Long Term Debt $</span></p>'
            st.markdown(text_media_query_manual4 + text, unsafe_allow_html=True)
            user_whatif_repayments_of_long_term_debt_field = st.empty()
            st.session_state.user_whatif_repayments_of_long_term_debt = user_whatif_repayments_of_long_term_debt_field.number_input(label="", label_visibility="collapsed", min_value=0.00, max_value=None, step=1.00, format="%.0f", value=st.session_state.default_whatif_repayments_of_long_term_debt_user_out, key="whatif_manual_20")
            text = '<p class="heading_text4A" style="margin-top: 0em; margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Notes / Other Split %</span></p>'
            st.markdown(text_media_query_manual4A + text, unsafe_allow_html=True)
            user_whatif_notes_other_split_field = st.empty()
            st.session_state.user_whatif_notes_other_split = user_whatif_notes_other_split_field.number_input(label="", label_visibility="collapsed", min_value=0, max_value=100, step=None, format="%i", value=st.session_state.default_whatif_notes_other_split_user_out, key="whatif_manual_21")
        col1, col2, col3, col4 = st.columns([4, 1.05, 0.5, 0.5])
        with col1:
            instructions_text = '<p class="instructions_text_update" style="margin-top: 2em; margin-bottom: 0em; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 1em;">Click "ReRun" once you have made your selection or click "Reset" to reset to the default values.</span></p>'
            text_media_query_manual3A = '''
            <style>
            @media (max-width: 1024px) {
                p.instructions_text_update {
                     font-size: 3.2em;
                     margin-top: 0em !important;
                }
            }
            </style>
            '''
            st.markdown(text_media_query_manual3A + instructions_text, unsafe_allow_html=True)
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
                                                                                          'props': [('color', '#25476A'), ('font-size', '0.85em')]}, {'selector': 'th:nth-child(1)',
                                                                                          'props': [
                                                                                              ('text-align', 'left'), ('font-size', '0.85em'),
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
                                                                                                       '#FAFAFA'), ('font-size', '0.85em')]}, {
                                                                                                'selector': 'th:last-child',
                                                                                                'props': [('text-align', 'center'), ('font-size', '0.85em')]
                                                                                            },
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
                    0] + " Millions)"], **{'text-align': 'left'}, **{'width': '400px'}) 
    
        df_cash_flow_statement_out_png = st.session_state.df_cash_flow_statement_out.style.set_table_styles([{'selector': 'td',
                                                                                          'props': [('color', '#25476A'), ('font-size', '0.85em')]},{
            'selector': 'th:nth-child(1)',
            'props': [('text-align',
                       'left'), ('font-size', '0.85em'), (
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
                          '#FAFAFA'), ('font-size', '0.85em')]}, {
                                                                                                'selector': 'th:last-child',
                                                                                                'props': [('text-align', 'center'), ('font-size', '0.85em')]
                                                                                            }, {
                                                                                                'selector': 'th:last-child',
                                                                                                'props': [('text-align', 'center'), ('font-size', '0.85em')]
                                                                                            }, {'selector': 'tr:nth-child(5) td',
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
                0] + " Millions)"], **{'text-align': 'left'}, **{'width': '400px'})

        df_balance_sheet_out_png = st.session_state.df_balance_sheet_statement_out.style.set_table_styles([{'selector': 'td',
                                                                                          'props': [('color', '#25476A'), ('font-size', '0.85em')]},{
            'selector': 'th:nth-child(1)',
            'props': [(
                'text-align',
                'left'), ('font-size', '0.85em'), (
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
                     '#FAFAFA'), ('font-size', '0.85em')]},
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
                0] + " Millions)"], **{'text-align': 'left'}, **{'width': '400px'})

        st.text("")
        st.markdown(styles, unsafe_allow_html=True)
        
        current_rating = "B+"
        predict_rating = "BBB"
        
        rating_dict = {'AAA': 1, 'AA+': 2, 'AA': 3, 'AA-': 4, 'A+': 5, 'A': 6, 'A-': 7, 'BBB+': 8,
               'BBB': 9, 'BBB-': 10, 'BB+': 11, 'BB': 12, 'BB-': 13, 'B+': 14, 'B': 15, 'B-': 16,
               'CCC+': 17, 'CCC': 18, 'CCC-': 19, 'CC': 20, 'C': 21, 'D': 22}

        current_rating_value = rating_dict.get(current_rating)
        predict_rating_value = rating_dict.get(predict_rating)
        difference = predict_rating_value - current_rating_value

        if difference > 0:
            text1 = '''
        <p class="text1" style="margin-top: 1em; margin-bottom: 2em; text-align: justify;"><span style="color: #25476A; background-color: rgba(3, 169, 244, 0.2); border-radius: 0.375em; padding-left: 0.75em; padding-right: 0.75em; padding-top: 0.5em; padding-bottom: 0.5em; font-family: sans-serif; font-size: 1em; font-weight: bold; display: block; width: 100%; border: 0.1875em solid #25476A;">Based on manual analysis of the company's financial statements, Paydar calculates a {} rating for {} at {}. Paydar predicts a {} rating based on the financial scenario provided, indicating a {} notch rating downgrade and a deterioration in the company's credit quality.</span></p>
        '''.format(current_rating, st.session_state.user_entity_name, st.session_state.user_reporting_period, predict_rating, abs(difference))
        elif difference < 0:
            text1 = '''
        <p class="text1" style="margin-top: 1em; margin-bottom: 2em; text-align: justify;"><span style="color: #25476A; background-color: rgba(3, 169, 244, 0.2); border-radius: 0.375em; padding-left: 0.75em; padding-right: 0.75em; padding-top: 0.5em; padding-bottom: 0.5em; font-family: sans-serif; font-size: 1em; font-weight: bold; display: block; width: 100%; border: 0.1875em solid #25476A;">Based on manual analysis of the company's financial statements, Paydar calculates a {} rating for {} at {}. Paydar predicts a {} rating based on the financial scenario provided, indicating a {} notch rating upgrade and an improvement in the company's credit quality.</span></p>
        '''.format(current_rating, st.session_state.user_entity_name, st.session_state.user_reporting_period, predict_rating, abs(difference))
        else:
            text1 = '''
        <p class="text1" style="margin-top: 1em; margin-bottom: 2em; text-align: justify;"><span style="color: #25476A; background-color: rgba(3, 169, 244, 0.2); border-radius: 0.375em; padding-left: 0.75em; padding-right: 0.75em; padding-top: 0.5em; padding-bottom: 0.5em; font-family: sans-serif; font-size: 1em; font-weight: bold; display: block; width: 100%; border: 0.1875em solid #25476A;">Based on manual analysis of the company's financial statements, Paydar calculates a {} rating for {} at {}. Paydar predicts a {} rating based on the financial scenario provided, indicating no change to the company's rating and stable credit quality.</span></p>
        '''.format(current_rating, st.session_state.user_entity_name, st.session_state.user_reporting_period, predict_rating)
       
        left_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 2.25em;'>{}&nbsp;{}<span class='break-line'>&nbsp;{}</span>".format(str(st.session_state.user_reporting_period), "Rating:", current_rating)
        right_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 2.25em;'>{}<span class='break-line'>&nbsp;{}</span>".format("Scenario Rating:", predict_rating)
        html4 = f"<div class='col'><div class='left'>{left_text}</div><div class='right'>{right_text}</div></div>"
        st.markdown(html4, unsafe_allow_html=True)
        st.markdown(text_media_query_manual1 + text1, unsafe_allow_html=True)
               
        
        color1 = "#5007E3"
        color2 = "#03A9F4"
        col_cmap = clr.LinearSegmentedColormap.from_list(name="",
                                                              colors=[color1, color2])
        num_steps = 1000
        values = np.linspace(0, 1, num_steps)
        step_values = np.linspace(0, 22, num_steps)
        colors = col_cmap(values)
        step_colors = [clr.rgb2hex(color) for color in colors]

        manual_current_rating_fig = go.Figure(go.Indicator(
            mode="gauge",
            value=0,
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {
                    'range': [0, 22],
                    'dtick': 1,
                    'tickwidth': 4,
                    'tickcolor': "#25476A",
                    'ticktext': ['AAA', 'AA+', 'AA', 'AA-', 'A+', 'A', 'A-', 'BBB+', 'BBB', 'BBB-', 'BB+', "BB", 'BB-', 'B+', 'B', 'B-', 'CCC+', 'CCC', 'CCC-', 'CC', 'C', 'D'][::-1],
                    'tickvals': [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5],
                    'tickangle': 0
                },
                'shape': "angular",
                'bar': {'color': "rgba(0, 0, 0, 0)"},
                'bgcolor': 'rgba(0, 0, 0, 0)',
                'steps': [{'range': [step_values[i], step_values[i + 1]], 'color': step_colors[i]} for i in range(num_steps - 1)],
                'borderwidth': 4,
                'bordercolor': "#25476A",
                'threshold': {'line': {'color': "#FAFAFA", 'width': 5}, 'thickness': 0.75,
                                                          'value': 21.5-(current_rating_value-1)}
                }
            ))

        manual_current_rating_fig.add_annotation(
    dict(font=dict(color="#25476A", size=25, family="sans-serif"), x=0.5, y=0, xanchor='center',
         xref="paper",
         yref="paper", showarrow=False,
         text="{}<br>Rating<br>{}".format(st.session_state.user_reporting_period, current_rating)))
        manual_current_rating_fig.update_layout(
            paper_bgcolor='rgba(0, 0, 0, 0)',
            font={'color': "#25476A", 'size': 14},
            width=180,
            height=180,
            margin=dict(t=20, b=1)
        )

        manual_current_rating_fig.update_xaxes(color="#25476A", mirror=True, showline=True)      
        
        manual_scenario_rating_fig = go.Figure(go.Indicator(
            mode="gauge",
            value=0,
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {
                    'range': [0, 22],
                    'dtick': 1,
                    'tickwidth': 4,
                    'tickcolor': "#25476A",
                    'ticktext': ['AAA', 'AA+', 'AA', 'AA-', 'A+', 'A', 'A-', 'BBB+', 'BBB', 'BBB-', 'BB+', "BB", 'BB-', 'B+', 'B', 'B-', 'CCC+', 'CCC', 'CCC-', 'CC', 'C', 'D'][::-1],
                    'tickvals': [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5],
                    'tickangle': 0
                },
                'shape': "angular",
                'bar': {'color': "rgba(0, 0, 0, 0)"},
                'bgcolor': 'rgba(0, 0, 0, 0)',
                'steps': [{'range': [step_values[i], step_values[i + 1]], 'color': step_colors[i]} for i in range(num_steps - 1)],
                'borderwidth': 4,
                'bordercolor': "#25476A",
                'threshold': {'line': {'color': "#FAFAFA", 'width': 5}, 'thickness': 0.75,
                                                          'value': 21.5-(predict_rating_value-1)}
                }
            ))

        manual_scenario_rating_fig.add_annotation(
    dict(font=dict(color="#25476A", size=25, family="sans-serif"), x=0.5, y=0, xanchor='center',
         xref="paper",
         yref="paper", showarrow=False,
         text="Scenario<br>Rating<br>{}".format(predict_rating)))
        manual_scenario_rating_fig.update_layout(
            paper_bgcolor='rgba(0, 0, 0, 0)',
            font={'color': "#25476A", 'size': 14},
            width=180,
            height=180,
            margin=dict(t=20, b=1)
        )

        manual_scenario_rating_fig.update_xaxes(color="#25476A", mirror=True, showline=True) 
        
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(manual_current_rating_fig, config={'displayModeBar': False}, use_container_width=True)
 
        with col2:
            st.plotly_chart(manual_scenario_rating_fig, config={'displayModeBar': False}, use_container_width=True)
          
  #      st.markdown("<style>.full-width-chart .chart-container { display: flex; justify-content: center; }</style>", unsafe_allow_html=True)
        subtext1A = '<p class="subtext" style="margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 2em;">Financial Statements</span></p>'
        text_media_query_manual2 = '''
            <style>
            @media (max-width: 1024px) {
                p.subtext {
                    font-size: 2.5em;
                }
            }
            </style>
        '''
        st.markdown(text_media_query_manual2 + subtext1A, unsafe_allow_html=True)        
        st.markdown(line_media_query2 + line2, unsafe_allow_html=True)
        instructions_text = '<p class="instructions_text" style="margin-top: -1.8em; margin-bottom: 0.8em; padding-top: -20em; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 1em;">Company financial statements for the reporting period and the expected scenario are shown below. The financial statements may be downloaded for your records.</span></p>'
        st.markdown(text_media_query_manual3 + instructions_text, unsafe_allow_html=True)
       
        col1, col2, col3 = st.columns([1, 1, 4])
        with col1:
            text = '<p class="heading_text4A" style="margin-top: 0em; margin-bottom: 0em;"><span style="font-family:sans-serif; color:#25476A; font-size: 0.85em; font-weight: bold;">Download Statements</span></p>'
            st.markdown(text_media_query_manual4A + text, unsafe_allow_html=True)
            statement_out_download_typ_field = st.empty()
            statement_out_download_type = statement_out_download_typ_field.selectbox(label="", label_visibility="collapsed",
                                                       options=["Select Download Type", "CSV", "PNG"],
                                                       key="manual_download1")
            if resubmit_button or reset_button:
                statement_out_download_typ_field.empty()
                statement_out_download_type = statement_out_download_typ_field.selectbox(label="", label_visibility="collapsed",
                                                           options=["Select Download Type", "CSV", "PNG"],
                                                           key="manual_download2")
        with col2:
             if statement_out_download_type == "CSV":
                spinner = st.markdown(marker_spinner_css, unsafe_allow_html=True)
                spinner_image = st.markdown(spinner_image_css.format(img_to_bytes("images/spinner_center2.png")), unsafe_allow_html=True)
                statements_out = [(st.session_state.df_income_statement_out.reset_index(drop=True).to_csv().encode(), "manual_analysis_income_statement", "csv"), (st.session_state.df_cash_flow_statement_out.reset_index(drop=True).to_csv().encode(), "manual_analysis_cashflow_statement", "csv"), (st.session_state.df_balance_sheet_statement_out.reset_index(drop=True).to_csv().encode(), "manual_analysis_balance_sheet", "csv")]
                downloader = MultiFileDownloader()
                downloader.download_manual_figures(statements_out, st.session_state.user_entity_name)
                spinner.empty()
                spinner_image.empty()
             if statement_out_download_type == "PNG":
                spinner = st.markdown(marker_spinner_css, unsafe_allow_html=True)
                spinner_image = st.markdown(spinner_image_css.format(img_to_bytes("images/spinner_center2.png")), unsafe_allow_html=True)
                statements_out = ([df_income_statement_out_png, "manual_analysis_income_statement.to_html()", "png", "Income Statement", 36], [df_cash_flow_statement_out_png.to_html(), "manual_analysis_cash_flow_statement", "png", "Cash Flow Statement", 36], [df_balance_sheet_out_png.to_html(), "manual_analysis_balance_sheet", "png", "Balance Sheet", 36])
                downloader = MultiFileDownloader()
                downloader.export_tables(statements_out, st.session_state.user_entity_name)
                spinner.empty()
                spinner_image.empty()

        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
               
        col1, col2, col3 = st.columns(3)
        with col1:
            left_text = "<span style='margin-bottom: 0em; font-family: sans-serif; color: #25476A; font-size: 1.7em;'>Income Statement</span>"
            right_text = "<span style='margin-bottom: 0em; font-family: sans-serif; color: #25476A; font-size: 0.8em;'>(blue fields indicate change)</span></span>"

            html5 = f"<div class='col3'><div class='left3'>{left_text}</div><div class='right3'>{right_text}</div></div>"
            st.markdown(html5, unsafe_allow_html=True)
            st.table(df_income_statement_out_png)
            st.text("")
            #st.markdown('<div style="margin-top: -11px">' + df_income_statement_out_png.to_html(), unsafe_allow_html=True)
        with col2:
            left_text = "<span style='margin-bottom: 0em; font-family: sans-serif; color: #25476A; font-size: 1.7em;'>Cash Flow Statement</span>"
            right_text = "<span style='margin-bottom: 0em; font-family: sans-serif; color: #25476A; font-size: 0.8em;'>(blue fields indicate change)</span></span>"

            html5 = f"<div class='col3'><div class='left3'>{left_text}</div><div class='right3'>{right_text}</div></div>"
            st.markdown(html5, unsafe_allow_html=True)
            st.table(df_cash_flow_statement_out_png)
            st.text("")
            #st.markdown('<div style="margin-top: -11px">' + df_cash_flow_statement_out_png.to_html(), unsafe_allow_html=True)
        with col3:
            left_text = "<span style='margin-bottom: 0em; font-family: sans-serif; color: #25476A; font-size: 1.7em;'>Balance Sheet</span>"
            right_text = "<span style='margin-bottom: 0em; font-family: sans-serif; color: #25476A; font-size: 0.8em;'>(blue fields indicate change)</span></span>"

            html5 = f"<div class='col3'><div class='left3'>{left_text}</div><div class='right3'>{right_text}</div></div>"
            st.markdown(html5, unsafe_allow_html=True)
            st.table(df_balance_sheet_out_png)
            #st.markdown('<div style="margin-top: -11px">' + df_balance_sheet_out_png.to_html(), unsafe_allow_html=True)


            
