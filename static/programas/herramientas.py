import numpy as np
def DictToArray(my_dict):
    cols=(len(my_dict)-7)//3
    matriz = np.zeros((3,cols))
    for x in range(cols):
        matriz[0,x]=float(''.join(my_dict['form-'+str(x)+'-x']))
        matriz[1,x]=float(''.join(my_dict['form-'+str(x)+'-y']))
        matriz[2,x]=float(''.join(my_dict['form-'+str(x)+'-dydx']))

    return matriz
    
    
    

my_dict= {'csrfmiddlewaretoken': ['xVi60EGCeycyZJQSiPHCAFPerPSUc19LsRsDJBqgC6BufyamaOi4FFTf4NdzWtyw'], 
          'form-TOTAL_FORMS': ['4'], 
          'form-INITIAL_FORMS': ['0'], 
          'form-MIN_NUM_FORMS': ['0'], 
          'form-MAX_NUM_FORMS': ['1000'], 
          'form-0-x': ['1'], 
          'form-0-y': ['2'], 
          'form-0-dydx': ['0.0'], 
          'form-1-x': ['2'], 
          'form-1-y': ['-1'], 
          'form-1-dydx': ['1'], 
          'form-2-x': ['2.5'], 
          'form-2-y': ['0.0'], 
          'form-2-dydx': ['1'], 
          'form-3-x': ['4'], 
          'form-3-y': ['1'], 
          'form-3-dydx': ['-1'], 
          'cantidad': ['2'], 
          'btnCalc': ['btnCalc']}

