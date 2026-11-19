**Algorithm (Jet-prefix transport in the $q \to 1$ classical neighbourhood).**
*Expand a rational Markov-trace observable $P_K(q) = \mathrm{tr}_M(\mathrm{NF}(K)) \in \mathbb{Q}(q)$ around $q = 1$ in powers of the quantum Planck step $\hbar_q = 1 - q^{-1}$, extract its exact order-$N$ jet $P_K^{(N)}(\hbar_q)$, and enclose the truncation remainder at $q = q_0$.*

### Input

- *Symbolic rational trace observable $P_K(q) = A_K(q) / B_K(q) \in \mathbb{Q}(q)$ with $B_K(1) \neq 0$ (from [Step 3](#alg:markov-trace) and [Step 7](#alg:gb-filtration)).*
- *Target jet order $N \in \mathbb{N}$ (or target enclosure tolerance $\varepsilon > 0$ at $q_0 > 1$).*

### Output

- *Exact degree-$N$ rational jet polynomial $P_K^{(N)}(\hbar_q) = \sum_{m=0}^{N} a_m\,\hbar_q^m \in \mathbb{Q}[\hbar_q]$ together with an explicit rational remainder polynomial $R_{K,N}(q)$ certifying $P_K(q) - P_K^{(N)}(\hbar_q) = \hbar_q^{N+1}\,R_{K,N}(q) / B_K(q)$.*

### Algorithm

1. **Substitute the classical coordinate:** Express $q = (1 - \hbar_q)^{-1}$ in $P_K(q) = A_K(q)/B_K(q)$ and clear powers of $(1 - \hbar_q)$ to obtain coprime polynomials $\tilde{A}_K(\hbar_q), \tilde{B}_K(\hbar_q) \in \mathbb{Q}[\hbar_q]$ with $\tilde{B}_K(0) \neq 0$.
2. **Truncated Newton series division:** Invert $\tilde{B}_K(\hbar_q) \bmod \hbar_q^{N+1}$ over $\mathbb{Q}$ by Newton iteration in $\mathbb{Q}[\hbar_q] / (\hbar_q^{N+1})$ and multiply by $\tilde{A}_K(\hbar_q) \bmod \hbar_q^{N+1}$ to obtain $P_K^{(N)}(\hbar_q) = \sum_{m=0}^{N} a_m\,\hbar_q^m$.
3. **Align length filtration and jet order:** Using the filtration correspondence of [Step 7](#alg:gb-filtration), match each $(q - q^{-1})^\ell$ reducer stratum to its leading $\hbar_q^\ell$ jet contribution, verifying that normal-form strata of crossing excess $> N$ enter only in $\hbar_q^{N+1}$ and above.
4. **Enclose the archimedean tail at $q_0$:** Form the exact algebraic numerator $\tilde{A}_K(\hbar_q) - \tilde{B}_K(\hbar_q)\,P_K^{(N)}(\hbar_q) = \hbar_q^{N+1}\,\tilde{R}_{K,N}(\hbar_q)$ and evaluate $\bigl|\hbar_{q_0}^{N+1}\,\tilde{R}_{K,N}(\hbar_{q_0}) / \tilde{B}_K(\hbar_{q_0})\bigr|$ in real ball arithmetic ($\ge 80$ decimal digits) to verify that the remainder is strictly below $\varepsilon$.

### Termination and Complexity

Newton inversion modulo $\hbar_q^{N+1}$ over $\mathbb{Q}$ requires $O(N \log N)$ polynomial operations; forming and bounding the exact algebraic remainder requires $O(N + \deg P_K)$ operations.

### Mathematical Justification

1. **Filtration-to-jet alignment:** [The jet-prefix filtration proposition](#prop:jet-prefix-gb-filtration) identifies the $(q - 1)$-adic jet order on $H_n(q)$ with the Gröbner–Shirshov filtration degree, ensuring that finite jet prefixes depend only on bounded-length Coxeter strata.
2. **Absence of higher-order mixing:** [Gröbner–Shirshov spectral-sequence collapse](#prop:gb-spectral-sequence) ($E_2$ degeneration) guarantees that no higher differential transports weight from degree $> N$ back into $P_K^{(N)}(\hbar_q)$.
