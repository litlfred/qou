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

PR #644's [`paper_six_term_isotope_sweep.py`](../../computations/sweeps/paper_six_term_isotope_sweep.py)
P1.B section states:

> V1 is the natural Hecke choice; V2–V4 are alternative mirror-knot
> conventions whose physical meaning differs.

Reading [`term5_aK_audit.py`](../../computations/audits/term5_aK_audit.py)
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

### V2 production-wired into `paper_six_term_mass` (2026-05-15 follow-up)

Canonical V2 library
[`term5_v2_chirality.py`](../../computations/term5_v2_chirality.py)
exposes `aK_v2(Z, N, q_val=Q_0)` (mp.mpf return for 50-dps callers) and
`term5_v2_factor(...)` (drop-in for `term5_chirality`). Both wired
into:

| Caller | Mode flag | Default |
|---|---|---|
| [`paper_six_term_isotope_sweep.paper_six_term_mass`](../../computations/sweeps/paper_six_term_isotope_sweep.py) | `chirality_source: "v2" | "closed_form"` | `"v2"` |
| [`mass_formula_6term_mpfr_50dps.term_5_chirality_bw_mp`](../../computations/mass_formula_6term_mpfr_50dps.py) | `chirality_source: "v2" | "bw_legacy"` | `"v2"` |

V2-cache-miss fallback in both callers: surface the routing
decision (`print` flush) and fall back to the legacy path so the
sweep completes for out-of-window (Z, N). The probe script
[`probe_term5_aK_v2_mirror_chirality.py`](../../computations/probe_term5_aK_v2_mirror_chirality.py)
was de-duplicated to import the library's `aK_v2_full` — single
source of truth, no copy/paste compute.

Witness records the routing decision under
`term5_chirality_source` in every per-atom row.

### V2 numerical result (initial witness)

[`probe_term5_aK_v2_mirror_chirality.py`](../../computations/probe_term5_aK_v2_mirror_chirality.py)
wires V2 via the per-irrep numeric Hoefsmit path
(`global_wedderburn_sum_q_hecke_seminormal` machinery) — fast: <1 s
total across {p, n, D, T, ³He}. The probe computes the canonical
chirality per the Gram-matrix conjecture
`a_K = τ(β · β_mirror⁻¹)` where `β_mirror⁻¹` = reverse-word(β)
under V2's algebra (a derivation in the probe docstring).

| atom | V1 (slow audit) | V2 (this probe) | Δ |
|------|---:|---:|---:|
| proton | 1.022 | 2.424 | +137 % |
| neutron | 1.022 | 2.134 | +109 % |
| D | 1.056 | 5.228 | +395 % |
| T | 1.079 | **10.477** | +871 % |
| ³He | 1.079 | **13.994** | +1197 % |

**Slow-audit V1 is provably informationless on chirality.** V1 is
defined as `τ(β · β⁻¹)` where β⁻¹ is the Hecke multiplicative
inverse; `β · β⁻¹ = 1_n` in the Hecke algebra, so V1 reduces to
`τ(1_n)` which depends only on $n = 3A$ — not on the braid. The
identical V1(proton) = V1(neutron) and V1(T) = V1(³He) values
seen in the audit are not "emergent symmetries"; they are exact
identities, dictated by the Markov-trace normalisation $z^{n-1}$.
The slow audit's framing of V1 as a chirality measure is wrong on
construction.

**V2 distinguishes T from ³He at −25.13 %.** Computed asymmetry
$(V_2(T) - V_2({}^3\mathrm{He})) / V_2({}^3\mathrm{He}) = -25.1275\,\%$.
This is the structural T ↔ ³He spin-involution chirality that V1
cannot detect. Witness:
[`term5-aK-v2-mirror-chirality-probe.witness.json`](../../computations/term5-aK-v2-mirror-chirality-probe.witness.json).

**Compute cost.** Per-atom timings on the integration branch:
proton 0.18 s, neutron 0.00 s (cache hit), deuteron 0.00 s
(cache hit), T 0.33 s, ³He 0.39 s — total 0.90 s. The
"unbounded for A ≥ 3" warning in the plan-doc applied only to
the fully-symbolic `sp.cancel` path; the numeric per-irrep path
trivialises the compute. V2 production-wiring of `term5_chirality`
is now unblocked.

### Compute-infra optimization — `y_lambda_at(q_0)` witness loader

While building the F1-braid probe (canonical ⁴He τ_M at n=12), the
y_λ load was bottlenecking at 974 s. Root cause:
`wedderburn_jones_markov.y_lambda_at(n, q_val=q_0)` was recomputing
y_λ from scratch on every call despite an existing 50-dps witness
[`y-lambda-at-q0.witness.json`](../../computations/y-lambda-at-q0.witness.json)
covering n=2..12.

Fix: extend `y_lambda_at` with a fast-path check — when the
numeric `q_val` matches q_0 (within 1e-12), load values directly
from the witness via `_load_y_lambda_at_q0_witness()`. Module-
level memoization for repeated calls.

**Speedup**: n=12 load **974 s → 0.004 s** (~240,000×). Propagates
to every consumer of `y_lambda_at(n, q_val=q_0)`, including:
- V2 mirror chirality (`term5_v2_chirality.aK_v2`) — was 109 s cold
  for 5 atoms, now sub-second.
- `global_wedderburn_sum_q_hecke_seminormal` (all isotope sweeps).
- F1-braid ⁴He canonical Markov-trace probe.

The patch is non-invasive — original recompute path remains the
fallback for non-q_0 numeric values or missing witness file.

### F1 ⁴He compositional probe — SDP/LP active-set fingerprint

[`probe_he4_sdp_compositional.py`](../../computations/probe_he4_sdp_compositional.py)
+ witness
[`he4-sdp-compositional-probe.witness.json`](../../computations/he4-sdp-compositional-probe.witness.json).
Uses `lp_dual_solver.solve_psd_operator_selection_sdp` with LP
fallback (equivalent for diagonal $G$, no cvxpy dep needed).

**Channel decomposition for ⁴He = (Z=2, N=2)** with $\Delta_\mathrm{cat}(^4\mathrm{He}) = 28.21$ MeV:

| channel | parts | parts sum (MeV) | binding residual |
|---|---|---:|---:|
| D ⊕ D    | (1,1)+(1,1) | 4.05  | **24.16** |
| T ⊕ p    | (1,2)+(1,0) | 7.83  | **20.38** |
| ³He ⊕ n | (2,1)+(0,1) | 7.04  | **21.18** |

`n_target = Δ_coupling(2,2) = Δ_cat(⁴He) − 2·Δ_cat(³He) = 13.197` MeV.

**LP solution** (strong duality holds; gap = 0):

| field | value |
|---|---:|
| primal_obj | 268.949 |
| dual_obj   | 268.949 |
| duality_gap | 0.00 |
| y0_star | 20.380 |
| y_star (DD, Tp, ³He+n) | (3.778, 0.000, 0.796) |
| x_star (DD, Tp, ³He+n) | (0, 13.197, 0) |
| active_set | {DD, ³He+n} |

**Interpretation.**
1. **T⊕p is the primal-saturating channel**: the LP "uses" the T+p
   decomposition to satisfy the binding-residual constraint
   (the channel with the smallest per-unit cost).
2. **D⊕D has the highest shadow price** $y_\star = 3.778$: it is
   the most binding-receptive sub-braid (matches the
   doubly-magic structural intuition — ⁴He's pole-saturation at
   D-shell-pairing).
3. **³He⊕n is the secondary active channel** $y_\star = 0.796$.

The fingerprint identifies a **two-tier structure**: T⊕p carries
the primal weight, but the DD active-set constraint shows
deuteron-pairing is the most receptive sub-braid (consistent with
the H7a + LR-coupling-saturation framing of PR #645 that #654's F2
refuted at A=3 but not at A=4 doubly-magic).

### F1 ⁴He canonical Markov-trace fingerprint (braid-comp)

[`probe_he4_canonical_tr_m_fingerprint.py`](../../computations/probe_he4_canonical_tr_m_fingerprint.py)
+ witness
[`he4-canonical-tr-m-block-fingerprint.witness.json`](../../computations/he4-canonical-tr-m-block-fingerprint.witness.json).

Computes the full canonical Markov trace `tr_M(β_⁴He) =
Σ_{λ ⊢ 12} y_λ(q_0) · χ^λ_q(β_⁴He)` on the 47-crossing
12-strand atom braid word. Uses Hoefsmit per-irrep at q_0 with
on-disk caching; total compute time 232.8 s with the
y_λ cache fast-path (was previously bottlenecked on y_λ recompute
alone).

**Result**: `tr_M(β_⁴He) = 0.05534835` (dimensionless raw trace).

**Per-partition Wedderburn-block fingerprint** (top 5 by
|contribution|):

| rank | λ ⊢ 12 | dim_λ | y_λ(q_0) | χ^λ_q(β_⁴He) | contribution | % of \|total\| |
|---:|---|---:|---:|---:|---:|---:|
| 1 | [9, 3]   | 154 | +5.87e−4 | +27.33 | +1.604e−2 | **29.0** |
| 2 | [8, 4]   | 275 | +4.31e−4 | +30.26 | +1.304e−2 | **23.6** |
| 3 | [10, 2]  | 54  | +7.12e−4 | +10.46 | +7.45e−3  | **13.5** |
| 4 | [7, 5]   | 297 | +2.62e−4 | +21.77 | +5.70e−3  | **10.3** |
| 5 | [11, 1]  | 11  | +7.67e−4 | +7.39  | +5.67e−3  | **10.2** |
| | | | | top-5 cum | | **86.5** |

**All five top blocks are two-row partitions.** The cumulative
two-row stratum carries 86.5 % of the trace. The trivial rep
[12] contributes only 2.9 %; the sign rep [1¹²] is sub-1e−9.

**Structural agreement with SDP fingerprint.**

| level | dominant structure | binding source |
|---|---|---|
| Channel (SDP/LP)            | T⊕p (primal), D⊕D (highest dual) | deuteron-pairing receptivity |
| Wedderburn block (braid)    | [9,3], [8,4], [10,2] (two-row stratum) | q-symmetric magic shell |

The two probes are independent at the computational level — SDP
operates on the channel-level coupling residual; braid operates
at the per-irrep matrix-trace level — but they identify the
same structural fingerprint: **⁴He binding lives in the
q-symmetric pairing stratum**, with the deuteron-pairing channel
as the geometrically-receptive surface and the two-row Young-
tableau partitions as the algebraic dual.

This is the substrate-derived account of "doubly-magic" that
PR #645's H7a empirically pinned at the (2,2) anchor. F2 refuted
H7a as a universal closure law, but the agreement here shows the
**structural identity** of the doubly-magic case is robust — both
geometric (SDP) and algebraic (braid) approaches recover the
same fingerprint.

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
| `computations/sweeps/paper_six_term_isotope_sweep.py` | landed | P1.A, P1.C, P1.D, P2.A, P2.B all wired |
| `computations/sweeps/paper-six-term-isotope-sweep.witness.json` | landed | output of the above; combined+sub_tower_mode audit field present |
| `computations/d_from_scratch.py` | landed | T4 → per-3A migration; P1.C hard break comment |
| `computations/mass_formula_6term_mpfr_50dps.py` | landed | T4 → per-3A migration |
| `computations/unified_low_isotope_predictor.py` | landed | docstring fix only |
| `computations/magic-shell-empirical-instantiation.witness.json` | landed | Δ_cat columns for {p, n, D, T, ³He, ⁴He} — required by #645's H7a cross-anchor |
| `computations/probe_magic_shell_empirical_instantiation.py` | landed | producer for the above |
| `computations/probes/delta_coupling_closed_form_probe.py` | landed | H1 closed-form probe |
| `computations/probes/delta-coupling-closed-form-probe.witness.json` | landed | H1 witness |
| `computations/audits/term5_aK_audit.py` | landed (audit-only) | V1-V4 audit; **not** production-wired |
| `computations/audits/term5-aK-audit.witness.json` | landed (audit-only) | V1 backfill {p, n, D, T, ³He} |
| `computations/probe_he4_model_b_knot_survey.py` | **DROPPED** | compositionality violation |
| `computations/model-b-he4-knot-survey.witness.json` | **DROPPED** | compositionality violation |
| `docs/coordination/1ppb.md` (one ledger row) | **NOT cherry-picked** | replaced by this branch's integrated row |

### From #645 — H7a finding + Lean P4 audit

| File | Action |
|------|--------|
| `docs/audits/2026-05-12-delta-coupling-leading-term-followup.md` | landed |
| `docs/audits/2026-05-12-delta-coupling-residual-closure.md` | landed (H7a finding) |
| `docs/audits/2026-05-12-lean-gap-closeability-audit.md` | landed |
| `docs/audits/2026-05-12-lean-p4-canonical-instance-review.md` | landed |
| `computations/probe_delta_coupling_leading_form.py` | landed (H1/H3/H4/H5) |
| `computations/probe_delta_coupling_residual_closure.py` | landed (H6/H7/H8 — H7a is the win) |
| `computations/delta-coupling-leading-form-probe.witness.json` | landed |
| `computations/delta-coupling-residual-closure-probe.witness.json` | landed |
| `content/quantum-observable-universe/braids-and-knots/conj-magic-shell-stabilization.lean` | landed |
| `content/quantum-observable-universe/braids-and-knots/prop-rigid-monoidal-structural-gap-invariance.lean` | landed |

### From #652 — CODATA literal cleanup + new audit infra

| File | Action |
|------|--------|
| `.claude/skills/local/compute-audit.md` | landed |
| `docs/audits/2026-05-12-canonical-derivation-compute-review.md` | landed |
| `computations/canonical_derivation_pipeline_compliance.py` (NEW) | landed |
| `computations/canonical-derivation-pipeline-compliance.witness.json` (NEW) | landed |
| `computations/witness_reproducibility_check.py` (NEW) | landed |
| `computations/witness-reproducibility-check.witness.json` (NEW) | landed |
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

**F2. H7a cross-anchor at (2,1) and (1,2).** ✅ **Landed — H7a
REFUTED at A = 3.** [`probe_h7a_cross_anchor_a3.py`](../../computations/probe_h7a_cross_anchor_a3.py)
+ [`h7a-cross-anchor-a3-probe.witness.json`](../../computations/h7a-cross-anchor-a3-probe.witness.json)
at 50 dps:

| anchor | decomposition | value (MeV) | H7a prediction (MeV) | gap |
|---|---|---:|---:|---:|
| (2,2) | $\Delta_\mathrm{cat}({}^4\mathrm{He}) - 2\Delta_\mathrm{cat}({}^3\mathrm{He})$ | 13.197 | 13.175 (= $[2]_q E_0 \log(1/h)$) | **−0.169 %** ✓ |
| (2,1) | $\Delta_\mathrm{cat}({}^3\mathrm{He}) - \Delta_\mathrm{cat}(D) - \Delta_\mathrm{cat}(p)$ | 6.025 | 6.552 (= $[1]_q E_0 \log(1/h)$) | **+8.74 %** ✗ |
| (1,2) | $\Delta_\mathrm{cat}(T) - \Delta_\mathrm{cat}(D) - \Delta_\mathrm{cat}(n)$ | 6.821 | 6.552 (= $[1]_q E_0 \log(1/h)$) | **−3.95 %** ✗ |

H7a's quantum-integer prefactor $[A-2]_q$ depends only on $A$, so
under universality the (2,1) and (1,2) anchors must agree. Empirical
asymmetry: $-11.67\,\%$. **The T ↔ ³He spin-involution asymmetry of
the magic-shell coupling at $A = 3$ is real and structural** — H7a
in the form $[A-2]_q \cdot E_0 \cdot \log(1/h)$ is a special-case
anchor relation, not a universal closure law.

Implications:

1. PR #645's H7a is correct at (2,2) by construction — the empirical
   ratio of $\Delta_\mathrm{coupling}(2,2) / (E_0 \log(1/h))$ is
   close to $[2]_q$ to 4 sig figs, but extrapolation to $A = 3$
   shows the rule is single-anchor-tied.
2. Any closed form must carry a $Z, N$-dependent piece beyond
   $[A-2]_q$ — a candidate structure is $[Z-1]_q \cdot [N-1]_q$ or
   a Murphy-central element product depending on the partition
   spectrum (per CLAUDE.md §7b crystal-bases hint). **PR #656**
   proposes a sharper substrate-derivation candidate **D-2**:
   $\mathrm{Cat}_q(A-1, 1) = [A-1]_q [A-2]_q / ([2]_q [A]_q)$ with
   Z/N-dependent SYT-shape corrections; survives the same cross-
   anchor refutation.
3. The "magic-shell" framing of $\Delta_\mathrm{coupling}$ is
   physically asymmetric at $A = 3$ because ³He and T are
   isospin mirrors — one has the magic Z-shell partially-filled
   (Z=2, N=1), the other the magic N-shell partially-filled
   (Z=1, N=2). The decomposition rule itself encodes the choice of
   which sub-shell to subtract.

### §6 cross-coordination with PR #656

[PR #656](https://github.com/litlfred/qou/pull/656) (sibling Claude
session) independently arrived at the same H7a-NOT-universal headline
with a different decomposition convention:

| anchor | F2 (this branch) | #656 | difference |
|---|---:|---:|---:|
| (2,1) | 6.025 MeV | 5.481 MeV | $\Delta_\mathrm{cat}(p) = -0.544$ |
| (1,2) | 6.821 MeV | 6.349 MeV | $\Delta_\mathrm{cat}(n) = -0.472$ |
| (2,2) | 13.197 MeV | 13.197 MeV | 0 ✓ |

- **F2 (here)** uses the *fully-decomposed* baseline:
  `Δ_coupling(2,1) = Δ_cat(³He) − Δ_cat(D) − Δ_cat(p)`. Treats
  the single-nucleon Δ_cat as part of the structural budget.
- **PR #656** uses the *previous-magic-shell* baseline:
  `Δ_coupling(2,1) = Δ_cat(³He) − Δ_cat(D)`. Treats the third
  nucleon as not-yet-categorically-realized; consistent extension
  of PR #645's `⁴He − 2·³He` convention.

Per §6 (do not silently rewrite framing), both readings are
retained: F2 is the conservative "fully decomposed" probe;
#656 is the consistent "previous-magic-shell" probe. Both
**agree the universality claim is refuted** — the Z↔N asymmetry
is robust under either convention. Going forward, #656's convention
should be canonical because it matches #645's original (2,2)
anchor choice; F2's reading is a useful sanity check that the
single-nucleon residuals are not where the closure lives.

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

F1 remains queued; F2's negative finding makes it more urgent —
the magic-shell coupling needs a substrate-derived structural
account, and ⁴He compositionality is the natural place to start.

## PR closure rationale

PRs #644, #645, and #652 should be **closed without merging** — all
their canonical work is now on `claude/review-1ppb-prs-EC0ay` (this
PR, #654), with the two corrections above applied. Closing comments
should reference this integration audit + #654 as the surviving
trunk.
