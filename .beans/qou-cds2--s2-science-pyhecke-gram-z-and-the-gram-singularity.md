---
# qou-cds2
title: 'S2 (SCIENCE): pyhecke.gram.z and the Gram singularity — the ruling answers the convention, not the singularity'
status: in-progress
type: task
priority: high
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-15T00:00:00Z
---

Parent: `qou-cdx1`. Predecessor: `qou-wgta` item 11. **Highest-risk item in the
plan.** Blocks `qou-cdh2`.

## The state the ruling inherits

`trace-convention-registry.json → blocked_migrations[0]` was the registry's only
`owner_decision_required: true`:

> `tools/pyhecke/python/pyhecke/gram.py::z` **stays C**, because
> `G_INV = np.linalg.inv(G)` runs at **module import**, and under D the
> Markov–Gram form on the `H₃(q)` NF basis is **SINGULAR** — exactly one null
> direction (the row-cap one).

Measured at the proton pin: bilinear eigenvalues
`−0.752702, 0, +0.752702 ×3, +4.230339`; `det 3.998e-17`; `cond 4.9e16`.
**numpy raises nothing** — it returns entries up to `7.6e15` with
`‖G·G_INV − I‖ = 1.64`. Switching that one line silently corrupts every consumer
of `G_INV`.

**The 2026-08-15 ruling removes the convention question. It does not remove the
singularity.** That is the whole content of this bean.

## Corank accounting

`n=3` corank 1; `n=4` corank 10 (`3²+1²`); `n=5` corank 78 (`6²+5²+4²+1²`).

## The named repair

Quotient by the radical — `QOU/QBeta/GramSignature.lean`. Post-retraction the
quotient is a genuine **positive-definite** inner product, so the repair is more
attractive than it first looked. The supporting Lean already exists in
`QOU/QBeta/MarkovGramDegenerate.lean`:

1. `TemperleyLiebTower.conventionD_kills_antisymmetriser` — the pin forces `y_(1³) = 0`
2. `block_mem_radical` — a zero-weight block lies in the trace radical
3. `gram_det_eq_zero_of_radical_combination` — hence `det G = 0`
4. `TemperleyLiebTower.traceRadical_two_sided` — the quotient is a ring
5. `pairing_descends` — the pairing is constant on radical cosets
6. `mem_radical_of_pairing_zero` — and is non-degenerate on the quotient

## Signature caveat — quote only the post-retraction statement

Quote `QOU.QBeta.GramSignature` **only after** its in-file retraction (commit
`748ba9b1`). The original *"(5,1) under C, (4,1)+null under D, LORENTZIAN"* used
the **bilinear** pairing and is **WITHDRAWN**. The Hecke `*`-structure is
`T_w* = T_{w⁻¹}`, giving C `(6,0,0)` positive definite and D `(5,0,1)` positive
semidefinite. The **singularity** under D is common to both pairings and is the
only thing the dependent blocks rely on.

## Blast radius

`G_INV` is **exported at import**, so every consumer of `pyhecke.gram` is
affected — that is the 13 re-exporters + 13 consumers of `qou-cdh2`, plus
whatever imports `gram` directly.

## Two findings from the TL_n survey (PR #5241, 2026-08-16)

**1. `pyhecke/gram.py` is internally CONVENTION-SPLIT.** The float64 `z`
(L175) is convention D; but `z_mp` / `tr_m_mp` (L622-652) and
`gram_matrix_mp` (L746) are still convention **C** (`1/(sqrt q + 1/sqrt q)`),
per their own docstrings. So the 50-dps path and the float64 path in the SAME
MODULE do not build the same form — anything reading `gram_matrix_mp` is not
reading the same object as `G`.
Note this is exactly the "returned, not assigned" spelling that PR #5124
showed `scripts/convention-c-producer-audit.py` is structurally blind to, and
`1/(sqrt q + 1/sqrt q)` equals `sqrt q/(q+1) = z_C` exactly. Relevant to the
C-excision tranche (qou-cdx1) as well as to this bean.

**2. The singularity has a principled fix, not just a guard.** The radical is
exactly `ker(H_n -> TL_n)`, dimension `n! - Catalan(n)` (= 1 at n=3), proved
sorry-free for all n by
`QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff`
(docs/audits/2026-08-16-tl-all-n-weight-vanishing.md). On the 5-dimensional
TL_3 quotient the form is genuinely NON-SINGULAR — so the pinv at
`gram.py:407` / the rank-one-shift Moore-Penrose at `gram.rs:339` are
working around a degeneracy that disappears if the form is built on TL_3 in
the first place. Costed in bean `qou-8iru` at ~2-3 days, moderate-high risk
(touches Rust engine + Python wrapper + confinement-operator-selection);
should be its own PR.

Also surfaced: `qbeta_crossing_weight_hecke_probe.py:128` does an UNGUARDED
`np.linalg.solve` against this same singular form — the one site with no
degeneracy handling at all. Split out as bean `qou-yof3`.

## MEASURED 2026-08-18: the singularity is EXACT, not a conditioning artifact

This bean held two readings at once and did not separate them:

  det 3.998e-17, cond 4.9e16          (looks ill-conditioned)
  'np.linalg.inv is inverting rounding noise -- which is exactly the observed
   cond 4.9e16'                        (says it is noise)

Both are consistent with the float64 data.  The distinction decides whether
quotient-by-the-radical is the right repair or an over-reaction, so I measured
it instead of inferring.

Probe: computations/qbeta/gram_convention_d_singularity_structural_probe.py
(3/3, witness gram-convention-d-singularity-structural.witness.json).  Rebuilt
the 6x6 Gram at 30/60/120 dps from pyhecke's own _nf_of_word_mp / NF_BASIS,
swapping ONLY z:

   conv   dps       |det|         cond      min|eig|
      C    30     0.189205        34.16     0.101797
      C    60     0.189205        34.16     0.101797
      C   120     0.189205        34.16     0.101797
      D    30            0    9.748e+31   4.33951e-32
      D    60            0    3.331e+61   1.26988e-61
      D   120            0   1.587e+121   2.6656e-121

|det| under D is EXACTLY ZERO at all three precisions -- not small, zero.  And
min|eig| falls ~30 orders per 30-dps step, i.e. pinned to epsilon rather than
converging to a nonzero limit.  That is an exact null direction being resolved.
C is rock-steady (|det| 0.1892, cond 34) at every precision, so the collapse is
attributable to z alone.

VERDICT: the bean's float64 reading is that exact zero seen through f64
epsilon.  The form is genuinely rank-deficient, the radical is genuinely
nontrivial, and quotient-by-the-radical is a STRUCTURAL fix, not a numerical
patch.  The repair is correctly aimed.

## Correction to my own probe, recorded

My first assertion tested '|det| collapses by >20 orders as dps rises' and
FAILED -- because the outcome is stronger than the test: |det| is exactly 0, so
the comparison "0 < 0/1e20" is false.  Rewrote to test (a) det exactly zero at every dps and
(b) min|eig| tracks working precision.  A test written for 'very small' does
not fire on 'exactly zero'.

## Also found: gram.py has NO convention-D path at all

Both gram_matrix_mp (line ~747) and z_mp (line ~634) hardcode
z = 1/(sqrt(q) + sqrt(1/q)).  That IS sqrt(q)/(q+1) -- a detector-blind C
spelling.  Anyone measuring D through gram.py measures C without being told.
The probe therefore reimplements the construction rather than calling it.

## Already done in gram.py (this bean understates its own progress)

G_INV is GONE rather than rebound; G_PINV = np.linalg.pinv(G) exists; and
safe_inverse() (line 542) raises the singularity guard numpy does not give.
The silent-corruption hazard the bean leads with is already mitigated at
source.  What remains open is the convention switch itself plus routing
consumers through the quotient.


## 2026-08-19 — the module was straddling C and D internally; migrated (commit ab11d493b, PR #5265)

Owner directive: "d path. no float64."

**The straddle.** The f64 `z` went D on 2026-08-15; the mpmath mirror stayed
C. 0.6126880371464652 vs 0.4993203341836944 — 22.70% apart inside one
module, with BOTH docstrings asserting lockstep. Two consequent false
claims: `gram_matrix_mp` said it "agrees with G to ~1e-15" (real gap 0.172),
and `z_mp` warned that splitting the mirror "would be strictly worse than
the stale convention" while describing the live state. The C spelling was
the detector-blind `1/(sqrt(q)+1/sqrt(q))` = `sqrt(q)/(q+1)` from PR #5124 —
a grep for the C form does not find it. Three sites migrated: z_mp,
tr_m_mp, gram_matrix_mp.

**Why not one line.** Under D the mp Gram is exactly singular and
`mp.lu_solve` DOES NOT RAISE — swept 20..120 dps it returned at every
precision with max|x| ~ 10^dps and residual ~1e-3. Same silent-corruption
shape as the numpy `np.linalg.inv` behaviour this bean was opened for. One
arrangement raised ZeroDivisionError; that is the exception, and "it would
raise so we'd notice" is the wrong lesson.

**Shipped** (float64-free, mirroring the f64 side): `radical_mp()`,
`gram_quotient_solve_mp()` (min-norm on H_3/rad, RETURNS the unreachable
radical component), `gram_inverse_mp()` (raises like `gram_inverse`).
Verified: lockstep 4.1e-18; G-vs-mp agreement 0.172 -> 2.1e-16 so the
docstring is TRUE again; quotient solve max|x| 0.90 vs lu_solve 2.9e50,
residual 1.7e-51, min-norm. pyhecke suite unchanged (21F/148P/13S with AND
without — baseline measured, the 21 are pre-existing native failures).

**NEW FINDING, not repaired.** `qbeta_braid_nf_sdp_offset_probe` assumes "G
is invertible (rank 6)". Under D both anchors carry a radical component of
~47% of NF norm (0.47268915 each, identically), so `G x = nf` is
UNSATISFIABLE and the question is ill-posed, not merely harder. I did NOT
re-solve on the quotient and re-report an angle — that laundering is exactly
what the anti-fit discipline forbids. The probe now refuses to run (exit 2)
with the measurement in the message. Re-derivation under D = separate work.

**NOT DONE — cds2 stays open.** 19 witness-emitting producers consume the mp
path (mass chain included: build_proton_mass_50dps_chain,
mass_formula_6term_mpfr_50dps, atomic_tr_m_*, paper_six_term_isotope_sweep,
rho_k_full_via_wenzl_lr, regenerate_y_lambda_mpfr). Every committed value
moves. Scoped bulk sweep with long-compute members per the qou-1c4y posture
— needs its own pass, not an idle drain.


## 2026-08-19 RETRACTION — the "19 downstream producers" figure was wrong (commit d3875aac8)

The entry above says 19 witness-emitting producers consume the mp path, "mass
chain included", and defers regenerating them as a sign-off-gated bulk sweep.
**That is a substring-grep artifact.** `tr_m_mp` is a substring of
`tr_m_mpfr`, and my grep had no word boundaries, so it matched every file
that merely NAMES `atomic_tr_m_mpfr_50dps.py` in a docstring.

    substring grep (used)      26 files, 19 witness-emitting
    word-boundary grep (right) 13 files,  9 witness-emitting

**The mass chain is NOT downstream of the mp path** — verified per file:
every mass-chain hit is a string literal naming that producer, not a call.
Same error class as the detector-blind z_C spelling and the sibling's habiro
family, but in the OTHER direction: over-matching inflates a scope estimate
rather than hiding work, and drove a wrong "needs sign-off" decision.

**Of the real 9:** 2 are this branch's probes, 1 is the SDP probe already
guarded, and 4 ran clean and are regenerated — compound_shift_nf 19/19,
mass_formula_6term_mpfr_50dps 10/10, qbeta_confinement_sdp_offset_homogeneity
2/2, qbeta_lorentzian_gram_offset 3/3. The other 2 FAIL IDENTICALLY on the
pre-change baseline (atom_dual_q0_mpfr_demo: no path bridge;
proton_residual_rootcause: float() on mpc) — pre-existing, not D-induced. I
had begun attributing the second to the convention change.

**Lorentzian probe — a clean-looking regeneration worth distrusting.** It
moved (5,1) -> (4,1), i.e. a two-number signature for a 6x6 matrix whose
pos+neg is now 5. `signature()` now returns full inertia (pos, neg, zero):
**(4,1,1) at EVERY q from 1.02 to 2.5**, so the degeneracy is structural in
q. Header now carries the GramSignature retraction (748ba9b1): the Lorentzian
signature is the BILINEAR form's; the *-form tr(a·b*) is POSITIVE — (6,0,0)
C, (5,0,1) D. The "causal structure" reading is withdrawn.

**Still open:** the 2 pre-existing failures, and re-deriving
qbeta_braid_nf_sdp_offset_probe's question under D.

**Process note:** do not use `git stash` to baseline here — producers write
witness files and the pop collides (12 conflicts, including an unrelated
sibling branch's stash). Use `git worktree` / `git show HEAD:<file>`.


## 2026-08-19 — both consumer failures fixed; one hid a stale C-frame witness (commit 179f030c2)

Neither failure was where it appeared to be.

**atom_dual_q0_mpfr_demo** — could not be imported (`from pyhecke import gram`,
no sys.path wiring; `_path_bridge` does not reach outside computations/, and
must be imported FIRST because gram.py resolves `q_parameter` from
computations/substrate/ before falling back to the uninstalled `qou_substrate`).
That import failure had been masking two more: `wb.write()` does not exist
(API is `wb.save()`), and `float(res["duality_gap"])` raises when the solver
did not run. All three were swallowed by `hasattr` guards inside a bare
`except Exception` printing "(witness emission skipped)" and exiting 0 — the
same "cannot fail loudly" shape as lu_solve on the singular D Gram. Now
returns 2 with an explicit message when the clarabel binary is absent, instead
of emitting a witness of Nones. It still cannot produce numbers here (needs the
Rust binary) and now says so.

**proton_residual_rootcause** — `float(phi0)` on an `mpc`. Obvious reading:
the |v|>=1 product fallback goes complex. MEASURED, THAT IS WRONG:
`PhiQ_euler_mpfr` returns mpc in EVERY regime (v=0.5 -> 378.207990286 + 0.0j,
well inside convergence), imaginary part exactly 0 at v = 0.1 … 1.2 at 50 dps.
Branch C could never run at all. Fixed with `_re()` which ASSERTS Im == 0 and
raises otherwise — a genuine imaginary part would be a fact about the
q-exponential, not a cast nuisance.

**The finding that unblocked:** its witness was committed but its producer had
been crashing, so it was never regenerated — and it is convention C:

    z_markov  0.49932033403356124  ->  0.6126880505488901

last touched 2026-08-10. This is C surface invisible by construction: no grep
finds it, because the producer that would rewrite it cannot run. Worth
checking whether other committed witnesses have crashing producers — that is a
detector class the campaign does not currently have.

**Gates:** all blocking GREEN; raw-float64 NEW (not baselined) = 0 — the 38
float64 fields in that witness were already baselined, so re-running adds no
violation. Draining them is separate and NOT claimed.

**State of the 9 real consumers:** 6 run clean, 2 are this branch's probes, 1
is the SDP probe that correctly refuses. Remaining cds2 item: re-derive that
probe's question under D.


## 2026-08-19 — the radical pairing IS the sign rep; the obstruction is UNIVERSAL (commit a4b310b07)

    <v, nf(beta)> = (-1/q)^writhe(beta)     exact, 13 words, writhe -3..+3, 1.3e-51

`-1/q` is the antisymmetric eigenvalue of (sigma-q)(sigma+1/q)=0 and the
q-antisymmetriser is its projector, so the radical pairing is beta's value in
the one-dimensional SIGN REPRESENTATION. It is what the radical IS. The pairing
depends on the word only through writhe (`s1 s2` and `s1^2` pair identically).

**Consequence.** G symmetric with kernel span(v) ⇒ range = v-perp ⇒ `G x = nf`
solvable iff `<v,nf> = 0`; a zpow of a nonzero base never vanishes. So
**`G x = nf` is unsatisfiable for EVERY braid** — not a bad anchor choice, not
fixable by another knot. That is what makes "re-solve on the quotient and
report an angle" a category error rather than a repair.

Lean `QOU/QBeta/RadicalPairingIsSignRep.lean`, sorry-free, generic Field,
axioms clean: signRepValue_append (from writhe_append), signRepValue_inv (from
writhe_inv; needs NO q≠0 — the linter caught the hypothesis as unused and
zpow_neg is unconditional), signRepValue_ne_zero, and
radical_pairing_ne_zero_of_sign_rep (measured identity as an explicit
hypothesis, not smuggled in).

**Method note worth keeping.** My first prediction used the NORMALISED pairing
`<v,nf>/<v,v>` and failed at every row — but the ratio was 0.22343503365538
in all of them, exactly 1/<v,v>. "Wrong by a constant factor at every point"
is a different signal from "wrong"; reading it as refutation would have
discarded a correct result.

**Where the missing piece belongs:** graded by WRITHE — precisely what the
Ocneanu trace does not carry (invariance needs a writhe prefactor OUTSIDE the
trace, Jones 1987 §5) and what D's pin kills outright
(conventionD_kills_antisymmetriser). Same writhe thread as the cds1
ladder-phase result, reached from the other end.

**NOT done:** re-posing the SDP on H_3(q)/rad. cds2's remaining work is that
re-derivation, now with the obstruction characterised rather than merely
observed.


## 2026-08-19 — the SDP offset angle is NOT an invariant under D (commit a0a8e5682)

Last open cds2 science item, and the answer is a sharp negative.

Under D the solution set is `x_0 + t*v` for ALL real t (`G v = 0`), and the
C-frame probe never imposed its net constraint as an input — it read the net
off as an OUTPUT — so t is free. Sweeping it:

    separation angle  in  [0.000899, 2.10987] rad   for t in [-1000, 1000]

essentially all of (0, pi). **The committed C-frame 0.355119 rad lies INSIDE
that range**, reachable at t ~ ±2.2 — so "does D reproduce C?" carries no
information whichever way it comes out. Hence this probe reports NO D-frame
offset angle.

**A trap I walked into.** I wrote a "quotient-intrinsic" reading (project off
the symmetric direction P(1)) and asserted in the output that it was
"t-independent by construction". It is NOT — v ⊥ P(1), so projecting off P(1)
leaves the t·v component untouched; the sweep gave 2.110 → 0.822 → 0.296 →
0.090 and refuted my own printed claim. The DOUBLE projection is genuinely
t-independent (2.10986587031 at every t out to 1e3) but only because
projecting off v IS the min-norm selection — the choice restated, not removed,
and Euclidean at that, on top of a metric the C witness already listed under
`untried_not_excluded`. **D needs two choices where C needed none.**

**Effect on the C result:** `homogeneity_broken: true` at 0.355119 rad was
well-defined ONLY because G is invertible under C. Scope-(a) — the measurement
stands in its frame; its PORTABILITY is withdrawn. Not a number that changes,
a number with no D counterpart absent an added choice.

**Also measured:** nf vectors are convention-INDEPENDENT (fold with h = q−1/q,
no z; committed C nf matches D recomputation to 8.5e-22). Every C/D difference
in this probe localises to G — the geometry, not the braid data.

**Deliberately NOT attempted:** choosing a canonical metric (the G-induced form
on the quotient, positive definite per GramSignature post-retraction) to make
the angle well-defined. Picking a metric so an angle comes out is the fit this
corpus forbids. Honest state: needs a structural reason to prefer one
representative.

### cds2 status
Science items are now DONE: convention straddle migrated, quotient API shipped,
obstruction characterised and proved universal, SDP question re-posed and
answered (negatively). All 9 real consumers run or correctly refuse. Remaining
is not science: draining the 38 baselined float64 fields in
proton-residual-rootcause, and the detector-class question of committed
witnesses whose producers crash.
