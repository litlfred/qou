# Item C + Q6 probes (2026-05-17)

> Follow-on to PR #684 (m_p Item A closure) per workplan v5 §4.

## Item C — T6 Habiro residue at A=1

> **Item C** (PR #671 audit): "*Full Habiro residue at A=1: T6 ~
> 0.68 may be a truncated subset of a larger series (cheap to
> probe).*"

### Finding: same pattern as Item A — stale aggregator value

T6 for A=1 IS already computed at 50 dps in the canonical residue
witness:

| Source | T6 at A=1 (proton) |
|--------|-------------------|
| [`term6-habiro-residue-mpfr-50dps.witness.json`](../../computations/term6-habiro-residue-mpfr-50dps.witness.json) (canonical 50 dps) | **0.98169832816688179653645 MeV** |
| [`mass-formula-6term-mpfr-50dps.witness.json`](../../computations/mass-formula-6term-mpfr-50dps.witness.json) on main (aggregator output) | 0.68071547375114662431009 MeV |
| The "T6 ~ 0.68" cited in #671 audit | matches the **stale** aggregator value, NOT the canonical residue |

`term_6_habiro_residue_mp(A=1)` in
`mass_formula_6term_mpfr_50dps.py` correctly returns **0.98169...**
when called directly. The 0.6807 in the on-main committed witness
is from a stale earlier aggregator run (predates the residue
pipeline rewiring).

### What PR #671 actually identified

Not "T6 is a truncated subset of a larger series" — but rather
"two different T6 values are co-existing on main (residue
witness vs aggregator)". The structural question (is T6 a
truncation?) reduces to: which value is canonical, the 0.68 or
the 0.98?

Per the residue-pipeline lineage:
- 0.68 is from the **f64 producer** `term6_residues_at_roots`
  (legacy)
- 0.98 is from the **MPFR-native bridge**
  `term6_habiro_residue_mpfr_50dps_bridge.py` (canonical 50 dps)

The 0.98 value is the canonical one. The Item A fix on PR #684
already updated the aggregator path; once PR #684 lands, a
re-run of `mass_formula_6term_mpfr_50dps.py` will pick up the
canonical T6 = 0.98 instead of the stale 0.68 for proton.

### Item C closure status

**Closed structurally**, pending PR #684 to land:
- T6 IS computable at A=1 (no missing data)
- The "stale value vs canonical" gap is the same stale-witness
  pattern as Item A
- Once #684 merges and the aggregator re-runs, proton T6 = 0.98
  MeV propagates to consumers

Recommend: After PR #684 lands, re-run `mass_formula_6term_mpfr_50dps.py`
on main and verify T6 for proton matches the residue witness
(0.98169..., not 0.68071...). Single witness regen + commit.

## Q6 — MPFR precision floor in `seminormal_mpfr`

> Workplan v5 §6 Q6: PR #683 finds the chain agrees with Hoefsmit
> only to ~14 digits despite `--dps 50` request. Is this an actual
> `seminormal_mpfr` precision bug, or a convention difference?

### Status: investigation blocked on PR #683 merging

The `hecke-canonical-chi` binary that exposed Q6 lives on the
in-flight PR #683 branch, not on main. Re-probing the precision
floor requires either:
1. Cherry-picking PR #683 into a sibling branch (creates conflict
   territory)
2. Waiting for #683 to merge

### What can be said now (static code audit)

`seminormal_mpfr.rs` precision plumbing looks consistent on
inspection:

- `dps_to_bits(50) = ceil(50 · 3.32193 + 2) = 169` bits → adequate
  for 50 dps (log₂(10⁵⁰) ≈ 166)
- All `Float::with_val` allocations in `build_blocks_mpfr` and
  `chi_lambda_braid_mpfr` use the same `prec` parameter
- The two `sqrt` calls (line 85: `b_sq.abs().sqrt()`; reentry at
  198 via `h = q - q.recip()`) operate on `Float` values with
  `prec` precision; MPFR's `sqrt` preserves precision

### Suspected root cause (hypothesis pending confirmation)

The ~14-digit floor likely comes from **outside** `seminormal_mpfr`:

1. The **canonical braid word's averaged-crossing expansion** in
   `wenzl_lr::chi_lambda_canonical_h_n_mpfr` parses each sub-word
   result via `Float::parse(s).expect(...)` followed by
   `Float::with_val(prec, v)`. If the string has fewer digits than
   `prec` bits, this is the precision floor — but `chi_lambda_braid_mpfr`
   emits the result via `trace.to_string_radix(10, Some(dps as usize))`
   which DOES emit `dps` digits.

2. The **Python combiner** `canonical_tr_m_via_rust.py` previously
   downcast `y_λ` to f64 (PR #683 gemini-fix replaced with
   `mp.mpf(str(y_lam))`); but the precision-floor symptom predated
   that fix.

3. The **q_str parsing** in `chi_lambda_braid_mpfr` — accepts a
   decimal string of arbitrary length. PR #683 passes
   `Q_50_DIGIT_STR` (52 chars; sufficient for 50 dps). OK.

The most likely culprit is **fixed-point string conversion**
somewhere in the chain — possibly the `to_string_radix` in
`chi_lambda_braid_mpfr` rounds at 50 dps, then `Float::parse` in
the averaging-expansion accumulator re-parses at 169 bits but the
string is already truncated.

### Q6 next steps

1. **(after #683 merge)** Add a Rust integration test:
   `chi_lambda_canonical_h_n_mpfr(λ=(3), n=3, [proton word], q_50dps, dps=50)`
   should match Hoefsmit's `1.0653062285923892551532775699...` to
   50 dps. If it doesn't, instrument each precision-loss candidate
   above one at a time.
2. **(quick)** Try `dps=100` and see if agreement extends. If yes,
   internal precision is OK and the 14-digit floor was a measurement
   artifact. If no, hunt the truncation.

This audit doc preserves the Q6 finding for follow-up; the
investigation itself is deferred until PR #683 merges.

## Coordination summary

| Item | Closure | Blocking |
|------|---------|----------|
| Item A (T2+T3 KeyError) | structural ✓ (PR #684) | numerical (#682 Li₂^q) |
| Item C (T6 ~ 0.68 truncation?) | structural ✓ (stale aggregator, this audit) | aggregator re-run after #684 |
| Item B (T5 attribution) | open R&D, no known ansatz | — |
| Q6 (MPFR precision floor) | static audit done | live probe after #683 merge |
