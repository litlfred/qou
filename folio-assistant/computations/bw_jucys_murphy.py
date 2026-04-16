"""
BW mass formula via Jucys-Murphy central element expansion.

The nuclear operator decomposes into central elements of H_k(q),
which are power sum symmetric functions in the Jucys-Murphy elements
J_i = Σ_{j<i} (j,i). Each central element gives one BW term.

The Jucys-Murphy eigenvalue on cell □ with content c = col - row is:
  J_i |□⟩ = q^{c(□)} |□⟩

The BW binding decomposes as:
  B = Σ_{n=0}^{k-1} a_n × e_n(λ)

where e_n(λ) = Σ_{□∈λ} q^{n·c(□)} is the n-th content power of λ,
and a_n depends on (Z, N, A) through the nuclear crossing counts.

The coefficients a_n are determined by the nuclear potential:
  Φ(x) = n_pp × x + n_nn × x⁻¹ + n_pn × ½(x + x⁻¹)

evaluated as a power series in x = q^c:
  Φ(q^c) = Σ_n a_n(Z,N) × q^{nc}

The per-partition BW contribution:
  B_λ = w_λ × Σ_n a_n × e_n(λ) / dim(λ)

Summing over all partitions at level k:
  B(k) = α × Σ_λ w_λ/dim × Σ_n a_n × e_n(λ)

The key: e_n(λ) is a KNOWN algebraic invariant of the partition.
No physics identification needed — pure algebra.

Usage:
    python3 bw_jucys_murphy.py
"""

import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi, HA as h, q_int
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from hoefsmit_witness import load_witness
from witness_base import WitnessBuilder

CATALAN = 0.915965594177219015054603514932
alpha_bind = M_E_MEV * 8 * CATALAN


def content_power(shape, n):
    """e_n(λ) = Σ_{□∈λ} q^{n·c(□)} where c = col - row."""
    total = 0.0
    for r, width in enumerate(shape):
        for col in range(width):
            c = col - r
            total += q0 ** (n * c)
    return total


def nuclear_coefficients(Z, N, n_max):
    """Compute the power series coefficients a_n(Z,N).

    The nuclear potential expanded in powers of q^c:
      Φ(q^c) = n_pp × q^c + n_nn × q^{-c} + n_pn × ½(q^c + q^{-c})

    For the BW: the binding involves the LOGARITHM of the trace:
      ln|tr| = ln|Σ_□ Π_{crossings} eigenvalue(c(□))|

    The per-crossing contributions in the q^c expansion:
      pp: q^c = Σ_n (c·ln q)^n / n!    [Taylor of q^c]
      nn: q^{-c} = Σ_n (-c·ln q)^n / n!
      pn: ½(q^c + q^{-c}) = Σ_n even powers only

    The n-th order nuclear coefficient:
      a_0 = n_pp + n_nn + n_pn (total crossings = A(A-1)/2)
      a_1 = (n_pp - n_nn) × ln(q)  (chirality × coupling)
      a_2 = (n_pp + n_nn + n_pn) × (ln q)²/2  (second order)
      a_n = nuclear_n × (ln q)^n / n!
    """
    n_pp = Z * (Z - 1) / 2.0
    n_nn = N * (N - 1) / 2.0
    n_pn = float(Z * N)
    ln_q = math.log(q0)

    coeffs = []
    for n in range(n_max + 1):
        if n == 0:
            # Zeroth order: total crossings (doesn't contribute to binding)
            a = n_pp + n_nn + n_pn
        elif n % 2 == 1:
            # Odd orders: (n_pp - n_nn) × (ln q)^n / n! (chirality)
            a = (n_pp - n_nn) * ln_q**n / math.factorial(n)
        else:
            # Even orders: (n_pp + n_nn + n_pn) × (ln q)^n / n!
            a = (n_pp + n_nn + n_pn) * ln_q**n / math.factorial(n)
        coeffs.append(a)

    return coeffs


def bw_jm(Z, N, k, n_terms=None):
    """BW binding at level k via Jucys-Murphy expansion.

    B = α × Σ_λ w_λ/dim × Σ_n a_n × e_n(λ)

    n_terms: number of power series terms (default: k-1)
    """
    witness = load_witness()
    level = witness['levels'].get(str(k), [])
    if not level:
        return 0.0

    if n_terms is None:
        n_terms = k

    # Nuclear coefficients
    a = nuclear_coefficients(Z, N, n_terms)

    B = 0.0
    for entry in level:
        shape = tuple(entry['shape'])
        w = entry['w']
        dim = entry['dim']
        if dim == 0:
            continue

        # Content powers e_n(λ)
        partition_contribution = 0.0
        for n in range(min(n_terms + 1, len(a))):
            if n == 0:
                continue  # Skip zeroth order (constant, doesn't bind)
            en = content_power(shape, n)
            partition_contribution += a[n] * en

        B += (w / dim) * partition_contribution

    return B * alpha_bind


# ══════════════════════════════════════════════════════════════

AME = [
    (1, 0, 1, 0.0, "H"), (1, 1, 2, 1.1121, "D"),
    (2, 2, 4, 7.0739, "⁴He"), (3, 4, 7, 5.6063, "⁷Li"),
    (6, 6, 12, 7.6801, "¹²C"), (7, 7, 14, 7.4756, "¹⁴N"),
    (8, 8, 16, 7.9762, "¹⁶O"), (14, 14, 28, 8.4477, "²⁸Si"),
    (20, 20, 40, 8.5513, "⁴⁰Ca"), (26, 30, 56, 8.7904, "⁵⁶Fe"),
    (50, 70, 120, 8.5050, "¹²⁰Sn"), (82, 126, 208, 7.8675, "²⁰⁸Pb"),
]

if __name__ == "__main__":
    print("BW via Jucys-Murphy central element expansion")
    print(f"α = {alpha_bind:.4f} MeV, q = {q0:.10f}, ln(q) = {math.log(q0):.6f}")
    print()

    # Show nuclear coefficients for ¹²C
    a = nuclear_coefficients(6, 6, 10)
    print("Nuclear coefficients a_n for ¹²C (Z=6, N=6):")
    for n in range(min(8, len(a))):
        print(f"  a_{n} = {a[n]:+.6f}")
    print()

    # Compute at each level
    print(f"{'El':>6s} {'B_AME':>8s}", end="")
    for k in [3, 5, 7, 10, 13, 15]:
        print(f" {'k='+str(k):>9s}", end="")
    print()
    print("-" * 70)

    t0 = time.monotonic()
    for Z, N, A, BperA, name in AME:
        B_ame = A * BperA
        print(f"{name:>6s} {B_ame:>8.1f}", end="")
        for k in [3, 5, 7, 10, 13, 15]:
            B = bw_jm(Z, N, k)
            print(f" {B:>9.2f}", end="")
        print()

    elapsed = time.monotonic() - t0
    print("-" * 70)
    print(f"Time: {elapsed:.1f}s")

    # RMS
    print()
    for k in [3, 5, 7, 10, 13, 15]:
        sq = sum((bw_jm(Z,N,k) - A*BperA)**2
                 for Z,N,A,BperA,_ in AME if A*BperA > 0.01)
        n = sum(1 for _,_,_,b,_ in AME if b > 0.01)
        rms = math.sqrt(sq / n)
        print(f"  RMS(k={k:>2d}) = {rms:.3f} MeV")

    # Save witness
    w = WitnessBuilder("bw-jucys-murphy", engine="python")
    w.set_description(
        "BW mass formula via Jucys-Murphy central element expansion. "
        "B = α × Σ_λ (w_λ/dim) × Σ_n a_n × e_n(λ). "
        "Pure algebra from partition content powers. Zero parameters."
    )
    w.add_parameter("alpha_MeV", alpha_bind)
    w.add_parameter("q", q0)
    for k in [5, 10, 15]:
        data = {n: round(bw_jm(Z,N,k), 4) for Z,N,_,_,n in AME}
        w.add_data(f"k{k}", data)
    w.save()
