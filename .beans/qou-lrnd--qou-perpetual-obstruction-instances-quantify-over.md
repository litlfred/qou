---
# qou-lrnd
title: QOU perpetual-obstruction instances quantify over p but conclude about a constant
status: todo
type: task
priority: normal
created_at: 2026-08-22T15:26:08Z
updated_at: 2026-08-25T19:05:00Z
---

FOUND 2026-08-22 while resolving qou-oy4r (main red on
def:qou-motivic-galois-instance). File:
content/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicPerpetualObstructionFromTrace.lean
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
