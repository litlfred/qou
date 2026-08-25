Read the Frobenius/Markov trace $\mathrm{tr}_M = \sum_{\lambda} y_\lambda(q)\,\chi_\lambda$ as a statistical-mechanics partition function, with the Wedderburn blocks $\lambda$ as microstates. At inverse temperature $\beta = \ln q$ (positive for $q > 1$), each positive weight $y_\lambda(q)$ is the Boltzmann weight of block $\lambda$, whose energy is

$$
  E_\lambda = -\frac{\ln y_\lambda(q)}{\ln q}.
$$

This energy is the unique solution of $e^{-\beta E_\lambda} = y_\lambda$, and it is order-reversing in the weight:

$$
  E_{\lambda_1} \le E_{\lambda_2} \iff y_{\lambda_2} \le y_{\lambda_1},
$$

so the dominant Wedderburn block — the one with the largest Frobenius weight — is the ground state. Summing the Boltzmann weights over the blocks with their degeneracies $d_\lambda$ recovers the Frobenius weighted sum,

$$
  \sum_{\lambda} d_\lambda\, e^{-\beta E_\lambda} = \sum_{\lambda} d_\lambda\, y_\lambda,
$$

so the statistical-mechanics partition function written in energy variables and the Frobenius weighted sum are the same object in two bases.
