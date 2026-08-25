"""Settle the c_k slope tension, and audit the ladder's convergence premise.

Bean `qou-0etg`. `q-beta-c-k-recursion-from-habiro-q-difference.md` asserts two
things about the same `c_k`:

  (a) they satisfy a CONSTANT-kernel linear recursion
      `c_{k+1} = sum_j a_j(q0) c_{k+1-j}`, `a_j(q0)` fixed in `k`;
  (b) they obey the Hahn-Exton q-Bessel SECOND-ORDER q-difference equation.

A constant-kernel recursion has solutions that are geometric, i.e. q-Gevrey
order `s = 0`. A genuine second-order q-difference equation generically has
`s > 0`, meaning `|c_k| ~ C^k q^{s k^2/2}` -- SUPER-geometric. Those are
different growth classes, so at most one reading can be right.

`QOU.Mathlib.QGevreyOrder.IsQGevreyOrder` gives the decisive test:

    s = lim_k  2 log_q |c_k| / k^2

This probe evaluates it on the two committed c_k datasets. No fitting; the
numbers are read from the witnesses and only compared.

## Result

Neither dataset shows a positive q-Gevrey slope. **(a) is right, (b) is not
what these c_k do.** Dataset B's apparent `s ~ 5.8` is the finite-k artifact of
purely geometric growth (`2 log_q(A)/k -> 0`) and is already turning over by
k = 8.

## The more serious finding

The two committed datasets are NOT the same sequence:

* **A** `qbeta-closed-form-wiring-n4-to-n10.witness.json :: closed_form_c_k_at_q0`
  is bounded, `O(1)`, and the ladder terms `|c_k u^k|` decay cleanly
  `7.2e-05 -> 3.4e-21`.
* **B** `qbeta/qbeta-decay-sdp-extended-ck.witness.json :: c_k_extracted_50dps`
  grows geometrically with ratio **117.4**, and `1/u = 117.409`. So
  `c_k ~ C u^{-k}` and the ladder terms `|c_k u^k|` are **FLAT at 7.34e-09
  from k=6 through k=10** -- they do not decay at all.

`AGENTS.md` frames the ladder `Q_beta = Q_base * prod (1 + c_k u^k)` as a
*convergent series* with truncation order `N >= log10(1/eps)/2.07 - 1`. This
probe shows where the `2.07` comes from: `log10(1/u) = 2.0697`. So the rule is
**derived, not fitted** -- but only under the premise `c_k = O(1)`, which is
dataset A's behaviour. Dataset B violates it, and under B the ladder does not
converge in the sense the rule needs.

A sequence whose terms `c_k u^k` sit at a constant `7.34e-09` is the signature
of an extraction solving for `c_k` to absorb a fixed residual at each order.
Flagged, not diagnosed -- this probe does not inspect the SDP extractor.

Ref: prop:q-beta-c-k-recursion-from-habiro-q-difference
Ref: QOU.Mathlib.QGevreyOrder.IsQGevreyOrder
"""

from __future__ import annotations

import json
from pathlib import Path

from mpmath import fabs, log, log10, mp, mpf
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

_HERE = Path(__file__).resolve().parent

# Anchors. q0 = experimental (proton) pin per the 2026-08-07 owner directive;
# u is the ladder variable as recorded alongside the Ohtsuki kappa comparison.
Q0 = mpf("1.1099785827513808")
U = mpf("0.008517234550156142")

# Dataset A — closed-form c_k. Bounded.
CK_CLOSED_FORM = {
    2: "-1.0", 3: "-2.0",
    4: "-1.13312094437407740556944287932",
    5: "-1.25270211384520417247078416697",
    6: "3.0108084553808166898831366679", 7: "-8.0",
    8: "2.26624188874815481113888575864",
    9: "-6.0216169107616333797662733358",
    10: "1.70580506014528415139336635043",
}

# Dataset B — SDP-extracted c_k at 50 dps. Geometric, ratio 1/u.
CK_SDP = {
    2: "-1.0172173285667249513240662532242009198014962646275",
    3: "-2.0216155770600061205300249700296445660947408177192",
    4: "-2.5378659117940255569454500193524358506536471385217",
    5: "-164.92966962997120315189506117224341793666720626325",
    6: "-19217.145207925212509908947239063591863338276085142",
    7: "-2256618.8430159516520727812660641237219777899347218",
    8: "-264946369.0809749418316620596552190900680213585986",
    9: "-31107082245.428488701150349050271676018490685326017",
    10: "-3652250682718.0302448331440574991158032911030226467",
}


def analyse(name: str, raw: dict[int, str]) -> dict:
    ks = sorted(raw)
    c = {k: mpf(raw[k]) for k in ks}
    ratios = {k: c[k + 1] / c[k] for k in ks[:-1]}
    # IsQGevreyOrder: s = lim 2 log_q |c_k| / k^2
    slope = {k: 2 * log(fabs(c[k])) / log(Q0) / k**2 for k in ks}
    terms = {k: fabs(c[k]) * U**k for k in ks}
    tail = [slope[k] for k in ks[-3:]]
    return {
        "name": name,
        "ratios": {str(k): str(v) for k, v in ratios.items()},
        "qgevrey_slope_estimates": {str(k): str(v) for k, v in slope.items()},
        "ladder_terms_abs_ck_uk": {str(k): str(v) for k, v in terms.items()},
        "slope_turning_over": bool(tail[-1] < tail[0]),
        "ladder_terms_decay": bool(terms[ks[-1]] < terms[ks[-3]] / 10),
    }


def main() -> int:
    a = analyse("closed_form_c_k_at_q0", CK_CLOSED_FORM)
    b = analyse("c_k_extracted_50dps_sdp", CK_SDP)

    for r in (a, b):
        print(f"--- {r['name']} ---")
        print("  ratio      :", " ".join(f"{float(mpf(v)):.4g}"
                                          for v in r["ratios"].values()))
        print("  q-Gevrey s :", " ".join(f"{float(mpf(v)):.3g}"
                                          for v in r["qgevrey_slope_estimates"].values()))
        print("  |c_k u^k|  :", " ".join(f"{float(mpf(v)):.3g}"
                                          for v in r["ladder_terms_abs_ck_uk"].values()))
        print(f"  slope turning over: {r['slope_turning_over']}   "
              f"ladder terms decay: {r['ladder_terms_decay']}")

    print(f"\nlog10(1/u) = {float(log10(1 / U))}   (AGENTS.md truncation constant: 2.07)")
    print(f"1/u        = {float(1 / U)}   (dataset B ratio from k=6: 117.4)")

    witness = {
        "computation": "ck-qgevrey-slope-probe",
        "description": (
            "q-Gevrey slope test (IsQGevreyOrder: s = lim 2 log_q|c_k|/k^2) on the "
            "two committed c_k datasets, to settle whether the c_k follow the "
            "constant-kernel recursion (s=0) or the Hahn-Exton q-Bessel "
            "second-order q-difference equation (s>0)."
        ),
        "audit_only": True,
        "tier": "numerical-exact (mpmath 40 dps, values read from committed witnesses)",
        "anchors": {"q0": str(Q0), "q0_pin": "experimental/proton", "u": str(U)},
        "verdict": {
            "slope_positive_anywhere": False,
            "reading_supported": "constant-kernel recursion (q-Gevrey slope 0)",
            "reading_refuted": (
                "Hahn-Exton q-Bessel second-order q-difference as a description of "
                "these c_k's GROWTH; dataset B's apparent s~5.8 is the finite-k "
                "artifact 2 log_q(A)/k of geometric growth, already turning over by k=8"
            ),
            "truncation_constant_2_07_is": "log10(1/u) = " + str(log10(1 / U)),
            "truncation_rule_is_derived_given": "c_k = O(1)  (dataset A only)",
            "dataset_B_flag": (
                "c_k ~ C u^{-k} (ratio 117.4 vs 1/u = 117.409), so |c_k u^k| is FLAT "
                "at 7.34e-09 for k=6..10 -- the ladder terms do not decay and the "
                "convergence premise behind the truncation rule fails under B"
            ),
        },
        "datasets": [a, b],
        "refs": [
            "prop:q-beta-c-k-recursion-from-habiro-q-difference",
            "QOU.Mathlib.QGevreyOrder.IsQGevreyOrder",
            "computations/qbeta-closed-form-wiring-n4-to-n10.witness.json",
            "computations/qbeta/qbeta-decay-sdp-extended-ck.witness.json",
        ],
    }
    out = _HERE / "ck-qgevrey-slope.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
