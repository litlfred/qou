Let $A$ be the Frobenius--Hopf substrate algebra and let $D(A)$ denote
its derived category of bimodules. A *rigid dualizing complex* for $A$
is a complex $\omega_A^\bullet$ of $A$-bimodules satisfying the
following conditions.

**Finite injective dimension.** The complex $\omega_A^\bullet$ has
finite injective dimension on both sides: as a left $A$-module and as a
right $A$-module.

**Rigidifying isomorphism.** There exists a canonical isomorphism

$$
\omega_A^\bullet
\simeq
R\mathrm{Hom}_{A^e}(A, A^e)
$$

in $D(A^e)$, where $A^e = A \otimes A^{\mathrm{op}}$ is the enveloping
algebra. This isomorphism is the *rigidifying structure*: it pins down
$\omega_A^\bullet$ up to unique isomorphism, eliminating the ambiguity
that afflicts ordinary dualizing complexes.

**Van den Bergh duality.** For any finitely generated $A$-bimodule $M$,
the rigid dualizing complex induces a duality

$$
\mathrm{Ext}^i_A(M, \omega_A^\bullet)
 \cong 
H^{d-i}(M)^\vee,
$$

where $d$ is the homological dimension of $A$.

The rigidity condition \cite{yekutieli2010} ensures that the
dualizing complex is *intrinsic* to $A$ --- it does not depend on a
choice of base ring or presentation. This makes $\omega_A^\bullet$ the
correct categorical substitute for the canonical sheaf in the
non-commutative setting.
