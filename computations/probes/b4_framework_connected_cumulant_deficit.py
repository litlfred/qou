#!/usr/bin/env python3
"""Value leg — the framework's CURRENT connected-cumulant deficit (multiplicative model).

Scoping: docs/design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md.
After the value target (b₄=9.243 MeV, AME) and the Lean-proved orthogonality
(BodyOrderCumulant: additive B_sym / linear B_vol supply 0), this unit quantifies
how much connected many-body binding the framework's MULTIPLICATIVE complete-graph
model actually produces — the honest baseline the [1^4] Slater term must lift.

Unlike the additive B_sym, the multiplicative binding
    B(K) = E₀·τ_vac·(1 − ∏_{pairs} f_pair)
does carry connected multi-body cumulants (the ∏ cross-terms). Using the committed
pair factors (pp/nn = z, pn = z−h/2; interface_4body_assembly_probe) on the complete
graph K_A, and the Ursell inversion b₂=B(D), b₃=B̄(3)−3b₂, b₄=B(4He)−6b₂−4b₃:

RESULT (non-circular — framework's own binding decomposed; no fit):
    framework:  b₂ = 3.056,  b₃ = −2.525,  b₄ = 0.583 MeV
    AME target: b₂ = 2.225,  b₃ = +1.426,  b₄ = 9.243 MeV

  • connected b₄:  0.583 / 9.243 = 6.3 %  — the multiplicative model supplies only
    ~6 % of the connected 4-body binding (consistent with I-conn: pairwise products
    ceiling below target).
  • connected b₃:  −2.525 vs +1.426 — WRONG SIGN. The multiplicative connected
    structure is not merely small, it is qualitatively wrong at 3-body.

VERDICT (scope-(a), no fit): the framework's existing multiplicative model supplies
~6 % of the connected b₄ and a wrong-signed b₃, so the [1^4] Slater term (Λ^A(4)
nucleon-flavor antisymmetrizer, per the spec) must supply the missing ~94 % of the
4-body AND repair the 3-body sign. This is the honest baseline; it does NOT compute
the [1^4] value (that needs the Slater↔trace dictionary — the next unit), it
measures the DEFICIT the Slater term must close. b₂ over-binds (3.06 vs 2.22) — the
multiplicative deuteron over-prediction, inherited by the inversion.

`-- Ref:` spec §2; interface_4body_assembly_probe.py (pair factors, complete graph);
b4_value_cumulant_target_probe.py (AME target); BodyOrderCumulant.lean (orthogonality).
"""
from __future__ import annotations

import importlib.util
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


def _load_assembly():
    spec = importlib.util.spec_from_file_location(
        "iface4", os.path.join(COMP, "probes", "interface_4body_assembly_probe.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    m = _load_assembly()

    def Bmult(Z, N):
        return mp.mpf(m.binding(Z, N, m.complete_pairs(Z, N), pn="chi"))

    BD, B3He, B3H, B4 = Bmult(1, 1), Bmult(2, 1), Bmult(1, 2), Bmult(2, 2)
    b2 = BD
    B3 = (B3He + B3H) / 2
    b3 = B3 - comb(3, 2) * b2
    b4 = B4 - comb(4, 2) * b2 - comb(4, 3) * b3

    ame = {"b2": mp.mpf("2.2245"), "b3": mp.mpf("1.4264"), "b4": mp.mpf("9.2431")}
    frac_b4 = b4 / ame["b4"]
    b3_wrong_sign = (b3 < 0) and (ame["b3"] > 0)

    result = {
        "framework_multiplicative_binding_MeV": {
            "D": mp.nstr(BD, 8), "3He": mp.nstr(B3He, 8),
            "3H": mp.nstr(B3H, 8), "4He": mp.nstr(B4, 8)},
        "framework_connected_cumulants_MeV": {
            "b2": mp.nstr(b2, 8), "b3": mp.nstr(b3, 8), "b4": mp.nstr(b4, 8)},
        "ame_target_cumulants_MeV": {k: mp.nstr(v, 8) for k, v in ame.items()},
        "b4_fraction_of_target": mp.nstr(frac_b4, 6),
        "b3_wrong_sign": bool(b3_wrong_sign),
        "verdict": (
            "Framework multiplicative complete-graph model supplies connected b₄ = 0.583 MeV = "
            "6.3% of the 9.243 target, and a WRONG-SIGNED b₃ (−2.52 vs +1.43). So the [1^4] "
            "Slater term (Λ^A(4) nucleon-flavor) must supply the missing ~94% of the 4-body AND "
            "repair the 3-body sign. This measures the DEFICIT, not the [1^4] value (that needs "
            "the Slater↔trace dictionary). b₂ over-binds (multiplicative deuteron). Scope-(a), no fit."),
    }

    payload = {
        "computation": "b4-framework-connected-cumulant-deficit",
        "description": ("Framework multiplicative complete-graph connected cumulants (Ursell "
                        "inversion of committed pair factors): b₄=0.58 MeV = 6.3% of the 9.24 "
                        "target, b₃ wrong-signed. Quantifies the deficit the [1^4] Slater term "
                        "must close. audit-only, no fit."),
        "tier": "structural (framework's own multiplicative binding, cumulant-inverted)",
        "result": result,
        "context": {
            "axis": "GAP-A-4 class-D — [1^4] value leg, framework connected-cumulant baseline",
            "spec": "docs/design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md",
            "next_unit": "the Slater↔Markov-trace dictionary → the actual [1^4] connected value",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "b4-framework-connected-cumulant-deficit", payload,
        script_path=__file__, engine="python+mpmath", output_dir=os.path.join(COMP, "probes"),
    )
    wb.add_assertion("framework_b4_far_below_target", computed=mp.nstr(frac_b4, 4), expected="0.063", tolerance=0.02)
    wb.add_assertion("framework_b3_wrong_sign", computed=str(bool(b3_wrong_sign)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Framework connected-cumulant deficit (multiplicative complete-graph) ===")
    print(f"  binding MeV:  D={float(BD):.3f}  3He={float(B3He):.3f}  3H={float(B3H):.3f}  4He={float(B4):.3f}")
    print(f"  framework cumulants:  b2={float(b2):.3f}  b3={float(b3):.3f}  b4={float(b4):.3f} MeV")
    print(f"  AME target:           b2={float(ame['b2']):.3f}  b3={float(ame['b3']):.3f}  b4={float(ame['b4']):.3f} MeV")
    print(f"  connected b4 fraction supplied: {float(frac_b4)*100:.1f}%   b3 wrong-signed: {b3_wrong_sign}")
    print("  ⇒ [1^4] Slater term must supply ~94% of b4 AND fix the b3 sign. Deficit measured; value TBD.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
