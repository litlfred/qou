#!/usr/bin/env python3
"""
Borromean axial-coupling probe — restored with the cyclic-trivial bug fixed.

The deprecated script evaluated β · σ₁ · β⁻¹.  Any trace-like observable of
that expression is cyclic-trivial:

    tr(β · σ₁ · β⁻¹) = tr(σ₁).

So the old "Borromean suppression" was forced to be 1 identically.

This restored version keeps that identity as a diagnostic, then switches to the
non-conjugate probe β · σ₁, which is at least sensitive to the Borromean word.
It remains an audit-only probe: the full bound-state observable should use the
G⁻¹ + LP-active-set formula, not a raw trace.
"""
from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q
from witness_base import WitnessBuilder

qi = 1.0 / q
ha = q - qi


def sigma1_std() -> list[list[float]]:
    return [[q, 0.0], [1.0, -qi]]


def sigma2_std() -> list[list[float]]:
    return [[-qi, ha], [0.0, q]]


def sigma1_inv_std() -> list[list[float]]:
    s = sigma1_std()
    return [[s[0][0] - ha, s[0][1]], [s[1][0], s[1][1] - ha]]


def sigma2_inv_std() -> list[list[float]]:
    s = sigma2_std()
    return [[s[0][0] - ha, s[0][1]], [s[1][0], s[1][1] - ha]]


def mat_mul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]


def mat_trace(a: list[list[float]]) -> float:
    return a[0][0] + a[1][1]


def mat_id() -> list[list[float]]:
    return [[1.0, 0.0], [0.0, 1.0]]


def evaluate_braid_std(word: list[tuple[str, int]]) -> list[list[float]]:
    result = mat_id()
    for gen, exp in word:
        if gen == "s1":
            mat = sigma1_std() if exp > 0 else sigma1_inv_std()
        else:
            mat = sigma2_std() if exp > 0 else sigma2_inv_std()
        for _ in range(abs(exp)):
            result = mat_mul(result, mat)
    return result


def evaluate_braid_triv(word: list[tuple[str, int]]) -> float:
    result = 1.0
    for _, exp in word:
        result *= (q if exp > 0 else -qi) ** abs(exp)
    return result


def evaluate_braid_sign(word: list[tuple[str, int]]) -> float:
    result = 1.0
    for _, exp in word:
        result *= ((-qi) if exp > 0 else q) ** abs(exp)
    return result


def q_int(n: int) -> float:
    return (q ** n - qi ** n) / ha


def main() -> int:
    beta_borr = [("s1", 1), ("s2", -1), ("s1", 1), ("s2", -1)]
    beta_borr_inv = [("s2", 1), ("s1", -1), ("s2", 1), ("s1", -1)]
    conversion_op = [("s1", 1)]

    cyclic_op = beta_borr + conversion_op + beta_borr_inv
    direct_op = beta_borr + conversion_op
    bare_op = conversion_op

    tr_bare_std = mat_trace(evaluate_braid_std(bare_op))
    tr_bare_triv = evaluate_braid_triv(bare_op)

    tr_cyclic_std = mat_trace(evaluate_braid_std(cyclic_op))
    tr_cyclic_triv = evaluate_braid_triv(cyclic_op)

    tr_direct_std = mat_trace(evaluate_braid_std(direct_op))
    tr_direct_triv = evaluate_braid_triv(direct_op)
    tr_direct_sign = evaluate_braid_sign(direct_op)

    cyclic_suppression = abs(tr_cyclic_std / tr_bare_std)
    direct_channel_ratio = abs(tr_direct_std / tr_direct_triv)
    g_a_naive = 5.0 / 3.0
    g_a_direct_probe = g_a_naive * direct_channel_ratio
    target_g_a = 1.2754

    w = WitnessBuilder("borromean-axial-coupling", engine="python")
    w.set_description(
        "Restored Borromean axial-coupling probe. Diagnoses the cyclic-trivial βσ₁β⁻¹ bug and replaces it with the non-conjugate βσ₁ probe."
    )
    w.set_audit_only("docs/audits/2026-05-07-borromean-axial-coupling-fix.md")
    w.add_parameter("q", float(q))
    w.add_parameter("betaBorr", "σ₁ σ₂⁻¹ σ₁ σ₂⁻¹")
    w.add_parameter("conversionOperator", "σ₁")

    w.add_assertion("cyclic standard trace identity", tr_cyclic_std, tr_bare_std, tolerance=1e-12)
    w.add_assertion("cyclic trivial trace identity", tr_cyclic_triv, tr_bare_triv, tolerance=1e-12)
    w.add_assertion("direct probe breaks cyclic triviality", abs(tr_direct_std - tr_bare_std) > 1e-6, True)
    w.add_assertion("direct probe stays near PDG", abs(g_a_direct_probe - target_g_a) < 0.05, True)

    w.add_data("qIntegers", {
        "[2]_q": q + qi,
        "[3]_q": q_int(3),
        "[4]_q": q_int(4),
        "[5]_q": q_int(5),
    })
    w.add_data("cyclicDiagnostic", {
        "operator": "β · σ₁ · β⁻¹",
        "trStandard": tr_cyclic_std,
        "trTrivial": tr_cyclic_triv,
        "suppression": cyclic_suppression,
    })
    w.add_data("directProbe", {
        "operator": "β · σ₁",
        "trStandard": tr_direct_std,
        "trTrivial": tr_direct_triv,
        "trSign": tr_direct_sign,
        "channelRatioStdOverTriv": direct_channel_ratio,
        "gA_naive": g_a_naive,
        "gA_directProbe": g_a_direct_probe,
        "targetPDG": target_g_a,
        "relativeErrorVsPDG": abs(g_a_direct_probe - target_g_a) / target_g_a,
    })

    w.add_caveat("The old β · σ₁ · β⁻¹ formula is trace-cyclic and cannot encode Borromean suppression.")
    w.add_caveat("The direct β · σ₁ probe is still not the full bound-state observable; the principled formula uses G⁻¹ and the LP active set.")

    out = w.save()
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
