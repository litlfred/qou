---
# qou-ghy5
title: '68 dangling citation keys in .lean -- Ref: and .ts cites[] — neither path is checked'
status: in-progress
type: task
priority: normal
created_at: 2026-08-21T15:54:24Z
updated_at: 2026-08-22T12:14:01Z
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

PROGRESS 2026-08-21 (PR #5384): 69 -> 66 sites.

Landed: check-citation-keys.py (the durable half — the two unchecked paths
are now checkable, --strict for a gate); 14 keys repointed over 29 sites; 10
author lists filled on fallback-id entries; one entry renamed so a proof's
citation resolves without editing the proof.

REMAINING 66 sites / ~46 keys, in two groups:

  (a) classics absent from the bibliography — bethe1936, serre1977 (6 sites),
      voisin2002, pontryagin1934, weizsacker1935, lefschetz1926, aitken1956,
      prasad1973, wielenberg1978, shirshov1962, bokut1978, macdonald1971,
      lusztig1989, tate1950, hewitt-ready1979, turaev-viro1992, pachner1991.
      These need an ENTRY, and the metadata cannot be verified from here:
      arxiv.org is 403 and none of them is in library/. Writing a CSL entry
      from memory is the thing this repo's discipline forbids, so they want
      either a copy uploaded or an owner willing to accept unverified
      metadata explicitly marked as such.

  (b) ambiguous against an existing author — garoufalidis2020 scores 0.97
      against THREE different entries; faddeev1996 against two; murakami1996,
      murakami2013, frenkel2020, zagier2007, ohtsuki2002, bridgeland2007,
      sauzin2014, rsz2013, costin2020 similar. Each needs the citing block
      read to see which result is being invoked. Doable here, one at a time;
      not mechanical.

Also filed from this work: qou-3vgs (run-validate reports Valid on a
references.ts that does not parse — confirmed by controlled test).

EGRESS 2026-08-21/22: the owner opened arxiv / Google Scholar / Semantic
Scholar, but THIS session cannot reach them. Every request returns
'Tunnel connection failed: 403 Forbidden' and the proxy's own status endpoint
records 'connect_rejected' for export.arxiv.org:443, api.crossref.org:443 and
api.semanticscholar.org:443 — a policy denial, not TLS or transport. Nine
hosts probed (apex and subdomain), all refused. /root/.ccr/README.md says the
policy is fixed 'for this session' and to report the blocked host rather than
route around it. A NEW session in that environment should pick it up.

READY FOR THAT SESSION: scripts/enrich-dangling-citations.py. Queries arXiv,
Crossref and Semantic Scholar, writes docs/audits/citation-candidates.json for
adjudication, never touches references.ts. Verified end to end against the
live proxy — tier selection, identifier extraction, request and failure
handling all work; only the CONNECT is refused.

Tiering of the 40 remaining keys, and the confidences are NOT comparable:

   6  identifier  arXiv id or DOI in the citing comment -> exact lookup.
                  Apply with light review.
   8  title       a work named but no id. TWO are descriptions rather than
                  titles (murakami2013 -> 'deformed 4₁ asymptotic
                  (theorem-grade regime)'; wielenberg1978 -> 'the Whitehead
                  complement is a single regular'), so this tier needs real
                  review.
  26  search      nothing in the comment, because a cites: [] array has no
                  room for one. Only the key remains, and the key is a
                  CONVENTION not data: 'lusztig1989' means 'something by
                  Lusztig around 1989', and Lusztig published a great deal in
                  1989. Read the citing block before accepting any hit.

Run: scripts/enrich-dangling-citations.py --tier identifier   (start there)
