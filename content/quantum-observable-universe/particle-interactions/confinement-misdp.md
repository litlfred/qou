**Reading.** When operator counts are constrained to integers—as in the confinement hierarchy at levels $\ell \le 3$ where crossing multiplicities must be integral—the feasible region of the [confinement SDP](#prop:confinement-sdp) becomes:

$$
  \Phi \succeq 0
  \;\wedge\;
  \mathrm{rank}\text{-content}(\Phi) \in \mathbb{Z}_{\ge 0}^{|\mathcal{S}|}.
$$

We solve this Mixed-Integer Semidefinite Program (MISDP) via continuous SDP relaxation combined with branch-and-cut (see `computations/misdp_cross_channel.py`). This strictly matches the confinement framework at every level of the hierarchy.
