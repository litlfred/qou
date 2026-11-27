#!/usr/bin/env python3
"""Try to derive m_s/m_d = 2[3]_q[4]_q − 1 from torus-knot invariants.

The merged #1436 reduction: m_K²/m_π² = [3]_q[4]_q (GMOR) ⟹ (isospin-
symmetric) m_s/m_d = 2[3]_q[4]_q − 1 ≈ 24. The open piece: derive
m_s/m_d from the knot/generation assignment.

Generation map (knot-particle-generation-table-data.md):
  gen-1 (d): T(2,3) trefoil  (3 crossings, genus 1)
  gen-2 (s): T(2,5) cinquefoil (5 crossings, genus 2)

CRITICAL TENSION: both leptons AND quarks are gen-2/gen-1, but
  m_μ/m_e ≈ 206.77   (lepton, = Vol(4₁)/ℏ²)
  m_s/m_d ≈ 17–22     (quark, scheme-dependent)
So the quark ratio is NOT the bare generation-knot ratio — quark
masses are confinement-dressed. This probe tests whether 2[3]_q[4]_q−1
is (a) a bare torus-knot invariant ratio, or (b) confinement-specific.
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP, vol_4_1_at  # noqa: E402


def q_int(k, q):
    return (q**k - q**(-k)) / (q - 1/q)


def jones_T2n(n, q):
    """Jones polynomial of the (2,n) torus knot (n odd), in the
    variable q (Skein: σ_i − σ_i^{-1} = (q − q^{-1})). Closed form:
      V_{T(2,n)} = (-1)^{(n-1)} q^{(n-1)} (1 - q^{2(n+1)} ... )
    Use the standard normalized form via the 2-strand Markov trace of
    σ₁^n. We use the textbook closed form (Lickorish):
      V(T(2,n)) = -q^{-(n-1)} (q^{2n} + (-1)^n) / (q^2 + 1)  ...
    Here we use the q-integer-friendly Markov trace value instead."""
    # Markov trace of σ₁^n in H₂(q): eigenvalues of σ₁ are q and −q⁻¹.
    # tr_M(σ₁^n) = y₂·(q^n) + y₁'·((−q⁻¹)^n) with Jones-Wenzl weights.
    # For the unnormalised invariant we use the eigenvalue power sum,
    # which is the natural "spectral mass" of the closed braid.
    return q**n + (-q**(-1))**n  # power-sum of σ₁ eigenvalues (n-th)


def main():
    _t0 = time.perf_counter()
    set_compute_dps()
    q = Q_MP
    eps = ((q - 1)/q)**2
    vol = vol_4_1_at(mp.mp.dps)

    target = 2*q_int(3, q)*q_int(4, q) - 1   # = m_s/m_d from GMOR fusion
    ms_md_pdg = mp.mpf("20.0")               # PDG ballpark (17–22)

    print("=" * 70)
    print("  Derive m_s/m_d = 2[3]_q[4]_q − 1 from torus-knot invariants?")
    print("=" * 70)
    print()
    print(f"  Target (GMOR fusion): 2[3]_q[4]_q − 1 = {float(target):.4f}")
    print(f"  PDG m_s/m_d ≈ 17–22 (scheme-dependent)")
    print(f"  Lepton gen-2/gen-1: m_μ/m_e = Vol(4₁)/ℏ² = {float(vol/eps):.2f}")
    print()

    # ---------------------------------------------------------------
    # The tension: if quark mass ratio = bare generation-knot ratio,
    # it should match the LEPTON ratio (207). It doesn't (20). So
    # quark masses are confinement-dressed. Quantify.
    # ---------------------------------------------------------------
    print("-" * 70)
    print("  Is m_s/m_d the bare generation-knot ratio? (NO)")
    print("-" * 70)
    print()
    print(f"  If quarks used the lepton mechanism (Vol(4₁)/ℏ²), m_s/m_d")
    print(f"  would be ~{float(vol/eps):.0f} — but it's ~20. Factor "
          f"{float(vol/eps)/20:.1f}× smaller.")
    print(f"  ⟹ quark masses are confinement-dressed, NOT bare knots.")
    print()

    # ---------------------------------------------------------------
    # Candidate torus-knot invariant ratios T(2,5)/T(2,3):
    # ---------------------------------------------------------------
    print("-" * 70)
    print("  Torus-knot invariant ratios T(2,5)/T(2,3) vs target 24:")
    print("-" * 70)
    print()
    cands = [
        ("crossings 5/3", mp.mpf(5)/3),
        ("genus 2/1", mp.mpf(2)/1),
        ("[5]_q/[3]_q", q_int(5, q)/q_int(3, q)),
        ("[5]_q²/[3]_q²", (q_int(5, q)/q_int(3, q))**2),
        ("|J(T2,5)/J(T2,3)|", abs(jones_T2n(5, q)/jones_T2n(3, q))),
        ("[5]_q·[3]_q", q_int(5, q)*q_int(3, q)),
        ("[5]_q²/[2]_q", q_int(5, q)**2/q_int(2, q)),
        ("[15]_q/[3]_q...", q_int(15, q)/q_int(3, q)),
    ]
    best = None
    for name, val in cands:
        m = abs(float(val/target - 1))*100
        if best is None or m < best[2]:
            best = (name, val, m)
        print(f"    {name:<22s} = {float(val):>9.4f}  ({m:.1f}% vs 24)")
    print()
    print(f"  Best torus-knot candidate: {best[0]} = {float(best[1]):.3f} ({best[2]:.1f}%)")
    print()

    # ---------------------------------------------------------------
    # The honest structural reading of 2[3]_q[4]_q − 1
    # ---------------------------------------------------------------
    print("-" * 70)
    print("  What IS 2[3]_q[4]_q − 1 structurally?")
    print("-" * 70)
    print()
    # 2[3][4]−1 = 2([2]+[4]+[6]) − 1. At q→1: 2·12 − 1 = 23.
    cl = 2*3*4 - 1
    print(f"  Classical limit (q→1): 2·3·4 − 1 = {cl}")
    print(f"  = 2·(crossings_d · crossings_s_fusion) − 1, the doubled")
    print(f"    pion-fusion channel minus the self-term. This is a MESON")
    print(f"    (H₃, 3-strand) fusion quantity, NOT a single-quark knot")
    print(f"    invariant — consistent with m_s/m_d emerging from the")
    print(f"    qq̄ BOUND STATE (confinement), not bare quark knots.")
    print()

    # ---------------------------------------------------------------
    print("=" * 70)
    print("  VERDICT")
    print("=" * 70)
    print()
    print(f"  m_s/m_d = 2[3]_q[4]_q − 1 does NOT reduce to a clean bare")
    print(f"  torus-knot ratio T(2,5)/T(2,3) (best {best[2]:.0f}% miss).")
    print(f"  This is EXPECTED and informative: the lepton gen-2/gen-1")
    print(f"  ratio is {float(vol/eps):.0f} (bare knot, Vol(4₁)/ℏ²), but the")
    print(f"  quark ratio is ~20 — quark masses are CONFINEMENT-DRESSED.")
    print(f"  So 2[3]_q[4]_q−1 is a property of the qq̄ MESON fusion (H₃),")
    print(f"  not of the isolated quark knots. The honest status: the")
    print(f"  m_K²/m_π² = [3]_q[4]_q fusion (#1436) is the derived-candidate;")
    print(f"  'm_s/m_d as a bare-knot ratio' is the WRONG target — quark")
    print(f"  masses live in the confined (meson) sector, which is exactly")
    print(f"  what the [3]_q[4]_q H₃-fusion already encodes.")
    print()

    w = WitnessBuilder("derive-ms-md-torus-knot", engine="mpmath", start_time=_t0)
    w.set_description(
        "Tests whether m_s/m_d = 2[3]_q[4]_q−1 (≈24) derives from a bare "
        "torus-knot ratio T(2,5)/T(2,3). It does NOT (best candidate "
        f"{best[2]:.0f}% off). Informative negative: the lepton gen-2/gen-1 "
        f"ratio is Vol(4₁)/ℏ²≈207 (bare knot) but the quark ratio is ~20 — "
        "quark masses are confinement-dressed, so 2[3]_q[4]_q−1 is a qq̄ "
        "meson-fusion (H₃) property, not an isolated-quark-knot invariant. "
        "The [3]_q[4]_q fusion (#1436) already encodes the confined sector."
    )
    w.set_audit_only("docs/audits/2026-05-28-meson-mass-ratio-derived-vs-fitted.md")
    w.add_data("target_2x3q4q_minus1", float(target))
    w.add_data("lepton_gen2_gen1_ratio", float(vol/eps))
    w.add_data("quark_ms_md_pdg", 20.0)
    w.add_data("best_torus_knot_candidate", best[0])
    w.add_data("best_torus_knot_miss_pct", best[2])
    w.add_data("conclusion", "m_s/m_d is confinement-dressed (meson sector), not a bare-knot ratio")
    w.add_assertion("bare_knot_ratio_does_not_match",
                    computed=1 if best[2] > 5 else 0,
                    expected=1, tolerance=0,
                    source="no bare T(2,5)/T(2,3) invariant ratio gives 2[3]_q[4]_q−1 to <5%")
    w.add_assertion("lepton_quark_ratio_tension",
                    computed=1 if float(vol/eps)/20 > 5 else 0,
                    expected=1, tolerance=0,
                    source="lepton gen-2/1 ratio (207) ≫ quark (20): confinement dressing")
    print(f"  Witness: {w.save()}")


if __name__ == "__main__":
    main()
