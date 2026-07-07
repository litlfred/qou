<!-- FILE_START: particles-intro.md -->
The transport equation $\mathcal{D}_\nabla \psi = 0$
selects on-shell solutions, but does not yet say what a particle
is. We define a particle as a $q$-harmonic form, then read off
the fermion--boson decomposition from the weight splitting,
and finally treat observation as a structural operation that
acts on these solutions.

Definition: Categorical $q$-deformed exterior derivative extends
the substrate-deformation construction from the previous section
to all of $\Omega^\bullet(A)$, giving $d_q = q^{-1}d + (1 -
q^{-1})\pi_V \circ d$ and its dagger-adjoint $\delta_q$.
Proposition: Existence of the categorical $q$-exterior derivative
and Proposition: uniqueness of the categorical $q$-exterior derivative, with their proofs, fix $d_q$ once the QOU data is
chosen. Definition: $q$-harmonic form (particle) defines a
particle as $\alpha \in \Omega^k(A)$ in the kernel of the
$q$-Laplacian $\Delta_q = d_q \delta_q + \delta_q d_q$.
Definition: Fermion--Boson decomposition restricts the weight
decomposition to $\mathcal{H}_q^k = \ker\Delta_q$, giving the
short exact sequence $0 \to \mathcal{H}_{q,H}^k \to
\mathcal{H}_q^k \to \mathcal{H}_{q,V}^k \to 0$: a boson is
purely horizontal, a fermion has non-trivial vertical part.

Definition: Categorical point and Remark: Explication of the categorical point introduce a point of $A$ as a
morphism $p \colon \mathbf{1} \to A$, the categorical
replacement for "evaluation at a spacetime point" with no
ambient topology on $A$. Definition: Observation defines an
observation on $U$ as a pair $(\mathfrak{O}, \epsilon)$ where
$\mathfrak{O}$ is a section of $\mathrm{Ad}(J^1 \mathcal{S})$
satisfying Frobenius compatibility and an adjoint backreaction
that shifts the substrate parameter via the Hopf coaction;
$\epsilon \in \{+1, -1\}$ selects the braiding orientation
under $\prec_c$. Remark: The two physical roles of an observation ($J^1$ versus $\mathrm{Ad}$) and Proposition: Observation as a backreacting Hecke generator, with its proof, expand
the structural content.

Remark: Two-observer parallelogram computes the commutator
$[\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p}](\alpha_p) =
[q_1'(p), q_2'(p)] \cdot (\alpha_V)_p$ at a point and shows that
it vanishes exactly on bosons; on fermions, the non-cocommutativity
of the Hopf structure forces independent observations to disagree.
The closing block Remark: The observer acts directly on fermions via the colour fibre reads this through the Hecke eigenspace
decomposition $V \otimes V = \mathrm{Sym}^2 \oplus \bigwedge^2$:
the $\mathrm{Ad}$ component preserves the bosonic eigenspace and
rotates the fermionic one, depositing $q + q^{-1}$ per crossing
in the colour fibre. The next section, **Geometric
interpretations**, takes the operators of this section and reads
them through the classical vector-calculus dictionary.

_(draft.)_
<!-- FILE_END: particles-intro.md -->

<!-- FILE_START: categorical-q-ext-deriv.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
connection $\nabla$ ([categorical connection](#def:categorical-connection)),
substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)),
and weight decomposition $\pi_H, \pi_V$
([weight decomposition](#def:weight-decomposition)).  The **$q$-deformed
exterior derivative** $d_q \colon \Omega^k(A) \to \Omega^{k+1}(A)$ is

$$
  d_q =  q^{-1}d + (1 - q^{-1})\pi_V \circ d,
$$

where $d \colon \Omega^k(A) \to \Omega^{k+1}(A)$ is the differential
of the non-commutative de Rham complex.  Equivalently, $d_q$ acts as
$q^{-1}d$ on horizontal forms and as $d$ on vertical forms:

```tex
\begin{equation}\label{eq:categorical-dq-cd}
\begin{tikzcd}[row sep=2.5em, column sep=2.5em]
  \Omega^k_H(A) \ar[r, "d"] \ar[d, hook]
  & \Omega^{k+1}(A) \ar[r, "q^{-1}"]
  & \Omega^{k+1}(A) \\
  \Omega^k(A) \ar[rru, "d_q"']
\end{tikzcd}
\end{equation}
```

The *$q$-adjoint* $\delta_q \colon \Omega^{k+1}(A) \to \Omega^k(A)$
is the adjoint of $d_q$ with respect to the dagger structure
([positive definite dagger](#prop:positive-definite-dagger)).
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
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
$q$-deformed exterior derivative $d_q$
([categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)).  The *$q$-Laplacian*
on $\Omega^k(A)$ is $\Delta_q = d_q\delta_q + \delta_qd_q$.
A **particle** is an element $\alpha \in \Omega^k(A)$ that is
$q$-harmonic:

```tex
\begin{equation}\label{eq:q-harmonic-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^{k-1}(A)
    \ar[r, "d_q"]
  & \Omega^k(A)
    \ar[r, "d_q"]
    \ar[d, "\delta_q"'{near start}, "{\scriptstyle \Delta_q \alpha = 0}"{description, near end}]
  & \Omega^{k+1}(A)
  \\
  & \Omega^{k-1}(A)
\end{tikzcd}
\end{equation}
```

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: q-harmonic-form.md -->

<!-- FILE_START: fermion-boson-decomposition.md -->
Let $\mathcal{H}_q^k = \ker\Delta_q \subset \Omega^k(A)$ denote the
space of particles ([$q$-harmonic form](#def:q-harmonic-form)).  The weight
decomposition ([weight decomposition](#def:weight-decomposition)) restricts to
a short exact sequence

```tex
\begin{equation}\label{eq:fermion-boson-ses}
\begin{tikzcd}[column sep=2.5em]
  0 \ar[r]
  & \mathcal{H}_{q,H}^k \ar[r, hook]
  & \mathcal{H}_q^k \ar[r, "\pi_V"]
  & \mathcal{H}_{q,V}^k \ar[r]
  & 0
\end{tikzcd}
\end{equation}
```

where $\mathcal{H}_{q,H}^k = \mathcal{H}_q^k \cap \Omega^k_H(A)$
and $\mathcal{H}_{q,V}^k = \pi_V(\mathcal{H}_q^k)$.  A **boson**
is a particle in the kernel $\mathcal{H}_{q,H}^k$ (purely horizontal:
$\alpha_V = 0$).  A **fermion** is a particle with
$\alpha_V \neq 0$, i.e. one whose image under $\pi_V$ is non-zero.

The sequence splits via $\pi_H$:

```tex
\begin{equation}\label{eq:fermion-boson-split}
\begin{tikzcd}[column sep=2.5em]
  \mathcal{H}_q^k
    \ar[r, "\pi_H \oplus \pi_V", "\sim"']
  & \mathcal{H}_{q,H}^k  \oplus  \mathcal{H}_{q,V}^k
\end{tikzcd}
\qquad
\text{(bosons $\oplus$ fermion vertical parts).}
\end{equation}
```
<!-- FILE_END: fermion-boson-decomposition.md -->

<!-- FILE_START: categorical-point.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum universe](#def:quantum-universe)).  A **categorical point**
of $A$ is a morphism

```tex
\begin{equation}\label{eq:categorical-point}
\begin{tikzcd}[column sep=3em]
  \mathbf{1} \ar[r, "p"] & A
\end{tikzcd}
\qquad\text{(categorical point)}
\end{equation}
```
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
Let $(\mathbf{C}, A, \tau)$ be a quantum observable
universe with state bundle $\mathcal{S} \to M$, let $q$
denote the
([substrate parameter](#def:substrate-parameter)), let
$p \colon \mathbf{1} \to A$ be a
([categorical point](#def:categorical-point)), and let
$U \subset M$ be an open causal neighbourhood of $p$.

An **observation** on $U$ — an **intent** — is a pair
$(\mathfrak{O}, \epsilon)$
where $\epsilon \in \{+1, -1\}$ is the **direction** and

$$
  \mathfrak{O}  \in 
  \Gamma\bigl(U, \mathrm{Ad}(J^1 \mathcal{S})\bigr)
$$

is a section of the adjoint bundle of the $1$-jet
prolongation of $\mathcal{S}$.  The sign $\epsilon$
determines the arrow of time:
$\epsilon = +1$ (braiding, $\sigma_i$, forward under
$\prec_c$) or $\epsilon = -1$ (unbraiding,
$\sigma_i^{-1}$, backward).

The section $\mathfrak{O}$ satisfies:

1. **Frobenius compatibility.** The observation preserves
   the Frobenius form on $U$:

   ```tex
   \begin{equation}\label{eq:observation-frobenius}
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     A / \mathfrak{m}_p^2 \ar[r, "\mathfrak{O}_p"] \ar[dr, "\int_{A,p}"']
     & A / \mathfrak{m}_p^2 \ar[d, "\int_{A,p}"] \\
     & \mathbf{1}
   \end{tikzcd}
   \end{equation}
   ```

   at every $p \in U$, where $\int_{A,p}$ is the germ of
   the Frobenius form.  Measurement is consistent: the trace
   is preserved.

2. **Adjoint backreaction.** The observation acts on the
   colour fibre via the adjoint representation of $G$.  At
   each point $p$, the section $\mathfrak{O}_p$ conjugates by
   $G$: it rotates the colour degrees of freedom, shifting
   the substrate parameter $q \mapsto q' = q + \delta q$
   via the Hopf coaction:

   ```tex
   \begin{equation}\label{eq:observation-substrate}
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     A \ar[r, "\Delta"] \ar[d, "\mathfrak{O}_p"']
     & A \otimes A \ar[r, "\mathfrak{O}_p \otimes S"]
     & A \otimes A \ar[d, "\mu"] \\
     A \ar[rr, "\int_A"']
     & & \mathbf{1}
   \end{tikzcd}
   \end{equation}
   ```

   with $\delta q(p) = \int_A(\mathfrak{O}_p(a_{(1)})S(a_{(2)}))$.
   Observing the universe changes it: the act of reading the
   field feeds back through the colour fibre into the Reeb
   flow.

An intent at a **point** is the restriction
$\mathfrak{O}_p = \mathfrak{O}|_p$, recovering the germ-level
endomorphism $\mathfrak{O}_p \colon A / \mathfrak{m}_p^2 \to A / \mathfrak{m}_p^2$.  The sign $\epsilon$ determines
whether the crossing injected at $p$ is $\sigma_i$ (forward,
$\epsilon = +1$) or $\sigma_i^{-1}$ (backward,
$\epsilon = -1$) in the braiding-induced ordering $\prec_c$.
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
**Proposition.**
*Let $\mathfrak{O}\in \Gamma(U, \mathrm{Ad}(J^1 \mathcal{S}))$
be an observation ([observation](#def:observation)) with
substrate perturbation $\delta q$.  Then:*

1. **(Quantum energy increases.)** *The quantum Planck constant
   $\hbar_q = 1 - q^{-1}$
   ([quantum Planck constant](#def:quantum-planck-constant))
   satisfies*

   $$
     \hbar_{q + \delta q} - \hbar_q
     =  \frac{\delta q}{q(q + \delta q)}
      >  0
   $$

   *for $\delta q > 0$.  Every observation with positive
   substrate perturbation strictly increases the quantum
   energy of the system.*

2. **(Action deformation.)** *The categorical action
   $\mathfrak{S}_q[\nabla, \lambda, \psi]$
   ([categorical action](#def:categorical-action)) evaluated
   at the perturbed parameter $q' = q + \delta q$ satisfies*

   $$
     \mathfrak{S}_{q'}
     = 
     \mathfrak{S}_q +  \delta q \cdot \frac{\partial \mathfrak{S}_q}{\partial q}
     +  O((\delta q)^2)
   $$

   *The first-order shift $\partial \mathfrak{S}_q / \partial q$ is the
   **observation cost**: the rate at which the action changes
   per unit of substrate perturbation.*

3. **(Classical energy is unconstrained in sign.)** *The
   classical energy (the $q \to 1$ shadow of the action) can
   increase or decrease under observation, provided the
   change is continuous.  Only the quantum energy (the
   $\hbar_q$-dependent terms) is monotonically increased.*
<!-- FILE_END: observation-energy.md -->

<!-- FILE_START: two-observer-parallelogram.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$, and let
$p \colon \mathbf{1} \to A$ be a
([categorical point](#def:categorical-point)).  Let
$\alpha$ be a ([fermion](#def:fermion-boson-decomposition)) with germ
$\alpha_p \in A / \mathfrak{m}_p^2$.
Consider two independent observations at $p$,
$\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p} \colon A / \mathfrak{m}_p^2 \to A / \mathfrak{m}_p^2$
([observation](#def:observation)).  These data
assemble into a *parallelogram of observations at $p$*:

```tex
\begin{equation}\label{eq:observation-parallelogram}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  & \mathfrak{O}_{1,p}(\alpha_p) \arrow[dr, "\text{compare}"] & \\
  \alpha_p \arrow[ur, "\mathfrak{O}_{1,p}"]
           \arrow[dr, "\mathfrak{O}_{2,p}"']
  & & \delta\alpha_p \\
  & \mathfrak{O}_{2,p}(\alpha_p) \arrow[ur, "\text{compare}"'] &
\end{tikzcd}
\end{equation}
```

The discrepancy is the *commutator of observations at $p$*:

$$
  [\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p}](\alpha_p)
  = 
  \mathfrak{O}_{1,p}(\mathfrak{O}_{2,p}(\alpha_p))
  - \mathfrak{O}_{2,p}(\mathfrak{O}_{1,p}(\alpha_p)).
$$

Each observation perturbs the substrate parameter at $p$ by
$\delta q_i(p)$ ([observation](#def:observation), condition (2)),
inducing shifted parameters $q_1'(p) = q(p) + \delta q_1(p)$
and $q_2'(p) = q(p) + \delta q_2(p)$.  The commutator
$[q_1'(p), q_2'(p)]$ measures the obstruction:

$$
  [\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p}](\alpha_p)
  = 
  [q_1'(p), q_2'(p)] \cdot (\alpha_V)_p.
$$

This vanishes if and only if $[q_1'(p), q_2'(p)] = 0$ (the shifted
parameters commute at $p$) or $(\alpha_V)_p = 0$ (the particle is a
boson at $p$).  Generically, the non-cocommutativity of the Hopf
structure ensures $[q_1'(p), q_2'(p)] \neq 0$: independent
observations of a fermion at the same point necessarily disagree.

**Germs rather than global morphisms.**
The categorical algebra $A$ carries no intrinsic topology (it is an
object in $\mathbf{C}$, not a topological ring).  Working with germs
$A / \mathfrak{m}_p^2$ at a point $p$ plays the role of localisation:
it captures the first-order jet of the observation without requiring a
topology on $A$.  In the archimedean realisation
([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)), where
$A = C^{\infty}(M)$, germs at $p$ recover the usual smooth germs
$C^{\infty}_p(M) / \mathfrak{m}_p^2$.
<!-- FILE_END: two-observer-parallelogram.md -->

<!-- FILE_START: germ-commutator-q-curvature.md -->
**Proposition (Germ-commutator equals the $q$-curvature).**
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
**Conjecture (q-harmonic-map heat flow for the substrate field).**
*The substrate parameter $q(p)$, promoted from a fixed modulus to a
field over the base, evolves in time by the **$q$-harmonic-map heat
flow**:*

$$
  \partial_t\, q \;=\; -\,\Delta_q\, q,
  \qquad
  \Delta_q \;=\; q^{-2}\Delta \;+\; q^{-1}(1-q^{-1})\,\mathfrak{C}
            \;+\; (1-q^{-1})^2\,\Delta_\xi ,
$$

*where $\Delta$ is the base Laplacian, $\mathfrak{C}$ the first-order
Casimir/drift term, and $\Delta_\xi$ the Reeb-fibre Laplacian. Its
stationary configurations $\Delta_q q = 0$ are the **$q$-harmonic
sections**; the vacuum constant $q \equiv q_0$ is the trivial one.*

This is the *dynamical* half of the local-$q$ programme. Route 2a
([germ-commutator $=$ $q$-curvature](#prop:germ-commutator-q-curvature))
supplies the *kinematic* half: the germ $\delta q(p)$ of two
disagreeing observations is the $q$-curvature on the loop they trace.
What 2a leaves open is *time evolution* of $q(p)$ — and that is what
this conjecture postulates.

> **Ansatz, not theorem.** The operator $\Delta_q$ is read off from the
> $q$-heat equation
> ([$q$-Gaussian solves the $q$-heat equation](#prop:q-gaussian-solves-q-heat)),
> whose fundamental solution is the Reeb-invariant $q$-Gaussian with the
> clock running at rate $q^{-2}$. But that proposition governs diffusion
> of a *scalar density at fixed $q$*. Making $q(p)$ **itself** the
> diffusing field is a **new postulate** — the specific PDE above is an
> ansatz, not derived from existing blocks. What is solid is the germ
> $\delta q(p)$ (Route 2a, verified) and its identification with the
> $q$-curvature; the evolution law is conjectural.

The fixed-point equation $\Delta_q q = 0$ is the hand-off to the
$q_0$-selection question (Route 1): the vacuum $q \equiv q_0$ is the
trivial $q$-harmonic section, and a *non-trivial* stationary point
balancing the intrinsic curvature $(q-1)\mathcal{F}_q^{\mathrm{intr}}$
against a Reeb-fibre source would be a candidate selection condition for
$q_0$ — but the naive "$q_0$ is the only fixed point" reading is false
(every constant field is stationary), so selection needs an extra
equation. That remains open and is **not** wired to production.

## Lean

The flow is axiomatised as a class
`QOU.LocalQ.QHarmonicFlow` over an additive group $V$ of field
configurations: a configuration `q`, its time-derivative `dq` $= \partial_t q$,
the $q$-Laplacian `Δq`, and the ansatz law `dq = -Δq q`. The *existence*
of such a structure for the physical substrate field is the conjecture.
Conditional on the class, two structural consequences are
**verified, sorry-free**:

1. `stationary_iff_qharmonic` — the flow is stationary ($\partial_t q = 0$)
   iff the configuration is $q$-harmonic ($\Delta_q q = 0$);
2. `vacuum_stationary` — the trivial (zero/constant) field is stationary,
   i.e. the vacuum is a $q$-harmonic fixed point.

The conjectural content is isolated in the class instance (the ansatz
PDE); the consequences hold for *any* flow of this shape.
<!-- FILE_END: q-harmonic-flow.md -->

<!-- FILE_START: observation-fermion-action.md -->
The $\mathrm{Ad}$ component of an observation
([observation](#def:observation)) acts directly on
fermions.  The mechanism is the eigenspace decomposition
of the Hecke generator $\sigma$:

$$
  V \otimes V
  = 
  \underbrace{\mathrm{Sym}^2(V)}_{\text{bosonic, eigenvalue } q}
   \oplus 
  \underbrace{\textstyle\bigwedge^2(V)}_{\text{fermionic, eigenvalue } {-q^{-1}}}
$$

The two idempotents are:

$$
  e_+ = \frac{\sigma + q^{-1}}{q + q^{-1}}, \qquad
  e_- = \frac{q - \sigma}{q + q^{-1}}
$$

with $e_+$ projecting onto $\mathrm{Sym}^2$ (bosonic) and
$e_-$ onto $\bigwedge^2$ (fermionic).

**Action of observation on each sector.**

- **On bosons** ($\mathrm{Sym}^2$): the observation preserves
  the eigenspace.  The $\mathrm{Ad}$ action commutes with
  $e_+$: symmetric states remain symmetric.  The commutator
  of two observations vanishes on bosons
  ([two-observer parallelogram](#rem:two-observer-parallelogram)):
  $[I_1, I_2](\alpha_p) = 0$ when
  $\alpha$ is a boson.  Bosons can be observed without
  interference.

- **On fermions** ($\bigwedge^2$): the observation rotates
  the state within the colour fibre.  The $\mathrm{Ad}$
  action conjugates the antisymmetric component by $G$,
  which generically does **not** preserve $\bigwedge^2$ —
  it mixes the fermionic state with the bosonic eigenspace.
  This is the projection $e_+$: the observation partially
  converts fermionic content to bosonic content, depositing
  $q + q^{-1}$ per crossing in the colour fibre
  ([observation energy](#prop:observation-energy)).

  The commutator is non-zero on fermions:
  $[I_1, I_2](\alpha_p) \neq 0$.  Two
  observers acting on the same fermion interfere because
  each observation rotates the $\bigwedge^2$ component in a
  different direction in the colour fibre, and these
  rotations do not commute (the Hopf structure is
  non-cocommutative on $\bigwedge^2$).

**The physical picture.**

An observation reads the field through the $J^1$ (jet)
component — this is passive and commutative.  But to extract
information from a fermion, the observation must also act
through the $\mathrm{Ad}$ component — rotating the colour
fibre.  This rotation is the backreaction: it changes the
fermion's state in the process of measuring it.

The uncertainty is not epistemic (we lack information) but
geometric: the $\mathrm{Ad}$ action on $\bigwedge^2(V)$ is
a non-commutative rotation in the colour fibre.  Two
observations compose as group elements in $G$, and
$G = \mathrm{SU}_2(R)$ is non-abelian.  The order of
observation matters because rotations in three dimensions
do not commute.

This is why uncertainty is kept in the Reeb bundle --- the
$U(1)$ fibration $S^3 \to \mathcal{S}_p \cong S^2$ over the exceptional
divisor.  The Reeb vector field generates the $U_1(R) \subset G$
that commutes with everything --- it is the **one direction** in
the colour fibre where observations do commute.  The
remaining two directions (the off-diagonal generators of
$\mathfrak{su}(2)$) are where fermionic uncertainty lives.
<!-- FILE_END: observation-fermion-action.md -->

