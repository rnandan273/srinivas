# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 17:14:44 2014

@author: raghu
"""

import csv
import xlrd
from pymongo import MongoClient
"""
Process Menuss and recipes
"""


def processMenus():
    workbook = xlrd.open_workbook('/Users/raghu/work/projects/srinivas/Foods.xlsx')
    worksheets = workbook.sheet_names()
    
    for worksheet_name in worksheets:
        #print "worksheet_name %s"%worksheet_name
        if(worksheet_name=="Menu"):
            sheets.append(worksheet_name)
            worksheet = workbook.sheet_by_name(worksheet_name)
            num_rows = worksheet.nrows - 1
            num_cells = worksheet.ncols - 1
            curr_row = -1
            curr_cell = -1
            sheet_details=[[]]

            MenuItem=[]

            while curr_row < num_rows:            
                curr_row += 1
                print  worksheet.cell_value(curr_row, 0)
                
def processMenuDetails():
    workbook = xlrd.open_workbook('/Users/raghu/work/projects/srinivas/Foods.xlsx')
    worksheets = workbook.sheet_names()
    for worksheet_name in worksheets:
        worksheet = workbook.sheet_by_name(worksheet_name)
        num_rows = worksheet.nrows
        num_cells = worksheet.ncols
        jsObj={}
        #print "worksheet_name %s"%worksheet_name
        if(worksheet_name!="Menu" and worksheet_name!="Working sheet"):
            #print "worksheet_name %s"%worksheet_name"
            jsObj['MenuItem']=worksheet_name

            itemType = worksheet.cell_value(0, 0)
            itemValue = worksheet.cell_value(1, 0)
            cusType = worksheet.cell_value(0, 1)
            cusValue = worksheet.cell_value(1, 1)

            itemsArr={}
            for row in range(0,num_rows):                
                if(row==0):
                    continue
                
                ingrType = worksheet.cell_value(0, 2)
                ingrValue = worksheet.cell_value(row, 2)
                qtyType = worksheet.cell_value(0, 3)
                qtyValue = worksheet.cell_value(row, 3)
                timeType = worksheet.cell_value(0, 4)
                timeValue = worksheet.cell_value(row, 4)
                
                itemArr={}
                itemArr[ingrType]=str(ingrValue)
                itemArr[qtyType]=str(qtyValue)
                itemArr[timeType]=str(timeValue)
                itemsArr[str(row)]=itemArr
                
            jsObj['items']=itemsArr                
            recipeArr={}
            recipesStr=""
            for cell in range(6,num_cells-3):
                cellType = worksheet.cell_value(0, cell)

                for row in range(0,num_rows):

                    if(row==0):
                        continue
                    cellValue = worksheet.cell_value(row, cell)
                    if(cellValue !=""):
                        recipesStr=recipesStr+str(cellValue)
                recipeArr[str(row)]=recipesStr       
            
            jsObj['recipe']=recipeArr
            print jsObj

            print client.database_names()
            food = db.food
            food_id = food.insert(jsObj)
            
            print db.collection_names()
                    
def viewAllRecipes():
    for cont in db.food.find():
        print cont
        
processMenus()

processMenuDetails()

client = MongoClient('localhost:27017')
db=client.food
viewAllRecipes()
    
