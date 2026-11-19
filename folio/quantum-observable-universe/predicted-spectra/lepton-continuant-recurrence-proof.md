## Proof

The Hecke relation $\sigma_0^2 = (q - q^{-1}) \sigma_0 + \mathbf{1}$ yields:

$$
  \sigma_0^{n+1}
  = \sigma_0 \cdot \sigma_0^n
  = \sigma_0 (a_n \cdot \mathbf{1} + b_n \cdot \sigma_0)
  = a_n  \sigma_0 + b_n  \sigma_0^2
  = a_n  \sigma_0 + b_n ((q - q^{-1}) \sigma_0 + \mathbf{1})
  = b_n \cdot \mathbf{1} + (a_n + h  b_n) \cdot \sigma_0.
$$

Extracting the coefficients gives $a_{n+1} = b_n$ and $b_{n+1} = a_n + h b_n = b_{n-1} + h b_n$. The initial conditions $a_0 = 1, b_0 = 0$ represent the identity. The initial conditions $a_1 = 0, b_1 = 1$ represent the single generator. This completes the induction.

## The lepton tower

At the aether parameter $q_0 \approx 1.1100$, the continuant yields the following normal form data for the three charged lepton generations:

| Lepton | Torus knot | $n$ | $a_n$ | $b_n$ | $\mathrm{net}$ |
|:------:|:----------:|:---:|:-----:|:-----:|:---------:|
| $e^-$  | $T_{2,3}$  | $3$ | $0.209$ | $1.044$ | $1.253$ |
| $\mu^-$ | $T_{2,5}$ | $5$ | $0.427$ | $1.133$ | $1.560$ |
| $\tau^-$ | $T_{2,7}$ | $7$ | $0.664$ | $1.272$ | $1.936$ |

The recurrence is exact in $\mathbb{Z}[q^{\pm 1}]$. The decimal values are evaluations at $q = q_0$.

## Structural content

Each additional factor of $\sigma_0^2$ in $T_{2,n+2}$ applies the Hecke relation once. This adds exactly $(q - q^{-1}) b_n$ to the $\sigma_0$ coefficient and shifts the identity coefficient by $b_n$. The lepton generations form a discrete tower indexed by odd $n$. The inter-generation spacing is controlled by $h = q - q^{-1}$.
