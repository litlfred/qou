"""Habiro-ring cross-validation: tr_M(β_Bor) at root-of-unity vs J_N(Bor).

Per `docs/audits/2026-05-24-rt-route-research-frontiers-w-correction-habiro-heegaard.md`
§5 next-step #1: test whether the Borromean Markov-trace closed form
$\mathrm{tr}_M(\beta_\mathrm{Bor}) = (4+h^2-3h^4-h^6)/(h^2+4)$
(PR #1081) at $q = e^{2\pi i/N}$ matches the colored Jones polynomial
$J_N(\mathcal{B}_3, q)$ at the same q.

If the Habiro-ring unification conjecture holds, the two specializations
should agree (modulo a known normalization). This would directly
empirically test the unification.

Method:
1. Compute tr_M closed form at $q = e^{2\pi i/N}$ for N = 2, 3, 4, 5
2. Compute J_N(B_3, q) — the colored Jones at level N — for same q
3. Compare; report agreement / disagreement

The Borromean rings are NOT a torus knot (they're hyperbolic), so this
test is *cross-chain*: real-q_0 closed form (hyperbolic-derived) vs
root-of-unity colored Jones (RT-derived).

Status: EXPLORATORY.
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpc, mpf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def hpos(q):
    return q - mpf(1) / q


def tr_M_borromean_closed_form(q) -> mpc:
    """Borromean Markov trace closed form (PR #1081):
       tr_M = (4 + h² - 3h⁴ - h⁶) / (h² + 4)
    where h = q - q⁻¹.
    Works for complex q (e.g., root-of-unity)."""
    h = hpos(q)
    h2 = h ** 2
    return (4 + h2 - 3 * h ** 4 - h ** 6) / (h2 + 4)


def main():
    print("Habiro-ring cross-validation: Borromean tr_M closed-form vs root-of-unity")
    print(f"50-dps mpmath. Testing q = exp(2πi/N) for N = 2..8.")
    print("=" * 80)

    N_values = [2, 3, 4, 5, 6, 7, 8]
    results = []
    print(f"\n{'N':<4} {'q = exp(2πi/N)':<20} {'|tr_M|':<14} {'arg(tr_M) [rad]':<18} {'tr_M (complex)':<35}")
    print("-" * 95)

    # Also evaluate at q_0 (real) for comparison — canonical 50-digit pin
    Q_0 = mpf(Q_50_DIGIT_STR)
    tr_at_q0 = tr_M_borromean_closed_form(Q_0)
    print(f"q_0  q_0 ≈ 1.10998        {float(abs(tr_at_q0)):<14.6f} {0.0:<18.6f} {complex(tr_at_q0)}")

    for N in N_values:
        q = mp.exp(mpc(0, 2 * mp.pi / N))
        try:
            tr = tr_M_borromean_closed_form(q)
            print(f"{N:<4} exp(2πi/{N}){'':<10} {float(abs(tr)):<14.6f} {float(mp.arg(tr)):<18.6f} {complex(tr)}")
            results.append({
                "N": N,
                "q_real": float(q.real),
                "q_imag": float(q.imag),
                "tr_M_real": float(tr.real),
                "tr_M_imag": float(tr.imag),
                "tr_M_magnitude": float(abs(tr)),
                "tr_M_arg_radians": float(mp.arg(tr)),
            })
        except Exception as e:
            print(f"{N:<4} exp(2πi/{N})    FAILED: {e}")
            results.append({"N": N, "error": str(e)})

    # Comparison observations
    print("\n" + "=" * 80)
    print("Observations:")
    print("=" * 80)
    print("If Habiro-ring conjecture holds, the values at root-of-unity should")
    print("match the colored Jones J_N(B_3, q) computed via RT TQFT directly.")
    print()
    print("Note: J_N for the Borromean rings has no simple closed form (unlike")
    print("T(2, n) torus links). The Habiro-ring view says the SAME element")
    print("specializes both ways:")
    print("  - tr_M(B_3, q) = (4+h²-3h⁴-h⁶)/(h²+4) at real q (PR #1081 closed form)")
    print("  - J_N(B_3, q = exp(2πi/N)) at root-of-unity q (RT colored Jones)")
    print()
    print("The values reported above are tr_M at root-of-unity, giving the")
    print("Habiro-conjectural J_N values for B_3. Cross-validation against an")
    print("independent J_N(B_3) computation (e.g., via state-sum on the 8-cell")
    print("triangulation of B_3's complement) would settle the conjecture.")
    print()
    print("That cross-validation is research-grade (~1 day for the state-sum")
    print("compute) and queued separately.")

    # Witness
    witness = {
        "compute": "rt_habiro_borromean_cross_validation",
        "description": (
            "Per docs/audits/2026-05-24-rt-route-research-frontiers-"
            "w-correction-habiro-heegaard.md §5#1: tests Borromean "
            "Markov-trace closed form (PR #1081) at q = exp(2πi/N) "
            "for N = 2..8. The values are the Habiro-conjectural "
            "specializations of the Borromean trace element to root-"
            "of-unity. Cross-validation against independent J_N "
            "computation (via state-sum on 8-ideal-octahedra) is "
            "queued as the next research-grade test."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "N_values_tested": N_values,
        },
        "tr_M_at_q0_real": {
            "q": float(Q_0),
            "tr_M": float(tr_at_q0.real if hasattr(tr_at_q0, 'real') else tr_at_q0),
        },
        "tr_M_at_root_of_unity": results,
        "interpretation": (
            "Per Habiro-ring unification conjecture, these values should "
            "match J_N(B_3, q = exp(2πi/N)) computed via RT TQFT. "
            "Confirming match would unify the hyperbolic and RT chains. "
            "The Borromean rings have no simple J_N closed form (unlike "
            "torus links T(2, n)), so the cross-validation requires a "
            "non-trivial state-sum computation on the 8-cell triangulation."
        ),
        "status": "exploratory",
        "tags": [
            "habiro-ring",
            "borromean",
            "root-of-unity",
            "cross-validation",
            "hyperbolic-rt-unification",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    out_path = WitnessBuilder.wrap_legacy(
        "rt-habiro-borromean-cross-validation", witness, script_path=__file__, engine="mpmath",
    ).save()
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
