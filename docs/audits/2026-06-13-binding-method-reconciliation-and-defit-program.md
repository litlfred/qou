# Binding-method reconciliation + de-fit program (heat-kernel weight)

**Date:** 2026-06-13. **Owner ask:** "we need to resolve binding
methods" → "use heat kernel, active-set partitions to figure out the
weight" → "get rid of fitting."

This is the **single authoritative map** of every binding-energy method
in the corpus, what is canonical vs fitted, and the disciplined program
to replace the one remaining fit (the per-depth weight) with a
**derived** q-heat-kernel weight. It indexes — and is meant to be read
in place of re-deriving — the ~12 scattered binding audits/ledgers
listed in §6.

## 0. TL;DR

- There is **one canonical production method**:
  [`binding_canonical.py`](../../computations/binding_canonical.py)
  (Jones–Markov trace difference `B = E·(tr_M(W_free) − tr_M(W_atom))`,
  signed, zero-fit). ⁴He is closed separately by the **magic-A** formula
  `2·m_e·A·Vol(L6a4)` (+5.87%, zero-fit,
  [`prop:magic-A-binding-formula`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula.md)).
- **The deuteron closes (+0.2–1%); A ≥ 3 undershoots 50–95%.** This is
  the documented **many-body ceiling**
  ([`2026-06-02-binding-many-body-ceiling.md`](2026-06-02-binding-many-body-ceiling.md)):
  pairwise/per-block/trace methods capture ~26% of ⁴He; the rest is
  irreducible 3-/4-body cooperativity. No pairwise method can reach it.
- **The one genuinely open math item is the WEIGHT** — the per-depth
  `α_k` *assignment rule* in the depth-stratified default
  ([`2026-06-09-binding-canonical-default-depth-stratified.md`](2026-06-09-binding-canonical-default-depth-stratified.md),
  `canonical_status = canonical-with-empirical-assignment`). The α_k
  *constants* are structural; which constant sits at which depth is
  **empirical**. That is the fit "get rid of fitting" targets.
- **The replacement is already-derived**: the q-heat-kernel eigenvalue
  `μ_λ(q) = ℏ_q² Σ_□ [c(□)]_q [c(□)+1]_q`
  ([`prop:q-heat-kernel-peter-weyl`](../../content/quantum-observable-universe/information-theory/q-heat-kernel-peter-weyl.md)),
  a per-partition weight that grades by depth structurally. It is the
  one candidate weight the existing measure-search never tested (§4).

## 1. Method census (14 methods → 4 classes)

Full file/line inventory: see the consolidated table in the companion
compute sweep. Condensed by class:

| Class | Methods | Formula spine | Fit? |
|---|---|---|---|
| **CANONICAL** | `binding_canonical` (Jones–Markov trace); `magic_A_formula` (⁴He) | `E·(tr_M^free − tr_M^atom)`; `2·m_e·A·8G` | **none** |
| **PRODUCTION (gated)** | `binding_K_direct` (`m_e·Σ y_λ χ^λ Δ_λ`) | blocked on Δ_λ derivation; status-reporter only | none (gated) |
| **EXPLORATORY (fitted)** | `binding_depth_stratified` (α_k); `binding_block_multiplicative` (v_p,v_n,V_inter); `binding_factor_f_decomposition` (f(Z,N)); `binding_alpha_shift` (ρ₀) | various per-block weights | **yes** — see §2 |
| **EXPLORATORY (zero-fit probes)** | `binding_endomorphism_deuteron` (+0.19% D); `binding_via_interface_knot`; per-bond graph (`f_bond=c·z+d`, fibre-derived); `binding_k_solver`; `delta_lambda_canonical_residual` | structure-seeking | none |
| **DEPRECATED** | `hecke_core.atom_markov_trace` / `binding_from_frobenius_pairing` (double-modulus, non-archimedean) | redirects to `binding_canonical` | — |

The signed-trace convention (`tr_free − tr_atom`, NOT `|tr_free| −
|tr_atom|`) is canonical
([`2026-06-09-binding-trace-convention-split.md`](2026-06-09-binding-trace-convention-split.md));
the double-modulus form was a non-archimedean misuse.

## 2. The fitted inventory + disposition (the "get rid of fitting" list)

| Fit | Method | Value(s) | Disposition |
|---|---|---|---|
| per-depth α_k **assignment** | `binding_depth_stratified` | α₂=z², α₃=1, α_{k≥4}=m_e·8G | **replace** with derived μ_λ (§4) |
| block factors | `binding_block_multiplicative` | v_p=0.7084, v_n=0.6005, V_inter=0.1045 | quarantine; A-independence unproven |
| per-(Z,N) factor | `binding_factor_f_decomposition` | f extracted from AME | **demote** — pairwise hypothesis falsified at ⁴He |
| atom→knot census | `low-isotope-mass-table` | 6₂/8₁₁/L6a4 chosen to fit AME | **tag non-canonical** (no derived selection rule, PR #1421) |
| C_knot | a3-honesty ledger | 5.852 = B_AME/(m_e·\|sum\|) | already **retracted** |
| ρ₀ | `binding_alpha_shift` | deuteron-pinned | flagged exploratory |
| ρ_F=2 | `magic_A_formula` | claimed structural | confirm not-a-fit (PR #1507 fit-pattern audit) |

**Disposition rule:** do **not** delete production-wired fitted methods
before the derived replacement is validated — binding would be left
with no method. Quarantine + label now; demote after §4 lands.

## 3. Why A ≥ 3 is open (so the weight is the right lever, not a new ansatz)

The many-body ceiling is proved zero-fit: ⁴He is 74% irreducible
4-body. **A 7th multiplicative Δ_λ ansatz is forbidden** (CLAUDE.md
§Precision-goals Δ_λ gate; six ansätze already failed on the deuteron).
The productive lever is therefore **not** a new closed form but the
**weight on the existing decomposition** — and it must be *derived*,
which is exactly what the heat-kernel program supplies.

## 4. The derived-weight program (heat kernel + active set)

Three λ-indexed weight families exist, **all derived** (do not conflate
— CLAUDE.md notation register):

| weight | formula | role |
|---|---|---|
| **q-heat-kernel** μ_λ(q) | `ℏ_q² Σ_□ [c]_q[c+1]_q` | q-Laplacian eigenvalue / heat-flow decay rate |
| Plancherel w_λ(q) | `[n]_q!/H_q(λ)²` → d_λ²/n! | spectral measure ([`prop:plancherel-weight-boundedness`](../../computations/probes/plancherel_weight_boundedness_probe.py)) |
| Wenzl/Markov y_λ(q) | H_3: `[4]_q/[2]_q³, 1/[2]_q², 0` | Markov-trace weighting (now exact closed-form, `prop:h3-markov-wenzl-weights`) |

**Hypothesis (derived, testable, zero-fit):** the per-depth α_k
assignment is reproduced by the q-heat-kernel weight `e^{−μ_λ(q₀)t}`
(or μ_λ-graded), with the heat-time `t` substrate-fixed (NOT tuned to
AME). The GB-filtration depth k correlates with the content-sum, so
μ_λ grades by depth structurally — supplying the assignment the fitted
α_k currently hard-codes.

**Known headwind:** `probe_binding_measure_search.py` established that
y_λ *anti*-correlates with A — it suppresses the growth channels
(|χ/d| > 1) where extensive binding lives. μ_λ is the untested derived
candidate; whether the heat-kernel weighting emphasises or further
suppresses those channels is the empirical question the probe settles.

**⚠ Active-set guardrail.** The active set (3–4 few-row λ carrying ~90%
of tr_M) is a **search-narrowing device only** — use it to identify the
*form* of the weight-law (which dominant λ the weight must get right).
**Do not truncate the production binding sum to it**: that drops ~10%
of tr_M and breaks the L1 1-ppQ goal
([`2026-06-10-binding-active-set-compute-optimization.md`](2026-06-10-binding-active-set-compute-optimization.md);
the only lossless optimization is per-nucleon block caching).

**Probe plan** (`binding_heat_kernel_weight_probe.py`, formalize-first):
extend the measure-search harness with the μ_λ heat-kernel weight;
test on D/T/³He/⁴He at full p(3A) (no truncation); t substrate-fixed
(zero-fit) with a 1-param-t variant reported separately and tiered;
assert the refutation if it does not close (a zero-fit refutation is
still a result and prunes the class).

## 4a. Probe result (this PR) — derived heat-kernel weight REFUTED (zero-fit)

[`binding_heat_kernel_weight_probe.py`](../../computations/binding_heat_kernel_weight_probe.py)
→ `binding-heat-kernel-weight-probe.witness.json`. Tests the derived
μ_λ eigenvalue weight `C_λ(q)=Σ_□[c]_q[c+1]_q` in `B=E·Σ_λ w_λ|Δθ_λ|`
at one global scale over D/T/³He/⁴He (full p(3A) sum, no truncation):

| weight | worst \|err\| | S(⁴He)/S(D) vs 12.72 | verdict |
|---|---|---|---|
| **heat μ_λ eigenvalue** (derived, zero-fit) | 61.3% | **34.15** (over) | **refuted** — over-weights growth channels |
| heat kernel e^{−μ_λτ} (1-param τ) | 100–381% | ~0 (suppresses) | refuted — same failure mode as y_λ |
| abs_content Σ\|c\| (classical baseline) | 19.9% | 13.40 ≈ target | closest A-growth, still no closure |
| y_λ (baseline) | 198.8% | 0.04 | anti-correlates (known) |

**Reading:** the derived weight *brackets* the right A-growth — the
μ_λ eigenvalue overshoots (Σ[c]_q[c+1]_q ~ q-quadratic in content),
the heat kernel e^{−μτ} suppresses (like y_λ). The classical Σ\|c\|
(≈ linear in content) lands closest on A-growth but still misses at
19.9%. **No per-block weight on |Δθ_λ| closes A≥3 to 5%** — direct
corroboration of the many-body ceiling (§3): a per-block measure
cannot carry 4-body cooperativity. The heat-kernel de-fit lever is
**closed as a closure mechanism** (zero-fit refutation); the open
lever stays the substrate-derivation of the per-depth assignment
rule (or the operator-valued combiner, §7).

## 5. Discipline guardrails (STRICT)

1. **No 7th fit** (Δ_λ gate). The weight must be derived (μ_λ, w_λ, y_λ
   are; α_k assignment is not).
2. **No fishing** — no enumerating weight/coupling variants against AME
   and keeping the best
   (`local/production-vs-exploratory-discipline`; α_k audit §4).
3. **No active-set truncation** of the production sum (§4 guardrail).
4. **Tiered reporting** — `derived` (t substrate-fixed) /
   `1-param near-match` (t tuned) / `fitted`. Never binary.
5. **Signed trace** convention only.

## 6. Superseded / indexed docs

This map indexes (read here first, then drill):

- [`2026-06-09-binding-canonical-default-depth-stratified.md`](2026-06-09-binding-canonical-default-depth-stratified.md) — the canonical default + the α_k assignment gap
- [`2026-06-02-binding-many-body-ceiling.md`](2026-06-02-binding-many-body-ceiling.md) — 74% of ⁴He is 4-body (zero-fit)
- [`2026-06-09-binding-trace-convention-split.md`](2026-06-09-binding-trace-convention-split.md) — signed vs double-modulus
- [`2026-06-10-binding-active-set-compute-optimization.md`](2026-06-10-binding-active-set-compute-optimization.md) — active-set truncation is precision-invalid
- [`2026-06-12-borromean-h4-q-heat-kernel-consistency-audit.md`](2026-06-12-borromean-h4-q-heat-kernel-consistency-audit.md) — μ_λ vs χ^λ vs y_λ vs w_λ disambiguation
- [`2026-06-12-alpha-k-per-force-selection-scoping.md`](2026-06-12-alpha-k-per-force-selection-scoping.md) — derived (non-fit) selection-rule discipline exemplar
- [`docs/coordination/2026-05-29-binding-a3-honesty.md`](../coordination/2026-05-29-binding-a3-honesty.md) — C_knot retraction
- [`docs/coordination/2026-06-05-step9-binding-closure.md`](../coordination/2026-06-05-step9-binding-closure.md) — binding is extensive; closure = SW-residue/jet series
- [`docs/coordination/show-mass-sweep-table.md`](../coordination/show-mass-sweep-table.md) — the fitted knot-census flag

## 7. Next steps (in order)

1. **(this PR)** This map + the heat-kernel-weight probe (§4).
2. Reconcile the production tables into one (deliverable A): depth-
   stratified-or-μ_λ default + magic-A(⁴He), tag the fitted table.
3. If μ_λ closes (tiered `derived`): promote to a content block,
   Lean §3b-cond if conditional; demote the fitted α_k.
   If it refutes: record the zero-fit refutation; the open lever
   stays the substrate-derivation of the per-depth assignment rule.
