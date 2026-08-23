---
# n920
title: 'Borromean AJ: cross-check Borromean cyclotomic c_k against Habiro [H1] (simple links, RIMS Kokyuroku 1172) — NOT Masbaum math/0306345 (twist knots only); ref unavailable, DEFERRED'
status: in-progress
type: task
priority: normal
created_at: 2026-07-04T10:42:30Z
updated_at: 2026-08-21T15:00:58Z
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
