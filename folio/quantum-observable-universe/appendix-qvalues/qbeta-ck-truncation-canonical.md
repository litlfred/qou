The $\mathfrak{Q}_\beta$ truncation coefficients differ in epistemic status. The tiering below records, for each rung, whether it is proved, near-matched, or calibration-anchored, so that its open status is explicit and checkable. A second axis, **the Markov convention**, cuts across all three tiers and is recorded separately at the end of this block: every numerical statement here is convention-C-frame, and the canonical convention is D.

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

**Convention frame (cuts across every tier above).** The tiers record *epistemic*
status. They do **not** record which Markov convention the numbers were computed
in, and that is the larger caveat of the two. Every value in this block —
$c_2 = -1$, $c_3 = -2$, and the cal-anchored $c_{k\ge3}$ — was obtained with the
Markov parameter $z_C = \sqrt{q}/(q+1)$ (convention **C**), which is **excised**;
the canonical Markov parameter is $z_D = q^3/(q^2+1)$ (convention **D**).

The convention enters at exactly one place: the $N{=}1$ eigenphase
$\alpha = (z-1)\,h/2$, where $h = q - q^{-1}$. The four tail factors — the rungs
$k = 2,\ldots,5$ of the product above — are built from $b$ and $\hbar_q$ alone and
never mention $z$. But every extracted $c_k$ is obtained by dividing the measured
$Q$-value through a partial product that *begins* with the $N{=}1$ factor, so that
single entry point propagates into all of them. Measured at 60 decimal places, re-extracting under
convention D:

| | convention C | convention D |
|---|---|---|
| implied $c_2$ | $-1.017623798$ | $-9.298862871$ |
| $c_3$ (proton anchor) | $-2.069342577115168$ | $-974.4318877467484$ |
| distance to $-\mathrm{Vol}(4_1)$ | $\approx 0$ | $972.402004534$ |

For scale, the caveat the $c_3$ tier above *does* carry — anchor dependence — is
worth $0.0495$ across the two pins. The convention shift is worth $972.36$,
roughly twenty thousand times larger. Both are real; only one was recorded.

One pillar is convention-**immune** and does not need re-establishing: the
cross-anchor swing, whose ratio between the two conventions is $1.00522$ because
its dominant source — the sensitivity of the Form-A baseline $Q_{\text{base}}(q)$
divided by $u^3$ — is $z$-free. So the
verdict that $c_3$ is refuted as a real-$q$ fibre element survives the convention
change. It is the *value-level* near-matches that do not.

Re-deriving the ladder under D is **not** a substitution of $z_D$ into the
existing expressions — that is proved invalid
. It requires deriving the D-frame
eigenphase first, after which the ansatz above is reusable as it stands and the
five values are re-extracted from it.

**Conjecture (open).** *For every $k \geq 3$ there exists a canonical, substrate-only, $q_0$-anchor-independent closed form for the truncation coefficient $c_k$ — a genuine Taylor coefficient of a single underlying $q$-series (a Habiro element) rather than a calibration-anchored near-match.*

The expected mechanism mirrors the $\alpha_{\mathrm{EM}}$ next-order factor resolution: identify the $\mathfrak{Q}_\beta$ **Habiro element**, the $q$-series whose Taylor coefficients are the $c_k$. Such an element would make each $c_{k\geq 3}$ exact and anchor-independent, convert the per-rung magnitude $|c_{N+1}\,u^{N+1}|$ into a rigorous arbitrary-order truncation bound, and elevate the precision-order formula $N(\varepsilon)$ from heuristic to derivation. Until then, higher rungs serve as a calibration record, not a prediction.
