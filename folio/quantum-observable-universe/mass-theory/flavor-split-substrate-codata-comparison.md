**Remark (comparison with CODATA).**

This remark is where the formula of [the flavor-split identity](#prop:flavor-split-substrate) is compared with measurement. The identity itself makes no empirical claim; the claim compared here is [the conjectured mass split](#conj:flavor-split-substrate-mass).

At the proton pin $q = q_0 \approx 1.1099785827513808$, evaluated at 40 digits:

$$
  (q_0 - 1)^2 \cdot (1 - q_0^{-4}) / 3
  \;\approx\;
  0.0120953 \cdot 0.341218 / 3
  \;\approx\;
  1.3757 \times 10^{-3},
$$

against the CODATA value $(m_n - m_p)/M_N \approx 1.2933 / 938.919 \approx 1.3775 \times 10^{-3}$, with $M_N = (m_p + m_n)/2$. The residual is $-0.128\%$.

**Evaluation at $q_0$.**

| Quantity                       | Substrate formula                 | Substrate value          | CODATA target            | Residual   |
| ------------------------------ | --------------------------------- | ------------------------ | ------------------------ | ---------- |
| $(m_n - m_p)/M_N$              | $(q-1)^2 (1 - q^{-4}) / 3$        | $1.3757 \times 10^{-3}$  | $1.3775 \times 10^{-3}$  | $-0.128\%$ |
| $(m_n - m_p)/\mu_{\text{avg}}$ | $\hbar_q^2 \cdot h_q \cdot [2]_q$ | $4.1271 \times 10^{-3}$  | $4.1324 \times 10^{-3}$  | $-0.128\%$ |
| $m_n - m_p$                    | $M_N \cdot (q-1)^2(1-q^{-4})/3$   | $1.2917\,\text{MeV}$     | $1.2933\,\text{MeV}$     | $-0.128\%$ |

The three rows carry the same residual. The CODATA target of the second row is $3 (m_n - m_p)/M_N$, using $M_N = 3\mu_{\text{avg}}$ from Step 6 of the proof, and the third row multiplies the first by $M_N$. So the table records one comparison, not three.

The residual is far larger than the uncertainty in $q_0$ and in the CODATA masses, so the formula does not reproduce the splitting exactly. The ansatz of Step 2 of the proof was chosen partly for its agreement with experiment, so this agreement is not independent evidence for it.
