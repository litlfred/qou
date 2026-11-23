"""Shared defs for the Lean generator of BondChiralitySixStrand (exact sympy, no float)."""
import sympy as sp, itertools, sys
q = sp.symbols('q'); h = q - 1/q
N = 6
def bits(s): return [(s >> j) & 1 for j in range(N)]
def zc(s): return sum(1 for b in bits(s) if b == 0)
SPACES = {k: [s for s in range(64) if zc(s) == k] for k in (1, 2, 4, 5)}
POS = {k: {s: p for p, s in enumerate(v)} for k, v in SPACES.items()}
def flip(s, i): return s ^ (3 << i)
def act_full(i, inv, vec):
    out = {}
    for s, c in vec.items():
        b = bits(s)
        if b[i] == b[i+1]:
            terms = [(s, q)]
        elif b[i] == 0:      # "01" -> "10"
            terms = [(flip(s, i), 1)]
        else:                # "10" -> "01" + h "10"
            terms = [(flip(s, i), 1), (s, h)]
        if inv: terms = terms + [(s, -h)]
        for t, v in terms: out[t] = out.get(t, 0) + c * v
    return {t: sp.cancel(v) for t, v in out.items() if sp.cancel(v) != 0}

def lean_poly(p):
    p = sp.Poly(sp.expand(p), q)
    terms = []
    for (e,), c in sorted(p.terms(), key=lambda x: -x[0][0]):
        c = int(c)
        mono = "" if e == 0 else ("q" if e == 1 else f"q^{e}")
        a = abs(c)
        if mono == "": body = f"{a}"
        elif a == 1: body = mono
        else: body = f"{a}*{mono}"
        terms.append(("-" if c < 0 else "+", body))
    if not terms: return "0"
    s = ("-" if terms[0][0] == "-" else "") + terms[0][1]
    for sg, b in terms[1:]: s += f" {sg} {b}"
    return s
def lean_expr(e):
    e = sp.cancel(sp.together(e))
    if e == 0: return "0"
    n, d = sp.fraction(e)
    n = sp.expand(n); d = sp.expand(d)
    # d should be c*q^m
    dp = sp.Poly(d, q)
    assert len(dp.terms()) == 1, d
    (m,), c = dp.terms()[0]; c = int(c)
    if c < 0: n = -n; c = -c
    ns = lean_poly(n)
    if m == 0 and c == 1: return f"({ns})"
    ds = (f"{c}*" if c != 1 else "") + ("q" if m == 1 else f"q^{m}") if m > 0 else f"{c}"
    return f"(({ns}) / {ds})"

V3 = lambda i: [(i, False), (i+1, True)]*3
V3m = lambda i: [(i, True), (i+1, False)]*3
P = lambda ws: [(i, False) for i in ws]
e3 = P([3, 4, 3]); e0 = P([0, 1, 0])
CASES = {
 "GL": (V3(0) + e3 + V3(2), [0,1,2], "`(σ₀σ₁⁻¹)³ · σ₃σ₄σ₃ · (σ₂σ₃⁻¹)³`, proton on strands `0–2` (bond `G`, ruled form)"),
 "GR": (e0 + V3(3) + V3(2), [3,4,5], "`σ₀σ₁σ₀ · (σ₃σ₄⁻¹)³ · (σ₂σ₃⁻¹)³`, proton on strands `3–5` (bond `G`, ruled form)"),
 "GpL": (V3(0) + e3 + V3m(2), [0,1,2], "`(σ₀σ₁⁻¹)³ · σ₃σ₄σ₃ · (σ₂⁻¹σ₃)³`, proton on strands `0–2` (bond `G′`, non-ruled comparison arm)"),
 "GpR": (e0 + V3(3) + V3m(2), [3,4,5], "`σ₀σ₁σ₀ · (σ₃σ₄⁻¹)³ · (σ₂⁻¹σ₃)³`, proton on strands `3–5` (bond `G′`, non-ruled comparison arm)"),
}
def pz(s, prot): return sum(1 for k in prot if bits(s)[k] == 0)
def needed(prot):
    plus = [(s, zc(s) - 3) for s in range(64) if pz(s, prot) == 2 and zc(s) != 3]
    minus = [(s, zc(s) - 3) for s in range(64) if pz(s, prot) == 1 and zc(s) != 3]
    return plus, minus
TARGET = {"GL": -4*q*h**4, "GR": (3*q**2+1)*h**4/q,
          "GpL": (q**2+1)*(3*q**4-2*q**2+1)*h**4/q, "GpR": -(3*q**2+1)*q**3*h**4}
TARGET_LEAN = {"GL": "-(4 * q * (q - q⁻¹) ^ 4)", "GR": "(3 * q ^ 2 + 1) * (q - q⁻¹) ^ 4 / q",
  "GpL": "(q ^ 2 + 1) * (3 * q ^ 4 - 2 * q ^ 2 + 1) * (q - q⁻¹) ^ 4 / q",
  "GpR": "-((3 * q ^ 2 + 1) * q ^ 3 * (q - q⁻¹) ^ 4)"}
