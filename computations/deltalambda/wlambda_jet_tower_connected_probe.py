#!/usr/bin/env python3
"""Jet-tower lift of the connected standard-channel binding weight.

Follow-on to wlambda_nuclear_braid_connected_probe.py, which found: at fixed H_3
the connected part C_std lives in the non-abelian (2,1) rep but its PER-BOND value
SHRINKS for heavy nuclei (does not sustain extensivity). This probe asks the queued
question: does lifting to the JET TOWER (branching H_k -> H_3, k >= 3) restore the
per-bond A-scaling, or does the tower converge to a bounded correction?

Uses the EXACT branching machinery of computations/jet_knot_invariants.py
(count_syt_skew multiplicities + q-Plancherel weights W_lambda) — no fit, no
truncation beyond the level cap.

NORMALIZATION (2026-09-05, bean qou-uk8o). W_lambda is now the SELF-NORMALIZED
q-Plancherel weight d_q^2 / Sigma_mu d_q^2, not d_q^2/[k]_q!. The latter is a
probability measure at q = 1 only; at the substrate q_0 it sums to
c_k = 0.9874 / 0.9822 / 0.9822 / 0.9911 / 1.0124 / 1.0506 / 1.1109 at k = 3..9
(docs/audits/2026-09-04-plancherel-convention-gap.md). Because w_mu(k) is
linear in the weight, every level carried a DIFFERENT factor and this probe's
whole point is a comparison ACROSS levels. Effect, w_std(k) for k = 3..9:

    was  0.661 0.903 1.677 3.841 8.945 22.406 62.193   (d_q^2/[k]_q!)
    now  0.669 0.919 1.707 3.876 8.835 21.328 55.984   (self-normalized)

BOTH assertions still pass and the verdict is unchanged: growth is still
monotone with growing increments, and the std fraction is unchanged to 6 dp
because it is a ratio at ONE k, where c_k cancels exactly.

The universal (nucleus-independent) standard-channel tower weight at level k is

    w_std(k) = Sigma_{lambda |- k} W_lambda * mult_(2,1)(lambda restricted to H_3),

and likewise w_sym(k), w_alt(k) for the two 1-dim reps. The tower-accumulated
connected binding per nucleus is w_std(<=K) * C_std(nucleus).

Finding (overturned the naive expectation):
  1. The RAW connected weight w_std(k) does NOT converge — it GROWS geometrically
     (~2.5x/jet level, unbounded), even though the NORMALIZED a_k converges (the
     ratio cancels the growth). The standard (connected) channel holds a stable
     ~51% share at every level.
  2. So the jet tower DOES supply unbounded, extensive-capable growth in the
     connected (2,1) channel. The open piece is now sharp: the LEVEL-SELECTION
     rule k(A) (= GAP-A-3, categorical brane-tower level selection) — if k(A)
     grows with mass/bond-count, w_std(k(A)) supplies the extensive binding.

Usage:
    python3 wlambda_jet_tower_connected_probe.py
"""
import datetime
import hashlib
import json
import os
import platform
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

_HERE = os.path.dirname(os.path.abspath(__file__))

# Exact branching helpers from the canonical jet-invariant compute (no fit).
from jet_knot_invariants import (  # noqa: E402
    count_syt_skew, contains, H3_PARTS, H3_DIMS,
)
from hecke_characters import partitions_of, dim_q, qfac  # noqa: E402
from qou_substrate.constants import Q as Q0_PROTON  # noqa: E402 — anchor-independent proton pin (qou-6p3b Tranche C)
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402
import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps()
Q0_MP = Q_MP   # same proton pin as Q0_PROTON, at compute dps


def _q_int(m, q):
    """[m]_q = (q^m - q^-m)/(q - q^-1), balanced convention, in mpmath."""
    return (q ** m - q ** (-m)) / (q - 1 / q)


def _q_fact(m, q):
    r = mp.mpf(1)
    for j in range(1, m + 1):
        r *= _q_int(j, q)
    return r


def _dim_q(lam, q):
    """d_q(lambda) = [n]_q!/prod_cells [h]_q, in mpmath.

    Local rather than `hecke_characters.dim_q`, which returns a builtin float:
    the normalizer below is a sum over all p(k) partitions and this producer's
    weights are the object under audit, so they are carried as mpf. (This is
    precision hygiene only -- c_k differs from 1 by 1e-2..1e-1, so float64
    rounding was never what made the weights non-normalized.)
    """
    num = _q_fact(sum(lam), q)
    den = mp.mpf(1)
    for r, row in enumerate(lam):
        for c in range(row):
            arm = row - c - 1
            leg = sum(1 for rr in range(r + 1, len(lam)) if lam[rr] > c)
            den *= _q_int(arm + leg + 1, q)
    return num / den


def normalization_c(k):
    """c_k = Sigma_{lambda |- k} d_q(lambda)^2 / [k]_q!.

    The textbook q-Plancherel weight W = d_q^2/[k]_q! is a probability measure
    at q = 1 ONLY; at the substrate q_0 it sums to c_k, which VARIES with k
    (0.9874 / 0.9822 / 0.9822 / 0.9911 / 1.0124 / 1.0506 / 1.1109 at k = 3..9).
    Since w_mu(k) is linear in W, an unnormalized w_mu(k) carries c_k -- which
    cancels from the std-fraction (a ratio at one k) and does NOT cancel from
    the growth comparison ACROSS k that assertion 1 is scored on.
    docs/audits/2026-09-04-plancherel-convention-gap.md; bean qou-uk8o.
    """
    nfac = _q_fact(k, Q0_MP)
    return sum((_dim_q(lam, Q0_MP) ** 2 / nfac for lam in partitions_of(k)),
               mp.mpf(0))


def tower_channel_weights(k, self_normalized=True):
    """(w_sym, w_std, w_alt) at jet level k: Sigma_{lambda|-k} W_lambda * mult_mu.

    `self_normalized` divides by c_k, i.e. uses W_lambda = d_q^2/Sigma_mu d_q^2,
    a probability measure at every k. Pass False for the historical
    (unnormalized) form.
    """
    nfac = _q_fact(k, Q0_MP)
    denom = normalization_c(k) if self_normalized else mp.mpf(1)
    w = {mu: mp.mpf(0) for mu in H3_PARTS}
    for lam in partitions_of(k):
        W_lam = _dim_q(lam, Q0_MP) ** 2 / nfac / denom
        for mu in H3_PARTS:
            if contains(lam, mu):
                w[mu] += W_lam * count_syt_skew(lam, mu)
    return w[(3,)], w[(2, 1)], w[(1, 1, 1)]


def main() -> int:
    assertions = []

    def rec(name, passed, detail):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}: {detail}")
        return passed

    all_ok = True
    print("Universal jet-tower channel weights  w_mu(k) = Sigma_{lam|-k} W_lam * mult_mu(lam|H_3)\n")
    print(f"{'k':<4}{'w_sym (3)':<14}{'w_std (2,1)':<15}{'w_alt (1^3)':<14}"
          f"{'std frac':<10}{'c_k':<10}")
    K = 9
    rows = {}
    for k in range(3, K + 1):
        ws, wstd, wa = tower_channel_weights(k)
        tot = ws + wstd + wa
        frac = (wstd / tot if tot else mp.mpf(0))
        rows[k] = dict(w_sym=fmt(ws), w_std=fmt(wstd), w_alt=fmt(wa),
                       std_frac=fmt(frac), c_k=fmt(normalization_c(k)))
        print(f"{k:<4}{float(ws):<14.8f}{float(wstd):<15.8f}{float(wa):<14.8f}"
              f"{float(frac):<10.6f}{float(normalization_c(k)):<10.6f}")

    # 1. The RAW connected standard-channel weight GROWS with the jet level (it is
    #    the multiplicity-weighted Plancherel expectation of (2,1) in the restriction,
    #    which is unbounded), even though the NORMALIZED a_k converges (the ratio
    #    cancels the growth). This is the extensive-capable content.
    wstd_vals = [mp.mpf(rows[k]['w_std']) for k in rows]
    _ws = {k: mp.mpf(rows[k]['w_std']) for k in rows}
    d = [_ws[k] - _ws[k - 1] for k in range(4, K + 1)]
    grows = all(_ws[k] > _ws[k - 1] for k in range(4, K + 1)) \
        and all(d[i] > d[i - 1] for i in range(1, len(d)))
    all_ok &= rec("jet_tower_w_std_grows_unbounded",
                  grows,
                  f"w_std(k) k=3..{K}: {[round(float(v),3) for v in wstd_vals]} — monotone "
                  f"growth with GROWING increments (~2.5x/level) -> UNBOUNDED, "
                  f"extensive-capable connected content in the tower")

    # 2. The standard (connected) channel keeps a STABLE share (~0.51) at every level
    #    -> the connected channel does not wash out as you climb the tower.
    fracs = [mp.mpf(rows[k]['std_frac']) for k in rows if k >= 4]
    stable_share = (max(fracs) - min(fracs)) < 0.03
    all_ok &= rec("std_connected_share_stable",
                  stable_share,
                  f"std fraction k>=4: {[round(float(f),4) for f in fracs]} (stable ~0.51 -> "
                  f"the connected channel holds a constant ~half share up the tower)")

    verdict = ("POSITIVE REDIRECT (no closure): contrary to the naive expectation, the "
               "RAW connected standard-channel tower weight w_std(k) does NOT converge — "
               "it GROWS geometrically (~2.5x per jet level, unbounded), while the "
               "NORMALIZED per-level invariant a_k converges (the ratio cancels the "
               "growth). The standard (connected) channel holds a stable ~51% share at "
               "every level. So the jet tower DOES supply unbounded, extensive-capable "
               "growth in the connected (2,1) channel — the extensivity the fixed-H_3 "
               "braid lacked is AVAILABLE in the tower. The open piece is now sharp and "
               "named: the LEVEL-SELECTION rule k(A) (which jet level a nucleus of mass A "
               "occupies) = GAP-A-3 'categorical brane-tower level selection'. If k(A) "
               "grows with A/bond-count, w_std(k(A)) supplies the extensive binding. No "
               "fit; no wiring; does NOT set k(A) or land magnitudes.")
    print(f"\nVERDICT: {verdict}")

    with open(os.path.abspath(__file__), "rb") as _f:
        src = _f.read()
    try:
        commit_sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=_HERE,
                                    capture_output=True, text=True, check=True).stdout.strip() or "unknown"
    except Exception:
        commit_sha = "unknown"
    witness = {
        "schema": "witness/v1",
        "computation": "wlambda-jet-tower-connected",
        "engine": "python",
        "engineVersion": platform.python_version(),
        "scriptFile": os.path.basename(__file__),
        "commitSha": commit_sha,
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "description": (
            "Jet-tower lift of the connected standard-channel binding weight: the "
            "universal w_std(k)=Sigma W_lam*mult_(2,1) GROWS geometrically (~2.5x/level, "
            "unbounded) while normalized a_k converges; the connected (2,1) channel holds "
            "a stable ~51% share. The jet tower DOES supply extensive-capable growth; the "
            "open piece is the level-selection rule k(A) (GAP-A-3). Exact branching (no "
            "fit); positive redirect, not a closure."
        ),
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "assertions": assertions,
        "allPassed": all_ok,
        "result": {
            "tower_weights_by_k": rows,
            "w_std_successive_deltas_k5plus": [
                fmt(abs(mp.mpf(rows[k]['w_std']) - mp.mpf(rows[k - 1]['w_std'])))
                for k in range(5, K + 1)],
            "verdict": verdict,
        },
        "context": {
            "builds_on": "wlambda_nuclear_braid_connected_probe.py (fixed-H_3 per-bond shrinkage)",
            "exact_branching": "jet_knot_invariants.py (count_syt_skew + W_lambda=d_q^2/[k]_q!)",
            "redirect": "extensive-capable growth IS in the tower; open piece is the level-selection rule k(A) = GAP-A-3 (categorical brane-tower level selection)",
            "scope": "mechanism triage; positive redirect; no fit; no wiring; no closure; does NOT set k(A)",
        },
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    # Payload carries a top-level `assertions` mapping → stamp preserves it.
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = os.path.join(_HERE, "wlambda-jet-tower-connected.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
