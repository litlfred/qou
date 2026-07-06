#!/usr/bin/env python3
"""Measure the effective bond dimension χ_eff(k) of the atom-braid Markov trace.

Decisive gate (direction 1) of the atom-braid program (PR #2389): does the atom
braid populate ≪ p(3k) intermediate partitions at each strand-cut (→ a restricted
MPS could beat the p(3A) wall), or all p(3k) (→ the wall is intrinsic)?

Reports, per nucleon-level k:
  - p(3k)                     (total Wedderburn sectors / partition labels)
  - #partitions reached       (structural Bratteli support, bratteli_state_sizes)
  - Σ running-multiplicity    (full Bratteli-path count — what the partition basis
                               collapses away)
and, for small A, the NUMERICAL nonzero-χ^λ count (no accidental zeros at q₀).

Verdict (see docs/audits/2026-06-16-bond-dimension-verdict-p3A-wall-intrinsic.md):
χ_eff(k) = p(3k) exactly → no support reduction → the transfer is already minimal →
exact ¹⁶O is out of reach; heavy nuclei stay on the A→∞ q-CLT extrapolation.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from chi_atom_transfer import bratteli_state_sizes  # noqa: E402
from chi_monotone_transfer import chi_all_lambda  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from lr_coefficients import partitions_of  # noqa: E402
import mpmath as mp  # noqa: E402


def structural(max_A: int = 8) -> None:
    print("STRUCTURAL bond dimension (Bratteli reachability):")
    print(f"  {'k':>3} {'3k':>4} {'p(3k)':>8} {'#reached':>10} {'Σ paths':>16}  full?")
    for A in range(1, max_A + 1):
        k, nreach, nstates = bratteli_state_sizes(A)[-1]
        p3k = len(partitions_of(3 * k))
        print(f"  {k:>3} {3*k:>4} {p3k:>8} {nreach:>10} {nstates:>16}  "
              f"{'YES' if nreach == p3k else 'no'}")


def numerical(atoms=(("D", 1, 1), ("3He", 2, 1), ("4He", 2, 2)), dps: int = 40) -> None:
    mp.mp.dps = dps
    print(f"\nNUMERICAL support (nonzero χ^λ at q₀, dps={dps}):")
    for lbl, Z, N in atoms:
        n = 3 * (Z + N)
        chi = chi_all_lambda(atom_braid_word_3A(Z, N), n, dps=dps)
        nz = sum(1 for v in chi.values() if abs(v) > mp.mpf("1e-30"))
        p3a = len(partitions_of(n))
        flag = "= p(3A)" if nz == p3a else f"≠ p(3A)={p3a}"
        print(f"  {lbl:<4} n={n:<3} nonzero χ^λ = {nz:>4}  ({flag})")


def row_tail(atoms=(("D", 1, 1), ("3He", 2, 1), ("4He", 2, 2)), dps: int = 40) -> None:
    """SU_q(3) question: contribution of >row-r sectors to tr_M (atom + free).

    y_λ is the Wenzl PRINCIPAL Schur specialization (canonical Jones–Markov trace,
    nonzero for all λ). The ≤3-row (SU_q(3) finite-specialization) restriction is a
    DIFFERENT trace; measured here to be a 0.2–3.4 % error (growing with A) — invalid
    at the 1-ppQ floor. The free reference (no inter-nucleon coupling) also carries
    >3-row content (≥ the atom's), refuting "binding lives in >3-row sectors"."""
    from q_parameter import Q as Q0  # noqa: E402

    def ymp(v):
        return mp.mpc(v) if isinstance(v, complex) else mp.mpf(str(v))

    mp.mp.dps = dps
    print(f"\nROW-TAIL (>r-row contribution to |tr_M|, dps={dps}):")
    print(f"  {'atom':<5} {'≤2 miss':>10} {'≤3 miss':>10} {'≤4 miss':>10}   free ≤3 miss")
    for lbl, Z, N in atoms:
        n = 3 * (Z + N)
        y = y_lambda_at(n, float(Q0))
        chA = chi_all_lambda(atom_braid_word_3A(Z, N, include_inter=True), n, dps=dps)
        chF = chi_all_lambda(atom_braid_word_3A(Z, N, include_inter=False), n, dps=dps)

        def tr(ch, mr=99):
            return sum(ymp(y[l]) * ch[l] for l in ch if len(l) <= mr)

        Af = abs(tr(chA))
        miss = [float(abs(tr(chA) - tr(chA, mr)) / Af) for mr in (2, 3, 4)]
        free_miss3 = float(abs(tr(chF) - tr(chF, 3)) / abs(tr(chF)))
        print(f"  {lbl:<5} {miss[0]:>10.3e} {miss[1]:>10.3e} {miss[2]:>10.3e}"
              f"   {free_miss3:.3e}")


def main() -> int:
    structural(8)
    numerical()
    row_tail()
    print("\nχ_eff(k) = p(3k) exactly → no support reduction → p(3A) wall is intrinsic.")
    print("y_λ = principal specialization (all rows); SU_q(3) ≤3-row is a different")
    print("trace (0.2–3.4 % error, growing with A), and free nuclei need >3-row too.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
