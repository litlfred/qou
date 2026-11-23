Let $A$ be the Frobenius--Hopf substrate algebra and let $D(A)$ denote its derived category of bimodules. A **rigid dualizing complex** for $A$ is a complex $\omega_A^\bullet$ of $A$-bimodules satisfying:

1. **Finite injective dimension:** The complex $\omega_A^\bullet$ has finite injective dimension as a left $A$-module and as a right $A$-module.
2. **Rigidifying isomorphism:** There exists an isomorphism $\omega_A^\bullet \simeq R\mathrm{Hom}_{A^e}(A, \omega_A^\bullet \otimes \omega_A^\bullet)$ in $D(A^e)$, where $A^e = A \otimes A^{\mathrm{op}}$ is the enveloping algebra \cite{yekutieli-zhang1999-auslander-dualizing}. A rigid dualizing complex, when it exists, is unique up to unique isomorphism. The complex $R\mathrm{Hom}_{A^e}(A, A^e)$ is a different object, the inverse dualizing complex; it is not the rigid dualizing complex.
3. **Van den Bergh duality:** For any finitely generated $A$-bimodule $M$, the rigid dualizing complex induces a duality $\mathrm{Ext}^i_A(M, \omega_A^\bullet) \cong H^{d-i}(M)^\vee$, where $d$ is the homological dimension of $A$.

The rigidity condition ensures that the dualizing complex is intrinsic to $A$, independent of base ring or presentation. This is the categorical substitute for the canonical sheaf in the non-commutative setting.
