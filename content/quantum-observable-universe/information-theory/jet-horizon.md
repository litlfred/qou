Let $U \subset M_0$ be an open subset of the descended universe carrying an affine chart. Let $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ be the brane tower .

A **jet horizon** in $U$ is a closed codimension-$1$ subset $\mathcal{H} \subset U$ such that every section of $A_0$ extending continuously across $\mathcal{H}$ vanishes on $\mathcal{H}$:

$$
  \mathcal{H}
  = 
  V\!\bigl(\mathfrak{h}\bigr),
  \qquad
  \mathfrak{h}
  = 
  \bigl\{
    s \in \Gamma(U, A_0)
     : 
    s|_{\mathcal{H}} = 0
  \bigr\}.
$$

The ideal $\mathfrak{h} \subset \Gamma(U, A_0)$ is the **horizon ideal**. At degree $0$, no fibre data crosses $\mathcal{H}$: photons ($K = \mathbf{1}_{B_4}$ 4-strand id, step $0$) cannot propagate across the horizon, and no zeroth-order observable distinguishes one side from the other.

**Higher-degree leakage.**
The horizon ideal lives strictly in $A_0$. The quotient algebras $A_k / A_0$ for $k \geq 1$ are not constrained by $\mathfrak{h}$. First-order (linear) and second-order (curvature) jet data can carry non-trivial sections across $\mathcal{H}$. 

| Jet degree | Data type | Crosses $\mathcal{H}$? |
|:---:|:---|:---:|
| $0$ | Fibre value (photon identity) | **No** |
| $1$ | Linear transport (winding number) | Yes |
| $2$ | Curvature (linking number) | Yes |
| $\geq 3$ | Higher-order topology | Yes |

The information that leaks through a jet horizon is exactly the degree $\geq 1$ jet data: the Taylor coefficients of the energy function beyond the constant term. This leakage is thermal in character. It carries no particle identity (degree $0$), only statistical correlations (degrees $1$ and $2$).
