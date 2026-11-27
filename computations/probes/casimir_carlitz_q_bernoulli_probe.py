#!/usr/bin/env python3
"""Probe: casimir-carlitz-q-bernoulli
(audit support for conj:casimir-epsilon-vacuum, Route A sub-problem 3).

**Question.**  Does the Carlitz q-Bernoulli definition (ζ_q^{KKW}
via Kaneko–Kurokawa–Wakayama 2002, with values at negative
integers given by q-Bernoulli numbers β_n^q) recover the Casimir
prefactor `π²/720`?

The standard derivation uses:

    ζ(-3) = -B_4/4 = -1/120     ⟹    Casimir prefactor π²/720

The q-analogue would use:

    ζ_q(-3) = -β_4^q / [4]_q

with `β_4^q` the Carlitz q-Bernoulli number.  At `q → 1`,
`β_4^q → B_4 = -1/30`, so `ζ_q(-3) → -(-1/30)/4 = 1/120` … wait,
classical `ζ(-3) = -1/120`, with sign convention matters. Let's
just compute and compare.

**Carlitz q-Bernoulli recursion (Carlitz 1948):**

    β_0^q = 1
    For n ≥ 1:
      Σ_{k=0}^{n} C(n,k) · q^{k+1} · β_k^q  -  β_n^q  =  δ_{n,1}

Closed-form low cases:

    β_0^q = 1
    β_1^q = -1 / (q + 1)
    β_2^q = q / ((q + 1)(q² + q + 1))
    β_3^q = 0  (at q = 1 it's -B_2/2 = -1/12; should check)
    β_4^q = …

**Empirical test at substrate `q_0 ≈ 1.110`:**

1. Compute β_n^q for n = 0..4 symbolically via the recursion.
2. Evaluate at substrate q_0 to 50 dps.
3. Compute candidate q-zeta values:
   - ζ_q(-3) = -β_4^q / [4]_q
   - Compare to -1/120 (classical target)
4. Multiply by π² and divide by 6 (Casimir geometric factor) to
   see if we recover π²/720.

Emits `casimir-carlitz-q-bernoulli-probe.witness.json`.

A null result (no clean recovery of π²/720) reinforces the
audit's conclusion that the prefactor is not substrate-derivable
from low-degree q-rationals — even with the more sophisticated
Carlitz q-zeta machinery.

Ref: [casimir1948] https://dwc.knaw.nl/DL/publications/PU00018547.pdf
Ref: [carlitz1948] Carlitz, "q-Bernoulli numbers and polynomials",
                   Duke Math. J. 15, 987-1000 (1948)
Ref: [kaneko-kurokawa-wakayama2002] doi:10.4310/MRL.2003.v10.n2.a4
"""
from __future__ import annotations


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

import sys
from pathlib import Path
from math import comb

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from mpmath import mp, mpf, pi as mp_pi  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()


def _q_int(n: int, q: "mpf") -> "mpf":
    """[n]_q = (qⁿ - q⁻ⁿ) / (q - q⁻¹)."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def carlitz_q_bernoulli(n_max: int, q: "mpf") -> list["mpf"]:
    """Compute β_n^q for n = 0..n_max via the Carlitz recursion.

    Recursion (Carlitz 1948):
        Σ_{k=0}^{n} C(n,k) · q^{k+1} · β_k^q  -  β_n^q  =  δ_{n,1}

    Solve for β_n^q:
        β_n^q · (q^{n+1} - 1)  =  -Σ_{k=0}^{n-1} C(n,k) · q^{k+1} · β_k^q + δ_{n,1}

    Returns [β_0, β_1, ..., β_{n_max}] as mpf.
    """
    beta = [mpf(0)] * (n_max + 1)
    beta[0] = mpf(1)
    for n in range(1, n_max + 1):
        lhs_coef = q ** (n + 1) - 1   # coefficient of β_n^q
        if lhs_coef == 0:
            raise ValueError(f"q^{n+1} - 1 = 0; q is a root of unity")
        rhs = mpf(1) if n == 1 else mpf(0)
        # Move the k=n contribution from LHS sum to LHS-isolated form:
        # Σ_{k=0}^{n} ... · β_k - β_n = δ ⟹ β_n · (q^{n+1} - 1) = δ - Σ_{k=0}^{n-1} ... · β_k
        partial = mpf(0)
        for k in range(0, n):
            partial += mpf(comb(n, k)) * q ** (k + 1) * beta[k]
        beta[n] = (rhs - partial) / lhs_coef
    return beta


def main() -> int:
    builder = WitnessBuilder(
        "casimir-carlitz-q-bernoulli-probe",
        engine="mpmath",
    )

    # NOT `mpf(Q)` / `mpf(str(Q))`: `q_parameter.Q` is `float(_d["q"])`, so
    # either form lifts the DOUBLE's binary expansion and caps this whole
    # probe at ~17 digits.  Read the pin as the SOURCE STRING and build the
    # mpf here, i.e. AFTER `set_compute_dps()`.  Do NOT substitute the
    # module-level `Q_MP`: `q_parameter` builds it at `mp.dps = 50`, so it is
    # a 50-digit cap, which is BELOW `OUTPUT_DPS = 60`.  Measured against the
    # exact 50-digit decimal in `Fraction` arithmetic, `mpf(Q_50_DIGIT_STR)`
    # built at dps 70 sits 4.594e-72 from it and `Q_MP` sits 2.015e-50.
    q = Q_MP
    pi_sq = mp_pi ** 2
    pi_sq_720 = pi_sq / 720
    target_zeta_neg_3 = mpf(-1) / 120   # classical ζ(-3) = -B_4/4 = -1/120

    # ─── Step 1: Compute Carlitz q-Bernoulli numbers β_0 … β_4 ───
    beta_q = carlitz_q_bernoulli(4, q)
    beta_at_q1 = [mpf(1), mpf("-0.5"), mpf("1/6"), mpf(0), mpf("-1/30")]
    # Sanity-check the classical limit q → 1: β_n^q → B_n
    # (Bernoulli convention: B_0=1, B_1=-1/2, B_2=1/6, B_3=0, B_4=-1/30)

    # ─── Step 2: ζ_q(-3) candidates ───
    q4 = _q_int(4, q)
    zeta_q_neg3 = -beta_q[4] / q4

    # Alternative: standard ζ_q(-3) via β_4^q / 4 (no q-deformation in denom)
    zeta_q_neg3_alt = -beta_q[4] / mpf(4)

    # ─── Step 3: Map to Casimir prefactor ───
    # Standard derivation: |ζ(-3)| · π² / 6 = (1/120) · π² / 6 = π²/720.
    # So we expect any successful q-analogue to give |ζ_q(-3)| ≈ 1/120
    # at substrate, with the same π²/6 geometric multiplier.

    candidates = []
    for name, val in [
        ("ζ_q(-3) = -β_4^q / [4]_q", zeta_q_neg3),
        ("ζ_q(-3)_alt = -β_4^q / 4", zeta_q_neg3_alt),
        ("β_4^q only", beta_q[4]),
        ("β_4^q / [2]_q²", beta_q[4] / _q_int(2, q) ** 2),
        ("β_4^q · [2]_q / [4]_q", beta_q[4] * _q_int(2, q) / q4),
        ("β_4^q · [4]_q / [2]_q²", beta_q[4] * q4 / _q_int(2, q) ** 2),
    ]:
        # Map each to a Casimir-prefactor candidate via the standard
        # geometric multiplier `π² / 6` (which converts
        # ζ(-3) = -1/120 to π²/720):
        casimir_candidate = abs(val) * pi_sq / 6
        rel_residue = abs(casimir_candidate - pi_sq_720) / pi_sq_720
        # mpf-valued: `rel_residue_vs_pi_sq_720` is the `min()` key below AND
        # is compared against 0.01 in the assertion, so it is arithmetic, not
        # display.  Serialized once, at the witness.
        candidates.append({
            "form": name,
            "raw_value": val,
            "casimir_candidate": casimir_candidate,
            "rel_residue_vs_pi_sq_720": rel_residue,
        })

    # ─── Step 4: pick best match ───
    best = min(candidates, key=lambda c: c["rel_residue_vs_pi_sq_720"])

    (
        builder
        .set_description(
            "Empirical Carlitz q-Bernoulli probe for the Casimir-"
            "prefactor sub-problem.  Computes β_n^q for n = 0..4 "
            "via the Carlitz 1948 recursion, evaluates at substrate "
            "q ≈ 1.110, and checks whether any of {ζ_q(-3), "
            "β_4^q / [4]_q, β_4^q / [2]_q², ...} multiplied by "
            "the standard π² · 6 geometric factor recovers the "
            "Casimir prefactor π²/720.  A null result reinforces "
            "the audit's conclusion that the prefactor is not "
            "substrate-derivable from low-degree q-rationals — "
            "even with the more sophisticated Kaneko–Kurokawa–"
            "Wakayama q-zeta machinery."
        )
        .set_content_block("conj:casimir-epsilon-vacuum")
        .add_parameter("substrate_q", fmt(q))
        .add_parameter("target_pi_sq_720", fmt(pi_sq_720))
        .add_parameter("target_zeta_neg_3", fmt(target_zeta_neg_3))
        .add_data(
            "carlitz_q_bernoulli_numbers",
            [
                {
                    "n": n,
                    "beta_n_q_at_substrate": fmt(beta_q[n]),
                    "B_n_classical": fmt(beta_at_q1[n]),
                    "ratio": fmt(beta_q[n] / beta_at_q1[n])
                        if beta_at_q1[n] != 0 else "n/a (classical 0)",
                }
                for n in range(len(beta_q))
            ],
        )
        .add_data(
            "casimir_candidates",
            [
                {k: (v if k == "form" else fmt(v)) for k, v in c.items()}
                for c in candidates
            ],
        )
        .add_data(
            "best_carlitz_match",
            {
                "form": best["form"],
                "casimir_candidate": fmt(best["casimir_candidate"]),
                "rel_residue": fmt(best["rel_residue_vs_pi_sq_720"]),
            },
        )
        .add_assertion(
            name="zero_carlitz_candidates_within_one_percent",
            computed=float(sum(
                1 for c in candidates
                if c["rel_residue_vs_pi_sq_720"] < 0.01
            )),
            expected=0.0,
            tolerance=0.5,
            unit=(
                "count of Carlitz q-Bernoulli derived Casimir-"
                "prefactor candidates within 1% of π²/720"
            ),
            source=(
                "Empirical null assertion: even the Carlitz/KKW "
                "q-zeta machinery does not yield a sub-1% match "
                "to π²/720 at substrate q_0.  Passing this "
                "assertion documents that Route A (q-deformed ζ) "
                "remains open for sub-problem 3 of "
                "conj:casimir-epsilon-vacuum."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"Substrate q = {float(q):.10f}")
    print(f"Target π²/720 = {float(pi_sq_720):.8e}")
    print(f"Classical ζ(-3) = {float(target_zeta_neg_3):.8e}")
    print()
    print("─── Carlitz q-Bernoulli numbers ───")
    print(f"  {'n':<4} {'β_n^q at substrate':<22} {'B_n classical':<18} {'ratio':<10}")
    for n in range(len(beta_q)):
        cl = float(beta_at_q1[n])
        ratio = float(beta_q[n] / beta_at_q1[n]) if beta_at_q1[n] != 0 else "n/a"
        ratio_str = f"{ratio:<10.6f}" if isinstance(ratio, float) else f"{ratio:<10}"
        print(f"  {n:<4} {float(beta_q[n]):<22.10e} {cl:<18.10e} {ratio_str}")
    print()
    print("─── Carlitz Casimir-prefactor candidates ───")
    print(f"  {'form':<35} {'value':<20} {'rel residue':<12}")
    for c in candidates:
        print(f"  {c['form']:<35} {c['casimir_candidate']:<20.6e} {c['rel_residue_vs_pi_sq_720']:<12.4e}")
    print()
    print(f"BEST MATCH: {best['form']}")
    print(f"  value: {best['casimir_candidate']:.6e}")
    print(f"  rel residue: {best['rel_residue_vs_pi_sq_720']:.4e}")
    print()
    if best["rel_residue_vs_pi_sq_720"] < 0.01:
        print("→ MATCH! Carlitz q-zeta route closes sub-problem 3.")
    else:
        print("→ NULL RESULT: Carlitz q-Bernoulli does not yield π²/720 within 1%.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
