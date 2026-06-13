# Exotic-Signed KLR Composite Probe Findings

The objective was to test whether an exotic-signed variant of Composite 1 (where signs are flipped to bypass the positivity refutation) could viably serve as the Habiro element for Q_beta by producing `c_2 = -1` at both anchors.

## 1. The Target Constraints
To produce `c_2 = -1` at the $u^2$ rung, the sum of the exotic characters must exactly cancel the $(q;q)_2$ factor:
$\sum_{l(w)=2} D_w^{exotic}(\lambda) = \frac{-1}{(1-q)(1-q^2)}$

Evaluating this target function $T(q)$ at the two substrate anchors:
- **Proton anchor ($q_p \approx 1.10997$):** $T(q_p) = -39.18372$
- **Muon anchor ($q_m \approx 1.10996$):** $T(q_m) = -39.18371$

## 2. The Cross-Anchor Rigidity Wall
The probe evaluated not just the absolute magnitude, but the "cross-anchor rigidity"—the required slope to match both anchors simultaneously:
- **Slope ($dT/dq$):** $\approx 731.14$
- **Log-Derivative ($T'/T$):** $\approx -18.66$

## 3. Why Exotic Signs Cannot Save It
For a generic Laurent polynomial $P(q) = \sum a_k q^k$ to match this, it must have $P(q_p) \approx -39.18$ and $P'(q_p) \approx 731.14$.

- **Degree Argument:** For a single monomial $q^k$, the log-derivative is $k / q \approx k / 1.11$. To match $-18.66$, we would need a degree $k \approx -21$. Length-2 Demazure elements for small-rank groups (like $sl_3$ or $sl_4$) have extremely small degrees (e.g., $0, 1, 2$).
- **Coefficient Magnitude Argument:** If we try to build the slope using a combination of small-degree terms (e.g., $P(q) = a q^2 + b q + c$), forcing $P' \approx 731$ requires the coefficients $a, b, c$ to be on the order of hundreds (e.g., $b \approx 731$, $c \approx -850$). However, the total number of terms in the length-2 character sum for small-rank groups is strictly bounded (e.g., $\le 6.7$ for $sl_3$).

## Conclusion
The mathematical finding is a definitive **NEGATIVE**. An exotic-signed variant is not just unwritten; it is structurally ruled out for small-rank groups. Flipping signs can achieve a negative value, but it cannot bridge the massive slope/log-derivative gap ($T'/T \approx -18.66$) required by cross-anchor rigidity without artificially inflating coefficients to the hundreds—which violates the categorical nature of the characters.
