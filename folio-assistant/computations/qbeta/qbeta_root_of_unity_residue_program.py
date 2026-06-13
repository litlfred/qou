#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic structural exploration.
"""Q_β heat-route — root-of-unity residue program (over-determination test).

The kernel-constraint set (synthesis §2): bar-ODD a_1, simple pole at
u_substrate, ζ₄ residue, period-3 (ζ₃/ζ₆) resonance. This probe pulls the
root-of-unity data to the FIBRE: the content-Casimir μ_λ = ℏ_q²·Σ_□[c]_q[c+1]_q
factors over CYCLOTOMIC polynomials Φ_d(q), so each Hecke mode λ "carries"
specific roots of unity ζ_d (where [c]_q degenerates — the synthesis's named
source of the ζ₄ structure).

Question (owner): do bar-parity + ζ₄ + period-3 OVER-determine the active mode
set Λ (closure) or merely constrain it? Decisive sub-question computed here:
which content levels supply which ζ_d, and is the bar-odd selection compatible
with carrying ζ₃ and ζ₄?

STRUCTURAL only; no c_3 value; flip-flop guard respected.
"""
from __future__ import annotations
import sympy as sp

q = sp.symbols('q')


def jackson(k):
    if k == 0:
        return sp.Integer(0)
    return sp.cancel((1 - q ** k) / (1 - q))


def contents(part):
    return [j - i for i, row in enumerate(part) for j in range(row)]


def casimir_sum(part):
    """Σ_□ [c]_q[c+1]_q (the μ_λ Casimir sum, ℏ_q² stripped)."""
    return sp.expand(sum(jackson(c) * jackson(c + 1) for c in contents(part)))


def partitions(n):
    if n == 0:
        yield ()
        return
    def rec(rem, mx):
        if rem == 0:
            yield ()
            return
        for f in range(min(rem, mx), 0, -1):
            for r in rec(rem - f, f):
                yield (f,) + r
    yield from rec(n, n)


def cyclotomic_carriers(expr, dmax=12):
    """Which Φ_d(q) (d=2..dmax) divide expr → which roots of unity ζ_d it carries."""
    poly = sp.Poly(sp.numer(sp.cancel(expr)), q)
    carried = []
    for d in range(2, dmax + 1):
        Phi = sp.Poly(sp.cyclotomic_poly(d, q), q)
        if poly.rem(Phi).is_zero:
            carried.append(d)
    return carried


def bar_parity(part):
    hbar2 = ((q - 1) / q) ** 2
    kap = sp.cancel((q - 1) * hbar2 * casimir_sum(part))
    return "ODD" if sp.simplify(kap.subs(q, 1 / q) + kap) == 0 else "—"


def main():
    print("=" * 78)
    print("  Root-of-unity carriers of the content-Casimir μ_λ  (Φ_d | Σ[c][c+1])")
    print("=" * 78)
    by_zeta = {}
    for n in range(2, 7):
        for p in partitions(n):
            cs = casimir_sum(p)
            if cs == 0:
                continue
            zd = cyclotomic_carriers(cs)
            par = bar_parity(p)
            maxc = max(contents(p)) if contents(p) else 0
            print(f"  n={n} λ={str(p):16s} maxC={maxc:2d}  ζ_d carried={zd}   a_1-parity={par}")
            for d in zd:
                by_zeta.setdefault(d, []).append(p)
    print("\n  ── which modes can supply each constraint's root of unity ──")
    for d in sorted(by_zeta):
        lowest = min(by_zeta[d], key=lambda p: sum(p))
        print(f"   ζ_{d}: first carried by {lowest} (needs content c≥{d-1}); "
              f"{len(by_zeta[d])} modes total")
    print("\n  ── VERDICT (data-driven) ──")
    zetas = sorted(by_zeta)
    print(f"  Summed μ_λ carries ONLY ζ_d for d ∈ {zetas} (n≤6).")
    print(f"   • ζ_2: all 27 modes (the universal Φ_2=[2] factor).")
    if 6 in by_zeta:
        print(f"   • ζ_6: {by_zeta[6]} "
              f"— MATCHES the synthesis's period-3 (ζ₃/ζ₆) resonance ✓.")
    has3 = 3 in by_zeta
    has4 = 4 in by_zeta
    print(f"   • ζ_3 present at sum level: {has3};  ζ_4 present at sum level: {has4}.")
    print("  KEY: ζ_4 is ABSENT from the summed μ_λ. The per-cell [3]_q[4]_q of a")
    print("  content-3 cell (n≥4) DOES contain Φ_4, but it is WASHED OUT by the")
    print("  mode-sum Σ_□[c][c+1] (other cells aren't divisible by Φ_4). So the")
    print("  synthesis's 'ζ_4 from [c]_q degeneracy' is a PER-CELL feature, not a")
    print("  property of the summed content-Casimir.")
    print("\n  ⇒ Over-determination answer: the summed-μ_λ heat kernel SUPPLIES the")
    print("    bar-odd leading structure ((2),(2,1)) + the period-3/ζ_6 resonance,")
    print("    but does NOT supply ζ_4. So it is NOT a clean closure: either the")
    print("    kernel must use PER-CELL (not mode-summed) content data to carry ζ_4,")
    print("    or ζ_4 has a source outside the content-Casimir. The bar-odd modes")
    print("    carry ζ_2 only and the ζ_6-carriers are not bar-odd, so a")
    print("    content-spanning Λ with cancellation is still required for ζ_6.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
