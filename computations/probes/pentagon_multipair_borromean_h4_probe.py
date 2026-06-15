"""T2b: multi-pair Pentagon-sum for the Borromean braid h⁴ coefficient.

The single-pair Pentagon test (commit 49839f96,
`pentagon_to_borromean_h4_probe.py`) found that no diagonal (u, v)
specialization gives the structural h⁴ = −3/4 of the Borromean
Markov trace. Per the broad-context audit
`docs/audits/2026-05-24-pentagon-identity-broad-context.md` §4(a):

  The actual chain requires:
    - A SUM over multiple Pentagon evaluations (one per pair of
      strands in the 3-strand braid)
    - WITH the braid's specific monodromy weighting

This probe tests several multi-pair summing schemes for the Borromean
braid β_Bor = (σ_1⁻¹σ_2)³ on 3 strands. The 3 strand pairs are
(1,2), (2,3), (1,3); the braid word has 6 generator applications.

Schemes tested:

  (S1) Uniform sum: sum Pentagon residual h⁴ over 3 pairs equally
  (S2) Generator-weighted: weight by generator multiplicity in β
       (σ_1: 3, σ_2: 3, σ_1·σ_2: composite)
  (S3) Cyclic monodromy: weight by braid's monodromy at each pair
  (S4) Strand-distance weighted: 1/d(i,j) (adjacent vs distant)
  (S5) Jones-coefficient weighted: weight by Jones polynomial
       coefficient on each crossing

For each scheme, multiple (u_ij, v_ij) lifts are tested:
  - All diagonal (u_ij, v_ij) = z_markov² (small uniform)
  - All diagonal (u_ij, v_ij) = h² (substrate-natural)
  - Asymmetric (u_12, v_12) = (h_p, h_q) coupling pair indices

If any scheme matches −3/4 within 5%, identifies the Pentagon →
−3/4 lifting. Otherwise documents the negative result as "the
direct categorical Pentagon → −3/4 chain requires more structure
than multi-pair summation."

Per `local/production-vs-exploratory-discipline`: this is EXPLORATORY.
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
from itertools import combinations_with_replacement
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpf

mp.mp.dps = 50

Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
H_0 = Q_0 - mpf(1) / Q_0
H4_TARGET = mpf("-3") / 4

# Strand pairs in B_3 (3-strand braid group)
STRAND_PAIRS = [(1, 2), (2, 3), (1, 3)]


def h_of_q(q: mpf) -> mpf:
    return q - mpf(1) / q


def li2_q(z: mpf, q: mpf, n_terms: int = 60) -> mpf:
    """q-dilogarithm via series."""
    if abs(z) >= 1:
        return mp.nan
    h = q - mpf(1) / q
    if abs(h) < mpf("1e-30"):
        return mp.polylog(2, z)
    result = mpf(0)
    for n in range(1, n_terms + 1):
        bracket_n = (q ** n - q ** (-n)) / h
        result += z ** n / (n * bracket_n)
    return result


def pentagon_residual(u: mpf, v: mpf, q: mpf) -> mpf:
    """Pentagon residual: LHS − classical log² correction.
    LHS = Li_2^q(u) + Li_2^q(v) − Li_2^q(uv) − Li_2^q(α) − Li_2^q(β)
    where α = u(1−v)/(1−uv), β = v(1−u)/(1−uv).
    Classical correction = log((1−u)/(1−uv)) · log((1−v)/(1−uv))
    """
    a = u * (1 - v) / (1 - u * v)
    b = v * (1 - u) / (1 - u * v)
    arg1 = (1 - u) / (1 - u * v)
    arg2 = (1 - v) / (1 - u * v)
    log_term = mp.log(arg1) * mp.log(arg2)
    lhs = (li2_q(u, q) + li2_q(v, q) - li2_q(u * v, q)
           - li2_q(a, q) - li2_q(b, q))
    return lhs - log_term


def extract_h4_coefficient(uv_pairs: list, weights: list) -> mpf:
    """Compute weighted-sum of Pentagon residuals over multiple (u, v)
    pairs, expand in h, extract h⁴ coefficient by least-squares fit."""
    n_samples = 4
    h_values = [mpf("0.005") * (k + 1) for k in range(n_samples)]
    samples = []
    for h_val in h_values:
        q_val = (h_val + mp.sqrt(h_val ** 2 + 4)) / 2
        total = mpf(0)
        for (u, v), w in zip(uv_pairs, weights):
            r = pentagon_residual(u, v, q_val)
            total += w * r
        samples.append((h_val, total))

    # Fit c_2 h² + c_4 h⁴
    H = mp.matrix(n_samples, 2)
    R = mp.matrix(n_samples, 1)
    for i, (h_val, r) in enumerate(samples):
        H[i, 0] = h_val ** 2
        H[i, 1] = h_val ** 4
        R[i, 0] = r
    HT = H.T
    try:
        coeffs = mp.lu_solve(HT * H, HT * R)
        return coeffs[1, 0], samples
    except Exception:
        return mp.nan, samples


def get_pair_uv(scheme_name: str, lift: str) -> dict:
    """For each strand pair (i, j), return (u, v) for the Pentagon eval.
    `lift` = how braid generators lift to q-shuffle variables.
    """
    z_markov = mpf(1) / (mp.sqrt(Q_0) + mpf(1) / mp.sqrt(Q_0))
    if lift == "small_uniform":
        u_val = z_markov ** 2
        return {p: (u_val, u_val) for p in STRAND_PAIRS}
    elif lift == "h_squared":
        u_val = H_0 ** 2
        return {p: (u_val, u_val) for p in STRAND_PAIRS}
    elif lift == "asymmetric_z":
        return {
            (1, 2): (z_markov, z_markov / 2),
            (2, 3): (z_markov / 2, z_markov),
            (1, 3): (z_markov / 3, z_markov / 3),
        }
    elif lift == "h_quartic":
        u_val = H_0 ** 4
        return {p: (u_val, u_val) for p in STRAND_PAIRS}
    else:
        u_val = mpf("0.1")
        return {p: (u_val, u_val) for p in STRAND_PAIRS}


def weighting_scheme(scheme: str) -> dict:
    """Return weighting on STRAND_PAIRS."""
    # Borromean β = (σ_1⁻¹σ_2)³ generator counts: σ_1: 3, σ_2: 3
    # σ_1 acts on pair (1,2); σ_2 on (2,3); virtual (1,3) only via composite
    if scheme == "uniform":
        return {p: mpf(1) for p in STRAND_PAIRS}
    elif scheme == "generator_weighted":
        # σ_1: 3 applications on (1,2); σ_2: 3 applications on (2,3); (1,3) virtual
        return {(1, 2): mpf(3), (2, 3): mpf(3), (1, 3): mpf(0)}
    elif scheme == "cyclic_monodromy":
        # Sum of writhes per pair in Borromean = ±2 alternating
        return {(1, 2): mpf(-3), (2, 3): mpf(3), (1, 3): mpf(0)}
    elif scheme == "strand_distance":
        # 1/d(i,j); (1,2), (2,3) adjacent (d=1); (1,3) distant (d=2)
        return {(1, 2): mpf(1), (2, 3): mpf(1), (1, 3): mpf("0.5")}
    elif scheme == "jones_coefficient":
        # Jones poly V(B_3, t) = ... ; per-strand-pair coefficient
        # heuristic: coefficient sum at each pair's crossing slot
        return {(1, 2): mpf(2), (2, 3): mpf(2), (1, 3): mpf(-1)}
    elif scheme == "borromean_squared_minus_third":
        # 3² for each adjacent pair, -1 for distant (rough cell-count)
        return {(1, 2): mpf(9), (2, 3): mpf(9), (1, 3): mpf(-1)}
    return {p: mpf(1) for p in STRAND_PAIRS}


def main():
    print("T2b: multi-pair Pentagon-sum for Borromean braid h⁴ = -3/4")
    print(f"50-dps mpmath; target h⁴ coefficient = -3/4 = {float(H4_TARGET):.6f}")
    print(f"3 strand pairs of B_3: {STRAND_PAIRS}")
    print("=" * 70)

    lifts = ["small_uniform", "h_squared", "asymmetric_z", "h_quartic"]
    schemes = ["uniform", "generator_weighted", "cyclic_monodromy",
               "strand_distance", "jones_coefficient", "borromean_squared_minus_third"]

    results = []
    matches = []

    for lift in lifts:
        pair_uv = get_pair_uv("", lift)
        # Check convergence
        bad = False
        for p, (u, v) in pair_uv.items():
            if max(abs(u), abs(v), abs(u * v)) >= 1:
                bad = True
        if bad:
            print(f"\nlift={lift}: DIVERGES, skipping")
            continue

        for scheme in schemes:
            weights = weighting_scheme(scheme)
            uv_list = [pair_uv[p] for p in STRAND_PAIRS]
            weight_list = [weights[p] for p in STRAND_PAIRS]

            c_4, samples = extract_h4_coefficient(uv_list, weight_list)
            if mp.isnan(c_4):
                continue

            diff = c_4 - H4_TARGET
            rel_diff = abs(diff) / abs(H4_TARGET) * 100

            r = {
                "lift": lift,
                "scheme": scheme,
                "weights": {str(p): float(w) for p, w in weights.items()},
                "c_4": float(c_4),
                "target": float(H4_TARGET),
                "abs_diff": float(diff),
                "relative_diff_pct": float(rel_diff),
                "matches_within_5pct": bool(rel_diff < 5),
                "matches_within_20pct": bool(rel_diff < 20),
            }
            results.append(r)
            if r["matches_within_5pct"]:
                matches.append(r)

            indicator = ""
            if r["matches_within_5pct"]:
                indicator = "  ✓ MATCH 5%"
            elif r["matches_within_20pct"]:
                indicator = "  ~ close 20%"
            print(f"lift={lift:<18} scheme={scheme:<35} c_4 = {float(c_4):+.4f}  "
                  f"({float(rel_diff):+.2f}%){indicator}")

    print("\n" + "=" * 70)
    print(f"SUMMARY: {len(results)} multi-pair configurations tested")
    print(f"  Matches within 5%:  {len(matches)}")
    print(f"  Matches within 20%: {sum(1 for r in results if r['matches_within_20pct'])}")
    print("=" * 70)

    if matches:
        print("\nMatching configurations (potential Pentagon → -3/4 routes):")
        for m in matches:
            print(f"  lift={m['lift']}, scheme={m['scheme']}")
            print(f"    c_4 = {m['c_4']:+.4f}, diff = {m['abs_diff']:+.4f}")
    else:
        print("\nNo multi-pair sum matches -3/4 within 5%.")
        closest = min(results, key=lambda r: r["relative_diff_pct"]) if results else None
        if closest:
            print(f"\nClosest: lift={closest['lift']}, scheme={closest['scheme']}")
            print(f"  c_4 = {closest['c_4']:+.4f}, {closest['relative_diff_pct']:+.2f}% off")

    # Witness
    witness = {
        "compute": "pentagon_multipair_borromean_h4_probe",
        "description": (
            "T2b: multi-pair Pentagon-sum for the Borromean braid "
            "h⁴ coefficient. Single-pair (T2, commit 49839f96) was "
            "NEGATIVE; this probe tests 6 weighting schemes × 4 "
            "(u,v) lifts (24 configurations). Matches indicate "
            "candidate Pentagon → -3/4 lifting; none indicates the "
            "categorical chain requires deeper machinery."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "H_0": str(H_0),
            "target_h4": str(H4_TARGET),
            "strand_pairs": [list(p) for p in STRAND_PAIRS],
            "lifts_tested": lifts,
            "schemes_tested": schemes,
        },
        "results": results,
        "matches_within_5pct": matches,
        "n_matches_5pct": len(matches),
        "n_matches_20pct": sum(1 for r in results if r["matches_within_20pct"]),
        "summary": {
            "verdict": (
                f"{len(matches)} configurations match within 5%"
                if matches
                else "NEGATIVE: no multi-pair sum matches -3/4 within 5%. "
                     "The categorical Pentagon → -3/4 chain requires more "
                     "structure than 3-pair Pentagon residual summation. "
                     "Candidate next steps: (a) Pachner-coherent state-sum "
                     "via 8 ideal octahedra; (b) Ding-Iohara-Miki master "
                     "Pentagon; (c) Habiro cyclotomic expansion of "
                     "colored Jones J_N(B_3) (see "
                     "docs/audits/2026-05-24-pentagon-identity-broad-context.md "
                     "§4 for the four candidate routes)."
            ),
        },
        "status": "exploratory",
        "tags": [
            "pentagon-archimedean",
            "multi-pair",
            "borromean",
            "h4-coefficient",
            "categorical-derivation",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "pentagon-multipair-borromean-h4-probe.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
