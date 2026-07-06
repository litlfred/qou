"""m_p_linking_weight_operator_valued_probe.py — Topic 2 of PR #1712.

Tests whether an **operator-valued** linking_weight (not the uniform
H_4 Wedderburn average) at q_0 reproduces the CODATA-implied target
2.461648, closing PR #1698's +2.89% m_p gap structurally.

## Target

PR #1698 (`docs/audits/2026-06-02-subgoal-1-final-verdict.md`):

  linking_weight_family_a(q_0) = (3q² + 4 + 3q⁻²)/4 = 2.532780  ← uniform H_4 avg
  CODATA-implied (round-trips m_p)                = 2.461648
  GAP                                              = +28900 ppm = +2.89%

Closing this single number auto-closes the periodic table (per PR
#1698 H2 magic-A finding: gap is quasi-uniform across A=1→56).

## Hypotheses tested

For each Wedderburn-weight function w : P(n) → ℝ, compute

    L(n, w; q_0) = Σ_{λ⊢n} w(λ) · dim_q(λ)
                 -----------------------
                   Σ_{λ⊢n} w(λ)

at n=3,4,5 (proton's strand count is 3; the H_4 Family A average uses
n=4 by convention; n=5 is next-rank). Tested weights — all canonical
categorical objects, NO fits:

| weight | formula | categorical meaning |
|---|---|---|
| `uniform`  | w_λ = 1                          | the H_4 Family A baseline (= 2.5328 at n=4) |
| `dim_q`    | w_λ = dim_q(λ)                   | first-moment self-weighted |
| `dim_q²`   | w_λ = dim_q(λ)²                  | q-Plancherel measure on partitions (KLR-canonical) |
| `1/dim_q`  | w_λ = 1/dim_q(λ)                 | Frobenius co-Casimir reciprocal (T4 prefactor) |
| `[hook]_q`    | w_λ = Σ_h 1/[h]_q                | q-deformed hook density |
| `y_λ`         | w_λ = dim_q²(λ)/[n]_q!           | Wenzl weight (mass-formula T1) |
| `abs_content` | w_λ = Σ_cell \|j − i\|             | per-partition |content| sum (per sibling #1709 Δ_λ binding-measure scan) |

Reports tiered: PASS within 1 ppm = structural finding; PASS within
1% = near-match (not closure); FAIL = refute.

## Forbidden (AGENTS.md)

- NO ansatz fits — every weight w is a pre-existing canonical
  categorical object.
- NO retrofitting toward 2.461648 — pass/fail reported as-is.

Ref: docs/coordination/2026-06-02-m-p-linking-weight-and-binding-link-scope.md
Ref: docs/audits/2026-06-02-subgoal-1-final-verdict.md
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# Phase 5 path bridge (2026-06-02): puts every cluster subdir on
# sys.path so flat-namespace imports (`_precision`, `q_parameter`)
# resolve. Idempotent.
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from q_parameter import Q as Q_CANONICAL  # noqa: E402
from murnaghan_nakayama import dim_q_lambda  # noqa: E402
from partition_utils import hook_lengths  # noqa: E402 — centralized hook-length util

set_compute_dps()

q = mp.mpf(str(Q_CANONICAL))
TARGET = mp.mpf("2.461648")     # CODATA-implied (from PR #1698 linking-weight-residual-fix witness)
FAMILY_A = mp.mpf("2.532780")   # uniform H_4 average (production)


def partitions_of(n: int):
    """All integer partitions of n as descending tuples."""
    if n == 0:
        yield ()
        return

    def helper(m: int, mx: int):
        for f in range(min(m, mx), 0, -1):
            if f == m:
                yield (f,)
            else:
                for r in helper(m - f, f):
                    yield (f,) + r

    yield from helper(n, n)


def n_q(k: int) -> mp.mpf:
    """[k]_q = (q^k − q^{−k}) / (q − q^{−1})."""
    return (q ** k - q ** (-k)) / (q - 1 / q)


def n_q_factorial(k: int) -> mp.mpf:
    """[k]_q! = Π_{j=1..k} [j]_q."""
    p = mp.mpf(1)
    for j in range(1, k + 1):
        p *= n_q(j)
    return p


# (hook_lengths centralized in partition_utils — imported above.)


def _abs_content_sum(lam: tuple[int, ...]) -> mp.mpf:
    """Σ_cell |content(cell)| where content(i, j) = j - i (0-indexed)
    on partition cells. Per sibling PR #1709 (Δ_λ binding-measure
    search, 2026-06-02): abs_content matched A-growth (13.40 vs 12.72)
    in their per-block measure scan. Added here for cross-check
    coverage on the linking_weight target."""
    rows = list(lam)
    s = mp.mpf(0)
    for i, row in enumerate(rows):
        for j in range(row):
            s += abs(j - i)
    return s


WEIGHTS = {
    "uniform":      lambda lam, n: mp.mpf(1),
    "dim_q":        lambda lam, n: dim_q_lambda(lam, q),
    "dim_q_sq":     lambda lam, n: dim_q_lambda(lam, q) ** 2,
    "recip_dim_q":  lambda lam, n: 1 / dim_q_lambda(lam, q),
    "hook_q_inv":   lambda lam, n: sum(1 / n_q(h) for h in hook_lengths(lam)),
    "y_lambda":     lambda lam, n: dim_q_lambda(lam, q) ** 2 / n_q_factorial(n),
    "abs_content":  lambda lam, n: _abs_content_sum(lam) + mp.mpf("1e-30"),
}


def weighted_mean(n: int, weight_name: str) -> mp.mpf:
    """L(n, w; q_0) = Σ w(λ)·dim_q(λ) / Σ w(λ).

    NB: when `weight_name == "uniform"`, normalization is **divide
    by n** (the partition-count, matching Family A's documented
    convention `(Σ_{λ⊢n} dim_q V_λ) / n`), NOT divide by p(n) (the
    number of partitions). Family A at n=4 is (Σ/4), not (Σ/5).
    """
    w_fn = WEIGHTS[weight_name]
    num = mp.mpf(0)
    denom = mp.mpf(0)
    for lam in partitions_of(n):
        w = w_fn(lam, n)
        d = dim_q_lambda(lam, q)
        num += w * d
        denom += w
    if weight_name == "uniform":
        # Family A convention: divide by n, not by p(n).
        return num / mp.mpf(n)
    if denom == 0:
        return mp.inf
    return num / denom


def tier(value: mp.mpf) -> str:
    """Classify how close `value` is to the CODATA target."""
    if value == mp.inf:
        return "INF"
    err = (value / TARGET - 1) * mp.mpf("1e6")  # ppm
    abs_err = abs(err)
    if abs_err < mp.mpf("1"):       return f"PROVED ({mp.nstr(err, 3)} ppm)"
    if abs_err < mp.mpf("1000"):    return f"NEAR-MATCH ({mp.nstr(err, 4)} ppm)"
    if abs_err < mp.mpf("100000"):  return f"WEAK ({mp.nstr(err, 4)} ppm)"
    return f"REFUTED ({mp.nstr(err, 4)} ppm)"


def main() -> int:
    print(f"m_p linking_weight operator-valued probe @ q_0 = {mp.nstr(q, 12)}")
    print(f"  TARGET: 2.461648 (CODATA-implied)")
    print(f"  Family A baseline: 2.532780 (+28900 ppm above target)")
    print()
    print(f"  {'n':>2s}  {'weight':>14s} {'L(n, w; q_0)':>16s}  {'tier':<28s}")
    print("  " + "-" * 70)

    findings: list[dict] = []
    for n in (3, 4, 5):
        for weight_name in WEIGHTS:
            val = weighted_mean(n, weight_name)
            t = tier(val)
            findings.append({"n": n, "weight": weight_name, "value": val, "tier": t})
            mark = ""
            if "PROVED" in t:     mark = " ★ PROVED ★"
            elif "NEAR-MATCH" in t: mark = " ★ NEAR-MATCH ★"
            print(f"  {n:>2d}  {weight_name:>14s} {mp.nstr(val, 12):>16s}  {t:<28s}{mark}")
    print()

    n_proved = sum(1 for f in findings if "PROVED" in f["tier"])
    n_near = sum(1 for f in findings if "NEAR-MATCH" in f["tier"])
    print(f"Verdict: {n_proved} PROVED + {n_near} NEAR-MATCH out of {len(findings)} candidates")

    # Mixed-H_n probe: test α·Family_A(H_3) + (1−α)·Family_A(H_4) for
    # categorically-motivated α values (no fits).
    print()
    print("--- Mixed-H_n test: α · Family_A(H_3) + (1−α) · Family_A(H_4) ---")
    FA_H3 = weighted_mean(3, "uniform")
    FA_H4 = weighted_mean(4, "uniform")
    print(f"  Family_A(H_3) = {mp.nstr(FA_H3, 12)}  (=(2+[2]_q)/3)")
    print(f"  Family_A(H_4) = {mp.nstr(FA_H4, 12)}  (= 2.5328 = production)")
    mixed_findings = []
    for label, alpha in [
        ("1/2 + 1/2",      mp.mpf(1) / 2),
        ("3/4 + 1/4",      mp.mpf(3) / 4),
        ("1/4 + 3/4",      mp.mpf(1) / 4),
        ("h_q² ratio",     (q - 1 / q) ** 2 / 1),       # categorical: h²-scaled
        ("[3]_q / [4]_q",  n_q(3) / n_q(4)),            # categorical: n=3/n=4 q-int ratio
        ("dim_(2,1)/Σ_H4", dim_q_lambda((2, 1), q) /
                            sum(dim_q_lambda(lam, q) for lam in partitions_of(4))),
    ]:
        val = alpha * FA_H3 + (1 - alpha) * FA_H4
        t = tier(val)
        mixed_findings.append({"label": label, "alpha": alpha, "value": val, "tier": t})
        print(f"  α = {label:18s} ({mp.nstr(alpha, 6)}): L = {mp.nstr(val, 10):>14s}  {t}")
    for mf in mixed_findings:
        if "PROVED" in mf["tier"] or "NEAR-MATCH" in mf["tier"]:
            print(f"  ★ Mixed match: α = {mf['label']}")

    w_out = WitnessBuilder("m-p-linking-weight-operator-valued-probe", engine="mpmath")
    w_out.set_description(
        "Topic 2 of PR #1712: tests operator-valued linking_weight at "
        "H_3/H_4/H_5 against the CODATA-implied target 2.461648. Weights "
        "tested are pre-existing canonical categorical objects (uniform, "
        "dim_q, dim_q², 1/dim_q, q-hook density, Wenzl y_λ, abs_content); "
        "no fits. Reports tiered (PROVED <1ppm / NEAR-MATCH <1000ppm / "
        "WEAK / REFUTED). Also runs a mixed-H_n sweep (6 categorically-"
        "motivated α values for α·Family_A(H_3) + (1−α)·Family_A(H_4))."
    )
    for f in findings:
        w_out.add_data(
            f"L_n{f['n']}_{f['weight']}",
            mp.nstr(f["value"], 30),
        )
    w_out.add_assertion(
        name="at_least_one_categorical_weight_passes_1ppm",
        computed=bool(n_proved > 0),
        expected=False,    # honest: structural test, default expectation is refutation
        tolerance=0,
        source="If a single canonical weight passes 1 ppm, that's the m_p closure",
    )
    w_out.add_data("lean_uniqueness_ref", lean_uniqueness_ref("proton"))
    out = w_out.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
