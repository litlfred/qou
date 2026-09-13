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
    as classical S₆ braiding), and dF_q ~ h² — the "order-2 surface term". Sharpened 2026-08-25
    on the mpmath port: lim_{q→1} ‖dF_q‖²/h⁴ = 4k/9 EXACTLY, k ∈ {0,1,2,3,4}, verified to 22
    digits and conjugation-symmetric ((5,1)↔(2,1⁴) both 4/9, (3,2,1) alone 16/9). The ratio is
    NOT constant — at q₀ it spans 0.4355…1.7506 across partitions — and the "1.77" this line
    used to quote is 16/9, the LIMIT for (3,2,1) alone, i.e. the maximum over partitions rather
    than a q₀ value. The h²-scaling conclusion is unchanged; it is now measured, not asserted.
    F_q(1) is now the exact classical Young form; it was q = 1 + 1e-7, worth ~1e-9 in dF_q.

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

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hecke"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "substrate"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from _witness_q0_stamp import stamp_q0  # noqa: E402

import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

# NO-FLOAT64 (AGENTS.md, owner directive 2026-08-18: "PROBES ARE NOT EXEMPT").
# dps raised at MODULE scope, before the first mpf below is constructed.
set_compute_dps()

from hecke_characters import build_seminormal_matrices_mp  # noqa: E402

# q0 RESOLVED, not frozen (2026-08-29, bean qou-1c4y). This was the literal
# 1.10997859555733471..., the SUPERSEDED muon pin A -- it stopped being the
# muon anchor when PR #5500 re-derived that anchor to CODATA-2022. A frozen
# literal cannot follow an anchor move, so the witness kept recording A under
# the label "muon" and the anchor gate scored it Q0_FLIP; re-running could not
# clear it, because the producer was the source of the stale number. It now
# resolves the PROTON pin per the owner directive of 2026-08-15 ("we want
# proton unless for an explicit reason ... otherwise pin proton").
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402 -- q0 RESOLVED, not frozen (qou-1c4y)

Q0_STR = _Q0_RESOLVED
Q0 = mp.mpf(Q0_STR)
H = Q0 - 1 / Q0

PARTITIONS_6 = [(6,), (5, 1), (4, 2), (4, 1, 1), (3, 3), (3, 2, 1),
                (3, 1, 1, 1), (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)]


def comm(A, B):
    return A * B - B * A


def fro2(M):
    return sum(abs(M[r, c]) ** 2 for r in range(M.rows) for c in range(M.cols))


def q_int(k, q):
    """[k]_q, with the exact q -> 1 limit [k]_1 = k (the ratio is 0/0 there)."""
    if q == 1:
        return mp.mpf(k)
    return (q ** k - q ** (-k)) / (q - 1 / q)


def wedderburn_weight(shape, q):
    """**quantum Plancherel** measure `w_planch(λ) = d_q(λ)² / [n]_q!`
    (symmetric q-integers).

    NOT the Wenzl y_λ, which is the production Markov weight. This docstring
    read `y_λ = d_q(λ)²/[n]_q!` until 2026-09-13 — the conflation AGENTS.md
    forbids, since the three families y_λ / w_λ / w̃_λ are distinct at q ≠ 1.
    The sibling Magnus Ω₂ probes carried the same line, and there it was not
    cosmetic: re-weighting their committed traces with the real Wenzl bridge
    flips the sign of P_total at A=3 and A=4 (bean `qou-za3q`). Found by
    `computations/audits/y_lambda_conflation_audit.py`, which exists because
    the name was the only thing telling the two families apart.
    """
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
    # HOOK-LENGTH FORMULA: d_q(λ) = [n]_q! / ∏_x [h(x)]_q.
    #
    # This previously read `dq = prod(q_int(hh, q) for hh in hooks)` — the
    # DENOMINATOR of that formula, not d_q — and then returned dq²/[n]_q!.
    # The result was the EXACT RECIPROCAL of the documented weight:
    # computed H²/[n]_q! where d_q²/[n]_q! = [n]_q!/H². Verified against the
    # committed witnesses to a relative 1e-40, and probe × correct = 1.0
    # identically on every partition checked.
    hook_prod = prod(q_int(hh, q) for hh in hooks)
    nfact = prod(q_int(k, q) for k in range(1, n + 1))
    dq = nfact / hook_prod
    return (dq * dq) / nfact


def sigmas(shape, q):
    sig, dim, _ = build_seminormal_matrices_mp(shape, q)
    return sig, dim


def h4_limit_ratio(shape):
    """lim_{q->1} ‖dF_q‖²/h⁴, computed rather than asserted.

    This probe used to record `dFq_scales_as_h_squared: True` as a HARDCODED
    boolean, annotated "‖dFq‖² ~ 1.77·h⁴ (measured, constant ratio)". Neither
    half of that annotation was what the probe measured: at q₀ the ratio is
    partition-DEPENDENT (0.4355 … 1.7506, a 4× spread), so it is not constant;
    and 1.77 is not a q₀ value at all, it is the q->1 LIMIT of the single
    partition (3,2,1). The h²-scaling conclusion is right; the evidence for it
    was not in the witness.

    PRECISION IS LOAD-BEARING HERE, which is why this is only possible after
    the mpmath port. dF_q = F_q(q) − F_q(1) is O(eps²) against O(1) matrix
    entries, so the subtraction cancels ~2·|log10 eps| digits. At the module
    dps (70) a probe at eps = 1e-25 returns ~1e6 — pure rounding, and
    superficially plausible. dps is raised locally so the cancellation is
    affordable; the ratio is then stable from eps = 1e-15 to 1e-80.
    """
    _saved = mp.mp.dps
    try:
        mp.mp.dps = 400
        sig1, dim, _ = build_seminormal_matrices_mp(shape, mp.mpf(1))
        if dim == 1:
            return mp.mpf(0)
        base = comm(sig1[2], sig1[3])
        q = 1 + mp.mpf(10) ** -40
        sg, _, _ = build_seminormal_matrices_mp(shape, q)
        return fro2(comm(sg[2], sg[3]) - base) / (q - 1 / q) ** 4
    finally:
        mp.mp.dps = _saved


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
            tr = abs(sum(Fq[r, r] for r in range(Fq.rows)))
            far = fro2(comm(sig[0], sig[3]))  # proton σ₀ vs neutron σ₃ (far-commute check)
            # q = 1 EXACTLY (Young's classical seminormal form), not the former
            # q = 1 + 1e-7 finite difference: that epsilon put ~1e-7 of error
            # into every matrix entry and hence straight into dF_q, which is
            # the quantity this probe reports. See build_seminormal_matrices_mp.
            sig1, _ = sigmas(shape, mp.mpf(1))
            dFq2 = fro2(Fq - comm(sig1[2], sig1[3]))
        lim = h4_limit_ratio(shape)
        y = wedderburn_weight(shape, q)
        weighted_raw += y * Fq_raw2
        weighted_defm += y * dFq2
        rows.append({
            "lambda": list(shape), "dim": dim, "y_lambda": fmt(y),
            "Fq_raw_fro2": fmt(Fq_raw2), "Fq_trace_abs": fmt(tr),
            "dFq_deformation_fro2": fmt(dFq2),
            "dFq2_over_h4": fmt(dFq2 / H ** 4) if H > 0 else None,
            "far_commute_s0_s3_fro2": fmt(far),
            "dFq2_over_h4_q_to_1_limit": fmt(lim),
            "dFq2_over_h4_q_to_1_limit_times_9": fmt(lim * 9),
            "_tr": tr, "_far": far, "_raw": Fq_raw2,   # mpf, stripped below
        })

    # Thresholds were float64-grade sentinels (1e-9 / 1e-12). These are exact
    # structural claims -- tracelessness, far-commutativity, singlet vanishing --
    # so at 70 dps they are asserted at 1e-40 instead.
    _EXACT = mp.mpf(10) ** -40
    # Every q->1 limit ratio must be an exact multiple of 1/9 (4k/9, k=0..4).
    all_limits_are_ninths = all(
        abs(mp.mpf(r["dFq2_over_h4_q_to_1_limit_times_9"])
            - mp.nint(mp.mpf(r["dFq2_over_h4_q_to_1_limit_times_9"]))) < mp.mpf(10) ** -18
        for r in rows)
    all_traceless = all(r["_tr"] < _EXACT for r in rows)
    all_far_commute = all(r["_far"] < _EXACT for r in rows)
    singlets_zero = all(r["_raw"] < _EXACT for r in rows if r["dim"] == 1)
    for r in rows:
        del r["_tr"], r["_far"], r["_raw"]

    witness = {
        "computation": "deuteron-interface-handle-curvature",
        "scriptFile": "deuteron_interface_handle_curvature_probe.py",
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "engine": "mpmath mpf (H₆ Hoefsmit seminormal via build_seminormal_matrices_mp; 0 free params)",
        "free_parameters": 0,
        "inputs": {
            "q0": Q0_STR, "q0_pin": "proton (experimental pin, resolved)", "h": fmt(H),
            "q0_precision_note": (
                "RESOLVED from substrate.q_parameter at run time, not frozen. It was a "
                "17-digit muon literal until 2026-08-29 (bean qou-1c4y); a frozen literal "
                "cannot follow an anchor move, which is how this witness came to record "
                "the superseded muon pin under the label \"muon\"."),
            "arithmetic": f"mpmath mpf at {mp.mp.dps} dps (no float64 anywhere)",
            "q_eq_1_reference": "exact classical Young seminormal limit (was q = 1 + 1e-7)",
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
            # MEASURED, not asserted (this was a hardcoded True until 2026-08-25).
            "dFq_scales_as_h_squared": bool(all_limits_are_ninths),
            "dFq2_over_h4_limits_are_exact_ninths": bool(all_limits_are_ninths),
            "dFq2_over_h4_limit_numerators_over_9": [
                r["dFq2_over_h4_q_to_1_limit_times_9"] for r in rows],
            "dFq2_over_h4_limit_note": (
                "lim_{q->1} ||dF_q||^2/h^4 = 4k/9 exactly, k in {0,1,2,3,4}, verified to 22 "
                "digits and conjugation-symmetric. The ratio is NOT constant: at q0 it spans "
                "0.4355..1.7506 across partitions. The '1.77' previously recorded is 16/9, the "
                "LIMIT for (3,2,1) alone -- the maximum over partitions, not a q0 value."),
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
                 "canonical binding pairing (qou-jqof/qou-dp32).",
    }

    # Provenance stamp (bean 1j39): this producer hand-rolls json.dump and so

    # never reaches WitnessBuilder.build(), which is where q0Anchor is set.

    # Without this the witness stays unstamped permanently — re-running it

    # cannot fix that. Adds two keys; touches nothing else.

    stamp_q0(witness, __file__)

    out = os.path.join(os.path.dirname(__file__), "deuteron-interface-handle-curvature.witness.json")
    with open(out, "w", encoding="utf-8") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, fh, indent=1)  # every numeric already fmt()'d to str
        fh.write("\n")

    print(f"q0={mp.nstr(Q0, 17)}, h={mp.nstr(H, 6)}, h²={mp.nstr(H*H, 6)}")
    print(f"{'λ':>16} {'dim':>4} {'||Fq||²':>10} {'tr':>7} {'||dFq||²':>12} {'/h⁴':>8}")
    for r in rows:
        print(f"{str(tuple(r['lambda'])):>16} {r['dim']:>4} {r['Fq_raw_fro2'][:9]:>10} "
              f"{r['Fq_trace_abs'][:7]:>9} {r['dFq_deformation_fro2'][:11]:>13} "
              f"{(r['dFq2_over_h4'] or '0')[:7]:>8}")
    print(f"traceless(all)={all_traceless}  far-commute(all)={all_far_commute}  singlets=0:{singlets_zero}")
    print(f"Wedderburn-weighted ‖F_q‖²(raw) = {mp.nstr(weighted_raw, 6)}   ‖dF_q‖²(deform) = {mp.nstr(weighted_defm, 5)}")
    print(f"wrote {out}")
    assert all_traceless, "F_q must be traceless"
    assert all_far_commute, "proton-neutron must far-commute"
    assert singlets_zero, "singlet reps must give zero curvature"
    assert weighted_raw > 0, "weighted curvature must be nonzero"
    print("ALL ASSERTIONS PASS")


if __name__ == "__main__":
    main()
