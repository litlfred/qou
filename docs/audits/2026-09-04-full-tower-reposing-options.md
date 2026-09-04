# Re-posing the 14 SM per-term attacks on the full tower — options for review

**Status:** decision paper, written for the owner. Nothing here is wired, and no
option has been executed. Prepared 2026-09-04 on the owner's request for
"pros/cons/recommendations for thoughtful review".

**The ruling this responds to** (2026-09-03, verbatim): *"The QOU should be on the
full tower in the derivations to the standard model — should make use of the full
tower even though what is observable is only order zero."* Confirmed the same day
to mean **both** all *n* of the Hecke tower **and** all orders in *q*.

---

## 1. The finding that should shape the decision

**Eleven of the fourteen open terms already name their own full-tower
formulation.** This is not a search for an approach; it is a build order.

Read the `tower status` line on each `sm-26` bean and the pattern is consistent:
the bean says what the tower-level object *would be*, and then says it is
unattempted. `qou-qneo` names the coloured Jones as a Markov trace over all
partitions. `tqcp` names bar-parity of the full colour-sector Markov trace.
`qou-ha6c` names keeping the bar-odd `sinh` channel inside
`tr_M = Σ_λ y_λ χ_λ` rather than letting the canonical projection discard it.
`qou-5iaz` goes furthest: it names a **test that already exists** (`qou-lxh5`).

The three that name nothing — CKM (`qou-pj82`), PMNS (`qou-y0mq`), and
`m_b`/`m_t` (`qou-b1k4`) — share one blocker, the three-dimensional flavour
object (cheat-sheet 4-A). They are not fourteen separate problems.

## 2. "Climb the tower" is the wrong picture, and this is proved

The intuitive reading of the ruling — take the same fibre and go to higher `n` —
is blocked by results already in the corpus, and understanding why redirects the
whole option space.

- **Wenzl levels are alternatives, not stages.** The block
  `rem:su5-hypercharge-n3-gate` *argues* this — it is a `remark` with no `.lean`
  sibling, so it proves nothing itself. Its argument has two inputs: the
  sorry-free `ocneanu_param_eq_of_fibre_qdim` (a fibre of quantum dimension
  `[N]_q` forces `z·[N]_q = q^N`, generic `[CommRing R] [IsDomain R]`, general
  `N`), plus the observation that production carries a single `z`. One fibre
  occupies one level; the framework does not pass *through* `r = 3` on its way
  to `r = 5`.
- **`dim V = 2` is an INPUT, not a theorem, and the row cap it induces is the
  obstruction.** It is re-sourced to axiom 5 under the *iso* reading, by
  `exteriorSquareDim_eq_one_iff` (`VolumeConstraintForcesFibreTwo.lean`,
  sorry-free) — and that file records that the *weak* reading forces only
  `N ≥ 2`, exhibiting `N = 3` surviving it. The obstruction itself is
  `weyl_dim_alt_eq_zero_iff` (`RowCapObstruction.lean`, sorry-free). Higher `n`
  does not relax it.
- **The >2-row blocks carry zero WEIGHT, and the restriction is an identity.**
  `TwoRowCapDerived.lean` (sorry-free) proves `traceSum_eq_twoRow_of_wenzl` —
  restricting `Σ_μ y_μ χ_μ` to `ℓ(μ) ≤ 2` is an identity for **arbitrary** `χ`,
  at every `n` — together with `bindingSum_eq_twoRow_of_wenzl` (arbitrary `Δ`,
  every `A`), `threeRowPart_eq_zero_of_wenzl` (the residual share is `0`, not
  "small") and `twoRow_share_eq_one_of_wenzl`. Non-vacuity is proved too
  (`exists_three_row_diagram`, `two_one_survives_filter`), so the filter is
  neither empty nor everything.

That last point disposes of one natural reading of the ruling: **"carry the
complete Frobenius pairing over all partitions" is, for a rank-2 fibre, already
satisfied — as a proved identity, at every `n`, for arbitrary summands.** The
partitions not being summed carry zero weight. Summing over them adds nothing.
Whatever force the ruling has, it is not there.

**One conditionality, carried deliberately.** The bridge from that hook-content
formula to the *actual* Markov weight is Wenzl 1988 (Invent. Math. 92, 349–383),
held in the corpus as `class IsOcneanuWeightSystem` with **zero instances**.
That is a citation, not a gap — but `TwoRowCapDerived`'s own header warns that an
axiom-clean `#print axioms` does **not** certify the identification, and the
paper it cites is **not ingested in `library/`**, so it cannot be checked from
the corpus. One independent corroboration exists inside the corpus:
`moment_and_schur_routes_agree_of_wenzl` reaches the same three-row zero at
`n = 3` via the Markov moment equations without Wenzl.

A note on what NOT to cite here. An earlier draft of this paper routed the
argument through `schurPrincipal_eq_zero_iff` and called it a statement about
**multiplicity**. It is not — it is `s_λ(1, Q, …, Q^{r−1}) = 0 ⟺ r < ℓ(λ)`, a
statement about the *weight*. The object-level general-`n` split is **not
formalised anywhere**: `RowCapObstruction`'s header says it is proved at `n = 3`
only, the general identity being Worpitzky's. The weight route above is both
correct and stronger.

**The picture that survives is different and more interesting: you do not climb
the tower, you choose a different fibre.** `qou-lxh5` sets this out as a proved
chain rather than an ansatz —

    colour antisymmetry needs a three-row block   (FibreDimensionForcesTL.lean)
      ⇒ r ≥ 3                                     (schurPrincipal_eq_zero_iff, sorry-free)
      ⇒ a fibre of quantum dimension [3]_q
      ⇒ z is DETERMINED, not free                 (ocneanu_param_eq_of_fibre_qdim, sorry-free)
        z₃ = q⁵/(q⁴ + q² + 1) = 0.4493048091 at the proton pin

— and that determined `z` is what makes the resulting test parameter-free.

## 3. The fourteen terms, characterised

| # | term | bean | tower status | what its full-tower form would be |
|---|---|---|---|---|
| 1 | α_s | `qou-5iaz` | order-zero | level-3 Markov trace over three-row blocks — **test exists** (`qou-lxh5`) |
| 2 | m_s, m_c | `qou-qneo` | order-zero | coloured Jones as `tr_M` over all partitions — unattempted |
| 3 | θ_QCD | `tqcp` | order-zero | bar-parity of the full colour-sector Markov trace — not formulated |
| 4 | m_u, m_d | `qou-ha6c` | order-zero | keep the bar-odd `sinh` channel inside `tr_M` — not formulated |
| 5 | ν masses (3) | `qou-qydm` | order-zero | per-braid q-volume / Habiro tail of the unknot — none formulated |
| 6 | m_τ | `qou-pvu4` | mixed | ℓ-branching `e→(3,1,1)`, `μ→(3,2)`, `τ = ℓ=3` — **scaffold exists**, no instance |
| 7 | 3 generations | `qou-x4qm` | mixed | same ℓ-degree branching — **same scaffold**, no instance |
| 8 | α_EM | `qou-rgiz` | mixed | CS resummation `1/(1 − δκ)` is all-orders; κ conjectural |
| 9 | m_H | `qou-pgzo` | mixed | RT at a root of unity is fibre-level; level unselected, mass map absent |
| 10 | sin²θ_W | `qou-h72x` | order-zero | none formulated (one Hecke block's eigenvalue ratio at q₀) |
| 11 | v (EW scale) | `qou-z3x8` | order-zero | none formulated (crossing count × single-crossing energy) |
| 12 | m_b, m_t | `qou-b1k4` | **no attack** | must be a tower object by construction (order-zero volume ≡ 0 on the carrier) |
| 13 | CKM (4) | `qou-pj82` | **no attack** | an operator on flavour Wedderburn blocks, not a number at q₀ |
| 14 | PMNS (4) | `qou-y0mq` | **no attack** | needs the neutrino to be a non-trivial tower object at all |

Two structural observations from the table. **Rows 6 and 7 share one scaffold**
(`S5SO3FiberAction.lean`) — one instance would move two terms. **Rows 12–14 share
one blocker** (4-A), and row 1's test probes exactly that blocker's successor
question.

---

## 4. The options

### Option A — Run `qou-lxh5` first

**What it means.** Build the level-3 (SU(3)) channel and test it against a colour
observable at the three existing calibrations. PASS/FAIL.

**What it costs.** One compute unit. The chain above is already proved, so no new
mathematics is required to *pose* it; the work is constructing the r = 3 fibre's
Markov trace and evaluating it.

**What it risks.** A FAIL is informative and cheap. The real risk is a
*near*-miss, which under the anti-fit discipline must be reported as a near-match
and not wired — the corpus has a documented history of near-matches becoming
fits.

**What it commits to.** Nothing structural. It is a test, not an adoption.

**Why it is different from every other option:** `z` is **determined** by a
sorry-free lemma, so the test has **no free parameter**. That is rare here and it
is what makes the result meaningful in either direction.

### Option B — Instantiate the `S5SO3FiberAction` scaffold

**What it means.** The ℓ-degree branching (`e` ℓ=1, `μ` ℓ=2, `τ` ℓ=3) exists in
Lean as a scaffold with no instance. Give it one.

**What it costs.** Real mathematics, not typing — the scaffold has no instance
*because* the construction is open, not because nobody typed it.

**What it risks.** The §"Axiomatization is NOT a Proof" trap in its purest form.
Fabricating an instance to make downstream conditionals fire would be laundering.
If the construction does not close, the honest outcome is that it stays open.

**What it commits to.** Two terms at once (m_τ and three-generations), which is
the best ratio on the table.

### Option C — Attack 4-A: a second fundamental object, or relax axiom 5

**What it means.** PR #6458 established that a fibre functor changes dimensions,
not fusion rules (Bichon 2003), so re-fibring cannot supply the missing flavour
object — the invariant is Clebsch–Gordan parity of `Rep(SL_q(2))`, preserved by
every monoidal functor, and the carriers are sorry-free
(`FibreFunctorDimensionNotCategorical.lean`, 12 declarations). The eightfold
needs a category with `Λ³W ≠ 0`. The disjunction is stated verbatim in that
audit: *either a different fundamental object* (not a summand of `V^{⊗n}`) *or a
category not generated by one object satisfying axiom 5*. Bean `qou-dwsh`
(completed 2026-08-03) reached the same specification independently, by a
different route.

**What it costs — and this is the part an earlier draft of this paper got
wrong.** Axiom 5 as *written* in `def:quantum-observable-universe` says
**"non-degenerate epimorphism"**, not "iso". Only the **iso** reading forces
`N = 2`; the epi reading admits `N = 3`, and `weak_volume_reading_admits_three`
(sorry-free) exhibits it. So "relax axiom 5" may not be an axiom change at all —
it may be a **reading selection between two documented alternatives** on an
ambiguous phrase. `VolumeConstraintForcesFibreTwo.lean` calls the choice *"an
editorial question this file cannot settle"*.

**What it risks — split the blast radius, because the two halves differ by
everything.** On the **formal** side it is currently **zero**: the formalised
axiom-5 condition is two free fields that `volumeForm := 0` inhabits, so, in that
file's own words, *"the formalised condition (v) constrains nothing whatever."*
Nothing depends on it because there is nothing to depend on. On the **prose**
side the radius is real and **unmeasured** — every argument in the paper that
leans on the iso reading would need re-reading.

**What it commits to.** Unblocks rows 12–14 (nine of the twenty-six parameters,
counting CKM and PMNS entries) and is the only route that does.

**Still an owner decision — but for a different reason than the earlier draft
gave.** That draft said an agent must not start C *because it changes an axiom*.
If it is a reading selection, that reasoning does not hold. What survives is
better: it is an **editorial question about the author's intent** in a definition
the author wrote, and the formal side gives no evidence either way because it
constrains nothing. That is squarely yours, and it may be considerably cheaper
than the earlier pricing implied.

### Option D — Systematic Habiro re-posing

**What it means.** Replace, across all fourteen, the question *"find a real
`f(q₀)` matching the anchor"* with *"find a Habiro-ring element whose archimedean
evaluation at q₀ reproduces it"*. AGENTS.md's fibre-versus-observable banner
already says the first question is known to fail and the second is the right one.

**What it costs.** Moderate and spread thin — a re-framing of fourteen bean
bodies plus the probes that follow from them.

**Better motivated than an earlier draft argued.** That draft called the Habiro
route "one of the two non-order-zero attacks", which both overstates and
understates it. It is not an attack, it is a **vocabulary** — and the corpus
already reaches for it independently in **three** rows: inside α_EM
(`[2]_q(1 − h²α)` is fibre-level, `qou-rgiz`), as the named tower-form of the
neutrino masses (the Habiro tail of the unknot, `qou-qydm`) and of θ_QCD (the
bar involution is fibre-level, `tqcp`). Three separate terms reaching for the
same vocabulary unprompted is the argument for applying it uniformly.

**What it risks.** It addresses "all orders in q" and **not** "all n". Presenting
it as satisfying the ruling would overstate it.

**What it commits to.** A vocabulary the corpus already uses for α_EM and the
`c_k` ladder, applied uniformly.

### Option E — Do nothing structural; keep the annotation discipline

**What it means.** Every per-term bean already carries a tower-status line, and
the rule that an order-zero residual is not evidence about the tower is recorded
in four places.

**What it costs.** Nothing; it is already done.

**What it risks.** Nothing — but it advances no derivation.

**This is the default.** If you say nothing, this is what happens, and it is a
defensible resting state rather than a failure.

---

## 5. Recommendation

**Run Option A now, then Option B, and put Option C to yourself as a separate
decision when A reports.** My reasoning, offered as judgement rather than
finding:

1. **A is the only parameter-free falsifiable test on the table.** Its `z` is
   determined by a sorry-free lemma. In a corpus whose recurring failure mode is
   the near-match that becomes a fit, a test with no free parameter is worth more
   than its cost regardless of outcome.
2. **A and C are the same question at different scales.** A probes the r = 3
   fibre; C asks whether the framework should admit one as a second fundamental
   object. A FAIL on A is real evidence about C, obtained cheaply.
3. **B has the best terms-per-unit-effort ratio** (two terms, one instance) and
   is independent of A, so it can run in parallel.
4. **D is cheap but should not be sold as satisfying the ruling.** It closes the
   "all orders in q" half only. Worth doing as hygiene, not as an answer.
5. **C should not be started by an agent — but not for the reason I first
   gave.** I wrote "it changes an axiom". Measured, it may not: axiom 5 says
   *non-degenerate epimorphism*, and only the iso reading forces `N = 2`, so C
   may be a **reading selection** whose formal blast radius is currently zero
   (the formalised condition is inhabited by `volumeForm := 0` and constrains
   nothing). What survives is a better reason and a cheaper option: it is an
   **editorial question about your own intent** in a definition you wrote, on
   which the formalisation offers no evidence either way. That is yours to
   settle, and settling it may be much less work than the first pricing
   suggested.

**What would change this recommendation.** If `qou-lxh5` turns out to require the
flavour object it is meant to probe — i.e. if the r = 3 fibre cannot be
constructed without assuming what C would supply — then A collapses into C and
the ordering above is wrong. I have not established that it does not.

## 6. A prior full-tower attempt exists — cite it, do not re-derive it

**`qou-tower`** (PR #6333, in-progress, ~630 lines) is the only place the corpus
has actually **carried the tower intact and measured**. It is the nuclear /
magic-number arc, not the SM, so it does not close any of the fourteen — but four
of its findings bear directly on the options above.

1. **It ran the full `H_{3A}` tower walk exhaustively at A = 2, 3, 4** — a real
   `d_λ × d_λ` matrix per `λ ⊢ 3A`, **no per-step Gröbner–Shirshov reduction**,
   generators at true strand positions, every `Z ∈ 0..A`. Result: **no
   separation** on top-block share, participation ratio, rank or argmax.
2. **It ran the symbolic q-degree grading at A = 2..20**, exact over ℚ, reaching
   Z = 2, 8, 20. Result: `interleaved` at every level, every observable.
3. **It retracted its own headline on owner correction.** *"The `H_{3A}`
   structure is destroyed as it is built"* is **wrong**: the GS reduction
   *digests* entanglement into coefficients, and the surviving q-degree grading
   **is** the many-body decomposition. This is the corpus's own worked example of
   mistaking a collapsed **evaluation** for a collapsed **object** — which is
   precisely the error this paper is trying not to make about the tower.
4. **It retracted a compute wall, and the retracted number is the one not to
   repeat.** *"A = 4 is the end of the road; A = 5 needs 686 GB"* was `max_λ d_λ²`
   — a property of the chosen representation, not of the problem. The symbolic
   normal form is **6 coefficients for any nucleus at any A**; only the
   polynomial degree grows. **Any full-tower option priced on compute should use
   this, not the 686 GB.**

It also logs **eight control failures**, mostly parity artifacts and
input-presented-as-output. Option A's near-miss paragraph above is understated
relative to that record.

**Option E has already executed.** The annotation pass is `qou-bsu0`, done
2026-09-03: fourteen beans, every one carrying a tower-status line. It is not a
proposal on this table; it is the current state.

## 7. Two claims this paper previously made that were wrong

Recorded rather than silently fixed, because both were load-bearing and both
came from inheriting a sentence rather than checking it.

- **"`su5-hypercharge-n3-gate` *proves* levels are alternatives."** It is a
  `remark` with no `.lean` sibling; it *argues* from one sorry-free lemma plus a
  codebase observation. The block already carries a 2026-08-25 `authorNotes`
  caveat recording that **its own first merged version over-claimed in exactly
  this direction** and was retracted for restating a conditional's hypothesis as
  fact. Writing "proves" would have been the third pass of the same error on the
  same block.
- **"`dim V = 2` is invariant along the single-fibre tower."** Not a corpus
  result. The phrase occurs in exactly three files and they are **one chain** —
  §10 of the 2026-09-03 status audit, the chip-away ledger quoting it, and this
  paper quoting that. It is also near-vacuous as stated: `V` is fixed by
  construction and `n` is the tower index. The load-bearing facts are the row-cap
  obstruction and the alternatives-not-stages argument, not an invariance.

A third, smaller: §10 of the status audit places the Habiro route and the Magnus
hook-slice among "the attacks in §§2–7". Neither is discussed in §§2–7 — "Habiro"
appears in that document only inside §10 itself. The Magnus hook-slice
(`qou-o6ov`) is on the Δ_λ / binding arc and is **not** one of the twenty-six
parameters at all.

## 8. What this paper does not claim

It does not claim the tower reading is *wrong*, only that one natural reading of
it (sum over all partitions) is already satisfied and another (climb to higher
`n`) is blocked by proved results. It does not claim `qou-lxh5` will pass. And it
does not settle whether any of the fourteen is closeable at all — §5 of the
2026-09-03 status audit still reads *zero derived to experimental precision*, and
nothing here changes that.
