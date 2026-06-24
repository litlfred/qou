The Skein relation weights positive crossings by $q$ and negative
crossings by $q^{-1}$:

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0.
$$

For $q > 1$, the per-crossing repulsive Coulomb correction relative to
a mixed-charge baseline is

$$
  \delta_{\mathrm{Coulomb}}
  =  q -  \tfrac{1}{2}(q + q^{-1})
  =  \tfrac{1}{2}(q - q^{-1})
   >  0,
$$

and the ratio of the antisymmetric (Coulomb) to symmetric (strong)
Skein weights is

$$
  \frac{q - q^{-1}}{q + q^{-1}}
  =  \tanh(\ln q).
$$

At $q = 1$ the asymmetry vanishes; at $q \to \infty$ the ratio
approaches $1$.

## Lean formalization

The companion Lean `skein_crossing_asymmetry` currently encodes a placeholder (`: True`); the intended statement ($q > 1 \Rightarrow \tfrac{1}{2}(q - q^{-1}) > 0$) is sketched in-file and deferred via `sorry` (`-- Ref: [manuscript]`).
