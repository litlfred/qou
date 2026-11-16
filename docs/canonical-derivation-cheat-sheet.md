# Canonical derivation cheat sheet — substrate → observables

**Audience**: math/phys starting grad — a one-page-up map of "where every QOU formula comes from" and "which script computes it". Treats the chain as a cookbook so you don't have to dig through 700+ scripts to find what's canonical.

**Paper-side companion**: [`prose:pre-archimedean-derivation-chain`](../folio/quantum-observable-universe/mass-theory/pre-archimedean-derivation-chain.md) (the rendered version that appears in the paper, in the Mass Analysis chapter's "Pre-Archimedean Derivation Chain and Audit" section). This doc adds the **compute-pipeline mapping**, **Phase 5 findings**, and the **migration backlog** that don't belong in the paper but are essential for code review.

**Highlight to Claude** — referenced from AGENTS.md so any agent picking up final-stage QOU work has the full canonical chain visible.

> **🛑 ABSOLUTE MASS EXCISED (owner ruling 2026-08-11, bean `qou-exam`).** Every "absolute nucleon/atom mass" entry below (`m_p ≈ 938.27 MeV`, `m_n ≈ 939.56 MeV`, the Step-9a "absolute mass identity") is retained for the compute map but is **no longer a framework prediction** — it is an `m_e`-scaled *realization of the dimensionless ratio* (`m_p/m_e`), since m_e (CAL-1) sets the MeV scale by fiat. The predictive content is the ratio / binding / Q-value / splitting; the `canonical_mass.py` facade and the muon-anchored form still stand as the correct *ratio realization*. Read "absolute mass" below as "the `m_e`-scaled ratio, rendered in MeV". Full ruling: [`audits/2026-08-11-excise-absolute-mass-notion.md`](audits/2026-08-11-excise-absolute-mass-notion.md).

---

## 0. This is the PRIMARY coordination document for the canonical chain

This cheat-sheet is the **coordination hub for the 11-step substrate→observable
chain**, the same role [`duality-tracker.md`](duality-tracker.md) plays for the
D1–D24 dualities. Every agent working a chain step coordinates **through this
table**: it records, per step, what is **proved** (→ Lean), what is **derived**,
what is **fitted/open**, and **which sibling PR owns the gap**. Update the
relevant row when you open/land work on a step — do not fork a parallel status
doc.

**Coordination infra this plugs into** (the "good infra around this"):

| Layer | Doc | Role |
|---|---|---|
| Chain steps (this doc) | `canonical-derivation-cheat-sheet.md §0/§2` | per-step status + owner PR |
| Dualities used per step | [`duality-tracker.md`](duality-tracker.md) | D1–D24 status + closure paths |
| Per-goal ledgers | `docs/coordination/*.md` | `1ppb-categorical-chain.md`, `1ppq-qbeta.md`, `2026-05-24-low-isotope-mass-anatomy-ledger.md`, `2026-05-22-cheat-sheet-manager.md` |
| Automated watchers | `todos/{proof,canonical,compute,detangler}-*-queue.json` | integration-watcher backlog |
| Precision targets | [`precision-goals.md`](precision-goals.md) | L1 (compute) / L2 (100×) |
| **Programme map (current, 2026-09-08)** | [`audits/2026-09-08-l2-1ppq-research-program-gaps.md`](audits/2026-09-08-l2-1ppq-research-program-gaps.md) | live L2 status (1/6 scoreable, §1); per-step proved / chosen / open map for the mass chain (§2) and binding chain (§3); Q_β / c_k / f-map under D (§4); the four un-derived objects, ranked (§7.2); owner rulings of 2026-09-08 (§8) |

**Status legend.** ✅ proved (sorry-free Lean) · 🟢 derived (categorical, no fit) ·
🟡 conjecture-conditional / partial · 🔴 fitted / open gate · ⬜ not started.

### Per-step status + owner index (the coordination table)

> **Current programme map (2026-09-08):** [`audits/2026-09-08-l2-1ppq-research-program-gaps.md`](audits/2026-09-08-l2-1ppq-research-program-gaps.md) §1–§4 carries the per-step proved / chosen / open status as measured against the 2026-09-07 witnesses, and §7 the ranked gaps. The rows below are the coordination record; where a row lags that audit it carries a dated `🛑 CURRENCY` block (rows 9b and 11), prepended rather than rewritten.

| Step | What | Status | Owner gap / active PR |
|---|---|---|---|
| 1. Cat action | `ρ_n: B_n → Aut_C(V^⊗n)` | ✅ proved | — (settled) |
| 2. Stokes → Hecke | `σ_i²=(q−q⁻¹)σ_i+1` | 🟡 **algebra proved, GEOMETRY ASSERTED** — since 2026-09-06 carried as the §3b class `QOU.Mass.HeckeMonodromy`; its `q = 1` shadow (a reflection) is **derived** from the colour cubic's branch-point monodromy (`HeckeQuadraticClassicalShadow.lean`, `colour_cubic_branch_monodromy_probe.py`); plan and the real-`q` KZ prune in [`2026-09-06-step-2-plan-hecke-monodromy.md`](audits/2026-09-06-step-2-plan-hecke-monodromy.md) | the curvature 2-form is *defined* to be the Hecke quadratic (see §2a below) |
| 3. Alexander+Markov | unique `tr_M` (canonical convention D: `z_D = q³/(q²+1)`) | 🟢 derived (Lean: **0 sorries**; 2 cited external-proof **axioms** — `markov_trace_unique_axiom` in `QOU/Hecke/MarkovTrace.lean`, `jones_markov_trace_exists` in `jones-markov-trace.lean`, both `-- Ref: [jones1987]`; verified 2026-07-02) | discharge needs a cross-level M3 class field + a reduced-words basis lemma for `H_n(q)` (research-grade — uniqueness is not provable from the current generator-level class) |
| 4. Bring `χ_eu(M₀)=−6` (`g(M₀)=4`) | `6 = |S₃| = dim H₃(q)` ↔ torus knots; topological `χ_eu(M₀) = 2 − 2g(M₀) = −6` separated from sheaf `χ(M₀, 𝒱)` and rigid `dim_q` (§10.1 A); global surface Euler class `NS(A) = e(ξ) ∈ H²(𝒮, ℤ)` (#7982) | 🟢 derived | — (settled) |
| 5. Wedderburn / partitions | `H_n(q)≅⊕_λ M_{d_λ}`, `tr_M=Σ y_λ χ^λ` | 🟢 derived (Wenzl) | — (the per-block frame; everything downstream rides on it) |
| 6. Frobenius pairing + self-duality | `⟨a,b⟩_F`, `Ψ=S²=id` | ✅ proved (D3/D23) | partition-respecting audit (§9 below) |
| 7. GB filtration | `J^•`-graded, `E_1` collapse | 🟢 derived | which `J^•` is **open** — `qou-sw8n` |
| 8. Jet order | jet-prefix → `q→1` limit | 🟡 partial (Lean: **0 sorries**; `SkewSYT.lean` C1 + C2 **PROVED 2026-07-02** — C2's over-quantified `removeCorner` spec re-scoped to the witnessed row and proved, C1 `skewCorners_nonempty` proved via lex-max cell; all three `PartitionHelpers` fields now theorems ⇒ default instance **unconditional**, `Fact` crutches dropped) | residual: q-Plancherel `ConvergenceBound` (research-grade), commented-out `saturatedChainsCount` section, and the `conj:` classical-limit statement itself |
| 9a. Mass identity `m_p` | **absolute**: muon-anchored Hecke energy `m_p = 2·(m_μ·F_Bor − 6·m_e)` via the [`canonical_mass.py`](../computations/canonical_mass.py) facade (owner ruling 2026-06-24; [guardrail](canonical-mass-formula-guardrail.md)); per-knot `VolDensity(K, q₀)` retained for **binding ratios** only | 🟠 **`m_p` is an ANCHOR ROUND-TRIP, not a prediction** — `q₀` is pinned by solving exactly this form against `m_p/m_e`, so the *ratio* is reproduced **by construction**: `m_p,can/m_e = 1836.152673426000032` against the CODATA anchor `1836.152673426`, i.e. **~1.7e-17 relative**. In MeV the agreement is **2.85 ppq** (`938.2720894273242637` vs CODATA `938.27208943`). **The MeV figure cannot be checked beyond ~11 digits at all**: CODATA *quotes* 11 significant digits for both `m_e` (0.51099895069) and `m_p` (938.27208943), so past that there is nothing to compare against, whatever the working dps. The content is in the ratio, and the ratio is the calibration input. The live witness marks it `NOT SCORED` / *"the framework content cancels"*, and `mba-step09a` says so in its own text; only this status column said "settled". The genuine 9a **predictions** are `m_μ` (211.2 ppb, **970.2×** the L2 target) and `m_n` (**176.7×**). $m_n \approx 939.56$ MeV is the real one. 🟡 per-knot density wire-up still open on the **binding side**: 64 of 65 atom-touching scripts use uniform `vol_density_borromean(q)` ([`vol-usage-audit`](audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)). The old +2.89–3.86% "absolute-mass gap" is **produced by a fitted form, not a live discrepancy**: it is what `Vol(𝓑₃)·λ_A/ℏ_q²` gives, and λ_A is a CODATA-implied fit, deprecated for absolute mass by the 2026-06-24 ruling ([guardrail](canonical-mass-formula-guardrail.md)). **Do not read that as "remove the fit and the gap closes"** — the per-knot `tr_M` base gives **−57 % / −62 %**, so the true density sits between the two and neither reproduces the absolute mass. (The separate question of whether λ_A-baselined *refutations* were artifacts was re-run 2026-07-17 and measured **6 of 7 ROBUST**, 1 partial — bean `qou-sqgf`, [execution audit](audits/2026-07-17-perknot-density-rerun-execution-and-frame-reassessment.md); the 2026-06-24 [audit](audits/2026-06-24-lambda-a-refutation-artifact-audit.md) only localised the candidates.) | per-knot density wire-up (binding side; same object as the 9b ρ/Δ_λ leg per the [flip decision](audits/2026-06-13-step9a-flip-decision-package.md)); #1698 (m_avg combiner), `vol_density_per_block_wiring.py` testbed |
| 9b. Per-isotope binding `B(K)` | **bond-count × hyperbolic volume** (the honest derived core): $B = m_e\sum_n (n-1)\,\mathrm{Vol}_n(K)$ — `M_n=(n−1)` **Lean-proved sorry-free** (`LinearChainBondCount.lean`); ³H **−0.16 %**, ³He −2.97 %, zero fit; deuteron derived via the θ_λ scalar-trace collapse `m_e·Vol(𝓑₃)·Δtr` (+0.19 %) — the "two deuteron derivations" are two contractions of the ONE q-Reeb phase θ_λ ([ledger](coordination/binding-scale-is-hyperbolic-volume.md), #3748). Scale conditional on `conj:kashaev-volume-conjecture`. | **🛑 CURRENCY (2026-09-08)** — the record below stands as dated; read it with five corrections. (i) The "honest derived core" `B = m_e Σ_n (n−1) Vol_n(K)` is **census-selected, not derived**: only the multiplicity `M_n = n−1` is Lean-proved, and the producer's ³H `8.4686` / ³He `7.4889` are byte-identical to the retired `2·m_e·Vol(8₁₁)` / `2·m_e·Vol(L6a4)` census rows (`mass-table-ppb.witness.json`, `origin: hyp: census-assigned`). The 2026-09-05 owner ruling *"NO knot-selection routes allowed"* ([audit](audits/2026-09-05-binding-route-consolidation-no-knot-selection.md)) retires them, and the 2026-09-08 owner ruling (bean `qou-ales`; [audit §8](audits/2026-09-08-l2-1ppq-research-program-gaps.md)) fixes the replacement: braid words are **selected via γγ pair-production + the confinement SDP at q₀, never by census**. (ii) The live derived object is the **log functional** `B = E₀·ln(tr_M(β_free)/tr_M(β_atom))` — log is the unique multiplicative→additive map, so the functional is forced, with bond factors `b_pp = z_D`, `b_pn`, `b_nn` closed-form in q ([2026-09-05 arc synthesis](audits/2026-09-05-binding-law-arc-synthesis.md)); `B = scale·Δtr` is refuted algebraically (`Δtr/tr_free → 1` by A = 11); the identification `α·ln(·)` = energy is posited, not derived. (iii) **Both corpus assemblies are proved incapable of `b₃ > 0`** (AME `b₃ = +1.426`): the multiplicative `W = 1 − ∏f` forces `b₃ < 0` whenever `f_pn ≤ 2/3` (`QOU.MassTheory.MayerThreeBodySign`, sorry-free) and the pairwise-additive log forces `b₃ = 0`; sibling PR #7155 (open, not on `main`) adds that every edge set `atom_braid_word_3A` can express is a linear layout with no bulk. (iv) The deuteron is **non-hyperbolic** — owner ruling A, 2026-08-29 ([audit](audits/2026-08-29-deuteron-knot-owner-decision.md)): canonical braid closure, `Vol = 0`, Bloch volume leg ≡ 0 — so the θ_λ `m_e·Vol(𝓑₃)·Δtr` (+0.19 %) deuteron route below is retired. (v) Complete-graph coordination is excluded by the saturation lemma (`QOU.Mass.CoordinationSaturation`, sorry-free; [2026-08-30](audits/2026-08-30-coordination-saturation-formalized.md)). The one open problem is the extensive many-body term — `qou-brng` (todo), `qou-edt7`; "signs first": `qou-vbyi` (diproton). Programme map: [audit §3](audits/2026-09-08-l2-1ppq-research-program-gaps.md). — 🟡 partial. **The prior "NA-Stokes CKRecursion closure (sub-1ppq / 3.4 keV)" claim was ADVERSARIALLY REFUTED as presented** ([review](audits/2026-07-13-na-stokes-ck-recursion-binding-adversarial-review.md), #3723): the "SU(4) differential 1.4947 m_e" IS the measured ³H–³He split relabeled (its Lean self-marked vacuous); `r_res=2.596` ≠ the advertised invariant 5/2; `c_3=10/3` collides with canonical `c_3≈−2`. Block rewritten to honest status (#3723). Open: A≥3 per-rep θ_λ magnitude; ⁴He `Vol₄=8.05` falsifiable prediction; mirror Coulomb residual (31 % derived; pairwise EM route provably empty — Borromean). **Keystone `R(q,x)` status (2026-07-20):** the bounded-depth kernel on the raw OGF is **excluded** (Lean `QOU.Mass.QDifferenceConfluentObstruction`, sorry-free — `R(1,x)=1` forced, first-order relation fails Gevrey-1/2 growth); re-targeted on the **q-Borel carrier**, where the classical fibre is **proved** (`normalized_classical_kernel_exists`: `(n+2)·b_{n+2}=b_{n+1}+b_n`, depth 2 exact). Open: the q-lift (`[n+2]_q` relation) + prolongation-symbol identification — `conj:qdifference-kernel-prolongation-symbol` stays a conjecture. **Update (2026-07-20):** the q-lift exists exactly on the `[n]_q!`-normalized carrier (`c(q)=1`, probe-verified to 1e-45 incl. q₀ — [`qlift_kernel_candidate_crosscheck_probe`](../computations/probes/qlift_kernel_candidate_crosscheck_probe.witness.json); Lean brick in progress) and is DISTINCT from the GGM eq-49 carrier up to **arbitrary diagonal gauge, including every formal q-Borel/q-Laplace coefficient weight** (invariant `I_m = −[m]_q` vs `1/((2−q^m)(2−q^{m−1}))`; [gauge prune](audits/2026-07-20-qlift-ggm-gauge-prune.md) + [Route D](audits/2026-07-20-qlift-routeD-qborel-transform.md)) — identification open only via non-diagonal routes (Stokes matrix / analytic q-Borel–Laplace summation). | `universal-binding-architecture.md` (resolved); [`binding-scale-is-hyperbolic-volume.md`](coordination/binding-scale-is-hyperbolic-volume.md) |
| 10. Confinement SDP | canonical `T_w` | 🟢 derived | LP/SDP duals infra (`lp_dual_solver.py`) |
| 11. β-decay `Q_β` | `\|Δ(net)\|·𝔈₀` | **🛑 CURRENCY (2026-09-08)** — "🟢 derived; `c_k` truncation" is stale. The published functional solves to Markov parameter **`z = 1`, inadmissible under convention D** (`QOU/QBeta/ConventionDAdmissibleRoots.lean`, 8 theorems, sorry-free; admissible roots `z = q`, `z_D = q³/(q²+1)`; AGENTS.md scoping note 2026-09-05). **Owner decision 2026-09-08 (bean `qou-99qc`): ε := the augmentation `σ ↦ q`**, base `0.8798906` MeV, **+12.470 %** — **superseded the same day: `13bb8243d8` showed the augmentation is the Markov trace at `z = q`, and the owner then ruled ε := the Markov trace at `z_D` (−43.157 %), following D7; the augmentation is the other admissible point**; the 0.17 % form is retired as the base and citable only as the C-frame / `z = 1` historical cross-check. The scored 1279 ppb / 164.0× (`per-observable-100x-status`, 2026-09-07, stamped `INHERITED_C` + `INADMISSIBLE_FUNCTIONAL`) is convention-C and not yet re-scored on the augmentation. The C-frame ladder is **exhausted** — the greedy extraction terminates at its first rung identically, so `c₄ … c₇` are never computed (`QOU.QBeta.GreedyLadderTermination`, sorry-free) — and **no D-frame ladder exists** (`qbeta_ck_cache.py` refuses under D; `qou-cds1`; a z-swap is proved invalid by `decayLadder_zC_threeRow_ne_zero`). The ladder's N = 1 phase `α = (z−1)h/2` has **no derivation**: its carrier class is proved vacuous (`QOU.QBeta.EigenphaseCarrierVacuity`, sorry-free), bean `qou-pdix`. On the legend this row is 🔴 open (functional decided, ladder un-derived). Programme map: [audit §4](audits/2026-09-08-l2-1ppq-research-program-gaps.md). — 🟢 derived; `c_k` truncation | `ck-dk-canonical-registry.md` (rung tiers) + `1ppq-qbeta.md` ledger |

**Threads active 2026-08-10 → 09-08** (beans the 2026-09-08 audit §6.4 measured as absent from this document; one clause each): `qou-brng` (todo) — the extensive many-body binding term, the one open binding problem; `qou-k5r5` (in-progress) / `qou-o6ov` (todo) — the `M₁ > 0` first-odd-moment and Magnus-decay fronts, two ~100-commit beans that do not cite each other; `qou-cds1` (in-progress) / `qou-pdix` (in-progress) — the D-frame `c_k` ladder re-derivation and its blocker, the eigenphase; `qou-99qc` (todo) — the Q_β functional, ε decided as the augmentation 2026-09-08, rows not yet re-scored; `qou-aemx` (in-progress) — the two rival α_em derivations 470 ppb apart; `qou-auq3` (completed) / `qou-phir` (todo) / `qou-kwoa` (in-progress) — the Hecke / TL Lean foundations (GS basis, `H_n(q)` as field-algebra, Hecke character theory); `qou-ales` (todo) — the 2026-09-08 braid-word-selection ruling.

**The frontier is step 9** (everything else is settled or proof-cleanup).
**Absolute nucleon mass is SETTLED (owner ruling 2026-06-24)** via the
muon-anchored [`canonical_mass.py`](../computations/canonical_mass.py) facade
($m_p \approx 938.27$ MeV, CODATA;
[guardrail](canonical-mass-formula-guardrail.md)); the old vol-density
absolute-mass gap (+2.89–3.86%) is produced by a fitted form — `Vol(𝓑₃)·λ_A/ℏ_q²`
with λ_A a CODATA-implied fit — and is not a live discrepancy
([guardrail](canonical-mass-formula-guardrail.md)); removing the fit does not
close it (per-knot gives −57 %). Two gaps
remain, both **binding-side**: **9a** = per-knot `VolDensity(K, q₀)` wire-up
(valid where the scale cancels; 64 of 65 atom-touching scripts still uniform
per [`vol-usage-audit`](audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md));
**9b** = the **Δ_λ** per-block density (the Track-A blocker).

> **📌 Single narrative source for the step-9 frontier: §9.** Full detail —
> the 9b `q₀^(10A−5)` residual (derive-or-refute), the 2026-06-13 9a flip
> gate (`R(K)` 2.3→63×; do not re-litigate), the intensive-vs-extensive
> reframing, and the many-body series — lives in **§9 only**. Update §9 and
> keep this paragraph + §5 item 1 as pointers. (Restructure 2026-07-02,
> PR #3200: three drifting copies of this narrative caused the staleness
> that PR fixed.)

> **Brane-tower convergence law + Borromean single pipeline (2026-06-28, PR
> #3016 / bean `km42`).** The per-braid brane tower (`prop:per-braid-mass-tower`,
> Li₂^q form) **converges iff the nucleon trace `< 1`**. The colour-weighted
> **atom-word** proton has `tr_p = 1.0653 > 1`, so the free pp pair `tr_p² =
> 1.135 > q₀` exceeds the Li₂^q radius and the tower **diverges for Z ≥ 2** (the
> same divergence class as the superseded per-generator form — formalize-first
> *refuted* the standing `|tr_M(ξ)| < q` premise, counterexample exact at ⁴He
> H₁₂). The **Borromean** nucleon `τ = |tr_M(β_Bor)| = (4+h²−3h⁴−h⁶)/(h²+4) =
> 0.9986 < 1` (Lean `BorromeanMarkovTrace`) makes every free pair `< q₀` ⇒
> **converges ∀Z**. This is the *single pipeline* (no special-casing): nucleon
> mass (`F_Bor`, bean `ovud`) and per-isotope binding both flow from the one `τ`
> ([`borromean_binding_recompute.py`](../computations/borromean_binding_recompute.py)).
> **It is the per-knot answer to "why Bor"**: `β_Bor` is the *nucleon's own knot*
> (a baryon **is** `𝓑₃(3 colour tubes)`; Borromean = confinement), the A=1
> instance of the per-knot rule — *not* a global assumption (that bug is the 9a
> uniform-`Vol(𝓑₃)`). **Result:** converges ∀Z, right *shape* (binding grows with
> pair count: ¹⁶O err 31×→2.3×), **wrong normalization** (under-binds mid-mass,
> over-binds ⁵⁶Fe) — i.e. the missing **Δ_λ** per-partition weight (the tower
> applies a uniform `E₀` where `B = m_e·Σ_λ y_λ χ^λ Δ_λ` carries a per-λ weight).
> Conventions derived from the categorical action (`g(x)=−Li₂^q(−x)` bar-even
> channel; A=2 pair included). Full record:
> [`formalize-first plan`](audits/2026-06-28-brane-tower-formalize-first-plan.md),
> [`higher-order finding`](audits/2026-06-28-brane-tower-higher-order-deuteron.md).
> Cross-link #2985 (binding correction tower is not a single low-order
> q-hypergeometric element — consistent; no single-element closure).

> ## ⚠ Critical framing — do NOT treat `λ_scale` as a separate object
>
> **`λ_scale` was ABSORBED into `VolDensity(K)` on 2026-05-23 (commit ffdd84409).** The numerical factor that older docs call `λ_scale` is *what the canonical `VolDensity(K)` evaluation produces per knot/link*. It is **not** a separate constant to derive, calibrate, or "close". There is **one** canonical mass formula:
>
> ```
> m(K) = m_e × VolDensity(K, q₀)
> ```
>
> per `conj:geom-universality`. `VolDensity` is **knot-dependent** — each atom's canonical K (proton 𝓑₃, deuteron β_D via `atom_braid_word_3A(1,1)`, etc.) gets its own `VolDensity(K, q₀)` evaluation. For the proton specifically, `VolDensity(𝓑₃, q₀)` factors as `(Vol(𝓑₃)/ℏ_q²) · linking_weight(q)` — but the linking weight is **part of Geom**, not separate. The current categorical computation gives m_p ≈ 965 MeV (+2.89%); the open R&D is **per-knot wire-up of `VolDensity(K)` across all atoms** (production uses `vol_density_borromean(q)` uniformly for ALL atoms — the Vol-uniform bug per [`vol-usage-audit`](audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)), not "refining `VolDensity(𝓑₃)`" alone. The Yekutieli per-cell route was briefly tried in production then PURGED 2026-05-24 (71d674da1) as non-canonical.
>
> See [`lambda-scale-absorbed-into-vol-density.md`](lambda-scale-absorbed-into-vol-density.md) for the canonical reference, including the numerical demonstration that no standard invariant produces 2.46 directly and the full list of refuted alternative derivations.
>
> Original numerical discussion: [`coordination/2026-05-23-algebraic-geometric-observable-consistency.md`](coordination/2026-05-23-algebraic-geometric-observable-consistency.md) §"λ_scale is NOT a separate object — it's what VolDensity produces".
>
> Agents recurrently rediscover and re-frame "λ_scale closure" as if it were the open problem — it is not. The problem is per-knot `VolDensity` refinement.

> ## 🛑 CORRECTION (owner ruling 2026-06-24) — the block above is SUPERSEDED for ABSOLUTE mass
>
> Read with `K = 𝓑₃`, `m(K) = m_e × VolDensity(K, q₀)` is the **wrong absolute-mass form**: it applies `1/ℏ_q²` to the Borromean volume and yields $m_p \approx 966$ MeV (+2.96%; the λ_A linking weight is a CODATA-implied **fit**) or $\approx 406$ MeV (−57%, naive tr_M). *(Figure note: 966.05 MeV / +2.96% is the exact flip-decision-witness value; older passages in this doc quote the rounded 965 MeV / +2.89% — same λ_A artifact, trust the witness figure.)* The canonical absolute nucleon mass is the **muon-anchored Hecke energy**
>
> ```
> m_p = 2·(m_μ·F_Bor − 6·m_e),   m_μ = m_e·Vol(4₁)/ℏ_q²,   F_Bor = |tr_M(β_Bor)|·[3]_q!/q³
>     → m_p ≈ 938.27 MeV, m_n ≈ 939.56 MeV  (CODATA)
> ```
>
> — the `c_q² = 1/ℏ_q²` belongs in the **muon** anchor `Vol(4₁)`, then dressed by the *dimensionless* `F_Bor`. Route every absolute nucleon/atom mass through the [`canonical_mass.py`](../computations/canonical_mass.py) facade. `vol_density_borromean` / `mass_vol_density` / `linking_weight_family_a` (λ_A) are **deprecated for absolute mass** (emit `DeprecationWarning`); `vol_density_per_block` stays valid for **binding ratios only** (the scale cancels). The per-knot `VolDensity(K)` framing above survives as the **binding-side** per-knot density question (the 9b ρ/Δ_λ leg). Read first: [`canonical-mass-formula-guardrail.md`](canonical-mass-formula-guardrail.md); λ_A excision: [`coordination/2026-06-24-lambda-a-fit-excised-per-knot-density.md`](coordination/2026-06-24-lambda-a-fit-excised-per-knot-density.md).

### 0.1 Notation Disambiguation Table (`qou-6tdg` currency pass, 2026-09-15)

To prevent symbol conflation across §§1–10 (enacted in PR #7426 and #7982; see §10.1 Decisions A–D and [`notation/notation-collisions.md`](../folio/quantum-observable-universe/notation/notation-collisions.md)), the following symbols are strictly separated throughout the corpus:

| Symbol | Name & Domain | Canonical Definition / Value | Where Formalized / Audited |
|---|---|---|---|
| $\chi^\lambda$ (or $\chi_\lambda$) | **Hecke irreducible character** on $H_n(q)$ ($\lambda \vdash n$) | $\chi^\lambda(T_w) = \operatorname{tr}\bigl(\rho_\lambda(T_w)\bigr) \in \mathbb{Q}(q)$ on the Hoefsmit seminormal module $V_\lambda$ of dimension $d_\lambda = f^\lambda$ | `computations/hecke/hecke_characters.py`, `QOU/Machinery/DerivedCharacterCatalogue.lean` |
| $\chi_{\mathrm{eu}}(M_0)$ | **Topological Euler characteristic** of Bring's curve $M_0$ | $\chi_{\mathrm{eu}}(M_0) = 2 - 2g(M_0) = -6$, where $g(M_0) = 4$ is the Descartes genus condition (alternating sum of Hochschild homology of $M_0$) | `rem:three-euler-characteristics`, `lem:brings-euler-characteristic`, `QOU/Information/EulerCharacteristicOfHochschild.lean` (`hhEuler_bring = -6`) |
| $\chi(M_0, \mathcal{V})$ | **Holomorphic sheaf Euler characteristic** on $M_0$ | $\chi(M_0, \mathcal{V}) = h^0(M_0, \mathcal{V}) - h^1(M_0, \mathcal{V}) = \deg \mathcal{V} + \operatorname{rk}\mathcal{V}\cdot(1 - g(M_0))$ (Riemann–Roch) | `rem:chern-character-and-riemann-roch`, `notation/notation-collisions.md` |
| $\operatorname{tr}$ | **Ordinary matrix / vector-space trace** | Standard linear-algebraic trace $\operatorname{tr} : \operatorname{End}_k(V) \to k$ on a finite-dimensional module or Wedderburn block $M_{d_\lambda}$ | `rem:trace-ledger` |
| $\operatorname{tr}_M$ | **Normalized Markov trace** on $H_n(q)$ | $\operatorname{tr}_M(\beta) = \sum_{\lambda \vdash n} y_\lambda(q)\,\chi^\lambda(\beta)$ with $\operatorname{tr}_M(1) = 1$; under canonical **convention D**, the single-generator Markov parameter is $z_D = \frac{q^3}{q^2+1}$ (excising convention C's $z_C = \frac{1}{q^{1/2}+q^{-1/2}}$) | `QOU/Hecke/MarkovTrace.lean`, `QOU/QBeta/ConventionDAdmissibleRoots.lean`, `rem:categorical-trace-is-the-markov-trace` |
| $\dim_q(X)$ | **Quantum / categorical rigid dimension** | $\dim_q(X) = \operatorname{tr}_C(\mathrm{id}_X) = (\mathrm{ev} \circ \mathrm{ch})([X])$, $q$-dependent and positive on simple objects (e.g. $\dim_q(V_m) = [m+1]_q$; for the regular representation $\mathcal{O}_q(\mathrm{SU}(2))$, $\sum [m]_q^2$ is divergent — §10.1 D) | `QOU/GrothendieckChern.lean` (`dimQK0_eq_evDimQ_chernCharacter`), `QOU/Information/DimqRegularisationIdentities.lean` |
| $\mathrm{NS}(A) = e(\xi)$ | **Global surface Néron–Severi / contact Euler class** | $\mathrm{NS}(A) = e(\xi) \in H^2(\mathcal{S}, \mathbb{Z})$ on the global surface $\mathcal{S}$ (#7982), paired with the Wigner obstruction class $w(A)$ (`conj:wigner-axiom`, $\dim \mathrm{Obs} = 1$) | `QOU/AlgebraicSubstrate/WignerAxiom.lean`, `QOU/Brings/WignerTargetEquivariance.lean`, PR #7982 |
| $q_0$ (proton pin) | **Canonical archimedean substrate pin** | $q_0 = 1.10997858275138080759\dots$ (50-dps proton pin from $m_p/m_e$ via `substrate.q_parameter.Q_50_DIGIT_STR`; owner directive 2026-08-15 retires frozen muon literals) | `computations/substrate/q_parameter.py`, bean `qou-1c4y` |
| $\beta_{\mathrm{Bor}}$ | **Canonical Borromean intra-nucleon braid word** | Alternating 3-strand closure $\beta_{\mathrm{Bor}} = (\sigma_1 \sigma_2^{-1})^3 \in B_3$ with $\operatorname{tr}_M(\beta_{\mathrm{Bor}}) = \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4}$ | `QOU/BraidKnot/BorromeanMarkovTrace.lean` |

---

## 1. The chain in one diagram

```
            ┌──────────────────────────────────────────────┐
            │  3 weak-sector calibration inputs (only)     │
            │   m_e ──── leptonic mass scale (CAL-1, h⁰)   │
            │   P_skew^β ──── neutron β-sector bar-skew channel (CAL-2, h²)  │
            │   P_avg^π ──── pion-sector bar-even channel (CAL-3, h³)       │
            │   proxies: m_e, m_μ/m_e (Q_β=P_skew^β), m_π     │
            └──────────────────────────────────────────────┘
            (phys-obs precision anchor: q_0 on m_p/m_e via Q_50_DIGIT_STR, re-pin 2026-05-28; owner directive 2026-08-15)
                            │
   step 1. Cat action  ↓  ρ_n : B_n → Aut_𝐂(V^⊗n) via R-matrix
                            │
   step 2. Stokes (Yekutieli)  ↓  σ_i² = (q − q⁻¹)σ_i + 1
                            │           (monodromy quadratic of a flat connection ⇒ Hecke relation)
                            ▼
                       𝐇_n(q)  ─── Iwahori-Hecke algebra
                            │
   step 3. Alexander+Markov  ↓  knot ⇄ braid closure, unique trace tr_M (convention D: z_D = q³/(q²+1))
                            │
   step 4. Bring χ_eu(M₀)=−6  ↓  6 basis elements ↔ 6 torus knots ↔ particle content (g(M₀)=4; NS(A)=e(ξ))
                            │
   step 5. Wedderburn  ↓  𝐇_n(q) ≅ ⊕_{λ⊢n} M_{d_λ}(ℚ(q)),  Σ-rep over partitions
                            │
   step 6. Frobenius pairing  ↓  ⟨a,b⟩_F = ∫_A(a·b);  𝔪 = |∫_A ρ(β)| = |tr_M(𝓑_K)|
                            │
                            │  Markov-trace formula (Wenzl bridge):
                            │     tr_M(β) = Σ_λ y_λ(q) · χ^λ(β)
                            │           ↑           ↑
                            │     Wenzl weights    Hecke characters
                            │     (uniquely         (Hoefsmit
                            │      determined)      seminormal)
                            ▼
   step 7–8. GB-NF / jet  ↓  E_∞ = ⊕_λ M_{d_λ}(ℚ(q)); collapse at E_1 ⇒ finite-slice
                            │
                            ▼  T_w canonical, GB-NF ground truth
                            │
   step 9. Archimedean realization  ↓  τ : 𝐂 → Vec_ℝ at q = q_0
                            │
                            ▼
        B(𝔥) = m_e · ρ · [|tr_M(T_w)| + tower(T_w) + tr_M(C_{dim_q})] |_{q=q_0}
                            │
   step 10. Confinement SDP  ↓  selects canonical T_w
                            │
   step 11. β-decay Q  ↓  Q_β = |Δ(net(T_w))| · 𝔈₀
                            │
                            ▼
                    OBSERVABLES (MeV):
                    m_p, m_n, m_He, B_AME(K), Q_β, half-lives
```

Every arrow lives in $\mathbb{Q}(q)$ until the Archimedean functor in step 9. No fitting, no empirical nuclear-physics constants, no analytic limits in the pre-Archimedean chain.

### §3a — what step 3's closure does (cups, caps, and two separate steps)

*Added 2026-11-16 (issue #8133). The math below is classical or already in the
corpus; the Lean (`QOU/BraidsAndKnots/ClosureUnseen.lean`, sorry-free) is on the same branch and is
**not** yet merged. Exact checks: `/mnt/project-files/qou-braid-closure/closure_probe.py`.*

Step 3 writes "knot ⇄ braid closure, unique trace `tr_M`". Closure adds **no crossing**. It
adds a coevaluation (cup) below every strand and an evaluation (cap) above it. Observation in
the corpus *inserts* a crossing (`measurement-observation/observation-braid.md`), so closure is
not observation.

- **Cups and caps as entangled pairs.** `coev(1) = Σᵢ eᵢ ⊗ eⁱ` is the maximally entangled vector;
  with the pivotal weight `K = diag(q, q⁻¹)` it is the q-weighted Bell vector `Ω_K`, and
  `Tr_q(β) = ⟨Ω_K | (β ⊗ 1) | Ω_K⟩`. Read: the cups prepare `n` entangled pairs, `β` acts on one
  half, and the caps project back onto the pairs. Every map here lives in `ℚ(q)`; nothing is
  archimedean yet.
- **Two steps, which "closure" runs together.**
  1. *Annular closure* (keep the axis): `H_n → HH₀(H_n) = H_n/[H_n, H_n]` ≅ the annular skein,
     basis `Q_λ`. It keeps **every** character `χ_λ` separately.
  2. *Forget the axis* (embed in S³): `Q_λ ↦ dim_q`, giving
     `tr_M^{z_D} = Σ_k [n−2k+1]/[2]ⁿ · χ_(n−k,k)` — already proved as
     `rem:categorical-trace-is-the-markov-trace` (`qtrace_rHecke_div`).
- **What closure cannot see.** Two braid elements have the same value under every trace iff
  their difference lies in the commutator span `[H_n, H_n]`. So an emitted-and-reabsorbed
  subword `y·w·y⁻¹` is invisible to every closure; that is the precise meaning of an
  intermediate that is "produced and not seen" (no virtual particles needed). Exact check: 340
  cases in `B₃`.
- **Relation to the guiding principle below** ("preserve information until observation").
  Step 1 keeps the per-λ data; **step 2 is the collapse that principle warns about**, because it
  averages the sectors with weights `p_k = [n−2k+1] f_(n−k,k)/[2]ⁿ` (positive, summing to 1) and
  happens before `τ`. So "cup/cap = projection onto the observable" is accurate for step 2
  followed by `τ`; the cups and caps by themselves only project onto conjugation-invariant data.

**Where closure enters the Navier–Stokes / fluid chapter.** `fluid-dynamics/braid-fluid.md`
("Helicity as Markov trace") and `fluid-dynamics/helicity-conservation.md` (item 3) use
`J_L(q) = tr_M(ρ(β_L))` for the vortex tangle, so they use step 3, but neither says which arcs
close the vortex strands. The classical counterpart is Arnold's asymptotic linking number:
orbit segments of a volume-preserving field are closed by **short paths**, and the closing arcs
drop out of the helicity in the limit `T → ∞` (stated with proof references in
`[komendarczyk2008]` §2, held at `library/arxiv-0808.1533v3/`). This is the fluid version of
"the return arcs are unseen". Both blocks now say so explicitly. The Lean twin of
`prop:helicity-conservation` encodes md part (3) in three cases: under **isotopy** (frozen-in
vortex lines, then Markov's theorem: a path of conjugations and stabilisations) the normalised
Jones value is conserved (`jones_normalised_conserved`); with a **fixed axis** (conjugation only)
the finer annular class is conserved (`annular_class_conserved`); across a **reconnection** every
closure invariant jumps by exactly `h` times its value on the smoothed word (`reconnection_jump`).
The frozen-in and Markov inputs are cited, not proved. Reading the periodic direction of a periodic-box flow as the closure axis
(so that step 1 survives there) is an interpretation, not a derivation.

---

## 2. Step-by-step: math + reference + compute script

| Step | Math | Key prop / paper ref | Canonical compute script | Witness |
|---|---|---|---|---|
| **1. Cat action** | $\rho_n: B_n \to \mathrm{Aut}_\mathbf{C}(V^{\otimes n})$ via R-matrix | `prop:braid-action-tensor` | `substrate/hecke_core.py` (σ_i seminormal matrices) | — |
| **2. Non-abelian Stokes** | Hecke quadratic $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ as curvature 2-form | ⚠ `prop:hecke-spectral-sequence` **DOES NOT EXIST** (0 `label:` declarations in `content/`; the only hits are two Lean docstrings and this file) — [yekutieli2015] | `substrate/hecke_core.py`, `hecke/hecke_character_symbolic.py` (Hoefsmit + Hecke) | — |

> ### §2a — what Step 2 actually proves, and what it assumes
>
> **Downgraded from "✅ proved" 2026-08-25** (PR #5765). The distinction matters because
> this is the **only bridge from the categorical/geometric substrate to `H_n(q)`**, and
> steps 3–11 and every number in the framework ride on it.
>
> **What is proved.** `QOU.Mass.HeckeStokes.stokes_curvature_factors`
> ([`HeckeStokesEigenvalues.lean:38`](../folio/quantum-observable-universe/lean/QOU/Mass/HeckeStokesEigenvalues.lean))
> is real and useful — but it is a **factorisation identity over a generic field**:
>
> ```lean
> theorem stokes_curvature_factors (q : K) (hq : q ≠ 0) (X : K) :
>     X ^ 2 - (q - q⁻¹) * X - 1 = (X - q) * (X + q⁻¹) := by
>   field_simp
>   ring
> ```
>
> It establishes that the polynomial's roots are `λ₊ = q` and `λ₋ = −q⁻¹`, which is what
> the downstream bar-evenness of `τ` is inherited from
> (`quantum_dim_is_eigenvalue_gap`). That part is sound and is not in question.
>
> **What is assumed.** That the polynomial *is the curvature 2-form*. There is no
> connection, no curvature form, no surface and no multiplicative integral in that file.
> The interpretation lives in a **docstring** in
> [`NaStokesKeystone.lean:22`](../folio/quantum-observable-universe/lean/QOU/Mass/NaStokesKeystone.lean):
>
> > *"The abelianised Cartan connection on the exceptional divisor `S_c` **has** curvature
> > 2-form `F(σ) = σ² − (q − q⁻¹)σ − 1`. Flatness `F = 0` derives the Hecke quadratic."*
>
> The 2-form is **stipulated** to be the Hecke quadratic, so setting it to zero recovers
> it **tautologically**. Nothing computes a curvature that *turns out* to be this
> polynomial. The appendix's own Step-2 block is consistent with this: the braiding obeys
> the Hecke relation because `def:categorical-action` says so.
>
> **And the citation does not resolve.** Both Lean files attribute the geometry to
> `prop:hecke-spectral-sequence`; corpus-grep finds **0 `label:` declarations** for it in
> `content/` — the only occurrences are those two docstrings and this document. The
> 2026-07-05 currency audit cleared "all 14 §2 step-table paper labels" by **stem**-grep;
> two of its fourteen do not resolve by label, so it is not clearance.
>
>
> **Update 2026-10-11 (owner pick "Derive it"): the polynomial is not a curvature at all.**
> `F(σ)` is the eigenvalue relation satisfied by the exchange monodromy of a **flat**
> connection; a curved connection has path-dependent holonomy and gives no braid
> representation. For the 𝔰𝔩₂ Knizhnik–Zamolodchikov connection on two points it is now
> **derived** from the Casimir eigenvalues `½` / `−3/2`:
> `QOU.Mass.KohnoTwoPoint.kzExchange_quad` (`β² = (q − q⁻¹)β + 1`, `q = e^c`) and
> `kzExchange_shadow_involution` (at `q = 1` the exchange is the flip), both sorry-free. Flatness
> of the 𝔰𝔩₂ KZ connection ⇔ the infinitesimal pure braid relations is proved for 3 points in
> `mass-endomorphism/kz-connection-sl2.lean`. Still open: the braid relation for `n ≥ 3`
> (holonomy on configuration space, bean `qou-9634`), and whether the substrate connection *is*
> KZ (bean `qou-d0qq`; as the corpus stands it is not). The declaration name
> `stokes_curvature_factors` keeps the historical word.
>
> This is AGENTS.md §"Derive-then-check" item 8 verbatim: *if it is true by unfolding or
> by `ring`, it is notation, not a theorem.*
>
> **Scope (a).** The current formalisation does not derive the geometry→algebra step. This
> does **not** exclude a genuine Yekutieli derivation existing or being found — no
> invariant forbids it. To close it, Step 2 needs either a real multiplicative-integral
> construction whose curvature is *computed* to be `σ² − (q−q⁻¹)σ − 1`, or an honest
> restatement as a §3b conjecture class with the geometric step as its hypothesis.
>
> **In fairness to `NaStokesKeystone.lean`:** that file is explicit that its *own* open
> core is the geometric `period = lw` equality, and it states the τ assembly is
> conditional on it. What was wrong was this document's status column, not that file's
> self-description.

| **3. Alexander+Markov** | Unique trace $\mathrm{tr}_M$ invariant under braid + stabilization moves (canonical convention D: $z_D = q^3/(q^2+1)$); $J_K(q) = \mathrm{tr}_M(\beta)$ | `thm:jones-markov-trace`, [jones1987] | `hecke/hecke_characters.chi_lambda_braid`; `pyhecke_native` (Rust) | per-witness. $\mathrm{tr}_M(\beta_{\mathrm{Bor}})$ closed form **Lean-proved** (`BorromeanMarkovTrace.lean`, modulo cited $V$). **Cross-method checkpoint:** the *narrative-only* per-rep $\chi^\lambda(\beta_{\mathrm{Bor}})$ ($\chi^{(3)}{=}\chi^{(1^3)}{=}1$, $\chi^{(2,1)}{=}2{-}3h^4{-}h^6$) confirmed numerically to $\le 4\mathrm{e}{-}50$ by the skein-validated seminormal engine (`borromean-chi-independent-crosscheck`; proof-status audit [`2026-06-07`](audits/2026-06-07-borromean-chi-crossmethod-proof-status.md)) |
| **4. Bring $\chi_{\mathrm{eu}}(M_0)=-6$** | $\dim H_3(q) = 6 = $ # embeddable torus knots in $\Sigma_4$ ($g(M_0)=4$, $\chi_{\mathrm{eu}}(M_0) = 2-2g(M_0) = -6$, separated from sheaf $\chi(M_0,\mathcal{V})$ and rigid $\dim_q$ per §0.1 / §10.1 A; global surface $\mathrm{NS}(A)=e(\xi)$); particle content fixed | `prop:x5-bring-weight-identification`, `prop:spectral-sequence-h3-explicit`, `rem:three-euler-characteristics` | `hecke_core._PROTON_G0/G1`, `_NEUTRON_G0/G1` (canonical H_3 chains) | — |
| **5. Wedderburn + partitions** | $H_n(q) \cong \bigoplus_{\lambda \vdash n} M_{d_\lambda}(\mathbb{Q}(q))$; $\mathrm{tr}_M = \sum y_\lambda \chi^\lambda$ | `prop:alpha-k-derivation-procedure`, [wenzl1988] §1 | `y_lambda_wenzl_bridge.py` (numeric + symbolic); **3-axis (K, λ, A) derived-χ catalogue** [`derived_chi_catalogue_sweep.py`](../computations/derived_chi_catalogue_sweep.py) (PR #1952) — pre-emits $\chi^\lambda(\beta_K)(q)$ as exact q-Laurent for every production atom × every partition; backed by `pyhecke_native.chi_q_via_gp` (Rust Geck-Pfeiffer, GIL-released v0.9.0) | `y-lambda-at-q0.witness.json`; `derived-chi-catalogue.witness.json` |
| **6. Frobenius pairing** | $\langle a, b \rangle_F = \int_A(a \cdot b)$; $\Psi = S^2 = \mathrm{id}_A$ (symmetric); chirality $a_K = 1 + w(K)·h + O(h^2)$ | `def:frobenius-hopf-substrate`, `prop:chirality-writhe-ribbon-derivation` | `chi_lambda_braid` + `tau_M_*` family | various |
| **7. GB filtration** | Filtration $J^\bullet(q)$; spectral sequence collapses at $E_1$. **🛑 Corrected 2026-09-14 on owner instruction — this row disagreed with both carriers it cites.** It read *"Filtration by Coxeter length $\ell(w)$ … collapses at $E_2$"*. (a) **Page:** `prop:spectral-sequence-collapse` says $E_1$ in its own first line, and $E_1$ collapse is *strictly stronger*, so the row **understated its own carrier** — a direction that reads as a weaker result rather than an error, so nothing flagged it. (b) **Filtration:** the Coxeter-length reading is excluded at **every** $n \geq 2$ (`QOU.BraidKnot.shift_cannot_fill_a_gap`, sorry-free; [audit](audits/2026-08-26-no-shift-rescues-the-word-partition-bridge.md)), as are the ideal-power and rewrite-depth readings ([audit](audits/2026-08-16-three-gb-filtrations-one-name.md)) and the whole GS-definable class ([audit](audits/2026-08-26-the-unit-coefficient-excludes-gs-definable-filtrations.md)). Meanwhile `prop:gb-spectral-sequence` itself cites a **fourth** object — the *confinement* filtration of `def:confinement-level`, indexed by Wedderburn-block energy — which no audit has examined and which evades both exclusion routes (its unit sits at the **top**, and it is block-indexed rather than monomial in $\{T_w\}$). **So which $J^\bullet$ this row means is OPEN: bean `qou-sw8n`.** The decisive test is to compute $E(\lambda, q_0)$ — the confinement-LP duals, i.e. **step 10** — and compare its strata to `gbDepth`'s. | `prop:gb-spectral-sequence`, `prop:spectral-sequence-collapse` | `derivation_chain.py` (GB-NF tracker) | per-chain |
| **8. Jet order** | Slice-traversal order = jet-prefix partial order; jet tower → classical limit at $q \to 1$ | `conj:jet-convergence-classical-limit` (conjecture, not prop — corpus kind) | `derivation_chain.py` (jet-order log) | — |
| **9. Mass identity** | $\mathfrak{E}_0 = m_e/(q_0(q_0-1)) = m_e c_q^2 \hbar_q$ (lept); $\mathfrak{E}_0 = Q_\beta/|h(h-2)/2|$ (had). $B(K) = m_e ρ \cdot [|\mathrm{tr}_M| + \text{tower} + \mathrm{tr}_M(C_{\dim_q})]$ | `prop:atom-knot-mass-derivation` | **absolute mass**: [`canonical_mass.py`](../computations/canonical_mass.py) facade (muon-anchored, owner ruling 2026-06-24; producer `m_p_substrate_identity_50dps.py`). Legacy vol-density scripts (`mass_table_ppb.py`, `m_p_borromean_verification_50dps.py`, `mass_formula_6term_mpfr_50dps.py`) **deprecated for absolute mass** ([guardrail](canonical-mass-formula-guardrail.md)) | `m-p-substrate-identity-50dps.witness.json`; legacy `mass-table-ppb.witness.json` |
| **10. Confinement SDP** | $T_w$ canonical from joint mass-tower SDP; $\min \|\mathrm{tr}_M(T_w) \mathfrak{E}_0 - B_\mathrm{tgt}\|$ over GB-NF | `prop:confinement-sdp`, `conj:canonical-knot-id-sdp` | `lp_dual_solver.py` (`solve_operator_selection_lp`) | `operator-selection-lp.witness.json` |
| **11. β-decay Q** | $Q_{\beta^-} = [\mathrm{net}(T_w^H) - \mathrm{net}(T_w^{H'})] · \mathfrak{E}_0$; free neutron: $\Delta(\mathrm{net}) = h(h-2)/2 \approx -0.1872071945$ | `prop:neutron-qvalue-symbolic` | `free-neutron-decay.py`, `qbeta_*.py` | `q-beta-*.witness.json` |

---

## 3. Phase 5 findings — what's settled vs open

| Phase | Finding | Status | Impact |
|---|---|---|---|
| **5b** | $\alpha \approx [3]_q^2 \cdot \cosh(h)$ at single-block $|\Delta_\lambda^*|$ level (0.022 % rel.err. at $q_0$) | conjecture, §3b-cond axiomatized | Z-step factor at single-block level |
| **5c.1** | Interface knot factor: $\mathrm{tr}_M(\mathcal{B}_K) / \mathrm{tr}_M(\mathcal{B}_K^{\mathrm{vac}}) = z^{p_+(K)} \cdot (z-h)^{p_-(K)}$ exactly (with $z = z_D = q^3/(q^2+1)$ under canonical convention D; historically recorded at $z_C = 1/(q^{1/2}+q^{-1/2})$) | **PROVED sorry-free** in PR #819 | exact closed form for interface contribution |
| **5g** | Constit-side per-Z step matches $(2q - 1)$ to 0.033 % at $q_0$ | **falsified globally** (PR #842 / #854) — coincidence, not identity | bridge to 5l |
| **5k.1** | Residual against $(2q-1)$ matches $h^5(q_0)$ with c≈1.016 | **falsified globally** (PR #854) — numerical accident at $q_0$ | bridge to 5l |
| **5l** | $\rho_Z^{\mathrm{constit}}(q) = \mathrm{tr}_M^3(\mathcal{B}_p, q)$ exactly | **STRUCTURAL IDENTITY** (PR #854) — mpfr-50-dps precision; derivable from Wenzl §1.7 disjoint multiplicativity | constit-side closure |
| **5l.1** | Closed-form Laurent rationals for $\chi^\lambda(\mathcal{B}_p, q)$ for $\lambda \vdash 3$ | clean χ^λ closed forms (PR #854); y_λ normalization reconciliation queued as 5l.2 | partial closed form for $\mathrm{tr}_M^3(\mathcal{B}_p)$ |
| **5n** | Comprehensive notation refactor: $\beta_K \to \mathcal{B}_K$, $\Delta_I^K \to \bowtie_K$, $\mathbf{E} \to \mathfrak{E}$, $\mathcal{B}(q) \to \mathfrak{B}(q)$, $\tau_M \to \mathrm{tr}_M$ | **MERGED** (PR #853) — register expansions: cal admits Hecke structurals; fraktur admits energies | notation discipline |
| **5o** | Functor disambiguation — $\tau$ (fibre, $\mathbf{C} \to \mathbf{Arch}$) vs $U$ (forgetful, $\mathbf{Arch} \to \mathbf{Vec}_\mathbb{R}$) vs $R \mapsto \mathbb{R}$ realisation (base-ring substitution, not a categorical functor) | doc note added to `notation-collisions.md` | terminology discipline |
| **5q** | Closed-form $\mathrm{tr}_M(\mathcal{B}_K)$ shared utility (`closed_form_tau_M.py`) for production migration; combines Phase 5c.1 + 5l | new branch `claude/phase-5q-pipeline-discipline`; verification witness in progress | unblocks cheat-sheet §5 action #4 |
| **Bind** | A≥3 binding deficit is the **linear truncation** of the boundary holonomy: the scalar Δtr collapses the per-rep **q-Reeb phase** $\theta_\lambda$; binding is carried by $\theta_\lambda$ (Markov-weighted), closing the **A=3 mirror pair (³H, ³He) to 2% with no fit**. μ₀ = m_e/(3(q−q⁻¹)/2) ≈ 1.63 MeV **derived**; q-Hamiltonian rotational energy μ₀·ℏ_q·J_q²(j=n/2) reproduces **B_D to −9% with 0 free params**, A≥3 keeps the per-rep deficit | per-λ "closure" retracted as a C_knot fit; gate is the A≥3 per-rep structure, NOT the scale (PR #1417) | deuteron derived twice; A≥3 narrowed to one structural item |

**Combined Z-step factor at full tr_M level (post-5l + 5c.1):**

$$\frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})} \;=\; z(q) \cdot \mathrm{tr}_M^3(\mathcal{B}_p, q)$$

— exact, no residuals. (`z_D = q^3/(q^2 + 1)` under canonical **convention D**, per 2026-08-15 owner ruling R1; historical Phase-5 record used convention C's `z_C = 1/(q^{1/2} + q^{-1/2})` from the C-frame Markov normalization; `tr_M^3(B_p)` from Wenzl disjoint multiplicativity.)

> **🛑 CONVENTION LABEL (added 2026-09-15, bean `qou-6tdg`):** the `z` in the line above is `√q/(q+1)`, **convention C**. The 2026-08-15 owner ruling (R1) makes convention D, `z_D = q³/(q²+1)`, canonical and excises C; the Phase-5 identities in this section are correct **for C** and are kept as recorded — they need scoping, not correction (AGENTS.md, the `c_k` banner and §R1). Under D the Z-step factor is `z_D · tr_M^3(𝓑_p, q)` with the D-frame traces, which the live producers (`bond_factors_are_z_plus_d_probe`, `binding_canonical`) already use; `rem:categorical-trace-is-the-markov-trace` identifies `z_D` as the normalised rigid trace of one generator. Do not substitute `z_D` into a C-frame identity by hand (`decayLadder_zC_threeRow_ne_zero`).

**Full closed-form $\mathrm{tr}_M(\mathcal{B}_K)$ (Phase 5q):**

$$\mathrm{tr}_M(\mathcal{B}_K) \;=\; \mathrm{tr}_M^3(\mathcal{B}_p, q)^Z \cdot \mathrm{tr}_M^3(\mathcal{B}_n, q)^N \cdot \prod_{i \in \bowtie_K} f_i(q),$$

with per-interface factors $f_i \in \{z, \, z - h\}$ for positive ($\sigma$, both p-p and **p-n**) and negative ($\sigma^{-1}$, n-n) interfaces. **Convention finding (Phase 5q v2).** The production marshalling for `chi_lambda_braid` — implemented in [`canonical_braid_marshalling.marshal_to_chi_lambda_braid`](../computations/canonical_braid_marshalling.py) — silently maps the canonical averaged p-n form `(c=1, d=-h/2, gen)` to `(sign=+1, gen)` (the explicit `# averaged → σ convention` line), so `chi_lambda_braid` itself never sees the averaging coefficient. The closed form for production-matching purposes uses $f_{pn} = z$, NOT $z - h/2$. The strict averaged convention (math-correct $z - h/2$) is available as an opt-in via `pn_convention="strict_averaged"` for audit-trail probes. (**Currency note 2026-07-02:** the [`closed_form_tau_M.py`](../computations/closed_form_tau_M.py) default switched on 2026-06-01 to `pn_convention="bring_color_weighted"` per the owner directive "when canonical / derived, bring should be default"; `"chi_lambda_braid"` remains the opt-in that matches the production marshalling.) Verification witness: `closed-form-tau-M-verification-phase5q.witness.json`.

**Geom ↔ tr_M unification (Phase 5p, queued).** The downstream `ω` stage of `prop:hoefsmit-scattering-pipeline` (`braid β → tr_M → J_K(q) → ω → Geom(K) → × m_e → 𝔪`) consumes $J_K = \mathrm{tr}_M(\mathcal{B}_K)$. The Phase 5q closed form gives the input to ω in closed form; verifying that the propagation through ω → Geom(K) matches the canonical mass-table chain is the Phase 5p task (queued, depends on Phase 5q verification landing).

**Bring color-tube weighted averaging — open audit finding (Phase 5q).** The p-n interface "averaging" in the canonical atomic braid is currently the **uniform bar-invariant projection** $\sigma_{\mathrm{avg}} = (\sigma + \sigma^{-1})/2 = \sigma - h/2$ (per [`thm:averaging-resonance-rule`](#thm:averaging-resonance-rule)). However, the owner's intuition — recorded in [`probe_pn_flavor_asymmetry.py`](../computations/probe_pn_flavor_asymmetry.py) and [`probe_per_sheet_flavor_nonin.py`](../computations/probe_per_sheet_flavor_nonin.py) — is that the canonical form should be **Bring color-tube weighted**: each nucleon carries 3 quark color sheets (proton uud → $(\mu_u, \mu_u, \mu_d)$; neutron udd → $(\mu_u, \mu_d, \mu_d)$), and the p-n boundary should average over the 9 color-pair assignments weighted by quark content. Empirically (Scheme 4, per-sheet PL integration on Bring's surface) this reproduces $\Delta m_{n-p}$ to ~0.14% of CODATA. **Status (updated 2026-07-02 — the paragraph below was stale)**: `pn_convention="bring_color_weighted"` is **IMPLEMENTED and the canonical default since 2026-06-01** in [`closed_form_tau_M.py`](../computations/closed_form_tau_M.py) — net interface factor $f_{pn} = z - h\,(1/2 - \delta/4)$ with the substrate-derived flavor split $\delta = (m_n - m_p)/M_N$ from `flavor_split_subleading(q)` (PR #690, `prop:flavor-split-substrate`; substrate-pure, **no fitted quark masses**). The earlier text describing it as a `NotImplementedError` placeholder requiring quark-mass inputs is obsolete. What **remains open** is the paper-side item flagged by `probe_pn_flavor_asymmetry.py`: the canonical color-sheet ↔ quark-flavor mapping is not yet explicitly stated in the paper (the compute uses the substrate δ, sidestepping quark masses; the downstream Scheme-4 per-sheet PL integration reproducing $\Delta m_{n-p}$ to ~0.14% is a separate mass-level probe, not the substrate convention).

**A≥3 binding campaign — summary (PR #1417, 2026-05-29).** Full record:
[`docs/audits/2026-05-28-binding-endomorphism-analogy.md`](audits/2026-05-28-binding-endomorphism-analogy.md) §"A≥3 derivation campaign". Key chain (all derive-or-refute, no AME fit):
1. **Linear-truncation diagnosis** — `tr ~ exp(Vol)` (Kashaev), so the endomorphism's $\Delta\mathrm{tr}$ is the linearisation; exact for the deuteron, saturating for A≥3. Loci: chirality factor first-order ($a_K=1+wh+O(h^2)$); $\sinh(\ln q)$ Coulomb channel discarded by the canonical projection; $[F,F]$=Hecke-quadratic identified-but-unused.
2. **cosh/sinh bridge PROVED** (Lean + paper): $[n]_q=\sinh(n\lambda)/\sinh(\lambda)$ — algebraic q-integer = transcendental hyperbolic sine; cosh=strong / sinh=Coulomb is a theorem, not a fit.
3. **Yekutieli boundary↔surface form assembled** (Step 2 of the pre-archimedean chain).
4. **Binding carrier = per-rep q-Reeb phase** $\theta_\lambda=\arccos(\chi^\lambda/d_\lambda)$; the scalar $\mathrm{tr}_M$ collapses it. **🛑 The "closes the A=3 mirror pair to 2%, no fit" claim this item used to carry is RETRACTED and must not be re-quoted:** that 2 % came from `C_knot = 5.852 = B_AME/(m_e·|Σ|)`, a straight AME anchor inversion, i.e. a fit (`docs/audits/2026-06-13-binding-method-reconciliation-and-defit-program.md`; PR #1417). The producer `computations/probe_theta_carry_binding.py` says so in its own docstring. What survives is the **structural** claim — that binding is carried per-rep rather than by the collapsed scalar — not any closure figure. Volume-difference (log/cosh/SnapPy) and Lobachevsky-volume observables **refuted** — binding is *linear* in the angle.
5. **q-Hamiltonian rotational energy with derived μ₀** — μ₀ = m_e/(3(q−q⁻¹)/2) ≈ 1.63 MeV is the framework's per-crossing scale (`universal-ilp-algorithm`); E_rot = μ₀·ℏ_q·J_q²(j=n/2) reproduces **B_D = 2.02 MeV vs 2.225 (−9 %) from FULLY derived quantities (0 free params)** — a second independent deuteron derivation. A≥3 keeps the 44–72 % deficit (the per-rep structure, unchanged).

**Net:** deuteron derived twice (m_e·Vol(𝓑₃)·Δtr at +0.19 % and μ₀·ℏ_q·J_q²(3) at −9 %); A≥3 narrowed to one structural item — the per-rep highest-weight $j=n/2$ collapses the per-block Reeb phase just as the scalar trace does. **μ₀ is derived;** the gate is the A≥3 per-rep structure, not the scale. The per-λ "closure" with a fitted `C_knot=5.852` was **retracted**.

---

## 4. Φ_q (compact q-dilog) vs Li_2^q (Rogers) — context sorting

The QOU framework uses **two distinct q-dilogarithms**, NOT interchangeable. Confusion between them was a known historical bug (`mass-endomorphism-tower.md` SUPERSEDED banner; stage-1b audit in `126699b8c`).

| | $\Phi_q(z)$ (Faddeev) | $\mathrm{Li}_2^q(z)$ (Rogers) |
|---|---|---|
| **Context** | MASS-anchor compute | BINDING / symmetric-channel compute |
| **Bar-symmetry** | NOT bar-symmetric (carries dimensional mass scale) | bar-symmetric: $\mathrm{Li}_2^q = \overline{\Phi_q}$ under $q \mapsto q^{-1}$ |
| **Active in compute** | 37 scripts (mass-anchor: `mass_*`, `derived_masses`, `proton_*`, `m_p_*`) | 16 scripts (binding-context: `binding_block_multiplicative`, `binding_via_interface_knot`, bar-symmetric tools) |
| **Active in paper** | 133 content blocks | 77 content blocks |
| **Reference** | `prop:li2q-phiq-bar-symmetrization`, [faddeev1996] | [kashaev1995] for the q-deformed dilog series |
| **Stage-1b audit** | ✓ correctly used in 14 binding scripts? **NO** — they're Φ_q-free | ✓ binding compute pipeline is Li_2^q-only (verified `grep -c Phi_q` = 0 across 14 `binding_*.py`) |

**Key identity (Phase 5b):**

$$\mathrm{Li}_2^q(z) \;=\; \overline{\Phi_q(\bar z)} \quad \text{under bar-involution } q \mapsto q^{-1}$$

The two q-dilogarithms are **bar-conjugates** of each other on the substrate $q$. Using $\Phi_q$ in a binding-context script would import the bar-asymmetric (mass) component into a place that should be bar-symmetric — a discipline violation.

**AJ-saddle unification (conditional — do not treat as established).**
The corpus records a §3b-cond proposition that the context-sorting table
above is two archimedean views of ONE algebraic object: the AJ
annihilator $\hat A_K$ of the colored Jones tower, with $\Phi_q$ = the
root-of-unity saddle regime and $\mathrm{Li}_2^q$ = the real-$q$ saddle
regime — see
[`prop:phi-q-aj-machinery-identification`](../folio/quantum-observable-universe/stochastic-mechanics/phi-q-aj-machinery-identification.md)
(conditional on the class-axiomatised `QuantumAPolynomial` +
regulator-identification inputs; no instances fabricated). Per-knot AJ
status backing it: strong AJ **proved sorry-free in-repo** for $4_1$
(`AJFigureEightAnnihilation.lean`) and the trefoil
(`AJTrefoilAnnihilation.lean` + `AJTrefoilRootEval.lean`, PR #3434);
for $\mathcal{B}_3$ the question is **verified open** in the literature
([`2026-07-06-borromean-aj-literature-status.md`](audits/2026-07-06-borromean-aj-literature-status.md)).
Read-first for any AJ re-pitch:
[`2026-07-03-aj-conjecture-dialog-assessment.md`](audits/2026-07-03-aj-conjecture-dialog-assessment.md).
The table's per-context discipline stands unchanged either way — the
unification, if discharged, would *explain* the split, not license
mixing the two regulators.

**Phase 5b three-layer synthesis (PR #819 §"synthesize"):**

$$\mathrm{Li}_2^q \;\leftrightarrow\; \cos_q(h) \;\leftrightarrow\; \cosh(h)$$

These are **three avatars of the same bar-symmetric kernel** at different levels of detail:
- $\mathrm{Li}_2^q$ — series / motivic level
- $\cos_q(h)$ — phase / oscillatory level  
- $\cosh(h)$ — gain / closed-form level

Pick the right avatar by context — same content, different "lens" on the substrate.

**Where this surfaces categorically** (added 2026-05-24): the torus-knot trace polynomial `P_m(h)` from `tr_M(σ_1^{2m})` reduces to `(q^{2m+1} + q^{-(2m+1)}) / (2[2]_q)`, which at the substrate is `cosh((2m+1)η_0) / (2 cosh η_0)` (hyperbolic avatar) and at a root-of-unity is `cos((2m+1)θ) / (2 cos θ)` (trigonometric avatar). The categorical Weinberg-angle identity `cos θ_W ≈ cosh(5 η_0) / cosh(7 η_0)` (within 1%) is a direct application — see §5 item 5 below.

---

## 5. Compute-pipeline migration backlog (canonical-derivation gaps)

Per the deep review of last 10 days of math improvements (2026-05-20 audit), the following **pipeline-discipline migrations** are queued. The MATH is correct; the COMPUTE has not migrated to the new canonical sources yet.

**Status legend.** ✅ closed · 🟡 in-flight · ⏸️ gated · ⬜ not started.
Tracker last updated: **2026-07-02** — items 2–5 closed (2026-05-23); item 1
was **re-opened as 🟡 PARTIAL** by the 2026-06-03 reconciliation (closed for
the proton only; the per-knot wire-up for A ≥ 2 is the live 9b binding-side
item). An earlier header here claimed "ALL 5 ITEMS CLOSED" — stale.

| # | Status | Action | Where | Closure / PR |
|---|---|---|---|---|
| 1 | ⬛ | Per-knot `VolDensity(K, q₀)` wire-up — **SUPERSEDED, not open** | `m_p_borromean_verification_50dps.py` (proton) + `mass_table_comprehensive.py:208` (all 65 — currently `vol_density_borromean(q)` uniform) + 62 other atom-touching scripts (per [`vol-usage-audit 2026-06-02`](audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)) | **⚠️ SUPERSEDED — DO NOT DO THIS (measured 2026-08-31).** Three independent reasons, any one of which is sufficient. **(a)** Absolute mass is **EXCISED** — owner ruling 2026-08-11, *"NO ABSOLUTE MASS — excise the notion"* ([audit](audits/2026-08-11-excise-absolute-mass-notion.md)) — so there is no absolute-mass magnitude for this wire-up to move. **(b)** The swap makes it **worse**, not better: `computations/canonical_mass.py`'s own docstring records `per_block` → **406 MeV (−57 %)** against λ_A's 966 (+2.96 %, itself a fit), because *both* apply `1/ℏ_q²` to the wrong (Borromean) volume. `per_block` is **binding-ratios-only** by owner ruling 2026-06-24; absolute mass routes through the `canonical_mass` facade. **(c)** The **+2.89 %→+3.86 % budget below is produced by the fitted λ_A form**, not by a missing wire-up — so closing the wire-up would not remove it ([guardrail](canonical-mass-formula-guardrail.md)). Nor would swapping the density: per-knot gives −57 %, i.e. worse in the other direction. **And the "64 scripts" count is not live:** measured 2026-08-31, `vol_density_borromean` appears in **8** files — two probes, `_li_2_q_util.py` plus its vendored mirror, and in `mass_table_comprehensive.py` it is a *reporting field*, not a mass computation. Migration bean `0voz` is **completed** (2026-07-05, superseded by the 2026-06-24 ruling, PR #3340); milestone `4f2d` is closed and was re-verified in the corpus (PR #4822: `mass_vol_density()` has zero external callers; 0 re-entry violations across 2104 scripts). Historical detail follows. **PARTIAL.** Closed for the **proton** specifically (#888 + #895 + #1056 — `m_e × VolDensity(𝓑₃, q₀)` via Family-A linking_weight, gives 965 MeV / +2.89%; **no separate `λ_scale`**, absorbed into the Geom functor per 2026-05-23 coord doc). **NOT closed for atoms A ≥ 2**: production uses `vol_density_borromean(q)` uniformly for ALL atoms instead of the canonical knot-dependent `VolDensity(K, q₀)` per each atom's `atom_braid_word_3A`. The per-knot infrastructure exists (`_li_2_q_util.py::vol_density_per_block(vol_K, tr_M_K, q)`; the only consumer is `vol_density_per_block_wiring.py` testbed) but 64 atom-touching scripts haven't migrated. Error budget mirrors the bug: m_p +2.89%, m_n +2.89%, ⁴He +3.65%, ¹²C +3.73%, ⁵⁶Fe +3.86%. The Yekutieli-extended derivation was briefly tried in production (a1f68d5e5) then PURGED (71d674da1) as non-canonical (bijection NEGATIVE per PR #985; Reading A was substrate-q₀ coincidence). Current PROVED categorical at the **proton**: `VolDensity(𝓑₃, q₀) = (Vol(𝓑₃)/ℏ_q²) · λ_A` with `λ_A = 5/2 + (3/4)h²` Family A from H_4 Wedderburn — but extending this per-K is the open work. |
| 2 | ✅ | Migrate 20 importers of SUPERSEDED `mass_endomorphism.py` to the new `mass_tower_operator_valued` API | 2 substantive callers (`mass_at_3A_proper.py`, `pn_alpha_lp_dual.py`) + 15 utility-only (no migration needed) | **Closed by #889 (block-graph hygiene, 15 `.ts` files) + #944 (H_12 Phase-1 extract unblocking) + #960 (scope-correction audit: 20 → 4) + #966 (canonical API surface in `mass_tower_operator_valued.py` + 2-caller migration).** Strict count: only 2 scripts actually called `mass_from_tower(`; 18 utility-only importers consume substrate helpers and need NO migration. Re-export at the canonical block-name location (`new is orig → True`); zero computation change. |
| 3 | ✅ | Wire the Rust LR convention adapter (PR #829) into `atomic_tr_m_*` scripts for A ≥ 3 | `atomic_tr_m_mpfr_50dps.py` + tr_m_wenzl_bridge + `atomic_tr_m_helium4.py` | **Closed by #901 (bridge-level wiring) + #895 (entry-point `--method canonical-rust` flag + 76-90× speedup at A ≥ 3) + #915 (helium4 refactor to Wenzl bridge — 300× speedup at H_3 cross-check, sub-second H_12 expected) + #946 (default-method flip).** Both `atomic_tr_m_*` files now Rust-backed; defaults flipped. |
| 4 | ✅ | Refactor 4 production tr_M scripts to use `tr_M(𝓑_K) = tr_M(𝓑_K^vac) · z^{p_+} · (z-h)^{p_-}` closed form (Phase 5c.1 + 5l) | `binding_canonical.py` (the one true scalar candidate); the other 3 (`atomic_chirality_residue.py`, `atom_level_wedderburn_tower.py`, `binding_depth_stratified*.py`) need per-partition χ^λ which the scalar closed form cannot supply | **Closed by #921 (opt-in `use_closed_form=True` in `binding_canonical.py` via Phase 5q identity; 3.58e-16 vs symbolic at deuteron, 251× faster).** The other 3 scripts use the per-partition Rust wire-up from PR #901 indirectly — they don't need the scalar closed form (scope clarified during the cluster). |
| 5 | ✅ | Add compute verification for the Reeb-flow / Garside closed-form (4 paper-only commits — `b6ed74635`, `88d7934b4`, `172263c6e`, `6ce96b4ce`) | new script `reeb_flow_garside_closed_form_verification.py` | **Closed by #935.** Verifies all six canonical knot operators (identity, σ_1, σ_2, σ_1σ_2σ_1 Garside, σ_1σ_2, σ_2σ_1) reproduce the closed-form trajectory at MPFR 50 dps. 13/13 assertions pass; Garside-thirds use rational ("1/3", "2/3", "1") to avoid f64 truncation. |

### Manager view — what's next (2026-05-24)

**All 5 cheat-sheet §5 migration items are CLOSED.** The "pipeline-discipline migrations" backlog is empty.

> **⚠️ The paragraph below is superseded** — see the SUPERSEDED banner on row 1 of the §5 table. Its closing sentence, *"analogous per-knot evaluations for atoms A ≥ 2 are the open wire-up work"*, is **no longer true**: the migration is closed, `per_block` is binding-ratios-only, and absolute mass is excised. Kept for the record.
>
> **Framing correction (2026-05-23–24):** there is **no separate `λ_scale` to derive**. The numerical factor previously called `λ_scale` is *what the canonical `VolDensity(K, q₀)` evaluation produces per knot K* — it is absorbed into the Geom functor on a per-knot basis (per `conj:geom-universality` and the 2026-05-23 algebraic→geometric→observable consistency coord doc). The framework's open work is to refine the categorical computation of `VolDensity(K)` **knot-by-knot for each atom** (production currently uses `vol_density_borromean(q)` uniformly across all 65 isotopes — see [`vol-usage-audit`](audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md): 87 scripts uniform, 2 per-knot), not to "calibrate λ_scale". The Yekutieli per-cell variant of `VolDensity` was briefly tried in production (a1f68d5e5) and PURGED on 2026-05-24 (71d674da1) as non-canonical (bijection negative per PR #985). Current canonical at **the proton specifically**: Family A linking-weight inside `VolDensity(𝓑₃, q₀)`; analogous per-knot evaluations for atoms A ≥ 2 are the open wire-up work.
>
> **⚠️ The budget below is an artefact of the FITTED λ_A FORM, deprecated 2026-06-24** — it is not "the gap between the framework's current `VolDensity` evaluation and the categorically-exact one", and closing a wire-up does not remove it; neither does swapping to the per-knot density, which gives −57 %. Absolute mass is in any case excised (2026-08-11). Kept for the record.
>
> **Per-isotope error budget under the current `VolDensity`:** m_p ≈ +2.89%, m_n ≈ +2.89%, Δ_pn ≈ +2.86%, ⁴He ≈ +3.65%, ⁵⁶Fe ≈ +3.86% — see `mass-table-comprehensive.witness.json` (65 isotopes). This is a **single** error, not a "λ_scale closure gap" — it is the gap between the framework's current `VolDensity` evaluation and the categorically-exact one. Refinements queued below address different routes to that refinement.

> **🛑 Superseded for absolute mass (owner ruling 2026-06-24).** The framing-correction above and item 1 below predate the muon-anchor ruling: `m(K) = m_e·VolDensity(K, q₀)` is **not** the canonical absolute mass — absolute nucleon/atom masses route through [`canonical_mass.py`](../computations/canonical_mass.py) ($m_p \approx 938.27$ MeV, CODATA), and the Family-A λ_A leg was excised as a CODATA-implied fit ([refutation audit](audits/2026-06-24-lambda-a-refutation-artifact-audit.md)). The per-knot `VolDensity(K)` wire-up below remains live as the **binding-side** per-knot density (scale-cancelling uses only). Read first: [`canonical-mass-formula-guardrail.md`](canonical-mass-formula-guardrail.md).

The forward work has shifted from §5 mechanics to scientific closure:

1. ~~**Per-knot `VolDensity(K, q₀)` wire-up — binding-side only (post
   2026-06-24 ruling; see the 🛑 note above).** 64 of 65 atom-touching
   scripts still use uniform `vol_density_borromean(q)`
   ([`vol-usage-audit`](audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md));
   consumer-lane migration is running on PR #3199 (bean `4f2d`).~~
   **⚠️ STALE ON ITS OWN TERMS (2026-08-31).** Bean `4f2d` is **closed**, so the
   migration this points at is not running. And the binding side does not go
   through `vol_density` at all: measured across `computations/`, **no binding
   script references `vol_density`** — binding is `B = m_e·Σ_n (n−1)·Vol_n(K)`
   (step 9b), which uses `Vol` directly. `vol_density_per_block` has **four**
   references in the whole repo — its definition, its vendored mirror, one
   demonstration script and one audit — so there is no consumer lane left to
   migrate. See the SUPERSEDED banner on row 1 of the §5 table for the
   absolute-mass half.
   **Single narrative source: §9** (frontier detail, flip gate,
   many-body series) — the long per-knot narrative that lived here
   drifted against §0/§9 and was consolidated 2026-07-02 (PR #3200);
   pre-ruling history is preserved in the item-1 row of the table above.
2. **Q_β refinement (research-grade, open).** **2026-06-03 reconciliation**: the prior bullet "the 2026-05-24 dashboard shows it now passes 100×" + "c_3 = -2 = J_Hopf(q=1) categorical-closure-friendly" is **STALE**. Live state per `per-observable-100x-status.witness.json` (2026-06-03): Q_β err = 1279 ppb, **miss = 164×**, `beats_100x = False`. The 2026-05-28 q₀ re-pin (per `docs/audits/2026-05-30-q0-repin-stale-witness-audit.md`) reverted the temporary 2026-05-24 pass. The `c_3 = -2 = J_Hopf(q=1)` framing is itself **flip-flop entry #4** in [`docs/coordination/1ppq-qbeta.md`](coordination/1ppq-qbeta.md) — settled as NEAR-MATCH not Taylor-exact (PR #1593 order audit: the per-block Δtr_M is O(√u) ε¹, ladder c_3 is at u³ ε⁶ — accidental 5-ε-order coincidence). Current keystone: **Q_β Habiro element identification** (the scaling map `f: Δtr_M(√u) ↦ Q_β(c_3 at u³)`). **Currency update (2026-06-10):** per-rung tiers live in [`coordination/ck-dk-canonical-registry.md`](coordination/ck-dk-canonical-registry.md); eliminated methods in the [refuted-class map](audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md) (C1–C12 + 1309-candidate real-q saturation + 4 KLR composite preflights refuted at u², PRs #1914/#1924); the extraction precision floor `σ(c_k) = σ_R/u^k` (PR #1844) proves only c_2, c_3 are data-determined ⇒ c_k≥4 is framework-derivation-only. Open axis: fibre-level kernel `R(q,ξ)`/`Φ₂` (constraints: bar-odd `a_1 = √2·Φ₂`, depth ≥ 3 or non-constant, ζ₄ residue, simple pole at u_substrate). Full state of play: [2026-06-10 synthesis](audits/2026-06-10-qbeta-ck-state-of-play-synthesis.md). **Currency update (2026-07-02, per the [`1ppq-qbeta.md`](coordination/1ppq-qbeta.md) ledger tail):** discrete braid-tower probes are exhausted (single-content mode residual 480/606/186/240 %, PR #2502); the live lead is the **continuous E_q(2) contraction** (Hahn–Exton q-Bessel). The content/twist eigenbasis reframing ([2026-06-19 audit](audits/2026-06-19-content-twist-eigenbasis-reframing.md)) makes three verified facts promotable to exact-symbolic lemmas (L1 order-parity = word-length parity; L2 `χ_λ(1/q) = (−1)^L·χ_{λ'}(q)`; L3 the framing 3-pole GF) — Lean follow-up queued; does NOT close the Δ_λ gate.
3. **Phase-1b BlochWigner Lake-wiring** (PR #956's roadmap) — Lake-wire `QOU.Archimedean.BlochWigner_unit_circle` into the module tree, then strengthen `BringZeroModeBlochClass` field from `∃ z : ℝ, z = bringZeroModeValue` to `∃ θ : ℝ, BlochWigner_unit_circle θ = bringZeroModeValue`. Closes the literal-rfl loophole. Auxiliary to the `VolDensity` refinement.
4. **L2 100× Subgoal-1 close-out**. **Currency update (2026-07-05)**: the committed `per-observable-100x-status.witness.json` carries `beats_100x_scoreable = 1` / `scoreable_total = 5` — **1 of 5 SCOREABLE predictions** passes 100×, and it is **m_K/m_π** alone. Do **not** quote the bare `beats_100x_count = 2` (AGENTS.md STRICT): it counts the calibration inputs `m_e` and `m_p`, whose errors are *defined* zero rather than measured. And even that 1 is **truncation-fitted + α_em-`sorry`-conditional**, so the **unconditional parameter-free count is 0/5** (red-team 2026-08-22, `docs/audits/2026-08-22-mK-mpi-l2-red-team.md`). **m_p was DROPPED 2026-07-04**: its "pass" (substrate anchor, 0.0004 ppb) held only because a fitted Habiro tower `(1+46u⁴)(1+4u⁵)(1−29u⁶)` — a muon-era fit left applied to the proton-pinned q₀, a live +242 ppb regression — landed it on CODATA; that tower was removed, and the honest documented-pin round-trip is +1.35 ppb, a ~437× miss (full analysis: [`docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md`](audits/2026-07-04-c4-mu-p-tension-pin-dependence.md)). So the remaining gaps are the **five scoreable** (m_μ, Q_β, m_n, Δ_pn, m_K/m_π); **m_p is `NOT SCORED`** — the live witness marks it an anchor round-trip (`miss_factor: "N/A"`, "the framework content cancels"). m_μ is a separate gap (211.2 ppb, 970.2× miss — independent μ–p floor, see `docs/audits/2026-06-02-m-mu-pr1556-superseded-by-witness.md`). The (Q_β, m_n, Δ_pn) trio shares a single root cause documented in `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`. (Supersedes the prior "3 of 7 … m_p PASSES" reconciliation, which predated the 2026-07-04 de-fit.)
5. **Electroweak triplet (H/W/Z) torus-knot mass route — RT-chain only.** Higgs = T(2,8), Z = T(2,6), W± = T(2,4) per the SM-particle RT-route map [`2026-05-24-sm-particle-categorical-map-rt-route.md`](audits/2026-05-24-sm-particle-categorical-map-rt-route.md) + [`2026-05-24-pr1122-retraction-and-existing-canonical-adaptation.md`](audits/2026-05-24-pr1122-retraction-and-existing-canonical-adaptation.md). (Currency 2026-07-05: the standalone content block was dropped from `archimedean-universe/` in the 2026-05-25 chapter restructure and **re-homed** to [`particle-interactions/electroweak-higgs-torus-link-triplet.md`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md) — the live block for the T(2,k) triplet identification. The structural embedding half is split into [`prop:electroweak-triplet-bring-embedding`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/particle-interactions/electroweak-triplet-bring-embedding.md); the physical identification stays a conjecture. Related EW-cell content also lives in `mass-theory/{hoefsmit-ew-cell-content,weak-symmetric-normalization,weak-spectral-completeness}.md`, and the audit docs above document the RT-route.) T(2, k) is Seifert-fibered with Vol = 0, so the canonical `VolDensity` chain in #1 above does **not** apply directly. Recent results:
   * **Unified binomial pattern (PR #1125 — `torus-knot-h-expansion-pattern.md`):** Every even-h coefficient of `tr_M(σ_1^{2m})` collapses to `c_{2j}(T(2, 2m)) = C(m+j, 2j) / 2`, verified symbolically across 54 cells. This is the lower-level validator for any candidate RT specialization.
   * **Closed cosh form for the trace polynomial — connects to Phase 5b `cos_q ↔ cosh` synthesis (§4 above).** The trace polynomial `P_m(h) = Σ_{j=0}^{m} C(m+j, 2j)/2 · h^{2j}` reduces (sympy-exact across `m = 1..6`) to a single bar-symmetric ratio:
     $$P_m(h) \;=\; \frac{q^{2m+1} + q^{-(2m+1)}}{2\,[2]_q}, \qquad h = q - q^{-1}.$$
     At substrate `q_0 ∈ ℝ_{>0}` set `η_0 = log q_0`: then `q^n + q^{-n} = 2 cosh(n η_0)` and `[2]_q = 2 cosh(η_0)`, so $P_m(h_0) = \cosh((2m+1)\,η_0) \,/\, (2\cosh η_0)$. The trace polynomial is the **hyperbolic-cos avatar** of the bar-symmetric kernel (Phase 5b § "three avatars: Li_2^q ↔ cos_q ↔ cosh"). **Currency 2026-08-30:** the identity is still recorded as "sympy-exact across `m = 1..6`", i.e. case-verified. It has since been checked exact for `m = 0..14`, and — more usefully — it is *provable*: `S_m(h) := Σ_j C(m+j,2j) h^{2j}` satisfies the Chebyshev recurrence `S_{m+1} = (h²+2)S_m − S_{m−1}` (verified `m = 1..15`), which is the same recurrence as `(q^{2m+1}+q^{−(2m+1)})/(q+q^{−1})` since `q²+q^{−2} = h²+2`, with base cases `S_0 = 1`, `S_1 = h²+1`. The coefficient-level identity behind it is `C(m+1+j,2j) = C(m+j−1,2j−2) + 2C(m+j,2j) − C(m+j−1,2j)` (no counterexample for `1 ≤ m ≤ 15`). So this is a finite induction, not an open problem — a Lean proof would move it from case-verified to proved. **DONE 2026-08-30** — `QOU.BraidKnot.TorusKnotTracePolynomial.traceIdentity`, sorry-free, over any field of characteristic zero with no bound on `m`: `chebS_q_form` is the `q`-form of the recursion, `chebSum_eq_chebS` the binomial sum, and `choose_shift_identity` the Pascal fact underneath. This row is no longer case-verified. At a root-of-unity `q = e^{iθ}` it becomes the trigonometric Chebyshev ratio `cos((2m+1)θ) / (2 cos θ)`.
   * **W/Z ≈ cos θ_W within 1% — categorical Weinberg-angle identity (commit `12b6c77c1`).** Combining the previous two bullets, `P_W / P_Z = \cosh(5 η_0) / \cosh(7 η_0)` (no `[2]_q` factor; it cancels). At `η_0 = log q_0 = 0.1043407203`: `cosh(5η_0) / cosh(7η_0) = 0.8908357` vs SM `cos θ_W = m_W/m_Z = 0.8814` — **+1.1% deviation, structurally derived, no empirical fit.** The trigonometric SM Weinberg angle is realised categorically as a *hyperbolic* cosh ratio at the substrate parameter. **⚠️ The explanation of the 1% gap that stood here — "the substrate `q_0` is close enough to 1 that `cosh((2m+1)η_0) ≈ cos((2m+1)θ_W)`", so "the 1% gap is the cosh-vs-cos discrepancy" — is REFUTED by its own numbers (2026-08-30).** At the *same* `η_0`, `cos(5η_0)/cos(7η_0) = 1.163849`, against the cosh form's `0.890836`: the cosh↔cos difference is **30.6 %**, not 1 %, and it points the wrong way (the trigonometric form overshoots 1, while the SM value is below it). The two functions split at *second* order with *opposite* signs (`cosh x = 1 + x²/2`, `cos x = 1 − x²/2`), so their gap grows like `x²` rather than shrinking, and `7η_0 = 0.7304` is not small. Note also that the refuted sentence compared `cosh` at `η_0` with `cos` at `θ_W` — two different parameters — which is not a well-formed approximation claim. The 1.07 % deviation is therefore **unexplained**, not attributed. The separation is itself now a theorem rather than a measurement — `QOU.MathlibExt.CoshCosSeparation.cosh_div_lt_one_lt_cos_div` proves `cosh a / cosh b < 1 < cos a / cos b` for **all** `0 < a < b < π/2`, so the two readings bracket `1` at every admissible `η`, not merely at `η_0`. For scale: it is whatever the cosh form misses, and it corresponds to a **5.11 %** shift in `η_0` (the `η` making the cosh form exact is `0.109676` against `q_0`'s `0.104341`). What survives unchanged is the *structural* claim — the closed form is derived, bar-symmetric, and carries no empirical fit. Better than PR #1122's substrate-point √[2]_q fit (which was 7% per jet under jet-order check) — and now has a clean closed form.
   * **Z/H twist-count ratio is GENUINE.** `J_2(T(2,6))/J_2(T(2,8))` ratio = `6/8 = 0.75` at every jet order matches SM `m_Z²/m_H² ≈ 0.729` within ~3 %. Structurally real per the jet-order validation in commit `aa11d2f06`.
   * **W = √[2]_q STRONG claim RETRACTED** (commit `aa11d2f06`, PR #1122 / PR #1126 jet-order check + retraction audit `1e56c9464`): the substrate-point match was a jet-mixing coincidence, not a structural identity. A single multiplicative W-only correction cannot fix W/Z and W/H simultaneously (they need boosts in opposite directions). The √2 in the framework is implicitly recovering the SM Higgs-VEV doublet convention.
   * **Two-class normalization observation** (commit `12b6c77c1` §"structural-limit"): `mass(GeV) / P_m(h_0)` gives ≈ 143 for W and Z (gauge bosons), ≈ 171 for H (scalar). Reassessed in audit [`2026-05-24-gauge-vs-scalar-mass-factor-derivation-path.md`](audits/2026-05-24-gauge-vs-scalar-mass-factor-derivation-path.md) §5: empirically real but NOT a simple ratio of SM couplings. Three candidate paths (A: substrate-derived `v_VEV`, declined 2026-05-08; B: `g, g'` from categorical SU(2)_L × U(1)_Y; C: `λ/g²` from categorical chain — numerically inconsistent with simple SM combinations). Cleanest defensible statement: the absolute scale + W/H + Z/H ratios remain open.
   * **Lean infrastructure landed** (commit `555587685`, PR #1128 follow-up):
     - `QOU.QuantumObservableUniverses.CategoricalHiggsIdempotent` REFINED with explicit fields (`vev_v_GeV`, `vev_lower_component_GeV = vev_v_GeV / √2`, `gauge_coupling_g`, `gauge_coupling_g_prime`, `higgs_self_coupling`, `cos_theta_W`) and a PROVED theorem `m_W_over_m_Z_eq_cos_theta_W : m_W_GeV / m_Z_GeV = cos_theta_W` (via `field_simp + ring`, conditional on the class). The √2 is now explicit in `vev_lower_component_eq_v_over_sqrt2` — encoding the SM Higgs-doublet convention, NOT a deeper categorical fact (per PR #1126 retraction).
     - `QOU.BraidKnot.TorusKnotMass` (new): scaffolds RT-route mass-derivation with `poly_growth_degree`, `gauge_mass_factor`, `scalar_mass_factor`, `factors_distinct`, `WZ_mass_ratio`. Default instance carries `sorry` (open conjecture per §3b-cond).
     - `QOU.Kashaev.VolumeConjecture` (pre-existing, adaptable): encodes Vol=0 ⇒ sub-exponential `|J_N|`, already captures "torus knots need a different chain".
   * **Three substrate→EW empirical-match hypotheses + scaffolded Lean theorems** (probe `ew_couplings_substrate_derivation_probe.py` + audit [`2026-05-24-ew-couplings-substrate-empirical-matches.md`](audits/2026-05-24-ew-couplings-substrate-empirical-matches.md) + Lean `QOU.BraidKnot.SubstrateEWHypotheses` from commit `f16adbb17`). Probe tested ~50 candidates; three pass the triple test (match < 1%, uses only substrate + universal constants, plausible categorical origin):

     | hypothesis | predicted | dev | structural anchor |
     |---|---:|---:|---|
     | `g = π · h_0` | `π · 0.2090602988 = 0.6567823` vs SM 0.6535 | **+0.50%** | π from connection 1-form integration on substrate (Yekutieli MI machinery; see [`yekutieli-mi-derivation-path.md`](audits/2026-05-24-yekutieli-mi-derivation-path.md)) |
     | `v_framework / v_SM = log(6)` | `log(6) = 1.7918` vs measured `443/246 = 1.8008` | **−0.50%** | 6 = `gsNFBasisCardinalityB3` = `|S_3|` = `dim_ℂ H_3(q)` (PROVED) — order of the 6 GS-NF knot operators (γ, σ_0, σ_1, L_+, L_-, e^-); Chern-Simons-style `log |G|` |
     | `scalar_mass_factor / gauge_mass_factor = 6/5` | `6/5 = 1.200` vs measured 1.196 | **+0.35%** | 6 = `|S_3|` (knot-operator basis); 5 = `partitionsOfFour` = Wedderburn-block count at H_4 ((4), (3,1), (2,2), (2,1,1), (1,1,1,1)) — both PROVED |

     **(Currency 2026-07-02 — the Lean side is already in the honest §3b shape, 0 sorries.)** The three hypotheses live in `SubstrateEWHypotheses.lean` as a **content-bearing conjecture class `SubstrateEWDerivations`** (fields `claim_g_eq_pi_h`, `claim_v_ratio`, `claim_scalar_gauge`; `-- Ref:` cited; **no instance provided** — the open state), with honest conditional `def` accessors projecting the fields; the structural anchors (`gsNFBasisCardinalityB3 := 6`, `partitionsOfFour := 5`) are PROVED unconditionally by `rfl`/`norm_num`. Earlier text here describing "class-conditional `theorem`s with `sorry` markers" is obsolete. **Epistemic discipline (per `production-vs-exploratory-discipline`):** these are *structurally suggestive empirical matches*, not theorems. The conversion to rigorous identities requires: (a) connection 1-form integration over the substrate loop to derive `π · h_0`, (b) knot-operator partition-function evaluation to derive `log |S_3|`, (c) cross-Wedderburn-block normalization ratio to derive `|S_3| / |Part(4)|`. Research-grade, 1-2 weeks each.
   * Open: **derive** the 3 structural→empirical hypotheses above — i.e. supply the `SubstrateEWDerivations` instance via (a) connection 1-form integration (`g = π·h₀`), (b) knot-operator partition function (`log|S_3|`), (c) cross-block normalization (`6/5`) — upgrading them from "match within < 1%" to "categorical theorem". Research-grade, 1–2 weeks each; there are **no sorries to close** (the class deliberately has no instance).

### Adjacent open work (not in §5 but cited by the cluster)

- **Tier 1.A 4× gate** (PR #886): ⁶Li wall 84.5 s, target < 60 s. 1-2 day Rust optimisation (FxHashMap intermediate + defer-GCDs in `reduce_laurent`).
- **Tier 1.B orbit reduction** (gates A ≥ 8, ¹²C / ¹⁴N / ¹⁶O — organic chemistry): preflight required (`§4.2` of the handover doc; orbit-trace identity must validate at 1e-25 on ⁴He / ⁵Li / ⁶Li before implementation).
- **Bring color-tube quark-weighted p-n averaging**: closes Δm_{n−p} to ~0.14 % per `probe_pn_flavor_asymmetry.py` Scheme 4. Research-grade — a candidate refinement of the p-n cross-section of `VolDensity`.
- **Complex-$q_0$ categorical lift** (research-grade — PR #1127): the pre-Archimedean substrate is already generic over `{R : Type*} [CommRing R]`; $q_0 \in \mathbb{R}$ is an *engineering / empirical* commitment, not a theorem (audit: [`2026-05-24-q-zero-reality-audit.md`](audits/2026-05-24-q-zero-reality-audit.md)). On $|q| > 1$ with $\mathrm{Im}(q) \neq 0$ the **Lusztig bar** ($q \mapsto q^{-1}$) and the **Hermitian $\ast$** ($q \mapsto \bar q^{-1}$) involutions *split*; the split is the categorical home for any future $\mathrm{Im}(q_0)$ contribution. Note: the dominant 2.89 % L2 gap is **bar-symmetric** (m_p, m_n shift together), so complex $q_0$ is *not* a candidate fix for that gap — VolDensity refinement is. Complex lift is independently valuable infrastructure.

---

## 6. Key bibliography (paper-side BibTeX keys)

| Result | Reference |
|---|---|
| Hecke algebra of type A | `[iwahori1964]`, `[geckpfeiffer2000]` |
| Iwahori-Hecke quadratic relation as Yang-Baxter | `[jimbo1986]` |
| Markov trace uniqueness + Jones polynomial | `[jones1987]` |
| Wenzl Markov-trace closed form + disjoint multiplicativity | `[wenzl1988]` §1.7 |
| Hoefsmit seminormal representations | `[hoefsmit1974]`, `[ram1991]` |
| Murnaghan-Nakayama for Hecke characters | `[ram1991]` |
| Frobenius pairing / Hopf algebra symmetric structure | `[majid1995]`, `[kassel1995]` |
| Yekutieli multiplicative integration | `[yekutieli2015]` |
| Quantum dilogarithm Φ_q (compact q-dilog) | `[faddeev1996]` |
| Rogers q-dilogarithm Li_2^q | `[kashaev1995]`, `[kirillov1995]` |
| Macdonald-Schur polynomials | `[macdonald1995]` |
| Bring surface $\chi_{\mathrm{eu}}(M_0) = 2 - 2g(M_0) = -6$ ($g(M_0)=4$) | `[bring1786]`, `[klein1884]` (historical); `rem:three-euler-characteristics` |
| Gröbner-Shirshov basis (general) | `[bokut2007]`, `[chenhongbo2010]` |

---

## 7. Where to find things (quick index for Claude / future agents)

| Need | Look at |
|---|---|
| The full chain rendered in the paper | [`pre-archimedean-derivation-chain.md`](../folio/quantum-observable-universe/mass-theory/pre-archimedean-derivation-chain.md) |
| 7 first-principles entry points + trust basis hierarchy | `computations/DERIVATION-CHAIN-METHODOLOGY.md` |
| Canonical-derivation discipline (production scripts) | `computations/derivation_chain.py` |
| q_0 50-dps canonical pin | `computations/q_parameter.Q_50_DIGIT_STR` |
| Wenzl y_λ (numeric + symbolic) | `computations/y_lambda_wenzl_bridge.py` |
| Hecke characters at varying q | `computations/hecke/hecke_characters.chi_lambda_braid` (Python + Rust kernel) |
| **3-axis (knot, partition, atom) derived-χ catalogue** | [`computations/derived_chi_catalogue.py`](../computations/derived_chi_catalogue.py) (schema), [`derived_chi_catalogue_sweep.py`](../computations/derived_chi_catalogue_sweep.py) (production sweep), `derived-chi-catalogue.witness.json` (cell witness) — PR #1952 |
| Catalogue parallel backend (auto-detects GIL release) | [`derived_chi_catalogue_parallel.py`](../computations/derived_chi_catalogue_parallel.py) — `ThreadPoolExecutor` when `pyhecke_native >= 0.9.0`, else `ProcessPoolExecutor` fallback |
| Catalogue Tier 2/3/4 optimisations | Tier 4 in-memory memoize: [`derived_chi_catalogue_memoize.py`](../computations/derived_chi_catalogue_memoize.py); Tier 3 bar-symmetry: [`derived_chi_catalogue_bar_symmetry_audit.py`](../computations/derived_chi_catalogue_bar_symmetry_audit.py) (1.9× sweep speedup); Tier 2 M_n disk cache: [`derived_chi_catalogue_mn_disk_cache.py`](../computations/derived_chi_catalogue_mn_disk_cache.py) |
| Catalogue Tier 1 LR factorisation (math + scaffold) | Audit: [`docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`](audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md); Scaffold: [`derived_chi_catalogue_lr_scaffold.py`](../computations/derived_chi_catalogue_lr_scaffold.py) |
| Catalogue Phase 3 production wire demo (1189× lookup speedup) | [`derived_chi_catalogue_production_wire_demo.py`](../computations/derived_chi_catalogue_production_wire_demo.py) |
| Catalogue Lean scaffold | [`folio/quantum-observable-universe/lean/QOU/Machinery/DerivedCharacterCatalogue.lean`](../folio/quantum-observable-universe/lean/QOU/Machinery/DerivedCharacterCatalogue.lean) |
| pyhecke_native GIL release + batched-GP roadmap | [`docs/audits/2026-06-07-pyhecke-native-gil-release-patch.md`](audits/2026-06-07-pyhecke-native-gil-release-patch.md) — Patch 1 (GIL) LANDED in v0.9.0; Patch 2 (batched chi_lambdas_via_gp + Rayon) LANDED but **NOT routed by default** — empirical perf showed threads + Tier 3 outperform batched-Rayon at medium n |
| Hoefsmit symbolic matrices | `computations/hecke/hecke_character_symbolic.hoefsmit_matrices_symbolic` |
| Canonical atomic braid construction | `computations/mass_at_3A_proper.atom_braid_word_3A` |
| LP duality (operator selection) | `computations/lp_dual_solver.py` (`solve_operator_selection_lp`) |
| Notation register (post-Phase 5n) | [`folio/quantum-observable-universe/notation/notation-register.md`](../folio/quantum-observable-universe/notation/notation-register.md) |
| 1ppb coordination ledger | [`docs/coordination/1ppb-categorical-chain.md`](coordination/1ppb-categorical-chain.md) |
| Precision dashboards | `computations/onepb-status-dashboard.witness.json` (L1) + `per-observable-100x-status.witness.json` (L2) |

---

## 8. The "everything is derivation, not fit" discipline (CLAUDE-facing)

**The 3-calibration rule** is strict: the canonical mathematical calibration triple is the **bar-parity channel triple** $(m_e, P_{\mathrm{skew}}^{\beta}, P_{\mathrm{avg}}^{\pi})$ — a leptonic mass scale and two bar-parity channels, entering at orders $h^0$, $h^2$, $h^3$ (owner ruling 2026-06-26; the masses are the numerical *proxies*, not the canonical inputs). CAL-2 is the neutron $\beta$-sector bar-skew channel $P_{\mathrm{skew}}^{\beta}$; it fixes $q_0$ through its most precise proxy, the lepton ratio $m_\mu/m_e$ (which dimensionalises to $\mathrm{Vol}(4_1)$). In the **Physical-Observations** layer one may anchor $q_0$ on a derived quantity of smaller experimental error — the proton ratio $m_p/m_e$ (0.017 ppb vs the muon ratio's 22 ppb; re-pin 2026-05-28, live solver `constants.py::q_at`), making $m_\mu/m_e$ a $9.5\sigma$ cross-check prediction (the μ–p tension — see `docs/audits/2026-05-28-mu-p-tension-substrate-floor.md`); this is a precision substitution, not a fourth calibration. $Q_\beta = \hbar/P_{\mathrm{skew}}^{\beta}$ is the **CAL-2 proxy** — not a fourth input and not "derived from CAL-1+CAL-2": the symbolic form $Q_\beta = m_e |q_0^2 - 2q_0 - 1|(q_0+1)/(2q_0^3)$ reproduces it from $q_0$ to 0.17% as a cross-check, the bar-odd $\sinh$ partner of the bar-even $\cosh$ meson scale $m_\pi$. Everything else MUST derive from these three via the chain above.

**Common pitfalls** (look for these in code review):
- Hardcoded literal values where a categorical derivation exists → **discipline violation**. Example: `LAMBDA_PROTON_DOC = 2.4599527869` should derive from `prop:lambda-scale-bring-bloch-identity`.
- Φ_q in a binding-context script → **bar-symmetry violation**. The binding context wants Li_2^q.
- Calibration parameters not in the 3-input set → **4th-calibration violation**. The AGENTS.md `Δ_λ gate` (Track A blocker) explicitly forbids a 7th closure ansatz.
- Substrate-side compute using $q$ as $\mathbb{R}$ before the Archimedean functor → **§7c base-ring violation**. Everything categorical should be generic over `[Field R]` until step 9.

**Final-stage discipline**: every script in `computations/` (non-deprecated) should either (a) be backed by a `derivation_chain.py`-tracked DerivationChain, or (b) be marked `SCRIPT_CITED` against a canonical script that IS so backed.

---

## 9. Partition-respecting verification + mass = density × volume (2026-06-02)

The chain's frontier (step 9) is governed by one structural question the owner
posed: **do all the categorical invariants / functors / pairings respect the
Wedderburn partition decomposition `⊕_{λ⊢n} M_{d_λ}`?** If they do, the per-block
density `Δ_λ` is forced and `mass = density × volume` must be a per-λ sum.

### 9.1 Partition-respecting status

| Object | Respects partition? | Basis |
|---|---|---|
| Markov trace `tr_M = Σ_λ y_λ χ^λ` | ✅ **by construction** | Wenzl §1 — the `y_λ` ARE the per-block central weights; this IS the block decomposition |
| Wenzl weights `y_λ(q)` | ✅ derived | `y_lambda_wenzl_bridge.py`; one scalar per λ |
| Hecke characters `χ^λ(β_K)` | ✅ derived | Hoefsmit seminormal, per-irrep λ |
| Frobenius pairing `⟨a,b⟩_F`, self-duality `Ψ=S²=id` | ✅ formalised (D3/D23) | the pairing is central/symmetric; per-block orthogonality follows from Schur — **proved sorry-free** at the algebra level, finer per-λ orthogonality is the standing audit item |
| q-Reeb phase `θ_λ = arccos(χ^λ/d_λ)` | ✅ per-λ | `binding_reeb_phase_decomposition.py` |
| Categorical action / R-matrix (per generator) | ✅ **proved block-diagonal** | `MultiGeneratorSpectrum.lean` — 6×6 transfer matrix block-diagonal by induction; partition-*agnostic* until the Schur projection `π_λ` |
| Central idempotents `π_λ` (orthogonal, central) | 🟡 asserted (class axiom) | `Wedderburn.lean` — `trace_decomposition` PROVED *from* the axiom; the orthogonality `π_λπ_μ=0` is a classical theorem (Mathas §3.43) **awaiting Lean formalization**, not math |
| Confinement SDP (`T_w` selection) | ✅ per-block duals | `lp_dual_solver.py` emits `y_star[λ]` shadow prices |

**Verdict:** the binding/mass machinery is **manifestly block-graded** — every
load-bearing object is a per-λ quantity or a sum over λ, and the per-generator
block-diagonality is *proved by induction*. So `Δ_λ` is genuinely a per-block
density and the volume-Wedderburn framing is structurally legitimate. The gap is
not whether the objects respect the partition (they do) but **what the per-block
density numerically is** (§9.3).

**Two caveats the 1–6 audit surfaced** (both *formalization*, not math, gaps —
track in the proof-watcher queue):

1. **`y_λ` uniqueness rests on Schur character-orthogonality**, which is **not yet
   in Mathlib** (`wedderburn-as-noncomm-fourier.lean`); the cross-validation
   `Σ_λ y_λ χ^λ = z^{ℓ(w)}` passes numerically (n=3,4,5) but is unproved in Lean.
   Same for `π_λ` orthogonality. The per-λ Frobenius block-orthogonality
   `⟨a,b⟩_F = ⊕_λ ⟨a,b⟩_F^λ` is now **formalized** (2026-07-03,
   `QOU.Hecke.WedderburnDecomp.frobPairing_block_decomp` /
   `frobPairing_block_orthogonal`, sorry-free) — conditional on the
   `WedderburnDecomp` class axioms, whose discharge is the L-1/L-2 debt
   (§9.4).
2. **The per-block q-Reeb phase `θ_λ` is DERIVED at step 2 (Yekutieli boundary
   holonomy) but COLLAPSED by the scalar trace** `tr_M = Σ_λ y_λ χ^λ`. This is an
   *information loss*: the framework computes the per-λ phase, then sums it away.
   **Retaining `θ_λ` per-block instead of collapsing it is the binding lever**
   (§9.3) — and the heaviest *unused* duality in steps 1–6.

### 9.2 mass = density × volume — the realized form

The owner's `mass = density × volume` IS the chain, with one correction the
compute has already established:

- **Volume is NOT the carrier** — it is the *exponential* of it. `tr_M ~ exp(Vol)`
  (Kashaev), so the binding endomorphism's `Δtr_M` is the **linearization** of the
  hyperbolic volume (§3, the *Bind* row; re-confirmed by the volume-Wedderburn
  probe in PR #1709, where *no* positive per-block volume reproduces even the
  **sign** of the ³H/³He split).
- **Density = per-rep q-Reeb phase** `θ_λ = arccos(χ^λ/d_λ)` (the "Hecke energy"
  per block) — a *signed, per-λ* angle. Markov-weighted it is a defensible
  per-block structural object, but its **magnitude closure of the A=3 mirror
  difference is NOT categorically derived**: the best *structural* combination
  reaches only ≈ 2.52 %, and the published 0.11 % relied on a **fitted `(1+q)/2`
  factor (CAL-4 antipattern)** that is also stale (canonical q₀ gives +0.12 %,
  sign-flipped). See §9.3 and [`2026-05-31-isospin-mirror-v9-discipline-assessment.md`](audits/2026-05-31-isospin-mirror-v9-discipline-assessment.md).
- **Volumes** enter as the knot volumes of the canonical braid — `Vol(𝓑₃)` (proton,
  step 9a), `Vol(6₂)`, Borromean `8G` — through the q-hyperbolic infra
  (`knot-volumes.py`, `Li_2^q` / compact-q-dilog `Φ_q`, §4 context-sorting).

> **🛑 RETRACTED 2026-08-25 (PR #5765): `Δ_λ` is NOT the q-Reeb phase density.**
> The per-partition value is **proved**, sorry-free and general-n:
>
> `Δ_λ = (−1)^{n(λ)} · dim V_λ` — the **signed Springer dimension**; sign = jet-order
> valuation parity, magnitude = Wedderburn dimension.
> [`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`](../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaGeneralNUnconditional.lean)
> (PR #4580), wired to [`computations/delta-lambda-witness.json`](../computations/delta-lambda-witness.json).
>
> An identification of the **same symbol** with a different object is a
> contradiction, not a second reading, so the sentence this note replaces is
> withdrawn rather than qualified.
>
> **What survives, and it is the paragraph above:** the q-Reeb phase `θ_λ` is a
> defensible *per-block structural object*, and the text above is already correct
> that its **magnitude closure is NOT categorically derived** (best structural
> combination ≈ 2.52 %; the published 0.11 % relied on a fitted `(1+q)/2`, a CAL-4
> antipattern, and is stale besides). Keep it as the per-block phase it is; do not
> read it as `Δ_λ`.
>
> **And the proof does not close the gate.** The witness's own caveat: *"VALUE ONLY —
> the binding total additionally needs the `y_λ·χ^λ` weighting and a separate
> super-pairwise [extensive term]."* The **magnitude** leg is open; six ansätze failed
> on the deuteron because they tried to force an extensive quantity into a per-block
> weight. See [`2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`](audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md).

> **Guiding principle — preserve information until observation.** The
> archimedean functor `τ` (step 9) *is* the observation; it is the **only**
> place categorical structure should collapse to a real number. The production
> scalar `tr_M = Σ_λ y_λ χ^λ` collapses the per-block phase `θ_λ` at step 5 —
> *before* observation — which is an **information loss** that is harmless at
> A=2 (the linearization is exact) but destroys the per-block content needed at
> A≥3. The fix is to **carry the full per-λ `θ_λ` vector** (rotation
> `arccos` + growth `arccosh`) through the GB-filtration/jet tower and let `τ`
> (or the operator-valued combiner) do the collapse last. This is the same
> fibre-vs-observable cut as the `Im(q)` discipline and the "delta is
> pre-archimedean" result (`prop:delta-pre-archimedean`): **stay in the fibre as
> long as possible, observe last.** The per-λ vector is now emitted by
> [`binding_reeb_phase_decomposition.py`](../computations/binding_reeb_phase_decomposition.py)
> (`results[atom].by_partition`: `θ_free`, `θ_atom`, `Δθ_λ`, channel) — the
> un-collapsed carrier ready for downstream observation.

### 9.3 The gap, narrowed to one item

> **🛑 CURRENCY (2026-09-08) — the 2026-08-30 block below stands; four things landed after it.** (1) The derived binding object is now the **log functional** `B = E₀·ln(tr_M(β_free)/tr_M(β_atom))` ([2026-09-05 arc synthesis](audits/2026-09-05-binding-law-arc-synthesis.md)); `B = scale·Δtr` is refuted algebraically (`Δtr/tr_free → 1` by A = 11). (2) The 3-body sign in the table below is a **structural exclusion, not a shortfall to tune**: both corpus assemblies are proved incapable of `b₃ > 0` (`QOU.MassTheory.MayerThreeBodySign` for the multiplicative `W = 1 − ∏f` with `f_pn ≤ 2/3`; the pairwise-additive log gives `b₃ = 0` identically); sibling PR #7155 (open) adds no-bulk for every expressible edge set. (3) Knot / census selection is excluded as a route (owner ruling 2026-09-05, [audit](audits/2026-09-05-binding-route-consolidation-no-knot-selection.md)); braid words are to be selected by γγ pair-production + the confinement SDP at q₀ (owner ruling 2026-09-08, bean `qou-ales`). (4) The programme map is [`audits/2026-09-08-l2-1ppq-research-program-gaps.md`](audits/2026-09-08-l2-1ppq-research-program-gaps.md) §3 (binding) and §7.2 R2; the one open problem is `qou-brng` / `qou-edt7`, with "signs first" running through `qou-vbyi` (diproton).
>
> **🛑 CURRENCY (2026-08-30) — the gate in this section is RE-LOCALISED. It is no
> longer "the per-rep `θ_λ` magnitude" (the row below) nor "the per-depth `α_k`
> assignment rule" (§9.5). Both were superseded on 2026-08-29/30, and the metric
> that produced them cannot see the actual defect. Read this before working any
> row here or in §9.5.**
>
> **The old metric was blind at 3-body.** PROBE 2's lumped ratio
> `1 + |b₄ᶜ|/Σg` compares the 4-body cluster against the 2-body sum and **omits
> the 3-body order entirely** — so a *sign error* at 3-body, averaged against an
> order-of-magnitude deficit at 4-body, reads as a benign "26 % short". The
> matching metric is the Ursell cumulant inversion, which is a *definition* of a
> binding map's body-order content rather than a fit
> ([`2026-08-29-he4-magnitude-shortfall-location.md`](audits/2026-08-29-he4-magnitude-shortfall-location.md),
> canonical convention D, proton pin, mpmath end to end):
>
> | | `b₂` | `b₃` | `b₄` |
> |---|---:|---:|---:|
> | **AME2020 (target)** | 2.224566 | **+1.426222** | +9.243387 |
> | model (D, probe2 typing) | 2.22457 *(the unit)* | **−2.74386** | 2.07699 |
> | model / target | — | **−1.924** | 0.225 |
>
> **The convention leg is closed as an explanation.** Under canonical D the
> lumped enhancement is *farther* from target than under excised C — 0.6664 vs
> 0.7360 — in both `f_pn` typings. The 23 % `z_C → z_D` difference moves the
> answer the wrong way, so the convention is not the missing ingredient
> (scope-(a); this is no argument against D, which is forced independently by
> `markovWeights_eq_jones_of_threeRow_eq_zero`).
>
> **The deficit is present BELOW 4-body**, so looking at ⁴He alone misses it. The
> held-out ³He−³H splitting carries no 4-body content and is untouched by any
> common per-order weight: right-signed in all four convention × typing
> combinations, magnitude short by **2–6×** (D/probe2: model/AME = 0.320).
>
> **Both corpus assemblies are now PROVED incapable of the observed `b₃`.** This
> is the crux, and it is two scope-(b) exclusions, not a numerical shortfall:
>
> | assembly | forces | invariant (all sorry-free on `main`) |
> |---|---|---|
> | multiplicative / Mayer `W = 1 − ∏ f_ij` | `b₃ > 0` requires `f_pn > 2/3`; every measured `f_pn` is below it (largest `z_D = 0.61269`) ⇒ **`b₃ < 0` always** | [`QOU.MassTheory.MayerThreeBodySign.lt_of_b3_pos`](../folio/quantum-observable-universe/lean/QOU/MassTheory/MayerThreeBodySign.lean) |
> | pairwise-additive log `B = −α Σ ln f_ij` | every connected cumulant above 2 vanishes ⇒ **`b₃ = 0` exactly** | arithmetic (uniform `g`: `B(2)=g, B(3)=3g, B(4)=6g`) |
>
> Assembly 1 gives `b₃ < 0`, assembly 2 gives `b₃ = 0`, nature gives `b₃ > 0`.
> And the 2026-08-08 audit §10a **derives** the log form (tr_M multiplicative +
> energy extensive ⇒ Cauchy functional equation ⇒ `f = c·ln x`, "forced"), so if
> §10a stands the corpus is committed to a functional that provably cannot
> reproduce the measured 3-body cumulant. **That tension is the live question**
> — a derivation question, not a fit (bean `qou-edt7`).
>
> **What a replacement assembly may NOT be** (each already proved, so do not
> re-run these): not pairwise-additive (`b₃ ≡ 0`); not multiplicative with
> `f_pn ≤ 2/3` (`b₃ < 0`); not reachable by varying the **edge set**, the
> **like-pair typing**, or the **energy scale** (all three proved sign-irrelevant
> in `MayerThreeBodySign`); not a **per-λ reweighting** (PROBE 4 / #5234 — a
> per-λ re-decomposition of the same Borromean trace reproduces the scalar tower
> to ≤ 6.6e-7); and it must be **arrangement-independent**, which the linear
> chain provably is not at `q ≠ 1`
> ([`ChainBondOrderDependence.orderIndependent_iff`](../folio/quantum-observable-universe/lean/QOU/MassTheory/ChainBondOrderDependence.lean)).
>
> **Three further fences added the same week**, so effort does not go here:
>
> 1. **Milnor `μ̄` and the ⁴He magic surplus** — **RE-SCOPED (b) → (a) on
>    2026-08-30.** The exclusion's premise ("every bonded pair has `lk = 1`") is
>    contradicted by the corpus's own triton model, which puts `lk = 0` on three
>    *bonded* pairs; and on the branch that saves the premise, `M₃(T) = 0` makes
>    the 3-body calibration `e₃` a division by zero. The conditional survives,
>    its hypothesis does not. **Superseded 2026-08-30**: the canonical braid word
>    fixes the interfaces non-uniformly — ⁴He's three are `σ` (+1),
>    `averaged_weighted` (no sign) and `σ⁻¹` (−1) — so the uniform premise is
>    *false*, not merely unestablished. Originally stated as: the physical
>    max-contact tetrahedron `K₄` has all six pairs
>    Hopf-linked (`lk = 1`), so Milnor indeterminacy makes every higher `μ̄`
>    defined only mod `gcd(lk) = 1` ⇒ `M₃_irr = M₄ = 0`, and the tower supplies
>    nothing beyond `M₂ = 6`. It does **not** touch the non-link-invariant SU(4)
>    `[1⁴]` shell object, which is the surviving candidate for that surplus.
>    ([audit](audits/2026-08-29-gap2-he4-milnor-indeterminacy-exclusion.md))
> 2. **`w_3` is a required boundary condition of a rank-2 problem, not a
>    computable output.** `no_scalar_kernel_on_carrier` (sorry-free): the
>    q-Borel-normalised carrier is pure isoclinic of Newton slope `1/2`, every
>    rank-1 q-difference module has integer slope, and `2u − 2p = 1` is
>    unsolvable over ℤ — so no scalar `R(q,x)` acts on the carrier at **any**
>    depth. A rank-2 recursion needs two base cases and the corpus supplies one
>    (n=2). Four routes to a second were measured and none closes; the one route
>    nothing excludes is the **ramified double cover** (adjoin `q^{1/2}, x^{1/2}`,
>    slope becomes 1). ([audit](audits/2026-08-29-w3-closeability.md), bean `qou-v8qx`)
> 3. **The complete graph cannot saturate**, so it is structurally excluded for
>    heavy `A` — only a bounded coordination number gives the observed finite
>    `B/A` plateau (`complete_graph_no_saturation` /
>    `bounded_degree_saturates`, sorry-free).
>    ([audit](audits/2026-08-30-coordination-saturation-formalized.md))
>
> **One upstream contradiction to settle before pricing any per-order weight.**
> `prop:prolonged-periods-fixed-depth` asserts an **n-independent** kernel, while
> `a_D^(n) = I(n)/n` grows **super-exponentially**; a constant-coefficient
> recurrence of depth `d` obeys `|a_n| ≤ M·Kⁿ`, so at most one of the two holds.
> The tell sits in their own load-bearing step — `I(n+2) = I(n+1) + (n+1)·I(n)`
> has the `n`-dependence in the coefficient. This is the **second** independent
> crack in that proposition; the first, `no_equivariant_prolongation` (merged),
> reaches it from equivariance instead of growth. Until it is settled, the
> question *"does a depth-≤8 Bring Gauss–Manin recurrence admit
> `a₂ : a₃ : a₄ = 1 : −0.52 : +4.45`?"* (bean `qou-i5yp`) may be moot. Bean
> `qou-9yqb`.
>
> **Downstream cost of the open gate, so the priority is legible:** ⁴He
> under-binds 3.26× on the production form, and **D + T → ⁴He + n comes out
> endothermic** (−0.29 MeV against +17.59 observed) in every current form,
> because a fusion Q-value is a small difference of same-order bindings and
> amplifies per-isotope error without mercy
> ([gap map](audits/2026-08-29-mass-provenance-breakdown-and-gap-map.md) §4).

| Quantity | Status |
|---|---|
| Mirror-pair **differences** (³H/³He, A=3) | 🟡 **partial — signed structure real, magnitude not derived.** The bar-symmetric `(χ^λ + χ^{λᵀ})/2` isospin-mirror combination IS the signed per-block object the volume side proved necessary (#1709 T/³He obstruction), but its best *structural* result is ≈ 2.52 %. The widely-cited **0.11 % is a fitted `(1+q)/2` (CAL-4) near-match**, and is **stale** (canonical q₀ → +0.12 %). Not a derived closure. ([discipline assessment](audits/2026-05-31-isospin-mirror-v9-discipline-assessment.md)) |
| Deuteron **absolute** binding | 🟢 derived twice: `m_e·Vol(𝓑₃)·Δtr` (+0.19 %) and `μ₀·ℏ_q·J_q²(j=1)` (−9 %), `μ₀` derived |
| **A≥3 absolute** binding | 🔴 **the open gate — but NOT where this row used to say.** ~~needs the full per-rep `θ_λ` magnitude~~ is **superseded**: PROBE 4 measured that a per-λ re-decomposition of the same Borromean trace reproduces the scalar tower to ≤ 6.6e-7, so the missing content cannot be a per-block weight at all. The gate is the **assembly functional**, and both corpus assemblies are proved incapable of the observed `b₃ > 0` — see the currency banner above. |

**Trace-canonical residual (2026-06-09).** On the trace-canonical path the
whole 9b gap collapses to a near-integer q₀-power, `Δ_λ(K) ≈ q₀^(10A−5)`
(D exact to 0.01 q₀-units, T −0.07, ⁴He +0.27; ³He −1.40, Z-dependent) —
near-match tier, NOT wired
([residual audit](audits/2026-06-09-delta-lambda-canonical-residual.md)).
**RESOLVED 2026-06-29** (landed on main while PR #3200 was in flight):
refuted-as-global at A≥5 (⁶Li measures 36.1 vs predicted 55) yet
derived-as-bookkeeping `10A−5 = 5·(2A−1)` over chain units, Lean sorry-free
(`QOU/Mass/BindingResidualExponent.lean`,
`QOU/BraidKnot/DeltaLambdaExponentKeystone.lean`;
[synthesis](audits/2026-06-29-delta-lambda-residual-synthesis.md)); the
per-site "5" is a B_pred-linearization artifact. Surviving open legs: the
bar-odd Z-correction κ = b/4 ≈ −0.437 and the IMME `Δ³=0` checks — see the
§0 9b row. PROBE 1 below (run independently the same week) confirms the
linearization-artifact reading from the exact-degree side.

> **PROBE 1 verdict (2026-07-02) — bookkeeping route REFUTED, scope-(a).**
> The `10A−5 = 5·[A nucleons + (A−1) interfaces]` factorization does NOT
> come from closed-form Laurent-degree bookkeeping: exact degrees and
> writhe differences are nowhere of that form, and the closed form's
> trace-side contribution *shrinks* with A (4.97 → 0.88 in log-q₀ units,
> D → ⁴He) while the law grows +10/nucleon. Constrains this route only —
> no ingredient excluded. **Observation tier (near-match, unwired):**
> `h(q₀) = q₀^(−15.0002)` — the deuteron exponent is `−log_q₀ h` to
> 2e-4 relative, i.e. `Δ_λ(D) ≈ 1/h(q₀)`; and the ³He −1.40 outlier
> decomposes as p/n-trace asymmetry +1.372 (dominant) + interface-sign
> swap −0.938 + AME mirror +0.904. Hardening byproduct: the Phase-5q
> closed form is now verified as an **exact ℚ identity** (symbolic
> H₆/H₉, 11/11 assertions).
> [Probe audit](audits/2026-07-02-9b-probes-laurent-degree-manybody.md),
> `probe_9b_laurent_degree_10a5.py`.

> **Follow-ups (2026-07-03, PR #3247).** (i) h-power re-parametrization:
> the residual law reads `Δ_λ(K) ≈ h(q₀)^(−(2A−1)/3)` (the h-exponent
> carries the 1/3); adding the derived asymmetry κ = log_q₀(tr_n/tr_p)
> as a proton-excess gate collapses the ³He outlier +1.40 → +0.033 at
> A=3 (`probe_9b_h_power_asymmetry.py`). (ii) **Gate refuted as a generic
> rule, scope-(a)** (`probe_9b_gate_interface_algebra.py`): the exact
> mirror decomposition `gap = asym + swap + mirror` is proved as an
> identity (≤1e-30), and the A=3 swap/mirror near-cancellation (−0.938 +
> 0.904 = −0.034) is A-specific — swap decays geometrically with A while
> the mirror term stays O(0.4) (⁷Li/⁷Be: +0.394) — so M3 stays a
> near-match at A=3 only. (iii) **Interface-factor algebra Lean-proved
> sorry-free** (22 theorems, generic field, `q = s²`, no ℝ:
> [`QOU/Hecke/ClosedFormInterfaceFactors.lean`](../folio/quantum-observable-universe/lean/QOU/Hecke/ClosedFormInterfaceFactors.lean)
> — factor algebra, bar-involution behaviour, δ cubic factorization,
> assembly product, Markov trace bridge); the cross-level `H_{3A}`
> bond-word induction remains sympy-verified only (the honest boundary).
> *Complement note (2026-07-06):* the **abstract fold** form was already
> formalized in `interface-knot-markov-z.lean` (bean-`s1ik` subsumption,
> PR #3329, + the Phase-5l constituent multiplicativity proved
> separately); the explicit module above adds the named factors with
> δ(q), per-factor bar behaviour, and the `MarkovBondFactor` bridge —
> cross-cited both ways, no duplication.

**9a flip gate (owner ruling, 2026-06-13).** Production stays on the
uniform shortcut until the per-A normalisation `R(K)` — the same object as
the 9b ρ/Δ_λ leg — is derived; the flip is a *derivation milestone*, not a
wiring choice, and flip+re-pin is **refuted** (`R(K)` runs 2.3→63× with A;
[decision package](audits/2026-06-13-step9a-flip-decision-package.md)).
Do not re-litigate per-knot production flips against this gate. (Post
2026-06-24 this gate governs the **binding-side** wire-up; absolute mass
routes through `canonical_mass.py` regardless.)

**The narrowed compute item (REFRAMED 2026-06-02 — intensive vs extensive).**
A zero-fit derivation ([`2026-06-02-binding-intensive-vs-extensive-derivation.md`](audits/2026-06-02-binding-intensive-vs-extensive-derivation.md))
settles the framing: the canonical binding `B = E_0·(|tr_M_free| − |tr_M_atom|)`
is **INTENSIVE** — the trace difference *saturates* at ~3–4 MeV. The deuteron
(one inter-nucleon bond) is **derived to +3.6 %**, but A≥3 collapses (derived
A-growth 1.65× vs AME 12.72×). **Nuclear binding is EXTENSIVE (`∝ A`)**, so the
canonical trace-difference formula is **structurally missing the additive term**.

**Consequence — the Δ_λ gate was mis-framed.** No per-block *weight* `Δ_λ` can
turn an intensive quantity extensive (which is *why* the six prior ansätze + the
2026-06-02 probe series — volume, rotation/full-order `θ_λ`, content-energy,
content×phase — all failed). The closure is **not a density to multiply**; it is
an **additive sum over inter-nucleon bonds**:

$$B(K) = \sum_{b\,\in\,\bowtie_K} B_b,\qquad B_b = E_0\,\Delta|\mathrm{tr}_M|_b
\ \text{(the derived single-bond piece; deuteron = the base case)}.$$

Bond count `C(A,2)` already gives A-growth 6× (vs the intensive 1.65×); the
residual 6×→12.72× is the **per-bond growth** (each bond embedded in a denser
braid). The open compute item is therefore: **enumerate the `⨝_K` bonds and
derive each `B_b` from its embedded sub-braid trace difference** (the deuteron is
`n=6` base case, derived). This is a *derivation* (sum of derived pieces over the
structural bond set), the natural job of the operator-valued combiner (#1698) —
not a weight-fit. Tracking:
[`2026-05-28-binding-endomorphism-analogy.md`](audits/2026-05-28-binding-endomorphism-analogy.md),
Δ_λ gate context [`2026-05-18-delta-lambda-gating-context.md`](audits/2026-05-18-delta-lambda-gating-context.md),
inter-nucleon bonds [`inter-nucleon-channel-color-tube.md`](../folio/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md).

**Update (2026-06-03) — the gate dissolves into a many-body series; the 4-body
term EXISTS.** The pairwise bond-sum has a ceiling: the canonical braid is a
**chain of A−1 interfaces** (verified), and the pairwise chain-sum captures only
**26 %** of ⁴He's binding ([`2026-06-02-binding-many-body-ceiling.md`](audits/2026-06-02-binding-many-body-ceiling.md)).
The 74 % residual is irreducible **many-body** binding — and the **4-body α term
already exists** as the sibling's canonical **magic-A** formula
`B(⁴He) = 2·m_e·A·Vol(L6a4) = 2·m_e·4·8G` → **+5.87 %, no fit**
([`2026-06-02-he4-binding-canonical-vs-full-theta-design.md`](audits/2026-06-02-he4-binding-canonical-vs-full-theta-design.md),
branch `he4-jsj-binding-link`). So the binding is a **many-body series**:

| body order | structure | regime | result |
|---|---|---|---|
| **2-body** | pairwise bond-sum (per-bond `E_0·Δtr_M`, abs convention) | A≤3 | correct T/³He ordering; A=2 derived |
| **3-body** | A=3 residual (the ~40 % pairwise gap) | T, ³He | **open** (whole-A link-volume — §below) |
| **4-body** | whole-α volume `2·m_e·A·8G` (magic-A) | ⁴He | **+5.87 %, no fit** |

> **PROBE 4 verdict (2026-07-02) — per-λ collapse-last tower REFUTED,
> scope-(a); one invariant-backed exclusion; one convention finding.**
> Normalized collapse-last per-λ towers (Jones, Wenzl, ambient-H₆ per-ν
> via exact MN/LR branching) all converge ∀Z, preserve the shape, and
> **reproduce the scalar tower to ≤ 6.6e-7** (¹⁶O err 2.2752 → 2.2752;
> Jensen gap over the block spread is O(10⁻⁶)) — the missing Δ_λ weight
> **cannot be a pure re-decomposition of the same Borromean trace**; it
> must carry new per-block content (volume enrichment / knot-ideal
> projector — GAP-A-3/A-4). Raw (unnormalized) per-block tower is
> **EXCLUDED (invariant-backed)**: `χ^{(2,1)}² ≈ 3.977 > q₀` exceeds the
> proved Li₂^q radius. **Convention finding (DERIVED, 9e-72):** the
> pipeline's τ closed form is the **SU(2)/Temperley–Lieb (Jones)** Markov
> decomposition (`y₃ = [4]/[2]³, y₂₁ = 1/[2]², y_{(1³)} = 0`), NOT the
> corpus-canonical Wenzl z-trace (τ_W ≈ 0.9983666, gap 1.955e-4) —
> **registered as convention D** in the trace-convention registry
> ([convention-split audit, 2026-07-02 addendum](audits/2026-06-09-binding-trace-convention-split.md)):
> sub-0.1 % binding claims must state their trace convention.
> [Probe audit](audits/2026-07-02-9b-probes-alphak-perlambda-tower.md),
> `probe_9b_perlambda_brane_tower.py`.

> **PROBE 3 verdict (2026-07-02) — "4-body cross-term ≈ magic-A" REFUTED,
> scope-(a).** The exact finite inclusion–exclusion expansion of the
> Phase-5q product form (`B = Q_β·tr_free·[Σg_i − Σg_ig_j + …]`, sums to
> B_pred at 1e-40) is **alternating and non-perturbative** (g ≈ 0.50–0.71;
> ⁴He order-1 = +192.6% of B_pred, order-2 = −115.4%, order-3 = +22.8%),
> and the **connected 4-body cross-term at ⁴He is 0.16 MeV (Q_β scale) /
> 0.87 MeV (E₀ scale) — 34–184× below the magic-A 29.96 MeV**. The probe
> measures the size of the missing higher term; no factor is excluded.
> Consistency hook: order-1 at E₀ scale = **25.98% of B_AME**, exactly
> reproducing the many-body-ceiling audit's 26% pairwise figure.
> [Probe audit](audits/2026-07-02-9b-probes-laurent-degree-manybody.md),
> `probe_9b_manybody_expansion.py`.

**Common shape, per-isotope scale/assignment.** The deuteron (`m_e·Vol(6₂)`,
+1.1 %), the deprecated census A=3 (`2·m_e·Vol`, knot 8₁₁/Borromean), and magic-A
⁴He (`2·m_e·A·8G`, +5.87 %) all share the **shape** `(scale)·m_e·Vol(link)` —
but the scale (`ρ`, the `A` factor) and the link assignment **vary per isotope**
and are **not yet derived** (this is the residual heuristic/fitted aspect, NOT a
single law). The open items are therefore: (i) the **canonical link-volume
assignment** per nucleus (deuteron `6₂` is fixed; A=3/A=4 assignments are
heuristic-or-magic); (ii) the **scale rule** `ρ·A` (why ρ=1 at A=2 but ρ=2·A at
A=4); (iii) **reconciling** the pairwise (2-body) and whole-nucleus (4-body)
decompositions into one additive many-body series. The Δ_λ gate is dissolved —
it was never a per-block density — but the many-body series is not yet a closed
single form; the 4-body ⁴He piece (magic-A) is its most-derived member at +5.87 %.

> **🛑 CURRENCY (2026-08-29 OWNER RULING A) — the deuteron member of that shape
> family is RETIRED. The paragraph above says "deuteron `6₂` is fixed"; it is
> not, and the deuteron is no longer a volume term at all.**
>
> The deuteron knot is the **canonical braid closure** (trefoil / Hopf),
> **Vol = 0** — two of the three routes give zero, and only the census *lookup*
> gave `Vol(6₂) ≈ 4.40083251612`. The `6₂` census assignment is **retired**, and
> the explicit corollary of the ruling is that **the deuteron binding is NOT a
> hyperbolic-volume term** (the Bloch volume leg is proved 0, PR #5242). So
> open item (i) no longer reads "the deuteron is fixed, A=3/A=4 are heuristic":
> the deuteron is *excluded from the volume shape*, which removes the family's
> one supposedly-settled member.
>
> The obvious replacement was tested and failed: sourcing the binding from the
> **Gram/Frobenius pairing + confinement SDP** (`deuteron_real_sdp.py`, H₆) is a
> **scope-(a) negative** — the diagonal Gram SDP is degenerate and 0 of 6
> off-diagonal encodings derive the binding; the single non-zero result
> (`2.22456607`) is the AME value fed in as the constraint, i.e. circular. Same
> intensive-vs-extensive gap as everywhere else on this front.
>
> Rulings and measurements:
> [deuteron-knot owner decision](audits/2026-08-29-deuteron-knot-owner-decision.md),
> [Gram-SDP compute](audits/2026-08-29-deuteron-binding-via-gram-sdp-compute.md),
> consolidated arc ledger
> [bk-crossing reassessment](coordination/2026-08-29-bk-crossing-mass-binding-arc-reassessment.md).
> Note that ledger also flags the exact-`ℏ_q²` saturated-fraction value as
> **suspect numerology** (`qou-brng`) — do not chase it.

> **⚠ CURRENCY (2026-08-10) — item (ii) is NOT independently open; it is gated on
> `conj:s5-so3-fiber-action`. Do not open a scale-rule probe.** The list above
> predates the **GAP-A-4 final retrospective (2026-06-05)**, which closed that
> axis. Four transplant routes for the per-atom multiplier `λ(K)` were tested and
> **all refuted** — Phase-4 carrier (−56 % to +106 358 %), `Vol(K)` convention
> choice (best swing +132 %), additive `S(K)` under uniform `λ` (100× swing),
> bar-symmetric q-Pochhammer (−98 %). Per-knot `Vol(K)` as a **standalone** fix is
> closed **negatively**. And `ρ·A` is not free-standing: the binding generating
> function `G(x;q) = Σ Bₙxⁿ` satisfies a fibre-level q-difference equation whose
> τ-image at real `q₀` is named as fixing **both** the per-order terms **and** the
> scale rule `ρ·A`. Mass-side and binding-side reach this independently, so the
> framework's open derivation math on this axis is **one categorical conjecture**.
> Re-running a scale-rule probe repeats R1–R4.
>
> Items (i) and (iii) survive as genuinely open, but **downstream of** that
> conjecture rather than independent of it.
>
> Read first: [`2026-06-05-gap-a4-final-retrospective.md`](audits/2026-06-05-gap-a4-final-retrospective.md)
> §2–§5; ledger [`s5-so3-keystone.md`](coordination/s5-so3-keystone.md).
> History: this staleness was caught when an agent (PR #4939 follow-up) read this
> passage, called (ii) "bookkeeping, not mechanism" in a delivered analysis, and
> was about to probe it — exactly the already-closed-but-declared-open pattern the
> AGENTS.md corpus-grep checklist exists to prevent, reaching a reader through the
> designated coordination hub.

### 9.4 Lean formalization debt (tracked — verification, NOT a compute gate)

The §9.1 partition-respecting objects are **already wired and numerically
cross-validated in compute** (Wenzl bridge n=3,4,5; `lp_dual_solver.py`; the
1ppb cross-check). The math is **classical and published** — the gap is only
that it isn't ported to Lean/Mathlib yet. **These do NOT block compute** (the
only compute gate is §9.3's full-order `θ_λ`); they are tracked here as
verification-debt for the proof-watcher / a Lean session (lake required).

| # | Statement to formalize | Target Lean | Classical ref | Status |
|---|---|---|---|---|
| **L-1** | Schur character-orthogonality on `H_n(q)` ⇒ `y_λ` uniqueness (`Σ_λ y_λ χ^λ = z^{ℓ(w)}` invertible at generic q) | `QOU.Hecke.Wedderburn` / `wedderburn-as-noncomm-fourier.lean` | Mathas (1999) §3.43; not in Mathlib | 🔴 debt |
| **L-2** | Central-idempotent orthogonality `π_λ π_μ = δ_{λμ} π_λ` (currently a class axiom) | `QOU.Hecke.Wedderburn` (`WedderburnDecomp`) | Mathas (1999) §3.43 | 🔴 debt — **n=3 groundwork landed 2026-07-03**: explicit π_λ coefficients on the 6-word basis, exact in ℚ(q), all four class axioms + tr_C values verified (`probes/probe_h3_central_idempotents_exact.py`, 4/4); ready for Lean transcription into a concrete n=3 `WedderburnDecomp` instance |
| **L-3** | Per-λ Frobenius block-orthogonality `⟨a,b⟩_F = ⊕_λ ⟨a,b⟩_F^λ` | module `QOU.Hecke.Wedderburn`, decls `QOU.Hecke.WedderburnDecomp.frobPairing_block_decomp` + `.frobPairing_block_orthogonal` | follows from L-2 + `def:frobenius-hopf-substrate` | 🟡 **formalized 2026-07-03** (sorry-free, `lean`-direct exit 0), conditional on the `WedderburnDecomp` class — the docstring-promised centrality of `π_λ` is now an encoded `central` field, and both L-3 statements are *derived* from `complete` + `central` + `idempotent`/`orthogonal`. Residual debt = discharging those class axioms from the Hecke structure, i.e. exactly L-1/L-2 (Mathas §3.43) |

These three close the "ASSUMED" entries in the §9.1 table. They are the
canonical chain's standing Lean backlog; pick them up in a lake-enabled session
(per AGENTS.md §1, every resulting `sorry` carries a `-- Ref:` citation until
discharged). Proof-watcher: route under the proof-integration-watcher queue.

### 9.5 The 6-knot multiplicative closure (tower interpretation)

Step 4 of the canonical chain establishes **6 H_3(q) basis elements**:

```
{ 1, σ_1, σ_2, σ_1σ_2, σ_2σ_1, σ_1σ_2σ_1 = σ_2σ_1σ_2 }   ← Bring χ_eu(M₀) = 2 − 2g(M₀) = −6
```

A recurrent agent confusion is reading "6 basis elements" as **6 independent
SM-equivalent operators** that each contribute one slot of binding. That is
**wrong**: the 6 are **GENERATORS** of `H_3(q)` — the full binding spectrum is
the **multiplicative closure** of these generators climbing the **GB filtration /
jet tower** of Steps 7-8:

| GB depth k | tower layer | element class | count |
|---|---|---|---:|
| 0 | identity | `1` | 1 |
| 1 | length-1 | `σ_1, σ_2` | 2 |
| 2 | length-2 | `σ_1σ_2, σ_2σ_1` | 2 |
| 3 | length-3 (center) | `σ_1σ_2σ_1 = σ_2σ_1σ_2` | 1 |

Total: **6** — same 6 H_3 basis elements, viewed as the tower closure.

For atoms with `A ≥ 2`, the full braid lives in `H_{3A}` and the tower
extends to depth `3A − 1`. Each **depth band** `J^k / J^{k+1}` contributes
binding via the **depth-stratified canonical compute** (§9.5.1):

$$B(K) \;=\; m_e \cdot \sum_{k\,\geq\,0} \alpha_k \cdot
\sum_{w\,\in\,J^k/J^{k+1}}
y_w \cdot \bigl(\chi^\lambda_{\text{free}}(w) - \chi^\lambda_{\text{atom}}(w)\bigr).$$

So the binding spectrum is **NOT** 6 standalone contributions — it is the
sum over the whole tower closure, of which the 6 basis elements are the
generating set at depth ≤ 3.

#### 9.5.1 Canonical default compute

The default binding-energy compute IS the depth-stratified tower sum:

- **Production**: [`binding_depth_stratified_rust.py`](../computations/binding_depth_stratified_rust.py)
  (full H_{3A} via Geck-Pfeiffer + Hoefsmit Rust kernel, n ≥ 9)
- **LR variant** (per-nucleon H_3 → H_{3A} combiner for A ≥ 4):
  [`binding_depth_stratified_lr.py`](../computations/binding_depth_stratified_lr.py)
- **Python fallback**: [`binding_depth_stratified.py`](../computations/binding_depth_stratified.py)

α_k coefficients (NOT empirical fits):
- α_0 = α_1 = α_3 = 1 (trivial layers)
- α_2 = z² ≈ 0.2493 (Markov braid-trace marker²) — **🛑 convention-C
  frame, in both spelling and value; see the scope note below**
- α_{k≥4} = m_e · 8G ≈ 3.7445 (Vol(L6a4) Borromean plateau)

> **🛑 CONVENTION SCOPE (added 2026-09-03) — the α₂ line above is
> convention C, sitting in the canonical-default compute section.**
> It was written `z = 1/(√q + 1/√q) = √q/(q+1)`, which is the Markov
> parameter of **convention C**; the 2026-08-15 owner ruling (R1) makes
> **convention D** (`z = q³/(q²+1)`) canonical and excises C. At the
> proton q₀ the two differ by more than a factor of 1.5 in α₂:
>
> | frame | z(q₀) | α₂ = z² |
> |---|---|---|
> | **C** (as written above) | 0.499320334184 | **0.2493207961** |
> | **D** (canonical since 2026-08-15) | 0.612688037146 | **0.3753866309** |
>
> **Do NOT simply substitute 0.3754 and call it migrated.** Per the
> standing discipline, a C-frame result is *correct for C* and needs
> **scoping**, and a z-swap is not by itself a valid re-derivation —
> the depth-stratified functional's α_k assignment has to be re-derived
> in the D frame, and whether the PROBE-2 `z^k`-series structure below
> survives that is exactly what is *not* yet established. Until it is,
> read every α₂-dependent number in this section as **C-conditional**.
> Tracked with the rest of the D migration (`qou-cds1` family).

> **PROBE 2 verdicts (2026-07-02) — assignment-rule structure checks**
> ([probe audit](audits/2026-07-02-9b-probes-alphak-perlambda-tower.md),
> `probe_9b_alphak_structure.py`):
> - **DERIVED (exact):** the Markov-marker series `z^k` **breaks at k=3
>   structurally** — `χ^{(2,1)}(σ₁σ₂σ₁) = 0` exactly (Δ² is the central
>   full-twist scalar and `det ρ_{(2,1)}(Δ) = −1 < 0` forces
>   tracelessness), so `tr_M(T_Δ) = z + h·z² = z·(1 + q^{1/2} − q^{−1/2})
>   ≈ 0.5514 ≠ z³`. The break is forced, not assigned.
> - **REFUTED-(a):** "because Δ is central" as literally stated (Δ is not
>   central in H₃; Δ² is). **NEAR-MATCH (10.4%):** the value α₃ = 1 itself
>   — the collapsed weight is `1 + q^{1/2} − q^{−1/2} ≈ 1.1044` at q₀,
>   exactly 1 only as q → 1.
> - **REFUTED-(a):** the plateau resummation `Σ_{k≥4} z^k·N_k = m_e·8G` —
>   fails under all 4 layer-count readings × 4 atoms; sharpener: the tail
>   is strongly **A-dependent** while the plateau is A-independent, which
>   kills the whole per-atom layer-count family.

Current state (per witnesses 2026-06-09 — full audit at
[`docs/audits/2026-06-09-binding-canonical-default-depth-stratified.md`](audits/2026-06-09-binding-canonical-default-depth-stratified.md)):

| atom | tower B_pred | B_AME | ratio |
|---|---:|---:|---:|
| D | 0.607 MeV | 2.225 | −73 % |
| T | 2.808 MeV | 8.482 | −67 % |
| ³He | 2.653 MeV | 7.718 | −66 % |
| ⁴He | 14.063 MeV | 28.296 | −50 % |

LR and Rust direct now agree to 3 dp across all four atoms (verified
post-regen 2026-06-09). An earlier session reported a 4× LR vs Rust
disagreement on ⁴He (LR 2.089 vs Rust 0.497); this was 100 % an
artifact of a stale binding witness consuming a 24/77 partial cached
⁴He atom chi witness, since resolved. See the audit doc §Prevention
for the partition-completeness gate added to prevent recurrence.

**Tower sum does NOT close binding at the 10 % threshold.** The flat
**magic-A** formula `B(⁴He) = 2·m_e·A·8G` (+5.87 %, §9.3) BEATS the
depth-stratified tower on ⁴He (-50 % Rust direct). The unclosed gap
is in the **per-depth α_k ASSIGNMENT RULE** (which structural
constant goes to which k, why α_3 = 1 breaks the Markov-marker
series, why α_{k≥4} plateaus at m_e·8G) — NOT in the LR-vs-Rust
choice.

> **🛑 CURRENCY (2026-08-30) — the α_k assignment rule is no longer the named
> unclosed gap.** The paragraph above is kept as the record of what the tower
> measures; the *diagnosis* in its last sentence is superseded by the §9.3
> currency banner. The defect is one order lower and one level up: the model's
> connected **3-body** cumulant is **wrong-signed** (`−2.744` against AME's
> `+1.426`) under every convention × bond-typing combination tested, and that
> sign is forced by the assembly functional rather than by any per-depth
> coefficient — proved for the multiplicative form
> (`MayerThreeBodySign.lt_of_b3_pos`) and by arithmetic for the pairwise-additive
> log form (`b₃ ≡ 0`). Re-running an α_k assignment variant cannot move a
> quantity that is sign-fixed upstream of it. Two further §9.5-adjacent routes
> are separately fenced: reading the **magic-A formula as the n=4 term** rather
> than as the total determines `w_3` **negative** and predicts *unbound tritium*
> (−1.66 MeV), scope-(a) against that reading only
> ([w₃ audit](audits/2026-08-29-w3-closeability.md) R4); and the **depth-2 SL₂
> route to `τ`** is measurably circular — substituting any value for `a_D^(3)`
> leaves the `a_D^(4)` residual at 0.0 to full precision, so `τ` carries no
> information about it (same audit, R2).

**Agent guidance for binding compute:**

1. ✅ DO use `binding_depth_stratified_rust.py` (or LR variant for A ≥ 4)
   as the **default canonical compute** — cite the witness JSON.
2. ✅ DO cite `canonical_status = canonical-with-empirical-assignment`
   when reporting binding numbers — flags the unclosed assignment-rule gap.
3. ✅ DO report `B_pred / B_AME` ratio alongside any number.
4. ❌ DO NOT invent new closure formulas (Coulomb correction, cross-
   isotope bar-symmetric, etc.) without first checking §9.3 + the
   audit doc. The Δ_λ gate is mis-framed; CAL-4 numerology is forbidden
   (cheat sheet §9.3 + isospin-mirror discipline assessment).
7. ❌ DO NOT re-run an **edge-set**, **like-pair typing**, or **energy-scale**
   variant expecting the 3-body sign to move — all three are proved
   sign-irrelevant (`MayerThreeBodySign`), as is a per-λ reweighting
   (PROBE 4 / #5234). And do NOT propose a functional *chosen because it
   lands `b₃ > 0`*: that is anchor inversion in new clothes, i.e. the
   seventh ansatz under another name.
8. ✅ DO report the body-order cumulants (`b₂, b₃, b₄`) rather than a lumped
   ratio when claiming a binding form works — the lumped metric is blind
   at 3-body, which is where the defect is.
5. ❌ DO NOT treat the +5.87 % magic-A formula as universal binding —
   it applies only to ⁴He's doubly-magic shell.
6. ❌ DO NOT chase the retracted Option E v9 cross-isotope `(1+q)/2`
   0.11 % "closure" — see §9.3 retraction + audit doc.

---

## 10. The 2026-09-15 decisions, and the open mass-binding gaps as of that date (bean `qou-6tdg`)

Owner ask (queued 2026-09-15): make this sheet reflect every decision of that day, and name the specific open gaps rather than gesturing at them. Each row below names the artifact a reader checks; none of the numbers here is new — they are the day's results collected in one place.

### 10.1 Decisions enacted on PR #7426 and #7982 (owner selections A, B, C; "both, distinct symbols"; "go with your recommendations")

| decision | what changed | where to read it |
|---|---|---|
| **A — the four "Euler characteristics" separated by name.** `χ_eu(M₀) = 2 − 2g = −6` (topological, the alternating sum of the base curve's Hochschild homology); `χ(M₀, V) = deg V + rk V·(1 − g)` (sheaf, Riemann–Roch); `dim_q(X) = tr(id_X)` (rigid trace, $q$-dependent, positive); `w(A)` (the Wigner obstruction class) and the global surface contact Euler class `NS(A) = e(ξ) ∈ H²(𝒮, ℤ)` (#7982). The Descartes condition is restated as `g(M₀) = 4`. | `rem:three-euler-characteristics`, `rem:chern-character-and-riemann-roch`, `lem:brings-euler-characteristic` (restated), `notation/notation-collisions.md`; Lean `QOU/Information/EulerCharacteristicOfHochschild.lean` (`hhEuler_bring = −6`), `QOU/Brings/S5CharactersOnBringDeformations.lean` |
| **B — the explicit `K₀ → HH₀ → R` layer.** `def:hochschild-homology`, `def:grothendieck-group-of-a-qou`, `def:chern-character`, and **`dim_q = ev ∘ ch`** proved (`QOU/GrothendieckChern.lean`, `dimQK0_eq_evDimQ_chernCharacter`); `ex:su2-characters-and-quantum-dimension` shows the two evaluations `n+1` and `[n+1]_q` of one character. `rem:categorical-trace-is-the-markov-trace`: the normalised rigid trace of `V^{⊗n}` *is* `tr_M` at `z_D` (`qtrace_rHecke_div` for one generator; the weights `[n−2k+1]_q/[2]_q^n` are quantum Schur–Weyl). `rem:hkr-theorem` states HKR with its hypotheses (commutative, smooth, char 0) — it says nothing about `HH²(𝒰_q, Ad)`. | chapter 1 (quantum-universes) and mass-theory; `rem:trace-ledger` |
| **C — the `HH²` scalar cut from the χ chain; one-dimensionality is the Wigner axiom.** `conj:wigner-axiom` (W1: `dim Obs = 1`; W2: the generator realises `e(TM₀) ∈ H²(M₀; k)`), cited to Wigner's Courant lecture (`wigner1960`); class `QOU.AlgebraicSubstrate.WignerAxiom`. Why it is an axiom and not a theorem: Brown–Zhang duality is cohomology-to-*homology* with a Nakayama twist; a deformation direction lives in `HH²`, not `HH¹`; and at `q = 1` Whitehead's lemmas make the space **zero** (`rem:classical-shadow-of-the-substrate`). Equivariance forces the target into `H²(M₀; k)`: the `S₅`-invariant Hochschild ledger of the base is `k` in `HH⁰`, `k²` in `HH₀`, `0` in `HH², HH¹, HH_{±1}` (`QOU/Brings/WignerTargetEquivariance.lean`). `thm:qou-obstruction-reduction` is conditional on the axiom. | stochastic-mechanics; `docs/audits/2026-09-15-chi-as-a-component-of-the-chern-character.md` §2.4, §12 |
| **D — the regularisation negative recorded, none selected.** `dim_q(A)` for `A = 𝒪_q(SU(2))` is the divergent Peter–Weyl sum `Σ[m]_q²`; ζ-regularised `0`, Hadamard `−1/(q−q⁻¹)²`; `= −6` only at `u² = 1/6` (`QOU/Information/DimqRegularisationIdentities.lean`; probe `dimq_regularisation_schemes_probe.py` 16/16). | `rem:euler-characteristic-of-the-regular-representation` |
| **`tr(id_A)` ruling (owner, same day): it is `dim_q(A)`, $q$-dependent.** The `−6` downstream is `χ_eu`, a different object; not a competing value. | bean `qou-2uf0` (completed); register entry |
| **Bring cone link (finding, owner-gated).** The link of the affine cone over Bring's curve is the circle bundle of `K⁻¹` over the curve, Euler number `−deg K = 2 − 2g = −6 = χ_eu`, infinite `π₁`; the quaternionic model is the cone over the Hopf bundle (Euler number `−1`). The 3-Sasakian description is a local model of the fibre, not the link. Lean `QOU/Brings/BringConeLinkEulerNumber.lean`; the rewording of `lem:bring-cone-reeb-quaternionic-twist` awaits the owner. | bean `qou-rydq` (todo), `rem:spatial-realization-base-generality` |
| **EFT / power counting (attack option 1, owner: "do as suggested"): a clean negative.** Every bond factor is `z_D + d_kind` with `z_D(1) = 1/2`, `d_kind(0) = 0`, so the body-number expansion has a classical floor (`b₃ = −5/8 ≠ 0` at `q = 1`; ε-valuation 0). The framework's ordered expansion is the **jet tower** (ratio `q⁻²`), not body number. Lean `QOU/MassTheory/BondFactorClassicalFloor.lean`; probe 15/15. | bean `qou-olxi`, `rem:body-number-expansion-classical-floor` |
| **Yekutieli's hypotheses made explicit.** Formal parameter vs the real `q − 1`; which theorem the lifting cites (Čech, no nilpotence); smoothness of the base as "`Ω¹(A)` dualisable of constant rank"; characteristic zero for the DG-Lie half. Two rows change wording in definitions and are left for the owner. | `rem:yekutieli-setting-explicit` |
| **The running example's spine.** 35 `ex:*-su2` blocks; 14 back-links repaired; 47 definitions in the three foundational chapters have no SU(2) example, five recommended first. | `docs/audits/2026-09-15-running-example-placement-audit.md`, bean `qou-zq1r` |

### 10.2 The open mass-binding gaps, by name (status as of 2026-09-15; re-check the bean before quoting)

| gap | what is open, precisely | bean | status |
|---|---|---|---|
| **The extensive term.** The super-pairwise additive object that turns the intensive per-block `Δ_λ` into an extensive binding; scaling pruned four ways (saturation, chain order-dependence, body-order depth ≥ 3, `b₃ < 0` on every bond triple); the coefficient/mechanism is open. Now also: the body-number expansion is *not* ε-ordered (§10.1), so no power counting closes it. | `qou-brng` | in-progress |
| **`b₃`'s sign.** Every derived bond scalar is confined to `(0,1)`; a chain needs exactly one bond above 1 (sign-mixed pair = the two-nucleon spectrum); both derived bond families are excluded from supplying it; `σ²` is not the fix (binds the diproton). | `qou-q8vl`, `qou-kj4v`; `qou-82mc` (completed: the sign is a convexity property of the aggregator) | in-progress / todo |
| **The scored element.** `nuc11_interleaved` fails the whole-word Frobenius positivity (reading 3) on `(2,1)` for both nucleons; the replacement is an owner decision; the L2 rows `Q_β / m_n / Δ_pn` are scored on a rejected element. | `qou-99qc` | todo (owner call) |
| **The `c_k` ladder on the ruled base.** Not a `z`-swap (proved); on the `z_D` base no cosine ladder reaches the required factor `> 1` (`F_required = 1.759`), so the live question is the base or the assembly, not the phase. | `qou-cds1` (ladder), `qou-pdix` (phase α, de-prioritised), `qou-iagg` (second re-score) | in-progress / in-progress / todo |
| **The Gram singularity under D.** `pyhecke.gram.z` is settled by the convention ruling; the singular Gram matrix at `z_D` is a numerical blocker, not a convention question. | `qou-cds2` | in-progress |
| **The Plancherel numerator.** `dim_q²/[n]_q!` vs Molien's `f^λ dim_q(λ)` (sums to `[n]_q!` exactly, Lean); the `y_lambda` conflation audit is wired blocking; the choice moves the sign of `P_total` at `A = 3, 4`. | `qou-oots`, `qou-za3q` | in-progress |
| **Braid-word selection.** Every canonical word via γγ production + confinement SDP at `q₀`, never census; reading 3 whole-word; the γγ half reaches 6 of 11 letters. | `qou-ales` | in-progress |
| **Deuteron knot.** Canonical braid closure, `Vol = 0`; binding is not a hyperbolic-volume term; three inconsistent assignments blocked the Bloch-group magnitude. | `qou-e5jf` | todo |
| **Tetraplectic structure.** Vacuous at `m = 1` (a volume form); reaches SU(2), not SU(3), and that SU(2) is already spent. | `qou-8p1g` | in-progress |
| **The Wigner axiom itself.** `dim Obs = 1` at `q ≠ 1` is assumed; no computation of `HH²(𝒰_q(𝔤), Ad)` at the substrate parameter exists in the corpus; at `q = 1` the space is zero. What would settle it: that computation (twisted theory, Hadfield–Krähmer), or a derivation of the line from the axioms. | `conj:wigner-axiom`; `qou-mjt3` (Lean ledger, now written) | conjecture |
| **A derived-level archimedean realisation.** The fibre functor lands in `Vect`; no kernel on `Spec(A) × M₀`, so no Fourier–Mukai trace map and no application of Orlov. A definition to be made. | `rem:fourier-mukai-and-orlov` | open direction, no bean |
| **The link lemma rewording.** Owner-gated content change (options on the bean). | `qou-rydq` | todo (owner call) |

**What is NOT on this list, on purpose:** the substrate derivation of `q₀` (forever gated, 2026-08-02), a fourth calibration constant (banned), and any per-case dispatch or selection against the AME/CODATA target (banned). A route through any of them is not a gap to close; it is a route to refuse.

---

## See also

- [`pre-archimedean-derivation-chain.md`](../folio/quantum-observable-universe/mass-theory/pre-archimedean-derivation-chain.md) — paper-side rendering of this chain
- [`DERIVATION-CHAIN-METHODOLOGY.md`](../computations/DERIVATION-CHAIN-METHODOLOGY.md) — compute-side discipline
- [`docs/precision-goals.md`](precision-goals.md) — L1 vs L2 precision targets
- [`docs/duality-tracker.md`](duality-tracker.md) — coordinate-side classifier of every duality the framework uses or could use (D1-D24); status flags + closure paths; sibling-coordination index
- [`docs/audits/2026-08-30-magnitude-gate-is-the-assembly-five-fronts.md`](audits/2026-08-30-magnitude-gate-is-the-assembly-five-fronts.md) — **read first on this axis**: both corpus assemblies proved incapable of `b₃ > 0`; the double cover measured and not closing; SU(4) `[1⁴]` the surviving non-link-invariant candidate (its sign-capability is analytic and discriminates nothing — corrected 2026-08-30); the `M_n(K)` blocker stale under the Option-A ruling
- [`docs/audits/2026-08-29-he4-magnitude-shortfall-location.md`](audits/2026-08-29-he4-magnitude-shortfall-location.md) — **the current magnitude localisation**: Ursell body-order inversion; the model's `b₃` is wrong-signed under every convention × typing; the convention leg closed as an explanation; held-out ³He−³H splitting short by 2–6×
- [`docs/audits/2026-08-29-w3-closeability.md`](audits/2026-08-29-w3-closeability.md) — `w_3` is a rank-2 boundary condition, not a computable output; four routes measured, the ramified double cover the only one unexcluded
- [`docs/audits/2026-08-29-gap2-he4-milnor-indeterminacy-exclusion.md`](audits/2026-08-29-gap2-he4-milnor-indeterminacy-exclusion.md) — **RE-SCOPED (b) → (a) 2026-08-30**: originally a structural exclusion (Milnor indeterminacy on a max-contact cluster); its uniform-`lk` premise is contradicted by the canonical braid word, so the conditional survives and the exclusion does not
- [`docs/audits/2026-08-30-coordination-saturation-formalized.md`](audits/2026-08-30-coordination-saturation-formalized.md) — complete-graph coordination cannot saturate; bounded degree is the forced regime
- [`docs/audits/2026-08-29-mass-provenance-breakdown-and-gap-map.md`](audits/2026-08-29-mass-provenance-breakdown-and-gap-map.md) — provenance ladder + the G1–G8 expected-gap map; why every fusion channel through ⁴He currently has the wrong sign
- [`docs/audits/2026-06-09-binding-canonical-default-depth-stratified.md`](audits/2026-06-09-binding-canonical-default-depth-stratified.md) — depth-stratified `Σ_k α_k Φ_k` is the canonical binding default; α_k structural (z² Markov + m_e·8G Borromean), per-depth assignment rule is the unclosed gap
- [`docs/audits/2026-05-24-magic-shell-gs-filtration-exploitation.md`](audits/2026-05-24-magic-shell-gs-filtration-exploitation.md) — magic-shell + GS-NF wiring gap (L3 closure path)
- [`docs/audits/2026-05-24-isospin-categorical-source.md`](audits/2026-05-24-isospin-categorical-source.md) — D9 isospin closure path (operator-valued bowtie extension)
- [`.claude/skills/local/canonical-watcher.md`](../.claude/skills/local/canonical-watcher.md) §Slot J — probe follow-up discipline (GB filtration + jet order + bar-symmetry triple-check)
- [`AGENTS.md`](../AGENTS.md) — repo-wide agent discipline (§3b-cond, §7c, §7aa)
