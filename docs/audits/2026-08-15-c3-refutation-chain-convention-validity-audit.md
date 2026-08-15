# c₃ refutation chain vs the post-probe convention changes — validity audit

**Date:** 2026-08-15 · **Branch:** `claude/q-beta-fmap-c3-gap-er7fe3` ·
**Trigger:** owner redirect (critical-distance license): *"many compute fixes
landed since those probes ran — the C→D trace-convention change, the
color-weighting fixes, the canonical GGM V₃ = −7.693 correction, q₀ pin
documentation changes — so probes underlying the 'REFUTED as real-q fibre
element' verdict may be INVALID."* ·
**Probe:** [`qbeta_c3_ladder_trace_convention_sensitivity_probe.py`](../../computations/qbeta/qbeta_c3_ladder_trace_convention_sensitivity_probe.py)
(witness [`qbeta-c3-ladder-trace-convention-sensitivity.witness.json`](../../computations/qbeta/qbeta-c3-ladder-trace-convention-sensitivity.witness.json),
9/9 assertions, exit 0) ·
**Tier:** scope-(a) provenance audit; no convention adjudicated; no `c_k`
wired; no tier change; evidence-tiered per the anti-flip-flop guard (§8).

## Verdict up front

**The "REFUTED as real-q fibre element" verdict SURVIVES.** Its load-bearing
pillars are convention-immune, and this audit *measured* that rather than
assuming it (swing ratio D/C = **1.0052**).

**The value-level layer WEAKENS to convention-C-conditional.** Every ≈ −2
fact about c₃ — the extracted values −2.0693/−2.0202, (H1)
`c₃^even = −Vol(4₁)`, the `[3]_q/25` 2.65 ppm near-match, `J−ℏ²`,
`S_leak = c₃ + Vol(4₁)`, `q*_S`, and the KC21/KC22 D-ladder constants — is
extracted through a ladder that consumes the **convention-C** Markov
parameter. Re-extracting the same ladder shape with the convention-D `z`
shifts c₃ by ≈ −972 (to ≈ −974.4). This was invisible because **the Q_β
channel is not registered in the trace-convention registry** (channels:
`mass`, `binding`, `borromean-binding-single-pipeline` only — all D since
2026-08-09).

**One finding is larger than the redirect anticipated:** even the canonical
rung **c₂ = −1 (Lean-proved, Taylor-exact) is a C-frame statement.** The
implied empirical c₂ under D is ≈ −9.30, and the ladder's rung-by-rung
convergence (N2 improves N1 by 58× under C) disappears under D (1.12×). The
C→D excision therefore does **not** transfer to the Q_β channel by a z-swap;
it would require re-deriving the ladder from the D-trace — an open derivation
question, not a mechanical migration.

## 1. The convention changes audited

| change | date | scope | reaches the c₃ chain? |
|---|---|---|---|
| **C→D trace flip** (`z: √q/(1+q) → q³/(q²+1)`, +22.7% at q₀) | owner ruling 2026-08-09; gram.py/trace_formal.py 2026-08-15 (PR #5055); 54 witnesses regenerated | `mass`, `binding`, `borromean` channels of [`trace-convention-registry.json`](../coordination/trace-convention-registry.json) | **YES — unregistered.** The Q_β N=1 rung phase is `α = (z−1)h/2` with `z = √q/(1+q)` ([`qbeta_utils.py:124-125`](../../computations/qbeta/qbeta_utils.py)); same `z_C` in the D-ladder core ([`qbeta_ck_sseries_exact_rational.py:20,248`](../../computations/qbeta/qbeta_ck_sseries_exact_rational.py)) and in the KC13 Lean certificate ([`ZBarParity.lean:59-79`](../../content/quantum-observable-universe/lean/QOU/QBeta/ZBarParity.lean)). The registry has **no Q_β channel**. |
| **Color-weighting fixes** (`bring_color_weighted`, p/n interface ctype) | 2026-08 | mass/binding p–n interface (`closed_form_tau_M.py`) | **NO.** Grep over `computations/qbeta/` + the pillar probes: the only reference is `qbeta_habiro_phase5q_dn_refactorize.py`, not a refutation pillar. |
| **Canonical GGM V₃ = −7.693** | 2026-07-30 | Habiro/GGM assembly scans | **Already incorporated.** The B1 assembly re-run *was* the V₃-correction re-run ("0 hits in 180; old near-misses were artifacts of wrong V₃" — registry §3 c₃ row). |
| **q₀ pin changes** (proton default directive 2026-08-07) | 2026-08-07 | reporting layer | **No value change.** The probe's C-frame regression reproduces the committed c₃ values from the *current* `q_at()`/`q_muon_at()` constants; the cross-anchor pillars evaluate both pins by construction. |

## 2. Pillar classification

Verdict values: **VALID-immune** (convention-independent, survives as stated) ·
**VALID-C-scoped** (proved/true, but a statement about the C-frame object —
survives with its scope named) · **C-CONDITIONAL** (value-level; holds only
in the C frame).

| # | pillar | evidence site | convention dependence (file:line) | verdict |
|---|---|---|---|---|
| P1 | cross-anchor rigidity falsification of `[3]_q/25`, `J−ℏ²` | [2026-06-04 audit](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md); `probes/qbeta_c3_habiro_3rung_crossanchor_rigidity_probe.py` | rigidity **logic** (a smooth formula swings 4.7×10⁶× less than the extracted target) is z-free; the hardcoded `EMPIRICAL_C3_*` targets are C-frame (and its muon −2.0097 is the pre-#1824 value, superseded by −2.0202 — value staleness already reflected in the registry window) | **VALID-immune (mechanism)**; targets C-conditional |
| P2 | `dc₃/dq ≈ 4.6×10⁶` smoothness kill (PR #1821) + capstone `1/u³` (#3636) | [capstone](2026-07-12-c3-wall-resolution-capstone.md) | `u = b·ℏ_q²` and `Q_A` are z-free; **measured** swing_D/swing_C = 1.0052 | **VALID-immune (measured)** |
| P3 | P4 entropy bound — c₃ has ≤ 2.2 reliable digits/anchor (PR #3536) | `qbeta-ck-basis-constrained-pslq.witness.json` | `σ(c₃) = σ(Q_β)/(Q_N2·u³)`; Q_N2 moves 6×10⁻⁴ *relative* under D — bound unchanged | **VALID-immune** |
| P4 | q→1 shadow `G(0,1) = −2` (longitude norm form, 2026-07-30) | registry §3 c₃ row | pure cusp arithmetic; `z_C(1) = z_D(1) = 1/2` exactly, so KC10 shadow gates are convention-blind at the classical point | **VALID-immune** |
| P5 | B1 GGM assembly 0/180 at V₃ = −7.693 (2026-07-30) | registry §3 c₃ row | already canonical-V₃ (it *was* the correction re-run); its match target was the C-frame c₃ ≈ −2.07 | **VALID as a C-frame negative** |
| P6 | KC20 ζ₄-residue exclusion + trace-cubic certificate | [`QBetaZeta4ResidueRefutation.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QBetaZeta4ResidueRefutation.lean) | `Δ_net` numerator `q¹⁴−5q¹²+…` is a pure even-power Laurent polynomial — **z-free** | **VALID-immune** |
| P7 | KC21/KC22 D-ladder: exact `d_k ∈ ℚ(√3)`, radius `ρ`, `h·D(ũ₀)` 38-digit pin | `qbeta_ck_sseries_exact_rational.py` | the `d_k` are Taylor data of `log R` with `R = Q_β/(Q_A·cos α)` and `α` built on `z_C` (lines 20, 248; consumed by the generating-function producer at line 123) — C-frame end-to-end. The radius *object* `R₁₂`/`Δ_net` is z-free, but "the ladder whose radius it is" is the C-frame ladder | **C-CONDITIONAL** |
| P8 | KC13 "z exactly bar-even" (+ KC18/KC19 eval-map parity split downstream) | `ZBarParity.lean:59-79` | proved for `z_C = s/(1+s²)`, `s=√q`. **Exact (sympy 0):** `bar(z_D) = q⁻⁴·z_D` — convention D's trace parameter is NOT bar-invariant | **VALID-C-scoped** — the "no scalar z-functional sources the odd channel" prune does not transfer to D as stated |
| P9 | value layer: extracted c₃ = −2.0693/−2.0202; (H1) −Vol(4₁); `[3]_q/25` 2.65 ppm; `J−ℏ²`; `S_leak`; `q*_S`; registry §9b/§9e/§9f error analyses | throughout | re-extraction under D: c₃ → ≈ −974.4; `\|c₃_D + Vol(4₁)\| ≈ 972` (vs 0.0097–0.0395 under C) | **C-CONDITIONAL (all)** |
| P10 | canonical rung c₂ = −1 (Lean-proved Taylor-exact, PR #1602) | `q-beta-c-2-eq-neg-one-structural.lean` | implied empirical c₂: **−1.0176 under C** (= −1 + c₃u, as expected) vs **−9.299 under D**; N2/N1 residual ratio 0.017 (C) vs 0.89 (D) | **VALID-C-scoped** — proved for the C-frame ladder object; the frame was implicit until now |

## 3. Why the refutation survives — stated plainly

The registry's "REFUTED as real-q fibre element" rests on the **anchor-swing
mechanism**: the extracted c₃ swings −2.88% across a 1.28×10⁻⁸ anchor
separation while any smooth real-q formula is rigid, because the extractor
divides an O(1)-sensitive numerator by `u³ ≈ 6×10⁻⁷`. Both ingredients —
`u(q)` and the dominant `Q_A(q)` sensitivity — contain no `z`. Measured: the
swing under D is 0.0494 vs 0.0491 under C (ratio 1.0052). **A real-q closure
fails the cross-anchor test identically under either convention.** P3, P4,
and P6 are likewise convention-free. The refutation does not weaken; if
anything it now holds in two frames.

## 4. What weakens, and how to say it

Scope-(a), and symmetric — the same care as §9c's treatment of (H1):

- **Nothing here refutes the C-frame values.** Convention C was excised from
  the *mass/binding* channels by a forcing argument specific to those
  channels (the two-row cap `ℓ(λ) ≤ 2` / `y_(1³) = 0` of
  `2026-08-08-mass-fibre-dimension-forces-convention-d.md`). Whether that
  forcing transfers to the **decay** channel is unexamined — the β channel's
  explicit Markov-weight instance (`y = (z, 1/2−z, z)`,
  `prf:qbeta-canonical-markov-weights-explicit-instance`) has `y_(1³) ≠ 0`,
  i.e. it genuinely uses the third row. If the decay channel legitimately
  carries the full-Hecke trace, the C-frame c₃ record stands as the Q_β
  channel's own convention.
- **But the conditionality must be carried explicitly from now on.** Every
  ≈ −2 statement about c₃ is a statement about the C-frame extraction. A
  registry row, witness, or audit that quotes c₃ ≈ −2.02/−2.07, (H1), or
  `q*_S` without naming the convention is exactly the failure mode the
  trace-convention registry was built for (its own rule: *"Convention-silent
  trace values are not comparable"*), and the Q_β channel has been
  convention-silent since the registry was created.
- **KC13's prune is C-scoped, not false.** Under D the trace parameter itself
  carries an exact `q⁻⁴` bar-twist. This audit does **not** claim the odd
  channel is sourced by `z_D` — only that the KC13-based exclusion was proved
  for `z_C` and does not transfer as stated. Re-examining the odd-channel
  sourcing under D is part of the open item below, not a result.

## 5. The open item (bean `qou-b3nk`)

**Register the Q_β channel in `trace-convention-registry.json` and settle its
convention** — either (a) derive that the decay channel carries the
full-Hecke (C-type) trace (its `y_(1³) ≠ 0` instance suggests the two-row
forcing does *not* apply — but that is an observation, not a derivation), or
(b) show the two-row forcing transfers, in which case the entire Q_β ladder
(c₂ = −1 included) needs re-derivation from the D-trace and the c₃ value
record is superseded, or (c) register it as `disputed` with this audit as the
open_item. Until settled, the channel status is **unregistered/disputed** and
every consumer of c₃ values should cite this audit.

Formalize-first note for whoever takes it: the decision object is the
decomposition of the β-decay channel's H₃ representation — the mass channel's
forcing came from `markovWeights_eq_jones_of_threeRow_eq_zero` (sorry-free) +
the mass chapter's own row cap; the analogous question is whether the decay
channel's decomposition kills the third row. That is a Lean-sized question,
not a scan.

## 6. Witness / probe staleness notes (mechanical)

- `qbeta-c3-habiro-3rung-crossanchor-rigidity.witness.json`: recorded
  `scriptHash d79c91ed99e0`; its hardcoded muon target (−2.0097) is the
  pre-#1824 value — **value-stale, mechanism unaffected** (the registry
  window already carries the corrected −2.0202).
- The re-run demanded by the redirect is this audit's probe (fresh, current
  q₀ constants, 60 dps, teed log per the long-compute discipline —
  runtime < 10 s).
- No witness file was edited; none reports a wrong number *for what it
  computed*. The staleness class here is **semantic** (convention-silent
  values), the same class as the 2026-08-09 D-ladder convergence correction.

## 7. Registry actions taken in this PR

- §3 c₂ and c₃ rows: convention-provenance clauses added (frame named; no
  tier change — c₂ stays CANONICAL *for the C-frame ladder object*, c₃ stays
  EMPIRICAL/REFUTED-as-real-q).
- KC13, KC21, KC22: C-scope notes added (.md **and** JSON twin;
  `kernel_constraints_registry_validate.py` run clean).
- New §9g: consolidated convention-provenance statement.
- Ledger row: [`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
- Beans: `qou-b3nk` (new, the open item); notes appended to `qou-qb8e`,
  `qou-qb8g` (their fibre-carrier target `q*_S` inherits the C-frame
  conditionality).
