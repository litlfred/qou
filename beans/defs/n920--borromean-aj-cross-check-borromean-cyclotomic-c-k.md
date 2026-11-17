---
# n920
title: 'Borromean AJ: cross-check Borromean cyclotomic c_k against Habiro [H1] (simple links, RIMS Kokyuroku 1172) — NOT Masbaum math/0306345 (twist knots only); ref unavailable, DEFERRED'
status: in-progress
pr: 8250
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-04T10:42:30Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---

UNBLOCKED 2026-07-06: owner uploaded library/arxiv-math-0508100v6/0508100v6.pdf (GL2011).
Habiro's Borromean formula transcribed + verified in
computations/habiro_borromean_colored_jones.py (4/4 anchors: n=1
exactness, bar-symmetry n<=6, Laurent polynomiality, independent TL_3
Kauffman-bracket cross-check at n=2). Remaining for this bean: the
actual c_k cross-check against the corpus's Borromean cyclotomic
values, + the (novel) recurrence hunt on the diagonal tower.
EXISTENCE CERTIFICATE 2026-07-06 (borromean_diagonal_recurrence_hunt.py):
a q-difference operator annihilating the diagonal tower J_{B,n} EXISTS
at order r=5, m-window W=13 (nullity 2; 9/9 (p,s) mod-p samples, each
surviving 30 beyond-fit-range check rows; orders <=4 excluded for
W<=14). Phase 2 = symbolic reconstruction over Z[q^{±1}] + exact
symbolic annihilation + q->1 specialization (candidate Borromean
A-ideal generator, diagonal restriction).
PHASE-2 SCOPING RESULT 2026-07-07: the (6,11) canonical coefficient
entries are rational functions of q-degree ~218 (measured by bisected
modular fit on 1260 samples, column 6; degrees <=150 excluded, fits at
219+/-6). Full symbolic reconstruction is therefore a compute project:
~460+ samples x 184 columns of deg-470 eliminations + multi-prime CRT
(single 61-bit Wang lift insufficient for deg-218 integer coefficients).
Options: (a) Python+multiprocessing overnight run, (b) Rust-side
(hecke-engine) modular interpolation tranche, (c) proper qZeilberger.
Existence certificate (r<=4 excluded, three verified windows) stands.
PHASE-2 CONDITIONING DIAGNOSIS 2026-07-07 (PR #3450, audit
docs/audits/2026-07-07-borromean-recurrence-reconstruction-conditioning.md):
the RREF-nullspace-per-sample interpolation produces RATIO entries of
q-degree up to 252 (median 208) — coeff_c/coeff_free — and one genuinely
low-degree column (181) destabilized the multi-prime CRT consensus. Fix
committed: --degrees as bisection hints + per-column modal-degree CRT
consensus + lifted-operator checkpoint + atomic p0 regen. Validation
gated on an uninterrupted ~35min run (container reclaim killed 3 runs).
Two clean routes forward: (1) finish the fixed CRT pipeline; (2) qZeilberger
(proof-grade, mirrors aj_figure_eight_certificate.py, Lean-formalizable).
Existence certificate stands regardless.
QZEILBERGER ROUTE 2026-07-07 (PR #3450): shift-ratios verified exact +
q-proper-hypergeometric (borromean_qzeil_ratios.py, 6/6) — the well-posed-
ness precondition, DELIVERED. Operator+cert solve: symbolic sp.solve too
slow for the cube summand; fixed-q mod-p solve is fast but the naive
(operator + poly-cert, free x-window) ansatz admits a LARGE telescoping
family (nullity 41-311) because the nested R_i=prod r1(q^t x,y) share
factors. PRECISE NEXT STEP: implement Gosper certificate-denominator
normalization (pins the minimal telescoper → nullity 1), or restrict to
polynomial a_i + Gosper-DEN cert. Not closed tonight (compute env: 5+
container restarts destroyed runs). Foundation + existence certificate +
Habiro transcription all stand.
ROUTE-2 CAPSTONE 2026-07-07 (docs/audits/2026-07-07-borromean-qzeilberger-
route-diagnosis.md): all 3 telescoping shortcuts diagnosed — symbolic
sp.solve too slow (cube); fixed-q nullspace swamped by a=0 cert-homogeneous
solutions; op-projection gives a SPURIOUS r*=2 (tower-verify False,
contradicts existence cert) because the free rich certificate Gosper-sums
anything. PINNED REQUIREMENT: exact q-Gosper certificate-denominator
normalization (Gosper-Petkovsek greatest-factorial factorization of s) —
a standalone ~200-400 line q-Gosper impl, fast (no long compute window),
the well-scoped next step. Foundation + existence cert stand.
DEGREE TERMINUS 2026-07-07 (docs/audits/2026-07-07-borromean-explicit-
operator-degree-terminus.md): multi-q DQ-scan is decisive — operator-part
of the telescoping nullspace grows LINEARLY with ansatz q-degree
(72→145→294→494→772), never saturating, so NO low-degree telescoper
exists. The minimal recurrence is intrinsically ~deg-126 in q (unique,
route-independent). CORRECTION: qZeilberger does NOT reduce operator
degree — q-Gosper is strictly harder, not the clean next step. The right
route is the committed Rust CRT pipeline (PR #3450) in a PERSISTENT
compute environment (only blocker was 5 container restarts). Existence
certificate (evidence-grade) stands.

CYCLOTOMIC COEFFICIENTS DELIVERED 2026-07-07 (PR #3470,
docs/audits/2026-07-07-borromean-habiro-cyclotomic-coefficients.md):
the headline input — Habiro cyclotomic coefficients C_l(q) of the
diagonal Borromean rings — extracted C_0..C_6 exactly and verified
OVER-DETERMINED (same C_l rebuild J_{B,n} for n=1..7; non-circular
n-independence). Basis {n+j}{n-j}=(q^n+q^-n)-(q^j+q^-j) IS Habiro's
standard cyclotomic basis, so these are THE coefficients. Poles at
roots of unity (Habiro-ring structure, expected for a link);
palindromic numerators (amphichirality). NO c_k identification
asserted (corpus c_k = Q_beta/meson/m_p truncation coeffs, distinct
object) — supplied as clean input, no forced coincidence.
Also this branch: laptop-runnable explicit-operator reconstruction
script (borromean_operator_reconstruct_laptop.py) delivered for the
degree-terminus-blocked multi-hour CRT run.

CORPUS NOTE 2026-08-21 (bean qou-kqbk): the primary source this bean's TITLE calls unavailable — Habiro [H1], RIMS Kokyuroku 1172 — IS in the library and is now greppable: library/1172-3/ ('ON THE COLORED JONES POLYNOMIALS OF SOME SIMPLE LINKS', Kazuo Habiro), whose own opening names 'the trefoil and the figure eight knots, the Whitehead and the Borromean links'. The 2026-07-06 unblock came via a different document (arxiv-math-0508100v6, GL2011), so the transcription stands; this is a second, independent copy of the formula's original statement available for cross-check. Its extracted title was over-welded ('THECOLOREDJONESPOLYNOMIALSOF') which is why a title-grep missed it.

REVIVAL 2026-08-29 (branch claude/borromean-a-polynomial-2026-08-29, PR
#6064). Arc reassessed after a ~7-week gap. CLOSEOUT of the physics
hope: the reason colored-Jones q-holonomy mattered to QOU was the hope
it would deliver the Q_beta c_k truncation constants; main's c3-wall
capstone PROVED the odd D-ladder non-holonomic (KC22) and WITHDREW the
resurgent/Ecalle inference (kappa=0, 2026-08-09), so any c_k closure
lies OUTSIDE every holonomic class — the AJ->c_k bridge is dead
(scope-limited negative backed by a proved invariant; c_k closure by
non-holonomic means is not excluded). SURVIVING PIECE (pursued for its
own sake, physics-decoupled): the explicit Phase-2 reconstruction. The
reconstruction is now UNBLOCKED environmentally — the sampler is
per-prime resumable (DEG_CAP=320), resuming from main's committed
prime-0 checkpoint (184 cols, max deg 252) with a reclaim-safe
per-prime checkpoint commit, so container reclaim resumes instead of
restarting. Deliverable: explicit operator + q->1 Borromean
A-polynomial, or an honest primes_used ceiling. See
docs/audits/2026-08-29-borromean-a-polynomial-revival.md.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-21 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** The explicit order-6 Borromean operator and a classical A-polynomial candidate exist. Exact annihilation is checked only for n ≤ 9, and the gap with the r = 5 existence certificate is unexplained. The claim that the AJ→c_k bridge is dead cites KC22, which is a finite-window exclusion on convention-C ladder data, not a proved non-holonomicity, so do not cite it as scope-(b).

Evidence: The bean's last stated deliverable (explicit operator) has partly landed. `computations/borromean-operator-explicit.json`: `order: 6`, `primes_used: 6`, `verified_exact: False` (annihilation re-checked only for n ≤ 9). `borromean-a-polynomial-classical.json`: candidate, `degenerate: False`, "NOT independently checked". The bean records neither. The order-6 result is not reconciled with the r = 5 existence certificate (`borromean-diagonal-recurrence-hunt.witness.json`). The "PROVED non-holonomic (KC22)" closeout of the physics hope is overstated: registry KC22 (`docs/coordination/ck-dk-canonical-registry.md` row KC22) excludes only low-order windows (r≤3, E≤3 etc.) on convention-C d_k Taylor data. That is not a proof of non-holonomicity.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## Round 54 Implementation Progress (PR #8250)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8250 (head `6ee51e358507527bd6866f4cac2f3d6f10b8818b`, Commit 1 `ee378949fa465d0b0bd6d825c653bded4b4ca1c9`)
- **Lean 4 Module & Theorems:** `QOU/AlphaEM/TauFunctorMarkovHodgeAndBorromeanCyclotomic.lean` (`borromean_habiro_n1_exact_normalization`, `borromean_order_five_recurrence_certificate`)
- **80-dps Witness:** `computations/probes/round54-tau-functor-borromean-monotone-gs-pipeline.witness.json` (`scriptHash: de41a1d3c1e1`, `allPassed: true`, `0` raw `float64`)
