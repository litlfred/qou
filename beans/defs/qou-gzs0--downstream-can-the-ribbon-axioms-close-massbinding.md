---
# qou-gzs0
title: 'Downstream: can the ribbon axioms close mass/binding derivation gaps'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-17T01:45:48Z
updated_at: 2026-10-04T15:12:24Z
---

## 2026-08-17 — first pass: the twist reaches the mass chain, but is ONE AXIOM SHORT

Traced whether the newly-landed `BalancedCategory` twist can close a recorded
mass/binding gap. It touches a real one, and falls exactly one axiom short of
closing it. Measured, not argued.

### The chain

```
twist θ (landed)
  → [MISSING: dual compatibility θ_{X∨} = (θ_X)∨]
  → sphericality on all of C
  → qDim_conj : qDimObj(X∨) = qDimObj(X)          -- bean rtqd, OPEN
  → dim_q(λ) consistency
  → G⁻¹_{λμ} = δ·[n]_q!/(dim_q(λ)·dim(λ))          -- gram-matrix-spectral-connection
  → the mass chain
```

### The measurement

`KeystoneBalancedRibbon.lean` carries `twist`, `twist_isIso`, `twist_unit`,
`twist_naturality`, `twist_tensor` — and **no dual-compatibility field**. Grep
for `twist_dual`: empty. So what landed is **balanced, not ribbon**.

`KeystonePivotalSpherical.lean` factors `rtqd` into two named inputs:
`hTransport` (pivotal transport) and `hSpherical` (sphericality). Its only
unconditional proof of the second is `leftQDim_eq_qDimObj_of_symmetric` — the
**symmetric** case, which the framework calls the classical limit.

Ribbon = balanced **+** dual compatibility, and sphericality follows from
*ribbon*, not from balanced alone. So the twist as merged does not supply
`hSpherical` in the braided case.

### Why this is the useful answer rather than a disappointment

`rtrb`'s own note already names the missing piece: *"Next: the dual-
compatibility ribbon axiom (theta_{X*}=(theta_X)*) + connect to qDimObj
conjugation symmetry."* That was written 2026-08-02 and is precisely the field
this trace independently arrives at from the mass side.

So the gap is **one identified axiom**, not an open research question, and
closing it has a traced consumer: `dim_q` feeds `G⁻¹` feeds the mass chain.
That makes it the highest-value next Lean item on this surface.

### Scope (a) — what this does NOT claim

It does **not** claim that closing `rtqd` improves any *number*. The chain above
is a **correctness/consistency** dependency: `qDim_conj` is currently an
unproved input that the Gram-inverse formula's derivation leans on. Improving
`m_p` or the `Δ_λ` binding magnitude is a separate question, and nothing here
touches the six failed `Δ_λ` ansätze or the `c_k` ladder.

Distinguish these carefully: *"the twist closes a proof gap in the mass chain's
derivation"* is what the evidence supports. *"the twist improves mass accuracy"*
is **not**, and would be exactly the over-claim the framework's own anti-
laundering rules exist to catch.

### Next

1. Add `twist_dual` to `BalancedCategory`, promoting it to a genuine
   `RibbonCategory`.
2. Derive `hSpherical` from it in the braided case.
3. Discharge `rtqd`'s `qDim_conj` — which then no longer needs `hTransport` as
   a bare hypothesis either, if the pivotal transport also follows.

Coordinate with `rtrb` (in-progress since 2026-08-02, stale) before starting.


## 2026-08-17 — HANDOFF: RibbonCategory landed; hSpherical is the next proof, NOT started

`RibbonFromBalanced.lean` (PR #5262, `244f3cf8`) has `RibbonCategory =
BalancedCategory + twist_dual`, stated **and inhabited** (`ribbonOfSymmetric`,
lean-direct exit 0).

### What remains, precisely

`KeystonePivotalSpherical` needs `hSpherical : leftQDim X = qDimObj X`. The two
differ in exactly one factor:

```lean
qDimObj  X = η_ X Xᘁ ≫ (β_ X Xᘁ).hom ≫ ε_ X Xᘁ
leftQDim X = η_ X Xᘁ ≫ (β_ Xᘁ X).inv ≫ ε_ X Xᘁ
```

so the goal reduces to relating `(β_ X Xᘁ).hom` and `(β_ Xᘁ X).inv` *under the
coevaluation/evaluation sandwich*. In the **symmetric** case they are equal
outright (`braiding_inv_eq_hom_of_symmetric`, already proved) — which is why
proving only the symmetric case would be **zero progress**: it needs no ribbon
structure at all.

The braided case is the real theorem (ribbon ⇒ spherical, Deligne/Yetter,
Bakalov–Kirillov ch. 2). It is a string-diagram argument in which the twist
mediates: `twist_dual` is what lets `θ` be pushed across the dual so the two
sandwiches become comparable. It needs several intermediate lemmas — at
minimum a `twist`-vs-`ev`/`coev` compatibility and a slide lemma — and is a
session of work, not a tactic call.

### Do not

- Prove the symmetric case and report it as progress. It was already provable.
- Add `leftQDim_eq` as a *field* of `RibbonCategory`. That is the §3b-cond
  rule-5 self-assuming projection: the class would carry the conclusion and the
  "theorem" would be `ctx.leftQDim_eq`. `SphericalStructure` already exists as
  the honest place for the hypothesis; the job is to *derive* it.

### Two method notes, because the same error happened twice this session

1. **B1** — I claimed Mathlib lacked `LeftRigidCategory (FGModuleCat K)` having
   grepped for the declaration. `inferInstance` proved it derivable in one step.
2. **The diamond** — I committed that the `KeystonePivotalSpherical` dodge "does
   not transfer". A 10-line probe showed it transfers exactly.

Both were "X is not available / does not work" judgements reached by reasoning
about the elaborator instead of asking it. **Test first.** The probe is seconds;
the retraction costs a commit and the reader's trust.

### Scope reminder for whoever continues

This whole arc is **derivation correctness**, not accuracy. `qDim_conj` is an
unproved input the Gram-inverse derivation leans on; closing it does not move
`m_p`, `Δ_λ`, or any `c_k`. The owner's actual question — mass and binding
accuracy — is still untouched and lives in the `Δ_λ` magnitude and the `c_k`
ladder, neither of which this arc reaches.
updated_at: 2026-08-18T15:59:31Z
---


## ANSWERED: no for precision, yes for percent-level systematics (2026-08-18)

`computations/ribbon_framing_ladder_scale_probe.py` +
`ribbon-framing-ladder-scale.witness.json` (2 assertions, both pass).

### The setup

The balancing twist wired onto QuantumUniverse (qou-pkf3) forces
`theta_V = q^{1/2} . id_V` on the defining representation. Because that is a
SCALAR, a framing T on a mass-carrying object contributes exactly one factor

    weight(T) = theta^T = q^{T/2},   T integer

and that is the ONLY free parameter the ribbon layer adds to a mass or binding
evaluation. T is an integer, so the effect is a discrete LADDER.

### Q1 -- can it close the L2 gaps?  NO, by four orders of magnitude

    one framing unit = 5.35552 %   <- the ladder quantum

    Q_beta    gap 1279 ppb    ladder is    41 873x too coarse
    m_n       gap 1400 ppb    ladder is    38 254x too coarse
    Delta_pn  gap 1200 ppb    ladder is    44 629x too coarse
    L2 target  7.8 ppb        ladder is 6 866 050x too coarse

The smallest nonzero framing change overshoots every L2 gap by ~4e4. So the
ribbon axioms CANNOT supply the corrections those misses need -- not because the
axioms are wrong, but because their only adjustable parameter is quantised far
too coarsely. This is a structural prune, not a numerical failure.

Corollary worth stating: the 2.96% m_p discrepancy is ALSO unreachable. No
integer T gives 2.96% (T=1 gives 5.36%, T=0 gives 0), so framing cannot explain
that gap either.

### Q2 -- the mass path already carries a factor of exactly this shape

`canonical_mass` uses `F_Bor = |tr_M(beta_Bor)| . [3]_q! / q^3`, and

    q^-3  =  q^{T/2}  at  T = -6      EXACT match, not approximate
                                      i.e. -2 per Borromean component

The Borromean word (s1 s2^-1)^3 has writhe 0, so this factor is NOT q^writhe.
It has framing shape. Whether that is the intended reading is a question for the
corpus/owner -- I am recording an exact structural identification, NOT claiming
the derivation was framing-motivated.

If it IS a framing, the mass formula's framing is already fixed at -2 per
component and there is no free knob left. If it is NOT, then there is an
unaccounted framing DOF sitting on a 5.36% ladder, which would be a
percent-scale systematic. Either way the answer to Q1 is unchanged.

### Verdict for this bean

The ribbon axioms CANNOT close the mass/binding precision gaps. They CAN move a
result at the percent level, so a mis-set framing is a percent-scale systematic
rather than a ppb-scale knob. The L2 work stays where qou-rwhj put it: the
convention-D re-derivation (qou-cds1), not the ribbon layer.

Scope (b) on the exclusion -- it rests on a proved invariant (theta scalar =>
weight is q^{T/2} with T integer) plus arithmetic, not on a failed search.
Scope (a) on the Q2 identification, which is an observation awaiting a ruling.

## Follow-up: can T = 0 be PROVED?  No -- and that is itself a theorem

`QOU/StandardModel/FramingIsAChoice.lean` -- lean-direct exit 0, no sorry /
axiom / native_decide, #print axioms [propext] (+ Quot.sound on the two
Fin-indexed ones).

    framing_unobservable_iff_trivial_twist
        (forall T, theta^T = 1)  <->  theta = 1

So the framing is blind to T EXACTLY when the twist is trivial. At q != 1 --
the whole substrate regime, q_0 ~ 1.11 -- distinct T give distinct weights, so
the framing is OBSERVABLE. A quantity that changes the prediction cannot be
fixed by the axioms that leave it free: "T = 0" is a normalisation CONVENTION to
be declared, not a proposition to be derived. The converse is the classical
boundary (theta = 1 is q = 1), consistent with BalancedCategory.ofSymmetric.

    exists_framing_pair_distinguished
        theta != 1  =>  some framing pair is separated (sharper form)

### Where T = 0 IS derivable

    bar_invariant_forces_zero    t = -t pointwise  =>  t = 0
    bar_invariant_total_zero     hence total 0, weight 1

The bar involution negates the twist, so a SELF-CONJUGATE state has zero framing
and needs no convention at all. That is a genuine derivation of T = 0 -- on the
bar-invariant sector only (amphichirality), not for the nucleon.

### The caveat that redirects the question

Q2 above found F_Bor's /q^3 is EXACTLY q^{T/2} at T = -6. If that factor is the
framing, the mass path's operative convention is T = -6, NOT 0 -- and proving
T = 0 would CONTRADICT the working formula rather than support it.

So the target is not "prove T = 0". It is "DECLARE which framing the mass path
uses", which is a corpus/owner ruling and not a Lean obligation. This file makes
the choice visible as a choice.



## 2026-08-26 — TAKEOVER, and the stated blocker is gone

Bean was in-progress since 2026-08-17 with no movement (9 days), so taken over per the
stalled-claim rule.

**The handoff's blocker no longer holds.** It said hSpherical 'needs several intermediate
lemmas — at minimum a twist-vs-ev/coev compatibility and a slide lemma — and is a session of
work'. Those slide lemmas now exist, landed today in PR #5848 (`bfdedc68e6`):

* `QOU.MathlibExt.braiding_slide_cap_right` / `_left` — a strand crossing ANY cap
  `c : A ⊗ B ⟶ 𝟙` can be pushed off it at the cost of braiding past each leg separately.
  Nothing assumed of `c` beyond its type: no rigidity, no exact pairing.
* `braiding_slide_cup_right` / `_left` — the cup duals.
* `braiding_slide_cap_right_inv` — the inverse form, which is what produces a leftover
  braiding rather than deleting one.

That last is likely the load-bearing one here: the goal is to relate `(β_ X Xᘁ).hom` to
`(β_ Xᘁ X).inv` under the coev/ev sandwich, i.e. exactly a difference of one braiding
across a cap.

**Also newly available**, from #5848/#5859/#5860:
* `rightDualIso_swap_tensor` — two dual structures differ by the inverse monodromy.
* `PivotalCategory` now carries monoidality (`pivotor_tensor`), and `pivotalOfRibbon`
  supplies it from a balancing. So Barrett–Westbury's 'braided pivotal ⇒ spherical' is
  applicable to the class as stated, which it was not before.
* `twist_tensor_three` — θ on a 3-fold tensor is pairwise braidings + single twists only.

**Scope (a) preserved from the original entry, and re-affirmed:** this closes a
correctness/consistency gap in the mass chain's DERIVATION. It does not claim to improve
m_p, the Δ_λ binding magnitude, or any number. Both Do-nots from the handoff stand.



## 2026-08-26 (same day) — RETRACTION: the chain is broken at the link this bean exists to supply

I claimed the takeover above was unblocked. **Checking the bean's own premises against current
code, its consumer chain no longer runs through sphericality at all.** Two independent reasons:

**1. The named consumer is already discharged, by a different route.**
`QOU.BraidKnot.Ribbon.qDim_conj_object` proves `qDimObj (Xᘁ) = qDimObj X` **unconditionally**,
in any braided right-rigid category — no pivotal, no spherical, no transport hypothesis. It goes
via `QOU.MathlibExt.qDimWith_rightDual`: the quantum dimension does not depend on the choice of
dual, and `X` is itself a right dual of `Xᘁ`. So the chain
`sphericality → qDim_conj → dim_q(λ) → G⁻¹ → mass` is severed at its first arrow: `qDim_conj`
does not need sphericality.

**2. For these definitions, ribbon probably does NOT imply spherical — and the file already says
so.** `KeystonePivotalSpherical`'s own docstring records it: `qDim_twist_eq_leftQDim` shows the
two traces differ by the twist factor `θ_{Xᘁ} ⊗ θ_X`, so the classical `ribbon ⇒ spherical` — a
theorem about the **twisted** trace — does not reach these **twistless** ones.

My own algebra lands in the same place. Using `rightAdjointMate_comp_evaluation` on
`f = θ_X`, then `tensorHom_def`:

    (θ_{Xᘁ} ⊗ₘ θ_X) ≫ ε  =  ((θ_{Xᘁ} ≫ (θ_X)ᘁ) ▷ X) ≫ ε

so `leftQDim X = qDimObj X` would require `θ_{Xᘁ} ≫ (θ_X)ᘁ = 𝟙`. The repo's ribbon axiom is
`twist_dual : θ_{Xᘁ} = (θ_X)ᘁ`, which gives `((θ_X)ᘁ)²` — so it would need **θ² = 𝟙**, false in
general. The axiom that WOULD close it is the anti-compatibility `θ_{Xᘁ} = ((θ_X)ᘁ)⁻¹`, which is
a different axiom from the one the class carries.

**Where the error was:** I ran the corpus-grep, found this bean, and then took its premises at
face value instead of checking them against current code — the same failure the grep discipline
exists to prevent, one level up. AGENTS.md's own warning applies verbatim: a sibling's bean is not
a primary source.

**What is actually left**, and it is smaller and differently shaped:
- Decide whether `SphericalStructure` (twistless) is the right class at all, given the classical
  theorem is about twisted traces. That is a definitional question, not a proof gap.
- If it is kept, the honest statement is the **obstruction**: `leftQDim` and `qDimObj` differ by
  `((θ_X)ᘁ)²` under the sandwich. Worth proving as a lemma — it converts 'not yet proved' into
  'precisely this, and here is why ribbon does not give it'.

No number moves either way. Scope (a) throughout.



## 2026-08-26 — the bean's OWN question answered: NO, the ribbon axioms cannot close it

This bean asks 'can the ribbon axioms close mass/binding derivation gaps'. Having severed the
sphericality route above, here is the answer for the *binding* half, from the binding side.

**The missing term is graph-combinatorial, not categorical.**
`QOU.MassTheory.AdditiveSignChangingTerm` gives the leading derived candidate as a
bond−frustration simplex term on the A-nucleon coordination graph `K_A`:

    M(A) = s · (C(A,2) − κ · C(A,3))

`C(A,2)` edges (2-body bonds) minus κ times `C(A,3)` triangular faces (frustrated 3-cycles).
It is defined by **counting simplices on a graph**, not as a composite of twists and braidings
in a ribbon category. So `twist_tensor_three` — 'θ on a 3-fold tensor is pairwise braidings
plus single-object twists, with no irreducible 3-body datum' — **does not apply to it**. The
bridge I left open on 2026-08-26 is now closed, and it closes the wrong way for the ribbon route.

**What IS gained, narrowly.** The same lemma is a scope-(b) structural exclusion of one route:
**no ribbon-derived weight can supply the `C(A,3)` piece**, because the balancing axiom
decomposes θ on a 3-fold tensor into pairwise + per-object data only. The invariant is named
(`BalancedCategory.twist_tensor`), so this qualifies as (b) rather than (a). It does not
retroactively explain the six failed ansätze — Frobenius co-Casimir, Demazure-fibre,
LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov are representation-theoretic, not
twist/braiding composites.

**Where the real gap is**, per that file, and it is not where this bean assumed:
- The **sign** is already derived, 0-parameter: `M(3) > 0 ∧ M(4) < 0 ↔ 3/2 < κ < 3`, a genuine
  open window from the simplex structure.
- The **magnitude** is a fit, and provably vacuous: `(s,t) ↦ (M(3), M(4))` has determinant
  −6 ≠ 0, so ANY target pair is hit uniquely. Matching both residuals is 2 parameters on 2
  points and carries zero predictive content.
- Progress = fixing **κ** by structure to 0–1 free parameters, turning `M(3)/M(4)` into a
  prediction. Pre-registered candidates `κ ∈ {1,2,3,[3]_q}` + tetrahedral penalty were tried
  and none lands.

**Not going fishing for κ.** Searching the window `3/2 < κ < 3` for something that fits is
precisely the fit-hunting the anti-fit rules forbid; a κ must come from structure or not at all.

**Verdict for this bean: answer is NO on both halves.** Sphericality's consumer was already
discharged by a shorter route; the binding term is not ribbon-shaped. Recommend closing it as
answered-negative rather than leaving it in-progress.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: 22affaed24 "ribbon axioms cannot close the binding gap"; body: "Recommend closing it as answered-negative"; previously stalled (last activity 2026-08-30); 11 main commits
