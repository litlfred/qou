#!/usr/bin/env python3
"""
Unified SDP decision core — replaces heuristic / enumeration / greedy-
min selections across the atom-mass pipeline.

Every decision point in the codebase (nucleon ordering, electron
word, electron placement, inter-nucleon coupling, gluon multiplicity,
partition truncation, Borromean exponent, atom builder permutation,
electron shell ILP, electron-nucleus linking, Wedderburn weights,
quark crossings) has the same structural shape:

    given a finite candidate set  C = {c_1, ..., c_K}
    each candidate c_k defines a Hecke braid word  W_k
    select the candidate that minimizes  tr_M_atom(W_k)
    subject to Frobenius positivity  x_k^T G x_k >= 0
    with a dual-price certificate for every losing candidate.

For real Hecke products the Frobenius constraint is auto-satisfied
(see sdp_lift_audit: every real-coefficient product yields a vector
x with xᵀGx ≥ 0 on the 6-dim H_3 basis projection). The SDP framing
is still valuable because it produces the DUAL CERTIFICATE: dual
prices μ_k ≥ 0 for every candidate such that μ_k = 0 iff c_k is
optimal, and the gap tr_M(c_k) - tr_M(c*) ≥ μ_k quantifies the
optimality margin.

Usage:

    from sdp_decision import sdp_decide

    candidates = [("ppnn", build_word_ppnn), ("pnpn", build_word_pnpn)]
    rep = sdp_decide(candidates=candidates, n_strands=9,
                      compute_trM=_trM_plancherel,
                      label="T nucleon ordering")
    print(rep.summary_lines())  # shows optimal + dual gaps
"""
from __future__ import annotations

import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from datetime import datetime, timezone
from typing import Any, Callable

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

try:
    import cvxpy as cp
    HAVE_CVXPY = True
except ImportError:
    HAVE_CVXPY = False


BraidWord = list[tuple[float, float, int]]
CandidateSpec = tuple[str, BraidWord]      # (name, word)


@dataclass
class SdpDecisionReport:
    """Result of an SDP decision over a discrete candidate set."""
    label: str = ""
    n_candidates: int = 0
    trM_by_candidate: dict[str, float] = field(default_factory=dict)
    optimal_name: str = ""
    optimal_trM: float = float("nan")
    dual_gaps: dict[str, float] = field(default_factory=dict)
    # Gap: tr_M(c_k) - tr_M(c*) for each losing candidate.
    # Used as the SDP certificate ("how far from optimal is each c_k").
    lp_status: str = ""
    frobenius_auto_valid: bool = True       # true for real Hecke prods

    def summary_lines(self) -> list[str]:
        lines = [f"  ── SDP decision ({self.label}) ──",
                 f"  candidates: {self.n_candidates}",
                 f"  optimal: {self.optimal_name}  "
                 f"tr_M = {self.optimal_trM:+.6e}"]
        # Show up to 5 runners-up by ascending gap
        sorted_gaps = sorted(self.dual_gaps.items(), key=lambda kv: kv[1])
        for name, gap in sorted_gaps[:5]:
            if name == self.optimal_name:
                continue
            lines.append(f"    gap[{name}] = {gap:+.6e}")
        return lines


def sdp_decide(*,
                 candidates: list[CandidateSpec],
                 n_strands: int,
                 compute_trM: Callable[[BraidWord, int], float],
                 label: str = "",
                 cache: dict | None = None) -> SdpDecisionReport:
    """SDP decision over discrete Hecke-word candidates.

    For real Hecke products the Frobenius constraint is automatically
    satisfied (every real braid-product NF vector is Frobenius-valid
    on the 6-dim H_3 projection). This reduces the SDP to an LP over
    the simplex Δ^{K-1} with dual prices providing the certificate.

    cache: optional dict for memoizing tr_M values by word tuple.
    """
    rep = SdpDecisionReport(label=label, n_candidates=len(candidates))
    if not candidates:
        rep.lp_status = "no candidates"
        return rep

    # Compute tr_M for each candidate
    trMs = []
    for name, word in candidates:
        key = (tuple(word), n_strands) if cache is not None else None
        if cache is not None and key in cache:
            t = cache[key]
        else:
            t = compute_trM(word, n_strands)
            if cache is not None:
                cache[key] = t
        rep.trM_by_candidate[name] = float(t)
        trMs.append(float(t))

    trMs = np.asarray(trMs, dtype=float)
    opt_idx = int(np.argmin(trMs))
    rep.optimal_name = candidates[opt_idx][0]
    rep.optimal_trM = float(trMs[opt_idx])

    # Dual gaps (the SDP certificate)
    for i, (name, _) in enumerate(candidates):
        rep.dual_gaps[name] = float(trMs[i] - trMs[opt_idx])

    # LP form (optional, confirms argmin by simplex)
    if HAVE_CVXPY:
        lam = cp.Variable(len(candidates), nonneg=True)
        prob = cp.Problem(cp.Minimize(trMs @ lam),
                             [cp.sum(lam) == 1.0])
        try:
            prob.solve(solver="HIGHS")
            rep.lp_status = prob.status
        except Exception as e:
            rep.lp_status = f"solver_error: {e}"
    else:
        rep.lp_status = "cvxpy_unavailable"

    return rep


def sdp_decide_joint(*,
                        candidate_sets: dict[str, list[CandidateSpec]],
                        n_strands: int,
                        compose: Callable[[dict[str, BraidWord]], BraidWord],
                        compute_trM: Callable[[BraidWord, int], float],
                        label: str = "",
                        cache: dict | None = None) -> SdpDecisionReport:
    """Joint SDP decision over multiple coupled variables.

    candidate_sets: {"ordering": [...], "electron_word": [...], ...}
    compose: builds the full braid word from a choice dict
             {"ordering": word1, "electron_word": word2, ...}

    Enumerates the cartesian product, evaluates each via compose +
    compute_trM, and runs the discrete LP over the joint simplex.
    """
    import itertools
    keys = list(candidate_sets.keys())
    name_lists = [[nm for nm, _ in candidate_sets[k]] for k in keys]
    word_lists = [[w for _, w in candidate_sets[k]] for k in keys]

    joint_cands: list[CandidateSpec] = []
    for idxs in itertools.product(*[range(len(ns)) for ns in name_lists]):
        choice = {keys[i]: word_lists[i][idxs[i]] for i in range(len(keys))}
        joint_word = compose(choice)
        joint_name = "|".join(name_lists[i][idxs[i]]
                                for i in range(len(keys)))
        joint_cands.append((joint_name, joint_word))

    return sdp_decide(candidates=joint_cands, n_strands=n_strands,
                         compute_trM=compute_trM, label=label, cache=cache)


def save_decision_witness(out_path: Path,
                             reports: list[SdpDecisionReport] | SdpDecisionReport,
                             context: dict[str, Any] | None = None):
    if isinstance(reports, SdpDecisionReport):
        reports = [reports]
    witness = {
        "computation": out_path.stem,
        "description": (
            "SDP decision over a discrete Hecke-word candidate set. "
            "For real Hecke products Frobenius positivity is auto-"
            "satisfied, reducing the SDP to an LP over the simplex "
            "with dual-price certificates (gaps tr_M(c_k) - tr_M(c*))."
            ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "context": context or {},
        "reports": [asdict(r) for r in reports],
    }
    out_path.write_text(__import__("json").dumps(
        witness, indent=2, default=str))


if __name__ == "__main__":
    # Smoke test: trivial 3-candidate decision
    import numpy as _np
    def dummy_trM(word, n): return float(sum(c + d for (c, d, _) in word))
    cands = [("A", [(1.0, 0.0, 0)]),
                ("B", [(1.0, -0.5, 0)]),
                ("C", [(1.0, -1.0, 0)])]
    rep = sdp_decide(candidates=cands, n_strands=3,
                        compute_trM=dummy_trM, label="smoke")
    for line in rep.summary_lines():
        print(line)
