---
# qou-q5jn
title: chap:particle-interactions is authored but UNREGISTERED in the paper manifest (5 broken xrefs)
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T10:39:21Z
updated_at: 2026-11-15T14:10:00Z
parent: qou-hqo3
---

Found 2026-08-07 by run-validate on the folio-assistant pipeline. content/quantum-observable-universe/particle-interactions/particle-interactions.ts EXISTS and declares label 'chap:particle-interactions' (line 16), but the paper manifest quantum-observable-universe.ts has NO chapterRef({dir: 'particle-interactions'}) -- the only mention is a COMMENT at line 87. So the chapter does not render in the paper at all, and 5 blocks that cross-reference it emit 'Undefined cross-reference': chapter-overview, approach-to-exceptional-divisor, thurston-relaxation, observations-intro, ns-blowup-physical-evidence.\n\nLikely an oversight, not a deliberate exclusion: the same line-87 comment records that the dissolved statistics-symmetrisation chapter REDISTRIBUTED four blocks INTO particle-interactions (spin-from-so3-fiber, type-b-folding-cpt, weinberg-angle-categorical, wigner-su4-from-spin-isospin). So content was deliberately moved there, but the chapterRef was never added.\n\nNOT FIXED UNILATERALLY -- adding a whole chapter to the paper manifest changes the RENDERED DOCUMENT (its Part placement and ordering are an authorial decision, and the surrounding manifest is organised into Part I/II/III with deliberate ordering). Needs the owner's call on WHERE it goes. Once placed, all 5 xref warnings clear at once.\n\nNote these are WARNINGS not hard errors, so CI does not block on them -- which is why it has persisted.

DONE 2026-11-15: already fixed on main 0d4e4a005e. chap:particle-interactions is no longer referenced anywhere in folio/.
