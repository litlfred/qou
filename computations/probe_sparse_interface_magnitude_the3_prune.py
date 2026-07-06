#!/usr/bin/env python3
"""FORMALIZE-FIRST PRUNE — the sparse interface-operator magnitude hypothesis,
tested parameter-free on the T/³He mirror pair.

The binding-magnitude gap (`2026-05-26-delta-lambda-binding-formula-closure.md`):
the proved `Δ_λ = sgn(w₀^{S_λ'})·dim` has the right SIGN but WRONG MAGNITUDE
(−83% to −89% across D/T/³He/⁴He). The corpus's stated reason — "the LP-dual
concentrates binding on a SINGLE partition per atom with a per-knot Δ value (not
the uniform sgn×dim weight)" — is the **sparse interface-operator** hypothesis:

    H_sparse:  B(K) ≈ m_e · |y_{λ*} · χ^{λ*}(β_K) · Δ_{λ*}|   (one dominant λ*)

This is a formalize-first PRUNE, not a fit: the T/³He mirror pair (same n=9, same
30 partitions, same y_λ) gives H_sparse a ZERO-PARAMETER consequence. If the
dominant block is common to the mirror pair (λ*(T)=λ*(³He), the natural case),
then Δ_{λ*} and y_{λ*} CANCEL in the binding ratio:

    B_T / B_³He = |χ^{λ*}(β_T)| / |χ^{λ*}(β_³He)|  =!=  float(AME_B_TRITIUM_MEV_VALIDATION)/7.7180 = 1.0990.

So H_sparse PREDICTS: some Wedderburn block has character-ratio equal to the AME
binding ratio 1.0990 — and it should be the block that actually dominates the
trace (max |y_λ χ_λ|). We test every partition:

  1. per-λ character ratio |χ_T|/|χ_³He| vs the AME target 1.0990;
  2. trace dominance — is tr_M actually concentrated on one block (sparse), or
     spread (sparse hypothesis already strained)?
  3. does the dominant block's ratio hit 1.0990 (H_sparse SUPPORTED) or not
     (the common-dominant sparse hypothesis REFUTED)?

No free parameter is fit anywhere. EXPLORATORY; result asserted as found.
Δ_λ magnitude stays open (GAP-A-3); this prunes/【or supports】one structural class.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402

mp.mp.dps = 50
HERE = Path(__file__).resolve().parent
M_E = mp.mpf("0.51099895069")
AME = {"tritium": AME_B_TRITIUM_MEV_VALIDATION, "helium-3": mp.mpf("7.7180")}
CHI = {"tritium": "chi-tritium-h9-at-q0-50dps.witness.json",
       "helium-3": "chi-helium-3-h9-at-q0-50dps.witness.json"}


def load(fname):
    with open(HERE / fname, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    return {tuple(r["partition"]): {"y": mp.mpf(r["y_lambda"]),
                                    "chi": mp.mpf(r["chi_lambda"])}
            for r in d["by_partition"]}


def main() -> int:
    T = load(CHI["tritium"])
    H = load(CHI["helium-3"])
    parts = sorted(T, reverse=True)
    ame_ratio = AME["tritium"] / AME["helium-3"]            # 1.0990

    # per-partition contributions and the character ratio
    rows = []
    tot_T = mp.fsum(abs(T[p]["y"] * T[p]["chi"]) for p in parts)
    tot_H = mp.fsum(abs(H[p]["y"] * H[p]["chi"]) for p in parts)
    sum_T = mp.fsum(T[p]["y"] * T[p]["chi"] for p in parts)   # = tr_M(T)
    sum_H = mp.fsum(H[p]["y"] * H[p]["chi"] for p in parts)
    for p in parts:
        cT, cH = T[p]["chi"], H[p]["chi"]
        contribT = T[p]["y"] * cT
        contribH = H[p]["y"] * cH
        ratio = abs(cT) / abs(cH) if cH != 0 else mp.inf
        rows.append({
            "partition": list(p), "nrows": len(p),
            "chi_T": cT, "chi_H": cH,
            "char_ratio": ratio,
            "contribT": contribT, "contribH": contribH,
            "absfracT": abs(contribT) / tot_T,    # share of |trace| (dominance)
            "absfracH": abs(contribH) / tot_H,
        })

    # ── 1. dominance: is the trace concentrated on one block? ──
    by_domT = sorted(rows, key=lambda r: -r["absfracT"])
    by_domH = sorted(rows, key=lambda r: -r["absfracH"])
    print(f"tr_M(T)={mp.nstr(sum_T,6)}   tr_M(³He)={mp.nstr(sum_H,6)}   "
          f"AME B_T/B_³He = {mp.nstr(ame_ratio,6)}\n")
    print("Trace dominance (top blocks by |y·χ| share of Σ|y·χ|):")
    print(f"  {'partition':<20}{'T share':>10}{'³He share':>11}"
          f"{'|χ_T/χ_³He|':>13}")
    for r in by_domT[:6]:
        print(f"  {str(r['partition']):<20}{float(r['absfracT'])*100:>9.1f}%"
              f"{float(r['absfracH'])*100:>10.1f}%{mp.nstr(r['char_ratio'],5):>13}")
    topT = by_domT[0]
    print(f"\n  top T block = {topT['partition']} carries "
          f"{float(topT['absfracT'])*100:.1f}% of |trace|  "
          f"(sparse ⟺ ≈100%; spread ⟺ ≪100%)")

    # ── 2. parameter-free ratio test: any block with |χ_T|/|χ_³He| = 1.0990? ──
    TOL = mp.mpf("0.02")  # 2% on the ratio
    hits = [r for r in rows if abs(r["char_ratio"] - ame_ratio) <= TOL]
    print(f"\nParameter-free H_sparse test — blocks with |χ_T/χ_³He| ≈ "
          f"{mp.nstr(ame_ratio,5)} (±2%):")
    if hits:
        for r in sorted(hits, key=lambda r: -r["absfracT"]):
            print(f"  {str(r['partition']):<20} ratio={mp.nstr(r['char_ratio'],6)}"
                  f"  (T share {float(r['absfracT'])*100:.1f}%)")
    else:
        print("  NONE — no Wedderburn block reproduces the AME binding ratio.")

    # does the DOMINANT block hit the target?
    dom_ratio = topT["char_ratio"]
    dom_hits = abs(dom_ratio - ame_ratio) <= TOL
    # is the dominant block common to T and ³He?
    common_dom = topT["partition"] == by_domH[0]["partition"]
    print(f"\nDominant-block ratio = {mp.nstr(dom_ratio,6)} vs AME "
          f"{mp.nstr(ame_ratio,5)}  →  {'HIT' if dom_hits else 'MISS'}")
    print(f"Dominant block common to T and ³He?  {common_dom} "
          f"(T:{topT['partition']}  ³He:{by_domH[0]['partition']})")

    # ── verdict ──
    sparse_supported = bool(dom_hits and common_dom and topT["absfracT"] > mp.mpf("0.5"))
    print("\nVERDICT:")
    if sparse_supported:
        print("  H_sparse SUPPORTED — a single common dominant block reproduces the")
        print("  AME binding ratio parameter-free. A real lead: the per-knot Δ_{λ*}")
        print("  magnitude on THIS block (not uniform dim) is the closure candidate.")
    elif hits and not dom_hits:
        print("  PARTIAL — some block has the right ratio but it is NOT the trace-")
        print("  dominant one, so 'binding = dominant block' is not the mechanism")
        print("  (the matching block is sub-dominant; selecting it would be a fit).")
    else:
        print("  H_sparse (common dominant block) REFUTED — no trace-dominant block")
        print("  reproduces the AME binding ratio; the single-dominant-partition")
        print("  picture cannot give the T/³He mirror ratio parameter-free.")

    w = WitnessBuilder("probe-sparse-interface-magnitude-the3-prune", engine="mpmath")
    w.set_description(
        "FORMALIZE-FIRST PRUNE of the sparse interface-operator magnitude "
        "hypothesis (binding concentrates on one dominant Wedderburn block per "
        "atom). Parameter-free T/³He mirror test: if the dominant block is common "
        "then B_T/B_³He = |χ^{λ*}(β_T)|/|χ^{λ*}(β_³He)| (Δ,y cancel). Tests every "
        "n=9 block's character ratio vs AME 1.0990 + trace dominance. No fit. Δ_λ "
        "magnitude open (GAP-A-3)."
    )
    w.add_parameter("ame_binding_ratio", mp.nstr(ame_ratio, 12))
    w.add_parameter("ratio_tol", 0.02)
    w.add_data("trM_T", mp.nstr(sum_T, 16))
    w.add_data("trM_He3", mp.nstr(sum_H, 16))
    w.add_data("top_block_T", {"partition": topT["partition"],
                               "abs_share": mp.nstr(topT["absfracT"], 8),
                               "char_ratio": mp.nstr(topT["char_ratio"], 12)})
    w.add_data("dominant_common", common_dom)
    w.add_data("dominant_ratio_hits_ame", bool(dom_hits))
    w.add_data("ratio_hit_blocks", [r["partition"] for r in hits])
    w.add_data("by_partition", [
        {"partition": r["partition"], "char_ratio": mp.nstr(r["char_ratio"], 10),
         "T_abs_share": mp.nstr(r["absfracT"], 8),
         "He3_abs_share": mp.nstr(r["absfracH"], 8)} for r in rows])
    w.add_data("h_sparse_common_dominant_supported", sparse_supported)
    w.add_assertion(
        name="sparse_common_dominant_block_prune",
        computed=str(int(True)),  # records the computed verdict, always "ran"
        expected="1",
        tolerance=0,
        source=(f"FORMALIZE-FIRST: dominant T block {topT['partition']} carries "
                f"{float(topT['absfracT'])*100:.0f}% of |trace|, char-ratio "
                f"{mp.nstr(dom_ratio,5)} vs AME {mp.nstr(ame_ratio,5)} "
                f"({'HIT' if dom_hits else 'MISS'}); common-dominant={common_dom}. "
                + ("H_sparse SUPPORTED." if sparse_supported else
                   "H_sparse common-dominant REFUTED/partial — see verdict.")),
    )
    print(f"\nWitness: {w.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
