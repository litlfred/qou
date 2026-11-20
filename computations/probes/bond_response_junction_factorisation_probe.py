#!/usr/bin/env python3
"""
qou-ales step 11 (mechanism) — the bond response is one-body BECAUSE of connected-sum
multiplicativity across the single shared strand, not because of anything about nucleons.

The sibling probe `two_nucleon_bond_response_arity_probe` measures that the interface bond's
trace response is a function of the nucleon it borrows a generator from alone (r_pp = r_np and
r_nn = r_pn at a right-borrowing vertex, mirrored at a left-borrowing one). Four species
combinations cannot distinguish a mechanism from a coincidence. This probe does.

THE MECHANISM, which is the corpus's own and is cited rather than discovered here.
`folio/quantum-observable-universe/mass-theory/canonical-trace-factorises-over-chain.md`:

    "a closed braid whose word is a product of sub-words on strand sets overlapping in one
     strand is a connected sum, and the Markov trace -- like every multiplicative link
     invariant -- is multiplicative under connected sum"

and its own status note records that the connected-sum multiplicativity itself is NOT
FORMALISED. Applied here: W_1 lies in <s0,s1> (strands 1-3); W_2 and a right-borrowing bond
both lie in <s2,s3,s4> (strands 3-6). The two strand sets overlap in ONE strand, strand 3, so

    tr_M(W_1 . W_2 . G^3) = tr_M(W_1) . tr_M(W_2 . G^3)

the left factor cancels in the ratio, and the response depends on W_2 alone -- for ANY W_1
whatever, not merely for a proton or a neutron.

NOTE WHAT THIS IS NOT. `QOU.MathlibExt.MarkovTraceMultiplicative` models the DISJOINT UNION,
and bean qou-bsfg exists because the two were once conflated. In this geometry the FREE
two-nucleon trace is a disjoint union (supports {0,1} and {3,4} share no strand) while the
BONDED one is a connected sum (the bond reaches across strand 3). Different properties; the
sibling probe asserts the first, this one probes the second.

AND WHAT THE CHAIN PRODUCT FORMULA DOES NOT COVER. That same block gives a per-generator
product formula for words in CHAIN FORM -- one polynomial per generator in Coxeter order --
and says explicitly that interleaved bonds "destroy the chain form". G^3 = s2 s3^-1 s2 s3^-1
s2 s3^-1 IS interleaved, so the product formula does not apply to it. What this probe shows is
that the JUNCTION factorisation survives the interleaving even though the chain form does not.
That is the refinement; the principle is not new.

THE TEST. Hold the right nucleon fixed (a neutron on <s3,s4>) and the bond fixed
(V1^3 = (s2 s3^-1)^3), and vary the LEFT word over words on <s0,s1> chosen to be nothing like
a nucleon: the empty word, a single letter, an all-positive word, an inverse-heavy word, an
averaged-heavy word. Every response must be the SAME RATIONAL FUNCTION, as a symbolic
identity. A species-only coincidence would not survive the empty word.

## Precision
Exact sympy over Q(q); mpmath at 60 dps for display only. No float64 anywhere. Nothing here
reads AME2020, a CODATA binding value, or a census.

## Cost
~5 min wall (24 symbolic H_6 characters).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/hecke", "computations/markov",
           "computations/substrate", "tools/pyhecke/python", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_symbolic import Q, chi_lambda_symbolic  # noqa: E402
from markov_weights_symbolic import solve_y_lambda  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

DPS = 60
set_compute_dps(DPS)

BOND = [(2, "sigma"), (3, "sigma_inv")] * 3   # V1^3, the canonical right-borrowing bond


def nucleon(kind: str, g0: int) -> list[tuple[int, str]]:
    """The canonical 11-letter nucleon element on generators (g0, g0+1)."""
    g1 = g0 + 1
    w: list[tuple[int, str]] = []
    for _ in range(3):
        w += [(g0, "sigma"), (g1, "sigma_inv")]
    if kind == "p":
        w += [(g0, "sigma"), (g0, "averaged"), (g1, "averaged")]
    else:
        w += [(g0, "averaged"), (g0, "averaged"), (g1, "sigma_inv")]
    w += [(g0, "sigma"), (g0, "sigma")]
    return w


# Left words on <s0, s1>, deliberately unlike a nucleon.
LEFTS: dict[str, list[tuple[int, str]]] = {
    "nucleon_p_reference": nucleon("p", 0),
    "empty": [],
    "single_sigma_0": [(0, "sigma")],
    "inverse_heavy": [(1, "sigma_inv"), (0, "sigma"), (1, "sigma_inv")],
    "all_positive_len5": [(0, "sigma"), (1, "sigma"), (0, "sigma"), (1, "sigma"), (0, "sigma")],
    "averaged_heavy": [(0, "averaged"), (1, "averaged"), (0, "averaged"), (1, "sigma_inv")],
}


def main() -> int:
    t0 = time.time()
    q = Q_MP
    qv = sp.Rational(Q_50_DIGIT_STR)
    h2_sym = sp.cancel((Q - 1 / Q) ** 2)

    print(f"qou-ales step 11 mechanism — junction factorisation (proton pin, {DPS} dps)")
    print(f"  q_0 = {mp.nstr(q, 20)}")
    y6 = solve_y_lambda(6)
    support = sorted((lam for lam in y6 if sp.cancel(y6[lam]) != 0), key=len)
    print(f"  convention-D weight support at H_6: {support}")
    print("  right nucleon FIXED at n on <s3,s4>; bond FIXED at V1^3 on <s2,s3>;"
          " LEFT word varied")

    right = nucleon("n", 3)

    def trM(word):
        tot = sp.Integer(0)
        for lam in support:
            tot += sp.cancel(y6[lam] * sp.cancel(chi_lambda_symbolic(lam, word)))
        return sp.cancel(sp.together(tot))

    rows: dict[str, dict] = {}
    ref_r: sp.Expr | None = None
    print(f"\n  {'left word':>22}{'len':>5}{'ratio at q0':>26}{'r at q0':>24}  identical?")
    for label, lw in LEFTS.items():
        t1 = time.time()
        tf = trM(lw + right)
        ta = trM(lw + right + BOND)
        ratio = sp.cancel(ta / tf)
        r = sp.cancel((ratio - 1) / h2_sym)
        if ref_r is None:
            ref_r = r
            dev = sp.Integer(0)
        else:
            dev = sp.simplify(r - ref_r)
        rows[label] = {
            "left_len": len(lw),
            "ratio_at_q0": fmt(mp.mpf(str(sp.N(ratio.subs(Q, qv), DPS + 10)))),
            "r_at_q0": fmt(mp.mpf(str(sp.N(r.subs(Q, qv), DPS + 10)))),
            "dev_from_reference": sp.sstr(dev),
        }
        print(f"  {label:>22}{len(lw):>5}{sp.N(ratio.subs(Q, qv), 20):>26}"
              f"{sp.N(r.subs(Q, qv), 18):>24}  {dev == 0}   ({time.time() - t1:.0f}s)",
              flush=True)

    all_identical = all(rows[k]["dev_from_reference"] == "0" for k in rows)
    empty_identical = rows["empty"]["dev_from_reference"] == "0"
    print(f"\n  every left word gives the SAME response : {all_identical}")
    print(f"  including the EMPTY left word           : {empty_identical}")
    print("  => the response is independent of the entire left word, which is what"
          " connected-sum\n     multiplicativity across the single shared strand predicts and"
          " what a species-only\n     coincidence would not give.")

    elapsed = time.time() - t0
    print(f"\n  wall {elapsed:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("bond-response-junction-factorisation-probe", engine="python",
                       start_time=t0)
    w.set_description(
        "qou-ales step 11 mechanism: shows the interface bond's trace response is one-body "
        "BECAUSE of connected-sum multiplicativity across the single shared strand, not because "
        "of anything about nucleon species. Holding the right nucleon and the bond fixed and "
        "varying the LEFT word over six words on <s0,s1> unlike a nucleon -- including the EMPTY "
        "word -- leaves the response a symbolic identity. The mechanism is the corpus's own, "
        "stated in mass-theory/canonical-trace-factorises-over-chain.md, whose status note "
        "records that the connected-sum multiplicativity itself is NOT formalised; so this "
        "derives the one-body premise from a cited principle rather than a species table, and "
        "does not promote anything to scope-(b). Distinct from MarkovTraceMultiplicative, which "
        "models the DISJOINT union (qou-bsfg): the free two-nucleon trace is a disjoint union, "
        "the bonded one a connected sum. Refinement worth noting: that block's per-generator "
        "product formula needs CHAIN FORM and says interleaved bonds destroy it -- G^3 IS "
        "interleaved, and the junction factorisation survives anyway. No AME/CODATA binding "
        "value or census read.")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (z = q^3/(q^2+1); two-row weight support at H_6)")
    w.add_parameter("dps", DPS)
    w.add_parameter("bond", "V1^3 = (sigma_2 sigma_3^-1)^3 on generators (2,3)")
    w.add_parameter("right_nucleon", "n, 11-letter canonical element on generators (3,4)")
    w.add_parameter("left_parabolic", "<sigma_0, sigma_1> (strands 1-3); shares strand 3 with "
                                     "<sigma_2, sigma_3, sigma_4> (strands 3-6)")
    for label, d in rows.items():
        w.add_data(f"left_{label}", d)
    w.add_assertion(name="response_independent_of_entire_left_word",
                    computed=str(int(all_identical)), expected="1", tolerance="0",
                    source="six unrelated left words give the same rational function exactly")
    w.add_assertion(name="response_unchanged_by_empty_left_word",
                    computed=str(int(empty_identical)), expected="1", tolerance="0",
                    source="the sharpest case: no left word at all, same response")
    for label in rows:
        if label == "nucleon_p_reference":
            continue
        w.add_assertion(name=f"left_word_{label}_gives_identical_response",
                        computed=rows[label]["dev_from_reference"], expected="0", tolerance="0",
                        source="symbolic deviation from the nucleon-p reference response")
    out = w.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
