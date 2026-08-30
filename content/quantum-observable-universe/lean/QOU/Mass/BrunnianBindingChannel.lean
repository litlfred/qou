/-
QOU.Mass.BrunnianBindingChannel — why the nuclear binding multiplier is an UNSIGNED
coordination COUNT and not a (vanishing) Gauss linking number.

Arc context (bk-crossing-coordination; bean `qou-brng`, the linking-vs-self-energy amplitude
assignment). The mass/binding split assigns

  mass    ← self  (intra-component) crossings, closed into a q-dimension self-trace  `lw`
  binding ← mutual (inter-component) crossings                                        (`M`)

(the self+mutual partition of the crossing energy is stated in
`content/quantum-observable-universe/climax-volume-mass/crossing-energy-trefoil.md`:
`𝔈_cross(𝔥) = Σᵢ 𝔈_cross(Kᵢ) + 𝔈_cross(𝓛)`; the field-theoretic analogue is the
Biot–Savart self-adjointness split `H(ΣVᵢ) = Σ H(Vᵢ) + 2 Σ_{i<j}⟨Vᵢ,BS(Vⱼ)⟩`,
`docs/audits/2026-08-01-em-linking-reads-round1.md` Round 3).

The OPEN puzzle (bean `qou-brng`): the binding multiplier `M` is the arc's integer
**coordination count** (graph degree `z = A−1`; `bk-coordination-multiplicity.md`), NOT a Gauss
linking number — and for the actual nuclear building-block links this distinction is forced, not
cosmetic: the ³He/⁴He carrier is the **Borromean** link `L6a4`, which is *Brunnian* — every
pairwise Gauss linking number is identically zero. A route that read binding off the pairwise
linking number would give **zero** for these nuclei.

This file resolves that half of the puzzle, using the *proved* crossing-energy channel
decomposition (`QOU.Braiding.CrossingEnergy.decomposition`):

  signed  (strong / cosh) channel  ~  (n₊ − n₋)   the writhe = 2·(Gauss linking number)
  unsigned(Coulomb / sinh) channel ~  (n₊ + n₋)   the crossing / coordination COUNT

For a **Brunnian** pair the pairwise linking number vanishes (`n₊ = n₋`, signed crossing sum
zero), so the signed channel is empty and the mutual/binding energy is carried ENTIRELY by the
unsigned count channel. The surviving multiplier is therefore a coordination COUNT, not a linking
number — exactly the arc's `M`. This is the discrete analogue of the em-linking thread's
"route around O1 is an UNSIGNED quantity" (Khesin Rmk 3.5, `…em-linking-reads-round1.md` Round 4):
two independent threads land on the same unsigned object.

What this does NOT close (still `qou-brng`): (i) the exact map from `n₊+n₋` to the graph-degree
`z = A−1`; (ii) why the surviving count channel enters as a *bare integer* while the self/mass
channel keeps the full q-dimension self-trace `lw`. Both are stated precisely in
`docs/audits/2026-08-30-brunnian-binding-channel.md`; neither is asserted here.

Ground ring `ℝ` (§7c: archimedean — uses `q⁻¹`, division, and the substrate ordering `1 < q`),
matching `crossing-energy.lean`. `n₊`, `n₋` are crossing multiplicities (`ℕ`). No fit.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.Mass.BrunnianBindingChannel

/-- Skein-signed mutual crossing energy of a component pair with `np` positive and `nn` negative
inter-component crossings: `n₊·q − n₋·q⁻¹` (the `𝔈_cross(𝓛)` of `def:crossing-energy`). -/
noncomputable def pairEnergy (np nn : ℕ) (q : ℝ) : ℝ := (np : ℝ) * q - (nn : ℝ) * q⁻¹

/-- **Signed** (strong / cosh) channel: `½(n₊ − n₋)(q + q⁻¹)`. Its multiplicity is the
**writhe** `n₊ − n₋ = 2·lk`, the (signed) Gauss linking number — sign-changing. -/
noncomputable def signedChannel (np nn : ℕ) (q : ℝ) : ℝ := ((np : ℝ) - (nn : ℝ)) * (q + q⁻¹) / 2

/-- **Unsigned** (Coulomb / sinh) channel: `½(n₊ + n₋)(q − q⁻¹)`. Its multiplicity is the
crossing **count** `n₊ + n₋` — sign-blind, i.e. a coordination count rather than a linking
number. -/
noncomputable def countChannel (np nn : ℕ) (q : ℝ) : ℝ := ((np : ℝ) + (nn : ℝ)) * (q - q⁻¹) / 2

/-- The mutual crossing energy splits into the signed (writhe) and unsigned (count) channels.
Mirrors `QOU.Braiding.CrossingEnergy.decomposition` for the inter-component pair. -/
theorem pairEnergy_decomp (np nn : ℕ) (q : ℝ) :
    pairEnergy np nn q = signedChannel np nn q + countChannel np nn q := by
  unfold pairEnergy signedChannel countChannel
  ring

/-- **A Brunnian pair empties the signed channel.** The Brunnian condition is that the pairwise
Gauss linking number vanishes, i.e. the signed crossing sum is zero (`n₊ = n₋`). Then the
writhe-weighted strong channel is identically zero — no signed/linking contribution to binding
survives. -/
theorem brunnian_signedChannel_zero (m : ℕ) (q : ℝ) : signedChannel m m q = 0 := by
  unfold signedChannel
  simp

/-- **For a Brunnian pair the binding energy IS the unsigned count channel.** With the signed
channel empty, the entire mutual/binding energy is carried by the sign-blind coordination-count
channel. -/
theorem brunnian_energy_is_count_channel (m : ℕ) (q : ℝ) :
    pairEnergy m m q = countChannel m m q := by
  rw [pairEnergy_decomp, brunnian_signedChannel_zero, zero_add]

/-- The Brunnian count channel evaluates to `m·(q − q⁻¹)` — proportional to the crossing count
`m = ½(n₊+n₋)`, not to the (zero) linking number. -/
theorem brunnian_countChannel_eq (m : ℕ) (q : ℝ) :
    countChannel m m q = (m : ℝ) * (q - q⁻¹) := by
  unfold countChannel
  ring

/-- **Binding survives the Brunnian vanishing.** For a crossing pair (`m > 0`) at a substrate
modulus `q > 1`, the count channel is strictly positive — so the mutual energy is nonzero even
though the pairwise linking number is zero. This is the crux of `qou-brng`'s "surviving route":
the coordination count is the correct, non-vanishing binding multiplier for a Brunnian nuclear
link, where the Gauss linking number is not. -/
theorem brunnian_binding_survives (m : ℕ) (hm : 0 < m) (q : ℝ) (hq : 1 < q) :
    0 < countChannel m m q := by
  rw [brunnian_countChannel_eq]
  have hm' : (0 : ℝ) < (m : ℝ) := by exact_mod_cast hm
  have hq0 : (0 : ℝ) < q := lt_trans one_pos hq
  have hinv : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have : (0 : ℝ) < q - q⁻¹ := by linarith
  exact mul_pos hm' this

/-- **The two mutual invariants genuinely diverge for a Brunnian pair.** The signed channel is
zero for every `m` (any number of sign-cancelling crossings), while the count channel strictly
increases with `m`. So "linking number" and "coordination count" are not two names for one
multiplier: on a Brunnian link they take different values, and only the unsigned one is the
binding carrier. -/
theorem brunnian_channels_strict_mono (m : ℕ) (q : ℝ) (hq : 1 < q) :
    signedChannel m m q = signedChannel (m + 1) (m + 1) q
      ∧ countChannel m m q < countChannel (m + 1) (m + 1) q := by
  refine ⟨by rw [brunnian_signedChannel_zero, brunnian_signedChannel_zero], ?_⟩
  rw [brunnian_countChannel_eq, brunnian_countChannel_eq]
  have hq0 : (0 : ℝ) < q := lt_trans one_pos hq
  have hinv : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have hpos : (0 : ℝ) < q - q⁻¹ := by linarith
  have : (m : ℝ) < ((m : ℝ) + 1) := by linarith
  calc (m : ℝ) * (q - q⁻¹)
      < ((m : ℝ) + 1) * (q - q⁻¹) := by nlinarith
    _ = (((m + 1 : ℕ) : ℝ)) * (q - q⁻¹) := by push_cast; ring

end QOU.Mass.BrunnianBindingChannel
