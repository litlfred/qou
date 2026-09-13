---
# qou-qqm4
title: 'DERIVE c2: the second-order hbar_q coefficient of the trace difference -- and why the pairwise chain is nearly additive at that order'
status: in-progress
type: task
priority: high
created_at: 2026-09-03T15:51:43Z
updated_at: 2026-09-13T13:07:38Z
updated_at: 2026-09-13T12:47:52Z
---

Successor to qou-pdg9 (c1 derived, PR #6492). Exact c2 = [eps^1]+[eps^2] of Dtr(1+eps) is in c1-leading-coefficient-derived-probe.witness.json: pp 357/32, pn 403/32, nn 217/16, T 3285/128, 3He 3451/128 (4He pending, order-4 series). Observation from that data: chain/atom at SECOND order is 3348/3285 = 1.019 (T) and 3040/3451 = 0.881 (3He), against 292/163 = 1.79 and 30/17 = 1.76 at first order -- the over-count nearly cancels one order up. qou-zrx2 called the q0 agreement 'higher-order terms partially cancelling'; this quantifies it exactly. Goal: (1) 4He c2 exact; (2) derive c2 by extending the [star] expansion to second order (the Y-terms Tr(Y P Y P') no longer vanish; K'' and the normaliser's second derivative enter); (3) explain the near-additivity structurally or refute it as coincidence at A=4.



2026-09-03: 4He c2 EXACT = 15307/512 (order-4 series, 15 min). Second-order chain/atom ratios: T 3348/3285 = 1.019, 3He 3040/3451 = 0.881, 4He (597/16)/(15307/512) = 19104/15307 = 1.248 -- against 1.79 / 1.76 / 3.43 at first order. So the second-order over-count is much smaller than the first-order one but is NOT uniformly ~1; 'nearly additive' in the title overstates 4He. Tensor-picture engine (tensor_picture_markov_trace_probe.py) reproduces the seminormal Markov trace on the deuteron words to every computed order for BOTH R-matrix h-placements -- both must, by uniqueness of the Markov trace at fixed loop value.



2026-09-03 (later): c2 DERIVED. The tensor-picture generator is EXACTLY s + diag((q-1), 0, h, (q-1)), so tr_M(word) = sum over subsets S of letters of fixed-point counts of the sub-word with S deleted, weighted by diagonal pattern scalars; order eps^k needs |S| <= k. c2_diagonal_insertion_expansion_probe.py reproduces c0, c1 and the exact c2 of all six words (4/4, 231 s). c2 by insertion class |S| = 0/1/2: pp 0, 9/4, 285/32; pn 0, 71/32, 83/8; nn 0, 35/16, 91/8; T 5/32, 321/128, 23; 3He 5/32, 41/16, 3103/128; 4He 11/64, 127/64, 14203/512 -- the pair class dominates. Lean: TensorPictureGenerator.lean (R = s + D(q), Hecke relation, Tr(K R)/(1+q^2)^2 = z_D, D(1+eps) expansion, Y anticommutes with s, Tr Y = 0), lean-direct exit 0.



DONE — PR #6521 merged (a2e07cef4c). c2 derived by the diagonal-insertion expansion; every order is a fixed-point count over sub-words. Schur-Weyl checked on the D/T/3He words. Lean: TensorPictureGenerator.lean, lean-direct exit 0, no sorryAx.

SUCCESSOR (new bean): does the eps-series converge at q_0 = 1.11? The coefficients grow 1/8 -> 19/8 -> 357/32 (ratios 19, 4.70). If the ratio settles below ~9 the series converges at eps = 0.11 and the expansion is a COMPUTE route to A=5,6 (cost 2^n C(L,<=k), vs 15! for the direct trace). If not, it is a structural tool only. Decisive and cheap at n=6.


## 2026-09-06 — REOPENED: the six c2 values are the PRE-2026-09-05 word, MEASURED

Probe: `computations/probes/c2_is_stale_on_the_reordered_atom_word_probe.py`.

This bean completed **2026-09-03**; the atom word changed **2026-09-05** (owner ruling
`qou-hu1f`). Sibling `qou-pdg9` was already reopened for the same cause at first order
(c1 moved up to 163x). Measured here rather than inferred from the dates — all six moved:

    case   c2 canonical (measured)   c2 recorded (grouped)   ratio
    pp            1.0312552               357/32  = 11.156    10.8x
    pn            0.78125616              403/32  = 12.594    16.1x
    nn            0.062506813             217/16  = 13.563   217.0x
    T             0.77344459             3285/128 = 25.664    33.2x
    3He           1.2265703              3451/128 = 26.961    22.0x
    4He           0.85742792            15307/512 = 29.897    34.9x

**Convention settled, not assumed.** This bean's c2 is described as [eps^1]+[eps^2] of
Dtr(1+eps); the probe uses the hbar_q expansion, so a bare disagreement would be
uninterpretable. The self-test resolves it: the SAME measurement on the grouped word returns
c1 -> 2.3125 = 37/16 and c2 -> 12.59375 = 403/32, reproducing BOTH recorded deuteron
coefficients. So the conventions agree and the canonical column is about the word.

**The self-test also caught a real bug in the probe itself:** `tr_m_atom_via_transfer` does
`from mass_at_3A_proper import atom_braid_word_3A`, so it holds its own name; patching only
`M.atom_braid_word_3A` left the consumer on the original and the 'grouped' run returned the
CANONICAL c1. Both namespaces are now rebound.

**🛑 EXACT CANONICAL RATIONALS ARE NOT ESTABLISHED.** Richardson error ~1e-5 at eta = 1e-6 is
four orders too coarse to identify a denominator <= 4096; `limit_denominator` returns
4223/4095, 3193/4087, 2598/3359 — noise fits, not answers, and they are deliberately not
recorded. Only nn is near a simple rational (1/16 vs 0.062506813) and that is a GUESS. The
exact values need this bean's own exact-Fraction eps-series route. **That is the remaining
work.** What IS established: all six moved by 10x-217x, far outside any extrapolation error.

**Downstream — the second-order chain/atom ratios move materially:**

    ratio                        recorded   canonical
    T    (c2pn + c2nn)/c2T          1.019      1.0909
    3He  (c2pp + c2pn)/c2He3        0.881      1.4777
    4He  (c2pp+c2pn+c2nn)/c2He4     1.248      2.1868

The reading that the first-order over-count 'nearly cancels one order up' is weaker under the
canonical word and at 4He much weaker — it roughly doubles. So
`docs/audits/2026-09-04-c2-does-not-continue-the-cancellation.md` is stale in its numbers,
though its title's conclusion holds a fortiori.

Contrast FIRST order, where `chain_over_atom_He4_generic` (PR #6920) proves the 4He ratio is
24/7 for EVERY deletion-sum pair. No such invariance is claimed or observed at second order,
and these numbers are evidence against one.


### Same day — FIVE of the six exact canonical values ARE established (correcting my own note above)

The entry above says the exact canonical rationals are 'not established' and that getting them
'needs this bean's own exact-Fraction eps-series route'. **The second half was wrong**: that route
is already in the corpus AND already canonical. `c1_leading_coefficient_derived_probe.tr_M_series`
computes the exact series through the validated seminormal pipeline and reaches the word via
`atom_canonical_crossings`, whose `intra_order` default became `borromean` with the ruling. It
needed **re-running, not redoing**. Driven directly (not through that probe's `main`, which would
rewrite a committed witness):

    case   [eps^1]   [eps^2]    c2 = [e1]+[e2]     recorded (grouped)
    pp     1/8       29/32      **33/32**          357/32
    pn     1/16      23/32      **25/32**          403/32
    nn     0         1/16       **1/16**           217/16
    T      1/64      97/128     **99/128**         3285/128
    3He    1/8       141/128    **157/128**        3451/128
    4He    -         -          pending (n=12)     15307/512

**Self-test 3/3** on the A=2 cases: the same driver on the grouped word returns 357/32, 403/32,
217/16 — the recorded values exactly. **And every [eps^1] reproduces PR #6920's c1** (1/8, 1/16, 0,
1/64, 1/8) by a route with no connection to [*] — an independent confirmation of that closed form.
All five agree with the Richardson column to its extrapolation error, so the earlier 'nn ~ 1/16'
guess is now confirmed rather than guessed.

**Remaining: 4He only** (n = 12 order-4 series, ~15 min). Command for any case:

    python3 computations/probes/c2_is_stale_on_the_reordered_atom_word_probe.py \
        --exact-cases pp pn nn T 3He 4He


### ALL SIX exact canonical c2 established (completes the entry above)

4He landed: **c2 = 439/512** ([eps^0] = 7/128 = c0(4), [eps^1] = 7/128 = the canonical c1). So the
table above completes:

    case   [eps^1]   [eps^2]    c2 = [e1]+[e2]     recorded (grouped)
    pp     1/8       29/32      **33/32**          357/32
    pn     1/16      23/32      **25/32**          403/32
    nn     0         1/16       **1/16**           217/16
    T      1/64      97/128     **99/128**         3285/128
    3He    1/8       141/128    **157/128**        3451/128
    4He    7/128     411/512    **439/512**        15307/512

**Every [eps^1] reproduces PR #6920's c1** (1/8, 1/16, 0, 1/64, 1/8, 7/128) by a route with no
connection to [*] — an independent confirmation of that closed form through the exact series. All
six agree with the Richardson column to its extrapolation error.

**Exact second-order chain/atom ratios:**

    ratio                        recorded (grouped)      canonical (exact)
    T    (c2pn + c2nn)/c2T        3348/3285  = 1.019     **12/11**   = 1.0909
    3He  (c2pp + c2pn)/c2He3      3040/3451  = 0.881     **232/157** = 1.4777
    4He  (c2pp+c2pn+c2nn)/c2He4  19104/15307 = 1.248     **960/439** = 2.1868

The 'over-count nearly cancels one order up' reading is weaker under the canonical word and at 4He
roughly doubles. `docs/audits/2026-09-04-c2-does-not-continue-the-cancellation.md` is stale in its
numbers; its title's conclusion holds a fortiori.

**Nothing analogous to the first order's invariance appears here.** At first order
`chain_over_atom_He4_generic` proves 24/7 for EVERY deletion-sum pair; 12/11, 232/157 and 960/439
share no such structure, and are evidence against a second-order analogue.

**Remaining on this bean:** a closed form in (Z,N) for c2, as PR #6920 gives for c1. Six exact
points do not fix one — do not guess.


### Same day — WHY things survive the ruling: the content-cancellation criterion (tested)

Probe: `computations/probes/content_cancellation_invariance_probe.py`.

The ruling fallout had been case-by-case (c0 survives, c1 moves 163x, c2 moves 10-217x, the 4He
first-order chain ratio 24/7 survives, the mirror difference survives at first order but not
second). One rule accounts for all of it:

**A linear combination of SAME-A isotope coefficients whose NET NUCLEON CONTENT IS ZERO is
invariant under any intra-nucleon reordering, at EVERY order** — because such a combination cancels
every per-nucleon contribution identically, leaving only INTERFACE data, and interfaces are single
letters OUTSIDE the nucleon blocks, unreachable by a reordering within one.

    combination                        net (p,n)   c1 canon/grouped   c2 canon/grouped
    X(pp) + X(nn) - 2X(pn)      [A=2]    (0,0)      0     / 0         -15/32 / -15/32  OK
    X(3p) + X(3n) - X(T) - X(3He) [A=3]  (0,0)      0     / 0           9/64 /   9/64  OK
    X(T) - X(3He)               [A=3]   (-1,+1)    -7/64 / -7/64      -29/64 / -83/64  differs

**Row 2 is a HELD-OUT test.** The criterion was stated from row 1 alone; row 2's combination was
then chosen because 3p+3n and T+3He carry the same content, and c2(3p) = 117/64, c2(3n) = 5/16
(canonical) / 963/32, 1451/64 (grouped) were computed AFTERWARDS purely to test it. Coefficients are
fixed by content bookkeeping, not fitted. Row 3 is the control and fails invariance exactly as
predicted.

Incidentally all four new A=3 species reproduce PR #6920's c1 closed form at [eps^1] (19/64, 181/64,
19/8, -5/32) — 4 more independent confirmations.

**Note the first-order column: both content-cancelling combinations are 0, not merely equal.** So at
first order the surviving interface terms cancel too (pp -4 and nn +4 against pn 0). At second order
they do not — -15/32 and 9/64 — which is the substance: interface-interface cross terms enter one
order up. That is also the concrete form of this bean's original 'the Y-terms Tr(Y P Y P') no longer
vanish'.

**This SHARPENS the MirrorAsymmetrySign caveat rather than removing it.** That file survives the
ruling and its docstring calls the invariance 'measured on two words, not structural'. Row 3
confirms it: the mirror difference does not cancel content, so the criterion gives it no protection;
its c1 invariance is the coincidence that P - Q = (S_p - S_n)/2 is 5 for both words, and its c2
invariance FAILS. Do not promote that file's invariance to a structural one.

**NOT a proof** — a criterion stated from one case, tested on a second, with a control, at orders 0,
1 and 2 only. It constrains COMBINATIONS, not individual values, so it gives no closed form for c2.


### Same day — the FREE side's second order is forced by its first (probe, 8/8 incl. held-out 4He)

Probe: `computations/probes/free_word_second_order_product_structure_probe.py`. This is progress on
goal (2) for HALF the object; it does not attempt the atom word.

With u(Z,N) = (Z*S_p + N*S_n)/2 = 3Z - 2N (the c1 per-nucleon sum, PR #6920):

    [e1](free)          = u * 2^(-A-1)
    2^(A+2) * [e2](free) = u^2/2 + (37Z + 20N)/2

Exact, 7/7 across every (Z,N) split at A = 2 and 3, plus the **held-out 4He** (A=4, n=12, in
neither the fit nor the pattern search): predicted [e1] = 1/16, [e2] = 59/64; both measured exactly.

**The three quadratic coefficients (9/2, -6, 2) are FORCED by u^2/2** — fixed the moment u is known
from the FIRST order, with nothing about the second order choosing them. Only (37, 20) was free. So
8 exact points against 2 parameters. (37, 20) is the second-order analogue of (S_p, S_n) = (6, -4).

**🛑 MY MECHANISM WAS WRONG and is retracted.** I read u^2/2 as an exponentiation signature — the
free word's A nucleon blocks act on disjoint strand triples, so the normalised trace should
factorise, log be additive, and second order be (first order)^2/2 + per-nucleon terms. That needs u
to BE the first-order coefficient in the same normalisation. It is not: [e1] = u*2^(-A-1), so
([e1])^2/2 = u^2 * 2^(-2A-2)/2, differing from the measured u^2/2 * 2^(-A-2) by a factor 2^(-A). The
probe's own prediction column caught it (an earlier version asserted u = 2^(A+2)*[e1], which is 2u,
and every row printed FAIL). What survives is a RELATION BETWEEN THE ORDERS with no mechanism —
still the useful half, since it is what makes this 2 parameters rather than 5.

**Does NOT give c2.** c2 = [e1]+[e2] of tr(free) - tr(atom); the atom word does not factorise (its
interfaces couple adjacent blocks, which is why c1's closed form needs a separate interface term).
Nothing here says what the atom side's second order is.


### Same day — the ATOM side's [e2], as exact data (not fitted)

Since c2 = [e1]+[e2] of Dtr = tr(free) - tr(atom) and [e1](Dtr) = c1, the atom half follows from
quantities already measured, with NO new computation: **[e2](atom) = [e2](free) - (c2 - c1)**.

    (Z,N)   A   [e2](atom)   x 2^(2A)    I_pp  I_nn
    (2,0)   2   81/32        81/2        1     0
    (1,1)   2   35/32        35/2        0     0
    (0,2)   2   27/16        27          0     1
    (3,0)   3   47/32        94          2     0
    (2,1)   3   79/128       79/2        1     0
    (1,2)   3   59/128       59/2        0     1
    (0,3)   3   33/32        66          0     2
    (2,2)   4   61/512       61/2        1     1

**NO CLOSED FORM IS PROPOSED, deliberately.** Eight points admit several parameterisations (a
quadratic in (Z,N) alone is five parameters before any interface term) and this arc has been burned
by exactly that. Two facts for whoever derives it:

- **The obvious analogue of the free-side result FAILS.** Taking v = u + 4(I_pp - I_nn) — the
  first-order atom bracket — leaves x2^(2A) - v^2/2 at -19/2, 17, -5, -101/2, 15/2, 17, -32, 57/2,
  which is not linear in (Z,N).
- **The parity is uneven** — three integers, five half-integers — so any form must produce that.

**The one constraint in hand** is the content-cancellation criterion: a zero-net-content combination
of the atom-side second order must be ordering-invariant, being interface-only. Consistency check at
A=2: atom(pp)+atom(nn)-2atom(pn) = 65/32 vs free = 50/32, difference -15/32 — exactly the measured c2
combination, as it must be since the [e1] part cancels there.

So the remaining work on goal (2) is the atom side alone, and it is now well-posed: 8 exact target
values, one invariance constraint, and one refuted ansatz.


### Same day — a THIRD stale artifact, and the first that is a COMMITTED WITNESS

`computations/probes/c2-diagonal-insertion-expansion-probe.witness.json` (computedAt
**2026-09-04**, the day before the ruling) contains all six **grouped** c2 values — 357/32, 403/32,
217/16, 3285/128, 3451/128, 15307/512 — and none of the canonical ones. Unlike qou-pdg9 and
qou-qqm4, which are beans, **this is a committed record on main that a consumer reads.**

Its producer `c2_diagonal_insertion_expansion_probe.py` implements the diagonal-insertion expansion
[<>] — an exact, ALL-ORDERS derivation of the Markov trace as a fixed-point count over sub-words, of
which [*] is the |S| <= 1 case. It reaches the word through `atom_canonical_crossings`, so like the
eps-series it is **canonical by default and needs RE-RUNNING, not rewriting**. Not done here: its
main() writes the witness, and rewriting a committed witness is a separate deliberate act.

**This also settles what my 'next' should have been.** I had queued 'derive the second-order analogue
of [*] over letter pairs' as the remaining work. That derivation ALREADY EXISTS — [<>] is all-orders
and [e2] is its |S| <= 2 case, with the probe reporting the |S| = 0,1,2 class split per word
explicitly as 'the raw material for' a closed form. Corpus-grep caught this before the tranche was
spent; it is the third such catch this session.

So the remaining work on goal (2) is narrower than 'derive the second order': it is **re-run [<>]
canonically and read the class split**, then find the (Z,N) form from the pair terms. And that
probe's own docstring already declines to assert a closed form, so not fitting one is the corpus's
position and not merely mine.


### [◇]'s witness is refreshed — canonical, 4/4, and a THIRD stale table came with it (2026-09-06, PR #6920)

`c2-diagonal-insertion-expansion-probe.witness.json` no longer carries the grouped values. Re-run on
the canonical word, 252 s, 4/4 assertions, all six `c₂` matching the tables this branch repaired.
**The class split this bean asked for, canonical:**

    case  (Z,N)   A   |S|=0    |S|=1      |S|=2      c₂
    pp    (2,0)   2   0        7/8        5/32       33/32
    pn    (1,1)   2   0        27/32      −1/16      25/32
    nn    (0,2)   2   0        13/16      −3/4       1/16
    T     (1,2)   3   5/32     123/128    −11/32     99/128
    ³He   (2,1)   3   5/32     65/64      7/128      157/128
    ⁴He   (2,2)   4   11/64    25/32      −49/512    439/512

**ONE STRUCTURAL FACT IS ALREADY VISIBLE, and it is not a fit.** The `|S| = 0` column is
**species-blind** — it depends only on `A`. All three `A = 2` words give `0`; both `A = 3` words
give `5/32`; `⁴He` gives `11/64`. Six points collapse to three, with no parameter chosen. That is
the second-order shadow of the same fact at order `ε⁰`, where `c₀ = 2^(−A)(1 − 2^(−O))` likewise
sees only the interface pattern. So the species dependence of `c₂` lives entirely in `|S| = 1` and
`|S| = 2`.

**THE THIRD STALE TABLE.** Repairing this file earlier I fixed `RECORDED_C1` and `EXACT_C2` and
stopped, because those are the two the assertions compare against. Forty lines below them sat

    first = {"T": F(292, 163), "3He": F(30, 17), "4He": F(24, 7)}

the FIRST-order chain/atom ratios the second-order assertion measures against — hardcoded from the
grouped word. Nothing compared to it, so nothing failed; it simply wrote grouped numbers into a
witness whose every other field was canonical. **It is now DERIVED from `RECORDED_C1`.**

    T     292/163 = 1.7914  →  4
    ³He    30/17  = 1.7647  →  3/2
    ⁴He    24/7           →  24/7   (unchanged)

⁴He's invariance is not luck — `pp+pn+nn` and `⁴He` carry the same nucleon content, so the ratio is
ordering-invariant by the content-cancellation criterion, and `chain_over_atom_He4_generic` proves
it algebraically. T and ³He have `Z ≠ N` and moved.

**AND THE ASSERTION IT FEEDS IS NOW MARGINAL — read this before quoting it.** "Second-order
over-count is smaller than first-order" still holds 3/3, but:

    |ratio − 1|    second    first
    T              0.0909    3.0000
    ³He            0.4777    0.5000     ← clears by 4.5 %
    ⁴He            1.1868    2.4286

Under the grouped data ³He read 0.1191 vs 0.7647 and looked comfortable. It is not. Do not cite this
as evidence the over-count is controlled at second order. (Its source string had two further defects,
both fixed: it printed the RATIOS while labelling them `|ratio − 1|`, and quoted a hardcoded grouped
`1.248` for ⁴He.)

### The next step on goal (2), and why it is a TEST rather than a fit

The `c₁` closed form has the shape `a(A)·u + b(A)·(I_pp − I_nn) + c(A)` with `u = 3Z − 2N`. Ask
whether `|S| = 1` at second order has the same shape. At `A = 2` the three species give a
**degenerate** system — `pp + nn` reproduces `pn` exactly, so one parameter stays free — and `A = 3`
supplies only two equations from T and ³He. **Three parameters need four species at one `A`.**

So: measure `3p` and `3n` (`A = 3`, `n = 9`, ~15 s each), solve the three parameters from three of
the four, and **predict the fourth**. A held-out species at the same `A` is a real test; three points
against three parameters would not be. If it fails, the shape is wrong and that is the finding.

Deliberately NOT done: reading a form off the six points above. Six points admit many
parameterisations and this arc has been burned by exactly that.


### `A = 5` verdict: the `k(A)` form is REFUTED — and the `|S| = 2` pair-class decomposition (2026-09-06, PR #6920)

**The zero-dof fit died, as a zero-dof fit should.** `m(A) = (3/8)4^A + (15/2)2^A − 23` reproduced
`13, 61, 193` with three parameters on three points. `⁵He` (`Z=2, N=3`, `n = 15`, `2¹⁵` basis
states, 49 min) gives:

    m(5)  predicted 601   measured 521   MISS by 80/2¹⁰

Sequence `m(A) = 13, 61, 193, 521` at `A = 2…5`. **No closed form is offered for it** — a fourth
point does not license a four-parameter fit any more than the third licensed the three-parameter
one. This is the cheaper outcome to have learned: the form was going to be quoted otherwise.

🛑 **My stated prediction was wrong before the run refuted it.** Three artifacts said
`k(5) = 663/2¹⁰`; `(3/8)·4⁵ + (15/2)·2⁵ − 23 = 384 + 240 − 23 = 601`, so the arithmetic error was
mine. Verdict unaffected (601 misses 521 too), but the wrong number was in
`c2_pairwise_shape_holdout_probe.py`, the `qou-pdg9` bean and PR #6920's body — all three corrected.

⚠ **What the `A = 5` run does NOT test:** species-independence of `k` at `A = 5`. One species yields
one residual; it is consistent with the relation and cannot check it. Species-independence stays
measured at `A = 2, 3, 4` (8 species, 3 constants). A second `A = 5` species would test it, ~49 min.

**Positively established at `A = 5`:**

- `c₁`'s closed form holds — measured `1/256`, predicted `1/256`. Eighth independent size, largest
  word ever put through `[◇]`.
- New exact values: `c₂(⁵He) = 1001/2048`; class split `|S|=0: 67/512`, `|S|=1: 523/1024`,
  `|S|=2: −313/2048`.

### And `|S| = 2` is now split by letter-PAIR class — the break is in THREE of four

Letters are nucleon (`g % 3 ∈ {0,1}`) or interface (`g % 3 == 2`), so every pair is `intra` /
`cross` / `n-if` / `if-if`, read off the generators. The four classes **sum to `[◇]`'s `|S| = 2` on
7/7 words** — an independent recomputation of that witness by a different accumulation.

    case   (Z,N)    intra     cross     n-if    if-if      sum = [◇]
    pp     (2,0)     1/2      9/32      −5/8       0         5/32
    pn     (1,1)       0     −3/16       1/8       0        −1/16
    nn     (0,2)    −1/2       1/8      −3/8       0         −3/4
    3p     (3,0)    9/16    81/128      −1/2    −1/8       73/128
    T      (1,2)   −3/16     −3/16      1/32       0       −11/32
    ³He    (2,1)    3/16    −9/128     −1/16       0        7/128
    3n     (0,3)   −9/16      9/32     −5/16    −1/8       −23/32

Per-class leave-one-out at `A = 3`: **`intra` AFFINE 4/4; `cross`, `n-if`, `if-if` all 0/4.** So the
non-affinity is **not localised to one class** — that is a weaker answer than the question hoped for
and it is the answer.

Two shapes stated from the table and then checked:

- **`intra = (Z − N)·κ(A)`**, `κ(2) = 1/4`, `κ(3) = 3/16`. Seven species, two constants — five dof —
  exact throughout, including the `Z = N` species where it must give `0`. `Z − N` is affine in
  `(u, D)`, which is *why* this class passes the leave-one-out.
- **`if-if = −(1/8)·[C(I_pp,2) + C(I_nn,2)]`** — a count of ways to pick two interfaces *of the same
  kind*. Its dof are thin and the file says so: `A = 2` contributes nothing (count and class both
  `0`), so the content is four `A = 3` species against one coefficient. The value is the **shape** —
  a like-interface *pair* count is quadratic in `(I_pp, I_nn)`, so no affine form in `D` can reach
  it. A mechanism for the MISS, not a fit to it.

**`cross` and `n-if` deliberately unmodelled.** `cross` runs over distinct nucleon pairs so it
should be quadratic in content; a full quadratic in `(u, D)` is six parameters and `A = 5` has
exactly six species, so it is **unfalsifiable at every reachable `A`** (`A = 6` is `n = 18`). The
route is to COUNT pair types, not fit them — this decomposition is that groundwork.

Probes: `c2_pairwise_shape_holdout_probe.py`, `c2_pair_class_decomposition_probe.py` (exact
`Fraction`s, no `q`, no witness).


### The free word IS a product — my retraction of that mechanism was WRONG (2026-09-06, PR #6920)

**Correcting my own claim, recorded here because this bean carries the copy of it.** Earlier in this
session I retracted the factorisation reading of the free word's second order and wrote that the
relation had "no mechanism attached". It has one, and it was the one I first proposed.

`tr(free; Z,N) = tr(p)^Z · tr(n)^N`. Writing each single-nucleon series as `a(1 + rε + qε² + …)`,
measured independently at `n = 3`:

    a_p = a_n = 1/2      r_p = 3/2, r_n = −1      q_p = 23/4, q_n = 3

Everything at order 2 follows with **zero free parameters**, 7/7 exact:

    [ε⁰] = 2^(−A)
    [ε¹] = (Z r_p + N r_n)·[ε⁰] = u·2^(−A−1)
    [ε²] = [Z q_p + N q_n + (σ₁² − σ₂)/2]·[ε⁰]
    intra(free) = (2Z − 2N)·[ε⁰]      cross(free) = [C(Z,2)r_p² + ZN r_p r_n + C(N,2)r_n²]·[ε⁰]
    n-if(free) = if-if(free) = 0      (verified, not assumed)

**Two constants this arc called "new data" are now derived.** `(S_p, S_n) = (6, −4)` — `c₁`'s only
ordering-dependent input, the thing this whole branch turned on — is `4·(r_p, r_n) = 4·(3/2, −1)`.
And `(37, 20)`, which the probe called "the only fitted pair", falls out of `q_p, q_n`: the identity
`4[Z q_p + N q_n + (σ₁² − σ₂)/2] == u²/2 + (37Z + 20N)/2` holds exactly on all 8 `(Z,N)` at
`A = 2,3,4`. So that form is **8 points against ZERO free parameters**, not two.

**Where my retraction went wrong.** I said factorisation fails because `([ε¹])²/2` is off from the
measurement by `2^(−A)`. Multiplicativity never predicts `([ε¹])²/2`:

1. **The normaliser was squared.** `[ε¹]` already carries `[ε⁰] = 2^(−A)`; a product's cross term is
   `Σ_{i<j} r_i r_j·[ε⁰]`, with `[ε⁰]` appearing **once**. Squaring `[ε¹]` squares it — that stray
   `2^(−A)` is exactly what I read as the refutation.
2. **The self terms were not subtracted.** `Σ_{i<j} r_i r_j = (σ₁² − σ₂)/2`, not `σ₁²/2`; part of
   the linear `(37Z + 20N)` comes from `−σ₂/2`. No version of "(first order)²/2" can be right.

The probe's own prediction column agreed with the retraction because it had been written to the same
wrong expression. **A self-check only checks what you encoded.**

**Contaminated and now corrected:** the 🛑 box in
`free_word_second_order_product_structure_probe.py` (rewritten), finding 5 of PR #6920's body, and
this bean. The *measured relation* was right throughout; only its status moves, from "empirical, 2
free parameters" to "derived, 0".

**Where this leaves goal (2).** The **free** side of `c₂` is now fully derived at orders 0, 1, 2 —
every class. What remains is entirely the **atom** side: `n-if` and `if-if` of `Δtr` are pure
atom-side data (the free word contributes exactly 0 to both, verified), and `intra` and `cross` each
have a free half now known and an atom half that is not. That is a much sharper statement of the
remaining work than "derive `c₂`".

🛑 Factorisation is **not proved** — disjoint strand triples is an argument, and 7 words across three
orders and four pair classes is evidence. A Lean `tr(free; Z,N) = tr(p)^Z tr(n)^N` would settle it
and does not exist. Worth opening as its own item.


## 🟢 GOAL (2) IS ANSWERED — `c₂` in closed form, as a BOND PRODUCT (2026-09-06, PR #6920)

`c₂` has a closed form. It is **not** a form in `(Z, N)` alone — which is why the `(u, D)`
leave-one-out had to miss, and that MISS is now explained rather than merely recorded. It is a form
in the **ordering**:

    tr(atom) = ∏_nucleons a(1 + rε + qε²) · ∏_bonds (1/2)(1 + ρ_b ε + τ_b ε²)

The atom word is a **chain**: `A` nucleon blocks on disjoint strand triples joined by `A − 1` single
interface letters at generators `3k + 2`, and its trace is the corresponding product. Every factor
is **measured on a smaller object**, never fitted:

    proton    a = 1/2   r = 3/2   q = 23/4      measured at n = 3, one nucleon, free word
    neutron   a = 1/2   r = −1    q = 3
    bond pp   (1/2)(1,  2, 1/2)                 measured at A = 3 by turning ONE interface on
    bond pn   (1/2)(1,  0, 3/2)                 (`m_pp` / `m_pn` / `m_nn` select which)
    bond nn   (1/2)(1, −2, 5/2)

With `Δ = tr(free) − tr(atom)`: **9/9 on `c₀`, `c₁` AND `c₂` across `A = 2…5`** — `pp, pn, nn, 3p,
T, ³He, 3n, ⁴He, ⁵He`. Five measured series predict 27 numbers, no free parameter at any step.
`--verify-live` re-measures the `n ≤ 9` targets rather than trusting the recorded table; passes too.

**Why it is not a fit, twice over.** The bond factors come from **one-interface** words, so every
prediction is for a **multi-interface** word — even T and ³He, which supplied the extraction, are
real tests of the *product*. And `A = 2` (three words), `A = 4` and `A = 5` contributed nothing to
any input; ⁵He was computed for the unrelated `k(A)` refutation before this form existed.

**Every earlier finding on this bean is now a corollary:**

- `c₀ = 2^(−A) − 2^(1−2A)` is the `ε⁰` part: `2^(−A)` over nucleons times `2^(−(A−1))` over bonds.
  Interfaces act **multiplicatively** (each halves the leading term) — measured directly, and it is
  why the `Δ` of one interface is *not additive* over interfaces.
- `(S_p, S_n) = (6, −4)`, `c₁`'s only ordering-dependent input, is `4·(r_p, r_n)`.
- `(37, 20)` falls out of `q_p, q_n`.
- The `|S| = 2` pair classes are this product's second-order terms: `intra` from one nucleon's `q`,
  `cross` from two nucleons' `r`, `n-if` from a nucleon and a bond, `if-if` from **two bonds** —
  which is exactly why `if-if` counts *pairs of like interfaces* and cannot be affine in
  `I_pp − I_nn`.

The bond factors fall into a pattern, `ρ_b = p_b − n_b` and `τ_b = 1/2 + n_b`. That is a
*description* of three measured values with one spare dof and is **not** what the form uses, so
nothing rests on it; it is the shape a derivation would have to produce.

### 🛑 What is NOT established — read before quoting

1. **Sorted orderings only.** Every word is `p…p n…n`, because `atom_canonical_crossings` takes
   `(Z, N)`. The bond product is *stated* for an arbitrary ordering and is **untested** on one;
   `pnp` is the discriminating case and needs the canonical construction extended, not a hand-built
   word. Corollary: only the `(p, n)` orientation of the mixed bond ever occurs, so treating
   `(n, p)` as the same factor is an **assumption**, inert here.
2. **Orders 0, 1, 2 and `A ≤ 5` only.**
3. **NOT PROVED.** Disjoint blocks and single-letter bonds is a structural argument; 9 words × 3
   orders exact is evidence. Neither the bond product nor the free-word factorisation has a Lean
   statement — that is the formalize-first follow-on and is the highest-value next item on this arc.
4. **No `q₀` anywhere.** Exact rational ε-coefficients, wired to nothing, no witness, no content
   block.

Probe: `computations/probes/atom_bond_product_closed_form_probe.py`.


## 🛑 CORRECTION to the "goal (2) answered" section above — the bond half was ALREADY in the corpus

Measured, not suspected: `computations/probes/bond_factors_are_z_plus_d_probe.py`, 3/3.

The three bond factors that section calls "measured at `A = 3` by turning ONE interface on" are
**exactly** the corpus's `∏ᵢ (z + dᵢ)`, coefficient for coefficient:

    bond   the "measured" factor      z + d (interface letter kind)
    pp     1/2,  1,  1/4              1/2,  1,  1/4    (sigma)
    pn     1/2,  0,  3/4              1/2,  0,  3/4    (averaged_weighted)
    nn     1/2, -1,  5/4              1/2, -1,  5/4    (sigma_inv)

with `z_D = q³/(q²+1)` at `q = 1+ε` and the interface kinds read off `atom_canonical_crossings`.

**And the mechanism was already stated too.** `atom_braid_word_3A`'s own docstring and
`the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe` record that
`tr_M(W_atom)/tr_M(W_free)` is identical under both orderings to `~1e-60` and equals
`prod_i (z + d_i)` over the `A−1` interfaces, *because* "the chain closure is a connected sum, and
connected-sum multiplicativity of the Markov trace does not care how each summand's word is
internally ordered." That is "disjointness is not monotonicity" in other words — so my claim that the
reconciliation is something "neither bean states" is **wrong**, and PR #6920's finding 9 and its
`qou-wdij` cross-reference both need reading with that correction.

**What survives as new, and it is the half that turns a ratio into an absolute.** The corpus's bond
model is about the **ratio**, which cancels the free word entirely and therefore cannot give `c₀`,
`c₁`, `c₂` — those are coefficients of the **difference** `Δ = tr(free) − tr(atom)`. The new part is

    tr(free; Z,N) = tr(p)^Z · tr(n)^N,  (a,r,q) = (1/2, 3/2, 23/4) p, (1/2, −1, 3) n

measured on single nucleons. `(S_p,S_n) = 4(r_p,r_n)` and `(37,20)` from `q_p,q_n` are downstream of
that free half, so they are not re-derivations. Also new: the **ε-series** form of the bond factors
(the corpus's is the ratio at `q₀`) and the `A = 5` verification.

**Corrected framing to quote from here on:** the closed form is the corpus's bond half —
independently re-derived, not new — **times** a free half that is new. Not "goal (2) answered", and
not a mechanism nobody had stated.

**Why the grep missed it, which is the reusable part.** The pre-#6920 checklist searched `.beans/`,
`content/`, `docs/`, `computations/` and the library for the *topic*, and found `qou-kru4`,
`qou-wdij` and `MonotoneWordTraceFactorizes`. It could not find this: the bond model lives in a
**producer's docstring**, and in probe filenames phrased as what they refute
(`..._moves_absolute_traces_not_the_bond_model`, `..._is_overstated`). Standing lesson: **read the
docstring of the producer your result is about** — here, the one word builder every claim in this arc
goes through.

2026-09-07 (order 3): the bond product survives order 3, and the bond factor turns out to have
NO free parameter at any order tested. Probe: computations/probes/bond_product_order_three_probe.py
(40/40, 15s with recorded targets; --verify-live re-measures, ~21 min).

THE SHARP FORM. The three interface factors are exactly the two Markov parameters and their
average -- not "measured constants", not z+d with an offset:

    pp  = z            = (1/2)(1,  2,  1/2, -1/2)   positive crossing
    pn  = (z + z')/2   = (1/2)(1,  0,  3/2, -3/2)   the average of the two
    nn  = z' = z - h   = (1/2)(1, -2,  5/2, -5/2)   negative crossing

z = q^3/(q^2+1) at q = 1+eps (convention D); z' = z - h is FORCED by the quadratic relation
(OcneanuTrace.markovParam_inv_eq_sub), so it is not an independent constant. This supersedes
#6992's "z + d" reading -- both are 3/3 and they are the same object, but d_sigma_inv = -h and
d_averaged = -h/2 are functions of z and h, which is why every offset vanishes when written this
way. Corollary: upsilon_b = -tau_b for all three bonds, i.e. order 3 adds no degree of freedom;
that is z's own -1/2-against-+1/2 and h's +1-against--1, inherited.

HELD OUT: 40/40 coefficients over 5 words x free+atom x orders 0-3 at A=3 -- 3p, T, 3He, 3n and
the UNSORTED pnp. Inputs are nucleon factors at A=1 and bond factors at A=2 only; every A=3 word
is held out. 125-145s per word to measure at K=3.

WHY THE SHAPE: pattern_scalar adds d uniformly across every basis pattern (asserted, 192 sites,
4 kinds, diagonal and off-diagonal both present), so a letter acts as sigma + d.1 and linearity
of tr gives the factor. LEAN (this branch, lean-direct exit 0, axiom-clean, 3 new theorems in
QOU/MathlibExt/DisjointBlockTraceLaw.lean): tr_mul_gen_comb covers all three bonds at once as
c.g + c'.ginv -- stated without division so R stays a bare CommRing -- plus tr_mul_gen_add_ginv
and tr_mul_gen_comb_of_quadratic. tr_mul_gen / tr_mul_geninv already covered the two like-bonds;
the mixed bond had no counterpart and now does. ALL THREE ARE CONDITIONAL on TwoSidedMarkov,
which has no instance -- conditional-proved is not premise-established, and this is evidence FOR
that premise rather than a consequence of anything settled (qou-301d).

OPEN / THE NEXT DISCRIMINATING MEASUREMENT. d_averaged_weighted = -h(1/2 - delta/4) with
delta = O(eps^3) and h = O(eps), so delta first bites at eps^4: d_averaged == d_averaged_weighted
identically through K=3 (asserted). So neither #6992 nor this probe determines the pn interface's
kind -- both establish only that it is NOT sigma and NOT sigma_inv. ORDER 4 is where
averaged_weighted predicts a DEVIATION from the plain average, and is the measurement that would
settle it. Cost: A=3 at K=4 is ~4x the K=3 word cost. Also open: A >= 6, and A=4/A=5 at K=3
(A=4 at K=3 is ~25x A=3, i.e. ~1h/word).


2026-09-07 (order 4): THE pn KIND IS SETTLED -- `averaged_weighted`, twice over. Probe:
computations/probes/bond_pn_kind_order_four_discriminator_probe.py (exit 0, 122s). This CLOSES the
open item the order-3 entry above left, and supersedes the "two-and-a-half determinations" caveat
posted on #6992 and #7000.

MY COST ESTIMATE ABOVE WAS WRONG. The entry above says "A=3 at K=4 is ~4x the K=3 word cost" and
both PR bodies costed the discriminator as an A=3 word (~17 min). Wrong object: the bond factors are
EXTRACTED at A=2, so the discriminator is an A=2 measurement -- 41 seconds. Do not repeat that
estimate; ask which object carries the quantity before costing a measurement.

THE DISCRIMINATOR. At eps^4 the two candidate kinds separate for the first time:
    d_averaged           (0, -1, 1/2, -1/2, 1/2 )
    d_averaged_weighted  (0, -1, 1/2, -1/2, 7/6 )
    z + d_averaged       (1/2, 0, 3/4, -3/4,  5/8 )   RULED OUT
    z + d_averaged_wtd   (1/2, 0, 3/4, -3/4, 31/24)   matches
    measured pn bond     (1/2, 0, 3/4, -3/4, 31/24)

SETTLED ON TWO DIFFERENT OBJECTS, not one. The held-out 3He word at K=4 re-discriminates the same
pair independently: carrying the ruled-out plain-average bond through the product gives 3745/512 at
eps^4 against the measured 11299/1536. That word contributed nothing to the extraction.

WHAT IT COSTS THE ORDER-3 HEADLINE. Two thirds of "the bonds are z, (z+z')/2, z'" survive order 4
and one third does not:
    pp   z            STILL EXACT at order 4
    nn   z' = z - h   STILL EXACT at order 4
    pn   (z+z')/2     BREAKS at eps^4  (5/8 predicted vs 31/24 measured)
The mixed bond is the plain mean only through order 3. pp and nn take NO correction, so the entire
delta weighting lives in the one interface where a (p,n) asymmetry could enter. The `upsilon = -tau`
corollary also stops -- the order-3 entry called it inherited from z and h rather than structural,
and this is the measurement showing the inheritance ends (order-4 normalised: 1/4, 31/12, 9/4).

HELD OUT: 10/10 at order 4 -- 3He free and atom, all five coefficients each, predicted from A<=1
nucleon and A<=2 bond factors. Cost 1470s free + 1785s atom.

NOT FITTED, NOT LEAN. d_averaged_weighted and delta = (q-1)^2(1-q^-4)/3 are the corpus's own
letter_d_series, untouched; a previously untested BRANCH of that function is now tested and passed.
The merged DisjointBlockTraceLaw.tr_mul_gen_comb does NOT cover this: averaged_weighted is not a
constant combination of the two generators once delta enters. No Lean claim is made.

STILL OPEN: A >= 6; A=4/A=5 at K=3 (A=4 at K=3 is ~25x A=3); order 5+.


2026-09-07 (order 5): all three identities hold one order further, and pp = z is EVIDENCE for the
TwoSidedMarkov premise. Same probe, section 6 (241-244s per bond, 730s total, recorded).

    pp = z                        HOLDS   (1/2, 1, 1/4, -1/4, 1/8, 0)
    nn = z' = z - h               HOLDS   (1/2, -1, 5/4, -5/4, 9/8, -1)
    pn = z + d_averaged_weighted  HOLDS   (1/2, 0, 3/4, -3/4, 31/24, -5/2)
    pn = z + d_averaged           ruled out again (eps^5: -1/2 vs -5/2)

So the kind determination stands at TWO orders as well as on two objects.

WHY IT MATTERS BEYOND "one more order". pp's letter has d = 0, so pp = z IS the statement
tr(a.sigma) = tr(a).z -- the premise of TwoSidedMarkov, the class every theorem in
DisjointBlockTraceLaw is conditional on and which has NO INSTANCE. Six coefficients now, including
eps^5 where z's own coefficient is 0 (a zero predicted and a zero measured, not vacuous). This is
EVIDENCE and discharges nothing: conditional-proved is not premise-established, and that rule
applies to numerical support exactly as to Lean. The route to the premise is still E_n (qou-301d).

PROCESS TRAP, cost me the edits once and worth recording. `git checkout -- computations/` is the
command used all session to revert the contended audit witnesses that a precision-gates run
rewrites. It is TREE-WIDE, so it also destroys uncommitted probe work in computations/. Scope it
(`git checkout -- computations/audits computations/*.witness.json`) or commit before running gates.


2026-09-07 (CORRECTION to the order-5 entry above): "evidence for the TwoSidedMarkov premise, a
class with NO INSTANCE" is WRONG, both halves, and it is a category error. PR #7067 proves
TwoSidedMarkov is DERIVABLE from MarkovTrace in four lines -- cyclicity + T3 + the fact that H n is
a Subalgebra, so y merges with x into y*x in H n and T3 applies -- and registers a global instance.
So the class has an instance for every MarkovTrace. Worse: tr(a.sigma) = tr(a).z for a in H n is T3
ITSELF, an AXIOM of MarkovTrace. Offering numerical evidence for an axiom of the structure you are
reasoning in is not a weak result, it is a category error.

WHAT THE MEASUREMENT ACTUALLY SUPPORTS: that the CONCRETE Hecke Markov trace (the one [diamond]
evaluates) satisfies Markov stabilisation at the atom word's interface positions with z = z_D. A
fact about the concrete trace matching the abstract axioms -- classical (Jones/Ocneanu), unformalised
here, strictly weaker and different. The numbers are unaffected; only their interpretation moved.
Corrected in the probe's section 6, its docstring, and on #7023.


---
**2026-09-08 — the ρ_pp target posted on #7000 was TAKEN OVER and answered elsewhere; no action needed here, but the result bears on this bean's own claim.**

This bean was `in-progress` and 16 h stale (last update `2026-09-07T11:13Z`) with no response to the target posted on #7000 at 17:09Z, so per the stalled-claim protocol `qou-brng` computed it. **Nothing of this bean's work was touched or duplicated** — its bond-factor extraction is the *input*, used as published.

**Result:** the derived kind-dependent bond weight does **not** reproduce the measured three-body cumulant. Required `ρ_pp ≈ 1.641`; the bond factors give **0.72–1.21** across four identifications, and the principled (log/additive) one misses worst at 55.9 %. No carrier `m ∈ 1..6` closes it.

**Why it matters here:** this bean's order-4 discriminator is *confirmed as the input* and is not in question — the sign of the kind-dependence is right (`bond_pp > bond_pn`). What the comparison shows is that its **magnitude** is roughly half what the binding data would need. That is a constraint on the bond model that this bean's own front is best placed to interpret, and it was not visible from inside the extraction.

Details and the anti-fit reasoning: `qou-brng`, and `computations/probes/rho_pp_kind_weight_does_not_close_b3_probe.py`.


---

## 2026-09-13 — §"What is NOT established" item 3 is STALE: BOTH halves already have Lean statements

Item 3 of the "GOAL (2) IS ANSWERED" section (written 2026-09-06, PR #6920) reads:

> **NOT PROVED.** … Neither the bond product nor the free-word factorisation has a
> Lean statement — that is the formalize-first follow-on and is **the highest-value
> next item on this arc**.

**Both halves had Lean statements before that sentence was written.** Measured on
`main` 2026-09-13; neither file is referenced anywhere in this bean.

**Free-word factorisation — `QOU/MathlibExt/MonotoneWordTraceFactorizes.lean`**
(landed 2026-09-04, i.e. *two days before* item 3; sorry-free, axiom-clean on 8
decls per bean `qou-kru4`):

- `tr_stabWord_eq_prod_tr` — a **monotone** word (ascending, letters `s m ∈ H (m+1)`
  stabilising `H m`) has `tr = ∏ tr(letter)`. This is the free-word factorisation.
- `tr_affineWord` / `affine_mul_affine` / `runCoeff` / `tr_runWord` — the production
  superposition letters `a•1 + b•g` and their runs.
- `tr_sequential_via_factorization` — the production word specifically.
- `content_reorder_defect` — the same letters in non-ascending order pick up
  `z(z² − hz − 1)`.

And it carries the *reason*, which this bean never states: **bond-additivity is a
theorem about ORDERING, not a Markov-trace property.** The production per-bond
product is exact because `atom_braid_word_3A` is monotone.

**Bond product — `QOU/Hecke/MarkovInteriorBond.lean`**:

- `tr_bondWord_of_interiorMarkov` : `tr (bondWord) = (∏_k (z + d_k)) * tr (freeWord)`
  — the bond product itself, with `bondWord` / `freeWord` / `ChainOK` defined.
- `interiorMarkov_ascending` — discharges the hypothesis unconditionally for
  ascending `b`, from the Markov axioms alone.
- `exists_not_interiorMarkov` — an explicit counter-model (`R[X₀,X₁,X₂]`) proving the
  hypothesis is **independent of the tower axioms**, so it is not free.

**So what actually remains is narrower than item 3 says, and it is named in a
different bean.** The bond product is proved *conditional on* `InteriorMarkov`
(`∀ g, ∀ a ∈ H g, ∀ b ∈ upper g, tr(a σ_g b) = z tr(a b)`), discharged only for
ascending `b`. Bean **`qou-gr3t`** carries that gap and names the route: prove it
from quadratic + braid + **word-spanning** `H_{n+1} = H_n + H_n σ_n H_n`.

**That third ingredient landed 2026-09-08** as `TowerSpanReduction.step_of_sandwichReduces`
/ `HeckeSandwichReduces.sandwichReduces_all` — one day after `qou-gr3t` was last
updated, and the two were never connected. `qou-gr3t` calls the remaining work "a
multi-session build"; with word-spanning in hand it is a short induction.

**Process note, and it is the same failure twice in one session.** This bean's item 3
was written without checking `qou-kru4` (`completed`, 2026-09-04), whose closure entry
names `MonotoneWordTraceFactorizes.lean` explicitly. Earlier today I re-derived a
`qou-301d` result a sibling had landed on 2026-09-08 because I read 30 lines of that
bean and stopped. Corpus-grep path 6 — *"Read `status` and the whole body, not the
title"* — is the control for both, and a `completed` bean is the one that bites.

No number in this bean moves. The measurement stands; only the "what is left" claim
was wrong.


## 2026-09-13 — the bond product for the production LAYOUT is now a theorem (#7281)

§"What is NOT established" recorded the identity

    tr_M(W_atom) / tr_M(W_free) = prod over bonds of (z + d_b)

as **measured, not proved** — orders <= 5, A <= 5. The *structural* half of that is
now proved, sorry-free, in `QOU/Mass/ProductionChainBondProduct.lean`
(`tr_productionChain_braided`): on any `BraidedTower`, with no `InteriorMarkov`
hypothesis, the trace factorises as the product of `z + d` over the bonds.

**What made it available was a connection, not new machinery.** Two results landed
the same day and nobody joined them: `tr_bondWord_of_braided` (#7265) proves the
bond product on every braided tower *given* `ChainOK`, and `StrandLayoutForcesChain`
(#7153 arc) proves the inter-nucleon bridges are exactly `sigma_{3k+2}`. The second
is the index set the first quantifies over, and `ChainOK` then falls to arithmetic
on `3k+2` — bonds increase (`3k+2 < 3(k+1)+2`), block `k+1` is above bond `k` (its
generators `3k+3, 3k+4` exceed `3k+2`) and below bond `k+1` (they are under `3k+5`).

## 🛑 This does NOT close the bean, and the half it leaves is the interesting half

**The letters stay measured.** The chain carries an arbitrary scalar `d k` per bond.
That the production letters are `pp -> 0`, `nn -> -h`, `pn -> d_averaged_weighted`
is this bean's `letter_d_series` measurement and nothing in #7281 derives it. What
is derived is that *whatever* those scalars are, the product form holds. So the
bean moves from "the form is measured and the letters are measured" to "the form is
a theorem and the letters are measured" — one of two items, and the remaining one
is where the physics is.

**The blocks are hypotheses too.** `hlow`/`hup` say each nucleon word sits in its own
strand window, which is what `StrandLayoutForcesChain` establishes about
`atom_braid_word_3A` — but there is **no Lean model of `atom_braid_word_3A`**, so
the bridge from the Python producer to a Lean term is not made.

**And it is about a class, not yet about the production trace.** The theorem is
stated over `OcneanuTrace.MarkovTrace` + `BraidedTower`, and the only such instance
in the tree is `heckeTowerMarkovTrace`, whose trace factors through a rank-2
quotient. Instantiating it at the production Ocneanu trace at `z_D = q^3/(q^2+1)`
needs the colimit bridge `qou-0fmb` (#7274, in flight) — posted there as a
downstream consumer.


## 2026-09-13 (later) — two of the three letters derived (#7285), and my pn claim RETRACTED

Following #7281, which proved the bond product's *form* and left the letters measured.

**Derived, sorry-free** (`QOU/Hecke/BondLetterIdentification.lean`), in the
**interior** position a bond actually occupies, over `MarkovTrace` + `[BraidedTower]`
so `InteriorMarkov` is discharged rather than assumed:

- `sigma` carries `d = 0`, factor `z`  (`tr_bond_gen`)
- `sigma^-1` carries `d = -h`, factor `z - h`  (`tr_bond_ginv`)

The corpus had the second only in **right-multiplication** form
(`tr_mul_ginv_of_quadratic`, `tr_mul_gen_comb_of_quadratic`, both `b = 1`), because
`MarkovTower` has no `ginv` field. A bond has material on both sides, so the bond
product needs `b ∈ upper g`. ~3 lines once composed.

## 🛑 RETRACTED, same PR: the pn letter is NOT the symmetric one

I claimed `d_pn = -h/2`. **Wrong.** The production letter is `averaged_weighted`,
`d_pn = -h(1/2 - delta/4)` with `delta = (q-1)^2 (1-q^-4)/3` — carried by
`ClosedFormInterfaceFactors.bondD`, `MarkovBondRule.dIface`,
`canonical_braid_crossings.py` and `markov_peel.py`. `-h/2` is the corpus's
**`averaged`** letter, a different ctype.

**This was already settled here on 2026-09-07** —
`bond_pn_kind_order_four_discriminator_probe.py`, lines 609-641 of this bean, on two
objects plus a held-out 3He word. Re-verified independently in exact rationals:

    z - h/2     1/2, 0, 3/4, -3/4,  5/8
    z + d_pn    1/2, 0, 3/4, -3/4, 31/24   <- matches the measured pn bond

**How the error got made, which is the part worth keeping.** I verified to `eps^2`.
The two candidates are **identical through `eps^3`** and separate only at `eps^4`, so
my check passed *both* and I read it as confirming one. Agreeing to the order you
happened to expand to is not evidence of identity — and the corpus-grep that caught
it also found bean `7uhw` (*completed*, 2026-06-23, title = the claim, **body empty**)
and the published block `mass-theory/interface-knot-markov-z-proof.md` §39-43, which
states the three-factor result outright. A title-only completed bean is exactly the
carrier the six-path checklist exists to reach, and I reached it only on the second
pass.

## What is still open, sharpened

**Derive the `delta/4`.** The pn interface's colour-tube weighting is the one letter
the skein does not give, and it is now isolated: `pp` and `nn` are theorems, the
product form is a theorem (#7281), so the whole measured residue of the bond model is
that single factor. `mass-theory/pn-averaging-uniqueness.md` frames the two candidates
and records that only the **uniform** form is bar-invariant (`delta-bar = -q^2 delta`),
so the uniqueness theorem's hypotheses **exclude** the production letter — that
tension is where a derivation would have to start, or a convention change would have
to be argued to the owner.


## 2026-09-13 (later still) — what `delta/4` EQUALS, and why that is still not a derivation

The open item after #7285's `tr_bond_interp` is the single VALUE
`t = 1/2 - delta/4`. Measured, not argued:

**The identity.** `observations/flavor-split-substrate` defines
`delta = (m_n - m_p)/M_N` with `M_N = (m_p + m_n)/2` -- the **mean** nucleon
mass. Under that normalisation, identically:

    t = 1/2 - delta/4 = m_p / (m_p + m_n)

and dually `1 - t = m_n/(m_p + m_n)`. So the `sigma` branch carries the
NEUTRON's mass fraction and the `sigma^-1` branch the PROTON's -- **cross-
weighted**, which is the shape a barycentric lever arm takes (the distance from
a body to the centre of mass is proportional to the OTHER body's mass).

Also verified exactly, since it is the producer's own docstring claim and had
not been checked here: `delta = (q-1)^2 (1 - q^-4)/3 = hbar_q^2 * h_q * [2]_q / 3`.

Both are `QOU.Hecke.BondLetterIdentification.tPN_eq_proton_mass_fraction`,
sorry-free.

## 🛑 It is an IDENTITY, not a derivation — and the test it fails is recorded

Re-expressing `delta/4` in the corpus's own quantities supplies no mechanism.
What it buys is that the open coefficient now has a name and a candidate reading
**that can be tested**. The test:

    massFraction_like_pair :  m/(m+m) = 1/2

A mass-fraction rule assigns any **like** pair the weight `1/2`. The corpus
assigns `t = 0` to `pp` (`sigma`) and `t = 1` to `nn` (`sigma^-1`). So the rule
contradicts BOTH like-pair letters and cannot be the general mechanism. Stated
as a theorem rather than a remark so the refutation is machine-checked
alongside the identity.

**What survives, and it is a story rather than a result:** the like pairs may be
fixed by exchange symmetry -- identical particles admit no interpolation, so the
letter is forced to an endpoint -- leaving only the UNLIKE pair with a free
weight, displaced from the symmetric `1/2` by the flavour asymmetry. That would
explain why `delta` appears at all. It does not derive the factor `1/4`, and the
`1/4` is the whole of what is open.

## Corpus-grep, so the next agent does not redo it

Nothing in `content/`, `docs/`, `computations/` or `.beans/` carries the
mass-fraction / barycentric / lever-arm reading, or the `m_p/(m_p+m_n)` shape.
`mass-theory/canonical-braid-interface-composition` states the weighted form and
records that the two conventions differ by `h*delta/4` -- **with no rationale for
the 1/4**, which is consistent with it being open rather than merely unwritten.


## 2026-09-13 — the open question RELOCATES: the p/n asymmetry is injected at the like-pair letters

Chasing `delta/4` led upstream. Four exact results, all verified symbolically.

### 1. The `pp -> sigma` / `nn -> sigma^-1` assignment is a BARE choice

`computations/mass_at_3A_proper.py` lines 622-623:

    _X_PP = (mpf(1), mpf(0))      # sigma
    _X_NN = (mpf(1), -h_loc)      # sigma^-1

No rationale anywhere. The module docstring says the inter-pass letters come
"from Hecke relation" (line 32) — but the Hecke relation only relates `sigma`
to `sigma^-1`; it does **not** say which flavour pair gets which. The
assignment is stated, never derived.

### 2. That choice ALONE produces the mirror-pair asymmetry

Canonical `pppnnn` ordering at `A = 3`:

    3H  (Z=1,N=2):  bonds (p,n),(n,n)   ->  (z + d_pn)(z - h)
    3He (Z=2,N=1):  bonds (p,p),(p,n)   ->  z (z + d_pn)

Swapping the `pp` and `nn` letters **exactly exchanges the two bond products**
(verified symbolically, not numerically). So the `3H`/`3He` asymmetry the
framework is trying to explain is, at the bond-model level, *entirely* the
content of an unexplained letter assignment — and `delta` contributes nothing
to it, since the `pn` factor is common to both and cancels.

### 3. The mirror ratio is exactly `q^-4`, independent of the pn convention

    tr(3H)/tr(3He)  =  (z - h)/z  =  q^-4

exactly. This is a **falsifiable, delta-free structural prediction** of the
bond model, and it does not depend on any of the open pn-convention questions.
Testing it against AME is the obvious next step and is NOT done here.

### 4. `1 - q^-4` in `delta` IS the like-pair bond gap

`z_D - h = 1/(q(q^2+1))` against `z_D = q^3/(q^2+1)`, so `(z_D - h)/z_D = q^-4`
and therefore `1 - q^-4 = h/z_D` exactly. Hence

    delta = (q-1)^2 * (h/z_D) / 3

So one of `delta`'s three factors is not an independent substrate expression at
all — it is the relative gap between the two like-pair bond factors.
Sorry-free: `nnFactor_eq_ppFactor_div_q_pow_four`, `flavorSplit_eq_bondGap`.

## 🛑 What this does and does not settle

**Does not close the bean.** Results 3 and 4 are algebraic identities in the
same class as `tPN_eq_proton_mass_fraction`: they re-express corpus quantities
in terms of each other and supply no mechanism. The `(q-1)^2/3` is unexplained,
and the `1/4` — the whole of what is open — is untouched by all four.

**Does relocate the question, which is the point.** `delta/4` is a
*second-order* refinement sitting on top of a *first-order* p/n asymmetry that
is injected by hand at `_X_PP` / `_X_NN`. Asking "why `delta/4`" before "why
`pp -> sigma`" is asking the second question first.

**A route I considered and did NOT take.** Result 3 gives a clean closed form,
and it is tempting to look for a numerical match to a measured `3H`/`3He`
quantity. Matching a ratio to data without a derivation of the coefficient is
selection against the target under the NO-FITTING directive, so it is left
alone; the honest next step is to derive the letter assignment, not to score
the ratio.


## 🛑 SAME SESSION — correcting the "relocation" entry above, twice over

The entry above says *"the open question RELOCATES: the p/n asymmetry is
injected at the like-pair letters"*. A corpus-grep I should have run before
writing it turns up
`content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-sidecar-mirror-cancellation`,
which corrects it in three ways.

### 1. The bond letters are NOT the only p/n injection

That block records a second one, upstream of the bond model — the **intra**-
nucleon writhe asymmetry, verbatim:

> The sign of `ζ` is fixed by the per-nucleon intra-`B₃` writhe asymmetry
> (proton `+3` > neutron `+1`); its magnitude is open and unfitted.

So the correct statement is that the asymmetry is injected **at the bond
letters AND in the per-nucleon blocks**. My entry's unqualified form is wrong.
The scoped form — *"nothing else **in the bond model** distinguishes a proton
from a neutron"* — is right and is what the Lean docstring says; the bean and
the PR body had dropped the scope.

### 2. The `4(Z−N)` was already in the corpus, as the writhe difference

The same block gives the total writhe `w = σ − σ⁻¹ = 4Z`, hence

    w(Z,N) − w(N,Z) = 4(Z − N)

which is **numerically the same exponent** as my
`tr(Z,N)/tr(N,Z) = q^(4(Z−N))`. So the mirror ratio is `q` raised to the
writhe difference.

🛑 **Whether that is structural or a coincidence of two different counts is NOT
established.** The block's writhe is over the **whole word**, intra letters
included; my `a` and `b` count only the `A−1` **inter**-nucleon bonds. Two
different populations producing the same `4(Z−N)` is suggestive and is not a
derivation. Do not cite the agreement as one. Checking it is a real next step:
if the intra letters contribute `2(Z−N)` to the writhe difference (proton `+3`,
neutron `+1`, so `3Z+N` against `3N+Z`), then the totals cannot both be
`4(Z−N)` unless the inter contribution is `2(Z−N)` rather than the `4(Z−N)` I
computed — so **at least one of the two readings is wrong**, and that is worth
resolving before either is quoted.

### 3. The magnitude was ALREADY declared open

*"its magnitude is open and unfitted"* — so the open item I described myself as
"relocating to" is in part one the corpus had already named and recorded. The
new content is the **bond-product** statement and its `q^(4(Z−N))` closed form,
not the observation that a mirror asymmetry needs explaining.

**What survives unchanged.** The four exact results are all still exact: the
bare `_X_PP`/`_X_NN` assignment, the swap-exchanges-mirror-products fact, the
`q^(−4(N−Z))` law, and `1 − q^-4 = h/z_D`. What was wrong was the framing
around them, in the direction of claiming more novelty and more exclusivity
than the corpus supports.

Also noted, not acted on: `mba-sidecar-mirror-cancellation` lives under
`appendix-mass-binding-algorithms`, which AGENTS.md makes a maintenance
contract requiring same-PR updates for mass/binding changes. This PR adds Lean
theorems and changes no algorithm, compute or witness, so nothing there is
stale on its account — flagging rather than editing another arc's contract,
per ASK-BEFORE-CHANGING.


## 🛑 THIRD correction, and this one retracts a novelty claim

A six-path corpus-grep (run late, after I had already written the claims into
this bean and PR #7285) found three things that change the entries above.

### A. The delta-cancellation is a RE-DERIVATION

`QOU.QBeta.InterfaceScalar.mirror_split_eq_L_diff` is **sorry-free on main**,
and its docstring states my reasoning in almost my words:

> On the chain topology `3H = pnn` carries bonds `{pn, nn}` and `3He = ppn`
> carries `{pp, pn}`, so the predicted splitting is `alpha (L_nn - L_pp)`
> **regardless of what the p-n bond is**.

That IS "delta cancels from the mirror ratio". It was in the corpus before I
derived it. **What is actually new is narrower than I claimed**: the *closed
form* `q^(4(Z-N))` for the bare bond-product ratio, and its generalisation off
`A = 3`. The cancellation is not mine.

### B. The orientation is not merely underived — it is reported FALSIFIED

Bean `qou-0pzi` (`status: todo`, live):

> So `pp = sigma`, `nn = sigma^-1` **cannot be the right assignment**

because the model makes the diproton `+2.5416` and the dineutron `+3.3069`
**bound**, where nature has both unbound (the pn/deuteron case is bound and
+27.3 % over). This is a **scope-(a)** negative — this assignment, alone, gets
the two-nucleon signs wrong — and names no proved invariant excluding the
ingredient, so it must NOT be upgraded to scope (b).

That is much more consequential than "underived", and I did not have it.

### C. "Nothing derives it" was falsifiable by one grep

There IS a stated rationale — `computations/inter_nucleon_linked_channel.py:16`
and `docs/audits/2026-06-01-inter-nucleon-linked-channel.md:68`, *"Chirality
(matter/matter vs matter/antimatter) gives the sign"*. It does not hold (the
`epsilon` rule it cites keys on whether the two flavours MATCH, giving `+1` for
pp and nn alike, and that block lists the epsilon sign rule as its own open
question), and a second "DERIVED via integer-LP / SDP" claim in
`computations/_deprecated/` misattributes scripts that hold the quark crossings
fixed and optimise only the gluon tail. But "nothing in the corpus derives or
justifies it" is the sentence a reviewer falsifies in one grep.

**The accurate form, which is a stronger claim and checkable:** the orientation
is **asserted, not derived, and not declared as a convention either**. Two
ledgers already log it — *"asserted ... without a `prop:` block"*
(`docs/coordination/2026-05-24-low-isotope-mass-anatomy-ledger.md:31`) and
*"the framework's own crossing **convention**"* (`docs/coordination/option-e.md:340`).
No Lean forces it: `MarkovBondRule.bond_pp_nn` takes `d = 0` / `d = -h` as
INPUTS and carries the flavour attribution only in its docstring.

### D. The intra-nucleon letters are not an upstream rescue

`tools/pyhecke/python/pyhecke/atom.py:524-531` applies the identical map one
scale down — `uu -> sigma`, `dd -> sigma^-1`, `ud -> avg` — and `atom.py:69-70`
says of it, verbatim, *"nothing here establishes what convention a u-d crossing
should carry."* So the upstream carries the same undecided choice, not a
derivation of it.

### Still not done, and it is a concrete next step

My closed form is for the **bare** bond-product ratio, before `alpha` and before
the writhe normalisation `(1-h)^(Delta_e/2)`. `InterfaceScalar` reports the
measured split as `alpha(L_nn - L_pp) = 2.27077 MeV` under convention C and
`0.76532 MeV` under D with writhe wired. **No arithmetic bridging the two has
been written down**, by me or by the corpus, and anyone quoting both owes that
step.
---

COORDINATION NOTE (2026-09-13, session gracious-dijkstra, from bean `qou-gba1`).
Not a claim on this bean, and nothing here is edited — a cross-citation only,
per AGENTS.md's "a result landing on one should be cited in the others".

**Your `b_pp` is the Markov stabilisation parameter, exactly.**
`qbeta_bond_factors_derived_probe.MEASURED["b_pp"] = 0.6126880371464652516`
is `z(q₀) = q₀³/(q₀²+1)` — the convention-D Markov parameter
(`closed_form_tau_M.markov_z`) — agreeing to **all 19 digits `b_pp` carries**
(z = 0.6126880371464652515958299…). Verified numerically today, not eyeballed.
So this bean's working title, "the bond factors ARE the two Markov parameters",
is right at least for the pp factor, and it is right *identically* rather than
to some tolerance.

**Why that may be worth more than a coincidence check.** `qou-gba1` (option E
of `qou-za3q`) independently derived the same constant from the other end. The
Jones–Ocneanu axiom `tr_{n+1}(x·σ_{n-1}) = z·tr_n(x)` forces an exact
stabilisation law on the Magnus Ω₂ pairing,

    P_y(βσ_{n-1}) = z·P_y(β) + (m/2)·Σ_λ y_λ tr(ρ'_λ [A_{n-2},A_{n-1}]_λ)

confirmed to a relative **4.4e-141** on the deuteron word and two successive
stabilisations, and *falsified* at the two wrong values a reader might
substitute (z = q, the degenerate competing root: 49 % / 69 % off; z = 1:
38 % / 54 %). Witness
`computations/deltalambda/magnus-omega2-markov-stabilisation.witness.json`.

So `z` is not a fitted or chosen number in either place: it is what
stabilisation costs. If a bond factor *is* `z`, the natural reading is that
adding a nucleon to the chain is a stabilisation — which would make the
near-additivity this bean is chasing a statement about Markov moves rather than
about the expansion. Offered as a lead, not a result; I have not tested it, and
`b_pn` / `b_nn` are not `z` (ratios 0.8295 and 0.7942 to their predecessors),
so whatever the structure is, it is not simply one parameter.


---

RESULT + TWO CORRECTIONS (2026-09-13, session sleepy-morse, PR #7285).
Prompted by the coordination note immediately above, which I followed back into
the file it cites.  The note's lead is right and is stronger than it says; my own
PR overstated what was new.

**The three qbeta bond constants are ONE law, exactly.**
`qbeta_bond_factors_derived_probe` extracts five closed forms from the 2H / 3H
traces.  All three BOND constants are the interior bond factor `b(t) = z - h*t`
of `QOU.Hecke.BondLetterIdentification.tr_bond_interp`, at three values of the
single mixing parameter `t`:

    letter   t                b(t)                       the file's closed form
    ------   --------------   ------------------------   -------------------------
    pp       0                z                          q^3/(q^2+1)
    pn       1/2 - delta/4    z - h*(1/2 - delta/4)      the degree-10 rational
    nn       1                z - h                      1/(q^3+q)

with `z = q^3/(q^2+1)` (convention D), `h = q - 1/q`, `delta = (q-1)^2(1-q^-4)/3`.
Each difference simplifies to **exactly 0** in sympy over the symbol `q` — these
are rational-function identities, not agreements at `q0`.  Checked in
`computations/qbeta/qbeta_bond_factors_are_one_interpolation_probe.py` (4/4;
numerical leg agrees with the file's own MEASURED values to rel 7e-21).

**CORRECTION 1 — to myself.  `nnFactor_eq_ppFactor_div_q_pow_four` is a
FORMALISATION, not a discovery, and PR #7285 did not say so.**  That probe
already records `b_pp/b_nn - q^4 = 0` as its identity 2, established
symbolically, and `b_pp - z = 0` as its identity 1 under a check literally named
`b_pp_IS_the_markov_parameter`.  Both predate this branch.  What the Lean adds is
that they are the SAME law at `t = 0` and `t = 1` — identity 2 is `tr_bond_ginv`
divided by `tr_bond_gen` — and that the law holds for a bond with material on
both sides, which the probe does not address.  The credit belongs upstream and
the PR body is being amended.  I found this only because the sibling's note sent
me to the file; my own corpus-grep for the `q^-4` fact had not reached it.

**CORRECTION 2 — to the coordination note above, and it makes the note's point
stronger.**  It reports `b_pp = markov_z(q0)` as verified numerically today,
"agreeing to all 19 digits `b_pp` carries".  The file it cites already had this
EXACTLY, symbolically, in its own docstring at the lines listing its three
identities.  So the right statement is not "agrees to 19 digits" but "is equal as
a rational function of `q`", which is a stronger claim than the one offered.
The note's *independence* argument is untouched and stands: `qou-gba1` reaching
`z` from the Jones-Ocneanu stabilisation axiom, and this probe reaching it by
extraction from nuclear traces, are genuinely different routes.

Its stated counter-argument does not survive: *"`b_pn` and `b_nn` are not `z`
(ratios 0.8295 and 0.7942), so it is not one parameter doing all the work."*
Both ratios reproduce (0.82950826287, 0.79418355002 at dps=60), and they
telescope to `b_nn/b_pp = q^-4` exactly — but the substantive answer is that all
three letters ARE one parameter, `z`, plus the Hecke quadratic constant `h`,
with `t` selecting the letter.  `b_pn` and `b_nn` are not `z` for the same reason
`z - h` is not `z`.

**Independent exact confirmation of this PR's correction 1** (the production p-n
letter is `averaged_weighted`, not `averaged`).  Solving `b_pn` for `t` gives
`(-q^6+2q^5+5q^4+q^2-2q+1)/(12q^4)`, identical to `1/2 - delta/4`; and
`b(1/2) - b_pn = (-q^8+2q^7-2q^5+2q^4-2q^3+2q-1)/(12q^5)`, nonzero.  That is a
symbolic separation of the two ctypes, stronger than the `eps^4` discriminator
(`5/8` vs `31/24`) I had been relying on — and it is the check that would have
caught my original error at first attempt, since it needs no expansion order at
all.

**Still open, unchanged.**  This derives no mechanism for the `1/4` or the
`(q-1)^2/3` in `delta`; it shows the extracted `b_pn` IS that `t`, not why `t` is
that.  It says nothing about the `pp -> sigma` / `nn -> sigma^-1` ORIENTATION,
which `qou-0pzi` reports falsified on the two-nucleon signs — the law says what a
letter contributes, not which letter a flavour pair gets.

**Offered to `qou-4383`, as evidence and not as a resolution.**  That bean's flag
sits in this same file: its `t_p` / `t_n` are GROUPED-era while its per-atom
inputs are canonical.  `b(t)` has no intra-nucleon content — it is the Markov
property plus the Hecke quadratic relation, both statements about the INTERFACE
crossing — so the exact agreement of all three `b_*` with it is evidence the
flagged mismatch is confined to `t_p` / `t_n`.  I have not checked `r_previous`,
and this does not tell anyone which way to flip the two nucleon traces.

---

RESULT (2026-09-13, session sleepy-morse, PR #7300) — the target
`KindDependentBondBreaksIntegrality` stated is now ANSWERED, and the answer is a
NEGATIVE that is sharper than a plain miss.

**The connection that file says nobody made.** `QOU.Mass.KindDependentBondBreaksIntegrality`
(merged) observes that the `b₃` count-channel exhaustion rests on a UNIFORM bond
weight, that this bean has since derived a weight that is NOT uniform, and — its
words — that "the corpus has since taken that escape, on a different front, and
nobody connected the two." It then states a number and a direction of use:

> `ρ_pp = 1 + rMeasured = 2433859/1483044 ≈ 1.64112`. "Read RIGHT-TO-LEFT only:
> this is the number `qou-qqm4`'s derived `z + d_kind` at the `pp` interface must
> independently produce. ... Agreement would be a parameter-free prediction;
> disagreement is a real negative about the bond model."

`BondLetterIdentification` (merged today) supplies that input: `b(t) = z − h·t`
for every `t`, `t = 0` at `pp`, `1` at `nn`, `1/2 − δ/4` at the production `pn`.

**Computed, exactly.** With `P q = q¹⁰−2q⁹+7q⁸−2q⁶+4q⁵+4q⁴+q²−2q+1`:

    b_pn   = P q / (12 q⁵ (q²+1))     <- IS the probe's extracted degree-10 form
    ρ_pp   = 12 q⁸ / P q              ρ_nn = 12 q⁴ / P q      ρ_pp/ρ_nn = q⁴

All three are rational-function identities over the symbol `q`, now in Lean:
`QOU.Mass.KindRatioFromBondLetters`, five theorems, sorry-free, lean-direct
exit 0, axioms `[propext, Classical.choice, Quot.sound]`.

**Scored at the minimal ³He carrier (`ppn`: one `pp` pair, two `pn`).**

| carrier | ρ_pp | b₃/b₂ | miss |
|---|---|---|---|
| uniform ρ = 1 (the exhaustion's premise) | 1 | 0 | −100 % |
| best INTEGER carrier ρ = 2 | 2 | 1 | +55.976 % |
| **DERIVED** | 1.2055335007 | 0.2055335007 | **−67.942 %** |
| target | 1.6411239316 | 0.6411239316 | 0 |

**The finding, and it is the part worth carrying forward.** The derived
kind-dependence moves `b₃/b₂` off zero and *toward* the measurement — roughly a
third of the way — and still lands **further from it than the integer carrier the
exhaustion had already excluded**. So breaking integrality, which is precisely
the escape `KindDependentBondBreaksIntegrality` identifies, does not buy the
escape. That is a stronger statement than "the derived number misses": it says
the named escape route is not where the missing `b₃` lives.

**Scope (a)**, explicitly: this carrier, these weights, at the minimal Brunnian
counts. No invariant is proved here, so kind-dependent weights are **NOT**
excluded in general and this must not be written up as scope (b).

**Which ratio, and the reason for the choice.** `ρ_pp` admits two readings — the
ratio of bond FACTORS `b_pp/b_pn`, or the ratio of their LOGS (the binding is
`B = −α log μ`, so log-space is defensible). I take the factor ratio **on the
target file's own wording** ("`z + d_kind`", which is the factor) and NOT because
it scores better — which it does: the log reading gives ρ_pp = 0.7238235153 and
a −143.077 % miss. Recording this because choosing the better-scoring reading
would be selection against the target, which is exactly what the anti-fit rule
forbids, and the two readings are close enough in plausibility that the
temptation is real.

**Still open, untouched by this.** Why `t_pn = 1/2 − δ/4` specifically — the
`1/4` and the `(q−1)²/3` remain underived. This result constrains what the bond
model BUYS downstream; it does not derive the weight.

Probe: `computations/qbeta/kind_dependent_rho_pp_derived_check.py` (5/5).
COORDINATION NOTE (2026-09-13, session from bean `qou-5c64`). Not a claim on
this bean and nothing here is edited — this answers the one item the previous
coordination note left explicitly untested.

**Your working title is right, and it needs only ONE Markov parameter, not
two.** That note closed with *"`b_pn` / `b_nn` are not `z` (ratios 0.8295 and
0.7942 to their predecessors), so whatever the structure is, it is not simply
one parameter."* Measured: it is one parameter. `b_nn` **is** `z`, bar-conjugated.

The probe's own identity 2 already contains this — `b_pp/b_nn - q^4 = 0` — and
the `q^4` is not a scale factor that happens to be a fourth power. It is the bar
involution `q -> q^-1`, and `b_nn = 1/(q(q^2+1))`, which the docstring calls
"the simplest of the five", is `z|_{q -> 1/q}`. Five identities, each
`sympy.simplify`ing to **exactly zero**
([`qbeta_bond_bar_parity_probe.py`](../computations/qbeta/qbeta_bond_bar_parity_probe.py),
witness `computations/qbeta/qbeta-bond-bar-parity.witness.json`):

    b_nn - z|_{q->1/q}                      = 0     n-n bond = bar conjugate of p-p
    z - zbar - (q - q^-1)                   = 0     separation is exactly h
    b_pn - (z + zbar)/2 - h.delta/4         = 0     p-n bond = their MIDPOINT, colour-displaced
    z.zbar - 1/(q + q^-1)^2                 = 0     sqrt(b_pp b_nn) = 1/(q+q^-1), bar-fixed
    bar-odd(b_pn) + (q-1)^5(q+1)^3(q^2+1)/(24 q^5) = 0   fifth-order zero at q = 1

so

    b_pp = z          b_nn = zbar          b_pn = (z + zbar)/2 + (delta/4) h

The two like-pair bonds are the bar-conjugate endpoints of a single object; the
unlike-pair bond is its bar-EVEN part, and it is the **only** one that breaks the
bar symmetry — by `h.delta/4 = 7.1902e-05` absolute, `1.6415e-05` relative, at
the proton pin. Set `delta = 0` (the colour-BLIND crossing your docstring
already separates at 1e-25) and `b_pn` is the exact midpoint. The bar form
reproduces all three of your `MEASURED` literals to **1.24e-20** — every digit
they carry. Your 0.8295 and 0.7942 are then `b_pn/z` and `b_nn/b_pn`, with
`b_nn/z = 1/q^4 = 0.65879` closing the chain.

**Two scope limits, stated because they bear on how you'd use it.** (i) These
are identities between *closed forms*; the involution is `q -> q^-1` on a
rational function. Whether it is the Hecke bar involution acting on the Markov
*trace* — which would promote row 1 from a fact about the traces to a fact about
the words, and would be the interesting version — is **not** established here
and needs the trace's own bar-equivariance. (ii) They inherit your file's own
GROUPED-frame caveat (`qou-4383`) verbatim; I did not resolve it.

**Separately: three of your four shift values are independently confirmed by a
route that never touches the Laurent expansion.** Bean `qou-5c64` isolated the
interface shifts by differencing the June-era `binding-single-pipeline-comparison`
witness against a live run and solving four atoms' bond residuals for three
unknowns. It returned `d_pp = 0`, `d_pn = -0.10445825933572413`,
`d_nn = -0.20906032198987946` at the MUON pin — against your `0`,
`-h(1/2 - delta/4)` and `-h`, agreeing to **2.73e-11** on both non-zero ones at
the same anchor (that is the isolation's floor, not a disagreement). So the
colour-WEIGHTED-vs-BLIND separation your probe asserts at 1e-25 is visible from
outside the expansion too: witness differencing lands on the weighted value.


**SELF-CORRECTION to the note above (same author, after reading #7285).** Two
things, and the ordering of this file was one of them.

**1. My block was inserted between the `qou-gba1` note and #7285's, breaking a
reference.** #7285 opens *"prompted by the coordination note immediately
above"* and quotes *"agreeing to all 19 digits `b_pp` carries"* and *"ratios
0.8295 and 0.7942 … not one parameter doing all the work"* — both are the
`qou-gba1` note's wording, not mine. A rebase union put mine in the middle and
silently re-pointed "immediately above" at a note containing neither phrase.
Re-ordered to gba1 → #7285 → this. **An append-only ledger is not order-free
once an entry says "above".**

**2. #7285 SUPERSEDES my framing, and it is the better one.** I gave three
points; it gives the law they are points on, in Lean:

    b(t) = z - h*t      QOU.Hecke.BondLetterIdentification.tr_bond_interp
    pp  t = 0            pn  t = 1/2 - delta/4            nn  t = 1

My identities 1 and 3 (`b_nn = zbar`, `b_pn = (z+zbar)/2 + h.delta/4`) are the
`t = 1` and `t = 1/2 - delta/4` rows restated. **"It is one parameter" is
#7285's result to claim, not mine** — and its version is stronger, because it
holds for a bond with material on both sides, which none of the closed-form
identities address.

**What survives as this note's, narrowly:** the reading of `t` as the **bar
involution** rather than as a mixing weight — `b_nn = z - h` and `b_nn = zbar`
are the same number and different statements, since `z - zbar = h` exactly — plus
two identities #7285 does not carry:

    sqrt(b_pp . b_nn) = 1/(q + q^-1)                          bar-FIXED
    bar-odd(b_pn)     = -(q-1)^5(q+1)^3(q^2+1)/(24 q^5)       fifth-order zero at q=1

The second is the one with content beyond restatement: it says the p-n letter is
the **only** one that breaks the bar symmetry, that it breaks it solely through
`delta`, and that it does so at fifth order — 1.6415e-05 relative at the proton
pin. In `b(t)` language: `t = 0` and `t = 1` are bar-conjugate endpoints and
`t = 1/2` would be the bar-EVEN midpoint; `delta/4` is exactly the bar-symmetry
breaking, and its smallness is why the p-n letter is nearly self-conjugate.

Whether `t`'s endpoints being bar-conjugate is a *mechanism* or a restatement is
**not** established here, and #7285's own "still open" applies unchanged: nothing
above derives the `1/4` or the `(q-1)^2/3`.
