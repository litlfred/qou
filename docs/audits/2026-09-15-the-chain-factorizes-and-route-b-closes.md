# The production chain factorizes exactly — so route (b) has nothing to work with

> **Scope note (2026-11-19, port onto main).** This audit was carried from PR #7418,
> which was written on 2026-09-15 and never merged. Since then the owner ruled
> (2026-11-15) that the γγ selection rule also covers the nuclear bond letters, so
> `atom_braid_word_3A` is no longer the canonical nucleus word. Read R11 (the six
> measurements on that word) as a record of a superseded word. The Lean result R12
> is stated for a generic `MarkovTrace` tower and is unaffected. Record:
> `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. File paths below
> were updated from `content/` to `folio/`; nothing else changed.


Closing audit for the arc opened in
[`2026-09-14-gamma-gamma-forces-the-layout-and-the-artin-band-fork.md`](2026-09-14-gamma-gamma-forces-the-layout-and-the-artin-band-fork.md)
(R1–R9, C1–C7). That document ended with §7 open item 4 carrying an explicit
refusal:

> 🛑 **Not settled, deliberately:** whether the corpus's one exact cross term
> (`−0.4611715803`, proton pin) is large enough. It is a difference of
> **traces**; `Z` is a **ratio**. No conversion is attempted, and the comparison
> must not be made until one is.

This audit supplies the missing conversion, measures the quantity it converts,
and then proves that the quantity is zero rather than merely small.

## Summary

| | result | scope | evidence |
|---|---|---|---|
| **R10** | The cross term's `Z`-ratio normalisation is `X = Δ / tr_free`, and the route-(b) threshold in those units is `|b₃|` itself | derived | probe 6/6 |
| **R11** | The production word carries **no** cross term — six measurements, two algebras, two pins, all at the arithmetic floor | measured | probe 6/6 |
| **R12** | **And that is a theorem, not a measurement.** The chain trace factorizes exactly; the three-body cumulant vanishes identically | (b), invariant named, **conditional on an unproved `TowerSpan`** | Lean, 23 decls, sorry-free |
| **C8** | My own claim that the join needs a new axiom beyond the disjoint-block law was **wrong** | correction | the two-line proof |
| **C9** | The corpus's own bond-product grounding cites a theorem whose hypothesis the production word **fails** | correction | verified at source |

**Net:** route (b) — "leave the bond-product family by finding a negative
three-body correction to `Z₁₂₃`" — does not exist **on this word**. The escape
requires a *different word*, and which word is selected is decided elsewhere
(`qou-ales` / `qou-99qc`), not by this arc.

## 1. R10 — the normalisation, which is what item 4 refused to assume

The §4 target was stated normalisation-free: `b₃ > 0` iff `Z₁₂₃ < f₁₂ + f₂₃ − 1`,
and the bond product overshoots by exactly `g₁₂g₂₃ = |b₃|`, cited from
`UrsellPartitionFunctionB3` / bean `qou-rwhv` as

- **0.293278112721** (³H)
- **0.190468485549** (³He)

Those are in `Z`-units — ratios. A trace deviation `Δ = tr_M(W_atom) −
tr_free·∏(z+d_e)` is not. The conversion is one line once stated: since
`Z = tr_M(W_atom)/tr_free`, a deviation `Δ` in the numerator is a deviation
`X = Δ/tr_free` in the ratio. Hence the threshold, in trace units, is
`tr_free · |b₃|`:

| nucleus | `tr_free` | threshold `tr_free·|b₃|` |
|---|---|---|
| ³H | 0.142072056797304797 | **0.041666624687904** |
| ³He | — | **0.035842101144800** |

[`cross_term_normalisation_threshold_probe.py`](../../computations/onedim/cross_term_normalisation_threshold_probe.py),
6/6. The probe records as an explicit **non-claim** that the ³H threshold sits
about 1 ppm from `1/24`; that is a coincidence of the anchors, not a structure,
and is flagged so nobody later reads it as one.

**This does not license the comparison item 4 forbade, and it must not be read
as doing so.** The corpus's exact cross term `z(z²−hz−1) = −0.4611715803243431`
lives on **three adjacent generators in `H₄`**. The conversion above divides by
*the atom word's own* free trace in `H₉`. Different word, different algebra —
dividing the `H₄` figure by `0.142` would be a category error, and no such
number appears in this audit. What the conversion does is make *the production
word's own deviation* comparable to its own threshold, which is R11.

## 2. R11 — the deviation, measured

[`production_word_cross_term_probe.py`](../../computations/onedim/production_word_cross_term_probe.py),
6/6, at 60-dps serialization:

| nucleus | A | algebra | bonds | rel. deviation (proton / muon) |
|---|---|---|---|---|
| ²H | 2 | `H₆` | 1 | 2.56e-61 / 5.12e-61 |
| ³H | 3 | `H₉` | 2 | 9.17e-61 / 5.84e-61 |
| ³He | 3 | `H₉` | 2 | 7.47e-61 / 4.98e-61 |

`tr_M(W_atom)` equals `tr_free · ∏(z + d_e)` to every printed digit. Against the
R10 threshold, at the proton pin on ³H:

```
|Δ|        = 2.67395e-62
threshold  = 0.0416666246879
|Δ|/thresh = 6.41749e-61
```

The deviation is **6.4e-61 of what route (b) requires** — i.e. zero to the
precision of the arithmetic, which at `OUTPUT_DPS = 60` is where zero lives.

Two things are deliberately absent. **⁴He is not here**: `H₁₂` has blocks to
dimension 132 and did not complete in 28 minutes at 60 dps, so it is omitted and
said so rather than estimated. And the supporting values are the **live** ones —
`tr_M(p) = 0.629328402202921918`, `tr_M(n) = 0.475133517155682213` — not the
retired `1.145759692`.

## 3. R12 — and it is a theorem

A measured zero at the arithmetic floor is consistent with a small non-zero
quantity. It is not, here:
[`SingleCrossingChainFactorizes.lean`](../../folio/quantum-observable-universe/lean/QOU/MathlibExt/SingleCrossingChainFactorizes.lean),
sorry-free.

The hypothesis is one property of a Markov trace:

```lean
def SingleCrossingJoin : Prop :=
  ∀ m : ℕ, ∀ a ∈ T.H m, ∀ b ∈ shifted T (m + 1),
    T.tr (a * T.g m * b) = T.z * T.tr a * T.tr b
```

— *a block below, one crossing, a block strictly above: the trace splits and the
crossing contributes `z`.* From it the affine letter `g_m + d·1` contributes
`z + d` (`tr_affine_letter`), the chain of any length factorizes by induction
(`tr_chainWord`), and at the production `A = 3` layout — blocks on generator
pairs `(0,1)`, `(3,4)`, `(6,7)`, interfaces the single generators `2` and `5` —

```lean
theorem three_body_cumulant_vanishes … :
    T.tr (B₀ * (T.g 2 + d₀ • 1) * (B₁ * (T.g 5 + d₁ • 1) * B₂))
        * T.tr B₀ * T.tr B₁ * T.tr B₂
      = T.tr (B₀ * (T.g 2 + d₀ • 1) * B₁)
          * T.tr (B₁ * (T.g 5 + d₁ • 1) * B₂)
          * T.tr (B₀ * B₂)
```

which is `Z₀₁₂ = Z₀₁ · Z₁₂ · Z₀₂` with the denominators cleared — the statement
that the three-body cumulant is **identically** zero, stated without division so
it holds over any `CommRing` with no invertibility hypothesis.

**What it is conditional on, stated plainly — and the file is blunter about this
than a summary would be.** `SingleCrossingJoin` is not a new axiom. It is a
theorem of `DisjointBlockMultiplicative` (`singleCrossingJoin_of_disjointBlock`)
— the law
[`DisjointBlockTraceLaw.lean`](../../folio/quantum-observable-universe/lean/QOU/MathlibExt/DisjointBlockTraceLaw.lean)
already derives from `TowerSpan` — and hence of `TowerSpan` directly
(`singleCrossingJoin_of_towerSpan`, which records the composition so the
reduction is machine-checked rather than asserted). That file's docstring says
*"Nothing here derives the bond product"*; this is what derives it.

**But `TowerSpan` is itself unproved.** Quoting the new file's own docstring:

> `TowerSpan` itself is not proved here or anywhere in the corpus, and it is not
> provable from `MarkovTrace`: the structure carries no hypothesis constraining
> how `H (m+1)` is generated, so `H` may be any monotone family of subalgebras
> containing the generators. Per AGENTS.md §"Axiomatization is NOT a Proof", the
> bond product is therefore **still not unconditionally derived** — but the
> condition is now one classical, citable structure theorem rather than two
> independent unknowns.

So the honest statement of R12 is: **a reduction, not a closure.** The bond
product and the vanishing cumulant are theorems *of `TowerSpan` plus the
quadratic relation*, and what the arc gained is that the cross-term question is
no longer independent — it collapses into a gap the corpus had already isolated.
Per AGENTS.md §"Before declaring refuted" this is a **scope-(b)** exclusion,
structural with the invariant named, and **conditional**. It is not an
unconditional impossibility claim, and it must not be quoted as one.

Two disciplines were applied and are worth recording because they are what makes
the conditional meaningful:

- **Anti-vacuity.** `markov_of_singleCrossingJoin` shows the `b = 1` case of
  `SingleCrossingJoin` *is* the stabilisation axiom (T3), so the property
  constrains `tr`, `g` and `z` jointly rather than being a predicate that
  ignores its arguments.
- **Satisfiability — and the witness is DEGENERATE, which the file says in those
  words.** `disjointBlock_unitMarkovTrace` and `tr_chainWord_unit_two` exhibit a
  concrete model, so the conditional theorems are not vacuously true for want of
  anything satisfying the hypothesis. That is *all* they establish.
  `unitMarkovTrace`'s algebra is `R` itself, where `⊥ = ⊤`, so every `shifted n`
  sits in the scalars and the disjoint-block law holds there by linearity alone —
  *"nothing about disjointness, nothing about the tower, and nothing about `g`"*.
  It exercises **none** of what the law asserts. No better witness exists in the
  corpus and none can, for the reason the parent file records against
  `towerSpan_of_constant`: **Mathlib has no Hecke tower**, so there is no tower
  with a genuinely growing filtration to test against.

## 4. C8 — my own claim that this needed a new axiom was wrong

The brief I wrote for this file asserted that the join does **not** follow from
the disjoint-block law plus the Markov axiom, reasoning that stabilisation needs
both factors in `H_m` while `b` lives above `g_m`, and that cyclicity only
yields `tr(B₀B₁·g_m)` with `B₀B₁ ∉ H_m`.

That reasoning is sound **at level `m`** and the conclusion drawn from it is
false, because the proof is at level `m + 1`:

```lean
intro m a ha b hb
have hag : a * T.g m ∈ T.H (m + 1) :=
  (T.H (m + 1)).mul_mem (T.H_mono (Nat.le_succ m) ha) (T.g_mem m)
rw [hdb (m + 1) _ hag b hb, T.markov m a ha]
```

`a * g_m` is a single left factor living in `H_{m+1}`; the disjoint-block law
applies there, and stabilisation then applies to `a * g_m` alone. Three tactic
lines, and no `mul_assoc` is even needed — `a * T.g m * b` already parses as
`(a * T.g m) * b`.

The hidden assumption in my brief was that the disjoint-block law had to be
applied **at level `m`**, where the interface sits. It is `∀ n, …` — universally
quantified over the level — and `m+1` is the level at which `a * g m` is a single
admissible left factor.

**An 8-mutant battery was run, 8/8 red against a green pristine control**, and
two of them are the ones that matter: **M8** applies the law at level `m` instead
of `m+1` (red), and **M9** groups `a*g` into `H m` (red). So the compiler
confirms that the *level choice*, not anything else, is what makes the derivation
go. Separately, `SingleCrossingJoin` and `DisjointBlockMultiplicative` each
resist `rfl` and `simp`, so neither is extensionally `True`.

**This is the second time this error has been made on this object.**
`DisjointBlockTraceLaw.lean` carries a `🛑 CORRECTED 2026-09-07` block recording
`TwoSidedMarkov` being introduced as *"the one input `MarkovTrace` does not
carry"* and then retracted as a four-line theorem of T1+T3 — the same shape, one
level down.

The generalisable form: **"this cannot be derived from X" is a claim about a
proof attempt, not about X**, and the level at which a tower law is applied is
exactly the kind of degree of freedom that makes the difference.

## 5. C9 — the corpus's bond-product grounding cites a hypothesis the production word fails

Verified at source, not relayed.
[`UrsellPartitionFunctionB3.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/UrsellPartitionFunctionB3.lean)
lines 14–19 ground the bond-product reading —

> `Z_S = ∏_{e ⊆ S} f_e` … `= tr_M(W_atom(S)) / tr_M(W_free(S))` by connected-sum
> multiplicativity of the Markov trace
> (`QOU.MathlibExt.MonotoneWordFactorizes.tr_stabWord_eq_prod_tr`; re-measured on
> the live alternating-core word in the probe, to `1e-40`)

— on a theorem whose hypothesis is

```lean
theorem tr_stabWord_eq_prod_tr (s : ℕ → A) (c : ℕ → R) (hs : ∀ m, s m ∈ T.H (m + 1))
```

i.e. the **ascending / monotone** word condition. The production word is
interleaved and does not satisfy it — which is C3 of the previous audit
(`MonotoneWordTraceFactorizes`'s docstring claim of monotonicity went stale at
the 2026-09-05 β_Bor ruling), now traced to a *downstream consumer* rather than
left as a stale docstring.

The concrete failure, from `DisjointBlockTraceLaw`'s own docstring: under owner
ruling `qou-hu1f` one nucleon's generator sequence is
`[0,1,0,1,0,1,0,0,1,0,0]`, which attains its maximal level **four times**. An
ascending word attains each level once.

The citation itself resolves (the namespace is
`QOU.MathlibExt.MonotoneWordFactorizes` while the file is
`MonotoneWordTraceFactorizes.lean`); this is not a dead reference. And the gap
was already covered *by measurement* — the file says so in the same breath, "to
`1e-40`". What was missing was a theorem for the word actually used.
`tr_chainWord` is that theorem, and it needs no ascending hypothesis: the
production layout's interfaces sit at `3k+2`, three apart, and far-commute.

## 6. What route (b) now requires

Unchanged in form, sharpened in what satisfies it. With a cross term `X` on the
two-bond chain, `b₃ = −(f−1)² − X`, so `b₃ > 0` iff `X < −(f−1)²`. R12 says
`X = 0` identically on the production word. Therefore:

**Route (b) cannot be entered by re-deriving, re-measuring or re-normalising the
production word.** It requires a word whose interfaces are *adjacent and
non-commuting*. The corpus's one exact cross term of the right sign is exactly
such a case — `z(z²−hz−1)` between the interleaved `g₀g₁g₀g₂g₁` and the
sequential `g₀²g₁²g₂` in `H₄` — which is why the previous audit recorded it as
*"evidence the family can be left at all, and it says where"*.

The normalisation probe does print the raw ratio `|Δ_H4| / threshold(³H) =
11.068129`, and it is recorded here rather than omitted, **with the scope its own
check attaches to it**: it is *"a statement about SCALE in this algebra family,
not evidence about the production word"*. An `H₄` trace difference over an `H₉`
threshold is not a comparison of like with like, and the 11 must not be read as
"the cross term is 11× big enough". It says only that cross terms of this family
are not numerically negligible where they occur — which is the reason the word
question is worth asking at all.

Whether the selected word has adjacent interfaces is the γγ / confinement-SDP
selection question (`qou-ales`, `qou-99qc`), not a free parameter of the
assembly. That is where this arc hands off.

## 7. Open

1. **⁴He.** `H₁₂` did not complete at 60 dps in 28 min. The Lean covers chains of
   any length, so nothing structural turns on it — but the measurement is absent
   and is not claimed.
2. **The band candidate set.** Unchanged from the previous audit's item 1:
   running the confinement SDP (reading 3, Frobenius positivity) over the band
   candidate set is still a compute task, and `EnumeratorSelectionDegeneracy`
   counts 27 inter-nucleon band generators in `B₉` against the 2 searched.
3. **The bridge lemma** (previous audit item 2) and **`vertexStrands` as a
   theorem** (item 3) are untouched.
4. **`qou-brng` residual (ii) is not closed and is not reached** — and per PR
   #7407 that bean's own 2026-08-30 entry declares its self-vs-mutual framing
   mis-posed, so this arc does not bear on it either way.

## Verification

CI auto-triggers are disabled repo-wide; the agent's own verification is the
gate (AGENTS.md §"QA is agent-owned").

- **Lean** — `lean`-direct with `-DautoImplicit=false -s 65536` against the real
  import cone: **exit 0**, no diagnostics, no warnings. `#print axioms` on **all
  23 declarations** individually: every one that carries axioms reports
  `[propext, Classical.choice, Quot.sound]`, **no `sorryAx`**, no
  `Lean.ofReduceBool`, no `Lean.trustCompiler`. No `sorry`, no `native_decide`,
  no `axiom` keyword, no `: True` in the file. §7c clean: zero occurrences of
  `ℝ`, `ℚ`, `Real.`, `Complex.` or `linarith` — generic `{R : Type*} [CommRing R]`
  throughout.

  Verified twice, and the second time was necessary: the first pass ran against
  the 08:35 source and the file was then edited at 08:45, so that olean was
  stale. The figures above are from a rebuild at 08:49 off the 08:45 source.
  **A `lean`-direct green is a claim about the snapshot it was built from**; this
  is that trap firing inside the very audit that cites it.

- 🛑 **The check that was NOT run.** A *semantic* necessity check — a concrete
  instance where the disjoint-block law fails and the conclusion fails with it —
  **was not constructed**, and the necessity evidence here is syntactic (the 8
  mutants) plus satisfiability plus trivial-inhabitation. There is a pen-and-paper
  argument that no small model can work (with `H n = ⊤`, stabilisation appears to
  force `g n` to the central scalar `z·1`; `Mat₂(ℚ)` with the normalised trace and
  `R × R` both collapse that way), so a counter-model would need a genuinely
  growing tower — which, again, Mathlib has not got. **That argument is not a
  machine check and must not later be quoted as though the check had been done.**
- **Probes** — `cross_term_normalisation_threshold_probe.py` 6/6,
  `production_word_cross_term_probe.py` 6/6.
- **Precision** — `scripts/precision-gates.sh --changed` → RC=1 on the standing
  baseline ratchets only. **NEW dirty witnesses: 0** on both ratchets, and
  neither new probe is named anywhere in the output. The nine contended audit
  witnesses the run rewrote were reverted **by name**, not committed
  (bean `qou-v0t8`).
- **Corpus-grep** — paths 1–6 run. **Path 0 (`corpus_search`) was unavailable**:
  `.mcp.json` routes it to `paper-assistant`, which failed `ENOENT` this session,
  so no `emptyRoots` reading was obtainable. Findings here are grep-open, not
  graph-open.

## Not reused, and why

[`EdgeDecoupling.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidKnot/EdgeDecoupling.lean)
(landed on `main` 2026-09-15) carries the same *pattern* — "the value decomposes
into within-class parts plus a cross term, and the cross term is bounded" — with
`sum_pairs_split` as its exact-splitting lemma. It is **not reusable here**: it
is an additive double sum over pairs in an `AddCommMonoid`, on the `REV_n`
objective in β-coordinates, with no shared type or statement with a Markov trace
of a product in a Hecke tower. Recorded so the parallel is visible without being
mistaken for a dependency.
