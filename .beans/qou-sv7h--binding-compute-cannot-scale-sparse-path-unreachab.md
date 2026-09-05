---
# qou-sv7h
title: 'Binding compute cannot scale: sparse path unreachable, zero Rust, float64 straddle'
status: in-progress
type: task
priority: high
created_at: 2026-08-30T15:41:58Z
updated_at: 2026-09-05T12:00:00Z
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
