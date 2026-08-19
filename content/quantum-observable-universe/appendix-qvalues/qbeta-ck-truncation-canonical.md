We set out the epistemic status of the $\mathfrak{Q}_\beta$ truncation coefficients. It designates which rung is proved, near-matched, or calibration-anchored, ensuring their open status is explicit and checkable.

The $\mathfrak{Q}_\beta$ categorical precision ladder expresses the neutron $\beta$-decay $Q$-value substrate prediction as a convergent product of correction rungs around a Form-A baseline:

$$
  \mathfrak{Q}_\beta(q) \;=\; Q_{\text{base}}(q) \cdot \prod_{k\geq 2}\bigl(1 + c_k\,u^k\bigr),
  \qquad u \;=\; b\,\hbar_q^2 \;\approx\; 0.00852,
$$

with $b$ the Hoefsmit off-diagonal coupling on the seminormal $V_{(2,1)}$ representation and $\hbar_q = (q-1)/q$. Because $u \approx 0.00852$, each rung adds roughly $\log_{10}(1/u) \approx 2.07$ decimal digits. The target precision fixes the truncation order $N$: $N \geq \log_{10}(1/\varepsilon)/2.07 - 1$. Target precision, not a canonicity criterion, determines $N$.

The status of the rung coefficients $c_k$ is **tiered**:

- **$c_2 = -1$ — structural.** The depth-2 coefficient is the exact $u^2$ coefficient of the explicit-factor product $\prod_{k\ge2}(1 + c_k u^k)$, obtained by re-reading the Kashiwara $\tilde f_1$ geometric-tail factor $(1 - b^2\,\hbar_q^4)$ in that form ([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)). Being a constant, it is $q_0$-anchor-independent. Two scope limits: the factor $(1 - b^2\hbar_q^4)$ is itself a **definition**, not a derived object, so "proved" overstates what is established; and "Taylor coefficient" is a statement about *that* series — the normalised series with the cosine factor inside has $\tilde c_2 = c_2 - 1/8 = -9/8$.
- **$c_3 = -2 = J_{\mathrm{Hopf}}(q{=}1)$ — near-match.** The depth-3 coefficient matches the classical-limit Jones value of the two-component Hopf link, $J_{\mathrm{Hopf}}(q{=}1) = -2$. This is a structural resemblance, not an exact identity. The empirical Taylor coefficient extracted at the substrate parameter is anchor-dependent. A true Taylor coefficient would be anchor-independent; $c_3$ is not.
- **$c_k$ for $k \geq 3$ — cal-anchored (open).** We obtain the higher coefficients by matching the truncated product to the measured $Q$-value. They are circular: they encode the calibration datum they attempt to predict, and shift with the substrate anchor. They are cached for downstream reuse but carry no predictive content.

**Conjecture (open).** *For every $k \geq 3$ there exists a canonical, substrate-only, $q_0$-anchor-independent closed form for the truncation coefficient $c_k$ — a genuine Taylor coefficient of a single underlying $q$-series (a Habiro element) rather than a calibration-anchored near-match.*

This conjecture outlines the requirement for closure. The expected mechanism mirrors the $\alpha_{\mathrm{EM}}$ next-order factor resolution: identify the $\mathfrak{Q}_\beta$ **Habiro element**, the $q$-series whose Taylor coefficients are the $c_k$. Such an element would make each $c_{k\geq 3}$ exact and anchor-independent, convert the per-rung magnitude $|c_{N+1}\,u^{N+1}|$ into a rigorous arbitrary-order truncation bound, and elevate the precision-order formula $N(\varepsilon)$ from heuristic to derivation. Until then, higher rungs serve as a calibration record, not a prediction.
