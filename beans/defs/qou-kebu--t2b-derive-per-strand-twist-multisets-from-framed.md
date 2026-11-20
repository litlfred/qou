---
# qou-kebu
title: 'T2b: derive per-strand twist multisets from framed braid words'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
    - 8f-tseries
    - 8f-open
created_at: 2026-08-04T10:16:22Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
blocked_by:
    - qou-qvpl
    - htw2
---

BATTERY RESULT (strand-twist-y-battery.witness.json):
- 10,000 candidate helon-style twist assignments tested
- Only 4 survive the spectrum + nucleon-GMN battery
- u-quark multiset {0,1,1} is UNIQUELY determined
- electron multiset {-1,-1,-1} is UNIQUELY determined
- All 4 survivors are sign-flip variants of the SAME assignment

DERIVATION GAP:
The battery proves CONSISTENCY (the twist assignments are compatible
with known physics) but does NOT DERIVE them from QOU axioms.

To close T2b, need to show: given the framed braid word for each
torus knot T(2,p), the per-strand twists follow from the ribbon
structure of the Hecke category. Specifically:
1. The twist θ_V = q^{c_V} acts on each strand by the Casimir
2. For T(2,p) = σ₁^p, the total twist is p·θ_V
3. The per-strand multiset is determined by the braid monodromy
4. The battery result shows the answer is {0,1,1} for u, etc.

DEPENDS ON: T2 (hypercharge from ribbon twist = the derivation
of what Y means categorically, which is still the gap).

## Step 1 of the proposed route cannot deliver step 3 (2026-08-16)

`QOU/StandardModel/ComponentFraming.lean` — lean-direct exit 0, no warnings, no
sorry/axiom/native_decide. Library file, no sidecar; my verification is the gate.

### Why theta is the wrong tool, from the corpus's own probe

The route above says "theta_V = q^{c_V} acts on each strand by the Casimir" and
then "the per-strand multiset is determined by the braid monodromy".
`ribbon_twist_charge_quantum_probe.py:13-17`:

  > "On a simple object of a ribbon category the twist theta acts by a SCALAR;
  >  for Hecke / quantum-sl_N the exponent is the CONTENT SUM of the partition"

A scalar attached to an object is ONE number. The battery's answers are
NON-CONSTANT multisets -- u = {0,1,1}, d = {-1,-1,1} -- and no scalar produces a
non-constant multiset over identical strands. That probe tested Q = c(lambda)/3
directly and it FAILED; this is the structural reason it had to.

theta is the WEIGHT PER UNIT FRAMING (q^{c_V t_i}), not the framing t_i. Step 1
cannot fix integers; it acts on them.

### What does fix them: the closure map, not the twist

Step 3's instinct is right but the mechanism is the PERMUTATION. In a framed
link the framing is one integer PER COMPONENT, not per strand. Closing beta
joins strand i to strand pi(beta)(i), so a cycle of pi becomes ONE component and
a well-defined framing takes one value on all of it. That is not an extra
assumption about ribbons -- it is what "framing of a framed link" means,
transported to strand indices.

    IsComponentFraming pi t  :=  forall i, t (pi i) = t i

### Derived, falsifiable consequences

  constant_of_transitive   pi transitive (closure is a KNOT) => t constant, so
                           the multiset is {a,...,a}
  eq_one_of_injective      all entries distinct => pi = 1, closure is a totally
                           split n-component link

Applied to the four survivors:

  u  {0,1,1}              pi is NOT transitive -- u's closure is not a knot
  d  {-1,-1,1}/{-1,0,0}   same
  nu {-1,0,1}             pi = 1, totally split
  nu {0,0,0}              unconstrained
  e  {-1,-1,-1}           unconstrained (constant fits any pi)

Two of these are Lean-instantiated at Fin 3, the battery's strand count:
`u_multiset_forces_nontransitive`, `nu_multiset_forces_trivial_perm`.

These are the first constraints in this arc that are DERIVED rather than
enumerated. The battery searched 10 000 assignments and reported which survive;
this says which are POSSIBLE given a braid, before any search.

### Scope

Scope-(b) on the one excluded step -- theta alone determining a non-constant
per-strand multiset is excluded by the scalar/multiset mismatch, a proved
invariant. Scope-(a) on everything else. NOT excluded: theta in its actual role
as the weight q^{c_V t_i}; the hypercharge programme; this bean, whose step 3 is
reformulated rather than closed.

### Blocking input unchanged

The battery's own witness records it: the corpus carries NO per-chiral-fermion
framed braid words (bean htw2). Until those exist the table cannot be evaluated
-- which is exactly why it is worth stating now, as the test those words face.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Triage 2026-10-10 — open, and guard against a wrong closure from T2's body

Tagged `8f-open`; `blocked-by qou-qvpl` (T2) per this bean's own "DEPENDS ON"
line, and `blocked-by htw2` per the blocking input the body already records.

**The wrong closure to guard against.** `qou-qvpl` (T2) lists this bean's
battery under a heading reading "BATTERY PASSED (T2b, witness)" with items 6–9
— 10,000 candidates, only 4 survivors, `u = {0,1,1}` and `e = {−1,−1,−1}`
uniquely determined. A reader taking that at face value would close T2b. **It
does not close:** this bean's own body states the gap in as many words — *"the
battery proves CONSISTENCY (the twist assignments are compatible with known
physics) but does NOT DERIVE them from QOU axioms."* A 10,000-candidate search
reporting which assignments survive is enumeration against known physics, which
under §NO FITTING is selection against the target, not a derivation. Recorded on
`qou-qvpl` too, from the other side.

**What the 2026-08-16 append already settled, so nobody re-derives it.** The
four-step route in the original body is **not** the route: step 1 ("θ_V = q^{c_V}
acts on each strand by the Casimir") cannot deliver step 3, because θ acts by a
**scalar** on a simple object while the battery's answers are **non-constant
multisets** (`u = {0,1,1}`, `d = {−1,−1,1}`), and no scalar produces a
non-constant multiset over identical strands. That is scope-(b) on that one
step — a proved invariant, the scalar/multiset mismatch — and it is why the
corpus's own `ribbon_twist_charge_quantum_probe.py` test of `Q = c(λ)/3`
FAILED structurally rather than numerically. θ is the weight *per unit framing*
(`q^{c_V t_i}`), not the framing `t_i`.

**What replaced it is derived and is this bean's real asset.** The mechanism is
the **closure permutation**, not the twist: in a framed link the framing is one
integer per *component*, so closing β joins strand `i` to `π(β)(i)` and a cycle
of π becomes one component carrying one framing value —
`IsComponentFraming π t := ∀ i, t (π i) = t i`, with
`constant_of_transitive` and `eq_one_of_injective` as falsifiable consequences,
two of them Lean-instantiated at `Fin 3`. Those are the first constraints in
this arc that are **derived rather than enumerated**: they say which multisets
are *possible given a braid*, before any search.

**The blocker is unchanged and is upstream.** The corpus carries **no
per-chiral-fermion framed braid words** (bean `htw2`), so the derived table
cannot be evaluated. That is why the constraints are worth having now: they are
the test those words will face.


---

## Carrier files re-verified on `main` `3c0351a40da` (2026-10-10)

This bean already cites `ComponentFraming` / `SignCoherentTwist` nine times. The
checkable part, measured today rather than carried:

    ComponentFraming.lean    304 lines  rc=0  0 diagnostics  0 sorry/axiom/native_decide
    SignCoherentTwist.lean   226 lines  rc=0  0 diagnostics  0 sorry/axiom/native_decide

`lean -DautoImplicit=false -s 65536`, exit status captured directly (not through
a pipe — a `| head` makes `$?` report *head's* status, which is how a first pass
of this check produced four meaningless `exit=0`s). All seven declarations the
predecessor bean names resolve: `lepton_framing_determined`,
`nu_framing_is_zero`, `nu_distinct_multiset_excluded`, `e_framing_is_neg_one`,
`d_multiset_forced`, `coherent_iff_all_same_sign`, `cancel_preserves_total`.

**Note on the predecessor.** `htw2` is `scrapped` as this bean's duplicate, and
its 294-line body is where the lepton closure and the `θ_V = q^{1/2}·id_V`
ribbon-normal-form upgrade are actually written up. It is not superseded content
— only a closed work item. The full open/closed split is appended to
`qou-h0zz`; the correction to a stale "root blocker" recommendation of mine is
on `qou-8lxd`.


## Progress Update — 2026-11-16 (`litlfred/qou#8149`, `e824457ca8e0ff4e0b85644c5478eebd2c3c8d56`)

- **Lean 4 formalization (`folio/quantum-observable-universe/lean/QOU/StandardModel/RibbonTwistZ6Hypercharge.lean`, `0` `sorry`, wired into `QOU.lean`)**:
  - Formalizes `strandTwistSum` and proves `battery_survivors_produce_exact_twist_sums` verifying that both survivor multiset families $A = ((-1,-1,-1), (-1,0,0), (0,0,0), (0,1,1))$ and $B = ((-1,-1,-1), (-1,-1,1), (0,0,0), (0,1,1))$ produce the exact twist-sum spectrum $[T(e), T(d), T(\nu), T(u)] = [-3, -1, 0, +2]$, satisfy $3 \mid (\tau + T(t))$, and force the Baez–Huerta $\mathbb{Z}_6$ quantization $6 \mid (2\tau + 3w + 3Y_t)$ across all 8 chiral states (`firstGenChiralStates_all_valid_z6`).
  - Establishes why 3-strand framed ribbon twists succeed where 1-component Seifert knot signatures $\sigma(K) \in 2\mathbb{Z}$ fail (`knot_signature_even_obstruction`): per-strand framing $t_i \in \{-1, 0, +1\}$ reaches both odd ($-3, -1$) and even ($0, +2$) numerators over $3$.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8149, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
