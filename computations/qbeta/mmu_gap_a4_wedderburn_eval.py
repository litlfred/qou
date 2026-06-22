import sympy as sp
import mpmath as mp

def main():
    mp.mp.dps = 60
    
    q_val = mp.mpf("1.1099785955573347198997632204832250266562084087801536866079811461")
    
    # Let's compute the (2,1) representation matrices of sigma_1, sigma_2
    q = sp.Symbol('q')
    
    # Standard Iwahori-Hecke algebra H_3(q) matrices for lambda=(2,1)
    # Using the standard Hoefsmit / Wenzl representation
    # sigma_1 = [[q, 0], [1, -1]]
    # sigma_2 = [[-1, q], [0, q]]
    
    s1 = sp.Matrix([[q, 0], [1, -1]])
    s2 = sp.Matrix([[-1, q], [0, q]])
    s1_inv = sp.simplify(s1.inv())
    s2_inv = sp.simplify(s2.inv())
    
    # 4_1 knot braid word: (s1 * s2_inv)^2
    braid = s1 * s2_inv
    braid_sq = sp.simplify(braid * braid)
    
    chi_21 = sp.trace(braid_sq)
    print(f"chi_21(q) = {chi_21}")
    
    # Wenzl weights:
    # y_(3) = [4]_q / [2]_q^3
    # y_(2,1) = 1 / [2]_q^2
    # y_(1,1,1) = 0
    # where [k]_q = (q^k - 1) / (q - 1) (Wait, standard quantum integer is (q^k - q^-k)/(q - q^-1) or (1-q^k)/(1-q)?)
    # Let's use hbar_q definition [2]_q = 1 + q
    
    # Evaluate chi_21 at q_0
    chi_21_val = chi_21.subs(q, sp.Float(str(q_val), 60))
    print(f"chi_21(q_0) = {chi_21_val}")
    
    # We want to see if chi_21 or something similar provides a factor of (1 + 210e-9)
    # The discrepancy is 209.75 ppb.
    # What is the deviation of chi_21 from something?
    # chi_21 is a polynomial in q.
    
    chi_21_eval = float(chi_21_val)
    print(f"Numeric chi_21: {chi_21_eval}")
    
    # What if the mass correction is exactly chi_21 / 2 ?
    # 2 is the classical dimension of (2,1)
    print(f"chi_21 / 2: {chi_21_eval / 2}")
    
    # What is the exact 209.75 ppb factor?
    target_factor = 1.0 - 209.75e-9
    print(f"Target factor: {target_factor}")

if __name__ == "__main__":
    main()
