Virtual particles mediate forces as off-shell excitations. The Heisenberg relation $\Delta E \cdot \Delta t \gtrsim \hbar$ limits their existence. The QOU framework localizes them geometrically.

**The exceptional divisor as the virtual stage.**

The blow-up replaces each brane point $p \in M$ with an [exceptional divisor](#def:exceptional-divisor) $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$. This sphere parametrizes internal departure directions invisible from the base manifold.

A virtual particle operates within the Reeb bundle over $\mathcal{S}_p$. This is the Hopf fibration $U(1) \hookrightarrow S^3 \to \mathcal{S}_p$ where braiding occurs ([vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor)). The excitation originates at the blow-up locus, propagates through the [brane tower](#def:recursive-brane-tower), and is reabsorbed before reaching the base level $A_0$.

**Brane tower levels as virtual depth.**

The [recursive brane tower](#def:recursive-brane-tower) $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ stratifies excitations by [jet prolongation](#prop:jet-prolongation) level:

| Tower level | Algebra | Physical interpretation |
|-------------|---------|----------------------|
| $A_0 = A$ | $\mathcal{O}(\mathrm{SU}(2))$ | On-shell particles |
| $A_1 = J^1(A_0)$ | Frame bundle sections | 1-virtual (gauge bosons) |
| $A_2 = J^1(A_1)$ | Second jet sections | 2-virtual (curvature fluctuations) |
| $A_n$ | $n$-th jet sections | $n$-virtual |

The state space expands with virtual depth. Projection to $A_0$ collapses this structure.

**Non-observability of virtual particles.**

Level $A_n$ ($n \geq 1$) excitations remain invisible at $A_0$. The canonical projection $\pi_0 \colon A_n \to A_0$ annihilates $\Omega^1$ components:

$$
  \pi_0(f \otimes \omega_1 \otimes \cdots \otimes \omega_n)
  = 
  f \cdot \varepsilon(\omega_1) \cdots \varepsilon(\omega_n).
$$

For a form $\omega$ lacking a constant part ($\varepsilon(\omega) = 0$), the projection yields zero. The excitation projects no shadow onto $A_0$. This mimics "off-shell" behaviour.

**Lifetime from the Heisenberg commutator.**

The [Heisenberg commutator](#rem:heisenberg-commutator) at level $n$ is

$$
  [\hat{X}, \hat{P}]_{q_n} =  J\hbar_{q_n}, \qquad
  \hbar_{q_n} =  1 - q_n^{-1}.
$$

The uncertainty bound $\Delta E \cdot \Delta t \geq \hbar_{q_n} / 2$ restricts the level-$n$ excitation lifetime:

$$
  \Delta t_{\text{virtual}}
   \leq 
  \frac{\hbar_{q_n}}{2\Delta E}.
$$

The excitation remains within the tower, never descending to $A_0$.
