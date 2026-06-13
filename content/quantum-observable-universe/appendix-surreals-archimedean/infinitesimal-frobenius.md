The Frobenius axiom in
[quantum observable universe](#def:quantum-observable-universe)
requires the pairing $\int_A \circ \mu : A \otimes A \to \mathbf{1}$
to induce an isomorphism $A \xrightarrow{\sim} A^{\vee}$ — a
strict equality. In a surreal QOU, this can be relaxed.

## Conjecture

Let $A$ be a Frobenius--Hopf object in a $K$-linear monoidal
category with $K = \mathbf{No}$. The **$\varepsilon$-relaxed
Frobenius axiom** is:

$$
  (\int_A \circ \mu) \circ \eta_{A^\vee}
  \;=\; \mathrm{id}_{A^\vee} + \varepsilon \cdot \delta,
$$

where $\eta_{A^\vee} : A^\vee \to A \otimes A^\vee$ is the
adjoint coevaluation, $\varepsilon \in \mathbf{No}$ is a fixed
positive infinitesimal, and $\delta : A^\vee \to A^\vee$ is an
arbitrary $K$-linear endomorphism (the *deviation*).

The conjecture has two parts:

1. **Standard-part recovery**: applying the standard-part functor
 $\mathrm{St}$
 ([standard-part functor](#def:standard-part-functor)) to a
 relaxed Frobenius axiom yields a strict Frobenius axiom on the
 archimedean image. Concretely, $\mathrm{St}(\delta) = 0$ is
 automatic if and only if the deviation is birthday-shifted.

2. **Strict generalisation**: there exist relaxed Frobenius
 structures with non-trivial deviation $\delta$ (i.e. not
 gauge-equivalent to the strict structure) that nonetheless
 project to the same archimedean Frobenius structure.

If (2) holds, the relaxation is a *strict* generalisation of the
classical Frobenius axiom, with the surreal QOU carrying first-
order $\varepsilon$-corrections invisible to the archimedean QOU.

## Plausibility

The classical Frobenius axiom $\int \circ \mu = \mathrm{id}$ is a
*non-degeneracy* condition. In a $\mathbb{R}$-linear category, this
is binary (degenerate or not). In a $\mathbf{No}$-linear category,
non-degeneracy can fail at infinitesimal scale: a pairing can have
its Gram determinant equal to $1 + \varepsilon \cdot \delta$
rather than $1$.

Whether such infinitesimal degeneracies are *realisable* (i.e.
constructible from QOU axioms) is the content of (2). The natural
candidate is to deform $A$ by a coboundary at infinitesimal order:

- pick a $\delta \in \mathrm{End}(A^\vee)$;
- define a new comultiplication $\Delta_\varepsilon = \Delta + \varepsilon
  (\delta \otimes 1) \circ \Delta$;
- check that the Frobenius axiom is satisfied to order $O(\varepsilon)$.

Whether the resulting structure is gauge-equivalent to the
strict $A$ is open.

## Why this matters

Three uses:

1. **Möbius energy**: the diagonal regularisation in the Möbius
 energy formula
 ([Möbius energy proof](#prf:mobius-energy)) is accordingly read
 as an infinitesimal Frobenius deviation: the strict Frobenius
 axiom $\int \delta(0) = $ infinity becomes $\int \delta(\varepsilon)
   = 1/\varepsilon$, and the regularised value is the
 standard-part.

2. **CODATA fits**: the QOU mass formula's $\sim 4\%$ MAE on
 $\mathcal{Q}$-values may be partly attributable to a small
 non-Frobenius deviation in the underlying algebra. An
 infinitesimal Frobenius axiom would absorb such deviations
 into a single $\varepsilon$-parameter.

3. **Mathematical interest**: even without physical motivation,
 the relaxation gives a one-parameter deformation theory for
 Frobenius algebras, parallel to the classical
 Hochschild-cohomology obstruction theory but valued in
 $\mathbf{No}$ rather than $\mathbb{R}$.
## Proof strategy

The conjecture has two halves: standard-part recovery (easy)
and strict generalisation (hard).

**Standard-part recovery (provable now)**:

1. Assume an $\varepsilon$-relaxed Frobenius algebra
 $(A, \mu, \int_A, \delta)$ over $\mathbf{No}$.

2. Apply $\mathrm{St}$ to all components: $\mathrm{St}(\delta)$ has
 coefficients in $\mathbb{R}$. Since $\delta$ is multiplied by
 the infinitesimal $\varepsilon$, the term $\varepsilon \cdot \delta$
 is itself infinitesimal.

3. By `standardPart_of_infinitesimal`, $\mathrm{St}(\varepsilon
   \cdot \delta) = 0$. So $\mathrm{St}((\int \circ \mu) \circ \eta)
   = \mathrm{St}(\mathrm{id} + \varepsilon \cdot \delta) = \mathrm{id}$,
 recovering the strict Frobenius axiom.

**Strict generalisation (open)**:

4. Construct a candidate non-trivial $\delta$ in a non-rigid
 Frobenius algebra. Concrete proposal: take
 $A = \bigwedge^* V$ (exterior algebra) at infinitesimal
 $q$-deformation; the rigidity argument doesn't apply because
 $\bigwedge^* V$ is not the regular representation.

5. Verify the deformed pairing satisfies
 $\int_\varepsilon \circ \mu_\varepsilon = \mathrm{id} +
   \varepsilon \cdot \delta$ for non-zero $\delta$.

6. Show the deformed structure is **not** gauge-equivalent to
 the strict structure (a Hochschild-cohomology computation).

**Required infrastructure**:
- `standardPart_of_infinitesimal` (proved).
- `standardPart_add` (axiomatic; reduces to
 `IsFinite_decomposition`).
- Hochschild cohomology of Frobenius algebras over $\mathbf{No}$
 (does not exist in mathlib).

**Falsification path**: prove a *rigidity theorem* for
$\varepsilon$-Frobenius algebras: every $\varepsilon$-deformation
is gauge-equivalent to the strict structure. This would refute
the strict-generalisation half by collapsing the relaxation.

**Provability assessment**: standard-part recovery provable in
Lean today (modulo `standardPart_add` axiom). Strict
generalisation requires deformation theory of Frobenius algebras
over a surreal-coefficient field — substantial new mathematics.
