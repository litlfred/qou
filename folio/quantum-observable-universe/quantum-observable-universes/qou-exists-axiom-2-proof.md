**Proof.**
It suffices to show $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.
By the Peter--Weyl decomposition for compact quantum groups
\cite{woronowicz1988},

$$
  \mathcal{O}_{q}(G)
  \;\cong\;
  \bigoplus_{\lambda \in \widehat{G}} V_{\lambda}^{*} \otimes V_{\lambda},
$$

and the adjoint action decomposes each summand as
$V_{\lambda}^{*} \otimes V_{\lambda} \cong \mathrm{End}(V_{\lambda})$.
The invariant subspace
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{End}(V_{\lambda}))$
consists only of scalar multiples of $\mathrm{id}_{V_{\lambda}}$, so
the only invariant morphisms $\mathbf{1} \to \mathrm{Ad}(A)$ factor
through the unit $\eta \colon \mathbf{1} \to A$, which is excluded by
axiom~(2).  Semisimplicity of $G$ and generic $q$ ensure no further
fixed vectors appear.  $\square$
