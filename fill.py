import pandas as pd
import scans

#will take finalData as an argument
def fillIn(finalData, fileName):

    #elements 9, 10, 13 
    #create it so that file name can be changed
    dataCols = ['Serial Number', 'Product ID','Problem Description']
    df = pd.DataFrame(finalData, columns = dataCols)

    #add the columns here
    newVals = ['Jason Waddle', '502-568-7838', 'jwaddle@shccs.com', 'Jason Waddle', '502-568-7839', 'Signature HealthCARE LLC.', 'Louisville', 'KY', '40299']
    newCols = ['Submitters', "Submitter's Phone", "Submitters Email", 'Equipment Contact Name', 'Equipment Contact Phone', 'Equipment Contact Company', 'Equipment Contact City', 'Equipment Contact State', 'Equipment Contact Zip/Postal Code']
    for i in range (0, len(newCols)):
        df[newCols[i]] = newVals[i] 
    
    #rearrange columns
    cols = list(df.columns)
    df = df[cols[3:6] + cols[0:3] + cols[4:-1]]



    #df['Serial Number'] = data1[0::2]
    #df['Product ID'] =  data2[1::2]

    df.to_csv(fileName + '.csv', index = False)

#fillIn()

    