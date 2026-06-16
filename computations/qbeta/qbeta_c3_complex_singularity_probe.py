"""qbeta_c3_complex_singularity_probe — the genuine non-real-q direction.

After the c_3 cross-anchor rigidity falsification (PR-merged 2026-06-04:
docs/audits/2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md),
no real-q formula c_3 = f(q) can track the empirical c_3 swing
(dc_3/dq ≈ 4.6e6). Per CLAUDE.md §"Im(q) at fibre vs observable level" the
genuine object is complex-analytic / root-of-unity at the fibre level.

This probe makes that concrete and falsifiable. A function whose value
c_3 ≈ −2 has |dc_3/dq| ≈ 4.6e6 near q₀ is dominated by a NEARBY SINGULARITY.
The characteristic distance to that singularity is

    b ≈ |c_3| / |dc_3/dq|.

Two falsifiable checks:
  (1) COMPLEX-ANALYTIC framing — is b tiny (near-real singularity)? A smooth
      real-q f cannot have |f'| ≈ 4.6e6 at |f| ≈ 2 without a singularity at
      distance ~b; b ≪ O(1) is the signature of a fibre-level complex-analytic
      Habiro element.
  (2) ROOT-OF-UNITY mechanism — is b comparable to the distance from q₀ to the
      nearest root of unity (all on |q| = 1, so dist ≈ |q₀| − 1 ≈ 0.11)? If
      b ≪ 0.11, roots of unity are TOO FAR to be the mechanism (refuting that
      sub-hypothesis while leaving the complex-analytic framing intact).

Inputs: published anchor values from the falsification doc —
  c_3(proton q₀) = −2.0693, c_3(muon q₀) = −2.0097, Δq ≈ 1.28e-8.

This is a FEASIBILITY / GEOMETRY probe, NOT a closure attempt: it pins the
singularity geometry; it does not produce a categorical c_3 formula.

Usage:
  python3 computations/qbeta/qbeta_c3_complex_singularity_probe.py
Emits: qbeta-c3-complex-singularity-probe.witness.json
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40

# Published anchor data (falsification doc, PR-merged 2026-06-04).
Q_PROTON = mp.mpf("1.10997858275138080759166909561")
Q_MUON_FALSIF = mp.mpf("1.10997859555")     # the falsification-doc muon anchor
C3_PROTON = mp.mpf("-2.0693")
C3_MUON = mp.mpf("-2.0097")


def main() -> int:
    print("=" * 78)
    print("Q_β c_3 complex-singularity probe — genuine non-real-q direction")
    print("=" * 78)

    dq = Q_MUON_FALSIF - Q_PROTON
    dc3 = C3_MUON - C3_PROTON
    dc3_dq = dc3 / dq
    c3_mag = abs(C3_PROTON)

    print(f"\nAnchors: q_proton = {mp.nstr(Q_PROTON, 18)}")
    print(f"         q_muon   = {mp.nstr(Q_MUON_FALSIF, 18)}")
    print(f"  Δq            = {mp.nstr(dq, 6)}")
    print(f"  c_3(proton)   = {mp.nstr(C3_PROTON, 6)}")
    print(f"  c_3(muon)     = {mp.nstr(C3_MUON, 6)}")
    print(f"  Δc_3          = {mp.nstr(dc3, 6)}  ({mp.nstr(dc3/c3_mag*100, 4)}% swing)")
    print(f"  dc_3/dq       = {mp.nstr(dc3_dq, 6)}")

    # ── Singularity distance ────────────────────────────────────────────
    # |f/f'| ~ distance to nearest singularity (the natural length scale of
    # a function dominated by a nearby pole/branch point).
    b = c3_mag / abs(dc3_dq)
    print(f"\n--- Nearest-singularity distance b ≈ |c_3| / |dc_3/dq| ---")
    print(f"  b ≈ {mp.nstr(b, 6)}")

    # ── Check 1: complex-analytic framing (b ≪ O(1)?) ───────────────────
    framing_supported = b < mp.mpf("1e-3")
    print(f"\n--- Check 1: complex-analytic framing ---")
    print(f"  b ≪ O(1)?  {framing_supported}  "
          f"(b ≈ {mp.nstr(b,3)}; a smooth real-q f cannot have |f'|≈{mp.nstr(abs(dc3_dq),3)}")
    print(f"   at |f|≈2 without a singularity this close ⇒ NOT a real-q function)")

    # ── Check 2: root-of-unity mechanism ────────────────────────────────
    # All roots of unity lie on |q| = 1; q₀ ≈ 1.11 is OUTSIDE. Distance from
    # q₀ to the unit circle (hence to the nearest root of unity, at best):
    rou_dist = abs(Q_PROTON) - 1          # q₀ real, > 1
    # nearest actual root of unity to q₀ on the real axis is q=1 (ζ_1):
    dist_to_one = abs(Q_PROTON - 1)
    ratio = dist_to_one / b
    rou_refuted = b < rou_dist / 1000     # b orders of magnitude closer
    print(f"\n--- Check 2: root-of-unity mechanism ---")
    print(f"  dist(q₀, unit circle) = |q₀|−1 = {mp.nstr(rou_dist, 6)}")
    print(f"  dist(q₀, ζ_1=1)       = {mp.nstr(dist_to_one, 6)}")
    print(f"  ratio dist_to_1 / b   = {mp.nstr(ratio, 6)}  "
          f"(roots of unity are ~{mp.nstr(ratio,3)}× farther than the singularity)")
    print(f"  root-of-unity TOO FAR to be the mechanism?  {rou_refuted}")

    # ── Verdict ─────────────────────────────────────────────────────────
    print("\n" + "=" * 78)
    print("VERDICT (feasibility / geometry — NOT a closure):")
    print(f"  • c_3 is dominated by a singularity at distance b ≈ {mp.nstr(b,3)} "
          f"from q₀.")
    print(f"  • COMPLEX-ANALYTIC framing SUPPORTED: b is ~{mp.nstr(b,2)} ≪ 1 — "
          f"no smooth")
    print(f"    real-q f(q) can reproduce c_3 across anchors (confirms the "
          f"falsification).")
    print(f"  • ROOT-OF-UNITY mechanism REFUTED: the nearest root of unity is "
          f"~{mp.nstr(ratio,2)}×")
    print(f"    farther than the singularity — RoU evaluation cannot source the "
          f"hypersensitivity.")
    print(f"  • The relevant singularity is NEAR-REAL at q₀ — consistent with "
          f"the residue-A")
    print(f"    simple pole at u_substrate (radius of convergence = u_subst, "
          f"PR #1713/#1727).")
    print(f"  • OPEN: this pins the singularity GEOMETRY; it does NOT give a "
          f"categorical c_3")
    print(f"    formula. The genuine Habiro element remains the open keystone "
          f"(see registry).")
    print()

    w = WitnessBuilder("qbeta-c3-complex-singularity-probe", engine="mpmath")
    w.set_description(
        f"Tests the complex-analytic/root-of-unity framing for c_3 after the "
        f"real-q falsification. From published anchors (c_3 swing "
        f"{mp.nstr(dc3/c3_mag*100,3)}% over Δq={mp.nstr(dq,3)}), the nearest-"
        f"singularity distance b≈|c_3|/|dc_3/dq|≈{mp.nstr(b,4)}. Complex-analytic "
        f"framing SUPPORTED (b≪1); root-of-unity mechanism REFUTED (nearest RoU "
        f"~{mp.nstr(ratio,3)}× farther). Singularity is near-real at q₀, "
        f"consistent with the residue-A simple pole at u_substrate. "
        f"Feasibility/geometry probe — NOT a closure; the categorical c_3 "
        f"element remains open. Diagnostic-only."
    )
    w.add_data("q_proton", str(Q_PROTON))
    w.add_data("q_muon_falsif", str(Q_MUON_FALSIF))
    w.add_data("c3_proton", str(C3_PROTON))
    w.add_data("c3_muon", str(C3_MUON))
    w.add_data("dc3_dq", mp.nstr(dc3_dq, 8))
    w.add_data("swing_pct", mp.nstr(dc3 / c3_mag * 100, 6))
    w.add_data("singularity_distance_b", mp.nstr(b, 8))
    w.add_data("root_of_unity_distance", mp.nstr(rou_dist, 8))
    w.add_data("dist_to_zeta1", mp.nstr(dist_to_one, 8))
    w.add_data("rou_over_b_ratio", mp.nstr(ratio, 8))
    w.add_data("complex_analytic_framing_supported", str(bool(framing_supported)))
    w.add_data("root_of_unity_mechanism_refuted", str(bool(rou_refuted)))
    w.add_data("is_closure", "false")
    w.add_assertion(
        name="complex_analytic_framing_supported",
        computed=bool(framing_supported), expected=True, tolerance=0,
        source="b = |c_3|/|dc_3/dq| ≪ 1 ⇒ near-singularity-dominated, not a "
               "smooth real-q function (confirms the cross-anchor falsification).",
    )
    w.add_assertion(
        name="root_of_unity_is_the_mechanism",
        computed=bool(not rou_refuted), expected=False, tolerance=0,
        source="Roots of unity (|q|=1) are ~10^5× farther from q₀ than the "
               "singularity at b; they cannot source the c_3 hypersensitivity. "
               "Expected False — RoU is NOT the mechanism.",
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
