The left trefoil $T_{2,3}$ and the right trefoil
$T_{2,3}^{\sigma}$ are the **electron** and **positron**
respectively.  The choice of which chirality is assigned to
which particle is arbitrary — it is a convention, not a
physical distinction.  What matters is that the two are
**mirror images**: $T_{2,3}^{\sigma}$ is $T_{2,3}$ with all
crossings reversed.

**Antiparticles from crossing reversal.**

An **antihadron** is the hadron constructed from positrons
instead of electrons: replace every $T_{2,3}$ with
$T_{2,3}^{\sigma}$ in the knot formula.  The proton's
antiquark content is obtained by mirroring:

$$
  \mathfrak{p}^{\sigma}
  = 
  [u^{\sigma}, u^{\sigma}, d^{\sigma}]_p \oplus \mathcal{L}_H
$$

where $u^{\sigma} = T_{2,3}^{\sigma}$ and
$d^{\sigma} = (T_{2,3}^{\sigma})^{\sigma} = T_{2,3}$.  The
crossing energy of $\mathfrak{p}^{\sigma}$ has the opposite sign
to that of $\mathfrak{p}$: the Coulomb charge reverses,
$Q(\mathfrak{p}^{\sigma}) = -1$.

**Time reversal and the exceptional divisor.**

If a trefoil can **change chirality** — passing from $T_{2,3}$
to $T_{2,3}^{\sigma}$ — while traversing the exceptional divisor
of the brane tower, this would correspond to a particle
travelling **backward in time** (in the Feynman--Stueckelberg
sense: an electron moving forward in time is a positron moving
backward).

The fiber adjoint involution
([fiber adjoint involution](#prop:fiber-adjoint-involution))
acts on the weight decomposition and reverses the sign of the
Reeb flow direction.  If this involution extends to the
exceptional divisor, it could provide the mechanism for
chirality reversal — the vortex tube of the electron reverses
its winding orientation as it passes through the blow-up.

**Open questions.**

1. **Vortex inversion**: can a vortex tube in the brane fluid
   reverse its circulation?  Classical fluid dynamics has
   results on vortex reconnection and reversal — these should
   be translated to the categorical setting.

2. **Information transfer**: if a trefoil reverses chirality
   twice (electron $\to$ positron $\to$ electron), this would
   constitute a round-trip through the time-reversed sector.
   Does the categorical algebra forbid this?  The fiber adjoint
   involution is an involution ($\sigma^2 = \mathrm{id}$), so
   the double reversal returns to the original state — but
   whether information is preserved across the round-trip
   depends on the monodromy of the exceptional divisor.

3. **The imaginary part**: in the Archimedean realisation over
   $\mathbb{C}$, the substrate parameter $q$ can be complex.
   The observability axiom (fibre functor) forces $q$ to be
   real and positive (via the involutive structure), but the
   **imaginary part of $q$** — if it were nonzero — would
   contribute a phase to the crossing energy that distinguishes
   particles from antiparticles without requiring mirror
   reflection.  This suggests that the full theory (before
   restricting to the observable sector) may have a richer
   structure in which chirality reversal is a continuous
   rotation, not a discrete flip.

4. **CPT from the categorical algebra**: the combined operation
   C (charge conjugation = crossing reversal $\sigma$),
   P (parity = spatial reflection), T (time reversal = Reeb
   flow direction) should be derivable from the fiber adjoint
   involution and the Frobenius structure.  The CPT theorem
   (CPT is always a symmetry) would then be a consequence of
   the involutive axiom on the QOU.
