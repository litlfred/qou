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

## 3. Plan once the rational associator lands

Bar-Natan's thread, stage 5, discharges the `Φ` hypothesis of
`HeckeTemperleyLieb/QuasiYangBaxterFromHexagon.lean` (#9519).

| step | change | consumers touched |
|---|---|---|
| A | Generalise `Associator` to an algebraic carrier: a `ℚ`-algebra `R`, with a half-twist `e : R → R` given as a field satisfying `e(X+Y) = e X · e Y` for commuting `X, Y` and `Commute c X → Commute c (e X)`. These two laws are what `KZHexagonCentral` uses (`eπ_add`, `commute_eπ`). | `DrinfeldAssociator`, `Drinfeld/*` signatures (normed context drops) |
| B | Build the KZ instance (`phiKZ`, `ePi = NormedSpace.exp`) as `Associator.ofKZ` and move it, with `AssociatorKZ`, `KZEdge`, `KZHexagon`, `KZShift`, `KZShiftPhi`, `KZPentagon` and `KZHexagonCentral`, into `QOU/Transcendental/BraidsAndKnots/`. | `GLnKZ`, `BlockResidues`, `KZIntertwine`, `ZigZag` import the instance from inside the boundary |
| C | Instantiate `Associator` from the rational `Φ` over `R⟦h⟧`, with `e X = exp(h X / 2)` as a formal power series. The quasi-Yang–Baxter result (#9519) then becomes a corollary. | new file only |
| D | Re-run the audit. `Drinfeld/*` should leave the outside set; the `Braiding`, `BraidingVV` and `RibbonDH` files still call `NormedSpace.exp` directly and need the same `e`-field treatment. | 3 files |

Steps A and B do not need the rational associator, so they can start now. Step C waits on stage 5.
Step A changes the type of a public structure that 21 files use. That makes it a single PR of
roughly 30 files, which is the cost to weigh.

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

Every edge except the last three passes through the `Associator` interface or the KZ instance. Step
A plus step B cuts them.
