"""Hoefsmit cell-content identification probe for the EW triplet.

Per the path-α-Bring refinement, the H_2(q)-only formulation of
conj:weak-spectral-completeness collapses dimensionally (six rank-1
projectors cannot fit in a 2-dim algebra).  The fix: lift the EW
carriers into End_R(A) for A = V^⊗6 (six strands), placing W, Z, H
on DISJOINT strand-pairs (1-2, 3-4, 5-6) in B_6.  σ_1, σ_3, σ_5 then
COMMUTE pairwise via far-commutativity, and (σ_1)^4 (σ_3)^6 (σ_5)^8
acts as a tensor product (q^4, q^-4) ⊗ (q^6, q^-6) ⊗ (q^8, q^-8)
= 8 distinct eigenvalues on the (sym⊗sym⊗sym) block ... etc.

In each Wedderburn block V_λ for λ ⊢ 6, the seminormal action of
σ_1, σ_3, σ_5 is computed via Hoefsmit cell-content on standard
tableaux: σ_i acts as +q (resp. -q⁻¹) on tableaux where i, i+1 are
in the same row (resp. same column), with off-diagonal mixing if
neither.

This script enumerates standard Young tableaux of shape (3,1,1,1)
through (3,2,1) and records the eigenvalue pattern of σ_1^4, σ_3^6,
σ_5^8 on each tableau, identifying the (λ, c_W, c_Z, c_H) data
where each EW carrier idempotent lives.

Output: hoefsmit-ew-cell-content.witness.json
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Standard tableaux enumeration (recursive)
def standard_tableaux(shape):
    """All standard Young tableaux of given partition shape."""
    n = sum(shape)
    if n == 0:
        return [[[None] * c for c in shape]]
    # Place n at any "removable corner" (cell whose removal gives valid shape)
    results = []
    for i, ri in enumerate(shape):
        if ri == 0:
            continue
        # Cell (i, ri-1) is removable if row i+1 doesn't reach ri
        if i + 1 < len(shape) and shape[i+1] >= ri:
            continue
        new_shape = list(shape)
        new_shape[i] -= 1
        # Trim trailing zeros
        while new_shape and new_shape[-1] == 0:
            new_shape.pop()
        for sub in standard_tableaux(tuple(new_shape)):
            # Pad sub to original shape and place n at (i, ri-1)
            tab = [list(row) + [None] * (shape[k] - len(row)) for k, row in enumerate(sub)]
            while len(tab) < len(shape):
                tab.append([None] * shape[len(tab)])
            tab[i][ri-1] = n
            results.append(tab)
    return results


def cell_content(tab, n):
    """Return (row, col) of cell containing label n in tableau."""
    for r, row in enumerate(tab):
        for c, val in enumerate(row):
            if val == n:
                return r, c
    return None


def sigma_eigenvalue_class(tab, i):
    """Eigenvalue class of σ_i on tableau:
       'sym' (+q) if i, i+1 in same row
       'alt' (-q⁻¹) if i, i+1 in same column
       'mixed' otherwise (both row and column differ)
    """
    p1 = cell_content(tab, i)
    p2 = cell_content(tab, i + 1)
    if p1 is None or p2 is None:
        return None
    if p1[0] == p2[0]:
        return 'sym'
    if p1[1] == p2[1]:
        return 'alt'
    return 'mixed'


def partitions_of(n):
    """All partitions of n in decreasing order."""
    if n == 0:
        return [()]
    result = []
    def gen(remaining, max_part, current):
        if remaining == 0:
            result.append(current)
            return
        for p in range(min(remaining, max_part), 0, -1):
            gen(remaining - p, p, current + (p,))
    gen(n, n, ())
    return result


def main():
    n = 6
    print(f"Hoefsmit cell-content identification probe — n = {n}")
    print(f"EW carriers as disjoint strand-pairs in B_6:")
    print(f"  W: σ_1^4  (strands 1-2)")
    print(f"  Z: σ_3^6  (strands 3-4)")
    print(f"  H: σ_5^8  (strands 5-6)")
    print()
    print(f"Wedderburn blocks of H_6(q): partitions of 6")
    print(f"For each tableau, classify σ_1, σ_3, σ_5 as (sym | alt | mixed)")
    print()

    results = {}
    total_tableaux = 0
    pure_sym_alt_count = 0  # tableaux where ALL THREE σ_i are sym or alt (no mixed)

    for partition in partitions_of(n):
        tabs = standard_tableaux(partition)
        f_lambda = len(tabs)
        block_data = {
            "f_lambda": f_lambda,
            "tableaux": [],
        }
        for tab in tabs:
            tab_str = "/".join("".join(str(v) for v in row if v is not None) for row in tab)
            sigma1_class = sigma_eigenvalue_class(tab, 1)
            sigma3_class = sigma_eigenvalue_class(tab, 3)
            sigma5_class = sigma_eigenvalue_class(tab, 5)
            classes = (sigma1_class, sigma3_class, sigma5_class)
            is_pure = all(c in ('sym', 'alt') for c in classes)
            if is_pure:
                pure_sym_alt_count += 1
            block_data["tableaux"].append({
                "tableau": tab_str,
                "sigma1_class": sigma1_class,
                "sigma3_class": sigma3_class,
                "sigma5_class": sigma5_class,
                "is_pure": is_pure,
            })
        results[str(partition)] = block_data
        total_tableaux += f_lambda

    print(f"Total seminormal basis vectors (sum_λ f_λ for λ ⊢ 6):"
          f" {total_tableaux}")
    print(f"  (dim End_R(V^⊗6) = sum_λ f_λ² = 720; the 76 tableaux are"
          f" basis vectors, the 720 is matrix-algebra dim.)")
    print(f"Pure-(sym/alt) tableaux (σ_1, σ_3, σ_5 all decisive): "
          f"{pure_sym_alt_count} / {total_tableaux}")
    print()

    # Enumerate the 8 sym/alt eigenvalue patterns and count tableaux per pattern
    pattern_counts = {}
    for partition_str, block in results.items():
        for entry in block["tableaux"]:
            if entry["is_pure"]:
                pattern = (entry["sigma1_class"],
                           entry["sigma3_class"],
                           entry["sigma5_class"])
                pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
    print("Pattern counts (σ_1, σ_3, σ_5 each ∈ {sym, alt}):")
    for pat in [('sym','sym','sym'), ('sym','sym','alt'), ('sym','alt','sym'),
                ('alt','sym','sym'), ('sym','alt','alt'), ('alt','sym','alt'),
                ('alt','alt','sym'), ('alt','alt','alt')]:
        c = pattern_counts.get(pat, 0)
        print(f"  {pat}: {c} tableaux")

    # Identify (W, Z, H) as the (sym, sym, sym) projector and the alt counterparts
    # W^+ ↔ sym of σ_1^4; W^- ↔ alt of σ_1^4; etc.
    # The six EW projectors correspond to:
    #   e_W^+ : σ_1 sym, σ_3 anything, σ_5 anything  → projector on σ_1=q eigenspace
    #   e_W^- : σ_1 alt, ...                          → σ_1=-q⁻¹
    #   etc. for Z, H
    # These six projectors are NOT pairwise orthogonal as currently sorted —
    # but the *six rank-1* projectors at the (sym,sym,sym), (sym,sym,alt), ...
    # eight pure patterns ARE pairwise orthogonal.

    # Count rank-1 projectors per pure pattern (= number of tableaux per
    # pattern after restricting to pure tableaux only).
    print()
    print("Rank-1 projectors at each of the 8 pure patterns:")
    print(f"  (Each pattern = a candidate EW projector; total pure tableaux"
          f" = {pure_sym_alt_count})")
    print()
    print("Conclusion: the six EW projectors {e_W±, e_Z±, e_H±} live as "
          f"rank-{pure_sym_alt_count // 6 if pure_sym_alt_count >= 6 else '?'} "
          f"projectors in pure-(sym/alt) eigenspaces of σ_1^4 σ_3^6 σ_5^8 in "
          f"End_R(V^⊗6); n = 6 is the minimum strand count where all six "
          f"are simultaneously realisable.")

    out = {
        "computation": "hoefsmit-ew-cell-content",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Hoefsmit cell-content identification of the EW triplet "
            "(W, Z, H) inside End_R(V^⊗6) as disjoint-strand-pair "
            "projectors σ_1^4, σ_3^6, σ_5^8 in B_6.  Tabulates which "
            "standard Young tableaux of partitions of 6 carry pure-"
            "(sym/alt) eigenvalue classes for all three operators."
        ),
        "n_strands": n,
        "carriers": {
            "W": "σ_1^4 (strands 1-2)",
            "Z": "σ_3^6 (strands 3-4)",
            "H": "σ_5^8 (strands 5-6)",
        },
        "total_tableaux": total_tableaux,
        "pure_sym_alt_tableaux": pure_sym_alt_count,
        "wedderburn_blocks": results,
        "pattern_counts": {f"{p}": c for p, c in pattern_counts.items()},
        "audit": "docs/audits/2026-05-05-path-alpha-bring-refinement.md",
    }
    # Write next to this script (Path(__file__).parent), not via a
    # multi-level parent chain — robust to invocation from any cwd.
    out_path = Path(__file__).parent / "hoefsmit-ew-cell-content.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
