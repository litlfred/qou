*The Wedderburn-weighted nuclear character signal $\delta^2\Phi(Z)$, computed purely from the substrate parameter $q_0$ (per-partition Hoefsmit characters at Hecke levels $k = 3\ldots 10$, with no empirical input), is **conjectured** to carry nuclear shell structure.*

*For each partition $\lambda \vdash k$ with Wedderburn weight $w_\lambda = \dim_q(\lambda)^2/[k]_q!$, the nuclear braid $\mathcal{N}(Z, Z)$ has character $\chi_\lambda(Z)$ computed from the Hoefsmit seminormal matrices. The cumulative Wedderburn-weighted signal*

$$
  \Phi(Z) = \sum_{k=3}^{K} \sum_{\lambda \vdash k} w_\lambda \, \ln|\chi_\lambda(Z)|
$$

*has forward second difference $\delta^2 \Phi(Z) = \Phi(Z) - 2\Phi(Z{-}1) + \Phi(Z{-}2)$, which at $K = 10$ and $q_0$ takes the values*

| $Z$ | $\delta^2 \Phi$ ($K{=}10$) | Magic? |
|----:|-----:|:------:|
| $8$ | $+33.25$ | $\star$ |
| $20$ | $+20.40$ | $\star$ |
| $28$ | $+4.43$ | $\star$ |

*These three values are reproducible from $q_0$ with no empirical input. What they do **not** establish is any relation between $\delta^2\Phi$ and the magic numbers; see the scope below.*

**Scope — this is a conjecture, and the tabulated values above are not evidence for it.** *Three measured facts bound what the signal can support. Each was obtained by re-running the producer over the full range $Z \le 32$, not by inspecting the three magic $Z$ alone.*

*1. **The sign of $\delta^2\Phi$ is a parity test.** Over $Z = 3 \ldots 31$ at $K = 10$, $\delta^2\Phi(Z) > 0$ holds precisely when $Z$ is even, with no exceptions. Every magic number is even, so the positivity property is satisfied by every even $Z$ and distinguishes none of them.*

*2. **The magic numbers are not maxima.** Among even $Z$ at $K = 10$ the local maxima are $Z \in \{4, 12, 16\}$ — none magic — and the global maximum is $Z = 12$. The magic $Z = 8$ ranks sixth of the fourteen even $Z$ in range, below the non-magic $Z = 10$ and $Z = 12$. The earlier reading of the table above as showing elevation **at** the magic numbers came from tabulating only magic $Z$; the non-magic contrast reverses it.*

*3. **No value of $q$ repairs this.** Sweeping $q$ across $1 < q < \varphi$ (49 points, $K = 8$) moves the peak monotonically downward through $Z$ — the global maximum runs $12 \to 16 \to 14 \to 12 \to 10 \to 8$ as $q$ rises — so the signal is genuinely $q$-dependent. But $Z = 20$ and $Z = 2$ are local maxima at **no** sampled $q$, and the best overlap with the magic set anywhere in the interval is two of four maxima. The parity property itself holds only for $q \lesssim 1.16$ and fails above.*

*What survives is the construction and its $q$-dependence, not the identification. Whether some other functional of the same Hoefsmit data carries shell structure is open; the second difference of the Wedderburn-weighted log-character, at any $q$ in the interval tested, does not. The selection principle remains open at [`prop:homological-shell-condensation`](../mass-endomorphism/homological-shell-condensation.md).*
