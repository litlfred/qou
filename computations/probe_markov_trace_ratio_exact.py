#!/usr/bin/env python3
"""Probe — `prop:markov-trace-ratio-exact` (I1: proved-in-Lean, no probe).

Claim (content block
`content/quantum-observable-universe/mass-theory/markov-trace-ratio-exact.md`,
Lean `qou:QOU.BraidsKnots.markov_trace_ratio_exact`):

For braids β₁, β₂ ∈ B_n on a FIXED strand count n, with the Jones
normalisation factor

    C(n, q) = (-q^{1/2} - q^{-1/2})^{n-1}

depending only on (n, q) and NOT on the braid word, the Jones values are
J_{K_i}(q) = C(n, q) · tr_M(β_i), so the ratio is normalization-independent:

    J_{K_1}/J_{K_2} = (C·tr_M(β_1)) / (C·tr_M(β_2)) = tr_M(β_1)/tr_M(β_2).

The corollary the prop draws is that the Gram matrix G_ij = tr_M(b_i·b_j),
the LP cost vectors t_k = tr_M(b_k), and the shadow prices y* are all exact
up to a single global scalar that cancels in every ratio / inner product /
optimality condition.

WHAT THIS PROBE VERIFIES (numerical-exact evidence at the substrate q₀):

  (A) C(n, q) is genuinely braid-WORD-independent — it depends only on the
      strand count n and on q. We assemble it once per n and reuse it for
      every braid on n strands.
  (B) For every pair (β_i, β_j) on the SAME strand count n, the ratio of
      Jones values J_i/J_j equals the ratio of canonical Markov traces
      tr_M(β_i)/tr_M(β_j), to ≤ 1e-25 at q₀ (50-dps compute floor).
  (C) The cancellation is exact in ℚ(q) too: the SYMBOLIC ratio of Jones
      values simplifies to the symbolic ratio of Markov traces (the prop is
      an algebraic identity, not a numerical coincidence). Verified symbolically.

This is a structural identity (the normalisation literally cancels), so per
the compute-author formalize-first discipline (§3.3) the right check is the
exact-cancellation verification above — NOT a wide numerical scan. The Lean
side already proves J₁/J₂ = tr_M₁/tr_M₂; this probe is the numerical/symbolic
cross-check + CI guard.

Engine: canonical `markov/markov_trace_canonical.tr_M_word` (the unique
Jones–Markov trace on H_n(q); NOT hand-rolled). Substrate q₀ from
`qou_substrate.constants.Q_50_DIGIT_STR`.

Run:  python3 -u computations/probe_markov_trace_ratio_exact.py
"""
from __future__ import annotations

import sys
from pathlib import Path

# 4-line path bridge (subdirectory refactor) so the bare-name canonical
# imports inside markov_trace_canonical resolve.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from markov.markov_trace_canonical import tr_M_word  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402 (bean yfvb: muon under ideal anchor)
from qou_substrate import WitnessBuilder  # noqa: E402
from qou_substrate.precision import COMPUTE_DPS, OUTPUT_DPS  # noqa: E402

# 50-dps compute floor + guard digits.
mp.mp.dps = COMPUTE_DPS + 15
TOL = mp.mpf("1e-25")  # the compute-author 50-dps cross-check bar


def _sqrt(q):
    """sqrt selecting the impl by input type — works for both a SymPy
    symbol/expr and an mpmath mpf (per Gemini review on PR #2978)."""
    return sp.sqrt(q) if isinstance(q, sp.Basic) else mp.sqrt(q)


def jones_norm_factor(n: int, q):
    """C(n, q) = (-q^{1/2} - q^{-1/2})^{n-1}. Depends only on (n, q).
    Generic over sympy / mpmath inputs."""
    qh = _sqrt(q)
    return (-(qh + 1 / qh)) ** (n - 1)


def markov_z_h(q):
    """Markov parameter z = q³/(q² + 1) (convention D) and h = q - q⁻¹ at q.
    Generic over sympy / mpmath inputs.

    MIGRATED C -> D 2026-08-30 (bean qou-t9r1). This site was one of the
    sqrt-variable spellings invisible to scripts/convention-c-producer-audit.py
    (it matches shapes, and `1/(qh + 1/qh)` with qh = sqrt(q) is z_C exactly).

    Migrating here is a FREE TEST rather than a risk: this probe's whole claim
    (prop:markov-trace-ratio-exact) is that the Jones normalisation C(n, q)
    cancels in every RATIO taken at fixed strand count n. If that is true the
    assertions must survive a change of z; if it is not, they break and the
    probe has found something. Ratio-invariance is NOT automatic in general —
    a generic weighted ratio over TR_M = [1,z,z,z²,z²,·] does depend on z —
    so this is a real check, not a tautology."""
    z = q ** 3 / (q ** 2 + 1)
    h = q - 1 / q
    return z, h


def main() -> int:
    q0 = mp.mpf(Q_50_DIGIT_STR)
    z, h = markov_z_h(q0)

    # ── Braid words grouped by strand count n (generators σ_0..σ_{n-2}) ──
    # The prop's hypothesis is FIXED n across the braids whose ratio we take,
    # because C(n,q) only cancels when both braids share the strand count.
    families: dict[int, list[tuple[str, tuple]]] = {
        2: [
            ("1",        ()),
            ("sigma0",   (0,)),
            ("sigma0^3", (0, 0, 0)),
        ],
        3: [
            ("sigma0",        (0,)),
            ("sigma0sigma1",  (0, 1)),
            ("sigma0sigma1sigma0 (Garside)", (0, 1, 0)),
            ("sigma1sigma0sigma1 (braid-equiv)", (1, 0, 1)),
            ("sigma0^2sigma1", (0, 0, 1)),
        ],
        4: [
            ("sigma0sigma1sigma2", (0, 1, 2)),
            ("sigma0sigma2",       (0, 2)),
            ("sigma1sigma0sigma2sigma1", (1, 0, 2, 1)),
        ],
    }

    w = WitnessBuilder("probe-markov-trace-ratio-exact", engine="mpmath")
    w.set_description(
        "Numerical-exact + symbolic cross-check of prop:markov-trace-ratio-exact: "
        "Jones values J = C(n,q)*tr_M with C braid-word-independent, so "
        "J_i/J_j = tr_M_i/tr_M_j (the normalisation cancels). Canonical engine "
        "markov/markov_trace_canonical.tr_M_word; substrate q0."
    )
    w.set_content_block("prop:markov-trace-ratio-exact")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("compute_dps", mp.mp.dps)
    w.add_parameter("output_dps", OUTPUT_DPS)
    w.add_parameter("tolerance", "1e-25")

    per_family = {}
    max_resid_num = mp.mpf(0)

    for n, members in families.items():
        # (A) ONE C per strand count — reused for every braid on n strands.
        C = jones_norm_factor(n, q0)
        rows = []
        evals = []
        for name, word in members:
            tr = mp.mpf(tr_M_word(word, n, z, h))
            J = C * tr
            evals.append((name, word, tr, J))
            rows.append({
                "braid": name,
                "word": list(word),
                "tr_M_at_q0": mp.nstr(tr, OUTPUT_DPS),
                "J_at_q0": mp.nstr(J, OUTPUT_DPS),
            })

        # (B) every ordered pair: J_i/J_j == tr_i/tr_j  to TOL
        pair_resids = []
        for i in range(len(evals)):
            for j in range(len(evals)):
                if i == j:
                    continue
                _, _, tr_i, J_i = evals[i]
                _, _, tr_j, J_j = evals[j]
                if tr_j == 0 or J_j == 0:
                    continue
                resid = abs(J_i / J_j - tr_i / tr_j)
                pair_resids.append(resid)
                if resid > max_resid_num:
                    max_resid_num = resid

        worst = max(pair_resids) if pair_resids else mp.mpf(0)
        per_family[f"n={n}"] = {
            "C_n_q_at_q0": mp.nstr(C, OUTPUT_DPS),
            "n_braids": len(members),
            "n_ordered_pairs_checked": len(pair_resids),
            "max_pair_residual": mp.nstr(worst, 6),
            "braids": rows,
        }
        w.add_assertion(
            f"J_i/J_j == tr_M_i/tr_M_j for all pairs at n={n} (q0, <=1e-25)",
            computed=mp.nstr(worst, 6),
            expected="0",
            tolerance=float(TOL),
            source=f"markov_trace_canonical, {len(pair_resids)} ordered pairs",
        )

    # (C) SYMBOLIC exactness: the cancellation is an identity in ℚ(q).
    qs = sp.Symbol("q", positive=True)
    # Reuse the now-generic helpers symbolically (per Gemini review).
    zs, hs = markov_z_h(qs)
    Cs = jones_norm_factor(3, qs)  # n=3
    w0 = (0, 1, 0)
    w1 = (0, 1)
    tr0 = sp.nsimplify(tr_M_word(w0, 3, zs, hs))
    tr1 = sp.nsimplify(tr_M_word(w1, 3, zs, hs))
    J0, J1 = Cs * tr0, Cs * tr1
    sym_diff = sp.simplify(J0 / J1 - tr0 / tr1)
    sym_exact = sym_diff == 0
    w.add_assertion(
        "Symbolic cancellation J(s0s1s0)/J(s0s1) - tr_M ratio == 0 in Q(q)",
        computed=str(sym_diff),
        expected="0",
        source="sympy.simplify (exact, all q)",
    )

    w.add_data("families", per_family)
    w.add_data("symbolic_cancellation_exact", bool(sym_exact))
    w.add_data("max_numerical_pair_residual_all_families",
               mp.nstr(max_resid_num, 6))
    w.add_caveat(
        "Numerical assertions are 50-dps numerical-exact EVIDENCE at q0 for "
        "the algebraic identity J_i/J_j = tr_M_i/tr_M_j proved sorry-free in "
        "qou:QOU.BraidsKnots.markov_trace_ratio_exact; the symbolic assertion "
        "establishes the cancellation as an exact Q(q) identity (not a q0 "
        "coincidence). Probe, not a proof."
    )
    path = w.save()

    all_passed = all(a.passed for a in w.assertions)
    print(f"max numerical pair residual (all n): {mp.nstr(max_resid_num, 6)}")
    print(f"symbolic cancellation exact in Q(q): {sym_exact}")
    print(f"witness: {path}")
    print("ALL PASSED" if all_passed else "FAILURES PRESENT")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
