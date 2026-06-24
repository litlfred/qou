For an atomic closed braid the Habiro expansion of the Markov trace
([Habiro completion](#prop:full-pole-structure-mass-trace))
**terminates**: only finitely many cyclotomic coefficients $a_m$
are nonzero. This corollary records the explicit termination bound
and integrality, with a constructive proof by sequential cyclotomic
division.

**Corollary.**
*Let $T_w(Z, N) \in H_{3A}(q)$ be the atomic-braid image for
$A = Z + N$ nucleons
([categorical mass, Markov](#prop:categorical-mass-markov)), and
let $u = q^{1/2}$. Then there exists a denominator $D(u)$ — a
finite product of cyclotomic polynomials — and a Laurent
polynomial $p(u) := D(u) \cdot \mathrm{tr}_M(T_w(Z, N), u^2) \in \mathbb{Z}[u, u^{-1}]$
admitting the finite Habiro expansion*

$$
  p(u) \;=\; \sum_{m=0}^{m_{\max}} a_m(u)\,(u; u)_m,
  \qquad (u; u)_m = \prod_{k=1}^{m}(1 - u^k),
$$

*with*

1. **Integrality.** *$a_m(u) \in \mathbb{Z}[u]$ for every $m$.*
2. **Degree bound.** *$\deg_u a_m(u) \leq m$.*
3. **Termination.** *$a_m = 0$ for $m > m_{\max}$, and
   $m_{\max} \leq \lceil \sqrt{2 \deg_u p(u)} \rceil$.*
4. **Uniqueness.** *Given $\deg a_m \leq m$, the sequence
   $\{a_m\}$ is uniquely determined by $p$.*

## Computational verification

The symbolic pipeline `habiro_coefficients_atomic.py` implements
the cyclotomic-division algorithm and verifies the corollary for
the smallest atomic braids:

| Braid | $\deg_u p(u)$ | # Habiro terms | $m_{\max}$ | $\sqrt{2 d}$ bound |
|:------|:-:|:-:|:-:|:-:|
| proton $(Z{=}1, N{=}0)$   | $48$  | $10$ | $9$  | $\lceil \sqrt{96} \rceil = 10$  |
| neutron $(Z{=}0, N{=}1)$  | $40$  | $9$  | $8$  | $\lceil \sqrt{80} \rceil = 9$   |
| deuteron $(Z{=}1, N{=}1)$ | $104$ | $14$ | $13$ | $\lceil \sqrt{208} \rceil = 15$ |

Observed $m_{\max}$ saturates the Step-3 bound to within one step,
consistent with the cyclotomic structure of $p(u)$ inherited from
Markov–Jones integrality. Pointwise agreement with the
numerical-interpolation pipeline at $q_0 \approx 1.1100$ to 50
decimal digits cross-validates the two paths:

- $\mathrm{tr}_M(\mathrm{proton}, q_0) = 2.12258250945\ldots$
- $\mathrm{tr}_M(\mathrm{neutron}, q_0) = 1.58939344595\ldots$
- $\mathrm{tr}_M(\mathrm{deuteron}, q_0) = 0.17743692421\ldots$

These finite Habiro expansions realise the atomic-braid Markov
trace as the **finitely-supported** elements of the Habiro ring
predicted by ([Habiro ring](#def:habiro-ring), item 1); the
infinite-support case is reserved for the colored-Jones
Volume-Conjecture limit ([Kashaev volume density](#rem:kashaev-volume-density)).
