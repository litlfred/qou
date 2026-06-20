**Proposition** (q-zero complex extension).
*Let $R$ be a commutative ring and $q \in R^\times$ a unit. Every
pre-Archimedean substrate identity — the Hecke quadratic
$\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ on the Iwahori–Hecke algebra
$H_n(R, q)$, the [bar involution](#def:bar-involution)
$q \leftrightarrow q^{-1}$, $\sigma_i \leftrightarrow \sigma_i^{-1}$,
the Frobenius pairing $\langle\cdot,\cdot\rangle_F$ on the
Hecke–Hopf substrate, and the Markov trace
$\mathrm{tr}_M \colon H_n(R, q) \to R$ — is stated polymorphically
in $R$. In particular the specialization*

$$
R \;=\; \mathbb{C}, \qquad q_0 \in \mathbb{C} \quad \text{with}
   \quad \lvert q_0 \rvert > 1
$$

*is admissible: the substrate identities transfer verbatim, with
$\lvert q \rvert > 1$ replacing the archimedean ordering $q > 1$ as
the substrate-level non-degeneracy condition.*

## Proof

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

## Significance

The proposition makes explicit that the framework's pre-Archimedean
content is *independent of the choice of $\mathrm{Im}(q)$*. The
current convention $q_0 \in \mathbb{R}$, $q_0 > 1$ is one valid
specialization: the one whose Archimedean realisation $\tau$ maps
into $\mathbf{Vec}_\mathbb{R}$.

**CAL-4 caveat:** a complex $q_0$ with $\lvert q_0 \rvert > 1$ would require either:

1. **A function** expressing $\mathrm{Im}(q_0)$ in terms of the
   three existing calibrations $(m_e,\,m_\mu/m_e,\,\mathfrak{Q}_\beta)$ — *not*
   a fourth calibration, which the
   [three-input discipline](#rem:calibration-inputs) forbids; or
2. **A structural constraint** fixing $\mathrm{Im}(q_0)$ from
   substrate data (e.g. a self-consistency equation in the Hecke
   algebra over $\mathbb{C}$).

Neither is currently supplied. The proposition is *infrastructure*
for the categorical lift; it is not a claim about physical reality
of $\mathrm{Im}(q_0)$.

## Relation to the unit-circle deformation

The codebase already treats one complex-$q$ regime: the unit circle
$q = e^{i\Theta}$, where the bar involution coincides with complex
conjugation and the pair $(\Phi_q, \mathrm{Li}_2^q)$ becomes a
Hermitian-conjugate pair (see
[`commutative-chirality-vanishes`](#cor:commutative-chirality-vanishes)
and cheat-sheet §4). This proposition extends the admissible regime
to $\lvert q \rvert > 1$, where Lusztig bar and Hermitian $\ast$
*split* (see [`lusztig-vs-hermitian-bar`](#prop:lusztig-vs-hermitian-bar)).
The unit-circle case is the boundary; the real-axis case is the
$\mathrm{Im}(q) = 0$ specialization; the general complex case is
between them.
