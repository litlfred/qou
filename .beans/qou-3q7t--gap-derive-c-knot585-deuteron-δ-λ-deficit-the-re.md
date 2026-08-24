---
# qou-3q7t
title: 'GAP: derive C_knot=5.85 (deuteron Δ_λ deficit) — the real ''improve binding'' target, not the scale-ambiguous A=3 near-miss'
status: in-progress
type: task
priority: normal
created_at: 2026-08-01T23:41:01Z
updated_at: 2026-08-21T19:58:36Z
---

## 2026-08-02 (PR #4556) — single-factor / single-scale route REFUTED with the pinned weight

With the binding weight now pinned to the derived Wenzl y_λ (#4543), the clean cross-isotope test:
C_knot(D/T/³He/⁴He) = 5.85/4.44/3.29/9.31 → spread 2.83× → NON-UNIVERSAL.

RULED OUT (all 0-fit): (1) weight (#4543); (2) dimension — f^λ is already tightest (vs d_q 116×, none 122×); (3) any single scale — global scale leaves the spread invariant, C_knot/A and C_knot/(A-1) non-constant, log C/log A non-constant, and a deuteron-pinned 0-fit scale mispredicts T/³He/⁴He by +32/+78/−37% (≫ isospin ±8%). Parallel checks also ruled out 'simple known invariant' and showed C_knot(D) 5.85× ≈ [sgn-chirality-cancellation 2.23×, NOT scale-fixable] × [intrinsic 2.62×].

Lean (sorry-free): T,³He at the SAME H₉ need C_knot differing 35% → no level-only rescale g(n,q₀) closes both (mirror_cross_ne / no_level_only_closure). scope-(b) for that closure class.

STILL OPEN: a genuine per-knot Δ_λ magnitude derivation. SURVIVING DIRECTION: the residual lives in the per-knot χ^λ-magnitude / word content, above a chirality-cancellation floor — NOT reachable by any weight/dim/scale choice. The one non-circular opening remains the per-vertex seminormal eigenphase / q-Reeb Δθ_λ (E₀-options audit Candidate #1), which to date closes only differences, not absolute magnitude. Audit: docs/audits/2026-08-02-c-knot-nonuniversal-pinned-weight.md.

## 2026-08-21 (PR #5406) — the recorded figures were CONVENTION-C-STALE, and the 59× spread is a coordinate artifact

TWO CORRECTIONS to the 2026-08-02 entry above, both 0-fit (convention D, proton pin, mpmath 50 dps).

(1) STALE FIGURES. The 5.85/4.44/3.29/9.31 → spread 2.83× recorded above is CONVENTION-C. The producer was refreshed to canonical convention D on 2026-08-11 (70d1ade383, bean qou-4jut); the committed witness reads C_knot(D/T/3He/4He) = 6.0679/6.7061/4.9054/290.007 → spread 59.12×, mirror ratio 1.35 → 1.3671. Do NOT quote 2.83× or 'C_knot ≈ 5.85' (including this bean's own TITLE, which names 5.85). Every VERDICT above survives and strengthens; only the magnitudes moved. Audit doc corrected with a banner in the same PR.

(2) THE 59× IS ILL-CONDITIONED. S(K) = Σ_λ t_λ is ALTERNATING, so |S| can sit far below the scale of its summands. Cancellation ratio κ(K) = |S|/Σ_λ|t_λ| is the reciprocal condition number under per-block relative perturbation (‖δ‖_∞ ≤ ε ⇒ |S′−S| ≤ ε·Σ|t| = (ε/κ)|S|; ε = κ drives S to 0 and C_knot to +∞). Measured: κ = 0.2911 (D) / 0.4137 (T) / 0.2944 (3He) / 0.0079548 (4He). 4He sits on a 126× near-cancellation, its largest single block term 52× the whole signed sum — a 0.8% per-block correction moves C_knot(4He) anywhere, sign included. Corroborated independently: threerow_4he_completion_probe.py (qou-prjo) already records a 4He sign change in q for the ℓ(λ)≥3 stratum of the same object; a sign change is a zero, hence κ=0 on the physical interval. Historical check: under the C→D migration |S| moved 3.5/34/33/96.8% for D/T/3He/4He — a ~24% per-term perturbation amplified by 1/κ≈126 reproduces the 96.8%, no 4He-specific mechanism needed.

RE-SCOPED TARGET. In per-block coordinates δ_min^∞ = |B_AME/m_e − S|/Σ|t| (minimum sup-norm relative per-block correction reaching the target) = 1.475/2.361/1.150/2.299 → spread 2.05×, not 59×. This does NOT rescue universality (δ_min is a LOWER BOUND on the missing structure; equal δ_min does not mean equal correction DIRECTION) and does NOT weaken the Lean mirror-pair exclusion no_level_only_closure (T and 3He are both well-conditioned, κ ≈ 0.29–0.41). What it says: the missing per-block magnitude is an ORDER-UNITY relative correction uniformly across all four isotopes. 'Derive C_knot ≈ 6' and 'derive C_knot ≈ 290' are the SAME SIZE of problem in per-block coordinates; reading 59× as '4He is qualitatively harder' is reading a coordinate artifact.

scope-(a) only — a correction to the INTERPRETATION of the spread, resting on the triangle inequality |Σt| ≤ Σ|t| plus the measured κ. No structural exclusion asserted, no ansatz proposed, nothing wired, B_AME used only as a diagnostic ratio (never inverted into a weight). Δ_λ MAGNITUDE STILL OPEN. Probe: computations/deltalambda/c_knot_cancellation_conditioning_probe.py.

## 2026-08-21 (PR #5406, cont.) — the 'SURVIVING DIRECTION' named above is SUPERSEDED

The entry above (and the 2026-08-02 audit) ends by naming the per-vertex q-Reeb eigenphase Δθ_λ (E₀-options Candidate #1) as 'the one non-circular opening', closing only differences to date. That is no longer accurate. qreeb_eigenphase_compactness_probe.py (bean qou-0g4z, audit docs/audits/2026-08-02-qreeb-eigenphase-compactness.md — landed the SAME DAY as the C_knot audit, which is why neither cites the other) measured |χ_λ/f^λ| block by block, 0-fit, reads_B_AME=false, and found: in every binding knot the ONLY block with |χ/d| > 1 is the trivial 1-dim rep (n) — character q^w, a pure writhe scaling with no mixing and hence no rotation angle at all. Every genuinely-rotational block (dim ≥ 2, where θ_λ = arccos(χ_λ/f^λ) is defined) is COMPACT. So the eigenphase channel is BOUNDED and cannot supply an absolute scale, and the sole unbounded channel q^w is already a summand of the master formula. The difference-only behaviour has a STRUCTURAL REASON (boundedness), not merely a failed search. scope-(a) for that construction; covers D/T/³He, with ⁴He falsified separately (docs/audits/2026-06-24-he4-qreeb-phase-falsification.md).

ADDED HERE: the blocks that actually DOMINATE the master sum are the compact ones, in every isotope — max|t_λ| sits at (5,1)/(6,3)/(6,3)/(8,4), all two-row, all dim ≥ 2, never the trivial rep. So the §2 near-cancellation is a compact-block phenomenon and the one unbounded channel contributes a minority share. The two results point the same way rather than merely coexisting.

WHAT IS ACTUALLY LEFT. The VALUE Δ_λ = (−1)^{n(λ)}·dim V_λ is proved sorry-free general-n and is untouched. Per-block weights are excluded as a class (six failed ansätze + no per-block weight converts intensive → extensive, cap exchangeDet_pow_two_le_four) — and the δ_min measurement agrees, the required correction being order-unity, i.e. not a refinement of the block weights but a comparably-sized separate object. The eigenphase opening is now closed for absolute magnitude. The honest remaining shape is the one AGENTS.md already names and which this session does NOT improve on: a separate, super-pairwise, ADDITIVE EXTENSIVE term. Two things would move it, neither attempted: (i) GAP-A-1 — fix the binding operator K(𝔥) ∈ H_{3A}(q₀) by substrate-only SDP and read its block content directly, bypassing any χ^λ → M_λ rule (E₀-options Candidate #2, multi-week); (ii) an absolute per-block energy normalization, which is a NEW SUBSTRATE AXIOM — the E₀-options audit already flags that if every candidate collapses to difference-only then Subgoal-1 is unreachable without one, and qou-0g4z is one more collapse of exactly that kind.

METHODOLOGICAL: any future cross-isotope diagnostic on this axis should report κ alongside the ratio. A spread computed across points of wildly differing κ compares one ill-conditioned measurement against three well-conditioned ones, and the resulting number is not a property of the physics.

NOTE ON THIS BEAN'S TITLE: it still names 'C_knot=5.85', a convention-C value; the convention-D deuteron figure is 6.0679. Not retitled here because that renames the file and siblings may reference it — flagged instead. Full write-up: docs/audits/2026-08-21-c-knot-conditioning-and-stale-convention.md.
