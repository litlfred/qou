---
# qou-lw9l
title: 'Log-ratio channel is EXACTLY extensive: derived, with g-cancellation as the mechanism'
status: completed
type: task
priority: normal
created_at: 2026-09-02T21:27:41Z
updated_at: 2026-09-02T22:09:37Z
---

## Measured 2026-09-02 — `computations/probes/logratio_exactly_extensive_probe.py` (4/4)

Completes the dichotomy opened by `chain_binding_closed_form_probe` (#6394).

### The result

With `b = A-1` bonds the measured structure is `S_off = g^(b+1)`,
`S_on = g^(b+1)·f^b`, so

    L(A) = log(S_off/S_on) = -b·log f

**exactly linear in bond count, no constant term.** Worst relative deviation
2.4e-30 (pp), 9.2e-31 (nn) at A=2..5 — exact at compute precision. Slope:

    -E0·log f = 2.0507096923814336856 MeV/bond  (pp)
    -E0·log f = 3.79778293514235333  MeV/bond   (nn)

The pp slope reproduces `bpp_a_dependence_bound_probe`'s independently-computed
`-alpha·ln z` to **4.3e-13**. Two routes, one number.

### Why it matters: it DERIVES an assertion the corpus carries

`log_ratio_binding_prototype.py` states *"the EXTENSIVE invariant is the
log-ratio"* in one sentence, without derivation. It now follows from the same
identity that excludes the difference channel.

**The mechanism is that `g` cancels.** The free-trace growth `g^(b+1)` sits in
both numerator and denominator of the ratio and drops out entirely — verified
by recomputing L with g scaled 1.7x and getting a bit-identical value at every
A on both species. The DIFFERENCE channel cannot cancel it, which is exactly
what its two exclusion branches are about. So the two channels are not two
guesses at one quantity: they differ by whether the single-nucleon growth
survives, and that alone decides extensivity.

### Lean (both sorry-free, 0 axiom beyond the standard three)

    QOU.MassTheory.MarginalRatio.logRatio_linear_in_bonds
    QOU.MassTheory.MarginalRatio.logRatio_independent_of_growth

### Scope — shape, NOT magnitude

This settles only which channel is extensive. The magnitude is separately
measured to be wrong by the `t7qv` arc: `B(4He) = 10.387277` vs AME `28.295661`
(-63.29 %), three-body term negative at all eight A=3 orderings, four-body
negative in 80/80 random bond orders — every many-body correction pushing
further from the data.

**Extensive-and-short is a different problem from not-extensive.** What this
closes is the shape question; the arc's remaining difficulty is entirely in the
magnitude category now.


## EXTENDED 2026-09-02 — the channel has NO many-body term at all

`computations/probes/logratio_exactly_pairwise_additive_probe.py`, 4/4.

Extended the exact-linearity test from the pure chains to **every mixed
composition** of A=3 and A=4:

    S_on/S_off = f_pp^(Z-1) * f_pn * f_nn^(N-1)     worst rel dev 1.78e-50

across all 9 compositions. Taking logs, `L = sum over chain bonds of
(-log f_bond)` — **exactly pairwise-additive, with identically ZERO many-body
terms.** No three-body at A=3, no four-body at A=4. Not small; zero to fifty
digits.

### The consequence for the shortfall

The channel is ~2.7x short (`B(4He) = 10.387` vs AME `28.296`). The natural
place to look for missing binding is a many-body term. **In this channel there
is none to find.** Whatever closes the gap must change the per-bond VALUES or
the BOND COUNT — it cannot be an irreducible 3- or 4-body piece of L. That
removes a candidate class; it does not supply the binding.

### Tension with t7qv, and the candidate reconciliation

`t7qv` measures three-body negative at all 8 A=3 orderings (`c1491ec174`) and
four-body negative in 80/80 random bond orders (`2bbb6115c5`), by **Mobius
inversion over nucleon SUBSETS**. Not in conflict with additivity over the
CHAIN bond set: for chain 1-2-3, the subset {1,3} has a sub-braid where 1 and 3
are adjacent and bonded, while the full chain has no such bond. Mobius
inversion attributes that manufactured bond to a "three-body term".

**FLAGGED AS A READING, NOT VERIFIED.** Their own commit names *"a labelling
artifact of embedding the bond graph in a line"*, so the mechanism was
identified there. What this adds is the measurement that over the chain bond
set the term is exactly zero. Confirming it against their probe is separate
work and was not done.

### An f_pn mismatch, chased rather than rounded away

    measured (blind arm) 0.50815788774864559388
    canonical            0.50822978937673896258     rel 1.41e-4

Not a defect: `atomic_tr_m_helium4_canonical.py:243` defines
`f_pn = z_d - h_q*(1/2 - delta/4)`, the colour-WEIGHTED value; this probe uses
the blind arm. Every mixed composition carries exactly one `averaged_weighted`
crossing (#6379) and that is the only place the arms differ — #6379 measured
the gap at ~1e-4. `f_pp` and `f_nn` are arm-independent: a pure chain carries
no `averaged_weighted` crossing at all.


## PARAMETER-FREE REFUTATION 2026-09-02 — the chain bond set cannot make an alpha

The three obvious repairs to the shortfall are each now closed, and the last one
is closed without using any model constant.

    bonds(3H) + bonds(3He) - bonds(2H) = bonds(4He)      (1,1,1) both sides

an EXACT multiset identity for the chain layout `p..p n..n`, where (Z,N) has
(Z-1) pp, one pn, (N-1) nn bonds. So **any** additive functional on those
multisets obeys

    B(4He) = B(3H) + B(3He) - B(2H)

with the per-bond values cancelling entirely. Against AME2020:

    predicted 13.975275 MeV     AME 28.295661 MeV     ratio 2.0247

**No rescaling of f_pp, f_pn, f_nn can help — they do not appear in the
relation.** This is the alpha particle's excess binding arriving as a structural
obstruction rather than a numerical shortfall.

### All three repairs are closed

| repair | status |
|---|---|
| more bonds | bond set is FORCED — `QOU.Mass.StrandLayoutForcesChain` (sibling, Lean) |
| many-body term | exactly ZERO, measured to 1.8e-50 at every A=3,4 composition |
| rescale per-bond values | they CANCEL in the relation — parameter-free |

### Lean (sorry-free, axioms clean)

    QOU.MassTheory.MarginalRatio.alpha_relation
    QOU.MassTheory.MarginalRatio.chain_additive_cannot_match_alpha

### And the shortfall is not even uniform

Model vs AME with the model's own slopes: 2H **0.785** (model OVERSHOOTS), 3H
1.279, 3He 1.580, 4He 3.259. The ratio changes SIDE of 1, so no uniform rescale
was ever going to work — the parameter-free relation is the sharp version of
that observation.

### Unreconciled

t7qv reports `B(4He) = 10.387277`; my chain log-ratio gives `8.682248`. The gap
is 19.6 %, far larger than the ~1e-4 colour arm, so it is a different
construction. NOT reconciled here.


## 🛑 SCOPE CORRECTION — "all three repairs are closed" was WRONG

Reconciling the 19.6 % `B(4He)` disagreement with `t7qv` found an error in the
entry above, made one commit earlier.

`StrandLayoutForcesChain` forbids a **single generator** from joining
non-consecutive nucleons. It does NOT forbid a bond routed through **several**
generators. The sibling does exactly that —
`four_body_term_and_the_h12_collapse_probe.py:224`: *"bond between nucleons
i<j: strand 3i+2 routed rightwards to strand 3j"*, line 324 branching to a
single generator only when `j = i+1` and to `band_between` otherwise.

**So "more bonds" is NOT closed.** Band-routed bonds are a live escape.

### And it reconciles both disagreements at once

    adjacent bonds     exactly multiplicative -> order-independent, many-body ZERO
    band-routed bonds  DO NOT COMMUTE -- 11.12 % spread over one A=3 triangle's
                       six orders, 38-40 % over 4He's

So the structure this bean measured as absent reappears exactly where band
routing enters. And the numeric gap is explained: their `B(4He) = 10.387277`
against my adjacent-only `8.682248` is **two different bond sets, both computed
correctly** — not the colour arm (~1e-4), not an error on either side.

### Corrected status

| repair | status |
|---|---|
| rescale f_pp, f_pn, f_nn | **closed** — cancel in `alpha_relation` |
| irreducible many-body term | **closed on the adjacent set** — measured zero |
| add band-routed bonds | **OPEN — the live frontier** |

The parameter-free refutation stands, scoped to the ADJACENT bond set, which is
what `atom_canonical_crossings` builds and what every measurement here uses.

The sibling's finding that band routing does not close the gap either (still
-63 %, every many-body term negative) is **their** result, cited not re-derived,
and does not follow from anything proved on this branch.
