---
# qou-cds1
title: 'S1 (SCIENCE): re-derive the Q_beta c_k ladder under D — not a z-swap, and that is proved'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-11-21T04:40:00Z
parent: qou-wxhi
---

Parent: `qou-cdx1`. **The largest science item in the ruling.** Supersedes the
`disputed` outcome of `qou-b3nk`.

## What moves (registry §9g, probe `qbeta-c3-ladder-trace-convention-sensitivity`, 9/9)

| fact | C frame | D re-extraction | consequence |
|---|---|---|---|
| `c₃` (proton / muon) | −2.06934258 / −2.02020024 | **−974.43 / −974.38** | every ≈−2 value-level fact is C-conditional |
| anchor swing | 0.0491423 | 0.0493990 (ratio 1.0052) | REFUTED-as-real-q **survives** |
| implied empirical `c₂` | −1.0176 | **−9.299** | `c₂ = −1` is a C-frame statement |
| N2/N1 residual ratio | 0.017 (58× rung gain) | 0.89 (**no convergence**) | rung convergence is C-frame only |
| bar parity of `z` | `bar(z_C) = z_C` | `bar(z_D) = q⁻⁴·z_D` | KC13's prune is C-scoped |

**C-conditional downstream, all named in §9g:** (H1) `c₃^even = −Vol(4₁)`,
`[3]_q/25`, `J − ℏ²`, `S_leak`, `q*_S`.

## The load-bearing constraint — this is NOT a z-swap

`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free, PR #5111): **any**
faithful normalised Markov trace at the ladder's `z_C` carries `y_(1³) ≠ 0`, for
**every** substrate `s = √q > 1` (the coincidence locus `s⁷+s⁵ = s⁴+1` factors
as `(s−1)(s⁶+s⁵+2s⁴+s³+s²+s+1)` and is empty there).

So *"keep the C-frame ladder"* and *"the two-row forcing applies here"* are
**mutually exclusive**. Under the ruling the decay trace is `z_D` — and **the
existing ladder is not that trace.** The ladder must be **re-derived**, not
re-evaluated.

**`c₃ ≈ −974` is a sensitivity measurement, not a proposed value.** It is what
the *current extractor* returns when fed `z_D`. Do not wire it anywhere.

## Live C sites in the decay channel

- `computations/qbeta/qbeta_utils.py::markov_parameter` + `substrate_ladder_quantities`
  (`α = (z−1)h/2` at `z_C` feeds every committed `c_k` extraction)
- `computations/qbeta/qbeta_ck_sseries_exact_rational.py:20,248` — the KC21/KC22
  `D(ũ)`-ladder core. **Naming hazard:** the `D` there is KC21's bar-even ℚ(√3)
  ladder *function* `D`, **not** convention D. Those lines evaluate `z = √q/(q+1)`.
- `content/.../lean/QOU/QBeta/ZBarParity.lean:59-79` (KC13 bar-even `z`)

## Discipline

Formalize-first: before any wide numerical re-fit of the ladder, state the
structural constraint the D-frame ladder must satisfy and check whether it
prunes the class. A re-derivation that lands on a nice number by search is a
fit, not a derivation, and the anti-laundering rule applies unchanged.

## Red-team verdict (2026-08-16, adversarial audit — docs/audits/2026-08-16-ck-ladder-red-team.md)

BOTTOM LINE: the c_k ladder is convergence-framework PHYSICS wrapped around higher-coefficient NUMEROLOGY, and the corpus already separates them correctly.

Per-claim:
- c_2 = -1: symbolic-exact but the Lean is a ring tautology (1-b2h4 = 1-(bh2)^2); the N=2-factor identification is asserted in a docstring, not derived. Anchor-stable to 1e-50 (real). C-frame (implied empirical c2 under D = -9.299).
- c_3 = -2 = J_Hopf(q=1): FITTED/near-match. Extracted by inverting the single Q_beta anchor; ~2 reliable digits; swings 2.98% cross-anchor (15000x its rigidity); REFUTED as real-q. The '=-2' is a 1-2 digit shadow coincidence 5 eps-orders off the ladder order.
- c_k>=4: FITTED/noise. c_4 vanishes when c_3 extracted exactly (normalisation artifact); zero reliable digits at k>=4; c_6/c_7 imposed in extraction (self-consistency); c_8 pattern breaks (wrong sign).
- KEY Q: series convergence is REAL (radius=u_substrate, kappa=0, KC22 Lean); N(eps) 'derivation' only holds for O(1) coeffs which c_k>=3 are NOT; the N=4->N=5 non-monotonicity is a fit tell the framing itself flags. Production wires c_2 ONLY -- the fit was caught and never shipped.
- C->D: does NOT survive. Ladder is z_C end-to-end (qbeta_utils.py:124). Under D c_3->-974, convergence vanishes, and decayLadder_zC_threeRow_ne_zero PROVES it's not a z-swap (C ladder trace and D two-row trace mutually exclusive). Honest status: UNKNOWN pending D re-derivation.
- (H1) c3^even = -Vol(4_1): NOT derived -- defined residual S_leak:=c3+Vol(4_1); not determinable from anchor data; '0.48%' agreement is 0.031 sigma = no evidence.

DOF-vs-precision: ladder fits ONE experimental scalar (Q_beta) with unboundedly many residual-absorbing coefficients; only c_3 carries signal (~2 digits) and those swing 3% across anchors. No high-precision identification exists.

Do NOT: re-quote any C-frame c_k as a D result; resurrect c_3=-2=J_Hopf as a derivation (that is flip-flop #5).

## Step 1 done (2026-08-16) — the formalize-first prune this bean asked for

PROVED, sorry-free, generic CommRing (MarkovZFullBarCondition.lean):
  eigenphase_barOdd_of_barEven      bar(z)=z    => bar(2a)+2a = 0
  eigenphase_bar_defect_of_fullBar  bar(z)=z-h  => bar(2a)+2a = h^2
axioms: [propext, Quot.sound] on both; lean-direct exit 0.

The ladder eigenphase a = (z-1)h/2 is bar-odd EXACTLY when z is bar-even.
z_C is bar-even, so eigenphase_bar_involution holds -- as a C statement.
z_D satisfies the full-bar condition, so under D the eigenphase is NOT
bar-odd and the defect is exactly h^2/2. That is a structural reason the
C->D move cannot be a z-substitution, independent of any number: the swap
keeps the formula while breaking the parity its consumers assume.

The defect is z-INDEPENDENT, so no member of the full-bar family restores
bar-oddness. The bar-odd projection is therefore forced with no free
parameter: a_odd = a - h^2/4.

MEASURED (probe qbeta-d-frame-eigenphase-bar-parity, both anchors):
  frame                     implied c2      c3      rung gain
  C (alpha_C)                  -1.018    -2.069        57.7x
  D z-swap                     -9.299  -974.43         1.12x
  D bar-odd projection         -1.733   -86.08         2.36x

Scope-(a): NECESSARY and derived, but NOT sufficient. Do not search for
further corrections until one lands near -1; that is a fit.

## Remaining piece

The two-row cap. WenzlWeightVanishing.lean landed 2026-08-16 (sorry-free,
all n; z_D is Wenzl level r=2 exactly), supplying exactly the input
qbeta_c3_ladder_trace_convention_sensitivity_probe named as its own open
item ('the two-row cap argument has not been examined for the decay
channel'). Under D the >=3-row blocks are annihilated, so chi_(1,1,1)
drops from the H_3 decomposition. NOT folded in yet: the ladder as
written exposes z only through alpha, not through the per-block
characters, so folding it in means going back to where the (z-1)h/2 form
is derived.

---

## Progress (PR #5210, 2026-08-16) — the phase is inverted, and C crosses it

Formalize-first step done before any re-fit, per the Discipline section above.

**α is not a prediction.** It enters at one place, `cos(α − u/2)`, and `c₃` is
obtained by *inverting* the ladder against the measured Q-value. Inverting for
α and reporting in radians instead of `c₃` units:

    window for |c3| <= 1     +-1.09e-5 rad
    convention C misses by    2.26e-5 rad  (-0.04%)   c3 = -2.0693
    convention D misses by    1.19e-2 rad  (-22.7%)   c3 = -974.43

So the table at the top of this bean (`c₃: -2.07 -> -974.43`) is the same fact
as "the phase error grows from 0.04% to 23%". The 500x is the fixed `1/u³`
magnifier, identical for both conventions — asserted as an exact identity in
`qbeta-ladder-required-phase.witness.json`, not estimated.

**Prune achieved (scope-(a)).** `z_D` sits ~1000 window-widths from the
required phase, so no D-frame ladder is recoverable by substituting `z_D` into
`α = (z−1)h/2`. The FUNCTIONAL FORM must change. The one-parameter class
"α = (z−1)h/2, z a convention parameter" is pruned for D without running a
search over it — which is what the Discipline section asked for.

**The finding that also bears on C.** `α_required` and `α_C` move in OPPOSITE
directions with q: slopes `+41.53` vs `−0.455`, ratio `−91`. They CROSS at the
substrate anchor rather than coincide. The 2.3e-5 rad agreement at q₀ is a
transversal crossing of two curves with different q-dependence, not a
functional identity.

That is consistent with where α comes from:
- `q-beta-cos-resummation.ts:48` — the eigenphase identification is
  **AXIOMATISED** (class `QOU.Interactions.QBetaCosResummation`). Per
  §"Axiomatization is NOT a Proof" that is an assumption, not a derivation.
- `q-beta-spectral-bridge.lean:188` — `(z−1)h/2` first enters as the O(h)
  Taylor coefficient of the Form-A/Form-B bridge `(1−h/2)/(1−zh/2)`, algebraic
  in z, carrying no representation-theoretic content by itself.

So **neither frame's α is derived.** C is numerically close, at a crossing.

**Also recorded:** past ±0.1% in q the ladder has no real phase at all (`Q_A`
exceeds `Q_codata` by only 0.17%, so the arccos argument leaves [−1,1]).

**Sibling state incorporated** (both cited, not re-derived): S2 (#5185) solved
the D weight vector directly; #5187 RETRACTED its positivity headline, so
"D fails positivity" is withdrawn and the wall moved to the phase. Two rows of
the table at the top of this bean are superseded by #5187: `c₂ = −1` is
convention-immune (registry §9g row 3 is wrong), and `c₃` is not an
independent rung (`c₃ = (c₂^emp + 1)/(u(1−u²))` exactly with `c₂` hardcoded).

**Independent confirmation added:** S2's n=3 solve equals the Lean-proved
general-n D formula `yw q n m = [m]_q/[2]_q^n` exactly on all three weights,
with `Σ dim·y = 1`. Third route; neither sibling had checked it.

## Still open — this narrows, it does not close

The re-derivation is NOT done. What a D-frame ladder needs is a phase of a
DIFFERENT functional form, derived from the representation rather than
axiomatised. Nothing here supplies one, and the crossing result says the
C-frame answer is not a template to copy.

## The phase is a BAD COORDINATE (2026-08-16, follow-on)

alpha_req has a square-root branch point at q_b = 1.110663462558, only
**0.062% above q0**; the law alpha_req - u/2 ~ -sqrt(2*eps(q)) reproduces the
measured slope to 0.5% (41.30 vs 41.53), where eps = 1 - Q_cod/(Q_A(1-u^2)).

Consequences:

1. **The slope mismatch is structural, not accidental.** alpha_C is analytic
   near q0; alpha_req is not. No analytic-in-q phase ansatz can equal
   alpha_req as a FUNCTION -- they can only cross at a point. So the prune
   extends from "no z-family" to "no analytic phase ansatz at all".

2. **The branch point is a parameterization artifact.** If the true
   correction is a smooth factor F(q) = Q_beta/Q_A, then writing
   F = cos(alpha - u/2) manufactures a sqrt singularity wherever F = 1. The
   cosine INTRODUCES the pathology; it is not in the physics. The natural
   coordinate is the multiplicative correction F, which is smooth.

3. **c_3 inherits it.** c_3 is defined through the cos parameterization, so
   its steep anchor-dependence and the S_leak window are downstream of a bad
   coordinate choice, not of substrate structure.

Recommendation for whoever takes the derivation: work in F, not alpha. The
eigenphase identification that forces the cosine is AXIOMATISED
(QOU.Interactions.QBetaCosResummation), so dropping it costs nothing proved.
Target to DERIVE (not match): 1 - F(q0) = 1.6748e-3.

## Progress 2026-08-18 (PR #5283) — two-row cap folded in; c_k shown to be a bad coordinate

TWO-ROW CAP: FOLDED IN, and it does NOT supply the correction. This closes the
'Remaining piece' item above. Measured at n=3, both anchors:
    dim*y_(1,1,1) in C = 0.0227449  = 13.6x the target 1.6748e-3
    sum dim*y = 1 in BOTH frames (C on three blocks, D on two)
So the cap is an order too big AND leaves no residue -- each frame is already a
complete normalised trace on its own support. The D two-row weights close by
themselves: y_(3)=(q^4+1)/(q^2+1)^2, y_(2,1)=q^2/(q^2+1)^2, 1*y_(3)+2*y_(2,1)=1
exactly. Class 'F = two-row restriction fraction of the n=3 trace' pruned with
NO search over it. Scope-(a): no invariant proved; the cap is not excluded as
one ingredient of a multi-term closure.

c_k IS A BAD COORDINATE, exactly like the phase, and by an EXACT factor:

    c_2 + 1 = (F_required - F_N2) / (F_N1 * u^2)      [verified ~1e-47, 50 dps]

magnifier 1/u^2 = 13785, FIXED, carrying no model information -- the same role
the 1/u^3 magnifier plays for c_3. A 1% F-error becomes a 137.6 shift in c_2.

CONSEQUENCE FOR THIS BEAN'S OWN TABLE. The forced bar-odd projection is recorded
above as 'implied c2 = -1.733', which reads as a 73% catastrophe. In F:
    C                  -0.076 %
    D z-swap           -35.9  %
    D bar-odd (forced) - 3.17 %
The forced projection buys ~11x over the z-swap. The c_2 coordinate concealed
it. Judging D-frame progress in c_k units overstates the failure by ~1e4.

NOT A CLOSURE. -3.17% is five orders from L2 (~7.8 ppb for Q_beta). This bean's
verdict on the bar-odd projection is UNCHANGED -- necessary, derived, not
sufficient -- and its instruction not to search for further corrections until
one lands near -1 stands. The finding is about MEASUREMENT, not progress.

Chain validated against this bean's three recorded numbers BEFORE concluding
anything: -1.0176 / -9.2989 / -1.7331 reproduce -1.018 / -9.299 / -1.733. It
also reproduces the committed dashboard's Q_beta miss to 163.98x vs 164.0x.

SHARPENING of my own 2026-08-18 accuracy audit: 'the 164x floor is
C-conditional' is understated. Correct statement -- under D there is currently
NO Q_beta prediction at all, because no D-frame ladder has been derived. The
only D number available is from the refuted z-swap (77263x) and is a
sensitivity measurement, not a value.

STILL OPEN, unchanged: a correction of a DIFFERENT functional form, derived
from the representation rather than axiomatised. Note the cosine-forcing
eigenphase identification is axiomatised (QOU.Interactions.QBetaCosResummation)
so dropping the cosine costs nothing proved -- and the c_k readout should be
dropped alongside it, since both coordinates distort the residual by fixed
magnifiers.

Audit: docs/audits/2026-08-18-convention-d-two-row-cap-and-ck-magnifier.md

## 2026-08-18 follow-on (PR #5283) — the projection does not make the PHASE bar-odd

Extends THIS BEAN's bar-parity analysis by the one term it never checked. The
Lean above is about the eigenphase a alone. The ladder's phase is a - u/2, and
u's parity was never examined. Symbolically (bar: q -> 1/q):

    h -> -h (ODD);  h^2, b (EVEN);  hbar_q -> -q*hbar_q;  u -> q^2 * u

u is NEITHER bar-even nor bar-odd. So for ANY bar-odd a,

    bar(a - u/2) + (a - u/2) = -u(1+q^2)/2  !=  0.

MEASURED (50 dps, both anchors):
  * the defect is IDENTICAL in C and D: -0.0095054571 for a_C and for the
    forced a_odd alike. Carried entirely by u => CONVENTION-INDEPENDENT.
    This is a ladder problem, not a D problem.
  * replacing u/2 by its bar-odd part u(1-q^2)/4 moves 1-F by 15.1% of the
    required correction -- not a rounding term.

The two Lean theorems are CORRECT AS STATED (they concern a). What does not
follow is the motivation: making a bar-odd does not make the phase bar-odd, so
'restore bar-oddness' is not achieved by a_odd on its own.

NOT SETTLED, and flagged rather than assumed: whether F is REQUIRED to be
bar-even. Q_A is not bar-odd in the naive sense --
bar(Q_A)/Q_A = q^3*|q^2+2q-1|/|q^2-2q-1|, not +-1 -- so the requirement cannot
be read off the chain as written. If bar-evenness is not required this is a
curiosity; if it is, the ladder violates it in BOTH conventions by a 15% term
and the projection is incomplete rather than forced-and-final. Resolving that
question looks like the cheapest next step, because it decides whether the
u/2 term needs replacing before any new functional form is attempted.

Probe: computations/qbeta/qbeta_phase_bar_parity_completeness_probe.py

### …and the parity requirement turns out not to be available at all

Follow-on to the item above, which had left open whether F must be bar-even.
The corpus states the requirement AND names the involution:

  'the bar-odd (sinh) partner of the bar-even (cosh) meson scale m_pi UNDER THE
   BAR-INVOLUTION q -> q^{-1}'
  -- three-calibration-discipline.md:18; also
     epistemic-status-of-calibrations.md:3,
     three-calibration-discipline-proof.md:36, AGENTS.md.

Testable against the closed form the framework computes. Measured, both anchors:

    Q_A/m_e at q   = 1.5335566273012
    Q_A/m_e at 1/q = 2.5868438911015
    bar(Q_A)/Q_A   = 1.686826456258      <- odd would be -1, even would be +1

NEITHER, and not marginally. q -> -q and q -> -1/q give non-constant ratios too.

CONSEQUENCE: a bar-parity constraint on the D-frame correction CANNOT be derived
from 'Q_beta is bar-odd', because Q_beta as computed is neither. The open
question resolves as NOT AVAILABLE from the chain as written. Anyone invoking a
parity constraint on F must first supply the object that actually carries the
parity -- it is not this closed form.

SCOPE (this contradicts four corpus sites, so stated carefully): the measurement
is of Q_A = m_e|q^2-2q-1|(q+1)/(2q^3), which is what AGENTS.md gives for Q_beta
and what qbeta_utils computes. If the parity claim is meant for a DIFFERENT
representation -- an unevaluated sinh form, or the width D_beta before inversion
-- it may hold there, and the defect is that the corpus attaches it to this
form. Either way the statement as written does not hold of the computed object.
m_pi's claimed bar-evenness is NOT tested.

Probe: computations/qbeta/qbeta_bar_odd_sinh_partner_check_probe.py

NET EFFECT ON THE RE-DERIVATION: bar-parity is now removed from the toolkit as a
CONSTRAINT (it cannot be derived), while remaining available as a DESCRIPTION of
a to-be-identified object. That is a narrowing, not progress: it says one more
route into the D-frame correction is closed.

### SETTLED 2026-08-19: the 'sinh partner' is Im(frak V) -- and my 'not available' was WRONG

Owner asked what object the description was about, pointing at q-hyperbolic
geometry. Answer: the COMPLEX VOLUME.

three-calibration-discipline.md:18 cites
mass-theory/substrate-cohomology-calibration-story.md, line 11:
  'A crossing has two eigenvalues, q and -q^{-1}. Setting lambda = log q, these
   split as cosh(lambda) +- sinh(lambda). ... binding sits on the cosh, bar-even
   side ... Q_beta and its precision coefficients sit on the sinh, bar-odd side.
   ... That single element is the COMPLEX VOLUME frak-V. Re frak-V = E_bind.
   Im frak-V = Q_beta, the QOU analogue of Neumann-Zagier Vol + i CS.'
and conj:binding-qbeta-complex-volume states
    frak-V(K) = E_0 tr_M((Pi_free - 1).M),  E_bind = Re,  Q_beta = Im.

So bar (q -> 1/q) IS lambda -> -lambda and sinh/cosh parity is exactly
bar-odd/bar-even. The sinh partner is Im(frak V) -- the Chern-Simons-analogue
part of the complex volume, NOT the rational closed form.

RETRACTION of my own previous entry. I concluded a bar-parity constraint on F
was 'NOT AVAILABLE from the chain as written'. That was WRONG -- I had not found
the object carrying the parity. The constraint IS available.

CORRECTLY STATED: writing Q_beta^pred = Q_A * F, the requirement is NOT that F
be bar-even. It is that Q_A * F be BAR-ODD: Q_beta(1/q) = -Q_beta(q).

MEASURED (both anchors):
    Q_A alone                bar-ratio = +1.686826    (bar-odd needs -1)
    Q_beta^C = Q_A * ladder  bar-ratio = +1.687595
    ladder's effect on the ratio: 0.046 %

TWO READINGS, both worth keeping:
  * the chain VIOLATES the conjecture's parity requirement outright;
  * the entire precision ladder moves the ratio by 0.05%, so the violation is
    inherited wholesale from Q_A -- the ladder does essentially nothing to
    restore bar-oddness.
=> either Q_A is NOT Im(frak V) (the closed form is a different object from the
   one the parity claim is about), or the conjecture's parity claim fails for
   the computed object. THE CORPUS DOES NOT DISTINGUISH THESE. Settling that is
   the next step, ahead of trying any further candidate F.

CONDITIONALITY: conj:binding-qbeta-complex-volume is a CONJECTURE,
class-axiomatised in Lean (ComplexVolumeMatch / SingleFrakVAssembly /
StageCSigma3Lift). So Q_beta's bar-oddness is CONDITIONAL on it, and the four
sites asserting it as fact -- three-calibration-discipline.md:18,
epistemic-status-of-calibrations.md:3, three-calibration-discipline-proof.md:36,
AGENTS.md -- omit the conditional ('conditional-proved != premise-established').

NET: restores a constraint I had wrongly removed, and it is far sharper than
matching 1-F(q0)=1.6748e-3 at a single point -- it constrains F as a FUNCTION.

Probe: computations/qbeta/qbeta_sinh_partner_object_identification_probe.py

### FORK RESOLVED 2026-08-19: Q_A is the COUNIT; Im(frak V) is the TRACE

Previous entry left two possibilities the corpus did not distinguish. It is the
first, and the corpus says so explicitly once the derivation is located.

nuclear-interactions/qbeta-counit-closed-form.md derives the closed form as a
FROBENIUS COUNIT evaluation:
    eps(Delta)*E_0 = m_e(q+1)(q^2-2q-1)/(2q^3),  E_0 = m_e/(q(q-1)),
    Delta = NF(n) - NF(p) in H_3(q)
and states the distinction outright:
    eps(Delta) = h^2/2 - h,   tr_M(Delta) = h^2/2 - h*z
    'The two agree precisely when z = 1. The trivial-loop value is never
     attained on the substrate. THE COUNIT AND THE MARKOV TRACE ARE GENUINELY
     DISTINCT FUNCTIONALS ON THE SUBSTRATE.'
while conj:binding-qbeta-complex-volume defines
    frak-V = E_0 * tr_M((Pi_free - 1) . M)      -- a TRACE object.

VERIFIED: eps(Delta)*E_0 reproduces the committed closed form EXACTLY
(-0.783645827375 vs +0.783645827375). The closed form's |q^2-2q-1| discards the
sign -- worth noting, since a bar-odd object is signed.

=> the +1.687-vs--1 bar-ratio is NOT a corpus contradiction. Q_A was never the
object the parity claim is about. Question closed.

THE IDENTITY THIS EXPOSES (the real result):

    eps(Delta) - tr_M(Delta) = h(z-1) = 2*alpha        [exact, any z]

The ladder's phase alpha is EXACTLY HALF THE COUNIT-MINUS-TRACE GAP. So alpha is
not an arbitrary parameterisation: the precision ladder is implicitly
TRANSPORTING the evaluation from the counit to the trace, and alpha measures
precisely that gap.

This also LOCATES THE UNJUSTIFIED STEP. It is the COSINE -- exponentiating a
DIFFERENCE into cos(alpha - u/2) -- which is exactly the axiomatised piece
(QOU.Interactions.QBetaCosResummation). The gap is structural; its
exponentiation is not. That is a much more specific target than 'derive a
different functional form': the object to derive is the counit->trace
transport, and alpha already measures its infinitesimal generator.

MEASURED ONCE, NOT PURSUED: bare transport ratios on Delta are
    C: trM/eps = 0.44087, odd(trM)/eps = 0.55761
    D: trM/eps = 0.56748, odd(trM)/eps = 0.68421
against F_required = 0.998325. None close, so the transport is not a bare ratio
of these functionals on Delta. Deliberately not explored further -- hunting
combinations that land near 0.998 is the fit this bean forbids.

NEXT (concrete, and narrower than before): derive the counit->trace transport
for the frak-V operator (Pi_free - 1).M rather than for Delta, in convention D.
That is now a specific object with a specific role, not a search over functional
forms -- and alpha = (eps - tr_M)/2 says the ladder was always approximating it.

Probe: computations/qbeta/qbeta_counit_vs_trace_fork_probe.py

### TRIED 2026-08-19: the frak-V transport route is BLOCKED at the source

Attempted the concrete next step from the previous entry -- derive the counit ->
trace transport for the frak-V operator (Pi_free - 1).M rather than for Delta.
It CANNOT BE STARTED, and the reason is a corpus defect worth recording.

The transport is a change of FUNCTIONAL, so its effect on X is fixed by X's
character vector:
    tr_M^z(X) - eps(X) = sum_lambda [y_lambda(z) - y_lambda(1)] * chi_lambda(X)
(eps = tr_M at the trivial loop value z=1). So the frak-V transport needs
chi_lambda((Pi_free-1).M) -- i.e. frak-V evaluated as a TRACE object. Never done.

complex_volume_witness.py opens 'frak-V = E_0 tr_M((Pi_free-1).M) as ONE object'
and then computes Re from tr_M but IMPORTS Im:
    from q_beta_substrate_prediction import q_beta_substrate     (line 39)
So Im IS the counit closed form Q_A. VERIFIED: the witness's
im_qbeta_pred_MeV = 0.7836458273746213 equals |eps(Delta)*E_0| to 9e-17.

The two halves of the 'one object' come from TWO DIFFERENT FUNCTIONALS -- Re
from the Markov trace, Im from the Frobenius counit -- which
qbeta-counit-closed-form.md itself calls 'genuinely distinct functionals on the
substrate'. The 'one object' is not realised in compute.

CONSEQUENCES:
 1. Transport blocked at the source -- Im(frak V) is the counit object by
    ASSIGNMENT, so there is nothing to transport TO.
 2. THE PARITY CLAIM IS CIRCULAR. The corpus says Q_beta is bar-odd BECAUSE it
    is Im(frak V); in the only compute Im(frak V) IS Q_beta, whose bar-ratio is
    +1.6868 (neither parity). Asserted of an object defined to be the object
    whose parity is in question.

ALSO MEASURED (bears on how much that witness establishes):
  * assertions: []  -- it asserts NOTHING; allPassed:true is VACUOUS.
  * its REAL part -- the half that genuinely IS a tr_M object -- misses AME
    binding by 21.8% / 21.8% / 36.7% / 69.3% on 2H / 3H / 3He / 4He.

This is the AGENTS.md 'Defined residual != derived decomposition' family.

SCOPE: does NOT refute conj:binding-qbeta-complex-volume. It says the conjecture
is UNTESTED by the compute that appears to test it, and the transport route
cannot start from that compute.

WHAT THIS MEANS FOR THE BEAN. Every route into the D-frame correction that runs
through the complex-volume identification is blocked until someone actually
EVALUATES tr_M((Pi_free-1).M) for the imaginary channel. That is now the
gating computation -- and it is a well-posed one, unlike 'find a functional
form'. Until it exists, the sinh/bar-odd story cannot support any derivation,
because nothing in compute realises it.

Probe: computations/qbeta/qbeta_frakv_transport_blocked_probe.py

### 2026-08-19: WHAT BLOCKS tr_M((Pi_free-1).M) FOR THE IMAGINARY CHANNEL -- four issues

The previous entry named this the gating computation. The corpus ALREADY MAPS
why it has not been done: frakV_descent_zeta4_partner_probe.py carries a
descent_gap_map with four entries. Reported, not re-derived.

ORDERED -- the first makes the naive computation ILL-POSED, not merely hard:

 1. observable_level: 'DEGENERATE (Im(q_0)=0) -- must NOT be used to claim
    closure (numerology guard, #2951)'. q_0 is real
    (lusztig_q_0_imaginary_part_zero); the Markov weights y_lambda(q) and the
    characters are real for real q; so tr_M of a real operator at q_0 is REAL
    and Im(frak V) == 0 there. Confirmed 3 ways: the gap map; the witness's own
    fibre_caveat ('Im(q_0)=0; complex structure is fibre-level (pre-tau)'); and
    every trace the witness computed is a Python float.
    => Q_beta = 0.7836 MeV CANNOT be the imaginary part of a real number. The
    computation cannot be POSED at the level where Q_beta lives. This is the
    AGENTS.md fibre-vs-archimedean distinction and Q_beta = Im(frak V)
    straddles it.

 2. single_fibre_V: 'OPEN ... Missing: both fibre kernels AND their assembly
    into one trace object.' Not one kernel -- BOTH, plus the assembly.

 3. Im_V_qbeta: 'GATED' on conj:qdifference-kernel-prolongation-symbol
    (SW-residue jet-prolongation symbol R(q,xi)); fitting Phi_2 is the
    FORBIDDEN seventh ansatz.

 4. Re_V_binding: 'NOT closed' either (no finite low-order q-difference
    operator; Stages 3-4) -- consistent with the 21.8%-69.3% AME misses
    measured in the previous entry.

ONE FILTER IS AVAILABLE AND PROVED: the zeta_4 orbit analysis is sorry-free
(vModel_zeta4_sq / _cube / _orbit_sum_zero / _sign_isotype_zero /
_eq_faithful_sum) and gives a rejection test -- any candidate single-frak-V
assembly must be zeta_4-FAITHFUL; a nonzero orbit sum (trivial isotype) or
sign-isotype component falsifies it BEFORE any numerical comparison.

WHAT THIS ADDS: the gap map CORROBORATES the previous entry from the corpus's
own records. The discrepancy worth recording is between two artifacts --
complex-volume-unification.witness.json reads allPassed:true under the title
'frak V = E_bind + i Q_beta' and would be taken as verified, while the gap map
has it open on four fronts. The witness assigns Im and asserts nothing.
THE GAP MAP IS THE ACCURATE ARTIFACT; THE WITNESS IS THE MISLEADING ONE.

CONSEQUENCE FOR THIS BEAN: the complex-volume route cannot supply the D-frame
correction at the observable level AT ALL -- not 'not yet', but not in
principle, because Im is identically zero there. Any use of the sinh/bar-odd
story for a D-frame derivation must first close a FIBRE-level construction that
is open on three further fronts. That is a much larger programme than the
c_k re-derivation this bean is scoped to.

SIBLING: main carries fcffeee2 'lean(qou-cds1): the D-frame Markov weights are
two-row AND bar-even' -- another agent is on this bean. Coordinated on PR #5283.

### 2026-08-19 SYNC: sibling corroboration, and a prune sharper than mine

Rebased over 268 commits. Two sibling landings bear on my entries; both cited.

fcffeee29 (SIBLING ON THIS BEAN) solved the three H_3(q) Markov equations for
general z and specialised to z_D:
    y_(1^3) = 0 exactly,  y_(2,1) = q^2/(q^2+1)^2,  y_(3) = (q^4+1)/(q^2+1)^2,
    y_3 + 2 y_21 = 1 exactly
IDENTICAL to my two-row-cap measurement, reached from the MARKOV LINEAR SYSTEM
rather than from WenzlWeightVanishing's Wenzl route or my numeric evaluation.
THREE INDEPENDENT ROUTES NOW AGREE on the D weights.

THEIR PRUNE IS SHARPER THAN MINE. Both surviving D weights are BAR-EVEN, so no
quantity built from the D-frame weights alone carries a bar-odd part, and the
bar-odd eigenphase the C-frame ladder uses CANNOT BE ASSEMBLED FROM THEM AT ALL.
My entry said the repair (the u/2 term) is incomplete; theirs says the MATERIAL
IS ABSENT. That supersedes mine in force -- not a conflict, a stronger form.
Lean: QOU.QBeta.MarkovWeightsConventionD, 7 decls, sorry-free, generic CommRing.

457a27181 (qou-gzs0) UPGRADED MY OWN SCOPE-(a) CAUTION TO SCOPE-(b). theta_V =
q^{1/2}.id is a SCALAR, so a framing contributes exactly q^{T/2} with T integer
-- a DISCRETE ladder with quantum 5.36%, overshooting every L2 gap by ~4e4
(Q_beta 41873x, m_n 38254x, Delta_pn 44629x). In PR #5262 I wrote that 'the
twist closes a proof gap' is supported while 'the twist improves mass accuracy'
is NOT, marked scope-(a). They proved the scope-(b) version on a proved
invariant rather than a failed search. No conflict; the caution was warranted.
Their verdict puts L2 work where this bean is: 'the convention-D re-derivation
(qou-cds1), not the ribbon layer.'

WHAT OF MY ENTRIES SURVIVES:
  two-row cap 13.6x too big + both frames normalise ....... STANDS (triple-confirmed)
  c_k magnifier identity c2+1 = (F_req-F_N2)/(F_N1 u^2) ... STANDS (untouched)
  u/2 breaks the phase parity ............................. STANDS but SUPERSEDED
                                                            IN FORCE by bar-even
  counit-vs-trace; alpha = (eps - tr_M)/2 ................. STANDS (orthogonal)
  four issues blocking the imaginary channel .............. STANDS; bar-even adds
                                                            a FIFTH, at weights level

All six of my probes re-run post-rebase: ASSERTIONS PASS.


## MEASURED 2026-08-18: -974 is 1/u^3 amplification, not evidence D breaks

Probe: computations/qbeta/qbeta_alpha_required_c_vs_d_probe.py (4/4).

alpha_required -- the phase making the N=2 ladder hit CODATA with NO c_3 rung --
is convention-INDEPENDENT: b and u are built from the Hoefsmit couplings
(d1 = q^3/(q^2+1), d2 = -1/(q(q^2+1))), never from z.  (d1 is numerically
identical to z_D while being a different object; do not read that as 'the Gram
already uses D'.)  So one fixed target scores both frames fairly.

Residual the c_3 rung must absorb, proton anchor:
    C frame  0.11321204
    D frame  0.10136170        ratio D/C = 0.8953

MY PREDICTION WAS WRONG.  I wrote the probe expecting the D residual to be
ORDERS larger and asserted ratio > 10.  It failed.  D is 0.895x -- slightly
BETTER than C.  Retracted.

Where -974 actually comes from:
    cos(alpha_eff) differs C -> D by  0.000601154  (relative)
    1/u^3                          =  1618468.2
    product                        =  972.94833
    actual |c_3(D) - c_3(C)|       =  972.36255
    agreement                      =  0.06 %

The entire c_3 gap is the ladder's own 1/u^3 = 1.6e6 amplifier acting on a
0.06 % difference in cos.  This is the SAME amplification behind
sigma(c_k) = sigma_R/u^k, which the corpus already knows makes extracted c_k
noise-dominated.  Quoting -974 as though convention D were catastrophic
overstates what the number shows -- it measures the amplifier, not the physics.

This does NOT reinstate D-by-substitution: decayLadder_zC_threeRow_ne_zero
still proves the re-derivation requirement, and the probe wires nothing.  What
it removes is the impression that D is disqualified on the numbers.

## Two further facts for whoever derives the phase

1. THE PHASE IS NOT WHERE THE ANCHOR INSTABILITY LIVES.  The residual drifts
   0.00046 % (C) / 0.00052 % (D) between anchors, while extracted c_3 swings
   2.37 %.  Both asserted phases are anchor-stable to ~5e-4 %.  A derived phase
   will not, by itself, fix the cross-anchor swing.

2. NEITHER asserted phase reproduces CODATA at N=2 -- both leave ~0.1 rad for
   c_3 to absorb.  The un-derived alpha is open in C exactly as much as in D,
   which is why there is no C-frame derivation to port.  That is the real
   content of this bean.


## Formalize-first prune on the PHASE (2026-08-18) — narrow licence, not a block

Probe: computations/qbeta/qbeta_alpha_entropy_bound_probe.py (3/3).

Before attempting to derive alpha, I asked of the phase the question PROBE 4
asked of c_3: invert the ladder for alpha_required, then count reliable digits
against the PSLQ entropy floor n*log10(2H).

    cos(alpha_eff_req) = Q_codata / (Q_A (1 - u^2))
    sigma(alpha_eff)   = cot(alpha_eff) * sigma_rel(Q_beta)

MY HYPOTHESIS WAS WRONG.  I predicted a blanket entropy block and asserted
best-case D_eff < cheapest floor.  It FAILED: 5.61 > 3.90.  The phase is NOT
as noise-starved as c_3.  Third refuted prediction in this tranche; the
measurement beat the guess each time.

What is true, as a per-(sigma, basis) grid:

    D_eff(alpha)  experimental sigma 7.8e-7 : 3.61427 digits
    D_eff(alpha)  optimistic   sigma 7.8e-9 : 5.61427 digits

    basis                floor    experimental   optimistic
    minimal n=3 H<=10    3.903    NO             yes
    standard n=4 H<=100  9.204    NO             NO
    wide n=6 H<=100     13.81     NO             NO

Identifying alpha by matching alpha_required is permitted by entropy ONLY for a
3-term height<=10 basis AND only under a sigma nobody claims.  Every realistic
basis is blocked at both readings (deficit 3.59 digits even at the optimistic
sigma).  A narrow licence, not a green light -- worth stating before anyone
runs a wide search.

## The amplifier on the phase is NOT 1/u^3

cot(alpha_eff) = 17.6436.  The rung's amplifier is 1/u^3 = 1.6e6 (now proved
exactly: QOU.QBeta.c3Of_sub_mul_u_cubed).  Two different amplifiers; conflating
them misattributes the phase's noise budget.  The cot is large for a structural
reason -- alpha_eff is small, so the ladder reads the phase through the FLAT
part of the cosine.

## Corrects my own earlier note in this bean

I recorded alpha_required as 'anchor-stable to 0.0005 %' as though that were a
structural fact.  It is not: with ~3.6 honest digits there is not enough
resolution for the two anchors to disagree, and D_eff comes out IDENTICAL at
both.  The stability is a resolution artifact, not evidence.

## Still open, unchanged

alpha is asserted in both conventions and derived in neither.  This bounds one
ROUTE (fitting the anchor); a categorical derivation is not limited by
sigma(Q_beta) and remains the open item.


## RESEARCH (2026-08-18): the corpus-grep found a constraint I did not know,
## and it exposed an ELEMENTARY error in my own earlier result

### First: the four-path corpus grep was overdue and it paid

I had been repeating 'alpha is asserted, derived nowhere' from my own earlier
session rather than from a fresh grep.  Running it found
qbeta-d-frame-eigenphase-bar-parity (2026-08-16), which I did not know about
and which changes the problem:

  * under C the eigenphase is BAR-ODD: bar(alpha) + alpha = 0
  * under D (full-bar bar(z) = z - h) it is NOT, with a Z-INDEPENDENT defect
    bar(alpha) + alpha = h^2/2 = (q-1)^2(q+1)^2/(2q^2)   [symbolic-exact]
  * so the FORCED bar-odd projection is alpha - h^2/4, taking c_3 from
    -974.43 to -86.08, recorded there as 'improves substantially but does NOT
    restore'

So alpha is not derived, but it IS structurally constrained, and one correction
is already forced rather than fitted.  I would have started cold without this.

### RETRACTION of my own claim from earlier today

qbeta_alpha_required_c_vs_d_probe reported that both conventions leave '~0.1
rad' for c_3 and concluded 'NEITHER asserted phase reproduces CODATA at N=2'.
WRONG, elementarily: cos is EVEN and mp.acos returns only the PRINCIPAL
branch, so alpha_eff_req has two solutions.  The C phase sits on the NEGATIVE
branch.

    distance to the + branch (what I reported) : 0.11321204
    distance to the - branch (the real one)    : 2.2563251e-5
    overstatement                              : 5017.54x

C DOES reproduce CODATA at N=2, to 2.26e-5 rad -- which amplified by
1/u^3 = 1.6e6 is exactly the observed c_3 = -2.069.  That consistency check
would have caught it immediately and I did not run it.

The C-vs-D RATIO (0.895) is branch-independent and stands; only the absolute
gaps and the conclusion were wrong.  The offending assertion is now recorded
as RETRACTED in the probe itself rather than deleted, and the prose is fixed.

### The actual research result

Re-expressing the ALREADY-DERIVED bar-odd projection in the amplifier-free
coordinate (justified by the proved QOU.QBeta.c3Of_sub_mul_u_cubed):

    D phase gap             0.011872906
    after alpha - h^2/4     0.00094635405
    closed                  92.03 % of the D gap
    residual                41.94x the C-frame residual

Through c_3 the projection reads as a failure (-974 -> -86, still nothing like
-2).  In phase space it recovers 92 % of the discrepancy.  ONE
structurally-forced correction -- forced by requiring the bar-oddness that
holds identically under C -- gets most of the way there.

This STRENGTHENS the D programme: the D phase is not wild, it is one derived
correction and a ~42x residual away from the frame that works.

### Discipline

Proposes NO correction and searches NO space.  The source witness explicitly
fences further correction-hunting as fitting ('does NOT license searching for
further corrections until one lands near the proved c_2 = -1'), and this
respects it -- it adds a coordinate, not a candidate.  alpha remains asserted
in both frames and derived in neither.


## 2026-08-18 — the D-frame phase anomaly is a CLOSED FORM (writhe/ribbon avenue)

Commit `0a2cf2b56`, PR #5265. Lean
`QOU/QBeta/LadderPhaseMirrorCovariance.lean` (sorry-free, 7 decls, axioms
clean, lean-direct exit 0) + probe
`computations/qbeta/qbeta_ladder_phase_mirror_covariance_probe.py` (3/3).

**Why bar-parity is the right test (this is the new part).** The Ocneanu
trace is not a link invariant alone: the two stabilisation loop values are
z and z-h, and invariance is restored by a writhe-dependent prefactor
OUTSIDE the trace (Jones 1987 §5, block
prop:jones-markov-trace-stabilisation). Writhe is mirror-ODD and that is
already proved in this corpus generically —
WritheMarkovInvariance.writhe_inv : writhe (inv a) = -writhe a — and mirror
is q -> 1/q on the Hecke side. So a framing phase MUST be bar-odd.

**The result.** For alpha = (z-1)h/2 with h bar-odd,

    bar(alpha) + alpha = h * (z - bar z) / 2     for ANY z

(phaseTwice_bar_anomaly, one ring line), hence the phase is bar-odd IFF z is
exactly bar-fixed (phaseTwice_bar_odd_iff_z_bar_fixed — an iff, so it
excludes as well as certifies). Then:

- C passes by structure: z_C bar-fixed is the corpus's own
  z_bar_invariant_field (ZBarParity, PR #3449), which the new file now
  IMPORTS rather than restates. My earlier "alpha_C is bar-odd" measurement
  was not an anchor coincidence.
- D fails with a closed form: z_D - bar(z_D) = (q^4-1)/(q(1+q^2)) = q - 1/q
  = h, EXACTLY (zD_sub_bar_eq_h). Hence bar(alpha_D)+alpha_D = h^2/2.
- So the bar-odd part is alpha_D - h^2/4, and h^2 is bar-EVEN so the same
  constant comes off both sides — the shift is UNIQUE
  (phaseTwiceD_sub_hsq_bar_odd).

**What changed.** alpha_D - h^2/4 is the projection I applied last session
on numerical grounds (it closed 92.03% of the D gap in the amplifier-free
coordinate). It is now DERIVED — the unique mirror-covariant part. Epistemic
status moved; the value did not. That is the whole difference between this
and a seventh fitted ansatz.

**Still open, unchanged.** The projected D phase leaves a residual 41.94x
the C-frame one. Untouched here. The fence from
qbeta-d-frame-eigenphase-bar-parity stands: hunting further phase
corrections is fitting until one lands with the structural standing of
c_2 = -1. cds1 is NOT closed — the ladder re-derivation under D still needs
the c_k rungs, and the Gram singularity (cds2) still blocks the H_3 route.


### Sharpened, same day (commit 78c089e1d): bar EXCHANGES the two loop values

Reading `z_D - bar(z_D) = h` with the Markov axioms (`tr(x s) = z tr(x)`,
`tr(x s^-1) = (z-h) tr(x)`) gives:

    bar(z_D) = z_D - h = the NEGATIVE-stabilisation loop value.

Under D the bar involution **exchanges the two Markov loop values** — what
mirror must do, since mirroring exchanges positive and negative crossings.
Convention C's z is bar-FIXED, i.e. mirror-BLIND, missing the exchange by
exactly h.

**I had the value judgement backwards** in the entry above: D does not
"fail" a parity test that C "passes". The h^2/2 anomaly is the signature
that D tracks the crossing-sign exchange, while the phase formula
alpha = (z-1)h/2 — written in the C frame where z is bar-fixed — was carried
over unchanged. It is the phase FORMULA that needed re-deriving under D, not
the convention. Both facts in the entry above are correct; only the reading
was wrong.

And the re-derivation is not a shift:

    alpha_D - h^2/4 = ((z_D + (z_D - h))/2 - 1) * h/2

the SAME formula at the MEAN of the two loop values — which under D equals
the bar-mean (zD_bar_mean_eq_loop_mean). Symmetrising over the mirror and
over the crossing sign are one operation in this frame; that is why no
freedom remains.

Lean §4: loopMeanTwice, phaseTwice_projected_eq_loopMean,
zD_bar_eq_negative_loop, zD_bar_mean_eq_loop_mean. Probe now 5/5.

Incidentally an argument FOR the 2026-08-15 D ruling on structural grounds,
reached independently of it. Scope unchanged — still closes nothing.

── State synthesis 2026-08-21 (session, PR #5348, branch n24484) → docs/audits/2026-08-21-cds1-d-frame-ladder-state-synthesis.md ──
NET: structurally determined, numerically fenced. BOTH legs of the D re-derivation are already FORCED + FORMALIZED symbolically (corpus-grepped, not re-derived here):
• Phase leg (forced): bar-odd projection α_D − h²/4, LadderPhaseMirrorCovariance.lean sorry-free (phaseTwiceD_sub_hsq_bar_odd; forced via zD_sub_bar_eq_h + loop-mean=bar-mean). This IS why it is not a z-swap: the formula re-derives to give −h²/4.
• Weight leg (forced, exact ℚ(q)): z_D·[2]_q=q² (zD_eq_qsq_div_bracketTwo) = Jones/two-row; S2 (#5185) solved the D weights y_(3)=(q⁴+1)/(q²+1)², y_(2,1)=q²/(q²+1)², y_(1³)=0; PSD (5,0,1). Resolves the horn in decayLadder_zC_threeRow_ne_zero: under D the decay trace IS two-row TL.
OPEN = the c_k assembly only, and it is anti-fit FENCED: forced phase closes 92.03% of the D gap, residual 41.94×C (qbeta-eigenphase-branch-and-barodd-projection.witness). Any c_k absorbing the residual is a fit until one lands with c₂=−1's standing — the same magnitude wall as C.
CORRECTION: the sensitivity-table c₃≈−974 / c₂≈−9.299 are NAIVE-Z-SWAP artifacts (C-extractor fed z_D, which S1 proves invalid). NOT proposed D values; do not wire/quote.
FORMALIZE-FIRST NEXT: state the invariant a forced D c₂ must satisfy (D analogue of c₂=−1=1−b²ℏ⁴) and check if exact weights + α_D−h²/4 determine it. Do NOT run the extractor on z_D and report the output.

── Executed 2026-08-21 (part 2, new PR): convention is localised to the N=1 phase (FORCED, sorry-free) ──
Read Q_beta_categorical factor by factor: ONLY N1_factor=cos(α−bℏ²/2) reads markovZ' (via α=(z−1)h/2). N2..N5 — carrying c₂=−1, c₃=−2, c₄, c₅ — are closed forms in q via hoefsmitB + hbarQ' ALONE (pure Kashiwara/Hopf tails b^k·ℏ^{2k}), NO z.
Formalized: QOU/BraidKnot/LadderConventionLocalisation.lean (lean-direct EXIT=0): Q_beta_categorical_eq_ofPhase (ladder = φ=α q instance of phase-parameterised family) + Q_beta_categorical_ofPhase_tail_common (two phases differ only by cos factors, ckTail common).
CONSEQUENCE: distinguishes CATEGORICAL c_k (structural, z-free — C→D moves ONLY the N=1 phase to α_D−h²/4, higher rungs unchanged) from EXTRACTED c_k (inverted from full Q_β, z-dependent). The S1 c₃≈−974 is EXACTLY the N=1 phase change mis-attributed to the higher rungs by the extractor — reconciled, not a categorical value.
SCOPE: localises z-dependence + explains the −974 artifact; does NOT claim the physical D re-derivation leaves the Kashiwara tails untouched (open). Fence unchanged: closing the 41.94×C residual by adjusting N2..N5 is a fit until a rung lands with c₂=−1's standing.

── Explored 2026-08-21: what is Lean-provable about N2..N5 (PR #5364) ──
Solved the three H₃ Markov eqns exactly over ℚ(q) at BOTH z_C and z_D (hoefsmit_b_vs_d_weights_probe.py, 7/7):
• At z_D the system FORCES y_(1³)=0 (two-row TL) + y_(2,1)ᴰ=q²/(q²+1)², and b² = 1 − y_(2,1)ᴰ = y_(3)ᴰ+y_(2,1)ᴰ EXACTLY.
• At z_C the weights are genuinely three-row (√q powers) and b² ≠ 1 − y_(2,1)ᶜ. So the identity is CONVENTION-D SPECIFIC.
⇒ The Hoefsmit coupling b that generates ALL of N2..N5 is a D-frame object (b = √(1−y_(2,1)ᴰ)) — a POSITIVE structural reason the tails are correctly D-framed, beyond 'b is z-free'.
PROVABLE (formalized, EXIT=0): hoefsmitB_sq_eq_one_sub_stdWeightD (b²=1−y_(2,1)ᴰ) + the c₂=−1 Taylor form. NOT provable-as-forced: c₃/c₄/c₅ VALUES (fitted near-matches; only the form J_Hopf·b^k is structural). The provable content of N2..N5 = the coupling identity + c₂; fence holds on the higher-rung values.

── Lean-proved the full provable D-weight structure 2026-08-21 (PR #5364, all EXIT=0) ──
Formalized S2 in Lean (turned the Python symbolic result into proved theorems) + characterized the D weights:
• dWeights_normalised (y₃+2y₂₁=1), trivWeightD_eq (y₃=1−2y₂₁)
• dWeights_markov_sigma + dWeights_markov_sigmasigma — the S2 weights SOLVE the σ and σσ Markov equations at z_D=q³/(q²+1)
• stdWeightD_eq_jones (y₂₁ᴰ=1/[2]_q²) — matches markovWeights_eq_jones_of_threeRow_eq_zero's (q+q⁻¹)²y₂₁=1
• hoefsmitB_sq_eq_trivWeightD_add_stdWeightD (b²=y₃+y₂₁), dWeights_at_one (q=1: y₂₁=¼,y₃=½,b²=¾)
Combined with the prior b²=1−y₂₁ᴰ and the existing uniqueness lemma, the D weights are now FULLY characterized in Lean.
HONEST BOUNDARY (stated in dWeights_at_one docstring): c₃=−2=J_Hopf(1) is a TOPOLOGICAL input (Jones of Hopf link), NOT derivable from these weights — no forced-c₃ lemma exists. Provable D-structure = weight/coupling algebra + c₂ Taylor form; c₃/c₄/c₅ values stay fitted.

── J_Hopf(1)=−2 now DERIVED, not asserted 2026-08-21 (PR #5364, EXIT=0) ──
Built the Hopf-link Jones value from the skein relation: JonesHopfSkein.lean (sorry-free).
jonesHopf_of_skein: over any CommRing, the cleared Jones axioms (V(unknot)=1, s·V(2-unlink)=−(s²+1), cleared skein V₊−s⁴V₋=(s³−s)V₀) FORCE V(Hopf)=−(s+s⁵) at the Hopf crossing (one linear_combination).
jonesHopf_at_one: hence V(Hopf)=−2 at s=1 (q=1).
jonesHopfClassicalLimit_eq_jonesHopfValue_one: the ladder's c₃ constant = jonesHopfValue 1 = −2 — the wired constant is now the classical-point value of the skein-derived Hopf polynomial, no longer a bare def.
This addresses the c₃-input provability gap flagged in dWeights_at_one: c₃'s value −2 is derived from the Jones skein axioms (the polynomial's DEFINITION applied to the Hopf link), conditional-class style. Still NOT derived: that −2 is the right coupling for the ladder's N3 rung (the c₃ near-match, 3.47%) — that remains the fitted step. What is now proved: −2 IS J_Hopf(1), from the axioms.


── c₂ invariant STATED and SETTLED 2026-08-22 (owner: "4 y") ──
Executes this bean's own FORMALIZE-FIRST NEXT verbatim: *"state the invariant a
forced D c₂ must satisfy … and check if exact weights + α_D−h²/4 determine it.
Do NOT run the extractor on z_D."* No extractor run; no number fitted.

ANSWER: the PHASE LEG DOES NOT ENTER, and the WEIGHT LEG DETERMINES IT WHOLLY.
`Q_beta_categorical_ofPhase_tail_common` already localises every z-dependence to
the N=1 phase, so α_D−h²/4 is irrelevant to N2_factor. The weights then force
the coupling, via a quantum-integer identity:

    y_(2,1)^D = 1/[2]_q²        stdWeightD_eq_jones          (already proved)
    b²        = 1 − y_(2,1)^D   hoefsmitB_sq_eq_one_sub…     (already proved)
    [2]_q² − [3]_q = 1          NEW
    ⇒ b²      = [3]_q/[2]_q²    NEW

So under D **the N=2 rung has no free parameter**: b is not an independent
Hoefsmit input but a function of the forced D weights. Under C the same
statement is FALSE — b² ≠ 1 − y_(2,1)^C, the C weights are genuinely three-row
(y_(1³)^C ≠ 0, half-integer powers of q) — so there the coupling is separate
data. That is a second positive structural reason the tails are D-framed,
independent of the "b is z-free" argument already recorded above.

LEAN (sorry-free, lean-direct EXIT=0, axioms [propext, Classical.choice,
Quot.sound] on all three) — QOU/BraidKnot/LadderConventionLocalisation.lean:
  bracketTwo_sq_sub_bracketThree_eq_one
  hoefsmitB_sq_eq_bracketThree_div_bracketTwo_sq
  N2_factor_eq_bracketRatio      (N2 = 1 − ([3]_q/[2]_q²)·ℏ_q⁴)

PROBE: computations/qbeta/qbeta_d_frame_c2_invariant_probe.py, 6/6 exact
symbolic ℚ(q), no float. Includes the C-side negative (assertions 4–5).

SCOPE — settles c₂ ONLY, closes nothing numerically. c₃/c₄/c₅ values stay
fitted near-matches; the 41.94×C residual is UNTOUCHED. What is removed is the
possibility that a D-frame c₂ could be *chosen*. The bean's standing fence —
any c_k absorbing the residual is a fit until one lands with c₂=−1's standing —
is unaffected, and this does not supply such a rung.

NON-OVERLAP: sibling PR #5415 works the c₃ f-map (routes A/B refuted, route C
= analytic Φ_b open). Different rung; no duplication.

── f-map 3-route attack: c₃ NOT forceable from the D trace (2026-08-21) ──
Dispatched 3 routes; all trace-weight routes fail, C (amplitude) untouched:
• Route A (bar-odd crossing): REFUTED scope-(b) — bar-odd part of D two-row trace of σ^k vanishes at q=1 (parity), target −2 is bar-even.
• Route B (Z3 carrier G·D): REFUTED scope-(b) SAME parity — every bar-even-functional × bar-odd-carrier is bar-odd → 0 at q=1.
• Redirect (bar-even channel): REFUTED scope-(a) genericity — −2 at q=1 hit by 4/4 natural bar-even combos (pins nothing); no bar-even object = full V(Hopf)(q)=−(s+s⁵) (which isn't bar-even).
UNIFIED INSIGHT: c₃=−2=J_Hopf(1) is a bar-EVEN q=1 SHADOW; no bar-odd construction reaches it, bar-even is generic. D-trace/weights cannot force c₃ in any parity.
DELIVERABLES: FMapC3ParityExclusion.lean (barOdd_at_one, barOdd_ne_hopf_value_at_one — sorry-free scope-b invariant); fmap_c3_parity_genericity_exclusion.py (19/19); audit 2026-08-21-fmap-c3-parity-genericity-exclusion.md.
OPEN: only route C (analytic Φ_b/Lawrence-Rozansky amplitude leg) — structurally different (not a parity object), the corpus's real wall; ingredients gathered (Φ_b s_n=B_2n/(2n)!, 4₁ κ-tower) but c_k-reduction not completed. That is where future f-map work goes.

── Bridge lemma 2026-08-22 (branch n24484): phase = counit-trace gap, FORMALIZED ──
phaseTwice_eq_counit_sub_trace (LadderPhaseMirrorCovariance.lean, lean-direct
EXIT=0): phaseTwice z h = evalMap h 1 - evalMap h z = eps(Delta) - tr_M(Delta),
so 2*alpha IS the counit-minus-trace gap. The 'real result' (alpha measures the
counit->trace transport generator) is now a single named cross-file theorem
bridging CrossingWeightAffine (evalMap, counit at w=1 / trace at w=z) to the
ladder phase — previously only prose + two disconnected Lean pieces (evalMap_affine
+ phaseTwice). LOCATES the unjustified step (the cosine QBetaCosResummation) as
the transport a D re-derivation must supply. SCOPE: locates, closes nothing; the
41.94xC c_k residual stays anti-fit-fenced. HONEST WALL on gap 3: both structural
legs forced+formalized, c2 settled, c3 proven un-forceable (f-map), residual
closure forbidden as fitting. No legitimate derivation move remains that isn't
already done or a forbidden fit.


## 2026-08-22 — the N=3 rung is frame-invariant, and that REMOVES its evidence (PR #5448)

Formalize-first step for N=3, per this bean's own fence. No extractor run, no c_k proposed.

**Constraint.** `decayLadder_zC_not_jones` already proves C != D for s > 1 (the Jones
pin z*[2]_q = q^2 IS z_D). The complementary half was never recorded: s = 1 IS a root
of that locus, so **C and D define the same Markov parameter at q = 1**, and by the
factorisation (s-1)(s^6+s^5+2s^4+s^3+s^2+s+1) at no other positive point.

**Prunes:** c_2 = -1 (ring identity, z-free) and c_3 = J_Hopf(q=1) = -2 (evaluated at
the one coincidence point) are UNMOVED by the ruling. The extraction, c_4, c_5 are all
at q_0 != 1 and still need re-deriving.

**This is a negative.** c_3 = -2 surviving is not evidence for it: its only support was
the 3.47% C-frame near-match, which does not transfer (under D the same value sits
~4.7e4% from re-extraction). The ruling does not refute the closed form, it removes its
support. Scope-(a). -974 stays a sensitivity measurement.

LEAN (sorry-free, lean-direct EXIT=0, axioms [propext, Classical.choice, Quot.sound] on
all six) QOU/QBeta/MarkovZClassicalCoincidence.lean: coincidenceLocus_factor (generic
CommRing), zCsub_one, zDsub_one, zCsub_eq_zDsub_one, coincidenceLocus_cofactor_pos,
zCsub_eq_zDsub_iff (SHARPER than the existing s>1 result — also rules out 0<s<1).

PROBE: computations/qbeta/qbeta_zcd_classical_coincidence_probe.py, 7/7 exact ℚ, no
float. The locus is DERIVED from the numerator of z_C - z_D, not asserted (my first
draft asserted it, with a comment misstating z_C(s^2) as s/(s^4+1); it is s/(s^2+1)).

STILL OPEN: the extraction path, c_4, c_5.


## 2026-08-22 (2) — CORRECTION to my own entry above, and the real S1 residual

Correcting the entry I wrote an hour ago. Found while corpus-grepping c_4/c_5
before working them.

**tail_common is the primary result, not my q=1 coincidence.**
QOU.BraidKnot.Q_beta_categorical_ofPhase_tail_common (already in corpus,
sorry-free) proves z reaches the ladder ONLY via the N=1 eigenphase, so the
whole N=2..5 tail is phase-blind. markovZ' is hardcoded to z_C, so alpha is the
C-frame phase and is the sole entry point.

**My c_4/c_5 claim was WRONG.** I wrote that they 'must be re-derived, being
evaluated at q_0 != 1'. They must not — they are in the phase-blind tail. The
error: reasoning about where a coefficient is EVALUATED instead of whether z
enters its rung at all.

**What my result does cover (narrower, still needed).** tail_common is about the
WRITTEN FORM; it says nothing about the PROVENANCE of the constants in it.
c_3 = J_Hopf(q=1) is a Markov trace, and a Markov trace DOES depend on z — so a
z-free written form does not establish that -2 survives. The q=1 coincidence
does. Complementary; neither subsumes the other.

**The -974 is NOT mine and is already known.** qbeta_ladder_required_phase_probe.py
already records that it is the N=1 phase residual magnified by 1/u^3 (a fixed
magnifier common to both frames), and warns it 'overstates what it measures'. I
reconstructed it independently before checking — holding the tail fixed and
pushing cos(alpha_D - u/2)/cos(alpha_C - u/2) into the N=3 rung gives -974.4319
vs the recorded -974.43, 1.9e-6 relative — and record that as a cross-check of
theirs, not as a finding.

**THE REAL S1 RESIDUAL: the tail is fine; the PHASE is the job.**
alpha = (z-1)h/2 is ASSERTED in both frames and derived in neither (a literal at
probe_q_beta_operator_valued_N3.py:70). There is no C-frame derivation to port
to D. Deriving alpha is what tranche S1 actually needs — not a tail re-derivation.

PR #5448 body + probe docstring + Lean header all corrected (commit 16847c7f5b).
Probe now 8/8 (new assertion 7: markovZ' = z_C exactly).


## 2026-08-23 (PR #5536) — branch 1 of the trichotomy is CLOSED, in every convention

Picking up from the 2026-08-22 entry above, which named the real S1 residual:
*"the tail is fine; the PHASE is the job"*, and from `EigenphaseCarrierVacuity.lean`,
which reduced "where can a derivation of `α` live" to a trichotomy:

1. `M` in the braid image — called excluded there, **by transcendence of
   `2cos((z−1)h/2)` over `ℚ(q,z)`**. That was a docstring assertion, unproved,
   and scoped to convention C.
2. `M` arbitrary — circular (`rotationOfPhase` satisfies it for any `α`).
3. `M` a holonomy of an independently-defined connection (KZ / Kohno–Drinfeld).

**Branch 1 is now PROVED, and the proof is convention-independent.**
`QOU/QBeta/BraidImageEigenphaseExclusion.lean` (sorry-free, lean-direct EXIT 0,
axioms `[propext, Classical.choice, Quot.sound]` on all seven declarations):

  `no_laurent_of_surjective_nonpos` — if `α` attains every non-positive real on
      `[1,∞)`, then `2cos(α ·)` is no Laurent polynomial `P(s)/s^N` there.
      `cos` hits `+1` at infinitely many points ⇒ `P = C 2 * X^N`; and `−1` at
      infinitely many ⇒ `P = C (−2) * X^N`; compare `coeff N`.
  `alphaC_le`   — `α_C(s) ≤ −(s−1)/4` for `s ≥ 1`  (unbounded BELOW)
  `alphaD_ge`   — `α_D(s) ≥ s−3`      for `s ≥ 3`  (unbounded ABOVE)
  `no_braid_character_C` / `_D` — branch 1 closed in both frames; D via `cos`
      evenness applied to `−α_D`.

**Why it is elementary rather than a transcendence argument.** A braid word's
character is a Laurent polynomial and `|2cos α| ≤ 2` always; a Laurent
polynomial bounded on `(0,∞)` is constant. That kills any braid-image
realisation whose phase is non-constant — and **it never reads `z`'s formula**.
So the exclusion is not a fact about C: re-picking `z` cannot repair the
D-frame ladder inside the braid picture. Scope-(b), citing a proved invariant.

Probe `computations/qbeta/qbeta_braid_image_eigenphase_exclusion_probe.py`,
12/12 exact (sympy ℚ(s) + `Fraction`; one 60-dps mpmath readout; no float64):

  det ρ(σ_i) = −1 identically in q; tr ρ(w) ∈ ℤ[q,q⁻¹] over all 1364 words of
  length ≤ 5; `1/2 − z_C = (s−1)²/(2(s²+1))`; `α_C(10) = −9009/200 < −4π`;
  `α_D(10) = 9899000001/2000200 > 4π`.

**Concrete, not merely asymptotic.** The canonical single-wrap candidate
`ρ(σ₁σ₂)` has `det = 1` and `tr = −1` **identically in q** — eigenphase `2π/3`
at every substrate value — against `2cos(α_C(q₀)) = 1.99726`,
`2cos(α_D(q₀)) = 1.99836`. A q-independent phase cannot be a ladder rung.

**Objection I raised against myself, and closed.** A *normalised* character is a
rational function, and a bounded rational function need not be constant
(`1/(1+q²)`) — an apparent escape. It is not one: `det M = 1` pins the
normalisation. For `M = c·ρ(w)`, `det M = c²·(−1)^{e(w)}`, so `det M = 1` forces
`e(w)` even and `c = ±1` (assertion 11: `−c² = 1` has no real solution). No
q-dependent normalisation survives.

**Two limits, stated so this is not over-read.** (i) It excludes a FUNCTIONAL
identification on the substrate branch, not a numerical coincidence at `q₀`.
(ii) The Laurent shape of `tr ρ(w)` is imported from Geck–Pfeiffer as the shape
of the hypothesis, checked exactly over 1364 words but not proved in Lean.

### STILL OPEN — and this is the honest state of S1

**No D-frame ladder is stated, and none is derivable from what is now known.**
`α` remains derived in neither convention. Branch 2 is circular; branch 1 is
closed; **branch 3 (KZ / Kohno–Drinfeld holonomy) is untouched and is the only
remaining place a derivation of `α` can live.** Nothing here proposes a `c_k`;
`−974` stays a sensitivity measurement and is wired nowhere.

What branch 3 would have to deliver, stated concretely so the next agent can
start cold: a connection defined **without reference to `α`**, whose monodromy
reproduces the Hecke braiding on `V_(2,1)`, and whose holonomy angle along a
specified path evaluates to `(z−1)h/2` — with `z` the D parameter. It escapes
branch 1 precisely because a holonomy is transcendental, and escapes branch 2
because the connection is prior to the phase. **Do not search for a corrective
term that lands `α_D` near the required window; that is a fit** (the required
window is ±1.09e-5 rad and `z_D` misses by 1.19e-2 rad — see the #5210 entry).


### Correction to my own entry above, same day — the closure is NARROWER than I first wrote

Devil's-advocate pass on my own result. The entry above says branch 1 is
"closed"; that is true **for the case branch 1 actually states**, and I should
have named the boundary the first time.

`EigenphaseCarrierVacuity`'s branch 1 is a **2 × 2** matrix on `V_(2,1)` with
`trace = 2cos α` and `det = 1` — a *character*. That is exactly what
`no_braid_character_C` / `_D` exclude, so the closure is real.

**But if `α` were one eigenphase among several of a LARGER braid-image matrix,
the argument does not extend.** `2cos α` is then a sum of two eigenvalues — an
**algebraic** function of `q`, root of a polynomial with Laurent coefficients,
not a Laurent polynomial itself. And boundedness does not kill algebraic: `q/(q+1)`
is bounded on `(0,∞)` and non-constant. That sub-case still needs the
transcendence argument the docstring asserted.

**Net effect on the corpus, stated precisely:** one unproved assertion becomes
*(proved half: the character case, elementary, every convention)* + *(still
assumed half: the eigenvalue-pair case, still needing transcendence)*, with the
boundary named. That is strictly better bookkeeping than before, and it is less
than "branch 1 is closed" unqualified. Recorded in the Lean header (§"Three
limits"), the probe docstring, and registry §9g.


---

## 2026-08-23 — branch 1 of the trichotomy is now closed IN FULL

Branch `claude/b3nk-decay-convention-c-excluded-2026-08-23` (PR #5544).

The 2026-08-15 pass closed branch 1 only for the **character** case and named
the boundary honestly: the **eigenvalue-pair** sub-case was left open, "still
needing the transcendence argument" (§9g "Three limits" (i)).

**It does not need one.** Boundedness was the wrong invariant to push. The
hypothesis that pass already proved — `alpha` attains EVERY non-positive real
on [1,inf) (`alphaC_surjective_nonpos` / `alphaD_neg_surjective_nonpos`) — is
far stronger than boundedness: each level set `{s : 2cos alpha(s) = c}` for
`c` in [-2,2] is INFINITE, and infinitely many solutions kill a polynomial
relation of ANY degree, Laurent or algebraic.

`QOU.QBeta.BraidImageEigenphase.coeffs_zero_of_surjective_nonpos`
(BraidImageEigenphaseAlgebraic.lean, sorry-free, axioms [propext,
Classical.choice, Quot.sound]): if `sum_{j<=d} p_j(s)*(2cos alpha s)^j = 0` on
[1,inf), then EVERY `p_j = 0`. Three applications of "a polynomial with
infinitely many roots is zero" — freeze Y at c, freeze X at x, read off
coefficients.

Covers the eigenvalue-pair case because a sum of two eigenvalues of a matrix
over QQ(s) is algebraic over QQ(s) (pairwise-sum resolvent; coefficients are
symmetric functions, so they stay in the base field) — verified exactly at 3x3
and 4x4.

**Subsumption machine-checked, not asserted:** `no_laurent_of_algebraic`
re-derives the predecessor `no_laurent_of_surjective_nonpos` as the `d = 1`
case (`p_0 = -P`, `p_1 = X^N`).

Probe `computations/qbeta/qbeta_eigenphase_algebraic_exclusion_probe.py`, 4/4,
sympy-exact over QQ(s) + mpmath 60 dps, no float64. A1 confirms the
strengthening was NECESSARY: the cited counterexample q/(q+1) really is
bounded, non-constant and algebraic, so the Laurent argument genuinely does
not extend.

## What this does NOT do — the bean stays OPEN

- Does **not** derive `alpha`, in either convention.
- Does **not** state a D-frame ladder. The re-derivation this bean is actually
  about is untouched.
- Branch (3) — a holonomy of an independently-defined KZ / Kohno-Drinfeld
  connection — is untouched, and with branch (1) now closed in full and branch
  (2) circular, it is the **ONLY** place a derivation of `alpha` can live.
  That is the next front.
- `c_3 ~ -974` remains a sensitivity measurement, wired nowhere.

Scope-(b): structural exclusion citing a proved invariant. The argument never
reads `z`'s formula, so it holds for every Markov parameter with unbounded
phase — C and D alike.

Fibre follow-on beaned 2026-08-19, corrected 2026-08-23: the D-frame
re-derivation stays blocked behind the imaginary channel, and the four blocking
issues have owners -- qou-jqjc (witness surface, FIXED), qou-ztod (the two
sorry-free zeta4 artifacts do not touch), qou-sglq (four sites assert
bar-oddness), and qou-e58e.

CORRECTION to what I first wrote here: I recorded qou-e58e as "tr_M(q0^-1) not
computable: the bar-parity blocker is TOOLING, not mathematics". THE PREMISE WAS
WRONG. tr_M(q0^-1) already computed; a stale docstring said otherwise and I
believed it without checking. There was no tooling blocker to remove. Do not
plan around that sentence.

Workplan: docs/audits/2026-08-19-frakv-fibre-workplan-options.md. cds1 itself
remains open and unclosed, and this branch does not touch it.


---

## 2026-08-23 (2) — owner reaffirmed "D is convention, excise C"; the AUTOMATED path is 0-for-2 here

Branch `claude/excise-convention-c-2026-08-23`.

Acting on the directive. Measured first, per the AGENTS note that the C surface
is UNMEASURED rather than clear.

**Current live-C surface: 32 actionable sites** (`convention-c-producer-audit.py`,
AST-verified). Of those, `convention-c-producer-migrate.py --dry-run` was willing
to rewrite exactly **2**, and **both rewrites are wrong**:

1. **`qbeta_zcd_classical_coincidence_probe.py:213` — fails LOUDLY.** Binds
   `markovZ_prime` (not C-named, so the per-site name guard missed it) purely to
   assert `markovZ_prime - z_C(q) == 0`. Rewriting took the probe from
   **8/8 exit 0** to **FAILED 1/8 exit 1**, printing the self-refuting
   `1/(sqrt q + 1/sqrt q) = q**3/(q**2 + 1) = z_C`. Class "deliberate
   comparison -> LEAVE IT": sweeping it destroys the instrument that measures
   the excision.

2. **`qbeta_h_frame_rungs_probe.py:73` — passes SILENTLY.** Binds the z feeding
   the ladder phase `alpha = (z-1)*h/2` — the one substitution
   `decayLadder_zC_threeRow_ne_zero` proves is not a migration. After the
   rewrite the probe **still exits 0 with all 3 assertions passing**, while
   silently moving **14 mathematical fields of its committed witness**:

       h^3 rung   -sqrt(3)/64      ->  1/16 - sqrt(3)/64     (SIGN CHANGE)
       h^6 rung   -6781/2949120    ->  -25381/2949120 - 25*sqrt(3)/12288

   The h^6 move is rational -> irrational, contradicting the probe's own
   headline finding ("h^3 is nonzero and purely irrational") while reporting
   success.

**Fixed.** Two file-level guards added to the migrate script, each justified by
the measurement above and regression-tested:

  G1  file references a deliberately C-named symbol -> comparison, needs a human
  G2  the target feeds `(z-1)*h/2` -> ladder phase, re-derivation required

Verified independent (S4): G1 does not catch the ladder file, G2 does not catch
the comparison file. Neither alone is sufficient. Auto-migratable set for
`computations/qbeta/` is now **0**.

Evidence + regression test:
`computations/qbeta/qbeta_convention_c_migration_safety_probe.py`, 4/4.

**Still open, and this is the bean's actual work:** the decay channel's excision
is a RE-DERIVATION of the ladder under D, not a substitution. Untouched here.

**Also open, and NOT covered by this finding:** the ~30 actionable sites OUTSIDE
the decay channel (alpha/, delta_lambda*, per_braid_tower, hydrogen_qshuffle,
q_pinning_50_digit, tools/pyhecke, qou-mass). Each needs the same three-way
triage. Two carry extra hazards already known: `q_pinning_50_digit.py:115`
writes into the ANCHOR-DEFINING witness (AGENTS rule 1 — never re-pin), and the
qou-mass `_internal/` copy is GENERATED (sync via scripts/sync-qou-mass-vendor.py,
never hand-edit).


## z_bar de-escalated (2026-08-24): it is not a choice, and the comment is a false claim under D

I had flagged `computations/convergence_safe_vhat_tower.py:198` as **needing a
bar-symmetry decision** before conversion. That escalation was **unnecessary** —
the site is mechanically determined. Recording the resolution so the next agent
does not re-escalate it.

Read in context, `z_bar` is not a free constant. The surrounding code builds the
**bar image** of V̂ by evaluating `_std_vhat` with every argument mapped under
q ↔ q⁻¹:

    _std_vhat(pg0, qi, q, z_bar, qi - q)
                   ^^^^^^  ^^^^^  ^^^^^^^
                   q<->qi         h -> -h

so `z_bar` must be **`z` evaluated at q⁻¹**, whatever `z` is. There is nothing to
decide.

Measured at the proton pin (50 dps):

| | z | z(q⁻¹) | equal? |
|---|---|---|---|
| convention C | 0.499320334183694452 | 0.499320334183694452 | **yes** |
| convention D | 0.612688037146465252 | 0.403627738350825936 | **no** |

Under D, `z(q⁻¹) = q⁻³/(q⁻²+1) = 1/(q³+q)` — verified to 18 digits against the
closed form — and `z(q⁻¹)/z = q⁻⁴` **exactly** (0.658781816976030318 both ways).

So the conversion is:

    z_bar = qi**3 / (qi**2 + 1)          # = 1/(q**3 + q)

**and the trailing comment `# = z (bar-symmetric)` MUST be deleted, not
carried.** It is true only in convention C. Left in place under D it would
assert an equality that is false by 34 %, in a file whose whole purpose is the
bar image — precisely the stale-comment failure mode this branch keeps finding
(the `borromean_per_lambda_fr_probe` "mirror of" docstring; the
`hecke_core_symbolic` `ℚ[q^{±1/2}]` notes; the `alpha_high_precision` bracket).

**Not yet converted** — the producer emits a witness, so it needs the
baseline→convert→diff treatment, and the CPU is currently saturated by the
`delta_lambda_v_hat_z_transfer_phase5d_4` measurement (job bgc281s54). Running a
second producer concurrently risks pushing that one into its 2400 s timeout and
manufacturing a spurious abort. Queued behind it.


## delta_lambda_v_hat_z_transfer_phase5d_4 — measured: the baseline exceeds 40 MINUTES

Attempted the conversion via `scripts/convention-c-convert-one.sh` with a
**2400 s (40 min) per-run** ceiling. Result:

    baseline exit=124
    !! baseline did NOT complete (exit 124; 124 = timeout).
    !! Refusing to convert ... Tree untouched.

**The guard worked**, and this is the case it was added for (a0a55a6150). Before
that guard the harness would have printed "BASELINE moved: 0" — which reads as
*stability* but actually means *the killed producer never wrote* — then
converted and diffed against a non-baseline, producing a clean-looking
single-cause attribution that was worth nothing. Tree verified untouched
afterwards.

So this site's cost is **> 40 min per run**, i.e. > 80 min for a measurement,
not the ">15 min" I had recorded. Re-launched standalone with a 3 h ceiling and
a teed log to get the true figure.

## And it violates the long-compute logging discipline

    grep -cE "print\(|log\(" -> 7      (all terminal output)
    progress / elapsed / ETA lines -> 0

AGENTS.md §5 requires any script expected to run > 5 min to emit periodic
progress lines with wall elapsed + ETA. This one runs 40+ minutes in total
silence, which is exactly why a 40-minute burn produced **zero** information
about how far through it was — I could not tell "slow but progressing" from
"hung". **Add progress logging before attempting this site again**; measuring it
blind is how the budget gets spent twice.

Incidentally, `/usr/bin/time` is **not installed** in this container — a first
re-launch using it exited 127 instantly. Use bash's `SECONDS` builtin.


### Correction to the >40 min figure

The bean records this site as "> 40 min per run", from the harness aborting at a
2400 s ceiling. **Measured longer:** the standalone baseline launched 13:31 was
still running at 14:45 — **> 74 minutes** and counting, on a 3 h ceiling. So a
full measurement is > 2.5 h, not the ~80 min implied. The producer prints
`gen 2/3/4` within its first minutes and then emits nothing for the remaining
70+, which is the AGENTS §5 logging gap doing real damage: there is no way to
distinguish "slow but progressing" from "hung" for over an hour.


## 🛑 CORRECTION: `bar(z_D) = z − h` is ALREADY IN THE CORPUS — I re-derived it, I did not find it

In `d81293cdc9` I presented `bar(z_D) = z_D − h` as something I "proved
symbolically", framing it as the discovery behind the
`derived_bond_graph_binding` fix. **It is established corpus, and in a stronger
form than mine.**

[`computations/markov_z_full_bar_condition_probe.py`](../computations/markov_z_full_bar_condition_probe.py),
on `main` since at least 2026-08-16 (`29cff89c49`):

> the bar-partner of `z` is `z - h`, and the correct covariance condition on the
> Markov parameter is `bar(z) = z - h` … **Result: convention D satisfies it;
> convention C does not** … `bar(z) = z - h` is an **identity of the whole fibre
> family**, verified for symbolic `N` (equivalently `z_N = h/(1-q^(-2N))`).

Mine was the single point `z_D = q³/(q²+1)`; theirs is the whole one-parameter
family for symbolic rank. Three further qbeta probes tabulate the same pair
(`qbeta_d_frame_eigenphase_bar_parity_probe.py:24-25` writes both branches out
explicitly as "bar-EVEN — convention C" vs "full-bar — convention D").

**What is actually mine, and survives:** the *defect* —
`derived_bond_graph_binding.py` running convention-D `z` through
convention-C bar logic — and its measurement (per-bond pp 2.0507 → 2.9242 MeV;
the corrected value landing within 0.6 % of the old self-consistent C figure
while the mixed-frame one sat 30 % away). That was unflagged and the fix stands.
I have not checked whether the pp↔nn exchange consequence is also known, so I am
not claiming it either.

**Why I missed it:** the AGENTS corpus-grep checklist reads as gating
*"is this open?"* declarations, and I was doing what felt like a derivation, so
I never ran it. That is the wrong reading — a derivation presented as new is a
claim about corpus status just as much as "X is open" is. One
`grep -rn "bar(z)" computations/` would have found it in seconds.

Found only because I later scanned for the *bug shape* (asserts z bar-symmetry
AND already carries a D expression) and four of the six hits turned out to be
files documenting the identity correctly. The scan I wrote to find more bugs
found my own over-claim instead.


### Self-audit of my other claims on this branch (same discipline, applied to myself)

Having found that `bar(z_D) = z − h` was established corpus, I greped my two
remaining structural claims. Result: **no prior statement, but neither is
independent** — both are one-step corollaries of that established identity, so
"absent from the corpus" here probably means "nobody bothered writing it down",
not "new insight".

**1. `z_D/(z_D − h) = q⁴`.** Searched `computations/`, `docs/`, `content/` and
the Lean tree for `q^4` / `q**4` / `q^{-4}` / "fourth power" near z, markov or
bar. Only my own two commits. The other hits are `ℏ_q**4` — a **different
quantity**, ℏ_q not q — and `q-beta-bar-even-kernel-invariant.lean:100-102`,
which is about a Q_β correction being bar-even iff `q⁴ = 1`: adjacent territory,
different statement.

But given `bar(z) = z − h` (corpus) it is immediate: `z/(z−h) = z/bar(z)`, and
`bar(z_D) = q⁻⁴·z_D`, so the ratio is `q⁴` in one line.

**2. pp↔nn exchange under bar.** Only my own commits; the other "exchange" hits
are the Slater antisymmetrizer / exchange-determinant family, unrelated. Also
immediate from the same identity: `f_pp = z`, `f_nn = z − h = bar(z)`, so bar
swaps them by inspection.

**Net:** one retracted novelty claim (`bar(z_D) = z − h`), two corollaries that
are unstated in the corpus but follow in one step from it. The load-bearing
contribution of that commit remains the *defect* in
`derived_bond_graph_binding.py` and its measurement, not the mathematics.


## Re-audit of the "0 fields moved" verdicts — 1 frozen, 3 genuinely safe

`compound_shift_nf` showed **0 fields moved** under the `hecke_core_symbolic`
conversion and I read that as convention-INDEPENDENT. It was convention-FROZEN
(transcribed constants, fixed in `35930672e3`). Since that inference was
backwards once, I re-checked the other three zero-movement importers from
`a24fdac8a1`:

| importer | why it did not move | verdict |
|---|---|---|
| `crystal_shift_nf_atomic` | **0** z references at all | genuinely independent |
| `canonical_ordering_dof_probe` | `z = markov_z(q)` — the canonical helper, already D | independent **of my change** |
| `hecke_channel_binding_probe` | `from closed_form_tau_M import markov_z`, `z = markov_z(Q0)` | independent **of my change** |
| `compound_shift_nf` | transcribed integers, cannot move | **FROZEN — was the defect** |

So one in four. The other three are safe for two different reasons, and the
distinction matters: `crystal_shift_nf_atomic` does not use z; the other two use
it but obtain it from a **canonical helper** that is already convention D, so
migrating `hecke_core_symbolic` correctly leaves them alone.

## The structural remedy is already in the corpus, and it is better than mine

`hecke_channel_binding_probe.py:61-68` carries a prior agent's rationale:

> Convention D via the canonical helper. This was `mp.sqrt(Q0)/(Q0+1)` —
> convention C, excised by the 2026-08-09 ruling. Note the witness
> `_provenance` already CLAIMED `z=q^3/(q^2+1)`, so the file **documented D
> while computing C**. Calling `markov_z` rather than re-spelling z inline is
> deliberate: **every convention detector keys on how z is WRITTEN, and an
> inline spelling is how a site goes blind** (this one was missed by two
> independent detectors).

That is the same "documents D, computes C" defect I found in
`derived_bond_graph_binding`, hit earlier by someone else, and their fix is
structural where mine was local: **route through `markov_z(q)` so there is no
spelling for a detector to miss.**

Worth adopting as the campaign's end state. Every detector on this branch —
mine, the sibling's witness-layer one, the value-literal one — exists only
because z is re-spelled at each site. A site that calls the helper needs no
detector at all. Converting an inline spelling to `markov_z(q)` is strictly
better than converting it to a D spelling, and costs the same edit.


## Independent numerical confirmation that convention D is FORCED, not stipulated

`closed_form_tau_M.markov_z`'s docstring asserts the selection is forced: the
row cap `ell(λ) ≤ 2` gives `y_(1³) = 0`, and given that,
`markovWeights_eq_jones_of_threeRow_eq_zero` (sorry-free) makes the faithful
normalised Markov trace unique and equal to `q³/(q²+1)`.

Checked it numerically rather than taking it on the docstring's word, by
solving the three H_3(q) normalised-trace equations at both conventions
(`ocneanu_param_from_fibre_dimension.markov_weights(q, z)`, which is
parameterised by z so both frames go through one code path):

    q0 = 1.109978582751381

    convention C   z = 0.49932033418369
        y_(3)   = 0.4153957953606134
        y_(2,1) = 0.2809296310310197
        y_(1^3) = 0.02274494257734718      <-- NONZERO
        sum = 1.0

    convention D   z = 0.61268803714647
        y_(3)   = 0.5054042265039308
        y_(2,1) = 0.2472978867480346
        y_(1^3) = 0.0                      <-- EXACTLY ZERO
        sum = 1.0

So D is not a preference among conventions: it is the **unique** z at which the
three-row weight vanishes, and C fails that condition by 0.0227. The Lean
theorem and the owner ruling agree with the arithmetic.

Worth having explicitly, because most of this branch's work is mechanical
excision and it is easy to lose sight of *why* D is canonical. It is not
"because the ruling says so" — the ruling follows the mathematics.

## What this did NOT settle: `TRM_L6A4 = 0.998367` (qou-5pgl)

None of the six weights above is `0.998367`, so that constant is **not** a
`y_λ`. It is a *trace value* — the `_deprecated` tables list it as the λ=[3]
entry for p / n / ³He, one of them annotated *"(registry; convention TBD)"*.
Weights and traces are different objects and I should not have implied the
weight solve would answer it.

`qou-5pgl`'s question therefore stands open: is `0.998367` convention-C, and
what is its D value? That needs the trace machinery, not the weight solve.
Recording the negative so the next attempt does not repeat this route.


## 2026-08-25 — the two qbeta C sites in the probe drain: one LEFT, one KEPT

The probe/derived-tower convention-C drain (PR #5739) was assigned both live
qbeta C sites. **Neither was migrated**, and the two reasons are different.

### `computations/qbeta/qbeta_h_frame_rungs_probe.py:73` — LEFT, because this bean owns it

    z = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))      # z_C
    alpha = (z - 1) * hh / 2

That `alpha` is the **C-frame eigenphase**, and per
`qbeta_zcd_classical_coincidence_probe` assertion 7 the ladder's `markovZ'` is
hard-coded to z_C, so the phase is exactly where the convention enters the
ladder. Substituting z_D into it is the banned "substitute into a derived
conclusion" move — and AGENTS.md is explicit that the ladder "must be
RE-DERIVED under D, and that is not a z-swap", with
`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free) making the C-frame
ladder and the mass channel's three-row forcing mutually exclusive.

So the site is a **real C defect that cannot be fixed by the drain**; it closes
when this bean's re-derivation lands, not before. Flagging it here so the
re-derivation knows to update this probe's z and alpha together rather than
leaving a C binding behind in a file that will then look migrated.

Note the probe's own docstring already says it establishes "nothing physical"
and that alpha is "un-derived in both frames", so nothing downstream is
asserting a D-frame result off it today.

### `computations/qbeta/qbeta_zcd_classical_coincidence_probe.py:213` — KEPT, deliberate comparison

    markovZ_prime = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))

This is assertion 7 of a probe whose entire subject is C-vs-D. The line exists
to RECORD that the ladder's markovZ' equals z_C; migrating it would destroy the
probe's own finding. Correctly left, and it should stay through the
re-derivation too — it is the record of what the C frame was.

The drain's audit lists both as actionable because the detector cannot tell a
comparison from a defect; only the second is a false positive.


### Addendum 2026-08-25 — basis for both qbeta dispositions, given qou-4bq3

`qou-4bq3` has shown the audit's `deliberate` column is unreliable. Neither
qbeta disposition above used it.

**`qbeta_zcd_classical_coincidence_probe.py`** was left because of what the code
says: it defines `def z_C(qq)` (`sqrt(qq)/(qq+1)`, line 113) directly beside
`def z_D(qq)` (`qq**3/(qq**2+1)`, line 117), each with a docstring naming its
convention, and assertion 7 exists precisely to record that the ladder's
`markovZ'` equals `z_C`. Prose naming C and D and explaining why both are
present — the standard `qou-4bq3` sets.

Note line 113 is itself an instance of the detector-blind `sqrt(q)/(q+1)`
spelling catalogued in `qou-l7j1`, benign here.

**`qbeta_h_frame_rungs_probe.py:73`** was never called deliberate. It is a real
C defect, deferred to this bean's re-derivation because swapping it is the
banned substitution — a different disposition from "leave it, it is fine".

> **Cross-reference to the section above (added on resolving the rebase conflict).**
> `main`'s *"the two qbeta C sites in the probe drain"* entry covers
> `qbeta_h_frame_rungs_probe.py:73`, which is **one of the 13 sites** the AST pass
> below flags, and reaches the same verdict independently: a real C defect the
> drain cannot fix, closing only when this bean's re-derivation lands. The two
> records are complementary — that one covers producers *still on C*, this one
> covers producers *already moved to D with a C witness and a C gate*.
---

## A sub-class the "Live C sites" list does not cover (2026-08-25, bean `qou-uz7q`)

That list tracks producers **still computing in C**. There is a second, opposite
failure mode, and it is worse because it is invisible:

> **already swapped to D, with the witness AND the gate threshold left at C.**

Such a producer computes D numbers, compares them to a C answer, and **fails its
own gate** — while the corpus reads it as passing, because the committed witness
still says `allPassed: true`.

### Measured instance: `qbeta_c3even_exact_sseries_probe`

`70d1ade383` ("excise C tiers 2+3: 176 producer sites to convention D") swapped
this probe's `z` on 2026-08-09 and did not regenerate its witness. Re-running it
today flips `allPassed` `true` → `false`.

Attribution by decisive test — numeric Taylor of `log(R(1+s)/R(1))` with the
**live `cos`**, mpmath 60 dps, under each `z`:

| probe source | `[s^3]` | matches |
|---|---|---|
| **D** — today's `z = q**3/(q**2+1)` | −4.4084936490538903383 | the re-run, `\|diff\| = 0.0` |
| **C** — witness-era `z = 1/(sqrt(q)+1/sqrt(q))` | −3.9084936490538903383 | the committed, `\|diff\| = 3.1e-61` |

The gate threshold confirms it independently: `c_2^even ≈ −8.006` **is** the C
value — the committed C witness carries `−8.00641005870925` exactly. A correctly
migrated D producer *must* fail a C-calibrated gate.

This is candidate **33** of `convention-frame-staleness-audit` (73 suspects over
139 D-form producers), promoted **suspect → confirmed** by that audit's own
decisive-test method.

### 🛑 Do NOT connect these numbers to (H1) — normalisation unestablished

The probe reports `c3_even` **+86.66 (C) → +78.59 (D)**, a 9.3 % move. It is
tempting to read that against this bean's table (`c₃`: −2.069 → −974.43, a 500×
move) or against (H1) `c₃^even = −Vol(4₁) ≈ −2.03`. **Do not.** Those are three
different objects, and `+86.66` cannot be the same normalisation as `−2.03`.
Nothing here establishes which normalisation the probe's `c3_even` is in, so
nothing here bears on (H1) either way. Recorded because AGENTS.md names *"a
quantity differing only by normalisation, mistaken for a discrepancy"* as the
exact error class this section could otherwise commit.

### The D numbers were NOT landed

Per this bean's own load-bearing constraint — `decayLadder_zC_threeRow_ne_zero`,
so the C→D move **is not a z-swap** — `70d1ade383` performed exactly that
substitution on this probe. Its D output is correct arithmetic from a move the
ruling names invalid. The committed C witness was **restored**; nothing landed.
The re-derivation this bean owns is what would produce a landable number.

### What is now unblocked

Both exact-`s`-series probes were **TIMEOUT / UNMEASURED** (> 1800 s censored),
so no D-frame number could be obtained from them at all. Profiling showed the
cost was `sympy`'s `trigsimp` → `polys.factor` fired by a live `cos` node inside
`sp.series` — **3 `factor()` calls = 97.8 % of a 1200 s run** — not the probe's
own `simplify`. Expanding `cos(alpha_eff)` to a finite Taylor polynomial first
(exact: `alpha_eff(q=1) = 0`) gives **370 s at the probe's own order 9**, against
a live-`cos` route that cannot finish **order 3** in 420 s.

So the re-derivation now has a working experimental instrument on this axis where
it previously had none. Validated value-neutral twice: the residual against the
live-`cos` function falls at `s^N` (9.002 decades/decade at N=9), and the numeric
Taylor above reproduces the D value the fixed probe emits.

**Still not started, and still needs the owner's go:** the actual D-frame
re-derivation. Nothing above is a re-derivation — it is one confirmed staleness
instance plus a faster instrument.
---

## 2026-08-25 — S1 attempt (PR #5748). Does NOT close; block located.

Scope-(a). Nothing wired; no c_k value, tier or channel registration moved.

**Correction to this bean's own framing.** `decayLadder_zC_threeRow_ne_zero`
does not forbid the z-substitution. It is about z_C ONLY: at the C parameter
the third Wedderburn row is forcibly present, so "keep the C ladder" and "the
two-row forcing applies here" are incompatible. The theorem that blocks the
SUBSTITUTION is `eigenphase_bar_defect_of_fullBar` (same file): feeding a
full-bar parameter into the C eigenphase leaves a bar defect of exactly h²,
z-independently. Two different blocks, both needed.

**What parity derives.** For a general shift c = ce + co,
`generalShift_bar_defect` gives defect h·(h + 2·co) — ce and z both absent.
So bar-oddness forces co = −h/2 UNIQUELY and constrains ce NOT AT ALL. The
canonical member is z_D^even = z_D − h/2 = (q⁴+1)/(2q(q²+1)), which is
[2]_q·Ξ/2 — the weight-determined half of the Markov parameter — so this is a
re-derivation, not a substitution. Does not contradict
`no_weight_function_gives_phase`, which excludes the weights fixing the FULL α.

**Measured (proton; muon agrees). Harness reproduces C's −2.06934258 and this
bean's −974.43 before being trusted.**

  candidate            implied c₂    c₃       |r₂/r₁|
  C as recorded          −1.0176   −2.0693     0.017
  D naive z-swap         −9.2989 −974.43       0.893
  D bar-odd, derived     −1.7331  −86.081      0.423

11× better than the banned swap, still not the c₂ = −1 band.

**Three no-fit measurements.**
* Window: landing in |c₂+1| ≤ 0.02 demands the eigenphase to 4.5e-4 relative.
  C and derived-D differ by 36 window-widths; naive by 463.
* The cross-anchor swing — this bean's f-map discriminator — is
  phase-independent to 0.5% (1.0052 naive, 1.00026 derived). It carries almost
  no convention information.
* The data demand z* = 0.4991045: 0.043% from z_C, 1.81% from z_D^even, 22.8%
  from z_D. The ladder's empirical content IS "z ≈ z_C", which is why C looked
  derived — and is why the re-derivation must change the SHAPE, not just z.

**Where it blocks / what unblocks it.** ce = z* − z_D^even = −0.0090534 is
bar-even, hence NOT excluded by parity. Deriving ce from convention-D data is
the open item. Two guards for whoever tries:
* ce ≈ −u (6.3% away) is INADMISSIBLE: bar(u)/u = q², u is not bar-even. h² is.
* ce is resolved to only 1.45% (68.8σ) by σ(Q_β)/Q_β = 7.8e-7. ce/h² =
  −0.207142 sits 1.7e-4 from (√2−1)/2 — 84× below resolution. Any
  identification quoted to better than 1.5% is arithmetic, not measurement.

Artifacts: `computations/qbeta/qbeta_d_frame_eigenphase_window_probe.py`;
`QOU/QBeta/DFrameEigenphaseBarOdd.lean` (9 theorems, sorry-free, axioms clean);
`docs/audits/2026-08-25-qbeta-ck-ladder-convention-d-eigenphase-window.md`.


---

### Adjudication, 2026-08-25: `qbeta_h_frame_rungs_probe.py:73` — the sibling is RIGHT, I was wrong

Recorded because two records in this bean disagreed and the merge coordinator
declined to adjudicate. Adjudicating my own side against it: **the sibling's
"this bean owns it" is correct, and my contrary claim is retracted.**

I reported that file as "a frame-change probe that disclaims carrying physics",
and named only `qbeta_utils.py::substrate_ladder_quantities` and
`markov_parameter` as the live C eigenphase sites. Read at the body:

    73:    z = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
    74:    alpha = (z - 1) * hh / 2

That is an independent inline C spelling of the ladder eigenphase — a third
genuine site, not a consumer of the other two, and squarely a B2-class site:
swapping z there is exactly the substitution `naivePhase_not_barOdd` shows is
never bar-odd.

**How I got it wrong, since the mode recurs.** I read the docstring's "WHAT THIS
DOES NOT ESTABLISH. Nothing physical." and stopped. That disclaimer is about the
probe's *conclusion* — it is a change of variable — not about what the file
*contains*. AGENTS.md's own instruction covers this exactly ("Read at the body
rather than the docstring"), and it is the same failure the `y_lambda_at`
correction documents one section over. A docstring saying a file establishes
nothing physical is not evidence about which convention its arithmetic carries.

My "two live sites" count is therefore also retracted as incomplete. It should
not be used as a denominator anywhere.


## The F coordinate does NOT rescue it — the crossing pathology survives the change of coordinate (2026-08-25)

Angle taken from this bean's own closing recommendation (*"work in F, not alpha"*).
Distinct from PR #5337, which is on the two-row cap.

`qbeta_F_coordinate_bridge_audit_probe.py` was committed (#5745) but **its
witness never was** — the producer declares `WitnessBuilder('qbeta-F-coordinate-
bridge-audit')` and no such file is in the tree. Ran it; 3 assertions pass.

**The result the bean was hoping against.** The move to F was motivated by the
alpha coordinate's sqrt branch point being a parameterization artifact — which
it is. But F does not restore tracking:

    dF_required/dq  =  +2.3355460960     <- POSITIVE
    bridge_truncated_C   -0.4548          bridge_truncated_D   -0.2414
    bridge_exact_C       -0.5061          bridge_exact_D       -0.2887
    cos_model_C          -0.0321          cos_model_D          -0.0163

All six candidates have the WRONG SIGN. Independently verified here from the
closed form `Q_A = m_e|q^2-2q-1|(q+1)/(2q^3)` by central difference:
+2.3355460958, matching the probe to 1.8e-10 (differentiation error).

So the prune extends: it is not merely that no analytic phase ansatz can equal
alpha_required as a function. In the SMOOTH coordinate, where no branch point
exists to blame, every candidate still only CROSSES F_required — and does so
transversally from the opposite direction. Changing coordinate removed the
artifact and left the disagreement intact, which localises the failure in the
candidates rather than in the parameterization.

**Also measured, and it bears on the C-vs-D question directly:** the cos model's
relative error against F_required is 1.28e-6 under C and 6.02e-4 under D — D is
471x worse in the coordinate the bean nominated as the honest one.

Scope-(a). Nothing here derives F, and no value is proposed for anything.

## 2026-08-26 — the D-frame TRACE baseline, computed not substituted

Probe: computations/qbeta/qbeta_d_frame_trace_baseline_probe.py (4/4).

NOT a z-swap. The ladder's formula is untouched. The D-frame object is built
from its defining structural property instead -- under D the decay trace kills
the third row and factors through Temperley-Lieb -- and
`y_lambda_su_n(3, q, N=2)` IS that structure: a three-row partition has
vanishing Schur function at N = 2, so y_(1^3) = 0 FALLS OUT rather than being
imposed. Machine-checked.

Trace taken on the EXHIBITED nucleon words, per block:

    chi_(3)      = -0.26038764179012
    chi_(2,1)    = -0.10681445765158
    chi_(1,1,1)  = -0.17153864377660

    two-row (D)   tr_M(Delta) = -0.15801600434149   Q_beta = 0.661452  -15.451 %
    three-row     tr_M(Delta) = -0.13591200273905   Q_beta = 0.568925  -27.278 %
    counit        (coordinate sum)                  Q_A    = 0.783646  +0.1678 %

WHAT THIS FORECLOSES, and it is the useful part. Every rung of the published
ladder is a sub-percent correction; the whole five-rung product moves Q_A by
0.168 %. The D-frame trace baseline is off by 15.451 % -- **92.1x the entire
existing ladder**. So re-deriving the ladder ON THE MARKOV TRACE cannot rescue
Q_beta under D: no product of rungs that size closes a gap that large.

SCOPE -- (a), NOT (b). This is "this construction, alone, does not reproduce
the numbers as-is". It does NOT exclude the trace as an ingredient and does NOT
prove Q_beta is not a trace observable. It excludes the specific hope that a
D-frame re-derivation of the EXISTING rung structure lands on CODATA, and
prices how far off that hope is.

CONSEQUENCE FOR THE RE-DERIVATION. The two live routes are now:
 (i) the counit/coordinate-sum route survives into D -- but the coordinate sum
     is not an algebra map (QOU.QBeta.CounitSigmaOne.h_eq_zero_of_image_one)
     and would need its own D-frame justification, which nothing supplies; or
 (ii) Q_beta is not a trace observable at all, and step 8 of the 2026-05-24
     fitting-finding audit (Q_beta = |Delta(net)|*E_0, POSTULATED) is where the
     re-derivation actually has to happen.

Either way the work is at step 6/8, not in the rungs.


## 2026-08-26 — RETRACTION of the foreclosure reading, and step 8

**Owner correction (verbatim):** *"Every driving ladder doesn't fully close the
gap if it is the proper thing to do, it should be done as once the other parts
of the gap are closed it will improve the accuracy"* / *"Even if derriving the
ladder..."*

That names an inversion of AGENTS.md's own rule. My D-frame trace baseline
(`qbeta_d_frame_trace_baseline_probe.py`, 4/4) measured the two-row (D)
`tr_M(Δ) = −0.158016004341` → `Q_β = 0.661452 MeV`, −15.451 %, against a
five-rung ladder that moves `Q_A` by 0.168 % — a 92.106× gap. I then read that
as foreclosing the D-frame ladder re-derivation. Wrong: the two permanence
principles under *"Before declaring refuted"* say a structurally-exact piece is
a permanent, correct contribution **even while the total is inaccurate**, and
that *"inaccurate alone" ≠ "excluded"*. Measuring how far a term falls short is
not an argument against deriving it correctly.

Fixed in `0da1e06c4`: docstring re-scoped, title line no longer says
"forecloses", measurement untouched. **`qou-cds1` stays open and the D-frame
re-derivation is still to be done.** What the measurement supplies is an
expectation set on it, not a verdict on whether to run it.

## Step 8, and why it interlocks with this bean

`qbeta_net_trace_invariance_probe.py` (25/25, `428488665`) attacks step 8 of the
2026-05-24 fitting-finding audit — the chain's one postulate, `Q_β =
|Δ(net)|·𝔈₀` *"by construction"*.

- **`net` is NOT a trace.** 8 of 36 ordered basis pairs fail cyclicity in the
  6-dim regular rep of `H_3(q)`; both controls (augmentation, regular
  character) pass on all 36. So the corpus's stated licence — that `ε(Δ)` is a
  *"counit (transition) observable"* — is unavailable: an algebra map into a
  commutative ring is automatically cyclic, so a counit **is** a class function.
- **The split.** `H = Z(H) ⊕ [H,H]`, dim 3 + 3 (measured). At q₀:
  `epsNPq = −0.187207194529378` = central `−0.172847658641848` (92.33 %) +
  commutator `−0.014359535887530` (**7.67 %**). That 7.67 % is invisible to the
  Markov trace, the augmentation, every `χ^λ`, and every combination.
- **The derivable piece** — the constructive half, and the one that matters for
  this bean. The unique trace agreeing with `net` on the centre is exhibited:
  `a_(3) = (q+1)/((q²+1)(q²−q+1))`, `a_(2,1) = q(q²−1)/(q⁴+q²+1)`,
  `a_(1³) = q³(q−1)/((q²+1)(q²+q+1))`. Verified to reproduce `net` on the whole
  centre, annihilate `[H,H]`, and give exactly the central part on Δ.
  **`a_(1³) ≠ 0`**, so it is not a two-row Markov trace of the shape convention
  D forces at N=2 — which is a live datum for the re-derivation, not a block on
  it.
- **Presentation dependence.** Conjugating both nucleon words by one basis
  element (a Markov-I move) moves `Q_β` over 0.692169 … 0.783646 MeV, a 0.0915
  MeV spread ≈ 70× the +0.168 % residual. Exactly two values, because
  conjugation by `w₀` is the diagram automorphism `s₀↔s₁` and permutes the
  standard basis.

Step 8's postulate is now narrowed from the whole of `net` to the 7.67 %
remainder. Scope-(a) throughout.


## 2026-08-26 (2) — the re-derivation advances: block resolution, a z-free floor, and the quotient reading

Three probes, 57 assertions, all exact-symbolic. Owner directed this bean as
first priority after correcting my foreclosure reading (section above).

### 1. The phase has a z-FREE commutator floor, and it is bar-even

`qbeta_alpha_commutator_floor_probe.py` (22/22). Combining this bean's identity
`ε(Δ) − tr_M^z(Δ) = h(z−1) = 2α` with step 8's split `H = Z(H) ⊕ [H,H]`:

    2α = [ net(dZ) − tr_M^z(dZ) ] + net(dC),    net(dC) = −(q²−1)²/(q⁴+q²+1)

The floor contains **no Markov parameter**: identical in C and D to 50 digits
(`−0.01435953588753045`), carrying **13.72 %** of 2α in C and **17.73 %** in D.
Not a rounding term.

**It extends the sibling prune.** `fcffeee29` reads: both surviving D weights
are bar-even ⇒ no bar-odd part can be assembled from the D-frame **weights** at
all. The floor is not built from weights — it is a non-trace functional on the
component every weight annihilates — so that prune does not reach it. Measured:
**the floor is bar-EVEN**, exactly. The trace-invisible sector supplies no
bar-odd material either. Gap closed in an existing exclusion, proved not searched.

**Fourth independent route to the D weights**, from the Ocneanu recursion
(`tr(1)=1, tr(T_i)=z, tr(T_0T_1)=z², tr(T_0T_1T_0)=z(hz+1)`) solved symbolically
in `z`: recovers `y_(1³)=0`, `y_(3)=(q⁴+1)/(q²+1)²`, `y_(2,1)=q²/(q²+1)²`,
cross-checked against `y_lambda_su_n`.

### 2. The functional form this bean has been asking for

`qbeta_phase_block_resolution_probe.py` (18/18). Exactly, for every `z`:

    2α(z) = Σ_λ [ a_λ − y_λ(z) ] · χ^λ(Δ) + net(dC)

with `a_λ`, `χ^λ(Δ)` and `net(dC)` **all z-free** — the convention enters at
**one factor**. That is why it is a re-derivation: the C-frame scalar `(z−1)h/2`
is the *sum* of the blocks, and the sum is resolved into parts **before** a
convention is chosen, so specialising to `z_D` is a statement about the D-frame
representation rather than a reuse of the C formula.

Three structural facts:
- **`χ^(2,1)(Δ) = 0` identically** — dim 2 at the identity, trace `h` at each
  generator: `(h²/2)·2 − (h/2)h − (h/2)h = 0`. The phase is blind to the
  2-dimensional block, in **every** convention.
- With that, under D the two-row forcing leaves `tr_M(Δ)` carried **entirely by
  the trivial block**.
- The `(1³)` block contributes `a_(1³)·χ^(1³)(Δ)` **uncancelled** under D, with
  no counterpart in C: `−0.000543 → +0.004238`, sign flip and 7.8×.

*A prediction of mine failed and is retained, not deleted:* I asserted all three
`a_λ` were bar-"neither"; `a_(2,1)` is exactly bar-**odd**. It is the block χ
kills, so it costs nothing — but the guess lost to the measurement again.

### 3. The two-row forcing read as a QUOTIENT — 18× on the D phase

`qbeta_d_frame_tl_quotient_phase_probe.py` (17/17). The identity above is exact,
so it moves no number; a re-derivation needs a changed **input**. There is one
the D convention touches that C does not, and it is not `z`:
`WenzlWeightVanishing` proves `z_D` is Wenzl level `r = 2` exactly.

Read that as a **quotient** — evaluate in `H_3(q)/J_(1³)`. The central idempotent
is unique ⇒ `π(Δ)` is one determined element, **no free parameter**. It bites
because projection is invisible to the D trace (`y_(1³)` already annihilated that
block, so `tr_M^D(πΔ) = tr_M^D(Δ)` exactly) and **visible to `net`**, which is
not a trace and does not respect the block ideal.

| candidate | \|Δz\|/z* |
|---|---|
| C (as recorded) | 0.00043244 |
| D naive z-swap (banned) | 0.22757466 |
| D TL-quotient | 0.18695789 |
| D naive + bar-odd | 0.01813926 |
| **D TL-quotient + bar-odd** | **0.01268105** |

**Calibrated before being trusted:** this bean records z* as "0.043% from z_C,
1.81% from z_D^even, 22.8% from z_D"; the harness returns 0.0432% / 1.8139% /
22.757%, the middle being an independent reproduction of the recorded
`z_D^even` candidate reached by projecting the *phase* onto its bar-odd part
instead of deriving `z_D^even = z_D − h/2`. The bar-odd projection's licence is
a control: under C it acts as the **identity** (asserted).

### Scope — this does NOT close the bean

Best D is still **29.3×** the C distance. `z*` is anchor-inverted, not derived.
The quotient reading is an **interpretive** step: the corpus establishes the
two-row forcing for the trace's *support*, not for the *element*. Both
corrections are reported separately so each marginal contribution is visible,
and nothing is wired. Scope-(a) on two named readings.

**Next, concrete:** decide the quotient reading on its merits rather than by its
number — does the D-frame decay channel live in `H_3(q)` or in its TL quotient?
That is a corpus/owner question, and it is now worth 1.43× on the best D
candidate.


## 2026-08-26 (3) — `net` = tr_M at z=1, corrected on ONE element; and the floor IS the 2-dim block

`qbeta_net_as_trace_plus_longest_probe.py` (13/13). Sharpens two corpus
assertions and closes the loop between the last two entries.

`qbeta-counit-closed-form.md` says *"the counit and the Markov trace are
genuinely distinct functionals on the substrate"* and *"the two agree precisely
when z = 1"*. Both true, both vaguer than the situation. Measured exactly, on
all six basis elements:

    net  =  tr_M^{z=1}  −  h · (coefficient of the longest element w₀)

The Ocneanu trace at z=1 sends every basis element to 1 **except** the longest,
where `tr(T₀T₁T₀) = z(hz+1) → 1+h`; `net` sends every basis element to 1 by
definition. **A single rank-one difference, supported on w₀.**

### Three consequences

1. **"They agree precisely when z=1" is about Δ's SUPPORT, not the
   functionals.** Δ has zero w₀ coordinate, so `ε(Δ) = tr_M^{z=1}(Δ)` follows
   structurally rather than numerically. On `T_{w₀}` the two differ by `h` at
   **every** z, z=1 included.

2. **The phase is a transport WITHIN one family**, not between two unrelated
   functionals: `2α(z) = tr_M^{1}(Δ) − tr_M^{z}(Δ)`, symbolic in z. The
   counit-minus-trace framing recorded above is right and understates it — the
   endpoint is the same Ocneanu trace at the trivial loop value. That is what
   the (axiomatised) cosine exponentiates.

3. **The 2-dimensional block carries the entire z-free floor.** `tr_M^{z=1}` is
   a trace, so it annihilates `[H,H]` and only the rank-one term survives:

       net(dC) = −h·(dC)_{w₀}   and   (dC)_{w₀} = a_(2,1) = q(q²−1)/(q⁴+q²+1)
       ⇒  net(dC) = −h·a_(2,1)                                        [exact]

   Read against the block resolution, which gave `χ^(2,1)(Δ) = 0` identically:
   **the 2-dimensional block contributes nothing to the trace-visible part of
   the phase and everything to the trace-invisible part.** Its contribution was
   never absent — it was in the sector no trace can see.

Also pinned: the longest-coefficient functional is not cyclic, which is exactly
why `net` fails cyclicity (step 8's 8-of-36).

Convention-free: every result holds for all z, and the floor contains no Markov
parameter. Scope-(a): derives no correction, proposes no value, wires nothing.

## Lean landed alongside (sorry-free)

`QOU/QBeta/PhaseBlockResolution.lean`, generic `[CommRing R]` per §7c, `lean`-
direct exit 0 with no warnings, `#print axioms` → `[propext, Classical.choice,
Quot.sound]` on all four declarations, 0 `sorry`. Tree is a RESTORED olean cache
(6990 oleans / 0 traces, marker present) so **no `lake build` was run**.

- `chi_two_one_delta_eq_zero` — the (2,1) character annihilates Δ, from the
  block's dimension and generator trace alone; the character's values on the
  three longer basis elements are left free in the statement.
- `floor_bar_even` — division-free, bar involution carried by `u·v = 1`.
- `floor_bar_defect` — committed **so the first is not mistaken for a `ring`
  tautology**: off the bar locus the two sides differ by `3(u²−v²)((uv)²−1)`.
- `floor_bar_even_units` — the `q : Rˣ` restatement.

## Where the bean stands

Still open. Best D candidate is 29.3× the C distance, and the bean's own
discipline forbids hunting further corrections until one lands near the proved
`c₂ = −1`. What this tranche adds is structure rather than a number: the phase's
z-free part is now a closed form tied to a named block, the transport is
identified as motion along the Markov line, and the two pieces that are ring
identities are machine-checked.


### Closed form of the floor, inside the Ocneanu family alone

Follow-through, same probe (now 20/20). Everything in the block-resolved
identity except the `a_λ` came from the Ocneanu trace; the `a_λ` were *solved
for*, which makes them determined but not explained. Since
`net = tr_M^{z=1} − h·δ_{w₀}` and both sides restrict to the centre:

    a_λ = y_λ(1) − h·b_λ

with `b_λ` the χ-expansion of the longest-coefficient functional on the centre.
Verified for all three blocks — **and `b_(2,1) = 0`**. So `a_(2,1)` is not merely
numerically equal to a Markov weight, it **is** one, and

    net(dC) = −h · y_(2,1)(1)                                        [exact]

The z-free part of the ladder phase, stated entirely inside the Ocneanu family
with no `net`-specific object left in it. With `χ^(2,1)(Δ) = 0` from the block
resolution, the 2-dimensional block's role is now complete: nothing in the
trace-visible part, everything in the trace-invisible part, and its size there
fixed by its own Markov weight at the trivial loop value.


---

## Tranche (2026-08-26, PR #5864) — what rung 1 IS

Owner directive this session: *"Even if deriving the ladder doesn't fully close
the gap, if it is the proper thing to do it should be done."* So this tranche
does the derivation and prices the expectation separately, rather than treating
the 92x baseline gap as a reason to leave it undone.

### Derived (exact, symbolic over Q(q); no anchor, no fit; 12/12)

`computations/qbeta/qbeta_d_frame_rung_one_rederivation_probe.py`

**(D1) — new.**

    2*alpha = net(Delta) - tr_M^z(Delta)          identically in q AND z

`alpha = (z-1)h/2` is the rung-1 phase, `net` the coordinate sum (step 8's
"counit"), `tr_M^z` the Ocneanu trace. Delta rebuilt from the typed-crossing
words, asserted against its stated coordinates. So alpha is neither free nor
fitted: it IS the discrepancy between the ladder's baseline and the admissible
functional.

**(D2) — NOT new, corroboration only.** Rungs 2-5 carry no `z`. Already
Lean-proved as `QOU.BraidKnot.Q_beta_categorical_ofPhase_tail_common` by the
sibling on #5337. I derived it independently and initially wrote it up as a
finding; corrected the same session.

**(D1) + (D2) jointly:** the ladder's ENTIRE convention-dependence is its own
baseline's inadmissibility. Neither half states that alone.

**(D3) — new, modest; an explanation of a proved theorem, not a new one.**

    d_1 = q^3/(q^2+1) = z_D           (Hoefsmit V_(2,1) DIAGONAL entry)
    y_(2,1)^D = -d_1 * d_2                                        [exact]

Convention D's Markov parameter is the (2,1) Hoefsmit diagonal entry -- the same
expression written twice in the corpus without being joined. Since `b^2 =
d_1*d_2 + 1` is the Hoefsmit coupling's DEFINITION, the sibling's
`hoefsmitB_sq_eq_one_sub_stdWeightD` is that definition re-read, not a
coincidence between the D weights and the Hoefsmit matrix.

### What that makes of rung 1

Both terms of its phase are 2-dimensional-block objects: alpha's z-free part is
`-h*y_(2,1)(1)`, and `b` is the (2,1) Hoefsmit coupling. That block has
`chi^(2,1)(Delta) = 0` -- invisible to the trace of Delta -- and D's TL quotient
KEEPS it (only the three-row `(1^3)` is annihilated).

**So rung 1 is built entirely from a block the trace cannot see and the
convention retains.** That is a DERIVED reason a trace baseline does not rescue
it, not a further measurement of the fact that it doesn't.

### Measured, none selected

Three readings of the D-frame rung 1, order fixed before evaluation; no convex
combination formed, no selection on agreement:

    R-i    baseline=tr_M^{z_D}, alpha dropped        -4.316e+8 ppb
    R-ii   baseline=tr_M^{z_D}, alpha kept at z_D    -4.322e+8 ppb
    R-iii  baseline=net,        alpha at z_D          6.012e+5 ppb   [INVALID]
    R-iv   baseline=augmentation (z=q), alpha dropped 1.246e+8 ppb

**Adverse.** R-iii -- the reading the corpus FORBIDS -- is **207x closer** to
CODATA than the nearest admissible one. Third construction in this channel where
proximity tracks INADMISSIBILITY; step 8's `net` was the first. My reading is
that this points at the ansatz rather than the rungs. Reported, not buried.

### Calibration

The decomposition reproduces the existing implementation BIT-IDENTICALLY
(`|diff| = 0.0`, both pins), so (D1) is about this ladder and not a lookalike.

### Prediction retracted, kept in the file

I asserted "all four readings exceed 1e6 ppb" before checking. FAILED on R-iii
at 6.0e5. Repaired by stating what is true and naming what the failure showed --
not by widening the bound.

### Spun off, not chased

`qou-54g5` (high): the block claims -0.0066 ppm at the muon pin; the
implementation returns +7.34 ppb. Opposite sign, ~11 % apart in magnitude. That
is the number the whole ladder is quoted on.

### Still open

The bean is NOT closed. What remains is the choice among the readings on
principled grounds -- which (D3) now constrains but does not settle -- and the
`qou-xzrj` trace-invisible term. Coordination posted to #5337.


### Correction 2026-08-27 — (D1)'s identification is a sibling's, not mine

The tranche note above presents **(D1) — new**. That is wrong and is corrected
here rather than edited away.

A sibling stated the identification on PR #5337 at **2026-08-26T06:59Z**
(comment 5421747260, from #5815 / bean `qou-avt5`) — roughly 15 hours before my
probe existed:

> "`Q_A = -E_0*eps(Delta)`, and the ladder's phase **is** `eps - tr_M`."

I read that comment during coordination and did not connect it. It sits in the
same #5337 thread where I then posted (D1) as new.

**What survives as mine** is the derivation rather than the assertion, and the
gap between the two is load-bearing rather than cosmetic:

- **The factor.** "the phase IS eps - tr_M" is off by 2; the phase is `alpha`
  and the identity is `2*alpha = net - tr_M`.
- **"Identically in z"** — the part the localisation argument actually needs.
  An unquantified assertion at one `z` cannot be joined to (D2) to conclude
  anything about where the convention lives; a for-all-`z` identity can.
- **Delta rebuilt from the typed-crossing words** and asserted against its
  stated coordinates, so the identity is about the corpus's object.

Restated honestly: **identification theirs, proof and exact form mine.**

### The pattern, since this is the second time in one session

(D2) was already the sibling's Lean; (D1)'s identification was already the
sibling's comment. Both were caught *after* I had written them up as findings.
The common cause is that I grep before *starting* and after *finishing*, but
write the novelty claim in between — and in both cases the prior was somewhere
the six-path corpus-grep does not reach: a Lean file I had not linked to the
question, and a **PR comment**.

**PR comments are a seventh surface and the checklist does not name them.** On
an actively-coordinated bean like this one they are where sibling results land
*first*, hours to days before an audit doc or a content block. Worth adding to
the checklist, or at minimum: on a bean with a live sibling PR, read that PR's
comment history before claiming novelty, not only before starting.


## 2026-08-28 — the D-frame ladder is priced: 74x to 257x the correction the C ladder supplies

Owner selected "re-derive the ladder under D" as one of four tracks on
`qou-99qc`. Not attempted here; priced, so the next session starts from the
cost rather than rediscovering it.

**Why it cannot start from the current base.** The ladder multiplies a base
`Q_base = eps(Delta) * E_0`, and that `eps` is the coordinate sum, which
`qou-99qc` establishes is INADMISSIBLE under D (it does not descend to
TL_inf(q)). So a D-frame ladder cannot be the C ladder with `z` swapped — that
much AGENTS.md and `decayLadder_zC_threeRow_ne_zero` already say — but it also
cannot keep the same BASE. Both the functional and the ladder change.

**What the re-derivation has to achieve.** Recomputed at q0 from the NF vector,
reproducing this bean's and `qou-99qc`'s published table exactly (independent
route: covectors built from the basis, not read off the recorded numbers):

    functional                       |Q_pred| MeV     err vs CODATA
    coordinate sum (INADMISSIBLE)    0.7836458274        +0.167757 %
    augmentation   (admissible)      0.8798905613        +12.47 %
    tr_M at z_D    (admissible)      0.4447004085        -43.1572 %

The current five-rung ladder corrects the 0.167757 % residual of the
inadmissible base. Starting from an admissible base instead, the ladder must
correct:

    augmentation    12.47 %    ->   74.3339x larger
    tr_M at z_D     43.1572 %  ->  257.26x  larger

**So this is not a perturbation of the existing ladder.** A correction two-plus
orders of magnitude larger is a different object, and the c_k extracted for the
C frame carry no information about it. Any attempt that reuses the C rungs as a
starting point is doing the substitution the corpus forbids, one level up.

**Track 3 is closed and it removes the shortcut.** The convex-combination repair
(a weight between the two admissible functionals) is EXCLUDED by a rank
computation — `net` is not in their span, so there is no weight to derive. See
`qou-99qc` and `computations/qbeta/qbeta_admissible_span_prune_probe.py` (8/8).
That route is not available to shrink the 74x.

Scope-(a): none of this shows the Q-value wrong, and none of it forecloses the
re-derivation. It sizes it.

## 2026-08-28 — base-admissibility completeness now Lean-proved (PR #5925, bean qou-06wh)

The 'admissible set is COMPLETE, closed at two elements {q, z_D}' fact (qou-99qc,
sympy bracket probe 15/15) is now sorry-free Lean: QOU/QBeta/ConventionDAdmissibleRoots.lean.
The (1^3)-weight numerator factors over any CommRing as (z-q)*((q^2+1)z-q^3), so
admissible_markov_param_iff proves roots = {q, z_D} exactly and one_not_root proves
z=1 (net) excluded on the substrate window. The base side of the re-derivation is
now on a Lean foundation; the ladder/correction side (74x-257x) stays open.

## 2026-08-29 — TAKEOVER of the ladder/correction side (owner directive)

Owner: take over the cds1 ladder/correction side if not active in 2h. Checked:
- #5897 (element-identity fork) last commit 2026-08-28T23:53Z (7 min) — ACTIVE, left alone.
- #5337 (claude/qbeta-f-coordinate, the ladder/correction side) last commit
  2026-08-19T20:30Z (9 days), still DRAFT, body says 'work starting, nothing
  claimed yet'. Stale tip db4beedfa0. Its stated goal (fold the Wenzl two-row
  cap into the D decay correction) is UNSTARTED — the F-coordinate bridge it
  cites is already on main.
Taking over the WORK on my own branch (claude/borel-alien-calculus-n24484,
from main); NOT force-pushing #5337's branch. Goal: compute the parameter-free
two-row-capped correction under D (base = admissible aug/tr_M, must close
12.47%/43.16% residual), falsifiable, no fit.

## 2026-08-29 — ladder/correction side: no parameter-free admissible correction (takeover result)

Systematic enumeration of parameter-free correction candidates on BOTH admissible
bases (probe qbeta_d_frame_admissible_base_correction_search_probe.py, audit
2026-08-29-cds1-admissible-base-correction-search.md):
- tr_M base (z_D): F_required=1.75924, closest q^6 at 6.31% => WALLED.
- augmentation base (z=q): F_required=0.88913; sqrt(1-h)=0.889348 lands 0.025%
  but is DIAGNOSED as the forbidden z=1 return — base ∝ affine trace
  tr_M(Delta_S)=h^2/2-h*z, so F_required = the trace's z=q->z=1 ratio
  (h/2-1)/(h/2-q) to 0.17% (net-vs-CODATA gap; base ratio agrees 1.3e-11).
  Correcting aug back to CODATA = return to inadmissible net(z=1). Not adopted.
VERDICT scope-(a): no parameter-free ADMISSIBLE correction; the sub-0.1% near-match
is the forbidden z=1 return in disguise. Extends the two-row-cap prune (13.6x) to
both bases; closes #5337's stated question. Open core sharpened: the accurate value
lives at inadmissible z=1, so a genuinely different D construction (not tr_M(Delta)
at a single z) is needed. Nothing wired.

## 2026-08-28 — TWO ELEMENTS ANSWER TO THE NAME `Delta`, and this bean's two
## headline results sit on different ones (PR: claude/cds1-ladder-convention-d-2026-08-28)

Probe `computations/qbeta/qbeta_delta_element_fork_pricing_probe.py` (15/15,
exact symbolic Q(q), no float64). Audit
`docs/audits/2026-08-28-cds1-two-nucleon-word-models.md`. Bean `qou-bg3w`.
Scope-(a): refutes nothing, proposes no c_k, wires nothing, decides nothing.

**The two elements.**

| | Delta_S | Delta_L |
|---|---|---|
| source | `deuteron-binding-dressing-proton-net.md`: net(p)=1-h/2, net(n)=1-3h/2+h^2/2 | `hecke_core._PROTON_G0/_G1` etc. |
| crossings | 1 (p), 2 (n) | **11** each |
| reduced | (h^2/2, -h/2, -h/2, 0,0,0) | (-h/2, -h^2/4, -h^2/4, -h(q^4+1)/(4q^2), 0, 0) |
| net(Delta) | h^2/2 - h = epsNPq = **-0.187207** | **-0.233198** |
| tr_M^z(Delta) | h^2/2 - h z (**affine in z**) | **quadratic in z** |
| chi^(2,1)(Delta) | **0** identically | -0.106814 |

Both closed forms in `qbeta-counit-closed-form.md` hold for Delta_S and FAIL
for Delta_L. Delta_S's crossing count is DERIVED (a typed crossing has
net = 1+d and net is multiplicative across DISTINCT generators, so
net(n) = (1-h/2)(1-h) exactly); Delta_L's 11 is what
`q-beta-c3-hopf-three-fold-markov.md` states the construction uses.
Mechanism: net is NOT multiplicative within one generator, since
T_0^2 = h T_0 + 1 gives net(T_0^2) = 1+h vs net(T_0)^2 = 1.

**CALIBRATED BEFORE CONCLUDING.** Delta_L reproduces all three chi^lambda in
the committed `qbeta-d-frame-trace-baseline.witness.json` to **6.1e-50**, and
the probe reproduces the committed `gap_over_ladder_ratio = 92.1058...`
EXACTLY. That is what establishes the attribution rather than asserting it.

**Consequence 1 — the D-frame trace baseline is priced across the two.**
`qbeta_d_frame_trace_baseline_probe` hard-codes `eps = h**2/2 - h` (Delta_S)
and traces the 11-crossing words (Delta_L).

    published, MIXED   92.106x
    consistent Delta_S  257.260x     <- the element Q_A is actually built from

The published figure UNDERSTATES the gap by **2.793x**. Per the owner's
2026-08-26 correction this is not a reason to leave the re-derivation undone;
it moves the expectation, in the harder direction.

**Consequence 2 — (D1) IS SHORT-MODEL-SPECIFIC. This is the part that
matters.** `2*alpha(z) = net(Delta) - tr_M^z(Delta)` is affine in z ONLY
because Delta_S is supported on {gamma, sigma0, sigma1}, where net - tr_M^z is
0, 1-z, 1-z. Delta_L is supported on L+ too, where the Ocneanu trace is z^2, so
there the difference is QUADRATIC and alpha = (z-1)h/2 is not the
counit-minus-trace gap at all.

So the ladder phase's LINEARITY IN THE MARKOV PARAMETER — the property that
makes the C->D move look like a substitution in the first place — is a fact
about the short model, not about the 11-crossing nucleon words the corpus
names.

**Where that leaves the re-derivation.** It cannot be posed until the element
is chosen, and the two answers send it to different places:
 * Delta_S canonical -> the phase leg is derived as recorded ((D1) holds for
   every z), the bar-odd projection and forced D weights apply, the D price is
   257x, and the open item is the c_k assembly (still fenced).
 * Delta_L canonical -> (D1) is UNAVAILABLE, so with branch 1 closed in full
   and branch 2 circular, **branch 3 (KZ / Kohno-Drinfeld holonomy) is the only
   remaining home for a derivation of alpha**. Also chi^(2,1)(Delta_L) != 0, so
   "the phase is blind to the 2-dim block" and the floor
   `net(dC) = -h*y_(2,1)(1)` both need restating.

**NOT the qou-avt6 / qou-goc9 question.** Those concern the AUGMENTATION
(sigma -> q, an algebra map). This concerns the COORDINATE SUM `net`
(T_w -> 1), which is what epsNPq is (qou-99qc) and what Q_A is computed from.
Under `net` the element exists — it is Delta_S. Complementary; neither implies
the other. (Non-overlap checked against live PR #5893 before writing.)

**FLAGGED, NOT CLAIMED.** `pyhecke.atom.PROTON_NF`/`NEUTRON_NF` coordinate sums
differ by -0.188291, 0.58 % from epsNPq and matching NEITHER element. Stored
float64 and the basis convention is UNVERIFIED, so it is a pointer, not a
measurement. Tracked in `qou-bg3w`.

**Still open.** cds1 is not closed and nothing here closes it.


## 2026-08-29 — THE FORK IS FORCED: (D1) cannot be had for the 11-crossing element

Owner asked directly: *"can we derive full 11 cross w/ D1?"* Answer: **no**, and
the exclusion is symbolic.

The entry above says (D1) is affine only because Delta_S is supported on
{gamma, sigma_0, sigma_1}, while Delta_L also lives on L+ where the Ocneanu
trace is z^2. **But Delta is a DIFFERENCE** -- if n and p carried the same L+
coordinate it would cancel and (D1) would survive for the 11-crossing element.
That escape was open and is now measured shut.

`computations/qbeta/qbeta_d1_eleven_crossing_exclusion_probe.py` (6/6), exact
symbolic in h, words from the hash-pinned `build_nucleon` transcription (PR
#5893) imported rather than re-transcribed:

    gamma     h(2h^4 + h^2 - 2)/4
    sigma_0   h^2 (h^2+1)(2h^2+1)/4
    sigma_1   h^2 (h^2-h+1)(h^2+h+1)/4
    L+        -h^5/4                     <- DOES NOT CANCEL
    L-        h(h^2+1)(h^4-2)/4          <- DOES NOT CANCEL
    e^-       -h^4 (h^2+2)/4

**L+ = -h^5/4 shuts it cleanly.** A monomial has one root, h = 0, and the
substrate has h = q - 1/q ~ 0.209 at q0. There is no parameter value in range
where the quadratic term drops out. Scope-(b) with the invariant cited (a
degree argument). L- corroborates independently: roots only at h = 0 and
h^4 = 2 (~1.189), neither the substrate value.

**Consequence.** The two branches this bean records are now genuinely
exclusive, and the choice of element IS the choice of programme:

  * Delta_S canonical -> (D1) holds for every z, the phase leg is derived as
    recorded, open item narrows to the c_k assembly.
  * Delta_L canonical -> (D1) unavailable; with branch 1 closed and branch 2
    circular, branch 3 (KZ / Kohno-Drinfeld holonomy) is the only remaining
    home for a derivation of alpha.

No third option keeps both. cds1 remains blocked on `qou-bg3w` (which element
is Delta) -- but that block is now a decision with both costs priced, not an
open question about whether the dichotomy is real.

**A float64 run was done first and is NOT the evidence.** The stored
PROTON_NF/NEUTRON_NF give L+ = -9.98e-5, L- = -0.109 -- the right answer, from
values whose basis convention this bean's own tail records as UNVERIFIED, and
-9.98e-5 is small enough that "is it exactly zero?" is precisely what float64
cannot answer.


## 2026-08-29 (LATER) — CORRECTION to the entry above: it tested the wrong element

The entry immediately above ("THE FORK IS FORCED") reported a real result by
three wrong routes at once. **Its verdict stands and is now established
properly**, but do not cite its reasoning. Corrected in
computations/qbeta/qbeta_d1_eleven_crossing_exclusion_probe.py (14/14, rewritten).

1. **It built a NINE-crossing element and called it eleven.** build_nucleon is
   the transcription of pyhecke.atom.build_nucleon_nf: 3x(sigma_0, sigma_1^-1)
   + 3 quark pairs = 9. That builder omits the 2-sigma_0 gluon dressing
   deliberately — its own docstring says "No separate gluon dressing — B_3 IS
   the gluon structure".

2. **There is no single 11-crossing element.** pyhecke.atom carries THREE
   mutually inconsistent nucleon constructions:

     build_nucleon_nf     ( 9 crossings)      net = -0.1883216147
     build_atom_nf_exact  (11, interleaved)   net = -0.2272041420
     nucleon_gen_chains   (11, gen-grouped)   net = -0.2332458961

   The two 11-crossing models carry the SAME multiset of typed crossings and
   differ only in ORDER — build_atom_nf_exact interleaves gen-0/gen-1,
   nucleon_gen_chains emits all gen-0 then all gen-1. H_3(q) is not commutative
   across generators, so they are different elements and their nets differ by
   2.6 %. **qou-bg3w's Delta_L (-0.233198) is the gen-grouped one**, which the
   first version never touched.

3. **It tested the wrong quantity.** (D1) is affine in z iff the **z^2
   coefficient of tr_M** vanishes. With TR = [1, z, z, z^2, z^2, z(hz+1)] that
   is d[L+] + d[L-] + h*d[e^-], a SUM — not L+ alone. **On qou-bg3w's actual
   Delta_L, L+ is EXACTLY 0**, so the first version's stated reason ("L+ =
   -h^5/4 shuts it cleanly") is FALSE for that element. The exclusion there
   rides on L- instead.

**The corrected exclusion**, exact symbolic in h, all three long models:

     9-crossing       [z^2] = -h(h^2-h+1)(h^2+h+1)/2   real roots {0}
     11 interleaved   [z^2] = -h(h^2+2)(2h^4+h^2+1)/4  real roots {0}
     11 gen-grouped   [z^2] = -h(h^2+2)/4              real roots {0, +-i sqrt2}

Each nonzero, each with h = 0 as its ONLY real root; substrate h ~ 0.209.
Scope-(b), invariant cited (a polynomial with no real root but zero cannot
vanish at a nonzero real point). So the fork is forced **against all three long
candidates**, not against one 9-crossing element mislabelled as eleven.

Both 11-crossing transcriptions are VALIDATED against pyhecke rather than
trusted: nuc11_interleaved coordinate-by-coordinate against build_atom_nf_exact
in exact Fraction arithmetic, nuc11_gen_grouped against the _PROTON_G0/_G1
chains.

**New, and it is a defect in the tree, not in this bean:** pyhecke.atom's three
nucleon constructions disagree by up to 24 %, and different consumers read
different ones. The exact atom/mass path uses build_atom_nf_exact; the module
constants PROTON_NF/NEUTRON_NF are build_nucleon_nf; the fork-pricing probe
reads _PROTON_G0/_G1. Not filed as its own bean yet.
## 2026-08-29 — workflow: ALL 5 Q_beta/c3 lanes converge on this bean as the blocker
Adversarially-verified (audit 2026-08-29-convention-d-qbeta-front). Key results: (1) proved-lean STRUCTURAL VERDICT (both lenses survive): the C ladder does NOT survive under D; z_D IS the two-row/TL trace (y_(1^3)=0 IFF z=z_D; qou-06wh/PR#5925 proves roots {q,z_D}, net excluded); C->D not a z-swap. Next brick = owner-call qou-99qc (a counit eps that DESCENDS to TL_inf AND reduces to the mass-channel eps; current net(e) != 0 on J_(1^3)). (2) c2 under D is OPEN, NOT -1 and NOT -9.299: the C-frame expression 1-u^2 is z-free (docstring, symbolic-exact) but whether the D-REBUILT N=2 factor = 1-u^2 is OPEN; -9.299 is a CODATA data-inversion (Q_exp/Q_N1^D-1)/u^2, scope-(a) non-structural. (3) -974 cost framing corrected: it is a 1/u^3 amplifier; D phase residual 0.895x (better than C) -- 'measures the amplifier, not the physics'. Mass three-row forcing is COMPATIBLE with a genuine D ladder (must factor through TL, co-located with mass channel).


## 2026-08-29 — an ADJACENT class exclusion from the #5337 branch, and that branch closing out

Recorded by the agent who opened #5337 (closed unmerged; the takeover was
correct — the branch was stale and its named route was already pruned). One
result from it is worth keeping, and it is **not** a re-derivation of the
2026-08-18 prune above: it excludes a different class, by a bound rather than
by a measurement.

**Not the same object.** The 2026-08-18 entry prunes
`F = two-row restriction fraction of the n=3 trace` — the correction taken to
BE the dropped weight, `dim.y_(1^3) = 0.0227449`, 13.6x the target. The class
below instead keeps Form B's functional shape and resolves it per block:

    g(zeta) := ln(1 + zeta.h)/zeta          (Form B's integrand)
    F_blocks := Sum_lambda p_lambda . g(zeta_lambda)

where `zeta_lambda := chi_lambda(sigma)/f^lambda` is the block's own loop value
and `p_lambda := f^lambda.y_lambda`. This is a **Jensen gap** — Form B as
written evaluates `g` AT the mean, this averages `g` — not a restriction
fraction. Nothing above covers it.

**The identity underneath it, symbolically exact (sympy, over Q(q)).** With
characters `chi_(3) = q`, `chi_(2,1) = h`, `chi_(1^3) = -1/q` (the Hecke
generator's eigenvalues `q` and `-1/q`, §7a):

    Sum_lambda y_lambda . chi_lambda(sigma)  =  q^3/(q^2+1)  =  z_D   EXACTLY

So `z` is not an independent convention knob at all: it is the MEAN of the
per-block loop values under `p_lambda`. This is the n=3 shadow of the
now-proved `y_(1^3) = 0 <=> z = z_D` (qou-06wh / PR #5925), reached
independently and before that landed, and it is a third route to the
`Sum dim.y = 1` normalisation the 2026-08-18 entry reports.

**The exclusion, and why it is a class statement.** A convex combination lies
in the convex hull of its arguments, so for ANY weights whatsoever
`F_blocks in [min_lambda g, max_lambda g]`. Measured at 65 dps, proton pin:

    convention D   hull = [0.786985113907, 0.865697506066] MeV
    convention C   hull = [0.786985113907, 0.969606940981] MeV
    Q_codata       = 0.782 MeV                       BELOW BOTH HULLS

The lower edge is identical in the two frames because it is set by the same
block, `(2,1)`, which both retain. So **no block-resolved Form B reaches the
measured Q-value in either convention, under any weighting** — the weights
never enter. Scope-(b) for the class as stated, with the invariant cited
(convexity); scope-(a) as to the physics, since the hull is evaluated
numerically at one anchor and the per-block `1/zeta` normalisation is an
assumption the corpus does not derive.

For completeness, the derived weights themselves (they are inside their own
hull by construction, and far from the target):

    frame  mean_form      blocks_full    blocks_logonly   (rel. to Q_codata)
    D      +5.2549e-02    +5.5708e-02    +1.4436e-02
    C      +6.3990e-02    +6.7785e-02    +8.2005e-03

all 1-6 % objects, consistent with the F-coordinate audit's finding that the
bridge is a ~5e-2 object while the cos factor is ~1e-6 — i.e. this class is the
wrong SIZE for the correction, independently of the hull.

**The probe was never committed.** It lived on `claude/qbeta-f-coordinate-2026-08-19`
as an uncommitted file and is not being landed: the route is settled, and a
witness for a pruned class is maintenance surface with no consumer. The
argument above is ten lines to reproduce from this text.

**That agent is off this bean.** No claim held; the takeover stands.

## 2026-08-30 — a LEAD on where the D-frame re-derivation should start (NOT a finding)

Stating this as a lead because I can measure the identity but cannot yet
separate the two readings of it, and the difference is the whole content.

### The identity, exact over Q(q)

The ladder's Hoefsmit constant b = sqrt(q^4+q^2+1)/(q^2+1) satisfies

    b^2 = [3]_q * z_D^2 / q^4          EXACT (sympy, difference simplifies to 0)

and the convention-C analogue does NOT hold ([3]_q z_C^2/q^4 leaves a
q^5(q+1)^2 denominator). Equivalently: b's denominator is (q^2+1), which is
convention D's denominator, and b contains no (q+1) and no sqrt(q) — the two
things convention C is built from.

If that is structural it is a real prune: the ladder's RUNGS are already
D-natural (b appears in every rung as b^2 h^4, 2b^3 h^6, b^8 h^8, ...) and
the entire convention question localises to the PHASE alpha = (z-1)h/2,
which is the only place z_C appears. That would make the published ladder
convention-MIXED rather than convention-C, and would say the re-derivation
has to re-derive one object, not five.

### Why this is NOT yet a finding — the honest objection to my own lead

The coefficient [3]_q/q^4 was chosen BY ME to make the identity come out.
Any b can be written as (coefficient) * z^2 for a suitable coefficient; the
question is whether THIS coefficient is natural or fitted, and I have not
established that. Sharpened: the unique positive z solving b^2 = [3]_q z^2/q^4
is exactly z_D — but I picked the numerator that makes it so.

Independent reason for caution: b is a HOEFSMIT object (the H_3 seminormal
rep), defined with no reference to any Markov parameter
(qbeta_symbolic_chain_alpha_b.py calls it 'Hoefsmit b (closed form!)' and
derives it from the representation, not from z). So the identity relates two
INDEPENDENTLY defined objects, which is what makes it interesting — and also
what makes a shared cyclotomic factor (q^2+1) a plausible coincidence, since
(q^2+1) is not rare in H_3.

### The test that would separate the two readings

Does it GENERALISE? If b is genuinely D-natural the analogous relation should
hold between the n=4 Hoefsmit constant and the n=4 convention-D parameter; if
it is a shared cyclotomic factor at n=3 it will break. This is the
da-arity-conflation discipline applied to my own lead: a relation at one
instance says nothing about the family, and I have exactly one instance.

Not run yet — 'the n=4 Hoefsmit b' needs defining before it can be tested,
and that definition is itself the work. Nothing wired; nothing claimed.

## 2026-08-30 (later) — the lead above is RETRACTED; what replaces it (PR #6103)

**The lead is dead, and I killed it.** b^2 = [3]_q z_D^2/q^4 is a RESTATEMENT.
In quantum integers:

    b   = sqrt([3]_q)/[2]_q      (Hoefsmit off-diagonal, axial distance 2)
    z_D = q^2/[2]_q
    z_C = 1/[2]_sqrt(q)

Substituting z_D = q^2/[2]_q returns b^2 = [3]_q/[2]_q^2, which IS b's own
definition. Zero information about b. The objection I attached to the lead
this morning was the right one and it was fatal: two independently defined
objects sharing a cyclotomic factor. Probe
qbeta_ladder_convention_dependence_is_one_phase_probe, 7/7, carries the
retraction as a control rather than deleting it.

**What is actually true, and it is the opposite of the lead:** b is a HOEFSMIT
constant, built from the H_3 seminormal representation with NO Markov
parameter in it. So b is convention-INDEPENDENT — neither C nor D.

## The sharpening, which is the real gain

Measured over the whole published formula: Q_A, hbar_q, b and ALL FOUR RUNGS
are z-free. alpha = (z-1)h/2 is the ONLY z.

That creates a tension worth naming, because both halves are corpus positions:

  (i) the published ladder's only z-dependence is one phase, so a
      z-substitution changes the phase and NOTHING ELSE; and
  (ii) AGENTS.md + QOU.QBeta.decayLadder_zC_threeRow_ne_zero say the D-frame
      ladder must be RE-DERIVED and that a z-swap is invalid.

Both cannot be the whole story. The only resolution: the RUNGS' DERIVATION
used the three-row C-frame trace at a step that has been integrated out of the
final formula. Under D the trace is two-row (y_(1^3)(z_D) = 0, Lean-proved in
qou-06wh and reproduced here from the regular representation).

**LOCATING THAT STEP IS THE RE-DERIVATION.** That is a sharper statement of
this bean's open problem than it carried before, and it is where the next
session should start: find where b^2 hbar^4, 2b^3 hbar^6, 2b^8 hbar^8 and
(b^2+1/2)b^5 hbar^10 come from, and check which of them used three rows.

## Reproduced, NOT new — verified as not new

The D-frame H_3 weights recomputed here match
computations/y-lambda-symbolic-witness.json (markov_convention: D) exactly:
y_(3) = (q^4+1)/(q^2+1)^2, y_(2,1) = q^2/(q^2+1)^2, y_(1^3) = 0. Corpus-grep
found this AFTER I computed them, so treat my run as an independent check on
that committed witness, not as a contribution.

Newly recorded (vocabulary, not mathematics): y_(2,1)(z_D) = 1/[2]_q^2 and
tr_M^D(T_e) = 1 exactly, so the D-frame trace closes as

    tr_M^D = ( [2]_{q^2} chi^(3) + chi^(2,1) ) / [2]_q^2 ,  [2]_q^2 = [2]_{q^2} + 2.

## 2026-08-30 (third pass) — the sharpened question is ANSWERED, and the answer is a negative

Previous entry asked: the published ladder's only z-dependence is the phase
alpha, so where does the three-row C-frame dependence hide such that
're-derive, do not z-swap' is true?

**It does not hide. There is no derivation of c_3 to redo.** The live producer
computations/probe_q_beta_operator_valued_N3.py extracts c_3 by INVERTING the
experimental Q_beta against the ansatz, in its own comments:

    Q_emp_factor    = Q_AME / Q_N2                        # 'residual factor we need'
    c3_emp_additive = (Q_emp_factor - 1) / (b**3 * hbar_q6)

and labels the matching row '[fit]'. So 'c_3 = -2 = J_Hopf(q=1)' is a post-hoc
MATCH to an extracted number, not a derivation. J_Hopf(q=1) = -2 is itself
convention-free — the Jones polynomial of ANY link at t=1 is
(-2)^(components-1), and Hopf has 2 components — and every J_Hopf site in the
corpus is a hardcoded literal in _deprecated/ citing Jones 1985, computed from
no trace at any z.

Measured (probe qbeta_c3_is_extraction_determined_probe, 5/5):
  - the extracted c_3 fed back reproduces its own input, residual 0
  - the published N=3 residual is exactly the (-2 vs extracted) gap propagated
  - the extraction amplifies its reference Q by 1.618e6
  - c_3 moves 2.8 % across q0 pins but 5.5e4 % between z_C and z_D

## What this means for this bean, restated

'Re-derive under D' cannot mean 'redo the derivation'. For c_3 there is none.
It means DERIVE it for the first time — or establish that the product-ansatz
SHAPE, Pi(1 + c_k u^k) with u = b*hbar_q^2, is itself C-specific. The D-frame
extracted c_3 near -974 sits near no categorical candidate, which is scope-(a)
evidence the shape does not transfer.

This is consistent with, and sharpens, the red-team verdict already recorded in
this bean ('convergence-framework PHYSICS wrapped around higher-coefficient
NUMEROLOGY').

## The near-match is fragile — and this is NOT a corpus defect

I nearly filed 'the corpus carries two neutron masses' as a high-priority bug.
It is DOCUMENTED at both sites: codata_2022_source.py lists CODATA-2022's
direct measurement 939.56542194(48) AND an AME-derived 939.56542179, and
qou_substrate's line reads 'AME-derived, NOT CODATA'. Retracted.

What survives is stronger: choosing between those two legitimate references
moves Q_beta by 191.73 ppb and the extracted c_3 by 17.6 % — about 5x the
3.4671 % gap on which the c_3 = -2 near-match rests. The near-match is not
robust to a reference choice the corpus deliberately leaves open.

(Second retraction, same pass: I read M_N_MEV_VALIDATION's long decimal
expansion as an mpf built from a float64 literal. Wrong — the witness stores
strings; that was str(mpf) at 65 dps.)

SCOPE: the probe does not reproduce the corpus's recorded c_3 = -2.0693425728
with either reference and says so up front. Its content is structural.

## 2026-08-30 (fourth pass) — the audit is COMPLETE: nothing above N=0 is derived

Traced every ingredient of the published ladder to its definition site.

| ingredient | z-carrying? | derivation status |
|---|---|---|
| Q_A = abs(eps m_e/(q(q-1))) | no | eps is a coordinate sum; z-free |
| hbar_q = (q-1)/q | no | definition |
| b = sqrt([3]_q)/[2]_q | no | Hoefsmit off-diagonal, axial distance 2 — genuinely representation-theoretic, and convention-INDEPENDENT |
| alpha = (z-1)h/2 | **YES, the only one** | **bare `def`, NO derivation theorem** |
| c_2 = -1 | no | bare `def` (N2_factor), no theorem; 'structural' by unfolding only |
| c_3 = -2 | no | **EXTRACTED by inverting CODATA**; the J_Hopf(q=1) match is post-hoc |
| c_4 = -2b^4, c_5 = -(b^2+1/2) | no | read off b |

**So 're-derive the ladder under D' has nothing to re-derive.** Above N=0 the
ladder is one undeirved phase, one undeirved structural rung, one extracted
rung, and two read off a representation-theoretic constant. The task is to
DERIVE it, first time — that is a bigger and more honest statement of this
bean than 'redo the derivation under a different convention'.

Evidence for the alpha row specifically
(content/.../lean/QOU/BraidKnot/QBetaCategoricalPrecisionLadder.lean):
`alpha` is a bare `noncomputable def` at line 61. Every theorem touching it
evaluates at q=1 (`alpha_one`), states bar-behaviour
(`eigenphase_bar_involution`), or restates the form (`q_beta_nK_structural_form`).
None derives it. The same file at lines 686-690 already records that the
'eigenphase = f' hypothesis is **falsified at u^1** — so the one derivational
story alpha had is closed, negatively.

## Two things I checked that were ALREADY KNOWN (corpus-grep caught both)

1. The Lean ladder's `markovZ'` is convention **D** (`q^3/(q^2+1)`) while the
   Python implementation is **C**. Not a discovery: the file's own docstring
   carries the caveat ('a theorem evaluated only at the classical point is
   convention-agnostic by accident of sitting exactly on the coincidence ...
   anything evaluated away from q = 1 still needs re-deriving under D'), and
   the migration commit bf7d8f3d3e is titled 'qou-cxjq: the c_k ladder — it
   COMPILES under D, and that is a much weaker result than it sounds'.
2. The D-frame H_3 Markov weights — already in y-lambda-symbolic-witness.json.

## Where a next session should start

Not on the ladder's algebra, which this pass has now exhausted. On alpha: it
is the only convention-carrying object and it has no derivation. Either derive
the single-wrap eigenphase from the D-frame two-row trace, or establish that
the product ansatz Pi(1 + c_k u^k) with u = b*hbar_q^2 is not the right shape
under D. The u^1 falsification above is a live constraint on the first route.

## 2026-08-30 — CORRECTION to my own fourth-pass entry above

The fourth-pass table says alpha is a "bare \`def\`, NO derivation theorem" and
concludes "nothing above N=0 is derived". **The first clause is true only of the
LEAN; the conclusion over-claims for alpha.**

alpha IS derived, and by me, three days before I wrote that:
computations/qbeta/qbeta_d_frame_rung_one_rederivation_probe.py (PR #5864)
proves

    (D1)   2*alpha = net(Delta) - tr_M^z(Delta)     identically in q and z

with the IDENTIFICATION credited there to a sibling on PR #5337 (comment
5421747260, bean qou-avt5). I re-derived it from scratch this pass before the
corpus-grep found my own file — searching "net minus trace" and "eigenphase"
first, which miss it; only the file-level grep hit.

So the corrected status of the ladder above N=0:

  alpha    DERIVED as a probe (2*alpha = net(Delta) - tr_M(Delta), exact in z);
           NOT formalized in Lean, where it remains a bare \`def\`
  c_2      bare \`def\` (N2_factor), no theorem
  c_3      EXTRACTED by inverting experiment
  c_4,c_5  read off the Hoefsmit b

**The concrete next step is therefore narrower than 'derive alpha': Lean-prove
(D1).** The derivation exists, is exact and symbolic in both variables, and
formalizing it would upgrade alpha from bare def to derived — which is exactly
the formalize-first discipline this bean's own Discipline section asks for.
## Step 2 (2026-08-30, PR #6110) — the bar-weight prune: the OFFSET is forced, not z

`computations/qbeta/qbeta_d_frame_ladder_bar_weight_prune.py`. This is the formalize-first prune this bean's Discipline section asks for, done before any numerical re-fit.

**Two recorded forms are ONE fact.** This bean records `bar(z_D) = q^-4·z_D`; PR #6110 measured `bar(z_D) = z_D − h`. Both are correct and equal `1/(q³+q)`. Recorded because they read as competing parity claims.

**z is bar-HOMOGENEOUS in BOTH conventions** — `bar(z_C)/z_C = 1` (weight 0), `bar(z_D)/z_D = q^-4` (weight −4). So "bar-even" is not something C has and D lacks; it is weight 0. The KC13 statement is the weight-0 instance of a two-case fact.

**What breaks under D is the AFFINE OFFSET, not z.** With `h` bar-odd:

    C:  bar(alpha)/alpha = -1                            bar-ODD, clean
    D:  bar(alpha)/alpha = (q^3+q-1)/(q(q^3-q^2-1))      NOT an eigenvector

`z_D` has weight −4, the constant `1` has weight 0, and a sum of two bar-weights is never an eigenvector. **The `−1` is the obstruction.** That is a structural explanation for this bean's own sensitivity row (`c_3 → −974`, "no convergence"): the naive swap keeps a weight-mismatched offset and destroys the grading the C ladder's convergence rests on.

**THE PRUNE.** For `(z − c)h/2` to be bar-anti-homogeneous, `c` must carry z's bar-weight. For `c = q^n`, `bar(c)/c = q^{-2n}`:

    C: weight  0 => n = 0 => c = 1     bar(alpha)/alpha = -1     <- DERIVES the existing ladder
    D: weight -4 => n = 2 => c = q^2   bar(alpha)/alpha = -q^-4

The rule reproduces C's offset rather than assuming it — the consistency check that makes it worth stating.

**NOT established:** that `c = q²` IS the D offset. Only that bar-homogeneity FORCES weight −4, uniquely `q²` among monomials. What replaces `tr_M(1) = 1` in the D normalisation is open. A `q²` reached by search would be a fit; this is reached by grading. No `c_k` proposed, extracted or wired.

Complements Step 1: that proved the ADDITIVE defect forms; this is the MULTIPLICATIVE (eigenvector) reading, and it is the one that prunes the offset class.

## Step 3 (2026-08-30) — the open half of Step 2 is ANSWERED, and it CLOSES the repair

`computations/qbeta/qbeta_trm_identity_normalisation_under_d.py`.

Step 2 left exactly one thing open: *what replaces `tr_M(1) = 1` in the D normalisation.* **Answer: nothing.**

`tr_M(1) = Σ_λ y_λ·f^λ` on the convention-D Wenzl weights, exact rationals: **== 1 EXACTLY at all 12 rows** (s = 3/2, 7/5, 13/9 × n = 2..5). It holds even though every ℓ(λ) ≥ 3 block VANISHES under D — the surviving two-row blocks carry the whole normalisation.

**But it is IMPOSED, not derived.** `markov_trace_s` seeds the recursion with `tr = {1: {(0,): Fraction(1)}}`. The twelve hits establish that the imposed normalisation and the D block weights are CONSISTENT — and that the vanishing ℓ ≥ 3 blocks do not break it — not that `tr_M(1)` must be 1 under D. It is a normalisation carried unchanged across the convention, not a quantity the convention determines.

**Consequence: the natural repair is CLOSED.** Step 2 forced the phase offset to bar-weight −4 (uniquely q² among monomials). The hope was that the D normalisation would supply something of weight −4 in place of the `1`. It does not — `1` has bar-weight 0 in both conventions. So IF the offset is the trace normalisation, **no offset-reinterpretation can make the D phase bar-homogeneous**, and the ladder must be rebuilt on a principle other than bar-homogeneity of `α = (z−1)h/2`.

**The one link NOT established, and the cheap next step.** The `1` in `α = (z−1)h/2` is a **bare literal** at `qbeta_utils.py:255`. That it IS `tr_M(1)` is the reading under which the verdict follows; this probe does not prove it. Settling that provenance is cheap and decides which of two paths the re-derivation takes — if the `1` has a different origin, the weight-0 argument does not bind it and the offset question reopens.

Consistent with the corpus already treating this as unresolved: `qbeta_utils.py` WITHHOLDS `z` and `alpha` under D behind a guard citing the proved invalidity of substituting `z_D` here. No `c_k` proposed, extracted or wired.

## Step 3 CORRECTION (same session) — the link is settled and it is FALSE

Step 3 above flagged the `tr_M(1)` reading as unproved and said settling it would decide the path. **Settled, and it goes the other way.**

`folio/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.md:21`:

> `α = (z−1)h/2` is the single-wrap **eigenphase on V_(2,1)** (per `prop:q-beta-spectral-bridge`)

So the `1` is an artifact of an eigenphase computation on the 2-dim Wedderburn block, **not** the trace normalisation. The weight-0 argument does not bind it, and **"the offset repair is CLOSED" is RETRACTED.** The offset question is REOPENED.

**What survives, unaffected:** the measurement. `tr_M(1) = 1` is preserved exactly under D at all 12 rows, is imposed rather than derived, and nothing replaces it. That answers what Step 2 asked; it simply lacks the consequence Step 2's framing expected, because Step 2 mis-identified which `1` sits in the phase.

**Sharpened next step, and it is narrower than "re-derive the ladder".** From `beta-decay-transfer-matrix-proof.md`, the phase factors as `(z − 1)·(h/2)` where `h/2` is the β-decay transfer-matrix shift `Δ_β = (h/2)·𝕀` — built from `h` alone, so **z-free and convention-INDEPENDENT**. All convention dependence sits in `(z − 1)`. The D phase therefore comes from re-deriving the single-wrap eigenphase on V_(2,1) under the D trace, from `prop:q-beta-spectral-bridge` — not by substituting `z_D`, and not by adjusting the offset to weight −4.

**Also noted:** `computations/probes/probe_alpha.py` substitutes `z_D` into `α = (z−1)h/2` and calls it "the canonical convention", while `qbeta_utils.py:172` WITHHOLDS `α` under D because that substitution is "proved invalid". The probe is inert (no consumers, no witness) and its Taylor expansion of a formal expression is defensible, but the two files read as disagreeing and a reader could quote the probe.

## Step 4 (2026-08-30) — WHAT breaks under D is now precisely located: the cosine loses its justification

Traced the phase to its authority. Two corrections to my own Step 3 correction, and then a much stronger result.

**(a) The `1` is not an eigenphase offset either — the ladder block and its authority describe it differently.** `q-beta-categorical-precision-ladder.md:21` calls `α = (z−1)h/2` "the single-wrap eigenphase on V_(2,1)". `prop:q-beta-spectral-bridge` derives it as the **first-order term of a ratio**: `Q^A/Q^B = 1 + (z−1)h/2 + O(h²)`. Both are right — `q-beta-cos-resummation` is the block that connects them, and it says so explicitly: it *replaces* the linear bridge correction with `cos((z−1)h/2)`, and separately identifies α as the eigenphase of M_β, whose spectrum on V_(2,1) is `{e^{+iα}, e^{−iα}}`.

**(b) THE RESULT. The cosine's justification is that α is BAR-ODD — and under D it is not.** Quoting the theorem's own constraint 1:

> Markov cyclicity. The trace is cyclic. It is invariant under the bar involution q ↦ q⁻¹, which maps **α ↦ −α**. The resummation must be **even in α**. The minimal even-power resummation that matches the linear bridge is the cosine.

Measured (Step 2, this session): `bar(α_C)/α_C = −1` **exactly** — α IS bar-odd under C, so `α ↦ −α` holds and the evenness requirement is satisfied by `cos`. Under D, `bar(α_D)/α_D = (q³+q−1)/(q(q³−q²−1))` — not −1, not even constant in q. **So under convention D, α ↦ −α FAILS, the trace-symmetrization argument does not apply, and the cosine form loses the structural justification the theorem gives for it.**

That is much sharper than Step 2's "the bar grading is destroyed". It names the exact load-bearing step that fails: constraint 1 of the cos-resummation theorem, which is the theorem's own stated reason for the cosine rather than some other even resummation.

**(c) Two content blocks carry live convention-C `z` in their own statements**, and they are the upstream authority for the entire ladder phase:
- `nuclear-interactions/q-beta-spectral-bridge.md` — "We define the Markov–Jones parameter as z := 1/(√q + 1/√q)"
- `nuclear-interactions/q-beta-cos-resummation.md` — "z = 1/(√q + 1/√q)"

**Consequence for the re-derivation.** The D-frame ladder needs more than a new phase value: it needs a replacement for the *resummation form*. Under C the chain is [α bar-odd] ⇒ [trace symmetrization is even in α] ⇒ [cos is the minimal even resummation]. Under D the first link is gone, so neither the cosine nor its minimality survives, and the D re-derivation must establish what the M_β spectrum on V_(2,1) is under the D trace and what evenness (if any) the D bar involution imposes.

## Step 5 (2026-08-30) — the D weights in closed form, and the carrier block SURVIVES

Solved the H₃ Wedderburn system with `z` free and specialised to D. The weights collapse to closed forms of striking simplicity (against convention C's half-integer-power mess):

    y_(3)   = (q^4 + 1)/(q^2 + 1)^2
    y_(2,1) = q^2/(q^2 + 1)^2
    y_(1^3) = 0                      IDENTICALLY, all q

Three results at once:

1. **The radical is confirmed symbolically for all q**, not just at sampled s — `y_(1³) ≡ 0` is an identity. (Step 4 and the PR #6110 Wenzl run had it only at sampled rational s.)
2. **Step 3 upgrades from 12 sampled rows to an identity**: `Σ_λ y_λ f^λ = (q⁴+1)/(q²+1)² + 2q²/(q²+1)² = (q²+1)²/(q²+1)² = 1` **for all q**. `tr_M(1) = 1` under D is now proved, not sampled.
3. **THE LADDER'S CARRIER BLOCK SURVIVES D.** `y_(2,1) = q²/(q²+1)²` has numerator `q²`, whose only real root is q = 0 — so it is **nonzero for every q > 0**. V_(2,1), the block the whole eigenphase/cos-resummation construction lives on, is NOT in the D radical.

That third point is the one that matters for planning: **the D re-derivation is not futile.** Had V_(2,1) been in the radical the entire ladder would be dead under D and the only honest move would be to abandon it. It is not; the carrier survives, the weights are simple, and what needs replacing is the resummation FORM (Step 4) rather than the object it acts on.

## Step 6 (2026-08-30) — the bridge phase is GENERIC in z; the D target is narrower than the guard reads

`computations/qbeta/qbeta_d_frame_bridge_generic_z.py`.

**Where z enters, measured.** `beta-decay-transfer-matrix-proof.md` gives T_pp, T_nn, T_mix and Δ_β explicitly, and **all four are z-FREE** (built from `h` alone) — verified by symbolic differentiation. So M_β as an OPERATOR is convention-independent. `z` enters in exactly two downstream places, both trace/normalisation:

    Vhat_i = z·M_11 + M_21              the Markov trace on a 2x2 (z-linear)
    Q^B    = ln(Vhat_dau/Vhat_par)·E_0/z

**The result.** Re-derived the bridge with `z` carried as a FREE symbol (Vhat_pp = z·h+1, Vhat_nn = 1, Q^A/E_0 from `prop:neutron-qvalue-symbolic` over E_0 = m_e/(q(q−1))), expanded about q = 1+w:

    w^0 : 1
    w^1 : z − 1                          <- matches the corpus's (z−1)h/2 EXACTLY
    w^2 : −z²/3 − 3z/2 + 1/2             } NEW — the corpus records only
    w^3 : z³/3 + 2z²/3 + 3z/2 − 1/2      }  first order plus O(h²)

**So `α = (z−1)h/2` is the GENERIC-z result, not a convention-C specialisation.** Nothing in the bridge derivation privileges z_C.

**Scope — and the guard is NOT wrong.** `qbeta_utils.py`'s KeyError says *"substituting z_D into alpha = (z−1)h/2 is proved invalid by decayLadder_zC_threeRow_ne_zero and eigenphase_bar_defect_of_fullBar"*. Those two Lean results are about the **ladder's three-row forcing** and the **bar defect** — not about whether the bridge's first-order coefficient is generic. The sentence is correct for the ladder. What this adds is the split:

| object | status under D |
|---|---|
| bridge term `(z−1)h/2` | **generic in z** → z_D substitution legitimate |
| cos resummation `cos α` | justified by α bar-odd (Step 4) → **FAILS** |
| c_k ladder | C-frame → **FAILS** |

So the D re-derivation target is the **resummation form + the ladder**, not the phase formula — strictly narrower than "re-derive the ladder from scratch". **The guard should stay exactly as it is**: it withholds z/α unless a convention is NAMED (a visibility mechanism) and already serves `convention='D'`. Nothing here asks for it to be loosened.

**Values at the proton pin:** α_C = −0.0523361202682285, α_D = −0.0404857773406426. Recorded as generic-formula values, NOT wired ladder inputs. No c_k proposed, extracted or wired; c_3 ≈ −974 remains a sensitivity measurement.

**I also corrected my own reading twice here.** I had described the guard as "withholding α under D because the substitution is proved invalid" — the withholding is actually of UNNAMED access, and D is served. And the quoted sentence is in the KeyError, not the docstring; my quote was accurate, my characterisation of its scope was not.

## Step 7 (2026-08-30) — WHY the cosine fails: the bar action itself changes shape

`computations/qbeta/qbeta_d_frame_bar_action_on_traced_volume.py`. Step 4 saw the *symptom* (α not bar-odd under D). This derives the *cause*, from the group action.

**The phase is a re-centred traced volume.** With `V̂ = z·h + 1` (the Markov trace on the pp transfer matrix), verified for BOTH conventions:

    alpha = (z-1)h/2 = (Vhat - 1 - h)/2        EXACT identity

**The bar involution acts completely differently in the two conventions** — different group actions, not different values of one:

    C:  bar(Vhat) = 2 - Vhat        AFFINE REFLECTION, fixed point 1
    D:  bar(Vhat) = Vhat / q^2      MULTIPLICATIVE eigenvector, weight -2

Under C bar fixes the centre 1 and negates h, so `V̂ − 1 − h` is bar-ODD and α inherits `α ↦ −α`. Under D bar does not fix 1 — it scales — so the centring buys nothing: `bar(α)+α = (q−1)²(q+1)²/(2q²) ≠ 0`.

**No constant re-centring repairs it.** Solving for the offset `c` making `V̂ − c − h` bar-odd under D gives `c = (q⁴+1)/(2q²)` — which is exactly the **bar-midpoint** of V̂, and is q-dependent. A q-dependent offset is not a re-centring of the phase, it is a different object. Independently confirms Step 2's bar-weight argument, reached there from weights rather than from the action.

**THE RESULT.** `cos α = (e^{iα}+e^{−iα})/2` is precisely the **ADDITIVE** symmetrisation. Measured:

    C:  bar(Vhat) + Vhat = 2                    CONSTANT in q
    D:  bar(Vhat) + Vhat = (q^4+1)/q^2          NOT constant
        bar(Vhat) * Vhat = (q^4+1)^2/(q^2(q^2+1)^2)   NOT constant

Under C the additive bar-symmetrisation of the traced volume is a **constant**. That is the precise sense in which the additive/cosine structure belongs to convention C: the bar action is affine, so additive symmetrisation is the invariant and the cosine is its trigonometric realisation. Under D the action is multiplicative, so **no additive form — cosine included — can be the minimal invariant.**

**What it does NOT establish:** the replacement form. It fixes the CLASS (multiplicative in the bar action) and closes the additive route, from the group action rather than by search. Naming the form still needs the D-frame M_β spectrum on V_(2,1). No c_k proposed, extracted or wired.

## Step 8 (2026-08-30) — the sharpest statement: under D there is NO FIXED CENTRE to resum around

Same probe, extended. Step 7 showed the bar action changes from affine to multiplicative. This asks what each action's **invariant** is, which is what a resummation needs.

**Which q-power makes V̂ bar-invariant?**

    C:  NONE          an affine reflection has a FIXED POINT, not a weight
    D:  q^(-1) only   -> Vhat_D/q = (q^4+1)/(q(q^2+1))   bar-invariant, UNIQUE

**And the decisive difference is whether the invariant is CONSTANT:**

    C invariant = (Vhat + bar Vhat)/2 = 1              CONSTANT
    D invariant = Vhat/q = (q^4+1)/(q(q^2+1))          NOT constant

**Closed form for the D invariant** (derived, verified exactly):

    Vhat_D / q  =  ( [2]_q + h^2 · z_D / q^2 ) / 2,      [2]_q = q + 1/q

At the proton pin: [2]_q = 2.01089686670712230, h²z_D/q² = 0.0217346842874601, V̂_D/q = 1.01631577549729119.

**THE SHARPEST STATEMENT of why cos is C-only.** A resummation needs something to be centred on. Under C the bar-invariant is the **constant 1** — a fixed centre — and `cos` is the additive resummation about it. Under D the invariant is `V̂/q`, which **moves with q**: there is no fixed centre, so no additive resummation has anything to be centred on. That is stronger than Step 7's "the action is multiplicative": it names what is missing.

**Still NOT established:** the replacement form. The class is fixed (must respect the multiplicative action; the invariant is `V̂/q`), the additive route is closed, and the closed form above is a derived candidate anchor — but naming the form needs the D-frame M_β spectrum on V_(2,1). No c_k proposed, extracted or wired.



## (D1) IS LEAN-PROVED (PR #6211) — and this bean's own next-step note over-states what was missing

The entry above says "The concrete next step is therefore narrower than
'derive alpha': Lean-prove (D1)". Correct in direction, but the scope is
smaller again, and the corpus-grep is why.

### The analytic core has existed since 2026-06-16

QOU/Interactions/qbeta_counit_vs_trace.lean already carries, TWO AND A HALF
MONTHS before this bean asked for it:

    epsNP h     = h^2/2 - h        the Frobenius counit of Delta  (= net)
    trMNP h z   = h^2/2 - h*z      the Ocneanu trace of Delta
    eps_sub_trMNP : epsNP h - trMNP h z = h*(z-1)      the exact gap
    agree_iff     : for h != 0, the two agree iff z = 1

I wrote a first draft that re-derived all four under new names before grepping.
Deleted; #6211 imports them instead. Recording it because the bean's phrasing
invites exactly that duplication: "Lean-prove (D1)" reads as from-scratch work
and it is not.

### What was genuinely missing: the alpha bridge

That file relates the counit to the trace and NEVER MENTIONS alpha. So it never
says the gap IS twice the rung-1 phase — which is the whole content of (D1) and
the step that upgrades alpha from bare def to derived.

Neither existing alpha closes it:
  EigenphaseCarrierVacuity.eigenphase  built on markovZC — pinned to the
                                       EXCISED convention C
  BraidImageEigenphaseExclusion.alphaOf  R-valued AND function-valued
A claim holding "identically in q and z" needs the free form over a general
field. That is what #6211 adds.

### The three theorems (sorry-free, axioms propext/Classical.choice/Quot.sound)

  rungOnePhase_eq_counit_sub_trace    2*alpha = epsNP - trMNP          (D1)
  generatorWeight_forced              with the sigma-weight left UNKNOWN as w,
                                      (D1) holds IFF w = z. The falsifiable
                                      content: the phase PINS the Markov
                                      parameter rather than merely agreeing
                                      with it. This is the precise form of
                                      "z enters the ladder in exactly one
                                      place", and it is what stops (D1) from
                                      being arithmetic on chosen constants.
  generatorWeight_unpinned_at_classical
                                      sharpness: at h = 0 the weight is
                                      unpinned — (D1) holds for EVERY w. Same
                                      degeneracy this bean records elsewhere
                                      when warning that a theorem evaluated
                                      only at q = 1 is convention-agnostic by
                                      accident.

### Characteristic two is a REAL hypothesis

2*(x/2) = x fails when 2 = 0, so (D1)'s left side is identically 0 in char 2
while the gap need not be: the identity is FALSE there and (2 : K) != 0 is
required. My first attempt omitted it and `ring` refused — that refusal was
mathematics, not a syntax error. The imported lemmas do NOT need it (in
epsNP - trMNP the h^2/2 cancels first); it enters with alpha's uncancelled /2.
The classical-point lemma does not need it either, so it is DROPPED there
rather than carried unused, which makes that lemma strictly stronger.

### Scope

Delta's NF coordinates are INPUT, not proved — rebuilt from typed-crossing
words by qbeta_d_frame_rung_one_rederivation_probe.py and already encoded in
the imported defs. Identification remains the sibling's (PR #5337 comment
5421747260, bean qou-avt5); the exact derivation incl. the factor of 2 is that
probe (PR #5864).

NO convention is assumed: z free throughout, nothing substituted. This does NOT
touch the resummation question — Steps 6-8 landed while I was working and Step
8's "no fixed centre under D" is untouched by this.

### What this does and does not change for the ladder

alpha is now DERIVED in Lean rather than a bare def, which was the bean's
stated goal for this step. It does not produce a c_k, does not re-derive the
ladder, and does not reopen the additive-resummation route Step 8 closed. The
status line above should now read alpha: DERIVED (probe) + FORMALIZED (#6211),
where it previously read "NOT formalized in Lean, where it remains a bare def".



## The offset is the BAR-MIDPOINT — and one rule derives C's `1` too (PR #6211)

Owner authorised duplication ("duplicate ok", 2026-08-30). This walks at
Steps 7/8 from a different direction and lands on a WEAKER conclusion than
Step 8's. Probe: `computations/qbeta/qbeta_d_frame_bar_midpoint_offset_probe.py`,
12/12, sympy exact, no float64 (verified: 0 hits in f64-into-mpmath and
raw-float64; the file imports only sympy).

### The measurement

  * `(q^4+1)/(2q^2)` — the offset Step 7 solves for — is NOT an arbitrary
    function of q. It is `(q^2 + q^-2)/2`, the BAR-MIDPOINT `(Vhat + bar Vhat)/2`,
    i.e. `cosh(2 log q)`.
  * Under C the bar-midpoint is the CONSTANT `1`. So the single rule
    **offset := bar-midpoint** DERIVES convention C's offset instead of
    assuming it, and hands D its `(q^2+q^-2)/2`. C's `1` is `cosh(0)`.
  * The midpoint-built phase `(Vhat - midpoint - h)/2` is bar-ODD in BOTH
    conventions.
  * Under C it reproduces the KNOWN `alpha` exactly — so it is not a new object
    there, it IS `alpha` re-derived. Under D it DIFFERS from the naive z-swap,
    which is what makes it a candidate rather than a restatement.

That is the same consistency test Step 2's bar-weight argument passed — a rule
that only described D could be tuned to say anything — applied to the OFFSET
rather than the weight.

### What this changes, and what it does not

**Step 8's "no FIXED centre" is CONFIRMED**, explicitly, by check 5:
`d/dq` of the D midpoint is nonzero. Not overturned, and I am not claiming to.

**Step 7's "a q-dependent offset is not a re-centring of the phase, it is a
different object" is too strong as stated.** It IS the same object; its VALUE
is constant in C and q-dependent in D — exactly as the bar-weight is 0 in C
and −4 in D. Both are two-case facts about one construction, not a structure
C has and D lacks. This bean already makes that correction once, for
bar-homogeneity ("'bar-even' is not something C has and D lacks; it is weight
0"). The offset is the same shape of correction, one line down.

So: **"no fixed centre" stands; "nothing to be centred on" does not follow
from it.**

### What is still open — unchanged

The replacement FORM. Naming a centre does not exhibit a resummation about it,
and `cos` remains the wrong realisation because the action is multiplicative.
NO `c_k` is proposed, extracted or wired. Scope (a): one object (`Vhat`), two
conventions, symbolic.

The concrete next question this leaves is narrower than Step 8's: not "what
replaces the cosine" in general, but **what resums about a centre that moves as
`cosh(2 log q)`** — a named, derived, q-dependent centre rather than an absent
one.



## The replacement FORM, named: resum `log Vhat`, not `Vhat` (PR #6211)

Step 8 leaves this open in as many words — *"The replacement FORM. The class is
fixed ... the additive route is closed ... but naming the form needs [more]."*
Probe: `computations/qbeta/qbeta_d_frame_log_coordinate_form_probe.py`, 11/11,
sympy exact.

### The move

Work in `theta = log q`, where the bar involution is simply `theta -> -theta`.
Every bar statement becomes a PARITY statement in theta, and the two conventions
stop looking like different phenomena.

### Closed forms, derived not assumed

    C:  Vhat = 1 + 2 sinh(theta/2)
             = bar-EVEN CONSTANT  +  bar-ODD term            ADDITIVE

    D:  Vhat = e^theta * cosh(2 theta)/cosh(theta)
             = bar-ODD MONOMIAL   *  bar-EVEN factor         MULTIPLICATIVE

D's even factor is `(q^2+q^-2)/(q+q^-1) = [2]_{q^2}/[2]_q` — a **ratio of
q-integers**, not a generic function of q.

### Why this answers the form question

`cos` is not a generic resummation. It is the one adapted to C's shape: a SUM
whose bar-odd part sits on a fixed centre. D has no such sum. The object adapted
to a PRODUCT is the LOGARITHM:

    log Vhat_D  =  theta  +  [ log cosh 2theta - log cosh theta ]
                   ^odd       ^--------- even ---------^

So the D-frame ladder should resum `log Vhat`, not `Vhat`. In that coordinate
the bar-odd part is exactly `theta = log q`, and the bar-even remainder is a
series in `theta^2` — equivalently in the `q^{2k}`-integers.

### It absorbs the "moving centre"

The bar-midpoint `cosh(2 theta)` — Step 7's q-dependent offset, identified as
the bar-midpoint in the previous entry — is exactly the NUMERATOR of D's
bar-even factor. So the moving centre is not a separate obstacle: it is one half
of the multiplicative decomposition, and it moves *because* the decomposition is
multiplicative rather than additive. Two entries that arrived separately are one
fact.

### Step 8 is CONFIRMED, not overturned

There is no fixed centre for an ADDITIVE resummation of `Vhat`, and that is
exactly why the additive form fails. What is added here is the positive half —
the coordinate in which the structure is visible — not a contradiction.

### Not claimed

No `c_k`. Naming the coordinate and the parity structure is not exhibiting the
ladder; the series coefficients are untouched and nothing is wired. Scope (a):
one object (`Vhat`), two conventions, symbolic.

### The next question, now sharper again

Not "what replaces the cosine" (answered: the log), and not "what resums about a
moving centre" (dissolved: the centre is the even factor's numerator). It is:
**what are the coefficients of `log Vhat_D`'s bar-even remainder in the
`q^{2k}`-integer basis, and do they reproduce the ladder's rung structure?**
That is a concrete symbolic expansion, and it is the first form of this question
that does not presuppose an additive shape.



## `u` and `Vhat` carry OPPOSITE bar-weights — `u*Vhat` is invariant (PR #6223)

Follows the log-coordinate entry above. That one asked what `Vhat` does under
bar; this asks what the LADDER'S OWN expansion variable does, which the corpus
does not state anywhere. Probe:
`computations/qbeta/qbeta_d_frame_u_vhat_bar_pairing_probe.py`, 8/8, sympy exact.

    object      bar-weight   q-integer form
    u            +2          sqrt([3]_{q^2})/[2]_q * hbar_q^2
    Vhat_D       -2          q * [2]_{q^2}/[2]_q
    u * Vhat_D    0          BAR-INVARIANT

### The pieces, each verified

* **`b = sqrt([3]_{q^2})/[2]_q`.** The Hoefsmit `b` is a RATIO OF q-INTEGERS:
  `q^4+q^2+1 = q^2*[3]_{q^2}` and `q^2+1 = q*[2]_q`, so the powers of q cancel.
  It is not written that way anywhere in the corpus — `_h4_route_ladder_scan.py:25`
  carries it as `sqrt(q**4+q**2+1)/(q**2+1)`.
* **`b` is bar-EVEN** — `[2]_x` and `[3]_x` are each invariant under `x -> 1/x`.
* **`hbar_q` is a bar-eigenvector**: `bar(hbar) = -q*hbar`. So `hbar^2` carries
  `q^2`, and with `b` even, `u` has bar-weight **+2** — exactly minus `Vhat`'s.
* **The additive counterpart does NOT cancel**: `u + Vhat` is not invariant. The
  cancellation is specifically MULTIPLICATIVE, matching the multiplicative
  action Step 7 identified.
* **`b` and `Vhat_D/q` share the `[2]_q` denominator**, so it cancels in their
  ratio: `(Vhat_D/q)/b = [2]_{q^2}/sqrt([3]_{q^2})` — a pure q^2-object.

### Why it matters

A resummation needs a bar-invariant to organise around. Step 8 showed the D
invariant `Vhat/q` is not CONSTANT, which is what closes the additive route.
This exhibits a DIFFERENT invariant — one built from the ladder's own variable
rather than from `Vhat` alone. The weights permit an organising object that
`Vhat` by itself does not supply.

### What it is NOT

Not a resummation. No series exhibited, no `c_k` proposed, extracted or wired,
and nothing here shows the ladder MUST be organised this way — only that the
bar-weights permit it. **Step 8's closure of the ADDITIVE route is untouched and
remains correct.** Under C the question does not arise: the action is affine
there and weights are not what organises it. Scope (a).

### Where this leaves the arc

Four entries now, in one direction:

  1. (D1) Lean-proved — `alpha` is DERIVED, not a bare def.
  2. The D offset is the BAR-MIDPOINT; one rule gives C's `1` and D's `cosh(2t)`.
  3. The form is MULTIPLICATIVE — resum `log Vhat`, not `Vhat`.
  4. `u` and `Vhat` have opposite bar-weights; `u*Vhat` is invariant.

Each is scope (a) and none proposes a `c_k`. The next question is whether the
invariant in (4) is the thing the ladder's rungs actually expand in — i.e.
whether `log(u*Vhat)` or `u*Vhat` has a series whose coefficients reproduce the
rung structure. That is a concrete symbolic expansion and it is the first
version of the question that has a bar-invariant to expand ABOUT, which is what
Step 8 said was missing.



## `alpha_eff`'s bar-defect: D's is u-INDEPENDENT — the series is the wrong tool (PR #6223)

A NEGATIVE on my own hypothesis, plus a sharpening. Both recorded so neither is
re-walked. Probe:
`computations/qbeta/qbeta_alpha_eff_bar_defect_order_probe.py`, 9/9, sympy exact.

### The hypothesis, and its refutation

Having found that `u` has bar-weight +2 while `Vhat` has −2, I guessed the
ladder's `− u/2` term might be exactly the bar-correction repairing `alpha`
under D. **It is not.**

The ladder uses `alpha_eff = alpha − u/2`, not `alpha`
(`Q_N1 = Q_A*cos(alpha_eff)`, `_h4_route_ladder_scan.py:26`):

    convention   bar(alpha)+alpha       bar(alpha_eff)+alpha_eff
    C            0       (bar-ODD)      -u*(q^2+1)/2
    D            (q^2-1)^2/(2q^2)       (q^2-1)^2/(2q^2) - u*(q^2+1)/2

### My first reading of that was ALSO wrong

Seeing "`alpha_eff` is bar-odd in NEITHER frame", I took it to mean C's clean
bar structure does not survive to the object the ladder actually evaluates —
i.e. that Step 7 describes `alpha` but not the ladder. **Wrong.** Under C the
residual is EXACTLY `−u*(q^2+1)/2`, a RATIONAL multiple of `u`: the bar-oddness
fails precisely at the order of the correction term that caused it. That is what
a truncated series does, and it is not a defect.

### What is actually there

The `− u/2` term's own bar-defect is CONVENTION-INDEPENDENT — the same
`−u*(q^2+1)/2` in both frames. What differs is what it is added to:

    C:  residual = O(u)                      vanishes with truncation order
    D:  residual = (q^2-1)^2/(2q^2) - O(u)   carries a u-INDEPENDENT piece

Verified by the surd: `residual/u` is rational in q under C (`−(q^2+1)/2`, no
surd) and retains `sqrt(q^4+q^2+1)` under D — precisely because the D residual
has a part not proportional to `u` at all.

### The sharpening

D's obstruction is **not** "the phase has a bar-defect" — C's does too,
harmlessly. It is that **D's defect does not live in the series**, so no order
of ladder correction removes it and the correction series is the wrong
instrument. That takes Step 7 from a statement about `alpha` to one about the
LADDER.

It also explains, structurally, the sensitivity row this bean already records
(`c_3 -> -974`, "no convergence"): fitting a series against a defect the series
cannot represent is what that number looks like.

### Symbol collision, worth flagging

`alpha_eff` is OVERLOADED. `qbeta_multi_block_eigenphase_probe.py` uses it for a
dimension-weighted block average — a different object. This probe means the
ladder one (`alpha − b*hbar^2/2`).

### Not claimed

No `c_k`, no replacement phase. Steps 7 and 8 untouched. Scope (a).



## The un-removable defect IS `h^2/2` — and it is built from the ladder's own `b`

Identifies the u-independent piece the previous entry left unnamed. Probe:
`computations/qbeta/qbeta_d_bar_defect_is_h_squared_probe.py`, 8/8, sympy exact.

    bar(alpha_D) + alpha_D  =  h^2/2  =  ([3]_{q^2} - 3)/2  =  ((b*[2]_q)^2 - 3)/2

`alpha_C` has NO such defect (it is bar-odd), so this is D-specific.

### The link

The Hoefsmit `b` — which defines the ladder variable `u = b*hbar_q^2` — is
`sqrt([3]_{q^2})/[2]_q` (established earlier in this arc). So
`(b*[2]_q)^2 = [3]_{q^2}`, and the defect is `((b*[2]_q)^2 - 3)/2`.

**The same q^2-integer governs both the ladder's expansion variable and the
defect the ladder cannot remove.**

### Why that matters

The order result says the defect does not live in the series. One might then
expect it to be something external to the construction. It is not: it is
`h^2/2`, the most elementary invariant in the algebra, expressible in the
ladder's own `b`. So D does not introduce an alien obstruction — the same
ingredient enters at a place the correction series cannot reach. That is a
sharper account of why the series is the wrong instrument than "the defect does
not live in the series": it says WHICH object it is and where it comes from.

### A notation trap, recorded because it caught me

AGENTS.md writes `h_A^2 = [3]_q - 3`. With the symmetric convention
`[3]_x = x + 1 + 1/x` that is **FALSE at argument q** (giving `q - 2 + 1/q`) and
**TRUE at argument q^2**. My first test used the literal argument `q` and
returned a false negative on the corpus's own identity. The corpus is right; the
argument is `q^2`. The probe asserts both the true and the false form so the
trap is on record rather than re-discovered.

### Not claimed

A repair, a replacement phase, or any `c_k`. Naming an obstruction is not
removing it. Steps 7 and 8 untouched. Scope (a).

### Where the arc stands — six entries
## D's bar-odd slot is EMPTY OF CONTENT — no cos-type phase can express it (PR #6244)

Closes the follow-up the previous entry left open: can the log form absorb the
`h^2/2` defect? **No**, and for a structural reason rather than a failed search.
Probe: `computations/qbeta/qbeta_d_odd_content_is_structure_free_probe.py`,
5/5, sympy exact.

    odd(log Vhat_D) = log q                     EXACTLY
    odd(log Vhat_C) = z-dependent, NOT log q

Under D the log frame DOES supply a bar-odd object — but it is `theta = log q`,
carrying no `z`, no Markov data, nothing convention-specific. ALL of D's
structure sits in the bar-EVEN part (the cosh-ratio `[2]_{q^2}/[2]_q`).

Under C the position is reversed: `Vhat_C - 1 = 2 sinh(theta/2)` is a bar-ODD
eigenvector AND carries the convention's data.

### The consequence

`cos(phase)` is bar-invariant only when the phase is bar-ODD.

  * **C**: such a phase exists and carries structure — a cosine has something
    to resum.
  * **D**: every bar-odd object available from `Vhat` is structure-free. So NO
    bar-odd phase can carry D's structure, and therefore no cos-type
    resummation of a phase can express it, **whatever offset is chosen**.

Stronger than Step 7 ("the offset must be q-dependent") and than Step 8 ("no
fixed centre"): those say the additive repair is awkward. This says the bar-odd
slot is EMPTY OF CONTENT, so there is nothing for a phase to be.

### Honesty about what is new

`odd(log Vhat) = log q` is EQUIVALENT to Step 7's `bar(Vhat) = Vhat/q^2` — take
logs of both sides. A restatement in log coordinates, NOT an independent
discovery; the probe asserts it as such. Only the consequence is new.

### A discarded test, recorded so it is not repeated

I first substituted a generic CONSTANT `zz` for `z` to find which `z` collapses
the odd part to `log q`. That test is MEANINGLESS: it treats `z` as
bar-invariant when `z` is a function of `q` and `bar` acts on it. Any conclusion
from a constant-`z` substitution here is void. Dropped before it reached a claim.

### Not claimed

That no D-frame resummation exists — only that no cos-of-a-bar-odd-phase one
does. The multiplicative/log route and the `u*Vhat` invariant are untouched by
this negative. No `c_k`. Scope (a).

### Where the arc stands — seven entries

  1. (D1) Lean-proved — `alpha` is DERIVED, not a bare def.
  2. The D offset is the BAR-MIDPOINT; one rule gives C's `1` and D's `cosh(2t)`.
  3. The form is MULTIPLICATIVE — resum `log Vhat`, not `Vhat`.
  4. `u` and `Vhat` carry opposite bar-weights; `u*Vhat` is bar-invariant.
  5. D's bar-defect is u-INDEPENDENT — the correction series cannot reach it.
     (Includes two recorded wrong turns of mine.)
  6. That defect IS `h^2/2 = ((b*[2]_q)^2 - 3)/2` — built from the ladder's own `b`.

None proposes a `c_k`; all are scope (a). Taken together they say: the D-frame
ladder fails not because a coefficient is wrong but because the correction
series is the wrong instrument for an obstruction that is `h^2/2` and sits
outside it. The next question is whether the multiplicative/log form (3) plus
the invariant `u*Vhat` (4) can absorb `h^2/2` — i.e. whether an instrument
exists that reaches it.
## Step 9 (2026-08-30) — Steps 6-8 are now LEAN-PROVED, sorry-free

`folio/quantum-observable-universe/lean/QOU/QBeta/DFrameBarAction.lean`. Eleven theorems, `lean`-direct **exit 0**, `#print axioms` clean on all eleven (`propext, Classical.choice, Quot.sound`; **zero sorryAx**). No `sorry`, no `axiom`, no `native_decide`, no `: True`.

Stated over a generic `Field K` per §7c — no `ℝ`, no `Real.sqrt`. Convention C is carried in the square-root variable `u` (`q = u²`), which keeps it algebraic in the same generic setting.

| theorem | content |
|---|---|
| `bridgePhase_eq_recentred_tracedVolume` | `α = (V̂ − 1 − h)/2` for EVERY z — no hypothesis; this is why the phase formula is convention-independent |
| `hq_bar` | `h(q⁻¹) = −h(q)` |
| `zD_bar` | `z_D(q⁻¹) = z_D(q)/q⁴` — weight −4 |
| `tracedVolume_D` | `V̂_D = (q⁴+1)/(q²+1)` |
| **`tracedVolume_D_bar`** | **`V̂(q⁻¹) = V̂(q)/q²`** — the D action is MULTIPLICATIVE |
| **`tracedVolume_C_bar`** | **`V̂(u⁻¹) = 2 − V̂(u)`** — the C action is an AFFINE REFLECTION |
| `tracedVolume_D_invariant` | `V̂/q` is bar-invariant |
| `tracedVolume_D_invariant_closed_form` | `V̂_D/q = ([2]_q + h²z_D/q²)/2` |
| `bridgePhase_C_bar_odd` | α IS bar-odd under C — the cos-resummation's stated hypothesis |
| `bridgePhase_D_bar_defect` | defect `= (q−1)²(q+1)²/(2q²)` under D |
| `bridgePhase_D_not_bar_odd` | that defect is NONZERO for q ≠ ±1 |

**The hypotheses are genuine, not bookkeeping.** `q ≠ 0` and `q²+1 ≠ 0` are both needed — over a field where −1 is a square (ℂ at q = i) the denominators vanish — and `CharZero` is needed wherever the construction divides by 2, since in characteristic 2 neither the phase nor the closed form is well posed. Proving it forced those out into the open; the Python probes had them implicitly.

**On the M_β spectrum question.** The spectrum claim `{e^{+iα}, e^{−iα}}` on V_(2,1) is the content block's (`q-beta-cos-resummation`), not mine, and I have not re-derived it. What Steps 6-9 establish is that the *phase* α is generic in z (so the spectrum formula carries to D unchanged) and that what fails under D is the *trace symmetrisation* `tr_M(M_β) = cos α` — because bar stops being an affine reflection. So the spectrum is not the open part; the resummation is.
  6. That defect IS `h^2/2 = ((b*[2]_q)^2 - 3)/2` — built from the ladder's own `b`.
  7. D's bar-ODD slot is structure-free — so no cos-type phase can work at all.

Read together, (5)–(7) are a converging negative: the C ladder's instrument
(a cosine of a bar-odd phase, corrected by a series in `u`) fails under D in
BOTH of its parts — the series cannot reach the defect, and the phase slot has
no content to carry. That is a much sharper statement of the obstruction than
"the naive z-swap gives c_3 -> -974".

**The surviving positive lead is (3)+(4)**: the multiplicative/log form, and the
bar-invariant `u*Vhat`. Nothing in (5)–(7) touches either — they close the
ADDITIVE/phase family specifically. Whether `u*Vhat` or `log(u*Vhat)` admits an
expansion whose coefficients reproduce the rung structure is still open, and is
now the only live route this arc has identified.



## The PRODUCT FORM is weight-inhomogeneous under D — and the fix is forced (PR #6244)

Applies the arc's surviving lead (the multiplicative form + the bar-invariant
`u*Vhat`) to the ladder's product form. Probe:
`computations/qbeta/qbeta_d_product_form_grading_probe.py`, 12/12, sympy exact.

    bar(u^k)/u^k          = q^{2k}     weight 2k, verified k = 1,2,3
    bar((u*Vhat)^k)/(..)  = 1          weight 0,  verified k = 1,2,3

    1 + c*u^k          is NEVER a bar-eigenvector — bar(f)/f depends on q for
                       EVERY c, so no coefficient repairs it
    1 + c*(u*Vhat)^k   is EXACTLY bar-invariant for EVERY c

Under D each ladder factor `(1 + c_k u^k)` mixes bar-weight 0 (the `1`) with
bar-weight 2k (the `u^k`). That is the SAME weight-mismatch pathology Step 2
found in the offset, now one level up — **in the product form itself**. It is
the grading that fails, not the coefficients.

The weight-homogeneous form is FORCED by the grading:

        Pi ( 1 + c_k (u * Vhat)^k )

because `u*Vhat` is the bar-invariant. Reached BY GRADING, not by search —
which is what makes it a candidate rather than a fit.

### The C control, without which this would be an overclaim

`u` is convention-INDEPENDENT (`u = b*hbar_q^2`; neither factor involves `z`),
so `1 + c*u^k` is weight-inhomogeneous under C as well. That is **not** a defect
there: C's bar action is AFFINE and weights are not its grading. Confirmed —
`u*Vhat_C` is NOT bar-invariant, so the D repair does not even typecheck under
C. Two-case, like every other result in this arc.

### Not claimed

That `Pi(1 + c_k (u*Vhat)^k)` **is** the D ladder. Only that it is the
weight-homogeneous form. No `c_k` proposed, extracted or wired; no series
evaluated; nothing compared to experiment. A form reached by fitting
coefficients to Q_beta would be exactly what this bean's Discipline section
forbids, and none is attempted. Scope (a).

### Where the arc stands — eight entries

  1. (D1) Lean-proved — `alpha` is DERIVED.
  2. The D offset is the BAR-MIDPOINT; one rule gives C's `1` and D's `cosh(2t)`.
  3. The form is MULTIPLICATIVE — resum `log Vhat`, not `Vhat`.
  4. `u` and `Vhat` carry opposite bar-weights; `u*Vhat` is bar-invariant.
  5. D's bar-defect is u-INDEPENDENT — the series cannot reach it.
  6. That defect IS `h^2/2 = ((b*[2]_q)^2 - 3)/2` — the ladder's own `b`.
  7. D's bar-ODD slot is structure-free — no cos-type phase can work.
  8. The PRODUCT FORM is weight-inhomogeneous; `Pi(1 + c_k (u*Vhat)^k)` is forced.

(5)-(7) closed the phase family. (8) says the *other* half of the C instrument —
the product in `u` — is also wrong under D, for the same grading reason. So both
halves of `Q_A cos(alpha_eff) * Pi(1 + c_k u^k)` fail under D, and in each case
the replacement is dictated by the multiplicative grading rather than chosen.

**The next question is now concrete and non-fitting:** does
`Pi(1 + c_k (u*Vhat)^k)` reproduce the known structural rung `c_2 = -1`? That is
a derivation check against an already-proved value, not a fit to experiment — if
it fails, the forced form is wrong and this route closes too.



## The forced form, worked through: BLOCKED on the N=1 phase — not refuted (PR #6244)

Probe: `computations/qbeta/qbeta_d_forced_form_derivation_probe.py`, 6/6. Two of
the three findings are corrections to my own plan.

### 1 — my proposed test does NOT discriminate

The previous entry said the next check was whether the forced form reproduces
the proved `c_2 = -1`, and called that falsifying. **It is not.** `c_2 = -1`
comes from `N2_factor = 1 - b^2*hbar^4 = 1 - u^2`; its content is that the N=2
factor has the SHAPE `1 - x^2`, and the `x^2` coefficient of `1 - x^2` is `-1`
for ANY `x`. So `u -> u*Vhat` preserves it trivially. A consistency check, not
evidence. Recorded because I claimed otherwise one entry ago.

### 2 — convergence is not broken

At the proton pin: `u = 0.0085172`, `Vhat_D = 1.1280887`,
`u*Vhat = 0.0096082` — same order, 1.128x. The route does not die on numerics.

### 3 — but it cannot be tested against Q_beta. This is the terminus.

    Q_beta = Q_A * cos(alpha_eff) * Pi_{k>=2}(1 + c_k u^k)

The forced form replaces only the PRODUCT. The N=1 factor is `cos(alpha_eff)`,
and **entry 7 of this arc** showed that under D the bar-ODD slot is
structure-free — so no cos-of-a-bar-odd-phase exists to play that role.
Confirmed against the committed cache: its only DERIVED rung is `k = 2`
(`k = 3` is tier `cal-anchored`, i.e. extracted from experiment).

So the forced product refines a leading term that **does not exist** under D. No
D-frame Q_beta is computable from it — not because the comparison would be a
fit, but because there is nothing to compare.

### Derivable anyway, and not nothing

Rung `k` scales by `Vhat^k`, so the `k=2` rung — the ONLY one the corpus derives
rather than extracts — is `Vhat^2 = 1.2726x` larger under the forced form.
**+27.3%**, stated without any fit.

### Status

**NOT refuted. BLOCKED**, on the N=1 phase, by a blocker this arc established
itself. Naming which of two open pieces gates the other is progress; claiming
the form confirmed would not be.

### The arc, closed out — nine entries

  1. (D1) Lean-proved — `alpha` is DERIVED.
  2. The D offset is the BAR-MIDPOINT; one rule gives C's `1` and D's `cosh(2t)`.
  3. The form is MULTIPLICATIVE — resum `log Vhat`, not `Vhat`.
  4. `u` and `Vhat` carry opposite bar-weights; `u*Vhat` is bar-invariant.
  5. D's bar-defect is u-INDEPENDENT — the series cannot reach it.
  6. That defect IS `h^2/2 = ((b*[2]_q)^2 - 3)/2` — the ladder's own `b`.
  7. D's bar-ODD slot is structure-free — no cos-type phase can work.
  8. The PRODUCT form is weight-inhomogeneous; `Pi(1 + c_k (u*Vhat)^k)` is forced.
  9. That forced product is BLOCKED on (7) — it refines a leading term that
     does not exist.

**The single open item this arc leaves is sharp: what replaces `cos(alpha_eff)`
as the N=1 factor under D?** Everything else is either settled or downstream of
it. (7) says it is not a cosine of a bar-odd phase; (3) says the frame is
multiplicative/log; (4) says `u*Vhat` is the available invariant. A candidate
must be bar-invariant, must reduce to `cos(alpha_eff)` in the C limit, and must
absorb the `h^2/2` defect of (6) — three conditions, all stated, none yet met.

That is a better-posed question than the one this arc started with, and it is
the honest end of what I can derive without either a new structural input or a
fit.


## Entry 10 — the N=1 factor IS a bar-midpoint. The single open item is answered.

Probe: `computations/qbeta/qbeta_d_n1_factor_bar_midpoint_probe.py`, **8/8**.

The arc closed with one open item and three conditions on any candidate. All
three are met, by **re-applying the arc's own entry-2 rule one slot over**.

### The move introduces no new freedom

Entry 2 established `offset := the bar-midpoint of Vhat`, and showed that rule
DERIVES convention C's offset of `1` rather than assuming it. It was applied to
the **offset**. It had not been applied to the **N=1 factor**. Applying it:

    N=1 factor := ( cos(alpha) + bar(cos alpha) ) / 2

No fitted quantity, no new structure — the same rule, one slot over.

### Why C could use a bare cosine, which is what makes the rest work

Under C, `alpha_C` is bar-ODD and cosine is EVEN, so
`bar(cos a_C) = cos(-a_C) = cos(a_C)`: **the C-frame N=1 factor is already its
own bar-midpoint.** The rule is *vacuous* in C.

That is a sharper statement of entry 7 than "the bar-odd slot is empty" — it
says why the C form was available at all, and why its unavailability under D is
structural rather than a gap in the search.

Under D, `bar(a_D) = h^2/2 - a_D` — a **reflection about `h^2/4`**, not about 0.
So `cos(a_D)` is not bar-invariant, which is the arc's blocker restated.

### The result

    M := (cos(a_D) + cos(h^2/2 - a_D))/2  =  cos(a_D - h^2/4) * cos(h^2/4)

| condition (set by the arc) | verdict | how |
|---|---|---|
| (a) bar-invariant | **PASS** | exact symbolic identity, `bar(M) - M = 0` |
| (b) reduces to `cos(alpha_eff)` in C | **PASS** | exact symbolic identity |
| (c) absorbs the `h^2/2` defect | **PASS** | as a phase re-centring by `h^2/4` **times a u-independent constant** `cos(h^2/4)` |

(c) lands in exactly the multiplicative/log frame **entry 3** requires, with the
**u-independence entry 5** established for the defect. Size at the proton pin:
phase shift `h^2/4 = 0.0109265521331`, constant `cos(h^2/4) = 0.99994030582315`.

### 🛑 A CAS trap that nearly cost the result

`sympy.simplify` does **not** reduce
`(cos A + cos B)/2 - cos((A+B)/2)cos((A-B)/2)` to 0 for these arguments — it
returns a non-zero residual of two uncombined cosines. **That is a
non-simplification, not a refutation.** Re-checked numerically at 60 dps across
five values of q including both pins: worst `|diff| = 7.779e-62`, i.e. mpmath's
floor. Reading the CAS residual as a negative would have retired a correct
identity, and I was one step from doing so.

### Scope — what this does NOT claim

- **NOT uniqueness.** Other bar-invariant functions exist. The argument is that
  this one adds no freedom, being the arc's own rule re-applied.
- **NOT a D-frame Q_beta.** Rungs above `k=2` are still `cal-anchored`
  (extracted from experiment), so no D-frame number is computable and none is
  quoted here. The arc's entry-9 blocker on *testing* against Q_beta stands.
- **NOT wired.** Nothing downstream consumes it.

Scope (a). What changes is that the arc's terminus — *"it refines a leading term
that does not exist"* — no longer holds: the leading term now has a derived
candidate form.


## Entry 10b — uniqueness, tested by trying to break it: (a)+(b) FAIL, (c) saves it

Entry 10 asked whether `M` is **the** N=1 factor or merely **a** candidate. The
first two conditions do not pin it, and the third turns out to carry the content.

### The rival

`G := sqrt(cos(a_D) · bar(cos a_D))` — the **geometric** mean — is also
bar-invariant (verified symbolically) and also reduces correctly under C, where
`bar(a_C) = −a_C` gives `|cos a_C|`. So **(a) and (b) admit a second solution.**

**And it is not a rounding difference:**

    proton pin   M = 0.9986190619723252   G = 0.9986189041126984   rel 1.581e-7
    muon pin     M = 0.9986190616623656   G = 0.9986189038026348   rel 1.581e-7

**158 ppb**, against the Q_beta 100× target of 7.8 ppb — **~20× the target**.
Had the arc stopped at (a)+(b), the framework would carry a 158 ppb ambiguity
in its leading factor.

### Condition (c) discriminates — structurally, not numerically

Read as **entry 3** requires (the defect enters as a phase shift times a factor
with no phase dependence: `log F = f(a − c(δ)) + g(δ)`):

- `M = cos(a − δ/2)·cos(δ/2)` **separates exactly**. One singular set in `a`.
- `G` **does not**. It inherits the poles of *both* `cos a` and `cos(a − δ)` —
  two shifted singular sets — and a separated `f(a−c)·K` admits only one.
  Counted symbolically: at `δ = 0` both have **2** pole families (they must
  agree when there is no defect); at `δ = 1/3`, M has **2** and G has **3**.

So (c) is not decoration on (a)+(b) — **it is the condition doing the work**,
and the arc was right to state it separately.

### Not claimed

**Full uniqueness.** (c) is shown to exclude `G`; it is *not* shown that no
other function satisfies all three. That needs a functional-equation argument
this probe does not attempt, and entry 10's summary now says so rather than the
blanket "NOT uniqueness" it carried before.

Probe **12/12**.


## Entry 10c — the functional equation SETTLES uniqueness, in the negative

Entry 10b left full uniqueness open. It is now settled — as a **proof**, not a
failure to find one.

Under bar, `a -> delta - a`. Seek every `F(a, delta)` with (i) bar-invariance,
(ii) the log-separable form **entry 3** requires (`F = phi(a - c(delta)) *
K(delta)`), and (iii) the C limit `F(a, 0) = cos a`. Then (iii) gives
`phi = cos`, `c(0) = 0`, `K(0) = 1`, and (i) demands
`cos(a - c) = cos(delta - a - c)` for all `a`. The `+` branch gives `2a = delta`
— not an identity in `a`. The `-` branch gives

    c(delta) = delta / 2          ← THE PHASE SHIFT IS FORCED

and **`K(delta)` is left FREE** apart from `K(0) = 1` — verified symbolically
for an arbitrary `K`.

**So uniqueness does not follow from the three conditions**, and the arc's
choice of `K = cos(delta/2)` comes from the **entry-2 bar-midpoint rule**, not
from the conditions.

### That distinction is quantitative, not pedantic

    |1 - K| at both pins = 5.96942e-5 = 59694 ppb
    Q_beta 100x target   =                7.797 ppb
    ratio                =              7656x

The residual freedom the conditions leave open is **~7656× the accuracy
target**. The rule is doing real work, and had the arc stopped at "three
conditions met" the leading factor would carry that ambiguity.

### The three results together

| claim | status |
|---|---|
| phase re-centring by `delta/2` | **FORCED** by (i)+(ii)+(iii) |
| the rival `G` (geometric mean) | **EXCLUDED** by (c), on pole structure |
| the constant `K(delta)` | **FREE** — selected by the entry-2 rule alone |

**Not claimed:** that the bar-midpoint rule is itself forced. It is the arc's
own rule applied consistently — parsimony, not derivation. Probe **14/14**.
---

## Entry 11 — bar-parity prunes **every** D rung, and `u` is why C escaped it

`computations/qbeta/qbeta_d_rung_bar_parity_prune_probe.py` — **6/6**.

Entry 7 recorded that D's bar-odd slot is structure-free. This entry says the
same thing from the algebra, and turns it into a **test a candidate rung can
fail**.

### The prune

Under D the ladder variable is `X = u·V̂`, which entry 4 established is
**bar-invariant**. Expand `∏_{k≥2}(1 + c_k X^k)` and apply `bar` coefficient by
coefficient:

    [X^2]   c2 - bar(c2) = 0
    [X^3]   c3 - bar(c3) = 0
    [X^4]   c4 - bar(c4) = 0

Verified symbolically, not numerically. So **every D rung is forced bar-even** —
`bar(c_k) = c_k` for all `k`, with no bar-odd freedom anywhere in the ladder.

### Why the C ladder was never pinned this way

Because the C variable is **not** bar-invariant. Measured exactly:

    u = (q-1)^2 * sqrt(q^4 + q^2 + 1) / (q^4 + q^2)
    bar(u) / u = q^2          (exact, symbolic)

`u` is bar-**covariant** with weight `q²`. A `bar` applied to `∏(1 + c_k u^k)`
therefore reshuffles the grading instead of matching coefficient to coefficient,
so the C product imposes no parity condition on its own rungs. The conventions
differ here structurally, not by a substitution.

### What this buys, and what it does not

**Buys:** a falsifying test. Any future D-frame `c_k` must be bar-even, and the
extraction route — invert one rung against experimental `Q_β` — does not respect
that constraint, so a candidate produced that way is checkable against something
other than its own residual.

**Does not buy:** a value. No `c_3` is produced, proposed or fitted; the k=3 rung
stays underived and L2 is untouched. Scope **(a)**.

**Three things it is explicitly not:**

1. Not a claim the C-frame `c_3 = -2.0693…` *fails* the test. Bar-evenness needs
   `c_3` at both `q` and `1/q`; every anchor in this corpus sits at `q ≈ 1.11`,
   so the C value is not measurable against it (same accessibility obstruction as
   the §"Defined residual ≠ derived decomposition" bar-split).
2. Not applicable to the candidate `c_3 = -2 = J_Hopf(q=1)` — a constant is
   trivially bar-even, so the test has nothing to say about it either way.
3. Not a uniqueness result. It constrains the rungs; it does not select them.
---

## Entry 12 — bar-parity is SILENT on `K(δ)`, the freedom that dominates L2

`computations/qbeta/qbeta_d_n1_constant_bar_silence_probe.py` — **6/6**.

Entry 11 forces every D rung bar-even. The obvious next hope is that the same
symmetry pins entry 10c's free constant `K(δ)`. **It does not, and the reason is
structural rather than circumstantial.**

    delta = h^2/2,  h = q - 1/q
    bar: q -> 1/q  sends  h -> -h,  so  h^2 -> h^2

`δ` is bar-**invariant**. Therefore `K(δ)` is bar-even for **every** `K`, and
bar-parity imposes no condition at all. It is not a weak constraint on `K`; it is
a vacuous one. (Verified symbolically, with the contrast: `bar(u)/u = q²` exactly
— `u` is bar-covariant, a *graded* weight, which is precisely what makes entry 11
bite on the rungs.)

### Why this matters more than the k=3 rung

The gap between the two `K` the arc admits — `K ≡ 1` and `K = cos(δ/2)`, the
latter being what the midpoint factor `M` supplies — is

    delta(q0)          = 0.021853104266260994701
    |1 - cos(delta/2)| = 5.9694176850430203e-5   =  59694.18 ppb
    vs target 7.797    = 7656.0x

**That single residual is ~7656× the Q_β 100× target**, which is far larger than
anything a derived k=3 rung could contribute. So `K` is the L2 blocker at N=1,
and entry 11 — real as it is — does not reach it.

### A rounding, not a discrepancy

My first run reported **7653.1×** against entry 10c's recorded **7656×**. Same
number: 59694.18 / 7.8 = 7653.1 and 59694.18 / 7.797 = 7656.0. AGENTS.md quotes
the Q_β target as "7.8 ppb", which is `σ_exp/100 = 779.7/100 = 7.797` rounded.
The probe now uses the unrounded target and says so in a comment, so the pair
cannot be mistaken later for two measurements — the exact failure mode the `c₃`
"3.47 % vs 3.35 %" note in AGENTS.md was written about.

### Scope

A **negative**, scope (a). No `c_k` is produced, proposed or fitted; Q_β stays at
1279 ppb. It is **not** a claim that `K` is underivable — only that bar-parity is
not the tool, and that no sharpening of entry 11 will become one, because the
quantity it would have to constrain is invariant under the symmetry it is built
from. Closing `K` needs a genuinely different input.


---

## Entry 13 — `K(δ)` is NOT free in this arc; it is fixed by entry 2's rule

`computations/qbeta/qbeta_d_n1_constant_rule_determined_probe.py` — **6/6**.

Entries 10c and 12 read together suggest a 7656× residual with nothing in the arc
to close it. **That reading is wrong**, and this entry corrects it.

Entry 10 did **not** obtain `M` by searching the space of functions satisfying
(a)+(b)+(c). It obtained `M` by applying a rule the arc had already established
one slot over:

| | rule |
|---|---|
| entry 2 | `offset := bar-midpoint of V̂` |
| entry 10 | `N=1 factor := bar-midpoint of cos(α)` |

The arithmetic bar-midpoint of `cos(a_D)` is not *some* function meeting the three
conditions — it is a single determinate object,

    M = (cos(a_D) + cos(delta - a_D))/2 = cos(a_D - delta/2) * cos(delta/2)

whose constant factor is `cos(δ/2)`, **not** 1. So `K ≡ 1` is not an alternative
the arc admits: it is what you get by **discarding the rule** and keeping only the
three weaker conditions the rule happens to satisfy. Verified symbolically that
`K ≡ 1` does satisfy (a) — which is exactly the point, since it shows the
conditions are strictly weaker than the rule.

### Where the rule's authority comes from, and where it does not

- **Offset slot — non-vacuous and independently checked.** The rule *re-derives*
  convention C's known offset `1` (as `cosh(0)`) and C's known `α` exactly,
  rather than assuming them (entry 2). That is a genuine two-point validation.
- **N=1 slot — vacuous under C.** `α_C` is bar-odd and cosine is even, so the
  C-frame N=1 factor is already its own bar-midpoint. Verified here. The C limit
  therefore says only `K(0) = 1` and **cannot discriminate `K` at δ ≠ 0**.

### Status, stated precisely because it decides whether L2 may use it

`K = cos(δ/2)` is **rule-determined and slot-untested**: strictly stronger than
"free", strictly weaker than "derived". It is **not a fit** — nothing was
inverted against Q_β, and the rule was fixed before this slot was considered.

### What would settle it

A **third slot** where the bar-midpoint rule is non-vacuous under C, so the rule
can be tested somewhere other than where it was built. This probe does not find
one; it states the requirement, which is the next concrete thing to look for.

### Scope

Scope (a). No `c_k` produced, proposed or fitted; Q_β stays at 1279 ppb. The
7656× figure of entry 12 is unchanged as a *measurement of the condition-set
freedom*; what changes is that the arc does not actually sit at that freedom.


---

## Entry 14 — the third slot exists, the rule FAILS it, and entry 13 is withdrawn

`computations/qbeta/qbeta_d_bar_midpoint_rule_third_slot_probe.py` — **6/6**.

Entry 13 named the test that would settle `K`: **a third slot where the
bar-midpoint rule is non-vacuous under C.** This entry finds one and runs it.

**The slot:** the N=2 ladder factor `1 − u²`, whose `u²` coefficient is the
corpus's structural `c₂ = −1` (no fit, no CODATA, no q₀). Under C the ladder
variable is bar-**covariant** (`bar(u)/u = q²`), so the rule is non-vacuous
there — exactly the condition entry 13 required.

**The result:** the rule does not reproduce `c₂`.

    bar-midpoint of (1 - u^2)  has u^2 coefficient  -(q^4 + 1)/2
    at the proton pin          -1.25897662490917    vs known -1
    off by                     25.8977 %

| slot | C-frame | verdict |
|---|---|---|
| offset | non-vacuous | **passes** (entry 2 — re-derives C's `1` and C's `α`) |
| N=1 factor | vacuous | no evidence available |
| N=2 factor | non-vacuous | **FAILS, 25.90 %** |

### Entry 13's status claim is withdrawn

It rested on an implicit **universality** of the rule. That universality is now
measured false. `K = cos(δ/2)` is rule-**transported** from a slot where the rule
works, to a slot where it cannot be tested, **past a slot where it demonstrably
fails**. Entry 12's **7656×** freedom is reinstated as live.

### The defence, and what it costs

One can read the rule as *"re-express in bar-invariant form"* rather than *"apply
everywhere"* — vacuous wherever that is already done. Under D the N=2 slot **is**
vacuous (`X = u·V̂` is bar-invariant, verified here), so on that reading the
C-frame N=2 test is outside the rule's remit. But **entry 2's validation is a
C-frame check of exactly the same kind.** The dichotomy has no comfortable
branch:

- the C-frame check is legitimate ⇒ **the rule fails at N=2**;
- it is not ⇒ **entry 2's validation goes too**, and the rule is validated nowhere.

Either way `K` is not rule-determined in entry 13's strong sense.

### Also fixed here: entry 11 asserted entry 4 rather than computing it

Entry 11's sixth check was labelled *"stated structurally; entry 4 supplies
`bar(u·V̂) = u·V̂`"*. Now computed: `V̂ = z·h + 1` gives
`V̂_D = (q⁴+1)/(q²+1) = 1.12808874411` (matching the value the arc records),
`bar(V̂_D)/V̂_D = q⁻²` against `bar(u)/u = q²`, hence `bar(X)/X = 1` **exactly**.
**Entry 4 is confirmed.** My first pass guessed `V̂ = q²` from the offset
`cosh(2 log q)` and got `bar(X)/X = q⁻²` — which looked like a refutation of
entry 4 and was a wrong `V̂`, not a wrong entry. Recorded because the near-miss
is the point: an assumed definition nearly produced a false retraction of a
correct result.

### Scope

Scope (a). No `c_k` produced, proposed or fitted; Q_β stays at 1279 ppb.
## Entry 10d — entries 10/10b/10c are now LEAN-PROVED (8 theorems, sorry-free)

`folio/quantum-observable-universe/lean/QOU/QBeta/N1FactorUniqueness.lean`.
`lean`-direct exit 0; `#print axioms` clean on all 8; zero sorryAx.

**No new mathematics.** The functional-equation argument is entry 10c's (PR
#6310). I started the same derivation independently, found 10c on the intent
pass ~35 min after it landed, and re-scoped from *derive* to *verify with a
different instrument* per the converge-on-landing rule. 10c is cited, not
restated.

**The one that earns its keep:** entry 10 records that `sympy.simplify` returns a
NON-ZERO residual for

    (cos A + cos B)/2 - cos((A+B)/2)*cos((A-B)/2)

and that the identity was therefore confirmed at 60 dps, one step from being
read as a refutation. `barMidpoint_eq` proves it exactly (`Real.cos_add_cos`).
A CAS non-simplification is not a refutation; a proof assistant settles which.

| theorem | content |
|---|---|
| `barMidpoint_eq` | the identity sympy would not reduce |
| `phase_forced` | `BarInvariant δ c K ↔ ∃k, c = δ/2 − kπ` (K ≠ 0) — an **iff** |
| `const_free` | for ARBITRARY K, `cos(a−δ/2)·K` is bar-invariant — 10c's "K is FREE" as a proved negative |
| `barMidpoint_barInvariant` | the arc's M sits in the forced phase |
| `c_limit` | `δ = 0` gives the bare cosine (condition iii) |
| `c_rule_is_vacuous` | under C, bar is `a ↦ −a` and cos is even — WHY C could use a bare cosine |
| `uncentred_fails` | **CONTROL**: `c = 0` is bar-invariant only if `δ = 2kπ`, arbitrary δ, proved FROM `phase_forced` |
| `uncentred_fails_of_pos_of_lt` | **CONTROL**: physical form, `0 < δ < 2π`, needs only `Real.pi_pos` |

The controls exist because all eight compiled on the first attempt, which is
exactly when a vacuous statement hides.

**Unchanged:** the bar-midpoint RULE is still not derived (parsimony, not
derivation); `const_free` proves the conditions do NOT select `K = cos(δ/2)`;
no `c_k` proposed or wired; no D-frame Q_beta computable while rungs above
`k = 2` are cal-anchored. Entry 9's blocker on TESTING against Q_beta stands.

Mathlib note: `Real.pi_gt_three` is in `Mathlib.Analysis.Real.Pi.Bounds`, whose
olean is absent from the restored cache. The π-free control is the better
statement regardless — general in δ rather than one sample point.

### Read against entries 11-14, which landed while this was in review

Entries 12/13/14 oscillated on whether `K(δ)` is free: 12 measured the 7656×
condition-set freedom, 13 argued `K` is rule-determined, 14 **withdrew 13** (the
bar-midpoint rule fails the N=2 slot by 25.90 %) and reinstated 12's freedom as
live. `const_free` is the theorem on the condition-set side of that question: for
ARBITRARY `K`, `cos(a − δ/2)·K` is bar-invariant. So the freedom entry 14
reinstates is not an unfound constraint — it is proved that (i)+(ii)+(iii) cannot
supply one, and any closure must come from outside them, as entry 14 concludes.

Nothing here bears on entry 14's separate finding that the RULE fails at N=2;
that is about the rule's authority, not about what the conditions force.
## The z=1 exclusion is a WALL — measured, and it goes against the hypothesis (2026-08-30, PR #6144)

I tested whether `one_not_root` is as strong as the framing treats it, expecting
it to be weaker. It is not. Negative recorded.

**The gap in the reasoning I was probing.** `AdmissibleRoots` defines admissible
= the (1^3) weight VANISHES (the two-row cap), roots {q, z_D}, z=1 excluded. The
2026-08-29 correction search measured that the augmentation base's required
correction IS the trace's own z=q -> z=1 return to 0.17 %, and called that
direction forbidden on the strength of `one_not_root`. That moves from a BINARY
fact to a claim about a MAGNITUDE. `one_not_root` is an invariant about a SIGN:
N(q,1) = (1-q)(q^2+1-q^3) < 0. It says the leak is nonzero, not that it is
correction-sized.

**MEASURED** (`qbeta_admissibility_is_a_magnitude_probe.py`, 4/4, exact sympy
from the H_3 trace on the NF basis with the CORRECTED weight z(hz+1)):

    y_(1^3) numerator == q^2 * wtNumer   EXACTLY  (independent Lean confirmation,
                                         and it SURVIVES the qou-isu5 trace fix)
    denominator = (q^2+1)(q^2-q+1)(q^2+q+1)

    three-row share at z=1     1.4589 %
    augmentation base needs   11.087 %   ->  leak 7.6x too small
    tr_M base needs           75.924 %   ->  leak 52x too small

**Two separate facts, neither dressed as the other:**
1. The exclusion HOLDS, exactly as proved.
2. The leak is the WRONG SIZE to be the correction, by 7.6x. So the 08-29
   verdict is now quantitatively supported rather than merely defensible: the
   near-coincidence net/aug = 0.8906 vs F_required = 0.88913 is NOT explained by
   the admissibility violation being correction-sized.

**Reference scale, because a verdict against a self-chosen threshold is not a
measurement:** three-row share at other z. z=1 gives 1.459 %, the SECOND SMALLEST
of seven sampled; generic z gives 3-33 %. So z=1 IS unusually close to two-row,
just not close enough to matter. Worth knowing before anyone reaches for it again.

LIMITATION: the leak is a weight SHARE, the correction a RATIO OF TRACE VALUES.
Order-of-magnitude check, not a proof. 7.6x is outside what that could hide;
1.2x would not have been.

**What this does NOT do:** it does not derive F, does not readmit z=1, does not
propose a correction. It closes off one way of rescuing the augmentation base
and confirms the wall the 08-29 audit hit is real.

**Also relevant to this bean from the same PR:** the scope-(a) negative published
by `qbeta_c3_barodd_hs_matrix_resolvent_probe` is WITHDRAWN. Its trace vector was
`z*z*z`; with the correct weight its finding 2 ("the pairing is bar-even") is
falsified at mu=0 (BAR-ODD, 18.38 vs 6.86). Not a positive either -- still
convention C, and inverting a now-singular Gram in float64. Re-run belongs here.

### How this sits with Step 8 (added on the rebase that brought Step 8 in)

Step 8 and this section are two DIFFERENT routes, both negative, and neither
subsumes the other. Recording the relation so a later reader does not treat one
as a restatement of the other:

  Step 8   closes the ADDITIVE/cos route: under C the bar-invariant is the
           constant 1, a fixed centre for a resummation; under D it is V^/q,
           which moves with q, so nothing is available to centre on.
  this     closes RESCUING THE AUGMENTATION BASE via the z=1 return: the
           admissibility leak at z=1 is 1.459 %, against an 11.087 % required
           correction -- 7.6x short, so the violation is not correction-sized.

They converge on the same consequence from opposite ends: the D re-derivation
needs a genuinely new form, not a repair of the C one. Step 8 says the C FORM
has no D analogue; this says the nearest INADMISSIBLE point is not where the
missing size comes from either.


## Step 9 (2026-08-30, PR #6144) — the D decay carrier is ONE block, and that closes the block route

**Lean-proved sorry-free**, `QOU/QBeta/DecayBlockCarrier.lean`, lean-direct exit 0,
`#print axioms` = [propext, Classical.choice, Quot.sound] on all ten, no sorryAx.

### The finding

    chi^(2,1)(Delta_S) = 0     EXACTLY, at EVERY z

The 2-dimensional block never carries the decay element. It follows from two
one-line identities, both proved:

    reg_char(Delta_S) = 0                  traceless in the regular rep
    chi^(3)(Delta_S)  = -chi^(1^3)(Delta_S)  exact opposites

so `chi^(2,1) = (reg - chi3 - chi111)/2 = 0`. Consequence, also proved:

    tr(Delta_S) = (y_3 - y_(1^3)) * chi^(3)(Delta_S)   for ALL z

### What it does to the framing

**The two-row cap does NOT take the decay carrier from 3 blocks to 2. It takes
it from 2 to 1**, because (2,1) was never in it. Under D the decay lives
entirely in a single 1-dimensional block with weight
`y_(3)(z_D) = (q^4+1)/(q^2+1)^2` (proved), alongside
`y_(2,1)(z_D) = q^2/(q^2+1)^2` and `y_(1^3)(z_D) = 0` (both proved), normalising
to 1 (proved).

### Why this closes a class

I set out to test whether the D weights are FORCED: two surviving blocks, two
constraints (normalisation + anchor), zero free parameters. They are -- and the
solve is DEGENERATE. The anchor constrains only `y_3`, returning

    y_3*  = F * y_3^D          exactly: the anchor can only RESCALE the one
                               carrying weight
    y_21* = normalisation's leftover, INVISIBLE to Q_beta

**So block re-weighting cannot source the convention-D correction.** There is
one weight after the cap and it is fixed by the trace axioms. The new form the
D re-derivation needs cannot come from the Wedderburn decomposition at all.

Recognition test ran against a candidate list declared BEFORE solving (nearest
form 8.9 %, not isolated) -- but the structural verdict does not depend on it.

### How this sits with Steps 7-8

Three routes now closed from three directions, none subsuming another:

  Step 8    the ADDITIVE/cos route: under D the bar-invariant V^/q moves with q,
            so there is no fixed centre to resum around
  z=1 wall  rescuing the AUGMENTATION base via the z=1 return: the admissibility
            leak is 1.459 % against an 11.087 % correction, 7.6x short
  Step 9    the BLOCK route: only one block carries the decay, so re-weighting
            has nothing to re-weight

The 2026-08-29 audit had already closed `admissible base x one multiplicative
correction`. Four classes down. Still NOT established: the replacement form.

### Caveat on scope, stated in the Lean too

The two 1-dim characters are DEFINED by their defining evaluations; the REGULAR
character's basis values are taken as DATA from the corpus's own
trace-of-left-multiplication computation. Formalising the H_3 multiplication
table is not what these results turn on. The theorems are exactly "given those
values, these identities hold".


## Step 10 (2026-08-30, PR #6144) — z_required = 0.99850, and the block is a RULING

### The reduction makes the question exact

Step 9 proved `tr(Delta_S)(z) = (y_3 - y_(1^3))(z) * chi^(3)(Delta_S)` with
`chi^(3)` FIXED. So the whole z-dependence is one scalar, and it is AFFINE:

    g(z) = (2qz - q^2 + 1)/(q^2 + 1)
    g(z) * chi^(3)(Delta_S) = h^2/2 - h z        exact, all z
    g(z_D) = (q^4+1)/(q^2+1)^2

Affine => invertible => "what z does CODATA require" is EXACT and UNIQUE, zero
free parameters. Not a fit.

### The number

    z_required = 0.998500302563
    z = 1        PROVED inadmissible (one_not_root)
    z_D          0.612688037146   admissible
    z = q        1.109978582751   admissible

**0.15 % from z = 1, and 257x nearer to it than the admissible z_D.** Both
admissible bases give the SAME z_required to 10 digits -- as they must, since
only one z reproduces the Q-value. The two "different bases" were never
different problems; that agreement is the check the reduction is right.

### The block is a ruling, not an impossibility — CHECKED, not assumed

`MarkovZFullBarCondition`'s docstring says "Which horn is the decay channel's is
NOT decided here: no corpus block derives the decay fibre, and the channel is
registered `disputed`". That could be a stale status note superseded by the
2026-08-15 ruling. It is not. The trace-convention registry preserves the
distinction verbatim:

  "Supersedes the CONTRADICTORY/null registration ... AS A STATUS, NOT AS
   ANALYSIS: its finding that neither convention was DERIVED for this channel
   stands"

STATUS settled (D, by ruling); DERIVATION not. `AdmissibleRoots` proves
`admissible <=> y_(1^3)=0 <=> z in {q,z_D}` -- a theorem ABOUT the condition.
That the DECAY channel must satisfy it is the ruling.

### Splitting my own results honestly

UNCONDITIONAL (any z, any convention):
  - chi^(2,1)(Delta_S) = 0                    (Lean, sorry-free)
  - tr(Delta_S)(z) = g(z) * chi^(3), g affine
  - the decay channel's entire z-content is ONE affine scalar
  - z_required = 0.998500302563

CONDITIONAL ON THE RULING:
  - "under D the carrier is a single block"
  - "block re-weighting cannot source the correction"  <- Step 9's own headline
  - the inadmissibility of z_required
  - the four closed correction routes (08-29, Step 8, z=1 wall, Step 9)

conditional-proved != premise-established, applied to my own work.

### The reframing — what the open problem actually is

The D re-derivation is NOT blocked by a proved impossibility. The decay trace is
one affine scalar; the data fixes it at 0.99850; the ruling fixes it at 0.61269.
Closing that gap means **DERIVING THE DECAY FIBRE**, which the registry already
names as the open item — not finding another correction.

**The thing missing is not a form.** Every "new form" search, mine included, has
been searching inside a constraint that was never derived for this channel.

z = 1 is NOT readmitted: its admissibility leak is 7.6x too small to be the
correction. "Nearly z=1" describes the tension; it is not a mechanism.


## Step 11 (2026-08-30, PR #6144) — the decay fibre DERIVED from bar-parity, and the settled account

Lean sorry-free, `QOU/QBeta/DecayFibreBarParity.lean`, lean-direct exit 0,
axioms clean on all ten.

### Derived: the bar-parity iff (uses NO two-row cap)

    chi3S_bar_odd                  chi^(3)(Delta_S) at q^-1 is its NEGATIVE
    g_bar_defect_mul               (g(q^-1,zbar) - g(q,z))(q^2+1) = 2q(zbar-(z-h))
    g_bar_even_iff_fullBar         g bar-EVEN  <=>  bar(z) = z - h  (FULL-BAR)
    decayTrace_bar_odd_of_fullBar  full-bar => the decay trace is bar-ODD
    one_not_fullBar                the CONSTANT z == 1 is not full-bar
    barEven_not_fullBar            a bar-EVEN z is NEVER full-bar (so z_C isn't)
    y21_at_augmentation            y_(2,1)(q) = 0 EXACTLY

g can never be bar-ODD (no solution). Measured parity:

    z = q  full-bar YES -> bar-ODD      z = 1  full-bar NO -> NO definite parity
    z_D    full-bar YES -> bar-ODD      z_C    full-bar NO -> NO definite parity

This also explains `decayLadder_zC_threeRow_ne_zero` from the parity side:
**z_C is bar-EVEN, which is a DIFFERENT condition from full-bar.** The two have
sat adjacent in the corpus for weeks; what is new is that they are not the same
one, and which one this channel needs.

### THE SETTLED ACCOUNT — three conditions, three different jobs

  cap  y_(1^3) = 0     RULING for this channel    narrows to {q, z_D}
  faithful y_21 != 0   STRUCTURAL (corpus hfaith) picks z_D from that pair
  full-bar             DERIVED here               excludes z_C and z == 1;
                                                  constrains FORM, not VALUE

**The limitation, and it narrows my own Step 11 first pass.** `fullBar_add_const`:
z_D + c is full-bar for ANY constant c, since constants are bar-even. So a
full-bar parameter can take ANY value at the pin. `one_not_fullBar` excludes
z = 1 as a CHOICE OF PARAMETER; it does NOT exclude the required VALUE
(z_required ~ 0.99850), which a full-bar function could attain.

**So the narrowing to the admissible set — and hence the exclusion of what the
data wants — still rests on the cap, i.e. on the ruling.** Bar-parity and
faithfulness say WHICH POINT of that set is the decay channel's; they do not
establish the set.

### Correction trail, recorded so it stops oscillating

  Step 10        "the block is a ruling, not an impossibility"  — right about
                 the CAP
  Step 11 (1st)  "bar-parity excludes z=1 independently"        — right about
                 the CONSTANT, overstated as a closure of the gap
  Step 11 (2nd)  this reconciliation                            — written INTO
                 the Lean file's prose so it cannot be quoted away

### Still open

What establishes the admissible set for the DECAY channel without the ruling.
Bar-parity + faithfulness pin z_D GIVEN the cap; nothing yet derives the cap
for this channel. That is the same open item the registry names, now with the
logical structure around it fully mapped.


## Step 12 — the decay channel is BLIND to the cap (so it HAD to be a ruling)

Lean sorry-free: `threeRow_undetermined_by_decay`, `cap_member_of_family`.

tr(Delta_S) = (y_3 - y_(1^3)) * chi^(3), so the decay pairing depends on the
weights ONLY through the difference. With normalisation that is 2 constraints on
3 unknowns:

    y_3 = g + t,  y_21 = (1 - g - 2t)/2,  y_111 = t

normalised, decay pairing g, for EVERY t. A one-parameter family all giving the
same Q-value and sweeping every value of y_(1^3).

**The cap is not merely un-derived for this channel — it is UNDETERMINABLE BY
it.** No decay measurement at any precision can establish or refute
y_(1^3) = 0. It selects one member of a family the channel cannot tell apart.

So the cap had to arrive as a ruling: there was never a decay-side derivation to
find. A derivation would have to come from another channel or a structural
argument, never from Q_beta itself. This CLOSES the question Step 11 left open,
with a negative, and retro-justifies the registry's "no corpus block derives the
decay fibre".

### Arc status after Steps 9-12

  what the channel determines   g = y_3 - y_(1^3), one affine scalar; and the
                                data fixes it exactly (z_required = 0.99850)
  what it cannot determine      y_(1^3) separately — hence the cap, hence the
                                admissible set, hence the exclusion of 0.99850
  derived here                  the bar-parity iff (full-bar <=> definite parity)
                                and faithfulness picking z_D within {q, z_D}
  still open                    a cross-channel or structural derivation of the
                                cap. NOT findable in Q_beta data.


## Step 13 — WITHDRAWAL: the cap is DERIVED, not a ruling. Steps 10/12 framing was wrong.

Asked "what condition makes the mass fibre functor land in Rep(SU_q(2))~TL".
Answer: (a) tau monoidal, (b) dim tau(fundamental) = 2, i.e. Lambda^3_q V = 0 --
the (1^3) block IS the image of the q-antisymmetrizer, which projects onto
Lambda^3 V, zero for a 2-dim fibre.

**And it is ALREADY VERIFIED.** Bean `qou-n1dj`, RESOLVED 2026-08-08, found on
corpus-grep path 6 (`.beans/`):

- `lem:feynman-eigenbasis-decomposition` writes the mass decomposition with the
  row cap `l(lambda) <= 2` IN THE INDEX SET, so (1^3) is absent at n=3 by
  construction — not an extra assumption.
- `FibreDimensionForcesTL.lean` (verified today: lean-direct exit 0, 0 sorries)
  proves `z*[N]_q = q^N` (fibre q-dim DETERMINES the Ocneanu parameter),
  `N=2 => z_D`, and `z_D => y_(1^3) = 0`.

### Why I got it wrong

I read `MarkovTraceTLUniqueness.lean`'s "What this does NOT establish" section as
current. It is STALE — the file establishing the premise is in the SAME
DIRECTORY, and the audit that section cites is the one that POSED the question.
AGENTS.md's "source-file status notes are NOT authoritative" applies to Lean
docstrings too; mine only fired on `## Status` blocks. Fixed at the source.

### Arc status

  Step  9  chi^(2,1)(Delta_S) = 0                 STANDS
  Step 10  z_required = 0.998500302563            STANDS
  Step 10  "the block is a ruling"                WITHDRAWN
  Step 11  bar-parity iff                         STANDS, less load-bearing
  Step 12  decay cannot determine y_(1^3)         STANDS; the inference "hence
                                                  the cap had to be a ruling" is
                                                  WITHDRAWN
  today    joint determinacy (decay+mass)         STANDS and GAINS: the derived
                                                  cap is empirically falsifiable

### The real remaining tension, restated

The cap is derived, so z_D is forced, so z_required = 0.99850 is genuinely
excluded. The gap between what the data wants and what the theory gives is
therefore REAL and unexplained — not an artefact of an undecided convention.
That is a sharper problem than the one I thought I had.


## Step 14 (2026-08-30) — the terminus, stated as a negative

With the two-row cap DERIVED (Step 13), the missing convention-D Q_beta
factor `Q_beta = K · g · χ` has exactly three places to live, and all
three are measured-negative. Probe
`computations/qbeta/qbeta_d_frame_terminus_probe.py`, 2/2, proton pin.

| leg | status |
|---|---|
| `g` block-weight pairing | **CLOSED.** Cap derived ⇒ `z = z_D` forced ⇒ `g = y_(3)(z_D) = (q⁴+1)/(q²+1)² = 0.5054042265`, no freedom left. Data wants `0.8891258104` — short by ×1.7592369905. Not a failed search; a DOF that does not exist. |
| `χ` element characters | **NEGATIVE.** `χ^(2,1)(Δ_S) = 0` exactly (Lean-proved), so `Δ_S` is `(c, 0, −c)`. An element would need `a_(2,1)/a_(3) = 1.5516573513`. Nearest declared: `[3]_q/[2]_q` 2.45 %, `3/2` 3.33 % — basket distance, not isolation. |
| `K` trace→MeV scale | **NEGATIVE.** Enumerated 2026-08-29 (`qbeta_d_frame_admissible_base_correction_search`): nothing parameter-free within 6.31 %. |

Joins the four correction classes already closed: the 2026-08-29
corrections, additive/cos (Step 8), the `z = 1` wall, block re-weighting
(Step 9).

**Scope-(a), explicitly.** An enumeration over DECLARED classes, not a
proved impossibility. A *derived* (not searched) decay element with the
right character ratio would still close it. Searching for one on the
number would be a fit, so `1.5516573513` is recorded as a target to check
a future derivation AGAINST, never a criterion to search ON.

**Not claimed:** that the framework or convention D is wrong, or that no
closure exists — only that none is findable by any enumeration this
corpus has run.

## Step 14b — my own Step-13 correction had not been propagated

The Step-13 withdrawal ("the cap is a ruling" → the cap is DERIVED, from
the 2-dim mass fibre, `FibreDimensionForcesTL.lean`, `qou-n1dj`) fixed
the Lean docstring and this bean and left the same wrong sentence live in
`qbeta_cap_is_jointly_determined_probe.py` — in its verdict string, its
`premise_corrected` field, and the witness both write. Two copies, five
commits apart, on one branch. Corrected in `c297bd7b04`.

What stands unchanged: `χ^(3)(β_Bor) = χ^(1³)(β_Bor) = 1`, so mass sees
`y₃ + y₁₃` and decay sees `y₃ − y₁₃`; with normalisation
`det = −2(q−1)⁴(q+1)⁴(q²−q+1)(q²+q+1)/q⁶ ≠ 0` off `{0,1,−1}`, so the
three functionals determine all three weights uniquely. Re-scoped, not
retracted: the cap is *also* an observable — a falsifiable cross-check on
the derived `z_D`, not a second route to be taken on trust.

## Step 14c — all five of this branch's probes were `Q0_ANCHOR_MISSING`

They read `q_at()` (proton) but no stem was in `q0_anchor_manifest.json`,
and `WitnessBuilder.build()` stamps `q0Anchor` only on a positive
declaration. `q0-anchor-consistency-audit` `Q0_ANCHOR_MISSING`
1634 → 1639; the +5 was mine. Registered and re-run (`7820b814f6`) —
fixed at the producer, no witness hand-edited, no computed value moved.


---

## 2026-08-31 — the Borromean trace with `z` SYMBOLIC, and the anomaly is NOT the convention

Owner-requested. `computations/qbeta/qbeta_z_symbolic_borromean_crosscheck.py`,
PR #6328.

### Why it was needed

`m_p_substrate_identity_50dps.trM_borromean(q)` is a closed form in `h` alone
with **no `z` parameter** — convention D was substituted before it was written
down. So `y_(1³) = 0` is baked into `F_Bor → canonical_mass`, and any attempt to
*measure* the cap through that route measures its own assumption. Provably
circular, not merely suspected.

### The control, which is why the rest is trustworthy

    tr_M(β_Bor)(z,q) = (−q¹⁰z + q⁹z² − q⁹ + 5q⁸z − 4q⁷z² + 4q⁷ − 10q⁶z + 6q⁵z²
                        − 5q⁵ + 10q⁴z − 4q³z² + 4q³ − 5q²z + qz² − q + z) / q⁵

At `z = z_D` this reproduces `BorromeanMarkovTrace.lean`'s
`(4 + h² − 3h⁴ − h⁶)/(h² + 4)` with **symbolic difference exactly 0**.
`y_(1³)(z) = 0` has exactly the two known roots `{q, z_D}`.

### 🛑 A CORRECTION TO PR #6144's FRAMING — mine

#6144 solved a 3×3 system treating `(y₃, y₂₁, y₁₁₁)` as three unknowns fixed by
three independent functionals, and concluded the cap is **"jointly
determined"**. Correct as linear algebra, **wrong about the object**: for a
normalised Markov trace the 3×3 Markov system already consumes all freedom, so
the weights are a **one-parameter family in `z`** and `y_(1³)` is a function of
`z` alone.

Mass and decay do **not** measure three independent weights — they each
determine **the same single parameter**. The system is **over-determined**, not
jointly determined. Do not repeat the "jointly determined" phrasing.

### The measurement — muon pin, the only convention-free one

The proton pin is fixed *through* `F_Bor` and so presupposes what is under test.
The muon pin is `m_μ/m_e = Vol(4₁)/ℏ_q²` — pure geometry, no trace.

| determination of `z` | value | vs cap |
|---|---|---|
| the **cap** (`y_(1³) = 0`, derived) | 0.612688050638272415 | — |
| **mass** (measured `m_p`, non-circular) | 0.612812650836121753 | **0.0203 %** |
| **decay** (measured `Q_β`) | 0.998500302563013 | **62.97 %** |

**The anomaly is localised to the decay channel, not the convention.** An
independent, non-circular measurement puts `z` essentially where the derived cap
puts it. That is a materially different problem from the one this arc has been
treating.

### Quoted with its leverage — the agreement is weaker than it looks

`d ln(tr_M)/d ln z = 0.00119` against decay's `1.206`: the mass channel is
**1012× less sensitive** to `z`. A tr_M residual of 2.42e-7 opens out to 2.03e-4
in `z`. This does **not** claim mass confirms the cap to 1e-7.

### The residual is not absorbed

2.42e-7 relative in tr_M is **~21× the μ–p substrate tension** (11.5 ppb), so it
is neither obviously that tension nor obviously experimental. Open.

### Standing owner rulings from this session

- The **cross-check was green-lit** and has now run.
- A **categorically constrained *and derived*** search is permitted; a fit is
  not. This licenses `[3]_q/[2]_q` (2.45 % from the needed character ratio,
  isolated by 2.1× inside the constrained class) as something to derive
  *toward*, never to fit to.
- Open with the owner: whether the **counit reading** now becomes the leading
  hypothesis for the decay channel, given `z_required` sits 0.15 % from `z = 1`
  and mass independently confirms `z_D`.



## The two-row cap route is EXHAUSTED (2026-08-30, PR #6264)

The §"Remaining piece" above is closed **as a route**, without running a search.

The cap is `y_(1³) = 0`, whose admissible set is **proved complete** by
`qou-06wh`: `N = (z−q)((q²+1)z − q³)`, roots exactly `{q, z_D}`. Verified
symbolically: `y_(1³)(z_D) = 0` exactly, nonzero at `z_C`.

So the cap permits **exactly two** bases and only `z_D` had been phase-tested.

    alpha_required = -0.052358683519      window = +/- 1.09189e-5
    z_C   -0.0523361202682       2.07 windows
    z_D   -0.0404857773406    1087.37 windows
    z=q   +0.0114960776856    5848.10 windows

**`z = q` is excluded structurally, not numerically.** Since `h = q − 1/q > 0`
for all `q > 1`, `α = (z−1)h/2 < 0 ⟺ z < 1`. The required phase is negative, so
the form forces `z < 1`; and `z = q > 1` always. No anchor, no window, no
numerics — the 5848-window figure is an illustration at one anchor, not the
argument.

**Consequence.** The prune in §Progress tested `z_D` and *inferred* the
one-parameter class. It is now **exhaustive over the admissible set** — the
stronger statement, because the cap was the only structural constraint selecting
members of that class.

**Scope (a).** Excludes the cap as a route to a D-frame ladder *in the
`α = (z−1)h/2` form*. Does NOT exclude convention D, nor a D-frame ladder derived
another way. The finding that **neither frame's α is derived** is untouched.

**Does not license a search for a third base:** the set is proved to have exactly
two members, so a third requires dropping the cap — the constraint under the
ruling.

**What remains** is what this bean already names: the functional form must
change, and α is axiomatised in both frames
(`q-beta-cos-resummation.ts:48`). That is a derivation, not a measurement.


## The filter, verified and made executable (2026-08-30, PR #6264)

### The two-constraint filter

`α_required` is known at two anchors that share `Q_codata_MeV` **exactly**
(checked, not assumed — otherwise the "slope" is a confound between two
experimental values, not a q-derivative). Imposing both value and slope on
`α = (z−1)h/2`:

    required   z(q0) = 0.499104480185     z'(q0) = +400.289678821
    z_C        z = 0.4993203342           z' = -0.01172370089
    z_D        z = 0.6126880371           z' =  1.046577629
    z=q        z = 1.109978583            z' =  1.0

**`z_C` passes the VALUE row to four decimals and misses the SLOPE row by a
factor of −34,144, sign included.** That is this bean's "transversal crossing",
quantified. **Passing row 1 alone is not evidence.**

For *constant* z the two rows are contradictory: the value needs `z ≈ 0.4991`,
the slope needs `z = 46.69` (which gives `α = +4.78`).

### The slope was red-teamed before being relied on

It is a secant over `dq = 1.29e-8` from two points, and two points cannot
distinguish a derivative from an artifact. Reconstructed `α_required` from its
closed form (`−arccos(Q_codata/(Q_A(1−u²)))`) and differentiated exactly:

    witness secant   41.388615
    my secant        41.31873053
    my exact deriv   41.31853588        agree to 0.17 %

**Caveat:** my reconstruction sits a *constant* −0.004259 from the witness at
both anchors (my `Q_A`/`m_e` differs slightly), which is exactly why the slopes
agree while the values do not. Quote the slope as **≈ +41.3–41.4**, not to six
digits.

**Bonus corroboration:** at `q₀+1e-3` the reconstruction returns a COMPLEX α —
independently reproducing this bean's separate note that past ±0.1 % in q the
ladder has no real phase at all.

### Delivered as a probe, not a table

`computations/qbeta/qbeta_ladder_alpha_form_filter_probe.py` recomputes the
filter from the required-phase witness on every run and asserts its own
precondition. Rationale is this arc's own history: the convention-C tranche was
a sequence of recorded figures going stale, three of them mine. A table records
what the numbers were; the probe tracks the anchor.

### What this changes for the search

The prune is now **exhaustive over the two-row cap's admissible set** (proved
complete: `{q, z_D}`; `z = q` excluded structurally by sign for all `q > 1`), and
the filter says what any replacement must satisfy: **sit at ≈0.499 while
carrying a derivative ≈+400**. No rational function of the kind this corpus uses
does that near `q₀` without a near-pole or an engineered feature exactly there —
a fine-tuning signature.

That is independent support for this bean's existing conclusion: **the
functional form must change.** The problem is not that the wrong `z` was picked.

**Still open, and unchanged:** the derivation of α itself, axiomatised in both
frames (`q-beta-cos-resummation.ts:48`). The filter above is now the
pre-registered test any candidate must pass — which is what the Discipline
section asks for before a search begins.

---

## Entry 15 — the defect at BLOCK resolution: C's bar-oddness is a CANCELLATION, D's defect is z-FREE. Two hypotheses of mine refuted. (2026-08-31)

`computations/qbeta/qbeta_block_bar_defect_conjugation_probe.py` — **14/14**,
sympy exact, **runs standalone with `PYTHONPATH` stripped**.
Audit: `docs/audits/2026-08-31-cds1-block-bar-defect-and-conjugation.md`.

Built on entry 8's master identity (`qbeta_phase_block_resolution_probe`,
a sibling's) — **not re-derived**. `bar` acts on `(q, z)` jointly; `zbar` is an
independent symbol specialised only at the end, by the two conditions
`MarkovZFullBarCondition.lean` proves. The constant-`z` substitution this bean
already discarded as meaningless is not done here.

### What was tested, and why

Entry 12 closed with *"Closing `K` needs a genuinely different input."* Entry 14
then withdrew entry 13, so `K` is free again at **7656×** the target — the
arc's largest single L2 blocker. Two structural candidates:

  * **(A)** does resolving the defect PER BLOCK restore a parity handle?
  * **(B)** is `bar` the Kohno–Drinfeld conjugation `λ ↔ λ'`, making C's
    cancellation a theorem rather than a coincidence?

**Both refuted.** They were my hypotheses; recorded as negatives because each is
plausible enough to cost someone else a session.

### The positive that came out of the attempt

| | `(3)` | `(2,1)` | `(1³)` | floor | sum |
|---|---|---|---|---|---|
| bar-even (C) | **z-dep** | 0 | **z-dep** | z-free | **0**, every bar-even z |
| full-bar (D) | `(h²/2)·r` | 0 | `(h²/2)/r` | `−2q²h²/(q⁴+q²+1)` | **h²**, every full-bar z |

`r = (q²+q+1)/(q²−q+1)`; the two D defects are exact **reciprocal** multiples of
`h²/2`. At q₀ in units of h²: `(3)` 1.48922059503199, `(1³)` 0.16787304770965,
floor −0.6570936427416, `r(q₀)` 2.97844119006. `χ^(2,1)(Δ) = 0` identically, so
the phase is blind to the 2-dim block in both conventions.

**C's bar-oddness — what the whole C ladder's bare cosine rests on — is a
CANCELLATION between the symmetric and antisymmetric blocks, not a property any
block has.** Under D the cancellation dies and the per-block defects become
CONSTANTS: the z-dependence cancels *inside* each block, not *between* blocks.

**Consequence.** No z within the full-bar class changes the D defect, at block
resolution or in aggregate. The "choose a better z" direction is now closed from
**two independent directions** — the anchors (`qbeta_ladder_alpha_form_filter_probe`:
no constant z meets both the value and slope rows) and parity (this: the defect
does not depend on z at all).

### (A) refuted

Every `d_λ` is itself bar-INVARIANT — as a bar-defect always is
(`bar(bar X + X) = X + bar X`). Entry 12's silence survives block resolution
verbatim. Block resolution is **not** the different input entry 12 asked for.

### (B) refuted, and the failing half is ONE scalar

```
bar(chi^λ(Δ)) = chi^{λ'}(Δ)   EXACT, all three blocks, convention-free
bar(a_λ)     != a_{λ'}
bar(y_λ)     != y_{λ'}
```

The block CHARACTERS do carry Kohno–Drinfeld. The weights do not — but all three
residuals carry the **same factor `(z + zbar)`**, and solving them simultaneously
gives the unique action `zbar = −z`. So `y_λ` is conjugation-equivariant **iff z
is bar-ODD**, which is neither C (`zbar = z`) nor D (`zbar = z−h`). C's
bar-oddness is therefore **not** conjugate-partition equivariance.

### A distinguished fourth value, excluded twice

`z = h/2` is the unique bar-ODD member of the full-bar class (`bar(z) = z−h` AND
`bar(z) = −z`), so there the weights ARE conjugation-equivariant. Excluded by the
two-row cap (`qou-06wh`: admissible set exactly `{q, z_D}`) and by the anchor
filter (needs 0.499104480185 / +400.29; `h/2` gives **0.104530149398** /
**0.905826877183**). Recorded, not pursued.

### Not claimed

No `c_k`, no `K`, no Q_β movement — L2 stays 1279 ppb. Not a claim that no
D-frame resummation exists. Scope (a).

### Entry 15 read against the counit-hypothesis entry (merged from main, 2026-08-31)

The two landed in parallel and are **complementary, not overlapping** — recorded
so a later reader does not take them for one result stated twice.

  * The counit entry attacks the **trace** side: which `z` reproduces the
    required weight. Answer: neither admissible point (`z = q` 12.470 % off,
    `z_D` 43.157 % off), the point that fits (`z = 1`, counit) is proved
    excluded, and `z_required` forces a **negative** Wedderburn weight.
  * Entry 15 attacks the **bar-defect** side: the defect is z-FREE within the
    full-bar class, so no `z` in that class changes it.

They converge on the same conclusion from opposite directions — *the `z`
direction is closed* — and neither is evidence for the other. Together with the
anchor filter (`qbeta_ladder_alpha_form_filter_probe`) that is **three**
independent closures: trace weight, bar parity, and the anchors.

One cross-check worth stating because it is easy to conflate: entry 15's
distinguished `z = h/2` and the counit entry's `z = 1` are **different points**
excluded for **different reasons** — `h/2` by the two-row cap (it is the unique
bar-ODD member of the full-bar class), `z = 1` by `one_not_root`. Neither
exclusion implies the other.

---

## Entry 16 — the two-anchor filter on `K(δ)`: entry 12 measured the SMALLER of two quantities (2026-08-31)

`computations/qbeta/qbeta_n1_constant_two_anchor_filter_probe.py` — **9/9**,
mpmath 60 dps, **runs standalone with `PYTHONPATH` stripped**.
Audit: `docs/audits/2026-08-31-cds1-block-bar-defect-and-conjugation.md` (addendum).

Entry 12 asked for a "genuinely different input" on `K`. Entry 15 established
that neither block resolution nor Kohno–Drinfeld supplies one. This applies the
technique the **z-form filter** already uses — two anchors sharing `Q_codata`
exactly (asserted, not assumed) — to `K` instead of to `z`:

    K_required = Q_codata / ( Q_A * (1 - u^2) * cos(alpha - delta/2) )

### 1 — Neither admitted candidate reaches the VALUE, and that reframes entry 12

| | miss vs `K_required` | × the 7.797 ppb target |
|---|---|---|
| `K ≡ 1` | **281380 ppb** | 36088× |
| `K = cos(δ/2)` | **221686 ppb** | 28432× |
| *gap between the candidates* | *59694 ppb* | *7656×* ← **what entry 12 measured** |

**The choice between the two is not the blocker.** The N=1 factor is ~2.8e-4
short whichever is chosen. Entry 12 is not wrong about the gap — it is measuring
the smaller of two quantities, and the larger was never computed.

### 2 — The SLOPE misses by three orders, wrong sign

    required  dK/ddelta = +6.2399501753 (D)   +6.2934180689 (C)
    cos(delta/2)        = -0.0054631674        ratio -1142.19
    K == 1              =  0

### 3 — Candidate-free self-consistency

`K(0) = 1` + the value fix the MEAN slope over `[0, δ₀]` = **−0.0128759899**;
the filter fixes the LOCAL slope = **+6.2399501753**. Ratio **−484.62**. Any `K`
meeting all three is strongly non-monotonic on the scale of `δ`, with nothing in
the arc motivating it.

### Convention-INDEPENDENT — which is what makes it a statement about the FORM

C and D require slopes agreeing to **0.85 %**. The obstruction belongs to
`F = cos(a − δ/2)·K(δ)`, not to a convention choice.

### The slope is RED-TEAMED, unlike the z filter's

That one was a 2-point secant over `dq = 1.29e-8` and carried an explicit
caveat. This is a central difference **stable to 12 significant figures across
twelve orders of step size** (rel `1e-8`→`1e-20`, max spread 3e-15), with the
independent two-anchor secant reproducing it to 8.

### Scope — read the attribution

Scope (a). `K_required` holds `α` at the value **the form** gives, and `α` is
not derived — so a wrong `α` is absorbed into `K_required`. This does **not**
show `K` must equal 0.99972; it shows the **pair** `(α, K)` from this form
cannot reproduce both anchors. Form-level negative, consistent with and sharper
than the arc's standing conclusion that the form must change. No `c_k`, no fit,
L2 unchanged at 1279 ppb.

### Also: my own "next" recommendation was wrong twice, and the corpus said so

I twice recommended the **Habiro-element route** as the untried source for `K`.
Corpus-grep on `qou-i2ir` (in-progress, Route C f-map) shows the amplitude leg
is **already fenced**: C16 (not a formal Habiro element), C17 (qZeilberger,
O(1) residuals), C18 (PSLQ, entropy-blocked), and the Route-C amplitude route
itself REFUTED scope-(a) structurally by a one-scale/two-target gate
(`4λ₂³ + λ₃² = 6.088 ≠ 0`, a sum of positives) plus a √3-parity mismatch. That
fencing targets the **`c_k` rungs**, so it does not literally reach `K` — but
the route I was pointing at is not open ground, and I should have grepped before
recommending it rather than after.

### Entry 16b — `K` is OVERLOADED in this arc, and the two verdicts are opposite

Found while reading Step 14 against entry 16. Two different objects carry the
letter `K` in this bean, and a reader who transfers a verdict between them gets
the wrong answer in **both** directions:

| | what it is | verdict |
|---|---|---|
| Step 14's `K` | the trace → MeV scale, **outside the Hecke trace entirely**; a MeV-scale factor | **NEGATIVE** — enumerated 2026-08-29, nothing parameter-free within 6.31 % |
| entries 10c/12/16's `K(δ)` | the multiplicative constant in the N=1 factor `F = cos(a − δ/2)·K(δ)`, `K(0) = 1`; numerically ≈ 1 | **FREE** (entry 12), then filtered but **not determined** (entry 16) |

Take "K is closed, enumerated negative" from Step 14 and you close a question
that is open; take "K is free" from entry 12 and you re-open one that is
enumerated. Same class as the `alpha_eff` overload this arc **already flags**
(`qbeta_multi_block_eigenphase_probe` uses it for a dimension-weighted block
average), and as the `markovZ` / `markovZC` / `markovZc` family in AGENTS.md —
which is why the omission is worth recording rather than just fixing: the arc
has the habit and this one still slipped through.

Disambiguating notes added at all three sites so a reader arriving at any one of
them sees the collision: `qbeta_d_frame_terminus_probe.py`,
`qbeta_d_n1_constant_bar_silence_probe.py`,
`qbeta_n1_constant_two_anchor_filter_probe.py`. All three re-run exit 0.

**Not renamed.** Renaming either would churn a witness key and the arc's own
prose across a dozen entries; the notes are the cheaper fix and they put the
warning where the reader is. If a future tranche does rename, Step 14's is the
one to change — it is the later coinage and the less used.
## Where to look: the corpus names it — and the D generator is forced BAR-INVARIANT (PR #6282)

Owner asked where to look for a structural replacement for `cos(alpha_eff)`.
The corpus answers itself, and following the pointer gives two results. Probe:
`computations/qbeta/qbeta_d_habiro_generator_parity_probe.py`, 8/8, sympy exact.

### The place, already named

AGENTS.md:1828 — "Permanent fix is the Q_beta Habiro element". The Lean exists:
`QOU/BraidKnot/QBetaHabiroGeneratorRigidity.lean` carries the open class
`QBetaSingleHabiroGenerator` (verified: **NO instance**), conjecturing the tower
is ONE fixed generator, forcing the rank-1 law `c_{k+1} = rho*c_k` and
collapsing the per-rung freedom to `(rho, c_2)`.

It also already carries a **falsifiable test**: `hankel_minor_vanishes` /
`not_single_generator_of_hankel_ne` — a single generator REQUIRES
`c_2*c_4 = c_3^2`, and the corpus's fitted menu (`c_2=-1, c_3=-2, c_4 != -4`)
already fails it.

### Hypothesis (both results are conditional on it)

Under D each ladder factor `(1 + c_k X^k)` must be bar-INVARIANT, since Q_beta
is an observable and D's grading is multiplicative. Under C this does NOT apply
— C's action is affine, weights are not its grading — so nothing here is a
claim about the C ladder.

### Result 1 — the generator's parity is FORCED, and is not bar-odd

    X = u        bar(X)/X = q^2  ->  forced bar(rho)/rho = q^{-2}
    X = u*Vhat   bar(X)/X = 1    ->  forced bar(rho)/rho = 1   BAR-INVARIANT

Neither is `-1`. The class STATEMENT is parity-free
(`exists rho, c_{k+1} = rho*c_k`), so **nothing in Lean has to change**. It is
the DOCSTRING's intended bar-ODD "sinh partner" — dual to alpha_EM's bar-even
`[2]_q` — that is a C-frame reading and does not carry to D. **The D-frame
search target is a BAR-INVARIANT generator.**

### Result 2 — `c_2 = -1` discriminates after all, by WEIGHT not by VALUE

A previous entry of mine recorded that this test "does not discriminate". That
holds for its VALUE (the `x^2` coefficient of `1 - x^2` is `-1` for any `x`) and
I stand by it. Its BAR-WEIGHT is a different question:

    c_2 = -1 is a rational constant  ->  bar-ratio 1, weight 0
    X = u*Vhat requires w(c_k) = 0   ->  CONSISTENT
    X = u      requires w(c_2) = -4  ->  INCONSISTENT

So the one rung the corpus DERIVES rather than extracts is compatible with the
forced form and incompatible with the naive one — evidence from an
already-proved value, nothing fitted. This partially recovers a test I had
written off; the write-off was right about the value and wrong to stop there.

### Not claimed

That the forced form IS the D ladder — conditional on the bar-invariance
hypothesis, which is motivated but not proved. No `c_k` proposed, extracted or
wired. No instance of `QBetaSingleHabiroGenerator` produced. Scope (a).

### Other surfaces measured

`Faddeev` (165 content files), `quantum dilogarithm` (141), `q-Pochhammer` (41),
`cyclotomic completion` (13) — all carry MULTIPLICATIVE inversion relations, the
right shape for D's multiplicative action.

### The next move, concrete

Search for a bar-INVARIANT single generator (not bar-odd), test any candidate
against the already-formalized `c_2*c_4 = c_3^2` Hankel condition, and check its
`c_k` weights are all 0. Three gates, all pre-existing or derived here, none
requiring a fit.



## Correction: parity is a FILTER not a selector, and the Hankel gate is VACUOUS (PR #6282)

Two corrections to the method I proposed in the previous entry. Probe:
`computations/qbeta/qbeta_d_parity_is_a_filter_not_a_selector_probe.py`, 7/7.

**1. Parity is a filter, not a selector.** The corpus's `quantumInt` is the
SYMMETRIC convention `(q^n - q^-n)/(q - q^-1)`, and every symmetric q-integer is
bar-invariant — `[2]_q`, `[3]_q`, `[4]_q`, `[5]_q` all have bar-ratio 1. So the
parity condition admits the ENTIRE q-integer family at once. It rules out the
bar-ODD "sinh partner" reading (that result stands) but does **not** pick a
member. Reading the previous entry as "parity identifies the generator" would be
over-reading it.

**2. The Hankel gate is vacuous for rank-1 candidates.** I listed
`c_2*c_4 = c_3^2` as a gate on candidates. But rank-1 gives `c_3 = rho*c_2` and
`c_4 = rho^2*c_2`, so the condition holds IDENTICALLY for every `rho`. It
excludes non-rank-1 menus — which is what the corpus uses it for, against the
fitted menu — but cannot discriminate BETWEEN single generators. Listing it as a
candidate gate was my error.

**So of the three gates I named: one is a class filter, one is vacuous, and one
(the C-limit reduction) survives** — joined by the numerical value of
`c_3 = rho*c_2`, which I had not listed.

### A worked non-candidate, so it is not mistaken for a refutation

`habiroT25 = [3]_q/25` (`MmuR9V9Closure.lean:76`) IS bar-invariant and passes
the parity filter; with `c_2 = -1` it gives `c_3 = -0.1217` at the proton pin
against the extracted `-2.0693`. NOT a match — but `habiroT25` belongs to the
m_mu R9/V9 closure, NOT the Q_beta ladder. It refutes nothing; it is a different
object sharing a name. Recorded because it shows the shape of how the surviving
gates work: parity passes it, the value test rejects it.

### Honest status of the "where to look" answer

The place is named (the Habiro element, `QBetaSingleHabiroGenerator`, open with
no instance). The parity is now derived (bar-invariant, not bar-odd). What is
NOT available is a way to select the generator without either a new structural
input or a fit — the surviving gates test a candidate once you have one; they do
not produce one. That is the honest boundary of this arc.

### Scope against entries 10–10d, which landed on main while this was in flight

Entries 10/10b/10c/10d (sibling, now on `main`) answer the **N=1 slot** — the
leading `cos(alpha_eff)` factor — deriving `M = cos(a_D - h^2/4)*cos(h^2/4)` as
its bar-midpoint and Lean-proving it. That is a **different slot** from the one
above. The "honest boundary" I state is about the **product generator** (the
`rho` in `c_{k+1} = rho*c_k`), and is unaffected by their result: N=1 has a
derived candidate form, the generator does not.

The two results are consistent and complementary. Their entry 10 shows why C
could use a bare cosine (the midpoint rule is *vacuous* in C, since `alpha_C` is
bar-odd and cosine is even); my Result 1 shows the *generator's* forced parity is
bar-INVARIANT rather than bar-odd. Both are the same underlying fact — D's action
is multiplicative, C's is affine — read at two different slots of the ladder.

## CORRECTION to the previous entry — Result 2 tested a coefficient the corpus does not derive

Probe: `computations/qbeta/qbeta_d_n2_factor_bar_invariance_probe.py`, **13/13**,
sympy exact.

The previous entry argued that `c_2 = -1`, being a rational constant of bar-weight
0, is CONSISTENT with the forced expansion variable `X = u*Vhat_D` and INCONSISTENT
with plain `u`. The weight arithmetic is right. The object it was applied to is
not.

### What the corpus actually derives

AGENTS.md ties the derived rung to `u` **specifically**:

    "1 - b^2*hbar^4 = 1 - (b*hbar^2)^2, a one-line `ring` identity: it proves
     only that re-reading the N=2 factor in the ansatz form yields -1."

So the derived object is `1 - u^2`, in the variable `u` — not an abstract
`1 + c_2*X^2` whose variable is free to be chosen later.

### That object is not bar-invariant under D

    bar(1 - u^2) - (1 - u^2)  =  (1 - q^4)*u^2   != 0

exactly, since `w(u) = +2` (`b` is bar-invariant, `bar(hbar_q)/hbar_q = -q`, and
the sign squares away). Re-expressed in the forced variable:

    1 - u^2  =  1 - X^2/Vhat_D^2   ->   c_2^(X) = -1/Vhat_D^2,  weight +4

against the weight 0 the forced form requires. **INCONSISTENT.** The previous
entry's "CONSISTENT" verdict came from reading `-1` as the coefficient of `X^2`
when it is the coefficient of `u^2`; the two differ by `Vhat_D^2 = 1.27258` at
the proton pin — the same +27.3% k=2 rescaling the forced-form probe already
measured, arrived at from the other side.

### What this does and does not say

- **NOT** that `c_2 = -1` is wrong. It is correct in the frame it was derived in.
  What fails is its TRANSPORT to D. Scope **(a)**: a scope-limited negative about
  one construction, not a structural exclusion of anything.
- **NOT** a new refutation of the ladder. It is the same failure already
  established for `cos(alpha_eff)` (#6244) and for the product form (#6282),
  now shown for the third and last leg.

### The consolidated statement, which is cleaner than the three separate ones

All three legs of the C-frame instrument — the leading phase `cos(alpha_eff)`,
the product form `Prod(1 + c_k u^k)`, and the one structurally derived rung
`1 - u^2` — fail to transport to D, **for a single reason**: D's bar action is
multiplicative (a grading, `bar(x)/x = q^w`) where C's is affine. Nothing in the
C ladder is a bar-eigenvector, so nothing in it survives the change of frame
unmodified. That is a sharper result than "the ladder needs re-deriving": it says
the ladder has no D-frame reading at all, in any of its three parts.

The sibling's entries 10-10d supply the replacement for leg 1 (the bar-midpoint
`M = cos(a_D - h^2/4)*cos(h^2/4)`). Legs 2 and 3 have no replacement yet, and per
the previous entry the generator is not selectable without a new structural input
or a fit.

---

### 2026-08-31 — attack options: the D-frame trace COLLAPSES, and the assets exist

Question put: *we have a Habiro basis and D in terms of it — can we use that?*
**Yes**, and the D side is structurally **simpler** than C — the opposite of
what "blocked" suggests.

**ASSET 1 — the D-frame Habiro machinery exists and is LIVE.**
`habiro_mass_table_convention_attribution_probe.py`, run today: *"committed
reproduced by convention D : **25/25** … uniformly convention D: True"*, exit 0.
PR #5526 regenerated all 25 atoms into D (`cde2fbcd89`), probe kept as a
regression check. Four regenerators sit beside it
(`regenerate_y_lambda_{jones_markov,symbolic,orphans,sdp}_conventionD.py`) — the
`y_λ` weights are **already** convention D.

**ASSET 2 — at `z_D` the trefoil trace collapses to ONE closed-form term.**
`tr_M = Σ_λ y_λ χ^λ` with `χ^(3)=q³`, `χ^(2,1)=0` exactly (PR #1873),
`χ^(1³)=−q⁻³`. Two of three die for **independent** reasons: `χ^(2,1)=0` is a
convention-free character fact, and `y_(1³)=0` under D — exactly the Lean
characterisation this bean already cites
(`markovWeights_eq_jones_of_threeRow_eq_zero`: `y_(1³)=0 ⟺ z=z_D`), verified
against the live bridge. What remains:

> **`tr_M(trefoil)|_D = q³(q⁴+1)/(q²+1)²`**

Control: weights normalise exactly, `1·y_(3) + 2·y_(2,1) + 1·y_(1³) = 1`, so the
collapse is a property of the trace, not a truncation artefact.

**Why this reframes "not a z-swap", favourably.** Under C,
`decayLadder_zC_threeRow_ne_zero` forces `y_(1³) ≠ 0` for every `s=√q>1`, so the
C trace has **two** terms. The C→D move changes the trace's **rank**, not a
parameter value — this bean's own point — and it cuts the helpful way: **the
object to re-derive under D is smaller than the one under C.**

**OBSTRUCTION, named.** `qbeta_habiro_element_probe.py` records its divisibility
fact `D(u) = 4u¹⁹(1+u²)` as the convention-C denominator, explicitly *"true
under convention C, false under D"*. So the Habiro **basis** transfers while the
integrality/divisibility **lemmas** do not — they must be re-derived against the
collapsed D trace. That is the real remaining work, and it is **narrower than
re-deriving the ladder from nothing**.

**Recommended order.** (1) re-run the operator route
(`qbeta_ck_from_operator_markov_trace_probe.py`, the existing vehicle) with the D
weights and the one-term trace; (2) re-derive divisibility against the D
denominator — derive-anew, not port; (3) only then compare to the C-frame `c₃`,
and **not** to the −974 sensitivity number.

**Nothing here derives the ladder.** cds1 stays OPEN.


---

### 2026-08-31 — step 1 RUN, and REFUTED. Plus two findings under it.

**🛑 My own recommended step 1 is closed, and I should have run the existing
probe before recommending it.** `qbeta_ck_local_taylor_around_u0_probe.py` had
already evaluated the route and returns FAIL with a structural diagnostic:

> `R := tr_M(trefoil)/[Q_A·cos(α_eff)]` is **NOT** the correct global ladder
> target `Π_k(1+c_k u^k)` … R's Taylor coefficients grow with ratio ~90 around
> `u₀` (radius ≈0.011), whereas an O(1) ladder would have singularities at
> `|u| ~ 1`. … **the c_k are PER-RUNG operator identities at each truncation
> level N=k. Aggregating them via `tr_M` of the trefoil gives the WRONG global
> function.**

This kills the route **independent of C-vs-D**. So last entry's one-term D trace
`q³(q⁴+1)/(q²+1)²` is a true closed form but **irrelevant to the ladder** — the
ladder is not extracted from the global trace at all.

**FINDING A — the per-rung route's own anchor is C-frame.** This bean's table
already records it and the probe confirms it live:
`implied c₂: C −1.0176238, D −9.2988629 (proved: −1, C frame)`, with the
assertion `implied_c2_is_minus1_in_C_frame_only` **passing**. So "derive each
`c_k` as a per-rung operator identity" cannot use `c₂ = −1` as its gate under D.
**Both routes are blocked at the ANCHOR, not at the extraction** — which is a
sharper statement of what this bean needs than "re-derive the ladder".

**FINDING B — this bean cites the sensitivity probe as 9/9; it is committed at
8/9.** `qbeta_c3_ladder_trace_convention_sensitivity_probe.py` fails
`C_frame_regression_matches_committed_corpus_values`, and the **committed
witness on disk already records `allPassed: False`** — pre-existing, not a
container artefact. The substance:

| | probe computes | registry asserts | diff | tol |
|---|---|---|---|---|
| C proton | −2.06934257712 | −2.06934258 | 2.9e-9 | 1e-6 ✓ |
| **C muon** | **−2.01986031187** | **−2.02020024** | **3.4e-4** | 1e-6 ✗ |

**340× the tolerance, muon anchor only** — and the muon anchor is where `q₀` is
pinned. Note −2.01986 is neither the live −2.02020024 nor the superseded
−2.0097; it is a third value. Too large to be the container's mpmath 1.3.0 vs
the recorded 1.4.1.

**Witnesses NOT committed** — this container's environment is weaker than the
recorded one (mpmath 1.4.1→1.3.0, numpy 2.5.0→2.4.6, python 3.13→3.11), and the
probes' own guards say so; I reverted the timestamp-only changes rather than
downgrade the provenance.


## FINDING B — RESOLVED and CLOSED (2026-08-31, commit 636c1541c0)

**It is not a third value; it is `qou-t39x`.** Finding B above reports
`-2.01986031187` as "neither the live `-2.02020024` nor the superseded
`-2.0097`". It is the live one. `-2.02020024` is the superseded one:
`fca08de7d2` (2026-08-22, owner ruling) moved the muon pin to CODATA 2022 three
weeks before Finding B was written, and the probe's regression target stayed on
CODATA 2018. Attribution, at 60 dps (probe
`qbeta-c3-muon-anchor-codata-edition-attribution`, 11/11):

| quantity | value |
|---|---|
| disagreement `corpus − c_3(2022)` | −3.3992813e-4 |
| edition shift `c_3(2018) − c_3(2022)` | −3.3992315e-4 |
| **explained fraction** | **0.9999853535** |
| residual | −5.0e-9 = the corpus literal's own rounding to its 9 quoted figures |

The lever is `1/u³ = 1.618e6`: a **1.451 ppb** step on `m_μ/m_e`
(206.7682830 → 206.7682827) is **1.7e-4 relative** on `c_3`, amplification
2.1e6. The proton arm never warned because `m_p/m_e` moved 2e-12 relative
against the muon ratio's 1.5e-9.

**One correction to what Finding B records above:** "the committed witness on
disk already records `allPassed: False`" — it does not. The witness records
`allPassed: true` with `c_3(muon) = -2.020200235021255` and
`computedAt 2026-08-15`, i.e. generated *before* the re-pin. Stale but
internally consistent, which is worse to read and better to fix. Fixed.

### THE EXPERIMENTAL IDEAL — and this is the part that matters for the bean

Nothing had priced `c_3` against the CAL inputs it is built from. Recomputing at
±1σ of each CODATA-2022 published uncertainty (not through a recorded
derivative):

| input | rel. σ | δc_3(proton) | δc_3(muon) | δ(swing) |
|---|---|---|---|---|
| CAL-2 `m_μ/m_e` | 2.225e-8 | 0 | 5.212e-3 | 5.212e-3 |
| CAL-2′ `m_p/m_e` | 1.743e-11 | 3.54e-6 | 0 | 3.54e-6 |
| CAL-1 `m_e` | 3.131e-10 | 5.068e-4 | 5.068e-4 | 3.06e-10 |
| `Q_β` | 7.797e-7 | **1.2619** | **1.2619** | 7.63e-7 |
| **total** | | **1.262** | **1.262** | **0.005212** |

**`c_3(muon) = −2.0199 ± 1.26`, `Q_β`-dominated** — 0.78 ppm on a 0.782 MeV
Q-value times `1/u³`. The registry quotes **nine** significant figures for a
quantity its own calibration inputs support to **0.2** of one, and the 3.4e-4
Finding B calls "340× the tolerance" is **3700× *inside* the error bar**. The
1e-6 is a *reproducibility* tolerance being read as a physics one.

**The cross-anchor swing survives, and it is the only thing that does.** `Q_β`
and `m_e` are common mode and cancel in the difference to 7.6e-7 and 3.1e-10,
leaving **swing = −0.0494823 ± 0.0052 = 9.49σ** — the same 9.5σ as the μ–p
tension, because it is the same statement. So the "REFUTED as real-q fibre
element" verdict, which rests on the swing, is experimentally supported while
every absolute `c_3` digit past the first is not. **That asymmetry is the usable
result for this bean**: a D-frame re-derivation must be validated against the
swing, not against an absolute `c_3` target, because no absolute target here
carries more than one supported figure.

### What was changed in live compute

- **sensitivity probe** — target retargeted to CODATA 2022, anchor-qualified,
  with the 2018 literal kept and asserted-against so a slide back is caught
  rather than re-diagnosed. **9/9 → 10/10**, witness regenerated under
  mpmath 1.4.1 (matching its recorded provenance — no engine downgrade; the
  container was upgraded 1.3.0 → 1.4.1, which is what unblocked this).
- **`c3_even_canonical_split_contradiction.py`** — was itself a straddle
  (frozen pin + CODATA-2018 `c_3`); both anchors now derived from the substrate
  and licensed against the corpus proton value.
- **`sleak_offset_genericity_check.py`** — anchors derived; window moves to
  (2.01986, 2.06934), Vol(4₁) still strictly inside, conclusion unchanged.

### Two more CODATA-2018-era literals the same step surfaced

1. the 2026-07-07 audit's **`S(muon) = 886.8`** is now **3.17× outside its own
   4-s.f. rounding window**; at the live pin it reads **886.6**.
2. **KC21's Φ_b scale claim degrades 3.01 % → 6.63 %**, i.e. **2.2× worse**. The
   deficit 0.0094 is anchor-blind to sub-ppm, so all the movement is on the |S|
   side — the quoted "~2.9 %" was never a property of the saddle. The verdict
   now computes it rather than asserting it.

**STILL OPEN** (not done here, deliberately): ~20 prose/Lean/TS sites still
carry `−2.02020024` as "today's muon extraction", including
`SLeakZeroCrossing.lean`, `FaddeevModularDouble.lean`,
`ThetaLipschitzObstruction.lean` and `qbeta-ck-truncation-canonical.ts`; and the
registry's KC21 row and §9f window endpoints. Re-pinning
`Q_MUON_50_DIGIT_STR` / migrating the 336 ancestor-bearing files is
owner-authorised work sequenced behind PR #5500 and `qou-1c4y`.


## Step 15 (2026-08-31) — the anchor question, answered: there is no D-frame anchor

Finding A left this bean at *"both routes are blocked at the ANCHOR, not the
extraction"*. Rather than hunt for a D-frame anchor, I asked whether one **can**
exist. It cannot, and the reason is measurable. Probe
`qbeta-d-frame-z-determinations-experimental-budget` (8/8), muon pin, 60 dps,
commit `c6b88d78ea`.

**Method.** Every CAL input shifted ±1σ of its CODATA-2022 published
uncertainty, with **both ends of each gap recomputed together** — `q₀` is itself
a function of `m_μ/m_e`, so the cap and the mass determination are correlated
and a naive per-quantity bar is wrong in both directions.

| gap | value | 1σ | significance |
|---|---|---|---|
| mass − cap | 1.246002e-4 | 1.3123e-5 | **9.49479 σ** |
| decay − cap | 3.858123e-1 | 6.9705e-7 | **553 497 σ** |
| ladder anchor − `z_C` | −2.107e-4 | 1.3161e-4 | **1.60089 σ** |
| ladder anchor − cap | −1.1358e-1 | 1.3161e-4 | **862.989 σ** |
| `c₂(z_C) + 1` | −1.7202e-2 | 1.0748e-2 | **1.60058 σ** |
| `c₂(z_D) + 1` | −8.298441 | 1.0741e-2 | **772.583 σ** |

### 1. 🛑 The mass channel does NOT confirm the cap — correcting my own entry above

The 2026-08-31 section above says *"an independent, non-circular measurement puts
`z` essentially where the derived cap puts it… the anomaly is localised to the
decay channel, not the convention."* **The "0.0203 %" is 9.49 σ.** It is four and
a half orders of magnitude closer than decay and it is still a decisive
disagreement. Both channels disagree with the derived cap; decay disagrees
5.8e4× harder. The localisation claim needs that qualification, and the leverage
caveat I attached (`d ln tr_M/d ln z = 0.00119`) was the right instinct pointing
at the wrong conclusion — leverage is *why* the σ is large, not a reason the
percentage is reassuring.

### 2. Three corpus facts are ONE measurement

| fact | σ |
|---|---|
| μ–p substrate tension (11.614 ppb) | 9.49362 |
| `c₃` cross-anchor swing | 9.49363 |
| mass-vs-cap gap in `z` | 9.49479 |

They agree to **0.0123 %** because all three **are** `(q_muon − q_proton)`
divided by CODATA's bar on `m_μ/m_e`. The corpus carries them as three separate
facts in three coordinates. Anything that explains one explains all three, and a
proposal that moves one without the others is inconsistent.

### 3. `c₂ = −1` is a 1.6 σ empirical statement — both standing readings are wrong

`implied c₂(z_C) = −1.0172 ± 0.0107` (bar = `Q_β`'s 0.78 ppm ÷ `u² = 7.3e-5`).

- The extraction's **"−1.0176 vs −1"** is **not** a 1.76 % miss — it is
  **agreement at 1.6 σ**.
- The red team's **"symbolic-exact"** overstates it the other way: the Lean is
  the ring tautology `1 − (bℏ_q²)² = 1 − u²` and the N=2-factor identification is
  asserted in a docstring, so what actually supports `c₂ = −1` is *this* 1.6 σ,
  nothing stronger.

Under D the same quantity is **−9.2984, i.e. 773 σ from −1**.

### 4. The ladder's anchor is itself a measurement of `z`, and it selects C

Solving `implied c₂ = −1` for `z` at fixed `q` gives a **fourth determination**:

    z = 0.499110 ± 0.000132    →  1.60 σ from z_C,  863 σ from the derived cap

(the other `cos` branch is `z = 1.599`; **neither** is decay's 0.9985). So the
ladder is not merely *written* in convention C — its empirical anchor
independently measures the Markov parameter and lands on `z_C`.

### THE ANSWER FOR THIS BEAN

**There is no D-frame anchor.** The object that would play `c₂ = −1`'s role
under D is excluded, by the same data that supports it under C, at 773 σ. So
*"re-derive the ladder under D"* **cannot proceed by finding a D-frame `c₂`** —
the ladder's **functional form** has to change, not its parameter. That is the
anchor-side statement of what `decayLadder_zC_threeRow_ne_zero` says
structurally, and it converts this bean's open item from "find the D-frame `c_k`"
into "derive the D-frame decay functional", which is a different and larger job.

### 5. The two decay-side functionals disagree with each other

The trace reduction wants `z = 0.9985`; the ladder wants `z = 0.4991`. Both claim
to reproduce the same `Q_β`, so reconciling them needs a scale `K` off by
**2.2656× (126.6 %)** — **20× outside** Step 14's 6.31 % parameter-free wall. So
this is not a missing normalisation of the kind already enumerated, and at most
one of the two functionals is the right reading of the decay channel. That is a
sharper form of Step 14's terminus.

**Control:** cap and mass reproduce the committed values to **1e-15** through the
symbolic Borromean trace (imported from `qbeta_z_symbolic_borromean_crosscheck`,
not re-spelled); decay to **1.49e-8**, asserted as a tolerance because `F` is
reconstructed from the 2026-08-29 witness rather than re-derived.

**Scope-(a).** Nothing derived, proposed, wired or readmitted; no convention
adjudicated; no `c_k` value changed. A `z` near an inadmissible point is TENSION,
not permission — `one_not_root` stands, as does the derived two-row cap.

**Recommended next**, and it is a judgement not a fact: the three-facts-one-
measurement identity (§2) says the μ–p tension is the single unexplained
residual behind the mass side, so the decay side is where new information can
come from — and §5 says the first question there is *which of the two decay
functionals is right*, since they cannot both be. That is answerable without
re-deriving anything: it is a question about which object `Q_β` is a trace of.


## Step 16 (2026-08-31) — the two decay functionals are ONE functional. Protium settles it.

Step 15 asked which decay reading is right. **Neither — the question was
malformed.** Probe `qbeta-decay-functional-unification-protium` (6/6), Lean
`QOU/QBeta/DecayFunctionalUnification.lean` (5 theorems, sorry-free, axioms
`[propext, Classical.choice, Quot.sound]`), write-up
`docs/audits/2026-08-31-qbeta-decay-functional-unification.md`. Commit `a949c94115`.

### Protium is what makes it checkable

β decay's daughter is the **neutral atom**, so `n → ¹H + ν̄` has
`Q_β = m_n − m(¹H)` — an **atomic** difference, larger by exactly `m_e` than the
nucleon difference `m_n − m_p` that the corpus's `Δ = NF(n) − NF(p)` notation
suggests. Priced with the corpus's own derived scale `𝔈₀ = m_e/(q₀(q₀−1))`
(CAL-1 + CAL-2 only, no fit):

| | vs atomic `Q_β` | vs nuclear `m_n − m_p` |
|---|---|---|
| `𝔈₀·\|ε(Δ_S)\|` | **0.168 %** | −39.41 % |
| `𝔈₀·\|net(Δ_L = n−p)\|` | 21.55 % | −26.48 % |
| `𝔈₀·\|net(Δ_β = n−¹H)\|` | 5.60 % | −36.12 % |

**235× discrimination, zero free parameters. `Δ_S` is already an ATOMIC object**
— the emitted electron is inside it, and the `NF(n) − NF(p)` notation misleads
about what the element is.

**And the protium ELEMENT is refuted.** `Δ_β := NF(n) − NF(protium)`, the naively
correct β-decay difference, **double-counts**: on the physical pairing its
nearest required `z` is **0.4439** from the derived cap, *worse* than the
corpus's **0.3858**. (One off-diagonal cell — atomic element vs the *nuclear*
target — is nearer at 0.3386; unphysical pairing, still 55 % from `z_D`, rescues
nothing.) 🛑 Recorded because my first draft asserted *"every protium z is
further from the cap"* and the data refuted it.

### The unification

`ε(Δ_S) = h²/2 − h` is `tr_M^z(Δ_S)` at `z = 1`, and

    𝔈₀ · (−ε(Δ_S))  ≡  Q_A        identically in q and m_e

**This identity is NOT new** — it is `prop:neutron-qvalue-symbolic`, restated in
`qbeta_delta_tr_vs_formA.py`. New is the consequence nobody had drawn: the
ladder's leading term **is** the trace functional at `z = 1` with `K = 𝔈₀`, so
the two readings share it *by construction*, and equating them forces

    Π_k (1 + c_k u^k) = affine(z) / cos((z−1)h/2 − u/2),
    affine(z) = (2qz − q² + 1)/(2q − q² + 1),   affine(1) = 1

The trace side is **exact and affine in z**. So the `c_k` are the mismatch
between an affine function of `z` and a cosine of one — a **reparametrisation
residual**, the **third** instance of AGENTS.md's STRICT *"defined residual ≠
derived decomposition"* class after `S_leak` and `S`. Consistent with what the
corpus already recorded: *"α … a square-root branch point 0.062 % above q₀,
manufactured by writing a smooth correction as a cosine."*

### Why the routes reported different z

Both invert **their own** correction function to the same measured
`Q_β/Q_A = 0.998325`. At `z = 1` the affine slope is **1.116732**, the cosine's
**4.4515e-4** — a factor **2508.65**. That is the entirety of "0.9985 vs
0.4991"; it was never two physical claims.

### 🛑 Two withdrawals, both Step 15's and both mine

1. *"the two decay-side functionals disagree … reconcilable only by a scale `K`
   off by 2.2656×, 20× outside Step 14's 6.31 % wall"* — **withdrawn**. No scale
   gap: the leading terms are identical, and `F_REQUIRED_TRM = 1.75923699` is
   exactly `(Q_β/Q_A)/affine(z_D)`, reproduced to **3.6e-9**.
2. *"at most one of the two functionals is the right reading"* — **withdrawn**.

Step 15's other findings stand unchanged: mass-vs-cap 9.49 σ, decay-vs-cap
5.5e5 σ, `c₂ = −1` at 1.6 σ under C and 773 σ under D, three-facts-one-measurement.

### What this does to the bean's primary item

**"Re-derive the `c_k` ladder under D" has no hidden answer to find.** Given `z`
the ladder is *defined* by the equation above; under D you substitute `z_D` and
read off whatever comes out. That is *why* both routes were "blocked at the
anchor" in Step 15 — there is no independent object for an anchor to pin.

The live question is narrower and different in kind: **should the cosine
parametrisation exist at all?** The trace side is exact, affine, and needs no
series; the whole `c_k` tower exists because that affine correction was rewritten
as `cos(affine)`. Removing the cosine removes the tower — and with it the
`c₂ = −1`, `c₃ ≈ −2 = J_Hopf(1)` and `c_{k≥4}` program.

**NOT claimed:** that the cosine is wrong, that the framework is wrong, or that
`Q_β` is closed. The decay channel's **5.5e5 σ** tension with the derived cap is
untouched by any of this and remains the open problem — this step says only that
the tension has ONE form rather than two, and that the `c_k` are not where it
lives.


## Step 17 (2026-08-31) — the cosine is unfalsifiable. Phase yes, cosine no.

Probe `qbeta-cosine-parametrisation-justification` (7/7), Lean
`QOU/QBeta/CosineParametrisationUnfalsifiable.lean` (3 theorems, sorry-free,
axioms `[propext, Classical.choice, Quot.sound]`), write-up
`docs/audits/2026-08-31-qbeta-cosine-parametrisation-justification.md`. Commit
`b19a6ede64`.

### What was already closed, and I nearly re-derived it

`QOU/QBeta/BraidImageEigenphaseExclusion.lean` (this bean, already landed) leaves
three ways a transfer matrix with spectrum `{e^{±iα}}` could earn the cosine and
closes two: `EigenphaseCarrier` is **vacuous**, the braid-image branch is
**excluded in every convention**, and "M arbitrary" is **circular**. Only a
**KZ/Kohno–Drinfeld holonomy** survives, and nothing supplies one. Read it before
re-opening this.

### The quantitative half (proton pin, convention C, 50 dps)

| quantity | value | in σ of `Q_β/Q_A` |
|---|---|---|
| 1σ on measured `Q_β/Q_A` | 7.784e-7 | 1 |
| `cos(θ)` explains, of the 0.167 % deviation | **95.599 %** | — |
| …without the `−u/2` offset | 81.756 % | — |
| `\|cos θ − (1 − θ²/2)\|` — the cosine's **own signature** | 4.274e-7 | **0.549** |
| residual the `c_k` tower absorbs | 7.382e-5 | **94.836** |
| **ratio** residual / signature | | **172.7×** (D: **4039×**) |

**The phase does real work** — 95.6 % of the deviation, zero free parameters, and
the `−u/2` offset is part of it. **The cosine does none the data can see**: its
entire content beyond a parabola is *half a standard deviation*, against a
*ninety-five sigma* residual it fails to explain. Any function agreeing to second
order fits identically and leaves the same tower. Under D the cosine explains only
59.8 %.

**And it discards information.** `cos` is even, so `z = 0.4993` and `z' = 1.5822`
share `cos = 0.998399` while their exact corrections are **0.4409** and
**1.6501**. The exact correction is affine in `z` hence injective — the algebraic
form of the "square-root branch point 0.062 % above q₀".

### Warranted vs not

**Warranted:** the correction is `1 − θ²/2` within the experimental resolution.
**Not warranted by anything measured:** that it is a *cosine*; that `θ` is an
*angle*; that a rotation or unitary is behind it; or that the residual should be
expanded **in powers of `u`** at all. The anchor constrains exactly **one**
number (7.382e-5) — so `c₂ = −1` is an assumption and `c₃` is what is left after
it. **One measurement cannot determine a series.**

### 🛑 Correction to Step 16 — mine

*"The two decay functionals are one functional in two coordinates"* and *"the
`c_k` are the affine-vs-cosine reparametrisation residual"* are **overstated**.
The identity `Π = affine(z)/cos(θ(z))` needs both sides at the **same `z`**; the
corpus's ladder **fixes** `z = z_conv` and lets the `c_k` absorb, while the trace
route **frees** `z`. At `z_C`:

    affine(z_C)           = 0.4409      <- 55.84 % from the data
    corpus ladder product = 0.999926
    Step 16 printed         0.441582    <- affine/cos, which the ladder is not

They are two **allocations** of one residual with different free parameters, not
one functional. **Surviving Step 16 unchanged:** the bridge `𝔈₀·(−ε(Δ_S)) ≡ Q_A`;
both corrections `= 1` at `z = 1` (so leading-order agreement is automatic and
uninformative); every protium finding (`Δ_S` atomic, 235×; protium element
refuted); and `F_REQUIRED_TRM = (Q_β/Q_A)/affine(z_D)` to 3.6e-9 — hence Step 15's
withdrawal of "K off by 2.2656×" stands too. Banner added to the Step-16 audit.

### Where the bean's primary item now stands

*Re-derive the `c_k` ladder under D* has **three** independent problems, none of
them "the algebra is hard":

1. **No anchor** (Step 15) — `c₂ = −1` is 1.6 σ under C, excluded at 773 σ under D.
2. **No derivation for the parametrisation** (`BraidImageEigenphaseExclusion` +
   Step 17) — two of three branches closed, and the survivor is empirically
   indistinguishable from a parabola.
3. **Under-determination** — one measured number, a series of coefficients.

**Recommended next, and it is judgement:** the productive direction is **branch
3** — supply a KZ/Kohno–Drinfeld connection whose holonomy *is* the phase. That
would justify the cosine independently of the anchor and give the tower a reason
to exist. The alternative is to state the correction as what the data supports,
`1 − θ²/2`, and retire the tower. Both are owner calls; neither is done here.


## Step 18 (2026-08-31) — branch 3 narrows to one requirement: an ELLIPTIC generator

Attacked branch 3 (= `qou-pdix` route 5). Read that bean first — it is further
along than this one records: routes 1–4 closed, route 5's constant-residue horn
closed by `PhaseFailsLogFunctionalEquation`, and the old acceptance test retired
for a two-tier D1–D6 replacement.

**What I added** (probe `qbeta-holonomy-spectrum-sign-obstruction` 6/6, Lean
`QOU/QBeta/HolonomySpectrumSignObstruction.lean` 6 theorems sorry-free, audit
`docs/audits/2026-08-31-qbeta-holonomy-spectrum-sign-obstruction.md`, commit
`4471ee72ce`): route 5's **three remaining survivors close at once**.

The correction the holonomy must produce is **strictly below 1** (`Q_β/Q_A =
0.998325`; ladder cosine `0.998399` C / `0.998999` D). A **real-spectrum**
generator gives `cosh a ≥ 1` for *every* real `a` — quantified over all `a`, so
**residue-independent**, which is why it reaches the q-dependent, non-flat and
q-dependent-parameter cases the doubling identity could not. Kohno–Drinfeld's own
scale-fixing `ħ = 2 ln q` is **real** at real `q₀ > 1`, giving character
`(q+1/q)/2 = 1.005448` with excess `(q−1)²/(2q)` — a square, so never negative.
**Wrong side of 1.**

**Branch 3 is therefore not closed but narrowed to one requirement**: an elliptic
generator (`det A > 0`, spectrum `±iθ`, `θ = 0.0565947`) at real `q`, against
Kohno–Drinfeld's `det A = −(ln q₀)² < 0`. The imaginarity must come from
somewhere, and `conj:im-q-physical-role` is the corpus's name for that place.
Added as **tier-0 (D0)** to `qou-pdix`'s acceptance test.

**Where the primary item stands after Steps 15–18.** *Re-derive the `c_k` ladder
under D* has four independent blockers, none of them "the algebra is hard":

1. **No anchor** (Step 15) — `c₂ = −1` is 1.6 σ under C, excluded at 773 σ under D.
2. **No derivation for the parametrisation** (Step 17 + `BraidImageEigenphaseExclusion`).
3. **Under-determination** — one measured number, a series of coefficients.
4. **Branch 3 needs an elliptic generator** (Step 18) — and nothing supplies one.


## Step 19 (2026-08-31) — Im(q) refuted as the elliptic source; "no tower" quantified

Probe `qbeta-imq-elliptic-generator-refutation` (8/8), Lean
`QOU/QBeta/ImQCannotSupplyEllipticGenerator.lean` (4 theorems, sorry-free), audit
`docs/audits/2026-08-31-qbeta-imq-elliptic-generator-refutation.md`. Commit
`f65a953dd3`.

### Part 1 — `conj:im-q-physical-role` cannot supply the elliptic generator

**Route A, `Im(q)` as a phase coordinate.** Generator eigenvalues are `±ln q`,
purely imaginary only if `|q| = 1` — impossible, since `Re q = 1.10998 > 1`
forces `|q|² > 1` for **every** `Im q`. The only move left is a complex character
with the real part kept, and it costs more than it buys:

| | |
|---|---|
| threshold for `Re[character] < 1` at all | `\|Im q\| > 0.122819` (11.07 % of `Re q`) |
| `Im q` to hit `Re[character] = 0.998399` | **±0.139956** (12.61 %) |
| resulting `Im[character]` | **0.014069** = **8.40×** the deviation = **18074 σ** |

`Q_β` is real, so that must vanish — and with `|q|² > 1` the factor `1 − 1/|q|²`
is strictly positive, so it vanishes **only** at `Im q = 0`, returning the
character to `≥ 1`, which the sign obstruction already excludes.

**Route B, non-Hermitian deformation.** An elliptic generator forces
unit-modulus braiding eigenvalues, but Kohno–Drinfeld fixes `ħ = 2 ln q` by
matching the Hecke pair `{1.109979, −0.900918}`, neither of modulus 1. It fails
not on the data but by **dissolving the scale-fixing the route depends on**.

**This does NOT refute `conj:im-q-physical-role`** — its chirality role is
untouched and `Im q` may be physical for other reasons. What is settled is that
it cannot supply the elliptic generator.

### Part 2 — "retire the tower", quantified

The **tower** is the sequence `c₂, c₃, c₄, …` in powers of `u`. Retiring it does
**not** drop the correction:

| | value | σ |
|---|---|---|
| correction needed | 0.998325 | — |
| `1 − θ²/2` (no cosine, no tower) | 0.998399 | — |
| residual `δ` | **−7.3394e-5** | **94.29** |
| `c₂ = −1` predicts `−u²` | −7.2543e-5 | **98.84 %** of `δ` |
| left for `c₃` **and all above** | −8.5042e-7 | **1.09** |

`δ` is real and large; `c₂ = −1` consumes almost all of it; what remains to
determine `c₃` **and every coefficient above** is one marginal number. Absolute
bar `σ/u³ = 1.2598`, reproducing Step 15's independent **1.2619**.

**And `c₃`'s central value is an artefact, not merely imprecise:** `−2.069343`
through `cos` (reproducing the committed proton `−2.06934258`, which validates
the extraction) against `−1.376381` through `1 − θ²/2` — a **33.49 % shift** from
a choice the data resolves at **0.549 σ**.

So "no tower" means writing `Q_β = Q_A·(1 − θ²/2)·(1 + δ)` with `δ` measured,
rather than asserting `δ = c₂u² + c₃u³ + …`. *One measurement determines one
number; it cannot determine a series.*

### The fork, both arms now priced

| arm | status |
|---|---|
| take `conj:im-q-physical-role` as the elliptic source | **refuted** (Step 19) |
| retire the cosine, state the correction as `1 − θ²/2` | **coherent**, costs only the tower, not the correction |

Route 5 is not closed — an elliptic generator from some *other* source stays
logically open — but the one place the corpus had named as a source of
imaginarity is excluded. **This is an owner call now, not a measurement
question**: Steps 15–19 have priced everything that can be priced without
choosing.


## Step 20 (2026-08-31) — Bring's elliptic curve: right KIND of source, no phase

Owner: *"Bring's surface has an elliptic curve naturally associated"*. It does.
Probe `qbeta-bring-elliptic-generator` (5/5), Lean
`QOU/QBeta/BringEllipticCurveJInvariant.lean` (3 theorems, sorry-free).

**Guard against a pun, stated first:** "elliptic generator" (elliptic element of
SL₂) and "elliptic curve" are different senses. The bridge is **KZB** — the
elliptic analogue of KZ — which lives on an elliptic curve and whose monodromy
genuinely carries `exp(2πiτ)` factors. That is where imaginary spectrum can enter
a Drinfeld–Kohno construction, which Step 18 showed is missing.

**Why it is the right kind.** A flat **unitary** connection on a torus has
monodromy in `U(1)×U(1)` — elliptic by construction. So this is the **first
candidate source of imaginarity to pass tier-0 D0 at all**, where `Im(q)` failed
(Step 19). And it is not a foreign import: the corpus already carries a *"Bring
color-tube (n=10 substrate)"* route in the **mass** sector (m_p ≈ 938 MeV,
−670 ppm).

**The curve** (library: Riera–Rodríguez, *Period matrix of Bring's curve*, Pacific
J. Math. 154 (1992), held in full). Serre: Jacobian isogenous to **E⁴**,
`E : y² = x³ − 675x − 79650`, **`j = −25/2`**, period matrix diagonalising to
`(5τ, 5τ, 5τ, τ)`. `j` re-derived from the equation, not transcribed.

**And it supplies no phase:**

1. **`j = −25/2` is not a CM invariant** — every CM `j` is a rational *integer*;
   `−25/2` is not even an algebraic integer. So **E has no complex
   multiplication**, `τ` has no closed form, and the curve hands the ladder no
   *derived* number — which was the whole appeal of "naturally associated".
2. **`Re τ = 1/2` exactly** (forced by `j` real and negative), so the natural
   angle `2π·Re τ = π` is a **sign**, not a tunable phase.
3. **Nothing lands.** Ratios to `θ_required = 0.0565947`: **55.5, 277.6, 27.8,
   0.0501** — closest a factor of **19.94**. The four comparisons were declared
   *before* computing and are reported in full including the misses; no search
   over combinations was run.

**Verdict:** structurally the best candidate the arc has had; quantitatively
empty. The **direction is not refuted** — a KZB construction on E is untouched
and is where an elliptic generator could still come from — but this curve at face
value gives nothing.

**Provenance caveat:** the library copy is OCR of a scanned page, garbled in
places. Only legible, independently checkable parts are used. The paper's own
`τ₀` is pinned by **two** j-values, the second illegible in this scan, so `τ₀` is
**not** reconstructed — only the SL(2,ℤ) representative with `j = −25/2`.
Recovering `j(5τ₀)` from a clean copy is the obvious next step if anyone wants to
push this.


## Step 21 (2026-08-31) — τ₀ is not CM; the jet tower is blind to decay

Probe `qbeta-bring-tau0-and-jet-tower-closure` (6/6), Lean
`BringEllipticCurveJInvariant.lean` (extended) + `JetTowerBlindToDecay.lean`
(both sorry-free, axioms clean).

### Theorem 2, decoded by DERIVATION

No clean scan was needed. Given `j(τ₀) = −25/2`, the possible `j(5τ₀)` are exactly
the six roots of `Φ₅(−25/2, Y)`. Computed independently, one is **−3810.78125 =
−5·29³/2⁵ = −121945/32** — decoding the OCR's `- 293x5` whose `2⁵` exponent had
been rendered onto its own line.

> **THEOREM 2:  `j(τ₀) = −5²/2`,  `j(5τ₀) = −5·29³/2⁵`**

**And the answer is NO.** Both are **non-integral** rationals: `v₂ = −1` and
`−5`. A CM j-invariant is an algebraic integer; negative 2-adic valuation is
potentially *multiplicative* reduction at 2 (Tate curves), exactly what CM
forbids. **τ₀ is not a CM point** — no closed form, no derived phase. The
hypothesis is refuted.

### The Gröbner–Shirshov jet tower is blind to decay

The q-Plancherel weight `W_λ = [k]_q!/(∏_cells [h(c)]_q)²` depends on λ **only
through its hook multiset**, which transposition permutes; and transposition
swaps the trivial and sign branchings. `λ ↦ λ'` is an involution, so

    w_sym(k) = w_alt(k)   EXACTLY, every k, every q.

Verified: **zero** counterexamples to hook-multiset transpose invariance over
every partition of every `k ≤ 9`; `|w_sym − w_alt| ≤ 7.3e-40` at 40 dps for
k=3..9 (exactly 0 for k=3,4,5).

Mass sees `y₃ + y₍₁³₎`; decay sees `y₃ − y₍₁³₎`. **So the tower's decay
contribution is identically zero at every level — no phase can hide there,
because the tower contributes nothing at all to the channel that needs one.** The
mass sector is untouched: `w_sym + w_alt = 2w_sym` is exactly what the tower's
unbounded ~2.5×/level growth feeds.

### Lean vs numeric, stated so nobody over-reads it

**Lean:** both j-values as rational identities, their non-integrality, and the
involution reindexing (stated abstractly, so it carries the argument without
formalising Young diagrams). **Numeric only:** that −3810.78125 is among the six
`Φ₅` roots; hook-multiset transpose invariance (standard, checked exhaustively
k≤9); `w_sym = w_alt` at 40 dps.

### Branch 3 is out of NAMED candidates

braid image **excluded** · arbitrary M **circular** · constant-residue holonomies
**fail the doubling identity** · every real-spectrum generator **on the wrong
side of 1** · `Im(q)` **cannot supply ellipticity** · Bring's E **non-CM** · τ₀
**non-CM** · jet tower **blind**. What remains is unnamed — and naming it is
research, not measurement.


## 🛑 Step 22 (2026-08-31) — Step 21 OVER-REACHED. `Δ_L` is ELLIPTIC.

**Owner correction, and it is right.** Step 21 concluded "no phase can hide in
the jet tower" from the fact that every tower quantity it examined is **real** at
real `q`. True, and beside the point: the ladder needs an elliptic **generator**
— a complex-conjugate *spectrum* — and **a real trace says nothing about a real
spectrum.** Step 21 ranged over traces and drew a conclusion about spectra.

Probe `qbeta-decay-operator-elliptic-spectrum` (6/6), Lean
`QOU/QBeta/TraceRealSpectrumComplex.lean` (sorry-free). Commit `1540977a43`.

### The owner's framing was the right one, and the corpus already had both pieces

> *"you're not really looking for the beta decay itself, but the thing that does
> beta decay"* — and *"you should be able to see the trefoil"*.

- The H₃ normal-form basis is `[γ, σ₀, σ₁, L₊, L₋, e⁻]` = `[1, T₀, T₁, T₀T₁,
  T₁T₀, T₀T₁T₀]`. **Its sixth element, named `e⁻` — the electron — IS the longest
  element, which IS the trefoil `σ₀σ₁σ₀`.** The electron was in the basis all along.
- `qbeta_hoefsmit_tbeta_matrix_build` already builds `T_β` **operator-valued** per
  Wedderburn block, on the stated ground that PR #1840 ruled out the scalar route
  because *"the `c_k` are irreducibly operator-valued"*.

### The finding — (2,1) block, proton pin

| operator | `tr²−4det` | `det(traceless)` | spectrum |
|---|---|---|---|
| `Δ_S` (short; **the ladder's closed forms**) | +0.043706 | −0.010927 | real — hyperbolic |
| `Δ_L = NF(n)−NF(p)` (long; **production runs on this**) | **−0.035837** | **+0.008959** | **ELLIPTIC** |

eigenvalues `−0.045681 ± 0.094653 i`, `|λ| = 0.105100`, `cos θ = −0.434649`,
**eigenphase θ = 2.020445 rad**.

**Step 18's exclusions never touched it**, for three reasons: it is a *difference*
of normal forms — an **algebra** element, not a braid-group element — so
`BraidImageEigenphaseExclusion` does not apply; it lives in the `(2,1)` block that
`χ^(2,1)(Δ_S) = 0` hides; and its **trace is real**, so a trace-level scan cannot
see it.

**The asymmetry is the point:** the model the ladder's closed forms come from is
hyperbolic; the model production runs on is elliptic. This bean already records
`Δ_S` vs `Δ_L` as a live fork with mixed pricing — they differ in **kind**.

### But it is the wrong phase

**θ = 2.020445 rad against the required 0.056595 — a factor 35.7.** `Δ_L`
supplies an elliptic generator, **not** the ladder phase.

### 🛑 Withdrawn / unaffected

- **WITHDRAWN:** Step 20/21's *"branch 3 is out of NAMED candidates"*. The corpus
  contains an elliptic generator; the arc missed it by looking at the wrong kind
  of object.
- **UNAFFECTED:** the vanishing Step 21 proved — a bar-odd operator has zero
  Plancherel trace, since `W_{λ'} = W_λ` and `χ^{λ'} = −χ^λ` — stands exactly as
  stated. Only the inference *trace-real ⟹ spectrum-real* is withdrawn.

### ⚠ Flagged coincidence, NOT pursued

`θ = 2.0204450` sits **0.012 %** from `|c₃(muon)| = 2.02020024` — at the
**superseded** CODATA-2018 anchor (Step 16). No mechanism connects a radian
eigenphase to a dimensionless Taylor coefficient, and this corpus has a
documented precedent for exactly this trap (stale `−2.00973976` vs
`J_Hopf − ℏ_q²` `−2.00981719`, agreeing to four decimals while being different
objects, which misled an earlier pass). Recorded per the standing owner ruling as
a target to check a derivation **against**, never a criterion to search **on**.
No search was run.

**Next, my judgement:** the live question is now whether `Δ_L`'s ellipticity is
*structural* or an artefact of the 11-crossing word choice — i.e. does every
long-model nucleon-difference land elliptic, or just this one? That is a
constrained, derivable question, unlike hunting for a phase.


## Step 23 (2026-08-31) — `Δ_L`'s ellipticity is STRUCTURAL: the nucleons are nearly parallel in sl₂

Probe `qbeta-nucleon-difference-ellipticity-structural` (6/6), Lean
`QOU/QBeta/TracelessDifferenceEllipticity.lean` (sorry-free). Commit `f1e6062e04`.

### The mechanism

For traceless 2×2 matrices,

    det(A₀ − B₀) = det A₀ + det B₀ + tr(A₀B₀)

(Lean `det_sub_traceless`, by `ring`; checked against the direct `det` to 1e-20).
Traceless real 2×2 is **hyperbolic** at `det < 0`, **elliptic** at `det > 0`, so
the difference of two hyperbolic directions is elliptic exactly when their
Killing pairing clears `−(det A₀ + det B₀)` — i.e. when they are **aligned**.

| | value |
|---|---|
| `det A₀` (proton) | −1.041656 — hyperbolic |
| `det B₀` (neutron) | −1.056560 — hyperbolic |
| `tr(A₀B₀)` | 2.107175 |
| **sum** | **+0.0089591 > 0 ⇒ ELLIPTIC** |
| exact-parallel threshold `2√(dA·dB)` | 2.098163 |
| **alignment excess** | **0.43 %** |

**The neutron and proton traceless parts are the same sl₂ direction to within
0.43 %.** That is the near-degeneracy of the nucleons (`m_n − m_p = 1.29` MeV out
of 939) — not a property of any word.

### Supporting, in decreasing weight

- **Robust in `q`:** discriminant negative at all 31 samples over `q ∈ [1.01,
  1.61]`, **zero** sign changes, smooth from −0.03376 to −0.04484. No fine-tuning
  at `q₀`. *(A first reading of the 0.43 % as a "thin margin" was wrong — the
  alignment margin is small, the discriminant margin is not, and the discriminant
  decides.)*
- **Random control:** NF vectors resampled at matched scale are elliptic **8.9 %**
  of the time (357/4000). The right null is this one, not the textbook
  `1 − 1/√2 = 29 %` for a generic real 2×2 — the NF→matrix map isn't that ensemble.
- **Word orderings:** 8 of 9 elliptic — **with its caveat**: the 9 collapse to only
  **3 distinct** (tr, det) pairs, 2 of them elliptic, so the raw 8/9 overstates it.
  Recorded because quoting 8/9 alone would mislead.

### Observation, not claimed

`det ρ(NF(p))` and `det ρ(NF(n))` agree to **1.4e-16** relative. Looks exact —
both words have 11 crossings — but it is **not proved** here and is used in no
argument above. Someone should settle it.

### What it does not settle

That `Δ_L` is the **right** generator. Its eigenphase stays 2.020445 against a
required 0.056595 — a factor 35.7 (Step 22). This explains why an elliptic
generator **exists**, and that its existence is a fact about the nucleons.
Nothing more.

**Next, my judgement:** the gap is now a single clean question — the required
phase is 0.0566 and the available one is 2.0204, a factor 35.7. Two things could
close it and both are checkable rather than speculative: whether `Δ_L`'s phase in
a **higher tower block** differs (Step 22 only measured `(2,1)` at `k = 3`), and
whether the ladder phase is a *fraction* of an eigenphase rather than an
eigenphase itself. Neither is a search over forms; both are readings of an
existing operator.


## Step 24 (2026-08-31) — both readings CLOSED; the gap is not bridged

Probe `qbeta-eigenphase-tower-and-fraction-readings` (5/5). Commit `be0d3f2`(see log).

### Check A — a higher tower block? **No, structurally.**

Across `k = 3,4,5,6` and every partition, the **only** distinct `|arg|` of a
complex eigenvalue of `ρ_λ(Δ_L)` anywhere in the tower is **2.02044502**, in
blocks of dimension 1–16, zero eig failures. Blocks without complex eigenvalues
are entirely real.

**The reason is standard rep theory** (cited, not proved): `Δ_L ∈ H₃` acts
block-diagonally on the H₃-isotypic decomposition of `λ↓H₃`, so
`spec ρ_λ(x) = ⋃_μ spec ρ_μ(x)` with multiplicity. **The tower repeats the H₃
spectrum and cannot add to it** — closing this reading for *every* H₃-induced
operator, not just `Δ_L`.

### Check B — a fraction of the eigenphase? **No, and not close.**

`θ_eig/θ_req = 35.700`, not an integer. Seven pre-declared candidates (list fixed
before computing; all reported, misses included; 11 and 22 because both nucleon
words are 11-crossing):

| | ratio | | ratio |
|---|---|---|---|
| `θ/2` | 17.850 | `2π−θ` | 75.320 |
| `θ/11` | 3.2455 | `π−θ` | 19.810 |
| **`θ/22`** | **1.6227** ← closest, still **62 % off** | `θ−2` | 0.36125 |
| `2θ` | 71.400 | | |

**And the non-numerological version settles it.** `θ_req` isn't intrinsic — it's
`(z−1)h/2 − u/2`, a *function of z*. So the real question is what `z` the
eigenphase corresponds to:

    +θ_eig → z =  20.3696          admissible z_D = 0.6127
    −θ_eig → z = −18.2881                     z_C = 0.4993

Off by ~33× and outside any admissible range both ways. The two phases aren't
related by a rational factor — they're different magnitudes in different ranges.

### Where this leaves it

`Δ_L` supplies a genuine elliptic generator whose ellipticity is a fact about the
nucleons — **but its phase is not the ladder's**, and neither tower level nor a
rational factor bridges the gap.

**What remains** is the single thing Step 22's correction opened and nothing since
has touched: **a genuinely level-`k` operator, not induced from H₃.** By Check A
that is the *only* place in the tower a different phase could come from.

*No new Lean here: the Check-A argument is textbook representation theory, and
manufacturing a proof file for it would overstate what this step established.*


## Step 25 (2026-08-31) — level-k avenue UNINSTANTIATED; real decays hyperbolic; Step 23 corrected

Probe `qbeta-level-k-operator-and-real-decays` (5/5).

### 1. The corpus never leaves H₃

`build_atom_nf` returns a **six-vector in the H₃ normal-form basis for every mass
number**, tritium (A=3) included. The atom words are laid out on `3A` strands but
the normal form is H₃-valued throughout. **So Step 24's one remaining avenue
exists logically but is NOT INSTANTIATED** — building a level-`k` operator is new
*construction*, not a reading, and belongs to the `T_β` Stage B branch queued
since PR #1840.

### 2. Real beta decays are hyperbolic

| decay | disc | kind |
|---|---|---|
| free n → p (Q=782 keV) | **−0.03584** | ELLIPTIC |
| n → protium (atomic) | +6.52244 | real |
| tritium → ³He (Q=18.6 keV) | +4.46143 | real |
| ¹⁴C → ¹⁴N (Q=156 keV) | +12.94889 | real |

Only the **bare nucleon pair** is elliptic. The alignment diagnostic says why —
for the nuclear cases parent and daughter are nowhere near parallel in sl₂ (sums
−1.63, −1.12, −3.24 against the nucleons' +0.00896). **Ellipticity is a property
of the near-degenerate n/p pair, not of beta decay.**

### 3. No species difference supplies the phase

All 105 pairs from 15 species: **21 elliptic**, eigenphases spanning **0.24950**
(he4−li6) to **2.96861** (he3−he4). The required **0.0565947 is below all
twenty-one** — the smallest available is **4.41×** too large.

### 🛑 Correction to Step 23, mine

Step 23 called the ellipticity "structural" on a random control of 8.9 %. That
control was against **random** vectors; against the corpus's **own** species it is
**21/105 = 20 %**. So ellipticity is *not rare*, and "structural" should not have
been read as "special".

What **stands, and is now independently confirmed**: the **mechanism**. `n−p` has
the **smallest |disc| of all 21** elliptic pairs — marginal ellipticity is exactly
what a 0.43 % alignment excess predicts. **Near-parallelism is the special thing;
ellipticity is its consequence.**

### Where the arc stands

Every named avenue closed or uninstantiated: braid image excluded · arbitrary M
circular · constant-residue holonomies fail the doubling identity · all
real-spectrum generators on the wrong side of 1 · `Im(q)` cannot supply
ellipticity · Bring's E and `τ₀` both non-CM · bar-odd operators have zero
Plancherel trace · the tower carries one eigenphase per H₃ element · no rational
factor bridges the gap · real nuclear decays hyperbolic · no species difference
small enough.

**What is left is not a reading but a construction the corpus does not have.**

---

## Step 26 — the discriminant curve in `q`: the tower is not elliptic, and the phase is excluded at `3·10¹¹ σ`

**Artifacts.**
[`qbeta_discriminant_curve_in_q_probe.py`](../computations/qbeta/qbeta_discriminant_curve_in_q_probe.py)
(8/8) ·
[`QOU/QBeta/DiscriminantCurveInQ.lean`](../folio/quantum-observable-universe/lean/QOU/QBeta/DiscriminantCurveInQ.lean)
(15 theorems, sorry-free) ·
[audit](../docs/audits/2026-08-31-qbeta-discriminant-curve-in-q.md).

### 🛑 A method error running through Steps 21–25, mine

Every one of those steps evaluated its spectra at the **single point** `q = q₀`.
That cannot distinguish a discriminant that is a perfect square from one that is
an irreducible degree-18 polynomial, so **nothing in Steps 21–25 could have
settled a question about the tower** — and each of them asserted tower-level
conclusions anyway. "Collapsing to order zero" is the right description.

### 🛑 And a factual claim, also mine

Step 25 said `Δ_L` "cannot be asked this question" because `build_nucleon_nf`
takes no `q`. **Wrong.** `hecke_core_symbolic.hm_sym` is the symbolic-`q` twin of
`hm`; mirroring `build_nucleon_nf`'s 11-crossing braid-order word through it
gives the nucleon NF as an exact element of `ℚ(q)`, matching the canonical
numeric builder to `9·10⁻¹⁷` in all twelve coordinates. There was no gap.

⚠️ `shift_from_nf_basis.build_nucleon_nf_sym_atomic` is **not** that mirror: it
matches the crossing counts and the 7/4 split but applies the **monotone**
re-sort of `B₃` where the canonical builder alternates — an **82 %** difference on
`tr_M` by `nucleon_braid_word`'s own measurement, visible as `L₊ = e⁻ = 0`.

### 1. No twisting exists to be missed

`tr(1/q) = −tr(q)` · `det(1/q) = det(q)` · `disc(1/q) = disc(q)`, as **exact
identities in `ℚ(q)`**. The bar involution acts trivially, so `disc` is a
polynomial in `x = q + 1/q`. Consequence on the unit circle: `tr` is purely
imaginary and `det` real (checked to 40 digits), so every root of unity carries a
real discriminant.

### 2. The curves: genus 0 and genus 8, never genus 1

| model | `disc(x)` | curve |
|---|---|---|
| short `Δ_S` | `x² − 4` (`= h²`, a perfect square in `q`) | conic, **genus 0** |
| long `Δ_L` | `(x−2)(x+2)G₋G₊/16`, deg 18, squarefree | hyperelliptic, **genus 8** (genus 4 on `w = x²`) |

`G∓(x) = 2x⁸ − 21x⁶ + 77x⁴ − 115x² ∓ 2x + 58`. **Neither is genus 1** — no
elliptic curve, hence no tower of them.

**New, and only visible symbolically:** `x = q + 1/q ≥ 2` for every real `q > 0`,
so `disc_S ≥ 0` **identically**. The short model is hyperbolic at *every* real
`q`, not merely at `q₀`. Closed for good.

### 3. The Hecke tower adds no eigenvalue

Branching: `Res S^λ = ⊕ S^μ`. Verified on all five `H₄` shapes at three `q`.
Every corpus object is `H₃`-valued (Step 25), so no new discriminant at any level.

### 4. The classical limit is exactly `2π/3`, and the trefoil is second-order

Every NF coordinate of `Δ_L` carries `(q−1)(q+1)`, so `Δ_L → 0` at `q = 1`.
Orders: `γ:1 σ₀:2 σ₁:2 L₊:3 L₋:1 e⁻:2` → leading direction `−(1 + T₁T₀)`, and
`T₁T₀` is the `S₃` 3-cycle: eigenvalues the primitive cube roots of unity,
`tr = −1`, `det = 1`, `disc = −3`, eigenphase **exactly `2π/3`**.

**The electron word `e⁻ = T₀T₁T₀` enters only at second order.** The thing that
does the decay is `1 + L₋` first; the trefoil is its correction.

### 5. The window, and the closure by measurement

`Δ_L` is elliptic **exactly for `q ∈ (1, 1.379732661603278)`**; `q₀` sits 29.0 %
up. `θ(q₀) = 2.02044502` — reproducing Step 22's `2.0204` from an independent
construction. `θ` sweeps to 0 at the wall, so the required phase **is** attained:

| conv | `θ_req @ q₀` | `q*` | `(q*−q₀)/σ_q₀` | dist. to wall |
|---|---|---|---|---|
| `z_C` | `0.0565947` | `1.37812464914` | **`2.91·10¹¹`** | `0.0016` |
| `z_D` | `0.0447444` | `1.37956231361` | **`2.93·10¹¹`** | `0.00017` |

Both hard against the degeneracy wall: **the phase is only small where `Δ_L` is
about to stop being elliptic.** Excluded by the CODATA proton pin
(`σ_q₀ = 9.2116·10⁻¹³`) at three hundred billion σ. Curve derived first, crossing
located after — a falsification test, not a search. `q*` is a fact **about the
curve**, never a candidate `q`.

### 6. The cyclotomic tower `q = ζ_N` is real, and also too big

`φ₃ = φ₆ = 2π/3` exactly (`disc = 9/16`), `φ₈ = π`, `N=4` singular, `N=5`
degenerate, `φ_N → 2π/3`. Minimum over every non-degenerate `N ≤ 120`:
**`φ₇ = 1.4042`** — still **24.8×** the required phase.

### Where the arc stands after Step 26

The short model is closed **for all `q`**. The long model's phase is excluded
**by the calibration**, not by inspection. Neither tower — Hecke or cyclotomic —
carries an elliptic curve or a small enough phase. What remains is unchanged from
Step 25: not a reading, but a construction the corpus does not have.

---

## Step 27 — the level-`k` operator IS binding, and the trace is blind to 588 of the 720 dimensions it lives in

**Artifacts.**
[`qbeta_level_k_binding_operator_probe.py`](../computations/qbeta/qbeta_level_k_binding_operator_probe.py)
(8/8) ·
[`QOU/QBeta/TraceBlindSector.lean`](../folio/quantum-observable-universe/lean/QOU/QBeta/TraceBlindSector.lean)
(8 theorems, sorry-free) ·
[audit](../docs/audits/2026-09-01-qbeta-level-k-binding-operator.md).

### 🛑 Correction to Step 25, mine

Step 25 said "the corpus is H₃-valued at every `A`, so the level-`k` avenue is not
instantiated", from `build_atom_nf` returning a 6-vector at every `A`. **That reads
the evidence backwards**, and `qou-tower` had already named the cause:
`build_atom_nf_mp` applies the H₃ Gröbner–Shirshov reduction **after every
crossing**. A 6-vector at every `A` is not evidence the atom *lives* in H₃ — it is
evidence H₃ is where the chain can **observe** it. `atom_braid_word_3A` is the
faithful object and its `include_inter` switch is composite-vs-constituents.

### 1. The construction — binding, done on the operators

`Δ_bind = β_atom − β_free ∈ H_{3A}(q)`. `tr_M` is linear, so `tr_M(Δ_bind)` is the
binding number the corpus already computes — but `Δ_bind` is an **operator**, and
an operator has a spectrum no linear functional determines.

Deuteron (`3A = 6`), exact in all 11 blocks:
`β_atom = P·I·N`, `β_free = P·N` ⟹ **`Δ_bind = P·(I−1)·N`**.
`β_free` uses only gens `{0,1,3,4}` and IS `H₃ ⊗ H₃`; `I−1 = σ₂ + (d−1)·1` is not.
**So `Δ_bind` is genuinely `H₆`-valued and Step 24's branching argument does not
reach it.** Validated against the corpus's `chi_lambda_of_word` to `5.4e-15`.

### 2. THE FINDING — the blind spot is structural, not accidental

Convention D is the SU(2)/Temperley–Lieb trace, so `ω_λ = 0` on every partition
with **> 2 rows** — measured `< 2e-16` on seven of eleven, and confirmed by
arithmetic: `Σd² = 720 = 6!` total, `132 = C₆ = dim TL₆` visible.

> **588 of 720 dimensions (81.7 %) are invisible**, and the binding character is
> **largest in an invisible block**: `χ_(3,2,1) = −9.598` vs `+0.009` in the
> visible 1-dim block.

### 3. The blind sector holds the first small phases in the arc

| λ | dim | vis | eigenphase |
|---|---|---|---|
| `(3,2,1)` | 16 | **no** | `0.0252506` |
| `(2,2,1,1)` | 9 | **no** | `0.0195531` |

Required: `0.0447444`. Every prior candidate was **above** it (Step 25: `4.41×`;
Step 26 cyclotomic: `24.8×`). **These are the first below.**

### 4. 🎯 TARGET, NOT A RESULT — the 0.13 % sum

`0.0252506 + 0.0195531 = 0.0448038` vs required `0.0447444`. **Wall artefact:**
`θ₂ → 0` at the `(2,2,1,1)` wall `q_w = 1.1121238`, so the sum sweeps down through
everything and a crossing is guaranteed. It is at `q* = 1.109988469` =
**`1.07e7 σ_q₀`**. `q*` is `0.19200 %` below the wall, `q₀` is `0.19289 %` — both
hard against the **same** degeneracy, exactly Step 26 §5's structure. And "sum of
two block eigenphases" has **no derivation**. Recorded to check a future
derivation AGAINST; never a criterion.

### 5. How far it reaches — blindness deepens super-exponentially

Visible share is `C_n/n!`, `n = 3A`: **83.3 %** (A=1) → **18.3 %** (A=2) →
**1.34 %** (A=3) → **7.5e-6 %** (A=6).

### 6. ⚠️ The corpus's word is a nearest-neighbour CHAIN, not all pairs

`ordering = ['p']*Z + ['n']*N`, interface at `gen 3k+2` for `k < A−1`: `A−1`
couplings where all pairs would be `A(A−1)/2`. Deficit `(A−1)(A−2)/2` — **zero at
A=2**, so §1–§4 are exact for the deuteron. From A=3 it bites: permuting the
arbitrary ordering (`ppn`/`pnp`/`npp`) moves the binding character by **22.54 %**,
and all-pairs coupling would show none by symmetry. **A first-order modelling
choice at A≥3 that every heavy-nucleus number inherits.**

**NOT proposed here:** an all-pairs word with distance decay. A decay rate per
bond type is three free parameters with no derivation, and a non-adjacent nucleon
pair has **no single generator to sit on** (`σ_g` couples `g`,`g+1` only), so the
coupling is a modelling choice, not a letter to insert.

### Where the arc stands after Step 27

The level-`k` operator exists, is validated, and is **binding**. The observable is
blind to 81.7 % of it at A=2 and 98.7 % at A=3, structurally. The only small
eigenphases in the corpus are in that blind sector. Two open items, in order:
**(a)** the all-pairs coupling word for A≥3 — a construction, needing an owner
call on the decay convention; **(b)** whether anything derives a *combination* of
block eigenphases, which is what the 0.13 % target would need before it could be
anything but a coincidence.

---

## Step 28 — the all-pairs decay rates are DERIVED: transfer-matrix spectrum, sector-indexed, one degree of freedom

**Artifacts.**
[`qbeta_bond_decay_rates_from_transfer_spectrum_probe.py`](../computations/qbeta/qbeta_bond_decay_rates_from_transfer_spectrum_probe.py)
(5/5) ·
[`QOU/QBeta/BondDecayRates.lean`](../folio/quantum-observable-universe/lean/QOU/QBeta/BondDecayRates.lean)
(sorry-free) ·
[audit](../docs/audits/2026-09-01-qbeta-bond-decay-rates-from-transfer-spectrum.md).

Unblocks Step 27's stopping point. Owner steer: *"go back to looking at how we
define CAL 123 ideal math — there are decay rates right there… link these to the
spectral decomposition of the transfer matrices operating on the tower."* Both
halves hold.

### 1. Where the rates were

The math-ideal CAL triple is **`(m_e, 𝔇_β, 𝔇_π)`**, not three masses: CAL-2 is the
**neutron β-decay width** at `h²`, CAL-3 the **pion decay width** at `h³` (owner
ruling 2026-06-26). `m_μ/m_e` and `m_π` are only the observational proxies. **Two
of the three calibration points are decay rates by definition.**

### 2. The transfer matrix's spectrum IS the bond rate

`chi_monotone_transfer._alpha_beta` reduces each fine-Bratteli step to
`O_g = α·σ_g + β·I` with `E₁ = ∏(q + d_j)`, `E₂ = ∏(−1/q + d_j)`. Those ARE the
step's spectrum, so the falloff across one bond is `E₂/E₁`:

| bond | `d` | `E₂/E₁` |
|---|---|---|
| p–p `σ` | `0` | **`−1/q²`** |
| n–n `σ⁻¹` | `−h` | **`−q²`** |
| p–n avg | `−h/2` | **`−1` exactly** |
| p–n colour | `−h(½−δ/4)` | `−1 + tanh(ln q)·δ + O(δ²)` |

Closed forms in `q`. **No free parameter** — the rate Step 27 declined to invent
was already fixed by the transfer matrix.

### 3. ⚠️ They are NOT independent (owner's steer, confirmed)

`r_pp · r_nn = 1 = r_pn²` and `r_nn/r_pp = q⁴`. **One relation → one degree of
freedom (`q²`), not three.** An all-pairs coupling on these adds NO parameter.

### 4. And they ARE sector-indexed, by bar parity

| | under `q ↦ 1/q` | sector |
|---|---|---|
| `r_pp ↔ r_nn` | **exchange** | a bar-conjugate pair |
| `r_pp·r_nn = 1` | bar-**even** (cosh) | **strong** |
| `r_nn/r_pp = q⁴` | bar-**odd** (sinh) | **weak** |
| `r_pn = −1` | bar-**fixed** | **electromagnetic** |

The last row is the sharp one. `1 − |r_pn| = tanh(ln q)·δ + O(δ²)`, and
`tanh(ln q₀) = 0.103963710` is **exactly** the odd-to-even ratio
`interaction-sector-taxonomy.md` derives for the **EM coupling** by a wholly
separate argument (bar decomposition of `α_EM⁻¹ = q[9]_q[10]_q`). Predicted
`1.4302400e-4` vs measured `1.4301377e-4` — `7.2e-5` relative, the second order
in `δ`. The p–n bond sits at the intertwiner point, where the taxonomy
independently puts EM.

### 5. h-orders match the CAL ladder

`r_pp, r_nn` are `O(h⁰)`; `tanh(ln q)` is `O(h)` (measured `0.9999980`); **`δ` is
`O(h³)` (measured `2.9999902`) — CAL-3's order, the pion decay width's**; so
`1 − |r_pn|` is `O(h⁴)`.

### What is still open

The **coupling word**, not the rate. `σ_g` couples strands `g`, `g+1` only, so a
non-adjacent nucleon pair has no generator to sit on and the all-pairs braid
remains a construction. Step 27's caveat stands; only the three-free-parameter
objection is removed.

---

## 🛑 Step 28 CORRECTED, and duplicated — `main` had it right (2026-09-01)

Integrated `main` (271 commits, then 3 more mid-session) and it landed
**`qou-brng`**: *"the decay rate per bond type IS the transfer matrix spectral
gap — pp/nn exactly 1/q^2, pn long-range"*, with
`computations/probes/spectral_gap_bond_decay_probe.py`.

**Same object as Step 28, derived independently, and correctly.** Step 28 read
the rate as `E₂/E₁` in the **fixed** `(q, −1/q)` order; the correlation decay is
`|λ₂/λ₁|` with `λ₁` the **larger-magnitude** eigenvalue. `σ⁻¹` carries `σ`'s
spectrum up to sign, so:

| bond | Step 28 as published | correct |
|---|---|---|
| p–p | `−1/q²` | `1/q²` |
| **n–n** | **`−q²`** | **`1/q²`** |
| p–n | `−1` | `1` — **long-range** |

**Withdrawn, not restated:**
- `r_pp · r_nn = 1 = r_pn²` → the product is `1/q⁴`. No "one degree of freedom".
- bar exchange → strong/weak sector split. Equal rates do not exchange; and the
  claim was partly circular anyway, since `d = 0` and `d = −h` *are* `σ` and
  `σ⁻¹`, bar-images by definition.

**Surviving:** the rates are derived closed forms with no free parameter (Step
27's three-free-parameter objection is still removed); **p–n is long-range while
both like-nucleon bonds are short-range**; and the colour-weighted p–n departure
is `tanh(ln q)·δ`, `tanh(ln q₀) = 0.103963710` matching the taxonomy's EM ratio
to `7.2e-5` — with a self-raised triviality caveat in `qou-i9gk`.

**And the recommended next was already done.** `qou-brng` also carries
`allpairs_distance_decay_probe.py`, which tests the owner's all-pairs proposal
directly and returns a **negative**: the strand-routing cost is exactly `z²` per
unit separation but cannot be the binding's distance decay (read as interaction
it makes distant pairs bind *more*; read as kinematics it divides out), and the
decay AME wants is not constant and not fast — `r*` runs `0.709..0.827`, falling
monotonically with `A`.

So this session's recommended next was duplicated work twice over. Roast and the
two surviving self-checks: **`qou-i9gk`**.

---

## 🛑 Step 27's headline reading is CORRECTED — the blind sector is the TL kernel (2026-09-01)

`qou-i9gk` hole 1, settled.
[`qbeta_blind_sector_is_the_tl_kernel_probe.py`](../computations/qbeta/qbeta_blind_sector_is_the_tl_kernel_probe.py)
(4/4).

**Step 27 said** the `>2`-row blocks carry *"information the observable cannot
see"* — 588 of 720 dimensions. **They carry no states at `N = 2`.**

Measured at `n = 3..8`, not just Step 27's `n = 6`: `ω_λ = 0 ⟺ ℓ(λ) > 2` exactly,
with a clean gap (`~1e-16` against `0.039..0.49`), and `∑d²` over the `≤2`-row
blocks equals `Catalan(n)` at every `n` — `5, 14, 42, 132, 429, 1430`. So those
blocks **are** `TL_n` and the rest span the **kernel** of `H_n(q) → TL_n(q)`.
`TL_n = End_{U_q(sl₂)}(V^{⊗n})`, so that kernel is exactly the part of the
algebra acting as **zero** on the `N = 2` physical space. It is the Schur–Weyl
row cap (`qou-fvzm`), structurally — not a second, independent vanishing.

### The reading contradicts the convention it was measured in

`FibreCategoricalTraceForcesJones.lean` (bean `qou-n1dj`) already has the chain:
`ℓ > 2` channels absent at `N = 2` (**proved**) → **open premise**, that the mass
trace *is* the categorical trace of the fibre action on `V^{⊗n}` → `y_{(1³)} = 0`
forces **Jones** (**proved**).

**Convention D is forced by the premise that empties the blind sector.** Step 27
computed in D and read D's zeros as hidden information. Under the premise giving
D there are no states there; under its negation D is not forced and D's weights
are the wrong ones.

**And the premise is NOT open.** `qou-n1dj` is **resolved** — its status is
`todo` only because closing a bean is a human action (AGENTS.md §4a), and
`qou-cds1` itself already recorded this at line 4285. Verified here:
`lem:feynman-eigenbasis-decomposition` **defines** the mass channel as
`V^{⊗n} ≅ ⊕_{λ ⊢ n, ℓ(λ) ≤ 2} V_λ ⊗ S_λ` — the row cap is **in the index set** —
and `FibreDimensionForcesTL.lean` (sorry-free) proves `z·[N]_q = q^N`, so a
two-dimensional fibre leaves **no residual trace freedom**.
`MassTraceIsFibreCategorical` is a Lean *class* only because no quantum
Schur–Weyl development exists in this tree; its content is already asserted by
the mass chapter. **So the blind sector is unphysical FULL STOP, and Step 27's
headline is false rather than conditional.**

### The 0.13 % coincidence dies structurally

`N_min(λ) = ℓ(λ)`. Physical at `N=2`: `(6), (5,1), (4,2), (3,3)`. `N=3` adds
`(4,1,1), (3,2,1), (2,2,2)`. `N=4` adds `(3,1,1,1), (2,2,1,1)`.

- `0.0252506` in `(3,2,1)`, `ℓ=3` → needs **`N ≥ 3`**
- `0.0195531` in `(2,2,1,1)`, `ℓ=4` → needs **`N ≥ 4`**
- **the sum therefore requires `N ≥ 4`** — nothing in the corpus motivates it.

Cleaner than Step 27's degeneracy-wall argument, and structural.

### What survives

`qou-fvzm`: the super-pairwise binding term **requires `N ≥ 3`**. `(3,2,1)` — the
block with the largest binding character (`−9.598`) and the smaller phase — is an
`ℓ = 3` block. So Step 27 measured **what an `N = 3` extension would carry**.
Weaker and different from its claim, and the part that stands. The construction
`Δ_bind = P·(I−1)·N`, its validation, and the chain-vs-all-pairs finding are
untouched.

---

## 🛑 Step 28's last positive is DOWNGRADED — the tanh/EM match is formal (2026-09-01)

`qou-i9gk` residual, settled and the bean completed.
[`qbeta_tanh_em_match_is_formal_probe.py`](../computations/qbeta/qbeta_tanh_em_match_is_formal_probe.py)
(4/4).

A census finds **5 of 12** unrelated corpus `q`-quantities have odd-to-even ratio
exactly `tanh(ln q)`, and **`q` alone is one of them** — quantum integers are
bar-even, so `[9]_q[10]_q` divides out of the taxonomy's coupling and contributes
**nothing** to the matched number. `X = q·B` with `B` bar-even gives it for any
`B`. And `tanh(ln q)` **is** `h/(q+1/q)`, exactly how it arises in the p–n
departure. Discriminator: the taxonomy's **dressed** ratio is `0.10356`, `54×`
the residual away, and the match lands on the **bare** value.

**Kept:** the closed form `1 − |r_pn| = tanh(ln q)·δ + O(δ²)`, `δ` at CAL-3's `h³`.
**Withdrawn:** the electromagnetic link.

### Where Steps 26–28 stand, after three self-checks

Step 26 stands in full (the discriminant curves, the exact `2π/3` classical
limit, the `3·10¹¹ σ` exclusion). Step 27 keeps its construction and its
chain-vs-all-pairs finding, and loses its headline. Step 28 keeps only derived
closed-form bond rates, which `qou-brng` had first and correctly.

**The real blocker is unchanged and upstream of all of it:** `α` is axiomatised
(`q-beta-cos-resummation.ts:48`), the two-row cap admits exactly `{q, z_D}` and
both fail (PR #6264), so the functional form must change. `qou-pdix`. And
`qou-n1dj` now sits upstream of *that*, since which convention is forced depends
on the same fibre-categorical premise.


---

## Entry 17 — the terminus, recomputed from an independent route, as a PROBE not a summary (2026-08-31)

`computations/qbeta/qbeta_cds1_terminus_status_probe.py` — **13/13**, sympy
exact, **runs standalone with `PYTHONPATH` stripped**.

### Why

This bean is ~4760 lines over 16 entries and 14 steps and carries **four
withdrawals** — Step 10's "the block is a ruling" (Step 13), entry 13 (entry
14), a Step-13 correction that did not propagate (Step 14b), and entry 12's
framing of the `K` blocker (entry 16). A reader arriving cold cannot tell what
stands, and this arc's own history is of recorded figures going stale. So the
consolidation is a probe that RECOMPUTES, not a document that transcribes: if an
anchor moves or a producer changes, it fails rather than quietly disagreeing.

### Verified here, from a THIRD independent 3×3 Markov solve

    y_(3)(z_D)   = (q^4+1)/(q^2+1)^2        symbolic difference exactly 0
    y_(1^3)(z_D) = 0                         the cap at z_D
    y_(3)(q)     = 1                         exactly, at the augmentation root
    y_(1^3)(q)   = 0
    admissible set = EXACTLY {q, z_D}        qou-06wh re-derived from the roots
    chi^(2,1)(Delta) = 0  identically        Step 9
    g(q0)        = 0.505404226504
    shortfall    = x1.75923699055            a DOF that does not exist
    z_required   = 0.998500302563            re-solved, and EXCLUDED by the cap
    entry 15's two bar conditions            both reproduced

So the terminus is **not a computational artefact**: three routes (this solve,
the sibling's, and Lean `wtNumer`) agree on the weights.

### A rounding that looked like a disagreement — recorded because it nearly wasn't

My first run FAILED `z_required`, returning `0.998500302519` against the
recorded `0.998500302563`. That is not a discrepancy: I had hardcoded
`g_required = 0.8891258104` from this bean's prose, which is the **10-sig-fig
rounding** of the witness's `0.88912581044405784613`, and that rounding alone
moves the root by ~4.4e-11. Fixed by reading the witness, **not** by widening
the tolerance. Two lessons, both already this repo's: a quoted figure is a
lossy copy of its witness, and the fix for a red goes at the input.

### Not verified here, and the probe says so

Step 14's `chi` leg quotes a required element ratio `1.5516573513` for a
HYPOTHETICAL decay element whose definition this probe cannot rebuild without
guessing; Step 14's `K` is an enumeration, not a closed form; and the derived
cap is a Lean result (`FibreDimensionForcesTL.lean`) to be checked with
`lean`-direct. All three are recorded as `verified_here: false` with the reason.

### Where the arc stands

**Open:** a derivation of `alpha`. The z direction is closed from three
independent sides (trace weight, bar parity, anchors); the cos form is closed
(Steps 7-8, entry 15); the amplitude route is fenced (`qou-i2ir`: C16/C17/C18
plus a structural one-scale/two-target refutation). **No route is known to be
open** — stated as a fact about the search, not as an impossibility claim.
Scope (a). L2 unchanged at 1279 ppb.

### 🛑 Correction to entry 15's cross-reference — I repeated an inflated reading (2026-08-31)

The cross-reference section I added when merging main says the counit entry
closes the z direction partly because *"`z_required` forces a **negative**
Wedderburn weight"*. **That phrasing over-states what the negative shows**, and
PR #6361 is right to deflate it. Verified independently here before accepting it:

    wtNumer(q,z) = (z − q)((q²+1)z − q³)

is an **upward parabola in `z`** (leading coefficient `q²+1 > 0`) whose two real
roots are *exactly* the two admissible Markov parameters, and
`q − z_D = q/(q²+1) > 0` **identically**, so `z_D < q` for every `q > 0`.
Therefore `y_(1³)(z) < 0` for **every** `z` in the open interval `(z_D, q)` —
width **0.49729055** at the pin, about half the substrate parameter itself.

    z_C   0.4993203342   wtNumer  +0.15452259   outside (left of both roots)
    z_D   0.6126880371   wtNumer   0            ROOT
    z*    0.9985003026   wtNumer  −0.095999879  inside
    z=1   1.0            wtNumer  −0.095076553  inside
    z=q   1.1099785827   wtNumer   0            ROOT

So the negative at `z*` and the negative at `z = 1` are **one fact**, and it is
`z ∈ (z_D, q)` — **not** a property of either point. My cross-reference presented
it as a finding *about* `z_required`, which is the stronger-sounding and weaker
claim. The z direction is still closed from three sides; that conclusion is
unaffected. Only the weight of this particular piece of evidence shrinks.

Recorded rather than silently edited because it is the same shape as the errors
this bean already collects: a quantity that is true at a point, reported as
though the point were what made it true.

### Entry-numbering collision with PR #6342 — flagged, not unilaterally renumbered

PR #6342 (open, `claude/convention-migration-validation-77exfa`) appends **its
own** "Entry 15" and "Entry 16" to this bean, for different content — a pinning
/ non-D sweep, and the `c_k^even` exact rungs against entry 9's `|c_4|`. Mine
(block bar-defect; K two-anchor filter) landed first, in `7a11282fe58`.

Whoever merges second should renumber rather than union into two Entry 15s and
two Entry 16s. Flagged on #6342; **not** renumbered here unilaterally, since
that branch is a sibling's live claim.

## 🛑 Third correction (2026-09-01) — the `N = 3` reading is withdrawn too

**🛑 THIRD CORRECTION, same day — the last positive goes too.** The reading
*"(3,2,1) is an ℓ = 3 block carrying the largest binding character, so this
measures what an `N = 3` extension would carry"* cited **`qou-fvzm`'s REOPENED
paragraph**. That bean is **`status: completed`**, and its line 18 closes
exactly that paragraph: *"my reopened form … is closed — the route is
**UNAVAILABLE**, not merely hard"*, and *"**THE MISSING ADDITIVE TERM IS NOT A
HECKE-TRACE OBJECT AT ALL**."* Moving to `N = 3` re-weights channels the mass
pipeline already evaluates (`y_(2,1)/y_(3) = q[2]_q[N−1]_q/[N+2]_q` differs at
every `q`), so it is a **regression risk, not an opening**. The surviving
candidates that bean names are the ones that were never trace objects — the
extended-Bloch route (`qou-985x`) and the atomic-braid→nucleus map (`qou-imcd`).
>
**So Steps 27–28 retain no positive claim about the blind sector at all.** What
stands from that arc is the construction `Δ_bind = P·(I−1)·N` (validated to
`5.4·10⁻¹⁵`, genuinely `H₆`-valued) and the chain-vs-all-pairs structural
finding.

Found by a dispatched audit of the Standard-Model work against the full tower;
verified against `qou-fvzm` directly rather than taken on the agent's word.

## 2026-09-04 — the open bar-parity question is ANSWERED (PR #6605)

This bean named as its own cheapest next step: *is `F` required to be
bar-even?* Answered symbolically — **it is not required, and it is not
satisfiable.**

With `Q_A = m_e·|q²−2q−1|(q+1)/(2q³)` and `bar : q ↦ 1/q`:

    bar(Q_A)/Q_A = −q³·(q² + 2q − 1)/(q² − 2q − 1)

- `+1` only at `q = 1`, where `bar` is the identity and the test is vacuous;
- `−1` at no positive real `q`;
- **not bar-definite even up to a power of `q`** — stripping `−q³` leaves
  `(q²+2q−1)/(q²−2q−1)`, a ratio of two distinct irreducible quadratics
  (roots `−1+√2`, `1+√2`), not a monomial.

The third test is the operative one, because *"bar-definite up to a power of
`q`"* is this bean's own working notion: it records `bar(z_D) = q⁻⁴·z_D`.
`z_D` is covariant in that weaker sense; `Q_A` is not covariant in it at all.

`Q_β^exp` is bar-even trivially, so `F` inherits `Q_A`'s non-parity.

**Consequence for this bean's plan: the `u/2` term does NOT need replacing on
bar-parity grounds.** The "if it is required" branch is closed — there is no
constraint for a 15 % term to violate, so the projection is not shown
incomplete by this route. A case for replacing that term must come from
elsewhere. Scope (a): about this closed form, not about the weak sector.

Probe `computations/qbeta/qbeta_f_bar_parity_requirement_probe.py` (5/5,
sympy end to end, no floats / no anchor); audit
`docs/audits/2026-09-04-qbeta-f-bar-parity-requirement.md`.

### Flagged, NOT resolved — for the owner

Four corpus sites call this same object bar-odd (`AGENTS.md:1937`,
`epistemic-status-of-calibrations.md:3`,
`three-calibration-discipline-proof.md:36`, and the strongest,
`interaction-sector-taxonomy.md:20` — "pure odd"). The Lean cited for the
split, `mass-theory/bar-parity-split.lean`, proves only the GENERIC
decomposition of an arbitrary `x` under an arbitrary involution; the
identification of `Q_β` with the odd part lives in its docstring, not in a
theorem. Two readings survive — the claim is about the channel (then scope the
prose), or about the observable (then it is refuted). Physics call; recorded,
not decided, and explicitly NOT a claim that the corpus is inconsistent.

Symbol collision also flagged: that docstring's `F` (abstract Habiro element)
and this bean's `F = Q_β^exp/Q_A` (numerical correction factor) are two
objects sharing a glyph in one channel.


## Backlog for the re-derivation — two STALE-GREEN witnesses (from #6606, `qou-zk51`)

A sibling flagged these on #6605 and I verified the committed half myself
(`git show origin/main:<witness>`): both carry the convention-C signature —
half-integer powers `sqrt(q)`, `q**(15/2)`, `q**(13/2)` — while recording
`allPassed: true`.

- `computations/qbeta/qbeta-symbolic-tbeta-min-l2.witness.json`
  (`A_q_symbolic`: `sqrt(q)`-form → `q**3/(q**2 + 1)` under D)
- `computations/qbeta/qbeta-markov-trace-norm-probe.witness.json`
  (same symbolic swap; L2 residue `6.85e-14` → `3.48e-9`)

I confirmed the C-form and the committed green. I did **not** re-run the
producers, so the sibling's "a fresh run returns `false`" half is
unverified here — take it as reported, not as measured by me.

**Neither producer is broken.** A C-frame assertion failing under D is exactly
what `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` predicts. They must not be
refreshed in place — that would commit a red. They are inputs to this bean's
re-derivation, and they land green again only when the ladder itself is
re-derived under D.


## 2026-09-04 — the phase term has NO derivation to re-derive (PR #6625)

Follow-on from the bar-parity result. With parity ruled out as a constraint,
the next lever was the eigenphase `α = (z−1)h/2`. Asked the prior question the
two-row filter arc never asked: **what derives the form?**

The corpus answers with one citation —
`q-beta-categorical-precision-ladder.md`: *"α = (z−1)h/2 is the single-wrap
eigenphase on V_(2,1) (per `prop:q-beta-spectral-bridge`)"*. Read it.

- **It names no eigenphase.** Across that proposition's `.md`, `.lean` and
  proof block, the strings `eigenphase`, `V_{(2,1)}`, `V_{2,1}`, `(2,1)` and
  even `phase` occur **zero** times.
- **What it produces is a ratio coefficient.**
  `Q_A/Q_B = (1−h/2)/(1−zh/2) = 1 + (z−1)h/2 + O(h²)` — so `(z−1)h/2` is the
  first-order term of a multiplicative ratio (remainder exactly
  `z(z−1)h²/4/(1−zh/2)`, the source's own Lean `bridge_first_order_remainder`).
  The ladder uses it as an **angle**.
- **Measured, the roles are far apart.** `cos(α−u/2)` vs the source's own
  `1+α`: **5.354 %** (C) / **4.115 %** (D) at the proton pin. And the `δ`
  solving `cos(α−δ) = 1+α` is **−0.377** (C) / **−0.326** (D) against the
  ladder's `u/2 = 0.004259` — off by **88.6× / 76.6×** and opposite in sign.
  That closes the charitable "cited only for the value" reading.
- Also: the proposition is **conditional on the Borromean quark conjecture**;
  its two proved Lean theorems are free-variable `ring`/`field_simp`
  identities saying nothing about any convention; its analytic step is open.

**CONSEQUENCE FOR THIS BEAN. "Re-derive under D" cannot mean "recompute α at
`z_D`."** The provenance fails in BOTH conventions — there is no C-frame phase
awaiting a D-frame twin. **The D work must SUPPLY a phase, not convert one.**
It also explains the two-row filter's empty result rather than leaving it a
brute fact: it searched for a `z` inside a form with no derivation behind it.

NOT a new declaration — the arc's standing position (2026-08-31 audit, §Scope)
is already that α is not derived. This records the **mechanism**, which was
not: the cited source derives a different object.

**Incidental, flagged not fixed:** `markovZ` in `q-beta-spectral-bridge.lean`
has body `q³/(q²+1)` (D, migrated 2026-08-26, `2af189af1a`, `qou-cxjq`) while
its own docstring and the `.md` proposition define z as C. Changes no proved
theorem (both quantify over free `z`), but the load-bearing definition
disagrees with itself. Which way to reconcile it depends on the re-derivation.

Probe `computations/qbeta/qbeta_ladder_alpha_provenance_probe.py` (5/5, mpmath
50 dps + sympy, no float64); audit
`docs/audits/2026-09-04-cds1-ladder-phase-has-no-derivation.md`. Scope (a).


### Correction to the entry above — the route it points at is CLOSED

The entry above ends "the D work must SUPPLY a phase, not convert one" and I
recommended supplying a Hoefsmit/seminormal eigenphase on `V_(2,1)`, on the
grounds that the machinery is already there. **That route is excluded**,
scope-(b), invariant named — by this bean's own child `qou-pdix`. Found by
corpus-grep after the fact; recorded so nobody re-derives it.

- `qbeta_eigenphase_seminormal_exclusion_probe.py` — every character of
  `V_(2,1)` lies in `ℤ[q,q⁻¹]` (`b` enters traces only through the rational
  `b·c`; every word of length 2, 4, 6 — 17 traces, 0 exceptions), while
  `2cos((z−1)h/2)` is not Laurent. Scalar normalisation does not rescue it:
  `det ρ(w) = (−1)^L` forces `L` even and `λ = ±1`.
- `qbeta_braid_image_eigenphase_exclusion_probe.py` — no braid-image transfer
  matrix carries it in **any** convention, by boundedness. Extended
  Laurent → algebraic in `qbeta_eigenphase_algebraic_exclusion_probe.py` +
  sorry-free `QOU.QBeta.BraidImageEigenphaseAlgebraic`.
- `QOU.QBeta.EigenphaseCarrier.carrier_is_trivial` — the Lean carrier is
  **proved vacuous**, independent of the citation defect measured above.
- `qbeta_ladder_required_phase_probe.py` — the convention-parameter class is
  pruned for D: required window half-width ≈1.09e-5 rad, `z_D` misses by
  ≈1.19e-2 rad, ~1000×.

**And S1 is smaller than this bean's header says.**
`QOU.BraidKnot.Q_beta_categorical_ofPhase_tail_common` (sorry-free): `z` reaches
the ladder at exactly one place, the N=1 phase, so `c₂ … c₅` are **phase-blind**
and do not need re-deriving. **The D-frame work is the phase and only the
phase.** The header's "every ≈−2 value-level fact is C-conditional" still holds
for the recorded values; what does not hold is that the whole tail needs
re-derivation.

**Still open**, quoting the seminormal probe's own scope section — these are
where a supplied phase could come from, and nothing above excludes them:

1. an `M_β` from a **non-scalar** normalisation (divided by a `q`-dependent,
   non-rational Markov-trace factor);
2. an `M_β` **outside the braid image** — a general element of `H₃(q)`, or an
   operator on a larger space restricted to `V_(2,1)`;
3. the KZ / Kohno–Drinfeld holonomy branch, which the `EigenphaseCarrier`
   trichotomy leaves as branch (3). **Check `9a8b09c661` on main first** — its
   subject says the Kohno–Drinfeld route was excluded, and I have not read it.

The provenance finding itself is unaffected: the attribution defect and the
4–5 % / 88× measurements stand independently of all of this.


### Route 3 (KZ / Kohno–Drinfeld) is CLOSED — checked, per the caveat above

The entry above listed it open with "check `9a8b09c661` first". Checked:
`QOU/QBeta/HolonomySpectrumSignObstruction.lean` (`4471ee72ce`, 2026-08-31,
6 theorems, sorry-free) **excludes every holonomy whose generator has real
spectrum**, Kohno–Drinfeld included. Residue-independent — a real eigenvalue `a`
gives character `cosh a ≥ 1` for every real `a`, and the required factor is
**0.998399 < 1**. The obstruction is `(x−1)² ≥ 0`.

**Exact cross-check with my probe.** That 0.998399 is what
`qbeta_ladder_alpha_provenance_probe` computes as `cos(α − u/2)` at C
(0.9983989452530845), and the surviving condition's angle `θ = 0.0565947` is
exactly `|α − u/2|` there. Same object from opposite directions — one asking
what the ladder's factor **is**, the other what could **produce** it.

**Route status after this:**

| route | status |
|---|---|
| non-scalar normalisation (÷ a `q`-dependent non-rational Markov-trace factor) | **open** |
| `M_β` outside the braid image | **open in general**; holonomy sub-case closed for real spectrum |
| KZ / Kohno–Drinfeld | **CLOSED** |

**The surviving condition is sharp:** a connection whose generator is
**elliptic** at real `q` — `det A > 0`, spectrum `±iθ`, `θ = 0.0565947`. The
imaginarity must be **sourced**; the corpus names `conj:im-q-physical-role`, and
it is Tier-0 condition D0 on `qou-pdix` / this bean.

Pointer, not a result: AGENTS.md's Im(q) banner separates the **observable**
level (`Im(q₀) = 0`, verified) from the **fibre** level (`Im(q)` unconstrained).
An elliptic generator at real `q₀` needs its imaginary part from somewhere, and
the fibre level is the only place the framework leaves for it. Nothing here
derives such a generator or shows one exists.


## 2026-09-04 — my elliptic-generator recommendation was ALREADY REFUTED (PR #6688)

I recommended, twice, pursuing the elliptic-generator condition via
`conj:im-q-physical-role`. **Corpus-grep on starting: that is refuted.** The arc
is well developed and current, and I did not know it:

- **step 18** `HolonomySpectrumSignObstruction` — the generator must be elliptic;
- **step 19** `ImQCannotSupplyEllipticGenerator` /
  `qbeta_imq_elliptic_generator_refutation_probe.py` — **Im(q) is not the source
  AT THE ARCHIMEDEAN LEVEL. Scoped 2026-09-04, see below; the fibre level is
  OPEN.** `|q|² = x² + y² > 1` for every `y` since `Re q = 1.10998 > 1`, so a
  purely elliptic generator is impossible outright; forcing `Re[character]` onto
  0.998399 needs `Im(q) = ±0.139956` and leaves `Im[character] = 0.014069`,
  8.40× the entire deviation and 18074σ.
- `qbeta_bring_elliptic_generator_probe.py` — Bring's elliptic curve passes D0
  *in principle* but hands the ladder no phase;
- `qbeta_decay_operator_elliptic_spectrum_probe.py` — **an elliptic generator
  DOES exist in the corpus**: `Δ_L = NF(n) − NF(p)`, an algebra element (not a
  braid image) in the (2,1) block. Wrong phase: `θ = 2.0204` vs required
  `0.056595`, a factor of **35.7**.

### SCOPE CORRECTION to my own line above (same day, caught on check-in)

I wrote "**Im(q) is NOT the source**" flat. That is **under-scoped**, and main
landed the reason while this branch sat: `e68347cc12` **retargets
`conj:im-q-physical-role` to the fibre**, recording that all three candidate
roles are *"settled at `q_0` and all three stay open on the fibre"*.

The step-19 argument I quoted is archimedean by construction — it reasons from
`Re q = 1.10998 > 1` at the substrate anchor, so `|q|² > 1` for every `y`. That
refutes Im(q) **as an observable-level quantity**. It says nothing about the
fibre, where `Im(q)` is unconstrained (AGENTS.md's Im(q) banner makes exactly
this split, and I cited that banner two messages before making the error).

So the correct statement is: **Im(q) is refuted as the elliptic source at the
archimedean level; at the fibre level it is open, and as of `e68347cc12` that is
where the conjecture now lives.** That also means my "every route I can name is
closed" summary was too strong — the fibre reading of route 5 is live.

So there was nothing for me to add by "researching the elliptic condition"
*as an archimedean question*. What I did instead was audit the number every
candidate is scored against.

### The target is experimentally anchored — my circularity worry was WRONG

I expected `0.0565947` to be the ladder's own `cos(α − u/2)` output, which given
#6625 would make every branch-3 candidate scored against a fit. It is not:

    required = Q_exp / (Q_A·(1 − u²)) = 0.99839766871925519

uses only the `Q_A` closed form, the structural `c_2 = −1`, and CODATA — no `z`,
no `α`, no fitted `c_k`. **Branch 3 has a legitimate criterion.** Recorded as a
refuted worry, not dropped.

### The defect that IS there

`arccos(required) = 0.0566173`. The **quoted** target `0.0565947` is `|α − u/2|`
— the form's own phase — matching it to `6.6e-7` while matching the experimental
value only to `4.0e-4`.

**Correct branch-3 target: `θ_required = 0.0566173`, not `0.0565947`.**

Changes no verdict on record (0.0399 % against `Δ_L`'s 35.7× miss). Matters only
for a candidate landing inside 4e-4 — which is the regime in which a branch-3
result would be *declared*, so it should be right before then.

Convention note, so it is not misread: the C form sits 1.28e-6 from the
requirement, the D form 6.02e-4, ~470× further. Consistent with the ladder having
been **built** in C; **not** evidence for C, which is excised.
## 2026-08-31, S1 — the gate inventory is EXHAUSTED. Do not run the sweep.

Probe: `computations/qbeta/qbeta_d_gate_inventory_is_exhausted_probe.py`, **10/10**,
exact sympy.

PR #6282 named three gates on a candidate D-frame Habiro generator `rho` and
retracted two of them in its own commits. This closes the third — the one I
recorded as surviving.

    gate                     verdict
    -----------------------  ---------------------------------------------------
    bar-parity               FILTER, not a selector: every symmetric q-integer is
                             bar-invariant, so it admits the whole family (#6282)
    Hankel c_2*c_4 = c_3^2   VACUOUS for rank-1: c_3 = rho*c_2, c_4 = rho^2*c_2,
                             so it holds IDENTICALLY for every rho (#6282)
    C-limit reduction        VACUOUS: see below (THIS ENTRY)

### Why the C-limit gate is vacuous

The gate asks that the D ladder reduce to the C ladder where the conventions
agree, i.e. where `z_C = sqrt(q)/(q+1)` equals `z_D = q^3/(q^2+1)`. Solved
exactly: **the only positive real solution is `q = 1`.** Away from it they
diverge immediately (`q = 1.11`: `z_C = 0.499320` vs `z_D = 0.612710`).

And `q = 1` is exactly where the ladder is degenerate:

    hbar_q(1) = 0      u(1) = 0        h(1) = 0
    Vhat_D(1) = 1      alpha_D(1) = 0  X(1) = u*Vhat_D = 0

so every rung factor `1 + c_k X^k` is 1, the whole product is 1 **for symbolic
`rho` and symbolic `c_2`**, and the sibling's derived N=1 factor
`M = cos(a_D - h^2/4)cos(h^2/4)` is 1 as well. The ladder collapses to the bare
`Q_A` for **every** candidate. The gate is satisfied by all of them.

### Consequence for S1 — this is a prune, not a setback

**All three named conditions admit every candidate.** They do not rank
candidates; they are satisfied identically. So a wider sweep against these gates
cannot select a generator no matter how many candidates it enumerates.

This is the formalize-first discipline applied to my own proposed search: the
structural argument says **do not run the scan**. That is the rule's whole
purpose — "too much time is lost chasing numerical rainbows that a one-line
structural argument would have eliminated up front" — and the rainbow here was
mine, proposed at the end of #6282 ("search for a bar-INVARIANT single
generator, test any candidate against the Hankel condition, check its weights").
Two of those three gates I had already retracted; this closes the third, so that
proposed next move is now fully withdrawn.

Scope **(a)**: a scope-limited negative about the three gates identified so far,
NOT a claim that no gate exists.

### What S1 actually needs

An **external structural input**, not more candidates. Not asserted here as
available — naming routes is the next step, and each needs the corpus-grep
before it is called open or novel.

## 2026-09-02, S1 — the Wenzl c_3 candidate: a fit that misses, formalized as `rfl`

Probe: `computations/qbeta/qbeta_wenzl_c3_candidate_audit_probe.py`, **6/6**.

Found by the corpus-grep for an external structural input (the previous entry's
stated next step). `docs/coordination/2026-06-13-qbeta-habiro-element-ledger.md`
records a candidate for `c_3` and marks it "Structural decomposition identified.
Proceeding to formal derivation." It is a **worked instance of the
gate-exhaustion finding**, which is why it belongs here rather than as a
separate defect.

### What the ledger says, verbatim

    "Swept q-deformed fractions against the empirical c_3 = -2.06249 from
     Kashiwara truncation."
    "Finding: The residual EXACTLY matches -2 - (3/2) W_4(q), where
     W_4(q) = 1/[4]_q! is the alternating Wenzl weight."

The selection method is a **sweep against an empirically extracted target** —
a fit, by its own wording.

### "Exactly matches" does not hold

    [4]_q!                    25.1536370049
    W_4 = 1/[4]_q!             0.0397556822422
    candidate -2-(3/2)W_4     -2.05963352336

      vs ledger's own target        -2.06249          0.1385 %
      vs live extracted, proton     -2.0693425728     0.4692 %
      vs live extracted, muon       -2.0202002328     1.952  %

Not exact against **any** of them — including the target it was swept to.

### The promised formal derivation is `X = X`

`folio/quantum-observable-universe/lean/QOU/BraidKnot/QBetaWenzlDecomposition.lean`:

```lean
noncomputable def q_beta_c3_wenzl_coefficient (q : ℝ) : ℝ :=
  -2 - (3/2 : ℝ) * wenzlAltWeight 4 q

theorem q_beta_c3_wenzl_decomposition_exact {q : ℝ} :
  q_beta_c3_wenzl_coefficient q = -2 - (3/2 : ℝ) * wenzlAltWeight 4 q := by
  rfl
```

The theorem unfolds the definition and proves it equals itself. Its docstring
says *"Here we formally assert the Wenzl weight identity for the c_3 scalar"* —
it asserts nothing. This is `X = X := rfl`, banned by AGENTS.md §"No trivial
trues, no tautologies, no laundering" rule 5; and the definition's own docstring
says the value was *"Empirically identified"*. **Sorry-free is not derived.**
Nothing in that file connects the Wenzl weight to `c_3`.

### Why this belongs to the gate-exhaustion entry

`W_4` is built from symmetric q-integers, so it is **bar-invariant** — verified
symbolically, as is the whole candidate. It therefore **passes the parity gate**,
and would pass the Hankel and C-limit gates too, since those hold identically.

That is the previous entry instantiated: a candidate with a categorical story,
clearing every named gate, and still a fit that misses by 0.47 % against the
live value.

### Reconstruction-independence, stated because one finding is weaker

Findings above are independent of how this probe rebuilds the ladder: the
0.1385 % is two stated numbers compared, the `rfl` is read off the file, the
bar-invariance is symbolic. A **fourth** check — that no pin reproduces the
ledger's headline `-0.0005 ppm` (closest reconstruction 0.00738 ppm away) —
**does** depend on the reconstruction, and is recorded as the weakest of the
four. Same caution as table 3 in `qou-54g5`.

### Scope

**(a).** NOT a claim that the Wenzl weight is the wrong object, that `1/[4]_q!`
plays no role, or that the ledger's categorical reasoning is wrong. Only that
**this identification is unestablished**: not exact, selected by fitting, not
derived by the Lean written for it.

**What would establish it:** derive `c_3` FROM the H_4 Wenzl projector — the
route the ledger says produced `1/[4]_q!` in the m_n−m_p split — with Lean
deriving the coefficient rather than restating it. Not attempted here.

## 2026-09-02, S1 — WHY parity cannot select: the bar-fixed subfield is Q([2]_q)

Probe: `computations/qbeta/qbeta_bar_fixed_field_is_q_of_two_probe.py`, **19/19**,
exact sympy. This upgrades the gate-exhaustion entry from an empirical
observation to a structural one, and supplies the reason.

### First, a CORRECTION to PR #6282's own wording

That PR said D's bar action is a multiplicative grading, `bar(x)/x = q^w`.
Measured, the ratio is **`±q^w`** — there is a Z/2 sign alongside the Z weight,
and the sign is not a curiosity:

    q        +q^-2         b          +q^0
    h        -q^0    <--   z_D        +q^-4
    hbar_q   -q^1    <--   u          +q^2
    h^2      +q^0          Vhat_D     +q^-2
                           u*Vhat_D   +q^0

**`h`, the ladder's primary ingredient, is bar-ANTI-invariant of weight 0.** Its
square is invariant, which is the only reason `u = b*hbar^2` came out clean —
the sign squares away. The pure-Z-grading statement is right about `u` and
`Vhat_D` by accident of their even degree in `h`, and I generalised from those
two cases.

### The reason parity cannot select

Bar-invariance is exactly membership in the fixed field, and that field is
`Q(s)` with `s = q + 1/q = [2]_q`:

- `bar(s) = s`;
- `q` satisfies `q^2 - s*q + 1 = 0` over `Q(s)`, so `[Q(q) : Q(s)] = 2`;
- `1/q` is the other root, and bar exchanges them, so bar is a nontrivial
  `Q(s)`-automorphism;
- hence by Galois for a degree-2 extension, **`Fix(bar) = Q(s)` exactly**.

And every symmetric q-integer is a Chebyshev polynomial in `s` — verified n=1..8,
and it is the recurrence `U_k = s*U_{k-1} - U_{k-2}`, not a coincidence about
small n:

    [1] = 1              [2] = s            [3] = s^2 - 1
    [4] = s^3 - 2s       [5] = s^4 - 3s^2 + 1
    [6] = s^5 - 4s^3 + 3s                   [7] = s^6 - 5s^4 + 6s^2 - 1

so they all lie in `Z[s] ⊂ Q(s)`. The ladder's own ingredients sit there too:
`h^2 = s^2 - 4`, and `b = sqrt([3]_q)/[2]_q = sqrt(s^2-1)/s` in the quadratic
extension `Q(s)[sqrt(s^2-1)]`.

**CONSEQUENCE.** "`rho` is bar-invariant" is the single condition "`rho` lies in
an index-2 subfield" — and an index-2 subfield of `Q(q)` is still an
infinite-dimensional Q-vector space. A condition whose solution set is an entire
function field cannot select one element of it.

That is why the parity filter admitted `[2]_q … [5]_q` in #6282 and will admit
every further one: **they are polynomials in `[2]_q`, and `Q([2]_q)` IS the
fixed field.** No sharpening of parity-type reasoning helps, because there is
nothing left to sharpen.

So the gate inventory being exhausted is a *structural fact*, not a gap in the
search — the three gates are consequences of, or weaker than, membership in
`Q(s)`.

### Scope, stated carefully because half of this is (b)

- **(b) STRUCTURAL** for the narrow claim: `Fix(bar) = Q(s)` is Galois for a
  degree-2 extension, and the Chebyshev identity is a recurrence. Neither is a
  numerical observation.
- **(a) scope-limited** for the consequence: it says **parity** cannot select the
  generator, NOT that the generator is unselectable. An input that is not a
  parity condition — a degree bound, an anchor-independent functional equation,
  a derivation from the H_4 Wenzl projector — is untouched by this.

### Next, and deliberately not done here

Formalise `Fix(bar) = Q(s)` and `[n]_q = U_{n-1}([2]_q)` in Lean. The corpus
carries bar-invariance lemmas for individual `quantumInt` values; the general
statement is what is missing. That is the honest thing to prove — and it is
worth more than any further candidate testing, since it is the theorem that
makes candidate testing pointless.

### CORRECTION to the entry above — I had the Lean inventory backwards

The previous entry closes with: *"The corpus carries bar-invariance lemmas for
individual `quantumInt` values; the general statement is what is missing."*
**Both halves are wrong, and in opposite directions.** I wrote it without
grepping, immediately after an entry whose whole subject is a claim asserted
without checking.

**What IS present** — `folio/quantum-observable-universe/braids-and-knots/bar-involution.lean`,
sorry-free, generic over `[CommRing R] [BarInvolution R]`:

    IsBarSymmetric / IsBarAntiSymmetric        (both, as first-class predicates)
    barSymmetricProjection / barSkewProjection + `decompose`
    IsBarSymmetric.add / .mul / .neg
    IsBarAntiSymmetric.add / .neg
    IsBarSymmetric.of_mul_antisym
    IsBarAntiSymmetric.of_sym_mul
    IsBarAntiSymmetric.pow_two_mul  /  .pow_two_mul_add_one

So the **general** bar-grading algebra is already there — including the Z/2 half.
`IsBarAntiSymmetric.pow_two_mul` is exactly the "the sign squares away" fact I
observed for `u = b*hbar_q^2`. My correction to #6282's wording stands (that PR
did drop the sign), but I should not have implied the corpus was unaware of it:
it carries the anti-symmetric half as a first-class notion.

**What is ABSENT**: `quantumInt` bar-invariance, at all. Not per-n, not general —
grepped for `IsBarSymmetric (quantumInt`, `quantumInt_bar`, `bar_quantumInt`,
and for `quantumInt` near `bar`: nothing. And no `[n]_q = U_{n-1}([2]_q)`; the
Chebyshev material in the corpus (`brings-surface/genus-filtration-ideal.lean`)
is about Seifert genus and is unrelated.

So the inventory is the reverse of what I wrote: **the abstract layer is
present, the concrete instantiation is missing.**

### Which makes the Lean target sharper, not vaguer

The missing bridge is one lemma, and it connects two things that already exist:

    theorem quantumInt_barSymmetric (n : N) (q : R) : IsBarSymmetric (quantumInt n q)

with the Chebyshev identity `quantumInt n q = U (n-1) (quantumInt 2 q)` as the
natural route (induction on the recurrence `U_k = s U_{k-1} - U_{k-2}`, with
`IsBarSymmetric.add` / `.mul` / `.neg` discharging the step — all already proved).

That is a better target than the field-theoretic `Fix(bar) = Q(s)`, which needs
Mathlib `IntermediateField` / `fixedField` machinery. The lemma above delivers
the load-bearing half of the S1 finding — *every symmetric q-integer passes the
parity filter, for all n* — inside the corpus's own existing abstractions.

Not attempted here.

## 2026-09-02, S1 — LEAN: every symmetric q-integer is bar-symmetric, for all n

`folio/quantum-observable-universe/lean/QOU/BraidKnot/QuantumIntBarSymmetric.lean`
— `lean`-direct **exit 0**, no errors, no warnings; `#print axioms` on all seven
declarations gives `[propext, Classical.choice, Quot.sound]`, **no `sorryAx`**.

This makes the S1 negative permanent. The empirical observation was that the
parity filter admits `[2]_q … [5]_q`; this proves it admits `[n]_q` for **every**
`n`, so no candidate generator built from symmetric q-integers can ever be
distinguished from another by bar-parity.

    theorem quantumInt_isCPEven {q : R}
        (hbarq : BarInvolution.bar q = q⁻¹) (hden : q - q⁻¹ ≠ 0) (n : ℕ) :
        IsCPEven (quantumInt n q)

The proof needs neither the Chebyshev identity nor any field theory: numerator
`qⁿ - q⁻ⁿ` and denominator `q - q⁻¹` are each bar-**anti**-symmetric, and the two
signs cancel in the quotient. Supporting lemmas `bar_zero'`, `bar_neg'`,
`bar_sub'`, `bar_inv'`, `bar_inv_eq` are derived from the four class axioms
(`bar_involutive`, `bar_add`, `bar_mul`, `bar_one`) — the class has no `bar_zero`
or `bar_inv` field, so both are proved rather than assumed.

**Base ring (§7c):** generic `{R : Type*} [Field R]`, `Field` only because
`[n]_q` needs `q⁻¹`. No ordering, no `Real.sqrt`, no archimedean construct, no
numerical `q₀`. Pre-archimedean.

### Where it had to live, and why that is a finding

The ring-level bar algebra I cited two entries ago —
`braids-and-knots/bar-involution.lean`, 321 lines, sorry-free, carrying
`IsBarSymmetric`/`IsBarAntiSymmetric` and the closure lemmas — **is outside the
Lake library glob** (`globs = ["QOU", "QOU.+"]`; that file is under
`braids-and-knots/`, not `QOU/`) and **is imported by nothing**. The only
reference to it anywhere is a docstring mention in `ThetaQcdFramingCp.lean`.

So my "PRESENT" in the correction entry was true of the *source* and false of the
*module*: the algebra is proved but unreachable from any library file. That is a
third correction to my own inventory, and it is the one that changed what could
be built.

It also cites `bar-symmetric-three-layer-synthesis.lean` as the file it
"intentionally duplicates during the transition, once both blocks land on main".
**That file does not exist.** The transition its header describes cannot complete
as written.

**What is reachable, and is a better home anyway:**
`QOU/StandardModel/ThetaQcdFramingCp.lean` declares an in-library
`BarInvolution` + `IsCPEven`, with a docstring saying it is declared locally
"so this file is verifiable stand-alone by `lean`-direct without depending on
whether the content-block sibling is compiled". Someone hit this exact problem
and solved it locally. It also already carries `bar_qpow`
(`bar (qⁿ) = (qⁿ)⁻¹`), which is precisely the helper this proof needs.

### Verification, and two process notes

`lean`-direct against the real import cone (a genuine Lake build here — 3399
traces against 3393 mathlib oleans, so not a restored no-trace cache and
`lake build` was never at risk). Compiled with `-o` to produce an olean, then a
separate importing file for `#print axioms`, because bare `lean` writes no olean.

Two of my own errors, both caught before any claim: I wrote `linarith` into a
proof over a generic `CommRing` and a nonsense `▸` term, and I read `EXIT=0`
off `head` rather than off `lean` on the first run — the same wrong-exit-code
trap recorded earlier in this bean. The first real run then failed on two
Mathlib argument-order mismatches, fixed with `linear_combination` and an
explicit `calc` rather than by guessing further lemma names.

## 2026-09-02, S1 — I re-derived a result the corpus already has. Credit + a small correction.

Working the "what non-parity input could select ρ?" question, I computed the
experimental error bar on `c_3` and was about to record it as an S1 finding.
**The corpus already has it**, and the corpus-grep caught me one step before
writing it up.

[`mass-theory/rem-qstar-decay-sector-q0.md:43`](../folio/quantum-observable-universe/mass-theory/rem-qstar-decay-sector-q0.md)
states it exactly:

> "The extractor amplifies the experimental Q_β uncertainty by `1/u³`, giving
> `σ(c_3) = σ(Q_β)/(Q_N2 u³) ≈ ±1.262` — about 61 % of `|c_3|`. Against that
> band, `c_3`'s proximity to `−Vol(4_1)` is 0.031σ at the proton pin and 0.008σ
> at the muon. These are not close agreements in the evidential sense; they are
> the absence of a measurement, since every candidate constant in
> `[0.807, 3.331]` agrees at least as well."

Same mechanism, same conclusion, and it goes further than I had (the admissible
interval, and the `32×`/`130×` sharpening a decisive measurement would need).
**Not my finding.** Recorded here because it is directly load-bearing for S1 and
belongs in this bean's chain of reasoning, not because it is new.

### What it means for S1, combined with the parity result

Two independent closures now sit on the generator:

- **Parity cannot select it** — `Fix(bar) = Q([2]_q)`, an infinite-dimensional
  family, now Lean-proved for all `[n]_q` (this bean, above).
- **The data cannot select it either** — `c_3 = −2.069 ± 1.38` is a 67 %
  uncertainty, so `−2`, the Wenzl `−2.0596`, and `−(b²+1/2) = −1.2527` all sit
  **inside 0.6σ** of the extracted value and of each other.

So the "3.47 % gap" between `−2` and the extracted `c_3` that this corpus has
flip-flopped over six times is **0.05σ**. It is not a near-match to be explained;
it is a quantity with no measurement behind it.

Only the superseded `+12.87` is excluded, at **10.8σ** — an independent
confirmation of the `c_5`-slot direction settled in `qou-54g5`, from a completely
different argument.

### One correction to the block's number, in the direction that strengthens it

The block's `±1.262` corresponds to the **neutron-mass-alone** uncertainty:

    sigma source                          sigma(Q_beta)   sigma(c_3)   % of |c_3|
    full quadrature (Q_NEUTRON_MEV_ERR)      6.66408e-7      1.37865      66.62 %
    neutron mass alone (M_N_MEV_ERR)              6.0e-7      1.24126      59.98 %
    proton alone                                  2.9e-7     0.599943      28.99 %
    electron alone                               1.6e-10   0.000331003      0.016 %

But `Q_β = m_n − m_p − m_e`, and `qou_substrate.constants` defines
`Q_NEUTRON_MEV_ERR` as the quadrature sum of all three — the proton term alone
contributes 29 %, which is not negligible. So the correct bar is **±1.379
(66.6 %)**, and the block's is understated by ~9 %.

That makes the block's own argument **stronger**, not weaker: the admissible
interval widens, so even more candidates are indistinguishable. Not fixed here —
it is a one-number edit in another chapter's block, and it belongs with whoever
owns that block rather than riding on an S1 branch.

## 2026-09-03, S1 — the two c_3 bands are the SAME sigma, 100x apart. Do not conflate them.

Probe: `computations/qbeta/qbeta_c3_two_bands_are_the_l2_factor_probe.py`, **8/8**.
Reviewing what landed on main and the live sibling PRs, two bands for the same
number are now in the corpus:

    (1) EXPERIMENTAL   rem-qstar-decay-sector-q0.md:43
        sigma_exp(c_3) = sigma(Q_beta)/(Q_N2 u^3) = +/- 1.262    (61 % of |c_3|)
        "the absence of a measurement ... every candidate constant in
         [0.807, 3.331] agrees at least as well"

    (2) L2 TOLERANCE   PR #6353, relayed by #6342
        c_3 = -2.0693425728 +/- 0.01262                          (0.61 %)
        "c_3 = -2 = J_Hopf(q=1) is 5.495x outside"

**`band(1)/band(2) = 100.0` exactly** — band (2) is band (1) scaled by the L2
goal's own factor (`sigma_pred <= sigma_exp/100`). Verified to the digit,
including that #6353's `5.495x` reproduces specifically from the *neutron-only*
sigma; under the quadrature sigma it is `5.03x`.

### Both are true, and the same gap sits on opposite sides of them

    |c_3 - (-2)| = 0.0693426
      vs band (1)   0.055 sigma   INSIDE    experimentally indistinguishable
      vs band (2)   5.495 x       OUTSIDE   misses the L2 goal by 5.5x

**`5.495x outside` is NOT evidence against `c_3 = -2`.** That candidate sits
0.055σ from the extracted value; nothing in the data disfavours it. The 5.495x
says only that *if* `-2` holds, Q_β's L2 goal is missed by 5.5×. A statement
about the **goal**, not the candidate.

Reading it the other way is exactly the trap AGENTS.md's own `c_k` banner
records — *"a quantity differing only by normalisation, mistaken for a
discrepancy"* — one normalisation over. Flagging it because the two bands were
recorded days apart, by different sessions, and the `5.495x` phrasing reads as a
refutation on its own.

### The consequence, which is the substantive part

**A derived `c_3` that meets the L2 tolerance could not be validated against
Q_β at all.** It would be a number claimed to 0.61 % inside a quantity the
experiment pins to 61 %. The measurement cannot separate a correct derivation
from a wrong one landing anywhere in `[0.807, 3.331]`.

So Q_β's L2 target sits **two orders of magnitude beyond current experimental
reach on this parameter**. Consequences, both concrete:

1. A derived `c_3` has to be justified **structurally**. Empirical agreement
   with Q_β is available to every candidate in that interval and therefore
   discriminates nothing — including agreement claimed by a future derivation.
2. The experimental route is quantified, not hopeless: the source block gives
   **32×** (proton pin) / **130×** (muon pin) sharpening of the neutron
   Q-value as what would make this parameter testable.

This composes with the two closures already in this bean — parity cannot select
the generator (`Fix(bar) = Q([2]_q)`, Lean-proved for all `[n]_q`), and the data
cannot either. The third leg is now explicit: **even a successful derivation
could not be checked here.**

### Scope and coordination

**Scope (a).** Not a claim that `c_3 = -2` is right, nor that the L2 goal is
unreachable.

**Coordination.** Band (2) is #6353's, reached independently and **first**;
#6342 relays it. This entry adds only the *relation* between the bands and its
consequence. It takes **no position** on #6342's entry-9 `|c_4| <= 1.4816`
threshold, which is that PR's result and is not re-derived here.

## 2026-09-03, S1 — "RESOLVED" overstates the swing: it carries ±0.0052 from the muon pin

Probe: `computations/qbeta/qbeta_c3_derivative_vs_value_precision_probe.py`,
**7/7**.

**Most of what I set out to find was already in the corpus, and my corpus-grep
missed it because I searched `AGENTS.md docs/audits/ content/` and skipped
`computations/` — path 3 of the checklist.** There are ~55 `qbeta_c3_*` probes.
Recording what is theirs before what is mine:

- **The 1/u³ amplification and the value bar are `qbeta_c3_experimental_uncertainty_probe.py`'s**:
  gain `1.618e6`, `σ(c_3) = 1.16`, *"-2 is inside 1 sigma"*. Same mechanism I
  re-derived, same conclusion.
- **The common-mode cancellation is `qbeta_c3_swing_gate_probe.py`'s**, and it
  goes further than I did: it *derives* the cancellation by perturbing `Q_β`
  rather than asserting it, and already uses the swing as the **primary resolved
  filter on candidate `u(q₀)` maps**, replacing a conditional diagonal gate.

### What survives, and it bears on that live gate

That probe calls the swing **RESOLVED** on the grounds that the CAL-3 error is
common-mode — and **does not propagate the pin uncertainty** (grepped:
no `MASS_RATIO_MU_E_ERR`, no `dq/dr`, no pin σ anywhere in it).

That is exactly the gap my own first pass had. Propagating it:

    sigma(swing) from Q_beta   (common-mode, cancels)   +/- 8.33e-7
    sigma(swing) from muon pin (does NOT cancel)        +/- 5.21e-3   <- 6255x larger
    total                                               +/- 5.21e-3

    swing        = -0.049482266
    significance = 9.4936 sigma

**The swing is significant but not exact.** It carries a **10.5 %** bar. A gate
keyed on ΔS must allow that tolerance; a tighter one rejects correct candidates.

The 9.4936σ independently reproduces the **9.5σ** μ–p substrate tension AGENTS.md
documents, from the Q_β side rather than the m_μ side — which is what convinced
me the corrected number is right rather than a third error.

### Two errors of mine, in opposite directions, before that

1. Propagating only `Q_β` gives *"the swing is 59,400σ"* — wrong by four orders,
   and it would have passed every gate in this repo.
2. My first hand-fix applied the 22.2 ppb **directly to q**, giving *"0.53σ, not
   significant"* — also wrong, because the ratio→q₀ map **compresses** by ~18×
   (`dq/dr = −2.95e-4`).

### The one consequence worth carrying forward

    quantity      value          sigma        relative     limited by
    c_3           -2.0693        +/- 1.379      67 %       Q_beta^exp
    dc_3/dq        3838405.9     +/- 4.04e5     10.5 %     m_mu/m_e

**"Improve the measurement" is two programmes.** Sharpening `Q_β` (the 32× / 130×
in `rem-qstar-decay-sector-q0`) buys the **value** and almost nothing for the
derivative; sharpening `m_μ/m_e` buys the **derivative** and nothing for the
value. The derivative's *value* is the corpus's three ways over (my fourth route
agrees to ~1e-6); the **error bar** is what was missing.

### Note on a small numeric difference, not chased

The swing-gate probe records `ΔS = 0.0491423421` (its O2 value); I get
`0.049482266`, 0.7 % apart. Different extraction paths (its `S_leak` carries a
`Vol(4₁)` that cancels in the swing). Flagged, not reconciled — it does not
move the 10.5 % conclusion, and reconciling it belongs with that probe's owner.

### Scope

**(a).** Convention C. Not a claim that the swing gate is wrong — its cancellation
derivation is sound and its use as the primary filter stands. Only that its
tolerance should be **±0.0052**, not zero.

---

## Route 5, projection: the mechanism is PARTIAL, and it retracts my own #6875 (2026-09-05)

Probe: `computations/qbeta/qbeta_fibre_projection_and_rou_sublocus_probe.py` (5/5).
Audit: `docs/audits/2026-09-05-cds1-projection-and-rou-sublocus.md`.

**Retraction first.** #6875 derived `N = 5` (modulus kept) / `N = 4` (analytic
continuation) from the reality of `Q_A/m_e = |q²−2q−1|(q+1)/(2q³)` on `|q| = 1`.
**That form holds only on the real axis** — it follows from the block's own
`|Δ(net)|·E_0` only via `|q²−1| = (q−1)(q+1)`, which needs `q` real `> 1`.
Measured gap: `0` at `q = 1.1`, **2.407** at `q = e^{i/3}`, **1.186** at
`q = e^{iπ/3}`. Both `N` values are withdrawn.

**The mechanism was already in the corpus.** `neutron-qvalue-symbolic` writes
`𝔔_β = |Δ(net)| · E_0` — the projection *is* the modulus, and it is applied to
`Δ(net)` alone, with `E_0 = m_e/(q(q−1))` unprojected. That partiality is the
entire source of the reality condition:

    𝔔_β real on |q|=1  ⟺  Im[q²−q] = sin φ (2 cos φ − 1) = 0
                       ⟺  φ ∈ {π/3, π, 5π/3}    — the SIXTH roots

A **full** projection `|Δ(net)·E_0|` is real for every `q` and selects nothing.
**So the projection question and the N question are one question.** Taking the
full projection *because* it admits the required phase would be fitting the
mechanism to the target — named, not taken.

**The root-of-unity sublocus is EMPTY**, on grounds independent of `θ`:
`π/3` and `5π/3` are primitive 6th roots, where `q⁶−1 = (q²−1)(q⁴+q²+1)` forces
`q⁴+q²+1 = 0` and so Hoefsmit `b² = (q⁴+q²+1)/(q²+1)² = 0` — `V_{(2,1)}`
decouples; `φ = π` gives `h = q − 1/q = 0`. Verified numerically (4.139e-41 at
40 dps) and exactly (`expand_complex` → 0); `sympy.simplify` alone reports a
**false** non-degeneracy here.

`θ` is not the binding constraint: it sits 18.496× below `π/3`, but the
emptiness is established before `θ` is mentioned.

**Scope (a)** for the reality arithmetic; the degeneracy exclusion is exact.
**Route 5 is not closed** — `|q| = 1` is much more than its roots of unity, and
the full projection stays structurally available at the price of selecting
nothing.

### Strengthening, same day: the partial projection kills the WHOLE locus

Probe: `computations/qbeta/qbeta_fibre_partial_projection_kills_whole_locus_probe.py` (5/5).

The scope line I wrote above — *"`|q| = 1` is a great deal more than its roots
of unity"* — is true about the locus and **irrelevant to the argument**. The
reality condition `sinφ(2cosφ−1) = 0` is imposed at **every** point of `|q| = 1`,
and its solution set on `[0,2π)` is exactly `{0, π/3, π, 5π/3}` — four points,
all roots of unity. The non-rational phases were never open; I described them as
open. Verified by `solveset` and by an independent 20,000-point scan.

All four degenerate, and `φ = 0` twice (`h = 0` *and* the `E_0` pole — I had
checked only the pole). So:

    PARTIAL  ->  reality leaves 4 points, all degenerate  ==> whole locus excluded
    FULL     ->  no condition at all                      ==> nothing selected

**Route 5's N-selection mechanism predicts nothing under either reading.**
Scope (a) on the MECHANISM; silent on route 5's underlying fibre-Habiro idea.

**The load-bearing assumption, now isolated:** that `𝔔_β` must be real *at the
fibre evaluation point* rather than after the archimedean functor. `AGENTS.md`'s
fibre-vs-observable banner says `Im(q)` is unconstrained at fibre level — so this
closes the mechanism as posed and reopens whether reality belonged there at all.
That is the next question, and it is a framework question rather than a
measurement.

Method trap worth keeping: the first scan reported a spurious **fifth** zero
because dedup used linear distance and `φ = 0` / `φ = 2π` are the same point.
On a circle use `min(d, 2π−d)`. The false reading was a spurious *finding*
("solveset missed a branch"), not a spurious failure.

### 🛑 RETRACTION — owner ruling 2026-09-06: "Does not need to be real in fiber."

The reality premise **both** sections above inherit from #6875 is **rejected**.
The strengthening section flagged it as load-bearing and asked the question; the
owner has resolved it against the premise.

**Withdrawn:**
- "reality selects N on the fibre locus" (#6875, both readings)
- "the root-of-unity sublocus is EMPTY *because reality admits only 3 phases*"
- "the partial projection excludes the ENTIRE fibre locus" — the exclusion ran
  entirely through the rejected premise

Reality of `𝔔_β` is an **archimedean** constraint on the evaluation at `q₀`
(`lusztig_q_0_imaginary_part_zero`; a `complex-substrate-interpretation` sidecar
note already flags that fibre-vs-observable `Im(q)` is exactly the AGENTS.md
2026-06-01 distinction). Imposing it on `|q| = 1` was the level-conflation that
banner warns against — **I did it twice**, in two consecutive commits, having
quoted the banner in the second one.

**Survives, unchanged** — every measurement; none depended on the premise:
- written `Q_A` is real-axis-only (gap 2.407 at `e^{i/3}`); #6875 stays withdrawn
- the block's projection is the modulus on `Δ(net)` and is partial — structural
- `Im[q²−q] = sinφ(2cosφ−1)`, zeros exactly `{0, π/3, π, 5π/3}`, no fifth
- the four degeneracies (`b²=0`, `h=0`, the double one at `q=1`) — structural,
  not reality-based

**What the ruling changes is their WEIGHT, not their truth.** Under the rejected
premise those four points were the entire admissible set, so excluding them
closed the locus. Under the ruling they are four excluded points out of a
continuum: the same measurement goes from decisive to nearly vacuous. That
inversion is the substantive consequence.

**Route 5's actual state:** the fibre locus `|q| = 1` is INTACT less four
degenerate points; nothing selects N there; #6755's `1/111` is neither selected
nor excluded.

**The open question, now cleanly separated from the archimedean one it was
entangled with:** if not reality, what constrains the fibre element? That needs
a *fibre-level structural* condition — Habiro-integrality, or an `H_n(q)`
representation-theoretic one — not an evaluation condition.

Nothing was wired at any stage. No `c_k` moved. Cost: three commits of analysis,
all of whose measurements remain reusable.

### Correcting my own hand-off, one message later: the fibre condition is NOT missing

I closed the retraction by saying the open question "needs a fibre-level
structural condition — Habiro-integrality, or an `H_n(q)` representation-
theoretic one." **The corpus already has it, stated for exactly this object.**
That is an over-claim of precisely the kind the corpus-grep checklist exists to
catch, made in the same message as a retraction. 1133 files mention Habiro.

`prop:habiro-precision-ladder-equivalence` (`mass-theory/`) states:

> the Markov trace `tr_M(T_w, q)` of any braid word admits a **finite** Habiro
> expansion with **integer** coefficients, and specifically
> `tr_M(β_n) − tr_M(β_p) = Σ_{m=0}^{M} a_m(u)·(u;u)_m` with `a_m ∈ Z[u]`,
> `M < ∞`

— the neutron–proton braid-word difference, i.e. the Q_β object itself. Its Lean
carries `habiro_terminates`, `habiro_integral`, `habiro_evaluation_determined`,
**1 sorry**, and — the part that matters — the bridge to the ladder is
`precision_ladder_is_habiro_taylor`, **conditional on the unproved class
`QbetaHabiroTaylorBridgeClass`** (§3b-cond). So the condition is stated and
partly formalized; what is open is the *bridge*, not the condition.

### A CANDIDATE this suggests — not a finding, and I have not tested it

Habiro integrality gives an N–truncation link for free, with no reality anywhere:
at a primitive N-th root of unity `ζ`, `(q;q)_m` **vanishes for `m ≥ N`**, so a
Habiro expansion evaluated at `ζ` truncates to `m ≤ N−1` automatically. That is a
fibre-level mechanism relating a root of unity to a truncation order — the exact
shape route 5's "what selects N" question wants, arriving structurally rather
than from an evaluation condition.

**The gap that stops this being a result:** the ladder's `N` (truncation order in
`u^k`) and the Habiro index `m` (Pochhammer degree) are **different indices**.
Identifying them is precisely what `QbetaHabiroTaylorBridgeClass` would have to
supply, and that class is unproved. So: promising shape, unproved bridge, and
anyone picking it up should start at that class rather than at the arithmetic.

Recorded as a candidate so the next reader inherits both the shape and the gap.
No compute run on it; nothing wired.

### Working `QbetaHabiroTaylorBridgeClass`: it is honestly open, and NOT a Lean target

Probe: `computations/qbeta/qbeta_habiro_bridge_class_is_not_a_lean_target_probe.py` (4/4).

**My hypothesis was wrong, and that is the first finding.** Both sides are
`opaque ... := fun _ => 0`, hence *semantically equal*; a leaky seal would make
the class trivially inhabited and every downstream conditional vacuous. I
expected a leak. Six tactics under `lean`-direct (`-DautoImplicit=false -s
65536`, real import cone; the file itself checks 0 errors):

    rfl / unfold / simp / decide / norm_num / aesop   -> 6/6 exit 1

So the 2026-09-04 `axiom` -> `opaque` conversion is **sound**: it dropped the
axiom-ledger entry without weakening the seal.

**But the class admits no deductive attack.** `precisionLadderCoeff` and
`habiroTaylorCoeff` carry **no defining properties** — nothing in the file or its
cone constrains either — so there is no premise from which `ck_eq_taylor` could
be derived. It is a **named hole**, not a hypothesis-carrying conditional. Its
companion `precision_ladder_is_habiro_taylor := h.ck_eq_taylor k` is the
self-assuming projection §3b-cond item 5 names (honestly labelled by its own
docstring — a labelling device, not a concealed claim).

**So "work the bridge class" resolves to: progress is COMPUTATIONAL, not
deductive** — one must first *define* the two sequences. And the corpus already
ran that computation: `qbeta-delta-tr-vs-formA` finds the leading Taylor orders
differ, `−2ε` vs `−5/4 ε`.

**Two things I checked rather than assumed:**

1. **That negative is unaffected by my #6889.** The test expands in `ε = q−1`
   on the **real axis**, where #6889 measured the simplified form's gap as 0 —
   and the witness does not even use the simplified form, recording
   `Abs((q²−1)(q(q−2)−1))/(2q³(q−1))`, the faithful `|Δ(net)|·E_0` #6889 says to
   use. Two independent reasons it stands.
2. **The negative's inference is sound**, which nobody had verified. "Leading
   orders differ ⇒ structurally distinct" would be weak if the series were
   merely *proportional*. Term-by-term `dtr/dnet` = `5/8, −1/8, 1/48, 5/112,
   17/256` — not constant, and it **changes sign at k=2**. A normalisation would
   have given a constant ratio.

**Scope (a).** Does not close the bridge and does not claim the `c_k` cannot be
the Habiro Taylor coefficients — only that the Form-A slot route is refuted and
the class as written admits no deductive attack. Nothing wired; no `c_k` moved.

### Dead end closed: rescaling z_D to bar-evenness LEAVES convention D (2026-09-06)

Probe: `computations/qbeta/qbeta_d_frame_bar_even_normalisation_deadend_probe.py` (5/5).

**The route.** Under D the eigenphase `2α = (z−1)h` is not bar-odd because `z_D`
is not bar-even. The obvious repair is to rescale. It exists and is **forced**:
`bar(q^a z_D)/(q^a z_D) = q^{−2a−4}` gives `a = −2` uniquely, so

    z̃_D := z_D/q² = q/(q²+1) = 1/[2]_q      (bar-even)

and it sits beside `z_C = √q/(q+1) = 1/[2]_√q` as **the same functional form in a
different variable** — the same shape as the `(u;u)_m` vs `(q;q)_m` defect fixed
in #6906. Numerically `z̃_D = 0.49729` vs `z_C = 0.49932` (0.4 % apart) where raw
`z_D = 0.61269` is 23 % away, which is why the C-built ladder nearly works under
`z̃_D`. **That closeness is not evidence and was not used.**

**Why it is closed.** `z_D`'s *defining* property here is the full-bar condition
`bar(z) = z − h` (`zD_full_bar_covariant`), and `barEven_fullBar_forces_classical`
proves bar-even and full-bar are incompatible away from `q² = 1`. Measured: `z̃_D`
misses full-bar by **exactly `h`** — and so does `z_C`. So rescaling does not
re-derive the ladder *within* D; it moves to a third parameter that is neither
`z_C` nor `z_D`.

**Worth recording separately:** the corpus states the bar law **additively**
(`bar(z_D) = z_D − h`); deriving it from scratch gives it **multiplicatively**
(`bar(z_D) = q^{−4} z_D`). These look like two constraints and are **one
identity** (difference exactly 0). A reader meeting both forms could reasonably
think two separate conditions apply.

**The live route is unchanged:** `eigenphase_bar_defect_of_fullBar` gives defect
exactly `h²`, **z-independent across the whole full-bar family**, so no choice
inside it restores bar-oddness — the derived D eigenphase is `α − h²/4`, no free
parameter. Independently reproduced here.

Scope (b). Closes one alternative; adjudicates nothing about the live route.

### The live D route, measured through the ladder: it improves, it does not restore (2026-09-06)

Probe: `computations/qbeta/qbeta_d_eigenphase_projection_through_ladder_probe.py` (4/4).

`eigenphase_bar_defect_of_fullBar` gives `bar(2α)+2α = h²` for any full-bar `z`,
so the bar-odd projection is `α − h²/4`, **derived, no free parameter**. Pushing
it through the ladder is therefore a derivation, not a search. Result at the
proton pin, `c_2` held at its structural `−1`:

    arm                     implied c_2      c_3        N1/N2
    C   (z_C)                 −1.0176     −2.069342     57.74
    D   naive (z_D)           −9.2989   −974.431888      1.12
    D   corrected (−h²/4)     −1.7331    −86.080994      2.36

**A large improvement and an insufficient one.** The right metric is
self-consistency — how far the anchor-inverted `c_2` sits from the *structural*
`c_2 = −1` — because it references no candidate value (`−2`, `Vol(4₁)`, …):

    C  1.8 %      D corrected  73 %      D naive  830 %

So the corrected D ladder is ~40× less self-consistent than C, with convergence
2.36× against C's 57.7×. **The eigenphase projection alone is not the whole of
the C→D move.**

Two things checked rather than assumed:

- **`c_2 = −1` is convention-INDEPENDENT** — it is `1 − (bℏ²)² = 1 − u²`, no `z`
  anywhere — so holding it fixed across all three arms is legitimate. The
  "implied `c_2` = −9.3 under D" recorded earlier is the *inverted* `c_2`, a
  different quantity.
- **The sign is derived, then corroborated, in that order.** `bar(2α)+2α = h²`
  forces `−h²/4`; the three candidates rank with the derived one first
  (`−h²/4` 2.364, `+h²/4` 1.070, `−h²/2` 0.882) and that agreement is recorded
  as corroboration only. Quoting it as the reason would invert the argument.

**Scope (a).** Does NOT refute the projection — it is proved. Measures only that
it is insufficient by itself, and identifies nothing about what else is needed.
Nothing wired; no `c_k` moved.

### C and D are DIFFERENT ALGEBRAS, z is a RANK label, and #6889's exclusion is withdrawn (2026-09-06)

Probe: `computations/qbeta/qbeta_c_vs_d_are_different_algebras_probe.py` (5/5).
Prompted by the owner asking whether the proper `z` coordinate was in use, and
to work the **full tower** rather than the semisimple part. Both pointed at a
framing error running through three of my PRs on this arc.

**1. Not a coordinate change — a change of algebra.** Registry:

    convention  name                                y_(3)      y_(2,1)    y_(1^3)
    C           full-Hecke Ocneanu / Wenzl z-trace  0.415396   0.280930   0.022745
    D           SU(2)/Temperley-Lieb (Jones)        [4]/[2]^3  1/[2]^2    0

Both normalise; **D annihilates the sign block**. `TL_n = H_n/⟨antisymmetriser⟩`
kills every >2-row partition, at `n=3` exactly `(1³)`. D is a **quotient** of C.
`z_D(q) = q²z_C(q²)` is true but relates parameter *values* only — no
substitution carries a 3-block trace to a 2-block one.

**2. `z` is indexed by RANK.** `z_N = q^N/[N]_q` satisfies full-bar
`bar(z) = z−h` for **every** N (checked 1–6, exactly zero), twist `q^{−2N}`.
`z_D = z_2` — **D is SU(2)**. `z_C = 1/[2]_√q` has no `q^N` numerator, is
bar-even, and is in the family for **no** N. The `q^N` numerator **is** the bar
twist — so #6915's rescale-to-bar-even was stripping the rank label.

**3. `b² = [3]_q/[2]_q²` exactly** ⟹ `b² = 0 ⟺ [3]_q = 0 ⟺ H₃(q) non-semisimple`.
The `π/3`, `5π/3` phases #6889 called "degenerate" are where
`tr = Σ_λ y_λ χ^λ` ceases to exist. **#6889's arithmetic stands; its emptiness
verdict is withdrawn as interpretation** — it excluded the interesting locus
because its own tooling stopped there. (First attempt `q²[3]/[2]²` was false;
sympy caught it.)

**4. Ruling tension, flagged not adjudicated.** 2026-08-15 makes D canonical;
2026-09-03 asks derivations to use the full tower. D = SU(2)/TL is a two-row
truncation discarding most of the tower at `n = 3A`. Which governs the Q_β
channel is an owner decision.

Measurements from #6915 and #6921 stand; their **framing** was wrong.

#### The truncation cost, as a number rather than an adjective

Probe: `computations/qbeta/qbeta_tl_truncation_cost_by_atom_probe.py` (4/4).

I called D's discarded part "the overwhelming majority of the tower". That is an
adjective, and not something to rule on. `dim TL_n = Catalan(n)` **exactly**
(verified by summing `(f^λ)²` over ≤2-row partitions, against `C(2n,n)/(n+1)`;
`Σ_λ (f^λ)² = n!` asserted first):

    n    A    dim H_n = n!              dim TL_n        retained
    3    1                  6                   5       83.3333 %
    6    2                720                 132       18.3333 %
    9    3            362,880               4,862        1.3398 %
    12   4        479,001,600             208,012        0.0434 %
    15   5  1,307,674,368,000           9,694,845        0.0007 %
    18   6  6.4e15                    477,638,700          ~0 %

**The cost is n-DEPENDENT, and the two rulings live at different n.** The Q_β
ladder is an `H_3` object: D discards one 1-dim block and keeps **83 %**, which
is why C-vs-D differs only in the 4th decimal on `β_Bor` (0.99836662 vs
0.99856216). The mass/binding work is at `n = 3A`: ⁴He retains **0.043 %**.

So "D canonical" (2026-08-15) and "full tower" (2026-09-03) may **both** be
right in their own domains, and the live question is where the crossover bites —
not which ruling wins globally. Measured, not adjudicated.

#### 🛑 CORPUS-GREP, BELATEDLY: most of the above is PRIOR ART

I did not run the six-path checklist before claiming the C-vs-D findings. Run
now, on owner instruction. **Two of the three headline claims are already in the
corpus, one of them Lean-proved:**

- **D kills the ≥3-row blocks** — `docs/audits/2026-08-10-convention-d-ylambda-root-and-derivation.md`
  (2026-08-10, a month old): *"Under convention D every `y_λ` with `ℓ(λ) ≥ 3`
  vanishes identically (**Schur–Weyl on a two-dimensional fibre**)"*. A better
  reason than my "TL quotient": Schur–Weyl on a 2-dim fibre.
- **`b² = [3]_q/[2]_q²`** — `prop:hoefsmit-binding-amplitude`, **Lean-proved**
  as `QOU.BraidsAndKnots.hoefsmit_b_sq_eq_q3_over_q2sq`.
- **The rank family and the TL stratification** — `qou-p-neq-np.md` §37: at
  `X = Q^{−N}` the surviving Wedderburn blocks are exactly `λ₁ ≤ N`, **proved
  sorry-free** in `WenzlSchurElement` (`tl_numerator_eq_zero_iff`,
  `schurElement_tl_eq_zero_iff`). That `N` is my `z_N = q^N/[N]_q`.

So #6924's algebra section is a **re-derivation**, not a discovery, and it says
so now. What survives as new: the **#6889 interpretation withdrawal**, the
**quantified truncation cost** (Catalan(n)/n! by atom), and the **D2 update**.

#### What was actually missing, and is now Lean-proved

The corpus had `b² = [3]_q/[2]_q²` AND the Wenzl/Schur-element semisimplicity
machinery — and **nothing linked them**. Four sorry-free lemmas added to
`hoefsmit-binding-amplitude.lean` (`lean` exit 0, 0 errors, 0 sorry, 0 axiom):

    hoefsmit_b_sq_eq_zero_iff          b² = 0  ↔  [3]_q = 0     (given [2]_q ≠ 0)
    qInt3_eq_zero_iff_cyclotomic       [3]_q = 0  ↔  q⁴+q²+1 = 0
    q_pow_six_eq_one_of_qInt3_eq_zero  [3]_q = 0  →  q⁶ = 1
    q_sq_ne_one_of_qInt3_eq_zero       [3]_q = 0  →  q² ≠ 1     (needs 3 ≠ 0)

So `b²` vanishes **exactly** at primitive 6th roots of unity. A probe finding
`b² = 0` has found a root of unity, not a defect — which is the Lean form of
#6889's withdrawal.

**Scope, stated in the file:** these are the ARITHMETIC half only. They do not
prove non-semisimplicity — that is the Schur-element criterion, carried
elsewhere in the corpus. They pin the vanishing locus.

**Literature: not consulted, and not needed for these four.** They are ring
identities over a field. The Schur–Weyl / Wenzl / Geck–Pfeiffer citations the
surrounding claims rest on are already carried by the corpus blocks above.


## 2026-09-07 — Lean tranche (PR #6965)

The corpus-grep that should have opened the earlier TL work found something
bigger than the missing witness, and it is now closed.

**Finding.** Two halves of the Lean tree quantify over TL survivors in opposite
conventions and nothing related them: `QBeta.TemperleyLiebTower` /
`QBeta.TwoRowNormalisation` use at most two ROWS, while
`MathlibExt.WenzlSchurElement` / `MassTheory.SelfConjugateStratumVanishes` use at
most two COLUMNS. The families are equinumerous but different sets, and their
squared-dimension totals agree at every `n` — so a proof transported by matching
totals rather than by transposing is wrong *without producing a wrong number*.
At `n = 6` the two families share nothing at all and both total `catalan 6 = 132`.

**Proved, sorry-free, general `n`** — `QOU/MassTheory/TwoRowTwoColumnCollision.lean`:
`transposeEquiv`, `card_transpose`, `atMostTwoCols_transpose` / `atMostTwoRows_transpose`,
`atMostTwoRows_iff_atMostTwoCols_false`, **`dimHLF_two_col_eq_two_row`**
(`dim λ = dim λ'` for this family), **`dimHLF_two_col_sq_sum`**.

**Stale status header corrected.** `QBeta/QDimNormalisation.lean` declared the
general-`n` normalisation open; it had been closed in `TwoRowNormalisation.levelSum_eq_one`
(bean `qou-f1qs`) under a different name. Cause is a naming split — one identity
called `levelSum` there and `qdim_normalisation` here, so a grep for either finds
neither the other nor the overlap. Added `qdim_normalisation_general` and
`ballot_cast` (the ℤ↔`R` `ballot` bridge that nothing had).

**Not closed, still open, and stated as such in both the Lean and the block:**
`H_n(q)/rad ≅ TL_n(q)` itself. A count of blocks and a count of dimensions are
not an isomorphism of algebras. Also `dim λ = dim λ'` for a *general* partition
(three-or-more rows AND columns) — Mathlib-shaped, no longer between the two
halves of this corpus.

Gap bean `qou-yhod` filed and closed the same session.


## 2026-09-07 — the isomorphism front (PR #6986)

#6965 merged. Continued onto `H_n(q)/rad ≅ TL_n(q)` itself.

**Landed, sorry-free, general index type** — `QOU/MathlibExt/HeckeToTemperleyLieb.lean`:
`heckeToTL : H_n(v²) →ₐ[R] TL_n(δ)` with `T_i ↦ v·e_i − 1`, and
`heckeToTL_surjective`. Twelve declarations, `#print axioms` clean on every one.

**Key facts worth keeping.**
- The two files' normalisations (Iwahori vs balanced) do NOT match under any
  shift `T_i ↦ a − e_i`: quadratic forces `δ = q+1`, braid forces `δ = q+q⁻¹`,
  equal only at `q = 1`. The fix is `v` as primitive datum with the *polynomial*
  hypothesis `v·δ = v²+1` — no inverse, no `Real.sqrt`, §7c-clean.
- In the braid check `Q` **cancels**: both sides are `−u_iu_j − u_ju_i + u_i + u_j − 1`.
  So no centrality hypothesis is needed, and the braid imposes nothing on `δ`
  beyond the loop relation.
- Use `•`, not `algebraMap _ * _`. `algebraMap v * e i * (algebraMap v * e j)`
  cannot be reassociated by `noncomm_ring` — the second scalar is trapped between
  generators; only centrality frees it. `smul_mul_smul_comm` does it in one rewrite.

**Still open, and NOT laundered into a class:**
1. *Mathematics* — `tlKernel = traceRadical tr_M`. `⊆` is a computation; `⊇` is
   semisimplicity of `TL_n(δ)`, the Wedderburn input the construction avoids.
2. *Engineering* — no first isomorphism theorem for NONCOMMUTATIVE rings in
   Mathlib. `Ideal` is `Submodule R R` (commutative); `TwoSidedIdeal` has `ker`
   but no quotient-equivalence. `RingCon` plumbing, deliberately not done badly.

**Build trap recorded.** `MathlibExt.IwahoriHeckeAlgebra` and
`MathlibExt.TemperleyLiebAlgebra` have no olean in `lake-cache/qou-v4-24-0` and
are not reachable from `QOU.lean` (the lakefile glob builds them; the aggregator
does not import them). Build lean-direct before verifying importers.


## 2026-09-07 (cont.) — the isomorphism is PROVED, presentation-level

`heckeTLEquiv` in `QOU/MathlibExt/HeckeToTemperleyLieb.lean`, sorry-free,
general index type:

    TL_n(δ)  ≅  H_n(v²) / ⟨ U_i U_j U_i − v²·U_i : i ~ j ⟩ ,   U_i = T_i + 1

**The engineering blocker recorded earlier was routed around, not waited on.**
Mathlib has no first isomorphism theorem for noncommutative rings (`Ideal` is
`Submodule R R`, the commutative notion; `TwoSidedIdeal` has `ker` and no
quotient-equiv). Quotienting by the NAMED RELATORS via `RingQuot` sidesteps it
and gives a *stronger* statement — the ideal is presented by generators rather
than merely named. `heckeQuotientEquivTL` was written against `Ideal`, failed
instance synthesis, and was removed rather than forced.

**`U_sq` is the load-bearing observation:** `U_i² = q·U_i + U_i` holds in `H`
ALREADY (Iwahori quadratic relation rearranged), so the adjacency relator is the
ONLY thing the quotient imposes.

**Still open, and now exactly one thing:**
`⟨U_i U_j U_i − v²·U_i⟩ = traceRadical tr_M`. `⊆` is a computation; `⊇` is
semisimplicity of `TL_n(δ)` — the Wedderburn input the construction avoids. That
is the whole remaining distance to `rem:hecke-radical-is-temperley-lieb`'s claim.

**Lean traps recorded.** `map_smul` fails instance synthesis on these `AlgHom`s
(use `Algebra.smul_def` then `map_mul`). `algebraMap v * e i * (algebraMap v * e j)`
cannot be reassociated by `noncomm_ring` — the second scalar is trapped between
generators; `smul_mul_smul_comm` in `•` form does it in one rewrite.

PR #6986.


## 2026-09-07 (cont.) — #6986 merged; Wedderburn-side infra in #7001

`traceRadical_eq_zero_of_algEquiv_pi_matrix` (sorry-free):
`A ≃ₐ Π Mat(d i) K` + `τ = Σ y_i·trace_i` + all `y_i ≠ 0` ⟹ `traceRadical τ = {0}`.
Plus `weightedBlockTrace_traceRadical_ne_zero` as a sharpness witness (the
hypothesis is load-bearing, not decorative).

Everything downstream of the Wedderburn decomposition is now closed. The
nonzero-weight input is ALREADY in the corpus (`yw_pos`). So the `⊇` half of
`⟨relators⟩ = traceRadical tr_M` reduces to the decomposition alone.

**Correction recorded.** I reported the matrix trace form as a Mathlib gap. It is
not: `Matrix.ext_iff_trace_mul_right` IS nondegeneracy, phrased as an
extensionality lemma, which is why a grep for "nondegenerate" misses it. Reusable
lesson: a Mathlib lemma may exist under the SHAPE it is used for rather than the
NAME it is known by. The weighted-product case IS genuinely absent.

**Mathlib has Wedderburn–Artin** (`RingTheory/SimpleModule/WedderburnArtin.lean`,
`exists_algEquiv_pi_matrix_divisionRing`). The gap is not the structure theorem —
it is proving `TL_n(δ)` SEMISIMPLE, which needs a cellular/diagram-basis
development Mathlib does not have.

### Scale of what is left (for whoever picks this up)

Three known routes to semisimplicity, all large:
1. **Cellular algebra** (Graham–Lehrer) — cell modules on two-row shapes, Gram
   determinants. Mathlib has NO cellular-algebra framework.
2. **Schur–Weyl / Jones–Wenzl** — TL acts faithfully on `V^⊗n`, image is the
   `U_q(sl2)` commutant. Needs the quantum group.
3. **Diagram basis + meander determinant** (DFGG) — the corpus already flagged
   this as gated behind the very isomorphism it would prove
   (`TemperleyLiebTower` §T4).

Route 3's *combinatorial* half is partly done here already:
`ballot_sq_sum_catalan`, `dimHLF_two_row_sq_sum`, `dimHLF_two_col_sq_sum`. What
is missing is the planar-diagram basis itself (`dim TL_n = Catalan n` as an
algebra fact, not a partition count).


## 2026-09-07 (cont.) — TL₂ is FREE of rank two (PR #7001, tranche 2)

`MathlibExt/TemperleyLiebAlgebra.lean` said twice, in its own words, that **no
upper bound on `TL₂(δ)` is proved anywhere in this file** and therefore
"freeness itself is not claimed". That is the structural gap: everything there
bounds TL from BELOW, so no dimension count or Wedderburn statement could even
be attempted.

Closed, sorry-free:
- `tl2_span_eq_top` — `TL₂(δ) = span_R {1, e₀}`
- `tl2Basis` — a `Module.Basis (Fin 2) R (TL₂ δ)`

⟹ `dim TL₂ = 2 = catalan 2`, the first `dim TL_n = catalan n` here proved as an
ALGEBRA fact rather than a partition count.

**The method generalises; the spanning SET does not.** `eq_top_of_one_mem_of_gen_mem_of_mul_mem`
(a submodule with 1, the generators, and closed under `*` is everything — via
`Submodule.toSubalgebra` + `adjoin_range_e_eq_top`) and `mul_mem_span_of_pairs`
(closure reduces to products of spanning elements, via `Submodule.span_mul_span`)
are both stated at general index type. What does not generalise is knowing WHAT
spans: general `n` needs the planar diagram basis.

**Both stale notes in `TemperleyLiebAlgebra.lean` updated**, not left to rot —
kept as written (each is correctly scoped to that file) with a pointer to the
complement. `≅ R × R` is still NOT claimed: the basis {1,e₀} ↦ {(1,1),(δ,0)} has
determinant `−δ`, so that map is an iso only when δ is a unit.

**Lean version trap:** `Basis` is `Module.Basis` in this Mathlib pin; a bare
`Basis` does not resolve.

### Next concrete step
`TL₃(δ) = span {1, e₀, e₁, e₀e₁, e₁e₀}` (5 = catalan 3). 25 product cases, each a
one-line consequence of `e_sq`/`e_adjacent`/`e_farCommute`; the two reduction
lemmas above are reused unchanged. Then the general-`n` diagram basis.


## 2026-09-07 (cont.) — TL₃ spanned by five (#7001, tranche 3)

`tl3_span_eq_top` — `TL₃(δ) = span_R {1, e₀, e₁, e₀e₁, e₁e₀}`, sorry-free ⟹
`dim TL₃(δ) ≤ 5 = catalan 3`.

n = 3 is where `e_i e_j e_i = e_i` first has content (n = 2 has no adjacent
pair). 25 products instead of 4. **The two reduction lemmas were reused
unchanged** — the payoff of stating them at general index type.

The six non-trivial products (A = e₀, B = e₁):
`A(BA)=A`, `B(AB)=B`, `(AB)(AB)=AB`, `(BA)(BA)=BA` (adjacency);
`(AB)(BA)=δA`, `(BA)(AB)=δB` (loop then adjacency).

🛑 **Freeness NOT claimed at n = 3, and the reason is structural**: the corpus's
`tl3Fam` representation lands in 2×2 matrices — a 4-dimensional target — so it
*cannot* witness linear independence of five elements however chosen.
`dim TL₃ = 5` needs a faithful rep of dimension ≥ 5, which does not exist here.
Recorded in the docstring with the dimension count so the gap is legible.

### Running state of the Wedderburn arc
- downstream of the decomposition: DONE (`traceRadical_eq_zero_of_algEquiv_pi_matrix`)
- `dim TL₂ = 2` exact (basis) — DONE
- `dim TL₃ ≤ 5` — DONE; the matching lower bound is open
- general `n`: needs the planar diagram basis — OPEN, and it is the real work
- semisimplicity of `TL_n(δ)`: OPEN, the deep input


## Lean tranche — TL₃ freeness closes (2026-09-07, PR #7001)

`dim TL₃(δ) = 5 = catalan 3`, exactly. `tl3Basis` / `tl3_finrank_eq_five` in
`QOU/MathlibExt/TemperleyLiebSpanning.lean`, sorry-free, all 34 branch
declarations `#print axioms`-clean.

**The bound that was called impossible.** Tranche 2 of this PR left a 🛑 on
`tl3_span_eq_top` saying freeness was not claimable at n = 3, because
`TemperleyLiebAlgebra`'s `tl3Rep` lands in 2×2 matrices and a 4-dimensional
target cannot separate five elements however it is chosen. **That obstruction
is real; the conclusion was too strong.** The fix is not a different 2×2
family but the SAME one summed with the trivial representation e_i ↦ 0 —
`tl3Rep5 : TL₃(δ) →ₐ[R] Matrix (Fin 2) (Fin 2) R × R`. Five dimensions is
exactly enough, and the argument then needs no linear system solved: reading
entries (1,1) → (0,1) → (1,0) → (0,0) kills each coefficient using only those
already known.

Recording it because the shape recurs: **a dimension-count obstruction bounds
the TARGET, not the METHOD.** The right move was to enlarge the target by the
one dimension the algebra already supplies, not to look for a cleverer family.

**Hypotheses, both load-bearing.** δ a unit (already needed by
`tl3Fam_adjacent`), and δ²−1 a non-zero-divisor — genuine, since δ = 1 really
does collapse M₀M₁ onto M₁M₀. Both hold at the substrate with room:
δ = q + q⁻¹ ≈ 2.01, δ²−1 ≈ 3.05.

**Still open, and it is the same object from both sides.** General n needs the
planar diagram basis — for the spanning set (upper) and because each lower
bound so far is a representation exhibited by hand at exactly the right
dimension. Semisimplicity of TL_n(δ), the input the whole arc is for, is
downstream of that. NOT closed.


## Wedderburn at n = 2 and n = 3 (2026-09-07, PR #7001, commit 63a6bb9741)

```
TL₂(δ) ≃ₐ[R] R × R                          (δ a unit)
TL₃(δ) ≃ₐ[R] Matrix (Fin 2) (Fin 2) R × R   (δ and δ²−1 units)
```

sorry-free, `QOU/MathlibExt/TemperleyLiebWedderburn.lean`, 22 declarations
axiom-clean. Consequence `tl3_traceRadical`: the weighted trace on TL₃(δ) has
**zero radical with no hypothesis standing in for semisimplicity** — the ⊇ half
of #6986's single open item, at n = 3.

**The arc's shape.** `TraceRadicalNondegenerate` proved everything downstream
of a Wedderburn decomposition as a theorem about whatever satisfies the
hypothesis; nothing was known to satisfy it. At n = 2, 3 something now does.

**Nothing new was constructed.** Both maps are representations already in the
corpus (`tl2Rep`; `tl3Rep5` from the freeness proof). What is new is that each
is BIJECTIVE — the basis images are independent (already the freeness content),
they span (the one new computation), so they are a basis, and a basis-to-basis
linear map is an isomorphism.

**The lesson worth keeping: injectivity and surjectivity are NOT symmetric over
a ring.** `tl3Basis` needs δ²−1 only as a non-zero-divisor. Surjectivity needs
it as a **unit** — an injective endomorphism of a free module of finite rank
need not be onto (×2 : ℤ → ℤ). The determinant of the five images is exactly
**(δ²−1)²**, so onto ⟺ δ²−1 invertible. Not a basis artefact: at δ = ±1 the
algebra degenerates.

**§7c for free.** The inverse is polynomial in c = δ⁻¹ and w = (δ²−1)⁻¹, both
carried as primitive data with polynomial hypotheses — no ℝ, no ordering, no
square root, no division. Substrate: δ = q + q⁻¹ ≈ 2.01, δ²−1 ≈ 3.05.

**Cross-check that was not designed in.** The 1 ⊕ 2 block shape matches
`TemperleyLiebTower.catalan_three`'s 1² + 2² = 5, reached from the
representation-theoretic side. Two tables became two theorems that agree.

**Method note.** The determinant and every `linear_combination` multiplier were
computed exactly (five rational δ, then a symbolic solve and an ideal
reduction) BEFORE any Lean was written. Multipliers derived, not guessed — the
first Lean attempt then went through.

**Still open, unchanged.** n = 2 and n = 3 are not n. TL_n(δ) is not proved
semisimple; the ideal equality is open for n ≥ 4. General n needs the planar
diagram basis, which this arc reaches from a new side each tranche. NOT closed.


## The diagram basis, measured before building it (2026-09-07, PR #7001, aae63bb6d8)

`computations/tl_normal_form_basis_probe.py` — formalize-first applied to a
Lean build: the wide search is the development, this is the prune. Exact
integers only; the witness carries zero float-valued fields.

**Settled.** The **Jones normal forms** — `(e_{i1}…e_{j1})(e_{i2}…e_{j2})…` with
`i₁<…<i_k`, `j₁<…<j_k`, `j_m ≤ i_m` — number exactly `catalan n` (n=1..8) and
map **bijectively onto all planar diagrams** (n=1..6), every one loop-free. Left
multiplication by a generator **closes** in them (n=2..7, 2574 products at n=7).
So the family to formalise is settled and is not in the corpus yet.

**🛑 THE FINDING THAT CHANGES THE DESIGN — and it is a negative.** Closure holds
and is **NOT length-monotone**: `Δ|word|` takes `+1`, `0` and **negative odd**
values, reaching **−5** by n = 7. **A 'rewrite until shorter' termination measure
does not exist**, and that is the first thing an agent reaches for. The proof
must carry the `(I, J)` index data and prove the multiplication rule on that —
a substantially different and larger design. Loop counts are always 0 or 1, so
δ-bookkeeping is one factor per generator, never a power.

**Two checker errors of mine, recorded because the class recurs.** My first
planar enumerator recursed on the *concatenation* of the two sides rather than
each side separately, counting `n!` not `catalan` — it printed `bijection=NO`
for n ≥ 3, a **false negative about the corpus produced entirely by the
checker**. The same script then printed `all bijections hold` while its own rows
said NO, because the flag tracked only collisions. A summary disagreeing with
the rows it summarises is worse than none.

**Gate posture.** `precision-gates.sh --changed` is RED and the RED is
**pre-existing corpus state, established not assumed**: this probe and its
witness appear nowhere in the gate output, and `witness_raw_float64_audit.py`
does not list the witness. Tree-measuring audit witnesses reverted per
`qou-v0t8` (twice — the second time because *running the ratchet to check*
rewrote one).

**Scope.** Finite n; proves nothing at general n. Wires to nothing. The general
theorem is NOT closed.


## Merged: Wedderburn at n=2,3 (PR #7001, main 6fadee41bb)

`TL₂(δ) ≅ R×R`, `TL₃(δ) ≅ M₂(R)×R`, `tl3_traceRadical` — the ⊇ half of #6986's
open item at n=3 with **nothing standing in for semisimplicity**. Verified by
content on main: 12 commits, both new files, all headline decls, 0 sorries.
Rebased 143→0 before merge; all six cone files rebuilt lean-direct exit 0; 56
declarations axiom-clean.

## Next tranche opened: the general index type (PR #7049)

`QOU/MathlibExt/TemperleyLiebNormalForm.lean`, 24 decls, axiom-clean.

**The design is dictated by the probe's negative, not chosen.** Because
`Δ|word|` reaches −5, a length-based induction cannot exist, so `NormalIdx m`
carries the **(I,J) data** and never a word.

**Two things measured before they went into Lean** — both would have cost a
rewrite otherwise:
- **Threshold counting ⟺ pointwise domination**, checked for every pair at
  m ≤ 7. It makes the type a subtype of a Fintype, so `card` is `decide`-able
  rather than needing a bijection argument.
- **`Finset.sort` does NOT reduce in the kernel** (merge sort), so every
  `decide` fails if it is used. `elems` filters `List.finRange`, already sorted.
  This is how the first draft failed — found by running it, not by foresight.

**Proved:** `card = catalan (m+1)` for m ≤ 4 (bridged to `Nat.catalan`); and
`range_elt_one` / `range_elt_two` — the general `elt` reproduces the proved TL₂
and TL₃ bases **exactly**. That pair is the whole reason to trust the
definition.

**🛑 NOT proved, nothing substitutes:** `card = catalan` at general m (needs a
Dyck-path or binary-tree bijection); `elt` spans at general m (the real content
of dim TL_n = catalan n — needs the closure lemma on (I,J)); `elt` injective at
general m. The two `span_range_elt_*` are proved by CITING the m = 1, 2 results
— consistency checks, not progress on the general case. NOT closed.


## 🟧 OWNER RULING 2026-09-07 — D7 = option 1, CHANNEL-SCOPED

Convention **D governs the decay / `Q_β` channel**; the **full tower governs
mass and binding**. Both prior rulings stand, each in its own domain
(2026-08-15 "D canonical" → decay; 2026-09-03 "full tower", settled as all `n`
AND all orders in `q` → mass/binding). "Canonical convention" is
**channel-local, not corpus-global**.

**What this does and does not change for this bean.** The `c_k` ladder is a
decay-channel object, so it **stays in D** — and its C-frame results still need
the re-derivation this bean tracks. The ruling does **not** license a `z_C →
z_D` substitution: `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` makes the
C-frame ladder and the mass channel's three-row forcing mutually exclusive, so
that move is invalid regardless of which convention is canonical.

**D2 is unblocked** — it could not be posed until D7 was settled.

**Implementation trap, and it is this bean's own finding:** label by the
PREDICATE (`colLen 0 ≤ 2` vs `rowLen 0 ≤ 2`), never by counting survivors. The
row and column families are equinumerous with **equal dimension sums** (at
`n = 3` both give 5 = catalan 3), so a count-based labelling is
transposition-blind and mislabels *without ever producing a wrong number*. Use
`transposeEquiv` in `QOU/MassTheory/TwoRowTwoColumnCollision.lean`.

Full ruling: `docs/coordination/2026-09-05-owner-gated-bean-triage.md` §D7.


## Merged: the δ half of the closure rule (PR #7096, main b7f0ba7902)

`computations/tl_closure_rule_probe.py` + `QOU/MathlibExt/TemperleyLiebClosure.lean`.

**Measured on 3456 products (n = 2..7), then PROVED.** The probe computes
`e_k · elt(I,J)` by planar diagrams, indexes BOTH sides by their (I,J) data, and
tests candidates — it does not guess.

```
loops = 1  ⟺  (I',J') = (I,J)        the δ is exactly at the fixed points
loops = 1  ⟺  k ∈ I  ∧  k-1 ∉ I      and that is the test — J never enters
```

Sharp: `k ∈ I` alone fails 650, `k ∈ I ∧ k+1 ∉ I` fails 882, `k ∈ I ∧ k ∉ J`
fails 846.

**Not a fit — the mechanism is Lean.** `e_comm_prod` (e_k commutes past a word
all far from k) and `e_mul_prod_eq_smul` (on `pre ++ k :: post` with pre far
from k, left mult returns the SAME word scaled by δ). `k ∈ I` puts k at a block
top; `k-1 ∉ I` forces every earlier block ≤ k-2 — exactly the hypothesis. The
`post` being untouched is why the form comes back UNCHANGED, matching the first
rule: the two halves cross-check each other.

**🛑 STILL OPEN, nothing substitutes.**
- **The instantiation** — deriving 'pre far from k' from `k ∈ I ∧ k-1 ∉ I` needs
  `NormalIdx.word`'s block decomposition. Next concrete step.
- **The loops=0 branch** — 2378 products, no candidate fits (`I' = I ∪ {k}`
  fails 1821, `I' ⊆ I ∪ {k}` 348, `J' ⊆ J ∪ {k}` 129). `|I'|-|I|` moves BOTH
  ways (302 / 1519 / 557) and **that decrease IS the word-length
  non-monotonicity** — so the rule cannot be insertion-shaped. The two negatives
  explain each other.
- Two invariants hold on all 3456 but are recorded, not proved: `k ∈ I'`,
  `|I'| = |J'|`.

Arc state: TL₂/TL₃ Wedderburn done (#7001); general index type done (#7049);
δ half of closure done (#7096). `dim TL_n = catalan n` NOT closed — it needs the
loops=0 rule and the general count (bicoloured-Motzkin bijection, which Mathlib
has nothing for).


## Closure-rule measurement arc (2026-09-07, PRs #7096–#7111, all merged)

**PROVED.** The δ half, end to end: `e_mul_elt_eq_smul` — `k ∈ I → (∀ j ∈ I,
j+1 ≠ k) → e_k · elt(I,J) = δ • elt(I,J)`. Measured on 3456 products, then
proved through `descRun_le` + `elems_sorted` (#7103) + `threshold_to_pointwise`
(#7105) + `word_split`/`e_mul_prod_eq_smul` (#7096, #7107).

**🛑 THREE NEGATIVES that close routes**, all measured on the same 3456:

1. **No natural measure is monotone** — 12 candidates, every one increases
   somewhere. The word-length negative was one row of a general pattern, not
   special. A rewriting induction of that shape **does not exist**.
2. **The image of e_k has exactly catalan(n−1) elements, for every k** — the
   tower relation dim(e_k·TL_n) = dim TL_{n−1}, in the combinatorics. This is
   the one POSITIVE lead.
3. **The tower map is not the naive index surgery** — dropping k and closing the
   gap is a bijection onto NF(n−1) **for k = 1 only**; it fails for every k ≥ 2.
   Caught after I printed one row and read it as general.

**STILL OPEN, nothing substitutes:** the (I',J') formula for the loops=0 branch
(2378 products, no candidate); the tower map itself; `card = catalan` at general
m (route: bicoloured Motzkin, absent from Mathlib); and therefore
`dim TL_n = catalan n` and the semisimplicity it feeds. NOT closed.

## 2026-09-08 — BASE SETTLED by owner ruling (qou-99qc): ε := tr_M at z_D. The D-frame ladder is to be re-derived on the z_D base (0.4447004 MeV, −43.157 %). Structural c₂ = −1 remains the self-consistency check; the blocker is still the N=1 phase (qou-pdix). No z-swap of the C ladder (decayLadder_zC_threeRow_ne_zero).



## 🛑 CORRECTION 2026-09-12 (from PR #7212) — the three net figures quoted here are at q = 111/100

This bean quotes, in its "no single 11-crossing element" item:

  build_nucleon_nf     ( 9 crossings)      net = -0.1883216147
  build_atom_nf_exact  (11, interleaved)   net = -0.2272041420
  nucleon_gen_chains   (11, gen-grouped)   net = -0.2332458961

All three match **q = 111/100** to every digit quoted; none matches the
substrate proton pin:

  model                                q=111/100        substrate proton
  build_nucleon_nf     ( 9 crossings)  -0.18832161472   -0.18829060147
  build_atom_nf_exact  (11, interl.)   -0.22720414203   -0.22715971177
  nucleon_gen_chains   (11, gen-grp)   -0.23324589607   -0.23319771132

q = 111/100 is `pyhecke.gram._H_FRAC`'s exactness device, **185 ppm** off the
substrate -- ~16000x the 11.54 ppb mu-p tension. Diagnosed 2026-09-04 in
`docs/audits/2026-09-04-delta-net-canon-and-crossing-count-analysis.md` §(ii)
and asserted in `qbeta_delta_candidate_census_probe`; the correction had not
reached this bean.

The item's CLAIM is unaffected -- there really are three mutually inconsistent
nucleon constructions, and the two 11-crossing ones really do differ only in
ORDER. Only the decimals were at the wrong q.

Cross-check that fixes them: the gen-grouped substrate value is the calibration
constant `qbeta_option_e_order_dof_range_probe` (merged) asserts at 1e-30,
-0.23319771131565870204...

Same correction appended to `qou-bg3w` and `qou-1qsw`, and applied to
`qbeta_d1_eleven_crossing_exclusion_probe`'s docstring (commit 4694165f19).

NOT closing or re-statusing this bean -- it is in-progress and belongs to
another agent's arc.

---

## 2026-09-13 — the N question's last branch closed, and the ω-grade written in

Three landings, plus a correction to the first of them.

**#7149 (`8f6771235f`)** reduced the route-5 `N` question to a trichotomy on
the arithmetic nature of `q₀`. Two branches closed; one survived — `q₀`
algebraic irrational, which by the pinning identity needs `Vol(4₁)` algebraic.

**#7263 (`f6f17fa092`)** closed it. `QOU/Archimedean/VolumeTranscendence.lean`
already carried `HyperbolicVolumeIndependence`, whose `no_relation` quantifies
over arbitrary finitely-supported `f : ℕ × ℕ × ℕ → ℚ`; restricted to the
`(i,0,0)` slice that is Mathlib's `transcendental_iff` verbatim. The file drew
only the *irrationality* rung and `Transcendental` appeared nowhere in it — but
`SingleVolumeIrrational` cannot touch the survivor, since an irrational may be
algebraic and the survivor is precisely the algebraic-irrational case.
`volTranscendental [HyperbolicVolumeIndependence] : Transcendental ℚ vol_4_1`,
lean-direct exit 0, axioms `[propext, Classical.choice, Quot.sound]`, no
`sorryAx`. **Not a proof of transcendence** — the class has no instance and
this adds none; the `[Instance]` binder is the §3b-tax dependency edge.

**#7289** writes the ω-grade into `conj:kashaev-surreal`, which was thorough
about what `st` *is* and silent on what it discards. At `N = ω` the leading
monomial of `δ_N := (2π/N)log⟨4₁⟩_N − Vol(4₁)` is `(log ω)/ω`, strictly between
grade −1 and grade 0. Both halves matter: `ord_ω(δ) = −1` coarsely (so
`st(δ) = 0` and the figure-eight discharge stands), **and** `δ` is not a
grade-(−1) monomial because `ω·δ` diverges. Three consequences, all written
down before measurement and all landing: `N·δ/log N → 3π` from below with the
derived offset (gap `0.0183 → 0.000295`, halving on each doubling); `N·δ`
divergent (`35.22 → 67.81`); `1/N` Richardson leaving `3π log 2 = 6.53275827`
(measured `6.53058` at N=800).

### 🛑 The correction, and it is mine

The #7263 probe and its witness `description` attributed the sub-leading
asymptotic to *"the cited Ohtsuki / Andersen–Hansen expansion"* and said it was
not re-derived here. **Written without running the corpus-grep.**
`prop:one-loop-prefactor-provenance` **derives** both `3^{-1/4}` and the power
`3/2` from the one-variable saddle at `θ* = 5π/6` (Lean
`c_pow_four_eq_third`), and says in its own words that the `4₁` calibration the
whole `c_σ` arc rested on is thereby retired. Near-miss worth recording:
`ohtsuki2016` in `references.ts` is about the **5₂** knot, not `4₁` — reaching
for it would have been a second wrong attribution in the act of fixing the
first.

#7289 corrects all seven sites in the probe and re-runs it: **every numeric
field is byte-identical**, only the attribution words move. What does *not*
change is that the `O(1/N²)` tail is **measured** (check 1), not derived — the
proposition states a leading asymptotic and records the step from its two
machine-checked analytic inputs to the saddle hypotheses as still assumed.

### What this does NOT do for `qou-cds1`

Nothing here touches the D-frame re-derivation of the `c_k` ladder, which is
this bean's subject and remains **open** (still blocked on the phase
`qou-pdix`). The `N` question was one branch of the route-5 sub-arc; closing it
conditionally on an instance-free conjecture class does not produce a `c_k`.



## 2026-09-14 — D2 AUTHORISED by the owner, and the authorisation is smaller than it looks

Owner, verbatim: *"work convention-D c_k re-derivation"*. Ledger ruling recorded
at `docs/coordination/2026-09-05-owner-gated-bean-triage.md`.

**Measured before starting it: four of the five rungs need no re-derivation.**
Full working, with numbers:
[`docs/audits/2026-09-13-d2-ck-tail-is-already-convention-d.md`](../docs/audits/2026-09-13-d2-ck-tail-is-already-convention-d.md).

AGENTS.md says *"treat every `c_k` conclusion … as C-conditional"*. The
companion half — *"the ladder must be RE-DERIVED under D, and that is not a
z-swap"* — is exactly right and proved
(`decayLadder_zC_threeRow_ne_zero`). **The first half is too strong for
`c₂…c₅`.**

Read at the definitions in `QBetaCategoricalPrecisionLadder.lean`, not the
docstrings: `N2…N5` are built from `hoefsmitB` and `hbarQ'` alone — **`z` does
not appear in any of them.** Only `N1_factor` reads `alpha q`. Two sorry-free
theorems on `main` make that structural rather than incidental:

* `Q_beta_categorical_ofPhase_tail_common` — the tail is **phase-independent**
  (proof: `unfold; ring`).
* `hoefsmitB_sq_eq_one_sub_stdWeightD` — **`b² = 1 − y_(2,1)^D`**, and the Lean's
  own docstring records the identity as **D-specific**: under C the `H₃(q)`
  weights carry `√q`, keep `y_(1³) ≠ 0`, and it fails.

Verified numerically at the proton pin, `mp.dps = 50`:
`b² = 1 − y_(2,1)^D` to **2.7e-51**; `ckTail = 0.999926215050140186`
(`N2 = 0.99992745671562`, `N3 = 0.99999876426366`, `N4 = 0.99999999403692`,
`N5 = 0.99999999994385`), against `z_C = 0.499320334184` and
`z_D = 0.612688037146`, neither of which enters it.

**So the D2 re-derivation is ONE PHASE, not five coefficients.** What is
genuinely C-conditional is the N=1 eigenphase `α` — the blocker `qou-pdix`
already isolates — and through it the ladder's overall value.

**Scope, explicitly.** Not a claim that the ladder's *value* is
convention-blind (it is not — `N1_factor` carries `alpha`, and a z-swap stays
invalid). Not a claim that the original 2026-05 *derivation* of `c₂…c₅` was free
of C-flavoured reasoning; what is established is about the objects the corpus
now carries. Not a derivation of `α`. Nothing wired, no number moved.

**Why this matters now:** as of `main` `8b367484ed`, `qou-pdix` has **all four
named attacks on `α` closed or forbidden** (A withdrawn by its own author, B
pruned then measured inert, C closed by PR #7340, D a fourth calibration). With
every route shut, the useful thing to know is what the blocker costs — and it
costs one rung, not five.

## 2026-09-14 — where the convention enters, measured (PR #7343)

Owner authorised D2 (*"work convention-D c_k re-derivation"*). Measuring the
scope first:

**The Markov convention reaches this ladder at exactly ONE place** — the N=1
eigenphase `alpha = (z-1)*h/2`. The tail factors N2..N5 never mention z. Two
independent surfaces agree:

- Python: `qbeta_utils.py:225` says so outright and guards it (`_WITHHELD =
  ("z","alpha")`, raises rather than hand out a convention unnamed).
- Lean (new, this PR): `N2_factor..N5_factor` are built from `hoefsmitB` and
  `hbarQ'` alone; `Q_beta_categorical_ofPhase_tail_common` proves the tail is
  phase-independent; `hoefsmitB_sq_eq_one_sub_stdWeightD` gives
  `b^2 = 1 - y_(2,1)^D`, so the tail's generator is structurally a D object.

**But that does NOT make four rungs convention-blind, and my first draft said it
did.** Every extracted c_k divides through Q_N1, so the single entry point
propagates to all five. AGENTS.md's "treat every c_k conclusion as
C-conditional" is correct as written; the draft's "too strong for c2..c5" is
withdrawn.

Already on main with a committed witness, and my corpus-grep missed it:
`qbeta_c3_ladder_trace_convention_sensitivity_probe.py` (2026-09-05, witness
2026-08-31, 10/10 PASS, proton, 60 dps):

    implied c2   -1.017623798 (C)  ->  -9.298862871 (D)
    c3 proton    -2.069342577 (C)  ->  -974.4318877 (D)
    dist to -Vol(4_1) under D: 972.402004534
    swing_D/swing_C = 1.00522   <- the ONE convention-immune pillar

Its own assertion names: implied_c2_is_minus1_in_C_frame_only,
h1_volume_proximity_does_not_survive_D_reextraction. Grep failure was on the
CLAIM SHAPE, not the topic.

**Net scope for this bean: one phase to derive, five values to re-extract.** The
ansatz survives as it stands; the numbers do not. Still blocked on qou-pdix
(alpha), where every named attack is now closed or forbidden.

Audit: docs/audits/2026-09-13-d2-convention-enters-at-one-rung.md

---

## 2026-09-14 — on the RULED base the ladder is excluded for EVERY phase, so α is not the blocker

Probe: [`qbeta_ladder_form_cannot_reach_ruled_base_probe.py`](computations/qbeta/qbeta_ladder_form_cannot_reach_ruled_base_probe.py)
— 5/5, proton pin, 50 dps. Scope **(b)** for the exclusion (proved invariant
cited); (a) for the numbers.

**`qou-cds1`'s last entry (2026-09-08) holds two halves that do not fit
together.** It adopts the ruled base and keeps the old blocker in one sentence:
*"eps := tr_M at z_D … the D-frame ladder is to be re-derived on the z_D base
(0.4447004 MeV, −43.157 %) … the blocker is still the N=1 phase (qou-pdix)."*

The ladder's correction factor is `F(α) = cos(α − u/2)·(1 − u²)·Π(1 + c_k u^k)`,
and what it must supply is `F_required = Q_codata/Q_base`:

| base | Q_base (MeV) | `F_required` | |
|---|---|---|---|
| `z = 1` (Form A) — **RETIRED** | 0.783645827375 | **0.998325241673** | < 1 |
| `z_D`, order-zero `E₀` — **RULED** | 0.444700408522 | **1.75923699418** | **> 1** |
| `z = q` (augmentation) | 0.87989056126 | **0.889125812282** | < 1 |
| dashboard scored cell — **RULED** | 0.65185631006 | **1.20016236389** | **> 1** |

**`cos ≤ 1`, so `F_N2(α) = cos(α − u/2)(1 − u²) ≤ 1 − u² = 0.99992745…` for
EVERY real α** — the supremum is attained at `α = u/2` and is still below 1.
Both ruled cells need more than 1. **No phase closes it**, derived or fitted.

**So deriving α cannot unblock this ladder on the base the bean adopted.** The
blocker line was correct for the retired cell — there `F_required = 0.9983 < 1`,
a small phase fits, and α is exactly the interesting unknown. It does not
survive the base change.

**Pushing the shortfall into the rungs instead is not a route either:** it needs
`c_2 ≈ 1.047e4` (z_D) or `2.760e3` (dashboard cell) against the structural
`c_2 = −1` — four orders, wrong sign. The `1/u² = 13784.87` magnifier is why,
which is this bean's own finding about `c_k` being the wrong coordinate.

### Calibration, run before anything was concluded

The probe first reproduces **this bean's own F-table** on the retired base —
**−0.0762164 / −35.9111 / −3.17063 %** against the recorded −0.076 / −35.9 /
−3.17 — so the machinery is the bean's, not a re-invention.

### A coordinate trap this exposes

That table reports relative deviation of **`1 − F`**, not of `F`. On the retired
base both are small and positive and the ratio is informative. On a ruled base
`1 − F_required = −0.7592` is **negative** while the model's `1 − F_N2 = +0.0016`
stays positive, so the same ratio returns −100.21 % — opposite-signed
quantities, meaningless rather than merely large. **Report `F` directly on a
ruled base;** the reldev table is retired-base-only.

### What this does NOT say

It does **not** retire α: `qou-pdix` stays open on its own terms, α is still the
N=1 phase, and this says only that α is not what stands between the ladder and
the ruled base. It does **not** refute the ladder or the forced bar-odd
projection `a_odd = a − h²/4` — both C-frame, sorry-free, untouched. And it does
**not** choose a base: `F_required < 1` on the retired cell is **not** a reason
to prefer it (§NO FITTING — a base is never chosen by which obstruction it
removes).

### What it changes about the next step

The open question is no longer "what is α" but **what object supplies a factor
above 1 at all** — the ladder's multiplicative form cannot, whatever its phase.
That is a question about the *base or the assembly*, not about the phase.

**Addendum, same probe (now 7/7): "a higher rung saves it" does not work.**
Check 3 bounds only the N=2 truncation, so the natural objection is that a later
rung could lift `F` above 1. It cannot — **every `c_k` this corpus records or
derives is negative**:

| | value | `(1 + c_k u^k)` |
|---|---|---|
| `c_2` structural | −1 | 0.999927456715617626 |
| `c_3` recorded (proton) | −2.0693425728 | 0.999998721419095324 |
| `c_5` derived `−(b²+½)` | −1.25270211325 | 0.999999999943851153 |
| product | | **0.999926178171320707 < 1** |

So each factor is below 1, the product is below 1, and with `cos ≤ 1` the whole
`F` is **strictly below 1 at every truncation order**. Reaching `F > 1` needs a
**positive** coefficient and none of the derived ones is.

**The target, stated so its size is on the record — and explicitly not a search
specification.** At the order-zero `E₀` the ruled functional gives
`|ε| = 0.106235639848`; reproducing CODATA needs `0.186893667722`, a factor
**1.759236994**. Per §NO FITTING a target may be checked **against**, never
searched **on** — do not hunt for an element whose Markov trace lands there. The
dashboard's own scored element already fails the confinement-SDP selection rule
(owner ruling 2026-09-13), so the assembly is under review independently.

---

## 2026-09-14 (2) — the route-5 obstruction that shaped this arc is base-conditional

Companion to the entry above, and it changes what "blocked on `qou-pdix`" means.

The entry above established that the ladder's factor cannot reach the ruled base
for **any** phase (`cos ≤ 1`, so `F ≤ 1 − u² = 0.99992745` against `F_required`
of 1.7594 / 1.2002). The natural next question — *what supplies a factor above 1*
— turns out to be answered by route 5's own machinery, in the branch route 5
currently treats as excluded.

`correction_below_one_excludes_real_spectrum` (step 18, sorry-free) carries the
hypothesis `(hκ : κ < 1)`. Measured at 50 dps on the proton pin
(`qbeta_ruled_base_inverts_the_route5_obstruction_probe`, 6/6): `κ = 0.998398` on
the **retired** `z = 1` cell — reproducing step 18's own quoted `0.998399` — and
`κ = 1.759365` / `1.200249` on the two **ruled** cells. The exclusion does not
fire on either.

**Consequence for this bean.** Two sorry-free inequalities on a base needing
`κ > 1` — `cosh ≥ 1` and `|cos| ≤ 1` — exclude the **elliptic** generator and
leave the **hyperbolic** one, which the substrate's Kohno–Drinfeld generator
already is at real `q₀` (`det A = −(ln q)² < 0`). The `det A > 0` / `|q| = 1` /
Kashaev-locus / `N = 111` narrowing was derived from the retired requirement.

The Lean stands; only its premise moved. Nothing here derives `c_k` or `α`, and
nothing selects a base — per NO FITTING, an exclusion lapsing is not a reason to
prefer the base it lapses on.

**This bean stays blocked and open**, but the blocker is better described: not
*"derive α"* (which the entry above shows cannot close it) and not *"find an
elliptic construction"* (which this entry shows was never required on the ruled
base), but the **quantitative** gap between the hyperbolic character available at
`q₀` (`1.00544843`) and the one required (`1.75936462`) — 11.17× in the generator
eigenvalue, 139.37× in the character excess. Rule 13a.
## 2026-09-14 — the phase is NOT what blocks this bean, and AGENTS.md said it was

Recorded here because `qou-cds1`'s previous entry is 2026-09-08 and predates the
result. **Status stays `in-progress`; nothing is closed** (§13a — the subject is
open).

**The claim.** "Blocked on the phase `qou-pdix`" is correct only for the
**retired `z = 1` cell**. It did not survive the 2026-09-08 ruling that made
`z_D` the base, and nothing re-checked it then.

**The evidence.** The ladder's N=2 factor is `F_N2(α) = cos(α − u/2)·(1 − u²)`,
so `cos ≤ 1` caps it at `1 − u² = 0.99992745` for **every real α** (supremum at
`α = u/2`, still below 1). What it must supply is `F_required = Q_codata /
Q_base`, recomputed at 70 dps:

| base | `Q_base` (MeV) | `F_required` | vs cap |
|---|---|---|---|
| `z = 1` (Form A) — RETIRED | 0.783645827375 | 0.998325241673 | reachable |
| `z_D`, order-zero `E₀` — RULED | 0.444700408522 | **1.75923699418** | **excluded** |
| `z = q` (augmentation) | 0.87989056126 | 0.889125812282 | reachable |
| dashboard scored cell — RULED | 0.65185631006 | **1.20016236389** | **excluded** |

**The two cells a cosine can reach are exactly the two the ruling does not
select.** Inverting the cap gives `u = 0.008517628778` against AGENTS.md's
`u ≈ 0.00852` — consistent.

**The implication.** No value of α unblocks this bean on the ruled base. The
live question is **what object supplies a factor above 1 at all** — about the
base or the assembly, not the phase. An agent sent to derive α as *the* `Q_β` L2
blocker is working off the critical path.

**Provenance.** Established twice, independently and sorry-free, in PR #7355
(`LadderFactorBound.lean`, 4 lemmas, 7/7 probe) and PR #7262
(`EigenphaseQuantization.lean`, 19/19, base-independent table) — **both still
open**. Verified rather than taken on trust, and **merged**, in
`docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md` §5.1
(PR #7276, merged as `f3cb908ee7`), which recomputed all four `F_required` at
70 dps and inspected the Lean for `sorry`. **Cite the merged audit, not the two
PRs**, when checking this.

**AGENTS.md fixed in the same PR** — both "blocked on the phase `qou-pdix`"
sites now point at a scoping note carrying the table above. That edit is
exemption 2 under §ASK THE OWNER (derived from a corpus artifact — the merged
audit), not agent judgement.

── 2026-09-15 — the search over z is CLOSED, negatively ──────────────────

Probe: `computations/qbeta/qbeta_ruled_base_affine_solve_probe.py`, 2/2.
Status unchanged: this closes a line of enquiry, it does not unblock the bean.

**What was already settled.** `qbeta_ladder_form_cannot_reach_ruled_base_probe`
bounds the ladder factor `F(alpha) <= 1 - u^2 < 1` for every real alpha, and the
merged 2026-09-13 audit §5.1 adds that the rungs cannot help either — every
recorded `c_k` is negative, so each shrinks `F` monotonically. So the FORM is
bounded by 1 and `Q_pred = Q_base * F <= Q_base`.

**What was not computed: whether any z reaches CODATA at all.** Both prior
results test the two admissible roots. The base is AFFINE in z —

    tr_M(Delta_S)(z) = A + B z,  A = q^2/2 - 1 + 1/(2q^2),  B = 1/q - q < 0
    Q_beta(z)        = |tr_M(Delta_S)(z)| * E_0,   E_0 = m_e/(q(q-1))

— so the family inverts in closed form. A monotone affine map has exactly one
preimage, so this reports THE z, not a best one: **no fit is involved and none
is possible.**

Rebuilt from `q_0` alone and calibrated against the audit's three published
cells before inverting anything:

    z_D (RULED)          Q = 0.444700408522 MeV   published 0.444700408522   rel 4.9e-13
    z=q (augmentation)   Q = 0.87989056126        published 0.87989056126    rel 1.4e-13
    z=1 (retired)        Q = 0.783645827375       published 0.783645827375   rel 4.8e-13

    z REQUIRED for CODATA = 0.99850030441113
       to z_D 0.385812     to q 0.111478     to the excluded z=1 0.0014997
       an admissible convention-D root?  NO

**The reading.** The ruled base's shortfall is not a missing factor, not a
phase, and not a rung. Within this assembly it would have to be a different z,
and the only z that works is inadmissible — it sits 0.15 % below the excluded
coordinate sum, which is exactly why that retired cell so nearly worked
(`F_required` 0.9983). So the live question the audit states — *what object
supplies a factor above 1* — has a sharper answer on this assembly: **nothing
can, because the shortfall is not multiplicative.** Any route to CODATA under D
must change the ELEMENT or the FUNCTIONAL, not the parameter.

**Not proposed.** `z = 0.9985` is reported as the inadmissible preimage, not as
a candidate. Adopting it is the forbidden return to the coordinate sum
(`ConventionDAdmissibleRoots.one_not_root`), the same trap
`qbeta_d_frame_admissible_base_correction_search_probe` diagnoses for the
augmentation base. Nothing here touches the C-frame ladder results.

**Checked before writing:** no existing probe inverts the family —
`qbeta_zd_gap_anatomy_probe` decomposes the gap and
`qbeta_cds1_terminus_status_probe` recomputes the load-bearing numbers, neither
solves for z.


## 2026-09-14 (session gifted-feynman, 3) — the ladder exclusion no longer depends on the SIGNS, so a re-derivation here cannot void it

**The fragility this closes.** `LadderFactorBound.ladder_lt_of_rungs` (#7355,
sorry-free) is the corpus's whole-product exclusion, and its hypothesis is
`∀ x ∈ l, 0 < x ∧ x ≤ 1` — i.e. **every `c_k` negative**. That file is honest
about it ("`P` is a *hypothesis*, not a claim about the rungs, and the numeric
fact that this corpus's rungs satisfy it is measured in the probe"). But **this
bean is the open task of re-deriving those very coefficients**, and a
re-derivation producing one positive `c_k` voids that theorem outright — the
hypothesis fails and it says nothing at all. An agent reading only that file
would then be entitled to conclude the exclusion had lifted.

**The sign-blind replacement**, `QOU.QBeta.LadderUniformBound` (7 declarations,
sorry-free, `lean`-direct exit 0 with `-DautoImplicit=false -s 65536`,
`#print axioms` on all 7 = `[propext, Classical.choice, Quot.sound]`):

    ∑ |c_k u^k| ≤ S < 1   ⟹   ∏ (1 + c_k u^k) · (1 − S) ≤ 1

proved by induction, division-free, nothing past `nlinarith`; composed with the
`cos ≤ 1` cap as `ladder_lt_of_sum_bound`, and `sum_abs_le_of_scaled` reduces
the hypothesis to **one scalar `C`**.

**The numbers** (`qbeta_ladder_uniform_coefficient_bound_probe.py`, 9/9):

| quantity | value |
|---|---|
| `u` (proton pin) | 0.0085172345501561421893 |
| `G = ∑_{k≥2} u^k = u²/(1−u)` | 7.31664602858e-5 |
| `C_min`, LIVE SCORED cell | **2279.45973262** |
| `C_min / largest live \|c_k\|` (= \|c₃\| = 2.0693425728) | **1101.54×** |
| `C_min / largest EVER held` (superseded `c₅ = +12.8676`) | **177.15×** |
| ladder cap at a gratuitous `C = 100` | 1.00737 vs required 1.20016 |

So the exclusion survives not merely a sign flip but an order-of-magnitude
coefficient blow-up. **A re-derivation under D overturns the base-not-rungs
conclusion only by producing a coefficient above ~2279** — a single scalar,
checkable the moment this bean's work lands.

**THE CONCLUSION IS NOT NEW AND MUST NOT BE REPORTED AS SUCH.** That the `Q_β`
L2 residual is a base/assembly problem is already the corpus's position in at
least five places — the merged adjudication
`docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md` ("the live
open question is not *what is α* but *what object supplies a factor above 1 at
all*"), this bean, `qou-pdix`,
`qbeta_eigenphase_rationality_quantization_probe.py`, and that probe's witness.
Every one of them rests on `cos ≤ 1` plus the **measured sign**. None argues
from magnitude. Nothing here establishes the conclusion; it replaces a fragile
premise so the conclusion stays standing through this bean's work.

**Mathlib already had half of it, and the corpus-grep is what found that.**
`Finset.norm_prod_one_add_sub_one_le` bounds `‖∏(1+fᵢ) − 1‖ ≤ exp(∑‖fᵢ‖) − 1`
over any `NormedCommRing` with **no hypotheses at all**, so the induction is a
re-derivation rather than a necessity. Both are kept, and the difference is
stated rather than glossed: Mathlib's is the **tighter** product bound
(`1/(1−S) ≥ exp S` on `[0,1)`), which is why the **Weierstrass** `C_min`
(2279.46) is quoted over the exp route's (2493.73) — a weaker product bound is
easier to beat, so it concedes more to the thing being excluded, the honest
direction for a refutation. Mathlib's carries no `S < 1` hypothesis and so
survives a blow-up that makes the induction vacuous.
`ladder_lt_of_sum_bound_exp` is that second, independent route; assertion 9
records that the two bracket the requirement.

**Scope, deliberately narrow.** Proves the **implication** only. Does NOT prove
a re-derived convention-D ladder's coefficients **are** bounded by any `C` —
that is a hypothesis and this bean has not run. Exhibits no missing factor.
Says nothing about the cosh route, which Part 4 of the sibling probe re-opened
on the ruled base (the 2026-08-22 exclusion was computed on the retired `z = 1`
cell and is void). Nothing selected, nothing re-scored.

**Two process notes worth more than the result.** The cells are **read from the
sibling witness, not hardcoded**: the first draft hardcoded four cells from
AGENTS.md prose and the witness carries **five** — the bar-odd parity-forced
survivor (`F = 2.2136`, `C_min = 7493`) was simply absent — and the prose's
live-cell factor differs from the computed one at the 8th digit. For the same
reason assertion 4 keys on the **property** (`F > 1`) rather than on a curated
list of ruled cells, which had already drifted. A hand-kept list narrows a
claim without saying so.


## 🛑 Citation correction 2026-09-26 (bean `qou-6moa`) — the reading is unaffected

This bean cites `markovWeights_eq_jones_of_threeRow_eq_zero` for the claim that
under convention D the three-row weight vanishes. **That lemma proves the
converse.** Read its signature (`BraidsAndKnots/MarkovTraceTLUniqueness.lean:119`):
`hTL : y₁₃ = 0` is a **hypothesis** and `z * (q + qi) = q ^ 2` — convention D — is
the **conclusion**. So it gives TL ⟹ D, which is the direction
`docs/coordination/trace-convention-registry.json:173` correctly cites it for.

It also carries `hfaith : y₂₁ ≠ 0`, and that is load-bearing rather than
decorative: the sibling `markovWeights_degenerate_root` (`:154`) proves that
dropping it makes the conclusion **false**, not merely unprovable — the trivial
character `y = (1,0,0)` at `z = q` satisfies all three moment equations and gives
`q·(q+qi) = q² + 1 ≠ q²`. A lemma that *assumes* a form of faithfulness on the
two-row block cannot be evidence about the three-row block vanishing.

**Cite instead**, matching the frame:

| lemma | typeclass | scope |
|---|---|---|
| `QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows` (`:142`) | `[Field R]`, sole hypothesis `q²+1 ≠ 0` | general `n`, on the actual Ocneanu weight |
| `QOU.BraidsAndKnots.FibreDimensionForcesTL.threeRow_eq_zero_of_jones_ocneanu` (`:179`) | `[CommRing R] [IsDomain R]`, division-free | `n = 3`, same variable frame |
| `QOU.QBeta.TemperleyLiebTower.conventionD_kills_antisymmetriser` (`:368`) | `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` — **an ordered field** | `n = 3`, archimedean only |

The third is the wrong citation at any §7c generic-`R` site.

**Nothing in this bean's conclusions changes** — only the authority cited for one
step. Measured: the reversal is a class of 14 across 9 files against 49 correct
citations, and 3 further files carry the same assertion with no lemma named at
all, so a grep on the identifier cannot find them. Full per-site table and blast
radius on `qou-6moa`; fixed so far in AGENTS.md and
`QOU/Mass/AltCharShiftMultiset.lean` (PR #7459).


## 2026-10-10 — item moved here from `qou-54g5` (epic `qou-d8c7`, issue litlfred/qou#7547)

`qou-54g5` is completed today: the ladder headline it questioned was settled on 2026-08-31 (sign positive, `+0.0071` ppm) and its 2026-09-13 entries confirm the witness carries the live `7.133937` ppb. One thing it left open belongs with this re-derivation: **the cause of the 7.133 ppb epoch offset** between the published-epoch column and the recomputed N=3 row (`qou-54g5` lines ~386-430, marked there "NOT FITTED: the cause ... is not identified"). It is not identified here either.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** c_k u^k\

Evidence: No D-frame c_k ladder exists. `qbeta_ck_cache.py` refuses on D (exit 2, re-run). On the ruled base the ladder form is excluded for every α (`qbeta_ladder_form_cannot_reach_ruled_base_probe.py` re-run: exit 0, 8/8, F_required 1.75923699418 / 1.20016236389 vs cap 0.99992745). It is also excluded for any rungs with Σ\

Status: `in-progress` → `in-progress` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.


## 2026-10-10 — the convention-D ladder, expanded exactly from its definitions (owner: "Do c_k under convention D", option 1)

Derivation from `QBetaCategoricalPrecisionLadder.lean`'s definitions with sympy, plus a numeric check at the proton pin (`q_at(50)`, 50 dps). **No data enters except the final comparison against the ruled-base requirement, which is a CHECK and not a search target. Nothing is wired and no number moved.**

**1. Bar parity, exact (sympy `simplify` → 0).**
- `bar(z_D) = z_D − h = q⁻⁴·z_D`.
- `bar(2α_D) + 2α_D = h²`.
- `a_odd := α_D − h²/4` is exactly bar-odd.
- `b` is bar-even; `z_C` and `α_C` are bar-even and bar-odd respectively.

**2. In the h-frame the forced projection is just the odd part.**
- `q ↦ 1/q` sends `h ↦ −h`, and the whole even part of `α_D` is `h²/4`, exactly.
- So `a_odd` is the odd part of `α_D` in `h` (`qou-cwin`'s authorised frame):
  - `α_C(h)        = −h/4 −  h³/128 + 7h⁵/8192  − 33h⁷/262144 + …`
  - `α_D(h)        = −h/4 + h²/4 + 3h³/32 − 5h⁵/512 + 7h⁷/4096 − …`
  - `a_odd^D(h)    = −h/4 + 3h³/32 − 5h⁵/512 + 7h⁷/4096 − …`
- **C and D agree at O(h) and first differ at O(h³):** `−1/128` against `+12/128`, a difference of `13h³/128`.

**3. The rungs `c₂…c₅` are unchanged under D, because they are z-free.**
- The tail `N2…N5` contains no `z` (checked symbolically).
- Its rungs are, exactly:
  - `c₂ = −1`
  - `c₃ = −2`
  - `c₄ = −2(q⁴+q²+1)²/(q²+1)⁴ = −1.13312094258…`
  - `c₅ = −(3q⁴+4q²+3)/(2(q²+1)²) = −1.25270211325…`
- **"Re-deriving c_k under D" therefore has nothing to re-derive at k ≥ 2.** The only convention-D object is the N=1 phase.
- This is consistent with the 2026-09-14 entry: "one phase to derive, five values to re-extract". The re-extracted values are artefacts of inverting the single data scalar through N1.

**4. The uniform-bound gate passes, so the ruled-base exclusion STANDS for this ladder.**
- `max|c_k| = 2 ≪ C_min = 2279.46` (`LadderUniformBound`).

| N=1 phase | α(q₀) | F(q₀) |
|---|---|---|
| C (`α_C`) | −0.0523361203 | 0.9983252784 |
| D z-swap (`α_D`) | −0.0404857773 | 0.9989254255 |
| D bar-odd (`a_odd`) | −0.0514123295 | 0.9983771024 |
| cap `1 − u²` | | 0.9999274567 |

- `F_required` on the ruled `z_D` base is 1.75924, so every row misses by about 76%.
- The tail is `0.99992621505014018…`, reproducing the 2026-09-14 entry.

**Scope.**
- This derives the ladder *as the corpus defines it*. It does not derive the ladder's ansatz, and it does not derive α: `a_odd` is forced by parity, not by mechanism.
- It does not touch `qou-pdix`.
- The open question remains the one recorded on 2026-09-14: **what element or functional supplies a factor above 1 on the ruled base.** Owner, 2026-10-10: work that next.

Script: `ck_D_exact.py` (sympy and mpmath; sections 1–2 exact, section 4 at 50 dps).


## 2026-10-10 (2) — what supplies a factor above 1 on the ruled base: nothing admissible, with one ruling question open

Owner, 2026-10-10: *"Find what element or functional supplies a factor above 1 on the ruled base."*

The candidates were pre-registered at 07:46Z, before any value was computed at q₀: 19 rows, each with its structural source, why it is admissible, and a gate. Results: **0 SUPPLIES · 11 FAILS · 6 INADMISSIBLE · 1 INDETERMINATE.** Every inadmissible row also failed its own gate on value, so admissibility decided nothing on its own. All numbers are at 60 dps, after 7 calibrations against corpus witnesses. 1.75924 was used only as a check, never as a search target.

**Functional side — closed by an exact identity, for every q.**
- `χ_(2,1)(Δ_S) = 0`. Proof: σᵢ has trace `h` in the (2,1) irrep, so `2·(h²/2) − (h/2)(h+h) = 0`. Verified independently.
- Under D, `y_(1³) = 0`. So **every** trace of `Δ_S` is `a_(3)·χ_(3)(Δ_S)`, Markov or not.
- The two admissible Wenzl levels fix `a_(3)` at:
  - `y_(3) = [4]_q/[2]_q³ = (q⁴+1)/(q²+1)² = 0.5054` at `z_D` (ruled), or
  - `1` at `z = q` (augmentation).
- CODATA needs `0.8891`, strictly between them, which is the non-integer level 1.1258.
- So the functional choice is a single bit, and the ruling takes the value further from CODATA.
- Projections, adding or removing the trace-invisible part, conjugation and bar-symmetrisation all give exactly 1. `Δ_S` is already exactly bar-odd at `z_D`.
- `[2]_q²` and `[2]_q³` quantum-trace rescalings (4.04, 8.13) and the augmentation (1.979) are inadmissible, and they overshoot anyway.

**Element side — a factor above 1 exists, but not 1.759 under the literal rulings.** These figures are the research agent's numerics and have not been re-derived here.
- The most ruling-compliant family is the γγ core `(σ₀σ₁⁻¹)³` with quark letters, no gluon letters, and the reading-3 test passed on the whole word.
- It gives `F = 1.147–1.349` across the four combinations the unresolved 2-fold degeneracy leaves.
- With the tower-summed `E₀` the best is 1.362, about 23% short: `Q_β ≤ 0.606 MeV` against 0.78233.

**OPEN — owner ruling, recorded undecided 2026-10-10.** Does the 2026-08-30 single-wrap ruling's *"no gluon"* exclude the gluon letters of the γγ nucleon words?
- **If yes:** the ruled base is closed negatively for the corpus alphabet, capped at 1.362.
- **If no:** the family straddles the target. In a POST-HOC check, only the live 2-letter gluon budget straddles (0.12–2.29), and nothing selects a word. The next item is then the energy / O'Hara selection principle proposed on 2026-09-14 (`qou-99qc`). Only that principle may pick a word, never closeness to 1.759.

**Follow-ups this surfaced.**
- A small Lean target: `χ_(2,1)(Δ_S) = 0`, and hence "the admissible functionals on `Δ_S` are exactly `{y_(3), 1}·χ_(3)(Δ_S)`".
- An engine fragility: at 2 gluon letters, 16 words sit exactly on the reading-3 boundary (`χ_(2,1) = 0`). The corpus counts of 149 and 145 are right only because round-off falls at `+4e-51`; a fresh engine counted 146 and 142. The comparison needs an explicit tolerance.
- The 30 routes the corpus had already closed are listed with their evidence in the research notes and were not re-run.


## 2026-10-10 — two of this bean's cited supports are red (cross-cluster check, verification sweep of `qou-avtq`)

- **Step 27** cites `qbeta_level_k_binding_operator_probe.py` as "(8/8)" for "the level-k operator IS binding". A re-run today gives **6/8**, exit 1, failing `binding_character_is_largest_in_a_tl_kernel_block` and `the_only_small_eigenphases_are_in_blind_blocks`. Both headline findings of Step 27 are red. `qou-g5oz` (parent `qou-9nnz`) tracks the probe.
- **The swing-gate cancellation and α(q0):** `qbeta-c3-swing-gate.witness.json` fails `swing_matches_o2` (3.4e-4 against tol 1e-6) and carries no q0Anchor. `qbeta-symbolic-chain-alpha-b.witness.json` fails `alpha_q0_matches_probe_n3_witness` (0.01185 against tol 1e-30).


## 2026-10-10 — re-audit: you are the ONLY thing left, and the 8593 lines above are why nobody could tell (bean `qou-am5t`)

Measured the whole C→D surface today rather than quoting any figure. Result:
**this bean is the migration.** Three of the four trace channels are `agreed`
with definitional and production convention both D; `qbeta-decay` is the fourth
and is yours. Across the entire repo there is **one non-probe production file**
binding convention C — `computations/qbeta/qbeta_ck_cache.py:140`,
`z = sqrt(q) / (1 + q)` — and 11 of the registry's 12
`blocked_on_rederivation` rows point here.

Everything else an audit still reports is accounted: 143 adjudicated comparison
arms (the last 6 adjudicated today, `BLOCKING` 6 → 0, `e6a5d23e9`), 1 stays-C
by design, 18 deliberate Lean definitions, 1 symbolically-C witness.

**Nothing about the mathematics is new here.** The one thing worth adding is a
pointer, because this bean is 8593 lines and its own framing of the blocker was
wrong until 2026-09-14: the ladder is **not** blocked on the phase `α`
(`qou-pdix`). `cos ≤ 1` caps `F_N2(α) = cos(α − u/2)·(1 − u²)` at
`1 − u² = 0.99992745` for every real `α`, while the ruled `z_D` base needs
`F_required = 1.75923699418` (order-zero `E₀`) or `1.20016236389` (the
dashboard-scored cell) — so no `α` unblocks it, and the two cells a cosine can
reach are the two the 2026-09-08 ruling does not select. The live question is
**what object supplies a factor above 1 at all** — the base or the assembly.

State summary with the command behind each number:
[`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §5.

**Not reclaiming this bean** — the claim reset of 2026-10-04 stands and the open
item is research, not drain.

## 2026-10-10 — follow-up review (re-check of the `qou-avtq` sweep flags)

- The ruled-base exclusion reproduces 8/8, F_required = 1.7592.
- Step 27 (`:5997`) says "(8/8)" for the level-k probe; a re-run gives **6/8**, and the committed witness already records `allPassed: false`, so `qou-g5oz`'s title is stale.
- Under mpmath 1.3.0 that probe crashes at `:396` (`mp.eig` on a 1×1 block); a scratch shim was needed to reach 6/8.
- The α check is red from a C-vs-D mismatch: gap 0.01185 = α_D − α_C, against a hardcoded α_C at `qbeta_symbolic_chain_alpha_b.py:284`.
- The re-check verdict line (`:8603`) is cut off after an escaped `|`.
- The swing gate `swing_matches_o2` misses by 0.000339923 — cause R2 (muon pin CODATA 2018 → 2022, ΔS(muon) = 3.399e-4), a stale reference value.

The real gate remains the owner's gluon-letter ruling (`:8676`).

Checked read-only against qou `main` at `aa914b606a`, mpmath 1.3.0. Full write-up: `qou-review/avtq-reopened-beans-2026-10-10.md` (project files). Status unchanged.

## 2026-10-10 — owner decision: convention-D extractor support is tracked here

`qbeta_decay_sdp_full_ck.py` and `qbeta_decay_sdp_extended_ck.py` now **refuse** (exit 2) instead of reading the D-frame N3 witness with C-frame rungs (which produced c_2 = −9.296, c_3 = −974). The owner chose (2026-10-10, PR #7574) to merge the refusal and track D support **in this bean**: the extractors can run again only once the c_k ladder is re-derived under convention D, which is the open research item here, not a code change. The old C-frame bodies are kept as `_main_convention_c_historical()`. Bean stays open.

## 2026-10-11 owner ruling (decision card): gluon tail ALLOWED

Asked: does the 2026-08-30 "no gluon" ruling exclude the 2-letter gluon tail in γγ nucleon words? Owner answer: **allowed** (it does not exclude it). Consequence recorded earlier on this bean: the gluon family stays in the candidate set, so the family straddles the required factor and the selection must come from elsewhere (qou-99qc / O'Hara routes). Thread: Continue fourth session.

<!-- ported 2026-11-15 from PR #7603 (branch predates the beans/defs and folio/ moves) -->

## 2026-10-10 (3) — `χ_(2,1)(Δ_S) = 0` is now a sorry-free Lean theorem

`QOU/QBeta/DeltaSTwoRowCharacterVanishes.lean` turns the exact half of entry (2) into a theorem over an arbitrary field. It compiles with `lean`-direct exit 0 and no warnings, and `#print axioms` gives `[propext, Classical.choice, Quot.sound]` on all six results.

- **`trace_deltaS_eq_zero`:** for ANY `A B : Matrix (Fin 2) (Fin 2) K` with `tr A = tr B = h`, `tr((h²/2)·1 − (h/2)(A+B)) = 0`. This is basis-free.
- **`s1_quadratic`, `s2_quadratic`, `braid`:** an explicit two-row representation with `σ₁ = diag(q, −q⁻¹)` and `σ₂ = [[h − z_D, 1], [b², z_D]]`. It satisfies `(σ − q)(σ + q⁻¹) = 0` and the braid relation, and each generator has trace `h`. Its entries are the corpus's own objects: `z_D = q³/(q²+1)`, Hoefsmit `b²`, and `h − z_D = −1/(q(q²+1))` (`h_sub_zD`).
- **`chi21_deltaS_eq_zero`:** the composition.

**Consequence, as entry (2) stated.** Every convention-D functional on `Δ_S` is `a_(3)·χ_(3)(Δ_S)`, so the functional side of "what supplies a factor above 1" reduces to the trivial-block weight `{y_(3), 1}`.

**Scope.** That this representation IS the `(2,1)` irreducible for generic `q` is the standard Hoefsmit fact and is not re-proved. The basis-free theorem does not need it. Nothing numerical enters.



2026-11-15: moved under epic `qou-wxhi` (c_k ladder under convention D). Previous parent kept in history.


## 2026-11-15 — route 1 (full Hecke tower) cannot supply the missing factor without a free choice

Owner chose "full Hecke tower first" for the factor above 1 that the ruled z_D base needs (1.20016 on the dashboard cell, 1.75924 at order-zero E₀).

- **Trace side: nothing to sum.** `QOU.SchurWeyl.HeckeColimitFamilyTrace.trFam_inclLE` (sorry-free, any CommRing, any z) shows the iterated inclusion preserves the Markov trace. So the z_D trace of a fixed element already *is* its full-tower value. It is also exact in q, so all q-orders are already in it.
- **E₀ side: the tower factor carries a free scale.** Per qou-y3bm the true sum is 1/(1 − ℏ_q²λ₁) with λ₁ = ℏ_q/L_q², and L_q is free in the corpus. Measured at the proton pin (mp.dps 40), L_q would have to be **0.0745627** (λ₁ = 17.82) to give 1.20016, or **0.0474749** (λ₁ = 43.96) to give 1.75924. Both are above the divergence threshold √(ℏ_q³) = 0.0311882, so the tower can supply any factor in (1, ∞). Picking L_q that way is selection against the target. The one corpus-derived value, Kelvin L_q = L, gives 1.00097, which is −0.885 % against the implemented tower and moves away from CODATA.
- **Verdict, scope (a):** the full tower does not supply the factor unless the free L_q is chosen, so route 1 reduces to the open L_q modelling call (qou-y3bm successor). The live sources are the element (qou-99qc) and the N=3 colour trace (PR #7896).


## 2026-11-15 — route 2 (N=3 colour trace) also cannot supply the factor

The owner chose route 2 next. Measured with the census normal forms from `qbeta_option_e_required_level_probe.py` (sympy exact in h, read out at mp.dps 60, proton pin):

| element | z_D (level 2) | rank-3 colour z₃ = q⁵/(q⁴+q²+1) (level 3) |
|---|---|---|
| nuc11_interleaved | −17.496 % | −29.702 % |
| nuc11_gen_grouped | −15.451 % | −27.278 % |
| nuc9 | −30.936 % | −39.086 % |

- **Whole element at rank 3: wrong direction**, a factor of 0.852 on nuc11. Structural reason: z(r) = (q²−1)/(q(1 − q^{−2r})) is strictly decreasing in r for q > 1, and every census candidate needs a level between 1 and 2 (nuc11 r = 1.46, gen-grouped 1.49, nuc9 1.13, Δ_S 1.13). Any rank ≥ 3 moves away. It also contradicts D7 (D governs the decay channel). Scope: (a) for these candidates, plus the monotonicity of z(r).
- **Colour trace on the quark block only:** no corpus rule says which letters take which trace. In the reduced 6-slot normal form [γ, σ₀, σ₁, L−, L+, e⁻] the quark block is not a separate slot, and `SecondMarkovTrace.lean` says the rank-3 trace on general H_n elements is not re-derived there. Inventing a per-block rule would be a choice, so this is left as an owner modelling question.
- Net: routes 1 and 2 are both exhausted without a free choice. What is left is the element (route 3, qou-99qc), the L_q sibling thread, and the meaning of ε (assembly).

## 2026-11-16 — derived D rungs recover none of the gap (PR #8098, issue #8097)

Probe `qbeta_d_ladder_gap_recovery_probe.py` (60 dps, 6/6 PASS). The only derived D rung (c_2 = −1, b² = [3]_q/[2]_q², factor 1 − u² = 0.99992746) applied to all 4 census elements × both E₀ forms: recovery −0.013 % to −0.046 % of the log-gap on every cell, i.e. it moves every cell away by 72.5 ppm. Closing the 12–43 % gap with any ladder needs uniform |c_k| ≥ 1997..5898 (LadderUniformBound). c_3, c_k≥4 and the N=1 phase are not derived under D and were not applied. Scope (a). The gap is in the base (element qou-99qc / meaning of ε); the one ladder-side lever that can exceed 1 is an imaginary eigenphase (cosh route), still underived. Bean stays open.

## 2026-11-20 — W2: Q_beta ladder threads consolidated in #8540
#7610 (wiring producer refuses; four D probes on chi_all_lambda_any), #8098 (the derived c2 rung recovers ~0 % of the gap) and #8100 (production Q_beta labelled as the retired mixed base) are cherry-picked onto current main as PR #8540. All probes re-run and reproduce their witnesses. No element was chosen, no rung was fitted, and nothing was re-scored. Still open: the base (F_required > 1 on every ruled cell) and the element (qou-99qc). (session_01VQDpPfkCTEiKEWdANj7rYB)

## 2026-11-20 — W2 cross-workstream briefing (owner: "make sure they know")
Full briefing: PR #8526 comment 7047864732 and docs/coordination/2026-11-20-w2-qbeta-ud-briefing.md. Record: docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md sections 1-11.
Key points: Q_beta = (h[2]/2)*y3*E0 and sees only the isospin-3/2 block. The ruled epsilon (z_D, -43%) = label-A round trip = whole-space quantum trace. Label B (J4, strand-4 gamma-gamma) gives +0.33% and is NOT adopted (it labels isospin multiplicity, not n<->p). Label C gives 1/3, 0 and 0.202, none close. The owner made no label ruling ("3 2"). u/d are separate lines of the (3,1) rep of H4, not orientation-only (def:up/down-quark are stale). Convention-D volumes lie past the Phi_q pole. The six-term -2.43e15 was a truncated divergent series (fixed). The +0.17% / ~1 ppm Q_beta values and the April BW run are superseded or circular.

### 2026-11-21 — the 4.50e+04 gate-out IS the convention C → D switch, at 1.9e8 gain

`d5cbc0146ee`, [`qbeta_c4_gate_out_is_the_convention_switch_probe.py`](../../computations/qbeta/qbeta_c4_gate_out_is_the_convention_switch_probe.py), **9/9**, exit 0. Scope (a); nothing fitted, nothing wired, no witness refreshed.

**The chain, reproduced rather than argued.** `Q_N1` in the upstream witness `q-beta-operator-valued-N3.witness.json` is `Q_A·cos(α_eff)` with `α = (z−1)·h/2` — so it depends on **`z`, the Markov parameter**, i.e. on the convention. The owner ruled convention D canonical on **2026-08-15**, after the committed witness was written on **2026-06-28**:

| | convention C | convention D |
|---|---|---|
| `z` | `0.499320334184` | `0.612688037146` |
| `α = (z−1)h/2` | `−0.05233612027` | `−0.04048577734` (22.6 % change) |
| `Q_N1 = Q_A cos(α_eff)` | `0.7823911675028` | `0.78286150492739` (**6.01e-4** relative) |

The peel **pins** `c_2 = −1` and `c_3 = −2`, so the entire discrepancy lands on the next free rung at a gain of `1/u⁴ = 1.90023e+8`:

    c_4 from the sha-era upstream : -2.543811724   (HEAD records -2.537865912)
    c_4 from the HEAD upstream    : -114136.1531   (the fresh run recorded -114136.0)

**Convention D reproduces the live `Q_N1` to 2.96e-52**; convention C reproduces the committed one to `3.03e-8`, the residual being the `Q_A` precision difference between the two upstreams. So the move is neither drift, nor environment, nor precision — **a 6.01e-4 move upstream becomes a 44867× move in a recorded "tower coefficient."**

**What is already the corpus's.** `docs/coordination/1ppq-qbeta.md` calls this producer *"form-fitting iterative peel"* (2026-05-31), and `qbeta_habiro_integrality_kill_test.py` states that `c_4`/`c_5` have *"NO scheme-independent empirical value … every recorded c_4/c_5 number presupposes a structural choice at a lower rung (extended-ck imposes c_3 = −2)"*. **This producer is that variant.** New here is the exact cause and the two defects below.

**It is a measured case for a standing warning.** AGENTS.md says the ladder *"must be RE-DERIVED under D, and that is NOT a z-swap"*. This is what a z-swap produces: `c_4 = −114136` where the C frame had `−2.54`, with the integrality claim gone vacuous.

**Defect 1 — the integrality test is RELATIVE, so it goes vacuous as `c_k` grows.** Not found in the corpus. `frac = |c − round(c)|/|c| · 100 < 5` admits **±0.127** at `c_4 = −2.54` but **±5706.8** at `−114136`, so *"c_k is an integer"* carries no information there — and the producer then **continues peeling with the rounded value**, so the next rung absorbs the rounding error. The `1 ppQ ACHIEVED` banner is likewise unfalsifiable: `c_k := (R−1)/u^k` followed by `R /= (1 + c_k u^k)` gives `R/R = 1` exactly, so the residual is zero **by construction** at any anchor — the same inversion AGENTS.md records for `qbeta_ck_cache.py`.

**Defect 2 — found by the probe failing its own first version.** The witness's `commitSha` (`69f7ec22fef`) holds `c_4 = −1.14353678` while **HEAD** holds `−2.537865912`: it was re-committed after that sha was stamped, so `commitSha` does not identify the content at HEAD. AGENTS.md records this class for `scriptCommitSha`; it applies to `commitSha` too, and it is why a gate must baseline against **HEAD**, not the recorded sha. Asserted as a check so it cannot silently stop being true.

**Attribution is NOT available, and saying so is part of the result.** The only commit this clone's log attributes to the upstream witness in the window is `806d5146227`, which **is** a shallow boundary (checked against `.git/shallow`), so the log is truncated there. The values are reliable — both read out of git — but which commit moved `Q_N1` cannot be determined here. **Do not quote `806d5146227` as the cause.**
