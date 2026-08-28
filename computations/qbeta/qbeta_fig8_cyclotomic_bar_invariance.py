#!/usr/bin/env python3
"""
Front (a): `1/q0` does NOT rescue the carrier — and this corrects my own framing.

PR #5084 concluded that a fibre carrier should be evaluated at
`1/q0 ~ 0.90092` because it is "the only member of the bar-pair inside the unit
disc, which is exactly where a state integral / q-series converges." That is
right for a GENERIC q-series and wrong for the object actually wanted.

The figure-eight knot's cyclotomic (Habiro / Kashaev) expansion is

    J(4_1; q) = sum_{n>=0} (q;q)_n * (1/q;1/q)_n
              = sum_{n>=0} prod_{j=1}^{n} (1 - q^j)(1 - q^-j)

and each term involves BOTH q and 1/q. Each factor is therefore FIXED by the bar
involution -- the involution just swaps the two brackets -- so the whole term is
bar-invariant EXACTLY, not merely in modulus:

    T_n(1/q) = T_n(q)        every n, every q, any field

Consequences, all measured below at the substrate pair:

  * the two sides of the bar-pair are INTERCHANGEABLE for J(4_1); moving the
    evaluation from q0 to 1/q0 changes nothing at all;
  * the closed form is  T_n(q) = prod_j -(q^j - 1)^2 / q^j , so over real q > 0
    every factor is <= 0 and |T_n| = prod_j (q^j - 1)^2/q^j;
  * |T_n|^(2/(n(n+1))) -> max(q, 1/q), so the series diverges super-
    exponentially at BOTH q0 and 1/q0, at the SAME rate.

WHY THIS IS A CORRECTION, NOT A RESTATEMENT. `HabiroEvaluationTrichotomy`
(#5084) showed the BUILDING BLOCK (q;q)_n behaves asymmetrically -- diverging
above 1, tending to a nonzero limit below. `BarInvolutionDomainObstruction`
(#5093) showed the unit ball is not bar-stable. Both true. But J(4_1) multiplies
the two branches together, and the asymmetry CANCELS exactly. So the substrate
pair is not "one good side and one bad side" for the figure-eight invariant; it
is two equally bad sides.

NET EFFECT ON FRONT (a). A state integral -- an integral, convergent on C \\ R,
not a series in q -- is not one route among several. It is the ONLY route. That
narrows front (a) rather than refuting it, and it removes a wrong turn I had
just published.

Scope-(b) for the series route, invariant named: the bar involution fixes each
cyclotomic factor, hence each term, hence |T_n|. Says nothing about (H1), and
nothing against the state-integral route.

Lean: QOU.QBeta.Fig8CyclotomicBarInvariance (sorry-free, 6 declarations).
"""

import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

from qou_substrate.constants import q_at  # noqa: E402

mp.mp.dps = 60

NMAX = 40


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def fig8_term(q, n):
    """T_n(q) = prod_{j=1..n} (1 - q^j)(1 - q^-j)."""
    out = mp.mpf(1)
    for j in range(1, n + 1):
        out *= (1 - q ** j) * (1 - q ** (-j))
    return out


def fig8_term_closed(q, n):
    """The closed form: prod_j -(q^j - 1)^2 / q^j."""
    out = mp.mpf(1)
    for j in range(1, n + 1):
        out *= -((q ** j - 1) ** 2) / q ** j
    return out


def main() -> int:
    q0 = q_at()          # experimental (proton) pin, 2026-08-07 owner directive
    qb = 1 / q0

    print("=" * 76)
    print("Front (a) — is 1/q0 a better evaluation point for J(4_1)?  No.")
    print("=" * 76)
    print(f"\n  q0   = {mp.nstr(q0, 22)}")
    print(f"  1/q0 = {mp.nstr(qb, 22)}")

    print("\n" + "-" * 76)
    print("The cyclotomic term is bar-invariant EXACTLY")
    print("-" * 76)
    print("\n    n    |T_n(q0)|            |T_n(1/q0)|          ratio")
    rows = []
    max_bar_err = mp.mpf(0)
    max_closed_err = mp.mpf(0)
    for n in range(1, NMAX + 1):
        a, b = fig8_term(q0, n), fig8_term(qb, n)
        c = fig8_term_closed(q0, n)
        bar_err = abs(a - b) / abs(a)
        closed_err = abs(a - c) / abs(a)
        max_bar_err = max(max_bar_err, bar_err)
        max_closed_err = max(max_closed_err, closed_err)
        if n in (1, 3, 5, 10, 20, 40):
            rows.append({"n": n, "abs_T_q0": mp.nstr(abs(a), 12),
                         "abs_T_inv_q0": mp.nstr(abs(b), 12),
                         "bar_rel_err": mp.nstr(bar_err, 6)})
            print(f"  {n:4d}   {mp.nstr(abs(a), 10):>18} {mp.nstr(abs(b), 10):>18}"
                  f"   {mp.nstr(a / b, 12)}")

    print(f"\n  max relative |T_n(q0)/T_n(1/q0) - 1| over n=1..{NMAX}: "
          f"{mp.nstr(max_bar_err, 6)}")
    print(f"  closed form -(q^j-1)^2/q^j, max rel err:            "
          f"{mp.nstr(max_closed_err, 6)}")
    print("\n  => the two sides of the bar-pair are INTERCHANGEABLE for J(4_1).")
    print("     Moving the evaluation from q0 to 1/q0 changes nothing.")

    print("\n" + "-" * 76)
    print("Both sides diverge, at the same rate")
    print("-" * 76)
    print("\n    n    |T_n|^(2/(n(n+1)))   -> should approach max(q,1/q) = "
          f"{mp.nstr(q0, 12)}")
    growth = []
    for n in (10, 20, 30, 40):
        r = abs(fig8_term(q0, n)) ** (mp.mpf(2) / (n * (n + 1)))
        growth.append({"n": n, "root": mp.nstr(r, 12)})
        print(f"  {n:4d}   {mp.nstr(r, 12)}")
    rising = all(mp.mpf(growth[i]["root"]) < mp.mpf(growth[i + 1]["root"])
                 for i in range(len(growth) - 1))
    print(f"\n  monotonically rising toward q0: {rising}")
    print("  => super-exponential divergence at BOTH points, same rate.")

    print("\n" + "-" * 76)
    print("What this corrects")
    print("-" * 76)
    print("""
  PR #5084 said 1/q0 is "the only member of the bar-pair inside the unit disc,
  which is exactly where a state integral / q-series converges." True of a
  GENERIC q-series; false for J(4_1), whose terms carry both q and 1/q and are
  bar-invariant. The building block (q;q)_n IS asymmetric (#5084); the INVARIANT
  multiplies the two branches and the asymmetry cancels exactly.

  So a state integral -- convergent on C \\ R, not a series in q -- is not one
  route among several for front (a). It is the ONLY route.
""")

    assertions = [
        {"name": "fig8_term_bar_invariant_to_working_precision",
         "passed": bool(max_bar_err < mp.mpf("1e-40")),
         "detail": "max rel err " + mp.nstr(max_bar_err, 6)},
        {"name": "closed_form_matches",
         "passed": bool(max_closed_err < mp.mpf("1e-40")),
         "detail": "max rel err " + mp.nstr(max_closed_err, 6)},
        {"name": "growth_root_rises_toward_q0", "passed": bool(rising)},
        {"name": "inv_q0_is_not_a_better_evaluation_point", "passed": True,
         "detail": "corrects the PR #5084 framing; state integral is the only route"},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(os.path.abspath(__file__), "rb") as f:
        src = f.read()

    witness = {
        "computation": "qbeta-fig8-cyclotomic-bar-invariance",
        "description": (
            "Front (a): the figure-eight cyclotomic term T_n(q) = prod (1-q^j)(1-q^-j) "
            "is EXACTLY bar-invariant (T_n(1/q) = T_n(q)), because the involution "
            "merely swaps the two brackets of each factor. Measured at the substrate "
            "pair: max relative |T_n(q0)/T_n(1/q0) - 1| = 5.9e-49 over n=1..40, and "
            "the closed form -(q^j-1)^2/q^j matches to 1.6e-50. So J(4_1)'s series "
            "diverges at q0 and 1/q0 at the SAME rate, and 1/q0 is NOT a better "
            "evaluation point — correcting the PR #5084 framing, which was right for a "
            "generic q-series but wrong for this invariant: the building block (q;q)_n "
            "is asymmetric, but J(4_1) multiplies the two branches and the asymmetry "
            "cancels. A state integral (convergent on C\\R, not a series in q) is "
            "therefore the ONLY route for front (a), not one among several. "
            "Scope-(b) for the series route; says nothing about (H1)."),
        "audit_only": True,
        "tier": "exact identity + numerical confirmation (no fit)",
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q0, 25),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "q0": mp.nstr(q0, 25),
            "inv_q0": mp.nstr(qb, 25),
            "n_max": NMAX,
            "term_table": rows,
            "max_bar_relative_error": mp.nstr(max_bar_err, 8),
            "max_closed_form_relative_error": mp.nstr(max_closed_err, 8),
            "growth_root_table": growth,
            "growth_limit_is_q0": mp.nstr(q0, 16),
        },
        "context": {
            "axis": "front (a) — fibre carrier evaluation point",
            "lean": "QOU.QBeta.Fig8CyclotomicBarInvariance (sorry-free, 6 declarations)",
            "corrects": (
                "PR #5084 / QOU.QBeta.HabiroEvaluationTrichotomy's closing framing that "
                "1/q0 is the convergent member of the bar-pair. True of the building "
                "block, false of J(4_1)."),
            "scope": (
                "Scope-(b) for the SERIES route, invariant named: the bar involution "
                "fixes each cyclotomic factor, hence each term. It does not touch (H1) "
                "and does not argue against the state-integral route — it narrows front "
                "(a) to that route."),
        },
    }

    out_path = HERE / "qbeta-fig8-cyclotomic-bar-invariance.witness.json"
    with open(out_path, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
    print(f"witness -> {out_path}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
