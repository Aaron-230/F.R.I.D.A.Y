from google import genai as Gemini
from google.genai import types
import sys
import googlefinance as Finance

with open("System.txt", "r") as file:
    SystemInstructions = file.read()

def Shutdown():
    print("Shutting down...")
    sys.exit()

def getMarketData(stock):
    data = Finance.get_stock_data(stock)
    return data

AI = Gemini.Client(api_key="AIzaSyBOGaQ_kSv4e67-Ylc2gmCsyamVr8NutHY")
Search = types.Tool(google_search=types.GoogleSearch())
Config = types.GenerateContentConfig(tools=[Search], system_instruction=SystemInstructions)

def Response(content):
    response = AI.models.generate_content(model="gemini-2.5-flash", contents=content, config=Config)
    return response.text

while True:
    Input = input("User: ")
    print("F.R.I.D.A.Y.: " + Response(Input))