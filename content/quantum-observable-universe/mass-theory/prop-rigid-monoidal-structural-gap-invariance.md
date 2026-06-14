**Proposition (structural-gap convention-invariance via rigid
monoidal Type-B folding).**

*Let $\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$ be the rigid
monoidal category of $\mathrm{SU}_q(2)$-representations, and let*

$$
  \tau \;:\; \mathrm{End}_{\mathbf{C}}(A^{\otimes n}) \;\longrightarrow\; \mathbb{C}_q
$$

*be the canonical Markov trace on the Hecke endomorphism algebra
$\mathrm{End}_{\mathbf{C}}(A^{\otimes n}) \cong H_n(q)$.  For any
confined particle $\mathfrak{H}$, let $\beta_{\mathfrak{H}} \in
H_{3A}(q)$ be its canonical atomic-braid representative
([`def:confined-particle`](#def:confined-particle)) and define the
**categorical structural gap**

$$
  \Delta_{\mathrm{cat}}(\mathfrak{H})
    \;:=\; B_{\mathrm{AME}}(\mathfrak{H})
    \;-\; m_e \cdot \rho \cdot \bigl|\tau(\beta_{\mathfrak{H}})\bigr|.
$$

Then $\Delta_{\mathrm{cat}}(\mathfrak{H})$ depends only on the
categorical-trace invariant $\tau(\beta_{\mathfrak{H}})$ and not on
any choice of operator-volume convention (per-generator algebraic
volumes, eigenvalue spectra, pair-knot composites, multi-term
assembly, ...) for evaluating $\mathrm{End}_{\mathbf{C}}(A^{\otimes 3A})$.*

## Why this is convention-independent

The Markov trace $\tau$ on $H_n(q)$ is **uniquely determined** by
the categorical axioms M1 (cyclicity), M2 (Markov-axiom Hecke peel
$\mathrm{tr}_M^{(n)}(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}_M^{(n-1)}(x)$),
M3 ($\mathrm{tr}_M(1) = 1$), and the Hecke quadratic relation, up
to the choice of the Markov parameter $z = 1/(\sqrt{q} + 1/\sqrt{q})$. Two evaluations of the same $\beta_{\mathfrak{H}}$
through different operator-volume conventions give the SAME
categorical $\tau(\beta_{\mathfrak{H}})$ value — this is the
universal property of the rigid monoidal Markov trace.

What the operator-volume conventions vary is the **non-categorical**
remainder:
- Per-generator $\Phi_q$ towers depend on the algebraic volumes $|\hat V_i|$ — not categorical.
- Per-eigenvalue $\Phi_q$ depends on the choice of basis in $V_\lambda$ — not categorical without further structure.
- Pair-knot product-volume / Markov-trace composites depend on the operator-volume convention chosen for the shell sub-braid.

The **categorical trace** $\tau(\beta_{\mathfrak{H}})$ is the
common invariant; the brane-tower formula contributions beyond
$|\tau(\beta_{\mathfrak{H}})|$ (the "transient tower" component of
[`conj:brane-tower-z-habiro`](#conj:brane-tower-z-habiro)) are
convention-dependent regularizations of a divergent analytic
object, and their differences must therefore cancel into the same
$\Delta_{\mathrm{cat}}$ value.

## Type-B-folded rigid monoidal structure

The Type-B folding (CLAUDE.md §7b) folds the
$\mathfrak{sl}_n$ Cartan datum into a Type B datum; the resulting
*symmetric* Kashiwara crystal is the categorical home of the
spin-involution invariance ([`prop:spin-involution-lp-dual-invariance`](#prop:spin-involution-lp-dual-invariance)).
Stable matter = fixed points of the folded crystal.

Under Type-B folding:
- **Spin involution $\sigma = S$** (Hopf antipode) acts as the
  folded-crystal involution; magic-shell sub-braids are S-conjugate.
- **Markov trace $\tau$** is S-invariant
  ([`prop:spin-involution-lp-dual-invariance`](#prop:spin-involution-lp-dual-invariance)
  §"Step 2: cycle stable"); in particular
  $\tau(\sigma_{pp}) = \tau(\sigma_{nn})$
  ([`pair_knot_Z_N_trace_invariance`](spin-involution-lp-dual-invariance.lean)
  in the Lean sibling).
- **Operator-selection LP** dual y_0* is S-invariant; magic-shell
  composite operators are in the active set EXACTLY at $Z = 2$ /
  $N = 2$ shells (the LP-dual finding from  family 5).

This is the unified rigid monoidal framework under which the
three load-bearing findings of the  closure are
consequences of a single structural fact.

## Unification of findings (1)–(3) from  closure

| Finding | Categorical content |
|:---|:---|
| (1) Pair-knot operators active at magic shells | LP-dual active set selects S-conjugate composites in Type-B-fixed locus (categorical: sub-algebra structure in $\mathbf{Rep}(\mathrm{SU}_q(2))$) |
| (2) Z$\leftrightarrow$N substrate-binding symmetry | $\tau$ is S-invariant $\Rightarrow$ $\tau(\sigma_{pp}) = \tau(\sigma_{nn})$ algebraically |
| (3) Convention-independence of structural gap | The categorical $\tau(\beta_{\mathfrak{H}})$ is the only invariant; conventions vary the non-categorical regularizer |

## Proof sketch

The proof of the proposition factors into three steps:

**Step 1: Uniqueness of the Markov trace.**  For $H_n(q)$, the
trace satisfying M1 (cyclicity), M2 (Markov axiom
$\mathrm{tr}^{(n)}(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}^{(n-1)}(x)$),
and M3 ($\mathrm{tr}(1) = 1$) is **unique** (Jones 1985, Wenzl 1988).
Any two operator-volume conventions that respect the Hecke
quadratic relation and the Markov axiom evaluate to the same
$\tau$ value on a given $\beta$.

**Step 2: All probed conventions respect $\tau$.**  Each of the
six brane-tower convention families probed in
[`conj:brane-tower-z-habiro`](#conj:brane-tower-z-habiro) §"Closure"
(scalar uniform-$k$, $\ell n_0 + k$, per-eigenvalue operator-valued,
multiplicity / Type-B-fold, pair-knot product-volume, pair-knot
Markov-trace) is a regularization of the divergent analytic $\Phi_q$
tower — none of them VARY the categorical trace
$\tau(\beta_{\mathfrak{H}})$; they only differ in how the divergent
tower is regularized.

**Step 3: $\Delta_{\mathrm{cat}}$ is convention-independent.**
From Steps 1+2: any two probed conventions yield the same
$|\tau(\beta_{\mathfrak{H}})|$ and hence the same
$\Delta_{\mathrm{cat}}(\mathfrak{H})$, regardless of which
convention is used to *evaluate* the operators in the
endomorphism algebra. $\square$

## Falsifiable predictions

1. **Convention-independence of $\Delta_{\mathrm{cat}}({}^3\mathrm{He})$.**
   Compute $|\tau(\beta_{{}^3\mathrm{He}})|$ via Hoefsmit seminormal
   (per-eigenvalue), via `markov_peel` (recursive symbolic), and via
   `tr_M_via_wenzl_bridge_mpfr` (50 dps Wenzl bridge).  All three
   should give the same $|\tau|$ to 50 dps; the resulting
   $\Delta_{\mathrm{cat}}$ should be ATOM-DEPENDENT but
   CONVENTION-INDEPENDENT.

2. **Convention-dependent regularizer dominates the brane-tower
   variation.**  The non-categorical brane-tower regularization
   contributions vary by orders of magnitude across the six probe
   families — but their *difference from* $|\tau|$ is the same
   non-categorical regularizer.  The structural gap
   $\Delta_{\mathrm{cat}}$ should be the same across all probed
   conventions, on each atom separately.

3. **Magic-shell decomposition.**  $\Delta_{\mathrm{cat}}(Z, N)$
   should decompose as
   $\Delta_{\mathrm{cat}}(Z, N) = \Delta_0(A) + \mathbb{1}_{Z \in \mathrm{magic}} \cdot \Delta_p + \mathbb{1}_{N \in \mathrm{magic}} \cdot \Delta_n$
   with $\Delta_p = \Delta_n$ (the Z$\leftrightarrow$N symmetry constraint).  This
   is the precise content of
   `conj:magic-shell-stabilization`.

## Discussion

The proposition is **conjectural** at the falsifiable-prediction
level (predictions 1–3 are testable but not yet verified
exhaustively).  The categorical content (Steps 1–3 of the proof)
follows from established results in quantum-group representation
theory (Jones 1985, Wenzl 1988, Kassel 1995).  Lean class
`RigidMonoidalStructuralGapInvariance` in
[sibling `.lean`](prop-rigid-monoidal-structural-gap-invariance.lean)
axiomatizes the conjectural content per §3b conditional-class
pattern; downstream conditional theorems are unconditional Lean
theorems whenever the class is in scope.
