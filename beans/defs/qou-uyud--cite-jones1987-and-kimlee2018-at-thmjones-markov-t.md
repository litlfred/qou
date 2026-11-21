---
# qou-uyud
title: Cite [jones1987] and [kimlee2018] at thm:jones-markov-trace — the block titled '(Jones, 1987)' cites nothing
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T18:29:45Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-mub3
---

`folio/quantum-observable-universe/braids-and-knots/jones-markov-trace.ts` has
NO cites field at all, while its .md (line 29) asserts that the vanishing blocks
span the radical of the trace form, that H_n(q)/rad =~ TL_n(q), and that the
surviving sum of dim^2 is the Catalan number C_n (2, 5, 14, 42, 132, 429). The
block's own title is "Existence and non-degeneracy of the Markov trace (Jones,
1987)" and it is tagged `external-proof`.

- PRIMARY: `jones1987` is already in references.ts (Ann. Math. 126 (1987)
  335-388, DOI 10.2307/1971403). Both Kim-Lee papers in the nine-PDF batch name
  Jones 1987 as the standard source for Temperley-Lieb as a quotient of the
  type-A Hecke algebra, which is the folio's open item "a clean statement of the
  Hecke -> TL quotient". Worth noting: [kimlee2018] section 1 gives Fan,
  "Structure of a Hecke algebra quotient", J. Amer. Math. Soc. 10 (1997) 139-167
  as the source for the STRUCTURE of that quotient; Fan is not in references.ts.
- SECONDARY, for the Catalan count specifically: [kimlee2018] Prop. 3.1 gives an
  explicit Groebner-Shirshov standard-monomial basis of T(A_{n-1}) of cardinality
  C_n, i.e. dim TL_n = Catalan(n) at general n from the literature. Today the
  folio's support for that is `QOU/QBeta/TemperleyLiebTower.lean`'s
  catalan_three / catalan_four / catalan_five, which check the folio's own table
  against Mathlib's Nat.catalan -- internal consistency, not a source. The same
  unsourced general-n assertion appears at
  `markov-trace-frobenius-selection.md:82` (that block does cite jones1987,
  wenzl1988, yekutieli2015, but nothing for the Catalan count).

While there, consider a `-- Ref: [jones1987]` on the TemperleyLiebTower.lean
module docstring; the file currently carries none.

NOT closed by this: the open identity sum_k m_k^2 = Catalan(n) with
m_k = C(n,k) - C(n,k-1). Converting dim TL_n = C_n into it needs semisimplicity
of TL_n at delta = 2.0108969 and the two-row indexing of the Wedderburn blocks,
neither of which [kimlee2018] states.


## 2026-11-21 — expo-chapter drain (session https://claude.ai/code/session_01Qmmkt5JeUvGF2FboRQJbLN, issue #8826)

Done on branch `claude/expo-chapter-drain-2026-11-21` (bd9168d5a): `cites: ["jones1987", "kimlee2018"]` on `jones-markov-trace.ts`. Kim–Lee checked in the held copy (`library/fd58d8e182edda805fed0946606c5ab82f81/sections/page-003.md`, page-004): the standard-monomial count is the Catalan number C_n. Not done: Fan 1997 (not registered), the Catalan citation at `markov-trace-frobenius-selection.md:82`, and a `-- Ref:` on `TemperleyLiebTower.lean` (needs lean-direct).
