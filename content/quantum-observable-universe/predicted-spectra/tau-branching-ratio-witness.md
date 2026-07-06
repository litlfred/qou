Evaluating both the factorized and the product models at $q_0 \approx 1.1100$ allows comparison with the PDG experimental branching ratio.

## Weak vertex data

The $T_{3,5} = (\sigma_0 \sigma_1)^5$ weak vertex in $H_3(q)$ reduces (38 Hecke and 18 Yang–Baxter steps) to **6 normal form (NF) terms** in the standard basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$:

See [Table 1](#tbl:tau-branching-ratio-witness-table1-data).

$$
  \mathrm{net}(T_{3,5}) = 2.316,
  \qquad
  \mathrm{tr}_{\mathrm{Markov}}(T_{3,5}) = 0.704,
  \qquad
  |\mathcal{W}|^2 = 0.495.
$$

## Branching ratio comparison

**Factorized model** (lepton universality):

$$
  \frac{\mathrm{BR}(\tau \to e)}{\mathrm{BR}(\tau \to \mu)}
  =
  \frac{f(m_e^2/m_\tau^2)}{f(m_\mu^2/m_\tau^2)}
  =
  \frac{0.99999934}{0.97255996}
  \approx \mathbf{1.028}.
$$

**Product model** (universality-breaking):

$$
  \frac{|M_e|^2}{|M_\mu|^2}
  =
  \frac{|\mathrm{tr}_3(T_{2,3} \cdot T_{3,5} \cdot T_{2,7})|^2}
       {|\mathrm{tr}_3(T_{2,5} \cdot T_{3,5} \cdot T_{2,7})|^2}
  =
  \frac{5.426}{7.865}
  \approx 0.690.
$$

This gives a branching ratio of $\approx 0.709$. This is inconsistent with experiment.

**PDG 2024 experimental values:**

$$
  \mathrm{BR}(\tau \to e\bar\nu_e\nu_\tau) = 17.82\%,
  \qquad
  \mathrm{BR}(\tau \to \mu\bar\nu_\mu\nu_\tau) = 17.39\%,
$$

$$
  \frac{\mathrm{BR}(\tau \to e)}{\mathrm{BR}(\tau \to \mu)}
  = \mathbf{1.025} \pm 0.003.
$$

## Result

See [Table 2](#tbl:tau-branching-ratio-witness-table2-data).

The factorized model treats the Markov trace of $T_{3,5}$ as the universal matrix element. It reproduces the PDG ratio to $0.34\%$. The product model is excluded by data.

## Decay channel NF structure

Both decay channels $\tau \to e$ and $\tau \to \mu$ reduce to **6 NF terms** in $H_3(q)$. The dominant term in both channels is $L_+ = \sigma_0\sigma_1$ (the Hopf link), contributing $\sim 30\%$ of the total weight. The $L_-$ (anti-Hopf) contribution is larger in $\tau \to \mu$ ($15.6\%$) than in $\tau \to e$ ($13.9\%$). This is consistent with the heavier daughter lepton requiring more re-crossing energy.

The full witness data (including all NF coefficients, Markov traces, phase-space factors, and reverse-order checks) is recorded in `tau-leptonic-decay.witness.json`.
