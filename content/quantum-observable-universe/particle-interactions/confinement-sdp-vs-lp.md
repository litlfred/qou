**Reading.** The scalar [confinement LP](#prop:confinement-lp)
is obtained from the [confinement SDP](#prop:confinement-sdp)
by restricting $\Phi$ to the diagonal span of the NF basis
$\{b_i\}$ and dropping the 2$\times$2 pair blocks.  Equivalently:
the LP is the SDP with the rank-1 restriction
$\Phi = \mathrm{diag}(x)$ and the simplification
$\pi_\lambda \mapsto \mathbf{1}_\lambda$ (indicator vector).

Consequences:

* The LP is **exact** when every Wedderburn block is
  one-dimensional (no cross-channel coupling).
* In general the LP is a **lower bound** on the SDP and misses
  the multi-operator binding structure described in the
  [multi-operator remark](#rem:confinement-sdp-multi-operator).

For most baryonic and light-nuclear configurations the
Wedderburn decomposition has 1-dimensional blocks and the LP
suffices; magic-number and shell-closure configurations require
the SDP.
