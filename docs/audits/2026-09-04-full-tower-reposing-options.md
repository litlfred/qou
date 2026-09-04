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

- **Wenzl levels are alternatives, not stages.** One fibre occupies one level
  (`su5-hypercharge-n3-gate`). Higher `n` does not stack representations onto
  the ones you had.
- **`dim V = 2` is invariant along the single-fibre tower.** The obstruction to a
  three-dimensional flavour object does not dissolve at large `n`.
- **The vanishing lemma says exactly which blocks exist:**
  `s_λ = 0 ⟺ ℓ(λ) > r` (`QOU.QBeta.WenzlWeight.schurPrincipal_eq_zero_iff`,
  sorry-free). For a rank-2 fibre, every partition with more than two rows has
  **zero** multiplicity.

That last point has a consequence worth stating plainly, because it disposes of
one natural reading of the ruling: **"carry the complete Frobenius pairing over
all partitions" is, for a rank-2 fibre, already satisfied.** The partitions not
being summed carry zero weight. Summing over them adds nothing. Whatever force
the ruling has, it is not there.

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
not fusion rules, so re-fibring cannot supply the missing flavour object. The
eightfold needs a category with `Λ³W ≠ 0`, and axiom 5 (`Λ²V ≅ 𝟙`) forbids it for
the fundamental. Either add a second fundamental object that is not a summand of
`V^{⊗n}`, or relax axiom 5.

**What it costs.** The largest item here by an order of magnitude. It is a change
to the framework's definition, with a blast radius across every result that
depends on axiom 5.

**What it risks.** Everything downstream of axiom 5 needs re-verification. A
relaxed axiom may admit objects that break results currently proved.

**What it commits to.** Unblocks rows 12–14 (nine of the twenty-six parameters,
counting CKM and PMNS entries) and is the only route that does. **This is an
owner-level question about the definition of the framework, not an agent
decision.**

### Option D — Systematic Habiro re-posing

**What it means.** Replace, across all fourteen, the question *"find a real
`f(q₀)` matching the anchor"* with *"find a Habiro-ring element whose archimedean
evaluation at q₀ reproduces it"*. AGENTS.md's fibre-versus-observable banner
already says the first question is known to fail and the second is the right one.

**What it costs.** Moderate and spread thin — a re-framing of fourteen bean
bodies plus the probes that follow from them.

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
5. **C should not be started by an agent.** It changes an axiom.

**What would change this recommendation.** If `qou-lxh5` turns out to require the
flavour object it is meant to probe — i.e. if the r = 3 fibre cannot be
constructed without assuming what C would supply — then A collapses into C and
the ordering above is wrong. I have not established that it does not.

## 6. What this paper does not claim

It does not claim the tower reading is *wrong*, only that one natural reading of
it (sum over all partitions) is already satisfied and another (climb to higher
`n`) is blocked by proved results. It does not claim `qou-lxh5` will pass. And it
does not settle whether any of the fourteen is closeable at all — §5 of the
2026-09-03 status audit still reads *zero derived to experimental precision*, and
nothing here changes that.
