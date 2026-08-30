---
# qou-cds1
title: 'S1 (SCIENCE): re-derive the Q_beta c_k ladder under D — not a z-swap, and that is proved'
status: in-progress
type: task
priority: high
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-30T18:48:18Z
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

`content/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.md:21`:

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

`content/quantum-observable-universe/lean/QOU/QBeta/DFrameBarAction.lean`. Eleven theorems, `lean`-direct **exit 0**, `#print axioms` clean on all eleven (`propext, Classical.choice, Quot.sound`; **zero sorryAx**). No `sorry`, no `axiom`, no `native_decide`, no `: True`.

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
