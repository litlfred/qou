In the unified six-term formula ([unified knot mass](#thm:knot-mass-formula-unified)), $|\mathrm{tr}_M(\rho(\beta))|$ forms **Term 1** ($E_\infty^{0,*}$, vortex-specific). The brane tower $\sum \Phi_q(z_i)$ supplies **Terms 2–3** ($E_\infty^{1,*}$ and $E_\infty^{2,*}$). In the archimedean realisation, these three terms together evaluate to $\mathrm{Vol}(K)/\hbar_q^2$ ([topological decomposition](#thm:topological-mass)). Terms 4–6 (Frobenius co-Casimir, chirality, jet prefix) form separate structural pieces handled elsewhere. This conjecture concerns only the tower piece.

The **Hecke mass element** $\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$ ([Hecke mass element](#def:hecke-mass-element)) is defined categorically: it is the fibre functor image of the mass integrand $(\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho$. Its Markov trace gives the full categorical mass ([mass via Markov trace](#prop:hecke-mass-trace)). The open problem consists of computing $\Phi_{\mathrm{mass}}(\beta)$ explicitly—expressing its NF decomposition in the basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$ for specific braid words.

## Scope: convenience target, not load-bearing

The scope of this conjecture is as follows:

- **Load-bearing claim** (already proved, not part of this conjecture): The categorical mass equals the infinite-series sum

  $$
    \mathfrak{m}(\varrho)
    \;=\;
    \bigl|\mathrm{tr}_M(\rho(\beta))\bigr|
    \;+\; \sum_{n \ge 0}\!\Bigl(
      \textstyle\sum_i \Phi_q(|\hat V_i^{(n)}|)
      + z^2 \sum_{(i,j)} \Phi_q(|\hat V_i^{(n)} \hat V_j^{(n)}|)
    \Bigr).
  $$

  This follows from [the unified knot mass formula](#thm:knot-mass-formula-unified) and [the mass endomorphism tower](#prop:mass-endomorphism-tower). It does not depend on the closed-form conjecture below. Every algebraic downstream result that relies on the mass tower routes through this infinite series.

- **Convenience target** (the conjectural content here): The conjecture posits the existence of a single element $\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$—a finite-rank Hecke element—whose Markov trace gives the full categorical mass. This element would collapse the infinite series into a closed-form evaluation. It serves symbolic computation but is not required for the structural derivations in this paper.

If this conjecture fails (no closed-form $\Phi_{\mathrm{mass}}$ exists in finite-rank $H_n(R, q)$), the algebraic mass formula remains valid as the infinite series. Compute scripts attempting to materialise $\Phi_{\mathrm{mass}}$ as a single element must truncate explicitly. Scripts that evaluate the infinite sum at $q_0$ (the dominant case) remain unaffected.

The scope of a failure is therefore exactly this: the tower formula remains correct as an infinite series, and the closed form is a convenience.

## Statement

**Conjecture (explicit mass endomorphism).** *The Hecke mass element $\Phi_{\mathrm{mass}}(\beta)$ ([Hecke mass element](#def:hecke-mass-element)) admits a closed-form NF decomposition in $H_n(R, q)$ expressible in terms of the braid word $\beta$, the substrate parameter $q$, and the quantum dilogarithm $\Phi_q$. Specifically, the transient component satisfies:*

$$
  \mathrm{tr}_M\!\bigl(\Phi^{\mathrm{trans}}(\beta)\bigr)
  =
  \sum_{i=1}^{N} \Phi_q(z_i)
  =
  \frac{\mathrm{Vol}(K_\beta)}{\hbar_q^2}
  -
  \bigl|\mathrm{tr}_M\!\bigl(\rho(\beta)\bigr)\bigr|,
$$

*where the spectral coordinates $z_i$ of the blow-up centres are determined by the braid word and the Briggs--Klein chart.*

## Tower convergence

The electron mass $\mathrm{Li}_2(q^{-2})/\hbar_q^2$ decomposes as a sum over brane levels $n = 1, 2, \ldots$, with level $n$ contributing $q^{-2n}/n^2$ to $\mathrm{Li}_2$:

| Levels | Fraction of $\mathrm{Li}_2(q^{-2})$ |
|:---:|:---:|
| $N = 1$ | $73.9\%$ |
| $N = 3$ | $94.3\%$ |
| $N = 10$ | $99.75\%$ |
| $N = 20$ | $99.99\%$ |

The tower converges in $\sim 20$ terms. This rate is consistent with $t_P = 1/\hbar_q \approx 10$ Reeb operations per Planck time. The first brane level alone provides $74\%$ of the electron mass; the remaining $26\%$ comes from higher jet prolongations.

## Established results

**Step 1 (Categorical $\to$ Markov, proved).** Single-level mass satisfies $\mathfrak{m}(\varrho)|_{\text{single level}} = |\mathrm{tr}_M(\rho(\beta))|$. This is [categorical mass as Markov trace](#prop:categorical-mass-markov). The Nakayama automorphism is $S^2 = \mathrm{id}$, so the mass reduces to the Markov trace of the braid word.

**Step 2 (Tower sum $\to$ Vol, archimedean).** Full-tower mass satisfies $\mathfrak{m}(\varrho)|_{\text{full tower}} = \mathrm{Vol}(K)/\hbar_q^2$. This is the [archimedean mass formula](#prop:topological-mass-formula). The descended trace gives $\mathrm{Vol}(K)$, each transient trace gives $\Phi_q(z_i)$, and their sum is $\mathrm{Vol}(K)/\hbar_q^2$.

**Step 3 (Markov trace $\neq$ Vol, the gap).** The Jones--Markov trace $\mathrm{tr}_M(\rho(\beta))$ is the Jones polynomial $J(K; q)$—a Laurent polynomial in $q^{1/2}$. The hyperbolic volume $\mathrm{Vol}(K)$ is a transcendental number. They are different knot invariants: $J(\text{trefoil}; q) = -q^{-4} + q^{-3} + q^{-1}$ while $\mathrm{Vol}(\text{trefoil}) = 0$.

The bridge between them is the **Volume Conjecture** \cite{kashaev1997, murakami-murakami2001}:

$$
  \lim_{N \to \infty}
  \frac{2\pi}{N}
  \log |J_N(K; e^{2\pi i/N})|
  =
  \mathrm{Vol}(S^3 \setminus K),
$$

where $J_N$ is the $N$-colored Jones polynomial. This limit involves evaluating at roots of unity ($q = e^{2\pi i/N}$, not generic $q$), the $N$-dimensional representation (not the fundamental), and an asymptotic limit ($N \to \infty$). Each step departs from the Hecke algebra at generic $q$.

The Habiro ring ([Habiro ring](#def:habiro-ring)) partially closes this gap. The colored Jones polynomials for all $N$ coexist as a single element of $\widehat{\mathbb{Z}[q]}$. The algebraic quantum volume ([algebraic quantum volume](#def:algebraic-quantum-volume)) $\mathrm{Vol}_q(\beta) = \prod \hat{V}_i$ embeds into $\widehat{\mathbb{Z}[q^{1/2}]}$. Its evaluations at roots of unity collectively encode the hyperbolic volume via the Volume Conjecture. The mass at $q_0$ is a different specialisation of the same Habiro element, evaluated directly at the substrate parameter rather than passing through roots of unity.

## Encoding requirements for $\Phi_{\mathrm{mass}}$

The brane tower $\{A_n\}$ provides the categorical version of $N \to \infty$. Each brane level $n$ contributes a transient trace $\Phi_q(z_n)$, and the full mass sums over all levels. A mass endomorphism $\Phi_{\mathrm{mass}}$ must encode this sum as a single element of $H_n(R, q)$.

The quantum dilogarithm $\Phi_q(z) = \prod_{k=1}^{\infty}(1 - q^{-k}z)^{-1}$ is an infinite product. It is not a finite element of $H_n(R, q)$ for any $n$. However, the brane tower truncates at finite $N$ (determined by the knot crossing number), so the relevant sum is finite. The open question is whether this finite sum admits a closed-form expression in $H_n(R, q)$.

**Habiro-ring home for the tower limit.** *Even when the brane tower does not truncate finitely, the partial sums*

$$
  \Phi_{\mathrm{mass}}^{(N)}(\beta)
  \;:=\;
  \sum_{i=1}^{N} \Phi_q(z_i)
$$

*form a Cauchy sequence in the $(q;q)_n$-adic topology on $\widehat{\mathbb{Z}[q]}$ ([Habiro ring](#def:habiro-ring)). Each factor $\Phi_q(z_i)$ has cyclotomic-denominator structure (the $[k]_q$ in $\Phi_q$ are cyclotomic), making successive partial sums agree modulo $((q;q)_n)$ for $n$ growing with $N$. Therefore the limit*

$$
  \Phi_{\mathrm{mass}}^{(\infty)}(\beta)
  \;\in\;\widehat{\mathbb{Z}[q]}
$$

*exists as an element of the Habiro completion. It is well-defined purely algebraically, without analytic convergence. This limit object is the motive of the mass: it carries the combinatorial data mapping to $\mathrm{Vol}(K)/\hbar_q^2$ only when the archimedean realization [$\rho_\infty$](#def:archimedean-realization-functor) of the [motivic substrate](#def:motivic-substrate) is applied at $q_0 \in \mathbb{R}$. The non-archimedean realizations $\{\rho_p\}$ recover the colored-Jones data via cyclotomic projection $\widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q]/\Phi_N(q)$ without any complex-analytic limit.*

The conjecture regarding a "closed-form expression in $H_n(R, q)$" asks a question in the finite-rank Hecke algebra. The $N \to \infty$ tower limit asks a question in the Habiro completion $\widehat{\mathbb{Z}[q]}$. Both are algebraic.

**Two distinct convergence problems.** *The Habiro completion resolves the $N \to \infty$ tower-limit problem in the $((q;q)_n)$-adic topology on $q$. This is well-defined. At $q_0 \approx 1.11$ (real, $|q| > 1$, outside the natural boundary $S^1$), the Habiro evaluation agrees with the analytic infinite product.*

*A separate convergence problem affects the brane tower numerically. For the per-generator volumes $|\hat{V}_i|$ of low isotopes, all values sit at $|\hat{V}_i| \in [0.85, 1.0]$—at the boundary of the $z$-radius of convergence of $\Phi_q(z) = \prod (1 - q^{-k} z)^{-1}$. Numerically $\Phi_q(0.989) \approx 6.7 \times 10^5$ and $\Phi_q(1) \approx 9 \times 10^5$. The Habiro framework addresses completion in $q$, not in $z$. It does not regularize the $|\hat{V}|\approx 1$ behaviour.*

*Two partial mitigations are documented, though neither universally closes the gap:*

1. *The [$z$-Habiro completion](#def:z-habiro-ring)—analogous to the $q$-Habiro completion but in the $z$-variable. The cyclotomic denominator structure in $z$, parallel to $(q; q)_n$ in $q$, is*

  $$
      P_n(q, z) \;=\; \prod_{k=1}^{n} \bigl(1 - q^{-k} z\bigr)
      \;=\; (z q^{-1};\, q^{-1})_n,
  $$

  *whose zero locus is exactly the first $n$ poles of $\Phi_q$. The completion $\widehat{\mathbb{Z}[q^{\pm 1}][z]}_z = \varprojlim_n \mathbb{Z}[q^{\pm 1}][z] / (P_n(q, z))$ has cyclotomic projections $\pi_n^{(z)}$ acting as structural truncations at depth $n$, replacing Yekutieli's ad-hoc cutoff with a quotient by a structural ideal. The [conjecture that the brane tower lives in this ring](#conj:brane-tower-z-habiro) has two independent claims: (a) the algebraic Cauchy-limit (the partial sums converge in the $z$-Habiro topology), and (b) the existence of a canonical level-selection rule $n_\star(\mathfrak{H})$ derivable from substrate data.*

2. *Magic-shell structural term. Add a separate $\Delta_{\text{shell}}(Z, N)$ contribution to the binding formula distinguishing closed-shell stabilization from the brane-tower transient.*

3. *Markov-trace audit on ${}^3\mathrm{He}$. Verify $|\mathrm{tr}_M(\beta_{{}^3\mathrm{He}})|$ at $q_0$ against the canonical reducer to confirm the structural gap is real and not a Markov-trace mis-count.*

The brane tower contribution remains not computable in closed form for $|\hat{V}|\approx 1$ under the original conjecture. The descended Markov trace plus Frobenius co-Casimir alone empirically reproduces the binding within $\sim 30\%$ for low isotopes.

## Descended vs transient mass (computed)

The Hecke mass element splits as $\Phi_{\mathrm{mass}} = \Phi^{\mathrm{desc}} + \Phi^{\mathrm{trans}}$ ([Hecke mass element](#def:hecke-mass-element)). At $q_0$, the transient (tower) component dominates overwhelmingly:

| Particle | $\mathrm{tr}_M(\Phi^{\mathrm{desc}})$ | $\mathrm{tr}_M(\Phi^{\mathrm{trans}})$ | Ratio trans/desc |
|:---:|:---:|:---:|:---:|
| $e^-$ (trefoil) | $0.551$ | $111.86$ | $203\times$ |
| $4_1$ (figure-eight) | $0.182$ | $207.40$ | $1137\times$ |

The single-level (descended) Markov trace contributes less than $0.5\%$ of the total mass. The mass is almost entirely a brane tower effect—the accumulated quantum dilogarithm across exceptional divisors.

## Computational verification (single-level)

Three single-level approaches were evaluated for the proton ($uud$) and neutron ($udd$) Borromean braids:

| Method | Proton | Neutron | Ratio $n/p$ | CODATA |
|:---|:---:|:---:|:---:|:---:|
| $\lvert\mathrm{tr}_M(\beta)\rvert$ | $1.165$ | $0.911$ | $0.782$ | $1.001$ |
| $\Phi_q/\hbar_q^2$ | $-89.8$ | $-125.2$ | $1.395$ | $1.001$ |
| GS energy | $0.852$ | $1.184$ | $1.390$ | $1.001$ |

None of these single-level computations reproduce the neutron-to-proton mass ratio. The quantum dilogarithm $\Phi_q = \sum \log \lvert\hat{V}_i\rvert$ gives the correct binding energy differences between nuclei (Q-values at Level 0), but not single-nucleon absolute masses.

The proton mass $938.272$ MeV in this paper derives from the pair Skein formula $m_p = \mathcal{S}_{uu} + 2\mathcal{S}_{ud}$. This requires the dressed quark mass $\mu_\mathfrak{u} \approx 311$ MeV as input, calibrated from CODATA $m_p$. The structural content (pair formula, splitting isolation, binding energy) is categorically derived; the absolute scale is calibrated — consistent with absolute mass in MeV not being a framework prediction, the predictive content residing in the dimensionless ratios, with $m_e$ (CAL-1) setting the MeV scale by fiat.

## Candidate structures

**(a) Figure-eight $4_1$ as Higgs coupling.** The figure-eight knot $4_1 = (\sigma_0\sigma_1^{-1})^2$ is the gluon unit squared. Its NF is $h^2\gamma + h^3\sigma_0 - h\sigma_1 - h^2 L_+ + L_-$ with zero electron content. As a mass operator, the pairing $\mathrm{tr}_M(e^- \cdot 4_1) = hz^2 + z = \mathrm{tr}_M(e^-)$ does not produce the correct mass ratios. The figure-eight encodes the mass mechanism (amphichiral, hyperbolic, $\mathrm{Vol} = 2.0299$) but acts as the identity on the trefoil in $H_3(R, q)$.

**(b) Tower-accumulated operator.** The mass endomorphism may equal the product $\Phi_{\mathrm{mass}} = \prod_{n=0}^{N} (1 + \Phi_q(z_n))$ of Hecke elements at each brane level, composed via the comultiplication. This forms an element of $H_n(R, q)$ growing with $N$—a categorically defined object, but not a fixed element independent of the knot.

**(c) Spectral decomposition via RJ weights.** The Rosso--Jones inner product ([RJ canonical inner product](#prop:rj-canonical-inner-product)) decomposes the Markov trace over irreps: $\mathrm{tr}_M = \sum_\lambda d_\lambda(q) \cdot \mathrm{tr}_\lambda$. A mass endomorphism could reweight the irreps: $\Phi_{\mathrm{mass}} = \sum_\lambda w_\lambda(q) \cdot e_\lambda$, where $w_\lambda$ encodes the volume information. The Volume Conjecture then states that the weights $w_\lambda$ grow exponentially with $\lambda$, recovering $\mathrm{Vol}(K)$ in the limit.

## Relation to knot operator selection

The multi-channel decomposition ([knot operator selection](#prop:knot-operator-selection)) showed that interactions decompose over irreps of $H_n(R, q)$ weighted by quantum dimensions. The mass endomorphism conjecture asserts that mass is a specific reweighting of the same decomposition—using weights that produce $\mathrm{Vol}(K)$ instead of $J(K; q)$.

If the conjecture holds:
- The operator selection framework (Frobenius dual, Gram matrix, demand/supply) applies to mass, with $\Phi_{\mathrm{mass}}$ replacing the identity.
- The Higgs field provides the dominant contribution to $\Phi_{\mathrm{mass}}$ for leptons (it supplies the volume that the trefoil lacks).
- The graviton is the residual of $\Phi_{\mathrm{mass}}$ after subtracting the Higgs contribution.
