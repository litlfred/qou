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
import snappy

HA = 1.10997858275138080759166 - (1 / 1.10997858275138080759166)

def _classify_factor(c: float, d: float) -> str:
    if abs(c - 1.0) > 1e-6:
        raise ValueError(f"unsupported c={c} (expected 1)")
    if abs(d) < 1e-6:
        return "pos"
    if abs(d + HA) < 1e-6:
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
    L = snappy.Link(braid_closure=word)
    
    initial_crossings = L.crossing_entries()
    num_initial_crossings = len(initial_crossings) if initial_crossings else 0
    
    L.simplify('global')
    
    final_crossings = L.crossing_entries()
    num_final_crossings = len(final_crossings) if final_crossings else 0
    
    vol_val = None
    try:
        v = L.exterior().volume()
        vol_val = float(v)
    except Exception as e:
        vol_val = f"Error: {e}"
        
    return {
        "Z": Z,
        "N": N,
        "A": Z + N,
        "initial_braid_length": len(word),
        "initial_crossings": num_initial_crossings,
        "reduced_crossings": num_final_crossings,
        "volume": vol_val,
        "reduced_knot_name": L.identify() if hasattr(L, 'identify') else None
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
                print(f"  -> Reduced Crossings:    {res.get('reduced_crossings', 'N/A')} (from {res.get('initial_crossings', 'N/A')})")
                print(f"  -> Hyperbolic Volume:    {res.get('volume', 'N/A')}")
                results.append(res)
            else:
                print("  -> Error constructing or reducing (Process crash/exception)")
        print()
        
    out_file = HERE / "iterative-knot-builder.witness.json"
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved witness to {out_file.name}")

if __name__ == "__main__":
    main()
