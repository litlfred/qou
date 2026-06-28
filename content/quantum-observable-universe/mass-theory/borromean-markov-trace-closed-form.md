**Proposition (Borromean Markov trace closed form).**
*The Markov trace of the Borromean braid
$\beta_{\mathrm{Bor}} = (\sigma_1^{-1}\sigma_2)^3$ on $H_3(q)$,
evaluated via the Jones polynomial of the Borromean rings
$\mathcal{B}_3$, admits the exact closed form*

$$
  \boxed{\;\;
  \mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)
  \;=\;
  \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4},
  \;\;}
$$

*where $h = q - q^{-1}$ and $h^2 + 4 = [2]_q^2$.*
## Structural significance for the mass formula

The $h^2 = 0$ result separates the proton-mass $h$-dependence into
clean layers:

| Factor in $F_{\mathrm{Bor}} = \mathrm{tr}_M(\beta_{\mathrm{Bor}}) \cdot [3]_q! / q^3$ | $h^2$ coefficient | Source |
|---|---|---|
| $\mathrm{tr}_M(\beta_{\mathrm{Bor}})$ | $0$ | per-partition cancellation (this proposition) |
| $[3]_q! = (h^2 + 3)\sqrt{h^2 + 4}$ | $11/4$ | algebraic (q-factorial) |
| $q^3$ (denominator) | $9/8$ | algebraic ($q = (h + \sqrt{h^2+4})/2$) |
| $F_{\mathrm{Bor}}$ (combined) | $19/2$ | $11/4$ and $9/8$ via division |

The $h^2$ contribution to the linking weight
$\mathfrak{w}(\mathcal{B}_3)$ must come from the **normalization
layer** ($[3]_q! / q^3$), not from the braid character. The
Canonical Wedderburn $h^2$ coefficient $+3/4$ (per
`prop:lambda-scale-substrate-form`) is a **Geom-level contribution**,
structurally independent of the Markov trace.
