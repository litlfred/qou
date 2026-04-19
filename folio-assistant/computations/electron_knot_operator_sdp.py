#!/usr/bin/env python3
"""
Electron placement via SDP over the KNOT-OPERATOR BASIS.

Per user directive (2026-04-19):
  "use knot operators basis"

And per [prop:knot-operator-selection](#prop:knot-operator-selection):

  The physics endomorphism Φ decomposes over torus-knot operators
  {T_{1,0}, T_{2,1}, T_{2,2}, T_{2,3}, T_{2,5}, ...} with braid words

    β(T_{1,0}) = 1                          (identity)
    β(T_{2,1}) = σ_j                         (single crossing)
    β(T_{2,2}) = σ_j^2                       (Hopf link / gluon)
    β(T_{2,3}) = σ_j σ_{j+1} σ_j             (trefoil / electron)
    β(T_{2,5}) = (σ_j σ_{j+1})^2 σ_j         (cinquefoil / muon)

  The interaction is a SUPERPOSITION of channels with weights
  d_λ(q). SDP picks the Φ ∈ span{β(T_{r,s})} that minimizes
  categorical action |tr(Φ)| subject to the on-shell (Frobenius
  demand-supply) constraint.

This script routes the electron-placement decision through the
knot-operator basis candidate set (not raw σ combinations). For
each electron in a Z-electron atom:

  • Candidate set = {T_{1,0}, T_{2,1}, T_{2,2}, T_{2,3}, T_{2,5}}
  • Each Tα has an exact braid word as a list of (c, d, gen) tuples
  • SDP enumerates per-electron choice + link position
  • Returns optimal knot operator per electron + dual gaps

Uses the unified sdp_decision core.
"""
from __future__ import annotations

import sys
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0, HA as h
from canonical_plus_multibrane import E_0_BETA_DECAY_MEV
from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A
from sdp_decision import sdp_decide


def _trM_word(word, n_strands):
    """Plancherel-weighted tr_M on a word in H_{n_strands}(q)."""
    from scipy.sparse import issparse, eye as speye
    nfac = qfac(n_strands)
    trM = 0.0
    for shape in partitions_of(n_strands):
        sigmas, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = dim_q(shape)
        if dq == 0:
            continue
        sparse = bool(sigmas) and issparse(sigmas[0])
        if sparse:
            prod = speye(dim, format='csr'); I = speye(dim, format='csr')
        else:
            prod = np.eye(dim); I = np.eye(dim)
        for (c, d, g) in word:
            if g < len(sigmas):
                prod = prod @ (c * sigmas[g] + d * I)
        chi = float(prod.diagonal().sum()) if sparse else float(np.trace(prod))
        w = (dq * dq) / nfac
        trM += w * chi / dim
    return trM


def knot_operator_word(op: str, base_gen: int) -> list[tuple[float, float, int]]:
    """Exact Hecke braid word for a torus-knot operator T_{r,s}.

    `base_gen` is the low-index generator where the operator anchors.
    T_{2,3} needs 3 strands starting at base_gen, T_{2,5} needs 3
    strands; T_{2,1}, T_{2,2} need 2 strands (one generator).
    """
    if op == "T_1_0":
        return []
    if op == "T_2_1":
        return [(1.0, 0.0, base_gen)]
    if op == "T_2_2":
        return [(1.0, 0.0, base_gen), (1.0, 0.0, base_gen)]
    if op == "T_2_3":
        return [(1.0, 0.0, base_gen),
                 (1.0, 0.0, base_gen + 1),
                 (1.0, 0.0, base_gen)]
    if op == "T_2_5":
        # (σ_j σ_{j+1})^2 σ_j
        return [(1.0, 0.0, base_gen), (1.0, 0.0, base_gen + 1),
                 (1.0, 0.0, base_gen), (1.0, 0.0, base_gen + 1),
                 (1.0, 0.0, base_gen)]
    raise ValueError(f"unknown knot operator: {op}")


KNOT_OPERATORS = ["T_1_0", "T_2_1", "T_2_2", "T_2_3", "T_2_5"]


def place_electrons_knot_op(Z: int, N: int, B_AME: float,
                                 reserve_strands: int = 3) -> dict:
    """Iterative SDP electron placement over the knot-operator basis.

    n_total = 3A + reserve_strands (default 3, enough for T_{2,3} and
    T_{2,5} which need 3 strands of room anchored at gen = 3A - 1).

    For each electron k ∈ {0..Z-1}:
      • base_gen = 3A - 1  (anchored at last nucleon strand; keeps
                             all electrons operating on the same
                             boundary — single Markov closure)
      • Candidates = {T_{1,0}, T_{2,1}, T_{2,2}, T_{2,3}, T_{2,5}}
      • SDP picks the operator minimizing tr_M_atom(full word)
      • Dual gaps vs the other 4 operators are the SDP certificate
    """
    A = Z + N
    n_total = 3 * A + reserve_strands
    base_gen = 3 * A - 1

    word_atom = list(atom_braid_word_3A(
        Z, N, include_inter=True, include_electrons=False))
    word_free = list(atom_braid_word_3A(
        Z, N, include_inter=False, include_electrons=False))

    # Baseline at extended n_total with no electrons.
    trM_a_ext = _trM_word(word_atom, n_total)
    trM_f_ext = _trM_word(word_free, n_total)
    B_ext = E_0_BETA_DECAY_MEV * (abs(trM_f_ext) - abs(trM_a_ext))
    err_ext = abs(B_ext - B_AME) / (A * 938.272) * 100

    # 3A-baseline (no extension, no electrons) for context.
    trM_a_3A = _trM_word(word_atom, 3 * A)
    trM_f_3A = _trM_word(word_free, 3 * A)
    B_3A = E_0_BETA_DECAY_MEV * (abs(trM_f_3A) - abs(trM_a_3A))
    err_3A = abs(B_3A - B_AME) / (A * 938.272) * 100

    result = {
        "Z": Z, "N": N, "A": A, "B_AME_MeV": B_AME,
        "n_total": n_total, "base_gen": base_gen,
        "baseline_3A_no_electrons": {
            "n_strands": 3 * A, "B_pred_MeV": B_3A, "err_pct": err_3A},
        "baseline_extended_no_electrons": {
            "n_strands": n_total, "B_pred_MeV": B_ext,
            "err_pct": err_ext},
        "electrons": [],
    }

    for k in range(Z):
        # Build candidate braid words (per electron k)
        cands = []
        for op in KNOT_OPERATORS:
            w = knot_operator_word(op, base_gen)
            cands.append((op, word_atom + w))

        def compute_trM_atom(w, n):
            return _trM_word(w, n)

        t0 = time.time()
        rep = sdp_decide(candidates=cands, n_strands=n_total,
                            compute_trM=compute_trM_atom,
                            label=f"electron {k+1}/{Z}")
        dt = time.time() - t0

        # Compute binding for each candidate (tr_M_free is shared — no
        # internucleon channel — so |tr_f| is identical for all ops)
        free_with_op = {}
        for op in KNOT_OPERATORS:
            w = knot_operator_word(op, base_gen)
            free_with_op[op] = _trM_word(word_free + w, n_total)

        sweep = []
        for op in KNOT_OPERATORS:
            trM_a_op = rep.trM_by_candidate[op]
            trM_f_op = free_with_op[op]
            B = E_0_BETA_DECAY_MEV * (abs(trM_f_op) - abs(trM_a_op))
            err = abs(B - B_AME) / (A * 938.272) * 100
            sweep.append({
                "op": op, "trM_atom": trM_a_op, "trM_free": trM_f_op,
                "B_pred_MeV": B, "err_pct": err,
                "dual_gap": rep.dual_gaps[op],
            })

        chosen = rep.optimal_name
        chosen_row = next(s for s in sweep if s["op"] == chosen)
        chosen_by_err = min(sweep, key=lambda s: s["err_pct"])

        print(f"  e {k+1}/{Z} (base_gen={base_gen}): SDP picks {chosen}  "
              f"trM_a={chosen_row['trM_atom']:+.4e}  "
              f"B={chosen_row['B_pred_MeV']:+.4f}  "
              f"err={chosen_row['err_pct']:.4f}%  [{dt:.1f}s]")
        print(f"    alt lowest-err: {chosen_by_err['op']} "
              f"err={chosen_by_err['err_pct']:.4f}%")
        for s in sweep:
            if s["op"] != chosen:
                print(f"      gap[{s['op']}] = {s['dual_gap']:+.3e}  "
                      f"err={s['err_pct']:.4f}%")

        # Commit chosen operator into the braid
        chosen_word = knot_operator_word(chosen, base_gen)
        word_atom = word_atom + chosen_word
        word_free = word_free + chosen_word

        result["electrons"].append({
            "electron_index": k,
            "chosen_op": chosen,
            "chosen_B_pred_MeV": chosen_row["B_pred_MeV"],
            "chosen_err_pct": chosen_row["err_pct"],
            "chosen_trM_atom": chosen_row["trM_atom"],
            "chosen_trM_free": chosen_row["trM_free"],
            "lowest_err_op": chosen_by_err["op"],
            "lowest_err_pct": chosen_by_err["err_pct"],
            "sweep": sweep,
            "dual_gaps": dict(rep.dual_gaps),
            "time_sec": dt,
        })

    final_atom = _trM_word(word_atom, n_total)
    final_free = _trM_word(word_free, n_total)
    B_final = E_0_BETA_DECAY_MEV * (abs(final_free) - abs(final_atom))
    err_final = abs(B_final - B_AME) / (A * 938.272) * 100
    result["final"] = {
        "n_strands": n_total,
        "trM_atom": final_atom, "trM_free": final_free,
        "B_pred_MeV": B_final, "err_pct": err_final,
        "chosen_operators": [e["chosen_op"] for e in result["electrons"]],
    }
    return result


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1,  2.22452),
        ("T",   1, 2,  8.481821),
        ("3He", 2, 1,  7.71804),
    ]

    out = (Path(__file__).parent
             / "electron-knot-operator-sdp.witness.json")
    print("=" * 110)
    print("ELECTRON SDP over KNOT-OPERATOR BASIS  "
          "{T_{1,0}, T_{2,1}, T_{2,2}, T_{2,3}, T_{2,5}}")
    print(f"q0 = {Q0}, E_0 = {E_0_BETA_DECAY_MEV} MeV")
    print("=" * 110)

    all_results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        print(f"\n{name} (Z={Z}, N={N}, A={A}, n_total={3*A+3})")
        try:
            r = place_electrons_knot_op(Z, N, B_AME, reserve_strands=3)
            r["atom"] = name
            all_results.append(r)
            b3A = r["baseline_3A_no_electrons"]
            ext = r["baseline_extended_no_electrons"]
            fin = r["final"]
            print(f"  baseline n=3A={3*A}:     "
                  f"B={b3A['B_pred_MeV']:+.4f}  err={b3A['err_pct']:.4f}%")
            print(f"  ext n={ext['n_strands']} (no e):  "
                  f"B={ext['B_pred_MeV']:+.4f}  err={ext['err_pct']:.4f}%")
            print(f"  knot-op SDP ({Z} e, ops={fin['chosen_operators']}):  "
                  f"B={fin['B_pred_MeV']:+.4f}  err={fin['err_pct']:.4f}%")
        except Exception as e:
            import traceback
            print(f"  ERR: {type(e).__name__}: {e}")
            traceback.print_exc()
            all_results.append({"atom": name, "Z": Z, "N": N,
                                    "error": str(e)})
        out.write_text(json.dumps({
            "computation": "electron-knot-operator-sdp",
            "description": (
                "SDP-guided electron placement over the torus-knot "
                "operator basis {T_{1,0}, T_{2,1}, T_{2,2}, T_{2,3}, "
                "T_{2,5}} per prop:knot-operator-selection. Each "
                "candidate has an exact Hecke braid word; SDP returns "
                "the operator minimizing tr_M_atom with dual-gap "
                "certificates against the other 4 operators. "
                "Frobenius positivity is auto-satisfied for real "
                "Hecke products."),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "parameters": {"q0": Q0, "E_0_MeV": E_0_BETA_DECAY_MEV,
                              "knot_operators": KNOT_OPERATORS},
            "results": all_results,
        }, indent=2, default=str))

    print(f"\nWitness: {out}")
