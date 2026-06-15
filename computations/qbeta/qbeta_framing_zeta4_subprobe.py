#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic structural exploration.
"""Q_β heat-route — FRAMING ζ₄ sub-probe (option 2 of the over-determination test).

Option 1 (qbeta_per_cell_zeta4_subprobe.py) showed ζ_4 is NOT a clean fibre
feature of the content-Casimir compatible with the bar-ODD a_1: ζ_4 needs a
content-≥3 cell (bar-neither), and the only bar-ODD per-cell content (c=1)
carries ζ_2 only. So if the heat kernel must carry ζ_4, it cannot come from
μ_λ. The remaining fibre candidate is the FRAMING factor of
F = Q_β/(Q_A·cos α_eff), with the on-main closed form
(qbeta_alpha_eff_hoefsmit_symbolic_probe.py):

    z      = 1/(√q + 1/√q) = √q/(q+1)     [bar-EVEN]
    h      = q − 1/q                       [bar-ODD]
    α_eff  = (z − 1)·h/2                    [bar-ODD]

Does the framing supply a GENUINE ζ_4 in the q variable, or only a √q double-
cover artifact that is really ζ_2 in q (the bar-FIXED point q=-1)?

METHOD (robust — the framing carries √q so it is NOT rational in q): do ALL
cyclotomic factoring in s=√q (everything is rational in s), then map each root
of unity Φ_d(s) to its ORDER in q=s². A primitive d-th root s gives q=s² of
order d/gcd(d,2). So:
    Φ_2(s) → q order 1 (q=1, classical)     Φ_3(s),Φ_6(s) → q order 3 (ζ_3)
    Φ_4(s) → q order 2 (q=-1, ζ_2, bar-fix) Φ_8(s)        → q order 4 (ζ_4!)
A GENUINE ζ_4 in q requires Φ_8(s) in the framing's s-form. This probe checks.

STRUCTURAL only; no c_3 value; flip-flop guard respected.
"""
from __future__ import annotations
import sympy as sp

q = sp.symbols('q', positive=True)
s = sp.symbols('s', positive=True)   # s = √q


def order_in_q(d):
    """Order of q=s² when s is a primitive d-th root of unity: d/gcd(d,2)."""
    import math
    return d // math.gcd(d, 2)


def s_carriers(expr_s, dmax=16):
    """Φ_d(s) dividing numer / denom of a rational expr in s."""
    expr_s = sp.cancel(expr_s)
    num = sp.Poly(sp.numer(expr_s), s)
    den_e = sp.denom(expr_s)
    den = sp.Poly(den_e, s) if den_e != 1 else None
    num_c, den_c = [], []
    for d in range(2, dmax + 1):
        Phi = sp.Poly(sp.cyclotomic_poly(d, s), s)
        if not num.is_zero and num.rem(Phi).is_zero:
            num_c.append(d)
        if den is not None and not den.is_zero and den.rem(Phi).is_zero:
            den_c.append(d)
    return num_c, den_c


def report(name, expr_q):
    es = sp.cancel(expr_q.subs(q, s ** 2))
    nc, dc = s_carriers(es)
    nq = sorted({order_in_q(d) for d in nc})
    dq = sorted({order_in_q(d) for d in dc})
    print(f"\n  {name}")
    print(f"    in s=√q: {es}")
    print(f"      Φ_d(s) | numer: d={nc}  → q-orders {nq}")
    print(f"      Φ_d(s) | denom: d={dc}  → q-orders {dq}")
    return nc, dc


def main():
    print("=" * 80)
    print("  FRAMING ζ_4 sub-probe — genuine Φ_8(√q)→ζ_4(q), or only Φ_4(√q)→ζ_2(q)?")
    print("=" * 80)

    z = sp.sqrt(q) / (q + 1)          # = 1/(√q + 1/√q)
    h = q - 1 / q                      # bar-odd
    alpha = sp.cancel((z - 1) * h / 2)
    two_q = 1 + q
    em = sp.cancel(two_q * (1 - h ** 2 * alpha))   # α_EM element [2]_q(1-h²α)

    all_d = []
    for nm, e in (("z = √q/(q+1)  [bar-even]", z),
                  ("h = q - 1/q  [bar-odd]", h),
                  ("α_eff = (z-1)·h/2  [bar-odd]", alpha),
                  ("α_EM element [2]_q·(1 - h²·α_eff)", em)):
        nc, dc = report(nm, e)
        all_d += nc + dc

    print("\n  ── VERDICT (data-driven) ──")
    has_phi8 = 8 in all_d
    q_orders = sorted({order_in_q(d) for d in all_d})
    print(f"  All Φ_d(√q) appearing in the framing: d ∈ {sorted(set(all_d))}")
    print(f"  Their orders in q (=s²):              {q_orders}")
    print(f"  genuine ζ_4 in q (needs Φ_8(√q))?     {has_phi8}")
    # confirm the Φ_4(s)=Φ_2(q) identity explicitly
    same = sp.simplify(sp.cyclotomic_poly(4, s) - sp.cyclotomic_poly(2, q).subs(q, s**2)) == 0
    print(f"  Φ_4(√q) == Φ_2(q) identity holds?     {same}  (q=-1 bar-fixed point)")
    print(f"""
  ⇒ The framing factor's root-of-unity structure maps to q-orders {q_orders}.
    {"It DOES" if has_phi8 else "It does NOT"} contain a genuine ζ_4 in q (Φ_8(√q)).
    The q+1 = Φ_2(q) factor reads as Φ_4(√q) in the double cover, but that is
    the SAME locus q=-1 (the bar-FIXED point), NOT a primitive 4th root in q.

    Combined with option 1 (content-Casimir μ_λ has no bar-odd ζ_4): NEITHER
    fibre object (μ_λ NOR cos α_eff) supplies a bar-odd-compatible genuine
    ζ_4(q). The synthesis's "ζ_4 residue" kernel constraint is therefore most
    likely (a) the √q radial double cover read as ζ_4 (really ζ_2 at q=-1), or
    (b) a post-cos-wrap ARCHIMEDEAN feature (Kashaev/Ohtsuki near q=i, after τ).
    Either way the fibre kernel R need NOT carry ζ_4 — that constraint is
    RELAXED. Live fibre constraints remain: bar-odd a_1 = κ_(2,1) and the
    period-3/ζ_6 resonance (both realisable, option 0).""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
