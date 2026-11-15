# Bridge A, step A2: the Lagrangian's connection and the KZ connection

Date: 2026-11-15. Bean `qou-d0qq`. Audit: `derivation-chain-audit-2026-11-15.md` §2.5 (G2.1), §8 step 8.
Lean: `folio/quantum-observable-universe/lean/QOU/Mass/LagrangianKZIdentification.lean` (sorry-free;
`#print axioms` shows only `propext`, `Classical.choice`, `Quot.sound`).

## Result in one paragraph

The corpus's connection `∇` cannot be identified with KZ *as the corpus stands*, because it lives on
the algebra `A` of one universe and has no `n`-body base. With three explicit postulates (P1–P3
below) the identification is exact, not just up to gauge, and it is proved algebraically. The Dirac
operator `𝒟 = q⁻¹∇ + ℏ_q ι_ξ∇` is an invertible reweighting of `∇`, so it has the same flat
sections and the same monodromy. The only analytic input, Riemann–Hilbert, is needed only to leave
the Arnold class, and it is carried as one hypothesis structure.

## What is proved (Lean, any field unless noted)

1. **`𝒟` is `∇` reweighted.** Pointwise `𝒟 = P ∘ ∇` with `P φ = q⁻¹ φ + ℏ_q · η ⊗ φ(ξ)`, `η(ξ) = 1`.
   * `dirac_reeb`: the Reeb component is unchanged, `(𝒟s)(ξ) = (∇s)(ξ)`.
   * `dirac_transverse`: transverse components are scaled by `q⁻¹`.
   * `dirac_left_inverse`: `P` is inverted by the weights `(q, 1 − q)`.
   * `dirac_eq_zero_iff`: `𝒟s = 0 ⇔ ∇s = 0`. Flat sections, hence monodromy, agree.
   * `reweight_sum_eq_one_of_reeb`: `q⁻¹ + ℏ_q = 1` is *exactly* the condition that the Reeb
     component is preserved. This is the algebraic content of the corpus's "convex pair".
   * `reweight_comp_fibre`: `P` commutes with every fibre map, so `𝒟` is as isospin-blind as `∇`.
2. **Residues determine an Arnold-class form** (`arnoldCoeff_injective`, any infinite field). For
   `ω_M = Σ_{i<j} M_ij d log(z_i − z_j)` the functions on `Conf_n` determine every `M_ij`.
   The proof is partial-fraction uniqueness (`partialFraction_unique`) plus separation by
   functionals. `arnoldForm_eq_half_dlog` matches the sibling file's form exactly.
3. **Identification** `eq_kz_iff`: an Arnold-class form equals `ω_KZ = ℏ Σ Ω_ij d log(z_i − z_j)`
   on all of `Conf_n` iff its residues are `ℏ Ω_ij`.
4. **Constant gauge** `const_gauge_iff`: `g ω_M g⁻¹ = ω_N` iff `N_ij = g M_ij g⁻¹` for all `i ≠ j`.
5. **Euler/Reeb part** `arnold_euler`: `ι_E ω_M = ½ Σ_{i≠j} M_ij`, a constant. With item 1,
   `(𝒟s)(E) = E·s − ½ Σ_{i≠j} M_ij s`. The Reeb part of `𝒟` on the KZ sector is the total pair
   Casimir with no `q` weight; only the transverse part carries `q⁻¹`.
6. **Riemann–Hilbert, isolated** (`RiemannHilbertInput`, `gauge_equiv_kz_iff_monodromy`): a
   regular-singular flat connection is KZ up to gauge iff its monodromy is conjugate to the KZ
   monodromy, which by Drinfeld–Kohno (sibling A4 thread) is the `R`-matrix representation.

## The three postulates the corpus does not yet derive

* **P1, `n`-body base.** The `n`-particle sector is the trivial bundle `V^{⊗n}` over `Conf_n(ℂ)`,
  and the corpus's Reeb field `ξ` is the Euler field (its rotation part is the Reeb field of the
  link sphere). Nothing in `def:categorical-lagrangian` mentions `Conf_n`.
* **P2, two-body locality.** The connection form is in the Arnold class: a sum of pair terms with
  constant residues. This is what turns "residues" into "the connection".
* **P3, the residue.** The pair residue is `ℏ Ω_ij` (for `𝔰𝔩₂` fundamentals, `ℏ(s_ij − ½)`,
  matching `KohnoTwoPoint`).

Given P1–P3: `∇ = ∇_KZ` on the nose (item 3), flat for every `n` (sibling
`InfinitesimalPureBraid.casimir_curvature_zero`), vacuum ⇔ flat (`YangMillsVacuumFlat`), and `𝒟`
has the same flat sections (item 1). The 2026-10-11 verdict "as the corpus stands, it is not" is
confirmed and sharpened: what is missing is exactly P1–P3, and nothing else.

## Deriving P1–P3 (added the same day, on the owner's question)

Status in one line. **P3** reduces to facts the corpus already has, plus permutation symmetry; the
key step is proved in Lean. **P2** reduces to two more primitive conditions, Reeb (dilation)
invariance and regular residues, with the key step in Lean and the rest written out. **P1** is
categorical: the braided structure *is* a local system on the configuration space, and the
Euler field is forced up to translation. Only the passage from a local system to a holomorphic
connection uses Riemann–Hilbert.

### P3: the pair residue is ℏΩ_ij

1. The corpus makes `∇` a morphism in `C` (`categorical-dirac-operator-exists-proof`). So its
   residues are endomorphisms in `C`, and the pair residue lies in `End_C(V ⊗ V)`.
2. If `V ⊗ V` splits into two simples, as the fundamental does (`Sym² ⊕ Λ²`), then
   `End_C(V ⊗ V)` is 2-dimensional. In the classical fibre functor, `schurWeyl_two` (Lean, char 0,
   `N ≥ 2`) proves that an `X` commuting with `E_ab ⊗ 1 + 1 ⊗ E_ab` for all `a, b` is
   `α·1 + β·P`. The argument is weight spaces plus four commutator entries; there is no basis
   choice beyond `K^N`.
3. Permutation symmetry: identical particles mean the residue of pair `(i,j)` is the
   `S_n`-conjugate of the pair `(1,2)` residue. So every residue is `α + β s_ij` with the same
   `α, β`. `arnoldForm_split` then gives `ω = α·(abelian form) + KZ(ℏ = β, Ω = s)`.
4. The two scalars are not free.
   * `β`: it is the KZ coupling, which the two-point Hecke quadratic ties to `q` (`KohnoTwoPoint`).
   * `α`: the half-monodromy eigenvalues are `e^{πi(α+β)}` on `Sym²` and `−e^{πi(α−β)}` on `Λ²`.
     Matching them to `q, −q⁻¹` forces `e^{2πiα} = 1`, so `α ∈ ℤ`. Then `∏(z_i − z_j)^α` is a
     single-valued gauge, and the abelian part is pure gauge.
   * This is written, not formalised.
5. Caveat: in the `q`-deformed fibre `End_C(V⊗V)` is spanned by `1, Ř`, not `1, P`. The residue
   lives on the classical side of Drinfeld–Kohno, so the classical statement is the right one;
   the categorical content is just "two simple summands ⇒ two scalars".

### P2: the pair residues are constant

Written proof. The Lean step is `eval_const_of_dilation_invariant`. Assume `ω = Σ f_m dz_m` is
rational and satisfies:

* (a) logarithmic poles along the diagonals only (Saito's condition: the polar part along
  `z_i = z_j` is in the `d(z_i − z_j)` direction);
* (b) **Reeb invariance**: `ω` is invariant under the Euler dilation, `f_m(λz) = λ⁻¹ f_m(z)`;
* (c) **regular residues**: the residue along each diagonal is a polynomial function on it. It
  does not blow up when a third point arrives.

Then `f_m = P_m / ∏_{j≠m}(z_m − z_j)` with `P_m` a polynomial, homogeneous of degree `n − 2` by (b).
As a function of `z_m`, the numerator degree `n − 2` is below the denominator degree `n − 1`, so
partial fractions give `f_m = Σ_j R_mj/(z_m − z_j)` with no polynomial part. `R_mj` is the
residue along `z_m = z_j`. It is a polynomial by (c) and dilation invariant by (b), so it is
constant (Lean). By (a), `R_mj = R_jm`. So `ω` is in the Arnold class. **Translation invariance
is not assumed; it follows.**

* For `n = 3`, (c) can be replaced by translation invariance. On a diagonal, a translation- and
  dilation-invariant function of the two remaining points is constant.
* For `n ≥ 4`, (c) is needed as stated. I have not checked whether flatness alone forces it.
* What the corpus does not yet say: that `∇` is invariant under the Reeb flow (`L_ξ ∇ = 0`). It
  defines `ξ` and `ι_ξ` as morphisms in `C`, but no block found here asserts the invariance.
  That is the one new axiom P2 needs (with (c) for `n ≥ 4`).

### P1: the n-body base, and ξ = Euler

* **The base comes from the braiding.** The braiding of `C` gives an action of the braid group
  `B_n` on `V^{⊗n}`. `B_n = π₁(Conf_n/S_n)`, so this action *is* a local system on the
  unordered configuration space. This is topology, not analysis. Turning the local system into a
  holomorphic connection with log poles is Deligne's Riemann–Hilbert (the isolated Part IV);
  P2 then picks the KZ representative in the gauge class.
* **ξ is forced up to translation.** A one-parameter symmetry of `Conf_n` that commutes with
  permutations and translations is `z ↦ e^{ta}z + b(t)`, so its generator is `a·E + b·T`. Since
  `ι_T ω = 0`, only the Euler part acts. The loop of the rotation is the full twist `Δ²`, which
  generates the center of `B_n`.
* **Consistency check.** The Euler-loop holonomy of KZ is `exp(2πi·ι_E ω)`. On the `λ`-isotypic
  part this is `exp(2πiβ·c(λ))`, where `c(λ)` is the content sum, because `Σ_{i<j} s_ij` is the
  Jucys–Murphy sum. That equals the ribbon value `q^{2c(λ)}` of `Δ²` at `q = e^{πiβ}`. So
  "Reeb loop = twist" is consistent with the corpus's ribbon structure. This is standard and not
  formalised here.

### What is left as genuine new input

1. Reeb invariance of `∇`, `L_ξ ∇ = 0` (for P2).
2. Regular residues at triple collisions, for `n ≥ 4` (for P2).
3. Permutation symmetry of the `n`-body sector (for P3). This is identical particles; the corpus
   uses symmetric tensor powers throughout but does not state it for `∇`.

Everything else is derived, either from `∇` being a morphism in `C` with the braiding of `C`, or
from Schur–Weyl and the Hecke normalisation.

## Caution on the coordinator's phrasing

"A flat connection with Casimir residues is KZ up to gauge" is **not** a theorem in general. Inside
the Arnold class it holds with equality (item 3). Outside it, local data (residues up to
conjugacy) do not in general fix the gauge class: non-rigid Fuchsian systems with the same local
monodromy classes need not be gauge equivalent (Katz). The correct general statement goes through
monodromy (item 6). Whether residues equal to `Ω_ij` in a fixed trivialisation on every diagonal
already force the gauge class is left open; it is not needed if P2 is adopted.

## For Bridge B

The reweighting gives the corpus's two weights a geometric meaning: `q⁻¹` on directions
transverse to the Euler field, `1` on the Euler (Reeb) direction. On `𝒟²`, transverse–transverse
terms carry `q⁻²`, Reeb–Reeb terms `1`, mixed terms `q⁻¹`. This is a candidate origin for the
dressing ratios in `h1_hierarchy_origin.md`; it is **not** checked here, and it is stated only as
a lead.
