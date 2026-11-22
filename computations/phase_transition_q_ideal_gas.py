#!/usr/bin/env python3
"""
Numerical scan of boiling and freezing temperatures from the q-deformed equation of state.

Follows the user directive to use strictly:
P_q V_q = n_q R T  => T_boil = S_q^(∂) / (n_q R)
with n_q = [2]_q for boiling (gas phase exploring S^2)
and n_q = [2]_q [n_K]_q for freezing.

NO fitted scales are used to force the temperatures to 373 K / 273 K.
The gap is reported honestly, and marked tier=open.
"""

from __future__ import annotations
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE / "substrate"))
import _path_bridge  # noqa: F401
from mpmath import mp  # noqa: E402
from _precision import fmt as _fmt, set_compute_dps  # noqa: E402
set_compute_dps()

try:
    from qou_substrate.constants import q_at
    Q0 = q_at()
    # EXCISED: was Q0 = float(q_at()). q_at() ALREADY returns mpf at 50 dps, so
    # the cast was a pure downgrade to 53 bits -- a NO-FLOAT64 violation with
    # nothing bought: mpf supports every arithmetic operator this file uses.
except Exception as _exc:  # pragma: no cover - fail loudly, never substitute
        # Was: Q0 = 1.1099780333553254 — a value that is NEITHER pin, sitting
        # 506 ppb from muon and 495 ppb from proton, i.e. ~44x the ~11.5 ppb
        # mu-p substrate tension the two-layer discipline exists to manage. It
        # was substituted silently on any import hiccup, so a bare container
        # produced numbers that looked fine and were wrong by 44 tensions.
        # AGENTS.md q0-anchor: never straddle the two layers inside one quantity;
        # q0_cross_layer_fallback_scan.py: "fail loudly" rather than substitute.
        raise RuntimeError(
            "q_at() unavailable and there is no safe fallback: this producer "
            "must compute at a declared pin, not at a hardcoded approximation. "
            "Install/point at qou-substrate rather than substituting a literal."
        ) from _exc

try:
    from qou_substrate.witness import WitnessBuilder
except Exception:
    from witness_base import WitnessBuilder

# Constants
R_gas = mp.mpf("8.314462618")  # J / (mol K), exact SI molar gas constant R = N_A * k_B
h = Q0 - 1 / Q0
h2 = h * h
dim_q = Q0 + 1 / Q0  # [2]_q

# Molecule Data: (E_cov kJ/mol, n_HB, n_K, T_boil_obs K, T_melt_obs K)
#
# Carried as mpf from decimal STRINGS, not float literals. These are exact
# tabulated values (373.15 K is a definition, not a measurement with a binary64
# tail), and writing them as `373.15` put six raw float64 into the witness and
# then propagated into every ratio computed from them.
MOLECULES = {
    "H2O": (mp.mpf("460.0"), 2, 6, mp.mpf("373.15"), mp.mpf("273.15")),
    "HF":  (mp.mpf("565.0"), 1, 3, mp.mpf("293.15"), mp.mpf("189.6")),
    "NH3": (mp.mpf("391.0"), 1, 3, mp.mpf("239.81"), mp.mpf("195.4"))
}

def q_integer(n: int, q: mp.mpf) -> mp.mpf:
    return (q**n - q**(-n)) / (q - 1/q)

def main() -> int:
    w = WitnessBuilder("phase-transition-q-ideal-gas", engine="python")
    
    print("=" * 80)
    print("Boiling/Freezing Temperature Scan via q-Equation of State (NO FIT)")
    print("=" * 80)
    
    # Collected so the "~6-10x" claim below can be checked against the run
    # rather than asserted as a constant (bean `qou-26f2`).
    boil_ratios: dict[str, "mp.mpf"] = {}

    for name, (e_cov, n_hb, n_k, t_boil_obs, t_melt_obs) in MOLECULES.items():
        print(f"[{name}]")

        # 1. Cohesion Energy S_q^(∂)
        S_q_boundary = n_hb * h2 * e_cov * 1000  # J/mol
        
        # 2. Boiling Point (Gas -> Liquid)
        t_boil_pred = S_q_boundary / (dim_q * R_gas)
        boil_ratio = t_boil_pred / t_boil_obs
        
        # 3. Melting Point (Liquid -> Solid)
        n_k_q = q_integer(n_k, Q0)
        t_melt_pred = S_q_boundary / (dim_q * n_k_q * R_gas)
        melt_ratio = t_melt_pred / t_melt_obs
        
        w.add_data(f"{name}_T_boil_pred", _fmt(t_boil_pred))
        w.add_data(f"{name}_T_boil_obs", _fmt(t_boil_obs))
        w.add_data(f"{name}_boil_ratio", _fmt(boil_ratio))
        boil_ratios[name] = boil_ratio
        w.add_data(f"{name}_T_melt_pred", _fmt(t_melt_pred))
        w.add_data(f"{name}_T_melt_obs", _fmt(t_melt_obs))
        w.add_data(f"{name}_melt_ratio", _fmt(melt_ratio))
        
        print(f"  T_boil(pred) = {float(t_boil_pred):.1f} K | obs = {float(t_boil_obs):.1f} K | gap ratio = {float(boil_ratio):.2f}x")  # float64-ok: stdout display only
        print(f"  T_melt(pred) = {float(t_melt_pred):.1f} K | obs = {float(t_melt_obs):.1f} K | gap ratio = {float(melt_ratio):.2f}x")  # float64-ok: stdout display only
        print()

    print("CONCLUSION: The strict geometric mapping P_q V_q = n_q R T over-predicts temperatures.")
    print("The empirical 'entropy of vaporization' involves a missing topological factor beyond the simple [2]_q.")
    
    _over = {n: r for n, r in boil_ratios.items() if r > 1}
    w.add_data("boil_ratios", {n: _fmt(r) for n, r in boil_ratios.items()})
    w.add_data("boil_ratio_range", {"min": _fmt(min(boil_ratios.values())),
                                    "max": _fmt(max(boil_ratios.values())),
                                    "previously_claimed_band": "6-10x (wrong when written; see bean qou-3hre)",
                                    "matches_claimed_band": False})
    w.add_assertion(
        "Direct substitution of [2]_q over-predicts T_boil for every material",
        computed=str(len(_over)), expected=str(len(boil_ratios)), tolerance="0",
        source=f"T_boil_pred = S_q / ([2]_q R) misses high everywhere: "
               f"{', '.join(f'{n} {float(r):.2f}x' for n, r in boil_ratios.items())} "  # float64-ok: source prose formatting only
               f"(range {float(min(boil_ratios.values())):.2f}-"  # float64-ok: source prose formatting only
               f"{float(max(boil_ratios.values())):.2f}x, NOT the 6-10x the previous "  # float64-ok: source prose formatting only
               f"assertion name claimed — see bean qou-3hre)"
    )
    
    w.set_description(
        "Attempts to derive absolute boiling and freezing temperatures strictly from "
        "the q-ideal gas law (q-PV = nRT) without fitted scaling factors. Computes the "
        "cohesion energy from the h²-suppressed H-bond network, then sets T_boil = S_q / (n_q R). "
        "With the naive choice n_q = [2]_q (the dimension of the Hopf base exploring S²), "
        "this over-predicts T_boil by a factor of 4.26x to 6.45x (H2O 6.45, HF 5.04, "
        "NH3 4.26) and T_melt by 1.38x to 2.56x. This demonstrates that "
        "the true entropy of vaporisation ΔS_vap requires a more sophisticated topological "
        "partition function (likely involving the full Reeb flow phase space) rather than just "
        "the bare dimension [2]_q. Result is recorded honestly as open."
    )
    w.add_data("tier", "open")
    # The band in this string, and in `set_description` above, previously read
    # "6-10x" and never matched what this script computes (bean `qou-3hre`).
    # The constant assertion that stood where `boil_ratio_range` now sits was
    # why: `computed=True, expected=True` could not contradict a prose figure.
    #
    # Ruled out before correcting it, because "the model drifted" and "the band
    # is wrong" want opposite fixes:
    #   * q₀ — the excised literal 1.1099780333553254 (removed for sitting
    #     ~495 ppb off either pin) gives 4.26-6.44x, against 4.26-6.45x at
    #     today's `q_at()`. A 495 ppb shift moves these ratios by 0.01x.
    #   * inputs — `MOLECULES` and the cohesion formula were introduced once
    #     and have never been modified; the only later commits are the float64
    #     excision, the q₀ fallback hardening, and the qou-26f2 drain.
    # So the model has not moved. The band was wrong when it was written, and
    # this is a description corrected to match an unchanged computation — not
    # a model adjusted to match an observation.
    w.add_data("finding", "The bare mapping P_q V_q = [2]_q R T over-predicts T_boil by 4.26-6.45x (H2O 6.45, HF 5.04, NH3 4.26) and T_melt by 1.38-2.56x. A derived topological factor for ΔS_vap is required. No fit applied. Status remains OPEN.")
    
    w.save({"q0Anchor": "proton", "q0Value": _fmt(Q0)})
    print("Saved witness: phase-transition-q-ideal-gas.witness.json")
    return 0


def _selftest() -> int:
    assert isinstance(Q0, mp.mpf) and isinstance(R_gas, mp.mpf)
    assert abs(q_integer(2, Q0) - dim_q) < mp.mpf("1e-60")
    print("self-test: ok (Q0 and R_gas are mpf, q_integer(2, Q0) == [2]_q)")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:] or "--selftest" in sys.argv[1:]:
        raise SystemExit(_selftest())
    raise SystemExit(main())
