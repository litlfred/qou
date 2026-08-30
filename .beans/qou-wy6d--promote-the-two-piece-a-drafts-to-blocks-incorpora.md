---
# qou-wy6d
title: Promote the two Piece A drafts to blocks; incorporate bring_tetraplectic into brings-surface
status: completed
type: task
priority: normal
created_at: 2026-08-24T18:16:12Z
updated_at: 2026-08-24T19:07:57Z
---

Owner ruling 2026-08-24, superseding bean `qou-cauj`'s "probably not blocks"
disposition for three of the four paper-root `.md`: promote the two Piece A
drafts to real content blocks, and **incorporate** `bring_tetraplectic.md`
into `brings-surface/` (not merely relocate it). Branch
`claude/q407-self-assuming-projections-2026-08-21`.

## Piece A → `mass-theory`, §`sec:lp-dual-jucys-murphy` (5 blocks)

`lem:piece-a-hook-content-identity` is the shared statement
`Σ_□ h(□)² = Σ_□ c(□)² + n²`; the two drafts became the two routes to it.

* **The Specht/JM draft's Lean names all exist.** `trace_centralC2_specht_module`,
  `trace_centralC2_regular_rep`, `pieceA_hook_sq_eq_content_sq_add_n_sq` are all
  in `PieceASpechtCharacter.lean`, sorry-free. But the third **delegates** to the
  combinatorial `IdentityI.sumSqHooks_eq_sumSqContents_add_sq` — so the route does
  not prove Piece A representation-theoretically, and the block says so rather
  than presenting it as a second proof. It is `lem:piece-a-specht-character-trace`
  (the two genuine trace evaluations) plus its proof.
* **The corner-induction draft's Lean names do NOT exist — none of the seven.**
  `colLen_corner`, `hook_r_j`, `hook_i_s`, `sum_hook_r`, `sum_hook_s`,
  `sz_decomposition`, `corner_removal_obligation`: zero hits repo-wide, against a
  control (`pairCount_holds`) that resolves. Shipping those annotations would have
  put seven fabricated Lean references into the corpus. The block carries **no**
  `lean.ref` and cites a probe instead.
* `computations/probes/piece_a_corner_removal_probe.py` + witness — new. Exact
  integer arithmetic, `q0Anchor: independent`; checks all five supporting steps,
  the assembled obligation, that the obligation IS `sumHookSq(λ) − sumHookSq(μ)`,
  and that the content difference is `content(corner)²`, over every corner of
  every partition of n ≤ 16 (914 partitions, 2,455 corners). 8/8 assertions.

## `bring_tetraplectic.md` → `brings-surface`, §`sec:spectral-gauge` (6 blocks)

Split by what it actually claims: `def:bring-cone-tetraplectic-structure` (§1),
`lem:bring-cone-reeb-quaternionic-twist` + proof (§4, the one formalised piece),
`rem:tetraplectic-su2-gauge-reading` (the interpretation),
`conj:tetraplectic-askey-localisation` (§2) and
`conj:tetraplectic-sw-localisation-bridge` (§3) — both conjectural in the draft
and conjecture-kind here.

**Two Lean files stop being orphans.** No block anywhere referenced
`BringCone.lean` or `QuaternionicElectroweak.lean`; both are sorry-free and both
now carry a `lean.ref`.

**Bean `qou-8p1g`'s three findings ride on the blocks as `authorNotes`** rather
than being dropped in the promotion: `m = 1` makes the tetraplectic condition
vacuous; the triad is `dim su(2) = 3`, the *adjoint*, not a fundamental of
`SU(3)`; and that `SU(2)` is already spent on the electroweak sector.

**Nine references to the old path repointed** — `references.ts`, five `.lean`
files (incl. `BringCone.lean`'s own `[manuscript]` line), two probes — now naming
block labels. The `content/bib-qa-verifications.json` rows keep the old `target`:
they are a record of what a triage agent saw, nothing reads the field, and
rewriting a past verification would falsify it.

## Discharged in passing

* `qou-k6a4` — "Cite 0206161v1.pdf at bring_tetraplectic.md §3". Done, as
  `cites: [nekrasov2002]` on `conj:tetraplectic-sw-localisation-bridge`.
* `qou-t1ry` — "Remark interpreting 67-6-1860.pdf at
  `qou:QOU.Tetraplectic.su2L_su2R_commute`". Done: that IS
  `rem:tetraplectic-su2-gauge-reading`, whose `lean.ref` is exactly that
  declaration, citing `[morita1982]` and stating the left–right-symmetric
  consequence the bean asked for — which is what makes the identification
  falsifiable rather than only interpretive.

## fa: a voice-checker false positive found by this work

`voice-scholarly-default` failed on the new remark, citing
`QuaternionicElectroweak.lean:63: "Right gauge action \`SU(2)_R\`."`.
`LECTURER_OPENER_RE` carried a bare `Right,?\b`, so it read the technical
adjective as the interjection "Right,". Measured over the corpus: **22** Lean
docstring lines open with `Right`, and **21** are "Right multiplication by",
"Right action of", "Right inverse", "Right identity", "Right zero law", "Right
branch" — a 21/22 false-positive rate. Nothing had noticed because no block's
`lean.ref` had ever pointed at a file with such a docstring. Narrowed to
`Right(?:,|\s+now\b)`, which keeps the one true hit ("Right now we encode",
`Clausen.lean:40`), with six tests. `OK,?` / `Okay,?` / `Alright,?` keep their
optional comma — none of the three is ever a technical term.

validate: 20 → 21 issues, zero errors. The one added issue is
`lem:piece-a-corner-removal-obligation: no Lean declaration yet`, which is true
and is the point. QA sweep on all 11 new blocks: 0 fail, 1 advisory warn
(`wall-base-ring-minimal`, adjudicated in an `authorNotes` — the field is
essential for `LinearMap.trace` / `Module.finrank`).
