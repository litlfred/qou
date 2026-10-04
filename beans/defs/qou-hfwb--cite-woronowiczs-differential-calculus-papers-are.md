---
# qou-hfwb
title: 'CITE: Woronowicz''s differential-calculus papers are not held and the 4D bicovariant classification carries no Ref key — U+C — CalculusDimensionObstruction.lean:89-94, SelfDualityDegree.lean:89-90'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:04:51Z
updated_at: 2026-10-04T15:14:46Z
parent: qou-mub3
---

**Class U + C — the pivot of two sorry-free Lean files rests on a classification
that is neither held nor pointed at.**

**What is registered.** Four Woronowicz keys exist in `references.ts` and **none
carries a `library:` block**:

| key | work | held? | cited at |
|---|---|---|---|
| `woronowicz1987` | *Compact matrix pseudogroups*, CMP **111** (1987) 613–665 | no | `qou-exists-axiom-1-proof.md:4`, `qou-exists-axiom-1.ts` |
| `woronowicz1987-twisted-su2` | *Twisted SU(2) group. An example of a non-commutative differential calculus*, Publ. RIMS **23** | no | `brings-is-qou-proof.md:11,15`; `connection-su2.ts` |
| `woronowicz1988` | *Tannaka–Krein duality … Twisted SU(N)*, Invent. Math. **93** | no | `tannaka-krein-reconstruction.lean:73,111`, 5 `.ts` |
| `woronowicz1989` | *Differential calculus on compact matrix pseudogroups (quantum groups)*, CMP **122** | no | `categorical-lichnerowicz.lean:41`, `categorical-reeb-brings.ts` |

**Nothing is held.** `library/` has **0** files containing the phrase
*"differential calculus"*, **0** containing *"bicovariant"*, **0** containing
*"left-covariant"*, and **0** `INDEX.md` rows for `Woronowicz` / `pseudogroup` /
`twisted SU`. (`Woronowicz` matches 13 section dirs — all citing him in *other*
papers' bibliographies and text, not his own papers.)

**The C half: the 4-dimensional bicovariant classification has no `-- Ref:` at all.**

- `lean/QOU/QuantumObservableUniverse/SelfDualityDegree.lean:89-90` — *"anything
  about Woronowicz's classification. That `𝒪_q(SU(2))` also admits **4-dimensional
  bicovariant** calculi is standard and cited, not formalised"*.
- `lean/QOU/QuantumObservableUniverse/CalculusDimensionObstruction.lean:89-94` —
  *"the Woronowicz structure equations, or that `Ω¹(𝒪_q(SU(2)))` is free of rank 3
  … (Woronowicz's classification), cited, and `library/` holds no source on it"*.

**Both files carry zero `-- Ref:` lines.** So "cited" is a description of intent,
not a citation. And `CalculusDimensionObstruction` is the file whose whole point is
that no calculus dimension satisfies both the contact requirement (odd) and the
self-duality requirement (4) — the classification is its load-bearing premise.

**Flag, not an assertion.** The corpus attributes the 4D bicovariant classification
for `SL_q(2)`/`SU_q(2)` to *"Woronowicz's classification"*. Woronowicz 1989 sets up
the bicovariant framework; the *classification for this specific quantum group* is
usually attributed to **Schmüdgen & Schüler, *Classification of bicovariant
differential calculi on quantum groups*, CMP 170 (1995) 315–335**, with related work
by **Stachura**. I have **not** verified which paper actually contains the statement
the corpus needs — external egress is 403 this session (`api.crossref.org`,
`export.arxiv.org`) — so **whoever picks this up must check the attribution before
writing a locator**, not just add a key.

**Fix, in order:**
1. Add `-- Ref:` lines at `SelfDualityDegree.lean:89` and
   `CalculusDimensionObstruction.lean:89`, once (2) settles which key is right.
2. Verify the attribution and, if it is Schmüdgen–Schüler, register that paper.
3. Ingest at least `woronowicz1987-twisted-su2` (Publ. RIMS 23, 117–181) so the
   3-dimensional calculus the framework declares is checkable in-corpus; it is
   currently cited three times with nothing behind it.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.
