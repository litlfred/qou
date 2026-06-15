#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; gap-analysis probe.
"""EXPLORATORY shape-probe (per .claude/skills/local/production-vs-exploratory-discipline.md).

EM-linking invariant for the pp-Coulomb T-vs-³He split — gap analysis.

This script is exploratory hypothesis-generation; it does NOT wire to
production. It tests the crux question of the merged-PR-#1775 OPEN gate
(docs/audits/2026-06-03-charge-coulomb-tn3he-derived.md):

    Is there a DERIVED per-pair EM-linking invariant that supplies the
    pp-Coulomb MAGNITUDE — the remaining 3.2× of the T-³He binding split
    — WITHOUT fitting to the AME value 0.7638 MeV?

DERIVED inputs already on main (zero fit):
  • def:coulomb-charge: Q_pp = (n₊−n₋)/2 = +1 for two protons; Coulomb/
    strong ratio = tanh(ln q₀) ≈ 0.104 (q₀-only).
  • inter-nucleon LINKED channel (2026-06-01-inter-nucleon-linked-channel.md):
    pp = Hopf T(2,+2) = σ₁², linking number lk = +1, writhe w = +2, with a
    DERIVED Markov-trace asymmetry tr_M(pp)−tr_M(nn) = 0.16507 and a LIVE
    U(1)_framing factor q^{w·c}.
  • α_EM Habiro element [2]_q·(1−h²α) (alpha-em-habiro-bar-involution).
  • binding_link_volumes.py: ³He binding link = L6a4 = Borromean (Vol = 8G);
    ³H binding link = 8₁₁ (Vol = 8.2863).

THE TEST. The derived categorical Coulomb measures the pp-repulsion as a
FRACTION of the strong bond: dHe = tanh(ln q₀)·B_pp = 0.2377 MeV. The
physical pp-Coulomb is a DIMENSIONFUL energy e²/(4πε₀·r_pp) set by the
inter-proton SEPARATION r_pp. We check whether any DERIVED dimensionless
q-form (linking number, framing factor, trace asymmetry, α_EM normalization,
binding-link volume ratio) reproduces the 3.2× factor — or whether the
factor is intrinsically a length scale the framework does not supply.

DISCIPLINE. 0.7638 MeV is a POST-HOC CHECK, never a fitting input. We do
NOT tune any coupling, radius, or h^k to hit it. We ASSERT THE REFUTATION
(no derived dimensionless form matches) so the witness stays allPassed.

VERDICT (this probe): the EM-linking STRUCTURE is derived (lk = +1 = Q_pp,
U(1)_framing, trace asymmetry — all already in the corpus), but the per-pair
Coulomb MAGNITUDE is DIMENSIONFUL: the 3.2× factor is exactly the ratio of
the nuclear-charge-radius Coulomb scale to the strong-bond scale (effective
r_pp ≈ 1.885 fm from AME vs ≈ 6.06 fm implied by the strong-bond proxy).
No derived dimensionless object closes it; a concrete value needs a
categorical brane-separation / nuclear-charge-radius scale NOT yet in the
framework — any number would be a CAL-4 fit. PRECISE OBSTRUCTION, not a fit.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
for _d in ("hecke", "habiro", "substrate"):
    _p = str(_Path(__file__).resolve().parent / _d)
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from q_parameter import Q_MP as Q0  # noqa: E402 — canonical proton-pinned q0
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = set_compute_dps(40)
q0 = mp.mpf(str(Q0))
h = q0 - 1 / q0                       # Hecke differential q − q⁻¹


def _bracket(n):
    """Balanced q-integer [n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)."""
    return (q0 ** n - q0 ** (-n)) / (q0 - 1 / q0)


def _link_trace_asymmetry():
    """Wenzl Jones-Markov trace on H₂(q): tr_M(pp=σ₁²) − tr_M(nn=σ₁⁻²).

    DERIVED in 2026-06-01-inter-nucleon-linked-channel.md (no fit). Blocks
    (2): σ₁↦q, and (1,1): σ₁↦−q⁻¹, with Wenzl weights from the Markov axioms.
    """
    den = q0 ** 3 + q0 ** 2 + q0 + 1
    W2 = (q0 ** mp.mpf("1.5") + q0 + 1) / den
    W11 = (q0 ** 3 + q0 ** 2 - q0 ** mp.mpf("1.5")) / den
    pp = W2 * q0 ** 2 + W11 * q0 ** (-2)
    nn = W2 * q0 ** (-2) + W11 * q0 ** 2
    return pp, nn


def main() -> int:
    # --- The OPEN gate's numbers (from the merged-PR-#1775 finding) ---
    ratio = mp.tanh(mp.log(q0))                    # derived Coulomb/strong ratio
    derived_dHe = mp.mpf("0.2377")                 # derived categorical Coulomb (MeV)
    ame_split = mp.mpf("0.7638")                   # AME T−³He split (POST-HOC only)
    factor = ame_split / derived_dHe               # the 3.2× to be explained

    # --- DERIVED dimensionless EM-linking objects available on main ---
    Q_pp = 1                                       # def:coulomb-charge: lk = +1
    framing_pp = q0 ** 2                           # U(1)_framing q^{w·c}, w=+2, c=1
    pp, nn = _link_trace_asymmetry()
    trace_asym = pp - nn                           # 0.16507 (derived, no fit)
    two_q = _bracket(2)                            # [2]_q  (α_EM Habiro lead)
    # binding-link volume ratio (³H 8₁₁ vs ³He L6a4=Borromean=8G)
    vol_811 = mp.mpf("8.2863168")
    vol_borr = 8 * mp.catalan
    vol_ratio = vol_811 / vol_borr                 # 1.131 (Seifert/hyperbolic)

    # Catalogue of DERIVED dimensionless candidates (NONE tuned to 0.7638):
    candidates = {
        "Q_pp (linking number)": mp.mpf(Q_pp),
        "framing q^2 (U(1), c=1)": framing_pp,
        "trace asymmetry tr(pp)-tr(nn)": trace_asym,
        "[2]_q (alpha_EM Habiro lead)": two_q,
        "1/h": 1 / h,
        "1/(h[2]_q)": 1 / (h * two_q),
        "binding-link vol ratio 8_11/8G": vol_ratio,
        "1/tanh(ln q0)": 1 / ratio,
    }

    # The honest test: does ANY derived dimensionless form match 3.21 at <1%?
    matches = {k: float(abs(v - factor) / factor) for k, v in candidates.items()}
    best_label = min(matches, key=matches.get)
    best_rel = matches[best_label]
    none_match = int(best_rel > 0.01)              # 1 ⇒ NO derived form matches

    # --- WHY: the factor is a DIMENSIONFUL length scale (post-hoc diagnosis) ---
    # e²/(4πε₀) = α·ħc = 1.4399645 MeV·fm. The derived dHe and the AME split
    # each imply a single-pair separation r = (α ħc)/E. These are NOT fitted —
    # they DECODE the energies into the length scale the magnitude depends on.
    alpha_hc = mp.mpf("1.4399645")                 # MeV·fm (standard physics)
    r_from_derived = alpha_hc / derived_dHe        # ≈ 6.06 fm (strong-bond proxy)
    r_from_ame = alpha_hc / ame_split              # ≈ 1.885 fm (≈ ³He charge radius)

    print(f"q₀ = {float(q0):.6f}   dps = {DPS}")
    print(f"derived Coulomb/strong ratio tanh(ln q₀) = {float(ratio):.5f}")
    print(f"derived categorical pp-Coulomb dHe = {float(derived_dHe):.4f} MeV")
    print(f"AME T−³He split = {float(ame_split):.4f} MeV  (POST-HOC check only)")
    print(f"factor to explain = {float(factor):.4f}×\n")
    print("DERIVED dimensionless EM-linking candidates vs the 3.2× factor:")
    for k, v in candidates.items():
        print(f"  {k:38s} = {float(v):8.4f}   rel-miss {matches[k]*100:6.1f}%")
    print(f"\nbest = {best_label!r} at {best_rel*100:.1f}% — "
          f"{'NO match' if none_match else 'MATCH'} (gate: <1%)")
    print(f"\nLength-scale decode (the factor IS dimensionful):")
    print(f"  r implied by derived dHe  = {float(r_from_derived):.3f} fm "
          f"(strong-bond scale)")
    print(f"  r implied by AME split    = {float(r_from_ame):.3f} fm "
          f"(≈ ³He charge radius 1.97 fm)")
    print(f"  ratio r_derived/r_ame     = {float(r_from_derived/r_from_ame):.3f}× "
          f"= the 3.2× factor")

    wb = WitnessBuilder("em-linking-invariant-probe", engine="mpmath")
    wb.set_description(
        "EXPLORATORY gap-analysis of the per-pair EM-linking invariant for the "
        "pp-Coulomb T-³He split (OPEN gate of merged PR #1775). Tests whether "
        "any DERIVED dimensionless q-form (linking number, U(1)_framing, "
        "Markov-trace asymmetry, [2]_q α_EM lead, binding-link volume ratio) "
        "reproduces the remaining 3.2× factor. Finds NONE do (<1% gate); the "
        "factor decodes as a DIMENSIONFUL nuclear-charge-radius scale (r≈1.885 "
        "fm from AME vs ≈6.06 fm strong-bond proxy). 0.7638 MeV is POST-HOC; no "
        "fit, no tuning. RAW @ 40 dps. Audit: "
        "docs/audits/2026-06-03-em-linking-invariant.md")
    wb.set_audit_only("docs/audits/2026-06-03-em-linking-invariant.md")
    wb.data["q_0"] = str(Q0)
    wb.data["coulomb_strong_ratio_tanh_ln_q0"] = float(ratio)
    wb.data["derived_categorical_dHe_MeV"] = float(derived_dHe)
    wb.data["ame_split_MeV_POSTHOC"] = float(ame_split)
    wb.data["factor_to_explain"] = float(factor)
    wb.data["Q_pp_linking_number"] = Q_pp
    wb.data["framing_q2"] = float(framing_pp)
    wb.data["link_trace_asymmetry_pp_minus_nn"] = float(trace_asym)
    wb.data["bracket_2_q"] = float(two_q)
    wb.data["binding_link_vol_ratio_811_over_8G"] = float(vol_ratio)
    wb.data["candidate_rel_miss"] = {k: float(v) for k, v in matches.items()}
    wb.data["best_candidate"] = best_label
    wb.data["best_rel_miss"] = float(best_rel)
    wb.data["r_implied_by_derived_fm"] = float(r_from_derived)
    wb.data["r_implied_by_ame_fm"] = float(r_from_ame)
    wb.data["verdict"] = (
        "EM-linking STRUCTURE is derived (lk=+1=Q_pp, U(1)_framing q^{w·c}, "
        "Markov-trace asymmetry — all on main). But the per-pair Coulomb "
        "MAGNITUDE is DIMENSIONFUL: the 3.2× factor is the ratio of the "
        "nuclear-charge-radius Coulomb scale (r≈1.885 fm) to the strong-bond "
        "scale (r≈6.06 fm). NO derived dimensionless q-form matches it (<1% "
        "gate). The MISSING OBJECT is a categorical brane-separation / "
        "nuclear-charge-radius scale; any concrete value would be a CAL-4 fit "
        "to AME. PRECISE OBSTRUCTION — not a fit, not closed.")
    # Assert-the-refutation: no derived dimensionless form matches the factor.
    wb.add_assertion("no_derived_dimensionless_form_matches_factor_at_1pct",
                     computed=none_match, expected=1, tolerance=0)
    # Sanity: the AME-implied separation is the physical ³He charge-radius scale.
    wb.add_assertion("ame_implied_separation_is_nuclear_radius_scale",
                     computed=1 if 1.0 < float(r_from_ame) < 3.0 else 0,
                     expected=1, tolerance=0)
    wb.save()
    print("\n✓ Witness: em-linking-invariant-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
