<!-- FILE_START: q-gl-classical-limit-intro.md -->
We verify that the $q \to 1$ degeneration recovers familiar geometry and provides a clear physical structure. Specialising at $q = 1$ recovers the classical Geometric Langlands equivalence of Beilinson–Drinfeld, tracing the degeneration of $q$-opers and $q$-Hecke eigensheaves to their classical counterparts. The perpetual obstruction refines this picture: the obstruction classes $\kappa_n$ vanish identically at $q = 1$ but persist on the full non-torsion locus. This forces the correspondence to remain intrinsically $q$-deformed away from the classical fibre. The equivalence acts physically as the observability condition supplied by the fibre functor $\tau$.
<!-- FILE_END: q-gl-classical-limit-intro.md -->

<!-- FILE_START: q-gl-classical-limit.md -->
As $q \to 1$, the $q$-Geometric Langlands correspondence recovers the classical Geometric Langlands equivalence:

$$
  \lim_{q \to 1} \mathbb{L}_q =  \mathbb{L}_{\mathrm{BD}}
  \colon \mathcal{D}\text{-}\mathrm{mod}(\mathrm{Bun}_G(X))
  \xrightarrow{ \sim }
  \mathrm{QCoh}(\mathrm{LocSys}_{\check{G}}(X)).
$$

We factor this degeneration into three limits:

1. **Differential limit**: $d_q \to d$ and $d_q^2 \to 0$ ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)). Quantum flat connections become classical flat connections. Quantum local systems become classical local systems.
2. **Hecke limit**: The Hecke relation $(T-q)(T+q^{-1}) = 0$ degenerates to $(T-1)(T+1) = 0$. This recovers the symmetric group action. Quantum Hecke operators become classical Hecke correspondences.
3. **Dual group limit**: $\check{G}_q = G_{q^{-1}}^\vee \to G^\vee = \check{G}$ as the quantum deformation vanishes.
<!-- FILE_END: q-gl-classical-limit.md -->

<!-- FILE_START: q-gl-obstruction-classical-compatibility.md -->
The perpetual obstruction ([obstruction calculation](#prop:q-gl-obstruction-calc)) and the classical limit ([classical recovery](#conj:q-gl-classical-limit)) coexist compatibly, rendering the $q$-Geometric Langlands correspondence a singular deformation of the classical theory.

The point $q = 1$ is the universal torsion point. It belongs to $\mu_n$ for every $n \geq 1$. At $q = 1$, the $q$-exterior derivative reduces to $d$, the obstruction $d_q^2$ vanishes, and the $q$-curvature $\mathcal{F}_q = 0$. Classical flatness $\nabla^2 = 0$ holds, as does the Beilinson--Drinfeld equivalence $\mathbb{L}_{\mathrm{BD}}$. However, $q = 1$ lies in $\mu_\infty$, outside the non-torsion locus $\mathbb{G}_m^{\mathrm{nt}}$ where $\mathbb{L}_q$ is well-defined. The classical correspondence is the degenerate fibre of the $\mathbb{G}_m$-family, not a generic point.

Let $q \in \mathbb{G}_m^{\mathrm{nt}}$ and $\chi(A) \neq 0$. The obstruction class $\kappa_0$ is non-trivial at density-$1$ Kummer levels. Thus, $q$-flatness is strictly stronger than classical flatness. The moduli $\mathrm{LocSys}_{\check{G}_q}(X)$ is a proper subspace of the classical prediction. We resolve this through three observations:

1. The classical limit $q \to 1$ approaches a boundary point of the parameter space $\mathbb{G}_m^{\mathrm{nt}}$. The point $q = 1$ lies in the closure of the open complement of $\mu_\infty$.
2. As $q \to 1$, the $(q-1)$-factor in the $q$-flatness equation $\nabla_q^2 = (q-1)\mathcal{F}_q$ forces $\nabla_q^2 \to 0$, even though $\mathcal{F}_q$ remains non-zero. The vanishing prefactor screens the curvature.
3. The Kummer constraint (property (4) of the [$q$-GL conjecture](#conj:q-geometric-langlands)) encodes this singular behaviour. The equivalence degenerates precisely at roots of unity. The classical limit is the universal degeneration.

We recover the classical theory not by continuity, but by specialisation to a singular point.
<!-- FILE_END: q-gl-obstruction-classical-compatibility.md -->

<!-- FILE_START: q-gl-physical-interpretation.md -->
We interpret the $q$-Geometric Langlands correspondence physically within the QOU framework.

The category $\mathcal{D}_q\text{-}\mathrm{mod}(\mathrm{Bun}_{G_q})$ encodes $q$-deformed gauge theory on the brane. We interpret $G_q$-bundles as field configurations, $q$-$\mathcal{D}$-modules as quantum states, and $q$-Hecke operators as particle insertions that modify the gauge field at a point. The $q$-curvature $\mathcal{F}_q$ is the field strength. The $d_q^2 \neq 0$ obstruction forces this curvature to be non-zero.

The category $\mathrm{QCoh}(\mathrm{LocSys}_{\check{G}_q})$ encodes the $q$-deformed matter sector. The $\check{G}_q$-local systems carry parallel transport data for matter fields. The Langlands dual $\check{G}_q$ controls the allowed representations. The Kummer filtration on $\mathrm{LocSys}_{\check{G}_q}$ stratifies the matter sector by the divisibility of the obstruction class $\kappa_0$.

The functor $\mathbb{L}_q$ asserts categorically that the gauge and matter sectors carry equivalent information. This duality arises because a single substrate parameter $q$ controls both the braiding and the differential calculus. A $q$-Hecke eigensheaf is a quantum state that responds to gauge field modifications by scalar multiplication by a $q$-local system. It represents a particle carrying a definite charge under $\check{G}_q$.
<!-- FILE_END: q-gl-physical-interpretation.md -->

<!-- FILE_START: q-gl-automorphic-observability.md -->
The [fibre-functor mediation conjecture](#conj:q-gl-fiber-functor) connects the $q$-Geometric Langlands correspondence to the observability axiom of the QOU ([quantum observable universe](#def:quantum-observable-universe)).

The observability condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ constrains the adjoint representation and thereby the fibre functor $\tau$. Because $\tau$ uniquely determines $\mathbb{L}_q$, the automorphic--spectral duality follows from observability. Relaxing observability reintroduces adjoint cohomology. The obstruction classes $\kappa_n$ interact with this cohomology to produce additional obstructions to the equivalence ([fibre-functor rigidity](#rem:fibre-functor-rigidity)).

The rigidity of $\tau$ guarantees that the Langlands equivalence is unique. The Kummer filtration on $\kappa_0$ ([Kummer filtration](#rem:kummer-filtration-obstruction)) determines the arithmetic locus where $\mathbb{L}_q$ is well-defined.

The passage from $\mathbb{L}_{\mathrm{BD}}$ to $\mathbb{L}_q$ is controlled by $(q-1)$, which acts as $\hbar_q$ ([q-Planck constant](#def:quantum-planck-constant)). The $q$-Geometric Langlands correspondence represents the fully quantum-corrected gauge/matter duality. We recover the classical Langlands programme in the semiclassical limit $\hbar_q \to 0$. The perpetual obstruction ensures this quantum correction cannot be trivialised at cofinitely many Kummer levels.
<!-- FILE_END: q-gl-automorphic-observability.md -->
