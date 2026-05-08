The black hole information paradox \cite{hawking1975} asks
whether information that falls past the event horizon is
destroyed, preserved but inaccessible, or slowly radiated back
in Hawking quanta.  The incompleteness--horizon identification
([incompleteness as opacity](#rem:incompleteness-horizon))
reframes this as a question about arithmetic, not gravity.

**Picture.**  Think of the horizon as a **syntax boundary**.
Beyond it lie sections that **exist** as semantic objects in the
model — well-defined elements of the full algebra
$\Gamma(\mathcal{S}, A_0)$ — but **no finite braid computation**
from outside can derive them.  They are syntactically
unprovable.  This is the categorical reading of Gödel:
existence without provability is the rule at the boundary, and
the Bekenstein–Hawking entropy counts only what leaks across
(degree-$1$ witnesses), never what remains hidden (degree-$0$
truth).

**The paradox, restated.**

A black hole interior is a region where $A_0 = 0$
([jet horizon](#def:jet-horizon)).  The degree-$0$ sections
that describe particle identities, crossing structures, and
fibre values inside the horizon are **well-defined elements**
of $\Gamma(\mathcal{S}, A_0)$ --- they exist in the full
algebra.  But they are not elements of
$\Gamma_{\mathrm{fin}}(\mathcal{S}, A_0)$: no finite
braid computation from outside the horizon can produce them.

This is the structure of a G\"{o}del sentence: a statement
that is **true** in the model (the section exists) but
**unprovable** from the accessible axioms (no finite
derivation from outside can reach it).

The three standard positions on the paradox map to three
positions on incompleteness:

| Position | Information paradox | Incompleteness analog |
|----------|-------------------|---------------------|
| Information is destroyed | Sections in the interior have no algebraic meaning | G\"{o}del sentences are neither true nor false (rejected by standard model theory) |
| Information is preserved but inaccessible | Sections exist but cannot be computed from outside | G\"{o}del sentences are true but unprovable (the standard reading) |
| Information escapes via Hawking radiation | Degree $\geq 1$ data gradually reconstructs degree-$0$ truth | Partial witnesses accumulate toward a proof that never terminates |

The QOU framework selects the second option: the sections
exist (the algebra $A$ is well-defined everywhere, including
behind the horizon), but no finite sequence of Planck steps
from outside the horizon reaches them.

**The Bekenstein--Hawking entropy as a G\"{o}del count.**

The Bekenstein--Hawking entropy $S = A / (4\ell_P^2)$
\cite{bekenstein1973} counts the dimension of
$\Gamma(\mathcal{H}, A_1/A_0)$ --- the independent
degree-$1$ sections on the horizon surface
([Hawking radiation](#rem:hawking-radiation)).  These are
the statements that **can** be witnessed from outside:
the verifiable partial evidence, the thermal leakage, the
NP witnesses.

The degree-$0$ sections behind the horizon --- the
G\"{o}delian core --- are not counted by the
Bekenstein--Hawking entropy.  They are the **uncountably
many** true statements that the horizon conceals.  The
entropy counts only what leaks: the proof fragments, not
the theorems.

$$
  S_{\mathrm{BH}}
  \;=\;
  \dim \Gamma(\mathcal{H},\, A_1/A_0)
  \;=\;
  \text{number of witnessable facts}
  \;\neq\;
  \dim \Gamma(\mathcal{H},\, A_0)
  \;=\; 0.
$$

The entropy is large (proportional to area) because the
degree-$1$ space is rich --- many witnesses, many thermal
modes, many partial truths.  The degree-$0$ space is empty
--- no complete truths cross the boundary.  This asymmetry
is not a feature of gravity.  It is a feature of any
formal system powerful enough to encode self-referential
computation.

**Aeon boundaries as G\"{o}del boundaries.**

The identification extends to cosmological horizons.  An
aeon boundary ([aeon](#def:aeon)) is a locus where
$A_0 = 0$ --- degree-$0$ sections vanish, and the
observable subcategory $\mathrm{Bun}^{\circ}$ terminates.
The Big Bang state ([Big Bang](#def:big-bang-state)) is
such a boundary: the universe begins with no degree-$0$
data and accumulates it through Planck-step computation.

From the incompleteness perspective, each aeon is a
**consistent theory**: a connected component of
$\mathrm{Bun}^{\circ}$ where degree-$0$ sections are
non-trivial and the Frobenius pairing is non-degenerate.
The aeon boundary is where the theory reaches its
expressive limit --- where the G\"{o}delian sentences
live.  Crossing an aeon boundary
([aeon recycling](#conj:aeon-boundary-generates-chart))
is passing to a **stronger theory**: the degree $\geq 1$
data from the dying aeon seeds the axioms of the next,
just as adding a G\"{o}del sentence to a theory produces
a strictly stronger (but still incomplete) theory.

The universe does not resolve its own incompleteness.  It
iterates past it --- aeon by aeon, each one a consistent
fragment, each boundary a reminder that degree-$0$ truth
outruns finite derivation.
