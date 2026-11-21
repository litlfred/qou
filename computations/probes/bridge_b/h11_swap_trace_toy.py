"""H11 toy: twisted (swap) trace vs plain trace of a doubled Hecke letter, exact sympy.
sigma on V = C^2 has eigenvalues {q, -1/q}. Doubled letter on V(x)V is sigma(x)sigma, mirror swap P.
Plain trace over both copies (H9 'summed'): spectrum of sigma(x)sigma.
Swap-twisted trace: tr(P (A(x)A)) = tr(A^2), spectrum of sigma^2.
Lusztig 16.7(b) folded bulk letter: spectrum {q^2, -q^-2}."""
import sympy as sp
q = sp.symbols('q', positive=True)
S = sp.diag(q, -1/q)
D2 = sp.kronecker_product(S, S)
P = sp.zeros(4, 4)
for i in range(2):
    for j in range(2):
        P[2*i + j, 2*j + i] = 1
for k in range(1, 4):
    plain = sp.simplify((D2**k).trace())
    twisted = sp.simplify((P * D2**k).trace())
    lusztig = sp.simplify(q**(2*k) + (-1)**k * q**(-2*k))
    print(f"k={k}: plain={sp.factor(plain)}  twisted={sp.factor(twisted)}  lusztig={sp.factor(lusztig)}  twisted==lusztig: {sp.simplify(twisted-lusztig)==0}")
print("eigenvalues of sigma(x)sigma:", sp.Matrix(D2).eigenvals())
