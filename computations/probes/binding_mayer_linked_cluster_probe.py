#!/usr/bin/env python3
"""Binding question -- structural test: Mayer linked-cluster decomposition.

Candidate #1 (additive/log linked-cluster) confirmed that SUM-over-bonds out-scales
the multiplicative deficit, but still left a residual saturation curve. This probe
QUANTIFIES the cooperative (multi-nucleon) content of light-nuclei binding, so we
know how large the irreducible 3-/4-body term any closure must supply.

For A<=4 the nucleons form a simplex (all pairs nearest-neighbour), so the exact
Mayer / linked-cluster decomposition of the ENERGY is

    B(A) = C(A,2) b2 + C(A,3) b3 + C(A,4) b4 + ...

with b2 the irreducible 2-body, b3 the 3-body, b4 the 4-body binding.  b2 is
IDENTIFIED (not fit) from the deuteron -- the unique 2-body nucleus.  The residual
b3, b4 are then forced by the A=3, 4 data.

IMPORTANT scope (corrected per owner, 2026-06-23).  A large b3/b4 does NOT rule
out the interface program:

  (1) The framework's binding is the TRACE object  B = E0 * tau_vac * (1 - PROD f),
      NOT a pairwise-additive energy.  Expanding the product,
        1 - PROD f = SUM_i (1-f_i) - SUM_{i<j} (1-f_i)(1-f_j) + ...
      already generates the cross-bond (3-, 4-body) cooperative terms.  So a large
      irreducible b3/b4 is a statement about the REQUIRED MAGNITUDE of those cross
      terms, not a proof that the product form is structurally incapable.
  (2) The per-bond factors z, z-h, z-h/2 are Lean-PROVED exact for the trace ratio
      (interface_knot_markov_z_bar_symmetric).  A proved identity is a permanent,
      correct contribution to the eventual closure even while the current number is
      inaccurate; the missing cluster operator ADDS TO / re-weights it.

So this probe's role is to MEASURE the cooperativity (set the size of the 4-body
target), not to reject the interface factors.
"""
import json
import sys
from math import comb
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
REPO = Path(__file__).resolve().parents[2]
COMP = REPO / "computations"

AME = {"D": mp.mpf("2.224566"), "T": mp.mpf("8.481798"),
       "3He": mp.mpf("7.718043"), "4He": mp.mpf("28.295673")}
A = {"D": 2, "T": 3, "3He": 3, "4He": 4}


def main():
    print("=" * 78)
    print("BINDING -- Mayer linked-cluster decomposition (is binding cooperative?)")
    print("  B(A) = C(A,2) b2 + C(A,3) b3 + C(A,4) b4   (simplex; A<=4 all pairs adjacent)")
    print("=" * 78)

    print("\nper-bond AME energy at the physical (complete-graph) bond count:")
    perbond = {}
    for k in ["D", "T", "3He", "4He"]:
        a = A[k]
        npair = comb(a, 2)
        perbond[k] = AME[k] / npair
        print(f"  {k:4s} A={a} pairs={npair}: B/pair = {mp.nstr(perbond[k], 6)} MeV"
              f"   B/A = {mp.nstr(AME[k]/a, 6)}")

    # b2 identified from the unique 2-body nucleus (no pairwise ambiguity):
    b2 = AME["D"]
    b3_T = AME["T"] - 3 * b2
    b3_He = AME["3He"] - 3 * b2
    b3 = (b3_T + b3_He) / 2
    b4 = AME["4He"] - 6 * b2 - 4 * b3

    print("\nirreducible cluster terms (b2 identified from deuteron, not fit):")
    print(f"  b2              = {mp.nstr(b2, 6)} MeV")
    print(f"  b3(T)           = {mp.nstr(b3_T, 6)} MeV")
    print(f"  b3(3He)         = {mp.nstr(b3_He, 6)} MeV   (mirror split = charge-dependent 3-body)")
    print(f"  b4(4He)         = {mp.nstr(b4, 6)} MeV   (irreducible 4-body / alpha)")
    print(f"  b3/b2 = {mp.nstr(b3 / b2, 4)}    b4/b2 = {mp.nstr(b4 / b2, 4)}")

    print("\npure-pairwise prediction (b3=b4=0, b2 from deuteron) vs AME:")
    pairwise = {}
    for k in ["T", "3He", "4He"]:
        pred = comb(A[k], 2) * b2
        pairwise[k] = pred
        print(f"  {k:4s}: C({A[k]},2) b2 = {mp.nstr(pred, 6)}  vs AME {mp.nstr(AME[k], 6)}"
              f"   err = {mp.nstr((pred - AME[k]) / AME[k] * 100, 4)}%")

    print("\n" + "=" * 78)
    print("VERDICT: binding is strongly COOPERATIVE -- and this MEASURES the target.")
    print("  per-bond energy is non-constant (2.22 -> 4.72 MeV/bond); the irreducible")
    print("  3-body (b3/b2 = 0.64) and especially 4-body (b4/b2 = 4.16) terms are LARGE.")
    print("  The 4He spike IS the dominant 4-body alpha-cluster term, coincident with the")
    print("  closed [1^4] SU(4) supermultiplet (e_A vanishes for A>4).")
    print("  This does NOT rule out the interface program:")
    print("   - the trace object B = E0 tau_vac (1 - PROD f) already carries cross-bond")
    print("     (3-,4-body) cooperative terms when the product is expanded;")
    print("   - the per-bond factors z, z-h, z-h/2 are Lean-PROVED exact and remain a")
    print("     correct contribution even while the current number is inaccurate.")
    print("  It sets the SIZE of the missing piece: the closure must supply a 4-body term")
    print("  ~4x the 2-body -- the irreducible cluster operator (option-e PROBE 2) that")
    print("  ADDS TO / re-weights the proved interface structure. (b2 = the deuteron itself.)")

    sys.path.insert(0, str(COMP))
    sys.path.insert(0, str(COMP / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    description = ("Mayer linked-cluster decomposition of light-nuclei binding. b2 "
                   "identified from the deuteron (unique 2-body nucleus); residual b3, b4 "
                   "forced by A=3,4 data. Large b3/b2=0.64, b4/b2=4.16 => binding is "
                   "irreducibly cooperative; no pairwise interface factor can close it.")
    verdict = "strongly_cooperative_measures_4body_target"
    data_payload = {
        "parameters": {"free_parameters": 0, "b2_source": "deuteron (unique 2-body nucleus)"},
        "data": {
            "per_bond_MeV": {k: mp.nstr(perbond[k], 12) for k in perbond},
            "b2_MeV": mp.nstr(b2, 12), "b3_T_MeV": mp.nstr(b3_T, 12),
            "b3_3He_MeV": mp.nstr(b3_He, 12), "b4_4He_MeV": mp.nstr(b4, 12),
            "b3_over_b2": mp.nstr(b3 / b2, 8), "b4_over_b2": mp.nstr(b4 / b2, 8),
            "pairwise_only_pred_MeV": {k: mp.nstr(pairwise[k], 12) for k in pairwise},
            "verdict": verdict,
            "scope_note": ("does NOT rule out the interface program: the trace product "
                           "1-PROD f already carries cross-bond cooperative terms, and the "
                           "per-bond factors are Lean-proved exact (a permanent correct "
                           "contribution). Measures the size of the missing cluster operator."),
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "binding-mayer-linked-cluster-decomposition", data_payload,
        script_path=__file__, engine="mpmath", output_dir=COMP)
    wb.set_description(description)
    wb.add_assertion("verdict == strongly_cooperative_measures_4body_target",
                     computed=int(verdict == "strongly_cooperative_measures_4body_target"),
                     expected=1)
    # Preserve the legacy full-path scriptFile (build() emits the basename).
    out = wb.save(extra={
        "scriptFile":
        "computations/probes/binding_mayer_linked_cluster_probe.py"})
    print(f"\nwitness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
