# OV tower — remaining proof obligations (post-merge scoping)

**Date:** 2026-06-29
**Status:** the Okounkov–Vershik tower is **fully landed on `main`**. This doc
scopes the residual proof debt — every remaining `sorry` — into a navigable,
dependency-ordered research plan with classical references and a tractability
assessment, so future sessions / siblings can pick up individual obligations.

## What landed (merged `main` commits)

| Brick | File | Merge SHA |
|-------|------|-----------|
| 2 — Specht module `S^μ` | `QOU/BraidKnot/Specht.lean` | `bc4ec72c` |
| 3 — classification index | `QOU/BraidKnot/SpechtClassification.lean` | `61aab78c` |
| 5 — Jucys–Murphy / contents | `QOU/BraidKnot/JucysMurphy.lean` | `77b674f0` |
| 4 — standard-basis theorem | `QOU/BraidKnot/SpechtStandardBasis.lean` | `703e4b0e` |
| TOP — capstone | `QOU/BraidKnot/OVTopAssembly.lean` | `eb366ba6` |

Brick 1 (`StandardYoungTableau.lean`, `numSYT`) was already on `main`; its
`numSYT_mul_hookProduct` (Frame–Robinson–Thrall HLF) is a separate sibling
effort (PRs #2984 / #2986), out of scope here.

None of these modules is imported by the `QOU.BraidKnot` umbrella — they carry
honest `sorry`s and are deliberately kept out of the CI sorry-free surface.
All foundations are sorry-free + axiom-clean; **14 `sorry` tactics remain**, all
the genuinely deep classical theorems.

## What is already sorry-free (the foundations + this session's discharges)

- Brick 2: `Tableau`, the `S_n`-action, `rowStab`/`colStab`, `Tabloid`
  (Fintype/DecidableEq), `Mtab` + its `Representation`, `polytabloid`,
  `SpechtSubmodule`.
- Brick 3: `PartitionIndex`, `DecidableEq YoungDiagram`, `IsRepIso`
  (+refl/symm/trans), `transportPermHom`, `spechtRep`/`spechtRepOn`,
  **`partitionEquivYoungIndex`** (proved — `ofRowLens` round-trip),
  `instFintypePartitionIndex`, `card_partitionIndex`,
  `card_irreducibles_eq_card_partitions`, **`specht_smul_mem`** (proved — colStab
  conjugation + sign invariance).
- Brick 5: `jucysMurphy`, `cellContent`, `contentSqSum`, `centralC2`,
  `centralC2_eq_sum_jucysMurphy_sq` (`= RegularRepTrace.centralC2` by `rfl`),
  `centralC2_coeff_one`, **`jucysMurphy_commute`** (proved — Jucys's involution).
- Brick 4: `cellLabel`(+inj/bij), **`instFintypeStandardYoungTableau`** (closed
  brick 1's open instance), `sytToTableau`, `standardPolytabloid`(+mem/corestrict),
  `standardBasis` + `specht_finrank_eq_numSYT` (sorry-free **modulo** the two §4
  content facts).

## The 14 remaining obligations

### Group A — the standard basis (brick 4) — *most tractable, self-contained*

| # | Obligation | Ref | Notes |
|---|-----------|-----|-------|
| A1 | `standardPolytabloid_linearIndependent` | [sagan2001] 2.5.2 | unitriangularity in the **dominance order**: `e_T = ±{T} + (dominated)`; distinct standard `T` ⇒ distinct leading tabloids. Needs: a dominance partial order on `Tabloid μ`, the leading-tabloid map, and a Mathlib "triangular family ⇒ independent" lever. |
| A2 | `standardPolytabloid_span` | [sagan2001] §2.6 | the **Garnir relations**: every polytabloid straightens to a `ℤ`-combination of standard ones. Needs the Garnir element + the straightening algorithm. Slightly harder than A1. |

A1+A2 ⇒ `standardBasis` ⇒ brick-4 `specht_finrank_eq_numSYT` (already wired). They
are pure `S_n`-combinatorics on tabloids — **no** representation-theoretic
prerequisites — which is why they are the recommended entry point.

### Group B — irreducibility + classification (bricks 2, 3)

| # | Obligation | Ref | Depends on |
|---|-----------|-----|-----------|
| B1 | `Specht.specht_isSimple` (`S^μ` irreducible /char 0) | [james1984representation] | the James submodule theorem + the `S_n`-invariant bilinear form on `M^μ`; needs the standard basis (A) for dimension counts |
| B2 | `SpechtClassification.specht_pairwise_noniso` | [james1984representation] | B1 + the bilinear-form / Hom-space argument |
| B3 | `SpechtClassification.specht_exhausts_irreducibles` | [sagan2001] §2.4 | char-0 semisimplicity (Maschke, on `main`) + `#{S^μ} = #conj classes = #partitions` (the count is `card_irreducibles_eq_card_partitions`, already sorry-free) + B1/B2 |

### Group C — the Okounkov–Vershik eigenvalue theorem (brick 5)

| # | Obligation | Ref | Depends on |
|---|-----------|-----|-----------|
| C1 | `JucysMurphy.jucysMurphy_eigenvalue` (GZ/seminormal basis exists + diagonalises the `X_k` by cell contents) | [vershik-kerov1977] | the **branching rule** `S^λ↓ = ⊕_{μ⋖λ} S^μ` + the spectrum of the GZ algebra; the deepest single obligation (this *is* the OV paper) |
| C2 | `JucysMurphy.centralC2_acts_by_contentSqSum` (`C₂` acts on `S^λ` by `Σc²`) | [vershik-kerov1977] | C1 (an eigenvector) + B1 (`S^λ` simple ⇒ central `C₂` acts by a scalar, Schur) + the reindex `Σ_k content(cellOf k)² = Σ_{c∈λ} c²` (the reindex alone is sorry-free-able) |

### Group D — the capstone (`OVTopAssembly`) — *gated on the classification*

The six `snSpectralData` fields. `Idx`/`fintypeIdx`/`d`/`ω` are already sorry-free.

| # | Field | Depends on |
|---|-------|-----------|
| D1 | `p` (the `λ`-isotypic block) | **the critical-path obligation** — re-indexing the abstract Wedderburn blocks of `WedderburnSn.sn_wedderburnArtin_algClosed` (an existential `∏ Matrix` equiv) by `PartitionIndex` via the classification (B3) |
| D2 | `proj` | D1 (the block idempotent of the matrix decomposition, transported to `Module.End` via `LinearMap.mulLeft`) |
| D3 | `isProj` | D2 (idempotency of the central block idempotents) |
| D4 | `rank` (`finrank (p i) = d i ^ 2`) | D1 + brick-4 `specht_finrank_eq_numSYT` (A) + `WedderburnSn.sn_block_finrank_sq` |
| D5 | `decomp` (`mulLeft C₂ = Σ ω_i·proj_i`) | D2 + brick-5 `centralC2_acts_by_contentSqSum` (C2) + the `rfl` bridge `centralC2_eq_sum_jucysMurphy_sq` |
| D6 | `complete` (`Σ proj_i = id`) | D1 + completeness of the Wedderburn idempotents + `card_irreducibles_eq_card_partitions` |

## Dependency graph + critical path

```
        A1 ─┐
        A2 ─┴► standardBasis ► specht_finrank_eq_numSYT ─────► D4 (rank)
                                            │
        B1 (isSimple) ─┬► B2 ─┐              │
                       └──────┴► B3 ─────────┼► D1 (p) ► D2 (proj) ► D3 (isProj)
                                             │                       └► D6 (complete)
        C1 (OV eigenvalue) ► C2 (Σc² action) ┴──────────────────────► D5 (decomp)
                                                              │
                                         D1..D6 ► snSpectralData ► identityB_general
```

**Critical-path obligation: D1 / B3 — the Wedderburn-block ↔ partition
identification.** It underlies four capstone fields (D1/D2/D3/D6) and is the
representation-theoretic heart (B3). It needs the classification (B-group) *and*
the extraction of concrete idempotents from `WedderburnSn`'s currently-existential
`∏ Matrix` equiv (`Nonempty (… ≃ₐ …)` → a chosen, idempotent-bearing
decomposition). This is the single highest-leverage target.

## Recommended attack order (future sessions)

1. **A1, A2** (standard basis) — most self-contained, pure tabloid combinatorics,
   no rep-theory prerequisites; closes brick 4 outright and feeds D4.
2. **B1** (`specht_isSimple`) — needs the `M^μ` bilinear form; unblocks B2/B3 and C2.
3. **B3 + D1** (classification + isotypic re-indexing) — the critical path; the
   bulk of the capstone follows (D2/D3/D6) once D1 lands.
4. **C1** (OV eigenvalue) — the deepest; needed only for D5.

Each is a multi-session / potential-Mathlib-contribution effort (Specht modules
and the OV approach are long-standing Mathlib desiderata). The framework
consequence is modest and unchanged from the roadmap's honest assessment:
discharging these makes rigorous one leg (Identity (B)) of *Identity I*, a
**carried** input to the s5-so3 keystone — it removes a conditional from a
supporting lemma; it does not change any predicted observable or advance the
keystone's own assumptions.

## Cleanup note (non-blocking)

Brick 2's in-place `Specht.specht_finrank_eq_numSYT` stub and brick 4's
`SpechtStandardBasis.specht_finrank_eq_numSYT` (proved modulo A1/A2) are the **same
statement**. Brick 2 cannot import brick 4 (brick 4 imports brick 2), so they
cannot be wired directly. A future consolidation could move the standard-basis
machinery so the single reduction lives downstream of both; until then, A1/A2
discharge brick 4's copy, and brick 2's in-place copy should be discharged by an
independent (duplicated) standard-basis argument or removed in favour of a
forward-reference in its docstring.

## References

Citation keys resolve against `content/schema/references.ts` (the corpus
bibliography source of truth):

- **[sagan2001]** Sagan, Bruce E. (2001). *The Symmetric Group: Representations,
  Combinatorial Algorithms, and Symmetric Functions*. Springer, New York. —
  standard tableaux, tabloids, polytabloids; the standard basis (Thm 2.5.2), the
  Garnir relations (§2.6), and the classification of irreducibles (§2.4).
- **[james1984representation]** James, Gordon; Kerber, Adalbert (1984). *The
  Representation Theory of the Symmetric Group*. Encyclopedia of Mathematics and
  its Applications, vol. 16. Cambridge University Press. — Specht modules, the
  James submodule theorem, irreducibility and pairwise non-isomorphism in
  characteristic 0. (`references.ts` carries an unresolved edition/year caveat:
  the original is Addison–Wesley 1981, with a later CUP reprint; see
  [`docs/audits/2026-06-23-bibliography-doi-verification-doth.md`](../audits/2026-06-23-bibliography-doi-verification-doth.md) §C.)
- **[vershik-kerov1977]** Vershik, Anatoly M.; Kerov, Sergei V. (1977).
  *Asymptotic theory of characters of the symmetric group*. — the foundational
  Vershik–Kerov paper; the specific Jucys–Murphy-element = cell-content eigenvalue
  theorem cited in group C (C1/C2) is the Okounkov–Vershik "new approach to the
  representation theory of the symmetric groups" refinement of this line.
- **[fulton1997]** Fulton, William (1997). *Young Tableaux*. London Mathematical
  Society Student Texts 35. Cambridge University Press. — Young diagrams, tableaux,
  and the combinatorics of standard fillings.
