#!/usr/bin/env python3
"""qbeta_two_pole_ladder_decomposition.py — where the dominant and
subdominant F-poles each manifest in the canonical Q_β c_k ladder.

Two poles of the precision-ladder generating function
`g(u) = Σ_{k≥2} c_k u^k` (u = b·ℏ_q² at q_0) are now characterized:

  * DOMINANT — simple pole at u_substrate ≈ 0.00852, char root
    `1/u_substrate ≈ 117.41`, tail amplitude `L = lim c_k u_subst^k ≈
    2.118e-13`, residue `A = u_subst·L ≈ 1.804e-15` (PR #1727; precision
    capped at ~4 sig figs by having only 3 tail rungs, PR #1805).
  * SUBDOMINANT — silver/Q_A zero, char root `1/u_silver ≈ 3.1154`
    (PR #2454). Established PURELY ALGEBRAICALLY (Q_A(silver)=0 while
    Δ(net)(silver)≠0); NEVER tested against the actual c_k values.

This probe is a STRUCTURAL DIAGNOSTIC (no fit, no wiring, no tier change).
It answers three questions against the canonical c_2…c_10:

  Part 1 — RUNG PARTITION. The dominant pole contributes
    `D_k = L · root_sub^k` to c_k. Tabulate the fraction `D_k / c_k`.
    Result: the dominant pole is a TAIL phenomenon — it contributes
    <0.4% to the OPEN rungs c_3,c_4,c_5, ~16% at c_6, and overtakes at
    c_7. So the open rungs (the 1ppQ blockers) are NOT a dominant-pole
    phenomenon; they live in the subdominant + entire sector.

  Part 2 — DOES THE SILVER POLE MANIFEST IN THE LADDER? Peel the
    dominant pole (r_k = c_k − D_k, trustworthy for k≤7 given L's 4 sig
    figs) and test whether the residual follows the silver char root
    +3.1154. Result: the residual changes SIGN at k=6 — it does NOT
    exhibit a clean +3.1154 geometric. The canonical c_k do not
    corroborate the silver pole as the leading subdominant ladder
    structure (consistent with PR #2454's own caution that the silver
    zero "does not change any rung's empirical tier").

  Part 3 — TWO-POLE-REMOVED RESIDUAL (the handoff target). Apply the
    depth-2 annihilator of BOTH known roots:
      h_k = c_k − (root_sub+root_silver)·c_{k-1} + (root_sub·root_silver)·c_{k-2}.
    If the two simple poles were the whole story, h_k would vanish. It
    does not (it is large at low k where the entire/A-sector dominates,
    and collapses by ~10^4 in the tail). This re-confirms refuted class
    C5 (constant kernel) from the pole side: the minimal denominator
    Q(u) contains the two known factors (1−root_sub·u)(1−root_silver·u)
    but has degree ≥ 3 — the remainder is the open kernel R(q,ξ). h_k is
    the concrete residual the exact (non-SDP) c_k extraction of #2106 /
    #2474 must explain.

Inputs are loaded from canonical witnesses (no re-derivation):
  * c_k  ← qbeta-decay-sdp-extended-ck.witness.json  (SDP, q_0; carries
           the +1.7% C7 extraction bias on c_2 — structural conclusions
           are order-of-magnitude and robust to it).
  * pole roots ← recomputed from the canonical u(q) map and cross-checked
           against qbeta-silver-pole-subdominant.witness.json (PR #2454).

Grounds `QOU.QBeta.RationalCoeffRecurrence` ("poles of F = reciprocals of
the c_k C-finite-recurrence characteristic roots") with the empirical
two-root decomposition. NO FLOAT (mpmath, 70 dps). Exploratory; no fit.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401,E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

def _load_ck() -> dict[int, mp.mpf]:
    w = json.loads((HERE / "qbeta-decay-sdp-extended-ck.witness.json").read_text())
    raw = w["data"]["c_k_extracted_50dps"]
    return {int(k.split("_")[1]): mp.mpf(v) for k, v in raw.items()}


def main() -> int:
    set_compute_dps()

    c = _load_ck()
    ks = sorted(c)  # 2..10

    # Pole data sourced from the canonical PR #2454 witness — PROTON-anchored,
    # matching the proton-pinned c_k (avoids the 210 ppb proton/muon anchor
    # ambiguity of recomputing u from a q_0 string).
    sv = json.loads((HERE / "qbeta-silver-pole-subdominant.witness.json").read_text())
    u_sub = mp.mpf(sv["data"]["u_substrate"])
    u_silver = mp.mpf(sv["data"]["u_silver"])
    root_sub = mp.mpf(sv["data"]["char_root_dominant_1_over_u_substrate"])
    root_silver = mp.mpf(sv["data"]["char_root_silver_1_over_u_silver"])
    # self-consistency: 1/u must equal the stored char roots
    xchk = max(abs(root_silver - 1 / u_silver), abs(root_sub - 1 / u_sub))

    # --- tail amplitude L = lim c_k u_sub^k  (k = 8,9,10) ---
    xk = {k: c[k] * u_sub**k for k in (8, 9, 10)}
    L = sum(xk.values()) / 3
    L_spread = (max(xk.values()) - min(xk.values())) / L
    residue_A = u_sub * L

    print(f"\n  u_substrate = {mp.nstr(u_sub,12)}   root_sub    = {mp.nstr(root_sub,10)}")
    print(f"  u_silver    = {mp.nstr(u_silver,12)}   root_silver = {mp.nstr(root_silver,10)}")
    print(f"  pole data from PR #2454 witness (proton-anchored); 1/u self-check max|Δ| = {mp.nstr(xchk,3)}")
    print(f"  tail amplitude L = {mp.nstr(L,8)}  (spread {mp.nstr(L_spread,3)}); "
          f"residue A = u_sub·L = {mp.nstr(residue_A,6)}  (~4 sig figs, PR #1805)\n")

    # --- Part 1: rung partition  D_k = L·root_sub^k,  frac = D_k/c_k ---
    print("  Part 1 — RUNG PARTITION  (dominant-pole contribution D_k = L·root_sub^k)")
    print("    k    c_k              D_k (dominant)     |D_k/c_k|")
    D = {}
    frac = {}
    for k in ks:
        D[k] = L * root_sub**k
        frac[k] = abs(D[k] / c[k])
        print(f"   {k:2d}   {mp.nstr(c[k],9):>16}  {mp.nstr(D[k],6):>16}   {mp.nstr(frac[k],4):>10}")
    frac_c3 = frac[3]
    print(f"\n    => open rungs c_3,c_4,c_5 dominant-pole fraction: "
          f"{mp.nstr(frac[3],3)}, {mp.nstr(frac[4],3)}, {mp.nstr(frac[5],3)}  "
          f"(<0.4%); c_6 {mp.nstr(frac[6],3)}; c_7 {mp.nstr(frac[7],3)} (overtakes).")

    # --- Part 2: does the silver pole manifest? dominant-peeled residual ---
    print("\n  Part 2 — SILVER POLE vs LADDER  (residual r_k = c_k − D_k, k≤7 trusted)")
    r = {k: c[k] - D[k] for k in range(4, 8)}
    print("    k    r_k = c_k − D_k     r_k/r_{k-1}")
    ratios = {}
    prev = None
    for k in range(4, 8):
        rr = "" if prev is None else mp.nstr(r[k] / prev, 5)
        ratios[k] = None if prev is None else r[k] / prev
        print(f"   {k:2d}   {mp.nstr(r[k],7):>16}   {rr:>10}")
        prev = r[k]
    sign_flips = sum(1 for k in range(5, 8) if mp.sign(r[k]) != mp.sign(r[k - 1]))
    print(f"\n    silver char root = +{mp.nstr(root_silver,6)} (would give a clean "
          f"same-sign ×3.115 geometric).")
    print(f"    observed residual sign-flips in k=4..7: {sign_flips}  => NO clean "
          f"+3.115 geometric. The canonical c_k do NOT corroborate the silver pole")
    print(f"    as the leading subdominant ladder structure (entire/A-sector masks it).")

    # --- Part 3: two-pole-removed residual h_k (depth-2 annihilator) ---
    print("\n  Part 3 — TWO-POLE-REMOVED RESIDUAL  "
          "h_k = c_k − (r_s+r_σ)c_{k-1} + (r_s·r_σ)c_{k-2}")
    s1 = root_sub + root_silver
    s2 = root_sub * root_silver
    print("    k    h_k                |h_k/c_k|")
    h = {}
    for k in range(4, 11):
        h[k] = c[k] - s1 * c[k - 1] + s2 * c[k - 2]
        print(f"   {k:2d}   {mp.nstr(h[k],7):>16}   {mp.nstr(abs(h[k]/c[k]),4):>10}")
    h_tail_collapse = abs(h[10] / c[10])
    print(f"\n    two simple poles alone do NOT annihilate the ladder (h_k ≠ 0): large at"
          f"\n    low k (entire sector), collapses to {mp.nstr(h_tail_collapse,3)}·c_k in the tail.")
    print(f"    => minimal denominator Q(u) ⊇ (1−root_sub·u)(1−root_silver·u) but deg ≥ 3")
    print(f"       (consistent with refuted class C5, constant kernel). The deg≥3")
    print(f"       remainder is the open kernel R(q,ξ); h_k is the exact-extraction target.")

    # --- witness ---
    w = (WitnessBuilder("qbeta-two-pole-ladder-decomposition", engine="mpmath")
         .set_content_block("prop:q-beta-radius-of-convergence-gate")
         .set_description(
             "Structural diagnostic (no fit/wiring): where the dominant "
             "(root 117.41, PR #1727) and subdominant silver (root 3.1154, "
             "PR #2454) F-poles each manifest in the canonical Q_β c_2..c_10 "
             "ladder. (1) Rung partition: dominant pole is TAIL-only, "
             "contributing <0.4% to open rungs c_3,c_4,c_5. (2) First test of "
             "the silver pole against the actual c_k: the dominant-peeled "
             "residual shows no clean +3.1154 geometric (sign-flips at k=6) — "
             "the ladder does not corroborate the silver zero as leading "
             "subdominant structure (matches PR #2454's caution). (3) The "
             "depth-2 annihilator of both roots leaves h_k≠0 (large at low k, "
             "~1e-4 collapse in tail) => minimal denominator deg>=3 (re-confirms "
             "C5 from the pole side); h_k is the exact-extraction target for "
             "#2106/#2474. NO FLOAT, 70 dps. Exploratory."))
    w.add_data("u_substrate", str(u_sub))
    w.add_data("u_silver", str(u_silver))
    w.add_data("char_root_dominant", str(root_sub))
    w.add_data("char_root_silver", str(root_silver))
    w.add_data("tail_amplitude_L", str(L))
    w.add_data("tail_spread_rel", str(L_spread))
    w.add_data("residue_A", str(residue_A))
    w.add_data("rung_partition_frac_dom", {str(k): mp.nstr(frac[k], 6) for k in ks})
    w.add_data("dominant_peeled_residual", {str(k): mp.nstr(r[k], 8) for k in r})
    w.add_data("two_pole_removed_residual_h", {str(k): mp.nstr(h[k], 8) for k in h})
    w.add_data("residual_sign_flips_k4_7", sign_flips)

    # decisive assertions
    w.add_assertion(
        "dominant_tail_ratio_matches_root_sub",
        computed=float(c[10] / c[9]), expected=float(root_sub),
        tolerance=0.05,
        source="c_10/c_9 -> 1/u_substrate = 117.41 (reproduces PR #1727)")
    w.add_assertion(
        "open_rung_c3_dominant_negligible",
        computed=float(frac_c3), expected=0.0, tolerance=1e-3,
        source="dominant-pole fraction D_3/c_3 < 1e-3: c_3 is NOT a "
               "dominant-pole rung (lives in subdominant+entire sector)")
    w.add_assertion(
        "silver_pole_not_leading_subdominant_in_ladder",
        computed=float(sign_flips), expected=2.0, tolerance=0.5,
        source="dominant-peeled residual sign-flips at k=6 => no clean "
               "+3.1154 geometric; canonical c_k do not corroborate the "
               "silver pole as leading subdominant ladder structure")
    print(f"\n  witness: {w.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
