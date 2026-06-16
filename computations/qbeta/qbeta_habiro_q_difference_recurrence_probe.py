"""qbeta_habiro_q_difference_recurrence_probe.py — Topic 1 of PR #1713.

**Phase B symbolic q-difference attack** on the Q_β Habiro element.
Per `docs/coordination/2026-06-02-qbeta-habiro-element-scope.md`:

> Topic 1 target: find the fibre-level Habiro element F(q) whose
> archimedean evaluation at any q_0 reproduces c_k at that anchor.

A natural test: the canonical Habiro elements satisfy a 2-step
q-difference recurrence

    a_{k+1}(q) = G_k(q) · a_k(q)            (Habiro lattice action)
    or         a_{k+1}(q²) = G_k(q) · a_k(q)  (q-Frobenius action)

where G_k(q) is a polynomial in q. The SDP-extracted c_k values
(`qbeta-decay-sdp-extended-ck.witness.json`, c_2..c_10 at 50 dps)
are archimedean evaluations at q_0. If the underlying F(q) has a
clean q-difference structure, the c_k should satisfy *some* linear
recurrence with q_0-evaluated polynomial coefficients.

This probe:
  1. Loads the SDP c_k values (50 dps).
  2. Tests three candidate fibre-level structures:
     (a) Simple ratio test: r_k = c_{k+1} / c_k — does r_k follow a
         pattern consistent with G_k(q_0)?
     (b) 2-term homogeneous linear-recurrence test with constant
         q_0-evaluated coefficients: c_{n+1} = α · c_n + β · c_{n-1}.
         Solved per (n−1, n, n+1, n+2) triple via 2×2 `lu_solve`
         (mpmath); reports α/β spread across triples — constant
         spread = recurrence holds, large spread = refutation.
         (Note: not a PSLQ-style integer-relation search, despite
         legacy naming in the implementation; renamed below.)
     (c) Logarithmic-derivative test: u · d/du log F(u) — if F is
         meromorphic with a clean pole structure, this should
         simplify.
  3. Reports each candidate's residual at 50 dps.

NO ansatz fits per CLAUDE.md §"Q_β c_k truncation order" — this is
a STRUCTURAL TEST, reporting tiered (proved / near-match / refuted).
Each candidate either passes (clean recurrence, structural finding)
or fails (refutes that specific fibre-level structure, narrows the
search space).

Ref: docs/coordination/2026-06-02-qbeta-habiro-element-scope.md
Ref: docs/audits/2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md
Ref: docs/audits/2026-06-01-qbeta-eigenphase-not-f-falsified-at-u1.md
Ref: qbeta-decay-sdp-extended-ck.witness.json (c_k data)
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02). Mirrors
# the sibling pattern in qbeta_per_block_symbolic.py: puts the parent
# computations/ dir on sys.path so `from _path_bridge` resolves, then
# the bridge puts every other cluster subdir on sys.path so
# flat-namespace imports (`_precision`, `witness_base`, `q_parameter`)
# work. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json  # noqa: E402
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q_CANONICAL  # noqa: E402

set_compute_dps()

q = mp.mpf(str(Q_CANONICAL))
h = q - 1 / q              # Hecke skein parameter
hbar_q = 1 - 1 / q         # ℏ_q
b_sq = (q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2   # b² (from #1602 audit)
b = mp.sqrt(b_sq)
u = b * hbar_q ** 2        # Q_β precision-ladder variable


def load_ck_data() -> dict[int, mp.mpf]:
    """Load c_2..c_10 at 50 dps from the SDP extraction witness.

    HERE = computations/qbeta — so the sibling
    witness lives at HERE / "qbeta-decay-sdp-extended-ck.witness.json"
    primarily. Fall back to a nested ../qbeta/ path only if the
    parent layout ever flips (Gemini #1713 review: prior code had
    the order reversed). Uses `with` for clean file-descriptor
    closure.
    """
    path = HERE / "qbeta-decay-sdp-extended-ck.witness.json"
    if not path.exists():
        path = HERE.parent / "qbeta" / "qbeta-decay-sdp-extended-ck.witness.json"
    with path.open() as f:
        d = json.load(f)
    raw = d["data"]["c_k_extracted_50dps"]
    return {int(k.split("_")[1]): mp.mpf(str(v)) for k, v in raw.items()}


def test_ratio_pattern(ck: dict[int, mp.mpf]) -> dict:
    """Test (a) Simple ratio r_k = c_{k+1} / c_k.

    If F(q) satisfies a_{k+1} = G_k(q) · a_k with G_k a polynomial
    in q with bounded-degree coefficients, the ratios should be
    structured (e.g. integer-like for fixed q_0, or recognizable
    polynomial values in q_0 / h / u).
    """
    out = {"name": "ratio_pattern"}
    ratios = []
    ks = sorted(ck.keys())
    for i in range(len(ks) - 1):
        k_a, k_b = ks[i], ks[i + 1]
        if abs(ck[k_a]) > mp.mpf("1e-40"):
            r = ck[k_b] / ck[k_a]
            ratios.append((k_a, k_b, r))
            out[f"r_{k_a}_to_{k_b}"] = mp.nstr(r, 8)
    # Look at log ratios — exponential growth signature
    if len(ratios) >= 3:
        log_ratios = [mp.log(abs(r)) for _, _, r in ratios]
        # Differences of log ratios = log of "ratio of ratios"
        diffs = [log_ratios[i + 1] - log_ratios[i] for i in range(len(log_ratios) - 1)]
        out["log_ratio_growth_first_3_diffs"] = [mp.nstr(d, 6) for d in diffs[:3]]
        # If diffs are constant → exponential growth (geometric series)
        # If diffs are linear in k → factorial-like growth
        mean = sum(diffs) / len(diffs)
        var = sum((d - mean) ** 2 for d in diffs) / len(diffs)
        out["log_ratio_growth_std_over_mean"] = mp.nstr(
            mp.sqrt(var) / abs(mean) if abs(mean) > 1e-40 else mp.inf, 4
        )
    return out


def test_pslq_recurrence(ck: dict[int, mp.mpf]) -> dict:
    """Test (b): 2-term **homogeneous** linear recurrence with constant
    coefficients: ``c_{n+1} = α · c_n + β · c_{n-1}``.

    For each (n−1, n, n+1, n+2) triple, solve for constants α, β via
    a 2×2 linear system (mpmath ``lu_solve``, not PSLQ — the legacy
    ``pslq_2term_recurrence`` name in `out["name"]` is preserved for
    witness-key continuity but does NOT involve PSLQ / integer-
    relation detection):

        [c_n,    c_{n-1}]   [α]   [c_{n+1}]
        [c_{n+1}, c_n   ]   [β] = [c_{n+2}]

    Then report α-spread and β-spread across triples — if both spreads
    are < 1 %, a constant-coefficient recurrence holds. Otherwise it
    is refuted.
    """
    out = {"name": "pslq_2term_recurrence"}  # legacy key, see docstring
    ks = sorted(ck.keys())
    if len(ks) < 4:
        out["note"] = "need >=4 c_k values for 2-term recurrence test"
        return out

    # Test consistency: do α, β satisfy the SAME relation across triples?
    triples = []
    for i in range(1, len(ks) - 2):
        k0, k1, k2, k3 = ks[i - 1], ks[i], ks[i + 1], ks[i + 2]
        if k1 - k0 == 1 and k2 - k1 == 1 and k3 - k2 == 1:
            # Solve [c2 c1; c1 c0] · [α; β] = [c3; c2]
            try:
                M = mp.matrix([
                    [ck[k1], ck[k0]],
                    [ck[k2], ck[k1]],
                ])
                rhs = mp.matrix([[ck[k2]], [ck[k3]]])
                sol = mp.lu_solve(M, rhs)
                alpha, beta = sol[0, 0], sol[1, 0]
                triples.append((k0, alpha, beta))
            except Exception as e:
                triples.append((k0, mp.inf, mp.inf))
    if triples:
        for k0, a, b_ in triples[:5]:
            out[f"alpha_at_k={k0}"] = mp.nstr(a, 10)
            out[f"beta_at_k={k0}"]  = mp.nstr(b_, 10)
        # If recurrence holds, α and β should be CONSTANT across triples
        alphas = [a for _, a, _ in triples if a != mp.inf]
        betas  = [b_ for _, _, b_ in triples if b_ != mp.inf]
        if len(alphas) >= 2:
            alpha_var = max(abs(a - alphas[0]) / max(abs(alphas[0]), mp.mpf("1e-40")) for a in alphas)
            beta_var  = max(abs(b_ - betas[0])  / max(abs(betas[0]),  mp.mpf("1e-40")) for b_ in betas)
            out["alpha_relative_spread"] = mp.nstr(alpha_var, 4)
            out["beta_relative_spread"]  = mp.nstr(beta_var, 4)
            out["recurrence_holds_within_1pct"] = bool(alpha_var < mp.mpf("0.01") and beta_var < mp.mpf("0.01"))
    return out


def test_log_derivative(ck: dict[int, mp.mpf]) -> dict:
    """Test (c) Logarithmic-derivative of F via the partial-sum
    F_N(u) = Π_{k=2..N} (1 + c_k u^k) at q_0.

    Compute log F_N(u_substrate) for N=2..max, then fit a clean
    closed form in u. If F has structure log F = G(u) where G is
    a polynomial / simple rational in u, the partial-sum log
    will reveal it.
    """
    out = {"name": "log_F_partial_sums"}
    ks = sorted(ck.keys())
    log_F = mp.mpf(0)
    for k in ks:
        contrib = mp.log(1 + ck[k] * u ** k)
        log_F += contrib
        out[f"log_F_N={k}"] = mp.nstr(log_F, 12)
        out[f"contrib_c{k}_u{k}"] = mp.nstr(contrib, 12)
    # u-power expansion of log F (numerical Taylor coefficients
    # via the actual c_k input)
    out["u_value_at_q0"] = mp.nstr(u, 12)
    return out


def main() -> int:
    print(f"Q_β Habiro q-difference recurrence probe @ q_0 = {mp.nstr(q, 12)}")
    print(f"  u = b·ℏ_q² = {mp.nstr(u, 12)}")
    print(f"  b² = {mp.nstr(b_sq, 12)}")
    print()

    ck = load_ck_data()
    print(f"Loaded c_2..c_{max(ck)} from SDP-extended witness:")
    for k in sorted(ck.keys()):
        print(f"  c_{k} = {mp.nstr(ck[k], 14)}")
    print()

    # (a) Ratio pattern
    r = test_ratio_pattern(ck)
    print(f"--- (a) Ratio pattern test ---")
    for k, v in r.items():
        if k != "name":
            print(f"  {k}: {v}")
    print()

    # (b) PSLQ 2-term recurrence
    rec = test_pslq_recurrence(ck)
    print(f"--- (b) 2-term recurrence test ---")
    for k, v in rec.items():
        if k != "name":
            print(f"  {k}: {v}")
    print()

    # (c) Log-F partial sums
    lf = test_log_derivative(ck)
    print(f"--- (c) Log F partial sums ---")
    for k, v in lf.items():
        if k != "name":
            print(f"  {k}: {v}")
    print()

    # Witness
    w = WitnessBuilder("qbeta-habiro-q-difference-recurrence-probe", engine="mpmath")
    w.set_description(
        "Topic 1 of PR #1713 / PR #1698 follow-up: tests whether the "
        "SDP-extracted Q_β c_k (c_2..c_10, 50 dps) satisfy a fibre-level "
        "q-difference recurrence. Three candidates: (a) ratio pattern, "
        "(b) 2-term linear recurrence c_{k+1} = α·c_k + β·c_{k-1} with "
        "constant α/β, (c) log F partial sums for clean-closed-form "
        "detection. Reports tiered (no ansatz fits): each candidate "
        "passes (recurrence holds) or fails (refutes that structure)."
    )
    for k, v in r.items():
        if k != "name":
            w.add_data(f"ratio_{k}", str(v))
    for k, v in rec.items():
        if k != "name":
            w.add_data(f"rec_{k}", str(v))
    for k, v in lf.items():
        if k != "name":
            # Per Copilot #1713 review: avoid the `log_log_F_N=2`
            # double-prefix that arose when source keys already start
            # with "log_". Just pass the source key through.
            w.add_data(k, str(v))

    # Pass/fail assertion: recurrence either holds within 1% or not
    recur_holds = rec.get("recurrence_holds_within_1pct", False)
    w.add_assertion(
        name="qbeta_2term_recurrence_holds_within_1pct",
        computed=bool(recur_holds),
        expected=False,   # honest: structural test, default expectation is refutation
        tolerance=0,
        source="Phase B symbolic q-difference attack (Topic 1 of PR #1713)",
    )

    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
