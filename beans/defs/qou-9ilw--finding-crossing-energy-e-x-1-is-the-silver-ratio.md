---
# qou-9ilw
title: 'FINDING: crossing energy E_x = 1 IS the silver-ratio beta-decay null (h=2 branch); E_x=0 is the h=0 branch'
status: in-progress
pr: 8251
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:01:38Z
updated_at: 2026-10-04T15:12:36Z
parent: qou-v2om
---


## The identity

The corpus defines crossing energy per crossing as
`𝔈_×(q) = ½(q − q⁻¹)` (`binding-knots-visual-inventory.md`), and the Hecke
parameter as `h = q − 1/q`. So **`𝔈_× = h/2`**, and therefore

    𝔈_× = 0  ⟺  h = 0  ⟺  q = 1
    𝔈_× = 1  ⟺  h = 2  ⟺  q = 1 + √2   (silver ratio, q² = 2q + 1)

`prop:silver-ratio-beta-decay-null` is carried in Lean as
`QOU.ParticleInteractions.beta_decay_null_iff_h_zero_or_two`. Its two roots
`h ∈ {0, 2}` are therefore **exactly the two crossing energies 0 and 1**.

The corpus already treats the silver ratio as distinguished — `c_8, c_9, c_10`
become rational there (`prop:qbeta-c8-c10-silver-rationals`), `c_5` is a
Pell–Lucas outlier there and *not* at the golden ratio, and the σ-eigenvalues
are `1 ± √2` (self-referential fixed point). What is **not** recorded anywhere
is that this is the unit-crossing-energy point. Corpus-grep: every file
mentioning "silver ratio" and every file mentioning "crossing energy", zero
overlap outside the definition index.

## Why it is worth recording

The β-decay null is stated as a condition on `h`, which reads as an algebraic
accident. Restated as `𝔈_× ∈ {0, 1}` it reads as a physical statement: the
null occurs exactly when each crossing carries zero or unit energy. Same
theorem, and the second phrasing is the one a reader can interpret. That is a
naming/exposition fix, not new mathematics — but the corpus is a folio, and an
uninterpretable statement of a true theorem is a defect it cares about.

## What it does NOT do — do not overclaim

It does **not** connect to the volume conjecture, and the question it arose
from ("is there a limit where crossing energy = 1 and we recover the VC?")
answers **no**:

* VC lives at `|q| = 1`, `q = exp(2πi/N)`, `N → ∞` — approaching 1
  *tangentially along the unit circle*.
* `𝔈_× = 1` is `q = 1 + √2 ≈ 2.414`, real, modulus 2.414. Not on the circle;
  setting `𝔈_× = 1` moves **away** from the VC regime, not toward it.
* Worse, both β-decay-null roots are degenerate for the mass formula. At
  `q = 1`, `ℏ_q² → 0` so `Vol/ℏ_q² → ∞` (the mass term diverges). At the
  silver ratio the theorem's own content is that proton and neutron
  Markov-traces become *categorically indistinguishable* — a trace degeneracy,
  i.e. the point where the formula stops separating what it must separate.

## The limit that DOES recover the bare volume

`q → ∞`: `ℏ_q = 1 − 1/q → 1`, so `Vol/ℏ_q² → Vol` exactly. Measured:

| q | 𝔈_× | ℏ_q² | 1/ℏ_q² |
|---|---|---|---|
| q₀ ≈ 1.10998 | 0.10453 | 0.0098171 | 101.86 |
| 1+√2 | 1 | 0.34315 | 2.9142 |
| 10 | 4.95 | 0.81 | 1.2346 |
| 1000 | 499.9995 | 0.998001 | 1.0020 |
| → 1⁺ | → 0 | → 0 | → ∞ |

So the mass formula's volume term degenerates to the bare hyperbolic volume in
the large-`q` limit and diverges in the `q → 1` limit — and the VC regime sits
at the divergent end, approached along a direction the real-`q` axis never
takes.

## The real content: two non-commuting limits

This is the standard radial-vs-tangential dichotomy, and it is worth stating in
the corpus because the mass formula and the VC live on opposite sides of it:

* **radial** `q → 1` (real axis, the substrate direction) — Melvin–Morton–
  Rozansky: the colored Jones degenerates to the **Alexander** polynomial.
  Abelian/torsion data. No volume.
* **tangential** `q → 1` along roots of unity — Kashaev/VC: **hyperbolic
  volume**.

The object where both live is the **Habiro ring** (cyclotomic completion), which
is precisely what the corpus's whole `qbeta`/Habiro cluster is built on. So the
framework for asking "does the substrate ray see the volume?" already exists
in-repo; what is missing is anyone having pointed it at this question.

## Next

- [ ] Restate `prop:silver-ratio-beta-decay-null` in terms of `𝔈_× ∈ {0,1}` in
      the content block (exposition fix, same theorem).
- [ ] Record the `q → ∞ ⇒ Vol/ℏ_q² → Vol` limit somewhere a reader of the mass
      formula will meet it.
- [ ] Decide whether the radial/tangential non-commutation deserves its own
      block. It bears directly on whether the substrate pin can ever see VC.

---

## 2026-08-30 — restatement landed, and it uncovered two errors in the block

The "cheap exposition win" was not only exposition. Restating
`prop:silver-ratio-beta-decay-null` in crossing-energy terms required reading
the `.md` against its own Lean, and the two disagreed twice.

### Defect 1 — the boxed closed form was wrong

The block asserted

    Δ(net) = h(h-2)/2 = (q² − 2q − 1) / (2q)

The second equality is false. With `h = q − 1/q`,

    h(h−2)/2 = (q² − 1)(q² − 2q − 1) / (2q²)

Measured: at q = 2 the two sides are −0.375 and −0.25; at q = 3, 0.889 and
0.333. **They agree only where both vanish — at the silver ratio itself**,
which is the one point the block is about. A reader checking the identity at
the block's own subject would confirm it; the error is invisible exactly there.

### Defect 2 — the stated iff omitted a root

The prose read "vanishes if and only if $h = 2$". The block's own Lean theorem
is `beta_decay_null_iff_h_zero_or_two`: the null is `h = 0 ∨ h = 2`. Verified
`deltaNet(1) = 0` exactly. The narrative was strictly weaker than the formal
statement it carries — the reverse of the usual drift direction.

### What landed

Both fixed, and the null is now stated as `𝔈_× ∈ {0, 1}` alongside the h-form,
with a third equivalent `Δ(net) = 2𝔈_×(𝔈_× − 1)`. All three forms verified
numerically to agree at q ∈ {0.5, 1.11, 2, 3, 1+√2, 10}. The q→∞ behaviour and
the VC-regime separation are stated with their numbers.

QA: my edit initially tripped `voice-editorializing` twice ("the one a reader
can interpret", "undefined rather than merely large") — a fair catch both
times; reworded to plain statements. Final sweep is back to the pre-existing
baseline of 10 failing axes, i.e. **my change adds no new QA failure**.

### A third finding: 10 QA axes are failing on a deleted file

All 10 baseline failures on this block say a variant of "the Lean sibling
`folio/quantum-observable-universe/nuclear-interactions/silver-ratio-beta-decay-null.lean`
fails compilation / contains sorry". **That file does not exist.** Only two
copies remain — `nuclear-interactions/…` and the lake-built
`lean/QOU/ParticleInteractions/…` — and **both are sorry-free**. The block's
`.ts` correctly references `qou:QOU.ParticleInteractions.beta_decay_null_iff_h_zero_or_two`
and carries `validation: "not_checked"`, which is why nothing ever forced a
re-check.

So this block reads as ten-axes-red for a file that was moved and repaired.
`da-vacuous` in particular reports "contains 'sorry' placeholders" about
Lean that has none. That is a stale-evidence failure, not a content failure,
and it is the kind that trains readers to ignore red.

## Lean — LANDED 2026-08-30 on owner instruction, NOT type-checked here

The following extends the lake-built module. It is **not** in the tree: this
container has **no Mathlib oleans anywhere** (`find / -name Mathlib.olean` is
empty), `lake` is not installed, and no `lake-cache` branch carries them — so
`scripts/lean-direct-cone.sh` fails at `unknown module prefix 'Mathlib'`.
Pushing unverified proofs onto a branch three sessions share is not worth the
convenience, so it is parked here until someone can compile it.

Every proposition below is numerically verified (see above); what is unverified
is whether these particular *tactic scripts* close the goals.

```lean
/-- Per-crossing energy 𝔈_×(q) = ½(q − q⁻¹). -/
noncomputable def crossingEnergy (q : ℝ) : ℝ := heckeSkein q / 2

theorem crossingEnergy_eq_half_heckeSkein (q : ℝ) :
    crossingEnergy q = heckeSkein q / 2 := rfl

/-- The β-decay null is exactly zero-or-unit crossing energy. -/
theorem beta_decay_null_iff_crossing_energy_zero_or_one (q : ℝ) (hq : q > 0) :
    deltaNet q = 0 ↔ crossingEnergy q = 0 ∨ crossingEnergy q = 1 := by
  rw [beta_decay_null_iff_h_zero_or_two q hq]
  unfold crossingEnergy
  constructor
  · rintro (h | h)
    · left; rw [h]; norm_num
    · right; rw [h]; norm_num
  · rintro (h | h)
    · left; linarith
    · right; linarith

/-- Unit crossing energy pins q to the silver ratio. -/
theorem crossing_energy_eq_one_iff (q : ℝ) (hq : 0 < q) :
    crossingEnergy q = 1 ↔ q = 1 + Real.sqrt 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hs : Real.sqrt 2 * Real.sqrt 2 = 2 :=
    Real.mul_self_sqrt (by norm_num : (0 : ℝ) ≤ 2)
  have hs_pos : (0 : ℝ) < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  constructor
  · intro h
    have h2 : q - 1 / q = 2 := by unfold crossingEnergy heckeSkein at h; linarith
    have hquad : q ^ 2 - 2 * q - 1 = 0 := by field_simp at h2; nlinarith [h2]
    have hfac : (q - 1 - Real.sqrt 2) * (q - 1 + Real.sqrt 2) = 0 := by
      nlinarith [hquad, hs]
    rcases mul_eq_zero.mp hfac with h1 | h1
    · linarith
    · exfalso; nlinarith [hs, hs_pos]
  · intro h
    subst h
    unfold crossingEnergy heckeSkein
    have hden : (1 : ℝ) + Real.sqrt 2 ≠ 0 := by positivity
    field_simp
    nlinarith [hs]

/-- The unit-crossing-energy point is not on the unit circle, where the
volume conjecture's root-of-unity limit lives. -/
theorem crossing_energy_one_not_on_unit_circle (q : ℝ) (hq : 0 < q)
    (h : crossingEnergy q = 1) : |q| ≠ 1 := by
  rw [crossing_energy_eq_one_iff q hq] at h
  have hs_pos : (0 : ℝ) < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  rw [abs_of_pos hq, h]; linarith

noncomputable def hbarQ (q : ℝ) : ℝ := 1 - 1 / q
noncomputable def volTerm (V q : ℝ) : ℝ := V / (hbarQ q) ^ 2

/-- ℏ_q vanishes exactly at q = 1, the 𝔈_× = 0 root. -/
theorem hbarQ_eq_zero_iff (q : ℝ) (hq : q ≠ 0) : hbarQ q = 0 ↔ q = 1 := by
  unfold hbarQ
  constructor
  · intro h; field_simp at h; linarith
  · intro h; subst h; norm_num

theorem tendsto_hbarQ_atTop :
    Filter.Tendsto hbarQ Filter.atTop (nhds (1 : ℝ)) := by
  have h : Filter.Tendsto (fun q : ℝ => 1 - q⁻¹) Filter.atTop (nhds (1 - 0)) :=
    Filter.Tendsto.sub tendsto_const_nhds tendsto_inv_atTop_zero
  simpa [hbarQ, one_div] using h

/-- The large-q limit returns the bare hyperbolic volume. -/
theorem tendsto_volTerm_atTop (V : ℝ) :
    Filter.Tendsto (volTerm V) Filter.atTop (nhds V) := by
  have h1 : Filter.Tendsto (fun q : ℝ => (hbarQ q) ^ 2) Filter.atTop
      (nhds ((1 : ℝ) ^ 2)) := tendsto_hbarQ_atTop.pow 2
  have h2 : Filter.Tendsto (fun q : ℝ => V / (hbarQ q) ^ 2) Filter.atTop
      (nhds (V / (1 : ℝ) ^ 2)) :=
    Filter.Tendsto.div tendsto_const_nhds h1 (by norm_num)
  simpa [volTerm] using h2
```

Risk assessment for whoever lands it: the `rfl`, `rw`/`rintro` and limit proofs
are low-risk; the two `field_simp; nlinarith` steps in
`crossing_energy_eq_one_iff` and the `nlinarith [hquad, hs]` factorisation are
the ones most likely to need adjustment.

## Next

- [ ] Land the Lean above in a container that can compile it.
- [ ] Repoint or clear the stale QA evidence on this block (10 axes red for a
      deleted file). Consider whether `validation: "not_checked"` in the `.ts`
      should become a checked reference now that both live copies are
      sorry-free.
- [ ] The `q → ∞` limit deserves a home a reader of the mass formula will
      actually meet, not only this block.

---

## 2026-08-30 — Lean landed on instruction; three verification routes exhausted first

Owner: "Land the lean." Done, into the lake-built module
`QOU/ParticleInteractions/silver_ratio_beta_decay_null.lean`. CI is the first
type-checker. Before landing, verification was attempted three ways and all
three are closed in this container:

1. **No Mathlib oleans anywhere.** `find / -name Mathlib.olean` → empty.
2. **`lake` exists but cannot fetch them.** It is in the elan toolchain
   (not on PATH). `lake update` fetched the dependency *sources* fine —
   `.lake/packages` now has mathlib, batteries, aesop, … — but building
   `cache:exe` fails at link: `ld: cannot find -lleancpp`, `-lLean`. The
   toolchain ships only `libLean.a.trace` / `.hash` stubs, **not the archives**,
   so this Lean can elaborate but cannot link any executable. `lake exe cache
   get` is therefore unavailable.
3. **Source build** of the `Mathlib.Tactic` closure is hours and is the
   forbidden `lake build` path.

`lake update` left `lake-manifest.json` untouched and wrote only into the
gitignored `.lake/`; working tree verified clean afterwards.

### What IS verified

Every proposition, numerically, at `q ∈ {0.5, 1.11, 2, 3, 1+√2, 10}` and at
`q = 10^4, 10^8` for the limit. Structural check of the file: 9 new
declarations present, parens/brackets balanced, no `sorry`, namespace closed.

### What is NOT verified

Whether the tactic scripts close the goals. Before landing I hardened the two
weakest:

* `crossing_energy_eq_one_iff` — the factorisation was `nlinarith [hquad, hs]`
  on an *equality* goal, which nlinarith handles poorly. Replaced with an
  explicit `ring` expansion plus `rw [hs]; linarith`. The `field_simp at h2`
  step became a `have hmul … hexp` pair so the intermediate form is pinned
  rather than left to field_simp's normalisation.
* `crossing_energy_one_not_on_unit_circle` — **had a real bug**: the goal is
  `|q| ≠ 1` and I ended with `linarith`, which cannot close a `≠`. Now
  `intro hcontra; linarith`. Writing Lean without a compiler found this only
  on re-reading, which is the argument for not doing it.

Residual risk sits in `div_eq_one_iff_eq` (name/signature), the `simpa`
normalisations in the two limit lemmas, and `Filter.Tendsto.div`'s argument
order. If CI reddens, those are the places to look first.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 53 Formalization Update (2026-11-17)
- Formalized in `QOU.MassTheory` (`ConventionDErrorShiftAndBrunnianShortfall.lean`, `IntensiveVsExtensiveBindingAndClosureArity.lean`, `CrossingEnergyQuadraticAndBoxDiscrepancy.lean`) with 50-dps probe `computations/probes/convention_d_brunnian_intensive_arity_silver_probe.py` and witness on PR #8251.
