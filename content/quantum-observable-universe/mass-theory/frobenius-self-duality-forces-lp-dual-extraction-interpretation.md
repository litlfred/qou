**Remark (categorical content).** The Frobenius self-duality
holds at the categorical level: the rigid monoidal category
$\mathbf{Rep}(H_n(R,q))$ is self-dual under the
$\tau$-pairing, and $\tau$ is precisely the categorical trace
$\mathrm{tr}_C$ on the unit object. The "primal vs. dual"
distinction in the LP is a $K$-theoretic shadow of the
categorical self-duality; there is no other choice.

## Lean formalization

The companion Lean encodes `observationFrame`, `frobeniusSelfDualityMap`, and the theorem `frobenius_self_duality_forces_lp_dual_extraction`, with the construction deferred via `sorry` (`-- Ref: [manuscript]`).
