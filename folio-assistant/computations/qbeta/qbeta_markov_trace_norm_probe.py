"""qbeta_markov_trace_norm_probe — replace L2 with Markov-trace inner product.

PR #1739 landed the Step-1 closure showing that the 6 T_β NF coordinates
are q-rational SHAPE × ONE archimedean scalar S = Q_β(q₀)/E_0(q₀):

  x_i(q) = A_i(q) · S / ‖A(q)‖²

The L2 here is the Euclidean coordinate norm — basis-dependent.  This
probe replaces it with the categorical Markov-trace inner product

  ⟨X, Y⟩_τ := τ_M(X^† Y)                            (on H_n(q))

and asks the structural question:

  Does the SHAPE × S decomposition survive under that replacement?

The min-Markov-norm solution to the SDP is:

  x_M(q) = G(q)^{-1} · A(q) · S / (A(q)^T · G(q)^{-1} · A(q))

where G(q) := (τ_M(b_i^† b_j))_{i,j} is the q-rational Gram matrix of
the NF basis vectors under τ_M.  Since G(q), G(q)^{-1}, and A(q) are
all q-rational, the answer is structurally YES — both numerator
G^{-1}·A and denominator A^T·G^{-1}·A are q-rational.

The substantive question is:
  Does the Markov-trace SHAPE F_i^τ(q) := (G^{-1} A)_i / (A^T G^{-1} A)
  have a more Habiro-friendly w-Taylor expansion than the Euclidean
  SHAPE F_i(q) = A_i(q) / ‖A(q)‖²?

This is the natural follow-up to PR #1739's u↔w probe (which showed
that w gives sparse-dyadic structure on the A_{L_+} channel under L2).
If the Markov-trace replacement gives EVEN simpler Habiro-friendly
structure, the L2 SHAPE was a coordinate-system artifact, and the
Markov-trace SHAPE is the canonical answer.

Pipeline:
  1. Load symbolic NF basis vectors b_i (Hoefsmit seminormal,
     per qbeta_per_block_symbolic.py).
  2. Compute Gram matrix G(q) := (τ_M(b_i^† b_j))_{i,j} symbolically.
     τ_M = Σ_λ y_λ(q) · χ_λ — Wedderburn-block sum.
  3. Compute A(q) = (Σ_λ y_λ χ_λ(b_i))_i — already done in
     qbeta_symbolic_tbeta_min_l2.py.
  4. Solve x_M = G^{-1} A · S / (A^T G^{-1} A), keep symbolic.
  5. Sanity at q_0: compare x_M coords vs x_L2 coords from the
     existing witness.  They should differ at every channel (the
     point of the probe).
  6. Reparametrise both shapes to Taylor series in w = q - 1/q at
     q=1, compare leading coefficients.
  7. Emit witness with verdict.

References:
  - PR #1739 — Step 1 SHAPE × S closure under L2 (MERGED).
  - docs/audits/2026-06-03-qbeta-step1-symbolic-min-l2.md — caveats §1.
  - docs/audits (to be created) — Markov-trace replacement audit.
  - qbeta_symbolic_tbeta_min_l2.py — reused for A(q) and y_λ loader.
  - qbeta_per_block_symbolic.py — reused for σ_i Hoefsmit matrices.

Usage:
  python3 folio-assistant/computations/qbeta/qbeta_markov_trace_norm_probe.py

Emits: qbeta-markov-trace-norm-probe.witness.json  (≥3 assertions).

Status: SCAFFOLD — Step 1 only.  Steps 2-7 land on follow-up commits.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401


HERE = Path(__file__).resolve().parent


def main() -> None:
    print("=" * 78)
    print("Q_β Markov-trace inner product replacement of L2 (SCAFFOLD)")
    print("=" * 78)
    print()
    print("Status: scaffold only.  See module docstring for the planned")
    print("derivation.  Steps 1-7 will land on follow-up commits.")
    print()
    print("Next commit: Step 1 — Gram matrix G(q) symbolic computation.")


if __name__ == "__main__":
    main()
