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

@app.command(epilog="Made by [green]mariollesta[/green]") 
def myjsonp(
    file:str = typer.Argument("", help="File PATH"), 
    s: bool = typer.Option(help="Simple JSON parser", rich_help_panel="Main Options")  
):
    
    try:
        
        if file:
            with open(file, 'r') as f:
                content = f.read()
        
        else:
            content = sys.stdin.buffer.read()
    
        
        # 0 -> valid JSON, 1 -> invalid JSON
        valid = 0
        invalid = 1
        
        if s:
              try:
                  json.loads(content)
                  print(valid)
              
              except ValueError:
                  print(invalid)

      
    except FileNotFoundError:
        print(f"Error: File not found.")
           
    except Exception as e:
        print(f"Error: {e}")     
    


if __name__ == "__main__":
    app()  