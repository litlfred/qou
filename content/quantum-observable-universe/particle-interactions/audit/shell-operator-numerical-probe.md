# Shell Operator Numerical Probe

The numerical SDP/LP optimum, identified by [sdp_on_shadows.py](https://github.com/litlfred/qou/blob/main/computations/sdp_on_shadows.py) at $A_{\mathrm{magic}} = 8$, evaluates to $x_{(7,1)} = x_{(2,1^6)} = 35.24$. This is precisely the self-dual combination. The numerical observation aligns perfectly with the categorical prediction.

**Consequence for the ILP at level 4.**
*The shell-operator ILP is given by:*

$$
  \text{minimize}\;
  \sum_\lambda x_\lambda \cdot w_\lambda
  \;\text{s.t.}\;
  \sum_\lambda x_\lambda \cdot y_\lambda
  \;=\; y_{\mathrm{target}},
  \;\;
  x_\lambda \in \mathbb{Z}_{\geq 0}.
$$

*This admits a constrained formulation imposing $x_\lambda = x_{\lambda^*}$. This reduces the search space to self-dual vectors. The constrained ILP has at most $\lceil p(A_{\mathrm{magic}})/2 \rceil$ variables (one per conjugate-equivalence class). This yields significant computational savings for large $A_{\mathrm{magic}}$.*
