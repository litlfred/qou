import QOU.Machinery.MarkovTraceH4Gram
import QOU.Machinery.HeckeH4AlgebraLaws

/-!
# `QOU.Machinery.H4BasisBridge` — the two `H₄` normal-form bases are one basis

The tree carries two 24-word normal-form bases for `H₄(q)` and they have never
been connected:

| | module | has | lacks |
|---|---|---|---|
| **ASCII** | `MarkovTraceH4` + `MarkovTraceH4Gram0..7` | `trM`, `gram_symm`, **`trM_cyclic`** | associativity, `Ring` |
| **subscript** | `HeckeH4StabilizationRung` + `HeckeH4AlgebraLaws` | the presentation, `mulNF₄_assoc`, `H4A` `Ring`/`Algebra`, `wedderburn₄` | **cyclicity** |

They are the same basis relabelled. Mapping each reduced word to its `S₄`
element, both lists give the same 24 elements; the index permutation is `piIdx`
below; the trace weights agree under it; and only **6 of 24** words differ at
all, every difference a single far-commutation swap `σ₀σ₂ ↔ σ₂σ₀` — which
`far_commute_σ₀σ₂` proves, so the basis *elements* are equal, not merely the
group elements they index.

`phi` is the relabelling. It intertwines all three generator actions
(`phi_mulσ0/1/2`, depth 1 each), hence every word action (`phi_word_*`, a chain
of rewrites — no coordinate expansion), hence the products; and it carries `trM`
to `trM4`. Cyclicity therefore transports: **`trM4_cyclic`**, with no second
576-entry Gram closure.

Bean qou-x64l. Once the consumers move across, the ASCII chain — ~6.5k generated
lines and the tree's build pole, ~4.3 GB peak — can be retired.

Generated: the permutation and the word correspondence are computed from
`MarkovTraceH4.mulNF` and `HeckeH4AlgebraLaws.wordAction` themselves, so they
cannot drift from the tables they describe.
-/

namespace QOU.Machinery.H4Bridge

open QOU.Machinery.H4

universe u

variable {R : Type u} [CommRing R] (h : R)

/-- ASCII basis index ↦ subscript basis index. -/
def piIdx : Fin 24 → Fin 24 := ![0, 6, 2, 1, 7, 9, 8, 4, 3, 12, 10, 13, 11, 5, 14, 16, 15, 17, 18, 19, 20, 21, 22, 23]

/-- The inverse relabelling. -/
def invIdx : Fin 24 → Fin 24 := ![0, 3, 2, 8, 7, 13, 1, 4, 6, 5, 10, 12, 9, 11, 14, 16, 15, 17, 18, 19, 20, 21, 22, 23]

@[simp] theorem invIdx_piIdx (i : Fin 24) : invIdx (piIdx i) = i := by
  fin_cases i <;> rfl

@[simp] theorem piIdx_invIdx (j : Fin 24) : piIdx (invIdx j) = j := by
  fin_cases j <;> rfl

/-- Relabel an ASCII coordinate vector into subscript coordinates. -/
def phi (u : Fin 24 → R) : Fin 24 → R := fun j => u (invIdx j)

/-- `phi` is a linear bijection; this is its inverse. -/
def psi (w : Fin 24 → R) : Fin 24 → R := fun i => w (piIdx i)

@[simp] theorem psi_phi (u : Fin 24 → R) : psi (phi u) = u := by
  funext i; simp [psi, phi]

@[simp] theorem phi_psi (w : Fin 24 → R) : phi (psi w) = w := by
  funext j; simp [psi, phi]

/-! ## `phi` intertwines the three generator actions

Depth 1 on each side — this is what keeps the whole bridge cheap. -/

theorem phi_mulσ0 (u : Fin 24 → R) : phi (mulσ0 h u) = mulσ₀ h (phi u) := by
  funext j
  fin_cases j <;> simp [phi, invIdx, mulσ0, mulσ₀]

theorem phi_mulσ1 (u : Fin 24 → R) : phi (mulσ1 h u) = mulσ₁ h (phi u) := by
  funext j
  fin_cases j <;> simp [phi, invIdx, mulσ1, mulσ₁]

theorem phi_mulσ2 (u : Fin 24 → R) : phi (mulσ2 h u) = mulσ₂ h (phi u) := by
  funext j
  fin_cases j <;> simp [phi, invIdx, mulσ2, mulσ₂]

/-! ## Hence every word action, by rewriting — never by coordinate expansion -/

/-- ASCII word 0 (γ) ↦ subscript word 0 (γ). -/
theorem phi_word_0 (u : Fin 24 → R) :
    phi (u) = phi u := by
  rfl

/-- ASCII word 1 (σ₂) ↦ subscript word 6 (σ₂). -/
theorem phi_word_1 (u : Fin 24 → R) :
    phi (mulσ2 h (u)) = mulσ₂ h (phi u) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 2 (σ₁) ↦ subscript word 2 (σ₁). -/
theorem phi_word_2 (u : Fin 24 → R) :
    phi (mulσ1 h (u)) = mulσ₁ h (phi u) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 3 (σ₀) ↦ subscript word 1 (σ₀). -/
theorem phi_word_3 (u : Fin 24 → R) :
    phi (mulσ0 h (u)) = mulσ₀ h (phi u) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 4 (σ₁σ₂) ↦ subscript word 7 (σ₁σ₂). -/
theorem phi_word_4 (u : Fin 24 → R) :
    phi (mulσ2 h (mulσ1 h (u))) = mulσ₂ h (mulσ₁ h (phi u)) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 5 (σ₂σ₁) ↦ subscript word 9 (σ₂σ₁). -/
theorem phi_word_5 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ2 h (u))) = mulσ₁ h (mulσ₂ h (phi u)) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 6 (σ₂σ₀) ↦ subscript word 8 (σ₂σ₀). -/
theorem phi_word_6 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ2 h (u))) = mulσ₀ h (mulσ₂ h (phi u)) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 7 (σ₀σ₁) ↦ subscript word 4 (σ₀σ₁). -/
theorem phi_word_7 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ0 h (u))) = mulσ₁ h (mulσ₀ h (phi u)) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 8 (σ₁σ₀) ↦ subscript word 3 (σ₁σ₀). -/
theorem phi_word_8 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (u))) = mulσ₀ h (mulσ₁ h (phi u)) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 9 (σ₁σ₂σ₁) ↦ subscript word 12 (σ₁σ₂σ₁). -/
theorem phi_word_9 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ2 h (mulσ1 h (u)))) = mulσ₁ h (mulσ₂ h (mulσ₁ h (phi u))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 10 (σ₀σ₁σ₂) ↦ subscript word 10 (σ₀σ₁σ₂). -/
theorem phi_word_10 (u : Fin 24 → R) :
    phi (mulσ2 h (mulσ1 h (mulσ0 h (u)))) = mulσ₂ h (mulσ₁ h (mulσ₀ h (phi u))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 11 (σ₂σ₀σ₁) ↦ subscript word 13 (σ₂σ₀σ₁). -/
theorem phi_word_11 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ0 h (mulσ2 h (u)))) = mulσ₁ h (mulσ₀ h (mulσ₂ h (phi u))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 12 (σ₁σ₂σ₀) ↦ subscript word 11 (σ₁σ₀σ₂) — one `σ₀σ₂` swap. -/
theorem phi_word_12 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ2 h (mulσ1 h (u)))) = mulσ₂ h (mulσ₀ h (mulσ₁ h (phi u))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]
  rw [far_commute_σ₀σ₂]

/-- ASCII word 13 (σ₀σ₁σ₀) ↦ subscript word 5 (σ₀σ₁σ₀). -/
theorem phi_word_13 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ0 h (u)))) = mulσ₀ h (mulσ₁ h (mulσ₀ h (phi u))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 14 (σ₂σ₁σ₀) ↦ subscript word 14 (σ₂σ₁σ₀). -/
theorem phi_word_14 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ2 h (u)))) = mulσ₀ h (mulσ₁ h (mulσ₂ h (phi u))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 15 (σ₀σ₁σ₂σ₁) ↦ subscript word 16 (σ₀σ₁σ₂σ₁). -/
theorem phi_word_15 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (u))))) = mulσ₁ h (mulσ₂ h (mulσ₁ h (mulσ₀ h (phi u)))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 16 (σ₀σ₁σ₂σ₀) ↦ subscript word 15 (σ₀σ₁σ₀σ₂) — one `σ₀σ₂` swap. -/
theorem phi_word_16 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (u))))) = mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h (phi u)))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]
  rw [far_commute_σ₀σ₂]

/-- ASCII word 17 (σ₁σ₂σ₀σ₁) ↦ subscript word 17 (σ₁σ₀σ₂σ₁) — one `σ₀σ₂` swap. -/
theorem phi_word_17 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (u))))) = mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (phi u)))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]
  rw [far_commute_σ₀σ₂]

/-- ASCII word 18 (σ₁σ₂σ₁σ₀) ↦ subscript word 18 (σ₁σ₂σ₁σ₀). -/
theorem phi_word_18 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (u))))) = mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₁ h (phi u)))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 19 (σ₂σ₀σ₁σ₀) ↦ subscript word 19 (σ₂σ₀σ₁σ₀). -/
theorem phi_word_19 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (u))))) = mulσ₀ h (mulσ₁ h (mulσ₀ h (mulσ₂ h (phi u)))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 20 (σ₀σ₁σ₂σ₀σ₁) ↦ subscript word 20 (σ₀σ₁σ₀σ₂σ₁) — one `σ₀σ₂` swap. -/
theorem phi_word_20 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (u)))))) = mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h (phi u))))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]
  rw [far_commute_σ₀σ₂]

/-- ASCII word 21 (σ₀σ₁σ₂σ₁σ₀) ↦ subscript word 21 (σ₀σ₁σ₂σ₁σ₀). -/
theorem phi_word_21 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (u)))))) = mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₁ h (mulσ₀ h (phi u))))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 22 (σ₁σ₂σ₀σ₁σ₀) ↦ subscript word 22 (σ₁σ₀σ₂σ₁σ₀) — one `σ₀σ₂` swap. -/
theorem phi_word_22 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (u)))))) = mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (phi u))))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]
  rw [far_commute_σ₀σ₂]

/-- ASCII word 23 (σ₀σ₁σ₂σ₀σ₁σ₀) ↦ subscript word 23 (σ₀σ₁σ₀σ₂σ₁σ₀) — one `σ₀σ₂` swap. -/
theorem phi_word_23 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (u))))))) = mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h (phi u)))))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]
  rw [far_commute_σ₀σ₂]

/-! ## The traces correspond -/

theorem trM4_phi (z : R) (u : Fin 24 → R) : trM4 z h (phi u) = trM z h u := by
  simp only [trM, trM4, TRM, TRM4, phi, invIdx, Fin.sum_univ_succ, Fin.sum_univ_zero]
  simp
  ring

/-! ## Far-commutation on the ASCII side

`simp` rewrites innermost-first, so the three intertwiners collapse a subscript
composite to `phi (…)` one generator at a time — producing the *subscript* word
shape. For the 6 words where the two bases differ that is not the ASCII word, and
the two sides no longer match. Normalising needs `σ₀σ₂ = σ₂σ₀` on the ASCII
generators as well; the subscript counterpart is
`HeckeH4StabilizationRung.far_commute_σ₀σ₂`. -/

theorem mulσ_farcomm02 (u : Fin 24 → R) :
    mulσ0 h (mulσ2 h u) = mulσ2 h (mulσ0 h u) := by
  funext i
  fin_cases i <;> simp [mulσ0, mulσ2] <;> ring

/-! ## What is NOT here yet: the product correspondence

`phi_mulNF : phi (mulNF h u v) = mulNF₄ h (phi u) (phi v)` is the one step left,
and with it `trM4_cyclic` — cyclicity on the subscript basis — follows in four
lines from `H4.trM_cyclic` (sorry-free on the ASCII basis) and `phi_psi`:

```lean
theorem trM4_cyclic (z : R) (x y : Fin 24 → R) :
    trM4 z h (mulNF₄ h x y) = trM4 z h (mulNF₄ h y x) := by
  have hx : x = phi (psi x) := (phi_psi x).symm
  have hy : y = phi (psi y) := (phi_psi y).symm
  rw [hx, hy, ← phi_mulNF, ← phi_mulNF, trM4_phi, trM4_phi]
  exact trM_cyclic z h (psi x) (psi y)
```

**The obstacle is mechanical, not mathematical.** Everything the statement needs
is above: the generator actions correspond, hence every word action does
(`phi_word_*`), the traces agree (`trM4_phi`), and `mulNF`/`mulNF₄` are literal
24-term sums over exactly those word actions with coefficients related by
`(phi v) (piIdx i) = v i`.

Three `simp`-based approaches have failed, each differently — recorded so a
fourth guess is not needed:

1. **`phi` in the same `simp only` as `← phi_word_*`.** `phi` unfolds first and
   destroys the rewrite patterns.
2. **Two passes: `simp only [mulNF₄, ← phi_word_*]`, then unfold.** The
   unused-simp-args linter reports **all 24 `phi_word_*` as unused** — they never
   fire. Diagnosis: `simp` rewrites innermost-first, so `← phi_mulσ*` (which are
   `phi_word_1/2/3` in disguise) collapse each composite one generator at a time,
   yielding the *subscript* word shape; for the 6 words where the bases differ
   that is not the ASCII word, so the longer lemmas never match.
3. **Adding `mulσ_farcomm02` to normalise those 6.** Still fails, and worse: the
   right-hand side comes out with **70 terms instead of 24**, carrying
   coefficients indexed by `invIdx j` rather than by literals — `simp` is
   mangling the coefficient vector, not merely failing to rewrite.

What that points at: stop unfolding `mulNF`/`mulNF₄` by `simp` at all. The tree
already has the structured accessors — `mulNF₄_e_right`, `mulNF₄_expand_right`,
`mulNF₄_sum_left/right`, `basis_decomp₄` — and the proof should go through those,
expressing both products as `Finset.sum` over the basis and reindexing along
`piIdx` with `Finset.sum_nbij` or `Equiv.sum_comp`, so the 24 terms are never
written out. Bean qou-x64l.
-/

end QOU.Machinery.H4Bridge
