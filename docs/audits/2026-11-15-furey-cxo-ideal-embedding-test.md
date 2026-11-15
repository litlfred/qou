# Furey's ℂ⊗𝕆 minimal left ideals, formalised, and the tower-embedding test

Bean `qou-s4xb` (epic `qou-8lxd`), stream 15. Issue #7871, PR #7872.
Lean: `QOU/Eightfold/FureyMinimalLeftIdeal.lean` (the algebra, generic ring) and
`QOU/Eightfold/FureyIdealTowerTest.lean` (the ideal, `su(3)`, and the test).

**Verdict: (c).** No map from the tower's flavour-and-chirality data into `S_u`, `S_d` is
forced by structure both sides carry *and* reaches the quark states. The chirality part
alone is (b): it is unique up to a scalar on each line and up to the swap `i ↔ −i`. Its image
is the two lepton singlets `ν`, `e⁺`. The extra choices needed are listed in §4.

## 1. Sources held

Corpus-grep path 5, all four tiers, run 2026-11-15:

| Source | Held? | Where |
|---|---|---|
| Furey thesis 2016, *Standard model physics from an algebra?* (arXiv:1611.09182) | **yes**, 57 sections | `library/arxiv-1611.09182v1/`; §6.6 *Minimal left ideals* = `sec-038-66-minimal-left-ideals.md` (eqs. 6.19–6.21) |
| Gresnigt 2019 (`gresnigt2019`, arXiv:1901.01312) | yes | `library/arxiv-1901.01312v1/` |
| Furey 2018, ℂ⊗ℍ electroweak (arXiv:1806.00612) | PDF only | `uploads/1806.00612v1.pdf`, **not ingested** (no `library/` sections) |
| Furey 2016, *Phys. Lett. B* "Charge quantization from a number operator" / the journal version of the ideal construction | **not held** | — |

Stream 13 should fetch: (i) ingest `uploads/1806.00612v1.pdf` into `library/`;
(ii) the Phys. Lett. B journal paper(s), if the owner wants them cited alongside the thesis.
The thesis §6.6 is the citation used here. It states every object formalised below.

## 2. What is formalised (Step 1), all sorry-free

Conventions. The octonion table is the corpus table (`omul_map`). The special unit is the
corpus colour unit `e₁`. Furey's convention uses `e₇` instead. The index shift `k ↦ k+1` is
an automorphism of the Baez table and maps her generators onto ours:
`α₁ = ½(−e₆+ie₅)`, `α₂ = ½(−e₄+ie₂)`, `α₃ = ½(−e₇+ie₃)`. Products of octonions act from the
left, `αβf := α(βf)`.

Base ring (§7c). The algebra is over a generic `CommRing` with `i·i = −1`. The ideal is over
a generic `Field`, `CharZero`, with such an `i`; the minimal case is `ℚ(i)`. `ℂ` is never used.

| Result | Lean |
|---|---|
| `βⱼ = 2αⱼ`, `βⱼ†` are left multiplications in the corpus table | `Bm_eq`, `Bd_eq` |
| `{αₐ, α_b†} = δₐ_b`, `{αₐ, α_b} = 0`, `{αₐ†, α_b†} = 0` (Cl(6)) | `car_Bm_Bd`, `car_Bm_Bm`, `car_Bd_Bd` |
| `ωω† x = ½(x₀ − i x₁)·Ω`, `Ω = 1 + i e₁` (rank one) | `omega_omegaD_apply`, `vacProj_apply` |
| `ωω†` is idempotent | `vacProj_idem` |
| `αⱼ Ω = 0` (Furey 6.20) | `Bm_vac` |
| `ω†ω` is rank one onto `Ω' = 1 − i e₁ = Ω(−i)`: `S_d` is the Galois image | `omegaD_omega_apply` |
| `α†ⱼ = −αⱼ` at the opposite root | `Bd_eq_neg_Bm_neg` |
| `S_u = End·ωω†` is a left ideal, `≅ 𝕆_K`, **dim 8**, **minimal** | `Su_left_ideal`, `SuEquiv`, `finrank_Su`, `Su_minimal` |
| Furey's eight states (6.19) are the stated raising chains on `Ω`, and form a basis | `fock_chain`, `fock_linearIndependent` |
| Number operator: levels `0,1,1,1,2,2,2,3` | `numOp_fock` |
| `L(e₁) = −i·(−1)^N` on the eight states | `Le_fock` |
| corpus `su3 e₁` acts on `𝕆_K` by derivations | `extD_leibniz` |
| `su3` kills `ν`, `e⁺`; preserves levels 1 and 2 | `extD_su3_kills_fock0/7`, `extD_su3_mem_levelSpace` |
| the `su3`-invariant vectors are exactly `span(ν, e⁺)` | `su3_invariant_iff` |
| each level is spanned by its three Fock vectors | `level1_decomp`, `level2_decomp` |
| each triplet is irreducible under `su3 e₁` | `level1_irreducible`, `level2_irreducible` |

So the decomposition is `1 ⊕ 3̄ ⊕ 3 ⊕ 1` by level (Furey's `ν`, `d̄`, `u`, `e⁺`). The two
triplets are exchanged by `i ↦ −i`, and each is irreducible: any nonzero `su3`-stable
subspace that meets a level contains all three of its Fock vectors (added 2026-11-15).
The proof is the weight argument (`triplet_core`). Two Cartan elements, `octDer 7` and
`octDer 10`, act diagonally on the Fock vectors with eigenvalues `0, ±i`, so `x + H(Hx)`
picks out one weight line. Two root elements, `octDer 6` and `octDer 11`, then move between
the lines. The action table is `octDer_fock_action`. Irreducibility holds over every
characteristic-0 field containing `i`, not only over its algebraic closure.

## 3. The embedding test (Step 2)

Tower side. These are corpus facts, cited and not re-proved:

* the quark state is the `h¹` part of one letter, a scalar multiple of `1`
  (`QuarkState.quarkState_eq`). It carries no colour index;
* chirality is the eigenline pair `P±`, with `J = P₊ − P₋`, `J² = 1`
  (`OneSidedWeakVertex.grading_sq`). The left line is selected by `|eigenvalue| > 1`, which
  needs an **ordered** field (`LeftLineDefinition`, `WeakChiralityRootLabel`);
* flavour `σ ↔ σ⁻¹` fixes both eigenlines, so it is chirality-blind (`flip_eigenline_left`);
* the tower's colour is the level-3 `gl₃` Schur–Weyl. It is not an action of `su3 e₁`.

Which structures could force a map? An embedding by itself proves nothing, because any two
8-dimensional spaces are isomorphic. A forced map must intertwine structure. The candidates
on `S_u ≅ 𝕆_K` are:

* `su(3)`-equivariance, with the tower side trivial, because the tower has no `su3 e₁`
  action;
* the one canonical `ℤ/2` grading, `G := i·L(e₁)`. We prove **`G = (−1)^N`** (`G_fock`),
  so the `e`-complex structure *is* fermion-number parity.

Results:

1. **Colour-blind data reaches only leptons** (`colourBlind_lands_in_singlets`). Every
   `su(3)`-equivariant linear map from colour-blind data lands in `span(ν, e⁺)`. Quark
   levels 1 and 2 are never reached.
2. **Chirality: (b)** (`forced_chirality_embedding`). If the map also intertwines `J` with
   `G`, then `J=+1 ↦ K·ν` and `J=−1 ↦ K·e⁺`. This is unique up to a scalar on each line.
   The opposite root `−i` negates `G` (`G_neg_root`) and swaps the two lines.
3. **The tower cannot break the `i ↔ −i` symmetry** (`no_sqrt_neg_one_of_ordered`). The
   tower's chirality selector is an ordering of the base field. A field with `i² = −1` has
   no ordering. Tower data is defined over the ordered (real) subfield, so the Galois swap
   `i ↦ −i` fixes all of it, while `G` changes sign. No Galois-equivariant rule can pair
   `P₊` with a sign of `G`. Picking one is a choice of the root `i`. Furey makes the same
   choice when she calls `S_u` rather than `S_d` "particles".
4. **Flavour: obstruction** (`flavour_obstruction`). Furey's `S_u ↔ S_d` exchange maps the
   `G = +1` vacuum to the `G = −1` vacuum (`G_vacD`). So no `G`-commuting operator realises
   it. The tower flavour flip commutes with `J`. Under the forced `J ↦ G` the two
   involutions have opposite parity. Inside one ideal, `u` and `d̄` sit on levels 2 and 1.
   Those levels are inequivalent triplets (`3` vs `3̄`), so no `su(3)`-equivariant linear
   map exchanges them either.

## 4. The exact extra choices for a positive result

1. **A colour index on the tower quark state.** This is a linear identification of a
   tower colour triplet with level 1 (or 2) of `S_u`, intertwining the tower `gl₃` with
   `su3 e₁`. It is the stream-6c bridge (#7866). Without it every equivariant map lands in
   the lepton singlets.
2. **The root `i`**, equivalently which of `S_u`, `S_d` is "particle", or which of levels
   1 and 2 is `3`. No tower structure fixes it (result 3).
3. **For flavour, a `G`-odd identification.** Matching the tower flavour flip to
   `S_u ↔ S_d` requires dropping `J ↦ G`. That means a chirality identification other than
   the forced one. Stream 11's `T_j = τ_j·P_left` (ℂ⊗ℍ) is where chirality enters in
   Furey's own programme, not ℂ⊗𝕆.

## 5. Scope

Model mathematics throughout. Nothing here is compared to measurement. `ν`, `d̄`, `u`, `e⁺`
are Furey's names for the eight Fock vectors, used as labels. The negative results are
scope (b). Each cites its invariant: `su(3)`-invariants (result 1), the parity `G` (result
4), and the absence of an ordering on a field containing `√−1` (result 3). They exclude
*forced* maps. They do not exclude a map built with the choices in §4.
