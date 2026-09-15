# χ(A) = −6 as one component of a graded object: the four readings, what was assumed, and the resolution (2026-09-15)

**Owner ask, verbatim.** *"i also want to understand the euler characteristic = −6. it is derived from the axioms and is a scalar, but is probably just a single term of a larger algebraic object which may or may not vanish. i am not sure if we have implicitly (or explicitly) assumed. analyze and what are some of the options to resolve if we have done so. the only part of the −6 we need really is in knowing the genus of (so we can get to brings) and the dimension of things like the knot operator space."*

**Inputs.** Three read-only surveys of `main` at `0509e4010`, transcribed this session:
[χ / tr(id_A) / dim_q sites](2026-09-15-survey-chi-trace-dimq-sites.md),
[HH / HKR / ch / K₀ / FM / Orlov / S¹ / DG sites](2026-09-15-survey-hh-hkr-chern-k0-fm-orlov-s1-dg-sites.md),
[the axiom system and the running example](2026-09-15-survey-qou-axioms-braided-rigid-and-running-example.md);
the probe `computations/audits/dimq_regularisation_schemes_probe.py` (this PR) and the merged #7421 probe; and the owner's uploads of 2026-09-15 (BGHL 1409.1198, Trinh 2106.07444, Feng–Tsygan 1991, Hadfield–Krähmer math/0405249, Brown–Zhang math/0603732, Căldăraru–Willerton 0707.2052, Kontsevich q-alg/9709040, Nest–Tsygan 1995, Dolgushev–Rubtsov math/0408210), ingested into `library/` in this PR. Bean `qou-nnyn`, issue #7425.

## 0. Verdict

Yes. Under every one of the **four** readings the corpus gives the symbol `χ(A) = tr(id_A)`, the number −6 is a scalar extracted from a graded object, and the corpus never says which reading it means at a given site. Which components were assumed to vanish differs by reading:

- under the owner's ruling (reading 1, `tr(id_A) = dim_q(A)`) the "larger object" is the class `[A] ∈ K₀(𝐂)`; for `A = 𝒪_q(SU(2))` its quantum dimension diverges and the two standard regularisations give **0** and **−1/(q−q⁻¹)²**, never −6; the ζ-regularised value 0 is `χ_eu(SU(2)) = χ(S³)`, i.e. under the ruling the Euler characteristic of the substrate object *does* vanish, and −6 belongs to the base;
- under the chain's own computation (reading 2, Riemann–Roch for the rank-2 bundle) nothing was hidden: the other component `deg V = c₁(V)` is killed by `det V = 1`, and the genus enters through the Todd class of the **base**, not through `A`;
- under the topological reading (reading 3, `χ_eu(M₀) = 2 − 2g`) the larger object is the graded Hochschild homology of the base and −6 is its alternating sum, not a component;
- under the obstruction reading (reading 4, a class in `HH² ≅ k`) two things were assumed with no construction: that a "trace map" `H²(𝒮, ℬ) → R` exists, and that `HH² ≅ k` at all — the latter is contradicted at `q = 1` by Whitehead's lemma.

Only two consequences of −6 are load-bearing downstream, and both are consequences of the **genus**: the seven-element knot-operator generator set and the Hurwitz / genus-filtration bounds. The one genuine use of the integer −6 beyond the genus is the Kummer divisibility `n | χ(A)`, which is reading 4. Restating the Descartes condition as `g(M₀) = 4` loses nothing else.

## 1. The four readings in one table

| # | what `χ(A) = tr(id_A)` means at that site | the graded object it is extracted from | the extraction | sites (survey 1) |
|---|---|---|---|---|
| 1 | `dim_q(A) ∈ End(𝟙) ≅ k`, the rigid (Hom-level) trace — **owner ruling 2026-09-15** | `[A] ∈ K₀(𝐂)` (the character; the categorical Chern character in `HH₀(𝐂)`) | evaluate the character at the pivotal element: `dim_q(V_n) = ch(V_n)(q) = [n+1]_q`, classical `dim = ch(1)` | `prf:euler-char-stability` (`ev ∘ coev`), `knot-operator-selection-proof:66` (`[2]_q`), `notation-collisions.md:21` |
| 2 | `χ(M₀, V) = h⁰(V) − h¹(V)` for the rank-2 bundle `V = τ(A)` | `ch(V) = rk V + c₁(V) ∈ H⁰ ⊕ H^{1,1}(M₀)` | Hirzebruch–Riemann–Roch: `χ(M₀,V) = ⟨ch(V), td(M₀)⟩ = deg V + rk V·(1−g)` | `chi-minus-six-chain.md` Steps 3 and 6, `genus-maximal-descent-proof.md:2` |
| 3 | `χ_eu(M₀) = 2 − 2g = −6`, topological | `HH_•(M₀)` with `HH₀ = k²`, `HH_{±1} = k^g` (HKR); or `ch(T_{M₀}) = 1 + c₁(T)` | alternating sum `Σ(−1)ⁿ dim HH_n`; or `∫c₁(T_{M₀})` (Poincaré–Hopf) | `lem:brings-euler-characteristic`, `universality-general.md`, `bringTilingEuler_eq`, `BringsQOU.eulerChar_eq` |
| 4 | the obstruction class `κ₀ ∈ H²(𝒮, ℬ)` / generator of `HH²(𝒰_q, Ad) ≅ k` | the class itself | a "trace map `H²(𝒮,ℬ) → R`" (no construction, no Lean); `trace_pairing : ℤ → ℝ` and `chern_character` are class fields marked "honest domain gap" in `qou_obstruction_reduction.lean:78–118` | `skein-resolution-obstruction.md:1,11,17`, `qou-obstruction-reduction-proof.md:50`, `qou-p-neq-np.md:43`, `motivic-perpetual-obstruction.md:11` |

A fourth-and-a-half reading, `descartes_trace : MarkovTrace hp (singleton []) = -6` in `vertex-algebra-relations.lean:236`, is an axiom over an axiom asserting a Markov-trace value for every strand count and parameter; it is retired below.

## 2. The mathematics behind each reading

### 2.1 Reading 1: the rigid trace is one evaluation of the character

In a pivotal (here: ribbon) category the trace of an endomorphism `f : V → V` is `tr(f) = ev ∘ (f ⊗ id) ∘ coev ∈ End(𝟙)`, and `dim_q(V) = tr(id_V)`. For `𝐂 = Rep(U_q(𝔰𝔩₂))` with `End(𝟙) = k` this is a scalar by construction, so the question "one term of what?" is answered one level up: `dim_q` factors as

```
K₀(𝐂)  ──ch──▶  HH₀(𝐂)  ──ev_q──▶  k
```

where `K₀(𝐂)` is the split Grothendieck group (free on the simple objects, which is what QU axiom 4 makes it), `ch` is the categorical Chern character of Beliakova–Guliyev–Habiro–Lauda (their §1.4 "comparing Grothendieck group and trace", `library/arxiv-1409.1198v1`), `HH₀(𝐂) = ⊕_λ k·[p_λ]` is spanned by the central idempotents (QU axiom 4 again), and `ev_q` evaluates the character at the pivotal element. Concretely `ch(V_n)(x) = xⁿ + xⁿ⁻² + ⋯ + x⁻ⁿ`, `dim_q(V_n) = ch(V_n)(q) = [n+1]_q`, `dim(V_n) = ch(V_n)(1) = n+1`. The character has `n+1` terms; the quantum dimension is one number obtained from all of them.

For `A = 𝒪_q(SU(2))`, Peter–Weyl gives `[A] = Σ_n [V_n]²` in the completion of `K₀`, so `dim_q(A) = Σ_{m≥1} [m]_q²`, divergent at every real `q ≠ 1` (#7421). The probe of this PR computes the two standard regularisations exactly (§8): ζ-regularised, **0 for every `q`**, which equals `χ_eu(SU(2)) = χ(S³) = 0`; Hadamard finite part, `−1/(q − q⁻¹)²`, about −22.9 at `q₀`. Neither is −6.

### 2.2 Reading 2: Riemann–Roch for the bundle, and why it lands on 2 − 2g

For a vector bundle `V` of rank `r` and degree `d` on a curve of genus `g`, `χ(M₀, V) = d + r(1 − g)`. The chain uses `r = 2` (axiom 5, `su2_emergence_rank_forced`) and `d = 0` (`det V` trivial, from `G ⊆ SU(2)`), so `χ(M₀, V) = 2(1 − g)`. This equals the topological `χ_eu(M₀) = 2 − 2g` **iff** `d = (2 − r)(1 − g)`, i.e. exactly because `r = 2`. So the coincidence between "the Euler characteristic of the bundle" and "the Euler characteristic of the base" is the rank-2 fact, not an identity. Nothing is hidden in this reading; but the genus is an input from the base (through the Todd class `td(M₀) = 1 + (1−g)[pt]`), and −6 says `g = 4` only after the count 6 has been supplied from elsewhere (#7414).

### 2.3 Reading 3: the alternating sum over Hochschild homology

For a smooth projective curve `X` of genus `g`, HKR gives `HH_n(X) ≅ ⊕_i H^i(X, Ω^{i+n})`:

| `n` | summands | dim |
|---|---|---|
| 0 | `H⁰(𝒪) ⊕ H¹(Ω¹)` | 2 |
| 1 | `H⁰(Ω¹)` | `g` |
| −1 | `H¹(𝒪)` | `g` |

so `Σ(−1)ⁿ dim HH_n(X) = 2 − 2g = χ_eu(X)`, and for `g = 4` that is −6. This is the precise sense in which −6 is "a single number from a larger graded object": it is the Euler characteristic of `HH_•(M₀)`, and `HH₀(M₀)` alone has **two** components (rank and the point class), neither of which is −6. Equivalently −6 = `∫ c₁(T_{M₀})`, the degree-2 component of `ch(T_{M₀}) = 1 + c₁(T_{M₀})`. The Lean file `lean/QOU/Information/EulerCharacteristicOfHochschild.lean` (this PR; it was named here before it existed, and written on 2026-09-15 after the gap was noticed) proves the alternating-sum identity from a dimension-level HKR hypothesis, sorry-free: `hhEuler_eq_hodgeEuler` re-indexes `Σ_n (−1)^n dim HH_n` as `Σ_{i,j} (−1)^{i+j} h^{i,j}` for any Hodge square, and `hhEuler_curve` / `hhEuler_bring` give `2 − 2g` and `−6`.

For cohomology, `HHⁿ(X) ≅ ⊕_{p+q=n} H^p(X, Λ^q T_X)`: `HH⁰ = 1`, `HH¹ = H¹(𝒪) = g`, `HH² = H¹(T_X)` of dimension `3g − 3 = 9` at `g = 4`. The 9 is the tangent space to the moduli of genus-4 curves. Its `S₅`-invariant part is **0** (Bring's curve is rigid: signature `(0; 2,4,5)` has moduli dimension `3·0 − 3 + 3 = 0`), and the full `S₅`-module is `[4,1] ⊕ [3,2]` (standard ⊕ five-dimensional), with no trivial and no sign summand — measured exactly in §8. The `S₅`-invariant Hochschild theory of the base is therefore `k` in `HH⁰` and `k²` in `HH₀` and nothing else; its alternating sum is `χ(Σ₄/S₅) = χ(ℙ¹) = 2`, which is the "2" of `quantum-characteristic-classes-su2.md:10`.

### 2.4 Reading 4: the obstruction class, and what the derivation of `HH² ≅ k` actually establishes

`qou-obstruction-reduction-proof.md` argues: (Step 1) observability gives `HH⁰(𝒰_q, Ad) = Ad^G = 0`; (Step 2) Frobenius self-duality gives "Poincaré duality `HHⁿ ≅ (HH^{d−n})^∨`, `d = dim G = 3`" citing Yekutieli; (Step 3) "`HH² ≅ (HH¹)^∨`, and the outer-derivation space is one-dimensional because `q` is the unique deformation direction (Drinfeld)". Three gaps, each of which changes the conclusion:

1. **Derivations are not deformations.** A deformation direction is a class in `HH²`; `HH¹` is outer derivations (infinitesimal automorphisms). Drinfeld's rigidity concerns Hopf-algebra deformations of `U(𝔤)` and says nothing about `HH¹` of `𝒰_q`.
2. **The duality is cohomology-to-homology, with a twist.** For a Noetherian Hopf algebra that is AS-Gorenstein of dimension `d`, Brown–Zhang (`library/arxiv-math-0603732v2`, main theorem) give `HHⁱ(H, M) ≅ HH_{d−i}(H, ν M)` with `ν` the Nakayama automorphism; `ν` is trivial (up to inner) for `U(𝔤)` and `𝒪(G)` and **non-trivial** for `U_q(𝔤)` and `𝒪_q(G)`. The untwisted statement fails at `q ≠ 1`: Feng–Tsygan (`library/1104248094`) find the dimension drop `HH₃(𝒪_q(SL₂)) = 0`, and Hadfield–Krähmer (`library/arxiv-math-0405249v5`) recover a one-dimensional top group only in the twisted theory. So Step 2's target is `HH₁(H, Ad_ν)`, not `(HH¹)^∨`.
3. **At `q = 1` the space is zero.** `HHⁿ(U(𝔤), M) ≅ Hⁿ(𝔤, M^{ad})` (Cartan–Eilenberg XIII.5), and Whitehead's lemmas give `H¹(𝔤, M) = H²(𝔤, M) = 0` for `𝔤` semisimple in characteristic 0 and `M` finite-dimensional, hence for locally finite `M` such as `Ad(A)`. So the classical-limit obstruction space is **0** at the classical point, and a non-zero class would be a purely quantum phenomenon that no computation in the corpus exhibits. The one-dimensional cohomology that does exist for `SU(2)` is `H³(𝔰𝔲₂; k) = k`, the Cartan 3-form (integrally `H³(SU(2); ℤ) = ℤ`, the Chern–Simons level), in degree 3 with trivial coefficients — an instanton-number-type invariant, not an `HH²` obstruction.

The Lean carrier `qou_obstruction_reduction.lean` already labels `vdb_duality` and `drinfeld_rigidity` as `INPUT` class fields, and `ChiMinusSix.lean:44` carries the docstring slip "`HH² ≅ (HH⁰)^∨ ≅ k`" against its own `hh0 = 0`. So the honest status of "`χ(A) ∈ HH² ≅ k`" is: an unproved hypothesis about the substrate's deformation theory, contradicted at `q = 1`. That is the **Wigner axiom** of §12.

## 3. Where the corpus collapses the class to a number, and what is assumed

| assumption | explicit or implicit | where | status |
|---|---|---|---|
| `c₁(Ad A) = c₂(Ad A) = 0` — the Chern character of the adjoint object is its rank through degree 2 | **explicit axiom** (measurability, `quantum-observable-universe.md:6`) | QOU condition 4 | on a curve base `c₂ = 0` for dimension reasons, so the axiom has content only on the higher-dimensional total spaces `𝒮_n` |
| `deg V = 0` | explicit, **derived** from `det V = 1` | `chi-minus-six-chain.md` Step 2 | fine |
| `qdimUnit ≡ 1` — the `dim_q`-weights of `H^i(Σ₄)` are 1 | **implicit** (`def qdimUnit (_q) := 1`) | `brings_euler_characteristic.lean:42–68` | makes a `q`-dependent super-trace `q`-independent by fiat |
| a trace map `H²(𝒮, ℬ) → R` sending `κ₀` to `χ(A)` | **implicit**, never constructed | `quantum-characteristic-classes-su2.md:10`, `motivic-perpetual-obstruction.md:11`, `qou-obstruction-reduction-proof.md:50` | no Lean, no definition |
| `HH²(𝒰_q, Ad) ≅ k` | stated as a theorem, rests on §2.4's three gaps | `thm:qou-obstruction-reduction`(a) | contradicted at `q = 1` |
| the level-1 trace equals the total space's Euler characteristic | **implicit** in one sentence | `euler-char-stability.md:5` | false under the ruling except on a locus in `q` |
| `χ(𝒮_{n+1}) = χ(𝒮_n)` | asserted after computing `χ(𝒮_{n+1}) = χ(𝒮_n)·χ(S²) = 2χ(𝒮_n)` | `euler-char-stability-C.md` | the proof's own multiplicativity formula contradicts the stated stability unless `χ = 0`; its last sentence quietly switches to `χ(M₀)` |
| `[A] ∈ K₀(𝐂)` has "rank −6" | explicit | `archimedean-condition.md:7` | false under reading 1 (`rank` there is `dim_q`, regularised 0); `K₀(𝐂)` is never defined |

## 4. Defects found (beyond the scalar collapse)

1. `prf:euler-char-stability-C`: multiplicativity `χ(𝒮_{n+1}) = 2χ(𝒮_n)` is stated and then "the Euler characteristic rigidly persists" is asserted; the proposition's archimedean clause `χ(A_n) = χ(𝒮_n)` cannot be stable. What is stable is `χ(M₀)`. Fixed in this PR by restating the proposition about the base.
2. `ChiMinusSix.lean:44` docstring: `HH² ≅ (HH⁰)^∨` with `hh0 = 0` would give `HH² = 0`. Corrected to `(HH¹)^∨` in the docstring, and the whole class is re-labelled as the Wigner hypothesis.
3. `HochschildH1.lean:21` header claims "all sorry-free" over a file with 8 `sorry`. Corrected.
4. `thm:qou-obstruction-reduction` Step 2 states the wrong form of the duality (cohomology-to-dual-cohomology, untwisted) and Step 3 conflates `HH¹` with deformation directions. Rewritten in the twisted form, with the one-dimensionality moved to the Wigner axiom.
5. `descartes_trace` (axiom over axiom) asserts a Markov-trace value the corpus's own `MarkovTrace.lean` says is un-normalised. Retired in this PR.

## 5. What downstream actually consumes

Every downstream computation consumes the integer `g = 4`, never the trace (survey 1 §5–6):

- knot-operator generator set: `(m−1)(n−1) ≤ 2g = 8` ⟹ `{(2,3),(2,5),(2,7),(2,9),(3,4),(3,5)}` plus the unknot, seven generators (`torus-knot-generators.md:8`, `torus-embeddable-complete.md`); `tm-interaction-completeness.md` reaches seven independently as `1 + 4 + 2`;
- Hurwitz bound `|Aut| ≤ 84(g−1)` and the genus-filtration ideal `𝔦₄ = (u⁵)`;
- the electroweak-triplet embeddings and the `S₅` geometry.

The single use of the *integer* −6 beyond the genus is the Kummer divisibility `n | χ(A)` (`skein-resolution-obstruction.md:17`, `ClassicalLimitObstruction.lean:77`), which is reading 4 and moves with the Wigner axiom.

## 6. The #7421 ruling and its alternatives: implications and contexts

| reading | mathematical context | physical context | what it forces downstream |
|---|---|---|---|
| 1. `dim_q(A)` (ruled) | pivotal/ribbon trace; `K₀ → HH₀ → k`; Reshetikhin–Turaev unknot value; `dim_q(V_n) = [n+1]_q` | value of the unknot Wilson loop in Chern–Simons/WZW; total quantum dimension `D² = Σ d_λ²` and topological entanglement entropy `−log D`; growth rate of anyonic Hilbert spaces | `tr(id_A)` is `q`-dependent (enacted, #7411); for `A = 𝒪_q(SU(2))` it needs a regularisation and is 0 or `−1/(q−q⁻¹)²`; the Descartes condition, `euler-char-stability`'s bridge, the `K₀`-rank sentence and `descartes_trace` all have to move off `tr(id_A)` |
| 2. `χ(M₀, V)` | HRR; `χ(𝒪, V) = Σ(−1)ⁱ dim Extⁱ`; the functional `K₀(M₀) → ℤ` | index of the Dolbeault operator `∂̄_V` (Atiyah–Singer): sections minus obstructions of the SU(2)-bundle; `−6 = 2 − 2g` is two sections against `2g = 8` obstructions | keeps the chain arithmetic; needs `V` named (not `A`); coincides with reading 3 only because `rk V = 2` |
| 3. `χ_eu(M₀)` | Gauss–Bonnet / Poincaré–Hopf; `Σ(−1)ⁿ dim HH_n`; Riemann–Hurwitz | `∫K = 2πχ`; genus counts the independent cycles `b₁ = 2g = 8` and hence the moduli; worldsheet Euler characteristic weights a genus expansion | the cleanest home for −6; needs the symbol `χ_eu(M₀)` and the Descartes condition restated as `g(M₀) = 4` |
| 4. `HH²`-class | deformation theory; Kummer divisibility | obstruction to the classical limit; anomaly-like | unproved and contradicted at `q = 1`; must become a named conjecture (Wigner axiom) confined to the Millennium blocks |

## 7. Which object is `A` in `tr(id_A) = [2]_q`

| option | for | against | downstream if adopted |
|---|---|---|---|
| the fundamental `V` | `dim_q V = [2]_q` is the ruled value; `thm:su2-emergence` (`dim V = 2`); `knot-operator-selection-proof:66`; `chi-minus-six-chain` Step 1 literally says "the object `A` is the fundamental representation" | `A` is the Frobenius–Hopf object everywhere else (`def:quantum-universe`: `A = 𝒪(SU(2))`); even for `V`, `tr(id_V) = [2]_q ≠ χ(M₀, V) = −6` | a paper-wide symbol collision unless the chain's `A` is renamed `V` |
| the Frobenius–Hopf object `𝒪_q(SU(2))` | it is what the axioms call `A`; Peter–Weyl makes it the regular representation, the natural carrier of traces | `dim_q` diverges; regularised 0 (ζ) or `−1/(q−q⁻¹)²`; then `tr(id_A) = [2]_q` is false | `tr(id_A) = 0 = χ_eu(SU(2))` under ζ; the −6 cannot be attached to `A` at all |
| both, distinct symbols (**recommended**, as judgement) | every formula becomes true as written; matches the corpus's own usage (`V` for the fibre, `A` for the algebra) | about twenty sites to touch, all listed in survey 1 | `dim_q(V) = [2]_q`; `tr(id_A)` regularised `= 0`; −6 renamed `χ_eu(M₀)`; Descartes condition `g(M₀) = 4` |

## 8. Measured this session (probe, exact)

`computations/audits/dimq_regularisation_schemes_probe.py`, witness `dimq-regularisation-schemes.witness.json`, `mpmath` at 50 dps and exact `Fraction` character arithmetic:

- generating function `F(t) = Σ_{m≥1} [m]_q² tᵐ` has the closed form `(q²t/(1−q²t) + q⁻²t/(1−q⁻²t) − 2t/(1−t))/(q−q⁻¹)²`, checked against 400-term partial sums at a convergent `t`;
- ζ-regularised value `0` at `q₀` and at `q = 3/2, 2, 1.01` (the geometric pieces sum to −1, the constant piece `−2ζ(0) = +1`);
- Hadamard finite part `−1/(q−q⁻¹)²`, equal to −6 only at `q − q⁻¹ = 1/√6`, i.e. `q ≈ 1.2247`, not at `q₀ ≈ 1.10998`;
- `H¹(T_{Σ₄}) ≅ [4,1] ⊕ [3,2]` as an `S₅`-module, multiplicities of the trivial and sign representations 0 (from `H¹(T) = H⁰(K²)^∨`, Noether's `H⁰(K²) = Sym²H⁰(K)/(quadric)`, `H⁰(K) = ` standard representation, the quadric invariant).

The regularised trace is scheme-dependent; the probe selects none. What it excludes (scope b, invariant = exact rational identities) is "`tr(id_A) = −6` at `q₀` for `A = 𝒪_q(SU(2))` under either scheme".

## 9. HKR: is it needed, and what the literature actually offers at `q ≠ 1`

HKR (Hochschild–Kostant–Rosenberg) is invoked by name in five content blocks and never stated (survey 2 §2). For the χ chain it is **not needed**: reading 2 is Riemann–Roch and reading 3 is Poincaré–Hopf, both theorems. It is needed only where a Hochschild class is identified with a geometric object — `rem:poisson-hkr-connection` (the Poisson bivector from `HH²(A,A)`, the classical `q = 1` case, where HKR holds verbatim for smooth commutative `A`), and the two `q-geometric-langlands` blocks that identify a `q`-curvature with an `HH²` class at `q ≠ 1`.

What the literature offers at `q ≠ 1` is not an HKR isomorphism but two substitutes: (i) for a *formal* deformation `A_ℏ` of a smooth commutative algebra, Kontsevich formality (`library/arxiv-q-alg-9709040v1`) identifies `HH^•(A_ℏ)` with the Poisson cohomology `H^•_π[[ℏ]]`, and in the symplectic case with de Rham cohomology (Nest–Tsygan, `library/download-3`; Dolgushev–Rubtsov, `library/arxiv-math-0408210v3`); (ii) for the algebraic quantum group at fixed `q`, twisted Poincaré duality (Brown–Zhang) and the explicit computations (Feng–Tsygan, Hadfield–Krähmer), which show the naive HKR *fails* (dimension drop). Options:

- (a) state HKR as a cited theorem for the commutative fibre (`q = 1`) — adopted;
- (b) make the `q ≠ 1` identifications of the two q-GL blocks a named conjecture class — adopted for those two blocks only;
- (c) rewrite `thm:qou-obstruction-reduction`(b) on the geometric route (`κ₀ = e(ξ)` as the one named hypothesis, then Poincaré–Hopf) — adopted;
- (d) route the Millennium blocks through the Wigner axiom — adopted;
- (e) work the fibre formally in `ℏ = q − 1` so that formality applies verbatim, with the evaluation at `q₀` as a separate archimedean claim — the fibre-versus-observable doctrine already says this; recorded as the intended reading in `rem:classical-shadow-of-the-substrate`.

## 10. Yekutieli's hypotheses the axioms do not supply, and the options

| hypothesis | what Yekutieli needs it for | what the corpus has | option |
|---|---|---|---|
| a formal (pro-nilpotent) parameter | convergence of the Maurer–Cartan series and the gauge action in the pronilpotent DG Lie algebra (2009 MC paper; twisted deformation quantization 2008/2010) | `q − 1 ≈ 0.11`, a real number | work formally in `ℏ = q − 1` on the fibre; the evaluation at `q₀` is the archimedean functor's job and a testable convergence claim |
| which theorem is used | the lifting proof cites only Theorem 4.17 of the 2010 central-extensions-of-gerbes paper, which is Čech and needs **no** nilpotence | the twelve-row dictionary mixes this with the MC rows | split the dictionary by hypothesis; only "vacuum state = unique MC element" and "substrate field = local deformation parameter" need the formal side |
| smoothness of the base | HKR-type identifications; Yekutieli works over a smooth separated `k`-scheme | asserted in `def:spatial-realization-functor` ("an ordinary smooth manifold") | replace the assertion by the categorical condition "`Ω¹(A)` is a dualisable object of constant rank" (Kähler differentials projective ⇔ formally smooth); it is the same hypothesis HKR needs |
| characteristic 0, `6 ∈ R^×` | the DG-Lie side needs `ℚ ⊆ R` | finite-field and `p`-adic models exist in Ch. 5 | state that the DG-Lie half is developed over ℚ-algebras; the finite-field models get the Čech half |
| Čech–de Rham and the DG Lie algebra | the cosimplicial DG Lie algebra and its MC equation | Čech side spelled out; DG-Lie side two table cells | one block stating the cosimplicial DG Lie algebra and its MC equation, whose solution set is the descent condition the corpus already has |

## 11. Fourier–Mukai and Orlov: context, and where they could close a gap

The corpus uses no integral transform; its equivalences are Tannakian (`𝐂 ≃ Rep(H)`), which are monoidal, not derived. On the base itself FM buys nothing: by Bondal–Orlov a curve of genus ≥ 2 has no non-trivial derived partners and its autoequivalences are `Aut(X) ⋉ Pic(X) × ℤ[1]`. Where the language would help is precisely the unconstructed trace map: an integral transform `Φ_K : 𝒟(A) → D^b(M₀)` induces `HH_•(Φ_K)` canonically, and its trace is `ch(K)` (Căldăraru–Willerton, `library/arxiv-0707.2052v1`); that is a construction, not an assumption, and it forces the substrate's Hochschild dimensions to be the curve's (`2, 4, 4` in homology; `1, 4, 9` in cohomology; invariant parts `2, 0, 0` and `1, 0, 0`). It needs the archimedean realisation stated at the derived level, which the corpus has not done (τ lands in `Vect`). Orlov's representability theorem (fully faithful exact functors between `D^b` of smooth projective varieties are FM) would then apply to that functor. A direction, not a closure; recorded as a remark and a question.

## 12. Resolution adopted (owner selections of 2026-09-15: A, B, C; "both, distinct symbols"; "go with your recommendations")

**A — separate by name.** `χ_eu(M₀)` (topological), `χ(M₀, V)` (sheaf), `dim_q(V)` (rigid trace), `κ₀` (obstruction class) get distinct symbols in the notation register; the Descartes condition is restated as `g(M₀) = 4`; `prop:euler-char-stability` is restated about `χ_eu(M₀)`; `lem:brings-euler-characteristic` names the topological Euler characteristic; `descartes_trace` is retired; the `K₀`-rank sentence is rewritten.

**B — the explicit layer.** New blocks: `def:hochschild-homology`, `rem:hkr-theorem`, `rem:classical-shadow-of-the-substrate`, `def:grothendieck-group-of-a-qou`, `ex:su2-characters-and-quantum-dimension`, `rem:trace-ledger`, `rem:categorical-trace-is-the-markov-trace`, `def:chern-character`, `rem:three-euler-characteristics`, `rem:euler-characteristic-of-the-regular-representation`, `rem:yekutieli-setting-explicit`, `rem:s1-action-and-loop-space`, `rem:fourier-mukai-and-orlov`, glossary entries for distinguished triangles, derived and dg categories, the Fourier–Mukai transform and the Grothendieck group.

**C — cut the `HH²` scalar from the χ chain.** The chain runs on readings 2 and 3 only. `thm:qou-obstruction-reduction` keeps (a) and (c) as statements conditional on the **Wigner axiom** (`conj:wigner-axiom`, cited to Wigner's Courant lecture of 11 May 1959, *Comm. Pure Appl. Math.* 13 (1960) 1–14): *the classical-limit obstruction space of the substrate is one-dimensional and spanned by a class whose archimedean image is the Euler class of the tangent bundle of the base.* Its (b) is rewritten on the geometric route.

**D — recorded, not enacted.** The regularisation negative (§8) is a remark; no regularisation is selected.

## 13. Open for the owner

1. The Wigner axiom is a hypothesis about the substrate, contradicted at `q = 1`; whether to keep the Millennium blocks conditional on it or to demote them to conjectures outright.
2. Which of the Oberwolfach talks in pages 9–40 was meant ("Towards a categorification of the universal `sl(2)` link invariant", p. 23, or "Yokonuma–Hecke algebras", p. 28, are the on-topic ones).
3. Whether the archimedean realisation should be upgraded to a derived functor so that the FM/Orlov machinery of §11 applies.
