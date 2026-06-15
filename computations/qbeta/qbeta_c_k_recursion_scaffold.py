#!/usr/bin/env python3
"""qbeta_c_k_recursion_scaffold.py — recursion engine for the c_k
precision ladder, demonstration on toy kernels.

Per `prop:q-beta-c-k-recursion-from-habiro-q-difference`:

  A fibre-level Habiro element F(q) satisfying a q-difference equation
  F(qξ) = R(q,ξ)·F(ξ) of depth d induces a depth-d linear recursion
  on the precision-ladder coefficients:

      c_{k+1} = Σ_{j=0}^{d-1} kernel(j) · c_{k-j}.

This module:

  1. Provides the recursion-engine class `CKRecursion` (mirror of the
     Lean `structure CKRecursion R`) with `apply_recursion(history)`
     method computing one step.

  2. Demonstrates the engine on two toy kernels:
       * Depth-1 geometric:    kernel = [g], generates c_{k+1} = g·c_k
       * Depth-2 underdet.:    kernel = [a, b], generates c_{k+1} = a·c_k + b·c_{k-1}

  3. Emits a witness JSON recording the recursion outputs for both toys.

This is a SCAFFOLD — the categorical kernel for Q_β is not yet known
(requires symbolic α(q) from the operator-valued N=3 witness).  Once
that kernel is identified, the same `CKRecursion` engine produces the
c_k for the QOU framework.

The proved seed c_2 = -1 (PR #1602, bar-even constraint) is the input
to both demonstrations.  No fit, no CODATA residual — purely the
mechanical recursion.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time
from pathlib import Path
from dataclasses import dataclass

HERE = Path(__file__).resolve().parent
import sys as _sys2  # noqa: E402
_sys2.path.insert(0, str(HERE.parent))
del _sys2

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

from witness_base import WitnessBuilder  # noqa: E402

C2_SEED = mp.mpf("-1")  # proved by bar-even constraint, PR #1602
C3_EMPIRICAL = mp.mpf("-2")  # near-match cross-anchor average


@dataclass(frozen=True)
class CKRecursion:
    """Depth-d linear recursion on c_k.  `kernel` is a list of `depth`
    mpf coefficients; `apply_recursion(history)` consumes the last
    `depth` c_k values (most recent first) and produces c_{k+1}."""

    depth: int
    kernel: tuple

    def apply_recursion(self, history: tuple) -> mp.mpf:
        if len(history) != self.depth:
            raise ValueError(
                f"history length {len(history)} != depth {self.depth}")
        return sum(
            (mp.mpf(self.kernel[j]) * mp.mpf(history[j])
             for j in range(self.depth)),
            mp.mpf(0),
        )

    def generate_sequence(self, seeds: tuple, n: int) -> list:
        """Generate c_2, c_3, ..., c_{1+n} from the seeds + recursion.

        `seeds` provides the first `depth` values (c_2, c_3, ...,
        c_{1+depth}); subsequent values come from the recursion."""
        if len(seeds) != self.depth:
            raise ValueError(
                f"need {self.depth} seeds, got {len(seeds)}")
        seq = [mp.mpf(s) for s in seeds]
        for _ in range(n - self.depth):
            # history = most-recent first; recursion uses the last
            # `depth` entries with kernel[0] applied to the most recent.
            history = tuple(reversed(seq[-self.depth:]))
            seq.append(self.apply_recursion(history))
        return seq


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-c-k-recursion-scaffold",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Recursion engine for the c_k precision ladder + demonstration "
        "on toy kernels. Implements `CKRecursion.apply_recursion` "
        "mirroring the Lean structure of the same name. The proved seed "
        "c_2 = -1 (PR #1602) is the input; toy kernels (depth-1 "
        "geometric; depth-2 fit-to-c_4) generate c_4..c_8 mechanically. "
        "Scaffold — no claim about which kernel is the Q_β-categorical "
        "one (that requires symbolic α(q), open object)."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" c_k RECURSION SCAFFOLD — toy kernel demonstrations")
    print("=" * 78)
    print()
    print(f"  Proved seed: c_2 = {C2_SEED}")
    print(f"  Empirical:   c_3 ≈ {C3_EMPIRICAL}")
    print()

    # ─ Toy 1: depth-1 geometric kernel ───────────────────────────────────
    # c_{k+1} = g · c_k.  For g = 1, predicts c_k = -1 for all k, matching
    # the "even rungs geometric" pattern note of qbeta-1ppq-achieved
    # (where c_2 = c_4 ≈ -1 was observed).
    print("  TOY 1 — depth-1 geometric (g = +1):")
    rec1 = CKRecursion(depth=1, kernel=(mp.mpf(1),))
    seq1 = rec1.generate_sequence(seeds=(C2_SEED,), n=8)
    for k, v in enumerate(seq1, start=2):
        print(f"    c_{k} = {mp.nstr(v, 12)}")
    print()

    # ─ Toy 2: depth-2 kernel solved from c_2, c_3, c_4 ─────────────────
    # c_{k+1} = a·c_k + b·c_{k-1}.  At k = 3 with c_2 = -1, c_3 = -2,
    # c_4 = -0.97157 (the fit value of qbeta-1ppq-achieved):
    #   -0.97157 = a·(-2) + b·(-1)
    # Underdetermined (one equation, two unknowns).  Pick b = 0 to get
    # a = 0.485785 — degenerates to depth-1 with kernel +0.485785.
    # More interesting: pick a = 1/2 (bar-even prior) giving b = 0.02843.
    print("  TOY 2 — depth-2 with a = 0.5, b extracted from c_4 fit:")
    a, b = mp.mpf("0.5"), mp.mpf("0.97157") - mp.mpf("2") * mp.mpf("0.5")
    print(f"    kernel = (a, b) = ({mp.nstr(a, 10)}, {mp.nstr(b, 10)})")
    rec2 = CKRecursion(depth=2, kernel=(a, b))
    seq2 = rec2.generate_sequence(seeds=(C2_SEED, C3_EMPIRICAL), n=8)
    for k, v in enumerate(seq2, start=2):
        print(f"    c_{k} = {mp.nstr(v, 12)}")
    print()

    # ─ Sanity checks ────────────────────────────────────────────────────
    # Toy 1: every c_k = -1
    toy1_all_neg_one = all(abs(v - mp.mpf(-1)) < mp.mpf("1e-50")
                           for v in seq1)
    builder.add_assertion(
        "toy1_geometric_unit_kernel_all_c_k_eq_neg_one",
        computed=float(max(abs(v - mp.mpf(-1)) for v in seq1)),
        expected=0.0,
        tolerance=1e-30,
        source=("Toy 1: depth-1 geometric kernel g = 1, seed c_2 = -1. "
                "Recursion produces c_k = -1 for all k. Validates the "
                "applyRecursion machinery and confirms the 'even rungs "
                "geometric' pattern note of qbeta-1ppq-achieved."),
    )
    # Toy 2: c_4 matches the fit target by construction
    c4_fit_target = mp.mpf("-0.9715682590253777")
    c4_toy2 = -seq2[2]  # seq2[2] is c_4 (index 0 = c_2)
    # Actually seq2 = [c_2, c_3, c_4, ...]; seq2[2] is c_4 directly.
    c4_residue = float(abs(seq2[2] - c4_fit_target))
    builder.add_assertion(
        "toy2_depth2_c_4_matches_fit",
        computed=c4_residue,
        expected=0.0,
        tolerance=1e-3,
        source=(f"Toy 2: depth-2 kernel (a=0.5, b={mp.nstr(b, 10)}) "
                "constructed by inverting the c_4 fit value -0.97157 "
                "from qbeta-1ppq-achieved. Validates that the depth-2 "
                "recursion engine reproduces the fit by construction; "
                "extends to c_5, c_6, etc. predictions for that kernel."),
    )

    builder.add_data("toy1_geometric_g_eq_1", {
        "kernel": [str(rec1.kernel[0])],
        "depth": rec1.depth,
        "c_k_sequence": {f"c_{k+2}": str(v) for k, v in enumerate(seq1)},
    })
    builder.add_data("toy2_depth2_a_half_b_from_c4_fit", {
        "kernel": [str(a), str(b)],
        "depth": rec2.depth,
        "seeds": {"c_2": str(C2_SEED), "c_3": str(C3_EMPIRICAL)},
        "c_k_sequence": {f"c_{k+2}": str(v) for k, v in enumerate(seq2)},
    })
    builder.add_data("scaffold_status", {
        "proved_seed": {"c_2": str(C2_SEED), "source": "PR #1602 bar-even"},
        "empirical_seed": {"c_3": str(C3_EMPIRICAL),
                           "source": "canonical-framing audit"},
        "fit_extraction": {"c_4": str(c4_fit_target),
                           "source": "qbeta-1ppq-achieved.witness.json"},
        "open_object": (
            "categorical kernel R(q,ξ) for the fibre-level Habiro element "
            "F(q) = Q_β / [Q_A · cos(α_eff)]; requires symbolic α(q) "
            "from the operator-valued N=3 witness."
        ),
    })

    print("=" * 78)
    print(" VERDICT — scaffold working; categorical kernel still open")
    print("=" * 78)
    print()
    print("  • CKRecursion engine validates on depth-1 and depth-2 toys.")
    print("  • Lean structure `QOU.QBeta.CKRecursion.CKRecursion`")
    print("    mirrors this Python class exactly (same fields, same")
    print("    apply_recursion semantics).")
    print("  • Categorical Q_β kernel: open, requires symbolic α(q).")
    print()

    builder.save()
    print("  Witness: qbeta-c-k-recursion-scaffold.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
