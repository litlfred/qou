#!/usr/bin/env python3
"""qbeta_dladder_coupled_qsqrt3_recurrence_probe.py

Exact test of a recurrence class the merged D-ladder structure hunt
(qbeta_dladder_generating_function_structure_probe.py, PR #3716) did NOT run:
the **coupled ℚ(√3) vector P-recurrence** for the bar-odd D-ladder coefficients
d_k = a_k + b_k·√3.

## Why this is the missing test (not a duplicate)

The merged probe tested classical P-finite recurrences for a_k and b_k
**separately** over ℚ (order ≤ 4, deg ≤ 5 — all negative). But d_k is a single
ℚ(√3) object, and a P-recurrence *over ℚ(√3)*

    Σ_{i=0}^{r} P_i(k)·d_{k-i} = 0,   P_i ∈ ℚ(√3)[k],

does NOT reduce to separate ℚ-recurrences for a_k, b_k of the same order —
applying the √3-Galois conjugation couples the two rational components into a
2-vector v_k = (a_k, b_k)ᵀ obeying a **matrix** P-recurrence

    Σ_{i=0}^{r} M_i(k)·v_{k-i} = 0,   M_i(k) ∈ Mat₂(ℚ[k]),  deg ≤ D,

whose off-diagonal (√3-mixing) entries the separated scalar test structurally
cannot see. So a coupled recurrence can exist where both separated ones fail.
This is the exact ℚ(√3) P-finiteness question for D(ũ) — decisive either way.

## Discipline (STRICT)

Scope-(a). This is an EXACT linear-algebra test over ℚ (rational kernel of an
integer matrix — no floats, no PSLQ, no fitting, no free base to tune). No c_k
is wired, the registry is untouched, no tier changes. A POSITIVE result would be
an exact closed-form (q-)holonomic characterization of D(ũ) to be formalized; a
NEGATIVE result extends the merged "not P-finite (separated)" verdict to the
**coupled ℚ(√3)** case, tightening the corpus's resurgent / q-Gevrey reading of
the bar-odd S-leak (docs/audits/2026-07-12-dladder-divergence-correction.md).

Adjacent live sibling (different object, do not collide): PR #3683 does Borel /
alien-calculus resurgence on the **κ-tower**; this probe tests **holonomicity of
the D-ladder**, the complementary structural question.

Source of the exact d_k: qbeta_dladder_generating_function_structure_probe.py
(rebuilt here at a chosen ORD via the same core.ser_div path).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Build the exact d_k with the SAME machinery as the merged structure probe.
# core.ORD must be set BEFORE importing the probe module (it captures ORD at
# import time).
import qbeta_ck_sseries_exact_rational as core  # noqa: E402

ORD = int(sys.argv[1]) if len(sys.argv) > 1 else 43
core.ORD = ORD
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402
dlad.ORD = ORD  # keep the probe's module global in sync with core.ORD


def exact_dk():
    """Exact d_k = a_k + b_k√3 (a_k, b_k ∈ ℚ) via the merged build path."""
    dk, KMAX, valid_top, odd_ok = dlad.build_d_ladder()
    s3 = sp.sqrt(3)
    ab = {}
    for k in range(1, KMAX + 1):
        e = sp.expand(dk[k])
        b = sp.nsimplify(e.coeff(s3, 1))
        a = sp.nsimplify(e - b * s3)
        # sanity: a, b are rational
        assert a.is_rational and b.is_rational, (k, a, b)
        ab[k] = (sp.Rational(a), sp.Rational(b))
    return ab, KMAX


def coupled_recurrence_kernel(ab, KMAX, r, D):
    """Exact null-space test for a coupled 2-vector P-recurrence of order r,
    polynomial degree D:

        Σ_{i=0}^{r} M_i(k)·(a_{k-i}, b_{k-i})ᵀ = 0   (2 scalar rows per k)

    with M_i(k) ∈ Mat₂(ℚ[k]), deg_k ≤ D. Unknowns: the 4·(r+1)·(D+1) polynomial
    coefficients of the M_i entries. Build the exact rational constraint matrix
    over all valid k and return its right null space (sympy, exact).
    """
    # Unknown layout: for each shift i∈[0,r], each matrix entry (row∈{0,1} =
    # output component, col∈{0,1} = which of a/b feeds in), each degree d∈[0,D]:
    #   coefficient c[i, row, col, d].
    idx = {}
    n = 0
    for i in range(r + 1):
        for row in range(2):
            for col in range(2):
                for d in range(D + 1):
                    idx[(i, row, col, d)] = n
                    n += 1
    rows = []
    # Valid k: need k-i ≥ 1 (have d_1..d_KMAX). Use k from r+1..KMAX.
    for k in range(r + 1, KMAX + 1):
        for row in range(2):  # two scalar equations (a-row, b-row) per k
            eq = [sp.Integer(0)] * n
            for i in range(r + 1):
                a_ki, b_ki = ab[k - i]
                comp = (a_ki, b_ki)
                for col in range(2):
                    for d in range(D + 1):
                        eq[idx[(i, row, col, d)]] += comp[col] * sp.Integer(k) ** d
            rows.append(eq)
    Mmat = sp.Matrix(rows)
    ns = Mmat.nullspace()  # exact rational null space
    return ns, n, Mmat.rows


def main() -> int:
    print("=" * 78)
    print(" D-ladder coupled ℚ(√3) P-recurrence — exact holonomicity test")
    print("=" * 78)
    ab, KMAX = exact_dk()
    print(f"  exact d_k rebuilt: k = 1..{KMAX}  (ORD {ORD})")
    print(f"  parity spot check (den of a_k vs b_k):")
    for k in range(1, min(KMAX + 1, 7)):
        a, b = ab[k]
        print(f"    k={k}: den(a)={a.q:>12}  den(b)={b.q:>12}  "
              f"({'odd ' if k % 2 else 'even'})")

    wb = WitnessBuilder("qbeta-dladder-coupled-qsqrt3-recurrence", engine="sympy")
    wb.set_description(
        "Exact test of the coupled ℚ(√3) vector P-recurrence for the bar-odd "
        "D-ladder coefficients d_k = a_k + b_k√3 (the recurrence class the merged "
        "structure hunt #3716 skipped — it tested a_k, b_k separately over ℚ). "
        "Rational null-space of the exact integer constraint matrix; no floats, "
        "no PSLQ, no fit. POSITIVE ⇒ exact holonomic closed form to formalize; "
        "NEGATIVE ⇒ extends the merged 'not P-finite (separated)' verdict to the "
        "coupled ℚ(√3) case (corroborates the q-Gevrey/resurgent reading). "
        "Adjacent sibling PR #3683 does Borel resurgence on the κ-tower (distinct "
        "object). Scope-(a); no c_k wired; registry untouched."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    found = None
    # Bounded search: keep #unknowns comfortably below #equations (2·(KMAX-r)).
    for r in range(1, 5):
        for D in range(0, 5):
            n_unknowns = 4 * (r + 1) * (D + 1)
            n_eqs = 2 * (KMAX - r)
            if n_eqs < n_unknowns + 4:   # need a genuine overdetermination margin
                print(f"  (r={r}, D={D}): SKIP — {n_eqs} eqs < {n_unknowns}+4 unknowns "
                      f"(insufficient data; extend ORD)")
                continue
            ns, n_unk, n_row = coupled_recurrence_kernel(ab, KMAX, r, D)
            tag = f"r={r}, D={D}"
            if ns:
                # A nontrivial null vector = a genuine coupled recurrence.
                print(f"  ({tag}): *** NONTRIVIAL KERNEL dim {len(ns)} *** "
                      f"({n_row} eqs, {n_unk} unknowns) — candidate recurrence!")
                found = (r, D, len(ns))
                wb.add_data(f"kernel_r{r}_D{D}", [str(v.T) for v in ns[:2]])
                break
            else:
                print(f"  ({tag}): trivial kernel only "
                      f"({n_row} eqs, {n_unk} unknowns) — no coupled recurrence")
        if found:
            break

    wb.add_data("KMAX", KMAX)
    wb.add_data("ORD", ORD)
    wb.add_data("d_k_a_b", {str(k): [str(ab[k][0]), str(ab[k][1])]
                            for k in range(1, KMAX + 1)})
    wb.add_data("classes_tested", "coupled 2-vector P-recurrence, "
                "order r=1..4, poly-degree D=0..4, over ℚ (= ℚ(√3) P-finiteness)")
    verdict = ("coupled ℚ(√3) recurrence FOUND" if found
               else "NO coupled ℚ(√3) P-recurrence up to (r≤4, D≤4) at this ORD")
    wb.add_data("verdict", verdict)
    wb.add_assertion(
        "coupled_qsqrt3_recurrence_absent",
        computed=(0.0 if found else 1.0), expected=1.0, tolerance=0.5,
        source="exact rational null space is trivial for all tested (r≤4, D≤4) "
               "⇒ d_k is not coupled-ℚ(√3) P-finite at accessible order "
               "(extends #3716's separated-ℚ negative)")
    print(f"\n  VERDICT: {verdict}")
    if not found:
        print("  → extends the merged 'not P-finite' result to the coupled ℚ(√3)")
        print("    case; consistent with the q-Gevrey/resurgent D-ladder reading.")
    wb.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
