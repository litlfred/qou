**Proposition (joint Galois $\times$ braid action commutes on the figure-8
bi-filtration cell — verified directly).**

The joint motivic-Galois $\times$ braid-group action conjecture
([`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action))
predicts commutativity on each $\mathcal{H}_q^{(n, K)}$ stratum.
*This proposition verifies the prediction on the figure-8 row
$\mathcal{H}_q^{(2, 4_1)}$ by direct computation.*

### Setup

The figure-8 bi-filtration cell is

$$
  \mathcal{H}_q^{(2, 4_1)}
  \;\subseteq\;
  G^{(2)}(\mathcal{H}_q),
$$

with dominant cell $\lambda_K = (2, 2)$ in $H_4(q)$ — *self-conjugate*
([`rem:chirality-period-pairing`](#rem:chirality-period-pairing))
— and shape parameter $z_K = \zeta_6 = e^{i\pi/3}$.

The two group actions:

| Group | Generator | Action on $\mathcal{H}_q^{(2, 4_1)}$ |
|---|---|---|
| $G_{\mathrm{mot}} \supseteq \langle * \rangle$ (bar) | $*: q \mapsto q^{-1}$, $\zeta_6 \mapsto \zeta_6^{-1}$ | $\mathrm{Li}_2^q(\zeta_6) \mapsto \mathrm{Li}_2^q(\zeta_6^{-1})$ |
| $B_4 \to H_4(q)$ | $\sigma_1, \sigma_2, \sigma_3$ | conjugation in $H_4(q)$, fixes central idempotents |
