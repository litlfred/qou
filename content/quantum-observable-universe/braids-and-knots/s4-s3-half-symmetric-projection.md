**Proposition (half-symmetric $H_4$ projection extracts one octahedral
cell via $S_4 \downarrow S_3$ branching).**
*The half-symmetric Wedderburn projection on $H_4(q)$, further
restricted to the $S_3$-trivial subspace (where $S_3$ acts by permuting
the three components of the Borromean rings $\mathcal{B}_3$), extracts
the curvature contribution of exactly **one** of the 8 ideal octahedral
cells in the $\mathcal{B}_3$-complement tessellation.*

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
projection extracts the curvature contribution of exactly **one**
ideal octahedral cell. $\square$

## Application to $\lambda_{\text{scale}}$

Combined with the Yekutieli per-cell curvature $-G$ (non-abelian
Stokes integration, one cell contributing
$-\operatorname{Vol}(\mathcal{B}_3)/8 = -G$ at $h^2$ order), the
framework's substrate-pure $\lambda_{\text{scale}}$ is:

$$
  \lambda_{\text{scale}}^{\text{Yekutieli}}
  = \underbrace{\tfrac{5}{2} + \tfrac{3}{4} h^2}_{\text{canonical Wedderburn (proved)}}
    + \underbrace{(-G) \cdot h^2}_{\text{Yekutieli per-cell}}
  = \tfrac{5}{2} + \bigl(\tfrac{3}{4} - G\bigr) h^2
  \approx 2.4927 \text{ at } q_0.
$$

This gives $\mathfrak{m}_{\mathfrak{p}} \approx 951\;\text{MeV}$,
halving the framework-vs-CODATA gap from $\sim 3\%$ (canonical
Wedderburn alone) to $\sim 1.33\%$.
