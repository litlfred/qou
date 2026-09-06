---
# qou-qqm4
title: 'DERIVE c2: the second-order hbar_q coefficient of the trace difference -- and why the pairwise chain is nearly additive at that order'
status: in-progress
type: task
priority: high
created_at: 2026-09-03T15:51:43Z
updated_at: 2026-09-06T09:31:04Z
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
