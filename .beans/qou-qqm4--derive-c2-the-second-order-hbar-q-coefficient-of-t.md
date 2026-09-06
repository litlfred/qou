---
# qou-qqm4
title: 'DERIVE c2: the second-order hbar_q coefficient of the trace difference -- and why the pairwise chain is nearly additive at that order'
status: in-progress
type: task
priority: high
created_at: 2026-09-03T15:51:43Z
updated_at: 2026-09-06T10:18:58Z
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
