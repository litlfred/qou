<!-- FILE_START: confinement-selection-confinement-sdp-vs-intro.md -->
This subsection isolates the categorical confinement-selection mechanism. The SDP-vs-LP comparison identifies which substrate-level constraints survive the LP relaxation. The multi-input SDP records the multi-particle confinement condition. The topological confinement provides the categorical no-decay obstruction. Finally, the LP-dual stability analysis fixes the substrate-flow behaviour. The closing blocks specialise to the $n = 1$ vacuous-magic case and connect the confinement selection to the SDP-as-thimble flow.
<!-- FILE_END: confinement-selection-confinement-sdp-vs-intro.md -->

<!-- FILE_START: confinement-sdp-vs-lp.md -->
**Remark.**
*The scalar confinement LP restricts $\Phi$ in the confinement SDP to the diagonal span of the NF basis $\{b_i\}$ and drops the 2$\times$2 pair blocks. Equivalently, the LP is the SDP with the rank-1 restriction $\Phi = \mathrm{diag}(x)$ and the simplification $\pi_\lambda \mapsto \mathbf{1}_\lambda$.*

The LP is exact when every Wedderburn block is one-dimensional. In general, the LP provides a lower bound on the SDP and misses the multi-operator binding structure. For most baryonic and light-nuclear configurations, the Wedderburn decomposition has 1-dimensional blocks and the LP suffices. Magic-number and shell-closure configurations require the SDP.
<!-- FILE_END: confinement-sdp-vs-lp.md -->

<!-- FILE_START: confinement-misdp.md -->
**Reading.**
*When operator counts are constrained to integers, the feasible region of the confinement SDP becomes:*

$$
  \Phi \succeq 0
  \;\wedge\;
  \mathrm{rank}\text{-content}(\Phi) \in \mathbb{Z}_{\ge 0}^{|\mathcal{S}|}.
$$

*We solve this Mixed-Integer Semidefinite Program (MISDP) via continuous SDP relaxation combined with branch-and-cut. This strictly matches the confinement framework at every level of the hierarchy.*
<!-- FILE_END: confinement-misdp.md -->

<!-- FILE_START: confinement-topological.md -->
*Let $G \in \mathbb{R}^{6 \times 6}$ be the Gram matrix of $H_3(q)$ at $q = q_0$. Consider the linear program:*

$$
  \min_{x \in \mathbb{R}^6} \;
  \sum_{i=1}^{6} t_i x_i
  \qquad
  \text{s.t.} \quad
  \mathbf{1}^\top x = n_{\mathrm{target}},
  \quad
  Gx \geq 0
$$

*where $t_i = \mathrm{tr}_M(b_i)$ are the Markov traces of the NF basis elements. Then:*

1. *The LP has optimal value $\mathrm{tr}_M^* = 0$, achieved by exploiting the negative eigenvalue $\lambda_{\min}(G) < 0$.*
2. *The LP optimum $x^*$ has $|x_i^*| \gg 1$ for some components. It is not in the image of the braid group representation $\rho \colon B_3 \to H_3(q)$.*
3. *Among all elements $\Phi \in H_3(q)$ that are images of braid group elements of length $\leq 6$, $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the unique element with $|\mathrm{net}(\Phi \cdot \mathrm{crossings}) - n_{\mathrm{target}}| = 0$ for both proton and neutron typed crossings.*
<!-- FILE_END: confinement-topological.md -->

<!-- FILE_START: confinement-topological-interpretation.md -->
Confinement is topological, not energetic. The linear program over $H_3(q)$ has a strictly lower optimum than $\mathcal{B}_3$, but that optimum is not realizable as a braid group element.

Energy minimization alone permits unphysical states. The continuous LP finds algebra elements with zero Markov trace by mixing basis elements with large negative coefficients. These cannot be realized as physical braid words. The Borromean property is an independent constraint. The topological requirement restricts the feasible set from $\mathbb{R}^6$ to the image of $B_3$ under $\rho$. This discrete constraint selects $\mathcal{B}_3$. Confinement is topology plus action minimization.
<!-- FILE_END: confinement-topological-interpretation.md -->

<!-- FILE_START: lp-confined.md -->
**Definition (LP-confined).**
*An element $x \in H_3(q)$ is **LP-confined** if $x$ is LP-stable and no proper sub-braid is LP-stable.*

**Archimedean specialisation.** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: lp-confined.md -->

<!-- FILE_START: lp-dual-stability.md -->
*Let $x^*$ be a confined hadron. Then:*

1. *$x^*$ is LP-stable: $Gx^* \geq 0$ in all six channels.*
2. *The dual shadow prices $y_i^*$ are bounded: $|y_i^*| \leq \kappa(G) \cdot \|t\|$ where $\kappa(G) \approx 7.0$ is the condition number.*
3. *The $B_3$ sub-braid $\sigma_0\sigma_1^{-1}$ is LP-unstable: $G\vec{x}$ has a negative $\sigma_0$ component. Hence partial confinement is not sufficient. All three units are required.*
4. *Strong duality holds: $\mathrm{tr}_M(x^*) = y_0^* \cdot n_{\mathrm{target}}$.*

Individual quarks are LP-stable, but the $B_3$ sub-unit is not. This is the precise algebraic statement of confinement. The gluon field contains an LP-unstable intermediate, but the full 3-fold Borromean product restores stability. The confinement mechanism is not that quarks are unstable, but that the binding operator requires a topologically complete structure to be stable.

The negative eigenvalue $\lambda_{\min} \approx -0.956$ is the reason the LP has a global minimum at $\mathrm{tr}_M = 0$. The braid group realizability constraint prevents this.
<!-- FILE_END: lp-dual-stability.md -->

<!-- FILE_START: algebraic-primality.md -->
**Definition (algebraic primality).**
*Fix a substrate parameter $q > 1$. For each strand count $n \geq 1$, the confinement SDP selects a canonical state $\psi_n(q)$. We say that $n$ is **algebraically prime at $q$** if $\psi_n(q)$ is not contained in the closed span of any non-trivial tensor product*

$$
  \overline{\mathrm{span}}\bigl\{\,
    \psi_{n_1}(q) \otimes \cdots \otimes \psi_{n_k}(q)
  \,\bigr\}.
$$

*This product is indexed by a decomposition $n = n_1 + \cdots + n_k$ with $k \geq 2$ and every $n_i \geq 1$.*

By convention, $n = 0$ is not prime. This predicate serves as a purely algebraic surrogate for a magic strand count. An algebraically prime configuration does not factor into a product of smaller closed configurations.

The definition relies on a recursive decomposition argument. Testing primality at $n$ checks all decompositions into smaller parts. The recursion bottoms out at $n = 1$. The $n=1$ state is algebraically prime vacuously, because no decomposition into $k \geq 2$ positive parts sums to $1$.
<!-- FILE_END: algebraic-primality.md -->

<!-- FILE_START: n-equals-1-vacuous-magic.md -->
*For every substrate $q > 1$, the integer $n = 1$ is algebraically prime. Equivalently, the canonical state $\psi_1(q)$ is not in the closed span of any non-trivial tensor product of canonical states indexed by a decomposition $1 = n_1 + \cdots + n_k$ with $k \geq 2$ and $n_i \geq 1$. No such decomposition exists.*

The proof uses only elementary arithmetic. It uses no SDP analysis, Hecke-algebra machinery, or tensor-product manipulation. This is the base case of the recursion. Every primality check at $n \geq 2$ ultimately bottoms out at $n = 1$ through repeated decomposition.

Empirical nuclear magic numbers start at $2$. The framework's $n = 1$ primality is sometimes glossed as below the lowest shell closure. Within the algebraic-primality framework, $n = 1$ is strictly magic—just for a vacuous reason.

**Archimedean specialisation.** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: n-equals-1-vacuous-magic.md -->

<!-- FILE_START: q-beta-cos-resummation.md -->
**$\mathfrak{Q}_\beta$ cos-resummation theorem (conditional on $\beta$-decay transfer matrix).**
*The single-wrap Form A closed-form prediction $\mathfrak{Q}_\beta^A$ admits a tighter symbolic refinement. We obtain this refinement by replacing the linear bridge correction $(z-1)h/2$ with the classical cosine of half-argument:*
$$
  \mathfrak{Q}_\beta^{A,\mathrm{cos}}
  \;:=\;
  \mathfrak{Q}_\beta^A \cdot \cos\!\bigl(\tfrac{(z-1)\,h}{2}\bigr),
  \qquad
  z = \tfrac{1}{\sqrt q + 1/\sqrt q},
  \quad
  h = q - q^{-1}.
$$
*This refinement tightens the CODATA residual from $+1677.5$ ppm to $+305.7$ ppm.*

The transfer-matrix $M_\beta$ has spectrum $\{e^{+i\alpha},\, e^{-i\alpha}\}$ on the $2$-dimensional irreducible representation $V_{(2,1)}$ of $H_3(q)$. The eigenphase is $\alpha = (z-1) h / 2$ at the single-wrap order. The Markov trace $\tau_M$ symmetrizes the two eigenphases:
$$
  \tau_M(M_\beta)
  \;=\;
  \cos\alpha
  \;=\;
  \cos\!\bigl(\tfrac{(z-1)\,h}{2}\bigr).
$$

Two structural constraints enforce this form:

1. **Markov cyclicity.** The trace is cyclic. It is invariant under the bar involution $q \mapsto q^{-1}$, which maps $\alpha \mapsto -\alpha$. The resummation must be even in $\alpha$. The minimal even-power resummation that matches the linear bridge at the perturbative level is the cosine.
2. **Classical decategorification.** The mass observable lives in the classical limit, not in the q-deformed quantum group. The classical cosine is more accurate by $\approx 7$ ppm than the q-deformed cosine.
<!-- FILE_END: q-beta-cos-resummation.md -->

