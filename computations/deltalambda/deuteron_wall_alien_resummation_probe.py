#!/usr/bin/env python3
"""deuteron_wall_alien_resummation_probe.py

Test the parameter-free deuteron-wall closure (leading alien term undershoots;
full alien-calculus trans-series OPEN)
proposed in docs/audits/2026-07-13-last-5-days-machinery-for-mass-binding.md.

Setup. The bond-count route derives A≥3 binding zero-fit but leaves the deuteron
wall: its 2-body sub-link is the Hopf link with Vol=0, so the perturbative
even/Vol binding vanishes while B_D = 2.225 MeV ≠ 0. The proposal: the deuteron
binding is the non-perturbative (alien) contribution of the Gevrey-1/2 binding
period at the level-1/2 Borel singularity ξ=1/√2, using only PROVED structure:
  - action ω₀ = 1/√2 (level-1/2 Borel singularity, lever-1 borel-half probe);
  - Stokes constant A_ω = 4√2·e^{−3/8} (Bridge datum, c7fdd8ae);
  - scale m_e (CAL-1); coupling x substrate-fixed (NO tuning).

SCOPE (corrected 2026-07-13 — "resummation = Borel LEADING term, not full alien
calculus"): this probe tests only the single LEADING alien sector
ΔP = A_ω·exp(−ω₀/√x) (the m=1 Borel–Laplace term). Since exp(−ω₀/√x) < 1 for
every x>0, that single term is bounded, m_e·A_ω = 1.987 MeV, which is BELOW
B_D = 2.225 MeV at the substrate coupling (~0.21 MeV, ~10%). So the LEADING
alien term alone undershoots.

This is NOT a refutation of the resummation route (scope-(a), not (b)). The
FULL alien-calculus content is the whole trans-series over all sectors,
    B_D = m_e·Σ_{m≥1} S_m · A_ω^m · e^{−m ω₀/√x} · Φ_m(x)   (bridge equation),
whose Stokes constants S_m and per-sector fluctuations Φ_m this probe does NOT
compute. As x→∞ every sector → its constant, so Σ_m S_m A_ω^m is NOT bounded by
A_ω — the leading-term ceiling says nothing about the full sum. The full
alien-calculus resummation (the median/Écalle sum with the derived level-1/2
datum A_ω = 4√2 e^{−3/8}, ω₀ = 1/√2) remains OPEN and could reach B_D.

PHYSICAL FRAME (owner, 2026-07-13): read B_D as the **entanglement energy** of
the two-nucleon sub-braid bipartition; the perturbative (Vol) face vanishes for
the Hopf deuteron, so the binding is carried entirely by the **dual** channel,
where the alien calculus lives — the non-perturbative trans-series IS the
dualized entanglement energy. The next step is to compute S_m/Φ_m for the
bipartition dual, not to stop at the m=1 ceiling.

RESULT (scope-(a)): the LEADING level-1/2 alien term undershoots B_D (ceiling
1.987 MeV; ~0.21 MeV at the substrate coupling). The full alien-calculus
trans-series of the dualized entanglement energy is OPEN, not excluded. No fit;
no wiring; no tier change.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "qou-substrate" / "python"))
import mpmath as mp  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def main() -> int:
    q0 = q_at(40)
    me = mp.mpf('0.51099895069')
    B_D = mp.mpf('2.22452')
    target = B_D / me
    omega0 = 1 / mp.sqrt(2)                                  # proved
    A_omega = 4 * mp.sqrt(2) * mp.e ** (mp.mpf(-3) / 8)      # derived Stokes constant
    ceiling = me * A_omega                                   # x -> inf limit

    print("=" * 70)
    print(" deuteron-wall alien resummation — parameter-free test (no tuning)")
    print("=" * 70)
    print(f" target B_D = {mp.nstr(B_D,6)} MeV  (B_D/m_e = {mp.nstr(target,6)})")
    print(f" DERIVED: ω₀=1/√2={mp.nstr(omega0,6)}  A_ω=4√2 e^-3/8={mp.nstr(A_omega,6)}")
    print(f" hard ceiling m_e·A_ω = {mp.nstr(ceiling,6)} MeV  (leading alien term, x→∞)")

    hbar = 1 - 1 / q0
    t = mp.log(q0)
    rows = {}
    print("\n leading alien term m_e·A_ω·exp(-ω₀/√x) at substrate-fixed couplings:")
    for name, x in [("hbar_q^2", hbar ** 2), ("hbar_q", hbar), ("t=ln q0", t)]:
        val = me * A_omega * mp.e ** (-omega0 / mp.sqrt(abs(x)))
        rows[name] = mp.nstr(val, 8)
        print(f"   x={name:10s}={mp.nstr(x,5):>9}  m_e·ΔP={mp.nstr(val,5)} MeV "
              f"({mp.nstr(val/B_D*100,4)}% of B_D)")

    ceiling_below = ceiling < B_D
    print(f"\n ceiling {mp.nstr(ceiling,6)} MeV < B_D {mp.nstr(B_D,6)} MeV : {ceiling_below}")
    print(" ⇒ the leading level-1/2 alien term CANNOT reach B_D for any coupling.")
    print(" ⇒ parameter-free single-alien resummation does NOT close the deuteron wall.")

    verdict = (
        "Scope-(a), LEADING-TERM ONLY (not a refutation of the route): the single m=1 "
        f"level-1/2 alien term (derived ω₀=1/√2, A_ω=4√2 e^-3/8, scale m_e) has ceiling "
        f"m_e·A_ω={mp.nstr(ceiling,5)} MeV < B_D={mp.nstr(B_D,5)} MeV and gives ~0.21 MeV "
        "at the substrate coupling, so the leading alien term alone UNDERSHOOTS. The FULL "
        "alien-calculus trans-series Σ_m S_m A_ω^m e^{-mω₀/√x} Φ_m (bridge equation) is NOT "
        "bounded by A_ω and is OPEN — the leading ceiling does not exclude it. Physical "
        "frame: B_D is the dualized entanglement energy of the 2-nucleon bipartition, "
        "carried by the dual channel where the alien calculus lives; the perturbative Vol "
        "face is 0 (Hopf). Next: compute S_m/Φ_m for the bipartition dual. No fit; no wiring."
    )
    print("\nVERDICT:", verdict)

    import json
    import datetime
    wit = {
        "computation": "deuteron-wall-alien-resummation",
        "description": "LEADING-term test of the deuteron-wall closure via the m=1 level-1/2 "
                       "alien term of the Gevrey-1/2 binding period (derived ω₀=1/√2, "
                       "A_ω=4√2 e^-3/8, scale m_e, no tuning): ceiling m_e·A_ω=1.987 MeV < "
                       "B_D=2.225 MeV, so the LEADING term undershoots (~0.21 MeV at substrate). "
                       "NOT a refutation: the full alien-calculus trans-series Σ_m S_m A_ω^m "
                       "e^{-mω₀/√x} Φ_m (dualized entanglement energy of the 2-nucleon "
                       "bipartition) is unbounded by A_ω and OPEN. Scope-(a); no fit.",
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "mpmath", "engineVersion": mp.__version__,
        "derived_constants": {"omega0": "1/sqrt(2)", "A_omega": "4*sqrt(2)*e^(-3/8)",
                              "A_omega_num": mp.nstr(A_omega, 12)},
        "ceiling_m_e_A_omega_MeV": mp.nstr(ceiling, 10),
        "B_D_MeV": mp.nstr(B_D, 8),
        "leading_alien_at_substrate_couplings_MeV": rows,
        "verdict": verdict,
        "scope": "(a) — leading m=1 alien term undershoots; full alien-calculus trans-series (dualized entanglement energy) open",
        "assertions": [{"label": "leading m=1 alien term ceiling m_e*A_omega < B_D (leading term undershoots; full trans-series open)",
                        "passed": bool(ceiling_below)}],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(wit, script_path=__file__, engine="mpmath")
    wit["scriptFile"] = Path(__file__).name
    out = Path(__file__).resolve().parent / "deuteron-wall-alien-resummation.witness.json"
    json.dump(wit, open(out, "w"), indent=1)
    print("\nwitness ->", out.name, " allPassed:", wit["allPassed"])
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
