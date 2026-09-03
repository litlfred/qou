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

RESULT (non-circular -- framework's own binding decomposed; no fit): every number
is DERIVED at run time and printed below; none is written into this docstring.

  This block used to carry the numbers inline, and they went stale: it read
  b2=3.056, b3=-2.525, b4=+0.583 (6.3% of target) from the convention-C era.
  Under canonical convention D the live values are b2=1.927, b3=-1.388,
  b4=-0.304 -- and b4 has changed SIGN, so the deficit is 103% rather than 94%
  and the [1^4] term must reverse b4 as well as b3.  Those D-frame figures are
  quoted here only to explain the correction; the producer no longer depends on
  them.  See bean qou-jqla.

VERDICT (scope-(a), no fit): the framework's existing multiplicative model supplies
a small and WRONG-SIGNED connected b4 together with a wrong-signed b3, so the [1^4]
Slater term (Λ^A(4) nucleon-flavor antisymmetrizer, per the spec) must supply the
whole of the 4-body AND repair both signs. This is the honest baseline; it does NOT
compute the [1^4] value (that needs the Slater↔trace dictionary — the next unit), it
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
    b4_wrong_sign = (b4 < 0) and (ame["b4"] > 0)
    # What the [1^4] term must supply, as a fraction of the target. When b4 is
    # itself negative this EXCEEDS 1: the term must reverse the sign as well as
    # close the gap. The old hardcoded "~94%" silently assumed b4 > 0.
    deficit_frac = 1 - frac_b4

    result = {
        "framework_multiplicative_binding_MeV": {
            "D": mp.nstr(BD, 8), "3He": mp.nstr(B3He, 8),
            "3H": mp.nstr(B3H, 8), "4He": mp.nstr(B4, 8)},
        "framework_connected_cumulants_MeV": {
            "b2": mp.nstr(b2, 8), "b3": mp.nstr(b3, 8), "b4": mp.nstr(b4, 8)},
        "ame_target_cumulants_MeV": {k: mp.nstr(v, 8) for k, v in ame.items()},
        "b4_fraction_of_target": mp.nstr(frac_b4, 6),
        "b3_wrong_sign": bool(b3_wrong_sign),
        "b4_wrong_sign": bool(b4_wrong_sign),
        "deficit_fraction_the_slater_term_must_supply": mp.nstr(deficit_frac, 6),
        "verdict": (
            f"Framework multiplicative complete-graph model supplies connected "
            f"b4 = {mp.nstr(b4, 4)} MeV = {float(frac_b4) * 100:.1f}% of the "
            f"{mp.nstr(ame['b4'], 5)} target"
            + (", itself WRONG-SIGNED" if b4_wrong_sign else "")
            + f", and a {'WRONG-SIGNED' if b3_wrong_sign else 'correctly-signed'} "
            f"b3 ({mp.nstr(b3, 4)} vs {mp.nstr(ame['b3'], 4)}). So the [1^4] "
            f"Slater term must supply ~{float(deficit_frac) * 100:.0f}% of the "
            f"4-body AND repair the 3-body sign"
            + (" and the 4-body sign" if b4_wrong_sign else "")
            + ". This measures the DEFICIT, not the [1^4] value (that needs the "
            "Slater-to-trace dictionary). Scope-(a), no fit."),
    }

    payload = {
        "computation": "b4-framework-connected-cumulant-deficit",
        "description": (
            f"Framework multiplicative complete-graph connected cumulants (Ursell "
            f"inversion of committed pair factors): b4={mp.nstr(b4, 4)} MeV = "
            f"{float(frac_b4) * 100:.1f}% of the {mp.nstr(ame['b4'], 5)} target"
            + (" and wrong-signed" if b4_wrong_sign else "")
            + ", b3 wrong-signed. Quantifies the deficit the [1^4] Slater term "
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
    # The old assertion pinned expected="0.063", the convention-C measurement, as
    # though it were a prediction. It is not: it was a RECORD of a past run, so it
    # went red the moment the frame changed and could only ever be "fixed" by
    # editing the number -- which is the laundering the precision discipline
    # forbids. Assert the PROPOSITION the probe exists to establish instead, and
    # carry the value in the data block where a changing number belongs.
    #
    # "far below" is made explicit as < 50% of target. That threshold is a stated
    # reading of the words, not a tuned parameter: the live value is -3.3% and the
    # C-frame value was 6.3%, so the claim holds in both frames by a wide margin.
    wb.add_assertion("framework_b4_far_below_target",
                     computed=str(bool(frac_b4 < mp.mpf("0.5"))), expected="True")
    wb.add_assertion("framework_b3_wrong_sign", computed=str(bool(b3_wrong_sign)), expected="True")
    # NEW under convention D, and a strengthening rather than a weakening: b4 is
    # not merely small, it is negative against a positive target.
    wb.add_assertion("framework_b4_wrong_sign", computed=str(bool(b4_wrong_sign)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Framework connected-cumulant deficit (multiplicative complete-graph) ===")
    print(f"  binding MeV:  D={float(BD):.3f}  3He={float(B3He):.3f}  3H={float(B3H):.3f}  4He={float(B4):.3f}")
    print(f"  framework cumulants:  b2={float(b2):.3f}  b3={float(b3):.3f}  b4={float(b4):.3f} MeV")
    print(f"  AME target:           b2={float(ame['b2']):.3f}  b3={float(ame['b3']):.3f}  b4={float(ame['b4']):.3f} MeV")
    print(f"  connected b4 fraction supplied: {float(frac_b4)*100:.1f}%   b3 wrong-signed: {b3_wrong_sign}")
    print(f"  ⇒ [1^4] Slater term must supply ~{float(deficit_frac) * 100:.0f}% of b4"
          + (" (b4 is WRONG-SIGNED, so it must reverse it too)" if b4_wrong_sign else "")
          + " AND fix the b3 sign. Deficit measured; value TBD.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
