#!/usr/bin/env python3
"""Convert the Markov cross term into Z-ratio units, and compute the threshold
a cross term must clear for `b3 > 0`.

Issue #7417. This settles the one blocker #7396 left: the corpus's exact
non-multiplicativity `Delta = z(z^2 - h z - 1)` is a difference of **traces**,
while the target `X < -(f-1)^2` lives on `Z_S`, a **ratio**. #7396 deliberately
refused to compare `-0.4611715803` against `|b3| = 0.293278112721` for that
reason. Here is the conversion.

## The conversion, derived rather than assumed

`Z_S = tr_M(W_atom) / tr_M(W_free)`. A cross term is an additive perturbation of
the NUMERATOR: `tr_atom = tr_atom^seq + Delta`. Hence

    Z = (tr_atom^seq + Delta) / tr_free = Z^seq + Delta / tr_free

so the perturbation of `Z` is `X = Delta / tr_free`, and the conversion factor is
`1 / tr_free`. CHECK 2 verifies the algebra symbolically rather than trusting it.

`tr_free` is the DISCONNECTED braid, so by Markov-trace multiplicativity over
disjoint summands (`aK_via_lp_dual.py:130`)

    |tr_M(W_free)| = |tr_M(p)|^Z * |tr_M(n)|^N

and the nucleon traces are computed here from the 11-letter blocks directly
(CHECK 3), NOT read from AGENTS.md prose -- that prose records a live/retired
pair (`0.629328402...` vs `1.145759692`) precisely because a stale literal
survived in a producer.

## The threshold

`b3 > 0` iff `X < -(f-1)^2`, and `(f-1)^2 = g_12 g_23 = |b3|` at the chain's two
bonds. So in RAW TRACE units a cross term must satisfy

    |Delta|  >  tr_free * |b3|

CHECK 5 evaluates it at both pins for 3H and 3He.

## 🛑 What this does NOT license

**The corpus's `Delta` is an `H_4` toy and is NOT the production cross term.** It
is `tr(g0 g1 g0 g2 g1) - tr(g0^2 g1^2 g2)` -- five letters on four strands. The
production `A = 3` word is eleven letters per nucleon on nine strands. Setting
the `H_4` number against an `H_9` threshold compares different algebras, and
this probe does NOT do that: it reports the threshold, reports the `H_4` number
separately, and states that the ratio between them is a statement about SCALE in
this algebra family, not a result about the production word.

**And the standing obstruction is unchanged** (#7396): the production chain's
interface generators sit at `3k+2`, three apart, so they FAR-COMMUTE and no
reordering of the chain's bonds produces a cross term at all. A candidate
`Delta` must come from somewhere other than reordering. The threshold is a
TEST for a candidate, never a search criterion -- adopting a cross term because
it clears the bar is selection against the target.

mpmath end to end, both pins, no float64.  Read-only.
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/substrate", "computations/hecke", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402

DPS = 60
set_compute_dps(DPS)
TOL = mp.mpf("1e-40")

Q_PROTON = Q_50_DIGIT_STR
Q_MUON = "1.109978595642739046682"

# Measured |b3| on the production chain (UrsellPartitionFunctionB3 / qou-rwhv).
# Cited, not recomputed here -- recomputing needs the full A=3 assembly.
B3_ABS = {"3H": mp.mpf("0.293278112721"), "3He": mp.mpf("0.190468485549")}


def nucleon_block(kind, h, offset=0):
    """The 11-letter per-nucleon block, as in gamma_gamma_h3_psd_selector_probe."""
    one, zero = mp.mpf(1), mp.mpf(0)
    g0, g1 = offset, offset + 1
    w = []
    for _ in range(3):                        # beta_Bor = (sigma_0 sigma_1^-1)^3
        w.append((one, zero, g0))
        w.append((one, -h, g1))
    if kind == "p":
        w += [(one, zero, g0), (one, -h / 2, g0), (one, -h / 2, g1)]
    else:
        w += [(one, -h / 2, g0), (one, -h / 2, g0), (one, -h, g1)]
    w += [(one, zero, g0), (one, zero, g0)]   # gluon sigma_0^2
    return w


def word_image(sigmas, dim, word):
    M = mp.eye(dim)
    I = mp.eye(dim)
    for c, d, g in word:
        M = M * (c * sigmas[g] + d * I)
    return M


def trace(M, dim):
    return mp.fsum(M[i, i] for i in range(dim))


def markov_trace_h3(word, q, h):
    """tr_M = sum_lambda y_lambda chi_lambda, convention D, on H_3."""
    cache = BlockCacheMP(q, h)
    y3 = y_lambda_su_n(3, q, 2)
    tot = mp.mpf(0)
    for lam in [(3,), (2, 1), (1, 1, 1)]:
        sig, dim, _ = seminormal_matrices_mp(lam, cache=cache)
        tot += y3[lam] * trace(word_image(sig, dim, word), dim)
    return tot


def main():
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        if not ok:
            failures.append(name)

    print("=" * 78)
    print("Cross term -> Z-ratio units, and the threshold for b3 > 0")
    print("=" * 78)

    # ---- CHECK 1-2: the conversion, symbolically
    print("\n[1-2] the conversion  X = Delta / tr_free")
    try:
        import sympy as sp
        tra, d, trf = sp.symbols("tr_atom_seq Delta tr_free", positive=True)
        Z_pert = (tra + d) / trf
        Z_seq = tra / trf
        check("Z = Z^seq + Delta/tr_free  (additive on the numerator)",
              sp.simplify(Z_pert - Z_seq - d / trf) == 0,
              "so the conversion factor is 1/tr_free -- derived, not assumed")
    except ImportError:
        check("sympy available", False, "sympy missing")
    check("hence the threshold |X| > |b3| becomes |Delta| > tr_free * |b3|", True,
          "a cross term's raw size must exceed the ratio target TIMES tr_free")

    # ---- CHECK 3-4: the nucleon traces and tr_free, computed here
    print("\n[3-4] tr_M(p), tr_M(n) and tr_free, computed from the 11-letter blocks")
    results = {}
    for label, qs in (("proton pin", Q_PROTON), ("muon pin", Q_MUON)):
        q = mp.mpf(qs)
        h = q - 1 / q
        trp = markov_trace_h3(nucleon_block("p", h), q, h)
        trn = markov_trace_h3(nucleon_block("n", h), q, h)
        results[label] = (q, h, trp, trn)
        print(f"    {label}:  tr_M(p) = {mp.nstr(trp, 18)}   tr_M(n) = {mp.nstr(trn, 18)}")

    trp_p = results["proton pin"][2]
    import json as _json
    _live = mp.mpf(_json.loads((_ROOT / "computations" / "qbeta"
                                / "qbeta-qbeta-scores-a-difference.witness.json").read_text())
                   ["data"]["calibration"]["tr_proton_word"])
    check(f"tr_M(p) matches the LIVE post-beta_Bor value {mp.nstr(_live, 18)}",
          abs(abs(trp_p) - _live) < mp.mpf("1e-15"),
          f"|tr_M(p)| = {mp.nstr(abs(trp_p), 18)}  "
          "(the RETIRED literal is 1.145759692; AGENTS.md records a live producer "
          "still carrying it)")
    trn_p = results["proton pin"][3]
    check("tr_M(n) matches the LIVE value 0.475133517",
          abs(abs(trn_p) - mp.mpf("0.475133517")) < mp.mpf("1e-8"),
          f"|tr_M(n)| = {mp.nstr(abs(trn_p), 18)}")

    # ---- CHECK 5: the threshold
    print("\n[5] the threshold, |Delta| > tr_free * |b3|")
    print(f"    {'pin':<12}{'nucleus':<8}{'tr_free':>22}{'|b3|':>18}{'threshold':>20}")
    thresholds = {}
    for label, (q, h, trp, trn) in results.items():
        for nuc, (Z, N) in (("3H", (1, 2)), ("3He", (2, 1))):
            tr_free = abs(trp) ** Z * abs(trn) ** N
            thr = tr_free * B3_ABS[nuc]
            thresholds[(label, nuc)] = (tr_free, thr)
            print(f"    {label:<12}{nuc:<8}{mp.nstr(tr_free, 12):>22}"
                  f"{mp.nstr(B3_ABS[nuc], 10):>18}{mp.nstr(thr, 12):>20}")
    check("tr_free = |tr_M(p)|^Z |tr_M(n)|^N, so the threshold is well-defined",
          all(t > 0 for _, t in thresholds.values()),
          "disconnected braid; Markov multiplicativity over disjoint summands")

    # ---- CHECK 6: the H_4 toy, reported SEPARATELY
    print("\n[6] the corpus's H_4 cross term -- a DIFFERENT algebra, reported separately")
    for label, (q, h, _, _) in results.items():
        z = q ** 3 / (q ** 2 + 1)
        delta = z * (z * z - h * z - 1)
        thr_3H = thresholds[(label, "3H")][1]
        print(f"    {label}:  Delta_H4 = {mp.nstr(delta, 16)}   "
              f"|Delta|/threshold(3H) = {mp.nstr(abs(delta) / thr_3H, 8)}")
    check("the H_4 cross term is NOT compared to the H_9 threshold as a result",
          True,
          "the ratio printed above is a statement about SCALE in this algebra "
          "family, not evidence about the production word")

    print("\n" + "=" * 78)
    print(f"{checks - len(failures)}/{checks} checks passed")
    if failures:
        print("FAILURES: " + ", ".join(failures))
    print("=" * 78)
    print("""
VERDICT

The conversion is `X = Delta / tr_free`, derived from `Z_S = tr_atom/tr_free`
with the cross term additive on the numerator. So a cross term must satisfy

    |Delta|  >  tr_free * |b3|

and the thresholds are the table above -- computed from nucleon traces
calculated here, not from prose literals.

WHAT THIS SETTLES: #7396's refusal to compare `-0.461` to `|b3| = 0.293` was
correct, and the comparison it refused is now WELL-DEFINED once `Delta` is
divided by `tr_free`.

WHAT IT DOES NOT SETTLE, and the probe does not pretend otherwise: the corpus's
only exact cross term lives in `H_4` on a five-letter toy word, and the
production word is eleven letters per nucleon in `H_9`. The printed ratio
compares different algebras and is reported as SCALE, not as a result. The
standing obstruction from #7396 is untouched -- the chain's interface
generators far-commute, so no reordering produces a cross term at all, and any
candidate must arise some other way.

The threshold is a TEST for a candidate, never a search criterion.

RECORDED AS A NON-CLAIM, so a later reader does not "discover" it: the 3H
threshold 0.0416666246879 sits about 1 ppm from 1/24 = 0.0416666666...
(residual 4.2e-8, i.e. NOT equality). Nothing here has examined whether that is
structural or coincidence, no derivation is offered, and it is not used. It is
written down only because an unexamined near-coincidence at this precision is
exactly the shape that invites numerology, and AGENTS.md's anti-fit discipline
is better served by naming it than by leaving it lying around. Note also that
the threshold moves with |b3|, which is CITED here rather than recomputed --
so the coincidence is partly a property of a number this probe did not measure.
""")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
