# Structural Falsification of `BringFiberAction` via Orbit Counting

**Date:** 2026-06-13
**Branch:** `claude/s5-so3-fiber-action-functor`
**Status:** Falsified Lean Class Premises

## 1. The Contradiction in `S5SO3FiberAction.lean`
The conditional class `BringFiberAction` requires a geometric map:
`partition_to_rotation : PartitionOf5 → IcosahedralRotation`
with two key axioms:
1. `respects_conjugate`: `angle(p') = - angle(p)` where `p'` is the conjugate partition of `p`.
2. `hits_five_conjugacy_classes`: The image must cover all 5 conjugacy classes of the icosahedral group $A_5 \cong I$.

**Theorem: These two axioms are mutually unsatisfiable.**
*Proof:* The conjugacy classes of the icosahedral group $I$ are completely determined by the absolute rotation angle $|\theta| \in \{0, \pi, 2\pi/3, 2\pi/5, 4\pi/5\}$. 
By `respects_conjugate`, a partition $p$ and its conjugate $p'$ must map to angles $\theta$ and $-\theta$. In $SO(3)$, and specifically in $A_5$, $\theta$ and $-\theta$ belong to the **same conjugacy class** (e.g., the 5-cycles $(12345)$ and $(15432)$ are conjugate in $A_5$). 
Therefore, the function maps any conjugate pair $\{p, p'\}$ into a single conjugacy class. 

The domain `PartitionOf5` has 7 elements, which partition into 4 orbits under conjugation:
- $O_1 = \{(5), (1,1,1,1,1)\}$
- $O_2 = \{(4,1), (2,1,1,1)\}$
- $O_3 = \{(3,2), (2,2,1)\}$
- $O_4 = \{(3,1,1)\}$ (self-conjugate)

Since the map is constant on each of the 4 orbits, the image can hit **at most 4 distinct conjugacy classes**. It is mathematically impossible to hit all 5 conjugacy classes of $A_5$. $\square$

## 2. The True Functor Domain: $A_5$ Irreps, not $S_5$ Partitions
The structural error is attempting to map the 7 Wedderburn partitions of $S_5$ bijectively to the 5 conjugacy classes of $A_5$.
Instead, the correct index set is the **irreducible representations of $A_5$**.

Because the sign character is trivial on even permutations, a partition $\lambda$ and its conjugate $\lambda'$ restrict to the **exact same** representation of $A_5$:
- $O_1$: $(5)$ and $(1,1,1,1,1)$ restrict to the 1D irrep $A$.
- $O_2$: $(4,1)$ and $(2,1,1,1)$ restrict to the 4D irrep $G$.
- $O_3$: $(3,2)$ and $(2,2,1)$ restrict to the 5D irrep $H$ (the Muon generation $\ell=2$).
- $O_4$: $(3,1,1)$ is self-conjugate and **splits** into two distinct 3D irreps $T_1$ and $T_2$ (the Electron generation $\ell=1$ corresponds to $T_1$).

This yields exactly $1 + 1 + 1 + 2 = 5$ irreducible representations of $A_5$.
The canonical map is between the 5 irreps of $A_5$ and the 5 conjugacy classes of $A_5$, fulfilling the standard character-table duality.

## 3. Resolution for the Lean Formalism
To fix `conj:s5-so3-fiber-action`:
1. The domain of `partition_to_rotation` must be redefined. Instead of mapping $S_5$ partitions directly to rotations, the functor maps $A_5$ irreps to conjugacy classes.
2. The $\ell=1$ spherical harmonic targets $T_1 \subset (3,1,1)$.
3. The $\ell=2$ spherical harmonic targets $H$, which lifts symmetrically to the conjugate pair $\{(3,2), (2,2,1)\}$.
4. The Hecke algebra restriction $Res^{S_5}_{S_3}$ established in the previous audit operates on these $S_5$ lifts.

This removes the impossible `respects_conjugate` geometric sign-flip, correctly identifying that conjugate Wedderburn blocks correspond to the exact same $SO(3)$ physical fiber action.
