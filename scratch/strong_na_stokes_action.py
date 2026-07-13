import sys
import sympy as sp

def main():
    q = sp.symbols("q")
    h = q - 1/q
    t = sp.symbols("t", real=True)
    q_sub = 1/(1-t)
    
    # Let's directly use the q-bracket ratio which represents the normalized topological action
    def qbracket(k):
        return (q**k - q**(-k)) / h
        
    # The two strong sector interactions:
    # 1. Gluonic / internal binding (T_2,9 / T_2,3)
    ratio_gluonic = sp.cancel(qbracket(9) / qbracket(3))
    
    # 2. Residual strong force / nucleon-nucleon (T_2,5 / T_2,2)
    ratio_residual = sp.cancel(qbracket(5) / qbracket(2))
    
    MAX_ORDER = 4
    
    def process_ratio(ratio_expr, name):
        ratio_t = sp.series(ratio_expr.subs(q, q_sub), t, 0, 2*MAX_ORDER + 2).removeO()
        transformed = ratio_t.subs(t, sp.I * t)
        real_transformed = sp.re(sp.expand(transformed))
        
        print(f"=== {name} ===")
        for N in range(MAX_ORDER + 1):
            coeff_raw = sp.series(real_transformed, t, 0, 2*MAX_ORDER + 2).removeO().coeff(t, 2*N)
            c_k = sp.expand(coeff_raw)
            print(f"O(t^{2*N}) phase = {c_k}")
        print()

    process_ratio(ratio_gluonic, "Gluonic Binding (T_{2,9} / T_{2,3})")
    process_ratio(ratio_residual, "Residual Strong Force (T_{2,5} / T_{2,2})")

if __name__ == '__main__':
    main()
