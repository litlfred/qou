<!-- FILE_START: qbeta-formalize-first-gates-intro.md -->
The Hoefsmit He-4 channel fixes the selector direction as a single Markov-trace collapse, $T_\beta = S\cdot\mathbf{1}$ ([`prop:t-beta-markov-frobenius-collapse`](#prop:t-beta-markov-frobenius-collapse)). This collapse leaves one object to identify: the fibre-level Habiro element $F(q)$ whose $q$-Taylor coefficients provide the precision-ladder $c_k$ of the $\mathfrak{Q}_\beta$ series (`sec:mass-algebraic-complex-volume-ladder`). This section determines the structural constraints any candidate $F$ must satisfy before evaluation. It applies formalize-first discipline to the decay side: we prove the invariants that prune the hypothesis class, then search the survivors.

Four gates prune the candidates. The generating function must possess a pole at the substrate radius ([`prop:q-beta-radius-of-convergence-gate`](#prop:q-beta-radius-of-convergence-gate)). It must be bar-even under $q\mapsto q^{-1}$ to yield a clean integer-$u$ ladder ([`prop:q-beta-bar-even-kernel-invariant`](#prop:q-beta-bar-even-kernel-invariant)). It must reproduce the classical shadows $c_2\to-1$ and $c_3\to J_{\mathrm{Hopf}}(1)=-2$ at $q=1$ ([`prop:q-beta-q-eq-one-shadow-gate`](#prop:q-beta-q-eq-one-shadow-gate)). It must carry a magnitude consistent with the target observable ([`prop:q-beta-direction-sanity-gate`](#prop:q-beta-direction-sanity-gate)). These four gates bundle into one parametric typeclass ([`prop:q-beta-bar-even-kernel-typeclass`](#prop:q-beta-bar-even-kernel-typeclass)). We assemble the mass-side analogue alongside it ([`prop:mass-side-kernel-formalize-first-gates`](#prop:mass-side-kernel-formalize-first-gates)).

Between the gates sits the recursion machinery. The $c_k$ inherit a depth-$d$ linear recursion from the Habiro $q$-difference kernel ([`prop:q-beta-c-k-recursion-from-habiro-q-difference`](#prop:q-beta-c-k-recursion-from-habiro-q-difference)). The bridge connects this to the per-block $z$-recursion ([`prop:qbeta-z-recursion-to-ck-recursion-bridge`](#prop:qbeta-z-recursion-to-ck-recursion-bridge)). Exact rational forms emerge at the silver ratio ([`prop:qbeta-c8-c10-silver-rationals`](#prop:qbeta-c8-c10-silver-rationals)).

The gates determine which coefficients are structural and which remain calibration-anchored. The seed $c_2=-1$ is Taylor-exact. The term $c_3\approx-2$ is a near-match. The terms $c_k$ for $k\ge4$ fit to the CODATA residual. The $c_k$ remain cal-anchored here. We defer the categorical construction of $F(q)$ to the brane-tower limit, where the binding $\Delta_\lambda$ ladder lives. Any future $F$ failing a gate is excluded without a canonical search.
<!-- FILE_END: qbeta-formalize-first-gates-intro.md -->

<!-- FILE_START: toroidal-harmonics-delta-lambda.md -->
# Toroidal Harmonics and the $\Delta_\lambda$ Mass Gap

Bridging the mass calculation from the canonical base $m_{\text{can}}$ to the AME2020 experimental frontier requires resolving the $\Delta_\lambda$ normalization shift (the shell-filling fraction $c_\lambda$).

## The Toroidal JSJ Equivalence

The Markov parameter recursion $c_k$ drives the strong-force topological trace. It constitutes a discrete evaluation of the knot complement's toroidal structure.

Let $q = e^{-\eta}$. The Markov parameter $z(q) = \frac{\sqrt{q}}{1+q}$ is equivalently parametrised by $w = z^2 = \frac{1}{2(\cosh\eta + 1)}$. Under the change of variables $x = \cosh\eta = \frac{1}{2w} - 1$, the continuous Legendre differential equation for the Toroidal Harmonics of half-integer degree $n-1/2$:

$$ (1 - x^2) y'' - 2x y' + (n^2 - 1/4) y = 0 $$

reduces exactly to the polynomial generating function ODE of the $z$-recursion:

$$ 4w^2(4w - 1) f'' + 16w^2 f' + (4n^2 - 1) f = 0 $$

This explicit map establishes that the topological evaluation $B_{\text{sym}}$ is the discrete shadow of the Toroidal JSJ decomposition. Evaluating $P_{n-1/2}^m(\cosh\eta)$ over the SU(4) Plancherel measure resolves the missing normalization factor $\Delta_\lambda$ for heavy nuclei analytically.

## The Golden Ratio Anchor for $\Delta_\lambda$

The toroidal ratio $P_{-1/2}/P_{1/2}$ drives the scaling gap $c_\lambda$. Setting the topological boundary condition to the known TQFT Fibonacci anyon root $q_0 = 1/\phi = \frac{\sqrt{5}-1}{2}$ fixes the geometric coordinate to $\cosh \eta = \frac{\sqrt{5}}{2} \approx 1.1180$.

Evaluating the toroidal harmonics at this geometric anchor yields:

$$ c_\lambda^{\text{topological}} = \frac{P_{-1/2}\left(\frac{\sqrt{5}}{2}\right)}{P_{1/2}\left(\frac{\sqrt{5}}{2}\right)} \approx 0.944649 $$

This parameter-free constant matches the empirical macroscopic shell-filling fraction for ${}^4\text{He}$ ($c_\lambda^{\text{exp}} \approx 0.943503$) to within $0.1\%$. The residual difference stems from higher-order entanglement terms beyond the 2-row stratum.
<!-- FILE_END: toroidal-harmonics-delta-lambda.md -->

<!-- FILE_START: q-beta-over-e0-classical-vanishing.md -->
*Let $\mathfrak{Q}_\beta(q)$ and $E_0^{(N{=}0)}(q)$ be the substrate closed forms from [`prop:neutron-qvalue-symbolic`](neutron-qvalue-symbolic.md) and [`rem:beta-decay-energy-scale`](beta-decay-energy-scale.md):*

$$
\mathfrak{Q}_\beta(q) \;=\; m_e \cdot \frac{(2q + 1 - q^2)(q+1)}{2q^3},
\qquad
E_0^{(N=0)}(q) \;=\; \frac{m_e}{q(q-1)}.
$$

*The ratio*

$$
S(q) \;\coloneqq\; \frac{\mathfrak{Q}_\beta(q)}{E_0^{(N{=}0)}(q)} \;=\; \frac{(2q + 1 - q^2)\,(q^2 - 1)}{2 q^2}
$$

*satisfies $S(q = 1) = 0$ as an algebraic identity over any commutative ring.*

The shape-collapse audit states that $c_k$ comes from the $u_{\text{ladder}}$ Taylor expansion of $S(q) = \mathfrak{Q}_\beta(q)/E_0(q)$. Taken literally, this is degenerate. The Taylor expansion of $S/S(1)$ around $q = 1$ is $0/0$. The proved $c_2 = -1$ cannot be recovered this way.

The term $S = \mathfrak{Q}_\beta / E_0$ is the SDP-constraint scalar (canonical at $q_0$, matching the affine target $n_{\text{target}} = S(q_0) \approx 0.18689$). The $c_k$ ladder normalization is $\mathfrak{Q}_\beta / [Q_A \cdot \cos(\alpha_{\text{eff}})]$, with $Q_A$ and $\alpha$ read from the operator-valued $N{=}3$ witness. This proposition exposes the algebraic obstruction that identifies the missing categorical input ($Q_A(q)$ and $\alpha(q)$).

The vanishing $S(1) = 0$ provides the direct-algebraic witness. An operator-theoretic witness arrives from the SDP strict-complementarity analysis. Both routes converge: the bare substrate scale $Q_A$ predicts $\mathfrak{Q}_\beta$ to $0.168\%$ without CODATA input. The sub-ppb correction is the $c_k$ ladder. Its normalization is not $S = \mathfrak{Q}_\beta/E_0$.
<!-- FILE_END: q-beta-over-e0-classical-vanishing.md -->

<!-- FILE_START: qbeta-c8-c10-silver-rationals.md -->
*At the silver ratio $q = 1 + \sqrt{2}$, the Hoefsmit parameter is $b^2 = 7/8$. The closed-form $\mathfrak{Q}_\beta$ precision-ladder coefficients $c_8$, $c_9$, $c_{10}$ extend the Pell-Lucas $\sigma$-action pattern:*

$$
  c_8 = c_3^2 \cdot b^4 = \tfrac{49}{16}, \qquad
  c_9 = c_3^3 \cdot b^2 = -7, \qquad
  c_{10} = c_3^2 \cdot b^6 = \tfrac{343}{128}.
$$

*Each value matches the Pell-Lucas-clean prediction recorded in the SDP-extraction witness. Each constitutes a pure $\sigma$-action rung with no averaging-resonance $\tfrac{1}{2}$ fingerprint.*

The Pell-Lucas-clean classification at the silver ratio signals the structure of the $\mathfrak{Q}_\beta$ $c_k$ precision ladder. The $c_k$ values extracted at $q_0$ become noise-dominated for $k \geq 8$. The silver ratio exposes the algebraic structure. These three closed forms extend the $c_4 = c_3 \cdot b^4$, $c_6 = c_3^2 \cdot b^2$, $c_7 = c_3^3$ pattern.

The formalization provides three pure-rational identities closed by `norm_num`. The silver-ratio $b^2 = 7/8$ serves as a rational constant. The identities hold over any field containing $\mathbb{Q}$ and are specialized here to the silver-ratio rational point. They remain fibre-level Laurent rationals.
<!-- FILE_END: qbeta-c8-c10-silver-rationals.md -->

<!-- FILE_START: q-beta-c-k-recursion-from-habiro-q-difference.md -->
*Let $F(q) \in \mathbb{Z}[q, q^{-1}]^\wedge$ be a fibre-level Habiro element associated to the operator-valued $T_\beta$ selection ([`prop:t-beta-markov-frobenius-collapse`](t-beta-markov-frobenius-collapse.md)). Let $F(q)$ satisfy a $q$-difference equation of depth $d$:*

$$
F(q\xi) \;=\; R(q,\xi)\cdot F(\xi), \qquad R(q,\xi) \in \mathbb{Q}(q)[\xi, \xi^{-1}] \text{ of degree} \le d.
$$

*The precision-ladder coefficients $c_k$ satisfy a depth-$d$ linear recursion:*

$$
c_{k+1} \;=\; \sum_{j=1}^{d} a_j(q_0)\cdot c_{k+1-j}, \qquad a_j(q_0) \in \mathbb{Q}(q_0),
$$

*with kernel coefficients $\{a_j\}$ extracted from $R(q_0, \xi)$ via the $(u;u)_m \to u^k$ Habiro change-of-basis.*

The operator content is $T_\beta = S \cdot \mathbf{1}$, with $S$ pinned by the SDP constraint. The selector direction is $S$-independent and $q$-rational. The scalar $S = \mathfrak{Q}_\beta/E_0$ is not the ladder normalization. Together, these define $F(q) = \mathfrak{Q}_\beta(q)/[Q_A(q) \cdot \cos(\alpha_{\mathrm{eff}}(q))]$ as a single fibre-level Habiro object. Its $q$-difference structure generates the $c_k$.

The sequence $c_2, \ldots, c_8$ collapses to the proved seed $c_2 = -1$ and a kernel $R(q_0, \xi)$ of bounded degree $d$. The recursion generates $c_3, \ldots, c_8$ automatically.

We write the recursion coefficients as elementary symmetric polynomials $a_j = e_j(\{r_\lambda\})$ of the per-mode rates $r_\lambda = (q-1)\mu_\lambda$. Under the bar involution $q \mapsto q^{-1}$, the rates are bar-odd. We formally prove that $a_j$ alternates bar-parity. The recursion step and the parity-alternation theorem form the structural law behind the ladder's parity bookkeeping.

The cyclotomic factors $\Phi_d$ for $d \in \{2,3,6\}$ and for all primes $p$ are self-reciprocal. Divisibility by $\Phi_n$ is invariant under the bar involution for every $n > 1$. The identity $\Phi_n(1/q)\,q^{\varphi(n)} = \Phi_n(q)$ guarantees period-3 closure.

The Habiro element $F(q)$ is the trace of the $q$-heat kernel over the Hecke modules:

$$Z_q(t) = \sum_{\lambda \in \Lambda} d_\lambda(q) \cdot \exp_q(-\mu_\lambda(q) \cdot t).$$

The $q$-difference equation for $F(q)$ derives from the depth-1 Jackson equations of each mode. The net partition function satisfies a $q$-difference equation of depth $|\Lambda|$. The $c_k$ coefficients are extracted at $q_0$.

At the fibre level, $Z_q$ is a Hahn--Exton q-Bessel function. The coefficients $c_k$ obey the q-Bessel second-order q-difference equation. This identification applies at the fibre level only. Archimedian closure of $c_3$ via a substrate-fixed q-Bessel is refuted. The q-Bessel object lives in the brane-tower limit.
<!-- FILE_END: q-beta-c-k-recursion-from-habiro-q-difference.md -->

<!-- FILE_START: q-beta-c-k-recursion-from-habiro-q-difference-interpretation.md -->
**Remark (quantum-modularity of the bar-involution).**
Conjecturally, the bar-involution $q\mapsto q^{-1}$ serves as the fibre-level avatar of the quantum-modular $S$-transform $q\mapsto\tilde q$. The Kashaev asymptotics near roots of unity are quantum modular. Under this reading, the bar-odd requirement on $a_1$ represents the odd part under the $S$-transform, and the $\sqrt{u}$ prefactor represents the radial asymptotic. This remains a motivated analogy, not a theorem.
<!-- FILE_END: q-beta-c-k-recursion-from-habiro-q-difference-interpretation.md -->

<!-- FILE_START: q-bessel-c-k-recurrence-cfinite.md -->
**Proof.** The power-series coefficients $c_k$ of the $q$-Bessel function satisfy a first-order ($C$-finite / $q$-holonomic) recurrence. The closed-form coefficient `QOU.QBeta.qbessel_coeff_closed_form` and the recurrence are proved sorry-free algebraically in $q$. This provides the fibre-level skeleton of the recursion; the production $c_k$ ladder remains calibration-anchored.
<!-- FILE_END: q-bessel-c-k-recurrence-cfinite.md -->

<!-- FILE_START: q-bessel-second-order-qdifference.md -->
**Proof.** The $q$-Bessel function satisfies a second-order $q$-difference equation. The equation and the recurrence it induces are established formally and verified computationally. The second-order recurrence `QOU.QBeta.qbessel_second_order_recurrence` is proved sorry-free algebraically in $q$. This is a fibre-level structural result.
<!-- FILE_END: q-bessel-second-order-qdifference.md -->

<!-- FILE_START: jackson-q-bessel-contiguity-recurrence.md -->
Let $J_\nu^{(1)}(x;q)$ and $J_\nu^{(2)}(x;q)$ be Jackson's first- and second-kind $q$-Bessel functions. Their power-series coefficients satisfy purely algebraic first-order contiguity recurrences in the order $\nu$. The recurrence is algebraic in the formal deformation variable $q$. The $q$-weights are adapted to the $SU_q(1,1)$ Casimir invariants. This fibre-level identity fixes the radial coefficient algebra without fixing the binding scale.
<!-- FILE_END: jackson-q-bessel-contiguity-recurrence.md -->

<!-- FILE_START: jackson-q-bessel-contiguity.md -->
**Proof.** The first- and second-kind Jackson $q$-Bessel functions have power-series coefficients $c_k$ satisfying purely algebraic first-order contiguity recurrences in $\nu$. The closed forms are proved in `QBesselContiguityRecurrence.lean`. Computations verify the ratios symbolically and numerically. This formal-$q$ structural identity fixes the $SU_q(1,1)$ radial coefficient algebra.
<!-- FILE_END: jackson-q-bessel-contiguity.md -->

<!-- FILE_START: qbeta-c4-from-c3-c8-product-identity.md -->
*The coefficients $c_3$, $c_4$, $c_8$ satisfy the structural product identity:*

$$
  c_8 \;=\; c_3 \cdot c_4 \qquad (\text{symbolic in } b, \text{ exact } \forall b).
$$

*At the silver ratio $q = 1+\sqrt{2}$, where $c_3 = -2$, $c_4 = -49/32$, and $c_8 = 49/16$, this evaluates to the $\mathbb{Q}$-rational identity $(-2) \cdot (-49/32) = 49/16$. Consequently, $c_4 = c_8 / c_3 = -2 \cdot b^4$ is derived from $c_3$ and $c_8$.*

The Pell-Lucas linear recursion does not close the gap between $c_4$ and $c_5, c_6, c_7$. This proposition closes the gap via a multiplicative product law. The identities $c_3 \cdot c_4 = c_8$ and $c_3 \cdot c_6 = c_9$ hold algebraically. Applying the $J_{\mathrm{Hopf}}$ Markov-trace twist $c_3 = -2$ to $c_4$ yields $c_8$. If this follows from a categorical theorem, then $c_4$ is forced by $c_3$ and $c_8$.

The identities are stated as Laurent polynomials in $b$ and verified at the silver-ratio rational anchor in $\mathbb{Q}$. The Lean proofs use `norm_num` pure rational arithmetic. Until the upstream $c_8$ categorical proof lands, $c_4$ holds empirical tier.
<!-- FILE_END: qbeta-c4-from-c3-c8-product-identity.md -->

<!-- FILE_START: qbeta-z-recursion-to-ck-recursion-bridge.md -->
*For any `ZRecursionCoeffs` instance with Taylor coefficient sequence $a_n$, and for $n \geq 1$,*

$$
  a_{n+1} = -\frac{3n}{2(n+1)} \cdot a_n -\frac{2n-1}{4(n+1)} \cdot a_{n-1}.
$$

*The coefficients $a_n$ are real. The forward form is stated over $\mathbb{R}$.*
<!-- FILE_END: qbeta-z-recursion-to-ck-recursion-bridge.md -->

<!-- FILE_START: qbeta-odd-carrier-hopf-cubic.md -->
**Remark (why the $\mathfrak{Q}_\beta$ odd channel resists a real-$q$ closure).**
The precision-ladder coefficient $c_3$ splits under the bar involution
$q \mapsto q^{-1}$ into a bar-even part (exactly measured) and a bar-odd part,
the latter being the open channel. Its carrier is the bar-odd part of the net
decay-width Laurent polynomial $\Delta_{\mathrm{net}} = \Delta(\mathfrak{n}) - \Delta(\mathfrak{p})$
on the $\mathbf{H}_3$ normal-form basis, whose numerator over $4q^7$ is

$$
\mathrm{num}(q) = q^{14} - 5q^{12} + 10q^{10} - 16q^{8} + 16q^{6} - 10q^{4} + 5q^{2} - 1.
$$

**The cyclotomic content is trivial and the residue is a cubic.** Exactly,
$\mathrm{num}(q) = (q^2 - 1)\,R_{12}(q)$, so the only cyclotomic factor is
$\Phi_1 \Phi_2 = q^2 - 1$; the fourth cyclotomic polynomial $\Phi_4 = q^2 + 1$
does **not** divide $\mathrm{num}$ (it leaves the nonzero remainder $-64$, i.e.
$\mathrm{num} = -64$ at $q = i$). The residue $R_{12}$ is even and palindromic,
collapsing in the bar-even loop-trace variable $y = q^2 + q^{-2} = 2\cosh 2\lambda$ to

$$
R_{12}(q) = q^{6}\,C(y), \qquad C(y) = y^3 - 4y^2 + 3y - 2.
$$

$C$ is irreducible over $\mathbb{Q}$ (its only possible rational roots $\pm 1, \pm 2$
are all nonzero), so its root generates a genuine **degree-3 field**
(discriminant $-152 = -2^3 \cdot 19$, Galois group $S_3$). Every substrate
*quadratic* anchor sits at a rational trace value — golden $\varphi \mapsto y = 3$,
silver $1 + \sqrt{2} \mapsto y = 6$, classical $q = 1 \mapsto y = 2$ — and $C$ is
nonzero at each. A degree-$\le 2$ number can never be a root of an irreducible
cubic, so **no quadratic-anchor or real-$q$ construction can reproduce the odd
carrier**: this is the structural reason the real-$q$ $c_3$ closures fail.

**The degree-3 comes from the Hopf (double-crossing) sector.** Decomposing the
bar-odd carrier over the knot sectors of the $\mathbf{H}_3$ normal form isolates
the origin of the cubic:

| knot sector | crossings | bar-odd contribution in $y$ |
|---|---|---|
| virtual ($\sigma_0, \sigma_1$) | 1 | $0$ |
| trefoil ($\sigma_0\sigma_1\sigma_0$) | 3 | $0$ |
| unknot ($\mathbf{1}$) | 0 | $C_{\mathrm{unknot}}(y) = 2y^2 - 7y + 4$ |
| Hopf ($\sigma_0\sigma_1 + \sigma_1\sigma_0$) | 2 | $C_{\mathrm{Hopf}}(y) = y^3 - 6y^2 + 10y - 6$ |

with $C = C_{\mathrm{Hopf}} + C_{\mathrm{unknot}}$. The odd-crossing sectors
(virtual, trefoil) are bar-even and vanish; the identity contributes only a
quadratic; the **cubic — hence the degree-3 field — is sourced entirely by the
Hopf-link (double-crossing) sector**. $C_{\mathrm{Hopf}}$ is itself irreducible
(discriminant $-76 = -2^2 \cdot 19$), and the prime $19$ is the arithmetic
fingerprint shared with the total $C$. So the obstruction is not a
$3$-dimensional representation ($\mathbf{H}_3$ has none — its Wedderburn blocks
are $1, 2, 1$) nor a single knot invariant, but the two-crossing isospin
amplitude difference. Any genuine odd-channel closure must supply the cubic
field of $C_{\mathrm{Hopf}}$, routed through the archimedean evaluation of the
Markov crossing term, rather than a fibre-level real-$q$ formula.
<!-- FILE_END: qbeta-odd-carrier-hopf-cubic.md -->

<!-- FILE_START: q-beta-c-2-eq-neg-one-structural.md -->
*In the $\mathfrak{Q}_\beta$ precision-ladder factorisation,*

$$
\mathfrak{Q}_\beta(q) \;=\; Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q)) \cdot \prod_{k \ge 2} \bigl(1 + c_k \cdot u_{\text{ladder}}^k\bigr), \qquad u_{\text{ladder}} = b(q) \cdot \hbar_q^2,
$$

*the $k = 2$ coefficient satisfies $c_2 = -1$ as a structural identity over any commutative ring.*

The canonical observation $c_2 \approx -1$ is not an empirical fit. It is the exact coefficient of $u_{\text{ladder}}^2$ in the algebraic factorisation of the categorical $N{=}2$ ladder correction. The identity holds in any commutative ring, independent of $q_0$ and CODATA. The sympy verification simplifies the factor and obtains exactly $0$.

With $c_2 = -1$ structurally locked, the partial ladder $Q_{N=2}(q_0)$ evaluates to within $5.6\,\text{ppm}$ of $\mathfrak{Q}_\beta^{\text{CODATA}}$ with zero CODATA input. The remaining $\sim 6\,\text{ppm}$ sets the categorical target for $c_3$ and $c_4$. Testing exact structural matches for $c_3$ discriminates between brane-tower truncation schemes.
<!-- FILE_END: q-beta-c-2-eq-neg-one-structural.md -->

<!-- FILE_START: q-beta-bar-even-kernel-invariant.md -->
*In the $\mathfrak{Q}_\beta$ ladder $R(u) := \prod_k(1 + c_k u^k)$ with $u = b(q) \cdot \hbar_q^2$, the ladder admits a clean integer-$u$ Taylor representation if and only if $R$ is bar-even (an even function of $t := q - 1$ about $q = 1$).*

The substrate variable $u$ has a double zero at $q = 1$. Under $q \mapsto q^{-1}$, $t \mapsto -t + O(t^2)$. If $R$ is even in $t$, the $u$-grading absorbs the coefficients, avoiding a $\sqrt{u}$ branch. If $R$ has odd-in-$t$ content, the reversion picks up a $\sqrt{u}$ branch, making the scalar extraction singular.

This is the formalize-first gate for the bar-even invariant. We state the candidate as a power series in $t$. We compute $R(q^{-1}, \xi^{-1})$ and subtract. A non-zero difference refutes the candidate structurally.
<!-- FILE_END: q-beta-bar-even-kernel-invariant.md -->

<!-- FILE_START: q-beta-radius-of-convergence-gate.md -->
*In the $\mathfrak{Q}_\beta$ precision-ladder factorisation, the log-correction generating function $g(u) := \sum c_k u^k$ has a simple pole at $u = u_{\text{substrate}} \approx 0.00852$. Any candidate Habiro element $F(q)$ whose generating function has its nearest singularity elsewhere is structurally REFUTED.*

This provides the anchor-stable formalize-first gate. The simple-pole location is anchor-stable. A candidate is rejected if the ratio $|u_0 - u_{\text{substrate}}| / u_{\text{substrate}}$ exceeds $10^{-6}$.
<!-- FILE_END: q-beta-radius-of-convergence-gate.md -->

<!-- FILE_START: q-beta-q-eq-one-shadow-gate.md -->
*Any candidate Habiro element $F(q)$ generating the $\mathfrak{Q}_\beta$ ladder must satisfy the classical-limit shadows $\lim_{q \to 1} c_2(q) = -1$ and $\lim_{q \to 1} c_3(q) = -2$. A candidate failing either shadow is structurally REFUTED.*

This enforces the $q=1$ shadow formalize-first gate. The seed $c_2 = -1$ is Taylor-exact. The term $c_3 \to -2$ is the canonical Hopf-Jones limit. A candidate whose Taylor expansion disagrees with either anchor fails this invariant.
<!-- FILE_END: q-beta-q-eq-one-shadow-gate.md -->

<!-- FILE_START: q-beta-direction-sanity-gate.md -->
*Any candidate Habiro element $F(q)$ must satisfy the direction-sanity invariant: $|F(q_0)|$ must be in the same order of magnitude as the target ratio $\mathfrak{Q}_\beta^{\text{CODATA}} / [Q_A(q_0) \cdot \cos(\alpha_{\text{eff}}(q_0))]$. A candidate predicting a magnitude differing by more than $10\times$ is structurally REFUTED.*

This implements the formalize-first magnitude check. At $q_0$, the target magnitude is $\approx 1$. A candidate yielding a magnitude wildly different from 1 is automatically refuted on paper before compute.
<!-- FILE_END: q-beta-direction-sanity-gate.md -->

<!-- FILE_START: q-beta-c-k-leading-bias-correction-identity.md -->
*Let $\hat c_k$ be the joint-fit extraction at $u_0 = b(q_0) \cdot \hbar_{q_0}^2$. Let $c_k^{\mathrm{alg}}$ be the algebraic coefficients. If the extraction bias is leading-order linear in $u_0$, the bias-corrected values $\hat c_k^{\mathrm{corr}} := \hat c_k - \hat c_{k+1} \cdot u_0$ satisfy $\hat c_k^{\mathrm{corr}} = c_k^{\mathrm{alg}} + O(u_0^2)$.*

The $+1.71\%$ relative bias on the extracted $\hat c_2$ matches the structural signature $c_3^{\mathrm{alg}} \cdot u_0$. This agreement validates the generating-function hypothesis. Correcting $\hat c_3$ yields $-1.9999968$, consistent with $c_3 = -2$. The proposition mechanically inverts the bias in Lean.
<!-- FILE_END: q-beta-c-k-leading-bias-correction-identity.md -->

<!-- FILE_START: q-beta-bar-even-kernel-typeclass.md -->
*The `BarEvenKernel` Lean typeclass bundles all four formalize-first invariants for $F(q)$ into a single parametric type. Instantiating `BarEvenKernel` is equivalent to clearing all four gates simultaneously.*

This bundles the anchor-stable, bar-even, $q=1$ shadow, and direction-sanity checks into a single step for Lean. It operationalises the pre-flight checklist. The bar-even invariant is a structural identity in `CommRing R`. The composition theorem lifts the bundle into the individual gate classes.
<!-- FILE_END: q-beta-bar-even-kernel-typeclass.md -->

<!-- FILE_START: mass-side-kernel-formalize-first-gates.md -->
*The `MassSideKernel` Lean typeclass bundles the mass-theory analogs of the four formalize-first invariants for any candidate `linking_weight` function $w(q)$. Instantiating `MassSideKernel` requires clearing all four mass-side gates simultaneously.*

The four parametric classes implement the anchor-stable, bar-even, $q=1$ shadow (open categorical gap), and direction-sanity invariants for the mass side. The direction-sanity check uses an additive threshold. The $q=1$ shadow uses an `Option ℝ` parameter to accommodate hypothetical anchors. This infrastructure evaluates future candidates through a unified Lean class-instance attempt.
<!-- FILE_END: mass-side-kernel-formalize-first-gates.md -->

