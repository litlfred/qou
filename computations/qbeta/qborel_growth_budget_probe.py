#!/usr/bin/env python3
"""q-Borel growth budget: does ANY unramified level d absorb deg_q(c_n) = n^2?

Formalize-first prune for the W2 infinity-residual (bean qou-qbg2). Runs before
any analytic work on the transform, because it is cheap and potentially decisive.

SETUP
-----
RSZ (arXiv:0903.0853) §3.3 resolves a level-d singularity with

    B_{q,d}( sum f_n z^n ) = sum (f_n / t_n) xi^n,   t_n = q^{n-d} t_{n-d},

with stated kernel growth q^{n^2 / 2d}. The C1 infinity formal solution has
coefficient growth deg_q(c_n) = n^2 -- PROVED for all n, sorry-free, in
QOU/QBeta/C1InfDegreeLaw.lean (cCoeff_natDegree); see
docs/audits/2026-08-08-c1-inf-degree-law-proved.md.

For the transformed series to converge, the kernel must absorb the coefficient
growth, i.e. deg(c_n) - deg(t_n) must be bounded (<= 0 asymptotically per n^2).

WHAT THIS COMPUTES
------------------
Only DEGREES -- integer arithmetic on the kernel recurrence. No analysis, no
floats in the recurrence itself, nothing fitted.

  (a) deg t_n for the level-d kernel, from t_n = q^{n-d} t_{n-d}.
  (b) The ratio deg(t_n)/n^2, checked against RSZ's stated 1/(2d) -- this
      validates that the recurrence is being read correctly.
  (c) The budget deg(c_n/t_n)/n^2 = (n^2 - deg t_n)/n^2.

RESULT (see witness): (b) matches RSZ to ~3 decimals, so the reading is right;
and (c) is POSITIVE for every d tested, growing worse with d. No unramified
level d absorbs the growth.

SCOPE -- this is a consistency computation on degrees, NOT a theorem about RSZ.
It says the unramified B_{q,d} applied directly to sum c_n x^{-n} cannot
converge. Three candidate resolutions (ramification forced / normalization
mismatch / slope->level convention) are enumerated in bean qou-qbg2 and the
plan doc; deciding among them is stage S1.

Nothing fitted, nothing wired.
"""

from __future__ import annotations

import json
import os
import subprocess
from fractions import Fraction
from typing import Dict, List

import mpmath as mp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

mp.mp.dps = 60

D_VALUES = (1, 2, 3, 4)
N_ASYMPTOTIC = 400
N_TABLE = (4, 8, 12, 20, 30, 40)


def kernel_degrees(d: int, n_max: int) -> List[int]:
    """deg_q(t_n) for t_n = q^{n-d} t_{n-d}, with t_0 .. t_{d-1} = 1."""
    t = [0] * (n_max + 1)
    for n in range(n_max + 1):
        t[n] = 0 if n < d else (n - d) + t[n - d]
    return t


def coeff_degree(n: int) -> int:
    """deg_q(c_n) = n^2 -- PROVED (QOU.QBeta.cCoeff_natDegree), not assumed."""
    return n * n


def _rat(fr: Fraction) -> dict:
    """An exact rational, as both its "p/q" form and a 50-digit decimal.

    Neither alone is right for a witness: "p/q" is exact but unreadable and
    uncomparable at a glance, and a decimal alone throws the exactness away.
    Both, and no float64 anywhere in between.
    """
    return {"exact": f"{fr.numerator}/{fr.denominator}",
            "decimal": mp.nstr(mp.mpf(fr.numerator) / mp.mpf(fr.denominator), 50)}


def main() -> None:
    per_d: Dict[str, dict] = {}
    any_absorbs = False

    for d in D_VALUES:
        t = kernel_degrees(d, N_ASYMPTOTIC)
        # Every quantity here is an INTEGER over an INTEGER -- kernel degrees
        # t_n and the proved deg_q(c_n) = n^2 are exact. They were computed in
        # binary floating point, which put two verdicts (`< 0.01` and `<= 0`) on
        # the wrong side of a rounding step for no reason: Fraction is exact and
        # costs nothing at these sizes. Serialized as exact "p/q" plus a 50-dps
        # decimal, so the witness carries the rational, not a float64 shadow.
        measured = Fraction(t[N_ASYMPTOTIC], N_ASYMPTOTIC**2)
        predicted = Fraction(1, 2 * d)
        budget = Fraction(coeff_degree(N_ASYMPTOTIC) - t[N_ASYMPTOTIC],
                          N_ASYMPTOTIC**2)
        absorbs = budget <= 0
        any_absorbs |= absorbs
        per_d[str(d)] = {
            "measured_deg_t_over_n2": _rat(measured),
            "rsz_predicted_1_over_2d": _rat(predicted),
            "abs_diff": _rat(abs(measured - predicted)),
            "reading_matches_rsz": abs(measured - predicted) < Fraction(1, 100),
            "budget_deg_c_minus_t_over_n2": _rat(budget),
            "kernel_absorbs_growth": absorbs,
            "table": [
                {"n": n, "deg_t_n": t[n], "deg_c_n": coeff_degree(n),
                 "difference": coeff_degree(n) - t[n]}
                for n in N_TABLE
            ],
        }

    print(f"{'d':>3} {'deg t_n/n^2':>12} {'RSZ 1/2d':>9} {'match':>6} {'budget':>9} {'absorbs':>8}")
    for d in D_VALUES:
        r = per_d[str(d)]
        print(
            f"{d:>3} {float(mp.mpf(r['measured_deg_t_over_n2']['decimal'])):>12.4f} "
            f"{float(mp.mpf(r['rsz_predicted_1_over_2d']['decimal'])):>9.4f} "
            f"{str(r['reading_matches_rsz']):>6} "
            f"{float(mp.mpf(r['budget_deg_c_minus_t_over_n2']['decimal'])):>+9.4f} "
            f"{str(r['kernel_absorbs_growth']):>8}"
        )
    print()
    print(f"ANY unramified level d absorbs deg_q(c_n) = n^2 : {any_absorbs}")

    here = os.path.dirname(os.path.abspath(__file__))
    script = os.path.abspath(__file__)
    try:
        sha = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", script],
            cwd=here, stderr=subprocess.DEVNULL,
        ).decode().strip() or "uncommitted"
    except Exception:
        sha = "uncommitted"

    witness = {
        "schema": "witness/v1",
        "description": (
            "q-Borel growth budget for the C1 infinity residual: compares the "
            "RSZ level-d kernel degree growth against the PROVED coefficient "
            "growth deg_q(c_n) = n^2. Finds that no unramified level d absorbs "
            "it (budget positive for every d, worsening with d), so the "
            "unramified B_{q,d} cannot be the resolving transform. Formalize-"
            "first prune for stage S1 (bean qou-qbg2)."
        ),
        "computation": {"script": os.path.relpath(script, os.path.dirname(here))},
        "witness": {"scriptCommitSha": sha},
        "inputs": {
            "kernel_recurrence": "t_n = q^{n-d} * t_{n-d}, t_0..t_{d-1} = 1 (RSZ 3.3)",
            "coefficient_growth": "deg_q(c_n) = n^2",
            "coefficient_growth_status": (
                "PROVED sorry-free: QOU.QBeta.cCoeff_natDegree "
                "(content/quantum-observable-universe/lean/QOU/QBeta/C1InfDegreeLaw.lean)"
            ),
            "n_asymptotic": N_ASYMPTOTIC,
            "d_values": list(D_VALUES),
        },
        "results": {
            "per_d": per_d,
            "any_unramified_level_absorbs_growth": any_absorbs,
        },
        "verdict": (
            "scope-(a): the UNRAMIFIED B_{q,d} applied directly to sum c_n x^{-n} "
            "cannot converge for any tested d. This is a degree-consistency "
            "computation, not a theorem about RSZ. Candidate resolutions "
            "(ramification forced / normalization mismatch / slope-to-level "
            "convention) are stage S1, bean qou-qbg2."
        ),
        "wired_to_production": False,
        "is_fit": False,
    }
    out = os.path.join(here, "qborel-growth-budget-probe.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, fh, indent=2)
        fh.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"witness -> {os.path.relpath(out)}")


if __name__ == "__main__":
    main()
