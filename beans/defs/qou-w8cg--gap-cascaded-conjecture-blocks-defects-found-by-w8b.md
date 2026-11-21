---
# qou-w8cg
title: 'GAP: cascaded conjecture blocks (#8568) — defects found by W8b audit'
status: todo
type: task
priority: normal
created_at: 2026-11-20T18:30:00Z
updated_at: 2026-11-21T02:29:11Z
parent: qou-6qbv
---

Read-only audit (W8b, 2026-11-20) of the 9 blocks demoted by the #8568 cascade. Findings, none acted on except explicit-alpha-k-h3 (PR #8631):

- No §3b-cond conditional theorem is possible on the spectral chain yet: `SpectralSequenceH3Explicit` takes three arbitrary Props as parameters, so nothing derives from it. It needs content (an encoding of d1/d2/pages, owner deferred) first.
- Every edge in the 9 is citational except explicit-alpha-k-h3 (its sketch takes E∞ representatives from the spectral conj). The owner chose full cascade over dropping edges, so they stay.
- explicit-alpha-k-h3: values now derived as Markov traces (#8631). Open: σ1−σ2 is not central; 4 classes listed vs dim Z(H3) = 3.
- alpha-k-derivation-procedure: Lean proves generic unique solvability given invertibility; the invertibility of the generic-q character matrix is a hypothesis, needing a citation or proof. Its -proof.md pins q0 to the muon value (proton default).
- explicit-alpha-k-h4: hardcoded floats plus norm_num range checks on the same literals; the exact Q(q) table is not encoded (closable by a finite exact computation). Header still says convention C. Dangling lean.ref (library stub is empty).
- wedderburn-bratteli-recursion: BratteliEdge has no containment constraint and a free content field, so the predicate forces y ≡ 0; `axiom plancherel_completeness_axiom` has an unmeetable hypothesis (unused but undisclosed). Dangling lean.ref.
- joint-tower-sdp-confinement: `joint_tower_sdp_feasible` has its hypothesis equal to its conclusion; constraint predicates are placeholders. Dangling lean.ref.
- atom-knot-mass-derivation: near self-assuming projection; `MassIdentity` is "within 25 % of AME" (max miss 19.5 % at 40Ca) — a tolerance sized to its own miss.
- baryon-product-from-alt: the Lean proves a Vandermonde identity, not the .md's sign-isotype claim, which may be false (a plain product of three velocities is S3-symmetric). Lean over ℝ, .md says over R (§7c). Edge to atom-knot is citational.
- six-term / frobenius: stale `prop:`/`thm:` labels in docstrings; frobenius .lean links braids-and-knots/ but the block is in mass-theory/.

## 2026-11-20 W8b: three gaps closed (PR #8635, owner "Go")
- alpha-k-derivation-procedure: n=3 invertibility proved (det = -[2]_q[3]_q); ring generalised to a field. General n still a hypothesis.
- explicit-alpha-k-h4: floats replaced by the exact H4 table; proved dual basis χ_μ(r_λ) = δ κ_λ and tr(r_λ) = y_λ κ_λ. So α_3(H4) = 0 under convention D; the old +0.003463 was convention C.
- wedderburn-bratteli-recursion: degenerate predicate + unusable axiom removed; convention-D Jones weights proved to satisfy the Bratteli sum rule and single-edge relations. .md's summed form would double-count (authorNote). Normalisation Σ f^λ y_λ = 1 not encoded.
- Still open: atom-knot tolerance-as-fit, joint-tower hypothesis=conclusion, baryon-product claim mismatch, general-n invertibility, spectral-sequence carrier encoding.

## 2026-11-20 W8b (PR #8655)

#8635 merged (9949299). #8655 fixes: stale prop:/link in six-term + frobenius Lean docstrings; joint-tower placeholders renamed to well-formedness, tautological joint_tower_sdp_feasible removed, lean.ref -> JointTowerSdp; baryonProductFromAlt over CommRing; alpha-k proof .md y_λ pin now matches its witness.

Still open:
1. y-lambda-jones-markov-witness.json is at the CODATA-2018 muon pin and its producer is not listed ideal_muon, so by the proton default it should be re-run at proton; consumer binding_a3plus_joint_ji_combiner.py moves.
2. atom-knot MassIdentity = within 25% of AME, worst case 19.5% (tolerance sized to its miss).
3. baryon .md says the product of the three dc_k/dz is the sign-isotype projection; a product of commuting scalars is S3-symmetric. The Lean proves Vandermonde.
4. wedderburn .md sums the edge rule over all parents; each single edge already gives y_λ (checked at (3,1)), so the sum double-counts.

Items 2-4 put to the owner on cards.

Owner ruled 2026-11-20 on items 2-4 (all recommended options) and they are applied in #8655: atom-knot 25 % bound dropped (class now states B = m_e·M); baryon integrand restated as the velocity Vandermonde (false proof steps removed); wedderburn statement restated to the proved forms. Item 1 (re-run the y_λ Jones-Markov witness at the proton pin) remains open.

Item 1 done in #8655 (2fe41f665c): y-lambda-jones-markov witness re-pinned to proton via q_parameter.Q_50_DIGIT_STR, fmt-serialised. Effect ≤ 4.59e-8 relative on the weights and on the consumer. Found while checking: binding-a3plus-joint-ji-combiner.witness.json (computed 2026-09-06) is stale independent of the re-pin. A fresh run moves e.g. 4He joint_B_pred 15.87 → 0.587 MeV, and both old and new runs fail he3_baseline_sum_reproduces_full_theta_assembly (expected 0.7587; listed in witness-failed-assertion-baseline.json). Not regenerated: another arc's numbers. Cause not identified.

#8655 merged 2026-11-21 (e2cc9f6). Open: the stale binding-a3plus-joint-ji-combiner witness and its failing he3 read-check (cause not found).

## 2026-11-21 (PR #8697)

binding-a3plus-full-theta-assembly and binding-a3plus-joint-ji-combiner re-run on the 2026-09-13 Reeb witness (y_λ unchanged, every Δθ moved). ³He volume-scaled μ₀ |rel_err| 4.9 % → 78.5 %; D 264 % → 19.6 %. Combiner read-check now reads the assembly witness live (was literal 0.7587) and passes.
