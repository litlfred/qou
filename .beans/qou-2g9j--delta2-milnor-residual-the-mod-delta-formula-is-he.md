---
# qou-2g9j
title: 'Delta=2 Milnor residual: the mod-delta formula is HELD (Mellor-Melvin), so the residual is not blocked'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T10:58:08Z
updated_at: 2026-09-04T22:13:09Z
---

Successor to `qou-768r` route 3, which closed the `Delta = 0` (min-span) family and
left the `Delta = 2` triples as its **stated residual** — the ones touching a linked
pair, where `mubar` survives as ONE BIT. Owner opened the carrier tranche; PR #6560
merged as `01bc067cd5`.

## THE RESIDUAL IS NOT BLOCKED — the mod-delta formula is HELD

`qou-768r` records route 3's blocker as "computing a `mubar` needs the Magnus
expansion of a longitude in the free group, which is real work and is not done",
and my own ledger said *"none of the five core route-3 works supplies"* it.

**That was too pessimistic, and the source that supplies it is one I had already
listed.** Mellor & Melvin, *A geometric interpretation of Milnor's triple linking
numbers*, Alg. Geom. Topol. **3** (2003) 557-568 — held at `library/0110001v3/` —
gives the **general mod-delta** formula, not just the `Delta = 0` case:

    mubar_ijk  ==  m_ijk(F) - t_ijk(F)   (mod delta)

  * `t_ijk(F)` = signed count of TRIPLE POINTS of `F_i ∩ F_j ∩ F_k` for oriented
    Seifert surfaces in general position (an integer);
  * `m_ijk(F) = e_ijk + e_jki + e_kij` in `Z/delta`, where `e_pqr(F) = eps_pq(w_r)`
    is the coefficient of `h_p h_q` in the Magnus expansion of `w_r`, and `w_r` is
    read off by walking `L_r` and recording each intersection with `F_p`, `F_q`.

Source: `library/0110001v3/sections/sec-001-2-the-formula-for-µ-ijk.md` (the
displayed formula and the Borromean worked example, `m_ijk = 1`), with the proof
in `sec-002`.

**It is diagrammatic**, so it is computable from a braid word — which is exactly
what the derived carrier gives us.

**Contrast with the other held source, and this is why the ledger's "none supplies
it" reads plausible:** `arxiv-1101.3374v1` (DeTurck et al., Pontryagin invariants /
integral formulas) is stated **only when the pairwise linking numbers vanish** —
verified in the held text at lines 218, 332, 1003. That is the `Delta = 0` case,
which route 3 already closed by a structural argument. So the integral-formula
literature really is silent on the residual; Mellor-Melvin is not.

## A SKETCH, EXPLICITLY NOT A RESULT

Working the formula against the carrier's chain structure suggests it vanishes, but
this has NOT been verified and is recorded as a direction, not a finding:

  * for a triple `a - b - c` in the chain, `a` and `c` share no summand, so `F_a`
    and `F_c` can be made disjoint => `F_a ∩ F_b ∩ F_c = empty` => `t_ijk = 0`;
  * `w_a` and `w_c` then each read only ONE other surface, so their two-letter
    Magnus coefficients vanish, leaving `m_ijk = eps_ac(w_b)`;
  * the source's own line 88 gives `eps_ij(w_k) + eps_ji(w_k) = mu_ik mu_jk`, and
    `delta | mu_ik`, so that product is `0 (mod delta)`.

The gap: this bounds the SYMMETRISED sum, not `eps_ac(w_b)` itself. Closing it needs
either the antisymmetric part or an explicit `w_b`. **Do not report the sketch as a
vanishing result.**

## What a real attempt needs

1. Seifert surfaces for the components of the derived carrier — the components are
   `(2, odd)`-TORUS KNOTS, not unknots (measured on main by
   `atom_closure_milnor_indeterminacy_probe.py`, exact-integer Kauffman bracket,
   both branches), so their Seifert surfaces are not discs and `t_ijk` is not free.
2. The `w_r` words from the braid diagram.
3. `eps_pq` via Magnus expansion in the free group on two meridians — small, since
   the words are short.

## Scope note carried forward

This bean is about `Delta = 2` ONLY. `Delta = 0` is closed (`qou-768r`, merged:
min-span triples are defined exactly where they vanish). `Delta = 1` carries no
information by definition. Nothing here reopens route 2, which is blocked for an
unrelated reason (the complement-genus handle is Borromean-only).



## RESULT 2026-09-04 — mubar VANISHES ON EVERY TRIPLE. Residual CLOSED.

Not just the `Delta = 2` residual: **every** triple, all three indeterminacy
classes, both crossing-resolution branches, 7 isotopes.

    triples with NONZERO mubar        0  of 606
    Delta = 0 (route 3's case)      260
    Delta = 2 (THE RESIDUAL)        256
    Delta = 1 (no information)       90

Stronger than route 3's own result, which was a STRUCTURAL vanishing on a chosen
subfamily. This is a COMPUTED VALUE on every triple.

### The controls are the point

An all-zero first run is exactly when a bug is most likely. The **Borromean rings**
(closure of `(s1 s2^-1)^3` in `B_3`, textbook `mubar_123 = +/-1`) run through the
SAME code path and are asserted NONZERO — measured `eps_01(lam_2) = -1`, with all
pairwise linking zero so `delta = 0` and the invariant is a genuine integer. The
**Hopf link** is asserted at `mu = 2`, `lk = 1`. Without those two the vanishing
would be indistinguishable from a broken implementation.

Convention recorded because it is a choice: `sigma_i` sends position `i` OVER
`i+1` (Artin). The Borromean control runs under the SAME convention, so a
convention flip surfaces as a failed control rather than as silent zeros.

### I DISPROVED MY OWN OBSTACLE, twenty minutes after writing it

The section above says *"what a real attempt needs: Seifert surfaces for the
carrier's components — and these are `(2, odd)`-torus KNOTS, not discs, so
`t_ijk` is not free."* **That was wrong, and it is the more useful of the two
errors on this bean.**

Mellor-Melvin's surface formula is ONE route. **Milnor's ORIGINAL definition needs
no surface at all**: `mubar_ijk = eps_ij(lambda_k) mod delta`, the degree-2 Magnus
coefficient of the `k`-th LONGITUDE — and for a BRAID CLOSURE the longitude is read
straight off the word (walk each strand; at each undercrossing record the meridian
of the over-strand, with sign). That is the entire implementation.

The pattern worth keeping: I reached for the formula in the source I had **just
read**, instead of for the definition. The sketch recorded above — `t_ijk = 0` by
disjoint surfaces, `m_ijk` reduced to `eps_ac(w_b)` — was never needed.

### Files

`computations/probes/milnor_mubar_vanishes_on_every_triple_probe.py` + witness,
5/5. PR #6634.

### Scope (a), on the carrier as given

These isotopes, these two branches, length-3 invariants. Does **not** say Milnor
invariants vanish generally — the Borromean control in the same file is a
counterexample to that reading. Length > 3 invariants NOT examined. Route 2
untouched (blocked for an unrelated reason: the complement-genus handle is
Borromean-only).



## 2026-09-04 — GENERICITY CHECK: the vanishing is generic, which WEAKENS the result above

Ran the check AGENTS.md demands on my own merged result (#6634 / `046296ff06`).
It applies to a VANISHING exactly as to a near-match.

    MONOTONE random words       238 words   1879 triples    0 nonzero mubar
    NON-MONOTONE random words   220 words   1456 triples   27 nonzero mubar

**The vanishing is generic for monotone closures.** Any monotone word would have
given it, so it says nothing about the framework's carrier CHOICE. Honest reading:

    NOT  "the derived carrier has vanishing Milnor triples, a fact about the carrier"
    BUT  "the framework's word is monotone, and monotone closures have vanishing
          Milnor triples"

**Unaffected:** route 3's `Delta = 2` residual is closed either way — the residual
does not care WHY `mubar` vanishes. **What changes:** the closure carries no
information about whether the carrier is the right object, which is the question
the carrier-derivation arc is actually about.

**Second positive control, in the same probe deliberately.** 27 nonzero over 1456
non-monotone triples proves the scan detects nonzero in the RANDOM regime, not only
on the hand-picked Borromean example. A monotone zero beside a non-monotone zero
would indict the scanner; beside a non-monotone nonzero it is a dichotomy.

**Third independent route to the monotonicity root.** #6561 from the algebra,
#6560 route 3 from the topology, this from random words — with a rate (~1.9 % of
non-monotone triples).

Figure hygiene: the docstring first quoted 251/2080 (an exploratory run consuming
the RNG in a different order). The probe's figures are 238/1879 at seed 20260904;
caught pre-commit, and the file now says do not quote 251/2080.

`computations/probes/milnor_vanishing_is_generic_for_monotone_probe.py`, 3/3.
Scope (a): a sampling result over one regime, not a theorem.


## 2026-09-04 — the cyclic square DOES reopen Milnor, and the all-positive arm already did

Closing the residual `cyclic_square_does_not_reopen_milnor_probe.py` named in its own
witness ("inserted crossings are all positive. A mixed-sign insertion could cancel a
linking number and is not covered"). The answer corrects that probe's **framing**, not
its measurement.

**Its measurement is confirmed**, and now through a second independently written
`analyse`: 694 insertions, 188 span three components, **0** with all three pairwise
linking numbers zero. Byte-identical to the merged figures.

**Its inference fails.** It concluded "route 3's conclusion does not break, on this
shape" from `Delta != 0 => mubar is not a genuine integer there anyway`. That conflates
*not an integer* with *no obstruction*: `mubar` lives in `Z/Delta`, and a nonzero
residue is a nonvanishing invariant. It never computed `mubar`. Computing it, in that
probe's **own all-positive arm**:

    4He, position 25, m=5,  lk = [0, -2, 0],  Delta = 2,  mubar = 1
    8Be, position 77, m=17, lk = [0, 0, -2],  Delta = 2,  mubar = 1

`Delta = 2` with `mubar = 1` is exactly the one bit route 3's stated `Delta = 2`
residual is about. That probe's own scope note already said "the Delta = 2 one-bit
triples are untouched" — the scope note is right and the title is not.

**All 16 inserted-sign patterns**, 3008 spanning triples:

    Delta = 0     0   ->    0 nonzero      Delta = 3   373   ->  187 nonzero
    Delta = 1  2259   ->    0 nonzero      Delta = 4   371   ->  371 nonzero
    Delta = 2     5   ->    5 nonzero      TOTAL              ->  563 nonzero

**The join is sign-independent**, exactly: `span3 = 188` for every one of the 16
patterns, because the insertion's permutation `s_m s_{m+1} s_m s_{m+1}` is a 3-cycle
whatever the signs are. Signs move only the linking *values*. That is why `Delta = 0`
stays unreachable in every pattern while `mubar` is nonzero in 563 cases.

**Not a refutation of route 3.** Route 3 and `MilnorTriplesAreDefinedExactlyWhereThey
Vanish.lean` are about the *unperturbed* carrier at `Delta = 0`; control A re-measures
that null (294 triples, 0 nonzero) through this harness, so the nonzero counts are not
an artifact. Control B: Borromean gives nonzero.

Scope (a): one insertion shape, all-`sigma^-1` base branch, sampled positions, 4
isotopes. Probe `computations/probes/mixed_sign_cyclic_square_does_reopen_milnor_probe.py`,
5/5, idempotent, integer arithmetic throughout.
