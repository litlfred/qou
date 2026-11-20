#!/usr/bin/env python3
"""deuteron_two_body_kernel_overshoot_probe.py — where the +27 % deuteron overshoot lives.

The production two-body binding form (`mass_binding_dashboard._bond_type_L`) gives

    B_sym(2H) = E_0 * L_pn,
    E_0       = m_e / (q_0 (q_0 - 1)),
    L_pn      = -ln(z_D - h*t) - (t - 1/2)*ln(1 - h),
    z_D       = q_0^3/(q_0^2 + 1)          [convention D, owner ruling R1 2026-08-15]
    h         = q_0 - 1/q_0
    t         = 1/2 - delta/4              [bring_color_weighted, owner ruling R3]
    delta     = (q_0-1)^2 (1 - q_0^-4)/3   [prop:flavor-split-substrate]

against B_AME(2H) = 2.2245662 MeV: an overshoot of +27.34 %.  2H is the ONLY
negative residual in the low-isotope table (R = -0.61; every other isotope has
R > 0), which is what makes it logically prior to the additive-term programme —
a correction non-negative for all A cannot repair 4He (which UNDER-binds) and
2H (which OVER-binds) at once.

WHAT THIS PROBE ESTABLISHES

1. FREE-PARAMETER INVENTORY.  Every ingredient of B_sym(2H) is enumerated with
   the artifact that fixes it.  The count of continuous free parameters is 0:
   m_e is CAL-1, q_0 is the CAL-2 proxy pin, E_0's FORM is derived
   (`observations/mass-formula-validation.md`), z_D and the p/n colour weighting
   are owner-ruled conventions (discrete, and neither chosen against 2H), the
   interface coefficient a = 1 is forced by convexity of the colour
   superposition, and the writhe factor is Lean-proved unique up to sign.
   => the +27 % is a PARAMETER-FREE PREDICTION FAILURE, not a tuning gap.

2. WHERE THE MISS LIVES.  Each ingredient is moved, alone, to the value that
   would reproduce B_AME(2H), and the required displacement is reported against
   the displacement that ingredient is actually ALLOWED.  Only the colour weight
   t can reach the target at all, and it must travel 673x its own derived scale.

3. THE CAL-2 SCOPE QUESTION.  E_0 enters linearly, so a fix through E_0 needs a
   -21.5 % move; the entire proton-vs-muon pin spread is 128 ppb.  The ratio is
   the exact factor by which a CAL-2-respecting fix is unavailable.

4. LEAN AGREEMENT.  Every rational bound used by
   `QOU.MassTheory.DeuteronTwoBodyKernel` (sorry-free) is re-checked here against
   the mpf values, so the formal statement and the compute cannot drift apart
   silently.

HONESTY / SCOPE.  scope-(a), scope-limited negative: the two-body Markov-trace
kernel with the convention-D Markov parameter and the derived colour weighting
does not reproduce B_AME(2H); it over-binds by +27 %, and no interface weight
within 250x the derived flavour split closes the gap.  It is NOT scope-(b): the
target IS inside the convention-D admissible band (reached at t ~ 0.268), so no
invariant excludes it, and an ADDITIVE term is untouched by anything here.
Under the excised convention C the band was [2.907, 5.178] MeV and 2.2246 sat
below all of it; that older impossibility claim does not survive the D ruling
and must not be carried forward.

NO FLOAT64 anywhere: mpmath mpf end to end at 60 dps, serialized via
`_precision.fmt`.  Nothing is wired; no witness value is inverted from AME.

Output: deuteron-two-body-kernel-overshoot.witness.json
"""
from __future__ import annotations

import json
import os
import sys as _sys
import time
from pathlib import Path as _Path

_COMP = _Path(__file__).resolve().parent
for _d in ("substrate",):
    _p = str(_COMP / _d)
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
_sys.path.insert(0, str(_COMP))

from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps(60)

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402  (AME registry)

# AME2020 deuteron binding, MeV.  COMPARISON TARGET ONLY — never inverted.
B_AME_2H = AME_B_DEUTERON_MEV_VALIDATION


# ---------------------------------------------------------------- the kernel

def z_D(q):
    """Convention-D Markov parameter z = q^3/(q^2+1) (owner ruling R1)."""
    return q ** 3 / (q ** 2 + 1)


def h_q(q):
    """Hecke skein parameter h = q - 1/q."""
    return q - 1 / q


def interface_factor(q, t):
    """f(q,t) = z_D - h*t.

    t is the sigma^-1 branch weight of the colour superposition
    (1-t)*sigma + t*sigma^-1; by the Hecke skein relation sigma^-1 = sigma - h*1
    that superposition is sigma - h*t*1, so the interface coefficient a is
    identically 1 — forced by convexity, not chosen.
    """
    return z_D(q) - h_q(q) * t


def bond_L(q, t):
    """Writhe-normalised per-bond log suppression."""
    return -mp.log(interface_factor(q, t)) - (t - mp.mpf(1) / 2) * mp.log(1 - h_q(q))


def E_0(me, q):
    """CAL-1 x CAL-2 energy unit E_0 = m_e/(q(q-1))."""
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    return _qbeta_e0.order_zero_scaled(me, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)


def t_derived(q):
    """bring_color_weighted colour weight t = 1/2 - delta/4."""
    return mp.mpf(1) / 2 - flavor_split_leading(q) / 4


def B_sym_2H(me, q, t):
    return E_0(me, q) * bond_L(q, t)


# ------------------------------------------------------- inventory + analysis

def free_parameter_inventory():
    """Every ingredient of B_sym(2H), with the artifact that fixes it.

    `freedom` is the continuous tuning freedom the framework grants the
    ingredient.  The sum over the table is the free-parameter count.
    """
    return [
        {"ingredient": "m_e", "role": "sets the MeV unit",
         "fixed_by": "CAL-1 (CODATA electron mass)", "kind": "calibration input",
         "continuous_freedom": 0},
        {"ingredient": "q_0", "role": "substrate modulus",
         "fixed_by": "CAL-2 via the proton mass-ratio pin (0.017 ppb)",
         "kind": "calibration input", "continuous_freedom": 0},
        {"ingredient": "E_0 = m_e/(q_0(q_0-1))", "role": "energy scale of the bond",
         "fixed_by": "derived form, observations/mass-formula-validation.md",
         "kind": "derived", "continuous_freedom": 0},
        {"ingredient": "z_D = q^3/(q^2+1)", "role": "Markov parameter",
         "fixed_by": "owner ruling R1 2026-08-15 (convention D canonical)",
         "kind": "discrete convention", "continuous_freedom": 0},
        {"ingredient": "a = 1", "role": "interface coefficient in a*sigma + b*1",
         "fixed_by": "convexity of the colour superposition (a = (1-t)+t = 1)",
         "kind": "forced", "continuous_freedom": 0},
        {"ingredient": "t = 1/2 - delta/4", "role": "p-n colour weight",
         "fixed_by": "owner ruling R3 + prop:flavor-split-substrate",
         "kind": "derived", "continuous_freedom": 0},
        {"ingredient": "(1-h)^(delta_e/2)", "role": "writhe normalisation",
         "fixed_by": "QOU.QBeta.WritheNormalisation (sorry-free, unique up to sign)",
         "kind": "proved", "continuous_freedom": 0},
        {"ingredient": "one p-n bond", "role": "chain topology at A=2",
         "fixed_by": "A=2 has exactly one nucleon pair",
         "kind": "forced", "continuous_freedom": 0},
    ]


def locate_the_miss(me, q):
    """Move each ingredient ALONE to the value reproducing B_AME(2H).

    Reports the required displacement against the displacement the framework
    actually allows for that ingredient.  A ratio >> 1 means the ingredient
    cannot carry the miss.
    """
    t0 = t_derived(q)
    rows = []

    # (1) the colour weight t — the only interface degree of freedom
    t_star = mp.findroot(lambda x: B_sym_2H(me, q, x) - B_AME_2H, mp.mpf("0.27"))
    delta_over_4 = flavor_split_leading(q) / 4
    rows.append({
        "ingredient": "colour weight t",
        "derived_value": fmt(t0),
        "required_value": fmt(t_star),
        "required_displacement": fmt(t0 - t_star),
        "allowed_scale": fmt(delta_over_4),
        "allowed_scale_meaning": "the entire derived flavour split delta/4",
        "displacement_over_allowed": fmt((t0 - t_star) / delta_over_4),
        "reachable": True,
    })

    # (2) the energy scale E_0 — enters linearly
    e0 = E_0(me, q)
    e0_star = B_AME_2H / bond_L(q, t0)
    rows.append({
        "ingredient": "energy scale E_0",
        "derived_value": fmt(e0),
        "required_value": fmt(e0_star),
        "required_rel_move": fmt((e0_star - e0) / e0),
        "allowed_rel_move": None,          # filled by the caller (pin spread)
        "reachable": True,
    })

    # (3) the Markov parameter z — convention
    z0 = z_D(q)
    # solve -ln(z - h t0) - (t0-1/2) ln(1-h) = B_AME/E_0  for z
    target_L = B_AME_2H / e0
    hh = h_q(q)
    z_star = mp.exp(-(target_L + (t0 - mp.mpf(1) / 2) * mp.log(1 - hh))) + hh * t0
    z_C = mp.sqrt(q) / (q + 1)
    rows.append({
        "ingredient": "Markov parameter z",
        "derived_value": fmt(z0),
        "required_value": fmt(z_star),
        "required_rel_move": fmt((z_star - z0) / z0),
        "convention_C_value": fmt(z_C),
        "note": ("convention C is FARTHER from the required z than D is; the "
                 "R1 ruling moved z toward the deuteron and away from A >= 3, "
                 "which is why it cannot be read as a fit to 2H"),
        "reachable": True,
    })

    # (4) the writhe normalisation — measure its whole contribution
    L_with = bond_L(q, t0)
    L_without = -mp.log(interface_factor(q, t0))
    rows.append({
        "ingredient": "writhe normalisation",
        "whole_contribution_MeV": fmt(e0 * (L_with - L_without)),
        "miss_MeV": fmt(e0 * L_with - B_AME_2H),
        "fraction_of_miss": fmt((L_with - L_without) / (L_with - B_AME_2H / e0)),
        "reachable": False,
        "note": "the entire writhe term is ~5.7e-4 of the miss; it cannot carry it",
    })

    # (5) the substrate modulus q itself, if the pin were abandoned
    try:
        q_star = mp.findroot(lambda x: B_sym_2H(me, x, t_derived(x)) - B_AME_2H,
                             q * mp.mpf("0.9"))
        rows.append({
            "ingredient": "substrate modulus q_0 (pin abandoned)",
            "derived_value": fmt(q),
            "required_value": fmt(q_star),
            "required_rel_move": fmt((q_star - q) / q),
            "allowed_rel_move": "1.7e-11 (proton pin, 0.017 ppb)",
            "reachable": True,
            "note": "listed for completeness; moving q_0 breaks CAL-2 and every "
                    "other observable at once",
        })
    except Exception as exc:                      # pragma: no cover
        rows.append({"ingredient": "substrate modulus q_0",
                     "error": f"root-find failed: {exc}"})
    return rows


def admissible_band(me, q):
    """The full interface family t in [0,1]: p-p (t=0) through n-n (t=1)."""
    e0 = E_0(me, q)
    lo = e0 * bond_L(q, mp.mpf(0))
    hi = e0 * bond_L(q, mp.mpf(1))
    return {
        "t_0_pp_MeV": fmt(lo),
        "t_1_nn_MeV": fmt(hi),
        "B_AME_2H_MeV": fmt(B_AME_2H),
        "target_inside_band": bool(lo < B_AME_2H < hi),
        "note": ("the band is WRITHE-CONSISTENT: delta_e = 2t-1 is varied with t. "
                 "The [2.0507, 3.7978] band quoted in the 2026-08-25 low-isotope "
                 "audit is the NO-WRITHE band, and its 't = 0.119453' requirement "
                 "is the no-writhe root; both are superseded here."),
    }


def lean_bound_crosscheck(me, q):
    """Re-check every rational bound `QOU.MassTheory.DeuteronTwoBodyKernel` uses."""
    z, hh, e0 = z_D(q), h_q(q), E_0(me, q)
    checks = [
        ("q_lo <= q_0", mp.mpf("1.1099785") <= q),
        ("q_0 <= q_hi", q <= mp.mpf("1.1099786")),
        ("0.6126879 <= z_D", mp.mpf("0.6126879") <= z),
        ("z_D <= 0.6126881", z <= mp.mpf("0.6126881")),
        ("0.2090601 <= h", mp.mpf("0.2090601") <= hh),
        ("h <= 0.2090604", hh <= mp.mpf("0.2090604")),
        ("4.185980 <= E_0", mp.mpf("4.185980") <= e0),
        ("0.499 <= t_derived", mp.mpf("0.499") <= t_derived(q)),
        ("t_derived <= 1/2", t_derived(q) <= mp.mpf(1) / 2),
        ("0.4996 <= t_derived", mp.mpf("0.4996") <= t_derived(q)),
        ("delta <= 0.001377", flavor_split_leading(q) <= mp.mpf("0.001377")),
        ("q^4 <= 1.5180", q ** 4 <= mp.mpf("1.5180")),
        # the exact bar-symmetric identity the Lean proves by field_simp; ring
        ("z_D - h/2 == (q^4+1)/(2q(q^2+1))",
         abs((z - hh / 2) - (q ** 4 + 1) / (2 * q * (q ** 2 + 1))) < mp.mpf("1e-55")),
        # the headline inequality, at the derived weight
        ("1.25 * B_AME < B_sym(2H)",
         mp.mpf("1.25") * B_AME_2H < B_sym_2H(me, q, t_derived(q))),
        # the required-weight bound
        ("B_sym(q, 0.4) > 2.4", B_sym_2H(me, q, mp.mpf("0.4")) > mp.mpf("2.4")),
    ]
    return [{"claim": c, "holds": bool(v)} for c, v in checks]


def main():
    t_start = time.time()
    q = mp.mpf(Q_50_DIGIT_STR)
    me = mp.mpf(str(M_E_MEV))

    t0 = t_derived(q)
    b_sym = B_sym_2H(me, q, t0)
    overshoot_pct = 100 * (b_sym / B_AME_2H - 1)

    # bar-symmetric (delta = 0) reference: the writhe factor is EXACTLY 1 there
    b_bar = E_0(me, q) * (-mp.log(interface_factor(q, mp.mpf(1) / 2)))
    bar_closed = E_0(me, q) * mp.log(2 * q * (q ** 2 + 1) / (q ** 4 + 1))

    miss = locate_the_miss(me, q)
    # pin spread for the E_0 row
    # `from witness import ...` (the previous spelling) names a module that
    # exists nowhere on the path -- `_q0_value_for_anchor` lives in the
    # qou_substrate PACKAGE. So that import always raised, the bare `except`
    # swallowed it, and every run silently fell back to the hardcoded literal
    # below, which is the SUPERSEDED muon pin A. This witness therefore
    # published `q0Values.muon = A` no matter what the anchor said, and the
    # q0-anchor audit correctly flagged it as a comparison mislabelling its
    # own leg. Import the real module, and do NOT swallow a failure: a
    # comparison that cannot read one of its legs must not invent it.
    from qou_substrate.witness import _q0_value_for_anchor  # noqa: E402
    _muon_pin = _q0_value_for_anchor("muon")
    if not _muon_pin:
        raise RuntimeError(
            "cannot resolve the muon anchor; refusing to fall back to a "
            "hardcoded pin -- that is how the superseded value A survived here"
        )
    _MUON_PIN_STR = str(_muon_pin)
    q_mu = mp.mpf(_MUON_PIN_STR)
    e0_mu = E_0(me, q_mu)
    pin_spread = abs(e0_mu - E_0(me, q)) / E_0(me, q)
    for row in miss:
        if row["ingredient"] == "energy scale E_0":
            row["allowed_rel_move"] = fmt(pin_spread)
            row["allowed_rel_move_meaning"] = "the ENTIRE proton-vs-muon pin spread"
            row["displacement_over_allowed"] = fmt(
                abs(mp.mpf(row["required_rel_move"])) / pin_spread)

    checks = lean_bound_crosscheck(me, q)

    witness = {
        "computation": "deuteron-two-body-kernel-overshoot",
        "scriptFile": os.path.basename(__file__),
        # q₀-anchor stamp (added 2026-08-26). The pin was recorded only in the
        # prose `inputs.q0_pin` below, which `q0_anchor_consistency_audit.py`
        # cannot read — so this witness sat in Q0_ANCHOR_MISSING,
        # indistinguishable from a producer that simply forgot. It reads BOTH
        # pins on purpose (proton for every result; muon solely to size
        # `pin_spread`, the proton-vs-muon separation used as the "allowed
        # move" scale for E_0), so the honest label is `comparison`, not
        # `proton`: a single q0Value would assert the one pin this compute
        # deliberately does not have.
        "q0Anchor": "comparison",
        "q0Values": {"proton": Q_50_DIGIT_STR, "muon": _MUON_PIN_STR},
        "q0AnchorReason": (
            "results are computed at the PROTON pin (owner directive "
            "2026-08-07); the MUON pin is read once, to compute the "
            "proton-vs-muon spread of E_0 that bounds how far the energy "
            "scale could move. The comparison is the subject of the "
            "`allowed_rel_move` column, not an accidental layer straddle."
        ),
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
        "engine": "mpmath mpf at 60 dps; no float64 anywhere; 0 free parameters",
        "free_parameters": 0,
        "inputs": {
            "q0": fmt(q),
            "q0_pin": "proton (experimental / Physical-Observations layer)",
            "m_e_MeV": fmt(me),
            "B_AME_2H_MeV": fmt(B_AME_2H),
            "B_AME_role": "COMPARISON TARGET ONLY — never inverted into any output",
            "convention": "D (z = q^3/(q^2+1)), owner ruling R1 2026-08-15",
            "pn_convention": "bring_color_weighted, owner ruling R3 2026-08-15",
            "arithmetic": "mpmath mpf, 60 dps",
        },
        "results": {
            "z_D": fmt(z_D(q)),
            "h": fmt(h_q(q)),
            "flavor_delta": fmt(flavor_split_leading(q)),
            "t_derived": fmt(t0),
            "E_0_MeV": fmt(E_0(me, q)),
            "interface_factor": fmt(interface_factor(q, t0)),
            "L_pn": fmt(bond_L(q, t0)),
            "B_sym_2H_MeV": fmt(b_sym),
            "overshoot_percent": fmt(overshoot_pct),
            "residual_MeV": fmt(b_sym - B_AME_2H),
            "bar_symmetric_B_MeV": fmt(b_bar),
            "bar_symmetric_closed_form_MeV": fmt(bar_closed),
            "bar_symmetric_closed_form_agrees": bool(abs(b_bar - bar_closed) < mp.mpf("1e-50")),
            "bar_symmetric_closed_form":
                "E_0 * ln( 2 q (q^2+1) / (q^4+1) )  [writhe factor exactly 1 at t=1/2]",
            "flavour_split_contribution_MeV": fmt(b_sym - b_bar),
            "admissible_band": admissible_band(me, q),
            "free_parameter_inventory": free_parameter_inventory(),
            "continuous_free_parameter_count": 0,
            "where_the_miss_lives": miss,
            "lean_bound_crosscheck": checks,
            "lean_crosscheck_all_hold": all(c["holds"] for c in checks),
        },
        "verdict": (
            "B_sym(2H) = E_0 * L_pn = 2.8328 MeV against B_AME = 2.2246 MeV, +27.34 %, "
            "with ZERO continuous free parameters: m_e is CAL-1, q_0 is the CAL-2 proxy "
            "pin, E_0's form is derived, the interface coefficient a = 1 is forced by "
            "convexity, the colour weight is derived from prop:flavor-split-substrate, "
            "and the writhe factor is Lean-proved unique up to sign. So the overshoot is "
            "a PARAMETER-FREE PREDICTION FAILURE of the two-body kernel, not a tuning gap. "
            "Of the ingredients, only the colour weight t reaches the target at all, and "
            "it must move 673x its own derived scale (delta/4) to do so; a fix through "
            "E_0 needs -21.5 % against a 128 ppb CAL-2 pin spread, i.e. 1.7e6x the "
            "available room, so no CAL-2-respecting fix exists inside this kernel."
        ),
        "scope": (
            "scope-(a) scope-limited negative: the two-body Markov-trace kernel, ALONE, "
            "with convention D and the derived colour weighting, does not reproduce "
            "B_AME(2H). NOT scope-(b): the target IS inside the convention-D admissible "
            "band (reached at t ~ 0.268), so no invariant excludes it, and an ADDITIVE "
            "term is untouched by anything measured here. The convention-C-era claim that "
            "2H sat below the whole band does not survive the R1 ruling."
        ),
        "lean": "QOU.MassTheory.DeuteronTwoBodyKernel (7 theorems, sorry-free)",
        "wired": False,
        "notes": ("Supersedes the band [2.0507, 3.7978] and the requirement t = 0.119453 "
                  "quoted in docs/audits/2026-08-25-low-isotope-binding-error-staleness-"
                  "vs-gap.md section 6: both are NO-WRITHE values, computed before the "
                  "2026-08-09 writhe normalisation was applied to the p-n bond. The "
                  "writhe-consistent band is [1.5598, 4.2887] and the root is t = 0.26807."),
    }

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "deuteron-two-body-kernel-overshoot.witness.json")
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
        json.dump(witness, fh, indent=1)
        fh.write("\n")

    print(f"q0            = {mp.nstr(q, 22)}   (proton pin)")
    print(f"m_e           = {mp.nstr(me, 12)} MeV")
    print(f"z_D           = {mp.nstr(z_D(q), 22)}")
    print(f"h             = {mp.nstr(h_q(q), 22)}")
    print(f"delta         = {mp.nstr(flavor_split_leading(q), 22)}")
    print(f"t_derived     = {mp.nstr(t0, 22)}")
    print(f"E_0           = {mp.nstr(E_0(me, q), 22)} MeV")
    print(f"L_pn          = {mp.nstr(bond_L(q, t0), 22)}")
    print(f"B_sym(2H)     = {mp.nstr(b_sym, 22)} MeV")
    print(f"B_AME(2H)     = {mp.nstr(B_AME_2H, 12)} MeV")
    print(f"overshoot     = +{mp.nstr(overshoot_pct, 8)} %")
    print(f"bar-symmetric = {mp.nstr(b_bar, 22)} MeV  (closed form agrees: "
          f"{abs(b_bar - bar_closed) < mp.mpf('1e-50')})")
    print()
    print("WHERE THE MISS LIVES")
    for row in miss:
        keys = [k for k in ("required_displacement", "required_rel_move",
                            "displacement_over_allowed", "fraction_of_miss") if k in row]
        print(f"  {row['ingredient']:<40} " +
              "  ".join(f"{k}={row[k]}" for k in keys))
    print()
    print("LEAN BOUND CROSS-CHECK")
    for c in checks:
        print(f"  [{'OK ' if c['holds'] else 'BAD'}] {c['claim']}")
    print(f"\nwrote {out}   ({time.time() - t_start:.1f}s)")

    assert all(c["holds"] for c in checks), "a Lean bound disagrees with the mpf value"
    assert overshoot_pct > 27, "overshoot must exceed 27 %"
    assert witness["results"]["bar_symmetric_closed_form_agrees"]
    print("ALL ASSERTIONS PASS")


if __name__ == "__main__":
    main()
