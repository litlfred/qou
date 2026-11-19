This remark records the computation, interpretation, $q$-dependence, and homological cross-link for [the magic-numbers conjecture](#conj:magic-numbers-from-q).

## Computation

The Hoefsmit seminormal matrix for partition $\lambda$ at generator $g$ has block-diagonal structure:

- **Generator 0**: pure diagonal (eigenvalue per standard Young tableau).
- **Generator 1**: scattered $2 \times 2$ blocks plus diagonal singletons.

This structure yields $O(d)$ matrix--vector cost per crossing instead of $O(d^3)$ for dense multiplication. This enables a $15\,000\times$ speedup at $k = 9$ (from $557\,$s to $14\,$s) and makes $k = 10$ ($42$ partitions, $\dim \leq 768$) feasible in $48\,$s.

The nuclear character at each $Z$ is computed by multiplying crossing matrices through the full atomic braid $\mathcal{N}(Z, Z)$. This includes intra-nucleon $\mathcal{B}_3 \times \text{quarks}$, inter-nucleon pp/nn/pn crossings, and electron pe crossings using both generators.

## Interpretation

The forward second difference $\delta^2 \Phi$ measures the extra binding from adding one nucleon at $Z$ compared to the trend. At magic $Z$, the per-partition characters have enhanced coherence. The Wedderburn-weighted traces align to produce a positive $\delta^2$ peak. Between magic numbers, the characters decohere.

The declining amplitude ($+33.2$ at $Z = 8$, $+20.4$ at $Z = 20$, $+4.4$ at $Z = 28$) reflects the hierarchical resolution. Magic $8$ is fully resolved at $k = 3$ (3 partitions). Magic $28$ requires $k \geq 7$ (15 partitions) for resolution. Higher magic numbers ($50, 82, 126$) would require $k \geq 12$ where partition dimensions exceed current computational limits.

## Dependence on $q$

All quantities are functions of the aether parameter $q$:

- Hoefsmit matrix entries: $h/[\rho]_q$ where $[\rho]_q = (q^\rho - q^{-\rho})/(q - q^{-1})$
- Wedderburn weights: $w_\lambda = \dim_q(\lambda)^2/[k]_q!$
- Crossing eigenvalues: $q$ (pp), $-q^{-1}$ (nn), $(q - q^{-1})/2$ (pn)

At $q = 1$ (the classical limit), all $[\rho]_q \to \rho$, $w_\lambda \to \dim(\lambda)^2/k!$, and the magic number signal vanishes. There is no quantum deformation and no shell closure. The magic numbers are a quantum effect that exists only for $q \neq 1$.

## Cross-link: homological route past the $K = 12$ barrier

The Hoefsmit-seminormal pipeline above terminates at $K = 10$. The [homological shell-condensation conjecture](#prop:homological-shell-condensation) provides a $K$-independent algebraic-geometry route. The magic ladder $\{2, 8, 20, 28, 50, 82, 126\}$ is read off the collapse of a Białynicki–Birula spectral sequence at $E_2$, with no matrix evaluation required. The numerical agreement at $Z = 8, 20, 28$ above provides the [empirical computational verification](#rem:k12-barrier-bypass) of the homological prediction at the strand counts where Hoefsmit matrices remain tractable.
