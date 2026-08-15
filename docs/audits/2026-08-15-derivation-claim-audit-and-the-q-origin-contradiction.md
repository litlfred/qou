# The corpus said $q$ is "completely constrained" by the braiding. It also says $q_0$ is a calibration.

Bean `qou-5r17`. Scanner:
[`derivation_claim_audit.py`](scripts/derivation_claim_audit.py) ·
witness [`…witness.json`](scripts/derivation_claim_audit.witness.json).

Commissioned after the #5044 retraction, where a Ch 9 intro claimed a result was
*"forced by the braiding rather than assumed"* when the hexagon identities are
class fields of Mathlib's `BraidedCategory` — axioms. The question: is that an
isolated slip, or a pattern?

## Method, and why it is not a grep

A bare search for `derived` returns **454 hits across 291 files** and is almost
all noise — `def:derived-atom` is a defined term, "derived from the Markov trace"
is ordinary and correct.

What carries an epistemic claim is the **contrastive** form: prose asserting
something is derived *rather than* assumed. Those can be wrong. Filtering to
predicative and contrastive constructions, and discounting noun usages, gives
**134 candidates**, tiered by whether the sentence also names a block whose kind
is `definition` or `conjecture`.

| tier | shape | count |
|---|---|---|
| 1 | contrastive denial + assumed-kind label in the same sentence | 3 |
| 2 | contrastive denial, no co-located label | 76 |
| 3 | plain predicative "is derived" | 55 |

**Tier 1 was noise.** One is a table the sentence-splitter mangled; one is
`schwinger-measure-unit`, which says *"conditionally forced by"* and names the
conjecture — exactly the right phrasing. The tiering heuristic ranked the honest
block highest. Recorded so the next run does not trust the ordering.

## The finding, in tier 2

Two blocks state the origin of $q$ without distinguishing the parameter from its
value:

- [`braiding-eigenvalue-extraction-novelty`](../../content/quantum-observable-universe/quantum-observable-universes/braiding-eigenvalue-extraction-novelty.md)
- [`tannaka-krein-overview`](../../content/quantum-observable-universe/quantum-universes/tannaka-krein-overview.md)

The first went furthest. Its second paragraph claimed as *"the mathematical
novelty"*:

> a rigorous proof that the macroscopic substrate parameter governing the fluid
> PDE is **precisely and completely constrained** by the microscopic categorical
> braiding of the observable universe

Against the corpus's own statements about the same parameter:

| block | says |
|---|---|
| `three-calibration-discipline` | *"The QOU framework admits exactly **three external calibration inputs**"*; $q_0$ is CAL-2 |
| `epistemic-status-of-calibrations` | *"$q_0 \approx 1.10998$ is **pinned by matching** $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ to the CODATA value"* — and plainly: *"**We defined $q_0$ to enforce it.**"* |

These cannot both hold. If the braiding completely constrained $q_0$, it would
not need defining to enforce a CODATA match, and the discipline would count two
calibrations, not three.

## Why the claim fails

The parameter and its value are different objects, and the framework already has
vocabulary for the split (AGENTS.md §"Im(q) at fibre vs observable level"):

- **Fibre level.** $q$ is the braiding eigenvalue on $S^2V$, named by the Hecke
  relation. This is genuinely categorical and worth saying.
- **Archimedean level.** $q_0 \approx 1.10998$ is a number. It is CAL-2.

Reading $q$ off the braiding fixes the parameter's *role*, not its magnitude —
because **the braiding is assumed data**. A braided monoidal category comes
equipped with a braiding; different braidings give different eigenvalues, and
nothing upstream selects one. So "extracted from the monoidal structure" is the
same move #5044 made: denying assumption for something that is part of the
assumed data.

## Scope, and what this is not

**Scope-(a).** The categorical identification is real and is kept: the parameter
in the macroscopic fluid PDE *is* the microscopic braiding eigenvalue, so the two
descriptions share one parameter rather than two. That is a structural statement
about which quantity appears where. What is removed is the claim that this
settles the quantity's *value*.

This is **not** a claim that $q_0$ cannot be derived — only that it is not
derived here, and that the corpus says it is calibrated. Note separately that
substrate-$q_0$ derivation is under a permanent owner gate (2026-08-02,
`qou-eic1`); a block advertising a *"rigorous proof"* of it as a novelty was
advertising the one result agents are forbidden to pursue.

## Fixed

Both blocks rewritten to carry the fibre/archimedean split explicitly.

## Not checked

- `differential-structures-intro`: *"None of these structures are imposed
  externally; each is forced by the QOU axioms"* — a sweeping claim over four
  constructions. Each would need checking separately; not done.
- The two $q$-dilogarithm blocks claiming it is *"forced by the monoidal axioms"*
  / *"not imported into the framework"*. Plausible (pentagon coherence is a real
  constraint) but the same parameter-vs-value question applies, and being *a*
  solution of the pentagon is weaker than being *the* one.
- All 55 tier-3 rows, and the 74 tier-2 rows outside the foundational chapters.

## Second pass: the two claims left unchecked above

Both were named as "not checked" when this doc first landed. Both have now been
read.

**The $q$-dilogarithm pair — earned, not a defect.** The claim *"not imported
into the framework; forced by the monoidal axioms"* rests on a uniqueness step,
and the uniqueness is real: `def:q-dilogarithm` states $\mathrm{Li}_2^q$ is *"the
unique level-2 primitive normalised by the pentagon relation"*. So the pentagon
**names** the object rather than merely admitting it, and "forced" is the right
word. The block also self-hedges precisely where it should — *"it does not, by
itself, determine the analytic monodromy datum … that datum is genuinely
resurgent and remains open"*. This is what an earned contrastive claim looks
like, and it is worth recording as the positive control for the `qou-vud6`
checker.

One stray error fixed: the block said *"Because $\mathbf{C}$ is **rigid**
monoidal, its associator satisfies the Mac Lane pentagon coherence."* Pentagon
coherence is a **monoidal** axiom; rigidity is irrelevant to it. One word,
no claim changed.

**A consequence of #5021 nobody swept for.** Moving rigidity from
`def:quantum-universe` to `def:quantum-observable-universe` made every block
asserting "$\mathbf{C}$ is rigid" a QOU-level statement. Five blocks do:

| block | verdict |
|---|---|
| `hadron-operations-closure` | fine — own hypothesis, knot closure needs duals |
| `categorical-linking-operation` | fine — own hypothesis, and it already scopes properties 1–3 vs 4–5 |
| `categorical-neutrality-saturated-shells` | fine — own hypothesis |
| `q-dilogarithm-pentagon-associator` | **fixed** — pentagon is monoidal, not rigid |
| `frobenius-hopf-substrate` | **beaned `qou-t7mt`** — see below |

`frobenius-hopf-substrate` opens "Let $\mathbf{C}$ be a rigid monoidal category"
and phrases non-degeneracy as *"the induced map $A \to A^\vee$ is an
isomorphism"*, which presupposes $A^\vee$. Its own Lean encoding needs no such
thing: `FrobeniusHopfData` is declared over `[MonoidalCategory C]` alone and
builds the self-duality from `coevaluation` plus the snake identities. That is
exactly why axiom 3 could stay at QU level after #5021 — the traces come from
$A$'s own form, not from ambient duals.

Not fixed unilaterally: rewording a definition's axioms changes what the
definition says, and downstream blocks cite it. The prose is not wrong, only
stronger than needed. Options are recorded on the bean for the author.

## This is a recurring class, not a new one

Surfaced during the prepare-merge reuse pass:
[`2026-05-02-alpha-fit-NOT-derivation-retraction.md`](2026-05-02-alpha-fit-NOT-derivation-retraction.md)
is the same defect, three months earlier — an agent called
$\alpha \approx 82 \cdot E_0$ a *"structural binding formula"* and later
retracted it as fitting rather than categorical derivation.

So the corpus has now produced at least four instances of one shape:

| when | claim | actually |
|---|---|---|
| 2026-05-02 | $\alpha \approx 82 E_0$ a "structural binding formula" | a fit |
| 2026-08-14 (#5044) | pairwise result "forced by the braiding rather than assumed" | the hexagon is an axiom |
| 2026-08-15 (this doc) | $q$ "precisely and completely constrained" by the braiding | $q_0$ is CAL-2 |
| 2026-08-15 (this doc) | "Because $\mathbf{C}$ is **rigid** monoidal, its associator …" | pentagon is a *monoidal* axiom |

That frequency is the argument for the `qou-vud6` checker existing at all. Three
of the four were caught by a reader rather than by tooling, and the fourth was
caught only because the reader's question prompted a scan.

## Method note carried forward

`differential-structures-intro`'s *"None of these structures are imposed
externally; each is forced by the QOU axioms"* remains unchecked — it is a
sweeping claim over four separate constructions and each needs its own reading.
