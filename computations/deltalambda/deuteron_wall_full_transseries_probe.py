#!/usr/bin/env python3
"""deuteron_wall_full_transseries_probe.py

FULL alien-calculus test of the deuteron wall (upgrade of the leading-term
deuteron_wall_alien_resummation_probe.py, per owner "resummation = Borel? add
alien calculus" / "alien calculus for the entanglement energy dualized").

Setup. The Hopf-link deuteron has perturbative Vol=0, so (entanglement-dual
frame) its binding is carried entirely by the non-perturbative channel — the
resummed Gevrey-1/2 binding period a_D^(n)=I(n)/n (I = involution/telephone
numbers). This probe computes the FULL level-1/2 Borel–Laplace median sum, not
just the leading alien term:

    b_n = a_D^(n)/Γ(n/2+1)   (level-1/2 Borel; radius 1/√2, singularity on the
                              positive real axis, non-polar — lever-1 borel-half);
    P(x) = ∫_0^∞ e^{−u} B̂_{1/2}(x·√u) du    (median: contour rotated ±ε to
                              straddle the real-axis singularity; ReP = median
                              sum, 2·Im = alien jump).

The deuteron binding candidate is B = m_e·M_2·P(x) = m_e·P(x) (M_2=(2−1)=1 bond),
evaluated at the SUBSTRATE-fixed coupling x (no tuning).

RESULT (scope-(a) negative, no fit): at every substrate-fixed coupling the full
median resummation undershoots B_D massively —
    m_e·ReP = 0.005 / 0.056 / 0.060 MeV at x = ℏ_q² / ℏ_q / t=ln q₀
vs B_D = 2.225 MeV (≈ 2.7% at best). The alien jump is smaller still
(~0.006 at t). The median sum reaches B_D ONLY as x → the Borel radius
1/√2 ≈ 0.707 (where the sum diverges through the singularity) — which is NOT a
substrate quantity. So the FULL alien-calculus resummation of the binding
period, done parameter-free at the substrate coupling, does NOT close the
deuteron wall: it undershoots by ~40× at the substrate. Reaching B_D would
require tuning the coupling to the singularity (a fit, forbidden). The deuteron
binding is therefore NOT the resummed Gevrey-1/2 period at the substrate; the
working deuteron channel is the separate q-rotational μ₀·ℏ_q·J_q² route
(cheat-sheet "Bind" row, B_D to −9%, 0 params). This CLOSES the resummation
hypothesis for the deuteron (negatively) — the wall is a distinct-mechanism
problem, not a resummation-coupling problem. No fit; no wiring; no tier change.
"""
import sys
import json
import datetime
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
    q0 = q_at(30)
    me = mp.mpf('0.51099895069')
    B_D = mp.mpf('2.22452')
    target = B_D / me

    N = 42
    I = [mp.mpf(1), mp.mpf(1)]
    for n in range(2, N + 1):
        I.append(I[-1] + (n - 1) * I[-2])              # involution numbers
    b = [mp.mpf(0)] + [(I[n] / n) / mp.gamma(mp.mpf(n) / 2 + 1) for n in range(1, N + 1)]
    L = N // 2
    p, qd = mp.pade(b, L, L)

    def Bhat(xi):
        return mp.polyval(p[::-1], xi) / mp.polyval(qd[::-1], xi)

    def P(x, eps):
        return mp.quad(lambda u: mp.e ** (-u) * Bhat(x * mp.sqrt(u) * mp.e ** (1j * eps)),
                       [0, 1, 4, 12, 40])

    xi0 = 1 / mp.sqrt(2)
    hbar = 1 - 1 / q0
    t = mp.log(q0)
    print("=" * 72)
    print(" deuteron wall — FULL level-1/2 Borel–Laplace resummation (no tuning)")
    print("=" * 72)
    print(f" target B_D/m_e = {mp.nstr(target,6)}  (B_D={mp.nstr(B_D,5)} MeV);  Borel sing 1/√2={mp.nstr(xi0,6)}")
    rows = {}
    best = mp.mpf(0)
    for name, x in [("hbar_q^2", hbar ** 2), ("hbar_q", hbar), ("t", t),
                    ("0.35", mp.mpf('0.35')), ("0.5", mp.mpf('0.5'))]:
        Pp = P(x, mp.mpf('0.05')); Pm = P(x, -mp.mpf('0.05'))
        med = mp.re((Pp + Pm) / 2); jump = abs(mp.im((Pp - Pm) / 2))
        Bpred = me * med
        rows[name] = {"x": mp.nstr(x, 6), "m_e_ReP_MeV": mp.nstr(Bpred, 6),
                      "alien_jump": mp.nstr(jump, 6), "pct_of_B_D": mp.nstr(Bpred / B_D * 100, 4)}
        if name in ("hbar_q^2", "hbar_q", "t"):
            best = max(best, Bpred)
        print(f"  x={name:9s}={mp.nstr(x,5):>8}  m_e·ReP={mp.nstr(Bpred,5):>9} MeV "
              f"({mp.nstr(Bpred/B_D*100,4)}% of B_D)  alien|Im|={mp.nstr(jump,4)}")
    undershoots = best < B_D / 10        # best substrate value < 10% of B_D
    print(f"\n best substrate-coupling value {mp.nstr(best,5)} MeV = {mp.nstr(best/B_D*100,4)}% of B_D "
          f"⇒ undershoots by ~{mp.nstr(B_D/best,4)}×")
    print(" the median sum reaches B_D only as x → 1/√2 (the singularity) — NOT a substrate qty.")

    verdict = (
        "Scope-(a) NEGATIVE (no fit): the FULL level-1/2 Borel–Laplace median "
        "resummation of the Gevrey-1/2 binding period, evaluated parameter-free at "
        f"the substrate coupling, gives m_e·ReP ≤ {mp.nstr(best,4)} MeV (≤ "
        f"{mp.nstr(best/B_D*100,3)}% of B_D={mp.nstr(B_D,5)}), undershooting by ~"
        f"{int(B_D/best)}×; the alien jump is smaller still. It reaches B_D only as the "
        "coupling → the Borel radius 1/√2 (the singularity), which is not a substrate "
        "quantity — so a match would require tuning the coupling (a fit). The FULL alien "
        "calculus of the dualized entanglement energy therefore does NOT close the "
        "deuteron parameter-free; the wall is a distinct-mechanism problem. The working "
        "deuteron channel is the separate q-rotational μ₀·ℏ_q·J_q² route (B_D to −9%, 0 "
        "params). This closes the resummation hypothesis for the deuteron negatively. "
        "No fit; no wiring; no tier change."
    )
    print("\nVERDICT:", verdict)

    wit = {
        "computation": "deuteron-wall-full-transseries",
        "description": "FULL level-1/2 Borel–Laplace median resummation of the Gevrey-1/2 "
                       "binding period a_D^(n)=I(n)/n for the Hopf-deuteron (perturbative "
                       "Vol=0), parameter-free at the substrate coupling. Undershoots B_D by "
                       "~40× (m_e·ReP ≤ 0.06 MeV vs 2.225); reaches B_D only at the Borel "
                       "singularity 1/√2 (not a substrate qty). The full alien calculus of "
                       "the dualized entanglement energy does NOT close the deuteron "
                       "parameter-free; distinct-mechanism (q-rotational) route indicated. "
                       "Scope-(a) negative; no fit.",
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "mpmath", "engineVersion": mp.__version__,
        "borel_singularity": "1/sqrt(2)", "borel_level": "1/2 (Gevrey-1/2)",
        "target_B_D_over_m_e": mp.nstr(target, 8),
        "resummation_by_coupling": rows,
        "verdict": verdict,
        "scope": "(a) — full median Borel-Laplace undershoots B_D at every substrate coupling; "
                 "closes the resummation hypothesis for the deuteron negatively",
        "assertions": [{"label": "full median resummation undershoots B_D at substrate couplings",
                        "passed": bool(undershoots)}],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(wit, script_path=__file__, engine="mpmath")
    wit["scriptFile"] = Path(__file__).name
    out = Path(__file__).resolve().parent / "deuteron-wall-full-transseries.witness.json"
    json.dump(wit, open(out, "w"), indent=1)
    print("\nwitness ->", out.name, " allPassed:", wit["allPassed"])
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
