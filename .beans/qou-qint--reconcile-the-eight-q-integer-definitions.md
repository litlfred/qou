---
# qou-qint
title: 'Reconcile the 8 q-integer definitions — `qInt` names two conventions'
status: todo
type: task
priority: high
created_at: 2026-08-08T13:40:00Z
updated_at: 2026-08-08T13:40:00Z
---

Filed from the derivation in
docs/audits/2026-08-08-q-integer-convention-derived.md (probe:
computations/q_integer_convention_derivation.py, all identities exact).

## Settled first — the canonical convention is DERIVED, not chosen

BALANCED [k]_q = (q^k - q^-k)/(q - q^-1), forced by three independent routes:
  D2  bar-parity: balanced is bar-EVEN, geometric is bar-COVARIANT with weight
      -(k-1).  Any bar-even (cosh / mass-side) quantity MUST use balanced or the
      corpus's parity bookkeeping silently breaks.  [this one appears unrecorded]
  D3  AGENTS.md 7a's Hecke relation (s-q)(s+1/q)=0 has structure constant
      q - q^-1 = the balanced denominator.  Downstream of an existing choice.
  D4  it is the quantum dimension: sum over the SYMMETRIC sl_2 weight string.

And D1 (already Lean-proved as QHookDimensionBalanced.qIntBal_eq_twist):
  [k]_q^bal = q^-(k-1) * [k]_{q^2}^geo
so a GEOMETRIC site is CORRECT iff its variable means q^2.  This is why the
sweep cannot be blanket-applied.

## The inventory (4 geometric / 4 balanced)

  GEOMETRIC  qInt (q) (n)            MathlibExt/QIntegerFactorial
  balanced   qBracket (q) (n)        MathlibExt/QPartitionCombinatorics
  GEOMETRIC  qInt (q) (k)            FluidDynamics/surreal_enstrophy_finite_modes
  balanced   qInt (k)                FluidDynamics/q_turbulence_spectrum
  GEOMETRIC  qInt (q) (n)            Resurgence/StokesConstantQDimCategoricity
  GEOMETRIC  qIntPoly (q) (n)        Mass/QHookDimension
  balanced   qIntBal (q) (n)         Mass/QHookDimensionBalanced
  balanced   qBracket (R) (q) (k:Z)  IwahoriHecke/Hoefsmit

THE HAZARD: the bare name `qInt` is GEOMETRIC in three files and BALANCED in a
fourth.  Reading a call site does not tell you which object you have.

## The work

Per site, in this order:
 1. determine whether its variable means q or q^2 (D1 decides correctness);
 2. determine whether the consuming quantity must be bar-even (D2 decides
    whether geometric is even admissible there);
 3. rename so the convention is in the NAME (qIntGeo / qIntBal), never bare
    `qInt`;
 4. re-verify each touched file with lean-direct.

## Already CHECKED, do not re-open

 * Resurgence/StokesConstantQDimCategoricity -- geometric, but its result is an
   honest NEGATIVE that holds in EITHER convention ([n]_q|_{q=1} = n for all n;
   1+X+X^2 != 3 as a polynomial; balanced [3]_q = q^2+1+q^-2 is equally != 3).
   Conclusion robust.  Rename only.
 * Mass/QHookDimension vs QHookDimensionBalanced -- a deliberate pair; the
   second exists to prove the twist between them.  Not a contradiction.
 * predicted-spectra/em-coupling-chern-simons -- FIXED (bean qou-pjfu),
   lean-direct exit 0.

## Guardrail

Do NOT blanket-convert geometric -> balanced.  D1 makes a geometric site correct
when its variable is q^2; converting it would INTRODUCE an error.  Every site
needs the two-step check above.


---

# *** SCOPE CORRECTED (2026-08-08) — 55 definitions, not 9 ***

My original inventory came from a narrow grep and undercounted by 6x. Full scan
of `def q{Int,Bracket,Num,Integer}*` over content/**/*.lean:

    total       55
    balanced    43   <- the corpus is ALREADY overwhelmingly canonical
    geometric   10   <- the actionable set
    geo-in-q^2   1   <- CORRECT per D1 (HeckeEnergyPositivity.qIntegerRescaled)
    Z-polynomial 1

So this bean is NOT "convert everything to balanced" -- the convention is
already settled in practice. It is a NAMING problem: ~15 aliases (qInt, qIntBal,
qIntPoly, qIntReal, qIntSym, qIntZ, qInt2, qInt3, qBracket, qBracket2, qNum,
qNumber, qNumberSym, qInteger, qIntegerRescaled) and the bare name `qInt` used
for BOTH conventions across 18 files that define it locally.

THE 10 GEOMETRIC (actionable):
  MathlibExt/QIntegerFactorial                qInt
  Resurgence/StokesConstantQDimCategoricity   qInt  + qIntPoly (Z-poly)
  FluidDynamics/surreal_enstrophy_finite_modes qInt
  BraidKnot/wedderburn_trace_identity         qInt
  QCollatz                                    qInt
  Mass/QHookDimension                         qIntPoly
  Mass/QHookDimensionBalanced                 qIntPoly   (deliberate pair)
  Torsion/TopologicalMass                     qNumber
  lifting-and-descent/quantum-dilogarithm     qInteger

D1 VALIDATED EMPIRICALLY -- do not blanket-convert:
  Interactions/HeckeEnergyPositivity.qIntegerRescaled = sum_{j<k} q^(2j)
  is geometric IN q^2, which D1 says is CORRECT. It is even named "Rescaled".

CHECKED, NOT defects (do not re-open):
  * Archimedean/GroundRing.qInt scans geometric but IS BALANCED -- body is
    sum_{k<|n|} T(n-1-2k), the symmetric weight string, with correct n<0
    antisymmetry. A classifier matched its comment, not its body.
  * Torsion/TopologicalMass.qNumber is geometric in a MASS file (which D2
    predicts is a defect) but feeds NO mass result -- only two lemmas about
    itself. Dead weight. It DOES have a wrong docstring ("Quantum
    dilogarithm: Phi_q(z) = ...") on a q-number -- a real, separate, minor fix.

REVISED PLAN: this is a rename-for-clarity sweep over ~15 aliases plus a
convention check on 10 sites -- multi-session. Do the naming first (mechanical,
low risk), the 10 checks second.
