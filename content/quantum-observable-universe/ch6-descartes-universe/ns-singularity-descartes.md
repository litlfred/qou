Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with
$\chi(A) = -6$ (Bring's surface of genus 4).

The classical 3-dimensional Navier--Stokes equation, realised as
the $q = 1$ specialisation of the
[q-NS system](#def:q-navier-stokes) on the
[substrate line bundle](#def:substrate-line-bundle), admits
smooth initial data for which the solution develops a singularity
in finite time.

That is: the Descartes universe is
[NS-singular](#def:ns-regular-qou).

*Proof.*  The argument assembles five components, each
independently established.

**Step 1.  Observability at $q = 1$.**
The [observability axiom](#def:quantum-observable-universe)
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
is a property of the base $(\mathbf{C}, A, \tau)$ and does not
depend on the substrate section $q$
([Theorem](#thm:observability-q-independent)).  It holds at
$q = 1$.

**Step 2.  Observability implies Levi non-degeneracy.**
In the archimedean realisation, observability is
$H^0(M, \mathrm{Ad}(P)) = 0$: the holonomy group of the
$\mathrm{SU}(2)$ connection has no fixed vectors in
$\mathfrak{su}(2)$.  By the
[core-Levi equivalence](#prop:core-levi-form), this is
equivalent to the Levi form $\mathcal{L}_\theta$ being
non-degenerate on every normal plane, including at the
collision locus $\Sigma$ of an anti-parallel vortex pair.

**Step 3.  Non-degeneracy implies bounded core aspect ratio.**
By [Proposition](#prop:core-levi-form)(c), Levi non-degeneracy
implies the core aspect ratio
$\kappa(t) = a_\perp/a_\parallel$ is bounded:
$\sup_{t < T^*} \kappa(t) \leq C < \infty$.

**Step 4.  Bounded aspect ratio implies vorticity blowup.**
By the [vorticity lower bound](#prop:vorticity-lower-bound),
bounded $\kappa$ implies
$\|\omega^*(t)\|_{L^\infty} \geq c/(T^* - t)$.  This
diverges as $t \to T^{*-}$.

**Step 5.  Vorticity blowup implies loss of regularity.**
By the [q-BKM criterion](#thm:q-bkm),
$\int_0^{T^*} \|\omega^*\|_\infty\,dt = +\infty$ implies
the solution $v^*$ is not smooth on $[0, T^*]$.

**The logical chain.**

$$
  \underset{\text{(base property)}}{\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0}
  \;\Longrightarrow\;
  \underset{\text{(archimedean)}}{\mathcal{L}_\theta \text{ non-deg.}}
  \;\Longrightarrow\;
  \underset{\text{(geometry)}}{\kappa = O(1)}
  \;\Longrightarrow\;
  \underset{\text{(Biot--Savart)}}{\|\omega\| \geq c/(T^*\!-t)}
  \;\Longrightarrow\;
  \underset{\text{(BKM)}}{\text{blowup.}}
$$

No step uses an analytic limit.  The observability condition
is categorical (Step 1).  The Levi equivalence is algebraic
(Step 2).  The aspect ratio bound is geometric (Step 3).
The vorticity estimate is ODE (Step 4).  The BKM criterion
is classical real analysis (Step 5).

The $q \to 1$ limit appears only in the
[q-Aubin--Lions](#thm:q-aubin-lions) construction of the
initial data (producing a weak solution from the q-NS family).
Once the weak solution exists, Steps 1--5 are applied to it
without any limit.
