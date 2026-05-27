**Conjecture (Borel--Zagier for QOU volumes).**
The three QOU hyperbolic volumes are $\mathbb{Q}$-linearly independent:

$$
  a_1 \,\mathrm{Vol}(4_1) + a_2 \,\mathrm{Vol}(5_2)
  + a_3 \,\mathrm{Vol}(\mathcal{B}_3) = 0,
  \quad a_i \in \mathbb{Q}
  \;\;\Longrightarrow\;\;
  a_1 = a_2 = a_3 = 0.
$$

This is a special case of the Borel--Zagier conjecture, which asserts
$\mathbb{Q}$-linear independence of volumes of pairwise
non-commensurable hyperbolic 3-manifolds.

**Non-commensurability of the QOU complements.**
Two manifolds are *commensurable* if they share a common
finite-sheeted cover.  The three QOU complements are pairwise
non-commensurable:

- $S^3 \setminus 4_1$: the unique arithmetic hyperbolic knot
  complement, commensurable with $\mathrm{PSL}_2(\mathcal{O}_3)$
  (Reid, 1991).
- $S^3 \setminus 5_2$: non-arithmetic (its trace field is cubic, not
  quadratic imaginary), so it lies in a distinct commensurability class.
- $S^3 \setminus \mathcal{B}_3$: a 3-component link complement with
  cusp geometry incompatible with the knot complements.  Its volume
  $\approx 7.32772$ is not a rational multiple of either knot volume
  (the ratios are $\mathrm{Vol}(\mathcal{B}_3)/\mathrm{Vol}(4_1)
  \approx 3.610$ and $\mathrm{Vol}(\mathcal{B}_3)/\mathrm{Vol}(5_2)
  \approx 2.592$, neither rational with small denominator).

**Relation to $K$-theory.**
The Borel regulator maps $K_3(\overline{\mathbb{Q}}) \to \mathbb{R}$,
and volumes of hyperbolic 3-manifolds live in its image.  The conjecture
is equivalent to the Borel regulator being injective (modulo torsion)
on the $K_3$-elements corresponding to these three complements.

This is strictly weaker than [algebraic
independence](#prop:hyperbolic-volume-transcendence), which rules out
all polynomial relations, not just linear ones.  But it is strictly
stronger than [irrationality](#prop:single-volume-irrationality), since
$\mathbb{Q}$-linear independence of three numbers implies each is
irrational.
