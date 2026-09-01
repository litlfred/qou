# The fourteen `infra-blocked` verdicts, individuated

**Date:** 2026-08-31 · **Follows:** `2026-08-30-infra-blocked-is-one-verdict-stamped-fourteen-times.md` · **PR:** #6249

The companion audit established that one verdict — *"Infra-blocked: needs Mathlib theory that
does not exist. Track upstream"* — was stamped on fourteen beans in six seconds, and was wrong
on the one item that had been tested. This is the per-item pass it called for.

## Result: at least four distinct causes, and "missing upstream Mathlib" is one of them

| bean | target | actual cause |
|---|---|---|
| `qou-m3xr` | `sum_dimSYT_eq_involution` | **NOT blocked** — proved, no RSK needed (#6164/#6249) |
| `qou-o29t` | `covariance_kernel_conjecture` | **open QOU conjecture** — nothing to do with Mathlib |
| `qou-t28w` | `q_NS_wellposedness` | **millennium-class open problem** |
| `qou-fj8u` | `numSYT_mul_hookProduct` | Mathlib lacks it — but **buildable in-repo** |
| `qou-9gpo` | `confinement_frobenius_reciprocity` | **class carries the conclusion** (see below) |
| `qou-etfq` | `lp_dual_stability` | **class carries the conclusion** |
| `qou-ygyx` | `operator_selection_lp` | **class carries the conclusion** |
| `qou-vs2i` | `shell_filling_*` | mixed; two entries are plain in-repo combinatorics |
| `qou-apcl` | `confinementSDP` | class-structured; not re-checked in detail |
| `qou-l2xx` | `elliptic_divisor_degree_zero` | genuinely upstream (argument principle) |
| `qou-p494` | hyperbolic volume independence | genuinely upstream (transcendence) |
| `qou-xt9z` | single volume irrationality | genuinely upstream (transcendence) |
| `qou-bsqw` | `seminormalVector_base_exists` | genuinely upstream (Jucys–Murphy); 20 `sorry` tokens in file |
| `qou-phl4` | 3 entries in one file | 1 of 3 disproved; other 2 untouched |

So the verdict is right for roughly four of fourteen, and wrong or misleading for the rest —
not because the absence claims are false, but because **absence was recorded as cause**.

Two cases deserve their own note.

**`qou-o29t` is not a Mathlib gap in any sense.** Its own docstring reads *"**CONJECTURE
(OPEN).** … verified `k ≤ 30` computationally. Not proved."*, and its carrier is
`class CovarianceKernelConjecture : Prop where nonpos : ∀ k, kernelValue k ≤ 0` with no
instance. That is precisely the honest representation AGENTS.md §3b prescribes for an open
primary conjecture. Advising "track upstream" on it is simply wrong: no Mathlib release will
ever close a QOU conjecture.

**`qou-fj8u` (hook-length formula) is the clearest "wrong advice, true premise".** Mathlib
indeed has no hook-length formula. But the corpus has `YoungDiagram`, `StandardYoungTableau`,
the branching rule and now `upSum_eq` — the formula is in-repo work, and "track upstream" tells
the next agent to wait for something nobody is building.

## Correction to yesterday's audit: the blind area is not only tactic-mode

`2026-08-30-the-tactic-mode-self-assuming-blind-area.md` said the term-mode detector's blind
area is the documented `:= by …` exclusion. **That was incomplete.** Three of the fourteen are
missed by `scripts/lean-self-assuming-audit.py` while being *term-mode*, for two further
reasons:

1. **Conjunctive anonymous constructor.** `confinement_frobenius_reciprocity` is
   `⟨ctx.reciprocity, ctx.primal_nontrivial, ctx.y_0_star_pos, ctx.A_star_nonempty, …⟩` —
   six conjuncts, six class fields. `lp_dual_stability` is the same with four. The detector
   requires the *entire* proof term to be one identifier or projection, so an `⟨…⟩` of
   projections never matches.
2. **∀-instantiation.** `covariance_kernel_conjecture … := hi.nonpos k`, where the field is
   `nonpos : ∀ k, kernelValue k ≤ 0` and the goal is `kernelValue k ≤ 0`. The detector requires
   the conclusion to be *syntactically* the hypothesis type; an instantiation is not an
   identity, so it is excluded by the "conclusion differing in any way" rule.

So the shapes the drain's sizing does not cover are at least: tactic-mode (documented),
term-mode conjunctive, and ∀-instantiated. The 112 figure in `qou-z9ws` should be read
accordingly.

## The trap in widening the detector: missed ≠ defective

`covariance_kernel_conjecture` is missed by the detector **and is not a defect**. It is an
honest open-conjecture carrier — content-bearing class, no instance, docstring saying "Not
proved". §3b sanctions exactly that.

`confinement_frobenius_reciprocity` looks different: its class field is literally named
`reciprocity` and *is* the theorem's first conjunct, which is §3b-cond rule 5's
conclusion-carrier. But distinguishing the two needs a judgement about whether the fields are
*hypotheses* or *the conclusion*, and that is not syntactic.

**Consequence for anyone widening the scanner:** every new shape it catches will mix genuine
conclusion-carriers with honest conjecture carriers, and the ratio is not knowable from the
syntax. Do not treat a widened hit list as a defect list.

## Recommended action

Replace the boilerplate on the ten items where it is wrong or misleading. Suggested per-class
wording:

- open conjecture → *"Open QOU conjecture. Not a Mathlib gap; no upstream release closes it."*
- in-repo buildable → *"Mathlib lacks X, but X is buildable here from <named parts>. Do not track upstream."*
- conclusion-carrier → *"Not blocked: the class carries the conclusion. Belongs to the `qou-z9ws` drain."*
- genuinely upstream → keep, and name the specific library.

Applied: six beans re-triaged, four marked confirmed, originals kept.

## Addendum — the three "not re-checked" items, now checked

**`qou-apcl` — verdict CONFIRMED.** Mathlib has no SDP/conic-duality API and that is the
required input. Separately notable: this file *already carried* the conclusion-carrier defect
and a prior agent already fixed it — its in-body comment records that the proof "previously
read `exact HasConfinementSDPData.strong_duality`, projecting a `strong_duality` field the DATA
class carried … **Both were false**". The field is deleted; the theorem now takes Slater as a
real argument plus a separate, legitimate `[HasConfinementSDPStrongDuality n h]`.

**The two `qou-phl4` entries — both accounted for, and the tiers are the real finding.**
`skew_le_straight` is **proved unconditionally** (`YoungTableauStandard.lean:587`, four lines).
`branching_two_one` is open with a checked route (`qou-b21r`).

**This sharpens the whole audit.** The cataloguer assigned tiers **per entry**, and only tier-B
("infra-blocked") entries got the "Track upstream" verdict. `skew_le_straight` and
`branching_two_one` were tier **P** ("repo-infra-dependent") — and that was *correct*; one of
them has since been proved. So the defect is not that fourteen items were lumped together. It
is that **some genuinely in-repo items were mis-tiered into B**, and B carries advice that is
actively wrong for in-repo work.

The contrast sits inside one file: `skew_le_straight` (P) got proved; `sum_dimSYT_eq_involution`
(B) sat for a month and needed nothing upstream at all. The tier decided the advice, and the
advice decided whether anyone tried. `qou-fj8u` (hook-length) is the same mis-tiering.
