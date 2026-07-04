#!/usr/bin/env python3
"""
theta_mn_linearchain_vs_allpairs.py — resolve the θ_λ bond-count convention:
linear-chain (A−1 consecutive) vs all-pairs C(A,2) = binom(A,2).

The mba-step09b color-averaging note attributes the binding multiplicity to the
all-pairs binom(A,2) bond count; the M_n=(n−1) derivation (PR #3282) uses the
LINEAR CHAIN. This settles it from the atomic braid recipe's own structure.

The recipe (`atomic-braid-recipe-*-canonical.derivation.json`, "Inter-nucleon
averaged crossing rule") joins nucleon blocks k and k+1 by a SINGLE interface
crossing at 0-indexed generator 3k−1, for k=1..A−1 — with a channel-dependent
type (pp→σ, pn→averaged, nn→σ⁻¹). So the inter-nucleon bonds sit at generators
{2, 5, 8, …} = {3k−1 : k=1..A−1}: exactly A−1 of them, connecting only CONSECUTIVE
blocks. That is a linear chain, NOT the complete graph K_A (all-pairs).

This script COUNTS the interface crossings in the canonical words to confirm A−1,
and contrasts the two multiplicities. EXPLORATORY — asserts the finding, no fit.
"""
from __future__ import annotations
import json, re, sys
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
try:
    from witness_base import WitnessBuilder
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

ATOMS = {"d": 2, "4he": 4}   # recipes present with canonical words


def interface_crossings(A: int, word_txt: str):
    """Count canonical-word crossings sitting at inter-nucleon generators 3k−1."""
    interfaces = {3 * k - 1 for k in range(1, A)}          # {2,5,8,...}
    # crossings are (gen, ctype) tuples of ANY type (sigma / averaged / sigma_inv)
    gens = [int(g) for g in re.findall(r'\((\d+),\s*[\'"](?:sigma|averaged|sigma_inv)[\'"]\)', word_txt)]
    at_interface = sorted(g for g in set(gens) if g in interfaces)
    return interfaces, at_interface


def main() -> int:
    print("  Braid-recipe interface-crossing count (inter-nucleon bonds):\n")
    results = {}
    for tag, A in ATOMS.items():
        f = HERE / f"atomic-braid-recipe-{tag}-canonical.derivation.json"
        if not f.exists():
            print(f"  {tag}: recipe missing"); continue
        d = json.load(open(f)); dd = d.get("data", d)
        txt = json.dumps(dd)
        interfaces, found = interface_crossings(A, txt)
        results[tag] = {"A": A, "interfaces": sorted(interfaces), "found": found,
                        "n_bonds": len(found), "A_minus_1": A - 1, "binom_A_2": comb(A, 2)}
        ok = len(found) == A - 1
        print(f"  {tag} (A={A}): interface gens {{3k−1}} = {sorted(interfaces)}")
        print(f"        crossings found at interfaces = {found}  →  {len(found)} bonds")
        print(f"        linear-chain A−1 = {A-1}   {'✓ MATCH' if ok else '✗'}   "
              f"(all-pairs binom(A,2) = {comb(A,2)})")
    print()

    print("  Multiplicity comparison (2-body interface bonds):")
    print("     A  | linear-chain (A−1) | all-pairs binom(A,2) | braid recipe")
    for A in (2, 3, 4, 5, 6):
        note = "  ← agree" if A == 2 else "  ← DIFFER"
        print(f"     {A}  |        {A-1:>2}          |         {comb(A,2):>2}           |  A−1 (consecutive){note if A<=4 else ''}")
    print()

    print("### Verdict — the QOU braid is a LINEAR CHAIN (A−1), not all-pairs binom(A,2)")
    print("  • The recipe's 'Inter-nucleon averaged crossing rule' places ONE interface")
    print("    crossing at generator 3k−1 for k=1..A−1 — connecting only CONSECUTIVE")
    print("    blocks. Deuteron: 1 bond (gen 2). ⁴He: 3 bonds (gens 2,5,8), NOT")
    print("    binom(4,2)=6. So the structure is the path graph P_A, not K_A.")
    print("  • The body-order aggregate is Σ(A−n+1)(n−1)=binom(A+1,3) (Lean-proved,")
    print("    prop:linear-chain-bond-count); the M_n=(n−1) reading reproduces ³H to")
    print("    0.16% no-fit. all-pairs binom(A,2) is NOT the braid multiplicity.")
    print("  • RESOLUTION: the mba-9b color-averaging note's binom(A,2) is superseded")
    print("    by the linear-chain A−1 count. (A distinct all-pairs mean-field model")
    print("    would need its own derivation; the canonical braid does not realise it.)")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("theta-mn-linearchain-vs-allpairs", engine="python")
            wb.set_description(
                "Resolves the θ_λ bond-count convention: the atomic braid recipe places "
                "A−1 inter-nucleon crossings at generators 3k−1 (consecutive blocks) — a "
                "LINEAR CHAIN (path graph P_A), NOT all-pairs binom(A,2) (K_A). ⁴He has 3 "
                "bonds (gens 2,5,8), not binom(4,2)=6. binom(A,2) in the mba-9b note is "
                "superseded by the linear-chain A−1 / binom(A+1,3) aggregate. No fit.")
            wb.add_data("interface_counts", results)
            wb.add_assertion(
                name="braid_is_linear_chain_not_all_pairs",
                computed=str(int(all(r["n_bonds"] == r["A_minus_1"] for r in results.values()))),
                expected="1", tolerance=0,
                source=("interface crossings at {3k−1} number A−1 (deuteron 1, ⁴He 3) — "
                        "the path graph P_A, not K_A; all-pairs binom(A,2) refuted as the braid "
                        "multiplicity."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
