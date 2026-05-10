**Reading.** For any two confined particles
$P_1, P_2$ ([confined particle](#def:confined-particle))
whose composite satisfies the
[confinement SDP](#prop:confinement-sdp), the **binding subword**
is

$$
  W_{\mathrm{bind}}
  \;=\;
  \sum_{\lambda \in \mathcal{S}^*} y_\lambda^* \cdot \pi_\lambda \cdot \Phi^*
$$

where $\mathcal{S}^* = \{\lambda : y_\lambda^* > 0\}$ is the
**active support** at optimum.  The cardinality
$|\mathcal{S}^*| \ge 1$ is the **binding multiplicity**:

* $|\mathcal{S}^*| = 1$ recovers the scalar LP regime (single-channel
  binding);
* $|\mathcal{S}^*| \ge 2$ is the generic multi-operator regime and
  includes all shell-closure and magic-number configurations.

**Why complementary slackness is a matrix equation.**
The optimality identity

$$
  \Phi^* \cdot \bigl(y_0^* I + \textstyle\sum_\lambda y_\lambda^* \pi_\lambda - T\bigr) \;=\; 0
$$

is a **matrix** equality, not a sum of scalar complementary-slackness
relations.  Its rank counts the **active dual support** — the
number of Wedderburn blocks simultaneously coupled at the
optimum.  When the rank exceeds one, the confined state is a sum
of operators from distinct blocks, which is what the
`electron-shell-ilp` witness observes when it reports
"electrons alternate between $\sigma_1^{-1}$ and $\sigma_0^{-1}$":
those are two tight dual blocks at the same $\Phi^*$.
