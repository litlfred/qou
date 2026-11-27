import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Fin.VecNotation
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.GroupTheory.Perm.Sign
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.Dimension.RankNullity
import Mathlib.Tactic
import BraidKnotOctonion.S5CharactersOnBringDeformations
import BraidKnotOctonion.BringDescendingTower
import QOU.EightfoldWay.TrialitySelectionRule
import QOU.StandardModel.HyperchargeBatteryReduction

set_option autoImplicit false

/-!
# Bring Curve $\mathbb{Z}_3$ Kummer–Prym Riemann–Roch Zero-Mode Count, Chevalley–Weil Hurwitz Dichotomy, $\mathbb{F}_3[S_5]$ Torsion Breaking, and $\Lambda^1 F \oplus \Lambda^2 F^*$ Anomaly Matching

Pure-algebraic Lean 4 formalization for **Closing Open Gap 3 (Option 3A Primary)**:
why $N_{\mathrm{gen}} = 3$ fermion generations arise on Bring's genus-$4$ curve
$\mathcal{B} = \{p_1 = p_2 = p_3 = 0\} \subset \mathbb{P}^4$ ($\chi_{\mathrm{eu}}(\mathcal{B}) = -6$,
$\mathrm{Aut}(\mathcal{B}) \cong S_5$) when internal fermions couple to a non-trivial $\mathbb{Z}_3$
colour Kummer torsion line bundle $\mathcal{L} \in \mathrm{Pic}^0(\mathcal{B})[3] \setminus \{\mathcal{O}_{\mathcal{B}}\}$.

Authored strictly under AGENTS.md §7c generic ring/field discipline (`{R : Type*} [CommRing R]`,
`{F : Type*} [Field F]`, `ZMod 3`, `ℤ`, `ℕ`; zero `ℝ`, zero empirical literals, zero `sorry`,
zero custom `axiom`s, `[propext, Classical.choice, Quot.sound]` only):

1. **§1 — Divisor Positivity, Twisted Canonical Riemann–Roch, Spinor Contrast, & Prym $10 = 4 + 3 + 3$ Split:**
   - Proves `effective_deg_zero_divisor_eq_zero`: an effective divisor ($D(P) \ge 0$) of degree
     $\sum_P D(P) = 0$ vanishes identically ($D = 0$).
   - Defines `SmoothCurveRRData` (carrying Picard group, degree homomorphism, canonical class,
     Riemann–Roch, Serre duality, and effective degree-$0$ vanishing) together with an explicit
     inhabited genus-$4$ model `bringGenus4PicModel` on $\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$
     certifying complete non-vacuity.
   - Proves **unconditionally** for any $3$-torsion class $L \ne 0$ ($3 \cdot L = 0$) on a genus-$4$
     curve (`bring_z3_prym_chevalley_weil_ten_split`):
     * $\deg L = 0$, $\deg(2L) = 0$, and $2L \ne 0$ are **derived** (not assumed);
     * $(h^0(K), h^1(K)) = (4, 1)$, whereas $(h^0(K + L), h^1(K + L)) = (3, 0)$ and
       $(h^0(K + 2L), h^1(K + 2L)) = (3, 0)$ — **every non-trivial $\mathbb{Z}_3$-triality sector
       has exact chiral zero-mode dimension $3$ and zero mirror modes**;
     * Chevalley–Weil total canonical dimension on the étale $\mathbb{Z}_3$ Kummer cover
       $\tilde{\mathcal{B}} \to \mathcal{B}$ is $4 + 3 + 3 = 10 = \tilde{g}$, Prym cotangent
       dimension is $3 + 3 = 6 = \tilde{g} - g$, and the net Dolbeault index
       $h^0(K + kL) - h^1(K + kL) = 3$ holds uniformly for **all** $k \in \mathbb{N}$.
   - **Honest Spin-Bundle Contrast (`untwisted_spin_structure_zero_index`)**: For an untwisted
     theta characteristic / spin bundle $S$ ($2S = K$, $\deg S = g - 1 = 3$),
     $h^0(S + L) - h^1(S + L) = 0$ for every degree-$0$ $L$; thus nonzero chiral family index
     specifically requires the canonical / Spin$^c$ Euler-flux twist $K = 2S$ ($\deg K = 6$).

2. **§2 — Complete Hurwitz & Chevalley–Weil Classification: Ascending vs Descending $\mathbb{Z}_3$-Covers:**
   - Proves `unramified_z3_over_bring_genus_ten` ($2\tilde{g} - 2 = 3(2\cdot 4 - 2) \iff \tilde{g} = 10$)
     and `descending_z3_from_genus4_solutions`: a cyclic $\mathbb{Z}_3$-cover $\Sigma_4 \to \mathcal{B}_0$
     from genus $4$ ($\chi_{\mathrm{eu}} = -6$) satisfies $3g_0 + r = 6$, whose **complete** set of
     solutions in $\mathbb{N}^2$ is $\{(2, 0), (1, 3), (0, 6)\}$.
   - Proves `descending_z3_cannot_give_three_three`: under the exact Chevalley–Weil eigenspace
     formula, $(2,0)$ ($\mathcal{B} \to \mathcal{C}_2$, Bring's unique free $C_3 \subset S_5$ quotient)
     yields $(2, 1, 1)$; $(1,3)$ yields $(1, 2, 1)$ or $(1, 1, 2)$; and $(0,6)$ yields
     $(0, 3, 1)$, $(0, 2, 2)$, or $(0, 1, 3)$. **None** of the descending covers can ever produce
     $(d_1, d_2) = (3, 3)$, whereas among unramified $\mathbb{Z}_3$-covers $\tilde{\Sigma} \to \Sigma_{g_0}$,
     $(d_1, d_2) = (3, 3)$ holds **uniquely** at $g_0 = 4$ ($\tilde{g} = 10$).

3. **§3 — Exact $S_5$ Normalizer of $C_3$ & $\mathbb{F}_3[S_5]$ Torsion Action on $\mathrm{Pic}^0(\mathcal{B})[3]$:**
   - Proves directly in `Equiv.Perm (Fin 5)` that for $C_3 = \langle(0\,1\,2)\rangle$,
     $|C_{S_5}(C_3)| = 6$ ($C_3 \times S_2$) and $|N_{S_5}(C_3)| = 12$ ($S_3 \times S_2$).
   - Proves **algebraically** (`bringStdF3_simple_s5`) that $V_{\mathrm{std}}(\mathbb{F}_3) = \{\sum_{i=0}^4 v_i = 0\} \subset \mathbb{F}_3^5$
     (`card = 81`) is a **simple** $\mathbb{F}_3[S_5]$-module with zero $C_5$-fixed vectors, and
     deduces via `extension_fixed_eq_zero` that for **every** $\mathbb{F}_3[S_5]$-extension
     $0 \to V_{\mathrm{std}}(\mathbb{F}_3) \to M \to V_{\mathrm{std}}(\mathbb{F}_3) \to 0$
     (hence every $S_5$-invariant integral homology lattice of $\mathrm{Pic}^0(\mathcal{B})[3]$,
     `card = 3^8 = 6561`), $M^{C_5} = M^{A_5} = M^{S_5} = \{0\}$: **no non-trivial $3$-torsion line
     bundle on $\mathcal{B}$ can preserve $S_5$ or $A_5$**.
   - Characterizes the exact fixed subspaces under $S_4$ (`card = 3`, giving $8$ non-trivial
     $S_4$-invariant $3$-torsion classes in $V_{\mathrm{std}}(\mathbb{F}_3)^{\oplus 2}$),
     $S_3 \times S_2$ (`card = 3`, $8$ non-trivial classes), and $C_3$ (`card = 9`).

4. **§4 — Central $Z(\mathrm{SU}(3)_c)$ Kummer Twist on $\Lambda^1 F \oplus \Lambda^2 F^*$, Gauge Anomalies, & $S_5 \to S_4$ Lepton Pairing:**
   - Links the 5 Weyl multiplets of $\Lambda^1 F \oplus \Lambda^2 F^*$ ($F = W_2(y_2) \oplus W_3^*(y_3)$,
     $2y_2 + 3y_3 = 0$) to `QOU.Eightfold.TrialitySelectionRule.triality`: central $Z(\mathrm{SU}(3)_c) \cong \mu_3$
     holonomy ($\mathcal{W}_3 = \mathbb{C}^3 \otimes \mathcal{L}$, $\det \mathcal{W}_3 \cong \mathcal{O}_{\mathcal{B}}$)
     preserves unbroken $\mathrm{SU}(3)_c$ and assigns triality $t = 1$ to $Q_L$, $t = 2$ to
     $u_R^c, d_R^c$, and $t = 0$ to $L_L, e_R^c$.
   - Proves over any `[CommRing R]` (`exterior_su5_anomaly_identities`) that under $2y_2 + 3y_3 = 0$:
     $[\mathrm{SU}(3)_c]^2 \mathrm{U}(1)_Y = 0$ and $\mathrm{Tr}(Y) = 0$ identically, while
     $2\mathcal{A}_{[\mathrm{SU}(2)_L]^2 \mathrm{U}(1)_Y} = (N_\ell - N_q)y_2$ and
     $9\mathcal{A}_{[\mathrm{U}(1)_Y]^3} = 54(N_q - N_\ell)y_2^3$, refuting the naive $H^0$-only
     truncation $(N_q, N_\ell) = (3, 4)$ (which also violates Witten's $\mathrm{SU}(2)_L$ parity
     $4 + 3\cdot 3 = 13 \equiv 1 \pmod 2$) and confirming full anomaly cancellation for the
     Dolbeault index $(3 - 0, 4 - 1) = (3, 3)$.
   - Proves `s5_protects_fourth_lepton_s4_unlocks_pairing` over any `[Field F]` (`(2 : F) ≠ 0`):
     $\mathrm{Hom}_{S_5}(V_{\mathrm{std}}(F), F) = 0$ (unbroken $S_5$ forbids pairing the 4th lepton
     mode with $H^1(K_{\mathcal{B}}) \cong F$), whereas under $S_4 = \mathrm{Stab}_{S_5}(4)$ (forced
     once $\mathcal{L} \ne 0$ breaks $S_5$), $\dim_F \mathrm{Hom}_{S_4}(V_{\mathrm{std}}(F), F) = 1$,
     and any nonzero $S_4$-invariant Dirac pairing cuts out a massless chiral lepton subspace
     $\ker \Phi$ of exact `Module.finrank = 3`.
   - Isolates the surviving physical inputs in a Rule-13a zero-instance
     `class BringKummerGenerationClosureHypothesis`.

-- Ref: [chevalley-weil1934] C. Chevalley and A. Weil, *Über das Verhalten der Integrale 1. Gattung bei Automorphismen des Funktionenkörpers*, Abh. Math. Sem. Univ. Hamburg 10 (1934) 358–365.
-- Ref: [mumford1974] D. Mumford, *Prym Varieties I*, Contributions to Analysis (1974) 325–350.
-- Ref: [braden-disney-hogg-2022] H. W. Braden and L. Disney-Hogg, *Bring's Curve: Old and New*, Eur. J. Math. 10 (2024) 3, arXiv:2208.13692.
-- Ref: [baez-huerta2010] J. C. Baez and J. Huerta, *The Algebra of Grand Unified Theories*, Bull. Amer. Math. Soc. 47 (2010) 483–552.
-/

namespace QOU.StandardModel.BringPrymRiemannRochGenerations

open scoped BigOperators
open QOU.Brings QOU.Eightfold.TrialitySelectionRule

-- ============================================================================
-- §1. Divisor Positivity, Twisted Canonical Riemann–Roch, & Prym 10 = 4 + 3 + 3
-- ============================================================================

section TwistedRiemannRochAndPrym

/-- **Effective Degree-Zero Divisor Vanishing**:
    Any effective divisor ($D(P) \ge 0$ everywhere) on a finite support whose total degree
    $\sum_P D(P)$ vanishes is identically zero. This is the algebraic engine behind
    $H^0(\mathcal{B}, \mathcal{L}) = 0$ for every non-trivial $\mathcal{L} \in \mathrm{Pic}^0(\mathcal{B})$. -/
theorem effective_deg_zero_divisor_eq_zero {ι : Type*} [Fintype ι]
    (D : ι → ℤ) (heff : ∀ P : ι, 0 ≤ D P) (hdeg : ∑ P : ι, D P = 0) :
    D = 0 := by
  funext P
  exact (Finset.sum_eq_zero_iff_of_nonneg (fun Q _ => heff Q)).mp hdeg P (Finset.mem_univ P)

/-- Abstract Picard–Riemann–Roch–Serre-duality package on a smooth connected projective curve.
    Inhabited explicitly at genus $4$ with non-trivial $3$-torsion by `bringGenus4PicModel` below. -/
structure SmoothCurveRRData (Pic : Type*) [AddCommGroup Pic] where
  genus : ℕ
  deg : Pic →+ ℤ
  canonical : Pic
  h0 : Pic → ℕ
  h1 : Pic → ℕ
  deg_canonical : deg canonical = 2 * (genus : ℤ) - 2
  riemann_roch : ∀ D : Pic, (h0 D : ℤ) - (h1 D : ℤ) = deg D + 1 - (genus : ℤ)
  serre_duality : ∀ D : Pic, h1 D = h0 (canonical - D)
  h0_zero : h0 0 = 1
  h0_deg_zero_ne_zero : ∀ L : Pic, deg L = 0 → L ≠ 0 → h0 L = 0

/-- Concrete `h⁰` function on $\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ modeling the Picard
    sublattice $\mathbb{Z} \cdot P_0 \oplus \langle \mathcal{L} \rangle \subset \mathrm{Pic}(\mathcal{B})$
    of a genus-$4$ curve with a non-trivial $3$-torsion line bundle $\mathcal{L} = (0, 1)$. -/
def bringGenus4H0 (x : ℤ × ZMod 3) : ℕ :=
  if x.1 = 0 ∧ x.2 = 0 then 1
  else if x.1 = 6 ∧ x.2 = 0 then 4
  else (x.1 - 3).toNat

/-- **Explicit Non-Vacuity Witness (`genus = 4` with non-trivial $3$-torsion)**:
    Certifies constructively that `SmoothCurveRRData` is satisfiable at $g = 4$ with a genuine
    order-$3$ torsion element $(0, 1) \in \mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$. -/
def bringGenus4PicModel : SmoothCurveRRData (ℤ × ZMod 3) where
  genus := 4
  deg := AddMonoidHom.fst ℤ (ZMod 3)
  canonical := (6, 0)
  h0 := bringGenus4H0
  h1 := fun x => bringGenus4H0 ((6, 0) - x)
  deg_canonical := by simp
  riemann_roch := by
    rintro ⟨d, t⟩
    change (bringGenus4H0 (d, t) : ℤ) - (bringGenus4H0 (6 - d, -t) : ℤ) = d + 1 - 4
    unfold bringGenus4H0
    by_cases ht : t = 0
    · subst ht
      simp only [neg_zero, and_true]
      by_cases hd0 : d = 0
      · subst hd0; norm_num
      · by_cases hd6 : d = 6
        · subst hd6; norm_num
        · have h6d0 : 6 - d ≠ 0 := by omega
          have h6d6 : 6 - d ≠ 6 := by omega
          simp only [hd0, hd6, h6d0, h6d6, ↓reduceIte]
          omega
    · have hnt : -t ≠ 0 := neg_ne_zero.mpr ht
      simp only [ht, hnt, and_false, ↓reduceIte]
      omega
  serre_duality := fun _ => rfl
  h0_zero := by decide
  h0_deg_zero_ne_zero := by
    rintro ⟨d, t⟩ hd hne
    change d = 0 at hd
    subst hd
    have ht : t ≠ 0 := fun ht0 => hne (Prod.ext rfl ht0)
    simp [bringGenus4H0, ht]

/-- Every $n$-torsion class ($n \ge 1$) in `Pic` automatically has degree $0$ in $\mathbb{Z}$. -/
theorem deg_torsion_eq_zero {Pic : Type*} [AddCommGroup Pic]
    (C : SmoothCurveRRData Pic) {n : ℕ} (hn : n ≠ 0) {L : Pic} (htor : n • L = 0) :
    C.deg L = 0 := by
  have h := congrArg C.deg htor
  rw [map_nsmul, map_zero, nsmul_eq_mul] at h
  rcases mul_eq_zero.mp h with hn0 | hd0
  · exact absurd (Nat.cast_eq_zero.mp hn0) hn
  · exact hd0

/-- For any non-trivial $3$-torsion class ($3 \cdot L = 0, L \ne 0$), its inverse $2 \cdot L = -L$
    is also non-trivial ($2 \cdot L \ne 0$). -/
theorem two_nsmul_ne_zero_of_three_torsion {Pic : Type*} [AddCommGroup Pic]
    {L : Pic} (h3 : 3 • L = 0) (hne : L ≠ 0) :
    2 • L ≠ 0 := by
  intro h2
  apply hne
  calc L = 3 • L - 2 • L := by abel
    _ = 0 := by rw [h3, h2, sub_zero]

/-- **Serre Duality Vanishing of Twisted Canonical $H^1$**:
    For every non-trivial degree-$0$ class $L \ne 0$, $h^1(K + L) = h^0(-L) = 0$. -/
theorem h1_canonical_add_eq_zero {Pic : Type*} [AddCommGroup Pic]
    (C : SmoothCurveRRData Pic) {L : Pic} (hdeg : C.deg L = 0) (hne : L ≠ 0) :
    C.h1 (C.canonical + L) = 0 := by
  rw [C.serre_duality (C.canonical + L)]
  have hsub : C.canonical - (C.canonical + L) = -L := by abel
  rw [hsub]
  apply C.h0_deg_zero_ne_zero (-L)
  · rw [map_neg, hdeg, neg_zero]
  · exact neg_ne_zero.mpr hne

/-- **Twisted Canonical Riemann–Roch Zero-Mode Theorem**:
    On any curve of genus $g \ge 1$, twisting the canonical class $K$ by *any* non-trivial
    degree-$0$ class $L \ne 0$ yields $h^0(K + L) = g - 1$ and $h^1(K + L) = 0$. -/
theorem h0_canonical_add_eq_genus_sub_one {Pic : Type*} [AddCommGroup Pic]
    (C : SmoothCurveRRData Pic) (hg : 1 ≤ C.genus) {L : Pic}
    (hdeg : C.deg L = 0) (hne : L ≠ 0) :
    C.h0 (C.canonical + L) = C.genus - 1 ∧ C.h1 (C.canonical + L) = 0 := by
  have hh1 : C.h1 (C.canonical + L) = 0 := h1_canonical_add_eq_zero C hdeg hne
  have hrr := C.riemann_roch (C.canonical + L)
  rw [map_add, C.deg_canonical, hdeg, hh1] at hrr
  refine ⟨?_, hh1⟩
  omega

/-- **Untwisted Canonical Cohomology**:
    On any smooth connected projective curve of genus $g$, $h^0(K) = g$ and $h^1(K) = 1$. -/
theorem h0_h1_canonical_untwisted {Pic : Type*} [AddCommGroup Pic]
    (C : SmoothCurveRRData Pic) :
    C.h0 C.canonical = C.genus ∧ C.h1 C.canonical = 1 := by
  have hh1 : C.h1 C.canonical = 1 := by
    rw [C.serre_duality C.canonical, sub_self, C.h0_zero]
  have hrr := C.riemann_roch C.canonical
  rw [C.deg_canonical, hh1] at hrr
  refine ⟨?_, hh1⟩
  omega

/-- **Uniform Dolbeault Chiral Family Index**:
    For *every* degree-$0$ class $L$ (both trivial $L = 0$ and non-trivial $L \ne 0$),
    $h^0(K + L) - h^1(K + L) = g - 1$. -/
theorem dolbeault_index_canonical_twist_const {Pic : Type*} [AddCommGroup Pic]
    (C : SmoothCurveRRData Pic) {L : Pic} (hdeg : C.deg L = 0) :
    (C.h0 (C.canonical + L) : ℤ) - (C.h1 (C.canonical + L) : ℤ) = (C.genus : ℤ) - 1 := by
  have hrr := C.riemann_roch (C.canonical + L)
  rw [map_add, C.deg_canonical, hdeg] at hrr
  linarith

/-- **Honest Spin-Bundle Contrast (`2S = K` has Index Zero)**:
    For any untwisted theta characteristic / spinor bundle $S$ satisfying $2 \cdot S = K$
    ($\deg S = g - 1$) and any degree-$0$ flat bundle $L$, the chiral index
    $h^0(S + L) - h^1(S + L)$ vanishes identically. Thus a nonzero chiral generation count
    requires the canonical / Spin$^c$ Euler-flux twist $K = 2S$ ($\deg K = 2g - 2$). -/
theorem untwisted_spin_structure_zero_index {Pic : Type*} [AddCommGroup Pic]
    (C : SmoothCurveRRData Pic) {S L : Pic} (hspin : 2 • S = C.canonical)
    (hdegL : C.deg L = 0) :
    C.deg S = (C.genus : ℤ) - 1 ∧
    (C.h0 (S + L) : ℤ) - (C.h1 (S + L) : ℤ) = 0 := by
  have hdeg2S := congrArg C.deg hspin
  rw [map_nsmul, C.deg_canonical, nsmul_eq_mul] at hdeg2S
  have hdegS : C.deg S = (C.genus : ℤ) - 1 := by omega
  have hrr := C.riemann_roch (S + L)
  rw [map_add, hdegS, hdegL] at hrr
  exact ⟨hdegS, by omega⟩

/-- **Main Genus-$4$ Kummer–Prym–Riemann–Roch Decomposition (`10 = 4 + 3 + 3`)**:
    On any smooth genus-$4$ curve (in particular Bring's curve $\mathcal{B}$) equipped with
    *any* non-trivial $3$-torsion class $L \in \mathrm{Pic}(\mathcal{B})[3] \setminus \{0\}$:
    1. $\deg L = 0$, $\deg(2L) = 0$, and $2L \ne 0$ follow automatically;
    2. Untwisted sector ($t = 0$): $(h^0(K), h^1(K)) = (4, 1)$;
    3. Both colour-charged sectors ($t = 1, 2$): $(h^0(K + L), h^1(K + L)) = (3, 0)$ and
       $(h^0(K + 2L), h^1(K + 2L)) = (3, 0)$ — **unconditional $N_{\mathrm{gen}} = 3$ with zero
       anti-chiral mirror modes**;
    4. Chevalley–Weil sum on the unramified $\mathbb{Z}_3$-cover $\tilde{\mathcal{B}} \to \mathcal{B}$
       is $4 + 3 + 3 = 10 = \tilde{g}$, Prym cotangent dimension is $3 + 3 = 6$, and the net
       chiral index $h^0(K + kL) - h^1(K + kL) = 3$ holds for *every* $k \in \mathbb{N}$. -/
theorem bring_z3_prym_chevalley_weil_ten_split {Pic : Type*} [AddCommGroup Pic]
    (C : SmoothCurveRRData Pic) (hg4 : C.genus = 4) {L : Pic}
    (h3 : 3 • L = 0) (hne : L ≠ 0) :
    (C.deg L = 0 ∧ C.deg (2 • L) = 0 ∧ 2 • L ≠ 0) ∧
    (C.h0 C.canonical = 4 ∧ C.h1 C.canonical = 1) ∧
    (C.h0 (C.canonical + L) = 3 ∧ C.h1 (C.canonical + L) = 0) ∧
    (C.h0 (C.canonical + 2 • L) = 3 ∧ C.h1 (C.canonical + 2 • L) = 0) ∧
    C.h0 C.canonical + C.h0 (C.canonical + L) + C.h0 (C.canonical + 2 • L) = 10 ∧
    C.h0 (C.canonical + L) + C.h0 (C.canonical + 2 • L) = 6 ∧
    (∀ k : ℕ, (C.h0 (C.canonical + k • L) : ℤ) - (C.h1 (C.canonical + k • L) : ℤ) = 3) := by
  have hg1 : 1 ≤ C.genus := by omega
  have hdegL : C.deg L = 0 := deg_torsion_eq_zero C (by decide) h3
  have hdeg2L : C.deg (2 • L) = 0 := by rw [map_nsmul, hdegL, smul_zero]
  have h2ne : 2 • L ≠ 0 := two_nsmul_ne_zero_of_three_torsion h3 hne
  have huntw := h0_h1_canonical_untwisted C
  have htw1 := h0_canonical_add_eq_genus_sub_one C hg1 hdegL hne
  have htw2 := h0_canonical_add_eq_genus_sub_one C hg1 hdeg2L h2ne
  rw [hg4] at huntw htw1 htw2
  refine ⟨⟨hdegL, hdeg2L, h2ne⟩, huntw, htw1, htw2, by omega, by omega, ?_⟩
  intro k
  have hdegk : C.deg (k • L) = 0 := by rw [map_nsmul, hdegL, smul_zero]
  have hind := dolbeault_index_canonical_twist_const C hdegk
  rw [hg4] at hind
  omega

/-- Concrete instantiation on `bringGenus4PicModel` at $L = (0, 1)$, confirming end-to-end
    non-vacuous evaluation to $(4, 3, 3)$. -/
theorem bringGenus4PicModel_evaluates_to_4_3_3 :
    bringGenus4PicModel.h0 bringGenus4PicModel.canonical = 4 ∧
    bringGenus4PicModel.h1 bringGenus4PicModel.canonical = 1 ∧
    bringGenus4PicModel.h0 (bringGenus4PicModel.canonical + (0, 1)) = 3 ∧
    bringGenus4PicModel.h1 (bringGenus4PicModel.canonical + (0, 1)) = 0 ∧
    bringGenus4PicModel.h0 (bringGenus4PicModel.canonical + 2 • ((0, 1) : ℤ × ZMod 3)) = 3 ∧
    bringGenus4PicModel.h1 (bringGenus4PicModel.canonical + 2 • ((0, 1) : ℤ × ZMod 3)) = 0 := by
  decide

end TwistedRiemannRochAndPrym

-- ============================================================================
-- §2. Ascending vs Descending Cyclic Z_3 Covers of Genus 4 (Hurwitz + CW)
-- ============================================================================

section HurwitzAndChevalleyWeilDichotomy

/-- Riemann–Hurwitz relation for a prime-degree-$3$ cyclic Galois cover $\Sigma_{g_{\mathrm{top}}} \to \Sigma_{g_0}$
    branched (necessarily totally, $e_P = 3$) at $r$ points:
    $2 g_{\mathrm{top}} - 2 = 3(2 g_0 - 2) + 2 r$. -/
def CyclicZ3Hurwitz (gTop gBase r : ℕ) : Prop :=
  2 * (gTop : ℤ) - 2 = 3 * (2 * (gBase : ℤ) - 2) + 2 * (r : ℤ)

/-- **Case I (Ascending Étale $\mathbb{Z}_3$-Cover over Genus $4$)**:
    An unramified ($r = 0$) degree-$3$ cover $\tilde{\mathcal{B}} \to \mathcal{B}$ over $g(\mathcal{B}) = 4$
    has unique genus $\tilde{g} = 10$ ($\chi_{\mathrm{eu}}(\tilde{\mathcal{B}}) = -18 = 3 \cdot (-6)$). -/
theorem unramified_z3_over_bring_genus_ten (gTilde : ℕ) :
    CyclicZ3Hurwitz gTilde 4 0 ↔ gTilde = 10 := by
  unfold CyclicZ3Hurwitz
  omega

/-- **Case II (Complete Diophantine Classification of Descending $\mathbb{Z}_3$-Covers from Genus $4$)**:
    Any degree-$3$ cyclic Galois cover $\Sigma_4 \to \mathcal{B}_0$ *from* a genus-$4$ curve
    ($\chi_{\mathrm{eu}} = -6$) satisfies $3 g_0 + r = 6$, admitting **exclusively** the three
    pairs $(g_0, r) \in \{(2, 0), (1, 3), (0, 6)\}$:
    - $(2, 0)$: unramified cover over genus $2$ (Bring's actual free $C_3 \subset S_5$ quotient
      $\mathcal{B} \to \mathcal{C}_2$, `QOU.Brings.DescendingTower.free_quotient_genus`);
    - $(1, 3)$: cover of an elliptic curve branched at $3$ points;
    - $(0, 6)$: cyclic trigonal cover of $\mathbb{P}^1$ branched at $6$ points. -/
theorem descending_z3_from_genus4_solutions (gBase r : ℕ) :
    CyclicZ3Hurwitz 4 gBase r ↔
      (gBase = 2 ∧ r = 0) ∨ (gBase = 1 ∧ r = 3) ∨ (gBase = 0 ∧ r = 6) := by
  unfold CyclicZ3Hurwitz
  omega

/-- Division-free Chevalley–Weil triple `(3 * d₀, 3 * d₁, 3 * d₂)` for a connected cyclic
    $\mathbb{Z}_3$-cover over genus `gBase` with `m₁` branch points of local monodromy exponent `1`
    and `m₂` branch points of exponent `2` (`(m₁ + 2 * m₂) % 3 = 0`):
    $d_0 = g_0$, $3 d_1 = 3(g_0 - 1) + 2 m_1 + m_2$, $3 d_2 = 3(g_0 - 1) + m_1 + 2 m_2$
    (Chevalley–Weil 1934). -/
def cwZ3DimsScaled3 (gBase m1 m2 : ℕ) : ℤ × ℤ × ℤ :=
  (3 * (gBase : ℤ),
   3 * ((gBase : ℤ) - 1) + 2 * (m1 : ℤ) + (m2 : ℤ),
   3 * ((gBase : ℤ) - 1) + (m1 : ℤ) + 2 * (m2 : ℤ))

/-- **Exact Chevalley–Weil Sum Law & Integrality**:
    Under the $\mathbb{Z}_3$ branch-cycle sum rule `(m₁ + 2 * m₂) % 3 = 0`, all three
    Chevalley–Weil eigenspace dimensions are exact integers and their sum equals `gTop`
    whenever `CyclicZ3Hurwitz gTop gBase (m₁ + m₂)` holds. -/
theorem cwZ3Dims_sum_and_div3 {gTop gBase m1 m2 : ℕ}
    (hsum : (m1 + 2 * m2) % 3 = 0)
    (hrh : CyclicZ3Hurwitz gTop gBase (m1 + m2)) :
    let (s0, s1, s2) := cwZ3DimsScaled3 gBase m1 m2
    3 ∣ s0 ∧ 3 ∣ s1 ∧ 3 ∣ s2 ∧ s0 + s1 + s2 = 3 * (gTop : ℤ) := by
  unfold CyclicZ3Hurwitz at hrh
  dsimp only [cwZ3DimsScaled3]
  refine ⟨⟨gBase, rfl⟩, ?_, ?_, by omega⟩
  · refine ⟨(gBase : ℤ) - 1 + ((2 * m1 + m2) / 3 : ℕ), ?_⟩
    omega
  · refine ⟨(gBase : ℤ) - 1 + ((m1 + 2 * m2) / 3 : ℕ), ?_⟩
    omega

/-- **Complete Census & No-Go Theorem for Descending $\mathbb{Z}_3$-Covers of Genus $4$**:
    1. Across **every** descending cyclic $\mathbb{Z}_3$-cover $\Sigma_4 \to \mathcal{B}_0$
       (`gTop = 4`), $d_0 + d_1 + d_2 = 4$, so $(d_1, d_2) = (3, 3)$ (`(s₁, s₂) = (9, 9)`)
       is **strictly impossible** (`s₁ + s₂ ≤ 12 < 18`).
    2. Explicitly: $(2,0)$ gives $(d_0, d_1, d_2) = (2, 1, 1)$; $(1,3)$ gives $(1, 2, 1)$ or
       $(1, 1, 2)$; $(0,6)$ gives $(0, 3, 1)$, $(0, 2, 2)$, or $(0, 1, 3)$.
    3. Conversely, among unramified $\mathbb{Z}_3$-covers $\tilde{\Sigma} \to \Sigma_{g_0}$
       (`m₁ = m₂ = 0`), $(d_1, d_2) = (3, 3)$ holds **uniquely** at $g_0 = 4$ ($\tilde{g} = 10$). -/
theorem descending_z3_cannot_give_three_three :
    (∀ gBase m1 m2 : ℕ,
      (m1 + 2 * m2) % 3 = 0 →
      CyclicZ3Hurwitz 4 gBase (m1 + m2) →
      (cwZ3DimsScaled3 gBase m1 m2).2 ≠ (9, 9)) ∧
    cwZ3DimsScaled3 2 0 0 = (6, 3, 3) ∧
    cwZ3DimsScaled3 1 3 0 = (3, 6, 3) ∧
    cwZ3DimsScaled3 1 0 3 = (3, 3, 6) ∧
    cwZ3DimsScaled3 0 6 0 = (0, 9, 3) ∧
    cwZ3DimsScaled3 0 3 3 = (0, 6, 6) ∧
    cwZ3DimsScaled3 0 0 6 = (0, 3, 9) ∧
    (∀ gBase : ℕ, (cwZ3DimsScaled3 gBase 0 0).2 = (9, 9) ↔ gBase = 4) := by
  refine ⟨?_, rfl, rfl, rfl, rfl, rfl, rfl, ?_⟩
  · intro gBase m1 m2 _ hrh hcon
    unfold CyclicZ3Hurwitz at hrh
    simp only [cwZ3DimsScaled3, Prod.mk.injEq] at hcon
    omega
  · intro gBase
    simp only [cwZ3DimsScaled3, Nat.cast_zero, mul_zero, add_zero, Prod.mk.injEq]
    omega

end HurwitzAndChevalleyWeilDichotomy

-- ============================================================================
-- §3. Exact S_5 Normalizer of C_3 & F_3[S_5] Structure of Pic^0(B)[3]
-- ============================================================================

section S5NormalizerAndMod3Torsion

/-- Standard $3$-cycle $c_3 = (0\,1\,2) \in S_5 = \mathrm{Perm}(\mathrm{Fin}\ 5)$. -/
def c3Gen : Equiv.Perm (Fin 5) := Equiv.swap 0 1 * Equiv.swap 1 2

/-- Standard $5$-cycle $c_5 = (0\,1\,2\,3\,4) \in A_5 \subset S_5$. -/
def c5Gen : Equiv.Perm (Fin 5) :=
  Equiv.swap 0 1 * Equiv.swap 1 2 * Equiv.swap 2 3 * Equiv.swap 3 4

/-- **Exact Centralizer & Normalizer of $C_3 = \langle(0\,1\,2)\rangle$ in $S_5$**:
    1. $c_3$ has exact order $3$ and is even ($\mathrm{sgn}(c_3) = +1$);
    2. $|C_{S_5}(c_3)| = 6$ ($C_3 \times S_2$);
    3. $|N_{S_5}(\langle c_3 \rangle)| = 12$, and $N_{S_5}(\langle c_3 \rangle)$ coincides
       element-for-element with $S_3 \times S_2 = \{\sigma \in S_5 \mid \sigma(\{0,1,2\}) = \{0,1,2\}\}$. -/
theorem s5_centralizer_and_normalizer_of_c3 :
    c3Gen ^ 3 = 1 ∧ c3Gen ≠ 1 ∧ Equiv.Perm.sign c3Gen = 1 ∧
    (Finset.univ.filter (fun σ : Equiv.Perm (Fin 5) => σ * c3Gen = c3Gen * σ)).card = 6 ∧
    (Finset.univ.filter (fun σ : Equiv.Perm (Fin 5) =>
      σ * c3Gen * σ⁻¹ = c3Gen ∨ σ * c3Gen * σ⁻¹ = c3Gen ^ 2)).card = 12 ∧
    Finset.univ.filter (fun σ : Equiv.Perm (Fin 5) =>
      σ * c3Gen * σ⁻¹ = c3Gen ∨ σ * c3Gen * σ⁻¹ = c3Gen ^ 2) =
    Finset.univ.filter (fun σ : Equiv.Perm (Fin 5) =>
      ∀ i : Fin 5, (i.val < 3 ↔ (σ i).val < 3)) := by
  decide

/-- Left permutation action of $S_5$ on $(\mathrm{Fin}\ 5 \to R)$: $(\sigma \cdot v)_i = v_{\sigma^{-1}(i)}$. -/
def permVec {R : Type*} (σ : Equiv.Perm (Fin 5)) (v : Fin 5 → R) : Fin 5 → R :=
  fun i => v (σ⁻¹ i)

@[simp] theorem permVec_one {R : Type*} (v : Fin 5 → R) : permVec 1 v = v := by
  ext i; simp [permVec]

theorem permVec_mul {R : Type*} (σ τ : Equiv.Perm (Fin 5)) (v : Fin 5 → R) :
    permVec (σ * τ) v = permVec σ (permVec τ v) := by
  ext i; simp [permVec, _root_.mul_inv_rev]

/-- The $4$-dimensional $\mathbb{F}_3$-standard submodule
    $V_{\mathrm{std}}(\mathbb{F}_3) = \{v \in \mathbb{F}_3^5 \mid \sum_{i=0}^4 v_i = 0\}$ (`card = 81`). -/
def BringStdF3 : Submodule (ZMod 3) (Fin 5 → ZMod 3) where
  carrier := { v | ∑ i : Fin 5, v i = 0 }
  add_mem' {a b} ha hb := by
    change ∑ i : Fin 5, (a i + b i) = 0
    change ∑ i : Fin 5, a i = 0 at ha
    change ∑ i : Fin 5, b i = 0 at hb
    rw [Finset.sum_add_distrib, ha, hb, add_zero]
  zero_mem' := by simp
  smul_mem' c v hv := by
    change ∑ i : Fin 5, c * v i = 0
    change ∑ i : Fin 5, v i = 0 at hv
    rw [← Finset.mul_sum, hv, mul_zero]

/-- Induced $\mathbb{F}_3$-linear action of $S_5$ on `BringStdF3`. -/
def permActStdF3 (σ : Equiv.Perm (Fin 5)) : BringStdF3 →ₗ[ZMod 3] BringStdF3 where
  toFun v := ⟨permVec σ v.1, by
    change ∑ i : Fin 5, v.1 (σ⁻¹ i) = 0
    rw [Equiv.sum_comp σ⁻¹ v.1]
    exact v.2⟩
  map_add' _ _ := by ext i; rfl
  map_smul' _ _ := by ext i; rfl

/-- Root vector $e_0 - e_j \in V_{\mathrm{std}}(\mathbb{F}_3)$ for $j \ne 0$. -/
def rootStdF3 (j : Fin 5) (hj : j ≠ 0) : BringStdF3 :=
  ⟨fun k => if k = 0 then 1 else if k = j then -1 else 0, by
    change (∑ k : Fin 5, (if k = 0 then (1 : ZMod 3) else if k = j then -1 else 0)) = 0
    fin_cases j
    · exact absurd rfl hj
    · decide
    · decide
    · decide
    · decide⟩

private theorem zmod3_sq_eq_one_of_ne_zero {c : ZMod 3} (hc : c ≠ 0) : c * c = 1 := by
  fin_cases c
  · exact absurd rfl hc
  · rfl
  · rfl

private theorem zmod3_five_sum_eq_zero {x : ZMod 3}
    (h : x + x + x + x + x = 0) : x = 0 := by
  calc x = 2 * (x + x + x + x + x) - (9 : ZMod 3) * x := by ring
    _ = 0 := by rw [h, show (9 : ZMod 3) = 0 from by decide]; ring

private theorem zmod3_four_add_eq_zero {a b : ZMod 3}
    (h : a + a + a + a + b = 0) : b = 2 * a := by
  calc b = (a + a + a + a + b) - (6 : ZMod 3) * a + 2 * a := by ring
    _ = 2 * a := by rw [h, show (6 : ZMod 3) = 0 from by decide]; ring

private theorem zmod3_three_add_two_eq_zero {a b : ZMod 3}
    (h : a + a + a + b + b = 0) : b = 0 := by
  calc b = 2 * (a + a + a + b + b) - (6 : ZMod 3) * a - (3 : ZMod 3) * b := by ring
    _ = 0 := by
      rw [h, show (6 : ZMod 3) = 0 from by decide, show (3 : ZMod 3) = 0 from by decide]
      ring

private theorem zmod3_three_add_pair_eq_zero {a b c : ZMod 3}
    (h : a + a + a + b + c = 0) : c = -b := by
  calc c = (a + a + a + b + c) - (3 : ZMod 3) * a - b := by ring
    _ = -b := by rw [h, show (3 : ZMod 3) = 0 from by decide]; ring

/-- **Algebraic Simplicity of $V_{\mathrm{std}}(\mathbb{F}_3)$ as an $\mathbb{F}_3[S_5]$-Module**:
    Because $5 \equiv 2 \not\equiv 0 \pmod 3$, the mod-$3$ reduction $D^{(4,1)} = V_{\mathrm{std}}(\mathbb{F}_3)$
    of $H^0(\mathcal{B}, K_{\mathcal{B}})$ has **no** proper nonzero $S_5$-invariant submodule:
    every $S_5$-stable submodule $W \le V_{\mathrm{std}}(\mathbb{F}_3)$ satisfies $W = \bot \lor W = \top$. -/
theorem bringStdF3_simple_s5 (W : Submodule (ZMod 3) BringStdF3)
    (hW : ∀ (σ : Equiv.Perm (Fin 5)) {v : BringStdF3}, v ∈ W → permActStdF3 σ v ∈ W) :
    W = ⊥ ∨ W = ⊤ := by
  by_cases hbot : W = ⊥
  · exact Or.inl hbot
  · right
    obtain ⟨v, hvW, hv0⟩ := Submodule.exists_mem_ne_zero_of_ne_bot hbot
    -- Not all coordinates equal `v.1 0` since `5 = 2` is invertible in `ZMod 3`.
    have hnot_const : ¬ ∀ j : Fin 5, v.1 j = v.1 0 := by
      intro hconst
      apply hv0
      have hsum := v.2
      change ∑ i : Fin 5, v.1 i = 0 at hsum
      rw [Fin.sum_univ_five, hconst 1, hconst 2, hconst 3, hconst 4] at hsum
      have hv0_eq : v.1 0 = 0 := zmod3_five_sum_eq_zero hsum
      apply Subtype.ext
      funext j
      rw [hconst j, hv0_eq]
      rfl
    push_neg at hnot_const
    obtain ⟨j, hj_ne⟩ := hnot_const
    have hj0 : j ≠ 0 := fun h => hj_ne (congrArg v.1 h)
    set c : ZMod 3 := v.1 0 - v.1 j
    have hc0 : c ≠ 0 := sub_ne_zero.mpr hj_ne.symm
    -- `v - (0 j)·v = c • (e_0 - e_j) ∈ W`, hence `e_0 - e_j ∈ W`.
    have hdiff_mem : v - permActStdF3 (Equiv.swap 0 j) v ∈ W :=
      W.sub_mem hvW (hW (Equiv.swap 0 j) hvW)
    have hdiff_eq : v - permActStdF3 (Equiv.swap 0 j) v = c • rootStdF3 j hj0 := by
      apply Subtype.ext
      funext k
      simp only [Submodule.coe_sub, Submodule.coe_smul_of_tower, Pi.sub_apply, Pi.smul_apply,
        smul_eq_mul, permActStdF3, LinearMap.coe_mk, AddHom.coe_mk, permVec, Equiv.swap_inv,
        rootStdF3]
      by_cases hk0 : k = 0
      · subst hk0
        simp [Equiv.swap_apply_left, c]
      · by_cases hkj : k = j
        · subst hkj
          simp [hj0, Equiv.swap_apply_right, c]
        · simp [hk0, hkj, Equiv.swap_apply_of_ne_of_ne hk0 hkj]
    rw [hdiff_eq] at hdiff_mem
    have hroot_j : rootStdF3 j hj0 ∈ W := by
      have hcc := W.smul_mem c hdiff_mem
      rw [smul_smul, zmod3_sq_eq_one_of_ne_zero hc0, one_smul] at hcc
      exact hcc
    -- Transitivity of `S_4` on `{1,2,3,4}` puts every `rootStdF3 m` in `W`.
    have hroot_all : ∀ (m : Fin 5) (hm : m ≠ 0), rootStdF3 m hm ∈ W := by
      intro m hm
      by_cases hmj : m = j
      · subst hmj; exact hroot_j
      · have hact : permActStdF3 (Equiv.swap j m) (rootStdF3 j hj0) = rootStdF3 m hm := by
          apply Subtype.ext
          funext k
          simp only [permActStdF3, LinearMap.coe_mk, AddHom.coe_mk, permVec, Equiv.swap_inv,
            rootStdF3]
          by_cases hk0 : k = 0
          · subst hk0
            simp [Equiv.swap_apply_of_ne_of_ne hj0.symm hm.symm]
          · by_cases hkm : k = m
            · subst hkm
              simp [hm, hj0, Equiv.swap_apply_right]
            · by_cases hkj : k = j
              · subst hkj
                simp [hm, hmj, hk0, hkm, Equiv.swap_apply_left]
              · simp [Equiv.swap_apply_of_ne_of_ne hkj hkm, hk0, hkj, hkm]
        rw [← hact]
        exact hW (Equiv.swap j m) hroot_j
    -- Every `w ∈ BringStdF3` is a `ZMod 3`-linear combination of `rootStdF3 1..4`.
    rw [eq_top_iff]
    intro w _
    have hw_decomp : w =
        (-w.1 1) • rootStdF3 1 (by decide) +
        (-w.1 2) • rootStdF3 2 (by decide) +
        (-w.1 3) • rootStdF3 3 (by decide) +
        (-w.1 4) • rootStdF3 4 (by decide) := by
      have hsum := w.2
      change ∑ i : Fin 5, w.1 i = 0 at hsum
      rw [Fin.sum_univ_five] at hsum
      apply Subtype.ext
      funext k
      simp only [Submodule.coe_add, Submodule.coe_smul_of_tower, Pi.add_apply, Pi.smul_apply,
        smul_eq_mul, rootStdF3]
      fin_cases k
      · dsimp; linear_combination hsum
      · dsimp; ring
      · dsimp; ring
      · dsimp; ring
      · dsimp; ring
    rw [hw_decomp]
    exact W.add_mem
      (W.add_mem
        (W.add_mem (W.smul_mem _ (hroot_all 1 (by decide)))
                   (W.smul_mem _ (hroot_all 2 (by decide))))
        (W.smul_mem _ (hroot_all 3 (by decide))))
      (W.smul_mem _ (hroot_all 4 (by decide)))

/-- **Zero $C_5$-Fixed Points on $V_{\mathrm{std}}(\mathbb{F}_3)$**:
    The $5$-cycle $c_5 = (0\,1\,2\,3\,4) \in A_5$ fixes only $0 \in V_{\mathrm{std}}(\mathbb{F}_3)$. -/
theorem bringStdF3_c5_fixed_eq_zero {v : BringStdF3}
    (hv : permActStdF3 c5Gen v = v) :
    v = 0 := by
  have h1 := congrFun (congrArg Subtype.val hv) 1
  have h2 := congrFun (congrArg Subtype.val hv) 2
  have h3 := congrFun (congrArg Subtype.val hv) 3
  have h4 := congrFun (congrArg Subtype.val hv) 4
  simp only [permActStdF3, LinearMap.coe_mk, AddHom.coe_mk, permVec] at h1 h2 h3 h4
  have hc1 : c5Gen⁻¹ 1 = 0 := by decide
  have hc2 : c5Gen⁻¹ 2 = 1 := by decide
  have hc3 : c5Gen⁻¹ 3 = 2 := by decide
  have hc4 : c5Gen⁻¹ 4 = 3 := by decide
  rw [hc1] at h1; rw [hc2] at h2; rw [hc3] at h3; rw [hc4] at h4
  have h04 : v.1 0 = v.1 4 := h1.trans (h2.trans (h3.trans h4))
  have h14 : v.1 1 = v.1 4 := h2.trans (h3.trans h4)
  have h24 : v.1 2 = v.1 4 := h3.trans h4
  have hsum := v.2
  change ∑ i : Fin 5, v.1 i = 0 at hsum
  rw [Fin.sum_univ_five, h04, h14, h24, h4] at hsum
  have hv4 : v.1 4 = 0 := zmod3_five_sum_eq_zero hsum
  apply Subtype.ext
  funext k
  fin_cases k <;> simp [h04, h14, h24, h4, hv4]

/-- **Universal Left-Exactness of Fixed Points on Short Exact Sequences**:
    If $0 \to M_1 \xrightarrow{i} M \xrightarrow{p} M_2$ is $G$-equivariant and exact with
    $M_1^G = \{0\}$ and $M_2^G = \{0\}$, then $M^G = \{0\}$ — regardless of whether the
    extension splits. -/
theorem extension_fixed_eq_zero {G M₁ M M₂ : Type*}
    [AddZeroClass M₁] [AddZeroClass M] [AddZeroClass M₂]
    (act₁ : G → M₁ → M₁) (act : G → M → M) (act₂ : G → M₂ → M₂)
    (i : M₁ →+ M) (p : M →+ M₂)
    (hi : Function.Injective i)
    (hexact : ∀ x : M, p x = 0 → ∃ y : M₁, i y = x)
    (hcomm_i : ∀ (g : G) (y : M₁), i (act₁ g y) = act g (i y))
    (hcomm_p : ∀ (g : G) (x : M), p (act g x) = act₂ g (p x))
    (hfix₁ : ∀ y : M₁, (∀ g : G, act₁ g y = y) → y = 0)
    (hfix₂ : ∀ z : M₂, (∀ g : G, act₂ g z = z) → z = 0)
    {x : M} (hx : ∀ g : G, act g x = x) :
    x = 0 := by
  have hp0 : p x = 0 := hfix₂ (p x) (fun g => by rw [← hcomm_p g x, hx g])
  obtain ⟨y, rfl⟩ := hexact x hp0
  have hy0 : y = 0 := hfix₁ y (fun g => hi (by rw [hcomm_i g y, hx g]))
  rw [hy0, map_zero]

/-- **Unconditional $S_5$- and $A_5$-Breaking by Any Non-Trivial $3$-Torsion Kummer Bundle**:
    By Brauer–Nesbitt, every $S_5$-invariant integral lattice $H^1(\mathcal{B}, \mathbb{Z})$ in
    $H^1(\mathcal{B}, \mathbb{Q}) \cong V_{(4,1)}^{\oplus 2}$ reduces mod $3$ to an extension
    $0 \to V_{\mathrm{std}}(\mathbb{F}_3) \to M \to V_{\mathrm{std}}(\mathbb{F}_3) \to 0$.
    Every such module $M$ has **zero** non-trivial $c_5$-fixed, $A_5$-fixed, or $S_5$-fixed elements:
    choosing *any* $\mathcal{L} \in \mathrm{Pic}^0(\mathcal{B})[3] \setminus \{0\}$ necessarily
    breaks $S_5$ (and $A_5$). -/
theorem no_c5_a5_s5_fixed_in_any_pic3_extension {M : Type*} [AddCommGroup M]
    (act : Equiv.Perm (Fin 5) → M → M)
    (i : BringStdF3 →+ M) (p : M →+ BringStdF3)
    (hi : Function.Injective i)
    (hexact : ∀ x : M, p x = 0 → ∃ y : BringStdF3, i y = x)
    (hcomm_i : ∀ (σ : Equiv.Perm (Fin 5)) (y : BringStdF3), i (permActStdF3 σ y) = act σ (i y))
    (hcomm_p : ∀ (σ : Equiv.Perm (Fin 5)) (x : M), p (act σ x) = permActStdF3 σ (p x)) :
    (∀ x : M, act c5Gen x = x → x = 0) ∧
    (∀ x : M, (∀ σ : Equiv.Perm (Fin 5), Equiv.Perm.sign σ = 1 → act σ x = x) → x = 0) ∧
    (∀ x : M, (∀ σ : Equiv.Perm (Fin 5), act σ x = x) → x = 0) := by
  have hc5 : ∀ x : M, act c5Gen x = x → x = 0 := by
    intro x hx
    exact extension_fixed_eq_zero
      (G := Unit)
      (fun _ => permActStdF3 c5Gen) (fun _ => act c5Gen) (fun _ => permActStdF3 c5Gen)
      i p hi hexact
      (fun _ y => hcomm_i c5Gen y)
      (fun _ z => hcomm_p c5Gen z)
      (fun y hy => bringStdF3_c5_fixed_eq_zero (hy ()))
      (fun z hz => bringStdF3_c5_fixed_eq_zero (hz ()))
      (fun _ => hx)
  have hsign5 : Equiv.Perm.sign c5Gen = 1 := by decide
  exact ⟨hc5, fun x hx => hc5 x (hx c5Gen hsign5), fun x hx => hc5 x (hx c5Gen)⟩

private theorem vec_s4_apply (a : ZMod 3) (k : Fin 5) :
    (![a, a, a, a, 2 * a] : Fin 5 → ZMod 3) k = if k = 4 then 2 * a else a := by
  fin_cases k <;> simp

private theorem vec_s3xs2_apply (a : ZMod 3) (k : Fin 5) :
    (![a, a, a, 0, 0] : Fin 5 → ZMod 3) k = if k.val < 3 then a else 0 := by
  fin_cases k <;> simp

/-- **Exact Fixed-Subspace Characterization under $S_4$, $S_3 \times S_2$, and $C_3$ in $V_{\mathrm{std}}(\mathbb{F}_3)$**:
    1. $V_{\mathrm{std}}(\mathbb{F}_3)^{S_4}$ is $1$-dimensional (`card = 3`), spanned by `![1, 1, 1, 1, 2]`;
    2. $V_{\mathrm{std}}(\mathbb{F}_3)^{S_3 \times S_2}$ is $1$-dimensional (`card = 3`), spanned by `![1, 1, 1, 0, 0]`;
    3. $V_{\mathrm{std}}(\mathbb{F}_3)^{C_3}$ is $2$-dimensional (`card = 9`), consisting of `![a, a, a, b, -b]`;
    4. `Fintype.card BringStdF3 = 81` and `Fintype.card (BringStdF3 × BringStdF3) = 6561`
       (`8` non-trivial $S_4$-fixed and `8` non-trivial $(S_3 \times S_2)$-fixed $3$-torsion classes). -/
theorem bringStdF3_stabilizer_subspaces :
    (∀ v : BringStdF3,
      (∀ σ : Equiv.Perm (Fin 5), σ 4 = 4 → permActStdF3 σ v = v) ↔
        ∃ a : ZMod 3, v.1 = ![a, a, a, a, 2 * a]) ∧
    (∀ v : BringStdF3,
      (∀ σ : Equiv.Perm (Fin 5),
        (∀ i : Fin 5, i.val < 3 ↔ (σ i).val < 3) → permActStdF3 σ v = v) ↔
        ∃ a : ZMod 3, v.1 = ![a, a, a, 0, 0]) ∧
    (∀ v : BringStdF3,
      permActStdF3 c3Gen v = v ↔ ∃ a b : ZMod 3, v.1 = ![a, a, a, b, -b]) := by
  refine ⟨?_, ?_, ?_⟩
  · intro v
    constructor
    · intro hfix
      have h01 := congrFun (congrArg Subtype.val (hfix (Equiv.swap 0 1) (by decide))) 0
      have h02 := congrFun (congrArg Subtype.val (hfix (Equiv.swap 0 2) (by decide))) 0
      have h03 := congrFun (congrArg Subtype.val (hfix (Equiv.swap 0 3) (by decide))) 0
      simp only [permActStdF3, LinearMap.coe_mk, AddHom.coe_mk, permVec, Equiv.swap_inv,
        Equiv.swap_apply_left] at h01 h02 h03
      have hsum := v.2
      change ∑ i : Fin 5, v.1 i = 0 at hsum
      rw [Fin.sum_univ_five, h01, h02, h03] at hsum
      have hv4 : v.1 4 = 2 * v.1 0 := zmod3_four_add_eq_zero hsum
      refine ⟨v.1 0, ?_⟩
      ext k
      fin_cases k <;> simp [h01, h02, h03, hv4]
    · rintro ⟨a, ha⟩ σ hσ4
      have hinv4_iff : ∀ k : Fin 5, σ⁻¹ k = 4 ↔ k = 4 := by
        intro k
        constructor
        · intro h; simpa [hσ4] using congrArg σ h
        · rintro rfl; exact σ.injective (by simp [hσ4])
      apply Subtype.ext
      funext k
      simp only [permActStdF3, LinearMap.coe_mk, AddHom.coe_mk, permVec, ha, vec_s4_apply,
        hinv4_iff k]
  · intro v
    constructor
    · intro hfix
      have h01 := congrFun (congrArg Subtype.val (hfix (Equiv.swap 0 1) (by decide))) 0
      have h02 := congrFun (congrArg Subtype.val (hfix (Equiv.swap 0 2) (by decide))) 0
      have h34 := congrFun (congrArg Subtype.val (hfix (Equiv.swap 3 4) (by decide))) 3
      simp only [permActStdF3, LinearMap.coe_mk, AddHom.coe_mk, permVec, Equiv.swap_inv,
        Equiv.swap_apply_left] at h01 h02 h34
      have hsum := v.2
      change ∑ i : Fin 5, v.1 i = 0 at hsum
      rw [Fin.sum_univ_five, h01, h02, h34] at hsum
      have hv3 : v.1 3 = 0 := zmod3_three_add_two_eq_zero hsum
      have hv4 : v.1 4 = 0 := h34.trans hv3
      refine ⟨v.1 0, ?_⟩
      ext k
      fin_cases k <;> simp [h01, h02, hv3, hv4]
    · rintro ⟨a, ha⟩ σ hσ
      have hinv : ∀ i : Fin 5, (σ⁻¹ i).val < 3 ↔ i.val < 3 := by
        intro i
        simpa using hσ (σ⁻¹ i)
      apply Subtype.ext
      funext k
      simp only [permActStdF3, LinearMap.coe_mk, AddHom.coe_mk, permVec, ha, vec_s3xs2_apply,
        hinv k]
  · intro v
    constructor
    · intro hfix
      have h1 := congrFun (congrArg Subtype.val hfix) 1
      have h2 := congrFun (congrArg Subtype.val hfix) 2
      simp only [permActStdF3, LinearMap.coe_mk, AddHom.coe_mk, permVec] at h1 h2
      have hc1 : c3Gen⁻¹ 1 = 0 := by decide
      have hc2 : c3Gen⁻¹ 2 = 1 := by decide
      rw [hc1] at h1; rw [hc2] at h2
      have h01 : v.1 1 = v.1 0 := h1.symm
      have h02 : v.1 2 = v.1 0 := (h1.trans h2).symm
      have hsum := v.2
      change ∑ i : Fin 5, v.1 i = 0 at hsum
      rw [Fin.sum_univ_five, h01, h02] at hsum
      have hv4 : v.1 4 = -v.1 3 := zmod3_three_add_pair_eq_zero hsum
      refine ⟨v.1 0, v.1 3, ?_⟩
      ext k
      fin_cases k <;> simp [h01, h02, hv4]
    · rintro ⟨a, b, hab⟩
      have hc0 : c3Gen⁻¹ 0 = 2 := by decide
      have hc1 : c3Gen⁻¹ 1 = 0 := by decide
      have hc2 : c3Gen⁻¹ 2 = 1 := by decide
      have hc3 : c3Gen⁻¹ 3 = 3 := by decide
      have hc4 : c3Gen⁻¹ 4 = 4 := by decide
      apply Subtype.ext
      funext k
      fin_cases k <;>
        simp [permActStdF3, permVec, hc0, hc1, hc2, hc3, hc4, hab]

end S5NormalizerAndMod3Torsion

-- ============================================================================
-- §4. Central Z(SU(3)) Kummer Twist on Λ¹F ⊕ Λ²F*, Anomalies, & S_5 → S_4 Pairing
-- ============================================================================

section ExteriorFermionsAnomaliesAndLeptonPairing

/-- The five left-handed Weyl multiplets of $\Lambda^1 F \oplus \Lambda^2 F^*$
    ($F = W_2(y_2) \oplus W_3^*(y_3)$). -/
inductive ExteriorWeylMultiplet : Type
  | leptonDoubletL   -- L_L = (2, 1)_{y_2} ∈ Λ¹ F
  | chargedLeptonRc  -- e_R^c = (1, 1)_{-2 y_2} = Λ² W_2*
  | downQuarkRc      -- d_R^c = (1, 3*)_{y_3} ∈ Λ¹ F
  | quarkDoubletL    -- Q_L = (2, 3)_{-y_2 - y_3} = W_2* ⊗ W_3
  | upQuarkRc        -- u_R^c = (1, 3*)_{-2 y_3} = Λ² W_3
  deriving DecidableEq

instance : Fintype ExteriorWeylMultiplet :=
  Fintype.ofList [.leptonDoubletL, .chargedLeptonRc, .downQuarkRc, .quarkDoubletL, .upQuarkRc]
    (fun x => by cases x <;> simp)

/-- $\mathrm{SU}(3)_c$ $(a, b)$-tensor type (`a` fundamentals, `b` antifundamentals) determining
    each multiplet's central $Z(\mathrm{SU}(3)_c) \cong \mu_3$ Kummer twist $\mathcal{L}^{t(m)}$
    via `QOU.Eightfold.TrialitySelectionRule.triality`. -/
def multipletColourType : ExteriorWeylMultiplet → ℕ × ℕ
  | .leptonDoubletL  => (0, 0)
  | .chargedLeptonRc => (0, 0)
  | .downQuarkRc     => (0, 1)
  | .quarkDoubletL   => (1, 0)
  | .upQuarkRc       => (2, 0)

/-- Weyl state multiplicity per generation ($2 + 1 + 3 + 6 + 3 = 15$). -/
def multipletWeylDim : ExteriorWeylMultiplet → ℕ
  | .leptonDoubletL  => 2
  | .chargedLeptonRc => 1
  | .downQuarkRc     => 3
  | .quarkDoubletL   => 6
  | .upQuarkRc       => 3

/-- **Central $Z(\mathrm{SU}(3)_c)$ Triality Grading of $\Lambda^1 F \oplus \Lambda^2 F^*$**:
    Under `triality` (`ZMod 3`), both lepton multiplets ($L_L, e_R^c$) have triality $0$
    (untwisted $\mathcal{O}_{\mathcal{B}}$), $Q_L$ has triality $1 \ne 0$ ($\mathcal{L}$),
    both anti-quark singlets ($d_R^c, u_R^c$) have triality $2 \ne 0$ ($\mathcal{L}^2$), and
    total Weyl dimension per generation is $15$. -/
theorem exterior_multiplet_triality_and_dim :
    (let p := multipletColourType .leptonDoubletL;  triality p.1 p.2 = 0) ∧
    (let p := multipletColourType .chargedLeptonRc; triality p.1 p.2 = 0) ∧
    (let p := multipletColourType .quarkDoubletL;   triality p.1 p.2 = 1) ∧
    (let p := multipletColourType .downQuarkRc;     triality p.1 p.2 = 2) ∧
    (let p := multipletColourType .upQuarkRc;       triality p.1 p.2 = 2) ∧
    (∑ m : ExteriorWeylMultiplet, multipletWeylDim m) = 15 := by
  decide

/-- Twice the mixed strong-hypercharge anomaly $2\mathcal{A}_{[\mathrm{SU}(3)_c]^2 \mathrm{U}(1)_Y}$
    for $N_q$ chiral quark families. -/
def anomSU3SqU1 {R : Type*} [CommRing R] (Nq : ℤ) (y2 y3 : R) : R :=
  (Nq : R) * (2 * (-y2 - y3) + y3 + (-2 * y3))

/-- Twice the mixed weak-hypercharge anomaly $2\mathcal{A}_{[\mathrm{SU}(2)_L]^2 \mathrm{U}(1)_Y}$
    for $N_q$ chiral quark families and $N_\ell$ chiral lepton families. -/
def anomSU2SqU1 {R : Type*} [CommRing R] (Nq Nl : ℤ) (y2 y3 : R) : R :=
  (Nl : R) * y2 + (Nq : R) * (3 * (-y2 - y3))

/-- Mixed gravitational-hypercharge trace $\mathrm{Tr}(Y) = \mathcal{A}_{[\mathrm{grav}]^2 \mathrm{U}(1)_Y}$. -/
def anomGravSqU1 {R : Type*} [CommRing R] (Nq Nl : ℤ) (y2 y3 : R) : R :=
  (Nl : R) * (2 * y2 + (-2 * y2)) +
    (Nq : R) * (3 * y3 + 6 * (-y2 - y3) + 3 * (-2 * y3))

/-- Cubic hypercharge trace $\mathrm{Tr}(Y^3) = \mathcal{A}_{[\mathrm{U}(1)_Y]^3}$. -/
def anomU1Cubic {R : Type*} [CommRing R] (Nq Nl : ℤ) (y2 y3 : R) : R :=
  (Nl : R) * (2 * y2 ^ 3 + (-2 * y2) ^ 3) +
    (Nq : R) * (3 * y3 ^ 3 + 6 * (-y2 - y3) ^ 3 + 3 * (-2 * y3) ^ 3)

/-- **Exact Division-Free 4D Anomaly Factorisation on $\Lambda^1 F \oplus \Lambda^2 F^*$**:
    Over *any* `[CommRing R]`, whenever $F = W_2(y_2) \oplus W_3^*(y_3)$ satisfies the
    tracelessness / unimodularity relation $2 y_2 + 3 y_3 = 0$:
    1. $2\mathcal{A}_{[\mathrm{SU}(3)_c]^2 \mathrm{U}(1)_Y} = 0$ identically for all $N_q$;
    2. $\mathrm{Tr}(Y) = 0$ identically for all $(N_q, N_\ell)$;
    3. $2\mathcal{A}_{[\mathrm{SU}(2)_L]^2 \mathrm{U}(1)_Y} = (N_\ell - N_q) y_2$;
    4. $9\mathcal{A}_{[\mathrm{U}(1)_Y]^3} = 54 (N_q - N_\ell) y_2^3$. -/
theorem exterior_su5_anomaly_identities {R : Type*} [CommRing R]
    (Nq Nl : ℤ) {y2 y3 : R} (htr : 2 * y2 + 3 * y3 = 0) :
    anomSU3SqU1 Nq y2 y3 = 0 ∧
    anomGravSqU1 Nq Nl y2 y3 = 0 ∧
    anomSU2SqU1 Nq Nl y2 y3 = ((Nl : R) - (Nq : R)) * y2 ∧
    9 * anomU1Cubic Nq Nl y2 y3 = 54 * ((Nq : R) - (Nl : R)) * y2 ^ 3 := by
  unfold anomSU3SqU1 anomGravSqU1 anomSU2SqU1 anomU1Cubic
  refine ⟨?_, ?_, ?_, ?_⟩
  · linear_combination -(Nq : R) * htr
  · linear_combination -3 * (Nq : R) * htr
  · linear_combination -(Nq : R) * htr
  · linear_combination
      (Nq : R) * (-9 * (2 * y2 + 3 * y3) ^ 2 + 36 * (2 * y2 + 3 * y3) * y2 - 90 * y2 ^ 2) * htr

/-- **Anomaly Matching & Refutation of the Naive $H^0$-Only $(3, 4)$ Truncation**:
    Over any integral domain `[CommRing R] [IsDomain R]` with `y₂ ≠ 0` and `2 y₂ + 3 y₃ = 0`:
    1. $\mathcal{A}_{[\mathrm{SU}(2)_L]^2 \mathrm{U}(1)_Y} = 0 \iff (N_\ell : R) = (N_q : R)$;
    2. Keeping $H^0$ alone (`(N_q, N_ℓ) = (3, 4)`) violates $[\mathrm{SU}(2)_L]^2 \mathrm{U}(1)_Y$
       ($= y_2 \ne 0$) **and** violates Witten's $\mathrm{SU}(2)_L$ global $\mathbb{Z}_2$ doublet
       parity ($4 + 3 \cdot 3 = 13$ is odd);
    3. Retaining the full Dolbeault chiral index (`N_q = 3 - 0 = 3`, `N_ℓ = 4 - 1 = 3`) cancels
       all four perturbative anomalies identically and has even $\mathrm{SU}(2)_L$ doublet count $12$. -/
theorem anomaly_matching_and_h0_only_refutation {R : Type*} [CommRing R] [IsDomain R]
    {y2 y3 : R} (hy2 : y2 ≠ 0) (htr : 2 * y2 + 3 * y3 = 0) :
    (∀ Nq Nl : ℤ, anomSU2SqU1 Nq Nl y2 y3 = 0 ↔ (Nl : R) = (Nq : R)) ∧
    anomSU2SqU1 3 4 y2 y3 ≠ 0 ∧
    ¬ Even (4 + 3 * 3 : ℕ) ∧
    anomSU3SqU1 3 y2 y3 = 0 ∧
    anomGravSqU1 3 3 y2 y3 = 0 ∧
    anomSU2SqU1 3 3 y2 y3 = 0 ∧
    9 * anomU1Cubic 3 3 y2 y3 = 0 ∧
    Even (3 + 3 * 3 : ℕ) := by
  refine ⟨?_, ?_, by decide, ?_, ?_, ?_, ?_, by decide⟩
  · intro Nq Nl
    rw [(exterior_su5_anomaly_identities Nq Nl htr).2.2.1, mul_eq_zero, or_iff_left hy2, sub_eq_zero]
  · rw [(exterior_su5_anomaly_identities 3 4 htr).2.2.1]
    have h1 : (((4 : ℤ) : R) - ((3 : ℤ) : R)) * y2 = y2 := by push_cast; ring
    rw [h1]
    exact hy2
  · exact (exterior_su5_anomaly_identities 3 3 htr).1
  · exact (exterior_su5_anomaly_identities 3 3 htr).2.1
  · rw [(exterior_su5_anomaly_identities 3 3 htr).2.2.1]; ring
  · rw [(exterior_su5_anomaly_identities 3 3 htr).2.2.2]; ring

/-! ### Module-Level $S_5$ Chiral Protection vs $S_4$ Vector-Like Lepton Decoupling -/

/-- Bring's $4$-dimensional canonical differential space $V_{\mathrm{std}}(F) = \{\sum_{i=0}^4 x_i = 0\}$
    as an $F$-submodule of `Fin 5 → F` over any `[Field F]`. -/
def BringStdSubmodule (F : Type*) [Field F] : Submodule F (Fin 5 → F) where
  carrier := { x | ∑ i : Fin 5, x i = 0 }
  add_mem' {a b} ha hb := by
    change ∑ i : Fin 5, (a i + b i) = 0
    change ∑ i : Fin 5, a i = 0 at ha
    change ∑ i : Fin 5, b i = 0 at hb
    rw [Finset.sum_add_distrib, ha, hb, add_zero]
  zero_mem' := by simp
  smul_mem' c x hx := by
    change ∑ i : Fin 5, c * x i = 0
    change ∑ i : Fin 5, x i = 0 at hx
    rw [← Finset.mul_sum, hx, mul_zero]

/-- $F$-linear $S_5$ permutation action on `BringStdSubmodule F`. -/
def permActStd {F : Type*} [Field F] (σ : Equiv.Perm (Fin 5)) :
    BringStdSubmodule F →ₗ[F] BringStdSubmodule F where
  toFun x := ⟨permVec σ x.1, by
    change ∑ i : Fin 5, x.1 (σ⁻¹ i) = 0
    rw [Equiv.sum_comp σ⁻¹ x.1]
    exact x.2⟩
  map_add' _ _ := by ext i; rfl
  map_smul' _ _ := by ext i; rfl

/-- The $S_4$-invariant vector `(1, 1, 1, 1, -4) ∈ BringStdSubmodule F`. -/
def singletStd (F : Type*) [Field F] : BringStdSubmodule F :=
  ⟨![1, 1, 1, 1, -4], by
    change ∑ i : Fin 5, (![1, 1, 1, 1, -4] : Fin 5 → F) i = 0
    rw [Fin.sum_univ_five]
    dsimp
    ring⟩

/-- Canonical $S_4$-invariant linear functional `x ↦ x 4` on `BringStdSubmodule F`. -/
def evalFourStd (F : Type*) [Field F] : BringStdSubmodule F →ₗ[F] F where
  toFun x := x.1 4
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

/-- Root basis `e_j - e_4` ($j \in \{0,1,2,3\}$) of `BringStdSubmodule F`. -/
def stdBasisVec (F : Type*) [Field F] (j : Fin 4) : BringStdSubmodule F :=
  let j5 : Fin 5 := ⟨j.val, by omega⟩
  ⟨fun k => if k = j5 then 1 else if k = 4 then -1 else 0, by
    change (∑ k : Fin 5, (if k = j5 then (1 : F) else if k = 4 then -1 else 0)) = 0
    rw [Fin.sum_univ_five]
    fin_cases j <;> simp [j5]⟩

/-- Decomposition of any `x ∈ BringStdSubmodule F` in `stdBasisVec F`. -/
theorem eq_sum_stdBasisVec {F : Type*} [Field F] (x : BringStdSubmodule F) :
    x = ∑ j : Fin 4, (x.1 ⟨j.val, by omega⟩) • stdBasisVec F j := by
  have hsum := x.2
  change ∑ i : Fin 5, x.1 i = 0 at hsum
  rw [Fin.sum_univ_five] at hsum
  apply Subtype.ext
  funext k
  simp only [Fin.sum_univ_four, stdBasisVec]
  fin_cases k
  · simp
  · simp
  · simp
  · simp
  · dsimp; linear_combination hsum

/-- Exact dimension `Module.finrank F (BringStdSubmodule F) = 4`. -/
theorem finrank_bringStdSubmodule (F : Type*) [Field F] :
    Module.finrank F (BringStdSubmodule F) = 4 := by
  have hli : LinearIndependent F (stdBasisVec F) := by
    rw [Fintype.linearIndependent_iff]
    intro c hc i
    have hi := congrFun (congrArg Subtype.val hc) ⟨i.val, by omega⟩
    simp only [Submodule.coe_zero, Pi.zero_apply, Fin.sum_univ_four, stdBasisVec] at hi
    fin_cases i <;> simpa using hi
  have hspan : Submodule.span F (Set.range (stdBasisVec F)) = ⊤ := by
    rw [eq_top_iff]
    intro x _
    rw [eq_sum_stdBasisVec x]
    exact Submodule.sum_mem _ fun j _ =>
      Submodule.smul_mem _ _ (Submodule.subset_span ⟨j, rfl⟩)
  rw [Module.finrank_eq_card_basis (Module.Basis.mk hli hspan.ge), Fintype.card_fin]

/-- **$S_5$ Chiral Protection vs $S_4$ Vector-Like Lepton Decoupling Theorem**:
    Over any `[Field F]` with `(2 : F) ≠ 0`, modelling $H^0(\mathcal{B}, K_{\mathcal{B}}) \cong V_{\mathrm{std}}(F)$
    and $H^1(\mathcal{B}, K_{\mathcal{B}}) \cong F_{\mathrm{triv}}$:
    1. **Unbroken $S_5$ protects the 4th lepton mode**: every $S_5$-invariant linear pairing
       $\Phi : V_{\mathrm{std}}(F) \toₗ[F] F$ vanishes identically ($\Phi = 0$).
    2. **$S_5 \to S_4$ breaking (forced by $\mathcal{L} \ne 0$, §3) unlocks a unique pairing**:
       every $S_4$-invariant $\Phi : V_{\mathrm{std}}(F) \toₗ[F] F$ satisfies
       $\Phi(x) = -(x_4 / 4)\,\Phi(\mathrm{singletStd})$, and `evalFourStd` is a concrete nonzero
       $S_4$-invariant pairing.
    3. **Exact $3$-generation chiral lepton kernel**: whenever an $S_4$-invariant pairing $\Phi$
       is nonzero on `singletStd F` ($M_{\mathrm{vec}} \ne 0$), $\ker \Phi = \{x \in V_{\mathrm{std}}(F) \mid x_4 = 0\}$
       has exact dimension `Module.finrank F (LinearMap.ker Φ) = 3`. -/
theorem s5_protects_fourth_lepton_s4_unlocks_pairing {F : Type*} [Field F]
    (h2 : (2 : F) ≠ 0) :
    (∀ Φ : BringStdSubmodule F →ₗ[F] F,
      (∀ (σ : Equiv.Perm (Fin 5)) (x : BringStdSubmodule F), Φ (permActStd σ x) = Φ x) →
      Φ = 0) ∧
    (∀ (σ : Equiv.Perm (Fin 5)) (x : BringStdSubmodule F),
      σ 4 = 4 → evalFourStd F (permActStd σ x) = evalFourStd F x) ∧
    evalFourStd F (singletStd F) ≠ 0 ∧
    (∀ Φ : BringStdSubmodule F →ₗ[F] F,
      (∀ (σ : Equiv.Perm (Fin 5)) (x : BringStdSubmodule F),
        σ 4 = 4 → Φ (permActStd σ x) = Φ x) →
      (∀ x : BringStdSubmodule F, Φ x = -(x.1 4 / 4) * Φ (singletStd F)) ∧
      (Φ (singletStd F) ≠ 0 →
        (∀ x : BringStdSubmodule F, x ∈ LinearMap.ker Φ ↔ x.1 4 = 0) ∧
        Module.finrank F (LinearMap.ker Φ) = 3)) := by
  have h4 : (4 : F) ≠ 0 := by
    have : (4 : F) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  refine ⟨?_, ?_, ?_, ?_⟩
  · -- Part 1: `Hom_{S_5}(V_std, F) = 0`.
    intro Φ hΦ
    have hbasis_zero : ∀ j : Fin 4, Φ (stdBasisVec F j) = 0 := by
      intro j
      let j5 : Fin 5 := ⟨j.val, by omega⟩
      have hj4 : j5 ≠ 4 := by
        intro h
        have hv := congrArg Fin.val h
        simp [j5] at hv
        omega
      have hneg : permActStd (Equiv.swap j5 4) (stdBasisVec F j) = -stdBasisVec F j := by
        apply Subtype.ext
        funext k
        simp only [permActStd, LinearMap.coe_mk, AddHom.coe_mk, Submodule.coe_neg, Pi.neg_apply,
          permVec, Equiv.swap_inv, stdBasisVec]
        change (if (Equiv.swap j5 4) k = j5 then (1 : F) else if (Equiv.swap j5 4) k = 4 then -1 else 0) =
          -(if k = j5 then (1 : F) else if k = 4 then -1 else 0)
        by_cases hkj : k = j5
        · subst hkj; simp [hj4.symm, Equiv.swap_apply_left]
        · by_cases hk4 : k = 4
          · subst hk4; simp [hj4.symm, Equiv.swap_apply_right]
          · simp [Equiv.swap_apply_of_ne_of_ne hkj hk4, hkj, hk4]
      have heq := hΦ (Equiv.swap j5 4) (stdBasisVec F j)
      rw [hneg, map_neg] at heq
      have h2z : 2 * Φ (stdBasisVec F j) = 0 := by linear_combination -heq
      exact (mul_eq_zero.mp h2z).resolve_left h2
    ext x
    rw [eq_sum_stdBasisVec x, map_sum]
    simp [hbasis_zero]
  · -- Part 2a: `evalFourStd` is `S_4`-invariant.
    intro σ x hσ4
    have hinv4 : σ⁻¹ 4 = 4 := σ.injective (by simp [hσ4])
    simp [evalFourStd, permActStd, permVec, hinv4]
  · -- Part 2b: `evalFourStd (singletStd F) = -4 ≠ 0`.
    simp only [evalFourStd, LinearMap.coe_mk, AddHom.coe_mk, singletStd]
    change (-4 : F) ≠ 0
    exact neg_ne_zero.mpr h4
  · -- Part 3: Uniqueness up to scale & `finrank (ker Φ) = 3`.
    intro Φ hΦ
    -- For `j ∈ {0,1,2}`, `e_j - e_3` is negated by `swap j 3 ∈ S_4`.
    let root3 : Fin 3 → BringStdSubmodule F := fun j =>
      let j5 : Fin 5 := ⟨j.val, by omega⟩
      ⟨fun k => if k = j5 then 1 else if k = 3 then -1 else 0, by
        change (∑ k : Fin 5, (if k = j5 then (1 : F) else if k = 3 then -1 else 0)) = 0
        rw [Fin.sum_univ_five]
        fin_cases j <;> simp [j5]⟩
    have hroot3_zero : ∀ j : Fin 3, Φ (root3 j) = 0 := by
      intro j
      let j5 : Fin 5 := ⟨j.val, by omega⟩
      have hj3 : j5 ≠ 3 := by
        intro h
        have hv := congrArg Fin.val h
        simp [j5] at hv
        omega
      have hfix4 : (Equiv.swap j5 3 : Equiv.Perm (Fin 5)) 4 = 4 := by
        fin_cases j <;> decide
      have hneg : permActStd (Equiv.swap j5 3) (root3 j) = -root3 j := by
        apply Subtype.ext
        funext k
        simp only [permActStd, LinearMap.coe_mk, AddHom.coe_mk, Submodule.coe_neg, Pi.neg_apply,
          permVec, Equiv.swap_inv, root3]
        change (if (Equiv.swap j5 3) k = j5 then (1 : F) else if (Equiv.swap j5 3) k = 3 then -1 else 0) =
          -(if k = j5 then (1 : F) else if k = 3 then -1 else 0)
        by_cases hkj : k = j5
        · subst hkj; simp [hj3.symm, Equiv.swap_apply_left]
        · by_cases hk3 : k = 3
          · subst hk3; simp [hj3.symm, Equiv.swap_apply_right]
          · simp [Equiv.swap_apply_of_ne_of_ne hkj hk3, hkj, hk3]
      have heq := hΦ (Equiv.swap j5 3) (root3 j) hfix4
      rw [hneg, map_neg] at heq
      have h2z : 2 * Φ (root3 j) = 0 := by linear_combination -heq
      exact (mul_eq_zero.mp h2z).resolve_left h2
    have hformula : ∀ x : BringStdSubmodule F, Φ x = -(x.1 4 / 4) * Φ (singletStd F) := by
      intro x
      have hx_decomp : x =
          (-(x.1 4 / 4)) • singletStd F +
          (x.1 0 + x.1 4 / 4) • root3 0 +
          (x.1 1 + x.1 4 / 4) • root3 1 +
          (x.1 2 + x.1 4 / 4) • root3 2 := by
        have hsum := x.2
        change ∑ i : Fin 5, x.1 i = 0 at hsum
        rw [Fin.sum_univ_five] at hsum
        apply Subtype.ext
        funext k
        simp only [Submodule.coe_add, Submodule.coe_smul_of_tower, Pi.add_apply, Pi.smul_apply,
          smul_eq_mul, singletStd, root3]
        fin_cases k
        · dsimp; field_simp [h4]; ring
        · dsimp; field_simp [h4]; ring
        · dsimp; field_simp [h4]; ring
        · dsimp; field_simp [h4]; linear_combination 4 * hsum
        · dsimp; field_simp [h4]; ring
      conv_lhs => rw [hx_decomp]
      simp [hroot3_zero]
    refine ⟨hformula, ?_⟩
    intro hm
    have hker : ∀ x : BringStdSubmodule F, x ∈ LinearMap.ker Φ ↔ x.1 4 = 0 := by
      intro x
      rw [LinearMap.mem_ker, hformula x, mul_eq_zero, or_iff_left hm, neg_eq_zero,
        div_eq_zero_iff, or_iff_left h4]
    refine ⟨hker, ?_⟩
    have hsurj : Function.Surjective Φ := by
      intro y
      refine ⟨(y / Φ (singletStd F)) • singletStd F, ?_⟩
      rw [map_smul, smul_eq_mul, div_mul_cancel₀ y hm]
    have hrange : Module.finrank F (LinearMap.range Φ) = 1 := by
      rw [LinearMap.range_eq_top.mpr hsurj, finrank_top, Module.finrank_self]
    have hrn := LinearMap.finrank_range_add_finrank_ker Φ
    rw [finrank_bringStdSubmodule F, hrange] at hrn
    omega

/-- **Rule-13a Conditional Closure Carrier (Zero Instances)**:
    Packages the three physical inputs not derived by pure curve kinematics alone:
    (i) internal fermions couple to the topologically twisted canonical bundle `C.canonical`
        on a genus-$4$ curve (`C.genus = 4`) rather than an untwisted spin bundle;
    (ii) colour triality twists by a non-trivial $3$-torsion class `L` (`3 • L = 0`, `L ≠ 0`);
    (iii) in the untwisted colour-singlet lepton sector (`h0 = 4`, `h1 = 1`), the symmetry-unlocked
          vector-like Dirac mass pairing `leptonDiracPairing : H0Lep →ₗ[F] H1Lep` is surjective
          (`M_vec ≠ 0`, Georgi survival hypothesis).
    Deliberately uninstantiated per Rule 13a. -/
class BringKummerGenerationClosureHypothesis (Pic : Type*) [AddCommGroup Pic]
    (F : Type*) [Field F]
    (H0Lep H1Lep : Type*) [AddCommGroup H0Lep] [Module F H0Lep] [FiniteDimensional F H0Lep]
    [AddCommGroup H1Lep] [Module F H1Lep] [FiniteDimensional F H1Lep] where
  curve : SmoothCurveRRData Pic
  genus_eq_four : curve.genus = 4
  kummerClass : Pic
  three_torsion : 3 • kummerClass = 0
  kummer_nontrivial : kummerClass ≠ 0
  finrank_h0_lep : Module.finrank F H0Lep = curve.h0 curve.canonical
  finrank_h1_lep : Module.finrank F H1Lep = curve.h1 curve.canonical
  leptonDiracPairing : H0Lep →ₗ[F] H1Lep
  leptonDiracPairing_surjective : Function.Surjective leptonDiracPairing

/-- **Conditional Full Three-Generation Theorem (`N_gen(quark) = N_gen(lepton) = 3`)**:
    Under `BringKummerGenerationClosureHypothesis`, none of whose fields assumes the number `3`:
    - Riemann–Roch + Serre duality derive `h⁰(K + L) = 3, h¹(K + L) = 0` ($Q_L$, triality $1$)
      and `h⁰(K + 2L) = 3, h¹(K + 2L) = 0` ($u_R^c, d_R^c$, triality $2$);
    - Untwisted Riemann–Roch + Serre duality (`h⁰(K) = 4, h¹(K) = 1`) combined with rank-nullity
      on `leptonDiracPairing` derive `Module.finrank F (LinearMap.ker leptonDiracPairing) = 3`
      for the surviving massless chiral lepton families ($L_L, e_R^c$, triality $0$). -/
theorem quark_and_lepton_generations_eq_three_of_closure
    {Pic : Type*} [AddCommGroup Pic] {F : Type*} [Field F]
    {H0Lep H1Lep : Type*} [AddCommGroup H0Lep] [Module F H0Lep] [FiniteDimensional F H0Lep]
    [AddCommGroup H1Lep] [Module F H1Lep] [FiniteDimensional F H1Lep]
    [ctx : BringKummerGenerationClosureHypothesis Pic F H0Lep H1Lep] :
    ctx.curve.h0 (ctx.curve.canonical + ctx.kummerClass) = 3 ∧
    ctx.curve.h1 (ctx.curve.canonical + ctx.kummerClass) = 0 ∧
    ctx.curve.h0 (ctx.curve.canonical + 2 • ctx.kummerClass) = 3 ∧
    ctx.curve.h1 (ctx.curve.canonical + 2 • ctx.kummerClass) = 0 ∧
    Module.finrank F (LinearMap.ker ctx.leptonDiracPairing) = 3 := by
  have hmain := bring_z3_prym_chevalley_weil_ten_split
    ctx.curve ctx.genus_eq_four ctx.three_torsion ctx.kummer_nontrivial
  obtain ⟨_, ⟨hh0K, hh1K⟩, htw1, htw2, _, _, _⟩ := hmain
  have hrange : Module.finrank F (LinearMap.range ctx.leptonDiracPairing) = 1 := by
    rw [LinearMap.range_eq_top.mpr ctx.leptonDiracPairing_surjective, finrank_top,
      ctx.finrank_h1_lep, hh1K]
  have hrn := LinearMap.finrank_range_add_finrank_ker ctx.leptonDiracPairing
  rw [ctx.finrank_h0_lep, hh0K, hrange] at hrn
  exact ⟨htw1.1, htw1.2, htw2.1, htw2.2, by omega⟩

end ExteriorFermionsAnomaliesAndLeptonPairing

end QOU.StandardModel.BringPrymRiemannRochGenerations
