*Atomic masses from the seven-term [q-integer BW formula](#conj:q-integer-mass-formula)
with zero fitted parameters.  All seven coefficients and the shell
width $\sigma = [2]_q$ are products of quantum integers $[n]_q$
evaluated at $q_0 \approx 1.110$, times $m_e$.
Observed masses from AME2020.*

*Five standard BW terms:*

$$
\lambda_V = 2[2]_q[7]_q m_e, \quad
\lambda_S = 2[4]_q^2 m_e, \quad
\lambda_C = (q{-}q^{-1})[6]_q m_e, \quad
a_{\mathrm{asym}} = 3[2]_q[7]_q m_e, \quad
\delta_P = [3]_q[7]_q m_e
$$

*Two additional terms from Hecke representation theory:*

$$
\lambda_{\mathrm{ex}} = \frac{[3]_q}{[2]_q} m_e \quad (\text{exchange Coulomb}),
\qquad
\delta_S = [2]_q^2 [3]_q \, m_e \quad (\text{shell correction})
$$

*The exchange Coulomb corrects the direct Coulomb overcounting
at high $Z$ via the nucleon screening ratio $[3]_q/[2]_q$.
The shell correction adds binding at magic-number closures
$\{2,8,20,28,50,82,126\}$ where torus knot $T_{2,m}$ coherence
enhances the exceptional-divisor pairing (s-orbital effect).*

See [Table: Atomic mass predictions, He through U (32 isotopes)](#tbl:amc-q-integer-table-data)
for the predicted versus observed masses.

*Mean absolute error: $0.020\%$ (32 isotopes, He through U).*

*Best predictions: K $+0.002\%$, Zn $-0.003\%$, Ne $-0.003\%$,
Al $+0.003\%$, Fe $-0.003\%$, Cl $+0.003\%$.*

*Comparison with five-term formula: He improved from $+0.054\%$ to
$+0.006\%$ (9$\times$), Ti from $+0.182\%$ to $-0.013\%$ (14$\times$),
Cr from $-0.158\%$ to $-0.007\%$ (23$\times$).  Overall MAE reduced
from $0.034\%$ to $0.020\%$ (41\% improvement).*

*Both $M_{\mathrm{pred}}$ and $M_{\mathrm{obs}}$ use atomic mass
convention: $M = Z m_p + N m_n + Z m_e - B$.  AME2020 experimental
uncertainties are sub-keV for $Z \leq 30$.  Prediction errors
($0.002$--$0.1\%$) are systematic and reflect the semi-empirical
BW approximation, not measurement uncertainty.*

*Witness: `q-integer-bw-7term.witness.json`.*
