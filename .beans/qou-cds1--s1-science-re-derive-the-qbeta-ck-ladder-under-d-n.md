---
# qou-cds1
title: 'S1 (SCIENCE): re-derive the Q_beta c_k ladder under D — not a z-swap, and that is proved'
status: in-progress
type: task
priority: high
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-19T07:21:43Z
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
