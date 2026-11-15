/-
QOU.Mass.FreedmanHeGenusHandleNeedsVanishingLinking — the complement-genus lower
bound on `ac(L_k, L)` is stated **for Borromean links**, and the derived carrier
is the opposite of Borromean: every one of its components is linked.

Arc context (carrier derivation; beans `qou-768r`, `qou-o6ml`). The Freedman–He
link bound as Komendarczyk states it (arXiv:0808.1533v1 eq. (43), p. 26; held at
`library/arxiv-0808.1533v1/sections/sec-005-energy-bound.md:203-216`) is

  `E_{3/2}(X) ≥ (π/16)^{1/4} · (Σ_k ac(L_k, L)|Flux(X_k)|) · min_k |Flux(X_k)|`

`ac(L_k, L)` is an **infimum over homotopies** and so is not directly computable.
The corpus's route to a number has been the sentence immediately after (line 217),
which bounds it below by *"a smallest genus among surfaces in
`ℝ³ ∖ {L₁ ∪ … ∪ L̂_k ∪ … ∪ L_n}` with a single boundary component"*.

**That sentence opens "the asymptotic crossing numbers `ac(L_k, L)` FOR BORROMEAN
LINKS can be estimated below by …", and the qualifier is load-bearing.** The
corpus's record of it — `qou-a9li` and `qou-b5yi`, both `completed` 2026-09-02 —
quotes the genus clause without the qualifier, and this file's author repeated the
elision earlier in the same session that produced it.

**Why the qualifier must be there, homologically.** A compact oriented surface
`S ⊆ ℝ³ ∖ L_j` with `∂S = L_k` forces `lk(L_k, L_j) = 0`, since `[L_k] = [∂S] = 0`
in `H₁(ℝ³ ∖ L_j) ≅ ℤ` and that class *is* the linking number. So when some
`lk(L_k, L_j) ≠ 0` the surfaces being minimised over **do not exist**: the estimate
is not weaker off the Brunnian class, it is ill-posed there (an infimum over ∅).

**What this file proves.** The measured shape of the derived carrier — the closure
of the canonical atom braid word — is a **path**: `μ = A + 1` components with
exactly the consecutive pairs linked (`lk(i, i+1) = ±2`, measured on ²H, ³H, ³He,
⁴He, ⁶Li, ⁸Be, ¹²C in both crossing-resolution branches). On any such path with at
least two components, **no component has all its linking numbers vanishing**
(`no_component_is_brunnian`) — including the two endpoints, which is the case an
"every vertex has a successor" argument would miss.

Hence the genus handle is available at **no** component of the derived carrier, and
the only carrier in this arc on which it *is* available is the Borromean L6a4 — the
census assignment that owner ruling 2026-08-29 retired as a fit.

SCOPE — **scope-(b)**, and the invariant is cited: the homology of the complement,
via `∂S = L_k ⇒ lk(L_k, L_j) = 0`. This excludes *the complement-genus route to a
number for `ac`* on this carrier. It does **not** refute eq. (43), which remains a
true lower bound, and it does **not** show `ac(L_k, L)` is small or zero — `ac` is
untouched here; only this particular handle on it is.

**Deliberately not formalised.** The homological step itself. Seifert surfaces and
`H₁` of a link complement are not cheaply available in this Mathlib, and asserting
them as a `class` would be the axiomatisation-is-not-a-proof pattern. It is carried
here as the *stated reason* for the source's qualifier, and what is machine-checked
is the combinatorial half — that the measured carrier fails the hypothesis at every
component. The two halves are kept separate on purpose.

Base ring: `ℤ`, genuinely — linking numbers are integers, and the content is that
certain ones are nonzero. No ordering and no ring generality is used, so per
AGENTS.md §7c neither is assumed.
-/
import Mathlib.Data.Fin.Basic
import Mathlib.Order.Basic

namespace QOU.Mass.FreedmanHeGenusHandleNeedsVanishingLinking

variable {ι : Type*}

/-- **The hypothesis the genus handle needs at component `k`**: every pairwise
linking number of `k` with the other components vanishes.

This is the Brunnian condition localised at one component, and it is exactly what
makes a surface bounded by `L_k` in the complement of the rest exist at all.

**TIER 3.**  It is the pointwise form of `MilnorIndeterminacyGate`'s tier-2
condition — `BrunnianTierDisambiguation.linkingVanishes_iff_forall_at` proves the
two agree on a symmetric three-component matrix — and, like it, is strictly
weaker than true Brunnian-ness.  Tier table for the four things this corpus calls `Brunnian`, and which implications hold: `QOU.Mass.BrunnianTierDisambiguation`. -/
def BrunnianAt (lk : ι → ι → ℤ) (k : ι) : Prop := ∀ j, j ≠ k → lk k j = 0

/-- One linked partner is enough to destroy the hypothesis. -/
theorem not_brunnianAt_of_linked (lk : ι → ι → ℤ) (k j : ι) (hjk : j ≠ k)
    (h : lk k j ≠ 0) : ¬ BrunnianAt lk k := fun hb => h (hb j hjk)

/-- **The predicate is inhabited** — on an unlinked (or genuinely Brunnian)
configuration every component satisfies it. Recorded so `no_component_is_brunnian`
below cannot be read as vacuous: it is a statement about *this* carrier's shape, not
a statement that `BrunnianAt` is unsatisfiable. -/
theorem brunnianAt_of_all_zero (lk : ι → ι → ℤ) (h : ∀ i j, lk i j = 0) (k : ι) :
    BrunnianAt lk k := fun j _ => h k j

/-- **The measured shape of the derived carrier**: `m` components whose linking
graph is the path `P_m` — consecutive components linked, and (as recorded in
`lk_symm`) linking is symmetric.

Only the two facts the theorem uses are demanded. In particular nothing here says
the *non*-consecutive pairs vanish; the conclusion does not need it, and demanding
it would make the structure harder to instantiate than the result requires. -/
structure PathLinking (m : ℕ) where
  /-- the pairwise linking numbers -/
  lk : Fin m → Fin m → ℤ
  /-- linking is symmetric in its two components -/
  lk_symm : ∀ i j, lk i j = lk j i
  /-- consecutive components are genuinely linked -/
  consecutive_ne : ∀ (i : Fin m) (h : (i : ℕ) + 1 < m), lk i ⟨(i : ℕ) + 1, h⟩ ≠ 0

/-- **The result.** On a path of at least two components, *no* component has all
its linking numbers vanishing — so the Borromean hypothesis of the complement-genus
estimate fails at every single one.

The endpoint is the case worth stating: the last component has no successor, and the
argument closes it by walking backwards through `lk_symm`. -/
theorem no_component_is_brunnian {m : ℕ} (hm : 2 ≤ m) (P : PathLinking m)
    (k : Fin m) : ¬ BrunnianAt P.lk k := by
  by_cases h : (k : ℕ) + 1 < m
  · -- `k` has a successor: it is linked to it
    refine not_brunnianAt_of_linked P.lk k ⟨(k : ℕ) + 1, h⟩ ?_ (P.consecutive_ne k h)
    intro hcontra
    have : (k : ℕ) + 1 = (k : ℕ) := congrArg Fin.val hcontra
    omega
  · -- `k` is the last component: it is linked to its predecessor
    have hk : (k : ℕ) + 1 = m := le_antisymm k.isLt (by omega)
    have hpos : 0 < (k : ℕ) := by omega
    have hlt : (k : ℕ) - 1 < m := by omega
    have hsucc : ((k : ℕ) - 1) + 1 < m := by omega
    have key : P.lk ⟨(k : ℕ) - 1, hlt⟩ ⟨((k : ℕ) - 1) + 1, hsucc⟩ ≠ 0 :=
      P.consecutive_ne ⟨(k : ℕ) - 1, hlt⟩ hsucc
    have hidx : (⟨((k : ℕ) - 1) + 1, hsucc⟩ : Fin m) = k := by
      apply Fin.ext; simp only []; omega
    rw [hidx] at key
    refine not_brunnianAt_of_linked P.lk k ⟨(k : ℕ) - 1, hlt⟩ ?_ ?_
    · intro hcontra
      have : (k : ℕ) - 1 = (k : ℕ) := congrArg Fin.val hcontra
      omega
    · rw [P.lk_symm]; exact key

/-- The derived carrier's measured linking data: components `Fin m`, consecutive
pairs carrying `-2`, everything else `0`.

Instantiated so the theorem above is demonstrably about a real configuration rather
than an empty hypothesis. The value `-2` is what the probe measures in the
all-`σ⁻¹` branch; nothing below depends on it beyond being nonzero. -/
def atomCarrier (m : ℕ) : PathLinking m where
  lk i j := if (i : ℕ) + 1 = (j : ℕ) ∨ (j : ℕ) + 1 = (i : ℕ) then -2 else 0
  lk_symm i j := by
    by_cases h : (i : ℕ) + 1 = (j : ℕ) ∨ (j : ℕ) + 1 = (i : ℕ)
    · simp [h, Or.comm.mp h]
    · have h' : ¬((j : ℕ) + 1 = (i : ℕ) ∨ (i : ℕ) + 1 = (j : ℕ)) := fun hc => h (Or.comm.mp hc)
      simp [h, h']
  consecutive_ne i h := by simp

/-- **Applied to the carrier**: for `A ≥ 1` the closure has `μ = A + 1 ≥ 2`
components and the handle is available at none of them. -/
theorem genus_handle_available_at_no_component_of_the_carrier {m : ℕ} (hm : 2 ≤ m)
    (k : Fin m) : ¬ BrunnianAt (atomCarrier m).lk k :=
  no_component_is_brunnian hm (atomCarrier m) k

end QOU.Mass.FreedmanHeGenusHandleNeedsVanishingLinking
