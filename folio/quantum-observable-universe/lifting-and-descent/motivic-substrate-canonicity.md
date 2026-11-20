**Canonicity of the substrate.** Three observations factor through $\mathcal{S}_{\mathrm{mot}}$ rather than any single realization:
- **Mass formulas.** The topological mass of a knot ([motivic mass measure](#def:motivic-mass-measure)) is a class $\mathfrak{m}_{\mathrm{mot}}(\beta) \in \widehat{\mathcal{M}}$, not a real number. The real-valued mass arises only after applying $\rho_\infty$.
- **Adelic factorisation.** The global zeta integral $\mathcal{Z}(s)$ of the [adelic substrate](#def:adelic-substrate) factorises as a restricted product $\prod_v \zeta_v(s)$. This is the realization-tower factorisation $\rho_{\mathrm{tot}} = \prod_v \rho_v$ applied to a single motivic class.
- **Habiro evaluation.** The Habiro ring $\widehat{\mathbb{Z}[q]}$ is the universal target of the non-archimedean realizations of $\mathcal{S}_{\mathrm{mot}}$. The functor $\rho_p$ evaluates a motivic class at the level-$p$ root of unity. The inverse limit over $p$ recovers the Habiro completion.

Every algebraic invariant taking values in $\mathbb{R}$, $\mathbb{Q}_p$, or the Habiro ring is the realization at some place $v$ of a single motivic class living in $\widehat{\mathcal{M}}$.

**Relation to existing blocks.**
- The [Frobenius–Hopf substrate](#def:frobenius-hopf-substrate) is the algebraic-place realization. It forms a finite-type structure on $\mathcal{S}_{\mathrm{mot}}$.
- The [adelic substrate](#def:adelic-substrate) is the place-decomposition $\mathbb{A} = \mathbb{R} \times \prod_p' \mathbb{Q}_p$ indexing the realization tower. The adelic decomposition of a motivic class is the restricted product $\rho_{\mathrm{tot}}([X]) = (\rho_v([X]))_v$.
- The [arc space](#def:arc-space) $\mathcal{L}(X)$ provides the measurable space for motivic integration into $\widehat{\mathcal{M}}$. One derives the Kontsevich–Denef–Loeser motivic measure \cite{kontsevich1995, denef-loeser2001} from this space.

**Out of scope.** Mixed motives, Bloch–Kato exact sequences, and full motivic Galois groups are not axiomatized here. The realization tower is presented purely as the family $\{\rho_v\}$ of place-indexed evaluations; the categorical relationships among the $\rho_v$ remain implicit.
