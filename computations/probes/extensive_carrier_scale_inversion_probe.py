#!/usr/bin/env python3
"""Invert the alpha-cluster exclusion: WHAT ENERGY SCALE would close it?

`qou-n4zp` (probe `alpha_scale_is_outside_the_trace_probe.py`, PR #6443) reports
that the trace channel supplies `20.6-33.8 %` of one alpha, and `9.8-16.0 %` of
the bulk coefficient `a_V`. Both figures are **ratios of a computed trace against
an empirical MeV target**, and the trace side is `E_0 x L` — linear in an energy
scale that the framework does not derive.

Bean `qou-59j5` established exactly this hazard, against a different probe of
mine in the same lane:

> The Markov normaliser `Z(n) = (1+q_0^2)^n` is a **dimensionless** partition
> function. Turning `log Z` into MeV needs an energy, and **the framework does
> not derive one.** ... `E_0` is the corpus's, but it is CAL-1, a *calibration*,
> not a derivation. So neither side is pinned, and until one is, no `Nx` claim
> about the extensive term means anything.

`qou-n4zp` is an `Nx` claim about the extensive term. It inherits the defect.

This probe does not fix the defect — no scale is derived here. It converts the
bare ratio into a **falsifiable statement** by inverting it: the closure
requirement is a specific energy, and that energy can be compared against every
scale the corpus actually carries.

## The inversion

`B_trace = E x L`, so closing a target `T` requires exactly `E_req = T / L`. At
the complete graph (`L = 2.40868`, the largest the bond topology can produce):

    close one alpha   29.800 MeV  ->  E_req = 12.372 MeV  =  2.956 x E_0
    close the bulk    63.048 MeV  ->  E_req = 26.175 MeV  =  6.253 x E_0

## Against every energy scale in the corpus

    m_e                    0.511 MeV    0.122 x E_0     (my own earlier outlier)
    conv B = Q_beta        0.782 MeV    0.187 x E_0     (E_0_CONVENTIONS, hbar_q^0)
    E_0 = m_e/(q_0(q_0-1)) 4.186 MeV    1.000 x E_0     (CAL-1; conv A, hbar_q^1)
    hbar_q^2 * m_N         9.218 MeV    2.202 x E_0     (SaturationPeakStructure's unit)
    ---- required to close one alpha    2.956 x E_0 ----
    ---- required to close the bulk     6.253 x E_0 ----
    m_p / tr_M(proton)  1662.730 MeV  397.212 x E_0     (excised, bean qou-exam)

**The exclusion survives every live scale, and the margin is not large.** The
largest per-nucleon scale the corpus carries — `hbar_q^2 * m_N`, the unit
`QOU.Mass.SaturationPeakStructure` states `a_V` in — is `2.202 x E_0`, still
`1.34x` short of one alpha and `2.84x` short of the bulk. The only corpus scale
that would close it is `m_p / tr_M(proton)`, which overshoots by `134x` and
belongs to the absolute-mass chain excised on 2026-08-11.

## What this changes about `qou-n4zp`

**The direction of the finding is unchanged; its status is not.**

* `20.6-33.8 %` and `9.8-16.0 %` are **conditional on `E_0`** and are not
  scale-free measurements. Quote them with the scale named. At `hbar_q^2 * m_N`
  the same trace supplies **74.5 %** of one alpha and **35.2 %** of the bulk —
  so "two thirds to four fifths of every alpha is not in this channel" is an
  `E_0` statement, and at the corpus's other live scale it becomes "one quarter".
* The scale-free content is the requirement `E_req = T / L`, which holds for any
  `E`, and the comparison table above.
* Because a **larger** scale would close it, this is **scope (a)** — a
  scope-limited negative — and not scope (b). There is no proved invariant here
  bounding the energy scale from above. Do not write "the trace channel cannot
  carry the extensive term" without the qualifier "at any energy scale the
  corpus currently carries".

## Scope (a)

`L` is taken from this branch's measured values, `29.8 MeV/alpha` and the
`a_V` figure are cited empirical inputs, and `m_N` is CODATA. Nothing is fitted,
nothing is wired, and **no energy scale is derived here** — the open item
`qou-59j5` names stays open.
"""

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "habiro"),
           str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MUON_50_DIGIT_STR  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV, M_N_MEV_VALIDATION, M_P_MEV_VALIDATION,
)

set_compute_dps(40)

# measured on this branch (manybody_sign_by_bond_topology_probe)
L_CHAIN_A4 = "1.46969815276540455"
L_K4_BEST = "2.40867875195"
# corpus mean, docs/audits/2026-08-02-alpha-cluster-su4-extensive-term.md
ALPHA_SCALE_MEV = "29.8"
# QOU.Mass.SaturationPeakStructure's recorded empirical values, in hbar_q^2*m_N
A_V_OVER_HQ2_MN = "1.71"
M_N_MEV = "938.91875"
# computations/atom_mass_derived.py, E0_MEV = m_p / tr_M(proton).  Excised
# 2026-08-11 (bean qou-exam); carried here only as an upper comparison point.
EXCISED_ABS_MASS_SCALE_MEV = "1662.7295"
# derivation_chain.E_0_CONVENTIONS["B_q_value_absorbed"]: E_0 = Q_beta^CODATA,
# the hbar_q^0 rung of the registry (bean qou-59j5 §2). Computed in main() as
# m_n - m_p - m_e from the mpf CODATA constants — NOT from q_parameter's
# Q_NEUTRON_MEV, which is a Python float and would be f64-into-mpmath.


def main() -> int:
    checks, assertions = [], []

    def check(name, ok, detail):
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})
        checks.append(bool(ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {detail}")

    q = mp.mpf(Q_50_DIGIT_STR)
    m_e = mp.mpf(str(M_E_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    conv_B = (mp.mpf(str(M_N_MEV_VALIDATION)) - mp.mpf(str(M_P_MEV_VALIDATION))
              - m_e)   # Q_beta^CODATA = m_n - m_p - m_e, all mpf sources
    hbar_q = 1 - 1 / q
    m_N = mp.mpf(M_N_MEV)
    hq2_mN = hbar_q ** 2 * m_N

    # Copilot review on #6443: ENFORCE the proton-anchor assumption. The L values
    # were measured at the proton pin; the two pins differ at the 9th digit.
    check("q_0 is the PROTON pin (the pin the L values were measured at)",
          Q_50_DIGIT_STR != Q_MUON_50_DIGIT_STR
          and Q_50_DIGIT_STR.startswith("1.10997858"),
          f"Q_50_DIGIT_STR = {Q_50_DIGIT_STR[:20]}..., muon pin = "
          f"{Q_MUON_50_DIGIT_STR[:20]}...")

    L_chain = mp.mpf(L_CHAIN_A4)
    L_k4 = mp.mpf(L_K4_BEST)
    alpha_target = mp.mpf(ALPHA_SCALE_MEV)
    a_V = mp.mpf(A_V_OVER_HQ2_MN) * hq2_mN
    bulk4 = 4 * a_V

    print("=" * 78)
    print("  What energy scale would close the extensive term?")
    print("=" * 78)
    print(f"""
  q_0            = {mp.nstr(q, 20)}
  hbar_q         = 1 - 1/q_0        = {mp.nstr(hbar_q, 20)}
  E_0            = m_e/(q_0(q_0-1)) = {mp.nstr(E0, 20)} MeV
  hbar_q^2 * m_N                    = {mp.nstr(hq2_mN, 20)} MeV
  a_V = 1.71 * hbar_q^2 * m_N       = {mp.nstr(a_V, 20)} MeV/nucleon
""")

    # ------------------------------------------------- 1. the inversion
    print("-" * 78)
    print("  1. The inversion — B_trace = E x L, so E_req = T / L")
    print("-" * 78)
    E_req_alpha = alpha_target / L_k4
    E_req_bulk = bulk4 / L_k4
    E_req_alpha_chain = alpha_target / L_chain
    print(f"""
  target                        T (MeV)     L         E_req (MeV)   E_req/E_0
  one alpha, complete graph   {mp.nstr(alpha_target, 6):>9}  {mp.nstr(L_k4, 8)}  {mp.nstr(E_req_alpha, 8):>10}   {mp.nstr(E_req_alpha/E0, 6)}
  one alpha, chain            {mp.nstr(alpha_target, 6):>9}  {mp.nstr(L_chain, 8)}  {mp.nstr(E_req_alpha_chain, 8):>10}   {mp.nstr(E_req_alpha_chain/E0, 6)}
  bulk (4 x a_V), cplt graph  {mp.nstr(bulk4, 7):>9}  {mp.nstr(L_k4, 8)}  {mp.nstr(E_req_bulk, 8):>10}   {mp.nstr(E_req_bulk/E0, 6)}
""")
    check("closing one alpha needs an energy scale strictly above E_0",
          E_req_alpha > E0,
          f"E_req = {mp.nstr(E_req_alpha, 8)} MeV = "
          f"{mp.nstr(E_req_alpha/E0, 6)} x E_0. The requirement is a scale, not "
          f"a ratio — this statement is independent of which scale is chosen, "
          f"which the 20.6-33.8 % figures in qou-n4zp are not.")

    # ---------------------------------- 2. against every corpus scale
    print("\n" + "-" * 78)
    print("  2. Against every energy scale the corpus carries")
    print("-" * 78)
    scales = [
        ("m_e", m_e, "my own earlier outlier (qou-59j5); no reason was given"),
        ("conv B = Q_beta^CODATA", conv_B,
         "derivation_chain.E_0_CONVENTIONS['B_q_value_absorbed'], hbar_q^0"),
        ("E_0 = m_e/(q_0(q_0-1))", E0, "CAL-1 — a calibration, not a derivation; "
         "= E_0_CONVENTIONS['A_single_hecke_tick'], hbar_q^1"),
        ("hbar_q^2 * m_N", hq2_mN, "the unit SaturationPeakStructure states a_V in"),
        ("m_p / tr_M(proton)", mp.mpf(EXCISED_ABS_MASS_SCALE_MEV),
         "EXCISED 2026-08-11 (qou-exam) — absolute-mass chain"),
    ]
    print(f"\n  {'scale':<26}{'MeV':>12}{'x E_0':>12}   {'closes alpha?':<14}"
          f"{'closes bulk?':<13}")
    live_that_close_alpha, live_that_close_bulk = [], []
    rows = []
    for name, val, note in scales:
        excised = name.startswith("m_p /")
        ca = val >= E_req_alpha
        cb = val >= E_req_bulk
        if not excised:
            if ca:
                live_that_close_alpha.append(name)
            if cb:
                live_that_close_bulk.append(name)
        print(f"  {name:<26}{mp.nstr(val, 8):>12}{mp.nstr(val/E0, 6):>12}   "
              f"{('YES' if ca else 'no'):<14}{('YES' if cb else 'no'):<13}"
              f"{'  [excised]' if excised else ''}")
        rows.append({"scale": name, "mev": mp.nstr(val, 20),
                     "over_E0": mp.nstr(val / E0, 12),
                     "closes_alpha": bool(ca), "closes_bulk": bool(cb),
                     "excised": bool(excised), "note": note})
    print(f"\n  required, one alpha        {mp.nstr(E_req_alpha, 8):>12}"
          f"{mp.nstr(E_req_alpha/E0, 6):>12}")
    print(f"  required, bulk             {mp.nstr(E_req_bulk, 8):>12}"
          f"{mp.nstr(E_req_bulk/E0, 6):>12}\n")

    check("NO live corpus energy scale closes even one alpha",
          len(live_that_close_alpha) == 0,
          f"none of m_e, conv-B Q_beta, E_0, hbar_q^2*m_N reaches "
          f"{mp.nstr(E_req_alpha, 8)} MeV. The largest live scale is "
          f"hbar_q^2*m_N = {mp.nstr(hq2_mN, 8)} MeV, still "
          f"{mp.nstr(E_req_alpha/hq2_mN, 6)}x short of one alpha and "
          f"{mp.nstr(E_req_bulk/hq2_mN, 6)}x short of the bulk. The only scale "
          f"that would close it is the excised m_p/tr_M(proton), which "
          f"overshoots by {mp.nstr(mp.mpf(EXCISED_ABS_MASS_SCALE_MEV)/E_req_alpha, 6)}x.")

    # ------------------------------- 3. the scope correction to qou-n4zp
    print("\n" + "-" * 78)
    print("  3. The scope correction — (a), not (b)")
    print("-" * 78)
    # at hbar_q^2*m_N rather than E_0, the qou-n4zp percentages move by exactly
    # the scale ratio, since B_trace is linear in E.
    frac_hi_E0 = E0 * L_k4 / alpha_target
    frac_hi_hq2 = hq2_mN * L_k4 / alpha_target
    bulk_hi_E0 = E0 * L_k4 / bulk4
    bulk_hi_hq2 = hq2_mN * L_k4 / bulk4
    print(f"""
  qou-n4zp's headline figures are LINEAR in the scale:

    supplied fraction of one alpha   at E_0  {mp.nstr(100*frac_hi_E0, 4):>7} %
                                     at hq2  {mp.nstr(100*frac_hi_hq2, 4):>7} %
    supplied fraction of the bulk    at E_0  {mp.nstr(100*bulk_hi_E0, 4):>7} %
                                     at hq2  {mp.nstr(100*bulk_hi_hq2, 4):>7} %

  so the "20.6-33.8 %" and "9.8-16.0 %" are E_0 figures and must be quoted with
  the scale named. A LARGER scale closes the gap, so no proved invariant bounds
  this from above and the exclusion is scope (a), not scope (b).
""")
    ratio_check = mp.fabs(frac_hi_hq2 / frac_hi_E0 - hq2_mN / E0)
    check("the supplied fraction scales EXACTLY linearly with the energy "
          "(so the percentages are scale-conditional)",
          ratio_check < mp.mpf("1e-30"),
          f"|frac(hq2)/frac(E_0) - hq2/E_0| = {mp.nstr(ratio_check, 6)}. "
          f"B_trace = E x L has no other E-dependence, so every percentage in "
          f"qou-n4zp moves by the scale ratio {mp.nstr(hq2_mN/E0, 8)} and none "
          f"of them is a scale-free measurement.")

    check("the exclusion nonetheless SURVIVES the largest live scale",
          hq2_mN < E_req_alpha,
          f"at hbar_q^2*m_N the complete graph supplies "
          f"{mp.nstr(100*frac_hi_hq2, 4)} % of one alpha and "
          f"{mp.nstr(100*bulk_hi_hq2, 4)} % of the bulk — larger than the E_0 "
          f"figures by {mp.nstr(hq2_mN/E0, 6)}x, and still short. So the "
          f"DIRECTION of qou-n4zp is robust across the live scales even though "
          f"its NUMBERS are not scale-free.")

    # the count guard is deliberate: `all([])` is True, so a probe that fell
    # through every check would otherwise report success having verified nothing.
    ok = all(checks) and len(checks) == 5
    print("\n" + "=" * 78)
    print(f"  {sum(checks)}/{len(checks)} checks passed")
    print("=" * 78)

    witness = {
        "q0Anchor": "proton",
        "q0AnchorReason": (
            "Evaluates at the PROTON pin. q0 enters through "
            "q_parameter.Q_50_DIGIT_STR, which resolves to the proton "
            "anchor (1.1099785827513808075...) because this stem is not "
            "listed under ideal_muon; proton is the standing default for "
            "compute per the 2026-08-07 owner directive. A manifest entry "
            "would be inert here -- the manifest is read inside "
            "WitnessBuilder.build(), and this producer hand-rolls its "
            "witness and never enters build() -- so the declaration is "
            "made producer-side, the only route that reaches the file."),
        "$schema": "https://litlfred.github.io/qou/schemas/witness.schema.json",
        "name": "extensive-carrier-scale-inversion-probe",
        "description": (
            "Inverts the qou-n4zp alpha-cluster exclusion into an energy-scale "
            "requirement (E_req = T / L) and compares it against every energy "
            "scale the corpus carries. Records that qou-n4zp's percentages are "
            "conditional on E_0 and that the exclusion is scope (a), not (b)."
        ),
        "beans": ["qou-n4zp", "qou-59j5", "qou-brng"],
        "q0_anchor": "physical_proton",
        "inputs": {
            "q0": mp.nstr(q, 40),
            "conv_B_Qbeta_mev": mp.nstr(conv_B, 20),
            "L_chain_A4": L_CHAIN_A4,
            "L_complete_graph_A4": L_K4_BEST,
            "alpha_scale_mev": ALPHA_SCALE_MEV,
            "a_V_over_hbarq2_mN": A_V_OVER_HQ2_MN,
            "m_N_mev": M_N_MEV,
        },
        "results": {
            "E0_mev": mp.nstr(E0, 30),
            "hbarq2_mN_mev": mp.nstr(hq2_mN, 30),
            "a_V_mev": mp.nstr(a_V, 30),
            "E_req_one_alpha_mev": mp.nstr(E_req_alpha, 30),
            "E_req_one_alpha_over_E0": mp.nstr(E_req_alpha / E0, 20),
            "E_req_bulk_mev": mp.nstr(E_req_bulk, 30),
            "E_req_bulk_over_E0": mp.nstr(E_req_bulk / E0, 20),
            "scales": rows,
            "live_scales_closing_alpha": live_that_close_alpha,
            "live_scales_closing_bulk": live_that_close_bulk,
            "supplied_fraction_alpha_at_E0": mp.nstr(frac_hi_E0, 20),
            "supplied_fraction_alpha_at_hbarq2_mN": mp.nstr(frac_hi_hq2, 20),
            "supplied_fraction_bulk_at_E0": mp.nstr(bulk_hi_E0, 20),
            "supplied_fraction_bulk_at_hbarq2_mN": mp.nstr(bulk_hi_hq2, 20),
        },
        "verdict": (
            "SCOPE (a). Closing one alpha in the trace channel requires "
            "E >= 12.372 MeV = 2.956 x E_0; closing the bulk requires "
            "26.175 MeV = 6.253 x E_0. No live corpus energy scale reaches "
            "either — the largest, hbar_q^2*m_N = 9.218 MeV, is 1.34x short of "
            "one alpha and 2.84x short of the bulk. The exclusion therefore "
            "survives every scale the corpus carries, but a larger scale would "
            "close it, so this is a scope-limited negative and NOT a structural "
            "exclusion. qou-n4zp's 20.6-33.8 % and 9.8-16.0 % are E_0 figures "
            "and must be quoted with the scale named (bean qou-59j5). No "
            "energy scale is derived here; that item stays open."
        ),
        "assertions": assertions,
        "all_passed": bool(ok),
        "scope": "a",
    }
    out = _COMP / "extensive-carrier-scale-inversion-probe.witness.json"
    try:
        from witness import write_witness  # type: ignore
        write_witness(str(out), witness, script_path=__file__)
    except Exception:
        # Hand-rolled dump: build() never runs, so the manifest cannot stamp
        # this one. Ask for the anchor with the same precedence q_parameter
        # uses at compute time (env var > manifest stem > proton) rather than
        # hardcoding a pin this run may not have used.
        from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
        _q0a, _q0v = _rq0(__file__)
        witness["q0Anchor"] = _q0a
        if _q0v:
            witness["q0Value"] = _q0v
        out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  witness -> {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
