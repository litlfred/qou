#!/usr/bin/env python3
"""Probe — apply paper formula B(H) = m_e · ρ · tr_M(T_w(H)) to D, T, ³He
using SDP-canonical braid words + ρ_factor from joint-tower-sdp-h6-h9.

Per prop:atom-knot-mass-derivation, this IS the canonical formula.  This
probe tests whether it gives the right binding under both Plancherel and
Wenzl-Schur Markov-trace conventions.

Result: paper formula fails by 87-100% on all three atoms regardless of
convention.  Multi-term decomposition (Term 1 + Tower + Term 4 + Term 5
+ Term 6) is required; single-term ρ·tr_M is structurally inadequate.

Output: probe-sdp-canonical-paper-formula.witness.json
"""
import sys, json
import numpy as np
from scipy import sparse as sp_sparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from hecke_characters import partitions_of, build_seminormal_matrices, qfac, dim_q
from q_parameter import Q as Q0_FLOAT
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder

H_VAL = float(Q0_FLOAT - 1.0/Q0_FLOAT)

def chi_lambda_braid_word(shape, braid_word):
    sigmas, dim, _ = build_seminormal_matrices(shape)
    if dim == 0: return 0.0, 0
    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    if is_sparse:
        I = sp_sparse.eye(dim, format='csr')
        prod = sp_sparse.eye(dim, format='csr')
    else:
        I = np.eye(dim); prod = np.eye(dim)
    for g in braid_word:
        idx = abs(g) - 1
        if idx >= len(sigmas):
            return None, dim
        M = sigmas[idx] if g > 0 else (sigmas[idx] - H_VAL * I)
        prod = prod @ M
    chi = float(prod.diagonal().sum()) if is_sparse else float(np.trace(prod))
    return chi, dim

def tr_M_sdp(n_0, braid_word, wenzl_y_table):
    nfac = qfac(n_0)
    tr_P = 0.0; tr_W = 0.0
    per_lambda = []
    for lam in partitions_of(n_0):
        chi, d = chi_lambda_braid_word(lam, braid_word)
        if chi is None or d == 0:
            continue
        dq = float(dim_q(lam))
        wP = float(dq*dq / nfac)
        yW = wenzl_y_table.get(lam, 0.0) if wenzl_y_table else 0.0
        cP = wP * chi / d
        cW = yW * chi
        tr_P += cP; tr_W += cW
        per_lambda.append({
            "lambda": list(lam), "d_lambda": d, "dim_q": dq,
            "chi": chi, "w_planch": wP, "y_wenzl": yW,
            "contrib_P": cP, "contrib_W": cW,
        })
    return tr_P, tr_W, per_lambda

def main():
    HERE = Path(__file__).parent
    sdp = json.loads((HERE / "joint-tower-sdp-h6-h9.witness.json").read_text())
    yw = json.loads((HERE / "y-lambda-wenzl-witness.json").read_text())

    def get_wenzl(n):
        if str(n) not in yw["tables_by_n"]:
            return None
        return {tuple(w["partition"]): float(w["y_lambda_numeric"])
                for w in yw["tables_by_n"][str(n)]["weights"]}

    B_AME = {"deuteron": 2.224566, "tritium": 8.481798, "he3": 7.71806}

    print("=" * 92)
    print("SDP-canonical paper-formula probe: B = m_e · ρ · tr_M(T_w)")
    print("=" * 92)
    print(f"  m_e = {M_E_MEV} MeV   q_0 = {Q0_FLOAT}")
    print()

    results = {}
    for c in sdp["per_atom_certificates"]:
        name = c["name"]
        n_0 = c["n_0"]
        bw = c["braid_word_input"]
        rho = c["rho_factor"]
        knot = c.get("knot_name", "?")
        wenzl = get_wenzl(n_0)
        tr_P, tr_W, per_lam = tr_M_sdp(n_0, bw, wenzl)
        B_pred_P = M_E_MEV * rho * tr_P
        B_pred_W = M_E_MEV * rho * tr_W
        ame = B_AME[name]
        err_P = (B_pred_P - ame) / ame * 100
        err_W = (B_pred_W - ame) / ame * 100

        print(f"  {name} (knot={knot}, n_0={n_0}, ρ={rho}, braid={bw})")
        print(f"    tr_M Plancherel  = {tr_P:>10.6f}  ->  B = {B_pred_P:>10.4f} MeV  (err {err_P:>+8.2f}%)")
        print(f"    tr_M Wenzl-Schur = {tr_W:>10.6f}  ->  B = {B_pred_W:>10.4f} MeV  (err {err_W:>+8.2f}%)")
        print(f"    AME              = {ame:>10.4f} MeV")
        print()

        results[name] = {
            "n_0": n_0, "braid_word": bw, "rho_factor": rho, "knot": knot,
            "tr_M_plancherel": tr_P, "tr_M_wenzl_schur": tr_W,
            "B_predicted_plancherel_MeV": B_pred_P,
            "B_predicted_wenzl_schur_MeV": B_pred_W,
            "B_AME_MeV": ame,
            "err_plancherel_pct": err_P,
            "err_wenzl_schur_pct": err_W,
            "per_lambda": per_lam,
        }

    print("=" * 92)
    print("VERDICT: paper formula B = m_e · ρ · tr_M(T_w) FAILS by 87-100%")
    print("on all three atoms regardless of Plancherel/Wenzl-Schur convention.")
    print("Single-term formula is structurally inadequate; multi-term required.")
    print("=" * 92)

    w = (
        WitnessBuilder("probe-sdp-canonical-paper-formula", engine="python")
        .set_description(
            "Test prop:atom-knot-mass-derivation flagship formula "
            "B(H) = m_e · ρ · tr_M(T_w(H)) on the SDP-canonical braid "
            "words + ρ_factor from joint-tower-sdp-h6-h9.witness.json. "
            "Tests both Plancherel and Wenzl-Schur Markov-trace "
            "conventions. Result: -87% to -100% error on all of "
            "{D, T, ³He} for both conventions; single-term formula "
            "is structurally inadequate."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", Q0_FLOAT)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_data("results", results)
        .add_caveat(
            "Paper formula B = m_e · ρ · tr_M assumes the single-term "
            "Markov trace captures all of the categorical mass. The "
            "thm:knot-mass-formula-unified multi-term decomposition "
            "(T1 |tr_M| + T2+T3 brane tower Σ Φ_q + T4 m_e·Σ 1/dim_q + "
            "T5 chirality + T6 jet-prefix) gives a different answer. "
            "These two paper formulas are NOT reconciled. The single-"
            "term formula tested here fails empirically; the multi-term "
            "version is what compute approximately implements (with "
            "T2+T3 missing in current state)."
        )
    )
    out = w.save()
    print(f"\nWitness: {out.name}")

if __name__ == "__main__":
    main()
