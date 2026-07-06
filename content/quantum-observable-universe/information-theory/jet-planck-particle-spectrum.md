Each Planck step is one jet prolongation ([jet-Planck steps](#rem:jet-planck-steps)). The crossing number governs the particle content resolvable at each step.

**Particle content at each step.**
The crossing number of a knot is the number of $R$-matrix applications in its braid word. Each application is one action of $\nabla_q$, one jet prolongation, and one Planck step. Therefore, the crossing number equals the minimum jet order at which a knot first becomes resolvable.

A particle with crossing number $c$ cannot exist before step $c$. The $c$-th jet is the first Taylor order with sufficient polynomial degree to encode $c$ crossings of the braid closure.

See [Table 1](#tbl:jet-planck-steps-table1-data).

**Step 0: only the photon.**
Before any transport, only the fiber value exists. The photon is $K = \varnothing$, the empty knot ([photon wavefront example](#ex:photon-wavefront)). It is background flux on the state bundle with no topological identity. It requires no braiding, no crossings, and no connection. It is pre-geometric: it exists at the zeroth jet because it *is* the zeroth jet. The photon is its own antiparticle.

**Step 1: neutrino and antineutrino.**
The first application of $\nabla_q$ creates horizontal transport, enabling winding around the fiber. The unknot $0_1$ is a circle with zero crossings. It winds once around the Reeb direction with trivial braiding ([neutrino](#def:neutrino-knot)). Its Jones polynomial $J_\nu(q) = 1$ is a degree-0 polynomial. This is consistent with the linear (degree 1) jet, where the only available structure is a single winding with slope but no self-intersection.

The unknot is amphichiral: $T_{1,0} \cong T_{1,0}^{\sigma}$ as unoriented knots ([antineutrino](#def:antineutrino-knot)). The neutrino $\nu$ and antineutrino $\nu^{\sigma}$ are the same knot, distinguished by orientation (framing), not by knot type. Both appear at step 1. This degenerate matter-antimatter pair is topologically identical, differing only in the sign of the Reeb winding.

The neutrino has zero crossing chirality ($Q(\nu) = 0$), zero hyperbolic volume, and mass arising entirely from vacuum drag: $m_\nu \sim \mu_0 \cdot (q - 1)$. It is the lightest possible matter—the minimum topological excitation above the photon vacuum.

**Step 2: the Hopf link (bosons).**
The Hopf link $L2a1$ comprises two unknots linked once. The linking number is $1$, which requires detecting curvature (the failure of parallel transport around a loop to return to the identity). This is exactly the Hessian $d^2E$: the quadratic jet detects the first non-trivial holonomy.

Bosons are links with an even number of components ([fermion--boson decomposition](#prop:fermion-boson-knot-link)): $T(2,n)$ with $n$ even. The simplest is $T(2,2) = L2a1$ (gluon), which exists at step 2. The linking energy is the first binding—two fibers correlated by curvature. The gluon is its own antiparticle because the Hopf link is amphichiral.

At step 2, there is no chirality. The quadratic jet has a discriminant but no handedness. All particles so far (photon, $\nu$, $\nu^{\sigma}$, gluon) are either self-conjugate or distinguished only by orientation.

**Step 3: chirality, the electron, and the positron.**
The trefoil $3_1 = T_{2,3}$ has crossing number $3$. Its braid word $\sigma_1 \sigma_2 \sigma_1 \in B_3$ requires three $R$-matrix evaluations. It cannot exist before the cubic jet.

Step 3 introduces chirality. The trefoil is not amphichiral: the left trefoil $T_{2,3}$ and the right trefoil $T_{2,3}^{\sigma}$ are distinct knots ([chirality: electron and positron](#rem:chirality-trefoil-electron-positron)). The mirror operation $\sigma$ (reversing all crossings) produces a genuinely different topological object. This originates the particle-antiparticle distinction for chiral matter:

- **Electron** $e^- = T_{2,3}$ (left trefoil, solid ●)
- **Positron** $e^+ = T_{2,3}^{\sigma}$ (right trefoil, outlined ○)

Both have crossing number $3$ and appear at the same Planck step. The trefoil and its mirror are the two monodromy generators of the chiral cubic. They arise together as the two orientations of the holonomy around the branch points. The electron cannot exist without the positron: the cubic jet produces both chiralities simultaneously.

The same step produces the **up quark** ($u = T_{2,3}$) and **down quark** ($d = T_{2,3}^{\sigma}$) as the same trefoil pair in the color-tube sector. With quarks available, the first composite hadrons become constructible, though their linking structure requires step 4.

**Step 4: the Higgs mass mechanism and the first hadrons.**
The figure-eight knot $4_1$ has crossing number $4$ and is the first hyperbolic knot: $\mathrm{Vol}(4_1) = 2.0299$. It is amphichiral ($4_1 \cong 4_1^{\sigma}$), so the Higgs field $H$ is its own antiparticle. It resembles the neutrino but possesses non-trivial topology. The Hodge decomposition ([cohomological embedding](#prop:cohomological-embedding)) places $4_1$ in $H^{0,1}$ as the mass mechanism. Its hyperbolic volume drives the mass formula $m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^2$.

The **Borromean baryon** $\mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ also emerges at step 4. Although each constituent quark ($T_{2,3}$ or $T_{2,3}^{\sigma}$) has crossing number $3$, the three-component Borromean linking requires the quartic jet to resolve the inter-component holonomy. The proton $p$, neutron $n$, and their antiparticles $p^{\sigma}$ and $n^{\sigma}$ first appear here.

**Step 5: the muon and heavy quarks.**
The cinquefoil $5_1 = T_{2,5}$ has crossing number $5$ and genus $2$. It is chiral ($5_1 \neq 5_1^{\sigma}$), producing:

- **Muon** $\mu^- = T_{2,5}$ and **antimuon** $\mu^+ = T_{2,5}^{\sigma}$
- **Charm quark** $c = T_{2,5}$ and **strange quark** $s = T_{2,5}^{\sigma}$

The charm and strange quarks are the mirror pair at genus 2, just as the up and down quarks are the mirror pair at genus 1. The muon and antimuon share the same torus knot type but are distinguished by chirality. They are distinct knot types, consistent with their distinct charges.

**Summary: the unfolding.**
See [Table 2](#tbl:jet-planck-steps-table2-data).

Each row is one Planck step. The universe unfolds through successive jet approximations rather than springing into existence fully formed. The photon is pre-geometric (step 0). The neutrino and antineutrino are the first topological excitations (step 1), but they are amphichiral. Binding appears at step 2. True chirality, and the matter particle-antiparticle distinction, requires three steps. At step 3, the cubic jet produces the trefoil and its mirror simultaneously: the electron and positron, the up and down quarks, the golden ratio, and the braid group $B_3$ all emerge in a single Planck step.

**Crossing number as computational complexity.**
The crossing number $c(K)$ is the minimum number of $R$-matrix evaluations needed to compute a knot's Jones polynomial. In the jet-Planck correspondence, this is the computational cost in Planck steps. A universe at step $n$ can resolve knots with $c \leq n$ but not those with $c > n$. The particle spectrum is revealed incrementally. Heavier and more complex particles appear at later steps because the Taylor approximation of $E$ does not yet have enough polynomial degree to encode their topology.
