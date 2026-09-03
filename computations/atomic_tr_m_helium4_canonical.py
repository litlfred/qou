"""Canonical |tr_M(⁴He)| via Phase 5q closed form (Track C migration).

Replaces the deprecated `atomic_tr_m_helium4.py` (which used the
disjoint-product extension on H_12, documented as non-canonical
per PR #564 audit).

## Pipeline

1. Compute the H_3 traces `tau_p, tau_n` via the Wenzl bridge at 50 dps.
2. Apply the Phase 5q closed form
       tr_M(𝓑_⁴He) = closed_form_tau_M(2, 2, q_0, tau_p, tau_n)
   with the canonical `pn_convention="bring_color_weighted"` (owner
   ruling 2026-08-15, R3), which is also `closed_form_tau_M`'s own
   default.

   THIS WAS `chi_lambda_braid` UNTIL 2026-08-25, on two stated grounds,
   and both were wrong:

   * *"the default"* — it has not been the default since 2026-06-01.
     `closed_form_tau_M`'s docstring calls `chi_lambda_braid` a
     backward-compatibility convention "retained for pre-2026-06-01
     scripts", and it drops the p-n averaging entirely, treating the
     interface as a positive σ.
   * *"Phase 5q verified it matches the empirical slow path at 1e-49"* —
     true, and it does not say what it was used here to say. That slow
     path is BOUND to `chi_lambda_braid` via `marshal_to_chi_lambda_braid`
     (`closed_form_tau_M_verification_phase5q.py` says so in-line). So
     Phase 5q validates the closed form as a faithful, 22M×-faster
     reimplementation of the OLD MARSHALLING. It is a check on the
     machinery, not evidence that plain-σ is the right p-n treatment —
     and R3 says it is not.

   Effect: |tr_M(⁴He)| 0.4185152019887448 → 0.3471618181878358, −17.0 %.
   The interface census changes with it, {positive 2, negative 1,
   averaged 0} → {positive 1, negative 1, averaged 1}, which is the
   whole difference: the p-n interface stops being counted as a plain
   positive crossing.

## Why this is the canonical path

- The disjoint-product word in the legacy `atomic_tr_m_helium4.py`
  (4 disjoint 3-strand clusters on H_12) FAILS the Schur-Weyl
  identity `Σ_λ y_λ χ^λ = tr_M` by factor ~5 (per deuteron
  evidence in `rho_k_h3a_refinement.py` P3').
- The canonical word `atom_braid_word_3A(2,2)` has 47 crossings with
  3 interfaces (pp at gen 2, pn at gen 5, nn at gen 8). The closed
  form sums these as Markov-axiom factors per Phase 5c.1.
- Phase 5l completes the picture: the constit-side disjoint product
  `tr_M(𝓑_K^vac) = tr_M(𝓑_p)^Z · tr_M(𝓑_n)^N`.

## Performance

| script | wall (⁴He) |
|---|---:|
| Legacy `atomic_tr_m_helium4.py` (slow path) | ~1645 s |
| This script (closed form) | ~0.5 s |

22,690,901× speedup per Phase 5q witness.

## Reference

- `closed_form_tau_M.py` (the shared utility)
- `closed_form_tau_M_verification_phase5q.py` (validation witness)
- `tr_m_wenzl_bridge_mpfr.py` (H_3 baseline via Wenzl bridge)
- `docs/audits/2026-05-25-phase5q-closed-form-reconciliation.md`
- `docs/audits/AUDIT-DEEP-2026-05.md` §3.3a (legacy disjoint-product
  audit that recommended this migration)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from closed_form_tau_M import (  # noqa: E402
    closed_form_tau_M, compute_tau_M_nucleon_H3, hecke_h, interface_census,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    # Construct WitnessBuilder FIRST so its captured start_time spans
    # the full computation (per Copilot PR #1266 review discipline).
    w = WitnessBuilder(
        "atomic-tr-m-helium4-canonical",
        engine="python+mpmath",
    )
    w.set_description(
        "Canonical |tr_M(⁴He)| via Phase 5q closed form: "
        "tr_M(𝓑_⁴He) = tau_p² · tau_n² · ∏_i f_i(q) where f_i ∈ "
        "{positive=z, negative=z-h, averaged_weighted=z-h(1/2-δ/4)} "
        "per interface (canonical colour-weighted p-n, owner ruling R3). "
        "Replaces the deprecated disjoint-product witness "
        "atomic-tr-m-helium4.witness.json (PR #564 audit). NOTE the "
        "Phase 5q empirical slow-path agreement (1e-49) was measured in "
        "the convention-C, plain-σ frame and does NOT validate this "
        "value — see data.cross_check_status."
    )
    set_compute_dps(50)

    print("=" * 78)
    print("Canonical |tr_M(⁴He)| via Phase 5q closed form")
    print("=" * 78)

    q_str = Q_50_DIGIT_STR
    q_val = mp.mpf(q_str)
    print(f"\n  q_0 = {q_str}")

    # Compute H_3 baseline traces for proton and neutron via the
    # centralised compute_tau_M_nucleon_H3 helper. This uses the
    # canonical_braid_marshalling pipeline. NOTE these H_3 traces are
    # CONVENTION-INDEPENDENT: `compute_tau_M_nucleon_H3` takes no
    # `pn_convention` argument, because a single nucleon has no p-n
    # interface for one to apply to. The convention enters only in the
    # ⁴He interface product below. The comment here used to justify the
    # file's `chi_lambda_braid` by appeal to these traces "matching at
    # machine precision", which cannot be a reason for anything: there
    # is nothing here for a p-n convention to change.
    t0 = time.perf_counter()
    print("\n[1/3] Computing tau_p via compute_tau_M_nucleon_H3 (50 dps)...")
    tau_p = compute_tau_M_nucleon_H3("p", q_val, dps=50)
    print(f"      tau_p = {tau_p}")

    print("\n[2/3] Computing tau_n via compute_tau_M_nucleon_H3 (50 dps)...")
    tau_n = compute_tau_M_nucleon_H3("n", q_val, dps=50)
    print(f"      tau_n = {tau_n}")
    t_h3 = time.perf_counter() - t0

    # Apply the Phase 5q closed form for ⁴He (Z=2, N=2)
    print("\n[3/3] Applying closed form: tr_M(𝓑_⁴He) = "
          "tau_p² · tau_n² · ∏_i f_i(q)")
    t1 = time.perf_counter()
    tau_4he = closed_form_tau_M(
        Z=2, N=2, q=q_val,
        tau_M_proton_H3=tau_p, tau_M_neutron_H3=tau_n,
        pn_convention="bring_color_weighted",
    )
    t_closed = time.perf_counter() - t1

    # |tr_M| is what downstream binding consumers want
    abs_tau_4he = mp.fabs(tau_4he)
    interfaces = interface_census(2, 2, pn_convention="bring_color_weighted")

    print(f"\n      tr_M(𝓑_⁴He) = {tau_4he}")
    print(f"      |tr_M(𝓑_⁴He)| = {abs_tau_4he}")
    print(f"\n      interface census: {interfaces}")
    print(f"\n      wall time (H_3 baseline):     {t_h3:.4f}s")
    print(f"      wall time (closed form ⁴He):   {t_closed:.6f}s")
    print(f"      total:                          {t_h3 + t_closed:.4f}s")

    # Comparison vs the deprecated disjoint-product witness
    legacy_witness = _pb.witness_path("atomic-tr-m-helium4.witness.json", HERE)
    if legacy_witness.exists():
        import json
        with open(legacy_witness, encoding="utf-8") as f:
            legacy = json.load(f)
        if "data" in legacy:
            for k in ("abs_tr_m", "abs_tr_M_helium4", "trM_atom",
                      "tr_M_value"):
                if k in legacy["data"]:
                    print(f"\n  Legacy disjoint-product value ({k} from "
                          f"atomic-tr-m-helium4.witness.json):")
                    print(f"    {legacy['data'][k]}")
                    print(f"  (DEPRECATED — disjoint product fails "
                          f"Schur-Weyl identity per PR #564)")
                    break

    # Witness
    w.add_parameter("q_0", q_str)
    w.add_parameter("Z", 2)
    w.add_parameter("N", 2)
    w.add_parameter("A", 4)
    w.add_parameter("pn_convention", "bring_color_weighted")
    w.add_parameter("dps", 50)
    w.add_data("tau_p_str", str(tau_p))
    w.add_data("tau_n_str", str(tau_n))
    w.add_data("tau_4he_str", str(tau_4he))
    w.add_data("abs_tau_4he_str", str(abs_tau_4he))
    w.add_data("interface_census", interfaces)
    w.add_data("wall_seconds", {
        "h3_baseline": t_h3,
        "closed_form_4he": t_closed,
        "total": t_h3 + t_closed,
    })
    w.add_data("supersedes", {
        "witness": "atomic-tr-m-helium4.witness.json",
        "reason": ("disjoint-product extension on H_12 fails the "
                   "Schur-Weyl identity Σ_λ y_λ χ^λ = tr_M by ~5x "
                   "per PR #564 audit; this canonical-word closed-form "
                   "path is the canonical replacement. (The '1e-49 vs the "
                   "empirical slow path' agreement that used to be quoted "
                   "here is convention-C / plain-σ and is not a check on "
                   "this value — see cross_check_status.)"),
    })

    # ── Frame check (replaces a stale cross-convention comparison) ──
    #
    # This assertion USED TO read expected=0.15, tolerance=0.1, sourced from
    # the Phase 5q witness value 0.1538719675. That number is
    # **convention-C, plain-σ**: every one of that witness's four interface
    # ratios reproduces z_C = √q/(q+1) to ~1e-9 (the residual being the
    # muon→proton re-pin), e.g. ⁴He {pos 2, neg 1} obs 0.0723678572 vs
    # z_C²(z_C−h) = 0.0723678631. Its H_3 inputs are stale too
    # (tau_p 1.2204 there vs 1.3216 here). So the assertion compared this
    # script's output across TWO convention changes, and it has been
    # `passed: false` on main since the convention-D migration — silently,
    # because nothing gates on the flag. It was already red before the R3
    # colour-weighting flip; that flip did not break it.
    #
    # What replaces it is NOT a self-pin to the new value (that would be a
    # tautology, and re-anchoring a red check to whatever the code now
    # prints is the "widen the baseline" move the precision directive
    # forbids). It re-derives the interface ratio from q_0 alone, with the
    # convention written out longhand HERE, and compares it to the ratio
    # implied by the numbers this script emits.
    #
    # What it establishes: this witness's value is in the convention-D
    # (z = q³/(q²+1)) frame with the colour-weighted p-n interface
    # z − h(1/2 − δ/4). A regression of `markov_z` to convention C fails it
    # by a factor 2.196; a regression of the p-n interface to plain σ fails
    # it by 1.2055. (Both measured, not estimated; the tolerance is 1e-45.)
    #
    # What it does NOT establish: that the value is right. Two limits worth
    # being explicit about. (i) The constituent H_3 traces CANCEL out of the
    # ratio — tau_4he is constit_part * interface_part and constit_part is
    # exactly tau_p²·tau_n² — so this checks the INTERFACE convention only,
    # and says nothing about tau_p / tau_n. (ii) There is no independent
    # oracle for the value itself; see data.cross_check_status.
    z_d = q_val ** 3 / (q_val ** 2 + 1)          # convention D, longhand
    h_q = q_val - 1 / q_val
    delta = flavor_split_leading(q_val)
    f_pp = z_d                                   # p-p  : σ
    f_pn = z_d - h_q * (mp.mpf(1) / 2 - delta / 4)   # p-n  : colour-weighted
    f_nn = z_d - h_q                             # n-n  : σ⁻¹
    ratio_expected = f_pp * f_pn * f_nn
    ratio_computed = tau_4he / (tau_p ** 2 * tau_n ** 2)

    # Guard the "longhand" claim: the locally-written h must agree with the
    # shared hecke_h. Raised, not asserted, so `python -O` cannot strip it;
    # compared at 1e-45 rather than exactly, so a future dps change cannot
    # hard-fail the producer over a last-ulp difference.
    if mp.fabs(h_q - hecke_h(q_val)) > mp.mpf("1e-45"):
        raise RuntimeError(
            f"hecke_h drifted from the longhand q - 1/q: "
            f"{hecke_h(q_val)} vs {h_q}"
        )

    w.add_data("interface_factors", {
        "pp_positive": str(f_pp),
        "pn_colour_weighted": str(f_pn),
        "nn_negative": str(f_nn),
        "flavour_split_delta": str(delta),
        "product": str(ratio_expected),
    })
    w.add_assertion(
        name="interface_ratio_matches_convention_D_colour_weighted",
        computed=str(ratio_computed),
        expected=str(ratio_expected),
        tolerance="1e-45",
        source=("Re-derived from q_0 in this file: z = q³/(q²+1) "
                "(convention D, owner ruling R1 2026-08-15), h = q - 1/q, "
                "δ = flavor_split_leading(q); interfaces (p-p, p-n, n-n) = "
                "(z, z - h(1/2 - δ/4), z - h) per R3. Pins the frame of the "
                "emitted value; it is NOT an accuracy check — no independent "
                "oracle for |tr_M(⁴He)| exists in this frame, see "
                "data.cross_check_status."),
    )
    w.add_data("cross_check_status", {
        "independent_oracle": "none in the canonical frame",
        "detail": (
            "The empirical slow path in "
            "closed_form_tau_M_verification_phase5q.py is bound to the "
            "chi_lambda_braid convention via marshal_to_chi_lambda_braid, "
            "and its recorded run is convention-C. It therefore validates "
            "the closed form as a 22M×-faster reimplementation of the OLD "
            "MARSHALLING — a check on the machinery, not on the p-n "
            "treatment. Producing a real cross-check needs a "
            "marshal_to_bring_color_weighted slow path, which does not "
            "exist. Until then the value here rests on closed_form_tau_M "
            "plus the frame assertion above."
        ),
        "bean": "qou-cds4",
    })
    w.add_caveat(
        "No independent oracle: the Phase 5q empirical slow-path agreement "
        "is convention-C / plain-σ bound and does not validate this value. "
        "See data.cross_check_status."
    )
    # Lean SDP-uniqueness cross-reference (PR #1537/#1542/#1554
    # wiring, 2026-05-31). Each nucleus's canonical T_w knot
    # operator uniqueness at the empty-constraint SDP level.
    w.add_data("lean_uniqueness_ref", {
        "helium4": "qou:QOU.BraidKnot.helium4_uniqueness_closed",
        "framework_doc":
            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": (
            "These theorems certify T_w uniqueness at the abstract empty-constraint SDP level (PR #1537/#1542 parameterised module). The real per-nucleus SDP (multi-term cost + non-empty constraints) is per-nucleus substantive open work. Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md."
        ),
    })


    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
