# NA-Stokes transverse pairing on multi-generator words: is it super-pairwise?

**Date:** 2026-08-09 · **Bean:** `qou-prjo` (deuteron Δ_λ magnitude) — stays **OPEN**
**Branch:** `claude/nastokes-multigen-additivity-2026-08-09`

> **STATUS: IN PROGRESS.** Stub committed to open the PR. Findings land as they
> are measured.

## The question

[#4848](https://github.com/litlfred/qou/pull/4848) closed the transverse
NA-Stokes pairing on **single-generator** `(2,L)`-torus channels (the deuteron
`pn` word `σ₁³`): the germ `q`-curvature is an `Ad(ρ(σ₁))`-eigenvector, all
transported curvatures lie on one line, and `Ω₂^⊥ ≡ 0` for every intersection
form and every handle assignment — scope-(b), Lean-proved.

It explicitly left **multi-generator words (`A ≥ 3`) untouched**. This audit
runs that case with the conventions #4848 pinned (Yekutieli ordered partial
products; Seifert bands ↔ crossings; the logarithmic `q`-derivative germ) and
asks the question the bean actually gates on:

> Is the determined multi-generator pairing **additive** over links (⇒
> pairwise-capped, dead by [#4818](https://github.com/litlfred/qou/pull/4818)'s
> `seifertBettiOne_link_additive`) or **super-pairwise**?

`free_parameters = 0`; AME is a post-hoc comparison only, never an input.
