<!-- FILE_START: particles-intro.md -->
The transport equation $\mathcal{D}_\nabla \psi = 0$ selects on-shell solutions, but requires a formal definition of a particle. We define a particle as a $q$-harmonic form, read off the fermion--boson decomposition from the weight splitting, and treat observation as a structural operation acting on these solutions.
<!-- FILE_END: particles-intro.md -->

<!-- FILE_START: categorical-q-ext-deriv.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. The **$q$-deformed exterior derivative** $d_q \colon \Omega^k(A) \to \Omega^{k+1}(A)$ is

$$
  d_q =  q^{-1}d + (1 - q^{-1})\pi_V \circ d,
$$

where $d \colon \Omega^k(A) \to \Omega^{k+1}(A)$ is the differential of the non-commutative de Rham complex. The operator $d_q$ acts as $q^{-1}d$ on horizontal forms and as $d$ on vertical forms. The *$q$-adjoint* $\delta_q \colon \Omega^{k+1}(A) \to \Omega^k(A)$ is the formal adjoint of $d_q$ with respect to the dagger structure. These operators exist and are unique.
<!-- FILE_END: categorical-q-ext-deriv.md -->

<!-- FILE_START: categorical-q-ext-deriv-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[quantum observable universe](#def:quantum-observable-universe) with
connection $\nabla$, substrate parameter $q$, and weight
decomposition $(\pi_H, \pi_V)$.  Then the
[$q$-deformed exterior derivative](#def:categorical-q-ext-deriv)

$$
  d_q \;=\; q^{-1} d + (1 - q^{-1})  \pi_V \circ d
  \;\colon\; \Omega^k(A) \to \Omega^{k+1}(A)
$$

exists as a morphism in $\mathbf{C}$ for every $k$.

Uniqueness is
([uniqueness of categorical $q$-exterior derivative](#prop:categorical-q-ext-deriv-unique)).


**Strategy.** We constructively build $d_q$ by taking a scalar-weighted linear combination of the standard categorical de Rham differential $d$ and its vertical projection $\pi_V \circ d$. Substrate parameters supply the necessary weights in the $R$-linear category.
<!-- FILE_END: categorical-q-ext-deriv-exists.md -->

<!-- FILE_START: categorical-q-ext-deriv-unique.md -->
Given fixed $d$, $\pi_V$, and $q$, the
[categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)

$$
  d_q \;=\; q^{-1} d + (1 - q^{-1})  \pi_V \circ d
$$

is the unique morphism satisfying:

1. $d_q = q^{-1} d$ on horizontal forms $\pi_H(\Omega^k(A))$;
2. $d_q = d$ on vertical forms $\pi_V(\Omega^k(A))$;
3. $d_q$ is $R$-linear in the components.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: categorical-q-ext-deriv-unique.md -->

<!-- FILE_START: q-harmonic-form.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $q$-deformed exterior derivative $d_q$. The *$q$-Laplacian* on $\Omega^k(A)$ is $\Delta_q = d_q\delta_q + \delta_qd_q$. A **particle** is an element $\alpha \in \Omega^k(A)$ that is $q$-harmonic: $\Delta_q \alpha = 0$.
<!-- FILE_END: q-harmonic-form.md -->

<!-- FILE_START: fermion-boson-decomposition.md -->
Let $\mathcal{H}_q^k = \ker\Delta_q \subset \Omega^k(A)$ denote the space of particles. The weight decomposition restricts to a short exact sequence

$$
  0 \to \mathcal{H}_{q,H}^k \to \mathcal{H}_q^k \xrightarrow{\pi_V} \mathcal{H}_{q,V}^k \to 0,
$$

where $\mathcal{H}_{q,H}^k = \mathcal{H}_q^k \cap \Omega^k_H(A)$ and $\mathcal{H}_{q,V}^k = \pi_V(\mathcal{H}_q^k)$. A **boson** is a particle in the kernel $\mathcal{H}_{q,H}^k$ (purely horizontal: $\alpha_V = 0$). A **fermion** is a particle with $\alpha_V \neq 0$. The sequence splits via $\pi_H$, giving $\mathcal{H}_q^k \cong \mathcal{H}_{q,H}^k \oplus \mathcal{H}_{q,V}^k$.
<!-- FILE_END: fermion-boson-decomposition.md -->

<!-- FILE_START: categorical-point.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum universe. A **categorical point** of $A$ is a morphism $p \colon \mathbf{1} \to A$. In the archimedean realisation $A = C^\infty(M)$, a categorical point corresponds to evaluation at $p \in M$. The augmentation ideal at $p$ is $\mathfrak{m}_p = \ker(p^* \colon A \to \mathbf{1})$, and the germ of $A$ at $p$ is the quotient $A / \mathfrak{m}_p^2$.
<!-- FILE_END: categorical-point.md -->

<!-- FILE_START: categorical-point-explication.md -->
In the archimedean realisation $A = \mathcal{O}(G)$, a categorical point
$p \colon \mathbf{1} \to A$ is a character $\mathrm{ev}_g \colon f \mapsto f(g)$
for some $g \in G$; equivalently, a point of the group $G$.  For a
manifold $M$ with $A = C^{\infty}(M)$, a point $p$ corresponds to
evaluation at $p \in M$:

```tex
\begin{equation}\label{eq:point-diagram}
\begin{tikzcd}[column sep=2.5em]
  \{*\} \ar[r, "p"]
  & M
\end{tikzcd}
\qquad\longleftrightarrow\qquad
\begin{tikzcd}[column sep=2.5em]
  \mathbf{1} \ar[r, "p"]
  & A
\end{tikzcd}
\end{equation}
```

The *augmentation ideal* at $p$ is
$\mathfrak{m}_p = \ker(p^* \colon A \to \mathbf{1})$, where
$p^* = \int_A \circ \mu(p \otimes -)$.  The *germ* of $A$
at $p$ is the quotient $A / \mathfrak{m}_p^2$, which captures the
first-order behaviour of $A$ near $p$.
<!-- FILE_END: categorical-point-explication.md -->

<!-- FILE_START: observation.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with state bundle $\mathcal{S} \to M$. Let $p \colon \mathbf{1} \to A$ be a categorical point, and let $U \subset M$ be an open causal neighbourhood of $p$. An **observation** on $U$ is a pair $(\mathfrak{O}, \epsilon)$ where $\epsilon \in \{+1, -1\}$ is the direction and $\mathfrak{O} \in \Gamma\bigl(U, \mathrm{Ad}(J^1 \mathcal{S})\bigr)$ is a section of the adjoint bundle of the $1$-jet prolongation of $\mathcal{S}$.

The section $\mathfrak{O}$ satisfies:
1. **Frobenius compatibility:** The observation preserves the Frobenius form on $U$. The trace is preserved.
2. **Adjoint backreaction:** The observation acts on the colour fibre via the adjoint representation of $G$. The section $\mathfrak{O}_p$ rotates the colour degrees of freedom, shifting the substrate parameter $q \mapsto q' = q + \delta q$ via the Hopf coaction $\delta q(p) = \int_A(\mathfrak{O}_p(a_{(1)})S(a_{(2)}))$.

The sign $\epsilon$ determines whether the crossing injected at $p$ is $\sigma_i$ (forward, $+1$) or $\sigma_i^{-1}$ (backward, $-1$). The $J^1$ (jet) component receives information, reading the field and its first derivative. The $\mathrm{Ad}$ (adjoint) component sends back, rotating the gauge degrees of freedom and perturbing $q$.
<!-- FILE_END: observation.md -->

<!-- FILE_START: observation-physical-roles.md -->
The two components of an observation correspond to its two
physical roles:

- **Receiving**: the $J^1$ (jet) component reads the field
  $E$ and its first derivative --- position and linear
  approximation.  This is the inflow of information from the
  state bundle, through the affine chart
  ([fibre functor atlas](#prop:fibre-functor-atlas)) centred
  on $U$.

- **Sending back**: the $\mathrm{Ad}$ (adjoint) component
  acts on the colour fibre by conjugation, rotating the
  gauge degrees of freedom.  This is the backreaction: the
  observation perturbs $q$, which shifts the Reeb flow,
  which changes what the next observation reads.
<!-- FILE_END: observation-physical-roles.md -->

<!-- FILE_START: observation-energy.md -->
Let $\mathfrak{O}$ be an observation with positive substrate perturbation $\delta q > 0$. The quantum Planck constant $\hbar_q = 1 - q^{-1}$ satisfies

$$
  \hbar_{q + \delta q} - \hbar_q =  \frac{\delta q}{q(q + \delta q)} >  0.
$$

Every observation with positive substrate perturbation strictly increases the quantum energy of the system.

The categorical action evaluated at the perturbed parameter $q' = q + \delta q$ satisfies

$$
  \mathfrak{S}_{q'} = \mathfrak{S}_q +  \delta q \cdot \frac{\partial \mathfrak{S}_q}{\partial q} + O((\delta q)^2).
$$

The first-order shift is the observation cost. The classical energy can increase or decrease under observation; only the quantum energy monotonically increases.
<!-- FILE_END: observation-energy.md -->

<!-- FILE_START: two-observer-parallelogram.md -->
Let $p \colon \mathbf{1} \to A$ be a categorical point. Consider two independent observations $\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p} \colon A / \mathfrak{m}_p^2 \to A / \mathfrak{m}_p^2$ acting on a fermion $\alpha$. The commutator is

$$
  [\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p}](\alpha_p) = [q_1'(p), q_2'(p)] \cdot (\alpha_V)_p.
$$

This vanishes if and only if the shifted parameters commute at $p$ or the particle is a boson ($(\alpha_V)_p = 0$). The non-cocommutativity of the Hopf structure ensures $[q_1'(p), q_2'(p)] \neq 0$: independent observations of a fermion at the same point necessarily disagree.

At a point $p$, the commutator of two observations equals the $q$-curvature $F_q$ of the $q$-connection evaluated on the loop spanned by the two observation directions: $[\delta q_1, \delta q_2] = F_q$. The observers agree if and only if the $q$-curvature vanishes. Swapping the observers negates the curvature.
<!-- FILE_END: two-observer-parallelogram.md -->

<!-- FILE_START: germ-commutator-q-curvature.md -->
*At a point $p$, let two independent observations
([observation](#def:observation)) perturb the substrate parameter by
germ-level increments $\delta q_1, \delta q_2$ in the germ algebra
$A/\mathfrak{m}_p^2$. Their commutator equals the $q$-curvature $F_q$
of the $q$-connection ([$q$-flat connection](#def:q-flat-connection))
evaluated on the loop spanned by the two observation directions:*

$$
  [\delta q_1,\, \delta q_2] \;=\; F_q.
$$

This is the formal core of the two-observer parallelogram
([two-observer parallelogram](#rem:two-observer-parallelogram)): the
local disagreement between two observers *is* the $q$-curvature on the
infinitesimal loop they trace. Two structural consequences follow.

1. **Agreement $\iff$ flatness.** The observers agree
   ($[\delta q_1, \delta q_2] = 0$) iff the $q$-curvature vanishes,
   $F_q = 0$ — the boson / $q$-flat case. Generically the
   non-cocommutativity of the Hopf structure forces $F_q \neq 0$, so
   independent fermionic observations at the same point necessarily
   disagree.
2. **Antisymmetry.** Swapping the two observers negates the curvature,
   $F_q \mapsto -F_q$: the curvature is a genuine $2$-form on the loop.

## Lean

The identity and both consequences are formalised over an abstract
non-commutative ring $R$ of germ-level perturbations in
`QOU.LocalQ.ObservationParallelogram` — `commutator_eq_curvature`,
`agree_iff_flat`, and `curvature_antisymm` — sorry-free. The germ
algebra's non-commutativity is exactly what makes the commutator, and
hence $F_q$, non-trivial; over a commutative ring the parallelogram
would close and $F_q$ would vanish identically.

The identity $[\delta q_1, \delta q_2] = F_q$ is unconditional
(structural); the identification of $F_q$ with the intrinsic
$q$-curvature $(q-1)\mathcal{F}_q^{\mathrm{intr}}$ of the
$q$-flat connection is the narrative bridge. Together these promote the
parallelogram's $\delta q(p)$ to the curvature of the $q$-connection —
the kinematic half of how the substrate parameter $q$ evolves locally
at a point.
<!-- FILE_END: germ-commutator-q-curvature.md -->

<!-- FILE_START: q-harmonic-flow.md -->
The substrate parameter $q(p)$ is conjectured to evolve by the **$q$-harmonic-map heat flow**:

$$
  \partial_t\, q \;=\; -\,\Delta_q\, q,
  \qquad
  \Delta_q \;=\; q^{-2}\Delta \;+\; q^{-1}(1-q^{-1})\,\mathfrak{C}
            \;+\; (1-q^{-1})^2\,\Delta_\xi ,
$$

where $\Delta$ is the base Laplacian, $\mathfrak{C}$ the first-order Casimir/drift term, and $\Delta_\xi$ the Reeb-fibre Laplacian. Its stationary configurations $\Delta_q q = 0$ are the $q$-harmonic sections; the vacuum constant $q \equiv q_0$ is the trivial one. This PDE serves as an ansatz for the dynamical evolution of the substrate parameter.
<!-- FILE_END: q-harmonic-flow.md -->

<!-- FILE_START: observation-fermion-action.md -->
The $\mathrm{Ad}$ component of an observation acts directly on fermions via the eigenspace decomposition of the Hecke generator $\sigma$:

$$
  V \otimes V = \underbrace{\mathrm{Sym}^2(V)}_{\text{bosonic, } q} \oplus \underbrace{\textstyle\bigwedge^2(V)}_{\text{fermionic, } {-q^{-1}}}
$$

On bosons ($\mathrm{Sym}^2$), the observation preserves the eigenspace. The $\mathrm{Ad}$ action commutes with the symmetric projection. The commutator of two observations vanishes on bosons. Bosons can be observed without interference.

On fermions ($\bigwedge^2$), the $\mathrm{Ad}$ action conjugates the antisymmetric component by $G$, mixing the fermionic state with the bosonic eigenspace. The observation partially converts fermionic content to bosonic content, depositing $q + q^{-1}$ per crossing in the colour fibre. Two observers acting on the same fermion interfere because their rotations in the colour fibre do not commute. The geometric non-commutativity of $G = \mathrm{SU}_2(R)$ forces this uncertainty.
<!-- FILE_END: observation-fermion-action.md -->

