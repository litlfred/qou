---
# qou-f8lit
title: MostowRigidity.figureEight carries a truncated literal, not the exact Vol(4_1)
status: todo
type: task
priority: high
tags:
    - hyperbolic-volume
    - lean
    - precision
created_at: 2026-08-29T19:10:00Z
updated_at: 2026-08-30T13:58:14Z
parent: qou-8mtd
---

## The defect

`QOU/Encounter/MostowRigidity.lean:235`

    volume := 2.02988321281930   -- :leanval[Vol_4_1]{precision=15}

is a **15-significant-digit truncation**. The corpus records the exact value one
directory over, `QOU/Knot/FigureEightVolume.lean:88`:

    VOL_4_1         := 2 * Cl_2 (π/3)                       -- exact
    VOL_4_1_decimal := 2.029883212819307250011597804990     -- approximation carrier

They differ at the **16th significant digit**. So, in the corpus's own terms,

    volumeInvariant FigureEight  ≠  VOL_4_1

even though both are supposed to name the hyperbolic volume of the same manifold.

## Why it bites (not merely cosmetic)

`QOU/Knot/FigureEightTriangulation.lean` proves, **sorry-free**,

    figureEightTriangulation.volume = VOL_4_1

So instantiating `Encounter.MostowTriangulationBridge.figureEight_literal_eq_triangulation_volume`
— whose conclusion is `(2.02988321281930 : ℝ) = T.volume` — at the corpus's own
`figureEightTriangulation` forces a **false** conclusion. Its hypotheses are therefore
jointly unsatisfiable there: **no correct `HyperbolicVolumeBridge FigureEight` instance
can ever discharge them.**

That theorem is sound, derived, and sorry-free, and it is unusable at the one knot it
names. It is the vacuity trap `ManifoldVolumeBridge` documents — a degenerate model
satisfying every statement — reappearing one file later in the *numbers* rather than in
the relation. Worth internalising: **checking a carrier for degenerate models is not
finished when the relation is fixed; the constants can carry the same defect.**

## Done (2026-08-29)

- `QOU/Encounter/FigureEightVolumeBridge.lean` — the figure-eight statement keyed on the
  **exact** constant, so it applies: `vol_eq_VOL_4_1_of_realises`,
  `vol_eq_two_clausen_of_realises`, and `vol_pos_of_realises` / `vol_ne_zero_of_realises`
  — **positivity DERIVED** from `QOU.Knot.Cl_2_pi_div_three_pos`, closing (for this shape)
  the gap `ManifoldVolumeBridge` deliberately left open.
- The sibling theorem's docstring now carries the correction and points here. Kept rather
  than deleted, because the defect is instructive.

## Still open

1. **Exactify the Mostow instance** — `figureEight.volume := VOL_4_1` instead of the
   decimal. Blocked on three things, none hard but none free:
   - `volume_nonneg := by norm_num` must become a real proof (have:
     `Cl_2_pi_div_three_pos`);
   - `unknot_volume_lt_figureEight_volume` and `figureEight_volume_lt_knot5_2_volume`
     currently discharge by `norm_num` / `rfl` **on the literals** and would need
     genuine bounds on `Cl₂(π/3)`;
   - the `:leanval[Vol_4_1]{precision=15}` codemod contract (`codemod-leanval.ts`) syncs
     that literal from `hyperbolic-volumes.witness.json`; a symbolic value has to be
     taken out of the codemod's scope deliberately, not silently.
2. **Prove the inequality** `2.02988321281930 ≠ VOL_4_1` in Lean. Currently only a
   *numerical* observation — separating them needs a rigorous 16-digit lower bound on
   `Cl₂(π/3)`, which the corpus does not have. Do NOT state it as a Lean fact until it is.
3. **Audit the other `:leanval` literals** for the same truncation class — `vol_5_2`
   (`2.82812208833078`) is the obvious next one, and `VOL_5_2 := 3 * BlochWigner_lob
   fiveTwoShape` is exact in `Knot/FiveTwoVolumeConstant.lean`. Same shape of defect,
   unverified.

---

## 2026-08-30 — the `:leanval` audit, run. The defect class is BOUNDED.

Follow-up item 3 ("audit the other `:leanval` literals") is done. **16 sites, 7 keys.**

| key | sites | exact closed form in corpus? | verdict |
|---|---|---|---|
| `Vol_4_1` / `vol_4_1` | 7 | **yes** — `2·Cl₂(π/3)` | **DEFECT** (15- and 11-digit truncations) |
| `vol_5_2` | 2 | **yes** — `3·BlochWigner_lob fiveTwoShape` | **DEFECT** (15-digit truncation) |
| `m_p_MeV` | 1 | no — CODATA measurement | not a defect |
| `m_e_MeV` | 3 | no — CODATA measurement | not a defect |
| `q_0` | 2 | no — root of a transcendental eq; the 50-dps witness IS canonical | not a defect |
| `mostow_gap_4_1` | 1 | no — a deliberate conservative under-approximation | not a defect |

**The discriminator, stated so nobody "fixes" the wrong half:** a truncated literal is a
defect only where the corpus **also** carries an exact closed form for the same quantity
*and* something treats the two as interchangeable. A CODATA mass has no closed form to
disagree with; truncation is the correct representation of a measurement. `mostow_gap`
is deliberately loose. Only the two hyperbolic volumes qualify.

**`vol_5_2` confirmed to carry the identical defect.** `MostowRigidity.knot5_2.volume
:= 2.82812208833078` against exact `2.8281220883307831627638988092766…` — diverging at
digit 16 — and `fiveTwoTriangulation_volume : fiveTwoTriangulation.volume = VOL_5_2` is
proved sorry-free, so the unsatisfiability argument transfers verbatim.

### Done: `QOU/Encounter/FiveTwoVolumeBridge.lean`

`vol_eq_VOL_5_2_of_realises`, `vol_eq_three_blochWigner_of_realises`, and
`vol_lt_iff_of_realises` — the last stated as an **equivalence**, not an inequality,
because the corpus does not carry `VOL_4_1 < VOL_5_2` as a proved fact:
`MostowRigidity`'s comparison discharges by `norm_num` on the two **truncated literals**,
which is a statement about the decimals rather than about the constants.

### ⚠ The 4₁ positivity was a SPECIAL CASE, not the start of a pattern

`FigureEightVolumeBridge.vol_pos_of_realises` exists; the 5₂ analogue **does not, and
that is the honest outcome**. The 4₁ proof went through `Cl_2_pi_div_three_pos`, which
exists only because the 4₁ shape sits on the unit circle so its Bloch–Wigner value *is*
a Clausen value. The 5₂ shape is a root of `X³ − 2X² + 3X − 1` and is not.

Measured: the corpus has **no** `0 < BlochWigner_lob z` for `0 < z.im`. What it has is
`BlochWigner_lob_real_eq_zero` — vanishing *on the reals*, the opposite boundary.

So the general positivity `ManifoldVolumeBridge` declined to assume is still open.
Recorded explicitly because "we proved it for 4₁" invites the assumption that 5₂
follows.

### Still open, unchanged

1. Exactify both Mostow instances (`figureEight` and now `knot5_2`) — still needs real
   bounds for the comparison theorems and a deliberate `:leanval` codemod decision.
2. The inequalities as Lean facts (needs rigorous 16-digit bounds).
3. General `0 < D(z)` on the upper half plane.

---

## 2026-08-30 — follow-up item 2 is NOT "more digits". It is blocked by the method.

I recorded item 2 as *"needs a rigorous 16-digit lower bound on `Cl₂(π/3)`, which the
corpus does not have"*. That was right not to assert the inequality, but it understates
the obstacle in a way that would send the next agent down a dead end. Measured:

**The corpus DOES have certified bounds** — `QOU/Knot/ClausenValueBounds.lean`
(bean `qou-44ma`, 222 lines, **0 sorries**):

    abs_Cl_2_pi_div_three_sub_le : |Cl₂(π/3) − (414173156523019011/707846096282124800)·√3| ≤ 1/24
    abs_VOL_4_1_sub_decimal_lt   : |VOL_4_1 − VOL_4_1_decimal| < 1/10

built from a 24-term partial sum plus the crude tail `|sin| ≤ 1`, `Σ_{k>N} 1/k² ≤ 1/N`.

**The cost of closing the gap with that skeleton:**

| quantity | value |
|---|---|
| current certified bound on `Cl₂(π/3)` | `1/24 ≈ 4.2e-2` |
| literal-vs-exact gap to separate | `≈ 7.25e-16` |
| needed bound on `Cl₂(π/3)` | `≈ 3.6e-16` |
| **partial-sum terms `N` required** | **`≈ 2.8 × 10¹⁵`** |

The file's own note — *"Tightening to more digits is a longer partial sum plus a sharper
tail — same skeleton"* — is true of the **skeleton** and wildly optimistic about the
**cost**. A `Finset.range` of 2.8e15 cannot be elaborated. This is not a longer
computation; it is a different method.

**Not impossible, though — do not record it as refuted.** The tail bound throws away the
period-6 sign structure `sin(kπ/3) ∈ {√3/2, √3/2, 0, −√3/2, −√3/2, 0}`. Grouping in
blocks of six gives cancellation and a much faster-converging series, so a feasible route
plausibly exists. The corpus simply does not take it, and nobody should assume the
existing skeleton scales. **Scope-(a) negative: this construction, alone, cannot reach
16 digits — not a structural exclusion.**

### What this changes about the plan

**Exactify; do not try to prove the literal wrong.** Removing the literal
(`figureEight.volume := VOL_4_1`) needs no bounds at all for two of its three blockers —
`volume_nonneg` and `unknot_volume_lt_figureEight_volume` both fall straight out of
`Cl_2_pi_div_three_pos`, which is already proved. Only the cross-knot comparison
`figureEight_volume_lt_knot5_2_volume` needs real analysis, and it needs a **lower bound
on `VOL_5_2`**, not a tighter one on `Cl₂(π/3)`:

    VOL_4_1 < VOL_5_2  ⟺  2·Cl₂(π/3) < 3·D(y₁)  ⟸  D(y₁) > (2/3)·Cl₂(π/3) ≈ 0.6766

and there is no bound on `BlochWigner_lob fiveTwoShape` in the corpus at all. Note the
regular-tetrahedron maximum gives `VOL_5_2 ≤ 3·Cl₂(π/3)`, which is the **wrong
direction** and does not help.

So the ordered plan is: (i) a certified lower bound on `D(y₁)`; (ii) then
`VOL_4_1 < VOL_5_2`; (iii) then exactify both instances and retire the literals — at
which point item 2 becomes moot, because there is no literal left to be unequal to.

---

## 2026-08-30 — step (i) scoped: the route to `D(y₁) > 2/3·Cl₂(π/3)`, and where it stops

Measured the whole chain before attempting it. **It is a formalization project, not a
session task**, and the obstacle is specific enough to name.

### The numbers

`fiveTwoShape` is the non-real root of `X³ − 2X² + 3X − 1`:

    real root r  = 0.4301597090        (f(0.4) = −0.0560,  f(0.45) = +0.0361)
    y₁           = 0.7849201455 + 1.3071412787i
    |y₁|         = 1.5247025799
    D(y₁)        = 0.9427073628        target: > 0.703413      margin 34 %

The margin is comfortable — a bound good to ~1 % suffices. Accuracy is **not** the
problem here (unlike item 2, where 16 digits were needed).

### Step-by-step feasibility

| step | what | verdict |
|---|---|---|
| 1 | bracket the real root `r` by IVT on explicit rationals | **easy** — `f(0.4) < 0 < f(0.45)`, `norm_num` closes it |
| 2 | `Re(y₁) = (2−r)/2`, `\|y₁\|² = 1/r` from the factorisation (root sum 2, product 1) | **easy algebra** |
| 3 | the three tetrahedron angles `1.030019, 1.407715, 0.703858` (sum `= π` ✓) | needs certified `arctan` bounds — moderate |
| 4 | certified `Λ` at those three angles, `Λ(θ) = ½Σ sin(2kθ)/k²` | **THE OBSTACLE** |
| 5 | combine → `D(y₁) > 0.7034` | trivial once 4 lands |

### Two things that close off the obvious shortcuts

**The Li₂ power series DIVERGES at `y₁`.** `|y₁| = 1.5247 > 1`, so the direct
`Im Li₂(y₁)` route is not available at all — this is why the corpus uses the *extended*
`cLiTwoExt`. Anyone reaching for a dilogarithm partial sum here will find it does not
converge.

**The angles are not rational multiples of π.** This is what makes step 4 hard, and it
is exactly the property that made the 4₁ case easy. `ClausenValueBounds.lean` gets an
*exact rational multiple of √3* for its partial sum because `sin(kπ/3) ∈ {±√3/2, 0}`
repeats with period 6. At `θ = 1.030019…` there is no closed form for `sin(2kθ)`, so a
certified partial sum needs **interval arithmetic on `sin` at irrational arguments** —
machinery the corpus does not have. The tail is fine (≈50 terms for 1e-2); it is the
*head* that is the problem.

### Why `fiveTwoShape` currently admits no numeric bound at all

`realRoot := Classical.choose SaddleRoots.exists_real_root` — obtained from the
intermediate value theorem, so it is **non-constructive by construction**. Grepped: the
only fact about it anywhere is `fiveTwoShape_im_pos`. There is no bracket on `.re`, `.im`
or `|·|`. Step 1 above is therefore not optional bookkeeping — it is what first gives the
constant any numeric handle, and it is independently useful.

### Recommendation

**Do step 1 and 2 as a standalone brick** (`fiveTwoShape` re/im/modulus brackets). They
are cheap, sorry-free, unblock any later numeric work on 5₂, and are worth having
regardless of whether step 4 is ever attempted. **Do not start step 4** without first
deciding whether to build a general certified-`sin` interval facility — that is its own
project and would serve far more than this one theorem.

**Scope-(a) negative, not (b):** nothing here shows `VOL_4_1 < VOL_5_2` is unreachable.
It shows the *currently available* machinery does not reach it.

---

## 2026-08-30 — EXACTIFIED. The defect is fixed, not merely recorded.

`MostowRigidity.figureEight.volume` is now `VOL_4_1`, not `2.02988321281930`. There is
no decimal left to be unequal to.

### I had scoped this as blocked, and I was wrong about why

The recorded blocker was `figureEight_volume_lt_knot5_2_volume` needing `VOL_4_1 <
VOL_5_2`, hence a **lower** bound on `VOL_5_2` the corpus does not have. That assumed
both instances had to move together. **They do not.** Exactifying only the 4₁ side turns
the comparison into

    VOL_4_1 < 2.82812208833078

— an **upper** bound on `VOL_4_1`, which the existing certified bracket already gives:
`|Cl₂(π/3) − c·√3| ≤ 1/24` ⟹ `VOL_4_1 < 2.1103`, with **0.72 headroom**. The missing
lower bound was only ever needed if both sides were exact.

All three consumers now discharge from proved facts instead of `norm_num` on decimals:

| consumer | now derived from |
|---|---|
| `volume_nonneg` | `Cl_2_pi_div_three_pos` |
| `unknot_volume_lt_figureEight_volume` | `Cl_2_pi_div_three_pos` |
| `figureEight_volume_lt_knot5_2_volume` | `abs_Cl_2_pi_div_three_sub_le` |

### The typechecker made the defect visible — keep this

`MostowTriangulationBridge`'s theorem concluded `(2.02988321281930 : ℝ) = T.volume` and
**compiled**, because `volumeInvariant FigureEight` was *definitionally* that literal.
After exactification Lean reported:

    has type      volumeInvariant FigureEight = T.volume
    but expected  2.02988321281930 = T.volume

**A truncated literal standing in for an exact constant is invisible precisely while it
is the definition.** No audit catches that by reading the file; replacing the definition
is what surfaces it. The theorem is re-keyed on `VOL_4_1` and renamed
`figureEight_volume_eq_triangulation_volume` — it is now **applicable** at the corpus's
own `figureEightTriangulation`, which it never was.

### Also fixed: MostowRigidity was UNPINNED

It carries the corpus's manifold-volume instances and had **zero** axiom-guard entries.
Seven added — the guard is exactly what would catch a regression from these proofs back
to `norm_num` on literals.

### Scope kept honest

- `mostow_gap := 0.5` **keeps its literal deliberately** — a conservative
  under-approximation of the true gap, not an approximation *of* anything exact, so it
  is not in the defect class.
- The `:leanval[Vol_4_1]` tag is removed from the exactified field only: nothing left to
  sync.
- **The 5₂ side is unchanged and still carries the truncation.** Making it exact still
  needs the `VOL_5_2` lower bound, and that still routes through certified `Λ` at angles
  that are not rational multiples of π. Unchanged, still open.
- A **third** carrier exists: `Archimedean/HyperbolicVolumeTranscendence.vol_4_1 :=
  figureEightEntry.volume.value`, its own registry entry, whose comment says it "uses the
  identical value". Not touched, not audited against the exact constant.

---

## 2026-08-30 — `VOL_4_1_decimal` was WRONG, and I had been quoting it as exact

Chasing the third `Vol(4₁)` carrier turned up a defect worse in kind than the truncation
this bean is named for.

### The finding

    canonical 2·Cl₂(π/3)  = 2.0298832128193072500424051085490…
    VOL_4_1_decimal (was) = 2.029883212819307250011597804990     ← WRONG from sig fig 21
    MassDerivation (24 d) = 2.029883212819307250042408           ← correct, err 2.9e-24

`VOL_4_1_decimal` — the corpus's *designated approximation carrier*, the thing
`abs_VOL_4_1_sub_decimal_lt` certifies against — presented **30 digits of which only 20
were right**, error `3.08e-20`. Verified by three independent routes: `2·Cl₂(π/3)`,
`6·Λ(π/3)`, `2·Im Li₂(e^{iπ/3})`, all agreeing to 30 places.

**A truncated literal is correct but short; this was incorrect and long.** The extra
digits invite exactly the trust a short value would not get — and the corpus disagreed
with itself, since `MassDerivation.vol_figure_eight` carried the right value at 24
digits all along.

**Nothing in Lean was unsound.** `abs_VOL_4_1_sub_decimal_lt` bounds the gap by `1/10`,
and `3.08e-20 < 1/10` comfortably, so the theorem held either way. That is the point
worth keeping: **a coarse certified bound does not protect a decimal's digits.** The
bound was doing its stated job and could not have caught this.

### I propagated it

I quoted `…011597804990` as "the exact value" in `MostowRigidity`'s new comment, the
`FigureEightVolumeBridge` header, and this bean. All corrected. Corrected in
`FigureEightVolume.lean` and `ClausenValueBounds.lean` too.

**One near-miss worth recording:** my first pass was a blanket string replace, which also
rewrote the *historical* note in `VOL_4_1`'s docstring recording what the definition used
to be — the bad value. That falsified the record. Restored, with the old value left in
place and annotated. A historical note that silently adopts a later correction stops
being a record.

### Prior art — the corpus knew about the family, not this instance

Corpus-grepped before claiming novelty. Bean `qou-jgew` found **seven** wrong hand-typed
`Vol(4₁)` values in one session and named this one "the bad 8-file literal";
`docs/audits/2026-06-21-q0-clusterD-and-vol41-fixes.md` fixed one `.py` probe. **Neither
drain reached the Lean carrier.** So this is a known family with a live member in the
most authoritative place it could have been.

(That audit calls the value "wrong at the 16th sig-fig". Measured here it is the **21st**,
error 3.08e-20 not ~1e-16. The audit's figure was about a different file's variant.)

### Still live, not fixed here

Six `computations/` sites carry the sibling variant `2.0298832128193072500115970029`
(`mmu_r9_two_rung_v2_probe.py`, `mmu_simpler_form_search_probe.py`,
`mmu_categorical_correction_first_probe.py`, `mmu_categorical_correction_refined_probe.py`,
`mmu_r9_two_rung_extension_probe.py`, `mmu_r9_consistency_check.py`) plus the committed
witness `mmu-categorical-correction-first-probe.witness.json`. Fixing those needs producer
re-runs and is out of this branch's scope. **Note the variant differs from the Lean one**
(`…0115970029` vs `…011597804990`), so a grep for one does not find the other.

---

## 2026-08-30 — a VALUE-based detector, and what it caught that grep never could

`scripts/known-constant-literal-audit.py`. Every prior drain of this defect class was a
grep for a specific digit string, and every one missed the sites spelling the same wrong
number differently — the Lean carrier had `…011597804990` while `computations/` had
`…0115970029`, so **a grep for either misses the other**. This script instead finds every
sufficiently-long decimal literal, asks which canonical constant it is nearest, and
checks whether its own digits are right. Constants are **computed**, not transcribed —
a hard-coded table would reproduce the defect one level up.

It distinguishes **truncated** (a correct prefix; correct but short — usually deliberate)
from **WRONG** (digits disagree before the literal ends; incorrect *and* long, which is
worse because the extra digits invite trust).

### It over-flags, and the rate is measured

Raw: **191**. Of those **123 (64 %) were `witness.json` numeric outputs** — a probe's
computed estimate of a constant *should* differ from the exact value; that is the
measurement, not a defect. After gating JSON on whether the *key names* the constant
(so a transcribed `"vol_4_1": …` is still caught), and excluding the script's own
docstring: **92 candidates**. Still high-recall, still agent-confirmed. Three legitimate
classes remain in the output by design — historical records of known-bad values, float64
reprs recorded deliberately, and converging estimates quoted in prose.

### The catch: a live wrong constant in a mass formula

`content/quantum-observable-universe/mass-theory/nuclear-knot-classification.lean`
lines 28 and 30:

    bindingScale .satellite = m_e * 7.327724753846269
    bindingScale .borromean = m_e * 7.327724753846269

against `Vol(B₃) = 8·G = 7.327724753417752120…` — **wrong from digit 11**, abs err
`4.3e-10`. Every other Lean carrier (`building-block-knots.vol_borromean`,
`categorical-neutron`, `categorical-proton`) already had `7.32772475341775`, so this file
was the outlier, not an alternative convention. Corrected; the file's one theorem is
about `classifyByMassNumber`, not the literal, so nothing depended on it.

### The part that matters: an audit declared this axis CLEAN while it was live

The corpus had already **identified** the value —
`computations/snappy_borromean_volume.py` tabulates it as "**wrong** at digit 11". And
`docs/audits/2026-06-21-constant-consistency-axis2-clean.md` declared the axis clean on
the ground that it *"survives only as a comment in `experimental_constants.py`, wrong-tail
variants only in `_deprecated/`"*.

**That verdict was false.** The value was live in executable Lean, in a mass formula, at
two sites. The audit was evidently scoped to `computations/` and never looked at
`content/**/*.lean` — the same detector-blindness shape AGENTS.md catalogues elsewhere.
**A "clean" verdict is only as wide as the surface the detector walked**, and that audit
did not say which surface it walked.

### Not fixed here

The six `computations/` sites with the `…0115970029` variant, plus one committed witness.
Fixing those needs producer re-runs, and **this container has no numpy and no scipy**
(established earlier this session), so re-running would write degraded witnesses. Left
deliberately.

Also: the sidecar `nuclear-knot-classification.qa.json` cannot be refreshed here —
folio-assistant is not set up, so `qa-sweep` is unavailable. The Lean change is
`lean`-direct verified; the sidecar refresh is owed.

---

## 2026-08-30 — the second Lean family: a false precision CLAIM

The detector's other Lean cluster. `2.029883212819307250042408` at six sites
(`MassDerivation` ×2, `KnotTheory` ×2, `Calculations`, `HyperbolicVolumeTranscendence`),
carrying the docstring claim *"24 dps verified (OEIS A091518)"*.

    true to 24 dp : 2.029883212819307250042405
    literal       : 2.029883212819307250042408

**Wrong at exactly the digit it claimed to have verified.** err `2.9e-24` — numerically
harmless, and a false precision claim regardless. This is the value I earlier called
"correct" when comparing it against `VOL_4_1_decimal`; it *is* correct to 2.9e-24, and
its final digit is still wrong. Both statements are true and only one of them is what
the docstring asserts.

Corrected at all six. Safe: the only dependent proof is
`vol_figure_eight_approx : |vol_figure_eight − 2.029883| < 1e-6`, whose tolerance exceeds
the change by 18 orders of magnitude. Both modules `lean`-direct exit 0.

### Running tally of this defect class, all one root

| carrier | was | error | status |
|---|---|---|---|
| `MostowRigidity.figureEight.volume` | 15-digit truncation | — | **exactified** to `VOL_4_1` |
| `VOL_4_1_decimal` | wrong from sig fig 21 | `3.1e-20` | **corrected** |
| `nuclear-knot-classification` `Vol(B₃)` ×2 | wrong from digit 11 | `4.3e-10` | **corrected** |
| `vol_figure_eight` family ×6 | wrong at 24th dp | `2.9e-24` | **corrected** |
| `MostowRigidity.knot5_2.volume` | 15-digit truncation | — | open (needs `VOL_5_2` lower bound) |
| six `computations/` sites + 1 witness | wrong from sig fig 21 | `3.1e-20` | open (needs producer re-runs; no numpy/scipy here) |

Four distinct wrong values for two constants, spread across nine files, none of which a
grep for any one of them would have found. That is the argument for the value-based
detector, not the individual fixes.

---

## 2026-08-30 — the `.py` surface triaged: 30 blocked, 1 fixed, 1 correctly left alone

Of 32 distinct `computations/*.py` files the detector flagged, **30 emit witnesses** and
cannot be fixed here — they need producer re-runs, and this container has no numpy or
scipy, so re-running would write degraded numbers. Two were safe to edit.

**Fixed — `two_quark_volume_weighted_clean.py:77`.** `V_BORROMEAN = 7.327724753417960`
against `8·G = 7.3277247534177521204` — wrong from digit 13, abs err `2.079e-13`. It is
labelled *"from SnapPy canonical values"*, but SnapPy gives `…417752` at that precision;
this was a transcription slip, not a SnapPy variant. No committed witness, so the fix is
self-contained.

**Left alone deliberately — `alpha_em_lean_vs_compute_divergence_probe.py:270.**
`2.82812208832975` for Vol(5₂) is 1.03e-12 off canonical, and it is **not a defect**: the
docstring says the table is *"the corpus's own volume table plus five more hyperbolic
knots"*, its neighbours are 8–9 significant-figure census values (`6_1` at
`3.16396322888`, `6_2` at `4.40083251`), and the test being run is whether `Vol(K)/G` is
an integer — a question 1e-12 cannot affect. It is a **deliberate mirror** of the corpus
table, and "correcting" it would break the mirror the probe is built on. Same class as
the convention-C audit's deliberate C-named comparisons.

That is 1 fix and 1 dismissal out of 2 examined — a reminder that the detector's output
needs reading, not applying.

### Pre-existing red, NOT from this branch

`scripts/precision-gates.sh --changed` reports the **float64-padding ratchet** at
`NEW (not baselined): 4` (17 padded occurrences, 14 distinct values, 7 files, 2 live,
baseline 13). Verified pre-existing: the same 4 appear on a clean tree with this
branch's changes stashed. Not this arc's regression, and not silenced — draining it is
whoever owns those witnesses. The **raw-float64 ratchet is clean for this branch**:
NEW 0, REGRESSED 0.

### A separate defect noticed, not fixed

`two_quark_volume_weighted_clean.py` computes in **plain Python floats**
(`V_FIG8 = 2.0298832128193072` is a `float`, not an `mpf`), which the "PROBES ARE NOT
EXEMPT" rule (AGENTS.md, owner directive 2026-08-18) makes a defect in its own right.
Fixing it means carrying `mpf` through the whole cost computation — a different change
from correcting a constant, and out of this branch's scope. Recorded so it is not lost.

## 2026-08-30 — re-verified the other five axis-2 rows; 1 was false

Closing the flag this arc left on
`docs/audits/2026-06-21-constant-consistency-axis2-clean.md`. That flag read
*"none has been re-run against `content/`"* about the five surviving ✅ rows.
**It was an unmeasured absence.** Four of the five had been re-verified by
independent arcs before I wrote it.

    Vol(Hopf)=0   HOLDS   every executable carrier is literally 0; no nonzero
                          literal anywhere binds a Hopf-volume name
    Catalan G     HOLDS   covered by known-constant-literal-audit.py (computes
                          mp.catalan, walks content/**/*.lean)
    m_mu/m_e      DRAINED qou-7ot6 closed 2026-08-22; qou-wn1w wired
    m_mu (MeV)    DRAINED codata_corpus_literal_scan.py --strict as BLOCKING,
                          widening --changed to content/**/*.{lean,ts}.
                          Re-run on main 2026-08-30: CODE 0.
    q-bracket     FALSE   see below

**Row 4 is genuinely false, and the corpus found it three weeks before I
flagged it as unchecked.** `qou-qint` (2026-08-08): 55 q-integer definitions
under ~15 aliases — 43 balanced, 10 geometric, 1 geometric-in-`q²`, 1 ℤ-poly —
and the bare name `qInt` **defined in 18 files meaning BOTH conventions**. Two
single-line witnesses:

    QIntegerFactorial.lean:37   def qInt … := ∑ i ∈ range n, q ^ i     GEOMETRIC
    degree-two-baryon-weight.lean:22
                                abbrev qInt … := QOU.QInteger.qIntBal q n  BALANCED

Not cosmetic: `qIntBal` is bar-even, the geometric form is not, so a geometric
`[n]` inside a bar-even quantity breaks parity bookkeeping silently. Fixed at
`lean/QOU/MathlibExt/QIntegerCanonical.lean`; `qou-qint` stays `todo` at its
stated consolidation ceiling (the residue are guarded / ℤ- / ring-indexed
variants that are *different functions*).

### Two additions to this arc's lesson

1. **A verdict is only as sharp as its PREDICATE, not only its surface.** Row 4's
   surface was fine. Its question — *"is any def unbalanced?"* — structurally
   could not see *"is any NAME both?"*. That needs classify-by-body then
   group-by-name. Same shape as the `markovZ` overload AGENTS.md documents.
2. **An audit's canonical COLUMN ages.** This audit certifies `206.7682830`;
   PR #4860/#5149 made that the *stale* CODATA-2018 value on 2026-08-09. The ✅
   decayed without anyone touching the row. Record the edition, not the digits.

### Defect in my own measurement, recorded not quietly fixed

First classifier took an 8-line body window. Every migrated site carries a
**bridge lemma** right after it, so the window swallowed the bridge and
inherited its convention — it labelled `QCollatz.lean:46` BALANCED when that
site's own docstring says *"Bridge to the canonical GEOMETRIC bracket"*, and
left 22 of 82 unclassified. The tell was disagreeing with docstrings written by
the people who did the migration. The two witnesses above are single-line
bodies chosen so no window can contaminate them.

**Third time in this arc that a claim of mine was an unmeasured absence** (after
"no numpy/scipy" and "the producers are unblocked"). The pattern is specific: I
report the *absence of evidence I did not look for* as evidence of absence.

## 2026-08-30 — the FOURTH unmeasured absence, and the only one that landed

Immediately after #6084 merged, I picked up the two follow-ups I had named as
"next" and measured them. **Both claims were mine, both were false, and one of
them was already on `main` inside this arc's own correction.**

    claimed: chi-std-pernucleon-closed-form.lean "is still red [on main], and
             still carries an unrouted Z-index bracket at line 104"
    measured: EXIT 0, zero sorries; the site routes at the canonical module
             via a sorry-free bridge (qNum_eq_qIntBal, line 114)

    claimed: scratch.lean "holds a q-integer definition nothing checks"
    measured: nothing checks it (true -- no .ts/.md sibling, no importer, not
             in QOU.lean) but it is NOT an unrouted duplicate: it is
             `qNumberSym q n := qIntBalZ q n`, an alias for the canonical
             Z-index form, and it is green

I produced the first by reading `qou-qint`'s three-week-old `ALSO FOUND` line
and restating it. I did not open the file. Had I done so I would have hit, four
lines under the site I called unrouted, a docstring reading *"it is migrated
now that the two closed-form theorems above are proved."*

### Why this one is worse than the first three

The other three unmeasured absences in this arc ("no numpy/scipy", "the
producers are unblocked", "none re-checked against `content/`") were caught
before or during the PR and corrected in it. **This one I wrote into the
correction itself** — the `qou-qint` addendum whose thesis is *"an open bean's
stated blocker is a claim with a date on it"* — and merged it.

So the arc now contains its own counterexample: a durable artifact repeating a
stale claim, inside the paragraph explaining how durable artifacts repeat stale
claims. That is not irony worth enjoying, it is evidence the failure is
*structural rather than attentional*: I was maximally primed against this exact
error and still made it, because the cost of restating a secondary source is
zero and the cost of opening the file is one command — so the default wins
unless the rule is mechanical.

### The mechanical rule

**Before asserting a file's build state, `lean`-direct it. Before asserting a
site is unrouted, open the site.** A bean, an audit ✅, a sibling's finding, and
a docstring are all *secondary*. For "is this red?" the only primary source is
the compiler.

And the companion, applied here rather than assumed: **`EXIT 0` with no output
is the same shape as a check that examined nothing.** The green above was
established by injecting a deliberate error (`(1:Nat) = 2 := rfl`) and
confirming `EXIT 1` at the right line, then restoring. Same discipline
`qou-wn1w` records for gates.

### Net effect on the arc's open items

Both items I listed as "next" are **closed as non-issues**, and the second one
*strengthens* `qou-qint`: `scratch.lean` is a live consumer of `qIntBalZ`, so
the ℤ-index migration is not merely unblocked but partly already done.


---

## 2026-08-30 — the ⚠ section's CONCLUSION is now stale; its REASONING is not.

`QOU/Encounter/FiveTwoVolumeBridge.lean` now carries `VOL_5_2_pos`,
`vol_pos_of_realises` and `vol_ne_zero_of_realises`, all `lean`-direct exit 0 and
axiom-clean (`propext, Classical.choice, Quot.sound`; no `sorryAx`), plus
`vol_lt_of_realises` — the inequality itself rather than its transport.

**Separate the two claims in that section, because only one moved.**

*Still true, unchanged:* the corpus has **no** `0 < BlochWigner_lob z` for `0 < z.im`.
The 4₁ route through `Cl_2_pi_div_three_pos` really does depend on the 4₁ shape sitting
on the unit circle, and the 5₂ shape really is not on it. Item 3 of "Still open" —
general `0 < D(z)` on the upper half plane — is untouched. Anyone reaching for
positivity at a *third* knot gets nothing from this.

*Now false:* "the 5₂ analogue does not exist, and that is the honest outcome."
It exists, by a route that says nothing about `BlochWigner_lob` at all:
`QOU.Knot.FiveTwoVolumeChord.VOL_4_1_lt_VOL_5_2` (bean `qou-52ch`, merged in #6141)
puts `VOL_5_2` strictly above `VOL_4_1`, and `Cl_2_pi_div_three_pos` bounds `VOL_4_1`
from below. Positivity at 5₂ is a *comparison* result, not a special-value result.

**Item 2 of "Still open" is closed, and NOT the way this bean predicted.** It was
recorded as blocked on "rigorous 16-digit bounds", then re-scoped to "blocked by the
method". Both were about the *digit* route. What closed it was Rivin's strict concavity
of the ideal-tetrahedron volume applied along the chord from the regular shape to the
5₂ shape — the constants are never approximated at any point, so no digit bound was
ever needed. The obstacle was real for the route being attempted and irrelevant to the
route that worked; recording that distinction because "blocked by the method" reads as
"blocked", and it was not.

Item 1 (exactify both `MostowRigidity` instances) is unchanged.
