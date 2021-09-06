#!/usr/bin/env python
# coding: utf-8

# ### front page

# In[ ]:
import json

while 1>0:
    print("\n\n           IMS                 ")
    print("PRESS 1 to update inventory items ")
    print("PRESS 2 to display inventory items ")
    print("PRESS 3 for billing ")
    print("PRESS 4 to add new items to inventory ")
    print("PRESS 5 to display sales ")
    print("PRESS n/N to logout")
    print("********************************************")
    gg=input()
    if gg=='n' or gg=='N':
        break
    '''else:
        print("WRONG INPUT")'''

# ### loading json file sample

# In[ ]:


# import json
# gg=1
# if gg==1:
#     item_id=input("Enter item ID : ")
#     #new_quantity=input("Enter quantity/update quantity : ")
#     fd = json.load(open('inv.json'))
#     #print(fd)
#     for i in fd:
#         if i==item_id:
#             print("Item found")
#             #new_quantity=int(input("Enter quantity/update quantity : "))
#             print(fd["1001"])
#             #fd[str(item_id)]['quantity']+=new_quantity
#             #itemid=str(item_id)
#             print(fd[itemid]['quantity'])


# In[ ]:


# item={1001:{'name':'coco','price':10,'quantity':10,'self':1}}
# print(item)
# gg=json.dumps(item)
# print(type(gg))
# gh=json.loads(gg)
# print(gg)

      


# ### view inventory

# In[ ]:




    if gg=='2':
        fd=json.load(open('new_json.json'))
        #print(fd)
        print("**************************************************************************************************")
        print("                  INVENTORY                                                                       ")
        print("**************************************************************************************************")
        for i in fd:
    
            print("Item id : ",i,"| Name : ",fd[i]['name'],"|price : ",fd[i]['price'],"|Quantity : ",
                  fd[i]['quantity'],"|Self : ",fd[i]['self'],"|Type : ",fd[i]['type'])
            print("----------------------------------------------------------------------------------------------------")
            #print(j +"\n")


# ### updating json file

# In[ ]:



    if gg=='1':
        update_id=input("Enter item id :")
        up = json.load(open('new_json.json'))
        #print(fd)
    
        flag=0
        for i in up:
            if i==str(update_id):
                print("quantity or price")
                up_col=input("what you want to update :")
                up_data=input("enter value :")
                up[update_id][up_col]=up_data
                up_json=open("new_json.json",'w')
                up_file=json.dumps(up)
                up_json.write(up_file)
                up_json.close()
                flag=1
                break
        if flag==0:
            print("Item not found try again!")
        


# ### billing

# In[ ]:



    if gg=='3':
        bil_item=input("Enter id :")
        bil_quan=int(input("Enter quantity :"))
        fd = json.load(open('new_json.json'))
        yy=int(fd[bil_item]['quantity'])
        if bil_quan>yy:
            print("**OUT OF STOCK**")
        else:
            print("-------------------------------------------")
            print("            BILL                           ")
            print("-------------------------------------------")
            print("ITEM : ",fd[bil_item]['name'])
            print("QUANTITY : ",bil_quan)
            print("PRICE : Rs",bil_quan*int(fd[bil_item]['price']))
            print("-------------------------------------------")
            print("-------------------------------------------")
        fd[bil_item]['quantity']=yy-bil_quan
        up_json=open("new_json.json",'w')
        up_file=json.dumps(fd)
        up_json.write(up_file)
        up_json.close()
        #------------------------------------------------------------------------------------
        sal_info = json.load(open('sales.json'))
        sal_new_items={len(sal_info)+1:{'Product id':bil_item,'quantity':bil_quan,'price':bil_quan*int(fd[bil_item]['price'])}}
        sal={**sal_info, **sal_new_items}
        up_sal_json=open("sales.json",'w')
        up_sal_file=json.dumps(sal)
        up_sal_json.write(up_sal_file)
        up_sal_json.close()
    
        
    


# ### adding new item

# In[ ]:



    if gg=='4':
        flag=0
        item_id=input("Enter item ID : ")
        fd = json.load(open('new_json.json'))
        for i in fd:
             if i==item_id:
                print("Item found! please try updating option")
                flag=1
                break
        if flag==0:
            new_name=input("Enter item name : ")
            new_price=input("Enter item price : ")
            new_quantity=input("Enter item quantity : ")
            new_self=input("Enter item self : ")
            new_type=input("Enter item type : ")
            new_items={item_id:{'name':new_name,'price':new_price,'quantity':new_quantity,'self':new_self,
                                    'type':new_type}}
            ggez={**fd, **new_items}
            up_json=open("new_json.json",'w')
            up_file=json.dumps(ggez)
            up_json.write(up_file)
            up_json.close()
            print("Item added")
        
        
            


# ### sales display 

# In[ ]:




    if gg=='5':
        sales_file=json.load(open('sales.json'))
        print("**************************************************************************************************")
        print("                  SALES HISTORY                                                                   ")
        print("**************************************************************************************************")
        for i in sales_file:
            print("SNo. : ",i,"| Product ID : ",sales_file[i]['Product id'],"|Quantity : ",sales_file[i]['quantity'],
                  "|price : ",sales_file[i]['price'],)
            print("----------------------------------------------------------------------------------------------------")
            #print(j +"\n")


    