---
# qou-2u39
title: building-block-knots.lean asserts Vol(4_1) = a truncated decimal with an equals sign
status: completed
type: bug
priority: normal
created_at: 2026-08-30T15:04:15Z
updated_at: 2026-08-30T15:35:44Z
---

Found while exactifying `MostowRigidity.knot5_2` (bean `qou-f8lit` item 1, PR #6263). Two
`:leanval[Vol_4_1]` truncation sites survive outside the `Encounter` chapter; both were
assessed and **only one carries a defect, and it is not the exactification defect.**

## The two sites

    observations/building-block-knots.lean:43
      /-- Vol(4₁) = 2.02988321281930 (figure-eight, exact: 2·Cl₂(π/3)). -/
      noncomputable def vol_figure_eight : ℝ := 2.02988321281930  -- :leanval[Vol_4_1]{precision=15}

    knots-particles-confinement/knot-particle-generation.lean:71
      /-- Vol(4₁) = 2·Cl₂(π/3) ≈ 2.0298832128 (figure-eight knot, muon). -/
      noncomputable def vol_figure_eight : ℝ := 2.0298832128  -- :leanval[Vol_4_1]{precision=11}

## The defect: one docstring asserts `=` where the claim is false

`building-block-knots.lean` writes *"Vol(4₁) **=** 2.02988321281930 ... exact:
2·Cl₂(π/3)"*, putting an equals sign between a 15-digit truncation and the exact form it
names in the same sentence. They differ at the 16th digit. `knot-particle-generation.lean`
writes `≈` and is correct.

This is the AGENTS.md §7ab rule (`$\approx$`, never `$=$`, for a derived numerical value)
applied to a Lean docstring. One-character fix: `=` → `≈`.

## What is NOT wrong: these should NOT be exactified

The `MostowRigidity` defect was specific — a bridge statement keyed on the literal was
**unsatisfiable** against the sorry-free `figureEightTriangulation.volume = VOL_4_1`. There
is no such equality here. Both sites are **tables of numerical constants** whose other
entries are decimals or `0` (`vol_trefoil := 0`, `vol_cinquefoil := 0` — non-hyperbolic),
feeding numerical mass computations rather than exact comparisons. Exactifying one entry of
a decimal table makes the table inconsistent and buys nothing.

Recording that assessment explicitly, because "two more `:leanval[Vol_4_1]` sites" reads
like remaining drain from the same arc and it is not.

## Why it is not fixed in #6263

Different chapter, and these are content-block Lean with `.qa.json` sidecars — the fix is
one character but its verification path is `qa-sweep` on the touched criteria, which is
heavier than the change and unrelated to that PR's scope (strict `0 < D(z)`).


---

## 2026-08-30 (same day) — MEASURED. My assessment above was inferred, not checked, and it is wrong in its reasoning. There is also a larger defect I missed.

I wrote that both sites are *"decimal constant tables … feeding numerical mass computations
rather than exact comparisons"* after reading about twelve lines around each. Then I checked.

### 1. `building-block-knots.lean` is NOT a table. It is the CAL-2 muon anchor.

`vol_figure_eight` there feeds `muon_mass`, `muon_electron_ratio q = vol_figure_eight /
(hbarQ q)²`, and a **proved theorem**:

    theorem muon_electron_ratio_from_substrate :
        |muon_electron_ratio q₀ - 206.768| < 1

That is `m_μ/m_e = Vol(4₁)/ℏ_q²` — the CAL-2 pin of the canonical derivation chain, not an
inert constant.

### 2. The verdict "not the exactification defect class" SURVIVES, for a different reason.

Not because it is a table, but because the consumer is a **tolerance bound**, not an
equality. A 15-digit truncation differs from exact `2·Cl₂(π/3)` by ~1e-16, immaterial against
a bound of ±1. The `MostowRigidity` defect was a literal keyed against a *sorry-free exact
equality*, which made bridge statements unsatisfiable; nothing here is unsatisfiable.
**Right answer, wrong reason — and the wrong reason would have misled the next agent about
what to look for.**

### 3. THE REAL DEFECT, which I missed entirely: the docstring overclaims by 4.5×.

    /-- At the CODATA substrate parameter q₀, the muon-electron mass
        ratio matches the experimental value 206.768 to within 0.001. -/
    theorem muon_electron_ratio_from_substrate :
        |muon_electron_ratio q₀ - 206.768| < 1

Measured at `mp.dps = 40`, `q₀ = 1.10998`, `ℏ_q = 1 − 1/q₀`:

    ratio           = 206.763525398207
    |ratio − 206.768| = 0.0044746018

So **0.001 is false** — the true deviation is 4.5× larger — and the theorem proves `< 1`,
which is 1000× looser again. The prose claims a bound that is neither true nor proved.

This is the same species as the `mostow_gap` defect found in the same session (`qou-f8lit`):
**prose asserting more than the Lean carries, on a field or theorem where nothing checks the
prose.** Two instances in one day suggests looking for the pattern rather than the instance.

Fix is a choice, and it is the author's: either state `0.005` in the docstring (true, and
still not what the theorem proves), or tighten the theorem to `< 0.005` and say so. Do **not**
write `0.001` in either.

### 4. Two of the three literals are DEAD.

- `knots-particles-confinement/knot-particle-generation.lean:71` — `vol_figure_eight :=
  2.0298832128`, declared and referenced **nowhere**, in that file or any other.
- `mass-theory/terminal-resolution.lean:47` — `vol_figure_eight := 2.02988`, a **6-digit**
  literal carrying **no `:leanval` tag at all**, so whatever syncs those tags cannot see it.
  Also referenced nowhere.

Only `building-block-knots.lean`'s is live. So the population is three, not two, the untagged
one is the coarsest, and the drain here is mostly deletion rather than exactification.

### Scope

Still not fixed on #6263 — different chapter, sidecar verification path, and item 3 is now an
author decision rather than a mechanical fix.


---

## 2026-08-30 — the recommendation is no longer judgement. MEASURED in Lean, all three compile, exit 0.

I offered three options and said option 2 "may or may not take" a 200× tighter tolerance.
Tested it instead. Reduced harness (`/tmp/tighten2.lean`, the four definitions copied
verbatim from the file):

    theorem tight : |muon_electron_ratio q₀ - 206.768| < 0.005 := by
      simp only [muon_electron_ratio, vol_figure_eight, hbarQ, q₀, abs_lt]
      constructor <;> norm_num                                    -- ✓ compiles

    theorem tighter : |muon_electron_ratio q₀ - 206.768| < 0.00448 := by
      simp only [muon_electron_ratio, vol_figure_eight, hbarQ, q₀, abs_lt]
      constructor <;> norm_num                                    -- ✓ compiles

    theorem docstring_claim_is_false : ¬ (|muon_electron_ratio q₀ - 206.768| < 0.001) := by
      simp only [muon_electron_ratio, vol_figure_eight, hbarQ, q₀, abs_lt, not_and_or]
      left; norm_num                                              -- ✓ compiles

Three things follow, and they change the shape of the decision:

1. **Option 2 costs nothing.** The tightened bound proves with the *identical* one-line
   tactic the loose one uses. No new lemma, no `nlinarith`, no bracket. The arithmetic is
   rational and exact, so `norm_num` does not care how tight the tolerance is.
2. **`0.00448` also proves** — a bound **224× tighter** than the committed `< 1`, and
   within 0.03 % of the true deviation `0.0044746`. So the theorem can state essentially
   the exact bound, not merely a defensible one.
3. **The docstring's `0.001` is refuted by Lean**, not merely contradicted by an mpmath
   computation. It is a false statement, machine-checked as false, sitting on the CAL-2
   anchor.

**Revised recommendation, now evidence rather than preference: tighten the theorem to
`< 0.00448` and set the docstring to match.** Option 1 (docstring → `0.005`) was offered
as the cheap path and is now strictly dominated — it costs the same edit and leaves the
prose still claiming more than the Lean carries, which is the defect pattern this bean
exists to record. Option 3 (do nothing) leaves a Lean-refutable claim in the corpus.

The direction matters and is worth stating: the ratio is **below** `206.768`
(`206.763525398207`), which is why the refutation discharges on the `left` disjunct. An
agent writing the negation with `right` gets `⊢ False` and may conclude the claim is true.


---

## 2026-08-30 — FIXED in #6280 (items 1 and 3); item 4 deliberately left

- **The `=` → `≈`** on the `Vol(4₁)` docstring (AGENTS.md §7ab). Done.
- **The overclaim.** `muon_electron_ratio_from_substrate` now states `< 0.00448` — the
  measured bound to within 0.03 % — and the docstring says the same. The tightening cost
  nothing; the tactic is unchanged.
- **A regression guard.** `muon_electron_ratio_not_within_thousandth` proves the old `0.001`
  claim FALSE, so it cannot silently return. Discharges on the `left` disjunct because the
  ratio sits *below* `206.768`.
- **The two dead literals: NOT removed.** Neither is referenced and neither `.md` sibling
  mentions them, but deleting an expository constant from a content block is a judgement
  about the exposition, not a cleanup — and `terminal-resolution.lean`'s sits immediately
  above the CODATA constants in a file whose subject is `m(K) = Vol(K)/ℏ_q²`, where having
  `Vol(4₁)` visible is plausibly deliberate. Left for the author. The `terminal-resolution`
  one carries **no `:leanval` tag**, so it can drift from the canonical witness with nothing
  syncing it; that is the part worth acting on if anyone does.

Verified: `lean`-direct exit 0, `check-sidecars` clean, sidecar refreshed.
