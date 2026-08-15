# What do the Standard-Model and eightfold-way derivations actually give us?

**Date:** 2026-08-08
**Branch:** `claude/sm-eightfold-epistemic-audit-2026-08-08`
**Scope:** `content/quantum-observable-universe/eightfold-way/` (11 blocks) and
`content/quantum-observable-universe/appendix-standard-model/` (20 blocks),
both landed 2026-08-07.
**Mandate:** the owner asked directly — *"what does std model or 8-fold way
derivations give us?"* This is an epistemic accounting under the standing
[critical-distance license](../../AGENTS.md), not new mathematics. No content
was edited in this pass.

---

## Bottom line (read this and stop, if you only read one thing)

**The two chapters contribute one derived quantum-number entry, three proved
negative results, five self-withdrawn earlier over-claims, and a
well-organised catalogue of what is missing. That is the whole positive
yield. Everything else is either textbook representation theory correctly
applied, or open.**

Concretely, counting the eightfold chapter's own 23-row ledger
([`eightfold-open-problems.md:11-33`](../../content/quantum-observable-universe/eightfold-way/eightfold-open-problems.md)):

| Tier | Rows | Share |
|---|---|---|
| `derived` | **1** | 4 % |
| `proved` (Lean, sorry-free) | 3 | 13 % |
| `standard` (true of any `SU(3)`) | 8 | 35 % |
| `refuted` / `excluded` | 2 | 9 % |
| `open` | 9 | 39 % |

And the appendix's own headline count, which is accurate as written
([`sm-params-intro.md:5`](../../content/quantum-observable-universe/appendix-standard-model/sm-params-intro.md)):
of 26 Standard-Model parameters, **1 input + 1 proxy + 1 partial +
2 conjectural + 21 open**. Zero parameters are derived to experimental
precision.

Three structural facts sharpen this:

1. **The appendix contains no theorem.** Its 20 blocks are 1 chapter +
   4 `conjecture` + 2 `definition` + 10 `prose` + 3 `remark`. There is not a
   single `theorem`/`proposition`/`lemma`/`corollary` block in the entire
   Standard-Model appendix. This is *correct* under §3b conjectural
   propagation — and it is also the answer to the question: the appendix
   proves nothing about the Standard Model, and says so.
2. **All three "proved (Lean)" rows are arithmetic instances of standard
   facts.** Verified below: each reduces to `Nat`/`CommRing` arithmetic with
   the representation-theoretic content carried by `def` names and
   docstrings. They are correct and they are sorry-free; they are not
   representation theory.
3. **The one `derived` row is a two-point match**, and its only genuinely
   parameter-free ingredient (`c = 1/2`) was found *already in the corpus*
   (`def:coulomb-charge`), not produced by these chapters.

So: is the eightfold intro's self-assessment accurate? It claims the chapter
contributes *"the placement of the braid dictionary against that
classification, one derived entry ($I_3$ on the nucleon doublet), and a
sharpened statement of what is missing"*
([`eightfold-intro.md:74-80`](../../content/quantum-observable-universe/eightfold-way/eightfold-intro.md)).
**That is accurate, and if anything it is slightly generous to itself on
"derived" and slightly stingy on the negatives** — the three proved negatives
and five withdrawals are a larger contribution than the one derived entry,
and the intro does not count them. Net: **as claimed, with the balance
shifted toward the negative results.**

These are unusually honest chapters. The criticisms below are corrections at
the margin of an already self-audited pair of documents — not a teardown. The
one finding that matters materially is §5.1 (the twist battery).

---

## Verification performed

Everything below was checked, not summarised.

### Lean: 20 files, all green, all sorry-free, zero red

The 11 files the two chapters cite directly, plus the 9-module colour cone
(next subsection).

`scripts/lean-verify.sh` (never `lake build`), foreground, real exit codes
captured per file. Environment: `/usr/local/bin/lean`, toolchain `v4.24.0`,
6990 Mathlib oleans restored.

| File | Result | word-bounded `sorry` |
|---|---|---|
| `QOU/Eightfold/RowCapObstruction.lean` | ✓ exit 0 | 0 |
| `QOU/Eightfold/GellMannOkuboIdentity.lean` | ✓ exit 0 | 0 |
| `QOU/Eightfold/Sym2Gate.lean` | ✓ exit 0 | 0 |
| `QOU/Eightfold/Sym2GateParity.lean` | ✓ exit 0 | 0 |
| `QOU/Eightfold/WeylInvarianceQDeformation.lean` | ✓ exit 0 (1 deprecation warning) | 0 |
| `QOU/StandardModel/ColourStabilizerAction.lean` | ✓ exit 0 | 0 |
| `appendix-standard-model/gauge-action-groupoid.lean` | ✓ exit 0 | 0 |
| `appendix-standard-model/gauge-hecke-realization.lean` | ✓ exit 0 | 0 |
| `appendix-standard-model/sm-gauge-truncation.lean` | ✓ exit 0 | 0 |
| `appendix-standard-model/sm-hypercharge-invariant.lean` | ✓ exit 0 | 0 |
| `appendix-standard-model/strand-twist-datum.lean` | ✓ exit 0 | 0 |

The corpus-wide red-sweep warning
([`2026-08-08-library-lean-red-sweep-partial.md`](2026-08-08-library-lean-red-sweep-partial.md))
does **not** bite on the files these chapters cite: all eleven are green.
The `WeylInvarianceQDeformation` warning is only
`Mathlib.Algebra.GeomSum has been deprecated` — cosmetic.

> **Methodological note for future auditors: `grep -c sorry` is unusable in
> this corpus.** Raw `grep -c sorry` reports 1 hit in
> `strand-twist-datum.lean`, 2 in `OctonionSU3Stabilizer.lean`, 1 in
> `OctonionColourActionBaseModule.lean` — **every one of them is the phrase
> "sorry-free" in a docstring.** Word-bounded
> `grep -nE '(^|[^-[:alnum:]])sorry([^-[:alnum:]]|$)'` returns empty on all
> three. I briefly suspected an unproved colour claim on the raw count and
> retract that; the files are genuinely sorry-free.

### The colour-row cone: 9 more modules, all green

`QOU/MathlibExt/OctonionSU3BracketClosure.lean`,
`OctonionSU3Stabilizer.lean`, `OctonionColourActionBaseModule.lean` — the
Lean backing the colour row — initially returned `✗ FAILED` under
`lean-verify.sh`, but the diagnostic was a **missing intra-package olean
cascade** (`object file '…/QOU/MathlibExt/OctonionDerivationProperties.olean'
… does not exist`), an artifact of this worktree, **not** a proof error.

Rebuilt with the correct tool —
`scripts/lean-direct-cone.sh QOU.MathlibExt.OctonionColourActionBaseModule -k -j4`
— which confirms it: **`done: ok=9 in 923s`, `err=0`, `blocked=0`.** Every
module in the cone type-checks:

| Module | Status | Seconds |
|---|---|---|
| `QOU.MathlibExt.DerivationRankNullity` | ok | 6.0 |
| `QOU.MathlibExt.OctonionDerivations` | ok | 328.7 |
| `QOU.MathlibExt.OctonionDerivationProperties` | ok | 8.1 |
| `QOU.MathlibExt.OctonionDerivationsBound` | ok | 20.3 |
| `QOU.MathlibExt.OctonionDerivationsUpperBound` | ok | 554.3 |
| `QOU.MathlibExt.OctonionSU3Stabilizer` | ok | 7.1 |
| `QOU.StandardModel.ColourStabilizerAction` | ok | 2.2 |
| `QOU.MathlibExt.OctonionSU3BracketClosure` | ok | 3.3 |
| `QOU.MathlibExt.OctonionColourActionBaseModule` | ok | 3.0 |

**So the running total is 20 Lean files verified green and sorry-free, with
zero red.** The corpus red-sweep warning does not bite anywhere in these two
chapters' citation graph.

**Consequence for the colour row.** `sm-open-problems.md:12`'s substantive
claims — the proved `dim = 8` gate, bracket closure "sorry-free", the
faithful action on the octonion base module — are **accurate as stated**. The
only defect on that row is the citation-precision issue of §5.3 (the proofs
live in `QOU/MathlibExt/Octonion*`, not at the block's cited `lean.ref`), and
the row's own parenthetical "tautological instance" for the faithful action.
`OctonionDerivationsUpperBound` at 554 s is the cone's bottleneck, worth
noting for anyone re-running it.

### Numerics: independently reproduced, not read

- **Twist battery** (§5.1): reproduced from first principles in
  `python3`; matches
  [`computations/strand-twist-y-battery.witness.json`](../../computations/strand-twist-y-battery.witness.json)
  survivor-for-survivor.
- **`a5` branching table** (§4.3): re-derived by icosahedral character
  arithmetic, all six rows.
- **GMO algebra** (§3.2): hand-verified, `16a + 8c` both sides.

---

## 1. What is genuinely DERIVED?

**One item, and it is a two-point match.**

### 1.1 `Q = w/2` and the writhe → `I₃` map — the one derived entry

**Tier claimed:** `derived` (both chapters).
**Tier warranted:** *split* — the `c = 1/2` coupling is genuinely derived and
is the strongest single result in either chapter; the `I₃` *identification* is
a two-point sign-and-ratio match.

Evidence, from the authoritative source found by corpus-grep —
[`docs/audits/2026-06-02-u1-hypercharge-assignment.md`](2026-06-02-u1-hypercharge-assignment.md)
(PR #1683), whose own VERDICT is more careful than either chapter's prose:

- The per-crossing coupling `c` in the framing phase `q^{w·c}` is **not
  free**: it is `c = 1/2`, *structurally fixed* by the pre-existing
  `def:coulomb-charge` (`Q(H) = ½(n₊ − n₋) = writhe/2`). **This is real, and
  it is the audit's most positive finding.** The history is what makes it
  non-trivial: an earlier session had `c = 1` missing `(m_n − m_p)/m_p` by
  ~305×, and the author flagged tuning `c` as a FIT. `c = 1/2` was then found
  already in the corpus rather than fitted. That is the anti-fit discipline
  working as designed.
- With `c` fixed, *"the writhe ladder **matches I₃** … by sign+ratio across
  the nucleon doublet (p:+, n:−, scale-free)"*. Two states, one sign, one
  ratio.

**Finding 1 — the epistemic verb differs across the two chapters for the same
object.**

| Location | Wording |
|---|---|
| [`flavor-charge-assignments.md:13-18`](../../content/quantum-observable-universe/eightfold-way/flavor-charge-assignments.md) | "is **derived** in the framework without fitted parameters" |
| [`sm-lagrangian-selection-rules.md:5`](../../content/quantum-observable-universe/appendix-standard-model/sm-lagrangian-selection-rules.md) | "**matches** sign and ratio across the nucleon doublet scale-free" |
| [`dictionary-flavor-layer.md:50-52`](../../content/quantum-observable-universe/eightfold-way/dictionary-flavor-layer.md) | "the writhe difference **reproduces** `ΔI₃ = 1` scale-free — that entry is derived" |

"Matches on a two-element set" is what the evidence supports. `derived`
without qualification invites the reading that `I₃` is *output* by the braid
construction for general states, which the corpus does not claim.
Additionally `flavor-charge-assignments.md:13-18` states it with **no
pointer** — no Lean decl, no `prop:` ref, no witness — while every other
tier claim in the chapter cites one. (The claim is *not* absent from the
corpus; corpus-grep located it. The defect is citation, not substance.)

**Not a fit.** To be explicit, because it matters: nothing here was tuned to
data. `dictionary-flavor-layer.md:55-58` says so and is correct.

---

## 2. What is merely STANDARD?

**Roughly half of the substantive content, and the chapters say so.**

By the chapter's own ledger: 8 of 23 rows (35 %) are labelled `standard`. Add
the 3 `proved` rows — which §3 shows are arithmetic instances of standard
facts — and **≈ 48 % of the ledger is true of any `SU(3)`, any first-order
octet breaking, or any `ℕ`.**

Per-block, the standard content is:

| Block | Standard content | Chapter's own framing |
|---|---|---|
| [`a2-from-three-strands.md`](../../content/quantum-observable-universe/eightfold-way/a2-from-three-strands.md) | items 1–3: braid/Coxeter dictionary, `A₂` Cartan matrix, six roots | ":5-15 holds **by construction** … Nothing about the substrate is derived from it" — explicit |
| [`schur-weyl-eightfold.md`](../../content/quantum-observable-universe/eightfold-way/schur-weyl-eightfold.md) | quantum Schur–Weyl duality (Jimbo) | ":15 of the ledger — "the duality itself is not formalised" |
| [`meson-octet-decomposition.md`](../../content/quantum-observable-universe/eightfold-way/meson-octet-decomposition.md) | `3 ⊗ 3̄ = 8 ⊕ 1`, the full weight table | ":63 "is a theorem of `SU(3)` representation theory" |
| [`borromean-decuplet-derivation.md`](../../content/quantum-observable-universe/eightfold-way/borromean-decuplet-derivation.md) | the entire 10-row decuplet table | ":61-62 "a *matching of dimensions and weights*, not a derivation" |
| [`dictionary-flavor-layer.md`](../../content/quantum-observable-universe/eightfold-way/dictionary-flavor-layer.md) | every `(I₃, Y)` entry but one | ":46-49 "the standard `SU(3)` flavour assignments, **imported** … **not outputs of the braid construction**" |
| [`q-deformation-weight-lattice.md`](../../content/quantum-observable-universe/eightfold-way/q-deformation-weight-lattice.md) | Drinfeld–Jimbo root-datum invariance, lattices, Weyl group | ":60-62 has a section headed "standard, but not formalised here" |
| [`color-su3-from-g2.md`](../../content/quantum-observable-universe/eightfold-way/color-su3-from-g2.md) | `PSL(2,7) ≅ GL(3,𝔽₂)`, order 168, Günaydin–Gürsey `7 = 1 ⊕ 3 ⊕ 3̄` | ledger :21 "standard; machine-verified numerically" |
| [`a5-orbital-degeneracy-fracture.md`](../../content/quantum-observable-universe/appendix-standard-model/a5-orbital-degeneracy-fracture.md) | `SO(3) ↓ A₅` branching | ":12 "standard finite-group representation theory" |

**This is a credit, not a criticism.** The blocks label their standard content
as standard. The distinction is drawn cleanly and repeatedly. What a reader
must not do is read the *volume* of correct `SU(3)` representation theory as
framework support: 1061 lines of eightfold `.md` yield one derived entry.

---

## 3. The three "proved (Lean)" rows — correct, sorry-free, and arithmetic

All three compile green. The question is what the compiled statements *say*.

### 3.1 `RowCapObstruction.lean` — **the one genuine tier mislabel (Finding 2)**

**Tier claimed:** "**The obstruction is proved.** This is not an observation
but a theorem, machine-checked sorry-free"
([`schur-weyl-eightfold.md:75-77`](../../content/quantum-observable-universe/eightfold-way/schur-weyl-eightfold.md));
ledger row :17 "**proved** (Lean, sorry-free)".

**What the file actually contains** (read in full, 189 lines):

```lean
def weylDimAlt (N : ℕ) : ℕ := N.choose 3                       -- :92

theorem weyl_dim_alt_eq_zero_iff (N : ℕ) : weylDimAlt N = 0 ↔ N < 3 := by
  unfold weylDimAlt
  exact Nat.choose_eq_zero_iff                                 -- :101-103
```

Every proof in the file is `Nat.choose` arithmetic: `exact
Nat.choose_eq_zero_iff`, `by decide`, `omega`, `Nat.choose_le_choose`. The
representation theory — that `dim V_{(1³)}^{gl_N} = C(N,3)` (hook-content
formula), and the Schur–Weyl row cap `ℓ(λ) ≤ N` itself — is supplied by the
**`def` names and docstrings**, not proved. The file's own docstring is
candid about the boundary (:131-134: Worpitzky's identity "is **not**
formalised here").

**Why this is a mislabel and not a quibble: the chapter applies the correct
standard in two of three places and omits it in the third — the one place
where it is load-bearing.**

| Lean file | Chapter's framing |
|---|---|
| `Sym2Gate.lean` | ✅ "What that file *proves* is only the arithmetic — its declarations reduce to identities such as `6 = 6 ∧ 0 = 0`, with the representation-theoretic content **supplied by hand in the statement names, not by the proofs**. … the file should not be cited as [a machine-checked pass]." (schur-weyl:114-121) |
| `WeylInvarianceQDeformation.lean` | ✅ section headed "**What the Lean does not establish**": "What is machine-checked is the *arithmetic* of the separation on the `A₂` datum, which is a weaker statement and **should not be cited for the stronger one**." (q-deformation:52-58) |
| `RowCapObstruction.lean` | ❌ "**The obstruction is proved.** This is not an observation but a theorem" |

The `Sym2Gate` sentence describes `RowCapObstruction` verbatim. The chapter
knows the rule; it simply is not applied here.

**Mitigation, stated fairly.** The *content* is not wrong — the hook-content
formula and the row cap are textbook, so the conclusion (`N = 2` cannot host
the eightfold decomposition) is true. And the scope-(b) discipline **is**
correctly observed: schur-weyl:93-94 and the file's :61-68 both name the
invariant (the Schur–Weyl row cap), as AGENTS.md requires. The defect is
purely the tier word.

**Adversarial note on substance.** Even granting the row cap, the theorem is
close to a definitional restatement: "a partition with three rows does not
fit in two rows" needs no proof, and dressing it as a machine-checked theorem
inflates its weight. Note also that `decuplet_forces_three` and
`singlet_forces_three` run in the direction the framework does *not* need —
nobody doubted that observing a decuplet implies `N = 3`; the framework needs
`N = 3` **supplied**, which is exactly the open half the chapter correctly
records (ledger :18).

### 3.2 `GellMannOkuboIdentity.lean` — **correctly labelled**

Hand-verified. `massSqQuadrupled a b c fourCasimir Y := 4a + 4bY +
c(fourCasimir − Y²)` (:78-79) is the correct ×4 form of the standard
first-order octet ansatz `m² = a + bY + c(I(I+1) − Y²/4)`. On the
pseudoscalar octet: LHS `16a + 8c`, RHS `12a + (4a + 8c)` — identical, for
all `a, b, c`. `gmo_identity` is `unfold; ring` over generic
`[CommRing R]` (§7c-clean; no gratuitous `ℝ`).

**This is not laundering.** The `def` encodes a *hypothesis* (the textbook
ansatz) and the theorem *derives* the vanishing from it — the §3b-cond-legit
pattern, unlike §3.1 where the `def` encodes the conclusion's content.

**What it gives us is a proved negative about the target, not a derivation:**
Gell-Mann–Okubo has *zero* discriminating power, so reproducing it is not
evidence for QOU or for anything else. `meson-mass-splitting.md:74-77` and
ledger :29 state this correctly, and item 8 correctly relocates the testable
content to the ≈ 6 % *deviation*, for which the framework currently predicts
0. **This is genuinely valuable work** — it removes a target that would
otherwise have looked like a success — and it is the clearest example of the
chapters' main mode of contribution: *deleting false evidence.*

### 3.3 `WeylInvarianceQDeformation.lean` — **correctly labelled**

Green, sorry-free, and the block carries its own "What the Lean does not
establish" section (:52-58). The content — that the Serre coefficient `[2]_q`
moves with `q` while the Cartan diagonal `a_ii = 2` does not — is a real
conceptual disambiguation of a genuine confusion, correctly scoped to the
arithmetic of the `A₂` datum.

**Corollary for the `q`-leverage question.** This is the formal statement of
why this layer carries **no L2 precision leverage**, consistent with refuted
class row **C20**
([`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)):
the classification data is `q`-independent, so it cannot be the fibre-level
`F(q)` any `c_k` or `Δ_λ` closure needs. Nothing in either chapter changes
C20, and neither chapter claims otherwise.

---

## 4. What is CONDITIONAL, and on what?

### 4.1 `N = 3` gates essentially all flavour content

The framework supplies `dim V = 2`; no choice of `q` raises it (Drinfeld–Jimbo
does not change dimensions). **What collapses if `N = 3` never arrives:**

| Casualty | Block |
|---|---|
| Meson octet `3 ⊗ 3̄ = 8 ⊕ 1` — entire block | `meson-octet-decomposition.md:58-65` |
| Baryon decuplet — entire block, all 10 rows | `borromean-decuplet-derivation.md:75-80` |
| Every quark row of the dictionary (`u`, `d`, `s`) | `dictionary-flavor-layer.md:15-17` |
| Every `Y` value in every table | `dictionary-flavor-layer.md:39` |
| Meson mass splittings between isospin multiplets | `meson-mass-splitting.md:89-92` |
| The `η'` singlet (absent at `N = 2`) | `RowCapObstruction.lean:48-51` |

**What survives:** the `Q = w/2` / `I₃` writhe result (`SU(2)`-level, needs no
flavour `SU(3)`), the GMO negative (a statement about any first-order octet
breaking), and the `WeylInvariance` disambiguation.

So: **remove `N = 3` and the eightfold chapter retains one derived entry and
two proved negatives out of eleven blocks.** The intro states this plainly
(:36-39, :74-80) and it is the single most important honest sentence in either
chapter.

**Structural note (Finding 3, minor).** `meson-octet-decomposition` and
`borromean-decuplet-derivation` are block kind `proposition` while every
claim in them is conditional on an *unavailable* hypothesis. This is not a
formal §3b violation (`N = 3` is an open item, not a `conj:` block, so
propagation does not trigger), but the §3b-cond banner form — *"Proposition
(conditional on …)"* — would represent them more honestly than a bare
`proposition`. Similarly `a2-from-three-strands` is a `proposition` whose own
scope note says nothing is derived from it, and `color-su3-from-g2` is a
`proposition` whose abstract says its bridge "is refuted below".

### 4.2 The appendix's four conjectural stages

`conj:gauge-hecke-realization`, `conj:sm-gauge-truncation`,
`conj:sm-colour-stabilizer-action`, `conj:sm-hypercharge-invariant` — all
four are content-bearing classes with **no instance**, which is the honest
representation of an open primary (§3b-tax). Their Lean is thin and
*correctly* thin: the substantive lemmas are non-vacuity checks
(`not_gaugeHeckeRealization_of_subsingleton`,
`not_standardModelTruncation_of_subsingleton`,
`not_colourStabilizerAction_of_dim_sq_lt`, `negOneU1_ne_one`). These prove
the classes are not trivially satisfiable. That is worth having and it is not
progress toward the Standard Model.

`gauge-action-groupoid.lean` is the one place with positive content:
`gaugeEquiv_equivalence` (gauge equivalence is an equivalence relation),
`act_inv`, `zeroActionEnd`. Real, and light — the groupoid formalism, not
physics.

### 4.3 `a5-orbital-degeneracy-fracture` — correctly labelled, with an objection

**The task asked: prediction, or restatement of finite-group character
theory?** It is a restatement, and the block says so (:12 "standard
finite-group representation theory"; :14 "conditional on the truncation
conjecture … **not a prediction wired to any computation**"). **No mislabel.**

I re-derived all six rows independently by icosahedral character arithmetic
and they are correct: `l = 0 → 1`, `1 → 3`, `2 → 5`, `3 → 3' ⊕ 4`,
`4 → 4 ⊕ 5`, `5 → 3 ⊕ 3' ⊕ 5`.

**Objection the block does not address (scope-(a), an observational tension I
am raising, not a proved exclusion).** The block rests its value on
"falsifiability in principle": *"a truncated discrete symmetry cannot hold
seven states exactly degenerate, while exact `SO(3)` can."* But free-atom
`f`-shell degeneracy **is** observed, to spectroscopic precision: free-atom
states are labelled by `J` with degeneracy `2J + 1` exact by rotational
invariance, and the observed lifting is spin–orbit, in a `J` pattern, not
along a `3' ⊕ 4` seam. So either (i) the claim is already in tension with
free-atom spectra, or (ii) the splitting sits below all achieved resolution,
in which case the claim is *untestable* rather than *falsifiable* and the
block's stated value does not hold. The block should say which. This is a
referee objection, not a refutation — I have not computed a bound.

**Sidecar gap (Finding 4).** `a5-orbital-degeneracy-fracture` and
`cal2-higgs-knot-coupling` are the only two blocks in either chapter with
**no `.qa.json` sidecar**, so they are invisible to every per-block checker
(`clarity-*`, one-voice, `q-usage-*`, `da-*`). Both are `remark` kind.

---

## 5. Hidden DOF and fitted content

### 5.1 The strand-twist battery: **4 of 10,000 is forced arithmetic, not evidence** (Finding 5 — the material finding)

**The task asked whether "4 survivors from an enumerated candidate space" is
evidence, or a search whose prior nobody has computed. The prior is
computable. I computed it. The answer is forced.**

The battery's constraint is the helon normalisation
`Q_twist = totalTwist/3` ([`strand_twist_y_battery.py:10`](../../computations/strand_twist_y_battery.py)),
i.e. `totalTwist = 3Q` per flavour. Multiset counts of 3 draws from
`{−1, 0, +1}` by sum:

```
T:      -3  -2  -1   0  +1  +2  +3
count:   1   1   2   2   2   1   1     (total 10 = the witness's
                                        multisets_per_flavour)
```

Required `T = 3Q`: `u → +2`, `d → −1`, `ν → 0`, `e → −3`. Surviving options
per flavour are therefore `1 × 2 × 2 × 1 = ` **4**.

My reconstruction reproduces the witness element-for-element:

| flavour | required `T` | my enumeration | `witness.data.survivors.per_flavour_multisets` |
|---|---|---|---|
| `u` | +2 | `[(0,1,1)]` — unique | `[[0,1,1]]` ✓ |
| `d` | −1 | `[(-1,-1,1), (-1,0,0)]` | 2 options, first `[-1,-1,1]` ✓ |
| `ν` | 0 | `[(-1,0,1), (0,0,0)]` | 2 options, first `[-1,0,1]` ✓ |
| `e` | −3 | `[(-1,-1,-1)]` — unique | `[[-1,-1,-1]]` ✓ |

**Consequences.**

1. **"4 of 10,000" has no selectivity content.** The `10,000` is `10⁴`, the
   *unconstrained* product across four flavours. The constraint **factorises
   per flavour**, so the honest statement of selectivity is "`1 × 2 × 2 × 1`",
   not "4 in 10⁴". Quoting the ratio presents a factorised constraint as a
   global search and reads as ~2500× selectivity where there is none.
2. **The "uniquely determined" `u = {0,1,1}` and `e = {−1,−1,−1}` are
   compositional accidents.** They are unique *only because* `T = +2` and
   `T = −3` each admit exactly one multiset of three draws from
   `{−1, 0, +1}`. This is a fact about compositions, not about the framework's
   braid words. `d` and `ν` have two options for the same reason in reverse.
3. **The target was the input.** The battery's spectrum condition requires the
   `Y` values to reproduce the known SM first-generation spectrum; the
   `Z₆` block (`witness.data.z6.sm_table_ok`, all `True`) checks that the
   *SM table* satisfies `Z₆` — a known fact (Baez–Huerta) — not that the
   survivors do anything.

**Is the tier label wrong?** No — and this matters for fairness. The witness
`description` says "EXPLORATORY"; `flavor-charge-assignments.md:57-66` says
"candidate-space feasibility: the twist multisets are **enumerated, not
derived** from the framework's braid words, so the conjecture remains open";
`eightfold-open-problems.md:75-77` names "the derivation gap" precisely.
**Nothing is wired.** The defect is *presentation*: the "4 of 10,000" and
"uniquely determined" phrasings carry an evidential charge the computation
does not support, and they appear in **three** places —
`flavor-charge-assignments.md:57-66`, `eightfold-open-problems.md:70-74`, and
`sm-open-problems.md:11`. Recommended replacement: state the per-flavour
factorisation and note that the residual multiplicity is a composition count.

### 5.2 Three generations from `{3,5,7,9} \ {9}` — post-hoc shape (Finding 6)

[`sm-open-problems.md:18`](../../content/quantum-observable-universe/appendix-standard-model/sm-open-problems.md)
tiers the three-generation row **"partially derived"**: a genus bound admits
odd windings `n ∈ {3,5,7,9}`, a continuant divisibility `b_a ∣ b_n ⟺ a ∣ n`
(Lean, sorry-free) singles out `9 = 3·3` as "the unique harmonic", "leaving
the three prime windings `{3,5,7}`".

**This is the one place in either chapter where the shape of a numerological
argument shows through.** Three generations are obtained by *removing one
element* from a four-element set, and the removal criterion (harmonicity via
continuant divisibility) is unrelated to generation counting. Any criterion
that eliminated exactly one of four would have produced "three". The row
itself concedes the substance — "open (scope-(a)): the physical bridge
'normal-form-independent winding ⇒ generation' and the `net → mass` map" —
which is to say **the entire content is open** and what is proved is a
divisibility lemma about continuants.

`partially derived` is therefore too warm for a row whose own status field
says the bridge is open. `open, with an adjacent proved divisibility lemma`
would be accurate. (The genus bound and continuant Lean live outside my
declared scope, in `particle-interactions/`; I did not verify them and make
no claim about them.)

### 5.3 Citation precision on the colour row (Finding 7, minor)

`sm-open-problems.md:12` credits the colour row with "the proved `dim = 8`
gate", "bracket closure, sorry-free", and a faithful octonion base-module
action. Those proofs **do** exist in the corpus (`QOU/MathlibExt/Octonion*`,
8+ files — corpus-grep confirms, I am not claiming absence) but they are
**not** at the block's own cited `lean.ref`
(`qou:QOU.StandardModel.ColourStabilizerAction`, whose file contains only the
class and two negative sanity lemmas). A reader following the ref finds none
of the claimed proofs. Note also the row's own parenthetical "**tautological
instance**" for the faithful action — an admission worth keeping visible.

### 5.4 No fitted content found

To be explicit: **I found no fit, and no hidden continuous DOF, in either
chapter.** The twist battery is over-*presented*, not fitted. The `c = 1/2`
coupling is structurally fixed. No parameter is tuned to data anywhere in
the 31 blocks. The anti-fit discipline is intact.

---

## 6. The five self-withdrawals — an underweighted contribution

Both chapters *retract* earlier over-claims in the text. These are real
epistemic work and neither intro counts them:

| # | Withdrawn claim | Location |
|---|---|---|
| 1 | `A₂` Cartan matrix from a counting formula `a_ij = 2δ_ij − |{…}|` — "a re-encoding of the presentation, not an independent derivation" | `a2-from-three-strands.md:33-37` |
| 2 | GMO as a derivation *target* | `meson-mass-splitting.md:46-51` |
| 3 | ≈ 3.3 % `dim_q`(adjoint) vs the ≈ 6 % GMO deviation — "a category error (a dimension is not a mass splitting)" | `meson-mass-splitting.md:83-87`, ledger :134 |
| 4 | Brunnian-ness → Young-symmetriser selection — "withdrawn as a non-sequitur" | `borromean-decuplet-derivation.md:50-51` |
| 5 | `S₄ ⊂ PSL(2,7)` maximality as *selection* of the Klein quartic — "that inference is withdrawn" | `color-su3-from-g2.md:55-57` |

Plus two proved/verified negatives beyond GMO: the `S₄` bridge has "no
separating power at all" (an `S₄`-invariant quartic *pencil* means infinitely
many non-isomorphic genus-3 curves admit `S₄`; Fermat is `t = 0`), and the
Bring → Klein genus degeneration is **excluded** under its own three premises
with the invariant named (`S₄` has no orbit of size ≤ 2 on `ℙ²`) — a properly
formed scope-(b) per AGENTS.md.

**Deleting false evidence is the dominant mode of contribution in these two
chapters.** Five withdrawals + three proved negatives + two machine-verified
refutations, against one derived entry. A reader who wants to know "what do
these derivations give us" should be told that first.

---

## 7. Answers to the six questions asked

1. **What is genuinely derived?** One entry: `Q = w/2` with `c = 1/2`
   structurally fixed (genuine, parameter-free, and pre-existing in
   `def:coulomb-charge`), from which `I₃` on the nucleon doublet follows as a
   two-point sign-and-ratio match. Nothing else.
2. **What is merely standard?** ≈ 48 % of the ledger (8 rows explicitly
   `standard` + 3 `proved` rows that are arithmetic instances of standard
   facts). The chapters label this correctly; the risk is a reader mistaking
   volume for support.
3. **What is conditional, and on what?** `N = 3` gates the meson octet, the
   whole baryon decuplet, every quark row, every `Y` entry, all inter-multiplet
   mass splittings, and the `η'`. It is unavailable (`dim V = 2`) and no `q`
   changes it. The appendix's four stages are conditional on four
   instance-free conjecture classes.
4. **Is the intro's net-contribution claim accurate?** Yes — and it
   *understates* the negatives while slightly overstating "derived". The
   honest net is: **one derived quantum-number entry, three proved negatives,
   two machine-verified refutations, five self-withdrawals, and the best
   organised list of missing objects in the corpus.**
5. **Hidden DOF or fitted content?** No fits, no hidden continuous DOF. The
   4/10,000 twist battery is not evidence — the prior is computable and the
   outcome is forced (`1 × 2 × 2 × 1`). The `a5` claim is a restatement of
   character theory and says so. The three-generation row's `{3,5,7,9} \ {9}`
   is post-hoc in shape.
6. **Precision leverage?** None, consistent with C20. Neither chapter claims
   any, and `WeylInvarianceQDeformation` is effectively the formal statement
   of *why* not.

---

## 8. Findings, and beans filed

| # | Finding | Severity | Location | Bean |
|---|---|---|---|---|
| 1 | `derived` vs `matches` — different epistemic verb across chapters for the writhe → `I₃` map; eightfold statement carries no pointer | minor | `flavor-charge-assignments.md:13-18` | — |
| 2 | **`RowCapObstruction` tiered "proved" while `Sym2Gate` / `WeylInvariance` get the arithmetic-vs-rep-theory caveat — same construction, two standards** | **material (tier)** | `schur-weyl-eightfold.md:75-77`; ledger :17 | `qou-b4lo` |
| 3 | `proposition` kind on blocks wholly conditional on an unavailable hypothesis; §3b-cond banner form would be honester | minor | `meson-octet-decomposition`, `borromean-decuplet-derivation` | — |
| 4 | Two blocks have no `.qa.json` sidecar → unswept by every per-block checker | minor | `a5-orbital-degeneracy-fracture`, `cal2-higgs-knot-coupling` | `qou-cy2h` |
| 5 | **"4 of 10,000 survive" / "uniquely determined" — zero selectivity; forced by `1×2×2×1` composition counts** | **material (presentation)** | 3 sites: `flavor-charge-assignments.md:57-66`, `eightfold-open-problems.md:70-74`, `sm-open-problems.md:11` | `qou-xu5t` |
| 6 | Three generations tiered "partially derived" on `{3,5,7,9} \ {9}`; own status says the bridge is open | moderate | `sm-open-problems.md:18` | `qou-a5os` |
| 7 | Colour-row proofs cited at a `lean.ref` that does not contain them | minor | `sm-open-problems.md:12` | — |
| 8 | `a5` "falsifiable in principle" unaddressed against exact free-atom `f` degeneracy | moderate (objection) | `a5-orbital-degeneracy-fracture.md:14` | `qou-cy2h` |

**No content was edited in this pass** (content edits carry sidecar +
render-QA surface). Findings 1–8 are reported for the owner to triage.

## 9. What this audit did NOT establish

- ~~The three `QOU/MathlibExt/Octonion*` files backing the colour row are
  **UNVERIFIED-HERE**.~~ **Resolved after first commit:**
  `scripts/lean-direct-cone.sh` returned `ok=9, err=0, blocked=0` — all three,
  plus their 6-module cone, type-check. See §"The colour-row cone". The
  initial `✗ FAILED` was a missing-olean cascade, as diagnosed.
- The genus bound and continuant Lean behind Finding 6 live in
  `particle-interactions/` and were not verified.
- Finding 8 is a referee objection, not a computed bound.
- No claim is made that any item is open beyond what the chapters themselves
  record; the corpus-grep checklist located every "derived" claim's source
  (`docs/audits/`, `content/`, `computations/`, coordination ledgers), and one
  early suspicion of an uncited claim is retracted in §1.1.
