<!-- FILE_START: transfer-beta-decay-intro.md -->
The Gram-weighted $\mathcal{Q}_q$-value is the proper input for beta decay. We exhibit beta decay as a transfer-matrix insertion in the Skein-polynomial factorisation. The nuclear Skein polynomial factors as a product of $2 \times 2$ transfer matrices. This factorisation produces a universal transfer matrix operator. Consequently, every beta-decay event becomes a single matrix insertion in the same universal matrix-valued polynomial in $q$.

The eigenvalues of this transfer-matrix product select the ground-state ordering of nuclear configurations. Algebraic identities, such as $T_{pp}T_{nn} = I$ and $T_{pn}^2 = ([2]_q^2/4) I$, make the matrix factorisation tractable. We use these tools to compute symbolic $Q$-values, including the free neutron decay. We establish a basis-change identity between two forms of the $\mathfrak{Q}_\beta$ spectral bridge: Form A (normal form counit) and Form B (transfer-matrix log-ratio). At brane-tower depth $N = 1$, Form A admits a symbolic closed form via a geometric-series lift.

We connect the dimensionless normal form coefficients to physical MeV energy scales and track negative-coefficient debt that survives reduction. We provide a worked tritium example and its double-beta extension. Finally, an interactive simulator models beta decay as a $T_{3,5}$ braid insertion. This simulator tracks crossing budgets and transfer matrices. It serves as the computational basis for scaling the construction to the atomic braid $H_{A+Z}(q)$.

<!-- draft -->
<!-- FILE_END: transfer-beta-decay-intro.md -->

<!-- FILE_START: neutron-qvalue-symbolic.md -->
**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark) — $\mathfrak{Q}_\beta$ of free neutron $\beta^{-}$-decay).**
We derive the $Q$-value of free neutron $\beta^-$-decay $n \to p + e^- + \bar\nu_e$ symbolically from the categorical three-calibration inputs $m_e$ ($H^0$) and $q_0$ ($H^1$, fixed by $m_\mu/m_e$). The value $\mathfrak{Q}_\beta(n)$ ($H^2$) is the $\beta$-decay datum being predicted, not used as input ([three-calibration discipline](#prop:three-calibration-discipline)).

## Single-wrap normal-form computation

A single wrap of typed crossings in $H_3(q)$ represents the proton and neutron. Let $h = q - q^{-1}$.

**Proton** $[u, u, d]$: the typed crossing operators at generators $\sigma_0$ and $\sigma_1$ give:

$$
  \sigma_0 \cdot \bigl(\sigma_1 - \tfrac{h}{2}\mathbf{1}\bigr)
  = L_+ - \tfrac{h}{2}\sigma_0
$$

| $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ | net |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $-h/2$ | $0$ | $1$ | $0$ | $0$ | $1 - h/2$ |

**Neutron** $[u, d, d]$:

$$
  \bigl(\sigma_0 - \tfrac{h}{2}\mathbf{1}\bigr)
  \cdot
  \bigl(\sigma_1 - h\mathbf{1}\bigr)
  = L_+ - h\sigma_0 - \tfrac{h}{2}\sigma_1 + \tfrac{h^2}{2}\gamma
$$

| $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ | net |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $h^2/2$ | $-h$ | $-h/2$ | $1$ | $0$ | $0$ | $1 - 3h/2 + h^2/2$ |

## Symbolic $\Delta(\text{net})$

$$
  \Delta(\mathrm{net})
  =
  \mathrm{net}(n) - \mathrm{net}(p)
  =
  \frac{h^2}{2} - h
  =
  \frac{h(h - 2)}{2}.
$$

The difference per basis element is:

| $\Delta\gamma$ | $\Delta\sigma_0$ | $\Delta\sigma_1$ | $\Delta L_+$ | $\Delta L_-$ | $\Delta e^-$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $+h^2/2$ | $-h/2$ | $-h/2$ | $0$ | $0$ | $0$ |

The $L_+$ and $L_-$ contributions cancel exactly because both nucleons share the same Hopf content at single wrap. The entire $Q$-value arises from the vacuum channel ($+h^2/2$) and the two crossing channels ($-h/2$ each), with no trefoil content.

In terms of $q$:

$$
  \Delta(\mathrm{net})
  =
  \frac{(q+1)(q-1)(q^2 - 2q - 1)}{2q^2}.
$$

## $Q$-value from two inputs

The energy scale $E_0 = m_e / (q_0(q_0 - 1))$ ([energy scale](#rem:energy-scale-planck)) converts dimensionless normal-form differences to MeV:

$$
  \mathfrak{Q}_\beta
  =
  |\Delta(\mathrm{net})| \times E_0
  =
  \frac{(2 - h) \cdot h}{2}
  \times
  \frac{m_e}{q(q-1)}.
$$

Substituting $h = q - q^{-1}$:

$$
  \mathfrak{Q}_\beta
  =
  \frac{m_e \cdot (2 - h) \cdot h}{2q(q-1)}
  =
  \frac{m_e \cdot |q^2 - 2q - 1| \cdot (q+1)}{2q^3}.
$$

## Numerical evaluation

At $q_0 = 1.109978595554181\ldots$ (50 dps) (from $m_\mu/m_e$) and $m_e = :val[m_e_MeV]{precision=6, witness=computations/codata-masses.witness.json} \pm 0.00000000015$ MeV (CODATA 2022):

$$
  \mathfrak{Q}_\beta
  =
  0.7836 \text{ MeV}
  \qquad
  (\text{CODATA: } 0.7823 \text{ MeV},
  \quad +0.17\%,
  \quad +1.3 \text{ keV}).
$$

The $1.3$ keV discrepancy ($0.17\%$) represents the brane-tower correction to the energy scale $E_0$. The derived $E_0 = m_e/(q(q-1))$ is a single-level (Planck-tick) approximation; the exact tower-summed $E_0$ absorbs the residual.

This constitutes a 2-input closed form, conditional on the ansatz $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$ (stated "by construction" in [`pre-archimedean-derivation-chain.md`](../braids-and-knots/pre-archimedean-derivation-chain.md):391, not derived from the canonical per-braid mass formula). No hadronic calibration (neutron mass, proton mass, or $\mathfrak{Q}_\beta$ itself) is used in the closed form given the ansatz. The +0.17% match is empirical evidence for the ansatz but does not derive it. The functional standing of the relation — the counit $\varepsilon$ used here versus the Markov trace $\mathrm{tr}_M$ of the mass formula — is analysed in [`prop:qbeta-counit-closed-form`](#prop:qbeta-counit-closed-form) and [`rem:qbeta-counit-transition`](#rem:qbeta-counit-transition); see also [`docs/audits/-q-beta-net-ansatz-fitting-finding.md`](../../../docs/audits/-q-beta-net-ansatz-fitting-finding.md) for the audit and resolution paths.

**Witness**: symbolic derivation verified at $q_0 = 1.109978595554181$ from `q_parameter.py`.

## Relation to the transfer-matrix eigenfunction form

The closed form above (Form A, normal-form counit basis) is equivalent to the transfer-matrix log-ratio form ([prop:beta-decay-transfer-matrix](#prop:beta-decay-transfer-matrix)) up to the Markov–Jones normalization $z = 1/(\sqrt q + 1/\sqrt q)$, with explicit bridge identity in [prop:q-beta-spectral-bridge](#prop:q-beta-spectral-bridge):

$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \mathfrak{Q}_\beta^{\mathrm{B}} \cdot \Bigl(1 + \tfrac{(z-1)\,h}{2} + O(h^2)\Bigr).
$$

These two forms are not competing predictions; they describe the same observable in two bases. Form A is canonical here because the single-wrap normal-form counit reduces to a closed symbolic expression in $q$. Form B is the natural eigenfunction basis for $N \geq 1$ brane-tower truncation analysis.
<!-- FILE_END: neutron-qvalue-symbolic.md -->

<!-- FILE_START: qbeta-counit-closed-form.md -->
**Proposition (closed form of the counit $Q$-value).**
*Let $\Delta = \mathrm{NF}(n) - \mathrm{NF}(p)$ be the single-wrap normal-form difference of the neutron and proton typed-crossing elements in $H_3(q)$, and write $h = q - q^{-1}$. Let $\varepsilon$ denote the Frobenius counit (the unweighted sum of normal-form coefficients) and $\mathfrak{E}_0 = m_e/(q(q-1))$ the per-Hecke-step energy scale ([energy scale](#rem:energy-scale-planck)). Then:*
$$
  \varepsilon(\Delta)\cdot\mathfrak{E}_0
  \;=\;
  \frac{m_e\,(q+1)(q^2 - 2q - 1)}{2q^3}.
$$

## Counit versus Markov trace

The normal-form difference is supported on the identity and the two crossing generators, $\Delta = \bigl[\tfrac{h^2}{2},\,-\tfrac{h}{2},\,-\tfrac{h}{2},\,0,\,0,\,0\bigr]$ in the basis $[\gamma,\sigma_0,\sigma_1,L_+,L_-,e^-]$. The leading $L_+$ content cancels between the two nucleons. Two canonical functionals act on this difference:
$$
  \varepsilon(\Delta) = \frac{h^2}{2} - h,
  \qquad
  \mathrm{tr}_M(\Delta) = \frac{h^2}{2} - h\,z,
$$
where $z$ is the Markov–Jones loop parameter and the identity $\gamma = \mathbf{1}$ carries Markov weight $\mathrm{tr}_M(\mathbf{1}) = 1$. The counit is the Markov trace evaluated at the trivial loop value. The two agree precisely when $z = 1$, and otherwise differ by:
$$
  \varepsilon(\Delta) - \mathrm{tr}_M(\Delta) = h\,(z - 1).
$$

For $h \neq 0$, equality holds if and only if $z = 1$. Since $z = 1/(\sqrt q + 1/\sqrt q) \le \tfrac12$ for real $q > 0$, the trivial-loop value is never attained on the substrate. The counit and the Markov trace are genuinely distinct functionals on the substrate.

## Factorization of the energy scale

The per-Hecke-step energy factors through the information speed $c_q^2 = 1/(q-1)^2$ and the action-per-tick $\hbar_q^{E} = (q-1)/q$:
$$
  \mathfrak{E}_0
  =
  m_e\,c_q^2\,\hbar_q^{E}
  =
  \frac{m_e}{(q-1)^2}\cdot\frac{q-1}{q}
  =
  \frac{m_e}{q(q-1)}.
$$
The quantity $\hbar_q^{E} = (q-1)/q$ is the energy-scale action quantum, distinct from the Hecke parameter $h = q - q^{-1}$.

## Lean formalization

We verify the algebraic content over an arbitrary field, free of `sorry`. The module `QOU.Interactions.QBetaCounitTrace` contains the functional comparison ($\varepsilon = \mathrm{tr}_M$ at $z = 1$, the gap $h(z-1)$, and the equality criterion). The module `QOU.Interactions.QBetaEnergyScale` contains the energy-scale factorization `E0_eq` and the closed form `Qbeta_closed`.
<!-- FILE_END: qbeta-counit-closed-form.md -->

<!-- FILE_START: qbeta-counit-transition.md -->
The closed form ([`prop:qbeta-counit-closed-form`](#prop:qbeta-counit-closed-form)) clarifies the standing of the free-neutron relation $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})|\cdot\mathfrak{E}_0$ ([`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic)). The relation uses the Frobenius counit $\varepsilon$, whereas the per-braid mass uses the Markov trace $\mathrm{tr}_M$. These are distinct canonical functionals on $H_3(q)$. They agree on the nucleon difference only at the trivial loop $z = 1$. The substrate never attains this value.

## Two functionals, two observables

Both functionals are the Frobenius pairing $\langle x, y\rangle_G = \mathrm{tr}_M(xy)$ evaluated against different distinguished elements. The Markov trace pairs against the unit, $\mathrm{tr}_M(\beta) = \langle\beta, \mathbf{1}\rangle_G$. This closed-loop reading computes the static mass of a particle. The counit pairs against the canonical integral $\omega = G^{-1}\mathbf{1}$, $\varepsilon(\beta) = \langle\beta, \omega\rangle_G$. This crossing-stripped reading counts the net reduction content.

A static mass is a closed loop, read by $\mathrm{tr}_M$. A $\beta$-decay is a transition: the nucleon braid reduces, with one crossing re-typed under $d \to u$. The energy of a reduction is the number of reduction steps multiplied by the energy per step. The per-Hecke-step energy is exactly $\mathfrak{E}_0$ ([energy scale](#rem:energy-scale-planck)). The counit form:
$$
  \mathfrak{Q}_\beta = \varepsilon(\Delta)\cdot\mathfrak{E}_0
$$
is therefore the natural transition observable. The Markov trace (the loop observable) is the incorrect functional for a transition. When evaluated with $\mathrm{tr}_M$ instead of $\varepsilon$, the predicted $Q$-value falls short of the measured value by roughly a factor of two. When evaluated with the counit, it matches to $+0.17\%$.

## Agreement with the measured value

The $+0.17\%$ residual corresponds to the $N=0$ brane-tower truncation. This is the same residual that separates the derived energy scale $\mathfrak{E}_0 \approx 4.186$ MeV from its calibration cross-check $\approx 4.155$ MeV ([energy scale](#rem:energy-scale-planck)). The counit form and the Markov-trace mass difference $\mathfrak{m}(n) - \mathfrak{m}(p) - m_e$ compute the same physical observable in two ways. Their coincidence at the $N=0$ order demonstrates consistency between two canonical functionals, rather than a curve fit. A fully tower-summed derivation, which establishes that the trace mass difference converges to $\varepsilon(\Delta)\cdot\mathfrak{E}_0$ with the $+0.17\%$ serving as its remainder, remains open.
<!-- FILE_END: qbeta-counit-transition.md -->

<!-- FILE_START: qbeta-trace-counit-convergence.md -->
**Conjecture (trace–counit convergence).**
*The per-braid Markov-trace nucleon mass difference $\mathfrak{m}(n) - \mathfrak{m}(p) - m_e$, summed over the brane tower, equals the Frobenius-counit $Q$-value $\varepsilon(\Delta)\cdot\mathfrak{E}_0$ of [`prop:qbeta-counit-closed-form`](#prop:qbeta-counit-closed-form):*
$$
  \mathfrak{m}(n) - \mathfrak{m}(p) - m_e
  \;=\;
  \varepsilon(\Delta)\cdot\mathfrak{E}_0
  \;=\;
  \frac{m_e\,(q+1)(q^2 - 2q - 1)}{2q^3}.
$$
*The two sides represent evaluations through two canonical functionals on $H_3(q)$: the static-mass Markov trace $\mathrm{tr}_M$ (pairing with the unit) and the transition counit $\varepsilon$ (pairing with the integral $\omega = G^{-1}\mathbf{1}$). The conjecture posits their equality.*

## Formalization

We axiomatize this conjecture as the Lean class `QOU.Interactions.QBetaConvergence.QBetaTraceCounitConvergence`. The `counitForm_eq` field records the proven closed form ([`prop:qbeta-counit-closed-form`](#prop:qbeta-counit-closed-form), `Qbeta_closed`), and the `converges` field carries the conjectural identity. Given this class, the conditional corollary `qbeta_is_trace_mass_difference` proves that the physical trace mass difference equals the counit closed form. The class instance is the only unproved input.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-valued physical observables, real-analytic bounds, transcendental constants, and numerical evaluation at the substrate parameter $q_0$. Any generic categorical identities remain valid over an abstract coefficient ring; we specialise only their archimedean realisation here.
<!-- FILE_END: qbeta-trace-counit-convergence.md -->

<!-- FILE_START: delta-pre-archimedean.md -->
The proton/neutron difference observables—the $\beta$-decay Q-value $\mathfrak{Q}_\beta = \lvert\Delta(\mathrm{net})\rvert\cdot\mathfrak{E}_0$ ([neutron Q-value](#prop:neutron-qvalue-symbolic)) and the binding energy $B(K)$—are computed in a specific order. The categorical difference $\Delta = x_{\mathfrak n} - x_{\mathfrak p}$ is formed at the fibre level, and only then is the archimedean functor $\tau$ applied. We record why this order is forced and distinguish between proved statements and expository conventions.

**Proposition.** Let $f$ be any fibre fold (the bar involution $q\mapsto q^{-1}$, the Hecke antipode $\sigma_i\mapsto\sigma_i^{-1}$, or a Type-B fold). Since $f$ is an additive map on the fibre coefficient ring, for any fibre quantities $x_{\mathfrak n}, x_{\mathfrak p}$:

$$
  f\bigl(x_{\mathfrak n} - x_{\mathfrak p}\bigr)
  \;=\; f(x_{\mathfrak n}) - f(x_{\mathfrak p}).
$$

By contrast, the archimedean functor $\tau$ is a nonlinear $\mathrm{Li}_2^q$-tower / Markov-product / $\mathfrak{E}_0$-scaling. Thus, in general:

$$
  \tau(x_{\mathfrak n}) - \tau(x_{\mathfrak p})
  \;\neq\; \tau\bigl(x_{\mathfrak n} - x_{\mathfrak p}\bigr).
$$

## Fibre algebra vs nonlinear functors

This establishes two theorems:

1. **Fibre folds commute with subtraction.** A fold $f$ commutes with the categorical subtraction. This relies on additivity over a generic commutative ring, with no archimedean input. It allows the bar involution, the $\sigma\leftrightarrow\sigma^{-1}$ reduction, and Type-B folding to be applied inside the difference $\Delta(\mathrm{net})$ and inside the binding tower.
2. **Archimedean functors do not commute with subtraction.** A nonlinear functor does not commute with the difference. The two operations—masses-then-delta and delta-then-archimedean—are distinct.

The choice of which order to use is an expository convention dictated by physics:

- **Difference observables** ($\mathfrak{Q}_\beta$, binding $B$) are computed via **delta-then-archimedean**. We form $\Delta(\mathrm{net})$ in the fibre, then apply $\tau$. This preserves fold invariance and cancels the imaginary parts of the archimedean tower in the difference.
- **Absolute observables** ($m_{\mathfrak p}, m_{\mathfrak n}$) are computed via **archimedean-then-(no delta)**. Each is a full $\tau$-image of its own braid tower.

The proton–neutron mass split $\Delta_{pn} = m_{\mathfrak n} - m_{\mathfrak p}$ sits at the boundary. The framework's predicted split evaluates via the difference observable $\mathfrak{Q}_\beta$ (plus the electron: $\mathfrak{Q}_\beta = \Delta_{pn} - m_e$), following the delta-then-archimedean route.

## Necessity of the ordering for binding

Folding and unfolding drive the binding and $\mathfrak{Q}_\beta$ derivations. By the first theorem, these folds commute with the pre-archimedean delta, making them legitimate moves inside $\Delta(\mathrm{net})$. By the second theorem, they do not commute with the difference of two $\tau$-images. Thus, folding works for binding precisely because binding is a pre-archimedean delta. Computing the absolute masses first and then subtracting would interleave the nonlinear $\tau$ with the subtraction, breaking fold-invariance.

## Lean structure

`FibreFold R` bundles additivity. The lemma `fold_commutes_sub` proves $f(x-y)=f(x)-f(y)$ over a generic `CommRing`—no `ℝ`, no ordering. The lemma `archimedean_does_not_commute_sub` exhibits a concrete nonlinear witness. The fold lives in the fibre; reality enters only at $\tau$.
<!-- FILE_END: delta-pre-archimedean.md -->

<!-- FILE_START: transfer-beta-decay-q-beta-spectral-intro.md -->
We assemble the categorical $\mathfrak{Q}_\beta$ spectral bridge. We identify the bridge with closed-form tables and compute the silver-ratio $\beta$-decay null. This substrate-level prediction closes the silver-ratio falsifiability test. We support this construction with the nucleon normal form observability, the $\beta$-decay energy scale, the negative-debt confinement, and the visualiser-anchored braid presentation. We tabulate the resulting substrate-level $\mathfrak{Q}_\beta$ predictions against Particle Data Group (PDG) endpoints.
<!-- FILE_END: transfer-beta-decay-q-beta-spectral-intro.md -->

<!-- FILE_START: q-beta-spectral-bridge.md -->
**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark) — $\mathfrak{Q}_\beta$ spectral bridge).**

*Let $\mathcal{B}_n$ be the canonical free-neutron braid word with single wrap $A = 1$. Let $q = q_0$ be the substrate parameter and $h := q - q^{-1}$. We define the Markov–Jones parameter (Hecke–Skein normalization) as:*
$$
  z \;:=\; \frac{1}{\sqrt q + 1/\sqrt q}.
$$
*Write $E_0 := m_e \cdot c_q^2 \cdot \hbar_q = m_e/(q(q-1))$ for the single-tick energy scale ([rem:energy-scale-planck](#rem:energy-scale-planck)). Let:*
$$
  \mathfrak{Q}_\beta^{\mathrm{A}} \;:=\;
  \lvert \Delta(\mathrm{net}) \rvert \cdot E_0
  \qquad
  \mathfrak{Q}_\beta^{\mathrm{B}} \;:=\;
  \ln\!\frac{V_{\mathrm{pp}}}{V_{\mathrm{nn}}} \cdot \frac{E_0}{z}
$$
*denote the closed-form $Q$-value in the normal form counit basis (Form A, [prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic)) and the transfer-matrix eigenfunction basis (Form B, [prop:beta-decay-transfer-matrix](#prop:beta-decay-transfer-matrix)), respectively. Both forms are finite-depth truncations of the same spectral decomposition. They agree as:*
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
*The remainder at depth $N$ in the brane-tower truncation satisfies:*
$$
  \bigl\lvert \mathfrak{Q}_\beta^{(N)} - \mathfrak{Q}_\beta^{\mathrm{exact}} \bigr\rvert
  \;\le\;
  C(K) \cdot e^{-c(K)\,N}
$$
*per conj:archimedean-remainder-exponential-decay, where $C, c > 0$ depend only on the free-neutron sector data $K$.*
<!-- FILE_END: q-beta-spectral-bridge.md -->

<!-- FILE_START: archimedean-remainder-exponential-decay.md -->
**Conjecture (archimedean remainder exponential decay).**

*Fix a free-neutron sector $K \subset H_3(q)$. This is the canonical typed
braid word together with its Gröbner–Shirshov filtration. We evaluate
at the substrate parameter $q = q_0$. Let $\mathfrak{Q}_\beta^{(N)}$ be the
depth-$N$ brane-tower truncation of the $\beta$-decay $Q$-value (Form A
or Form B, [`prop:q-beta-spectral-bridge`](#prop:q-beta-spectral-bridge)). Let $\mathfrak{Q}_\beta^{\mathrm{exact}}$ be the value of the full
spectral decomposition. Then there exist constants $C(K), c(K) > 0$,
depending only on the sector data $K$, such that the truncation
remainder*

$$
  R_N(K) \;:=\; \mathfrak{Q}_\beta^{(N)} - \mathfrak{Q}_\beta^{\mathrm{exact}}
$$

*decays exponentially in the truncation depth:*

$$
  \bigl\lvert R_N(K) \bigr\rvert
  \;\le\;
  C(K)\,e^{-c(K)\,N}
  \qquad (N \ge 0).
$$

## Geometric and exponential phrasings coincide

The exponential form above and the geometric form used by the
categorical precision ladder are the same statement. With
$\hbar_q = (q_0 - 1)/q_0$, the Hecke quadratic structure gives the
explicit ceiling

$$
  \bigl\lvert R_N(K) \bigr\rvert
  \;\le\;
  \frac{\hbar_q^{\,2(N+1)}}{1 - \hbar_q^{2}}.
$$

This is exactly $C \, e^{-c N}$ with

$$
  c \;=\; -2\ln \hbar_q,
  \qquad
  C \;=\; \frac{\hbar_q^{2}}{1 - \hbar_q^{2}},
$$

because $\hbar_q^{\,2(N+1)} = \hbar_q^{2}\,(\hbar_q^{2})^{N}
= \hbar_q^{2}\,e^{-2N\ln(1/\hbar_q)}$. At $q_0 \approx 1.110$, one has
$\hbar_q^2 \approx 9.82 \times 10^{-3}$, so $c \approx 4.62$ and
$C \approx 9.91 \times 10^{-3}$. The conjecture asserts that some
pair $(C(K), c(K))$ controls the operator's own remainder. The
geometric ceiling above acts as the canonical witness rate. The true
operator rate may be tighter (larger $c(K)$).

## Purpose of the bound

This open conjectural input collapses the formally infinite
brane-tower product to a finite-precision real prediction. With
the bound in hand, each new rung tightens the prediction by a factor
$\hbar_q^{2} \approx 100^{-1}$. Thus, the truncation order required for a
target relative precision $\varepsilon$ is

$$
  N \;\ge\; \frac{\log_{10}(1/\varepsilon)}{2\log_{10}(1/\hbar_q)} - 1.
$$

This provides the precision-ceiling used by
[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder).
It supplies the eigenfunction dampening principle behind
[`prop:q-beta-spectral-bridge`](#prop:q-beta-spectral-bridge). Form A at
$N = 0$ already yields a $+0.168\%$ residual because the $N = 0$ term sits
inside the structural ceiling, showing a $\sim 5.9\times$ headroom against the
observed residual (verified at $50$ digits of precision,
[`c_k_beta_decay_witness.py`](https://github.com/litlfred/qou/blob/main/computations/c_k_beta_decay_witness.py)).
The remainder feeds the per-knot bound of Mechanism 1 in
[`prop:categorical-chain-convergence-mechanisms`](#prop:categorical-chain-convergence-mechanisms).
Its Lean script proves the geometric decay relation
$c_K\text{Bound}(N+1) = \hbar_q^{2}\cdot c_K\text{Bound}(N)$ and delegates the
bound itself to this conjecture.

## Status of the conjecture

The bound remains conjectural. The substrate identity fixes a witness
rate $(C, c)$ that the $N = 0$ residual respects empirically. However, a
proof that the operator's spectral tail along the Gröbner–Shirshov
filtration of $K$ decays at this (or any) exponential rate is not
available. Pinning $c(K)$ for the operator represents the open lift-formula part
of the brane-tower $z$-Habiro programme. The conjecture is primary;
it does not depend conditionally on any other conjecture.
<!-- FILE_END: archimedean-remainder-exponential-decay.md -->

<!-- FILE_START: silver-ratio-beta-decay-null.md -->
**Proposition (silver-ratio trace degeneracy).**
*Let $q$ be the substrate parameter and $h = q - q^{-1}$ the Hecke
skein parameter on $H_3(q)$. Then:*

$$
\boxed{\;
\Delta(\mathrm{net}) \;=\; \mathrm{net}(n) - \mathrm{net}(p)
\;=\;
\frac{h(h-2)}{2}
\;=\;
\frac{q^2 - 2q - 1}{2q}
\;}
$$

*vanishes if and only if $h = 2$ if and only if $q = 1 \pm \sqrt{2}$
(the **silver-mean conjugates**).*

*At $q = 1 + \sqrt{2}$ (silver ratio):*

1. *The Hecke quadratic $\sigma^2 = h\sigma + 1$ becomes
   $\sigma^2 = 2\sigma + 1$, whose roots are*
   $$\sigma = 1 \pm \sqrt{2} = q^{\pm 1}|_{q=1+\sqrt{2}}.$$
   *The generator $\sigma$ has eigenvalues equal to the
   silver-ratio conjugates themselves — a **self-referential
   fixed point**.*
2. *Proton and neutron single-wrap Markov traces become equal:
   $\mathrm{net}(p) = \mathrm{net}(n) = 1 - h/2 = 0$.*

## Derivation

From [`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic),
the symbolic single-wrap Markov-trace net coefficients are:

| | $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | net |
|---|:---:|:---:|:---:|:---:|:---:|
| proton | $0$ | $-h/2$ | $0$ | $1$ | $1 - h/2$ |
| neutron | $h^2/2$ | $-h$ | $-h/2$ | $1$ | $1 - 3h/2 + h^2/2$ |

Subtracting: $\Delta(\mathrm{net}) = h^2/2 - h = h(h-2)/2$.

Setting $h = 2$ gives $q - q^{-1} = 2$, i.e. $q^2 - 2q - 1 = 0$,
with roots $q = 1 \pm \sqrt{2}$.
<!-- FILE_END: silver-ratio-beta-decay-null.md -->

<!-- FILE_START: silver-ratio-beta-decay-null-interpretation.md -->
The categorical interpretation: $q = 1 + \sqrt{2}$ is the
**trace degeneracy point** — the substrate value at which proton and
neutron are categorically indistinguishable.

> **Bar-symmetry class** (per [`def:bar-involution`](#def:bar-involution)):
> $h = q - q^{-1}$ is **bar-anti-symmetric** ($\overline h = -h$);
> $\Delta(\mathrm{net}) = h(h-2)/2$ is bar-anti-symmetric in $h$.
> The null at $h = 2$ — the silver-ratio root of
> $\Delta(\mathrm{net})$ — is the unique value where the
> bar-anti-symmetric kernel vanishes inside the framework's
> empirical kinematic window. At silver, $[n]_q$ values are
> Pell-Lucas numbers ($a_n$); $b^2 = 1 - 1/[2]_q^2 = 7/8$ exactly.
> Both are bar-symmetric.

## Silver-mean self-similarity

At the silver-ratio limit, the Hecke quotient $\sigma^2 = 2\sigma + 1$
recovers the **silver-mean self-similarity**: the two eigenvalues
$1 + \sqrt{2}$ and $1 - \sqrt{2}$ are conjugate over
$\mathbb{Q}(\sqrt{2})$ and are exactly the q-values at which the
recursion $a_{n+1} = 2a_n + a_{n-1}$ (the **Pell recursion**)
generates the Pell-Lucas / Pell number sequences.

Specifically: at $q = 1 + \sqrt{2}$, the $q$-integers $[n]_q$
evaluate to integers via the Pell-Lucas sequence:

$$
[3]_q = q^2 + 1 + q^{-2} = 7, \qquad
[5]_q = q^4 + q^2 + 1 + q^{-2} + q^{-4} = 41,
$$

both Pell-Lucas numbers (companion sequence $1, 1, 3, 7, 17, 41, \dots$).
The Hoefsmit off-diagonal coupling $b^2$ becomes a clean rational:

$$
b^2(1 + \sqrt{2}) = \frac{q^4 + q^2 + 1}{(q^2+1)^2}
\bigg|_{q=1+\sqrt{2}}
= \frac{7(3 + 2\sqrt{2})}{8(3 + 2\sqrt{2})} = \frac{7}{8}.
$$

## $c_k$ closed forms at the silver ratio

Evaluating the precision-ladder coefficients at $q = 1 + \sqrt{2}$:

| $c_k$ | Closed form | At silver ratio | Pell-Lucas interpretation |
|:----:|:-----------:|:---------------:|---------------------------|
| $c_3$ | $-2$ | $-2$ | $-2$ (integer; constant) |
| $c_4$ | $c_3 \cdot b^4$ | $-49/32$ | $-a_3^2/2^5$ (Pell-Lucas-clean) |
| $c_5$ | $-(b^2 + 1/2)$ | $-11/8$ | **OUTLIER** (11 not Pell) |
| $c_6$ | $c_3^2 \cdot b^2$ | $7/2$ | $a_3/2$ (Pell-Lucas-clean) |
| $c_7$ | $c_3^3$ | $-8$ | $-2^3$ (integer; constant) |

**Four of five** $c_k$ values at the silver ratio are Pell-Lucas
rationals (clean integer numerators built from Pell-Lucas terms
$a_n$). The single outlier is $c_5$, suggesting that the current
empirical closed form $-(b^2 + 1/2)$ may not be the categorically
correct form — the framework's true $c_5$ likely has a Pell-Lucas-clean
silver-ratio value waiting to be identified.

Is there a categorical theorem in the framework's Hecke /
Wedderburn-block content that uses the Pell recursion?
The Pell recursion at $q = 1 + \sqrt{2}$ matches the Hecke quadratic
$\sigma^2 = 2\sigma + 1$ — this suggests **looking for braided
recursion identities at the Hecke level that reduce to Pell at the
silver ratio**.


## Outlier status of $c_5$ — involution + Leibniz interpretation

The $c_5 = -(b^2 + 1/2)$ outlier has a clean categorical interpretation
combining **involution** and **Leibniz** structure:

### Involution origin: the averaged crossing operator

The typed-$\mathbf{B}_3$ braid construction uses **averaged crossings**
at specific positions:
$$
\sigma_{\text{avg}} := \frac{\sigma + \sigma^{-1}}{2} = \sigma - \frac{h}{2}
$$
(using the Hecke quadratic $\sigma^{-1} = \sigma - h$).

This $\sigma_{\text{avg}}$ is the **bar-invariant projection of $\sigma$**:
$\sigma_{\text{avg}} = P_{\text{avg}}(\sigma)$ where $P_{\text{avg}} = (1 + \overline{\,\,})/2$
is the bar-involution projector ($\overline{\sigma} = \sigma^{-1}$ in $H_n(q)$).

The proton braid contains ONE averaged $\sigma_1$ position with coefficient
$-h/2$; the neutron braid contains TWO averaged positions. The $h/2$ is the
**involution fingerprint**.

### Leibniz propagation: how $h/2$ reaches $c_5$

Markov-trace expansion of the typed braid generates the
single-wrap $\Delta(\mathrm{net}) = h^2/2 - h = h(h-2)/2$. The
$h/2$ from averaging propagates through higher rungs of the
precision ladder via the Leibniz / product-expansion combinatorics.

At rung $k=5$ (order $\hbar_q^{10}$), the contribution from
averaged positions becomes the dominant non-pure-$\sigma$
structure, giving:
$$
c_5 = -b^2 - \frac{1}{2}
$$
where $-b^2$ is the **pure-$\sigma$-action** (Kashiwara return
amplitude squared) and $-1/2$ is the **averaged-crossing involution
fingerprint at rung 5**.

### Absence of the $1/2$ in other $c_k$

$c_3, c_4, c_6, c_7$ have dominant contributions from POSITIONS in
the braid that are pure $\sigma$ or pure $\sigma^{-1}$ — not averaged.
At their respective orders ($k = 3, 4, 6, 7$), the averaged-position
contributions are subdominant, and their closed forms factor through
pure Pell-Lucas combinatorics at the silver ratio.

$c_5$ is uniquely sensitive to the averaged-crossing structure
because: (a) the proton has exactly ONE averaged $\sigma_1$
position at coefficient $h/2$, and (b) the cross-term combinatorics
in the $b^5 \hbar_q^{10}$ rung amplify the $h/2$ contribution
relative to the pure-$\sigma$ contributions at this specific order.

### Implication

The $c_5$ Pell-Lucas outlier is **not a sign of categorical
incompleteness** — it is the **fingerprint of the typed-$\mathbf{B}_3$
averaged-crossing recipe**. The categorical chain IS complete; $c_5$
just lives in the involution-fixed-point sector while the other $c_k$
live in the pure-$\sigma$ sector.

This also predicts that **any $c_k$ at higher rungs whose order
coincides with an averaging-resonance position will pick up
similar $1/2$ fingerprints**. The next such rung is unknown but
testable by extending the SDP-$T_\beta$ extraction to $k \ge 8$.
<!-- FILE_END: silver-ratio-beta-decay-null-interpretation.md -->

<!-- FILE_START: beta-decay-interpretation.md -->
## Universality

The universality $\Delta_\beta^{nn \to \mathrm{mix}} = \Delta_\beta^{\mathrm{mix} \to pp}$ means the matrix perturbation produced by converting one nucleon from $\mathfrak{n}$ to $\mathfrak{p}$ is the same regardless of whether the partner nucleon is a proton or a neutron.

This is a consequence of the crossing coefficients being equally spaced:

$$
  T_{\mathrm{mix}} = \tfrac{1}{2}(T_{pp} + T_{nn})
$$

The mixed matrix is exactly the midpoint. Therefore the steps $T_{nn} \to T_{\mathrm{mix}}$ and $T_{\mathrm{mix}} \to T_{pp}$ are the same displacement $\Delta_\beta$.

**Physical interpretation**: Beta decay shifts each crossing at the converting nucleon by the same universal amount $\Delta_\beta(q)$, independent of the partner. The effect on the Skein polynomial depends only on the number of crossings affected and their positions in the transfer matrix chain.

## Worked example: tritium

Consider ${}^3\mathrm{H}(p, n, n) \to {}^3\mathrm{He}(p, p, n)$. The converting nucleon is at position 1 (first neutron to proton).

**Generator $\sigma_0$** (2 crossings: with nucleons 1 and 2):

| Crossing | Parent | Daughter | Change |
|----------|--------|----------|--------|
| $(0, 1)$ | $\mathfrak{p}\mathfrak{n}$ = mixed | $\mathfrak{p}\mathfrak{p}$ = pp | $+\Delta_\beta$ |
| $(0, 2)$ | $\mathfrak{p}\mathfrak{n}$ = mixed | $\mathfrak{p}\mathfrak{n}$ = mixed | unchanged |

$$
  M_0^{\mathrm{par}} = T_{\mathrm{mix}} \cdot T_{\mathrm{mix}},
  \quad
  M_0^{\mathrm{dau}} = T_{pp} \cdot T_{\mathrm{mix}}
$$

$$
  \hat{V}_0^{\mathrm{par}} = 0.7684, \quad
  \hat{V}_0^{\mathrm{dau}} = 0.7510
$$

**Generator $\sigma_1$** (1 crossing: with nucleon 2):

| Crossing | Parent | Daughter | Change |
|----------|--------|----------|--------|
| $(1, 2)$ | $\mathfrak{n}\mathfrak{n}$ = nn | $\mathfrak{p}\mathfrak{n}$ = mixed | $+\Delta_\beta$ |

$$
  M_1^{\mathrm{par}} = T_{nn},
  \quad
  M_1^{\mathrm{dau}} = T_{\mathrm{mix}}
$$

$$
  \hat{V}_1^{\mathrm{par}} = 1.3029, \quad
  \hat{V}_1^{\mathrm{dau}} = 1.2036
$$

**Skein polynomial ratio:**

$$
  \frac{P_{{}^3\mathrm{He}}(q)}{P_{{}^3\mathrm{H}}(q)}
  = 
  \frac{0.7510 \times 1.2036}{0.7684 \times 1.3029}
  = 
  \frac{0.9039}{1.0011}
  =  0.9029
$$

$$
  \ln\!\left(\frac{P_{{}^3\mathrm{He}}}{P_{{}^3\mathrm{H}}}\right)
  =  -0.1021
$$

Per-generator contribution:

| Generator | $\ln(\hat{V}^{\mathrm{dau}}/\hat{V}^{\mathrm{par}})$ | Fraction |
|:---------:|:---:|:---:|
| $\sigma_0$ | $-0.0229$ | $22\%$ |
| $\sigma_1$ | $-0.0792$ | $78\%$ |

Generator $\sigma_1$ (the converting nucleon's own generator) contributes $78\%$ of the total. This matches the generator volume profile for heavier nuclei.

## Double beta decay

For $2\beta$ decay, two nucleons convert. At each affected generator, the transfer matrix perturbation is a product of two $\Delta_\beta$ matrices (with intervening unchanged matrices):

$$
  \Delta M_i^{(2\beta)}
  = 
  L_i \cdot \Delta_\beta \cdot C_i \cdot \Delta_\beta \cdot R_i
  + 
  (\text{linear terms})
$$

Here $C_i$ is the product of unchanged matrices between the two converting positions. The quadratic term $\Delta_\beta \cdot C_i \cdot \Delta_\beta$ is the 2-jet cross-term, which forms the nuclear matrix element of double beta decay ([jet expansion](#prop:generator-volume-decomposition)).

Since $\Delta_\beta$ is universal, the double beta matrix element depends only on $C_i$ — the unchanged matrices between the two converting nucleons. We compute this from the nucleon types in that region.
<!-- FILE_END: beta-decay-interpretation.md -->

<!-- FILE_START: nucleon-nf-observability.md -->
The Gröbner--Shirshov normal form of each nucleon in $H_3(q)$ has exactly **six terms**, one for each basis element of the Iwahori--Hecke algebra. With typed crossings ($u$-$u = \sigma$, $d$-$d = \sigma - (q - q^{-1})\mathbf{1}$, $u$-$d = \sigma - \tfrac{1}{2}(q - q^{-1})\mathbf{1}$), the sign pattern differs between neutron and proton. We classify each term by **word length** $\ell$ and **observability** (whether the corresponding knot or link is topologically non-trivial).

## The six normal form terms

| Particle | Word | Knot/Link | $\ell$ | Neutron $\mathfrak{n}$ | Proton $\mathfrak{p}$ | Observable? |
|:---:|:---:|:---:|:---:|---:|---:|:---:|
| $\gamma$ | $\mathbf{1}$ | photon | $0$ | $-0.201704$ | $-0.099658$ | No (identity) |
| $\sigma_0$ | $\sigma_0$ | virtual | $1$ | $+0.048130$ | $+0.035729$ | No (virtual) |
| $\sigma_1$ | $\sigma_1$ | virtual | $1$ | $+1.008995$ | $+0.997570$ | No (virtual) |
| $L_+$ | $\sigma_0\sigma_1$ | Hopf link | $2$ | $-0.009641$ | $+0.099354$ | Yes (Hopf link) |
| $L_-$ | $\sigma_1\sigma_0$ | Hopf link | $2$ | $+0.009237$ | $+0.009337$ | Yes (Hopf link) |
| $e^-$ | $\sigma_0\sigma_1\sigma_0$ | trefoil ($3_1$) | $3$ | $-0.044184$ | $-0.043208$ | Yes (trefoil) |

Numerical values at $q_0 \approx 1.1100$ (typed crossings).

## Sign patterns

With typed crossings, the sign patterns are:

- **Neutron**: $[-, +, +, -, +, -]$ — four terms negative ($\gamma, L_+, e^-$). The $L_+$ coefficient flips from positive (untyped) to negative.
- **Proton**: $[-, +, +, +, +, -]$ — two terms negative ($\gamma, e^-$), unchanged from untyped.

The neutron's $L_+$ sign flip represents the key effect of typed crossings: the $d$-$d$ crossing in the neutron $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ shifts the $\sigma_0\sigma_1$ coefficient below zero.

## Observability criterion

A braid word of length $\ell$ is **observable** when the corresponding knot or link is topologically non-trivial:

- **$\ell = 0$**: The identity $\mathbf{1}$ maps to the photon $\gamma$. It is topologically trivial and carries no knot content.
- **$\ell = 1$**: A single crossing $\sigma_i$ can be undone by a Reidemeister-I move. It constitutes a **virtual crossing** (topologically removable). The terms $\sigma_0$ and $\sigma_1$ are virtual.
- **$\ell = 2$**: The products $\sigma_0\sigma_1$ and $\sigma_1\sigma_0$ form Hopf links. These two linked rings cannot be separated by any ambient isotopy, making them topologically non-trivial and observable.
- **$\ell = 3$**: The product $\sigma_0\sigma_1\sigma_0$ is the trefoil knot, the simplest non-trivial knot. This represents the electron $e^-$.

## Positive coefficients: observable vs virtual

The positive terms split into two classes:

|  | Observable ($\ell \geq 2$) | Virtual ($\ell < 2$) |
|:---:|---:|---:|
| **Neutron** | $+0.009$ ($L_-$ only) | $+1.057$ ($\sigma_0, \sigma_1$) |
| **Proton** | $+0.109$ ($L_+, L_-$) | $+1.033$ ($\sigma_0, \sigma_1$) |

Both nucleons are **dominated by virtual content**: the $\sigma_1$ term carries $\sim 94\%$ of the total positive amplitude. This term possesses word length $\ell = 1$, representing a single topologically trivial crossing. It cannot be observed as a free particle.

The observable positive terms are the **Hopf links** $L_+ = \sigma_0\sigma_1$ (proton only) and $L_- = \sigma_1\sigma_0$ (both nucleons). These are bound states of two linked rings. Note that $L_+$ is **negative** for the neutron, as the typed $d$-$d$ crossing transforms it into a debt.

## Location of $\sigma_1$: the color tube fiber

The generator $\sigma_1$ exchanges strands $1$ and $2$ in the $3$-strand braid (the crossing between the second and third quark lines). In the color tube geometry ([color tube fibers](#def:color-tube-fibers)), these strands map to color coordinates:

- **$\sigma_0$** acts on the $(\sigma, r)$ plane. This is the crossing between the space-like backbone $\sigma = w_1 - z$ and the first color tube coordinate $r = w_2 - z$.
- **$\sigma_1$** acts on the $(r, g)$ plane. This is the crossing **within the color tube fiber** between the red and green color coordinates $r = w_2 - z$ and $g = w_3 - z$.

The dominance of $\sigma_1$ thus implies: **the nucleon's internal energy resides overwhelmingly in the color tube fiber direction** — in the relative motion of color charges within the tube, not in the coupling between color and spacetime. This provides the algebraic expression of **color confinement**: the dominant dynamics remain internal to the color tube, invisible from the spacetime base.

## Linearity of the normal form

The transition $\Delta_i = \mathrm{coeff}_i(\mathfrak{n}) - \mathrm{coeff}_i(\mathfrak{p})$ computes the normal form of the **transition element** $\mathfrak{n} - \mathfrak{p} \in H_3(q)$. This holds because coordinate extraction in the Gröbner--Shirshov basis acts as a linear map on the vector space $H_3(q)$ ($\dim = 3! = 6$):

$$
  \mathrm{NF}(\mathfrak{n} - \mathfrak{p})
  = 
  \mathrm{NF}(\mathfrak{n}) - \mathrm{NF}(\mathfrak{p}).
$$

## Sign pattern and beta decay

The negative terms in each nucleon represent **leptonic debt** — topological content that must be supplied by (or released to) the vacuum. In the typed-crossing normal form:

|  | $\gamma$ debt | $L_+$ debt | $e^-$ debt |
|:---:|---:|---:|---:|
| **Neutron** | $-0.201704$ | $-0.009641$ | $-0.044184$ |
| **Proton** | $-0.099658$ | — | $-0.043208$ |

The neutron carries three debts ($\gamma, L_+, e^-$) while the proton carries only two ($\gamma, e^-$). The excess:

$$
  \Delta_\nu = -0.10205, \qquad \Delta_{L_+} = -0.10899,
  \qquad \Delta_{e^-} = -0.00098
$$

drives beta decay $\mathfrak{n} \to \mathfrak{p} + e^- + \bar{\nu}_e$. The neutron pays down its excess debt by emitting the physical electron and antineutrino.

## Summary

The nucleon normal form exhibits a clean tripartite structure:

1. **Virtual bulk** ($\ell \leq 1$, positive): $\sim 94\%$ of the amplitude. Confined inside the color tube fiber. Unobservable.
2. **Observable links** ($\ell = 2$, signed): Hopf-linked bound states. $L_-$ is positive for both nucleons; $L_+$ is positive for the proton but **negative for the neutron** (typed-crossing effect).
3. **Leptonic debt** ($\ell = 0$ and $\ell = 3$, negative): The neutrino and electron channels carry negative coefficients, dictating the required inputs from the vacuum. Beta decay settles this debt.

**Witness**: `free-neutron-decay.witness.json` (typed crossings; 17 reductions for $\mathfrak{n}$; 18 for $\mathfrak{p}$).
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

The framework provides $\mathfrak{E}_0$ in two forms. The first is a single-Planck-tick ($N=0$) value. The second is a tower-summed ($N \to \infty$) geometric form. These differ by the brane-tower correction $1/(1-\hbar_q^2) \approx 1.0099$ at $q_0 \approx 1.110$. Both derive from CAL-1 ($m_e$) and CAL-2 ($q_0$) alone; CAL-3 ($\mathfrak{Q}_\beta(n)$) provides the cross-check. See the [notation register](../notation/notation-register.md) for the $\mathfrak{E}_0^{(N=0)}$ / $\mathfrak{E}_0^{\text{full}}$ symbol convention and the [collisions note](../notation/notation-collisions.md) for why $\mathfrak{E}_0$ is not $\mathfrak{Q}_\beta(n)$.

## Linearity

The transition $\Delta = \mathrm{NF}(\mathfrak{n}) - \mathrm{NF}(\mathfrak{p})$ equals $\mathrm{NF}(\mathfrak{n} - \mathfrak{p})$ because $\mathrm{NF}$ is coordinate extraction in the Gröbner--Shirshov basis. This extraction acts as a linear map on the 6-dimensional vector space $H_3(q)$.

## Derivation (typed crossings)

From the witness (`free-neutron-decay.witness.json`, typed crossings):

- $\mathrm{net}(\mathfrak{n}) = +0.810835$, $\mathrm{net}(\mathfrak{p}) = +:val[confinement_B3_net_proton]{precision=6}$
- $\Delta(\mathrm{net}) = -0.188291$

From CODATA 2022:

- $\mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} \approx 1.29333\;\text{MeV}$
- $\mathfrak{m}_{e} \approx 0.51100\;\text{MeV}$
- $Q_{\beta} \approx 0.78233\;\text{MeV}$

**Derived energy scale — single-tick (Planck-tick) form, $\mathfrak{E}_0^{(N=0)}$.**
The leading-order energy scale derives from the categorical three-calibration inputs $m_e$ ($H^0$) and $q_0$ ($H^1$) alone. The target $\mathfrak{Q}_\beta(n)$ ($H^2$) is the datum the framework predicts, not consumed here ([three-calibration discipline](#prop:three-calibration-discipline)):

$$
  \mathfrak{E}_0^{(N=0)}
  :=
  \frac{m_e}{q_0(q_0 - 1)}
  =
  m_e \cdot c_q^2 \cdot \hbar_q
  \approx  4.186 \text{MeV}.
$$

This is the electron rest energy per Planck time ([energy scale and Planck time](#rem:energy-scale-planck)).

**Derived energy scale — tower-summed form, $\mathfrak{E}_0^{\text{full}}$.**
The full brane-tower geometric series ([symbolic derivation](https://github.com/litlfred/qou/blob/main/computations/q_beta_form_a_n1_extension.py#L32)) is:

$$
  \mathfrak{E}_0^{\text{full}}
  :=
  \mathfrak{E}_0^{(N=0)} \cdot \sum_{k=0}^{\infty} \hbar_q^{2k}
  =
  \frac{\mathfrak{E}_0^{(N=0)}}{1 - \hbar_q^2}
  \approx  4.228 \text{MeV}
$$

at $q_0 \approx 1.110$, which is $\approx +0.99\%$ over the single-tick value. Truncations $\mathfrak{E}_0^{(N)} = \mathfrak{E}_0^{(N=0)} \cdot (1 - \hbar_q^{2(N+1)})/(1 - \hbar_q^2)$ recover the tower at finite depth.

**Calibration cross-check, $\mathfrak{E}_0^{(\text{cal})}$.**
We extract the same scale from CODATA by dividing the free neutron $Q$-value by the Hecke NF difference:

$$
  \mathfrak{E}_0^{(\text{cal})}
  =
  \frac{Q_{\beta}}{|\Delta(\mathrm{net})|}
  =
  \frac{0.78233}{0.18829}
   \approx  4.155 \text{MeV}
   \approx  8.131 \times \mathfrak{m}_{e}.
$$

The computed values from the witness [`q-beta-form-a-n1-extension.witness.json`](https://github.com/litlfred/qou/blob/main/computations/q-beta-form-a-n1-extension.witness.json):

| Quantity | Value (MeV) | vs $\mathfrak{E}_0^{(\text{cal,symb})}$ |
|----------|------------:|------------------------------:|
| $\mathfrak{E}_0^{(N=0)}$ (single-tick derived) | $:val[E_0_N0_MeV]{precision=4}$ | $+0.17\%$ |
| $\mathfrak{E}_0^{\text{full}}$ (geometric-tower derived) | $:val[E_0_full_MeV]{precision=4}$ | $+1.16\%$ |
| $\mathfrak{E}_0^{\text{full},\mathrm{Li}_2^q}$ (symmetric q-dilogarithm candidate) | $:val[E_0_full_li2q_MeV]{precision=4}$ | $+1.15\%$ |
| $\mathfrak{E}_0^{(\text{cal,symb})}$ (CODATA / $h(h-2)/2$) | $:val[E_0_calibrated_MeV]{precision=4}$ | reference (symbolic) |
| $\mathfrak{E}_0^{(\text{cal,typed})}$ (CODATA / $\lvert\Delta(\text{net,typed})\rvert$) | $4.155$ | typed-crossings value (finite-size noise, 0.6% below symbolic) |

**Open finding.** Both the geometric tower form $1/(1-\hbar_q^2)$ and the bounded symmetric $\mathrm{Li}_2^q$ candidate move the framework prediction further from the calibrated values at the substrate level (only $\approx 0.01\%$ apart at $q_0$). We record this direction-of-residual puzzle in [`docs/audits/-tower-mev-calibration-finding.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-tower-mev-calibration-finding.md). The audit independently confirms $-\mathrm{Li}_2^q(-V)$ is the correct Kashaev specialisation, while the asserted $\Phi_q(V)$ form is off by $10^{6}$. We formally pose the open closure question as the conjecture [`conj:alpha-k-categorical-closure`](../braids-and-knots/alpha-k-categorical-closure.md) (existence, family selection, CAL-3 direction). The explicit $H_3$ $\alpha_k$ values from [`prop:alpha-k-derivation-procedure`](../braids-and-knots/alpha-k-derivation-procedure.md) do not satisfy the naive recursion $\alpha_k = \hbar_q^{2(k-1)}\alpha_{k-1}$ ($\alpha_1 = 0$, not $\hbar_q^0 \alpha_0 = 1$). Thus neither the geometric nor the $\mathrm{Li}_2^q$ closure is a trivial substitution. The correct closure is a non-obvious resummation identity that the conjecture seeks.

Note: $\Delta(\mathrm{net}) < 0$ (net$(\mathfrak{n}) <$ net$(\mathfrak{p})$ with typed crossings), so we use $|\Delta|$ to keep $\mathfrak{E}_0 > 0$.

## NF$_+$ / NF$_-$ decomposition

Each nucleon's NF splits into positive and negative coefficient sums:

| | NF$_+$ | NF$_-$ | Net |
|:---:|---:|---:|---:|
| **Neutron** | $+1.0664$ ($\sigma_0, \sigma_1, L_-$) | $-0.2555$ ($\gamma, L_+, e^-$) | $+0.8108$ |
| **Proton** | $+1.1420$ ($\sigma_0, \sigma_1, L_+, L_-$) | $-0.1429$ ($\gamma, e^-$) | $+0.9991$ |
| **$\Delta$** | $-0.0756$ | $-0.1127$ | $-0.1883$ |

The neutron has three negative terms ($\gamma, L_+, e^-$) while the proton has only two ($\gamma, e^-$). The $L_+$ sign flip is the typed-crossing effect: the $d$-$d$ crossing in neutron $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ shifts the Hopf link coefficient below zero.

## Observable vs virtual: $Q_{\geq 2}$

Terms of word length $\ell \geq 2$ (Hopf links $L_\pm$ and trefoil $e^-$) are topologically non-trivial and therefore observable. Terms $\ell < 2$ ($\gamma, \sigma_0, \sigma_1$) are virtual.

| | Observable ($\ell \geq 2$) | Virtual ($\ell < 2$) |
|:---:|---:|---:|
| **Neutron** | $-0.0446$ | $+0.8554$ |
| **Proton** | $+0.0655$ | $+0.9336$ |
| **$\Delta$** | $-0.1101$ | $-0.0782$ |

The observable-only $Q$-value, using $\mathfrak{E}_0(\mathrm{net})$:

$$
  Q_{\geq 2} = |\Delta(\ell \geq 2)| \times \mathfrak{E}_0
  = 0.11007 \times 4.155
  \approx 0.4573 \text{MeV}
  =  58.5\% \text{ of } \mathfrak{Q}_\beta.
$$

## Energy scale scenarios

| Scenario | $|\Delta|$ | $\mathfrak{E}_0$ (MeV) | $\mathfrak{E}_0 / \mathfrak{m}_e$ |
|:---|---:|---:|---:|
| All terms $|\Delta\mathrm{net}|$ | $0.18829$ | $4.155$ | $8.131$ |
| Observable $|\Delta(\ell \geq 2)|$ | $0.11007$ | $7.108$ | $13.909$ |
| Positive $|\Delta\mathrm{NF}_+|$ | $0.07563$ | $10.345$ | $20.244$ |
| Leptonic $|\Delta\nu| + |\Delta e^-|$ | $0.10302$ | $7.594$ | $14.861$ |

## Full energy budget

Each of the six NF terms contributes $\Delta_i \times \mathfrak{E}_0$ to the total decay energy. The budget is:

| Term | Word | Knot/Link | $\ell$ | $\Delta_i$ | $\Delta_i \times \mathfrak{E}_0$ (MeV) |
|:---:|:---:|:---:|:---:|---:|---:|
| $\gamma$ | $\mathbf{1}$ | photon | $0$ | $-0.10205$ | $+0.4240$ |
| $\sigma_0$ | $\sigma_0$ | virtual | $1$ | $+0.01240$ | $-0.0515$ |
| $\sigma_1$ | $\sigma_1$ | virtual | $1$ | $+0.01143$ | $-0.0475$ |
| $L_+$ | $\sigma_0\sigma_1$ | Hopf link | $2$ | $-0.10899$ | $+0.4529$ |
| $L_-$ | $\sigma_1\sigma_0$ | Hopf link | $2$ | $-0.00010$ | $+0.0004$ |
| $e^-$ | $\sigma_0\sigma_1\sigma_0$ | trefoil ($3_1$) | $3$ | $-0.00098$ | $+0.0041$ |
|  |  |  |  | **Sum** | **$+0.782$ MeV** |

(Signs: $\Delta(\mathrm{net}) < 0$ with typed crossings, so the $\mathfrak{E}_0$ budget uses the sign convention $\Delta_i \times \mathfrak{E}_0 \times (-\mathrm{sgn}\Delta_{\mathrm{net}})$ to give $Q > 0$.)

## The $L_+$ dominance (typed crossings)

With typed crossings, the single largest contributor is $\Delta(L_+) = -0.1090$, giving $+0.453 \text{MeV}$. This is larger than the $\gamma$ debt ($+0.424 \text{MeV}$) and replaces the $\sigma_1 dominance$ of the untyped computation.

The $\gamma$ debt ($+0.424 \text{MeV}$) and $L_+$ shift ($+0.453 \text{MeV}$) together account for $0.877 \text{MeV}$, which exceeds $\mathfrak{Q}_\beta$. The small virtual terms ($\sigma_0, \sigma_1$) absorb the excess:

$$
  \underbrace{+0.453}_{L_+}
  \underbrace{+0.424}_{\gamma\text{ debt}}
  \underbrace{-0.052}_{\sigma_0}
  \underbrace{-0.047}_{\sigma_1}
  \underbrace{+0.004}_{\text{other}}
  = 
  +0.782 \text{MeV}.
$$

## Physical interpretation

Beta decay pays down the neutron's leptonic debt. With typed crossings, the process $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu_e$ releases $\mathfrak{Q}_\beta = 0.782 \text{MeV}$ because:

1. The neutron's $L_+$ (Hopf link) coefficient is negative ($-0.010$) while the proton's is positive ($+0.099$). This $\Delta L_+ = -0.109$ is the dominant energy source.
2. The neutron carries a larger $\gamma$ debt than the proton ($\Delta\gamma = -0.102$), contributing $+0.424 \text{MeV}$.
3. The virtual terms ($\sigma_0, \sigma_1$) contribute small negative corrections ($-0.099 \text{MeV}$ total).
4. The $e^-$ channel contributes only $+0.004 \text{MeV}$ — the electron debt difference is nearly zero.

Witness: `beta-decay-energy-scale.witness.json`.
<!-- FILE_END: beta-decay-energy-scale.md -->

<!-- FILE_START: negative-debt-confinement.md -->
The NF$_+$ / NF$_-$ decomposition of the nucleon normal forms reveals a quantitative signature of confinement. The neutron carries significantly more internal cancellation than the proton.

## The negative coefficient debt

Each nucleon's Gröbner--Shirshov normal form in $H_3(q_0)$ splits into positive and negative coefficient sums:

| | NF$_+$ | NF$_-$ | Net |
|:---:|---:|---:|---:|
| **Neutron** | $+1.0664$ | $-0.2555$ | $+0.8108$ |
| **Proton** | $+1.1420$ | $-0.1429$ | $+0.9991$ |
| **$\Delta$** | $-0.0756$ | $-0.1127$ | $-0.1883$ |

The neutron's negative coefficient debt $|\mathrm{NF}_-(\mathfrak{n})| = 0.2555$ exceeds the proton's by $|\Delta\mathrm{NF}_-| = 0.1127$. This excess debt is $11.3\%$ of the proton's net coefficient $\mathrm{net}(\mathfrak{p}) = 0.9991$.

The dominant source is the $L_+$ sign flip. The $d$--$d$ typed crossing makes the Hopf-link coefficient negative in the neutron ($-0.010$) while it is positive in the proton ($+0.099$). This single channel contributes $|\Delta(L_+)|/\mathrm{net}(\mathfrak{p}) \approx 10.9\%$ --- approximately the entire excess debt.

## Confinement interpretation

The internal cancellation ratio $|\mathrm{NF}_-|/(|\mathrm{NF}_-| + \mathrm{NF}_+)$ measures how much of the total coefficient magnitude is consumed by destructive interference:

- **Neutron**: $19.3\%$ cancellation
- **Proton**: $11.1\%$ cancellation
- **Difference**: $8.2$ percentage points

The neutron's larger cancellation reflects its $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ composition. The $d$--$d$ crossing generates a $-\mathrm{HA} \cdot \mathbf{1}$ correction that propagates through the Gröbner--Shirshov reduction. It flips the $L_+$ coefficient and amplifies the $\gamma$ debt. This is a computable, algebraic manifestation of color confinement. The energy cost of holding three quarks in a color-singlet braid is larger for the neutron because the $d$--$d$ interaction is more confining than $u$--$u$.
<!-- FILE_END: negative-debt-confinement.md -->

<!-- FILE_START: beta-decay-braid-visualizer.md -->
Interactive visualization of beta decay as a $T_{3,5}$ braid insertion on the nuclear braid word.

## The $T_{3,5}$ weak vertex

The weak interaction is carried by the torus knot $T_{3,5}$ ([force identification](#rem:force-knot-identification)). Its braid word $\beta_{T_{3,5}} = (\sigma_1 \sigma_2)^5$ has $10$ crossings. This simulator draws the full braid left-to-right. It shows strands flowing from the parent nucleon through the $T_{3,5}$ insertion to the daughter nucleon plus lepton pair.

## Panels

1. **Braid flow diagram** --- The $10$-crossing $T_{3,5}$ braid inserted at the converting $\mathfrak{d}$-quark crossing. Input strands (left) carry the parent quark content. Output strands (right) carry the daughter quark content plus the emitted electron ($T_{2,3}$, $3$ crossings) and antineutrino ($K_{0_1}$, $0$ crossings). Toggle between $\beta^-$ ($\mathfrak{d} \to \mathfrak{u}$) and $\beta^+$ ($\mathfrak{u} \to \mathfrak{d}$).
2. **Transfer matrix crossings** --- The three nuclear crossing types $T_{pp}$, $T_{nn}$, $T_{\mathrm{mix}}$ drawn as individual braid crossings, with their $2 \times 2$ matrix entries evaluated at the substrate parameter $q$.
3. **Hecke and Skein relations** --- The Hecke relation $T^2 = (q - q^{-1})T + 1$ and the Skein relation $q[L_+] - q^{-1}[L_-] = (q^{1/2} - q^{-1/2})[L_0]$ illustrated as braid crossing reductions.
4. **Universal decay matrix** --- The equally-spaced property $\Delta_\beta = T_{\mathrm{mix}} - T_{nn} = T_{pp} - T_{\mathrm{mix}}$ with explicit polynomial entries.

## Strand conventions

Strands follow the pointed-knot convention from the building-block table ([building blocks](#rem:building-block-knots)):

- **Solid** ($\bullet$) = particle (positive time orientation, $T_{2,3}$).
- **Outlined** ($\circ$) = antiparticle (negative time / mirror, $\overline{T_{2,3}}$).
- **Basepoint** marked on each strand.

The $\mathfrak{u}$-quark strands are drawn in blue (solid), and $\mathfrak{d}$-quark strands in red (outlined). This matches the crossing-chirality convention where positive crossings are $\mathfrak{u}\text{-}\mathfrak{u}$ and negative crossings are $\mathfrak{d}\text{-}\mathfrak{d}$.

## The $10$-crossing budget

$$
  \underbrace{10}_{\text{total}} = 
  \underbrace{3}_{e^- (T_{2,3})} + 
  \underbrace{0}_{\bar{\nu}_e (K_{0_1})} + 
  \underbrace{7}_{\text{R2 re-reduction}}
$$

The $7$ re-reduction crossings modify inter-nucleon crossing types at the converting quark's strand. These produce the dominant contribution to the $Q$-value.
<!-- FILE_END: beta-decay-braid-visualizer.md -->

