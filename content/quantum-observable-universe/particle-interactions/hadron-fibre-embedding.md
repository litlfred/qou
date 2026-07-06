Abstract hadrons encode topological data algebraically. To represent a physical particle, this data must embed into the geometric fibre of the knot bundle over spacetime. 

Let $\mathfrak{H} \in \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$ be a hadron ([Definition](#def:hadron)). Let $\mathcal{S}_p$ denote the fibre over a point $p \in \mathbb{P}(V)$ ([Definition](#def:projective-line-object)). A **fibre-compatible hadron embedding** is a morphism

$$
  \iota_p \colon \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}} \longrightarrow \mathcal{S}_p
$$

satisfying four conditions.

1. **Integrability.** The abstract Skein action ([operations on hadrons](#rem:hadron-operations)) intertwines with the geometric operations on knots in $\mathcal{S}_p$. The embedding realizes the abstract linking, braiding, and Skein decomposition geometrically.
2. **Fibre confinement.** The image $\iota_p(\mathfrak{H})$ lies entirely in $\mathcal{S}_p$. No constituent knot extends to a neighbouring fibre $E_{p'}$ for $p' \neq p$. A finite Möbius energy bound enforces this:

   $$
     \mathcal{E}_{\mathrm{Mob}}(\iota_p) < \infty.
   $$

   This prevents the knot complement from developing cusps that reach the fibre boundary.
3. **Hopf compatibility.** The embedding respects the Hopf structure. For every linking operation $\ell_{ij}$, the following diagram commutes:

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

4. **Volume compatibility.** The embedding preserves hyperbolic volumes: $\mathrm{vol}(\iota_p(K_i)) = \mathrm{vol}(K_i)$ for each constituent knot $K_i$. This ensures the geometric mass contribution faithfully matches the abstract volume.

A localized hadron ([Definition](#def:localized-hadron)) with a fibre-compatible embedding is a **physically realized hadron**. The integrability condition ensures the abstract algebraic structure admits a strict geometric realization.
