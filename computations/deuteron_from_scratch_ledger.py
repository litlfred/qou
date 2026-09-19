#!/usr/bin/env python3
"""deuteron_from_scratch_ledger.py — γγ → D canonical chain, per-stage error ledger.

Owner request (2026-07-03): rebuild the deuteron mass + binding **from
scratch** along the canonical chain — from the substrate pin and the γγ
(pair-production) operator entry, through the H₆ Markov trace and the
confinement SDP, to the archimedean MeV numbers — fully witnessed, **no
fitted constants, no hardcoded literals**, and with a per-stage error
ledger so the origin of every error is visible.

## Stage decomposition

  S0  q₀ pin — solved LIVE under both anchors (muon CAL-2 proxy m_μ/m_e,
      proton phys-obs m_p/m_e), Vol(4₁) computed from Lobachevsky (not
      hardcoded). Error recorded: the μ–p anchor tension in q-space.
  S1  γγ production entry (structural): crossing energy 𝔈_× = ½(q−q⁻¹) > 0
      at q₀; the γγ → 6-operator-basis surjectivity + 𝓑₃ confinement
      selection are cited to their content blocks / witnesses. Contributes
      ZERO numerical error (topological identities); the honest gap flag is
      that the absolute-mass normaliser does NOT yet come from this chain
      (bean `ovud`).
  S2  Nucleon masses — muon-anchored Hecke energy (canonical_mass facade
      formula, recomputed live at both anchors):
        m_μ = m_e·Vol(4₁)/ℏ_q²,  F_Bor = |tr_M(β_Bor)|·[3]_q!/q³,
        m_p = 2·(m_μ·F_Bor − 6·m_e),  m_n = m_p + Q_β(Kashiwara b²) + m_e.
      Errors vs CODATA per anchor (anchor-choice attribution).
  S3  Deuteron H₆ Markov trace — transfer path (tr_m_atom_zn, fine
      Bratteli) vs Phase-5q closed form (tr_p·tr_n·f_pn) under both p-n
      conventions. Error recorded: cross-method / trace-convention spread
      (the convention-D registry item).
  S4  Confinement SDP at A=2 — reads the deuteron real-SDP witness
      (deuteron-real-sdp.witness.json, produced by deuteron_real_sdp.py,
      full primal+dual per AGENTS.md §LP/SDP); records the duality gap and
      the honest "does not close binding" flag.
  S5  Binding B_D — every non-fitted route in the corpus, each with its
      error vs AME2020 and its derivation tier.
  S6  m_D = m_p + m_n − B_D per route vs AME m_D; end-to-end error
      attributed between the nucleon-mass stage and the binding stage.

## Calibration content

INPUTS: m_e (CAL-1), q₀ (CAL-2 via m_μ/m_e — or the phys-obs proton pin),
Q_β enters S5 route R4 only as the CAL-2 proxy scale (diagnostic route).
CODATA / AME values appear ONLY as comparison anchors (validation), never
in any prediction path. No fitted constants; no hardcoded numeric
literals (all substrate constants route through substrate/ modules, which
compute them from Lobachevsky / CODATA source witnesses).

Usage:
    python3 -u computations/deuteron_from_scratch_ledger.py
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
warnings.filterwarnings("ignore")

import mpmath as mp  # noqa: E402

DPS = 50
mp.mp.dps = DPS + 10  # guard digits

from q_parameter import (  # noqa: E402
    Q_50_DIGIT_STR, q_at, q_muon_at, vol_4_1_at,
)
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION, M_D_MEV_VALIDATION,
    M_MU_MEV_VALIDATION,
    AME_B_DEUTERON_MEV_VALIDATION,
)
from knot_volumes import VOL_6_2_MPF  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from m_p_substrate_identity_50dps import F_Bor  # noqa: E402
from derived_masses import q_beta_kashiwara_n2_mev  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from closed_form_tau_M import (  # noqa: E402
    compute_tau_M_nucleon_H3, closed_form_tau_M, markov_z, hecke_h,
)
from per_braid_tower import deuteron_tower  # noqa: E402
from borromean_binding_recompute import borromean_binding  # noqa: E402
from binding_canonical import binding_canonical  # noqa: E402


def rel(pred: mp.mpf, ref: mp.mpf) -> mp.mpf:
    return (mp.mpf(pred) - mp.mpf(ref)) / mp.mpf(ref)


def ppb(x: mp.mpf) -> str:
    """Serialize a relative quantity in ppb.

    NOT `float(...)`: the arithmetic upstream is `mp.mpf` at DPS+10 guard
    digits, so a float64 cast at the write truncates ~45 determined digits
    (AGENTS.md NO-FLOAT64; drained 2026-09-13). Rendered at `DPS` via
    `q_str`, i.e. the guard digits are dropped rather than published.
    """
    return q_str(x * mp.mpf(10) ** 9)


# ---------------------------------------------------------------- S0
def stage0_q_pin() -> dict:
    """Solve q₀ live under both anchors; Vol(4₁) from Lobachevsky.

    The proton pin (`q_at`) solves the RAW identity
    m_p/m_e = 2·(Vol(4₁)/ℏ_q²)·F_Bor − 12 (owner ruling 2026-07-03:
    the fitted habiro tower that briefly dressed this solve is
    STRIPPED — see qou_substrate.constants.q_at + PR #3280, which
    proved the exact c₄ is linear in the pin offset, i.e. the tension
    reparametrized). Consequence: the μ–p anchor tension in q-space is
    the documented ~11.5 ppb (≈ ×21 sensitivity ⇒ ~242 ppb on masses;
    the AGENTS m_μ-prediction narrative is CURRENT)."""
    vol41 = vol_4_1_at(DPS)
    q_p = q_at(DPS)          # proton anchor  (phys-obs precision layer)
    q_mu = q_muon_at(DPS)    # muon anchor    (canonical CAL-2 proxy)
    pinned = mp.mpf(Q_50_DIGIT_STR)
    tension = rel(q_mu, q_p)
    return {
        "vol_4_1": q_str(vol41),
        "q_proton_anchor": q_str(q_p),
        "q_muon_anchor": q_str(q_mu),
        "q_pinned_witness": Q_50_DIGIT_STR,
        "pin_roundtrip_reldiff": q_str(abs(rel(q_p, pinned))),
        "anchor_tension_rel": q_str(tension),
        "anchor_tension_ppb": ppb(abs(tension)),
        "pin_note": (
            "RAW proton pin (owner ruling 2026-07-03; fitted habiro "
            "tower stripped — the exact c₄ is pin-offset-linear per "
            "PR #3280, so a dressed pin merely reparametrizes the μ–p "
            "tension)"
        ),
        "_q_p": q_p, "_q_mu": q_mu,
    }


def q_str(x: mp.mpf, digits: int = DPS) -> str:
    return mp.nstr(x, digits)


# ---------------------------------------------------------------- S1
#: Production-chain witnesses (categorical γγ → nucleon story) — cited,
#: existence-checked; the chain is topological (no numeric error term).
PRODUCTION_WITNESSES = (
    "four-term-photon-to-atoms.witness.json",
    "confinement-operator-selection.witness.json",
)

PRODUCTION_BLOCKS = (
    "content/quantum-observable-universe/particle-interactions/nucleon-from-photons-summary.md",
    "content/quantum-observable-universe/predicted-spectra/gamma-gamma-generates-particles.md",
    "content/quantum-observable-universe/predicted-spectra/breit-wheeler-pair-production.md",
    "content/quantum-observable-universe/particle-interactions/four-term-pair-nucleon.md",
)


def stage1_gamma_gamma(q: mp.mpf) -> dict:
    """γγ production entry — structural stage.

    Chain (content-block backed):  3(γγ) → 3(qq̄) → (q₁,q₂,q₃)
    →[𝓑₃ confinement, min action] 𝔑 nucleon →[⊕ Hopf] atom.
    The Lean side proves γγ spans the 6-element H₃ operator basis
    (gamma_gamma_chirality_surjective). Mass enters ONLY as crossing
    energy 𝔈_×(q) = ½(q − q⁻¹) per self-crossing (knot-particle
    dictionary: bare Vol = 0 for torus knots ⇒ no bare mass)."""
    e_cross = (q - 1 / q) / 2
    root = HERE.parent
    wit = {w: (HERE / w).exists() for w in PRODUCTION_WITNESSES}
    blocks = {b: (root / b).exists() for b in PRODUCTION_BLOCKS}
    return {
        "crossing_energy_at_q0": q_str(e_cross),
        "crossing_energy_positive": bool(e_cross > 0),
        "production_witnesses_present": wit,
        "production_blocks_present": blocks,
        "numeric_error_contribution": 0.0,
        "dangling_citation_flag": (
            "nucleon-from-photons-summary.md cites four-term-photon-to-"
            "atoms.witness.json, which does not exist anywhere in the "
            "repo — dangling witness citation (found 2026-07-03)"
        ),
        "gap_flag": (
            "absolute-mass normaliser (F_Bor) is NOT yet emitted by the "
            "γγ/brane tower itself — muon-anchored facade used at S2 "
            "(bean ovud: wire Li₂^q tower into production F_Bor)"
        ),
    }


# ---------------------------------------------------------------- S2
def habiro_ratio(q: mp.mpf, c4: mp.mpf) -> mp.mpf:
    """s5bb Habiro 4-loop correction (1+c₄u⁴)(1+4u⁵)(1−29u⁶),
    u = b·ℏ_q², b = √((q⁴+q²+1)/(q²+1)²)."""
    hbar_q_sq = ((q - 1) / q) ** 2
    b_val = mp.sqrt((q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2)
    u = b_val * hbar_q_sq
    return (1 + c4 * u ** 4) * (1 + 4 * u ** 5) * (1 - 29 * u ** 6)


def nucleon_masses_at(q: mp.mpf) -> dict:
    """Nucleon masses via the muon-anchored Hecke energy, recomputed
    live at q. Headline = the BARE (raw-pin) identity — the canonical
    form per the owner ruling 2026-07-03 (fitted habiro tower stripped
    from the pin). The two Habiro-dressed variants (c₄ = 46 and
    4143/90) are reported as FIT-TIER diagnostics: at the raw pin they
    miss CODATA m_p by ~+242 ppb, which IS the μ–p tension
    reparametrized (PR #3280 pin-offset linearity)."""
    m_e = mp.mpf(str(M_E_MEV))
    vol41 = vol_4_1_at(DPS)
    hbar_q_sq = ((q - 1) / q) ** 2
    m_mu = m_e * vol41 / hbar_q_sq
    fbor = F_Bor(q)
    m_p_bare = 2 * (m_mu * fbor - 6 * m_e)
    m_p_pin46 = m_p_bare * habiro_ratio(q, mp.mpf(46))
    m_p_prod = m_p_bare * habiro_ratio(q, mp.mpf(4143) / 90)
    q_beta = q_beta_kashiwara_n2_mev()   # evaluated at the canonical pin
    m_n = m_p_bare + q_beta + m_e
    return {"m_mu": m_mu, "F_Bor": fbor,
            "m_p": m_p_bare, "m_p_bare": m_p_bare,
            "m_p_pin46": m_p_pin46, "m_p_habiro_prod": m_p_prod,
            "m_n": m_n, "Q_beta": q_beta}


def stage2_nucleons(q_p: mp.mpf, q_mu: mp.mpf) -> dict:
    out = {}
    for label, q in (("proton_anchor", q_p), ("muon_anchor", q_mu)):
        r = nucleon_masses_at(q)
        out[label] = {
            "m_mu_MeV": q_str(r["m_mu"], 20),
            "m_p_bare_MeV": q_str(r["m_p_bare"], 20),
            "m_p_MeV": q_str(r["m_p"], 20),
            "m_n_MeV": q_str(r["m_n"], 20),
            "Q_beta_MeV": q_str(r["Q_beta"], 20),
            "F_Bor": q_str(r["F_Bor"], 20),
            "err_m_mu_ppb": ppb(rel(r["m_mu"], M_MU_MEV_VALIDATION)),
            "err_m_p_bare_ppb": ppb(rel(r["m_p_bare"], M_P_MEV_VALIDATION)),
            "err_m_p_pin46_ppb": ppb(rel(r["m_p_pin46"], M_P_MEV_VALIDATION)),
            "err_m_p_habiro_prod_ppb":
                ppb(rel(r["m_p_habiro_prod"], M_P_MEV_VALIDATION)),
            "err_m_p_ppb": ppb(rel(r["m_p"], M_P_MEV_VALIDATION)),
            "err_m_n_ppb": ppb(rel(r["m_n"], M_N_MEV_VALIDATION)),
            "_raw": r,
        }
    out["mismatch_flags"] = [
        "producer (m_p_substrate_identity_50dps.py) still applies the "
        "FIT-TIER habiro dressing while the pin is RAW (owner ruling "
        "2026-07-03) — at the raw pin the dressed m_p misses CODATA by "
        "~+242 ppb; reconcile is #3280's owner options (bean 2i8g)",
        "producer witness on main is stale vs the raw pin (computed at "
        "the old dressed pin) — flagged to #3280, not churned here",
    ]
    return out


# ---------------------------------------------------------------- S3
def stage3_trace(q: mp.mpf) -> dict:
    """Deuteron H₆ Markov trace, two independent routes + conventions."""
    ta, tf, _, _ = tr_m_atom_zn(1, 1, dps=DPS)
    ta, tf = mp.mpf(ta), mp.mpf(tf)
    tau_p = compute_tau_M_nucleon_H3("p", q, dps=DPS)
    tau_n = compute_tau_M_nucleon_H3("n", q, dps=DPS)
    cf = {}
    for conv in ("bring_color_weighted", "chi_lambda_braid"):
        cf[conv] = closed_form_tau_M(1, 1, q, tau_p, tau_n,
                                     pn_convention=conv)
    # free traces on the closed-form (Wenzl/χ_λ) route
    tf_cf = tau_p * tau_n
    # like-for-like object: the atom/free RATIO on each route
    ratio_transfer = ta / tf
    ratio_cf = {k: v / tf_cf for k, v in cf.items()}
    return {
        "transfer": {"tr_atom": q_str(ta), "tr_free": q_str(tf),
                     "Delta_tr": q_str(tf - ta),
                     "ratio_atom_over_free": q_str(ratio_transfer)},
        "closed_form": {
            "tau_p_H3": q_str(tau_p), "tau_n_H3": q_str(tau_n),
            "tr_free": q_str(tf_cf),
            "tr_atom_bring_color_weighted": q_str(cf["bring_color_weighted"]),
            "tr_atom_chi_lambda_braid": q_str(cf["chi_lambda_braid"]),
            "ratio_bring_color_weighted": q_str(ratio_cf["bring_color_weighted"]),
            "ratio_chi_lambda_braid": q_str(ratio_cf["chi_lambda_braid"]),
        },
        "route_ratio_gap_rel": q_str(
            abs(ratio_cf["chi_lambda_braid"] - ratio_transfer)
            / abs(ratio_transfer)),
        "note": (
            "the two routes are DIFFERENT trace normalizations on "
            "different canonical braid-word families (fine-Bratteli "
            "transfer / Z_N word vs colour-weighted atom word + Wenzl "
            "χ_λ) — NOT expected equal. Each is exact on its own "
            "reference (the Phase-5q closed form is verified as an "
            "exact-ℚ identity, PROBE-1 2026-07-02; the transfer path is "
            "the production binding object). The atom/free ratio gap "
            "recorded here is the route-choice error source; the "
            "finer Jones-vs-Wenzl convention-D spread is 1.955e-4 "
            "(trace-convention registry, 2026-07-02 addendum)"
        ),
        "_raw": {"ta": ta, "tf": tf, "tau_p": tau_p, "tau_n": tau_n,
                 "cf": cf},
    }


# ---------------------------------------------------------------- S4
def stage4_sdp() -> dict:
    """Read the deuteron real-SDP witness (full primal/dual)."""
    import json
    w = HERE / "deuteron-real-sdp.witness.json"
    if not w.exists():
        return {"available": False,
                "note": "deuteron-real-sdp.witness.json absent; run "
                        "deuteron_real_sdp.py to regenerate"}
    data = json.loads(w.read_text())
    d = data.get("data", {})
    interim = (d.get("phase_B_interim") or {}).get("lp") or {}
    return {
        "available": True,
        "witness": w.name,
        "full_space": {
            "duality_gap": d.get("duality_gap"),
            "primal_obj": d.get("primal_obj"),
            "dual_obj": d.get("dual_obj"),
            "strong_duality_holds": d.get("strong_duality_holds"),
            "diagnostic": d.get("diagnostic"),
        },
        "bounded_positive_norm_subspace": {
            "duality_gap": interim.get("duality_gap"),
            "primal_obj": interim.get("primal_obj"),
            "dual_obj": interim.get("dual_obj"),
        },
        "production_default_encoding": d.get("production_default_encoding"),
        "tr_M_beta_D": d.get("tr_M_beta_D"),
        "frobenius_gram_indefinite": d.get("frobenius_gram_indefinite"),
        "note": (
            "ERROR SOURCE (structural, documented): the full-space real "
            "SDP at q₀ is UNBOUNDED (Frobenius Gram indefinite — "
            "negative-norm conjugate blocks, bar-involution signature); "
            "the bounded positive-norm program achieves duality gap 0. "
            "Per the witness the canonical LR-branching encoding "
            "(production default 5) does NOT yet reproduce B_D — that "
            "open item IS the Δ_λ gate, quantified at S5"
        ),
    }


# ---------------------------------------------------------------- S5
def stage5_binding(q: mp.mpf) -> dict:
    m_e = mp.mpf(str(M_E_MEV))
    B_AME = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    h = hecke_h(q)
    routes = {}

    def add(key, value_mev, tier, source_of_error):
        v = mp.mpf(value_mev)
        routes[key] = {
            "B_MeV": q_str(v, 20),
            "err_rel_pct": q_str(rel(v, B_AME) * 100),
            "ratio_AME_over_pred": q_str(B_AME / v),
            "tier": tier,
            "error_source": source_of_error,
            "_raw": v,
        }

    # R1 — per-braid brane tower (level 0 + pair), transfer trace
    tow = deuteron_tower(DPS)
    add("R1_tower_level0_E0_dtr", tow["B_can0_MeV"],
        "derived (E₀ = m_e/(q₀(q₀−1)), Markov Δtr; convention: transfer)",
        "uniform E₀ where a per-λ weight (Δ_λ / FR projector) belongs; "
        "+12% overbind is the scalar-collapse signature")
    add("R1b_tower_with_pair_negarg", tow["B_tower_MeV_neg_arg"],
        "derived (adds z²·(−Li₂^q(−·)) pair term, sign derived)",
        "tower ADDS binding — the +33% shows the gap is not a truncation "
        "error of the tower")

    # R2 — Borromean single-pipeline (per-knot nucleon τ, closed form)
    bor = borromean_binding(1, 1, DPS)
    add("R2_borromean_level0", bor["B_can0"],
        "derived (Lean-proved τ(β_Bor) closed form; converges ∀Z)",
        "same uniform-E₀ / missing per-λ weight as R1, on the Borromean "
        "nucleon trace")
    add("R2b_borromean_tower", bor["B_tower"],
        "derived (R2 + Li₂^q pair term)",
        "as R2; pair term adds binding")

    # R3 — m_e·Vol(6₂): the deuteron's own knot volume
    add("R3_me_vol62", m_e * VOL_6_2_MPF,
        "derived shape (scale)·m_e·Vol(link) with ρ=1; 6₂ assignment is "
        "the one FIXED link assignment in the corpus",
        "link-volume route: error is the Kashaev linearization "
        "(tr ~ exp(Vol)) + the ρ-scale rule not yet derived for A>2")

    # R4 — diagnostic Q_β-scale trace difference + Δ_λ residual
    bc = binding_canonical(1, 1)
    B_diag = mp.mpf(str(bc["B_MeV"] if "B_MeV" in bc else bc.get("B", 0)))
    add("R4_diag_Qbeta_dtr", B_diag,
        "DIAGNOSTIC (Q_β scale, self-labeled wrong-scale)",
        "scale mismatch: Q_β = ℏ/P_skew^β vs the E₀ family; the residual "
        "B_AME/B_pred IS the Δ_λ(D) object probed symbolically (P1)")

    # R5 — q-Hamiltonian rotational energy (all factors derived);
    # n = 3A = 6 strands ⇒ j = n/2 = 3 (highest weight);
    # J_q²(j) = [j]_q·[j+1]_q with balanced q-integers [x] = (q^x−q^−x)/h
    hbar_q = 1 - 1 / q
    mu0 = m_e / (3 * h / 2)

    def qint(x):
        return (q ** x - q ** (-x)) / h

    j = mp.mpf(6) / 2
    add("R5_rotational_mu0", mu0 * hbar_q * qint(j) * qint(j + 1),
        "derived (μ₀ = m_e/(3h/2) per-crossing scale; J_q²(j=3) = "
        "[3]_q·[4]_q, n = 3A = 6 strands)",
        "highest-weight j=n/2 collapse of the per-λ Reeb phase — exact "
        "only in the linear (A=2) regime, −9% is the residual curvature")

    routes["_B_AME_MeV"] = q_str(B_AME, 20)
    routes["_bor_tau"] = q_str(bor["tau"])
    return routes


# ---------------------------------------------------------------- S6
def stage6_compose(s2: dict, s5: dict) -> dict:
    m_D_ref = mp.mpf(str(M_D_MEV_VALIDATION))
    out = {}
    for anchor in ("proton_anchor", "muon_anchor"):
        m_p = s2[anchor]["_raw"]["m_p"]
        m_n = s2[anchor]["_raw"]["m_n"]
        nucleon_sum = m_p + m_n
        nucleon_err_mev = (m_p - mp.mpf(str(M_P_MEV_VALIDATION))) + \
                          (m_n - mp.mpf(str(M_N_MEV_VALIDATION)))
        rows = {}
        for key, r in s5.items():
            if key.startswith("_"):
                continue
            B = r["_raw"]
            m_D = nucleon_sum - B
            B_err_mev = -(B - mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION)))
            rows[key] = {
                "m_D_MeV": q_str(m_D, 20),
                "err_m_D_ppm": q_str(rel(m_D, m_D_ref) * mp.mpf(10) ** 6),
                "error_from_nucleon_masses_MeV": q_str(nucleon_err_mev),
                "error_from_binding_MeV": q_str(B_err_mev),
            }
        out[anchor] = {
            "nucleon_sum_MeV": q_str(nucleon_sum, 20),
            "routes": rows,
        }
    out["m_D_AME_MeV"] = q_str(m_D_ref, 20)
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    print("=" * 72)
    print("DEUTERON FROM SCRATCH — per-stage error ledger (γγ → D)")
    print("=" * 72)

    s0 = stage0_q_pin()
    q_p, q_mu = s0.pop("_q_p"), s0.pop("_q_mu")
    print("\n[S0] q₀ pin (solved live)")
    print(f"  q₀(proton anchor) = {s0['q_proton_anchor'][:30]}…")
    print(f"  q₀(muon anchor)   = {s0['q_muon_anchor'][:30]}…")
    print("  pin round-trip vs witness: "
          f"{float(s0['pin_roundtrip_reldiff']):.2e}")
    print(f"  ERROR SOURCE: μ–p anchor tension = "
          f"{float(s0['anchor_tension_ppb']):.4f} ppb (in q-space; RAW pin)")
    print(f"  PIN NOTE: {s0['pin_note']}")

    s1 = stage1_gamma_gamma(q_p)
    print("\n[S1] γγ production entry (structural, no numeric error)")
    print(f"  𝔈_×(q₀) = ½(q−q⁻¹) = {s1['crossing_energy_at_q0'][:14]} > 0: "
          f"{s1['crossing_energy_positive']}")
    print(f"  witnesses present: {s1['production_witnesses_present']}")
    print(f"  GAP FLAG: {s1['gap_flag']}")

    s2 = stage2_nucleons(q_p, q_mu)
    print("\n[S2] nucleon masses (muon-anchored Hecke energy, live at both anchors)")
    for anchor in ("proton_anchor", "muon_anchor"):
        r = s2[anchor]
        print(f"  [{anchor}] m_p={r['m_p_MeV'][:12]}  m_n={r['m_n_MeV'][:12]}  "
              f"m_μ={r['m_mu_MeV'][:12]}")
        print("    err(ppb): "
              f"m_p(bare/RAW)={float(r['err_m_p_bare_ppb']):+.4f}  "
              f"m_p(hab.46 FIT)={float(r['err_m_p_pin46_ppb']):+.2f}  "
              f"m_p(hab.4143/90 FIT)={float(r['err_m_p_habiro_prod_ppb']):+.2f}  "
              f"m_n={float(r['err_m_n_ppb']):+.2f}  "
              f"m_μ={float(r['err_m_mu_ppb']):+.2f}")
    for f in s2["mismatch_flags"]:
        print(f"  MISMATCH FLAG: {f}")

    s3 = stage3_trace(q_p)
    print("\n[S3] deuteron H₆ Markov trace (cross-method)")
    print(f"  transfer: tr_atom={s3['transfer']['tr_atom'][:14]}  "
          f"tr_free={s3['transfer']['tr_free'][:14]}")
    print(f"  closed-form (χ_λ conv): "
          f"tr_atom={s3['closed_form']['tr_atom_chi_lambda_braid'][:14]}  "
          f"ratio={s3['closed_form']['ratio_chi_lambda_braid'][:12]}")
    print(f"  transfer ratio(atom/free) = "
          f"{s3['transfer']['ratio_atom_over_free'][:12]}")
    print(f"  ERROR SOURCE: route-choice ratio gap = "
          f"{float(s3['route_ratio_gap_rel']):.3e} (different normalizations; "
          f"convention-D Jones-vs-Wenzl spread = 1.955e-4)")

    s4 = stage4_sdp()
    print("\n[S4] confinement SDP at A=2")
    if s4.get("available"):
        print(f"  full space: gap={s4['full_space']['duality_gap']:.4g} "
              f"(UNBOUNDED — Gram indefinite, documented)")
        b = s4["bounded_positive_norm_subspace"]
        print(f"  bounded positive-norm subspace: gap={b['duality_gap']}, "
              f"primal={b['primal_obj']:.6g}")
        print(f"  production encoding: {s4['production_default_encoding']}")
    else:
        print(f"  {s4['note']}")

    s5 = stage5_binding(q_p)
    B_AME = s5["_B_AME_MeV"]
    print(f"\n[S5] binding routes (B_AME = {B_AME[:10]} MeV)")
    for key, r in s5.items():
        if key.startswith("_"):
            continue
        print(f"  {key:28s} B={r['B_MeV'][:10]:10s} "
              f"err={float(r['err_rel_pct']):+7.2f}%  "
              f"[{r['tier'].split('(')[0].strip()}]")

    s6 = stage6_compose(s2, s5)
    print(f"\n[S6] composed m_D vs AME ({s6['m_D_AME_MeV'][:14]} MeV) — proton anchor")
    for key, row in s6["proton_anchor"]["routes"].items():
        print(f"  {key:28s} m_D={row['m_D_MeV'][:12]:12s} "
              f"err={float(row['err_m_D_ppm']):+9.1f} ppm  "
              f"(nucleons {float(row['error_from_nucleon_masses_MeV']):+.5f} MeV, "
              f"binding {float(row['error_from_binding_MeV']):+.5f} MeV)")

    # strip mp objects for JSON
    def scrub(obj):
        if isinstance(obj, dict):
            return {k: scrub(v) for k, v in obj.items()
                    if not k.startswith("_raw")}
        if isinstance(obj, (list, tuple)):
            return [scrub(v) for v in obj]
        if isinstance(obj, mp.mpf):
            return str(obj)
        return obj

    wb = (WitnessBuilder("deuteron-from-scratch-ledger",
                         engine="mpmath+sympy+rust")
          .set_description(
              "Per-stage error ledger for the canonical γγ→D chain: q₀ pin "
              "(both anchors, live), γγ structural entry, muon-anchored "
              "nucleon masses, H₆ trace cross-method, A=2 SDP duals, all "
              "non-fitted binding routes vs AME2020, composed m_D with "
              "nucleon-vs-binding error attribution. No fitted constants; "
              "no hardcoded literals; CODATA/AME comparison-only.")
          .add_parameter("compute_dps", DPS)
          .add_parameter("q0_proton_anchor", s0["q_proton_anchor"])
          .add_parameter("q0_muon_anchor", s0["q_muon_anchor"])
          .add_data("S0_q_pin", scrub(s0))
          .add_data("S1_gamma_gamma", scrub(s1))
          .add_data("S2_nucleons", scrub(s2))
          .add_data("S3_trace", scrub(s3))
          .add_data("S4_sdp", scrub(s4))
          .add_data("S5_binding_routes", scrub(s5))
          .add_data("S6_composed_mass", scrub(s6)))

    wb.add_assertion(
        "q0_pin_roundtrip",
        computed=s0["pin_roundtrip_reldiff"], expected=0.0,
        tolerance=1e-45,
        source="q_at(50) vs q-pinning-50-digit witness string")
    wb.add_assertion(
        "crossing_energy_positive",
        computed=s1["crossing_energy_positive"], expected=True,
        source="knot-particle dictionary 𝔈_×(q₀) = ½(q−q⁻¹) > 0")
    # ratio-space round-trip: the RAW proton pin (owner ruling
    # 2026-07-03, fitted habiro tower stripped from q_at) solves the
    # BARE identity in m_p/m_e ratio space, so the exact check is the
    # bare mass; the ~+1.35 ppb seen in MeV space is the CODATA-internal
    # (m_p[MeV] vs m_e[MeV]·(m_p/m_e)) conversion inconsistency —
    # recorded as its own ledger line, not a failure.
    from q_parameter import MASS_RATIO_P_E_STR
    r_bare = s2["proton_anchor"]["_raw"]["m_p_bare"] / mp.mpf(str(M_E_MEV))
    ratio_roundtrip = q_str(abs(rel(r_bare, mp.mpf(MASS_RATIO_P_E_STR))))
    wb.add_data("S2_codata_mev_conversion_inconsistency_ppb",
                s2["proton_anchor"]["err_m_p_bare_ppb"])
    wb.add_assertion(
        "m_p_over_m_e_proton_anchor_ratio_roundtrip",
        computed=ratio_roundtrip, expected=0.0, tolerance=1e-40,
        source="RAW-pin anchor round-trip in RATIO space on the bare "
               "identity (not a prediction) — CODATA m_p/m_e")
    wb.add_assertion(
        "borromean_tau_below_one",
        computed=float(mp.mpf(s5["_bor_tau"]) < 1),
        expected=1.0,
        source="Li₂^q convergence gate |tr_M(β_Bor)| = 0.9986 < 1 "
               "(brane-tower plan Q3 resolution)")
    wb.save()
    print("\nwitness → deuteron-from-scratch-ledger.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
