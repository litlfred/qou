import QOU.Mass.DiprotonResponseClosedForm

/-!
# A γγ vertex at a two-nucleon interface must borrow, and a borrowed vertex cannot carry
# the two-body isospin pattern

Bean `qou-ales`, step 11. Steps 6–10 computed the interface bond's trace response at one
placement, `V1 = σ₂σ₃⁻¹`, and read its sign as "the γγ-selected diproton is unbound". This
file isolates the two structural facts that narrow that reading, and both are about **arity**,
not about magnitude or sign.

## The geometry

Two nucleons sit on generator sets `{0,1}` and `{3,4}` — strands 1–3 and 4–6 of `H₆` — so the
interface is the single generator `2`. A γγ vertex is a product `σ_g σ_{g+1}⁻¹`: it occupies
**two adjacent generators**. Since `{2}` is a single generator and an adjacent pair has two
distinct elements, **no vertex can sit on the interface alone** (`no_vertex_on_interface_alone`).
A vertex that touches the interface is therefore `{1,2}` or `{2,3}`, and:

* `{1,2}` borrows generator `1` from the **left** nucleon;
* `{2,3}` borrows generator `3` from the **right** nucleon.

`interfaceVertex_borrows_exactly_one_side` proves both together: a straddling vertex meets
exactly one of the two nucleon supports, never both and never neither. So **every placement
breaks the left–right symmetry of the pair by construction** — there is no symmetric choice to
prefer, and the arc's `shift 2` (step 6) picks one of the two without deriving it.

## The arity obstruction

Measured in `two_nucleon_bond_response_arity_probe` (exactly over `ℚ(q)`, deviations `0` rather
than tolerances), over all **four** interface vertices × all four ordered channels: **every
vertex's response is one-body, in the slot it borrows from.** `V1` and `V2` borrow right and
satisfy `r_pp = r_np`, `r_nn = r_pn`; `V3` and `V4` borrow left and satisfy `r_pp = r_pn`,
`r_nn = r_np`. So the obstruction below is not a defect of the canonical placement — it holds
at every placement and both orientations.

Note which comparisons decide this. `r_pn ≠ r_np` discriminates **nothing**: if `f a b = g b`
then `r_pn = g n` and `r_np = g p`, which *should* differ. Only the **like-pair** comparisons
test arity, and an earlier version of the probe omitted them off `V2`–`V4` and so could not
have decided the question it was built for.

That measured one-body property is exactly the hypothesis of
`no_signMixed_of_rightDependent` below, and the conclusion is that such a response can **never**
carry the two-body pattern bean `qou-q8vl` requires:

    the unlike pair binds while both like pairs do not,

i.e. `f p n` of opposite sign to both `f p p` and `f n n`. If `f a b = g b` then
`f p n = f n n` **identically**, so the two cannot differ in sign — the product of a real with
itself is non-negative. The same holds for a left-dependent response by the mirror argument
(`no_signMixed_of_leftDependent`), hence for **either** placement
(`no_signMixed_of_oneBody`).

This is a stronger objection than a sign objection. A sign objection says the numbers come out
the wrong way round and invites looking for a letter that fixes them. This says the functional
form cannot express the distinction at all, whatever the letters are, for as long as the
response depends on one nucleon.

## Scope — (a), not (b), and what the corpus already said

`placement_sign_not_determined_by_channel` records the second measured fact: on the **same**
channel, `V1` gives a trace ratio above one (unbound) and `V3` gives one below (bound), so the
binding *sign* is not a function of the channel. Measured: the discriminator is **which of the
vertex's two letters carries the inverse** — inverse on the borrowed letter (`V1`, `V4`)
unbinds, inverse on the interface letter (`V2`, `V3`) binds, 4/4 — and **not** which side is
borrowed, which sets only the magnitude.

**Do not restate that as "`σ₂` versus `σ₂⁻¹` flips the binding".** That is false and contradicts
`QOU.QBeta.SingleCrossingAlwaysBinds.interface_mem_Ioo` (sorry-free), which proves the
single-crossing family `μ = z + d`, `d ∈ [−h, 0]`, lies wholly in `(0,1)` — both orientations
bind. Nor is `V2` that substitution: `σ₂ → σ₂⁻¹` in `σ₂σ₃⁻¹` gives `σ₂⁻¹σ₃⁻¹`, not a γγ word
at all. `V2 = V1⁻¹` is the **group inverse** (reverse *and* invert), a third map distinct from
both the bar involution and the isospin `ℤ/2` swap — two of which the corpus has already had to
retract a conflation of. The rows are consistent with `interface_mem_Ioo` only because a γγ word
has length 6, which step 8 established.

**The placement being underived is the corpus's own position, not a new finding here.**
`docs/coordination/2026-05-24-low-isotope-mass-anatomy-ledger.md` records the `pp ↦ σ`,
`nn ↦ σ⁻¹`, `pn ↦ σ_avg` rule as *asserted without a `prop:` block*, a Rule-14 escalation
candidate, since 2026-05-24; `brings-surface/inter-nucleon-channel-color-tube.md` carries a live
conjectural derivation route for it. Because that route exists, this stays **scope-(a)** —
"this construction, at these placements, against these words" — and excludes no ingredient.

What *is* structural is the implication below: a one-body response cannot carry the isospin
pattern. The **premise** (one-body) is measured at four vertices against the canonical words;
promoting the whole to scope-(b) would need a proof that `tr_M(W·G^k)` always factorises over
the strand split, which is the open question this file hands forward.

## What is NOT affected

`DiprotonResponseClosedForm` is untouched. Its closed form, its `Θ(h⁴)` bracket and its
`α/100` ceiling are correct statements about the word they are about. The narrowing is to the
*interpretation* of `r` as a pair quantity.
-/

namespace QOU.Mass.InterfaceVertexArity

/-! ## Generator geometry of the two-nucleon interface -/

/-- The generator support of the left nucleon in `H₆`: `{0, 1}`. -/
def leftSupport : Finset ℕ := {0, 1}

/-- The generator support of the right nucleon in `H₆`: `{3, 4}`. -/
def rightSupport : Finset ℕ := {3, 4}

/-- The interface generator, the one belonging to neither nucleon. -/
def interfaceGen : ℕ := 2

/-- The generator pair a γγ vertex `σ_g σ_{g+1}⁻¹` occupies. -/
def vertexSupport (g : ℕ) : Finset ℕ := {g, g + 1}

/-- A vertex **straddles** the interface when its support contains the interface generator. -/
def Straddles (g : ℕ) : Prop := interfaceGen ∈ vertexSupport g

/-- The two nucleon supports are disjoint, and neither contains the interface generator. -/
theorem supports_disjoint_and_miss_interface :
    Disjoint leftSupport rightSupport ∧ interfaceGen ∉ leftSupport ∧
      interfaceGen ∉ rightSupport := by
  refine ⟨?_, ?_, ?_⟩ <;> decide

/-- **A vertex support is never the interface alone.** It has two distinct elements, so it
cannot equal the singleton `{2}` — there is no symmetric placement to prefer. -/
theorem no_vertex_on_interface_alone (g : ℕ) : vertexSupport g ≠ {interfaceGen} := by
  intro h
  have hg : g ∈ vertexSupport g := by simp [vertexSupport]
  have hg1 : g + 1 ∈ vertexSupport g := by simp [vertexSupport]
  rw [h] at hg hg1
  simp only [Finset.mem_singleton] at hg hg1
  omega

/-- **Exactly two placements straddle the interface**, `g = 1` and `g = 2`. -/
theorem straddles_iff (g : ℕ) : Straddles g ↔ g = 1 ∨ g = 2 := by
  unfold Straddles vertexSupport interfaceGen
  simp only [Finset.mem_insert, Finset.mem_singleton]
  omega

/-- **A straddling vertex borrows from exactly one nucleon.** `g = 1` meets the left support
and misses the right; `g = 2` meets the right and misses the left. Never both, never neither —
so every placement breaks the pair's left–right symmetry. -/
theorem interfaceVertex_borrows_exactly_one_side {g : ℕ} (hg : Straddles g) :
    ((vertexSupport g ∩ leftSupport).Nonempty ∧ vertexSupport g ∩ rightSupport = ∅) ∨
      (vertexSupport g ∩ leftSupport = ∅ ∧ (vertexSupport g ∩ rightSupport).Nonempty) := by
  rcases (straddles_iff g).mp hg with h | h <;> subst h
  · left; exact ⟨⟨1, by decide⟩, by decide⟩
  · right; exact ⟨by decide, ⟨3, by decide⟩⟩

/-! ## The arity obstruction on the two-body pattern -/

/-- A nucleon species. -/
inductive Nucleon
  | p
  | n
  deriving DecidableEq

/-- **The two-body isospin pattern** bean `qou-q8vl` requires of a pair functional: the unlike
pair sits on the opposite side of zero from **both** like pairs. Stated on products so it is
sign-agnostic — it says "opposite sign", not "positive" or "negative". -/
def SignMixed (f : Nucleon → Nucleon → ℝ) : Prop :=
  f .p .n * f .p .p < 0 ∧ f .p .n * f .n .n < 0

/-- **A response that depends only on its RIGHT argument cannot be sign-mixed.** This is the
measured situation at `V1` **and `V2`**: `r_pp = r_np` and `r_nn = r_pn`, so `r` is `g` of the
borrowed (right) nucleon. Then `f p n = g n = f n n`, and a real times itself is never
negative. -/
theorem no_signMixed_of_rightDependent {f : Nucleon → Nucleon → ℝ} {g : Nucleon → ℝ}
    (h : ∀ a b, f a b = g b) : ¬ SignMixed f := by
  rintro ⟨-, h2⟩
  rw [h .p .n, h .n .n] at h2
  nlinarith [sq_nonneg (g Nucleon.n)]

/-- **The mirror**: a response depending only on its LEFT argument cannot be sign-mixed
either, via `f p n = g p = f p p`. This is the measured situation at `V3` and `V4`, which
borrow from the left. -/
theorem no_signMixed_of_leftDependent {f : Nucleon → Nucleon → ℝ} {g : Nucleon → ℝ}
    (h : ∀ a b, f a b = g a) : ¬ SignMixed f := by
  rintro ⟨h1, -⟩
  rw [h .p .n, h .p .p] at h1
  nlinarith [sq_nonneg (g Nucleon.p)]

/-- **Either way, and this is the headline.** Every interface placement borrows from exactly
one side (`interfaceVertex_borrows_exactly_one_side`), and the response is measured to be a
function of that borrowed nucleon alone at **all four** vertices. So no placement of a γγ
vertex at this interface — either position, either orientation — can carry the two-body isospin
pattern. The obstruction is the *arity* of the response, not the sign of any number. -/
theorem no_signMixed_of_oneBody {f : Nucleon → Nucleon → ℝ}
    (h : (∃ g : Nucleon → ℝ, ∀ a b, f a b = g b) ∨ (∃ g : Nucleon → ℝ, ∀ a b, f a b = g a)) :
    ¬ SignMixed f := by
  rcases h with ⟨g, hg⟩ | ⟨g, hg⟩
  · exact no_signMixed_of_rightDependent hg
  · exact no_signMixed_of_leftDependent hg

/-- **The contrapositive, as the positive statement of what a closure needs**: any pair
functional realising the isospin pattern is genuinely two-body — it depends on both arguments.
This is what step 11 hands forward as the requirement, rather than a refutation. -/
theorem signMixed_is_genuinely_two_body {f : Nucleon → Nucleon → ℝ} (hs : SignMixed f) :
    (¬ ∃ g : Nucleon → ℝ, ∀ a b, f a b = g b) ∧ (¬ ∃ g : Nucleon → ℝ, ∀ a b, f a b = g a) := by
  constructor
  · intro h
    exact no_signMixed_of_oneBody (Or.inl h) hs
  · intro h
    exact no_signMixed_of_oneBody (Or.inr h) hs

/-! ## The placement record: the sign is not a function of the channel -/

/-- **The measured placement fact, carried as a hypothesis.** `ratioV1` and `ratioV3` are the
`H₆` convention-D trace ratios of the *same* two-nucleon channel under the two straddling
placements. The probe measures `1.00105775…` and `0.98669973…` at the proton pin; here only
their position relative to `1` is used. Verified by the probe, not proved in Lean — the same
epistemic position as `DiprotonResponseClosedForm.ResponseClosedForm`. -/
structure PlacementSigns (ratioV1 ratioV3 : ℝ) : Prop where
  /-- The right-borrowing placement raises the trace: the channel comes out unbound. -/
  v1_above_one : 1 < ratioV1
  /-- The left-borrowing placement lowers it: the same channel comes out bound. -/
  v3_below_one : ratioV3 < 1

/-- **The sign of the binding is not determined by the channel.** Given the measured
placement fact, the two ratios for one channel straddle `1`, so no function of the channel
alone fixes the sign of `B = −α·log(ratio)`. The sign is a function of the *placement*, and
the placement is not derived anywhere in the arc. This is the scope-(a) record: it narrows the
reading of steps 8–10, and excludes no ingredient. -/
theorem placement_sign_not_determined_by_channel {α ratioV1 ratioV3 : ℝ} (hα : 0 < α)
    (h : PlacementSigns ratioV1 ratioV3) (h3 : 0 < ratioV3) :
    -α * Real.log ratioV1 < 0 ∧ 0 < -α * Real.log ratioV3 := by
  refine ⟨?_, ?_⟩
  · have hlog : 0 < Real.log ratioV1 := Real.log_pos h.v1_above_one
    nlinarith
  · have hlog : Real.log ratioV3 < 0 := Real.log_neg h3 h.v3_below_one
    nlinarith

/-! ## Why the SELECTION survives the orientation swap and the BINDING does not -/

section Orientation

variable {R : Type*} [CommRing R]

/-- **The Cayley–Hamilton inverse of a `2×2` matrix of determinant one has the SAME trace.**
For `M : Matrix (Fin 2) (Fin 2) R`, Cayley–Hamilton reads `M² − (tr M)·M + (det M)·1 = 0`, so
when `det M = 1` the matrix `N = (tr M)·1 − M` satisfies `M·N = 1`. Its trace is
`2·tr M − tr M = tr M`. Step 4 proves `det V = 1` for the Hoefsmit `(2,1)` vertex image, so
this applies to every vertex power. -/
theorem trace_cayleyInverse (M : Matrix (Fin 2) (Fin 2) R) :
    ((M.trace) • (1 : Matrix (Fin 2) (Fin 2) R) - M).trace = M.trace := by
  simp [Matrix.trace_sub, Matrix.trace_smul, Matrix.trace_one]
  ring

/-- **But a MIXED trace is not protected, and that is a theorem, not a measurement.** There
exist `W`, `M`, `N` over `ℝ` with `M·N = 1` and `tr N = tr M` — so no character can tell `M`
from `N` — while `tr(W·M) ≠ tr(W·N)`. Exhibited concretely:
`W = !![1,0;0,0]`, `M = !![2,1;1,1]`, `N = !![1,-1;-1,2]`, giving traces `2` against `1`.

That is exactly the `H₆` situation. The interface bond's own character cannot see the
orientation swap (`trace_cayleyInverse`), but `tr_M(W·G³)` is a **mixed** trace against the
nucleon word `W`, so nothing protects it — and the step-11 probe measures it flipping the
binding sign across the swap. The selection and the binding are guarded by different things,
and only one of them is guarded. -/
theorem mixed_trace_not_inverse_invariant :
    ∃ (W M N : Matrix (Fin 2) (Fin 2) ℝ),
      M * N = 1 ∧ N.trace = M.trace ∧ (W * M).trace ≠ (W * N).trace := by
  refine ⟨!![1, 0; 0, 0], !![2, 1; 1, 1], !![1, -1; -1, 2], ?_, ?_, ?_⟩
  · rw [Matrix.one_fin_two]
    norm_num [Matrix.mul_fin_two]
  · norm_num [Matrix.trace_fin_two]
  · norm_num [Matrix.mul_fin_two, Matrix.trace_fin_two]

end Orientation

end QOU.Mass.InterfaceVertexArity
