# Shell Operator Numerical Probe

The **SDP/LP optimum** identified numerically by
[sdp_on_shadows.py](https://github.com/litlfred/qou/blob/main/computations/sdp_on_shadows.py)
at $A_{\mathrm{magic}} = 8$ —
$(x_{(7,1)} = x_{(2,1^6)} = 35.24)$ — is precisely this self-dual
combination. This provides a numerical observation that aligns with the categorical prediction.

**Consequence for the ILP at level 4.**
*The shell-operator ILP*

$$
  \text{minimize}\;
  \sum_\lambda x_\lambda \cdot w_\lambda
  \;\text{s.t.}\;
  \sum_\lambda x_\lambda \cdot y_\lambda
  \;=\; y_{\mathrm{target}},
  \;\;
  x_\lambda \in \mathbb{Z}_{\geq 0},
$$

*admits a **constrained** formulation imposing $x_\lambda =
x_{\lambda^*}$, reducing the search space to self-dual vectors.
The constrained ILP has at most $\lceil p(A_{\mathrm{magic}})/2 \rceil$
variables (one per conjugate-equivalence class), yielding a
significant computational saving for large $A_{\mathrm{magic}}$.*
