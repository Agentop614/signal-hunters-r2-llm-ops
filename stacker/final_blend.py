"""v14: average of stacker test probabilities. Usage: CACHE=cache/ DATA=data/ python final_blend.py"""
import os, numpy as np, pandas as pd
C=os.environ.get('CACHE','cache/'); D=os.environ.get('DATA','data/')
L=np.array(['eti_candidate','frb','pulsar','scintillating_star','satellite_pass','radar_chirp','rfi_intermittent','rfi_persistent','noise'])
te=pd.read_csv(D+'test_meta.csv')
v12=np.load(C+'test_stack_v12.npy'); hon=(np.load(C+'test_stack_h20.npy')+np.load(C+'test_stack_v14a.npy'))/2
for name,P in [('submission_r2_v14_blend.csv',(v12+hon)/2),('submission_r2_v14_honest.csv',hon)]:
    pd.DataFrame({'id':te.id,'label':L[P.argmax(1)]}).to_csv(name,index=False); print('wrote',name)
# v15: old-family stackers (v12, v13, v13a) averaged, then averaged with the honest wave-2 stackers
old=(np.load(C+'test_stack_v12.npy')+np.load(C+'test_stack_v13.npy')+np.load(C+'test_stack_v13a.npy'))/3
pd.DataFrame({'id':te.id,'label':L[((old+hon)/2).argmax(1)]}).to_csv('submission_r2_v15.csv',index=False); print('wrote submission_r2_v15.csv')
