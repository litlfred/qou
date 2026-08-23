#!/usr/bin/env python3
"""Whipple -> observable: does the toroidal amplitude PREDICT the even/odd ratio?

The Whipple-rotation identification ties the bar-even (cosh / binding) and
bar-odd (sinh / Q_beta) channels of the complex volume V. It is mathematically
exact (whipple-gamma-constant-gridverify, whipple-physical-windings-probe). The
open question is whether that exact tie has OBSERVABLE content: does the Whipple
amplitude at the physical forced windings (mu, nu) = (1/2, d-1/2) reproduce the
observed even/odd binding ratio?

This is an HONEST parameter-free test -- NOT a fit. We compute, at each axial
distance d, the Whipple constant magnitude |C(nu, mu)| and the raw toroidal
amplitude ratio |P/Q|, and compare to the observed B_even_cosh / B_odd_sinh
ratio from `binding-bar-even-odd-probe.witness.json`. No constant is tuned; a
match within 5% would be signal, otherwise the verdict is an explicit NULL
(the exact structural tie does not, by itself, yield the observable ratio --
sharpening what the binding-closure gap must still supply).

-- Ref: [whipple1917] https://doi.org/10.1112/plms/s2-16.1.301
"""
import json
import os

import mpmath as mp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
HALF = mp.mpf(1) / 2


def gamma_constant_mag(nu, mu):
    with mp.workdps(60):
        c = +mp.sqrt(2 / mp.pi)
    return abs(c / mp.gamma(nu + mu + HALF))  # |e^{-i pi nu}| = 1


def toroidal_amp_ratio(nu, mu, a):
    """|P^{-mu}_{nu-1/2}(coth a)| / |sqrt(sinh a) * Q^{nu}_{mu-1/2}(cosh a)|."""
    p = mp.legenp(nu - HALF, -mu, mp.coth(a), type=3)
    qq = mp.legenq(mu - HALF, nu, mp.cosh(a), type=3)
    return abs(p) / abs(mp.sqrt(mp.sinh(a)) * qq)


# Observed even/odd binding split (from binding-bar-even-odd-probe.witness.json).
# Keyed by the two-body-ish axial distance d we can cleanly assign: the deuteron
# is the clean d = 2 (single pn bond, the meson two-body channel). Heavier
# isotopes have no single d, so they are reported but not scored.
here = os.path.dirname(__file__)
beo_path = os.path.join(here, "..", "binding-bar-even-odd-probe.witness.json")
observed = {}
try:
    with open(beo_path, encoding="utf-8") as f:
        beo = json.load(f)

    def walk(o):
        if isinstance(o, dict):
            if "B_even_cosh_MeV" in o and "B_odd_sinh_MeV" in o:
                ev = float(o["B_even_cosh_MeV"])
                od = float(o["B_odd_sinh_MeV"])
                ame = float(o.get("B_AME_MeV", "nan"))
                yield (ev, od, ame)
            for v in o.values():
                yield from walk(v)
        elif isinstance(o, list):
            for v in o:
                yield from walk(v)

    rows = list(walk(beo))
    # first row is the deuteron (A=2, B_AME ~ 2.22)
    for ev, od, ame in rows:
        if abs(ame - 2.2245662) < 1e-3:
            observed["2"] = {"B_even": ev, "B_odd": od, "B_AME": ame}
            break
    # all labelled isotopes, for the factor-2 generalization falsification below
    _labels = {
        2.2245662: ("2H", 2), 8.4817962: ("3H", 3),
        7.71804132: ("3He", 3), 28.2956624: ("4He", 4),
    }
    for ev, od, ame in rows:
        for key, (iso, A) in _labels.items():
            if abs(ame - key) < 1e-2:
                observed.setdefault("_isotopes", {})[iso] = {
                    "A": A, "B_even": ev, "B_odd": od, "B_AME": ame,
                }
except Exception as e:  # noqa: BLE001
    observed["_error"] = str(e)

A_PROBE = mp.mpf("0.9")  # representative axial coordinate
per_d = {}
match_found = False
for d in (2, 3, 4):
    mu = HALF
    nu = mp.mpf(d) - HALF
    Cmag = gamma_constant_mag(nu, mu)
    amp = toroidal_amp_ratio(nu, mu, A_PROBE)
    row = {
        "windings_mu_nu": [mp.nstr(mu, 4), mp.nstr(nu, 4)],
        "whipple_C_magnitude": mp.nstr(Cmag, 10),
        "toroidal_amp_ratio_at_a": mp.nstr(amp, 10),
    }
    if str(d) in observed:
        o = observed[str(d)]
        obs_ratio = o["B_even"] / o["B_odd"]
        row["observed_B_even_over_B_odd"] = mp.nstr(mp.mpf(obs_ratio), 8)
        # parameter-free candidate matches (no tuning): C, 1/C, amp, 1/amp
        cands = {
            "C": float(Cmag),
            "1/C": float(1 / Cmag),
            "amp": float(amp),
            "1/amp": float(1 / amp),
        }
        best_k, best_rel = None, None
        for k, val in cands.items():
            rel = abs(val - obs_ratio) / abs(obs_ratio)
            if best_rel is None or rel < best_rel:
                best_k, best_rel = k, rel
        row["best_parameterfree_match"] = best_k
        row["best_rel_err"] = f"{best_rel:.4f}"
        row["is_match_within_5pct"] = bool(best_rel < 0.05)
        match_found = match_found or bool(best_rel < 0.05)
    per_d[str(d)] = row

# Factor-2 generalization falsification: the deuteron's 2/|C| ≈ observed ratio
# is a COINCIDENCE. Test the derived-factor hypothesis B_even/B_odd = A/|C(d=A)|
# across every isotope; it fails badly for A ≥ 3, so the factor-2 is not a
# structural law (do NOT wire — anti-fit discipline).
factor2_generalization = {}
_iso = observed.get("_isotopes", {})
for iso, o in _iso.items():
    A = o["A"]
    obs_ratio = o["B_even"] / o["B_odd"]
    A_over_C = A / float(gamma_constant_mag(mp.mpf(A) - HALF, HALF))
    rel = abs(A_over_C - obs_ratio) / abs(obs_ratio)
    factor2_generalization[iso] = {
        "A": A,
        "observed_B_even_over_B_odd": f"{obs_ratio:.4f}",
        "A_over_C_d_eq_A": f"{A_over_C:.3f}",
        "rel_err": f"{rel:.4f}",
        "matches_within_5pct": bool(rel < 0.05),
    }
factor2_is_derived = all(
    v["matches_within_5pct"] for v in factor2_generalization.values()
) and len(factor2_generalization) >= 2

assertions = {
    "whipple_amplitude_computed_all_d": True,
    "observed_deuteron_ratio_loaded": "2" in observed,
    "factor2_is_a_derived_law_not_coincidence": factor2_is_derived,
}
# The factor-2 assertion is EXPECTED to be False (coincidence); allPassed tracks
# only the compute/load assertions, not the physics hypothesis.
all_passed = bool(assertions["whipple_amplitude_computed_all_d"]
                  and assertions["observed_deuteron_ratio_loaded"])

if match_found:
    verdict = (
        "SIGNAL: a parameter-free Whipple toroidal amplitude reproduces the "
        "observed even/odd binding ratio within 5% at the physical windings -- "
        "see per_d.best_parameterfree_match. The exact structural tie carries "
        "observable content."
    )
else:
    verdict = (
        "NULL (honest, not a fit): the bare Whipple constant |C(nu,mu)| and the "
        "raw toroidal amplitude ratio at the physical forced windings "
        "(mu,nu)=(1/2,d-1/2) do NOT reproduce the observed even/odd binding "
        "ratio (deuteron B_even/B_odd) to 5% under any parameter-free "
        "combination {C, 1/C, amp, 1/amp}. The Whipple identification is "
        "mathematically exact but its BARE amplitude is not the observable "
        "ratio -- the binding-closure gap must supply the E0-scaled, "
        "many-body dressing between the dimensionless toroidal amplitude and "
        "the MeV even/odd split. This sharpens (does not close) the gap; "
        "nothing is fitted or wired. FURTHER: the tempting deuteron 2/|C| match "
        "is FALSIFIED as a derived factor — ratio = A/|C(d=A)| fails 446%/1644% "
        "at A=3/4 (see factor2_generalization_falsification); the factor-2 is a "
        "coincidence, explicitly NOT wired."
    )

witness = {
    "computation": "whipple_observable_ratio_probe",
    "description": (
        "Honest parameter-free test of whether the Whipple toroidal amplitude "
        "at the physical forced windings (mu,nu)=(1/2,d-1/2) reproduces the "
        "observed even/odd binding ratio (deuteron, d=2). No fit; explicit "
        "NULL if no parameter-free match. auditOnly."
    ),
    "discipline": "canonical-derivation / observable-connection test (no fit)",
    "auditOnly": True,
    "results": {
        "per_d": per_d,
        "observed": {k: v for k, v in observed.items() if not k.startswith("_")},
        "factor2_generalization_falsification": factor2_generalization,
        "factor2_finding": (
            "The deuteron 2/|C(d=2)| = 3.33 ≈ observed 3.373 (1.2%) is a "
            "COINCIDENCE, not a derived factor. The hypothesis "
            "B_even/B_odd = A/|C(d=A)| fails badly for A≥3 (446% off at A=3, "
            "1644% at A=4) because |C| collapses (0.60, 0.24, 0.069) while the "
            "observed ratios stay O(2-7). The fixed constant 3.33 also matches "
            "⁴He (0.3%) but not ³H/³He — i.e. it hits the two N=Z cases only, a "
            "fixed number matching 2 of 4 points, not a law. NOT wired "
            "(anti-fit / no-seventh-ansatz discipline)."
        ),
        "note": (
            "Only the deuteron (d=2, single pn bond) has a clean axial distance; "
            "heavier isotopes lack a single d and are reported unscored for the "
            "amplitude test. The factor-2 falsification uses the falsifiable "
            "hypothesis ratio = A/|C(d=A)| regardless of whether d=A is exact."
        ),
    },
    "assertions": assertions,
    "allPassed": all_passed,
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(here, "whipple-observable-ratio-probe.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("per_d:")
for d, r in per_d.items():
    print(f"  d={d}: {r}")
print(f"\nobserved: {observed}")
print(f"\nallPassed: {all_passed}")
print(f"VERDICT: {verdict}")
print(f"\nwitness -> {out}")
