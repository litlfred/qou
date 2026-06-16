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
near-match. At present only $c_2 = -1$ is proved exact; $c_3 = -2$ is a
near-match to the Hopf Jones value; and $c_k$ for $k \geq 3$ are
calibration-anchored.*

The conjecture is the precise statement of what would close the gap. The
expected route is the same machinery that resolved the analogous
$\alpha_{\mathrm{EM}}$ next-order factor: identify the $\mathfrak{Q}_\beta$
**Habiro element**, the $q$-series whose Taylor coefficients are the
$c_k$. Such an element would make each $c_{k\geq 3}$ exact and
anchor-independent, turn the per-rung magnitude $|c_{N+1}\,u^{N+1}|$ into a
rigorous truncation bound to arbitrary order, and promote the
precision-order formula $N(\varepsilon)$ from a heuristic to a derivation.
Until then the higher rungs remain a calibration record, not a prediction,
and the block records that status so it is auditable from the manifest.

## Lean structure

The conjecture is axiomatised as a class
`QbetaCkTruncationCanonicalClass` in the accompanying `.lean` file. Its
fields encode the three tier facts — $c_2$ proved exact, $c_3$ a
near-match to $J_{\mathrm{Hopf}}(q{=}1)$, and the existence claim for a
canonical $c_k$ at $k \geq 3$ — with the existence field carrying the open
content. Following the conditional-class convention, the class admits no
unconditional instance: the single `sorry` in any instance **is** the
conjecture, not a missing proof.
