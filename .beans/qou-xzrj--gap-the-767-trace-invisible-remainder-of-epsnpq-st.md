---
# qou-xzrj
title: 'GAP: the 7.67% trace-invisible remainder of epsNPq (step 8)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-26T21:07:16Z
updated_at: 2026-08-27T06:21:32Z
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
