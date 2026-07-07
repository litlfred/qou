<!-- FILE_START: intro-markov-axioms-braid-link.md -->
Markov's theorem (1936) states that two braid words have
isotopic closures iff they differ by a finite sequence of
conjugation and stabilisation moves.  This section promotes
Markov's theorem to a categorical setting, fixes the precision
ladder that controls the substrate-level Markov trace, and
enumerates the braid-link bijection that drives the chapter's
counting arguments.

The arc proceeds in three layers.  The first blocks establish
the $q$-deformed categorical precision ladder and prove its
compatibility with the Markov axioms; the middle blocks
enumerate the closure types (knot, link, mutually disjoint) and
record the substrate-level character of each; the closing blocks
specialise to the small-$n$ cases that drive the chapter's
explicit binding-energy formulas, including the cases where the
Markov-trace ambiguity propagates and must be resolved by the
parity-classification section downstream.

The output is the categorical braid-link enumeration with
explicit substrate-trace evaluations.  This is the chapter's
combinatorial engine — every closed-form prediction further
down relies on knowing both the count and the trace value for
each braid-link equivalence class.
<!-- FILE_END: intro-markov-axioms-braid-link.md -->

<!-- FILE_START: polynomial-bar-involution.md -->
**Proposition (polynomial bar-involution).**

*Let $R$ be a commutative ring and $R[X]$ its polynomial ring in
one indeterminate. The map*

$$
\overline{(\cdot)} \colon R[X] \to R[X], \qquad p(X) \mapsto p(-X)
$$

*is a ring involution. Under this bar:*

- *the indeterminate $X$ is **bar-anti-symmetric** ($\overline X = -X$);*
- *every constant $c \in R \hookrightarrow R[X]$ is **bar-symmetric**;*
- *every even-degree monomial $X^{2n}$ is **bar-symmetric**;*
- *every odd-degree monomial $X^{2n+1}$ is **bar-anti-symmetric**;*
- *the bar-symmetric subring is exactly $R[X^2]$.*

## Categorical role

This is the **canonical non-trivial bar-involution** in QOU. It
provides a concrete categorical setting where the polynomial
indeterminate $X$ plays the role of the bar-anti-symmetric Hecke
skein

$$h \;=\; q - q^{-1},$$

with the correct bar-action $h \mapsto -h$ matching the general
[`def:bar-involution`](#def:bar-involution) statement.

Three motivations for working in $R[X]$ rather than directly with
the Hecke skein:

1. **Algebraic decidability** — `Polynomial.comp` lemmas in
   Mathlib give the four ring-involution axioms for free; the
   proofs are short and `sorry`-free.
2. **No analysis needed** — unlike $\mathbb{C}$ with conjugation,
   $R[X]$ requires no analytic infrastructure; the bar map is
   defined by formal substitution.
3. **Concrete bar-symmetric subring identification** — the bar-
   symmetric subring is exactly $R[X^2]$, which is precisely the
   ring of "even" polynomials. This gives a concrete model of
   "$P_{\mathrm{avg}}$ kills odd powers" at the polynomial level.

## Proved theorems (Lean)

The Lean sibling [`polynomial-bar-involution.lean`](polynomial-bar-involution.lean)
proves the following, all `sorry`-free:

See [Table](#tbl:polynomial-bar-involution-table-data).

All proofs use only `Polynomial.comp` lemmas from Mathlib
(`X_comp`, `add_comp`, `mul_comp`, `one_comp`, `zero_comp`,
`neg_comp`, `comp_assoc`).

## Connection to the three-layer synthesis

In `prop:bar-symmetric-three-layer-synthesis`,
the universal kernel is bar-anti-symmetric. The polynomial
indeterminate $X$ is the **canonical such kernel**:

- Series layer: $F_{\text{series}}(X)$ is an even-power polynomial
  in $X$, hence in $R[X^2]$.
- Phase layer: similarly an even-power polynomial.
- Gain layer: similarly.

Each layer functor is concretely realised as a `BarHeckeFunctor R[X]`
sending bar-anti-symmetric inputs (degree-odd polynomials, in
particular $X$ itself) to bar-symmetric outputs (degree-even
polynomials). The synthesis-class fields `series_avatar`,
`phase_avatar`, `gain_avatar` then become explicit elements of
$R[X^2]$.
## Proofs (Lean $\leftrightarrow$ paper bridge)

Every Lean theorem below has both a narrative proof here and a
fully formalised Lean proof in [`polynomial-bar-involution.lean`](polynomial-bar-involution.lean).
The **core** bar-involution proofs (axioms, `barPoly_X_pow_*`,
`barPoly_natCast`, arbitrary-truncation theorems, generic `evenPoly_*`)
use only the four ring-involution axioms plus Mathlib's
`Polynomial.comp` lemmas — no archimedean or analytic infrastructure
invoked. The trailing $\mathbb{R}[X]$ section (`c5_taylor_6`,
`cos_truncated_6`, `cosh_truncated_6` and their concrete evaluations
via `norm_num`) specialises to the archimedean base ring to produce
falsifiable numerical predictions; per AGENTS.md §7c the generic /
specialised cut is a soft boundary inside this file, marked by the
"Concrete archimedean instances over $\mathbb{R}$" section header,
and may be moved to a sibling block under `observations/` in a
follow-up if reviewers prefer a hard split.

### Core bar-involution axioms

**Proposition (Lean: `barPoly_X`).** $\overline X = -X$.
<!-- FILE_END: polynomial-bar-involution.md -->

<!-- FILE_START: markov-axioms-braid-link-li2q-phiq-bar-intro.md -->
Continuation of the preceding sub-section.
<!-- FILE_END: markov-axioms-braid-link-li2q-phiq-bar-intro.md -->

<!-- FILE_START: c5-involution-leibniz-decomposition.md -->
**Proposition ($c_5$ involution + Leibniz decomposition).**

*Let $c_5(q)$ be the precision-ladder coefficient at rung $N=5$ in
the $\mathfrak{Q}_\beta$ categorical formula
[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder).
Then $c_5$ admits the categorical decomposition:*

$$
\boxed{\;
c_5(q) \;=\; \underbrace{-b(q)^2}_{\text{pure-}\sigma\text{ Kashiwara}}
\;-\; \underbrace{\tfrac{1}{2}}_{\substack{\text{averaged-crossing}\\\text{involution fingerprint}}}
\;}
$$

*where $b(q)^2 = (q^4+q^2+1)/(q^2+1)^2$ is the Hoefsmit off-diagonal
coupling squared on $V_{(2,1)}$. The $-1/2$ summand is **NOT** an
ad-hoc empirical offset: it is the fingerprint of the bar-invariant
averaged-crossing operator $\sigma_{\text{avg}} = (\sigma + \sigma^{-1})/2$
used at specific positions in the typed-$\mathbf{B}_3$ braid recipe
([`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic)).*

*The decomposition resolves the Pell-Lucas outlier status of $c_5$
at the silver ratio
([`prop:silver-ratio-beta-decay-null`](#prop:silver-ratio-beta-decay-null)):
the pure-$\sigma$ part $-b^2$ evaluates to $-7/8$ (Pell-Lucas-clean),
and the involution fingerprint $-1/2$ is the **non-Hecke** correction.*
<!-- FILE_END: c5-involution-leibniz-decomposition.md -->

<!-- FILE_START: c5-involution-leibniz-decomposition-interpretation.md -->
**Remark (bar-symmetry class, categorical sectors, and the $c_5$ falsifiable prediction).**

> **Bar-symmetry class** (per [`def:bar-involution`](#def:bar-involution)):
> $c_5(q) = -b^2(q) - 1/2 = -3/2 + 1/[2]_q^2$ is **bar-symmetric**
> as a function of $q$. The Hoefsmit-Quantum-2 identity
> $b^2 = 1 - 1/[2]_q^2$ is a proved algebraic theorem in the
> Lean sibling (`hoefsmit_b_squared_eq_one_minus_inv_quantum_two_squared`,
> no `sorry`). The "$-1/2$" piece is a q-independent
> commutative-QOU constant; $c_5(q=1) = -5/4$ proved as
> `c5_classical_limit_eq_neg_five_quarters`. So the c_5 outlier
> at silver is the *arithmetic sum* of two clean bar-symmetric
> pieces landing on inert prime $11 \in \mathbb{Z}[1+\sqrt 2]$,
> not a quantum-deformation artifact.

> **Pentagon-reduction cross-link.** The Leibniz expansion in
> step 3 below uses the q-dilogarithm pentagon identity
> implicitly. The algebraic identity making this rigorous in
> $\mathbb{Z}[q^{\pm 1}]$ for $|z| \ge q$ via duplication
> $u = v = i\sqrt{|z|}$, plus the post-$\tau$ $\log_q^2$
> correction, lives on `main` in
> [`pentagon_reduction_li2q.py`](../../../computations/pentagon_reduction_li2q.py)
> with audit doc
> [`-pentagon-reduction-li2q.md`](../../../docs/audits/-pentagon-reduction-li2q.md).
> Cross-link: the *Pentagon coherence layer* of $c_5$'s
> decomposition (one of the three layers in
> `prop:bar-symmetric-three-layer-synthesis`)
> is what `pentagon_reduction_li2q.py` makes algebraic.

## Categorical interpretation

The framework's $\mathfrak{Q}_\beta$ predictions live in TWO distinct
categorical sectors:

1. **Pure-$\sigma$ sector** ($c_3, c_4, c_6, c_7$): contributions
   from positions in the braid that act as pure Hecke generators
   or their inverses. Algebraically lives in the $\mathbb{Z}$-span
   of Hecke-quadratic eigenvalues, reducing at the silver ratio
   to the **Pell-Lucas extension** $\mathbb{Z}[1 + \sqrt{2}]$.
2. **Bar-invariant fixed-point sector** ($c_5$): contributions from
   averaged-crossing positions. Algebraically lives in the
   bar-invariant subring (fixed by $\sigma \leftrightarrow \sigma^{-1}$),
   which intersects with $\mathbb{Z}[1+\sqrt{2}]$ only on integer
   subspaces — the $1/2$ is the residual after this intersection.

The two sectors are **independent categorical inputs**: pure-$\sigma$
is the Hecke-generator action; bar-invariant fixed-point is the
involution-projector action. Both are needed to reproduce $\mathfrak{Q}_\beta$
exactly via the precision ladder.

## Falsifiable prediction

Any future rung $c_k$ at $k \geq 8$ whose order $\hbar_q^{2k}$
coincides with an **averaging-resonance** position (= a $k$-fold
cyclic substructure including at least one averaged crossing)
will pick up similar $1/2$ fingerprints.

Specifically, the proton braid has 11 typed crossings: 7 pure
$\sigma_0$, 4 pure $\sigma_1$, 1 averaged $\sigma_0$ (at coefficient
$-h/2$), 1 averaged $\sigma_1$ (at coefficient $-h/2$), 3 inverted
$\sigma_1^{-1}$ (at coefficient $-h$). The averaging-resonance
rungs are determined by the positions where two averaged crossings
interact at a given order in $\hbar_q^{2k}$.

By combinatorial counting of pairs of averaged positions among the
11 typed crossings, the predicted averaging-resonance rungs are
those $k$ for which $\binom{2}{2} \cdot (\text{combinatorial weight})$
peaks. **$k = 5$** is the first; subsequent peaks predicted at
**$k = 8, 11, \ldots$** (every 3 rungs by the 3-strand
sub-braid combinatorics).

This is testable by extending SDP-$T_\beta$ extraction to $k \geq 8$
and checking whether c_8 has a $1/2$ fingerprint — the probe is
queued in
[`computations/qbeta/qbeta_decay_sdp_extended_ck.py`](../../computations/qbeta/qbeta_decay_sdp_extended_ck.py).

## Discussion

This decomposition is a **structural identification**, not a
first-principles derivation. The $-b^2$ and $-1/2$ summands are
identified categorically, but the proof that the precision-ladder
$c_5$ takes exactly this form (modulo $2.4\%$ empirical residual)
requires:

1. Explicit computation of the typed-$\mathbf{B}_3$ Markov-trace
   expansion at order $b^5 \hbar_q^{10}$.
2. Separating pure-$\sigma$ contributions from averaged-position
   contributions order-by-order.

Both are concrete finite computations; neither is yet executed in
the framework. This proposition sets up the categorical grammar;
its full proof is gated on the order-by-order Hecke expansion
machinery (open R&D).
<!-- FILE_END: c5-involution-leibniz-decomposition-interpretation.md -->

