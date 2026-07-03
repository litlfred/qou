/-
# QOU.Hecke.ClosedFormInterfaceFactors — Phase-5q closed-form interface factors

Fibre-level (pre-archimedean, generic field — AGENTS.md §7c) formalization of
the algebraic layer of the Phase-5q closed form

  tr_M(𝓑_K) = tr_M³(𝓑_p)^Z · tr_M³(𝓑_n)^N · ∏_i f_i(q),
  f_pp = z,   f_nn = z − h,   f_pn = z − h·(1/2 − δ(q)/4),

with Markov parameter `z = 1/(√q + 1/√q)`, Hecke skein parameter
`h = q − q⁻¹`, and the PROVEN leading flavor split
`δ(q) = (q−1)²·(1−q⁻⁴)/3` (prop:flavor-split-substrate; the posited
subleading `(1+ℏ_q³)` correction was de-wired 2026-06-29 and is NOT used).

To avoid `Real.sqrt` (which would cross the substrate→archimedean wall),
everything is stated in the square-root variable `s` with `q = s²` over a
generic `{R : Type u} [Field R]`:

  z = s/(s²+1) = 1/(s + s⁻¹),   h = s² − s⁻²,
  δ = (s²−1)²·(1 − s⁻⁸)/3.

## What is proved sorry-free here

* the √q form of the Markov parameter (`markovZ_eq_inv_sqrt_sum`);
* bar-involution behaviour under `s ↦ s⁻¹` (i.e. `q ↦ q⁻¹`): `z` bar-even,
  `h` bar-odd, `δ(q⁻¹) = −q²·δ(q)`, and the induced swap on the factors;
* the exact cubic-vanishing factorization
  `δ = (q−1)³(q³+q²+q+1)/(3q⁴)` — third-order zero at `q = 1` — and the
  structural identity `δ = ℏ_q²·h·[2]_q/3`;
* factor algebra: `f_pp·f_nn = z² − z·h`, `f_pp + f_nn = 2z − h`,
  `f_pn = (f_pp+f_nn)/2 + h·δ/4` (bring-color-weighted p-n factor =
  bar-invariant average + flavor-split correction), and the division-free
  bridging form `4·f_pn = 4z − (2−δ)·h`;
* confluence at `q = 1`: all three factors collapse to `z(1) = 1/2`-slot
  value `markovZ 1` (since `h(1) = 0`);
* the interface-list assembly layer: for any interface multiset the closed
  form's product `∏_i f_i` equals `f_pp^{#pp}·f_nn^{#nn}·f_pn^{#pn}`, and
  for the canonical `p^Z n^N` ordering of `closed_form_tau_M.
  canonical_interface_kinds` (protons first, then neutrons: `Z−1` p-p
  bonds, one p-n bond, `N−1` n-n bonds) the closed form specialises to
  `τ_p^Z·τ_n^N·f_pp^{Z−1}·f_nn^{N−1}·f_pn`, with the deuteron instance
  `τ_p·τ_n·f_pn`;
* the trace bridge: via the existing `QOU.Hecke.MarkovTrace` class, the
  Markov trace of each bridge crossing `σ_i + d_k·1` equals the matching
  interface factor when `z_param = markovZ s`
  (`trace_interface_bond`, extending `trace_bond_crossing` of
  `MarkovBondFactor.lean` to the three named bond kinds).

## What is NOT claimed here (honest boundary)

The identification of the full `H_{3A}` Markov trace of the canonical atom
braid with the bond-factorized product for general `A` (the cross-level
Markov-axiom word induction) is not carried by the `MarkovTrace` class yet
— the same gap documented at `markov_trace_unique` and in
`MarkovBondFactor.lean`. That analytic step is verified exactly in ℚ at
rational `s`-points for D and T, and to 1e-49 at the four anchor atoms, by
`computations/probe_9b_laurent_degree_10a5.py` (11/11 assertions) and the
Phase-5q witness `closed-form-tau-M-verification-phase5q.witness.json`.
This module proves the complete algebraic layer downstream of that step.

## References

- [jones1987] https://doi.org/10.2307/1971403
- [manuscript] prop:constit-factor-tau-M-proton-identity (Phase 5l)
- [manuscript] prop:interface-knot-markov-z (Phase 5c.1)
- [manuscript] prop:flavor-split-substrate (PR #690 leading split)
- computations/closed_form_tau_M.py (conventions; bring_color_weighted)
- computations/probe_9b_laurent_degree_10a5.py (exact-ℚ verification)
-/

import QOU.Hecke.MarkovTrace
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.Hecke.ClosedForm

universe u

variable {R : Type u} [Field R]

/-! ## §1. The primary parameters in the square-root variable `s` (q = s²) -/

/-- Markov parameter `z = 1/(√q + 1/√q)` written as the rational function
`s/(s²+1)` in the square-root variable `s` (so no `Real.sqrt` is needed —
per AGENTS.md §7c this stays on the substrate side of the wall). -/
def markovZ (s : R) : R := s / (s ^ 2 + 1)

/-- Hecke skein parameter `h = q − q⁻¹ = s² − s⁻²`. -/
def heckeH (s : R) : R := s ^ 2 - (s ^ 2)⁻¹

/-- Substrate Planck parameter `ℏ_q = 1 − q⁻¹` (in `s`: `1 − s⁻²`). -/
def hbarQ (s : R) : R := 1 - (s ^ 2)⁻¹

/-- Quantum integer `[2]_q = q + q⁻¹` (in `s`: `s² + s⁻²`). -/
def quantumTwo (s : R) : R := s ^ 2 + (s ^ 2)⁻¹

/-- PROVEN leading flavor split `δ(q) = (q−1)²·(1−q⁻⁴)/3`
(prop:flavor-split-substrate, `_li_2_q_util.flavor_split_leading`).
In `s`: `(s²−1)²·(1−s⁻⁸)/3`. -/
def flavorDelta (s : R) : R := (s ^ 2 - 1) ^ 2 * (1 - ((s ^ 2) ^ 4)⁻¹) / 3

/-! ## §2. The three interface factors -/

/-- p-p interface factor `f_pp = z` (positive crossing, Markov axiom). -/
def fPP (s : R) : R := markovZ s

/-- n-n interface factor `f_nn = z − h` (negative crossing, Markov axiom +
Hecke skein `σ⁻¹ = σ − h·1`). -/
def fNN (s : R) : R := markovZ s - heckeH s

/-- Bring-color-weighted p-n interface factor
`f_pn = z − h·(1/2 − δ/4)` (canonical convention since 2026-06-01,
`closed_form_tau_M.closed_form_ratio` with the PROVEN leading `δ`). -/
def fPN (s : R) : R := markovZ s - heckeH s * (1 / 2 - flavorDelta s / 4)

/-! ## §3. √q form and bar-involution behaviour (`s ↦ s⁻¹`, i.e. `q ↦ q⁻¹`) -/

/-- `z = 1/(√q + 1/√q)`: the defining form of the Markov parameter. -/
theorem markovZ_eq_inv_sqrt_sum (s : R) (hs : s ≠ 0) :
    markovZ s = (s + s⁻¹)⁻¹ := by
  have h : s + s⁻¹ = (s ^ 2 + 1) / s := by
    field_simp
  rw [markovZ, h, inv_div]

/-- Helper: `(s⁻¹)² + 1` is a unit multiple of `s² + 1`. -/
theorem inv_sq_add_one_eq (s : R) (hs : s ≠ 0) :
    (s⁻¹) ^ 2 + 1 = (s ^ 2)⁻¹ * (s ^ 2 + 1) := by
  field_simp
  ring

/-- **`z` is bar-even**: `z(q⁻¹) = z(q)` — the Markov parameter is invariant
under the bar involution `q ↦ q⁻¹` (`s ↦ s⁻¹`). -/
theorem markovZ_bar (s : R) (hs : s ≠ 0) (h1 : s ^ 2 + 1 ≠ 0) :
    markovZ s⁻¹ = markovZ s := by
  have h2 : (s⁻¹) ^ 2 + 1 ≠ 0 := by
    rw [inv_sq_add_one_eq s hs]
    exact mul_ne_zero (inv_ne_zero (pow_ne_zero 2 hs)) h1
  unfold markovZ
  rw [div_eq_div_iff h2 h1]
  field_simp
  ring

/-- **`h` is bar-odd**: `h(q⁻¹) = −h(q)` — the Hecke skein parameter changes
sign under the bar involution (the skein swaps `σ ↔ σ⁻¹`). -/
theorem heckeH_bar (s : R) : heckeH s⁻¹ = - heckeH s := by
  unfold heckeH
  rw [inv_pow, inv_inv]
  ring

/-- **`δ` bar behaviour**: `δ(q⁻¹) = −q²·δ(q)` (in `s`: `−s⁴·δ`). The flavor
split is bar-odd up to the weight-two factor `q²` — consistent with its
`ℏ_q²·h·[2]_q/3` decomposition (`ℏ_q(q⁻¹) = −q⁻¹·ℏ_q(q)` twice, `h` odd,
`[2]_q` even). -/
theorem flavorDelta_bar (s : R) (hs : s ≠ 0) :
    flavorDelta s⁻¹ = -(s ^ 4) * flavorDelta s := by
  unfold flavorDelta
  field_simp
  ring

/-- Bar swap on the factors: the positive-crossing factor is bar-invariant. -/
theorem fPP_bar (s : R) (hs : s ≠ 0) (h1 : s ^ 2 + 1 ≠ 0) :
    fPP s⁻¹ = fPP s := markovZ_bar s hs h1

/-- Bar swap on the factors: the negative-crossing factor goes to
`z + h = f_pp + h` — bar exchanges the crossing chirality. -/
theorem fNN_bar (s : R) (hs : s ≠ 0) (h1 : s ^ 2 + 1 ≠ 0) :
    fNN s⁻¹ = fPP s + heckeH s := by
  unfold fNN fPP
  rw [markovZ_bar s hs h1, heckeH_bar s]
  ring

/-! ## §4. Structure of the flavor split `δ` -/

/-- **Structural identity** `δ = ℏ_q² · h · [2]_q / 3`
(prop:flavor-split-substrate; `_li_2_q_util.flavor_split_leading`
docstring). -/
theorem flavorDelta_eq_hbar_form (s : R) (hs : s ≠ 0) :
    flavorDelta s = hbarQ s ^ 2 * heckeH s * quantumTwo s / 3 := by
  unfold flavorDelta hbarQ heckeH quantumTwo
  field_simp
  ring

/-- **Exact cubic-vanishing factorization** (the leading-order identity):

  `δ(q) = (q−1)³ · (q³+q²+q+1) / (3q⁴)`,

exhibiting the third-order zero of the flavor split at `q = 1` exactly —
the algebraic content of the `δ ≈ (4/3)(q−1)³` leading order. Stated in
`s` with `q = s²`. -/
theorem flavorDelta_factored (s : R) (hs : s ≠ 0) (h3 : (3 : R) ≠ 0) :
    flavorDelta s
      = (s ^ 2 - 1) ^ 3 * (s ^ 6 + s ^ 4 + s ^ 2 + 1) / (3 * s ^ 8) := by
  unfold flavorDelta
  field_simp
  ring

/-- `δ(1) = 0`: no flavor split at the classical point `q = 1`. -/
theorem flavorDelta_one : flavorDelta (1 : R) = 0 := by
  norm_num [flavorDelta]

/-- `h(1) = 0`: the skein parameter vanishes at `q = 1`. -/
theorem heckeH_one : heckeH (1 : R) = 0 := by
  norm_num [heckeH]

/-! ## §5. Factor algebra -/

/-- `f_pp · f_nn = z² − z·h`: the p-p/n-n product needed by the closed
form's Laurent-degree bookkeeping (probe 9b). Pure ring identity. -/
theorem fPP_mul_fNN (s : R) :
    fPP s * fNN s = markovZ s ^ 2 - markovZ s * heckeH s := by
  unfold fPP fNN
  ring

/-- `f_pp + f_nn = 2z − h`: twice the bar-invariant (strict-averaged)
interface factor `z − h/2`. -/
theorem fPP_add_fNN (s : R) :
    fPP s + fNN s = 2 * markovZ s - heckeH s := by
  unfold fPP fNN
  ring

/-- **The bring-color-weighted p-n factor is the bar-invariant average plus
the flavor-split correction**:

  `f_pn = (f_pp + f_nn)/2 + h·δ/4`.

At `δ = 0` this recovers the strict-averaged convention `z − h/2`; the
`h·δ/4` term is the quaternionic color-tube asymmetry
(`closed_form_tau_M` §"bring_color_weighted"). -/
theorem fPN_eq_bar_avg_add_flavor (s : R) (h2 : (2 : R) ≠ 0) :
    fPN s = (fPP s + fNN s) / 2 + heckeH s * flavorDelta s / 4 := by
  have h4 : (4 : R) ≠ 0 := by
    have h : (4 : R) = 2 * 2 := by norm_num
    rw [h]
    exact mul_ne_zero h2 h2
  unfold fPN fPP fNN
  field_simp
  ring

/-- Division-free bridging form `4·f_pn = 4z − (2 − δ)·h` — the shape used
by the Markov-step identity `τ_M(α·(4σ − (2−δ)h·1)) = (4z − (2−δ)h)·τ_M(α)`
(cf. `QOU.BraidKnot.interface_knot_markov_z_bar_symmetric` for the δ = 0
case). -/
theorem fPN_four_mul (s : R) (h2 : (2 : R) ≠ 0) :
    4 * fPN s = 4 * markovZ s - (2 - flavorDelta s) * heckeH s := by
  have h4 : (4 : R) ≠ 0 := by
    have h : (4 : R) = 2 * 2 := by norm_num
    rw [h]
    exact mul_ne_zero h2 h2
  unfold fPN
  field_simp
  ring

/-- Confluence at `q = 1`: the n-n factor collapses onto the p-p factor
(`h(1) = 0`). -/
theorem fNN_one : fNN (1 : R) = fPP 1 := by
  unfold fNN fPP
  rw [heckeH_one]
  ring

/-- Confluence at `q = 1`: the p-n factor collapses onto the p-p factor
(`h(1) = 0` kills both the averaging and the flavor terms). -/
theorem fPN_one : fPN (1 : R) = fPP 1 := by
  unfold fPN fPP
  rw [heckeH_one]
  ring

/-! ## §6. Interface-list assembly of the closed form -/

/-- The three interface kinds of the canonical atomic braid `𝓑_K`
(`closed_form_tau_M.canonical_interface_kinds`): p-p (positive crossing),
n-n (negative crossing), p-n (bring-color-weighted averaged crossing). -/
inductive InterfaceKind : Type
  | pp
  | nn
  | pn
  deriving DecidableEq, Repr

/-- Per-interface factor `f_i(q)` of the closed form. -/
def interfaceFactor (s : R) : InterfaceKind → R
  | .pp => fPP s
  | .nn => fNN s
  | .pn => fPN s

/-- The interface product `∏_i f_i(q)` over an interface list. -/
def closedFormProduct (s : R) (ks : List InterfaceKind) : R :=
  (ks.map (interfaceFactor s)).prod

/-- **Assembly layer of the Phase-5q closed form**: the full closed-form
value `tr_M³(𝓑_p)^Z · tr_M³(𝓑_n)^N · ∏_i f_i(q)` from the two `H₃`
building blocks (`closed_form_tau_M.closed_form_tau_M`). -/
def closedFormTauM (s tauP tauN : R) (Z N : ℕ)
    (ks : List InterfaceKind) : R :=
  tauP ^ Z * tauN ^ N * closedFormProduct s ks

/-- The interface product depends only on the interface **census**:
`∏_i f_i = f_pp^{#pp} · f_nn^{#nn} · f_pn^{#pn}`. -/
theorem closedFormProduct_eq_pow_counts (s : R) (ks : List InterfaceKind) :
    closedFormProduct s ks
      = fPP s ^ ks.count .pp * fNN s ^ ks.count .nn
          * fPN s ^ ks.count .pn := by
  induction ks with
  | nil => simp [closedFormProduct]
  | cons k rest ih =>
    have hstep : closedFormProduct s (k :: rest)
        = interfaceFactor s k * closedFormProduct s rest := by
      simp [closedFormProduct]
    cases k <;>
      simp only [hstep, ih, interfaceFactor, List.count_cons] <;>
      simp <;>
      ring

/-- Canonical interface list of the `p^Z n^N` ordering
(`closed_form_tau_M.canonical_interface_kinds`, bring_color_weighted
labels): `Z−1` p-p bonds, then one p-n bond (when both species are
present), then `N−1` n-n bonds. Nat subtraction handles the `Z = 0` /
`N = 0` edge cases exactly as the Python (`A < 2 → []`). -/
def canonicalInterfaceKinds (Z N : ℕ) : List InterfaceKind :=
  List.replicate (Z - 1) .pp
    ++ (if 0 < Z ∧ 0 < N then [.pn] else [])
    ++ List.replicate (N - 1) .nn

/-- **Canonical closed form** for an atom with `Z ≥ 1` protons and `N ≥ 1`
neutrons:

  `tr_M(𝓑_K) = τ_p^Z · τ_n^N · f_pp^{Z−1} · f_nn^{N−1} · f_pn`. -/
theorem closedFormTauM_canonical (s tauP tauN : R) (Z N : ℕ)
    (hZ : 0 < Z) (hN : 0 < N) :
    closedFormTauM s tauP tauN Z N (canonicalInterfaceKinds Z N)
      = tauP ^ Z * tauN ^ N
          * (fPP s ^ (Z - 1) * fNN s ^ (N - 1) * fPN s) := by
  unfold closedFormTauM canonicalInterfaceKinds closedFormProduct
  rw [if_pos ⟨hZ, hN⟩]
  simp only [List.map_append, List.prod_append, List.map_replicate,
    List.prod_replicate, List.map_cons, List.map_nil, List.prod_cons,
    List.prod_nil, interfaceFactor]
  ring

/-- **Deuteron instance** (`Z = N = 1`, the `H₆` anchor of the exact-ℚ
verification): `tr_M(𝓑_D) = τ_p · τ_n · f_pn`. -/
theorem closedFormTauM_deuteron (s tauP tauN : R) :
    closedFormTauM s tauP tauN 1 1 (canonicalInterfaceKinds 1 1)
      = tauP * tauN * fPN s := by
  have h := closedFormTauM_canonical s tauP tauN 1 1 one_pos one_pos
  simpa using h

/-! ## §7. Trace bridge: interface factors as Markov-trace bond expectations -/

/-- Constant coefficient `d_k` of the bridge crossing `σ + d_k·1` realising
interface kind `k` (p-p: `0`; n-n: `−h`; p-n: `−h·(1/2 − δ/4)`) — the
`(c, d)` data of `MarkovBondFactor.lean` with `c = 1` throughout. -/
def bondD (s : R) : InterfaceKind → R
  | .pp => 0
  | .nn => - heckeH s
  | .pn => - (heckeH s * (1 / 2 - flavorDelta s / 4))

/-- Each interface factor is the conditional expectation `z + d_k` of its
bridge crossing. -/
theorem interfaceFactor_eq_bond_expectation (s : R) (k : InterfaceKind) :
    interfaceFactor s k = markovZ s + bondD s k := by
  cases k <;>
    simp only [interfaceFactor, bondD, fPP, fNN, fPN] <;>
    ring

section TraceBridge

variable {n : ℕ} {q : R} {A : Type u}
  [Ring A] [Algebra R A]
  [HA : HeckeAlgebra R n q A]
  [MT : MarkovTrace n q A]

/-- **Trace bridge**: when the Markov trace's `z_param` is the closed form's
`markovZ s`, the trace of the bridge crossing `σ_i + d_k·1` is exactly the
interface factor `f_k(q)` — connecting the Phase-5q factors to the
`QOU.Hecke.MarkovTrace` class (single-bond case; the two-bond case follows
from `trace_bond_pair_factorizes`, and the general `A`-bond factorization
awaits the cross-level Markov axiom, per the module docstring). -/
theorem trace_interface_bond (s : R) (hz : MT.z_param = markovZ s)
    (i : Generator n) (k : InterfaceKind) :
    MT.trace (HA.embed i + bondD s k • (1 : A)) = interfaceFactor s k := by
  rw [map_add, map_smul, MT.trace_gen, MT.normalised, smul_eq_mul, mul_one,
    hz, interfaceFactor_eq_bond_expectation]

end TraceBridge

end QOU.Hecke.ClosedForm
