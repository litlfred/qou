---
# qou-ezne
title: 'CITE: Riera-Rodriguez 1992 §2 sources the unsourced 240 and B = Delta/Gamma — M — EmCouplingBringZeroMode.lean, em-coupling-bring-zero-mode.md'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:03:28Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-mub3
---

**Class M — the source is held, registered, and cited for a different section of itself.**

**Work:** Riera, Gonzalo & Rodríguez, Rubí E., *The period matrix of Bring's curve*,
Pacific J. Math. **154** (1992) 179–200, DOI `10.2140/pjm.1992.154.179`.
Registered `[riera-rodriguez-1992]`; held at `library/pjm-v154-n1-p09-s/`
(25 pp, 8 sections). Second copy `library/the-period-matrix-of-bring-s-curve-1hik02mwva/`
carries `duplicate_of: "pjm-v154-n1-p09-s"` and has no `INDEX.md` row —
**one work, not two sources**; `references.ts` already records it under `alternates`.

**What §2 supplies, and the corpus asserts unsourced.**
`library/pjm-v154-n1-p09-s/sections/page-004.md`
(pp. 2–8) constructs `Γ*` as the **(2,4,5) triangle group** from a 20-sided
non-euclidean polygon with angles π/5, π/4, π/2; defines `φ : Γ* → S₅`, sets
`Γ = ker φ` and shows it torsion-free; and concludes **`B = Δ/Γ` has genus 4**
with `S₅` acting by automorphisms.

That paragraph is precisely:

- **B3** — that Bring's curve carries a hyperbolic metric at all (`B ≅ ℍ²/Γ`,
  Γ torsion-free Fuchsian). **Absent from the entire corpus** — there is no `ℍ²`,
  no Möbius action, no Fuchsian group and no `Δ/Γ` in any QOU file, and
  `Mathlib.Analysis.Complex.UpperHalfPlane.*` is never imported.
- **B2** — the bare integer `240`. `[Γ*:Γ] = |S₅| = 120`, two triangles per Γ*
  fundamental domain ⇒ 240.
- the **(2,4,5)** datum the Lean uses without citation.

**Where it bites.**
`folio/quantum-observable-universe/lean/QOU/Archimedean/EmCouplingBringZeroMode.lean`
(sorry-free): `bringFundamentalTriangleArea` (`:90`, the π/20 angle defect),
`bringSurfaceArea` (`:94`, `240 ×` that), `bringTilingFaces := 240` (docstring
`:195-199`), `bringSurfaceArea_eq_gaussBonnet` (`:132`). Its `-- Ref:` lines
(`:57-62`) are `[manuscript]`, `[suslin1991]`, `[bloch2000]`, `[thurston1978]` —
**the dilogarithm leg, not the geometry**. Narrative twin
`folio/quantum-observable-universe/predicted-spectra/em-coupling-bring-zero-mode.md:20`;
its `.ts` `cites: ["jones1987", "kassel1995", "suslin1991", "bloch2000"]` — same gap.

`references.ts:9037` registers the paper for its **period matrix** (`Z = τ₀·C`,
`Jac ~ E⁴`) only. Existing beans `qou-3q4q` (Lemma 1 p. 184 at
`BringHauptmodulGate`) and `qou-fkmt` (§2 integral homology action at
`TrBIntegerTracePrune`) cite **other** parts of the same paper; **neither covers
the triangle group / 240 / `B = Δ/Γ`**, so this is not a duplicate of either.

**Side note, worth one line in whoever picks this up:** both `qou-3q4q` and
`qou-fkmt` name the `duplicate_of` copy (`…-1hik02mwva`) as their source rather
than the preferred stem `pjm-v154-n1-p09-s`. Retarget while you are in there.

**Fix:** add `riera-rodriguez-1992` to `em-coupling-bring-zero-mode.ts` `cites`,
and a `-- Ref: [riera-rodriguez-1992] §2 (pp. 2–8)` at the `bringTilingFaces` and
`bringFundamentalTriangleArea` docstrings. This converts B2 and B3 from unsourced
assumptions into cited classical literature — the honest tier for an imported fact.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`;
first spotted in `docs/audits/2026-09-04-how-the-hyperbolic-volume-could-arise-from-qou.md` §4.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8480, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.


## 2026-11-21 — expo-chapter drain (session https://claude.ai/code/session_01Qmmkt5JeUvGF2FboRQJbLN, issue #8826)

Done on branch `claude/expo-chapter-drain-2026-11-21` (354d4bddc): `riera-rodriguez-1992` added to `em-coupling-bring-zero-mode.ts` cites. Locator checked in the held copy: `library/pjm-v154-n1-p09-s/sections/page-003.md`–`page-004.md` = journal pp. 180–181 (the bean's "pp. 2–8" is PDF pagination): Γ* the (2,4,5) triangle group from the 20-gon with angles π/5, π/4, π/2; φ: Γ* → S₅; Γ = ker φ torsion-free; B = Δ/Γ genus 4. Not done: the two `-- Ref: [riera-rodriguez-1992] pp. 180–181` lines in `EmCouplingBringZeroMode.lean` (need lean-direct).
