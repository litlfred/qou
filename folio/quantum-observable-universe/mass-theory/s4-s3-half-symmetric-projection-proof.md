**Proof.** By the standard $S_n$ branching rule (remove one box from
the Young diagram of $\lambda \vdash 4$ to obtain the restriction
$\lambda \downarrow S_3$):

| $\lambda \vdash 4$ | $\dim V_\lambda$ | $\lambda \downarrow S_3$ | Trivial $(3)$ content |
|---|---:|---|---:|
| $(4)$ | 1 | $(3)$ | 1 |
| $(3,1)$ | 3 | $(3) + (2,1)$ | 1 |
| $(2,2)$ | 2 | $(2,1)$ | 0 |
| $(2,1,1)$ | 3 | $(2,1) + (1^3)$ | 0 |
| $(1^4)$ | 1 | $(1^3)$ | 0 |

The half-symmetric part takes one representative of each conjugate pair
$\{(4), (1^4)\}$ and $\{(3,1), (2,1,1)\}$, with weight $1$, and the
self-conjugate $(2,2)$ with weight $\tfrac{1}{2}$:

$$
  \dim_{\text{half-sym}} = 1 + 3 + \tfrac{1}{2}\cdot 2 = 5, \qquad
  \text{trivial } S_3 \text{ content} = 1 + 1 + \tfrac{1}{2}\cdot 0 = 2.
$$

Hence the $S_3$-trivial share is $2/5$. $\square$
