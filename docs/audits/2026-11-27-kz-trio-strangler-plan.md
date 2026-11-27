# KZ trio: strangler plan (prep, bean `qou-dk7p`)

Prepared 2026-11-27 while the rational (Bar-Natan) associator is still in progress. Nothing here
moves a module yet. The plan follows the owner ruling recorded in
[`docs/coordination/owner-rulings.md`](../coordination/owner-rulings.md), 2026-11-27: isolate the
transcendental and analytic results in `QOU/Transcendental/` and keep the rest algebraic.

## 1. The audit was blind to the KZ chain

`scripts/transcendental-boundary-audit.py` matched named analytic lemmas such as `Tendsto`, `deriv`
and `Real.exp`. It did not match a module that is analytic only through its typeclass context,
`[NormedAlgebra ℂ R] [CompleteSpace R]`, or through `NormedSpace.exp`. Because of that, the
KZ/Drinfeld chain read as "algebraic but tainted" when it is in fact analytic.

The detector now matches `NormedSpace.exp`, `CompleteSpace` and `NormedAlgebra ℂ`. This adds **13
modules** to the outside-boundary baseline, measured 2026-11-27 (559 → 572). They are added as a
measurement correction, not a regression:

- the KZ shift/pentagon/hexagon layer: `KZShift`, `KZShiftPhi`, `KZPentagon`, `KZHexagonCentral`;
- the KZ holonomy files `MassTheory/KZHolonomy/*`, `HeckeTemperleyLieb/KZHolonomy/BraidRep` and
  `MathlibExt/KZHolonomy/LinearODE`;
- `MassTheory/BridgeAP2Regular`;
- `CompactQuantumMetrics/AlgebraicGnsEmbedding`, which is a Hilbert-space GNS file and is correctly
  analytic.

`Transcendental ℚ c` is deliberately **not** matched. It is a hypothesis about a field element, and
the Drinfeld files use it to choose a generic complex parameter `c`.

The three `QOU/Nuclear/Nucleon*` NEW rows the check reports come from other commits on `main`. They
are left visible and are not baselined here.

## 2. The interface already exists

`QOU/BraidsAndKnots/DrinfeldAssociator.lean` defines `structure Associator`. Its fields are an
admissibility predicate, `Φ`, inversion, unit, central shift, commutation, naturality, the pentagon
and the central hexagon, together with the half-twist `ePi X = NormedSpace.exp ℂ (−iπ X)`. The
Drinfeld category `Drinfeld/*` (21 files, about 3,800 lines) takes `Ψ : Associator` as a parameter.
So the category is already written against an interface, and the KZ associator is only one instance
of it.

The interface itself is analytic in two places:

1. every field quantifies over `[NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]`;
2. `ePi` is the analytic exponential.

## 3. Plan (corrected the same day)

The first version of this section proposed making `Associator` algebraic by replacing the normed
context with a half-twist field. That does not work. The `Drinfeld/*` files use the analytic
structure directly, not only through `Ψ`:

- the carriers are complex matrices with local `linftyOpNormedRing` instances;
- the coupling `c : ℂ` is assumed `Transcendental ℚ c`;
- `Braiding`, `BraidingVV`, `RibbonDH` and `Hexagon` call `NormedSpace.exp`, `expSeries` and
  `map_exp` themselves.

So the Drinfeld category as written is a specialisation of the formal parameter `h` to a
transcendental complex number. It is analytic, and an algebraic version is a new h-adic construction
rather than a change to its signature.

**Measured 2026-11-27:** the trio and everything downstream of it is **47 modules**. Apart from
`QOU.lean`, the only importer outside those 47 is `QOU/Transcendental/MassTheory/BridgeAStokesNBody`,
which is already inside the boundary. The chain is therefore a closed subgraph.

| step | change |
|---|---|
| A | Move the 47 modules, unchanged, into `QOU/Transcendental/BraidsAndKnots/` (and `.../MassTheory/` for the four `MassTheory` members). The work is renaming import paths and updating one content-block reference. |
| B | After Bar-Natan stage 5, build the h-adic Drinfeld category over `k⟦h⟧` from the rational `Φ`, outside the boundary. #9519's quasi-Yang–Baxter result is its first consumer. |
| C | Once the algebraic category covers what the analytic one proves, keep the analytic chain as the comparison instance inside the boundary (KZ = specialisation at a transcendental `c`). |

## 4. Cut edges (algebraic module → analytic import), measured 2026-11-27

```
BlockResidues        <- KZHexagonCentral, KZShiftPhi
Drinfeld.Assoc       <- KZHexagonCentral
Drinfeld.Transport   <- KZIntertwine
Drinfeld.Whisker     <- DrinfeldAssociator
GLnKZ                <- KZHexagon, KZPentagon, KZShiftPhi
Drinfeld.Braided/Twist <- Drinfeld.Hexagon
Drinfeld.Duals       <- Drinfeld.BraidingVV, ZigZag
Drinfeld.HeckeStrands <- Drinfeld.RibbonDH
```

All of these edges are inside the 47-module chain, so step A removes them from the outside set.

## 5. Step B prep, 2026-11-27

Step A has landed (#9643). Step B starts with the part that does not depend on `Φ`:
`QOU/BraidsAndKnots/HAdicDrinfeld/CasimirData.lean`, over any commutative ring `k`.

- `CasimirData` holds a cocommutative coproduct `Δ` and a symmetric invariant tensor `t` with
  the two splitting identities. For `A = U(𝔤)`, `t` is the split Casimir.
- `CasimirData.dk3`: `(t₁₂, t₁₃, t₂₃)` is a `RationalAssociator.DK3` family. So the hexagon
  results proved for `DK3` families apply to it.
- `CasimirData.dk3_smul`: the rescaled family `(c t₁₂, c t₁₃, c t₂₃)` is `DK3` too. With
  `k = ℚ[h]/(h^N)` and `c = h`, this is where the rational associator is evaluated.
- `CasimirData.quasiCocomm_aeval`: every polynomial `p(t)` is quasi-cocommutative. That is the
  hypothesis `hR` of `quasiYBE_of_hexagon`, and the truncated `exp(h t / 2)` is such a
  polynomial.

`QOU/BraidsAndKnots/HAdicDrinfeld/FourStrand.lean` adds the four-strand part:

- `CasimirData.dk4`: the six leg copies of `t` in `A^{⊗4}` form a `DK4` family. The near relations
  are `dk3` pushed along the four inclusions that each omit one strand. The far relations hold
  because the legs sit in disjoint tensor factors.
- `evalU4` (for any `ℚ`-algebra, with a central nilpotent `z`) and `CasimirData.evalU4` (with
  `c ∈ k`, `c ^ N = 0`): the algebra map `U4 N → A^{⊗4}`, `tᵢⱼ ↦ c tᵢⱼ`, built through
  `UniversalDK.lift`. With `k = ℚ[h]/(h^N)` and `c = h`, this is the truncated h-adic evaluation.

`QOU/BraidsAndKnots/HAdicDrinfeld/Hexagon.lean` plugs in the stage-5 associator (#9807, #9810):

- `CasimirData.realize3`: the realisation `U4 N → A^{⊗3}`, `t₁₂, t₁₃, t₂₃ ↦ c t₁₂, c t₁₃, c t₂₃`,
  `tᵢ₄ ↦ 0`. `QuasiYBE.lean` recorded that no such realisation was available; this is it.
- `CasimirData.rMatrix`: `R = E(c t)`. For `E = exp(X/2)` this is `exp(h t / 2)` modulo `h^N`.
- `CasimirData.hexagon`: for every rational associator `Φ` in `U4 N`,
  `(Δ ⊗ id)(R) = Φ₃₁₂ R₁₃ Φ₁₃₂⁻¹ R₂₃ Φ₁₂₃`, with the associators realised by `realize3`.
- `CasimirData.quasiYBE`: the quasi-Yang–Baxter equation, from `quasiYBE_of_hexagon`.

Still open: the pentagon transported to `A^{⊗4}` through `CasimirData.evalU4`. It needs the four-strand
coproduct identities `(Δ ⊗ id ⊗ id)`, `(id ⊗ Δ ⊗ id)` and `(id ⊗ id ⊗ Δ)` on `Φ`.
