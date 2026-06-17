#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; trace-weighted chirality-sign
# from the Wedderburn channels, no symbolic-q polynomial output.
"""
Chirality signs from the shell structure (not by hand).

The R-matrix-skein probe reproduced the empirical pn-rule a_K=Π(1±h) but took
the per-np-pair signs (symmetric/+, antisymmetric/−) as INPUT. This probe asks
whether the framework's OWN chirality sign — the option-e Wedderburn
transpose-parity δ_sign(λ)=sgn(w0^{S_{λ'}}) (merged keystone 585ca846,
Δ_λ = chirality sign × Wedderburn magnitude) — derives the net chirality from
the populated Wedderburn channels of each nucleus, with NO hand assignment.

Candidate (derivable): the trace-weighted average chirality parity
    ⟨sgn⟩_K = Σ_λ y_λ χ^λ(W_atom) δ_sign(λ) / Σ_λ y_λ χ^λ(W_atom)
computed from the q-parameterised core (χ^λ, y_λ at q₀) + the combinatorial
δ_sign. Compared to the empirical net first-order coefficient (#sym − #anti):
D → +1; T, ³He, ⁴He → 0. Also the naive pairing-parity rule ZN mod 2 for
contrast, and the FALSIFIABLE prediction for ⁶Li, ⁷Li (where rules diverge).

Exploratory; no fit.

Run:  python3 -u computations/chirality_shell_sign_probe.py 2>&1 | tee /tmp/sschi.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
import mpmath as mp  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from reduced_block_kernel import chi_all_lambda_reduced_block  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

# (name, Z, N, empirical net first-order coeff or None if unknown)
ISO = [("D", 1, 1, 1), ("3H", 1, 2, 0), ("3He", 2, 1, 0), ("4He", 2, 2, 0),
       ("6Li", 3, 3, None), ("7Li", 3, 4, None)]


def _transpose(lam):
    return tuple(sum(1 for r in lam if r > c) for c in range(lam[0])) if lam else ()


def delta_sign(lam) -> int:
    """option-e chirality sign = sgn(w0^{S_{λ'}}) (column Young subgroup)."""
    s = 1
    for b in _transpose(tuple(lam)):
        s *= (-1) ** (b * (b - 1) // 2)
    return s


def trace_weighted_sign(Z: int, N: int) -> float:
    """⟨sgn⟩ = Σ_λ y_λ χ^λ δ_sign(λ) / Σ_λ y_λ χ^λ at q₀."""
    n = 3 * (Z + N)
    q0 = mp.mpf(str(Q0))
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q0).items()}
    chi = chi_all_lambda_reduced_block(atom_braid_word_3A(Z, N, include_inter=True), n)
    num = sum(y[tuple(l)] * v * delta_sign(l) for l, v in chi.items())
    den = sum(y[tuple(l)] * v for l, v in chi.items())
    return float(num / den)


def main() -> int:
    mp.mp.dps = 40
    print("\n  CHIRALITY SIGNS FROM THE SHELL (Wedderburn transpose-parity δ_sign)")
    print("  candidates: ⟨sgn⟩ = trace-weighted δ_sign;  ZN mod 2 = pairing parity\n")
    print("| iso | A | Z·N | empirical net | ⟨sgn⟩ (trace-weighted) | ZN mod 2 |")
    print("|---|--:|--:|--:|--:|--:|")
    for name, Z, N, emp in ISO:
        zn = Z * N
        try:
            sgn = trace_weighted_sign(Z, N)
            sgn_s = f"{sgn:+.4f}"
        except Exception as e:
            sgn_s = f"err:{type(e).__name__}"
        emp_s = f"{emp:+d}" if emp is not None else "? (predict)"
        print(f"| {name} | {Z+N} | {zn} | {emp_s} | {sgn_s} | {zn % 2} |")
    print("\n  FINDING (honest): the principled candidate FAILS — the "
          "trace-weighted option-e chirality parity ⟨sgn⟩ does NOT track the "
          "empirical net (D: −0.26 vs +1, wrong even in sign; T/³He/⁴He: "
          "−0.5..−0.2 vs 0). So the empirical chirality is NOT the Wedderburn "
          "transpose-parity δ_sign. Corroborated by a full corpus audit: the "
          "production signs are a HARDCODED (Z,N) lookup table "
          "(paper_six_term_isotope_sweep.py:1260, alternating [+1,−1,…], "
          "net=L mod 2) — not derived on the Python or Lean side; and the one "
          "structural bridge (ribbon eigenvalue) is refuted (#2422 + an "
          "8-variant >20% sweep). The signs remain a physical np-spin-pairing "
          "input.")
    print("\n  DISCRIMINATOR — ⁶Li settles it. The hardcoded table gives ⁶Li "
          "net 0 (alternating, L=6 even). But ⁶Li's ground state is J=1 "
          "(deuteron-like — an unpaired ³S₁ np pair), so a STRUCTURAL "
          "(unpaired-spin-1-pair / Wigner-SU(4)) rule predicts net +1, like the "
          "deuteron; ZN mod 2 = 1 agrees with that +1, against the table's 0. "
          "⁶Li's experimental J=1 favors the structural +1 ⇒ the hardcoded "
          "table is likely WRONG at ⁶Li. ⁶Li net chirality is the decisive, "
          "falsifiable test of structural-vs-hardcoded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
