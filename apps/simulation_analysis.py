import streamlit as st
import numpy as np
import pandas as pd
import random
import pathlib
import base64
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import kaleido
from apps.functions import get_default_fields, run_whatif, run_simulation, FileDownloader, MultiFileDownloader

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
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 0 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 0 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 0 / 50))), calc(5em * sin(2 * 3.14159 * 0 / 50)));        
    }
    
    .marker1 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 1 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 1 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 1 / 50))), calc(5em * sin(2 * 3.14159 * 1 / 50)));
    }
    
    .marker2 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 2 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 2 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 2 / 50))), calc(5em * sin(2 * 3.14159 * 2 / 50)));
    }
    
    .marker3 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 3 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 3 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 3 / 50))), calc(5em * sin(2 * 3.14159 * 3 / 50)));
    }
    
    .marker4 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 4 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 4 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 4 / 50))), calc(5em * sin(2 * 3.14159 * 4 / 50)));
    }
    
    .marker5 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 5 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 5 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 5 / 50))), calc(5em * sin(2 * 3.14159 * 5 / 50)));
    }
    
    .marker6 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 6 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 6 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 6 / 50))), calc(5em * sin(2 * 3.14159 * 6 / 50)));
    }
    
    .marker7 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 7 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 7 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 7 / 50))), calc(5em * sin(2 * 3.14159 * 7 / 50)));
    }
    
    .marker8 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 8 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 8 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 8 / 50))), calc(5em * sin(2 * 3.14159 * 8 / 50)));
    }
    
    .marker9 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 9 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 9 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 9 / 50))), calc(5em * sin(2 * 3.14159 * 9 / 50)));
    }
    
    .marker10 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 10 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 10 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 10 / 50))), calc(5em * sin(2 * 3.14159 * 10 / 50)));
    }
    
    .marker11 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 11 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 11 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 11 / 50))), calc(5em * sin(2 * 3.14159 * 11 / 50)));
    }
    
    .marker12 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 12 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 12 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 12 / 50))), calc(5em * sin(2 * 3.14159 * 12 / 50)));
    }
    
    .marker13 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 13 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 13 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 13 / 50))), calc(5em * sin(2 * 3.14159 * 13 / 50)));
    }
    
    .marker14 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 14 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 14 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 14 / 50))), calc(5em * sin(2 * 3.14159 * 14 / 50)));
    }
    
    .marker15 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 15 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 15 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 15 / 50))), calc(5em * sin(2 * 3.14159 * 15 / 50)));
    }
    
    .marker16 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 16 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 16 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 16 / 50))), calc(5em * sin(2 * 3.14159 * 16 / 50)));
    }
    
    .marker17 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 17 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 17 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 17 / 50))), calc(5em * sin(2 * 3.14159 * 17 / 50)));
    }
    
    .marker18 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 18 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 18 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 18 / 50))), calc(5em * sin(2 * 3.14159 * 18 / 50)));
    }
    
    .marker19 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 19 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 19 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 19 / 50))), calc(5em * sin(2 * 3.14159 * 19 / 50)));
    }
    
    .marker20 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 20 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 20 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 20 / 50))), calc(5em * sin(2 * 3.14159 * 20 / 50)));
    }
    
    .marker21 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 21 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 21 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 21 / 50))), calc(5em * sin(2 * 3.14159 * 21 / 50)));
    }
    
    .marker22 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 22 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 22 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 22 / 50))), calc(5em * sin(2 * 3.14159 * 22 / 50)));
    }
    
    .marker23 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 23 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 23 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 23 / 50))), calc(5em * sin(2 * 3.14159 * 23 / 50)));
    }
    
    .marker24 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 24 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 24 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 24 / 50))), calc(5em * sin(2 * 3.14159 * 24 / 50)));
    }
    
    .marker25 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 25 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 25 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 25 / 50))), calc(5em * sin(2 * 3.14159 * 25 / 50)));
    }
    
    .marker26 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 26 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 26 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 26 / 50))), calc(5em * sin(2 * 3.14159 * 26 / 50)));
    }
    
    .marker27 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 27 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 27 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 27 / 50))), calc(5em * sin(2 * 3.14159 * 27 / 50)));
    }
    
    .marker28 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 28 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 28 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 28 / 50))), calc(5em * sin(2 * 3.14159 * 28 / 50)));
    }
    
    .marker29 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 29 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 29 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 29 / 50))), calc(5em * sin(2 * 3.14159 * 29 / 50)));
    }
    
    .marker30 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 30 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 30 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 30 / 50))), calc(5em * sin(2 * 3.14159 * 30 / 50)));
    }
    
    .marker31 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 31 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 31 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 31 / 50))), calc(5em * sin(2 * 3.14159 * 31 / 50)));
    }
    
    .marker32 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 32 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 32 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 32 / 50))), calc(5em * sin(2 * 3.14159 * 32 / 50)));
    }
    
    .marker33 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 33 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 33 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 33 / 50))), calc(5em * sin(2 * 3.14159 * 33 / 50)));
    }
    
    .marker34 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 34 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 34 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 34 / 50))), calc(5em * sin(2 * 3.14159 * 34 / 50)));
    }
    
    .marker35 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 35 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 35 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 35 / 50))), calc(5em * sin(2 * 3.14159 * 35 / 50)));
    }
    
    .marker36 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 36 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 36 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 36 / 50))), calc(5em * sin(2 * 3.14159 * 36 / 50)));
    }
    
    .marker37 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 37 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 37 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 37 / 50))), calc(5em * sin(2 * 3.14159 * 37 / 50)));
    }
    
    .marker38 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 38 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 38 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 38 / 50))), calc(5em * sin(2 * 3.14159 * 38 / 50)));
    }
    
    .marker39 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 39 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 39 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 39 / 50))), calc(5em * sin(2 * 3.14159 * 39 / 50)));
    }
    
    .marker40 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 40 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 40 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 40 / 50))), calc(5em * sin(2 * 3.14159 * 40 / 50)));
    }
    
    .marker41 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 41 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 41 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 41 / 50))), calc(5em * sin(2 * 3.14159 * 41 / 50)));
    }
    
    .marker42 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 42 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 42 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 42 / 50))), calc(5em * sin(2 * 3.14159 * 42 / 50)));
    }
    
    .marker43 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 43 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 43 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 43 / 50))), calc(5em * sin(2 * 3.14159 * 43 / 50)));
    }
    
    .marker44 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 44 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 44 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 44 / 50))), calc(5em * sin(2 * 3.14159 * 44 / 50)));
    }
    
    .marker45 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 45 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 45 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 45 / 50))), calc(5em * sin(2 * 3.14159 * 45 / 50)));
    }
    
    .marker46 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 46 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 46 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 46 / 50))), calc(5em * sin(2 * 3.14159 * 46 / 50)));
    }
    
    .marker47 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 47 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 47 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 47 / 50))), calc(5em * sin(2 * 3.14159 * 47 / 50)));
    }
    
    .marker48 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 48 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 48 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 48 / 50))), calc(5em * sin(2 * 3.14159 * 48 / 50)));
    }
    
    .marker49 {
        position: absolute;
        left: 0;
        width: 2em;
        height: 0.375em;
        background: rgba(0, 0, 0, 0);
        animation: animateBlink 3s linear infinite;
        animation-delay: calc(3s * 49 / 50);
        border-radius: 0.5em;
        transform: rotate(calc(360deg * 49 / 50)) translate(calc(5em * (1 - cos(2 * 3.14159 * 49 / 50))), calc(5em * sin(2 * 3.14159 * 49 / 50)));
    }

    @keyframes animateBlink {
    0% {
        background: #6f72de;
    }
    25% {
        background: rgba(0, 0, 0, 0);
    }   
}
@media (max-width: 600px) {
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

def img_to_bytes(img_path):
    img_bytes = pathlib.Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def get_financials(datafame, user_entity_name, user_period):
    entity_financials = datafame.loc[
        (datafame['entity_name'] == user_entity_name) & (datafame['period'] == user_period)]
    return entity_financials

def reset3():
#    st.session_state.user_whatif_simulated_values = ["Sales Growth %", "COGS Margin %", "D&A Expenses / Sales %", "Accounts Receivable Days",
#                         "Inventory Days", "Capital Expenditure / Sales %", "Accounts Payable Days"]
    if "user_whatif_simulated_values" in st.session_state:
        del st.session_state.user_whatif_simulated_values
    st.session_state.next1_confirm = False
    st.session_state.next2_confirm = False
    st.session_state.submit3_confirm = False
    st.session_state.simulation_run_confirm = False
    st.session_state.next3_confirm = False
    st.session_state.next4_confirm = False
    if 'seed_value' in st.session_state:
        del st.session_state.seed_value

def reset4():
    seed_options = ["", "Manually Set Seed", "Randomly Set Seed"]
    st.session_state.submit3_confirm = False
    st.session_state.simulation_run_confirm = False
    st.session_state.next3_confirm = False
    st.session_state.next4_confirm = False
    st.session_state.user_seed_option = seed_options[0]
    if 'seed_value' in st.session_state:
        del st.session_state.seed_value

def reset5():
    st.session_state.next3_confirm = False
    st.session_state.next4_confirm = False
    if "user_whatif_confidence_level" in st.session_state:
        del st.session_state.user_whatif_confidence_level
#    st.session_state.user_whatif_confidence_level = 95.00

def reset6():
    financial_statement_options = ["", "Income Statement", "Cash Flow Statement", "Balance Sheet"]
    st.session_state.next4_confirm = False
    st.session_state.user_whatif_financial_statement = financial_statement_options[0]

def change_callback3():
    if 'seed_value' in st.session_state:
        del st.session_state.seed_value
    st.session_state.next2_confirm = False
    st.session_state.submit3_confirm = False
    st.session_state.simulation_run_confirm = False
    st.session_state.next3_confirm = False
    st.session_state.next4_confirm = False

def change_callback4():
    if 'seed_value' in st.session_state:
        del st.session_state.seed_value
    st.session_state.submit3_confirm = False
    st.session_state.simulation_run_confirm = False
    st.session_state.next3_confirm = False
    st.session_state.next4_confirm = False

def change_callback5():
    st.session_state.next3_confirm = False
    st.session_state.next4_confirm = False

def change_callback6():
    st.session_state.next4_confirm = False


def app():
    line = '<hr style="height: 5px; border:0px; background-color: #03A9F4; margin-top: 0px;">'
    line2 = '<hr style="height: 3x; border:0px; background-color: #25476A; margin-top: -30px;">'
    spinner = st.markdown(marker_spinner_css, unsafe_allow_html=True)
    spinner_image = st.markdown(spinner_image_css.format(img_to_bytes("images/spinner_center.png")), unsafe_allow_html=True)
    st.session_state.simulation_analysis_confirm = True
    st.session_state.manual_analysis_confirm = False
    st.session_state.default_whatif_sales_revenue_growth_user_out, st.session_state.default_whatif_cost_of_goods_sold_margin_user_out, st.session_state.default_whatif_sales_general_and_admin_expenses_user_out, st.session_state.default_whatif_research_and_development_expenses_user_out, st.session_state.default_whatif_depreciation_and_amortization_expenses_sales_user_out, st.session_state.default_whatif_depreciation_and_amortization_split_user_out, st.session_state.default_whatif_interest_rate_user_out, st.session_state.default_whatif_tax_rate_user_out, st.session_state.default_whatif_dividend_payout_ratio_user_out, st.session_state.default_whatif_accounts_receivable_days_user_out, st.session_state.default_whatif_inventory_days_user_out, st.session_state.default_whatif_capital_expenditure_sales_user_out, st.session_state.default_whatif_capital_expenditure_user_out, st.session_state.default_whatif_capital_expenditure_indicator_user_out, st.session_state.default_whatif_tangible_intangible_split_user_out, st.session_state.default_whatif_accounts_payable_days_user_out, st.session_state.default_whatif_sale_of_equity_user_out, st.session_state.default_whatif_repurchase_of_equity_user_out, st.session_state.default_whatif_proceeds_from_issuance_of_debt_user_out, st.session_state.default_whatif_repayments_of_long_term_debt_user_out, st.session_state.default_whatif_notes_other_split_user_out = get_default_fields(select_user_entity_name=st.session_state.user_entity_name, select_user_period=st.session_state.user_reporting_period)
    default_fields = [st.session_state.default_whatif_sales_revenue_growth_user_out, st.session_state.default_whatif_cost_of_goods_sold_margin_user_out, st.session_state.default_whatif_sales_general_and_admin_expenses_user_out, st.session_state.default_whatif_research_and_development_expenses_user_out, st.session_state.default_whatif_depreciation_and_amortization_expenses_sales_user_out, st.session_state.default_whatif_depreciation_and_amortization_split_user_out, st.session_state.default_whatif_interest_rate_user_out, st.session_state.default_whatif_tax_rate_user_out, st.session_state.default_whatif_dividend_payout_ratio_user_out, st.session_state.default_whatif_accounts_receivable_days_user_out, st.session_state.default_whatif_inventory_days_user_out, st.session_state.default_whatif_capital_expenditure_sales_user_out, st.session_state.default_whatif_capital_expenditure_user_out, st.session_state.default_whatif_capital_expenditure_indicator_user_out, st.session_state.default_whatif_tangible_intangible_split_user_out, st.session_state.default_whatif_accounts_payable_days_user_out, st.session_state.default_whatif_sale_of_equity_user_out, st.session_state.default_whatif_repurchase_of_equity_user_out, st.session_state.default_whatif_proceeds_from_issuance_of_debt_user_out, st.session_state.default_whatif_repayments_of_long_term_debt_user_out, st.session_state.default_whatif_notes_other_split_user_out]
    spinner.empty()
    spinner_image.empty()

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

    left_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 44px;'>Simulation Analysis</span>"
    right_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 44px;'>{}&nbsp;&nbsp;&nbsp;{}</span>".format(
        st.session_state.user_entity_name, st.session_state.user_reporting_period)

    html = f"<div class='col'><div class='left'>{left_text}</div><div class='right'>{right_text}</div></div>"
    st.markdown(html, unsafe_allow_html=True)
    text = '<div style="margin-top: 20px; margin-bottom: 0px; border: 3px solid #25476A; background-color: rgba(3, 169, 244, 0.2); border-radius:6px; padding-left:12px; padding-right: 12px; padding-top:12px; padding-bottom:12px;">\
        <p style="margin-top: 0px; margin-bottom: 0px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Simulation analysis of financial statements is a process of creating a mathematical model that mimics the financial performance of a target company to gain insights into its financial position and performance. This analysis involves the following steps:</span></p>\
        <ul style="color:#25476A; text-align: justify;">\
            <li style="font-family:sans-serif; font-size:18px;">Reviewing the company&apos;s income statement, balance sheet and cash flow statement to understand its financial performance over time and identify trends.</li>\
            <li style="font-family:sans-serif; font-size:18px;">Identifying key financial drivers, such as sales growth, COGS margin and operating expenses and randomly simulating correlated values for these drivers to generate a range of potential outcomes for the company&apos;s financial performance.</li>\
            <li style="font-family:sans-serif; font-size:18px;">Conducting ratio analysis to evaluate the company&apos;s financial health and generate a credit rating for each simulated outcome. </li>\
        </ul>\
        <p style="margin-top: -10px; margin-bottom: 0px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">By performing a simulation analysis of financial statements, Comrate&apos;s wargame scenario analysis application can enable the evaluation of a target company&apos;s financial performance under various scenarios and the identification of potential risks and opportunities, empowering you to make informed decisions regarding the current and future financial performance of target companies.</span></p>\
    </div>'

    st.markdown(text, unsafe_allow_html=True)


    st.text("")
    st.text("")
    col1, col2 = st.columns([5.8, 0.2])
    with col1:
        subtext1 = '<p style="margin-bottom: 0px;"><span style="font-family:sans-serif; color:#25476A; font-size: 40px;">Income Statement, Cash Flow Statement & Balance Sheet Simulated Input Fields</span></p>'
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
                    The simulation model provides the user with the option to simulate the following risk factors.                               
                        <li>Sales Growth: A measure of the percentage increase or decrease in revenue over a period of time.</li>
                        <li>COGS Margin: The percentage of revenue that is consumed by the cost of goods sold. It indicates how efficiently a company is using its resources to produce goods.</li>
                        <li>D&A Expenses / Sales: Depreciation and amortization expenses as a percentage of revenue. It indicates how much a company is investing in its long-term assets and how much it is expensing in the current period.</li>
                        <li>Accounts Receivable Days: The number of days it takes for a company to collect payment for goods or services sold. A lower number of days is generally seen as a positive sign, indicating that a company is efficient in its collections process.</li>
                        <li>Inventory Days: The number of days it takes for a company to sell its inventory. A lower number of days is generally seen as a positive sign, indicating that a company has a strong demand for its products.</li>
                        <li>Capital Expenditure / Sales: The ratio of capital expenditures to sales. This ratio indicates how much a company is investing in long-term assets relative to its revenue. A higher ratio may suggest that a company is investing more in its long-term growth and may have higher future earnings potential.</li>
                        <li>Accounts Payable Days: The number of days it takes for a company to pay its bills to suppliers. A higher number of days may indicate that a company is using its suppliers&apos; money to finance its operations and may be seen as a positive sign for the company&apos;s cash flow management.</li>                    Simulating these risk factors can help provide an understanding of the potential impact of different scenarios on a company&apos;s financial health and performance.
                    </ul>
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(line, unsafe_allow_html=True)
    st.markdown(line2, unsafe_allow_html=True)
    instructions_text = '<p style="margin-top: -25px; margin-bottom: 20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Select simulated income statement, cash flow statement and balance sheet financial fields. Click "Next" once you have made your selections or click "Reset" to reset to the default selection.</span></p>'
    st.markdown(instructions_text, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([5, 0.5, 0.5])
    with col1:
        sim_field_options = ["Sales Growth %", "COGS Margin %", "D&A Expenses / Sales %", "Accounts Receivable Days", "Inventory Days", "Capital Expenditure / Sales %", "Accounts Payable Days"]
        text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Simulated Fields</span></p>'
        st.markdown(text, unsafe_allow_html=True)
        if "user_whatif_simulated_values" not in st.session_state:
            st.multiselect(label="", label_visibility="collapsed", options=sim_field_options, default=sim_field_options,
                           key="user_whatif_simulated_values", on_change=change_callback3)
        else:
            st.multiselect(label="", label_visibility="collapsed", options=sim_field_options, default=st.session_state.user_whatif_simulated_values, key="user_whatif_simulated_values", on_change=change_callback3)

    with col2:
        st.text("")
        st.text("")
        next_button1 = st.button("Next", key="whatif_sim_2")
    with col3:
        st.text("")
        st.text("")
        reset_button1 = st.button("Reset", key="whatif_reset_1", on_click=reset3)
    if next_button1:
        st.session_state.next1_confirm = True

    if st.session_state.next1_confirm == True:
        st.text("")
        st.text("")
        col1, col2 = st.columns([5.8, 0.2])
        with col1:
            subtext1 = '<p style="margin-bottom: 0px;"><span style="font-family:sans-serif; color:#25476A; font-size: 40px;">Income Statement, Cash Flow Statement & Balance Sheet Manual Input Fields</span></p>'
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
                        Specific risk factors are typically kept static during a simulation because they are assumed to be constant over the short-term time horizon of the simulation.                          
                            <li>SG&A Expenses: The total operating expenses of a company that are not directly related to production, such as salaries, rent, utilities and marketing costs.</li>
                            <li>R&D Expenses: The amount of money a company spends on research and development activities. It indicates a company&apos;s commitment to innovation and growth.</li>
                            <li>D&A Split: The breakdown of depreciation and amortization expenses between tangible assets (D) and intangible assets (A). It indicates how much a company is investing in different types of assets.</li>
                            <li>Interest Rate: The cost of borrowing money. It indicates how much a company is paying to finance its operations and how much debt it has.</li>
                            <li>Tax Rate: The percentage of a company&apos;s income that is paid in taxes. It indicates how much income a company able to retain.</li>
                            <li>Dividend Payout Ratio: The percentage of earnings paid out as dividends to shareholders. It indicates how much a company is returning to its shareholders in the form of dividends and how much it is retaining for reinvestment.</li>                                                                  
                            <li>Capital Expenditure: The amount of money a company spends on acquiring or improving long-term assets such as property, plant and equipment. This investment is typically made to increase a company&apos;s production capacity, efficiency or competitiveness.</li>
                            <li>Capital Expenditure Type (Ratio or Dollar): An indicator of whether capital expenditure is expressed as a ratio of sales or as a dollar amount. A ratio may be more informative in evaluating a company&apos;s investment decisions relative to its size, while a dollar amount may be more informative in evaluating the company&apos;s overall investment in long-term assets.</li>
                            <li>CapEx Tangible / Intangible Split: The breakdown of capital expenditures between tangible assets, such as property and equipment and intangible assets, such as patents and intellectual property. This breakdown indicates how much a company is investing in different types of long-term assets.</li>
                            <li>Sales of Equity: The total amount of equity sold by a company during a period. This may include common stock, preferred stock or other types of equity.</li>
                            <li>Repurchase of Equity: The total amount of equity repurchased by a company during a period. This may include buying back common stock, preferred stock or other types of equity.</li>                                    
                            <li>Proceeds from Issuance of Debt: The total amount of money a company receives from issuing debt. This may include bonds, notes or other forms of debt financing.</li>
                            <li>Repayments of Long-Term Debt: The total amount of money a company pays back to lenders for long-term debt. This may include interest payments as well as principal repayments.</li>
                            <li>Notes / Other Split: The breakdown of a company&apos;s short-term debt between notes and other types of short-term debt. Notes refer to short-term debt that is issued with a specific maturity date, while other types of short-term debt may not have a specific maturity date or may be payable on demand.</li>
                        The purpose of a simulation is to understand the potential impact of changing certain variables or assumptions, such as sales growth or COGS margin, on the overall financial performance of a company. By keeping other variables constant, the simulation is able to isolate the effects of the specific risk factors being analyzed. Additionally, it may be challenging to predict how these static variables might change over the simulation period, making it more practical to assume they remain constant. However, it is important to note that in real-world situations, these financial metrics and ratios will likely change over time and they should be continuously monitored to determine a company&apos;s financial position and performance.
                        </ul>
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )



        st.markdown(line, unsafe_allow_html=True)
        st.markdown(line2, unsafe_allow_html=True)
        instructions_text = '<p style="margin-top: -25px; margin-bottom: 20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Enter values for the non-simulated income statement, cash flow statement and balance sheet financial fields based on expectations for the company. Default values provided are based on the prior financial period.</span></p>'
        st.markdown(instructions_text, unsafe_allow_html=True)
        field_options = ["Sales Growth %", "COGS Margin %", "SG&A Expenses $", "R&D Expenses $", "D&A Expenses / Sales %", "D&A Split %", "Interest Rate %", "Tax Rate %", "Dividend Payout Ratio %",
                             "Accounts Receivable Days", "Inventory Days", "Capital Expenditure / Sales %", "Capital Expenditure $", "Capital Expenditure Type", "Capex Tangible / Intangible Split %",
                             "Accounts Payable Days", "Sale of Equity $", "Repurchase of Equity $", "Proceeds from Issuance of Debt $", "Repayments of Long Term Debt $", "Notes / Other Split %"]
        st.session_state.user_whatif_manual_field_options = [s for s in field_options if s not in st.session_state.user_whatif_simulated_values]
        field_names = ["user_whatif_sim_sales_revenue_growth_field", "user_whatif_sim_cost_of_goods_sold_margin_field",
                       "user_whatif_sim_sales_general_and_admin_expenses_field",
                       "user_whatif_sim_research_and_development_expenses_field",
                       "user_whatif_sim_depreciation_and_amortization_expenses_sales_field",
                       "user_whatif_sim_depreciation_and_amortization_split_field",
                       "user_whatif_sim_interest_rate_field", "user_whatif_sim_tax_rate_field",
                       "user_whatif_sim_dividend_payout_ratio_field", "user_whatif_sim_accounts_receivable_days_field",
                       "user_whatif_sim_inventory_days_field", "user_whatif_sim_capital_expenditure_sales_field",
                       "user_whatif_sim_capital_expenditure_field",
                       "user_whatif_sim_capital_expenditure_indicator_field",
                       "user_whatif_sim_tangible_intangible_split_field", "user_whatif_sim_accounts_payable_days_field",
                       "user_whatif_sim_sale_of_equity_field", "user_whatif_sim_repurchase_of_equity_field",
                       "user_whatif_sim_proceeds_from_issuance_of_debt_field",
                       "user_whatif_sim_repayments_of_long_term_debt_field", "user_whatif_sim_notes_other_split_field"]
        field_names_alt = ["user_whatif_sim_sales_revenue_growth", "user_whatif_sim_cost_of_goods_sold_margin",
                           "user_whatif_sim_sales_general_and_admin_expenses",
                           "user_whatif_sim_research_and_development_expenses",
                           "user_whatif_sim_depreciation_and_amortization_expenses_sales",
                           "user_whatif_sim_depreciation_and_amortization_split", "user_whatif_sim_interest_rate",
                           "user_whatif_sim_tax_rate", "user_whatif_sim_dividend_payout_ratio",
                           "user_whatif_sim_accounts_receivable_days", "user_whatif_sim_inventory_days",
                           "user_whatif_sim_capital_expenditure_sales", "user_whatif_sim_capital_expenditure",
                           "user_whatif_sim_capital_expenditure_indicator", "user_whatif_sim_tangible_intangible_split",
                           "user_whatif_sim_accounts_payable_days", "user_whatif_sim_sale_of_equity",
                           "user_whatif_sim_repurchase_of_equity", "user_whatif_sim_proceeds_from_issuance_of_debt",
                           "user_whatif_sim_repayments_of_long_term_debt", "user_whatif_sim_notes_other_split"]

        format_list = ["%.2f", "%.2f", "%.0f", "%.0f", "%.2f", "%i", "%.2f", "%.2f", "%.2f", "%.0f", "%.0f", "%.2f", "%.0f", "n.a.", "%i", "%.0f", "%.0f", "%.0f", "%.0f", "%.0f", "%i"]
        min_list = [None, 0.00, 0.00, 0.00, 0.00, 0, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, "n.a.", 0, 0.00, 0.00, 0.00, 0.00, 0.00, 0]
        max_list = [None, 100.00, None, None, None, 100, None, None, 100.00, None, None, None, None, "n.a.", 100, None, None, None, None, None, 100]
        step_list = [None, None, 1.00, 1.00, None, None, None, None, None, 1.00, 1.00, None, 1.00, "n.a.", None, 1.00, 1.00, 1.00, 1.00, 1.00, None]
        N = len(st.session_state.user_whatif_manual_field_options)//6
        M = len(st.session_state.user_whatif_manual_field_options)%6
        P = len(st.session_state.user_whatif_simulated_values)

        for i in range(0, P, 1):
            globals()[field_names[field_options.index(st.session_state.user_whatif_simulated_values[i])]] = np.nan
            globals()[field_names_alt[field_options.index(st.session_state.user_whatif_simulated_values[i])]] = np.nan

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            for i in range(0, (N + (1 if M >= 1 else 0)), 1):
                if st.session_state.user_whatif_manual_field_options[i] == "Capital Expenditure Type":
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">%s</span></p>' % st.session_state.user_whatif_manual_field_options[i]
                    st.markdown(text, unsafe_allow_html=True)
                    globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i])]] = st.empty()
                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i])]] = globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i])]].selectbox(
                        label = "", label_visibility = "collapsed",
                        options=["Dollar", "Sales %"],
                        key="whatif_sim_" + str(i + 3), on_change=change_callback3)
#                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i])]] = st.selectbox(
#                        label = "", label_visibility = "collapsed",
#                        options=["Dollar", "Sales %"],
#                        key="whatif_sim_" + str(i + 3))
                else:
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">%s</span></p>' % st.session_state.user_whatif_manual_field_options[i]
                    st.markdown(text, unsafe_allow_html=True)
                    globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i])]] = st.empty()
                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i])]] = globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i])]].number_input(label = "", label_visibility = "collapsed", min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i])], max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i])], step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i])], format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i])], value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i])], key="whatif_sim_"+str(i+3), on_change=change_callback3)
#                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i])]] = st.number_input(label = "", label_visibility = "collapsed", min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i])], max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i])], step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i])], format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i])], value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i])], key="whatif_sim_"+str(i+3))
                st.text("")
        with col2:
            for j in range(0, (N + (1 if M - 1 >= 1 else 0)), 1):
                if st.session_state.user_whatif_manual_field_options[i+j+1] == "Capital Expenditure Type":
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">%s</span></p>' % st.session_state.user_whatif_manual_field_options[i+j+1]
                    st.markdown(text, unsafe_allow_html=True)
                    globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])]] = st.empty()
                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])]] = globals()[field_names[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])]].selectbox(
                        label="", label_visibility="collapsed",
                        options=["Dollar", "Sales %"],
                        key="whatif_sim_" + str(i+j+1+3), on_change=change_callback3)
#                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])]] = st.selectbox(
#                        label = "", label_visibility = "collapsed",
#                        options=["Dollar", "Sales %"],
#                        key="whatif_sim_" + str(i+j+1+3))
                else:
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">%s</span></p>' % st.session_state.user_whatif_manual_field_options[i+j+1]
                    st.markdown(text, unsafe_allow_html=True)
                    globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])]] = st.empty()
                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])]] = globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])]].number_input(label = "", label_visibility = "collapsed", min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])], max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])], step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])], format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])], value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])], key="whatif_sim_"+str(i+j+1+3), on_change=change_callback3)
#                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])]] = st.number_input(label = "", label_visibility = "collapsed", min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])], max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])], step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])], format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])], value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+1])], key="whatif_sim_"+str(i+j+1+3))
                st.text("")
        with col3:
            for k in range(0, (N + (1 if M - 2 >= 1 else 0)), 1):
                if st.session_state.user_whatif_manual_field_options[i+j+k+2] == "Capital Expenditure Type":
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">%s</span></p>' % st.session_state.user_whatif_manual_field_options[i+j+k+2]
                    st.markdown(text, unsafe_allow_html=True)
                    globals()[field_names[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])]] = st.empty()
                    globals()[field_names_alt[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])]] = globals()[
                        field_names[
                            field_options.index(
                                st.session_state.user_whatif_manual_field_options[i+j+k+2])]].selectbox(
                        label="", label_visibility="collapsed",
                        options=["Dollar", "Sales %"],
                        key="whatif_sim_" + str(i+j+k+2+3), on_change=change_callback3)
#                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])]] = st.selectbox(
#                        label = "", label_visibility = "collapsed",
#                        options=["Dollar", "Sales %"],
#                        key="whatif_sim_" + str(i+j+k+2+3))
                else:
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">%s</span></p>' % st.session_state.user_whatif_manual_field_options[i+j+k+2]
                    st.markdown(text, unsafe_allow_html=True)
                    globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])]] = st.empty()
                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])]] = globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])]].number_input(label = "", label_visibility = "collapsed", min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])], max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])], step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])], format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])], value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])], key="whatif_sim_"+str(i+j+k+2+3), on_change=change_callback3)
#                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])]] = st.number_input(label = "", label_visibility = "collapsed", min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])], max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])], step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])], format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])], value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+2])], key="whatif_sim_"+str(i+j+k+2+3))
                st.text("")
        with col4:
            for ii in range(0, (N + (1 if M - 3 >= 1 else 0)), 1):
                if st.session_state.user_whatif_manual_field_options[i+j+k+ii+3] == "Capital Expenditure Type":
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">%s</span></p>' % st.session_state.user_whatif_manual_field_options[i+j+k+ii+3]
                    st.markdown(text, unsafe_allow_html=True)
                    globals()[field_names[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])]] = st.empty()
                    globals()[field_names_alt[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])]] = globals()[
                        field_names[
                            field_options.index(
                                st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])]].selectbox(
                        label="", label_visibility="collapsed",
                        options=["Dollar", "Sales %"],
                        key="whatif_sim_" + str(i+j+k+ii+3+3), on_change=change_callback3)
#                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])]] = st.selectbox(
#                        label = "", label_visibility = "collapsed",
#                        options=["Dollar", "Sales %"],
#                        key="whatif_sim_" + str(i+j+k+ii+3+3))
                else:
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">%s</span></p>' % st.session_state.user_whatif_manual_field_options[i+j+k+ii+3]
                    st.markdown(text, unsafe_allow_html=True)
                    globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])]] = st.empty()
                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])]] = globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])]].number_input(label = "", label_visibility = "collapsed", min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])], max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])], step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])], format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])], value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])], key="whatif_sim_"+str(i+j+k+ii+3+3), on_change=change_callback3)
#                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])]] = st.number_input(label = "", label_visibility = "collapsed", min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])], max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])], step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])], format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])], value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+3])], key="whatif_sim_"+str(i+j+k+ii+3+3))
                st.text("")
        with col5:
            for jj in range(0, (N + (1 if M - 4 >= 1 else 0)), 1):
                if st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4] == "Capital Expenditure Type":
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">%s</span></p>' % st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4]
                    st.markdown(text, unsafe_allow_html=True)
                    globals()[field_names[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])]] = st.empty()
                    globals()[field_names_alt[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])]] = globals()[
                        field_names[
                            field_options.index(
                                st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])]].selectbox(
                        label="", label_visibility="collapsed",
                        options=["Dollar", "Sales %"],
                        key="whatif_sim_" + str(i+j+k+ii+jj+4+3), on_change=change_callback3)
#                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])]] = st.selectbox(
#                        label = "", label_visibility = "collapsed",
#                        options=["Dollar", "Sales %"],
#                        key="whatif_sim_" + str(i+j+k+ii+jj+4+3))
                else:
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">%s</span></p>' % st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4]
                    st.markdown(text, unsafe_allow_html=True)
                    globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])]] = st.empty()
                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])]] = globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])]].number_input(label = "", label_visibility = "collapsed", min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])], max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])], step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])], format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])], value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])], key="whatif_sim_"+str(i+j+k+ii+jj+4+3), on_change=change_callback3)
#                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])]] = st.number_input(label = "", label_visibility = "collapsed", min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])], max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])], step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])], format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])], value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+4])], key="whatif_sim_"+str(i+j+k+ii+jj+4+3))
                st.text("")
        with col6:
            for kk in range(0, (N + (1 if M - 5 >= 1 else 0)), 1):
                if st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5] == "Capital Expenditure Type":
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">%s</span></p>' % st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5]
                    st.markdown(text, unsafe_allow_html=True)
                    globals()[field_names[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])]] = st.empty()
                    globals()[field_names_alt[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])]] = globals()[
                        field_names[
                            field_options.index(
                                st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])]].selectbox(
                        label="", label_visibility="collapsed",
                        options=["Dollar", "Sales %"],
                        key="whatif_sim_" + str(i+j+k+ii+jj+kk+5+3), on_change=change_callback3)
#                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])]] = st.selectbox(
#                        label = "", label_visibility = "collapsed",
#                        options=["Dollar", "Sales %"],
#                        key="whatif_sim_" + str(i+j+k+ii+jj+kk+5+3))
                else:
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">%s</span></p>' % st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5]
                    st.markdown(text, unsafe_allow_html=True)
                    globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])]] = st.empty()
                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])]] = globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])]].number_input(label = "", label_visibility = "collapsed", min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])], max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])], step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])], format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])], value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])], key="whatif_sim_"+str(i+j+k+ii+jj+kk+5+3), on_change=change_callback3)
#                    globals()[field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])]] = st.number_input(label = "", label_visibility = "collapsed", min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])], max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])], step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])], format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])], value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i+j+k+ii+jj+kk+5])], key="whatif_sim_"+str(i+j+k+ii+jj+kk+5+3))
                st.text("")
        col1, col2, col3, col4 = st.columns([4, 1.05, 0.5, 0.5])
        with col1:
            st.text("")
            st.text("")
            instructions_text = '<p style="margin-top: -25px; margin-bottom: 20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Click "Next" once you have made your selections or click "Reset" to reset to the default values.</span></p>'
            st.markdown(instructions_text, unsafe_allow_html=True)
        with col3:
            next_button2 = st.button("Next", key="whatif_sim_2A")
        with col4:
            reset_button2 = st.button("Reset", key="whatif_reset_2")
        if reset_button2:
            st.session_state.next2_confirm = False
            for i in range(0, (N + (1 if M >= 1 else 0)), 1):
                if st.session_state.user_whatif_manual_field_options[i] == "Capital Expenditure Type":
                    globals()[field_names[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i])]].empty()
                    globals()[
                        field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i])]] = \
                    globals()[field_names[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i])]].selectbox(
                        label="", label_visibility="collapsed",
                        options=["Dollar", "Sales %"],
                        key="whatif_simA_" + str(i + 3), on_change=change_callback3)
                else:
                    globals()[field_names[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i])]].empty()
                    globals()[
                        field_names_alt[field_options.index(st.session_state.user_whatif_manual_field_options[i])]] = \
                    globals()[field_names[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i])]].number_input(
                        label="", label_visibility="collapsed",
                        min_value=min_list[field_options.index(st.session_state.user_whatif_manual_field_options[i])],
                        max_value=max_list[field_options.index(st.session_state.user_whatif_manual_field_options[i])],
                        step=step_list[field_options.index(st.session_state.user_whatif_manual_field_options[i])],
                        format=format_list[field_options.index(st.session_state.user_whatif_manual_field_options[i])],
                        value=default_fields[field_options.index(st.session_state.user_whatif_manual_field_options[i])],
                        key="whatif_simA_" + str(i + 3), on_change=change_callback3)
            for j in range(0, (N + (1 if M - 1 >= 1 else 0)), 1):
                if st.session_state.user_whatif_manual_field_options[i + j + 1] == "Capital Expenditure Type":
                    globals()[field_names[field_options.index(
                        st.session_state.user_whatif_manual_field_options[i + j + 1])]].empty()
                    globals()[field_names_alt[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i + j + 1])]] = \
                    globals()[field_names[
                        field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + 1])]].selectbox(
                        label="", label_visibility="collapsed",
                        options=["Dollar", "Sales %"],
                        key="whatif_simA_" + str(i + j + 1 + 3), on_change=change_callback3)
                else:
                    globals()[field_names[field_options.index(
                        st.session_state.user_whatif_manual_field_options[i + j + 1])]].empty()
                    globals()[field_names_alt[
                        field_options.index(st.session_state.user_whatif_manual_field_options[i + j + 1])]] = \
                    globals()[field_names[field_options.index(
                        st.session_state.user_whatif_manual_field_options[i + j + 1])]].number_input(label="",
                                                                                                     label_visibility="collapsed",
                                                                                                     min_value=
                                                                                                     min_list[
                                                                                                         field_options.index(
                                                                                                             st.session_state.user_whatif_manual_field_options[
                                                                                                                 i + j + 1])],
                                                                                                     max_value=
                                                                                                     max_list[
                                                                                                         field_options.index(
                                                                                                             st.session_state.user_whatif_manual_field_options[
                                                                                                                 i + j + 1])],
                                                                                                     step=
                                                                                                     step_list[
                                                                                                         field_options.index(
                                                                                                             st.session_state.user_whatif_manual_field_options[
                                                                                                                 i + j + 1])],
                                                                                                     format=
                                                                                                     format_list[
                                                                                                         field_options.index(
                                                                                                             st.session_state.user_whatif_manual_field_options[
                                                                                                                 i + j + 1])],
                                                                                                     value=
                                                                                                     default_fields[
                                                                                                         field_options.index(
                                                                                                             st.session_state.user_whatif_manual_field_options[
                                                                                                                 i + j + 1])],
                                                                                                     key="whatif_simA_" + str(
                                                                                                         i + j + 1 + 3), on_change=change_callback3)

            for k in range(0, (N + (1 if M - 2 >= 1 else 0)), 1):
                if st.session_state.user_whatif_manual_field_options[
                    i + j + k + 2] == "Capital Expenditure Type":
                    globals()[field_names[
                        field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + 2])]].empty()
                    globals()[field_names_alt[
                        field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + 2])]] = globals()[
                        field_names[
                            field_options.index(
                                st.session_state.user_whatif_manual_field_options[i + j + k + 2])]].selectbox(
                        label="", label_visibility="collapsed",
                        options=["Dollar", "Sales %"],
                        key="whatif_simA_" + str(i + j + k + 2 + 3), on_change=change_callback3)
                else:
                    globals()[field_names[field_options.index(
                        st.session_state.user_whatif_manual_field_options[i + j + k + 2])]].empty()
                    globals()[field_names_alt[field_options.index(
                        st.session_state.user_whatif_manual_field_options[i + j + k + 2])]] = globals()[
                        field_names[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + 2])]].number_input(
                        label="", label_visibility="collapsed", min_value=min_list[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + 2])],
                        max_value=max_list[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + 2])], step=step_list[
                            field_options.index(
                                st.session_state.user_whatif_manual_field_options[i + j + k + 2])],
                        format=format_list[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + 2])],
                        value=default_fields[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + 2])],
                        key="whatif_simA_" + str(i + j + k + 2 + 3), on_change=change_callback3)
            for ii in range(0, (N + (1 if M - 3 >= 1 else 0)), 1):
                if st.session_state.user_whatif_manual_field_options[
                    i + j + k + ii + 3] == "Capital Expenditure Type":
                    globals()[field_names[
                        field_options.index(st.session_state.user_whatif_manual_field_options[
                                                i + j + k + ii + 3])]].empty()
                    globals()[field_names_alt[
                        field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + 3])]] = \
                    globals()[
                        field_names[
                            field_options.index(
                                st.session_state.user_whatif_manual_field_options[
                                    i + j + k + ii + 3])]].selectbox(
                        label="", label_visibility="collapsed",
                        options=["Dollar", "Sales %"],
                        key="whatif_simA_" + str(i + j + k + ii + 3 + 3), on_change=change_callback3)
                else:
                    globals()[field_names[field_options.index(
                        st.session_state.user_whatif_manual_field_options[i + j + k + ii + 3])]].empty()
                    globals()[field_names_alt[field_options.index(
                        st.session_state.user_whatif_manual_field_options[i + j + k + ii + 3])]] = globals()[
                        field_names[field_options.index(st.session_state.user_whatif_manual_field_options[
                                                            i + j + k + ii + 3])]].number_input(label="",
                                                                                                label_visibility="collapsed",
                                                                                                min_value=
                                                                                                min_list[
                                                                                                    field_options.index(
                                                                                                        st.session_state.user_whatif_manual_field_options[
                                                                                                            i + j + k + ii + 3])],
                                                                                                max_value=
                                                                                                max_list[
                                                                                                    field_options.index(
                                                                                                        st.session_state.user_whatif_manual_field_options[
                                                                                                            i + j + k + ii + 3])],
                                                                                                step=step_list[
                                                                                                    field_options.index(
                                                                                                        st.session_state.user_whatif_manual_field_options[
                                                                                                            i + j + k + ii + 3])],
                                                                                                format=
                                                                                                format_list[
                                                                                                    field_options.index(
                                                                                                        st.session_state.user_whatif_manual_field_options[
                                                                                                            i + j + k + ii + 3])],
                                                                                                value=
                                                                                                default_fields[
                                                                                                    field_options.index(
                                                                                                        st.session_state.user_whatif_manual_field_options[
                                                                                                            i + j + k + ii + 3])],
                                                                                                key="whatif_simA_" + str(
                                                                                                    i + j + k + ii + 3 + 3), on_change=change_callback3)

            for jj in range(0, (N + (1 if M - 4 >= 1 else 0)), 1):
                if st.session_state.user_whatif_manual_field_options[
                    i + j + k + ii + jj + 4] == "Capital Expenditure Type":
                    globals()[field_names[
                        field_options.index(st.session_state.user_whatif_manual_field_options[
                                                i + j + k + ii + jj + 4])]].empty()
                    globals()[field_names_alt[
                        field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + 4])]] = \
                    globals()[
                        field_names[
                            field_options.index(
                                st.session_state.user_whatif_manual_field_options[
                                    i + j + k + ii + jj + 4])]].selectbox(
                        label="", label_visibility="collapsed",
                        options=["Dollar", "Sales %"],
                        key="whatif_simA_" + str(i + j + k + ii + jj + 4 + 3), on_change=change_callback3)
                else:
                    globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[
                                                                  i + j + k + ii + jj + 4])]].empty()
                    globals()[field_names_alt[field_options.index(
                        st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + 4])]] = \
                    globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[
                                                                  i + j + k + ii + jj + 4])]].number_input(
                        label="", label_visibility="collapsed", min_value=min_list[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + 4])],
                        max_value=max_list[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + 4])],
                        step=step_list[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + 4])],
                        format=format_list[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + 4])],
                        value=default_fields[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + 4])],
                        key="whatif_simA_" + str(i + j + k + ii + jj + 4 + 3), on_change=change_callback3)
            for kk in range(0, (N + (1 if M - 5 >= 1 else 0)), 1):
                if st.session_state.user_whatif_manual_field_options[
                    i + j + k + ii + jj + kk + 5] == "Capital Expenditure Type":
                    globals()[field_names[
                        field_options.index(st.session_state.user_whatif_manual_field_options[
                                                i + j + k + ii + jj + kk + 5])]].empty()
                    globals()[field_names_alt[
                        field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + kk + 5])]] = \
                    globals()[
                        field_names[
                            field_options.index(
                                st.session_state.user_whatif_manual_field_options[
                                    i + j + k + ii + jj + kk + 5])]].selectbox(
                        label="", label_visibility="collapsed",
                        options=["Dollar", "Sales %"],
                        key="whatif_simA_" + str(i + j + k + ii + jj + kk + 5 + 3), on_change=change_callback3)
                else:
                    globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[
                                                                  i + j + k + ii + jj + kk + 5])]].empty()
                    globals()[field_names_alt[field_options.index(
                        st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + kk + 5])]] = \
                    globals()[field_names[field_options.index(st.session_state.user_whatif_manual_field_options[
                                                                  i + j + k + ii + jj + kk + 5])]].number_input(
                        label="", label_visibility="collapsed", min_value=min_list[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + kk + 5])],
                        max_value=max_list[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + kk + 5])],
                        step=step_list[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + kk + 5])],
                        format=format_list[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + kk + 5])],
                        value=default_fields[field_options.index(
                            st.session_state.user_whatif_manual_field_options[i + j + k + ii + jj + kk + 5])],
                        key="whatif_simA_" + str(i + j + k + ii + jj + kk + 5 + 3), on_change=change_callback3)

        if next_button2:
            st.session_state.next2_confirm = True
        if st.session_state.next2_confirm == True:
            st.text("")
            subtext1 = '<p style="margin-bottom: 0px;"><span style="font-family:sans-serif; color:#25476A; font-size: 40px;">Simulation Details</span></p>'
            st.markdown(subtext1, unsafe_allow_html=True)
            st.markdown(line, unsafe_allow_html=True)
            st.markdown(line2, unsafe_allow_html=True)
            instructions_text = '<p style="margin-top: -25px; margin-bottom: 20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Enter number of simulated iterations and use the dropdown menu to select seed option. Click "Run" once you have made your selections or click "Reset" to reset to the default selection.</span></p>'
            st.markdown(instructions_text, unsafe_allow_html=True)
            col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([0.85, 0.15, 0.85, 0.15, 1, 2, 0.5, 0.5])
            with col1:
                text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Number of Iterations (Min 1,000)</span></p>'
                st.markdown(text, unsafe_allow_html=True)
                user_whatif_iterations_field = st.empty()
                st.session_state.user_whatif_iterations = user_whatif_iterations_field.number_input(label = "", label_visibility = "collapsed", min_value=3, max_value=100000, step=1000, format="%i", value=3, key="whatif_sim_2B", on_change=change_callback4)

            with col2:
                st.markdown(
                    """
                    <style>
                    /* Tooltip container */
                    .tooltip2 {
                        position: relative;
                        display: inline-block;
                #        border-bottom: 1px dotted black;
                    }

                    /* Tooltip text */
                    .tooltip2 .tooltiptext {
                        visibility: hidden;
                        width: 600px;
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
                        margin-left: -300px;

                        /* Fade in tooltip */
                        opacity: 0;
                        transition: opacity 0.3s;
                    }

                    /* Tooltip arrow */
                    .tooltip2 .tooltiptext::after {
                        content: "";
                        position: absolute;
                        top: 100%;
                        left: 50%;
                        margin-left: -5px;
                        border-width: 5px;
                        border-style: solid;
                        border-color: #25476A transparent transparent transparent;
                    }

                    /* Show the tooltip text when you mouse over the tooltip container */
                    .tooltip2:hover .tooltiptext {
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
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown(
                    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">',
                    unsafe_allow_html=True)
                st.markdown(
                    """
                    <div class="tooltip2">
                    <i class="fas fa-info-circle fa-2x"></i>
                    <span class="tooltiptext">The number of iterations in a simulation refers to the number of times the simulation model is run. A higher number of iterations can generally provide more accurate results, but may also require longer processing time and vice versa.</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col3:
                text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Seed</span></p>'
                st.markdown(text, unsafe_allow_html=True)
                user_seed_option_field = st.empty()
                seed_options = ["", "Manually Set Seed", "Randomly Set Seed"]
                user_seed_option_field.selectbox(label="", label_visibility="collapsed", options=seed_options,
                             format_func=lambda x: "Select Seed Option" if x == "" else x, key="user_seed_option", on_change=change_callback4)
            with col4:
                st.text("")
                st.text("")
                st.markdown(
                    """
                    <div class="tooltip2">
                    <i class="fas fa-info-circle fa-2x"></i>
                    <span class="tooltiptext">In a simulation, the seed is a fixed numerical value that is used as an input to a random number generator algorithm to generate a sequence of numbers that have a certain degree of randomness but are deterministic and reproducible. Manually setting the seed ensures that the same sequence of random numbers is generated, allowing for consistent and reproducible results. By not manually setting the seed and instead allowing it to be randomly set, the results of the simulation will vary each time.</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col5:
                seed_value_text = st.empty()
                seed_value_field = st.empty()
                if st.session_state.user_seed_option == "Manually Set Seed":
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Seed Value (Max 4 Digits)</span></p>'
                    seed_value_text.markdown(text, unsafe_allow_html=True)
                    st.session_state.seed_value = seed_value_field.number_input(label="", label_visibility="collapsed",
                                                                     min_value=0, max_value=9999, step=1, format="%i", value=1111,
                                                                     key="whatif_sim_3C", on_change=change_callback4)
                if st.session_state.user_seed_option == "Randomly Set Seed":
                    if 'seed_value' not in st.session_state:
                        st.session_state.seed_value = random.randint(0, 9999)
            with col6:
                seed_text_field = st.empty()
                if st.session_state.user_seed_option == "Randomly Set Seed":
                    seed_text = '<p style="margin-top: 30px; margin-bottom: 0px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">A seed value of {} was randomly selected.</span></p>'.format(
                        st.session_state.seed_value)
                    seed_text_field.markdown(seed_text, unsafe_allow_html=True)
            with col7:
                st.text("")
                st.text("")
                submit3_button = st.button("Run", key="whatif_sim_2C")
            with col8:
                st.text("")
                st.text("")
                reset_button3 = st.button("Reset", key="whatif_reset_3", on_click=reset4)
            if reset_button3:
#                st.session_state.submit3_confirm = False
#                st.session_state.user_seed_option = seed_options[0]
                user_whatif_iterations_field.empty()
                st.session_state.user_whatif_iterations = user_whatif_iterations_field.number_input(label="",
                                                                                                    label_visibility="collapsed",
                                                                                                    min_value=3,
                                                                                                    max_value=100000,
                                                                                                    step=1000,
                                                                                                    format="%i",
                                                                                                    value=3,
                                                                                                    key="whatif_sim_2BA")
#                    user_seed_option_field.empty()
#                    st.session_state.user_seed_option = user_seed_option_field.selectbox(label="", label_visibility="collapsed", options=["","Manually Set Seed","Random Seed"],
#                                 format_func=lambda x: "Select Seed Option" if x == "" else x, key="whatif_sim_3BA")
#                    st.session_state.seed_value = random.randint(0, 9999)
                if "seed_value" in st.session_state:
                    del st.session_state.seed_value
                    seed_value_text.empty()
                    seed_value_field.empty()


            #            st.markdown('<p> <span style="font-family:sans-serif; color:white; font-size: 14px;">%s</span></p>' %('Estimated Runtime: Approx '+str(int(350/20000*st.session_state.user_whatif_iterations))+' Seconds'), unsafe_allow_html=True)
            if submit3_button:
                if st.session_state.user_seed_option == "":
                    st.session_state.simulation_run_confirm = False
                    col1, col2, col3 = st.columns([1, 4, 1])
                    st.text("")
                    st.text("")
                    with col2:
                        st.error("**Error**: please complete selection.")
                else:
                    st.session_state.submit3_confirm = True
                    st.session_state.df_ratings_sim_out, st.session_state.df_income_statement_sim_out, st.session_state.df_cash_flow_statement_sim_out, st.session_state.df_balance_sheet_statement_sim_out = run_simulation(st.session_state.seed_value, st.session_state.user_sector, st.session_state.user_whatif_simulated_values, st.session_state.user_whatif_manual_field_options, st.session_state.user_whatif_iterations, user_whatif_sim_sales_revenue_growth, user_whatif_sim_cost_of_goods_sold_margin,
                       user_whatif_sim_sales_general_and_admin_expenses,
                       user_whatif_sim_research_and_development_expenses,
                       user_whatif_sim_depreciation_and_amortization_expenses_sales,
                       user_whatif_sim_depreciation_and_amortization_split, user_whatif_sim_interest_rate,
                       user_whatif_sim_tax_rate, user_whatif_sim_dividend_payout_ratio,
                       user_whatif_sim_accounts_receivable_days, user_whatif_sim_inventory_days,
                       user_whatif_sim_capital_expenditure_sales, user_whatif_sim_capital_expenditure,
                       user_whatif_sim_capital_expenditure_indicator, user_whatif_sim_tangible_intangible_split,
                       user_whatif_sim_accounts_payable_days, user_whatif_sim_sale_of_equity,
                       user_whatif_sim_repurchase_of_equity, user_whatif_sim_proceeds_from_issuance_of_debt,
                       user_whatif_sim_repayments_of_long_term_debt, user_whatif_sim_notes_other_split)
                    st.session_state.simulation_run_confirm = True

            if st.session_state.submit3_confirm == True and st.session_state.simulation_run_confirm == True:
                col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
                with col1:
                    st.text("")
                    st.text("")
                    st.markdown(
                        '<p style="margin-bottom: 0px ;"><span style="font-family:sans-serif; color:#25476A; font-size: 40px;">Simulation Results</span></p>',
                        unsafe_allow_html=True)
                with col4:
                    text = '<p style="margin-bottom: 2px; margin-top: 20px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Download Simulation Output</span></p>'
                    st.markdown(text, unsafe_allow_html=True)
                    statement_out_download_field = st.empty()
                    statement_out_download = statement_out_download_field.selectbox(label="",
                                                                                             label_visibility="collapsed",
                                                                                             options=[
                                                                                                 "Select To Download",
                                                                                                 "Yes"],
                                                                                             key="sim_download1")
                with col5:
                    if statement_out_download == "Yes":
                        spinner = st.markdown(marker_spinner_css, unsafe_allow_html=True)
                        spinner_image = st.markdown(spinner_image_css.format(img_to_bytes("images/spinner_center.png")), unsafe_allow_html=True)
                        st.text("")
                        st.text("")
                        statements_out = [(st.session_state.df_ratings_sim_out.reset_index(
                            drop=True).to_csv().encode(), "simulation_analysis_rating", "csv"), (st.session_state.df_income_statement_sim_out.reset_index(
                            drop=True).to_csv().encode(), "simulation_analysis_income_statement", "csv"), (
                                          st.session_state.df_cash_flow_statement_sim_out.reset_index(
                                              drop=True).to_csv().encode(), "simulation_analysis_cashflow_statement", "csv"), (
                                          st.session_state.df_balance_sheet_statement_sim_out.reset_index(
                                              drop=True).to_csv().encode(), "simulation_analysis_balance_sheet", "csv")]
                        downloader = MultiFileDownloader()
                        downloader.download_simulation_figures(statements_out, st.session_state.user_entity_name)
                        spinner.empty()
                        spinner_image.empty()

                st.markdown(line, unsafe_allow_html=True)
                st.markdown(line2, unsafe_allow_html=True)
                information_text = '<p style="margin-top: -25px; margin-bottom: 20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">The simulation analysis has generated {} iterations of the company financial statements (based on a seed value of {}) and produced distributions of potential rating outcomes and financial statement variable values. Based on the generated distributions, multiple statistics may be calculated to provide an overall understanding of the dataset.</span></p>'.format(
                    '{:,.0f}'.format(st.session_state.user_whatif_iterations), st.session_state.seed_value)
                st.markdown(information_text, unsafe_allow_html=True)
                st.text("")
                currency = get_financials(st.session_state.df_input, st.session_state.user_entity_name, st.session_state.user_reporting_period)[
                    'currency_iso'].values[0]
                text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 24px;">Credit Rating</span></p>'
                st.markdown(text, unsafe_allow_html=True)
                text = '<p style="margin-top: 0px; margin-bottom: 20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;"> Enter a confidence level to calculate a Rating VaR statistic. Click "Next" once you have made your selections or click "Reset" to reset to the default selection.</span></p>'
                st.markdown(text, unsafe_allow_html=True)
                col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 0.5, 0.5])
                with col1:
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Confidence Level %</span></p>'
                    st.markdown(text, unsafe_allow_html=True)
                    user_whatif_confidence_level_field = st.empty()
                    if "user_whatif_confidence_level" not in st.session_state:
                        user_whatif_confidence_level_field.number_input(
                            label="", label_visibility="collapsed", min_value=0.00, max_value=100.00, step=0.01,
                            format="%.2f",
                            value=95.00, key="user_whatif_confidence_level", on_change=change_callback5)
                    else:
                        user_whatif_confidence_level_field.number_input(
                            label="", label_visibility="collapsed", min_value=0.00, max_value=100.00, step=0.01,
                            format="%.2f",
                            value=st.session_state.user_whatif_confidence_level, key="user_whatif_confidence_level", on_change=change_callback5)

                    
                    
                with col2:
                    st.markdown("""
                                        <style>
                                        /* Tooltip container */
                                        .tooltip2 {
                                            position: relative;
                                            display: inline-block;
                                    #        border-bottom: 1px dotted black;
                                        }

                                        /* Tooltip text */
                                        .tooltip2 .tooltiptext {
                                            visibility: hidden;
                                            width: 600px;
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
                                            margin-left: -300px;

                                            /* Fade in tooltip */
                                            opacity: 0;
                                            transition: opacity 0.3s;
                                        }

                                        /* Tooltip arrow */
                                        .tooltip2 .tooltiptext::after {
                                            content: "";
                                            position: absolute;
                                            top: 100%;
                                            left: 50%;
                                            margin-left: -5px;
                                            border-width: 5px;
                                            border-style: solid;
                                            border-color: #25476A transparent transparent transparent;
                                        }

                                        /* Show the tooltip text when you mouse over the tooltip container */
                                        .tooltip2:hover .tooltiptext {
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
                                        </style>
                                        """,
                                unsafe_allow_html=True
                                )
                    st.markdown(
                        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">',
                        unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div class="tooltip2">
                        <i class="fas fa-info-circle fa-2x"></i>
                        <span class="tooltiptext">Comrate calculates a Rating Value-at-Risk (VaR) statistic as an estimate of the potential downside risk associated with a company's credit rating.  Specifically, the Rating VaR quantifies the maximum (worst) expected deterioration in the credit rating within a certain time period at a given confidence level (often 95% or 99%). For example, a company with a Rating VaR of B+ at a 95% confidence level implies that there is a 95% chance that the company's rating will not decline to a grade worse than a B+ rating within the next year based on historical industry correlations.  The higher the confidence level, the higher the downside risk and vice versa.</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                with col6:
                    st.text("")
                    st.text("")
                    submit4_button = st.button("Next", key="whatif_sim_2CA")
                with col7:
                    st.text("")
                    st.text("")
                    reset_button4 = st.button("Reset", key="whatif_reset_4", on_click=reset5)

                if submit4_button:
                    st.session_state.next3_confirm = True

                if st.session_state.next3_confirm == True:
                    st.text("")
                    current_rating = "BBB+"
                    categories = ['AAA', 'AA+', 'AA', 'AA-', 'A+', 'A', 'A-', 'BBB+', 'BBB', 'BBB-', 'BB+', "BB", 'BB-',
                                  'B+', 'B', 'B-', 'CCC+', 'CCC', 'CCC-', 'CC', 'C', 'D']
                    rating_dict = {'AAA': 1, 'AA+': 2, 'AA': 3, 'AA-': 4, 'A+': 5, 'A': 6, 'A-': 7, 'BBB+': 8,
                                          'BBB': 9,
                                          'BBB-': 10, 'BB+': 11, 'BB': 12, 'BB-': 13, 'B+': 14, 'B': 15, 'B-': 16,
                                          'CCC+': 17,
                                          'CCC': 18, 'CCC-': 19, 'CC': 20, 'C': 21, 'D': 22}
                    cat_counts = st.session_state.df_ratings_sim_out["Credit Rating"].value_counts(normalize=True)
                    df_ratings_density = pd.DataFrame({"Credit Rating": categories, "Density": [cat_counts.get(cat, 0) for cat in categories]})
                    max_y = df_ratings_density["Density"].max()*100
                    ratings = pd.Categorical(st.session_state.df_ratings_sim_out["Credit Rating"], categories, ordered=True)
                    median_rating = categories[int(np.median(ratings.codes))]
                    mode_rating = st.session_state.df_ratings_sim_out["Credit Rating"].mode().values[0]
                    min_rating = ratings.max()
                    twenty_fifth_percentile = categories[int(np.percentile(ratings.codes, 25))]
                    seventy_fifth_percentile = categories[int(np.percentile(ratings.codes, 75))]
                    max_rating = ratings.min()
                    var_rating = categories[int(np.percentile(ratings.codes, st.session_state.user_whatif_confidence_level))]
                    var_rating_text = '{:,.2f}'.format(st.session_state.user_whatif_confidence_level)

                    styles2 = """
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
                                    .left2 {
                                        text-align: left;
                                        justify-content: left;
                                        float: left;
                                        width: 35%;
                                        padding-top: 10px;
                                        padding-bottom: 0px;
                    #                    padding: 10px;
                                    }
                                    .middle2 {
                                        text-align: center;
                                        justify-content: center;
                                        float: left;
                                        width: 30%;
                                        padding-top: 10px;
                                        padding-bottom: 0px;
                    #                    padding: 10px;
                                    }
                                    .right2 {
                                        text-align: right;
                                        justify-content: right;
                                        float: left;
                                        width: 35%;
                                        padding-top: 10px;
                                        padding-bottom: 0px;
                    #                    padding: 10px;
                                    }
                                </style>
                            """
                    st.markdown(styles2, unsafe_allow_html=True)


                    left_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 44px;'>{}&nbsp;{}&nbsp;{}</span>".format(
                        str(st.session_state.user_reporting_period), "Rating:", current_rating)
                    middle_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 44px;'>{}&nbsp;{}</span>".format(
                        "Median Rating:", median_rating)
                    right_text = "<span style='font-family: sans-serif; color: #FAFAFA; font-size: 44px;'>{}{}&nbsp;{}</span>".format(
                        var_rating_text, "% Rating VaR:", var_rating)
                    html = f"<div class='col'><div class='left2'>{left_text}</div><div class='middle2'>{middle_text}</div><div class='right2'>{right_text}</div></div>"
                    st.markdown(html, unsafe_allow_html=True)
                    text = '<p style="margin-top: 20px; margin-bottom: 10px;"><span style="color: #25476A; background-color: rgba(3, 169, 244, 0.2); border-radius:6px; padding-left:12px; padding-right: 12px; padding-top:12px; padding-bottom:12px; font-family:sans-serif; font-size: 24px; display: block; width: 100%; border: 3px solid #25476A; font-weight: bold;">Comrate&apos;s proprietary credit ratings model calculates a {} rating for {} at {} and predicts a median rating of {} and a {}% Rating VaR of {} based on the simulation analysis. This result implies that {}&apos;s expected rating is {} and there is a {}% chance that {}&apos;s rating will decline to a grade worse than a {} within the next year based on historical industry correlations.</span></p>'.format(current_rating, st.session_state.user_entity_name, st.session_state.user_reporting_period, median_rating, var_rating_text, var_rating, st.session_state.user_entity_name, median_rating, '{:,.2f}'.format(100-st.session_state.user_whatif_confidence_level), st.session_state.user_entity_name, var_rating)
                    st.markdown(text, unsafe_allow_html=True)
                    text = '<p style="margin-top: 10px; margin-bottom: 10px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Simulation statistics refer to the statistical properties of a set of simulated data points that follow a specific distribution. These statistics represent a way to summarize and understand the characteristics of the simulated dataset, which can be useful for making predictions and decisions based on the simulation results.</span></p>'
                    st.markdown(text, unsafe_allow_html=True)

                    st.session_state["df_rating_summary"] = pd.DataFrame(columns=[st.session_state.user_reporting_period])
                    st.session_state.df_rating_summary.loc[0, st.session_state.user_reporting_period] = current_rating
                    st.session_state.df_rating_summary.insert(loc=1, column="Count", value=len(st.session_state.df_ratings_sim_out["Credit Rating"]))
                    st.session_state.df_rating_summary.insert(loc=2, column="Median", value=median_rating)
                    st.session_state.df_rating_summary.insert(loc=3, column="Mode", value=mode_rating)
                    st.session_state.df_rating_summary.insert(loc=4, column="Rating VaR", value=var_rating)
                    st.session_state.df_rating_summary.insert(loc=5, column="Minimum", value=min_rating)
                    st.session_state.df_rating_summary.insert(loc=6, column="25% Quantile", value=seventy_fifth_percentile)
                    st.session_state.df_rating_summary.insert(loc=7, column="75% Quantile", value=twenty_fifth_percentile)
                    st.session_state.df_rating_summary.insert(loc=8, column="Maximum", value=max_rating)
                    st.session_state.df_rating_summary.columns = pd.MultiIndex.from_arrays([['Simulation Statistics',
                                                                                      'Simulation Statistics',
                                                                                      'Simulation Statistics',
                                                                                      'Simulation Statistics',
                                                                                      'Simulation Statistics',
                                                                                      'Simulation Statistics',
                                                                                      'Simulation Statistics','Simulation Statistics','Simulation Statistics'], [
                                                                                         st.session_state.user_reporting_period,
                                                                                         "Iterations", "Median", "Mode", "{}% Rating VaR".format(var_rating_text),
                                                                                         "Minimum",
                                                                                         "25% Quantile", "75% Quantile",
                                                                                         "Maximum"]])
                    rating_stats_table = st.session_state.df_rating_summary.style.set_table_styles(
                        [{'selector': 'td', 'props': [('color', '#25476A')]}, {'selector': 'th',
                                                                               'props': [
                                                                                   ('text-align', 'center'),
                                                                                   ('font-weight', 'bold'), (
                                                                                       'background-color',
                                                                                       '#25476A'),
                                                                                   ('color', '#FAFAFA')]},
                         {'selector': 'td:hover',
                          'props': [('background-color',
                                     'rgba(111, 114, 222, 0.4)')]},
                         {'selector': 'td',
                          'props': [('border',
                                     '0.5px solid #25476A')]},
                         {'selector': '', 'props': [(
                             'border',
                             '3px solid #25476A')]}]).set_properties(**{'text-align': 'center'},
                                                                     **{'width': '160px'}).hide_index()
                    st.text("")
                    col1, col2, col3  = st.columns([0.2, 2, 0.2])
                    with col2:
                        st.markdown(f"""<div style="display: flex; justify-content: center;">{rating_stats_table.to_html()}</div>""",
                                    unsafe_allow_html=True)
                    with col3:
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
                                <i class="fas fa-info-circle fa-2x"></i>
                                <span class="tooltiptext">
                                    <ul>
                                    The table presents common statistics used to describe the distribution of a dataset.                               
                                        <li>Count: The number of data points in the dataset.</li>
                                        <li>Mean: The sum of all the data points divided by the number of data points.  The mean is also known as the average.</li>
                                        <li>Median: The middle value that separates the ordered dataset into two equal halves. Half of the values are greater than the median and half are less than the median. The median is also known as the 50% quantile.</li>
                                        <li>Mode: The most frequently occurring value in the dataset.</li>
                                        <li>Standard deviation: A measure of how spread out the data is from the mean. A lower standard deviation indicates that the data is clustered closer to the mean, while a higher standard deviation indicates that the data is more spread out from the mean.</li>
                                        <li>Value-at-Risk (VaR): A measure of the potential downside risk associated with the simulated dataset. Specifically, it quantifies the maximum (worst) expected deterioration within a certain time period at a given confidence level (often 95% or 99%).</li>
                                        <li>Minimum: The smallest value in the dataset.</li>
                                        <li>25% Quantile: The value below which 25% of the data falls and above which 75% of the data is distributed.  The 25% quantile is also known as the first quartile.</li>
                                        <li>75% Quantile: The value below which 75% of the data falls and above which 25% of the data is distributed.  The 75% quantile is also known as the third quartile.</li>
                                        <li>Maximum: The largest value in the dataset.</li>                                    
                                    These statistics can help provide an overall understanding of how the data is distributed and can be used to make comparisons with other datasets.
                                    </ul>
                                </span>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    st.text("")
                    text = '<p style="margin-top: 10px; margin-bottom: -20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Data visualization tools give a valuable insight into the structure of the simulated dataset.  Plotting the simulated data points presents a graphical representation of the data over multiple iterations.  A histogram is used to visualize the frequency distribution of the simulated data. Displaying the actual value in addition to the simulated median and value-at-risk (VaR) statistics on these plots provides additional insights into the simulated data points and the underlying downside and upside risk profiles.</span></p>'
                    st.markdown(text, unsafe_allow_html=True)
                    ratings_hist_fig = px.histogram(st.session_state.df_ratings_sim_out["Credit Rating"], nbins=len(categories),
                                                    cumulative=False,
                                                    marginal="box",
                                                    histnorm="percent",
                                                    color_discrete_sequence=["#25476A"], category_orders={"x": categories})
                    for cat in categories:
                        if cat not in st.session_state.df_ratings_sim_out['Credit Rating'].unique():
                            zero_trace = {"x": [cat], "y": [0], "type": "bar", "marker": {"color": "#25476A"}}
                            ratings_hist_fig.add_trace(zero_trace)
                    bin_size = 1
                    mapped_data = st.session_state.df_ratings_sim_out["Credit Rating"].map(rating_dict)
                    kde_fig = ff.create_distplot([mapped_data], group_labels=["distplot"], histnorm="probability density", bin_size=bin_size,
                                                     curve_type="kde")
                    kde_fig_x = kde_fig.data[1]["x"]
                    kde_fig_y = kde_fig.data[1]["y"]*100
                    credit_rating_counts = {}
                    for category in categories:
                        credit_rating_counts[category] = cat_counts.get(category, 0)

                    rounded_x = [int(round(x)) for x in kde_fig_x]
                    summed_y_dict = {}
                    for i in range(len(rounded_x)):
                        if rounded_x[i] in summed_y_dict:
                            summed_y_dict[rounded_x[i]].append(kde_fig_y[i])
                        else:
                            summed_y_dict[rounded_x[i]] = [kde_fig_y[i]]

                    averaged_x = []
                    averaged_y = []
                    for key in summed_y_dict:
                        averaged_x.append(key)
                        averaged_y.append(sum(summed_y_dict[key]) / len(summed_y_dict[key]))
                    category_dict = dict(enumerate(categories, start=1))
                    averaged_x_categories = [category_dict[x] for x in averaged_x]

                    ratings_hist_fig.add_traces(
                        go.Scatter(x=averaged_x_categories, y=averaged_y, mode="lines", line=dict(color="#03A9F4", width=3),
                                   showlegend=False))

                    ratings_hist_fig.update_layout(
                        {"plot_bgcolor": "rgba(0, 0, 0, 0)", "paper_bgcolor": "rgba(0, 0, 0, 0)"})
                    ratings_hist_fig.add_annotation(
                        dict(font=dict(color="#25476A", size=24, family="sans-serif"), x=-0.15, y=1.14, xref="paper",
                             yref="paper", showarrow=False,
                             text="Histogram ({} Iterations)".format('{:,.0f}'.format(st.session_state.user_whatif_iterations))))
                    ratings_hist_fig.add_annotation(
                        dict(font=dict(color="#25476A", size=14, family="sans-serif"), x=-0.12, y=-0.22,
                             xref="paper",
                             yref="paper", showarrow=False,
                             text="Seed {}".format(st.session_state.seed_value)))
                    ratings_hist_fig.update_xaxes(showline=False, showgrid=False, zeroline=False)
                    ratings_hist_fig.update_yaxes(showline=False, showgrid=False, zeroline=False)
                    ratings_hist_fig.update_xaxes(categoryorder='array', categoryarray=categories)
                    ratings_hist_fig.update_traces(marker_line_width=2, marker_line_color="#FAFAFA")
                    ratings_hist_fig.update_layout(plot_bgcolor="#C5C6C7", bargap=0, width=800 * 0.9,
                                                   height=600 * 0.9,
                                                   yaxis_title=dict(text="Frequency (%)",
                                                                    font=dict(size=20, color="#25476A")),
                                                   xaxis_title=dict(text="Credit Rating",
                                                                    font=dict(size=20, color="#25476A")),
                                                   yaxis=dict(tickfont=dict(size=18, color="#25476A")),
                                                   xaxis=dict(tickangle=90, tickfont=dict(size=18, color="#25476A")),
                                                   showlegend=False,  margin=dict(
            l=100,
            r=40,
            b=100,
            t=70
        ), shapes=[go.layout.Shape(
            type="rect",
                 xref="paper", yref="paper",
                 x0=-0.15, y0=-0.26, x1=1.03, y1=1.04, line={'width': 2.5, 'color': '#25476A', 'dash': 'solid'})])
                    ratings_hist_fig.add_vline(x=current_rating, line_width=3,
                                                                               line_dash="dash", line_color='#FA9F1B')
                    ratings_hist_fig.add_annotation(
                                            dict(font=dict(color='#FA9F1B', family="sans-serif", size=18), x=current_rating,
                                                 y=max_y, align="right", xanchor="left", yanchor="top", textangle=90,
                                                 showarrow=False,
                                                 text=st.session_state.user_reporting_period + ": " + current_rating))

                    ratings_hist_fig.add_vline(x=median_rating, line_width=3,
                                                                               line_dash="dash", line_color='#0FCC2E')
                    ratings_hist_fig.add_annotation(
                                            dict(font=dict(color='#0FCC2E', family="sans-serif", size=18), x=median_rating,
                                                 y=max_y, align="right", xanchor="left", yanchor="top", textangle=90,
                                                 showarrow=False,
                                                 text="Median: " + median_rating))
                    ratings_hist_fig.add_vline(x=var_rating, line_width=3,
                                                                               line_dash="dash", line_color='#AB47BC')
                    ratings_hist_fig.add_annotation(
                                            dict(font=dict(color='#AB47BC', family="sans-serif", size=18), x=var_rating,
                                                 y=max_y, align="right", xanchor="left", yanchor="top", textangle=90,
                                                 showarrow=False,
                                                 text="{}% Rating VaR: ".format(var_rating_text) + var_rating))

                    ratings_line_fig = px.line(st.session_state.df_ratings_sim_out, x="Iteration", y="Credit Rating",
                                               markers=True, template="plotly",
                                               color_discrete_sequence=["#25476A"],
                                               category_orders={"Credit Rating": categories},
                                               range_y=[categories[0], categories[-1]])
                    ratings_line_fig.update_layout(
                        {"plot_bgcolor": "rgba(0, 0, 0, 0)", "paper_bgcolor": "rgba(0, 0, 0, 0)"})
                    ratings_line_fig.update_traces(line=dict(width=3))
                    ratings_line_fig.add_annotation(
                        dict(font=dict(color="#25476A", size=24, family="sans-serif"), x=-0.2, y=1.14, xref="paper",
                             yref="paper", showarrow=False,
                             text="Simulated Values ({} Iterations)".format('{:,.0f}'.format(st.session_state.user_whatif_iterations))))
                    ratings_line_fig.add_annotation(
                        dict(font=dict(color="#25476A", size=14, family="sans-serif"), x=-0.18, y=-0.31,
                             xref="paper",
                             yref="paper", showarrow=False,
                             text="Seed {}".format(st.session_state.seed_value)))
                    ratings_line_fig.update_xaxes(showline=False, showgrid=False, zeroline=False,
                                                  tickangle=-90)
                    ratings_line_fig.update_yaxes(showline=False, showgrid=False, zeroline=False)
                    ratings_line_fig.update_yaxes(tickvals=categories, range=[-0.5, len(categories)-0.5])
                    ratings_line_fig.update_layout(plot_bgcolor="#C5C6C7", width=800 * 0.9,
                                                   height=600 * 0.9,
                                                   yaxis_title=dict(text="Credit Rating",
                                                                    font=dict(size=20, color="#25476A")),
                                                   xaxis_title=dict(
                                                       text="Iteration",
                                                       font=dict(size=20, color="#25476A")), yaxis=dict(
                            tickfont=dict(size=18, color="#25476A")), xaxis=dict(
                            tickfont=dict(size=18, color="#25476A")), showlegend=False, margin=dict(
            l=120,
            r=40,
            b=130,
            t=70
        ), shapes=[go.layout.Shape(
            type="rect",
                 xref="paper", yref="paper",
                 x0=-0.2, y0=-0.36, x1=1.03, y1=1.04, line={'width': 2.5, 'color': '#25476A', 'dash': 'solid'})])
                    ratings_line_fig.add_hline(y=0, line_width=0, line_dash="dash", line_color='rgba(0, 0, 0, 0)')
                    ratings_line_fig.add_hline(y=current_rating, line_width=3,
                                                                               line_dash="dash", line_color='#FA9F1B')
                    ratings_line_fig.add_annotation(
                                            dict(font=dict(color='#FA9F1B', family="sans-serif", size=18), y=current_rating,
                                                 align="right",  xanchor="left", yanchor="bottom",
                                                 showarrow=False,
                                                 text=st.session_state.user_reporting_period + ": " + current_rating))
                    ratings_line_fig.add_hline(y=median_rating, line_width=3,
                                                                               line_dash="dash", line_color='#0FCC2E')
                    ratings_line_fig.add_annotation(
                                            dict(font=dict(color='#0FCC2E', family="sans-serif", size=18), y=median_rating,
                                                 align="right",  xanchor="left", yanchor="bottom",
                                                 showarrow=False,
                                                 text="Median: " + median_rating))
                    ratings_line_fig.add_hline(y=var_rating, line_width=3,
                                                                               line_dash="dash", line_color='#AB47BC')
                    ratings_line_fig.add_annotation(
                                            dict(font=dict(color='#AB47BC', family="sans-serif", size=18), y=var_rating,
                                                 align="right",  xanchor="left", yanchor="bottom",
                                                 showarrow=False,
                                                 text="{}% Rating VaR: ".format(var_rating_text) + var_rating))

                    col1, col2, col3, col4, col5  = st.columns([0.1, 1, 0.2, 1, 0.1])
                    with col2:
                        st.plotly_chart(ratings_line_fig, config={'displayModeBar': False})
                    with col4:
                        st.plotly_chart(ratings_hist_fig, config={'displayModeBar': False})
                    col1, col2 = st.columns([1, 5])
                    with col1:
                        text = '<p style="margin-bottom: -5px; margin-top: 10px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Download Visualizations</span></p>'
                        st.markdown(text, unsafe_allow_html=True)
                        statement_out_download_field = st.empty()
                        statement_out_download = statement_out_download_field.selectbox(label="",
                                                                                                 label_visibility="collapsed",
                                                                                                 options=[
                                                                                                     "Select To Download",
                                                                                                     "Yes"],
                                                                                                 key="sim_download2")
                    with col2:
                        if statement_out_download == "Yes":
                            spinner = st.markdown(marker_spinner_css, unsafe_allow_html=True)
                            spinner_image = st.markdown(spinner_image_css.format(img_to_bytes("images/spinner_center.png")), unsafe_allow_html=True)
                            st.text("")
                            st.text("")
                            ratings_plots_out = [(rating_stats_table.set_properties(**{'width': '130px'}), "simulation_analysis_rating_statistics", "png", 90, "table", "Credit Rating", st.session_state.user_entity_name), (ratings_line_fig.update_layout({"paper_bgcolor": "rgba(255,255, 255, 1)"}).to_image(format="png"), "simulation_analysis_rating_values", "png", 150, "figure", "", st.session_state.user_entity_name), (ratings_hist_fig.update_layout({"paper_bgcolor": "rgba(255,255, 255, 1)"}).to_image(format="png"), "simulation_analysis_rating_histogram", "png", 150, "figure", "", st.session_state.user_entity_name)]
                            downloader = MultiFileDownloader()
                            downloader.export_tables_figures(ratings_plots_out, st.session_state.user_entity_name)
                            spinner.empty()
                            spinner_image.empty()
                    st.text("")
                    st.text("")
                    text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 24px;">Financial Variables</span></p>'
                    st.markdown(text, unsafe_allow_html=True)
                    information_text = '<p style="margin-top: 0px; margin-bottom: 20px;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Use the dropdown menus to select the simulated financial statement and financial field. Click "Next" once you have made your selections or click "Cancel" to reset.</span></p>'
                    st.markdown(information_text, unsafe_allow_html=True)

                    col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 0.5, 0.5])
                    with col1:
                        text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Financial Statement</span></p>'
                        st.markdown(text, unsafe_allow_html=True)
                        financial_statement_options = ["", "Income Statement", "Cash Flow Statement", "Balance Sheet"]
                        user_whatif_financial_statement_field = st.empty()
                        user_whatif_financial_statement_field.selectbox(label="", label_visibility="collapsed", options=financial_statement_options,
                                 format_func=lambda x: "Select Statement Option" if x == "" else x, key="user_whatif_financial_statement", on_change=change_callback6)
                    with col2:
                        statement_hist_x_field_text = st.empty()
                        statement_hist_x_field = st.empty()
                        if st.session_state.user_whatif_financial_statement == "Income Statement":
                            st.session_state.df_statement_sim_out = st.session_state.df_income_statement_sim_out
                        if st.session_state.user_whatif_financial_statement == "Cash Flow Statement":
                            st.session_state.df_statement_sim_out = st.session_state.df_cash_flow_statement_sim_out
                        if st.session_state.user_whatif_financial_statement == "Balance Sheet":
                            st.session_state.df_statement_sim_out = st.session_state.df_balance_sheet_statement_sim_out
                        if st.session_state.user_whatif_financial_statement != "":
                            text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Financial Field</span></p>'
                            statement_hist_x_field_text.markdown(text, unsafe_allow_html=True)
                            financial_statement_hist_x = statement_hist_x_field.selectbox(label="", label_visibility="collapsed",
                                          options=[s for s in list(st.session_state.df_statement_sim_out[st.session_state.user_entity_name+" ("+currency+ " Millions)"])], key="hist1", on_change=change_callback6)

                            df_financial_statement_plot = st.session_state.df_statement_sim_out.loc[(st.session_state.df_statement_sim_out[st.session_state.user_entity_name+" ("+currency+ " Millions)"] == financial_statement_hist_x),
                                               st.session_state.df_statement_sim_out.columns[2]:(
                                               st.session_state.df_statement_sim_out.columns[
                                                   st.session_state.user_whatif_iterations + 1])].transpose()
                            df_financial_statement_plot = df_financial_statement_plot.replace(",", "", regex=True).astype("float64")
                            financial_statement_hist_value = st.session_state.df_statement_sim_out.loc[
                        (st.session_state.df_statement_sim_out[st.session_state.user_entity_name+" ("+currency+ " Millions)"] == financial_statement_hist_x),
                        st.session_state.df_statement_sim_out.columns[1]]
                            financial_statement_hist_value = financial_statement_hist_value.reset_index(drop=True)
                            financial_statement_hist_value_text = financial_statement_hist_value.loc[0]
                            financial_statement_hist_value = float(financial_statement_hist_value.loc[0].replace(",", ""))
                    with col6:
                        st.text("")
                        st.text("")
                        submit5_button = st.button("Next", key="whatif_sim_2CB")
                    with col7:
                        st.text("")
                        st.text("")
                        cancel_button4 = st.button("Cancel", key="whatif_reset_5", on_click=reset6)
                    if submit5_button:
                        if st.session_state.user_whatif_financial_statement == "":
                            col1, col2, col3 = st.columns([1, 4, 1])
                            with col2:
                                st.error("**Error**: please complete selection.")
                        else:
                            st.session_state.next4_confirm = True
                    if st.session_state.next4_confirm == True:
                        st.text("")
                        st.text("")
                        statement_x_field = st.empty()
                        statement_x_description_field = st.empty()
                        text = '<p style="margin-bottom: 2px;"><span style="font-family:sans-serif; color:#25476A; font-size: 24px;">{}</span></p>'.format(financial_statement_hist_x)
                        statement_x_field.markdown(text, unsafe_allow_html=True)
                        financial_variables =  ['Sales Revenue', 'Sales Revenue Growth %', 'COGS (Excluding D&A)', 'COGS (Excluding D&A) Margin %',
                        'D&A Expenses', 'COGS (Including D&A)', 'Gross Profit', 'Gross Profit Margin %', 'SG&A (Other) Expenses',
                        'R&D Expenses', 'SG&A (Including R&D) Expenses', 'EBIT', 'EBIT Margin %', 'Other Income (Expenses)',
                        'Interest Expenses', 'Interest Rate %', 'PBT', 'Income Tax Expense', 'Tax Rate %', 'Net Income',
                        'Net Income Margin %', 'Dividend or Distributions Paid', 'Dividend Payout Ratio %', 'D&A Expenses',
                        'D&A Expenses / Sales %', 'Increase (Decrease) in Other Items', 'Funds from Operations',
                        'Change in Working Capital', 'Net Cash from Operating Activities', 'Capital Expenditure',
                        'Capital Expenditure / Sales %', 'Other Investing Activities', 'Net Cash from Investing Activities',
                        'Dividend or Distributions Paid', 'Sale (Repurchase) of Equity', 'Issuance (Reduction) of Debt',
                        'Other Financing Activities', 'Net Cash from Financing Activities', 'Net Increase in Cash & Equivalents',
                        'Cash & Short Term Investments', 'Accounts Receivable', 'Accounts Receivable Days', 'Inventory',
                        'Inventory Days', 'Other Current Assets', 'Total Current Assets', 'Property, Plant & Equipment',
                        'Accumulated Depreciation', 'Net Fixed Assets', 'Intangible Assets', 'Total Other Assets', 'Total Assets',
                        'Accounts Payable', 'Accounts Payable Days', 'Short Term Notes Payable', 'Other Short Term Liabilities',
                        'Total Current Liabilities', 'Long Term Notes Payable', 'Other Long Term Liabilities', 'Total Non Current Liabilities',
                        'Total Liabilities', 'Stock Value', 'Retained Earnings', 'Capital Stock', 'Other Equity', 'Adjustments',
                        'Total Shareholders Equity', 'Balance Check']

                        financial_variable_descriptions = [
                            'Sales Revenue represents the total amount of revenue generated by the company from the sale of goods or services.',
                            'Sales Revenue Growth % represents the percentage change in sales revenue over a given period of time.',
                            'COGS (Excluding D&A) represents the cost of goods sold (COGS) that excludes depreciation and amortization expenses.',
                            'COGS (Excluding D&A) Margin % represents the percentage of revenue that is consumed by COGS, excluding depreciation and amortization expenses.',
                            'D&A Expenses represent the expenses associated with the depreciation and amortization of assets.',
                            'COGS (Including D&A) represents the total cost of goods sold, including depreciation and amortization expenses.',
                            'Gross Profit represents the total revenue generated by the company minus the cost of goods sold.',
                            'Gross Profit Margin % represents the percentage of revenue that remains after deducting the cost of goods sold.',
                            'SG&A (Other) Expenses represent the expenses incurred by the company for selling, general and administrative purposes, excluding research and development (R&D) expenses.',
                            'R&D Expenses represent the expenses incurred by the company for research and development of new products or services.',
                            'SG&A (Including R&D) Expenses represent the total expenses incurred by the company for selling, general and administrative purposes, including research and development expenses.',
                            'EBIT represents earnings before interest and taxes. It is a measure of a company\'s operating profitability and is calculated by subtracting operating expenses from revenues.',
                            'EBIT Margin % represents the percentage of revenue that remains after deducting operating expenses.',
                            'Other Income (Expenses) represent any income or expenses that are not related to the company\'s primary business operations, such as gains or losses from investments or currency fluctuations.',
                            'Interest Expenses represent the expenses incurred by the company for interest on its outstanding debts.',
                            'Interest Rate % represents the rate of interest that the company pays on its outstanding debts.',
                            'PBT represents profit before taxes. It is calculated by subtracting all expenses, including interest and taxes, from revenues.',
                            'Income Tax Expense represents the amount of income tax owed by the company.',
                            'Tax Rate % represents the percentage of income that the company pays in taxes.',
                            "Net Income represents the total profit or loss that the company has made after deducting all expenses, including taxes.",
                            "Net Income Margin % represents the percentage of revenue that remains after deducting all expenses, including taxes.",
                            "Dividend or Distributions Paid represents the amount of money paid by the company to its shareholders as dividends or distributions.",
                            "Dividend Payout Ratio % represents the percentage of net income that is paid out to shareholders as dividends or distributions.",
                            "D&A Expenses represents the expenses associated with the depreciation and amortization of assets.",
                            "D&A Expenses / Sales % represents the percentage of revenue that is consumed by depreciation and amortization expenses.",
                            "Increase (Decrease) in Other Items represents the net change in other items that are not included in the other categories.",
                            "Funds from Operations represents the cash generated from the company's core operations, excluding investments and financing.",
                            "Change in Working Capital represents the change in the company's working capital over a given period of time.",
                            "Net Cash from Operating Activities represents the net amount of cash generated or used by the company's operating activities.",
                            "Capital Expenditure represents the amount of money spent by the company on long-term assets, such as property, plant and equipment.",
                            "Capital Expenditure / Sales % represents the percentage of revenue that is spent on capital expenditures.",
                            "Other Investing Activities represents the cash flows from investing activities that are not related to capital expenditures or acquisitions.",
                            "Net Cash from Investing Activities represents the net amount of cash generated or used by the company's investing activities.",
                            "Dividend or Distributions Paid represents the amount of money paid by the company to its shareholders as dividends or distributions.",
                            "Sale (Repurchase) of Equity represents the proceeds from the sale or repurchase of the company's equity.",
                            "Issuance (Reduction) of Debt represents the proceeds from the issuance or reduction of the company's debt.",
                            'Other Financing Activities represents the cash inflows or outflows from financing activities that are not related to debt or equity issuance, such as lease payments or dividend payments.',
                            'Net Cash from Financing Activities represents the net change in cash flow resulting from financing activities, which includes the issuance or repurchase of debt or equity and any other financing activities.',
                            'Net Increase in Cash & Equivalents represents the net change in cash and cash equivalents over a given period of time.',
                            'Cash & Short Term Investments represents the total amount of cash and short-term investments held by the company.',
                            'Accounts Receivable represents the amount of money owed to the company by its customers for goods or services sold on credit.',
                            'Accounts Receivable Days represents the average number of days it takes for the company to collect payments from its customers for goods or services sold on credit.',
                            'Inventory represents the value of goods or materials that a company has on hand and available for sale or production.',
                            'Inventory Days represents the average number of days it takes for the company to sell or use its inventory.',
                            'Other Current Assets represents the value of other current assets not included in the company\'s cash, short-term investments, accounts receivable, or inventory.',
                            'Total Current Assets represents the total value of all current assets owned by the company, including cash, short-term investments, accounts receivable, inventory and other current assets.',
                            'Property, Plant & Equipment represents the value of the company\'s tangible assets, such as land, buildings and equipment, used in its operations.',
                            'Accumulated Depreciation represents the cumulative amount of depreciation recorded on the company\'s fixed assets over time.',
                            'Net Fixed Assets represents the value of the company\'s fixed assets, such as property, plant and equipment, after subtracting accumulated depreciation.',
                            'Intangible Assets represents the value of assets that do not have physical substance, such as patents, trademarks and goodwill.',
                            'Total Other Assets represents the value of all other assets not included in the company\'s current or fixed assets.',
                            'Total Assets represents the total value of all assets owned by the company, including current assets, fixed assets and other assets.',
                            'Accounts Payable represents the amount of money owed by the company to its suppliers for goods or services received on credit.',
                            'Accounts Payable Days represents the average number of days it takes for the company to pay its suppliers for goods or services received on credit.',
                            'Short Term Notes Payable represents the amount of short-term debt owed by the company, such as loans or lines of credit, that are due within one year.',
                            'Other Short Term Liabilities represents the value of other short-term liabilities not included in the company\'s accounts payable or short-term notes payable.',
                            'Total Current Liabilities represents the total value of all current liabilities owed by the company, including accounts payable, short-term notes payable and other short-term liabilities.',
                            'Long Term Notes Payable represents the amount of long-term debt owed by the company, such as bonds or mortgages, that are due after one year.',
                            'Other Long Term Liabilities represents the value of other long-term liabilities not included in the company\'s long-term notes payable.',
                            'Total Non Current Liabilities represents the total value of all non-current liabilities owed by the company, including long-term notes payable and other long-term liabilities.',
                            'Total Liabilities represents the total value of all liabilities owed by the company, including current and non-current liabilities.',
                            'Stock Value represents the total value of the company\'s outstanding shares of stock.',
                            'Retained Earnings represents the cumulative total of the company\'s earnings that have been retained rather than paid out as dividends.',
                            'Capital stock represents the amount of capital that a company has raised by issuing stock to its shareholders.',
                            'Other equity represents the cumulative value of all equity transactions that are not related to the issuance of stock.',
                            'Adjustments represent accounting entries made to correct errors, omissions or other discrepancies in financial statements to ensure accuracy and completeness.',
                            'Total shareholders equity represents the total value of the shareholders\' ownership in the company.',
                            'Balance check represents the process of verifying the accuracy of recorded balances of assets, liabilities and equity in a balance sheet statement to ensure they are equal and there are no discrepancies.']

                        if financial_statement_hist_x in financial_variables:
                            idx = financial_variables.index(financial_statement_hist_x)
                            result = financial_variable_descriptions[idx]
                            text = '<p style="margin-top: 0px; margin-bottom: 20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">{}</span></p>'.format(
                                result)
                            statement_x_description_field.markdown(text, unsafe_allow_html=True)

                        st.session_state.df_summary = df_financial_statement_plot.describe(include="all")
                        st.session_state.df_summary = pd.DataFrame.transpose(st.session_state.df_summary)
                        st.session_state.df_summary.insert(loc=1, column=st.session_state.user_reporting_period, value=financial_statement_hist_value)
                        st.session_state.df_summary.insert(loc=2, column="mode", value=df_financial_statement_plot.mode())
                        for col in st.session_state.df_summary.columns:
                            if col in ["count"]:
                                st.session_state.df_summary[col] = st.session_state.df_summary[col].apply('{:,.0f}'.format)
                            else:
                                st.session_state.df_summary[col] = st.session_state.df_summary[col].apply('{:,.2f}'.format)
                        st.session_state.df_summary = st.session_state.df_summary[[st.session_state.user_reporting_period, "count", "mean", "50%", "mode", "std", "min", "25%", "75%", "max"]]
                        st.session_state.df_summary.columns =  pd.MultiIndex.from_arrays([['Simulation Statistics', 'Simulation Statistics', 'Simulation Statistics', 'Simulation Statistics', 'Simulation Statistics', 'Simulation Statistics', 'Simulation Statistics', 'Simulation Statistics', 'Simulation Statistics', 'Simulation Statistics'], [st.session_state.user_reporting_period, "Iterations", "Mean", "Median", "Mode", "Standard Deviation", "Minimum", "25% Quantile", "75% Quantile", "Maximum"]])
                        stats_table = st.session_state.df_summary.style.set_table_styles([{'selector': 'td', 'props': [('color', '#25476A')]}, {'selector': 'th',
                                                                                                  'props': [
                                                                                                      ('text-align', 'center'),
                                                                                                      ('font-weight', 'bold'), (
                                                                                                      'background-color',
                                                                                                      '#25476A'),
                                                                                                      ('color', '#FAFAFA')]}, {'selector': 'td:hover',
                                                                                                  'props': [('background-color',
                                                                                                             'rgba(111, 114, 222, 0.4)')]},
                                                                                                 {'selector': 'td',
                                                                                                  'props': [('border',
                                                                                                             '0.5px solid #25476A')]},
                                                                                                 {'selector': '', 'props': [(
                                                                                                                            'border',
                                                                                                                            '3px solid #25476A')]}]).set_properties(**{'text-align': 'center'}, **{'width': '160px'}).hide_index()
                        st.text("")
                        st.markdown(f"""<div style="display: flex; justify-content: center;">{stats_table.to_html()}</div>""", unsafe_allow_html=True)
                        st.text("")
                        median_variable = np.median(df_financial_statement_plot)
                        mean_variable = np.mean(df_financial_statement_plot).values[0]
                        stdev_variable = np.std(df_financial_statement_plot).values[0]
#                        median_variable_text = pd.Series(median_variable).apply(lambda x: '{:,.2f}'.format(x))
#                        mean_variable_text = pd.Series(mean_variable).apply(lambda x: '{:,.2f}'.format(x))
                        if stdev_variable != 0:
                            column_names = df_financial_statement_plot.columns.tolist()
                            target_column = column_names[0]
                            financial_statement_hist_fig = px.histogram(df_financial_statement_plot, nbins=20, cumulative=False,
                                                                        marginal="box",
                                                                        histnorm="percent",
                                                                        color_discrete_sequence=["#25476A"])
                            start_value = financial_statement_hist_fig.full_figure_for_development(warn=False).data[0].xbins['start']
                            end_value = financial_statement_hist_fig.full_figure_for_development(warn=False).data[0].xbins['end']
                            size_value = financial_statement_hist_fig.full_figure_for_development(warn=False).data[0].xbins['size']
                            count_value = int((end_value - start_value) / size_value)
                            bin_edges = np.linspace(start=start_value, stop=end_value, num=count_value)
                            binned_data = pd.cut(df_financial_statement_plot[target_column], bins=bin_edges, include_lowest=True)
                            bin_counts = binned_data.value_counts(sort=False, normalize=True)
                            df_variable_density = pd.DataFrame({"Interval": bin_counts.index, "Density": bin_counts.values})
                            df_variable_density.sort_values("Interval", inplace=True)
                            max_y = df_variable_density["Density"].max()*100
                            kde_fig = ff.create_distplot([df_financial_statement_plot[target_column].reset_index(drop=True)], group_labels=["distplot"],
                                                         histnorm="probability density",
                                                         bin_size=size_value,
                                                         curve_type="kde")
                            kde_fig_x = kde_fig.data[1]["x"]
                            kde_fig_y = kde_fig.data[1]["y"] * size_value * 100
                            financial_statement_hist_fig.add_traces(go.Scatter(x=kde_fig_x, y=kde_fig_y, mode="lines", line=dict(color="#03A9F4", width=3),
                                           showlegend=False))

                            financial_statement_hist_fig.update_layout(
                                {"plot_bgcolor": "rgba(0, 0, 0, 0)", "paper_bgcolor": "rgba(0, 0, 0, 0)"})
                            financial_statement_hist_fig.add_annotation(
                                dict(font=dict(color="#25476A", size=24, family="sans-serif"), x=-0.15, y=1.14,
                                     xref="paper",
                                     yref="paper", showarrow=False,
                                     text="Histogram ({} Iterations)".format('{:,.0f}'.format(st.session_state.user_whatif_iterations))))
                            financial_statement_hist_fig.add_annotation(
                                dict(font=dict(color="#25476A", size=14, family="sans-serif"), x=-0.12, y=-0.22,
                                     xref="paper",
                                     yref="paper", showarrow=False,
                                     text="Seed {}".format(st.session_state.seed_value)))
                            financial_statement_hist_fig.update_xaxes(showline=False, showgrid=False, zeroline=False)
                            financial_statement_hist_fig.update_yaxes(showline=False, showgrid=False, zeroline=False)
                            financial_statement_hist_fig.update_traces(marker_line_width=2, marker_line_color="#FAFAFA")
                            financial_statement_hist_fig.update_layout(plot_bgcolor="#C5C6C7", bargap=0, width=800 * 0.9,
                                                                       height=600 * 0.9,
                                                                       yaxis_title=dict(text="Frequency (%)",
                                                                                        font=dict(size=20,
                                                                                                  color="#25476A")),
                                                                       xaxis_title=dict(text=financial_statement_hist_x,
                                                                                        font=dict(size=20,
                                                                                                  color="#25476A")),
                                                                       yaxis=dict(tickfont=dict(size=18, color="#25476A")),
                                                                       xaxis=dict(tickangle=90,
                                                                                  tickfont=dict(size=18, color="#25476A")),
                                                                       showlegend=False, margin=dict(
                                    l=100,
                                    r=40,
                                    b=100,
                                    t=70
                                ), shapes=[go.layout.Shape(
                                    type="rect",
                                    xref="paper", yref="paper",
                                    x0=-0.15, y0=-0.26, x1=1.03, y1=1.04,
                                    line={'width': 2.5, 'color': '#25476A', 'dash': 'solid'})])
                            financial_statement_hist_fig.add_vline(x=financial_statement_hist_value, line_width=3,
                                                                   line_dash="dash", line_color='#FA9F1B')
                            financial_statement_hist_fig.add_annotation(
                                dict(font=dict(color='#FA9F1B', family="sans-serif", size=18),
                                     x=financial_statement_hist_value,
                                     y=max_y, align="right", xanchor="left", yanchor="top", textangle=90,
                                     showarrow=False,
                                     text=st.session_state.user_reporting_period + ": " + financial_statement_hist_value_text))

                            financial_statement_hist_fig.add_vline(x=median_variable, line_width=3,
                                                                   line_dash="dash", line_color='#0FCC2E')
                            financial_statement_hist_fig.add_annotation(
                                dict(font=dict(color='#0FCC2E', family="sans-serif", size=18), x=median_variable,
                                     y=max_y, align="right", xanchor="left", yanchor="top", textangle=90,
                                     showarrow=False,
                                     text="Median: " + str(round(median_variable, 2))))
                            financial_statement_hist_fig.add_vline(x=mean_variable, line_width=3,
                                                                   line_dash="dash", line_color='#AB47BC')
                            financial_statement_hist_fig.add_annotation(
                                dict(font=dict(color='#AB47BC', family="sans-serif", size=18), x=mean_variable,
                                     y=max_y, align="right", xanchor="left", yanchor="top", textangle=90,
                                     showarrow=False,
                                     text="Mean: " + str(round(mean_variable, 2))))
                            financial_statement_line_fig = px.line(df_financial_statement_plot, markers=True,
                                                                   template="plotly",
                                                                   color_discrete_sequence=["#25476A"])
                            financial_statement_line_fig.update_layout(
                                {"plot_bgcolor": "rgba(0, 0, 0, 0)", "paper_bgcolor": "rgba(0, 0, 0, 0)"})
                            financial_statement_line_fig.update_traces(line=dict(width=3))
                            financial_statement_line_fig.add_annotation(
                                dict(font=dict(color="#25476A", size=24, family="sans-serif"), x=-0.2, y=1.14, xref="paper",
                                     yref="paper", showarrow=False,
                                     text="Simulated Values ({} Iterations)".format('{:,.0f}'.format(st.session_state.user_whatif_iterations))))
                            financial_statement_line_fig.add_annotation(
                                dict(font=dict(color="#25476A", size=14, family="sans-serif"), x=-0.18, y=-0.31,
                                     xref="paper",
                                     yref="paper", showarrow=False,
                                     text="Seed {}".format(st.session_state.seed_value)))
                            financial_statement_line_fig.update_xaxes(showline=False, showgrid=False, zeroline=False,
                                                                      tickangle=-90)
                            financial_statement_line_fig.update_yaxes(showline=False, showgrid=False, zeroline=False)
                            financial_statement_line_fig.update_layout(plot_bgcolor="#C5C6C7", width=800 * 0.9,
                                                                       height=600 * 0.9,
                                                                       yaxis_title=dict(text=financial_statement_hist_x,
                                                                                        font=dict(size=20,
                                                                                                  color="#25476A")),
                                                                       xaxis_title=dict(
                                                                           text="Iteration",
                                                                           font=dict(size=20, color="#25476A")), yaxis=dict(
                                    tickfont=dict(size=18, color="#25476A")), xaxis=dict(
                                    tickfont=dict(size=18, color="#25476A")), showlegend=False, margin=dict(
                                    l=120,
                                    r=40,
                                    b=130,
                                    t=70
                                ), shapes=[go.layout.Shape(
                                    type="rect",
                                    xref="paper", yref="paper",
                                    x0=-0.2, y0=-0.36, x1=1.03, y1=1.04,
                                    line={'width': 2.5, 'color': '#25476A', 'dash': 'solid'})])
                            financial_statement_line_fig.add_hline(y=financial_statement_hist_value, line_width=3,
                                                                   line_dash="dash", line_color='#FA9F1B')
                            financial_statement_line_fig.add_annotation(
                                dict(font=dict(color='#FA9F1B', family="sans-serif", size=18),
                                     y=financial_statement_hist_value,
                                     align="right",  xanchor="left", yanchor="bottom",
                                     showarrow=False,
                                     text=st.session_state.user_reporting_period + ": " + financial_statement_hist_value_text))
                            financial_statement_line_fig.add_hline(y=median_variable, line_width=3,
                                                                   line_dash="dash", line_color='#0FCC2E')
                            financial_statement_line_fig.add_annotation(
                                dict(font=dict(color='#0FCC2E', family="sans-serif", size=18), y=median_variable,
                                     align="right",  xanchor="left", yanchor="bottom", showarrow=False,
                                     text="Median: " + str(round(median_variable, 2))))
                            financial_statement_line_fig.add_hline(y=mean_variable, line_width=3,
                                                                   line_dash="dash", line_color='#AB47BC')
                            financial_statement_line_fig.add_annotation(
                                dict(font=dict(color='#AB47BC', family="sans-serif", size=18), y=mean_variable,
                                     align="right",  xanchor="left", yanchor="bottom", showarrow=False,
                                     text="Mean: " + str(round(mean_variable, 2))))

                            col1, col2, col3, col4, col5  = st.columns([0.1, 1, 0.2, 1, 0.1])
                            with col2:
                                st.plotly_chart(financial_statement_line_fig, config={'displayModeBar': False})
                            with col4:
                                st.plotly_chart(financial_statement_hist_fig, config={'displayModeBar': False})
                            col1, col2 = st.columns([1, 5])
                            with col1:
                                text = '<p style="margin-bottom: -5px; margin-top: 10px;"><span style="font-family:sans-serif; color:#25476A; font-size: 15px; font-weight: bold;">Download Visualizations</span></p>'
                                st.markdown(text, unsafe_allow_html=True)
                                statement_out_download_field = st.empty()
                                statement_out_download = statement_out_download_field.selectbox(label="",
                                                                                                label_visibility="collapsed",
                                                                                                options=[
                                                                                                    "Select To Download",
                                                                                                    "Yes"],
                                                                                                key="sim_download3")
                            with col2:
                                if statement_out_download == "Yes":
                                    spinner = st.markdown(marker_spinner_css, unsafe_allow_html=True)
                                    spinner_image = st.markdown(spinner_image_css.format(img_to_bytes("images/spinner_center.png")), unsafe_allow_html=True)
                                    st.text("")
                                    st.text("")
                                    variable_plots_out = [(stats_table.set_properties(**{'width': '120px'}),
                                                  "simulation_analysis_{}_statistics".format(financial_statement_hist_x), "png", 90, "table", financial_statement_hist_x, st.session_state.user_entity_name), (
                                                 financial_statement_line_fig.update_layout(
                                                     {"paper_bgcolor": "rgba(255,255, 255, 1)"}).to_image(format="png"),
                                                 "simulation_analysis_{}_values".format(financial_statement_hist_x), "png", 150, "figure", "", st.session_state.user_entity_name), (
                                                 financial_statement_hist_fig.update_layout(
                                                     {"paper_bgcolor": "rgba(255,255, 255, 1)"}).to_image(format="png"),
                                                 "simulation_analysis_{}_histogram".format(financial_statement_hist_x), "png", 150, "figure", "", st.session_state.user_entity_name)]
                                    downloader = MultiFileDownloader()
                                    downloader.export_tables_figures(variable_plots_out, st.session_state.user_entity_name)
                                    spinner.empty()
                                    spinner_image.empty()
                        else:
                            text = '<p style="margin-top: 0px; margin-bottom: 20px; text-align: justify;"><span style="font-family:sans-serif; color:#25476A; font-size: 18px;">Data visualizations are not shown because the selected variable exhibits zero variation during the simulation analysis.</span></p>'.format(
                                result)
                            statement_x_description_field.markdown(text, unsafe_allow_html=True)
