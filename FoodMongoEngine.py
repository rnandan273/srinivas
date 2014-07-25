# -*- coding: utf-8 -*-
"""
Created on Sat May 31 23:58:43 2014

@author: raghu
"""
import csv
import xlrd
from mongoengine import *
connect('food_test')

class Recipe(Document):
    MenuItem = StringField(required=True)
    Cusiene = StringField(max_length=50)
    Items = ListField(ListField(StringField(max_length=1028)))
    Procedure=ListField(StringField(max_length=1028))
    Cooktime = StringField(max_length=50)
    Totaltime = StringField(max_length=50)
    
def processMenuDetails():
    workbook = xlrd.open_workbook('/Users/raghu/work/projects/srinivas/Foods.xlsx')
    worksheets = workbook.sheet_names()
    for worksheet_name in worksheets:
        worksheet = workbook.sheet_by_name(worksheet_name)
        num_rows = worksheet.nrows
        num_cells = worksheet.ncols
        rcp = Recipe();
        if(worksheet_name!="Menu" and worksheet_name!="Working sheet"):
            #print "worksheet_name %s"%worksheet_name"
            rcp.MenuItem=worksheet_name
            
            itemsArr=[]
            for row in range(0,num_rows):                
                if(row==0):
                    continue
                
                ingrType = worksheet.cell_value(0, 2)
                ingrValue = worksheet.cell_value(row, 2)
                qtyType = worksheet.cell_value(0, 3)
                qtyValue = worksheet.cell_value(row, 3)
                timeType = worksheet.cell_value(0, 4)
                timeValue = worksheet.cell_value(row, 4)
                
                itemArr=[]
                """
                itemArr[ingrType]=str(ingrValue)
                itemArr[qtyType]=str(qtyValue)
                itemArr[timeType]=str(timeValue)
                """
                itemArr.append(str(ingrValue))
                itemArr.append(str(qtyValue))
                itemArr.append(str(timeValue))
                itemsArr.append(itemArr)
                
            rcp.Items=itemsArr
            
            recipeArr=[]
            recipesStr=""
            for cell in range(6,num_cells-3):
                cellType = worksheet.cell_value(0, cell)

                for row in range(0,num_rows):               
                    if(row==0):
                        continue
                    cellValue = worksheet.cell_value(row, cell)
                    if(cellValue !=""):
                        recipesStr=recipesStr+str(cellValue)
                        
                recipeArr.append(recipesStr)
                
            rcp.Procedure=recipeArr
                
            rcp.save()

def lookupDB(item):
    """
    db=client.test_food
    print db.collection_names()
    for cont in db.recipe.find():
        print cont
       """
    qry = item
    for rcp in Recipe.objects(MenuItem=qry):
        print rcp.Procedure
        break
        
processMenuDetails()
lookupDB('Coconut Chutney')
lookupDB('Rice Idli')

"""
recipe1 = Recipe(MenuItem='Coconut Chutney')
recipe1.Cusiene='South Indian'
recipe1.Cooktime='10'
recipe1.Totaltime='25'

recipe1.update


db=client.test_food
print db.collection_names()
for cont in db.recipe.find():
   print cont
   """