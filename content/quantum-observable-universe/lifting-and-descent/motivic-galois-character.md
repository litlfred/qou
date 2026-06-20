The motivic-Galois layer on the Yekutieli obstruction
$\kappa_n \in H^2(\mathcal{S}, \mathbb{G}_m)$ is carried by a single
character of the cyclotomic Galois group, the **motivic Galois
character of the Frobenius–Hopf substrate**.

**Definition.**
*Let $A$ be the Frobenius–Hopf substrate of a quantum observable
universe with motivic class $[A] \in \widehat{\mathcal{M}}$
([motivic substrate](#def:motivic-substrate)). The **motivic
Galois character of $A$** is the homomorphism*

$$
  \chi^{\mathrm{mot}}_A
  \;\colon\;
  \mathrm{Gal}\bigl(\mathbb{Q}(\mu_\infty)/\mathbb{Q}\bigr)
  \;\longrightarrow\;
  \mathrm{Aut}_{\widehat{\mathcal{M}}}\bigl([A]\bigr)
$$

*encoding the action of the cyclotomic Galois group on the realization
tower $\{\rho_p\}_{p \in \mathrm{Pl}(\mathbb{Q})}$
([adelic substrate](#def:adelic-substrate)) of $[A]$. At each finite
place $p$ the local component*

$$
  \chi^{\mathrm{mot}}_{A,\,p}
  \;\colon\;
  \mathrm{Gal}\bigl(\bar{\mathbb{Q}}_p/\mathbb{Q}_p\bigr)
  \;\longrightarrow\;
  \mathrm{Aut}\bigl(\rho_p([A])\bigr)
$$

*is the Frobenius character on the cyclotomic-projection
$\rho_p \colon \widehat{\mathcal{M}} \twoheadrightarrow \mathbb{Z}[q]/\Phi_{p^k}(q)$
of the substrate. The Yekutieli obstruction $\kappa_n$
([quantum characteristic classes](#def:quantum-characteristic-classes))
is the image of $\chi^{\mathrm{mot}}_A$ under the
[HKR comparison](#rem:hochschild-kummer-connection) to
$H^2(\mathcal{S}, \mathbb{G}_m)$.*

**Why this is the right level.**
*Working with $\chi^{\mathrm{mot}}_A$ directly (rather than with each
$\kappa_n$ at every level $n$) means the perpetual obstruction
phenomenon ([Kummer tower](#rem:kummer-tower)) becomes a single
non-vanishing statement about the character — see
[motivic perpetual obstruction](#conj:motivic-perpetual-obstruction)
— rather than a per-level Čech-cocycle non-vanishing argument.
The Čech-cocycle / Hochschild presentations of $\kappa_n$ become
**realizations** of $\chi^{\mathrm{mot}}_A$ at the archimedean place
and the Hochschild-deformation place respectively; the gerbe-vs-
deformation duality of [Hochschild–Kummer](#rem:hochschild-kummer-connection)
is the dual of two such realizations.*

**Lean axiomatization.**
*The formal-chain class
[`MotivicGaloisCharacter`](../../lean/QOU/LiftingDescent/MotivicGaloisCharacter.lean)
takes a `MotivicSubstrate K0 Mhat Target` instance as an explicit
hypothesis and exposes the character $\chi^{\mathrm{mot}}_A$ + its
compatibility with each local realization $\rho_p$. Per AGENTS.md §3b,
`sorry` in any concrete instance is a substrate axiom, not a missing
proof.*
