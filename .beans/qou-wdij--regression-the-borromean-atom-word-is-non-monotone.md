---
# qou-wdij
title: 'REGRESSION: the Borromean atom word is non-monotone, so every monotone-transfer consumer is dead on main'
status: in-progress
type: task
priority: normal
created_at: 2026-09-05T18:12:11Z
updated_at: 2026-09-05T19:13:28Z
---

## Measured, not assumed (branch claude/atom-trace-nonmonotone-regression-2026-09-05)

**The regression.** `7db032fb48` (2026-09-05 07:53 UTC, owner ruling, bean `qou-hu1f`) made `atom_braid_word_3A` emit the INTERLEAVED Borromean intra word by default. That fix is correct — the grouped assembly was a different element of H_3(q). But interleaving sigma_0 and sigma_1 makes the generator sequence non-monotone:

    grouped    (1,0)  gens [0,0,0,0,0,0,0,1,1,1,1]      monotone
    borromean  (1,0)  gens [0,1,0,1,0,1,0,0,1,0,0]  NOT monotone

and the whole fine-Bratteli transfer (`chi_monotone_transfer.chi_all_lambda` + `reduced_block_kernel.chi_all_lambda_reduced_block`) is valid ONLY for monotone words — its own module docstring states that as its KEY FACT. Both refuse.

So `tr_m_atom_via_transfer.tr_m_atom_zn` — the canonical atom trace producer — RAISES for every atom on main: (1,0), (0,1), (1,1) alike. `mass_binding_dashboard.py` dies on its first call. Live on main for 10 h.

**The refusal is correct and stays.** Composing a non-monotone word through the per-generator alpha/beta reduction would be silently wrong. What was missing is a route for the word the producer now builds.

**The route already existed** — found by corpus-grep, not built. Bean `qou-sorn` records `pyhecke_native.chi_lambda_all_partitions_mpfr` as the general-word kernel. Re-validated here rather than cited (a bean is not a primary source):

  probes/nonmonotone_atom_trace_kernel_route_probe.py — 15/15, 50 dps, no float64.
  kernel == transfer on the GROUPED word, max|d chi| = 6.1e-50 / 5.9e-50 / 1.5e-49
  (the 50-dps serialization floor) at (1,0)/(0,1)/(1,1).

**The corrected traces are large moves, not perturbations:**

  (1,0)  tr_M  1.1457596924573008697 -> 0.62932840220292191817   rel 0.451
  (0,1)  tr_M  0.98774368811580957163 -> 0.47513351715568221251  rel 0.519
  (1,1)  tr_M  0.57517224391777187083 -> 0.15196833920423160759  rel 0.736

At n=3 the discrepancy is confined ENTIRELY to the 2-dim (2,1) block
(1.8077030637786210288 -> -0.28059335090347205473); the two 1-dim blocks (3,)
and (1,1,1) are bit-identical, since sigma_0 and sigma_1 act by the same scalar
there and cannot see the ordering. That localises the owner ruling's premise.

**Next:** route non-monotone words in `tr_m_atom_via_transfer` through the general-word kernel; keep the transfer's refusal.

## Fixed (PR #6864), and what it costs

`chi_general_word.chi_all_lambda_any` dispatches on the word's own generator
sequence — monotone to the O(A) block transfer unchanged, non-monotone to
`pyhecke_native.chi_lambda_all_partitions_mpfr`. The transfer's refusal is left
exactly as it was, because it is correct. Wired into `tr_m_atom_via_transfer`
and `binding_canonical`; both run again.

**The route restores correctness and loses the O(A) scaling** (one word per row):

  A=1 n= 3   3 parts   <0.01 s
  A=2 n= 6  11 parts   <0.01 s
  A=3 n= 9  30 parts     0.36 s
  A=4 n=12  77 parts   621.38 s   <- ~1700x jump
  A=6                  still running at its 900 s budget

The transfer did all of these under 0.05 s. Adequate through 3H/3He; 4He is a
~21-minute long compute (two words); A>=5 impractical.

**The corrected word moves the binding predictions 4-8x DOWN, away from AME:**

  atom   AME (MeV)   B grouped     B borromean   ratio   AME/B_bor
  D       2.224566   0.43540348    0.11503953    0.264      19.3
  3H      8.481798   0.69513150    0.088347359   0.127      96.0
  3He     7.718043   0.69855221    0.10137663    0.145      76.1

Reported, not repaired. Reverting to the grouped word because its number was
closer is selection against the target.

## STILL OPEN — the real fix

The atom word is **block-monotone**: non-monotone only WITHIN each 3-strand
nucleon, while the nucleons stay in increasing generator order. A transfer
carrying the three-level window state (s_3k, s_3k+1, s_3k+2) instead of a single
Bratteli edge would compose the interleaved intra word and keep O(A),
d_lambda-free. `reduced_block_kernel.get_h3_transitions` is already a 3-step
window composition; what it lacks is the OFF-diagonal seminormal matrix element
at each step, which is what a revisited generator needs. That is the target.

## Not done here

22 further files statically combine `atom_braid_word_3A` with the monotone
transfer and were not individually run. A static list overstates — some may not
call the transfer on an atom word at all — so that is a count of candidates, not
of breakages.

## The repair does NOT make the dashboard runnable — measured

`mass_binding_dashboard.py --low` needs 2H, 3H, 3He, **4He, 6Li, 7Li** (lines
88-89). On the general-word kernel that is A=2 (instant), A=3 (0.36 s), A=4
(~21 min for the two words), and A=6/A=7 (hours). Run on the repaired branch it
produced **zero output in 25 minutes** before its budget expired.

So: the crash is fixed and the producer is correct, but the low-isotope
dashboard is still not computable. **The window transfer is not polish — it is
what makes this surface runnable at all.** That also de-prioritises `qou-4ohh`
(float64 hygiene in that same dashboard): cleaning arithmetic in a script that
cannot finish is worth less than making it finish.

## Design for the block-monotone window transfer, with its oracle

Worked out here so the next session does not re-derive it.

**The structure being exploited.** The atom word is
`P_0 b_0 P_1 b_1 ...`, where `P_k` is nucleon k's intra word on generators
{3k, 3k+1} (interleaved, hence non-monotone) and `b_k` is the single bond
letter on generator 3k+2. The `P_k` are non-monotone only INTERNALLY; the
windows themselves are in strictly increasing generator order. So the word is
**block-monotone**, and only the inside of a 3-strand window needs general
treatment.

**Why the current kernel fails, precisely.** `chi_all_lambda` computes
`chi^lambda = sum over SYT chains of prod_g [O_g]_diag` — DIAGONAL entries
only. That identity holds because for a monotone word each `O_g` is applied
once and acts only on level g+1, so the trace closes on diagonal paths. Revisit
a generator after a higher one and off-diagonal seminormal entries enter the
product, and the one-box-at-a-time recursion is no longer the trace.

**The fix.** `get_h3_transitions` is already a 3-step window composition keyed
on `(ab0, ab1, ab2, shape_in, c_in)` — the right architecture. What it lacks is
that each step multiplies by the scalar `alpha*D(delta)+beta` (the diagonal
element). Replace the per-step scalar with the FULL 2x2 seminormal block and
walk the nucleon's letters IN ORDER, summing over the 3-box chain segments from
`s_3k` to `s_3k+3`. The segment space is small — bounded by (addable corners)^3,
a few dozen — so it stays d_lambda-free and O(A).

**Two properties that make this cheap.** There are only TWO distinct intra
words (proton `uud`, neutron `udd`), and the existing cache key already
captures the window's dependence, so the per-window matrices are computed once
and reused across every nucleon and every isotope.

**The oracle is already in place.** `chi_all_lambda_general` is fast and correct
at A=1/2/3 (< 0.4 s), so the window transfer can be validated against it
byte-for-byte at those sizes before being trusted at A>=4 — which is exactly
where no independent check is affordable. Note the 1-ulp kernel wobble
(1.00229e-50) when setting that comparison's tolerance: compare tr_M, which was
measured to have spread EXACTLY 0.0, or use a tolerance above 1e-48.

**Risk.** The Hoefsmit off-diagonal sign/normalisation convention must match
this codebase's `_alpha_beta` / `D(delta)`; getting it wrong gives a plausible
wrong number rather than an error. The oracle is what catches that.
