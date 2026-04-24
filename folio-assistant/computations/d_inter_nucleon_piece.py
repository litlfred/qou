#!/usr/bin/env python3
"""
D's inter-nucleon JSJ piece — Hecke-direct analysis (no braid-lift).

The user's observation: we don't need to resolve the ud-half crossings
to signed braid generators.  For Hecke-level observables (character,
Markov trace, Jones polynomial, Plancherel-weighted volume) the
element (T + T⁻¹)/2 is perfectly well-defined — compute directly.

atom_braid_word_3A(1, 1) has exactly 3 contiguous blocks:

    [0:11]  proton  (gens {0, 1}; 6 σ, 3 σ⁻¹, 2 ud-halves)
    [11:12] inter   (gen   2;        1 ud-half)
    [12:23] neutron (gens {3, 4};  5 σ, 4 σ⁻¹, 2 ud-halves)

We isolate the **inter-nucleon piece** as a single Hecke factor
at gen 2, and analyse it via characters + Jones polynomial.

Three decompositions are recorded:

    (A) β_D^full   = full atom Hecke element
    (B) β_D^free   = β_D^full with the inter factor removed (2 free nucleons)
    (C) β_D^inter  = difference element  (T_2 + T_2⁻¹)/2

Question: does the topological data of (C) alone explain D's
+1.09% residual?  Or does the split of volume into (B) + (C) give a
cleaner JSJ picture?

Uses the chi-sym-alt-theorem closed forms (no matrix machinery).

Output: d-inter-nucleon-piece.witness.json
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import math
import snappy

from hecke_core import h as H_A_VAL
from mass_at_3A_proper import atom_braid_word_3A
from experimental_constants import M_E_MEV
from q_parameter import Q as Q0
from witness_base import WitnessBuilder

B_AME_D = 2.22456612


def count_types(word):
    c = {"pure_sigma": 0, "pure_sigma_inv": 0, "ud": 0}
    for cc, dd, _g in word:
        if abs(cc - 1.0) > 1e-9:
            continue
        if abs(dd) < 1e-9:
            c["pure_sigma"] += 1
        elif abs(dd + H_A_VAL) < 1e-6:
            c["pure_sigma_inv"] += 1
        elif abs(dd + H_A_VAL / 2) < 1e-6:
            c["ud"] += 1
    return c


def chi_sym_closed(n_s, n_si, n_ud, q):
    two_q = q + 1.0 / q
    return (q ** (n_s - n_si)) * (two_q / 2.0) ** n_ud


def chi_alt_closed(n_s, n_si, n_ud, q):
    two_q = q + 1.0 / q
    sign = -1.0 if (n_s + n_si + n_ud) % 2 else 1.0
    return sign * (q ** (n_si - n_s)) * (two_q / 2.0) ** n_ud


def closure_volume(word_as_ints, max_len: int | None = None):
    """Close a signed-braid word with SnapPy; return (vol, comps, hyp)."""
    if not word_as_ints:
        return None, None, False
    try:
        L = snappy.Link(braid_closure=word_as_ints)
        try:
            vol = float(L.exterior().volume())
            hyp = vol > 1e-4
        except Exception:
            vol = None
            hyp = False
        try:
            comps = int(L.number_of_components())
        except Exception:
            comps = None
        return vol, comps, hyp
    except Exception:
        return None, None, False


def word_to_signed_all_plus_ud(triples):
    """Deterministic lift: σ for σ, σ⁻¹ for σ⁻¹, σ for ud-half (arbitrary)."""
    out = []
    for c, d, g in triples:
        if abs(d) < 1e-9:
            out.append(+(g + 1))
        elif abs(d + H_A_VAL) < 1e-6:
            out.append(-(g + 1))
        elif abs(d + H_A_VAL / 2) < 1e-6:
            out.append(+(g + 1))  # placeholder choice
    return out


def analyse_block(name: str, triples, q: float, w):
    counts = count_types(triples)
    n_s = counts["pure_sigma"]
    n_si = counts["pure_sigma_inv"]
    n_ud = counts["ud"]
    chi_sym = chi_sym_closed(n_s, n_si, n_ud, q)
    chi_alt = chi_alt_closed(n_s, n_si, n_ud, q)

    # Hecke-level Plancherel-weighted log volume contribution
    # For a 1-dim irrep: log|χ_λ| per block.
    log_chi_sym = math.log(abs(chi_sym)) if chi_sym != 0 else float("-inf")
    log_chi_alt = math.log(abs(chi_alt)) if chi_alt != 0 else float("-inf")

    # Placeholder braid lift (arbitrary sign for ud; only for SnapPy, not
    # for Hecke derivations).
    signed = word_to_signed_all_plus_ud(triples)
    vol, comps, hyp = closure_volume(signed)

    print(f"--- block: {name} ({len(triples)} factors) ---")
    print(f"  counts: σ={n_s}, σ⁻¹={n_si}, ud={n_ud}")
    print(f"  χ_sym (closed)     = {chi_sym:+.6f}")
    print(f"  χ_alt (closed)     = {chi_alt:+.6f}")
    print(f"  log|χ_sym|         = {log_chi_sym:+.6f}")
    print(f"  log|χ_alt|         = {log_chi_alt:+.6f}")
    print(f"  closure (lift+ud)  : "
          f"Vol={vol:.6f} comps={comps} hyp={hyp}" if vol is not None
          else "  closure: non-hyperbolic or error")
    print()

    return {
        "name": name,
        "n_factors": len(triples),
        "counts": counts,
        "chi_sym": chi_sym,
        "chi_alt": chi_alt,
        "log_chi_sym": log_chi_sym,
        "log_chi_alt": log_chi_alt,
        "signed_braid_word_placeholder": signed,
        "closure_volume": vol,
        "closure_components": comps,
        "closure_is_hyperbolic": bool(hyp),
    }


def main():
    w = WitnessBuilder("d-inter-nucleon-piece", engine="closed-form+snappy")
    w.set_description(
        "Decompose D's atom braid word into proton / inter / neutron "
        "sub-blocks.  Compute Hecke-level Plancherel character data "
        "(no braid lift needed) and, for reference, SnapPy closures "
        "of each sub-block with an arbitrary ud-half sign convention."
    )
    w.add_parameter("q_0", float(Q0))
    w.add_parameter("H_A", float(H_A_VAL))
    w.add_parameter("B_AME_D", B_AME_D)
    w.add_parameter("target_rho_me_Vol", B_AME_D / M_E_MEV)

    word_full = atom_braid_word_3A(1, 1, include_inter=True)
    word_free = atom_braid_word_3A(1, 1, include_inter=False)

    # Position 11 is the inter-nucleon factor
    proton = word_full[:11]
    inter = word_full[11:12]
    neutron = word_full[12:]

    print("=" * 70)
    print("D's inter-nucleon piece — Hecke-direct analysis")
    print("=" * 70)
    print(f"  Full atom word: {len(word_full)} factors")
    print(f"  Free-nucleon word (intra only): {len(word_free)} factors")
    print()

    # Analyse the three sub-blocks independently
    proton_row = analyse_block("PROTON", proton, float(Q0), w)
    inter_row = analyse_block("INTER", inter, float(Q0), w)
    neutron_row = analyse_block("NEUTRON", neutron, float(Q0), w)

    # Full atom for completeness
    full_row = analyse_block("FULL ATOM", word_full, float(Q0), w)

    # Hecke-level additivity check: character multiplicativity
    # χ_sym(full) = χ_sym(proton) · χ_sym(inter) · χ_sym(neutron)  (if 1-dim)
    chi_sym_prod = (proton_row["chi_sym"] * inter_row["chi_sym"]
                     * neutron_row["chi_sym"])
    chi_alt_prod = (proton_row["chi_alt"] * inter_row["chi_alt"]
                     * neutron_row["chi_alt"])

    print(f"--- Multiplicativity check (1-dim irreps) ---")
    print(f"  Π χ_sym(blocks) = {chi_sym_prod:+.6f}")
    print(f"  χ_sym(full)     = {full_row['chi_sym']:+.6f}")
    print(f"  ratio            = {chi_sym_prod / full_row['chi_sym']:.6f}")
    print()
    print(f"  Π χ_alt(blocks) = {chi_alt_prod:+.6f}")
    print(f"  χ_alt(full)     = {full_row['chi_alt']:+.6f}")
    print(f"  ratio            = {chi_alt_prod / full_row['chi_alt']:.6f}")

    # Kashaev-volume contributions (in inter block)
    target_me = B_AME_D / M_E_MEV  # 4.3534
    target_2me = B_AME_D / (2 * M_E_MEV)  # 2.1767

    inter_vol = inter_row["closure_volume"]
    if inter_vol is not None and inter_row["closure_is_hyperbolic"]:
        err_me = (inter_vol - target_me) / target_me * 100
        err_2me = (inter_vol - target_2me) / target_2me * 100
        print()
        print(f"--- Inter-only closure as D's JSJ piece ---")
        print(f"  Vol(inter closure)   = {inter_vol:.6f}")
        print(f"  err vs target(m_e)   = {err_me:+.3f}%")
        print(f"  err vs target(2m_e)  = {err_2me:+.3f}%")
    else:
        print()
        print("--- Inter-only closure is non-hyperbolic ---")
        print("  (expected: single generator closure = Hopf-or-unlink)")

    # Additive volume (Thurston): if atom link JSJ decomposes into
    #   proton-piece + inter-piece + neutron-piece,
    # then Vol(atom) = Vol(proton) + Vol(inter) + Vol(neutron).
    atom_vol = full_row["closure_volume"] or 0
    proton_vol = proton_row["closure_volume"] or 0
    neutron_vol = neutron_row["closure_volume"] or 0
    hypothetical_inter_vol = atom_vol - proton_vol - neutron_vol
    print()
    print("--- Thurston-additive volume accounting ---")
    print(f"  Vol(full atom closure)   = {atom_vol:.6f}")
    print(f"  Vol(proton closure)      = {proton_vol:.6f}")
    print(f"  Vol(neutron closure)     = {neutron_vol:.6f}")
    print(f"  Vol(inter) if additive   = "
           f"{hypothetical_inter_vol:.6f}")
    print(f"  target (ρ=m_e):          = {target_me:.6f}")
    if atom_vol and abs(hypothetical_inter_vol) > 1e-4:
        err = (hypothetical_inter_vol - target_me) / target_me * 100
        print(f"  err vs target(m_e)       = {err:+.3f}%")

    w.add_data("blocks", [proton_row, inter_row, neutron_row, full_row])
    w.add_data("multiplicativity", {
        "chi_sym_product_of_blocks": chi_sym_prod,
        "chi_sym_full_atom": full_row["chi_sym"],
        "chi_alt_product_of_blocks": chi_alt_prod,
        "chi_alt_full_atom": full_row["chi_alt"],
    })
    w.add_data("thurston_additive_accounting", {
        "full_atom_vol": atom_vol,
        "proton_vol": proton_vol,
        "neutron_vol": neutron_vol,
        "derived_inter_vol": hypothetical_inter_vol,
        "target_rho_me": target_me,
    })
    w.save()


if __name__ == "__main__":
    main()
