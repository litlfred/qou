The paper works over a commutative ring $R$ and not over the real
numbers. Two reasons lead there. The first is mathematical and holds
independently of any physical reading. The second concerns what can
actually be observed.

**The mathematical reason.** Every construction in the paper is
algebraic: braids, Hecke algebras, Markov traces, Frobenius pairings
and characters are all defined by finitely many polynomial identities.
Identities of this kind hold over every commutative ring at once, so a
proof carried out over a general $R$ proves the statement over
$\mathbb{Z}[q, q^{-1}]$, over $\mathbb{Q}(q)$, over a finite field,
over the $h$-adic power series and over $\mathbb{R}$ or $\mathbb{C}$,
all at the same time ([base-field independence](#rem:base-field-independence);
[generic ground ring](#rem:q-generic-ground-ring)). Specialising to
$\mathbb{R}$ early would add nothing to such a proof and would hide
which hypotheses it actually uses. Where a hypothesis on $R$ is needed,
for example that $q^2 - 1$ be invertible, the ring makes it visible as
an explicit unit condition rather than leaving it implicit in "$q \neq 1$".

**The observational reason.** We learn about nature by building
instruments with an intent and using them to make observations. The
more energy goes into building and running an instrument, the finer the
observation it returns. No observation so far has met a floor: the
resolution of nature appears to be unbounded. Our ability to resolve
it, however, is always finite, and it grows with the energy we invest
in the measurement. An observation is therefore never a real number.
It is a pair of bounds, "larger than this and smaller than that", and
a more expensive instrument narrows the window. In mathematical terms
an observation is a *cut*: a located pair of lower and upper bounds, in
the sense of Dedekind and Lawvere, and the completed real line is the
idealisation reached only in the limit of unlimited energy.

Taking the real numbers as the stage is therefore a physical
assumption, not a neutral convention: it asserts that every quantity
has infinitely many correct digits. Nothing we can observe can justify
that assertion. Nature may be finite and bounded, with some very large
$N$, or it may not. The paper does not decide this, and its models are
built to work either way. A model is required to give the same answers
whether it is read in a continuum or in a finite setting, as it would
be on a computer, and the agreement between the two readings has to be
a theorem rather than a hope. That requirement is what the extra
formalism of the paper buys. The categorical computations are carried
out over a general ring, and an archimedean realisation is applied
only at the very end. Every number compared with experiment is reported
as a cut.

**Why the surreal numbers.** The usual $\varepsilon$–$\delta$ analysis
treats an error as a small real number and forgets where it came from.
That forgets too much. An error term in this paper is typically a
$q$-series, a cyclotomic expansion or an element of a Bloch group, and
its algebraic and number-theoretic structure is exactly what later
arguments use. The algebraic route to the volume conjecture shows this.
There the asymptotics of the Kashaev invariant are tracked through its
Habiro expansion and through the Bloch group, rather than through a
limit of real numbers ([Habiro ring](#def:habiro-ring);
[Kashaev volume conjecture](#conj:kashaev-volume-conjecture)). Conway's
surreal numbers give a field large enough to name infinitesimal and
infinite errors as genuine elements, ordered and with arithmetic. In
them the error of an approximation keeps its algebraic form instead of
collapsing to a single real bound. The [surreal appendix](#app:surreals)
develops this, and the classical statements are recovered from it by
taking standard parts.
