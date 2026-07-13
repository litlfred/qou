import sys
import sympy as sp

def main():
    q = sp.symbols("q")
    h = q - 1/q
    t = sp.symbols("t", real=True)
    q_sub = 1/(1-t)
    
    # We use the framework's proven delta_q decoration (bar-odd trivial-channel twist)
    def delta_q(w):
        return q**w - q**(-w)
        
    dq_T35 = delta_q(10)  # T_{3,5} writhe = 10
    dq_3_1 = delta_q(3)   # 3_1 (T_{2,3}) writhe = 3
    
    counit = h**2/2 - h
    
    # The categorical action difference
    # Q_beta is driven by the interaction shift: T_3_5 (mediator) vs 3_1 (boundary)
    # The topological deformation factor is proportional to their ratio or difference.
    # If we take the NA-Stokes integral of the deformation ratio:
    ratio_A = sp.cancel(dq_T35 / dq_3_1)
    
    MAX_ORDER = 4
    ratio_t = sp.series(ratio_A.subs(q, q_sub), t, 0, 2*MAX_ORDER + 2).removeO()
    transformed = ratio_t.subs(t, sp.I * t)
    real_transformed = sp.re(sp.expand(transformed))
    
    z_sub = sp.sqrt(q_sub)/(1+q_sub)
    h_sub = q_sub - 1/q_sub
    alpha_sub = (z_sub - 1)*h_sub/2
    b_sub = sp.sqrt((h_sub**2 + 3)/(h_sub**2 + 4))
    
    cos_arg = sp.series(alpha_sub - b_sub*t**2/2, t, 0, 2*MAX_ORDER + 2).removeO()
    cos_base = sp.series(sp.cos(cos_arg), t, 0, 2*MAX_ORDER + 2).removeO()
    
    ladder = sp.series(real_transformed / cos_base, t, 0, 2*MAX_ORDER + 2).removeO()
    
    print("NA-Stokes evaluation of interaction ratio (T_{3,5} / 3_1):")
    for N in range(0, MAX_ORDER + 1):
        coeff = ladder.coeff(t, 2*N)
        print(f"O(t^{2*N}): {sp.simplify(coeff)}")
        
if __name__ == '__main__':
    main()
