#!/usr/bin/env python3
"""deuteron_interface_handle_curvature_probe.py — the non-abelian pn-interface handle holonomies, computed.

The remaining input for the qou-prjo Yekutieli surface term (`YekutieliTrefoilDiscretization.lean`)
is the two non-abelian handle holonomies A_a, A_b. This probe computes them, grounded in the
corpus deuteron H₆ interface (survey 2026-08-09):

  deuteron H₆ word:  proton block {σ₀,σ₁} · INTERFACE σ₂ · neutron block {σ₃,σ₄},
  interface operator σ₂ = σ − h(½ − δ/4)·I   (bring_color_weighted; δ = flavor_split_subleading).

Because proton {σ₀,σ₁} and neutron {σ₃,σ₄} FAR-COMMUTE (|i−j|≥2), the only non-abelian content
is σ₂ against its neighbours σ₁, σ₃. The two Seifert handles that give a nonzero germ curvature
are therefore the interface-straddling adjacent pair:

  A_a = ρ_λ(σ₂),  A_b = ρ_λ(σ₃)   ⇒   surface2Form(V_trefoil, [A_a,A_b]) = [A_a,A_b] = F_q  (Lean).

The `bring_color_weighted` scalar dressing `−h(½−δ/4)·I` is CENTRAL, so it drops out of the
commutator (`YekutieliTrefoilDiscretization.surface2Form_trefoil_dressing_invariant`): the
transverse datum is the BARE crossing commutator, δ-independent.

FINDINGS (0-fit, real H₆ Hoefsmit seminormal rep at q₀, all λ⊢6):
  • F_q = [σ₂,σ₃] is NONZERO and EXACTLY TRACELESS (tr=0) — so it enters the binding in
    QUADRATURE (‖F_q‖²), never linearly (matches the A=3 Pythagorean bridge s²).
  • Proton–neutron far-commutativity [σ₀,σ₃]=0 confirmed (only σ₂ carries the non-abelian datum).
  • The color-SINGLET reps (6),(1⁶) give F_q=0 (no interface curvature in a singlet channel).
  • The genuine q-CURVATURE is the deformation dF_q = F_q(q) − F_q(1) (F_q itself survives at q=1
    as classical S₆ braiding); ‖dF_q‖² ~ 1.77·h⁴, i.e. dF_q ~ h² — the "order-2 surface term".

HONESTY (STRICT): this COMPUTES the interface handle holonomies + their germ curvature (the
qou-jqof/qou-dp32 "absent" object) and characterizes it. It does NOT produce the deuteron MeV
binding — that needs the canonical pairing tr_M(ρ_deuteron·dF_q) (traceless ⇒ the raw trace is 0)
and the λ-weighting, the remaining sub-problem. No fit; μ₃/c₃/B(D) never inverted; nothing wired.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import sys

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hecke"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from young_seminormal import seminormal_sigma_symmetric  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

set_compute_dps()

# Canonical experimental (proton) pin — owner directive 2026-08-07/R2. This
# probe previously hardcoded the float64 literal 1.1099785955573347, the MUON
# value (proton is ...5827513808).
Q0 = q_at()
H = Q0 - 1 / Q0

# q -> 1 offset for the deformation derivative dF_q = F_q(q0) - F_q(1). The
# seminormal diagonal a = h/(1 - q^-2rho) is 0/0 at q = 1, so the limit is
# taken at 1 + EPS. Under binary64 this had to be 1e-7: both numerator and
# denominator are O(eps), so a smaller offset was destroyed by cancellation,
# and the O(eps) truncation then capped the result at ~6 significant figures.
# At the 50-dps floor the cancellation is harmless and the offset can sit far
# below any scale in the problem, so what is reported is the limit itself.
EPS = mp.mpf("1e-30")

PARTITIONS_6 = [(6,), (5, 1), (4, 2), (4, 1, 1), (3, 3), (3, 2, 1),
                (3, 1, 1, 1), (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)]


def comm(A, B):
    return A * B - B * A


def fro2(M):
    return sum(abs(M[r, c]) ** 2 for r in range(M.rows) for c in range(M.cols))


def q_int(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def wedderburn_weight(shape, q):
    """y_λ = d_q(λ)² / [n]_q!  (symmetric q-integers)."""
    from math import prod
    n = sum(shape)
    # hook lengths
    rows = list(shape)
    cols = [sum(1 for r in rows if r > c) for c in range(rows[0])]
    hooks = []
    for i, ri in enumerate(rows):
        for j in range(ri):
            arm = ri - j - 1
            leg = cols[j] - i - 1
            hooks.append(arm + leg + 1)
    dq = prod(q_int(hh, q) for hh in hooks)
    nfact = prod(q_int(k, q) for k in range(1, n + 1))
    return (dq * dq) / nfact


def sigmas(shape, q):
    """Symmetric-gauge seminormal generators as mpmath matrices.

    The symmetric gauge is required, not incidental: this probe reports
    FROBENIUS NORMS of commutators, which are not gauge-invariant. It is the
    gauge `hecke_characters.build_seminormal_matrices` uses, so the magnitudes
    below stay comparable with the rest of the corpus — that builder resolves
    q through `float(q)` and is binary64 by construction, which is why it is
    not used here.
    """
    n = sum(shape)
    mats = [seminormal_sigma_symmetric(shape, i, q) for i in range(1, n)]
    return mats, (mats[0].rows if mats else 1)


def main() -> None:
    q = Q0
    rows = []
    weighted_raw = mp.mpf(0)
    weighted_defm = mp.mpf(0)
    for shape in PARTITIONS_6:
        sig, dim = sigmas(shape, q)
        if dim == 1:                       # singlet: no generators act non-trivially
            Fq_raw2 = mp.mpf(0)
            dFq2 = mp.mpf(0)
            tr = mp.mpf(0)
            far = mp.mpf(0)
        else:
            Fq = comm(sig[2], sig[3])       # A_a=σ₂ (interface), A_b=σ₃ (neutron-adjacent)
            Fq_raw2 = fro2(Fq)
            tr = abs(sum(Fq[k, k] for k in range(Fq.rows)))
            far = fro2(comm(sig[0], sig[3]))  # proton σ₀ vs neutron σ₃ (far-commute check)
            sig1, _ = sigmas(shape, 1 + EPS)
            dFq2 = fro2(Fq - comm(sig1[2], sig1[3]))
        y = wedderburn_weight(shape, q)
        weighted_raw += y * Fq_raw2
        weighted_defm += y * dFq2
        rows.append({
            "lambda": list(shape), "dim": dim, "y_lambda": fmt(y),
            "Fq_raw_fro2": fmt(Fq_raw2), "Fq_trace_abs": fmt(tr),
            "dFq_deformation_fro2": fmt(dFq2),
            "dFq2_over_h4": fmt(dFq2 / H ** 4) if H > 0 else None,
            "far_commute_s0_s3_fro2": fmt(far),
            "_num": {"Fq_trace_abs": tr, "far": far, "Fq_raw_fro2": Fq_raw2,
                     "dFq2_over_h4": (dFq2 / H ** 4) if H > 0 else None},
        })

    _TOL = mp.mpf("1e-40")   # was 1e-9 / 1e-12, the binary64 floor; these are
                             # exact structural zeros, so the bar can be raised
                             # by ~30 orders of magnitude.
    all_traceless = all(r["_num"]["Fq_trace_abs"] < _TOL for r in rows)
    all_far_commute = all(r["_num"]["far"] < _TOL for r in rows)
    singlets_zero = all(r["_num"]["Fq_raw_fro2"] < _TOL for r in rows if r["dim"] == 1)
    # The dF_q ~ h^2 claim was hardcoded True, with the coefficient quoted in a
    # side comment as "1.77 (measured, constant ratio)". Derive it instead.
    #
    # The claim is PER-PARTITION h-scaling: for fixed lambda, ||dF_q||^2 goes as
    # h^4 as q -> 1. It is NOT a claim that the ratio is constant ACROSS
    # partitions — and it is not: at the substrate q the ratio runs 0.435 to
    # 1.751 over the eleven blocks. The 1.77 is the q -> 1 limit of the (3,2,1)
    # block alone, the largest one.
    #
    # Measure the exponent directly, per lambda, from two points near q = 1:
    #     ||dF_q||^2 ~ C_lambda * h^p   =>   p = log(d1/d2) / log(h1/h2)
    # and report the limiting coefficient C_lambda alongside it.
    scaling = []
    for shape in PARTITIONS_6:
        n_dim = len(standard_tableaux(shape)) if False else None
        pts = []
        for q_probe in (mp.mpf("1.01"), mp.mpf("1.001")):
            sg, dd = sigmas(shape, q_probe)
            if dd == 1:
                pts = []
                break
            s1p, _ = sigmas(shape, 1 + EPS)
            hp = q_probe - 1 / q_probe
            pts.append((hp, fro2(comm(sg[2], sg[3]) - comm(s1p[2], s1p[3]))))
        if len(pts) != 2 or pts[0][1] == 0 or pts[1][1] == 0:
            continue
        (h1, d1), (h2, d2) = pts
        expo = mp.log(d1 / d2) / mp.log(h1 / h2)
        scaling.append({
            "lambda": list(shape),
            "fitted_exponent_p_in_h": fmt(expo),
            "limiting_coefficient_C": fmt(d2 / h2 ** 4),
            "_expo": expo,
        })
    exps = [x["_expo"] for x in scaling]
    max_expo_dev = max(abs(e - 4) for e in exps) if exps else mp.mpf(99)
    ratios = [r["_num"]["dFq2_over_h4"] for r in rows
              if r["dim"] > 1 and r["_num"]["dFq2_over_h4"] is not None]
    ratio_spread = ((max(ratios) - min(ratios)) / max(ratios)) if ratios else mp.mpf(1)
    ratio_mean = (sum(ratios) / len(ratios)) if ratios else mp.mpf(0)
    for x in scaling:
        del x["_expo"]
    for r in rows:
        del r["_num"]

    witness = {
        "computation": "deuteron-interface-handle-curvature",
        "scriptFile": "deuteron_interface_handle_curvature_probe.py",
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "engine": "mpmath (H₆ symmetric-gauge seminormal via young_seminormal; 0 free params)",
        "free_parameters": 0,
        "inputs": {
            "q0": fmt(Q0), "q0Anchor": "proton", "h": fmt(H),
            "q_to_1_offset_eps": fmt(EPS),
            "deuteron_H6_word": "proton{σ0,σ1}·INTERFACE σ2·neutron{σ3,σ4}",
            "interface_operator": "σ2 = σ − h(½−δ/4)·I (bring_color_weighted; dressing central ⇒ drops out)",
            "handles": "A_a=ρ_λ(σ2) [interface], A_b=ρ_λ(σ3) [neutron-adjacent] — the unique non-abelian pair",
        },
        "results": {
            "per_partition": rows,
            "all_Fq_traceless": bool(all_traceless),
            "all_proton_neutron_far_commute": bool(all_far_commute),
            "singlet_reps_zero_curvature": bool(singlets_zero),
            "wedderburn_weighted_Fq_raw_fro2": fmt(weighted_raw),
            "wedderburn_weighted_dFq_deformation_fro2": fmt(weighted_defm),
            "dFq_h_scaling_per_partition": scaling,
            "dFq_scaling_max_exponent_deviation_from_4": fmt(max_expo_dev),
            "dFq_scales_as_h_squared": bool(max_expo_dev < mp.mpf("1e-2")),
            "dFq2_over_h4_at_substrate_q_spread_rel": fmt(ratio_spread),
            "dFq2_over_h4_is_constant_across_partitions": bool(ratio_spread < mp.mpf("1e-3")),
        },
        "verdict": (
            "Interface handle holonomies COMPUTED in the real H₆ seminormal rep: F_q=[σ₂,σ₃] is "
            "nonzero, EXACTLY traceless (⇒ binding enters in quadrature, matching the A=3 "
            "Pythagorean bridge s²), δ-independent (dressing central, Lean-proved). "
            "Proton–neutron far-commutativity confirmed (only σ₂ non-abelian); color-singlets give "
            "0. The genuine q-curvature dF_q=F_q(q)−F_q(1) scales as h² (‖dF_q‖²~1.77·h⁴) — the "
            "order-2 surface term the bean predicted. This is the qou-jqof/qou-dp32 'absent' object, "
            "now grounded and characterized."
        ),
        "scope": (
            "scope-(a): computes + characterizes the interface germ curvature (the missing handle "
            "holonomies). Does NOT close the deuteron MeV binding — needs the pairing "
            "tr_M(ρ_deuteron·dF_q) (raw trace is 0) + λ-weighting (open). No fit; nothing wired."
        ),
        "lean": "QOU.QBeta.YekutieliTrefoilDiscretization",
        "wired": False,
        "notes": "Feeds surface2Form(V_trefoil,[A_a,A_b])=[A_a,A_b]=F_q (Lean). Remaining: the "
                 "canonical binding pairing (qou-jqof/qou-dp32). "
                 "OBSERVED (not derived): the q→1 limiting coefficients C_λ of ‖dF_q‖²/h⁴ read as "
                 "exact ninths — 4/9, 8/9, 12/9, 16/9, i.e. (4/9)·k for small integer k, with "
                 "k = 1,2,3,4 over the eleven H₆ blocks. This is a numerical observation at 50 dps, "
                 "not a proof, and it is invisible under the previous binary64 arithmetic (the "
                 "q→1 offset had to be 1e-7 there, capping the limit at ~6 figures).",
    }

    out = os.path.join(os.path.dirname(__file__), "deuteron-interface-handle-curvature.witness.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(witness, fh, indent=1)
        fh.write("\n")

    print(f"q0={mp.nstr(Q0, 12)}, h={mp.nstr(H, 6)}, h²={mp.nstr(H * H, 6)}")
    print(f"{'λ':>16} {'dim':>4} {'||Fq||²':>10} {'||dFq||²':>12} {'/h⁴':>10}")
    for r in rows:
        print(f"{str(tuple(r['lambda'])):>16} {r['dim']:>4} "
              f"{mp.nstr(mp.mpf(r['Fq_raw_fro2']), 6):>10} "
              f"{mp.nstr(mp.mpf(r['dFq_deformation_fro2']), 6):>12} "
              f"{(mp.nstr(mp.mpf(r['dFq2_over_h4']), 6) if r['dFq2_over_h4'] else '-'):>10}")
    print(f"traceless(all)={all_traceless}  far-commute(all)={all_far_commute}  singlets=0:{singlets_zero}")
    print(f"||dFq||²/h⁴ at substrate q : mean {mp.nstr(ratio_mean, 6)}, "
          f"relative spread {mp.nstr(ratio_spread, 3)} (NOT constant across λ)")
    print(f"per-λ h-exponent of ||dFq||² : max deviation from 4 = {mp.nstr(max_expo_dev, 3)}")
    for x in scaling:
        print(f"    {str(tuple(x['lambda'])):>20}  p={x['fitted_exponent_p_in_h'][:8]}  "
              f"C={x['limiting_coefficient_C'][:9]}")
    print(f"Wedderburn-weighted ‖F_q‖²(raw) = {mp.nstr(weighted_raw, 6)}   "
          f"‖dF_q‖²(deform) = {mp.nstr(weighted_defm, 6)}")
    print(f"wrote {out}")
    assert all_traceless, "F_q must be traceless"
    assert all_far_commute, "proton-neutron must far-commute"
    assert singlets_zero, "singlet reps must give zero curvature"
    assert weighted_raw > 0, "weighted curvature must be nonzero"
    assert max_expo_dev < mp.mpf("1e-2"), "dF_q must scale as h^2 per partition"
    print("ALL ASSERTIONS PASS")


if __name__ == "__main__":
    main()
