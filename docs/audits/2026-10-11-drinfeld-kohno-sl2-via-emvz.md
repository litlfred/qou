# Drinfeld–Kohno for 𝔰𝔩₂ at any ℏ ∉ ℚ, by the method of Etingof–Motorin–Varchenko–Zhu

Date: 2026-10-11. Goal milestone `qou-ywyq`; bean `qou-d0qq`. Requested by the owner:
"Use Etingof–Motorin–Varchenko–Zhu to get to sl_2".

**Status: an argument assembled here, not a published theorem and not refereed.**
Etingof–Motorin–Varchenko–Zhu prove the Deligne-category case only. The adaptation
below is ours, and every step that is not ours is cited. The Hecke-algebra half of Step 4 is in
Lean (§5); the analytic and categorical steps are not.

## 1. What Etingof–Motorin–Varchenko–Zhu prove, and why it does not cover 𝔰𝔩₂ directly

Source: arXiv 2504.02266v3, §6, Theorem 6.1. Ingested as `library/arxiv-2504.02266v3` on branch
`claude/library-ingest-kz-batch-2026-10-11`, **not yet on `main`**.

* **Setting.** `t ∈ ℂ ∖ ℤ`; `Rep(GL_t)` is Deligne's interpolation category; `ℏ ∉ ℚ`;
  `q = e^{πiℏ}`; `a = q^t`; and `q, a` multiplicatively independent.
* **Theorem 6.1.** The monodromy of the KZ equation `∂F/∂z_i = ℏ Σ_{j≠i} Ω_{ij} F/(z_i − z_j)`
  on `Hom(Y, V^{⊗n})` is isomorphic to the braid action in the skein category
  `Rep_q(GL_t)` (the HOMFLYPT skein category with parameters `q, a`).
* **Method.**
  1. Drinfeld's construction makes `Rep(GL_t)` braided using KZ: associator = renormalised
     monodromy of the 3-point KZ equation from 0 to 1, braiding `e^{ℏΩ/2}`. Its braid action
     on `Hom(Y, V^{⊗n})` is the KZ monodromy.
  2. A ribbon structure is added (balancing `q^{−⟨λ+2ρ,λ⟩}`).
  3. **Universal property** of the skein category: braided tensor functors
     `Rep_q(GL_t) → 𝒞` into a ribbon category correspond to objects `X` of quantum dimension
     `[t]_q` whose self-braiding satisfies the Hecke relation `(β − q)(β + q^{-1}) = 0`.
  4. This gives a braided functor `F` sending the generator `X_q` to `V`. Both categories are
     semisimple with the same simples, so `F` is an equivalence.

**Why 𝔰𝔩₂ is excluded.** For `𝔤𝔩₂` the tautological object has `t = 2`, an integer, so
`a = q²` and the independence hypothesis fails. At integer `t` the skein category is **not
semisimple**: it has nonzero morphisms of trace zero (negligible morphisms), for example the
`q`-antisymmetriser on three strands. So step 4 fails as written.

## 2. The adaptation to 𝔤𝔩₂, hence 𝔰𝔩₂

Fix `ℏ ∈ ℂ ∖ ℚ` and `q = e^{πiℏ}`; then `q` is not a root of unity. Let `V = ℂ²`.

**Step 1 (Drinfeld category).** Let `D_ℏ` be `Rep(𝔤𝔩₂)` with Drinfeld's KZ associator and
braiding. For complex `ℏ` the renormalised monodromy defining the associator exists when no
two residue eigenvalues differ by a nonzero integer. All Casimir eigenvalue differences are
integers, so the condition is `ℏ·m ∉ ℤ ∖ {0}` for integers `m`, which `ℏ ∉ ℚ` guarantees.
The braid action of `B_n` on `V^{⊗n}` in `D_ℏ` is the KZ monodromy.
(Drinfeld 1991 `drinfeld1991`; EMVZ §6 proof, the same construction for `GL_t`.)

**Step 2 (Hecke relation and dimension).** For `𝔤𝔩₂`, the Casimir on `V ⊗ V` is the flip `P`
itself (the 𝔰𝔩₂ Casimir is `P − ½`; see `QOU.Mass.KohnoTwoPoint.casimir_eq_flip`). The
braiding `β = P · e^{πiℏ P}` acts by `q` on `Sym²V` and by `−q^{-1}` on `Λ²V`, so
`(β − q)(β + q^{-1}) = 0`. This two-strand computation is proved in Lean, sorry-free, for the
actual KZ transport (`QOU.Mass.KohnoTwoPoint.exchange_eq_classical`). With the balancing of
EMVZ, `dim_q V = [2]_q`. **This last equality is a check still to be written out**, not
re-derived here.

**Step 3 (the functor).** By the universal property (EMVZ, step 3 above, with `t = 2`) there is
a braided ribbon functor `F : Skein_{q, a=q²} → D_ℏ` with `F(X_q) = V`. Being ribbon, `F`
preserves quantum traces.

**Step 4 (replacing semisimplicity by a dimension count).** This is the step that is new
relative to EMVZ.

* `End(X_q^{⊗n})` in the skein category is the Hecke algebra `H_n(q)`. It is semisimple
  because `q` is not a root of unity, with one matrix block per partition `λ ⊢ n` of size `f^λ`
  (the number of standard tableaux).
* The image `F(H_n(q)) ⊆ End_{D_ℏ}(V^{⊗n})` is a quotient of a semisimple algebra, so it is
  the sum of the blocks that `F` does not kill.
* For a minimal idempotent `p_λ` of block `λ`, the quantum trace is the HOMFLYPT dimension at
  `a = q²`:

  $$
  \mathrm{tr}_q(p_\lambda) = \prod_{\square \in \lambda} \frac{[2 + c(\square)]_q}{[h(\square)]_q},
  $$

  with `c` the content and `h` the hook length. For `λ` with at most two rows every numerator
  is `[m]_q` with `m ≥ 1`, which is nonzero. So `tr(F(p_λ)) = tr(p_λ) ≠ 0`, `F(p_λ) ≠ 0`, and
  every two-row block survives.
* The two-row blocks alone have total dimension `Σ_{λ ≤ 2 rows} (f^λ)² = C_n`, the Catalan
  number. The target `End_{D_ℏ}(V^{⊗n})` has the same underlying vector space as
  `End_{𝔤𝔩₂}(V^{⊗n})`, which also has dimension `C_n`.
  **Lean (sorry-free):** the count `Σ_{k ≤ n/2} (C(n,k) − C(n,k−1))² = C_n` is
  `QOU.Mass.TwoRowCatalan.twoRow_sum_sq_eq_catalan`, and `[m]_q ≠ 0` for `m ≥ 1` with `q` not a
  root of unity is `QOU.Mass.TwoRowCatalan.qint_ne_zero`. The identification of `C(n,k) − C(n,k−1)`
  with `f^λ` for `λ = (n−k, k)` is `QOU.SchurWeyl.TwoRowSYTBallot.numSYT_twoRow_eq_ballot`, and
  the count itself was first proved as `QOU.Mathlib.ballot_sq_sum_catalan`; both sorry-free.
* So `F : H_n(q) → End_{D_ℏ}(V^{⊗n})` is surjective. Its kernel is exactly the blocks with
  three or more rows, and it induces an isomorphism from the Temperley–Lieb algebra `TL_n(q)`.
* Consequently, for each simple `Y = V_j` the KZ monodromy representation on `Hom(V_j, V^{⊗n})`
  is the irreducible `TL_n(q)`-module of the two-row partition with `λ₁ − λ₂ = 2j`. The block
  is identified by the quantum dimension `[2j + 1]_q` of its image.

**Step 5 (comparison with Jimbo).** By Jimbo's `q`-Schur–Weyl duality (`jimbo1986`), for `q`
not a root of unity the Jimbo `R`-matrix action of `B_n` on `Hom_{U_q}(V_j, V^{⊗n})` is the same
irreducible `TL_n(q)`-module. So the two `B_n`-representations are isomorphic for every `j`.

**Step 6 (back to 𝔰𝔩₂).** Passing from 𝔤𝔩₂ to 𝔰𝔩₂ changes the Casimir by `−½`, which
multiplies each crossing by the scalar `e^{−πiℏ/2} = q^{−1/2}`. This is exactly the
`e^{−c/2}` factor in `QOU.Mass.KohnoTwoPoint.trace_weight_exchange_pow`.

**Conclusion.** Kohno's theorem (`kohno1987`, Thm 1.2.8) holds for 𝔰𝔩₂ at every `ℏ ∉ ℚ`,
by an algebraic argument with no analytic continuation in `ℏ`. For the framework's coupling
`ℏ₀ = ln q₀/(iπ)`, which is purely imaginary and nonzero, this is a second, independent route
to what Kohno's Remark 1.3.14 already gives (PR #7673, probe
`computations/kz_real_q0_pure_braid_monodromy_probe.py`).

## 3. What this does and does not change

* **Gives.** An independent proof of the representation-level identification at the real pin.
  Its only analytic input is Drinfeld's category (Step 1); Kohno's own proof instead uses
  analytic continuation from small `|λ|`.
* **Does not give.**
  * The weighted-trace statement still needs the weight-preserving intertwiner (merged in
    #7632, scope point 3 of `categorical-mass-markov-proof`).
  * It says nothing about whether the framework's own substrate connection **is** this KZ
    connection. That is still open (bean `qou-d0qq`; verdict of 2026-10-11: as the corpus
    stands, it is not).
* **Lean.** The Hecke side of Step 4 is formalised (§5). Steps 1, 3, 5 and the KZ side of Step 4
  are not. Formalising Steps 1 and 3 would need Drinfeld's associator and the skein category's
  universal property; §5 proposes a route that avoids both. That is far more than the two-strand file (`QOU/Mass/KohnoTwoPoint.lean`) and the flatness file
  (`mass-endomorphism/kz-connection-sl2.lean`).

## 4. Checks still owed

1. `dim_q V = [2]_q` under the EMVZ balancing (Step 2).
2. That the universal property in EMVZ §6 is stated for arbitrary `t`, including integers, and
   not only `t ∉ ℤ`. EMVZ state it without the integrality hypothesis. It is the standard
   universal property of the oriented skein category. Confirm against Brundan's
   *Representations of the oriented skein category* before relying on it.
3. Step 1 at complex `ℏ`. EMVZ use it for `GL_t`; for `𝔤𝔩₂` cite
   Etingof–Frenkel–Kirillov, *Lectures on representation theory and KZ equations*.

## 5. Lean status of each step, and a route to a full Lean proof (2026-10-11)

Owner instruction: no citation-only steps; everything to be proved in Lean on Mathlib. Survey of
`folio/quantum-observable-universe/lean/QOU/` (source scan for `sorry` / `axiom`, not a build):

| ingredient | Lean | status |
|---|---|---|
| `H_n(q)`: quadratic, braid, far commutation | `SchurWeyl/HeckeAlgebra` | done |
| `dim H_n(q) = n!`; Wedderburn `H ≃ ∏_λ M_{f^λ}` for `q` not a root of unity | `finrank_hecke_eq_factorial`, `heckeWedderburn`, `isSemisimpleRing_hecke_generic` | done |
| two-row `f^λ = C(n,k) − C(n,k−1)`; `Σ (f^λ)² = C_n` | `numSYT_twoRow_eq_ballot`, `ballot_sq_sum_catalan` | done |
| Markov trace on blocks: zero on ≥ 3 rows, nonzero on two rows | `ocneanuWeight_eq_zero_of_three_rows`, `…_ne_zero_of_two_rows` | done (generic field) |
| `H/rad ≅ ∏_{two-row} M_{f^λ}`, dimension `C_n` | `SchurWeyl/TraceQuotGeneric`: `traceQuotEquiv`, `finrank_traceQuot_eq_catalan`, `…_complex` | done over any char-0 field, `q ≠ 0` not a root of unity (that hypothesis implies the old `hgen` and `q²+1 ≠ 0`) |
| `H_n → TL_n` onto; `dim TL_n` | `heckeToTL_surjective`, `heckeTLEquiv`; `MathlibExt/TemperleyLiebNormalIdxCatalan` (normal words ≃ Dyck words), `…NormalFormSpanning.finrank_le_catalan` | onto: done. `dim TL_n ≤ C_n`: done for all `n`, any commutative ring. Equality and the Jones normal-form basis: done over `ℝ` for real `q ≠ 0` not a root of unity (`TemperleyLiebDimCatalan.finrank_eq_catalan`, `normalBasis`), via a direct TL action on `V^{⊗n}` whose image contains the Jimbo image |
| Jimbo `Ř`: quadratic, Yang–Baxter, action on `V^{⊗n}` | `RMatrixSl2`, `heckeActionN`; `SchurWeyl/JimboActionKernel` | done. Kernel = trace radical and image dimension `C_n`: done over ordered fields (`ker_jimbo_eq_traceRadicalIdeal`, `finrank_range_jimbo_eq_catalan`); over `ℂ` open |
| `U_q(𝔰𝔩₂)`, `q`-Schur–Weyl | `Mass/QuantumSl2Fundamental`: representation data `E,F,K^±`, coproduct, `V^{⊗n}`; every adjacent `Ř` commutes with `Δ^{(n)}` | partial. The algebra as a quotient ring and the double commutant are missing; the rigidity route below does not need them |
| KZ on `n` points as a `B_n` representation | 2 strands (`KohnoTwoPoint.kzExchange_quad`); `Mass/KZHolonomy/`: flatness of the KZ form on `Conf_n(ℂ)` (`kzForm_isFlatOn`), endpoint-only transport on star-shaped sets (`flat_transport_eq`), `kzBraidRep : B_n →* Aˣ` with braid relations, equal to the permutation action at coupling 0 | done, merged to main (PR #7719, `e1f5d1b4e`), including continuity in the coupling (`continuous_kzBraidRep`) |
| Drinfeld associator; skein-category universal property | — | missing (very large each); Mathlib has neither |

**Proposed full-Lean route (judgement, not a finding): bypass Drinfeld and the skein category.**
Kohno's own proof is a rigidity argument, and in Lean it needs strictly less than Steps 1 and 3.

1. **KZ holonomy is a `B_n` representation** `θ_λ : B_n → GL(V^{⊗n})` for every complex `λ`,
   continuous in `λ`. Needs the KZ system on `Conf_n(ℂ)`, local existence and uniqueness
   (Mathlib `PicardLindelof`, `Gronwall`), homotopy invariance of transport for a flat connection
   (flatness is `kz_isFlat`), and the braid relations from loops in `Conf_n/S_n`. This is the large
   item (bean `qou-9634`).
2. **It factors through `H_n(q)`**, `q = e^{iπλ}` (in the Lean normalisation `q = e^{2πiκ}`, so `λ = 2κ`; see §5.2): each `θ_λ(σ_i)` is conjugate to the two-point
   exchange, so the Hecke quadratic follows from `KohnoTwoPoint.kzExchange_quad`.
3. **Rigidity.** For `q` off the roots of unity `H_n(q)` is semisimple (`heckeWedderburn`), so a
   module is determined by its character. Along a continuous family the character is continuous
   and the block multiplicities are integers, hence locally constant. At `λ = 0` the KZ monodromy
   is the permutation action; the Jimbo action `heckeActionN` is also a continuous family that is
   the permutation action at `q = 1`. So the two have equal multiplicities on the connected
   admissible set and are isomorphic there. That set contains the purely imaginary coupling of the
   real pin.
4. The weight-preserving intertwiner (#7632) transports the weighted trace.

This needs neither `U_q(𝔰𝔩₂)`, nor Drinfeld's associator, nor the skein category.

### 5.1 Assembly status (2026-10-11, PR #7673)

These are proved without sorry; their only axioms are `propext`, `Classical.choice` and `Quot.sound`.
- `BraidHeckeFactor`: if a braid representation `θ` has `θ(σ₀)` satisfying the Hecke quadratic, then every `θ(σ_j)` does, because all `σ_j` are conjugate. So `θ` factors through `H_m(q)` (`heckeOfBraidRepOfZero`).
- `KZTwoStrandHecke`: for two strands the KZ holonomy is `θ(σ₀) = e^{θ(1−c)} e₊ − e^{−θ(1+c)} e₋`. After rescaling it satisfies the Hecke quadratic with `q = e^{2πiκ}`, so it factors through `H_1(q)`.
- `KohnoComparison`: two representations of `∏ M_{d_i}` are conjugate exactly when the ranks of their matrix-unit idempotents agree. On a preconnected parameter set, continuous families that are conjugate at one point are conjugate everywhere.

- `KZHolonomy/LocalMonodromy` (2026-10-12): for every strand count `n ≥ 2`, every representation `ρ : S_n →* A` into a complete normed `ℂ`-algebra, every coupling `κ ∈ ℂ` and every `c ∈ ℂ`, the rescaled generator `β_j = e^{2πiκc} θ(σ_j)` satisfies `β_j² = (q − q⁻¹)β_j + 1` with `q = e^{2πiκ}` (`kzBraidRep_sigma_isHeckeQuad`), so `kzBraidRep` factors through `H_n(q)` (`heckeOfKZ`, `heckeOfKZ_σ`). Proof: near `z₀ = z₁` the KZ coefficient along the half-turn is `iπ M(u)`, `M(u) = 2κ(P − c) + O(u)` holomorphic on `|u| < 3`; for non-resonant `κ` (`κ ∉ ±ℕ/4`) the convergent Fuchsian solution `H(u)u^{M₀}` gives `θ(σ₀) H(1) = H(1) · P e^{iπ M₀}`, using the exchange symmetry `H(−u) = P H(u) P` (from uniqueness of the formal solution) and invertibility of `H(1)` (ODE along `[ε,1]`). The resonant set is countable and the Hecke defect is continuous in `κ`, so it vanishes for every `κ`.

Two gaps stand between these and the full theorem (gap 1 below is closed by `LocalMonodromy`).
1. ~~The Hecke quadratic for the KZ generator when `n ≥ 3`.~~ Closed 2026-10-12, see `LocalMonodromy` above. Normalisation: `q = e^{2πiκ}` for the KZ form `κ Σ_{a≠b} d log(z_a − z_b)(ρ(s_ab) − c)` summed over ordered pairs (residue `2κ(P − c)`).
2. ~~Continuity in `q` of the Wedderburn isomorphism.~~ Closed 2026-10-12 (PR #7738): `JMProjector.heckeWedderburn_symm_single` writes `W⁻¹(E^λ_TT)` as a Jucys–Murphy Lagrange polynomial in the `σ_i` whose denominators are nonzero at every positive real `q`, including `q = 1`; `JMProjectorContinuity.continuousOn_projFamily`.
3. ~~A base point.~~ Closed 2026-10-12 (PR #7738): idempotence at `q = 1` follows by density (`isIdempotentElem_projFamily`), so no separate Wedderburn decomposition of `ℂ[S_n]` is needed.

### 5.2 The comparison theorem (2026-10-12, PR #7744)

`QOU/Mass/KohnoAssembly.lean`, sorry-free, axioms `propext`, `Classical.choice`, `Quot.sound` only; compiled with `lean -DautoImplicit=false -s 65536` after rebuilding its whole 134-module import cone from source.

**Convention.** The Lean KZ form is `κ Σ_{a≠b} d log(z_a − z_b)(ρ(s_ab) − c)` over ordered pairs, and its Hecke parameter is `q = e^{2πiκ}`. Relative to the `q = e^{iπλ}` of §5 this is `λ = 2κ`. The coupling of a real pin `q₀ > 0` is therefore `κ₀ = ln q₀ / (2πi) = −i ln q₀ / (2π)`, purely imaginary.

**Normalisation of the two sides.** Both are algebra maps out of the same `H_{m+1}(q) = Hecke ℂ q q⁻¹ m`, with relation `β² = (q − q⁻¹)β + 1`:
- KZ: `σ_j ↦ e^{2πiκc} θ_κ(σ_j)` (`kzHeckeRep`), with `ρ = permRep` the permutation action of `S_{m+1}` on `V^{⊗(m+1)}`, `V = ℂ²`. The scalar `e^{2πiκc}` per crossing is the only normalisation difference; it absorbs any Casimir shift `c`, including the `𝔤𝔩₂`/`𝔰𝔩₂` shift.
- Jimbo: `σ_j ↦ Ř_{j,j+1}(q)` (`jimboRep`), eigenvalues `q` (symmetric) and `−q⁻¹` (antisymmetric). Its entries are Laurent polynomials in `q` (`strandBraid_eq_eval`).
- Base point: at `κ = 0`, `q = 1`, both send `σ_j` to the permutation matrix of `(j, j+1)` exactly (`permRep_adjSwap`, `kzBraidRep_zero_σ`), with no scalar.

**Proved.**
- `kz_conj_jimbo_real`: for every number of strands `m + 1`, every `c ∈ ℂ` and every real `t`, at the coupling `κ = t/(2πi)` (so `q = e^t`) there is an invertible matrix `U` with `U · kzHeckeRep(h) = jimboRep(h) · U` for every `h ∈ H_{m+1}(q)`.
- `kz_conj_jimbo_pos`: equivalently, for every real `q₀ > 0`, one invertible `U` conjugates every rescaled KZ generator `e^{2πiκ₀c} θ_{κ₀}(σ_j)` to Jimbo's `Ř_{j,j+1}(q₀)`.
- The route is §5 steps 1–3: continuity of both families in `t`, the base point at `t = 0`, and rigidity (`conj_of_isPreconnected_hecke`) on `[0, t]` or `[t, 0]`, where every `q ≠ 1` is generic.

**Not proved.**
- Complex `q` off the positive real axis (couplings `κ` that are not purely imaginary). The rigidity argument needs a connected path to `κ = 0` avoiding roots of unity except `q = 1`, and the separation hypothesis on the `q²`-integers; neither is established off the real ray.
- An explicit intertwiner. `U` is produced by comparing ranks of block idempotents; nothing identifies it (e.g. with the weight-preserving intertwiner of #7632).
- `V ≠ ℂ²`, i.e. other representations of `𝔤𝔩_N`/`𝔰𝔩_N`, and the Drinfeld–Kohno theorem in its general form (associator, quasi-Hopf twist).
- `jimboRep` versus `JimboActionKernel.jimbo`: they agree on generators by construction, hence are equal by `Hecke.hom_ext`, but this equation is not stated in Lean, because `JimboActionKernel` does not compile against the olean cache used here (its cached dependency `SeminormalRep` predates that module's change to a general field).
