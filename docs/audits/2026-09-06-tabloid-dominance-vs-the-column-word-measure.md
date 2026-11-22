# 3.14's inner axis: a corpus counterexample raised a doubt, and the source settled it

> **Read the RESOLUTION at the bottom first.** The body below is the doubt as raised, kept
> because its reasoning is what a reader needs to see why the resolution is not circular.
> **Verdict: `murphyLex`'s inner axis is RIGHT** — Mathas' own proof of 3.14 sums over
> `v ▷ t`, strict dominance at the same shape, which is exactly `domGtOn`.

**Date:** 2026-09-06 · **Bean:** `qou-phir` · **Branch:** `claude/mathas-314-descent-2026-09-06`

## The finding

`MurphyInductionMeasure.murphyLex` (merged, #6899) is a lexicographic product:

* **outer** — `PartitionLexWellFounded.lexGtOn`, lex across shapes of fixed size;
* **inner** — `DominanceWellFounded.domGtOn`, **strict dominance on `Specht.Tabloid μ`**.

Opening the next step — 3.14's descent — with the corpus-grep the arc's discipline requires
turned up a directly relevant result that **neither of those two files cites**, and that a
topic-grep for "3.14" or "Murphy" does not reach because it lives in the `q = 1` Specht
tree under the word *straightening*.

[`SpechtStandardBasisCore.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/SpechtStandardBasisCore.lean),
§"Measure correction (2026-07-07)", lines 81–90 and 821–836:

> An earlier version used `domWeight` (a linear extension of *tabloid dominance*). That
> measure is **wrong** for straightening: `straightening_step_colMax` stated over it is
> FALSE (exact-arithmetic disproof, μ=(3,2), t=[[1,2,3],[5,4]]; audit §3.5), because Garnir
> produces terms whose tabloids are dominance-*incomparable* to `{t}`.
>
> […] **so no tabloid-level measure orders them.**

The replacement is the classical **column-reading word** `colWordNum` (James Thm 8.4, Sagan
§2.6), *"validated exhaustively to (3,3,2)/(4,3,1)"*, on which the whole `q = 1` spanning
argument then goes through **sorry-free**: `straightening_step`,
`straightening_step_colMax`, `standardPolytabloid_straightening`. `domWeight`/`domBound`
survive as *"orphaned […] no longer on the spanning path"*.

Counterexample audit:
[`2026-07-06-garnir-strict-domweight-counterexample.md`](2026-07-06-garnir-strict-domweight-counterexample.md).

## What this does and does not establish about `murphyLex`

**Stated carefully, because the two claims are different and only one is measured.**

What is measured: a **Garnir step in the `q = 1` polytabloid straightening** produces terms
whose tabloids are dominance-incomparable to the source's, at an explicit shape and tableau.

What is **not** measured, and must not be inferred from it: that Mathas 3.14's case (ii)
has the same defect. Three reasons to keep them apart:

1. **Different step.** Sagan §2.6 straightens a *polytabloid* `e_t` in the Specht module.
   Mathas 3.14 rewrites a *Murphy element* `m_{st}` in `H_n(q)`. That they share the name
   "Garnir" is not an argument.
2. **Different strictness.** Mathas' case (ii) states `u ⊵ s`, `v ⊵ t` — **non-strictly** —
   with case (i)'s lex drop doing the strict work. `domGtOn` is the *strict* part. The
   chain-status audit already records this reconciliation
   ([`2026-09-04`](2026-09-04-mathas-murphy-chain-status.md), §"The two orders are both
   live"), and it is why the 2026-07-06 counterexample was not treated as fatal then.
3. **The outer axis may carry every Garnir step anyway.** `GarnirShapeCard.lexGtOn_garnirPartOf`
   (merged) shows the Garnir step drops the **shape**, so on that step `murphyLex` descends
   on the outer axis and never consults dominance. If case (ii) is reached only by steps
   that do *not* change the shape, the counterexample's population and case (ii)'s may be
   disjoint.

So the honest status is: **`murphyLex` is not refuted, and it is not validated either.**
What is new is that the corpus holds a measured reason to doubt the inner axis and a
*validated alternative* for the same job, and the merged files pointed at neither.

## Why this is worth recording rather than just fixing

`murphyLex_wellFounded` proves the measure **terminates**. It says nothing about whether the
terms 3.14 produces actually **descend** in it — the scope note in
`MurphyInductionMeasure.lean` says exactly that. So the risk is not an unsound proof; it is
a measure that terminates and that the descent step cannot be proved against, discovered
after an induction has been written on it. That is what happened at `q = 1` in July, and it
cost a measure plus everything stated over it.

## The measurement that would settle it

A probe, in the arc's established style — exact arithmetic, self-checked, refuting-or-not
before any Lean:

> For every shape `μ ⊢ n` (n ≤ 6) and every row-standard non-standard `t`, take the Garnir
> tableau `g` and the `w` of 3.13 (already built,
> `DescentNodeExists.exists_garnir_length_additive`), expand `m^row_{s t} = m^row_{s g}·T_w`
> in the Murphy family, and ask of each surviving term `m_{uv}`: is its shape lex-greater
> than `μ`, or — when equal — is `u` dominance-comparable to `s`?

Three outcomes, all useful:

* every same-shape term is dominance-**comparable** and descends ⇒ `murphyLex`'s inner axis
  is right and case (ii) differs from the `q = 1` step;
* some same-shape term is **incomparable** ⇒ the `q = 1` counterexample's conclusion carries,
  and the inner axis should be `colWordNum` (which is already built, sorry-free, and has
  `colWordNum_lt_of_first_diff`, `colWordNum_swap_lt`, `fibre_colWordNum_decrease`);
* **no same-shape terms arise at all** ⇒ 3.14's case (ii) is vacuous on this route and the
  induction is single-axis, which would simplify it considerably.

The third is worth naming because it is cheap to test and would make the inner axis moot.

## Two things the corpus turned out to already have

Both were found by this grep and neither was known to the merged work:

1. **A complete, sorry-free straightening theorem at `q = 1`** —
   `standardPolytabloid_straightening`, by well-founded induction on `colWordNum`
   descending. The chain-status audit records that 3.13's *length* half has "NO `q = 1`
   antecedent in the corpus: Sagan's Garnir straightening never tracks Coxeter lengths".
   True of the length half. **It is not true of the spanning half**, which is what 3.14 is,
   and that antecedent is proved.
2. **A validated well-founded measure for exactly this kind of descent**, with its
   monotonicity lemmas already in place.

Neither closes 3.14 — `q`-deformation is the whole difficulty — but the next tranche should
open by asking what the `q = 1` argument gives and what the deformation costs, rather than
deriving from scratch.

## Action taken here

Cross-references added to `MurphyInductionMeasure.lean` and `DominanceWellFounded.lean` so a
reader of either meets this before writing an induction on it. No measure changed, no proof
touched, nothing retracted — the merged results stand exactly as stated.

---

## 🛑 RESOLVED, same day, from the primary source: the inner axis is RIGHT

The section above names a probe and three outcomes. **None of them had to be run** — Mathas'
own proof of 3.14 answers it, and reading it was one command. Recording that as the lesson
before the finding: the doubt was raised from a *corpus* result about a *different* step,
and the *source* settles it directly.

`library/hecke-alg/sections/page-027.md`, the proof of 3.14 (OCR normalised; `D` is
`⊵`, `B` is `▷`):

> First suppose that `t` is row standard but not standard. By Lemma 3.13, `m_st = m_sg T_w`
> for some Garnir tableau `g` and some `w ∈ S_n`. Consequently, by Lemma 3.12 there exists an
> element `h = Σ r_uv m_uv`, where `u` and `v` are row standard ν-tableaux with **ν > λ**,
> such that
>
>     m_st = T*_{d(s)} m_{t^λ g} T_w = T*_{d(s)} (h + Σ_{v ▷ g} m_{t^λ v}) T_w
>          = T*_{d(s)} h T_w + Σ_{v ▷ t} r_v m_sv
>
> for some `r_v ∈ R`, and where the last equality uses **Corollary 3.8**. By **Corollary 3.4
> and induction on ν**, `T*_{d(s)} h T_w` can be written in the required form. Furthermore,
> **by induction on `t`**, the terms `m_sv` can be written as a linear combination of terms
> `m_uv'` […]

Three things follow, and they overturn the concern rather than confirm it.

1. **Case (ii) is NOT vacuous.** The third outcome the section above proposed testing first is
   refuted outright: `Σ_{v ▷ t} r_v m_sv` is same-shape and is the case-(ii) population.
2. **Its terms are dominance-COMPARABLE by construction** — the sum is indexed *by* the
   dominance relation. This is the structural difference from the `q = 1` polytabloid step,
   whose Garnir terms were *measured* incomparable: there the terms fall out of a coset sum
   and their tabloids land where they land; here the term set is **defined** as those `v`
   dominating `t`. So the 2026-07-06 counterexample does not carry, for a reason sharper than
   "different step": the two term-sets are produced by different mechanisms, one of which
   cannot produce an incomparable term at all.
3. **And the dominance in the PROOF is STRICT.** 3.14's *statement* says `u ⊵ s`, `v ⊵ t`;
   its *proof* sums over `v ▷ t`, and Corollary 3.15 makes the same distinction explicitly —
   *"(ii) ν = λ, u = s and **v ▷ t**"*. The loose `⊵` is the shape of the conclusion; the
   induction steps on `▷`.

**That is exactly what `DominanceWellFounded.domGtOn` is** — `domRel b a ∧ b ≠ a`, "`a`
strictly dominates `b`" — and `domGtOn_induction` supplies `C a` from `C b` for every `b`
strictly dominating `a`, which is the direction *"by induction on `t`"* needs.
`MurphyInductionMeasure.murphyLex`'s inner axis is the right measure, and its outer axis
`ν > λ` is the lex order the proof names in the same breath. **The measure matches Mathas'
induction on both axes.**

The cross-references added to the two Lean files are kept, re-scoped to say this rather than
to raise the doubt: the `q = 1` counterexample is real and is *about the other mechanism*, and
a reader who meets `colWordNum` should know why it is not needed here.

### What this hands the next tranche, precisely

The proof names its own remaining inputs, and two of the four are already in the corpus:

| input | status |
|---|---|
| **3.13** — `m_st = m_sg T_w` | **proved**, `MurphyRefTab.exists_garnir_murphyMRow_factor` (#6899) |
| **Corollary 3.4** — `M^μ` free on `{x_μ T_d}` | **proved**, `CompositionCosetSum` |
| **3.12** — `m_{t^λ g} = h + Σ_{v ▷ g} m_{t^λ v}`, `h` over `ν > λ` | **open** — the algebra half; needs 3.9 at basis level |
| **Corollary 3.8** — collapses `(Σ_{v ▷ g} m_{t^λ v}) T_w` to `Σ_{v ▷ t} r_v m_sv` | **open, and not previously named on this arc** |

Corollary 3.8 is the new item. It is what converts a sum indexed by tableaux dominating `g`
into one indexed by tableaux dominating `t` — i.e. it is precisely the step that makes the
strict-dominance induction close, and nothing in this corpus's chain-status ledger had
identified it as an input. That is the next thing to read and then to state.

---

## 🟩 And reading one lemma further: dominance on tableaux **IS** the Bruhat order

Corollary 3.8 was named above as the new open input. Reading it, and the Proposition it
sits under, turns out to settle something much larger than 3.8 — and the source says it in
so many words, immediately before stating it:

> The partial order `⊵` on `S_n` is the ubiquitous **Bruhat–Chevalley order**. Perhaps
> surprisingly, it **agrees with the dominance ordering on row standard λ-tableaux** (when
> restricted to `D_λ`).
>
> **3.7 Proposition (Dipper–James).** Let λ be a composition of `n` and suppose that `s` and
> `t` are row standard λ-tableaux. Then **`s ⊵ t` if and only if `d(s) ⊵ d(t)`.**

`d` is a **bijection** from λ-tableaux to permutations (`TableauPerm.equivPerm`, proved).
So `DominanceWellFounded.domGtOn` and the Bruhat order on `Perm (Fin n)` are **the same
order, transported along `dOf`** — not two orders that happen to co-operate.

### What that changes

1. **The inner axis is Bruhat.** The resolution above showed `domGtOn` matches Mathas'
   `▷`. 3.7 says more: that `▷` *is* Bruhat. `murphyLex` is therefore
   **lex-on-shapes × Bruhat-on-permutations**, which is a far more standard object than
   "lex × tabloid dominance" and comes with a literature.
2. **`QOU/Machinery/CoxeterBruhat.lean` is on the critical path**, which was not known when
   it was built. It was written on this arc as *"the subword order Mathlib has none of"*, with
   four things deliberately left unproved: **transitivity, antisymmetry, the subword property,
   and lifting**. Corollary 3.8's proof consumes exactly those — its first move is
   > *"It follows from **Theorem 1.1.11** that there exist `r_x ∈ R` such that
   > `T_{d(v)} T_w = Σ r_x T_x`, where the sum is over elements `x ∈ S_n` which have a reduced
   > expression which is a **subexpression** of `d(v)w`; that is, `r_x ≠ 0` only if
   > `x ⊵ d(v)w`."*
   
   Theorem 1.1.11 **is** the subword property. The `T`-basis expansion of a product is
   supported on the Bruhat interval below the product — the same shape as this arc's already
   proved `TwInverseBruhat.TwInv_mem_spanBruhatLe`, which was built for `T_w⁻¹` and is the
   nearest thing the corpus has to it.
3. **Two inequivalent definitions of Bruhat are now both in play, and neither is labelled.**
   The source's is *reflection-generated with length increase* —
   `w = v t₁⋯t_k` with `ℓ(v t₁⋯t_j) = ℓ(v) + j`. `CoxeterBruhat.BruhatLe` is the **subword**
   definition. Their equivalence is a theorem (it is Theorem 1.1.11's neighbourhood), not a
   definitional unfolding. A corpus that accretes both under one name repeats the `dOf`
   defect this branch's parent PR spent a tranche fixing.

### The next step is now a different one, and it is smaller

Rather than attacking 3.12's algebra half (open, behind 3.9 at basis level), **prove
Proposition 3.7**. It is self-contained combinatorics — the source's proof is eight lines,
by induction on a transposition `(a,b)` chosen at the first row where `s` and `t` differ —
and it needs no Hecke algebra at all. What it buys:

* the inner axis of `murphyLex` becomes a **Bruhat** statement, so every Bruhat lemma proved
  anywhere in the corpus applies to it;
* it is the bridge Corollary 3.8's proof crosses, so 3.8 cannot be stated honestly without it;
* it makes the sibling work on Bruhat antisymmetry and the deletion condition (**#6894**)
  load-bearing for the Murphy arc rather than adjacent to it.

**Scope note, so this is not over-read.** 3.7 is stated for a **composition** λ and for
`d(s)`, `d(t)` in `D_λ`. This corpus's `TableauPerm.dOf` is defined on `YoungDiagram`-shaped
(partition) tableaux, and the composition-indexed coset machinery lives separately in
`CompositionCoset*`. Which of the two `d`'s 3.7 is about — and whether the corpus needs the
composition form to use it — is **not settled here** and should be checked before the
statement is written, exactly as the two-`dOf` collision would have been.

---

## Dipper–James 3.7, measured — confirmed, and the orientation is REVERSING

[`dipper_james_dominance_is_bruhat_probe.py`](../../computations/hecke/dipper_james_dominance_is_bruhat_probe.py),
exact integer arithmetic, no float, self-checks before any verdict (`d` injective with
`d(t^λ) = 1`; dominance a partial order; both Bruhat relations partial orders with least
element `1`).

Over **every ordered pair** of row-standard λ-tableaux, every partition λ ⊢ n:

| n | pairs | `s ⊵ t ⇒ d(s) ≤ d(t)` | converse |
|---|---|---|---|
| 3 | 46 | 46/46 | 46/46 |
| 4 | 773 | 773/773 | 773/773 |
| 5 | 19 426 | 19 426/19 426 | 19 426/19 426 |
| 6 | 708 062 | **708 062/708 062** | **708 062/708 062** |

**Both directions, both Bruhat definitions.** 3.7 is confirmed on the measured range.

### 🛑 The orientation is the finding, and I got it wrong first

The obvious transcription of *"`s ⊵ t` iff `d(s) ⊵ d(t)`"* is `d(t) ≤ d(s)`. **That is
backwards**, and the first run said so: it failed at **30/46, 511/773, 14201/19426,
565748/708062** — *identically in both directions and under both Bruhat definitions*. Equal
forward and converse counts is the signature of a **flipped relation**, not of a
counterexample, which is how it was caught rather than reported as a refutation of a
published lemma.

The reason is structural and worth stating once: **`t^λ` is dominance-MAXIMAL while
`d(t^λ) = 1` is Bruhat-MINIMAL**, so `d` is order-**reversing** onto standard Bruhat.
Equivalently, Mathas' `⊵` on `S_n` is standard Bruhat with the order reversed. The correct
correspondence is

    s ⊵ t   ⟺   d(s) ≤ d(t)   (standard Bruhat)

A Lean statement written off the page would have had this backwards and been unprovable for
a reason that looks like a hard mathematical obstruction. Sixth instance of the
handedness/orientation trap on this arc.

### The Bruhat naming collision is COSMETIC on `S_n`, not semantic

The two definitions — `CoxeterBruhat.BruhatLe` (subword) and Mathas' (reflection-generated
with length increase) — were compared directly, permutation by permutation:

| n | agree |
|---|---|
| 3 | 6/6 |
| 4 | 24/24 |
| 5 | 120/120 |
| 6 | **720/720** |

**Identical on the measured range.** So the collision flagged in `CoxeterBruhat.lean` needs a
docstring, not a rename — and 3.7 may be stated against `BruhatLe` without choosing sides.
This does **not** discharge the subword property as a *proof obligation*: Corollary 3.8 needs
it as a theorem about arbitrary `n`, and 720/720 at `n = 6` is evidence, not a proof.

### Scope question from the previous section: settled

3.7 is stated for a **composition** λ. The Lean statement should be for **partition** shapes
with `TableauPerm.dOf`, because:

* a partition **is** a composition, so the partition case is a genuine special case, not an
  analogue;
* `TableauPerm.dOf t = refTab.trans t.symm` with `refTab = t^λ` row-superstandard, which is
  Mathas' `d(t)` defined by `t = t^λ · d(t)` — same object, verified by the probe's
  self-check that `d(t^λ) = 1` and `d` is injective;
* `MurphyInductionMeasure.murphyLex` is indexed by `PartOf n`, so the partition case is
  exactly what consumes it.

The composition form stays available if 3.9 at basis level turns out to need it; nothing here
requires building it.

---

## 🛑 A verification claim I published was false: `precision-gates.sh` is RED, on `main` and everywhere

Both this PR's body and the **merged** #6899's said *"`scripts/precision-gates.sh --changed`
exit 0"*. **That is wrong.** I read the exit status of the backgrounded *wrapper command*,
not of the script. Measured with `${PIPESTATUS[0]}` on the script itself: **exit 1**.

### What is actually true, measured on both trees

| tree | invocation | exit | RED line |
|---|---|---|---|
| `origin/main` `e2ae4d5a31` | full `precision-gates.sh` | **1** | nine gates |
| this branch | `precision-gates.sh --changed` | **1** | **byte-identical nine gates** |

    RED: q0-anchor flip · q0-anchor refill ratchet · import-time dps ratchet ·
         never-raises-dps ratchet · float64-padding ratchet · q0-value drift ratchet ·
         CODATA stale-edition · hardcoded braid word (self-test) · mixed mpf/f64 → serializer

**Identical on both**, so the red is **pre-existing on `main`** and this branch adds nothing
to it. The attribution also holds independently: the script's own header says *"the ratchets
are corpus-wide, not per-file, so there is nothing to scope down"* — `--changed` decides
only **whether** to run — and this branch's sole `computations/` addition is an integer-only
probe that writes no witness and is **named zero times** in the gate output.

### Two non-answers on the way there, both worth recording

1. **`git checkout --detach origin/main && bash scripts/precision-gates.sh`** short-circuited
   on a dirty tree, so `&&` skipped the gates entirely. The output file did not exist and the
   job log was empty — a comparison that never ran and would have been reported as one.
2. **`--changed` on detached `main` exits 0 and that is NOT a green.** The log reads
   *"precision-gates: 0 relevant of 0 changed file(s) — skipped."* Nothing changed, so it
   short-circuits. Reporting that as "main is green" would have repeated the original error
   in the same turn.

**The lesson is one line: `exit 0` from a wrapper, a pipeline, or a short-circuit is not a
verification.** Capture the status of the thing you are claiming about — `${PIPESTATUS[0]}`,
or run it unpiped — and read the log to confirm it did work rather than skipping.

### Blast radius

The claim appears in **#6899's merged body** and in this PR's body; both are corrected, the
merged one by comment since its body is the record. It reached **no committed file on this
branch**. Two older audits carry the same sentence from prior sessions —
`2026-08-26-cable-shift-deficit-lives-in-multidim-channels.md:195` and
`2026-08-21-ladder-phase-from-wedderburn-weights.md:293` — and are **not swept here**: they
may have been true when written, and re-measuring the gate history is a separate job. Flagged
so the next agent does not cite them as evidence that the gates were ever green.

### And a repo-level cost, measured three times this session

`precision-gates.sh` **rewrites audit witnesses as a side effect of running** — eight on the
first pass, six more on the second, four on the third. None are the runner's work. The
session's stop hook then reports "uncommitted changes … please commit and push", and
following it commits other people's regenerated witnesses. That is exactly how seven of them
reached a pushed commit on #6899 before being caught. **Stage by explicit path; never
`git add -A` after running the gates.**
