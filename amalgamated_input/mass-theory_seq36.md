<!-- FILE_START: plancherel-knot-factor-mass-tower-intro.md -->
We now identify the knot factors and enumerate the Wedderburn channels. This closes the mass-tower arc.

We previously established the Plancherel-alpha spectral foundations. We now apply those tools to specific knot classes. We evaluate the knot factor for amphicheiral knots, Borromean composites, and shell-closed configurations. Finally, we formulate the Pauli factor via Wedderburn decomposition and stratify the mass-tower coefficients.
<!-- FILE_END: plancherel-knot-factor-mass-tower-intro.md -->

<!-- FILE_START: knot-factor-spectral-derivation.md -->
*Let $\mathcal{K}$ be a knot with braid representative $\beta_\mathcal{K} \in B_n$ and mirror $\beta_\mathcal{K}^*$. We work over $A = H_n(R, q)$. The knot factor $a_\mathcal{K}$ in the unified mass formula is the normalised chirality Gram pairing:*

$$
  a_\mathcal{K} \;=\;
  \frac{G_{\beta_\mathcal{K},\, \beta_\mathcal{K}^*}}
       {G_{\mathbf{1},\, \mathbf{1}}}
  \;=\;
  \sum_{\lambda \,\vdash\, n}
    w_\lambda \,
    \frac{\chi_\lambda(\beta_\mathcal{K})\, \chi_\lambda(\beta_\mathcal{K}^*)}
         {\chi_\lambda(\mathbf{1})^2}.
$$

*The Plancherel weights $w_\lambda = \dim_q^2 V_\lambda / [n]_q!$ sum to $1$. The identity holds exactly in $R$.*
<!-- FILE_END: knot-factor-spectral-derivation.md -->

<!-- FILE_START: knot-factor-amphicheiral.md -->
*Let $\mathcal{K}$ be Markov-amphicheiral. Its mirror braid representative $\beta_\mathcal{K}^*$ is conjugate to $\beta_\mathcal{K}$ in $H_n(R, q)$. There exists $w \in H_n(R, q)^{\times}$ such that:*

$$
  \beta_\mathcal{K}^* \;=\; w\,\beta_\mathcal{K}\, w^{-1}.
$$

*The knot factor is therefore a sum of positive squares weighted by Plancherel weights:*

$$
  a_\mathcal{K} \;=\;
  \sum_{\lambda \vdash n}\, w_\lambda\,
  \frac{\chi_\lambda(\beta_\mathcal{K})^2}{\chi_\lambda(\mathbf{1})^2}.
$$
<!-- FILE_END: knot-factor-amphicheiral.md -->

<!-- FILE_START: knot-factor-borromean-composite.md -->
*Consider a Brunnian $k$-component composite, where every $(k{-}1)$-component sublink is trivial. Its central-idempotent expansion equals the $k$-fold independent product of figure-eight pairings. The knot factor is:*

$$
  a_{\mathrm{Bor}_k} \;=\; (a_{4_1})^k \;=\; (1 - h^2)^k.
$$

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring. Only their archimedean realisation is specialised here.
<!-- FILE_END: knot-factor-borromean-composite.md -->

<!-- FILE_START: knot-factor-shell-closed.md -->
*For $Z = N$ even-even nuclei, the Markov chain on the three $H_3(R, q)$ partitions returns to equilibrium after every inter-nucleon crossing. The pp and nn character shifts cancel exactly. In the spectral language, $\beta_\mathcal{K} \cdot \beta_\mathcal{K}^*$ projects entirely onto the trivial idempotent $e_{(n)}$:*

$$
  \chi_\lambda(\beta_\mathcal{K} \cdot \beta_\mathcal{K}^*)
  \;=\;
  \delta_{\lambda, (n)} \cdot \chi_{(n)}(\mathbf{1})^2.
$$

*This forces the knot factor to unity:*

$$
  a_\mathcal{K} \;=\; 1.
$$

*The result is an exact algebraic cancellation.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring. Only their archimedean realisation is specialised here.
<!-- FILE_END: knot-factor-shell-closed.md -->

<!-- FILE_START: knot-factor-spectral-summary.md -->
These corollaries replace empirical per-isotope fits with derived expressions:

| Nucleus | Knot family | Empirical $a$ | Spectral derivation |
|---|---|---|---|
| ${}^3\mathrm{H},\ {}^3\mathrm{He}$ | $4_1$ figure-eight | $1 - h^2$ | Amphicheiral self-pairing on $e_{(1^n)}$ |
| ${}^4\mathrm{He}$ | Borromean-$2$ | $(1 - h^2)^2$ | Independent product of two figure-eight pairings |
| ${}^{12}\mathrm{C},\ {}^{40}\mathrm{Ca},\ {}^{56}\mathrm{Fe},\ {}^{208}\mathrm{Pb}$ | Shell-closed | $1$ | Markov-chain equilibrium $\Rightarrow$ projection onto $e_{(n)}$ alone |
| Odd-odd $Z = N$ (${}^6\mathrm{Li},\ {}^{14}\mathrm{N}$) | Asymmetric | $1 - \delta_{\mathrm{Wigner}}$ | Last-neutron breaking $\Rightarrow$ residual on standard irrep |

**Practical computation.**
The Hoefsmit pipeline produces $\chi_\lambda(\beta_\mathcal{K})$ for any braid word. The knot factor is then a single q-deformed Wedderburn-weighted sum. It is bounded by Wedderburn completeness without truncation. Implementation replaces per-isotope hand-fits with direct evaluation of the spectral form.
<!-- FILE_END: knot-factor-spectral-summary.md -->

<!-- FILE_START: pauli-factor-wedderburn.md -->
*Working over $A = H_n(R, q)$, the Pauli statistical weight in nuclear $Q$-value formulas is the ratio of Wedderburn-block traces:*

$$
  F_{\mathrm{Pauli}}(\beta_\mathcal{K})
  \;=\;
  \frac{\int_{A_{(1^n)}}\!\rho(\beta_\mathcal{K})}
       {\int_{A_{(n)}}\!\rho(\beta_\mathcal{K})}
  \;=\;
  \frac{\chi_{(1^n)}(\beta_\mathcal{K}) \cdot \dim_q V_{(1^n)}}
       {\chi_{(n)}(\beta_\mathcal{K}) \cdot \dim_q V_{(n)}}
  \,\in\, R.
$$

*This is the alternating-block trace divided by the symmetric-block trace. $F_{\mathrm{Pauli}}$ vanishes when $\beta_\mathcal{K}$ has no alternating-block content (bosonic). It is a unit when $\beta_\mathcal{K}$ saturates the alternating block (fully fermionic).*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring. Only their archimedean realisation is specialised here.
<!-- FILE_END: pauli-factor-wedderburn.md -->

<!-- FILE_START: mass-tower-coefficient-stratification.md -->
*Working over $A = H_n(R, q)$, every prefactor $\alpha_k$ in the unified mass formula $\mathfrak{m}_{q, \mathcal{K}}(\mathcal{T}) = \sum_{k = 0}^{n-1} \alpha_k \cdot \mathfrak{m}^{(k)}_{q, \mathcal{K}}(\mathcal{T})$ is the Plancherel-weighted projection onto a specific curvature-rank stratum $\Lambda_k$. No prefactor is a free fit. Each is the unique scalar making the depth-$k$ stratum reproduce its Bethe--Weizsäcker counterpart.*

**Coefficient-to-stratum mapping.**

See [Table 1](#tbl:mass-tower-coefficient-stratification-table1-data).

*Each row reads: the Bethe--Weizsäcker coefficient is the Plancherel-weighted Frobenius integral over partitions $\lambda$ in the indicated stratum $\Lambda_k$. The sum $\sum_{\lambda \in \Lambda_k} w_\lambda \leq 1$. Thus each coefficient is automatically bounded. We require neither truncation nor fitting.*
<!-- FILE_END: mass-tower-coefficient-stratification.md -->

<!-- FILE_START: flavor-dressing-functor.md -->
**Definition.**
*The **flavor dressing functor** assigns a dressed-mass scale to each quark flavor:*

$$
  \mu \colon \mathbf{Flavor} \longrightarrow \mathbb{R}_{>0},
  \qquad
  q \in \{\mathfrak{u}, \mathfrak{d}, \mathfrak{s}, \mathfrak{c}, \mathfrak{b}, \mathfrak{t}\}
  \longmapsto
  \mu_q \in \mathbb{R}_{>0}.
$$

*The discrete category $\mathbf{Flavor}$ contains the six quark flavors and identity morphisms. The target $\mathbb{R}_{>0}$ is the positive real line with canonical commutative-monoid structure under multiplication.*

We restrict our focus to the doublet $\{\mathfrak{u}, \mathfrak{d}\}$. We include heavy flavors for forward compatibility, but leave their individual $\mu_q$ values open.

The functor bridges two categorical layers:

1. **Substrate side.** The splitting $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ is determined by the substrate flavor split modulo the pair-skein factor.
2. **Bounds side.** The splitting respects the categorical bound enforced by the substrate factors $\hbar_q$, $h_q$, and $[2]_q$.

The flavor dressing functor composes with the shell dressing morphism at the hadron and atom levels:

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

Here $\Phi$ is the quark-content functor. The right-vertical arrow lifts a bare hadron mass to its electron-dressed atomic mass.

The discrete-category framing ensures compatibility with other categorical constructions. Sums over flavors in hadronic mass formulas become natural transformations of functors rather than ad-hoc weighted sums.

We encode the functor as a `FlavorDressingFunctor` typeclass in Lean. It requires a field `μ : Flavor → ℝ` and a positivity hypothesis `μ_pos : ∀ q, 0 < μ q`. Instances at specific substrate parameters are provided in sibling files.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring. Only their archimedean realisation is specialised here.
<!-- FILE_END: flavor-dressing-functor.md -->

<!-- FILE_START: staircase-ew-residual.md -->
**Conjecture (staircase EW-residual).**
*Let $\rho_k = (k, k-1, \ldots, 1)$ be the staircase partition. Let $V_{\rho_k}$ be the corresponding Specht module of $H_{n_k}(q)$. Let $\beta_{\mathrm{EW}}\,\bowtie_K^{\mathrm{minimal}} \in H_{n_k}(q)$ be the canonical electroweak braid word. For every $k \geq 2$, the matrix image*

$$
  \rho_{\rho_k}\!\bigl(\beta_{\mathrm{EW}}\,
                       \bowtie_K^{\mathrm{minimal}}\bigr)
  \;\in\;
  \mathrm{Mat}_{f^{\rho_k} \times f^{\rho_k}}\!\bigl(\mathbb Q(q)\bigr)
$$

*has two nonzero eigenvalues whose pairwise ratio equals*

$$
  q^{1 / h_{\mathrm{corner}}(\rho_k)}
  \;=\; q^{1 / (2k - 1)}.
$$

*The corner-hook length $h_{\mathrm{corner}}(\rho_k)$ is $2k - 1$.*

**Empirical content.**

* For $k = 3$, the residual factor $q^{1/5}$ closes the cot $\theta_W$ discrepancy from $2.19\%$ to $0.13\%$.
* For $k = 4$, the top eigenvalue is degenerate. We verify the conjecture via a pairwise ratio $e[254]/e[188] \approx q^{1/7}$ with $0.14\%$ relative error.
* For $k = 2$, the word collapses to length $0$. This leaves no matrix multiplication to inspect and renders the case untestable.

**Lean status.** We axiomatise the conjecture as a hypothesis-only `class`. We state the spectral content explicitly using `HoefsmitRepresentation.HasEigenvalueRatio`. Downstream Lean theorems take this class as an instance hypothesis and remain rigorous-conditional results.
<!-- FILE_END: staircase-ew-residual.md -->

