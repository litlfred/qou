#!/usr/bin/env python3
"""saddle_offset_zero_location_probe.py — where does the 5₂ saddle-offset
zero-crossing actually sit, and does it mean anything?

Follow-up to #4578 (`saddle_offset_fourone_fivetwo_probe.py`, bean qou-q86o).
That probe found the ι-odd offset o(q)=c⁺(q)−c⁻(q) of the certified 5₂ Stokes
data crosses zero at a *small finite* q≈0.08 within the convergent radius —
NOT at q=1 as the owner's saddle-vector picture asks. This probe answers three
honest, open-outcome questions, derive-then-check, NO fitting:

  Q1  WHAT is q≈0.08?  Is it truncation-stable (a genuine feature of the
      analytic offset) or a truncation artifact?  Is it a corpus/substrate
      quantity (q₀−1, ℏ_q, ℏ_q², a root of unity modulus, the series radius),
      or just the root of the DT expansion's own low-order coefficients?

  Q2  Is the "q=1" claim recoverable from CERTIFIED corpus Stokes data under a
      different (non-q→0-anchored) reading — or is it definitively the trivial
      bar-fixed-point vanishing, distinct from the DT datum?

  Q3  c_3-odd hook: can the offset magnitude even be evaluated at the substrate
      q₀≈1.1097, and if so does it relate to the bar-odd Q_β c_3 near-match?

LOCKED EXPECTATIONS (set BEFORE the compute — anti-fit; a miss is a valuable
honest negative, reported scope-(a)):

  E1  q*(N) := smallest positive real root of the order-N truncation o_N(q)
      CONVERGES as N grows (truncation-STABLE), because at q≈0.087 the q³⁺
      terms are O(10⁻²) — the root is dominated by the quadratic balance
      1 − 9q − 28q² = 0, whose root is q_quad = (−9+√193)/56 ≈ 0.0873.
      Predict |q*(18) − q_quad| < 0.01.  [If it DRIFTS → truncation artifact,
      honest negative on "q≈0.08 is a well-defined number" either way.]

  E2  q* is NOT within 1% of any substrate quantity — q₀−1≈0.1097,
      ℏ_q=1−1/q₀≈0.0990, ℏ_q²≈0.0098, 1/q₀≈0.9010, nor a clean root-of-unity
      modulus (all |ζ|=1).  Predict: NO corpus match; q* is set by the DT
      series' own coefficients {9,28} (which encode the {3,4} data), carrying
      no independent substrate meaning.  → honest negative on Q1.

  E3  o(q) CANNOT be evaluated at q₀ (q₀≈1.1097 ≫ the series radius R≈0.1, and
      q₀>1): the partial sums DIVERGE.  Predict: c_3 hook via direct q₀
      evaluation is INACCESSIBLE; no clean o↔c_3 relation.  → honest negative
      on Q3.  (Do NOT fit c_3 to any offset datum; wire nothing.)

  E4  The certified o(q)=c⁺(q)−c⁻(q) is a CROSS-CHIRALITY difference at the
      SAME q (leading term 1≠0), NOT a bar-covariant object f(q)−f(q⁻¹).  So
      its q=1 vanishing is NOT delivered by the bar-fixed-point argument.  The
      bar-fixed-point vanishing (every genuine bar-odd object → 0 at q=q⁻¹=1)
      is trivially true but is a DIFFERENT object from the DT {3,4} datum
      (which lives at q→0).  Predict: "origin-centred only at q=1" is
      recoverable ONLY as that trivial fixed-point vanishing — the DT offset is
      NOT placed at q=1 by any certified reading.  → Q2 refined-negative.

Reuses the certified sandwich UNCHANGED (K1/K2/K3 ✓); avoids every qou-fk19
red-flag (no v_offset ODE, no q=exp(2πiτ) pin, no invented θ-function). No fit,
no c_k wired, no axiomatization, nothing wired to any dashboard / Q_β ladder.
"""
from __future__ import annotations

import importlib.util
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_stokes_sandwich",
    _HERE / "qbeta_g3_5two_stokes_sandwich.py")
_sw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_sw)

ORD = 18

# STUB — analysis body lands in the next commit (probe scaffold for the DRAFT PR).
print("saddle_offset_zero_location_probe.py — scaffold; analysis body incoming.")
