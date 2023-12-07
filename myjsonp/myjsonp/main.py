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
):
    
    try:
        
        # 0 -> valid JSON, 1 -> invalid JSON
        valid = 0
        invalid = 1    
        
        content = None
        
        if file:
            with open(file, 'r') as f:
                content = f.read()
        
        else:
            content = sys.stdin.buffer.read()
    
        json_data = json.loads(content)
        print(json_data)
        
        if isinstance(json_data, dict):
            print(valid)
        else:
            print(invalid)
         
              
    except json.JSONDecodeError as e:
                  print(f"Error decoding JSON.")          

    except FileNotFoundError:
        print(f"Error: File not found.")
           
    except Exception as e:
        print(f"Error: {e}")     
    


if __name__ == "__main__":
    app()  