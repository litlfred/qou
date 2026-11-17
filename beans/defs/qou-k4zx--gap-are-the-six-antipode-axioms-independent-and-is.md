---
# qou-k4zx
title: 'GAP: are the six antipode axioms independent, and is the braiding instance over-applied?'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-15T08:45:13Z
updated_at: 2026-10-04T15:19:44Z
parent: qou-6qbv
---

## Two loose ends from the 2026-09-15 antipode change (`qou-c64q`), both found by red-teaming it

### 1. Independence of the six antipode axioms -- UNMEASURED

`def:frobenius-hopf-substrate` axiom 2 now asserts six laws on `S`:
anti-algebra, anti-coalgebra, `S(1) = 1`, `eps . S = eps`, `S^2 = id`,
`lambda . S = lambda`.

Classically the first two are THEOREMS derived from the convolution antipode
axiom, not axioms. Here they are asserted, because the convolution axiom is
gone (it has no models -- `qou-aawz`). Nobody has checked whether any of the
six follows from the others plus the Frobenius relation, the unit/counit laws
and the snake identities.

Asserting a redundant axiom is not a defect, but AGENTS.md's derive-then-check
discipline says measure it rather than assume it, and that was not done.

**How to settle it:** for each of the six, try to derive it in Lean from the
other five plus the structure axioms; where that fails, exhibit a model
satisfying five and violating the sixth. The `k[G]` probe harness
(`computations/probes/frobenius_hopf_intermediate_axioms_probe.py`) already has
every check as a separate predicate, so the counterexample search is cheap --
vary `S` over all `|G|^|G|` basis-permutation candidates for small `G` and look
for one satisfying five of six.

### 2. `[BraidedCategory C]` may be over-applied -- 55 added occurrences

The change gave `FrobeniusHopfData` a `[BraidedCategory C]` parameter, which had
to be threaded through its consumers. Six files were patched with a BLANKET
regex that added the instance to EVERY `MonoidalCategory` binder in the file,
including declarations that never touch `FrobeniusHopfData`.

Those declarations are now over-constrained: usable only in a braided category
where any monoidal one would previously do. Practical harm is low -- QOU's
ambient is braided throughout, and `QuantumUniverse` carries the instance -- but
it is a silent narrowing of the library's generality that nobody asked for, and
it is exactly the kind of thing a mechanical diff hides.

**How to settle it:** for each added instance, remove it and recompile the
module; keep the removal where the module is still clean. ~55 compiles, each a
few seconds against the restored olean shadow. Files to check first are the six
blanket-patched ones: `Instanton`, `ChannelSeparation`, `LightningPath`,
`QDifferentialGeometry`, `Torsion/Descent`, `CategoricalDqSquared`.

Both items are recorded in the red-team section of
`docs/audits/2026-09-15-antipode-anti-automorphism-package.md`.


## MEASURED 2026-09-15 — 1 of 6 independent

`computations/probes/frobenius_hopf_axiom_independence_probe.py`. Semantic
counter-models on `k[G]`: the structure maps involve no `S`, so the six
conditions are the only thing varying. Monomial candidates, exhaustive
`|G|^|G|` up to `S_3` (46656); `D_4`'s 40320 bijections only.

**Only `involutive` is proved INDEPENDENT.** Witness on `V_4`: the 3-cycle on
the three non-identity elements fixing the identity — an automorphism, hence an
anti-automorphism since `V_4` is abelian, satisfying the other five, but of
order 3 so `S^2 != id`.

The other five have no counter-model in the searched space. That is a statement
about the space, so the probe also measures WHY — minimal forcing subsets, on
two exhaustively-searched groups on opposite sides of commutativity:

    1 anti_mul    <= {2}                    on V_4 and S_3 alike
    3 unit        <= {1} or {2} or {4} or {6}
    4 counit      <= {2} or {6}
    6 form        <= {2} or {4}
    2 anti_comul  <= {1,4} or {1,5} or {1,6}

Three readings:

1. **`anti_mul` follows from `anti_comul` alone, on both groups.** If that
   survives categorically the package carries a redundant axiom in its most
   load-bearing position — `anti_mul` is what excludes `S = id`.
2. **`unit` is forced by any ONE of four others** — but it is provably NOT
   redundant in general. Chasing `antipode_anti_mul` through the unit laws gives
   only `s = (s (x) s) >> beta >> mu` for `s = eta >> S`, an idempotent-like
   condition. A monomial `S` on a group algebra lands on a group ELEMENT, where
   idempotent forces the identity; a general algebra has non-invertible
   idempotents. So on this axiom the family answers the OPPOSITE of the
   categorical truth, which is the reason not to shrink the structure on this
   evidence.
3. **`counit` and `form` force each other both ways, on every group.** The
   predicted blind spot, checked rather than assumed: on `k[G]` the counit and
   the Frobenius form are the same map. In the Lean structure they are separate
   fields tied by NOTHING (`frobeniusForm` appears only in the two snake
   identities), so deciding them needs a Frobenius object with `lambda != eps`.

Self-validation: `V_4` and `S_3` agree on every row except axiom 2, where `V_4`
carries three extra forcings (`{3,5}`, `{4,5}`, `{5,6}`) — exactly the abelian
artifact the two-column design anticipated. A forcing in both columns is the one
worth citing. `D_4` excluded from the table: bijections-only search would
manufacture forcings involving `involutive`.

## Still open (do NOT close)

- Does `anti_comul => anti_mul` hold CATEGORICALLY, or is it an artifact of
  monomial maps on group algebras? This is the live question and it is a
  formalize-first target, not another search.
- Are `counit` and `form` independent? Needs a Frobenius object with
  `lambda != eps`; no such model is in the corpus.
- The braiding-instance over-application (six blanket-patched consumer files)
  is untouched by this measurement.

## Progress Update (Round 59 — PR #8316)
- **Status:** `in-progress` (opened `litlfred/qou#8316`, branch `claude/round59-devacuify-6qbv-b9cj`, HEAD `53b4a670e74a8018b8da97a71f572d818338e732`, C1 `76d4ce5f89f2c26a87c0da074bf6c76b37e0ea03`).
- **Target:** `folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/AntipodeIndependence.lean` + 80-dps witness `computations/probes/round59-devacuify-6qbv-b9cj.witness.json` (`scriptHash = 80c9bce8d43a`, `allPassed = true`, `0` `float64`).
- **Updated at:** `2026-11-17T10:55:34Z`.
