# Δ_λ ansatz refutations (5 remaining) — anchored scope-(a) survey (bean b9ra)

**Date:** 2026-07-05
**Bean:** `b9ra` — document the 5 remaining Δ_λ-ansatz refutations at their correct anchors, scope-disciplined.
**Type:** READ-ONLY corpus synthesis. NON-Lean (owner directive: refutations do not need Lean formalization unless needed as a lemma for another proof). Feeds the gated Δ_λ / Option-E ledger; **not** a seventh-ansatz attempt.
**Scope discipline:** Per AGENTS.md §"Before declaring refuted / ruled out / dead end", every negative below is classified as **(a) scope-limited** ("this construction, *alone*, does not reproduce the numbers as-is") unless a **proved invariant** licenses **(b) structural exclusion** — in which case the invariant is cited. No ingredient is declared (b)-excluded without a cited proved invariant.

## Summary

The per-isotope binding formula (Path D, declared canonical for Track A by PR #564's T6 resolution) is

    B(K) = m_e · Σ_{λ ⊢ 3A} y_λ(q₀) · χ^λ(β_K) · Δ_λ(K)

([`docs/audits/2026-05-18-delta-lambda-gating-context.md:44`](2026-05-18-delta-lambda-gating-context.md)). Here `y_λ` (Wenzl closed form) and `χ^λ` (Hoefsmit / markov_peel / branching) carry no gate; **Δ_λ(K)**, the per-partition binding-energy density, is the open R&D. Six closure ansätze have failed. This doc records the **five non-Lean refutations** at their **correct anchors** with the backing probe + witness and a scope classification. The sixth — **Frobenius co-Casimir** — is already machine-checked sorry-free and is cross-referenced (not redone) in §"Co-Casimir (already Lean-formalized)".

**Anchor caution (the whole point of this doc).** The six ansätze were **not all tested on the deuteron**. In particular the **Demazure** family was screened at **H₅/H₆/H₇** as an h²-sign prescreen (target −G), *not* on the deuteron binding number; conflating that anchor with the deuteron misreads its refutation. Each subsection names the anchor the probe actually used.

**Bottom line.** Four of the five are **(a) scope-limited** (under-determined LP cost choice, tautological Demazure fibre ratio, convention-dependent augmented-Markov prior). The **crystal-graph** family carries a numeric **(a)** WRONG_SIGN miss *and* an independent **(b) structural** sign-leg exclusion via the Lean-proved KL-positivity prune. **None of these excludes the per-λ weight ingredient in general** — the surviving candidate is the owner-gated s5-so3 keystone `W_λ` knot-ideal projector (§"What remains open").

| # | Ansatz | Correct anchor | Result | Backing witness | Scope |
|---|--------|----------------|--------|-----------------|-------|
| C | Demazure-fibre `y_λ·D_w/D_{w₀}` | H₅/H₆/H₇ h²-sign prescreen (+ n=2,3 D_w/D_{w₀} evaluator) | no scheme hits −G (closest Δ=1.499 at H₄); fibre ratio ⇒ Δ_λ~10⁻⁵ tautological | `demazure-sub-crystal-prescreen-50dps` / `demazure-markov-trace` | **(a)** |
| D-Pl | LP-Plancherel shadow price | deuteron (H₆, 11 parts) | under-determined; singleton λ=[5,1], Δ=−22.96; L∞=1.9e-15 | `rho-k-h3a-lp-dual` | **(a)** |
| D-Fr | LP-Frobenius shadow price | deuteron (H₆) | under-determined; different singleton λ=[6], Δ=−47.16 | `rho-k-h3a-lp-dual` | **(a)** |
| E | crystal-graph (Kashiwara `c_λ(q)`) | deuteron (H₆), q₀ and q→1 | **WRONG_SIGN**; sum/target = −412.7 (q₀) / −75.9 (q=1); closure err 920 MeV | `rho-k-h3a-crystal` | **(a)** numeric + **(b)** sign-leg |
| F | Wenzl-bridge augmented Markov | deuteron (H₆), 11-var system | closure-pickle on first attempt; on rerun a convention-dependent uniform Δ_λ=Δρ_D "max-entropy prior", not a measurement | `rho-k-h3a-wenzl-bridge` | **(a)** |

Common deuteron target (all H₆ probes): `target_signed = −B_D/m_e = −4.35336728187014…` m_e units (B_D = 2.2245661 MeV), and `|tr_M(β_D)| = 0.38828647…` at q₀ (Schur–Weyl cross-check residual 3.3e-51).

---

## C — Demazure-fibre `y_λ · D_w / D_{w₀}`

**Ansatz.** Assign `Δ_λ` from the Demazure character ratio `D_w(λ)/D_{w₀}(λ)` (principal q-specialisation of the Schur polynomial), i.e. `c_λ(q) := s_λ(1,q,…,q^{n−1})`, per the §7b "Demazure sub-crystals for resonances" authoring shortcut.

**Selector/mechanism.** Kashiwara weight-lattice projection replacing the hand-built Hecke-energy LP cost vector; the fibre ratio `D_w/D_{w₀}` picks a per-partition weight from the 5/8 Demazure functional.

**Correct anchor — NOT the deuteron directly.** Two distinct probes, neither anchored on the deuteron binding number:

1. **H₅/H₆/H₇ h²-sign prescreen** — [`computations/demazure_sub_crystal_h5_h6_h7_prescreen.py`](../../computations/demazure_sub_crystal_h5_h6_h7_prescreen.py) → [`computations/demazure-sub-crystal-prescreen-50dps.witness.json`](../../computations/demazure-sub-crystal-prescreen-50dps.witness.json). Tests 6 normalization schemes (full Wedderburn, per-irrep, bar-symmetric, self-conjugate, two-row, rectangle) against Reading-A's target h² coefficient **−G** at q₀ (50 dps). **Verdict (witness `verdict` field):** *"NO simple sub-sum scheme yields h² ≈ −G at any tested N. Closest is `S2_per_irrep_dim_normalized` at H₄ with Δ = 1.4993 — far above the 1e-3 threshold."* The Demazure-derived sub-sums give **positive** h² where binding needs h² ≈ −G < 0.

2. **D_w/D_{w₀} evaluator at n=2,3** — [`computations/demazure_markov_trace.py`](../../computations/demazure_markov_trace.py) → [`computations/demazure-markov-trace.witness.json`](../../computations/demazure-markov-trace.witness.json). Confirms `D_{w₀}(λ)` = Schur principal specialisation (`demazure_w0_equals_schur`, `diff_simplified: "0"` for all λ ⊢ 2, 3; symbolic in q). The fibre ratio produces `Δ_λ ~ 10⁻⁵`, which **reproduces `M_LO` tautologically** (gives back the constituent sum with ~zero binding), per [`2026-05-18-delta-lambda-gating-context.md:67`](2026-05-18-delta-lambda-gating-context.md) row C.

**Scope: (a) scope-limited.** The prescreen excludes only the *simple* Wedderburn-derived sub-sums it enumerated; the witness itself says genuine Kashiwara/KLR crystal machinery is untested. No proved invariant forbids a Demazure-derived weight in general. Do **not** write "Demazure refuted" — write "simple Demazure-fibre sub-sums, alone, do not produce the h² sign (closest Δ=1.499) and the D_w/D_{w₀} ratio is tautological."

---

## D-Plancherel — LP shadow price, Plancherel cost

**Ansatz.** Resolve the underdetermined mass equation (1 equation, 11 unknown Δ_λ at the deuteron) by an operator-selection LP (`prop:operator-selection-lp`) with Plancherel cost `t_λ = 1/dim_q(λ)`, minimising `Σ|Δ_λ|·w_λ`.

**Selector/mechanism.** LP dual shadow prices lift the rank-deficient constraint manifold to a unique extremum.

**Correct anchor — deuteron (H₆, 11 partitions of 6).** [`computations/rho_k_h3a_lp_dual.py`](../../computations/rho_k_h3a_lp_dual.py) → [`computations/rho-k-h3a-lp-dual.witness.json`](../../computations/rho-k-h3a-lp-dual.witness.json), `lp_primary`. Duals emitted per the LP/SDP infra rule: `y0_star = −1.01025`, `primal_obj = dual_obj = 4.39799`, `duality_gap = 0.0`. **Result:** picks the singleton λ=[5,1] with `Delta_lambda_lp_primary = −22.9594…`; reproduces the legacy Occam single-support solution exactly (L∞ = 1.9e-15, [`2026-05-18-delta-lambda-gating-context.md:68`](2026-05-18-delta-lambda-gating-context.md) row D-Plancherel).

**Scope: (a) scope-limited (under-determined, not a numeric miss).** The LP *can* close the single deuteron equation — the defect is that it does so non-uniquely: it merely **shifts the underdetermination from a value choice to a cost choice.** No invariant is violated; a different cost gives a different Δ_λ (see D-Frobenius). Every operator-selection LP needs *some* cost vector to lift the rank-deficient manifold (witness `notes`), so "closes the deuteron" here is not evidence of the right Δ_λ.

---

## D-Frobenius — LP shadow price, Frobenius cost

**Ansatz.** Same LP, alternate categorically-motivated cost `t_λ = |χ^λ(β_D)|` (Frobenius character weight).

**Correct anchor — deuteron (H₆).** Same witness, `lp_secondary`: `y0_star = −16.8954`, `primal_obj = dual_obj = 73.5519`, `duality_gap = 1.4e-14`. **Result:** picks a **different** singleton, λ=[6], with Δ=−47.16 ([`2026-05-18-delta-lambda-gating-context.md:69`](2026-05-18-delta-lambda-gating-context.md) row D-Frobenius).

**Scope: (a) scope-limited.** The disagreement between D-Plancherel (λ=[5,1], Δ=−22.96) and D-Frobenius (λ=[6], Δ=−47.16) *is* the refutation: the LP framework has no canonical cost, so the "solution" is a free parameter (the cost vector). This is the same defect as D-Plancherel, exhibited by producing two incompatible answers. Not (b) — nothing is structurally excluded; the LP cost is simply an unfixed DOF.

---

## E — crystal-graph (Kashiwara `c_λ(q)`)

**Ansatz.** Take `Δ_λ = c_λ(q) := s_λ(1,q,…,q^{n−1})`, the Kashiwara symmetric-crystal weight (Macdonald hook-content = Demazure `D_{w₀}(λ)` at principal specialisation; → `dim V_λ` = `|B(λ,n)|` as q→1).

**Selector/mechanism.** Crystal-basis cardinality / principal-specialised Schur weight per partition.

**Correct anchor — deuteron (H₆), evaluated at both q₀ and q→1.** [`computations/rho_k_h3a_crystal.py`](../../computations/rho_k_h3a_crystal.py) → [`computations/rho-k-h3a-crystal.witness.json`](../../computations/rho-k-h3a-crystal.witness.json). `crystal_self_test` confirms `c_λ(1) = |B(λ,n)|` (Weyl dim) for all λ ⊢ 6 (`agree: true`). **Outcome field: `WRONG_SIGN`.**

| eval | `Σ y_λ χ^λ c_λ` | ratio sum/target | M_pred (MeV) | closure err |
|------|-----------------|------------------|--------------|-------------|
| q₀ | +1796.735 | **−412.7** | 2795.97 | 920.35 MeV (490695 ppm) |
| q→1 | +330.347 | **−75.9** | 2046.64 | 171.03 MeV (91187 ppm) |

The predicted sum is **large and positive** where the target `−4.3534` is small and negative — off by ~2–3 orders of magnitude *and* sign. The witness `honest_reporting` states the diagnostic `alpha_E` (the would-close-it factor) is ≈ −0.0024 (q₀) / −0.0132 (q=1), i.e. far from 1: *"the Kashiwara crystal weights are NOT the correct closed form for Δ_λ."* The weights are **not** scaled to force closure.

**Scope: (a) numeric miss, plus (b) sign-leg structurally excluded (invariant cited).**

- **(a):** The direct `c_λ(q)` substitution is a scope-limited WRONG_SIGN miss on the deuteron — this construction alone does not reproduce the number.
- **(b), invariant cited:** The *sign leg* of any KL-multiplicity-based crystal closure is structurally excluded. The target `Δ_λ = sgn(w₀^{S_{λ'}})·dim` is **mixed-sign** (Lean-proved sorry-free `QOU.BraidsAndKnots.S5SO3FiberAction.PartitionOf5.deltaSign_mixed`; n=3: 1+/2−, n=6: 6+/5−); KL multiplicities `n^w_λ` are **non-negative** (KL positivity, engine-verified at S₄, PR #2381). Therefore `Σ_w n^w_λ·X_w` supplies at most the magnitude `|Δ_λ|=dim`, never the chirality sign — the sign must come exogenously. The magnitude leg is separately (a): KL left-cell Betti sums `B_λ` are **not cell-invariant** (`kl-betti-cell-dependence.witness.json`, [`docs/coordination/option-e.md`](../coordination/option-e.md) 2026-06-25 row), so they cannot canonically supply `|Δ_λ|` either — but that is scope-(a), not a structural exclusion of KL data from every closure. Refs: [`2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md); PR #2416.

---

## F — Wenzl-bridge augmented Markov

**Ansatz.** Augment the Markov-trace axioms with an extra binding-energy datum `b_μ = Δρ·z^{n−ℓ(μ)}` per cycle type μ, turning the 1-equation deuteron system into a solvable 11×11 linear system for the 11 Δ_λ.

**Selector/mechanism.** Wenzl z-trace bridge + auxiliary cycle-type anchors as extra equations.

**Correct anchor — deuteron (H₆), 11-variable augmented system.** [`computations/rho_k_h3a_wenzl_bridge.py`](../../computations/rho_k_h3a_wenzl_bridge.py) → [`computations/rho-k-h3a-wenzl-bridge.witness.json`](../../computations/rho-k-h3a-wenzl-bridge.witness.json): `outcome: "uniquely-solvable"`, rank 11, cond 31.7, `max_residual 0.0`, using 10 auxiliary cycle-type variants (`w_(6,)`…`w_(2,2,2)`) as the extra rows. **First attempt** hit a closure-pickle bug (no result; [`2026-05-18-delta-lambda-gating-context.md:71`](2026-05-18-delta-lambda-gating-context.md) row F, "TBD (closure-pickle bug on first attempt)").

**Result / honesty caveat (witness `notes`, verbatim scope):** *"the Δ_λ Wenzl bridge yields a UNIQUE algebraic solution (Δ_λ = Δρ_D uniformly), but uniqueness depends on the `b_μ = Δρ·z^{n−ℓ(μ)}` convention. Other choices of b_μ correspond to additional physical anchors … that we do not have for the deuteron alone. The derived Δ_λ profile should be read as the 'maximum-entropy / y_λ-proportional' prior, not as a measurement."*

**Scope: (a) scope-limited.** The uniform `Δ_λ = Δρ_D` "solution" is a convention-dependent prior: it reproduces the LO residual **by construction** (a physics input that *fixes* Δ_λ, not one that *derives* it — [`2026-05-18-delta-lambda-gating-context.md:71`](2026-05-18-delta-lambda-gating-context.md)). The Lean landscape table calls this "ill-posed — over-determined axiom set (closure-pickle)" ([`DeltaLambdaRefutation.lean:108`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/DeltaLambdaRefutation.lean)); more precisely it is *under-constrained in the choice of anchor set* and *over-determined once anchors are fixed by convention*. Either way no invariant is violated — (a), not (b).

---

## Co-Casimir (already Lean-formalized) — cross-reference, not redone

The sixth ansatz, **Frobenius co-Casimir `1/dim_q(λ)`** (Option B, theorem-forced, no free params), is the one refutation already machine-checked sorry-free per the formalize-first / formalize-the-refutation discipline. **Do not redo it here.**

- **Lean:** [`content/quantum-observable-universe/lean/QOU/BraidKnot/DeltaLambdaRefutation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/DeltaLambdaRefutation.lean) — `coCasimir_refuted_deuteron` (magnitude: `tol < |coCasimirSum − targetSigned|`, gap ≈ 4.498 m_e ≫ tol=1) and `coCasimir_wrong_sign` (`0 < coCasimirSum ∧ targetSigned < 0`). Decidable rational (in)equalities, `norm_num`-discharged over ℚ, sorry-free.
- **Witness:** [`computations/rho-k-h3a-co-casimir.witness.json`](../../computations/rho-k-h3a-co-casimir.witness.json) (50 dps, `allPassed: true`): `sum_contributions_signed = +0.14495922…` (positive), deuteron target `−4.35336728…` (negative); `M_pred = 1877.91 MeV`, `residual = −2.2986 MeV` (−0.1226%); `closure_gap = 4.49832651…`.
- **Why it is the one formalized:** co-Casimir fails as a *clean numeric miss + wrong sign* (a `≠` fits it), so it maps onto a machine-checked inequality. The other five fail by structurally different mechanisms (tautology / under-determination / convention-dependence / sign-vs-positivity) that do not fit a miss-shaped lemma — they are catalogued by mechanism in the same file's landscape table ([`DeltaLambdaRefutation.lean:101–113`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/DeltaLambdaRefutation.lean)) and, for crystal-graph, independently Lean-proved via `deltaSign_mixed`. This doc supplies the anchored, scope-disciplined prose face of rows C, D-Pl, D-Fr, E, F.

Consistent with the owner directive: refutations do **not** need their own Lean formalization unless required as a lemma for another proof. The co-Casimir Lean file exists because it *is* used as the "no 7th ansatz" gate operand; the other five are documented, not forced into Lean.

---

## Scope discipline (a/b with cited invariants)

Per AGENTS.md §"Before declaring refuted", the classification is:

**(a) scope-limited negatives — the default here** (this construction, *alone*, does not reproduce the numbers as-is; constrains magnitudes/combinations, **not** ingredients):

- **C Demazure-fibre** — simple sub-sums miss the h² sign (closest Δ=1.499 at H₄); D_w/D_{w₀} ratio is tautological. Crystal/KLR machinery untested.
- **D-Plancherel / D-Frobenius** — LP closes the single deuteron equation but non-uniquely; the cost vector is an unfixed DOF (two incompatible singletons).
- **E crystal-graph (numeric)** — WRONG_SIGN on the deuteron for the direct `c_λ(q)` substitution.
- **F augmented-Markov** — convention-dependent uniform prior, not a measurement.
- **Co-Casimir (magnitude)** — a −0.12%-of-M miss / gap ≈ 4.5 m_e; scale-free only via the sign leg.

**(b) structural exclusions — only where a proved invariant is cited:**

1. **Sign leg of any KL-multiplicity crystal closure (row E).** Invariant: `deltaSign_mixed` (Lean, sorry-free — target is mixed-sign) + KL positivity (engine-verified S₄, PR #2381 — multiplicities ≥ 0). A non-negative weight sum can supply magnitude but never chirality sign. Refs: [`2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md), PR #2416.
2. **Co-Casimir wrong sign (row B, cross-ref).** Invariant: positivity of any overall normalisation `ρ > 0` cannot repair `pred > 0` vs `target < 0` — Lean `coCasimir_wrong_sign`.
3. **RAW (un-normalized) per-block tower (adjacent, from the zqyl report).** Invariant: proved Li₂^q convergence radius `|z| < q` (`computations/_li_2_q_util.py::li_2_q`); `χ^{(2,1)}² ≈ 3.977 > q₀ ≈ 1.110` diverges — forces normalized `r_λ = χ^λ/d_λ`. (Not one of the five ansätze; recorded to keep the (b) list complete.)
4. **Sign-only Δ_λ re-derivation ℓ¹ ceiling (adjacent).** Invariant: triangle inequality, `‖c‖₁/|target| < 1` for D/T/³He/⁴He (Lean `DeltaLambdaL1Ceiling.lean`, sorry-free) ⇒ a *magnitude-adding* ingredient is necessary. Bounds the sign-repair class, not any ingredient.

Everything **not** on the (b) list is (a). In particular the **magnitude leg** of the crystal/KL family (KL-Betti `B_λ`) is (a), not (b): `B_λ` is not cell-invariant, so it has no canonical value — but no invariant forbids KL data from *contributing* magnitude (measured ×2.0 uplift on the deuteron, contributive-not-closing, [`docs/coordination/option-e.md`](../coordination/option-e.md) 2026-06-24 row).

---

## What remains open (owner-gated `W_λ`)

**These five scope-(a) negatives do NOT exclude the per-λ weight ingredient in general.** Independent evidence (bean zqyl, [`docs/audits/2026-07-05-brane-tower-per-lambda-weight-delta-lambda-state.md`](2026-07-05-brane-tower-per-lambda-weight-delta-lambda-state.md)) shows the cheapest per-λ candidate — the *un-weighted* Markov re-decomposition `(y_λ, χ^λ)` of the same Borromean trace through the same dilog `g` — is null to 6.6e-7 across ²H…⁵⁶Fe (also scope-(a)). Both the six ansätze and the pure re-decomposition converge on the **same** conclusion: the missing weight must inject **per-block content beyond the Jones trace of β_K** — the FR-restricted knot-ideal projector `χ^λ·χ^λ(e_{K*})` / hyperbolic-volume enrichment.

That object is the **s5-so3 keystone `W_λ`** ([`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)). Its geometric derivation (the colored Σ(2,3,5) WRT / `E_q(2)` q-Bessel construction of the `W_λ` family) is **Subgoal-2 substrate-derivation territory**, owner-declined **except** the narrow keystone geometric-`W_λ` DG/WRT reversal (2026-06-19, PRs #2503/#2524). The reversal is narrow: it does **not** reopen fit-based q₀ derivation, and the **Δ_λ "no seventh fit-based ansatz" gate still stands** (AGENTS.md §Precision goals; caught by the three-calibration discipline review).

**Do not** read this survey as licence for a v10 ansatz. The productive, agent-tractable directions remain the formalize-first prunes that *narrow* the search without fitting (ℓ¹/A-scaling ceilings, KL-Betti cell-dependence, the α₃ break theorem) — all done or Lean-formalizable — and the owner-gated `W_λ` geometric build. The five ansätze above are recorded here so the next session does not re-walk them.

## Key files

- [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — the six-ansatz gate (Path A/B/C/D taxonomy; Δ_λ formal role)
- [`docs/coordination/option-e.md`](../coordination/option-e.md) — Δ_λ closure master ledger (v1..v9, PROBE 1–4, KL prunes, ℓ¹ ceiling)
- [`docs/audits/2026-07-05-brane-tower-per-lambda-weight-delta-lambda-state.md`](2026-07-05-brane-tower-per-lambda-weight-delta-lambda-state.md) — companion per-λ-weight state report (bean zqyl)
- [`content/quantum-observable-universe/lean/QOU/BraidKnot/DeltaLambdaRefutation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/DeltaLambdaRefutation.lean) — co-Casimir sorry-free refutation + five-ansatz landscape table
- Probes / witnesses (all under `computations/`): `demazure_sub_crystal_h5_h6_h7_prescreen.py` / `demazure-sub-crystal-prescreen-50dps.witness.json`; `demazure_markov_trace.py` / `demazure-markov-trace.witness.json`; `rho_k_h3a_lp_dual.py` / `rho-k-h3a-lp-dual.witness.json`; `rho_k_h3a_crystal.py` / `rho-k-h3a-crystal.witness.json`; `rho_k_h3a_wenzl_bridge.py` / `rho-k-h3a-wenzl-bridge.witness.json`; `rho_k_h3a_co_casimir.py` / `rho-k-h3a-co-casimir.witness.json`
