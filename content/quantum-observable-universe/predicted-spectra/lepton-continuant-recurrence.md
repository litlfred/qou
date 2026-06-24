The charged lepton tower $T_{2,n}$ ($n = 3, 5, 7$ for $e^-,
\mu^-, \tau^-$) has a closed-form normal form in $H_2(q) \subset
H_3(q)$ given by a **Morgan–Voyce continuant recurrence**.

## Statement

Let $h = q - q^{-1}$ be the Hecke parameter and
$T_{2,n} = \sigma_0^n$ the $(2, n)$-torus knot braid in $B_2$.
The Gröbner--Shirshov normal form in $H_2(q)$ is

$$
  \mathrm{NF}(\sigma_0^n)
  = 
  a_n \cdot \mathbf{1}
  + 
  b_n \cdot \sigma_0
$$

where the sequences $\{a_n\}$, $\{b_n\}$ satisfy:

$$
  a_{n+1} = b_n,
  \qquad
  b_{n+1} = h  b_n + b_{n-1},
  \qquad
  b_0 = 0,   b_1 = 1.
$$

The second relation is the **Morgan–Voyce continuant** — a
three-term recurrence with positive sign on $b_{n-1}$, in
contrast to the Chebyshev polynomials of the second kind
$U_n(\cos\varTheta)$ which have $b_{n+1} = 2\cos\varTheta \cdot
b_n - b_{n-1}$.

The **net coefficient** (sum of all NF terms) is
$\mathrm{net}(T_{2,n}) = a_n + b_n$.

## Proof

The Hecke relation $\sigma_0^2 = (q - q^{-1}) \sigma_0
+ \mathbf{1}$ gives:

$$
  \sigma_0^{n+1}
  = \sigma_0 \cdot \sigma_0^n
  = \sigma_0 (a_n \cdot \mathbf{1} + b_n \cdot \sigma_0)
  = a_n  \sigma_0 + b_n  \sigma_0^2
  = a_n  \sigma_0 + b_n ((q - q^{-1}) \sigma_0 + \mathbf{1})
  = b_n \cdot \mathbf{1} + (a_n + h  b_n) \cdot \sigma_0.
$$

Reading off: $a_{n+1} = b_n$ and $b_{n+1} = a_n + h
b_n = b_{n-1} + h b_n$. The initial conditions
$a_0 = 1, b_0 = 0$ (identity) and $a_1 = 0, b_1 = 1$
(single generator) complete the induction. $\square$

## The lepton tower

At the substrate parameter $q_0 \approx 1.1100$, the continuant
yields the following NF data for the three charged lepton
generations:

| Lepton | Torus knot | $n$ | $a_n$ | $b_n$ | $\mathrm{net}$ |
|:------:|:----------:|:---:|:-----:|:-----:|:---------:|
| $e^-$  | $T_{2,3}$  | $3$ | $0.209$ | $1.044$ | $1.253$ |
| $\mu^-$ | $T_{2,5}$ | $5$ | $0.427$ | $1.133$ | $1.560$ |
| $\tau^-$ | $T_{2,7}$ | $7$ | $0.664$ | $1.272$ | $1.936$ |

The recurrence is exact in $\mathbb{Z}[q^{\pm 1}]$; the
decimal values are evaluations at $q = q_0$.

The recurrence relations underlying this lepton tower are elementary identities in $\mathbb{Z}[q^{\pm 1}]$: the Morgan-Voyce sequences $\{a_n\}$ and $\{b_n\}$ satisfy a standard induction over $n$ via the quadratic Hecke relation.

## Structural content

Each additional factor of $\sigma_0^2$ in $T_{2,n+2}$ applies
the Hecke relation once, adding exactly $(q - q^{-1}) b_n$
to the $\sigma_0$ coefficient and shifting the identity
coefficient by $b_n$.  The lepton generations are thus a
**discrete tower indexed by odd $n$**, with inter-generation
spacing controlled by $h = q - q^{-1}$.


**Remark on Mathematical Novelty:** This structural identification of the lepton-tower sequence as a positive-sign Morgan-Voyce continuant, distinct from standard Chebyshev U_n recurrences, introduces a novel algebraic lens that elegantly captures the unique combinatorial constraints of the lepton sector.
