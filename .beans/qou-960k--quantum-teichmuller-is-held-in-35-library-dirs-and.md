---
# qou-960k
title: Quantum Teichmuller is held in 35 library dirs and used in ZERO content blocks
status: todo
type: task
priority: normal
created_at: 2026-09-04T10:28:54Z
updated_at: 2026-09-04T10:29:37Z
---

MEASURED 2026-09-04. Held-but-unused, the largest such body found this session:

  term                          content/  docs/  library/ dirs
  quantum Teichmuller              0        3        35
  Fock-Goncharov                   0        3         4
  skein algebra of the torus       0        0         2
  peripheral torus                 0        0         7
  recursion ideal                  0        0         3
  noncommutative A-polynomial      0        1         4

35 held directories on quantum Teichmuller and ZERO content blocks using it.

WHY IT MATTERS RATHER THAN BEING TRIVIA: bean qou-52fu (completed 2026-08-04, epic qou-8lxd) answered 'does hyperbolic geometry on the complement give SU(3)?' with NO - holonomy is rho: pi_1 -> PSL(2,C), rank 1 - and named the rank-2 route as 'the PGL(3,C) analogue: Garoufalidis-Thurston-Zickert gluing equations for PGL(n), Fock-Goncharov coordinates, higher Teichmuller'. That is exactly this machinery. So the corpus identified the rank-2 lead, and has 35 sources for it on disk, and has never written a block against them.

NOT A CLAIM THAT THE ROUTE WORKS. qou-52fu proposes it; nothing here evaluates it. This bean records only that the sources are held and unused, so the next agent does not conclude from a content/ grep that the material is absent - which is the mistake made four times in this session.

SCOPE OF THE MEASUREMENT: library/*/sections/ only. NOT searched: library/*/ocr/ (25 dirs carry one and a sections-grep is blind to them) or the PDFs themselves. corpus_search (path 0) unavailable for a fourth session.
