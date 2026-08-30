#!/usr/bin/env python3
"""borromean_apoly_renormalize.py — extract the classical diagonal Borromean
A-polynomial from the reconstructed quantum operator by the peripheral
renormalization the naive q->1 limit needs.

WHY. borromean_fast_extract.py found the naive q->1 limit of the operator
coefficients a_i(q,m) DEGENERATE: the monic-Q (CRT-compatible) normalization
leaves q-dependent poles at q=1, so lim_{q->1} a_coeff(i,k) is infinite for the
deepest-pole coefficients. The operator is defined only up to a common rational
left-multiplier, so this is a NORMALIZATION artifact, not a defect.

THE RENORMALIZATION (standard for a q-holonomic operator degenerating at q=1).
Let v = max over all coefficients of the pole order at q=1. Multiply the whole
operator by (q-1)^v (a valid common left-multiplier) and take q->1:

    a-tilde_coeff(i,k) = lim_{q->1} (q-1)^v * a_coeff(i,k)

Coefficients with pole order < v vanish (multiplied by (q-1)^{v-ord} -> 0); those
with the maximal pole order v survive finite. The surviving leading part is the
classical A-polynomial (the dominant balance of the recurrence at q=1):

    A(M,L) = sum_i ( sum_k a-tilde_coeff(i,k) * M^{2k} ) L^i     (m -> M^2)

This reuses the ALREADY-COMPUTED operator coefficients from
borromean-operator-explicit.json (no re-lift, no re-assembly).
"""
import json
import sympy as sp
from pathlib import Path

SRC = Path(__file__).with_name("borromean-operator-explicit.json")
OUT = Path(__file__).with_name("borromean-a-polynomial-classical.json")

q, M, L = sp.symbols("q M L")

d = json.load(open(SRC))
op = d["operator"]                      # {"a_0": {k: coeff_str}, ...}
W_WIN = d["m_window"]
R_ORD = d["order"]

def pole_order_at_1(expr):
    """Order of the pole of a rational function at q=1 (>=0; 0 = no pole)."""
    r = sp.together(sp.cancel(expr))
    num, den = sp.fraction(r)
    dm = sp.Poly(den, q).as_poly()
    nm = sp.Poly(num, q).as_poly()
    # multiplicity of (q-1) in denominator minus numerator
    dmult = dm.multiplicity(1) if hasattr(dm, "multiplicity") else 0
    # robust multiplicity via successive division
    def mult(poly):
        c, m = poly, 0
        while True:
            quo, rem = sp.div(c, sp.Poly(q - 1, q))
            if rem.is_zero:
                c, m = quo, m + 1
            else:
                break
        return m
    return mult(dm) - mult(nm)

# parse coefficients, find the max q=1 pole order
coeffs = {}   # (i,k) -> sympy expr in q
maxv = 0
for i in range(R_ORD + 1):
    ai = op.get(f"a_{i}", {})
    for kstr, cstr in ai.items():
        k = int(kstr)
        e = sp.sympify(cstr)
        coeffs[(i, k)] = e
        v = pole_order_at_1(e)
        if v > maxv:
            maxv = v
print(f"max q=1 pole order v = {maxv}; renormalizing by (q-1)^{maxv}", flush=True)

# renormalize and take q->1
Apoly = sp.Integer(0)
survivors = {}
for (i, k), e in coeffs.items():
    lim = sp.limit((q - 1) ** maxv * e, q, 1)
    if lim != 0:
        survivors[(i, k)] = lim
        Apoly += lim * M ** (2 * k) * L ** i

Apoly = sp.factor(sp.expand(Apoly))
print(f"\n*** CLASSICAL DIAGONAL BORROMEAN A-POLYNOMIAL ***")
print(f"A(M,L) = {Apoly}")
print(f"\nsurvivors ({len(survivors)} of {len(coeffs)} coefficients had the max pole order):")
for (i, k), lim in sorted(survivors.items()):
    print(f"  a_{i} m^{k}: {lim}")

result = {
    "computation": "borromean-a-polynomial-classical",
    "source_operator": SRC.name,
    "renormalization": f"(q-1)^{maxv} common left-multiplier, then q->1 (m->M^2)",
    "max_q1_pole_order": maxv,
    "classical_A_polynomial_ML": str(Apoly),
    "degenerate": bool(Apoly == 0),
    "n_survivor_coeffs": len(survivors),
    "n_total_coeffs": len(coeffs),
    "note": ("Classical diagonal Borromean A-polynomial candidate, from the q->1 "
             "leading part of the reconstructed order-6 quantum recurrence operator "
             "(6-prime CRT, exact-annihilation verified n=1..9). The operator "
             "degenerated under monic-Q normalization; this rescales by the q=1 "
             "pole order to recover the classical limit. NOT independently checked "
             "against a known Borromean A-polynomial (none in the literature for the "
             "diagonal restriction) -- this IS the candidate."),
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
print(f"\nwritten -> {OUT.name}")
