---
# qou-prjo
title: 'GAP: deuteron Delta_lambda magnitude — naive per-pair z dead across A; surviving object is transverse NA-Stokes surface-curvature (not braid-word, not scale, not level, not edge, not DT-count)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T19:09:10Z
updated_at: 2026-08-09T01:30:00Z
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
