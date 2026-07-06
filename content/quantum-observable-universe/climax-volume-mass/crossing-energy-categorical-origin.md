**Remark (crossing weights are Hecke eigenvalues, not postulates).**

The per-crossing weights $(q, -q^{-1})$ of the [crossing
energy](#def:crossing-energy) are not chosen as an energetic penalty
laid on top of a topological framework.  They are the **two
eigenvalues of the Hecke generator**
$T = P \circ R \colon V \otimes V \to V \otimes V$ acting on the
symmetric/antisymmetric decomposition, and they are forced by the
rigid monoidal structure:

1. *Rigidity fixes the $R$-matrix determinant.*  Dualisability of
   $V$ together with the categorical volume constraint
   ([volume constraint](#def:quantum-observable-universe)) requires
   the braiding $R = c_{V,V}$ to satisfy
   $\det(R|_{V \otimes V}) = 1$, with eigenvalues $(q, q^{-1})$ on
   $S^{2} V \oplus \Lambda^{2} V$.
2. *The Hecke generator carries the transposition sign.*  The
   Hecke generator is $T = P \circ R$, where $P$ is the swap.
   Since $P|_{\Lambda^{2} V} = -\mathrm{id}$, composition flips the
   sign on the antisymmetric summand, giving $T$-eigenvalues
   $(q, -q^{-1})$ with $\det(T) = -1$ --- exactly the Hecke minimal
   polynomial $(T - q)(T + q^{-1}) = 0$
   ([eigenvalue extraction](#prop:braiding-eigenvalue-extraction)).
3. *Crossing weights are eigenvalues, not postulates.*  Assigning
   a positive crossing $L_{+}$ the weight $q$ and a negative
   crossing $L_{-}$ the weight $-q^{-1}$ is precisely the action
   of $T$ on a symmetric-channel input and $T^{-1}$ on an
   antisymmetric-channel input.  The sum
   $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})$ is therefore a trace
   of $T^{\pm 1}$-eigenvalues along the braid, dictated by the
   categorical structure.
4. *Gröbner--Shirshov resolution.*  When $\mathfrak{H}$ is reduced
   to Gröbner--Shirshov normal form
   ([nuclear normal form](#prop:nuclear-groebner-reduction)), each
   crossing contributes its $T$-eigenvalue exactly once; the net
   $\mathfrak{E}_{\mathrm{cross}}$ is the resulting Laurent
   polynomial in $q$, read off the normal form.  Removing any of
   these weights would violate duality and break the Hecke
   relation.

This quantity is computed entirely from the $R$-matrix braiding
([R-matrix](#rem:r-matrix-braiding)) of
$\mathcal{U}_q(\mathfrak{su}(2))$ acting on the tensor product
of constituent representations.
