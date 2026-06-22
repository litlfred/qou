#!/usr/bin/env python3
"""
PSLQ uniqueness test for α_EM at 1000+ digit precision.

Tests whether the gluon-octet formula
    1/α_EM = 45·[3]_q·(1 + δ_CS + 8q·δ_CS²),  δ_CS = ℏ_q^4·[5]_q
is the UNIQUE q-arithmetic closed form matching CODATA α at 1000 dps,
or whether other integer relations exist in the same basis.

Method:
  1. Extend q_0 to 2000 dps via canonical formula
        q_0 = unique solution of  m_μ/m_e = Vol(4_1)/ℏ_q²
     using m_μ/m_e = 206.7682830 (CODATA) — but the framework's  # noqa: P31 — docstring narrative; live value comes from q_parameter.MASS_RATIO_MU_E_STR
     internal value is fixed by q_parameter at 17 digits.
     Since m_μ/m_e is bounded to ~22 ppb, treating q_0 as having
     more precision than that is a "what-if" exercise testing
     whether the closed-form formula extends consistently.

  2. Compute 1/α_EM(formula) at 2000 dps with extended q_0.

  3. Build basis of q-arithmetic objects:
        {1/α_form, 1, [n]_q for n=2..12, ℏ_q^k for k=1..6,
         π², ζ(3), G (Catalan), (q;q)_n for n=2..6, q^k}

  4. Run mpmath.pslq at 1000+ dps tolerance to find integer relations.

  5. Report:
      - Does the 'expected' relation {45·[3]_q, 8q·...} appear?
      - Are there OTHER simpler integer relations (with coeff < 1e6)?
      - At what tolerance does the closed form become unique?

Output: alpha-em-pslq-uniqueness.witness.json
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
from pathlib import Path
from datetime import datetime, timezone

import mpmath as mp

from q_parameter import vol_4_1_at
from witness_base import WitnessBuilder


def main():
    DPS = 1500  # Working precision; PSLQ at 1000 dps tolerance
    mp.mp.dps = DPS

    # Use the canonical q_0 string + extend digits via m_μ/m_e relation.
    # q_0 comes from solving m_μ/m_e = Vol(4_1) / ℏ_q² with ℏ_q = (q-1)/q.
    # Vol(4_1) = 2.029883212819307250042... (figure-eight, transcendental)
    # m_μ/m_e = 206.7682830 (input, ~22 ppb).  # noqa: P31 — comment narrative; live value via q_parameter.MASS_RATIO_MU_E_STR
    #
    # Since both inputs are CODATA-bounded, the "true" q_0 to 1000 dps
    # is not knowable — but we can test the formula's algebraic
    # CONSISTENCY at 1000 dps with a self-consistently extended q_0.

    # Vol(4_1) computed on demand at the working precision via the
    # Clausen identity Vol(4_1) = 2 Cl_2(π/3).  The previously-
    # hardcoded 38-dps string used here was inaccurate past digit
    # ~30 (its trailing digits did not match the converged Clausen
    # value), so PSLQ runs past 30 dps were searching corrupted
    # input.  See q_parameter.vol_4_1_at for the canonical source.
    Vol_4_1 = vol_4_1_at(DPS)
    # CAL-2: m_μ/m_e from q_parameter registry (P31-triage Phase B).
    from q_parameter import MASS_RATIO_MU_E_STR  # noqa: E402
    m_mu_over_m_e = mp.mpf(MASS_RATIO_MU_E_STR)

    # Solve q · m_mu/m_e = q · Vol(4_1) / ℏ_q²
    # i.e. m_μ/m_e · ((q-1)/q)² = Vol(4_1)
    # Quadratic in (q-1)/q: r² = Vol/(m_mu/m_e)
    target = Vol_4_1 / m_mu_over_m_e
    r = mp.sqrt(target)              # r = (q-1)/q  ⇒  q = 1/(1-r)
    q_0 = 1 / (1 - r)
    print(f"DPS = {DPS}")
    print(f"q_0 (extended)       = {mp.nstr(q_0, 50)}")
    print(f"q_0 (q_parameter.py) = 1.1099785955573347 (17 digits)")

    def q_int(n, q=q_0):
        return (q**n - q**(-n)) / (q - 1/q)

    def q_pochhammer(n, q=q_0):
        out = mp.mpf(1)
        for k in range(1, n+1):
            out *= (1 - q**k)
        return out

    # Compute the formula
    hbar_q = (q_0 - 1)/q_0
    delta_CS = hbar_q**4 * q_int(5)
    kappa = 8 * q_0
    one_over_alpha = 45 * q_int(3) * (1 + delta_CS + kappa * delta_CS**2)
    print(f"1/α_EM (formula at extended q_0) = {mp.nstr(one_over_alpha, 50)}")
    print(f"1/α_EM CODATA-2022                = 137.035999177(21)")
    print()

    # Build a candidate basis of q-arithmetic and transcendental objects
    print("Building PSLQ basis...")
    basis_labels = ["1/alpha"]
    basis_values = [one_over_alpha]

    # Constants
    for label, val in [
        ("1",        mp.mpf(1)),
        ("pi",       mp.pi),
        ("pi^2",     mp.pi**2),
        ("pi^4",     mp.pi**4),
        ("zeta(3)",  mp.zeta(3)),
        ("Catalan",  mp.catalan),
        ("e",        mp.e),
        ("euler",    mp.euler),
        ("log(2)",   mp.log(2)),
    ]:
        basis_labels.append(label); basis_values.append(val)

    # q-integers
    for n in range(2, 13):
        basis_labels.append(f"[{n}]_q"); basis_values.append(q_int(n))

    # Powers of q
    for k in range(1, 11):
        basis_labels.append(f"q^{k}"); basis_values.append(q_0**k)
        if k > 0:
            basis_labels.append(f"q^-{k}"); basis_values.append(q_0**(-k))

    # ℏ_q^k
    for k in range(1, 7):
        basis_labels.append(f"hbar_q^{k}"); basis_values.append(hbar_q**k)

    # q-Pochhammer (q;q)_n
    for n in range(2, 7):
        basis_labels.append(f"(q;q)_{n}"); basis_values.append(q_pochhammer(n))

    print(f"Basis size = {len(basis_values)}")
    print()

    # Run PSLQ with progressively tighter tolerance
    pslq_results = []
    for tol_dps in [50, 100, 200, 500, 1000]:
        print(f"--- PSLQ at tolerance 10^-{tol_dps} ---")
        t0 = time.time()
        try:
            tol = mp.mpf(10)**(-tol_dps)
            relation = mp.pslq(basis_values, tol=tol, maxcoeff=10**40)
            t1 = time.time()
            if relation is None:
                print(f"  No relation found  ({t1-t0:.1f}s)")
                pslq_results.append({"tol_dps": tol_dps, "relation": None,
                                     "walltime_s": t1-t0})
            else:
                # Express relation
                terms = [(c, lab) for c, lab in zip(relation, basis_labels) if c != 0]
                terms_str = " + ".join(f"{c}·{lab}" for c, lab in terms)
                print(f"  Relation: {terms_str} = 0")
                # Verify
                check = sum(c*v for c, v in zip(relation, basis_values))
                print(f"  |check| = {mp.nstr(abs(check), 6)}")
                pslq_results.append({
                    "tol_dps": tol_dps,
                    "relation": [(int(c), lab) for c, lab in zip(relation, basis_labels)],
                    "verify_residual": str(abs(check)),
                    "walltime_s": t1-t0,
                })
        except Exception as e:
            print(f"  EXCEPTION: {e}")
            pslq_results.append({"tol_dps": tol_dps, "exception": str(e)})

    out = {
        "computation": "alpha-em-pslq-uniqueness",
        "description": (
            "PSLQ uniqueness test for the hecke-engine-knot-tracker α_EM "
            "formula at 1000+ digit precision.  Tests whether 1/α = "
            "45·[3]_q·(1 + ℏ_q^4·[5]_q + 8q·(ℏ_q^4·[5]_q)²) is the "
            "UNIQUE integer relation in the q-arithmetic + transcendental "
            "basis at extreme precision, or whether spurious relations "
            "exist with comparable coefficient norms."
        ),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "precision_dps": DPS,
        "q_0_extended_50dp": mp.nstr(q_0, 50),
        "one_over_alpha_value_50dp": mp.nstr(one_over_alpha, 50),
        "basis_size": len(basis_values),
        "basis_labels": basis_labels,
        "pslq_results": pslq_results,
    }
    # P30 migration (compute-audit workplan, 2026-05-08): preserve the
    # original payload layout via WitnessBuilder.wrap_legacy so that
    # scriptHash + scriptCommitSha are recorded for staleness tracking
    # without changing top-level keys consumed by any narrative reader.
    builder = WitnessBuilder.wrap_legacy(
        "alpha-em-pslq-uniqueness",
        out,
        script_path=__file__,
        engine="mpmath",
    )
    if "auditOnly" not in out:
        builder.set_audit_only(
            "docs/audits/2026-05-08-compute-audit-workplan.md")
    out_path = builder.save()
    print()
    print(f"Witness: {out_path}")


if __name__ == "__main__":
    main()
