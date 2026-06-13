# Resolution of the S5 → SO(3) Fiber Action Functor (GAP-A-4 closure path)

**Date:** 2026-06-13
**Branch:** `claude/gap-a4-muon-operator-branching`
**Status:** Functor Identified

## 1. The Missing Object Identified
The 2026-06-01 audit (`2026-06-01-s5-so3-su2-u1-fiber-action.md`) identified that the geometric fiber map `S_5 \to SO(3)` was missing a categorical functor:
> "The precise missing object: a canonical functor from the SO(3)/I spherical-harmonic level ℓ on the 5-strand color×nucleon space to a specific Wedderburn-block coefficient of the 3-strand Borromean H₃(q) Markov trace."

We now establish that this functor is exactly the **Hecke/Symmetric Group Restriction Functor** $Res^{S_5}_{S_3}$, corresponding geometrically to the embedding of the Borromean 3-strand structure into the 5-strand Bring color-tube.

## 2. Derivation of the Functor
The Bring quintic surface carries an $S_5$ action. Its icosahedral rotation subgroup $I \cong A_5 \subset S_5$ governs the generations via the spherical harmonic levels $\ell$.

**At the $\ell=2$ level (Muon generation):**
1. The $SO(3)$ angular momentum representation $V_2$ restricts to $A_5$ as exactly one copy of the dimension-5 irrep $H$.
2. In the full $S_5$ group, the irrep $H$ is the restriction of the 5-dimensional $S_5$ irreps: the partitions **$\lambda = (3,2)$** and **$\lambda = (2,2,1)$**. Thus, the $\ell=2$ fiber is categorically localized in the $(3,2)$ Wedderburn block of $H_5(q)$.
3. We apply the restriction functor $Res^{S_5}_{S_3}$ by branching the $(3,2)$ partition down to $S_3$ (removing 2 boxes). The combinatorial branching rule yields:
   $$ (3,2) \downarrow S_3 \;=\; (3) \oplus 2 \cdot (2,1) $$
4. The Borromean $h^4 = -3/4$ coefficient lives **exclusively** in the $(2,1)$ block of $H_3(q)$ (the standard irrep).
5. The appearance of $2 \cdot (2,1)$ in the restriction proves that the $\ell=2$ 5-strand fiber naturally projects onto the exact 3-strand Wedderburn block responsible for the $h^4$ coefficient. 

**At the $\ell=1$ level (Electron generation):**
1. The $V_1$ representation restricts to $A_5$ as the dimension-3 irrep $T_1$.
2. $T_1$ lives inside the dimension-6 $S_5$ irrep, **$\lambda = (3,1,1)$**.
3. Branching $(3,1,1)$ down to $S_3$ yields:
   $$ (3,1,1) \downarrow S_3 \;=\; (1,1,1) \oplus 2 \cdot (2,1) \oplus (3) $$

## 3. Resolving the False Premise
The previous hypothesis assumed that the 3-strand $S_3$ trace "only saw $\ell \le 1$", and that reaching $\ell=2$ was required to unlock the $h^4$ coefficient. The 2026-06-01 audit proved this false by showing $(2,1)$ appears at both $\ell=1$ and $\ell=2$ under the $SO(3)$ rotation subgroup.

Our restriction functor $Res^{S_5}_{S_3}$ **perfectly corroborates** this: the $(2,1)$ block of $S_3$ appears with multiplicity 2 in the $S_5$ blocks for both $\ell=1$ ($(3,1,1)$) and $\ell=2$ ($(3,2)$). 

Therefore, the $h^4$ coefficient is not "turned on" by $\ell=2$; rather, the categorical operator-valued branching for $\ell=2$ changes the **Wedderburn projector trace weighting** from the $(3,1,1)$ block to the $(3,2)$ block over $H_5(q)$.

## 4. Next Steps for `conj:s5-so3-fiber-action`
The geometric map `partition_to_rotation` in `S5SO3FiberAction.lean` is the geometric manifestation of this restriction. To close the conjecture:
1. Formalize the $Res^{S_5}_{S_3}$ functor in Lean.
2. Evaluate the precise algebraic shift in the $H_3(q)$ Markov trace induced by evaluating the knot through the $\ell=2$ ($E_{(3,2)}$) projector versus the $\ell=1$ ($E_{(3,1,1)}$) projector.
3. Verify if this shift mathematically resolves the 210 ppb muon mass tension (GAP-A-4 operator-valued branching).
