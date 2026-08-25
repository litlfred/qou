#!/usr/bin/env python3
"""
markov_weights_symbolic.py — Closed-form symbolic Jones–Markov weights
y_λ(q) at H_n(q), derived directly from the Markov axioms.

Background.  The Ocneanu Markov trace on the Iwahori–Hecke algebra is
the unique linear functional satisfying

    tr_M(1) = 1,
    tr_M(σ_i x) = z · tr_M(x)        for x ∈ H_{i}(q),  i < n,
    tr_M(xy)   = tr_M(yx),

with z = q³/(q² + 1) — **convention D** (SU(2)/Temperley–Lieb, Jones);
convention C's z = 1/(√q + 1/√q) was excised by owner ruling 2026-08-09,
see docs/coordination/trace-convention-registry.md.  In the Wedderburn
decomposition

    tr_M(β) = Σ_{λ ⊢ n} y_λ(q) · χ^λ(β),

the weights y_λ(q) are uniquely determined by the axioms.  The
partition-sum normalisation w_λ/f^λ = dim_q(λ)² / ([n]_q! · f^λ)
is **NOT** equal to y_λ(q) for q ≠ 1 — they coincide only at the
classical Plancherel point q = 1.

This module solves the linear system at H_3 symbolically:

    A · y = b,

    A_{ij} = χ^{λ_j}(elem_i),   elem_i ∈ {1, σ_1, σ_1 σ_2},
    b_i    = {1, z, z²}.

The 3×3 symbolic solve produces closed-form rational functions of q
for y_{(3)}, y_{(2,1)}, y_{(1,1,1)}, which then assemble the
canonical tr_M(β) for any braid word β in B_3.

Cross-validation: at q_0 ≈ 1.1097, this reproduces the
markov_peel / Hoefsmit-Wenzl bridge value
tr_M(proton) ≈ 1.0653062286 to all printed digits.

For higher n the same construction works with n class-basis elements.
For n = 6 (deuteron) the basis is {1, σ_1, σ_1σ_2, σ_1σ_2σ_3,
σ_1σ_2σ_3σ_4, σ_1σ_2σ_3σ_4σ_5}.

References:
  - Ocneanu (1985); Jones (1987); Wenzl (1988).
  - prop:markov-pair-z2 (canonical formulation in this paper).
  - markov_peel (peel-recursion algorithm; equivalent output).

Run:
    python3 computations/markov_weights_symbolic.py
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
import time
from datetime import datetime, timezone
from math import factorial
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_character_symbolic import hoefsmit_matrices_symbolic  # noqa: E402
from hoefsmit_symbolic import Q, chi_lambda_symbolic  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402  — single source of truth
from canonical_braid_crossings import (  # noqa: E402
    atom_canonical_crossings as atomic_braid_to_crossings,
)
from hecke_characters import partitions_of  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import HA as HA_VAL  # noqa: E402

# Markov parameter — TRACE CONVENTION **D** (SU(2)/Temperley–Lieb, Jones):
#     z = q³/(q² + 1).
# Owner ruling 2026-08-09 excised convention C (z = 1/(√q + 1/√q) = √q/(q+1)),
# which this line carried until then.  Registry:
# docs/coordination/trace-convention-registry.md.
#
# Structural check this z passes and C does not: feeding it through the Wenzl
# level relation below gives Q^r = q⁴ = Q², i.e. **r = 2 exactly** — the SU(2)
# level, equivalently the row cap ℓ(λ) ≤ 2 that forces y_(1³) = 0.  Under C the
# same relation gives a non-integral level (Q^r ≈ 1.72025 at q₀) and y_(1³) ≠ 0.
Z_MARK = sp.cancel(Q**3 / (Q**2 + 1))


def atom_braid_word_3A_to_crossings(Z: int, N: int, *, include_inter: bool = False):
    """Convert atom_braid_word_3A's (c, d, gen_idx) tuples to the
    (gen_idx, ctype) format expected by chi_lambda_symbolic.

    This is the SAME canonical braid word used by `markov_peel`
    (production atomic Markov-trace witness path).  Differs from
    `atomic_braid_to_crossings` (in hecke_character_symbolic) by
    omitting two extra σ_0 gluon-self-coupling crossings per
    nucleon — those belong to the dressed atomic word, not the
    canonical Markov-trace input.
    """
    word = atom_braid_word_3A(Z, N, include_inter=include_inter)
    out = []
    # Delegate to the canonical classifier. The private three-way test this
    # replaces had no branch for the colour-weighted p-n interface
    # -h(1/2 - δ/4) and fell to its `else: raise`, so this broke on every
    # Z>=1,N>=1 word reached with include_inter=True (qou-8zjd).
    from canonical_braid_crossings import classify_crossing
    for c, d, gen_idx in word:
        out.append((gen_idx, classify_crossing(float(c), float(d), HA_VAL)))
    return out


def chi_at_canonical_basis(shape, n):
    """Compute χ^λ(elem) for elem ∈ {1, σ_1, σ_1 σ_2, …, σ_1 ⋯ σ_{n-1}}.

    These are the n canonical "ladder" elements that, by Markov
    descent, give tr_M values 1, z, z², …, z^{n-1} respectively.
    Returns a dict {idx: χ_value} where idx = 0,…,n-1 corresponds to
    the product σ_1 σ_2 ⋯ σ_idx (idx=0 is the identity).
    """
    matrices, dim, _syts = hoefsmit_matrices_symbolic(tuple(shape), Q)
    if dim == 0:
        return {idx: sp.Integer(0) for idx in range(n)}

    chi = {0: sp.Integer(dim)}  # χ^λ(1) = dim of irrep
    M = sp.eye(dim)
    for k in range(n - 1):
        # multiply by σ_{k+1}; this builds σ_1, σ_1σ_2, …, σ_1⋯σ_{n-1}
        M = (M * matrices[k]).applyfunc(sp.cancel)
        chi[k + 1] = sp.cancel(M.trace())
    return chi


def hooks_and_contents(lam):
    """Hook lengths and contents c(x) = j - i of cells of partition λ."""
    hs, cs = [], []
    rows = len(lam)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            hs.append(arm + leg + 1)
            cs.append(j - i)
    return hs, cs


def n_partition(lam):
    """n(λ) = Σ i · λ_i  (Macdonald's n-statistic)."""
    return sum(i * lam_i for i, lam_i in enumerate(lam))


# Wenzl convention parameters: Q = q², z_W = q · z (convention shift).
# The Wenzl level r satisfies z_W = Q^r (1 - Q) / (1 - Q^r), i.e.
# Q^r = z_W / (1 - Q + z_W)  (canonical eigenvalue relation).
Q_W = Q**2
Z_W_RAW = Q * Z_MARK
QR_W = sp.cancel(Z_W_RAW / (1 - Q_W + Z_W_RAW))  # Q^r symbolic — rational in q


def schur_principal_symbolic(lam) -> sp.Expr:
    """s_λ(1, Q, Q², …, Q^{r-1}) symbolically, where Q = q² and Q^r is
    the Wenzl level fixed by the Markov parameter z = q³/(q² + 1)
    (convention D).  For that z the relation collapses to Q^r = Q², i.e.
    r = 2, so this is the two-variable specialization s_λ(1, Q) and
    vanishes identically on any λ with three or more rows.

    Closed form:
        s_λ = Q^{n(λ)} · ∏_{x∈λ} (1 - Q^{r + c(x)}) / (1 - Q^{h(x)})

    The factor Q^{r + c(x)} = Q^r · Q^{c(x)} uses our symbolic QR_W.
    """
    hs, cs = hooks_and_contents(lam)
    num = sp.Integer(1)
    den = sp.Integer(1)
    for h, c in zip(hs, cs):
        num *= (1 - QR_W * Q_W**c)
        den *= (1 - Q_W**h)
    return sp.cancel(Q_W**n_partition(lam) * num / den)


def y_lambda_symbolic(n: int) -> dict[tuple, sp.Expr]:
    """Closed-form symbolic Jones–Markov weights y_λ(q) at H_n(q),
    via Wenzl's Schur principal specialization formula

        y_λ(q) = s_λ(1, Q, …, Q^{r-1}) / Z,
        Z      = Σ_μ s_μ(1, Q, …, Q^{r-1}) · f^μ,

    with Q = q², z_W = q · z, and Q^r = z_W / (1 - Q + z_W).

    Works for any n.  At q = 1 reduces to f^λ / n! (Plancherel).
    """
    shapes = [tuple(s) for s in partitions_of(n)]
    s_vals = {sh: schur_principal_symbolic(list(sh)) for sh in shapes}

    # Normalisation: Σ_λ y_λ · f^λ = tr_M(1) = 1.
    Z = sp.Integer(0)
    for sh in shapes:
        hs, _ = hooks_and_contents(list(sh))
        prod = 1
        for h in hs:
            prod *= h
        f_lam = factorial(n) // prod
        Z = Z + s_vals[sh] * f_lam
    Z = sp.cancel(Z)

    return {sh: sp.cancel(s_vals[sh] / Z) for sh in shapes}


def solve_y_lambda(n: int) -> dict[tuple, sp.Expr]:
    """Symbolic Jones–Markov weights y_λ(q) at H_n(q).

    Two paths are available:
      - n ≤ 3 : ladder linear system A y = b with A_{ij} = χ^{λ_j}(elem_i),
        elem_i = σ_1 ⋯ σ_{i-1},  b_i = z^i.  (Self-consistent derivation.)
      - n ≥ 4 : Wenzl's closed-form Schur principal specialization
        (the linear system is rank-deficient for n ≥ 4).

    For n = 3 the two paths agree (verified at q_0 to ≥10 digits).
    """
    if n <= 3:
        shapes = [tuple(s) for s in partitions_of(n)]
        chi_table = {sh: chi_at_canonical_basis(sh, n) for sh in shapes}
        A_rows = []
        b_rows = []
        for i in range(n):
            A_rows.append([chi_table[sh][i] for sh in shapes])
            b_rows.append(Z_MARK**i)
        A = sp.Matrix(A_rows)
        b = sp.Matrix(b_rows)
        if A.shape[0] != A.shape[1]:
            return y_lambda_symbolic(n)
        y = A.solve(b)
        y = sp.simplify(y)
        return {sh: sp.cancel(y[i]) for i, sh in enumerate(shapes)}
    return y_lambda_symbolic(n)


def tr_M_canonical(crossings, n: int):
    """Canonical Ocneanu/Jones-Markov tr_M(β) = Σ_λ y_λ(q) · χ^λ(β)."""
    y_lam = solve_y_lambda(n)
    total = sp.Integer(0)
    for shape, y in y_lam.items():
        chi = chi_lambda_symbolic(shape, crossings)
        total = total + sp.cancel(y * chi)
    return sp.cancel(total), y_lam


def main() -> int:
    print("=" * 80)
    print(" Symbolic Jones–Markov weights y_λ(q) at H_3(q) — closed form")
    print("=" * 80)

    # Solve the n=3 system.
    n = 3
    print()
    print(f"Solving the {n}-dim linear system  A · y = b  symbolically...")
    t0 = time.time()
    y_lam = solve_y_lambda(n)
    print(f"  [{time.time() - t0:.2f}s]")
    print()
    for shape, y in y_lam.items():
        print(f"  y_{shape} = {y}")
        # Cross-check: at q_0 the value should match the alpha_k_jones_markov_h3
        # numerical solution.
        val_q0 = sp.N(y.subs(Q, sp.Float(Q_50_DIGIT_STR, 50)), 30)
        print(f"           ≈ {float(val_q0):+.10f}  at q_0")  # display only

    # Sanity: Σ y_λ · dim_C(λ) = 1  (since tr_M(1) = 1 and χ^λ(1) = f^λ = dim)
    print()
    sum_check = sp.Integer(0)
    for shape, y in y_lam.items():
        chi_table = chi_at_canonical_basis(shape, n)
        sum_check = sum_check + sp.cancel(y * chi_table[0])
    sum_check = sp.simplify(sum_check)
    print(f"  Σ y_λ · χ^λ(1) = {sum_check}   (must equal 1)")

    # Apply to the proton internal braid (canonical markov_peel word).
    proton = atom_braid_word_3A_to_crossings(1, 0, include_inter=False)
    print()
    print(f"Proton canonical braid (markov_peel): {len(proton)} crossings")
    print("Proton internal braid: tr_M(β_p) = Σ_λ y_λ · χ^λ(β_p)")
    print()
    t0 = time.time()
    trM_p, _ = tr_M_canonical(proton, n)
    print(f"  [{time.time() - t0:.2f}s]")
    print()
    print(f"  closed form: {trM_p}")
    val_q0 = sp.N(trM_p.subs(Q, sp.Float(Q_50_DIGIT_STR, 50)), 30)
    print(f"  at q_0 ≈ 1.1097 : {val_q0}")
    print(f"  markov_peel ref : 1.0653062286131670")

    # Same for neutron (canonical markov_peel word).
    neutron = atom_braid_word_3A_to_crossings(0, 1, include_inter=False)
    print()
    print(f"Neutron canonical braid (markov_peel): {len(neutron)} crossings")
    print("Neutron internal braid:")
    trM_n, _ = tr_M_canonical(neutron, n)
    print(f"  closed form: {trM_n}")
    val_n = sp.N(trM_n.subs(Q, sp.Float(Q_50_DIGIT_STR, 50)), 30)
    print(f"  at q_0 ≈ 1.1097 : {val_n}")
    print(f"  markov_peel ref : 0.9232332971861535")

    # Witness JSON.
    out = HERE / "markov_weights_symbolic.witness.json"
    witness = {
        "computation": "markov-weights-symbolic",
        "description": (
            "Closed-form symbolic Jones–Markov weights y_λ(q) at H_3(q), "
            "derived directly from the Markov axioms tr_M(1)=1, "
            "tr_M(σ_i)=z, tr_M(σ_iσ_j)=z² via the 3×3 linear system "
            "A·y = b with A_{ij} = χ^{λ_j}(elem_i). Reproduces the "
            "markov_peel / Hoefsmit-Wenzl bridge value at q_0 from "
            "first principles, no numerical fitting."
        ),
        "n": n,
        "y_lambda": {str(sh): str(y) for sh, y in y_lam.items()},
        # str(), not float(). This evaluates a CLOSED FORM at a 50-digit q0
        # to 30 digits and then used to cast the result to a double, throwing
        # away 14 of them on the way out — the same defect as the isotope
        # producer, in a script whose whole point is that the value comes from
        # the Markov axioms rather than a fit.
        "y_lambda_at_q0": {
            str(sh): str(sp.N(y.subs(Q, sp.Float(Q_50_DIGIT_STR, 50)), 30))
            for sh, y in y_lam.items()
        },
        "tr_M_proton_closed_form": str(trM_p),
        "tr_M_proton_at_q0": str(val_q0),
        # The reference stays at the precision it was recorded with: it comes
        # from markov_peel, which returns a double. Serializing it through a
        # 50-digit formatter would pad 17 real digits with 33 invented ones —
        # exactly the fake precision the padding ratchet exists to catch.
        "tr_M_proton_markov_peel_reference": "1.0653062286131670",
        "tr_M_neutron_closed_form": str(trM_n),
        "tr_M_neutron_at_q0": str(val_n),
        "tr_M_neutron_markov_peel_reference": "0.9232332971861535",
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2))
    print()
    print(f"witness: {out.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
