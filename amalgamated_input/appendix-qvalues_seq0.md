<!-- FILE_START: im-complex-volume-intro.md -->
This appendix collects the $\beta$-decay $Q$-value predictions: the transfer-matrix $Q$-value chain, its substrate evaluations, and the benchmark table below. These are the imaginary-part companion of the binding-energy appendix — where that appendix computes $\mathrm{Re}\,\mathfrak{V} = \mathfrak{E}_{\mathrm{bind}}$, the binding energy, this one computes the bar-odd ($\sinh$) weak channel $\mathfrak{Q}_\beta = \mathrm{Im}\mathfrak{V}$, the imaginary part of the same complex volume $\mathfrak{V} = E_0\,\mathrm{tr}_M\big((\Pi_{\text{free}}-\mathbf{1})\circ\mathcal{M}\big)$ (defined in [The complex volume $\mathfrak{V}$](#sec:complex-volume)).

Everything below therefore records this $\mathrm{Im}$ channel, including the $c_k$ truncation-order ladder used in the chain. All entries are evaluated at the substrate $q_0$; since $\mathrm{Im}(q_0) = 0$ there, each is a real measured number.
<!-- FILE_END: im-complex-volume-intro.md -->

<!-- FILE_START: qvalue-derivation-chain.md -->
The Q-value of a $\beta^-$ decay $(Z, N) \to (Z+1, N-1)$ is
predicted from the substrate parameter $q$ alone, with zero fitting
parameters.  The formula works inside the $2 \times 2$ standard
representation of $H_3(q)$ — the two-dimensional irreducible
representation of the algebra.  Since $\dim H_3(q) = 3! = 6$, the
regular representation of $H_3(q)$ is $6 \times 6$; the traced-volume
computation below stays within the $2 \times 2$ standard block.
**MAE $\approx 4.4\%$ across six NNDC benchmarks, zero fitting.**

The derivation chain is:

$$
  q \xrightarrow{\text{Hecke}}
  \hat{V}_i(q) \xrightarrow{\text{ratio}}
  \log_q \frac{\hat{V}_i^{\mathrm{dau}}}{\hat{V}_i^{\mathrm{par}}}
  \xrightarrow{\kappa_q}
  \mathcal{Q}(q)
$$

**Step 1.** The traced volume $\hat{V}_i(q)$ for each generator
$\sigma_i$ is exact in $\mathbb{Q}(q^{1/2})$:

$$
  \hat{V}_i = z \cdot M_i[0,0] + M_i[1,0],
  \qquad
  M_i = \prod_{j > i} T(\mathfrak{w}^+(i,j), \mathfrak{w}^0(i,j))
$$

where $z = 1/(\sqrt{q} + 1/\sqrt{q})$ is the Markov parameter
and $T(c,d) = \begin{psmallmatrix} c(q-q^{-1})+d & c \\ c & d \end{psmallmatrix}$
is the transfer matrix.

**Step 2.** Classify each generator's log-ratio as unbinding ($u$),
rebinding ($r$), or unchanged ($uc$), then $q$-weight:

$$
  \mathcal{Q}_{\mathrm{raw}}
  = \bigl| q \cdot \Sigma_u + q^{-1} \cdot \Sigma_r + \Sigma_{uc} \bigr|
    \times \kappa_q
$$

where $\kappa_q = \ln(q) \times m_e / 3$.

**Step 3.** Apply shell and pairing corrections (all from $q$):

$$
  \mathcal{Q}
  = \mathcal{Q}_{\mathrm{raw}}
    \times F_{\mathrm{shell}}(q)
    \times F_{I_{10}}(Z, N; q)
$$

- $F_{\mathrm{shell}} \approx 0.5904$ for shell $\geq 5$: the
  Rosso--Jones weighted average over the two degree-$2$ torus knots
  $\tau(2,9)$ and $\tau(3,4)$, using the canonical inner product on
  $R(H_r(q))$
  ([canonical inner product](#prop:rj-canonical-inner-product)).
  The weights are the quantum dimensions $d_\lambda(q)$, forced by
  Schur orthogonality — no fitting freedom.
- $F_{I_{10}} = (1 - \delta_{\mathrm{pp}}/Z)(1 - \delta_{\mathrm{nn}}/N)$
  for odd-odd $\to$ even-even at shell $\geq 5$
<!-- FILE_END: qvalue-derivation-chain.md -->

<!-- FILE_START: qbeta-ck-truncation-canonical.md -->
This block records the epistemic status of the $\mathfrak{Q}_\beta$
truncation coefficients — which rung is proved, which is a near-match, and
which rungs remain calibration-anchored — so that their open status is
first-class and auditable from the manifest rather than buried in the
compute layer.

The $\mathfrak{Q}_\beta$ categorical precision ladder writes the substrate prediction
for the neutron $\beta$-decay $Q$-value as a convergent product of
correction rungs about a Form-A baseline,

$$
  \mathfrak{Q}_\beta(q) \;=\; Q_{\text{base}}(q) \cdot \prod_{k\geq 2}\bigl(1 + c_k\,u^k\bigr),
  \qquad u \;=\; b\,\hbar_q^2 \;\approx\; 0.00852,
$$

with $b$ the Hoefsmit off-diagonal coupling on the seminormal $V_{(2,1)}$
representation and $\hbar_q = (q-1)/q$. Because $u \approx 0.00852$, each
rung contributes roughly $\log_{10}(1/u) \approx 2.07$ additional decimal
digits, so the truncation order $N$ is fixed by the target precision
rather than by any canonicity gate: $N \geq \log_{10}(1/\varepsilon)/2.07 - 1$.

The status of the rung coefficients $c_k$ is **tiered**:

- **$c_2 = -1$ — proved.** The depth-2 coefficient is Taylor-exact: it is
  the Kashiwara $\tilde f_1$ geometric-tail factor $(1 - b^2\,\hbar_q^4)$,
  established in
  [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder).
  As a genuine Taylor coefficient of a convergent series it is
  $q_0$-anchor-independent (stable to compute precision $10^{-50}$).

- **$c_3 = -2 = J_{\mathrm{Hopf}}(q{=}1)$ — near-match.** The depth-3
  coefficient coincides numerically with the classical-limit Jones value
  of the two-component Hopf link, $J_{\mathrm{Hopf}}(q{=}1) = -2$. This is
  a structural resemblance, not an exact identity: the empirical Taylor
  coefficient extracted at the substrate parameter is anchor-dependent,
  and the integer $-2$ differs from it by a margin that grows with the
  anchor choice. A true Taylor coefficient would be anchor-independent;
  $c_3$ is not.

- **$c_k$ for $k \geq 3$ — cal-anchored (open).** The higher coefficients
  are obtained by matching the truncated product to the measured
  $Q$-value, so they are circular: they encode the calibration datum they
  are meant to predict, and they shift with the substrate anchor. They are
  cached for downstream reuse but carry no predictive content.

**Conjecture (open).** *For every $k \geq 3$ there exists a canonical,
substrate-only, $q_0$-anchor-independent closed form for the truncation
coefficient $c_k$ — a genuine Taylor coefficient of a single underlying
$q$-series (a Habiro element) rather than a calibration-anchored
near-match.*

The conjecture is the precise statement of what would close the gap. The
expected route is the same machinery that resolved the analogous
$\alpha_{\mathrm{EM}}$ next-order factor: identify the $\mathfrak{Q}_\beta$
**Habiro element**, the $q$-series whose Taylor coefficients are the
$c_k$. Such an element would make each $c_{k\geq 3}$ exact and
anchor-independent, turn the per-rung magnitude $|c_{N+1}\,u^{N+1}|$ into a
rigorous truncation bound to arbitrary order, and promote the
precision-order formula $N(\varepsilon)$ from a heuristic to a derivation.
Until then the higher rungs remain a calibration record, not a prediction.
<!-- FILE_END: qbeta-ck-truncation-canonical.md -->

