"""κ (magic-shell coupling slope) categorical derivation via D-2 q-Catalan.

Per PR #656's D-2 candidate, the magic-shell coupling has structure
involving the q-Catalan multiplicity

  Cat_q(A-1, 1) = [A-1]_q · [A-2]_q / ([2]_q · [A]_q)

with the Z/N-dependent SYT-shape correction. The empirical
slope κ ≈ -1.07 MeV/excess (from #656 v6 fit on single-magic anchors).

This probe tests whether κ admits a categorical closed form in terms
of [k]_q brackets at q_0, addressing user work-list item #4
(derive κ).

## Categorical candidate

Per the audit doc `2026-05-15-a-minus-2-q-substrate-derivation.md`:
- At doubly-magic anchor (Z, N) = (2, 2): Δ_coupling closes via
  [A−2]_q · E_0 · log(1/h) — the universal H7a piece survives.
- At single-magic anchors (2, 1) and (1, 2): the H7a prediction
  over-shoots; the residual is the κ · (n_pp − n_nn) · h · E_0 term.

The candidate categorical form for κ from the q-Catalan structure:

  κ_categorical = ((Cat_q(A-1, 1) at the magic anchor) − 1) · E_0 · h

i.e., κ is the deviation of the q-Catalan multiplicity from unity,
scaled by E_0 · h.

## Verification

Compute Cat_q(A-1, 1) at q = q_0 for A = 3 (single-magic anchor),
extract the categorical κ candidate, compare with empirical
-1.07 MeV/excess from #656 v6.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP, HA_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402


def q_bracket(n: int, q: mp.mpf) -> mp.mpf:
    """q-bracket [n]_q = (q^n − q^{-n}) / (q − q^{-1})."""
    if n == 0:
        return mp.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def cat_q(n: int, k: int, q: mp.mpf) -> mp.mpf:
    """q-Catalan number Cat_q(n, k) per D-2 candidate (#656).

    Closed form for the LR-fusion multiplicity in the Wedderburn
    decomposition of the magic-shell coupling channel:
      Cat_q(A-1, 1) = [A-1]_q · [A-2]_q / ([2]_q · [A]_q)
    """
    return (q_bracket(n, q) * q_bracket(n - 1, q)
            / (q_bracket(2, q) * q_bracket(n + 1, q)))


def main() -> int:
    mp.mp.dps = 50

    q = Q_MP
    h = HA_MP
    m_e = mp.mpf(M_E_MEV)
    E0 = m_e / (q * (q - 1))
    log_inv_h = mp.log(1 / h)

    print("=" * 80)
    print("  κ (magic-shell coupling slope) categorical derivation — D-2 q-Catalan")
    print("=" * 80)
    print()
    print(f"  q_0 = {mp.nstr(q, 12)}")
    print(f"  h   = q − q⁻¹  = {mp.nstr(h, 12)}")
    print(f"  E_0 = m_e/(q(q-1)) = {mp.nstr(E0, 12)} MeV/Hecke-unit")
    print()
    print("  ── q-Catalan multiplicities Cat_q(A-1, 1) ──")
    print()
    print(f"  {'A':>3} {'[A-2]_q':>10} {'[A-1]_q':>10} {'[2]_q':>10} {'[A]_q':>10} {'Cat_q':>11}")
    print('  ' + '-' * 60)
    cat_values = {}
    for A in [2, 3, 4, 5, 6]:
        cat = cat_q(A - 1, 1, q)
        cat_values[A] = cat
        print(f"  {A:>3} {float(q_bracket(A-2, q)):>10.6f} "
              f"{float(q_bracket(A-1, q)):>10.6f} "
              f"{float(q_bracket(2, q)):>10.6f} "
              f"{float(q_bracket(A, q)):>10.6f} "
              f"{float(cat):>11.6f}")

    # ── Empirical κ from PR #656 v6 ──
    KAPPA_EMP = mp.mpf("-1.0707907503265857")

    # ── Candidate categorical κ formulae ──
    print()
    print("  ── Categorical κ candidates (vs empirical -1.0708 MeV/excess at A=3) ──")
    print()

    # Candidate 1: κ = (Cat_q(A=3) − 1) · E_0 · h
    cat_A3 = cat_values[3]
    kappa_c1 = (cat_A3 - 1) * E0 * h
    print(f"  C1: κ = (Cat_q(2,1) − 1) · E_0 · h")
    print(f"        = ({float(cat_A3):.6f} − 1) · {float(E0):.4f} · {float(h):.4f}")
    print(f"        = {float(kappa_c1):+.4f} MeV    "
          f"(empirical: {float(KAPPA_EMP):+.4f} MeV; ratio: {float(kappa_c1/KAPPA_EMP):.4f})")
    print()

    # Candidate 2: κ = -[A-2]_q / [A]_q · E_0 · h
    A = 3
    kappa_c2 = -q_bracket(A - 2, q) / q_bracket(A, q) * E0 * h
    print(f"  C2: κ = -[A-2]_q / [A]_q · E_0 · h    (A=3)")
    print(f"        = -{float(q_bracket(A-2, q)):.4f}/{float(q_bracket(A, q)):.4f} · "
          f"{float(E0):.4f} · {float(h):.4f}")
    print(f"        = {float(kappa_c2):+.4f} MeV    "
          f"(ratio: {float(kappa_c2/KAPPA_EMP):.4f})")
    print()

    # Candidate 3: κ = -Cat_q(2, 1) · E_0 · log(1/h)  (mirrors H7a structure)
    kappa_c3 = -cat_A3 * E0 * log_inv_h
    print(f"  C3: κ = -Cat_q(2,1) · E_0 · log(1/h)  (H7a-like)")
    print(f"        = -{float(cat_A3):.6f} · {float(E0):.4f} · {float(log_inv_h):.4f}")
    print(f"        = {float(kappa_c3):+.4f} MeV    "
          f"(ratio: {float(kappa_c3/KAPPA_EMP):.4f})")
    print()

    # Candidate 4: κ = -(1 - Cat_q) · E_0 · log(1/h)
    kappa_c4 = -(1 - cat_A3) * E0 * log_inv_h
    print(f"  C4: κ = -(1 − Cat_q(2,1)) · E_0 · log(1/h)")
    print(f"        = -({1 - float(cat_A3):.6f}) · {float(E0):.4f} · {float(log_inv_h):.4f}")
    print(f"        = {float(kappa_c4):+.4f} MeV    "
          f"(ratio: {float(kappa_c4/KAPPA_EMP):.4f})")
    print()

    # Find best candidate
    candidates = [
        ("C1: (Cat_q − 1) · E_0 · h",                          kappa_c1),
        ("C2: −[A−2]_q/[A]_q · E_0 · h",                       kappa_c2),
        ("C3: −Cat_q · E_0 · log(1/h)",                        kappa_c3),
        ("C4: −(1 − Cat_q) · E_0 · log(1/h)",                  kappa_c4),
    ]
    best = min(candidates, key=lambda kv: abs(kv[1] - KAPPA_EMP))
    print(f"  Best candidate: {best[0]}")
    print(f"    value = {float(best[1]):+.6f} MeV  vs empirical {float(KAPPA_EMP):+.6f} MeV")
    print(f"    diff  = {float(best[1] - KAPPA_EMP):+.4e} MeV")
    print(f"    ratio = {float(best[1] / KAPPA_EMP):.6f}")

    builder = (
        WitnessBuilder("kappa-d2-catalan-derivation", engine="mpmath")
        .set_description(
            "Categorical κ candidates via D-2 q-Catalan (PR #656). "
            "Tests four closed-form candidates against the empirical "
            "κ = -1.07 MeV/excess from #656 v6 single-magic anchor fit."
        )
        .set_content_block("prop:magic-shell-coupling-witness")
        .add_parameter("q_0", mp.nstr(q, 50))
        .add_parameter("empirical_kappa", float(KAPPA_EMP))
        .add_data("cat_q_values",
                  {str(A): float(v) for A, v in cat_values.items()})
        .add_data("candidates", [
            {"label": lbl, "value": float(v), "ratio_to_empirical": float(v / KAPPA_EMP)}
            for lbl, v in candidates
        ])
        .add_data("best_candidate", best[0])
        .add_data("best_value", float(best[1]))
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
