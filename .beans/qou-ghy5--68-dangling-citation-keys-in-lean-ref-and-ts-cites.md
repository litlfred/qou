---
# qou-ghy5
title: '68 dangling citation keys in .lean -- Ref: and .ts cites[] — neither path is checked'
status: todo
type: task
priority: normal
created_at: 2026-08-21T15:54:24Z
updated_at: 2026-08-21T15:54:40Z
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
