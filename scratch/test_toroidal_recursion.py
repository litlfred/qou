import numpy as np
import scipy.special as sp
import sys

def test_toroidal_recursion():
    q0 = 1.10997858
    z_val = (q0 + 1.0/q0) / 2.0
    
    # We want to check the recursion relation of toroidal harmonics
    # and see if there is any constant-coefficient or specific recurrence 
    # that matches the c_k values.
    # The known c_k values (from empirical/Habiro) are:
    c_1 = 0
    c_2 = -1
    # c_3 is approx -2.07
    c_3 = -2.072234 # from previous runs
    
    # Let's generate Toroidal Harmonics P_{k-0.5}^m(z) for k=1..5
    for m in [0, 1, 2]:
        print(f"Testing m={m}")
        p_vals = []
        for k in range(1, 6):
            try:
                # scipy.special.lpmv uses branch cut [-1, 1], so for z > 1 it's real?
                # Actually, lpmv for z > 1 might return NaN if not careful, 
                # but earlier we saw m=0 works, m=1 gave NaN.
                # Let's use the hypergeometric definition for z > 1 if NaN occurs.
                v = k - 0.5
                # P_v^m(z) = (z+1)^{m/2} (z-1)^{-m/2} / Gamma(1-m) * 2F1(-v, v+1; 1-m; (1-z)/2)
                # For m positive integer, we can use the relation P_v^m(z) = (z^2-1)^{m/2} d^m/dz^m P_v(z)
                # Let's use sp.hyp2f1 directly to be safe for any m.
                
                if m == 0:
                    val = sp.hyp2f1(-v, v+1, 1, (1-z_val)/2)
                else:
                    # m > 0 integer:
                    # P_v^m(z) = (-1)^m \Gamma(v+m+1)/\Gamma(v-m+1) P_v^{-m}(z)
                    # P_v^{-m}(z) = 1/\Gamma(1+m) ((z-1)/(z+1))^{m/2} 2F1(-v, v+1, m+1, (1-z)/2)
                    factor = ((-1)**m * sp.gamma(v+m+1) / sp.gamma(v-m+1)) if m > 0 else 1
                    term1 = 1.0 / sp.gamma(1+m)
                    term2 = ((z_val-1)/(z_val+1))**(m/2.0)
                    term3 = sp.hyp2f1(-v, v+1, m+1, (1-z_val)/2)
                    val = factor * term1 * term2 * term3
                
                p_vals.append(val)
                print(f"  P_{v}^{m} = {val}")
            except Exception as e:
                print(e)
                
test_toroidal_recursion()
