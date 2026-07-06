# Placeholder / TODO resolution triage — cluster beans doth / ldup / mlt7 / xj99

**Date:** 2026-07-05
**Branch:** `claude/placeholder-resolution-2026-07-05`
**Scope:** `content/schema/`, `content/unital-groebner-bases/`,
`content/quantum-observable-universe/mass-endomorphism/`,
`content/quantum-observable-universe/quantum-observable-universes/`
**Lane restriction:** `.md` / `.ts` prose + metadata only. `.lean` bodies,
`.qa.json` sidecars, and `computations/*.py` are owned by sibling swarm agents
and are NOT touched here.

## Summary

The four cluster beans carry inflated raw-grep titles (25 / 29 / 15 / 7 = 76
"placeholders"). The honest counter
[`scripts/count-actionable-placeholders.ts`](../../scripts/count-actionable-placeholders.ts)
— which strips `.qa.json`/`.witness.json` sidecar noise, `sorry`-in-comment
false positives, and `-- Ref:`-cited (legitimately deferred / §3b-conjectural)
`sorry`s — reports **11 actionable markers, all TODO/FIXME, 0 uncited sorries**
across the four scopes:

| Scope | bean | honest actionable | in my lane (`.md`/`.ts`)? |
|-------|------|-------------------|---------------------------|
| `content/schema` | doth | 7 (all `references.ts`) | yes (`.ts`) — but owner-gated (below) |
| `content/unital-groebner-bases` | ldup | 3 (all `unital-groebner-basis.lean`) | **no** — `.lean`, sibling-owned |
| `mass-endomorphism` | mlt7 | 1 (`qbeta-per-block-chi-closed-forms.lean`) | **no** — `.lean`, sibling-owned |
| `quantum-observable-universes` | xj99 | 0 | — (fully drained by PR #2654) |

**Resolved this session: 0. Deferred: 11 (all with documented reason).**
This is an honest-triage outcome: no marker in my lane is tractable without
author judgment or off-sandbox network access, and fabricating a title/DOI/proof
would violate the anti-fabrication rule. The prior sessions (PRs #2649, #2654,
#2637, #2796) already drained every genuinely-mechanical item; this pass
re-confirms the state with a fresh count and consolidates the deferred list.

## Deferred items (file:line + reason)

### schema — bibliography DOI/title verification (owner-gated, sandbox-403)

All 7 markers in [`content/schema/references.ts`](../../content/schema/references.ts)
are bibliography-metadata placeholders whose resolution requires resolving a DOI
landing page — every such page is 403-blocked in this sandbox — or an author
decision on edition ambiguity. The full sourced findings live in
[`docs/audits/2026-06-23-bibliography-doi-verification-doth.md`](2026-06-23-bibliography-doi-verification-doth.md).
The author has already reviewed these (bean doth updates 2026-06-24) and elected
to **keep them flagged** pending manual DOI resolution:

1. `references.ts:1485` — bib metadata TODO until verified (entry note).
2. `references.ts:3582` (`wenzl1988b`, DOI `10.1007/BF01393839`) — `note:`
   PLACEHOLDER (entry title also carries the marker at `:3578`); DOI reportedly
   resolves to a non-Wenzl number-theory paper. Real paper (widely cited), only
   the DOI is wrong; correct DOI not found off-sandbox. **Author kept flagged.**
3. `references.ts:3597` (`wenzl1988c`, DOI `10.1007/BF01388470`) — `note:`
   PLACEHOLDER (title marker at `:3593`); same class, cited inline across 4
   `.lean` files. **Author kept flagged.**
4. `references.ts:5574`, `:5577` — block header comment marking the
   post-2026-05-29 placeholder-entry region ("venue/DOI marked PLACEHOLDER where
   not independently verified"). Documentation, not an actionable slot.
5. `references.ts:5643` (`drinfeld1985`) — `note:` PLACEHOLDER; edition
   ambiguity (1985 Doklady note vs 1986 ICM Berkeley address); needs author
   decision on which the Lean `-- Ref:` intends. **Author input required.**
6. `references.ts:5686` (`habiro2000`) — `note:` PLACEHOLDER; RIMS Kōkyūroku
   preprint, cited in `DeltaLambdaSignRule.lean` / `TwoRoutesProtonMass.lean`;
   author to confirm the Lean `-- Ref:` intends the 2000 RIMS preprint vs an
   alternate Habiro 2000 work. **Author input required.**
7. `references.ts:5758` (`james1984representation`) — `note:` PLACEHOLDER;
   partially verified 2026-06-23 (authors James & Kerber confirmed) but
   EDITION/YEAR unresolved (Addison-Wesley 1981 original vs CUP later reprint);
   author to confirm which edition `S5SO3FiberAction.lean` /
   `S4S3HalfSymmetricProjection.lean` cite. **Author input required.**

Reason not resolved: DOI landing pages 403-blocked in sandbox; author already
reviewed and chose to keep flagged. Editing titles/DOIs from memory would be
fabrication.

### unital-groebner-bases — `.lean` TODO markers (out of lane + intentional)

3 markers in `unital-groebner-bases-chapter/unital-groebner-basis.lean`. These
are `-- TODO`-style comments on Lean declarations, owned by the Lean/proof
swarm agents, not free-text prose. Per bean ldup (resweeps 2026-06-22..24) they
are **intentional research/upstream markers, not actionable placeholders**.
Not touched (lane rule + intentionality).

### mass-endomorphism — `.lean` TODO marker (out of lane + intentional)

1 marker in `qbeta-per-block-chi-closed-forms.lean`. Bean mlt7 (2026-06-23,
PR #2649) already converted the one prose-level vacuity dodge in this file to
the honest §1a disposition (real proposition + cited `sorry`); the residual is
a build-gated Lean proof marker, sibling-owned. Not touched.

The two `.md`/`.ts` hits in this dir are honest documentation, not placeholders:
`multi-link-jones-q1-extension.ts:33` (an `authorNotes` body correctly recording
open R&D) and `conj-rho-k-pair-gen-canonical-form.md:84` (prose stating an open
derivation). Both are correct as written — no change warranted.

### quantum-observable-universes — fully drained

0 actionable markers (drained by PR #2654; xj99 resweep 2026-06-25 = "FULLY
DRAINED"). The lone `.md` mention
(`fiber-adjoint-involution.md:39`) is honest prose describing a Lean existence
stub and its cited-`sorry` deferral — correct as written.

## Recommendation

The four beans (doth / ldup / mlt7 / xj99) have no remaining agent-tractable
work. All residual markers need either author DOI/edition decisions
(schema) or build-gated Lean proof work owned by sibling agents. Re-title or
close is owner-only. No content edits were made in this pass beyond adding this
consolidated triage record.
