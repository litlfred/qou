The $\mathrm{Ad}$ component of an observation
([observation](#def:observation)) acts directly on
fermions.  The mechanism is the eigenspace decomposition
of the Hecke generator $\sigma$:

$$
  V \otimes V
  = 
  \underbrace{\mathrm{Sym}^2(V)}_{\text{bosonic, eigenvalue } q}
   \oplus 
  \underbrace{\textstyle\bigwedge^2(V)}_{\text{fermionic, eigenvalue } {-q^{-1}}}
$$

The two idempotents are:

$$
  e_+ = \frac{\sigma + q^{-1}}{q + q^{-1}}, \qquad
  e_- = \frac{q - \sigma}{q + q^{-1}}
$$

with $e_+$ projecting onto $\mathrm{Sym}^2$ (bosonic) and
$e_-$ onto $\bigwedge^2$ (fermionic).

**How observation acts on each sector.**

- **On bosons** ($\mathrm{Sym}^2$): the observation preserves
  the eigenspace.  The $\mathrm{Ad}$ action commutes with
  $e_+$: symmetric states remain symmetric.  The commutator
  of two observations vanishes on bosons
  ([two-observer parallelogram](#rem:two-observer-parallelogram)):
  $[I_1, I_2](\alpha_p) = 0$ when
  $\alpha$ is a boson.  Bosons can be observed without
  interference.

- **On fermions** ($\bigwedge^2$): the observation rotates
  the state within the colour fibre.  The $\mathrm{Ad}$
  action conjugates the antisymmetric component by $G$,
  which generically does **not** preserve $\bigwedge^2$ —
  it mixes the fermionic state with the bosonic eigenspace.
  This is the projection $e_+$: the observation partially
  converts fermionic content to bosonic content, depositing
  $q + q^{-1}$ per crossing in the colour fibre
  ([observation energy](#prop:observation-energy)).

  The commutator is non-zero on fermions:
  $[I_1, I_2](\alpha_p) \neq 0$.  Two
  observers acting on the same fermion interfere because
  each observation rotates the $\bigwedge^2$ component in a
  different direction in the colour fibre, and these
  rotations do not commute (the Hopf structure is
  non-cocommutative on $\bigwedge^2$).

**The physical picture.**

An observation reads the field through the $J^1$ (jet)
component — this is passive and commutative.  But to extract
information from a fermion, the observation must also act
through the $\mathrm{Ad}$ component — rotating the colour
fibre.  This rotation is the backreaction: it changes the
fermion's state in the process of measuring it.

The uncertainty is not epistemic (we lack information) but
geometric: the $\mathrm{Ad}$ action on $\bigwedge^2(V)$ is
a non-commutative rotation in the colour fibre.  Two
observations compose as group elements in $G$, and
$G = \mathrm{SU}_2(R)$ is non-abelian.  The order of
observation matters because rotations in three dimensions
do not commute.

This is why uncertainty is kept in the Reeb bundle --- the
$U(1)$ fibration $S^3 \to \mathcal{S}_p \cong S^2$ over the exceptional
divisor.  The Reeb vector field generates the $U_1(R) \subset G$
that commutes with everything --- it is the **one direction** in
the colour fibre where observations do commute.  The
remaining two directions (the off-diagonal generators of
$\mathfrak{su}(2)$) are where fermionic uncertainty lives.
