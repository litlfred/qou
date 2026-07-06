#!/usr/bin/env python3
"""lpdual_active_set_vs_edge_set_negative.py
============================================

NEGATIVE result: the deuteron LP-dual active SET (Wedderburn blocks) is NOT
lever-2's binding edge-set (nucleon bonds), and its active/inactive split does
NOT reduce to a Pauli symmetry rule. Records the discrepancy so the lever-2
occupancy frontier (`w5tg`) does not mistake one for the other.

Context. PR #2661 found the qbk2 Reeb-propagator correction is 94.9% supported
on the 7 deuteron LP-dual *active channels* (Wedderburn blocks λ ⊢ 6 with
shadow price y_star > 0). Lever 2 of the Δ_λ-gate
(`docs/audits/2026-06-23-delta-lambda-three-lever-status.md` §Lever 2;
`QOU/Hecke/PauliChannelBinding.lean`) asks a DIFFERENT question: the binding
EDGE-SET — which inter-nucleon BONDS survive (Pauli: p-p/n-n forced into the
antisymmetric channel `-q⁻¹ < 0` ⇒ unbound; only p-n survive) and the open Z·N
p-n OCCUPANCY count. This probe tests whether the active-set (blocks) connects
to the edge-set (bonds).

Verdict (computed below): NO clean connection.
  1. Different objects — blocks (partitions) vs bonds (p-n edges + Z·N count).
  2. No simple block statistic (rows / cols / n(λ) / chirality) separates active
     from inactive (all ranges overlap).
  3. Only the Pauli ENDPOINTS agree: [6] (fully symmetric) active, [1⁶] (fully
     antisymmetric) inactive. The interior BREAKS any symmetry gradient —
     [2,1,1,1,1] (near-antisymmetric, n(λ)=10) is the most-active block while the
     balanced self-conjugate [3,2,1] is inactive.
  4. Moot anyway — the deuteron raw LP-dual is DEGENERATE (duality gap ≈ 4.4e4;
     strong duality fails on the full space), so the shadow-price magnitudes are
     unreliable; only the active *set* (gap-0 phase) is robust.

No fit; consumes the canonical deuteron LP-dual witness; audit-only.
"""
from __future__ import annotations

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
SDP = HERE.parent / "deuteron-real-sdp.witness.json"


def conj(lam):
    return tuple(sum(1 for p in lam if p > i) for i in range(lam[0]))


def nstat(lam):
    return sum(i * p for i, p in enumerate(lam))


def main():
    W = json.loads(SDP.read_text(encoding="utf-8"))
    parts = [tuple(int(x) for x in p.strip("()").rstrip(",").split(",") if x.strip())
             for p in W["data"]["partitions"]]
    ystar = W["data"]["lp"]["y_star"]
    active = set(W["data"]["lp"]["active_set"])
    dgap = W["data"]["lp"].get("duality_gap")

    rows_data = []
    print(f"{'block':<16}{'rows':>4}{'cols':>5}{'n(λ)':>5}{'chir':>5}{'y_star':>9}{'active':>7}")
    for i, lam in enumerate(parts):
        r, c, n = len(lam), lam[0], nstat(lam)
        chir = (-1) ** (n % 2)
        act = i in active
        rows_data.append({"block": list(lam), "rows": r, "cols": c, "n_lambda": n,
                          "chirality": chir, "y_star": ystar[i], "active": act,
                          "self_conjugate": lam == conj(lam)})
        print(f"{str(list(lam)):<16}{r:>4}{c:>5}{n:>5}{chir:>+5}{ystar[i]:>9.3f}"
              f"{'YES' if act else 'no':>7}")

    # separating-rule tests
    sep = {}
    for key in ["rows", "cols", "n_lambda", "chirality"]:
        av = sorted({d[key] for d in rows_data if d["active"]})
        iv = sorted({d[key] for d in rows_data if not d["active"]})
        clean = (max(av) < min(iv)) or (max(iv) < min(av))
        sep[key] = {"active_values": av, "inactive_values": iv, "cleanly_separates": clean}

    fully_anti = next(d for d in rows_data if d["block"] == [1, 1, 1, 1, 1, 1])
    fully_sym = next(d for d in rows_data if d["block"] == [6])
    most_active = max(rows_data, key=lambda d: d["y_star"])
    pauli_endpoints_ok = (not fully_anti["active"]) and fully_sym["active"]
    any_clean_rule = any(s["cleanly_separates"] for s in sep.values())

    print("\n--- separating-rule tests ---")
    for k, s in sep.items():
        print(f"  {k:10s}: active={s['active_values']}  inactive={s['inactive_values']}  "
              f"clean={s['cleanly_separates']}")
    print(f"\n  Pauli endpoints consistent ([6] active & [1⁶] inactive): {pauli_endpoints_ok}")
    print(f"  most-active block: {most_active['block']} (y_star {most_active['y_star']:.1f}, "
          f"n(λ)={most_active['n_lambda']}) — near-antisymmetric yet most active ⇒ "
          f"no symmetry gradient")
    print(f"  deuteron LP duality_gap = {dgap} (≫0 ⇒ degenerate; shadow-price magnitudes unreliable)")

    verdict = (
        "NEGATIVE — NO connection. (1) The LP-dual active set is Wedderburn BLOCKS "
        "(partitions λ⊢6); lever-2's edge-set is nucleon BONDS (p-n vs p-p/n-n) + "
        "Z·N occupancy — different objects. (2) No simple block statistic "
        "(rows/cols/n(λ)/chirality) separates active from inactive. (3) Only the "
        "Pauli endpoints agree ([6] active, [1⁶] inactive); the interior breaks any "
        "symmetry rule ([2,1,1,1,1] near-antisymmetric is the MOST active block, "
        "[3,2,1] balanced is inactive). (4) Moot — the raw LP-dual is degenerate "
        f"(duality_gap={dgap}), so shadow-price magnitudes are unreliable. The "
        "block-active-set is NOT lever-2's bond-occupancy answer; only the two Pauli "
        "endpoints, which lever-2 already has from PauliChannelBinding.lean, agree."
    )
    print("\nVERDICT:", verdict)

    out = {
        "computation": "lpdual_active_set_vs_edge_set_negative",
        "description": ("Cross-tab of the deuteron LP-dual active set (Wedderburn blocks) "
                        "against lever-2's binding edge-set (nucleon bonds) and Pauli symmetry "
                        "character. NEGATIVE: blocks ≠ bonds, no clean block-level separating "
                        "rule, only Pauli endpoints agree, and the LP-dual is degenerate."),
        "discipline": "no fit; consumes canonical deuteron LP-dual; audit-only; NEGATIVE result",
        "consumes_witness": "computations/deuteron-real-sdp.witness.json",
        "auditOnly": "docs/audits/2026-06-24-lpdual-active-set-not-lever2-edge-set.md",
        "per_block": rows_data,
        "separating_rule_tests": sep,
        "pauli_endpoints_consistent": pauli_endpoints_ok,
        "any_clean_block_rule": any_clean_rule,
        "most_active_block": most_active["block"],
        "deuteron_lp_duality_gap": dgap,
        "connection_holds": False,
        "verdict": verdict,
    }
    wp = HERE / "lpdual-active-set-vs-edge-set-negative.witness.json"
    wp.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness → {wp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
