# 9b step 1 result — H1 refuted at its proposed location: 10A−5 is not trace-side bookkeeping

**Date:** 2026-06-13 · **Branch:** `claude/9b-derive-10a-minus-5-2026-06-13` (PR #2217)
**Probe:** [`probes/h1_exponent_location_probe.py`](../../computations/probes/h1_exponent_location_probe.py)
(witness `h1-exponent-location.witness.json`, 8/8). All inputs read from
the source witness `delta-lambda-canonical-residual.witness.json`; no new
physics computation, no fit.
**Work-plan:** [`2026-06-13-9b-derive-10a-minus-5-workplan.md`](../workplans/2026-06-13-9b-derive-10a-minus-5-workplan.md) step 1
(formalize-first: decide forced / forbidden / underdetermined before
numerics). Outcome: **forbidden** — the cheap structural check killed the
derivation route before any wide search ran, which is the discipline's
purpose.

## The test

H1 read `10A−5 = 5(2A−1)` as weight-5-per-chain-object crossing/jet
bookkeeping of the canonical trace difference
`B_pred = E₀·(tr_M(W_free) − tr_M(W_atom))`. If so, the *framework* side
must carry the exponent: `ord(B_pred) := log_{q₀} B_pred` must fall by
≈ 10 q₀-units per added nucleon. Decompose the witnessed exponent
identically (E₀ is A-independent and cancels from every slope):

$$ \mathrm{ord}(\Delta_\lambda) \;=\; \mathrm{ord}(B_{\mathrm{AME}}) - \mathrm{ord}(B_{\mathrm{pred}}). $$

## The data (q₀ from the source witness; identity reproduces its exponents to 2e-3)

| atom | A | ord(B_AME) | ord(B_pred) | sum = witnessed exponent |
|---|---|---|---|---|
| D | 2 | +7.663 | −7.326 | 14.989 ✓ |
| T | 3 | +20.490 | −4.444 | 24.934 ✓ |
| ³He | 3 | +19.585 | −4.010 | 23.596 ✓ |
| ⁴He | 4 | +32.036 | −3.236 | 35.272 ✓ |

Per-nucleon slopes along the N ≥ Z chain (D→T, T→⁴He):

| side | slope (D→T) | slope (T→⁴He) |
|---|---|---|
| ord(B_AME) — experimental | **+12.83** | **+11.55** |
| ord(B_pred) — framework trace | **+2.88** | **+1.21** |

## Verdict

- **H1 forbidden at the proposed location.** The canonical trace
  difference contributes a small *positive* drift (+1.2…+2.9 per
  nucleon, decaying toward 0 as the traces of large words shrink
  together) — wrong magnitude and wrong sign for a q₀^{−10A}
  bookkeeping. No crossing-count / jet-order accounting of
  `atom_braid_word_3A` vs its free variant can produce the exponent,
  because the words' trace difference simply does not move at that
  rate. The weight-5-per-chain-object reading dies with it.
- **Relocation.** The 10-per-nucleon increment is carried by
  `ord(B_AME)` — the *experimental* binding curve. The 2026-06-09
  observation re-characterises as
  `B_AME ≈ E₀ · q₀^{10A−5} · (trace factor drifting q₀^{+1..+3}/nucleon toward 1)`,
  i.e. an exponential description of the empirical curve (base
  q₀¹⁰ ≈ 2.84 per nucleon) dressed by a slowly varying framework
  factor. Deriving `10A−5` from the canonical chain is therefore
  equivalent to deriving `B_AME(A)` itself — the Track-A programme,
  not a word-combinatorics lemma.
- **Tier assessment (critical-distance, said plainly):** with two
  integer parameters (slope, offset), three compliant points (|dev| ≤
  0.27) and one outlier (³He, −1.40), and now the knowledge that the
  A-dependence is experimental-side, the observation sits at the
  *fitted-adjacent* end of near-match tier. It should not be cited as
  evidence of crossing-count structure; it remains a compact empirical
  summary of the light-isotope binding curve in q₀ units.

## Consequences for the work-plan

1. Step 2 (Lean combinatorial lemma for H1) is **moot** — contingent on
   H1 surviving. No §3b-cond bridge will be authored for this route.
2. Step 3's ⁶Li/⁷Li extension changes role: from derivation support to
   curve characterisation (does the empirical base stay near q₀¹⁰ at
   A ≥ 5?). Optional, low priority.
3. The step-9a flip gate (owner option B) is **unaffected in
   direction** but sharpened in content: the per-A normalisation R(K)
   still must come from a real derivation of the binding/density leg;
   this result closes one candidate route and prevents a wide
   word-bookkeeping search that could not have succeeded.
