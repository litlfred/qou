The motivic-Galois layer on the obstruction $\kappa_n \in H^2(\mathcal{S}, \mathbb{G}_m)$ acts via a single character of the cyclotomic Galois group: the **motivic Galois character of the Frobenius–Hopf substrate**.

**Definition.**
Let $A$ be the Frobenius–Hopf substrate of a quantum observable universe. Let $[A] \in \widehat{\mathcal{M}}$ be its motivic class ([motivic substrate](#def:motivic-substrate)). The **motivic Galois character of $A$** is the homomorphism
$$
  \chi^{\mathrm{mot}}_A
  \;\colon\;
  \mathrm{Gal}\bigl(\mathbb{Q}(\mu_\infty)/\mathbb{Q}\bigr)
  \;\longrightarrow\;
  \mathrm{Aut}_{\widehat{\mathcal{M}}}\bigl([A]\bigr).
$$
This encodes the action of the cyclotomic Galois group on the realization tower $\{\rho_p\}_{p \in \mathrm{Pl}(\mathbb{Q})}$ ([adelic substrate](#def:adelic-substrate)) of $[A]$. At each finite place $p$, the local component
$$
  \chi^{\mathrm{mot}}_{A,\,p}
  \;\colon\;
  \mathrm{Gal}\bigl(\bar{\mathbb{Q}}_p/\mathbb{Q}_p\bigr)
  \;\longrightarrow\;
  \mathrm{Aut}\bigl(\rho_p([A])\bigr)
$$
is the Frobenius character on the cyclotomic projection $\rho_p \colon \widehat{\mathcal{M}} \twoheadrightarrow \mathbb{Z}[q]/\Phi_{p^k}(q)$. The obstruction $\kappa_n$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) is the image of $\chi^{\mathrm{mot}}_A$ under the [HKR comparison](#rem:hochschild-kummer-connection) to $H^2(\mathcal{S}, \mathbb{G}_m)$.

**Choice of level.**
Working directly with $\chi^{\mathrm{mot}}_A$ replaces per-level Čech-cocycle non-vanishing arguments with a single non-vanishing theorem about the character ([motivic perpetual obstruction](#conj:motivic-perpetual-obstruction), proved via Route A: prime-ideal collapse, $C = a_0(-1) + 2 \cdot a_1(-1)$). The Čech-cocycle and Hochschild presentations of $\kappa_n$ become realizations of $\chi^{\mathrm{mot}}_A$ at the archimedean and Hochschild-deformation places. The [Hochschild–Kummer](#rem:hochschild-kummer-connection) duality corresponds to the duality between these two realizations.

Conditional on the motivic substrate, the character $\chi^{\mathrm{mot}}_A$ is defined and is compatible with each local realization $\rho_p$.
