# Δ_λ `10A−5` exponent — formalize-first keystone audit (2026-06-19)

**Branch:** `claude/friendly-einstein-oe3wlr` (PR #2485). Owner-directed
research item 1 + queued item B. Discipline: formalize-first, tiered status,
**no fit** (Δ_λ gate). This audit records what is *derived*, what is *open*,
and — newly surfaced — what is in *empirical tension*, so the next pass starts
from the right statement.

## Item 1 question (owner)

> Is the `10A−5` Δ_λ binding exponent derived using **confinement** (Step 10),
> the **Gröbner–Shirshov filtration** (Step 7), or the **jet order** (Step 8)?

**Answer: no.** The exponent is a raw combinatorial crossing count.
`computations/delta_lambda_exponent_from_crossings.py` reads the atom braid
word `atom_braid_word_3A(Z, N)` (`computations/mass_at_3A_proper.py`) and counts:

| quantity | closed form |
|---|---|
| positive crossings `σ` | `7Z + 5N − 1` |
| negative crossings `σ⁻¹` | `3Z + 5N − 1` |
| sum `σ + σ⁻¹` | `10Z + 10N − 2 = 10A − 2` (Z, N cancel) |

So the **slope of 10 per nucleon is genuinely derived** (the `Z`/`N`
coefficients cancel in the sum, verified for D, T, ³He, ⁴He). Confinement,
the GS normal form, and the jet order are **never invoked** in this path —
confinement enters only the binding *magnitude* / operator selection
(Step 10), not the exponent.

## The two asserted sub-quantities (open)

The crossing count asserts, without deriving:

1. **per-site `5`** — the exponent is read as `5·(2A−1) = 5 × (A nucleons +
   A−1 bonds)`, with `5 =` the Bring-quintic degree (`𝒳₅`). Why each
   chain-site contributes exactly `5` is open
   (`docs/audits/2026-06-15-delta-lambda-q5-per-site-mechanism-start.md §quintic`).
2. **per-nucleon `9`** — the intra-𝓑₃ crossing count is `9` (+ 1 interface
   = 10 per nucleon). Why `9` is not derived from the GS normal form.

The owner's reframing is the productive one: **the missing derivation is
plausibly a jet-grade / GS-normal-form statement, not a crossing count.**
- "per-site 5" → a jet-grade-per-chain-site claim (Step 8, jet order). The
  jet order grades the Markov-trace Laurent polynomial by `h`-power; "5 per
  site" would be the per-site jet grade.
- "per-nucleon 9" → a GS-normal-form crossing count (Step 7), i.e. the number
  of irreducible crossings in the reduced word for the intra-𝓑₃ braid.

## ⚠ Newly surfaced: the per-site-5 magnitude is in EMPIRICAL TENSION

Going to *formalize* "exponent = `5·(2A−1)`" surfaced (per
`docs/audits/2026-06-15-delta-lambda-q5-per-site-mechanism-start.md` §magnitude
caveat, and `2026-06-15-binding-qa-followups-investigation.md §5`) that the
literal `q₀^{5(2A−1)}` exponent **overpredicts the measured `B_sym/B_lin`
ratio by 3×→145×** and runs away exponentially in `A` where the data grows
~linearly. The exponent that actually fits is **≈ 1.4 per site, not 5**, and
is consistent with the `−ln(1−s)/s` exp-vs-linear (Kashaev `exp(Vol)` vs
linear `Δtr`) correction — **not** a `q₀`-power.

**Consequence for formalization (formalize-first verdict):** do **not** state
"per-site exponent = 5" as a Lean *theorem*. It is (a) underived and (b)
contradicted at face value by the binding data. Enshrining it would violate
the Δ_λ-gate "no fit" discipline in reverse — encoding a refuted near-match as
structure. The honest formalization is:

- **Provable (arithmetic, true for all Z, N):** the crossing-sum cancellation
  `σ + σ⁻¹ = 10A − 2` and the factorization `5·(2A−1) = 10A − 5`. These are
  pure `omega`/`ring` facts about the *crossing bookkeeping*; they say nothing
  about whether the binding exponent equals them.
- **Conjectural (open + magnitude-contested):** the bridge from the crossing
  count to the binding exponent, and the per-site-5 / per-nucleon-9 reading.
  Stated as a `conjecture`-kind claim carrying the magnitude caveat, never a
  theorem.

## Lean target (item B)

A self-contained file `QOU/BraidKnot/DeltaLambdaExponentKeystone.lean`
(namespace `QOU.BraidKnot`) holding:

1. `crossing_sum_cancels : protonCrossings Z N + neutronCrossings Z N = 10*(Z+N) − 2` — **proved** (`omega`, with `1 ≤ Z+N`).
2. `exponent_factorization : 5*(2*A − 1) = 10*A − 5` — **proved** (`omega`).
3. `BindingExponentBridge` — a `conjecture`-flavored statement (the per-site
   jet-grade = 5 and per-nucleon GS count = 9 hypotheses, with a docstring
   recording the ≈1.4/site empirical tension). Marked `sorry` + `-- Ref:` to
   this audit and `2026-06-15-...-q5-per-site-mechanism-start.md`.

Existing decls the bridge *documents* (not term-level dependencies, to keep
the compile surface minimal): `QOU.BraidKnot.deltaLambda`
(`DeltaLambdaSignRule.lean`), `UGB.GrobnerShirshov.JetConfig` /
`degLexNat` (`JetOrder.lean`, Step 8), `UGB.GrobnerShirshov.SU2Gen` /
`degLexLt` (`NormalForms.lean`, Step 7), `QOU.BraidsAndKnots.A5Irrep`
(`S5SO3FiberAction.lean`, Bring `dim H = 5`).

## Next real step (not session-sized)

Per the 2026-06-15 caveat: **measure the per-site binding exponent from real
compute** (fit `B_sym` vs `B_lin` per chain-site) and confirm whether it is
`5`, `1.4`, or `A`-dependent, *before* chasing the complex-q / Kashaev
`exp(Vol)` mechanism for "why 5". Until that lands, the keystone stays a
conjecture; the arithmetic core is the only part that formalizes.

## Connection to the canonical order recurrence (separation verdict, 142deb16)

The binding Δ_λ ladder is the **order** recurrence (C-finite, constant-`b`),
proved and Lean-distinguished from the Q_β `c_k` **argument** recurrence in
`docs/audits/2026-06-18-qbeta-qbessel-vs-zhabiro-binding-tower-separation.md`
(Lean: `QOU/QBeta/QLommelOrderRecurrence.lean` vs
`QBesselContiguityRecurrence.lean`). Its three-term form is

    a(n+2) = b · a(n+1) − a(n),   b = q₀¹⁰ + q₀⁻¹⁰.

**The exponent `10` in `b` is exactly item B's slope-10-per-nucleon**
(`σ + σ⁻¹ = 10A − 2`): the crossing-count bookkeeping formalized here is the
generator of the *same* `q₀¹⁰` that drives the canonical C-finite order
recurrence. This is a consistency check, not a new claim — the per-*nucleon*
10 is on firm ground (crossing count ⇒ recurrence constant), and it is the
per-*site* split into `5 + 5` (and the magnitude) that remains open/contested.

**Scope caution (from the separation verdict).** Do **not** reach for the Q_β
`c_k` argument recurrence to close the binding exponent: the joint J+I lever
was tested and **refuted** (2026-06-14 NO-GO; ³He +17.4% → +117.9%). Q_β and
binding share an analytic home (Hahn–Exton q-Bessel, `E_q(2)` contraction
limit) but are **separate recurrences**; the binding keystone is the Option-E
route, not a Q_β cross-constraint.

## Items A and C — corpus-frontier status (corpus-grep checked)

The two distinct open keystones (per the separation verdict) were checked
against the corpus before claiming any new chip. **At the formalize-first
level both are already at the frontier**; the remainder is research-grade /
multi-session compute that the corpus explicitly gates — not a session-sized
Lean chip, and *not* an opening for a fit (Δ_λ gate).

- **C — Q_β kernel `R(q,ξ)`.** The formalizable layer is **already complete on
  main**: `QOU/QBeta/QBesselContiguityRecurrence.lean` proves the contiguity ⟹
  closed-form coefficients (`qbessel_coeff_closed_form`), names the ratio
  (`qbesselRatio`), distinguishes q-holonomic from the C-finite degeneration,
  gives the second-order recurrence, and characterizes the kernel `R` of
  `F(qξ)=R·F(ξ)` as *an operator, not a rational degeneration*. The genuinely
  open part is the **categorical derivation** of `R` from the substrate
  (Hecke → `E_q(2)` contraction) — research-grade; no Lean chip remains.
- **A — H₆/H₉ typed braid construction.** Scoped upstream in
  `2026-06-17-jacobi-anger-physical-weight-n3.md` (T_beta selector +
  tower-convergence test spec + H≥6 hand-off). **Corpus-grep (2026-06-19)
  corrects an earlier draft of this paragraph that claimed "n=6 lives only in
  deprecated probes":** the H₆ deuteron compute is already on `main` at
  production precision — free-word χ_λ at q₀ *and* q⁻¹ and bound χ_λ at 50 dps
  (`chi-deuteron-free-h6-at-q0-50dps`, `chi-deuteron-h6-at-q0-50dps`; landed
  PR #1742/#1748), the symbolic bound characters (`chi-deuteron-h6`), the full
  Littlewood–Richardson bound↔free bridge factor ω
  (`derived_chi_catalogue_bridge_factor_deuteron.py`), and the H6→H9
  joint-tower SDP (`joint-tower-sdp-h6-h9`). The `atom_braid_word_3A(1,1)`
  word *is* the 6-strand deuteron (3 strands × A=2), so no `_nA` generalization
  is needed for A=2. A float64 re-probe added earlier this session
  (`h6-deuteron-chi-lambda`) duplicated the 50-dps bound witness at inferior
  precision (≈1e-4 disagreement over the 23-crossing word, float64 being
  inadequate there) and is **removed** — its "first live" claim was a
  corpus-grep miss. The genuine open item is **not the H₆ characters but the
  Δ_λ closure itself** (the per-partition binding weights), which STATUS.md
  records as research-gated (deuteron "closure" overclaim corrected c27667d4;
  no light nucleus honestly closed) and which CLAUDE.md explicitly fences
  against a seventh fit-based ansatz.

**Conclusion.** The session-sized formalize-first work on this axis is done
(items 4, B, and this reconciliation). C requires a research derivation
(categorical `R` from the Hecke → `E_q(2)` contraction); A's H₆ compute
already exists on `main` at production precision, so A's only remaining work
is the research-gated Δ_λ closure. Neither admits a one-session Lean/compute
addition without either duplicating main or fitting.
