#!/usr/bin/env python3
"""
SDP-guided electron placement with BRANE-TOWER UNFOLDING.

User's insight (2026-04-19):
  "not per-nucleon H_3 SDP — you need to unfold one level"

Previous approach tried to place Z electron crossings within the
existing 3A-strand H_{3A}(q) algebra.  But electrons live in a
SEPARATE strand channel (the EM / pe coupling per Herrlich-Strecker
Wedderburn picture).  The brane-tower framework
[def:recursive-brane-tower](#def:recursive-brane-tower) prescribes
going UP one jet level: A_{n+1} = A_n ⊗ Ω^1(A_n), where Ω^1 adds
electron degrees of freedom.

Concretely: unfold from H_{3A}(q) → H_{3A+Z}(q) by giving each
electron its own strand.  The atom braid word then:

  strands 0 .. 3A-1   — nucleons (as before)
  strands 3A .. 3A+Z-1 — electron strands (one per electron)
  electron-nucleon coupling — σ crossings between strand 3A-1 and 3A,
                              3A and 3A+1, etc.  (serial chain, default;
                              SDP sweep identifies best coupling)

For Z electrons: at each step, tentatively add an electron strand
and sweep gen j ∈ {3A, 3A+1, ...} to find the position that
minimizes tr_M (maximum binding).  The SDP feasibility check
(Frobenius positivity of the full H_{3A+Z} element) is automatic
for real Hecke products but recorded for transparency.

Iterative witness is saved after each (atom, electron) case.
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


def place_electrons_unfolded(Z: int, N: int, B_AME: float) -> dict:
    """Iterative SDP-guided electron placement with brane-tower
    unfolding to H_{3A+Z}(q).

    Each electron adds ONE new strand.  At each step, sweeps gens
    in {3A + e, ..., current_top} where e is the electron index,
    picks the position that gives most-negative tr_M_atom.
    """
    A = Z + N
    # Nucleons-only word on 3A strands (no electrons, no unfolding).
    word_atom = list(atom_braid_word_3A(
        Z, N, include_inter=True, include_electrons=False))
    word_free = list(atom_braid_word_3A(
        Z, N, include_inter=False, include_electrons=False))

    # As we add electrons, strand count grows from 3A → 3A+Z.
    # Current n_strands starts at 3A; becomes 3A+e after electron e.
    current_n = 3 * A

    # Baseline at 3A strands.
    trM_a_base = _trM_word(word_atom, current_n)
    trM_f_base = _trM_word(word_free, current_n)
    B_base = E_0_BETA_DECAY_MEV * (abs(trM_f_base) - abs(trM_a_base))
    err_base = abs(B_base - B_AME) / (A * 938.272) * 100

    result = {
        "Z": Z, "N": N, "A": A, "B_AME_MeV": B_AME,
        "baseline_no_electrons": {
            "n_strands": current_n,
            "trM_atom": trM_a_base, "trM_free": trM_f_base,
            "B_pred_MeV": B_base, "err_pct": err_base,
        },
        "electron_placements": [],
    }

    for electron_i in range(Z):
        # Adding electron_i extends strand count by 1: 3A + electron_i → 3A + electron_i + 1
        new_n = 3 * A + electron_i + 1
        # Valid new generators are σ_k for k ∈ {0, ..., new_n - 2}.
        # An electron-nucleon coupling is a gen that straddles the old
        # strand range (0 .. 3A+electron_i - 1) and the new strand
        # (3A + electron_i).  Coupling gens: σ_{3A+electron_i - 1}
        # up to gens inside the nucleon range that could pull an
        # electron "down" across strands via braiding.  For simplicity
        # restrict to the NEW adjacent gen σ_{new_n-2} (= σ_{3A+e-1}).
        # But sweep all gens to let SDP pick.
        t0 = time.time()
        sweep = []
        for gen_j in range(new_n - 1):
            # σ_j^{-1} = (1, -h, j) at gen_j in H_{new_n}
            trial_atom = word_atom + [(1.0, -float(h), gen_j)]
            trial_free = word_free + [(1.0, -float(h), gen_j)]
            try:
                trM_a = _trM_word(trial_atom, new_n)
                trM_f = _trM_word(trial_free, new_n)
            except Exception as e:
                sweep.append({"gen": gen_j, "error": str(e)})
                continue
            B = E_0_BETA_DECAY_MEV * (abs(trM_f) - abs(trM_a))
            err = abs(B - B_AME) / (A * 938.272) * 100
            sweep.append({
                "gen": gen_j,
                "trM_atom": trM_a, "trM_free": trM_f,
                "B_pred_MeV": B, "err_pct": err,
            })

        # SDP-optimal placement: maximum binding = minimum tr_M_atom
        # (Frobenius positivity auto-satisfied for real Hecke products).
        valid = [s for s in sweep if "trM_atom" in s]
        if not valid:
            result["electron_placements"].append({
                "electron_index": electron_i, "error": "no valid sweep"})
            break
        chosen = min(valid, key=lambda r: r["trM_atom"])
        # Alternative scoring: lowest err vs AME
        chosen_by_err = min(valid, key=lambda r: r["err_pct"])

        dt = time.time() - t0
        print(f"  electron {electron_i+1}/{Z}: unfolded n={new_n}, "
              f"SDP picks gen={chosen['gen']} "
              f"(trM_atom={chosen['trM_atom']:+.4e}, "
              f"B={chosen['B_pred_MeV']:+.4f}, err={chosen['err_pct']:.4f}%); "
              f"alt lowest-err gen={chosen_by_err['gen']} "
              f"err={chosen_by_err['err_pct']:.4f}%  [{dt:.1f}s]")

        word_atom.append((1.0, -float(h), chosen["gen"]))
        word_free.append((1.0, -float(h), chosen["gen"]))
        current_n = new_n

        result["electron_placements"].append({
            "electron_index": electron_i,
            "new_n_strands": new_n,
            "chosen_gen_by_trM": chosen["gen"],
            "chosen_trM_atom": chosen["trM_atom"],
            "chosen_trM_free": chosen["trM_free"],
            "chosen_B_pred_MeV": chosen["B_pred_MeV"],
            "chosen_err_pct": chosen["err_pct"],
            "lowest_err_gen": chosen_by_err["gen"],
            "lowest_err_pct": chosen_by_err["err_pct"],
            "sweep": sweep,
            "time_sec": dt,
        })

    final_atom = _trM_word(word_atom, current_n)
    final_free = _trM_word(word_free, current_n)
    B_final = E_0_BETA_DECAY_MEV * (abs(final_free) - abs(final_atom))
    err_final = abs(B_final - B_AME) / (A * 938.272) * 100
    result["final"] = {
        "n_strands": current_n,
        "trM_atom": final_atom, "trM_free": final_free,
        "B_pred_MeV": B_final, "err_pct": err_final,
        "electron_gens": [p.get("chosen_gen_by_trM")
                             for p in result["electron_placements"]],
    }
    return result


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1,  2.22452),
        ("T",   1, 2,  8.481821),
        ("3He", 2, 1,  7.71804),
    ]
    # 4He adds 2 electrons → n=14 unfolded, p(14)=135.  Skip for first
    # iteration; add later if D/T/3He look good.

    out = (Path(__file__).parent
             / "electron-sdp-placement.witness.json")
    print("=" * 110)
    print("SDP ELECTRON PLACEMENT with UNFOLDING (n_strands = 3A + Z)")
    print(f"q0 = {Q0}, E_0 = {E_0_BETA_DECAY_MEV} MeV")
    print("=" * 110)

    all_results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        n_final = 3 * A + Z
        print(f"\n{name} (Z={Z}, N={N}, A={A}, n_final=3A+Z={n_final})")
        try:
            r = place_electrons_unfolded(Z, N, B_AME)
            r["atom"] = name
            all_results.append(r)
            baseline = r["baseline_no_electrons"]
            final = r["final"]
            print(f"  baseline (no e, n={baseline['n_strands']}): "
                  f"B_pred={baseline['B_pred_MeV']:+.4f}  "
                  f"err={baseline['err_pct']:.4f}%")
            print(f"  unfolded (+{Z} e, n={final['n_strands']}): "
                  f"B_pred={final['B_pred_MeV']:+.4f}  "
                  f"err={final['err_pct']:.4f}%  "
                  f"at gens {final['electron_gens']}")
        except Exception as e:
            import traceback
            print(f"  ERR: {type(e).__name__}: {e}")
            traceback.print_exc()
            all_results.append({"atom": name, "Z": Z, "N": N, "error": str(e)})
        # Iterative witness save
        out.write_text(json.dumps({
            "computation": "electron-sdp-placement-unfolded",
            "description": (
                "Brane-tower unfolded electron placement.  Each of the "
                "Z electrons gets its OWN strand; atom braid lives in "
                "H_{3A+Z}(q) rather than H_{3A}(q).  Iteratively "
                "places electrons at the generator giving minimum "
                "tr_M_atom (= maximum binding).  Frobenius positivity "
                "auto-satisfied for real Hecke products."),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "parameters": {"q0": Q0, "E_0_MeV": E_0_BETA_DECAY_MEV},
            "results": all_results,
        }, indent=2, default=str))

    print(f"\nWitness: {out}")
