#!/usr/bin/env python3
"""Value leg — the Slater↔trace dictionary FUNCTIONAL FORM (sign-determined).

Scoping: docs/design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md.
Continuing the value: the connected-cumulant DEFICIT probe found the framework's
multiplicative model supplies ~6% of b₄ with a WRONG-SIGNED b₃. This unit derives
what functional the [1^4] connected term must have, purely from the SIGN pattern of
the AME connected cumulants — no fit, no magnitude assumption.

SETUP. Any linked-cluster (determinant) binding has the form
    B = s · ln det(I + G) = s · Σ_k (−1)^{k-1}/k · tr(G^k),
so the connected k-body cumulant b_k has sign  s·(−1)^{k-1}·sign(λ)^k, where λ is
the dominant eigenvalue of the exchange matrix G.

REQUIREMENT. The AME connected cumulants are ALL POSITIVE: (b₂,b₃,b₄) = (+,+,+)
(2.225, 1.426, 9.243 MeV). Solving the sign pattern over (s, sign λ):

    s=+1, λ>0 : (−,+,−)      s=+1, λ<0 : (−,−,−)
    s=−1, λ>0 : (+,−,+)      s=−1, λ<0 : (+,+,+)   ← UNIQUE all-positive

RESULT (scope-(b), sign-exact — a functional-form constraint, not a fit):
    The [1^4] connected binding must be   B = −ln det(I + G_exchange)
    with a dominant-NEGATIVE-eigenvalue (net-ATTRACTIVE antisymmetric) exchange
    matrix G. UNIQUE among the four determinant sign-branches.

RULES OUT (both fail the sign pattern):
  • the multiplicative product 1−∏f (deficit probe: b₃ wrong-signed), and
  • the naive positive-g Slater det +ln det (gives (−,+,−)).

The negative-eigenvalue reading is physical: the fully-antisymmetric [1^4] channel
is the BOUND α (attractive), exactly the Wigner supermultiplet closed shell the gate
encodes. NEXT UNIT: build G_exchange from the framework pair factors (z, z−h/2) at
the nucleon-flavor level (Λ^A(4)), verify its dominant eigenvalue is negative, and
read the b₄ magnitude from −ln det — checked vs 9.243 as a verdict, never fitted.

`-- Ref:` spec §2 (Λ^A(4) projector); b4_framework_connected_cumulant_deficit.py;
b4_value_cumulant_target_probe.py (AME cumulants).
"""
from __future__ import annotations

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


def cumulant_signs(s: int, sign_lambda: int) -> list[str]:
    """Sign of b_k = s·(−1)^{k-1}·sign(λ)^k for k=2,3,4."""
    out = []
    for k in (2, 3, 4):
        val = s * ((-1) ** (k - 1)) * (sign_lambda ** k)
        out.append("+" if val > 0 else "-")
    return out


def main() -> int:
    ame_pattern = ["+", "+", "+"]  # AME b2,b3,b4 all positive
    branches = {}
    unique_solution = None
    for s in (+1, -1):
        for sl in (+1, -1):
            sig = cumulant_signs(s, sl)
            key = f"s={s:+d},lambda{'>' if sl > 0 else '<'}0"
            branches[key] = "".join(sig)
            if sig == ame_pattern:
                unique_solution = key

    is_unique = sum(1 for v in branches.values() if v == "+++") == 1

    result = {
        "ame_cumulant_signs": "(+,+,+)",
        "determinant_branches": branches,
        "unique_all_positive_branch": unique_solution,
        "is_unique": bool(is_unique),
        "functional_form": "B = − ln det(I + G_exchange), dominant-NEGATIVE-eigenvalue (attractive) G",
        "rules_out": ["multiplicative product 1−∏f (b3 wrong-signed)",
                      "naive positive-g Slater det +ln det (gives (−,+,−))"],
        "verdict": (
            "The sign pattern UNIQUELY fixes the [1^4] connected binding functional as "
            "B = −ln det(I + G_exchange) with a net-attractive (dominant-negative-eigenvalue) "
            "exchange matrix — the only one of four determinant branches giving all-positive "
            "connected cumulants (matching AME). Physical: the antisymmetric [1^4] channel is "
            "the bound α. Rules out the product and positive-g det. Scope-(b) (sign-exact), no fit. "
            "NEXT: build G from the nucleon-flavor pair factors, check λ<0, read b₄ from −ln det."),
    }

    payload = {
        "computation": "b4-slater-dictionary-functional-form",
        "description": ("Sign-determined functional form of the [1^4] connected binding: "
                        "B=−ln det(I+G) with net-attractive exchange is the UNIQUE determinant "
                        "branch giving all-positive AME cumulants; rules out the product and the "
                        "positive-g det. audit-only, sign-exact, no fit."),
        "tier": "structural (sign-pattern uniqueness over determinant linked-cluster branches)",
        "result": result,
        "context": {
            "axis": "GAP-A-4 class-D — [1^4] value leg, Slater↔trace dictionary functional form",
            "spec": "docs/design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md",
            "next_unit": "build G_exchange (nucleon-flavor pair factors), verify λ<0, read b₄ magnitude",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "b4-slater-dictionary-functional-form", payload,
        script_path=__file__, engine="python", output_dir=os.path.join(COMP, "probes"),
    )
    wb.add_assertion("all_positive_branch_is_unique", computed=str(bool(is_unique)), expected="True")
    wb.add_assertion("functional_is_minus_logdet_attractive",
                     computed=str(unique_solution), expected="s=-1,lambda<0")
    out = wb.save(extra={"auditOnly": True})

    print("=== Slater↔trace dictionary — functional form from the cumulant sign pattern ===")
    print(f"  AME connected-cumulant signs (b2,b3,b4): {tuple(ame_pattern)}")
    for k, v in branches.items():
        mark = "  <== UNIQUE all-positive" if v == "+++" else ""
        print(f"  {k:16} -> (b2,b3,b4)=({v[0]},{v[1]},{v[2]}){mark}")
    print()
    print("  => [1^4] connected binding: B = − ln det(I + G_exchange), net-ATTRACTIVE (λ<0).")
    print("     rules out: multiplicative product (b3 wrong sign) AND positive-g det (−,+,−).")
    print("  NEXT: build G from nucleon-flavor pair factors, verify λ<0, read b₄ vs 9.243.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
