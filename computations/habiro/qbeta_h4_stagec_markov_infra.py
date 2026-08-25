#!/usr/bin/env python3
"""Stage-C instrumented base: the H4 Markov trace, wired and gated (bean 1jrh).

Wires the H4(q) Markov trace tr_M(W) = sum_{lambda|-4} y_lambda chi^lambda(W)
from the validated corpus pieces (young_seminormal seminormal reps;
y_lambda_wenzl_bridge weights) into a single callable that accepts ANY H4
braid word — including sigma_3-involving words — at 50 dps.

This is the infrastructure half of Stage C (docs/scope/2026-06-18-qbeta-c4-
h4-tower-stage-c-scope.md #3): once the OPEN categorical sigma_3-lift Lambda
is specified, evaluating it is one call. NO Lambda candidate is enumerated or
evaluated here (the scope's no-fit rule).

Gates (all exact expectations, no fitting):
  A. Hecke relation on characters: chi(s_i^2) = h*chi(s_i) + chi(id), h=q-1/q,
     for every lambda|-4 and i in {1,2,3}.
  B. Markov generator-uniformity: tr_M(s_1) = tr_M(s_2) = tr_M(s_3) — the
     Markov property; exercises the NEW strand sigma_3 against a known law.
  C. H3->H4 stabilization (C12): tr_M^{H4}(iota w)/tr_M^{H3}(w) is the SAME
     constant for every sigma_3-free decay word w (the free-neutron-decay NF
     basis + extras), at multiple q points.
  D. Branching cross-check: tr_M^{H4}(iota w) computed directly (lambda|-4
     characters) equals the branching form sum_mu y_mu sum_{lam up mu}
     chi^lam(w) (H3 characters only).

Witness: qbeta-h4-stagec-markov-infra.witness.json (auditOnly).
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

from mpmath import mp

HERE = Path(__file__).resolve().parent           # computations/habiro
ROOT = HERE.parent                                # computations/
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "substrate"))

from young_seminormal import seminormal_sigma, standard_tableaux  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric, partitions_of  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def chi_word(shape: tuple, word: tuple, qv) -> mp.mpf:
    """Character chi^shape(word) via the seminormal rep (empty word -> dim).

    `word` uses 0-based generators (free-neutron-decay convention);
    `seminormal_sigma` is 1-based, so shift by +1 at the call."""
    d = len(standard_tableaux(shape))
    if not word:
        return mp.mpf(d)
    M = None
    for g in word:
        S = seminormal_sigma(shape, g + 1, qv)
        M = S if M is None else M * S
    return mp.fsum(M[i, i] for i in range(d))


def tr_M(n: int, word: tuple, qv) -> mp.mpf:
    """QOU Markov trace on H_n: sum_{lambda|-n} y_lambda chi^lambda(word)."""
    return mp.fsum(
        y_lambda_wenzl_bridge_numeric(tuple(lam), qv, mp.dps)
        * chi_word(tuple(lam), word, qv)
        for lam in partitions_of(n)
    )


def removable_to(mu: tuple):
    """Partitions lambda|-(n-1) with lambda up mu (remove one corner)."""
    out = []
    for i in range(len(mu)):
        if mu[i] >= 1 and (i == len(mu) - 1 or mu[i] > mu[i + 1]):
            lam = list(mu)
            lam[i] -= 1
            out.append(tuple(x for x in lam if x > 0))
    return out


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    from q_parameter import Q_50_DIGIT_STR  # noqa: E402
    q0 = mp.mpf(Q_50_DIGIT_STR)
    qpoints = [q0, mp.mpf("1.05"), mp.mpf("1.2"), mp.mpf("1.37"), mp.mpf("0.93")]

    # free-neutron-decay H3 NF basis (generators 0,1 = sigma_1, sigma_2) + extras
    decay_words = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
    extra_words = [(0, 0), (1, 1), (0, 0, 1)]
    tol = mp.mpf("1e-40")
    assertions = []

    print("=" * 76)
    print(" Stage-C infra: H4 Markov trace wired + gated (no Lambda evaluated)")
    print("=" * 76)

    # GATE A — Hecke relation on characters, every lambda|-4, every generator
    h = q0 - 1 / q0
    worstA = mp.mpf(0)
    for lam in partitions_of(4):
        lam = tuple(lam)
        for g in (0, 1, 2):
            lhs = chi_word(lam, (g, g), q0)
            rhs = h * chi_word(lam, (g,), q0) + chi_word(lam, (), q0)
            worstA = max(worstA, abs(lhs - rhs))
    print(f"  GATE A  Hecke chi(s_i^2)=h*chi(s_i)+chi(1), all lambda|-4, i=1..3: "
          f"worst {mp.nstr(worstA, 3)}")
    assertions.append({"label": "A: Hecke relation on H4 characters (<1e-40)",
                       "passed": bool(worstA < tol)})

    # GATE B — Markov generator-uniformity (exercises sigma_3)
    tg = [tr_M(4, (g,), q0) for g in (0, 1, 2)]
    worstB = max(abs(tg[0] - tg[1]), abs(tg[0] - tg[2]))
    print(f"  GATE B  tr_M(s_1)=tr_M(s_2)=tr_M(s_3) at H4: "
          f"{mp.nstr(tg[0], 12)}; worst dev {mp.nstr(worstB, 3)}")
    assertions.append({"label": "B: Markov generator-uniformity incl. sigma_3 (<1e-40)",
                       "passed": bool(worstB < tol)})

    # GATE C — C12 stabilization ratio constancy across sigma_3-free words, multi-q
    print("  GATE C  tr_M^{H4}(iota w)/tr_M^{H3}(w) constant over decay+extra words:")
    worstC = mp.mpf(0)
    ratio_at_q0 = None
    for qv in qpoints:
        ratios = []
        for w in decay_words + extra_words:
            r4 = tr_M(4, w, qv)
            r3 = tr_M(3, w, qv)
            ratios.append(r4 / r3)
        dev = max(abs(r - ratios[0]) for r in ratios)
        worstC = max(worstC, dev)
        if qv == q0:
            ratio_at_q0 = ratios[0]
        print(f"    q={mp.nstr(qv, 8)}: ratio={mp.nstr(ratios[0], 12)}  max dev {mp.nstr(dev, 3)}")
    assertions.append({"label": "C: C12 stabilization ratio word-independent at 5 q-points (<1e-40)",
                       "passed": bool(worstC < tol)})

    # GATE D — branching cross-check on the decay words at q0
    worstD = mp.mpf(0)
    for w in decay_words:
        direct = tr_M(4, w, q0)
        via_branch = mp.mpf(0)
        for mu in partitions_of(4):
            mu = tuple(mu)
            y = y_lambda_wenzl_bridge_numeric(mu, q0, mp.dps)
            via_branch += y * mp.fsum(chi_word(lam, w, q0) for lam in removable_to(mu))
        worstD = max(worstD, abs(direct - via_branch))
    print(f"  GATE D  direct lambda|-4 trace == branching (H3 characters) form: "
          f"worst {mp.nstr(worstD, 3)}")
    assertions.append({"label": "D: branching cross-check on decay words (<1e-40)",
                       "passed": bool(worstD < tol)})

    all_ok = all(a["passed"] for a in assertions)
    print(f"\n  {'ALL GATES PASS' if all_ok else 'GATE FAILURE'} — the H4 Markov-trace "
          f"pipeline is instrumented; the categorical sigma_3-lift Lambda remains the "
          f"sole open Stage-C item (none evaluated here).")

    witness = {
        "description": (
            "Stage-C instrumented base (bean 1jrh / Q_beta c_4): the H4(q) Markov "
            "trace wired from validated pieces (seminormal characters x Wenzl "
            "weights) into a callable accepting any H4 word incl. sigma_3, gated by "
            "four exact no-fit laws (Hecke, Markov generator-uniformity, C12 "
            "stabilization ratio constancy at 5 q-points, branching cross-check). "
            "NO sigma_3-lift candidate is enumerated or evaluated — the categorical "
            "Lambda stays the sole open item per the Stage-C scope. auditOnly."
        ),
        "audit_only": True,
        "parameters": {"q0": str(q0), "dps": mp.dps,
                       "q_points": [str(x) for x in qpoints],
                       "words": [list(w) for w in decay_words + extra_words]},
        "data": {
            "trM_H4_generator": mp.nstr(tg[0], 30),
            "c12_ratio_at_q0": mp.nstr(ratio_at_q0, 30),
            "worst_dev": {"A": mp.nstr(worstA, 6), "B": mp.nstr(worstB, 6),
                          "C": mp.nstr(worstC, 6), "D": mp.nstr(worstD, 6)},
        },
        "assertions": assertions,
        "allPassed": all_ok,
    }

    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = os.path.basename(__file__)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-h4-stagec-markov-infra.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  Witness: {out.name}   ({time.monotonic() - t0:.1f}s wall)")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
