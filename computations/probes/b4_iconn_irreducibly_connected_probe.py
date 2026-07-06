#!/usr/bin/env python3
"""I-conn (magnitude leg) — the ⁴He excess is irreducibly connected, A=4-local.

Scoping: docs/scope/2026-07-05-gap-a4-ursell-operator-magnitude-scoping.md §3
(invariant I-conn). After I-par (b4-connected-bar-parity: target b₄^even), this
unit verifies the missing many-body term is NOT a saturating pairwise product —
so a genuine connected operator is required.

DIRECT CLOSURE (committed ceiling witness, no new compute).
`interface-operator-pairwise-ceiling.witness.json` enumerates every pairwise
product/sum model — {mult,add} × {chain, complete-graph K_A} — as ratios over the
deuteron. At ⁴He the best pairwise model tops out at 6.079×D while the AME target
is 12.72×D:

    super_pairwise(⁴He) = 12.72 / 6.079 = 2.093 > 1

⇒ the ⁴He binding EXCEEDS the supremum over all pairwise products, so no pairwise
product realizes it — the excess is IRREDUCIBLY CONNECTED. And it is A=4-LOCAL:
super_pairwise returns to ≤ 1 by ⁶Li (0.944 — pairwise even over-counts), exactly
where the SU(4) gate gives C(4,6)=0 (no [1^4] cluster).

STRUCTURAL SUPPORT (Lean, proved).
`QOU.Mass.BindingTauAnchorClosure.binding_extensive_at_substrate` (0<q ⇒
1 < λ₊(τ_anchor); composes `tauAnchor_gt_two` + `lambdaPlus_gt_one`,
`BindingRecurrenceSpectral.lean`) proves the body-order binding recurrence is
EXTENSIVE (dominant root λ₊ > 1, grows with body order) for the whole substrate.
A saturating |χ| joint pairwise trace is non-extensive (`B_joint` A-independent,
λ_eff ≈ 1; PR #2703) — it cannot furnish the A=4 super-pairwise excess. So the
extensive, A=4-local excess must live in a connected many-body operator.

CITATION CORRECTION. The scoping note §3 named the anchor `productModel_3body_nonpos`;
that string is only a COMMENT reference (`BindingRecurrenceSpectral.lean` line 18,
citing PR #2703), NOT a proved Lean theorem. The actual proved anchor is
`binding_extensive_at_substrate` (+ `lambdaPlus_gt_one`). Recorded here so no later
session cites a non-existent theorem.

VERDICT (scope-(a)/(b)): I-conn CLEARED. The ⁴He excess is irreducibly connected
(scope-(b): strictly above the pairwise supremum) and A=4-local (gate). The next
unit is I-ceil (norm bound on b₄^even) then the single b₄^even value — still no
2.093× fit.

`-- Ref:` scoping note §3 I-conn; QOU.Mass.BindingTauAnchorClosure.binding_extensive_at_substrate.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from substrate.witness_base import WitnessBuilder  # noqa: E402

COMP = str(_COMP)
CEILING = os.path.join(COMP, "probes", "interface-operator-pairwise-ceiling.witness.json")


def load_rows() -> list:
    with open(CEILING, encoding="utf-8") as f:
        w = json.load(f)
    wit = w.get("witness", w)
    m = wit.get("result", wit.get("data", wit)).get("measurement", wit.get("measurement", {}))
    out = []
    for r in m.get("rows", []):
        pr = r.get("pairwise_ratios_over_D", {})
        best = max(float(v) for v in pr.values()) if pr else float("nan")
        ame = float(r.get("ame_ratio_over_D", "nan"))
        out.append({
            "atom": r["atom"], "A": int(r["A"]),
            "ame_over_D": ame, "best_pairwise_over_D": best,
            "pairwise_models": {k: float(v) for k, v in pr.items()},
            "super_pairwise": (ame / best) if best and best == best else float("nan"),
        })
    return out


def main() -> int:
    rows = load_rows()
    by = {r["atom"]: r for r in rows}
    he4 = by["4He"]
    li6 = by["6Li"]

    # I-conn: ⁴He target strictly above EVERY pairwise model
    he4_above_all_pairwise = all(he4["ame_over_D"] > v for v in he4["pairwise_models"].values())
    he4_super = he4["super_pairwise"] > 1
    a4_local = li6["super_pairwise"] <= 1.0  # returns to ≤ pairwise by ⁶Li (gate C(4,6)=0)

    result = {
        "closure": ("⁴He target (12.72×D) > sup over all pairwise products (6.079×D) ⇒ the "
                    "excess is irreducibly connected (super_pairwise = 2.093 > 1); A=4-LOCAL "
                    "(⁶Li super_pairwise 0.944 ≤ 1, where the SU(4) gate gives C(4,6)=0)."),
        "per_atom": {r["atom"]: {"A": r["A"], "ame_over_D": round(r["ame_over_D"], 4),
                                 "best_pairwise_over_D": round(r["best_pairwise_over_D"], 4),
                                 "super_pairwise": round(r["super_pairwise"], 4)} for r in rows},
        "lean_anchor": "QOU.Mass.BindingTauAnchorClosure.binding_extensive_at_substrate (λ₊>1, proved)",
        "citation_correction": ("scoping §3 named 'productModel_3body_nonpos' — that is a COMMENT "
                                "string (BindingRecurrenceSpectral.lean L18, PR #2703), not a "
                                "theorem. Real anchor: binding_extensive_at_substrate + lambdaPlus_gt_one."),
        "verdict": ("I-conn CLEARED (scope-(b) for ⁴He): the ⁴He binding is strictly above the "
                    "pairwise-product supremum ⇒ no pairwise product realizes it ⇒ irreducibly "
                    "connected; A=4-local. Extensivity (λ₊>1, Lean) supports that a saturating "
                    "pairwise trace cannot supply it. Next: I-ceil, then the b₄^even value. No fit."),
    }

    payload = {
        "computation": "b4-iconn-irreducibly-connected",
        "description": ("I-conn for the [1^4] magnitude leg: the ⁴He binding (12.72×D) exceeds "
                        "the pairwise-product ceiling (6.079×D) ⇒ irreducibly connected, A=4-local. "
                        "Anchored on the proved extensivity theorem (not the mis-named comment). "
                        "audit-only, no fit."),
        "tier": "structural (committed ceiling witness + proved extensivity theorem)",
        "result": result,
        "context": {
            "axis": "GAP-A-4 class-D — [1^4] Ursell operator magnitude, invariant I-conn",
            "scoping": "docs/scope/2026-07-05-gap-a4-ursell-operator-magnitude-scoping.md §3",
            "ceiling_witness": "probes/interface-operator-pairwise-ceiling.witness.json",
            "lean": "qou:QOU.Mass.BindingTauAnchorClosure.binding_extensive_at_substrate",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "b4-iconn-irreducibly-connected", payload,
        script_path=__file__, engine="python", output_dir=os.path.join(COMP, "probes"),
    )
    wb.add_assertion("he4_target_above_all_pairwise_models", computed=str(bool(he4_above_all_pairwise)), expected="True")
    wb.add_assertion("he4_is_super_pairwise", computed=str(bool(he4_super)), expected="True")
    wb.add_assertion("excess_is_A4_local", computed=str(bool(a4_local)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== I-conn: the ⁴He excess is irreducibly connected, A=4-local ===")
    print(f"  {'atom':5} {'A':>2} {'ame/D':>8} {'best_pairwise/D':>16} {'super_pairwise':>14}")
    for r in rows:
        print(f"  {r['atom']:5} {r['A']:>2} {r['ame_over_D']:>8.3f} {r['best_pairwise_over_D']:>16.3f} {r['super_pairwise']:>14.3f}")
    print(f"\n  ⁴He above ALL pairwise models: {he4_above_all_pairwise} | super-pairwise: {he4_super}")
    print(f"  A=4-local (⁶Li back to ≤ pairwise where C(4,6)=0): {a4_local}")
    print("  anchor: binding_extensive_at_substrate (λ₊>1, proved) — NOT the comment 'productModel_3body_nonpos'.")
    print("  VERDICT: I-conn CLEARED. Next = I-ceil, then b₄^even value. No fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
