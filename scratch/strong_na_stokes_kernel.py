import sympy as sp
import json

def qbracket(q, k):
    return (q**k - q**(-k)) / (q - 1/q)

def evaluate_na_stokes(ratio_expr, q, q_sub, t, MAX_ORDER=4):
    ratio_t = sp.series(ratio_expr.subs(q, q_sub), t, 0, 2*MAX_ORDER + 2).removeO()
    transformed = ratio_t.subs(t, sp.I * t)
    real_transformed = sp.re(sp.expand(transformed))
    coeffs = []
    for N in range(MAX_ORDER + 1):
        coeff_raw = sp.series(real_transformed, t, 0, 2*MAX_ORDER + 2).removeO().coeff(t, 2*N)
        coeffs.append(str(sp.expand(coeff_raw)))
    return coeffs

def main():
    q = sp.symbols("q", positive=True)
    t = sp.symbols("t", real=True)
    q_sub = 1/(1-t)
    
    # 1. Gluonic Binding: Mediator T_{2,9}, Boundary 3_1 = T_{2,3}
    ratio_gluonic = sp.cancel(qbracket(q, 9) / qbracket(q, 3))
    
    # 2. Residual Strong Force: Mediator T_{2,5}, Boundary L2a1 = T_{2,2}
    ratio_residual = sp.cancel(qbracket(q, 5) / qbracket(q, 2))
    
    coeffs_gluonic = evaluate_na_stokes(ratio_gluonic, q, q_sub, t)
    coeffs_residual = evaluate_na_stokes(ratio_residual, q, q_sub, t)
    
    out = {
        "computation": "strong-na-stokes-kernel",
        "gluonic_ratio_T29_T23": {
            "topological_phase": coeffs_gluonic[0],
            "higher_order_phases": coeffs_gluonic[1:]
        },
        "residual_ratio_T25_T22": {
            "topological_phase": coeffs_residual[0],
            "higher_order_phases": coeffs_residual[1:]
        }
    }
    
    print("Gluonic Binding (T_{2,9} / T_{2,3}):", coeffs_gluonic[0])
    print("Residual Strong Force (T_{2,5} / T_{2,2}):", coeffs_residual[0])
    
    with open("strong-na-stokes-kernel.witness.json", "w") as f:
        json.dump(out, f, indent=2)

if __name__ == '__main__':
    main()
