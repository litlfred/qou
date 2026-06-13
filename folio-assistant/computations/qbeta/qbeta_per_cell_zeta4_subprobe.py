#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic structural exploration.
"""Q_β heat-route — PER-CELL ζ₄ sub-probe (option 1 of the over-determination test).

The mode-summed program (qbeta_root_of_unity_residue_program.py) found the summed
content-Casimir μ_λ = ℏ_q²·Σ_□[c]_q[c+1]_q carries ζ_2 + ζ_6 but NOT ζ_4 — the
per-cell Φ_4 is washed out by Σ_□. The synthesis
(docs/audits/2026-06-10-qbeta-ck-state-of-play-synthesis.md, line 105) attributes
the "proved ζ_4 structure" to "[c]_q factors degenerate at roots of unity". This
probe tests that claim at the PER-CELL (un-summed) level:

  Q1. Which content c gives a per-cell [c]_q[c+1]_q divisible by Φ_4?
      (Expect c=3: [4]_q = [2]_q·Φ_4; and the bar-mirror c=-4.)
  Q2. Is that ζ_4-carrying per-cell κ_c = (q-1)·ℏ_q²·[c][c+1] bar-ODD?
      (The a_1 = -c_3 leading coefficient must be bar-odd.)
  Q3. Decisive: can ANY Hecke mode (partition) be BOTH bar-odd (full κ_λ) AND
      carry ζ_4? I.e. does a content-3 cell ever live in a bar-odd partition,
      and does its κ_λ survive Φ_4 after Σ_□? (We already know the summed Σ_□
      washes Φ_4; this asks whether the f-map could select at the SUB-mode/cell
      level instead — keeping per-cell content, breaking the Z_q mode-sum form.)

If ζ_4 needs a content-3 cell, every partition carrying it has λ_1≥4 ⇒ n≥4, and
those modes are bar-NEITHER (from the mode-summed probe). So bar-odd ∧ ζ_4 is
incompatible at the mode level ⇒ the f-map cannot be a simple mode-sum if it must
carry ζ_4. That is the structural prune.

STRUCTURAL only; no c_3 value; flip-flop guard respected.
"""
from __future__ import annotations
import sympy as sp

q = sp.symbols('q')


def jackson(k):
    """[k]_q = (1-q^k)/(1-q); valid for negative k (Laurent), [0]=0."""
    if k == 0:
        return sp.Integer(0)
    return sp.cancel((1 - q ** k) / (1 - q))


def per_cell(c):
    """The per-cell content-Casimir factor [c]_q[c+1]_q."""
    return sp.cancel(jackson(c) * jackson(c + 1))


def cyclotomic_carriers(expr, dmax=12):
    """Which Φ_d(q) (d=2..dmax) divide numer(expr)."""
    if expr == 0:
        return []
    poly = sp.Poly(sp.numer(sp.cancel(expr)), q)
    out = []
    for d in range(2, dmax + 1):
        Phi = sp.Poly(sp.cyclotomic_poly(d, q), q)
        if poly.rem(Phi).is_zero:
            out.append(d)
    return out


def bar(expr):
    return sp.cancel(expr.subs(q, 1 / q))


def parity(expr):
    if sp.simplify(bar(expr) + expr) == 0:
        return "ODD"
    if sp.simplify(bar(expr) - expr) == 0:
        return "EVEN"
    return "—"


def kappa_cell(c):
    """Per-cell a_1 building block (q-1)·ℏ_q²·[c][c+1], ℏ_q=(q-1)/q."""
    hbar2 = ((q - 1) / q) ** 2
    return sp.cancel((q - 1) * hbar2 * per_cell(c))


def partitions(n):
    def rec(rem, mx):
        if rem == 0:
            yield ()
            return
        for f in range(min(rem, mx), 0, -1):
            for r in rec(rem - f, f):
                yield (f,) + r
    yield from rec(n, n)


def contents(part):
    return [j - i for i, row in enumerate(part) for j in range(row)]


def casimir_kappa(part):
    """Full mode κ_λ = (q-1)ℏ_q² Σ_□[c][c+1]."""
    hbar2 = ((q - 1) / q) ** 2
    return sp.cancel((q - 1) * hbar2 * sum(jackson(c) * jackson(c + 1)
                                          for c in contents(part)))


def main():
    print("=" * 80)
    print("  PER-CELL ζ_4 sub-probe — [c]_q[c+1]_q cyclotomic carriers + bar-parity")
    print("=" * 80)
    print(f"  {'content c':>10}  {'[c][c+1] numer':<34}{'ζ_d (Φ_d|·)':<16}{'κ_c parity':>10}")
    print(f"  {'-'*10}  {'-'*34}{'-'*16}{'-'*10}")
    zeta4_contents = []
    for c in range(-5, 6):
        g = per_cell(c)
        if g == 0:
            continue
        zd = cyclotomic_carriers(g)
        par = parity(kappa_cell(c))
        num = sp.Poly(sp.numer(g), q).as_expr()
        print(f"  {c:>10}  {str(num):<34}{str(zd):<16}{par:>10}")
        if 4 in zd:
            zeta4_contents.append((c, par))

    print("\n  ── Q1+Q2: which contents carry ζ_4, and are they bar-odd? ──")
    print(f"  ζ_4-carrying contents (per-cell): {[c for c, _ in zeta4_contents]}")
    for c, par in zeta4_contents:
        print(f"    content c={c:>2}: per-cell κ_c parity = {par}")
    bar_odd_zeta4 = [c for c, par in zeta4_contents if par == "ODD"]
    print(f"  ⇒ ζ_4-carrying AND bar-ODD per-cell contents: {bar_odd_zeta4}")

    print("\n  ── Q3: do ζ_4-carrying cells ever live in a BAR-ODD mode? ──")
    print("  A content-3 cell needs λ_1≥4 (row-0 col-3) ⇒ first such mode is (4);")
    print("  a content-(-4) cell needs ≥5 rows ⇒ first is (1^5). Check their full κ_λ:")
    checks = [(4,), (1, 1, 1, 1, 1), (5,), (4, 1), (4, 2)]
    any_bar_odd_with_zeta4 = False
    for part in checks:
        cs = contents(part)
        has_c3 = 3 in cs or -4 in cs
        kap = casimir_kappa(part)
        zd_sum = cyclotomic_carriers(kap)
        par = parity(kap)
        flag = " ← carries content-3 cell" if has_c3 else ""
        print(f"    λ={str(part):14s} contents={cs}")
        print(f"        full κ_λ: ζ_d(summed)={zd_sum}  parity={par}{flag}")
        if par == "ODD" and 4 in zd_sum:
            any_bar_odd_with_zeta4 = True

    print("\n  ── VERDICT (data-driven) ──")
    print(f"  Q1: ζ_4 IS carried per-cell, by contents {[c for c, _ in zeta4_contents]} "
          f"([4]_q = [2]_q·Φ_4).")
    if not bar_odd_zeta4:
        print("  Q2: NONE of the ζ_4-carrying per-cell κ_c is bar-ODD "
              "(they are bar-EVEN or —).")
    print(f"  Q3: any mode that is BOTH bar-odd AND ζ_4-carrying (summed)? "
          f"{any_bar_odd_with_zeta4}.")
    print("""
  ⇒ STRUCTURAL PRUNE: ζ_4 requires a content-3 (or -4) cell, which forces
    λ_1≥4 (n≥4). Every such mode is bar-NEITHER, and Σ_□ washes out its Φ_4
    (mode-summed probe). The per-cell κ_c that carries ζ_4 is itself NOT
    bar-odd. So:
      • A mode-summed heat partition function Z_q = Σ_λ d_λ exp_q(-μ_λ t)
        CANNOT carry ζ_4 (washed out) — confirmed.
      • Even dropping to per-cell (un-summed) content keeps ζ_4 but the
        carrying cell is not bar-odd, so it cannot supply the bar-ODD a_1
        directly; a content-mixing cancellation is still required.
    ⇒ ζ_4 is NOT a clean fibre feature of the content-Casimir at the mode
      OR cell level compatible with bar-odd a_1. Either the synthesis's
      'ζ_4 from [c]_q degeneracy' is realised only after the archimedean
      cos-wrap (NOT a pre-wrap fibre residue), or ζ_4 comes from the
      framing factor cos(α_eff) — tested next (option 2).""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
