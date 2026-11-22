"""Prereg Addendum 1 (commit 622bdfe7ae1): is E0's weight w = hbar_q/q^2 a tower-level object?

Computes, in exact Q(q) arithmetic (sympy), the order of vanishing at q = 1 of the four
preregistered tower candidates, and checks each for exact equality with w. No numbers at q0.
"""
import sympy as sp

q, lam = sp.symbols("q lambda", positive=True)
hb = 1 - 1 / q
h = q - 1 / q
zD = q**3 / (q**2 + 1)
w = (q - 1) / q**3


def ord1(expr):
    """Order of the zero (negative: pole) of a rational function at q = 1."""
    num, den = sp.fraction(sp.factor(sp.together(expr)))
    def mult(p):
        p = sp.Poly(sp.expand(p), q)
        k = 0
        while p.eval(1) == 0:
            p = sp.Poly(sp.quo(p.as_expr(), q - 1), q)
            k += 1
        return k
    return mult(num) - mult(den)


cands = {}
# T1 brane tower (lambda generic, finite and nonzero at q = 1)
for n in (1, 2, 3):
    cands[f"T1 level n={n}: (hbar^2 lam)^{n}"] = (hb**2 * lam) ** n
cands["T1 sum: hbar^2 lam/(1-hbar^2 lam)"] = hb**2 * lam / (1 - hb**2 * lam)
cands["T1 implemented: 1/(1-hbar^2) - 1"] = 1 / (1 - hb**2) - 1
# T2 Markov stabilisation tower
for n in (1, 2, 3):
    cands[f"T2 z_D^{n}"] = zD**n
cands["T2 sum: z_D/(1-z_D)"] = zD / (1 - zD)
# T3 the target's own geometric tower
for k in (2, 3, 4):
    cands[f"T3 level q^-{k}"] = q**-k
for N in (2, 3, 5):
    cands[f"T3 partial S_{N}"] = sum(q**-k for k in range(2, N + 1))
cands["T3 full: 1/(q(q-1))"] = 1 / (q * (q - 1))
# T4 skein difference h*tau(beta), for the preregistered words with known closed forms
cands["T4 h*tau(1_n)"] = h
cands["T4 h*tau(sigma), n=2 (= h z_D)"] = h * zD
cands["T4 h*tau(sigma^-1), n=2"] = h / (q * (q**2 + 1))

lines = [f"target w = {sp.factor(w)},  ord1(w) = {ord1(w)}", ""]
ok = True
for name, X in cands.items():
    X1 = X.subs(lam, sp.Symbol("lambda_1", positive=True)) if X.has(lam) else X
    o = ord1(X1 if not X.has(lam) else X)
    exact = sp.simplify(X - w) == 0
    lead, c = "", None
    if o == 1:
        c = sp.limit(X / (q - 1), q, 1)
        lead = f", leading coeff X/(q-1) at 1 = {c}"
    if exact:
        verdict = "EQUAL"
    elif o != 1:
        verdict = "excluded by ord1"
    elif c != 1:
        verdict = "excluded by leading coefficient (w has 1)"
    else:
        verdict = "first-order match only (not equal)"
    lines.append(f"{name:42s} ord1 = {o:>2}{lead}  -> {verdict}")
    ok &= not exact
lines += ["", "required value for T4 equality: tau(beta) = w/h = " + str(sp.factor(w / h)),
          "  has a pole at q = -1; every word trace is N(q)/(q^2+1)^n with N Laurent, finite at q = -1",
          "", f"no candidate equals w: {ok}"]
out = "\n".join(lines)
print(out)
open(__file__.replace(".py", "_result.txt"), "w").write(out + "\n")
