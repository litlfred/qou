#!/usr/bin/env python3
"""rho_pp_kind_weight_does_not_close_b3_probe.py — the kind-dependent bond weight is
REAL but far TOO WEAK to reproduce b3. (qou-brng, taking over qou-qqm4's target)

## What this answers

#7097 re-scoped `BrunnianTripleExhaustion.no_carrier_reproduces_b3` from a scope-(b)
exclusion of the count channel to a scope-(a) negative about *uniform-weight* carriers,
because `qou-qqm4` had derived that the inter-nucleon bond factor DEPENDS ON THE KIND of
pair it joins.  It then handed one falsifiable number to that front:

    rho_pp = 1 + rMeasured = 2433859/1483044 ~ 1.64112393

with an explicit rule -- READ IT RIGHT-TO-LEFT ONLY.  Computing `rho_pp` FROM the
measurement is a one-parameter fit and ranks below the honest 55.98% miss it would
replace; the only admissible use is to compute it INDEPENDENTLY from the derived bond
factors and COMPARE.

`qou-qqm4` did not respond (bean 16 h stale at takeover, > the 3 h threshold), so this
probe does the comparison.  **Nothing here is fitted.**

## The inputs, both from the corpus

`bond_pn_kind_order_four_discriminator_probe.py` measures all three bond factors as exact
rational series in `eps = q - 1` (its `z_D` docstring fixes that convention):

    pp  (1/2,  1,  1/4, -1/4, 1/8,    0  )   = z exactly
    pn  (1/2,  0,  3/4, -3/4, 31/24, -5/2)   = the `averaged_weighted` kind
    nn  (1/2, -1,  5/4, -5/4, 9/8,   -1  )   = z' = z - h

and `rMeasured = 950815/1483044` is `CarrierCrossingQuantisation`'s.

## The answer: NO, under every identification tried, and the PRINCIPLED one is WORST

`rho_pp` is a ratio of per-pair weights, and the bond factors are MULTIPLICATIVE factors
in a trace, so the identification is not forced.  Four are tried rather than one, and the
best-fitting is NOT reported as the answer:

    A  multiplicative   bond_pp / bond_pn          1.2056     miss 26.5 %
    B  ADDITIVE (log)   log(pp) / log(pn)          0.7238     miss 55.9 %   <- PRINCIPLED
    C  shifted additive 1 + (log pp - log pn)      1.1869     miss 27.7 %
    D  inverse          bond_pn / bond_pp          0.8295     miss 49.5 %

**B is the principled one** and it misses worst.  The binding law is
`B = E0 * log(tr_M(free)/tr_M(atom))`, so interface factors multiply inside the trace and
their LOGS add -- an additive per-pair weight must be a log, not a ratio.  Reporting A
(the closest) as "the" answer would be selecting an identification against the target,
which is the selection-fitting §"NO FITTING" names.

## And no small carrier rescues it

The `1.64112393` target assumed the MINIMAL 3He carrier.  Scanning every integer carrier
`m_pp, m_pn in 1..6` (3He = ppn, so the pairs are pp, pn, pn):

    A  best (m_pp, m_pn) = (1, 1)   closest miss 67.9 %   <- WORSE than uniform
    B  best (m_pp, m_pn) = (2, 1)   closest miss 30.2 %

against the uniform case's recorded 55.98 %.  The scan reports a BOUND -- "even the best
small carrier misses by 30 %" -- not a claim that the carrier is (2,1); reading a carrier
off the residual would be the same fit one level down.

## Verdict

The escape from the exhaustion is **real structurally and insufficient quantitatively**.
`kind_ratio_not_determined_by_sum` stands: a kind-dependent weight does break the
integrality that made the exhaustion exhaustive.  But the kind-dependence the corpus
actually derives is far too weak -- it needs `rho_pp ~ 1.64` and delivers 0.72-1.21.
Under the principled reading it does improve on uniform (55.98 % -> 30.2 %), and only
with a non-minimal carrier; under the multiplicative reading it is worse than uniform.

**This is a real negative about the bond model**, which is exactly what #7097 said the
disagreement branch would be.  It does not refute the count channel and it does not
restore the exhaustion: the exhaustion's own premise is still derived-false.  What it
removes is the hope that the already-derived kind-dependence closes the three-body gap.

PRECISION: mpmath end to end at 60 dps, seeded from `Q_50_DIGIT_STR` -- NOT the float64
`q_parameter.Q`, which is the exact defect a sibling fixed in this cone on 2026-09-07
(commit 87bf88379).  Series coefficients are exact `Fraction`s.
"""
from __future__ import annotations

import datetime
import json
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools/qou-substrate/python"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mpmath import log, mp, mpf, nstr  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.dps = 60

# --- inputs, both from the corpus -------------------------------------------------
BOND = {
    "pp": [F(1, 2), F(1), F(1, 4), F(-1, 4), F(1, 8), F(0)],
    "pn": [F(1, 2), F(0), F(3, 4), F(-3, 4), F(31, 24), F(-5, 2)],
    "nn": [F(1, 2), F(-1), F(5, 4), F(-5, 4), F(9, 8), F(-1)],
}
R_MEASURED = F(950815, 1483044)          # CarrierCrossingQuantisation.rMeasured
TARGET = 1 + R_MEASURED                  # #7097 kindRatio_forced_at_minimal_carrier


def _f(x: F):
    return mpf(x.numerator) / mpf(x.denominator)


def ev(coeffs: list[F], eps, K: int):
    return sum(_f(c) * eps ** i for i, c in enumerate(coeffs[: K + 1]))


def _head_sha() -> str:
    """Repo HEAD at emission time, as the provenance audit expects (40-char sha).

    Returns the empty string when git is unavailable or this is not a checkout;
    the audit reads a missing/blank value as missing, which is the honest state.
    """
    try:
        return subprocess.run(
            ["git", "-C", str(Path(__file__).resolve().parent), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def main() -> int:
    q = Q_MP
    eps = q - 1
    pp, pn, nn = (ev(BOND[k], eps, 5) for k in ("pp", "pn", "nn"))
    tgt = _f(TARGET)
    r = _f(R_MEASURED)

    print(f"  q0  = {nstr(q, 25)}   (Q_50_DIGIT_STR)")
    print(f"  eps = q0 - 1 = {nstr(eps, 25)}")
    print(f"  bond_pp {nstr(pp,12)}   bond_pn {nstr(pn,12)}   bond_nn {nstr(nn,12)}\n")

    cands = [
        ("A multiplicative  pp/pn", pp / pn),
        ("B ADDITIVE (log)  log pp / log pn", log(pp) / log(pn)),
        ("C shifted additive 1 + (log pp - log pn)", 1 + (log(pp) - log(pn))),
        ("D inverse         pn/pp", pn / pp),
    ]
    print(f"  TARGET rho_pp = 1 + rMeasured = {nstr(tgt,12)}\n")
    print(f"  {'identification':<44}{'rho_pp':<16}miss %")
    rows = []
    for name, v in cands:
        miss = abs(v - tgt) / tgt * 100
        rows.append((name, v, miss))
        print(f"  {name:<44}{nstr(v,10):<16}{nstr(miss,5)}")

    # carrier scan -- a BOUND, not a carrier determination
    print("\n  carrier scan (3He = ppn, pairs pp/pn/pn), m in 1..6:")
    scan = {}
    for name, rho in (("A", pp / pn), ("B", log(pp) / log(pn))):
        best = None
        for m_pp in range(1, 7):
            for m_pn in range(1, 7):
                val = m_pp * rho + 2 * m_pn - 3
                d = abs(val - r)
                if best is None or d < best[0]:
                    best = (d, m_pp, m_pn, val)
        d, m_pp, m_pn, val = best
        scan[name] = (m_pp, m_pn, d / r * 100)
        print(f"    {name}: best (m_pp,m_pn)=({m_pp},{m_pn})  b3/b2={nstr(val,10)}  "
              f"closest miss {nstr(d/r*100,6)} %")
    print("    uniform (rho=1) reference miss: 55.98 %")

    a = [
        ("the derived kind weight does NOT reach the target under ANY identification tried",
         all(m > 5 for _, _, m in rows)),
        ("the PRINCIPLED (log/additive) identification misses by more than 50%",
         rows[1][2] > 50),
        ("the closest identification is NOT the principled one -- so reporting it "
         "would be selection against the target", rows[0][2] < rows[1][2]),
        ("no carrier m in 1..6 closes it under either identification",
         scan["A"][2] > 5 and scan["B"][2] > 5),
        ("under the MULTIPLICATIVE reading the kind weight is WORSE than uniform",
         scan["A"][2] > 55.98),
        ("under the PRINCIPLED reading it IMPROVES on uniform but does not close",
         5 < scan["B"][2] < 55.98),
        ("bond_pp > bond_pn: the SIGN of the kind-dependence is right, the magnitude is not",
         pp > pn),
    ]
    print("\n  assertions:")
    ok = True
    for name, passed in a:
        ok &= bool(passed)
        print(f"    [{'PASS' if passed else 'FAIL'}] {name}")

    w = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        # Provenance triple required by computations/audits/witness_provenance_audit.py
        # (REQUIRED_FIELDS = engine, scriptFile, commitSha). This probe hand-builds its
        # witness rather than going through WitnessBuilder, so the triple is emitted here.
        "engine": "mpmath",
        "scriptFile": Path(__file__).name,
        "commitSha": _head_sha(),
        "q0Anchor": "proton",
        "q0AnchorReason": "seeded from Q_50_DIGIT_STR; the bond series are in eps = q - 1",
        "description": (
            "Takes over qou-qqm4's unanswered target from #7097 and computes rho_pp "
            "INDEPENDENTLY from the corpus's derived kind-dependent bond factors, then "
            "compares. The answer is NO under all four identifications tried, and the "
            "PRINCIPLED one (log/additive, which the binding law B = E0*log(tr ratio) "
            "implies) misses worst at 55.9%. No carrier m in 1..6 closes it. The escape "
            "from BrunnianTripleExhaustion is real structurally and far too weak "
            "quantitatively. Nothing is fitted; the closest identification is reported "
            "as such and NOT adopted as the answer."),
        "free_parameters": 0,
        "inputs": {
            "bond_series_eps": {k: [str(c) for c in v] for k, v in BOND.items()},
            "bond_series_source": "computations/probes/bond_pn_kind_order_four_discriminator_probe.py",
            "rMeasured": str(R_MEASURED),
            "target_rho_pp": str(TARGET),
        },
        "bond_values_at_q0": {"pp": nstr(pp, 30), "pn": nstr(pn, 30), "nn": nstr(nn, 30)},
        "identifications": [
            {"id": n, "rho_pp": nstr(v, 30), "miss_pct": nstr(m, 8)} for n, v, m in rows
        ],
        "carrier_scan": {
            k: {"best_m_pp": v[0], "best_m_pn": v[1], "closest_miss_pct": nstr(v[2], 8)}
            for k, v in scan.items()
        },
        "uniform_reference_miss_pct": "55.98",
        "assertions": [{"name": n, "passed": bool(p)} for n, p in a],
        "allPassed": bool(ok),
    }
    out = Path(__file__).with_name("rho-pp-kind-weight-does-not-close-b3.witness.json")
    out.write_text(json.dumps(w, indent=1) + "\n")
    print(f"\n  witness -> {out.relative_to(Path(__file__).resolve().parents[2])}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
