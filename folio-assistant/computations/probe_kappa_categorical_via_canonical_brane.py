"""Categorical κ derivation via per-interface-type Vol_q^({i}).

Traces κ through the canonical mass-tower derivation (Markov-invariant
brane-tower form from prop:mass-endomorphism-tower §Algebraic form),
extracting the interface-type contribution PURELY from the categorical
braid-word structure with no empirical fit.

## Setup

Per `canonical_brane_tower_decomposition.py` theorem:

  Δ T_2 = bound − free = Σ_(i ∈ interface gens) z · Vol_q^({i})(β_atom)
  Δ T_3 = bound − free = z² · Σ_{(i, j) : i or j ∈ interface} Vol_q^({i, j})

The interface generators come in three types:
  - pp interface: between two protons (only present when Z ≥ 2)
  - pn interface: between proton and neutron (always present if Z, N ≥ 1)
  - nn interface: between two neutrons (only present when N ≥ 2)

Per `prop:magic-shell-coupling-witness`, the Δ_coupling has structure:

  Δ_coupling(Z, N) = (universal piece) + (n_pp − n_nn) · κ · h · E_0

where (n_pp − n_nn) is the pp-vs-nn imbalance and κ is the per-unit-
excess coupling slope. The empirical κ ≈ -1.07 MeV (#656 v6).

## Categorical κ derivation

Compute Vol_q^({i})(β_atom) for the per-interface-type i:
  V_pp := Vol_q^({pp interface i})(β_atom) for an atom with that interface
  V_nn := Vol_q^({nn interface i})(β_atom) for an atom with that interface
  V_pn := Vol_q^({pn interface i})(β_atom) for an atom with that interface

If the canonical braid word has p↔n mirror symmetry, then V_pp = -V_nn
(by writhe-sign flip), and κ extracts as:

  κ · h · E_0 = α · z · (V_pp − V_nn)  per unit interface excess
            = α · z · 2 V_pp           by mirror symmetry

This is the categorical derivation — NO empirical fit, purely from the
braid-word structure + the prop:mass-endomorphism-tower form.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from canonical_brane_tower import vol_q_S  # noqa: E402
from q_parameter import Q as Q_0_FLOAT, Q_MP, HA_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402


def interface_type(Z: int, N: int, gen: int) -> str | None:
    """Identify whether interface generator `gen` is pp, pn, or nn.

    Per canonical pppnnn ordering with A nucleons on strands {3k..3k+2}:
      interface k: gen = 3k+2 connects nucleon k to nucleon k+1.
    """
    A = Z + N
    if gen % 3 != 2 or gen >= 3 * (A - 1) + 2:
        return None  # not an interface gen
    k = gen // 3
    if k + 1 >= A:
        return None
    nucleon_k = 'p' if k < Z else 'n'
    nucleon_k_plus_1 = 'p' if (k + 1) < Z else 'n'
    pair = ''.join(sorted([nucleon_k, nucleon_k_plus_1]))
    if pair == 'pp':
        return 'pp'
    if pair == 'nn':
        return 'nn'
    return 'pn'


def vol_at_interface_type(atom_label: str, Z: int, N: int,
                            target_type: str, q_val: float) -> mp.mpf | None:
    """Compute Vol_q^({i})(β_atom) for the interface of given type.

    Returns the Vol for the first interface gen matching target_type,
    or None if no such interface exists in this atom.
    """
    A = Z + N
    word = atom_braid_word_3A(Z, N, include_inter=True)
    n_gens = 3 * A - 1
    for gen in range(n_gens):
        t = interface_type(Z, N, gen)
        if t == target_type:
            return vol_q_S(word, {gen}, n_gens, q_val)
    return None


def main() -> int:
    mp.mp.dps = 50

    q = Q_MP
    h = HA_MP
    m_e = mp.mpf(M_E_MEV)
    E0 = m_e / (q * (q - 1))
    z_mark = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    G_catalan = mp.mpf("0.91596559417721901505460351493238")  # Catalan G
    alpha = m_e * 8 * G_catalan  # binding-scale-catalan

    q_f = float(Q_0_FLOAT)
    KAPPA_EMP = mp.mpf("-1.0707907503265857")  # from #656 v6

    print("=" * 80)
    print("  κ categorical derivation via per-interface-type Vol_q^({i})")
    print("=" * 80)
    print()
    print(f"  q_0 = {mp.nstr(q, 12)}")
    print(f"  h   = {mp.nstr(h, 12)}")
    print(f"  z   = {mp.nstr(z_mark, 12)}")
    print(f"  E_0 = {mp.nstr(E0, 12)} MeV")
    print(f"  α   = m_e · 8G = {mp.nstr(alpha, 12)} MeV")
    print()
    print("  ── Per-atom per-interface-type Vol_q^({i})(β_atom) ──")
    print()
    print(f"  {'atom':>4} {'(Z, N)':>8} {'V_pp':>12} {'V_pn':>12} {'V_nn':>12}")
    print("  " + "-" * 60)

    rows = []
    for label, Z, N in [
        ("D",   1, 1),
        ("T",   1, 2),
        ("3He", 2, 1),
        ("4He", 2, 2),
    ]:
        v_pp = vol_at_interface_type(label, Z, N, 'pp', q_f)
        v_pn = vol_at_interface_type(label, Z, N, 'pn', q_f)
        v_nn = vol_at_interface_type(label, Z, N, 'nn', q_f)
        rows.append({
            "atom": label, "Z": Z, "N": N,
            "V_pp": float(v_pp) if v_pp is not None else None,
            "V_pn": float(v_pn) if v_pn is not None else None,
            "V_nn": float(v_nn) if v_nn is not None else None,
        })
        def fmt(x): return f"{float(x):>+12.6f}" if x is not None else f"{'—':>12}"
        print(f"  {label:>4} ({Z:>2},{N:>2}) {fmt(v_pp)} {fmt(v_pn)} {fmt(v_nn)}")

    # Extract V_pp and V_nn for any atom that has both type interfaces (⁴He)
    he4_row = [r for r in rows if r["atom"] == "4He"][0]
    V_pp = he4_row["V_pp"]
    V_nn = he4_row["V_nn"]

    print()
    print("  ── Mirror check (p↔n) in ⁴He ──")
    print()
    print(f"  V_pp(⁴He) = {V_pp:+.6f}")
    print(f"  V_nn(⁴He) = {V_nn:+.6f}")
    print(f"  V_pp + V_nn = {V_pp + V_nn:+.6e}   (should be 0 if mirror-symmetric)")
    print(f"  ratio V_nn / V_pp = {V_nn / V_pp:.6f}   (should be -1 if mirror-symmetric)")

    # ── Categorical κ via interface-type difference ──
    print()
    print("  ── Categorical κ derivation ──")
    print()
    # κ · h · E_0 per unit interface excess
    # = α · z · (V_pp − V_nn) for one (pp ↔ nn) swap
    delta_V = mp.mpf(repr(V_pp)) - mp.mpf(repr(V_nn))
    kappa_categorical = alpha * z_mark * delta_V / (h * E0)
    print(f"  Hypothesis: κ · h · E_0 = α · z · (V_pp − V_nn) per excess unit")
    print()
    print(f"  V_pp − V_nn        = {float(delta_V):+.6f}")
    print(f"  α · z · (V_pp−V_nn) = {float(alpha * z_mark * delta_V):+.6f}")
    print(f"  κ = α · z · (V_pp−V_nn) / (h · E_0)")
    print(f"    = {float(kappa_categorical):+.6f} MeV/excess")
    print()
    print(f"  vs empirical κ (#656 v6) = {float(KAPPA_EMP):+.6f} MeV/excess")
    print(f"  ratio = {float(kappa_categorical / KAPPA_EMP):.6f}")

    builder = (
        WitnessBuilder("kappa-categorical-via-canonical-brane", engine="mpmath")
        .set_description(
            "Categorical κ derivation by extracting per-interface-type "
            "Vol_q^({i})(β_atom) from the canonical Markov-invariant "
            "brane-tower form (prop:mass-endomorphism-tower §Algebraic). "
            "No empirical fit. Tests whether κ · h · E_0 = α · z · "
            "(V_pp − V_nn) per unit interface excess, with V_pp and V_nn "
            "the per-pp- and per-nn-interface generator's Vol_q^({i})."
        )
        .set_content_block("prop:magic-shell-coupling-witness")
        .add_parameter("q_0", mp.nstr(q, 50))
        .add_data("per_atom_vols", rows)
        .add_data("V_pp_4He", V_pp)
        .add_data("V_nn_4He", V_nn)
        .add_data("V_pp_plus_V_nn", V_pp + V_nn)
        .add_data("V_nn_over_V_pp_ratio", V_nn / V_pp)
        .add_data("kappa_categorical_MeV", float(kappa_categorical))
        .add_data("kappa_empirical_MeV", float(KAPPA_EMP))
        .add_data("ratio_to_empirical", float(kappa_categorical / KAPPA_EMP))
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
