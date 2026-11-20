> **Superseded.** The scalar substrate density $\rho_q = 1/\hbar_q^2$ used
> below is the structurally-wrong leading-order ansatz; the operator-valued
> form supersedes it ([`mass-endomorphism-tower`](mass-endomorphism-tower.md));
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](../mass-endomorphism/rho-k-graded-expansion.md).

The **Kashaev volume conjecture (KVC)** asserts that, for every
hyperbolic knot $K \subseteq S^3$, the Kashaev limit of the colored
Jones polynomial computes the hyperbolic volume of the complement,

$$
  \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K)
  \;=\;
  2\pi \cdot \lim_{N \to \infty}
  \frac{\log \lvert J_N(K)\rvert}{N},
  \qquad
  J_N(K)\big\vert_{q = \exp(2\pi i / N)},
$$

with the convention that the right-hand side vanishes when $K$ is not
hyperbolic. KVC was conjectured by Kashaev [`kashaev1997`] and reformulated
in terms of the colored Jones polynomial by Murakami–Murakami
[`murakami-murakami2001`]. It is **open in general** (proved only for
specific families: the figure-eight knot, certain torus and pretzel
knots, etc.).

Inside QOU, KVC is the consistency statement that the archimedean
realisation functor $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
([archimedean realization functor](#def:archimedean-realization-functor))
applied to the algebraic quantum volume
([algebraic quantum volume](#def:algebraic-quantum-volume))
recovers the hyperbolic volume; this is the content of the per-block
[Kashaev as archimedean realization](#rem:kashaev-as-archimedean-realization)
remark.

### Status of the conjecture in the argument

The volume conjecture is carried as a hypothesis: for each braid closure, the hyperbolic volume equals the Kashaev limit (the volume is also assumed non-negative). Results that depend on it assume this identification and are proved from it; the identification itself is the only unproved input, and it is not proved here.

This is the same pattern as the mass evaluation in the [mass endomorphism tower](#prop:mass-endomorphism-tower): the canonical computation is assumed, so that the algebraic tower identities can be proved from it.

### Rationale for a class rather than an axiom

Three reasons:

1. **Locality.** A typeclass instance can be supplied per knot family
   (figure-eight, torus, etc.) where KVC is actually proved; downstream
   theorems then specialise to verified ground.

2. **Compositionality.** A bridge theorem of the form
   $\Phi_q(V_S) = \rho_q \cdot \mathrm{Vol}(K_S)$ depends only on KVC
   restricted to $K_S$; the typeclass scope makes that dependency
   visible in the type signature.

3. **No global axiom pollution.** Mathlib's axiom audit
   (`#print axioms`) records typeclass dependencies but does not flag
   them as global axioms; the conditional nature of every downstream
   result is preserved.

The conjecture itself remains open at the level of $\pi_0$ —
no claim of proof is made by introducing the class.

### Motivic perspective

KVC is, in motivic language, a **regulator statement**: the
hyperbolic volume of $S^3 \setminus K$ is the image of a class in
the Bloch group $\mathcal{B}(\mathbb{C})$ under the Borel/Beilinson
regulator $r_\infty$, and the colored Jones polynomial at
$q = \exp(2\pi i / N)$ is the $q$-deformed avatar of that class
[`zagier1986`, `neumann-zagier1985`]. The QOU recasting frames
$\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$ as the archimedean
realisation functor on the algebraic data $\Phi_q(\lvert V_S\rvert)$
— a class in the quantum Bloch group
([quantum Bloch group](#def:quantum-bloch-group)) — landing in
$\mathbb{R}$ as the hyperbolic volume of the corresponding
Φ$_q$-piece. KVC, in this presentation, is the assertion that the
$q$-deformed regulator agrees with the classical one in the Kashaev
limit.
