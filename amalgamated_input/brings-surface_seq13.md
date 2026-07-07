<!-- FILE_START: descartes-theorem-intro.md -->
The atomic and nuclear spectra of the previous sections
are all consequences of one structural choice: $\chi(A) = -6$. The
Descartes theorem turns that observation into a uniqueness statement.
Theorem: Descartes theorem is the load-bearing claim of the
section: among quantum observable universes satisfying the Descartes
condition, Bring's surface is the terminal object. Example: Constructive terminal morphism to Bring's QOU exhibits the explicit
morphism that witnesses terminality.

Remark: Universality for a given Euler characteristic extracts the
general principle behind the theorem — the categorical Euler
characteristic selects a terminal QOU — and Example: Bring's surface and $q$-flatness obstructions records the $q$-flatness obstruction
language in which Yekutieli's theory expresses the same content.
Remark: Observations on the Bring's surface gathers the
observational consequences that the next section, topological mass
and the knot-particle spectrum, will use when it computes physical
masses from the knot generators selected by this terminality.

_(draft.)_
<!-- FILE_END: descartes-theorem-intro.md -->

<!-- FILE_START: descartes.md -->
Let $\mathbf{C}_{-6}$ denote the category of quantum observable universes
over $R$ satisfying the Descartes condition $\chi(A) = -6$
([Descartes condition](#def:archimedean-condition)), with morphisms given by QOU maps
that preserve the Euler characteristic.  Then Bring's surface $\Sigma_4$
([Bring's surface](#def:brings-surface),
[Bring's surface is QOU](#prop:brings-is-qou)) is a terminal object in
$\mathbf{C}_{-6}$: for every Descartes universe
$(\mathbf{C}, A, \tau)$ in $\mathbf{C}_{-6}$, there exists a unique
morphism to the Bring's QOU.

<!-- FILE_END: descartes.md -->

<!-- FILE_START: terminal-morphism-brings.md -->
The [Descartes theorem](#thm:descartes) asserts that for every
Descartes universe $(\mathbf{C}, A, \tau)$ in $\mathbf{C}_{-6}$,
there exists a *unique* morphism to the
[Bring's QOU](#prop:brings-is-qou). We construct this morphism
step by step.

**Setup.** Let $(\mathbf{C}, A, \tau)$ be any QOU with
$\chi(A) = -6$ and $(\mathbf{C}_B, A_B, \tau_B)$ be Bring's QOU
with $A_B = \mathcal{O}_q(\mathrm{SU}(2))$,
$\mathbf{C}_B = \mathrm{Rep}(\mathrm{SU}_q(2))$, and $\tau_B$ the
forgetful functor.

**Step 1: match the substrate parameters.** Both source and target
have $\chi(A) = -6$, so the Descartes condition determines
$q + q^{-1} = -6$ in both. By the
[constructive extraction](#ex:substrate-parameter-brings), both
algebras are defined over
$\mathbb{Z}[q, q^{-1}]/(q^2 + 6q + 1)$. The specialisation maps
$\iota, \iota_B \colon \mathbb{Z}[q, q^{-1}] \to k$ agree, giving an
isomorphism of base rings. Define $\phi_0 \colon k \to k$ as the
identity.

**Step 2: construct the :refterm[monoidal functor]{#monoidal-functor}.** The fibre functor
$\tau \colon \mathbf{C} \to \mathrm{Vect}_k$ is exact, faithful,
and monoidal. By Tannaka–Krein reconstruction
([constructive reconstruction](#ex:tannaka-krein-su2)), the
source algebra $A$ is recovered as
$\mathrm{coend}(\tau^\vee \otimes \tau)$. Since both $A$ and $A_B$
satisfy the same Hecke relation $(T - q)(T + q^{-1}) = 0$ with the
*same* $q$, the reconstructed Hopf algebras are isomorphic. Define:

$$
  F \colon \mathbf{C} \xrightarrow{\tau} \mathrm{Vect}_k
  \xleftarrow{\tau_B} \mathbf{C}_B.
$$

The :refterm[monoidal functor]{#monoidal-functor} $\Phi = \tau_B^{-1} \circ \tau$ (well-defined
up to natural isomorphism by Tannaka equivalence) is the desired
morphism on categories.

**Step 3: construct the algebra map.** The functor $\Phi$ induces
a Hopf algebra homomorphism $\phi \colon A \to A_B$ by applying
$\Phi$ to the regular representation. Concretely, $\phi$ maps
the generators of $A$ to those of $A_B$:

$$
  \phi(\alpha_A) = \alpha_B, \quad
  \phi(\beta_A) = \beta_B, \quad
  \phi(\bar\alpha_A) = \bar\alpha_B, \quad
  \phi(\bar\beta_A) = \bar\beta_B,
$$

where both sets of generators satisfy the same
$\mathcal{O}_q(\mathrm{SU}(2))$ relations (since $q$ is the same).
The Frobenius forms are compatible:
$\int_{A_B} \circ\, \phi = \int_A$ because both are Haar states.

**Step 4: verify uniqueness.** Suppose $\phi'$ is another such
morphism. Then $\tau_B \circ \Phi' \cong \tau_B \circ \Phi \cong \tau$
as monoidal functors. By Tannaka–Krein rigidity (the automorphism
group of $\tau_B$ is $G_q$ acting by inner automorphisms), there
exists $g \in G_q$ with $\Phi' = \mathrm{Ad}(g) \circ \Phi$. But
morphisms in $\mathbf{C}_{-6}$ must preserve the Haar state, and the
Haar state is $G_q$-invariant
([vacuum state uniqueness](#prop:vacuum-state)), so
$\int_{A_B} \circ\, \phi' = \int_{A_B} \circ\, \phi$. This forces
$\phi' = \phi$ as Frobenius-algebra homomorphisms. $\square$

**Summary.** The terminal morphism is constructed in four steps:
(1) match substrate parameters via the Descartes condition,
(2) build a :refterm[monoidal functor]{#monoidal-functor} via Tannaka–Krein,
(3) extract the Hopf algebra map on generators,
(4) verify uniqueness via Haar-state rigidity.
Every step is algorithmic — no non-constructive choices are made.
<!-- FILE_END: terminal-morphism-brings.md -->

<!-- FILE_START: universality-general.md -->
The Descartes theorem ([Descartes universe](#thm:descartes)) is expected to be a
special case of a more general result: for any admissible Euler
characteristic $\chi$, the category $\mathbf{C}_{\chi}$ of $\mathbb{C}$
quantum observable universes with $\chi(\mathcal{S}) = \chi$ should admit a terminal
object determined by the unique maximally symmetric Riemann surface of the
corresponding genus.  The Descartes case $\chi = -6$ (genus $4$) is
distinguished by Bring's curve, but analogous universal objects are expected
at other values of $\chi$.
<!-- FILE_END: universality-general.md -->

<!-- FILE_START: archimedean-yekutieli.md -->
Bring's surface satisfies [QU-to-QOU lifting](#thm:qu-to-qou) with
$\chi(A) = -6$.  The non-vanishing Yekutieli classes $\kappa_n \neq 0$
([QU-to-QOU lifting](#thm:qu-to-qou)(3)) obstruct smooth lifting at every level,
creating twisted sectors that control inertial mass
([mass geometric drag](#rem:mass-geometric-drag)) and the three lepton generations
--- corresponding to the three pairs of branch points under
$S_3 \subset S_5$ ([chirality and trefoil](#rem:chirality-trefoil)).

**Motivic-Galois reading.**  *In the realization tower of the
[motivic substrate](#def:motivic-substrate), the perpetual
non-vanishing $\kappa_n \neq 0$ at every level is the statement that
the Frobenius character of Bring's surface is non-trivial at every
finite place $p \nmid 6$ — a special case of
[motivic perpetual obstruction](#conj:motivic-perpetual-obstruction)
applied to the genus-4 substrate
([Kummer tower](#rem:kummer-tower) §motivic-Galois).
The three lepton generations then correspond to the
$\mathrm{Gal}(\mathbb{Q}(\mu_\infty)/\mathbb{Q})$-weight decomposition
under $S_3 \subset S_5$ — equivalently, the orbits of the cyclotomic
Galois group on the six branch points. The "three" of the three
generations is a Galois-theoretic statement, not an analytic count.*
<!-- FILE_END: archimedean-yekutieli.md -->

<!-- FILE_START: observation-brings.md -->
The general notion of an
([observation](#def:observation)) specialises on the Bring's surface as
follows: the observation morphism $\mathfrak{O} \colon A \to A$ acts
fibrewise on the state bundle $\mathcal{S} \to M$ and perturbs the substrate
parameter $q(p)$ ([substrate parameter](#def:substrate-parameter)), shifting
the non-commutative geometry of the quantum Bring's surface
([Section](#sec:quantum-brings)).  The two-observer parallelogram
([two-observer parallelogram](#rem:two-observer-parallelogram)) applies directly: two
independent observations of a fermion on the Bring's surface produce a
discrepancy controlled by the local Planck constant $\hbar_q(p)$.
<!-- FILE_END: observation-brings.md -->

