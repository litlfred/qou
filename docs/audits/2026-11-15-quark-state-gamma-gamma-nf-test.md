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

## 4a. First question: is a quark one strand (one letter) or one channel?

This question is prior to D1, and the hypothesis as stated answers it in a way that does not hold.

- **The (2,1) projection reads a three-strand channel.** Sibling #7823 (`qou-qs4c` §0.4) shows that at
  level 2 the (2,1) block of H₃ is isospin ½ for three strands, which is a nucleon. Klein–Kreisler's
  (2,1) state is a nucleon as well. So "NF(γγ) projected to (2,1)" names a **nucleon-type composite**.
  **Scope-(a) negative:** the hypothesis, as stated, does not define a single-quark state. This is not
  a structural exclusion. It is a mismatch between the object and its name.
- **What this file's theorems actually treat as the quark is a single letter.** In
  `template_*`, flavour is a per-letter sign bit: ℓ_g(c) = ρ(σ_g) + c·h·1, and a flip changes one
  letter by σ⁻¹ − σ = −h. The (2,1) character is taken of the **whole word** (core plus three quark
  letters) and is a nucleon observable. `template_order_zero` and `template_SplusAVG_proton` are
  therefore statements of the form "nucleon (2,1) observable built from three single-letter
  quarks". They are not statements about a (2,1)-projected quark.
- **Proposed alternative, NOT adopted:** quark state := a single-letter object σ_g^ε (generator g,
  flavour ε), with γγ supplying it through the word-degree-1 coordinates of NF(γγ). The (2,1)
  projection is then reserved for the **nucleon** state built from three of them. Under this
  reading the theorems already proved need no change. Only the names `quarkState` / `rho_pairNF_split`
  would move to a nucleon-level name. Nothing is redefined here. This is the owner's call (D1/D2).

## 4b. Owner decisions D1–D3 (2026-11-15), implemented

- **D1 = (b), per letter.** `quarkState g ε := hPart 1 (quarkLetter g ε)` over `R[X]`, with h = X formal.
  - Proved: `quarkState_eq` (= flavourShift ε · 1), `quarkState_flavour_ne`, `quarkLetter_order_zero`,
    `quarkLetter_order_ge_two`, `quarkLetter_inverse` (σ·(σ − h) = 1), and `hPart_one_pairNF` (on γγ, the
    h¹ part is N₁).
  - **Observation:** the per-letter quark state lies in **word degree 0**. It is a multiple of the unit. This
    is the same mechanism as `flavour_reaches_deg0` (§3).
- **Why "formal h".** Every NF coefficient is a polynomial in h whose coefficients are q-independent labels,
  because the Hecke relation σ² = hσ + 1 involves only h. The h-order split exists for the polynomial, not for
  a number at a fixed q. It is valid for all q, and evaluating at q₀ gives the observable. Caveats:
  - the labels must be q-independent;
  - the h¹ part must be taken *before* the (2,1) projection, whose matrices contain q and q⁻¹;
  - h² and higher terms are not part of the quark state.
- **D2 = rename.** `nucleonState` / `nucleonStateOfQuarks` is the (2,1) image of core × three single letters.
  `rho_letter` identifies each letter's image with the word's factor. The γγ projection is renamed
  `pairChannelState` and retired as "quark state". Caveat: the corpus S+ AVG template uses pair-averaged
  shifts (−½), which are not single letters. LO and HI are single letters.
- **D3 = fix.** The `L₊` label is an **orientation** trap, which corrects my earlier statement that coordinate
  3 "is σ₁σ₀":
  - `gram.hm` is left multiplication with concatenation, so `gram`'s coordinate 3 is σ₀σ₁ = L₊;
  - `mulNF` is the opposite product, so in the `H3A` ring coordinate 3 is σ₁·σ₀;
  - no value moves, because H₃ ≅ H₃ᵒᵖ by word reversal and TRM is z² on both coordinates.

  Documented on `mulNF` and `H3A.v`.

## 4c. Flavour extraction from NF(γγ) (bean `qou-usxh`, exploration; no map chosen)

The only flavour-sensitive datum the D1 definition supplies is the h¹ coefficient on the unit,
**net flavour** (`netFlavour`). It is additive (`netFlavour_add`), and on a letter it equals the
letter's flavour shift (`netFlavour_letter`). Results:

1. **Per-letter readout (Q1): not possible from a sum.**
   - `letter_sum_flavour_swap`: (u on σ₀) + (d on σ₁) = (d on σ₀) + (u on σ₁) as elements.
   - So a sum determines only the net flavour, never which letter carries which bit.
   - This residual freedom (Q3) is a finding. It is not resolved by choice.
2. **Net flavour of a photon pair is identically 0 (`pairNF_netFlavour`),** for every colour content,
   when both photons are built from σ letters with q-independent labels.
3. **uud / udd from one photon pair: the set is EMPTY (Q2)** (`pairNF_three_letters_all_up`).
   - Write NF(γγ) as three letters plus any remainder of zero net flavour. Then all three letters are u.
   - This is scope (b). The invariant is net flavour, which is additive and identically 0 on γγ.
   - The scope is stated exactly: σ-letter photons, q-independent labels, and the D1 functional.
4. **Flavour enters only through the photon's own letters.**
   - Flip the second photon's letters (σ ↦ σ⁻¹). Then the net flavour is −(ψ₀ + ψ₁ + (φ₀+φ₁)ψ₀₁)
     (`pairBar_netFlavour`).
   - So the net flavour equals the flavour put in, and the collision does not produce it.
   - Nucleon net flavour −1 (uud) or −2 (udd) then corresponds to the affine quadric
     ψ₀ + ψ₁ + (φ₀+φ₁)ψ₀₁ = 1 or 2. That is the level set of the input, not an extraction.

**Gap (open, beaned under `qou-usxh`).**
- A per-letter readout needs a PRODUCT (word) of letters, not a sum. The h¹ part of a word of letters
  is Σₖ cₖ·(word with letter k deleted), so the cₖ are recoverable exactly when those deleted words
  are linearly independent. This is not computed here.
- What decides a photon's letter orientation (σ vs σ⁻¹) is not derived here. It may connect to
  `qou-qs2u` (u as polarization or chirality).

## 4d. Flavour readout from a WORD of letters (bean `qou-qs1x`, research)

A sum of letters loses the per-letter bits (§4c). A product keeps them, with one structural exception.
The measurement was exact, over all 8 placements × 8 flavour assignments of core × ℓ(g₁)ℓ(g₂)ℓ(g₃),
by `computations/probes/quark_state/flavour_readout_word_probe.py` (sympy, exact, no float, no target).
Distinct objects out of 8 assignments:

| placement (g₁g₂g₃) | full NF | h¹ part | (2,1) matrix | (2,1) trace |
|---|---|---|---|---|
| 000, 111 | 4 | 4 | 4 | 4 |
| 001, 011, 100, 110 | 6 | 6 | 6 | 6 |
| 010, 101 (alternating) | **8** | **8** | 7 | 7 |

Findings, each proved in Lean (sorry-free):

1. **Letters on the same generator commute** (`sameGen_letters_commute`). Inside a run of consecutive
   same-generator letters, only the multiset of flavour bits is readable. This is the whole of the
   collision structure in the NF columns: every class is a permutation orbit within such runs.
2. **The h¹ part, the D1 quark state, carries all the readable information.** Its column equals the
   full-NF column at every placement.
   - Alternating word (`word010_hPart_one`): the h¹ part is (c₂, 0, 0, c₁, c₃, 0). Each letter's bit
     sits on its own coordinate, namely the word with that letter deleted.
   - Builder word σ₀σ₀σ₁ (`word001_hPart_one`): the h¹ part is (c₃, 0, 0, 0, c₁+c₂+1, 0). Only c₁+c₂
     survives.
3. **At the builder placement, the proton uud is uniquely readable but the neutron udd is not.**
   - udd ≡ dud: the d can sit on either σ₀ slot.
   - Reason: the neutron's two σ₀ slots carry different flavours, so the run hides which slot holds d.
     The proton's two σ₀ slots carry the same flavour, so there is nothing to hide.
4. **The (2,1) channel loses one more bit on the alternating word: uuu ≡ ddd.**
   - Reason: ρ(Δ⁻¹) = ρ(Δ) for Δ = σ₀σ₁σ₀ (`rho_delta_inv`), because the full twist Δ² acts as 1 on
     the (2,1) irrep (`rho_delta_sq`).
   - So the nucleon state does not see a global flavour flip of Δ, while the full NF does.

**What this does and does not settle.**
- A per-letter readout map is derived, not chosen, wherever the word separates the letters: it is the h¹
  coefficient on each deleted word.
- Where the word does not separate them (same-generator runs), the residual freedom is exactly the
  permutation of bits within the run. That is a finding, not something to fix.
- Which placement is canonical is **not** decided here. The builder's (σ₀,σ₀,σ₁) is a code convention, and
  the γγ/SDP selection (`qou-ales`) governs it.
- What fixes a photon's letter orientation (σ vs σ⁻¹) is still open.

## 5. Verification

`lean -DautoImplicit=false -s 65536` against the restored `cat/folio-assistant-sci/lake-cache/qou-v4-24-0`
Mathlib oleans. `MarkovTraceOnHecke` was recompiled from current source, not taken from the
snapshot. Result: exit 0. `#print axioms` on every exported theorem shows
[propext, Classical.choice, Quot.sound] only, with no `sorryAx`. Re-verified after D1–D3: 20/20 checked theorems are clean.

## 6. Decisions for the owner

These are listed in the PR and in the coordinator report.
