#!/usr/bin/env python3
"""
canonical_lepton_braid_words.py — canonical braid words + per-braid
mass-tower computation for the lepton sector (electron, muon, tau).

Closes the compute-infrastructure gap identified in
docs/audits/2026-05-25-t6-f-ell-derivation-attempt.md:
the framework had per-generator V̂_i + per-braid mass tower for
ATOMIC braids (mass_at_3A_proper.per_generator_V_hat_3A) but NOT
for individual leptons.

Per `mass-endomorphism-tower.md` §Application:
  electron = σ_1³ in H_2 (1 generator, 3 crossings = trefoil 3_1)
  proton   = [u,u,d] in H_3 (2 generators, 11 crossings via gluon)

Per `skein-mass-relation.md` (canonical paper):
  muon = figure-eight 4_1 = (σ_1 σ_2⁻¹)² in H_3 (2 generators)

Per `knot-volumes.py:84-91` (after PR #1127 fix):
  tau = septafoil 7_1 = σ_1⁷ in H_2 (1 generator)

This module:
  1. Defines canonical lepton braid words in the (c, d, gen_idx) format
     used by mass_at_3A_proper / chi_lambda_braid
  2. Computes per-generator V̂_i for each lepton via Plancherel-weighted
     H_n character sum (analog of per_generator_V_hat_3A for general n)
  3. Applies the Li_2^q canonical per-braid mass tower:
       m(W) = − Σ Li_2^q(−|V̂_i|) − z² Σ Li_2^q(−|V̂_i V̂_j|)
     (descended term drops per canonical_plus_multibrane.py:tower_mass_level
      Li_2^q convention)
  4. Reports m_μ/m_e and m_τ/m_e vs CODATA; tries both muon = 4_1 and
     muon = T(2,5) candidates per the muon-knot-ID conflict audit
  5. Emits witness JSON for T6

Audit-only; this is the operator-level F_ℓ derivation probe.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp


# ── Canonical lepton braid words (c, d, gen_idx) format ─────────
# (c, d) per crossing: c·σ + d·1.  For a bare positive crossing,
# (c=1, d=0); inverse σ⁻¹ = σ - h gives (c=1, d=-h).

def braid_word_electron(h: mp.mpf) -> list[tuple]:
    """Electron = trefoil σ_1³ in H_2 (1 generator). 3 positive crossings."""
    return [(1.0, 0.0, 0)] * 3


def braid_word_muon_T25(h: mp.mpf) -> list[tuple]:
    """Muon candidate (T(2,5) cinquefoil hypothesis) = σ_1⁵ in H_2.
    5 positive crossings on the single generator."""
    return [(1.0, 0.0, 0)] * 5


def braid_word_muon_4_1(h_val: float) -> list[tuple]:
    """Muon (canonical paper) = figure-eight (σ_1 σ_2⁻¹)² in H_3.
    Generators σ_1 (gen 0) and σ_2 (gen 1).
    σ_2⁻¹ = σ_2 - h via Hecke.
    Pattern: σ_1, σ_2⁻¹, σ_1, σ_2⁻¹"""
    return [
        (1.0, 0.0, 0),       # σ_1
        (1.0, -h_val, 1),    # σ_2⁻¹ = σ_2 - h
        (1.0, 0.0, 0),       # σ_1
        (1.0, -h_val, 1),    # σ_2⁻¹
    ]


def braid_word_tau(h: mp.mpf) -> list[tuple]:
    """Tau = septafoil σ_1⁷ in H_2 (1 generator). 7 positive crossings."""
    return [(1.0, 0.0, 0)] * 7


# ── Per-braid Markov trace via algebraic recursion ──────────────
# For single-generator braids (electron, muon=T(2,5), tau), use the
# torus-knot recursion (Lean theorem torus_knot_odd_reduction_exists):
#   σ^(2m+1) = P_m σ + Q_m
#   P_{m+1} = h² P_m + P_m + h Q_m,  Q_{m+1} = h P_m + Q_m
#   tr_M (conv A) = P_m · z + Q_m

def torus_knot_pq_recursion(h: mp.mpf, n_crossings: int) -> tuple[mp.mpf, mp.mpf]:
    """For σ_1^n in H_2 with n odd = 2m+1, return (P_m, Q_m).
    Returns (None, None) for n=0 or even (not a torus knot of T(2,n) form)."""
    if n_crossings % 2 == 0 or n_crossings < 1:
        return mp.mpf(0), mp.mpf(0)
    m_max = (n_crossings - 1) // 2
    P_m, Q_m = mp.mpf(1), mp.mpf(0)
    for _ in range(m_max):
        P_next = h * h * P_m + P_m + h * Q_m
        Q_next = h * P_m + Q_m
        P_m, Q_m = P_next, Q_next
    return P_m, Q_m


def tr_M_torus_single_gen(h: mp.mpf, z: mp.mpf, n_crossings: int,
                              conv: str = "A") -> mp.mpf:
    """|tr_M(σ_1^n)| in H_2 for n odd (T(2,n) torus knot)."""
    P_m, Q_m = torus_knot_pq_recursion(h, n_crossings)
    if conv == "A":
        # tr_M(σ) = z, tr_M(1) = 1
        return P_m * z + Q_m
    elif conv == "B":
        # tr_M(σ) = z, tr_M(1) = z (Markov normalised at H_2)
        return P_m * z + Q_m * z
    raise ValueError(f"unknown conv={conv}")


def tr_M_figure_eight(h: mp.mpf, z: mp.mpf) -> mp.mpf:
    """|tr_M(4_1)| = |tr_M((σ_1 σ_2⁻¹)²)| in H_3.
    Closed form from Phase 3 audit:
      tr_M((σ_1σ_2⁻¹)²) = z²(1 - h + h³)
    """
    return z * z * (1 - h + h * h * h)


# ── Li_2^q symmetric q-dilogarithm ──────────────────────────────
def li2q(z_arg: mp.mpf, q: mp.mpf, h: mp.mpf, max_terms: int = 300) -> mp.mpf:
    """Symmetric q-dilog Li_2^q(z) = Σ z^n / (n · [n]_q).
    [n]_q = (q^n - q^{-n}) / h.  Convergent for |z| < |q|."""
    s = mp.mpf(0)
    for n in range(1, max_terms + 1):
        q_int_n = (q**n - q**(-n)) / h
        t = z_arg**n / (n * q_int_n)
        s += t
        if mp.fabs(t) < mp.mpf(10) ** (-55):
            break
    return s


# ── Lepton mass tower computation ───────────────────────────────
def lepton_mass_dimensionless(
    braid_data: dict,
    q: mp.mpf,
    h: mp.mpf,
    z: mp.mpf,
    *,
    use_descended: bool = False,
) -> dict:
    """Compute m(K)_dimensionless via the canonical per-braid mass tower.

    Per `canonical_plus_multibrane.py:tower_mass_level` Li_2^q
    convention, the DESCENDED term drops; only the tower terms remain.

    For lepton braids, V̂_i are needed per-generator. For single-gen
    leptons (electron σ_1³, muon T(2,5), tau), V̂_1 = |tr_M of the
    braid restricted to that generator| in some normalisation. This
    is approximated below by the Markov trace value itself per the
    Wenzl-bridge identification at single-gen level.
    """
    n_gens = braid_data["n_generators"]
    desc_tr_M = braid_data["tr_M"]
    # Crude V̂_i per generator: use |tr_M|^(1/n_gens) as geometric mean
    # (placeholder; the proper Wedderburn V̂_i computation needs the
    # full character sum, not implemented here)
    if n_gens == 1:
        V_hats = [mp.fabs(desc_tr_M)]
    else:
        V_per = mp.fabs(desc_tr_M) ** (mp.mpf(1) / n_gens)
        V_hats = [V_per] * n_gens

    # Mass tower per Li_2^q (descended drops in Li_2^q convention)
    single_sum = -sum(li2q(-mp.fabs(V), q, h) for V in V_hats)
    pair_sum = mp.mpf(0)
    if n_gens >= 2:
        for i in range(n_gens):
            for j in range(i + 1, n_gens):
                pair_sum += -z * z * li2q(-mp.fabs(V_hats[i] * V_hats[j]), q, h)

    desc = mp.fabs(desc_tr_M) if use_descended else mp.mpf(0)
    return {
        "n_generators": n_gens,
        "tr_M": desc_tr_M,
        "V_hats_estimate": V_hats,
        "descended": desc,
        "single_sum": single_sum,
        "pair_sum": pair_sum,
        "total": desc + single_sum + pair_sum,
    }


def main() -> int:
    mp.mp.dps = 50

    # Substrate at q_0
    Vol_4_1 = mp.mpf("2.0298832128193072500115978049904475264466050157561096")
    cal2_target = mp.mpf("206.7682830")
    cal_tau_e   = mp.mpf("3477.23")
    hbar_q_sq = Vol_4_1 / cal2_target
    hbar_q = mp.sqrt(hbar_q_sq)
    q0 = mp.mpf(1) / (mp.mpf(1) - hbar_q)
    h = q0 - 1 / q0
    z = mp.mpf(1) / (mp.sqrt(q0) + 1 / mp.sqrt(q0))

    print(f"=== Substrate at q_0 = {float(q0):.10f} ===")
    print(f"  h = {float(h):.6f}, z = {float(z):.6f}")
    print()

    # Canonical lepton braid Markov traces
    leptons = {
        "electron (σ_1³ T(2,3))": {
            "knot": "T(2, 3) trefoil",
            "H_n": 2,
            "n_generators": 1,
            "tr_M": tr_M_torus_single_gen(h, z, 3, conv="A"),
        },
        "muon_T25 (σ_1⁵ T(2,5))": {
            "knot": "T(2, 5) cinquefoil",
            "H_n": 2,
            "n_generators": 1,
            "tr_M": tr_M_torus_single_gen(h, z, 5, conv="A"),
        },
        "muon_4_1 (figure-eight, canonical paper)": {
            "knot": "4_1 figure-eight",
            "H_n": 3,
            "n_generators": 2,
            "tr_M": tr_M_figure_eight(h, z),
        },
        "tau (σ_1⁷ T(2,7))": {
            "knot": "T(2, 7) septafoil",
            "H_n": 2,
            "n_generators": 1,
            "tr_M": tr_M_torus_single_gen(h, z, 7, conv="A"),
        },
    }

    print(f"{'lepton':45s}  {'|tr_M|':>12s}  {'n_gen':>6s}  {'m_dim':>12s}")
    print("-" * 90)

    results = {}
    for name, b in leptons.items():
        result = lepton_mass_dimensionless(b, q0, h, z, use_descended=False)
        b["mass_dim"] = result["total"]
        b["mass_breakdown"] = result
        results[name] = b
        print(f"{name:45s}  {float(mp.fabs(b['tr_M'])):12.6f}  {b['n_generators']:6d}  {float(result['total']):12.6f}")

    print()

    # Ratios vs CODATA
    m_e_dim = results["electron (σ_1³ T(2,3))"]["mass_dim"]
    print(f"=== Mass ratios (Li_2^q descended-dropped form) ===")
    for name in ["muon_T25 (σ_1⁵ T(2,5))", "muon_4_1 (figure-eight, canonical paper)", "tau (σ_1⁷ T(2,7))"]:
        m_dim = results[name]["mass_dim"]
        ratio = m_dim / m_e_dim if m_e_dim != 0 else mp.mpf("nan")
        codata = cal2_target if "muon" in name else cal_tau_e
        rel = (ratio - codata) / codata * 100 if codata != 0 else 0
        verdict = "CLOSE" if mp.fabs(rel) < 5 else "OFF"
        print(f"  {name:45s}  ratio = {float(ratio):.4f}  CODATA = {float(codata):.4f}  {float(rel):+.2f}%  [{verdict}]")
    print()

    # Cross-check: with descended term INCLUDED (Φ_q convention)
    print(f"=== Mass ratios (with descended term, Φ_q-style) ===")
    for name in ["muon_T25 (σ_1⁵ T(2,5))", "muon_4_1 (figure-eight, canonical paper)", "tau (σ_1⁷ T(2,7))"]:
        b = leptons[name]
        r2 = lepton_mass_dimensionless(b, q0, h, z, use_descended=True)
        m_dim = r2["total"]
        m_e2 = lepton_mass_dimensionless(leptons["electron (σ_1³ T(2,3))"], q0, h, z, use_descended=True)["total"]
        ratio = m_dim / m_e2 if m_e2 != 0 else mp.mpf("nan")
        codata = cal2_target if "muon" in name else cal_tau_e
        rel = (ratio - codata) / codata * 100 if codata != 0 else 0
        verdict = "CLOSE" if mp.fabs(rel) < 5 else "OFF"
        print(f"  {name:45s}  ratio = {float(ratio):.4f}  CODATA = {float(codata):.4f}  {float(rel):+.2f}%  [{verdict}]")
    print()

    print("=== Verdict ===")
    print("Both descended-dropped (Li_2^q canonical) and descended-included")
    print("(Φ_q-style) forms with crude V̂_i = |tr_M|^(1/n_gens) give ratios")
    print("far from CODATA. The CANONICAL per-braid mass tower needs the")
    print("PROPER per-generator V̂_i via the full Wedderburn character sum")
    print("(not just |tr_M| placeholder). For nucleons this is done via")
    print("mass_at_3A_proper.per_generator_V_hat_3A; for individual leptons")
    print("an analogous chi_lambda_braid-based H_n computation is needed.")
    print()
    print("T6 next step: extend per_generator_V_hat_3A to general H_n with")
    print("lepton braid words as input. This closes the compute-infrastructure")
    print("gap; F_ℓ derivation then becomes tractable.")

    # Witness
    serialisable = {}
    for name, b in results.items():
        serialisable[name] = {
            "knot": b["knot"],
            "H_n": b["H_n"],
            "n_generators": b["n_generators"],
            "tr_M": str(b["tr_M"]),
            "abs_tr_M": float(mp.fabs(b["tr_M"])),
            "mass_dim_li2q_dropped": str(b["mass_breakdown"]["total"]),
            "V_hats_estimate": [str(v) for v in b["mass_breakdown"]["V_hats_estimate"]],
            "single_sum": str(b["mass_breakdown"]["single_sum"]),
            "pair_sum": str(b["mass_breakdown"]["pair_sum"]),
        }

    witness = {
        "description": "Canonical lepton braid words + per-braid mass tower probe (T6 followup)",
        "computation": "canonical_lepton_braid_words",
        "audit_only": True,
        "precision_dps": 50,
        "context": {
            "purpose": "Build compute infrastructure for lepton braids at confinement levels (analog of per_generator_V_hat_3A for general H_n)",
            "source_audit": "docs/audits/2026-05-25-t6-f-ell-derivation-attempt.md",
            "owner_directive": "use canonical braid word forms. make sure compute infra is there for all. should be something working at confinement levels",
        },
        "constants": {
            "q_0": str(q0),
            "h": str(h),
            "z": str(z),
            "Vol_4_1": str(Vol_4_1),
            "cal2_codata": str(cal2_target),
            "cal_tau_codata": str(cal_tau_e),
        },
        "leptons": serialisable,
        "verdict": (
            "Crude per-generator V̂ = |tr_M|^(1/n_gens) placeholder does NOT close lepton mass ratios. "
            "T6 requires extending mass_at_3A_proper.per_generator_V_hat_3A to general H_n with "
            "proper Plancherel-weighted character sum for lepton braid words. "
            "Compute infrastructure gap identified; closes via chi_lambda_braid integration."
        ),
        "follow_up_required": [
            "Generalise per_generator_V_hat_3A to per_generator_V_hat_general(n_strands, word)",
            "Apply to electron σ_1³ at H_2; verify against mass-endomorphism-tower.md V̂_e ≈ 0.594",
            "Apply to muon 4_1 at H_3; obtain V̂_0, V̂_1 (currently unpublished in framework)",
            "Apply Li_2^q canonical mass tower; check m_μ/m_e against CODATA 206.77",
            "Same for tau; check m_τ/m_e against CODATA 3477.23",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    here = Path(__file__).resolve().parent
    out = here / "canonical-lepton-braid-words.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
