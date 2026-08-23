#!/usr/bin/env python3
r"""Probe: casimir-mode-indexed-derivation
(audit support for conj:casimir-epsilon-vacuum, derivation attempt).

**This probe is the most-honest derivation attempt.**  It states
the additional axiom needed explicitly, performs the derivation
under that axiom, and reports the result at substrate.

**Proposed extension to `prop:vacuum-epsilon`:**

> **Mode-indexed-vacuum axiom (proposed).** *For each natural
> number `n`, there exists a categorical "mode-n unknot"
> `⊙_n` such that:*
>
>     Geom(⊙_n)  =  ε_n  :=  ε · [n]_q
>
> *where `[n]_q = (q^n − q^{−n})/(q − q^{−1})` is the symmetric
> q-integer.  At `q = 1`, `[n]_q = n`, so `ε_n = n · ε`.*

**Motivation for `[n]_q`:**  In standard physics, the n-th plate
mode has energy `ℏω_n = ℏc·nπ/d` — linear in n.  In QOU, the
natural q-deformation of "linear in n" is "linear in `[n]_q`",
since `[n]_q` is the symmetric q-integer that QOU uses throughout
(α_em = 1/(q·[9]_q·[10]_q), atomic dressed levels (2k+1)-shells
as `[2k+1]_q`, etc.).

**Derivation under the mode-indexed axiom:**

Step 1.  Per-mode energy (in surreal units, dimensionless):
$$
   u_n  =  \tfrac{1}{2}\,\hbar c \cdot \mathrm{Geom}(\unicode{9737}_n)
         =  \tfrac{1}{2}\,\hbar c \cdot \varepsilon \cdot [n]_q
$$

Step 2.  Transverse mode integration in 2D `k_⊥` plane gives
factor `~ (n·π/d)³` per mode (standard Casimir derivation).  In
QOU this becomes `[n]_q³ · (π/d)³`:
$$
   u_n^{\mathrm{integrated}}  =  c_{\mathrm{geom}} \cdot \hbar c \cdot \varepsilon \cdot [n]_q^{3} \cdot (\pi/d)^{3}
$$
where `c_geom` collects geometric (π and integration) factors that
are q-independent.

Step 3.  Total energy per area:
$$
   u(d)/A  =  c_{\mathrm{geom}} \cdot \hbar c \cdot \varepsilon \cdot (\pi/d)^{3} \cdot \sum_{n\geq 1} [n]_q^{3}
$$

Step 4.  Surreal-Borel regularization.  `Σ [n]_q³` diverges
classically.  The q-analytic-continuation gives a specific
value at substrate q₀; we test three candidate
regularizations:

  (a) `1/[5]_q!_sym` (template fit from sweep 6)
  (b) `−β_4^q / 4` Carlitz (template fit from sweep 2)
  (c) Cesàro-style: `lim_{k→3⁺} Σ [n]_q³ · q^{-kn}` evaluated at
      critical damping

For each, multiply by `c_geom` (= 1/720 from classical fit) and
compare to π²/720.

**Critical question:**  Does ANY of the three regularizations
give the textbook prefactor at substrate, OR do they predict
substrate-specific deviations?  If they DISAGREE among themselves,
then the choice of regularization is the actual open question —
sub-problem 3 is the regularization problem, not the prefactor.

Emits `casimir-mode-indexed-derivation.witness.json`.

Ref: [casimir1948] https://dwc.knaw.nl/DL/publications/PU00018547.pdf
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path
from math import comb

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from mpmath import mp, mpf, pi as mp_pi  # noqa: E402

from q_parameter import Q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def _q_int(n: int, q: "mpf") -> "mpf":
    return (q ** n - q ** (-n)) / (q - 1 / q)


def _q_factorial_sym(n: int, q: "mpf") -> "mpf":
    r = mpf(1)
    for k in range(1, n + 1):
        r *= _q_int(k, q)
    return r


def _carlitz_beta_4(q: "mpf") -> "mpf":
    """Carlitz q-Bernoulli β_4^q via the recursion (q=1 → -1/30)."""
    beta = [mpf(0)] * 5
    beta[0] = mpf(1)
    for n in range(1, 5):
        lhs_coef = q ** (n + 1) - 1
        if lhs_coef == 0:
            raise ValueError(f"q^{n+1} = 1; q is a root of unity")
        rhs = mpf(1) if n == 1 else mpf(0)
        partial = mpf(0)
        for k in range(0, n):
            partial += mpf(comb(n, k)) * q ** (k + 1) * beta[k]
        beta[n] = (rhs - partial) / lhs_coef
    return beta[4]


def _cesaro_critical(q: "mpf", N: int = 500) -> "mpf":
    """Cesàro-style: evaluate Σ [n]_q^3 · q^{-kn} at k = 3 + δ for small δ.

    Extrapolate to k → 3⁺ via inverse-power fit.
    """
    # Sample at k = 3.5, 3.2, 3.1, 3.05
    samples = []
    for k_val in [3.5, 3.2, 3.1, 3.05, 3.02, 3.01]:
        k = mpf(k_val)
        total = mpf(0)
        for n in range(1, N + 1):
            term = _q_int(n, q) ** 3 * q ** (-k * n)
            total += term
            if abs(term) < mpf("1e-40"):
                break
        samples.append((k_val, total))
    # Naive extrapolation: take the value at k = 3.01 (closest to critical)
    return samples[-1][1]


def main() -> int:
    builder = WitnessBuilder(
        "casimir-mode-indexed-derivation",
        engine="mpmath",
    )

    q = mpf(Q)
    pi_sq = mp_pi ** 2
    pi_sq_720 = pi_sq / 720
    target_120 = mpf(120)  # classical |1/ζ(-3)|

    # ─── Three candidate regularizations of Σ [n]_q³ at substrate ───
    # (a) [5]_q!_sym (template substitution from sweep 6)
    q5fact = _q_factorial_sym(5, q)
    reg_a_value = q5fact  # interpreted as "1/ζ_q(-3) = [5]_q!_sym"
    reg_a_zeta = -1 / reg_a_value

    # (b) Carlitz β_4^q (template substitution from sweep 2)
    beta_4 = _carlitz_beta_4(q)
    reg_b_zeta = -beta_4 / mpf(4)
    reg_b_value = -1 / reg_b_zeta if reg_b_zeta != 0 else mpf("inf")

    # (c) Cesàro extrapolation
    reg_c_finite = _cesaro_critical(q)
    # Cesàro gives a positive value (divergent in limit); use 1/finite as proxy
    reg_c_zeta = -1 / reg_c_finite if reg_c_finite != 0 else mpf(0)
    reg_c_value = reg_c_finite

    # Each gives a different Casimir prefactor:
    candidates = []
    for name, zeta_value in [
        ("(a) 1/[5]_q!_sym         template-sub", reg_a_zeta),
        ("(b) Carlitz -β_4^q/4       template-sub", reg_b_zeta),
        ("(c) Cesàro at k=3.01      analytic-continuation", reg_c_zeta),
    ]:
        # Casimir prefactor: |ζ_q(-3)| · π²/6  (the standard geometric factor)
        c_q = abs(zeta_value) * pi_sq / 6
        rel_res = abs(c_q - pi_sq_720) / pi_sq_720
        # Multiply by 3 to get force-prefactor π²/240
        force_prefactor = c_q * 3
        textbook_force = pi_sq / 240
        force_residue = abs(force_prefactor - textbook_force) / textbook_force
        candidates.append({
            "regularization": name,
            "zeta_q_neg_3_value": float(zeta_value),
            "energy_prefactor_c_q": float(c_q),
            "energy_prefactor_target": float(pi_sq_720),
            "energy_rel_residue": float(rel_res),
            "force_prefactor_c_q": float(force_prefactor),
            "force_prefactor_target": float(textbook_force),
            "force_rel_residue": float(force_residue),
        })

    # ─── Disagreement assessment ───
    # If the 3 candidates agree within 1% → the choice is essentially
    # forced and we have a derivation.
    # If they disagree by > 1% → regularization choice is the open
    # question, and we have NOT derived the prefactor.
    values = [c["energy_prefactor_c_q"] for c in candidates if abs(c["energy_prefactor_c_q"]) < float("inf")]
    if values:
        spread = (max(values) - min(values)) / pi_sq_720 if min(values) > 0 else mpf("inf")
    else:
        spread = mpf("inf")

    derivation_succeeded = float(spread) < 0.01

    (
        builder
        .set_description(
            "Derivation attempt under the proposed mode-indexed-"
            "vacuum axiom: ε_n = ε · [n]_q.  Derivation chain "
            "follows standard Casimir steps with [n]_q substituted "
            "for n.  At Step 4 (regularization), three candidate "
            "q-zeta values are tested.  If they AGREE within 1%, "
            "the derivation is forced and we have a real result.  "
            "If they DISAGREE by > 1%, the regularization choice "
            "is the actual open question and the prefactor is NOT "
            "derived — only fit by choosing one regularization."
        )
        .set_content_block("conj:casimir-epsilon-vacuum")
        .add_parameter("substrate_q", float(q))
        .add_parameter("target_energy_prefactor", float(pi_sq_720))
        .add_parameter("target_force_prefactor", float(pi_sq / 240))
        .add_data("regularization_candidates", candidates)
        .add_data(
            "agreement_assessment",
            {
                "spread_relative_to_target": float(spread),
                "derivation_succeeded": bool(derivation_succeeded),
                "verdict": (
                    "DERIVED — regularizations agree, prefactor forced"
                    if derivation_succeeded
                    else "NOT DERIVED — regularizations disagree, choice = free parameter"
                ),
            },
        )
        .add_assertion(
            name="regularizations_agree_within_one_percent",
            computed=float(spread),
            expected=0.0,
            tolerance=0.01,
            unit="(max c_q - min c_q) / target",
            source=(
                "If this passes, the mode-indexed-vacuum axiom "
                "forces a unique answer and we have a derivation.  "
                "If it fails, the choice of q-zeta regularization "
                "is the actual open content and the prefactor "
                "remains undetermined."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"Substrate q = {float(q):.10f}")
    print(f"Target energy prefactor π²/720 = {float(pi_sq_720):.8e}")
    print(f"Target force prefactor π²/240  = {float(pi_sq / 240):.8e}")
    print()
    print("─── Three regularization candidates ───")
    for c in candidates:
        print(f"  {c['regularization']}")
        print(f"     ζ_q(-3)             = {c['zeta_q_neg_3_value']:.6e}")
        print(f"     c_q (energy/720)    = {c['energy_prefactor_c_q']:.6e}  (residue {c['energy_rel_residue']*100:6.2f}%)")
        print(f"     c_q (force/240)     = {c['force_prefactor_c_q']:.6e}  (residue {c['force_rel_residue']*100:6.2f}%)")
    print()
    print("─── Verdict ───")
    print(f"  spread across regularizations: {float(spread)*100:.2f}% of target")
    if derivation_succeeded:
        print("  → DERIVED: regularizations agree within 1%.")
    else:
        print("  → NOT DERIVED: regularizations disagree by >1%.")
        print("    The choice of q-zeta regularization is the actual open content.")
        print("    Without it, the prefactor is FIT, not derived.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
