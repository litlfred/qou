# CAL-2 (m_μ/m_e) cohomological derivation vs calibration — critical-analysis audit

**Date:** 2026-05-25
**Branch:** `claude/busy-lamport-5NS40`
**Owner question (paraphrased):**

> "Really m_μ/m_e should be over ℝ or some categorically derived
> object from ℝ — independent of physics, even before the mass-tower
> operator endomorphism. Is it the first lepton generation? Is that
> the scalar we're getting cohomologically? Then the second generation
> is either a derivative of that scale or a distinct scale. We need
> to explain it cohomologically. Can we re-look at m_e and β in this
> context? Paper may be wrong. Investigate, do critical analysis."

## TL;DR

The owner's critique is **structurally correct**. The paper's
"3 calibrations align bijectively to 3 (co)homological degrees"
framing
([`three-calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md),
[`three-calibration-discipline.md`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md),
[`three-parameters-wedderburn.md`](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md))
is internally tense:

1. **CAL-2 is self-referential.** The paper says
   `m_μ = m_e · Vol(4_1)/ℏ_q²` is *"the first prediction, by
   construction matches calibration input."* This is circular —
   m_μ/m_e is the input that pins q_0 via this equation, then m_μ
   is the "first prediction" via the same equation. The Lean
   cross-check `figure-8-muon-mass-cross-check.lean:36-42` says
   the equality holds *"by construction."* That is the textbook
   definition of a tautology, not a prediction.
2. **Vol(4_1) IS cohomological — but q_0 is calibrated.** The
   hyperbolic volume of the figure-eight knot is a deep topological
   invariant (Lobachevsky-Λ(π/3) closed form). The formula
   `m_μ/m_e = Vol(4_1)/ℏ_q²` is cohomologically structured, but the
   substrate-q_0 derivation was declined ("subgoal-2 out of scope,"
   per coordination ledger 2026-05-08).
3. **m_e in natural units IS cohomologically derived.**
   `calibration-inputs.md:32-36` gives
   `m_e(natural) = Li_2(q^{-2})/ℏ_q² ≈ 112`. This is a polylog
   (motivic) period. CAL-1 reduces to a single unit choice
   (MeV ↔ natural units).
4. **β is being recast cohomologically by sibling PRs.** PR #1127
   already found `Q_β = |Δ(net)|·E_0` is **postulated, not derived.**
   Audit
   [`2026-05-18-qbeta-n5-cohomological-breakdown.md`](2026-05-18-qbeta-n5-cohomological-breakdown.md)
   proposes Q_β-rungs as traces over **Khovanov-Rozansky
   cohomology strata** of the link projection. CAL-2 deserves the
   same treatment.
5. **The framework's anti-fitting discipline conflates "categorical
   structure" with "external calibration."** Three cohomological
   degrees of freedom is a structural statement; *how* those
   degrees are pinned (cohomologically vs by CODATA) is a separate
   question that the paper does not analyse.

This audit DOES NOT propose a 4th calibration input or a fit. It
proposes that **all three current calibrations are placeholders for
cohomological derivations** that the framework can in principle
deliver, and that the paper's "3-CAL discipline" language
**obscures** that fact.

## §1. What the paper currently says (verbatim, with file:line)

### §1.1 The headline 3-CAL claim

[`content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md:1-6`](../../content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md):

> *"The QOU framework admits exactly three external calibration
> inputs. Beyond these three, no further empirical, fitting, or
> numerological input is permitted — every other mass, Q-value,
> binding energy, coupling constant, mixing angle, and dimensionless
> ratio in the paper is a prediction."*

The same block §1.5 ("Forbidden") states: *"a second pinning of q_0…
is forbidden"* and *"a fourth calibration anywhere in the paper is
a hard audit failure."*

### §1.2 The cohomological alignment

[`content/quantum-observable-universe/observations/three-calibration-discipline.md:6-10`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md):

| (Co)homology degree | Calibration | Role | Source |
|---|---|---|---|
| **H⁰** — mass scale | m_e | dimensional unit | CODATA |
| **H¹** — substrate ratio | m_μ/m_e | fixes q_0 | CODATA |
| **H²** — weak/decay scale | Q_β | β-decay normalisation | PDG |

### §1.3 The Wedderburn-channel alignment

[`three-parameters-wedderburn.md:64-68`](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md):

| α | Irrep λ ⊢ 3 | Observable | What it fixes |
|---|---|---|---|
| α_1 | (3) symmetric | m_μ/m_e | substrate q_0 (all crossings +q) |
| α_2 | (2,1) standard | m_e | mass scale (mixed eigenvalues) |
| α_3 | (1,1,1) alternating | Q_β(n) | interaction scale (all -q⁻¹) |

### §1.4 The "first prediction by construction" pattern

[`calibration-inputs.md:152-154`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md):

> *"Muon mass: m_μ = m_e × Vol(4_1)/ℏ_q² (**first prediction, by
> construction matches calibration input**)"*

And in `content/quantum-observable-universe/braids-and-knots/figure-8-muon-mass-cross-check.lean:36-42`
(per Explore agent):

> *"The CAL-2 calibration defines q₀ as the unique real solution of
> m_μ/m_e = Vol(4_1)/ℏ_q². Evaluating both sides at q₀ therefore
> gives equality **by construction**."*

## §2. Critical findings

### F1. CAL-2 is self-referential (the "first prediction by construction" pattern)

Define:
- **Input axiom (CAL-2):** `q_0 := unique real solution of
  m_μ/m_e = Vol(4_1)/ℏ_q²`, pulling `m_μ/m_e` from CODATA.
- **First prediction:** `m_μ = m_e × Vol(4_1)/ℏ_q²` at `q = q_0`.

The first prediction holds because q_0 was DEFINED to make it hold.
This is an unavoidable structural feature, not a bug — but it does
mean that the language *"first prediction"* is misleading. The
framework predicts m_μ in MeV (modulo CAL-1) iff it predicts m_μ/m_e
(modulo nothing else). And m_μ/m_e is precisely the input.

A clearer accounting:

| Statement | Status |
|---|---|
| `m_μ/m_e = Vol(4_1)/ℏ_q²` at the substrate | **Cohomological identity** (proved structurally; numerical at q_0 by construction). |
| `m_μ ≈ 105.66 MeV` (= m_e · 206.768) | **Calibration** (uses CAL-1 + CAL-2 both). |
| `q_0 ≈ 1.10998` | **Calibration** (CAL-2 pin). |
| `Vol(4_1) ≈ 2.0299` | **Pure cohomology** (Lobachevsky function value; no calibration). |

The paper's narrative collapses rows 1 and 2 into "the first
prediction." Row 1 is a cohomological identity. Row 2 is a
calibration restatement.

### F2. Vol(4_1) and Li_2 are both cohomology, but q_0 is the gap

The framework already contains cohomological derivations on BOTH
sides of CAL-2:

- **Vol(4_1) ≈ 2.0299** = hyperbolic volume of S³ \ 4_1 =
  `2 · Λ(π/3)` where `Λ` is the Lobachevsky function. This is a
  motivic period (Bloch-Wigner dilogarithm at a primitive 6th root
  of unity). Pure topology + pure cohomology. No physics input.
- **m_e(natural) = Li_2(q^{-2})/ℏ_q²** = dilogarithm period. Pure
  cohomology *parametrized by q*. No physics input.

What **is** pinned to physics: the value of q_0 itself, and the
MeV-conversion factor for m_e. The cohomology produces the
RATIOS and FUNCTIONS; the physics produces the SPECIFIC POINT q_0
and the UNIT CONVERSION.

So the owner's instinct that *"m_μ/m_e should be over ℝ from
cohomology"* aligns with what the framework already does *modulo*
the q_0 pin. The cohomological content (Vol(4_1), Li_2, dim H_n(q))
is real; the substrate q_0 itself is the un-derived constant.

### F3. m_e cohomologically reframed

`m_e` plays **two** roles in the paper:

| Role | Type | Status |
|---|---|---|
| **Unit of mass** (MeV ↔ natural units) | dimensional choice | CAL-1 (choice, not derivation) |
| **Numerical value in natural units** `Li_2(q^{-2})/ℏ_q² ≈ 112` | dimensionless | cohomologically derived from q_0 |

The owner's *"is m_e the first-generation lepton scalar?"* question
maps to row 1 — **no, it's a unit choice**. The cohomological
"first scalar" is the dimensionless `Li_2(q^{-2})/ℏ_q²`, which is a
motivic period parametrized by q.

In a fully cohomological framing, CAL-1 would not exist as a
"calibration." It would be a unit-conversion convention: "we report
masses in MeV; the conversion is 4.57 × 10⁻³ MeV per natural unit."
That conversion factor is the only dimensional input the framework
genuinely needs.

### F4. β cohomologically — Khovanov-Rozansky strata (sibling work)

Two parallel efforts already recast β cohomologically:

- **PR #1127** ([`audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md`](2026-05-24-q-beta-net-ansatz-fitting-finding.md))
  found that `Q_β = |Δ(net)| · E_0` is **postulated**, not derived
  from the canonical per-braid mass formula. The +0.17% match
  could be (a) genuine N=0 truncation residual or (b) numerical
  coincidence — framework has no discriminator. CAL-3 remains an
  input.
- **Audit [`2026-05-18-qbeta-n5-cohomological-breakdown.md`](2026-05-18-qbeta-n5-cohomological-breakdown.md)**
  proposes Q_β rungs as traces over **Khovanov-Rozansky cohomology
  strata** of the link projection in the 3-fold Markov closure:
  `c_k = Σ_{p+q=k} Tr(E^{p,q}_∞)`, with N=3 rung = J_Hopf(q=1) = −2
  (Jones invariant of the Hopf link). This pattern continues
  through N=4, N=5 with multi-stratum sums.

So **β = beta, cohomologically, = trace over Khovanov-Rozansky
homology of the link projection**. The paper's `Q_β` as a
"calibration input" is a placeholder for this open derivation.
PR #1127 has begun the relabeling work.

### F5. The "first lepton generation" framing

The owner asks: is m_e the first lepton generation scalar
(cohomologically)? Is m_μ a derivative of that scale, or a distinct
scale?

The framework's structure:

- **Leptonic sector** lives at H_2(R, q) (2 strands, 2 partitions
  (2) and (1,1), `dim = 1² + 1² = 2`). Per
  [`three-parameters-wedderburn.md:103-115`](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md):
  *"Two irreps → two parameters (q and m_e). No standard
  representation → no interaction scale needed. Leptonic physics
  (electron, muon, tau) requires only two inputs."*
- **Muon ↔ 4_1 figure-eight knot.** The figure-eight needs 3
  strands (lives at H_3, not H_2). So the muon-as-knot is encoded
  ABOVE the leptonic sector's natural algebra. The ratio
  `Vol(4_1)/ℏ_q²` lifts the leptonic mass quantum to the figure-
  eight's hyperbolic volume normalisation.
- **No corresponding "electron-as-knot"** is in the framework. The
  electron is the *unit* — the trivial trace, the unknot in H_2,
  the Markov-trace baseline.

In a cohomological reading:
- **"First generation" cohomologically = the trivial trace at H_2**
  (electron as unknot / vacuum-like reference scale)
- **"Second generation" cohomologically = the smallest hyperbolic
  knot at H_3** (muon ↔ 4_1, Vol(4_1) ≈ 2.0299)
- **"Third generation"** would be the next-volume hyperbolic knot
  encoded at minimal H_n — candidates include 5_2 (Vol ≈ 2.828),
  6_3 (Vol ≈ 5.694), or a derivative encoding the next generation
  level

This re-framing is consistent with the framework's own
[`hoefsmit-scattering-pipeline.md:138`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-scattering-pipeline.md)
statement: *"the figure-eight knot defines q_0."* The figure-eight
is the muon-defining knot; q_0 itself is the substrate value at
which the muon-electron mass ratio matches CODATA.

The owner's instinct that m_μ should be cohomologically derivative
is **correct** — it IS, via `Vol(4_1)/ℏ_q²`. The piece that's NOT
derived is q_0. The "second generation is a derivative of the
first scale" framing maps onto `m_μ = (cohomological function of
q_0) · m_e`.

For the tau (third gen): per
[`calibration-inputs.md:144`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md),
the framework already claims `m_τ/m_e` is predicted from q_0 alone
("from q_0 alone (dimensionless): Lepton mass ratios m_τ/m_e,
m_τ/m_μ"). But the explicit formula isn't surfaced in
calibration-inputs.md. If the pattern holds, m_τ should be
`m_e · (some-knot-volume) / ℏ_q^k` for an integer k, where the knot
is the next hyperbolic generator in the H_n tower.

## §3. Where the paper is wrong (or at least weak)

I do not claim the paper is mathematically wrong about the
3-parameter count — that is correct (3 Wedderburn channels of
H_3, 3 surviving real scalars after on-shell + gauge + observability
quotient). I claim the paper is **rhetorically wrong** about the
status of those 3 scalars:

| Claim in paper | Status |
|---|---|
| "3 calibration inputs map to 3 cohomological degrees" | TRUE for the count; misleading for the status |
| "Three irreps, three surviving parameters, three calibration inputs" | The middle term is structural; the OUTER terms are independent choices |
| "m_μ is the first prediction (by construction)" | Tautological — m_μ/m_e fixed q_0 fixed m_μ |
| "A fourth calibration is a hard audit failure" | True, BUT does not address: could the 3 existing ones be cohomologically derived? |
| "The framework is rigid in this sense: increasing or decreasing the number of calibrations would require deforming the categorical substrate" | Conflates "number of cohomological degrees" with "number of external calibrations" |

The structural-vs-empirical distinction is critical:

- **3 cohomological degrees** is a categorical fact about H_3(R, q).
- **3 calibration inputs** is a CHOICE about which 3 numbers to
  borrow from CODATA — currently `{m_e, m_μ/m_e, Q_β}`.
- These are not the same statement.

The paper could in principle have:
- **3 cohomological derivations + 0 calibrations** (subgoal-2,
  declined 2026-05-08 — substrate q_0 + dimensionful scale from
  fundamental constants)
- **2 cohomological derivations + 1 unit choice** (the "honest
  minimum" — pick MeV vs natural units; everything else derived)
- **0 cohomological derivations + 3 calibrations** (current state)

The paper presents only the third option as legitimate. The owner
is asking for movement toward the first or second.

## §4. Where the framework ALREADY does what the owner is asking

Per F2-F5 above, the cohomological derivations are largely present
or in flight:

| Quantity | Cohomological derivation status |
|---|---|
| Vol(4_1) ≈ 2.0299 | **Closed-form** (Lobachevsky Λ(π/3); pure topology) |
| m_e(natural) ≈ 112 | **Closed-form** (Li_2(q^{-2})/ℏ_q²; pure motivic period in q) |
| h = q − q⁻¹ ≈ 0.188 | **Closed-form** in q |
| m_τ/m_μ | "Predicted from q_0 alone" (per [calibration-inputs.md:144](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md)); explicit formula not surfaced |
| Q_β-rungs (Khovanov-Rozansky strata) | **In flight** ([2026-05-18-n5 audit](2026-05-18-qbeta-n5-cohomological-breakdown.md); PR #1127) |
| **q_0 itself** | **Open R&D** (declined 2026-05-08; subgoal-2 out of scope) |
| Δ_λ (per-partition binding components) | **Open R&D** (6 closure ansätze failed; "Track A blocker"; PR #1224 + #1229 in flight) |

The **single load-bearing gap** is q_0. If q_0 were cohomologically
derived, CAL-2 would collapse from "input" to "verification." The
m_μ = m_e · Vol(4_1)/ℏ_q² identity would become a **genuine
prediction** (cohomological RHS predicting CODATA LHS), not a
tautology.

## §5. Suggested next steps (owner decision)

This audit is research-grade analysis only. No content blocks are
modified, no calibration changes are proposed. The actionable
follow-ups are:

1. **Add author-notes to `calibration-inputs.md` and
   `three-calibration-inputs.md`** flagging the self-referential
   pattern (per F1) and the F4-F5 in-flight cohomological work.
   Cite PR #1127 + audit [2026-05-18-n5](2026-05-18-qbeta-n5-cohomological-breakdown.md).
   Small, mechanical, doesn't change mathematical content.
2. **Re-open the substrate-q_0 derivation discussion.** The
   2026-05-08 declination ("subgoal-2 out of scope") predates
   PR #1127's CAL-3 droppability finding and this CAL-2 critique.
   The owner may want to revisit. Candidate paths:
   - q_0 as the unique fixed point of some categorical
     endomorphism on H_n(R, q)-irreps
   - q_0 from spectral collapse condition of the Wenzl/Hecke
     spectral sequence at a unique value
   - q_0 from K-theoretic / motivic period identity (the
     `Vol(4_1) = 2 Λ(π/3)` side already lives in this world)
   - q_0 as the algebraic-K-theory class fixed by the Bring
     surface χ = −6 condition
3. **Extend PR #1127's "Q_β droppability" workplan to all 3 CALs.**
   That PR labels Q_β as ansatz-conditional. The same labeling can
   apply to m_μ/m_e (CAL-2 is "q_0 fixed by ansatz: ratio matches
   CODATA") and m_e (CAL-1 is "MeV unit choice"). The result is a
   coherent epistemic accounting that does NOT introduce new
   fitting and does NOT loosen the no-fourth-CAL discipline.
4. **Predict m_τ from q_0 explicitly.** The paper claims this is
   possible from q_0 alone (cite above). Surfacing the formula
   (e.g., `m_τ/m_e = Vol(K_τ)/ℏ_q^k` for an explicit knot K_τ and
   integer k, then comparing to CODATA m_τ/m_e = 3477.23...) would
   be a concrete cohomological prediction. Currently this isn't
   surfaced.
5. **Combine with PR #1228 (vol-density-derivation full KLR path).** That
   PR is doing the bug-isolation for the cohomological /
   KLR-multiplicity side. The CAL-2 critique here and the F2-F5
   findings could feed into PR #1228's §10 "concrete next actions"
   list as additional context.

## §6. Coordination posts

Per CLAUDE.md "Coordinate intent with sibling branches on every
new workplan," posting brief intent comments to:

- **PR #1127** (Q_β fitting finding) — parallel critique for
  CAL-2; do not duplicate their Q_β work.
- **PR #1228** (vol-density-derivation bug squash) — F2-F5 findings
  potentially feed §10 action list.
- **PR #1224** (delta-lambda closure synthesis) — Δ_λ is the
  partition-level analog of the q_0-level question raised here.

## §7. What this audit does NOT do

- Does **not** propose a 4th calibration input.
- Does **not** propose to replace CAL-1/2/3 with empirical fits.
- Does **not** modify `calibration-inputs.md`,
  `three-calibration-inputs.md`, or any other content block.
- Does **not** claim q_0 has been cohomologically derived.
- Does **not** introduce new fitting, ansätze, or numerological
  inputs (per the CLAUDE.md anti-pattern guard).
- Does **not** override the framework's no-fourth-CAL discipline.

It is a critical-analysis document only, surfacing structural
tensions that the owner's question identified and that the
framework's own sibling work (PR #1127 et al.) is independently
moving toward.

## §8. References

### Paper-side
- [`calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/calibration-inputs.md) — canonical 3-CAL remark with formulas
- [`three-calibration-inputs.md`](../../content/quantum-observable-universe/braids-and-knots/three-calibration-inputs.md) — proposition form
- [`three-calibration-discipline.md`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md) — H⁰/H¹/H² mapping
- [`three-parameters-wedderburn.md`](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md) — Wedderburn → 3-channel
- [`hoefsmit-scattering-pipeline.md:138`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-scattering-pipeline.md) — "figure-eight defines q_0"

### Audit-side
- [`2026-05-01-calibration-inputs-addendum.md`](2026-05-01-calibration-inputs-addendum.md) — historical taxonomy fix (1 → 3 CAL)
- [`2026-05-11-three-calibration-discipline-violations.md`](2026-05-11-three-calibration-discipline-violations.md) — enforcement of 3-CAL discipline
- [`2026-05-17-m-n-substrate-investigation-and-lit-search.md`](2026-05-17-m-n-substrate-investigation-and-lit-search.md) — m_n NOT substrate-derived (1-param fit)
- [`2026-05-18-qbeta-n5-cohomological-breakdown.md`](2026-05-18-qbeta-n5-cohomological-breakdown.md) — Khovanov-Rozansky strata for Q_β
- [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — 6 closure ansätze failed; Track A blocker

### Sibling PRs (open)
- **#1127** — Q_β net-ansatz fitting finding + complex-q substrate lift
- **#1228** — vol-density-derivation: error localization + full KLR path
- **#1224 / #1229** — Δ_λ closure synthesis + bar-invariance probe

### Compute / Lean
- `computations/substrate/q_parameter.py` — q_0 numerical pin
- `computations/y_lambda_wenzl_bridge.py` — Wenzl weights
- `content/quantum-observable-universe/braids-and-knots/figure-8-muon-mass-cross-check.lean` — Lean cross-check ("by construction")
