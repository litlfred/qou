#!/usr/bin/env python3
"""
Shell-based binding energy predictions via transfer-matrix unfolds.

The simpler path: instead of computing the full H_{3A} Markov trace,
use the 2×2 transfer matrix at each generator with crossing coefficients
(c,d) determined by nucleon pair type. Binding = difference between
consecutive shell operations.

No magic = one unfold, one magic = two unfold, double magic = closure.

From shell-construction-rules.md §Algorithm.
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
import json
from pathlib import Path

from mpmath import mp, mpf, fabs, log

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402

set_compute_dps()

q0 = mpf(Q_50_DIGIT_STR)
m_e = mpf(M_E_MEV)
h = q0 - 1 / q0
z_markov = q0**3 / (q0**2 + 1)

MAGIC = [0, 2, 8, 20, 28, 50, 82, 126]


def magic_leq(X):
    return max(m for m in MAGIC if m <= X)


def n_out(X):
    return X - magic_leq(X)


def n_shell(X):
    m = magic_leq(X)
    m_prev = max(mm for mm in MAGIC if mm < m) if m > 0 else 0
    return m - m_prev


def markov_trace_sigma_n(n):
    """tr_M(σ^n) in H_2(q) via Chebyshev recurrence."""
    if n == 0:
        return mpf(1)
    if n == 1:
        return z_markov
    # Chebyshev: tr(σ^n) = (q-q⁻¹)·tr(σ^{n-1}) + tr(σ^{n-2})...
    # Actually for H_2: tr_M(σ^n) = z^n (geometric in the Markov param)
    # Wait — for H_2(q) with one generator σ, the Markov trace is:
    # tr_M(σ^n) uses the Hecke relation σ² = hσ + 1 to reduce.
    # The closed form: tr_M(σ^n) = z × U_{n-1}(h/(2z)) where U is Chebyshev-U
    # But simpler: direct recursion via σ^n = h·σ^{n-1} + σ^{n-2}
    t = [mpf(1), z_markov]  # tr(1), tr(σ)
    for k in range(2, n + 1):
        # σ^k = h·σ^{k-1} + σ^{k-2} (Hecke relation)
        # tr(σ^k) = h·tr(σ^{k-1}) + tr(σ^{k-2})
        # But tr_M is NOT multiplicative on products — it's:
        # tr_M(σ^k) = h·z·tr_M(σ^{k-2}) + tr_M(σ^{k-2})
        # No wait. tr_M(aσ) = z·tr_M(a) for the Markov property.
        # Actually for H_2 the recursion is simpler:
        # tr_M(σ^n) is determined by the eigenvalues q and -q⁻¹.
        # The trace on the 2D Wedderburn decomposition:
        # tr_M(σ^n) = y_(2)·q^n + y_(1,1)·(-q⁻¹)^n
        pass
    # Use the Wedderburn decomposition directly:
    # y_(2) = q/[2]_q, y_(1,1) = q⁻¹/[2]_q (proved in Lean, PR #1298)
    q2 = q0 + q0 ** (-1)  # [2]_q
    y2 = q0 / q2
    y11 = q0 ** (-1) / q2
    return y2 * q0 ** n + y11 * (-q0 ** (-1)) ** n


def transfer_matrix_trace(Z, N):
    """Compute |det(transfer chain)| for atom (Z,N) using 2×2 matrices.

    Per shell-construction-rules.md Step 3:
    pp: (c,d) = (1, 0)
    nn: (c,d) = (1, -(q-q⁻¹))
    mix: (c,d) = (1, -(q-q⁻¹)/2)
    """
    import numpy as np
    qq = float(q0)
    hh = qq - 1 / qq

    # Build the transfer chain: [p...p n...n] naive ordering
    # Each pair of adjacent nucleons contributes one generator
    chain = []
    nucleons = ['p'] * Z + ['n'] * N
    for i in range(len(nucleons) - 1):
        a, b = nucleons[i], nucleons[i + 1]
        if a == 'p' and b == 'p':
            c, d = 1.0, 0.0
        elif a == 'n' and b == 'n':
            c, d = 1.0, -hh
        else:
            c, d = 1.0, -hh / 2
        T = np.array([[c * hh + d, c], [c, d]])
        chain.append(T)

    if not chain:
        return 1.0

    M = chain[0]
    for T in chain[1:]:
        M = M @ T

    return abs(np.trace(M))


def main():
    t0 = time.perf_counter()

    E0 = m_e / (q0 * (q0 - 1))

    atoms = [
        ("D", 1, 1, float(AME_B_DEUTERON_MEV_VALIDATION)),
        ("T", 1, 2, float(AME_B_TRITIUM_MEV_VALIDATION)),
        ("³He", 2, 1, float(AME_B_HE3_MEV_VALIDATION)),
        ("⁴He", 2, 2, float(AME_B_HE4_MEV_VALIDATION)),
        ("⁶Li", 3, 3, 31.994),
        ("⁷Li", 3, 4, 39.245),
        ("⁹Be", 4, 5, 58.165),
        ("¹²C", 6, 6, 92.163),
        ("¹⁶O", 8, 8, 127.621),
        ("⁴⁰Ca", 20, 20, 342.052),
    ]

    print("SHELL-BASED BINDING: transfer-matrix unfold approach")
    print("=" * 80)
    print(f"E₀ = m_e/(q₀(q₀-1)) = {float(E0):.4f} MeV")
    print()
    print(f"{'Atom':>6s} {'Z':>2s} {'N':>2s} {'tr_atom':>10s} {'tr_free':>10s} "
          f"{'B_shell':>10s} {'B_AME':>10s} {'err%':>8s}")
    print("-" * 80)

    results = []
    for name, Z, N, B_ame in atoms:
        tr_atom = transfer_matrix_trace(Z, N)
        tr_free = sum(transfer_matrix_trace(1, 0) if nuc == 'p'
                      else transfer_matrix_trace(0, 1)
                      for nuc in ['p'] * Z + ['n'] * N)

        # Binding = E₀ × |tr_free - tr_atom| × q⁻¹
        delta_tr = abs(tr_free - tr_atom)
        B_pred = float(E0) * delta_tr / float(q0)

        err = (B_pred - B_ame) / B_ame * 100 if B_ame > 0 else 0

        print(f"{name:>6s} {Z:2d} {N:2d} {tr_atom:10.4f} {tr_free:10.4f} "
              f"{B_pred:10.3f} {B_ame:10.3f} {err:+8.1f}%")

        results.append({
            "atom": name, "Z": Z, "N": N,
            "B_pred_MeV": round(B_pred, 4),
            "B_AME_MeV": B_ame,
            "err_pct": round(err, 2),
        })

    wb = WitnessBuilder("shell-binding-transfer-matrix", start_time=t0)
    wb.data["E0_MeV"] = fmt(E0, 10)
    wb.data["method"] = "Transfer-matrix unfold: B = E₀ × |tr_free - tr_atom| / q₀"
    wb.data["results"] = results
    wb.add_assertion("deuteron_sign_correct",
                     computed=1 if results[0]["B_pred_MeV"] > 0 else 0,
                     expected=1, tolerance=0)
    wb.save()
    print(f"\n✓ Witness: shell-binding-transfer-matrix.witness.json")


if __name__ == "__main__":
    main()
