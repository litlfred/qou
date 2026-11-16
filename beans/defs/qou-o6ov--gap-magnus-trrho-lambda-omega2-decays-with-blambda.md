---
# qou-o6ov
title: 'RESEARCH: does |tr(rho_lambda Omega2^P)|/dim decay in b across the <=2-row column? (NOT a truncation blocker)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T17:41:56Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-10v9
---

**RESCOPED 2026-09-05 (owner: "rescope and continue"), after PR #6822. Read this header, not the historical one below it.**

**This is OPEN MATHEMATICS, not infrastructure. It blocks nothing.** The original framing --
"upgrades the poly-size row-truncation from heuristic to a rigorous error bound" -- is DEAD:
convention D (owner ruling 2026-08-09) sets y_lambda = 0 for l(lambda) > 2, so the excluded
high-row terms in this bean own rigor gap are multiplied by ZERO and the row truncation is
already exact. Measured n=3..12: the nonzero-y count is exactly floor(n/2)+1, i.e. LINEAR.
Corroborated at atom_bond_dimension_measure.py:94. Full argument: PR #6822 +
docs/audits/2026-09-05-magnus-arc-traced-the-wrong-rho.md.

**THE RESCOPED QUESTION.** Under D the entire sum runs over <=2-row shapes (n-k, k), where
b = k. So the two-row column is no longer one handle among several -- it is the WHOLE object.
Does |tr_{(n-k,k)}(rho Omega2^P)|/dim decay in k?

**Two corrections that any attempt must carry:**

1. **rho is the HECKE element, not a braid.** atom_braid_word_3A returns triples (c, d, g)
   denoting c*sigma_g + d*1. The whole prior arc used [int(t[2]) for t in ...], a bare sigma_g,
   which at A=3 is the wrong operator for 19 of 35 letters (54%). Every pre-#6822 number in
   this bean is for the positive braid, NOT the atom.
2. **The old headline figures are convention-C.** "86->92%" is
   magnus_sign_row_truncation_probe.py convention-C reflection-rep share; the D-frame value at
   A=3 is 73.50%. Do not quote 86%.

**What is measured for the TRUE element, n=9, dps 65 (#6822):** the y-weighted mass is monotone
decreasing in b and b=1 carries 73.50% (better than the braid 70.45%). But the full-census
envelope is NOT decreasing (peaks at b=3) and its total range is only 2.41x against the braid
1427x -- so the surviving claim must be stated on the <=2-row column, not the full census.

**Live handle:** the two-row reduction tr_{(n-k,k)}(g) = tr_{W_k}(g) - tr_{W_{k-1}}(g) via
U_q(sl_2) Schur-Weyl is EXACT for Omega2^P (verified ~1e-139, A=2,3) and is a character identity,
so it holds for any algebra element g -- rho_true included. That is the tool for the rescoped
question.

---

HISTORICAL HEADER (superseded above; retained as the record of the original framing):

Open theorem. Measured: |c_lambda|=y_lambda|tr(rho_lambda Omega2_lambda)| concentrates on low b=n-lambda_1 (b=1 reflection rep 86->92% for A=3->4). The naive bound |tr|<=q^L*dim FAILS (Sigma y*dim tail plateaus at 0.5, #6183/#6265) -- concentration is a tr cancellation (tr(Omega2)=0), NOT a weight effect. Route: Kerov-Olshanski shifted-symmetric bounded-degree + traceless cancellation = cluster/cumulant statement (Procacci-Yuhjtman/Rebenko ingested). Proving this upgrades the poly-size row-truncation from heuristic to a rigorous error bound (pins the 60-dps partition count). PRs #6265.

RESEARCH (2026-08-30): Kerov-Olshanski route tested empirically on A=3 (28 partitions dim>1). tr(rho_lambda Omega2)/dim_lambda is NOT a low-degree polynomial in content power-sums p_k=Sum c^k: max rel resid only 0.94->0.29(deg1)->0.20(deg2)->0.08(9 terms), no collapse to machine-zero (a true low-degree content polynomial nails it). So the germ-trace is OUTSIDE the standard polynomial-functions-on-Young-diagrams framework (rho*Omega2 neither central nor group-algebra element) -- naive content-polynomiality proof route REFUTED for this normalization. Steers the proof to the cluster/cumulant route (tr(Omega2)=0 connected-diagram cancellation), not content moments.

REFINEMENT (2026-08-30): the theorem statement 'raw |tr| decays with b' is FALSE as written -- measured |tr(10,2)|=12634 > |tr(11,1)|=12211 at A=4 (bump at b=2). The bump tracks dim (peaks mid-sector). The quantity that DECAYS is |tr|/dim (A=4 2-row: 1110,234,71,28,19,22 by b) or equivalently the y-weighted contribution c_lambda=y_lambda*tr. Also: the 2-row sector gives NO clean closed-form decay law (tr non-monotonic, inter-j ratios drift 0.51-1.03, sign-flip at (5,4)/A=3), so the closed-form-2-row proof route is not clean either. Correct theorem: |tr(rho_lambda Omega2)|/dim_lambda decays with b(lambda). Proof still open (cluster/cumulant route).

PROGRESS (2026-08-30, PR #6311): FIRST POSITIVE result. The tr-decay is PER-WINDOW LOCAL, not an inter-window cancellation. Ω₂ decomposes exactly (far-commutativity) into a period-3 lattice sum of 3-strand-local commutators [A_a,A_{a+1}] (multiplicities (28,4,7) per nucleon), self-checked 2·tr(ρΩ₂)=Σmult·t to 4.3e-57 (A=3)/4.5e-58 (A=2). Each per-window |tr(ρ_λ[A_a,A_{a+1}])|/dim_λ PEAKS at b=1 for EVERY window at A=2 and A=3 ⇒ decay already present per-window ⇒ RULES OUT the Penrose/Ursell inter-window-cancellation sub-route. REDUCES the theorem to a single fixed 3-strand-local operator's normalised-trace decay (ρ still global). Honest limits: not monotone; suppression modest at A=2 (~1.5x), sharpens to 5.6-12.8x A=3; single-window estimate STILL OPEN. Probe: computations/deltalambda/magnus_tr_decay_perpair_cluster_probe.py; audit docs/audits/2026-08-30-magnus-tr-decay-perpair-cluster-local.md

MERGED (2026-08-31, PR #6311, rebase 18dfda15c4): per-window-local result + verified Lean skeleton on main. Lean QOU/MassTheory/MagnusOmega2LocalDecomposition.lean sorry-free (commutator_eq_zero_of_commute, omega2_reduces_to_adjacent, trace_rho_localSum, trace_rho_weightedLocalSum), axioms={propext,Classical.choice,Quot.sound}. The empirical peak-at-b=1 decay is NOT formalized (measured/open). REMAINING OPEN: the reduced single-window estimate |tr(ρ_λ[A_a,A_{a+1}])|/dim_λ decays with b (with a rate), for a FIXED 3-strand-local operator.

PROGRESS (2026-08-31, PR #6331): the reduced single-window estimate is SUB-DIM, not a cancellation. --raw discriminator (A=2 all 11, A=3 all 30, exact mpf): raw |tr(ρ_λ[A_a,A_{a+1}])| grows FAR slower than dim_λ — at most 14.7% as fast (A=3, dim ×13.1) / 31.3% (A=2, dim ×3.2), o(dim) margin sharpens with A. So |t_λ^{(a)}|=o(dim_λ): decay = dim outgrowing a slowly-varying raw trace, NOT dim-tracking cancellation. Reduced target is now a SUBLINEAR single-window trace bound |t|≤C·dim^θ (θ<1) — more provable than Penrose/Ursell. HONEST: raw|t| not constant (rises ~2× then falls) so strict ≤C bound FALSE. NEXT: A=4 low-b cross-check + per-partition (not max_λ) bound + attempt the rank-bounded active-tableau count giving θ<1. Audit docs/audits/2026-08-31-magnus-single-window-sublinear-trace-growth.md

PROGRESS (2026-08-31, PR #6339): LOCALIZED the sublinear bound. Lean (sorry-free, lean-direct exit 0): trace_rho_commutator_reframe tr(ρ⁅A,B⁆)=tr(⁅ρ,A⁆B) [self-check 9.24e-139 A=3], + Leibniz commutator_mul_left ⁅XY,Z⁆=X⁅Y,Z⁆+⁅X,Z⁆Y. Cauchy-Schwarz ⇒ |tr(ρO)|≤‖⁅ρ,A_a⁆‖_F·‖A_{a+1}‖_F. Frobenius probe (A=2,A=3 exact mpf): ‖A_{a+1}‖_F/√dim≈1.0 FLAT (germ is Θ(√dim), dead end); ‖⁅ρ,A_a⁆‖_F/√dim DECREASES with b in every window. So the whole o(dim) decay lives in ‖⁅ρ_λ,A_a⁆‖_F. REDUCED TARGET: ‖⁅ρ_λ,A_a⁆‖_F=o(√dim) — a NORM (no signed cancellation). Leibniz telescopes ⁅ρ,A_a⁆ into only the O(1) crossings near a (⁅σ_g,A_a⁆=0 for |g−a|≥2), a bounded sum of LOCAL commutators dressed by word-pieces. NEXT: bound ‖σ_{<i}‖ word-piece op-norms + local ‖⁅σ_g,A_a⁆‖_F; check o(√dim) (not just decreasing) at A=4. Audit docs/audits/2026-08-31-magnus-sublinear-bound-localized-to-rho-germ-commutator.md

PROGRESS (2026-08-31, PR #6349): ROUTE-NEGATIVE. The operator-norm/telescoping route to o(dim) is a DEAD END. Controls: ‖σ_k‖_op=q exactly (σ symmetric, eig={q,−1/q}, err 0) — word-piece factors are dim-independent constants (sound half). But the LOCAL commutator max_{a,g∈{a±1,a}} ‖⁅σ_g,A_a⁆‖_F/√dim RISES and PLATEAUS at ≈1.5 (A=2,A=3 exact, all partitions) — Θ(√dim), NOT o(√dim). So submultiplicative bound gives |t|≤C·Θ(√dim)·Θ(√dim)=O(dim), CANNOT reach the measured o(dim). ⇒ the o(dim) is a genuine CANCELLATION (among the O(1) telescoping terms, each Θ(√dim), and/or in the trace) — a NORM-ONLY proof is impossible; must track signs (cumulant/connected-diagram, where tr(Ω₂)=0 began). scope-(a) route-negative, invariant ‖⁅σ_g,A_a⁆‖_F=Θ(√dim); o(dim) itself NOT refuted (measured true). Also caught: ⁅σ_a,A_a⁆≠0 (germ ≠ commute own gen). NEXT: the cancellation-tracking route is the only surviving one; the norm shortcut is closed. Audit docs/audits/2026-08-31-magnus-local-commutator-is-theta-sqrt-dim-opnorm-route-fails.md

PROGRESS (2026-08-31, PR #6352): the o(dim) cancellation is DISTRIBUTED, not pairwise. Leibniz telescoping ⁅ρ,A_a⁆=Σ_i T_i verified numerically to 8e-139; #terms=12 CONSTANT (O(1) near-a support). Cancellation splits two ways: WITHIN-term (dominant) Σ‖T_i‖_F/√dim ↓×7.6 (A=3) — the word-piece dressing σ_{<i}[σ_g,A_a]σ_{>i} sits well below its submultiplicative bound; BETWEEN-term κ=‖ΣT_i‖/Σ‖T_i‖≈0.1 ↓×2.3 (A=3, sharpens with A). Product ×17 = the ‖⁅ρ,A_a⁆‖_F/√dim decay. NOT a clean pairwise cancellation ⇒ no telescoping-collapse shortcut; proof needs a conjugation estimate ‖σ_{<i}[σ_g,A_a]σ_{>i}‖_F=o(√dim) AND κ→0, both sign-level (cumulant/connected-diagram). OPEN: does ‖⁅ρ,A_a⁆‖_F/√dim→0 or plateau (tracks b not dim)? — NEXT is the CS slack ‖⁅ρ,A_a⁆‖_F·‖A_{a+1}‖_F/|t| to localize commutator-vs-trace. Audit docs/audits/2026-08-31-magnus-telescoping-cancellation-is-distributed.md

PROGRESS (2026-08-31, PR #6354): SHARPEST characterization — o(dim) dominated by TRACE-ORTHOGONALITY. CS slack = ‖[ρ,A_a]‖_F·‖A_{a+1}‖_F/|t| GROWS from ~3 (b=1) to 10²–10³ (high b) in every window (A=3). slack=1/|cos θ| ⇒ [ρ,A_a] becomes nearly trace-ORTHOGONAL to germ A_{a+1} as b grows. So the DOMINANT o(dim) driver at high b is the trace overlap vanishing, NOT the commutator-norm decay (#6339, modest) nor only the telescoping cancellation (#6352). PROOF TARGET restated cleanly: ⟨⁅ρ_λ,A_a⁆,A_{a+1}⟩_Frobenius/dim_λ → 0 — a matrix-element/overlap (equidistribution) statement, exactly what cumulant/connected-diagram computes, the sharpest form of the sign cancellation the norm route can't reach. HONEST: A=3, dim≤200, slack magnitudes noisy; qualitative growth robust across 7 windows; not proved. FULL MAP now: single window (#6311)→‖[ρ,A_a]‖_F (#6339)→not a norm bound (#6349)→distributed cancellation (#6352)→trace-orthogonality dominant (#6354). Audit docs/audits/2026-08-31-magnus-cs-slack-trace-orthogonality-dominates.md

PROGRESS (2026-08-31, PR #6362): library assessment of the cluster route (corpus-grep path 5). Procacci-Yuhjtman (2016) IS ingested = arxiv-1508.07379v2 (Penrose tree-graph); Rebenko 2205.07095 + Jansen-Kolesnikov s10955 too. BUT all are CLASSICAL COMMUTATIVE convergence-radius results — Penrose tree-graph rewrites a sum over connected graphs of SCALAR pairwise Mayer weights; references.ts already notes it says nothing about cumulant SIGN. The QOU overlap ⟨⁅ρ_λ,A_a⁆,A_{a+1}⟩_F is NON-COMMUTATIVE operator-valued (no ∏-over-edges), needs a cumulant sign to vanish ⇒ the route is a TEMPLATE not a plug-in theorem; the proof is genuinely NEW work. Corrects the arc's repeated 'tied to Procacci-Yuhjtman' framing. Closer unassessed lead: arxiv-math-0411505 (non-commutative colored Jones formula), Jones/Hecke setting — recommended first read for next attempt. Audit docs/audits/2026-08-31-cluster-route-literature-assessment.md

PROGRESS (2026-08-31, PR #6372): assessed arxiv-math-0411505 (Garoufalidis-Le non-comm colored Jones) per owner. CORRECTS #6362 UPWARD: the non-commutative cumulant structure DOES exist in the corpus — colored Jones = zeta function of arc-graph ζ(G,B)=∏_c 1/(1−β(c)) = inverse quantum (MacMahon) determinant, so log ζ = sum over connected cycles = a genuine NON-COMMUTATIVE connected-diagram expansion (the non-comm counterpart of Penrose tree-graph #6362 said was absent). CAVEATS: still not a plug-in bound — (1) paper's limit is color n (MMR loop expansion), not my Young-diagram shape b; (2) total knot invariant, not per-seminormal-irrep germ overlap. Right machinery, wrong coordinates. CONCRETE BRIDGE (research program): express tr(ρ_λ⁅A_a,A_{a+1}⁆) as short-cycle term in log ζ(G_K,B) (germs A_a=∂σ_a·σ_a⁻¹ = edge-weight log-derivatives), re-index cycle sum by Hecke irrep (hard new step), read b→∞ decay off 1/(1−β(c)). Audit docs/audits/2026-08-31-noncommutative-cumulant-structure-exists-colored-jones.md

PROGRESS (2026-08-31, PR #6387): the b-decay ENDPOINT is an EXACT zero — Lean sorry-free. Every prior probe skipped dim≤1 so missed it: the two extreme partitions are 1-dim (trivial λ=(n) b=0; SIGN λ=(1ⁿ) b=n−1 max). In any 1-dim rep ⁅A_a,A_{a+1}⁆=0 ⇒ tr(ρ_λ Ω₂)=0 exactly (confirmed A=1,2,3 to 1e-100). New Lean lemma trace_rho_commutatorSum_eq_zero_of_commute (lean-direct exit 0): pairwise Commute ⇒ Σ⁅A_k,B_k⁆=0 ⇒ tr(ρ·Ω₂)=0, general CommRing. So the decay TERMINATES at a provable zero, not an asymptote. Grounds #6372: under Schur-Weyl the sign rep (1ⁿ) is the fully-antisymmetric/determinant = Alexander sector of the MMR loop expansion — the decay endpoint sits in the semiclassical corner the arc-graph zeta points to. HONEST: sign-rep zero RIGOROUS; Schur-Weyl/Alexander identification SUGGESTIVE (grading bridge open); RATE open. Audit docs/audits/2026-08-31-magnus-decay-endpoint-is-exact-zero-sign-rep.md

PROGRESS (2026-08-31, PR #6392): Schur-Weyl bridge ANSWERED (NO) + corrects #6387. Does the sign-rep endpoint = color-n Alexander sector? NO. Three distinct Alexander appearances: (a) MMR large-COLOR N limit → 1/Δ [user's 'color-n']; (b) reduced BURAU = reflection (n−1,1) = b=1: Δ∝det(I−Burau) [Jones 1987, Squier 1984]; (c) SIGN (1ⁿ) = b=max = the endpoint: σ_i=−q⁻¹ scalar ⇒ ρ writhe-only monomial, NO Alexander. #6387 conflated (c) with Alexander — BACKWARDS. Verified A=2,3: reflection dim n−1 at b=1; sign rep scalar tr=0; |tr(ρ_λ Ω₂)|/dim PEAKS at b=1 (46 at A=3), decays to sign zero. So Alexander is at the SOURCE of the decay (b=1 Burau peak), not the endpoint; decay runs AWAY from Alexander. #6387 exact-zero endpoint (Lean) STANDS; correction banner added. RATE: reframed as fall-off from Burau peak, ~2.6–11×/b-step empirically, STILL OPEN (governed by trace-orthogonality #6354, not a support collapse — #6349 showed local commutator Θ(√dim)). Audit docs/audits/2026-08-31-alexander-sector-is-b1-burau-not-the-sign-endpoint.md

PROGRESS (2026-09-02, PR #6416, after review of main): conjugation symmetry REFUTED + route-status consolidation. NEW negative: b-profile NOT conjugation-symmetric — tr(ρ_{λ'}Ω₂)/tr(ρ_λ Ω₂) messy (peak↔near-endpoint R=−0.0033 A=3, not ±1/q-power); germ log-derivative breaks q→−q⁻¹. CONSOLIDATION: 7 structural shortcuts to the RATE now measured-dead — (1) naive q^L·dim, (2) operator-norm telescoping [local commutator Θ(√dim) #6349], (3) support/tableau counting, (4) Kerov-Olshanski, (5) classical cluster/Penrose #6362, (6) non-comm colored-Jones zeta wrong-coordinates #6372, (7) conjugation symmetry. ONE open core: trace-orthogonality ⟨⁅ρ_λ,A_a⁆,A_{a+1}⟩_F/dim→0 (#6354), unreachable by routes 1–7. Proved endpoint (sign rep=0, Lean) + Burau/Alexander peak (b=1) stand. Practical: b=1=86–92% so truncation works; rigorous tail bound is what's blocked. Consolidation audit docs/audits/2026-09-02-magnus-tr-decay-route-status-consolidation.md

PROGRESS (2026-09-02, PR #6430): FIRST POSITIVE ADVANCE — the hook slice of the tr-decay is CLOSED-FORM via the reduced Burau, all orders. Hooks (k,1^{n-k}) = q-exterior-powers of the reflection rep V (reduced Burau). Verified exact (A=2,3, 139-digit/1e-91): PLAIN Σ_j tr_{(n-j,1^j)}(ρ)t^j = q^L det(1+sρ^V) [Burau char poly]; ALL ORDERS (Ω₂) Σ_j tr_{(n-j,1^j)}(ρΩ₂)t^j = q^L·s·det(1+sρ^V)·tr((1+sρ^V)^{-1}Ω₂^V ρ^V), s=t/q^L [determinant DERIVATIVE]. So the whole hook column reduces to one (n-1)-dim matrix pair (ρ^V,Ω₂^V) with explicit q^{-Lj}-per-order suppression — partial proof of the decay on the hook slice, reduced from exponentially-growing hook irreps. Extends #6392 (b=1 point) to the full hook column. LEAN (sorry-free, exit 0, axioms clean): MagnusHookExteriorPower.lean — the all-orders elementary-symmetric generating function ∏(1+tμ)=Σ t^j e_j, general CommRing (verified by lean-verifier subagent). HONEST: hook slice only; non-hook λ (not exterior powers) remain the open theorem. Audit docs/audits/2026-09-02-magnus-hooks-are-q-exterior-powers-of-reduced-burau.md

PROGRESS (2026-09-03, PR #6432): BEYOND HOOKS — does the determinant handle reach two-rows? Answered (A=2 exact): (1) NO to ρ^V — tr_{(n-k,k)}(ρ) vs Jacobi-Trudi s_{(n-k,k)}(eig ρ^V) fails (~1e-13); S^{(n-k,k)}(V) reducible over S_n ⇒ determinant handle is HOOK-SPECIFIC (single-column Schur functors only). (2) two-row CHARACTERS reduce EXACTLY to the 2-dim U_q(sl₂) R-matrix (Schur-Weyl): Σ_k(n-2k+1)tr_{(n-k,k)}(ρ)=tr_{(ℂ²)^⊗n}(ρ) to 140 digits. (3) BUT the germ Ω₂ does NOT — same sum with Ω₂ is 6.5% off (plain matches to 1e-140 ⇒ not a convention error). Root: germ A_i=q∂σ_i·σ_i⁻¹ is a log-derivative of the REP MATRIX (representation-specific); seminormal↔R-matrix intertwiner is q-dependent. This PINS why hooks were the breakthrough: exterior-power Λʲ(V) is GERM-NATURAL (matched 1e-91 in #6430), Schur-Weyl R-matrix is not. NEXT: germ-natural two-row handle = projected Schur functor of seminormal V. Two-row decay slice stays OPEN. Audit docs/audits/2026-09-03-magnus-two-row-germ-is-realization-dependent.md

PROGRESS (2026-09-03, PR #6434): 'germ on the full tower?' ANSWERED — NO, the germ is underdetermined ⇒ representation-specific. A=q∂σ·σ⁻¹ satisfies {σ,σ'}=h'σ+hσ' (diff'd Hecke): in σ-eigenbasis this FIXES the diagonal (2λ−h≠0 ⇒ A_ii=±1) but leaves the OFF-DIAGONAL FREE (λ_q+λ_₋=h ⇒ coeff vanishes). Verified genuine 2×2 block: diag ±1 both seminormal & R-matrix; off-diag differs (seminormal 0.171 vs R-matrix 1.43). ⇒ seminormal per-irrep germ (base.germ_csr, whole arc) is ONE gauge; P(A)=Σ y_λ tr(ρ_λΩ₂) well-defined specifically in that gauge; explains #6432 two-row 6.5% mismatch at mechanism level. RETRACTION (caught in-session): channel-sign closed form A=(2σ−h)/[2]_q is FALSE on genuine blocks (only holds where σ diagonal; first check used that degenerate case; max|A−(2σ−h)/[2]|=0.27). Arc results STAND (seminormal used consistently). OPEN: gauge-invariant (curvature) formulation? Audit docs/audits/2026-09-03-magnus-germ-is-underdetermined-not-a-full-tower-object.md

2026-09-03 (post #6445): hook column of the gauge-invariant curvature Ω₂^P reduces to the (n−1)-dim reduced Burau in closed form, all orders: tr_hook(ρΩ₂^P) = (4/[2]²)·q^{(L+2)(1−j)}·Σ_a[e_j(eig Wσ_aσ_{a+1}) − e_j(eig Wσ_{a+1}σ_a)], j=n−k. Verified to dps floor (worst 2.6e-139) on every hook at n=6. Endpoint-zeros manifest. TRAP: first pass omitted #6430's word-length twist (len=L+2, not L) and matched only j=0,1+endpoints — those rows cannot detect a missing twist. Probe: magnus_gauge_hook_closed_form_probe.py.


- 2026-09-03 (Lean, PR #6480): `MagnusGaugeCurvatureHookColumn.lean` — `curvatureSum` + `trace_mul_curvature_eq_sum_word_traces` (unconditional linearity: curvature trace = signed sum of word-traces of length L+2) + `trace_mul_curvature_eq_of_word_traces` (conditional closed form with a SINGLE common twist c — the L+2 trap made structural). lean-verifier: lean-direct EXIT 0, zero diagnostics, as authored; both thms `#print axioms` = [propext, Classical.choice, Quot.sound], no sorryAx. Generic CommRing/Algebra, no ℝ. Premise (per-word hook identity, 139 digits) stated as hypothesis, not proved.


- 2026-09-03 (decay bound, PR #6520): bounded the #6464 hook closed form in j=b(λ). CRUDE spectral-radius bound holds but is a binomial hump (peaks j=2/4 at A=2/3, loose 10–10³) — because r ≈ q^L (r/q^L = 1.006, 1.10): the twist q^{(L+2)(1−j)} EXACTLY cancels the dominant Burau eigenvalue, d ≈ q⁻², so only the subdominant spectrum can decay. SHARP bound |e_j(μ)| ≤ e_j(|μ|): B'_j = T_j·Σ_a[e_j(|μ⁺|)+e_j(|μ⁻|)] HOLDS and B'_j/C(n−1,j) is STRICTLY DECREASING for all j at BOTH A (tightness 0.23/0.13). Burau moduli fall off geometrically (≈0.71–0.77/step). Monotonicity is MEASURED on the real moduli, not a theorem for arbitrary spectra. Lean lemmas (MagnusHookDecayBound.lean: abs_esymm_le_esymm_abs + 2 corollaries) written; verification pending.


- 2026-09-03 (Lean verified, PR #6520): MagnusHookDecayBound.lean — abs_esymm_le_esymm_abs, abs_sum_esymm_sub_le, abs_mul_sum_esymm_sub_le — lean-direct EXIT 0, zero diagnostics after dropping an unused [DecidableEq ι] binder (strictly more general); all three #print axioms = [propext, Classical.choice, Quot.sound], no sorryAx. Binders [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] are exactly what Finset.abs_prod takes in v4.24.0.


- 2026-09-03 (two-row handle): the two-row column of Ω₂^P is carried EXACTLY by the up-spin sectors of the 2-dim R-matrix — tr_(n−k,k)(g) = tr_W_k(g) − tr_W_(k−1)(g), W_k = k-up-spin sector (dim C(n,k)), verified PLAIN and with ρΩ₂^P at A=2,3 to ~1e-139 (magnus_two_row_weight_sector_probe.py). Two-row analogue of the hooks' reduced-Burau handle (#6464); exists because Ω₂^P is an algebra element (#6445) — the germ failed this by 6.5% (#6432). Per-dim two-row decay monotone in k=b(λ) at both A (A=3: 33.6, 8.67, 4.00, 1.70). Next: a decay BOUND for two-rows must respect the difference structure — a per-sector triangle inequality does not decay in k.


- 2026-09-04 (mechanism SETTLED, PR pending): the b(λ)-decay is CANCELLATION, not size. Control = conjugate pairs (dim λ = dim λ' exactly, b flips): 9/9 pairs at A=2,3 have commutator-norm ratio ≥ 1 (1.13–1.31, ~1.25) while trace ratio is 0.003–0.27. Sharpest: (8,1) vs (2,1⁷), both dim 8 — norm 0.755→0.955, |tr|/dim 33.65→0.115. So NO bound |tr| ≤ Σ‖[ρ,σ_a]‖·‖σ_(a+1)‖ can produce the decay (scope-(a): plain norm route excluded, not every norm argument); the spectral route the hook bound #6520 takes is the one AVAILABLE, not merely the one taken. The earlier A=2/A=3 'contradiction' was an artifact: the normalised norm is U-SHAPED in b and the A=3 run was truncated inside the falling half. Targeting note: the high-b tail is CHEAP (dim λ = dim λ'), merely last in enumeration order — --min-b 6 --max-dim 50 gets it in ~1 min vs hours.


- 2026-09-04 (REFINES the #6548 reading): the decay FACTORIZES exactly, |tr|/dim = κ · Σ|eig|/dim with κ = |Σeig|/Σ|eig| (phase) and Σ|eig| (magnitude), M_λ = ρ_λ(ρ)·ρ_λ(Ω₂^P). On 9 conjugate pairs (dim controlled): Σ|eig| ratio falls in 9/9 (0.005–0.37) and DOMINATES in 9/9; κ falls in 8/9 and RISES in 1 ((3,3)→(2,2,2), 0.604→0.837). Product reproduces #6548's trace ratios independently (0.732×0.00469 = 0.00343). ⇒ the decay is chiefly a COLLAPSE OF THE OUTPUT SPECTRUM, not phase cancellation in the trace — correcting the inference I drew from #6548 (whose stated finding, that the INPUT-norm route is excluded, is untouched). Cancellation happens in the ASSEMBLY of Ω₂^P from the σ's, not in the final trace, which is why term-by-term input bounds fail. CONSTRUCTIVE: an absolute-value spectral bound on M_λ (Σ|eig|, or dim × spectral radius) IS viable and is the route to the general-λ statement.


- 2026-09-04 (CONSTRUCTIVE TARGET identified): majorant ladder |tr| ≤ Σ|eig| ≤ Σσ ≤ √dim·‖M‖_F (and Σ|eig| ≤ dim·ϱ) — EVERY rung decays in EVERY conjugate pair (max ratios A=2: 0.267/0.371/0.423/0.521/0.534; A=3: 0.093/0.106/0.133/0.179/0.122). So the b-info survives to the FROBENIUS norm of the assembled M_λ. AND that majorant is itself a positive trace: seminormal generators are EXACTLY symmetric (max|σ−σᵀ| = 0.0), so under word-reversal * , ‖M_λ‖_F² = tr_λ(X*X) with X = ρ·Ω₂^P — verified 7.6e-141 on all 11 shapes at n=6, POSITIVE, decaying 9/9 pairs (A=3 down to 9.2e-5). ⇒ the general-λ bound is a POSITIVE trace of an algebra element, so the #6464 Burau and #6525 R-matrix-sector handles (character identities, valid for ANY algebra element) apply to it verbatim, with no cancellation to fight. NOT yet derived: a closed form/bound for tr_λ(X*X).


- 2026-09-04 (DERIVED, not just applicable): reduced-Burau closed form for the POSITIVE majorant on the hook column. X*X = -c²Σ_{a,b}[σ_a,σ_(a+1)]·(ρ*ρ)·[σ_b,σ_(b+1)] expands into 4(ngen-1)² words ALL of length T=2L+4, so #6464's twist q^{len(1-j)} is COMMON and factors out: tr_hook(X*X) = -c²q^{T(1-j)}Σ_{a,b}Σ_± ± e_j(eig in reduced Burau). Verified every hook at A=2 AND A=3, worst 2.1e-138, positive throughout. Uses only (n-1)×(n-1) matrices (5x5, 8x8) vs dim_λ² up to 70/216. FIRST derived closed form for the BOUND rather than the quantity. Not done: two-row column (would go via #6525 sectors, same argument, not run); and a closed form is not yet a bound — no monotonicity in j derived from it.


- 2026-09-04 (hook column CHAIN CLOSED): Σ|eig(M_hook)|/dim ≤ √(B''_j/dim) with B''_j = c²q^{T(1-j)}Σ_{a,b}Σ_± e_j(|μ|), T=2L+4, and B''_j/dim STRICTLY DECREASING in j=b(λ) at A=2 and A=3. Every step derived: (B) Cauchy-Schwarz+Schur (#6573); the closed form via the common twist (#6556); B''_j via |e_j(μ)| ≤ e_j(|μ|), Lean-proved in MagnusHookDecayBound. Tightness 0.06–0.24 (bound 4–16x loose but valid+monotone). STILL INPUT not theorem: the Burau moduli themselves are measured. TWO ERRORS OF MINE CAUGHT BY THE PROBE: (a) tightness column mixed total Σ|eig| with the PER-DIM bound — a units error printing ratios >1 that read as a bound violation; fixed. (b) I asserted the CRUDE bound could not decay — it DOES decay per-dim at both A (the binomial divides back out since dim=C(n-1,j) for a hook); crude vs sharp differ in TIGHTNESS (3x to ~2000x), not monotonicity. #6520's precedent is about RAW monotonicity, a different quantity — do not carry it across.


- 2026-09-04 (two-row majorant route: NEGATIVE, scope-(a)). #6525's sector identity DOES carry the positive majorant (Ř symmetric, max|R−Rᵀ|=0.0; tr_λ(X*X) = tr_W_k − tr_W_(k−1) exact to 6.1e-139), and positivity makes dropping the subtracted sector LEGAL: 0 ≤ tr_(n−k,k)(X*X) ≤ tr_W_k(X*X), holds at every k, computed as ‖X|_W_k‖_F² on a C(n,k) block of the fixed 4×4 Ř (no eigenvalues). BUT the bound does NOT decay per dim — bound/dim rises at the last k at BOTH A (A=2: 320.8, 281.4, 560.0; A=3: 4718.6, 4191.2, 3856.1, 5388.2) and slack grows 1.0→10.5 (A=2), 1.0→5.5 (A=3), because the lower sectors accumulate. So positivity makes the drop legal, not affordable; the difference structure #6525 flagged remains the obstacle. Scope-(a): excludes the drop-the-sector route as stated, NOT a two-row bound that keeps the difference (e.g. via the sl₂ lowering intertwiner W_(k−1) ↪ W_k, so the difference is a trace on the cokernel) — untried.


- 2026-09-04 (CORRECTION to my own two-row entry above): I framed the two-row route as a NEGATIVE. Too pessimistic — RETRACTED. The two-row REDUCTION holds and IS monotone: tr_(n−k,k)(X*X) = ‖X|_W_k‖_F² − ‖X|_W_(k−1)‖_F², two Frobenius norms on C(n,k) blocks of the fixed 4×4 Ř (no seminormal construction, no eigenvalues), exact to 6.1e-139 and STRICTLY DECREASING per dim in k at both A (A=2: 320.78, 103.15, 53.56; A=3: 4718.6, 2793.1, 1498.6, 981.2). The negative is NARROW and only about the lossy shortcut (S): dropping tr_W_(k−1) is legal by positivity but too lossy (slack 1.0→10.5), so the difference must be KEPT — which costs nothing since it is exactly computable. NET: the positive majorant reduces BOTH columns to small n-independent objects, monotone per dim in b(λ) — hooks to the reduced Burau, two-rows to a sector Frobenius difference.


- 2026-09-04 (GLOBAL b-ordering: pointwise REFUTED, envelope HOLDS). Prior evidence for the b-decay was conjugate-pair only (#6556), which cannot see a violation between non-conjugate shapes. Tested directly over all λ up to a dim cap: (a) POINTWISE monotonicity is FALSE — 2 real inversions at A=3, hook (3,1^6) at b=6 per-dim 14.32 sitting BELOW OTHER shapes (2,2,2,2,1) 31.56 and (2,2,2,1,1,1) 24.97 at b=7. So a general bound in b ALONE cannot exist; hooks decay faster than handle-less shapes at comparable b. (b) The ENVELOPE max_{b(λ)=b} per-dim IS strictly decreasing at BOTH A — A=2: 320.78 > 174.18 > 53.56 > 19.74; A=3: 4718.6 > 3478.3 > 1498.6 > 981.2 > 211.6 > 31.6 — and the envelope is what a decay BOUND actually needs. So the arc's target survives in envelope form, not as pointwise monotonicity. Endpoint note: trivial/sign are EXACT zeros (Ω₂^P vanishes on 1-dim reps) and are excluded — including them makes 0 < anything read as an inversion, which is how my first run produced 9 spurious ones. Caveat: 17 of 30 shapes at A=3 exceed the dim cap and are unmeasured (named in the output); a found inversion refutes regardless, but the envelope claim is over the measured subset.


- 2026-09-04 (second-statistic search: ALL candidates DEAD). Given pointwise b-monotonicity is refuted, tested whether some other single statistic orders tr_λ(X*X)/dim_λ. Candidates: b(λ), ℓ(λ), n(λ)=Σ(i−1)λ_i (the corpus's own Δ_λ grading), n(λ'), n(λ)−n(λ'), b+ℓ, and dim_λ as a NULL CONTROL. Result at A=2 and A=3: NONE is strictly decreasing. Inversions/ties (A=2 | A=3): b 0/7 | 2/8; ℓ 4/7 | 3/8; n(λ) 2/2 | 1/1; n(λ') 32/2 | 53/1; n(λ)−n(λ') 2/2 | 1/0; b+ℓ 2/2 | 1/2; dim_λ 17/8 | 25/7. Two things worth keeping: (i) the NULL CONTROL FAILS HARD (dim_λ 17 and 25 inversions), so the decay is NOT a dimension artifact — it is about λ's shape; (ii) n(λ) and n(λ)−n(λ') are the closest (1–2 inversions) but do NOT order it, so they must not be quoted as the grading. NOTE b(λ) shows 0 inversions at A=2 and fails only on TIES there — the A=3 inversions are what refute it, which is why one size was not enough. NET: the per-dim majorant is not a function of any of these alone; what survives is the ENVELOPE form. 17 of 30 shapes at A=3 unmeasured (dim cap, named in output).

## 2026-09-04 — q-content statistic probe (#6669): ONE blocking pair, not a dead class

Three findings.

1. PREMISE REFUTED BY ITS OWN CONTROL. I built #6669 on the observation that all
   seven of #6587's dead statistics are q-INDEPENDENT while the ordered quantity is
   a normalized character of an element of H_n(q). The q-independent control
   n(λ')−n(λ) matches the best q-content statistic exactly at A=3 (1 inversion, 0
   ties, 55 pairs). q-independence was not the defect.

2. ONE BLOCKING PAIR. Five of seventeen statistics tested come within one inversion
   at A=3 and ALL FIVE fail on the same pair: (7,1,1) [hook, j=2, dim 28, per-dim
   3478.285] vs (7,2) [two-row, k=2, dim 27, per-dim 2793.099]. None fails elsewhere.
   b(λ) fails on a different pair ((3,1⁶) vs the two b=7 shapes) plus 8 ties.
   ⇒ ACTIONABLE: the blocking pair is hook-vs-two-row at b=2, and BOTH columns have
   derived closed forms already (#6556 reduced Burau; #6587 sector difference). The
   obstruction is analytically accessible, not merely measured.

3. THE q-CANDIDATE IS NOT INDEPENDENT EVIDENCE. P₁−P₋₁ = 2Σsinh(2c·lnq) has leading
   term 4·lnq·(n(λ')−n(λ)). Tested: at A=3 the two induce IDENTICAL orderings (0
   disagreements) so the q-result corroborates nothing; at A=2 they differ on one
   pair so they are not the same statistic.

CORRECTION TO MY OWN CHARACTERISATION of #6587 (not to its numbers — it re-runs and
reproduces exactly, and its verdict is right). 'All 7 candidates dead' is true as
'none is a strict orderer' and misleading as 'none is close': three miss by one pair.
The dim_λ null control still fails hard (25/7), so the shape-not-dimension conclusion
stands.

NEXT: settle (7,1,1) vs (7,2) from the two closed forms rather than by measurement —
do the hook Burau form and the two-row sector difference cross at b=2?

Limits: A=2/A=3, dim cap 50 skips 17 of 28 shapes at n=9 (not run, not evidence).
X*X is NOT central, so the JM/content structure is a reason to look, not a derivation.
scope-(a). Nothing wired.

## 2026-09-04 — hook vs two-row from the closed forms (#6677)

THE DIM CAP COMES OFF, AND IT STRENGTHENS #6587. Neither closed form builds the
seminormal irrep (hook: (n-1)x(n-1) reduced Burau, #6556; two-row: sectors of the
fixed 4x4 Ř, #6587), so neither is bound by dim ≤ 50 — the cap that made every
earlier probe in this arc skip 17 of 28 shapes at n=9. The full hook column at A=3
is monotone per-dim over ALL 7 hooks:
  4718.62 > 3478.29 > 1671.23 > 581.163 > 134.628 > 14.319 > 0.435429
with (6,1,1,1) dim 56, (5,1^4) dim 70, (4,1^5) dim 56 previously unreachable. #6587
could only say this of the 4 under the cap. A dimension-selected subset can flatter
a trend, so this was a real check, and it passed.

GATES (out-of-cap rows are refused unless both pass). In-cap vs direct seminormal:
6.67e-139 / 10 shapes at A=2, 2.06e-138 / 11 at A=3. The STRONGER gate — the two
INDEPENDENT reductions against EACH OTHER at b=1, where (n-1,1) is simultaneously a
hook and a two-row: 1.86e-139 (dims 5/5) and 3.21e-139 (dims 8/8).

THE RELATION REVERSES WITH b, at both sizes.
  A=3: hook > two-row at b=2 (3478.29 vs 2793.10) and b=3 (1671.23 vs 1498.56);
       two-row > hook at b=4 (981.20 vs 581.16).
  A=2: hook > at b=2 (174.18 vs 103.15); two-row > at b=3 (53.56 vs 47.26).
⇒ #6669's blocking pair (7,1,1)/(7,2) is NOT an instance of a systematic ordering.
Any statistic ordering the per-dim majorant must reproduce a hook/two-row relation
that CHANGES SIGN with b — a materially stronger demand than monotonicity, and a
better reason to stop hunting an eighth candidate than 'seven have failed'.

SUGGESTIVE, SAMPLE SIZE TWO: both reversals sit at b = ⌊n/2⌋, the LAST b at which a
two-row exists, where (n−b,b) is as square as it gets. May be a BOUNDARY effect of
the two-row column rather than an interior crossing. Two sizes cannot separate
those — OPEN, needs a third size.

Limits: A=2/A=3. Out-of-cap values are exact evaluations of formulas verified in-cap
and against each other — stronger than extrapolation, not a proof of either closed
form. Nothing here BOUNDS anything; the closed forms compute the trace of X*X, they
do not majorize it. At b=n−1 the Burau form returns −1.7e-141, roundoff at dps 140
against a true zero, excluded from the monotonicity check rather than clamped.
scope-(a). Nothing wired.

## 2026-09-05 — A=4 settles it: the crossing is INTERIOR, not a boundary artifact (#6710 kernel)

#6677 left this open: hook(b) vs two-row(b) reverses, but at both sizes then measured
the reversal sat at b = ⌊n/2⌋, which is ALSO the last b with a two-row shape. Two
readings fit two points — (i) BOUNDARY, the column just ends; (ii) INTERIOR, the
curves genuinely cross. A=4 separates them.

A=4 (n=12), ⌊n/2⌋ = 6, ratio hook/two-row per-dim:
  b=1  62105.983 / 62105.983  = 1.0        (same shape — forced, the cross-check)
  b=2  50708.093 / 43907.244  = 1.154891
  b=3  28688.965 / 25677.635  = 1.117274
  b=4  13057.703 / 15754.936  = 0.8288007  ← CROSSES
Crosses at b=4, STRICTLY before b=6. Reading (i) is REFUTED — the two-row column
continues to b=5,6, so its boundary cannot explain a crossing at b=4. k=5,6 were
never computed; the k=4 result already decides it.

CROSSING POINT vs ⌊n/2⌋ across all three sizes — the divergence IS the result:
  n= 6: crosses at b=3, ⌊n/2⌋=3  agree
  n= 9: crosses at b=4, ⌊n/2⌋=4  agree
  n=12: crosses at b=4, ⌊n/2⌋=6  DIVERGE

OBSERVATION, sample size 3, recorded as observation not law: over n=6,9,12 the
crossing sits at b=3,4,4 while n doubles — roughly CONSTANT in b, not proportional
to n (fractions 0.50, 0.44, 0.33). Second pattern same caveat: the ratio peak (always
at b=2) shrinks — 1.689, 1.245, 1.155 — so the columns converge as n grows. Whether
the crossing is asymptotically constant is OPEN; three sizes cannot settle it.

CONSEQUENCE FOR THE ARC. #6669: five of seventeen statistics come within one inversion,
all failing on the same hook-vs-two-row pair. #6677: the relation reverses. This closes
the remaining escape — the reversal is NOT an edge artifact a statistic could be excused
from reproducing. Any ordering statistic must reproduce a hook/two-row relation that
CHANGES SIGN at an interior b that does NOT track n. That is why hunting an eighth
diagram statistic is the wrong next move.

Limits: A=2,3,4; A=4 computed to k=4 only (k=5,6 not run, not evidence). The sparse
kernel is gated at A=2/A=3 against the dense implementation (9.09e-66, 1.92e-65, every
k); same algorithm at A=4 is an argument, not a measurement at that size. Nothing here
BOUNDS anything. scope-(a). Nothing wired.

## 2026-09-05 — third handle (sl3 + Kostka) and the FIRST COMPLETE b-levels (#6729)

CORRECTED MY OWN STATED PLAN. I had said the next step was to bound the envelope from
the two closed forms in hand. FALSE, and the refuting data was already measured: at
A=3 the envelope is not attained on a hook or a two-row at large b —
  b=6: (3,3,3) 211.56 vs hook (3,1^6) 14.319  -> 15x
  b=7: (2,2,2,2,1) 31.56 vs hook (2,1^7) 0.4354 -> 72x
At large b the hook is near the MINIMUM of its level. A handle reaching the FAT shapes
was required.

THE CONSTRUCTION SUBSUMES BOTH EXISTING HANDLES. (ℂ^k)^⊗n = ⊕_λ S^λ(ℂ^k) ⊗ M^λ, Hecke
acting only on M^λ, μ-weight space of S^λ has dim K_λμ, so tr_{W_μ}(g) = Σ_λ K_λμ χ_λ(g).
K unitriangular in dominance ⇒ inverts ⇒ every χ_λ with ≤k rows. #6525's two-row
difference IS the k=2 case, demonstrated not asserted (k=3 checked against k=2 on every
two-row shape).

GATES, sharing no code by design:
 (1) Kostka alone: multinomial(n;μ) == Σ_λ K_λμ f^λ, no trace code. Exact at n=6,9,12.
 (2) n=6 COMPLETE gate: all 7 ≤3-row shapes vs seminormal, + Burau on 3 hooks, + sl2 on
     4 two-rows. Worst |Δ_rel| = 2.68e-63; per-dim values reproduce #6587 exactly.

n=9, FIVE SHAPES NEVER PREVIOUSLY EVALUATED (per-dim):
  (6,2,1) dim105 1572.9564 | (5,3,1) dim162 836.89929 | (5,2,2) dim120 665.48861
  (4,4,1) dim 84 605.58457 | (4,3,2) dim168 384.85787
  (3,3,3) dim 42 211.56463 reproduces the capped value exactly.

FIRST COMPLETE LEVELS IN THE ARC. Every prior envelope was a max over a DIM-CAPPED
subset — a lower bound on the max, not the max. Levels b=1,2,3 at n=9 now close:
  b=1 (1/1) 4718.6197 (8,1) | b=2 (2/2) 3478.2851 (7,1,1) | b=3 (3/3) 1671.2349 (6,1,1,1)
  4718.62 > 3478.285 > 1671.235  strictly decreasing.
b=4 missing 1, b=5 missing 3, b=6 missing 5, b=7 missing 3 — no envelope reported for
those; the probe refuses a subset max. NOTE: the new (6,2,1) 1572.96 lands BETWEEN the
hook (6,1,1,1) 1671.23 and the two-row (6,3) 1498.56, so completing b=3 did NOT
overturn its max — recorded because it could have.

COVERAGE, MEASURED: of 30 partitions of 9 — 12 with ≤3 rows, 12 with ≤3 cols (same
handle on transposes, overlap only (3,3,3)), hooks add 3 => 26 COVERED, 4 NOT:
(5,2,1,1) 189, (4,3,1,1) 216, (4,2,2,1) 216, (4,2,1,1,1) 189. All four have ≥4 rows AND
≥4 cols so no k=3 orientation reaches them; k=4 is hopeless (largest sector 7560).
DIRECT SEMINORMAL at dim ≤216 is the cheaper route for exactly those four.

BUG IN MY OWN REPORTING, fixed: b=0 and b=n−1 printed 'COMPLETE? no' beside 'missing 0'.
They ARE complete — exact-zero endpoints where Ω₂^P ≡ 0 on a 1-dim rep — and the guard
conflated 'excluded by design' with 'coverage gap'.

Limits: n=6 and n=9; gate at n=6 (same algorithm at n=9 is an argument, not a
measurement at that size). Does NOT complete the envelope — 4 levels remain incomplete.
Nothing BOUNDS anything. Whether the envelope stays monotone once b=4..7 close is OPEN,
and is exactly what the capped measurements could not answer. scope-(a). Nothing wired.

## 2026-09-05 — n=9 COMPLETE at 30/30: envelope monotone, and the pointwise obstruction is THE HOOKS (#6729)

THREE RESULTS.

1. ENVELOPE strictly decreasing over ALL 7 interior levels, every one COMPLETE — first
   time on complete data rather than dim-capped subsets:
     b=1 4718.6197 (8,1)  | b=2 3478.2851 (7,1,1) | b=3 1671.2349 (6,1,1,1)
     b=4  981.20482 (5,4) | b=5  605.58457 (4,4,1)| b=6  211.56463 (3,3,3)
     b=7   31.556344 (2,2,2,2,1)
   Both PRE-REGISTERED falsification routes came back null: (5,2,1,1) measured 699.33
   against the 1671.23 needed to break b=3>b=4, and no b=5 straggler approached 981.20.

2. POINTWISE refuted with EXACTLY 6 violations — and 6/6 have a HOOK on the LOW side,
   0 on the high side, 0 involving no hook at all. ⇒ POINTWISE MONOTONICITY HOLDS ONCE
   HOOKS ARE EXCLUDED. The probe COUNTS this rather than my reading it off the list.
     (5,1^4) 581.16 < (4,4,1) 605.58
     (4,1^5) 134.63 < (3,3,3) 211.56 / (3,3,2,1) 170.63 / (3,3,1,1,1) 154.25
     (3,1^6)  14.32 < (2,2,2,2,1) 31.56 / (2,2,2,1,1,1) 24.97
   ACTIONABLE: the obstruction is ONE family, and it is the family that already has a
   derived closed form (reduced Burau, #6556). A bound can treat hooks separately and
   make a uniform statement elsewhere — instead of needing one statistic across all
   shapes, which #6669 showed none does and #6677 showed would have to reproduce a
   sign-changing hook/two-row relation. It also retroactively unifies two earlier
   observations: the hook near its level MINIMUM at large b (15x, 72x below), and the
   hook/two-row ratio crossing 1 — same fact, hooks decay faster than everything else.

3. 🛑 THE dim<=50 CAP WAS A DENSE-PRODUCTS ARTIFACT, not a seminormal one. The Young
   seminormal generators are AT MOST 2-SPARSE PER ROW (sigma_csr: one entry for a diag
   block, two per row for a 2x2), so #6710's column-wise kernel applies DIRECTLY. dim 216
   went from not-finishing to 8.6 s. So a good part of the tensor scaffolding built over
   the preceding PRs was NOT strictly necessary at n=9. What it still buys: at larger n
   the weight sectors stay bounded by multinomials while dim_lambda explodes, and the
   closed forms are INDEPENDENT cross-checks — which is what makes the gates meaningful.

GATES: sparse seminormal vs reduced-Burau on all 9 hooks, worst 1.38e-64; plus vs
sl_3+Kostka at dim 105-168, the regime the largest shapes live in (that gate's 1e-10 is
set by quoting a 10-sig-fig table, not by the arithmetic, and says so).

NOT ESTABLISHED: n=9 only (gated at n=6); the four stragglers rest on ONE kernel with no
independent second route BY CONSTRUCTION (positivity holds, as it must); nothing BOUNDS
anything; 'pointwise holds off hooks' is a statement about this census, not a theorem,
and one size cannot separate it from an n=9 coincidence. scope-(a). Nothing wired.

## 2026-09-05 — the hook crosses level-MAX to level-MIN, at b=4 at BOTH sizes (#6748)

SHARPENS #6729, which said 'the obstruction is the hook family'. Ranking each hook
inside its own level on the COMPLETE n=9 census:
  b=2 rank 1/2 MAXIMUM | b=3 rank 1/3 MAXIMUM | b=4 rank 5/5 MINIMUM
  b=5 rank 6/6 MINIMUM | b=6 rank 7/7 MINIMUM | b=7 rank 4/4 MINIMUM
The hook is the TOP of its level at small b and the BOTTOM at large b, crossing between
b=3 and b=4 — exactly where #6677 found the hook/two-row ratio crossing 1.

n=12 CONFIRMS THE LOCATION. Hook vs two-row per-dim:
  b=2 50708.093 > 43907.244  hook could still be max
  b=3 28688.965 > 25677.635  hook could still be max
  b=4 13057.703 < 15754.936  HOOK IS NOT THE LEVEL MAX
Same crossover b=4 while n grew from 9 to 12. So the rank crossover is a real feature,
not an n=9 coincidence — which is the one thing #6729's hook-exclusion result could not
distinguish.

⇒ FOUR observations recorded separately across this arc are ONE fact: the hook column
decays faster than every other family. 'Sits low', 'is the pointwise obstruction',
'crosses the two-row at b=4', and 'is 15x/72x below the level max at large b' are all
this.

ASYMMETRY THAT MAKES n=12 AFFORDABLE AT ALL, and the probe states it per row: refuting
'hook is the level MAX' needs ONE shape above it (cheap); establishing 'hook is the level
MIN' needs the whole level (Sum dim^2 = 12!, ~1e11 ops even sparse — permanently out of
reach). So n=12 confirms the crossover LOCATION and says nothing about minimality there.

Limits: n=9 ranks exact (complete census); n=12 decides maximality only; b=1 excluded
from the n=12 comparison since (n-1,1) IS both shapes. Nothing BOUNDS anything.
scope-(a). Nothing wired.

## 2026-09-05 — the chain CLOSES end-to-end, and the majorant route cannot carry the SIZE

COMPOSED, first time end-to-end against the actual signed trace:
  |tr_λ(ρΩ₂^P)| ≤ Σ|eig(M_λ)| ≤ √(dim_λ·tr_λ(X*X)) ≤ dim_λ·√(E(b))
Both links hold on all 30 shapes; composed bound strictly decreasing:
  b=1 68.6922 > 58.977 > 40.8807 > 31.3242 > 24.6086 > 14.5453 > b=7 5.6175
That IS the arc's target — a derived per-dim bound on the ORIGINAL signed trace that
falls with b, no fit anywhere. AND IT IS MUCH LESS THAN IT SOUNDS.

TIGHTNESS, the actual result:
                          b=1      b=7     falls by
  composed bound √E(b)   68.69    5.62     12.2x
  actual |tr|/dim env    33.65    0.178    189x
  actual worst shape     33.65    0.0142(b=6)  2360x
⇒ THE BOUND CAPTURES 12x OF A 189x EFFECT. Slack per link:
  link 1 (spectrum→Frobenius): 2.041x at (8,1) b=1  …  550.2x at (3,2,1^4) b=6
  link 2 (shape→level envelope): 1.0x … 8.513x
Link 2 is fine — replacing a shape by its level max costs ≤8.5x, the price of wanting a
bound in b alone. LINK 1 IS WHERE THE BOUND DIES, and its looseness GROWS with b.

WHAT IT MEANS. Link 1 is |tr X| ≤ √(dim·||X||_F²): it replaces a signed trace by a norm,
discarding all eigenvalue cancellation. That discarded cancellation is the DOMINANT part
of the effect at large b. So the majorant route — the strategy since #6556 — establishes
the SHAPE of the decay and structurally CANNOT carry its SIZE. It cannot be repaired by
tightening links 2/3; link 1 alone accounts for the loss.

CORRECTS MY OWN #6556 FRAMING. There I compared conjugate pairs, found the majorant
decaying 213x vs 1.4x in the input norm, and wrote the decay is 'overwhelmingly
output-spectrum collapse, not phase cancellation'. First half STANDS (E falls 149x
per-dim). 'Overwhelmingly' was TOO STRONG: there IS substantial trace-level cancellation
on top, reaching 550x. Not a contradiction — #6556 compared a majorant between
conjugates, this compares a signed trace against its OWN majorant — but this is the first
time that comparison has been made across a complete census, which is why it only becomes
visible now.

SETTLES: the b-decay of the signed trace is real, derived, monotone on complete data.
DOES NOT SETTLE: any quantitative claim — 550x slack cannot support a numerical statement
about the row-truncation error, which is what this bean wants it for.
REDIRECTS: a quantitatively useful bound must KEEP THE SIGN INFORMATION.

Limits: complete n=9 only, this atom word; the two exact-zero endpoints excluded; nothing
proved for general n. scope-(a). Nothing wired.

## 2026-09-05 — the whole arc was on a superseded braid word (PR #6822)

Sibling `7db032fb48` (qou-hu1f, owner ruling, 07:53 UTC today) fixed `atom_braid_word_3A` to emit
the interleaved beta_Bor where it had been emitting the same letters BUCKETED BY GENERATOR. Different
element of H_n(q) — the sibling measures 82% apart at q0. Verified at A=3 and A=4: same 35/47 letters,
different order.

**Recomputed, complete n=9 census, dps 65: every number moves 4–16%, every structural conclusion
survives, two strengthen.**

- both chain links hold on all 30 shapes; envelope strictly decreasing over all 7 levels
  (4147.55 > 2527.90 > 955.32 > 495.70 > 265.95 > 62.58 > 2.906)
- **hook crossing still at b=4** — same interior b under a different operator
- pointwise violations 6 -> 4, still 4/4 with a hook on the LOW side, 0 high, 0 hookless
- hook kappa still U-shaped, minimum b=5 -> b=4
- hooks still best-bounded: median slack 24.51 vs non-hook 100.5 (4.1x, was 3.3x)
- #6754 STRENGTHENS: worst link-1 slack 550x -> 1217x
- (8,1) |tr|/dim 33.648 -> 29.00125; hook fall 291.4x -> 263.16x

**Also: Feray-Sniady pruned, scope-(b).** FS Thm 1's only lambda-dependence at a fixed element is
max(r,c), transpose-INVARIANT; measured |tr|/dim differs 263.16x across the (8,1)/(2,1^7) conjugate
pair. Loose by >=263x before any constant is fitted. NOT excluded: a q-deformation carrying a
transpose-ASYMMETRIC shape parameter — that is exactly what such a deformation must supply.

**STILL OPEN / not covered:** the n=12 legs (#6748) are on the OLD word and are unverified. That is
the one load-bearing claim in the arc not recomputed.

**Follow-up (not done):** no probe in this arc prints the braid word or a hash of it — they all print
q0, dps and n, the three things never in doubt. Printing `hash(tuple(gens))` beside the dps line
would make two runs comparable without re-deriving where their inputs came from. Touches every probe
in the arc.

**Method note:** this surfaced only because a 10% gap appeared between two runs of my own code. At
3% I would have read it as rounding.

## 2026-09-05 (later) — THE PREMISE IS DISSOLVED, and the arc traced the wrong rho (PR #6822)

Two findings, both measured, the second larger than the first.

### 1. The arc traced the wrong rho (54% of letters)

Every probe here builds `gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]` and applies a bare
sigma_g. atom_braid_word_3A does NOT return a braid word (own docstring, capitals, PR #5765; rename
rejected at 685 call sites) -- each triple (c, d, g) is the HECKE ELEMENT c*sigma_g + d*1. At A=3,
35 letters: 16 sigma, 12 sigma^-1, 7 averaged => 19/35 = 54% applied as the WRONG operator.

Complete n=9 census under both (magnus_true_hecke_element_probe.py, dps 65):

  E(b) = max_{b(lam)=b} tr(X*X)/dim     rho_bare        rho_true
    b=1                                 4147.5518       18.758498
    b=3                                  955.31763      31.352745  <- PEAK
    b=7                                    2.9063514    13.001647
  strictly decreasing?                  YES             NO
  dynamic range over all 7 levels       1427x           2.41x

So the bean's theorem AS STATED is FALSE at n=9 for the atom's Hecke element, and holds cleanly
for the positive braid the arc substituted. The hook split does not survive either.

BUT the PRACTICAL claim survives and improves: y-weighted mass share at b=1 is 70.45% (bare) ->
73.50% (TRUE), monotone decreasing in b under both. The defect breaks the theorem, not the practice.

UNAFFECTED: all five arc Lean files are over a generic {R : Type*} [CommRing R] with rho an
ARBITRARY algebra element -- a 54%-wrong input invalidated no theorem. That is what formalize-first
bought. The Feray-Sniady prune is also unaffected (structural argument).

### 2. THE BEAN'S RIGOR GAP IS CLOSED BY CONVENTION D

magnus_sign_row_truncation_probe.py -- the probe this bean came from -- states its own gap:

  "a rigorous sign needs Sum_{lam excluded} |y_lam tr(rho_lam Omega2_lam)| < |P_truncated|,
   i.e. a bound on |tr(rho_lam Omega2_lam)| for the excluded HIGH-ROW lambda"

Under convention D (canonical since the 2026-08-09 owner ruling) y_lam = 0 for l(lam) > 2, so every
excluded term is zero and the inequality is trivial. The bound this bean exists to prove is
multiplied by zero. Measured n=3..12: nonzero-y count is EXACTLY floor(n/2)+1 -- 5 of 30 at n=9,
7 of 77 at n=12, i.e. LINEAR. Independently corroborated in the corpus:
atom_bond_dimension_measure.py:94, "Under D the <=2-row truncation is already exact".

Also re-scopes active-set-truncation-prototype.witness.json ("truncation is INVALID for
production", ~1e-3 error vs 1e-15): under D the dropped terms carry weight exactly zero.

Also identifies the 86-92% in this bean's own header: it is that probe's convention-C
"reflection rep alone 56% -> 86% -> 92%". D-frame value at A=3 is 73.50%. NOT decomposed: how much
of 86 -> 73.5 is C->D weights versus the 2026-09-05 word-ordering fix.

### DECISION FOR THE OWNER — should this bean stay open?

Not closing it myself; dissolving a GAP bean's premise is your call. The options:

  1. CLOSE as superseded-by-ruling. What it means: the row-truncation rigor gap is gone, so the
     bean's stated purpose is met. Costs: nothing to run. Risks: if some consumer applies the
     truncation to a differently-weighted sum, that consumer still needs a bound -- I checked the
     originating probe and atom_bond_dimension_measure, not every caller. Commits to: not funding
     more rate work under this framing.
  2. RESCOPE to the surviving mathematics. What it means: keep it open for "|tr(rho_lam Omega2)|
     decays in b across the <=2-row column", explicitly NOT as a truncation blocker. Costs: the
     rate work continues at its current pace. Risks: it is FALSE in the envelope form for the true
     element, so the rescoped target must be stated carefully or it will be chased as before.
     Commits to: treating it as pure mathematics, not infrastructure.
  3. LEAVE AS IS. What it means: the header keeps a premise this session measured to be moot and a
     convention-C 86% quoted as current. Risks: the next agent re-derives all of the above.

DEFAULT IF YOU SAY NOTHING: option 3 -- the bean stays open with the corrected body appended but
the stale header intact.

MY RECOMMENDATION (judgement, not a finding): option 2. The truncation question is genuinely
settled by the ruling, but the b-decay across the <=2-row column is real open mathematics with a
closed-form hook handle and a two-row sector reduction already built, and it would be a waste to
close that with the infrastructure framing that no longer applies.

## 2026-09-05 (later still) — THREE three-point trends, three fourth points that refuted them (PR #6842)

The dominant failure mode of this arc, recorded because it recurred three times in ONE session and
each time the fourth size was cheap enough that there was no excuse:

1. **The y-weighting margin table.** A=2 and A=3 gave margins x1.42 and x1.44 -- two sizes agreeing
   to 1%, with an exact closed form behind them (y_k/y_k+1 = [n-2k+1]_q/[n-2k-1]_q, verified 1e-50).
   A=4 refuted it: both its bumps lose, including at the square end where protection is MAXIMAL.
   The agreement was a column-LENGTH artifact -- those columns were too short for a bump to land
   anywhere but the protected end.
2. **The sector reframing.** |tr_W_k|/C(n,k) decayed at A=3 and A=4 where the irrep column did not,
   and I called it the arc's first constructive direction. A=5 refuted it (rise into k=4, x1.181):
   2 of 4, failing at the LARGEST size.
3. **The k=3->4 divergence RATE.** Ratios 1.23869 -> 5.36793 -> 26.4306 looked like ~4.6x/step and
   I wrote 'fails at a rate, not by a recoverable margin'. A=6 gave 19.2541 -- growth x0.728, margin
   IMPROVING 0.0503 -> 0.0664.

WHAT SURVIVES ALL THREE CORRECTIONS:
  * the k=3->4 step FAILS at A=4,5,6 (3 of 4), margins 0.272 / 0.050 / 0.066 vs a required 1
  * the CEILING argument, because it is FORCED not empirical: [n-2k+1]_q/[n-2k-1]_q -> q^2 at fixed
    k, capped at [3]_q = 3.0437 anywhere
  * the CONTROL: plain tr(rho) rises where rho*Omega_2^P decays, so the A=3/A=4 sector behaviour is
    about the curvature, not the weight filtration
  * concentration, eroding: k=1 share 77.882 -> 73.499 -> 59.437 %

THE LESSON, and it is not 'measure more sizes'. In every one of the three the probe's OWN OUTPUT
carried the correct caveat -- 'NOT an asymptotic claim: 3 sizes. Read it as a rate to test, not a
limit' is printed by magnus_fixed_k_trend_probe.py, and the sector probe's docstring says a property
holding from the third size is the shape of a small-size artifact. The caveats were right every
time. The failure was in the PROSE, which promoted each pattern to a mechanism anyway. A caveat
printed by the tool and contradicted by the sentence quoting it is worth nothing.

Practical rule for the next agent on this arc: an n-point trend here needs its (n+1)th point BEFORE
it goes in a summary line, not after. The sizes cost 33s / 410s / 3020s at A=4/5/6 -- hours, not
days, and cheaper than the corrections.

STILL OPEN: whether the k=4 attribution is 'k=4', 'the arriving shape', or 'the square end' -- two
steps cannot separate them; the A=4->5 step discriminates and comes free from the running A=5
sector job.

## 2026-09-05 — cross-arc: a sibling proved WHY a trace-based decay statement is fragile

Sibling bean `qou-v7ms` (merged `082b7d9f3c` / `0c24e1d8a3`, session 016hQePZ) proves in Lean,
sorry-free, in `QOU/HeckeAlgebra/WedderburnTrace.lean`:

  * `traceFunctional_supported_apply` — a trace functional supported at ONE lambda IS
    `c_lambda * trace(x lambda)`: one coefficient against one number.
  * `markovTraceOnWedderburn_eq_traceFunctional` — the Markov trace IS such a functional, with
    `c = y_lambda(q0)`, so the result bites the actual object, not an abstract family.
  * Its stated consequence: `f^(2,1) = 2`, so that block is `M_2(R)` -- FOUR real dimensions, of
    which the trace reads ONE. "The information the clause wants is present in the block and
    destroyed by taking its trace. A derivation that reads the block rather than its trace is not
    blocked by anything here."

**Why this matters to o6ov.** This whole arc measures `tr_lambda(rho Omega_2^P)` -- one number per
block, out of `(f^lambda)^2`. The sibling's theorem is about a different question (the (2,1)
clause's three coefficients), so this is a THEMATIC connection and not a logical implication: it does
not prove anything about b-decay. What it does supply is a proved reason to expect trace-based decay
statements to be fragile, which is what this arc measured from the other end -- irrep 0/4, sector
2/4, y-weighted failing at A=4.

**And the obvious response has already been tried here, with the same outcome.** "Read the block,
not the trace" is exactly the Frobenius route: `tr_lambda(X*X) = ||X||_F^2` is a different
functional of the same block, measured in #6754 and in the chain probe. Its envelope
`max_{b(lambda)=b} tr(X*X)/dim` DOES decrease monotonically for rho_bare and does NOT for the true
Hecke element (peaks at b=3, total range 2.41x against rho_bare's 1427x, #6822). So moving from the
trace to a norm of the same block did not rescue the decay for the correct rho.

**Not duplicating.** The sibling's Lean is about trace functionals at a single partition; nothing
here re-derives or extends it. Recorded so the next agent on o6ov meets the structural reason
alongside this arc's measurements, rather than rediscovering the connection.

## 2026-09-08 coordination: same kernel as qou-x631, qou-k5r5, qou-za3q, qou-omr7

Audit docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 1 / §7.3 C2: `k5r5` (99 commits, 08-21 → 09-08) and `o6ov` (99 commits, 08-30 → 09-05) both work the odd-moment / Magnus `tr(ρ_λ Ω₂)` kernel, and before this note there were **zero** cross-citations among k5r5 / o6ov / x631 / za3q / omr7 (measured 2026-09-08 by grepping each body for the other four ids). Shared ledger: epic `qou-x631`, now parent of the other four. Roles — x631: epic, Cov_Planch(f^λ, Σc²) ≤ 0 / T₃(k) kernel; k5r5: M₁ > 0 (first odd moment), all-n proof OPEN, identity Lean-proved; o6ov: does |tr(ρ_λ Ω₂)|/dim decay in b across the ≤2-row column (open mathematics, rescoped 2026-09-05, PR #6822); za3q: Magnus-Ω₂ probes use the Plancherel weight y_λ, 91 % of their work on shapes tr_M annihilates; omr7: Magnus probes' d_q was the hook product, weight inverted (4 files, PR #6442). Statuses are unchanged by this note; a result landing on any of the five should be cited in the other four.


## Cross-citation from qou-za3q (2026-09-11): the A=4 Magnus sign is measured

Per the 2026-09-08 coordination note on qou-za3q ("a result landing on any of the
five should be cited in the other four"), this is such a result.

`he4_magnus_omega2_sign_sparse_probe.py`, 77/77 partitions of H_12, max dim 7700,
28661s:

    P_total(A=4) = 34.1260272853576529271380692762741452981457684651471317452205
    sign = +1    control (rho = I) = 0.0 vanishes    33+/42-    sign_flip_vs_A3 = False

Sign map across the light nuclei: A2 = -1, A3 = +1, A4 = +1. There is exactly ONE
sign change in A = 2,3,4 and it sits between the deuteron and the triton, NOT at
the alpha particle.

Load-bearing for anyone reading the older framing: the he4 probe's docstring
asserted "A=3: P<0, NO flip vs A=2" and that premise had propagated into its
GENERATED VERDICT string. It is false — A=3 is +2.4701927, confirmed by the
committed witness and a fresh 30/30 re-run. Fixed under qou-rfhj. If any of the
five beans reasons from "negative through the deuteron and triton", that premise
is stale.

scope-(a): a dimensionless SIGN datum. NOT a MeV (the Delta_lambda magnitude gate
is open and untouched), NOT a physical binding-sign assertion (qou-v7ro / #6077,
cited not re-derived). The total is a weighted sum of mixed-sign terms (33+/42-).


## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Progress (Round 57)
- Round 57 (`litlfred/qou#8213`, commit `2301811899d7f5b7e6235c29e2d41d3e068ef89b`): Added `commutator_mul_three`, `commutator_mul_of_right_commute`, and `commutator_mul_of_left_commute` in `MagnusOmega2LocalDecomposition.lean` plus 80-dps mpmath witness.
