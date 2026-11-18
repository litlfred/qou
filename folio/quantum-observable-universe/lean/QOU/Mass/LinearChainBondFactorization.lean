/-
# Per-neutron multiplicativity of the linear-chain atom word (bean 2o66)

The bound atom braid `atom_braid_word_3A(Z, N)` orders strands `p^Z · n^N` and
places one inter-nucleon crossing between adjacent nucleons only, each on a
DISTINCT generator, so the Markov-trace ratio `tr_free / tr_atom` factorizes
over the A−1 bond positions (verified to the 50-dps floor in
docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md — that factorization
is the MODEL here, not re-proved from Hecke theory). This file proves the
combinatorial content of the closed form and its consequences:

  * `chainRatio_closed_form` — the bond census (Z−1 pp) · (1 pn) · (N−1 nn)
    gives  ratio(Z,N) = f_pp^(Z−1) · f_pn · f_nn^(N−1)   (Z, N ≥ 1);
  * `chainRatio_succ_neutron` — **per-neutron multiplicativity**: adding one
    neutron multiplies the ratio by exactly `f_nn` — the ratio is exactly
    geometric in N;
  * `chainRatio_neutron_slope_indep` — the per-neutron multiplier is
    Z-INDEPENDENT (cross-multiplied form, division-free);
  * `log_chainRatio_succ_neutron` — archimedean corollary: the log-binding is
    affine in N with slope `Real.log f_nn` (the probe's l(q₀) = ln f_nn ≈
    1.23698 at the substrate anchor, i.e. b_nn = α·l ≈ 5.178 MeV).

Base ring (§7c): the chain algebra needs only `[CommMonoid M]` — products, no
subtraction, no order. Only the final log corollary lives over `ℝ`.

-- Ref: [leitner2026] docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

namespace QOU.Mass.LinearChainBond

variable {M : Type*} [CommMonoid M]

/-- The factor carried by 0-indexed bond `i` (joining nucleons `i+1` and `i+2`
in the `p^Z · n^N` order): `pp` while both endpoints are protons
(`i + 2 ≤ Z`), `pn` at the single interface (`i + 1 = Z`), `nn` after. -/
def bondFactor (Z : ℕ) (fpp fpn fnn : M) (i : ℕ) : M :=
  if i + 2 ≤ Z then fpp else if i + 1 = Z then fpn else fnn

/-- The chain trace ratio `tr_free / tr_atom` of the `(Z, N)` atom word in the
distinct-generator bond model: the product of the `A − 1 = Z + N − 1`
per-bond factors. -/
def chainRatio (Z N : ℕ) (fpp fpn fnn : M) : M :=
  ∏ i ∈ Finset.range (Z + N - 1), bondFactor Z fpp fpn fnn i

/-- **Per-neutron multiplicativity** (the bean-2o66 lemma). For `Z, N ≥ 1`,
adding one neutron appends exactly one `nn` bond: the trace ratio is
multiplied by `f_nn`, so it is exactly geometric in `N` — and the multiplier
does not mention `Z`. -/
theorem chainRatio_succ_neutron (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 1 ≤ N)
    (fpp fpn fnn : M) :
    chainRatio Z (N + 1) fpp fpn fnn = chainRatio Z N fpp fpn fnn * fnn := by
  unfold chainRatio
  have hidx : Z + (N + 1) - 1 = (Z + N - 1) + 1 := by omega
  rw [hidx, Finset.prod_range_succ]
  congr 1
  -- the appended bond (index Z+N−1) joins two neutrons: both branches close
  unfold bondFactor
  have h1 : ¬ (Z + N - 1 + 2 ≤ Z) := by omega
  have h2 : ¬ (Z + N - 1 + 1 = Z) := by omega
  simp [h1, h2]

/-- Base of the tower: one neutron. The `Z` bonds are `Z − 1` pp's and the
single pn interface: `ratio(Z, 1) = f_pp^(Z−1) · f_pn`. -/
theorem chainRatio_one_neutron (Z : ℕ) (hZ : 1 ≤ Z) (fpp fpn fnn : M) :
    chainRatio Z 1 fpp fpn fnn = fpp ^ (Z - 1) * fpn := by
  unfold chainRatio
  have hidx : Z + 1 - 1 = (Z - 1) + 1 := by omega
  rw [hidx, Finset.prod_range_succ]
  have hlast : bondFactor Z fpp fpn fnn (Z - 1) = fpn := by
    unfold bondFactor
    have h1 : ¬ (Z - 1 + 2 ≤ Z) := by omega
    have h2 : Z - 1 + 1 = Z := by omega
    simp [h1, h2]
  have hbody :
      ∏ i ∈ Finset.range (Z - 1), bondFactor Z fpp fpn fnn i
        = fpp ^ (Z - 1) := by
    have hconst : ∀ i ∈ Finset.range (Z - 1),
        bondFactor Z fpp fpn fnn i = fpp := by
      intro i hi
      have hi' := Finset.mem_range.mp hi
      unfold bondFactor
      have h1 : i + 2 ≤ Z := by omega
      simp [h1]
    rw [Finset.prod_congr rfl hconst, Finset.prod_const, Finset.card_range]
  rw [hlast, hbody]

/-- **Closed form** (the audit's exact additive chain, multiplicatively):
`ratio(Z, N) = f_pp^(Z−1) · f_pn · f_nn^(N−1)` for `Z, N ≥ 1`. -/
theorem chainRatio_closed_form (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 1 ≤ N)
    (fpp fpn fnn : M) :
    chainRatio Z N fpp fpn fnn = fpp ^ (Z - 1) * fpn * fnn ^ (N - 1) := by
  induction N with
  | zero => omega
  | succ n ih =>
    rcases Nat.eq_or_lt_of_le hN with h1 | h2
    · -- N = 1
      have hn0 : n = 0 := by omega
      subst hn0
      simpa using chainRatio_one_neutron Z hZ fpp fpn fnn
    · -- N = n+1 with n ≥ 1: peel the last neutron
      have hn : 1 ≤ n := by omega
      rw [chainRatio_succ_neutron Z n hZ hn, ih hn]
      have hpow : n + 1 - 1 = (n - 1) + 1 := by omega
      rw [hpow, pow_succ, mul_assoc]

/-- **Z-independence of the per-neutron multiplier** (division-free
cross-multiplied form): the step `ratio(·, N) → ratio(·, N+1)` is the same
for every proton count. -/
theorem chainRatio_neutron_slope_indep (Z Z' N : ℕ)
    (hZ : 1 ≤ Z) (hZ' : 1 ≤ Z') (hN : 1 ≤ N) (fpp fpn fnn : M) :
    chainRatio Z (N + 1) fpp fpn fnn * chainRatio Z' N fpp fpn fnn
      = chainRatio Z' (N + 1) fpp fpn fnn * chainRatio Z N fpp fpn fnn := by
  rw [chainRatio_succ_neutron Z N hZ hN, chainRatio_succ_neutron Z' N hZ' hN]
  ac_rfl

/-! ## Archimedean corollary — the log-binding is affine in N

At the substrate anchor the per-bond factors are positive reals and
`B_sym = α · ln(ratio)`; the per-neutron log increment is `ln f_nn = l(q₀)`
(≈ 1.23698, i.e. `b_nn = α·l ≈ 5.178` MeV), independent of `Z`. -/

/-- Adding one neutron adds exactly `Real.log f_nn` to the log-ratio. -/
theorem log_chainRatio_succ_neutron (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 1 ≤ N)
    (fpp fpn fnn : ℝ) (hnn : fnn ≠ 0)
    (hchain : chainRatio Z N fpp fpn fnn ≠ 0) :
    Real.log (chainRatio Z (N + 1) fpp fpn fnn)
      = Real.log (chainRatio Z N fpp fpn fnn) + Real.log fnn := by
  rw [chainRatio_succ_neutron Z N hZ hN, Real.log_mul hchain hnn]

/-- **Two-neutron step multiplicativity (`qou-l2ob`).** Appending two neutrons
to the `(Z, N)` linear chain (`Z, N ≥ 1`) multiplies `chainRatio Z N` by `fnn ^ 2`. -/
theorem chainRatio_add_two_neutrons (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 1 ≤ N)
    (fpp fpn fnn : M) :
    chainRatio Z (N + 2) fpp fpn fnn = chainRatio Z N fpp fpn fnn * (fnn * fnn) := by
  have hN1 : 1 ≤ N + 1 := by omega
  rw [show N + 2 = (N + 1) + 1 by omega,
    chainRatio_succ_neutron Z (N + 1) hZ hN1,
    chainRatio_succ_neutron Z N hZ hN, mul_assoc]

end QOU.Mass.LinearChainBond
