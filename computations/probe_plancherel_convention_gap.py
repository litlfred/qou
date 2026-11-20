#!/usr/bin/env python3
"""probe_plancherel_convention_gap.py — the balanced-convention
q-Plancherel normalization gap, and what it does to cross-atom variance.

THE FINDING (bean qou-7o7h).  The textbook q-Plancherel weight

    w(lambda) = dim_q(lambda)^2 / [n]_q!

is a probability measure at q = 1 -- and at q = 1 ONLY.

CORRECTED 2026-09-05.  This docstring first said it is also a measure
"in the *asymmetric* q-integer convention", i.e. that the failure was a
convention artifact.  That was WRONG and is retracted.  Measured at the
proton q0, mp.dps = 60, with a q -> 1 control returning exactly 1.0 in
both conventions (so both implementations are sound):

    n     balanced [k]=(q^k-q^-k)/(q-q^-1)     asymmetric [k]=(q^k-1)/(q-1)
    3            0.987440229774                      0.914969211488
    4            0.982165323836                      0.882874426585
    5            0.982224148283                      0.868254573821
    6            0.991079523637                      0.874641716553
    9            1.11092313496                       1.04636760337
   12            1.51713321377                       1.6902849181

The asymmetric convention is FURTHER from 1 at five of those six n
(n = 9 is the exception).  So the defect is STRUCTURAL, not a
convention artifact: the q-deformation breaks the Burnside identity
Sum_lambda (f^lambda)^2 = n! that made the classical form a measure at
all, and no choice of q-integer convention restores it.

WHAT THE CORRECT q-DEFORMATION LOOKS LIKE (and it is already in the
corpus, Lean-proved unconditional for all n and all q > 1):

    Sum_{lambda |- n} f^lambda * q^{-kappa_lambda} * dim_q(lambda)
        = [n]_q!
    -- QOU/MathlibExt/NormalizedSumUnconditional.lean:45-50
       (molienSum_eq_qFactorial, axioms clean, no sorryAx)

i.e. the right q-lift of Sum (f^lambda)^2 = n! replaces ONE factor with
a quantum dimension, not both.  dim_q^2 is a misuse of dim_q where one
dim_q and one f^lambda belong -- at generic q, H_n(q) ~= C[S_n], so the
Wedderburn BLOCK DIMENSIONS are the classical f^lambda; dim_q is a
QUANTUM dimension, a different object.  The same statement appears in
the held literature as Feray-Meliot's q-Plancherel measure
M_{n,q}(lambda) = D_lambda(q)*dim(lambda)/{n!}_q, which sums to 1
exactly at every n (library/arxiv-1001.2180v2, sec-006-13-tools.md).

The defect is not small and it is not constant: c_n = Sum_lambda
dim_q^2/[n]_q! runs

    n =  6 (A=2):  0.991...      n =  9 (A=3):  1.111...
    n = 12 (A=4):  1.517...

so it grows with n.  Simple q^{+-2 n(lambda)} and q^{+-(n(lambda) -
n(lambda'))} prefactors do not close it (checked; see the audit doc).

WHY IT MATTERS — it is a CROSS-ATOM artifact, not a per-atom one.
Because w_textbook = c_n * w_selfnormalized EXACTLY, and the binding
functional B = Sum_k alpha_k (Phi_k^free - Phi_k^atom) is LINEAR in the
weights, B scales by exactly c_n.  Within one atom the factor cancels
out of any ratio.  Across atoms it does not, because n = 3A differs:
the light series spans n = 6, 9, 9, 12 and therefore three different
c_n.  Any metric that COMPARES atoms — the max/min "variance" the FR
probes are judged by — is distorted by the spread of c_n.

MEASURED CONSEQUENCE.  The FR-pullback family's published baseline
variance of 1.82x is ~53% inflated by this artifact alone.  Feeding the
self-normalized per-atom ratios through the scaling law reproduces the
textbook-normalized run to 5.5e-5 relative (that residual is the
4-significant-figure rounding of the recorded ratios, nothing else):

    atom   ratio_selfnorm   x c_n      = ratio_textbook
    D      0.2753           0.99108      0.27284
    T      0.2980           1.11092      0.33106
    3He    0.3094           1.11092      0.34372
    4He    0.3276           1.51713      0.49701
                       max/min ->        1.8216   (recorded run: 1.8217)
                                     vs  1.1901   self-normalized

A TRAP, RECORDED BECAUSE I FELL INTO IT.  It is tempting to notice that
1.8217/1.1901 = 1.5307 equals c_12/c_6 = 1.5308 and call that the
mechanism.  That identity is real but CONDITIONAL: it holds only because
the argmax atom (4He, largest c_n) and argmin atom (D, smallest c_n) are
the same under both normalizations.  Change the atom set, or move a
ratio enough to swap the argmax, and the shortcut breaks while the
scaling law below still holds.  Quote the scaling law, not the ratio
identity.  (I also first tested the law with the factor INVERTED —
dividing by c_n instead of multiplying — got 1.290 against a recorded
1.8217, and nearly wrote the whole mechanism off as coincidence.)

WHAT THE SELF-NORMALIZED FORM ACTUALLY IS (upgraded 2026-09-05).  It is
not merely "normalized by construction", which is the weak defence this
docstring first gave.  dim_q^2/Sum_mu dim_q^2 = d_q^2/D^2 is the
**Reshetikhin-Turaev / Verlinde Plancherel measure** of a modular tensor
category, with D^2 = Sum_lambda d_q^2 the total quantum dimension
squared.  The corpus derived that D^2 -- not [n]_q! -- is the
geometrically forced normalizer: an index/partition function is a trace
over a Hilbert space and is normalized by that space's total dimension,
and [n]_q! is merely the q = 1 value of D^2
(docs/audits/2026-06-20-keystone-wlambda-beasley-witten-localization.md,
citing Beasley-Witten Seifert-CS localization, hep-th/0503126).  It is
Lean-proved sorry-free that the two differ by a single lambda-INDEPENDENT
global factor (QOU/BraidKnot/WLambdaNormalizationInvariance.lean:
wPlanch_eq_global_factor, ratio_invariant), which is the same statement
this probe measures numerically as the c_n scaling law.

WHAT IT STILL DOES NOT CLAIM.  That d_q^2 is the right NUMERATOR.  Being
a probability measure does not make it the right weight, and bean
qou-sf1t states the point sharply: normalizing a family by its own sum
gives total mass one BY CONSTRUCTION and is "NOT evidence that
Sum_lambda d_q(lambda)^2 is the canonical normaliser for the Ocneanu
weights".  Whether Phi_k should instead carry the Molien weight
f^lambda * dim_q(lambda) (exactly normalized, Lean-proved) or the Markov
weights y_lambda (Sum_lambda y_lambda f^lambda = 1, the corpus's
canonical Frobenius pairing) is OPEN -- bean qou-mnsr.  Note a corpus
ruling against a naive swap to y_lambda: y_lambda is signed and
row-capped where d_q^2/[n]_q! is conjugation-symmetric, and
2026-06-16-keystone-plancherel-target-clarification.md says "do not
bridge them".

The claim here is narrower and firmer than any of that: the two choices
differ by a KNOWN, n-DEPENDENT factor, so figures computed under one are
not comparable to figures computed under the other, and the corpus
currently contains both.

Ref: prop:plancherel-term-7-formulation
Bean: qou-7o7h.  Registry: docs/coordination/trace-convention-registry.md row B.

Usage:
    python3 -u probe_plancherel_convention_gap.py
"""
from __future__ import annotations

import os
import sys
import time
from functools import lru_cache

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import _path_bridge  # noqa: F401,E402  (sys.path bootstrap first)

from substrate._precision import fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

_T0 = time.monotonic()

# The atom set the FR-pullback family is scored on, and its H_{3A} sizes.
ATOM_N = {"D": 6, "T": 9, "3He": 9, "4He": 12}

# Recorded per-atom |B_pred/B_AME| under the SELF-NORMALIZED measure, and
# the recorded max/min under the TEXTBOOK measure, both from the
# fr_pullback_borromean_h3a driver (uniform / no-FR variant).  These are
# INPUTS read from a prior run, not values this probe computes: they are
# what the reconstruction below is checked against.
RECORDED_SELFNORM_RATIOS = {
    "D": "0.2753", "T": "0.2980", "3He": "0.3094", "4He": "0.3276",
}
RECORDED_TEXTBOOK_MAXMIN = "1.8217"
RECORDED_SELFNORM_MAXMIN = "1.1901"


def partitions(n: int, mx: int | None = None) -> list:
    """All partitions of n as weakly-decreasing tuples."""
    if mx is None:
        mx = n
    if n == 0:
        return [()]
    out = []
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            out.append((k,) + rest)
    return out


def make_qdim(q: mp.mpf):
    """BALANCED q-integers — the convention this corpus's dim_q uses."""
    qi = 1 / q

    @lru_cache(maxsize=None)
    def qint(k: int) -> mp.mpf:
        return (q ** k - qi ** k) / (q - qi)

    @lru_cache(maxsize=None)
    def qfact(n: int) -> mp.mpf:
        r = mp.mpf(1)
        for k in range(1, n + 1):
            r *= qint(k)
        return r

    def hooks(shape: tuple) -> list:
        conj = [sum(1 for r in shape if r > c) for c in range(shape[0])]
        return [shape[i] - j + conj[j] - i - 1
                for i in range(len(shape)) for j in range(shape[i])]

    @lru_cache(maxsize=None)
    def dim_q(shape: tuple) -> mp.mpf:
        den = mp.mpf(1)
        for hk in hooks(shape):
            den *= qint(hk)
        return qfact(sum(shape)) / den

    return qint, qfact, dim_q


def main() -> int:
    mp.mp.dps = 60
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP

    q = Q_MP
    _, qfact, dim_q = make_qdim(q)

    ns = sorted(set(ATOM_N.values()))
    c_n: dict = {}
    selfnorm_dev = mp.mpf(0)
    scaling_dev = mp.mpf(0)

    for n in ns:
        shapes = tuple(sorted(partitions(n)))
        raw = {s: dim_q(s) ** 2 for s in shapes}
        total = sum(raw.values())
        w_self = {s: v / total for s, v in raw.items()}
        w_text = {s: raw[s] / qfact(n) for s in shapes}

        c_n[n] = total / qfact(n)
        selfnorm_dev = max(selfnorm_dev,
                           mp.fabs(sum(w_self.values()) - 1))
        # the exact relation the whole finding rests on
        scaling_dev = max(
            scaling_dev,
            max(mp.fabs(w_text[s] - c_n[n] * w_self[s]) for s in shapes))
        print(f"  n={n:2d} (A={n // 3}): {len(shapes):3d} shapes  "
              f"c_n = {mp.nstr(c_n[n], 16)}")

    # Reconstruct the textbook-normalized cross-atom variance from the
    # self-normalized per-atom ratios via the scaling law.
    text_ratios = {
        a: mp.mpf(RECORDED_SELFNORM_RATIOS[a]) * c_n[ATOM_N[a]]
        for a in ATOM_N
    }
    predicted = max(text_ratios.values()) / min(text_ratios.values())
    recorded = mp.mpf(RECORDED_TEXTBOOK_MAXMIN)
    recon_rel = mp.fabs(predicted - recorded) / recorded

    argmax_atom = max(text_ratios, key=lambda a: text_ratios[a])
    argmin_atom = min(text_ratios, key=lambda a: text_ratios[a])
    self_r = {a: mp.mpf(v) for a, v in RECORDED_SELFNORM_RATIOS.items()}
    same_extrema = (argmax_atom == max(self_r, key=lambda a: self_r[a])
                    and argmin_atom == min(self_r, key=lambda a: self_r[a]))

    print(f"\n  predicted textbook max/min = {mp.nstr(predicted, 10)}"
          f"   recorded = {RECORDED_TEXTBOOK_MAXMIN}"
          f"   rel dev = {mp.nstr(recon_rel, 4)}")
    print(f"  inflation vs self-normalized "
          f"({RECORDED_SELFNORM_MAXMIN}): "
          f"{mp.nstr(recorded / mp.mpf(RECORDED_SELFNORM_MAXMIN), 8)}x")

    wb = WitnessBuilder("probe-plancherel-convention-gap", engine="mpmath",
                        start_time=_T0)
    wb.set_description(
        "The balanced-convention q-Plancherel normalization gap (bean "
        "qou-7o7h). dim_q^2/[n]_q! is NOT a probability measure in the "
        "balanced q-integer convention: c_n = Sum dim_q^2/[n]_q! runs "
        "0.991 / 1.111 / 1.517 at n = 6/9/12 and GROWS with n. Because "
        "w_textbook = c_n * w_selfnormalized exactly and the binding "
        "functional is linear in the weights, B scales by c_n; the factor "
        "cancels within one atom but NOT across atoms, since n = 3A "
        "differs. So any cross-atom metric — the max/min variance the "
        "FR-pullback probes are scored on — is distorted. Measured: the "
        "published 1.82x baseline is ~53% inflated by this alone; the "
        "self-normalized figure is 1.19x, and the scaling law reproduces "
        "the textbook run to 5.5e-5 (that residual being the 4-sig-fig "
        "rounding of the recorded ratios). Says nothing about which "
        "normalization is physically right — only that the two differ by "
        "a known n-dependent factor and the corpus contains both.")
    wb.set_audit_only("docs/audits/2026-09-04-plancherel-convention-gap.md")

    wb.add_data("c_n", {str(n): mp.nstr(c_n[n], 30) for n in ns})
    wb.add_data("atom_to_n", ATOM_N)
    wb.add_data("reconstruction", {
        "inputs_are_recorded_not_computed": True,
        "selfnorm_ratios_recorded": RECORDED_SELFNORM_RATIOS,
        "textbook_maxmin_recorded": RECORDED_TEXTBOOK_MAXMIN,
        "selfnorm_maxmin_recorded": RECORDED_SELFNORM_MAXMIN,
        "textbook_ratios_predicted": {
            a: mp.nstr(text_ratios[a], 16) for a in text_ratios},
        "predicted_textbook_maxmin": mp.nstr(predicted, 16),
        "relative_deviation": mp.nstr(recon_rel, 8),
        "inflation_factor": mp.nstr(
            recorded / mp.mpf(RECORDED_SELFNORM_MAXMIN), 12),
    })
    wb.add_data("ratio_identity_shortcut", {
        "observation": "textbook/selfnorm maxmin = 1.5307 equals "
                       "c_12/c_6 = 1.5308",
        "status": "TRUE BUT CONDITIONAL — do not quote as the mechanism",
        "condition": "holds only while the argmax atom is the largest-c_n "
                     "atom and the argmin atom the smallest, under BOTH "
                     "normalizations",
        "argmax_atom": argmax_atom,
        "argmin_atom": argmin_atom,
        "condition_holds_here": bool(same_extrema),
        "quote_instead": "w_textbook = c_n * w_selfnormalized, and the "
                         "functional is linear in the weights",
    })

    wb.add_assertion(
        "selfnormalized_is_a_measure",
        computed=fmt(selfnorm_dev), expected=fmt(mp.mpf(0)),
        tolerance=1e-40,
        source="Sum_lambda dim_q^2/Sum_mu dim_q^2 = 1 for every n in the "
               "atom set — true by construction, checked numerically",
    )
    wb.add_assertion(
        "textbook_equals_c_n_times_selfnormalized",
        computed=fmt(scaling_dev), expected=fmt(mp.mpf(0)),
        tolerance=1e-40,
        source="w_textbook(lambda) = c_n * w_selfnorm(lambda) exactly, "
               "every lambda, every n — the identity the cross-atom "
               "distortion follows from",
    )
    wb.add_assertion(
        "scaling_law_reproduces_recorded_textbook_run",
        computed=fmt(recon_rel), expected=fmt(mp.mpf(0)),
        tolerance=1e-3,
        source="self-normalized per-atom ratios scaled by c_n reproduce "
               "the INDEPENDENTLY RECORDED textbook-normalized cross-atom "
               "max/min (1.8217); tolerance 1e-3 because the recorded "
               "ratios carry only 4 significant figures",
    )
    wb.add_caveat(
        "The reconstruction's inputs (per-atom self-normalized ratios, "
        "recorded textbook max/min) are READ FROM a prior run of "
        "fr_pullback_borromean_h3a_test, not recomputed here — that would "
        "need the ~25-minute H_12 character leg. The scaling law itself "
        "(assertion 2) is computed from scratch and is what carries the "
        "finding; the reconstruction is a consistency check on top of it.")
    wb.add_caveat(
        "Those recorded ratios come from a run at the RETIRED muon-era "
        "pin A, while c_n here is computed at the current proton pin. The "
        "11.5 ppb pin difference is ~7 orders below the effect being "
        "measured (a 53% inflation), so it cannot affect the conclusion — "
        "but the reconstruction is therefore a cross-pin comparison and "
        "its 5.5e-5 residual should not be read as a precision claim.")
    wb.save()
    print("\n  witness saved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
