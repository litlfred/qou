<!-- FILE_START: confinement-selection-confinement-sdp-vs-intro.md -->
This subsection isolates the categorical confinement-selection mechanism. The SDP-vs-LP comparison identifies which substrate-level constraints survive the LP relaxation. The multi-input SDP records the multi-particle confinement condition. The topological confinement provides the categorical no-decay obstruction. Finally, the LP-dual stability analysis fixes the substrate-flow behaviour. The closing blocks specialise to the $n = 1$ vacuous-magic case and connect the confinement selection to the SDP-as-thimble flow.
<!-- FILE_END: confinement-selection-confinement-sdp-vs-intro.md -->

<!-- FILE_START: confinement-sdp-vs-lp.md -->
**Remark.** The scalar [confinement LP](#prop:confinement-lp) restricts $\Phi$ in the [confinement SDP](#prop:confinement-sdp) to the diagonal span of the NF basis $\{b_i\}$ and drops the 2$\times$2 pair blocks. Equivalently, the LP is the SDP with the rank-1 restriction $\Phi = \mathrm{diag}(x)$ and the simplification $\pi_\lambda \mapsto \mathbf{1}_\lambda$ (the indicator vector).

The LP is exact when every Wedderburn block is one-dimensional (no cross-channel coupling). In general, the LP provides a lower bound on the SDP and misses the multi-operator binding structure (cf. [multi-operator remark](#rem:confinement-sdp-multi-operator)). For most baryonic and light-nuclear configurations, the Wedderburn decomposition has 1-dimensional blocks and the LP suffices. Magic-number and shell-closure configurations require the SDP.
<!-- FILE_END: confinement-sdp-vs-lp.md -->

<!-- FILE_START: confinement-misdp.md -->
**Reading.** When operator counts are constrained to integers—as in the confinement hierarchy at levels $\ell \le 3$ where crossing multiplicities must be integral—the feasible region of the [confinement SDP](#prop:confinement-sdp) becomes:

$$
  \Phi \succeq 0
  \;\wedge\;
  \mathrm{rank}\text{-content}(\Phi) \in \mathbb{Z}_{\ge 0}^{|\mathcal{S}|}.
$$

We solve this Mixed-Integer Semidefinite Program (MISDP) via continuous SDP relaxation combined with branch-and-cut (see `computations/misdp_cross_channel.py`). This strictly matches the confinement framework at every level of the hierarchy.
<!-- FILE_END: confinement-misdp.md -->

<!-- FILE_START: confinement-topological.md -->
## Statement

**Proposition.** Let $G \in \mathbb{R}^{6 \times 6}$ be the Gram matrix of $H_3(q)$ at $q = q_0$ ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)). Consider the linear program:

$$
  \min_{x \in \mathbb{R}^6} \;
  \sum_{i=1}^{6} t_i x_i
  \qquad
  \text{s.t.} \quad
  \mathbf{1}^\top x = n_{\mathrm{target}},
  \quad
  Gx \geq 0
$$

where $t_i = \mathrm{tr}_M(b_i)$ are the Markov traces of the NF basis elements. Then:

1. The LP has optimal value $\mathrm{tr}_M^* = 0$, achieved by exploiting the negative eigenvalue $\lambda_{\min}(G) < 0$.
2. The LP optimum $x^*$ has $|x_i^*| \gg 1$ for some components (specifically $x_{e^-}^* \to +\infty$ without bounds). It is not in the image of the braid group representation $\rho \colon B_3 \to H_3(q)$.
3. Among all elements $\Phi \in H_3(q)$ that are images of braid group elements of length $\leq 6$, $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the unique element with $|\mathrm{net}(\Phi \cdot \mathrm{crossings}) - n_{\mathrm{target}}| = 0$ for both proton and neutron typed crossings.
<!-- FILE_END: confinement-topological.md -->

<!-- FILE_START: confinement-topological-interpretation.md -->
Confinement is topological, not energetic. The linear program over $H_3(q)$ has a strictly lower optimum than $\mathcal{B}_3$, but that optimum is not realizable as a braid group element.

## Physical interpretation

The LP result has a precise physical meaning:

1. **Energy minimization alone permits unphysical states.** The continuous LP finds algebra elements with zero Markov trace (zero action) by mixing basis elements with large negative coefficients. These cannot be realized as physical braid words.
2. **The Borromean property is an independent constraint.** The topological requirement that removing any one quark unlinks the other two (Borromean linking) restricts the feasible set from $\mathbb{R}^6$ to the image of $B_3$ under $\rho$. This discrete constraint selects $\mathcal{B}_3$.
3. **Confinement is topology plus action minimization.** $\mathcal{B}_3$ is selected by the conjunction of Borromean topology (being a braid group element), the net constraint (physical mass), and minimum action among feasible elements.
<!-- FILE_END: confinement-topological-interpretation.md -->

<!-- FILE_START: lp-confined.md -->
**Definition (LP-confined).**
*An element $x \in H_3(q)$ is **LP-confined** if $x$ is [LP-stable](#def:lp-stable) and no proper sub-braid (obtained by removing one or more generators from the braid word) is LP-stable.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: lp-confined.md -->

<!-- FILE_START: lp-dual-stability.md -->
An element $x \in H_3(q)$ with NF decomposition $x = \sum_{i=1}^{6} x_i b_i$ is classified by the [LP-stable](#def:lp-stable) and [LP-confined](#def:lp-confined) criteria.

**Proposition (LP dual stability of confined hadrons).**
*Let $x^*$ be a confined hadron (proton or neutron, built via $B_3 \cdot \Phi_{\mathrm{quarks}}$). Then:*

1. *$x^*$ is LP-stable: $Gx^* \geq 0$ in all six channels.*
2. *The dual shadow prices $y_i^*$ are bounded: $|y_i^*| \leq \kappa(G) \cdot \|t\|$ where $\kappa(G) \approx 7.0$ is the condition number.*
3. *The $B_3$ sub-braid $\sigma_0\sigma_1^{-1}$ is LP-unstable: $G\vec{x}$ has a negative $\sigma_0$ component $\approx -0.106$. Hence partial confinement (1 of 3 $B_3$ units) is not sufficient. All three units are required.*
4. *Strong duality holds: $\mathrm{tr}_M(x^*) = y_0^* \cdot n_{\mathrm{target}}$.*

**Verified values at $q_0 \approx 1.110$:**

See [Table](#tbl:lp-dual-stability-table-data).

**Key finding: individual quarks are LP-stable, but the $B_3$ sub-unit is not.** This is the precise algebraic statement of confinement. The gluon field ($B_3 = (\sigma_0\sigma_1^{-1})^3$) contains an LP-unstable intermediate ($\sigma_0\sigma_1^{-1}$), but the full 3-fold Borromean product restores stability. The confinement mechanism is not that quarks are unstable, but that the binding operator requires a topologically complete (Borromean) structure to be stable.

**Gram eigenvalues:**
$\lambda = (-0.956, +0.414, +0.428, +0.956, +1.282, +2.893)$.

The negative eigenvalue $\lambda_{\min} \approx -0.956$ is the reason the LP has a global minimum at $\mathrm{tr}_M = 0$ (massless). The braid group realizability constraint prevents this. Braid words of length $L$ have NF coefficients bounded by $O((1+|h|)^L)$, and the $\mathrm{tr}_M = 0$ solution requires unbounded coefficients.

**Witness:** `confinement-lp.witness.json`, `confinement-operator-selection.witness.json`.
<!-- FILE_END: lp-dual-stability.md -->

<!-- FILE_START: algebraic-primality.md -->
**Definition (algebraic primality).**
Fix a substrate parameter $q > 1$. For each strand count $n \geq 1$, the
confinement SDP selects a canonical state $\psi_n(q)$. We say that $n$ is
**algebraically prime at $q$** if $\psi_n(q)$ is *not* contained in
the closed span of any non-trivial tensor product

$$
  \overline{\mathrm{span}}\bigl\{\,
    \psi_{n_1}(q) \otimes \cdots \otimes \psi_{n_k}(q)
  \,\bigr\}.
$$

This product is indexed by a decomposition $n = n_1 + \cdots + n_k$ with $k \geq 2$
and every $n_i \geq 1$.

By convention, $n = 0$ (the vacuum) is *not* prime. This predicate serves as
a purely algebraic surrogate for a magic strand
count. An algebraically prime configuration does not factor into a product of
smaller closed configurations.

The definition relies on a recursive decomposition argument. Testing
primality at $n$ checks all decompositions into smaller parts. Each part is built from canonical states $\psi_{n_i}(q)$.
The recursion bottoms out at $n = 1$. The $n=1$ state is algebraically prime
vacuously, because no decomposition into $k \geq 2$ positive parts sums
to $1$ ([vacuous primality at $n = 1$](#prop:n-equals-1-vacuous-magic)).

We state separately the conjecture that, at the substrate value $q_0$, the algebraically
prime integers coincide with the empirical magic ladder
$\{1, 2, 8, 20, 28, 50, 82, 126\}$. The present
definition fixes only the predicate, not its value at any particular
$q$.
<!-- FILE_END: algebraic-primality.md -->

<!-- FILE_START: n-equals-1-vacuous-magic.md -->
## Statement

**Proposition (vacuous primality at $n = 1$).**
*For every substrate $q > 1$, the integer $n = 1$ is algebraically prime (def:algebraic-primality). Equivalently, the canonical state $\psi_1(q)$ is not in the closed span of any non-trivial tensor product of canonical states indexed by a decomposition $1 = n_1 + \cdots + n_k$ with $k \geq 2$ and $n_i \geq 1$. No such decomposition exists.*

## Remarks

- The proof uses only elementary arithmetic (positivity-induced lower bound for sum vs length). It uses no SDP analysis, Hecke-algebra machinery, or tensor-product manipulation.
- This is the base case of the recursion in def:algebraic-primality. Every primality check at $n \geq 2$ ultimately bottoms out at $n = 1$ through repeated decomposition.
- The proposition holds uniformly in $q$. Whatever SDP machinery is supplied for $\psi_n(q)$ at general $n$, the case $n = 1$ always trivialises by structural impossibility of the decomposition.
- **Relation to the empirical "magic-1" question.** Empirical nuclear magic numbers start at $2$. The framework's $n = 1$ primality is sometimes glossed as "trivial" or "below the lowest shell closure." Within the algebraic-primality framework, $n = 1$ is strictly magic — just for a vacuous reason. Including $1$ in the predicted magic set is consistent with the framework's definition. Whether to display it alongside the empirical $\{2, 8, 20, 28, 50, 82, 126\}$ is a presentation choice, not a mathematical claim.

## Lean formalisation

The Lean proof [`one_isAlgebraicallyPrime`](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/content/quantum-observable-universe/lean/QOU/Interactions/AlgebraicPrimality.lean) encodes the four steps above. The auxiliary lemma `sum_ge_length_of_all_pos` is proved by list induction (base case: empty list trivial; step case: sum of `a :: as` $\ge$ 1 + length of `as`, by inductive hypothesis on the tail). The main theorem combines `length ≥ 2` and `sum = 1` via `omega` to derive the contradiction.

The proof contains no `sorry`.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: n-equals-1-vacuous-magic.md -->

<!-- FILE_START: q-beta-cos-resummation.md -->
**$\mathfrak{Q}_\beta$ cos-resummation theorem (conditional on [`prop:beta-decay-transfer-matrix`](#prop:beta-decay-transfer-matrix)).**
*The single-wrap Form A closed-form prediction $\mathfrak{Q}_\beta^A$ admits a tighter symbolic refinement. We obtain this refinement by replacing the linear bridge correction $(z-1)h/2$ from [`prop:q-beta-spectral-bridge`](#prop:q-beta-spectral-bridge) with the classical cosine of half-argument:*
$$
  \mathfrak{Q}_\beta^{A,\mathrm{cos}}
  \;:=\;
  \mathfrak{Q}_\beta^A \cdot \cos\!\bigl(\tfrac{(z-1)\,h}{2}\bigr),
  \qquad
  z = \tfrac{1}{\sqrt q + 1/\sqrt q},
  \quad
  h = q - q^{-1}.
$$
*This refinement tightens the CODATA residual from $+1677.5$ ppm (Form A bare) to $+305.7$ ppm. It improves accuracy by a factor of $5.49$ at $q_0 \approx 1.110$.*

## Structural origin

The transfer-matrix $M_\beta$ from [`prop:beta-decay-transfer-matrix`](#prop:beta-decay-transfer-matrix) has spectrum $\{e^{+i\alpha},\, e^{-i\alpha}\}$ on the $2$-dimensional irreducible representation $V_{(2,1)}$ of $H_3(q)$. The eigenphase is $\alpha = (z-1) h / 2$ at the single-wrap order. The Markov trace $\tau_M$ symmetrizes the two eigenphases:
$$
  \tau_M(M_\beta)
  \;=\;
  \tfrac{1}{2}\bigl(e^{+i\alpha} + e^{-i\alpha}\bigr)
  \;=\;
  \cos\alpha
  \;=\;
  \cos\!\bigl(\tfrac{(z-1)\,h}{2}\bigr).
$$

Two structural constraints enforce this form:

1. **Markov cyclicity.** The trace is cyclic: $\tau_M(xy) = \tau_M(yx)$. It is therefore invariant under the bar involution $q \mapsto q^{-1}$, which maps $\sigma_i \mapsto \sigma_i^{-1}$ and consequently $\alpha \mapsto -\alpha$. The resummation must be even in $\alpha$; only $\alpha^{2k}$ powers survive. The minimal even-power resummation that matches the linear bridge at the perturbative level is the cosine: $\cos\alpha = 1 - \alpha^2/2! + \alpha^4/4! - \cdots$.
2. **Classical decategorification.** The mass observable lives in the classical limit (Pauli/Bose–Einstein statistics), not in the q-deformed quantum group. Empirical comparison confirms this classical nature:

   | resummation | residual at $q_0$ |
   |---|---:|
   | $\cos((z-1)h/2)$ (classical) | $+305.7$ ppm |
   | $\cos_q((z-1)h/2)$ (q-deformed) | $+313.4$ ppm |

   The classical cosine is more accurate by $\approx 7$ ppm. This is consistent with the classical limit of the mass observable.

## Numerical reduction

At $q_0$:

See [Table](#tbl:q-beta-cos-resummation-table-data).
<!-- FILE_END: q-beta-cos-resummation.md -->

