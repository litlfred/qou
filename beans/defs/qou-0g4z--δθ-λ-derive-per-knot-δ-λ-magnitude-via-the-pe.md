---
# qou-0g4z
title: 'Δθ_λ: derive per-knot Δ_λ magnitude via the per-vertex q-Reeb eigenphase (surviving qou-3q7t lead)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T09:37:19Z
updated_at: 2026-10-04T15:25:45Z
parent: qou-v2om
---


## Scoping (2026-08-02, session 016vip)

**Object (precise):** per-vertex seminormal eigenphase `θ_λ = arccos(χ_λ/d_λ)` (rotation
channel, `|χ/d|≤1`) or `arccosh|χ_λ/d_λ|` (growth channel, `|χ/d|>1`). Provably NOT a function
of the scalar `χ^λ` alone (resolves the rotation-vs-growth split the scalar trace collapses).
Deuteron H₆: 10 rotation blocks + 1 growth block `(6,)` (χ/d=1.56). Source:
`docs/audits/2026-06-01-e0-lambda-substrate-derivation-options.md` (Candidate 3, ranked #1);
prior probes `binding_reeb_phase_decomposition.py`, `charge_slambda_reeb_phase_crack.py`.

**Honest prior status (do NOT re-tread v4/v5/v6):** the eigenphase closes only DIFFERENCES
(³H−³He mirror to 2%, B_D to −9%), never the absolute per-block scale; v6 re-introduced a free
scale `γ` (a FIT — forbidden). Four sibling candidates killed by the GAP-A-4 impossibility
theorem. Doc's honest bet: the χ^λ→M_λ map is probably impossible from H₃-level data without a
new substrate axiom (borders Subgoal-2).

**The structural crux (my read):** `θ_λ` is a dimensionless angle ⇒ any `F(θ_λ,χ,y,q₀)` is
scale-free ⇒ fixes RATIOS but the absolute MeV scale is a separate radial datum `θ_λ` does not
carry. "Difference-only" = the radial/scale part is undetermined by the eigenphase. The
disciplined question is therefore NOT "run v7" but: **is the radial-scale part PROVABLY
unrecoverable from H_{3A} substrate data (scope-(b) impossibility ⇒ L2-Subgoal-1 needs a new
axiom — the "profound valid result"), OR is there an un-probed radial handle** (e.g. the
off-diagonal per-vertex content / the growth-block `(6,)` amplitude, which the rotation-only
probes may have under-used)?

**Recommended next (fresh context):** (1) formalize the scale-gauge argument — is the map
`M_λ = m_e·G` with `G` determined by `θ_λ` up to an overall gauge? If the gauge is a proved
invariance ⇒ scope-(b) impossibility. (2) Else test whether the GROWTH block `(6,)` (the one
non-rotation channel) supplies the missing radial scale — it was the channel the difference
probes cancel. Anti-fit STRICT: no `γ`; the {e⁻,p,n} per-block energies are the FALSIFICATION
test, never fit targets.

---

## Result (2026-08-02) — eigenphase-as-absolute-scale is REFUTED (scope-a); Δ_λ magnitude stays OPEN

Branch `claude/qreeb-eigenphase-compact-2026-08-02`. 0-fit, formalize-first.

**Corpus finding:** the q-Reeb eigenphase `θ_λ = arccos(χ_λ/d_λ)` is already formalized for the
figure-eight muon anchor (`figure-eight-reeb-rotation`), with `tr M_{4₁}(q) ≥ −2` proved (block is
compact on the real axis).

**Measured (probe `qreeb_eigenphase_compactness_probe.py`, reads χ witnesses only, B_AME unread):**
in every binding knot (D/T/³He) the SOLE `|χ/d|>1` block is the trivial 1-dim rep `(n,)` — a pure
`q^w` scaling, no rotation angle; every dim≥2 rotation channel is compact (max |χ/d| = 0.85).

**Conclusion:** the eigenphase content is bounded/dimensionless ⇒ difference-only (structural, not a
probe artifact — confirms the E₀ 2026-06-01 audit). The one unbounded channel (`q^w`) is already a
summand of the master formula. **The q-Reeb eigenphase route cannot supply C_knot.** scope-(a).

Lean `QReebEigenphaseCompact.lean` sorry-free (lean-direct exit 0); audit
`docs/audits/2026-08-02-qreeb-eigenphase-compactness.md`.

**Δ_λ magnitude derivation stays OPEN.** Surviving directions (this negative narrows, does not close):
the absolute scale must be a *radial/dimensionful* handle the eigenphases structurally cannot carry —
a per-knot `Vol(K)·ρ` input (cf. mass formula `m = m_e·Vol·ρ/ℏ_q²`), or a many-body cross-term
re-weighting of `q^w` against the compact channels (invisible to pairwise probes). Neither is a fit;
neither is closed. Do NOT re-run a v7 eigenphase scan — it re-treads v4/v5/v6 and tempts the γ fit.

## Round 74 Progress (`litlfred/qou`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/StateIntegralBridgeAndTwoBridgeLayeredNZBrick.lean` (`reeb_eigenphase_scale_gauge_invariance_and_difference_lock`)
- **Summary**: Proved radial scale invariance `(s * chi) / (s * d) = chi / d` for `s != 0` and additive gauge cancellation `(gamma + e1) - (gamma + e2) = e1 - e2` in the Reeb eigenphase channel.
- **80-dps Probe & Witness**: `computations/probes/state_integral_bridge_and_two_bridge_layered_nz_brick_probe.py` -> `computations/probes/state-integral-bridge-and-two-bridge-layered-nz-brick.witness.json` (`scriptCommitSha: 5a0a98fc8762e45b734969dd4e71c7271737dbf3`, PR head `564a7f62489ee3d8fa99df6e5a109d1af0b09d37`)
