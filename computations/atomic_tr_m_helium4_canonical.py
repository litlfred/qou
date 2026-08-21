"""Canonical |tr_M(⁴He)| via Phase 5q closed form (Track C migration).

Replaces the deprecated `atomic_tr_m_helium4.py` (which used the
disjoint-product extension on H_12, documented as non-canonical
per PR #564 audit).

## Pipeline

1. Compute the H_3 traces `tau_p, tau_n` via the Wenzl bridge at 50 dps.
2. Apply the Phase 5q closed form
       tr_M(𝓑_⁴He) = closed_form_tau_M(2, 2, q_0, tau_p, tau_n)
   passing `pn_convention="chi_lambda_braid"` EXPLICITLY (line 117) —
   which Phase 5q verified matches the empirical slow-path tr_M at machine
   precision (1e-49 rel.err — see
   `closed-form-tau-M-verification-phase5q.witness.json`).

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
from closed_form_tau_M import (  # noqa: E402
    closed_form_tau_M, compute_tau_M_nucleon_H3, interface_census,
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
        "{positive=z, negative=z-h, averaged=z-h/2} per interface. "
        "Replaces the deprecated disjoint-product witness "
        "atomic-tr-m-helium4.witness.json (PR #564 audit). 22M× "
        "faster than the empirical slow path; matches the slow path "
        "at machine precision (1e-49 rel.err per Phase 5q witness)."
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
    # canonical_braid_marshalling pipeline (chi_lambda_braid convention)
    # that the Phase 5q witness validates against — matching the
    # `pn_convention="chi_lambda_braid"` passed explicitly below at machine
    # precision.
    #
    # NOT the default. `closed_form_tau_M`'s default is
    # `bring_color_weighted` (closed_form_tau_M.py:245,344,392,495), made
    # canonical by ruling R3. Both prose references here previously called
    # chi_lambda_braid "the default", which was true when written and is
    # not now. The explicit argument at line 117 is therefore LOAD-BEARING:
    # deleting it as redundant would silently switch this file's physics to
    # bring_color_weighted and invalidate the 1e-49 Phase 5q agreement cited
    # above, which was measured under chi_lambda_braid. Bean qou-cds4.
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
        pn_convention="chi_lambda_braid",
    )
    t_closed = time.perf_counter() - t1

    # |tr_M| is what downstream binding consumers want
    abs_tau_4he = mp.fabs(tau_4he)
    interfaces = interface_census(2, 2, pn_convention="chi_lambda_braid")

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
    w.add_parameter("pn_convention", "chi_lambda_braid")
    w.add_parameter("dps", 50)
    w.add_data("tau_p_str", str(tau_p))
    w.add_data("tau_n_str", str(tau_n))
    w.add_data("tau_4he_str", str(tau_4he))
    w.add_data("abs_tau_4he_str", str(abs_tau_4he))
    w.add_data("abs_tau_4he_float", float(abs_tau_4he))
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
                   "path matches the empirical slow path at 1e-49"),
    })

    w.add_assertion(
        name="abs_tau_4he_positive",
        computed=float(abs_tau_4he),
        expected=0.15,  # rough magnitude check from Phase 5q witness
        tolerance=0.1,
        source=("Phase 5q witness: 4He tau_M_closed_form = 0.1538719675... "
                "at q_0, |tr_M| = 0.1539 (sign positive)"),
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
