---
# qou-prjo
title: 'GAP: deuteron Delta_lambda magnitude — naive per-pair z dead across A; surviving object is transverse NA-Stokes surface-curvature (not braid-word, not scale, not level, not edge, not DT-count)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T19:09:10Z
updated_at: 2026-08-08T22:37:59Z
---

## State (PR #4615, 2026-08-02)

The deuteron binding magnitude is the Δ_λ Track-A gate. `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ`
with the derived fragment `Δ_λ = (−1)^{n(λ)}·dim V_λ` gives `B(D) = 0.380 MeV` (−82.9%);
the closing `C_knot = 5.853` is FITTED and is NOT a DT count (#4601).

### What is now excluded (this PR + prior)

- **naive per-pair `z = 1/[2]_v` dead across A** (this PR, Lean-proved): scope-(b)
  EXCLUDED at A=4 (`5z²>1 ⟹ det<0`) AND insufficient at A=2 where it is PHYSICAL
  (`b₂(z)=−ln(1−z²)=0.287`, a reduction; no derived scale reaches `B_AME`, needs 7.76 MeV;
  master-Σ dressing needs non-integer exponent k=6.16). `g_reeb` same (k≈7.94 near-8 is a
  numerology trap, not chased). A=2 is not a `[1^A]` singlet (rank C(4,2)=6), so the
  He4-local `−ln det` cumulant has no reason to transfer.
- prior walls: single-universal `C_knot` / single scale (#4556); level-only rescale
  (Lean `mirror_cross_ne`); weight `y_λ` (Markov, #4543); dimension `f^λ`; writhe/framing
  (Lean `no_writhe_only_framing`); coordination-edge 3/2 (#4472); brane-tower LEVEL/WIDTH
  (three-walls 2026-07-26); geometric `W_λ` (#4392, ~30× overshoot); jet-order valuation
  (#4574); DT-count/concentration (external Springer geometry, Rossmann-CC/#4581/#4601);
  6 original ansätze; KL-positivity PROBE-4 prune.

### Surviving direction (next honest step)

The residual is per-knot χ^λ-magnitude / word content above a chirality-cancellation floor
(`C_knot` audit §5). Two open deuteron residuals — master-Σ `C_knot=5.85` and rotational
`g₂=1.0087` (E⁺(1+h²) closes D to −0.036%, D-unique, g₂ underived) — BOTH point at the same
surviving object: the **transverse NA-Stokes surface-curvature pairing** `½P∮∮[F_q,F_q]` on
the pn (σ₁³/trefoil) Seifert surface (`2026-07-24-eunit-magnus-order2.md` §2: the σ₁³
single-generator word makes ALL braid-word/inter-crossing Magnus corrections vanish, so the
missing order-2 term MUST be transverse). **Wall: needs a canonical discretization of the
Yekutieli surface 2-form on the trefoil Seifert surface — data the corpus lacks.** Building
that discretization (genus-1 trefoil Seifert surface, Seifert form) is the named next unit;
until it exists the deuteron magnitude stays open.

### Do NOT redo

Any single-scale / per-pair / level / edge / dimension / writhe / DT-count closure — all
walled. A `Δ_λ` fitted to `B(D)` is the forbidden 7th ansatz.


---
## Update 2026-08-08 — LEAD 1 attempt (PR #4817, branch claude/deltalambda-3body-extensive-2026-08-08)

Built the q0-free >=3-row extensive cumulant FORWARD from the proved Delta_lambda.
s_k = Sum_{lam|-k, ell(lam)>=3} (-1)^{n(lam)} f^lam = {1:0, 2:0, 3:-1, 4:-2}, fed into
the derived C(A,k) coordination-simplex cluster basis (same basis as
AdditiveResidualSimplex, but q0-free / combinatorial instead of the q0 residual M(A)).

RESULT = scope-(a):
- 0-fit WIN: nu2 = 0 re-derives the derived mu2 = 0 combinatorially (s1=s2=0),
  independent of the graded-ladder self-reference, no q0. The deuteron carries no
  >=3-body cluster term (structural).
- NEGATIVE (sign): forward (nu3,nu4) = (-1,+2) -- the OPPOSITE sign order to the
  derived (mu3,mu4) = (+0.4708,-4.591) i.e. the #4316 (+,-) window is reversed.
  Delta_lambda chirality parity does NOT supply the many-body sign-change.
- NEGATIVE (magnitude): |nu4/nu3| = 2 vs derived ~9.75; extensive AME ratio
  B_ext(4)/B_ext(3) = 6.0 vs AME 3.336 (+80%); single-algebra reading = 2.0 (-40%).
  The two parameter-free readings BRACKET AME; interpolating is the forbidden fit.

CONCLUSION: the q0-free >=3-row signed-Springer-dimension content ALONE does not
supply the many-body binding sign+magnitude; those live in the q0-dependent
y_lam*chi^lam trace weighting. Nothing wired. free_parameters=0, no AME inversion.

SURVIVING SUB-QUESTION (next honest unit): is the (+,-) many-body sign-change window
an irreducibly ARCHIMEDEAN (q0-dependent) feature -- i.e. is a fully q0-free closure
provably impossible? Concretely: does sign( Sum_{lam|-k, ell>=3} y_lam(q) chi^lam Delta_lambda )
cross zero between the combinatorial q->1 limit and q0? If yes, the sign is not
combinatorial and the magnitude derivation must run through the q0 trace (the mu4
alpha-cluster residual via rho_F cluster integrals, AdditiveResidualSimplex sec S).

Files: docs/audits/2026-08-08-threerow-extensive-cumulant-forward-qfree.md;
QOU/MassTheory/ThreeRowExtensiveCumulant.lean (sorry-free; lean-direct exit 0,
#print axioms clean on all 11 decls -- the earlier "sandbox disk quota" block was a
MISDIAGNOSIS, corrected 2026-08-09: the toolchain and 6990 mathlib oleans were already
present. NOTE the residual "sorry-free != derived" seam: sRow3 is a hand-entered table,
Python-checked and independently re-derived by hook length, NOT a Lean-proved partition
sum -- cite as "the table sRow3 gives (-,+)", never "Lean proves the >=3-row stratum");
computations/deltalambda/threerow_extensive_cumulant_forward_probe.py (+witness).

---

## LEAD-2 geometric surface-curvature route (PR #4818, 2026-08-08)

Formalize-first attack on the transverse pairing Ω₂=½P∮∮[𝓕,𝓕]. Does NOT close
the magnitude (scope-(a)); localizes it and Lean-proves a diagonal dead-end.

- **Lean (sorry-free, lean-direct exit 0):** QOU/MassTheory/TransverseSurfaceCurvature.lean
  — Seifert Betti b₁=c−s+1 (trefoil=2); ordered transverse pairing over a
  generic Ring; **THE WALL** formalized (transverse_nonzero_needs_noncommuting_
  curvature: nonzero pairing ⇒ position-dependent transported curvature = the
  missing surface-2-form data). Magnitude NOT derived.
- **Forward probe (0-fit):** AME binding ratios sit BETWEEN the diagonal
  envelope (∝b₁, undershoots 4He 3 vs 12.72) and off-diagonal envelope
  (∝C(b₁,2), overshoots 15 vs 12.72) — same shape as na-Stokes ℏ⁰/ℏ² bracketing.
- **Scope-(b) sub-exclusion (Lean-proved):** the diagonal/Betti-count reading is
  EXACTLY linear in link count (seifertBettiOne_link_additive) ⇒ pairwise-capped
  ⇒ CANNOT be the ≥3-body term. DO NOT redo any additive/Betti closure.
- **Isospin-blind:** T=³He geometry but AME differs (p/n split invisible to
  genus topology).
- **Surviving sub-question:** compute the surface-ordered transport U(x,O) on
  the trefoil Seifert surface + the off-diagonal cross-handle pairing
  Σ_{i<j}[U_i⁻¹F U_i, U_j⁻¹F U_j], and test whether it is non-additive over
  links (super-pairwise). Still blocked on the canonical multi-nucleon Seifert
  braid word (corpus lacks it; only the deuteron trefoil is pinned).

Audit: docs/audits/2026-08-08-nastokes-transverse-surface-curvature-geometric-route.md

---
## SIGN sub-question RESOLVED (PR #4829, 2026-08-08) — bean stays OPEN (magnitude unclosed)

> SUPERSEDED ON TWO POINTS by #4832/#4836 (see the later entries): (a) the n=9
> "no crossing" is correct only on (1,q₀] — a crossing exists but sits ABOVE the
> Wenzl pole q*=1.27845 where the effective level r is COMPLEX, so it is not a
> member of the same trend; (b) the ⁴He "compute-limit / disk quota" was a
> MISDIAGNOSIS — the cause was a dense np.eye densifying the sparse seminormal
> matrices; fixed, ⁴He crosses on the physical interval at q=1.02092.

Ran #4817 §5's exact next unit: does sign(Σ_{λ⊢3A, ℓ≥3} y_λ(q)·χ^λ(β_K;q)·Δ_λ) cross zero on (1,q₀]?

VERDICT: **YES for the deuteron**. F_D = +8.05e-5 at q→1⁺ → −0.1950 at q₀, zero-crossing at **q≈1.05365** ∈ (1,q₀). T/³He (n=9) monotone negative, no crossing (scope-(a)). ⁴He (n=12) documented compute-limit (f64 seminormal, no mpfr kernel; disk quota). Char-free companion G=Σ y_λ·Δ_λ also crosses at n=6 (q≈1.024); n=9,12 don't.

Structural cause: 3-row block overtake — (4,1,1)[Δ=−10, +term near q=1] overtaken by (3,2,1)[Δ=+16, largest |Δ| in ℓ≥3, −term at q₀]; sgn F_D(q₀)=sgn(y·χ·Δ)_{(3,2,1)}<0.

CLOSES the sub-question 'where does the deuteron ≥3-row sign live' → the archimedean/q₀-dependent trace weighting (q₀-USE not q₀-derivation; derived not fitted; free_parameters=0; proton anchor; layer-pure). Confirms #4817 §5 / #4818 §5.

Does NOT close the MAGNITUDE (Δ_λ value-only; super-pairwise extensive term still open). Also NOT the cross-isotope (μ₃,μ₄)=(+,−) cumulant window (distinct surviving unit, §6.1). Files: docs/audits/2026-08-08-deltalambda-threerow-sign-crossing-probe.md; computations/deltalambda/threerow_sign_crossing_probe.py + witness.
