#!/usr/bin/env python3
"""
CONFINEMENT LEVEL STRAND COUNT — mathematical derivation.

For each confinement level ℓ, derive:
  - n_ℓ = number of strands required (the H_n algebra)
  - L_ℓ^before = word length of the primitive operator (# crossings)
  - L_ℓ^after = NF word length after Gröbner–Shirshov reduction
  - operator structure

Mathematical basis (per def:confinement-level, def:atom-knot,
def:hecke-normal-form):

  After NF reduction, every word in H_n(q) lies in a canonical
  basis {T_w : w ∈ S_n}, so the maximum NF length is
  ℓ_max(n) = (n-1)n/2 (longest element in S_n: w_0 has
  Coxeter length C(n, 2)).

  Before NF reduction, the primitive operator's word length
  depends on its construction:
    - σ alone:           length 1
    - Borromean B_3:     length 6  ((σ_1 σ_2)^3)
    - Hopf link:         length 2  (σ_1²)
    - Trefoil:           length 3  (σ_1³)

LEVEL HIERARCHY:

  ℓ=1  Meson (quark exchange)    H_2(q)
  ℓ=2  Nucleon (Borromean B_3)   H_3(q)
  ℓ=3  Pair (deuteron-like)      H_6(q)
  ℓ=4  Shell-magic               H_{3·A_magic}(q), A_magic ∈ {4, 8, 20, 28, ...}
  ℓ=5  Cross-shell               H_{3·A}(q), A non-magic
  ℓ=6  Atom (neutral, +electrons) H_{3(Z+N)+Z}(q)
  ℓ=7  Molecule (covalent)       H_{Σ atoms}(q)

References:
  * sec:atom-isotope-confinement
  * def:confinement-level (per-atom k_max)
  * def:hecke-normal-form (Gröbner-Shirshov NF)
"""
import sys
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import q0


def coxeter_length(n):
    """Longest word length in S_n (Coxeter length of w_0)."""
    return n * (n - 1) // 2


# Magic A values (closed nuclear shells)
MAGIC_A = [2, 8, 20, 28, 50, 82, 126]


def level_data():
    """Mathematical derivation of strand counts per confinement level."""
    levels = []

    # Level 1: meson (quark exchange σ_ud in H_2)
    levels.append({
        "level": 1, "name": "meson",
        "operator": "σ_ud (quark exchange)",
        "n_strands": 2,
        "L_before_NF": 1,            # σ alone
        "L_after_NF_max": coxeter_length(2),   # 1
        "wedderburn_partitions": ["(2)", "(1,1)"],
        "note": "1-dim sym + alt; no mixing block; trivial filtration",
    })

    # Level 2: nucleon Borromean B_3 in H_3
    levels.append({
        "level": 2, "name": "nucleon",
        "operator": "B_3 = (σ_1 σ_2)^3 (Borromean closure)",
        "n_strands": 3,
        "L_before_NF": 6,            # (σ_1 σ_2)^3
        "L_after_NF_max": coxeter_length(3),   # 3
        "wedderburn_partitions": ["(3)", "(2,1)", "(1,1,1)"],
        "note": "1+2+1 decomposition; (2,1) is the only mixing block",
    })

    # Level 3: pair coupling in H_6 (two 3-strand baryons + 1 connector)
    levels.append({
        "level": 3, "name": "pair",
        "operator": "B_3 ⊗ B_3 + σ_inter (deuteron-like)",
        "n_strands": 6,
        "L_before_NF": 6 + 6 + 1,    # two B_3 + one connector
        "L_after_NF_max": coxeter_length(6),   # 15
        "wedderburn_partitions": [
            "(6)", "(5,1)", "(4,2)", "(4,1,1)", "(3,3)",
            "(3,2,1)", "(3,1,1,1)", "(2,2,2)",
            "(2,2,1,1)", "(2,1,1,1,1)", "(1^6)",
        ],
        "note": "11 partitions of 6; (5,1) is standard analog of B_3's (2,1)",
    })

    # Level 4: shell-magic for each magic A
    for A in MAGIC_A[:4]:  # First 4 magic numbers (2, 8, 20, 28)
        n = 3 * A
        levels.append({
            "level": 4, "name": f"shell-magic-A={A}",
            "operator": f"shell-closure for {A}-nucleon shell",
            "n_strands": n,
            "L_before_NF": 6 * A + (A - 1),    # A nucleons + A-1 connectors
            "L_after_NF_max": coxeter_length(n),   # n(n-1)/2
            "wedderburn_partitions": f"all λ ⊢ {n}",
            "note": (f"Magic A={A}: n_strands = {n}, max NF length = "
                     f"{coxeter_length(n)}"),
        })

    # Level 5: cross-shell (non-magic, A between magic anchors)
    for A in [6, 16, 40]:  # representative non-magic / boundary
        n = 3 * A
        levels.append({
            "level": 5, "name": f"cross-shell-A={A}",
            "operator": f"shell-straddling for non-magic A={A}",
            "n_strands": n,
            "L_before_NF": 6 * A + (A - 1),
            "L_after_NF_max": coxeter_length(n),
            "wedderburn_partitions": f"all λ ⊢ {n}",
            "note": "Adds shell-straddling crossings between adjacent magic shells",
        })

    # Level 6: atom (nucleus + Z electrons) — for hydrogen, helium, carbon
    for atom, Z, N in [("H", 1, 0), ("He", 2, 2), ("C", 6, 6)]:
        n_nuc = 3 * (Z + N)
        n_atom = n_nuc + Z   # one strand per electron
        levels.append({
            "level": 6, "name": f"atom-{atom}",
            "operator": f"electron-shell coupling for Z={Z}",
            "n_strands": n_atom,
            "L_before_NF": 6 * (Z + N) + (Z + N - 1) + Z,
            "L_after_NF_max": coxeter_length(n_atom),
            "wedderburn_partitions": f"all λ ⊢ {n_atom}",
            "note": (f"Neutral {atom}: n_atom = {n_nuc} (nuclear) + {Z} "
                     f"(electron) = {n_atom}"),
        })

    # Level 7: molecule (multiple atoms) — H_2, H_2O
    # H_2: 2 hydrogen atoms = 2 × (3·1 + 1) = 8 strands
    n_H2 = 2 * (3 * 1 + 1)
    levels.append({
        "level": 7, "name": "molecule-H_2",
        "operator": "covalent bond between 2 hydrogen atoms",
        "n_strands": n_H2,
        "L_before_NF": 2 * (6 + 1) + 2,   # 2 atoms + 2 covalent crossings
        "L_after_NF_max": coxeter_length(n_H2),
        "wedderburn_partitions": f"all λ ⊢ {n_H2}",
        "note": "H_2: 2 H atoms (8 strands total); covalent bond = 1 e-pair",
    })

    # H_2O: 2 H + 1 O = 2·(3+1) + (3·16 + 8) = 8 + 56 = 64 strands
    n_H2O = 2 * (3 * 1 + 1) + (3 * 16 + 8)
    levels.append({
        "level": 7, "name": "molecule-H_2O",
        "operator": "2 covalent bonds (O-H × 2)",
        "n_strands": n_H2O,
        "L_before_NF": 2 * (6 + 1) + (6 * 16 + 15 + 8) + 4,
        "L_after_NF_max": coxeter_length(n_H2O),
        "wedderburn_partitions": f"all λ ⊢ {n_H2O}",
        "note": "H_2O: oxygen Z=8, 16O nucleus (48 strands) + 8 e + 2 H = 64",
    })

    return levels


if __name__ == "__main__":
    print("CONFINEMENT LEVEL STRAND COUNTS (mathematical derivation)")
    print("=" * 100)
    print(f"q₀ = {q0}")
    print(f"NF length bound: L_after^max = n(n-1)/2  (Coxeter length of "
          f"longest element in S_n)")
    print()
    print(f"  {'ℓ':>2} {'name':<22} {'n':>5} {'L_before':>10} "
          f"{'L_after^max':>12}  primitive operator")
    print("  " + "-" * 96)

    levels = level_data()
    for L in levels:
        print(f"  {L['level']:>2} {L['name']:<22} {L['n_strands']:>5d} "
              f"{L['L_before_NF']:>10d} {L['L_after_NF_max']:>12d}  "
              f"{L['operator']}")

    witness = {
        "computation": "confinement-level-strand-counts",
        "description": (
            "Mathematical derivation of strand count per confinement level. "
            "L_before = word length of primitive operator (# crossings). "
            "L_after^max = Coxeter length of S_n (longest NF word). "
            "Per def:confinement-level, def:hecke-normal-form."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q": q0, "magic_A_values": MAGIC_A},
        "level_data": levels,
        "math_notes": {
            "L_after_max_formula": "n(n-1)/2 (Coxeter length)",
            "atom_strand_formula": "3(Z+N) + Z (3 per nucleon + 1 per electron)",
            "magic_A": MAGIC_A,
        },
    }
    out = Path(__file__).parent / "confinement-level-strand-counts.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
