# The Matsumoto reduction of the general-rank braid + ρ-equivariance of the channels (2026-07-19)

**Bean:** `qou-mats`. **Lean:** [`QOU/Machinery/HeckeDihedralBraidReduction.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/HeckeDihedralBraidReduction.lean)
— sorry-free, `lean`-direct exit 0.

## Wall 1 — the exchange/Matsumoto layer, reduced

The general-rank braid relation is formalized by the classical parabolic
localization: a **`DihedralCosetStructure`** packages the coset datum for an
adjacent generator pair — `W ≃ C × Fin 6` (coset space × the S₃ cell in the
merged NF order), length additivity `ℓ(u₀d) = ℓ(u₀) + ℓ_D(d)`, and cell-wise
generator actions by the proved n=3 tables. From that datum alone:

- the two induced `DescentStructure`s (involution + toggle inherited from
  the `decide`-checked cell data);
- **`restrict_i` / `restrict_j`** — over each coset the action IS the
  proved n=3 σ₀/σ₁ action on the fibre;
- **`braid_of_dihedral`** — `σᵢσⱼσᵢ = σⱼσᵢσⱼ` on the whole module,
  localized to the fibres and closed by the merged `H3.braid_operator`
  (`cell_braid`);
- **`dihedralSelf`** — the n=3 self-instance (trivial coset space):
  non-vacuous inhabitation, re-deriving the concrete braid.

**The remaining open content of the general-rank braid is now exactly one
combinatorial fact**: every Coxeter system carries a
`DihedralCosetStructure` for each adjacent pair (the standard parabolic
coset decomposition, Bourbaki Lie IV–VI §1). The algebra is done; the
combinatorics is the isolated residue.

## Wall 2 — ρ-equivariance of the channel pair (B1 dictionary, module level)

- **`mulStep_star`** — entrywise conjugation intertwines the generator
  action with `h ↦ star h` (the descent test is real, so conjugation passes
  through the length rule);
- **`channel_plus_star` / `channel_minus_star`** — conjugation carries the
  e₊/e₋ channel vectors at `q` to the corresponding channel vectors at
  `star q` of the conjugated state, at every rank. On the fibre circle
  `|q| = 1`, `star q = q⁻¹`: conjugation implements the bar-involution
  `ρ : q ↦ q⁻¹` on the channel data — **`F∘ρ = conj∘F` at the module
  level**, the algebraic twin of the geometric
  `deck_eigenspace_exchange` (T3, merged).

## Honesty

`braid_of_dihedral` is conditional on the coset datum (existence for
general Coxeter systems not proved; no general-n class instance declared).
The ρ-equivariance is the equivariance *datum* of the τ-functor target,
not the functor's existence — `TauRhoHodgeLift` stays open. Nothing wired;
`1/(8π)` stays phase-4. §7c: `CommRing` for wall 1; `ℂ` only in the star
section (pre-archimedean).
