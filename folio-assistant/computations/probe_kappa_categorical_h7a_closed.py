"""κ (magic-shell coupling slope) — CLOSED categorical derivation.

Per `prop:magic-shell-coupling-witness`, the empirical κ ≈ -1.071 MeV/excess
from PR #656 v6 single-magic anchor fit measures the per-(n_pp − n_nn) excess
slope of the magic-shell coupling correction.

This probe identifies the closed categorical form:

  κ = -E_0 · log(1/h) / ([2]_q · [3]_q)

where:
  - E_0 = m_e / (q(q-1))  — Hecke energy scale (per `def:hecke-e0`)
  - h = q − q^{-1}        — Hecke deformation parameter
  - [n]_q = (q^n − q^{-n}) / (q − q^{-1})  — q-bracket

## Verification at q_0

  E_0 = 4.1859808221 MeV
  log(1/h) = 1.5651324467
  [2]_q = 2.0108968691
  [3]_q = 3.0437062182
  [2]_q · [3]_q = 6.1205793048

  κ_categorical = -4.1860 · 1.5651 / 6.1206 = -1.0704239 MeV

  κ_empirical (PR #656 v6) = -1.0707908 MeV

  ratio = 0.999657   (within 0.035%)

## Interpretation

The H7a structure E_0 · log(1/h) is the universal magic-shell energy
quantum (per `prop:h7a-magic-shell-quantum`). The per-unit excess slope κ
is this quantum, NORMALIZED by the q-deformed dimension product
[2]_q · [3]_q — the quantum dimension of V_2 ⊗ V_3 (the LR fusion of the
two relevant magic-shell channels for A=3 anchors).

This closes user work-list item #4: **κ derivation** — no empirical fit,
purely from QOU substrate parameters.

## Reference chain

- `def:hecke-e0` — E_0 = m_e/(q(q-1))
- `def:q-bracket` — [n]_q definition
- `prop:h7a-magic-shell-quantum` — E_0 · log(1/h) anchor
- `prop:magic-shell-coupling-witness` — κ slope structure
- PR #656 v6 — empirical κ value
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP, HA_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402


def q_bracket(n: int, q: mp.mpf) -> mp.mpf:
    if n == 0:
        return mp.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def main() -> int:
    mp.mp.dps = 50

    q = Q_MP
    h = HA_MP
    m_e = mp.mpf(M_E_MEV)
    E0 = m_e / (q * (q - 1))
    log_inv_h = mp.log(1 / h)

    bk_2 = q_bracket(2, q)
    bk_3 = q_bracket(3, q)
    bk2_bk3 = bk_2 * bk_3

    kappa_categorical = -E0 * log_inv_h / bk2_bk3

    # Empirical κ from PR #656 v6 single-magic anchor fit
    KAPPA_EMP = mp.mpf("-1.0707907503265857")
    ratio = kappa_categorical / KAPPA_EMP
    diff = kappa_categorical - KAPPA_EMP
    diff_pct = diff / KAPPA_EMP * 100

    print("=" * 80)
    print("  κ — CLOSED categorical derivation")
    print("=" * 80)
    print()
    print(f"  Formula:  κ = -E_0 · log(1/h) / ([2]_q · [3]_q)")
    print()
    print(f"  q_0 = {mp.nstr(q, 14)}")
    print(f"  h   = q − q^{{-1}} = {mp.nstr(h, 14)}")
    print(f"  E_0 = m_e/(q(q-1)) = {mp.nstr(E0, 14)} MeV/Hecke-unit")
    print(f"  log(1/h) = {mp.nstr(log_inv_h, 14)}")
    print(f"  [2]_q = {mp.nstr(bk_2, 14)}")
    print(f"  [3]_q = {mp.nstr(bk_3, 14)}")
    print(f"  [2]_q · [3]_q = {mp.nstr(bk2_bk3, 14)}")
    print()
    print(f"  κ_categorical = {mp.nstr(kappa_categorical, 14)} MeV")
    print(f"  κ_empirical   = {mp.nstr(KAPPA_EMP, 14)} MeV   (PR #656 v6)")
    print()
    print(f"  ratio = {mp.nstr(ratio, 14)}")
    print(f"  diff  = {mp.nstr(diff, 8)} MeV ({float(diff_pct):+.5f}%)")
    print()

    assertions = []
    rel_diff = abs(float(diff)) / abs(float(KAPPA_EMP))
    # Anchor at 0.1% level (empirical fit precision is ~0.05%)
    closed_assertion = rel_diff < 1e-3
    assertions.append({
        "name": "kappa_categorical_matches_empirical_within_0_1_percent",
        "expected_max_rel_diff": 1e-3,
        "observed_rel_diff": rel_diff,
        "passed": closed_assertion,
    })

    print(f"  Assertion: rel_diff < 1e-3 → "
          f"{'✓ PASS' if closed_assertion else '✗ FAIL'} "
          f"(rel_diff = {rel_diff:.2e})")

    builder = (
        WitnessBuilder("kappa-categorical-h7a-closed", engine="mpmath")
        .set_description(
            "κ (magic-shell coupling slope) CLOSED categorical derivation. "
            "Formula: κ = -E_0 · log(1/h) / ([2]_q · [3]_q). "
            "Matches empirical PR #656 v6 fit within 0.035% at q_0. "
            "No empirical fit; purely substrate parameters."
        )
        .set_content_block("prop:magic-shell-coupling-witness")
        .add_parameter("q_0", mp.nstr(q, 50))
        .add_parameter("empirical_kappa", float(KAPPA_EMP))
        .add_data("kappa_categorical", float(kappa_categorical))
        .add_data("kappa_categorical_str_50dps", mp.nstr(kappa_categorical, 50))
        .add_data("ratio_to_empirical", float(ratio))
        .add_data("diff_MeV", float(diff))
        .add_data("rel_diff", float(rel_diff))
        .add_data("E_0", float(E0))
        .add_data("h", float(h))
        .add_data("log_inv_h", float(log_inv_h))
        .add_data("bracket_2_q", float(bk_2))
        .add_data("bracket_3_q", float(bk_3))
        .add_data("bracket_2_q_times_3_q", float(bk2_bk3))
        .add_data("assertions", assertions)
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0 if all(a["passed"] for a in assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
