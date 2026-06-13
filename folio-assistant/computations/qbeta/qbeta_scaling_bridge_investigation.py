#!/usr/bin/env python3
"""qbeta_scaling_bridge_investigation.py — is the c_k ladder a 'wrong
scaling' artifact? Can a closed-form scaling close Q_β with NO c_k?

CONTEXT (user question, 2026-05-31): "can we get all c_k wired to
production? are we using the right scaling?"

The Q_β prediction is a precision ladder:

    Q_β = Q_A · cos(α − b·ℏ_q²/2) · Π_{k≥2}(1 + c_k·u^k),   u = b·ℏ_q²

where Q_A = Form A = m_e·|q²−2q−1|·(q+1)/(2q³). The neutron-qvalue-
symbolic.md is explicit that Form A's +1677 ppm overshoot is a SCALING
error: "the derived E_0 = m_e/(q(q−1)) is the single-level (Planck-tick)
approximation, while the exact tower-summed E_0 would absorb the 0.17%."

So the c_k are the E_0-tower / scaling expansion. THE QUESTION: is there
a closed-form scaling that closes Q_β to compute precision WITHOUT the
q₀-dependent c_k ladder? If yes → all c_k are 'absorbed' (wired via the
closed form, Taylor-exact). If no → only c_2 wires and the rest is the
μ-p substrate floor.

This script:
  1. Lays out the residual ladder at canonical q₀ (Q_A → N=1 cos → c_2),
     attributing each correction.
  2. Tests the two canonical closed-form E_0 towers (geometric 1/(1−x),
     Li_2^q) — including DIRECTION (Q_β needs a NEGATIVE correction).
  3. Tests whether the N=1 cos eigenphase scaling alone closes Q_β.
  4. Reports which scaling, if any, is Taylor-exact at canonical q₀.

DISCIPLINE: the candidate scalings (cos eigenphase, geometric tower,
Li_2^q tower) are all canonical objects already in the framework
(prop:q-beta-categorical-precision-ladder, conj:alpha-k-categorical-
closure). Zero free parameters; each is evaluated, not fitted.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from codata_constants import Q_BETA_MEV  # noqa: E402
del _sys, _Path, _bridge

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402


def li2q_symmetric(z, q, terms=400):
    """Symmetric q-dilogarithm Li_2^q(z) = Σ_{n≥1} z^n/(n·[n]_q)."""
    total = mp.mpf(0)
    for n in range(1, terms + 1):
        qn = (q ** n - q ** (-n)) / (q - 1 / q)  # [n]_q
        total += z ** n / (n * qn)
    return total


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder("qbeta-scaling-bridge-investigation",
                             engine="python+mpmath", start_time=t0)
    builder.set_description(
        "Tests whether the Q_β c_k ladder is a 'wrong scaling' artifact: "
        "does a closed-form scaling (cos eigenphase, geometric E_0 tower, "
        "Li_2^q tower) close Q_β to compute precision at canonical q₀ with "
        "NO q₀-dependent c_k? Attributes the residual ladder and checks "
        "direction. Answers the user's 'all c_k wired / right scaling' "
        "question. Zero free parameters."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")

    q = mp.mpf(Q_50_DIGIT_STR)
    m_e = mp.mpf(M_E_MEV)
    Q_codata = Q_BETA_MEV

    # substrate quantities
    h = q - 1 / q
    hbar = (q - 1) / q
    hbar2 = hbar ** 2
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    b = mp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    alpha = (z - 1) * h / 2
    u = b * hbar2

    Q_A = m_e * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)

    def ppb(x):
        return (x / Q_codata - 1) * mp.mpf(10) ** 9

    print("=" * 78)
    print(" Q_β SCALING / 'all c_k' INVESTIGATION at canonical q₀")
    print("=" * 78)
    print(f"  q₀ = {mp.nstr(q, 18)}   (m_p-pin, canonical)")
    print(f"  Q_codata = {mp.nstr(Q_codata, 10)} MeV")
    print()

    # ── 1. residual ladder ───────────────────────────────────────────
    N1 = mp.cos(alpha - b * hbar2 / 2)
    Q_N1 = Q_A * N1
    Q_N2 = Q_N1 * (1 - u ** 2)               # c_2 = -1, Taylor-exact
    print("  RESIDUAL LADDER (each factor's effect):")
    print(f"    {'stage':<28}{'value (MeV)':>16}{'err vs CODATA':>18}")
    print(f"    {'Q_A (Form A)':<28}{mp.nstr(Q_A,12):>16}{mp.nstr(ppb(Q_A),8)+' ppb':>18}")
    print(f"    {'× cos(α−bℏ²/2)  [N=1]':<28}{mp.nstr(Q_N1,12):>16}{mp.nstr(ppb(Q_N1),8)+' ppb':>18}")
    print(f"    {'× (1−u²)        [N=2,c2]':<28}{mp.nstr(Q_N2,12):>16}{mp.nstr(ppb(Q_N2),8)+' ppb':>18}")
    print()
    print(f"    ⟹ the N=1 cos eigenphase does the dominant correction")
    print(f"      (Form A {mp.nstr(ppb(Q_A),6)} ppb → N=1 {mp.nstr(ppb(Q_N1),6)} ppb).")
    print(f"      c_2 refines to {mp.nstr(ppb(Q_N2),6)} ppb. The remaining gap is")
    print(f"      what c_3+ would close.")
    print()

    # ── 2. closed-form E_0 towers (geometric, Li_2^q) + DIRECTION ─────
    # Q_β needs E_0_tower/E_0_single < 1 (Form A overshoots). Test both.
    needed_factor = Q_codata / Q_A      # what the total scaling must be
    geom = 1 / (1 - hbar2)              # geometric tower 1/(1-ℏ²)
    li2q = 1 + (-li2q_symmetric(-hbar2, q))   # bounded Li_2^q tower
    print("  CLOSED-FORM E_0 TOWER CANDIDATES (conj:alpha-k-categorical-closure):")
    print(f"    needed total scaling Q_codata/Q_A = {mp.nstr(needed_factor, 12)}  (<1 ⟹ NEGATIVE correction)")
    print(f"    geometric 1/(1−ℏ²)               = {mp.nstr(geom, 12)}  (>1 ⟹ WRONG direction)")
    print(f"    Li_2^q 1+(−Li_2^q(−ℏ²))          = {mp.nstr(li2q, 12)}  ({'>1 WRONG dir' if li2q>1 else '<1 ok dir'})")
    print(f"    cos(α−bℏ²/2)                     = {mp.nstr(N1, 12)}  ({'<1 ok dir' if N1<1 else '>1 WRONG'})")
    print()
    print(f"    ⟹ only the cos eigenphase has the correct (negative) direction;")
    print(f"      the geometric and Li_2^q E_0 towers push Q_β the WRONG way.")
    print()

    # ── 3. is the cos-eigenphase scaling Taylor-exact? ────────────────
    err_N1 = abs(ppb(Q_N1))
    err_N2 = abs(ppb(Q_N2))
    closes_N1 = err_N1 < mp.mpf("0.001")
    closes_N2 = err_N2 < mp.mpf("0.001")
    print("  IS A CLOSED-FORM SCALING TAYLOR-EXACT (residual < ~1 ppb)?")
    print(f"    Q_A·cos             residual = {mp.nstr(err_N1, 6)} ppb  → {'EXACT' if closes_N1 else 'NO'}")
    print(f"    Q_A·cos·(1−u²)      residual = {mp.nstr(err_N2, 6)} ppb  → {'EXACT' if closes_N2 else 'NO'}")
    print()

    # ── verdict ───────────────────────────────────────────────────────
    print("=" * 78)
    print(" VERDICT — can all c_k be wired? are we using the right scaling?")
    print("=" * 78)
    print(f"""
  RIGHT SCALING: the residual lives in the SCALING (E_0 / eigenphase),
  exactly as neutron-qvalue-symbolic.md says — NOT in Δ(net). The N=1
  cos(α−bℏ²/2) eigenphase is the correct closed-form scaling and the
  only candidate with the right (negative) direction; the geometric and
  Li_2^q E_0 towers push the wrong way and are refuted as the Q_β closure.

  ALL c_k WIRED? NO — not as derivations:
    • c_2 = -1 is Taylor-exact and wired (the cos·(1−u²) stage).
    • After the cos eigenphase + c_2, the residual is {mp.nstr(err_N2, 6)} ppb.
      Closing it needs c_3+, which are q₀-DEPENDENT (item-1 / addendum:
      the c_3 = J_Hopf structural forms drift 2.6–3.35% across q₀ pins).
    • The exact c_3+ CAN be extracted at canonical q₀, but only by using
      Q_codata itself — that is CIRCULAR (predicting Q_codata from
      Q_codata), not a derivation. So they cannot be wired as predictions.

  WHAT WOULD WIRE THEM: a closed-form scaling refinement to the cos
  eigenphase that is Taylor-exact at canonical q₀ (residual < compute
  precision) — i.e. the genuine multi-Wedderburn-block eigenphase, the
  open bridge. The geometric/Li_2^q towers are NOT it (wrong direction).
  Honest production stays Q_N2 ({mp.nstr(err_N2, 6)} ppb) at the μ-p floor.""")
    print()

    builder.add_data("substrate", {
        "q0": Q_50_DIGIT_STR, "hbar_q2": mp.nstr(hbar2, 18),
        "z": mp.nstr(z, 18), "b": mp.nstr(b, 18),
        "alpha": mp.nstr(alpha, 18), "u": mp.nstr(u, 18),
    })
    builder.add_data("residual_ladder", {
        "Q_A_MeV": mp.nstr(Q_A, 14), "Q_A_ppb": mp.nstr(ppb(Q_A), 8),
        "Q_N1_cos_MeV": mp.nstr(Q_N1, 14), "Q_N1_ppb": mp.nstr(ppb(Q_N1), 8),
        "Q_N2_c2_MeV": mp.nstr(Q_N2, 14), "Q_N2_ppb": mp.nstr(ppb(Q_N2), 8),
    })
    builder.add_data("scaling_direction", {
        "needed_factor_Qcodata_over_QA": mp.nstr(needed_factor, 14),
        "geometric_tower_factor": mp.nstr(geom, 14),
        "li2q_tower_factor": mp.nstr(li2q, 14),
        "cos_eigenphase_factor": mp.nstr(N1, 14),
        "needed_is_negative_correction": bool(needed_factor < 1),
        "geometric_wrong_direction": bool(geom > 1),
        "li2q_wrong_direction": bool(li2q > 1),
        "cos_correct_direction": bool(N1 < 1),
    })
    builder.add_data("verdict", {
        "right_scaling_is_eigenphase_not_delta_net": True,
        "geometric_and_li2q_E0_towers_wrong_direction": True,
        "all_ck_wireable_as_derivations": False,
        "only_c2_taylor_exact": True,
        "ck_ge3_are_circular_if_extracted": True,
        "production_residual_ppb": mp.nstr(err_N2, 8),
        "conclusion": ("Residual is in the scaling (eigenphase/E_0), per "
                       "neutron-qvalue-symbolic.md. The cos eigenphase is "
                       "the only closed-form scaling with the right "
                       "direction; geometric/Li_2^q towers are refuted. "
                       "Only c_2 wires (Taylor-exact); c_3+ are q₀-dependent "
                       "and circular if extracted from Q_codata. All-c_k "
                       "wiring needs the open Taylor-exact eigenphase "
                       "refinement (the bridge). Production stays Q_N2."),
    })
    builder.add_assertion(
        "geometric_li2q_towers_wrong_direction",
        computed=float(1 if (geom > 1 and li2q > 1 and needed_factor < 1) else 0),
        expected=1.0, tolerance=0.0,
        source=("Q_β needs a negative scaling correction (Q_codata/Q_A < 1) "
                "but both the geometric and Li_2^q E_0 towers give factors "
                "> 1 — refuted as the Q_β closure; only the cos eigenphase "
                "has the right direction."),
    )
    builder.save()
    print(f"  Witness: qbeta-scaling-bridge-investigation.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
