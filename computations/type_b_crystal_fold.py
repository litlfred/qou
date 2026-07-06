#!/usr/bin/env python3
"""
Groundwork for Option D: Type-B folded crystal sum

This module implements the folding of the Type-A (sl_{2n+1}) Kashiwara crystal 
into a Type-B (so_{2n+1}) crystal using the Dynkin diagram automorphism.

According to AGENTS.md 7b:
"Fold the sl_n Cartan datum into a Type B datum; the resulting Kashiwara graph 
is a symmetric crystal, and its GS normal forms are bar-involution (q -> q^-1) invariant 
by construction. Stable matter = fixed points of the folded crystal."

For n=2 (Type B_2, so_5), we fold A_4 (sl_5).
The Dynkin diagram automorphism for A_{2n} swaps node i with 2n+1-i.
The simple roots of B_n are formed by:
- e_i = f_i f_{2n+1-i} (for i < n)
- e_n = f_n (with appropriate multiplier/virtuality scaling)
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from crystal_basis import SSYT, crystal_B, kashiwara_lower, kashiwara_raise

def apply_f_folded(T, i, n_type_b):
    """
    Applies the folded Kashiwara lowering operator F_i on the A_{2n} crystal T.
    For i < n: F_i = f_i f_{2n+1-i} (these commute)
    For i = n: F_n = f_n
    """
    n_type_a = 2 * n_type_b
    if i < n_type_b:
        # F_i = f_i f_{2n+1-i} for i < n
        T1 = kashiwara_lower(T, i)
        if T1 is None:
            return None
        return kashiwara_lower(T1, n_type_a + 1 - i)
    elif i == n_type_b:
        # F_n = f_n f_{n+1} f_n
        T1 = kashiwara_lower(T, i)
        if T1 is None:
            return None
        T2 = kashiwara_lower(T1, i + 1)
        if T2 is None:
            return None
        return kashiwara_lower(T2, i)
    else:
        raise ValueError(f"Invalid index {i} for Type B_{n_type_b}")

def apply_e_folded(T, i, n_type_b):
    """
    Applies the folded Kashiwara raising operator E_i on the A_{2n} crystal T.
    """
    n_type_a = 2 * n_type_b
    if i <= n_type_b:
        T1 = kashiwara_raise(T, i)
        if T1 is None:
            return None
        return kashiwara_raise(T1, n_type_a + 1 - i)
    else:
        raise ValueError(f"Invalid index {i} for Type B_{n_type_b}")

def type_b_crystal_graph(shape, n_type_b):
    """
    Generates the Type-B crystal graph by exploring via the folded operators,
    starting from the Type-A highest weight vector of the given shape.
    """
    # Highest weight vector for Type A
    # E.g. shape (1,1) -> rows ((1,), (2,))
    hw_rows = []
    for i, length in enumerate(shape):
        hw_rows.append(tuple(i + 1 for _ in range(length)))
    
    hw = SSYT(tuple(hw_rows))
    
    # BFS
    visited = {hw}
    queue = [hw]
    edges = []
    
    while queue:
        T = queue.pop(0)
        for i in range(1, n_type_b + 1):
            T_next = apply_f_folded(T, i, n_type_b)
            if T_next is not None and T_next not in visited:
                visited.add(T_next)
                queue.append(T_next)
                edges.append((T, i, T_next))
            elif T_next is not None:
                edges.append((T, i, T_next))
                
    return visited, edges

if __name__ == "__main__":
    n = 2  # B_2 (so_5)
    shape = (2, 1, 1, 1)  # Vector representation
    print(f"Generating Type-B folded crystal B({shape}) for n={n}")
    
    nodes, edges = type_b_crystal_graph(shape, n)
    print(f"Total nodes in folded crystal: {len(nodes)}")
    print(f"Total edges: {len(edges)}")
    
    for T in nodes:
        print(f"Node: {T.rows}")
