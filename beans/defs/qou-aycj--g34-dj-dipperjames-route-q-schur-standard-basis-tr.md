---
# qou-aycj
title: 'G3.4-DJ: Dipper–James route — q-Schur standard basis, triangularity, generation, image = commutant'
status: in-progress
type: task
tags:
    - quark-state
    - schur-weyl
parent: qou-gl34
created_at: 2026-11-15T11:05:14Z
updated_at: 2026-11-21T08:00:00Z
---

Stream 16 (Dipper–James route), parallel to stream 14 (#7864: complete reducibility + V=B·N + dimension sandwich). Owner via coordinator: also do dipper-james. Branch claude/g34-dipper-james-2026-11-15. Scoping and milestones DJ0–DJ5: docs/audits/2026-11-15-gl34-dipper-james-scoping.md. Nothing proved yet. Key finding: Doty–Giaquinto (arXiv math/0108046, now in library/) ASSUMES that U→S is surjective, citing Du 1995 and Jimbo 1986. No held source proves the generation step.

## 2026-11-15 takeover (session_01Qmmkt9G83BWVJD2uM6cPfq)
Owner re-scope: **extend G3.4 to any field with q not a root of unity** (option 1). Stream 14 (#7864) covers ordered fields; its only ordered-field step is F1 (`isCompl_dotPerp`). Char 0 first; char p also needs Hecke semisimplicity in char p (`isSemisimpleRing_hecke_generic` is `[CharZero K]`).
**DJ0 done:** `QOU/MathlibExt/Bicommutant.lean`, `centralizer_centralizer_eq`: for `A ≤ End_K V`, V fin-dim and semisimple as an A-module, `A'' = A`, over any field. lean-direct exit 0; axioms propext/choice/Quot.sound only.

## 2026-11-21 — restored to the bean mount; files ported to main
Copied verbatim from PR #7874's branch tip `cfd55f5081` (beans moved to the branch mount, issue #7642).
The G3.4 files absent from main (Bicommutant.lean, QSchurUpperBound.lean, QSchurMoves.lean, the two
gl34 audits, Doty math/0610591 ingest + key `doty2006`) are cherry-picked (-x) onto
`claude/port-g34-dipper-james-2026-11-21`. Main already held Doty–Giaquinto math/0108046 as
`doty-giaquinto-2002`, so the duplicate key `doty-giaquinto2001` was dropped and the audit cites main's key.
Session https://claude.ai/code/session_01Qmmkt91GpCvJB15AZz7wMr.
