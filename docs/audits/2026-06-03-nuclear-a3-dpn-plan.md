# Nuclear A=3 binding + Δ_pn — derivation plan and baseline

**Status:** SCAFFOLD. Work tranche for two of the four error-reduction
items in the 2026-06-03 workplan: (2) per-nucleus A=3 binding (triton ³H,
helion ³He) and (3) the proton–neutron mass difference Δ_pn. Sibling
tranches: Q_β SDP strict-complementarity (PR #1752) and m_μ lepton
torus-tower (PR #1753).

## Governance (read first)

Both targets are formally below the ~780 ppb CAL-2 floor (Δ_pn 100×
target ≈ 4.7 ppb; the binding-energy ratios sit far below that), which is
owner-declined Subgoal-2 territory (substrate-derivation of q₀, declined
2026-05-08; see [`docs/precision-goals.md`](../precision-goals.md)). The
in-scope deliverable here is **reducing the prediction error from a
categorical/braid derivation** — not formally passing a sub-floor 100×
gate. Where the floor binds, it is reported, not crossed.

No empirical fits. The Δ_λ gate forbids a seventh fit-based ansatz
(six have failed on the deuteron); see
[`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md).

## Baseline (canonical Jones–Markov trace, current q₀)

From `binding_canonical.py` at q₀ ≈ 1.1099786, Q_β = 0.782333 MeV (CAL-3):

| Atom | A | 3A | B_AME (MeV) | B_pred (MeV) | \|Δm/m\| |
|------|---|----|-------------|--------------|----------|
| D    | 2 | 6  | 2.225       | +0.466       | 0.094 %  |
| T    | 3 | 9  | 8.482       | +0.629       | 0.279 %  |
| ³He  | 3 | 9  | 7.718       | +0.658       | 0.251 %  |
| ⁴He  | 4 | 12 | 28.296      | +0.714       | 0.735 %  |

Observation: the canonical trace `B = 𝔈₀·(|tr_M(W_free)| −
|tr_M(W_atom)|)` **underpredicts** the absolute binding by a large factor
(D: 0.466 vs 2.225 MeV). The per-nucleus comparison is currently carried
as a fractional-mass quantity (the `|Δm/m|` column), not as the absolute
binding. The A=3 task is to close the gap between the canonical trace and
the absolute B_AME for the two A=3 nuclei **without fitting**.

## A=3 plan (item 2)

Categorical object for A=3 is the H₉ atomic braid word (3A = 9
generators), `atom_braid_word_3A(Z, N)`:
- triton ³H (Z=1, N=2): (p-block, n-block, n-block) + inter-nucleon crossings;
- helion ³He (Z=2, N=1): (p-block, p-block, n-block) + inter-nucleon crossings.

Concrete first step (per scoping): explicit H₉ Wedderburn character sum
weighted by canonical Jones–Wenzl (Ocneanu) weights `ω_λ`, then scaled by
the binding-link hyperbolic volume (³H → 8₁₁ knot; ³He → L6a4 / Borromean
8G = 5.688). Compare residual vs AME (³H 8.482, ³He 7.718 MeV). If the
residual lands inside the error budget with no free parameters, escalate
to the GAP-A-3 categorical selector (which partition selects which brane
level).

Existing scripts to build on: `binding_canonical.py`,
`binding_threebody_joint_trace.py` (H₉ all-pairs joint trace),
`phase5/phase3_triton_binding_convention_b.py`,
`binding_a3plus_full_theta_assembly.py` (full-order θ_λ assembly; latest
attempt ³He at +17.4 % without fit).

## Δ_pn plan (item 3)

Re-derive the p–n mass difference against the current proton-anchored q₀
via the p–n channel asymmetry already implemented as
`pn_convention="bring_color_weighted"` in `closed_form_tau_M.py`. Confirm
the current 773.9 ppb error originates from a stale-q₀ evaluation vs a
structural gap, and whether the bring-color-weighted asymmetry closes it
at the current anchor.

## Done / next

- [x] Branch + baseline established (this doc).
- [ ] A=3: H₉ Wedderburn × link-volume probe (³H via 8₁₁), no fit.
- [ ] Δ_pn: re-derive at current q₀ via bring-color-weighted asymmetry.
- [ ] Report residuals; escalate the in-budget path to GAP-A-3 if it lands.
