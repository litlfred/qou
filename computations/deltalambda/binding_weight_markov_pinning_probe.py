#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""binding_weight_markov_pinning_probe.py — pin the binding weighting convention: the derived
weight is the Markov y_λ (axiom-solved); the Schur-Weyl/Plancherel W_λ = d_q²/[n]! is DOUBLY
excluded (wrong trace + conjugation-symmetric). Answers the prerequisite surfaced by PR #4491.

The claim (canonical, from wedderburn_jones_markov.py — the module the binding formula imports)
-----------------------------------------------------------------------------------------------
The binding trace is the Markov trace J_L = tr_M(ρ(β_L)) (§7a). The Markov trace on the Hecke tower
is UNIQUE up to normalization (Jones/Wenzl), so its Wedderburn weight is DETERMINED, not chosen. The
canonical module solves it from the Markov axiom (markov_weights_symbolic.solve_y_lambda,
markov_trace_recursive) → y_λ (Wenzl Schur principal specialization), and states the
`schur_weyl_weight = d_q²/[n]!` form is "NOT the Markov-trace weight."

Three structural checks (exact / verified)
------------------------------------------
  (1) y_λ ≠ W_λ  — genuinely different weight systems (n=3 ratios y/W ∈ [0.16, 2.9]).
  (2) W_λ = W_{λ'}  — CONJUGATION-SYMMETRIC, because the hook-length MULTISET is transpose-invariant
      ⇒ d_q(λ) = d_q(λ') ⇒ W_λ = d_q(λ)²/[n]! = W_{λ'}. (Verified for all λ ⊢ n ≤ 7.)
  (3) y_λ is ASYMMETRIC  — y_(3)=0.415 ≠ y_(1,1,1)=0.023. Binding REQUIRES this chirality/bar-parity
      split (GAP-1: a conjugation-symmetric Δ_λ gives g₂=0 for even A). So W_λ, being symmetric,
      CANNOT produce chiral binding — a SECOND, independent exclusion (scope-b, proved invariant).

Consequences
------------
  * three-walls Route 1's 33× W_λ overshoot is EXPLAINED — wrong trace.
  * corpus MISLABEL: alpha_em_b2_scalar_c_probe.py:116 calls d_q²/[n]! the "Markov/Wedderburn weight",
    contradicting the canonical module — flag (do not rewrite here).
  * HONEST REFINEMENT of PR #4491's c-knot-not-universal: the 41× "convention spread" (C_knot 5.85 vs
    240) was right-weight (y_λ, Markov) vs wrong-weight (signed dim_q, NOT Markov) — NOT a genuine
    ambiguity. With the weight PINNED to the derived y_λ, C_knot = 5.85 is well-posed.
  * the C_knot deficit is therefore NOT a weight issue — it lives in f^λ / sgn / E₀ / word-level,
    relocating the open Δ_λ target.

VERDICT (DERIVED pinning + scope-b exclusion): the binding weight is y_λ (Markov axiom); W_λ is
excluded (wrong trace + conjugation-symmetric). This makes the Δ_λ target well-posed. It is NOT a Δ_λ
magnitude derivation (still open, bean qou-3q7t). No fit; nothing wired. Exact (mpmath); W_λ computed
independently (hook lengths, no corpus dep); y_λ read from the canonical module when importable, else
from verified cache.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

Q0 = mp.mpf("1.10997859555733471989976322048322502665620840878015368660798114614493")

# verified y_λ(q0) cache (from the canonical wedderburn_jones_markov.solve_y_lambda; see PR #4543)
Y_LAMBDA_CACHE = {
    2: {(2,): mp.mpf("0.69632542"), (1, 1): mp.mpf("0.30367458")},
    3: {(3,): mp.mpf("0.41539579"), (2, 1): mp.mpf("0.28092963"), (1, 1, 1): mp.mpf("0.022744946")},
}


def qint(k):
    return sum(Q0 ** j for j in range(k)) if k > 0 else mp.mpf(1)


def qfac(k):
    r = mp.mpf(1)
    for j in range(1, k + 1):
        r *= qint(j)
    return r


def hook_multiset(shape):
    rows = list(shape)
    cols = [sum(1 for r in rows if r > c) for c in range(max(rows))]
    return sorted((ri - j - 1) + (cols[j] - i - 1) + 1 for i, ri in enumerate(rows) for j in range(ri))


def conj(shape):
    return tuple(sum(1 for r in shape if r > c) for c in range(max(shape)))


def d_q(shape, n):
    return qfac(n) / mp.fprod([qint(h) for h in hook_multiset(shape)])


def W_lambda(shape, n):
    return d_q(shape, n) ** 2 / qfac(n)


def partitions(n):
    out = []

    def rec(k, mx, cur):
        if k == 0:
            out.append(tuple(cur))
            return
        for p in range(min(k, mx), 0, -1):
            rec(k - p, p, cur + [p])

    rec(n, n, [])
    return out


def get_y_lambda(n):
    """canonical module if importable (numpy stack), else verified cache."""
    try:
        for p in ("computations", "computations/markov", "computations/hecke",
                  "qou-mass/src/qou_mass/_internal"):
            if p not in sys.path:
                sys.path.insert(0, str(ROOT / p))
        from wedderburn_jones_markov import y_lambda_at  # noqa: E402
        raw = y_lambda_at(n, q_val=Q0)
        return {tuple(k) if not isinstance(k, int) else (k,): mp.mpf(str(v)) for k, v in raw.items()}, "canonical-module"
    except Exception:
        return dict(Y_LAMBDA_CACHE.get(n, {})), "verified-cache"


def main() -> int:
    # (2) hook-transpose invariance ⇒ W_λ = W_{λ'} for ALL λ up to n=7
    hook_transpose_ok = all(
        hook_multiset(sh) == hook_multiset(conj(sh))
        for n in range(1, 8) for sh in partitions(n) if max(sh) >= 1)
    w_conj_symmetric = all(
        abs(W_lambda(sh, n) - W_lambda(conj(sh), n)) < mp.mpf("1e-30")
        for n in range(2, 7) for sh in partitions(n))

    # (1)+(3) at n=3: y_λ ≠ W_λ, and y_λ asymmetric while W_λ symmetric
    rows = {}
    y3, y_src = get_y_lambda(3)
    for sh in partitions(3):
        yv = y3.get(sh)
        Wv = W_lambda(sh, 3)
        rows[str(sh)] = {"y_lambda": mp.nstr(yv, 8) if yv is not None else None,
                         "W_lambda": mp.nstr(Wv, 8),
                         "y_over_W": mp.nstr(yv / Wv, 6) if yv is not None else None}
    y_sym = y3.get((3,))
    y_asym = y3.get((1, 1, 1))
    W_sym3 = W_lambda((3,), 3)
    W_asym3 = W_lambda((1, 1, 1), 3)
    y_is_asymmetric = bool(y_sym is not None and y_asym is not None and abs(y_sym - y_asym) > mp.mpf("0.1"))
    W_is_symmetric = bool(abs(W_sym3 - W_asym3) < mp.mpf("1e-30"))
    y_ne_W = bool(y_sym is not None and abs(y_sym - W_sym3) > mp.mpf("0.01"))

    result = {
        "substrate": {"q0": mp.nstr(Q0, 30)},
        "pinning": {
            "binding_trace": "J_L = tr_M(ρ(β_L)) — Markov trace (§7a); unique up to normalization",
            "derived_weight": "y_λ (Wenzl Schur principal specialization), solved from the Markov axiom "
                              "(wedderburn_jones_markov / markov_weights_symbolic.solve_y_lambda)",
            "y_lambda_source": y_src,
            "schur_weyl_is_not_markov": "the d_q²/[n]! form is 'NOT the Markov-trace weight' "
                                        "(canonical module docstring)",
        },
        "check1_y_ne_W": {"rows_n3": rows, "y_ne_W": y_ne_W},
        "check2_W_conjugation_symmetric": {
            "hook_multiset_transpose_invariant_upto_n7": bool(hook_transpose_ok),
            "W_lambda_eq_W_conj_upto_n6": bool(w_conj_symmetric),
            "mechanism": "hook multiset is transpose-invariant ⇒ d_q(λ)=d_q(λ') ⇒ W_λ=W_{λ'}",
        },
        "check3_y_asymmetric_binding_needs_it": {
            "y_(3)": mp.nstr(y_sym, 8) if y_sym is not None else None,
            "y_(1,1,1)": mp.nstr(y_asym, 8) if y_asym is not None else None,
            "y_is_asymmetric": y_is_asymmetric,
            "W_is_symmetric": W_is_symmetric,
            "binding_needs_asymmetry": "GAP-1: a conjugation-symmetric Δ_λ gives g₂=0 for even A; the "
                                       "chiral binding requires the λ↔λ' asymmetry y_λ carries and W_λ "
                                       "washes out. ⇒ W_λ excluded (scope-b, proved invariant).",
        },
        "consequences": {
            "route1_overshoot_explained": "three-walls Route 1's 33× W_λ overshoot = wrong trace",
            "corpus_mislabel": "alpha_em_b2_scalar_c_probe.py:116 calls d_q²/[n]! the 'Markov/Wedderburn "
                               "weight' — contradicts the canonical module; flag (not rewritten here)",
            "c_knot_refinement": "PR #4491's 41× C_knot spread (5.85 vs 240) was right-weight (y_λ) vs "
                                 "wrong-weight (signed dim_q), NOT a genuine ambiguity. With y_λ pinned, "
                                 "C_knot=5.85 is well-posed; the deficit is NOT a weight issue.",
            "relocated_target": "C_knot lives in f^λ / sgn / E₀ / word-level, not the weight.",
        },
        "verdict": {
            "classification": "DERIVED pinning (weight = y_λ, Markov axiom) + scope-(b) exclusion of "
                              "W_λ (conjugation-symmetric ⇒ no chiral binding). Makes the Δ_λ target "
                              "well-posed. NOT a Δ_λ magnitude derivation (open, bean qou-3q7t).",
            "anti_fit": "y_λ read from the canonical Markov-axiom module; W_λ computed independently "
                        "(hook lengths). No fit; nothing wired.",
        },
    }

    this = Path(__file__).resolve()
    witness = {
        "schema": "witness/v1",
        "producer": str(this.relative_to(ROOT)),
        "computation": "binding-weight-markov-pinning",
        "description": (
            "Pin the binding weighting convention. The binding is the Markov trace J_L=tr_M(ρ(β_L)) "
            "(§7a), unique up to normalization, so its Wedderburn weight is DETERMINED: y_λ (Wenzl, "
            "solved from the Markov axiom — canonical wedderburn_jones_markov module). The "
            "Schur-Weyl/Plancherel W_λ=d_q²/[n]! is DOUBLY excluded: (a) 'NOT the Markov-trace weight' "
            "(canonical module) and y_λ≠W_λ (n=3 ratios 0.16–2.9); (b) W_λ is CONJUGATION-SYMMETRIC "
            "(W_λ=W_{λ'} from hook-transpose invariance, verified ≤n=7) while y_λ is ASYMMETRIC "
            "(y_(3)=0.415≠y_(1,1,1)=0.023) — binding requires that chirality (GAP-1: symmetric Δ_λ ⇒ "
            "g₂=0 for even A), so W_λ washes it out (scope-b). Explains three-walls Route 1's 33× W_λ "
            "overshoot (wrong trace); flags the alpha_em_b2_scalar_c_probe:116 mislabel; and refines PR "
            "#4491's C_knot-not-universal (the 41× was right-vs-wrong weight, not genuine ambiguity — "
            "with y_λ pinned, C_knot=5.85 is well-posed, and is NOT a weight issue). DERIVED pinning + "
            "scope-(b) exclusion; NOT a Δ_λ magnitude derivation (open, bean qou-3q7t). No fit; nothing "
            "wired; exact (mpmath)."),
        "audit_only": True,
        "tier": "DERIVED weight pinning (Markov axiom) + scope-(b) W_λ exclusion (conjugation symmetry); no fit",
        "scriptHash": hashlib.sha256(this.read_bytes()).hexdigest()[:16],
        "result": result,
        "context": {"axis": "Δ_λ / binding weight — which weight is derived?",
                    "builds_on": "PR #4491 (C_knot), wedderburn_jones_markov (canonical), three-walls "
                                 "Route 1 (W_λ overshoot), GAP-1 (chirality needed)",
                    "bean": "qou-3q7t", "no_fit": True},
    }
    try:
        witness["scriptCommitSha"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(this)], cwd=this.parent, text=True).strip() or "uncommitted"
    except Exception:
        witness["scriptCommitSha"] = "uncommitted"
    out = HERE / "binding-weight-markov-pinning.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str) + "\n")

    print("=== pin the binding weight: derived = Markov y_λ; W_λ doubly excluded ===")
    print(f"y_λ source: {y_src}")
    print(f"  n=3   λ        y_λ(Markov)     W_λ=d_q²/[n]!    y/W")
    for sh in partitions(3):
        r = rows[str(sh)]
        print(f"        {str(sh):10} {str(r['y_lambda']):>12}   {str(r['W_lambda']):>12}   {r['y_over_W']}")
    print()
    print(f"(1) y_λ ≠ W_λ: {y_ne_W}")
    print(f"(2) W_λ conjugation-SYMMETRIC (hook-transpose ≤n7): {hook_transpose_ok} / W=W' ≤n6: {w_conj_symmetric}")
    print(f"(3) y_λ ASYMMETRIC y_(3)={mp.nstr(y_sym,6)}≠y_(1,1,1)={mp.nstr(y_asym,6)}: {y_is_asymmetric} "
          f"(W symmetric: {W_is_symmetric}) ⇒ W_λ washes out chirality (scope-b exclusion)")
    print()
    print("VERDICT: binding weight PINNED to y_λ (Markov axiom); W_λ excluded (wrong trace + symmetric). "
          "Δ_λ target now well-posed. C_knot=5.85 is NOT a weight issue. Not a magnitude derivation "
          "(open, bean qou-3q7t). No fit.")
    print(f"witness -> {out.name}")

    assert hook_transpose_ok and w_conj_symmetric, "W_λ must be conjugation-symmetric"
    if y_sym is not None:
        assert y_ne_W and y_is_asymmetric and W_is_symmetric, "y_λ≠W_λ, y asymmetric, W symmetric"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
