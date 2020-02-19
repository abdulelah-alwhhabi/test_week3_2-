def take_from_menu(category,set_to_save_to):

    for i in range(len(ingredients[category])):
        print ( str(i+1) + "--" + ingredients[category][i]  )
    x = int(input("\nWrite an %s you'll buy\n  >>>>>    " %(category)))
    return set_to_save_to.add(str(ingredients[category][x-1]))


print ('-'*50 )
print('*'*50 )
print('-'*50)
print('you are in a grocery store !! Just tell me what do you want and I will help you to know what to cock \n ')

ingredients = {'protein' :['Chicken' , 'Lamb' , 'teriyaki' ,'egg'] , 'carbs':['Rice', 'Pasta' ,'tortilla'] }

userinputs = set()
foods  = {'Checken_Kabsa':{'Chicken', 'Rice','Spices', 'tomato'},
'Lamb_Biryani':{'Lamb','Rice','Spices','tomato', 'pepper'},
'chinese rice':{'egg','Rice', 'Vegetables',},
'teriyaki_fried_rice': {'Rice','teriyaki','Lemon'},
'chicken_fettuccine':{'Pasta','Chicken','sauce' },
'Lamb_bechamel_pasta':{'Lamb','Pasta','Cheese'},
'spaghetti_with_fried_egg':{'Pasta','egg','parsley'},
'teriyaki_noodles':{'teriyaki','Pasta','bean'},
'Chicken_shawrma':{'Chicken','tortilla','onion','shatta_LOL'},
'tacos':{'tortilla','Lamb','sauce'},
'shakshuka_sandwich':{'egg','tortilla','cream_cheese'},
'teriyaki_tuna_sandwich':{'tortilla','teriyaki','tuna'}}  #################################3
# print(len(ingredients['protein']))




take_from_menu('protein',userinputs)
take_from_menu('carbs',userinputs )


for i in foods:
    true_or_false =  userinputs.issubset(foods[i])
    if true_or_false == True :
        print ('you can make >>>> ' + str(i) + '  Happy cooking!!!!' )
    else :
        pass
