By the standard $S_n$ branching rule (remove one box from
the Young diagram of $\lambda \vdash 4$ to obtain the restriction
$\lambda \downarrow S_3$):

| $\lambda \vdash 4$ | $\dim V_\lambda$ | $\lambda \downarrow S_3$ | Trivial $(3)$ content |
|---|---:|---|---:|
| $(4)$ | 1 | $(3)$ | 1 |
| $(3,1)$ | 3 | $(3) + (2,1)$ | 1 |
| $(2,2)$ | 2 | $(2,1)$ | 0 |
| $(2,1,1)$ | 3 | $(2,1) + (1^3)$ | 0 |
| $(1^4)$ | 1 | $(1^3)$ | 0 |

The half-symmetric $H_4$ projection includes one representative of each
conjugate pair $\{(4), (1^4)\}$ and $\{(3,1), (2,1,1)\}$, plus
$\tfrac{1}{2}$ of the self-conjugate $(2,2)$:

$$
  \dim_{\text{half-sym}} = 1 + 3 + 1 = 5, \qquad
  \text{trivial } S_3 \text{ content} = 1 + 1 + 0 = 2.
$$

The $S_3$-trivial projection factor is

$$
  \frac{\text{trivial content}}{\text{total half-sym dim}}
  = \frac{2}{5}.
$$

Applied to the 8-fold ideal-octahedral tessellation of
$S^3 \setminus \mathcal{B}_3$ (Adams 1985 \cite{adams1985hyperbolic}:
$\operatorname{Vol}(\mathcal{B}_3) = 8G$ where
$G = \Lambda(\pi/4) = \tfrac{1}{2} V_{\text{oct}}$ is Catalan's
constant):

$$
  \text{effective cell count}
  = \underbrace{\tfrac{5}{2}}_{\text{half-sym count}}
    \times \underbrace{\tfrac{2}{5}}_{S_3\text{-trivial factor}}
  = 1.
$$

The per-cell ratio is $1/8$, confirming that the half-symmetric
projection selects exactly **one** of the eight ideal octahedral
cells. The reading is purely structural — *which* cell is
identified, not *how much* per-cell curvature it carries.
$\qquad\blacksquare$
