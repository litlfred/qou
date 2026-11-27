# The nucleon split from the position-labelled diagonal of `V³` (parameter-free route)

**Date:** 2026-11-27 · **Branch:** `claude/nucleon-split-v3-diagonal`
**Beans:** `qou-myts` (nucleon split); related `qou-99qc`
**Pre-registration:** [`computations/probes/nucleon_split_v3_diagonal/PREREGISTRATION.md`](../../computations/probes/nucleon_split_v3_diagonal/PREREGISTRATION.md) (written and fixed before any MeV value of this route was computed)
**Lean:** [`QOU/Nuclear/NucleonSplitV3Diagonal.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitV3Diagonal.lean) (lean-verify exit 0, no warnings; axioms propext, Classical.choice, Quot.sound; generic `[Field R]`, no numerical value)
**Probe:** [`computations/probes/nucleon_split_v3_diagonal_probe.py`](../../computations/probes/nucleon_split_v3_diagonal_probe.py) → `nucleon-split-v3-diagonal.witness.json` (exact `Fraction` cross-check of the closed forms and the symmetry, then 80 dps at both q₀ anchors; 3/3 assertions)

## 1. Short answer

The route named "not excluded" in `2026-11-27-nucleon-charge-dressed-words.md` §4: read the pure
braid `V³ = (σ₁σ₂⁻¹)³` with a definite strand for the odd quark, using the diagonal entries
`⟨c|V³|c⟩` already proved in `BorromeanRingColouredTrace.lean`, and apply the Gibbs map of
route 1 (`NucleonSplitGibbsCoulomb`, no Coulomb term):

    m_n − m_p = E₀ · log(τ_p(c_p) / τ_n(c_n)),   τ_c = q^{2T³(c)} ⟨c|V³|c⟩ / [2]_q³,   E₀ = k_BT_q.

It contains no free parameter. It does **not** reach CODATA. The pre-registered,
symmetry-selected pairing `udu ↔ dud` gives **0.88991 MeV** (order-zero `E₀`), against
CODATA 1.29333 MeV: 31 % short. All nine pairings lie between 0.787 and 0.944 MeV. Every
ratio is positive, so the log is defined for all of them. The spread around the undressed cell
`2E₀ log q = 0.87354 MeV` is ±0.08 MeV.

## 2. The selection, decided before the numbers

**Proved (`strandRev_V3A`, `strandRev_V3B`):** with `J` the strand reversal `i ↦ 2 − i`,
`J ρ(σ₁)(q) J = ρ(σ₂)(q⁻¹)⁻¹`, and `J · V³(q) · J = V³(q⁻¹)ᵀ` on both weight spaces. So the
word is fixed by strand reversal ∘ bar (`q ↦ q⁻¹`, the mirror) ∘ word reversal (transpose; the
`ρ(σᵢ)` are symmetric). On the diagonal, `⟨rev c|V³|rev c⟩(q) = ⟨c|V³|c⟩(q⁻¹)` (`diagA_rev`,
`diagB_rev`, no hypothesis on `q`).

Strands 0 and 2 are therefore exchanged together with the chirality, and strand 1 is the
unique fixed strand. Of the nine pairings, the only one fixed by the symmetry is `udu ↔ dud`
(`pair_rev_fixed_iff`), and its braid part is bar-invariant (`braidPart_middle_bar`).
Pre-registered headline: that pairing. This is a symmetry of the word, not of the link (§4).

## 3. Results

Exact ratios (`ratio_00` … `ratio_22`, each under the explicit non-vanishing of its denominator
polynomial), with
`D₀ = q⁶ − 2q⁴ + 3q² − 1`, `D₁ = (q⁴ − q² + 1)(q⁸ − 3q⁶ + 3q⁴ − 3q² + 1)`,
`D₂ = q⁶ − 3q⁴ + 2q² − 1`. Numbers at the proton `q₀ = 1.10997858275…`,
`E₀ = 4.18598136329 MeV` (order zero) and `4.22748335563 MeV` (tower). The muon anchor agrees
to 7 digits (witness).

| pairing `c_p ↔ c_n` | class | `τ_p/τ_n` exact | at q₀ | MeV (E₀ ord. 0) | MeV (tower) | gap to CODATA |
|---|---|---|---|---|---|---|
| `uud ↔ udd` | (b) flip | `−q⁶(q²−2)(q⁴−q²+1)/D₀` | 1.206724 | 0.78658 | 0.79438 | −0.50675 |
| `uud ↔ dud` | (b) flip | `q⁸(q²−2)(q⁴−q²+1)/D₁` | 1.221426 | 0.83727 | 0.84558 | −0.45606 |
| `uud ↔ ddu` | (a) strand 2 | `q⁴(q²−2)(q⁴−q²+1)/D₂` | 1.229123 | 0.86357 | 0.87213 | −0.42976 |
| `udu ↔ udd` | (b) flip | `q⁶/D₀` | 1.221993 | 0.83922 | 0.84754 | −0.45411 |
| **`udu ↔ dud`** | **(a) strand 1, headline** | **`−q⁸/D₁`** | **1.236881** | **0.88991** | **0.89873** | **−0.40342** |
| `udu ↔ ddu` | (b) flip | `−q⁴/D₂` | 1.244676 | 0.91621 | 0.92529 | −0.37712 |
| `duu ↔ udd` | (a) strand 0 | `(2q²−1)(q⁴−q²+1)/D₀` | 1.230158 | 0.86709 | 0.87569 | −0.42624 |
| `duu ↔ dud` | (b) flip | `−q²(2q²−1)(q⁴−q²+1)/D₁` | 1.245145 | 0.91779 | 0.92689 | −0.37555 |
| `duu ↔ ddu` | (b) flip | `−(2q²−1)(q⁴−q²+1)/(q²D₂)` | 1.252992 | 0.94408 | 0.95344 | −0.34925 |
| class sums | (c) | `q²` (`epsP_V3_eq_qsq_mul_epsN_V3`) | — | 0.87354 | 0.88220 | −0.41980 |
| geometric mean | (c) | `(−q¹²(q²−2)(2q²−1)(q⁴−q²+1)²/(D₀D₁D₂))^{1/3}` | — | 0.87353 | 0.88219 | −0.41981 |

(a) = same strand for the odd quark (`c_n` the complement of `c_p`); (b) = β-decay single-strand
flip `d → u`; (c) = class aggregates. Every perfect matching has the same product
(`ratio_matching_prod_eq`, `ratio_sameposition_prod`), so the geometric mean over (a) and over
(b) is the same number, and it sits within 1.1·10⁻⁵ MeV of the class-sum cell.

## 4. Comparison boundary and scope

CODATA 2022 `m_n − m_p = 1.293332 MeV`, used only in the last column. No pairing reaches it.
The largest, `duu ↔ ddu` (0.944 MeV), is not selected by anything and would still be 27 % short.

* **(a) Scope-limited negative.** This construction, alone, under the Gibbs map with the derived
  `E₀`, gives 0.79–0.94 MeV for every pairing and 0.890 MeV for the symmetry-selected one. Position
  labelling moves the split by at most ±0.08 MeV around the `2E₀ log q` cell. It does not close the
  ~0.42 MeV gap to CODATA, so a missing term is still needed and has to be derived. The result does
  not exclude the ingredient: a position-labelled diagonal may still enter a multi-term closure.
* **(b) Structural exclusion.** None claimed.
* **Conjugation caveat (carried from `BorromeanRingColouredTrace` point 2).** Diagonal entries
  are not conjugation-invariant (`tauP_not_conj_invariant`). A colouring is a boundary condition on
  the open braid, not a label of the closed Borromean rings. The symmetry of §2 belongs to the word
  `(σ₁σ₂⁻¹)³`, not to its conjugacy class. A conjugate word would give other diagonal entries, so
  the per-pairing numbers are not link-invariant predictions. The class aggregates (c) are
  invariant, and they reproduce the #9475 cell.
* **Sign.** Every pairing makes the neutron heavier (all ratios > 1 at q₀).

## 5. Reproduce

```bash
scripts/lean-verify.sh folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitV3Diagonal.lean
python3 -u computations/probes/nucleon_split_v3_diagonal_probe.py
```

`scripts/precision-gates.sh --changed` (after `pip install -e tools/qou-substrate`): Q0_FLIP 0,
no NEW dirty witnesses, no NEW raw-float64. The reds (q0-anchor flip, witness-value copy ratchet)
are corpus-wide and name no file of this change. The tree-measuring audit witnesses that the gate
run moved were reverted, not committed.
