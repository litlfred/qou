# §3b-cond audit-visibility stubs — triage (2026-06-03)

> Triage doc for the 9 `True := trivial` theorem stubs in
> `content/quantum-observable-universe/lean/QOU/` that follow the
> standardised "§3b-cond conditional-class hypothesis (audit-visibility stub)"
> pattern. **Verdict: these are intentional documentation markers,
> not bugs to fix.** Recorded as a coord artifact (per user
> direction 2026-06-03) so future agents do not conflate them with
> the kind of placeholder PR [#1720](https://github.com/litlfred/qou/pull/1720)
> strengthened.

## How this triage got opened

Following PR #1720's strengthening of `QSchurYLambdaClosedFormClaim`
(replaced the vacuous `closed_form_holds : True := trivial` placeholder
with a concrete abstract field `qSchurWeight : List ℕ → ℝ → ℝ` plus an
extensional identity), an off-hand session estimate quoted the
`lean-section-3b-cond-classes-permanent` queue item's
`expected_count: "~80-100"` as the count of analogous
classes-to-strengthen — which would have been a substantial follow-up
sweep.

A grep on the **specific** `: True := trivial` pattern after PR #1720
merged found **14 occurrences across 14 files**, not 80-100. The 80-100
queue estimate was for a **broader** scope — all §3b-cond class sorries
of any shape, including registry-permanent ones — not the specific
`True := trivial` pattern.

**Pattern-conflation caveat for future agents.** When a queue / audit /
ledger gives a count for "§3b-cond placeholders", verify the exact
syntactic pattern before scoping a follow-up. The categories are:

| pattern | semantic | what to do |
|---|---|---|
| `holds : True := trivial` (class field) + `theorem foo_conditional [...] : True := trivial` (downstream) | **Audit-visibility stub** — intentional marker | **Leave as-is**; the file comment labels them so explicitly |
| `class FooClass : Prop where bar := sorry  -- Ref: [manuscript]` | **Conjecture itself** — §3b permanent placeholder | **Leave as-is**; per `lean-section-3b-cond-classes-permanent` registry |
| `closed_form_holds : True := trivial` (class field) intended to carry meaningful content | **Bug** — class meant to carry math but uses vacuous body | **Strengthen** like #1720 (abstract field + extensional identity) |

## The 14 occurrences (post-#1720 main)

### 9 theorem-level audit-visibility stubs (intentional, leave as-is)

| file | line | class (local) | classifier |
|------|------|---------------|------------|
| [`QOU/Molecular/h2_lp_dual_binding.lean`](../../content/quantum-observable-universe/lean/QOU/Molecular/h2_lp_dual_binding.lean) | 66 | `QIntegerMassFormula` | LP-dual binding |
| [`QOU/Molecular/ch4_lp_dual_binding.lean`](../../content/quantum-observable-universe/lean/QOU/Molecular/ch4_lp_dual_binding.lean) | 91 | `QIntegerMassFormula` | LP-dual binding |
| [`QOU/Molecular/co2_lp_dual_binding.lean`](../../content/quantum-observable-universe/lean/QOU/Molecular/co2_lp_dual_binding.lean) | 89 | `QIntegerMassFormula` | LP-dual binding |
| [`QOU/Molecular/co_lp_dual_binding.lean`](../../content/quantum-observable-universe/lean/QOU/Molecular/co_lp_dual_binding.lean) | 93 | `QIntegerMassFormula` | LP-dual binding |
| [`QOU/Molecular/benzene_threading_emergence.lean`](../../content/quantum-observable-universe/lean/QOU/Molecular/benzene_threading_emergence.lean) | 75 | `QIntegerMassFormula` | threading emergence |
| [`QOU/ParticleInteractions/neutron_qvalue_symbolic.lean`](../../content/quantum-observable-universe/lean/QOU/ParticleInteractions/neutron_qvalue_symbolic.lean) | 79 | `BorromeanQuark` | β-decay Q-value |
| [`QOU/BraidKnot/HoefsmitV21CosSymmetrization.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/HoefsmitV21CosSymmetrization.lean) | 302 | `BorromeanQuark` | Hoefsmit V_(2,1) symmetrisation |
| [`QOU/BraidsAndKnots/S4S3HalfSymmetricProjection.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S4S3HalfSymmetricProjection.lean) | 129 | `BorromeanCommonScale` | S_4 / S_3 half-symmetric projection |
| [`QOU/BraidKnot/BarSymmetricBarAntiSymmetricIdentities.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/BarSymmetricBarAntiSymmetricIdentities.lean) | 220 | `BorromeanQuark` | `Q_borromean_eq_zero` placeholder |

All 9 follow the uniform pattern:

```lean
/-! ## §3b-cond conditional-class hypothesis (audit-visibility stub) -/

namespace QOU.X.ConditionalAudit
class <ClassName> : Prop where
  holds : True
theorem <block>_conditional [_inst : <ClassName>] : True := trivial
end QOU.X.ConditionalAudit
```

The file comment explicitly labels these as **audit-visibility stubs**
— they exist to mark §3b-cond conditional-class structure for the audit
infrastructure (so the audit can verify "every conjectural block has a
class hypothesis"), but the conditional theorem itself doesn't carry
research content.

### 5 docstring mentions (not code, not stubs)

| file | line | context |
|------|------|---------|
| [`QOU/BraidKnot/PhiQTowerAlgebraicStratification.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/PhiQTowerAlgebraicStratification.lean) | 23 | docstring "upgrades the previous `: True := trivial` placeholder" |
| [`QOU/BraidKnot/GradedMarkovTraceFromGSFiltration.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/GradedMarkovTraceFromGSFiltration.lean) | 12 | docstring "replaces previous `: True := trivial` placeholder" |
| [`QOU/BraidsAndKnots/BorromeanMarkovTrace.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanMarkovTrace.lean) | 204 | docstring "closes the `Q_borromean_eq_zero : True := trivial` placeholder" |
| [`QOU/HeckeAlgebra/Formal.lean`](../../content/quantum-observable-universe/lean/QOU/HeckeAlgebra/Formal.lean) | 201 | docstring describing past `: True := trivial` body |
| [`QOU/BraidKnot/IwahoriHeckeAPI.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/IwahoriHeckeAPI.lean) | 334 | `example : True := trivial` (illustrative example, not a stub) |

These are not actionable — they're either documentation describing past
states or an illustrative example.

## Proof-of-concept candidates (per author direction)

For the 9 audit-visibility stubs, two stand out as the cleanest
candidates for strengthening if the project later decides the stubs
should become real conditional theorems:

### Candidate 1 — `neutron_qvalue_conditional` (`neutron_qvalue_symbolic.lean:79`)

The file already contains a real symbolic derivation of
`Q_β^{pred} = m_e · |q_0² − 2q_0 − 1| · (q_0 + 1) / (2 q_0³) ≈ 0.7836 MeV`
([`recomputed-low-isotope-mass-table.md`](../../content/quantum-observable-universe/mass-endomorphism/recomputed-low-isotope-mass-table.md)).
A strengthened version could read:

```lean
class BorromeanQuark : Prop where
  qBetaPredicted : ℝ       -- the canonical closed-form prediction
  matchesCodata :
    abs (qBetaPredicted - codata_Q_beta_MeV) / codata_Q_beta_MeV < 2e-3

theorem neutron_qvalue_conditional [inst : BorromeanQuark] :
    abs (inst.qBetaPredicted - codata_Q_beta_MeV) / codata_Q_beta_MeV < 2e-3 :=
  inst.matchesCodata
```

This is the cleanest candidate because the conditional content
(the +0.17% framework prediction) is already real, well-witnessed,
and a single-line extensional identity.

### Candidate 2 — `Q_borromean_eq_zero` (`BarSymmetricBarAntiSymmetricIdentities.lean:220`)

The file's title is literally `Q_borromean_eq_zero`. A strengthened
version could read:

```lean
class BorromeanQuark : Prop where
  qBorromean : ℝ
  vanishes : qBorromean = 0

theorem Q_borromean_eq_zero [inst : BorromeanQuark] : inst.qBorromean = 0 :=
  inst.vanishes
```

Trivially extensional but communicates the actual claim.

## Recent §3b-cond strengthening precedents (PR #1736, 2026-06-03)

PR [#1736](https://github.com/litlfred/qou/pull/1736) merged 5 new §3b-cond conjectural classes — none follow the `True := trivial` placeholder pattern. All carry **extensional identity fields**, modelling exactly the strengthening direction proposed for Candidates 1+2 above. Future strengthening work can use these as templates.

| class | file | identity field shape |
|---|---|---|
| `SubstrateEWDerivations` | [`QOU/BraidKnot/SubstrateEWHypotheses.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/SubstrateEWHypotheses.lean) | `claim_g_eq_pi_h : gauge_coupling_g = Real.pi * h_substrate_value` + 2 more |
| `HeckeMassTraceContext` | [`QOU/Braiding/hecke_mass_trace.lean`](../../content/quantum-observable-universe/lean/QOU/Braiding/hecke_mass_trace.lean) | `claim_cat_mass_eq_norm_trace : cat_mass = norm (markovInst.trace Phi_mass)` + 1 more |
| `CategoricalHiggsIdempotent` | [`QOU/QuantumObservableUniverses/CategoricalHiggsIdempotent.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/CategoricalHiggsIdempotent.lean) | qDim closed-form fields ([`0cf311f7`](https://github.com/litlfred/qou/commit/0cf311f7), [`8454f01f`](https://github.com/litlfred/qou/commit/8454f01f)) |
| `GActionOnSubstrate` | [`QOU/QuantumObservableUniverses/GActionOnSubstrate.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/GActionOnSubstrate.lean) | encoded axioms ([`b71592d9`](https://github.com/litlfred/qou/commit/b71592d9), [`f81044ff`](https://github.com/litlfred/qou/commit/f81044ff)) |
| `StaircaseEWResidual` | [`QOU/StaircaseCornerHook/StaircaseEWResidual.lean`](../../content/quantum-observable-universe/lean/QOU/StaircaseCornerHook/StaircaseEWResidual.lean) | bundled empirical hypotheses ([`32e93fd3`](https://github.com/litlfred/qou/commit/32e93fd3)) |

These are **not** part of the audit-visibility-stub category (no `: True` field) — they are examples of **already-strengthened §3b-cond classes**. The strengthening pattern is uniform: each conjectural-condition field is an extensional identity (LHS = RHS, both real expressions), no naked `sorry`, no `True := trivial`, hypothesis-only (no global instance).

For Candidate 1 (`neutron_qvalue_conditional`) and Candidate 2 (`Q_borromean_eq_zero`), use these 5 as templates when authoring the extensional fields.

## Recommended disposition

1. **Default: leave the 9 as-is.** They are intentional markers and
   the file comments document this. No PR needed.
2. **Optional follow-up (if author wants):** strengthen Candidates 1+2
   above as a precedent-setting micro-PR (~2-file change), mirroring
   PR #1720 in spirit but with simpler extensional identities. The other
   7 stubs can stay as-is until per-file research content surfaces.
3. **For future agents:** before quoting a count from a queue / ledger,
   `grep -rln '<exact pattern>' <scope>` to verify the count is for the
   syntactic pattern you're about to refactor, not a broader semantic
   category. See "Pattern-conflation caveat" above.

## Cross-refs

- PR [#1720](https://github.com/litlfred/qou/pull/1720) — the
  `QSchurYLambdaClosedFormClaim` strengthening that established the
  precedent (genuinely buggy placeholder, not an audit stub)
- CLAUDE.md §3b-cond — the conditional-class convention
- `.beans/lean-discharge-queue.json` item `lean-section-3b-cond-classes-permanent`
  — the source of the "~80-100" figure (broader scope than this triage)
- [`docs/audits/2026-06-02-lean-discharge-queue-staleness-audit.md`](../audits/2026-06-02-lean-discharge-queue-staleness-audit.md)
  — the queue staleness audit that surfaced the registry pattern
