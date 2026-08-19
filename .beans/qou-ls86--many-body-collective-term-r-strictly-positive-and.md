---
# qou-ls86
title: 'Many-body collective term R: strictly positive and bounded on the well-bound regime'
status: in-progress
type: task
priority: normal
created_at: 2026-08-17T00:44:48Z
updated_at: 2026-08-18T16:09:37Z
---

Opened working the many-body R term at owner direction ('go on many body').
First action was formalize-first: check what the existing screens rest on before
searching for a candidate. One of the three screens does not survive the check —
and it is one I wrote.

## The sign screen is REGIME-CONFINED, and was over-stated

collective_term_budget_probe (PR #4973) measured on a **14-isotope convenience
sample** and concluded R is 'MIXED-SIGN in A', which 'kills anything manifestly
non-negative by construction — an entropy, a KL divergence, a dimension count, a
sum of squares, a positive Plancherel weight'.

Over the **full AME2020 table** (3554 nuclides, Z>=1, N>=1, B>0):

* **7 rows have R < 0. Every one has B_AME/A < 1.73 MeV/nucleon.**
  5Be 0.0180 | 7H 0.9400 | 6H 0.9616 | 2H 1.1123 | 4Li 1.1538 | 5H 1.3364 |
  4H 1.7204. **Six of seven are particle-UNBOUND** drip-line exotics; the
  seventh is the deuteron, the weakest-bound stable nucleus.
* **Among the 3519 nuclides with B_AME/A > 5 (99.0% of the chart): ZERO
  negatives.** R in [+2.1009, +5.8926] — strictly positive, one-signed, bounded
  within a factor of 2.8.

**The negatives measure a different, already-proved defect.** B_sym with every
L > 0 is positive for every (Z,N), so the framework cannot produce an unbound
nucleus at all (single_crossing_binds; the two-nucleon floor). Exactly where
nature has ~zero binding the chain must over-bind and R < 0. Those rows re-measure
the KNOWN interface defect, not the collective term's sign structure.

**Withdrawn as stated:** 'mixed-sign in A, so non-negative candidates are
excluded.' **Replacement (scope-(a)):** on the well-bound regime R is strictly
positive and bounded in [2.10, 5.89] MeV/nucleon; an entropy / KL divergence /
dimension count / positive Plancherel weight is NOT excluded there. Do not cite
the old screen against them.

## A hypothesis of mine the measurement killed

I expected the negatives to be **2H alone** — R(2H) is by construction the
deuteron's single-bond error, hence contaminated. Wrong: seven rows, six not the
deuteron. The right claim is about the binding REGIME, not one contaminated
point. Recorded because the wrong version was the tidier story and I nearly
wrote it up.

## Where this leaves the search

A strictly-positive bounded target is far better conditioned than a mixed-sign
one. Surviving screens, unaffected:
* magnitude — plateau R/alpha = 1.3240 per nucleon, 1.90x the chain's asymptote;
* scaling — per (A-1) 19.4% spread on A>=24 vs per C(A,2) 184.6% falling
  monotonically, so an unsuppressed all-pairs term stays excluded.

Next honest step is NOT an ansatz: it is to decide whether R should be fitted at
all, or whether the well-bound regime's boundedness is itself derivable from the
step-7 functional (R must be a sum of log-suppressions over some additional
structure, since S = -sum log mu is the confirmed functional — so R's positivity
on the well-bound set says those extra factors are all < 1 there).

Probe: computations/probes/collective_term_sign_screen_regime_confined_probe.py


## 2026-08-17 — R is extensive at leading order; the count is DEGENERATE; R is not one term

Ran the structural test the confirmed step-7 functional poses. Since S = -sum log
mu is the archimedean functor (settled in qou-y0mc), any additive collective term
must itself be a sum of log-suppressions over some structure, so
T := R*A/alpha should be proportional to that structure's COUNT. One free
parameter (overall scale), not a fit.

**1. Scaling.** Over 3519 well-bound nuclides: C(A,2) all-pairs excluded at 110%
spread (this UPGRADES the existing scaling screen from the A>=24 band to the whole
chart); pure surface A^(2/3) excluded at 17.4%. Everything linear in A sits at
9.7-9.9%.

**2. THE COUNT IS DEGENERATE — the important negative.** The six 'good' rows
differ by 0.2pp. Rescaled to the A column at A=100 they all collapse to ~1.207:
A-1 -> 1.2075, A-2 -> 1.2094, A -> 1.2062, 3A -> 1.2062, 3A-1 -> 1.2066,
blocks -> 1.2077. They are ONE fit in different units. Reporting 'A-1 is tightest
at 9.7%' as an identification would be over-reading. The test constrains the
SCALING (extensive), NOT the structure.

Discriminating among linear counts needs the O(1) offset — i.e. the light nuclei —
which are exactly the rows contaminated by the two-nucleon defect. That is a real
obstruction, not a gap in the probe.

**3. The 10% residual is not noise, and correlation cannot identify it.**
Residual range [-70.69, +15.64] alpha, sd 17.70, against a leading term of 252.5
alpha at A=208. Extremes are physically identified: most POSITIVE at A=90 Z=40
(N=50, a shell closure); most NEGATIVE at A=295 Z=118 (the superheavy Coulomb
limit). But the liquid-drop correlations are Coulomb +0.827, surface +0.702,
asymmetry +0.689, volume -0.767 — all strong, because all are monotone in A and
mutually collinear. Same failure mode as the count degeneracy; a single Pearson r
is not an identification.

**Framing conclusion: 'find the missing collective term' is the WRONG FRAMING.**
R is at least three things: (1) an extensive piece ~1.207 alpha/nucleon,
scaling-identified but structure-degenerate; (2) shell structure; (3) a large
negative high-Z piece consistent with Coulomb, which the framework does not model
AT ALL. Only (1) is plausibly categorical. A search treating R as one object is
looking for something that is not there.

Scope-(a) throughout. Established: leading behaviour is extensive; all-pairs and
pure-surface excluded. NOT established: which extensive count, the residual's
decomposition, or that a categorical object supplies (1).

Probe: computations/probes/collective_term_shape_degeneracy_probe.py


## 2026-08-17 — RETRACTION + where Coulomb IS derived in QOU

**Retraction.** My shape-degeneracy probe said the high-Z residual is 'consistent
with Coulomb, which the framework does not model AT ALL'. **False. I skipped the
corpus-grep checklist.** The corpus carries def:coulomb-charge
(content/.../knots-particles-confinement/coulomb-charge.{md,ts,lean}),
magic-shell-coupling-kappa (shell, identification withdrawn),
docs/coordination/alpha-em.md, docs/audits/2026-08-01-em-linking-reads-round1.md,
and deprecated per_braid_tower_coulomb.py / coulomb_subtracted_binding.py /
term_7_shell_correction_test.py.

**What QOU actually derives.** def:coulomb-charge splits the crossing energy into
bar-even (strong) and bar-odd (Coulomb) parts:

    E_cross = (1/2)(n+ + n-)(q + 1/q)  +  Q (q - 1/q),   Q = (1/2)(n+ - n-)

Coulomb/strong = tanh(ln q0) = 0.103964 (block states ~0.104).

**Q = 2Z + eps on the framework's own words**, eps = 3.4393e-04 a CONSTANT
(spread 1.4e-14 across 2H..208Pb). Structural reason: writhe = 3Z + N + (Z-1)(+1)
+ (N-1)(-1) + e_pn = 4Z + e_pn, so N cancels entirely. The offset is the single
colour-weighted pn bond: under canonical bring_color_weighted its
d = -0.104458248 rather than the midpoint -h/2 = -0.104530149, giving crossing
sign e_pn = +6.878e-04 instead of 0. One per nucleus, hence constant.
(I first wrote 'Q = 2Z exactly' off a 2-decimal table; the probe's assertion
caught it. Colour weighting breaks exact integrality of the Coulomb charge by a
fixed universal amount — the corrected version is the more informative one.)

**THE GAP: linear vs quadratic.** Framework EM = tanh(ln q0) x strong; physical
Coulomb = a_C Z(Z-1)/A^(1/3):

    4He 1.0x | 12C 2.7x | 40Ca 6.5x | 56Fe 7.0x | 90Zr 8.8x | 208Pb 12.1x

Exact at 4He, diverging monotonically — the Z vs Z(Z-1) signature. **The framework
has a CHARGE; it has no charge-charge interaction energy.** Q*h is linear in the
charge; electrostatics is a pair energy and needs a quadratic term.

**The EM sector IS the writhe grading (route 2).** Q = (1/2)(n+ - n-) is half the
writhe, so the corpus's Coulomb correction and the T_3/writhe grading I closed as
route 2 are the SAME object. That is a consistency, not a failure: EM should be
small (10.4%), and route 2's conclusion (the writhe cannot fix the STRONG sign
structure) is correct physics.

**Prior art on shell, with a warning for me.** magic-shell-coupling-kappa proposed
a magic-shell coupling and WITHDREW it: its two anchors (3He, 3H) disagreed in
sign by a factor 5.3, and restoring the electrostatic energy of 3He's pp pair
removed the discord, leaving an excess coefficient of ZERO. An apparent SHELL
effect turned out to be electrostatics. Direct caution against reading my
residual's N=50 peak as shell structure.

**Where a quadratic term could live.** A single interface generates only the
2-dimensional span{1, sigma} (sigma^2 = h sigma + 1), so every single-bond
quantity is affine in the crossing — a Q^2 term CANNOT live at one bond. It could
live in the multi-bond word where distinct bonds' crossings pair, which is the
same structural place the many-body term must live. Not excluded by anything
proved; also not established.

Probe: computations/probes/coulomb_charge_is_linear_in_z_probe.py


## 2026-08-18 — the multi-bond quadratic lead is CLOSED at n=3

The last named lead: a Q^2-like pair term cannot live at one bond (single
interface = 2-dim span{1,sigma}), so it would have to live at MULTI-BOND level.
That is also the one place the many-body collective term could come from.

**A circular test, avoided.** Feeding a multi-bond word to
pyhecke.trace.markov_trace_at_q and checking factorisation is CIRCULAR — the
production trace is *implemented as* a bare product over generators
(`tr_M *= Vs` in the per-generator loop), and its docstring says so ('Only the
descended term = Pi V_i'). All three entry points (markov_trace_at_q,
markov_trace_symbolic_eval, tr_M_at_q0_via_crt) carry the same 'descended'
wording. Same shape as the circular CHECK-1 in the hyperbola probe.

**The independent route** is pyhecke.trace.nf_tr — a linear functional on the
Groebner-Shirshov normal-form basis of H_3,
NF_BASIS = [(), (0,), (1,), (0,1), (1,0), (0,1,0)] — which contains the
INTERLEAVED word (0,1,0). The product formula depends only on the per-generator
multiset, so it must give the same answer for sigma0 sigma1 sigma0 and for
sigma0^2 sigma1. The NF functional can tell them apart.

**Result — it doesn't:**

    sigma0 sigma1 sigma0   INTERLEAVED   0.6911664783584446
    sigma0^2 sigma1        sequential    0.6911664783584445
    (z*h + 1) * z          PRODUCT       0.6911664783584445
    interleaved - product = 7.4e-17

The product formula is EXACT for the interleaved word. So log tr is strictly
additive over generators and NO term quadratic in crossings across distinct
bonds exists at n=3. The trace does not couple distinct bonds at all.

**Scope-(a), narrow, and the limits are real:**
* n = 3 ONLY — H_3's NF basis has exactly one interleaved word. General-n
  multiplicativity is not established here; it is standard for far-apart
  generators (Markov property iterated down the tower), and this adds the
  adjacent case at the smallest n.
* float64 resolution — TR_M is a float64 table, so agreement resolves only to
  ~1e-16. A cross term below that is invisible. But a 1e-16 term cannot supply a
  12.1x Coulomb shortfall.

**Where this leaves the axis.** Both open items on qou-ls86 now have their named
lead closed: the Coulomb order-deficit (linear vs quadratic in charge) and the
many-body collective term were to share a multi-bond quadratic source, and this
trace has none. What remains is outside the trace: a different word class, a
different functional, or physics the framework does not represent (shell,
electrostatics). No candidate is proposed.

Probe: computations/probes/markov_multiplicativity_interleaved_probe.py


## 2026-08-18 — CORRECTION: the multiplicativity result was measured in float64

The 2026-08-18 entry above reports the multi-bond test as
'interleaved - product = 7.4e-17' from nf_tr against pyhecke.trace.TR_M.
**That test was VACUOUS.** TR_M is a float64 table, so any comparison through it
agrees to ~1e-16 regardless of what is true. I recorded the float64 resolution
as a scope caveat and shipped, which is exactly the move the owner has now
banned (AGENTS.md, 'PROBES ARE NOT EXEMPT', 2026-08-18).

**The conclusion survives, by exact algebra instead of measurement.** On H_3,
from tr(1)=1, the Markov property tr(x sigma_last) = z tr(x), cyclicity, and the
Hecke relation sigma^2 = h sigma + 1 — with no numbers at all:

    tr(s0 s1)    = z * tr(s0) = z^2
    tr(s0 s1 s0) = tr(s0^2 s1)            [cyclicity]
                 = h tr(s0 s1) + tr(s1)   [Hecke]
                 = h z^2 + z
    (z h + 1) z  = h z^2 + z
    difference   = 0, IDENTICALLY in (q, z, h)

Equal as rational functions — not 'agrees to 1e-16'.

**And the exact route SHARPENS the n=3 caveat.** It works because cyclicity
rotates the trailing s0 forward, where the Hecke relation collapses s0^2 back
into span{1, s0}. H_3's single interleaved word is a cyclic rotation of a
sequential one — a property of H_3 being small. For larger n there are
interleaved words with no such rotation (e.g. s0 s1 s0 s2 s1). **General n is
OPEN**, and the earlier entry's confidence was not earned.

**Also corrected in this bean's earlier entries:** the Coulomb offset was
computed with hf = float(pyhecke.gram.h). Recomputed at 50 dps it survives as
0.000343927701756774002 with spread 8.4e-48 (not 1.4e-14). The shape-degeneracy
figures were statistics.mean/pstdev over 3519 float64 rows; recomputed with
mpmath they are unchanged (9.733%, 1.2197, 110.1%, 17.44%, ~1.207 collapse), so
those conclusions stand.

Probes now mpmath/sympy end-to-end; precision-gates.sh --changed green.
