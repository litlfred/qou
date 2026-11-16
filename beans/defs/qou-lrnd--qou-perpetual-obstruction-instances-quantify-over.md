---
# qou-lrnd
title: QOU perpetual-obstruction instances quantify over p but conclude about a constant
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T15:26:08Z
updated_at: 2026-11-16T20:28:25Z
parent: qou-6qbv
pr: 8189
---

FOUND 2026-08-22 while resolving qou-oy4r (main red on
def:qou-motivic-galois-instance). File:
folio/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicPerpetualObstructionFromTrace.lean
Sorry-free, so every sorry and axiom audit reports it clean.

Two theorems are docstring'd as the QOU instances:

  theorem qou_proton_perpetual_obstruction :
      exists S : Finset N, forall p : Nat.Primes, (p : N) not-in S -> not IsUnit (4 : Z) :=
    <empty, fun _ _ => galois_trace_not_unit 4 (by norm_num)>

  theorem qou_deuteron_perpetual_obstruction :
      ... -> not IsUnit (-32 : Z) := <empty, fun _ _ => ...>

The conclusion does not mention p or S. The binders are decoration: the
proof term discards both and takes S = empty. What is proved is
'4 is not a unit in Z' and '-32 is not a unit in Z' — norm_num facts about
two integers. The claim the docstrings make — that the QOU Frobenius,
Frob_p = f(u)|_{u=zeta_2p} from the Habiro expansion, is a non-unit at every
prime — is nowhere in either TYPE. It is entirely in the prose: the
derivation 'Frob_p == a0(-1) + a1(-1)(1-(-1)) = 4 (mod p-ideal)' appears only
in the docstring.

NOT a claim that the theorems are false. They are true and sorry-free.
The defect is that the p-quantifier makes them LOOK like statements about
almost-every prime while their content is a statement about a constant.
This is the 'sorry-free != derived' family, and the shape the da-arity-conflation
criterion exists to catch (STRICT section: 'Pointwise, or the universal
closure?' / 'a proposition provable without using any hypothesis about the
mathematical objects in question').

NOT affected: perpetual_obstruction_from_trace in the same file is honest —
it takes trace : Nat.Primes -> Z and a real hypothesis h_bound, and the
conclusion genuinely depends on trace. The gap is that the QOU instances
never instantiate it with an actual Habiro trace; they pass a constant.
perpetual_obstruction_from_collapse_invariant has the same decorative
binders but its hypothesis 1 < C.natAbs does the work, so it is defensible
as a general lemma.

WHAT WOULD CLOSE IT: instantiate perpetual_obstruction_from_trace with a
real trace function derived from the Habiro expansion, so that the type
carries the p-dependence the docstring describes. The numerical side already
exists — computations/probes/habiro_frobenius_probe.py with a 57 KB witness
carrying per-prime atoms.

BLOCKS: qou-oy4r cannot be closed by retargeting def:qou-motivic-galois-instance's
lean.ref at these theorems — that would record a definition as formalized by
a theorem whose type says nothing about it.

PARTLY CLOSED 2026-08-22. Added to
MotivicPerpetualObstructionFromTrace.lean, sorry-free, verified with
lean-direct against restored mathlib oleans (exit 0, 3.0s):

  theorem habiro_frobenius_not_unit
      {R : Nat.Primes -> Type*} [forall p, CommRing (R p)]
      (frob : forall p, R p) (reduce : forall p, R p ->+* Z)
      (C : Z) (hC : 1 < C.natAbs)
      (h_collapse : forall p, reduce p (frob p) = C) :
      forall p : Nat.Primes, not IsUnit (frob p)

plus qou_proton_frobenius_not_unit (C = 4) and
qou_deuteron_frobenius_not_unit (C = -32), and the supporting
not_isUnit_of_image (non-unitness transfers backwards along a ring map).

The conclusion is 'not IsUnit (frob p)' — the Frobenius itself, with p in the
statement. That is the defect this bean names, fixed: p is no longer
decoration.

#print axioms on all four: [propext, Classical.choice, Quot.sound]; no
sorryAx. 0 sorries in the file.

WHAT IS STILL OPEN, deliberately: h_collapse — that reduce p (frob p) = C —
is an explicit HYPOTHESIS, not a proved lemma. It is the symbolic derivation
(at q = zeta_2p: q == -1 mod p-ideal, (q;q)_m == 0 mod p-ideal for m >= 2, so
the expansion collapses to a0(-1) + 2*a1(-1)) which lives in
computations/probes/habiro_frobenius_probe.py and not in Lean. Stating it as
a hypothesis is what keeps that boundary visible; proving it needs cyclotomic
ring theory over Z[zeta_2p] and is the remaining work.

The four original theorems are KEPT — all four are cited externally — with
their docstrings corrected to say what their types actually prove. The
proton/deuteron ones now open with 'read the TYPE. The conclusion is
not IsUnit (4 : Z), which mentions neither p nor S'.


---

# RE-SCOPED 2026-08-23 — the collapse is easier than recorded; the step after it does not hold

Worked in the foreground. The bean said the remaining work was that proving
`h_collapse` "needs cyclotomic ring theory over Z[zeta_2p]". Both halves of
that turned out to be wrong, in opposite directions.

## The collapse needs no cyclotomic theory at all — PROVED, general

New file `QOU/LiftingDescent/HabiroCollapse.lean` (sorry-free, lean-direct
exit 0, `#print axioms` = propext / Classical.choice / Quot.sound on all seven
declarations):

    map_qPoch_eq_zero     phi q = -1  ->  phi ((q;q)_m) = 0   for m >= 2
    map_habiro_expansion  phi (sum_{m<N} a m (q;q)_m) = phi (a 0) + 2 phi (a 1)

The whole mechanism is that the `i = 2` factor is `1 - q^2` and `1 - (-1)^2 = 0`.
No roots of unity, no ramification, no ring of integers appears in either
proof. So the cyclotomic content of `h_collapse` was exactly ONE fact,
`phi(zeta_2p) = -1`; everything downstream of it was ordinary ring theory that
had simply never been separated out.

## The step AFTER the collapse does not hold — scope (b), invariant exhibited

Per AGENTS.md this is a **structural exclusion, not a scope-limited
negative**, and the invariant is cited rather than asserted. Two exact checks
in `computations/probes/cyclotomic_residue_four_unit_probe.py` (pure integer
arithmetic; every polynomial division asserted exact; no floats):

**(1) The target ring cannot be Z.** `habiro_frobenius_not_unit` types
`reduce p : R p ->+* Z` while its docstring calls it "reduction modulo the
prime ideal P = (1 - zeta_p)". Those cannot be the same map — that reduction
lands in `O/P = F_p`. And no hom `Z[zeta_2p] ->+* Z` sends `zeta -> -1`: it
would force `Phi_2p(-1) = 0`, and computing Phi_2p from the defining recursion
(no closed form assumed) gives `Phi_2p(-1) = p` for every p tested. None
exists at all, in fact — `O/ker` would be an infinite quotient of a rank-(p-1)
ring of integers.

**(2) With the correct target, the residue is a UNIT.**
`not_isUnit_of_image : not IsUnit (phi x) -> not IsUnit x` needs the RESIDUE
to be a non-unit. In `F_p`, `4` is a unit for every `p != 2`
(`isUnit_four_zmod`, in Lean). And this is not a gap awaiting a cleverer
proof — the inference is FALSE: the cyclotomic unit

    u4 = 1 + zeta + zeta^2 + zeta^3 = (1 - zeta^4)/(1 - zeta)

is a unit of `Z[zeta_p]` — inverse `1 + zeta^4 + ... + zeta^{4(b-1)}` where
`4b == 1 (mod p)`, integral by inspection — and `zeta == 1 (mod P)` gives
`u4 == 4 (mod P)`. Verified `u4 * v = 1` exactly for
p in {3,5,7,11,13,17,19,23,29,31,101,1009}.

So `Frob_p == 4 (mod P)` is COMPATIBLE with `Frob_p` being a unit.

## The sharp statement of what the route CAN give

If `reduce p (frob p) = C` then `frob p` is a non-unit exactly when the
residue VANISHES, i.e. when `p | C` — then `frob p` lies in the proper ideal
`P`. For `C = 4` and `C = -32` that is `p = 2` alone.

**The collapse route therefore yields non-unitness at the finitely many primes
dividing C — which is the complement of what "perpetual" means.** A congruence
to a fixed nonzero constant is the wrong shape for an almost-every-prime
statement, independently of how the constant was derived.

## Correcting my own work from earlier today

I added `habiro_frobenius_not_unit` + the proton/deuteron instances in
`577266d17c` and reported them as closing the `p`-is-decoration defect. The
`p`-decoration part stands. But I described `h_collapse` as "an explicit
hypothesis ... the remaining work", implying it was dischargeable. It is not,
in the shape it is stated. The four theorems remain true, sorry-free and
cited — they are correct statements about an arbitrary family with a hom to Z
— and their docstrings are corrected in `0eb307afd0` to say what they reach.

Also removed there: `qou_proton_perpetual_obstruction`'s claim that
"N(Frob_p) == 4^{p-1} (mod p), which is never +-1 for p >= 3". Wrong twice —
by Fermat `4^{p-1} == 1 (mod p)` for `p` odd, and `1 == +1`.

## STILL OPEN — and it is a different question than this bean opened with

Not "discharge h_collapse". The open question is: **what argument gives the
perpetual obstruction for the QOU Frobenius at all?** A residue mod one prime
cannot, by (2). Candidate shapes, none attempted here:

* An **archimedean** bound. A unit of `O` has norm +-1, so bounding
  `|Frob_p|` below at every complex embedding bounds `|N(Frob_p)| > 1`. This
  is the norm argument the deleted docstring was reaching for, done at the
  right place — the archimedean side, not mod P.
* A **valuation** at some prime dividing the collapse invariant, which gives
  the finite set above and nothing more.
* Dropping "perpetual". If the honest theorem is about `p | C`, say so; a
  finite exception set is what `perpetual_obstruction_from_trace` already
  models, but with `S` the COMPLEMENT of the good set rather than a bad set.

Commits: `a9c289bb38` (HabiroCollapse + probe), `0eb307afd0` (docstrings).


---

# 2026-08-23 (second pass) — the constants are 8 and 192, and the cited witness never tested the collapse

Went at the archimedean route recorded above, and checked the input data before
building on it. Two findings, both measured.

## The Lean's constants are wrong

`map_habiro_expansion` fixes `C = φ(a₀) + 2φ(a₁)` from a₀ and a₁ alone — it does
not depend on p. Read straight out of
`computations/habiro/habiro-coefficients-atomic.witness.json`:

    atom      a_0            a_1              a_0(-1)  a_1(-1)   C     claimed
    proton    8              -172u - 172         8        0        8       4
    neutron   2              -34u - 34           2        0        2       —
    deuteron  192            -8544u - 8544     192        0      192     -32

`a₁(-1) = 0` holds — that half of the docstring was right. But **a₀ is a
CONSTANT** in every case, so *"a₀(u) evaluated at u=-1 gives 4"* cannot be true
at any evaluation point: `a₀ = 8` identically. Checked two independent ways
(own exact `Fraction` parser; Python's evaluator on the raw strings) in
[`habiro_collapse_constant_probe.py`](computations/probes/habiro_collapse_constant_probe.py).
Integers and Fractions throughout, no floats. Corrected in `d95309bfba` — in the
STATEMENTS, not just docstrings, since the theorems are named "QOU
proton/deuteron instance" and a wrong constant makes the name a mislabel.

Two more things fall out of the same table:

* The docstring claimed "C = 4 for the proton **and neutron**". They do not
  share a constant: 8 and 2.
* `tr_M` carries a denominator (`denom(-1)` = 16 / 4 / 1536). Dividing through,
  proton and neutron **both** collapse to `1/2`, the deuteron to `1/8` — not
  integers, and **the collapse does not separate proton from neutron**. For a
  quantity meant to carry nucleon-specific content that is a bigger problem
  than the numerals.

## The witness cited as `status: "verified"` never tested the collapse

`habiro-frobenius-probe.witness.json` backs the block
`rem:qou-motivic-galois-instance` with `status: "verified"`. What its
`step2_compatibility_passed` actually asserts is that the **Galois norm is an
integer** — not that anything equals a constant. Its recorded traces are nine
different values per atom (proton: -16, -2, 2, -8, 14, 5, 9, -8, -31; deuteron:
192, -9, -61, 23, -756, -525, 1162, 873, 134), `trace mod p` is not constant
either (proton: 0,1,2,6,3,5,9,11,15), and **neither 4 nor -32 occurs anywhere in
the file**. `galois_trace_full_is_integer` is `false` at every prime, and
`step2_full_trace_compatible` is `false` for every atom.

So "verified" is true of what the probe checks and not of what the Lean assumes.
Worth generalising: a `computation.status: "verified"` on a block says a script
ran and its own assertions passed. It does **not** say the script tested the
proposition the block states, and nothing checks that it does.

## Where this leaves the bean — still open, unchanged in direction

Correcting 4 -> 8 does **not** rescue the route and is not offered as doing so.
With C = 8 the residue is still a unit in `F_p` for every odd p, so the
cyclotomic-unit refutation applies verbatim; and there is still no ring hom
`ℤ[ζ_2p] →+* ℤ` for `reduce` to be. The constants are fixed because they were
wrong.

The archimedean route is untouched by this pass and remains the candidate: a
unit of `O` has norm ±1, so a lower bound on `|Frob_p|` at every complex
embedding would bound `|N(Frob_p)| > 1`. The witness records `abs_frob` at one
embedding per prime and it is frequently **< 1** (proton at p=11: 0.046;
deuteron at p=13: 0.033), which is not itself an obstacle — conjugates of a
non-unit may individually be small — but it does mean the bound has to be over
the whole orbit, and the data as recorded is one embedding, not the orbit.


---

# 2026-08-25 — the block never claimed non-unitness; it claims NON-VANISHING

Picked up from a stalled session (branch `claude/agent-stalled-discussion-iyeuqp`,
PR #5769) that had read the block's sketch and stopped mid-edit.

## The distinction this bean was missing

Every pass on this bean, mine included, has been trying to prove the QOU
Frobenius is a **non-unit**. Read the block:

> If `χ(A) ≠ 0`, then `χ^mot_A` is **non-trivial** at every finite place `p`
> with `p ∤ χ(A)`.

and its sketch's last step:

> a Frobenius character whose trace equals `χ(A) mod p`. Because `p ∤ χ(A)`,
> this trace is **non-zero** modulo `p`. The character is non-trivial.

**The block asks for NON-VANISHING. It never asks for non-unitness.** Over a
field those are not the same property and they point opposite ways — a unit is
precisely a nonzero element. `motivic_perpetual_obstruction`,
`motivic_perpetual_obstruction_frobenius` and `habiro_frobenius_not_unit` all
conclude `¬IsUnit`; none of them states what the block states.

## The refutation is untouched — and it is the affirmative answer

The scope-(b) exclusion recorded above stands verbatim: a congruence to a fixed
constant `C` gives non-unitness only at the primes dividing `C`, and
`isUnit_four_zmod` is why.

That same fact settles the block's actual claim **positively**. `IsUnit` in
`ZMod p` implies `≠ 0`. So exactly where the non-unit reading dies, the
non-vanishing reading lives — and it lives in the perpetual shape: at every
prime above `|χ(A)|`.

The route was never dead. It was answering a question the block had not asked.

## Landed

`QOU/LiftingDescent/MotivicCharacterNonvanishing.lean`, sorry-free, `#print
axioms` standard-only on all seven declarations, lean-direct exit 0:

    residue_eq_zero_iff_dvd     vanishes IFF p | χ(A) — the locus, not a bound
    residue_ne_zero_of_not_dvd  the sketch's final step, derived
    residue_ne_zero_of_gt_abs   perpetuity quantified: every prime > |χ(A)|
    ne_zero_of_isUnit_residue   the reconciliation

Per §3b-cond the substantive links are hypothesis **fields** — `chi` and
`residue_eq_chi` (the sketch's own congruence under `ρ_p`). The class carries
no non-vanishing field; `residue_eq_zero_iff_dvd` is real arithmetic
(`ZMod.intCast_zmod_eq_zero_iff_dvd`), not a projection. The witness is a
`def`, deliberately **not** an `instance`, so it cannot silently discharge a
downstream `[MotivicResidueRealization]`. It is built at `χ(A) = 8` — this
bean's own corrected proton constant — and a `decide`-checked example
witnesses **both** branches of the iff (vanishes at `p=2`, does not at `p=3`),
so the theorem separates primes rather than describing a constant.

## STILL OPEN, and unchanged

This does **not** prove `thm:motivic-perpetual-obstruction`. `residue_eq_chi`
— that the local Frobenius trace reduces to `χ(A)` mod `p` under `ρ_p` — is a
hypothesis and is not derived. The archimedean-bound route recorded above is
also untouched. What changed is which proposition the corpus should be aiming
at.

## Found alongside (fixed in `def765883`)

The `def:motivic-galois-character` sibling — which is what a reader following
the block's `lean.ref` lands on, per §0a — still declared
`almost_everywhere_nontrivial` as a **class field**, the field the library
removed 2026-08-12 because it "forced every instance to either prove it or
launder an axiom". Nothing compiles that path (Lake globs are `["QOU","QOU.+"]`
rooted at `lean/`), so it could drift indefinitely. Same family as `qou-a5dr`,
one file over, still live. Re-synced rather than deleted: a `definition` block
requires its sibling.


---

# 2026-08-25 (second pass) — the archimedean route is UNBLOCKED, and by what

Attempted the archimedean route this bean named. It supplies the algebraic
half; the estimate is still open. `QOU/LiftingDescent/FrobeniusNormRoute.lean`,
sorry-free, eight declarations, `#print axioms` standard-only.

## The refutation is about RING homs, and about FIELDS

Re-reading this bean's own two facts:

* no ring hom `ℤ[ζ_2p] →+* ℤ` exists at all;
* with target `𝔽_p` the residue is a **unit** whenever `p ∤ C`.

Both are statements about **ring** homomorphisms and about **fields**. The
field norm is neither. `Algebra.norm ℤ : S →* ℤ` is a `MonoidHom` — multiplicative
only, `N(x+y) ≠ N(x)+N(y)` — so its existence is untouched by the first; and
`ℤ` is **not a field**, so `|N| ≥ 2` is a genuine non-unit, untouched by the
second.

That asymmetry is why this route is open when the other is closed. I had been
reading the refutation as closing "transfer non-unitness backwards along a map
to ℤ" in general. It closes it only for **ring** maps into **fields**.

## Proved in a computable model, not asserted

`ℤ[i]` has the same shape as `ℤ[ζ_2p]` here — rank-2 free over `ℤ`, generated
by a root of an integer polynomial with no rational root — and is `decide`-able:

    no_ringHom_gaussianInt_to_int   NO ring hom ℤ[i] →+* ℤ (i would go to an
                                    integer square root of −1)
    one_add_i_not_isUnit            and the norm route goes through anyway:
                                    1+i is a non-unit, via Zsqrtd.normMonoidHom

`IsUnit` is not decidable, so `decide` cannot prove the second; it discharges
only `1 < |N(1+i)| = 2` and the criterion does the rest. The norm is what makes
the statement reachable.

Also `not_isUnit_iff_eq_zero_groupWithZero`: in a group with zero a non-unit is
exactly zero. That is the general fact `isUnit_four_zmod` is an instance of —
the cap is *every nonzero element being invertible*, not anything about
residues or primes — and `ℤ` escapes it by not being one.

`frobenius_not_unit_of_norm_bound` carries the perpetual shape: **no exception
set**, every prime rather than all but finitely many.

## STILL OPEN — the estimate, and it is the hard half

The archimedean bound is an explicit hypothesis, **not** established. And the
data recorded so far cannot supply it: `habiro-frobenius-probe.witness.json`
gives `abs_frob` at **one** embedding per prime, frequently `< 1` (proton at
`p = 11`: `0.046`), while the bound required is on the product over the **whole**
embedding orbit. A single small conjugate is no obstacle — conjugates of a
non-unit may individually be small — but one embedding is not an orbit.

So the next concrete step is a producer that emits the **full conjugate orbit**
per prime, not a single embedding. That is a compute task, not a Lean one, and
it is what would turn the hypothesis into a theorem.


---

# 2026-08-25 (third pass) — the archimedean route is REFUTED at p=3. Frob_3 is a unit.

Built the conjugate-orbit producer this bean called for
(`habiro_frobenius_conjugate_orbit_probe.py`). It answers the question and the
answer is **no**.

## Two corrections to this bean's own framing, before the result

1. **The orbit producer already existed.** `habiro_frobenius_norm_probe.py`
   computes the full orbit product and has a committed witness (#5745). This
   bean's *"the data as recorded is one embedding, not the orbit"* is true of
   `habiro-frobenius-probe.witness.json` — the **trace** probe — and false of
   the norm probe. My previous pass recommended building it from scratch; that
   was wrong and the corpus-grep caught it before any code was written.
2. **That producer preferred DEPRECATED coefficients.** It read
   `WITNESS_FAST if WITNESS_FAST.exists() else WITNESS_SYMBOLIC`, and
   `_deprecated/habiro-coefficients-atomic-fast.witness.json` exists. The two
   datasets disagree at `a₀` itself — neutron **8 vs 2**, deuteron **96 vs
   192** — and 2 / 192 are the values *this bean* corrected the corpus to on
   2026-08-23. Fixed to canonical-only; the source path is now recorded in the
   witness.

Also: **the committed norm witness reproduces from nothing on `main`.** All 7
of its exact rows differ from a recomputation against *either* dataset, and it
reports `route_a_supported: true`, `n_unit: 0`.

## The result

Canonical coefficients, exact integer arithmetic:

    atom        p=2                    p=3
    proton      N = 64    (= 8^2)      N = 1     <-- UNIT
    neutron     N = 4     (= 2^2)      N = 1     <-- UNIT
    deuteron    N = 36864 (= 192^2)    N = 171

A unit of `O` has norm `±1`. So **`Frob_3` is a unit for both nucleons**, and
`not_isUnit_of_natAbs_norm_ne_one`'s hypothesis `1 < |N(frob p)|` is **false**
there. The no-exception-set form — `∀ p, ¬IsUnit (frob p)`, which is what
`habiro_frobenius_not_unit` and `frobenius_not_unit_of_norm_bound` assert — has
an explicit counterexample at the smallest odd prime.

## Scope: (a) not (b)

A **counterexample to the ∀-form**, not a structural exclusion of the norm
route. One prime is not a positive density, so the **almost-every-prime form is
untouched and is NOT refuted**. What dies is the version with no exception set —
which is, however, the form the Lean carries.

## Three independent checks

1. orbit product vs **resultant** `Res(Φ_2p, f)` — no shared code path, agree on
   every row; the probe **raises** on disagreement rather than reporting it;
2. at `p=2` the representative collapses to a rational integer equal to the
   **collapse constant** (8 / 2 / 192) and the norm is exactly its square,
   forced by degree 2 — corroboration from a different witness;
3. the pre-existing probe, with **only** its input source corrected, flips its
   own verdict from "Route A SUPPORTED" to **"Route A BLOCKED — found unit
   Frobenius"**.

## What is still open

Exactness is bounded by **data**, not method: evaluating at `p` needs `2p+1`
coefficients. With 9/9/14 this reaches `p ≤ 3` for the nucleons, `p ≤ 5` for the
deuteron. The honest open question is now narrower and sharper than "does the
norm route work":

**Is `p = 3` an isolated exception, or do units recur?** That decides between
"drop perpetuity, keep an exception set" and "the norm route is dead". It needs
canonical coefficients beyond index 14 — `_deprecated/` has T (19) and ³He (20),
enough for `p = 7`, but they are the superseded dataset and must not be used.
So the next step is **generating canonical coefficients further out**, not more
Lean.


---

# 2026-08-25 (fourth pass) — the coefficient ceiling is PERMANENT; retracting my own next step

Last pass I wrote that the next step was "generating canonical coefficients
further out". **For the nucleons that is impossible, not expensive**, and the
producer says so in its own docstring.

## Why there are no more coefficients

`cyclotomic_expansion` terminates when the running remainder hits zero — *"if p
has finite degree this happens at some `m_max ~ sqrt(2*deg p)`"*. `tr_M` is a
Laurent polynomial of finite degree, so the Habiro expansion is **finite**. All
three atoms returned FEWER than `max_m=20` (9, 9, 14), so none was truncated by
the cap: **all three terminated naturally**. The proton's Habiro element *has*
nine coefficients. There is nothing to generate.

## The reachability table is therefore fixed for good

Evaluating the orbit at prime `p` needs `2p+1` coefficients:

    proton, neutron    9 coeffs   ->  p in {2, 3}        <- PERMANENT CEILING
    deuteron          14 coeffs   ->  p in {2, 3, 5}
    T, 3He         ~19-20 coeffs  ->  p in {2, 3, 5, 7}

So **"is the p=3 unit isolated?" is UNANSWERABLE for the nucleons by this
method** — permanently, not pending compute. It is answerable only up to `p=7`,
only for T and ³He, and those two need a container with **numpy** (absent here).

That is a much narrower question than the one I posed, and it changes what a
positive answer could even mean: no amount of work makes the *nucleon* norm
route testable past `p=3`, where it is already known to fail.

## A destructive producer defect, found by walking into it

Running the producer with `HABIRO_WITH_A3=1` here (no numpy) made every atom
raise — and **it wrote the witness anyway**, replacing all three atoms with
error stubs: `n_coeffs` 9/9/14 → **0/0/0**, 32 exact coefficients destroyed in
the file backing `def:habiro-ring` and calibrating α_M for the deuteron.
Recovered from git (byte-identical to a backup taken first).

The merge-preserve guard read `if _label not in results and "error" not in
_entry`. A *failing* atom IS in `results`, carrying an `error`, so the good
prior lost to the stub. Its own comment — "freshly computed cases always win" —
is right; a failed case was never computed, and that is the case it did not
distinguish. Fixed in `001866f43b` and **tested by reproducing** the loss, not
by inspection.

Not fixed, and recorded rather than left silent: a failed atom is still written
as an error stub, so a degraded run adds empty atoms to the witness. Harmless
to consumers but it misrepresents scope.

## What is actually next

Not more Lean, and not "generate coefficients". Either:

1. **Run the A3 atoms in a numpy container** — the one remaining measurement
   that can move this, reaching `p=7` for T and ³He; or
2. **Accept the exception set.** The `for-all p` form is refuted at `p=3` and
   cannot be rescued for the nucleons. If the framework wants a perpetual
   obstruction it needs a different invariant, not more primes of this one.


---

# 2026-08-25 (fifth pass) — Frob_3 IS zeta_6. The refutation is an identity, not an estimate.

Sharpened the p=3 refutation while an A3 compute ran. The sharpening is itself
the strongest available check on it.

## The prediction, and why it is a real test

`N(Frob_3) = 1` forces `Frob_3` to be a **unit of `Z[zeta_6]`** — the Eisenstein
integers, whose unit group is *exactly* the six roots of unity. So the norm
result is not a soft number: it constrains the element to **six specific values
out of an infinite ring**. A mis-computed norm would almost certainly land
outside the six.

## The result

    proton     Frob_3 = u = zeta_6,   order exactly 6
    neutron    Frob_3 = u = zeta_6,   order exactly 6
    deuteron   Frob_3 = 15 - 6u,      no finite order (non-unit, N = 171)

Not merely a unit — the **primitive** 6th root of unity (order exactly 6, not a
proper divisor), and **the same element for both nucleons**, whose coefficient
sequences are entirely different (`a_0` = 8 vs 2, every `a_1..a_8` distinct).

Tested by the **defining property**, not by list membership: the check powers
the element up and reports its multiplicative order. An srepr comparison against
a hand-built set of roots of unity would pass on a representation artifact and
say nothing about the algebra. The deuteron is the control — same loop, no
order returned.

## Why this changes the standing of the refutation

"N = 1" reads as a near-miss a sharper estimate might overturn. **"Frob_3 =
zeta_6 exactly, order 6" cannot be overturned by any estimate** — it is an
identity. The archimedean hypothesis is not unproved at `p=3`; it is *false*
there, by exact computation.

It also says the failure is **structural, not accidental**: the Frobenius at
`p=3` is torsion in the unit group, and it is the *same* torsion element for two
different nucleons. That is a fact worth explaining in its own right, and it is
not explained here.

Scope unchanged, still **(a)**: a counterexample to the `for-all p` form, not to
the almost-every-prime form.

## Open question this raises (new, and possibly more interesting than the bean)

Why do two atoms with different Habiro coefficients collapse to the *same*
primitive root of unity at `q = zeta_6`? If that is forced by the structure
rather than coincidental, it is a statement about the Habiro element at roots of
unity that nothing in the corpus currently makes. Not pursued here.


---

# 2026-08-25 (sixth pass) — A=3 is 18 DAYS in sympy. The owner was right about Rust.

Measured the thing I had been recommending, and it is not viable. Third
correction to my own recommendation on this front; the pattern is recorded
below because it matters more than any single number.

## The measurement

The symbolic chi cache is per-partition and resumable
(`per_irrep_pole_atom.py tritium`). Two completed partitions give a clean
cost law:

    lambda = (9)     dim   1     3.9 s
    lambda = (8,1)   dim   8   276.1 s      (dim^2 predicts 250 s)

A `dim^2` fit on two independent points, matching the Rust docstring's stated
`O(dim^2 * k)`. Unit cost **4.31 s per dim^2**.

Partitions of 9 have `sum dim^2 = 9! = 362,880`, so the total is
**1,564,920 s = 18.1 DAYS** of CPU. The worst single partition,
`(4,3,1,1)` at dim 216, is **55.9 hours on its own**.

So the "resumable grind" I recommended one pass ago is resumable and
**infeasible**. Four workers does not rescue an 18-day serial total.

## What this does to the options

| route | verdict |
|---|---|
| sympy symbolic chi (the cache) | **18 days** — dead |
| word-expansion + exact word characters | `2^19` words for tritium — dead |
| Geck-Pfeiffer exact q-characters | crate documents it "structurally incomplete at q != 1" — our regime |
| **Rust exact seminormal over Q(q)** | the only live route |

The owner's instinct — *"A=3 should not be out of reach... using rust?"* — is
**correct, and now quantified**: 18 days of sympy is exactly the gap a compiled
exact-arithmetic implementation closes. The same doc that gives the cost law
says `chi_q_atomic` is "<< 1 s in release-optimised Rust for typical atomic
braids" at f64.

## What the Rust build actually requires (measured, not assumed)

NOT a coefficient-type swap, which is what I originally proposed:

1. **A gauge change to remove the square root.** Hoefsmit's symmetric form is
   `[[a, b], [b, a']]` with `b = sqrt(a a' + 1)`; the trace-invariant
   asymmetric form `[[a, b^2], [1, a']]` is rational. `seminormal.rs:275` is
   the `sqrt` in question.
2. **A genuine `Q(q)` fraction field with polynomial gcd.** Intermediate
   entries carry denominators `1 + q^2 + ... + q^{2(rho-1)}`: verified `a = q`
   at `rho = 1` but `q^3/(q^2+1)` at `rho = 2`, and n=9 reaches `rho = 8`.
   `LaurentRationalQ` holds Laurent polynomials, **not** quotients.

The OUTPUT type is fine — cached characters are Laurent with rational
coefficients (denominators `768 q^7`, `192 q^5`: integer times monomial), which
`LaurentRationalQ` represents exactly. The denominators cancel in the trace.
So the target was right and the route was wrong.

## The pattern, recorded because it is the lesson

Three recommendations on this front, three corrections:

1. "generate more coefficients" — impossible; the expansion terminates.
2. "extend chi_q_atomic to LaurentQ" — the intermediates are not Laurent.
3. "finish the cache, it is a resumable grind" — 18 days.

Each was stated before measuring the thing that killed it. The measurements
were all cheap: a docstring, eight symbolic `cancel` calls, and two cache
timings. **Measure the cost law before recommending a route**, especially when
recommending against the one the owner proposed.


---

# 2026-08-25 (seventh pass) — the partial cache is worth NOTHING, not "some progress"

Sharpening my own framing from the sixth pass, because it was too generous to a
route I had already called dead.

I described the chi cache as "resumable — every run banks progress permanently"
and left it running on that basis. **The banked partitions have zero usable
value.** `tr_M = sum_lambda y_lambda * chi^lambda` is a sum over ALL 30
partitions of 9. With 29 of 30 you cannot form the trace, so you cannot run the
Habiro expansion, so you get no coefficients and no p=7 answer.

The cache route is therefore not "18 days with partial payoff along the way".
It is **all-or-nothing at 18 days**. Resumability protects the investment; it
does not produce anything until the last partition lands, and the last
partitions are the 56-hour ones.

Consequence: there is no reason to leave the cache grinding as a background
hedge, which is what I was doing. It was killed by a container restart at
2/30 and is deliberately NOT restarted.

This does not change the verdict from the sixth pass, it removes the last
reason to hedge against it: the Rust exact-arithmetic route is not merely the
better option, it is the only one that produces anything at all.


---

# 2026-08-25 (eighth pass) — the exact route is PROVED. The Rust port is now mechanical.

The blocker I scoped as "needs a `Q(q)` fraction field with polynomial gcd" is
gone, and my scoping was wrong in a specific way worth naming.

**The square root was the whole problem, and it is a gauge artifact.** Hoefsmit's
SYMMETRIC seminormal form carries `b = sqrt(a a' + 1)` off-diagonal
(`seminormal.rs:275`) — irrational, hence the Rust chi path being f64/mpfr only.
The trace-invariant ASYMMETRIC gauge `[[a, b^2], [1, a']]` is rational. Verified
on all 15 shapes for n=3,4,5: Hecke quadratic, braid, far-commutation and equal
traces.

With the sqrt gone, and with `delta` rational, **every quantity in the atom is
rational in q**, so the whole computation runs in exact `Fraction` /
`BigRational` arithmetic — **no fraction field needed**. That was the expensive
half of my earlier estimate and it does not exist.

Proved end to end in `probes/exact_rational_chi_gauge_probe.py`: all 11 cached
deuteron characters reproduced exactly at three independent rational `q`.

## What remains for the Rust port

Mechanical translation, not research:
1. `blocks_at` with `BigRational` instead of `f64` — the asymmetric gauge.
2. `chi_at` — per-basis-vector trace, already the shape `chi_q_atomic` uses.
3. Evaluate at `deg + 1` rational points and interpolate. Interpolation is
   standard and is the one piece not yet written or tested.

The 18-day sympy figure is a cost of SYMBOLIC MANIPULATION, not of the
mathematics: the same arithmetic in exact integers is `O(dim^2 * k)` per
evaluation point with no expression swell.

**Not claimed:** any A=3 timing. That needs the port and a measurement.

## 2026-08-25 — THE A=3 DOOR IS OPEN. It was a routing choice, not a wall.

**A=3 Habiro coefficients now computed for helium-3 AND tritium, in
seconds.** Producer:
`computations/habiro/habiro_coefficients_a3_via_peel.py`, witness
`habiro-coefficients-a3-via-peel.witness.json`, 16 assertions all passed.

    helium-3   n=9  deg_u(p)=144   a_0..a_16   trace 2.1 s  cancel 2.6 s
    tritium    n=9  deg_u(p)=136   a_0..a_16   trace 4.4 s  cancel 5.7 s

### What was actually wrong

`habiro_coefficients_atomic.py` gets `tr_M` from `markov_trace_symbolic`,
which sums `y_λ · χ^λ` over every partition of `3A` — 30 partitions at
A=3, irreps to dim 216. I measured that at 4.31 s/dim², i.e. **18.1
days**, and that measurement is what closed the door.

`markov_peel.tr_M_atomic` reaches the *same object* by reducing the braid
word in the Hecke NF basis (256 terms at A=3) and tracing by recursive
ascent — no partition sum at all. **1.8 s.**

Deuteron, both routes, same machine: **0.23 s vs 39.74 s** (173×). At A=3
that ratio is what separates 2 seconds from 18 days.

They are not merely close. `sp.cancel(peel − partition_sum) == 0`
**exactly**, proton and deuteron — a symbolic identity, asserted in the
witness.

### My Rust work solved a problem that did not need solving

`seminormal_exact.rs` (exact BigRational χ via the asymmetric gauge) plus
the A=3 cost benches were built to feed an interpolation route: ~157
evaluation points at ~25 s each, ~66 min. All of that is **unnecessary**
for A=3. The measurement was sound and the code is correct and tested;
the *motivation* is gone. Keeping it — it is a genuine exact-arithmetic
capability with no square root — but it should not be described as the
route that opened A=3. It didn't.

Root cause of the detour: I measured the cost of the route the producer
happened to use, then optimised *that route*, instead of first asking
whether it was the right one. Five separate things I was about to build
this session already existed. The corpus-grep discipline is written for
declaring items open; it applies just as much before starting to build.

### Two traps, both caught only by validating on the deuteron first

**1. `to_u_polynomial` does not cancel, and the peel returns an
UNREDUCED fraction.** Without `sp.cancel` the deuteron comes out with
`deg_u(p) = 108` instead of 100 and denominator `192·u⁴⁶(u⁴+1)⁵` instead
of `(u⁴+1)³` — a spurious `(q²+1)²`. Every `a_m` is then wrong, **and
`reconstruction_matches` still reports True**, because reconstruction
only checks `p = Σ a_m (u;u)_m`, which holds for the wrong `p` too. A
self-consistent wrong answer. I had already printed the bad A=3
coefficients before catching it.

**2. sympy symbol assumptions, second occurrence this session.**
`sp.sympify("u**100 + …")` mints a bare `Symbol('u')`; my `Symbol('u',
positive=True)` is a *different symbol*, so the difference never
simplifies to zero and the comparison reports a mismatch that is not
there. I briefly believed the peel disagreed with the committed
deuteron. It does not — `p_in_u`, `denom_in_u` and **all 14 `a_m` are
identical**. Parse with `locals={'u': U}`. The producer's `_sym()` helper
exists exactly for this and says why.

### What is NOT established

The A=3 values have **no independent second computation** — there is
none, because the partition route *is* the 18-day path. Their warrant is
that the same code path reproduces every committed A≤2 value exactly
(p_in_u, denom, and every a_m, for proton / neutron / deuteron) and that
the two routes are symbolically identical wherever both can run. Recorded
as a caveat in the witness rather than left implicit.

### Next

A=4 (⁴He) is the obvious follow-on — the peel witness already lists it as
covered numerically, and tritium at 4.4 s suggests headroom. Cost is not
yet measured, so do not assume it.

## 2026-08-25 (cont.) — it does not stop at A=3. Proton through lithium-6.

Having found the route, I measured how far it goes rather than assuming.
All four higher atoms complete with **exact reconstruction**:

| atom | A | n | deg_u(p) | a_m | tr_M | cancel |
|---|---|---|---|---|---|---|
| helium-3  | 3 |  9 | 144 | a_0..a_16 |    1.8 s |   2.6 s |
| tritium   | 3 |  9 | 136 | a_0..a_16 |    3.8 s |   5.7 s |
| helium-4  | 4 | 12 | 180 | a_0..a_18 |   24.6 s |  18.6 s |
| helium-5  | 5 | 15 | 216 | a_0..a_20 |  325 s   |  84 s   |
| lithium-6 | 6 | 18 | 260 | a_0..a_22 | 2036 s   | 212 s   |

Denominators keep the peel law: `49152·u¹¹⁰(u⁴+1)¹¹` at A=6.

**The growth FLATTENS.** Step ratios are 13.7×, 13.2×, **6.3×**. I
extrapolated A=6 at ~70 min from the 13× figure and it came in at **38**.
That wrong extrapolation is recorded in the module docstring next to the
measured table, with an explicit "do not extrapolate A=7 from 13× either —
measure it."

Producer covers A=1..6 behind `--max-a` (default 4, the whole set in about
a minute; the committed witness is the default run so a plain re-run
reproduces it byte-for-byte).

For scale: the route this replaces was measured at **18.1 days for A=3**.

### Still open / next

- **A=7+** unmeasured. Do not guess from the ratios above.
- The A≥3 values still have **no independent second computation** — the
  partition route *is* the 18-day path. Warrant remains exact reproduction
  of every committed A≤2 value through the same code path.
- Whether `habiro_coefficients_atomic.py` itself should switch to the peel
  route is a **separate** call: the two are symbolically identical, so it
  is safe, but it changes which code path produces the committed
  A≤2 witnesses and should be scoped deliberately rather than slipped in.


## 2026-10-10 — pointer

Tracked under the in-scope list (not merged) of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.

## Progress (PR #8189, 2026-11-16T20:28:25Z)

- [x] Restated `perpetual_obstruction_from_collapse_invariant`, `qou_proton_perpetual_obstruction`, `qou_neutron_perpetual_obstruction`, and `qou_deuteron_perpetual_obstruction` in `folio/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicPerpetualObstructionFromTrace.lean` using `habiroPrimeCollapse` so the conclusion genuinely evaluates the `p`-indexed Habiro prime-ideal collapse functional at `p` via `perpetual_obstruction_from_trace`.
- [x] Verified with Lean v4.24.0 (`lean -DautoImplicit=false -s 65536`: 0 errors, 0 warnings, 0 `sorry`) and all 6 static vacuity audits (0 findings).
- [x] Verified with 80-dps `mpmath` probe (`computations/probes/round50_devacuify_6qbv_probe.py`) and 2-commit stamped witness (`computations/probes/round50-devacuify-6qbv.witness.json`, `scriptCommitSha: 357a63280dd6b77b067855dfd2ebaeb6340b2c28`, `scriptHash: 3ff73a87c2af`).
- [ ] Awaiting review and merge of PR https://github.com/litlfred/qou/pull/8189 (`status: in-progress` maintained per repo rule).
