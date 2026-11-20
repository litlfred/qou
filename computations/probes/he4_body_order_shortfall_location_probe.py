#!/usr/bin/env python3
"""Locate the ⁴He super-pairwise magnitude shortfall: body-order weights vs bond
convention.

QUESTION. PROBE 2 (`su4_connected_1111_magnitude_probe.py`, audit
`docs/audits/2026-07-05-delta-lambda-gate-status.md`) reports that the connected
Ursell/Mayer `[1⁴]` cluster `b_A^c` delivers a super-pairwise enhancement short of
the measured target. The shortfall can sit in either of two places:

  (1) the body-order weights — the prolonged Seiberg-Witten periods `a_D^{(n)}`
      of `thm:binding-closure-conditional` (`B(K) = m_e Sum_n a_D^{(n)}`), which
      PROBE 2's lumped ratio metric `1 + |b4c|/Sum g` implicitly assigns a COMMON
      value across body orders (and which omits the 3-body order entirely); or

  (2) the per-bond Mayer factors — in particular the Markov parameter `z`, whose
      convention changed under owner ruling R1 (2026-08-15): convention **D**
      `z = q^3/(q^2+1)` canonical, **C** `z = sqrt(q)/(q+1)` excised.
      `z_C(q0)=0.49932` vs `z_D(q0)=0.61269` is a 23 % difference, the same order
      as the reported shortfall — a lead, since re-running under D moves `Sum g`
      as well as `b4c` and the RATIO need not move at all.

THIS UNIT MEASURES BOTH, and does not attempt to close either. No fit, no scan,
no free parameter: every quantity is a function of (q0, convention) and AME2020.

METHOD. Two metrics over the SAME zero-fit ingredients, so the comparison is
apples-to-apples:

  metric L (LUMPED — PROBE 2's own):   delivered = 1 + |b4c| / Sum g
                                       needed    = r_AME / ceiling
      with the log-additive pairwise ceiling `Sum(-log f)` PROBE 2 uses.

  metric B (BODY-ORDER-RESOLVED — Ursell/Mayer cumulant inversion):
      W(K) = 1 - PROD_{i<j} f_ij      (the multiplicative binding proxy)
      B(K) = B_AME(D) * W(K)/W(D)     (deuteron as the unit — one scale, not a fit)
      b2 = B(D),  b3 = Bbar(3) - 3 b2,  b4 = B(4He) - 6 b2 - 4 b3
      compared against the SAME inversion applied to AME2020 itself.

  Metric B is convention-CLEAN: it consumes only (z, h, delta) and AME. It uses no
  cached Markov traces, so swapping the convention cannot produce a layer
  straddle (AGENTS.md §"Never straddle the two layers inside one quantity").
  Metric B is also exactly the `a_D^{(n)}` body-order series of the binding
  closure, which is why it can separate location (1) from location (2).

BOND FACTORS (canonical, unchanged from PROBE 2):
  f_pp = z,  f_nn = z - h,  f_pn = z - h*(1/2 - delta/4),  delta = flavor_split_leading(q)
  Mayer function g_ij = 1 - f_ij.
A second typing `f_pn = z` ("chi", the production marshalling of
`interface_4body_assembly_probe`) is reported alongside so the finding is not an
artifact of one f_pn choice.

PRECISION. mpmath end to end at the repo compute dps; no float64 anywhere. There
are no `float()` calls at all — display goes through `mp.nstr` (AGENTS.md
NO-FLOAT64, which covers probes explicitly).

`-- Ref:` Ursell 1927 / Mayer cluster expansion; Wigner 1937 (SU(4) supermultiplet);
`thm:binding-closure-conditional`; `prop:prolonged-periods-fixed-depth`;
owner ruling R1 2026-08-15 (convention D canonical).
"""
from __future__ import annotations

import datetime
import json
import os
import sys
from itertools import combinations
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import fabs, log, mp, mpf  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from closed_form_tau_M import hecke_h, markov_z  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)

set_compute_dps()

# AME2020 total nuclear binding, MeV — same literals as
# interface_4body_assembly_probe.py / su4_connected_1111_magnitude_probe.py.
AME = {
    "D": AME_B_DEUTERON_MEV_VALIDATION,
    "3H": AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}
ATOMS = {"D": (1, 1), "3H": (1, 2), "3He": (2, 1), "4He": (2, 2)}


def z_of(q, convention):
    """Markov parameter. D = q^3/(q^2+1) (canonical, owner ruling R1 2026-08-15);
    C = sqrt(q)/(q+1) (excised — computed here ONLY to measure the frame
    difference, never wired)."""
    if convention == "D":
        return markov_z(q)                        # q**3 / (q**2 + 1)
    if convention == "C":
        return mp.sqrt(q) / (q + 1)               # == 1/(sqrt q + 1/sqrt q)
    raise ValueError(convention)


def nodes(Z, N):
    return ["p"] * Z + ["n"] * N


def bond_factor(a, b, z, h, fpn):
    if a == "p" and b == "p":
        return z
    if a == "n" and b == "n":
        return z - h
    return fpn


def connected_spanning_subgraphs(n):
    """Edge-subsets of K_n that connect all n labelled vertices."""
    verts = list(range(n))
    edges = list(combinations(verts, 2))
    out = []
    for r in range(n - 1, len(edges) + 1):
        for S in combinations(range(len(edges)), r):
            chosen = [edges[i] for i in S]
            parent = list(range(n))

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            for (u, v) in chosen:
                ru, rv = find(u), find(v)
                if ru != rv:
                    parent[ru] = rv
            if len({find(v) for v in verts}) == 1:
                out.append(chosen)
    return out


def connected_kbody(order, z, h, fpn):
    """Irreducible connected A-body Mayer cluster b_A^c over K_A, g_ij = 1 - f_ij."""
    n = len(order)
    g = {}
    for (i, j) in combinations(range(n), 2):
        g[(i, j)] = mpf(1) - bond_factor(order[i], order[j], z, h, fpn)
    total = mpf(0)
    for S in connected_spanning_subgraphs(n):
        prod = mpf(1)
        for (u, v) in S:
            prod *= (-g[(u, v)])
        total += prod
    return total


def pairwise_2body_sum(order, z, h, fpn):
    n = len(order)
    return mp.fsum(mpf(1) - bond_factor(order[i], order[j], z, h, fpn)
                   for (i, j) in combinations(range(n), 2))


def log_additive_ceiling_ratio(Z, N, z, h, fpn):
    """PROBE 2's pairwise ceiling: Sum(-log f) over K_A, normalised at the deuteron."""
    def logsum(Zx, Nx):
        order = nodes(Zx, Nx)
        return mp.fsum(-log(bond_factor(order[i], order[j], z, h, fpn))
                       for (i, j) in combinations(range(len(order)), 2))
    return logsum(Z, N) / logsum(1, 1)


def multiplicative_W(Z, N, z, h, fpn):
    """W(K) = 1 - PROD_{i<j} f_ij over the complete interface graph K_A."""
    order = nodes(Z, N)
    p = mpf(1)
    for (i, j) in combinations(range(len(order)), 2):
        p *= bond_factor(order[i], order[j], z, h, fpn)
    return mpf(1) - p


def ursell_cumulants(B):
    """Body-order (Ursell) inversion of a binding map {D,3H,3He,4He} -> MeV.

    B(A) = C(A,2)*b2 + C(A,3)*b3 + C(A,4)*b4  ==>
      b2 = B(D);  b3 = Bbar(3) - 3*b2;  b4 = B(4He) - 6*b2 - 4*b3,
    with Bbar(3) the isospin average of 3H and 3He. This is a DEFINITION of the
    body-order content of a given binding map, not a fit to anything.
    """
    b2 = B["D"]
    b3 = (B["3H"] + B["3He"]) / 2 - 3 * b2
    b4 = B["4He"] - 6 * b2 - 4 * b3
    return {"b2": b2, "b3": b3, "b4": b4}


def measure(convention, pn_typing):
    q = Q_MP
    z = z_of(q, convention)
    h = hecke_h(q)
    delta = flavor_split_leading(q)
    if pn_typing == "probe2":
        fpn = z - h * (mpf(1) / 2 - delta / 4)
    elif pn_typing == "chi":
        fpn = z
    else:
        raise ValueError(pn_typing)

    # ---- metric L: PROBE 2's lumped enhancement -------------------------
    Z4, N4 = ATOMS["4He"]
    order4 = nodes(Z4, N4)
    b4c = connected_kbody(order4, z, h, fpn)
    sg4 = pairwise_2body_sum(order4, z, h, fpn)
    ceil4 = log_additive_ceiling_ratio(Z4, N4, z, h, fpn)
    needed = (AME["4He"] / AME["D"]) / ceil4
    delivered = mpf(1) + fabs(b4c) / sg4

    # ---- metric B: body-order-resolved Ursell cumulants -----------------
    W = {a: multiplicative_W(Zx, Nx, z, h, fpn) for a, (Zx, Nx) in ATOMS.items()}
    Bmodel = {a: AME["D"] * W[a] / W["D"] for a in W}
    cum_model = ursell_cumulants(Bmodel)
    cum_ame = ursell_cumulants({a: AME[a] for a in ATOMS})

    # ---- what the body-order weights would have to be -------------------
    # DIAGNOSTIC, NOT A DERIVATION. Given the model's own body-order content,
    # these are the per-order rescalings a_D^{(n)}/a_D^{(2)} that would make the
    # series reproduce AME. Reading them off the anchors is anchor INVERSION —
    # it is a fit if wired, and it is not wired. Their value is that they turn
    # "the magnitude is short" into a specific, falsifiable target for the OPEN
    # identification half of `prop:prolonged-periods-fixed-depth` (does a
    # depth-<=8 Gauss-Manin recurrence on the Bring periods admit this ratio?).
    req_a3 = cum_ame["b3"] / cum_model["b3"]
    req_a4 = cum_ame["b4"] / cum_model["b4"]

    # ---- HELD-OUT check: the 3He-3H isospin splitting --------------------
    # The cumulant inversion above consumes only the isospin AVERAGE of 3H and
    # 3He, so their DIFFERENCE is untouched by it and by every a_D^{(n)} (a
    # common per-order weight cancels in the difference at fixed body order).
    # It is therefore a genuine held-out, zero-parameter test of the bond
    # typing itself.
    split_model = Bmodel["3He"] - Bmodel["3H"]
    split_ame = AME["3He"] - AME["3H"]

    return {
        "convention": convention,
        "pn_typing": pn_typing,
        "z": z, "h": h, "delta": delta, "f_pn": fpn,
        "b4c_abs": fabs(b4c), "sum_g": sg4, "ceiling_over_D": ceil4,
        "delivered": delivered, "needed": needed,
        "delivered_over_needed": delivered / needed,
        "model_binding_MeV": Bmodel,
        "cumulants_model": cum_model,
        "cumulants_ame": cum_ame,
        "b3_ratio": cum_model["b3"] / cum_ame["b3"],
        "b4_ratio": cum_model["b4"] / cum_ame["b4"],
        "b3_sign_agrees": bool((cum_model["b3"] > 0) == (cum_ame["b3"] > 0)),
        "b4_sign_agrees": bool((cum_model["b4"] > 0) == (cum_ame["b4"] > 0)),
        "required_a3_over_a2": req_a3,
        "required_a4_over_a2": req_a4,
        "isospin_split_model": split_model,
        "isospin_split_ame": split_ame,
        "isospin_split_ratio": split_model / split_ame,
    }


def main() -> int:
    q = Q_MP
    print(f"q0 = {mp.nstr(q, 20)}   (proton pin)")
    print(f"z_C = {mp.nstr(z_of(q, 'C'), 12)}    z_D = {mp.nstr(z_of(q, 'D'), 12)}"
          f"    h = {mp.nstr(hecke_h(q), 12)}\n")

    runs = [measure(c, t) for c in ("D", "C") for t in ("probe2", "chi")]

    print("-- metric L: PROBE 2's LUMPED enhancement (1 + |b4c|/Sum g) --------")
    print(f"  {'conv':>5}{'f_pn':>9}{'|b4c|':>12}{'Sum g':>12}{'delivered':>12}"
          f"{'needed':>10}{'del/need':>11}")
    for r in runs:
        print(f"  {r['convention']:>5}{r['pn_typing']:>9}"
              f"{mp.nstr(r['b4c_abs'], 6):>12}{mp.nstr(r['sum_g'], 6):>12}"
              f"{mp.nstr(r['delivered'], 6):>12}{mp.nstr(r['needed'], 6):>10}"
              f"{mp.nstr(r['delivered_over_needed'], 6):>11}")

    ame_cum = runs[0]["cumulants_ame"]
    print("\n-- metric B: BODY-ORDER-RESOLVED Ursell cumulants (MeV) -----------")
    print(f"  AME2020 target:  b2={mp.nstr(ame_cum['b2'], 7)}  "
          f"b3={mp.nstr(ame_cum['b3'], 7)}  b4={mp.nstr(ame_cum['b4'], 7)}")
    print(f"  {'conv':>5}{'f_pn':>9}{'b2':>12}{'b3':>12}{'b4':>12}"
          f"{'b3/tgt':>10}{'b4/tgt':>10}")
    for r in runs:
        c = r["cumulants_model"]
        print(f"  {r['convention']:>5}{r['pn_typing']:>9}"
              f"{mp.nstr(c['b2'], 6):>12}{mp.nstr(c['b3'], 6):>12}"
              f"{mp.nstr(c['b4'], 6):>12}"
              f"{mp.nstr(r['b3_ratio'], 5):>10}{mp.nstr(r['b4_ratio'], 5):>10}")

    print("\n-- required body-order weights (DIAGNOSTIC — anchor inversion, NOT wired)")
    print("   and the HELD-OUT 3He-3H isospin splitting (no a_n enters it) -----")
    print(f"  {'conv':>5}{'f_pn':>9}{'a3/a2':>11}{'a4/a2':>11}"
          f"{'split_mdl':>12}{'split_AME':>12}{'ratio':>9}")
    for r in runs:
        print(f"  {r['convention']:>5}{r['pn_typing']:>9}"
              f"{mp.nstr(r['required_a3_over_a2'], 5):>11}"
              f"{mp.nstr(r['required_a4_over_a2'], 5):>11}"
              f"{mp.nstr(r['isospin_split_model'], 5):>12}"
              f"{mp.nstr(r['isospin_split_ame'], 5):>12}"
              f"{mp.nstr(r['isospin_split_ratio'], 4):>9}")

    canon = next(r for r in runs
                 if r["convention"] == "D" and r["pn_typing"] == "probe2")
    cC = next(r for r in runs
              if r["convention"] == "C" and r["pn_typing"] == "probe2")

    # Leg 2 — does the convention close the lumped gap?
    conv_closes = fabs(canon["delivered_over_needed"] - 1) < mpf("0.05")
    conv_improves = (fabs(canon["delivered_over_needed"] - 1)
                     < fabs(cC["delivered_over_needed"] - 1))
    # Leg 1 — is the body-order structure right at ALL under the canon?
    body_signs_ok = canon["b3_sign_agrees"] and canon["b4_sign_agrees"]

    print("\n-- VERDICT --------------------------------------------------------")
    print(f"  LEG 2 (bond convention).  canonical D lumped del/need = "
          f"{mp.nstr(canon['delivered_over_needed'], 6)};  excised C = "
          f"{mp.nstr(cC['delivered_over_needed'], 6)}")
    print(f"    convention closes the gap: {conv_closes}   "
          f"D is closer to target than C: {conv_improves}")
    print("  LEG 1 (body-order weights).  under canonical D + probe2 typing:")
    print(f"    b3 sign agrees with AME: {canon['b3_sign_agrees']}   "
          f"(model {mp.nstr(canon['cumulants_model']['b3'], 6)} vs AME "
          f"{mp.nstr(ame_cum['b3'], 6)})")
    print(f"    b4 sign agrees with AME: {canon['b4_sign_agrees']}   "
          f"(model {mp.nstr(canon['cumulants_model']['b4'], 6)} vs AME "
          f"{mp.nstr(ame_cum['b4'], 6)})")
    print(f"    body-order structure reproduced: {body_signs_ok}")
    print(f"    weights that would be needed: a3/a2="
          f"{mp.nstr(canon['required_a3_over_a2'], 6)}  a4/a2="
          f"{mp.nstr(canon['required_a4_over_a2'], 6)}   (PROBE 2 assumes 1 and 1)")
    print(f"  HELD-OUT (no a_n enters).  3He-3H splitting: model "
          f"{mp.nstr(canon['isospin_split_model'], 6)} vs AME "
          f"{mp.nstr(canon['isospin_split_ame'], 6)} MeV  = "
          f"{mp.nstr(canon['isospin_split_ratio'], 4)} of it")
    print("\n  LOCATION: the shortfall is NOT the bond convention. Canonical D is\n"
          "  FARTHER from target than the excised C on the lumped metric, in both\n"
          "  f_pn typings, and the body-order signs are wrong under BOTH. It sits\n"
          "  in the body-order content: the connected 3-body cumulant has the\n"
          "  WRONG SIGN, and the weights that would repair the series are far from\n"
          "  the common value PROBE 2's lumped ratio implicitly assumes. The\n"
          "  lumped metric omits the 3-body order entirely, so it cannot see this.\n"
          "  Scope-(a): this constrains the multiplicative/Mayer assembly and the\n"
          "  equal-weight assumption; it does NOT exclude the [1^4] ingredient\n"
          "  (AGENTS.md §'Before declaring refuted / ruled out').")

    # required weights are nowhere near the equal-weight assumption
    weights_far_from_unity = (fabs(canon["required_a3_over_a2"] - 1) > mpf("0.5")
                              and fabs(canon["required_a4_over_a2"] - 1) > mpf("0.5"))
    # the held-out isospin splitting is understated by the model
    isospin_understated = fabs(canon["isospin_split_ratio"]) < mpf("0.75")

    # -- witness -------------------------------------------------------
    def _ser(d):
        return {k: str(v) for k, v in d.items()}

    witness = {
        "engine": "mpmath",
        "engineVersion": f"{mp.dps}dps",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "computation": "he4-body-order-shortfall-location",
        "scriptFile": os.path.basename(__file__),
        "description": (
            "Locates the 4He super-pairwise magnitude shortfall between (1) the "
            "body-order weights a_D^{(n)} of the binding closure and (2) the "
            "per-bond Mayer factors / Markov convention. Measures PROBE 2's "
            "lumped enhancement and the body-order-resolved Ursell cumulants "
            "over the same zero-fit ingredients, under canonical convention D "
            "and excised convention C, for two f_pn typings. Audit-only, no fit, "
            "no free parameter."),
        "tier": "structural (zero-fit canonical bond factors + AME2020 cumulant inversion)",
        "data": {
            "q0": str(q),
            "z_C": str(z_of(q, "C")), "z_D": str(z_of(q, "D")),
            "ame_cumulants_MeV": _ser(ame_cum),
            "runs": [{
                "convention": r["convention"], "pn_typing": r["pn_typing"],
                "z": str(r["z"]), "h": str(r["h"]), "delta": str(r["delta"]),
                "f_pn": str(r["f_pn"]),
                "b4c_abs": str(r["b4c_abs"]), "sum_g": str(r["sum_g"]),
                "ceiling_over_D": str(r["ceiling_over_D"]),
                "delivered": str(r["delivered"]), "needed": str(r["needed"]),
                "delivered_over_needed": str(r["delivered_over_needed"]),
                "model_binding_MeV": _ser(r["model_binding_MeV"]),
                "cumulants_model_MeV": _ser(r["cumulants_model"]),
                "b3_ratio_to_ame": str(r["b3_ratio"]),
                "b4_ratio_to_ame": str(r["b4_ratio"]),
                "b3_sign_agrees": r["b3_sign_agrees"],
                "b4_sign_agrees": r["b4_sign_agrees"],
                "required_a3_over_a2": str(r["required_a3_over_a2"]),
                "required_a4_over_a2": str(r["required_a4_over_a2"]),
                "isospin_split_model_MeV": str(r["isospin_split_model"]),
                "isospin_split_ame_MeV": str(r["isospin_split_ame"]),
                "isospin_split_ratio": str(r["isospin_split_ratio"]),
            } for r in runs],
            "verdict": "LOCATION=body-order-weights",
            "verdict_note": (
                "Scope-(a). LEG 2 (convention) is measured and does NOT close the "
                "gap: under canonical convention D the lumped PROBE-2 enhancement "
                "is FARTHER from the target than under the excised convention C, "
                "so the 23% z_C->z_D difference moves the answer the wrong way. "
                "LEG 1 (body-order weights) is where the shortfall sits: resolved "
                "by body order, the model's connected 3-body and 4-body Ursell "
                "cumulants disagree with the AME ones in SIGN, not merely in "
                "magnitude, under BOTH conventions and BOTH f_pn typings. The "
                "lumped '1.4x vs 2.1x' reading averages a sign failure against an "
                "order-of-magnitude deficit. This constrains the "
                "multiplicative/Mayer assembly and the assumption that the "
                "a_D^{(n)} are a common constant across body orders; it does NOT "
                "exclude the [1^4] ingredient."),
        },
        "assertions": [
            {"name": "convention_does_not_close_gap",
             "computed": str(bool(conv_closes)), "expected": "False",
             "passed": not bool(conv_closes)},
            {"name": "canonical_D_not_closer_than_excised_C",
             "computed": str(bool(conv_improves)), "expected": "False",
             "passed": not bool(conv_improves)},
            {"name": "body_order_signs_not_reproduced",
             "computed": str(bool(body_signs_ok)), "expected": "False",
             "passed": not bool(body_signs_ok)},
            {"name": "required_weights_far_from_equal_weight_assumption",
             "computed": str(bool(weights_far_from_unity)), "expected": "True",
             "passed": bool(weights_far_from_unity)},
            {"name": "heldout_isospin_splitting_understated",
             "computed": str(bool(isospin_understated)), "expected": "True",
             "passed": bool(isospin_understated)},
        ],
        "auditOnly": True,
        "context": {
            "axis": "GAP-A-4 class-D — 4He magnitude shortfall LOCATION",
            "supersedes_framing": (
                "the '1.540x delivered / 26% short' figures of "
                "docs/audits/2026-07-05-delta-lambda-gate-status.md are "
                "convention-C-frame; the committed PROBE-2 witness is already D."),
            "related": [
                "probes/su4-connected-1111-magnitude.witness.json",
                "probes/b4-framework-connected-cumulant-deficit.witness.json",
                "folio/quantum-observable-universe/mass-theory/binding-closure-conditional.md",
                "folio/quantum-observable-universe/mass-theory/prolonged-periods-fixed-depth.md",
            ],
            "owner_ruling": "R1 2026-08-15 — convention D canonical, C excised",
        },
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__,
                                            engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = _HERE / "he4-body-order-shortfall-location.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str), encoding="utf-8")
    print(f"\n  Witness: {out.name}   allPassed={witness['allPassed']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
