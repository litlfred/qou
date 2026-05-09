# 2026-05-09 — Wedderburn pair-volume LP/SDP-EW wiring + Δ_I-word Weinberg probe

**Branch:** `claude/wedderburn-lp-sdp-wiring`
**Predecessor:** [`2026-05-09-refocused-1ppb-workplan-v3.md`](2026-05-09-refocused-1ppb-workplan-v3.md) §3 item 4
**Companion to:**
[`prop:knot-operator-lp-selection`](../../content/quantum-observable-universe/braids-and-knots/knot-operator-lp-selection.md),
[`def:ew-interface-knot`](../../content/quantum-observable-universe/braids-and-knots/ew-interface-knot.md)

## 1. Two deliverables

This audit captures two compute-bound items per the user's direction
(execute v3 §3 item 4 + try alternative Δ_I words for the Weinberg gap):

**(A) Wire `wedderburn_pair_volumes.py` into
`prop:knot-operator-lp-selection`.** A concrete numerical instance:
solve the LP/SDP-dual program for the EW-sector operator selection
with Wedderburn pair amplitudes |V̂_i V̂_j|_Wedd as the supply matrix.
Report primal_obj, dual_obj, y_0_star, y_star, active_set per
[CLAUDE.md](https://github.com/litlfred/qou/blob/main/CLAUDE.md)
"LP/SDP duals — first-class infra" mandate.

**(B) Try to close the 2.19% Weinberg gap.** The (3,2,1)
max+/2nd-max+ = 1.78 reading on Δ_I^minimal = σ_2 σ_4 σ_2 was
2.19% off CODATA cot θ_W = 1.823 (per the prior deep-dive PR).
Test ~14 alternative Δ_I words and report the best.

Witness:
[`folio-assistant/computations/wedderburn-lp-ew-wiring.witness.json`](../../folio-assistant/computations/wedderburn-lp-ew-wiring.witness.json)

## 2. Deliverable (A) — LP/SDP-EW wiring

### Setup

Pair amplitudes |V̂_i V̂_j|_Wedd computed via the Wedderburn-block
decomposition

$$
  |V̂_i V̂_j|_{\rm Wedd}
  \;=\; w_{\rm sym} \cdot \lambda_i^{\rm sym} \lambda_j^{\rm sym}
  \;+\; w_{\rm std} \cdot (z \cdot (M_i M_j)_{12} + (M_i M_j)_{22})
  \;+\; w_{\rm alt} \cdot \lambda_i^{\rm alt} \lambda_j^{\rm alt}.
$$

The LP per [`prop:operator-selection-lp`](../../content/quantum-observable-universe/braids-and-knots/operator-selection-lp.md):

$$
  \min_{x \geq 0} \sum_k t_k x_k \quad
  \text{s.t.} \quad G x \geq n_{\rm target}, \quad x \geq 0,
$$

with $t_k = |V̂_i V̂_j|_{\rm full}$ (Wedderburn-channel-summed
amplitude per pair), $G = \mathrm{diag}(t) + \epsilon I$ as the
PSD Gram-matrix proxy, and $n_{\rm target} = \sum_k t_k / 2$
(loose feasibility constraint).

### Atom sweep

Per-atom LP solves, all with `duality_gap = 0` (strong duality
verified):

| Atom | $(Z, N)$ | # pairs | primal_obj = dual_obj | y_0_star (shadow price) | # active channels |
|------|---------:|--------:|----------------------:|------------------------:|-----------------:|
| proton | (1, 0) | 1 | 0.180 | 0.601 | 0 |
| neutron | (0, 1) | 1 | 0.069 | 0.373 | 0 |
| deuteron | (1, 1) | 10 | 1.429 | 0.373 | (sweep) |
| triton | (1, 2) | 28 | 3.966 | 0.373 | (sweep) |
| **helium-4** | (2, 2) | **55** | **1.323** | **0.059** | **53** |

Helium-4 is the headline: 55 pair amplitudes feed a 55-element
LP, of which **53 are LP-active** (positive primal x_k). The
shadow price y_0_star = 0.059 quantifies the marginal value of
adding mass to the EW Wedderburn structure at this atom.

### What this gives the workplan

`prop:knot-operator-lp-selection` now has a concrete EW-sector
LP/SDP instance with proper Wedderburn-pair-volume input data.
The witness includes all required dual fields per the
[lp_dual_witness_validator](../../folio-assistant/computations/lp_dual_witness_validator.py)
contract. The wiring closes v3 §3 item 4.

## 3. Deliverable (B) — alt-Δ_I Weinberg probe

### Candidates tested

14 Δ_I words, all using inter-pair generators σ_2 (idx 1) and
σ_4 (idx 3):

| Δ_I | (3,2,1) max+/2nd-max+ | rel err vs CODATA cot θ_W |
|-----|----------------------:|--------------------------:|
| **σ_2 σ_4 σ_2 (minimal, baseline)** | **1.7832** | **2.19%** ★ |
| σ_2 σ_4 | 1.7720 | 2.80% |
| σ_4 σ_2 | 1.7720 | 2.80% |
| σ_2 (single) | 1.7239 | 5.44% |
| σ_4 (single) | 1.9532 | 7.14% |
| σ_4 σ_2 σ_4 (mirror) | 1.4757 | 19.05% |
| σ_2² σ_4² | 1.4277 | 21.69% |
| σ_4² σ_2² | 1.4277 | 21.69% |
| σ_2 σ_4² σ_2 | 1.4277 | 21.69% |
| σ_4 σ_2² σ_4 | 1.4277 | 21.69% |
| σ_2 σ_4 σ_2 σ_4 | 1.4277 | 21.69% |
| σ_4 σ_2 σ_4 σ_2 | 1.4277 | 21.69% |
| σ_2 σ_4 σ_2 σ_4 σ_2 | 1.4298 | 21.57% |
| (empty Δ_I = trivial) | 1.0000 | 45.15% |

### Verdict (B)

**The minimal Δ_I = σ_2 σ_4 σ_2 is OPTIMAL** within this candidate
space. The 2.19% gap is **not closable by Δ_I-word substitution**.
This is informative: the structural origin of the residual lies
elsewhere — likely in:

1. **Non-Wedderburn corrections** to the cot θ_W reading. The
   max+/2nd-max+ ratio on (3,2,1) is a plausible-but-coarse
   structural reading of the EW Wedderburn structure; a more
   refined formula (e.g., weighted by Hoefsmit cell-content
   multiplicity, or by pair-coupling shadow prices y_k from
   deliverable (A)) may close the gap.
2. **Higher-order corrections in the Higgs-vev coupling**. Even
   the optimal Δ_I^minimal is a *minimal* coupling; physical
   Higgs-vev structure may add higher-order corrections (analogous
   to the δ_CS = ℏ_q^4 [5]_q in the EM α derivation).
3. **A categorical-physics derivation of the** structural cot θ_W
   formula that doesn't reduce to an eigenvalue ratio. The
   "max+/2nd-max+" reading was *empirically* close — the right
   categorical formula may differ.

Routes to close the 2.19% gap (open):
- Combine (A)'s LP-active set with (B)'s spectrum: weight the
  (3,2,1) eigenvalues by the LP shadow prices y_k, re-test ratio.
- Test β_EW words with NON-EVEN twists (allowing σ_1, σ_3, σ_5
  with odd exponents in the construction) — these break
  bar-self-duality but may match the actual physical Higgs-vev.
- Investigate whether the RHS of cot θ_W = 1.823 has a clean
  q-rational form involving [k]_q^a for some structural (k, a).

## 4. Connection to v3 workplan

This audit closes v3 §3 item 4 ("`wedderburn_pair_volumes.py`
LP/SDP integration"). The Weinberg probe (B) is a follow-on to
the `claude/weinberg-wedderburn-321-deepdive` finding (2.19%
near-miss); the negative result here narrows where to look.

Recommended next actions per v3 §3:
- Item 1 (Tier-2 PSLQ extension): unchanged.
- Item 2 (Term 7 α_5 numerical fit): unchanged.
- Item 3 (Chirality ⟨c⟩_β concrete computation): unchanged.
- **Item 4 (this audit)**: ✓ DONE.
- Item 5 (`gb_filtration_jet_tracker.py` extension to H_n, n≥4):
  unchanged.

## 5. Files

- This audit:
  [`docs/audits/2026-05-09-wedderburn-lp-ew-wiring.md`](2026-05-09-wedderburn-lp-ew-wiring.md)
- Witness:
  [`folio-assistant/computations/wedderburn-lp-ew-wiring.witness.json`](../../folio-assistant/computations/wedderburn-lp-ew-wiring.witness.json)
- Script:
  [`folio-assistant/computations/wedderburn_lp_ew_wiring.py`](../../folio-assistant/computations/wedderburn_lp_ew_wiring.py)
- Workplan v3:
  [`docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md`](2026-05-09-refocused-1ppb-workplan-v3.md)
