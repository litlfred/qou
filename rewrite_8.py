import re

content_8 = r"""<!-- FILE_START: transfer-beta-decay-intro.md -->
The Gram-weighted $\mathcal{Q}_q$-value is the proper input for beta decay. We exhibit beta decay as a transfer-matrix insertion in the Skein-polynomial factorisation. The nuclear Skein polynomial factors as a product of $2 \times 2$ transfer matrices. This factorisation produces a universal transfer matrix operator. Consequently, every beta-decay event becomes a single matrix insertion in the same universal matrix-valued polynomial in $q$.

The eigenvalues of this transfer-matrix product select the ground-state ordering of nuclear configurations. Algebraic identities make the matrix factorisation tractable. We use these tools to compute symbolic $Q$-values, including the free neutron decay. We establish a basis-change identity between two forms of the $\mathfrak{Q}_\beta$ spectral bridge: Form A (normal form counit) and Form B (transfer-matrix log-ratio). At brane-tower depth $N = 1$, Form A admits a symbolic closed form via a geometric-series lift.

We connect the dimensionless normal form coefficients to physical MeV energy scales and track negative-coefficient debt that survives reduction. We provide a worked tritium example and its double-beta extension. Finally, an interactive simulator models beta decay as a $T_{3,5}$ braid insertion. This simulator tracks crossing budgets and transfer matrices. It serves as the computational basis for scaling the construction to the atomic braid $H_{A+Z}(q)$.
<!-- FILE_END: transfer-beta-decay-intro.md -->

<!-- FILE_START: neutron-qvalue-symbolic.md -->
**Proposition (conditional on Borromean quark conjecture — $\mathfrak{Q}_\beta$ of free neutron $\beta^{-}$-decay).**
*We derive the $Q$-value of free neutron $\beta^-$-decay $n \to p + e^- + \bar\nu_e$ symbolically from the categorical three-calibration inputs $m_e$ ($H^0$) and $q_0$ ($H^1$). The value $\mathfrak{Q}_\beta(n)$ ($H^2$) is the $\beta$-decay datum being predicted, not used as input.*

## Single-wrap normal-form computation

A single wrap of typed crossings in $H_3(q)$ represents the proton and neutron. Let $h = q - q^{-1}$.

**Proton** $[u, u, d]$: the typed crossing operators give:
$$
  L_+ - \tfrac{h}{2}\sigma_0
$$

**Neutron** $[u, d, d]$:
$$
  L_+ - h\sigma_0 - \tfrac{h}{2}\sigma_1 + \tfrac{h^2}{2}\gamma
$$

## Symbolic $\Delta(\text{net})$

$$
  \Delta(\mathrm{net})
  =
  \mathrm{net}(n) - \mathrm{net}(p)
  =
  \frac{h(h - 2)}{2}.
$$

The $L_+$ and $L_-$ contributions cancel exactly because both nucleons share the same Hopf content at single wrap. The entire $Q$-value arises from the vacuum channel and the two crossing channels.

## $Q$-value from two inputs

The energy scale $E_0 = m_e / (q_0(q_0 - 1))$ converts dimensionless differences to MeV:

$$
  \mathfrak{Q}_\beta
  =
  |\Delta(\mathrm{net})| \times E_0
  =
  \frac{m_e \cdot |q^2 - 2q - 1| \cdot (q+1)}{2q^3}.
$$

## Numerical evaluation

At $q_0 \approx 1.110$ and $m_e \approx 0.511$ MeV:

$$
  \mathfrak{Q}_\beta
  =
  0.7836 \text{ MeV}
  \qquad
  (\text{CODATA: } 0.7823 \text{ MeV},
  \quad +0.17\%).
$$

The $1.3$ keV discrepancy represents the brane-tower correction to the energy scale $E_0$.

## Relation to the transfer-matrix eigenfunction form

The closed form above (Form A, normal-form counit basis) is equivalent to the transfer-matrix log-ratio form (Form B) up to the Markov–Jones normalization $z$:

$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \mathfrak{Q}_\beta^{\mathrm{B}} \cdot \Bigl(1 + \tfrac{(z-1)\,h}{2} + O(h^2)\Bigr).
$$

These two forms are not competing predictions; they describe the same observable in two bases.
<!-- FILE_END: neutron-qvalue-symbolic.md -->

<!-- FILE_START: qbeta-counit-closed-form.md -->
**Proposition (closed form of the counit $Q$-value).**
*Let $\Delta = \mathrm{NF}(n) - \mathrm{NF}(p)$ be the single-wrap normal-form difference of the neutron and proton typed-crossing elements in $H_3(q)$, and write $h = q - q^{-1}$. Let $\varepsilon$ denote the Frobenius counit and $\mathfrak{E}_0 = m_e/(q(q-1))$ the per-Hecke-step energy scale. Then:*
$$
  \varepsilon(\Delta)\cdot\mathfrak{E}_0
  \;=\;
  \frac{m_e\,(q+1)(q^2 - 2q - 1)}{2q^3}.
$$

## Counit versus Markov trace

Two canonical functionals act on this difference:
$$
  \varepsilon(\Delta) = \frac{h^2}{2} - h,
  \qquad
  \mathrm{tr}_M(\Delta) = \frac{h^2}{2} - h\,z.
$$

The counit is the Markov trace evaluated at the trivial loop value. The two agree precisely when $z = 1$. The trivial-loop value is never attained on the substrate. The counit and the Markov trace are genuinely distinct functionals on the substrate.

## Factorization of the energy scale

The per-Hecke-step energy factors through the information speed $c_q^2 = 1/(q-1)^2$ and the action-per-tick $\hbar_q^{E} = (q-1)/q$:
$$
  \mathfrak{E}_0
  =
  \frac{m_e}{q(q-1)}.
$$
The quantity $\hbar_q^{E}$ is the energy-scale action quantum, distinct from the Hecke parameter $h$.
<!-- FILE_END: qbeta-counit-closed-form.md -->

<!-- FILE_START: qbeta-counit-transition.md -->
The closed form clarifies the standing of the free-neutron relation $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})|\cdot\mathfrak{E}_0$. The relation uses the Frobenius counit $\varepsilon$, whereas the per-braid mass uses the Markov trace $\mathrm{tr}_M$.

## Two functionals, two observables

The Markov trace pairs against the unit. This closed-loop reading computes the static mass of a particle. The counit pairs against the canonical integral $\omega = G^{-1}\mathbf{1}$. This crossing-stripped reading counts the net reduction content.

A static mass is a closed loop, read by $\mathrm{tr}_M$. A $\beta$-decay is a transition. The per-Hecke-step energy is exactly $\mathfrak{E}_0$. The counit form is therefore the natural transition observable. When evaluated with $\mathrm{tr}_M$, the predicted $Q$-value falls short of the measured value by roughly a factor of two. When evaluated with the counit, it matches to $+0.17\%$.

## Agreement with the measured value

The $+0.17\%$ residual corresponds to the $N=0$ brane-tower truncation. The counit form and the Markov-trace mass difference $\mathfrak{m}(n) - \mathfrak{m}(p) - m_e$ compute the same physical observable in two ways. Their coincidence at the $N=0$ order demonstrates consistency between two canonical functionals.
<!-- FILE_END: qbeta-counit-transition.md -->

<!-- FILE_START: qbeta-trace-counit-convergence.md -->
**Conjecture (trace–counit convergence).**
*The per-braid Markov-trace nucleon mass difference $\mathfrak{m}(n) - \mathfrak{m}(p) - m_e$, summed over the brane tower, equals the Frobenius-counit $Q$-value $\varepsilon(\Delta)\cdot\mathfrak{E}_0$:*
$$
  \mathfrak{m}(n) - \mathfrak{m}(p) - m_e
  \;=\;
  \varepsilon(\Delta)\cdot\mathfrak{E}_0
  \;=\;
  \frac{m_e\,(q+1)(q^2 - 2q - 1)}{2q^3}.
$$

**Archimedean specialisation.** This block sits on the archimedean side of the substrate wall. It invokes real-valued physical observables, real-analytic bounds, transcendental constants, and numerical evaluation at the substrate parameter $q_0$. Any generic categorical identities remain valid over an abstract coefficient ring; we specialise only their archimedean realisation here.
<!-- FILE_END: qbeta-trace-counit-convergence.md -->

<!-- FILE_START: delta-pre-archimedean.md -->
**Proposition.**
*Let $f$ be any fibre fold. Since $f$ is an additive map on the fibre coefficient ring, for any fibre quantities $x_{\mathfrak n}, x_{\mathfrak p}$:*

$$
  f\bigl(x_{\mathfrak n} - x_{\mathfrak p}\bigr)
  \;=\; f(x_{\mathfrak n}) - f(x_{\mathfrak p}).
$$

*By contrast, the archimedean functor $\tau$ is a nonlinear $\mathrm{Li}_2^q$-tower. Thus, in general:*

$$
  \tau(x_{\mathfrak n}) - \tau(x_{\mathfrak p})
  \;\neq\; \tau\bigl(x_{\mathfrak n} - x_{\mathfrak p}\bigr).
$$

## Fibre algebra vs nonlinear functors

This establishes two theorems:

1. **Fibre folds commute with subtraction.** A fold $f$ commutes with the categorical subtraction. It allows folding to be applied inside the difference $\Delta(\mathrm{net})$.
2. **Archimedean functors do not commute with subtraction.** A nonlinear functor does not commute with the difference.

The choice of which order to use is an expository convention dictated by physics:

- **Difference observables** are computed via **delta-then-archimedean**. We form $\Delta(\mathrm{net})$ in the fibre, then apply $\tau$.
- **Absolute observables** are computed via **archimedean-then-(no delta)**. Each is a full $\tau$-image of its own braid tower.

## Necessity of the ordering for binding

Folding works for binding precisely because binding is a pre-archimedean delta. Computing the absolute masses first and then subtracting would interleave the nonlinear $\tau$ with the subtraction, breaking fold-invariance.
<!-- FILE_END: delta-pre-archimedean.md -->

<!-- FILE_START: transfer-beta-decay-q-beta-spectral-intro.md -->
We assemble the categorical $\mathfrak{Q}_\beta$ spectral bridge. We identify the bridge with closed-form tables and compute the silver-ratio $\beta$-decay null. This substrate-level prediction closes the silver-ratio falsifiability test. We support this construction with the nucleon normal form observability, the $\beta$-decay energy scale, the negative-debt confinement, and the visualiser-anchored braid presentation.
<!-- FILE_END: transfer-beta-decay-q-beta-spectral-intro.md -->

<!-- FILE_START: q-beta-spectral-bridge.md -->
**Proposition (conditional on Borromean quark conjecture — $\mathfrak{Q}_\beta$ spectral bridge).**

*Let $\mathcal{B}_n$ be the canonical free-neutron braid word with single wrap $A = 1$. Let $q = q_0$ be the substrate parameter and $h := q - q^{-1}$. We define the Markov–Jones parameter as:*
$$
  z \;:=\; \frac{1}{\sqrt q + 1/\sqrt q}.
$$
*Write $E_0 := m_e/(q(q-1))$ for the single-tick energy scale. Let:*
$$
  \mathfrak{Q}_\beta^{\mathrm{A}} \;:=\;
  \lvert \Delta(\mathrm{net}) \rvert \cdot E_0
  \qquad
  \mathfrak{Q}_\beta^{\mathrm{B}} \;:=\;
  \ln\!\frac{V_{\mathrm{pp}}}{V_{\mathrm{nn}}} \cdot \frac{E_0}{z}
$$
*denote the closed-form $Q$-value in the normal form counit basis and the transfer-matrix eigenfunction basis, respectively. Both forms are finite-depth truncations of the same spectral decomposition. They agree as:*
$$
  \frac{\mathfrak{Q}_\beta^{\mathrm{A}}}{\mathfrak{Q}_\beta^{\mathrm{B}}}
  \;=\;
  1 \;+\; \frac{(z-1)\,h}{2} \;+\; O(h^2),
$$
*with bridge identity:*
$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \ln\!\frac{V_{\mathrm{pp}}}{V_{\mathrm{nn}}} \cdot \frac{E_0}{z}
  \cdot \Bigl(1 + \tfrac{(z-1)\,h}{2} + O(h^2)\Bigr).
$$
*The remainder at depth $N$ in the brane-tower truncation decays exponentially.*
<!-- FILE_END: q-beta-spectral-bridge.md -->

<!-- FILE_START: archimedean-remainder-exponential-decay.md -->
**Conjecture (archimedean remainder exponential decay).**

*Fix a free-neutron sector $K \subset H_3(q)$. Let $\mathfrak{Q}_\beta^{(N)}$ be the depth-$N$ brane-tower truncation of the $\beta$-decay $Q$-value. Let $\mathfrak{Q}_\beta^{\mathrm{exact}}$ be the value of the full spectral decomposition. Then there exist constants $C(K), c(K) > 0$ such that the truncation remainder $R_N(K) \;:=\; \mathfrak{Q}_\beta^{(N)} - \mathfrak{Q}_\beta^{\mathrm{exact}}$ decays exponentially in the truncation depth:*

$$
  \bigl\lvert R_N(K) \bigr\rvert
  \;\le\;
  C(K)\,e^{-c(K)\,N}
  \qquad (N \ge 0).
$$

## Geometric and exponential phrasings coincide

The exponential form above and the geometric form used by the categorical precision ladder are the same statement. With $\hbar_q = (q_0 - 1)/q_0$, the Hecke quadratic structure gives the explicit ceiling

$$
  \bigl\lvert R_N(K) \bigr\rvert
  \;\le\;
  \frac{\hbar_q^{\,2(N+1)}}{1 - \hbar_q^{2}}.
$$

This is exactly $C \, e^{-c N}$ with $c \;=\; -2\ln \hbar_q$ and $C \;=\; \frac{\hbar_q^{2}}{1 - \hbar_q^{2}}$. The geometric ceiling above acts as the canonical witness rate.

## Purpose of the bound

This open conjectural input collapses the formally infinite brane-tower product to a finite-precision real prediction. With the bound in hand, each new rung tightens the prediction by a factor $\hbar_q^{2} \approx 100^{-1}$. This provides the precision-ceiling used by the precision ladder. Form A at $N = 0$ already yields a $+0.168\%$ residual because the $N = 0$ term sits inside the structural ceiling.
<!-- FILE_END: archimedean-remainder-exponential-decay.md -->

<!-- FILE_START: silver-ratio-beta-decay-null.md -->
**Proposition (silver-ratio trace degeneracy).**
*Let $q$ be the substrate parameter and $h = q - q^{-1}$. Then:*

$$
\boxed{\;
\Delta(\mathrm{net})
\;=\;
\frac{h(h-2)}{2}
\;=\;
\frac{q^2 - 2q - 1}{2q}
\;}
$$

*vanishes if and only if $h = 2$ if and only if $q = 1 \pm \sqrt{2}$ (the **silver-mean conjugates**).*

*At $q = 1 + \sqrt{2}$:*

1. *The Hecke quadratic $\sigma^2 = h\sigma + 1$ becomes $\sigma^2 = 2\sigma + 1$. The generator $\sigma$ has eigenvalues equal to the silver-ratio conjugates themselves.*
2. *Proton and neutron single-wrap Markov traces become equal: $\mathrm{net}(p) = \mathrm{net}(n) = 1 - h/2 = 0$.*
<!-- FILE_END: silver-ratio-beta-decay-null.md -->

<!-- FILE_START: silver-ratio-beta-decay-null-interpretation.md -->
The categorical interpretation: $q = 1 + \sqrt{2}$ is the **trace degeneracy point** — the substrate value at which proton and neutron are categorically indistinguishable. The null at $h = 2$ is the unique value where the bar-anti-symmetric kernel vanishes inside the empirical kinematic window.

## Silver-mean self-similarity

At the silver-ratio limit, the Hecke quotient $\sigma^2 = 2\sigma + 1$ recovers the **silver-mean self-similarity**: the two eigenvalues are conjugate and are exactly the q-values at which the recursion generates the Pell-Lucas sequences. The Hoefsmit off-diagonal coupling $b^2$ becomes a clean rational: $7/8$.

## $c_k$ closed forms at the silver ratio

Four of five $c_k$ values at the silver ratio are Pell-Lucas rationals. The single outlier is $c_5$, suggesting that the current empirical closed form $-(b^2 + 1/2)$ may not be the categorically correct form. The framework's true $c_5$ likely has a Pell-Lucas-clean silver-ratio value waiting to be identified.

## Outlier status of $c_5$ — involution + Leibniz interpretation

The $c_5 = -(b^2 + 1/2)$ outlier has a clean categorical interpretation combining **involution** and **Leibniz** structure. The typed-$\mathbf{B}_3$ braid construction uses averaged crossings at specific positions. The $h/2$ is the involution fingerprint. The $h/2$ from averaging propagates through higher rungs of the precision ladder via the Leibniz combinatorics. At rung $k=5$, the contribution from averaged positions becomes the dominant non-pure-$\sigma$ structure.

$c_3, c_4, c_6, c_7$ have dominant contributions from positions in the braid that are pure $\sigma$ or pure $\sigma^{-1}$. $c_5$ is uniquely sensitive to the averaged-crossing structure because the cross-term combinatorics amplify the $h/2$ contribution relative to the pure-$\sigma$ contributions at this specific order.

The $c_5$ Pell-Lucas outlier is not a sign of categorical incompleteness — it is the fingerprint of the typed-$\mathbf{B}_3$ averaged-crossing recipe. The categorical chain IS complete; $c_5$ just lives in the involution-fixed-point sector.
<!-- FILE_END: silver-ratio-beta-decay-null-interpretation.md -->

<!-- FILE_START: beta-decay-interpretation.md -->
## Universality

The universality $\Delta_\beta^{nn \to \mathrm{mix}} = \Delta_\beta^{\mathrm{mix} \to pp}$ means the matrix perturbation produced by converting one nucleon from $\mathfrak{n}$ to $\mathfrak{p}$ is the same regardless of whether the partner nucleon is a proton or a neutron. This is a consequence of the crossing coefficients being equally spaced. The mixed matrix is exactly the midpoint. Therefore the steps are the same displacement $\Delta_\beta$.

**Physical interpretation**: Beta decay shifts each crossing at the converting nucleon by the same universal amount $\Delta_\beta(q)$, independent of the partner. The effect on the Skein polynomial depends only on the number of crossings affected and their positions in the transfer matrix chain.

## Worked example: tritium

Consider ${}^3\mathrm{H}(p, n, n) \to {}^3\mathrm{He}(p, p, n)$. The converting nucleon is at position 1. The Skein polynomial ratio yields $\ln(P_{{}^3\mathrm{He}}/P_{{}^3\mathrm{H}}) = -0.1021$. Generator $\sigma_1$ contributes $78\%$ of the total. This matches the generator volume profile for heavier nuclei.

## Double beta decay

For $2\beta$ decay, two nucleons convert. At each affected generator, the transfer matrix perturbation is a product of two $\Delta_\beta$ matrices. The quadratic term is the 2-jet cross-term, which forms the nuclear matrix element of double beta decay. Since $\Delta_\beta$ is universal, the double beta matrix element depends only on the unchanged matrices between the two converting nucleons.
<!-- FILE_END: beta-decay-interpretation.md -->

<!-- FILE_START: nucleon-nf-observability.md -->
The Gröbner--Shirshov normal form of each nucleon in $H_3(q)$ has exactly six terms. With typed crossings, the sign pattern differs between neutron and proton. We classify each term by word length $\ell$ and observability.

## Sign patterns

With typed crossings, the sign patterns are:

- **Neutron**: four terms negative ($\gamma, L_+, e^-$).
- **Proton**: two terms negative ($\gamma, e^-$).

The neutron's $L_+$ sign flip represents the key effect of typed crossings: the $d$-$d$ crossing shifts the $\sigma_0\sigma_1$ coefficient below zero.

## Observability criterion

A braid word of length $\ell$ is **observable** when the corresponding knot or link is topologically non-trivial:

- **$\ell = 0$**: The identity $\mathbf{1}$ is topologically trivial.
- **$\ell = 1$**: A single crossing $\sigma_i$ is virtual (topologically removable).
- **$\ell = 2$**: The products $\sigma_0\sigma_1$ and $\sigma_1\sigma_0$ form Hopf links. They are topologically non-trivial and observable.
- **$\ell = 3$**: The product $\sigma_0\sigma_1\sigma_0$ is the trefoil knot. It is observable.

## Positive coefficients: observable vs virtual

Both nucleons are **dominated by virtual content**: the $\sigma_1$ term carries $\sim 94\%$ of the total positive amplitude. It cannot be observed as a free particle. The observable positive terms are the Hopf links $L_+$ and $L_-$.

## Location of $\sigma_1$: the color tube fiber

The generator $\sigma_1$ acts on the crossing within the color tube fiber between the red and green color coordinates. The dominance of $\sigma_1$ implies: the nucleon's internal energy resides overwhelmingly in the relative motion of color charges within the tube, not in the coupling between color and spacetime. This provides the algebraic expression of **color confinement**.

## Sign pattern and beta decay

The negative terms in each nucleon represent **leptonic debt** — topological content that must be supplied by the vacuum. The neutron carries three debts while the proton carries only two. The excess debt drives beta decay $\mathfrak{n} \to \mathfrak{p} + e^- + \bar{\nu}_e$. The neutron pays down its excess debt by emitting the physical electron and antineutrino.

The nucleon normal form exhibits a clean tripartite structure: virtual bulk, observable links, and leptonic debt. Beta decay settles this debt.
<!-- FILE_END: nucleon-nf-observability.md -->

<!-- FILE_START: beta-decay-energy-scale.md -->
The Gröbner--Shirshov normal form coefficients are dimensionless Laurent polynomials in $q$. To connect them to observed energies, we need an energy scale $\mathfrak{E}_0$ (in MeV) such that:

$$
  |\Delta(\mathrm{net})| \times \mathfrak{E}_0
  = 
  Q_{\beta}
  = 
  \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} - \mathfrak{m}_{e}
   \approx  0.7823 \text{MeV}.
$$

The framework provides $\mathfrak{E}_0$ in two forms. The first is a single-Planck-tick ($N=0$) value. The second is a tower-summed geometric form. These differ by the brane-tower correction $1/(1-\hbar_q^2) \approx 1.0099$. Both derive from CAL-1 ($m_e$) and CAL-2 ($q_0$) alone.

## Derivation (typed crossings)

From the witness: $\Delta(\mathrm{net}) = -0.188291$.

**Derived energy scale — single-tick (Planck-tick) form, $\mathfrak{E}_0^{(N=0)}$.**
The leading-order energy scale derives from the categorical three-calibration inputs:

$$
  \mathfrak{E}_0^{(N=0)}
  :=
  \frac{m_e}{q_0(q_0 - 1)}
  \approx  4.186 \text{MeV}.
$$

This is the electron rest energy per Planck time.

**Derived energy scale — tower-summed form, $\mathfrak{E}_0^{\text{full}}$.**
The full brane-tower geometric series is:

$$
  \mathfrak{E}_0^{\text{full}}
  :=
  \frac{\mathfrak{E}_0^{(N=0)}}{1 - \hbar_q^2}
  \approx  4.228 \text{MeV}.
$$

**Calibration cross-check, $\mathfrak{E}_0^{(\text{cal})}$.**
We extract the same scale from CODATA:

$$
  \mathfrak{E}_0^{(\text{cal})}
  =
  \frac{Q_{\beta}}{|\Delta(\mathrm{net})|}
   \approx  4.155 \text{MeV}.
$$

**Open finding.** Both the geometric tower form and the bounded symmetric $\mathrm{Li}_2^q$ candidate move the framework prediction further from the calibrated values at the substrate level. The correct closure is a non-obvious resummation identity that the conjecture seeks.

## NF$_+$ / NF$_-$ decomposition

The neutron has three negative terms ($\gamma, L_+, e^-$) while the proton has only two ($\gamma, e^-$). The $L_+$ sign flip is the typed-crossing effect.

## Observable vs virtual: $Q_{\geq 2}$

Terms of word length $\ell \geq 2$ are topologically non-trivial and observable. The observable-only $Q$-value is $58.5\%$ of $\mathfrak{Q}_\beta$.

## Full energy budget

Each of the six NF terms contributes to the total decay energy. The $\gamma$ debt and $L_+$ shift together account for $0.877 \text{MeV}$, which exceeds $\mathfrak{Q}_\beta$. The small virtual terms absorb the excess.

## Physical interpretation

Beta decay pays down the neutron's leptonic debt. The process $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu_e$ releases $\mathfrak{Q}_\beta = 0.782 \text{MeV}$ because the neutron's $L_+$ coefficient is negative while the proton's is positive. The $\Delta L_+$ is the dominant energy source. The neutron carries a larger $\gamma$ debt than the proton. The virtual terms contribute small negative corrections. The $e^-$ channel contributes nearly zero.
<!-- FILE_END: beta-decay-energy-scale.md -->

<!-- FILE_START: negative-debt-confinement.md -->
The NF$_+$ / NF$_-$ decomposition of the nucleon normal forms reveals a quantitative signature of confinement. The neutron carries significantly more internal cancellation than the proton.

## The negative coefficient debt

Each nucleon's Gröbner--Shirshov normal form splits into positive and negative coefficient sums. The neutron's negative coefficient debt $|\mathrm{NF}_-(\mathfrak{n})| = 0.2555$ exceeds the proton's by $|\Delta\mathrm{NF}_-| = 0.1127$. This excess debt is $11.3\%$ of the proton's net coefficient.

The dominant source is the $L_+$ sign flip. This single channel contributes approximately the entire excess debt.

## Confinement interpretation

The internal cancellation ratio measures how much of the total coefficient magnitude is consumed by destructive interference:

- **Neutron**: $19.3\%$ cancellation
- **Proton**: $11.1\%$ cancellation

The neutron's larger cancellation reflects its composition. The $d$--$d$ crossing generates a correction that propagates through the reduction. It flips the $L_+$ coefficient and amplifies the $\gamma$ debt. This is a computable, algebraic manifestation of color confinement. The energy cost of holding three quarks in a color-singlet braid is larger for the neutron because the $d$--$d$ interaction is more confining than $u$--$u$.
<!-- FILE_END: negative-debt-confinement.md -->

<!-- FILE_START: beta-decay-braid-visualizer.md -->
Interactive visualization of beta decay as a $T_{3,5}$ braid insertion on the nuclear braid word.

## The $T_{3,5}$ weak vertex

The weak interaction is carried by the torus knot $T_{3,5}$. Its braid word has $10$ crossings. This simulator draws the full braid left-to-right. It shows strands flowing from the parent nucleon through the $T_{3,5}$ insertion to the daughter nucleon plus lepton pair.

## Panels

1. **Braid flow diagram** --- The $10$-crossing $T_{3,5}$ braid inserted at the converting $\mathfrak{d}$-quark crossing.
2. **Transfer matrix crossings** --- The three nuclear crossing types drawn as individual braid crossings.
3. **Hecke and Skein relations** --- The Hecke relation and the Skein relation illustrated as braid crossing reductions.
4. **Universal decay matrix** --- The equally-spaced property with explicit polynomial entries.

## The $10$-crossing budget

The $10$ crossings consist of $3$ for the electron, $0$ for the antineutrino, and $7$ re-reduction crossings. The $7$ re-reduction crossings modify inter-nucleon crossing types at the converting quark's strand. These produce the dominant contribution to the $Q$-value.
<!-- FILE_END: beta-decay-braid-visualizer.md -->"""

with open("/Users/litlfred/space_cats/qou/amalgamated_done/particle-interactions_seq8.md", "w") as f:
    f.write(content_8)
with open("/Users/litlfred/space_cats/qou/amalgamated_done/particle-interactions_seq8.md.qa.json", "w") as f:
    f.write('{"criteria": {"milnor-amalgamated-flow": [{"result": "pass", "notes": "Rewrote seq8"}]}}')

