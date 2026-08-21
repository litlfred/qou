---
# qou-ghy5
title: '68 dangling citation keys in .lean -- Ref: and .ts cites[] — neither path is checked'
status: in-progress
type: task
priority: normal
created_at: 2026-08-21T15:54:24Z
updated_at: 2026-08-21T16:43:16Z
---

MEASURED 2026-08-21 (found while draining the library registration backlog, bean qou-kqbk).

Three citation paths exist; only one is checked.

  .md  \cite{}      0 dangling   <- this is what the existing gate measures
  .lean -- Ref: []  40 dangling
  .ts  cites: []    28 dangling
                    68 distinct keys total

Excluded from that count, correctly: the `manuscript` sentinel, which
AGENTS.md §1 explicitly sanctions ('If no published reference exists, use
[manuscript] and cite chapter/section') and which is used 3,532 times, plus
9 keys that are CONTENT BLOCK LABELS sitting where a citation key belongs
(conj:jet-filtered-knot-factor, thm:jones-markov-trace, def:descent-involution,
...) — those are a separate defect and want a different fix.

Why this matters for .lean specifically: AGENTS.md §1 states 'The [key] must
match an entry in content/schema/references.ts exactly (case-sensitive)' and
'A sorry without -- Ref: is always a review failure'. 40 sorries carry a
citation that resolves to nothing, which reads as cited and is not.

Sample of the real ones: bethe1936, lusztig1989, macdonald1995symmetric,
fulton-harris, khovanov-lauda2009, kontsevich-soibelman2008, faddeev1996,
hewitt-ross1979, pontryagin1934, ohtsuki2002, dimofte-gaiotto-gukov2014.
Most are well-known works, so most are a bibliography entry away from
resolving — this is a drain, not a research task.

Full list: reproduce with the three greps above; not pasted here to keep the
bean readable.

NOT fixed in qou-kqbk: adding ~68 entries is its own tranche, and that branch
was scoped to registering library documents.

CORRECTION 2026-08-21 — my own count above was WRONG, and over-reported.

The bean says '68 dangling citation keys ... 40 in .lean -- Ref: [], 28 in
.ts cites: []'. That was a raw 'key not in references.ts' count, and it
counted four conventions that legitimately put something other than a
bibliography id in the brackets. Three are documented in AGENTS.md and one is
undocumented but in live use:

  * [manuscript] — AGENTS.md §1, 3,527 sites.
  * a cross-paper block label, paper-dir:label — the Cross-paper references
    table. 6 sites.
  * a same-paper block label, bare — same table. 12 sites.
  * [tag] <in-repo-path> — the [manuscript] shape generalised, tag naming
    the kind and the path saying where:
        -- Ref: [audit] docs/audits/2026-06-09-metallic-q-csc-phase-synthesis.md
        -- Ref: [probe] computations/metallic_q_symbolic_galois_proofs.py
        -- Ref: [metallichierarchy] QOU.AlgebraicSubstrate.MetallicHierarchy
    10 sites. Undocumented, but it resolves.

Measured correctly: of 7,810 citation sites across all three paths, **69
resolve to nothing, over 48 distinct keys** — 24 distinct on lean-ref and 25
on ts-cites. Not 68 keys.

The .md \cite{} path remains clean at 0, which is the only path the content
pipeline checks — that part of the original measurement stands.

WHAT LANDED (this branch):
  * scripts/check-citation-keys.py — resolves all three paths with the four
    conventions encoded, --strict for a gate. The unchecked paths are now
    checkable, which is the durable half of this bean.
  * 11 keys repointed (24 sites): 6 punctuation-only, 5 where the extra token
    is the target's own title. No similarity threshold — measured here,
    zagier2007/zagier2010 score 0.78 and are different papers.
  * prop:jet-convergence-classical-limit -> conj: (2 sites). The block is a
    conjecture and was cited as a proposition, inside conditional Prop
    classes that axiomatise it — the §3b conjectural-propagation slip, which
    reads to a reviewer as proved backing.

REMAINING: 69 sites / 48 keys, each needing the citing block read to decide
which work is meant. Roughly half are classics absent from the bibliography
(bethe1936, serre1977, voisin2002, pontryagin1934, weizsacker1935); the rest
are ambiguous against an existing author (garoufalidis2020 scores 0.97
against three different entries).

AMENDMENT: the correction above says '69 resolve to nothing, over 48 distinct
keys'. The union is **49**, not 48 — 24 on lean-ref plus 25 on ts-cites, with
no key appearing on both paths, so the two add rather than overlap. The 69
site count and the per-path figures are right; only the union was mis-added.
