Let $\ell_n \colon A_n \hookrightarrow A_{n+1}$ denote the ascent embedding
([jet prolongation](#prop:jet-prolongation)) and
$\mathfrak{d}_{n+1} \colon \mathrm{End}_{\mathbf{C}}(A_{n+1}) \to \mathrm{End}_{\mathbf{C}}(A_n)$ the :defterm[descent]{#descent} homomorphism
([descent](#lem:descent)).  The *descent involution* at level $n$ is
the endomorphism of the level-$(n{+}1)$ endomorphism algebra:

$$
  \hat{\tau}_n =  \ell_n \circ \mathfrak{d}_{n+1}
   \colon 
  \mathrm{End}_{\mathbf{C}}(A_{n+1})
   \longrightarrow 
  \mathrm{End}_{\mathbf{C}}(A_{n+1}).
$$

Since $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$ on
$\mathrm{End}_{\mathbf{C}}(A_n)$ (the descent of the ascent recovers the
original endomorphism, because $\ell_n$ embeds $A_n$ as a direct summand of
$A_{n+1}$ and $\mathfrak{d}_{n+1}$ is the retraction), we have

$$
  \hat{\tau}_n^2
  = 
  \ell_n \circ \mathfrak{d}_{n+1} \circ \ell_n \circ \mathfrak{d}_{n+1}
  = 
  \ell_n \circ (\mathfrak{d}_{n+1} \circ \ell_n) \circ \mathfrak{d}_{n+1}
  = 
  \ell_n \circ \mathrm{id} \circ \mathfrak{d}_{n+1}
  = 
  \hat{\tau}_n,
$$

so $\hat{\tau}_n$ is idempotent.  Its image is the
*descended subalgebra* $\mathcal{A}_{n+1}^{\mathrm{desc}} \subseteq \mathrm{End}_{\mathbf{C}}(A_{n+1})$, consisting of endomorphisms at
level $n{+}1$ that factor through the level-$n$ algebra via the ascent
embedding.
