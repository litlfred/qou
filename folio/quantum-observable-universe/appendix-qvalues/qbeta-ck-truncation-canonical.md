The $\mathfrak{Q}_\beta$ truncation coefficients differ in epistemic status. The tiering below records, for each rung, whether it is proved, near-matched, or calibration-anchored, so that its open status is explicit and checkable. A second axis, **the eigenphase loop parameter**, cuts across all three tiers and is recorded separately below: the rung values $c_2 = -1$, $c_3 = -2$, and $c_{k \geq 3}$ above are extracted at the auxiliary parameter $z_{\mathrm{aux}} = \sqrt{q}/(q+1)$, whereas the canonical Markov parameter is $z = q^3/(q^2+1)$.

The $\mathfrak{Q}_\beta$ categorical precision ladder expresses the neutron $\beta$-decay $Q$-value substrate prediction as a convergent product of correction rungs around a Form-A baseline:

$$
  \mathfrak{Q}_\beta(q) \;=\; Q_{\text{base}}(q) \cdot \prod_{k\geq 2}\bigl(1 + c_k\,u^k\bigr),
  \qquad u \;=\; b\,\hbar_q^2 \;\approx\; 0.00852,
$$

with $b$ the Hoefsmit off-diagonal coupling on the seminormal $V_{(2,1)}$ representation and $\hbar_q = (q-1)/q$. Because $u \approx 0.00852$, each rung adds roughly $\log_{10}(1/u) \approx 2.07$ decimal digits. The target precision fixes the truncation order $N$: $N \geq \log_{10}(1/\varepsilon)/2.07 - 1$; $N$ is a precision setting rather than a criterion for whether a rung is canonical.

The status of the rung coefficients $c_k$ is **tiered**:

- **$c_2 = -1$ — structural.** The depth-2 coefficient is the exact $u^2$ coefficient of the explicit-factor product $\prod_{k\ge2}(1 + c_k u^k)$, obtained by re-reading the Kashiwara $\tilde f_1$ geometric-tail factor $(1 - b^2\,\hbar_q^4)$ in that form ([$\mathfrak{Q}_\beta$ categorical-derivation precision ladder](#prop:q-beta-categorical-precision-ladder)). Being a constant, it is $q_0$-anchor-independent. Two scope limits: the factor $(1 - b^2\hbar_q^4)$ is itself a **definition**, not a derived object, so "proved" overstates what is established; and "Taylor coefficient" is a statement about *that* series — the normalised series with the cosine factor inside has $\tilde c_2 = c_2 - 1/8 = -9/8$.
- **$c_3 = -2 = J_{\mathrm{Hopf}}(q{=}1)$ — near-match.** The depth-3 coefficient matches the classical-limit Jones value of the two-component Hopf link, $J_{\mathrm{Hopf}}(q{=}1) = -2$. This is a structural resemblance, not an exact identity. The empirical Taylor coefficient extracted at the substrate parameter is anchor-dependent. A true Taylor coefficient would be anchor-independent; $c_3$ is not.
- **$c_k$ for $k \geq 3$ — cal-anchored (open).** The higher coefficients are obtained by matching the truncated product to the measured $Q$-value. They are circular: they encode the calibration datum they attempt to predict, and shift with the substrate anchor. They are cached for downstream reuse but carry no predictive content.

**Dependence on the loop parameter (cuts across every tier above).** The tiers record *epistemic* status for extractions performed with the auxiliary loop parameter $z_{\mathrm{aux}} = \sqrt{q}/(q+1) = 1/(q^{1/2}+q^{-1/2})$, rather than the canonical Markov parameter $z = q^3/(q^2+1)$.

The loop parameter enters at a single place: the $N{=}1$ eigenphase $\alpha = (z-1)\,h/2$, where $h = q - q^{-1}$. The four tail factors — rungs $k = 2,\ldots,5$ of the product above — are built from $b$ and $\hbar_q$ alone and never mention $z$. However, every extracted $c_k$ is obtained by dividing the measured $Q$-value through a partial product beginning with the $N{=}1$ factor, so that single entry point propagates into all rungs. Evaluated at 60 decimal places, comparing extractions at $z_{\mathrm{aux}} = \sqrt{q}/(q+1)$ and at $z = q^3/(q^2+1)$:

| | $z_{\mathrm{aux}} = \sqrt{q}/(q+1)$ | $z = q^3/(q^2+1)$ |
|---|---|---|
| implied $c_2$ | $-1.017623798$ | $-9.298862871$ |
| $c_3$ (proton anchor) | $-2.069342577115168$ | $-974.4318877467484$ |
| distance to $-\mathrm{Vol}(4_1)$ | $\approx 0$ | $972.402004534$ |

For scale, the anchor-dependence shift on $c_3$ across the muon and proton pins is $0.0495$, whereas shifting the eigenphase parameter from $z_{\mathrm{aux}}$ to $z = q^3/(q^2+1)$ moves $c_3$ by $972.36$, roughly twenty thousand times larger.

One structural property is invariant under this parameter shift: the cross-anchor swing ratio between the two parameter evaluations is $1.00522$, because its dominant source — the sensitivity of the Form-A baseline $Q_{\text{base}}(q)$ divided by $u^3$ — is $z$-free. Thus the refutation of $c_3$ as a real-$q$ fibre element holds under both parameter evaluations, whereas the numerical near-matches hold only at $z_{\mathrm{aux}}$.

Formulating the precision ladder at $z = q^3/(q^2+1)$ is **not** a substitution of $z = q^3/(q^2+1)$ into the $z_{\mathrm{aux}}$ expressions; it requires deriving the $N{=}1$ eigenphase at $z = q^3/(q^2+1)$ first, after which the product ansatz above applies.

**Conjecture (open).** *For every $k \geq 3$ there exists a canonical, substrate-only, $q_0$-anchor-independent closed form for the truncation coefficient $c_k$ — a genuine Taylor coefficient of a single underlying $q$-series (a Habiro element) rather than a calibration-anchored near-match.*

The expected mechanism mirrors the $\alpha_{\mathrm{EM}}$ next-order factor resolution: identify the $\mathfrak{Q}_\beta$ **Habiro element**, the $q$-series whose Taylor coefficients are the $c_k$. Such an element would make each $c_{k\geq 3}$ exact and anchor-independent, convert the per-rung magnitude $|c_{N+1}\,u^{N+1}|$ into a rigorous arbitrary-order truncation bound, and elevate the precision-order formula $N(\varepsilon)$ from heuristic to derivation. Until then, higher rungs serve as a calibration record, not a prediction.
