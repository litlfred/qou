The QOU observability axiom requires
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([quantum observable universe](#def:quantum-observable-universe)
condition (ii)): the trivial representation does not appear in
the adjoint of $A$. This is a *rigidity* condition that
guarantees $A$ has no infinitesimal symmetries beyond the
identity.

Under a surreal lift, this can be relaxed to allow
infinitesimally many symmetries.

## Conjecture

The **$\varepsilon$-relaxed observability axiom** is:

$$
  \dim_{\mathbf{No}} \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))
   \;\leq\; \varepsilon,
$$

interpreted as: the hom-space is non-empty but every element has
$\mathbf{No}$-norm bounded by an infinitesimal $\varepsilon$.

The conjecture: a surreal QOU satisfying $\varepsilon$-relaxed
observability has standard-part image satisfying strict
observability.

## Plausibility

In the archimedean case, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$
is either zero or non-zero — there is no "small" middle ground.
In the surreal case, hom-spaces are $\mathbf{No}$-modules, so
"small" becomes "infinitesimal-norm" in a meaningful sense.

A natural example: take a strict-observability $A$ and add an
infinitesimal generator $\xi \in \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$
with $|\xi| = \varepsilon$. The resulting structure is a surreal
QOU with $\dim_{\mathbf{No}} \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))
= 1$ but $|\xi| = \varepsilon$, so the condition is satisfied if
"$\leq \varepsilon$" is read as norm-bound.

Whether such $\xi$ can be constructed cohomologically (rather than
imposed by hand) is open. The natural source is a non-trivial
class in $\mathrm{HH}^1(A, A)$ that becomes trivialised in the
archimedean limit but persists at infinitesimal order.

## Standard-part recovery

Applying $\mathrm{St}$ kills the infinitesimal $\xi$ (since
$\mathrm{st}(\varepsilon) = 0$), so the archimedean image has
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ — strict
observability is recovered. This is the easy direction of the
conjecture.

The hard direction is **lifting**: given an archimedean QOU with
strict observability, does there exist a surreal QOU above it
with relaxed observability and a non-trivial $\xi$? If so, the
relaxation is a strict generalisation; if not, the relaxation is
a tautology.

## Why this matters

The observability axiom controls *what counts as an observable*
in QOU: if $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$, every
endomorphism of $A$ is detectable by the fibre functor $\tau$.
Under the relaxation, infinitesimally many endomorphisms might be
*almost-detectable* — visible at first order in $\varepsilon$ but
invisible to standard-part archimedean observers.

Physically (if a physical reading is allowed): this corresponds
to *near-symmetries* — symmetries that are spontaneously broken
at archimedean scale but restored at infinitesimal scale. The
analog in particle physics is approximate isospin or chiral
symmetry, which are exact in some idealised limit and broken at
the physical scale by small parameters.
## Proof strategy

Same architecture as
[infinitesimal-frobenius](#conj:infinitesimal-frobenius):

**Standard-part recovery (provable now)**:

1. Given an $\varepsilon$-relaxed observability witness $\xi \in
   \mathrm{Hom}_{\mathbf{No}}(\mathbf{1}, \mathrm{Ad}(A))$ with
   $|\xi| \leq \varepsilon$.

2. $\mathrm{St}(\xi) = 0$ by `standardPart_of_infinitesimal`.
   The standard-part of the hom-space contains no non-zero
   elements: $\mathrm{Hom}_{\mathbb{R}}(\mathbf{1},
   \mathrm{Ad}(\mathrm{St}(A))) = 0$.

3. Strict observability holds for the standard-part image.

**Strict generalisation (open)**:

4. Construct a candidate non-trivial $\xi$. Source: a class in
   $\mathrm{HH}^1(A, A) \otimes_{\mathbb{R}} \mathbf{No}$ that
   becomes infinitesimal under standard-part.

5. Show that $\xi$ is **not** in the image of any classical (i.e.
   strict) Hochschild representative — this would establish
   strict generalisation.

**Required infrastructure**:
- `standardPart_of_infinitesimal` (proved).
- Surreal-coefficient Hochschild cohomology (does not exist in
  mathlib).
- A specific cohomological computation distinguishing
  $\mathrm{HH}^1_{\mathbb{R}} \otimes \mathbf{No}$ from
  $\mathrm{HH}^1_{\mathbf{No}}$.

**Falsification path**: prove that every infinitesimal element
of $\mathrm{Hom}_{\mathbf{No}}(\mathbf{1}, \mathrm{Ad}(A))$ comes
from a *real* element scaled by $\varepsilon$ (i.e., $\xi = \varepsilon
\cdot \eta$ for some $\eta \in \mathrm{Hom}_{\mathbb{R}}$). If
$\eta$ must vanish for $\xi$ to satisfy the original observability
constraint, the relaxation is empty.

**Provability assessment**: identical to
[infinitesimal-frobenius](#conj:infinitesimal-frobenius). One
side trivial, the other requires deformation theory.
