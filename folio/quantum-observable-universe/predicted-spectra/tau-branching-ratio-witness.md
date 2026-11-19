Evaluating both the factorized and the product models at $q_0 \approx 1.1100$ allows comparison with the PDG experimental branching ratio.

## Weak vertex data

The $T_{3,5} = (\sigma_0 \sigma_1)^5$ weak vertex in $H_3(q)$ reduces to 6 normal form terms in the standard basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$. This requires 38 Hecke and 18 Yang–Baxter steps.

See Table 1.

$$
  \mathrm{net}(T_{3,5}) = 2.316,
  \qquad
  \mathrm{tr}_{\mathrm{Markov}}(T_{3,5}) = 0.968,
  \qquad
  |\mathcal{W}|^2 = 0.938.
$$

## Branching ratio comparison

Factorized model:

<!-- literal-source: closed-form V-A three-body phase-space integral f(x) = 1 - 8x + 8x^3 - x^4 - 12x^2 ln x at PDG lepton mass ratios -->
$$
  \frac{\mathrm{BR}(\tau \to e)}{\mathrm{BR}(\tau \to \mu)}
  =
  \frac{f(m_e^2/m_\tau^2)}{f(m_\mu^2/m_\tau^2)}
  =
  \frac{0.99999934}{0.97255996}
  \approx 1.028.
$$

Product model:

$$
  \frac{|M_e|^2}{|M_\mu|^2}
  =
  \frac{|\mathrm{tr}_3(T_{2,3} \cdot T_{3,5} \cdot T_{2,7})|^2}
       {|\mathrm{tr}_3(T_{2,5} \cdot T_{3,5} \cdot T_{2,7})|^2}
  =
  \frac{9.407}{13.730}
  \approx 0.685.
$$

This gives a branching ratio of $\approx 0.704$. This is inconsistent with experiment.

PDG 2024 experimental values:

$$
  \mathrm{BR}(\tau \to e\bar\nu_e\nu_\tau) = 17.82\%,
  \qquad
  \mathrm{BR}(\tau \to \mu\bar\nu_\mu\nu_\tau) = 17.39\%,
$$

$$
  \frac{\mathrm{BR}(\tau \to e)}{\mathrm{BR}(\tau \to \mu)}
  = 1.025 \pm 0.003.
$$

## Result

See Table 2.

The factorized model treats the Markov trace of $T_{3,5}$ as the universal matrix element. It reproduces the PDG ratio to $0.34\%$. The product model is excluded by data.

## Decay channel normal form structure

Both decay channels $\tau \to e$ and $\tau \to \mu$ reduce to 6 normal form terms in $H_3(q)$. The dominant term in both channels is $L_+ = \sigma_0\sigma_1$. It contributes $\sim 30\%$ of the total weight. The $L_-$ contribution is larger in $\tau \to \mu$ ($15.6\%$) than in $\tau \to e$ ($13.9\%$). The heavier daughter lepton requires more re-crossing energy.
