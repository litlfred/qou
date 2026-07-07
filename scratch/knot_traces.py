import sympy as sp

q, w = sp.symbols('q w', real=True)
h = q - 1/q
z = sp.sqrt(q) / (1 + q)  # The Markov parameter

# Let's define the Hecke algebra trace recursively for sigma_1^k
# sigma^2 = h * sigma + 1
def tr_sigma(k):
    if k == 0:
        return sp.S.One
    elif k == 1:
        return z
    else:
        return sp.expand(h * tr_sigma(k-1) + tr_sigma(k-2))

# 1. Standard Topological Trace (no crossing weight w, just standard q)
print("--- Standard Topological Trace ---")
print(f"Unknot (sigma^1): {tr_sigma(1)}")
print(f"Hopf Link (sigma^2): {tr_sigma(2)}")
print(f"Trefoil (sigma^3): {tr_sigma(3)}")
print()

# Now, introduce the Evaluation Map E(w) which replaces the basic trace of a crossing.
# As established by KC19, the archimedean evaluation map on the N=0 nucleon NF difference is:
# E(w) = h^2 / 2 - h * w
def eval_map(w_val):
    return h**2 / 2 - h * w_val

print("--- Modulated Trace with Crossing Weight w ---")
# The crossing weight w replaces the standard topological loop z.
# For k crossings, the simplest modulation would just be replacing the linear sigma term.
# However, the Hopf link has TWO crossings, so its evaluation involves w^2.
# Let's show the ladder factor L(w) which is the ratio E(w)/E(1)
L_w = eval_map(w) / eval_map(1)
print(f"Ladder Factor L(w) (1 crossing): {sp.simplify(L_w)}")

# To "feel" c3, you need at least 2 crossings because c3 is the non-linear deviation.
# In the Hopf sector (sigma^2), we have w^2.
hopf_modulated = w**2 * (q**2 + q**-2 - 2)**3 # (Just a symbolic representation of the Hopf cubic)
print(f"Hopf Modulated Sector: w^2 * C_Hopf(y)")
