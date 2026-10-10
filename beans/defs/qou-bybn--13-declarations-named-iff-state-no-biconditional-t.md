---
# qou-bybn
title: 13 declarations named *_iff* state no biconditional -- the structure-word class, drained of its bijection member
status: completed
type: task
priority: normal
created_at: 2026-09-14T19:56:26Z
updated_at: 2026-10-10T07:32:25Z
parent: b9cj
---

Measured 2026-09-14 while exploring `qou-mfdq` Finding 3 (PR #7401, issue #7400).
**Nothing renamed here** — per AGENTS.md §"ASK THE OWNER BEFORE CHANGING THINGS",
a rename tranche across 13 declarations in 11 files is not one of the two
exemptions, so it waits.

## The class

Taxonomy row 46: a declaration whose NAME asserts a mathematical **structure**
its own **statement** does not contain. Distinct from
`scripts/lean-borrowed-name-audit.py`, which asks whether a declaration is named
after an external *body* (Seifert, Kashiwara, Donaldson) whose theorem it does
not use — that audit's gate is `hits = borrowed_hits(name, doc); if not hits:
continue`, and a name borrowing *content words* rather than an eponym never
reaches it.

The type case was `pole_cusp_bijection_proved` (renamed to
`denomPolyLocal_roots_explicit` in #7371). Measured with
`scripts/lean-structure-word-audit.py`, it was the **sole** `bijection` member at
`926f2c71ec^` and the token is now empty — so that half of the class is drained.

## The 13 live members, all under one token

`*_iff*` with **no `↔` and no `Iff` anywhere in the statement OR the proof**
(verified against the whole declaration body, so not a parser artifact):

| file:line | declaration | what the type actually says |
|---|---|---|
| `mass-theory/q-pochhammer-partial-product.lean:66` | `denomPoly_root_iff` | one direction: `1 - x q^k = 0 → denomPoly q x n = 0` |
| `mass-theory/figure-eight-branching-rule.lean:96` | `figure_eight_b_zero_iff_row_or_col` | one direction |
| `lean/QOU/ColorTubeFibers.lean:50` | `mem_iff_shift_root` | hypothesis → a polynomial identity; no "mem" either |
| `lean/QOU/PAdicQuantumGroups.lean:87` | `padic_observability_iff_irreducible` | a single `∀`; neither named property appears |
| `lean/QOU/PAdicQuantumGroups.lean:170` | `unit_root_iff_skew_poisson_integrable` | `∀ y ∃ x, frobenius x = y` — Frobenius **surjectivity** |
| `lean/QOU/BringsSurface/BarLiftAmbiguity.lean:156` | `invLift_defect_eq_zero_iff` | conclusion is `≠ 0` — the name says `eq_zero` |
| `lean/QOU/Mass/LowerBoundCannotConstrainADifference.lean:113` | `diff_bounded_collapses_iff_saturated` | one direction |
| `lean/QOU/Mass/QGaugeSpectralRigidity.lean:215` | `gauge_scaling_fixes_colorCubic_iff` | hypothesis → `t = 1` |
| `lean/QOU/BraidKnot/PartitionLex.lean:306` | `partitionDom_not_iff_lexGt` | **defensible** — refuting one direction refutes the iff |
| `lean/QOU/SchurWeyl/OffDiagNonvanishing.lean:45` | `offDiag_eq_zero_iff` | one direction |
| `lean/QOU/Eightfold/NonetMixingUnconstrained.lean:128` | `no_mixing_iff_eigenvalues_are_diagonal` | a `charPoly` identity; no "no mixing" predicate |
| `lean/QOU/QBeta/FiveTwoEnvelopeWiring.lean:272` | `exp_saddle_iff_curve` | hypothesis → `curve x y = 0` |
| `lean/QOU/QBeta/WindingLatticeNormForm.lean:130` | `parity_flip_iff_golden` | a **conjunction** of two facts, not a biconditional |

**12 of 13 are genuine over-namings; `partitionDom_not_iff_lexGt` is defensible.**
The two `PAdicQuantumGroups` ones are the sharpest — same shape as
`pole_cusp_bijection_proved`, a name asserting properties the type does not
mention.

## Why it matters here specifically, and it is not style

Mathlib's convention is that `foo_iff_bar` **is** an `↔`; a one-directional
lemma is `bar_of_foo`. So the name is a claim about what was proved. An agent
running the corpus-grep checklist to ask *"is X ⟺ Y established?"* finds a
sorry-free `X_iff_Y` and stops. That is the trap `qou-mfdq` documents for
`pole_cusp_bijection_proved`, one token over.

`denomPoly_root_iff` is in the same arc: its converse is in fact true over a
domain (a product vanishes iff a factor does) — so the honest options there are
*prove the converse* or *rename to `_of_`*, and they are different amounts of
work.

## Options

1. **Rename all 12** to Mathlib style (`_of_`, `_imp_`, or drop the token).
   Cheap per site, 11 files, zero mathematical risk. Needs `lean`-direct on each
   changed file plus consumer updates; several are library modules with
   importers, so the blast radius is real and must be measured per site first.
2. **Prove the missing directions** where they are true (`denomPoly_root_iff`,
   `offDiag_eq_zero_iff` are the plausible ones) and rename the rest. More work,
   strictly better outcome, and it turns a naming defect into content.
3. **Do nothing.** The 13 stay, the audit keeps reporting them, and the
   corpus-grep trap stays live. Nothing downstream moves — none of these is
   cited as evidence for a physical claim as far as I measured.

**Recommendation (judgement, not a finding): option 2 for the two in the
`q-pochhammer` / `SchurWeyl` arcs where the converse is true and cheap, option 1
for the rest, as one reviewable tranche.** But it is a rename tranche across
library modules and it is the owner's call to start it.

## Reproduce

    python3 scripts/lean-structure-word-audit.py --token iff
    python3 scripts/lean-structure-word-audit.py --selftest

`--selftest` hardcodes nothing: it fails unless `pole_cusp_bijection_proved` is
the sole `bijection` hit at `926f2c71ec^`, unless that token is empty now, and
unless the Mathlib uniqueness idiom is NOT flagged.


## 2026-10-10 — DISPOSITIONED on owner go-ahead: 10 renamed, 2 REMOVED, 1 left alone

Owner authorised the tranche (PR #7546, branch
`claude/triangulation-citation-chain-2026-10-10`). The naming class is drained;
the token `iff` now reports only the one defensible member.

**The split is not 12 renames.** Two of the three "sharpest" members above were
the wrong shape for a rename, and the corpus had **already ruled on them** —
`PAdicQuantumGroups.lean` carries its own
`### Removed 2026-08-30 — self-assuming projections` note deleting a sibling for
exactly this. Both bodies are a projected `PAdicQOU` field **verbatim**:

    theorem padic_observability_iff_irreducible (pq : PAdicQOU) : … :=
      pq.frobenius_irreducible
    theorem unit_root_iff_skew_poisson_integrable (pq : PAdicQOU) : … :=
      pq.frobenius_surjective

A theorem whose body is `:= pq.field` asserts nothing beyond the structure it
unpacks. **Renaming it launders it** — it would turn a vacuous projection into a
correctly-named vacuous projection, which is worse, because the honest name is
then indistinguishable from a real lemma. The recorded disposition for the
sibling is verbatim *"drop the pseudo-theorem and project the field at use
sites"*, so that is what was done. Note also that the first name one reaches for,
`frobenius_surjective`, **collides with the very field it projects** — the
collision is the tell.

Both removed in `9c71bcda58`; a `### Removed 2026-10-10` note appended in the
file's existing format.

### The 10 renames (`a48ba4e4da`)

    denomPoly_root_iff                     -> denomPoly_eq_zero_of_factor_eq_zero
    figure_eight_b_zero_iff_row_or_col     -> row_or_col_degenerate_of_skewSYTCount_eq_zero
    mem_iff_shift_root                     -> shiftedCubic_eq_zero_of_cubic_eq_zero
    invLift_defect_eq_zero_iff             -> invLift_defect_ne_zero
    diff_bounded_collapses_iff_saturated   -> diff_eq_of_bounds_saturated
    gauge_scaling_fixes_colorCubic_iff     -> eq_one_of_gauge_scaling_fixes_colorCubic
    offDiag_eq_zero_iff                    -> eq_one_or_neg_one_of_offDiag_eq_zero
    no_mixing_iff_eigenvalues_are_diagonal -> charPoly_zero_mixing_eq_linear_factors
    exp_saddle_iff_curve                   -> curve_eq_zero_of_saddle
    parity_flip_iff_golden                 -> norm3_pell3_eq_one_and_normPhi_goldenPow

Each new name states what the type states: `_of_` for the one-directional
implications, `_ne_zero` where the conclusion is `≠ 0` against a name saying
`eq_zero`, `_and_` for the conjunction. `parity_flip_iff_golden` is the clearest
win — a conjunction of two facts was wearing a biconditional's name.

**`partitionDom_not_iff_lexGt` is left alone**, as the table above predicted:
refuting one direction refutes the iff, so the name is defensible. It is also the
calibrating negative named in `scripts/lean-structure-word-audit.py`'s own
docstring, so renaming it would silently weaken the audit.

### Blast radius — MEASURED, and my first measurement was blind

**All 13 members have zero consumers**, so every rename is file-local. But the
first sweep grepped `*.lean` only, which **cannot see a `lean.ref` in a `.ts`
manifest** — the §0a package-qualified URI is how a content block cites a
declaration, and it is not Lean source. Re-measured across `.ts`, `.md`, `.json`
and `.py`: two load-bearing non-Lean references exist in the corpus generally,
neither to any of these 13. Same detector-blindness class as everything in
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`: the obvious file glob
was the blind spot.

### Verification

`lean -DautoImplicit=false -s 65536` on each of the 11 changed files:
**10 of 11 `errors=0`**. The eleventh, `QGaugeSpectralRigidity.lean`, carries one
error **proved pre-existing** — a missing `QOU.Mass.PalindromicInvolutionLift.olean`,
byte-identical message on the unmodified file restored from git. Warning counts
baselined pre = post (4 and 2).

A bare `lean` is **not** the gate: it does not read the lakefile, so
`autoImplicit` defaults back to `true` and an unbound identifier silently
auto-binds instead of erroring. The first pass of this verify loop also treated
*any* output as failure and reported two files as FAILED on `unused variable`
**warnings**; re-run keyed on `error:`.

### NOT done — the content half

The recommendation above was **option 2** (prove the missing directions) for the
two members where the converse is in fact true, and **option 1** (rename) for the
rest. What landed is option 1 for all ten. So the two converses remain unproved:

- `denomPoly_eq_zero_of_factor_eq_zero` — a product vanishes **iff** a factor
  does, over a domain. The converse is true and cheap.
- `eq_one_or_neg_one_of_offDiag_eq_zero` — the plausible second case.

Proving either turns a naming defect into content and would restore a *correct*
`_iff_`. Spun out rather than left implicit in a closed bean.

### Taxonomy

Row 49's worked example is **removed, not renamed** — recorded in
`docs/audits/2026-08-15-detector-blindness-taxonomy.md` (`46d7c21b2a`), together
with the stale "table is at 47 rows" line, which was two rows behind.
