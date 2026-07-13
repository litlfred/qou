<!-- FILE_START: intro-alpha-k-procedure.md -->
The categorical mass coefficients $\alpha_k$ in the six-term mass formula are deterministic. A substrate-split procedure fixes each $\alpha_k$. This procedure separates the flavor-dressing contribution from the bare categorical mass and maps the $k$-dependence to a Jacobi–Pochhammer factorial.

We first define the substrate-split decomposition and prove uniqueness of the flavor-dressed mass. We then specialise to small $k$ to verify the procedure. Finally, we tabulate the $\{\alpha_k\}$ values that drive the six-term mass formula.
<!-- FILE_END: intro-alpha-k-procedure.md -->

<!-- FILE_START: confinement-sdp.md -->
*Let $n$ be the Hecke strand count at confinement level $\ell$. Let $(\pi_\lambda)_{\lambda \vdash k, k \le n}$ be the central idempotents projecting onto the Wedderburn blocks of $H_n(q)$. Let $T$ be the cost operator. The confined operator at $q$ is the solution $\Phi^* \succeq 0$ of the primal matrix program:*

$$
  \min_{\Phi \succeq 0} \quad \langle T, \Phi \rangle
$$

*subject to:*

1. *(Per-block Frobenius positivity)* $\langle \pi_\lambda, \Phi \rangle \ge 0$ for all $\lambda \vdash k, k \le n$.
2. *(Adjacent-pair PSD)* Every $2 \times 2$ block corresponding to an adjacent generator pair $(\sigma_i, \sigma_{i+1})$ is positive semi-definite.
3. *(Normalisation)* $\mathrm{tr}(\Phi) = n_{\mathrm{target}}$.

*The dual program determines the matrix shadow prices:*

$$
  \max_{y_0, (y_\lambda \ge 0)} \quad n_{\mathrm{target}} \cdot y_0
$$

*subject to the matrix inequality:*

$$
  y_0 \cdot I \;+\; \sum_\lambda y_\lambda \cdot \pi_\lambda \;-\; T
  \;\preceq\; 0.
$$

*At the generic $q$ optimum, strong duality holds and complementary slackness applies as a matrix equation.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-analytic constructs. Any generic categorical identities remain valid over an abstract coefficient ring.
<!-- FILE_END: confinement-sdp.md -->

<!-- FILE_START: flavor-dressed-mass-from-substrate-split.md -->
*Let $\mu \colon \mathbf{Flavor} \to \mathbb{R}_{>0}$ be the flavor dressing functor. Let $M_N$ be the average nucleon mass, and $q = q_0$ the substrate parameter. The down-up dressed mass splitting is exactly determined by the substrate flavor formula:*

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;=\;
  M_N \cdot \frac{(q - 1)^2 (1 - q^{-4})}{3}
  \cdot
  \frac{q^{1/2} + q^{-1/2}}{q + q^{-1}}
  \;+\;
  O\!\left(\bigl(\Delta m / M_N\bigr)^2\right).
$$

*Dropping the $O$ correction yields the leading-order substrate-pure form:*

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;\approx\;
  \frac{M_N}{3} \cdot
  \hbar_q^2 \cdot h_q \cdot
  \frac{1}{z_{\mathrm{mkv}}}.
$$

The CODATA neutron-proton mass difference is no longer an input. The functor extracts the splitting purely from $q_0$ and the scale $M_N$. The individual masses $\mu_{\mathfrak{u}}$ and $\mu_{\mathfrak{d}}$ are then pinned by the baryon-content sum-rule.
<!-- FILE_END: flavor-dressed-mass-from-substrate-split.md -->

<!-- FILE_START: flavor-mass-splitting-bound.md -->
*For substrate parameter $q > 1$, the down-up splitting satisfies the two-sided bound:*

$$
  0 \;<\; \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;<\; M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q,
$$

*where $\hbar_q = (q - 1)/q$, $h_q = q - q^{-1}$, and $[2]_q = q + q^{-1}$.*

We bound the difference rather than the individual masses to isolate the substrate-derivable quantity from the CODATA-anchored mean. 
<!-- FILE_END: flavor-mass-splitting-bound.md -->

<!-- FILE_START: alpha-k-derivation-procedure.md -->
*Over $H_n(R, q)$ at generic $q$, the Jones-Markov trace admits a unique central-character expansion:*

$$
  \mathrm{tr}_M(\beta) \;=\; \sum_{\lambda \,\vdash\, n}
    y_\lambda \cdot \chi_\lambda(\beta).
$$

*Substituting the trace evaluation $\mathrm{tr}_M(w_\mu) = z^{\,n - \mathrm{len}(\mu)}$ for reduced words yields the $p(n) \times p(n)$ linear system:*

$$
  \sum_{\lambda \,\vdash\, n}
    \chi_\lambda(w_\mu)\, y_\lambda
  \;=\;
  z^{\,n - \mathrm{len}(\mu)},
  \qquad \mu \,\vdash\, n.
$$

*The character matrix is invertible at generic $q$. The system has a unique solution $y_\lambda \in R(\!(z)\!)$.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-analytic constructs. Any generic categorical identities remain valid over an abstract coefficient ring.
<!-- FILE_END: alpha-k-derivation-procedure.md -->

<!-- FILE_START: alpha-k-categorical-closure.md -->
**Conjecture (closed forms for categorical resummation).**
*At the substrate level, the categorical resummation $\mathcal{F}(\hbar_q^2)$ of the mass tower provides a dimensionless factor. This factor admits exactly one of the following closed forms:*

1. *(Geometric)* $1/(1-x) = \sum_{k\geq 0} x^k$.
2. *(Symmetric q-dilogarithm)* $1 - \mathrm{Li}_2^q(-x)$.

*The geometric closure overshoots the calibrated energy scale. The q-dilogarithm closure is the rigorously bounded analog derived from the brane tower. Both forms evaluate to identical significant figures at the substrate level, leaving the exact CAL-3 direction open.*
<!-- FILE_END: alpha-k-categorical-closure.md -->

<!-- FILE_START: chi-lambda-w0-sign-weighting.md -->
*Let $\mathcal{B}_n$ and $\mathcal{B}_p$ be canonical nucleon braids. The empirical coefficients $c_k^{(\lambda)}$ do not match a uniform Plancherel-weighted sum. Instead, they require weighting by the character values at the longest element $w_0 \in S_3$:*

$$
  S_k^{(w_0)} \;:=\; \sum_{\lambda \vdash 3}
    \chi_\lambda(w_0) \cdot c_k^{(\lambda)}
  \;=\; c_k^{(3)} \;-\; c_k^{(1,1,1)}.
$$

*This long-element character weighting correctly reproduces the sign of the empirical $c_k$ at $k=5$ and $k=6$.*

The longest element $w_0$ plays the role of central reversal. The $c_k$ Markov-trace decomposition is thus governed by the maximal mixing element, not the identity.
<!-- FILE_END: chi-lambda-w0-sign-weighting.md -->

<!-- FILE_START: atom-knot-mass-derivation.md -->
*Let $\mathfrak{H}$ be a confined particle with canonical Hecke element $T_w$ in Gröbner–Shirshov normal form. Its categorical mass invariant is the exact finite sum:*

$$
 M(\mathfrak{H}) \;=\; \nu_{\mathrm{SDP}} \cdot \bigl[\,\mathrm{tr}_M(T_w) + \mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})\,\bigr].
$$

*After applying the Archimedean realization functor at $q = q_0$, the physical binding energy is:*

$$
 B(\mathfrak{H}) \;=\; m_e \cdot M(\mathfrak{H}) \big|_{q = q_0}.
$$

*The derivation evaluates Yekutieli's multiplicative integral at finite slices. Since the GB spectral sequence collapses at $E_2$, no higher slices contribute. The computation relies entirely on the pre-Archimedean data encoded in the GB-filtration jet-order certificate.*
<!-- FILE_END: atom-knot-mass-derivation.md -->

