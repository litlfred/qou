Let $H \in \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$ be a
hadron ([Definition](#def:hadron)) and let $E_p$ denote the fibre of the
knot bundle over a point $p \in \mathbb{P}(V)$
([Definition](#def:projective-line-object)). A **fibre-compatible hadron
embedding** is a morphism

$$
  \iota_p \;\colon\;
  \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}
  \;\longrightarrow\;
  E_p
$$

satisfying the following compatibility conditions:

1. **Confinement (Mobius energy bound).** The embedding $\iota_p$
   has finite Mobius energy $\mathcal{E}_{\mathrm{Mob}}(\iota_p) < \infty$,
   ensuring that the constituent knots remain confined within the fibre
   $E_p$ and do not "escape" to neighbouring fibres.

2. **Hopf compatibility.** The embedding respects the linking structure:
   for any sub-configuration obtained by linking or unlinking via the
   Hopf structure, the image under $\iota_p$ undergoes the corresponding
   operation in $E_p$. That is, the diagram

   ```tex
   \[
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}
       \ar[r, "\iota_p"]
       \ar[d, "\text{link/unlink}"']
     & E_p
       \ar[d, "\text{link/unlink}"]
     \\
     \mathrm{Sym}^{n'}(K) \otimes \mathcal{L}_{\mathrm{Hopf}}'
       \ar[r, "\iota_p'"']
     & E_p
   \end{tikzcd}
   \]
   ```

   commutes.

3. **Volume compatibility.** The embedding preserves hyperbolic volumes:
   for each constituent knot $K_i$, the hyperbolic volume
   $\mathrm{vol}(\iota_p(K_i))$ in $E_p$ equals the abstract hyperbolic
   volume $\mathrm{vol}(K_i)$. Equivalently,
   $\iota_p^*(\mathrm{vol}_{E_p}) = \mathrm{vol}_{\mathrm{Sym}^n(K)}$.

A localized hadron ([Definition](#def:localized-hadron)) equipped with a
fibre-compatible embedding is a **physically realized hadron**: it is
both situated at a base point and faithfully embedded in the fibre
geometry.
