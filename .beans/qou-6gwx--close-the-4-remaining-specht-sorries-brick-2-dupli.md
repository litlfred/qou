---
# qou-6gwx
title: Close the 4 remaining Specht sorries (brick-2 duplicates + classification cores)
status: in-progress
type: task
created_at: 2026-08-08T11:16:42Z
updated_at: 2026-08-08T11:16:42Z
---


Four `sorry` tactics remained in `QOU/BraidKnot/Specht*.lean` after
`specht_form_nondegenerate` was closed (see qou-0xyc). Verified by
`grep -E '^\s+sorry\s*$'`, not by reading docstrings — several of those are
stale (qou-oacr).

## Todo

- [x] `Specht.specht_finrank_eq_numSYT` — brick-2 duplicate of a proved theorem
- [x] `Specht.specht_isSimple` — brick-2 duplicate of a proved theorem
- [x] Prerequisite for the third: `M^μ = S^μ ⊕ (S^μ)ᗮ` and stability of `ᗮ`
- [x] Combinatorial core of the third: Sagan Lemma 2.2.6
- [x] `SpechtClassification.spechtIso_imp_dom_both` — module-theoretic half
- [ ] `SpechtClassification.specht_exhausts_irreducibles` — completeness

## Summary of Changes

### The two brick-2 stubs — DELETED, not documented in place

Both statements are proved one layer up
(`SpechtStandardBasis.specht_finrank_eq_numSYT`,
`SpechtIrreducible.specht_isSimple`), and neither stub had a consumer — every
call site already used the wired/downstream version.

Deleting rather than annotating matters: a `sorry`-backed duplicate of a proved
theorem **typechecks and is usable**. Anything writing
`exact Specht.specht_isSimple …` would have obtained a `sorryAx`-tainted proof
of a statement available cleanly one module up, with no error anywhere. §6 of
`Specht.lean` now records where each proof lives and why it cannot be written
there (both run through modules that import `Specht`).

One real generalization is noted rather than re-stubbed: the deleted finrank
statement had **no** `CharZero` hypothesis; the proved one does. Probably
removable, but it needs `standardBasis`'s `CharZero` uses traced.

Also dropped the unused `μ.card ≠ 0` from `specht_form_nondegenerate` and
`specht_isSimple`. It was retained last commit only to match the brick-2
contract, which no longer exists — and keeping it actively blocked
`isCompl_specht_perp`, which cannot be stated for every `μ` if its input
demands a nonemptiness proof `μ = ∅` cannot supply.

### Toward `spechtIso_imp_dom_both` — two of four pieces proved

Sagan's Thm 2.4.4 is `Hom(S^μ, M^ν) ≠ 0 ⇒ μ ⊵ ν`; an isomorphism supplies
nonzero homs both ways, and `partitionDom_antisymm` (already proved) finishes.
The proof has four pieces:

| Piece | Status |
|---|---|
| `M^μ = S^μ ⊕ (S^μ)ᗮ`, `ᗮ` `S_n`-stable | **DONE** — `SpechtIrreducible.isCompl_specht_perp`, `spechtPerp_stable` |
| Sagan Lemma 2.2.6 (no-clash ⇒ dominance) | **DONE** — `SpechtCrossDominance.dominance_of_noclash` / `_of_tableau_noclash` |
| cross-shape `κ_t` acting on `M^ν`, and clash ⇒ `κ_t {s} = 0` | open |
| extension `θ̃ : M^μ → M^ν` and the assembly | open |

Both new results are `sorry`-free and axiom-clean.

The decomposition became available only because `specht_form_nondegenerate`
supplies Mathlib's missing hypothesis in
`isCompl_orthogonal_of_restrict_nondegenerate`.

Lemma 2.2.6 turned out cheap: `SpechtIrreducible` §4.x already contained the
**same-shape** case of exactly this count, inside `row_lt_colLen`, where it
feeds the Gale–Ryser matching. Its two cell-counting ingredients
(`filterCard_reindex`, `colCells_card`) were `private`; they are now public and
imported rather than re-derived. What was new is only `card_cells_row_lt`
(cells in the first `r` rows number `Σ_{j<r} μ_j`) and the cross-shape
statement, which is phrased on a bare label type with the fiber counts as
hypotheses so it applies across two shapes without transporting a tableau.

### What remains, precisely

**`spechtIso_imp_dom_both`.** The open half is module-theoretic, and its cost is
mostly the `nOf μ = nOf ν` transport: `colStab t ≤ Perm (Fin (nOf μ))` has to
act on `Mtab ν`, whose representation takes `Perm (Fin (nOf ν))`. Concretely:

1. `kapCross t : Mtab ν →ₗ Mtab ν`, `Σ_{π ∈ colStab t} sgn π • rep_ν (cast π)` —
   mirrors `SpechtIrreducible.kapL`.
2. clash ⇒ `kapCross t {s} = 0` — mirrors `kap_of_mem_line_clash`, the
   sign-reversing involution.  Its contrapositive is the no-clash hypothesis of
   `dominance_of_noclash`.
3. `θ̃ := θ ∘ (projection onto S^μ)`, a `k[S_n]`-map by `isCompl_specht_perp`
   plus `spechtPerp_stable`.
4. `θ̃(e_t) = kapCross t (θ̃ {t})`; expand `θ̃ {t}` in the ν-tabloid basis; some
   coefficient survives, so `kapCross t d ≠ 0` for some ν-tabloid `d`; feed
   `tabloidRowPattern d` (`SpechtDominanceCore`) into `dominance_of_noclash`.

Estimate: 250–400 lines, one focused session. Nothing further is missing from
Mathlib.

**`specht_exhausts_irreducibles`.** Genuinely larger and *not* reducible to the
above. The standard route is a count — #simple `k[S_n]`-modules = #conjugacy
classes = #partitions — which over an arbitrary characteristic-zero field needs
`S_n` to be split (all irreps realizable over `ℚ`). `WedderburnSn` supplies
Wedderburn–Artin for `k[S_n]` but its block count `N` is abstract, not
identified with the partition count; closing that identification is the work.
Not attempted. Its own bean is sp06.

## Update — `spechtIso_imp_dom_both` is PROVED (3 of 4 done)

`SpechtClassification.spechtIso_imp_dom_both` and `specht_pairwise_noniso` both
report `[propext, Classical.choice, Quot.sound]`. Sagan Thm 2.4.4 in full.

New module `QOU/BraidKnot/SpechtCrossKappa.lean`, sorry-free:

- `transportPerm` — permutations along `nOf μ = nOf ν`; definitionally the same
  term as `SpechtClassification.transportPermHom`, which is downstream and so
  cannot be imported.
- `kapCross` — `κ_t = Σ_{π ∈ C_t} sgn(π)·π` for a **μ**-tableau `t` acting on
  **M^ν**. With `ν = μ`, `h = rfl` it is `SpechtIrreducible.kapL`.
- `kapCross_of_eq_zero_of_clash` — the sign-reversing involution, cross-shape.
- `dominance_of_kapCross_ne_zero` — its contrapositive composed with Lemma 2.2.6.
- `kapL_kapL`, `kapL_polytabloid`, `polytabloid_ne_zero`.

Assembly is `SpechtClassification.dom_of_intertwiner`.

### The plan in this bean was wrong about the hard part

It said the remaining work was "extend `θ : S^μ → M^ν` to `M^μ` along
`isCompl_specht_perp`" — the textbook step, and the reason the orthogonal
decomposition was proved first. **That step is not needed.**

The textbook writes `θ(e_t) = θ(κ_t {t}) = κ_t θ({t})`, which requires `θ` at
the tabloid `{t} ∉ S^μ`, hence requires `M^μ = S^μ ⊕ (S^μ)ᗮ`. But

    κ_t e_t = |C_t| · e_t          (`kapL_polytabloid`)

stays **inside** `S^μ`. So equivariance of `θ` on `S^μ` alone already gives

    κ_t (θ e_t) = |C_t| · θ(e_t) ≠ 0

which is everything the dominance argument consumes. No extension, no
projection, no equivariance-of-the-projection lemma.

`isCompl_specht_perp` and `spechtPerp_stable` are therefore **not** on the
critical path. They stay as the honest orthogonal decomposition — worth having,
and they cost little — but the bean's sizing (250–400 lines, dominated by the
extension) mis-attributed the difficulty. Actual cost was ~200 lines, dominated
by the `nOf μ = nOf ν` transport.

### Friction worth recording

- `map_smul` does not fire on a `ℤ`-scalar against a `k`-linear map; `map_zsmul`
  does. Cost two compiles.
- `Quotient.exists_rep` returns `⟦s⟧`, which `rw` will not match against
  `Tabloid.mk s` even though they are definitionally equal. `show` bridges it.
- `Nat.cast_smul_eq_nsmul` is stated `(n : R) • b = n • b`, so converting an
  `ℕ`-smul goal into a `k`-smul one needs `←`.
- `Subtype.ext h` with `h : ↑x = 0` elaborates to a metavariable equation unless
  the expected type is given; bind it with `have h0 : e y = 0 := Subtype.ext hzero`.

### Remaining

Only `specht_exhausts_irreducibles` (bean sp06). Genuinely separate: it needs
#simple `k[S_n]`-modules = #partitions, i.e. `WedderburnSn`'s abstract block
count identified with the partition count. Not reachable from this chain.
