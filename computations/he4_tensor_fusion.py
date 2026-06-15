#!/usr/bin/env python3
"""
Investigating the Littlewood-Richardson fusion for ⁴He (4 nucleons)
H_3 ⊗ H_3 ⊗ H_3 ⊗ H_3 → H_12
"""

import sys
import os

# Import LR routines from existing script
import lr_fusion_self_conj_test as lr

def tensor_product(partitions):
    """
    Compute the LR decomposition of a list of partitions.
    Returns a dict mapping resulting partition (as tuple) to multiplicity.
    """
    if not partitions:
        return {}
    if len(partitions) == 1:
        return {tuple(partitions[0]): 1}
    
    current_decomp = {tuple(partitions[0]): 1}
    for p in partitions[1:]:
        next_decomp = {}
        for shape, mult in current_decomp.items():
            # Decompose shape ⊗ p
            step_decomp = lr.lr_decomposition(list(shape), p, max_partitions=1000)
            for new_shape, c in step_decomp:
                new_shape_t = tuple(new_shape)
                next_decomp[new_shape_t] = next_decomp.get(new_shape_t, 0) + mult * c
        current_decomp = next_decomp
    return current_decomp

def main():
    nucleons = [
        [3],
        [2, 1],
        [1, 1, 1]
    ]
    
    for nuc in nucleons:
        print(f"\n--- Fusion of four {nuc} nucleons ---")
        decomp = tensor_product([nuc, nuc, nuc, nuc])
        
        # Sort by partition size (all should be 12) then by lexicographical order
        sorted_shapes = sorted(decomp.keys(), key=lambda x: (-x[0], -len(x), x))
        
        # Check for presence of (4,4,4) and the trace-dominant 2-row partitions
        # [9,3], [8,4], [10,2], [11,1], [7,5]
        targets = [(4, 4, 4), (9, 3), (8, 4), (10, 2), (11, 1), (7, 5)]
        
        total_mult = sum(decomp.values())
        print(f"Total multiplicity: {total_mult}")
        for t in targets:
            if t in decomp:
                print(f"  {t} : {decomp[t]}")
            else:
                print(f"  {t} : NOT PRESENT")
        
        print("\n  Top 5 overall partitions by multiplicity:")
        top_mult = sorted(decomp.items(), key=lambda x: -x[1])[:5]
        for shape, c in top_mult:
            print(f"  {shape} : {c}")

if __name__ == "__main__":
    main()
