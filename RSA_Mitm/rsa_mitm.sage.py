
# This file was *autogenerated* from the file rsa_mitm.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_17 = Integer(17); _sage_const_23 = Integer(23); _sage_const_19 = Integer(19); _sage_const_24 = Integer(24)

def rsa_setup():
  p = _sage_const_23 
  q = _sage_const_19 
  e = _sage_const_17 
  
  N = p*q
  phi_N = (p-_sage_const_1 )*(q-_sage_const_1 )
  
  print "gcd(e,phi_N) = ", gcd(e,phi_N)
  
  d = power_mod(e,-_sage_const_1 ,phi_N)
  
  return [N,e,d]
  

def rsa_exp(inp, exp, N):
  return power_mod(Integer(inp),Integer(exp),Integer(N))



def mitm(d,c):
  B = d
  A = ceil(sqrt(B))
  print "A: ", A
  
  d0 = []
  
  for i in range(_sage_const_0 , A):
    d0.append( power_mod(c, A*i, N)  )
    
  print d0
  
  for j in range(_sage_const_0 , A):
    #tmp = power_mod(c, -1, N)
    #tmp = power_mod(tmp, j, N)
    tmp = m * power_mod(c, -j, N)
    
    print tmp, tmp in d0
    
    if(tmp in d0):
      d0_index = d0.index(tmp)
      print "d0_index: ", d0_index
      d1_index = j
      print "d1_index: ", d1_index
      
      restored_d = d0_index * A + d1_index
      print "restored_d: ", restored_d

  

params = rsa_setup()
N = params[_sage_const_0 ]
e = params[_sage_const_1 ]
d = params[_sage_const_2 ]

print "key d : " , d

m = _sage_const_24 
c = rsa_exp(m,e,N)

print "Cipher c: ", c

m_new = rsa_exp(c,d,N)

print "Plain m_new: ", m


mitm(d,c)



