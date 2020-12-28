import pandas as pd
import scans

#will take finalData as an argument
def fillIn(finalData, fileName):

    #elements 9, 10, 13 
    #create it so that file name can be changed

    df = pd.DataFrame(finalData, columns = ['Serial Number', 'Product ID','Problem Description'])

   

    #df['Serial Number'] = data1[0::2]
    #df['Product ID'] =  data2[1::2]

    df.to_csv(fileName + '.csv', index = False)

#fillIn()

    