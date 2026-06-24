Each substrate identity is stated in the cited literature
(Wenzl 1988; Jones 1987) over a commutative ring with $q$ a unit;
the QOU formalisation enforces the same generic typing through
[`AGENTS.md` §7c](https://github.com/litlfred/qou/blob/main/AGENTS.md#7c-base-ring-convention-generic-r-vs-archimedean-r-strict)
("base-ring convention"). The relevant Lean files
([`hq-bi-filtration.lean`](hq-bi-filtration.lean),
[`explicit-central-idempotent.lean`](explicit-central-idempotent.lean),
[`categorical-q-lie-bracket.lean`](../quantum-observable-universes/categorical-q-lie-bracket.lean),
[`bar-involution.lean`](bar-involution.lean)) all carry
`{R : Type*} [CommRing R]` (or stronger) and `{q : R}` without an
ordering predicate.

The condition $\lvert q \rvert > 1$ on $\mathbb{C}$ is sufficient to
make $q$ a unit (since $\lvert q \rvert > 0$ implies $q \neq 0$), so
the existing polymorphic identities specialize. $\quad\square$
