#!/usr/bin/env python3
"""Value leg — the connected 4-body cumulant target b₄, and why existing forms give 0.

Scoping: docs/scope/2026-07-05-gap-a4-ursell-operator-magnitude-scoping.md §3.
After the three gates (I-par bar-even projection, I-conn irreducibly connected,
I-ceil ~14% headroom), this unit is the first honest step of the b₄^even VALUE:
compute the exact TARGET the [1^4] operator must supply, and show the value cannot
be shortcut from any existing binding form.

(A) TARGET — the connected 4-body cumulant of ⁴He (Ursell/cluster inversion of
AME, non-circular: a body-order DEFINITION of the measured binding, not a fit):

    B(A) = C(A,2)·b₂ + C(A,3)·b₃ + C(A,4)·b₄ + …
    b₂ = B(D)                       = 2.2245 MeV   (the pair)
    b₃ = B̄(3-body) − 3·b₂           = 1.4264 MeV   (connected 3-body; B̄ = avg ³H/³He)
    b₄ = B(⁴He) − 6·b₂ − 4·b₃       = 9.2431 MeV   (connected 4-body — the [1^4] TARGET)
    exact: 6·b₂ + 4·b₃ + b₄ = 28.2957 = B(⁴He).

So the [1^4]-projected connected operator must supply **b₄ ≈ 9.24 MeV**. This sits
comfortably inside the I-ceil room (16.8 MeV) — the gate margin is real.

(B) WHY NO SHORTCUT — the connected b₄ is orthogonal to every existing form:
  • B_sym = α·Σ_bonds L_bond  is 2-body ADDITIVE  ⇒ connected b_k = 0 for k ≥ 3.
  • B_vol = a_V·A            is 1-body LINEAR    ⇒ connected b_k = 0 for k ≥ 2.
  • B_gate = E₀·ln(1/W_λ)    is a single-partition collective scalar, not a
    body-order cumulant expansion (no separable connected 4-body slice).
So the framework's current trace binding produces connected **b₄ = 0** — which is
exactly why B_sym under-binds ⁴He (11.97 vs 28.30). The missing 9.24 MeV is
entirely absent from the present formulation.

VERDICT (scope-(a), no fit): the value target is b₄ = 9.24 MeV (AME cumulant,
non-circular); existing forms supply 0; the [1^4] connected operator is a genuinely
NEW object. The remaining core — the b₄^even VALUE from the [1^4]-projected
4-nucleon Markov trace on the ⁴He χ (77 partitions) via the branching combiner —
is the multi-session compute, now with an exact target and a cleared ceiling.
NO 2.093× / 9.24 reverse-engineering — the operator is built parameter-free and
its value compared to this target.

`-- Ref:` scoping §3; standard-part-functor.md (B_sym/B_vol forms); AME2020.
"""
from __future__ import annotations

import os
import sys
from math import comb
from pathlib import Path

import mpmath as mp

# Path bridge (moved above the set_compute_dps() call — it is what
# puts computations/substrate on sys.path so `_precision` resolves).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from substrate.witness_base import WitnessBuilder  # noqa: E402

COMP = str(_COMP)


def main() -> int:
    B = {"D": mp.mpf("2.22452"), "3H": mp.mpf("8.48180"),
         "3He": mp.mpf("7.71804"), "4He": mp.mpf("28.29567")}
    b2 = B["D"]
    B3 = (B["3H"] + B["3He"]) / 2
    b3 = B3 - comb(3, 2) * b2
    b4 = B["4He"] - comb(4, 2) * b2 - comb(4, 3) * b3
    recon = comb(4, 2) * b2 + comb(4, 3) * b3 + b4
    i_ceil_room = mp.mpf("16.811")

    result = {
        "cumulants_MeV": {"b2_pair": mp.nstr(b2, 8), "b3_connected_3body": mp.nstr(b3, 8),
                          "b4_connected_4body_TARGET": mp.nstr(b4, 8)},
        "reconstruction_check": {"sum_6b2_4b3_b4": mp.nstr(recon, 8),
                                 "B_4He": mp.nstr(B["4He"], 8),
                                 "exact": bool(abs(recon - B["4He"]) < mp.mpf(10) ** -20)},
        "target_within_iceil_room": bool(b4 < i_ceil_room),
        "existing_forms_connected_b4": {
            "B_sym": "0 (2-body additive)", "B_vol": "0 (1-body linear)",
            "B_gate": "n/a (single-partition collective, not a cumulant expansion)"},
        "verdict": (
            "Value TARGET = connected 4-body cumulant b₄ ≈ 9.243 MeV (AME Ursell inversion, "
            "non-circular). Existing trace forms supply connected b₄ = 0 (B_sym 2-body, B_vol "
            "1-body) — orthogonal, no shortcut. b₄ sits inside the I-ceil room (16.8 MeV). The "
            "remaining core is the b₄^even VALUE from the [1^4]-projected 4-nucleon Markov trace "
            "(77-partition ⁴He χ + branching combiner) — multi-session, now with an exact target "
            "and cleared ceiling. Built parameter-free; NO fit to b₄. Scope-(a)."),
    }

    payload = {
        "computation": "b4-value-cumulant-target",
        "description": ("Value leg step 1: the connected 4-body cumulant of ⁴He is b₄=9.243 MeV "
                        "(AME Ursell inversion), the exact non-circular target for the [1^4] "
                        "operator; existing forms (B_sym 2-body, B_vol 1-body) supply connected "
                        "b₄=0 ⇒ no shortcut, a new operator is required. audit-only, no fit."),
        "tier": "structural (exact cumulant inversion of AME; body-order argument on existing forms)",
        "result": result,
        "context": {
            "axis": "GAP-A-4 class-D — [1^4] Ursell operator magnitude, VALUE leg",
            "scoping": "docs/scope/2026-07-05-gap-a4-ursell-operator-magnitude-scoping.md §3",
            "gates_cleared": "I-par (#3395), I-conn (#3398), I-ceil (#3400)",
            "remaining": "b₄^even value = [1^4]-projected 4-nucleon Markov trace (branching combiner + 77-partition ⁴He χ)",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "b4-value-cumulant-target", payload,
        script_path=__file__, engine="python+mpmath", output_dir=os.path.join(COMP, "probes"),
    )
    wb.add_assertion("cumulant_reconstruction_exact", computed=mp.nstr(recon, 8), expected=mp.nstr(B["4He"], 8), tolerance=1e-6)
    wb.add_assertion("b4_target_within_iceil_room", computed=str(bool(b4 < i_ceil_room)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Value leg step 1 — connected 4-body cumulant target ===")
    print(f"  b2 (pair)             = {float(b2):.4f} MeV")
    print(f"  b3 (connected 3-body) = {float(b3):.4f} MeV")
    print(f"  b4 (connected 4-body) = {float(b4):.4f} MeV   <- [1^4] TARGET (exact AME cumulant)")
    print(f"  reconstruction 6b2+4b3+b4 = {float(recon):.4f} = B(4He)  (exact)")
    print(f"  within I-ceil room (16.8 MeV): {bool(b4 < i_ceil_room)}")
    print("  existing forms connected b4: B_sym=0 (2-body), B_vol=0 (1-body) — orthogonal, no shortcut.")
    print("  remaining core: [1^4]-projected 4-nucleon Markov trace value. No fit to b4.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
