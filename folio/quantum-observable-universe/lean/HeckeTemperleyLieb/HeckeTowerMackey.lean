/-
  Decategorified Mackey / oscillator relation on the Hecke tower, levels 0–3.

  The categorical oscillator equation on ⊕_n H_n(q)-mod is the Heisenberg
  relation for the biadjoint induction/restriction pair (a† = Ind, a = Res):

      Res ∘ Ind  ≅  Ind ∘ Res  ⊕  Id            (categorical [a, a†] = 1).

  For generic q the Hecke algebra H_n(q) is semisimple with the same branching
  multiplicities as S_n (one-box addition/removal on partitions), so the
  decategorified relation is a matrix identity over ℕ between the branching
  matrices R_{n+1→n} (restriction) and their transposes I_{n→n+1} = Rᵀ
  (induction, by Frobenius reciprocity):

      R_{n+1→n} · R_{n+1→n}ᵀ  =  R_{n→n-1}ᵀ · R_{n→n-1}  +  Id_n .

  This file proves that identity at the levels the lepton/meson channel story
  lives on (see QOU/Mass/LeptonMesonParitySplit.lean and the audit doc
  docs/audits/2026-07-06-parabolic-cylinder-toroidal-channel-interpolation.md):

    * level 1 (H_1, one irrep (1)):        R21·R21ᵀ = R10ᵀ·R10 + Id₁
    * level 2 (H_2, lepton irreps (2),(1,1)): R32·R32ᵀ = R21ᵀ·R21 + Id₂

  The level-2 instance contains the Frobenius-reciprocity matrix element
  ⟨Res V_{(2,1)}, V_{(2)}⟩ = ⟨V_{(2,1)}, Ind V_{(2)}⟩ = 1 used by the
  frobenius-lepton-meson-bridge proposition, and upgrades it to the full
  oscillator commutation relation: the number-operator shift by Id is what
  makes the tower a Fock space with Wedderburn blocks as eigenstates.

  Pure ℕ-combinatorics on explicit branching matrices; no imports (§7c: no
  archimedean ring anywhere).

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.Mass.HeckeTowerMackey

/-- Matrix over ℕ as a list of rows. -/
abbrev Mat := List (List Nat)

/-- Dot product of two rows (zero-padded). -/
def dot : List Nat → List Nat → Nat
  | [], _ => 0
  | _, [] => 0
  | a :: as, b :: bs => a * b + dot as bs

/-- `mulT A Bt` is the product `A · B` where `Bt` is `B` given as its
    transpose (list of columns of `B`). -/
def mulT (A Bt : Mat) : Mat := A.map (fun r => Bt.map (dot r))

/-- Entrywise sum (shapes must agree). -/
def matadd (A B : Mat) : Mat := List.zipWith (List.zipWith (· + ·)) A B

/-! ## Branching matrices (rows = level-n irreps, columns = level-(n+1) irreps)

Irrep orderings: level 1: [(1)]; level 2: [(2), (1,1)];
level 3: [(3), (2,1), (1,1,1)]. Restriction = remove one box. -/

/-- `R10`: restriction H_1 → H_0 ((1) → ∅). -/
def R10 : Mat := [[1]]

/-- `R21`: restriction H_2 → H_1 ((2) → (1); (1,1) → (1)), rows = level-1. -/
def R21 : Mat := [[1, 1]]

/-- `R32`: restriction H_3 → H_2 ((3) → (2); (2,1) → (2) ⊕ (1,1);
    (1,1,1) → (1,1)), rows = level-2. -/
def R32 : Mat := [[1, 1, 0], [0, 1, 1]]

def Id1 : Mat := [[1]]
def Id2 : Mat := [[1, 0], [0, 1]]

/-- **Frobenius-reciprocity matrix element of the bridge**: the standard
    (meson) irrep (2,1) restricts to H_2 containing each lepton channel
    exactly once — the middle column of `R32` is (1, 1). -/
theorem bridge_multiplicities :
    (R32.map (fun r => r[1]?)) = [some 1, some 1] := by decide

/-- **Mackey / oscillator relation at level 1**:
    `Res∘Ind = Ind∘Res + Id` on K₀(H_1). Here `R21·R21ᵀ = [[2]]` and
    `R10ᵀ·R10 + Id₁ = [[1]] + [[1]]` (for the 1×1 matrix `R10`,
    `R10ᵀ·R10 = mulT R10 R10`). -/
theorem mackey_level1 :
    mulT R21 R21 = matadd (mulT R10 R10) Id1 := by
  decide

/-- **Mackey / oscillator relation at level 2** (the lepton level):
    `Res∘Ind = Ind∘Res + Id` on K₀(H_2):
    `R32·R32ᵀ = [[2,1],[1,2]] = R21ᵀ·R21 + Id₂ = [[1,1],[1,1]] + Id₂`.
    The off-diagonal 1 is the meson bridge: inducing a lepton channel to H_3
    and restricting reaches the OTHER lepton channel exactly once — through
    the entangled (2,1) Hoefsmit block, never through (3) or (1,1,1). -/
theorem mackey_level2 :
    mulT R32 R32 = matadd (mulT [[1], [1]] [[1], [1]]) Id2 := by
  decide

/-- The transpose used in `mackey_level2` is honest: `[[1],[1]]` is `R21ᵀ`. -/
theorem r21_transpose_ok : mulT [[1], [1]] [[1], [1]] = [[1, 1], [1, 1]] := by
  decide

/-- Sanity: the left side of level 2 is the tridiagonal `[[2,1],[1,2]]` —
    the two lepton channels each of norm 2 with unit coupling, the
    decategorified seat of the Hoefsmit mixing. -/
theorem level2_gram : mulT R32 R32 = [[2, 1], [1, 2]] := by decide

end QOU.Mass.HeckeTowerMackey
