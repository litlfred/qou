Let $\mathfrak{H} = [K_1, \ldots, K_n]_p \bowtie \mathcal{L}$ be a composite
of knots linked by a link $\mathcal{L}$, with braid word
$\beta \in B_n$ representing the linking.  The *crossing energy*
of $\mathfrak{H}$ is

$$
  \mathbf{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \sum_{\text{crossings in } \beta}
  \begin{cases}
    q   & \text{positive crossing } (L_+), \\
    -q^{-1} & \text{negative crossing } (L_-),
  \end{cases}
$$

where $q$ is the substrate parameter
([substrate parameter](#def:substrate-parameter)) and the sign
convention follows the Skein relation

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0.
$$

### Categorical origin: $\mathbf{E}_{\mathrm{cross}}$ is not an external postulate

The per-crossing weights $(q, -q^{-1})$ are not chosen as an
energetic penalty laid on top of a topological framework.  They
are the **two eigenvalues of the Hecke generator**
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
   $\mathbf{E}_{\mathrm{cross}}(\mathfrak{H})$ is therefore a trace
   of $T^{\pm 1}$-eigenvalues along the braid, dictated by the
   categorical structure.
4. *Gröbner--Shirshov resolution.*  When $\mathfrak{H}$ is reduced
   to Gröbner--Shirshov normal form
   ([nuclear normal form](#prop:nuclear-groebner-reduction)), each
   crossing contributes its $T$-eigenvalue exactly once; the net
   $\mathbf{E}_{\mathrm{cross}}$ is the resulting Laurent
   polynomial in $q$, read off the normal form.  Removing any of
   these weights would violate duality and break the Hecke
   relation.

The crossing energy measures the net Skein weight of the composite:
positive $\mathbf{E}_{\mathrm{cross}}$ indicates repulsion dominates,
negative indicates binding dominates.  This quantity is computed
entirely from the $R$-matrix braiding
([R-matrix](#rem:r-matrix-braiding)) of
$\mathcal{U}_q(\mathfrak{su}(2))$ acting on the tensor product
of constituent representations.
