---
# qou-uq5x
title: 'The G2 frame: S6 = G2/SU(3) isotropy is viable, and what it actually costs'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T02:31:24Z
updated_at: 2026-10-04T15:11:10Z
parent: qou-8lxd
---

## Result 2026-09-04 (branch claude/w-derived-from-axioms-2026-09-04)

Audit: docs/audits/2026-09-04-the-g2-frame.md -- full evidence, scopes, grep record.
Lean:  QOU/Eightfold/G2FrameDimensions.lean (17 decls, lean-direct exit 0,
       axioms at most [propext, Classical.choice, Quot.sound], no sorryAx).

VERDICT. S^6 = G2/SU(3) is VIABLE: its isotropy is the complex 3-dim fundamental
of SU(3), FS type COMPLEX, so it passes the Sym^2 gate whose self-dual sector
real_triple_fails_gate / two_dvd_dimOf_of_no_complex exclude. G2/SO(4) (Wolf
space) dies twice: isotropy 8-dim, and REAL type (V1 (x) Sym^3 V2). But S^6 does
NOT discharge the owner's objection -- it derives W from the octonions, and O is
an external input the corpus states as such (the one substrate->O route, the S4
Bring->Klein bridge, is scope-(b) excluded). It trades 'postulate W' for
'postulate O'.

PROVED (integers only, no R): C(n,3) <= n^2 iff n <= 8; C(n,4) <= n^2 iff n <= 7
(so n=8 is where the 4-form route dies -- qou-8p1f generalised); n^2 - C(n,3) =
14 iff n = 7 UNIQUELY; and no SO(n) gives a 6-dim G2 quotient, no SU(n) an 8-dim
one -- the load-bearing form of qou-ko4g's 'complementary'.

FRAMING CORRECTED. 'Corpus G2 is a discrete PSL(2,7) skeleton' is FALSE at
Lie-algebra level: dim Der(O) = 14, finrank_su3_e1 = 8, finrank_range_evOct_e1 =
6 -- dim G2/SU(3) = 6 is already Lean, sorry-free, with Le^2 = -id supplying the
complex structure. Missing is the Lie GROUP and MANIFOLD. Mathlib gap is deeper
than item 3 says: NO differential forms on manifolds at all. ko4g's 'no mention
of G2/SO(4) anywhere' is self-falsified. library/ has ZERO held source (sections
and ocr). Path 0 corpus_search unavailable (paper-assistant MCP down).

NEXT (judgement): build W := span(e2..e7) with Le, prove su3 e1 preserves it and
Lambda^3_C W = 1 -- linear algebra on objects the corpus has, via Mathlib
ExteriorPower; no manifold needed. Turns the cited Gunaydin-Gursey input into a
derived one. Does not close O-from-substrate (Hecke transport: qou-ni4b).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
