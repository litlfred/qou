#!/usr/bin/env python3
"""qbeta_dladder_q_holonomic_base3_probe.py

The q-holonomic follow-up to the coupled-recurrence test
(qbeta_dladder_coupled_qsqrt3_recurrence_probe.py, PR #3737). That test — and the
merged structure hunt (#3716) — ruled out recurrences whose coefficients are
**polynomial in k**. For a q-Gevrey series that is the wrong class: the natural
object is a **q-difference (q-holonomic) recurrence**, coefficients polynomial in
`X^k` for a base `X`. This probe runs that test with the base fixed **by the
observed arithmetic, not by fitting**.

## Why base X = 3 (principled, not a free parameter)

The exact `d_k = a_k + b_k√3` have denominators that are **3-power-dominated**:
the 3-adic valuation `v_3(den d_k)` grows ~1.5·k (the merged hunt's
"factorial-smooth / Ohtsuki–Habiro" denominators; 3-adic branch of PR #3737's
grading table). A q-holonomic recurrence in base 3,

    Σ_{i=0}^{r} P_i(3^k)·d_{k-i} = 0,   P_i(Y) = Σ_{d=0}^{E} (A_{id}+B_{id}√3) Y^d,

has coefficients `3^{k·d}` that **exactly clear** those 3-power denominators —
the arithmetic mechanism that a polynomial-in-k coefficient cannot supply. So
base 3 is the structurally-indicated q-difference base (q ~ 3 / q ~ 1/3 in the
Ohtsuki–Habiro normalization), tested exactly over ℚ(√3). Control: the classical base `X=k` (reproduces the prior negative). Base
√3 is excluded — it introduces ℚ(√3) monomials that break the rational/√3
equation split; base 3 already clears the 3^{1.5k} denominators at E≥2.

## Method (exact, decisive, no fit)

Same genuine-ℚ(√3)-coupling kernel as PR #3737 (2 coupled scalar equations
sharing the A,B polynomials; the fix from @gemini-code-assist), with the monomial
basis `k^d` replaced by `(X^k)^d = X^{k d}`. Exact rational null space — no
floats, no PSLQ, no fit, no free base. A nontrivial kernel is a genuine exact
q-holonomic recurrence (⇒ a closed-form q-difference characterization of D(ũ),
to be formalized); an empty kernel across the principled bases tightens the
"D-ladder is genuinely resurgent / non-(q-)holonomic at accessible order"
reading further.

Discipline: scope-(a); no c_k wired; registry untouched; no tier change.
Adjacent sibling PR #3683 (Borel resurgence on the κ-tower) — distinct object.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402

ORD = int(sys.argv[1]) if len(sys.argv) > 1 else 43
core.ORD = ORD
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402
dlad.ORD = ORD


def exact_ab():
    dk, KMAX, _vt, _ok = dlad.build_d_ladder()
    s3 = sp.sqrt(3)
    ab = {}
    for k in range(1, KMAX + 1):
        e = sp.expand(dk[k])
        b = sp.nsimplify(e.coeff(s3, 1))
        a = sp.nsimplify(e - b * s3)
        assert a.is_rational and b.is_rational, (k, a, b)
        ab[k] = (sp.Rational(a), sp.Rational(b))
    return ab, KMAX


# Modular rank: a NEGATIVE (trivial nullspace) is rigorous via full column rank
# mod a prime — full rank mod p ⟹ full rank over ℚ ⟹ trivial ℚ-nullspace. Huge
# 3^{k d} entries are reduced mod p first, so the linear algebra stays cheap.
# Primes chosen large and coprime to 3/2/√3-norms.
_PRIMES = (2_147_483_647, 2_147_483_629, 999_999_937)


def _rat_mod(x, p):
    """A sympy Rational (or Integer) reduced into GF(p)."""
    x = sp.Rational(x)
    num = int(x.p) % p
    den = int(x.q) % p
    return (num * pow(den, p - 2, p)) % p


def _col_rank_mod(rows_mod, n, p):
    """Column rank of an (m × n) matrix over GF(p) by Gaussian elimination."""
    M = [row[:] for row in rows_mod]
    rank = 0
    pivot_row = 0
    for col in range(n):
        piv = None
        for rr in range(pivot_row, len(M)):
            if M[rr][col] % p != 0:
                piv = rr
                break
        if piv is None:
            continue
        M[pivot_row], M[piv] = M[piv], M[pivot_row]
        inv = pow(M[pivot_row][col], p - 2, p)
        prow = [(v * inv) % p for v in M[pivot_row]]
        M[pivot_row] = prow
        for rr in range(len(M)):
            if rr != pivot_row and M[rr][col] % p != 0:
                f = M[rr][col]
                M[rr] = [(M[rr][c] - f * prow[c]) % p for c in range(n)]
        rank += 1
        pivot_row += 1
        if rank == n:
            break
    return rank


def _build_rows(ab, KMAX, r, E, base):
    """Constraint rows (rational) for the genuine-ℚ(√3)-coupled recurrence with
    monomial basis X^{k d} (base=None ⇒ classical k^d). 2·(r+1)·(E+1) unknowns."""
    n_half = (r + 1) * (E + 1)
    n = 2 * n_half
    rows = []
    for k in range(r + 1, KMAX + 1):
        Xk = sp.nsimplify(base ** k) if base is not None else None
        eq1 = [sp.Integer(0)] * n
        eq2 = [sp.Integer(0)] * n
        for i in range(r + 1):
            a_ki, b_ki = ab[k - i]
            for d in range(E + 1):
                idx_A = i * (E + 1) + d
                idx_B = n_half + idx_A
                mon = (Xk ** d) if base is not None else (sp.Integer(k) ** d)
                eq1[idx_A] += a_ki * mon
                eq1[idx_B] += 3 * b_ki * mon
                eq2[idx_A] += b_ki * mon
                eq2[idx_B] += a_ki * mon
        rows.append(eq1)
        rows.append(eq2)
    return rows, n


def q_holonomic_kernel(ab, KMAX, r, E, base):
    """Return (has_nontrivial_kernel, n_unknowns, n_rows). NEGATIVE is decided
    rigorously by full column rank mod a large prime; a rank deficiency mod all
    primes triggers an EXACT sympy re-verification (so a reported positive is
    exact, and a reported negative is prime-certified)."""
    rows, n = _build_rows(ab, KMAX, r, E, base)
    nrow = len(rows)
    full_rank_somewhere = False
    for p in _PRIMES:
        rows_mod = [[_rat_mod(v, p) for v in row] for row in rows]
        if _col_rank_mod(rows_mod, n, p) == n:
            full_rank_somewhere = True
            break
    if full_rank_somewhere:
        return False, n, nrow            # certified trivial nullspace
    # Deficient mod every prime → re-verify exactly (rare; expected only on a
    # genuine recurrence).
    ns = sp.Matrix(rows).nullspace()
    return (len(ns) > 0), n, nrow


def main() -> int:
    print("=" * 78)
    print(" D-ladder q-holonomic recurrence — exact test in the 3-adic base")
    print("=" * 78)
    ab, KMAX = exact_ab()
    print(f"  exact d_k: k=1..{KMAX} (ORD {ORD})")
    # Principled bases give RATIONAL monomials 3^{k d} (base √3 would introduce
    # ℚ(√3) monomials that break the rational/√3 equation split; and 3 already
    # clears the 3^{1.5k} denominators at E≥2, so it is the right base). 1/3 =
    # the reciprocal (Ohtsuki–Habiro q↔q⁻¹) direction; k = the classical control.
    bases = [("3", sp.Integer(3)), ("1/3", sp.Rational(1, 3)),
             ("k-classical", None)]

    wb = WitnessBuilder("qbeta-dladder-q-holonomic-base3", engine="sympy")
    wb.set_description(
        "Exact q-holonomic (q-difference) recurrence test for the bar-odd "
        "D-ladder d_k=a_k+b_k√3, base fixed by the observed 3-power denominators "
        "(v_3(den d_k)~1.5k). Coefficients polynomial in X^k (X=3 principal, 1/3 reciprocal, "
        "classical k control), genuine ℚ(√3) coupling, exact rational "
        "null space (no floats/PSLQ/fit). A nontrivial kernel = an exact "
        "q-difference closed form for D(ũ); empty across bases tightens the "
        "resurgent/non-q-holonomic reading. Follows PR #3737 (coupled-recurrence "
        "negative) + #3716; sibling #3683 does κ-tower Borel (distinct object). "
        "Scope-(a); nothing wired."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    any_found = False
    results = {}
    for bname, bval in bases:
        found_here = None
        cells = 0
        for r in range(1, 4):
            for E in range(0, 4):
                n_unk = 2 * (r + 1) * (E + 1)
                n_eq = 2 * (KMAX - r)
                if n_eq < n_unk + 4:
                    continue
                cells += 1
                has_ker, n, nrow = q_holonomic_kernel(ab, KMAX, r, E, bval)
                if has_ker:
                    found_here = (r, E)
                    any_found = True
                    print(f"  base {bname:12s} (r={r},E={E}): *** NONTRIVIAL "
                          f"KERNEL *** ({nrow} eqs, {n} unk) — candidate recurrence!")
                    # re-extract exact kernel for the witness
                    rows, _n = _build_rows(ab, KMAX, r, E, bval)
                    ns = sp.Matrix(rows).nullspace()
                    wb.add_data(f"kernel_{bname}_r{r}_E{E}",
                                [str(v.T) for v in ns[:2]])
                    break
            if found_here:
                break
        if not found_here:
            print(f"  base {bname:12s}: full column rank (prime-certified) across "
                  f"{cells} cells (r≤3, E≤3) — NO q-holonomic recurrence")
        results[bname] = (f"FOUND {found_here}" if found_here
                          else "none (r≤3,E≤3, prime-certified full rank)")

    wb.add_data("KMAX", KMAX)
    wb.add_data("ORD", ORD)
    wb.add_data("bases_tested", {b: results[b] for b, _ in bases})
    verdict = ("q-holonomic recurrence FOUND" if any_found
               else "NO q-holonomic recurrence in base {3,1/3} (+ classical k) up to (r≤3,E≤3)")
    wb.add_data("verdict", verdict)
    wb.add_assertion(
        "q_holonomic_base3_recurrence_absent",
        computed=(0.0 if any_found else 1.0), expected=1.0, tolerance=0.5,
        source="exact null space trivial for the 3-adic-principled bases "
               "{3, 1/3} (and classical k) through (r≤3,E≤3) ⇒ D(ũ) is not "
               "q-holonomic at accessible order in the structurally-indicated base")
    print(f"\n  VERDICT: {verdict}")
    wb.save()
    return 0




if __name__ == "__main__":
    raise SystemExit(main())
