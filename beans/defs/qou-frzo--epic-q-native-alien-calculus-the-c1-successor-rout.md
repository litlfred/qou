---
# qou-frzo
title: 'EPIC: q-native alien calculus — the C1 successor route the RSZ closure names'
status: todo
type: epic
priority: normal
created_at: 2026-09-07T06:24:35Z
updated_at: 2026-11-15T13:30:00Z
parent: b9cj
---

Owner directive 2026-09-07: *"Take up idle as relevant. Do q-native alien calculus.
What is workplan. Bean up and roast."*

Parent of `qou-wgnx` and `qou-odh5` (both taken up today; both were ~30 d idle with
`status: in-progress`). Successor to the RSZ slope-½ chain closed 2026-08-08.

---

# 🔥 THE ROAST — written BEFORE the plan, so the plan has to survive it

Owner asked for a roast. Standing critical-distance licence, applied to my own
proposal. **Seven objections, ordered by how likely they are to kill it.**

## R1. The corpus has a LOT of alien machinery, and that is a reason for suspicion, not comfort

`AlienDerivation.lean`, `AlienBridgeEquation.lean` (13 thms), `QAlienBridgeEquation.lean`
(~25 thms), `BorelLaplace`, `BorelWatson*` (×8), `BorelSingularity`, `QBorelResummation`
(14 thms). That is a large, mostly sorry-free surface built over months.

**And the arc it serves has produced no wired result.** If that much machinery has not
moved a single L2 number, the bottleneck is not more machinery. A plan whose first
instinct is "build more Lean" is answering the question the corpus has already
answered five times over.

**The `qbs4` scrap text says this in the corpus's own words:** *"not a session brick."*

## R2. The classical bricks may be worse than useless — they are ATTRACTIVE and WRONG

The closure audit is explicit that C1 **cannot** be confluenced to the classical
setting and handed to Écalle. So every classical-only brick in the list above is a
**trap**: it compiles, it is sorry-free, it looks applicable, and it silently assumes
a limit that does not exist here.

This is the exact failure this session already committed twice at smaller scale —
`RamifiedShiftCalculus` cited as absent while present, and the RSZ chain cited as live
while retired. **A sorry-free Lean file is not evidence that it applies to your
object.** Until each brick is triaged q-native vs classical-only, the machinery count
is a liability.

## R3. The one concrete alien number rests on an unsupported identification

`A_ω = 4√2·e^{−3/8}` at `ω₀ = 1/√2`, `A₂ = 1/4` — probe-verified and explicitly **NOT
wired**. Bean `qou-q3np` records that the `A_ω → S` identification is
**literature-unsupported**, and AGENTS.md §13a cites that bean as the type case of a
conjecture that must not be closed.

So the headline datum is a number in search of a theorem. Wiring it would be exactly
the laundering the anti-fit rules forbid.

## R4. ANTI-FIT is the hardest constraint here, and alien calculus is the most fit-prone place in the corpus

`qou-qbs4`'s own scrap text: *"ANTI-FIT (hard). `U` must be DERIVED. Two constants
tuned so a downstream number lands is a fit, must be labelled one, and may NOT be
wired as canonical. The Q_β `Φ₂` precedent — the forbidden seventh ansatz — applies
directly."*

Alien calculus **produces Stokes constants**. Its whole output shape is "a small number
of constants that fix the resummation." That is the shape the corpus has ruled against
six times on Δ_λ. **The route's natural deliverable is the corpus's forbidden object.**
Any plan must say up front how a derived constant is distinguished from a fitted one —
and if it cannot, the plan is a fit generator.

## R5. The motivation cites a scoreboard that is 0/5

`qou-odh5`: *"the c₃ closure is the shared root of three of the five L2 misses."*
But AGENTS.md records the honest L2 count as **0/5 unconditional parameter-free** —
the single "scoreable win" is truncation-fitted and α_em-`sorry`-conditional.

So "closing c₃ fixes 3 of 5" is a claim about a denominator that does not survive its
own audit. The motivation is inherited from a framing the corpus has since corrected.
**Not fatal — c₃ may still be worth closing — but the stated payoff is overstated and
must not be repeated in a PR body.**

## R6. My own track record on the adjacent problem, this session

I closed **five** routes to `REV` (extensivity, cumulant expansion, polynomial `Var`,
palindromicity, spectrum limit-shape) and cracked none. `REV` is a **vastly** smaller
problem than q-native alien calculus: one scalar sequence, exact combinatorics
available, no new formalism required.

**A plan that treats q-native alien calculus as tractable in the same sessions that
could not settle `REV` is not calibrated.**

## R7. "q-native" has no agreed definition here, and that is where the plan will rot

Nobody has said what would COUNT as a q-native alien derivation. Without a falsifiable
acceptance criterion, the work drifts into "build q-analogues of classical lemmas
until something looks like Écalle" — months of sorry-free Lean that nothing consumes,
which is R1 again one level down.

**The first deliverable must be the acceptance criterion, not a lemma.**

---

## What survives the roast

Not nothing, and the honest residue is narrow:

- **The negative is solid.** RSZ is closed for a stated, checkable reason (§3.3 is
  integral-slope-only). That is real and already banked.
- **The direction is the corpus's own**, not mine: the closure audit argues alien
  derivations need no slope filtration, which is precisely why they survive where RSZ
  died.
- **`REV` is genuinely Borel-plane structure**, so the deuteron work and this arc do
  meet — that convergence was measured today, not asserted.

**Therefore the plan below is deliberately NOT "build q-native alien calculus."** It is
the smallest sequence that would tell us whether that is even the right target, with
each step falsifiable and cheap, and with the anti-fit gate stated before any constant
is computed. Plan follows in the next update, after the corpus-grep returns.


---

# The acceptance criterion for "q-native" (R7's demand, answered first)

R7 says the plan rots without a falsifiable definition of the target. So here it is,
**before any lemma**. A construction counts as a **q-native alien derivation** iff all
four hold:

**(A) Domain.** It is defined for a q-Gevrey series of the corpus's actual class —
`deg_q(c_n) = n²` (proved for C1, `C1InfDegreeLaw`) — and **not merely** for classical
Gevrey-1. A construction that needs `n!`-type growth is classical machinery wearing a
`q`.

**(B) Twisted Leibniz.** Its product rule is stated and proved for the **σ-twisted**
product — `Δ(fg) = Δ(f)·g + σ(f)·Δ(g)` with `σ` the q-shift `f(z) ↦ f(qz)` — not the
untwisted classical rule. The classical rule must be recovered only in a limit the
construction never takes.

**(C) Commutation with the q-difference operator, not `d/dz`.** Classically the
alien derivative is normalised so `Δ̇_ω = e^{−ωz}Δ_ω` commutes with `d/dz`. The
q-native statement must commute (up to the analogous twist) with `σ_q`. **This is the
criterion that RSZ failed** — its machinery is filtration-based, and the closure audit's
whole point is that alien derivations need no filtration.

**(D) No archimedean or confluence dependence in the import cone.** MECHANICALLY
CHECKABLE, and this is the one that makes the criterion real rather than rhetorical:
nothing in the cone may assume continuity in `z`, a `q → 1` limit, or a classical
Borel-plane geometry. The closure audit states C1 **cannot** be confluenced, so any
such dependence is a silent falsehood.

## Why (D) is the load-bearing one

(A)–(C) are mathematical judgements a reviewer must make. **(D) is a static analysis a
script can run**, and it converts R2 — "the classical bricks are attractive and wrong" —
from a worry into a measurement.

That gives the epic its first brick, and it is deliberately **not** a formalization:

> **Brick 0 — triage the existing alien/Borel surface q-native vs classical-only, by
> import cone and by whether each statement quantifies over a q-difference operator at
> all.**

Cheap, falsifiable, no new mathematics, and it either de-risks the largest objection or
kills the route early. If Brick 0 finds the surface is classical-only, then the corpus's
"large alien machinery" is a liability rather than an asset, R1 and R2 both bite hard,
and the honest report is that this frontier is much further away than the file count
suggests.

**Note what Brick 0 is NOT:** it is not "check the files are sorry-free." They already
are. Sorry-freeness says the proofs are complete; it says nothing about whether the
statements apply to a q-difference object. That distinction is the whole of R2.


---

# BRICK 0 RESULT — and it changes the target

`scripts/alien-surface-qnative-triage.py`, run on the Lean tree.

## The population finding (my own warning, measured)

| selection | files |
|---|---|
| by **filename** | 50 |
| by **content** | 89 |
| **content-only — filename MISSED** | **40 (44 % of the surface)** |

Filename selection misses nearly half. That is the trap I fell into earlier in this
same session; it is now a number rather than a memory.

## The verdicts (90 files, criterion (D) on STATEMENTS, not proofs)

| verdict | files |
|---|---|
| Q-NATIVE-CANDIDATE | **9** |
| MIXED | 2 |
| CLASSICAL-ONLY | **18** |
| NEITHER (abstract or off-topic) | 61 |

**Twice as many classical-only as q-native.** R2 is confirmed as a measurement.

**The sharpest single row:** `QBeta/OneInstantonNormalization.lean` — the file the
closure audit names as *"already the corpus's route"* — is **CLASSICAL-ONLY**. Its
theorems are `{M Z : ℝ → ℝ}` with `HasDerivAt` **in the hypotheses**. So the successor
pointer has the same defect as the `QBorelKernelLevel` note fixed this morning: **third
instance of that class today.**

# 🛑 BUT THE MAIN FINDING INVERTS THE PLAN

`AlienDerivation` / `AlienBridgeEquation` classify NEITHER because they are **abstract**,
not vacuous — `structure AlienDerivationSystem (R A Ω : Type*)`. And on the q side:

**`QOU.Mathlib.QAlienBridgeEquation` already contains a genuinely q-native alien bridge.**

```lean
structure QBridgeSystem (R A Ω : Type*) [CommSemiring R] [CommRing A] [Algebra R A] where
  dil       : A ≃ₐ[R] A                      -- the dilation automorphism σ
  alien     : Ω → Derivation R A A
  weight    : Ω → R
  unipotent : Ω → Derivation R A A
  bridge    : ∀ ω f, conjDeriv dil (alien ω) f = weight ω • alien ω f + unipotent ω f
```

with `conjDeriv σ D = σ ∘ D ∘ σ⁻¹`. Its own docstring: *"in the q-setting the 'ordinary
operator' is an automorphism, so the relation is a **conjugation rather than a
commutator**."*

**Scored against this epic's own acceptance criteria:**

| criterion | verdict |
|---|---|
| (A) growth class | **silent** — 0 growth references, purely algebraic. `QGevreyTaming` carries this side separately (`abs_qBorel_le_of_qGevrey`, `qBorelCoeff_dilate`) |
| (B) twisted Leibniz | **PASSES** — `conjDeriv` via `σ ≃ₐ[R]`, genuine `leibniz'` |
| (C) commutes with `σ_q`, not `d/dz` | **PASSES** — bridge stated as conjugation by `dil` |
| (D) no archimedean / confluence in the cone | **PASSES** — imports only `Mathlib.RingTheory.Derivation.Basic`, `Mathlib.Tactic`, `QOU.Mathlib.AlienBridgeEquation` |

**0 sorries. And ZERO IMPORTERS.** `QBridgeSystem` appears in its own file and
`QGevreyTaming`, nowhere else. **Nothing instantiates it at any concrete object.**

## What this does to the roast

**R1 is sharpened, not refuted.** Its complaint — the machinery has moved nothing — is
confirmed in the strongest possible form: *zero importers*. But its prescription changes
completely. The problem is **not** that more theory is needed. It is that the theory
exists, passes three of four criteria, is sorry-free, and **has never been instantiated
once.**

**R7 is answered by the corpus rather than by me.** "q-native" already has a carrier
with a falsifiable shape. The criterion I wrote is satisfied by an object built months
ago.

**R2 stands and is now quantified.** 18 classical-only files, including the one the
closure audit points at.

**R4 (anti-fit) stands entirely, and moves closer.** An instance supplies `weight : Ω → R`
— the Stokes weights. That is precisely the "small set of constants" shape the corpus
has ruled against six times. The gate below is therefore not optional.

**R6 (my calibration) stands.** Providing a first instance is still real work.

# THE WORKPLAN

Not "build q-native alien calculus" — that is largely built. The target is the
**instance**, in the §3b class-with-no-instance sense.

| brick | deliverable | falsifiable by | cost |
|---|---|---|---|
| **B0** ✅ **DONE** | the triage above | script re-runs | done |
| **B1** | **Fix the stale successor pointer**: the closure audit names `OneInstantonNormalization` (classical-only) as the route. Correct it to `QAlienBridgeEquation` | grep the audit; lean-direct | small |
| **B2** | **Relate the two carriers.** `QBridgeSystem` and the abstract `BridgeSystem` have the same signature and no proved relation. Either a forgetful map or a stated reason there is none | Lean, sorry-free | small |
| **B3** | **Connect (A) to (B/C/D).** `QGevreyTaming` holds the growth side, `QBridgeSystem` the algebra, with nothing joining them. State the hypothesis under which a q-Gevrey series of class `deg_q(c_n) = n²` yields the `alien` field | Lean statement; may stay conditional | medium |
| **B4** | **THE FIRST INSTANCE.** Any concrete object. Deliberately NOT C1 first — pick the cheapest honest one (candidate: the deuteron `Z_n`, whose divisor and degree law are now derived) | an `instance` that typechecks | **the real work** |
| **B5** | Only then: read `weight` off the instance and compare to `A_ω` | — | **GATED — see below** |

## 🛑 THE ANTI-FIT GATE, stated BEFORE any constant is computed (R4)

`weight : Ω → R` **is** the Stokes-constant slot. So, binding on B5 and on anything
downstream:

1. A `weight` obtained by **choosing values so a downstream number lands** is a **fit**,
   must be labelled one, and may **NOT** be wired as canonical. This is the `Φ₂`
   seventh-ansatz precedent, which `qou-qbs4` invoked for exactly this object.
2. `A_ω = 4√2·e^{−3/8}` may **NOT** be used to *define* the instance and then reported as
   agreement. That is circular. It may only be a **cross-check computed after** the
   instance is fixed by independent data.
3. The `A_ω → S` identification is **literature-unsupported** (`qou-q3np`), so it cannot
   be a premise. AGENTS.md §13a forbids closing that bean while it is open.
4. If B4 cannot be done without choosing a constant, **the honest output is that B4 is
   blocked**, recorded as such — not an instance with a tuned field.

## What would kill this plan, stated in advance

- **B4 needs data nobody has.** If no object supplies `dil`, `alien`, `weight` from
  independently-known structure, the class stays instance-free and the route is
  *correctly* open rather than merely unattempted.
- **(A) cannot be bridged to (B/C/D).** If the `n²` growth class provably cannot produce
  a `Derivation`, B3 fails and B4 is unreachable.
- **The `Ω` index set is not determined.** `Ω` indexes the singularities; if the
  Borel-plane singularity set for the q-object is not known, `alien : Ω → …` has no
  domain. Note this is exactly where my `REV` work stalled — the deficit spectrum
  `N_n(E)` does not stabilise, and that spectrum *is* the candidate `Ω`.

That last one is the honest link between this epic and the deuteron work, and it is a
warning rather than a synergy: **the thing I failed to characterise five ways this
session is the same object this plan needs as an index set.**


---

# 🛑 CORPUS-GREP RESULT — the plan above needs three corrections, one of them fatal to B4-as-written

The grep returned after the plan was written. Three findings change it.

## C1. The objective this whole route serves DOES NOT EXIST

**There is no Stokes multiplier for C1 at `∞`** — four independent confirmations, and
this covers the **connection-matrix** multipliers too, not just the local isoformal ones:

1. the isoclinicity invariant (RSZ Thms 2.2.1 / 2.2.4 / 5.5.7, cited by number in
   `conj:qdifference-kernel-prolongation-symbol` author notes, 2026-07-20);
2. `Λ_I(M)` trivial ⇒ `H¹(E_q, Λ_I(M₀))` a point (RSZ §5);
3. DVRSZ: *"pur ⟺ une seule pente"* — `T±` are two **exponents at one slope**;
4. RSZ Thm 3.3.5's dimension formula is empty at `k = 1` — **Lean**,
   `RSZIsoformalInterface.lean:148`, `c1_infinity_isoformalDim_eq_zero`.

**So `qou-wgnx`'s target is a non-object too**, not merely dormant — and my B1 note
naming it as "the live carrier" is itself now corrected. `qou-wgnx`'s own top summary
said "open" while its entries 21–23 said the opposite; that stale summary already caused
one agent to re-derive the triviality. **I nearly became the second.**

**Consequence for B4:** it must **NOT** target C1. Aiming the first instance at an object
whose Stokes data is provably a point would produce a trivially-satisfied instance — the
`: True := trivial` failure one level up.

**One caveat, recorded by the agent who found it and never discharged:** RSZ's
constructions are for *integral* slopes; C1's is integral only *after* ramification, and
"ramify, then apply integral-slope theory" was skipped. van der Put–Reversat
(`library/afst-2007-6-16-3-665-0/`) is the non-integral text and **is held**.

## C2. My anti-fit gate item 3 was WRONG — two different objects share the glyph `A_ω`

- **even-face** `A_ω = 4√2·e^{−3/8} ≈ 3.8884` at `ω₀ = 1/√2` — the W5 datum (bean
  `qou-z4x5`, completed, body empty; content lives only in the audit).
- **odd-face** `A_ω` — the G3 keystone, candidate **integer 3** from the GGM Stokes
  matrix. **This is the one `qou-q3np` is about.**

`qou-q3np`'s obstruction is **integrality** (integer Stokes constants vs small
non-integer opposite-signed reals). **That argument does not touch `4√2·e^{−3/8}`**,
which is neither an integer nor a DT count. My gate item 3 asserted it did.

**Three sharper blocks on the W5 datum do apply**, and replace it:
1. it is a **`q = 1` object** — at `q=1` the binding EGF `e^{x+x²/2}` is entire, so there
   is **no equational Stokes phenomenon**; the resurgence is **co-equational**, and the
   literal Bridge form `Δ_ω f = A_ω·df/dz` does not apply verbatim;
2. its q-deformation is `O((q−1)²)` and bar-even (measured exponent 1.956) — *stationary
   at the classical point*, so it carries almost no substrate information at `q₀`;
3. **`m_e·A_ω = 1.987 MeV` is a hard ceiling below `B_D = 2.225 MeV`** — already a
   measured negative (`deuteron_wall_alien_resummation_probe.py`).

## C3. B0 is confirmed as the only cheap and genuinely-absent step — and it is done

Measured absences in the Lean tree: `qLaplace`, `qBorelSum`, `qBorelTransform`,
`qResurgent`, `qStokes`, `qAlien` — **zero occurrences**. Every q-native object in the
corpus is a **coefficient** statement. There is no summation operator, no sector, no
singularity support, no alien derivative acting on anything.

And in Mathlib (vendored, 6883 files): `Gevrey` **0 files**, no Borel summation (the 146
`Borel` hits are `BorelSpace`, measure theory), no q-difference. Only `Derivation` exists.

**A name trap worth recording:** `qBorelCoeff` is declared **three times with three
different divisors** — `borelCoeff = aₙ/n!`, `QBorel.qBorelCoeff = aₙ/[n]_q!`,
`QGevreyTaming.qBorelCoeff = aₙ/q^{e n}`. **The `[n]_q!` one is not the RSZ q-Borel and
cannot tame `q^{n²}` growth.** `QGevreyTaming` and `QBorelResummation` do not import each
other.

## Revised plan

| brick | status |
|---|---|
| **B0** triage | ✅ **done** |
| **B1** fix the successor pointer | ✅ **done** — but see C1: `qou-wgnx` is *also* a non-object, so the note needs a second pass |
| **B2** relate the carriers | unchanged, still small |
| **B3** join growth to algebra | unchanged |
| **B4** first instance | **MUST NOT TARGET C1** (C1). Target is now: exhibit an *analytic q-difference module* satisfying the q-bridge relation — `qou-vkg5` item 2, the whole remaining gap since 2026-08-08 |
| **B5** read `weight` | gate stands; **item 3 of the gate is replaced** by the three blocks in C2 |

**The honest scope of the whole epic, after the grep:** there is **no held literature**
doing alien calculus q-natively — six alien documents have zero q-difference hits, and
eight q-difference documents have zero alien hits. You would not be extending a
literature; you would be starting one, in a corpus where the entire existing alien
surface has **zero consumers**. That is not a reason to refuse, but it is the correct
size of the claim, and it must appear in any PR body.



## Reorganisation 2026-10-04

Now the epic for P2.RES under UMBRELLA: open conjectures (formal mathematics only).

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.
