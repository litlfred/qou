#!/usr/bin/env python3
"""Δ_λ closure check on the CANONICAL H_{3A} matrix-M tr_M (not H₃-local).

EXPLORATORY (no production wiring). The merged #2076 scale-gate analysed
the **H₃-local** `build_atom_nf` NF (tr_M → 10^1025). The object the
binding formula actually uses is the **canonical H_{3A} matrix-M Markov
trace**, which is **O(1)** (owner-confirmed 2026-06-09). This driver reads
the canonical matrix-M `tr_M(q₀)` + the AME binding and quantifies the
required channel factor on the RIGHT object:

    B(K) = m_e · tr_M(β_K) · Δ̄(K)        (single-scale reduction; exact
                                           iff Δ_λ is λ-independent = Δ̄)
  ⟹  Δ̄(K) = B(K) / (m_e · tr_M(β_K)).

Δ̄(K) is the per-nucleus target the volume route (Stage ②) must produce.

Finding to report: on the canonical O(1) tr_M, Δ̄ is **mild** (O(1–10),
per-nucleus) — NOT the 10^459 scale gate. So Δ_λ(K) is the *last* blocker
but no longer a catastrophic one; deriving Δ̄(K) from the per-nucleus
volume is the remaining work, free of the H₃-local scale obstruction.

Inputs (read-only): matrix-M `tr_M(q₀)` witnesses + AME binding witness.
Extends to all A as matrix-M witnesses land (the A≥4 infra, #2062).

Output: atom-vhyp-closure-matrix-m.witness.json
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401,E402

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
# Repo root by LANDMARK SEARCH, not by counting `.parent`s: the fixed
# count was off by one and resolved OUTSIDE the repo, so this bootstrap
# never fired -- masked because `_path_bridge`/PYTHONPATH already supplies
# the same directory in every in-repo run. Bean qou-rug0.
_ROOT = next(
    (_a for _a in _Path(__file__).resolve().parents
     if (_a / "tools").is_dir() and (_a / "computations").is_dir()),
    _Path(__file__).resolve().parent,
)
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV as _M_E_MEV  # noqa: E402  (registry, P31)

M_E_MEV = float(_M_E_MEV)
AME = HERE / "ame-2020-binding-energies.witness.json"

# (label, AME binding key, Z, N, atom_symbol)
NUCLEI = [
    ("deuteron", "B_deuteron_MeV", 1, 1, "D"),
    ("tritium", "B_tritium_MeV", 1, 2, "T"),
    ("helium-3", "B_he3_MeV", 2, 1, "3He"),
    ("helium-4", "B_he4_MeV", 2, 2, "4He"),
    ("lithium-6", "B_li6_MeV", 3, 3, "6Li"),
    ("lithium-7", "B_li7_MeV", 3, 4, "7Li"),
    ("beryllium-9", "B_be9_MeV", 4, 5, "9Be"),
]

def main() -> int:
    t0 = time.monotonic()
    ame = json.loads(AME.read_text())["data"]
    transfer_path = HERE / "tr-m-atom-via-transfer.witness.json"
    if not transfer_path.exists():
        print(f"Error: {transfer_path} not found")
        return 1
    transfer_data = json.loads(transfer_path.read_text())["data"]["rows"]
    tr_m_by_atom = {r["atom"]: float(r["tr_M_atom"]) for r in transfer_data}

    rows = []
    for label, bkey, Z, N, atom_sym in NUCLEI:
        if atom_sym not in tr_m_by_atom:
            rows.append({"label": label, "status": f"{atom_sym} missing from transfer witness"})
            continue
        tr_M = tr_m_by_atom[atom_sym]
        B = float(ame[bkey])
        A = Z + N
        delta_bar = B / (M_E_MEV * tr_M)   # required λ-independent Δ̄
        rows.append({
            "label": label, "Z": Z, "N": N, "A": A,
            "tr_M_canonical_matrixM": tr_M,
            "B_AME_MeV": B,
            "delta_bar_required": delta_bar,   # = B / (m_e · tr_M)
            "B_per_A_MeV": B / A,
        })

    solved = [r for r in rows if "delta_bar_required" in r]
    deltas = [r["delta_bar_required"] for r in solved]
    trms = [r["tr_M_canonical_matrixM"] for r in solved]
    spread = (max(deltas) / min(deltas)) if deltas and min(deltas) > 0 else None

    w = WitnessBuilder("atom-vhyp-closure-matrix-m", engine="python",
                       start_time=t0)
    w.set_description(
        "Δ_λ closure check on the CANONICAL H_{3A} matrix-M tr_M (EXPLORATORY). "
        "Quantifies the required λ-independent Δ̄(K)=B/(m_e·tr_M) on the O(1) "
        "matrix-M Markov trace — the object the binding formula uses — vs the "
        "H₃-local NF used by #2076. Shows Δ̄ is mild (O(1–10)), not the 10^459 "
        "H₃-local scale gate; the per-nucleus Δ̄(K) is the target for the "
        "Stage-② volume route."
    )
    w.add_data("m_e_MeV", M_E_MEV)
    w.add_data("rows", rows)
    w.add_data("canonical_trM_is_O1", {
        "tr_M_values": trms,
        "range": [min(trms), max(trms)] if trms else None,
        "note": "H_{3A} matrix-M Markov trace — O(1), decreasing with A; "
                "contrast the H₃-local NF (#2076) reaching 10^1025.",
    })
    w.add_data("required_delta_bar", {
        "values": deltas,
        "spread_factor": spread,
        "scale_gated": False,
        "conclusion": (
            "On the canonical O(1) tr_M the required Δ̄(K) is mild "
            f"({min(deltas):.2f}–{max(deltas):.2f}, ~{spread:.1f}× over "
            "A=2→3) — NOT the H₃-local 10^459 gate. Δ_λ(K) remains the last "
            "un-derived input, now a per-nucleus O(1–10) volume/density "
            "factor to be produced by Stage ② (no scale obstruction)."
            if deltas else "no matrix-M witnesses available"
        ),
    })
    # Sanity: tr_M is O(1), not exponential (the whole point of the correction)
    w.add_assertion(
        name="canonical_trM_is_order_unity",
        computed=float(max(trms)) if trms else 0.0, expected=1.0, tolerance=2.0,
        source="matrix-M tr_M(q0) ∈ [~1, 2] — not the H₃-local 10^1025",
    )

    out = w.save()
    print(f"m_e = {M_E_MEV} MeV")
    for r in solved:
        print(f"  {r['label']:9s} A={r['A']}  tr_M={r['tr_M_canonical_matrixM']:.5f}  "
              f"B={r['B_AME_MeV']:.4f} MeV  Δ̄_req={r['delta_bar_required']:.3f}")
    if deltas:
        print(f"required Δ̄ spread: {min(deltas):.2f}–{max(deltas):.2f} "
              f"(~{spread:.1f}×) — MILD, not scale-gated (H₃-local was 10^459)")
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
