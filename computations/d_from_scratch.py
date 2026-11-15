#!/usr/bin/env python3
"""D from scratch — full canonical infra at 50 dps mpmath.

Per user 'lets investigate D error. recalc from scratch using full
infra'.

Strategy: avoid all f64 noise + all convention mixing. Compute D's
binding energy from the canonical chain end-to-end at 50 dps:

  Inputs (at 50 dps):
    q_0  = 1/(1 - sqrt(Vol(4_1)/(m_μ/m_e)))
    m_e  = CODATA leptonic mass
    Q_β(n) = m_n − m_p − m_e  (CODATA splitting calibration)

  Step 1-2: ONE trace functional for every trace in Term 1 (2026-11-15)
    Convention-D Markov trace (Ocneanu, z = q^3/(q^2+1)) on the ruled
    borromean words (owner ruling qou-hu1f), at the proton pin, 50 dps:
      tr_M(p), tr_M(n), tr_M(D_atom)  from atomic-tr-m-mpfr-50dps-proton
      tr_M(D_free)                    from binding-canonical (the disconnected
                                      p ⊔ n word), checked == tr_M(p)·tr_M(n)

    Until 2026-11-15 Term 1 mixed two functionals: Q_cat and tr_M(D_free)
    came from light_isotope_sweep.tr_M_at_q0 (float64, Plancherel-weighted
    character sum), while tr_M(D_atom) came from the habiro-coefficients-atomic
    witness (grouped word, convention C, 0.38829). |free − atom| was therefore a
    difference of two different objects. Owner-approved fix, tracker #7735.

  Step 3: Term 1 (descended, β-calibrated subtraction)
    Q_cat = tr_M(n_free) − tr_M(p_free) (numerical)
    E_0  = Q_β(n) / |Q_cat|
    Term 1 = E_0 · |tr_M(D_free) − tr_M(D_atom)|
    where tr_M(D_atom) is the Habiro polynomial value (50 dps).

  Step 4: Term 4 (universal Frobenius co-Casimir, Lean-proved)
    Term 4 = m_e · Σ_{λ⊢3A} 1/dim_q(λ)  (canonical per-3A)
    For D: A = 2, so sum is over partitions of 6.

    P1.C HARD BREAK 2026-05-12: legacy `A · m_e · (2 + 1/[2]_q)` REMOVED.
    See P1.C of `docs/audits/2026-05-12-1ppb-implementation-plan.md`.

  Step 5: Δm_shell (per σ_shell ILP, A_magic = 2 only contributes)
    Δm_shell = E_0 · 5.889e-3 ≈ 0.018 MeV

  Step 6: Final B(D) = T1 + T4 + Δm_shell

NO Vol_hyp.  NO census.  NO BW formula (T5 invalid at A=2).

Output: d-from-scratch.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV, Q_NEUTRON_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

# Substrate parameter: the q_parameter pin (PROTON — this producer is not in
# `ideal_muon`, and is listed `physical_proton` in q0_anchor_manifest.json).
#
# Until 2026-11-15 this block DERIVED its own q_0 from the muon ratio
# (Vol(4_1)/(m_mu/m_e)) and recorded that as `q_0_mpf50` -- while every number
# it actually computed came from the proton pin: the free traces it then read
# from `tr_M_at_q0` used `q_parameter.Q`, `term4_frobenius_codim` likewise, and the Habiro witness it
# loads is stamped at the proton q_0. The local muon q_0 was used for nothing
# but the printout and the witness field, so the witness declared one layer
# and computed in the other (the straddle AGENTS.md §q0 anchor convention
# forbids). It now records the pin it uses.
from q_parameter import q_at as _q_at  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION
Q0               = mp.mpf(_q_at(70))
QI0              = mp.mpf(1) / Q0
HA               = Q0 - QI0
TWO_Q            = Q0 + QI0  # [2]_q


def _load_witness(name: str) -> dict:
    with open(Path(__file__).parent / name) as f:
        return json.load(f, parse_float=str)


def canonical_traces() -> dict:
    """tr_M(p), tr_M(n), tr_M(D_atom), tr_M(D_free) on ONE functional.

    Refuses unless both owning witnesses are at the pin this producer runs at,
    and unless the free trace equals tr_M(p)·tr_M(n) and the two witnesses
    agree on tr_M(D_atom), each to 1e-40.
    """
    from canonical_trm_reference import tr_m_nucleon
    p = tr_m_nucleon("proton")
    n = tr_m_nucleon("neutron")
    d_atom = tr_m_nucleon("deuteron")
    bc = _load_witness("binding-canonical.witness.json")
    if bc.get("q0Anchor") != "proton":
        raise SystemExit("refusing: binding-canonical.witness.json is not at "
                         f"the proton pin (q0Anchor={bc.get('q0Anchor')!r})")
    rows = {r["atom"]: r for r in bc["data"]["results"]}
    d_free = mp.mpf(rows["D"]["tr_M_free"])
    d_atom_bc = mp.mpf(rows["D"]["tr_M_atom"])
    tol = mp.mpf(10) ** -40
    if not mp.almosteq(d_atom_bc, d_atom, rel_eps=tol):
        raise SystemExit(f"refusing: binding-canonical D atom {d_atom_bc} != "
                         f"atomic-tr-m-mpfr-50dps-proton {d_atom}")
    if not mp.almosteq(d_free, p * n, rel_eps=tol):
        raise SystemExit(f"refusing: tr_M(D_free) {d_free} != tr_M(p)tr_M(n) "
                         f"{p * n}")
    return {"proton": p, "neutron": n, "D_atom": d_atom, "D_free": d_free}


def main():
    print("=" * 78)
    print("D from scratch — full canonical infra at 50 dps mpmath")
    print("=" * 78)

    # ────────────────────────────────────────────────────────────
    # Inputs at 50 dps
    # ────────────────────────────────────────────────────────────
    print(f"  q_0          = {mp.nstr(Q0, 30)}")
    print(f"  [2]_q        = {mp.nstr(TWO_Q, 30)}")
    print(f"  H_A = q-q⁻¹  = {mp.nstr(HA, 30)}")
    print(f"  m_e          = {M_E_MEV} MeV")
    print(f"  Q_β(n)       = {Q_NEUTRON_MEV} MeV")
    print(f"  m_p (CODATA) = {M_P_MEV} MeV")
    print(f"  m_n (CODATA) = {M_N_MEV} MeV")
    print()

    # ────────────────────────────────────────────────────────────
    # Step 1: Habiro polynomial values at 50 dps (EXACT, no f64)
    # ────────────────────────────────────────────────────────────
    print("Step 1-2: canonical Markov traces @ q_0 (conv D, borromean, proton)")
    print("─" * 78)
    TR = canonical_traces()
    for k in ("proton", "neutron", "D_atom", "D_free"):
        print(f"  tr_M({k:<7}) = {mp.nstr(TR[k], 30)}")
    print()

    # ────────────────────────────────────────────────────────────
    # Step 3: Term 1 = E_0 · |tr_M(D_free) − tr_M(D_atom)|
    # ────────────────────────────────────────────────────────────
    print("Step 3: Term 1 (descended, β-calibrated)")
    print("─" * 78)
    Q_cat = TR["neutron"] - TR["proton"]
    E_0 = mp.mpf(str(Q_NEUTRON_MEV)) / mp.fabs(Q_cat)
    print(f"  Q_cat = tr_M(n) − tr_M(p)   = {mp.nstr(Q_cat, 12)}")
    print(f"  E_0  = Q_β / |Q_cat|        = {mp.nstr(E_0, 12)} MeV/cat")
    delta_tr_M = mp.fabs(TR["D_free"] - TR["D_atom"])
    T1 = E_0 * delta_tr_M
    print(f"  Δtr_M = |free − atom|       = {mp.nstr(delta_tr_M, 12)}")
    print(f"  Term 1 = E_0 · Δtr_M        = {mp.nstr(T1, 12)} MeV")
    print()

    # ────────────────────────────────────────────────────────────
    # Step 4: Term 4 = m_e · Σ_{λ⊢3A} 1/dim_q(λ)  (canonical per-3A)
    # ────────────────────────────────────────────────────────────
    print("Step 4: Term 4 (universal Frobenius co-Casimir, Lean-proved)")
    print("─" * 78)
    A = 2
    # P1.C HARD BREAK (2026-05-12): the legacy
    # `Frob_per_vortex = m_e · (2 + 1/[2]_q); T4 = A · Frob_per_vortex`
    # has been REMOVED. It was an H_3-character formula × A that
    # overcounts T4 by 1.56× at A=2, 4.44× at A=4. The canonical form
    # per `thm:frobenius-codim-universal` is m_e · Σ_{λ⊢3A} 1/dim_q(λ).
    # See P1.C of `docs/audits/2026-05-12-1ppb-implementation-plan.md`.
    from paper_six_term_isotope_sweep import term4_frobenius_codim
    T4 = mp.mpf(str(M_E_MEV)) * term4_frobenius_codim(A)
    print(f"  Term 4 = m_e · τ(C_dim_q) at A={A}  = {mp.nstr(T4, 15)} MeV")
    print()

    # ────────────────────────────────────────────────────────────
    # Step 5: Δm_shell (σ_shell ILP, A_magic=2 only for D)
    # ────────────────────────────────────────────────────────────
    print("Step 5: Δm_shell (σ_shell ILP at A_magic = 2)")
    print("─" * 78)
    SIGMA_SHELL_BARE_AT_Q0_AMAGIC2 = mp.mpf("5.889176e-3")
    Dm_shell = SIGMA_SHELL_BARE_AT_Q0_AMAGIC2 * E_0
    print(f"  y_shell · σ_shell      = {mp.nstr(SIGMA_SHELL_BARE_AT_Q0_AMAGIC2, 10)} cat")
    print(f"  Δm_shell = y_shell·σ·E_0 = {mp.nstr(Dm_shell, 12)} MeV")
    print()

    # ────────────────────────────────────────────────────────────
    # Step 6: Final B(D)
    # ────────────────────────────────────────────────────────────
    print("Step 6: Final B(D)")
    print("─" * 78)
    B_pred = T1 + T4 + Dm_shell
    B_AME = AME_B_DEUTERON_MEV_VALIDATION
    err_pct = (B_pred - B_AME) / B_AME * 100
    err_ppb = err_pct * mp.mpf(10)**7
    print(f"  T1 + T4 + Δm_shell    = {mp.nstr(B_pred, 15)} MeV")
    print(f"  AME B(D)              = {mp.nstr(B_AME, 15)} MeV")
    print(f"  err vs AME            = {mp.nstr(err_pct, 8)}%")
    print(f"  err in ppb            = {mp.nstr(err_ppb, 6)}")
    print()

    # Per-term breakdown
    print("Per-term breakdown:")
    print(f"  Term 1 (descended)     = {mp.nstr(T1, 10)} MeV  ({mp.nstr(T1/B_AME*100, 4)}% of AME)")
    print(f"  Term 4 (Frobenius)    = {mp.nstr(T4, 10)} MeV  ({mp.nstr(T4/B_AME*100, 4)}% of AME)")
    print(f"  Δm_shell              = {mp.nstr(Dm_shell, 10)} MeV  ({mp.nstr(Dm_shell/B_AME*100, 4)}% of AME)")
    print(f"  Sum                   = {mp.nstr(B_pred, 10)} MeV  ({mp.nstr(B_pred/B_AME*100, 4)}% of AME)")
    print()


    # Build witness
    w = (
        WitnessBuilder("d-from-scratch", engine="python+mpmath")
        .set_description(
            "Deuteron binding from scratch using full canonical infra at "
            "50 dps mpmath. Every trace in Term 1 (tr_M(p), tr_M(n), "
            "tr_M(D_atom), tr_M(D_free)) is the convention-D Markov trace on "
            "the ruled borromean words at the proton pin, read from "
            "atomic-tr-m-mpfr-50dps-proton and binding-canonical (since "
            "2026-11-15; previously a float64 Plancherel character sum was "
            "subtracted from a convention-C Habiro trace). NO Vol_hyp, NO BW "
            "(invalid at A=2), NO census."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0_mpf50", mp.nstr(Q0, 50))
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("Q_beta_n_MeV", Q_NEUTRON_MEV)
        .add_parameter("E_0_MeV_per_cat", fmt(E_0))
        .add_data("tr_M_canonical_50dps", {k: mp.nstr(v, 50) for k, v in TR.items()})
        .add_data("tr_M_source", {
            "functional": "convention-D Markov trace, borromean word, proton pin",
            "proton/neutron/D_atom": "atomic-tr-m-mpfr-50dps-proton.witness.json",
            "D_free": "binding-canonical.witness.json (checked == tr_M(p)·tr_M(n) to 1e-40)",
        })
        .add_data("terms_50dps", {
            "Term_1_descended_MeV": mp.nstr(T1, 30),
            "Term_4_frobenius_MeV": mp.nstr(T4, 30),
            "delta_m_shell_MeV":   mp.nstr(Dm_shell, 30),
            "B_pred_MeV":          mp.nstr(B_pred, 30),
            "B_AME_MeV":           mp.nstr(B_AME, 30),
            "err_pct":             fmt(err_pct),
            "err_ppb":             fmt(err_ppb),
        })
        .add_caveat(
            "Δm_shell uses the typed σ_shell value 5.889176e-3 (A_magic = 2), "
            "which has no owning witness read here; its convention is not "
            "re-checked by this producer."
        )
        .add_caveat(
            "Term 5 (BW) explicitly NOT included — BW formula is "
            "structurally invalid at A=2 (surface dominates volume; "
            "B_bulk(D) = -4.44 MeV negative)."
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
