# Binding magic-A wireup — the existing-but-unwired ⁴He formula

**Authored:** 2026-05-31
**Branch:** `claude/binding-magic-A-wireup-2026-05-31`
**Trigger:** Explaining why
[`binding-alpha-shift-extension`](../../content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean)
misses ⁴He binding by 5× (per the
[2026-05-31 status audit](2026-05-31-binding-alpha-shift-a4-status.md))
revealed the framework already carries a different formula that hits
⁴He to within 6% — but it isn't reachable from the §3b-cond class.

## Headline

For doubly-magic ⁴He (Z=N=2):

| Formula | Predicted B(⁴He) | Experimental | Miss |
|---|---:|---:|---:|
| `binding-alpha-shift-extension` (α_shift via T(3,4)) | 5.93 MeV | 28.30 MeV | **−79%** (5× too small) |
| [`magic_A_formula::magic_A_binding`](../../folio-assistant/computations/magic_A_formula.py) (ρ_F·m_e·A·8G, ρ_F=2) | 29.96 MeV | 28.30 MeV | **+5.9%** |

Wiring the existing magic_A path through for the doubly-magic case
closes the ⁴He gap by **13.5×** (|rel_err| from 0.7904 → 0.0587),
with zero new math required.

## What the framework already has (per existing code)

1. **`magic_A_formula.py`** — explicit:
   > *The reason ⁴He uses the magic-A rule rather than tr_M(T_w) is
   > that ⁴He has no single hyperbolic knot — it is doubly magic
   > (Z = N = 2, both magic) and the shell-closure structure replaces
   > the per-knot Markov-trace evaluation.*

2. **`prop:diagrammatic-double-magic-lr-fusion`** — algebraic content:
   - LR-fusion at double-magic is **rigid**: `V_λ ⊗ V_μ → V_ν` with
     multiplicity 1 and content sum zero.
   - *"no Wedderburn block at the double-magic level capable of
     absorbing further binding energy through Hecke channels"*
   - *"exceptional double-magic stability is the algebraic absence of
     decomposition channels, not a fitted shell-correction term"*

3. **`rem:strutinsky-from-graded-trace`** — the categorical
   decomposition is **forced**:
   $$
     \mathrm{tr}_M(T_w, q_0)
       = \mathrm{tr}_{\mathrm{gr}}(\sigma(T_w), q_0)
       + \mathrm{Res}_{\mathrm{GB}}(T_w, q_0)
   $$
   with the residue sum identified as the Strutinsky shell correction
   $\delta E_{\mathrm{shell}}$.  *"Magic-number enhancement arises
   algebraically when λ reaches a rectangular shape and H_q(λ)
   factorises"* (per `prop:shell-schur-weyl-self-duality`).

4. **`prop:shell-closure-normal-form`** (Lean ref:
   `qou:QOU.OptimalNF.optimal_nf_is_standard_basis`) — Poincaré
   distribution of the Hecke normal form at shell closure.

5. **`prop:gravity-spectral-prefactor`** — supplies the
   `8G = Vol(L6a4) = Vol(Borromean)` factor.

6. **`binding_ladder_catalog.py:63`** — supplies `ρ_F = 2` for ⁴He
   as `2·m_e·4·Vol(L6a4)`.

7. **`binding_shell_enhancement_derivation.py`** — the prior probe
   that confirmed the deuteron is exact and the A≥3 enhancement is
   "multiplicative per closure with f ≈ 2.45–2.88 (17% spread)",
   and refuted a single-q-power scalar closing it (p/n asymmetry kills
   any scalar derived factor).

## The wire-up gap

The §3b-cond class
[`BindingForceCarrierKnot`](../../content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean#L106)
takes a single `αShiftAt : ℕ → ℕ` per nucleus, embedding the
**implicit assumption** that every light nucleus has a single
hyperbolic force-carrier knot whose `k·(p−1)` pole order suffices.
For doubly-magic A's that assumption is false by construction — the
shell-closure rigidity means there is no single hyperbolic knot.

The current `lightNucleiForceCarrierKnot` instance dutifully maps
A=4 to `T(3,4)` per the agent-survey table, and gets the wrong
number (-79%). The categorical answer is "A=4 is in a different
regime; dispatch to magic_A".

## The minimal fix

Three options, in order of scope:

### Option 1 — Witness-side dispatch (this PR's deliverable)

Extend [`binding_alpha_shift_witness.py`](../../folio-assistant/computations/binding_alpha_shift_witness.py)
to compute and report **both** formulas for each candidate, with the
doubly-magic predicate dispatching to `magic_A_formula`. The witness
JSON now carries `B_predicted_magic_A_MeV` + `ratio_magic_A_over_exp`
for the ⁴He row alongside the original alpha_shift columns. Honest
audit; no Lean / canonical changes; closes the "what's the wire-up
look like" question.

**Status:** done in this PR. Output:

```
   A nucleus T(p,k)   α_shift     B_pred      B_exp  pred/exp
   2 D     T(2,3)         3     2.2246     2.2246    1.0000
   3 T     T(2,5)         5     3.7076     8.4818    0.4371
   3 ³He   T(2,5)         5     3.7076     7.7181    0.4804
   4 ⁴He   T(3,4)         8     5.9322    28.2957    0.2096
```

with the new gap report: *"For doubly-magic ⁴He the magic_A formula
B = ρ_F·m_e·A·8G predicts 29.956 MeV (+5.9% miss), closing the
alpha_shift gap by **13.5×** (|rel_err| 0.7904 → 0.0587)."*

The script dispatches to the canonical
[`magic_A_formula.magic_A_binding`](../../folio-assistant/computations/magic_A_formula.py)
rather than mirroring the formula locally; `VOL_BORROMEAN` is sourced
from `knot_volumes` (mpmath 50dps) via that import chain.

### Option 2 — Lean dispatcher class (DONE in this PR)

**Status:** completed via the new content block
[`prop:magic-A-binding-formula`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula.md).
The block triple ships:

- [`magic-A-binding-formula.ts`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula.ts) —
  manifest, `proposition` kind, `uses` cites
  `prop:binding-alpha-shift-extension`,
  `prop:diagrammatic-double-magic-lr-fusion`,
  `rem:strutinsky-from-graded-trace`.
- [`magic-A-binding-formula.md`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula.md) —
  narrative theorem statement (conditional on
  `conj:magic-numbers-bring` + `prop:gravity-spectral-prefactor`)
  with the two-regime dispatch table.
- [`magic-A-binding-formula.lean`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula.lean) —
  Lean §3b-cond formalisation:
  - `isMagic : ℕ → Prop` (magic-number predicate)
  - `isDoublyMagic Z N : Prop` (conjunction)
  - `class CatalanPrefactor R` (abstracts `8G` as a field-level
    parameter so the formula statement doesn't depend on
    Catalan-constant Mathlib import depth)
  - `class MagicABindingFormula B m_e` (the §3b-cond hypothesis
    bundling `ρ_F` per (Z, N) and the formula
    `B Z N = ρ_F · m_e · A · 8G`)
  - `theorem magic_A_binding_formula` — sorry-free conditional
    theorem discharging the formula from the class hypothesis
  - `theorem he4_is_doubly_magic` — `isDoublyMagic 2 2` proven by
    `Or.inl rfl`
  - `theorem two_regime_dispatch_exists` — non-trivial existence

Per CLAUDE.md §3b-cond: the formula is a rigorous-conditional
theorem — fully verified by Lean modulo the single class hypothesis
`MagicABindingFormula`. The class field `formula` discharges
definitionally for any concrete (Z, N) instance; the categorical
derivation of `ρ_F = 2` for ⁴He (Open Math A below) is the
remaining open content.

Chapter manifest
[`mass-theory.ts`](../../content/quantum-observable-universe/mass-theory/mass-theory.ts)
updated to include the new block after
`binding-alpha-shift-extension`.

### Option 3 — Canonical-side full-trace replacement (research)

Per the user's question: *"replace α_shift(T(p_A, k_A)) with the
full Markov-trace sum over ALL partitions."* This means folding the
two regimes into one: the binding becomes
`B = m_e · F[tr_M(β_atom)]` for the full Markov trace, where the
graded-trace + residue split (`rem:strutinsky-from-graded-trace`)
naturally produces the magic-A enhancement at doubly-magic Z, N via
the rectangular-partition spike. The `canonical_tr_m_via_branching.py`
infrastructure already computes the full trace; the binding wiring
would consume its output rather than the single-knot α_shift.

This is the right long-term path — it makes Option 2 a special case
(magic A's pick up the residue spike automatically) — but the
functional `F[·]` derivation and the `tr_M → B` calibration are
research-grade.

## ρ_F = 2 — what derives it? (reanalysed 2026-05-31)

**Status:** structurally answered by the existing block
[`conj:kashaev-density-equals-sdp-multiplicity`](../../content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md)
(landed 2026-05-24, Rule-14 escalation owner-authorised). The
identity is

$$
  \rho_F \;=\; \nu_{\mathrm{SDP}}
$$

where $\nu_{\mathrm{SDP}}$ is the joint-tower SDP Wedderburn
multiplicity of the canonical Hecke element $T_w$'s saturating SDP
solution. Driver (x) of the canonical 13-menu (MacMahon-style
partition-algebra multiplicity). Exact on the three SDP-confirmed
hyperbolic atoms:

| Atom | $K_w$ | $\rho_F$ (legacy) | $\nu_{\mathrm{SDP}}$ |
|------|-------|------:|------:|
| D | $6_2$ | 1 | 1 |
| T | $8_{11}$ | 2 | 2 |
| ³He | $L_{6a4}$ | 2 | 2 |
| ⁴He | magic A·8G | 2 | **extrapolated** |

**What remains open** (was previously framed as "Open Math A"):
extending the joint-tower SDP solver to produce
$\nu_{\mathrm{SDP}}(^4\mathrm{He})$ directly and confirm the value 2
(R&D follow-up per the kashaev-density block's `## Status` section).
The structural derivation is **not** open; only the numerical
verification for ⁴He is.

The `magic-A-binding-formula` Lean class hypothesis
`MagicABindingFormula.rho_F` can therefore be replaced (Sprint 2)
with a derivation from
[`conj:kashaev-density-equals-sdp-multiplicity`](../../content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md)
once the SDP-multiplicity Lean class is in place.

## Why was the resolution missed? (post-mortem)

The initial framing of this audit ($\rho_F = 2$ as "Open Math A",
single-magic A=3 p/n asymmetry as "Open Math B") was wrong: both
items had been structurally answered earlier in the framework. The
miss came from scoping against a single source file's status note
without cross-checking the broader corpus:

- $\rho_F$ derivation: I read `binding-alpha-shift-extension.lean`
  and `magic_A_formula.py` headers; both flagged $\rho_F$ as
  "pending formal justification" / "open math". I did **not** grep
  `docs/audits/` for the topic, where
  [`2026-05-24-rule14-kashaev-density.md`](2026-05-24-rule14-kashaev-density.md)
  recorded the owner-authorised resolution + the new content block
  `conj:kashaev-density-equals-sdp-multiplicity`.
- p/n asymmetry: I read `binding_shell_enhancement_derivation.py`'s
  conclusion ("$f_T \neq f_{³He}$ — no scalar q-factor closes it");
  framed this as "categorical object that carries p/n distinction
  not yet identified". I did **not** check `brings-surface/` (where
  [`conj:inter-nucleon-channel-color-tube`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md)
  identifies the structure) nor grep computations for
  `bring_color_weighted` (where the substrate-pure formula
  $f_{\mathrm{pn}} = z - h(1/2 - \delta/4)$ is already implemented
  in `closed_form_tau_M.py`).

**Pattern this session.** This is the *third* consecutive item in
this session that was framed as open but turned out to be already-
implemented: Track B Gap #2 (already in `canonical_tr_m_via_branching.py`,
PR [#1515](https://github.com/litlfred/qou/pull/1515));
α_shift A=4 instance (already in `lightNucleiForceCarrierKnot`,
PR [#1532](https://github.com/litlfred/qou/pull/1532)); and now
$\rho_F$ + p/n (this PR). Each time, the source file's stated
"open" status was treated as authoritative without cross-checking
the corpus.

**Corrective discipline** (to apply going forward, before declaring
any item "open"):

1. `grep -rln <topic> docs/audits/` — prior owner-authorised
   resolutions land as audit docs.
2. Search the full `content/` tree for related conjectures and
   propositions (especially in adjacent chapters — `brings-surface`,
   `observations`, `mass-theory` cross over).
3. Search `folio-assistant/computations/` for related Python:
   `pn_convention`, `nu_sdp`, the topic keyword, etc.
4. Cross-check the coordination ledger
   `docs/coordination/<theme>.md` for the topic.

The framework's own status notes lag the corpus by weeks or months;
the corpus is the source of truth. This audit's reanalysis section
above and the paper-block update reflect the corrected framing.

## A=3 (T, ³He) — what closes them? (reanalysed 2026-05-31)

The p/n asymmetry **is** structurally answered by two existing pieces
in the framework:

### 1. Bring color-tube weighting — IMPLEMENTED

[`folio-assistant/computations/closed_form_tau_M.py`](../../folio-assistant/computations/closed_form_tau_M.py)
already implements `pn_convention="bring_color_weighted"` with the
substrate-pure formula

$$
  f_{\mathrm{pn}}^{\mathrm{Bring}} \;=\; z - h \cdot (1/2 - \delta/4),
  \qquad
  \delta = \frac{\Delta m_{n-p}}{M_N} \approx 1.3697 \times 10^{-3}
$$

where $\delta$ comes from `_li_2_q_util.flavor_split_subleading(q)` —
**PROVED** (PR #690 / #942), substrate-pure with no fitted quark
masses. The arc-composition pattern for the four light nuclei:

| Atom | arc composition | $\tau_M$ (strict) | $\tau_M$ (Bring) | $\Delta$ (ppm) |
|---|---|---:|---:|---:|
| D | pn | +0.394985 | +0.395056 | +180.9 |
| T | pn, nn | +0.114801 | +0.114822 | +180.9 |
| ³He | pp, pn | +0.197225 | +0.197261 | +180.9 |
| ⁴He | pp, pn, nn | +0.057323 | +0.057333 | +180.9 |

The Bring correction is uniform at +180.9 ppm because each of the
four has exactly one pn arc. The **arc-composition asymmetry**
between T (pn,nn) and ³He (pp,pn) is what drives the very different
baseline values 0.115 vs 0.197 — that is the structural source of
the f≈2.82 vs f≈2.45 spread reported in
[`binding_shell_enhancement_derivation.py`](../../folio-assistant/computations/binding_shell_enhancement_derivation.py).

### 2. Quark color-sheet content — STATED in `conj:inter-nucleon-channel-color-tube`

The pn-arc factor uses the substrate-pure $\delta$ because the
proton's $(u, u, d)$ vs the neutron's $(u, d, d)$ color-sheet
content propagates through the Bring $\mathrm{SO}(3)$-fiber action
to give a $9$-element color-pair weight matrix $W_{c_1 c_2}(F_1, F_2)$
(per
[`conj:inter-nucleon-channel-color-tube`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md)).
The uniform-flavor projection (current production) collapses this
to a single $\sigma_{\mathrm{avg}}$; the Scheme-4 per-sheet
PL-integration probe on Bring reproduces $\Delta m_{n-p}$ to
$\sim 0.14\%$ vs $305$ ppm for uniform — third-line evidence that
this IS the categorical structure.

### What remains open (was previously framed as "Open Math B")

Three pieces are still genuinely open:

1. **Lean formalisation** of `conj:inter-nucleon-channel-color-tube`
   (conditional on `conj:s5-so3-fiber-action` per PR #1081 Task 3).
2. **Re-evaluation of the binding-shell enhancement** with
   `pn_convention="bring_color_weighted"`: does the 15% T vs ³He
   f-factor spread close when the closed-form $\tau_M$ baseline
   uses Bring weighting? The +180.9 ppm uniform correction is at
   the closed-form-ratio scale; the f-factor lives at the binding-
   energy scale — propagating through `binding_canonical` requires
   re-running
   [`binding_shell_enhancement_derivation.py`](../../folio-assistant/computations/binding_shell_enhancement_derivation.py)
   against the Bring-weighted ratio.
3. **Closed form for the $9$-element $W_{c_1 c_2}(F_1, F_2)$**
   weight matrix from the $\mathrm{SO}(3)$-fiber tensor (Open
   Question 1 of the inter-nucleon-channel-color-tube block).

None of the three is "no categorical object identified" — the
object IS identified (Bring color-tube weighting via $\delta$);
the residual work is verification + Lean formalisation, not
discovery.

## Action items

1. ✓ **This PR**: witness emitter shows the 13.5× ⁴He gap closure
   (|rel_err| 0.7904 → 0.0587) via the wired-in formula.
2. ✓ **This PR (now)**: Lean content-block triple
   `magic-A-binding-formula.{ts,md,lean}` ships the §3b-cond
   formalisation + chapter-manifest entry. The Lean theorem
   `magic_A_binding_formula` is sorry-free conditional on the
   `MagicABindingFormula` class hypothesis.
3. ✓ **Reanalysis 2026-05-31** (this commit, post-Bring-investigation):
   Open Math A and B are **structurally already answered** in the
   framework; "Open" was a framing error. ρ_F = ν_SDP per
   `conj:kashaev-density-equals-sdp-multiplicity` (driver x); p/n
   asymmetry per Bring color-tube weighting in `closed_form_tau_M.py`
   (`bring_color_weighted` mode, +180.9 ppm uniform at q_0, with
   the f-factor spread coming from arc-composition asymmetry).
4. **Research (remaining)**: full-trace functional derivation
   (Option 3 — collapses both regimes via Strutinsky); R&D
   follow-up: extend joint-tower SDP solver to verify
   ν_SDP(⁴He) = 2; re-run binding-shell-enhancement-derivation
   against the Bring-weighted ratio to check whether the 15% T vs
   ³He f-factor spread closes; Lean formalisation of
   `conj:inter-nucleon-channel-color-tube` (gated on
   `conj:s5-so3-fiber-action` PR #1081 Task 3).

## References

- [`binding-alpha-shift-extension.lean`](../../content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean) — the §3b-cond class that needs the dispatcher.
- [`magic_A_formula.py`](../../folio-assistant/computations/magic_A_formula.py) — the doubly-magic formula `B = ρ_F·m_e·A·8G`.
- [`binding_shell_enhancement_derivation.py`](../../folio-assistant/computations/binding_shell_enhancement_derivation.py) — prior shell-enhancement probe.
- [`prop:diagrammatic-double-magic-lr-fusion`](../../content/quantum-observable-universe/observations/diagrammatic-double-magic-lr-fusion.md) — LR-rigidity at double-magic.
- [`rem:strutinsky-from-graded-trace`](../../content/quantum-observable-universe/observations/strutinsky-from-graded-trace.md) — Strutinsky decomposition is forced by graded-trace residue split.
- [`magic-ladder-pattern-investigation.md`](../../folio-assistant/computations/magic-ladder-pattern-investigation.md) — confirms pure partition combinatorics doesn't pick out the magic ladder; the categorical input is required.
- [Binding A=4 already-closed audit (2026-05-31)](2026-05-31-binding-alpha-shift-a4-status.md) — the precursor finding.
- [Universal-branching multinucleon gap audit (2026-05-30)](2026-05-30-universal-branching-multinucleon-gap.md) — analogous "already-implemented" pattern (Track B Gap #2).
