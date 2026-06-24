**Proposition (q-Gaussian obstruction at the substrate value).** *At the
substrate parameter $q_0 \approx 1.10998 > 1$, the Bożejko–Speicher
non-commutative $q$-Gaussian does not exist as a probability measure.
As a quantitative witness, the would-be even moments*
$$
  T_n(q_0) \;=\; \sum_{\pi \in \mathcal{P}_2(2n)} q_0^{\,\mathrm{cr}(\pi)}
$$
*(the sum over perfect matchings $\pi$ of $[2n]$, weighted by crossing number
$\mathrm{cr}(\pi)$) diverge super-exponentially in $n$.*

## Consequence

Braid-word fluctuation statistics at $q_0$ **cannot** be modelled by the BS
$q$-Gaussian. The convergent substitutes are the *inner* Perron–Frobenius
dominant eigenvalue (a deterministic law-of-large-numbers limit) and the
*outer* Féray–Méliot $q$-Plancherel CLT (a genuine Gaussian-fluctuation limit
on the partition chain). This is the rigorous backing for the framing in
[`rem:markov-chain-fluctuations`](#rem:markov-chain-fluctuations): any
"$q$-Gaussian limit" invoked for braid observables at $q_0$ is mis-applying
the $|q| \le 1$ Bożejko–Speicher theory.
