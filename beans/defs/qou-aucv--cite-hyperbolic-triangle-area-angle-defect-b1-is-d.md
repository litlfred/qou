---
# qou-aucv
title: 'CITE: hyperbolic-triangle area = angle defect (B1) is docstring-asserted with no source — M — EmCouplingBringZeroMode.lean:88-89, em-coupling-bring-zero-mode.md:20'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:06:49Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-mub3
---

**Class M — the one geometric input under the Bring zero-mode chain that is neither
proved nor cited, while sixteen held sources state it.**

`lean/QOU/Archimedean/EmCouplingBringZeroMode.lean` is sorry-free and proves a
clean chain — `bringSurfaceArea_eq_gaussBonnet` (`:132`), `bringTilingEuler_eq`
(`:206`), `bringTiling_genus_four` (`:213`), `bringTiling_b1` (`:218`),
`bringZeroMode_fully_tiling_derived` (`:232`, `b₁/Area = 2/(3π)`). But
`gaussBonnetArea` (`:123`) is a **`def`**, `4π(g−1)`, and the proofs close by
`ring`. It is arithmetic wearing geometric names, and the geometry underneath is
assumed in a docstring:

- **(B1)** that a hyperbolic triangle's area equals its angle defect
  (Gauss–Bonnet for `ℍ²`) — docstring at `:88-89`, proved nowhere.
- The narrative twin says it outright:
  `folio/quantum-observable-universe/predicted-spectra/em-coupling-bring-zero-mode.md:20`
  — *"The area evaluates under constant negative curvature −1 as
  `Area = −2πχ = 4π(g−1) = 12π`."* Block kind **`proposition`**.

**The file's `-- Ref:` lines (`:57-62`) are for a different leg**: `[suslin1991]`,
`[bloch2000]`, `[thurston1978]` plus three `[manuscript]` labels — the
dilogarithm/Bloch-group side. The `.ts` `cites: ["jones1987", "kassel1995",
"suslin1991", "bloch2000"]` likewise. **Nothing points at Gauss–Bonnet.**

**`references.ts` has no Gauss–Bonnet entry** (no `gauss`, no `bonnet` id over 828
entries).

**Sixteen held dirs state it** — `Gauss-Bonnet` (hyphen) **12**: `18`,
`210811825v1`, `6gtx-j455`, `arxiv-1303.5278v1`, `arxiv-1512.04993v2`,
`arxiv-1604.02688v1`, `arxiv-math-9907032v1`, `arxiv-math-9911033v1`,
`bsmf-2002-130-3-457-0`, `disssubmission`, `ihpmay2025`,
`topologicalinvariance3dindex`; `Gauss–Bonnet` (en dash) **4** more: `0307092v2`,
`ant-v14-n7-s`, `ant-v14-n7-s-p05`, `ant-v14-n7-s-p10`. **Only the en-dash spelling
appears in `INDEX.md` (1 row)** — a hyphen-only `INDEX.md` scan reports zero and
reads as an absence.

**Also worth checking while here:** `library/thurston/` Ch. 2 covers elliptic and
hyperbolic geometry and hyperbolic trigonometry (sections `sec-008` … `sec-021`,
including `cosh d(x,y)` and hyperplane distance). It may well contain B1 directly,
which would make `[thurston1978]` — already cited in this very file — the right key
after all. **Check the held excerpt before adding a new source**; see the sibling
bean on the Thurston excerpt for why its 33 pages cannot be assumed to cover a
given chapter.

**Companion facts, tracked separately:** (B2) the `240` and (B3) `B ≅ ℍ²/Γ` are the
subject of the Riera–Rodríguez §2 bean. This one is only B1.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8480, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
