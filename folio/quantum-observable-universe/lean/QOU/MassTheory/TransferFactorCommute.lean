/-
# Transfer factors of the `Φ_q` chain commute

The nucleon-ordering objective named by `prop:ground-state-ordering`,

  `Φ_q(ordering) = Σ_i log |V̂_i|`,

is built in `computations/substrate/hecke_core_symbolic.py`
(`_phi1_from_ordering_sym`) like this: for each strand `i`, walk the strands
`j > i`, form the crossing coefficient `d = crossingCoeff(t_i, t_j)`, update the
running `2 × 2` matrix by `M ← M * T(d)` with

  `T(d) = ((h + d, 1), (1, d))`,

and read off `V̂_i = z · M₁₀ + M₁₁`.

This file proves the structural fact behind the exact numerical degeneracies
measured in `computations/probes/ground_state_ordering_a3_probe.py`:

  **every transfer factor of a given chain commutes with every other**,
  because `T(d) = S + d · 1` for one fixed `S = ((h, 1), (1, 0))`.

Consequently the running product — and hence the readout `V̂_i` — depends on the
crossing coefficients **only through their multiset**: the order in which the
later strands are encountered cannot change it.

In particular the strand-0 coefficient lists of the two ³He arrangements `ppn`
and `pnp` are permutations of one another (`[0, -h/2]` versus `[-h/2, 0]`), so
the two arrangements carry *identical* `V̂` data on the bare nucleon chain. At
the nucleon level the objective is **degenerate** between them and cannot prefer
either — so rule (iii) of `prop:ground-state-ordering` (*"the sorted ordering
beats interleaving for `A ≤ 3`"*) cannot hold at ³He as a strict inequality.

## What this does NOT claim

`sorry-free ≠ derived`. Nothing here derives a binding energy, a nucleon
ordering, or a value of `Φ_q`, and nothing is compared to AME or CODATA. This is
a statement about the *shape* of the transfer chain: it turns the observed ³He
degeneracy from a numerical coincidence into a theorem. It does **not** prove
`prop:ground-state-ordering`, which remains stated-not-proved, and it says
nothing about which arrangement production should use.

The `2 × 2` carrier `M2` is spelled out rather than imported as `Matrix (Fin 2)
(Fin 2) R` so the entries line up one-for-one with the four scalars
`M00, M01, M10, M11` that the Python actually carries, and so that
`mulNotComm` below can certify — inside this same file — that the carrier is
genuinely non-commutative and the commutation theorem therefore has content.

## Base ring

§7c-clean: everything is stated over a generic `{R : Type*} [CommRing R]`. No
archimedean construct appears; the `log |·|` wrapper of `Φ_q` lives strictly
downstream of the readout proved here.

Companion audit:
`docs/audits/2026-08-09-ordering-loose-ends-a3-helper-and-missing-he-rows.md`.
Bean `qou-48is`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.List.Perm.Basic
import Mathlib.Tactic.Ring

namespace QOU.MassTheory

variable {R : Type*} [CommRing R]

/-- The `2 × 2` transfer state of the `Φ_q` chain, carried as the four scalars
`M00, M01, M10, M11` exactly as `_phi1_from_ordering_sym` does. -/
structure M2 (R : Type*) where
  /-- entry `M₀₀` -/
  m00 : R
  /-- entry `M₀₁` -/
  m01 : R
  /-- entry `M₁₀` -/
  m10 : R
  /-- entry `M₁₁` -/
  m11 : R

namespace M2

/-- Matrix product, transcribed from the Python update
`n00 = M00*t00 + M01*t10`, `n01 = M00*t01 + M01*t11`,
`n10 = M10*t00 + M11*t10`, `n11 = M10*t01 + M11*t11`. -/
def mul (X Y : M2 R) : M2 R :=
  ⟨X.m00 * Y.m00 + X.m01 * Y.m10, X.m00 * Y.m01 + X.m01 * Y.m11,
   X.m10 * Y.m00 + X.m11 * Y.m10, X.m10 * Y.m01 + X.m11 * Y.m11⟩

/-- The identity transfer state the chain starts from. -/
def one : M2 R := ⟨1, 0, 0, 1⟩

theorem mul_assoc (X Y Z : M2 R) : mul (mul X Y) Z = mul X (mul Y Z) := by
  simp only [mul, M2.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring⟩

theorem one_mul (X : M2 R) : mul one X = X := by
  simp [mul, one]

theorem mul_one (X : M2 R) : mul X one = X := by
  simp [mul, one]

/-- **The carrier is genuinely non-commutative.**

Guards the commutation theorem below against vacuity: if `M2 R` were a
commutative monoid, `transferFactor_comm` would say nothing. -/
theorem mulNotComm [Nontrivial R] :
    ∃ X Y : M2 R, mul X Y ≠ mul Y X := by
  refine ⟨⟨0, 1, 0, 0⟩, ⟨0, 0, 1, 0⟩, ?_⟩
  simp only [mul]
  intro h
  simp at h

end M2

/-- One step of the `Φ_q` transfer chain for crossing coefficient `d`:
`T(d) = ((h + d, 1), (1, d))`. -/
def transferFactor (h d : R) : M2 R := ⟨h + d, 1, 1, d⟩

/-- The `d`-independent skeleton `S = ((h, 1), (1, 0))`. -/
def transferSkeleton (h : R) : M2 R := ⟨h, 1, 1, 0⟩

/-- `T(d) = S + d · 1` componentwise — the reason the factors commute:
the crossing coefficient only ever adds a multiple of the identity, and never
touches the off-diagonal structure. -/
theorem transferFactor_eq_skeleton_add (h d : R) :
    transferFactor h d
      = ⟨(transferSkeleton h).m00 + d, (transferSkeleton h).m01,
         (transferSkeleton h).m10, (transferSkeleton h).m11 + d⟩ := by
  simp [transferFactor, transferSkeleton]

/-- **Any two transfer factors of the same chain commute.**

Not a triviality: the carrier is non-commutative (`M2.mulNotComm`) and the
readout `phiReadout` is not symmetric in the entries. Commutation holds because
every factor is `S + d · 1` for one and the same `S`. -/
theorem transferFactor_comm (h d₁ d₂ : R) :
    M2.mul (transferFactor h d₁) (transferFactor h d₂)
      = M2.mul (transferFactor h d₂) (transferFactor h d₁) := by
  simp only [M2.mul, transferFactor, M2.mk.injEq]
  refine ⟨by ring, by ring, by ring, by ring⟩

/-- The chain product over a list of crossing coefficients, in list order. -/
def chainProd (h : R) : List R → M2 R
  | [] => M2.one
  | d :: l => M2.mul (transferFactor h d) (chainProd h l)

/-- **The chain product depends on the crossing coefficients only as a
multiset**: permuting the later strands cannot change it. -/
theorem chainProd_perm (h : R) {l₁ l₂ : List R} (hp : l₁.Perm l₂) :
    chainProd h l₁ = chainProd h l₂ := by
  induction hp with
  | nil => rfl
  | cons x _ ih => simp only [chainProd, ih]
  | swap x y l =>
      simp only [chainProd, ← M2.mul_assoc, transferFactor_comm h y x]
  | trans _ _ ih₁ ih₂ => exact ih₁.trans ih₂

/-- The `Φ_q` readout of a chain state: `V̂ = z · M₁₀ + M₁₁`, mirroring
`V_sym = z * M10 + M11`. -/
def phiReadout (z : R) (M : M2 R) : R := z * M.m10 + M.m11

/-- The readout is not a constant function of the state — so the invariance
results below are statements about the chain, not artefacts of a degenerate
readout. -/
theorem phiReadout_transferFactor (h d z : R) :
    phiReadout z (transferFactor h d) = z + d := by
  simp only [phiReadout, transferFactor]
  ring

/-- **The per-strand `Φ_q` datum depends only on the multiset of crossing
coefficients contributed by the strands after it.** -/
theorem phiReadout_chainProd_perm (h z : R) {l₁ l₂ : List R} (hp : l₁.Perm l₂) :
    phiReadout z (chainProd h l₁) = phiReadout z (chainProd h l₂) := by
  rw [chainProd_perm h hp]

/-- **The ³He nucleon-level degeneracy, as a theorem.**

For a proton at position 0 the later strands of `ppn` contribute
`d(p,p) = a` then `d(p,n) = b`, while those of `pnp` contribute them in the
opposite order. The objective cannot tell the two arrangements apart. -/
theorem he3_ppn_pnp_readout_eq (h z a b : R) :
    phiReadout z (chainProd h [a, b]) = phiReadout z (chainProd h [b, a]) :=
  phiReadout_chainProd_perm h z (List.Perm.swap b a [])


/-- **Multiplicativity of `chainProd` over list concatenation (`qou-48is`).** -/
theorem chainProd_append (h : R) (l₁ l₂ : List R) :
    chainProd h (l₁ ++ l₂) = M2.mul (chainProd h l₁) (chainProd h l₂) := by
  induction l₁ with
  | nil => simp [chainProd, M2.one_mul]
  | cons d l ih =>
      simp only [List.cons_append, chainProd, ih, M2.mul_assoc]

/-- **Explicit symmetric polynomial form of the 2-step `Φ_q` readout (`qou-48is`).**
`phiReadout z (chainProd h [a, b]) = z * (h + a + b) + (1 + a * b)`, depending on
`(a, b)` solely through the elementary symmetric polynomials `a + b` and `a * b`. -/
theorem phiReadout_chainProd_two_explicit (h z a b : R) :
    phiReadout z (chainProd h [a, b]) = z * (h + a + b) + (1 + a * b) := by
  simp only [chainProd, M2.mul, M2.one, transferFactor, phiReadout]
  ring

end QOU.MassTheory
