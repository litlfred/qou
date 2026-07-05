# Brane-tower per-λ weight ↔ Δ_λ residual + magic-A: state report (bean zqyl)

**Date:** 2026-07-05
**Bean:** `zqyl` — "Brane-tower per-lambda weight: reconcile with Delta_lambda residual + magic-A"
**Type:** READ-ONLY state report (no corpus edits, no compute rewire). Feeds the gated Δ_λ / Option-E ledger.
**Scope discipline:** This report classifies every negative result as **(a) scope-limited** ("this construction, alone, does not reproduce the numbers as-is") unless a **proved invariant** is cited for a **(b) structural exclusion**. Per AGENTS.md §"Before declaring refuted/ruled out/dead end". It is a status synthesis, **not** a seventh-ansatz attempt — the Δ_λ "no 7th fit-based ansatz" gate stands.

## Summary

There is **no per-λ brane-tower weight in production.** The production binding pipeline collapses the per-block Markov decomposition to a **single scalar** τ = |tr_M(β_Bor)| ≈ 0.99856 and rides it through the dilog tower g(x) = −Li₂^q(−x). The "per-λ brane-tower weight" of this bean is a *candidate re-decomposition* of that same scalar — carrying the pairs (y_λ, χ^λ) for λ ⊢ 3A through g per block, collapsing last — and it has been **tested and found null to 6.6e-7** relative across ²H…⁵⁶Fe (PROBE 4, bean `v292`). So the un-weighted Markov re-decomposition **is not** the missing weight.

The **Δ_λ** the bean asks to "reconcile with" is the per-partition binding-energy density in the Path-D formula `B = m_e·Σ_λ y_λ χ^λ Δ_λ`. Six closure ansätze have failed (all scope-(a) or magnitude/sign-leg (b)-with-invariant), and the corpus's own diagnosis is that the missing weight must inject **per-block content beyond the Jones trace of β_Bor** (knot-ideal projector `χ^λ·χ^λ(e_{K*})` / hyperbolic-volume enrichment) — which is exactly the **s5-so3 keystone `W_λ`** object.

**"Magic-A" is a distinct, non-per-λ path.** `B = ρ_F·m_e·A·8G` (doubly-magic regime) has *no per-knot / per-λ evaluation at all* — it is dispatched precisely because the LR fusion collapses to a single self-conjugate Specht module (no Wedderburn channel). Its "reconciliation" with the per-λ tower is a **regime-split boundary**, not a shared weight. ρ_F=2 for ⁴He is an unclosed conditional-class input.

**Where the gate sits:** the geometric origin of `W_λ` (the per-λ weight that would simultaneously distinguish p/n at the trace level and close binding normalization) is **owner-gated** under the narrow s5-so3 keystone Subgoal-2 reversal. What is **agent-tractable** without owner sign-off: the exact-machinery prunes that narrow the search (done), the ℓ¹/A-scaling ceiling characterizations (done), and Lean-formalizing the proved sub-facts.

## Corpus-grep results (four paths)

Per AGENTS.md §"Before declaring open", all four paths run for topics {brane-tower, per-λ weight / y_λ / w_λ, Δ_λ, magic-A / α_cluster}. **None returns empty** — this item is heavily worked; the report below is a synthesis of extant results, not a new "open" declaration.

**Path 1 — `docs/audits/`.** Rich. Load-bearing hits:
- `docs/audits/2026-05-18-delta-lambda-gating-context.md` — the canonical Δ_λ gate doc (six failed ansätze table; Path A/B/C/D taxonomy; the RETRACTION banner of the 2026-05-26 "closure").
- `docs/audits/2026-07-02-9b-probes-alphak-perlambda-tower.md` — **the most direct hit**: PROBE 4 tests the per-λ Borromean brane tower (collapse-last) and finds it null to 6.6e-7; PROBE 2 handles α_k assignment (α_3=1 break derived, α_{k≥4}=m_e·8G plateau refuted-scope-(a) as a filtration resummation).
- `docs/audits/2026-06-28-brane-tower-formalize-first-plan.md` — single-pipeline / per-knot Borromean derivation; §7 explicitly ties the per-λ weight to Δ_λ ("one missing object answers both: distinguish p/n, and close binding").
- `docs/audits/2026-06-28-brane-tower-higher-order-deuteron.md`, `2026-06-29-brane-tower-isospin-blindness-formalized.md`, `2026-06-18-brane-tower-full-channel-regular-rep-trace.md`, `2026-05-11-brane-tower-n_star-closure-audit.md` (n_⋆ scalar selector closed by refutation, PR #638).
- Δ_λ specifics: `2026-06-28-delta-lambda-l1-ceiling-sign-only-prune.md`, `2026-06-28-delta-lambda-borromean-ascaling-diagnostic.md`, `2026-06-16-option-e-probe4-kl-positivity-prune.md`, `2026-06-14-delta-lambda-qlommel-precheck.md`, `2026-05-09-mass-table-fitting-audit.md`.

**Path 2 — `content/` (whole tree).** Hits:
- `content/quantum-observable-universe/observations/brane-tower-q-laplacian-decay.md` (+ `.ts`, `.qa.json`, `-interpretation`, `-proof` siblings) — the brane-tower convergence proposition (jet prolongation T(ρ)=Σ ℏ_q^{2n}Δ^{(n)}(ρ), geometric q^{-2} tail). This is the *convergence* content, not a per-λ weight.
- `content/quantum-observable-universe/mass-theory/magic-A-binding-formula.md` (+ `.ts`, `.qa.json`) — the doubly-magic `B=ρ_F·m_e·A·8G` formula.
- `content/quantum-observable-universe/mass-theory/tower-binding-energy.md`, `terms-2-6-higher-operations.md` — the tower binding formula content.
- `content/quantum-observable-universe/braids-and-knots/rho-k-h3a-refinement.md` — Δ_λ formal definition; `conj-rho-prefactor-structural.md` (GAP-A-4).
- `content/quantum-observable-universe/observations/diagrammatic-double-magic-lr-fusion.lean` — the LR-fusion-collapse proof underpinning the magic-A regime dispatch.

**Path 3 — `computations/`.** Hits:
- `computations/probe_9b_perlambda_brane_tower.py` → `probe-9b-perlambda-brane-tower.witness.json` (the per-λ tower probe; 9 assertions pass).
- `computations/probe_9b_alphak_structure.py`, `probe_9b_manybody_expansion.py` (α_k structure + many-body expansion).
- `computations/delta_lambda_empirical_tabulation.py` (2-row stratum tabulation), `computations/binding_canonical.py`, `computations/borromean-binding-recompute.witness.json` (scalar baseline).
- `computations/y_lambda_*` family (Wenzl-bridge y_λ closed forms — the *central* Markov coefficient, no gate) and `computations/rho_k_h3a_*` (the six-ansatz probes: co_casimir, crystal, lp_dual, frobenius_pairing, wenzl_bridge, refinement).
- `computations/option_e_*` / KL-Betti probes (`kl_betti_cell_dependence_probe.py`).

**Path 4 — `docs/coordination/`.** Hits:
- `docs/coordination/option-e.md` — **the Δ_λ closure master ledger** (v1..v9 progression; PROBE 1–4; KL-positivity prune; A=4 non-closure; the 2026-06-28 ℓ¹-ceiling coordination with z2bn).
- `docs/coordination/s5-so3-keystone.md` — the `W_λ` geometric-origin keystone (owner-gated Subgoal-2 reversal; the object the per-λ weight reduces to).
- `docs/coordination/2026-06-05-step9-binding-closure.md`, `gap-a-path-b-lambda.md`, `2026-06-24-lambda-a-fit-excised-per-knot-density.md`, `2026-06-03-nuclear-binding-color-averaging.md`, `six-term-mass-pipeline.md`.

## Current per-λ weight in use (file:line)

**Production: there is no per-λ weight.** The canonical single-pipeline binding tower operates on a **collapsed scalar**:

- τ = |tr_M(β_Bor)| ≈ 0.998562 — the Borromean-nucleon Markov (Jones) trace, carried through g(x) = −Li₂^q(−x). Scalar baseline committed at `computations/borromean-binding-recompute.witness.json` (cross-checked to 3.3e-16). Sign convention derived at `docs/audits/2026-06-28-brane-tower-formalize-first-plan.md` §2 (`g = −Li₂^q(−x)`, from the Hecke antisymmetric eigenvalue −q⁻¹).

**Candidate per-λ weight (probe only, not production).** The weight this bean names is defined in the probe:

- `computations/probe_9b_perlambda_brane_tower.py:42` — `W_λ = y_λ·d_λ` (Σ W_λ = 1 by Markov M3), with normalized block values `r_λ = χ^λ/d_λ`, collapsed last via `Σ_{λ,μ} W_λ W_μ [g(r_λ r_μ) − g(r_λ r_μ f_b)]` (line 44), consistency `Σ W_λ r_λ = τ` (line 46). Run under both Jones/TL and Wenzl z-trace conventions.

The trace decomposition it re-expresses is the SU(2)/Temperley–Lieb (Jones) form τ = ([4]/[2]³)·χ^{(3)} + (1/[2]²)·χ^{(2,1)}, y_{(1³)}=0 (DERIVED exact, 9.1e-72 at 50 dps; `docs/audits/2026-07-02-9b-probes-alphak-perlambda-tower.md` PROBE 4 table). A **RAW** per-block tower (arguments χ_λχ_μ) is **(b)-excluded** by the proved Li₂^q convergence radius |z|<q (`computations/_li_2_q_util.py::li_2_q`), forcing the *normalized* r_λ = χ^λ/d_λ, W_λ = y_λ·d_λ form.

**The α_k depth-assignment** (the depth-stratified variant of "per-level weight"): α_0=α_1=α_3=1, α_2=z²≈0.2493, α_{k≥4}=m_e·8G≈3.7445 (`docs/audits/2026-06-09-binding-canonical-default-depth-stratified.md`; α_{k≥4} uniform per `prop:plancherel-term-7-formulation`).

## Relationship to the Δ_λ gate and the six failed ansätze

The Path-D binding formula is (`docs/audits/2026-05-18-delta-lambda-gating-context.md:44`):

    B(K) = m_e · Σ_{λ⊢3A} y_λ(q₀) · χ^λ(β_K) · Δ_λ(K)

where y_λ (Wenzl, closed-form, no gate) and χ^λ (Hoefsmit/markov_peel/branching, no gate) are known, and **Δ_λ(K) is the open per-block density**. Δ_λ is load-bearing only for **Path D** (declared canonical for Track A by PR #564's T6 resolution); Path B (Borromean tower) bypasses Δ_λ at the cost of the per-atom λ(K) derivation.

**The six failed ansätze** (`2026-05-18-delta-lambda-gating-context.md` §"Closure attempts"; all scope-(a) fits or magnitude-blind):

| # | Ansatz | Selector | Outcome on deuteron |
|---|--------|----------|---------------------|
| A | Occam single-support | min\|Δ\| singleton | underdetermined; arbitrary (λ=[5,1], Δ=−22.96) |
| B | Frobenius co-Casimir 1/dim_q(λ) | theorem-forced | fails, −2.30 MeV (wrong sign, vortex-blind) |
| C | Demazure-fibre y_λ·D_w/D_w₀ | 5/8 Demazure | fails, Δ_λ~10⁻⁵ (reproduces M_LO tautologically) |
| D-Pl | LP-Plancherel shadow price | min Σ\|Δ_λ\|·w_λ | reproduces Occam (underdetermination → cost choice) |
| D-Fr | LP-Frobenius shadow price | alt LP cost | different singleton (λ=[6], Δ=−47.16) |
| E | crystal-graph weight | Kashiwara q→1 | refuted (see below) |
| F | augmented Markov | new B-energy axiom | physics input, not a derivation |

**How the per-λ brane-tower weight relates to these:**

1. **The bean's per-λ tower is NOT ansatz #7.** Per the PROBE-4 discipline note (`2026-07-02-9b…` line 106): it introduces *no new constant* — the (y_λ, χ^λ) pairs are exactly the decomposition the scalar pipeline already collapses. It is a re-decomposition test, explicitly permitted.

2. **Result: it does not close the residual (scope-(a)).** All three collapse-last variants (per-λ Jones, per-λ Wenzl, ambient-H₆ per-ν with exact Murnaghan–Nakayama + LR branching) reproduce the scalar tower to ≤ 6.6e-7 relative. ¹⁶O errT 2.2752 → 2.2752. The Jensen gap of g over the block spread r=(1, 0.997093, 1) is O(10⁻⁶). **Conclusion (corpus, verbatim):** "the missing per-λ weight, if it exists, cannot be the un-weighted Markov decomposition (y_λ, χ^λ) of the same Borromean trace carried through the same g. It must inject per-block information beyond the Jones trace of β_Bor."

3. **This is the same wall the six ansätze hit, from the other side.** Ansätze A–F tried to *derive Δ_λ from single-nucleon / q-algebraic data*; PROBE 4 shows the *pure Markov re-decomposition* is also insufficient. Both converge on the corpus's frontier object: **χ^λ·χ^λ(e_{K*})** (FR-restricted knot-ideal projector / hyperbolic-volume enrichment), = the s5-so3 keystone `W_λ`.

4. **Option-E state (`docs/coordination/option-e.md`):** deuteron NOT closed (the 2026-05-26 claim retracted; best parameter-free = interface-knot+T3, −31%). A=3 mirror pair near-matched 0.11%/+0.12% via `(1+q)/2` — PROBE 1 REFUTED it as a fit (required factor 1.05372 ≠ (1+q)/2=1.05499). A=4 UNSUBSTANTIATED (full 77-partition f^λ sum → −80.4%). KL-Betti is **contributive not closing** (×2.0 on deuteron, ×5.85 needed) — scope-(a).

## Magic-A reconciliation — what it would require

The magic-A formula (`content/quantum-observable-universe/mass-theory/magic-A-binding-formula.md`) is:

    B(^A_Z X) = ρ_F · m_e · A · 8G,   8G = Vol(L6a4) = Vol(Borromean),  ρ_F ∈ ℝ

For ⁴He (ρ_F=2): B ≈ 29.956 MeV vs 28.296 experimental, **+5.9%** — far tighter than the alpha-shift formula's −79%.

**It is architecturally NOT a per-λ object.** The magic-A path is dispatched precisely *because* there is no Wedderburn channel to carry per-λ binding: `prop:diagrammatic-double-magic-lr-fusion` (Lean `diagrammatic-double-magic-lr-fusion.lean`) proves that at a doubly-magic level (Z, N ∈ {2,8,20,28,50,82,126}) the LR fusion of the Z-block and N-block collapses to a **single self-conjugate Specht module**. The per-rep Reeb-phase mechanism that generates the per-λ weight *vanishes* (no hyperbolic knot); binding is set by the universal Borromean residue 8G × nucleon count.

**So "reconciling the per-λ brane-tower weight with magic-A" means characterizing the regime boundary, not sharing a weight:**

1. **The regime split itself is the reconciliation.** `rem:strutinsky-from-graded-trace` gives `tr_M = tr_gr(σ(T_w)) + Res_GB(T_w)`; the per-λ (Wedderburn / graded) content and the residue content are the two summands. The doubly-magic case is the rectangular-spike limit where `H_q(λ)` factorises (`prop:shell-schur-weyl-self-duality`) and the per-λ channel degenerates. A reconciliation would need to show the per-λ brane tower **continuously degenerates to `ρ_F·A·8G` at rectangular λ** — i.e. that magic-A is the λ→rectangular limit of the per-λ tower, not a separate formula.

2. **ρ_F would have to be derived.** ρ_F=2 for ⁴He is currently an **unclosed conditional-class input** (`magic-A-binding-formula.md` §"ρ_F for ⁴He": "The categorical derivation of the integer 2 — vs [2]_q, 2cos(π/3), or another natural candidate — is not closed … consumed as an input hypothesis per AGENTS.md §3b-cond"). A genuine reconciliation must produce ρ_F from the same categorical action that would produce Δ_λ.

3. **Note the α_{k≥4} plateau = m_e·8G is the SAME constant** as the magic-A per-nucleon quantum (8G = Vol(Borromean)). PROBE 2b tested whether m_e·8G is a z-geometric resummation of the GB-filtration layer counts Σ_{k≥4} z^k·N_k and found **REFUTED-scope-(a)** (A-independence of the plateau vs A-dependence of any per-atom layer count). This is a partial reconciliation attempt between the depth-tower plateau and the magic-A residue that failed as-is.

## Scope classification

Every negative result in this report is **(a) scope-limited** — "this construction, alone, does not reproduce the numbers as-is" — with the following exceptions where a **proved invariant** licenses **(b) structural exclusion** (cited):

- **(b), invariant cited — RAW per-block tower divergence.** χ^{(2,1)}²≈3.9768 > q₀≈1.10998 exceeds the **proved** Li₂^q convergence radius |z|<q (`computations/_li_2_q_util.py::li_2_q` returns ∞ at |z|≥q). Excludes the *un-normalized* per-block argument form; forces normalized r_λ. (`2026-07-02-9b…` PROBE 4.)
- **(b), invariant cited — sign-leg of Δ_λ from KL data.** Target Δ_λ = sgn(w₀^{S_λ'})·dim is mixed-sign (Lean-proved `PartitionOf5.deltaSign_mixed`, sorry-free); KL multiplicities are non-negative (KL positivity, engine-verified S₄, PR #2381). A Σ_w n^w_λ·X_w sum supplies at most magnitude |Δ_λ|=dim, never the chirality sign. (`option-e.md` KL-positivity prune; `2026-06-16-option-e-probe4-kl-positivity-prune.md`.)
- **(b), invariant cited — sign-only re-derivation ℓ¹ ceiling.** Triangle inequality bounds any sign/chirality reassignment by ‖c‖₁=Σ|y_λ χ^λ dim_λ|; measured ‖c‖₁/|target| < 1 for D/T/³He/⁴He ⇒ a magnitude-adding ingredient is *necessary*. (Lean `DeltaLambdaL1Ceiling.lean`, sorry-free; `2026-06-28-delta-lambda-l1-ceiling-sign-only-prune.md`.)

**Everything else is (a):**

- **The bean's core result — un-weighted per-λ Markov re-decomposition does not close the ¹⁶O 2.3× (or any isotope) — is (a), NOT (b).** Why not (b): there is **no proved invariant** forbidding a per-λ weight *in general*. The 6.6e-7 null result excludes only the *specific* construction "un-weighted (y_λ, χ^λ) of the same β_Bor Jones trace through the same g." The corpus explicitly leaves the door open to a weight that "injects per-block information beyond the Jones trace" (the knot-ideal projector / `W_λ`). Writing this as "per-λ weights refuted" would over-narrow the search — exactly the failure mode AGENTS.md §"refuted" warns against. A compositional/trace object (1−∏fᵢ, the tower) is already many-body; showing the pairwise re-decomposition is insufficient measures the size of the missing higher term, it does not exclude the per-λ factor.
- α_{k≥4}=m_e·8G not a filtration resummation: (a) (other weightings untested; A-independence rules out the *layer-count family*, not all A-independent structures).
- α_3=1 exactly: NEAR-MATCH (residual 1+q^{1/2}−q^{-1/2}≈1.1044, →1 as q→1), not refuted.
- Option-E v9 (1+q)/2, KL-Betti contributive, A=4 f^λ: all (a).

## What is gated vs tractable

**Owner-gated (do NOT attempt without explicit owner sign-off):**

1. **The geometric origin of `W_λ`** — the per-block weight that would inject "content beyond the Jones trace" and simultaneously (i) distinguish p/n at the trace level and (ii) close binding normalization. This reduces to the **s5-so3 keystone** (`docs/coordination/s5-so3-keystone.md`): does the colored Σ(2,3,5) WRT / `E_q(2)` q-Bessel q-series evaluated at q₀ reproduce the `W_λ` family? This is **Subgoal-2** (substrate-derivation territory), owner-declined **except** the narrow keystone geometric-`W_λ` DG/WRT construction reversal (2026-06-19, PRs #2503/#2524). The reversal is narrow: it does not reopen fit-based q₀ derivation, and the **Δ_λ "no seventh fit-based ansatz" rule still stands**.
2. **A seventh fit-based Δ_λ ansatz** — explicitly banned (AGENTS.md §Precision-goals; caught by three-calibration discipline review).
3. **Deriving ρ_F for magic-A** by fitting — same ban; must come from the categorical action.
4. **Migrating the ~840 muon-q₀ `computations/` witnesses** — gated (bean `tnjb`), unrelated but a standing gate.

**Agent-tractable (no owner sign-off needed) — the formalize-first narrowing:**

1. **Prune-tightening on the existing frontier** — the exact-machinery probes that *narrow* the search without fitting: the α_3 break theorem (natural Lean target `chi21_garside_zero`, pure algebra, generic ring per §7c), the ℓ¹/A-scaling ceiling characterizations, KL-Betti cell-dependence. These are DONE or Lean-formalizable.
2. **Re-express the binding tower over β_Bor and re-validate against AME** (`2026-06-28-brane-tower-formalize-first-plan.md` §"Next action") — the per-knot Borromean single pipeline; a validation, not a fit. Note it *changes* every binding number, so it is a hypothesis to test, not a free fix.
3. **Lean-prove the true convergence bound** `|tr_M(β_Bor)|<1 ⇒ pair traces < q₀` (Q3 resolution) — replaces the false atom-word bound.
4. **z2bn magnitude-side generating function** (`Ŝ(z)=Σ dim_q(λ) z^m/[m]_q!`, q-Gaussian/Habiro, sorry-free Lean `BindingQGaussianHabiro`) — pinning the structure of the magnitude object the ℓ¹-ceiling shows is necessary. Structure-pinning is tractable; the closure downstream of it touches the gated `W_λ`.
5. **Documenting the regime-boundary reconciliation** between the per-λ tower and magic-A (the Strutinsky graded/residue split, the shared m_e·8G constant) — this state report.

**Bottom line for bean zqyl:** the per-λ brane-tower weight and the Δ_λ residual are *the same open object*, and the honest reconciliation is that (i) the cheapest candidate (pure Markov re-decomposition) is numerically excluded to 6.6e-7 scope-(a), (ii) the surviving candidate is the knot-ideal-projector `W_λ` whose *geometric derivation* is owner-gated behind the s5-so3 keystone, and (iii) magic-A is a **separate, degenerate-λ regime** with an unclosed ρ_F input, reconciled to the per-λ tower only as the rectangular-λ limit (shared 8G residue), not as a shared weight. No item here is refuted in scope (b) beyond the three invariant-cited legs above.

## Key files

- `docs/audits/2026-05-18-delta-lambda-gating-context.md` (the gate)
- `docs/audits/2026-07-02-9b-probes-alphak-perlambda-tower.md` (the direct per-λ tower probe — null to 6.6e-7)
- `docs/coordination/option-e.md` (Δ_λ master ledger)
- `docs/coordination/s5-so3-keystone.md` (the owner-gated `W_λ` object)
- `docs/audits/2026-06-28-brane-tower-formalize-first-plan.md` (single-pipeline / per-knot Borromean derivation, §7 per-λ↔Δ_λ↔p/n unification)
- `content/quantum-observable-universe/mass-theory/magic-A-binding-formula.md` (magic-A, separate regime)
- `computations/probe_9b_perlambda_brane_tower.py` (candidate W_λ = y_λ·d_λ, probe-only)
