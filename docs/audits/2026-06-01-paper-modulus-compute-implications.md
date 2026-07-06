# Paper `|...|` refactor — compute implications (2026-06-01)

**Date:** 2026-06-01
**PR:** TBD (claude/phi-q-modulus-audit-and-reframe-2026-06-01)
**Status:** Implications analysis — follow-up to paper audit (this PR)
+ signed-vs-abs diagnostic (PR #1641).
**Triggered by:** user 2026-06-01: *"fix all issues. try to resolve
questions. escalate specific things to author as needed. then work
on implications for compute."*

## TL;DR

Refactoring the paper to remove `|...|` from non-archimedean sections
**raises the question of compute consistency**: do the production
scripts use `|v|` (current) or signed `v` (would match the corrected
paper)?

**Per PR #1641:** at single-nucleon level both `tr_M(β_p) = +1.07` and
`tr_M(β_n) = +0.92` are positive, so `|...|` is no-op at level 0 in
production. **No immediate production change required.**

At DEEPER LEVELS (pair joints, jets, multi-nucleon interfaces),
sub-braid V̂ values can be negative. There the `|...|` materially
changes the result — up to 92% per term per PR #1641.

## Site-by-site compute consistency

| Paper formula | Paper now (after audit) | Compute script |
|---|---|---|
| `M(𝔥) = ν_SDP·[\|tr_M(T_w)\| + tower + tr_M(C_dim)]` (refactored on this PR to remove `\|...\|` from categorical statement) | signed tr_M(T_w) | `mass_endomorphism.py:145` uses `Phi_q(abs(v["full"]))` |
| `tower = Σ Li_2^q(-\|V̂_i\|) + z²·Σ Li_2^q(-\|V̂_i V̂_j\|)` (refactored on this PR) | signed -V̂_i | `binding_via_interface_knot.py:119` uses `li_2_q(-mp.fabs(v))` |
| `𝔪(ϱ) = \|tr_M(ρ(β))\|` (`calibration-inputs.md:147`, NOT refactored on this PR) | NEEDS REFACTOR | (no direct compute consumer — definition only) |
| `B = m_e·ρ·\|tr_M(T_w)\|` (`conj-canonical-knot-id-sdp.md:20,99`, NOT refactored) | NEEDS REFACTOR | (consumed by atomic_mass_*.py series) |

## The structural inconsistency

After the paper refactor (which this PR partially completes), the
paper-level statements say:

> Categorical: `m(𝔥) = tr_M(T_w) + Σ Li_2^q(-V̂_i) + ...`
> Archimedean specialization: `B(𝔥) = m_e · |m(𝔥)|_{q=q_0}`

But production scripts compute:

> `m_prod(𝔥) = Σ Phi_q(|v|) + ...` (or Li_2^q(-|v|))

The compute uses Φ_q (Faddeev, bar-asymmetric, MASS context per
`prop:li2q-phiq-bar-symmetrization`) while the paper categorical
statement uses Li_2^q (Rogers, bar-symmetric, BINDING context). The
`|...|` is inside the Φ_q / Li_2^q call.

**Two-axis inconsistency:**
1. **Φ_q vs Li_2^q**: production seems to use Φ_q in many sites; paper says Li_2^q
2. **`|...|` placement**: production applies `|...|` at the per-term level inside Φ_q/Li_2^q; paper-corrected has it only at the outer archimedean specialization

## Production impact assessment

Per PR #1641 numerical test:

| Context | Production current `Φ_q(|v|)` | Production signed `Φ_q(v)` | Change |
|---|---|---|---|
| Single-nucleon level (all V̂ > 0) | x | x | **no change** |
| Pair joints (mixed sign possible) | depends | depends | up to ~25% per term |
| Higher-level jets | depends | depends | up to ~92% per term |
| Realistic m_p case | x | x | **likely no change** (V̂ values mostly positive) |
| Realistic Q_β = m_n - m_p | y | y | likely small but unverified |

**Conclusion:** the immediate production scripts are NOT affected by
the paper refactor at the single-nucleon level. The categorical-
correctness of the paper IS affected, and downstream consumers that
build per-isotope formulas from the paper definitions could shift if
they use the corrected signed forms.

## What this means for the c_k saga

Indirect. The c_k saga lives in BINDING (Q_β = m_n - m_p - m_e).
Both m_n and m_p use `Phi_q(|v|)` per current compute. If signed-v
were used:
- m_n changes by Δm_n
- m_p changes by Δm_p
- Q_β changes by Δm_n - Δm_p

If Δm_n ≈ Δm_p (correlated changes from similar sub-braid V̂
patterns), Q_β is INSENSITIVE to the sign change. If uncorrelated,
the c_3 saga could be affected.

**Cannot quantify without running the production at signed-v.** This
is a FOLLOW-UP probe (research-queue: "research-mass-tower-signed-
production-impact").

## Recommended next steps

### Tier A (this PR — DONE):

- ✓ Paper-level audit identifying 34 NON-ARCH-MISUSE sites
- ✓ One representative tier-2 refactor (`atom-knot-mass-derivation.md` lines 66, 76)
- ✓ Compute implications documented (this audit)

### Tier B (FOLLOW-UP, escalate to author):

- 32 remaining NON-ARCH-MISUSE sites in `mass-theory/`, `mass-endomorphism/`, etc.
- Each requires per-site read to confirm misuse vs accurate description of archimedean operation (Tier 1 was false-positive)
- Estimate: 1-2 sessions, 5-10 file edits per session

### Tier C (FOLLOW-UP, after Tier B):

- Production compute parallel refactor: change `Phi_q(abs(v))` to `Phi_q(v)` in scripts where the paper categorical form should be signed
- BUT: this requires deciding whether production uses ARCHIMEDEAN (specialization) or CATEGORICAL form
- If production is correctly archimedean (specialization at q_0 with `|...|` for positivity), NO compute change needed
- If production is meant to mirror the categorical form, signed-v should be used and witness regen triggered

### Tier D (RESEARCH, post-refactor):

- Quantify production impact: m_p_signed vs m_p_abs, Q_β_signed vs Q_β_abs at full per-isotope V̂ resolution
- If material change at q_proton, this is a SUBSTANTIAL finding about the framework
- If no change at q_proton (all relevant V̂ positive), confirm the audit is documentary

## Anti-pattern guards

- ❌ Do NOT refactor all 32 paper sites in one bulk edit without per-site read — Tier 1 was a false positive demonstrating regex audit imprecision
- ❌ Do NOT change production scripts before paper refactor is complete — order matters
- ❌ Do NOT claim the refactor "fixes" c_3 — indirect at best
- ✓ DO escalate flagship-formula refactors to author for individual confirmation

## Files

- This audit doc: `docs/audits/2026-06-01-paper-modulus-compute-implications.md`
- Sister audit (paper sites): `docs/audits/2026-06-01-paper-modulus-nonarchimedean-audit.md`
- Sister diagnostic (Φ_q sensitivity): `computations/qbeta/qbeta_signed_vs_abs_tower_diagnostic.py` + witness
- One representative refactor: `content/quantum-observable-universe/mass-theory/atom-knot-mass-derivation.md` (lines 66, 76 — `|tr_M|` → `tr_M`, `|V̂_i|` → `V̂_i` in categorical formula)

## Cross-refs

- This PR's audit: 34 NON-ARCH-MISUSE sites
- PR #1641: signed-vs-abs Φ_q sensitivity at q_proton
- PR #1626: complex-c_3 fibre diagnostic
- PR #1616: Im(q) fibre/observable framing in AGENTS.md
- `prop:li2q-phiq-bar-symmetrization`: the Φ_q vs Li_2^q discipline
