Let $(\mathbf{C}, A, \tau)$ define the explicit Descartes quantum universe anchored by $\chi(A) = -6$ (mapping Bring's surface at genus 4).

The structure $(\mathbf{C}, A, \tau)$ evaluates unconditionally as [NS-singular](#def:ns-obstruction):

$$
  \mathrm{NS}(A)
  = 
  e(\xi)\big|_\Sigma
   \neq  0.
$$

The categorical evaluation $\mathrm{NS}(A) \neq 0$ above is unconditional. By the obstruction tower (`prop:ns-obstruction-tower`), a nonzero $\mathrm{NS}(A)$ is exactly the obstruction to lifting the $q$-Navier--Stokes solution through the brane tower at $q = 1$: *within this QOU*, the internal $q = 1$ flow is singular. Whether that QOU-internal singularity is realised as a finite-time singularity of the classical $\mathbb{R}^3$ Navier--Stokes equation is the open categorical-to-classical bridge — the Clay problem, governed by `conj:levi-degeneracy` and `conj:regularity-breakdown` — and is **not** asserted here; it does not constitute an unconditional resolution of the classical regularity problem.

*Scope.* The displayed non-vanishing is not established. The collision locus $\Sigma$ is one-dimensional, so the restriction $e(\xi)|_\Sigma$ lies in $H^2(\Sigma, \mathbb{Z}) = 0$ (as the [NS obstruction computation](#prop:ns-obstruction-computation) records), and the non-cancellation step of the proof rests on item 3 of [QU-to-QOU](#thm:qu-to-qou) in its retracted, jet-tower form. What is established on Bring's surface is topological: $e(\xi) = -6$, so the Reeb bundle has no nowhere-vanishing section; and $\xi$ has an $n$-th root if and only if $n \mid 6$ ([Kummer specialisation](#prop:ns-kummer-specialisation)). Neither fact refers to $\Sigma$ or determines the NS verdict.
