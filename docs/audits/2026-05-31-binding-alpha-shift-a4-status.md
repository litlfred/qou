# Binding α_shift A=4 status — queue item already closed on main

**Authored:** 2026-05-31
**Branch:** `claude/alpha-shift-a4-binding-2026-05-30` (PR opening with this commit)
**Trigger:** Picking up multi-pick queue item #4
(α_shift A=4 `BindingForceCarrierKnot` instance via §3b-cond)
revealed the work is already on `main`.

## Headline

Queue item #4 is **complete on `main`** at the structural-Lean level.
The `lightNucleiForceCarrierKnot` instance in
[`content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean`](../../content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean#L251)
covers A ∈ {2, 3, 4} in a single sorry-free `rfl` proof:

| A | nucleus | T(p, k) | `lightNucleusP` | `lightNucleusK` | α_shift = k(p−1) |
|--:|---------|---------|---:|---:|---:|
| 2 | D       | T(2,3)  | 2 | 3 | 3 |
| 3 | T / ³He | T(2,5)  | 2 | 5 | 5 |
| 4 | ⁴He     | T(3,4)  | 3 | 4 | 8 |

The §3b-cond field `matches_alpha_shift` is discharged definitionally
since
`lightNucleusAlphaShift A = bindingAlphaShift (lightNucleusP A) (lightNucleusK A)`
holds by `rfl` for every `A`.

## Relevant commits on main

| commit | message |
|---|---|
| `addde9da` | binding: A≥3 via α_shift universal chain + per-rep Reeb phase wiring |
| `31faefe5` | review(#1464): refactor binding theorems to consume BindingForceCarrierKnot per §3b-cond |
| `55c60949` | binding(deuteron): concrete BindingForceCarrierKnot instance for T(2,3) |
| `917b2e6a` | binding(light-nuclei): consolidate four-nucleus force-carrier instance into binding-alpha-shift-extension |
| `16535431` | binding(light-nuclei): simplify lightNucleusAlphaShift to definitional composition per Gemini review |

## What is actually still open

Per the file's own status section
([lines 192-198](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean#L192-L198)):

> **Status.** These are CANDIDATE identifications, not derived
> uniqueness theorems. Phase 3 closure — proving each `(p_A, k_A)`
> is the substrate's unique choice — requires the per-nucleus
> `H_{3A}(q)` Wedderburn-block minimisation queued alongside the
> meson force-carrier identification. This block provides the
> instance scaffolding; substrate-uniqueness is the remaining
> open math.

So the genuinely-open follow-ups are:

1. **Substrate-uniqueness of `(p_A, k_A)`** — research-grade Phase 3
   closure via per-nucleus H_{3A}(q) Wedderburn-block minimisation.
   Not actionable in a single session.
2. **A ≥ 5 candidate identifications** — would require a fresh
   Phase-3 audit table for ⁵Li / ⁶Li / ⁷Li / etc. Without the
   audit table I would be fabricating; deferred until the audit
   lands.
3. **Numerical cross-check of the current candidates** — does
   `B(A) = m_e · ρ_0 · α_shift(T(p_A, k_A))` with deuteron-pinned
   `ρ_0` actually reproduce experimental binding energies for
   A ∈ {3, 4}? This is concrete + cheap; tracked separately.

The companion commit on this branch (witness emitter
[`computations/binding_alpha_shift_witness.py`](../../computations/binding_alpha_shift_witness.py)
emitting
[`binding-alpha-shift-witness.witness.json`](../../computations/binding-alpha-shift-witness.witness.json))
addresses #3 above and reports the numerical gap honestly.

## How this finding fits the pattern

This is the **second consecutive queue item** (after Track B
Gap #2, see audit doc
[`2026-05-30-universal-branching-multinucleon-gap.md`](https://github.com/litlfred/qou/blob/claude/track-b-skew-syt-count-2026-05-30/docs/audits/2026-05-30-universal-branching-multinucleon-gap.md)
in PR [#1515](https://github.com/litlfred/qou/pull/1515),
not yet merged to `main` at the time this PR was opened)
that turned out to be already-closed on `main` once the scoping
read landed. Lesson: when picking a multi-week-old framing of
"what's next", check `git log --grep <theme>` and recent
sibling-PR scope before authoring. Per CLAUDE.md
"Coordinate intent with sibling branches on every new workplan"
+ the 5-minute idle trigger, recurring this discipline at the
start of every work tranche keeps the queue current.

## References

- [`binding-alpha-shift-extension.lean`](../../content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean) — the Lean file containing the instance.
- [`binding-alpha-shift-extension.md`](../../content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.md) — narrative.
- [`alpha-shift-torus-knot.lean`](../../content/quantum-observable-universe/mass-theory/alpha-shift-torus-knot.lean) — defines `BindingForceCarrierKnot` upstream.
- [Universal-branching-multinucleon gap audit (2026-05-30)](https://github.com/litlfred/qou/blob/claude/track-b-skew-syt-count-2026-05-30/docs/audits/2026-05-30-universal-branching-multinucleon-gap.md) (PR [#1515](https://github.com/litlfred/qou/pull/1515), not yet merged at the time this PR was opened) — analogous already-closed-on-main finding for Track B Gap #2.
- [`binding_rotation_phase_lead.py`](../../computations/binding_rotation_phase_lead.py) and its existing witness output — the probe that derived `ρ_full(D) ≈ 14.67 MeV/rad`. The numerical value is in the emitted witness, not the script source; see the script's `--out` argument for the witness path.
