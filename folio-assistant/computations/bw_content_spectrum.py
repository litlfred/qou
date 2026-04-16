"""
BW mass formula at Hecke level k=3..15 via Jucys-Murphy content spectrum.

The binding energy is:
  B(Z,N) = α × Σ_λ (w_λ/dim_λ) × Σ_{□∈λ} Φ_nuclear(q^{c(□)}, Z, N)

where:
  - λ runs over partitions of k
  - w_λ = dim_q(λ)² / [k]_q! (Wedderburn weight)
  - c(□) = column - row of cell □ (content)
  - Φ_nuclear is the nuclear potential evaluated at the JM eigenvalue
  - α = m_e × Vol(B₃) (binding scale)

The nuclear potential for a nucleus with Z protons, N neutrons:
  Φ(x, Z, N) = n_pp × ln|x| + n_nn × ln|x⁻¹| + n_pn × ln|½(x + x⁻¹)|
             = (n_pp - n_nn) × ln|x| + n_pn × ln|½(x + x⁻¹)|

where x = q^{c(□)}, n_pp = Z(Z-1)/2, n_nn = N(N-1)/2, n_pn = ZN.

This is the EXACT algebraic form: no physics identification needed.
The partition shape determines the content spectrum, which determines
the BW term. Zero fitted parameters.

Usage:
    python3 bw_content_spectrum.py

@module folio-assistant/computations/bw_content_spectrum
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
alpha_bind = M_E_MEV * 8 * CATALAN  # m_e × Vol(B₃)


def nuclear_potential(x, n_pp, n_nn, n_pn):
    """Nuclear potential at Jucys-Murphy eigenvalue x = q^{c(□)}.

    Φ(x) = n_pp × ln|x| + n_nn × ln|x⁻¹| + n_pn × ln|½(x + x⁻¹)|

    This encodes:
      pp crossings: positive eigenvalue x (EM repulsion → positive ln)
      nn crossings: inverse eigenvalue x⁻¹ (nuclear attraction → negative ln)
      pn crossings: mixed eigenvalue ½(x + x⁻¹) (symmetric nuclear)
    """
    if abs(x) < 1e-300:
        return 0.0

    result = 0.0

    # pp contribution: ln|x|
    if n_pp > 0:
        result += n_pp * math.log(abs(x))

    # nn contribution: ln|x⁻¹| = -ln|x|
    if n_nn > 0:
        result += n_nn * (-math.log(abs(x)))

    # pn contribution: ln|½(x + x⁻¹)| = ln|cosh(ln|x|)|
    if n_pn > 0:
        half_sum = 0.5 * (x + 1.0 / x)
        if abs(half_sum) > 1e-300:
            result += n_pn * math.log(abs(half_sum))

    return result


def content_spectrum(shape):
    """Return the content values c(□) for all cells of partition λ."""
    contents = []
    for row, width in enumerate(shape):
        for col in range(width):
            contents.append(col - row)
    return contents


def bw_binding_content(Z, N, k):
    """BW binding energy at Hecke level k from content spectrum.

    B = α × Σ_λ (w_λ/dim_λ) × Σ_{□∈λ} Φ(q^{c(□)}, Z, N)
    """
    witness = load_witness()
    level = witness['levels'].get(str(k), [])
    if not level:
        return 0.0

    n_pp = Z * (Z - 1) / 2.0
    n_nn = N * (N - 1) / 2.0
    n_pn = Z * N * 1.0

    B = 0.0
    for entry in level:
        shape = tuple(entry['shape'])
        w = entry['w']
        dim = entry['dim']

        if dim == 0:
            continue

        # Content spectrum of this partition
        contents = content_spectrum(shape)

        # Sum nuclear potential over all cells
        phi_sum = 0.0
        for c in contents:
            x = q0 ** c  # Jucys-Murphy eigenvalue
            phi_sum += nuclear_potential(x, n_pp, n_nn, n_pn)

        B += (w / dim) * phi_sum

    return B * alpha_bind


# ── AME2020 data ─────────────────────────────────────────────────

AME2020 = [
    (1, 0, 1, 0.0, "H"),
    (1, 1, 2, 1.1121, "D"),
    (2, 2, 4, 7.0739, "⁴He"),
    (3, 4, 7, 5.6063, "⁷Li"),
    (4, 5, 9, 6.4628, "⁹Be"),
    (5, 6, 11, 6.9277, "¹¹B"),
    (6, 6, 12, 7.6801, "¹²C"),
    (7, 7, 14, 7.4756, "¹⁴N"),
    (8, 8, 16, 7.9762, "¹⁶O"),
    (10, 10, 20, 8.0325, "²⁰Ne"),
    (14, 14, 28, 8.4477, "²⁸Si"),
    (20, 20, 40, 8.5513, "⁴⁰Ca"),
    (26, 30, 56, 8.7904, "⁵⁶Fe"),
    (50, 70, 120, 8.5050, "¹²⁰Sn"),
    (82, 126, 208, 7.8675, "²⁰⁸Pb"),
    (92, 146, 238, 7.5702, "U"),
]


if __name__ == "__main__":
    print("BW mass formula via Jucys-Murphy content spectrum")
    print(f"α = m_e × Vol(B₃) = {alpha_bind:.4f} MeV")
    print(f"q₀ = {q0:.10f}")
    print()

    # Compute at each level
    print(f"{'El':>4s} {'A':>4s} {'B_AME':>8s}", end="")
    for k in [3, 5, 7, 10, 13, 15]:
        print(f" {'k='+str(k):>9s}", end="")
    print()
    print("-" * 75)

    results = {}
    for Z, N, A, BperA, name in AME2020:
        B_ame = A * BperA
        print(f"{name:>4s} {A:>4d} {B_ame:>8.1f}", end="")

        for k in [3, 5, 7, 10, 13, 15]:
            t0 = time.monotonic()
            B = bw_binding_content(Z, N, k)
            elapsed = time.monotonic() - t0
            err = B - B_ame if B_ame > 0.01 else 0
            print(f" {B:>9.2f}", end="")
            results[(name, k)] = B

        print()

    # RMS by level
    print("-" * 75)
    for k in [3, 5, 7, 10, 13, 15]:
        sq = sum((results.get((n, k), 0) - A * BperA) ** 2
                 for Z, N, A, BperA, n in AME2020 if A * BperA > 0.01)
        n = sum(1 for _, _, _, b, _ in AME2020 if b > 0.01)
        rms = math.sqrt(sq / n)
        print(f"  RMS(k={k:>2d}) = {rms:.3f} MeV")

    # Save witness
    w = WitnessBuilder("bw-content-spectrum", engine="python")
    w.set_description(
        "BW mass formula at k=3..15 via Jucys-Murphy content spectrum. "
        "B = α × Σ_λ (w_λ/dim_λ) × Σ_{□∈λ} Φ(q^{c(□)}, Z, N). "
        "Zero fitted parameters. Pure algebra from partition shape."
    )
    w.add_parameter("alpha_bind_MeV", alpha_bind)
    w.add_parameter("q", q0)

    for k in [5, 10, 15]:
        data = {}
        for Z, N, A, BperA, name in AME2020:
            B = results.get((name, k), 0)
            B_ame = A * BperA
            data[name] = {"B_QOU": round(B, 4), "B_AME": round(B_ame, 4),
                          "delta": round(B - B_ame, 4) if B_ame > 0.01 else 0}
        w.add_data(f"k{k}", data)

    w.save()
