<!-- FILE_START: plancherel-knot-factor-mass-tower-intro.md -->
The preceding sub-section developed the Plancherel-$\alpha$
spectral foundations ($\alpha_{\mathrm{em}}$ categorical trace,
Plancherel term-7 formulation, weight boundedness, unified
curvature-rank-mass formula, chirality residue mass term,
$E_\infty$-page identifications, spectral-sequence $H^3$ explicit
form, chirality-writhe ribbon derivation, Gram-matrix spectral
connection). This sub-section then traces the knot-factor
identification and the Wedderburn enumeration that close the
mass-tower arc: knot-factor spectral derivation + amphicheiral +
Borromean-composite + shell-closed + spectral summary, Pauli-
factor Wedderburn, mass-formula Wedderburn enumeration, mass-tower
coefficient stratification, and the flavor-dressing functor.

The closing blocks specialise the substrate-level knot-factor to amphicheiral knots, Borromean composites, and shell-closed configurations, then exhibit the Pauli-factor Wedderburn decomposition and the mass-tower coefficient stratification that the next sub-section consumes.
<!-- FILE_END: plancherel-knot-factor-mass-tower-intro.md -->

<!-- FILE_START: knot-factor-spectral-derivation.md -->
**Proposition (knot factor as chirality Gram pairing).**
*Let $\mathcal{K}$ be a knot with braid representative
$\beta_\mathcal{K} \in B_n$ and mirror $\beta_\mathcal{K}^*$, working
over $A = H_n(R, q)$.  The knot factor $a_\mathcal{K}$ in the unified
mass formula
([unified mass formula](#prop:unified-curvature-rank-mass-formula))
is the normalised chirality Gram pairing*

$$
  a_\mathcal{K} \;=\;
  \frac{G_{\beta_\mathcal{K},\, \beta_\mathcal{K}^*}}
       {G_{\mathbf{1},\, \mathbf{1}}}
  \;=\;
  \sum_{\lambda \,\vdash\, n}
    w_\lambda \,
    \frac{\chi_\lambda(\beta_\mathcal{K})\, \chi_\lambda(\beta_\mathcal{K}^*)}
         {\chi_\lambda(\mathbf{1})^2},
$$

*with Plancherel weights $w_\lambda = \dim_q^2 V_\lambda / [n]_q!$
summing to $1$.  The identity is exact in $R$.*
<!-- FILE_END: knot-factor-spectral-derivation.md -->

<!-- FILE_START: knot-factor-amphicheiral.md -->
**Corollary (knot factor for Markov-amphicheiral knots).**
*Let $\mathcal{K}$ be **Markov-amphicheiral**: its mirror braid
representative $\beta_\mathcal{K}^*$ is conjugate to
$\beta_\mathcal{K}$ in $H_n(R, q)$ — i.e. there exists
$w \in H_n(R, q)^{\times}$ with*

$$
  \beta_\mathcal{K}^* \;=\; w\,\beta_\mathcal{K}\, w^{-1}.
$$

*Then the knot factor is a sum of positive squares weighted by
Plancherel weights:*

$$
  a_\mathcal{K} \;=\;
  \sum_{\lambda \vdash n}\, w_\lambda\,
  \frac{\chi_\lambda(\beta_\mathcal{K})^2}{\chi_\lambda(\mathbf{1})^2}.
$$
<!-- FILE_END: knot-factor-amphicheiral.md -->

<!-- FILE_START: knot-factor-borromean-composite.md -->
**Corollary (Borromean-$k$ composite knot factor).**
*A Brunnian $k$-component composite — every $(k{-}1)$-component
sublink trivial — has central-idempotent expansion equal to the
$k$-fold independent product of figure-eight pairings.  The knot
factor is*

$$
  a_{\mathrm{Bor}_k} \;=\; (a_{4_1})^k \;=\; (1 - h^2)^k.
$$

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: knot-factor-borromean-composite.md -->

<!-- FILE_START: knot-factor-shell-closed.md -->
**Corollary (shell-closed knot factor).**
*For $Z = N$ even-even nuclei, the Markov chain on the three
$H_3(R, q)$ partitions
([three-parameters Wedderburn](#prop:three-parameters-wedderburn))
returns to equilibrium after every inter-nucleon crossing: the pp
and nn character shifts cancel exactly.  In the spectral language,
$\beta_\mathcal{K} \cdot \beta_\mathcal{K}^*$ projects entirely onto
the trivial idempotent $e_{(n)}$:*

$$
  \chi_\lambda(\beta_\mathcal{K} \cdot \beta_\mathcal{K}^*)
  \;=\;
  \delta_{\lambda, (n)} \cdot \chi_{(n)}(\mathbf{1})^2,
  \qquad\Longrightarrow\qquad
  a_\mathcal{K} \;=\; 1.
$$

*The result is exact algebraic cancellation, not approximation.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: knot-factor-shell-closed.md -->

<!-- FILE_START: knot-factor-spectral-summary.md -->
The three corollaries
([amphicheiral](#cor:knot-factor-amphicheiral),
[Borromean-$k$](#cor:knot-factor-borromean-composite),
[shell-closed](#cor:knot-factor-shell-closed)) replace the empirical
per-isotope $a_\mathcal{K}$ choices with derived expressions:

| Nucleus | Knot family | Empirical $a$ | Spectral derivation |
|---|---|---|---|
| ${}^3\mathrm{H},\ {}^3\mathrm{He}$ | $4_1$ figure-eight | $1 - h^2$ | Amphicheiral self-pairing on $e_{(1^n)}$ |
| ${}^4\mathrm{He}$ | Borromean-$2$ | $(1 - h^2)^2$ | Independent product of two figure-eight pairings |
| ${}^{12}\mathrm{C},\ {}^{40}\mathrm{Ca},\ {}^{56}\mathrm{Fe},\ {}^{208}\mathrm{Pb}$ | Shell-closed | $1$ | Markov-chain equilibrium $\Rightarrow$ projection onto $e_{(n)}$ alone |
| Odd-odd $Z = N$ (${}^6\mathrm{Li},\ {}^{14}\mathrm{N}$) | Asymmetric | $1 - \delta_{\mathrm{Wigner}}$ | Last-neutron breaking $\Rightarrow$ residual on standard irrep |

**Practical computation.**
The Hoefsmit pipeline
([Hoefsmit](#conj:hoefsmit-scattering-pipeline)) produces
$\chi_\lambda(\beta_\mathcal{K})$ for any braid word.  The knot
factor is then a single q-deformed Wedderburn-weighted sum,
bounded (though not unit-normalised) by Wedderburn completeness with
no truncation.  Implementation: replace per-isotope
hand-fits in the formal derivation
with direct evaluation of
([knot factor](#prop:knot-factor-spectral-form)).
<!-- FILE_END: knot-factor-spectral-summary.md -->

<!-- FILE_START: pauli-factor-wedderburn.md -->
**Proposition (spectral form of $F_{\mathrm{Pauli}}$).**
*Working over $A = H_n(R, q)$, the Pauli statistical weight in
nuclear $Q$-value formulas
([mass-formula validation](#rem:mass-formula-validation)) is the
ratio of Wedderburn-block traces*

$$
  F_{\mathrm{Pauli}}(\beta_\mathcal{K})
  \;=\;
  \frac{\int_{A_{(1^n)}}\!\rho(\beta_\mathcal{K})}
       {\int_{A_{(n)}}\!\rho(\beta_\mathcal{K})}
  \;=\;
  \frac{\chi_{(1^n)}(\beta_\mathcal{K}) \cdot \dim_q V_{(1^n)}}
       {\chi_{(n)}(\beta_\mathcal{K}) \cdot \dim_q V_{(n)}}
  \,\in\, R,
$$

*the alternating-block trace divided by the symmetric-block trace.
$F_{\mathrm{Pauli}}$ vanishes when $\beta_\mathcal{K}$ has no
alternating-block content (bosonic) and is a unit when
$\beta_\mathcal{K}$ saturates the alternating block (fully fermionic).*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: pauli-factor-wedderburn.md -->

<!-- FILE_START: mass-tower-coefficient-stratification.md -->
**Proposition (mass-tower coefficients are forced by Wedderburn strata).**
*Working over $A = H_n(R, q)$, every prefactor $\alpha_k$ in the
unified mass formula
$\mathfrak{m}_{q, \mathcal{K}}(\mathcal{T}) = \sum_{k = 0}^{n-1}
\alpha_k \cdot \mathfrak{m}^{(k)}_{q, \mathcal{K}}(\mathcal{T})$
([unified mass formula](#prop:unified-curvature-rank-mass-formula))
is the Plancherel-weighted projection onto a specific
curvature-rank stratum $\Lambda_k$.  No prefactor is a free fit:
each is the unique scalar making the depth-$k$ stratum reproduce
its Bethe--Weizsäcker counterpart.*

**Coefficient-to-stratum mapping.**

See [Table 1](#tbl:mass-tower-coefficient-stratification-table1-data).

*Each row reads: the Bethe--Weizsäcker coefficient is the
Plancherel-weighted Frobenius integral over partitions $\lambda$
in the indicated stratum $\Lambda_k$.  By
([Plancherel boundedness](#prop:plancherel-weight-boundedness)) the
sum $\sum_{\lambda \in \Lambda_k} w_\lambda \leq 1$, so each
coefficient is automatically bounded — no truncation, no
fitting.*
<!-- FILE_END: mass-tower-coefficient-stratification.md -->

<!-- FILE_START: flavor-dressing-functor.md -->
**Definition.**
*The **flavor dressing functor** is the categorical assignment
of a dressed-mass scale to each quark flavor:*

$$
  \mu \colon \mathbf{Flavor} \longrightarrow \mathbb{R}_{>0},
  \qquad
  q \in \{\mathfrak{u}, \mathfrak{d}, \mathfrak{s}, \mathfrak{c}, \mathfrak{b}, \mathfrak{t}\}
  \longmapsto
  \mu_q \in \mathbb{R}_{>0}.
$$

*Here $\mathbf{Flavor}$ is the discrete category whose objects are
the six quark flavors and whose only morphisms are identities; the
target $\mathbb{R}_{>0}$ is the positive real line carrying the
canonical commutative-monoid structure under multiplication.*

## Scope of this paper

The current paper formalises the functor on the doublet
$\{\mathfrak{u}, \mathfrak{d}\}$ only. Heavy flavors
$\{\mathfrak{s}, \mathfrak{c}, \mathfrak{b}, \mathfrak{t}\}$ are
included in the categorical signature for forward compatibility
but their individual $\mu_q$ values are open
(no derivation is committed in this revision).

## Categorical role

The functor is the chapter-level bridge between two layers that
already live in this chapter:

1. **Substrate side** — the splitting $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$
 is determined by the substrate flavor split
 ([`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md))
 modulo the Skein factor of
 [`lem:pair-skein-mass-formula`](../observations/pair-skein-mass-formula.md);
 see [`prop:flavor-dressed-mass-from-substrate-split`](flavor-dressed-mass-from-substrate-split.md).

2. **Bounds side** — the splitting respects the categorical bound
 coming from the substrate factors
 $\hbar_q$, $h_q$, $[2]_q$; see
 [`thm:flavor-mass-splitting-bound`](flavor-mass-splitting-bound.md).

## Composition with other functors

The flavor dressing functor composes with the
[shell dressing morphism](#def:dressed-particle) at the
hadron / atom level:

```tex
\begin{tikzcd}
  \mathbf{Flavor}
  \arrow[r, "\mu"] \arrow[d, "\Phi"]
  & \mathbb{R}_{>0}
  \\
  \mathbf{Hadron}
  \arrow[r, "m_{\mathrm{bare}}"']
  & \mathbb{R}_{>0}
  \arrow[u, "P_{\mathrm{bare}} \mapsto P_{\mathrm{dressed}}"']
\end{tikzcd}
```

where $\Phi$ is the quark-content functor (e.g. $\Phi(\mathfrak{p})
= \mathfrak{u}\mathfrak{u}\mathfrak{d}$, $\Phi(\mathfrak{n}) =
\mathfrak{u}\mathfrak{d}\mathfrak{d}$) and the right-vertical
arrow lifts a bare hadron mass to its electron-dressed atomic mass.

## Functor versus function

The discrete-category framing makes the dressing assignment
**accordingly** compatible with the chapter's other categorical
constructions (Markov trace, Hoefsmit functor, Wedderburn block
decomposition). In particular, sums over flavors that appear in
hadronic mass formulas (e.g. $\sum_q n_q \cdot \mu_q$ for quark
content $\{n_q\}$) are then natural transformations of functors,
not ad-hoc weighted sums.

## Lean encoding

The Lean side carries the functor as a typeclass
`FlavorDressingFunctor` with field `μ : Flavor → ℝ` and positivity
hypothesis `μ_pos : ∀ q, 0 < μ q`. Instances at specific values of
the substrate parameter (e.g. $q = q_0$) are provided by sibling
files; the canonical instance at $q_0$ uses the derivation in
[`prop:flavor-dressed-mass-from-substrate-split`](flavor-dressed-mass-from-substrate-split.md)
plus a chosen value of the nucleon-mass average $M_N$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: flavor-dressing-functor.md -->

<!-- FILE_START: staircase-ew-residual.md -->
**Conjecture (staircase EW-residual).**
*Let $\rho_k = (k, k-1, \ldots, 1)$ be the
[staircase partition](#def:staircase-partition), let
$V_{\rho_k}$ be the Specht module of $H_{n_k}(q)$ at this shape
(realised in
[Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)),
and let
$\beta_{\mathrm{EW}}\,\bowtie_K^{\mathrm{minimal}} \in H_{n_k}(q)$
be the canonical electroweak braid word.  Then for every
$k \geq 2$, the matrix image*

$$
  \rho_{\rho_k}\!\bigl(\beta_{\mathrm{EW}}\,
                       \bowtie_K^{\mathrm{minimal}}\bigr)
  \;\in\;
  \mathrm{Mat}_{f^{\rho_k} \times f^{\rho_k}}\!\bigl(\mathbb Q(q)\bigr)
$$

*has two nonzero eigenvalues whose pairwise ratio equals*

$$
  q^{1 / h_{\mathrm{corner}}(\rho_k)}
  \;=\; q^{1 / (2k - 1)},
$$

*where the corner-hook identification
$h_{\mathrm{corner}}(\rho_k) = 2k - 1$ is
[Lemma `lem:staircase-corner-hook`](#lem:staircase-corner-hook).*

**Empirical content.**

* $k = 3$ (dim $f^{\rho_3} = 16$): the residual factor $q^{1/5}$
  closes the $2.19\%$ cot $\theta_W$ discrepancy from the bare
  $\max^{+}/\!\operatorname{2nd-max}^{+}$ reading down to
  $0.13\%$ — see
  the canonical formalism,
  witness
  [`close-321-weinberg-gap.witness.json`](https://github.com/litlfred/qou/blob/main/computations/close-321-weinberg-gap.witness.json),
  audit
  [`docs/audits/-close-321-weinberg-gap.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-close-321-weinberg-gap.md).
* $k = 4$ (dim $f^{\rho_4} = 768$): the top eigenvalue is
  *degenerate* (multiplicity $\geq 2$, ratio $1.0$) because every
  Hecke generator has $\det \rho_{\rho_4}(\sigma_i) = +1$ on the
  pure-$\mathrm{SL}$ stratum; the conjecture is verified instead
  via a **pairwise** ratio
  $e[254]/e[188] = 1.01357 \approx q^{1/7} = 1.01502$
  (relative error $0.14\%$) — see
  the canonical formalism,
  audit
  [`docs/audits/-staircase-ew-residual-conjecture.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-staircase-ew-residual-conjecture.md).
* $k = 2$ (dim $f^{\rho_2} = 2$): currently untestable — the
  $\beta_{\mathrm{EW}}$ word at $n = 3$ collapses to a length-$0$
  word under the construction, leaving no matrix multiplication
  to inspect.

**Lean status (per
[`AGENTS.md` §3b-cond](https://github.com/litlfred/qou/blob/main/AGENTS.md)).**
The conjecture is axiomatised as a **hypothesis-only** Lean `class`
`QOU.StaircaseCornerHook.StaircaseEWResidual` (no global instance —
per §3b-cond, supplying one would require a `sorry`; the conjecture
*is* the existence of an instance
`StaircaseEWResidual q (canonicalScale q)`).  The predicate
`StaircaseEWSpectralContent q (scale k) k` is stated explicitly
in terms of
`HoefsmitRepresentation.HasEigenvalueRatio` applied to
`HoefsmitRepresentation.wordImage (betaEWWord (staircaseStrands k))`,
so downstream Lean theorems may take
`[StaircaseEWResidual q scale]` as an instance hypothesis and
remain rigorous-conditional results: their Lean proofs are fully
verified modulo this one named conjectural input.
<!-- FILE_END: staircase-ew-residual.md -->

