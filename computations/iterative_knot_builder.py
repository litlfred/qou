import sys
import os
from pathlib import Path
import json
import warnings
import multiprocessing
import time

warnings.filterwarnings("ignore")

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from mass_at_3A_proper import atom_braid_word_3A

import mpmath as mp  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()

# The EXPERIMENTAL (proton) pin — the standing default for all new and
# touched compute per the 2026-08-07 owner directive.
#
# This line used to read
#     HA = 1.10997859555733471989976 - (1 / 1.10997859555733471989976)
# a hardcoded MUON literal in float64, with no pin import and no anchor
# declared anywhere in the emitted witness. It was the correct muon value
# truncated to 24 digits (so not the wrong-value class bean qou-8q0u
# retires), but it pinned this file to the ideal layer invisibly: nothing
# in the file or its output said "muon", so no audit and no reader could
# tell which layer the classification threshold belonged to.
if not str(Q_50_DIGIT_STR).startswith("1.10997858275"):
    raise SystemExit(
        f"q_parameter resolved to {str(Q_50_DIGIT_STR)[:24]}…, not the proton "
        "pin. This file is not in q0_anchor_manifest.json, so it should get "
        "the default. Refusing to classify against an unknown layer.")

Q0 = mp.mpf(Q_50_DIGIT_STR)
HA = Q0 - 1 / Q0
_CLASSIFY_TOL = mp.mpf("1e-6")

def _classify_factor(c, d) -> str:
    """Template selector. Carried as mpf so the comparison against HA is
    exact-to-precision rather than float64; the 1e-6 tolerance is a
    template gate, not a numerical one."""
    c, d = mp.mpf(c), mp.mpf(d)
    if abs(c - 1) > _CLASSIFY_TOL:
        raise ValueError(f"unsupported c={mp.nstr(c, 12)} (expected 1)")
    if abs(d) < _CLASSIFY_TOL:
        return "pos"
    if abs(d + HA) < _CLASSIFY_TOL:
        return "neg"
    return "mixed"

def atom_to_braid_word_local(Z: int, N: int) -> list[int]:
    # strict_averaged convention removes the color split terms so it matches d=0, -h, -h/2
    triples = atom_braid_word_3A(Z, N, pn_convention="strict_averaged", include_inter=True)
    
    by_nucleon: list[dict] = []
    triples_with_kind = [(c, d, g, _classify_factor(c, d)) for (c, d, g) in triples]
    
    for (c, d, g, kind) in triples_with_kind:
        k = g // 3
        while len(by_nucleon) <= k:
            by_nucleon.append({"g0": [], "g1": [], "inter": []})
        r = g % 3
        if r == 0:
            by_nucleon[k]["g0"].append(kind)
        elif r == 1:
            by_nucleon[k]["g1"].append(kind)
        else:
            by_nucleon[k]["inter"].append(kind)
            
    word = []
    for k, blk in enumerate(by_nucleon):
        g0_len = len(blk["g0"])
        g1_len = len(blk["g1"])
        m = min(g0_len, g1_len)
        base = 3 * k + 1
        for i in range(m):
            word.append(base if blk["g0"][i] == "pos" else -base)
            word.append((base+1) if blk["g1"][i] == "pos" else -(base+1))
        for i in range(m, g0_len):
            word.append(base if blk["g0"][i] == "pos" else -base)
        for i in range(m, g1_len):
            word.append((base+1) if blk["g1"][i] == "pos" else -(base+1))
        for kind in blk["inter"]:
            word.append((base+2) if kind == "pos" else -(base+2))
            
    return word

def build_and_reduce(Z: int, N: int):
    word = atom_to_braid_word_local(Z, N)
    
    from hecke_core import atom_per_generator_volumes

    # Sum_i log|V_i| over the per-generator V_hat. Accumulated in mpf, not
    # float64: this is a sum over a growing number of terms, which is the
    # case AGENTS.md rule 2 names directly ("never aggregate with
    # statistics / math over floats").
    #
    # NOT a volume, despite the field name it used to carry. It is the log
    # of a PRODUCT of per-generator volumes, and its values run 7.8e6 to
    # 1.3e8 — no hyperbolic volume looks like that. Renamed
    # `sum_log_abs_V_hat`; `volume` is kept as an alias for existing
    # readers and marked deprecated in the witness.
    sum_log_V = None
    try:
        vols = atom_per_generator_volumes(Z, N, include_inter=True)
        acc = mp.mpf(0)
        for v in vols:
            x = mp.mpf(v["full"] if isinstance(v, dict) else v)
            if abs(x) > mp.mpf("1e-30"):
                acc += mp.log(abs(x))
        sum_log_V = mp.nstr(acc, 30)
    except Exception as e:
        sum_log_V = f"Error: {e}"
    vol_val = sum_log_V
        
    return {
        "Z": Z,
        "N": N,
        "A": Z + N,
        "initial_braid_length": len(word),
        "initial_crossings": len(word),
        # `reduced_crossings` was `len(word)` — the SAME expression as
        # `initial_crossings`. build_and_reduce performs no reduction, so
        # the field recorded a reduction that never ran. Reported as such
        # rather than silently dropped, since a consumer may key on it.
        "reduced_crossings": len(word),
        "reduction_performed": False,
        "sum_log_abs_V_hat": vol_val,
        "volume": vol_val,          # deprecated alias — NOT a volume
        "reduced_knot_name": "q-clt-proxy"
    }

def worker(Z, N, return_dict):
    res = build_and_reduce(Z, N)
    return_dict['res'] = res

def main():
    print("Iterative Knot Builder: Adding nucleons and performing braid reduction.")
    print("-" * 80)
    
    # 5 minutes in seconds
    TIMEOUT_SECONDS = 300
    
    sequence = [
        (1, 0), # p
        (1, 1), # D
        (2, 1), # 3He
        (2, 2), # 4He
        (3, 2), # 5Li
        (3, 3), # 6Li
        (4, 3), # 7Be
        (4, 4), # 8Be
        (5, 4), # 9B
        (5, 5), # 10B
        (6, 5), # 11C
        (6, 6), # 12C
    ]
    
    results = []
    
    manager = multiprocessing.Manager()
    
    for (Z, N) in sequence:
        print(f"Constructing atom Z={Z}, N={N} (A={Z+N}) [Timeout: {TIMEOUT_SECONDS}s]")
        return_dict = manager.dict()
        p = multiprocessing.Process(target=worker, args=(Z, N, return_dict))
        
        start_time = time.time()
        p.start()
        p.join(TIMEOUT_SECONDS)
        
        if p.is_alive():
            print(f"  -> TIMEOUT: Computation exceeded {TIMEOUT_SECONDS} seconds. Skipping.")
            p.terminate()
            p.join()
            results.append({
                "Z": Z, "N": N, "A": Z + N,
                "error": f"Timeout after {TIMEOUT_SECONDS}s"
            })
        else:
            if 'res' in return_dict:
                res = return_dict['res']
                print(f"  -> Initial Braid Length: {res.get('initial_braid_length', 'N/A')}")
                print(f"  -> Crossings:            {res.get('initial_crossings', 'N/A')} (no reduction is performed)")
                print(f"  -> Sum_i log|V_hat_i|:   {res.get('sum_log_abs_V_hat', 'N/A')}")
                results.append(res)
            else:
                print("  -> Error constructing or reducing (Process crash/exception)")
        print()
        
    # Was `json.dump(results, f)` of a bare list — the P30 raw-emit class.
    # A top-level JSON array carries no provenance (engine, scriptFile,
    # commitSha, scriptHash), so nothing could detect staleness and every
    # audit that does `body.get(...)` skipped the file in silence.
    # `derivation_chain_validator.py` still carries an explicit special
    # case to tolerate the array shape.
    from witness_base import WitnessBuilder  # noqa: E402

    failures = [r for r in results if "error" in r]
    completed = [r for r in results if "error" not in r]

    w = WitnessBuilder("iterative-knot-builder", engine="python")
    w.set_description(
        "Per-atom 3A braid words with the per-generator log-volume sum "
        "Sum_i log|V_hat_i|. Classification threshold HA = q0 - 1/q0 at the "
        "experimental PROTON pin. NOTE: no braid reduction is performed — "
        "`reduced_crossings` equals `initial_crossings` by construction and "
        "`reduced_knot_name` is a constant placeholder.")
    w.add_data("atoms", completed)
    # A timeout is unfinished work, not a result. It used to sit in the same
    # array as the completed rows, where a consumer reading the list would
    # take it for one — the "failure journalled as done" pattern the tnjb
    # sweep called out as a driver bug.
    w.add_data("incomplete", failures)
    w.add_assertion(
        name="every_scheduled_atom_completed",
        computed=str(len(failures)),
        expected="0",
        unit="incomplete atoms")
    w.save({
        "q0Anchor": "proton",
        "q0Value": str(Q_50_DIGIT_STR),
    })
    print(f"Saved witness: iterative-knot-builder.witness.json "
          f"({len(completed)} atoms, {len(failures)} incomplete)")

if __name__ == "__main__":
    main()
