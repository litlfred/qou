#!/usr/bin/env python3


# polynomial_q_not_applicable: numerical Hoefsmit characters at
# q = q_0; the Wenzl branching identity is checked numerically, not
# as a q-polynomial identity.
"""ρ_K LO piece: Wenzl 1988 Markov-multiplicativity / branching identity.

Emits `rho-k-markov-multiplicativity.witness.json` for
`prop:rho-k-graded-expansion` (LO piece).

The LO piece of the graded ρ_K expansion is proved categorically by
[Wenzl 1988] Theorem 5 (Markov multiplicativity for parabolic
subalgebras). For disjoint braids β_1 ∈ H_{n_1}(q) and β_2 ∈
H_{n_2}(q) embedded as β_1 ⊗ β_2 ∈ H_{n_1+n_2}(q):

    tr_M(β_1 ⊗ β_2) = tr_M(β_1) · tr_M(β_2).

Equivalently, at the Hecke-character level, the Wenzl branching
identity holds:

    χ^λ(β_1 ⊗ β_2) = Σ_{(μ,ν)} c^λ_{μ,ν} · χ^μ(β_1) · χ^ν(β_2)

with c^λ_{μ,ν} the Littlewood–Richardson coefficients.

This probe verifies the branching identity for the deuteron case
H_6 ↓ H_3 × H_3 (β_p ⊗ β_n, no inter-nucleon interface) at the
substrate parameter q_0, across all λ ⊢ 6. The maximum relative
deviation is **3.02e-70** at `_precision.COMPUTE_DPS` (70), confirming
the LO piece is a theorem, not an empirical ansatz.

This read "at machine precision (~10⁻¹⁴)" until 2026-09-14, and that
figure described the ARITHMETIC rather than the identity: the probe
called `char_fast.chi_lambda_fast`, which builds its σ_i matrices with
`dtype=complex` and multiplies them with numpy, so complex128 was the
floor whatever `q_val` it was handed. Moving to the mpmath sibling
`chi_lambda_fast_mp` (which `char_fast` has carried all along) and the
50-digit pin `Q_MP` drops the residue 56 orders. Nothing about the
mathematics changed; the verification simply stopped being limited by
the way it was computed. Re-measure rather than quoting this
paragraph — the witness's own `max_relative_deviation` is the figure.

It also confirms the trace-level multiplicativity
tr_M(β_p ⊗ β_n) = tr_M(β_p)·tr_M(β_n) by summing y_λ·χ^λ on the H_6
side and comparing to the product of the H_3 traces.

Reuses the verified LR table + character machinery from
`sublemma_2_1_deuteron_branching.py`.

Cited residual (`prop:rho-k-graded-expansion`): the content block
`content/quantum-observable-universe/mass-theory/rho-k-graded-expansion.md`
line 43 cites "machine precision (3.2 × 10⁻¹⁴)". As of 2026-09-14 that
UNDERSTATES this probe by 56 orders. The block was deliberately NOT
edited alongside this producer — it belongs to the mass-endomorphism
arc, and rewriting another arc's published figure is an owner call, not
a side effect of a float64 drain (bean `qou-840k`). Anyone quoting the
verification figure should take it from the witness.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps, fmt, OUTPUT_DPS  # noqa: E402 — dps must rise before module constants
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from mpmath import mp, mpf
# `chi_lambda_fast_mp`, NOT `chi_lambda_fast`.  The double-precision entry point
# builds its σ_i matrices with `dtype=complex` and multiplies them with numpy, so
# EVERY character in this probe was computed in complex128 no matter what `q_val`
# was handed to it — which is why the branching residue read ~1e-14 and the
# description called that "machine precision".  `char_fast` has carried an mpmath
# sibling all along (`chi_lambda_fast_mp`, `precision="mpmath50"` lambdify), and
# it is a drop-in taking an `mpf`.  ~10x slower; the H₆ Specht dims here are ≤ 16
# so the whole probe still runs in seconds.
from char_fast import chi_lambda_fast_mp  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
# `Q_MP`, NOT `Q`.  `q_parameter.Q` is `float(_d["q"])`; feeding it to the mpmath
# path would lift the double's binary expansion and cap a 70-dps computation at
# ~17 digits — the laundering case, since `fmt` would then write ~45 further
# characters of binary64 tail.
from q_parameter import Q_MP  # noqa: E402
from sublemma_2_1_deuteron_branching import (  # noqa: E402
    disjoint_word_n3_n3,
    lr_coef,
    partitions_of,
)
from witness_base import WitnessBuilder  # noqa: E402

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# Near-zero tolerance for direct character values; module-level to avoid
# re-parsing the literal into an mpf on every loop iteration.
EPS = mpf("1e-12")


def main() -> int:
    w = WitnessBuilder(
        "rho-k-markov-multiplicativity",
        # `mpmath`, not `numpy`.  The engine field was correct for the
        # complex128 character path this probe used to take; it no longer does.
        engine="mpmath",
    )
    w.set_description(
        "ρ_K LO piece: numerical verification of the [Wenzl 1988] "
        "Markov-multiplicativity / branching identity χ^λ(β_p ⊗ β_n) = "
        "Σ c^λ_{μν} χ^μ(β_p) χ^ν(β_n) for the deuteron decomposition "
        "H_6 ↓ H_3 × H_3 at q_0, across all λ ⊢ 6.  Max relative deviation "
        "3.02e-70 at _precision.COMPUTE_DPS (70) — quote this witness's own "
        "max_relative_deviation, not a figure from prose.  This read "
        "'machine precision (~1e-14)' until 2026-09-14, and that number was a "
        "property of the ARITHMETIC, not of the identity: the probe took "
        "char_fast's double-precision path, whose sigma matrices are "
        "dtype=complex and whose products are numpy, so complex128 was the "
        "floor no matter how precise q_0 was.  Re-run on the mpmath path the "
        "residue falls 56 orders, which strengthens rather than changes the "
        "conclusion — the LO piece of prop:rho-k-graded-expansion is a theorem "
        "(Markov multiplicativity + free-constituent additivity), not an "
        "empirical ansatz.  NOTE for a reader comparing artifacts: "
        "rho-k-graded-expansion.md still cites 3.2e-14 as the verification "
        "figure, i.e. UNDERSTATES this probe by 56 orders; that block belongs "
        "to the mass-endomorphism arc and was deliberately not edited here.  "
        "Also confirms trace-level multiplicativity "
        "tr_M(β_p ⊗ β_n) = tr_M(β_p)·tr_M(β_n)."
    )
    w.set_content_block("prop:rho-k-graded-expansion")

    q_val = Q_MP

    # Per-nucleon H_3 words (no interface).
    beta_p = atom_braid_word_3A(1, 0, include_inter=False)
    beta_n = atom_braid_word_3A(0, 1, include_inter=False)
    # Disjoint composite on H_6.
    beta_pn = disjoint_word_n3_n3(beta_p, beta_n)

    parts_3 = partitions_of(3)
    parts_6 = partitions_of(6)

    # H_3 characters.
    chi_p = {mu: chi_lambda_fast_mp(mu, beta_p, q_val) for mu in parts_3}
    chi_n = {mu: chi_lambda_fast_mp(mu, beta_n, q_val) for mu in parts_3}

    # H_6 direct characters of the disjoint product.
    chi_disjoint = {
        lam: chi_lambda_fast_mp(lam, beta_pn, q_val) for lam in parts_6
    }

    # LR prediction Σ c^λ_{μν} χ^μ(β_p) χ^ν(β_n).
    per_lambda = []
    rel_diffs = []
    for lam in parts_6:
        # `mp.mpc(0)`, not `0 + 0j`: a complex128 accumulator would have thrown
        # away the mpmath characters on the first `+=`.
        s = mp.mpc(0)
        for mu in parts_3:
            for nu in parts_3:
                c = lr_coef(mu, nu, lam)
                if c == 0:
                    continue
                s += c * chi_p[mu] * chi_n[nu]
        direct = chi_disjoint[lam]
        abs_direct = abs(direct)
        abs_diff = abs(direct - s)
        if abs_direct < EPS:
            rel = abs_diff
        else:
            rel = abs_diff / abs_direct
        rel_diffs.append(rel)
        per_lambda.append({
            "lambda": list(lam),
            "chi_direct_re": direct.real,
            "chi_direct_im": direct.imag,
            "chi_lr_pred_re": s.real,
            "chi_lr_pred_im": s.imag,
            "rel_diff": rel,
        })
        print(f"  λ={str(lam):<14} direct={direct.real:+.8e}  "
              f"LR={s.real:+.8e}  rel_diff={rel:.2e}")

    max_rel = max(rel_diffs)
    print(f"\n  max relative deviation (branching identity) = {max_rel:.3e}")

    w.add_parameter("q_0", fmt(q_val))
    w.add_parameter("n_strands", 6)
    w.add_parameter("branching", "H_6 ↓ H_3 × H_3")
    w.add_parameter("case", "deuteron β_p ⊗ β_n (no interface)")
    w.add_data("partitions_of_6", [list(p) for p in parts_6])
    w.add_data(
        "per_lambda",
        [{k: (v if k == "lambda" else fmt(v)) for k, v in r.items()}
         for r in per_lambda],
    )
    w.add_data("max_relative_deviation", fmt(max_rel))
    w.add_data(
        "chi_proton_h3",
        {str(mu): {"re": fmt(chi_p[mu].real), "im": fmt(chi_p[mu].imag)}
         for mu in parts_3},
    )
    w.add_data(
        "chi_neutron_h3",
        {str(mu): {"re": fmt(chi_n[mu].real), "im": fmt(chi_n[mu].imag)}
         for mu in parts_3},
    )

    # Assertion: the branching identity holds at the ARITHMETIC FLOOR, which
    # under mpmath is ~56 orders below the complex128 floor this probe used to
    # report.  The old comment here read "the exact last digits fluctuate with
    # float rounding run-to-run" and justified a 1e-12 gate on that; with the
    # mpmath path there is no such fluctuation — mpmath is deterministic at fixed
    # dps and repeated runs agree byte-for-byte.
    #
    # The tolerance is derived from the SERIALIZATION ROUND-TRIP bound, not from
    # the observed residue (a bound sized to its own miss is a fit): the largest
    # character written to this witness is |χ^(4,1,1)| ≈ 2.813, and `fmt` writes
    # `_precision.OUTPUT_DPS` = 60 significant places, so a value read back out
    # of the JSON can differ from the computed one by ~2.8e-60.  Rounded down a
    # decade for headroom against an OUTPUT_DPS change: 1e-58.  The measurement
    # sits 12 orders inside that.
    w.add_assertion(
        name="wenzl_branching_identity_arithmetic_floor",
        computed=max_rel,
        expected=mpf("0.0"),
        tolerance=mpf("1e-58"),
        source=(
            "prop:rho-k-graded-expansion cites the Wenzl 1988 branching "
            "identity χ^λ(β_p ⊗ β_n) = Σ c^λ_{μν} χ^μ χ^ν for all λ ⊢ 6 in "
            "the deuteron case.  The block cites 3.2e-14, which is the "
            "COMPLEX128 floor of the old numpy character path and is a "
            "statement about the arithmetic, not about the identity.  This run "
            "takes the mpmath path at _precision.COMPUTE_DPS and gives max "
            "rel.dev. 3.02e-70 — recorded in this witness's own "
            "max_relative_deviation, which is the figure to quote.  Gate is the "
            "serialization round-trip bound (see comment), not the residue."
        ),
    )
    w.add_assertion(
        name="branching_verified_all_lambda_6",
        # The 1e-6 here is DELIBERATELY coarse and is NOT sized to the
        # measurement: it is a "did anything go structurally wrong" gate (a
        # wrong LR coefficient, a mis-embedded word, a dropped partition all
        # miss by O(1)), and it is left where it was when the arithmetic was
        # complex128 so a regression to that path would still trip it.  The
        # quantitative statement lives in the sibling assertion above; do not
        # tighten this one to 3e-70 or it stops testing what it tests.
        computed=1 if max_rel < mpf("1e-6") else 0,
        expected=1,
        tolerance=0,
        source="branching identity holds for all 11 partitions λ ⊢ 6",
    )

    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
