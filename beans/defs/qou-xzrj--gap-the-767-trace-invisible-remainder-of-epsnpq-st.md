---
# qou-xzrj
title: 'GAP: the 7.67% trace-invisible remainder of epsNPq (step 8)'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T21:07:16Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---

Opened from `qou-cds1` / step 8 of the 2026-05-24 Q_β fitting-finding audit,
on owner instruction to bean-and-queue anything arising while `qou-cds1` is the
priority.

## What is open

`epsNPq` — the functional the Q_β ansatz calls `ε(Δ)` — is the **coordinate sum**
of the neutron−proton normal-form difference, not the Frobenius counit
(`qou-99qc`). It is not a trace: 8 of 36 ordered basis pairs fail cyclicity in
the regular representation of `H_3(q)`
(`computations/qbeta/qbeta_net_trace_invariance_probe.py`, 25/25).

`H_3(q)` is split semisimple, so `H = Z(H) ⊕ [H,H]` with dim 3 + 3, and **every**
trace annihilates `[H,H]`. At q₀:

    epsNPq   = −0.187207194529378
      central   −0.172847658641848   92.33 %
      commutator −0.014359535887530   7.67 %

The central 92.33 % is **derived**: it is exhibited as the unique trace agreeing
with `net` on the centre,

    a_(3) = (q+1)/((q²+1)(q²−q+1))
    a_(2,1) = q(q²−1)/(q⁴+q²+1)
    a_(1³) = q³(q−1)/((q²+1)(q²+q+1))

verified to reproduce `net` on the whole centre, annihilate `[H,H]`, and give
exactly the central part on Δ.

**The remaining 7.67 % is what is open.** No Markov trace, no augmentation, no
`χ^λ` and no combination of them can see it, so it is not an eigenvalue of
anything in the framework's current observable vocabulary. Q_β's +0.168 % match
to CODATA requires all of it: the trace-visible part alone gives 0.723537 MeV,
−7.52 %.

## What is already known about it

- It is **bar-even**, exactly: `net(dC) = −(q²−1)²/(q⁴+q²+1)`
  (`qbeta_alpha_commutator_floor_probe.py`, 22/22). So it supplies no bar-odd
  material — which *extends* the sibling prune `fcffeee29` rather than breaking it.
- It is **z-independent**, hence convention-independent: identical in C and D,
  and it is the whole z-free part of the ladder phase (13.72 % of 2α in C,
  17.73 % in D).
- Related: conjugating both nucleon words by one basis element — a Markov-I
  move — swings Q_β over 0.692169…0.783646 MeV, ≈ 70× the residual. `net` takes
  exactly two values across the six, because conjugation by `w₀` is the diagram
  automorphism `s₀↔s₁` and permutes the standard basis.

## The question

What object in the framework carries a non-cyclic functional's value on `[H,H]`,
and is the preferred presentation (the "single-wrap convention", audit step 4)
derivable rather than chosen? Step 8's postulate is now narrowed from the whole
of `net` to this remainder; answering it would close the postulate or replace it.


## 2026-08-26 — LOCATED: the traceless part of the 2-dimensional block, and D does NOT remove it

`qbeta_where_the_trace_invisible_part_lives_probe.py` (9/9). This answers where,
and settles the question the TL result made urgent.

**The structure.** For a split semisimple algebra `⊕ M_{n_i}` the commutator
subspace is `⊕ sl_{n_i}`, and `sl_1 = 0`. So in `H₃(q) = R ⊕ M₂ ⊕ R` the **entire**
commutator subspace sits inside the 2-dimensional block. Measured, not inferred:
`e_(3)` and `e_(1³)` both annihilate `[H,H]`, `e_(2,1)` acts on it as the
identity, and `dim [H,H] = 3 = dim sl₂`.

**Four facts that arrived separately are one fact.**

- `dC` lies entirely in the `(2,1)` block.
- **Δ's `(2,1)`-component *is* `dC`** — i.e. that component is traceless, which
  is the *same statement* as `χ^(2,1)(Δ) = 0`. Those were found independently.
- The floor `−h·y_(2,1)(1)` carries **that block's own weight** — not a
  coincidence of labels.
- So Δ splits as: two 1-dimensional blocks carrying everything a trace can see,
  plus a **traceless element of the 2-dimensional block** carrying everything it
  cannot.

**The urgent question, answered.** Convention D quotients the `(1³)` block. `dC`
is in `(2,1)`, so `e_(1³)·dC = 0` and `dC ≠ 0`: **the trace-invisible remainder
survives the Temperley–Lieb quotient intact.** It is not what D removes, and this
bean stays live under the canonical convention. The 7.67 % cannot be disposed of
by appealing to the quotient.

**Not claimed:** that anything in the framework's vocabulary evaluates a
traceless element of a 2-dimensional block. That is exactly what remains open —
this says where to look, not what to find. The sharpened question: **what
observable, if any, is sensitive to `sl₂ ⊂ M₂` in the decay channel?**


---

## 2026-08-27 — ANSWERED (representation), PR #5869: an ELEMENT, via the pairing

The bean's question — *"what object in the framework carries a non-cyclic
functional's value on [H,H]?"* — has an answer that needs nothing new.

**A trace is LINEAR and kills [H,H]. The Markov PAIRING `<x,y> = tr_M(x*y)` is
BILINEAR and does not** (for 2x2 traceless `A`, `tr(A^2) = -2 det A`).

**The enabling fact was already in the corpus and is the opposite of an
obstruction.** `qou-s7z2` proves the pairing is DEGENERATE on H_3 under
convention D with radical the `(1^3)` ideal
(`MarkovGramDegenerate.pairing_descends`, `mem_radical_of_pairing_zero`). But
`[H,H] = sl_2` sits in the TWO-row `(2,1)` block. So the pairing is degenerate
exactly where the remainder is NOT, and nondegenerate exactly where it IS.

### Measured (12/12, exact symbolic over Q(q), z a free symbol)

`computations/qbeta/qbeta_trace_invisible_is_pairing_representable_probe.py`

- Riesz system **rank 6/6** — `y0` is UNIQUE, not a fitted choice.
- `y0` lies in the commutator subspace (all three centre-coordinates vanish).
- `tr_M(dC * y0) = net(dC)` exactly; `|diff| = 0.0` at the proton pin.
- **Exact on all six basis elements:**

      net(x) = sum_lambda a_lambda chi^lambda(x) + tr_M(x * y0)

- The pairing term vanishes on the CENTRE, so no double-counting.

### Lean (4 declarations, sorry-free, lean-direct exit 0, no warnings)

`QOU/QBeta/PairingSeesCommutator.lean` — the structural facts, not a Lean
transcription of the probe:

- `cyclic_annihilates_commutator` — **cyclicity ALONE** kills every commutator,
  so no search over traces can repair the invisibility. `[propext, Quot.sound]`.
- `trace_pairing_sees_a_commutator` — the CONVERSE GUARD (`trace d = 0` but
  `trace(d*d) = 2`), without which the first reads as an impossibility.
- `diag_one_neg_one_is_commutator` — `d = e*f - f*e`, so the guard is about the
  commutator subspace and not merely a traceless matrix.
- `eq_of_pairing_eq_of_nondegenerate` — **uniqueness** of the representative,
  on `[propext]` alone. This is the load-bearing one: a solve admitting many
  answers would be a fit; nondegeneracy leaves nothing to select.

### Still open — the bean does NOT close

- **Existence of `y0` is not formalised.** It is a finite-dimensional
  dual-space fact, instantiated by the probe (rank 6/6). The Lean proves
  "unique if it exists" and "the pairing reaches [H,H] at all"; the probe
  supplies "it exists, here it is". Neither substitutes for the other.
- **Is `y0` DERIVABLE?** This is now the question. The representation is exact
  and `y0` is determined, but determined-by-`net` is not the same as
  derived-from-the-substrate. Until that is answered, step 8's postulate is
  narrowed rather than closed.
- Scope **(a)** throughout: a representation of `net`, not a derivation of it;
  says nothing about whether the single-wrap presentation is forced.

### Method note

My first version of the decomposition wrote `2 * a21`, reading the `a_lambda`
as regular-character coefficients. They are the trace functional's own
coefficients; it failed on 5 of 6 and the assertion caught it. My first
DIAGNOSTIC was also wrong (compared against `net(x)` rather than `net(x_Z)`,
which need not agree off the centre). Both are kept in the file as controls.


## 2026-08-27 (2) — y0 IS dC, and the z-independence now has a MECHANISM

`qbeta_riesz_element_is_structurally_forced_probe.py` (9/9, exact symbolic,
z free throughout). Asked whether the unique y0 is merely DETERMINED or
actually has an independent characterisation.

### y0 = mu * dC,   mu = -2q/((q-z)(qz+1))

The representing element is **Delta's own trace-invisible part**, rescaled.
Nothing outside the decomposition is introduced. So

    net(x) = sum_lambda a_lambda chi^lambda(x) + mu * tr_M(x * dC)

and on dC the remainder is a **self-pairing**: `net(dC) = mu * tr_M(dC^2)`.
The commutator space is 3-dimensional, so this is a real constraint.

### Why the remainder is convention-free — previously MEASURED, now explained

    <dC,dC> = -(z-q)(q-1)^2(q+1)^2(qz+1) / (2q(q^2-q+1)(q^2+q+1))
    mu      = -2q / ((q-z)(qz+1))
    product = -(q-1)^2(q+1)^2 / ((q^2-q+1)(q^2+q+1))            [z-FREE]

Both carry the Hecke-quadratic pair `(q-z)(qz+1)`; they **cancel exactly**. The
scalar's z-structure is the inverse of the pairing's. The bean recorded
z-independence as an observation — this is the mechanism.

### Two forced structural facts

- y0's denominator = `(z-q)(qz+1)(q^2-q+1)(q^2+q+1)` = `q(q^4+q^2+1)(z^2-hz-1)`
  — the **Hecke quadratic** `sigma^2 = h sigma + 1` read in z. Ratio exactly 1.
- so y0's only poles are `z = q` and `z = -1/q`: exactly the two Markov Gram
  roots that annihilate the **(2,1)** block (multiplicity law, PR #5864). y0
  blows up precisely where the pairing defining it degenerates **on its own
  block**. Neither z_C nor z_D is a pole.

### Independent cross-check

`net(dC) = -(q^2-1)^2/(q^4+q^2+1)` — the floor
`qbeta_alpha_commutator_floor_probe.py` reached by a different construction.
Two unrelated routes agree exactly.

### Corrected

I predicted the direction `[0,1,1,h,h,+2]` from a hand-factorisation; the
assertion failed and the sign is **-2**. Claim survived, arithmetic did not.
Retraction kept in the docstring.

### STILL OPEN — the bean does not close

Evidence y0 is **canonical rather than fitted**: z-free direction, structurally
forced poles, and it is an object the decomposition already had. It is still
**not a derivation from the substrate** — nothing here produces y0 without first
inverting `net`.

**The gap is now exactly `mu`.** Not "the element plus the scalar" — the element
is accounted for. Is `mu = -2q/((q-z)(qz+1))` derivable? Its shape is
suggestive: numerator `-2q`, denominator the Hecke quadratic. Scope (a).


## 2026-08-27 (3) — mu has a closed form; the gap is now an IDENTIFICATION, not an unknown

`qbeta_mu_closed_form_and_delta_alignment_probe.py` (6/6, exact symbolic, z free).

### mu is framework-native

    (q-z)(qz+1)   = -q (z^2 - h z - 1)            the HECKE QUADRATIC in z
    z^2 - h z - 1 = -(q^4+q^2+1)/q^2 * y_(2,1)(z)
    q^4+q^2+1     = q^2 [3]_q                      ([3]_q = q^2 + 1 + q^-2)

    ==>   mu = - dim(V_(2,1)) / ( [3]_q * y_(2,1)(z) ),    dim = 2

Block dimension, a quantum integer, the block's OWN Markov weight. So the full
representation, every ingredient a framework object:

    net(x) = sum_lambda a_lambda chi^lambda(x)
             - [ dim(V_(2,1)) / ([3]_q y_(2,1)(z)) ] * tr_M(x * dC)

**Not a fit:** an identity in TWO FREE SYMBOLS, exact for every q and every z —
nothing to tune. The `2` is `chi^(2,1)(1)`, measured not asserted. Bracket
convention cross-checked against the sibling's `b^2 = [3]_q/[2]_q^2` (#5337).

### The Delta alignment — measured, and NOT the clean answer I expected

y0 is the Riesz representative of `net` on [H,H]; **Delta enters nowhere in its
definition**, so `y0 ∥ dC` is a real alignment, not a restatement. Parallelism
in a 3-dim space is 2 conditions.

I expected "Delta alone". Measured: of five basis elements with nonzero
commutator part, **four are not parallel and one is** — `e_minus` = w_0, the
longest element. So Delta satisfies a real constraint but is **not unique** in
doing so. Do not over-claim this as "Delta is special".

That w_0 is the one is probably not accidental: conjugation by w_0 is the
diagram automorphism s_0 <-> s_1, which this bean already records as why `net`
takes only two values across the six conjugates.

### Where the bean now stands

Every piece of `net` is expressed in framework-native objects. What is NOT done:
mu's closed form was reached by **identification** — recognising the factors —
not by a forward derivation from a normalisation principle. That is a narrowing,
not a closure; step 8's postulate is not closed.

**The remaining question is sharp and small:** is
`mu = -dim / ([3]_q y_(2,1))` FORCED by a normalisation of the Markov pairing,
or is it merely the value that happens to work? A forward derivation would close
step 8. Scope (a) throughout.


## 2026-08-27 (4) — the split: ALL of mu's convention-dependence is DERIVED

`qbeta_mu_normalisation_is_derived_probe.py` (5/5).

On `[H,H] = sl_2` the Markov trace collapses to one block, so for x, w in [H,H]

    tr_M(x w) = y_(2,1)(z) * chi^(2,1)(x w)          [verified, all 9 pairs]

The Markov **pairing** there is just the block's trace form scaled by the
block's own Markov weight. That is Wedderburn — nothing chosen. Writing W for
the representative of `net|_[H,H]` against the UNSCALED form:

    mu = (W / dC) / y_(2,1)(z),    W/dC = -2/[3]_q,    W is z-FREE

  - `1/y_(2,1)(z)`  — **DERIVED**, the pairing's normalisation on the block
  - `-2/[3]_q`      — z-free, **still an identification**

**So all of mu's convention-dependence is derived.** What remains unexplained
does not move with the Markov parameter at all.

### Method trap worth remembering

Solving for W over **all of H_3** (6 unknowns) is **rank 4/6** — `chi^(2,1)(xw)`
annihilates both 1-dim blocks, so two coordinates stay free and the "ratio"
comes back still containing symbols: an answer-shaped expression that is not an
answer. W must be solved **inside sl_2** (3 unknowns, 3 commutator basis
vectors) → rank 3/3. The rank check is now an assertion in the file.

### Where the bean stands after four tranches

| question | status |
|---|---|
| what object sees the remainder? | **answered** — an element, via the Markov pairing |
| is that element derivable? | **answered** — it is `dC`, Delta's own commutator part |
| is `mu` derivable? | **half** — `1/y_(2,1)(z)` derived; `-2/[3]_q` identified |
| does step 8's postulate close? | **no** |

**The whole remaining gap is the pure-q constant `-2/[3]_q` = `-dim/[3]_q`.**
It is z-free, so no convention question touches it. Closing step 8 means
deriving that one constant from a normalisation principle — or showing it cannot
be, which would be an equally publishable negative. Scope (a) throughout.


## 2026-08-27 (5) — every factor of mu is a NAMED (2,1)-block invariant

`qbeta_mu_is_block_invariants_probe.py` (7/7). Names the two pieces that were
still bare constants.

### The `2` is the regular-rep MULTIPLICITY

    chi_reg(x y) = 2 * chi^(2,1)(x y)   for x,y in [H,H]      [all 9 pairs]

Only (2,1) contributes on sl_2, with multiplicity dim = 2. Against the regular
form the representative S satisfies `S/dC = -1/[3]_q`. So the 2 is the
multiplicity = block dimension = `chi^(2,1)(1)`, not a constant that worked.

### The `[3]_q` is the block's SCHUR ELEMENT

From `tau = sum_lambda chi^lambda/c_lambda`, `tau(T_w) = delta_{w,e}` (rank 3/3):

    c_(3)   = (q^2+1)(q^2-q+1)(q^2+q+1)
    c_(2,1) = (q^2-q+1)(q^2+q+1)/q^2 = [3]_q
    c_(1^3) = (q^2+1)(q^2-q+1)(q^2+q+1)/q^6

`c_(2,1) = [3]_q` **is the hook formula** — hooks of (2,1) are 3,1,1, so
`[3][1][1] = [3]_q`.

### The Hecke quadratic FACTORISES into the block's two invariants

    c_(2,1) * y_(2,1)(z) = -(z^2 - h z - 1)                      [exact]

hence

    mu = dim(V_(2,1)) / ( -c_(2,1) * y_(2,1)(z) )

Dimension, Schur element, Markov weight — three canonical invariants of one
block, no free constant among them.

### CAREFUL — not the corpus's `schurElement`

`QOU.MathlibExt.WenzlSchurElement.schurElement Q X lam` is the TWO-VARIABLE
Wenzl form, and the corpus builds `y_lambda` from it
(`jonesMarkovCoeff = schurElement/wenzlNormalisation`). What is computed here is
the CLASSICAL one-variable symmetrizing-trace Schur element of H_3(q). Same
concept, different variables/normalisation. **No equality claimed** under any
substitution — a separate question this does not settle. And `c_(2,1) = [3]_q`
is **not claimed new**: it is the standard hook formula, verified rather than
cited because the value is load-bearing.

### Method

Both linear systems **rank-checked before their output was read** (3/3, 3/3) —
the lesson from the rank-4/6 trap one tranche earlier.

### Where the bean stands after five tranches

Every ingredient of the representation is now a named framework object:

    net(x) = sum_lambda a_lambda chi^lambda(x)
             + [ dim(V_(2,1)) / (-c_(2,1) y_(2,1)(z)) ] * tr_M(x * dC)

**What is still NOT derived:** the COMBINATION. Nothing derives why net's
representative should be `-dim/(c_lambda y_lambda)` times dC rather than
something else. That is now the whole of the gap — no bare constants left in
it, just an unexplained combination of three named invariants. Scope (a); step
8's postulate is narrowed, not closed.


## 2026-08-27 (6) — `net` is tau against the ALL-ONES element; the gap is now ONE identity

`qbeta_net_is_tau_against_all_ones_probe.py` (8/8).

### `net` has an intrinsic form

`tau(T_w) = delta_{w,e}` picks the identity coefficient, so pairing against the
all-ones element sums coordinates — which is exactly `net`:

    Omega := sum_w T_w = [1,1,1,1,1,1]
    net(x) = tau(x * Omega)                     for every x

**Solved, not assumed** — the tau-representative system is rank 6/6 (unique) and
returns all-ones.

### which DERIVES the Schur-element factor

With `tau = sum_lambda chi^lambda/c_lambda`, and x in sl_2 where only (2,1)
survives, the representative against the unscaled block form is

    W = Omega_(2,1) / c_(2,1)

**So the `1/c_(2,1)` in mu is not an identification** — it is the Schur element
in tau's own decomposition. That was the largest identified piece; now derived.

### and collapses the gap to one identity

    Omega_(2,1) = -dim(V_(2,1)) * dC              exact, ratio -2

The whole remaining content: **the all-ones element's traceless part is minus
the block dimension times Delta's traceless part.** Two explicit canonical
elements, no constant left in the statement.

### A guess that failed, kept as a control

`Omega = sum_w T_w^{-1}` (the dual-basis reflex) is **NOT** the representative:
`net(x) = tau(x * sum T_w^{-1})` fails on 5 of 6, and the inverse-sum has
coordinates like `(q^2-q-1)^2/q^2` where the answer is plain 1.

### Where the bean stands after six tranches

    net(x) = sum_lambda a_lambda chi^lambda(x)  +  tr_M(x * y0)
    y0     = mu * dC
    mu     = dim / (-c_(2,1) y_(2,1)(z))

with, now DERIVED: the pairing normalisation `1/y_(2,1)` (Wedderburn); the
multiplicity `dim` (chi_reg = 2 chi^(2,1) on sl_2); the Schur element
`1/c_(2,1)` (tau's decomposition); and `net = tau(. * Omega)`.

**STILL OPEN — the only step:** why is `Omega_(2,1) = -dim * dC`? Nothing
explains why Delta's commutator part is parallel to the all-ones element's, nor
why the ratio is the dimension. And it is **not unique to Delta** — `e_minus` =
w_0 aligns too — so a derivation must explain a small family, not a singleton.

Scope (a). Step 8's postulate is narrowed to one identity, not closed.


## 2026-08-27 (7) — TRIED the last step. It does not close; it collapses onto step 4.

`qbeta_last_step_is_the_presentation_probe.py` (4/4).

### The result

Delta is built with mixed crossing `t = h/2` — **step 4 of the fitting-finding
audit, which this bean already flags as CHOSEN rather than derived**. Varying
only that parameter:

    t = h/2 (corpus)   parallel: YES   ratio = -2 = -dim(V_(2,1))
    t = h/3            parallel: NO
    t = h              parallel: NO
    t = 0              parallel: NO

At every other `t` the parallelism **fails outright** — not a different ratio,
no proportionality at all. `t = h/2` is what makes the pairing representation
EXIST; the clean `-dim` is its signature.

**So deriving `comm(Omega) = -dim * dC` is exactly as hard as deriving
`t = h/2`.** Six tranches reduce step 8's postulate to step 4's. They do not
eliminate it.

That is worth having — a postulate reduced to an earlier, already-named one
says where to push — but it is **not** a derivation of `net`.

### TWO CORRECTIONS to my own earlier entries in this bean

1. **Mislabel.** Tranche (6) wrote `Omega_(2,1)`; the object is Omega's
   **commutator part**. `chi^(2,1)(Omega) = 2h ≠ 0`, so the (2,1)-component is
   strictly larger and not traceless. Identity unaffected; both probes
   relabelled.

2. **I over-read the alignment, in tranches (2), (4) and (5).** I called
   `y0 ∥ dC` "a real 2-condition constraint". Measured:
   `{x : comm-part(x) ∥ dC}` has dimension **4 of 6** — two thirds of the
   algebra. Landing in it is not a coincidence, and `w_0` also aligning is
   unsurprising rather than suggestive. **The content was never the
   parallelism, only the ratio.**

Both are now assertions in the probe so they cannot quietly revert.

### Where this leaves the bean

Derived: `net = tau(. * Omega)`; the Schur element `1/c_(2,1)` (tau's
decomposition); the multiplicity `dim`; the pairing normalisation `1/y_(2,1)`.

**Open, and now precisely located:** `t = h/2`, the step-4 presentation. Not a
new unknown — the one the audit already named. The honest next move is either
to derive step 4, or to record that step 8 is not independent of it.

Scope (a). Step 8's postulate is REDUCED, not closed.


## 2026-08-27 (8) — CORRECTION to tranche (7), and the conclusion improves

Tranche (7) said the last step "collapses onto step 4, which the bean flags as
chosen rather than derived". **Both halves were wrong**, and reading the audit
table settled it:

1. **`t = h/2` is STEP 3, not step 4.** Step 3 defines the typed-crossing
   operators — `C(u,d;sigma) = sigma - h/2`. Step 4 only assembles words from
   them.
2. **Neither step is "chosen".** The audit marks BOTH ✓ **Derived**. What flags
   step 4 as a question is *this bean* (line 62, "is the preferred presentation
   … derivable rather than chosen?") — a question, and I quoted it as a finding.

And step 3's justification **checks exactly**:

    (C(u,u;sigma) + C(d,d;sigma))/2 = (sigma + (sigma - h))/2 = sigma - h/2

the symmetric midpoint forced by u<->d swap symmetry. Verified symbolically.

### So the conclusion is BETTER than tranche (7) reported

The chain does not bottom out in an undischarged postulate. It grounds out in
**step 3, which is derived**. Every constant in the representation of `net`
traces to derived material:

    net(x) = tau(x * Omega)             Omega = sum_w T_w      [derived, rank 6/6]
    1/c_(2,1)                            Schur element         [derived, hook formula]
    dim V_(2,1) = 2                      regular multiplicity  [derived]
    1/y_(2,1)(z)                         pairing normalisation [derived, Wedderburn]
    comm(Omega) = -dim * dC              contingent on t = h/2 [step 3, DERIVED]

### What is still NOT closed — and it is narrower than I have been saying

**Step 8 postulates the PHYSICAL IDENTIFICATION**: that
`Q_beta = |Delta(net)| * E_0`, i.e. that the unweighted NF sum *is* the
leading-order mass difference. Nothing in seven tranches touches that. Showing
`net` is expressible in derived algebraic objects says **what `net` is**, not
that it is **the right observable**.

That is the honest end state: the ALGEBRAIC side is fully grounded; the
PHYSICAL identification is untouched and remains step 8's postulate.

Written up as an addendum to
`docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md`, including all
four corrections (this one, the step-3/4 mix-up, the over-read alignment, the
Omega mislabel).

Scope (a) throughout.

## 2026-08-30 — PR #5869 merged (9ce3ed2942)

The pairing result is on main: the trace-invisible remainder is Riesz-representable by a unique y0 = mu*dC, and every factor of mu is a named (2,1)-block invariant except the last, which collapses onto step 3's presentation of the proton/neutron normal forms.

Bean stays OPEN. What merged is a *representation* of net, scope (a) throughout — nothing here produces y0 without first inverting net. Step 8's actual postulate, the physical identification Q_beta = |Delta(net)|*E0, is untouched by all seven tranches.

Merge note: GitHub refused rebase-merge (4 merge commits); branch was linearized locally per AGENTS.md rule 8, and the six audit-witness conflicts were resolved to origin/main's side because my regenerated copies carried this container's environment (mpmath 1.3.0, no scipy/clarabel) rather than main's.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: SUPERSEDED.** Superseded by the 2026-09-08 ruling (qou-99qc): the canonical ε is a trace and cannot see the [H,H] remainder, so "what carries the 7.67%" no longer bears on Q_β. The representation net = Σ a_λ χ^λ + μ·tr_M(x·dC) on main stays valid algebra (scope a).

Evidence: The question is about the trace-invisible 7.67% of epsNPq. The 2026-09-08 ruling makes ε a Markov trace (tr_M at z_D, AGENTS.md:2329), and every trace annihilates [H,H] (`L/QBeta/PairingSeesCommutator.lean` `cyclic_annihilates_commutator`, textually sorry-free). So the remainder is not part of the canonical functional. The algebraic representation result landed (PR #5869, 9ce3ed2942).

Status: `todo` → `scrapped`.
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
