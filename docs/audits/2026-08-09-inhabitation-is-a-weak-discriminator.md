# Inhabitation is a weak discriminator — and three `class` names are overloaded

**Date:** 2026-08-09
**Branch:** `claude/issue-2472-analysis-qgqk7u`
**Scope:** the 13 `field-projection` candidates; `docs/audits/lean-vacuity-review-ledger.json`

## The queue is drained

`--check-ledger` **exits 0** for the first time in this campaign. 141 entries:
**124 genuine, 9 legit, 8 advisory, 0 `needs-agent`** (was 122 `needs-agent` at
the start of this session).

## The discriminator the campaign was using does not hold up

PR #4882 split the 92 self-assuming projections on **carrier inhabitation** —
*"a bundle-plus-accessor is the ordinary Mathlib idiom, provided something
builds the bundle"* — marking the 68 never-inhabited carriers `genuine` and
leaving the 23 inhabited ones open on the grounds that inhabitation is
*"necessary, not sufficient"*. That caution was right, and the margin is wider
than expected. Of the 12 remaining inhabited-or-unknown projections, **only two
survive**:

| decl | carrier | instance | verdict |
|---|---|---|---|
| `saddle_eq_volume` | `VolumeConjecture41` | `⟨tendsto_log_kashaev_vol⟩` — proved via bricks E1–E5d | **legit** |
| `beta3_via_class` | `TheoremA` | `value_at_4 := beta3_from_jonquiere` — a real derivation | **legit** |
| `he4_strong_duality_value` | `HasHe4ChannelActiveSet` | 11 numeric literals from a witness JSON, fields by `norm_num` | **advisory** |
| `convergence_bound` | `ConvergenceBound` | `convergenceBound_refl … f f` — **the diagonal** | genuine |
| `knot_invariant_convergence` | `KnotInvariantConvergence` | `…_refl … a a` — **the diagonal** | genuine |
| `strong_duality` | `HasStrongDuality` | `instHasStrongDualityEmpty` — **`Empty` constraint index** | genuine |
| `rogers_correction_leading_h_order` | `RogersCorrectionLeadingOrderH4` | `leading_h_order := 4; … := rfl` — **stipulates the answer** | genuine |
| `ReebBundleComplementEqualsVolume` | `MassVolumeFactorization` (Reeb) | **none** | genuine |
| `categorical_irreducible` | `HasCategoricalIrreducibility` | **none** | genuine |
| `rho_eq_qdim_via_canonical_knot` | `RhoPrefactorStructural` | **none** | genuine |
| `q_beta_spectral_conditional` | `BorromeanQuark` (q-beta) | **none** | genuine |
| `wedderburn_weight_perturbation` | Pattern-4 `bound` class | conclusion-as-field | genuine |
| `adjoint_vanishing_propagation` | explicit `jgcs` argument, `k` unused | — | genuine |

So the useful test is not *"is the carrier inhabited?"* but **"is the instance
non-degenerate?"** Four distinct degeneracies appear, and each satisfies
inhabitation on a technicality:

1. **The reflexive diagonal.** `convergenceBound_refl … f f` inhabits
   `|f − f| ≤ C_q/(k−3)`. True, and says nothing about convergence.
2. **The trivial index.** `instHasStrongDualityEmpty` inhabits strong duality
   only for `SDPPrimal n R Empty` — the no-constraints case.
3. **The stipulated constant.** `RogersCorrectionLeadingOrderH4` sets
   `leading_h_order := 4` and discharges `leading_h_order_eq_four` by `rfl`, so
   `c.leading_h_order = 4` is circular. The file concedes the real theorem
   (Pentagon → −3/4) is *"structurally open"* two lines below.
4. **The zero model.** `MassVolumeFactorization.canonical K 0` sets
   `volume := 0`, `mass := 0`, and closes `factorization` by `mul_zero` — its
   docstring says it exists to *"discharge §3b-cond"*.

Recommendation: extend the scanner's inhabitation check to flag these four
shapes, rather than counting any instance as rescue. A reflexive instance whose
arguments are syntactically identical (`… f f`), an instance at `Empty`/`0`, and
an instance whose field proof is `rfl` against a value the same instance sets
are all mechanically detectable.

## Three `class` names are overloaded, and the collision is load-bearing

AGENTS.md §"conditional-proved ≠ premise-established" item 4 warns that
*attributes do not transfer across overloaded symbols*. Two of the 13 hit it,
and in both cases the wrong reading flips the verdict:

- **`MassVolumeFactorization`** — `mass-theory/mass-volume-factorization.lean:127`
  takes `(K : Type*) (n : ℕ)` with fields `density`/`volume`/`mass`/`factorization`
  and **has** an instance (the degenerate `canonical K 0`).
  `lean/QOU/BraidsKnots/ReebBundleComplementEqualsVolume.lean:31` takes no
  parameters and has fields `markov_trace`/`jsj_volume_sum`/`factorization_identity`
  — and has **none**. `ReebBundleComplementEqualsVolume` projects the second.
  Reading the grep hit for the first would have scored it "inhabited".
- **`BorromeanQuark`** — at least three distinct classes. The two instances in the
  corpus (`observations/borromean-quark.lean:120`,
  `lean/QOU/Archimedean/BorromeanQuark.lean:124`) inhabit the `orbitalDim`
  variant. `q_beta_spectral_conditional` projects a *third*, declared locally in
  `q-beta-spectral-bridge.lean:279` with fields `Q_beta_A`/`Q_beta_B`/`forms_agree`,
  which has no instance.

Any future inhabitation sweep must resolve the class by **declaration site**, not
by name. A name-keyed scan over-reports inhabitation exactly where the projection
is emptiest.

## Two shapes worth singling out

**`fiber_adjoint_involution_exists` is an audit-dodge (§1a).** Its docstring
promises the opposite of what it does — *"not the degenerate `∃ inv, True`"* and
*"the body is an honest `sorry`"* — while the body ships
`⟨{ adjointObj := 𝟙_ C, projLine := 𝟙_ C, orbit_embed := 𝟙 _, involution := 𝟙 _, … }⟩`.
Every field is the identity on the monoidal unit, all conditions hold trivially,
and `fh` is never used, so `Nonempty (FiberAdjointInvolution C fh)` is proved for
every category and every Frobenius–Hopf datum. It reaches the degeneracy the
docstring disclaims by a route the docstring did not anticipate. The honest
`sorry` should be restored — the docstring already explains why it was there.

**`q_beta_spectral_conditional` answers the wrong objection.** Its docstring
defends the projection as *"Derived from the class field `forms_agree` — not a
`sorry`-projection of an unrelated conclusion."* The §3b-cond item-5 complaint is
not that the conclusion is unrelated but that it is **identical**: the class field
*is* `Q_beta_A = Q_beta_B`, so the theorem derives nothing. The class itself is
honest (content-bearing, uninhabited — the correct open state per §3b-tax); only
the wrapper is the defect.

## Repairs applied, and one repair *not* applied

**`fiber_adjoint_involution_exists` — fixed.** The all-identities witness is
gone. The conclusion now pins `∃ inv, inv.adjointObj = fh.obj` — the adjoint
bundle is carried by the algebra object `A` — which the identity-on-`𝟙_ C`
witness cannot satisfy, and the body is the honest `sorry` + `-- Ref:` the
docstring always claimed it was. `lean`-direct exit 0 with the expected
`declaration uses 'sorry'`. Note that a bare `sorry` alone would not have been
enough: the *statement* was also too weak, so queueing it unchanged would have
queued a claim the unit object already satisfies.

**`su3_sym2_irreducible` — deliberately NOT repaired, and an earlier verdict of
mine corrected.** I first marked it `genuine` with disposition *"state the
actual proposition"*, having read the declaration but not the module header.
The header already carries a section titled *"Outstanding: this file's
representation-theoretic content is vacuous"*, naming this axiom and both gate
theorems, assigning the repair to bean `qou-8fl1` item 3, and noting the chapter
prose labels the result honestly. More important: the repair I was about to
write — singlet in `Sym²` ⇒ `V` self-dual ⇒ not the SU(3) fundamental — is
**refuted**. `QOU.Eightfold.Sym2GateParity` proves
`self_duality_does_not_decide_gate`, states *"That inference is invalid"*, and
is written so that *"the invalid inference cannot be re-derived from this
file."* The correct criterion there is parity (`gate_fails_iff_odd_dim`), all
`by decide`.

Re-verdicted `advisory` / `defer-to-bean-qou-8fl1-do-not-re-derive`. This is the
corpus-grep discipline earning its keep in the forward direction: the file that
looked most in need of repair was the one where repairing it would have
reintroduced a refuted argument.

## A detector gap found by reading, then closed

`octonion_3_passes_sym2_gate : (6 : ℕ) = 6 ∧ (0 : ℕ) = 0` — two tautologies
presented as a gate result — was flagged by **nothing**. The reflexive tests read
the conclusion as a single proposition, so the `^([^=]+?)=([^=].*)$` match splits
it as lhs `(6:ℕ)` against rhs `6∧(0:ℕ)=0` and finds no reflexivity.

Added a `conjunction-of-tautologies` arm: split the conclusion on top-level `∧`
(bracket-aware) and flag only when **every** conjunct is `True`, reflexive, or
reflexive-behind-an-ascribed-literal. One real conjunct means the statement
asserts something, so its file-mate `corpus_T1_fails_sym2_gate`
(`1 + 5 = 6 ∧ 1 > 0` — arithmetic, not tautology) correctly stays unflagged.

Verified on a 4-declaration probe (both vacuous shapes fire, both negatives
quiet) and the corpus: **exactly one hit across 2765 files**, the declaration
above. No false positives.

Worth noting how this one surfaced: not from the scanner, but from reading a
file the scanner had sent me to for a *different* criterion. The high-recall
detectors find candidates; they do not bound what is there.

## What the drain does not do

Recording 124 `genuine` verdicts is triage, not repair. Five declarations have
been fixed so far. The dispositions are recorded per candidate in the ledger and
each still needs its restate/demote applied and `lean`-direct verification.
