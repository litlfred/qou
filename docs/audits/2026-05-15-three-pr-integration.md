# Three-PR integration audit (#644 ⊕ #645 ⊕ #652)

**Date:** 2026-05-15
**Branch:** `claude/review-1ppb-prs-EC0ay`
**Author:** integration agent
**Scope:** integrate PRs #644, #645, #652 into a single branch;
filter deviations from canonical derivation; close the three PRs.
**Supersedes:** [`2026-05-15-three-pr-1ppb-review.md`](2026-05-15-three-pr-1ppb-review.md)
(the review verdict that recommended #644 → #645 → #652 in
sequence; the user opted for direct integration after #644's agent
stopped working).

## TL;DR

- **#644 work landed:** plan + Phase 1/2 plumbing (P1.A substrate
  $E_0$, P1.C T4 stragglers, P1.D per-partition $k_\lambda$, P2.A
  Habiro, P2.B combined router) + the Δ_coupling H1 leading-form
  probe + the `term5_aK_audit.py` V1-V4 audit.
- **#644 work dropped:** the ⁴He Model B knot survey script and
  witness (`probe_he4_model_b_knot_survey.py`,
  `model-b-he4-knot-survey.witness.json`) — survey methodology
  violates substrate-compositionality.
- **#644 framing corrected:** the plan-doc claim "V1 is the natural
  Hecke choice" is overridden by an integration banner — V1
  computes $\tau(\beta^2)$, **not** a chirality factor; V2 is the
  genuine mirror.
- **#645 work landed in full:** H7a finding (quantum-integer
  prefactor), H1 leading-form probe, Lean P4 audit, two Lean files
  with §3b-cond sorrys kept (trivial-skeleton discharge correctly
  reverted).
- **#652 work landed in full:** 8 CODATA literal migrations into
  typed registries; new `canonical_derivation_pipeline_compliance.py`
  + `witness_reproducibility_check.py` audit scripts; compute-audit
  skill doc update.
- **Mechanical conflict resolved:** `paper_six_term_isotope_sweep.py`
  and `d_from_scratch.py` take #644's structural version; #652's
  CODATA imports re-applied on top.

## §V1 ≠ mirror — the physics correction

PR #644's [`paper_six_term_isotope_sweep.py`](../../folio-assistant/computations/paper_six_term_isotope_sweep.py)
P1.B section states:

> V1 is the natural Hecke choice; V2–V4 are alternative mirror-knot
> conventions whose physical meaning differs.

Reading [`term5_aK_audit.py`](../../folio-assistant/computations/term5_aK_audit.py)
module docstring directly contradicts the "natural choice" framing:

| Variant | Definition | What $\tau(\beta \cdot \beta^{*-1})$ computes | Physical meaning |
|---|---|---|---|
| **V1** | reverse + invert each crossing ⇒ $\beta^* = \beta^{-1}$ | $\tau(\beta \cdot \beta) = \tau(\beta^2)$ | Double-winding |
| **V2** | invert each crossing, keep order ⇒ mirror knot $K^*$ | $\tau(\beta \cdot \beta_{\mathrm{mirror}}^{-1})$ | **Genuine mirror chirality** |
| V3 | reverse only ⇒ word reversal | $\tau(\beta \cdot \beta_{\mathrm{rev}}^{-1})$ | Hopf antipode reversal |
| V4 | V2 with averaged crossings preserved | mirror with symmetric-crossing fix | V2 refinement |

`prop:chirality-dual-space-derivation` defines
$a_K \cdot \mathcal{C}_K = \tau(\beta \cdot \beta^{*-1})$ where
$\beta^*$ is the **mirror braid**. By the audit's own definition,
"mirror braid" means each crossing's over/under is flipped — that
is V2, not V1. V1 is the multiplicative inverse, which is *not* a
mirror operation: $\sigma_i \mapsto \sigma_i^{-1}$ via inversion
yields the same braid presentation pattern as the mirror, but in
the Hecke quotient the relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$
breaks the symmetry — $\beta^{-1}$ unwinds the braid algebraically,
while the mirror flips its handedness geometrically.

**Empirical signature in the V1 backfill table** (from PR #644
plan, lines 153-160):

| Atom | closed-form $a_K$ | V1 | Δ_V1 |
|------|---:|---:|---:|
| proton | 1.000000 | 1.021972 | 0.0220 |
| neutron | 1.000000 | 1.021972 | 0.0220 |
| D | 1.209060 | 1.055840 | 0.1532 |
| T | 1.209060 | 1.079039 | 0.1300 |
| **³He** | **1.209060** | **1.079039** | **0.1300** |

V1(T) = V1(³He) is an "emergent symmetry" per the plan, but it is
mathematically inevitable: $\tau(\beta^2)$ is invariant under any
involution that preserves $\beta \mapsto \beta$ up to conjugation
(including the T ↔ ³He spin involution). The mirror-chirality V2
would explicitly **probe the T ↔ ³He asymmetry**, since the mirror
knot of T is not the mirror knot of ³He — they are mirror partners
of each other (one is the other's mirror). So V2 should give
$a_K(T) = 1/a_K({}^3\mathrm{He})$ (or the relevant chirality
inverse), not equality.

**Action taken in integration:**

1. `term5_aK_audit.py` + its witness are kept as **audit artefacts**.
2. No `chirality_signs_for_isotope` lookup replacement has been
   wired into `paper_six_term_mass()`. The hand-coded heuristic
   stays in production until V2 is computed for {p, n, D, T, ³He}.
3. Plan-doc P1.B is overridden by the integration banner at top.

## §⁴He compositionality — the methodology correction

PR #644's P1.E proposes picking ⁴He's canonical Model B knot from
the survey $\{8_{17}, 10_{123}, 8_{18}, L6a4\}$, ranked by
$\lvert \tau_M \rvert$ at $q_0$. The user's objection: **⁴He should
be built compositionally from less-complex isotopes and hadronic
material**, not chosen from a knot table.

The principle: a canonical-derivation pipeline produces ⁴He's knot
from the substrate, not from a candidate list. ⁴He is a doubly-magic
nucleus = (2p + 2n); it is naturally a composition such as

- ⁴He ≃ D ⊕ D (two deuterons), or
- ⁴He ≃ T ⊕ p (one triton + one proton), or
- ⁴He ≃ ³He ⊕ n (one ³He + one neutron),

with ⊕ a Markov composition of braids at the 12-strand Model A
level. JSJ decomposition of the closure of the composed braid
produces the canonical hyperbolic + Seifert pieces; their union is
**the** Model B knot for ⁴He, not a survey pick. By the same
principle, the existing Model B {D, T, ³He} → {$6_2$, $8_{11}$,
$L6a4$} assignments require re-validation from {p ⊕ p, p ⊕ n,
p ⊕ p ⊕ n, …} compositions; the present "they're hyperbolic and
nice" rationale is empirical, not derivational.

**Action taken in integration:**

1. `probe_he4_model_b_knot_survey.py` and its witness **dropped**
   from this branch.
2. Plan-doc P1.E is overridden by the integration banner at top.
3. Forward work (see §Forward, below) prototypes a compositional
   ⁴He probe.

## What landed (file inventory)

### From #644 — Phase 1/2 plumbing

| File | Action | Note |
|------|--------|------|
| `docs/audits/2026-05-12-1ppb-implementation-plan.md` | landed + corrected | banner override on P1.B + P1.E |
| `docs/audits/2026-05-12-lean-handover.md` | landed | Phase 4 hand-off for Lean agent |
| `docs/audits/2026-05-12-m1-mass-table.md` | landed | honest −98% MAE baseline under substrate $E_0$ |
| `folio-assistant/computations/paper_six_term_isotope_sweep.py` | landed | P1.A, P1.C, P1.D, P2.A, P2.B all wired |
| `folio-assistant/computations/paper-six-term-isotope-sweep.witness.json` | landed | output of the above; combined+sub_tower_mode audit field present |
| `folio-assistant/computations/d_from_scratch.py` | landed | T4 → per-3A migration; P1.C hard break comment |
| `folio-assistant/computations/mass_formula_6term_mpfr_50dps.py` | landed | T4 → per-3A migration |
| `folio-assistant/computations/unified_low_isotope_predictor.py` | landed | docstring fix only |
| `folio-assistant/computations/magic-shell-empirical-instantiation.witness.json` | landed | Δ_cat columns for {p, n, D, T, ³He, ⁴He} — required by #645's H7a cross-anchor |
| `folio-assistant/computations/probe_magic_shell_empirical_instantiation.py` | landed | producer for the above |
| `folio-assistant/computations/delta_coupling_closed_form_probe.py` | landed | H1 closed-form probe |
| `folio-assistant/computations/delta-coupling-closed-form-probe.witness.json` | landed | H1 witness |
| `folio-assistant/computations/term5_aK_audit.py` | landed (audit-only) | V1-V4 audit; **not** production-wired |
| `folio-assistant/computations/term5-aK-audit.witness.json` | landed (audit-only) | V1 backfill {p, n, D, T, ³He} |
| `folio-assistant/computations/probe_he4_model_b_knot_survey.py` | **DROPPED** | compositionality violation |
| `folio-assistant/computations/model-b-he4-knot-survey.witness.json` | **DROPPED** | compositionality violation |
| `docs/coordination/1ppb.md` (one ledger row) | **NOT cherry-picked** | replaced by this branch's integrated row |

### From #645 — H7a finding + Lean P4 audit

| File | Action |
|------|--------|
| `docs/audits/2026-05-12-delta-coupling-leading-term-followup.md` | landed |
| `docs/audits/2026-05-12-delta-coupling-residual-closure.md` | landed (H7a finding) |
| `docs/audits/2026-05-12-lean-gap-closeability-audit.md` | landed |
| `docs/audits/2026-05-12-lean-p4-canonical-instance-review.md` | landed |
| `folio-assistant/computations/probe_delta_coupling_leading_form.py` | landed (H1/H3/H4/H5) |
| `folio-assistant/computations/probe_delta_coupling_residual_closure.py` | landed (H6/H7/H8 — H7a is the win) |
| `folio-assistant/computations/delta-coupling-leading-form-probe.witness.json` | landed |
| `folio-assistant/computations/delta-coupling-residual-closure-probe.witness.json` | landed |
| `content/quantum-observable-universe/braids-and-knots/conj-magic-shell-stabilization.lean` | landed |
| `content/quantum-observable-universe/braids-and-knots/prop-rigid-monoidal-structural-gap-invariance.lean` | landed |

### From #652 — CODATA literal cleanup + new audit infra

| File | Action |
|------|--------|
| `.claude/skills/local/compute-audit.md` | landed |
| `docs/audits/2026-05-12-canonical-derivation-compute-review.md` | landed |
| `folio-assistant/computations/canonical_derivation_pipeline_compliance.py` (NEW) | landed |
| `folio-assistant/computations/canonical-derivation-pipeline-compliance.witness.json` (NEW) | landed |
| `folio-assistant/computations/witness_reproducibility_check.py` (NEW) | landed |
| `folio-assistant/computations/witness-reproducibility-check.witness.json` (NEW) | landed |
| 28 compute scripts with CODATA literal migrations | landed |
| `paper_six_term_isotope_sweep.py` CODATA imports | **re-applied on top of #644's version** |
| `d_from_scratch.py` CODATA import | **re-applied on top of #644's version** |

## Forward — next concrete step

The integration unblocks two natural forward steps. Per the user's
compositionality principle, the higher-leverage step is:

**F1. ⁴He compositional probe.** Build $\beta_{^4\mathrm{He}}$ as a
braid composition (D ⊕ D, T ⊕ p, or ³He ⊕ n) at the Model A
12-strand level. Compute $\tau_M(\beta_{^4\mathrm{He}})$ at $q_0$
via Hoefsmit seminormal × Wenzl-bridge $y_\lambda$ + recurse the
JSJ decomposition of the closure. Compare:

1. $T_1 = m_e \cdot \lvert \tau_M \rvert$ vs the survey's three
   in-window candidates ($8_{17}, 10_{123}, 8_{18}$).
2. Whether the compositional knot equals any of the surveyed
   candidates after JSJ reduction.
3. Whether all three composition paths (D⊕D, T⊕p, ³He⊕n) produce
   the same canonical knot — that would be a substrate-derived
   confirmation; if they disagree, the Model B mapping is itself
   ambiguous and needs structural narrowing.

**F2. H7a cross-anchor at (2,1) and (1,2).** Now that #644's
`magic-shell-empirical-instantiation.witness.json` is on the same
branch as #645's `probe_delta_coupling_residual_closure.py`, extract
$\Delta_{\mathrm{coupling}}$ at (Z, N) ∈ {(2, 1), (1, 2)} and test
the H7a form $[A-2]_q \cdot E_0 \cdot \log(1/h)$ at $A = 3$.
$[A-2]_q$ at $A = 3$ gives $[1]_q = 1$ exactly, so the prediction is
$E_0 \cdot \log(1/h(q_0)) \approx 6.55$ MeV — match this against
extracted $\Delta_{\mathrm{coupling}}(2,1)$ and $\Delta_{
\mathrm{coupling}}(1,2)$.

F2 is mechanical and small; F1 is substantive new compute. Both
should land as separate commits on this branch.

## PR closure rationale

PRs #644, #645, and #652 should be **closed without merging** — all
their canonical work is now on `claude/review-1ppb-prs-EC0ay` (this
PR, #654), with the two corrections above applied. Closing comments
should reference this integration audit + #654 as the surviving
trunk.
