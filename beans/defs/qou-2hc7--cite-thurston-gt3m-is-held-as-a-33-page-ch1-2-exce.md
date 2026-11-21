---
# qou-2hc7
title: 'CITE: Thurston GT3M is held as a 33-page Ch.1-2 excerpt — M — 113 citers, several at Ch.4 / §4.5 gluing equations'
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:02:44Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

**Class M — held, correctly attributed, but the held copy cannot support the locators.**

`library/thurston/` is registered as `[thurston1978]` (Thurston, *The Geometry and
Topology of Three-Manifolds*, Princeton lecture notes 1978). `references.ts:3636-3641`
records `pages: 33, sections: 22` — and that is the whole of what is ingested:
**22 section files, 54,841 bytes, Chapters 1–2 only** (geometry and 3-manifolds;
elliptic and hyperbolic geometry; hyperbolic trigonometry, `cosh d(x,y)`).

Measured inside the held copy, 2026-09-04:

| phrase | files in `library/thurston/sections/` |
|---|---:|
| `gluing equation` | **0** |
| `hyperbolization` / `hyperbolisation` | **0** / **0** |
| `figure-eight` / `figure eight` | **0** / **0** |
| `ideal simplex` | **0** |
| `Haken` | **0** |
| `ideal tetrahed` | 1 |
| `Dehn surgery` | 2 |

**113 files** cite `thurston1978`, and several cite it precisely for Chapter 4
material the held excerpt does not contain:

- `folio/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.lean:91`
  — `-- Ref: [thurston1978] §4.5 (gluing equations)`
- `folio/quantum-observable-universe/lean/QOU/MathlibExt/ManifoldVolumeBridge.lean:112`
  — `-- Ref: [thurston1978] Ch. 4 (hyperbolisation; the gluing-equation solution)`
- `folio/quantum-observable-universe/lean/QOU/MathlibExt/ManifoldVolumePositive.lean:30`
  — `-- Ref: [thurston1978] Ch. 4`
- `folio/quantum-observable-universe/mass-theory/kashaev-volume-conjecture.lean:142`
  — `hyperbolic structure on figure-eight complement`
- `folio/quantum-observable-universe/mass-theory/figure-8-archimedean-illustration.md:5,97`

**The citations are very likely correct about the book** — GT3M Ch. 4 does carry
that material. The defect is that **no reader or agent can check a Ch. 4 locator
against the corpus**, and corpus-grep path 5 for `gluing equation` will never land
in `library/thurston`. That is exactly the failure mode path 5 exists to prevent.

**Two fixes, either sufficient:**

1. Ingest the full GT3M notes (freely distributed by MSRI,
   <http://library.msri.org/books/gt3m/>) into `library/thurston/`, replacing the
   33-page excerpt, and update `references.ts` `library.pages`/`sections`.
2. Cheaper and already available: **`library/angled-survey`** (Futer–Guéritaud,
   *From angled triangulations to hyperbolic structures*) is held and covers
   exactly the cited material — `gluing equation` **10** section files,
   `ideal tetrahed` **9**, `angle structure` **13**, `Rivin` **31**. Add it
   alongside `thurston1978` at the Ch. 4 locators. It is **not registered in
   `references.ts`** — check before citing.

**Do NOT "fix" this by deleting the Thurston citations.** The attribution is right;
the holding is partial.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done-partial** (commit `147d65c7df6`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). FG Def2.4/Prop2.5/Thm1.2 added at 3 named sites; other ~110 thurston1978 citers not swept; full GT3M ingest still open

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
