*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
fundamental object $V$ of rank $2$ and braiding
$c_{V,V} \colon V \otimes V \to V \otimes V$.  Then:

1. **Spectral decomposition.** The tensor square decomposes
   as $V \otimes V = S^2 V \oplus \Lambda^2 V$, where $S^2 V$
   (symmetric) and $\Lambda^2 V$ (antisymmetric) are the eigenspaces
   of $c_{V,V}$.  This decomposition is *intrinsic* to $\mathbf{C}$
   — it depends only on the braiding, not on any external parameter.

2. **Eigenvalue definition of $q$.** Since $\Lambda^2 V \cong \mathbf{1}$
   ([volume constraint](#eq:categorical-volume-constraint)) is simple,
   $c_{V,V}$ acts on it by a scalar
   $\lambda_- \in \mathrm{End}(\mathbf{1}) \cong k$.  Similarly,
   $c_{V,V}$ acts on the $3$-dimensional $S^2 V$ by a scalar
   $\lambda_+$.  Define

   $$
     q  :=  \lambda_+,
     \qquad
     \lambda_- =  -q^{-1}.
   $$

   This is a *categorical invariant*: it is determined by the
   braiding endomorphism of $\mathbf{C}$ alone.

3. **Hecke relation.** The eigenvalue pair $(\lambda_+, \lambda_-) = (q, -q^{-1})$ is equivalent to the Hecke relation on
   $T = \tau(c_{V,V})$:

   $$
     (T - q)(T + q^{-1}) =  0,
   $$

   and the product $\lambda_+ \cdot \lambda_- = -1$ (which follows
   from $\det(c_{V,V}) = -1$ on a rank-$2$ object with trivial
   determinant).  The Hecke relation is intrinsic: it is a
   polynomial identity on the braiding morphism in $\mathbf{C}$.

4. **Classical vs.\ quantum.** When $c_{V,V}^2 = \mathrm{id}$,
   the eigenvalues are $+1$ and $-1$, giving $q = 1$ (symmetric
   monoidal, classical). When $c_{V,V}^2 \neq \mathrm{id}$,
   $q \neq 1$ and the category is genuinely braided — this is
   the quantum regime.

5. **Connection to the substrate parameter.** The categorical
   $q$ extracted here coincides with the
   ([substrate parameter](#def:substrate-parameter)): the
   one-parameter family $d_q = q^{-1} d + (1 - q^{-1}) \pi_V \circ d$
   is parametrised by the *same* $q \in \mathrm{End}(\mathbf{1})$
   that appears as the braiding eigenvalue.  The braiding determines
   the differential geometry.

**Summary.** The deformation parameter $q$ is not imposed externally.
It is the eigenvalue of the braiding $c_{V,V}$ on the symmetric
summand of $V \otimes V$ — a purely categorical datum, extracted from
the monoidal structure of $\mathbf{C}$ via the Hecke relation.
The Tannaka--Krein reconstruction
([reconstruction](#prop:tannaka-krein-reconstruction)) then recovers the
quantum group $\mathrm{SU}_q(2)$ as $\mathrm{End}^{\otimes}(\tau)$,
with $q$ already determined by the category.

**Mathematical Novelty.** While using the Hecke relation and determinant constraint to relate braiding eigenvalues is standard algebraic manipulation (e.g., following Kassel), the mathematical novelty here is treating this extraction not as a definition of $q$, but as a rigorous proof that the macroscopic substrate parameter governing the fluid PDE is precisely and completely constrained by the microscopic categorical braiding of the observable universe.
