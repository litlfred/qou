# Design — `HeckeH4Wedderburn` (full rank-4 Wedderburn isomorphism)

A2-s3 prep (bean `qou-308a`).  Target, at Wenzl-generic `q` over `[Field K]`:

```
wedderburn₄ :
  H4A K (q - q⁻¹) ≃ₐ[K] K × K × Matrix (Fin 2) (Fin 2) K
                        × Matrix (Fin 3) (Fin 3) K × Matrix (Fin 3) (Fin 3) K
```

mirroring the merged rank-3 pattern
`QOU/Machinery/HeckeH3Wedderburn.lean` (`wedderburnHom` → `wedderburnInvV` →
entry lemmas → left/right inverse via `linear_combination` cofactors →
`AlgEquiv.ofBijective`).

Genericity hypotheses (read off `det A = -(q²+1)²⁴ (q⁴+1)¹⁰ (q²-q+1)³ (q²+q+1)³ / q⁵⁰`):

```
hq : q ≠ 0        h2 : q ^ 2 + 1 ≠ 0
h3 : q ^ 4 + q ^ 2 + 1 ≠ 0        h4 : q ^ 4 + 1 ≠ 0
```

Over `ℝ` all four denominators are positive for `q ≠ 0`, so only `hq`
survives — same "unconditional real block" remark as rank 3.  If the sympy
run reports fallback atoms `x3a`/`x3b` (see `cofactors.json →
conventions.fallback_atoms_needed`), the file additionally derives
`h3a : q^2+q+1 ≠ 0` and `h3b : q^2-q+1 ≠ 0` from `h3` via
`q^4+q^2+1 = (q^2+q+1)*(q^2-q+1)` (one-line `fun h => h3 (by rw ...; ring)`
helpers).  **Result of the run: no fallback atoms were needed — every
denominator pairs `(q²+q+1)(q²−q+1)` into `(q⁴+q²+1)` powers**, so the
hypothesis set is exactly the four above (plus root facts `root_q`,
`root_negInv` re-stated from the H3 file).

## 0. Structural findings vs the H3 template (read before coding)

1. **Two different H₄ NF bases live in `QOU.Machinery.H4` — do not mix.**
   `MarkovTraceH4.lean` (`mulσ0/1/2`, ASCII) uses a *different* 24-word
   order than `HeckeH4StabilizationRung.lean` (`mulσ₀/₁/₂`, subscripts).
   The Wedderburn data (`computations/h4_wedderburn/…data.json`, matrix
   `A`/`A⁻¹`) is pinned to the **StabilizationRung subscript basis** (H₃
   Lean basis as prefix, then (length, canonical word) order).  Everything
   below builds on the subscript tables.  A permutation bridge to the
   `MarkovTraceH4` basis is an optional follow-up, not needed here.

2. **There is no H₄ algebra instance yet.**  Rank 3 had
   `HeckeH3AlgebraLaws` (brute-force `mulNF_assoc` by
   `fin_cases i <;> simp <;> ring` at 6 dims) + `HeckeH3AlgebraInstance`
   (`H3A` wrapper, `Ring`/`Algebra` instances).  At 24 dims the same brute
   force is **heartbeat-infeasible** (the depth-6 `whnf` wall documented in
   `MarkovTraceH4.lean`).  §2 below gives the structured (basis-sparse)
   associativity route; this is the main *new* work item that has no H3
   counterpart and should be its own PR-sized chunk.

3. **`sorry` status caution**: `MarkovTraceH4.trM_cyclic` currently rests on
   a cited `sorry` (`gram_symm`).  Nothing in the Wedderburn chain consumes
   it; do not import `MarkovTraceH4` into the Wedderburn files (import
   `HeckeH4StabilizationRung` + `HeckeH4BlockRep` only) so the new files
   stay sorry-free by construction.

4. **H3 bijectivity route confirmed**: `wedderburn₃` proves injectivity from
   the coordinate **left inverse** and surjectivity from the explicit
   **right inverse** (no dimension count).  Mirror that; both cofactor sets
   are in `cofactors.json` (SET A + SET B).

## 1. Definition-style decision: explicit-entry `blockOf`, not word products

H3 defined `blockOf` as `Σ v_j • (word product of S matrices)` and then
proved 4 `blockOf_apply` entry lemmas.  At rank 4 the longest word is
`σ₀σ₁σ₂σ₀σ₁σ₀` — a 6-fold product of 3×3 matrices; unfolding it inside
every lemma invites heartbeat blowups (3⁵ = 243 path terms per entry before
simplification).

**Recommendation: define the three block maps directly by their explicit
entries** (the rows of the verified 24×24 coordinate matrix `A`; Lean
syntax generated in `cofactors.json → lean_formulas.blockOf22/31/211`):

```lean
noncomputable def blockOf31 (q : K) (v : Fin 24 → K) :
    Matrix (Fin 3) (Fin 3) K :=
  Matrix.of ![![<row rho31_00 · v>, <rho31_01 · v>, <rho31_02 · v>], …]
```

With this choice:

* the H3-style `blockOf_apply` entry lemmas become **definitional**
  (a `show` + `simp only [blockOf31, Matrix.cons_val', Matrix.cons_val_zero,
  Matrix.cons_val_one, …]` unfold — no algebra);
* the mathematical content moves entirely into the **per-generator
  intertwiners** (§3, SET E cofactors), which never touch a word longer
  than 1;
* the link to the seminormal word products is recovered *as a theorem*
  (optional): `blockOf31 q (e j) = ρ₃₁(b_j)` follows by induction from the
  intertwiners + `blockOf31_unit`, or can be proved directly per word if
  wanted for the paper narrative.  If the implementer insists on the
  H3-mirror product definition instead, SET C in `cofactors.json`
  (`entry_blockOf*`) shows all 22 entry lemmas are **ring-trivial at the
  atom level** (the word-product path sums equal the explicit A-row
  formulas identically, no `mul_inv_cancel₀` facts needed) — so after the
  inverse-normalization simp pass each closes by plain `ring`.  The
  remaining risk is purely elaboration cost of expanding the length-≤6
  3×3 products (use `set_option maxHeartbeats 1600000` and expect slow
  elaboration).

`chiNF₄` is defined exactly like H3's `chiNF` (word-length powers, generic
`[CommRing R]`):

```lean
def chiNF₄ (l : R) (v : Fin 24 → R) : R :=
  v 0 + l * (v 1 + v 2 + v 6) + l ^ 2 * (v 3 + v 4 + v 7 + v 8 + v 9)
    + l ^ 3 * (v 5 + v 10 + v 11 + v 12 + v 13 + v 14)
    + l ^ 4 * (v 15 + v 16 + v 17 + v 18 + v 19)
    + l ^ 5 * (v 20 + v 21 + v 22) + l ^ 6 * v 23
```

(lengths per basis word: `[0,1,1,2,2,3,1,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,6]`).

## 2. The domain algebra: `mulNF₄` + `H4A` (prerequisite file)

New file `HeckeH4AlgebraLaws.lean` (imports `HeckeH4StabilizationRung`),
generic `[CommRing R]`:

* `mulNF₄ (h : R) (u v : Fin 24 → R) : Fin 24 → R` — right-linear
  expansion `Σ_j v_j • (u · b_j)`, where `u · b_j` composes the subscript
  `mulσ₀/₁/₂` along the word **first letter innermost** (the pinned
  convention: word `(i₀,i₁,…)` ⇒ `mulσ_{i_last} (… (mulσ_{i₀} u))`).
  Shape mirrors `MarkovTraceH4.mulNF` but over the subscript basis/words.
* Bilinearity: `mulNF₄_add_left/right`, `mulNF₄_smul_left/right`,
  `mulNF₄_zero_left/right` — Fin-24-free with the `mulσₖ_add/smul/zero`
  helper lemmas (copy the `MarkovTraceH4` pattern verbatim).
* `unitNF₄ : Fin 24 → R := Pi.single 0 1` (or `![1,0,…,0]`),
  `mulNF₄_one_left` (`= Σ v_j • (b_j) = v` — sparse), `mulNF₄_one_right`
  (`v 0`-term only — trivial).
* `e (i : Fin 24)` basis vectors + `basis_decomp` + `mulNF₄_sum_left/right`
  (copy `MarkovTraceH4`).
* `mulNF₄_e_right (u j) : mulNF₄ h u (e j) = wordAction j u` — 24 sparse
  goals.
* **Associativity — structured route (do NOT brute-force):**
  1. Per-generator/left-basis commutation, `3 × 24 = 72` **sparse** goals:
     `mulσₖ h (mulNF₄ h (e i) v) = mulNF₄ h (e i) (mulσₖ h v)`.
     On a basis left argument every word composite `wordAction j (e i)`
     is `e a` or `e a + h • e b` (sparse — this is exactly the trick that
     makes the Gram closure of `MarkovTraceH4` feasible, per its
     `gram_symm` docstring), so each goal is
     `funext m; fin_cases m <;> simp [...] <;> ring` over small sums.
  2. Lift to general left argument by bilinearity
     (`basis_decomp` + `mulNF₄_sum_left` + step 1):
     `mulσₖ_mulNF₄ : mulσₖ h (mulNF₄ h u v) = mulNF₄ h u (mulσₖ h v)`.
  3. Word induction (finite, 24 words):
     `wordAction j (mulNF₄ h u v) = mulNF₄ h u (wordAction j v)`.
  4. `mulNF₄_assoc` by right-linearity in `w`:
     expand `w = Σ w_j • e j`, use `mulNF₄_e_right` + step 3.
* `H4A R h` wrapper structure + `Ring`/`Algebra` instances — copy
  `HeckeH3AlgebraInstance.H3A` verbatim (only `Fin 6 → Fin 24`,
  `mulNF → mulNF₄`).

**Fallback** (if the 72 sparse goals misbehave): skip the unconditional
ring instance and derive `mulNF₄_assoc`/unit laws at generic `q` over a
field from **injectivity of the assembled coordinate map** (`W` linear +
multiplicative + left-invertible ⇒ `W (u·v·w)` associates in the target).
This costs hypothesis-carrying instances (`letI := h4Ring q hq h2 h3 h4`
plumbing in every downstream statement) — workable but uglier; prefer the
structured route.

## 3. The coordinate map and its lemmas

File `HeckeH4Characters.lean` (generic `[CommRing R]`):

* `chiNF₄` (above), `chiNF₄_unitNF` (`@[simp]`).
* `chiNF₄_mulσ₀ / _mulσ₁ / _mulσ₂ (h l : R) (hl : l * l = h * l + 1) (u)` :
  `chiNF₄ l (mulσₖ h u) = l * chiNF₄ l u` — closed by
  `simp [chiNF₄, mulσₖ]; linear_combination <cofactor> * hl` with the SET D
  cofactors (`chi_mulsigma0/1/2` in `cofactors.json`; each is a small
  polynomial in `l, h, u_j`, the direct generalization of H3's
  `(-(u 1) - l * u 3 - l ^ 2 * u 5) * hl`).
* `chiNF₄_mulNF₄` — Fin-free glue exactly as H3 `chiNF_mulNF`: expansion
  step (`simp only [chiNF₄, mulNF₄]; ring`), then rewrite the ≤6-deep word
  composites with the three intertwiners.
* `H4A.character` ring hom (copy H3).

File(s) `HeckeH4BlockMaps*.lean` (`[Field K]`, imports `HeckeH4BlockRep`):

* `blockOf22 / blockOf31 / blockOf211` explicit-entry defs (§1).
* `blockOfλ_unit : blockOfλ q unitNF₄ = 1` (verified: column 0 of `A` is
  `(1,1,I₂,I₃,I₃)`).
* Intertwiners (SET E, 9 matrix lemmas = 66 scalar goals):
  `blockOfλ_mulσₖ (hq h2 h3 h4) (u) :
     blockOfλ q (mulσₖ (q - q⁻¹) u) = blockOfλ q u * Sₖ_λ q`.
  Proof pattern per matrix entry:
  ```lean
  ext r c
  fin_cases r <;> fin_cases c
  all_goals simp only [blockOfλ, mulσₖ, Sₖ_λ, Matrix.mul_apply,
    Fin.sum_univ_two /-or _three-/, Matrix.cons_val', Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.head_cons, Matrix.of_apply,
    div_eq_mul_inv, one_div, mul_inv]
  all_goals linear_combination (norm := ring1) <SET-E cofactors>
  ```
  where the `linear_combination` payload is
  `c_hq * mul_inv_cancel₀ hq + c_h2 * mul_inv_cancel₀ h2 +
   c_h3 * mul_inv_cancel₀ h3 + c_h4 * mul_inv_cancel₀ h4`
  with the four cofactors from `cofactors.json → goals.block_*`.
* `blockOfλ_mulNF₄` — same Fin-free glue as H3 `blockOf_mulNF`
  (linearity expansion + intertwiners + `Matrix.mul_assoc` collection).
* `H4A.blockRepλ` AlgHom per block (copy H3 `blockRep`).

## 4. `wedderburnHom₄`, the inverse, and the equivalence

File `HeckeH4Wedderburn.lean` (`[Field K]`):

```lean
noncomputable def wedderburnHom (q : K) (hq …) :
    H4A K (q - q⁻¹) →ₐ[K] K × K × Matrix (Fin 2) (Fin 2) K
      × Matrix (Fin 3) (Fin 3) K × Matrix (Fin 3) (Fin 3) K where
  toFun x := (chiNF₄ q x.v, chiNF₄ (-q⁻¹) x.v,
              blockOf22 q x.v, blockOf31 q x.v, blockOf211 q x.v)
  …  -- five-fold Prod.ext, mirroring the H3 three-fold refine pattern:
     -- refine Prod.ext ?_ (Prod.ext ?_ (Prod.ext ?_ (Prod.ext ?_ ?_)))
```

* `wedderburnInvV (q s t : K) (M2 : Matrix (Fin 2) (Fin 2) K)
  (M31 M211 : Matrix (Fin 3) (Fin 3) K) : Fin 24 → K` — the 24 formulas
  from the verified `A⁻¹`, Lean syntax pre-generated in
  `cofactors.json → lean_formulas.wedderburnInvV4`.
  **Author them in atom-separated form** (only `q⁻¹`, `(q^2+1)⁻¹`,
  `(q^4+q^2+1)⁻¹`, `(q^4+1)⁻¹` powers — no `/`, no composite
  denominators), so the pre-derived cofactors apply verbatim without any
  `field_simp` round-trip.  To keep elaboration cheap, define the 24
  coordinates as 24 `private noncomputable def invC0 … invC23` scalars and
  assemble `wedderburnInvV … := ![invC0 …, …, invC23 …]`.
* **Payload-size finding (important).**  The direct H3-style per-coordinate
  `linear_combination` payloads for the left/right inverse (SET A/B in
  `cofactors.json → goals.left_inv_v*/right_inv_*`) are large: each
  24-coordinate goal mixes all 24 input coordinates, and even near-minimal
  cofactors sum to kilobytes per goal.  They are *provided and exactly
  verified* — usable as-is with per-coordinate private lemmas — but the
  **recommended architecture factors the inversion through explicit
  24×24 matrix literals**, because the coefficient of `v j` in left-inverse
  goal `i` is exactly the `(i,j)` entry of `A⁻¹·A − 1`:

  ```lean
  noncomputable def coordM (q : K) : Matrix (Fin 24) (Fin 24) K := …    -- A (atom form)
  noncomputable def coordMInv (q : K) : Matrix (Fin 24) (Fin 24) K := … -- A⁻¹ (atom form)

  theorem coordMInv_mul (hq h2 h3 h4) : coordMInv q * coordM q = 1      -- 576 tiny goals
  theorem coordM_mulInv (hq h2 h3 h4) : coordM q * coordMInv q = 1      -- 576 tiny goals

  theorem homVec_eq_mulVec (v) : homVec q v = (coordM q).mulVec v       -- definitional glue
  theorem wedderburnInvV_eq_mulVec (w) :
      wedderburnInvV q … = (coordMInv q).mulVec (wvec …)                -- definitional glue
  ```

  and then left/right inverse are three-line corollaries via
  `Matrix.mulVec_mulVec` + `Matrix.one_mulVec`.  The per-entry cofactors
  for BOTH matrix identities are pre-derived and exactly verified in
  `cofactors.json → matinv_left_entry_cofactors` (entries of `A⁻¹·A − 1`,
  keyed `"i_j"`) and `matinv_right_entry_cofactors` (`A·A⁻¹ − 1`, keyed
  `"r_m"`); each is a pure-`q` identity with small cofactors.  Prove each
  576-goal theorem as 24 `private` row lemmas
  (`rowLemma_i : ∀ j, (coordMInv q * coordM q) i j = (1 : Matrix _ _ K) i j`
  via `fin_cases j` + 24 `·  linear_combination <matinv cofactor i_j>`
  bullets — mechanical, generatable from the JSON).
* **Left inverse** (SET A, 24 goals; direct route if the matrix
  architecture is not adopted):
  ```lean
  theorem wedderburnInvV_left (hq h2 h3 h4) (v) :
      wedderburnInvV q (chiNF₄ q v) (chiNF₄ (-q⁻¹) v)
        (blockOf22 q v) (blockOf31 q v) (blockOf211 q v) = v
  ```
  Structure: 24 `private` per-coordinate lemmas (`show`-stated, one
  `simp only [invCi, chiNF₄, blockOf…-entry unfolds]` +
  `linear_combination <SET-A cofactors>` each), assembled by
  `funext i; fin_cases i <;> exact …`.  Splitting per coordinate keeps
  each elaboration small (the H3 file did all 6 in one `all_goals` block;
  at 24 coordinates with 24-term formulas a single block risks the
  heartbeat limit).
* **Right inverse** (SET B, 5 component lemmas = 24 scalar goals):
  `chiNF₄_wedderburnInvV_plus` (= `s`), `…_minus` (= `t`),
  `blockOf22_wedderburnInvV` (= `M2`, 4 entries),
  `blockOf31_wedderburnInvV` (= `M31`, 9), `blockOf211_wedderburnInvV`
  (= `M211`, 9) — `ext i j; fin_cases i <;> fin_cases j` + per-entry
  `show` + `linear_combination <SET-B cofactors>` (H3
  `blockOf_wedderburnInvV` pattern), or via `coordM_mulInv` in the matrix
  architecture.
* **`wedderburn₄`** — verbatim H3 `wedderburn₃` assembly:
  `AlgEquiv.ofBijective (wedderburnHom …)`; injectivity via
  `wedderburnInvV_left` + five `congrArg` projections
  (`Prod.fst`, `p.2.1`, `p.2.2.1`, `p.2.2.2.1`, `p.2.2.2.2`);
  surjectivity via the explicit inverse + the 5 right-inverse lemmas.
* Semisimplicity honesty note: keep the H3 module-docstring caveat
  (Mathlib `IsSemisimpleRing (Matrix ι ι R)` still `proof_wanted`); the
  explicit iso is the stronger statement.

## 5. Tactic/robustness notes (the H3 tricks, upgraded)

1. **No `field_simp` anywhere in the inverse lemmas.**  The H3 file's
   `field_simp [hq, h2', h3']` + hand-tuned `linear_combination` is
   replaced by the deterministic atom-level route: author formulas with
   separated inverse atoms and close each goal with `linear_combination`
   against `mul_inv_cancel₀` facts using the pre-derived cofactors.  This
   removes the two H3 pain points: (i) unpredictable `field_simp` normal
   forms (the `q^2*(q^2+1)+1 ≠ 0` regrouping hack in
   `HeckeH4BlockRep.S2_31_hecke`), and (ii) re-deriving cofactors
   interactively.  Where committed defs (`S2_31` etc.) contain composite
   denominators, normalize first with
   `simp only [div_eq_mul_inv, one_div, mul_inv]`; Mathlib's `ring1`
   (inside `linear_combination`) also distributes `⁻¹` over products and
   powers in a `Field`, so most goals close even without the explicit
   normalization pass — keep it for determinism.
2. **`show`-normalize indices** before each per-entry proof (H3
   `blockOf_wedderburnInvV` pattern): after `fin_cases`, state
   `show blockOf31 q (wedderburnInvV …) 1 2 = M31 1 2` so the `Fin`
   literals are canonical and `Matrix.cons_val*` simp lemmas fire.
3. **Heartbeats**: the per-coordinate/private-lemma split should keep every
   declaration under the default budget; if a straggler appears
   (`left_inv_v23` has the densest row), a local
   `set_option maxHeartbeats 800000 in` is acceptable — flag it in the PR.
4. **`Prod.ext` at 5 components**: the target is nested
   `K × (K × (M₂ × (M₃ × M₃)))`; write a small
   `refine Prod.ext ?_ (Prod.ext ?_ (Prod.ext ?_ (Prod.ext ?_ ?_)))`
   helper pattern once per structure field (map_one/map_mul/map_zero/
   map_add/commutes), exactly like the H3 three-fold version.
5. Base ring §7c: `chiNF₄`/`mulNF₄`/algebra laws stay `[CommRing R]`;
   block maps and everything touching `q⁻¹` go `[Field K]`.  No `ℝ`.

## 6. Recommended chunking (PR-sized, in dependency order)

| # | File | Content | Size/risk |
|---|------|---------|-----------|
| W0 | `HeckeH4AlgebraLaws.lean` | `mulNF₄`, bilinearity, unit, 72 sparse commutation goals, `mulNF₄_assoc`, `H4A` wrapper + instances | **the long pole**; no cofactors needed (CommRing, `ring` closes sparse goals) |
| W1 | `HeckeH4Characters.lean` | `chiNF₄`, 3 intertwiners (SET D), `chiNF₄_mulNF₄`, `character` | small |
| W2a | `HeckeH4BlockMap22.lean` | `blockOf22` + unit + 3 intertwiners (12 SET-E goals) + `blockOf22_mulNF₄` + AlgHom | medium |
| W2b | `HeckeH4BlockMap31.lean` | same for `(3,1)` (27 SET-E goals) | medium |
| W2c | `HeckeH4BlockMap211.lean` | same for `(2,1,1)` (27 SET-E goals) | medium |
| W3 | `HeckeH4WedderburnInv.lean` | `coordM`/`coordMInv` matrix literals, `coordMInv_mul` + `coordM_mulInv` (2×576 tiny per-entry goals, `matinv_*` cofactors), `wedderburnInvV` + mulVec glue, left/right-inverse corollaries | large but mechanical — every `linear_combination` payload is pre-derived; consider splitting the two 576-goal theorems into W3a/W3b |
| W4 | `HeckeH4Wedderburn.lean` | `wedderburnHom`, `wedderburn₄` | small, pure assembly |

W1 and W2a–c are independent of each other (parallelizable) once W0 lands;
W3 needs W1+W2*, W4 needs W3.  If a single-file H3-style layout is
preferred, merge W3+W4 — but keep W0 separate (different base-ring
typeclass and different review surface).

## 7. Conventions pinned (do not re-derive)

* Quadratic `x² = h·x + 1`, `h = q − q⁻¹`, eigenvalues `q`, `−q⁻¹`.
* Basis: 24 canonical S₄ words, H₃ Lean basis
  `[γ, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]` as prefix (indices 0–5), then the
  remaining 18 by (length, canonical word) — the `HeckeH4StabilizationRung`
  subscript order, NOT plain length-lex, NOT the `MarkovTraceH4` order.
* `ρ(word) = S_{i₀}·S_{i₁}·…` in word order; right action `u·b_j` applies
  `mulσ` of the word's **first letter first** (innermost).
* Tableaux orders `(2,2)`: `[12|34],[13|24]`; `(3,1)`: `[123|4],[124|3],
  [134|2]`; `(2,1,1)`: `[12|3|4],[13|2|4],[14|2|3]`; every 2×2 mixing
  block b-normalized `[[a,1],[a(h−a)+1,h−a]]`.
* `A` row order: `chi_plus, chi_minus, rho22_{00,01,10,11},
  rho31_{00..22}, rho211_{00..22}` (row-major within blocks); columns =
  basis words.  Verified in-script: rows 0–1 are the characters, rows 2–23
  are exactly the word-product entries, column 0 is `(1,1,I₂,I₃,I₃)`.
