The QOU framework's algebraic substrate has appeared so far through
two faces — the [Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)
(quantum vacuum as a Frobenius–Hopf algebra) and the
[adelic substrate](#def:adelic-substrate) (decomposition over places of
$\mathbb{Q}$). Both are realizations of a single underlying object:
the **motivic substrate**, a Grothendieck-ring datum equipped with a
tower of realization functors.

**Definition (motivic substrate, axiom).**
*The **motivic substrate** of the QOU framework is the triple*

$$
  \mathcal{S}_{\mathrm{mot}}
  \;:=\;
  \bigl(K_0(\mathrm{Var}_k),\; \mathbb{L},\; \{\rho_v\}_{v \in \mathrm{Pl}(\mathbb{Q})}\bigr),
$$

*consisting of:*

1. *the **Grothendieck ring of varieties** $K_0(\mathrm{Var}_k)$ over
 the base field $k$ — the free abelian group on isomorphism classes
 $[X]$ of $k$-varieties modulo the scissor relations
 $[X] = [Z] + [X \setminus Z]$ for closed $Z \subseteq X$, with
 product $[X] \cdot [Y] = [X \times_k Y]$;*
2. *the **Lefschetz motive** $\mathbb{L} := [\mathbb{A}^1_k] \in
   K_0(\mathrm{Var}_k)$, with the localized ring
 $\mathcal{M} := K_0(\mathrm{Var}_k)[\mathbb{L}^{-1}]$ and its
 dimension-completion $\widehat{\mathcal{M}}$
 ([motivic mass measure](#def:motivic-mass-measure));*
3. *a **realization tower**
 $\{\rho_v \colon \widehat{\mathcal{M}} \to \widehat{\mathcal{M}}_v\}$,
 one realization functor per place $v$ of $\mathbb{Q}$
 ([adelic substrate](#def:adelic-substrate)). The archimedean
 realization $\rho_\infty$ is the
 [archimedean realization functor](#def:archimedean-realization-functor),
 landing in $\mathbb{R}$; the non-archimedean realizations
 $\rho_p$ at a finite prime $p$ produce local cyclotomic /
 Kummer-level data compatible with the Habiro-ring framework
 ([Habiro completion](#prop:full-pole-structure-mass-trace)).*

**Why this is the right substrate.** Three observations accordingly
factor through $\mathcal{S}_{\mathrm{mot}}$ rather than through any
single one of its realizations:

- **Mass formulas** — the topological mass of a knot
 ([motivic mass measure](#def:motivic-mass-measure)) is a class
 $\mathfrak{m}_{\mathrm{mot}}(\beta) \in \widehat{\mathcal{M}}$,
 *not yet a real number*; the real-valued mass arises only after
 applying $\rho_\infty$.
- **Adelic factorisation** — the global zeta integral
 $\mathcal{Z}(s)$ of [adelic substrate](#def:adelic-substrate)
 factorises as a restricted product $\prod_v \zeta_v(s)$, which is
 exactly the realization-tower factorisation
 $\rho_{\mathrm{tot}} = \prod_v \rho_v$ applied to a single
 motivic class.
- **Habiro evaluation** — the Habiro ring
 $\widehat{\mathbb{Z}[q]}$ is the universal target of the
 non-archimedean realizations of $\mathcal{S}_{\mathrm{mot}}$:
 $\rho_p$ evaluates a motivic class at the level-$p$ root of unity,
 and the inverse limit over $p$ recovers the Habiro completion.

This is the structural content of the substrate axiom: every
algebraic invariant of the QOU framework that takes values in either
$\mathbb{R}$, $\mathbb{Q}_p$, or the Habiro ring is the realization at
some place $v$ of a single motivic class living in $\widehat{\mathcal{M}}$.

**Relation to existing blocks.**

- The [Frobenius–Hopf substrate](#def:frobenius-hopf-substrate) is
 the algebraic-place realization: a particular finite-type structure
 on $\mathcal{S}_{\mathrm{mot}}$, not an additional substrate.
- The [adelic substrate](#def:adelic-substrate) is the place-decomposition
 $\mathbb{A} = \mathbb{R} \times \prod_p' \mathbb{Q}_p$ that indexes
 the realization tower. Adelic decomposition of any motivic class is
 then the Tate-style restricted product
 $\rho_{\mathrm{tot}}([X]) = (\rho_v([X]))_v$.
- The [arc space](#def:arc-space) $\mathcal{L}(X)$ provides the
 measurable space for motivic integration into $\widehat{\mathcal{M}}$;
 Kontsevich–Denef–Loeser motivic measure
 \cite{kontsevich1995, denef-loeser2001} is a derived structure.

**Out of scope (deferred).** This definition does **not** axiomatize
mixed motives, Bloch–Kato exact sequences, motivic Galois groups, or
$\ell$-adic Galois realizations beyond what is needed for the QOU
framework. The realization tower is presented purely as the family
$\{\rho_v\}$ of place-indexed evaluations; the categorical
relationships among $\rho_v$ at different places (motivic Galois
action) are left implicit and are not used in subsequent chapters.
A future paper on motivic Galois structure of the QOU substrate is
the natural extension target.

**Lean axiomatization.** The substrate is axiomatized as a Lean
`class` (per AGENTS.md §3b) with fields encoding $K_0(\mathrm{Var}_k)$,
$\mathbb{L}$, the localization $\widehat{\mathcal{M}}$, and the family
of realization functors. The `sorry` in any concrete instance is
understood as a substrate axiom, not a missing proof; downstream
results in the realization tower (e.g.
[archimedean realization functor](#def:archimedean-realization-functor))
take a `[MotivicSubstrate]` instance as a hypothesis and derive
their conditional content fully verified.
