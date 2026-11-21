import Mathlib.Tactic

/-
  Δ_λ binding exponent — keystone (formalize-first, arithmetic core only)

  Owner-directed research item 1 (PR #2485). The per-isotope Δ_λ binding
  exponent is currently a RAW combinatorial crossing count off the atom
  braid word `atom_braid_word_3A(Z, N)`
  (`computations/delta_lambda_exponent_from_crossings.py`):

      σ   = 7Z + 5N − 1      (positive crossings)
      σ⁻¹ = 3Z + 5N − 1      (negative crossings)
      σ + σ⁻¹ = 10A − 2      (Z, N cancel ⇒ slope 10 / nucleon, derived)
      σ − σ⁻¹ = 4Z           (A, N cancel ⇒ atomWrithe is proton-number-only)

  This file formalizes ONLY what is genuinely derived: the crossing-sum
  cancellation, the factorization 5·(2A−1) = 10A−5, and — the Z-dependent
  companion added here — the atomWrithe `σ − σ⁻¹ = 4Z` together with its
  intra/interface split `(3Z+N) + (Z−N) = 4Z`. These are pure arithmetic
  facts about the crossing bookkeeping; they make NO claim that the binding
  exponent (or its correction) equals them.

  The bar-decomposition is the physical content: the **symmetric** sum
  `σ+σ⁻¹` is bar-even (q ↦ q⁻¹ invariant), A-only, and sets the *leading*
  exponent `10A−5`; the **antisymmetric** atomWrithe `σ−σ⁻¹` is bar-odd, Z-only,
  and is the *source* of the proton-excess (Z-dependent) correction the data
  demands — the ³He outlier (`≈ −1.4` q₀-units per excess proton). The
  mirror-pair splitter is the interface imbalance `Z−N`, and the p≠n
  asymmetry is seeded by the per-nucleon intra atomWrithe (proton `3` ≠ neutron
  `1`). See `delta_lambda_exponent_from_crossings.py` (`atomWrithe = 4Z`,
  `Z−N = (p-p ifaces) − (n-n ifaces)`).

  The bridge from the crossing count to the binding exponent — the per-site
  "5" (Bring-quintic degree) and per-nucleon "9" (intra-𝓑₃ count) reading —
  is OPEN and, per `docs/audits/2026-06-15-delta-lambda-q5-per-site-
  mechanism-start.md`, in EMPIRICAL TENSION: the literal q₀^{5(2A−1)}
  exponent overpredicts the measured B_sym/B_lin ratio by 3×→145× and the
  exponent that actually fits is ≈ 1.4 per site, not 5. It is therefore
  recorded below as a `conjecture` (sorry = conjecture, per AGENTS.md §3b),
  NOT a theorem, with the magnitude caveat in its docstring.

  Audit: docs/audits/2026-06-19-delta-lambda-exponent-keystone-formalize-first.md

  -- Ref: [leitner2026] appendix-mass-binding-algorithms, Step 9b (Δ_λ);
  --      docs/audits/2026-06-15-delta-lambda-q5-per-site-mechanism-start.md

  Imports: none — `omega` and `unfold` are core Lean 4 tactics, so this
  arithmetic-core file is self-contained and does not depend on Mathlib.
-/

namespace QOU.BraidKnot

/-- Positive (proton-walk) crossings in the atom braid word for `Z` protons,
`N` neutrons. Closed form from `atom_braid_word_3A`. -/
def protonCrossings (Z N : Nat) : Nat := 7 * Z + 5 * N - 1

/-- Negative (neutron-interface) crossings in the atom braid word. -/
def neutronCrossings (Z N : Nat) : Nat := 3 * Z + 5 * N - 1

/-- **Derived.** The proton and neutron crossing counts sum to `10A − 2`
(`A = Z + N`): the `Z`/`N` coefficients cancel, giving the slope of 10
crossings per nucleon. Requires at least one nucleon (`1 ≤ Z + N`) so the
truncated `ℕ` subtractions are exact. -/
theorem crossing_sum_cancels (Z N : Nat) (h : 1 ≤ Z + N) :
    protonCrossings Z N + neutronCrossings Z N = 10 * (Z + N) - 2 := by
  unfold protonCrossings neutronCrossings
  omega

/-- **Derived (pure arithmetic).** The per-site factorization: `10A − 5`
factors as `5·(2A − 1) = 5 × (A nucleon-sites + (A−1) bond-sites)`. This is
the arithmetic *shape* of the asserted per-site reading; it does not assert
that the binding exponent equals it. -/
theorem exponent_factorization (A : Nat) (h : 1 ≤ A) :
    5 * (2 * A - 1) = 10 * A - 5 := by
  omega

/-- The contested bridge claim, as a precise predicate (not asserted true):
the Δ_λ binding `q₀`-exponent for an isotope with `A` nucleons equals
`5·(2A − 1)` — i.e. exactly `5` per chain-site. Stated so the conjecture
below has a name; the truth value is open. -/
def perSiteFiveClaim (A bindingExponent : Nat) : Prop :=
  bindingExponent = 5 * (2 * A - 1)

/-- **Conditional restatement (proved; the conjectural content is the
hypothesis).** *If* the Δ_λ binding exponent equals `10A − 5`, then the
per-site-`5` claim `perSiteFiveClaim` holds — this direction is the pure
arithmetic factorization. The file asserts nothing about whether the
hypothesis `hexp` is true.

⚠ The hypothesis `hexp` (binding exponent = `10A − 5`, i.e. `5` per chain-
site) is exactly the OPEN, magnitude-contested claim — it is supplied here,
not proved. Two layers of doubt:
1. *Underived.* Why each chain-site contributes exactly `5` (the Bring
   quintic degree) is not derived from the jet order (Step 8) or the
   Gröbner–Shirshov normal form (Step 7); the crossing count merely asserts
   it.
2. *Empirically contested.* Per `2026-06-15-delta-lambda-q5-per-site-
   mechanism-start.md`, the literal `q₀^{5(2A−1)}` exponent overpredicts the
   measured `B_sym/B_lin` ratio by 3×→145×; the fitted exponent is ≈ 1.4 per
   site, consistent with an exp-vs-linear (Kashaev) correction, not a
   `q₀`-power.

The honest next step is to measure the per-site exponent from real compute
before chasing the complex-q mechanism for "why 5". Keeping the contested
claim as a *hypothesis* (rather than a `sorry`-conjecture asserting it) avoids
enshrining a refuted near-match while still recording the precise statement.

  -- Ref: [leitner2026] docs/audits/2026-06-19-delta-lambda-exponent-keystone-formalize-first.md
-/
theorem perSiteFive_of_exponent_eq (A bindingExponent : Nat) (h : 1 ≤ A)
    (hexp : bindingExponent = 10 * A - 5) :
    perSiteFiveClaim A bindingExponent := by
  unfold perSiteFiveClaim
  omega

/-! ## Z-dependent correction — the bar-antisymmetric companion

The leading exponent above lives in the bar-EVEN sum `σ+σ⁻¹` (A-only). The
binding data, however, shows a Z-dependent deviation from `q₀^{10A−5}` —
sharp on the proton-rich ³He (`≈ −1.4` q₀-exponent units) and slight on its
neutron-rich mirror T. That deviation is bar-ODD, so it cannot come from the
symmetric sum; it lives in the **atomWrithe** `σ−σ⁻¹`, derived below to be
proton-number-only (`4Z`). The coefficient (`≈ −1.4` / excess proton) is
*measured, not fitted* (Δ_λ gate): only the arithmetic skeleton is proved
here; the bridge to the coefficient is a named-but-unasserted predicate. -/

/-- Writhe (signed crossing total) of the atom braid word: `σ − σ⁻¹`. -/
-- Named `atomWrithe`, not `writhe` (bean `qou-u87j`). `QOU.BraidKnot.writhe`
-- in `AlphaShiftOneDimChannel` is the writhe of a BRAID WORD, `Word -> Int`,
-- summing a sign per letter. This one is the writhe of an ATOM, `Nat -> Nat -> Nat`,
-- from its proton and neutron crossing counts. Two different functions on two
-- different domains sharing one name, so the modules could never both be
-- imported. Nothing downstream used this one by name.
def atomWrithe (Z N : Nat) : Nat := protonCrossings Z N - neutronCrossings Z N

/-- **Derived.** The atomWrithe is `4Z`: the `A`/`N` content cancels, leaving
*proton number only*. This is the bar-ANTISYMMETRIC (q ↦ q⁻¹–odd) companion to
`crossing_sum_cancels`. The symmetric sum `σ+σ⁻¹ = 10A−2` is A-only and sets
the leading exponent `10A−5`; the antisymmetric atomWrithe `σ−σ⁻¹ = 4Z` is Z-only
and is the *source* of the proton-excess correction the data demands (³He). -/
theorem atomWrithe_eq_four_Z (Z N : Nat) (h : 1 ≤ Z + N) :
    atomWrithe Z N = 4 * Z := by
  unfold atomWrithe protonCrossings neutronCrossings
  omega

/-- Per-nucleon intra-𝓑₃ atomWrithe of a proton walk: `6σ − 3σ⁻¹ = 3`. -/
def protonIntraWrithe : Nat := 3

/-- Per-nucleon intra-𝓑₃ atomWrithe of a neutron walk: `5σ − 4σ⁻¹ = 1`. -/
def neutronIntraWrithe : Nat := 1

/-- **The p≠n seed (derived).** A proton and a neutron carry *different* intra
atomWrithe (`3 ≠ 1`): the proton walk is more positive-chirality. This inequality
is the structural origin of the asymmetric proton-excess penalty — why ³He
(one excess proton) is penalised sharply while its mirror T (one excess
neutron) is barely touched. -/
theorem proton_neutron_intra_writhe_asymmetry :
    protonIntraWrithe ≠ neutronIntraWrithe := by decide

/-- Total intra atomWrithe of the atom: the per-nucleon seeds summed, `3Z + N`. -/
def intraWrithe (Z N : Nat) : Nat := protonIntraWrithe * Z + neutronIntraWrithe * N

/-- The interface chirality imbalance `(Z−1) − (N−1)`: each `p-p` interface is a
`σ` (+1), each `n-n` a `σ⁻¹` (−1), the single `p-n` is bar-symmetric (0). Signed,
hence stated over `ℤ`. -/
def interfaceImbalance (Z N : Int) : Int := (Z - 1) - (N - 1)

/-- **Derived.** The interface imbalance equals `Z − N`. This is the
*mirror-pair splitter*: the only atomWrithe contribution that distinguishes ³He
(`Z−N = +1`) from the triton T (`Z−N = −1`) — the two share `σ+σ⁻¹ = 28`, hence
an identical leading exponent `25`, and differ only here. -/
theorem interfaceImbalance_eq_Z_sub_N (Z N : Int) :
    interfaceImbalance Z N = Z - N := by
  unfold interfaceImbalance; ring

/-- **Derived.** The atomWrithe splits as `intra (3Z+N) + interface (Z−N) = 4Z`,
reconciling `atomWrithe_eq_four_Z` with the per-nucleon seeds and the interface
imbalance. The intra term is the *defined* `intraWrithe` (cast to `ℤ`); the
interface term is signed, hence the identity lives over `ℤ`. -/
theorem atomWrithe_intra_interface_decomp (Z N : Nat) :
    (intraWrithe Z N : Int) + interfaceImbalance (Z : Int) (N : Int) = 4 * (Z : Int) := by
  unfold intraWrithe protonIntraWrithe neutronIntraWrithe interfaceImbalance
  push_cast
  ring

/-- **Conjectural bridge (NOT asserted).** The structural asymmetry the binding
data exhibits on mirror pairs: writing `δ` for the measured Δ_λ q₀-exponent
deviation indexed by the interface imbalance `Z−N`, the proton-rich member
(`Z−N = +k`, `k>0`) is penalised strictly more than its neutron-rich mirror
(`Z−N = −k`).

This is a content-bearing *conjecture predicate* — its truth is the OPEN claim,
deliberately NOT asserted (Δ_λ gate: the coefficient `≈ −1.4` per excess proton
is measured, never fitted into the closure). It is the honest Z-companion to
`perSiteFiveClaim`: derived arithmetic (`atomWrithe = 4Z`; the p≠n seed `3 ≠ 1`)
feeds a named-but-unproved bridge to the observable. Stated over any `Preorder`
so it makes no archimedean commitment beyond the order on the deviations.

  -- Ref: [leitner2026] docs/audits/2026-06-29-delta-lambda-z-correction-atomWrithe.md
-/
def ProtonExcessPenaltyAsymmetry {K : Type*} [Preorder K] (δ : Int → K) : Prop :=
  ∀ k : Int, 0 < k → δ k < δ (-k)

/-- **Conditional (proved; the asymmetry is the hypothesis).** *If* the
proton-excess penalty asymmetry holds, then proton-rich ³He (`Z−N = +1`) has a
strictly larger binding-exponent deficit than its mirror triton (`Z−N = −1`) —
the `−1.40` vs `−0.07` outlier pattern. Asserts nothing about whether the
hypothesis holds; only the structural consequence at `k = 1`. -/
theorem he3_penalised_more_than_triton {K : Type*} [Preorder K] {δ : Int → K}
    (h : ProtonExcessPenaltyAsymmetry δ) : δ 1 < δ (-1) :=
  h 1 (by decide)

/-! ### Mirror-pair cancellation — the bar-even baseline drops out

A mirror pair swaps `(Z, N) ↦ (N, Z)` (proton↔neutron counts) at fixed
`A = Z + N`. The bar-EVEN crossing statistics are `Z↔N`-symmetric (A-only), so
they are identical across a mirror pair; only the bar-ODD atomWrithe distinguishes
them. Hence any binding deviation that separates into an A-only baseline plus an
interface-imbalance term has the baseline cancel *exactly* in the mirror
difference — isolating the Z-correction. This is why the ³He/T (`−1.34`) and
⁷Be/⁷Li (`−1.77`) mirror splits are clean even though the absolute deviations
are large and A-dependent (and even though the leading `10A−5` law has collapsed
by A=7). See `delta_lambda_z_coefficient_and_slope.py`. -/

/-- **Derived.** The crossing sum is invariant under the mirror swap `Z ↔ N`
(it is A-only): the bar-even leading content is identical across a mirror pair. -/
theorem crossing_sum_mirror_invariant (Z N : Nat) (h : 1 ≤ Z + N) :
    protonCrossings Z N + neutronCrossings Z N
      = protonCrossings N Z + neutronCrossings N Z := by
  unfold protonCrossings neutronCrossings; omega

/-- **Derived.** The color-averaged count `2A + 1` is also mirror-invariant —
the second bar-even statistic is A-only too. -/
theorem averaged_count_mirror_invariant (Z N : Nat) :
    2 * (Z + N) + 1 = 2 * (N + Z) + 1 := by omega

/-- **Derived.** The atomWrithe is *not* mirror-invariant: it maps `4Z ↦ 4N`, and
the mirror difference is `4(Z − N)`. The atomWrithe is therefore the **unique**
crossing statistic that distinguishes a mirror pair — the entire mirror-pair
difference is carried by the bar-odd channel. -/
theorem atomWrithe_mirror_difference (Z N : Nat) (h : 1 ≤ Z + N) :
    (atomWrithe Z N : Int) - (atomWrithe N Z : Int) = 4 * ((Z : Int) - (N : Int)) := by
  have hZ : atomWrithe Z N = 4 * Z := atomWrithe_eq_four_Z Z N h
  have hN : atomWrithe N Z = 4 * N := atomWrithe_eq_four_Z N Z (by omega)
  rw [hZ, hN]; push_cast; ring

/-- **The mirror cancellation (proved; the separation is the hypothesis).** Model
the Δ_λ deviation as `f Z N = baseline (Z+N) + zCorr (Z − N)` — an A-only
baseline plus a term in the interface imbalance `Z − N`, the additive form
justified by the mirror-invariance of the two bar-even statistics above. Then
the mirror-pair difference cancels the baseline **exactly** (since
`Z + N = N + Z`) and equals `zCorr (Z−N) − zCorr (N−Z)`: the observable mirror
split is the bar-odd Z-correction alone, independent of the (A-dependent,
collapsing) baseline.

The cancellation given the additive form is *unconditional*; the separation
hypothesis `hf` itself is the additive-channel ansatz (supplied, not proved —
the data confirms it but the corpus gates fitting its magnitude). -/
theorem mirror_baseline_cancels {K : Type*} [AddCommGroup K]
    (baseline : Nat → K) (zCorr : Int → K) (f : Nat → Nat → K)
    (hf : ∀ a b : Nat, f a b = baseline (a + b) + zCorr ((a : Int) - (b : Int)))
    (Z N : Nat) :
    f Z N - f N Z = zCorr ((Z : Int) - N) - zCorr ((N : Int) - Z) := by
  rw [hf Z N, hf N Z, Nat.add_comm N Z]
  abel

end QOU.BraidKnot
