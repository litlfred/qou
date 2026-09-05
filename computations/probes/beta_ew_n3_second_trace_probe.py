#!/usr/bin/env python3
"""Does the EW word have a Markov trace at N=3, where its block is OCCUPIED?

Bean `qou-wapd`, follow-on measurement. `beta_ew_delta_I_321_and_wedderburn.py`
and `close_321_weinberg_gap.py` both extract cot(theta_W) candidates from the
lambda = (3,2,1) block of H_6(q), weighting by dim_q^2/[n]_q!. The corpus has
already adjudicated that construction, in
`appendix-standard-model/sm-params-gauge-couplings.md`:

    "(3,2,1) has three rows, and the Schur-Weyl row cap gives dim V_lambda = 0
     whenever l(lambda) > N; the fibre is the fundamental of SU_q(2), so N = 2
     and that block carries no states. Its Ocneanu weight vanishes identically
     ... Every route from such a block to a physical number is either a Markov
     trace, which the row cap sends to zero, or a spectrum, which has no states
     to act on."

That is a statement about **N = 2**. The corpus separately holds, in
`y_lambda_su_n.py` and `RowCapObstruction.lean`, that the flavour/eightfold
sector REQUIRES N = 3; that `ocneanu_N_lockin_probe.py` proves the mass channel
cannot merely be retuned to N = 3; and therefore that flavour needs a SECOND
trace on the same H_n(q) -- which `HnMarkovTrace.lean` already makes typeable by
carrying the Markov parameter as a free class field.

At N = 3 the block (3,2,1) has l(lambda) = 3 <= N, so it is OCCUPIED and its
Ocneanu weight is nonzero (measured: 0.0103939752433 at the substrate q0). The
row-cap objection therefore does not apply to an N = 3 trace, and the question
becomes empirical rather than structural:

    **what IS tr_M(beta_EW Delta_I) at N = 3, and does it go anywhere near
    cot(theta_W) = 1.82306787?**

This probe computes it. THE POINT IS THE NUMBER, WHOEVER IT FAVOURS -- a route
that survives a structural objection and then misses by 10x is refuted on its
own terms, which is a more useful outcome than leaving it as an untested idea.

WHAT THIS DOES NOT CLAIM. That N = 3 is the right reading of the EW sector. The
corpus's own preferred lever is elsewhere (the Milnor triple linking mu-bar_123,
which separates the two U(1)s), and the relative coupling normalisation is open
and inherits the SU(3) sector. This probe establishes only what the N = 3 trace
of this specific word IS, so that the route can be judged on a number.

METHOD NOTE, since the obvious way is too slow to finish. `_hoefsmit_build` with
a 50-digit q coerced to an exact `sp.Rational` (via `nsimplify`) builds enormous
rationals, and 21 multiplications of 16x16 symbolic matrices over them does not
terminate in ten minutes -- measured, on the first attempt at this. `sp.Float`
at 50 digits carries the same precision without the rational blow-up. Characters
are then read out at 40 digits. No float64 anywhere: the consumer under study
declares an `archimedean_by_design` numpy exemption for its eigenvalue path,
which this probe neither inherits nor exercises.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402
from hecke_character_symbolic import _hoefsmit_build  # noqa: E402

# CODATA: sin^2(theta_W) = 0.23129 -> cot(theta_W). Carried as the target the
# two consumer files compare against, not as an input to anything computed here.
COT_THETA_W_CODATA = mp.mpf("1.82306787")


def beta_ew_delta_I_word_n6() -> list[int]:
    """The EW word, copied verbatim from close_321_weinberg_gap.py:222-224."""
    delta_I = [1, 3, 1]
    return [0] * 4 + delta_I + [2] * 6 + delta_I + [4] * 8 + delta_I


def partitions(n: int, cap: int | None = None) -> list[tuple[int, ...]]:
    if n == 0:
        return [()]
    cap = n if cap is None else cap
    out: list[tuple[int, ...]] = []
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            out.append((first,) + rest)
    return out


def main() -> int:
    set_compute_dps()
    b = WitnessBuilder("beta-ew-n3-second-trace")
    b.set_description(
        "Bean qou-wapd. Computes tr_M(beta_EW Delta_I) at N=3, where the "
        "lambda=(3,2,1) block is OCCUPIED (l(lambda)=3 <= N) and its Ocneanu "
        "weight is nonzero -- as against N=2, where the Schur-Weyl row cap "
        "sends it to zero and the corpus's appendix-standard-model ruling "
        "places every route from the block outside the carrier. The corpus "
        "separately holds that the flavour sector requires N=3, that the mass "
        "channel cannot be retuned to it, and therefore that a SECOND Markov "
        "trace on the same H_n(q) is needed -- already typeable, since "
        "HnMarkovTrace.lean carries the Markov parameter as a free class "
        "field. This probe asks the resulting empirical question: what is the "
        "N=3 trace of this word, and does it approach cot(theta_W)? It does "
        "NOT claim N=3 is the right reading of the EW sector; the corpus's "
        "preferred lever is the Milnor triple linking, and the coupling "
        "normalisation is open."
    )
    b.add_parameter("q0_50dps", Q_50_DIGIT_STR)
    b.add_parameter("word", str(beta_ew_delta_I_word_n6()))
    b.add_parameter("cot_theta_W_codata", str(COT_THETA_W_CODATA))

    q0 = mp.mpf(Q_50_DIGIT_STR)
    q0_sym = sp.Float(Q_50_DIGIT_STR, 50)
    word = beta_ew_delta_I_word_n6()
    lams = partitions(6)

    # -- characters, exactly through the same Hoefsmit path the consumers use --
    chi: dict[tuple, mp.mpf | None] = {}
    dims: dict[tuple, int] = {}
    for lam in lams:
        mats, dim, _ = _hoefsmit_build(list(lam), q0_sym)
        dims[lam] = dim
        if dim == 0:
            chi[lam] = None
            continue
        M = sp.eye(dim)
        for g in word:
            if g < len(mats):
                M = M * mats[g]
        chi[lam] = mp.mpf(str(sp.N(M.trace(), 40)))

    b.add_data("characters", {
        str(list(l)): {"dim": dims[l],
                       "chi": fmt(chi[l]) if chi[l] is not None else None}
        for l in lams})

    # -- the trace at each N ---------------------------------------------------
    per_N = {}
    for N in (2, 3, 4):
        y = y_lambda_su_n(6, q0, N)
        terms, occupied = {}, 0
        tot = mp.mpf(0)
        for lam in lams:
            yv = y.get(lam)
            if yv is None or chi[lam] is None:
                continue
            yv = mp.mpf(str(yv))
            if yv != 0:
                occupied += 1
            t = yv * chi[lam]
            tot += t
            terms[str(list(lam))] = {"y": fmt(yv), "term": fmt(t)}
        y321 = y.get((3, 2, 1))
        per_N[str(N)] = {
            "occupied_blocks": occupied,
            "total_blocks": len(lams),
            "y_at_321": fmt(mp.mpf(str(y321))) if y321 is not None else None,
            "trace": fmt(tot),
            "ratio_to_cot_theta_W": fmt(tot / COT_THETA_W_CODATA),
            "terms": terms,
        }
    b.add_data("trace_by_N", per_N)

    tr2 = mp.mpf(per_N["2"]["trace"])
    tr3 = mp.mpf(per_N["3"]["trace"])
    b.add_assertion(
        "block_321_is_occupied_at_N3_not_N2",
        computed="1" if (mp.mpf(per_N["2"]["y_at_321"]) == 0
                         and mp.mpf(per_N["3"]["y_at_321"]) != 0) else "0",
        expected="1",
        source="y_(3,2,1) = 0 exactly at N=2 (Schur-Weyl row cap, l(lambda)=3 > 2) "
               "and nonzero at N=3 — so the corpus's 'the block carries no "
               "states' ruling is scoped to N=2 and an N=3 trace is not "
               "excluded by it",
    )
    b.add_data("verdict_inputs", {
        "trace_N2": fmt(tr2),
        "trace_N3": fmt(tr3),
        "cot_theta_W_codata": str(COT_THETA_W_CODATA),
        "rel_miss_N3": fmt(abs(tr3 - COT_THETA_W_CODATA) / COT_THETA_W_CODATA),
        "reading": "A Markov trace is normalised, so tr_M is not dimensionally "
                   "a cotangent and no agreement is EXPECTED here — the "
                   "consumers build cot(theta_W) from RATIOS of weighted "
                   "quantities, not from the bare trace. This row is reported "
                   "so the magnitude is on the record; do not read a miss as a "
                   "refutation of the N=3 route, nor a hit as confirmation.",
    })

    b.save()
    for N in ("2", "3", "4"):
        r = per_N[N]
        print(f"N={N}: tr_M = {r['trace'][:22]:>24}  "
              f"occupied {r['occupied_blocks']}/{r['total_blocks']}  "
              f"y_(3,2,1) = {r['y_at_321'][:14]}")
    print(f"\ncot(theta_W) CODATA = {COT_THETA_W_CODATA}")
    print(f"consumers' reported best (dim_q^2 aggregate) = 1.82075284")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
