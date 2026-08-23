---
# qou-cauj
title: 'Nine .md the 52c68267f2 bulk import dropped: 2 restored, 2 need an authoring call, 5 are probably not blocks'
status: todo
type: task
priority: normal
created_at: 2026-08-23T08:44:25Z
updated_at: 2026-08-23T08:47:25Z
---

MEASURED 2026-08-23 while draining the last validate errors.

`52c68267f2` (2026-08-15, Claude) added **3,593 content `.md` and 3,650 `.ts`**
in one commit. **Nine `.md` came through with no manifest** — 0.25%, which is
import breakage rather than curation. Four of the nine also got a `.qa.json`,
which is what made them visible: `run-validate` reports them as
`orphan QA sidecar: X.qa.json has no sibling X.ts`.

I had previously called these "the owner's content call, not a mechanical
one". For two of them the commit history says otherwise, and that is corrected.

## RESTORED (6d4bb17ccc) — determined, not judged

* `predicted-spectra/spectral-decomposition-qvalue-interpretation` ->
  `rem:…`, `interprets: cor:spectral-decomposition-qvalue`. Its `.md`, its
  `.qa.json` and **every sibling's `.ts`** landed in that same commit; only
  this manifest was omitted. Shape fixed by six registered siblings plus
  `rj-inner-product-interpretation` two entries above it in the same section.
* `mass-theory/q-clt-jsj-mass-scaling` -> `rem:…`,
  `interprets: conj:jsj-decomposition-linearity`. The `.md`'s own front-matter
  titled it "Remark: …" and its subject is exactly that conjecture (leading
  mass term linear in (Z,N) because volume is additive under torus gluing).

Both needed their YAML front-matter and H1 stripped into the manifest: **0/400**
sampled registered blocks carry front-matter, **0/60** registered remarks open
with an H1, and `render-latex.ts` strips neither.

## STILL FAILING — a genuine authoring call, do not "just register" these

Both are written in **audit register**, so registering as-is lands a one-voice
violation:

* `mass-theory/qbeta-fmap-structural-form` — sections titled "Exploratory
  Series: The Pole Obstruction", "Derivation pathways", "What remains open".
  It also carries a durable **refutation** — "**Conclusion: The f-map cannot be
  a scalar operator**" — which under §"Before declaring refuted" needs an
  (a)/(b) scope label it does not have. (Its argument looks like a real (b):
  a `1/w` pole against a series in `u = O(w²)`. But it is unlabelled.)
* `mass-theory/q-beta-c3-continuum-geometry` — opens with a dated
  `> **⚠ CORRECTION (2026-07-11) — …over-scoped**` banner, i.e. §4d
  `authorNotes` material sitting in prose.

Disposition for each is: clean up and register, or move to `docs/audits/`.
Both are real content — not superseded, checked — so **deleting the sidecar
and walking away would lose authored work**.

## THE OTHER FIVE — no sidecar, so validate never mentions them

* `fluid-dynamics/ns-kummer-specialisation-divisibility.md` — kebab-case in a
  chapter dir; looks like a block that lost its manifest. Same class as the two
  restored above; worth checking for a sibling family.
* `PieceACornerInduction.md`, `PieceASpechtCharacter.md`, `bring_tetraplectic.md`
  — at the PAPER ROOT, CamelCase / snake_case, i.e. not the kebab-case block
  convention. Probably working notes, not blocks.
* `lean/AUDIT-REPORT.md` — an audit report. Not a block. It has a `.qa.json`
  and is the fifth swept orphan; validate does not flag it only because it sits
  under `lean/`.

## Why this is worth a bean rather than a one-off

Nothing detects an unregistered `.md`. The orphan-sidecar error is a *proxy* —
it fires only when a file happened to get QA-swept. Five of the nine are
invisible to every gate. A checker for "content `.md` with no `.ts` and not
under `*/audit/`" would be ~10 lines and would have caught all nine on the day
of the import.

validate on this branch: 4 errors -> 2 (30 issues).


---

## CORRECTION (same day) — it is EIGHT, not nine, and I found it by testing my own gate

The list above names
`fluid-dynamics/ns-kummer-specialisation-divisibility.md` as one of the five
with no sidecar. **That file does not exist.** It was added by the import and
resolved afterwards: the directory now holds `ns-kummer-specialisation.md` and
`ns-kummer-specialisation-consequence.md`, both with manifests, both
registered. My list was built from the import commit's added-files and never
checked which of those paths are still live.

So: **8 dropped**, 2 restored, 2 needing an authoring call, and **4** — not
five — that are probably not blocks (`PieceACornerInduction.md`,
`PieceASpechtCharacter.md`, `bring_tetraplectic.md`, `lean/AUDIT-REPORT.md`).

A corpus scan confirms only **two** unregistered chapter-level `.md` remain,
and they are exactly the two audit-register files this bean already flags as
needing a call.

## The gate is written — and its first bug was this same mistake

`scripts/check-sidecars.sh` now flags a changed `content/<paper>/<chapter>/*.md`
with no `.ts` sibling (skipping `*/audit/`, `*/lean/`, `*.qa.md`), scoped to
changed files.

Its first version reported the deleted path above. `files` comes from
`git diff --name-only`, which lists **deletions**, and a removed `.md` has no
`.ts` either — so every file deletion would have been reported as an
unregistered block. Guarded with `[ -f "$m" ] || continue`. Verified: the
deleted path is now passed over, `qbeta-fmap-structural-form.md` is still
caught, and registered blocks / audit docs / `lean/AUDIT-REPORT.md` are not.
