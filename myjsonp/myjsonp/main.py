#!/usr/bin/ python

"""
Filename: main.py
Author: Mario Llesta
Creation date: 03/12/2023

Outline:
This module contains the main code of the myjsonp tool.
"""


# Imports

import sys
import typer
import json

from rich import print


app = typer.Typer(rich_markup_mode="rich")


# Functions

def read_file(file:str):
    content = None
    
    try:
        if file:
            with open(file, 'r') as f:
                content = f.read()
        else:
            content = sys.stdin.buffer.read()
        
        return content
    
    except FileNotFoundError:
        print(f"Error: File not found.")
           
    except Exception as e:
        print(f"Error: {e}")
        

def json_parser(file:str):
    
    content = read_file(file)
    
    try:
        json_data = json.loads(content)
        
        if isinstance(json_data, dict):
            return 0
        
    
    except json.JSONDecodeError as e:
        return 1 


@app.command(epilog="Made by [green]mariollesta[/green]") 
def myjsonp(
    file:str = typer.Argument("", help="File PATH"), 
):
    
    # 0 -> valid JSON
    # 1 -> invalid JSON 
    result = "0. Valid JSON" if json_parser(file) == 0 else "1. Invalid JSON"
    print(result)   
    

     
if __name__ == "__main__":
    app()  