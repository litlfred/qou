# Testing the quark-state hypothesis on NF(γγ)

Bean `qou-qs1d` (epic `qou-qs0e`), PR #7827. Lean file:
`folio/quantum-observable-universe/lean/QOU/QuarkState/PhotonPairNormalForm.lean`.
Verification is in §5.

## 0. Result in five lines

The hypothesis under test is the agent's working hypothesis, **not adopted**: *quark state := the
word-degree ≥ 1 part of NF(γ(φ)·γ(ψ)) in H₃(q), projected to the (2,1) channel*. Two of its three
non-vacuity requirements **fail as stated**, and both failures come from one source: the
hypothesis uses **word degree**, while `results.md:9-13` is a statement about **order in the tower**
(powers of h = q − q⁻¹ = 2t + O(t²)).

1. **Holds in the h-grading.** NF(γγ) is *exactly affine* in h: NF = NF|_{h=0} + h·N₁. The h¹
   coefficient N₁ lies entirely in word degree ≥ 1, is homogeneous bilinear in (φ, ψ), and is
   nonzero. On γγ the order-1 part therefore satisfies all three requirements.
2. **Requirement (1) fails beyond order zero (scope a).** The word-degree-0 coordinate
   1 + φ₀ψ₀ + φ₁ψ₁ is h-free on γγ. But under the flavour flip of `quark_template`
   (σᵢ ↦ σᵢ⁻¹ = σᵢ − h), it moves by h·(hψ₀₁ − φ₀ψ₀₁ − φ₁ψ₀₁ − ψ₀ − ψ₁). That is **−h** on the
   witness ψ = σ₀. So "degree 0 carries no flavour" holds only modulo h.
3. **Requirement (3) fails as stated (scope a).** The degree ≥ 1 part contains the pass-through
   terms φ₀ + ψ₀, φ₁ + ψ₁ and φ₀₁ + ψ₀₁. It is affine-bilinear, not bilinear: at φ = 0 it is ψ's own
   polarization. The **connected part** NF((γ(φ)−1)(γ(ψ)−1)) *is* bilinear.
4. **`results.md:9-13` re-derived as theorems** in the probe's reduced-Burau (2,1) representation,
   which is proved multiplicative on the NF algebra.
   - At q = 1 the nucleon-word character is 0 for **every** choice of quark shifts.
   - The flavour-blind S0 template is identically 0.
   - The corpus template S+ AVG on the proton is (q−1)·g(q) with g(1) = −1, so flavour is decided
     at order t¹.

## 1. Two gradings

| grading | what it counts | `results.md` uses it? | hypothesis uses it? |
|---|---|---|---|
| word degree | length of the Gröbner–Shirshov word (1 : 0; σᵢ : 1; σ₁σ₀, σ₀σ₁ : 2; σ₀σ₁σ₀ : 3) | no | **yes** |
| tower order | power of h (equivalently t = q − 1) | **yes** | in the epic's gloss ("order 0 = γγ core") |

On the γγ product alone they are compatible:
- word degree 0 is pure order 0 (`pairNF_deg0_h_free`);
- order 1 is pure word degree ≥ 1 (`N1_deg0`).

They come apart as soon as flavour enters. A flavour flip is a multiple of h by definition
(σ⁻¹ − σ = −h), and multiplying by the unit 1 carries it into word degree 0
(`flavour_reaches_deg0`).

## 2. The γγ normal form (cross-check of tables 1–5)

`pairNF_eq` computes NF(γγ) from `QOU.Machinery.H3.mulNF` rather than asserting it, and
reproduces table 5 of `trivial-knot-photon-interpretation` coordinate by coordinate:

| basis | coefficient |
|---|---|
| 1 | 1 + φ₀ψ₀ + φ₁ψ₁ |
| σ₀ | φ₀ + ψ₀ + hφ₀ψ₀ + φ₀₁ψ₁ |
| σ₁ | φ₁ + ψ₁ + hφ₁ψ₁ + φ₀ψ₀₁ |
| σ₁σ₀ (= L₋) | φ₀₁ψ₀₁ + φ₁ψ₀ |
| σ₀σ₁ (= L₊) | φ₀₁ + ψ₀₁ + φ₀ψ₁ + h(φ₀ψ₀₁ + φ₀₁ψ₁) |
| σ₀σ₁σ₀ (= e⁻) | φ₀₁ψ₀ + φ₁ψ₀₁ + hφ₀₁ψ₀₁ |

So table 5 is correct. **Trap (not fixed here):** `QOU.Machinery.H3` (`MarkovTraceOnHecke.lean`)
labels coordinate 3 `L₊`, but coordinate 3 is σ₁σ₀ (`s1_mul_s0`). `rem:knot-basis-color-content`
writes L₊ = σ₀σ₁, which is coordinate 4 (`s0_mul_s1`). The two files use the same name for
opposite chiralities.

`QuarkAntiquarkProduction.lean` carries the φ₀₁ = 0 coefficients as **structure fields**, which
are asserted rather than computed. `pairNF_eq` is the computed version.

## 3. Flavour

Flavour here means the sign bit of `quark_template`: a letter is σ or σ⁻¹ = σ − h.

- Order zero: `photonBar_order_zero` (at h = 0 the flipped photon is the photon) and
  `template_order_zero`.
- Order one, in word degree 0: `flavour_reaches_deg0`, with witness `flavour_reaches_deg0_witness`
  (Δ = −h).
- Order one, in the (2,1) channel: `template_SplusAVG_proton` plus `gSplus_one` (t¹ coefficient −1),
  against `template_S0_zero` (identically 0).

A side observation, sympy only and not in Lean: the flipped product NF(γ(φ)γ̄(ψ)) is **not**
affine in h. It has an h² term in degree 0, and its e⁻ coordinate has no h term at all.

## 4. What this does and does not establish

- It **does not** establish that any element is "the quark state". The definition `quarkState` is
  stated so that it can be tested, and it is not adopted.
- The (2,1) projection: sibling PR #7823 (`qou-qs4c` §0.4) argues that at level 2 the (2,1) channel
  is an **isospin-½, nucleon-type** three-strand channel. So the projection may select a nucleon
  label rather than a single-quark state. Nothing here tests that; it bears on decision D2 below.
- No fitting, no CODATA, no selection. Every statement is an identity over a generic ring or field.

## 5. Verification

`lean -DautoImplicit=false -s 65536` against the restored `cat/folio-assistant-sci/lake-cache/qou-v4-24-0`
Mathlib oleans. `MarkovTraceOnHecke` was recompiled from current source, not taken from the
snapshot. Result: exit 0. `#print axioms` on every exported theorem shows
[propext, Classical.choice, Quot.sound] only, with no `sorryAx`.

## 6. Decisions for the owner

These are listed in the PR and in the coordinator report.
