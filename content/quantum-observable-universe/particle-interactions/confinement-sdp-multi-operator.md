**Remark.** Let $P_1$ and $P_2$ be [confined particles](#def:confined-particle) whose composite satisfies the [confinement SDP](#prop:confinement-sdp). Their **binding subword** is

$$
  W_{\mathrm{bind}}
  \;=\;
  \sum_{\lambda \in \mathcal{S}^*} y_\lambda^* \cdot \pi_\lambda \cdot \Phi^*
$$

where $\mathcal{S}^* = \{\lambda : y_\lambda^* > 0\}$ is the **active support** at optimum. The cardinality $|\mathcal{S}^*| \ge 1$ is the **binding multiplicity**:

* $|\mathcal{S}^*| = 1$ is the scalar LP regime (single-channel binding).
* $|\mathcal{S}^*| \ge 2$ is the generic multi-operator regime. It includes all shell-closure and magic-number configurations.

The optimality identity

$$
  \Phi^* \cdot \bigl(y_0^* I + \textstyle\sum_\lambda y_\lambda^* \pi_\lambda - T\bigr) \;=\; 0
$$

is a matrix equation, not a sum of scalar complementary-slackness relations. Its rank counts the **active dual support**—the number of Wedderburn blocks simultaneously coupled at the optimum. When the rank exceeds one, the confined state is a sum of operators from distinct blocks. The `electron-shell-ilp` witness observes this when it reports electrons alternating between $\sigma_1^{-1}$ and $\sigma_0^{-1}$: these are two tight dual blocks at the same $\Phi^*$.
