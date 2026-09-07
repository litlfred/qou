---
# qou-sv7h
title: 'Binding compute cannot scale: sparse path unreachable, zero Rust, float64 straddle'
status: in-progress
type: task
priority: high
created_at: 2026-08-30T15:41:58Z
updated_at: 2026-09-07T14:14:57Z
---

Full measured analysis: `docs/audits/2026-08-30-binding-compute-scaling-bottleneck.md`.

Blocks `qou-i7ju` (hadron-knot-table regeneration). The regeneration is not the
problem; the producer cannot finish its second atom.

## Localisation

Every stage of `compute_atom` is sub-millisecond except `binding_energy`.
Inside it, `unified_iterative_correction` is the whole cost. 11/11 py-spy
samples on `hecke_core_legacy.py:1102` = `np.asarray(A) @ np.asarray(B)`.

## The six findings

1. **The O(dim*nnz) sparse path is unreachable.** Guard is
   `if s['sparse'] and not exact_chain:`, and `exact_chain` is True for EVERY
   physical chain (measured over all nucleon/prev/n_gens combos). Coefficient
   histogram: ('int','int') 132, ('int','mpf') 132, ('float','float') 48 -- the
   mpf are real 50-dps values, and `c` is int 1 which is not a float. So both
   inner branches are dead, INCLUDING the COO object accumulator written for
   exactly this case. Everything runs O(dim^3) at dims up to 2310.
   Deuterium ~40 days; Fe-56 ~16 years.
2. **Zero Rust in the hot file.** grep pyhecke_native|hecke_engine in
   hecke_core_legacy.py -> 0 hits.
3. **The Rust MPFR matmul exists and is not exported.**
   `dense_dense_mul_mpfr` in dense_la_mpfr.rs, called 16+ times inside Rust,
   has no #[pyfunction]. Python gets inverse/kron/nullspace but not multiply.
   Measured Rust speed >=24x the Python path at dim 16 (401us vs 9600us), and
   that is a lower bound (includes PyO3 + seminormal construction).
4. **Half the matmuls are float64.** Counter recorded
   {'float64': 275, 'object': 271}. Measured relative error vs an all-mpf
   reference: 1.40268e-16 = float64 eps, in a 50-dps producer. Also
   `q_parameter.Q` and `h` are Python floats; intra-nucleon coefficients are
   50-dps mpf but the inter-nucleon nn crossing carries float64 -h. A straddle
   inside one product.
5. **The `dim >= 8` numpy branch is a pessimization.** Its docstring claims a
   speedup; measured at dim 16 it is 31% SLOWER than the Python loop
   (0.0126s vs 0.0096s). object dtype has no BLAS.
6. **The q-Gaussian tier is dead.** k_exact defaults to k_max, so
   active_gaussian is empty (measured: 193 exact, 0 gaussian).

## The one-line fix is necessary but NOT sufficient -- TESTED

`if s['sparse']:` was applied and run. py-spy confirms it takes the COO path
(lines 1495/1500, no _matmul_dim). Deuterium STILL had not completed after
11 minutes. Complexity drops ~500x at dim 2310 but every scalar op is still a
Python-level mpmath call. Both layers must be fixed.

**Patch was reverted, not committed.** With neither version completing there is
no way to verify it preserves the number, and this is a binding-energy producer.
Landing it needs a value-equality check on a subset that completes both ways
(use k_exact to shrink the partition set; do NOT use deuterium).

## Order of work

1. Fix the guard (one line, ~500x) -- with the equality check above.
2. Export dense_dense_mul_mpfr via PyO3, route _matmul_dim + the COO
   accumulator through it (>=24x, on top of 1). This is what makes higher
   isotopes reachable.
3. Fix the precision straddle: Q and h as mpf from Q_50_DIGIT_STR; stop
   seeding accumulators with np.eye / 0.0. Correctness, independent of 1-2.
4. Delete the dim>=8 numpy branch.
5. Decide the q-Gaussian tier: real default below k_max, or delete.

## Scaling law

Partition set is FIXED (193 at k<=11, dims 1..2310; 37s just to materialise) --
it does not grow with A. Crossings grow O(A^2). Cost ~ A^2 * sum_lambda f(dim),
f = dim^3 today, dim*nnz after fix 1. Relative to deuterium: Li-7 ~5x,
O-16 ~17x, Fe-56 ~144x.


---

## CLAIMED 2026-09-05 — branch claude/rag-document-ingestion-options-orasrw

Taking the SIGN question specifically, on owner direction. The prior session
(`session_01Cb9sX3NisBDY4WN4z5wJL4`) last committed 2026-09-03; this bean is
still `todo`, so this is a claim on an unclaimed item rather than a takeover.

**Scope I am taking:** why `unified_iterative_correction` is negative. Its own
commit `815b2a46a0` says "nothing here says WHY the sign is wrong -- that is the
physics question this measurement opens and does not answer."

**Scope I am NOT taking**, so it stays available: 6Li / A>=6, which
`aaa2ef9c51` names as the discriminating measurement for the extensive term's
SHAPE. That is a different question from the sign and ~5x deuterium's cost.

**Route:** formalize-first, per AGENTS.md STRICT — locate where the sign is
DETERMINED in term 1 and ask whether it is forced, rather than scanning. The
strongest existing evidence that it is structural is this bean's own: the
accumulator is negative on BOTH matrix families (old braid-violating: -0.0319
at k=4 to -2.1955 at k=8; corrected: -0.0896 to -2.0200), so it survives a
change of the underlying representation.

**Falsifier stated in advance:** if the sign traces to a free choice — an
orientation, a w_0 convention, an ordering of the LP objective — then it is not
structural and this framing is wrong.

## Step 2 answered 2026-09-05 (qou-0wqd / PR #6708) — nothing moves; step 3 is what is left

Step 2 was "wire the correct family in, then re-run the binding numbers and
report what moved". Measured: `1e-14`, not the 71-221 % the step-2 first-half
table predicted. The correct family is now in
`hecke_core_legacy._build_ysn_matrices` (`a_rho = h/(1 - q^(-2 rho))`, braid
defect `0.7315 -> 7.5e-17`, `ysn_braid_relation_audit.py` exit 0).

Two independent reasons the accumulator could not move:

1. **The kernel bypasses the Python family entirely.**
   `_lp_kernel_steps(partition, chains)` takes the partition SHAPE, not
   `entry['ysn']`, so Rust rebuilds its own braid-satisfying family; both
   consumers early-return on it. 193 calls, 193 served.
2. **The consumers take traces, and the trace cannot see the defect.**
   `Tr(ABA) - Tr(BAB) = Tr(B) - Tr(A) = 0` from the quadratic relation alone, in
   any dimension. Established at MPFR in
   `computations/audits/ysn_trace_blindness_probe.py` (9/9): legacy MATRIX braid
   defect `0.731514`, legacy TRACE braid defect `6.68e-52`.

**Step 3 (performance / precision) is now the live item**, and it is joined by a
consumer this arc has not assessed: `q_sweep_sdp_atom` in
`sdp_cross_channel.py` imports `_build_ysn_matrices` directly and uses the
matrices, not their traces — so it is the one place where the defect could have
had a numerical consequence, and nobody has measured it.


## The `q_sweep_sdp_atom` gap is closed — it has no callers (2026-09-05)

Measured, correcting my own note above: `q_sweep_sdp_atom` is defined at
`computations/sdp_cross_channel.py:394` and **called nowhere in the repo**. A
tree-wide grep returns its own `def` plus only the three places this session
wrote *about* it (this bean, `qou-0wqd`, and the audit doc). No witness
references it.

It was named as "the one place the defect could still bite" because it is the
only importer of `_build_ysn_matrices` outside `hecke_core_legacy` and it uses
the **matrices** rather than their traces. That reasoning was right; the
premise was not — there is no caller, so no recorded number came from it, and
the fix makes it correct before anyone writes one.

This is a grep, not a run: it establishes there is no consumer, not that the
function is otherwise correct.

**So the arc's remaining item is step 3 alone** — the builder is still float64
(`math.sqrt`, `1.0` literals, no `mp.dps`), which is why the Python family
agrees with the Rust MPFR reference only to ~1e-16.


### Cross-reference for the sign claim (from `qou-0wqd` / PR #6708, 2026-09-05)

The claim section above rests its "the sign survives a change of the underlying
representation" argument on the accumulator values *"old braid-violating:
-0.0319 at k=4 to -2.1955 at k=8; corrected: -0.0896 to -2.0200"*. Those are the
2026-08-31 audit's step-2 table, which PR #6708 **retires**: its *corrected*
column is what today's `main` already produces WITH the braid-violating
matrices, and its *current* column reproduces on no tree measured there.

**The conclusion is strengthened, not weakened.** Varying only the matrix family
moves the accumulator by `1e-14`, and for a proved reason — the consumers take
traces, and `Tr(ABA) - Tr(BAB) = Tr(B) - Tr(A) = 0` follows from the quadratic
relation alone in any dimension. So the sign is invariant under that change by a
structural argument rather than by two numerical runs that happened to agree in
sign. Quote the invariance, not the table.

**And it narrows the falsifier usefully:** since the representation cannot move
the accumulator at all, the sign cannot be traced to anything in the seminormal
family — the free-choice candidates worth checking are the ones OUTSIDE it (the
LP objective's ordering, an orientation, a `w_0` convention).


## The sign IS answered — the Pass-2 gate forces it (2026-09-05, PR #6752)

The falsifier stated in advance above asked whether the sign traces to a free
choice. **It traces to the gate**, which is neither a free convention nor part
of the seminormal family — so the narrowing in the cross-reference section
above ("look OUTSIDE the family") pointed the right way.

`unified_iterative_correction` returns `B = sum over GATED lambda of
C_lambda * ( ln|Tr M_lambda(A)| - ln d_lambda )`. Three measured steps:

1. `C_lambda >= 0` everywhere — **0 of 682** negative.
2. Pass 2 keeps exactly the partitions with final trace `<= 0` (complementary
   slackness).
3. `|Tr| >= d` holds in **34.1 %** of `Tr > 0` cases and **3.4 %** of
   `Tr <= 0` cases — a 10x asymmetry, structural because `Tr(I) = +d`.

Non-negative scale times a negative log ⇒ `B < 0` forced, for any nucleus.
**Same cause explains the A-independence**: gated-set size across A = 2..6 is
`[15, 9, 9, 10, 15]` while AME spans 12.7x — the output is a property of the
gate's selection, not of the nucleus.

Probe: `computations/probes/uic_sign_forced_by_gate_probe.py` (5/5).

## The gate's justification is disproved — by a proof already in the corpus

`content/quantum-observable-universe/mass-theory/operator-selection-lp.md`
(commit `6b7d2ec4a8`) proves the operator-selection LP degenerate: `b_1 = 1`
makes the first Frobenius row equal the objective vector, so the optimum is
identically 0, `y_0* = 0` by strong duality, and the minimiser set is a
positive-dimensional face. That commit fixed the content blocks and never
touched `hecke_core_legacy.py`.

- `lp_shadow_price` sets `y_0 = 1/[k]_q!` and calls it "the dual variable of
  the normalisation constraint". Measured 0.497 (k=2) to 1.56e-4 (k=7) —
  never 0. What it actually does is zero the two extremes `(k)` and `(1^k)`.
- Substituting the **proved** `y_0* = 0` makes the sign MORE negative
  (2H -1.3657 -> -1.6092; 6Li -1.0770 -> -1.6065). So correcting the dual is
  necessary and **not sufficient** — the gate is the mechanism.

Probe: `computations/probes/uic_gate_justification_disproved_probe.py` (5/5).

## Replacement objective — written up, two falsifiers run, decision is the owner's

`docs/proposals/2026-09-05-operator-selection-objective-replacement.md`.

New measurement: **an index-set mismatch**. The primal LP is NF-basis-indexed
(`d = n! = 720` at n=6) while `prop:mass-coefficient-shadow-price` claims a
**partition's** shadow price — 11 partitions of 6, not 720. No partition-indexed
LP exists in the corpus. The natural bridge makes the object a `d_lambda x
d_lambda` matrix, not the scalar the code multiplies; and the `d_lambda = 1`
blocks, where the scalar type IS correct, are exactly the two `y_0 = 1/[k]_q!`
zeroes out. Probe: `lp_partition_index_mismatch_probe.py` (4/4).

Five options O1-O5 with cost / risk / what-each-forecloses; **which one to take
is the owner's decision**, the same one `6b7d2ec4a8` declined, one level down.

- **O3 falsifier FIRES** (`sdp_o3_falsifier_probe.py`, 6/6). The block SDP does
  exclude all six LP-optimal vertices (min eig -7.33 / -3.85) but is degenerate
  by a different route: SU(2) gives `y_(1,1,1) = 0` exactly, so a Phi on that
  block is PSD with objective 0 and nonzero net (0.02016). The ray matches the
  known q-antisymmetriser radical to **6.4e-51** — not a new object. Amended to
  **O3' — pose the SDP on `H_n(q)/radical`**.
- **O3' falsifier does NOT fire** (`sdp_o3prime_weight_positivity_probe.py`,
  5/5). n = 3..12 at the proton pin: >2-row partitions vanish exactly, every
  survivor strictly positive, `sum y_lambda f^lambda = 1` throughout; still
  positive at `k_max = 11` (9.2e-4). Cross-validated at n=3 to 14 digits
  against the weights the O3 probe solved independently.

**Do not start O3' expecting it to fix the sign.** It fixes the type error;
the feasible geometry still does not distinguish `B_3`, so selection stays open.

## Still open on this bean

- Step 3 (the float64 builder) — untouched by this session.
- 6Li / A>=6 for the extensive term's SHAPE (`qou-brng`) — a run is in flight
  but that is a different question from the sign.

## Owner ruling 2026-09-05 — O2 + O3′ chosen; O2 done, O3′ formalized

Author picked **1 and 2**: fix the documentation, and re-pose as the block SDP
on the radical quotient.

**O2 applied, six sites, no number moved.** The false claim was that
`y_0 = 1/[k]_q!` is "the dual variable of the normalisation constraint". It is
`min_λ(w_λ/d_λ)`, a weight normalisation; and the real net-constraint dual of
`prop:operator-selection-lp` is identically zero. Corrected in
`mass-coefficient-shadow-price.{md,ts}`, `knot-operator-energy.md`,
`unified-iterative-correction.lean` (docstring only), and three sites in
`hecke_core_legacy.py` — one of which additionally claimed the LP assigns
"unique invariants" to the partition basis, false twice over (NF-indexed, and a
positive-dimensional minimiser face). Content validate exit 0; `lean`-direct
exit 0. `shell-closure-stability.md` makes the same shape of claim about the
**confinement** LP and was left alone: different program, and settling it is a
measurement rather than a doc fix.

**O3′ begun formalize-first** — `QOU/MassTheory/BlockSDPNondegeneracy.lean`,
5 declarations, `lean`-direct exit 0, `#print axioms` clean on all five (no
`sorryAx`). `obj_pos_of_pos_weights`: on the quotient every feasible point has
strictly positive objective, so no degenerate ray.
`exists_zero_obj_of_zero_weight`: one vanishing weight restores the degeneracy
at any target — the falsifier as a theorem. `feasible_smul`: the value is
homogeneous of degree one in `n_target`, the property the LP lacks. **Not
proved: that O3′ selects.** The compute half of O3′ is not started.

## 🛑 My A-independence claim is UNVERIFIED, and ⁶Li is anti-correlated

`binding_energy(3,3)` with `_HAS_LP_KERNEL` asserted, 4039.8 s:
**B_pred = −3.065019520558719** against AME **+31.994**.

Against the only other production figure I measured myself (²H, kernel live,
−7.271102124876717): predicted `|B|` **falls ×0.42** while AME binding **rises
×14.4**. Per nucleon, predicted `|B|/A` falls ×7.1 against AME's ×4.8 rise. The
prediction is **anti-correlated** with its target, not merely sign-flipped. The
sign is negative at A = 6 too, consistent with the gate.

**The four-point plateau I quoted in PR #6752 (−7.271 / −7.742 / −7.456 /
−6.829) has provenance for ONE of its four figures.** A fixed-string grep for
the other three across `*.md`, `*.json`, `*.py` returns nothing anywhere in the
tree; they came from conversation context. Kernel-vs-fallback differ by 17.29 %
on the same atom, so an unverified figure could be either. Marked unverified,
not retracted. If the plateau is real, ⁶Li breaks it (2.4× smaller than the
smallest of the four) — deciding that needs A = 3,4,5 re-measured kernel-live,
~2 h, claimed separately.

Second tension, open: the k_max = 6 reconstruction does **not** show the A = 6
drop (⁶Li is second *largest* there at −1.0770), and the gated-set size at
A = 6 is **15**, the largest in the series. Production magnitude falls where the
gate admits the most partitions. The truncation argument covers absolute scale,
not a reversed trend.

Audit: `docs/audits/2026-09-05-li6-production-binding-anticorrelates.md`.
## Step 3 done — and the builder was float64 in three places, not one (2026-09-05, PR #6794)

I had recorded the remaining defect as "the builder is still float64
(`math.sqrt`, `1.0` literals, no `mp.dps`)" and framed leaving it as a
deliberate ordering choice. Both were wrong: NO-FLOAT64 makes it a defect, not
a deferred nicety, and the description named only the smallest of three.

| defect | evidence |
|---|---|
| `Q`/`Q_INV`/`HA` from `q_parameter` are Python **floats** — float64 from the INPUTS | `type(qp.Q).__name__ == 'float'` |
| `mp.dps` is **15** on a bare import — float64's significand, so mpf without raising it buys nothing | `mp.dps == 15` after import |
| **124 of 193** ysn entries (64 %, max dim 2310) were `scipy` `csr_matrix` — float64 by construction, kernels reject `dtype=object` | measured over `_PARTITION_TABLE` |

Fixed: exact twins `Q_MP`/`Q_INV_MP`/`HA_MP`, `mp.sqrt`, and
`mp.workdps(_precision.COMPUTE_DPS)` (70, read not hardcoded, restores the
caller's dps on exit). `_ExactCOO` replaces `csr_matrix` — deliberately not a
scipy type so `issparse` is False for it and no consumer can route it into
float64 BLAS.

The consumer dispatch moved with it: all three accumulators keyed on the
RUNNING matrix's dtype, which starts as `np.eye` (float64), so an exact sigma
would have sent the first crossing into a scipy call that raises. They key on
sigma now, and the COO accumulator is `dtype=object` rather than
`zeros_like(M_run)`.

**Verified.** Against the closed form derived in `qou-4m9u`
(`-1/(q(q^2+1))` at rho = -2): **9.5e-52**, was ~1e-16. Braid audit exit 0
with the Python rows at `4.0e-50 / 3.2e-50` against Rust's `1.2e-50 / 2.0e-50`
— previously `1.49e-16 / 1.52e-16`.

**A hypothesis of mine, REFUTED.** I proposed that main's "17.3 % off at
deuterium" banner was the sparse path, since the 1e-14 merged in #6708 came
from k = 4,5,6 which carry zero sparse partitions. Measured at k = 7 (2 sparse)
and k = 8 (12 sparse): rel **1.7e-14** and **8.9e-15** — same order. The
float64 defect does NOT account for 17.3 %.

**Still open, and not mine to close without measuring:** that banner's *braid*
claim is stale (#6708 fixed it; the audit exits 0), so it tells a user their
numbers are invalid when they are not. The 17.3 % half compares fallback
against kernel — a different comparison from the one above, unrun here.

## A-series COMPLETE (2026-09-05) — the plateau does not exist, and that was my claim

Owner asked for A = 3,4,5 kernel-live. Probe
`computations/probes/uic_binding_a_series_kernel_live_probe.py`, 5/5, 11350 s.

**All three unverified figures reproduce exactly** — ³H `−7.742121347136118`
(vs −7.742), ³He `−7.45619950551758` (vs −7.456), ⁴He `−6.828594293148849`
(vs −6.829). The series was kernel-live; my caution was procedurally right and
the substance was sound.

**And it identifies the set:** ²H, ³H, ³He, ⁴He — **A = 2, 3, 3, 4**, the same
five atoms as `[15, 9, 9, 10, 15]` minus ⁶Li. I labelled both "A = 2..5" and
both were wrong identically, because they are one set. **No A = 5 point had
ever been computed.**

| atom | A | Z | N | B_pred | AME |
|---|---|---|---|---|---|
| ²H | 2 | 1 | 1 | −7.2711 | 2.2246 |
| ³H | 3 | 1 | 2 | −7.7421 | 8.4818 |
| ³He | 3 | 2 | 1 | −7.4562 | 7.7180 |
| ⁴He | 4 | 2 | 2 | −6.8286 | 28.2957 |
| ⁵He | 5 | 2 | 3 | −6.7896 | 27.5607 |
| ⁵Li | 5 | 3 | 2 | **−8.1363** | 26.3307 |
| ⁶Li | 6 | 3 | 3 | −3.0650 | 31.9940 |

**I committed a two-branch prediction before ⁵Li landed and BOTH failed.**
⁵He and ⁵Li share A = 5 and differ only in Z, so: ⁵Li ≈ −6.8 ⇒ break at A = 6;
⁵Li ≈ −3 ⇒ break at Z = 3. It is **−8.136**, below the whole plateau.

**So the "A = 2..5 plateau with a cliff at A = 6" does not exist** — an artefact
of a sample holding one atom per mass number above A = 3. What survives:

- the **same-A mirror split grows ~5×** (³H/³He 3.835 %, ⁵He/⁵Li 19.84 %) — same
  A, differing only in Z, and the gate account predicts nothing about it;
- the **largest single jump is same-Z, adjacent-A**: ⁵Li → ⁶Li = 2.655×;
- predicted spread 2.655× against AME's 14.4×, every point the wrong sign.

**Scoped:** the probe's anti-correlation assertion compares only the extreme A
points and the series is not monotone (⁵Li sits below ²H) — true of two
endpoints, weaker than its passing suggests.

**Post-merge check:** ²H re-run after the sibling's #6794 exact-`mpf` fix is
**bit-identical** (`−7.271102124876717`, MOVED: False), so the series stands.
Mechanism: with the kernel live the Python sigma family is never consumed.

**Still open:** ⁶Li is the most extreme point and the one row not measured by
this probe (carried from a standalone run). It wants an independent re-run
before anything is built on it.

## ⁶Li independently confirmed; O3′ appears to SELECT (2026-09-05, later)

**⁶Li re-run is bit-identical** — `−3.065019520558719`, MOVED: False, 4024.9 s
against the recorded 4039.8 s run. The extreme outlier is real, and every row of
the A-series is now measured or independently confirmed. It doubles as a much
harder post-merge check than ²H (A = 6 exercises far more of the partition
table), so **#6794 does not move `binding_energy` on the kernel path**,
confirmed at both ends of the mass range.

**🛑 O3′ appears to SELECT — correcting my own §8 recommendation.** I told the
owner O3′ would fix the type error and leave selection open. Under the natural
lift `T_λ = t_λ·I`, the block SDP reduces to a scalar LP in the traces whose
optimum sits on `argmin_λ t_λ`. Measured over all six rows of
`a-K-via-lp-dual-full.witness.json`, survivors only: the argmin is **unique in
every row**, smallest gap 19.9 %, largest 110.8 %. Selected blocks (2,1), (2,1),
(3,3), (5,4), (5,4), (6,6) — the near-square two-row partition each time.

Precisely: the **block** is selected, the **operator** is not (any PSD `Φ_λ`
with the right trace is optimal). That is exactly the content the corpus's
physical reading wants — "which Wedderburn blocks the bound state saturates" —
and it does **not** contradict S4, which excludes selecting the *operator* `𝓑₃`
on the NF-indexed polyhedron.

Caveats kept explicit: the **reduction** was measured, not a solver run; the
lift `T = t·I` is an assumption; and `t_λ > 0` on survivors is measured over six
rows, not derived (recorded in `BlockSDPNondegeneracy.lean`'s docstring, since
that is the theorem's hypothesis and characters can in principle go negative).

**This raises the value of the O3′ compute**: authorised as a type fix, it may
also be a selection principle.

## 🛑 CORRECTION to the O3′ selection claim — it is ATOM-INDEPENDENT (PR #6841)

#6752 merged reading O3′'s selection as *"which Wedderburn blocks the bound
state actually saturates"*. **Wrong.**

`t_λ = w_λ · χ^λ(W_atom)`: `w_λ` depends only on the partition and `q`, and is
identical for every atom at a given `n`; `χ^λ` carries all atom-dependence.
**argmin(`t`) = argmin(`w`) in 6 of 6 rows** — the character never moves the
selection. Two atoms at `n = 3` and two at `n = 9` give the **same block** with
**different prices** (0.4470/0.4206; 0.01655/0.02879).

- **Pricing STANDS**: `y_0*` nonzero and atom-dependent, where the full LP has
  `y_0* = 0` identically. That is the defect O3′ was chosen to repair.
- **Selection is a function of `n` alone** — same block for proton, neutron and
  every other atom at that `n`.

**My explanation was refuted by the same probe.** Spread dominance (`w` varies
more than `χ`) holds at `n = 6` and **fails at `n = 9`** — χ-spread 6.448×/6.712×
against w-spread 5.915× — and the argmin is unmoved anyway. The probe now
asserts the *refutation*; the mechanism is **open**, and no replacement guess is
offered for six rows.

Probe `o3prime_selection_is_atom_independent` 4/4.


## RE-MEASURED 2026-09-07 against `main` (PR #7073) — 4 of 6 are gone, and re-measuring found a NEW one

Do not act on the six findings above without re-checking them; most have moved.

| # | claim above | status on `main` today |
|---|---|---|
| 1 | O(dim·nnz) sparse path unreachable (`if s['sparse'] and not exact_chain`) | **FIXED** — the guard is now `elif s['sparse']:`, and the in-code note records value-equality against the pre-fix result at `k_exact` 4–8 |
| 2 | zero Rust in the hot file | **FIXED** — 7 references, including a live `pyhecke_native.lp_accumulator_step_traces_mpfr` kernel that computes a partition's whole trajectory |
| 3 | `dense_dense_mul_mpfr` exists and is not exported | **still literally true, but SUPERSEDED** — it is still not a `#[pyfunction]`; a whole-trajectory kernel was exported instead, so a matmul export is moot for this path |
| 4 | half the matmuls are float64; the inter-nucleon `-h` straddle | **STILL LIVE → fixed in #7073** (below) |
| 5 | the `dim >= 8` numpy branch is a pessimization | **NOT re-measured** — `_matmul_dim` still branches at `dim >= 8` (line ~1310) |
| 6 | the q-Gaussian tier is dead (`k_exact` defaults to `k_max`) | **NOT re-measured** — the default is still `k_exact=K_PARTITION_MAX` |

**The headline is superseded.** "Cannot scale / deuterium ~40 days" was measured before the kernel landed. `qou-i7ju` records deuterium at **942 s** with the kernel live, against 22607 s on the fallback — and the fallback is 17.3 % off, because it uses braid-relation-violating matrices.

### Finding 4, localized and fixed

Six lines: the inter-nucleon crossings in `_step_chain_22` and `_step_chain_generic` used Python floats (`1.0`, `0.0`, `-h`, `_pn_d(h)`) while the intra-nucleon tables `_PROTON_G1` / `_NEUTRON_G1` carried exact `mpf`. Coefficient dtype histogram over every (nucleon, prev_types, n_gens) combination, n=480:

    before  ('int','int') 220  ('int','mpf') 220  ('float','float') 40
    after   ('int','int') 230  ('int','mpf') 250  ('float','float')  0

### NEW: the exact coefficients were truncated BELOW float64 entering Rust

`_lp_kernel_steps` serialized coefficients with a bare `str()`. `str(mpf)` renders at the AMBIENT `mp.dps`, which is **15** in a bare import of this module. So the exact 50-dps coefficients crossed at 14–15 significant digits — less than float64 — while the docstring one line above said "nothing narrows to f64". Measured by spying on the live call:

    mp.dps at the call : 15      prec requested : 50      q50 digits : 50
    d='-0.209060298795639'   (15 sig digits)
    exact -0.2090602987956393154308462131296749438598

**It is not cosmetic, and one truncation order does not tell you that.** Three-way run, each arm in its own process — A pre-fix, B boundary fix only, C both:

                  A                     B                     C
    k_exact=4   -0.08955968305895065  -0.08955968305895065  -0.08955968305895068
    k_exact=5   -0.7335499391634722   -0.7335499391634975   -0.7335499391634976

                A->B (boundary)   B->C (coefficients)
    k_exact=4        0                 3.35e-16
    k_exact=5      3.45e-14            1.36e-16

The boundary truncation is worth **3.45e-14 relative at k_exact=5** — ~150x the float64 floor and above the 1 ppQ L1 target — and **zero at k_exact=4**. It grows with the partition set. I first reported it as cosmetic on the k=4 arm alone; that was wrong and is corrected in the second commit of #7073.

### Also corrected: a stale convention claim in the `_pn_d` import note

It read "`-h/2` is `strict_averaged`" as though that were R3's outcome. R3 made `bring_color_weighted` canonical; `strict_averaged` is the colour-blind one the next sentence warns about. Live `PN_CONVENTION` is `bring_color_weighted`, and they are 6.9e-4 apart at this q0 (`-0.10445824776972631` vs `-0.10453014939781966`) — 12 orders above the 1 ppQ target. Do not "simplify" `_pn_d(h)` to `-h/2`.

### What stays open (why this bean is NOT completed)

- Findings **5** and **6** are unmeasured.
- The real ceiling on this producer is **downstream of everything above**: `unified_iterative_correction` narrows to float64 inside its own accumulation loop (`math.log(abs(tr_run))` returns a Python float whatever it is handed) and returns a Python `float`. Documented in-file, tracked separately, untouched by #7073.


## Findings 5 and 6 now measured too (2026-09-07, same PR) — the table above is complete

**Finding 6 CONFIRMED.** `k_exact` defaults to `k_max`, both `K_PARTITION_MAX = 11`, so the window `k_exact < k <= k_max` is empty and `active_gaussian` is `[]`:

    defaults (k_exact = k_max = 11)   0 partitions
    k_exact=4                       169 partitions
    k_exact=5                       164 partitions
    k_exact=6                       155 partitions

Every default run is fully exact and pays for it, and `_q_gaussian_character_approx` is dead code on that path. Not a defect — exact-everywhere is the right default for a producer — but it means the tier is **untested by any default run**, so a green default run says nothing about whether the approximation works. Noted at the `k_exact` docstring.

**Finding 5 does NOT reproduce — scope-limited negative.** The finding recorded the `dim >= 8` numpy branch as 31 % SLOWER than the Python loop at dim 16 (0.0126 s vs 0.0096 s) and called the threshold a pessimization. Re-measured against the ACTUAL `_matmul_dim` branches (not a reimplementation), best-of-7, mpf entries, python 3.11.15 / numpy 2.4.6 / mpmath 1.4.1:

    dim=8   numpy  1.10 ms   loop  1.34 ms   0.82x
    dim=12  numpy  3.89 ms   loop  4.37 ms   0.89x
    dim=16  numpy  9.50 ms   loop 10.65 ms   0.89x
    dim=24  numpy 32.54 ms   loop 34.96 ms   0.93x

numpy is faster at every dim, by 7-18 %. **This is scope-(a), not (b):** the claim does not reproduce in this container at these library versions, which is not the same as its having been wrong when taken. The arm that moved is numpy's (12.6 -> 9.5 ms at dim 16) while the loop arm is nearly unchanged (9.6 -> 10.65 ms), so a numpy version difference is the leading candidate — and it was **not** isolated, because this container has one numpy. Do not treat either figure as settled; re-measure.

Two things worth carrying forward regardless of which figure holds. The docstring's "significant speedup" was wrong in *both* measurements — 7-18 % here, negative there, never significant. And object dtype has no BLAS, so numpy on this path is an elementwise Python loop with less interpreter overhead, not a kernel; nobody should expect a large factor from it either way. Both recorded at the docstring.

My first pass at F5 reimplemented the loop branch with an `int` accumulator where `_matmul_dim` seeds with `0.0`; the numbers above are from the faithful version. The reimplementation gave 0.90-0.98x, so the conclusion did not turn on it, but a benchmark of a reimplementation is not a benchmark of the code.


## The last row — the accumulator's float64 log — measured (PR #7082), plus a finding that outranks it

### The narrowing is real and now fixed

`unified_iterative_correction` fed every running trace through `math.log`, which returns a Python `float` whatever it is handed, so an `mpf` trace from the Rust MPFR kernel lost every digit past the 16th. `_exact_log` replaces the three sites (`L0`, the `m_max` rescale, `log|tr_run|`) at `_EXACT_COEFF_DPS`. Engaged, checked not assumed: a spy records 30 calls per A=2 run, inputs `{int, mpf}`, outputs all `mpf`.

### What it moves — and where my own framing was wrong TWICE

Each arm in its own process; `float64` reproduces pre-fix behaviour exactly by rebinding `_exact_log` to `math.log`, so both arms come from one tree.

| A | k_exact | float64 | exact | delta |
|---|---|---|---|---|
| 2 | 4 | -0.08955968305895068 | -0.08955968305895068 | 0 |
| 2 | 5 | -0.7335499391634976 | -0.7335499391634976 | 0 |
| 3 | 4 | -0.10235605915957281 | -0.10235605915957281 | 0 |
| 3 | 5 | -0.3507860783973744 | -0.3507860783973744 | 0 |
| 4 | 4 | -0.08058674847769143 | -0.0805867484776914**1** | 2 ULP, 2.5e-16 |

**First wrong framing.** The commit message said the narrowing "compounds over the trajectory rather than rounding once". It does not. Per partition, with `scale` written once at init (1773) and read only at 1929, the loop is `raw_delta = scale*(log_cur - log_prev); cumul_partition += raw_delta; log_prev = log_cur` — it **telescopes** to `scale*(log_last - L0)`, so every intermediate log cancels algebraically and the error cannot grow like N independent truncations.

**Second wrong framing.** I then wrote that the telescoping made the null a *prediction*. Too strong: A=4 moves by 2 ULP. Telescoping BOUNDS the error near the float64 floor; it does not zero it, because `gated_total` still sums hundreds of per-partition endpoints. The correct statement is: the effect is O(float64 floor) and does not grow with trajectory length — which is why A<=3 shows nothing and A=4 shows 2 ULP.

### The finding that outranks it: the q-Gaussian tier is computed and DISCARDED

Chasing a suspected confound (at k_exact=4 the default k_max=11 leaves 169 Gaussian partitions active, and `_q_gaussian_character_approx` is float64 in both arms) I re-ran with `k_max = k_exact`, emptying the tier. Byte-identical results:

    A=2 k=4   gauss=169 -> -0.08955968305895068   gauss=0 -> same
    A=2 k=5   gauss=164 -> -0.7335499391634976    gauss=0 -> same
    A=4 k=4   gauss=169 -> -0.08058674847769143   gauss=0 -> same  (and the 2-ULP move survives)

Measured first, then explained by the code. `active = active_exact` (line 1721), so `state` never holds a Gaussian partition. Its contribution lands only in `cumul_total` — and Pass 2 does not use `cumul_total`, it rebuilds the answer as `gated_total = sum over state of cumul_partition`. **Computed, then discarded.**

Two consequences:

- **`k_max` does not affect the return value at all.** Raising it costs compute and changes nothing.
- **The per-step witness rows disagree with the return value.** `cumulative_MeV` and `raw_total_MeV` carry `cumul_total`, which INCLUDES the Gaussian contribution; the function returns `gated_total`, which excludes it. A witness reader and a caller get different numbers from the same run.

This is stronger than finding 6, which said the tier is unreachable at the defaults. It is also **inert when reachable**, and now has a mechanism rather than just a count.

**Not fixed, deliberately, and this is a decision for the author, not a typo.** Pass 2 gates on `final_tr_sign`, which a Gaussian partition has no matrix to supply, so making the tier contribute requires deciding what its gate should be. Recorded at the code site; behaviour unchanged.


## RETRACTION + resolution of the witness/return disagreement (2026-09-07, same PR #7082)

### 🛑 RETRACTED: "the q-Gaussian tier is computed and DISCARDED"

The entry above says the tier's contribution is computed in Pass 1, accumulated into `cumul_total`, and then dropped because Pass 2 rebuilds the answer from `state` (exact partitions only). **The mechanism is wrong. There is no contribution to drop.**

`delta_g` in the Gaussian loop is a **hardcoded `0.0`**, deliberately, and the comment immediately above it says so: *"Extension to higher k via this approximation does NOT generate non-zero corrections — it correctly predicts that typical high-k partitions are SLACK and contribute nothing in the LP-dual framework."*

The byte-identical `gauss=169` vs `gauss=0` measurements are **not retracted** — they are correct, and `k_max` genuinely does not affect the return value. What was wrong is the story about WHY. I inferred it from the two totals' definitions without reading the twenty lines that set `delta_g`, and the measurement is equally consistent with either story. **A measurement that matches your hypothesis is not evidence for its mechanism.**

Consequence: there is no design decision here for the author after all. The tier contributing zero is intended, documented in place, and correct under complementary slackness.

### The disagreement is REAL, and it is raw-vs-gated

Measured at `k_exact=4`:

| A | per-step running total | function returns | tight / exact |
|---|---|---|---|
| 2 | -0.4122121922450237 | -0.08955968305895068 | 4 / 10 |
| 4 | -0.2742397716173970 | -0.08058674847769141 | 2 / 10 |

**A factor of 3.4-4.6, not a rounding difference.** The per-step total is UNGATED; the return is GATED (Pass 2 keeps a partition only when `final_tr_sign <= 0`). Under the old field name `cumulative_MeV`, a reader taking the last row as "the answer so far" was several times off with nothing in the name to say so — `gated_total_MeV` exists but only on the LAST row.

### Resolved by rename, and it has to be a rename

`cumulative_MeV` -> **`cumulative_ungated_MeV`** in the per-step rows.

**The gate cannot be applied per step**, which is why this is a rename and not a fix: `final_tr_sign` is a property of the atom's FINAL state, so at step k there is no fact of the matter about which partitions survive. An honest per-step running total is *necessarily* ungated; the defect was the name, not the number.

**Safe: ZERO consumers.** Measured over the whole tree, tracked and untracked. `probe_9b_manybody_expansion.py` writes a `cumulative_MeV` of its own into its own witness and never reads this one. `where_the_a_dependence_is_lost_probe.py` reads `raw_total_MeV` / `gated_total_MeV` — untouched, and it already distinguishes the two correctly.

Verified after the rename: old key absent; `cumulative_ungated_MeV == raw_total_MeV`; and `float(gated_total_MeV) == ` the returned value **exactly**.
