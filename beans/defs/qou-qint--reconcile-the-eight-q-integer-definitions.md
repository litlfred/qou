---
# qou-qint
title: Reconcile the 8 q-integer definitions — `qInt` names two conventions
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T13:40:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-4cu3
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

---

## 2026-08-30 — THE STATED CEILING IS STALE. Both prerequisites already exist.

Found from `qou-f8lit` while re-verifying the q-bracket row of
`docs/audits/2026-06-21-constant-consistency-axis2-clean.md` (whose ✅ this bean
falsifies). **This is not a new design question — it is a bean that did not
learn.**

This bean closes by saying:

> To go further you must first EXTEND the canonical module — add a Z-index
> sibling and decide a policy for the guarded variants (either a guarded
> canonical form, or leave them and document that they are deliberately
> different functions). **That is a design decision, not a sweep.**

Both were done on **2026-08-10**, two days after this bean was written
(`90140791dd`, arc `qou-lgkd`). This bean's `updated_at` is still
`2026-08-08T13:40:00Z`, so it has never seen them.

### Prerequisite 1 — ℤ-index sibling: EXISTS

    QIntegerCanonical.lean:176   qIntBalZ (q : R) (k : ℤ) : R
    QIntegerCanonical.lean:195   qIntBalZ_neg      : qIntBalZ q (-k) = -qIntBalZ q k
    QIntegerCanonical.lean:204   qIntBalZ_bar_even : qIntBalZ q⁻¹ k = qIntBalZ q k

The bar-even lemma is the one that matters — it is the property this bean's own
argument for `qIntBal` rests on, now available at ℤ index.

### Prerequisite 2 — guarded policy: DECIDED, and it went the "guarded canonical
### form" way, covering BOTH guard shapes the corpus actually uses

    qIntBalCl     q n := if q = 1        then n else qIntBal q n   -- one-sided
    qIntBalClSing q n := if q - q⁻¹ = 0  then n else qIntBal q n   -- two-sided
    qIntGeoCl     q n := if q = 1        then n else qIntGeo q n

with the three bridges a migrating site needs:

    qIntBalCl_of_ne_one       guard invisible off q = 1
    qIntBalClSing_of_ne       guard invisible off the singular locus
    qIntBalClSing_eq_qIntBalCl  the two guards agree off q ∈ {0, −1}

and — the part that answers this bean's *reason* for calling the guarded sites
undrainable (*"Migrating changes behaviour at q=1"*) — two lemmas that make the
behaviour change **checkable rather than asserted**:

    qIntBal_one_eq_zero          qIntBal 1 n = 0, NOT n (Lean's x/0 = 0)
    qIntBalClSing_eq_qIntBalCl   names q = −1 as the point the two guards differ

So the objection stands as a *fact* (guarded → unguarded really is a behaviour
change) and is no longer a *blocker*: a guarded site migrates to a guarded
canonical form of the matching shape, and the difference between the two guard
shapes is a proved lemma rather than a judgement.

### What this changes

**This item is no longer an owner design call.** It is a mechanical migration
against an existing canonical module. Nothing here needs a ruling.

**Do not carry this bean's counts forward.** `Z-INDEX 6` / `GUARDED 11` /
`SHORTHAND 7` were measured on 2026-08-08 against a corpus that has moved; a
rough re-scan on 2026-08-30 found guarded and ℤ-indexed sites in files this
bean does not name. Re-measuring is the migration's first step, not a
precondition someone else owes.

Two adjacent findings, neither drained here:

* **`braids-and-knots/scratch.lean`** defines `qNumberSym` and is in `content/`.
  A file called `scratch` carrying a q-integer definition is the `qou-orph` /
  `qou-k448` class ("nothing checks a file"), not a q-bracket problem.
* This bean already records **`chi-std-pernucleon-closed-form.lean` RED ON
  MAIN**; it is still red, and still carries an unrouted ℤ-index bracket at
  line 104.

### Why this is worth writing down beyond the migration

`qou-f8lit` is an arc about durable artifacts carrying claims that decayed —
a certified constant that went stale, an audit's ✅ that was only as wide as one
directory, and three of my own unmeasured absences. **A bean is a durable
artifact too.** This one escalated a decision to the owner, the decision was
made by a sibling arc 48 hours later, and the escalation sat unqualified for
three weeks. AGENTS.md's rule that a *completed* bean is the one that bites has
a mirror: **an open bean's stated blocker is a claim with a date on it.**

## 2026-08-30 (same day, CORRECTION) — both "adjacent findings" above are WRONG

I wrote the two bullets above ("Two adjacent findings, neither drained here")
by repeating this bean's older `ALSO FOUND` line **without opening either
file.** Measured with `lean`-direct against the restored oleans, on `main` at
`a6b12890c9`:

| claim I made | measured |
|---|---|
| `chi-std-pernucleon-closed-form.lean` "is still red" | **EXIT 0.** Green, and **zero sorries.** |
| ...and "still carries an unrouted ℤ-index bracket at line 104" | **Routed.** `qNum_eq_qIntBal` at line 114, sorry-free. |
| `scratch.lean` "carries a q-integer definition" (implying unrouted) | **Routed** — `qNumberSym q n := qIntBalZ q n`, and green. |

**The file says so itself**, in the docstring immediately under the site I
called unrouted:

> This site was the one the `qou-qint` drain could not reach *while the file
> was red on `main`*; **it is migrated now** that the two closed-form theorems
> above are proved.

So this bean's own `ALSO FOUND: chi-std-pernucleon-closed-form.lean is RED ON
MAIN` is **stale as well** — someone fixed the file and migrated the site, and
neither this bean nor mine learned it. Both are corrected here.

**Verified the check FIRES, not merely that it passes.** An `EXIT 0` with no
output is the same shape as a check that examined nothing, which is why the
green above is not asserted on the exit code alone: injecting
`theorem deliberate_break_probe : (1:Nat) = 2 := rfl` produced
`error: Not a definitional equality` at line 328 and `EXIT 1`. File restored;
`git diff` clean.

### This strengthens the finding above rather than weakening it

`scratch.lean` is a **live consumer of `qIntBalZ`** — so the ℤ-index sibling
is not merely present in the canonical module, it is already being used at a
call site. The migration this bean calls blocked is not only unblocked, it has
partly already happened.

### And the failure is the one this arc exists to document

I asserted "it is still red" **inside an addendum whose entire subject is that
an open bean's stated blocker is a claim with a date on it**, and merged it to
`main` (#6084). Reading a durable artifact's old text and restating it is
exactly how the claim survived three weeks in the first place; doing it in the
correction is how it would have survived three more.

The rule that would have caught it costs one command: **open the file.** A
bean, an audit ✅, a docstring and a sibling's finding are all secondary
sources. `lean`-direct is the primary one.


## 2026-10-10 re-audit verdict: **REPARENT** (bean `qou-am5t`)

Same axis: `qInt` naming two q-integer conventions. Not the Markov parameter.
Keep open, re-home.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## Progress Update (Round 92 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/NucleonOrderingAndBringAdjointTorsionBrick.lean` with 80-dps probe `computations/probes/nucleon_ordering_and_bring_adjoint_torsion_brick_probe.py` and witness `computations/probes/nucleon-ordering-and-bring-adjoint-torsion-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8348 (`feat/qou-b9cj-q6h7-qd27-qint-r91v-tvok`, HEAD `e0985c4fc3ff765e1935e3343005512aaca69b2b`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8348, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-09: "consolidate(qou-qint): the Laurent twist, and closing the census at 47 of 55"). The work may be partly or fully done. Read the bean before you close it.
