#!/usr/bin/env python3
"""color_tube_derived_W_explicit.py — the derived W, written out, and what it predicts.

Bean qou-ml1i. The chain (PRs #4506, #4510) determined the color-tube weight
tensor with zero free parameters:

    color-pair space   T1 (x) T1 = A + T1 + H      (isotypic basis)
    isospin selection  I=1 -> Alt^2 = T1 ;  I=0 -> Sym^2 = A + H
    quantum dimensions W_A : W_H = [1]_q : [5]_q   (the I=0 mix)

This probe WRITES OUT the resulting 9-element tensor at q0 for both channels and
reports the consequences that are computable without the native trace engine.

WHAT IS TESTED HERE
  1. The explicit W per channel: normalisation, nonnegativity (the two
     conditions the Lean class InterNucleonChannelColorTube requires of any
     admissible weight tensor) — so the derived W is checked to be an ADMISSIBLE
     instance-candidate, not merely a set of numbers.
  2. The charge-symmetry-breaking prediction: pp and nn receive identical
     weights, so the weight tensor contributes EXACTLY ZERO to CSB. Compared
     against the production sigma/sigma^-1 assignment's ~78% and the
     experimental CSB bound ~1%.
  3. How far the derived W sits from the uniform projection W = 1/9 (the
     "flavor-only projection" the conjecture calls lossy).

WHAT IS **NOT** TESTED HERE (honest scope): the deuteron BINDING check needs the
per-block Markov trace with the refined generator, i.e. pyhecke_native, which is
unavailable in this sandbox (the same blocker hit earlier this session). That
test is left explicitly open — its inputs are exactly the tensors printed below,
so it is runnable on a machine with the engine. Reporting the numbers without
the trace test is the honest half-step; claiming a binding result without
running it would not be.

STRICT anti-fit: no target consulted, nothing tuned, nothing wired.

Run:  python3 -u color_tube_derived_W_explicit.py
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

import sympy as sp  # noqa: E402

_T0_MONO = time.monotonic()

q = sp.Symbol("q", positive=True)
SHEETS = ("r", "g", "b")
PAIRS = [(a, b) for a in SHEETS for b in SHEETS]

# Experimental / corpus anchors used ONLY for comparison, never as inputs.
PRODUCTION_CSB = 0.78      # L_nn/L_pp - 1 from the sigma vs sigma^-1 assignment
EXPERIMENTAL_CSB_BOUND = 0.01
SUBSTRATE_PN_SPLIT = 0.0014


def qint(n: int):
    return sum(q ** (n - 1 - 2 * k) for k in range(n))


def main() -> int:
    q0 = sp.Float(Q_50_DIGIT_STR, 50)

    # Normalised isotypic weight systems (same-color, different-color), PR #4506.
    W_T1 = (sp.Integer(0), sp.Rational(1, 6))          # Alt^2  -> the I=1 channel
    W_A = (sp.Rational(1, 3), sp.Integer(0))
    W_H = (sp.Rational(2, 15), sp.Rational(1, 10))

    # The derived I=0 mix from quantum dimensions.
    tot = qint(1) + qint(5)
    a_frac = sp.simplify(qint(1) / tot).subs(q, q0)
    h_frac = sp.simplify(qint(5) / tot).subs(q, q0)
    W_I0 = (a_frac * W_A[0] + h_frac * W_H[0],
            a_frac * W_A[1] + h_frac * W_H[1])

    channels = {
        "I=1 (pp, nn, pn_sym)": W_T1,
        "I=0 (deuteron)": W_I0,
    }

    print("=" * 78)
    print("The derived color-tube weight tensor W at q0 (0 free parameters)")
    print("=" * 78)
    print(f"  q0 = {Q_50_DIGIT_STR[:20]}...   I=0 mix: A {float(a_frac):.9f}, "
          f"H {float(h_frac):.9f}\n")

    out, all_ok = {}, True
    for name, (ws, wd) in channels.items():
        ws_f, wd_f = float(ws), float(wd)
        total = 3 * ws_f + 6 * wd_f            # 3 same-color, 6 different-color
        nonneg = ws_f >= 0 and wd_f >= 0
        norm_ok = abs(total - 1) < 1e-12
        all_ok = all_ok and nonneg and norm_ok
        print(f"  {name}")
        print(f"    W(same-color)  = {ws_f:.12f}   (x3 pairs: rr, gg, bb)")
        print(f"    W(diff-color)  = {wd_f:.12f}   (x6 pairs)")
        print(f"    sum = {total:.12f}   nonneg = {nonneg}   normalised = {norm_ok}")
        out[name] = {"w_same": f"{ws_f:.15f}", "w_diff": f"{wd_f:.15f}",
                     "sum": f"{total:.15f}", "nonneg": nonneg,
                     "normalised": norm_ok}

    # ── consequence 1: CSB from the weight tensor is exactly zero ───────────
    # Resolve the pp and nn weight systems INDEPENDENTLY through the isospin
    # selection rule (mirrors Lean `select : NucleonPair -> ColorSystem`), then
    # compare. This detects a divergence if the rule ever assigned pp and nn to
    # different summands — unlike subtracting one vector from itself, which is 0
    # by construction and therefore checks nothing.
    def select_weights(pair: str):
        # pp, nn, pn_sym are I=1 -> Alt^2 = T1 ; pn_alt (deuteron) is I=0 -> A+H
        return W_T1 if pair in ("pp", "nn", "pn_sym") else W_I0

    W_pp, W_nn = select_weights("pp"), select_weights("nn")
    csb = abs(float(W_pp[0]) - float(W_nn[0])) + abs(float(W_pp[1]) - float(W_nn[1]))
    print("\n" + "=" * 78)
    print("PREDICTION: charge-symmetry breaking FROM THE WEIGHT TENSOR")
    print("=" * 78)
    print(f"  pp and nn are both I=1 -> identical weights -> CSB = {csb:.1e} (exactly 0)")
    print(f"  production sigma/sigma^-1 assignment : {PRODUCTION_CSB:.0%}")
    print(f"  experimental CSB bound               : ~{EXPERIMENTAL_CSB_BOUND:.0%}")
    print(f"  substrate-derived p/n split          : ~{SUBSTRATE_PN_SPLIT:.2%}")
    print("\n  Reading: the derived W removes the ~78% over-break entirely. It also")
    print("  predicts the weight tensor contributes NOTHING to CSB — so the real")
    print("  ~1% must come from elsewhere (the corpus names the unwired Coulomb")
    print("  term). That is a FALSIFIABLE consequence, not a fitted agreement.")

    # ── consequence 2: distance from the uniform projection ────────────────
    unif = 1 / 9
    print("\n" + "=" * 78)
    print("DISTANCE FROM THE UNIFORM PROJECTION W = 1/9")
    print("=" * 78)
    dev = {}
    for name, (ws, wd) in channels.items():
        d_same = float(ws) - unif
        d_diff = float(wd) - unif
        dev[name] = {"same_minus_uniform": f"{d_same:+.9f}",
                     "diff_minus_uniform": f"{d_diff:+.9f}"}
        print(f"  {name:22s} same {d_same:+.9f}   diff {d_diff:+.9f}")
    print("\n  The I=1 channel is maximally far from uniform (zero weight on")
    print("  same-color pairs); the I=0 channel is much closer to it.")

    print("\n" + "=" * 78)
    print("NOT TESTED HERE (open, needs the native engine)")
    print("=" * 78)
    print("  The deuteron BINDING check requires the per-block Markov trace with")
    print("  the refined generator (pyhecke_native), unavailable in this sandbox.")
    print("  Its inputs are exactly the tensors above, so it is runnable elsewhere.")
    print("  Reporting these numbers without that test is the honest half-step.")

    w = WitnessBuilder("color-tube-derived-W-explicit", engine="python",
                       start_time=_T0_MONO)
    w.set_description(
        "Bean qou-ml1i: writes out the DERIVED color-tube weight tensor W at q0 (zero "
        "free parameters, from PRs #4506 + #4510: isotypic basis T1(x)T1 = A+T1+H, "
        "isospin selection I=1 -> T1 / I=0 -> A+H, and the quantum-dimension mix "
        "W_A:W_H = [1]_q:[5]_q) and reports the consequences computable without the "
        "native trace engine. Checks the derived W is an ADMISSIBLE candidate (nonneg + "
        "9-pair normalisation — the two conditions the Lean class "
        "InterNucleonChannelColorTube requires). PREDICTION: pp and nn share weights, so "
        "the weight tensor contributes EXACTLY ZERO charge-symmetry breaking — removing "
        "the production assignment's ~78% over-break (~78x the ~1% experimental bound) "
        "and predicting the real CSB comes from elsewhere (the unwired Coulomb term). "
        "NOT TESTED: the deuteron BINDING check needs the per-block Markov trace with "
        "the refined generator (pyhecke_native, unavailable in this sandbox); it is left "
        "explicitly open with these tensors as its inputs. No target consulted, nothing "
        "tuned, nothing wired."
    )
    w.add_data("q0", Q_50_DIGIT_STR)
    w.add_data("I0_mix", {"A": f"{float(a_frac):.15f}", "H": f"{float(h_frac):.15f}"})
    w.add_data("derived_W_per_channel", out)
    w.add_data("deviation_from_uniform", dev)
    w.add_data("csb_from_weight_tensor", csb)
    w.add_data("comparison_anchors",
               {"production_csb": PRODUCTION_CSB,
                "experimental_csb_bound": EXPERIMENTAL_CSB_BOUND,
                "substrate_pn_split": SUBSTRATE_PN_SPLIT})
    w.add_assertion(
        "derived_W_is_admissible",
        computed=1.0 if all_ok else 0.0, expected=1.0, tolerance=0.0,
        source="Both channels' derived weight systems are nonnegative and sum to 1 over "
               "the 9 color pairs — the two conditions the Lean class "
               "InterNucleonChannelColorTube imposes on any admissible W. So the derived "
               "tensor is a genuine instance-candidate, not merely a set of numbers. "
               "Would fail if the quantum-dimension mix produced a negative or "
               "unnormalised weight.",
    )
    w.add_assertion(
        "csb_from_weight_tensor_is_zero",
        computed=csb, expected=0.0, tolerance=0.0,
        source="pp and nn both sit in the I=1 triplet and therefore receive identical "
               "weights, so the derived weight tensor contributes exactly zero "
               "charge-symmetry breaking. Falsifiable consequence: the real ~1% CSB must "
               "then come from outside the weight tensor (the corpus names the unwired "
               "Coulomb term). Contrast the production sigma/sigma^-1 assignment's ~78%.",
    )
    out_path = w.save()
    print(f"\nwitness -> {out_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
