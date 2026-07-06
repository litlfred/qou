"""T2 (empirical step): Pentagon archimedean refinement → Borromean h⁴ = −3/4.

The claim (from
`docs/audits/2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md`):
the h⁴ = −3/4 coefficient of the Borromean Markov-trace closed form
should be derivable from the **post-τ Pentagon** (q-Rogers archimedean
refinement) via a specific (u, v) specialization for the Borromean
braid β = (σ₁⁻¹σ₂)³.

The post-τ Pentagon (per q-rogers-pentagon-archimedean.md):

    Li₂^q(u) + Li₂^q(v) − Li₂^q(uv) − Li₂^q(α) − Li₂^q(β)
    = log_q((1−u)/(1−uv)) · log_q((1−v)/(1−uv)) + O((q−1)²)

where α = u(1−v)/(1−uv), β = v(1−u)/(1−uv).

This script:

1. Expands the LHS (Pentagon residual) for fixed (u, v) as a power
   series in h = q − q⁻¹ around q = 1.
2. Reports the h⁴ coefficient.
3. Tests several natural Borromean specializations to see which
   match the empirical −3/4 from the Markov trace closed form.

Specializations tested:
  (u, v) = (1/2, 1/2)         — pentagon diagonal
  (u, v) = (1/3, 1/3)         — symmetric, smaller
  (u, v) = (z_markov, z_markov) — Markov parameter z = 1/(q^{1/2}+q^{-1/2})
  (u, v) = (h², h²)            — substrate-natural at h_0
  (u, v) = (1/q_0, 1/q_0)      — substrate-q⁻¹
  (u, v) = (h²/2, h²/2)        — half-substrate

Status: EXPLORATORY. If a specialization matches the structural
−3/4 to better than 1%, it identifies the Borromean (u, v) for
the categorical Pentagon → h⁴ derivation. Otherwise, the
specialization is open and the Pentagon → −3/4 chain needs deeper
analysis.

Per AGENTS.md three-calibration discipline: this probe does not
propose production wiring.
"""


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpf

mp.mp.dps = 50

Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
H_0 = Q_0 - mpf(1) / Q_0
H4_BORROMEAN_TARGET = mpf("-3") / 4  # from closed-form Markov trace


def h_of_q(q: mpf) -> mpf:
    return q - mpf(1) / q


def li2_q(z: mpf, q: mpf, n_terms: int = 80) -> mpf:
    """The q-dilogarithm Li_2^q(z) = Σ_{n≥1} z^n / (n · [n]_q)
    where [n]_q = (q^n − q^{-n}) / (q − q⁻¹).

    Converges for |z| < min(|q|, |q|⁻¹). For q ≈ 1.11 and small z,
    n_terms = 80 is plenty.
    """
    if abs(z) >= 1:
        # Outside convergence — return NaN-like sentinel
        return mp.nan
    h = q - mpf(1) / q
    if abs(h) < mpf("1e-30"):
        # Classical limit: Li_2^q → Li_2 (Spence's function)
        return mp.polylog(2, z)
    result = mpf(0)
    for n in range(1, n_terms + 1):
        bracket_n = (q ** n - q ** (-n)) / h
        term = z ** n / (n * bracket_n)
        result += term
    return result


def log_q(x: mpf, q: mpf) -> mpf:
    """q-logarithm: log_q(x) = (1 − x^{-1}) / (q − q⁻¹) · [bracket].

    Standard convention: log_q(x) such that log_q(x) → log(x) as q → 1.
    Use: log_q(x) = log(x) / log_q(e)  scaled appropriately.
    Simplest mpmath-friendly form: log_q(x) = (x − 1) / (q − 1)
    for x near 1 (linear approximation; exact would be a q-series).

    For empirical purposes we use the natural log (q-log → log as q→1).
    """
    # We use natural log as the leading-order q-log
    return mp.log(x)


def rogers_alpha(u: mpf, v: mpf) -> mpf:
    return u * (1 - v) / (1 - u * v)


def rogers_beta(u: mpf, v: mpf) -> mpf:
    return v * (1 - u) / (1 - u * v)


def pentagon_lhs(u: mpf, v: mpf, q: mpf) -> mpf:
    """Li₂^q(u) + Li₂^q(v) − Li₂^q(uv) − Li₂^q(α) − Li₂^q(β)."""
    a = rogers_alpha(u, v)
    b = rogers_beta(u, v)
    return (li2_q(u, q) + li2_q(v, q) - li2_q(u * v, q)
            - li2_q(a, q) - li2_q(b, q))


def pentagon_rhs_classical_log_term(u: mpf, v: mpf) -> mpf:
    """log((1-u)/(1-uv)) · log((1-v)/(1-uv)) — the classical
    Rogers correction term (q-independent leading order)."""
    arg1 = (1 - u) / (1 - u * v)
    arg2 = (1 - v) / (1 - u * v)
    return mp.log(arg1) * mp.log(arg2)


def pentagon_residual_h_expansion(u: mpf, v: mpf, n_h_samples: int = 5) -> dict:
    """Expand the Pentagon-LHS minus classical log² correction
    as a power series in h = q − q⁻¹ near q = 1, by sampling at
    multiple small h values and fitting a polynomial.
    """
    log2_classical = pentagon_rhs_classical_log_term(u, v)
    samples = []
    h_values = [mpf("0.01") * (k + 1) for k in range(n_h_samples)]
    for h_val in h_values:
        # Convert h to q: h = q − q⁻¹ ⟹ q² − h·q − 1 = 0
        # q = (h + sqrt(h² + 4)) / 2 (positive root)
        q_val = (h_val + mp.sqrt(h_val ** 2 + 4)) / 2
        lhs = pentagon_lhs(u, v, q_val)
        residual = lhs - log2_classical
        samples.append((h_val, residual))

    # Fit residual ≈ c_2 · h² + c_4 · h⁴ + c_6 · h⁶ via least-squares
    # Build matrix [h², h⁴, h⁶] and solve
    n = len(samples)
    h_powers = mp.matrix(n, 3)
    rhs_vec = mp.matrix(n, 1)
    for i, (h_val, res) in enumerate(samples):
        h_powers[i, 0] = h_val ** 2
        h_powers[i, 1] = h_val ** 4
        h_powers[i, 2] = h_val ** 6
        rhs_vec[i, 0] = res

    # Solve normal equations: (H^T H) c = H^T rhs
    HT = h_powers.T
    HTH = HT * h_powers
    HTrhs = HT * rhs_vec
    try:
        coeffs = mp.lu_solve(HTH, HTrhs)
        c2, c4, c6 = coeffs[0, 0], coeffs[1, 0], coeffs[2, 0]
    except Exception as e:
        c2, c4, c6 = mp.nan, mp.nan, mp.nan

    return {
        "samples": [(float(h), float(r)) for h, r in samples],
        "c2": float(c2),
        "c4": float(c4),
        "c6": float(c6),
        "classical_log_term": float(log2_classical),
    }


def test_specialization(name: str, u: mpf, v: mpf) -> dict:
    """Test one (u, v) specialization for the Pentagon residual h⁴."""
    a = rogers_alpha(u, v)
    b = rogers_beta(u, v)
    uv = u * v

    # Check convergence: need |u|, |v|, |uv|, |α|, |β| all < 1
    bounds = [abs(u), abs(v), abs(uv), abs(a), abs(b)]
    if max(bounds) >= 1:
        return {
            "name": name,
            "u": float(u),
            "v": float(v),
            "converges": False,
            "max_arg_abs": float(max(bounds)),
            "result": None,
        }

    exp = pentagon_residual_h_expansion(u, v)
    c4 = mpf(exp["c4"])
    target = H4_BORROMEAN_TARGET
    diff = c4 - target
    rel_diff = abs(diff) / abs(target) if target != 0 else abs(diff)

    return {
        "name": name,
        "u": float(u),
        "v": float(v),
        "alpha": float(a),
        "beta": float(b),
        "uv": float(uv),
        "max_arg_abs": float(max(bounds)),
        "converges": True,
        "h_expansion": exp,
        "c4_residual": float(c4),
        "target_h4_borromean": float(target),
        "absolute_difference": float(diff),
        "relative_difference_pct": float(rel_diff * 100),
        "matches_borromean_target_within_1pct": bool(rel_diff < mpf("0.01")),
    }


def main() -> None:
    print("T2 empirical: Pentagon archimedean → Borromean h⁴ = −3/4")
    print(f"50-dps mpmath; Q_0 = {Q_0}; h_0 = {float(H_0):.6f}")
    print(f"Target: h⁴ coefficient of Borromean Markov trace = -3/4 = {float(H4_BORROMEAN_TARGET):.6f}")
    print("=" * 60)

    z_markov = mpf(1) / (mp.sqrt(Q_0) + mpf(1) / mp.sqrt(Q_0))

    specializations = [
        ("diagonal_1_over_2",       mpf(1) / 2, mpf(1) / 2),
        ("diagonal_1_over_3",       mpf(1) / 3, mpf(1) / 3),
        ("markov_z_diagonal",       z_markov, z_markov),
        ("h_squared",                H_0 ** 2, H_0 ** 2),
        ("substrate_q_inv",          mpf(1) / Q_0, mpf(1) / Q_0),
        ("half_h_squared",           H_0 ** 2 / 2, H_0 ** 2 / 2),
        ("small_uniform_0.1",        mpf("0.1"), mpf("0.1")),
        ("small_uniform_0.2",        mpf("0.2"), mpf("0.2")),
        ("asymmetric_z_h2",          z_markov, H_0 ** 2),
    ]

    results = []
    for name, u, v in specializations:
        r = test_specialization(name, u, v)
        results.append(r)

        if not r["converges"]:
            print(f"\n{name:<30} | (u={float(u):.4f}, v={float(v):.4f})  DIVERGES (max arg={r['max_arg_abs']:.4f})")
            continue

        match = "✓ MATCH" if r["matches_borromean_target_within_1pct"] else ""
        print(f"\n{name:<30} | u={r['u']:.4f}, v={r['v']:.4f}")
        print(f"  α={r['alpha']:.4f}, β={r['beta']:.4f}, uv={r['uv']:.4f}")
        print(f"  c₂ = {r['h_expansion']['c2']:+.4f}, c₄ = {r['c4_residual']:+.4f}, c₆ = {r['h_expansion']['c6']:+.4f}")
        print(f"  vs target −3/4: diff = {r['absolute_difference']:+.4f} ({r['relative_difference_pct']:+.2f}%)  {match}")

    print("\n" + "=" * 60)
    print("VERDICT SUMMARY")
    print("=" * 60)
    matches = [r for r in results if r.get("matches_borromean_target_within_1pct")]
    print(f"Specializations matching Borromean h⁴ = −3/4 within 1%: {len(matches)} of {len(results)}")
    if matches:
        for m in matches:
            print(f"  → {m['name']}: c₄ = {m['c4_residual']:.4f}")
    else:
        print(f"  → None. The Pentagon residual h⁴ at tested (u, v) does not")
        print(f"     match −3/4 within 1% at any standard specialization.")
        print(f"     The Borromean braid's specific (u, v) lifting in the")
        print(f"     q-shuffle Hopf algebra is more intricate than a single")
        print(f"     diagonal pair — likely involves the braid's monodromy")
        print(f"     decomposition. Documenting closer matches as candidates.")

    # Best-match summary
    converging = [r for r in results if r.get("converges")]
    if converging:
        best = min(converging, key=lambda r: abs(r["relative_difference_pct"]))
        print(f"\nClosest match: {best['name']} (c₄ = {best['c4_residual']:.4f}, "
              f"{best['relative_difference_pct']:+.2f}% from target)")

    # Witness
    witness = {
        "compute": "pentagon_to_borromean_h4_probe",
        "description": (
            "Tests whether the post-τ Pentagon archimedean refinement "
            "(Rogers log² correction h² → h⁴ residual) at a natural "
            "Borromean (u, v) specialization gives the empirical "
            "h⁴ = −3/4 coefficient of the Borromean Markov-trace closed "
            "form. Multiple specializations tested; matches indicate "
            "candidates for the categorical Pentagon → h⁴ derivation."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "H_0": str(H_0),
            "target_h4_borromean": str(H4_BORROMEAN_TARGET),
            "li2_q_n_terms": 80,
            "h_expansion_n_samples": 5,
        },
        "specializations": results,
        "summary": {
            "n_specializations_tested": len(results),
            "n_converging": sum(1 for r in results if r.get("converges")),
            "n_matches_within_1pct": len(matches),
            "best_match_name": (
                min((r for r in results if r.get("converges")),
                    key=lambda r: abs(r["relative_difference_pct"]),
                    default={"name": "none"})["name"]
            ),
            "interpretation": (
                "T2 status: partial. Pentagon residual h⁴ extracted "
                "empirically at multiple specializations. If a clean "
                "Borromean specialization matches −3/4, T2 is "
                "computationally complete (Lean formalization queued). "
                "If not, the categorical Pentagon → h⁴ derivation "
                "requires the explicit Borromean q-shuffle lifting, "
                "which is itself an open structural step."
            ),
        },
        "status": "exploratory",
        "tags": [
            "pentagon-archimedean",
            "q-rogers",
            "h4-coefficient",
            "borromean",
            "li2-q",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }

    out_path = Path(__file__).parent / "pentagon-to-borromean-h4-probe.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
