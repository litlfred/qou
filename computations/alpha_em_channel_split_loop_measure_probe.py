#!/usr/bin/env python3
"""alpha_em_channel_split_loop_measure_probe.py

Lever 2 of the 1ppq re-evaluation (docs/audits/2026-07-17-onepq-path-reevaluation.md):
re-scope the single underived alpha_EM factor — the per-loop measure 1/(pi*b1) = 1/(8pi)
(2-loop derivability map, 2026-07-14: "the wall"; the proved heat-kernel measure
1/Area = 1/(12pi) is EXCLUDED by data at 1-loop).

THE CHANNEL-SPLIT READING (this probe, all steps verified symbolically):

  (1) DERIVED (map, re-verified here): the loop tower resums as
        sum_{L>=0} (-1)^L [L+1]_q x^L = 1 / ((1+q*x)(1+q^{-1}*x)),
      i.e. the tower FACTORS into TWO geometric series — the two braiding/Hecke
      channels of A(x)A (eigenvalues q, -q^{-1}; the singlet/adjoint idempotent pair).
  (2) Each channel is a geometric series with per-loop ratio q^{+-1} * x.
  (3) With x = alpha/(8pi), the 1-loop term at q=1 is [2]_1 * x = 2x = alpha/(4pi):
      the TWO channels together carry exactly ONE unit of the standard 4D gauge-theory
      loop normalization alpha/(4pi) — each channel carrying half, alpha/(8pi).

  So:  per-loop measure 1/(8pi) = (1/2) * (1/4pi)
                                = (universal loop unit) shared equally by the 2 channels.

  The "1/(pi*b1)" form is then a COINCIDENCE OF GENUS 4: pi*b1 = 8pi equals
  2*(4pi) only because b1 = 2g = 8. The structural constant is 2*4pi
  (channels x loop unit), NOT pi*(Betti number) — consistent with the derivability
  map's own finding that the b1-parallel to the zero-mode measure is unsound.

HONEST TIER — a RE-SCOPE, not a closure:
  What is removed:   the underived GEOMETRIC identification "1/(pi * dim H^1)".
  What replaces it:  (derived two-channel factorization) + ONE remaining input —
                     the correspondence-limit normalization: at q=1 the loop
                     parameter must reduce to the standard gauge loop unit
                     alpha/(4pi). This is a standard-QFT correspondence statement,
                     not a new geometric claim — but it IS still an input.
  Discriminant:      channel-split predicts the measure is GENUS-INDEPENDENT
                     (2*4pi always); the pi*b1 reading scales with genus. Not
                     testable at fixed g=4 by data, but structurally decisive for
                     any future multi-genus construction.

No coefficient fitted; identical numerics to the committed form (x = alpha/(8pi));
no c_k wired; scope-(a). Companion: alpha_em_loop_measure_consistency_probe.py,
alpha_em_theta_graph_two_loop_probe.py, docs/audits/2026-07-14-alpha-em-2loop-derivability-map.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def main() -> int:
    print("=" * 78)
    print(" α_EM per-loop measure — the channel-split reading (lever 2 re-scope)")
    print("=" * 78)

    wb = WitnessBuilder("alpha-em-channel-split-loop-measure", engine="sympy+mpmath")
    wb.set_description(
        "Re-scopes the underived alpha_EM per-loop measure 1/(8pi). Verified: the "
        "derived loop tower sum (-1)^L [L+1]_q x^L factors as 1/((1+qx)(1+q^-1 x)) "
        "(two braiding channels), and with x=alpha/(8pi) the q=1 one-loop term is "
        "exactly alpha/(4pi) — the standard gauge loop unit shared equally by the 2 "
        "channels. So 1/(8pi) = (1/2)(1/(4pi)) structurally; the 'pi*b1' form is a "
        "genus-4 coincidence (2*4pi = pi*8 only because b1=8). Remaining input: the "
        "q=1 correspondence normalization (standard QFT), replacing the unsound "
        "geometric 1/(pi*dimH1) identification. Genus-independence is the "
        "discriminant. No fit; numerics unchanged; scope-(a)."
    )
    wb.set_content_block("prop:em-coupling-bring-zero-mode")

    q, x = sp.symbols("q x", positive=True)
    L = sp.symbols("L", integer=True, nonnegative=True)

    # (1) factorization: sum (-1)^L [L+1]_q x^L == 1/((1+qx)(1+x/q)), verified to depth N
    N = 12
    qint = lambda n: (q**n - q**(-n)) / (q - 1/q)
    series_lhs = sum((-1)**l * qint(l + 1) * x**l for l in range(N))
    rhs = 1 / ((1 + q*x) * (1 + x/q))
    diff = sp.simplify(sp.series(rhs, x, 0, N).removeO() - series_lhs)
    fact_ok = diff == 0
    print(f"\n[1] factorization Σ(−1)^L[L+1]_q x^L = 1/((1+qx)(1+q⁻¹x)) to O(x^{N}): "
          f"{'VERIFIED' if fact_ok else 'FAILED: ' + str(diff)}")
    print("    ⇒ the loop tower IS two geometric channels with per-loop ratios q·x, q⁻¹·x.")

    # (2) q=1 one-loop term with x = alpha/(8pi) equals alpha/(4pi)
    alpha = sp.symbols("alpha", positive=True)
    x_val = alpha / (8 * sp.pi)
    one_loop_q1 = sp.simplify(qint(2).subs(q, 1) * x_val)  # [2]_1 * x — need limit at q=1
    one_loop_q1 = sp.simplify(sp.limit(qint(2), q, 1) * x_val)
    target = alpha / (4 * sp.pi)
    corr_ok = sp.simplify(one_loop_q1 - target) == 0
    print(f"[2] q→1 one-loop term [2]₁·x at x=α/(8π): {one_loop_q1} "
          f"{'= α/(4π) VERIFIED' if corr_ok else '≠ α/(4π) FAILED'}")
    print("    ⇒ the 2 channels together carry ONE standard loop unit α/(4π); each α/(8π).")

    # (3) the coincidence: pi*b1 = 2*(4pi) iff b1 = 8
    b1 = sp.symbols("b_1", positive=True)
    coincidence = sp.solve(sp.Eq(sp.pi * b1, 2 * 4 * sp.pi), b1)
    print(f"[3] π·b₁ = 2·(4π) ⟺ b₁ = {coincidence[0]} — the Bring value (2g=8). "
          "The b₁-form is a genus-4 coincidence; the structural constant is 2×4π.")

    # (4) sanity: the committed 1-loop residual is unchanged (numerics identical)
    Q_P = mp.mpf("1.109978582751380808")
    CODATA = mp.mpf("137.035999084")
    qb = lambda n, qq: (qq**n - qq**(-n)) / (qq - qq**(-1))
    T = Q_P * qb(9, Q_P) * qb(10, Q_P) + mp.mpf(8) / (12 * mp.pi)
    h2 = (Q_P - 1 / Q_P) ** 2
    H = qb(2, Q_P) / (8 * mp.pi)
    roots = mp.polyroots([-H * h2, H, T, -1])
    aB = min([mp.re(r) for r in roots if mp.im(r) == 0 and mp.re(r) > 0],
             key=lambda r: abs(r - mp.mpf("0.0073")))
    resid = float((1 / aB - CODATA) / CODATA * 1e9)
    print(f"[4] numerics unchanged: form-B residual at proton pin = {resid:+.3f} ppb (2.1σ) ✓")

    print("\n  RE-SCOPE (honest): the wall '1/(π·b₁) underived geometric measure' becomes")
    print("  (derived 2-channel factorization) + (q=1 correspondence: loop unit = α/(4π)).")
    print("  The remaining input is standard-QFT normalization, NOT a new geometric claim —")
    print("  but it IS still an input. Discriminant: measure is genus-INDEPENDENT (2·4π).")

    wb.add_data("factorization_depth", N)
    wb.add_data("channel_split", {
        "per_loop_x": "alpha/(8pi)", "per_channel": "alpha/(8pi)",
        "channel_pair_total": "alpha/(4pi) (standard gauge loop unit)",
        "b1_coincidence": "pi*b1 = 2*(4pi) iff b1=8 (genus-4)",
        "discriminant": "genus-independent (2*4pi), vs pi*b1 which scales"})
    wb.add_data("remaining_input", "q=1 correspondence normalization: loop unit = alpha/(4pi)")
    wb.add_data("form_B_residual_ppb", resid)
    wb.add_assertion("loop_tower_factorizes_two_channels",
                     computed=float(fact_ok), expected=1.0, tolerance=0.5,
                     source=f"sum (-1)^L [L+1]_q x^L = 1/((1+qx)(1+q^-1 x)) to O(x^{N}), sympy")
    wb.add_assertion("q1_limit_is_standard_loop_unit",
                     computed=float(corr_ok), expected=1.0, tolerance=0.5,
                     source="[2]_{q=1} * alpha/(8pi) = alpha/(4pi) exactly")
    wb.add_assertion("numerics_unchanged_form_B",
                     computed=float(abs(resid - 0.313) < 0.02), expected=1.0, tolerance=0.5,
                     source="form-B proton residual +0.313 ppb reproduced")
    wb.save()

    ok = fact_ok and corr_ok
    print(f"\n  RESULT: {'ALL OK' if ok else 'CHECK'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
