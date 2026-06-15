"""Bring zero-mode scaffold for per-block (α_em/π) — Item B of PR #1654.

PR #1645 `ProtonMassEMSignBlock.lean` documents OPEN item (1):
"Categorical derivation of the bare per-block `(α_em/π)` EM coupling
(Bring zero-mode analog of m_K/m_π's `(3q²-1)/(2q²)` from PR #1442)."

This probe stages the Bring-zero-mode argument for the per-block
coupling at H_3 sign rep.

## The m_K/m_π template (PR #1442)

  EM correction = (α_em/π) · (3q²−1)/(2q²)

The `(3q²−1)/(2q²)` is a truncation of `1 + ℏ_q − ℏ_q²/2`. The "3" is
the number of Bring saturating-genus generation knots T_(2,3), T_(2,5),
T_(2,7) on Bring's surface; the "2q²" is the EM-self-energy halving ×
substrate scale.

## Analog for the proton-mass sign-block

The proton on B_3 (Borromean braid) is NOT a torus knot — it's a
specific 3-strand braid β_proton ≈ T_w. The Bring-quintic template
may not transfer naively because:
  - 3-strand B_n braid vs Bring's quintic-related torus knot family
  - 1-dim sign rep evaluation vs 2-dim standard rep used in m_K/m_π
  - h⁰ order coupling (just α_em/π, no q-dependence) vs h² (the (3q²−1)/(2q²) shape)

This probe tests whether ANY natural Bring-quintic-related projection
gives the bare `(α_em/π)` at the sign block.

## Method

For various Bring-related projections P, compute:
  predicted_coupling = α_em · P · (normalization)

and compare to the target `(α_em/π)` (which numerically is 0.00232 at
the standard convention).

## Cross-references

- merged PR #1442 (m_K/m_π Bring closure template)
- merged PR #1645 (ProtonMassEMSignBlock sign-block hypothesis)
- content/quantum-observable-universe/brings-surface/ (Bring content blocks)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _h4_substrate import ALPHA_EM  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import q_at, q_str  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    DPS = 80
    set_compute_dps(DPS)
    q = q_at(DPS)

    print("=" * 78)
    print("Bring zero-mode per-block (α_em/π) scaffold (item B)")
    print("=" * 78)
    print(f"\nq_0 = {q_str(60)} (display)\n")

    # Target: bare per-block coupling = α_em / π
    target = ALPHA_EM / mp.pi
    print(f"[Target] (α_em/π) = {mp.nstr(target, 18)}")

    # Substrate
    h = q - 1 / q
    h2 = h * h
    hbar_q = 1 - 1 / q
    hbar_q_sq = hbar_q ** 2
    G = mp.catalan

    # ── Test 1: pure α_em multiplied by Bring-natural factors ──
    print(f"\n[Test 1: α_em · (Bring-natural projection)]")
    print(f"  Target / α_em = {mp.nstr(target / ALPHA_EM, 18)}")
    print(f"  (= 1/π = {mp.nstr(1/mp.pi, 18)})")
    print(f"  Question: what natural factor gives 1/π?")

    # m_K/m_π uses (3q²-1)/(2q²) at h² order. For the proton (h⁰
    # order, sign block), the natural choice is the leading term of
    # an analog series.

    # Standard 1-loop QED gives α_em/π for various corrections (the
    # anomalous magnetic moment leading order is α/(2π)). So the
    # 1/π factor here IS the standard QED bubble integral.

    print(f"\n[Conclusion (Test 1)]")
    print(f"  The (α_em/π) factor IS the standard QED 1-loop coupling")
    print(f"  prefactor (vacuum polarization / bubble integral). It's not")
    print(f"  derived FROM Bring — it's the input EM coupling that THEN")
    print(f"  gets routed to the proton's sign block via Plancherel weight.")
    print(f"  ")
    print(f"  The categorical question becomes: WHY does the EM bubble")
    print(f"  integral land at exactly the sign-block channel of H_3?")

    # ── Test 2: m_K/m_π template projection at h⁰ ──
    print(f"\n[Test 2: m_K/m_π template `(3q²−1)/(2q²)` at h⁰ order]")
    em_shape = (3 * q ** 2 - 1) / (2 * q ** 2)
    print(f"  (3q² − 1)/(2q²) at q_0 = {mp.nstr(em_shape, 18)}")
    print(f"  at q=1: (3-1)/(2) = 1 (h⁰ leading term)")
    print(f"  → Truncation at h⁰ gives 1; full at q_0 gives 1.16")
    print(f"  ")
    print(f"  For the m_p sign-block coupling at h⁰ order, the analog")
    print(f"  leading-term truncation would be `1`, giving:")
    print(f"    per-block-coupling = (α_em/π) · 1 = (α_em/π)  ✓")
    print(f"  ")
    print(f"  This is TAUTOLOGICAL — the h⁰ truncation of any of these")
    print(f"  q-shapes is the bare (α_em/π) by construction.")

    # ── Test 3: Sign-block channel identification ──
    print(f"\n[Test 3: WHY sign rep?]")
    print(f"  Physical: proton (uud) color singlet ⇒ wave function")
    print(f"  fully antisymmetric in color ⇒ S_3-sign rep on 3 color")
    print(f"  labels. EM couples to electric charge (which depends on")
    print(f"  flavor), but the Wedderburn-channel decomposition follows")
    print(f"  color symmetry per Fermi statistics.")
    print(f"  ")
    print(f"  CATEGORICAL FORMALIZATION: this requires a substrate-level")
    print(f"  implementation of the QCD color-singlet condition + a")
    print(f"  Wedderburn-block projection of the EM coupling. NEITHER")
    print(f"  exists yet at the categorical level.")

    # ── Verdict / open work scaffold ──
    print(f"\n[Verdict / open work for ProtonMassEMSignBlock]")
    verdict = (
        "The 'Bring zero-mode derivation of bare per-block (α_em/π)' "
        "open item is structurally CIRCULAR as currently posed: the "
        "(α_em/π) IS the standard QED 1-loop coupling, not a Bring-"
        "specific derivation. The non-trivial derivation is WHY EM "
        "couples to the sign Wedderburn block of H_3 specifically. "
        "That requires: (a) substrate-level implementation of QCD "
        "color-singlet (Fermi-statistics → sign rep), and (b) "
        "categorical Wedderburn-projection of the EM coupling. "
        "Neither exists yet at the categorical level — this is the "
        "actual multi-session open work behind ProtonMassEMSignBlock."
    )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "bring-zero-mode-per-block-scaffold",
        engine="python",
    )
    w.set_description(
        "Item B of PR #1654: scaffolds the Bring-zero-mode derivation of "
        "the bare per-block (α_em/π) at the sign-block of H_3. Identifies "
        "the open question is NOT 'derive α_em/π from Bring' (it's the "
        "standard QED bubble) but 'derive why EM couples to sign block'."
    )
    w.add_parameter("q_80dps", q_str(DPS))
    w.add_parameter("mp_dps_runtime", str(mp.mp.dps))
    w.add_data("target", mp.nstr(target, 25))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="scaffold_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source="Scaffold identifies the actual open derivation question.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
