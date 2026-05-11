# Coordination ledger — neutron-mass substrate Vol-form derivation (Phase 2)

**Goal**: deliver a substrate-only neutron-mass 50 dps derivation chain
(Workplan 2 Phase 2) and capture the Vol-form Borromean baryon
findings as content + audit so the open λ_scale problem is not lost.

**Owner branch**: `claude/neutron-mass-50dps-chain` → PR #640

## Scope map (2026-05-11 snapshot)

| PR | Title | Author | Branch | Classification |
|---|---|---|---|---|
| **#640** (this) | Neutron-mass 50dps derivation chain | @litlfred | claude/neutron-mass-50dps-chain | own |
| #639 | Q_β spectral bridge: unify Form A and Form B | @litlfred | claude/q-beta-spectral-bridge-content | **complementary** — my chain consumes Form? of the substrate Q_β closed form; their bridge identity could pin which |
| #638 | Refute scalar-eigenvalue n_⋆; operator-valued probe | @litlfred | claude/close-level-selection-rule-bvMvw | **convention-overlap** — both rely on canonical Jones-Markov τ_M, mutually reinforcing on the Frobenius selection theorem; their probe directly uses `y_lambda_wenzl_bridge` (correct), while my audit flags the wider registry conflation |
| #635 | Mikusiński WitnessBuilder migration | @litlfred | claude/mikusinski-witness-builder-migration | no overlap (different scope: graded-Mikusiński scripts) |
| #632 | Paper illustrations (SVG figures) | @litlfred | claude/add-paper-illustrations-Diggj | no overlap (figures, not derivations) |

(Bot PRs #31, #411 excluded.)

## Classification axes (skill §2)

### Overlap

- **#638**: HIGH on the τ_M / τ_SW Frobenius-selection convention.
  Their description explicitly chooses "canonical Jones-Markov weight
  $y_\lambda(q_0)$ from Wenzl Schur principal specialization, not the
  2-variable Schur formula." My audit landed in this same window
  flagging the registry-wide conflation. Mutually reinforcing — no
  conflict to resolve.
- **#639**: MODERATE on the substrate $Q_\beta$ closed form.
  My `derive_m_baryon_volume_form.py` evaluates
  $Q_\beta(q_0) = m_e \cdot |q^2 - 2q - 1|(q+1)/(2q^3)$ at $q_0$
  (which is plausibly their Form A). Posted a one-question coordination
  comment asking which form this is.

### Dependency

- **#638** has no dependency on my work. My τ_M / τ_SW audit
  diagnoses a registry-level concern that does not affect their
  probe (since they use `y_lambda_wenzl_bridge` directly).
- **#639** has no hard dependency on my work either. Their bridge
  identity is at leading order $O(h^2)$ — my $\Delta S(n - p)$
  identity is at $O(1)$ and is unaffected by the bridge correction
  size.

### Cherry-pick

- No cherry-picks identified. Each PR ships its own content blocks
  with no file overlap.

## Coordination posts

| PR | Comment URL | Topic |
|---|---|---|
| #638 | [#638-comment-4424639946](https://github.com/litlfred/qou/pull/638#issuecomment-4424639946) | τ_M / τ_SW Frobenius selection alignment; flag wider registry conflation |
| #639 | [#639-comment-4424641848](https://github.com/litlfred/qou/pull/639#issuecomment-4424641848) | Substrate $Q_\beta$ closed-form complementarity; ask Form A vs Form B |

## Inconsistent findings — none to escalate (skill §6)

PR #638's "canonical Jones-Markov" convention is consistent with my
Frobenius-selection-theorem reading and the on-main proof in
[`markov-trace-frobenius-selection.md`](../../content/quantum-observable-universe/braids-and-knots/markov-trace-frobenius-selection.md).
PR #639's bridge identity is consistent with the substrate $Q_\beta$
closed form on main (`derived_masses.py`).

No silent rewriting; no "split the difference" between conflicting
readings — there are no conflicting readings to split.

## Next concrete task (non-overlapping)

Per the user-directed work plan ("1 2 3" after `/coordinate`):

1. **Compute $J_{\mathcal{B}_3}(q_0; \text{orientation}=(k, 3-k))$
   symbolically** for $k \in \{0, 1, 2, 3\}$ — diagnostic (b) from the
   [λ_scale brief](../agent-briefs/2026-05-11-lambda-scale-borromean-baryon-derivation.md).
   This is PR #487 agent's "most actionable next step" and is
   downstream of both #638 (uses canonical τ_M) and #639 (uses
   $Q_\beta$ closed form). Non-overlapping with either sibling.
2. **Relabel registry `schur-weyl-weight-*` outputs** from `tr_M` to
   `tau_SW` — cleans up the conflation across all downstream chains.
   Non-overlapping with #638 (which already uses correct convention).
3. **Audit `derivation_chain.TR_M_AT_Q0` provenance** — annotate
   which values are τ_M vs τ_SW. Documentation work, non-overlapping.

## Periodic-triage schedule (skill §7)

Every 3-5 own commits, pull new sibling comments + CI status. If a
sibling's review comment touches the τ_M / τ_SW distinction or the
substrate $Q_\beta$ formula, fold it into this branch's audit doc;
otherwise skip silently.

Next periodic-triage cycle: after the orientation Jones polynomial
script lands.
