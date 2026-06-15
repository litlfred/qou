"""
Hoefsmit witness engine: load pre-computed character tables and
use them for iterative BW corrections at k >= 6.

The witness file (hoefsmit_witness.json) contains for each partition
λ ⊢ k (k = 3..11):
  - dim, dim_q, Wedderburn-Artin weight w_λ
  - χ(4₁, λ) = figure-eight character
  - χ(B₃, λ) = Borromean character
  - ratio = χ(4₁)/χ(B₃)
  - Frobenius decomposition: a_λ + b_λ × h²

The BW formula at level k uses these to compute exact corrections
without re-running the seminormal matrix construction.

Usage:
    from hoefsmit_witness import load_witness, bw_correction_at_level
    witness = load_witness()
    delta_B = bw_correction_at_level(Z, N, k=7, witness=witness)
"""

import json
import math
from pathlib import Path

_WITNESS_PATH = Path(__file__).parent / "hoefsmit_witness.json"
_CACHE = {}


def load_witness(path=None):
    """Load the Hoefsmit witness JSON. Cached after first load."""
    if 'data' in _CACHE:
        return _CACHE['data']
    p = Path(path) if path else _WITNESS_PATH
    with open(p) as f:
        data = json.load(f)
    _CACHE['data'] = data
    return data


def level_summary(k, witness=None):
    """Print summary of witness data at level k."""
    if witness is None:
        witness = load_witness()
    level = witness['levels'].get(str(k))
    if not level:
        raise ValueError(f"No witness data for k={k}")
    print(f"Level k={k}: {len(level)} partitions")
    for e in level:
        s = str(tuple(e['shape']))
        print(f"  {s:>20} dim={e['dim']:>4} w={e['w']:.6f} "
              f"chi_fig8={e['chi_fig8']:+.6f} a={e['a']:>3} b={e['b']:>3} "
              f"ratio={e['ratio']:.4f}")


def character_ratio(k, shape_tuple, witness=None):
    """Get χ(4₁,λ)/χ(B₃,λ) for partition λ at level k."""
    if witness is None:
        witness = load_witness()
    level = witness['levels'].get(str(k), [])
    for e in level:
        if tuple(e['shape']) == shape_tuple:
            return e['ratio']
    return None


def weighted_character_sum(k, witness=None, braid='fig8'):
    """Compute the Markov trace Σ w_λ χ(braid,λ)/dim(λ) at level k."""
    if witness is None:
        witness = load_witness()
    level = witness['levels'].get(str(k), [])
    total = 0.0
    for e in level:
        chi = e['chi_fig8'] if braid == 'fig8' else e['chi_borr']
        total += e['w'] * chi / e['dim']
    return total


def bw_correction_at_level(Z, N, k, witness=None):
    """Compute the BW correction from level k using witness data.

    At each level k >= 4, the correction from the new partitions
    (those not present at k-1) contributes additional binding terms.

    For Borromean nuclei (A >= 4): uses the Borromean character.
    For figure-eight nuclei (A = 3): uses the figure-eight character.

    Returns: delta_B (MeV) — the correction to add to the k-1 binding.
    """
    if witness is None:
        witness = load_witness()

    A = Z + N
    is_fig8 = (A == 3)
    level = witness['levels'].get(str(k), [])
    if not level:
        return 0.0

    # The correction at level k is the difference between the
    # Markov trace at level k and level k-1.
    # delta_tr = tr_M(k) - tr_M(k-1)
    # This requires computing both, which we have from the witness.
    tr_k = 0.0
    for e in level:
        chi = e['chi_fig8'] if is_fig8 else e['chi_borr']
        tr_k += e['w'] * chi / e['dim']

    prev_level = witness['levels'].get(str(k - 1), [])
    tr_km1 = 0.0
    for e in prev_level:
        chi = e['chi_fig8'] if is_fig8 else e['chi_borr']
        tr_km1 += e['w'] * chi / e['dim']

    delta_tr = tr_k - tr_km1

    # The correction to binding is proportional to the trace change
    # weighted by the binding scale and nuclear parameters
    from q_parameter import q_int
    from experimental_constants import M_E_MEV

    CATALAN_G = 0.915965594177219015054603514932
    alpha = M_E_MEV * 8 * CATALAN_G  # Borromean binding scale

    # Scale by A (the correction grows with nucleus size)
    return alpha * delta_tr * A


if __name__ == "__main__":
    witness = load_witness()
    print(f"Hoefsmit witness: levels {list(witness['levels'].keys())}")
    print(f"q = {witness['substrate']['q']}")
    print(f"h² = {witness['substrate']['h_squared']}")
    print()

    for k in range(3, 12):
        tr_borr = weighted_character_sum(k, witness, 'borr')
        tr_fig8 = weighted_character_sum(k, witness, 'fig8')
        n = len(witness['levels'][str(k)])
        print(f"k={k:>2}: {n:>3} parts  "
              f"tr_M(B₃)={tr_borr:+.8f}  tr_M(4₁)={tr_fig8:+.8f}")
