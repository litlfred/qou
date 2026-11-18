---
# qou-prjo
title: 'GAP: deuteron Delta_lambda magnitude — naive per-pair z dead across A; surviving object is transverse NA-Stokes surface-curvature (not braid-word, not scale, not level, not edge, not DT-count)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-02T19:09:10Z
updated_at: 2026-10-04T15:12:51Z
parent: qou-v2om
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


## Follow-up (PR #4832, 2026-08-08) — sign structure sharpened; MAGNITUDE STILL OPEN

Three units on the ≥3-row signed trace `F_K(q) = Σ_{λ⊢3A, ℓ≥3} y_λ(q)·χ^λ(β_K;q)·Δ_λ`.
Bean stays **OPEN** — `F_K` is value-only and none of this touches the extensive
super-pairwise term.

**1. The deuteron crossing is A-DEPENDENT, not special.** #4829 swept only
`(1,q₀]` and called n=9 "no crossing". On a beyond-substrate diagnostic ray the
n=9 crossing IS there, at q ≈ 1.4617 (T) / 1.4285 (³He) — just above q₀. The
ladder is non-monotone: D 1.0537 (below q₀) · T,³He ~1.43–1.46 (above) · ⁴He
~1.019 (below). q₀ ≈ 1.10998 sits INSIDE the light-nucleus crossing band.

**2. ⁴He was never compute-limited.** #4829 blamed a missing `pyhecke_native`.
The real cause: `chi_atom` added a dense `np.eye(dim)` to an already-sparse CSR
Hoefsmit operator, densifying it and forcing O(dim³) per braid-word letter
(Σdim³ = 2.1e12 over the ℓ≥3 stratum of 12, L=47). Keeping the identity sparse +
accumulating `Tr(∏M_j)` column-batch-wise gives O(L·dim²): largest n=12 partition
3.5 s, full 70-partition sum ~32 s/grid point, pure Python. Bit-identical to the
dense path (rel 1.4e-15). **No truncation was taken** — all 70 partitions summed.
Reusable kernel: `computations/deltalambda/threerow_chi_sparse.py`.

**3. Lean, sorry-free** (`QOU/BraidsAndKnots/ThreeRowSignCrossing.lean`,
`lean`-direct exit 0, `#print axioms` = [propext, Classical.choice, Quot.sound]):
`sign_crossing_of_block_dominance_exchange` (dominance exchange ⟹ zero, by IVT),
`crossing_unique_of_strictMonoOn_ratio` (monotone overtake ratio ⟹ unique zero),
`two_block_neg_iff_ratio_gt_one`. These take the per-block dominance data as
HYPOTHESES — they do not certify the f64 numbers.

**Flagged, NOT claimed:** Z=N (D, ⁴He) cross below q₀; Z≠N (T, ³He) cross above.
Four points in two pairs, no derivation. Needs ⁶Li/⁷Li continuation (now cheap)
plus a structural reason before it is anything.

**Also noted:** the character is decisive — the character-free `G(q)=Σ y_λ·Δ_λ`
puts the n=12 crossing ABOVE q₀ (1.597) while the full character object puts it
BELOW (~1.019). Any route modelling the ≥3-row sign from the `y_λ` weighting
alone gets n=12 wrong.

Audit: `docs/audits/2026-08-08-threerow-sign-crossing-a-dependence-4he-and-lean.md`


### ⁴He completed + a correction to how the deuteron result should be read

⁴He (n=12) ran to completion — full 70-partition ℓ≥3 sum, no truncation, no
native kernel. It crosses at **q = 1.02092, BELOW q₀**, so the ladder is
NON-MONOTONE: D 1.05365 (below) · ³He 1.42852 / T 1.46170 (above) · ⁴He 1.02092
(below).

**Correction worth carrying forward:** the per-λ decomposition shows three
qualitatively DIFFERENT mechanisms, measured as leading-term/total at q₀:

  n=6   ~1.2×   two-block overtake — one block sets the total
  n=9   4–11×   multi-block cancellation — total is a small residue
  n=12  0.34×   broad constructive accumulation — total EXCEEDS its largest term

So #4829 §2's (4,1,1)→(3,2,1) overtake describes **n=6 and only n=6**, and the
Lean lemma modelled on it is an n=6 statement (the theorems are true for a
generic split; the empirical premise that one block dominates holds only for the
deuteron). **Do not generalise the deuteron block story to larger A** — that is
generalising the wrong object.

---
## q_cross(n) trend + fixed-n isospin control — PR #4836 (2026-08-09)

**Bean STAYS OPEN.** Nothing here touches the binding magnitude; this is SIGN
structure of the value-only ≥3-row trace only.

**Three negative answers, and the negatives are the result.**

1. **`q_cross(n)` is NOT a structured sequence.** On the real-level branch,
   crossings exist only for a sporadic subset of n (none for n ∈
   {3,4,5,7,9,10,12,14,16}) and the values oscillate: 1.0244 (n=6) → 1.2604 (n=8)
   → 1.1397 (n=11) → … → 1.1002 (n=18) → 1.1697 → 1.1512. Not monotone, not
   convergent, not everywhere-defined.
2. **Exactly algebraic, but no closed form.** `Q=u⁴` and `Q^r=u³/D(u)` are rational
   in `u=√q` over ℤ, so each crossing is a root of an explicit integer polynomial.
   Exact (sympy rational arithmetic + certified VAS/Sturm isolation, no floating
   point): irreducible degree **54** (n=6), **110** (n=8), **224** (n=11) ⇒ not
   expressible in radicals.
3. **q₀'s position is COINCIDENTAL.** Window reproducing the identical isotope
   sign-vector = (1.053650, 1.207893): **55.4 % of the branch, 0.852 bits, 54**
   systematically-generated natural constants inside. Robust — sweeping the upper
   bound over its full plausible range gives 41–81 % and 0.31–1.28 bits.

**Two corrections to the sibling reads** (both by measurement; arithmetic reproduces):

- **(A)** The Wenzl level eigenvalue has a **POLE** at `q* = 1.27844957657969`
  (root of `−u⁶−u⁴+u³+u²+1`, `u=√q`); above it the effective level `r` is
  **COMPLEX** (`r(1.45)=0.81+4.23i`). The n=9 crossings at q≈1.4285/1.4617 sit
  there, so they are not comparable to `q_cross(6)=1.054` as one trend. On the
  real-level branch T/³He have no crossing — which *extends* #4829's original
  scope-(a) statement rather than overturning it.
- **(B)** The **Z=N / Z≠N isospin pattern is an n-effect**, falsified by a fixed-n
  control at BOTH n=6 and n=12. In {D,T,³He,⁴He} isospin and strand count are
  confounded (Z=N ⟺ A even ⟺ n∈{6,12}), and ⁶Li/⁷Li *preserve* the confound.
  Holding n fixed: n=6 → D(1,1) 1.05365, pp(2,0) 1.06577, nn(0,2) 1.05677;
  n=12 → ⁴He(2,2) (1.02,1.03), ⁴Li(3,1) (1.01,1.02), ⁴H(1,3) (1.02,1.03).
  **All below q₀ regardless of isospin.** No isospin argument is needed or
  supported; the corpus mirror/isospin machinery was NOT invoked because there is
  no surviving effect to explain.

**⁶Li/⁷Li are unaffordable by a HARD BOUND, not a sandbox limit.** The trace costs
`O(L·Σ_λ dim²)` and `Σ_{λ⊢n} dim² = n!` exactly, so n=18 is **1.34e7×** and n=21 is
**1.07e11×** the n=12 cost (≈14 yr and ≈10⁵ yr per grid point). The sparse fix
removed a dim³→dim² factor, not the factorial. **Do not queue those runs.**

**The sequence that IS structured** (and it is not `q_cross`): `s_λ = 0` whenever a
cell has `r + c(x) = 0`, so at integer level `r=k` every λ with `ℓ(λ)>k` drops out.
Ladder `r(q_k)=k` solves `Σ_{j<k}u^{4j+3} = u^{4k}+u^{4k+2}`: `q_2 = 1` exactly,
`q_3 = 1.15416065…`, increasing, accumulating at `q*`. Since `r→2⁺` as `q→1⁺` this
explains the O(10⁻⁵) values #4829 saw near q=1. **`r(q₀) = 2.5995` — on no rung.**

**Lean (sorry-free):** `QOU/BraidsAndKnots/WenzlLevelStratum.lean` — a partition
with >k rows has a cell of content −k, hence the specialisation numerator vanishes
for the whole `ℓ>k` stratum. Generic `Field K` (§7c, no ℝ); `lean`-direct exit 0;
`#print axioms = [propext, Quot.sound]`; two `decide` guards show the row-positivity
hypothesis is load-bearing.

**Cross-validation** via an independent normaliser path (dual-Cauchy closed form
`Z=((1−Q^r)/(1−Q))^n`, verified to 2.8e-41 — never `y_lambda_at_q0_mpmath`):
D 1.053650 vs #4829's 1.05365; character-free n=6 1.024447 vs 1.02445; ⁴He 1.020923
vs #4832's 1.02092; D's far diagnostic crossing 3.4101 vs #4832's late fix. ⁴He
additionally has a **second** on-branch crossing at **1.207893**.

Scope-(a) throughout; **no scope-(b) exclusion claimed anywhere**.

---
## NA-Stokes trefoil discretization BUILT — route resolves NEGATIVE (PR #4798, 2026-08-08)

Cherry-picked onto main 2026-08-09 (the PR's own branch carried a STALE copy of this
bean, pre-dating the LEAD-1/LEAD-2/sign-crossing records, so only its two content
files were taken and this record was written fresh).

This BUILDS the thing the "Surviving direction" section above named as the wall:
"needs a canonical discretization of the Yekutieli surface 2-form on the trefoil
Seifert surface — data the corpus lacks." That data now exists.

Construction (genus 1, trefoil σ₁³): Seifert matrix V=[[-1,1],[0,-1]], intersection
form J = V − Vᵀ = [[0,1],[-1,0]]; germ q-curvature F_q=[δq₁,δq₂] built two
principled ways (log germ; q-derivative germ) in the 2-dim Hecke rep; surface-ordered
½∮∮[𝓕,𝓕] = J_ab[𝓕_a,𝓕_b] with 𝓕_k = U_k⁻¹ F_q U_k, across natural handle holonomies.

RESULT = scope-(a) NEGATIVE, and it is the SHARP one for this route:
- The transverse term IS genuinely nonzero on the single-generator σ₁³ channel — it
  survives where the whole inter-crossing Magnus tower vanishes. So the object is real.
- BUT c₂ = ‖Ω₂^⊥‖/h² ranges over 0 … 897 across the natural germ/handle choices and is
  NEVER ≈ 1 (the g₂ ≈ 1.0087 that would close the deuteron). Sample: (q-deriv germ;
  s₁,s₁²) → 0; (q-deriv; s₁,s₂) → 897; (log; s₁,s₂) → 617.
- The surface→scalar map therefore carries O(100×) GAUGE FREEDOM the corpus does not
  fix: the germ normalization plus the two H₁ handle holonomies.

CONVERGENCE (why this matters beyond its own negative): this is the NUMERIC counterpart
of #4818's Lean wall `transverse_nonzero_needs_noncommuting_curvature` — the Lean says a
nonzero pairing forces position-dependent transported curvature; #4798 measures exactly
how underdetermined that transport is. Same wall, two languages. Together with #4818's
`listPairing_trace_zero` (and #4619's tr[A,B]=0), the picture is: the missing term is
invisible to the scalar trace AND its transverse realization is gauge-underdetermined.

REVIVING THE ROUTE needs a NEW PRINCIPLE fixing the germ + the two handle holonomies —
not another discretization sweep. A c₂ selected because it lands near g₂ would be the
forbidden fit. Honest scope: negative on the NATURAL discretizations tested; does NOT
prove no discretization works (no invariant proved ⇒ scope-(a), not scope-(b)).

Nothing wired, no fit, free_parameters=0. Bean stays OPEN.

Files: docs/audits/2026-08-08-nastokes-surface-curvature-trefoil-negative.md;
computations/probes/nastokes_surface_curvature_trefoil_probe.py.

---
## GAUGE QUESTION ANSWERED — the transverse route closes NEGATIVE (PR #4848, 2026-08-09)

Ran the one question #4798 left: *is there a derived principle fixing the germ
normalization and the two H₁ handle holonomies?* **YES — and it determines c₂ = 0,
not the c₂ ≈ 1 that would close the deuteron.** Bean stays **OPEN** (magnitude untouched).

**Phase 0 (the corpus already pinned BOTH gauges — no new principle needed):**
- *Transport*: `QOU.MathlibExt.YekutieliIntegration.holonomy = List.prod` in path order
  (+ `holonomy_append`) fixes the ordering; Seifert's algorithm on a braid closure puts
  discs↔strands, bands↔letters (`seifertBettiOne = c−s+1`, #4818). Together these make the
  transport to band k the ORDERED PARTIAL PRODUCT — so on the deuteron word σ₁³ **every**
  admissible transport is a power of ρ(σ₁). ρ(σ₂) is not in the word ⇒ #4798's `s1,s2` and
  `s2,s1s2` rows are INADMISSIBLE, not alternative gauges.
- *Germ*: `def:germ-commutator-q-curvature` defines δq as a germ-level increment **of q**,
  i.e. the logarithmic q-derivative. #4798's competing "log σ" is the braid-direction
  CONNECTION 1-form, not a q-germ (and is not a root vector — defect 14.48), so its
  294/617/251 column measures the wrong object.
- Negative Phase-0 findings (don't re-search): no corpus block assigns holonomies to
  Seifert H₁ handles; no Seifert-matrix convention beyond the standard V; `_deprecated/`
  Yekutieli per-cell probes are unrelated to surface transport.

**Derivation (exact, q-INDEPENDENT):** in the 2-dim Hecke rep the two q-derivative germs
are the constant matrices δq₁ = H−2E, δq₂ = −H, so F_q = [δq₁,δq₂] = **−4E** — a PURE ROOT
VECTOR (traceless, nilpotent) with **Ad(ρ(σ₁))F_q = −q²·F_q** (eigenvalue = the ratio of
σ₁'s Hecke eigenvalues). Hence every transported curvature 𝓕_k = (−q²)^{−k}F_q lies on ONE
LINE ⇒ [𝓕_i,𝓕_j] = 0 for all i,j ⇒ **Ω₂^⊥ = Σ J_ij[𝓕_i,𝓕_j] = 0 for EVERY intersection
form, EVERY H₁ basis/spanning tree, EVERY handle assignment.** The handle gauge never
needed fixing — the answer does not depend on it. Robust to any transport in the Borel
containing ρ(σ₁), i.e. to everything σ₁³ can build.

**SCOPE-(b) structural exclusion, RESTRICTED to single-generator (2,L)-torus channels.**
Cited invariant: the Ad(ρ(σ₁))-eigenvector property (Lean-proved). **Multi-generator words
(A ≥ 3) are explicitly NOT excluded** — there the eigenvector property fails and the object
is generically large (#4798's 896.71 is evidence of that); that stays scope-(a) open.

**Consequence — the σ₁³ channel is order-2 STERILE in BOTH directions:** longitudinal
inter-crossing Magnus tower = 0 (N2, single generator) AND transverse surface curvature = 0
(this PR). So the deuteron −9.2% / bar-even g₂·h² residual is **not a second-order NA-Stokes
effect at all**, and **g₂ ≈ 1.0087 now has NO NA-Stokes explanation** — it was never derived
and must not be wired. This CLOSES the LEAD-2 geometric surface-curvature route for the
deuteron with a named invariant, instead of parking it behind an unmeasurable gauge.

**DO NOT REDO:** any transverse-pairing / surface-curvature closure on a single-generator
channel, under any germ normalization or handle convention — the vanishing is
gauge-independent.

Lean (sorry-free, `lean`-direct exit 0, `#print axioms` clean on all 16 decls —
[propext, Classical.choice, Quot.sound], no sorryAx): `QOU/MassTheory/GermRootVectorGaugeFixing.lean`
(abstract layer generic CommRing/Ring per §7c; concrete layer generic Field; braid + Hecke
relations proved, so the matrices are certified Hecke generators). Seam recorded: the step
∂_q σ_i = ds_i is by-hand entrywise differentiation (sympy checks it independently) — cite
"Lean proves the commutator of the constant germs is the root vector", never "Lean proves
the germ is the q-derivative".

free_parameters=0; g₂ used ONCE, post-hoc, after the value was fixed by the principle;
AME never inverted; experimental proton anchor (immaterial — everything is q-independent).

Files: docs/audits/2026-08-09-nastokes-gauge-fixing-germ-root-vector.md;
computations/probes/nastokes_germ_root_vector_gauge_probe.py (+witness, 7/7 assertions).

**Surviving units:** (1) transverse pairing on multi-generator words — is it super-pairwise?
(still killed by the scalar trace, so needs a non-trace functional, itself an open licence
question); (2) g₂'s origin, now unexplained; (3) the super-pairwise extensive term, the
actual magnitude gate, untouched.

---
## Multi-generator (A >= 3) transverse pairing — PR #4849 (2026-08-09)

**Bean STAYS OPEN.** Runs the case #4848 explicitly left open. Supplies one input
to the >= 3-body term; closes no magnitude.

**1. The canonical A >= 3 words ALREADY EXIST** — `mass_at_3A_proper.atom_braid_word_3A(Z,N)`.
#4818's "the corpus lacks the canonical multi-nucleon Seifert braid word" is
superseded. D 6 strands/23 letters/gens 0-4; T,3He 9/35/0-7; 4He 12/47/0-10.

**2. SCOPING: every atom word is MULTI-generator, including the deuteron.** #4848's
scope-(b) is stated (correctly) for single-generator channels and covers the reduced
pn-CHANNEL word sigma_1^3 / trefoil. The 6-strand deuteron ATOM word that the
mass/binding compute consumes is a different corpus object and is NOT covered. Do not
transfer "the deuteron channel is order-2 sterile" from one to the other.

**3. VERDICT: SUPER-PAIRWISE (scope-(a)+).** With #4848's pinned conventions
(Yekutieli ordered partial products; Seifert bands<->crossings; log q-derivative germ)
in the corpus seminormal rep of H_12(q) (all A=2,3,4 words in ONE algebra):
Omega != 0; Moebius cluster residuals ||R3|| in [8.3, 2.0e4] and ||R4|| in [83, 2.3e4]
over 81/30 coupled readings. He4 cluster budget (band-local): 1-body 20.7%,
2-body 82.0%, **3-body 49.2%**, 4-body 0.0% of ||Omega||. So it clears #4818's
pairwise cap -- a NECESSARY property of the missing term.

**4. But the LEAN says that content is TRANSPORT, not curvature.**
`QOU/MassTheory/TransversePairingClusterDecomposition.lean` (sorry-free, generic Ring,
#print axioms <= [propext, Quot.sound] on all 11 decls): listPairing is BILINEAR, so
`listPairing_append` decomposes it exactly into 1-block + 2-block terms and
`moebius3_eq_zero` / `moebius4_eq_zero` vanish IDENTICALLY at fixed curvature lists.
=> the entire measured super-pairwise content is context-dependence of the Yekutieli
transport. Nothing three-body about the curvature.

**5. NEGATIVE (scope-(a)-): the value is NOT determined.**
- germ observer pair: 16.4x spread (0.342 band-local / 0.960 (0,1) / 2.265 (3,4));
  def:germ-commutator-q-curvature says "two independent observations", not WHICH two
  for n > 3. Derived prune: only ADJACENT pairs give F != 0 (|i-j|>=2 gives exactly 0)
  -- narrows to n-2 candidates, does not choose.
- **nucleon ORDERING: 1.13x** (T pnn/npn/nnp 0.960/1.007/1.087; He4 six orderings
  0.528-0.596). A many-body binding term is a function of the NUCLEUS; the corpus's
  own scalar observable is ordering-invariant (tr_M(beta)=tr_M(rep) exactly). This one
  is a function of the braid word. **This is the sharp negative.**
- lambda: only 1.03-1.10x across 5 partitions of 12 (dim 11-165, 2-6 rows) -- the one
  axis where it IS robust.

**6. Two facts worth carrying forward.**
- The germ is **q-DEPENDENT for A >= 3**. delta q is q-free only where every axial
  distance is +-1 (the 2-dim case #4848 worked in); at |rho|=2 it is manifestly
  q-dependent. He4 R3/||Om|| = 0.528 at q0 vs 0.185 at q=1.25.
- **The germ transforms like a CONNECTION, not a tensor**, under a q-DEPENDENT basis
  change: dq -> B dq B^-1 + (1 - Ad sigma)(q (d_q B) B^-1). The seminormal basis is
  q-dependent; the reduced-Burau basis of #4798/#4848 is a different gauge. #4848's
  conclusion is unaffected (0 in every gauge) but any NONZERO value inherits this.

**Revival needs two PRINCIPLES, not another sweep:** (i) which two germ observers
(+ the representation gauge); (ii) a nucleon-symmetric readout. Until both exist a
number off this object is a gauge choice.

free_parameters = 0; no AME input anywhere (not even a post-hoc comparison -- there is
no determined value to compare); q0 = experimental proton anchor; nothing wired.

Files: docs/audits/2026-08-09-nastokes-multigenerator-cluster-additivity.md;
QOU/MassTheory/TransversePairingClusterDecomposition.lean;
computations/probes/nastokes_multigen_cluster_additivity_probe.py (+witness, 16
assertions all passing, 40 s wall).

---
## Principle (i) RESOLVED — dissolved, not solved (PR #4850, 2026-08-09)

Branch `claude/nastokes-orbit-symmetric-readout-2026-08-09`. Bean stays **OPEN**.

#4849 named two principles as the price of reviving the transverse route:
(i) a nucleon-symmetric readout, (ii) which germ observer pair. **(i) is now
answered, and the answer removes the blocker rather than satisfying it.**

**1. Is orbit-symmetry FORCED?  YES — and it is VACUOUS.**
The corpus orbit identity `tr_M(beta) = tr_M(rep)` is over `S_Z x S_N` ONLY, and
its **Lemma 1** (2026-05-30 orbit-trace proof) establishes it by showing such a
permutation leaves the braid WORD unchanged: it fixes the ordering string and
preserves every adjacency type. Measured: the `S_Z x S_N` orbit of ordering
STRINGS is a SINGLE POINT for D/T/He3/He4 while |group| = Z!N! (up to 4). So
symmetrization over the forced group is the **IDENTITY MAP** — Lean-proved
sorry-free for an ARBITRARY readout into an ARBITRARY AddCommMonoid
(`sum_symmetrize_eq_nsmul`). Every symmetry statement in the corpus
(atom_orbit_reduction, IdenticalParticleSymmetrization.lean,
symmetrized_binding_probe.py) is over `S_Z x S_N`; none covers a cross-species
reordering.

**2. Does R survive?  YES — trivially, by derivation.** The derived readout IS
the readout on the canonical word. The NON-derived S_A counterfactual average
does not cancel either: ||<R>||/mean = 0.9858 / 0.9957 / 0.9998 (T) and
0.9746 / 0.9854 (He4) across all three of #4849's germ readings. He4 band-local
4-body level reproduces #4849's empty result (1.5e-11).

**3. #4849 section 5.1's ordering disqualifier is VOID.** The permutations it
varied (pnn/npn/nnp) are CROSS-SPECIES: not in `S_Z x S_N`, not covered by any
corpus identity, and not a symmetry at all (p and n are distinguishable).
DECISIVE CONTROL — the corpus's OWN scalar observable is cross-species
ordering-DEPENDENT:

    T   tr_M(pnn) = tr_M(nnp) = 0.10407   tr_M(npn) = 0.14158   -> +36.0 %
    He3 tr_M(ppn) = tr_M(npp) = 0.20658   tr_M(pnp) = 0.16336   -> -20.9 %
    D   tr_M(pn)  = tr_M(np)                                    -> 1.5e-41 (null control)

i.e. THREE TIMES the 13 % that #4849 treated as disqualifying. tr_M tracks the
interface multiset exactly (bit-identical within a class). Computed from the
certified Frobenius pairing sum_lambda y_lambda chi^lambda: tr_M(1) = 1, Markov
M1 to 4e-16, and a CONSTANT M2 stabilisation ratio z = 0.499320334184 to 6e-16
(M1 alone holds for any character weights; the constant M2 is what pins y_lambda
as Jones-Markov weights). D is the null control — its two orderings share one
interface multiset, so invariance there is required, and it holds to 1.5e-41 at
40 dps: the machinery does not manufacture spurious ordering differences.

**4. NET: blocker (i) is GONE; blocker (ii) is UNTOUCHED and STILL BINDING** —
which two germ observers (16.4x spread, #4849 s4.4) plus the unpinned
representation gauge of the connection-like germ (#4849 s2.3). The transverse
route is STILL BLOCKED, now on one principle instead of two. No magnitude, no
Delta_lambda, nothing wired, free_parameters = 0, no AME quantity and no g_2 in
the compute, q0 = experimental proton anchor with live y_lambda_at_q0_mpmath
(never the muon cache).

scope-(b) for the vacuity claim ONLY (proved invariant cited: the word is a
function of the species string). scope-(a) for everything else.

**SEPARATE ITEM SPUN OUT (not a transverse-route matter).** The corpus's
canonical cross-species ordering `p...pn...n` is a CHOICE: the orbit identity
does not license it (it covers only `S_Z x S_N`, under which the arrangement
never varies), "interface-minimal" is stated as a COST property rather than a
physical selection rule, and item 3 measures that the canonical trace DEPENDS on
it by O(10 %) for every A >= 3 mixed-species isotope. Filed as its own bean.

Files: docs/audits/2026-08-09-nastokes-orbit-symmetric-readout.md;
QOU/MassTheory/NucleonOrderingSymmetry.lean (exit 0, zero warnings, #print axioms
clean on all 8 decls, purely combinatorial — no ring, no R);
computations/probes/nastokes_orbit_symmetric_readout_probe.py (+witness, 17
assertions all passing, 162 s wall).

---
## Cross-reference 2026-08-09 — the #4850 §7 fallout item is resolved far enough to report (qou-48is / PR #4851)

The ordering item spun out of this bean is now traced. Two results relevant here:

1. **The deuteron is EXACTLY ordering-independent**, and provably so for every
   weight function: A=2 has a single interface class, so the interface product is
   arrangement-invariant (`ifaceProd_deuteron_ordering_independent`, sorry-free in
   `QOU/MassTheory/CanonicalOrderingSaddle.lean`). The ordering ambiguity does NOT
   reach the deuteron magnitude. Nothing in this bean needs an arrangement caveat.

2. **#4849's ordering disqualifier is doubly void.** The 36% swing #4850 measured
   on T is structural, not noise: the production interface product factorises as
   P(o)/P(canonical) = (f_pn/f_pp)^(b_p-1) (f_pn/f_nn)^(b_n-1) over p-/n-block
   counts, verified on all 3140 arrangements with Z,N<=6 to 8e-51, and reproduced
   independently by two full H_{3A} Markov-trace pipelines (rel 1.1e-8, 3.4e-14).

Also worth knowing for any A>=3 extension of this bean: production hardcodes the
sorted arrangement while the corpus's own prop:ground-state-ordering selects the
INTERLEAVED one for A>=4 (opposed in sign on the production readout). Anything
reported at A>=3 must state which arrangement it used. See
docs/audits/2026-08-09-canonical-ordering-dof-production-impact.md.

This bean (deuteron Delta_lambda magnitude) stays OPEN and is unaffected.


--------

## Update 2026-08-09 — Ω₂ IS NOT GAUGE-COVARIANT (PR #4856, branch claude/germ-gauge-covariance-2026-08-09)

Ran the question #4849 §2.3 left open. **VERDICT: not covariant.** The transverse
NA-Stokes route is closed at the level of the OBSERVABLE, not of its value.

**The algebra** (Lean sorry-free, generic `Ring R`, `#print axioms` clean on all 48
decls, umbrella-registered — `QOU/MassTheory/GermConnectionGaugeCovariance.lean`):

- `germ_mul` — the germ `α(u) = (Du)u⁻¹` is a **1-COCYCLE**: `α(uv) = α(u) + Ad(u)α(v)`.
  So it is defined only modulo the **coboundary** `(1 − Ad u)Θ` — that IS the gauge.
- `germ_conj` — the connection law: `α ↦ Ad(b)(α + (1 − Ad u)Θ)`, `Θ = b⁻¹(Db)`.
- `germCurvature_covariant_iff` + `gaugeDefect_ne_zero` — covariance holds IFF a defect
  vanishes, and a concrete ring/derivation/units triple has `Δ = !![X², −2X; 0, −X²] ≠ 0`.
- `listPairing_map_adAct` — the pairing is covariant GIVEN covariant inputs, so ALL of
  the failure sits in `F_q`, none in the transports or in the pairing.
- `cupSq_eq_neg_coboundary` — **the covariant order-2 object is ZERO**: the bracket cup
  square `⟦α(u), Ad(u)α(v)⟧` is EXACTLY `−∂β` with explicit primitive `β = q∂_qα`.
- `trace_germ_conj` — `τ(α(w)) = q∂_q log det ρ(w)` IS gauge-invariant, but abelian:
  pure writhe/framing, already walled by `no_writhe_only_framing`.

**The measurement** (`computations/probes/nastokes_germ_gauge_covariance_probe.py`,
15/15 assertions, 4.4 s; witness `nastokes-germ-gauge-covariance.witness.json`):

- exact over ℚ(q) in the 2-dim rep: connection law verified both-sides-independently;
  defect `Δ = −3q²H − 2E − 2q²F ≠ 0`; cup-square identity exact on all 25 word pairs.
- real ⁴He atom word `atom_braid_word_3A(2,2)`, H₁₂(q): covariance defect
  `‖Ad(B)⁻¹Ω₂′ − Ω₂‖/‖Ω₂‖` = **0.78 … 14.4** (0 iff covariant), gauge diag(1,q,…,q^{d−1}).
- **readout-independent**: seminormal λ=(11,1) vs REDUCED BURAU (same rep — character
  equality 1.7e-15 on 40 random words) give **different conjugation-invariant `tr(Ω₂^k)`**
  — `tr Ω₂²` even changes SIGN. Conjugate operators have equal trace powers, full stop.

**Consequences.**
1. #4849's 16.4× germ-observer spread is **VOID, not open** — nothing to choose between.
   ‖Ω₂‖ was never invariant on two counts (object not a tensor; Frobenius norm not
   invariant under non-unitary B).
2. **Retro-narrows #4848**: its `Ω₂ = 0` on `σ₁³` is itself gauge-dependent (in the gauge
   diag(1,q) the curvature is no longer an Ad(σ₁)-eigenvector and `Ω₂ ≠ 0`). Its algebra
   is correct; its "every gauge" ranged over J and handle exponents, not over
   q-DEPENDENT regaugings. #4849 §2.3's "zero in every gauge" parenthetical is too strong.
3. Structural reason the route was never going to work: `q` is ONE direction and a
   curvature needs TWO; the generator indices i,j are group elements, not base
   directions. The "transverse surface curvature" was never a curvature.

**Scope.** (b) for non-covariance (proved obstruction: cocycle + nonzero defect +
invariants differing across two realizations of one rep). (b) for the cup-square
vanishing (exact identity, primitive exhibited). **(a)** for "no OTHER nonzero covariant
functional exists" — NOT claimed; one exists (the abelian trace) and a classification of
invariants of `[α] ∈ H¹(B_n; 𝔤𝔩_{Adρ})` is open.

**Do NOT redo.** Any transverse-pairing magnitude extraction under any germ
normalisation, handle convention, intersection form, observer-pair rule, or basis. No
sweep can recover an object with no basis-independent value. A future attempt must work
with the class `[α] ∈ H¹` itself — noting its cup square vanishes and its invariant
linear functional is the already-walled writhe.

`free_parameters = 0`; no AME, no g₂, no binding number in the compute. q₀ = experimental
proton anchor (germ is q-dependent at A≥3, so the pin is material). Nothing wired.
Audit: `docs/audits/2026-08-09-germ-gauge-covariance-verdict.md`.

**The ≥3-body binding MAGNITUDE gate is untouched. Bean stays OPEN.**



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-09 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- **Round 90 (`https://github.com/litlfred/qou/pull/8410`, head `507a878f2b14ab11470e7af5019207b486d15e86`)**: Formalized theorem + 80-dps witness (`status: in-progress`).
