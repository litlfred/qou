The categorical-confinement proposition expresses every physical observable as a sum of Wedderburn residues, $\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi_\lambda$, with one term per Wedderburn channel $V_\lambda$. The content/twist eigenbasis organises these characters $\chi_\lambda$ by their ribbon-twist eigenvalue $\theta_\lambda = q^{2c(\lambda)}$, which is the scalar by which the full twist $\varDelta^2 \in Z(H_n(q))$ acts on $V_\lambda$. Three structural properties characterise each $\chi_\lambda(\beta)$:

1. **Parity.** For a braid word $\beta$ of length $L$, every Laurent exponent of $\chi_\lambda(\beta)(q)$ has the same parity as $L$. Equivalently, $\chi_\lambda(\beta)(-q) = (-1)^L\,\chi_\lambda(\beta)(q)$. This parity dictates which crossing-counts contribute to a given channel.
2. **Conjugation duality.** The sign-twisted map $\sigma_i \mapsto -\sigma_i^{-1}$ — an algebra automorphism, leaving the coefficients alone — swaps the seminormal eigenvalues $q \leftrightarrow -q^{-1}$ and so intertwines $V_\lambda$ with the conjugate channel $V_{\lambda'}$. At the level of characters this reads

   $$
     \chi_\lambda(-q^{-1}) = \chi_{\lambda'}(q),
   $$

   and combining it with the parity of item 1 gives the signed form $\chi_\lambda(q^{-1}) = (-1)^{L}\chi_{\lambda'}(q)$ for a braid word of length $L$. This conjugation duality represents the matter/antimatter symmetry of the channel weights.

   Two cautions. The intertwiner is **not** the [bar involution](bar-involution.md): that map sends $\sigma_i \mapsto \sigma_i^{-1}$ *together with* $q \mapsto q^{-1}$, and the two halves cancel on the spectrum, so it **fixes** each eigenchannel rather than exchanging them. The missing ingredient is the sign. And the sign in the displayed identity is $(-1)^L$, a function of the word, **not** a per-channel constant $\varepsilon_\lambda$: on every channel tested, including the self-conjugate $(2,1)$ of $H_3$, it takes both values as $L$ varies, as verified across all positive braid words of length $L \leq 6$ in $H_2$ and $H_3$.
3. **Framing rational.** Framing $\beta$ by $m$ full twists scales $\chi_\lambda$ by $\theta_\lambda^m$. The framing tower is given by the single-pole rational function $\chi_\lambda(\beta)/(1 - t\,\theta_\lambda)$, with its sole pole at $t = q^{-2c(\lambda)}$. This rational form determines how reframing redistributes weight across the tower.

These structural properties strictly derive from categorical inputs, namely the ribbon eigenvalue and the seminormal eigenvalue swap $q \leftrightarrow -q^{-1}$.
