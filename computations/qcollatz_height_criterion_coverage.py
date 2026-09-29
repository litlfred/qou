#!/usr/bin/env python3
"""How much of the q-Collatz word space does the height criterion exclude?

Enabled by the exact closed form proved in
folio/quantum-observable-universe/lean/QOU/AppendixSurreals/collatz_general_word.lean
(`wordNum_map_closed`):

    phi(n_w) = sum_{i<k, w i} 3^(#odd steps after i) * 2^i

and the exclusion `qcollatz_no_cycle_of_height_lt`: a period-k cycle on the
parity word w is impossible when

    0 < S_w  and  S_w < D_w := 2^k - 3^m,      m = #odd steps.

Before the closed form there was no way to evaluate that criterion for a general
word -- only for the two shape-restricted families (adjacent-tail, front-loaded).
This probe evaluates it for EVERY word up to a given length and reports how far
the criterion reaches, which is the honest measure of the distance between
"criterion" and "theorem".

Four disjoint classes per word:
  ALL_EVEN     m = 0. Excluded separately (qcollatz_alleven_forces_zero); the
               criterion does not apply and does not need to.
  D_NONPOS     2^k <= 3^m, so the denominator height is not positive. The
               criterion as stated cannot fire. These are the "too many odd
               steps to contract" words.
  S_TOO_LARGE  0 < D_w but S_w >= D_w. The criterion is evaluable and FAILS.
               This is where the open problem lives.
  EXCLUDED     0 < S_w < D_w. The criterion fires; no cycle on this word.

Exact integer arithmetic throughout (Python ints); no float anywhere.
Exploratory research probe (NOT canonical production).
"""
import sys, json
from fractions import Fraction
from pathlib import Path  # witness path must be FILE-relative, not cwd-relative

try:  # P30 provenance stamp; optional so a bare container still runs
    from qou_substrate.witness import WitnessBuilder as _WitnessBuilder
except ImportError:  # pragma: no cover
    from witness_base import WitnessBuilder as _WitnessBuilder


def word_height(bits, k):
    """S_w = sum_{i<k, w i} 3^(#odd after i) * 2^i, exactly."""
    total = 0
    odd_after = 0
    for i in range(k - 1, -1, -1):          # walk right-to-left
        if (bits >> i) & 1:
            total += (3 ** odd_after) * (2 ** i)
            odd_after += 1
    return total, odd_after                  # odd_after ends as m


def classify(bits, k):
    S, m = word_height(bits, k)
    if m == 0:
        return 'ALL_EVEN', m, S, None
    D = 2 ** k - 3 ** m
    if D <= 0:
        return 'D_NONPOS', m, S, D
    if S >= D:
        return 'S_TOO_LARGE', m, S, D
    return 'EXCLUDED', m, S, D


def run(kmax=18):
    from collections import Counter
    per_k = {}
    for k in range(1, kmax + 1):
        tally = Counter()
        surv_m = Counter()          # m-distribution of S_TOO_LARGE survivors
        max_excluded_m = 0
        for bits in range(2 ** k):
            cls, m, S, D = classify(bits, k)
            tally[cls] += 1
            if cls == 'S_TOO_LARGE':
                surv_m[m] += 1
            elif cls == 'EXCLUDED':
                max_excluded_m = max(max_excluded_m, m)
        total = 2 ** k
        # the m at which the denominator first goes non-positive: 2^k <= 3^m
        m_crit = next(m for m in range(0, k + 2) if 2 ** k <= 3 ** m)
        per_k[k] = dict(
            total=total,
            tally=dict(tally),
            excluded_frac=str(Fraction(tally['EXCLUDED'], total)),
            evaluable=tally['EXCLUDED'] + tally['S_TOO_LARGE'],
            excluded_frac_of_evaluable=(
                str(Fraction(tally['EXCLUDED'],
                             tally['EXCLUDED'] + tally['S_TOO_LARGE']))
                if (tally['EXCLUDED'] + tally['S_TOO_LARGE']) else None),
            max_m_excluded=max_excluded_m,
            m_denominator_nonpositive_from=m_crit,
            survivor_m_histogram=dict(sorted(surv_m.items())),
        )
        sys.stderr.write(f"[progress] k={k} {dict(tally)}\n")
        sys.stderr.flush()
    return per_k


if __name__ == '__main__':
    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 18

    # sanity: the adjacent-tail extreme O^m E^{k-m} must have height 3^m - 2^m,
    # and the reversed extreme E^{k-m} O^m must have 3^m 2^(k-m) - 2^k.
    for (m, k) in ((3, 9), (4, 11), (5, 13)):
        # bit i of `bits` is step i, so "early steps" = low indices
        early_bits = sum(1 << j for j in range(m))
        late_bits = sum(1 << (k - 1 - j) for j in range(m))
        Se, me = word_height(early_bits, k)
        Sl, ml = word_height(late_bits, k)
        assert me == m and ml == m
        assert Se == 3 ** m - 2 ** m, (m, k, Se, 3 ** m - 2 ** m)
        assert Sl == 3 ** m * 2 ** (k - m) - 2 ** k, (m, k, Sl)
    print("sanity OK: both extremes reproduce the proved bounds")

    r = run(kmax)
    for k, d in r.items():
        t = d['tally']
        print(f"k={k:2d} total={d['total']:7d} "
              f"EXCLUDED={t.get('EXCLUDED',0):7d} "
              f"S_TOO_LARGE={t.get('S_TOO_LARGE',0):7d} "
              f"D_NONPOS={t.get('D_NONPOS',0):7d} "
              f"ALL_EVEN={t.get('ALL_EVEN',0):2d} "
              f"| excl/evaluable={d['excluded_frac_of_evaluable']} "
              f"max_m_excluded={d['max_m_excluded']}")

    w = {
        'schema': 'qou-probe/v0',
        'description': ('Coverage of the q-Collatz height-criterion exclusion '
                        '(qcollatz_no_cycle_of_height_lt) over ALL parity words '
                        'up to length k, using the exact closed form '
                        'wordNum_map_closed. Exact integer arithmetic. '
                        'Exploratory research probe (NOT canonical production).'),
        'criterion': '0 < S_w < 2^k - 3^m  excludes a period-k cycle on word w',
        'closed_form': 'S_w = sum_{i<k, w i} 3^(#odd after i) * 2^i',
        'classes': {
            'ALL_EVEN': 'm=0; excluded separately by qcollatz_alleven_forces_zero',
            'D_NONPOS': '2^k <= 3^m; denominator height not positive, criterion cannot fire',
            'S_TOO_LARGE': 'criterion evaluable but fails -- where the open problem lives',
            'EXCLUDED': 'criterion fires',
        },
        'result': r,
    }
    with open(Path(__file__).with_name('qcollatz_height_criterion_coverage.witness.json'), 'w') as f:
        w["q0Anchor"] = "independent"
        # P30: add the staleness provenance (scriptHash / commitSha /
        # engine) that a hand-rolled dump cannot get from build().
        # The q0Anchor lines just below own the anchor decision and run
        # after this, so their value stands.
        _WitnessBuilder.stamp_staleness_metadata(
            w, script_path=__file__, engine="python")
        w["q0AnchorReason"] = "No substrate pin enters this computation: neither the producer nor its transitive import cone inside computations/ references q_at, q_muon_at, Q_50_DIGIT_STR, q_parameter or resolve_q0_anchor outside comments (AST import-cone walk, 2026-09-03). The probe computes: How much of the q-Collatz word space does the height criterion exclude?."
        json.dump(w, f, indent=2)
    print("wrote qcollatz_height_criterion_coverage.witness.json")
