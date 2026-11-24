import QOU.StandardModel.PhotonElectronTrace

/-!
# The 3-strand torus family `T(3, 3m+2)` as electron words

The braid `(σ₀σ₁)²` is literally the list `electron ++ [σ₁]`: the trefoil braid on three
strands is the electron word times one photon letter. Adding `m` full twists
`Δ² = electron²` gives `(σ₀σ₁)^(3m+2) = electron^(2m+1) · σ₁`, the braid of `T(3, 3m+2)`,
of writhe `6m + 4`. `m = 1` is the `T(3,5)` linchpin word of `PhotonElectronTrace`.

On the hook block every full twist acts as `1`, so the hook trace is the same for every
`m`. The two one-dimensional blocks see only the writhe. So the whole family differs only
in the power of `q` that `τ` reads. Nothing here selects `m = 1`.
-/

namespace QOU.AlphaEM.TorusFamily

open Matrix QOU.AlphaEM.IotaOdd QOU.AlphaEM.ElectronWord

variable {K : Type*} [Field K]

/-- `m` full twists, written as `electron²` repeated. -/
def fullTwists : ℕ → List Letter
  | 0 => []
  | m + 1 => electron ++ electron ++ fullTwists m

/-- The `T(3, 3m+2)` word, `electron^(2m+1) · σ₁`. -/
def torusWord (m : ℕ) : List Letter := fullTwists m ++ electron ++ [(1, true)]

/-- **The trefoil braid `(σ₀σ₁)²` is the electron times one photon letter.** -/
theorem trefoil_eq_electron_letter :
    electron ++ [(1, true)] = [(0, true), (1, true), (0, true), (1, true)] := rfl

theorem hookWord_append (q : K) (a b : List Letter) :
    hookWord q (a ++ b) = hookWord q a * hookWord q b := by
  simp [hookWord, List.map_append, List.prod_append]

theorem symWord_append (q : K) (a b : List Letter) :
    symWord q (a ++ b) = symWord q a * symWord q b := by
  simp [symWord, List.map_append, List.prod_append]

theorem altWord_append (q : K) (a b : List Letter) :
    altWord q (a ++ b) = altWord q a * altWord q b := by
  simp [altWord, List.map_append, List.prod_append]

/-- **Full twists act as `1` on the hook block.** -/
theorem hookWord_fullTwists (q : K) (hq : q ≠ 0) (m : ℕ) :
    hookWord q (fullTwists m) = 1 := by
  induction m with
  | zero => simp [fullTwists, hookWord]
  | succ m ih =>
    rw [fullTwists, hookWord_append, ih, mul_one,
      QOU.AlphaEM.PhotonElectron.electron_sq_hook q hq]

theorem symWord_fullTwists (q : K) (m : ℕ) : symWord q (fullTwists m) = (q ^ 6) ^ m := by
  induction m with
  | zero => simp [fullTwists, symWord]
  | succ m ih =>
    rw [fullTwists, symWord_append, symWord_append, ih]
    simp [symWord, electron, symLetter]
    ring

theorem altWord_fullTwists (q : K) (m : ℕ) :
    altWord q (fullTwists m) = ((q⁻¹) ^ 6) ^ m := by
  induction m with
  | zero => simp [fullTwists, altWord]
  | succ m ih =>
    rw [fullTwists, altWord_append, altWord_append, ih]
    simp [altWord, electron, altLetter]
    ring

/-- **The hook trace of `T(3, 3m+2)` does not depend on `m`.** -/
theorem torusWord_hook_trace (q : K) (hq : q ≠ 0) (m : ℕ) :
    (hookWord q (torusWord m)).trace = (hookWord q (electron ++ [(1, true)])).trace := by
  rw [torusWord, List.append_assoc, hookWord_append, hookWord_fullTwists q hq, one_mul]

/-- **`τ` on `T(3, 3m+2)` is `q^(6m+4) − q^-(6m+4)`.** -/
theorem torusWord_tau (q : K) (m : ℕ) :
    symWord q (torusWord m) - altWord q (torusWord m)
      = (q ^ 6) ^ m * q ^ 4 - ((q⁻¹) ^ 6) ^ m * (q⁻¹) ^ 4 := by
  rw [torusWord, List.append_assoc, symWord_append, altWord_append,
    symWord_fullTwists, altWord_fullTwists]
  simp [symWord, altWord, electron, symLetter, altLetter]
  ring

end QOU.AlphaEM.TorusFamily
