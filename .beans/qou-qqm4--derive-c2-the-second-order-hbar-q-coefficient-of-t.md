---
# qou-qqm4
title: 'DERIVE c2: the second-order hbar_q coefficient of the trace difference -- and why the pairwise chain is nearly additive at that order'
status: in-progress
type: task
priority: high
created_at: 2026-09-03T15:51:43Z
updated_at: 2026-09-07T09:31:51Z
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
