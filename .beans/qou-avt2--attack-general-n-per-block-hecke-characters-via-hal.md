---
# qou-avt2
title: 'ATTACK 2: general-n per-block Hecke characters via Halverson-Ram / Jing-Liu'
status: todo
type: task
priority: normal
created_at: 2026-08-26T04:14:19Z
updated_at: 2026-08-26T04:14:19Z
---

Newly enabled by the owner's 2026-08-26 Murnaghan-Nakayama upload drop
(commit 548de479), now ingested and greppable under library/.

WHAT THE CORPUS HAS NOW. chi_block_3 / chi_block_21 / chi_block_111 in
qbeta_utils.py are hand-derived and exist ONLY at n = 3, and the one-crossing
"character collapse" 2*chi_lambda(sigma_1) - h*f^lambda = [2]_q*chi^lambda(tau)
was likewise derived by hand (2026-08-21 ladder-phase audit).

WHAT THE LITERATURE SUPPLIES. A Murnaghan-Nakayama rule for IWAHORI-HECKE
characters on standard elements:

  library/9511222v1/          Halverson & Ram, MN rules for H(G(r,p,n))
  library/arxiv-2504.18825v2/ Jing & Liu (v2, 2026-03) -- STRONGER, PREFER THIS:
                              Shoji determinacy gives the FULL irreducible
                              character table of H_{m,n}(q,u), and Jing-Liu note
                              that HR "computed characters only on certain
                              standard elements and did not prove" completeness.
                              Also a DUAL MN rule via vertex operators.

So the deliverable is a general-n closed form for the per-block Hecke characters
-- taking the ladder's per-block structure past n = 3 without re-deriving by
hand each time.

TRAP, DO NOT FALL IN. library/arxiv-2406.05311v1/ (quantum MN rule for the FLAG
MANIFOLD) has a "quantum" that is the quantum-cohomology NOVIKOV parameter, NOT
the Hecke q. Identifying them is the overloaded-symbol failure registry section
2 exists for. Cite it for the hook-Schur reduction via quantum Bruhat order
(Leung-Li, Postnikov); do not import its q.

NOTE what this does NOT do: it does not bridge to the Xi_k weight moments --
those collapse to a function of h (qou-ximf, retracted 2026-08-26).
