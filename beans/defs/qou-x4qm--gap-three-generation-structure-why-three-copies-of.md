---
# qou-x4qm
title: 'GAP: three-generation structure — why three copies of each fermion; prior to CKM/PMNS'
status: todo
type: task
priority: normal
tags:
    - sm-26
    - reorg-2026-10-04
    - 8f-gen
    - 8f-open
created_at: 2026-07-31T20:15:08Z
updated_at: 2026-10-10T12:23:30Z
parent: qou-8lxd
blocked_by:
    - qou-xtcl
    - qou-7opd
---

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-q-alg-9504020v1/  ->  [kashaev1995]
  A link invariant from quantum dilogarithm

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [kashaev1995] as the citation key when you do it.

## 🔥 Roast (2026-09-03, qou-bsu0)

(i) Needs a derivation that the fermion count per charge is three — a physical bridge "normal-form-independent winding ⇒ generation".
(ii) What exists: the genus bound admits n ∈ {3,5,7,9}; continuant divisibility b_a | b_n ⟺ a | n (sorry-free) marks 9 as harmonic — removing one of four on a criterion unrelated to generation counting (`qou-a5os`); the S₅ filter gives {3,5} instead (`prop:s5-equivariant-torus-knots`); `generation-completeness.lean` is vacuous (`qou-0avp`); the fivefold-charts remark supplies no premise (embeddings ≠ isomorphism classes, 3+2 split). Excluded: nothing.
(iii) Trap: "any criterion removing one of four leaves three"; forcing 60 Weierstrass points into 3×20 (`qou-ak28`); Koide democracy (`k9td`).
(iv) Next: prove or refute that a composite odd winding cannot carry a generation (`qou-xtcl`'s one lemma) AND reconcile the two filters — two filters, two counts, is the live defect. Flavour generations sit downstream of 4-A; the lepton count does not.
(v) Forecast: a proof that the filters disagree is likelier than a derivation of three.
Tower status [reading: qou-ggdk]: MIXED — the divisibility is exact in q but on H₂(q) continuants; the tower-level object is the ℓ-degree branching (e ℓ=1, μ ℓ=2, τ ℓ=3; `S5SO3FiberAction.lean`), a scaffold with no instance.


## Correction 2026-10-10 — the roast says "two filters, two counts"; it is THREE

Roast item (iv) names the live defect as *"reconcile the two filters — two
filters, two counts"*. Measured during the `8f-gen` front triage, the corpus
carries **three**, returning **4 / 3 / 2**:

| # | filter | admits | count |
|---|---|---|---:|
| 1 | Seifert genus `≤ 4` | `{3,5,7,9}` | **4** |
| 2 | continuant divisibility (`9 = 3·3` harmonic) | `{3,5,7}` | **3** |
| 3 | `S₅`-equivariant embedding | `{3,5}` | **2** |

The roast has all three ingredients in item (ii) — it just does not add them
up as three *counts*: it treats the divisibility as "removing one of four" and
the `S₅` filter as "giving {3,5} instead", which is right, and then calls the
tension two-way.

**And the sharper form the roast misses: filters 1 and 3 are two properties of
the SAME object.** `brings-surface-def.md` states both in one sentence — `Σ₄`
is *"a smooth projective curve of genus 4. Its automorphism group is
`Aut(Σ₄) ≅ S₅`."* So they are not alternatives to adjudicate between; they are
two constraints imposed by one surface, and they return four and two. **Three
is produced by neither of them** — only by filter 2, whose criterion
`qou-a5os` already established is unrelated to generation counting.

That strengthens the roast's own forecast (v) — *"a proof that the filters
disagree is likelier than a derivation of three"* — into something closer to a
prediction: the disagreement is not between two candidate criteria but inside a
single geometric object, so it cannot be resolved by preferring one source over
the other.

Full measurement, the three dispositions (including that filter 3 read as *the*
criterion yields **two** generations and refutes the headline claim), and the
scope note on filter 3's Lean being `trivial`/1-step per the corpus's own
`lean-triviality.json`: **`qou-xtcl`**, which was title-only until today and now
carries it. This bean is already `blocked-by` it.

Tagged `8f-open`.
