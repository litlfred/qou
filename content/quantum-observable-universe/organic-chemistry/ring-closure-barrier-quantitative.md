**Statement.**
For an even-$N$ ring with $N = 2m$, the topological ring-closure
activation barrier is

$$
  \Delta E_{\mathrm{closure}}(N)
   = 
  \bigl[\,(N - 1) - \Delta_{T(2,N)}(q_{0})\,\bigr]\,
  \lvert q + q^{-1}\rvert_{\mathrm{mol}},
$$

where $(N-1)$ is the linear-chain pairwise-Hopf weight (sum of the
$N-1$ adjacent C–C link weights, each $1$), and
$\Delta_{T(2,N)}(q_{0})$ is the threading-link Alexander weight at
the substrate value
([$\Delta_{T(2,N)}$ closed form](#lem:alexander-T2N-closed-form)).

**Numerical evaluation.**
With $\lvert q + q^{-1}\rvert_{\mathrm{mol}} \approx 22.4\ \mathrm{kJ/mol}$
([molecular crossing quantum](#prop:molecular-crossing-quantum)) and
$\Delta_{T(2,N)}(q_{0})$ from
[$\Delta_{T(2,N)}$ closed form](#lem:alexander-T2N-closed-form):

| $N$ | $\Delta_{T(2,N)}(q_{0})$ | $(N-1) - \Delta$ | $\Delta E_{\mathrm{closure}}\ (\mathrm{kJ/mol})$ |
|:---:|:---:|:---:|:---:|
| 4   | 2.04 | 0.96 | 21.5 |
| 6   | 3.04 | 1.96 | 43.9 |
| 8   | 4.04 | 2.96 | 66.2 |
| 10  | 5.04 | 3.96 | 88.7 |
| 12  | 6.04 | 4.96 | 111.0 |
| 14  | 7.04 | 5.96 | 133.4 |

**Comparison with experiment and caveat.**
The predicted absolute barriers underestimate experimental closure /
aromatisation barriers (which lie in the $200\text{–}300\ \mathrm{kJ/mol}$
range) by a factor $5\text{–}10$, tracking the underprediction of
$\lvert q + q^{-1}\rvert_{\mathrm{mol}}$ documented in
[molecular crossing quantum](#prop:molecular-crossing-quantum).
The *ratios* between different $N$ are independent of any overall
rescaling of $\lvert q + q^{-1}\rvert_{\mathrm{mol}}$.
