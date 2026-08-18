---
# qou-cds1
title: 'S1 (SCIENCE): re-derive the Q_beta c_k ladder under D — not a z-swap, and that is proved'
status: in-progress
type: task
priority: high
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-19T13:36:01Z
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
