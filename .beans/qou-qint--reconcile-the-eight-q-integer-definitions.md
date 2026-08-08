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


---

# *** MIGRATION COST MEASURED (2026-08-08) — consolidation is NOT a free rename ***

Built the canonical home and tried a 5-file migration. Result: 2/5 clean,
3/5 needed proof surgery and were REVERTED rather than churned.

DELIVERED:
  QOU/MathlibExt/QIntegerCanonical.lean  -- the single home.
    qIntBal  (canonical [n]_q)  and  qIntGeo  (geometric, for q^2 sites),
    both `abbrev`s onto the ALREADY-PROVED defs in QHookDimension{,Balanced},
    so no new definition enters the corpus. Plus the bridge theorems in one
    place: qIntBal_eq_twist_canonical, qIntBal_bar_even_canonical,
    qIntGeo_bar_covariant, and @[simp] defining equations.

MIGRATED AND VERIFIED (lean-direct EXIT 0):
  mass-theory/degree-two-baryon-weight.lean       qInt
  mass-theory/wigner-coefficient-derivation.lean  qInt   (note: arg order (n)(q))

REVERTED, and why -- THE COST FINDING:
  QOU/MassComputationChainRoadmap.lean   qInt
  QOU/GaugeFieldFluidDynamics.lean       qInteger
  information-theory/quantum-volume.lean qInteger
  All three are VERBATIM duplicates of qIntBal, so the swap is semantically
  free -- but their downstream proofs do `unfold <local>; simp`, and after
  aliasing, `unfold` reduces through BOTH layers and leaves the follow-up
  tactic nothing to act on ("simp made no progress" / "failed to unfold").
  Adding @[simp] defining equations fixed 2 of 5; the rest need per-site
  tactic edits. I declined to rewrite three files' proofs in passing.

  => BUDGET FOR THE REST: expect ~60% of migrations to need proof surgery,
     roughly one tactic edit per lemma that unfolds the local name. This is
     the number to plan the sweep with; it is NOT a mechanical rename.

STILL NOT MIGRATED: ~40 balanced duplicates + the 10 geometric sites.

ALSO DO NOT FORGET (guard, unchanged): Interactions/HeckeEnergyPositivity's
qIntegerRescaled = sum q^(2j) is geometric IN q^2 and CORRECT. Do not convert.


---

# *** SURGERY COST REFINED (2026-08-08) — it is mechanical after all ***

The three files I reverted last round are now MIGRATED. The "~60% need proof
surgery" figure stands, but the surgery turned out to be a UNIFORM ONE-LINE
SUBSTITUTION, not per-site reasoning:

    unfold <local>   ->   simp only [<local>, QOU.Mass.QHookDimensionBalanced.qIntBal]

Verified empirically (three candidate tactics tested on the 1-site file; only
this one and an explicit `show` worked -- `unfold <local> <canonical>` FAILS,
because unfold reduces through the alias and the canonical name is no longer
present in the goal).

Applied to 8 sites across 3 files:
  QOU/MassComputationChainRoadmap.lean    qInt       1 site
  information-theory/quantum-volume.lean  qInteger   1 site
  QOU/GaugeFieldFluidDynamics.lean        qInteger   6 sites
All three lean-direct EXIT 0.

SO THE REVISED BUDGET IS BETTER THAN FEARED: ~60% of migrations need an edit,
but the edit is the single substitution above. Plan the remaining ~50 sites as
mechanical, not as per-file proof work.

A TRAP TO AVOID (cost me a cycle): if the migration comment mentions
"QIntegerCanonical", a naive `if "QIntegerCanonical" not in text` guard will
think the import is already present and SKIP inserting it. Check for the literal
import line, not the bare filename.


---

# *** THE CEILING, MEASURED (2026-08-08) — "43 duplicates" was WRONG ***

Pushed into the varied-signature batch to drain it. It does not drain: the 43
balanced definitions are NOT 43 duplicates of qIntBal. They are 43
balanced-CONVENTION definitions with genuinely DIFFERENT TYPES.

Method: attempted mechanical migration on every plausible candidate with
AUTO-REVERT, and let Lean adjudicate interchangeability rather than reasoning
about defeq. 3 kept, 2 refused, 4 skipped as type-incompatible up front.

MIGRATED THIS ROUND (lean-direct EXIT 0):
  predicted-spectra/em-coupling-fixed-point.lean    qIntReal
  predicted-spectra/skein-finiteness-bound.lean     qInt
  brings-surface/orbital-fourier-decomposition.lean qInt
RUNNING TOTAL: 8 of 55 consolidated onto the canonical definition.

WHY THE REST ARE NOT DRAINABLE (this is the ceiling, not a backlog):
  GUARDED     11   `if q = 1 then n else ...` -- a DIFFERENT function. Migrating
                   changes behaviour at q=1. Not a duplicate.
  Z-INDEX      6   (k : Z). qIntBal takes N. Needs a Z sibling in the canonical
                   module before any of these can move.
  RING-INDEX   3   exponent lives in the ring/reals, not N (q ^ (rho : R)).
                   A different function again.
  SHORTHAND    7   [2]_q = q + q^-1, [3]_q = q^2+1+q^-2 written out. Arguably
                   fine as-is; consolidating buys little.
  CTX-BOUND    1   q comes from a structure field (ctx.q).
  PROOF-FORM   2   defeq-equal, but downstream proofs need the literal
                   syntactic body (HabiroMagnitudeA3: (q^n)^-1 vs q^-1^n;
                   bar-involution-invariance: Z-cast exponent). Lean refused
                   both; auto-revert kept them intact.

SO: the honest consolidation ceiling on the CURRENT canonical signature is
roughly what has been done. To go further you must first EXTEND the canonical
module -- add a Z-index sibling and decide a policy for the guarded variants
(either a guarded canonical form, or leave them and document that they are
deliberately different functions). That is a design decision, not a sweep.

ALSO FOUND: braids-and-knots/chi-std-pernucleon-closed-form.lean is RED ON MAIN
(pre-existing, unrelated to this work) -- another instance of the class in
qou-orph / qou-k448 where nothing checks a file.
