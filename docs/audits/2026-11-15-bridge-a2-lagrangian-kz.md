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

## Follow-up: the three inputs (2026-11-15, later the same day)

Lean: `folio/quantum-observable-universe/lean/QOU/Mass/LagrangianKZInputs.lean`
(sorry-free; axioms only `propext`, `Classical.choice`, `Quot.sound`).

| input | status after this follow-up |
|---|---|
| 3. permutation symmetry | **derived** from P1 (Lean) |
| 1. Reeb invariance `L_ξ∇ = 0` | **reduced to a gauge choice**; one analytic gap left (log poles) |
| 2. regular residues at triple collisions | **derived in rank one** (written); matrix case `n ≥ 4` **still open** |

### Input 3 is the descent to unordered configurations

P1 already makes the `n`-body sector a local system on `Conf_n / S_n`. Pulled back to `Conf_n`
with factor `k` at point `z_k`, its descent datum is `ω(σ·z)(σ·u) = P_σ ω(z)(u) P_σ⁻¹`, where
`P_σ` permutes tensor factors. In Lean:

* `residue_covariant`: that equivariance forces `M_{σa,σb} = P_σ M_{ab} P_σ⁻¹` for every pair.
* `residue_uniform`: if one pair residue is `α + β P_{(i₀j₀)}` (what `schurWeyl_two` gives for
  one pair), every pair residue is `α + β P_{(ij)}`, with the same `α, β`.
* `arnoldForm_eq_abelian_add_kz`: the form is `α·(abelian) + KZ(ℏ = β, Ω_{ij} = P_{(ij)})`.

The only convention is the labelling "factor `k` at point `z_k`". So input 3 is not a new physical
assumption. Note that `Ω_{ij}` comes out as the transposition `P_{(ij)}` itself. On the fundamental
of `𝔤𝔩_N` that is the split Casimir, which is the expected KZ datum.

### Input 1 is a choice of gauge

`Conf_n ≅ ℂ × ℂ^× × M_{0,n+1}` by `z ↦ (z_0, z_1 − z_0, affineNormalize z)`. In Lean,
`affineNormalize` is invariant under all dilations and translations, and a function is invariant
under both iff it factors through it (`affineInvariant_iff`).

* The `ℂ` factor is contractible. The loop in the `ℂ^×` factor is the Euler loop, i.e. the full
  twist `Δ²`, which is central in `B_n`.
* So a local system `L` on `Conf_n` is a local system `L_M` on `M_{0,n+1}`, plus the automorphism
  `ρ(Δ²)`, which commutes with the monodromy of `L_M`.
* Take a connection `ω_M` for `L_M` (Riemann–Hilbert on `M_{0,n+1}`, the isolated Part IV). Let `B`
  be a logarithm of `ρ(Δ²)` chosen in the algebra it generates, transported to a `∇_M`-parallel
  section of `End(L_M)`. Since `ρ(Δ²)` commutes with the monodromy, that section is single-valued.
* Then `ω = ω_M + B · d log(z_1 − z_0)` is flat. The curvature reduces to `(∇_M B) ∧ d log t = 0`.
  It has the monodromy of `L`, and it is invariant under dilations and translations.

So `L_ξ∇ = 0` holds after a gauge transformation. Since the identification with KZ is only
claimed up to gauge, it is not a new axiom.

**The gap that remains.** P2 also needs Saito's condition (a), log poles along every diagonal.
`B` is a parallel section of a regular-singular connection, so it has moderate growth, but its pole
order along the boundary of `M_{0,n+1}` is not controlled here. If `B` has a pole, the invariant
representative leaves the log class.

### Input 2: rank one is derived; the matrix case is open

**Rank one (scalar coefficients).** Suppose `ω` is a scalar 1-form that is closed, logarithmic
along the braid arrangement, and homogeneous of degree 0. Then `ω = Σ c_{ij} d log(z_i − z_j)`
with constant `c_{ij}`. In particular its residues are constant, so condition (c) holds.

Proof (written):
1. Brieskorn–Arnold: the classes of the `d log(z_i − z_j)` span `H¹` of the complement. So
   `ω − Σ c_{ij} d log(z_i − z_j) = dg` with `g` single-valued.
2. Log poles bound the growth of `g` to logarithmic, so `g` is rational.
3. A pole of order `k ≥ 1` in `g` gives `dg` a pole of order `k + 1 ≥ 2`, which is impossible for a
   log form. So `g` is a polynomial.
4. `dg` is homogeneous of degree 0 with `deg dz = 1`, so `g` is constant.

**Consequence for the matrix case.** Flatness gives `d tr ω = −tr(ω ∧ ω) = 0`. So the trace of
every residue is constant, and the same holds for any one-dimensional quotient. On each diagonal
the residue is also a flat section of `End` for the induced connection, so its eigenvalues are
constant.

**Open.** It is not settled whether a flat, degree-0, log matrix connection on `Conf_n` with
`n ≥ 4` can have a residue that is non-constant along its diagonal. That would mean a rational
residue that is conjugate to a constant but not equal to one. The room for this exists:
- For `n = 4`, after quotienting by translations, the braid arrangement is free with exponents
  `1, 2, 3`.
- So its degree-0 log 1-forms form a space of dimension `1 + 3 + 6 = 10`, against the 6 forms
  `d log(z_i − z_j)`.
- In rank one, closedness removes the extra 4 dimensions. In the matrix case, flatness has not been
  shown to remove them.

### What is left

1. The log-pole order of the parallel twist logarithm `B` along the boundary of `M_{0,n+1}`
   (for input 1).
2. Regular residues at triple collisions for matrix connections, `n ≥ 4` (input 2).

Input 3 is closed.

## Second follow-up: triple collisions come from the monoidal structure (2026-11-15)

The owner pointed out that triple collisions are part of the monoidal structure. They are, and
that changes the status of input 2 (and probably of the gap left on input 1).

**The categorical side.** A braided monoidal category is an algebra over the little-disks
operad. When a cluster `S` of strands collides, the fibre near that collision is `⊗_{p∈S} V_p`
treated as one object, tensored with the rest. How a pair sits inside a larger cluster is
governed by the associator. The spaces of that operad are the Fulton–MacPherson compactifications,
and the compatible algebraic model is the De Concini–Procesi wonderful model `\overline{Conf}_n`,
where every collision stratum is blown up and the boundary is a normal-crossing divisor. The local
system the braiding defines extends across this model. That part is topology.

**Lean (`cluster_residue`, sorry-free).** For an Arnold-class form, let the cluster `S` collide as
`z_p = c + ε w_p`. Then `ε · ω` along the collision direction is `½ Σ_{p≠q∈S} M_{pq}` plus a term
regular at `ε = 0`. So:
- the exceptional divisor of the collision carries the residue `Σ_{p<q∈S} M_{pq}`;
- the pairs leaving the cluster contribute nothing singular.

With `M_{pq} = Ω_{pq}`, this is the Casimir of the cluster as one object minus the Casimirs of its
factors. The monoidal structure can be read off at the collision.

**Input 2, re-derived.**
1. On the wonderful model the boundary has normal crossings. Deligne's canonical extension gives a
   connection with log poles there whose residues are holomorphic along each boundary component.
2. The diagonal `z_i = z_j` meets the triple-collision locus `z_k = z_i` in a divisor of the
   diagonal, so blowing up does not change the diagonal there. Holomorphic residue on the
   diagonal is therefore exactly condition (c).
3. The local monodromy around the cluster divisor is the full twist of the cluster. The braided
   (ribbon) structure fixes it, so the categorical data determines the residues' exponentials.

So input 2 is not new physics. It is the monoidal structure plus the Riemann–Hilbert input
already isolated in Part IV, applied on the wonderful model rather than on `Conf_n`. The
rank-one restriction of the first follow-up is no longer needed.

**Input 1, probably closed the same way.** Including the point at infinity (the `ℂ^×`
compactification of the Euler direction) in the wonderful model, the Deligne extension also has
log poles along the divisor at infinity. That is the log-pole control on the twist logarithm `B`
that the first follow-up lacked. This is stated, not checked in detail.

**What is still assumed, explicitly.**
1. Riemann–Hilbert in Deligne's form on the (`ℂ^×`-equivariant) wonderful model. This is the same
   isolated analytic input, on a different compactification.
2. That the resulting algebraic vector bundle on `Conf_n` is trivial, so that the extension is
   `V^{⊗n}` with a single global connection form. Line bundles on `Conf_n` are trivial, since it is
   a hyperplane-arrangement complement with trivial Picard group. Triviality in higher rank is
   not checked here.
