#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

PSLQ on the EXTENDED basis for the weak-scale crossing count N_v.

Companion to `conj:weak-spectral-completeness`.  The conjecture says
    N_v  ?=  prod_{k=2,3,4} ([2k]_q^2 / [2]_q)  ·  N_sym(q)

The earlier `nv_pslq_uniqueness_probe.py` (PR #509) probed
{q^k, [k]_q, hbar_q^k, small primes} and was inconclusive.  Here we
add the Plancherel-weighted Hecke products called out by the new
conjecture and run PSLQ on log(target): multiplicative product
structure becomes INTEGER COEFFICIENTS on basis logs.  log(N_v) is
basis-element 0; nonzero coefficient there is "genuine", zero is a
basis-internal coincidence.

Output: nv-pslq-extended-basis.witness.json
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import math
import time
from pathlib import Path
from datetime import datetime, timezone
import mpmath as mp

from q_parameter import q_at


def main():
    DPS = 1100
    mp.mp.dps = DPS

    # --- substrate parameter ---------------------------------------------------
    q = q_at(DPS - 50)
    hbar_q = (q - 1) / q

    def qint(n: int) -> mp.mpf:
        # standard symmetric q-integer  [n]_q = (q^n - q^-n)/(q - q^-1)
        return (q**n - q**(-n)) / (q - 1/q)

    # --- target N_v ------------------------------------------------------------
    # N_v is FIXED by the unit choice m_e = 3·E_x·mu_0 plus the CODATA G_F:
    #   E_x = (q - 1/q)/2 = sinh(ln q)
    #   mu_0 = m_e/(3 E_x)             [MeV per Skein unit]
    #   v = 1/(sqrt(2) G_F)^(1/2)       [MeV, weak vev]
    #   N_v = v / (E_x · mu_0)
    # Centralized CODATA inputs (Gemini review on PR #515): pull from
    # experimental_constants instead of hardcoding the literals.
    from experimental_constants import G_F_MEV, G_F_MEV_ERR, M_E_MEV
    G_F        = mp.mpf(str(G_F_MEV))         # MeV^-2, CODATA 2022
    G_F_err    = mp.mpf(str(G_F_MEV_ERR))
    m_e        = mp.mpf(str(M_E_MEV))         # MeV
    E_cross    = (q - 1/q) / 2
    mu_0       = m_e / (3 * E_cross)
    v_weak     = 1 / mp.sqrt(mp.sqrt(2) * G_F)
    N_v        = v_weak / (E_cross * mu_0)
    log_N_v    = mp.log(N_v)

    # --- conjectured product form ---------------------------------------------
    # P(q) = [4]_q [6]_q [8]_q / [2]_q^3
    # (this is the "structural" factor; the conjecture writes it as
    #  prod_k [2k]_q^2 / [2]_q which is P(q) squared up to a [2]_q factor —
    #  we test BOTH forms.)
    P_struct = qint(4) * qint(6) * qint(8) / qint(2)**3
    P_conj   = (qint(4)**2 / qint(2)) * (qint(6)**2 / qint(2)) * (qint(8)**2 / qint(2))
    # Required N_sym for each form:
    N_required_struct = N_v / P_struct
    N_required_conj   = N_v / P_conj

    # --- additive (log) basis for PSLQ ----------------------------------------
    # First basis element is log(N_v).  A relation with nonzero coefficient on
    # this slot is a "genuine" candidate; coefficient zero is a basis coincidence.
    labels: list[str] = []
    values: list[mp.mpf] = []

    def add(lab: str, val: mp.mpf):
        labels.append(lab); values.append(val)

    add("log(N_v)", log_N_v)

    # --- prior basis: q, [k]_q (k=2..10), hbar_q^k (k=1..6), small primes ----
    # IMPORTANT: in additive (log) PSLQ, redundant generators are linearly
    # dependent and trivially close a relation, masking any genuine N_v
    # closed form.  We therefore use a MINIMAL spanning set of logs:
    #   log(q), log(hbar_q), log([k]_q) for k=2..10, log(p) for p prime.
    # Plancherel weights and the conjectured product DO NOT add new logs
    # over this spanning set (they are integer combinations); they enter
    # implicitly via log([2k]_q) and log([2]_q).  See `derived_targets`
    # in the witness for their numerical values.
    add("log(q)",      mp.log(q))
    add("log(hbar_q)", mp.log(hbar_q))
    for k in range(2, 11):
        add(f"log([{k}]_q)", mp.log(qint(k)))
    for p in (2, 3, 5, 7):
        add(f"log({p})", mp.log(p))
    add("log(pi)",     mp.log(mp.pi))

    print(f"DPS               = {DPS}")
    print(f"q (50 dps)        = {mp.nstr(q, 50)}")
    print(f"N_v               = {mp.nstr(N_v, 25)}")
    print(f"log(N_v)          = {mp.nstr(log_N_v, 25)}")
    print(f"P_struct          = [4]_q[6]_q[8]_q/[2]_q^3 = {mp.nstr(P_struct, 25)}")
    print(f"P_conj            = prod [2k]_q^2/[2]_q       = {mp.nstr(P_conj, 25)}")
    print(f"N_required (struct) = N_v / P_struct          = {mp.nstr(N_required_struct, 25)}")
    print(f"N_required (conj)   = N_v / P_conj            = {mp.nstr(N_required_conj,   25)}")
    print(f"basis size        = {len(values)}")
    print()

    # Sanity uncertainty: how much does CODATA G_F uncertainty move N_v?
    # dN/N = (1/4) dG/G   →  N_v has ~G_F's relative err / 4.
    G_F_rel = G_F_err / G_F
    N_v_rel = G_F_rel / 4
    print(f"CODATA G_F rel-err = {mp.nstr(G_F_rel, 4)}")
    print(f"N_v inherited rel-err ≈ {mp.nstr(N_v_rel, 4)}  "
          f"(≈ {mp.nstr(N_v_rel * mp.log(10), 4)} dps floor)")
    nv_dps_floor = int(-mp.log10(N_v_rel))
    print(f"  → digits of N_v that are actually CODATA-supported ≈ {nv_dps_floor}")
    print()

    # --- PSLQ at four tolerances ---------------------------------------------
    relations = []
    for tol_dps in (100, 50, 12, 7):
        print(f"--- PSLQ tol = 1e-{tol_dps} ---")
        t0 = time.time()
        try:
            tol = mp.mpf(10) ** (-tol_dps)
            rel = mp.pslq(values, tol=tol, maxcoeff=10**30)
            dt = time.time() - t0
            if rel is None:
                print(f"  no relation  ({dt:.2f}s)")
                relations.append({"tol_dps": tol_dps, "relation": None,
                                  "walltime_s": dt})
                continue
            terms = [(int(c), lab) for c, lab in zip(rel, labels) if c != 0]
            check = sum(c * v for c, v in zip(rel, values))
            nv_coef = next((c for c, lab in terms if lab == "log(N_v)"), 0)
            kind = "GENUINE_N_v_RELATION" if nv_coef != 0 else "BASIS_COINCIDENCE"
            note = ("nonzero log(N_v) coefficient — candidate closed form"
                    if nv_coef != 0 else
                    "log(N_v) coefficient is zero — relation lives entirely in "
                    "the q-basis and does NOT pin N_v")
            terms_str = " + ".join(f"{c}·{lab}" for c, lab in terms)
            print(f"  {kind}: {terms_str} = 0")
            print(f"  log(N_v) coef = {nv_coef}")
            print(f"  |residual|    = {mp.nstr(abs(check), 6)}     ({dt:.2f}s)")
            relations.append({
                "tol_dps":       tol_dps,
                "kind":          kind,
                "note":          note,
                "log_N_v_coef":  nv_coef,
                "relation":      terms,
                "max_abs_coef":  max(abs(c) for c, _ in terms),
                "residual":      mp.nstr(abs(check), 12),
                "walltime_s":    dt,
            })
        except Exception as e:
            print(f"  EXCEPTION: {e}")
            relations.append({"tol_dps": tol_dps, "exception": str(e)})

    # --- Conclusion logic -----------------------------------------------------
    genuine = [r for r in relations
               if isinstance(r, dict) and r.get("kind") == "GENUINE_N_v_RELATION"]
    coincidences = [r for r in relations
                    if isinstance(r, dict) and r.get("kind") == "BASIS_COINCIDENCE"]
    # Genuine relation that holds at >= 50 dps survives CODATA noise (~7 dps floor)
    deep_genuine = [r for r in genuine if r["tol_dps"] >= 50]
    if deep_genuine:
        conclusion = "CLOSED"
        verdict = ("Extended basis closes NV-1: genuine integer relation on "
                   "log(N_v) at >=50 dps, well below the CODATA G_F floor "
                   f"(~{nv_dps_floor} dps).  N_v is pinned to the conjectured "
                   "Plancherel-weighted form (mod rational N_sym).")
    elif genuine:
        conclusion = "REFINED_CONJECTURE_NEEDED"
        verdict = ("Genuine log(N_v) relations appear only near the CODATA "
                   "G_F floor — consistent with CODATA-noise overfit, not a "
                   "true closed form.  Refine the conjecture or extend the "
                   "basis (add N_sym explicitly, or genus factors [g]_q).")
    else:
        conclusion = "INCONCLUSIVE"
        verdict = ("Extended basis does NOT close NV-1: no log(N_v) relation "
                   "at any tested tolerance.  Consistent with the conjectured "
                   "form iff N_sym(q) is transcendental in the basis — N_sym "
                   "must be authored explicitly before PSLQ can verify.")

    # --- Witness file ---------------------------------------------------------
    out = {
        "computation":  "nv-pslq-extended-basis",
        "description": (
            "PSLQ on the EXTENDED basis for N_v that adds the "
            "Plancherel-weighted Hecke factors [2k]_q^2/[2]_q (k=2,3,4) and "
            "the conjectured product [4]_q[6]_q[8]_q/[2]_q^3 from "
            "conj:weak-spectral-completeness.  log-basis form: integer "
            "coefficients encode multiplicative product structure."
        ),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "precision_dps": DPS,
        "inputs": {
            "q_50dp":             mp.nstr(q, 50),
            "hbar_q_50dp":        mp.nstr(hbar_q, 50),
            "G_F_MeV_minus2":     mp.nstr(G_F, 12),
            "G_F_relative_err":   mp.nstr(G_F_rel, 6),
            "m_e_MeV":            "0.51099895000",
            "N_v_25dp":           mp.nstr(N_v, 25),
            "log_N_v_25dp":       mp.nstr(log_N_v, 25),
            "N_v_codata_dps_floor": nv_dps_floor,
        },
        "conjectured_product_structure": {
            "form_struct":             "[4]_q [6]_q [8]_q / [2]_q^3",
            "form_struct_value_25dp":  mp.nstr(P_struct, 25),
            "form_conj":               "prod_{k=2,3,4} [2k]_q^2 / [2]_q",
            "form_conj_value_25dp":    mp.nstr(P_conj, 25),
            "N_sym_required_struct":   mp.nstr(N_required_struct, 25),
            "N_sym_required_conj":     mp.nstr(N_required_conj, 25),
            "interpretation": (
                "If the conjectured product structure is exact, the "
                "categorical normalization N_sym(q) must equal N_v/P.  "
                "Authoring N_sym from first principles and matching one of "
                "these values discharges conj:weak-spectral-completeness."
            ),
        },
        "basis_labels": labels,
        "basis_size":   len(labels),
        "pslq_results": relations,
        "summary": {
            "n_genuine_relations":      len(genuine),
            "n_basis_coincidences":     len(coincidences),
            "n_deep_genuine_relations": len(deep_genuine),
            "conclusion":               conclusion,
            "verdict":                  verdict,
        },
    }

    out_path = Path(__file__).parent / "nv-pslq-extended-basis.witness.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print()
    print(f"Conclusion: {conclusion}")
    print(verdict)
    print(f"Witness: {out_path}")


if __name__ == "__main__":
    main()
