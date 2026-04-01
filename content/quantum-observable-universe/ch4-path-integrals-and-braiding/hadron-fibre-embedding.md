Let $\mathfrak{H} \in \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$ be a
hadron ([Definition](#def:hadron)) and let $\mathcal{S}_p$ denote the fibre of the
knot bundle over a point $p \in \mathbb{P}(V)$
([Definition](#def:projective-line-object)). A **fibre-compatible hadron
embedding** is a morphism

$$
  \iota_p \;\colon\;
  \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}
  \;\longrightarrow\;
  \mathcal{S}_p
$$

satisfying the following conditions:

1. **Integrability.** The embedding $\iota_p$ is *integrable* in the
   sense that the abstract hadron data (linking, braiding, Skein
   decomposition) can be consistently realized within the geometric
   structure of the fibre $\mathcal{S}_p$. Concretely, $\iota_p$ must intertwine
   the abstract Skein action
   ([operations on hadrons](#rem:hadron-operations)) with the
   geometric operations on knots in $\mathcal{S}_p$.

2. **Fibre confinement.** The image $\iota_p(\mathfrak{H})$ is entirely
   contained in the fibre $\mathcal{S}_p$. No constituent knot extends to a
   neighbouring fibre $E_{p'}$ for $p' \neq p$. This is enforced by a
   finite Mobius energy bound:

   $$
     \mathcal{E}_{\mathrm{Mob}}(\iota_p) \;<\; \infty,
   $$

   which prevents the knot complement from developing cusps that
   would reach the boundary of the fibre.

3. **Hopf compatibility.** The embedding respects linking and
   unlinking via the Hopf structure: the diagram

   ```tex
   \[
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}
       \ar[r, "\iota_p"]
       \ar[d, "\ell_{ij}"']
     & \mathcal{S}_p
       \ar[d, "\ell_{ij}"]
     \\
     \mathrm{Sym}^{n'}(K) \otimes \mathcal{L}_{\mathrm{Hopf}}'
       \ar[r, "\iota_p'"']
     & \mathcal{S}_p
   \end{tikzcd}
   \qquad\text{(Hopf compatibility)}
   \]
   ```

   commutes for every linking operation $\ell_{ij}$.

4. **Volume compatibility.** The embedding preserves hyperbolic
   volumes: $\mathrm{vol}(\iota_p(K_i)) = \mathrm{vol}(K_i)$ for each
   constituent knot $K_i$. This ensures that the mass contribution of
   each knot, computed via the hyperbolic volume, is faithfully
   represented in the fibre.


A localized hadron ([Definition](#def:localized-hadron)) equipped with a
fibre-compatible embedding is a **physically realized hadron**: it is
both situated at a base point and faithfully embedded in the fibre
geometry. The integrability condition is the key structural requirement
— it asserts that the abstract algebraic hadron can be "integrated"
into a concrete geometric realization.
