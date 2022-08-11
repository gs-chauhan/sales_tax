def s_tax(inp):
    from math import ceil
    def shopBasket(itemList):

        finalPrice =[]
        newSum = 0
        totalTax = 0
        rnd = 20
        
        for items in itemList:
            tempListItem = items.split()
            tempListItem = [x.replace(' ','') for x in tempListItem]
            exemptFlag = False
            
            for item in tempListItem:
                if item in ['book', 'books', 'chocolate', 'chocolates', 'pill', 'pills']:
                    exemptFlag = True
                    
            
            if exemptFlag == True and 'imported' in tempListItem:
                priceOfOne = float(tempListItem[-1])/float(tempListItem[0])
                tax = ceil(round((float(priceOfOne) * 0.05), 2) * rnd) / rnd
                totalTax += tax
                newPrice = tax + float(priceOfOne) 
                newPrice = newPrice * float(tempListItem[0])
                newSum += newPrice
                newPrice = round((newPrice*100))/100
                tempstr = ' '.join(tempListItem[:-1])
                tempstr = tempstr.replace(" at",":")
                print( tempstr+' ' + str(newPrice))
                finalPrice.append(newPrice)
                
            elif exemptFlag == True:
                priceOfOne = float(tempListItem[-1])/float(tempListItem[0])
                newPrice = float(tempListItem[-1])
                newPrice = newPrice * float(tempListItem[0])
                newSum += newPrice
                newPrice = round((newPrice*100))/100
                tempstr = ' '.join(tempListItem[:-1])
                tempstr = tempstr.replace(" at",":")
                print( tempstr+' ' + str(newPrice))
                finalPrice.append(newPrice)
                
            elif 'imported' in tempListItem:
                priceOfOne = float(tempListItem[-1])/float(tempListItem[0])
                tax = ceil(round((float(priceOfOne) * 0.15), 2) * rnd) / rnd
                totalTax += tax
                newPrice = tax + float(priceOfOne)
                newPrice = newPrice * float(tempListItem[0])
                newSum += newPrice
                newPrice = round((newPrice*100))/100
                tempstr = ' '.join(tempListItem[:-1])
                tempstr = tempstr.replace(" at",":")
                print( tempstr+' ' + str(newPrice))
                finalPrice.append(newPrice)
                
            else:
                priceOfOne = float(tempListItem[-1])/float(tempListItem[0])
                tax = ceil(round((float(priceOfOne) * 0.10), 2) * rnd) / rnd
                totalTax += tax
                newPrice = tax + float(tempListItem[-1])
                newPrice = newPrice * float(tempListItem[0])
                newSum += newPrice
                newPrice = round((newPrice*100))/100
                tempstr = ' '.join(tempListItem[:-1])
                tempstr = tempstr.replace(" at",":")
                print( tempstr+' ' + str(newPrice))
                finalPrice.append(newPrice)
                
        print('Sales Taxes:',round((totalTax*100))/100)
        print('Total:',round((newSum*100))/100)
                
    itemList = []

    import re
    inpString = ""
    inpString += inp
    list = re.findall("\d+ \D+ at \d+.\d+", inpString)
    itemList.extend(list)

    shopBasket(itemList)