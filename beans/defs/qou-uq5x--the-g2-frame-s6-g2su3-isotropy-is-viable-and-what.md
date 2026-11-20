---
# qou-uq5x
title: 'The G2 frame: S6 = G2/SU(3) isotropy is viable, and what it actually costs'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-09-04T02:31:24Z
updated_at: 2026-11-20T16:06:50Z
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


## Progress Update — 2026-11-16 (`litlfred/qou#8149`, `e824457ca8e0ff4e0b85644c5478eebd2c3c8d56`)

- **Lean 4 formalization (`folio/quantum-observable-universe/lean/QOU/Eightfold/G2IsotropyComplexThreefold.lean`, `0` `sorry`, wired into `QOU.lean`)**:
  - Formalizes the 6D orthogonal complement $W = \mathrm{span}(e_2, e_3, e_4, e_5, e_6, e_7) \subset \mathrm{Im}(\mathbb{O})$ (`OctComplement6`) and left multiplication $J = L_{e_1}$ (`OctComplement6.jMap`) under the Fano triples $(1,2,3), (1,4,5), (1,6,7)$;
  - Proves `OctComplement6.jMap_sq_eq_neg` ($J^2 = -\mathrm{id}_W$), `OctComplement6.fano_planes_jMap_invariant`, and `OctComplement6.direct_sum_three_fano_planes` ($W = W_1 \oplus W_2 \oplus W_3 \cong \mathbb{C}^3$);
  - Formalizes $J$-commuting endomorphisms (`ComplexEnd3`) and proves `ComplexEnd3.su3_annihilates_top_exterior_power`: every traceless $J$-commuting derivation $D \in \mathfrak{su}(3)_{e_1}$ ($\operatorname{tr}_{\mathbb{C}}(D) = 0$) acts with weight $(0,0)$ on $\Lambda^3_{\mathbb{C}} W \cong \mathbb{C}$ ($\Lambda^3_{\mathbb{C}} W \cong \mathbf{1}$) and satisfies $\operatorname{tr}_{\mathbb{R}}(D) = 0 \wedge \operatorname{tr}_{\mathbb{R}}(J D) = 0$, plus `exterior_algebra_dimension_split` ($1 + 3 + 3 + 1 = 8$).
- **50-dps / exact matrix verification (`computations/probes/ribbon_twist_z6_hypercharge_hirzebruch_probe.py` + `ribbon-twist-z6-hypercharge-hirzebruch.witness.json`)**:
  - Explicitly constructs $J = L_{e_1}$ and all 8 real $6 \times 6$ Gell-Mann generators $D_a$ ($a = 1..8$) of $\mathfrak{su}(3)_{e_1} \subset \mathfrak{so}(6)$, verifying $J^2 = -I_6$, $[D_a, J] = 0$, $D_a^T + D_a = 0$, and $\operatorname{tr}_{\mathbb{R}}(D_a) = \operatorname{tr}_{\mathbb{R}}(J D_a) = 0$ (`allPassed: true`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8149, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
