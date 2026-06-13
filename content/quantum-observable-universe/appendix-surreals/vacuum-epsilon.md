The Hoefsmit scattering pipeline assigns to each link $L$ a
*geometric energy* $\mathrm{Geom}(L) \in \mathbb{R}$
([Hoefsmit scattering pipeline](#conj:hoefsmit-scattering-pipeline)).
The vacuum normalisation requires $\mathrm{Geom}(\unicode{9737}) = 0$
on the unknot, so that the empty link contributes nothing to
particle masses.

This strict-zero condition is awkward in two ways:

1. It introduces a *boundary case* — the unknot must be
 special-cased in the geometric-energy formula.
2. It is *physically suspicious* — a "vacuum energy" of exactly
 zero is the textbook signature of a fine-tuned theory, and is
 thought by many to be the wrong setting (cosmological
 constant problem, vacuum-fluctuation arguments, etc.).

Under a surreal lift, the strict zero can be relaxed.

## Conjecture

The **$\varepsilon$-relaxed vacuum axiom** is:

$$
  \mathrm{Geom}(\unicode{9737}) \;=\; \varepsilon \in \mathbf{No},
$$

a single positive infinitesimal. The conjecture: every surreal
QOU satisfies this relaxation with some choice of $\varepsilon
> 0$, and the standard-part recovers the strict vacuum:
$\mathrm{st}(\varepsilon) = 0$.

## Consequences

If the conjecture holds, several existing results lift:

1. **Geometric-energy formula** simplifies: the special case for
 $\unicode{9737}$ is absorbed into the general formula, giving
 $\mathrm{Geom}(L) = (\text{generic formula}) +
   \varepsilon \cdot (\text{number of unknot components})$.

2. **Möbius energy regularisation** maps : the diagonal
 subtraction in the Möbius energy is exactly the
 $\varepsilon$-vacuum contribution.

3. **Mass spectrum** acquires an infinitesimal shift: every
 particle mass $\mathfrak{m}(\mathfrak{H})$ becomes
 $\mathfrak{m}(\mathfrak{H}) + \varepsilon \cdot c_{\mathfrak{H}}$
 for some standard-real $c_{\mathfrak{H}}$. Standard-part of
 this shift is zero, so archimedean predictions are unchanged.

4. **Boundary-conditioned vacuum sums become finite**: when the
 multiplier of $\varepsilon$ is not a standard real but a
 surreal-infinite mode count, the product can have *nonzero*
 standard part, since $\omega \cdot \varepsilon = 1$. The
 parallel-plate geometry realises exactly this case: the
 [Casimir force](#conj:casimir-epsilon-vacuum) is the
 $\mathrm{st}$-image of the plate-constrained unknot-count
 gradient times $\varepsilon$. Consequences 3 and 4 are the two
 regimes of the same axiom — a finite multiplier leaves
 archimedean predictions unchanged, while a surreal-infinite
 multiplier returns a finite force.

## Why this matters

Two reasons:

1. **Cleaner axioms**: the strict-zero vacuum is a fine-tuning
 that would-be reviewers can object to. The
 $\varepsilon$-vacuum is a parameter, not a fine-tuning, and
 the archimedean theory is recovered by standard-part.

2. **Möbius regularisation absorbed**: the diagonal-subtraction
 trick in the Möbius energy
 ([Möbius energy proof](#prf:mobius-energy)) becomes a special
 case of $\varepsilon$-vacuum subtraction. This unifies two
 regularisations into one.

## Discussion

**Open**. The conjecture is the most directly testable of the
appendix's relaxation conjectures: pick an
$\varepsilon \in \mathbf{No}$, recompute the QOU mass spectrum,
and check whether the archimedean image agrees with the strict-
vacuum prediction. The arithmetic is rational in $\varepsilon$,
The test reduces to a comparison of two polynomials in
$\varepsilon$ at the standard-part.

## Proof strategy

The most direct of the conjectures: pure computation.

1. **Recompute geometric energy** with vacuum convention
 $\mathrm{Geom}(\unicode{9737}) = \varepsilon$. For each link
 $L$ in the QOU mass table (Z=1–20),
 $\mathrm{Geom}(L)$ now has an additive $\varepsilon$-dependent
 correction proportional to the number of unknot components.

2. **Recompute particle masses**:
 $\mathfrak{m}(\mathfrak{H}) \to \mathfrak{m}(\mathfrak{H}) +
   \varepsilon \cdot c_{\mathfrak{H}}$.

3. **Apply $\mathrm{St}$**: standard-part of
 $\mathfrak{m}(\mathfrak{H}) + \varepsilon \cdot c_{\mathfrak{H}}$
 equals $\mathfrak{m}(\mathfrak{H})$ — the original mass. So
 archimedean predictions are unchanged.

4. **Verify Möbius regularisation absorbed**: show that the
 diagonal subtraction in
 [Möbius energy proof](#prf:mobius-energy) is exactly
 $\varepsilon \cdot (\text{boundary contribution})$, so the
 classical regularisation is the $\mathrm{St}$-image of the
 $\varepsilon$-vacuum subtraction.

**Required infrastructure**:
- `QOU.AppendixSurreals.standardPart_of_infinitesimal` (proved).
- `QOU.AppendixSurreals.standardPart_add` (axiomatic).
- Existing QOU mass table.

**Falsification path**: recompute the mass spectrum with
$\mathrm{Geom}(\unicode{9737}) = \varepsilon$ and find that some
particle mass *changes* under standard-part (i.e.,
$\mathrm{St}(\mathfrak{m} + \varepsilon \cdot c) \neq \mathfrak{m}$).
This would only happen if $c$ contained a non-infinitesimal
factor, contradicting the rational-in-$\varepsilon$ structure.

**Provability assessment**: this is a *computational* conjecture.
The verification is a mass-table re-computation that can be
done in Python/Mathematica today. Lean formalisation reduces to
the standard-part-of-infinitesimal lemma already proved.

**Easiest of the appendix conjectures to settle.**
