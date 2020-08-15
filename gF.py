import numpy as np
import itertools

# modelPath = '/home/marcus/PycharmProjects/Toha/iRecModelEF.pkl'

def fastaTOprediction(stepSize, X, Y):

   m3 = list(itertools.product('ACDEFGHIKLMNPQRSTVWY', repeat=3))
   T = []
   t = []
   t = np.array(t)
   T = np.array(T)


   def isValid(x):
        for base in x:
            if not base in {'A' ,'C' ,'D' ,'E' ,'F' ,'G' ,'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'}:
                return 'Invalid'
        return 'Valid'

   def kmers(seq, k):
        v = []
        for i in range(len(seq) - k + 1):
            v.append(seq[i:i + k])
        return v

   

   

   def diMonoKGap(x, g):  # 2___1

        m = m3
        for i in range(1, x + 1, 1):
            V = kmers(g, i + 3)
            # seqLength = len(x) - (i+2) + 1

            # print(V)
            for gGap in m:
                # print(gGap[0], end='')
                # print(gGap[1], end='')
                # print('-'*i, end='')
                # print(gGap[2], end=' ')
                # trackingFeatures.append(gGap[0] + gGap[1] + '-' * i + gGap[2])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[1] == gGap[1] and v[-1] == gGap[2]:
                        C += 1
                # print(C, end=',')
                t.append(C)

   def monoDiKGap(x, g):  # 1___2

        m = m3
        for i in range(1, x + 1, 1):
            V = kmers(g, i + 3)
            # seqLength = len(x) - (i+2) + 1
            # print(V)
            for gGap in m:
                # print(gGap[0], end='')
                # print('-' * i, end='')
                # print(gGap[1], end='')
                # print(gGap[2], end=' ')
                # trackingFeatures.append(gGap[0] + '-' * i + gGap[1] + gGap[2])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[-2] == gGap[1] and v[-1] == gGap[2]:
                        C += 1
                # print(C, end=',')
                t.append(C)

   def countelement(k, sequence):
    ### k-mer ###
    ### A, AA, AAA
         k=3
         for i in range(1, k + 1, 1):
             v = list(itertools.product('ACDEFGHIKLMNPQRSTVWY', repeat=i))
             for i in v:
                 t.append(sequence.count(''.join(i))/len(sequence))
        
        
   def generateFeatures(Sequence):
                
      k = 1
      countelement(k, Sequence)
      diMonoKGap(k, Sequence)
      monoDiKGap(k, Sequence)
      T.append(t)
    

   def evaluateModel(X_test):
        
        generateFeatures(X_test)
        X = T[:,0:8420]   # X = T[:,0:419]
        Y = T[:,8420:16420]    # Y = T[:, 420]
        Z = T[:,16420:24420]
        import pickle   
        import os
        from statistics import mode
  
        final_pred = np.array([])
        this_folder = os.path.dirname(os.path.abspath(__file__))
        filename1 = os.path.join(this_folder,'model1.pkl')

        with open(filename1, 'rb') as pickleFile:
            model1 = pickle.load(pickleFile)
            pred1 = model1.predict(X)
            
        this_folder = os.path.dirname(os.path.abspath(__file__))
        filename2 = os.path.join(this_folder,'model2.pkl')

        with open(filename2, 'rb') as pickleFile:
            model2 = pickle.load(pickleFile)
            pred2 = model2.predict(Y)

        this_folder = os.path.dirname(os.path.abspath(__file__))
        filename3 = os.path.join(this_folder,'model3.pkl')

        with open(filename3, 'rb') as pickleFile:
            model3 = pickle.load(pickleFile)
            pred3 = model3.predict(Z)

        for i in range(0,len(Y)):
           probability = np.append(final_pred, mode([pred1[i], pred2[i], pred3[i]]))

        
	
        return probability     

        
