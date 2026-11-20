*Let $R$ be a field, $q \in R$ with $q \neq 0$ and $q^{2}+1 \neq 0$, and write $z = q^{3}/(q^{2}+1)$ (convention D) and $h = q - q^{-1}$. For a function $c$, consider the p-n interface averaging $\sigma_{c} = z - c\,h$. Then $\sigma_c$ is bar-invariant at $q$,*

$$
  \sigma_{c}(q) = \sigma_{c}(q^{-1}),
$$

*if and only if $\bigl(c(q) + c(q^{-1}) - 1\bigr)\,h = 0$. In particular, if $c$ is constant and $h \neq 0$, bar-invariance forces $2c = 1$: the uniform form $z - h/2$ is the only bar-invariant member with constant coefficient.*

## Proof

Under the bar involution $q \mapsto q^{-1}$ we have $\overline{h} = -h$ and $\overline{z} = z - h$, since $q^{-3}/(q^{-2}+1) = 1/(q(q^{2}+1)) = z - h$. Hence $\overline{\sigma_c} = z - h + \overline{c}\,h$, and $\sigma_c - \overline{\sigma_c} = (c + \overline{c} - 1)\,h$. For constant $c$ this is $(2c-1)\,h$, which vanishes with $h \neq 0$ only when $2c = 1$. $\square$

The result does not single out a canonical averaging. A $q$-dependent coefficient with $c + \overline{c} = 1$ is also bar-invariant, so uniqueness holds only among constant coefficients.

## Setting

The QOU mass identity at $A \geq 2$ contracts a per-interface averaging functional $\sigma_{pn}$ across the p-n boundary slice. The two production candidates are the uniform bar-invariant form $z - h/2$ and the Bring color-tube weighted form $z - h(1/2 - \delta/4)$.

> **Scope.** Only the uniform form satisfies bar-invariance. Writing
> $\overline{\phantom{x}}$ for $q \mapsto q^{-1}$, the flavour split is
> bar-mixed, $\overline{\delta} = -q^{2}\delta$, and
>
> $$
>   \overline{\sigma_{pn}^{\,\mathrm{weighted}}} - \sigma_{pn}^{\,\mathrm{weighted}}
>   \;=\; \frac{(q-1)^{5}(q+1)^{3}(q^{2}+1)}{12\,q^{5}}
>   \;\neq\; 0
>   \quad (q \neq 1),
> $$
>
> about $1.67 \times 10^{-5}$ at the substrate anchor, whereas the uniform form
> is bar-invariant exactly — it is the bar-symmetriser $\tfrac12(z + \overline{z})$
> of the p-p factor, since $\overline{z} = z - h$
> ([Proof of interface knot markov z](#prf:interface-knot-markov-z)).
>
> The colour-weighted coefficient $c = 1/2 - \delta/4$ depends on $q$ and has
> $c + \overline{c} - 1 = -\delta(1-q^{2})/4 \neq 0$, which is the computation above.
>
> The consequence is one of **scope**: the
> uniqueness statement covers constant coefficients, and the colour-weighted
> convention lies outside its hypotheses. This does not say the colour weighting
> is wrong, and it does not by itself bear on which convention should be
> canonical.

### Derivation chain for the closed-form weight

The substrate evaluation $w(t, t', q) = 1/(1 - h_q \cdot q^{10})$ derives from Bring's surface geometry:
- Bring's surface has genus $g = 4$.
- The genus-4 force-carrier pair is $\{T(2,9), T(3,5)\}$.
- We prove $\alpha_{\text{shift}}(T_{p,k}) = k \cdot (p-1)$. For $T(3,5)$, $\alpha_{\text{shift}}(T(3,5)) = 10$. This specifies the pole order of $\sigma$.
- The Bring color-tube weight inherits this derived pole order $q^{10}$.

All statements above are proved: $\overline{z} = z - h$ under convention D,
the bar-invariance criterion, the uniqueness among constant coefficients, and
the bar-invariance of $z - h/2$. In addition, two averagings with the same
9-pair colour weight agree. Choosing that weight is open.
