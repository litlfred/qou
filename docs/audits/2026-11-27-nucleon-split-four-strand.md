# The nucleon split from the four-strand lepton reading (parameter-free route)

**Date:** 2026-11-27 · **Branch:** `claude/nucleon-split-four-strand`
**Beans:** `qou-myts` (nucleon split); related `qou-99qc`
**Pre-registration:** [`computations/probes/nucleon_split_four_strand/PREREGISTRATION.md`](../../computations/probes/nucleon_split_four_strand/PREREGISTRATION.md) (written and fixed before any MeV value of this route was computed)
**Lean:** [`QOU/Nuclear/NucleonSplitFourStrand.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitFourStrand.lean) (lean-verify exit 0, no warnings; axioms propext, Classical.choice, Quot.sound; generic `[Field R]`, no numerical value; builds on `QOU.MassTheory.NeutronFourStrand`)
**Probe:** [`computations/probes/nucleon_split_four_strand_probe.py`](../../computations/probes/nucleon_split_four_strand_probe.py) → `nucleon-split-four-strand.witness.json` (exact `Fraction` rebuild of the block from the Jimbo Ř on the 16-dimensional `V^{⊗4}`, check of every Lean closed form, of `[L, σ₁] = [L, σ₂] = 0`, of `L = Δ₄²Δ₃⁻²` and of the reciprocity; then 80 dps at both q₀ anchors; 3/3 assertions)

## 1. Short answer

The last parameter-free route on the `qou-myts` list: give the nucleon word a lepton strand
(β-decay picture `n → p e ν̄`, crossed to `n ν → p e`, the C-lep block of `NeutronFourStrand`:
`N = n⊗ν`, `P = p⊗e`) and let the split come from the lepton's crossings, through the Gibbs map
of route 1 (`NucleonSplitGibbsCoulomb`, no Coulomb term):

    m_n − m_p = E₀ · log(τ_p/τ_n),   τ_p/τ_n = tr_P(V³·L) / tr_N(V³·L),   L = σ₃σ₂σ₁²σ₂σ₃,   E₀ = k_BT_q.

It contains no free parameter. It does **not** reach CODATA. The pre-registered headline gives
**−0.35357 MeV** (order-zero `E₀`): the wrong sign, and 27 % of the CODATA magnitude
1.29333 MeV. The mirror word gives exactly **+0.35357 MeV** (proved reciprocity). Every
pre-registration-compliant variant (closed lepton, same block) lies in `|m_n − m_p| ≤ 0.354 MeV`.

## 2. The choices, decided before the numbers

**C1, trace and normalisation.** Rule: a lepton strand that crosses nothing must give zero split
(the route claims the split comes from the crossings). Only S1-closed (both nucleons in the same
four-strand block, `K^{⊗4}`, `[2]_q⁴` on both) passes: its spectator ratio is 1
(`NeutronFourStrand.trN_V3_eq_trP_V3`). S1-open (`K^{⊗3}⊗1`) gives `q²` (the three-strand cell),
S2a (four-strand `p⊗e` neutron vs three-strand proton, `[2]_q⁴` vs `[2]_q³`) gives `q[2]_q = q²+1`
(the free lepton loop's quantum dimension), S2b gives `q`. S1-closed is also the corpus coloured
trace (`K` on every strand) extended to four strands.

**C2, the word.** (1) The lepton must close on itself, so that "lepton coloured `ν` / `e`" labels
the lepton component: the crossing part must be a pure braid on strand 4. This excludes `σ₃^{±1}`
and the #8636 word `w = σ₁σ₃⁻¹`. (2) The lepton couples to the nucleon, not to a chosen quark:
`L = σ₃σ₂σ₁²σ₂σ₃ = Δ₄²Δ₃⁻²` (the lepton loops once around all three quarks) commutes with
`σ₁, σ₂` (**proved**, `Lp_comm_s1`, `Lp_comm_s2`), so `V³L = LV³` and the sector traces of `M·L`
are invariant under `B₃`-conjugation of `M` (**proved**, `trN_conj_mul`, `trP_conj_mul`). The
`A_{k4}` (lepton loops quark `k`) pick a strand and do not commute. (3) Chirality: `L` (positive
crossings, as the Jimbo `σ = Ř` and the corpus electron word `σ₀σ₁σ₀`), fixed in advance with the
explicit rule that a wrong sign is reported, not repaired by switching to `L⁻¹`.

## 3. Results

**Proved closed forms.** With `S = q¹² − 3q¹⁰ + 3q⁸ − 5q⁶ + 3q⁴ − 3q² + 1` (`tr V³ = −S/q⁶` on either
sector) and `Λ = q¹⁶ − 4q¹⁴ + 6q¹² − 10q¹⁰ + 11q⁸ − 10q⁶ + 6q⁴ − 4q² + 1`:

* `tr_N(V³L) = −Λ/q⁶`, `tr_P(V³L) = −S/q⁴`; the `P`-block of `L` is `q²·1` (`Lp_blockP`), so
  `tr_P(V³L) = q² tr_P(V³)` (`trP_V3_Lp_eq`). Headline `τ_p/τ_n = q²S/Λ` (`ratio_Lp`).
* `tr_N(V³L⁻¹) = −S/q⁸`, `tr_P(V³L⁻¹) = −Λ/q¹⁰`, ratio `Λ/(q²S)` = `(q²S/Λ)⁻¹`
  (`ratio_Lm_eq_inv`): the mirror flips the sign of the split and keeps its magnitude.
* `A_{k4}^{±1}`, `V³σ₃^{±1}`: exact `tr_N`, `tr_P` (`trN_V3_A34p` … `trP_V3_s3Inv`). `A_{14}` and
  `A_{24}` give identical sector traces with `V³`.

**Numbers** at the proton `q₀ = 1.10997858275…`, `E₀ = 4.18598136329 MeV` (order zero),
`4.22748335563 MeV` (tower). The muon anchor agrees to 7 digits (witness). S1-open = S1-closed
`+ 2E₀ log q = +0.87354 MeV` exactly.

| word `X` (`β = V³X`) | status | ratio S1-closed | MeV S1-closed (ord. 0 / tower) | MeV S1-open | MeV S2a | MeV S2b |
|---|---|---|---|---|---|---|
| `1` (spectator) | null test | 1 | 0 / 0 | 0.87354 | 3.36101 | 0.43677 |
| **`L`** | **headline** | **`q²S/Λ` = 0.919003** | **−0.35357 / −0.35708** | 0.51997 | 2.48748 | −0.43677 |
| `L⁻¹` | mirror | `Λ/(q²S)` = 1.088135 | +0.35357 / +0.35708 | 1.22711 | 3.88098 | 0.95673 |
| `A₃₄ = σ₃²` | picks quark 3 | 0.973381 | −0.11294 | 0.76060 | 3.05232 | 0.12807 |
| `A₃₄⁻¹` | picks quark 3 | 1.031394 | +0.12940 | 1.00293 | 3.50073 | 0.57648 |
| `A₂₄`, `A₁₄` | pick quark 2 / 1 | 0.973902 | −0.11070 | 0.76284 | 3.04608 | 0.12183 |
| `A₂₄⁻¹`, `A₁₄⁻¹` | pick quark 2 / 1 | 1.030845 | +0.12716 | 1.00070 | 3.50769 | 0.58344 |
| `σ₃` | lepton not closed | 0.722195 | −1.36237 | −0.48883 | — | — |
| `σ₃⁻¹` | lepton not closed | 0.527196 | −2.67979 | −1.80626 | — | — |
| `w = σ₁σ₃⁻¹` alone (#8636) | reference | `1 − h²` = 0.956294 | −0.18707 | — | — | — |

CODATA 2022 `m_n − m_p = 1.293332 MeV`, used only for the gap column of the witness. Every
ratio is positive, so the log is defined everywhere. "—" = not in the pre-registered grid.

## 4. Comparison boundary and scope

* **(a) Scope-limited negative.** Under the pre-registered rules (S1-closed, lepton closed on
  itself), the four-strand lepton reading gives `|m_n − m_p| ≤ 0.354 MeV` for every word, and the
  headline has the wrong sign. Without the `K`-weight cell `2E₀ log q` (which the null test removes,
  because the lepton's `K` cancels the nucleon's on both sectors), the lepton crossings alone
  supply at most about a quarter of the split. The route does not close the gap.
* **(b) Structural exclusion.** None claimed beyond the proved statements: the spectator lepton
  gives zero (on main), and the chirality of the lepton loop sets only the sign (`ratio_Lm_eq_inv`).
* **Nearest unselected number, disclosed.** S1-open with `L⁻¹` gives 1.22711 MeV (−5.1 %). It
  breaks two pre-registered rules: the open trace fails the null test (it is the three-strand cell
  0.87354 plus the mirror loop's 0.35357), and the chirality was fixed to `L`. Picking it now would
  be selection by closeness to CODATA; it is not a prediction. Read as a decomposition it says
  `cell + |lepton loop|` = 1.227 MeV; deriving both an open lepton strand *and* the mirror
  chirality would be needed to make it a claim, and neither is derived.
* **Conjugation.** The headline is invariant under `B₃`-conjugation of the nucleon word (proved),
  which removes the #9544 caveat for the nucleon part. Sector traces remain lepton-coloured traces,
  not invariant under `B₄` conjugation that moves the lepton strand; `tr_N + tr_P` is.
* **Sign.** The headline makes the proton heavier. The pre-registration fixed that this is
  reported as is.

## 5. Reproduce

```bash
scripts/lean-verify.sh folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonSplitFourStrand.lean
python3 -u computations/probes/nucleon_split_four_strand_probe.py
```

`scripts/precision-gates.sh --changed` was started but did not finish within 400 s in this
session (corpus-wide audits); the audit witnesses it had rewritten by then were reverted, not
committed. The gate run is left to CI.
