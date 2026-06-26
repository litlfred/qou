Let $(\mathbf{C}, A, \tau)$ be the Descartes quantum universe
with $\chi(A) = -6$ (Bring's surface of genus 4).

Then $(\mathbf{C}, A, \tau)$ is
[NS-singular](#def:ns-obstruction):

$$
  \mathrm{NS}(A)
  = 
  e(\xi)\big|_\Sigma
   \neq  0.
$$

The classical 3-dimensional Navier--Stokes equation admits
smooth initial data for which the solution develops a
singularity in finite time.

*Proof.*
The [NS obstruction](#def:ns-obstruction) is
$\mathrm{NS}(A) = \kappa_0|_\Sigma$ where
$\mathrm{tr}(\kappa_0) = \chi(A) = -6$.

**Step 1** (arithmetic).
For $\kappa \geq 4$, $2\kappa \geq 8 > 6 = |\chi(A)|$, so
$2\kappa \nmid -6$.  By the
[Kummer specialisation](#prop:ns-kummer-specialisation),
$\kappa_0 \bmod 2\kappa \neq 0$ for all $\kappa \geq 4$.  The
obstruction survives through infinitely many levels of the
Kummer tower.

**Step 2** (algebra).
The [perpetual obstruction](#thm:qu-to-qou) (item 3) says
$\kappa_0$ and the jet corrections $\delta_n$ live in
complementary subgroups of $H^2(\mathcal{S}, \mathcal{B})$.
The total obstruction $\kappa_n|_\Sigma = \kappa_0|_\Sigma
+ \delta_n|_\Sigma$ is nonzero because the topological term
$\kappa_0|_\Sigma \neq 0$ cannot be cancelled by the analytic
term $\delta_n|_\Sigma$.

**Step 3** (geometry).
$\mathrm{NS}(A) \neq 0$ implies, via the
[core-Levi equivalence](#prop:core-levi-form), that the
Levi form stays non-degenerate at the collision locus: the
contact structure does not degenerate.

**Step 4** (dynamics).
Non-degenerate Levi form implies bounded core aspect ratio,
which gives the [vorticity lower
bound](#prop:vorticity-lower-bound)
$\|\omega\|_\infty \geq c/(T^*-t)$, which gives
[BKM divergence](#thm:q-bkm) $\int \|\omega\|_\inftydt = \infty$.
