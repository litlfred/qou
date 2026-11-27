#!/usr/bin/env python3
"""Bean qou-j16x — DIAGNOSTIC: the required det-gate magnitude m* and whether any
DERIVED categorical constant supplies it (0-fit, nothing wired).

THE CRUX (qou-j16x). The `A4InterfaceMagnitude` det-gate is a ONE-SCALAR gate:
`b₄(m) = −ln det(I + m·S)`, S the ⁴He `[1⁴]` complete-graph writhe-exchange matrix
with the DERIVED spectrum {±√5, ±1}, so

    det(I + m·S) = (1 − 5m²)(1 − m²),     b₄(m) = −ln[(1 − 5m²)(1 − m²)]

(both confirmed against `A4InterfaceMagnitude.lean` / #3924). `A4InterfaceMagnitude`
already PROVED this form surjects onto (0,∞) in m∈(0,1/√5): so hitting the ⁴He target
by CHOOSING m is a FIT and forbidden. The open question this probe answers is the
DIAGNOSTIC one: what is the required m*, and does it coincide (0-fit) with an
INDEPENDENTLY-derived framework constant? If yes → a genuine derived lead. If no →
honest scope-(a): the det-gate needs a fitted m matching no derived constant.

NORMALIZATION. The det-gate cumulant `−ln det` is DIMENSIONLESS; the corpus writhe
witness (`b4-1four-complete-graph-writhe-signs`, w_pn=0 row: det=0.563519,
neg_log_det=0.573554, MeV=2.400885) sets MeV = E₀·(−ln det), E₀=4.1859808 MeV
(check: 4.1859808·0.573554 = 2.40088 ✓). So the CANONICAL det-gate normalization is
E₀. We ALSO report the E₀·τ_vac normalization (the *multiplicative* B=E₀·τ_vac·(1−∏f)
convention of the sibling front-4 probe) as an alternative, since the two front-4
objects use different scales.

DIAGNOSTIC ONLY. m* is obtained by inverting the target (an anchor-inversion = FIT);
it is NEVER wired. B_AME/target are diagnostic-only. free_parameters = 0.

`-- Ref:` QOU.MassTheory.A4InterfaceMagnitude (det form, surjectivity, closed-form m*);
b4-1four-complete-graph-writhe-signs (E₀ normalization); closed_form_tau_M (z, h).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path[:0] = [str(COMP), str(COMP / "substrate")]
import closed_form_tau_M as C  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This was a hardcoded PROTON
# literal -- the right VALUE by the wrong MECHANISM: it cannot follow the
# anchor, and it is invisible to the retired-pin drain because it never
# matched. Spellings across this family ran 13 to 60 digits for one pin.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

# ---- derived substrate constants (0-fit) -----------------------------------
Q0 = mp.mpf(Q_50_DIGIT_STR)
M_E = mp.mpf("0.51099895069")
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(M_E, Q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
Z_MK = C.markov_z(Q0)
H_MK = C.hecke_h(Q0)
TAU_P = mp.mpf("1.22036288908669305595736107223")
TRM_D = mp.mpf("0.7280918153466761555460727563")
TAU_N = TRM_D / (TAU_P * Z_MK)
TAU_VAC4 = TAU_P ** 2 * TAU_N ** 2         # ⁴He (Z=2,N=2)
INV_SQRT5 = 1 / mp.sqrt(5)

# ---- documented A=4 targets (DIAGNOSTIC-ONLY; never inverted into production) ---
B4_TARGET = mp.mpf("9.243")                # [1⁴] connected 4-body cumulant, MeV
MU4_TARGET = mp.mpf("4.591048")            # additive simplex residual |μ₄|, MeV


def detG(m: mp.mpf) -> mp.mpf:
    """det(I + m·S) = (1 − 5m²)(1 − m²) — the DERIVED closed form (spectrum {±√5,±1})."""
    return (1 - 5 * m ** 2) * (1 - m ** 2)


def b4_dimless(m: mp.mpf) -> mp.mpf:
    """Dimensionless det-gate cumulant −ln det(I + m·S)."""
    return -mp.log(detG(m))


def mstar_from_dimless(t: mp.mpf) -> mp.mpf:
    """Closed-form inverse (A4InterfaceMagnitude.uStar): the smaller root of
    5u² − 6u + (1 − e^{−t}) = 0 in u = m², then m* = √u.  Physical branch m*<1/√5."""
    D = mp.exp(-t)                          # target determinant value ∈ (0,1)
    u = (6 - mp.sqrt(16 + 20 * D)) / 10
    return mp.sqrt(u)


# ---- candidate DERIVED constants to test m* against (all 0-fit) -------------
def candidate_constants() -> dict:
    """Independently-derived framework scalars m* might coincide with."""
    return {
        "h (Hecke)": H_MK,
        "2h": 2 * H_MK,
        "z (Markov)": Z_MK,
        "z - h": Z_MK - H_MK,
        "z - h/2": Z_MK - H_MK / 2,
        "1/sqrt5 (writhe cap)": INV_SQRT5,
        "q0 - 1": Q0 - 1,
        "(q0-1)*... n/a": mp.mpf("nan"),
        "sqrt(h)": mp.sqrt(H_MK),
        "h/z": H_MK / Z_MK,
        "z^2": Z_MK ** 2,
        "1 - z": 1 - Z_MK,
        "z - 1/sqrt5": Z_MK - INV_SQRT5,
        "1/sqrt5 - h": INV_SQRT5 - H_MK,
        "1/sqrt5 - h/2": INV_SQRT5 - H_MK / 2,
        "(1/sqrt5)*z": INV_SQRT5 * Z_MK,
        "h + (q0-1)": H_MK + (Q0 - 1),
        "2h - (q0-1)": 2 * H_MK - (Q0 - 1),
        "sqrt(h*z)": mp.sqrt(H_MK * Z_MK),
        "tanh... n/a": mp.mpf("nan"),
    }


def match_report(mstar: mp.mpf, cands: dict) -> list:
    rows = []
    for name, val in cands.items():
        if mp.isnan(val):
            continue
        rel = abs(mstar - val) / abs(mstar)
        rows.append((name, val, rel))
    rows.sort(key=lambda r: r[2])
    return rows


def main() -> int:
    print("=" * 72)
    print("bean qou-j16x — required det-gate m* vs derived constants (DIAGNOSTIC)")
    print("=" * 72)
    print(f"Q0        = {mp.nstr(Q0, 18)}")
    print(f"E0        = {mp.nstr(E0, 18)} MeV")
    print(f"z (Markov)= {mp.nstr(Z_MK, 18)}")
    print(f"h (Hecke) = {mp.nstr(H_MK, 18)}")
    print(f"tau_vac4  = {mp.nstr(TAU_VAC4, 18)}")
    print(f"E0*tvac4  = {mp.nstr(E0 * TAU_VAC4, 18)} MeV")
    print(f"1/sqrt5   = {mp.nstr(INV_SQRT5, 18)}  (writhe cap; det>0 iff m<this)")
    print()

    # confirm the closed form against A4InterfaceMagnitude at a sample point
    m_probe = mp.mpf("0.3")
    assert abs(detG(m_probe) - (1 - 6 * m_probe**2 + 5 * m_probe**4)) < mp.mpf("1e-40")

    results = {}
    for norm_name, norm in [("E0 (canonical det-gate)", E0),
                            ("E0*tau_vac4 (mult. B scale)", E0 * TAU_VAC4)]:
        for tgt_name, tgt in [("b4=9.243", B4_TARGET), ("mu4=4.591048", MU4_TARGET)]:
            t_dimless = tgt / norm                    # required dimensionless cumulant
            mstar = mstar_from_dimless(t_dimless)
            # verify round-trip: E0*b4_dimless(mstar) hits the target
            back = norm * b4_dimless(mstar)
            assert abs(back - tgt) < mp.mpf("1e-30"), (norm_name, tgt_name, back)
            key = f"{norm_name} | {tgt_name}"
            results[key] = mstar
            print("-" * 72)
            print(f"NORM = {norm_name},  TARGET = {tgt_name}")
            print(f"  required dimensionless cumulant t* = {mp.nstr(t_dimless, 12)}")
            print(f"  required det value e^-t*           = {mp.nstr(mp.exp(-t_dimless), 12)}")
            print(f"  ==> required m* = {mp.nstr(mstar, 15)}")
            print(f"      (physical: m*<1/sqrt5={mp.nstr(INV_SQRT5,8)}? "
                  f"{'YES' if mstar < INV_SQRT5 else 'NO — UNPHYSICAL'})")
            rows = match_report(mstar, candidate_constants())
            print(f"      nearest derived constants (relative distance):")
            for name, val, rel in rows[:5]:
                flag = "  <== 0-FIT MATCH" if rel < mp.mpf("1e-3") else ""
                print(f"        {name:24s} = {mp.nstr(val,12):14s}  rel={mp.nstr(rel,4)}{flag}")

    # ---- FORWARD test (the non-inverting direction): plug each derived constant
    #      in AS m and report the resulting b4 fraction of target. Zero inversion. ----
    print("=" * 72)
    print("FORWARD (non-fit): derived constant AS m -> b4 (E0 norm) / target 9.243")
    print("=" * 72)
    forward = []
    for name, val in candidate_constants().items():
        if mp.isnan(val) or val <= 0 or 5 * val ** 2 >= 1:
            continue                      # skip unphysical (det<=0) / non-positive
        b4_mev = E0 * b4_dimless(val)
        frac = b4_mev / B4_TARGET
        forward.append((name, val, b4_mev, frac))
    forward.sort(key=lambda r: abs(r[3] - 1))
    for name, val, b4_mev, frac in forward[:8]:
        print(f"  m={name:24s}={mp.nstr(val,10):12s} -> b4={mp.nstr(b4_mev,8):10s} MeV "
              f"= {mp.nstr(frac*100,6)}% of target")

    # ---- verdict ----
    print("=" * 72)
    canonical_mstar = results["E0 (canonical det-gate) | b4=9.243"]
    best = match_report(canonical_mstar, candidate_constants())[0]
    matched = best[2] < mp.mpf("1e-3")
    print(f"CANONICAL (E0 norm, b4=9.243):  m* = {mp.nstr(canonical_mstar, 15)}")
    print(f"  nearest derived constant: {best[0]} = {mp.nstr(best[1],12)}  "
          f"(rel {mp.nstr(best[2],4)})")
    verdict = ("DERIVED-LEAD (m* coincides with a derived constant)" if matched
               else "SCOPE-(a) FIT-NEEDED (m* matches NO derived constant to 0.1%)")
    print(f"  VERDICT: {verdict}")
    print("=" * 72)

    # ---- witness ----
    w = WitnessBuilder("b4-nonsaturating-mstar-diagnostic", engine="mpmath")
    w.set_description(
        "DIAGNOSTIC (bean qou-j16x): the required A4InterfaceMagnitude det-gate "
        "magnitude m* for the det form b4=-ln[(1-5m^2)(1-m^2)] (derived spectrum "
        "{+-sqrt5,+-1}, #3924/A4InterfaceMagnitude.lean) to hit the 4He targets, and "
        "whether any INDEPENDENTLY-derived framework constant supplies it (0-fit). "
        "Normalization MeV=E0*(-ln det) is the corpus writhe convention "
        "(b4-1four-complete-graph-writhe-signs); E0*tau_vac4 reported as the "
        "multiplicative-B alternative. m* is an anchor-inversion (a FIT) and is NEVER "
        "wired; B_AME/targets diagnostic-only; free_parameters=0. VERDICT: " + verdict
    )
    w.set_audit_only("docs/audits/2026-08-02-b4-nonsaturating-mstar-diagnostic.md")
    w.add_data("q0", mp.nstr(Q0, 30))
    w.add_data("E0_MeV", mp.nstr(E0, 20))
    w.add_data("z_markov", mp.nstr(Z_MK, 20))
    w.add_data("h_hecke", mp.nstr(H_MK, 20))
    w.add_data("tau_vac4", mp.nstr(TAU_VAC4, 20))
    w.add_data("inv_sqrt5", mp.nstr(INV_SQRT5, 20))
    w.add_data("free_parameters", 0)
    w.add_data("targets_never_inverted_into_production", True)
    w.add_data("verdict", verdict)
    for key, mstar in results.items():
        w.add_data(f"mstar__{key}", mp.nstr(mstar, 18))
        w.add_data(f"physical__{key}", bool(mstar < INV_SQRT5))
    w.add_data("canonical_mstar_E0_b4", mp.nstr(canonical_mstar, 18))
    w.add_data("nearest_constant_name", best[0])
    w.add_data("nearest_constant_value", mp.nstr(best[1], 18))
    w.add_data("nearest_constant_relerr", mp.nstr(best[2], 8))
    w.add_data("derived_lead", bool(matched))
    w.add_data("forward_constant_as_m_pct_of_target",
               {name: mp.nstr(frac * 100, 8) for name, _, _, frac in forward})
    # Was add_assertion("detG_closed_form_ok", 1, 1, source="...verified to 40dps").
    # The verification is REAL -- a bare `assert` earlier in this function -- but only
    # its conclusion reached the witness as a literal, so deleting that assert would
    # have left this reporting "passed". Carry the measured deviation instead.
    _detG_dev = abs(detG(m_probe) - (1 - 6 * m_probe ** 2 + 5 * m_probe ** 4))
    w.add_assertion("detG_closed_form_max_deviation", mp.nstr(_detG_dev, 12), "0.0",
                    tolerance="1e-40",
                    source="detG(m)=(1-5m^2)(1-m^2)=1-6m^2+5m^4, measured at m=0.3")
    w.add_assertion("canonical_mstar_physical",
                    1 if canonical_mstar < INV_SQRT5 else 0, 1,
                    source="required m* below writhe cap 1/sqrt5 (det>0)")
    # Was an add_assertion(name, X, X) -- computed and expected the SAME expression,
    # so it read as a check while being `x == x`: tautologically true, unable to fail,
    # and rendered as "passed": true for the QA pipeline. It is a RECORDED FINDING
    # with no independent expectation, so it belongs in add_data. Bean qou-ploj.
    w.add_data("derived_lead_found", 1 if matched else 0)
    w.add_data("derived_lead_found_source",
               "whether m* matches a derived constant to <0.1% "
                           "(expected 0 = scope-(a) fit-needed)")
    out = w.save()
    print(f"witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
