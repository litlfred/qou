# Drinfeld–Kohno for 𝔰𝔩₂ at any ℏ ∉ ℚ, by the method of Etingof–Motorin–Varchenko–Zhu

Date: 2026-10-11. Goal milestone `qou-ywyq`; bean `qou-d0qq`. Requested by the owner:
"Use Etingof–Motorin–Varchenko–Zhu to get to sl_2".

**Status: an argument assembled here, not a published theorem and not refereed.**
Etingof–Motorin–Varchenko–Zhu prove the Deligne-category case only. The adaptation
below is ours, and every step that is not ours is cited. Nothing here is in Lean.

## 1. What Etingof–Motorin–Varchenko–Zhu prove, and why it does not cover 𝔰𝔩₂ directly

Source: arXiv 2504.02266v3 (library `arxiv-2504.02266v3`, §6, Theorem 6.1).

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
  with `f^λ` for `λ = (n−k, k)` (hook formula) is standard and not formalised.
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
* **Lean.** The counting core of Step 4 is formalised (`QOU/Mass/TwoRowCatalan.lean`). Steps 1, 3, 5 and the block theory of Step 4 are not. Formalising them would need Drinfeld's
  associator, the skein category's universal property and Hecke-algebra block theory. That is
  far more than the two-strand file (`QOU/Mass/KohnoTwoPoint.lean`) and the flatness file
  (`mass-endomorphism/kz-connection-sl2.lean`).

## 4. Checks still owed

1. `dim_q V = [2]_q` under the EMVZ balancing (Step 2).
2. That the universal property in EMVZ §6 is stated for arbitrary `t`, including integers, and
   not only `t ∉ ℤ`. EMVZ state it without the integrality hypothesis. It is the standard
   universal property of the oriented skein category. Confirm against Brundan's
   *Representations of the oriented skein category* before relying on it.
3. Step 1 at complex `ℏ`. EMVZ use it for `GL_t`; for `𝔤𝔩₂` cite
   Etingof–Frenkel–Kirillov, *Lectures on representation theory and KZ equations*.
