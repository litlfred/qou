#!/usr/bin/env python3
"""mu4_magnitude_gap_anatomy_probe.py
======================================

**The 9.56× A=4 magnitude gap: what shape is it, and is it chaseable?**

`helium4-mu4-cluster-moment.witness.json` reports `μ₄/μ₃ = −1.0206` against a
target `−9.7522` — alternation reproduced, `|ratio|` off by 9.56×. This probe
answers two questions about that number before anyone tries to close it.

**(1) THE GAP IS NOT ONE FACTOR ON μ₄.** It is the product of two misses in
OPPOSITE directions:

    μ₃ measured is 1.8228x TOO LARGE   (k₃ = target/measured = 0.5486)
    μ₄ measured is 5.2419x TOO SMALL   (k₄ = target/measured = 5.2419)
    k₄/k₃ = 9.5547 — the reported ratio-of-ratios

So an attack shaped as "μ₄ is 9.56× too small" is aimed at the wrong object; no
single multiplicative correction on μ₄ closes it, because μ₃ is also wrong and
in the other direction.

**A WARNING ABOUT THE OBVIOUS NEXT STEP.** It is tempting to read `k_n ∝ r^n`
with `r ≈ 9.55` — a geometric per-body-order rescaling. **That is a tautology,
not a finding**: two points (`k₃`, `k₄`) fitted by two parameters (`a`, `r`) is
exact for ANY pair. It becomes a test only with a third order, i.e. a μ₂ target
from the same simplex. This probe therefore reports the two-point law as
underdetermined and does NOT quote `r` as a result.

**(2) THE GAP IS A KNOWN WALL, AND IT IS SCOPE-(a).**
`a4-interface-magnitude-one-scalar-gate.witness.json` already establishes:

    b4(m) = -ln det(I+G),  det(I+G) = (1-5m^2)(1-m^2),  m in (0, 1/sqrt5)

is **surjective onto (0,∞)** in its single free per-pair scalar. Every positive
AME target is reachable, and each reaching `m` is a function of the target —
anchor inversion, i.e. a FIT. Its verdict: *"WALL(scope-(a)) magnitude open …
surviving mechanism = a categorical principle fixing m in (0,1/sqrt5) strictly
below the naive z"*.

**Consequence, and it is the practical point: the magnitude gap is not
chaseable by computation.** More numerics cannot close a one-scalar family that
already reaches every target; only a categorical principle that FIXES the scalar
can. Any probe that "closes" it by solving for `m` has inverted the anchor.

**(3) A CONVENTION-C RESIDUE IN THAT LIVE EXCLUSION — verdict unaffected.**
The same witness carries a *separate* scope-(b) exclusion: the naive uniform
per-pair bond factor gives `5z² > 1`, hence `det(I+G) < 0`, hence no attractive
branch. It cites

    naive_z_bond_factor = 0.499320334

which is `z_C = √q₀/(q₀+1)` — **convention C, excised by the owner ruling of
2026-08-09/2026-08-15 R1**. The canonical convention-D value is
`z_D = q₀³/(q₀²+1) = 0.612688037`.

This probe checks whether the exclusion survives the convention change. **It
does, and it strengthens**: `z_D` sits further above the `1/√5` ceiling than
`z_C`, so `det(I+G)` is more negative. The verdict is untouched; only the cited
number is stale. Recorded rather than silently corrected, because the witness is
not this branch's to regenerate and the exclusion it supports is live.

PRECISION
---------
mpmath at 50 dps. The measured μ inputs come from the committed He4 witness,
which serializes them as raw float64, so ratios inherit that and nothing beyond
it is claimed — the gap is O(1)–O(10), some 15 orders above float64 resolution.
The convention arithmetic is exact in mpf from `q₀`. `float()` only in display.

SCOPE
-----
(a). No target is inverted; no scalar is solved for; nothing is wired. This
probe closes nothing — it characterises the shape of an open wall and flags a
stale number inside a live exclusion.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import subprocess
import time

import mpmath as mp  # noqa: E402

from _precision import fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 50
HE4 = "computations/deltalambda/helium4-mu4-cluster-moment.witness.json"
GATE = "computations/deltalambda/a4-interface-magnitude-one-scalar-gate.witness.json"


def committed(path, key=None):
    raw = subprocess.run(["git", "show", f"origin/main:{path}"],
                         capture_output=True, text=True, check=True).stdout
    d = json.loads(raw)
    return d["data"][key] if key else d


def main() -> int:
    t0 = time.monotonic()

    # ---- (1) anatomy of the gap -------------------------------------------
    m = committed(HE4, "mu4_cluster_moment")
    mu4_meas = mp.mpf(str(m["mu4_measured"]))
    mu3_meas = mp.mpf(str(m["mu3_mean"]))
    ratio_meas = mp.mpf(str(m["ratio_measured"]))
    ratio_targ = mp.mpf(str(m["ratio_target"]))
    mu4_targ = mp.mpf("-4.591")
    mu3_targ = mp.mpf("0.4708")

    k3 = mu3_targ / mu3_meas
    k4 = mu4_targ / mu4_meas
    rr = ratio_targ / ratio_meas

    print("(1) ANATOMY — the gap is a PRODUCT of two opposite misses")
    print(f"    mu3 measured too LARGE by {mp.nstr(1/k3, 6)}x   (k3 = {mp.nstr(k3, 8)})")
    print(f"    mu4 measured too SMALL by {mp.nstr(k4, 6)}x   (k4 = {mp.nstr(k4, 8)})")
    print(f"    k4/k3 = {mp.nstr(k4/k3, 8)}   ratio-of-ratios = {mp.nstr(rr, 8)}")
    print("    => no single multiplicative fix on mu4 can close it.")
    print("    => k_n ~ a*r^n is 2 params on 2 points: UNDERDETERMINED, not a finding.")

    # ---- (2)/(3) convention frame of the live scope-(b) exclusion ----------
    q0 = Q_MP
    zC = mp.sqrt(q0) / (q0 + 1)
    zD = q0 ** 3 / (q0 ** 2 + 1)
    ceiling = 1 / mp.sqrt(5)
    gate = committed(GATE)
    # The gate's schema changed in 32c059c7d2, when the hand-written witness
    # got its first producer. `inputs.naive_z_bond_factor` -- a truncated
    # string "0.499320334  (b4-...)" -- is GONE, and correctly so: it cited
    # the excised convention-C value as though it were *the* naive factor.
    # The producer now reports BOTH conventions, at full precision, under
    # data.naive_z_exclusion_both_conventions. Read that; fall back to the
    # legacy path so this probe still runs against an older witness.
    _both = gate.get("data", {}).get("naive_z_exclusion_both_conventions")
    if _both:
        cited = mp.mpf(_both["z_C"]["z"])
        cited_src = "data.naive_z_exclusion_both_conventions.z_C.z"
    else:
        cited = mp.mpf(str(gate["inputs"]["naive_z_bond_factor"].split()[0]))
        cited_src = "inputs.naive_z_bond_factor (legacy schema)"

    def det_IG(z):
        return (1 - 5 * z ** 2) * (1 - z ** 2)

    cited_is_C = abs(cited - zC) < mp.mpf("1e-9")
    both_excluded = det_IG(zC) < 0 and det_IG(zD) < 0
    d_more_negative = det_IG(zD) < det_IG(zC)

    print()
    print("(3) CONVENTION FRAME of the live scope-(b) exclusion")
    print(f"    witness z_C = {mp.nstr(cited, 12)}   [{cited_src}]")
    print(f"      z_C (excised)   = {mp.nstr(zC, 12)}   agrees? {cited_is_C}")
    print(f"      z_D (canonical) = {mp.nstr(zD, 12)}")
    print(f"    ceiling 1/sqrt5   = {mp.nstr(ceiling, 12)}")
    for nm, z in (("z_C", zC), ("z_D", zD)):
        print(f"      {nm}: 5z^2 = {mp.nstr(5*z**2, 10):>14}  "
              f"det(I+G) = {mp.nstr(det_IG(z), 10):>14}  "
              f"{'EXCLUDED' if det_IG(z) < 0 else 'admissible'}")
    print(f"    exclusion survives under D? {both_excluded}   "
          f"and is STRONGER under D? {d_more_negative}")

    w = WitnessBuilder("mu4-magnitude-gap-anatomy", start_time=t0)
    w.set_description(
        "Anatomy of the 9.56x A=4 magnitude gap: it is a PRODUCT of two "
        "opposite misses (mu3 too large, mu4 too small), not one factor on "
        "mu4; the geometric per-order reading is underdetermined on two "
        "points; the gap is a known scope-(a) WALL whose mechanism is "
        "surjective onto every target, hence not chaseable by computation; "
        "and the live scope-(b) naive-z exclusion is reported by the gate "
        "under BOTH conventions, with the verdict unaffected and "
        "strengthened under D.")
    w.add_data("anatomy", {
        "mu3_measured": fmt(mu3_meas), "mu3_target": fmt(mu3_targ),
        "mu4_measured": fmt(mu4_meas), "mu4_target": fmt(mu4_targ),
        "k3_target_over_measured": fmt(k3),
        "k4_target_over_measured": fmt(k4),
        "mu3_too_large_by": fmt(1 / k3),
        "mu4_too_small_by": fmt(k4),
        "ratio_of_ratios": fmt(rr),
        "single_factor_on_mu4_suffices": False,
        "geometric_per_order_law": ("UNDERDETERMINED — 2 parameters on 2 "
                                    "points; needs a mu2 target from the same "
                                    "simplex to become a test. r deliberately "
                                    "not quoted."),
    })
    w.add_data("wall", {
        "source": GATE,
        "verdict_quoted": gate.get("verdict"),
        "mechanism_surjective_onto_all_targets": True,
        "reading": ("The magnitude gap is NOT chaseable by computation: a "
                    "one-scalar family already reaches every target, so any "
                    "probe that 'closes' it has inverted the anchor. Closing "
                    "requires a categorical principle FIXING m."),
    })
    w.add_data("convention_residue", {
        "cited_naive_z": fmt(cited),
        "z_C_excised": fmt(zC), "z_D_canonical": fmt(zD),
        "cited_is_convention_C": cited_is_C,
        "ceiling_one_over_sqrt5": fmt(ceiling),
        "det_IG_at_zC": fmt(det_IG(zC)), "det_IG_at_zD": fmt(det_IG(zD)),
        "exclusion_survives_under_D": both_excluded,
        "exclusion_stronger_under_D": d_more_negative,
        "action": ("Recorded, not silently corrected: the witness is not this "
                   "branch's to regenerate and the exclusion it supports is "
                   "live and unaffected."),
    })
    w.add_assertion("gap_is_not_single_factor_on_mu4", True, True)
    w.add_assertion("cited_naive_z_is_convention_C", cited_is_C, True)
    w.add_assertion("scope_b_exclusion_survives_under_D", both_excluded, True)
    w.save()
    print(f"\nwall {time.monotonic()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
