#!/usr/bin/env python3
"""Why `canonical-with-proper-tower` does not reproduce: the E_0 calibration is
evaluated at 96 % of Φ_q's pole, where the cap that is supposed to protect it
never fires (bean qou-0gqn).

THE SYMPTOM. `computations/canonical-with-proper-tower.witness.json`, written
2026-06-14, does not reproduce from today's tree. `E_0_MeV_per_cat` collapses
by 3.59e6 (243.5284428 -> 6.788428e-05), and every `B_MeV` follows it, because

    B = E_0 * (m_free - m_atom)

holds exactly in both the committed file and a fresh run.

WHAT IT IS NOT. The obvious suspect is `8cf5569648` ("swap the production
tower to the Lean-mandated towerTerm"), which introduced a `term=` parameter
and made `tower_term_li2q` the default. It is not the cause: that commit
DELIBERATELY pins the calibration to the historical form --

    # MASS context (proton absolute vs M_P_MEV) ... pins term="phi_q"
    r = binding_per_irrep_tower(1, 0, E_0=1.0, pair_mode=pair_mode,
                                term="phi_q")

-- and `_tower_spec("phi_q", cap_frac)` threads `cap_frac` faithfully into
`phi_q_safe`. The calibration path uses the same function June used.

Two further non-causes, checked and excluded:

  * The `_E0_PI_CACHE` / `_E0_TOWER_CACHE` are both keyed by `pair_mode`, so
    neither leaks one mode's value into the other.
  * `full` and `adjacent` now yield a BIT-IDENTICAL E_0 where June recorded
    243.5284 vs 249.4030. That is correct, not a defect: the calibration is
    A=1, a single generator, so there are no PAIRS and `pair_mode` is a no-op
    by construction. It is the June pair of distinct values that wants
    explaining, not today's single one.

WHAT IT IS. `phi_q_safe` clamps its argument to `cap_frac * q` to hold it off
the pole at |z| = q. With `cap_frac = 0.98` and q = 1.1099785828 the cap is
1.0877790. The proton's canonical V̂ is

    V̂ = [0.6629533727, 1.0646262154]

and the larger entry is **95.91 % of q -- below the cap**. So the clamp never
fires, and Φ_q is evaluated essentially at its singularity, returning 7.81e6
for that one generator.

The cap does not regularise this. It bounds Φ_q at 2.66e7, which is already
seven orders above the ~3.85 total the June witness implies; it relocates the
blow-up rather than removing it. Between V = 0.90 and the cap -- the whole band
the cap declares safe -- Φ_q spans a factor of ~300.

THE CONDITIONING IS THE POINT. At the actual calibration point a 0.188 %
change in V̂ (±0.001 either side) moves Φ_q by 9.06 % -- a relative-error
amplification of **48x**, measured. A quantity that magnifies its input's
relative error 48-fold is not a calibration; `E_0 = M_P_MEV / Φ_q(V̂)` inherits
all of it.

(An earlier draft of this file said "0.09 % -> 9.1 %, ~100x". That compared a
TWO-sided Φ_q change against a ONE-sided V̂ window and roughly doubled the
amplification. The probe's own threshold caught it. The finding is unchanged;
the factor is 48, not 100.)

AND THE V̂ MOVED TOO. Reproducing June's implied total of 3.85282 through
`phi_q` would need V̂ = 0.1432, i.e. 12.90 % of q -- 7.4x smaller than the
1.0646 the pipeline produces now. `tower_term_li2q` on today's V̂ gives 1.4447
(E_0 = 649.44), also not 243.53. So NEITHER current term at today's V̂
reproduces the witness, and the V̂ itself changed as well as the term.

SCOPE. scope-(a) throughout. This establishes that the committed artifact is
not derivable from its own producer, and that the calibration is
ill-conditioned where it is being evaluated. It does NOT establish which set of
numbers is right, that the tower formula is wrong, or which commit moved V̂ --
that bisect is not done. This is an exploratory tower probe; neither the
committed 4573 MeV nor the fresh 9.5e-5 MeV is a physical binding energy, which
is not itself news for this object.

PRECISION NOTE. `phi_q_safe` is float64 by construction and this probe reports
what production actually computes, so its Φ_q values are float64 and are
labelled as such. The sensitivity analysis is recomputed independently in
mpmath at 50 dps so the conditioning claim does not rest on the arithmetic it
is measuring.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
for _p in (_HERE.parent, _HERE.parent / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

import canonical_tower as CT  # noqa: E402
from mass_at_3A_proper import (  # noqa: E402
    Q0_PROTON,
    phi_q_safe,
    tower_term_li2q,
)

#: What the committed witness recorded, 2026-06-14.
JUNE_E0_FULL = mp.mpf("243.5284427694042")
JUNE_E0_ADJACENT = mp.mpf("249.4029733")
M_P_MEV = mp.mpf("938.272")
CAP_FRAC = mp.mpf("0.98")


def phi_q_exact(z, q, max_k: int = 4000):
    """Φ_q(|z|) = ∏_k 1/(1 − q^{−k}|z|), in mpmath at the ambient dps.

    Deliberately NOT a call into `phi_q_safe`: the conditioning claim below is
    about the mathematics near the pole, and computing it with the float64
    function under test would make the answer a property of that function's
    arithmetic rather than of Φ_q.
    """
    z, q = mp.mpf(z), mp.mpf(q)
    qi = 1 / q
    prod = mp.mpf(1)
    for k in range(1, max_k + 1):
        f = 1 - qi**k * abs(z)
        if abs(f) < mp.mpf("1e-40"):
            return mp.inf
        prod /= f
        if qi**k * abs(z) < mp.mpf("1e-40"):
            break
    return prod


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    q = mp.mpf(str(Q0_PROTON))
    cap = CAP_FRAC * q
    V = [mp.mpf(str(float(v)))
         for v in CT.per_gen_V_hat_canonical(1, 0, include_inter=False)]
    v_max = max(V)

    print("=" * 78)
    print(" Tower E_0: the calibration sits at 96% of Φ_q's pole")
    print("=" * 78)
    print(f"  q                = {mp.nstr(q, 12)}")
    print(f"  cap = 0.98 q     = {mp.nstr(cap, 12)}")
    print(f"  proton V̂         = {[mp.nstr(x, 10) for x in V]}")
    print(f"  max V̂ / q        = {mp.nstr(100 * v_max / q, 6)} %")

    # 1. The cap never fires at the calibration point.
    check("cap_does_not_fire_at_the_calibration_point", v_max < cap,
          v_max=mp.nstr(v_max, 12), cap=mp.nstr(cap, 12),
          fraction_of_q=mp.nstr(v_max / q, 8),
          source="phi_q_safe clamps to cap_frac*q; the proton's larger V̂ is "
                 "BELOW that cap, so the clamp is inert and Φ_q is evaluated "
                 "at 95.91% of its singularity")

    # 2. Φ_q is enormous there — production's own float64 value.
    phi_prod = [phi_q_safe(float(x)) for x in V]
    tot_prod = sum(phi_prod)
    print(f"  Φ_q(V̂) (float64, as production computes) = "
          f"{[f'{x:.6g}' for x in phi_prod]}")
    print(f"     total = {tot_prod:.6g}  ->  E_0 = {938.272 / tot_prod:.6g}")
    check("phi_q_at_the_calibration_point_is_enormous", tot_prod > 1e6,
          total=f"{tot_prod:.6g}", e0=f"{938.272 / tot_prod:.6g}",
          source="Φ_q summed over the proton's two generators exceeds 1e6, "
                 "against the ~3.85 the June witness implies")

    # 3. Conditioning, recomputed in mpmath so it is not float64's opinion.
    d = mp.mpf("0.001")
    lo, hi = phi_q_exact(v_max - d, q), phi_q_exact(v_max + d, q)
    amp = (hi / lo - 1) / (2 * d / v_max)
    print(f"  ±0.001 in V̂ ({mp.nstr(100 * 2 * d / v_max, 4)} % relative) moves "
          f"Φ_q by {mp.nstr(100 * (hi / lo - 1), 4)} %")
    print(f"  relative-error amplification ≈ {mp.nstr(amp, 6)}×")
    check("calibration_is_ill_conditioned", amp > 10,
          amplification=mp.nstr(amp, 8),
          phi_lo=mp.nstr(lo, 10), phi_hi=mp.nstr(hi, 10),
          source="a 0.188% change in V̂ moves Φ_q by 9.06%, so E_0 = M_P/Φ_q "
                 "amplifies its input's relative error by 48×; computed in "
                 "mpmath, not through the float64 function under test")

    # 4. The cap's "safe" band spans orders of magnitude.
    band_lo, band_hi = phi_q_exact(mp.mpf("0.90"), q), phi_q_exact(cap, q)
    print(f"  Φ_q over the sub-cap band [0.90, cap]: "
          f"{mp.nstr(band_lo, 6)} → {mp.nstr(band_hi, 6)}  "
          f"(factor {mp.nstr(band_hi / band_lo, 6)})")
    check("the_cap_does_not_regularise", band_hi / band_lo > 100,
          band_low=mp.nstr(band_lo, 10), band_high=mp.nstr(band_hi, 10),
          ratio=mp.nstr(band_hi / band_lo, 8),
          source="across the whole band the cap declares safe, Φ_q spans a "
                 "factor ~300 — the cap bounds the blow-up, it does not remove "
                 "it, and its bound is still 7 orders above the June total")

    # 5. Neither current term reproduces June at today's V̂.
    tt = sum(mp.mpf(str(tower_term_li2q(float(x)))) for x in V)
    e0_tt = M_P_MEV / tt
    june_total = M_P_MEV / JUNE_E0_FULL
    # Bisect for the V̂ that WOULD give June's total through phi_q.
    lo_b, hi_b = mp.mpf("1e-9"), cap
    for _ in range(200):
        mid = (lo_b + hi_b) / 2
        if phi_q_exact(mid, q) < june_total:
            lo_b = mid
        else:
            hi_b = mid
    print(f"  tower_term_li2q total = {mp.nstr(tt, 8)}  ->  E_0 = "
          f"{mp.nstr(e0_tt, 8)}   (June: {mp.nstr(JUNE_E0_FULL, 8)})")
    print(f"  V̂ that would give June's total via Φ_q = {mp.nstr(lo_b, 8)} "
          f"({mp.nstr(100 * lo_b / q, 5)} % of q), vs actual "
          f"{mp.nstr(v_max, 8)} ({mp.nstr(100 * v_max / q, 5)} %)")
    check("neither_current_term_reproduces_june", abs(e0_tt - JUNE_E0_FULL) > 1,
          tower_term_e0=mp.nstr(e0_tt, 10),
          june_e0=mp.nstr(JUNE_E0_FULL, 10),
          v_hat_needed_for_june=mp.nstr(lo_b, 10),
          v_hat_actual=mp.nstr(v_max, 10),
          source="tower_term gives E_0 = 649.44 and phi_q gives 6.79e-5; "
                 "neither is June's 243.53. Reaching it through Φ_q would need "
                 "V̂ = 0.1432 (12.9% of q), 7.4× smaller than today's 1.0646 — "
                 "so the V̂ moved as well as the term")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "MEASURED (scope-(a)): `canonical-with-proper-tower.witness.json` does "
        "not reproduce because its E_0 calibration evaluates Φ_q at 95.91 % of "
        "the pole, inside the band `cap_frac=0.98` declares safe, so the clamp "
        "never fires. Φ_q = 7.81e6 there against the ~3.85 the witness implies, "
        "and the point is ill-conditioned: a 0.188 % change in V̂ moves Φ_q by "
        "9.06 %, a 48× amplification that E_0 = M_P/Φ_q inherits whole. The "
        "term split of 8cf5569648 is NOT the cause — the calibration is "
        "deliberately pinned to the historical `phi_q` — and neither current "
        "term reproduces June at today's V̂, so the V̂ moved too. This does NOT "
        "say which numbers are right, that the tower formula is wrong, or which "
        "commit moved V̂; that bisect is not done."
        if all_passed else
        "PARTIAL: an assertion failed; read the per-assertion detail before "
        "citing any figure here.")
    print("\nVERDICT:", verdict)

    w = {
        "computation": "tower-e0-pole-conditioning",
        "description":
            "Why canonical-with-proper-tower does not reproduce: the E_0 "
            "calibration evaluates Φ_q at 95.91% of its pole, below the "
            "cap_frac=0.98 clamp, which therefore never fires. Φ_q = 7.81e6 vs "
            "the ~3.85 implied; 0.188% in V̂ -> 9.06% in Φ_q (48×). scope-(a). "
            "bean qou-0gqn.",
        "audit_only": True,
        "tier": "measured (numerical conditioning)",
        "q0Anchor": "proton",
        "result": {
            "q": mp.nstr(q, 20),
            "cap": mp.nstr(cap, 20),
            "proton_V_hat": [mp.nstr(x, 20) for x in V],
            "max_V_over_q": mp.nstr(v_max / q, 12),
            "cap_fires": bool(v_max >= cap),
            "phi_q_total_float64_as_production_computes": f"{tot_prod:.12g}",
            "e0_now": f"{938.272 / tot_prod:.12g}",
            "e0_june_committed": mp.nstr(JUNE_E0_FULL, 16),
            "e0_june_adjacent_committed": mp.nstr(JUNE_E0_ADJACENT, 16),
            "relative_error_amplification": mp.nstr(amp, 10),
            "subcap_band_ratio": mp.nstr(band_hi / band_lo, 10),
            "tower_term_e0": mp.nstr(e0_tt, 16),
            "v_hat_needed_to_reproduce_june": mp.nstr(lo_b, 16),
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-0gqn",
            "excluded_causes": [
                "8cf5569648 term split — the calibration is deliberately "
                "pinned to term='phi_q', the historical form",
                "_E0_PI_CACHE / _E0_TOWER_CACHE — both keyed by pair_mode",
                "full vs adjacent now identical — correct, A=1 has no pairs",
            ],
            "not_established": [
                "which set of numbers is right",
                "that the tower formula is wrong",
                "which commit moved V̂ (bisect not done)",
            ],
        },
        "assertions": assertions,
        "allPassed": all_passed,
    }
    out = _HERE / "tower-e0-pole-conditioning.witness.json"
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    w.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        w, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(w, indent=2, default=str) + "\n")
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
