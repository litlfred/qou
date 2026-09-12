---
# qou-v6wz
title: 'qbeta-ck-basis-constrained-pslq goes RED on re-run: c3 moves by 972, and the witness is stamped q0-independent while carrying q0_canonical'
status: todo
type: bug
priority: high
created_at: 2026-09-04T11:46:20Z
updated_at: 2026-09-12T08:05:24Z
---

FOUND 2026-09-04 as a hook-triggered producer re-run in a working tree, NOT by looking for it. Re-run against main at eb2f4588ce. NOT MY BRANCH'S CHANGE - reverted rather than committed, so this bean is the only record. Reproduce with: run the producer for computations/probes/qbeta-ck-basis-constrained-pslq.witness.json on current main and diff.

THE WITNESS GOES RED. allPassed: true -> false. Its own self-check: computed 1.5835e-30 -> 972.3619589513947 against tolerance 1e-08, passed false.

c3_reproduced_canonical: -2.02018812814143945582 -> -974.382147079536184945.

THE ANCHOR RE-PIN DOES NOT EXPLAIN IT, by a factor of 7.8 MILLION. q0_canonical moved 1.1099785955573347... -> 1.109978595642739... which is the retired pin -> the live CODATA-2022 pin, a 0.0769 ppb move (the qou-3f7a drain, correct and expected). With u^3 = 6.178685604e-7 the amplification gives a c3 shift of 1.245e-04. The observed shift is 972.362. Ratio 7.813e+06. So the migration is a red herring; something else changed.

THE LIKELY CAUSE IS IN THE SAME DIFF: anchor_slope_dc3_dq 4.65741e+6 -> 3.81298e+6. That is exactly the stale-4.66e6 -> corrected-3.84e6 figure AGENTS.md documents at length (the stale-c3 twin; beans qou-3nva / qou-kt8o). So a sibling corrected the slope - correctly - and c3_reproduced, which is computed FROM the slope, was not reconciled. Note the failing check's 'computed' value 972.3619589513947 IS the c3 shift 972.362 to ten digits: the check is measuring exactly this discrepancy.

SECOND DEFECT, INDEPENDENT AND WORSE FOR THE AUDIT SURFACE. The refreshed witness is stamped
    q0Anchor: 'independent'
    q0AnchorReason: 'producer declared q0-independent at the stamp site (q0_anchor=False): no q0-dependent field in this witness'
while the witness plainly carries q0_canonical AND c3_reproduced_canonical, both q0-dependent. The stamp contradicts the file it is on. A q0-dependent witness labelled q0-independent escapes the q0-anchor-flip audit entirely - it will never be reported as a flip no matter which pin it is on. Verify at the producer's stamp site (q0_anchor=False) before fixing; the reason string suggests the flag is hand-set rather than derived from the emitted fields.

UNRELATED AND CORRECT, noted so nobody 'fixes' it: the key rename 'Vol(4_1)=2*Lambda(pi/3)' -> 'Vol(4_1)=2*Cl_2(pi/3)=6*Lambda(pi/3)' with the VALUE unchanged (2.02988321281930725004240510855) is the Lambda-vs-Cl_2 naming drain (qou-zdz5) landing properly.

WHY THIS IS NOT MINE TO FIX HERE: PR #6584 is the eightfold/hyperbolic-volume arc; this is the c_k ladder producer, a different domain, and the change that broke it came from main. Fixing it would widen the PR and the reviewer is not loaded on that area. Also do NOT make it green by widening the tolerance or re-baselining - AGENTS.md forbids that explicitly; fix at the producer by reconciling c3_reproduced with the corrected slope.

DEFECT 2 FIXED 2026-09-05 (PR #6824, branch claude/fervent-noether-zssd1k). Producer stamp q0_anchor=False -> q0_anchor='ambiguous' (the manifest's own classification for this stem; reads both pins on purpose, pin undetermined). No bare q0Value. Verified clean: not a flip in q0_anchor_consistency_audit, not listed in q0_value_drift_audit. The stale '# no q0 in this producer's cone' comment corrected.

DEFECT 1 STILL OPEN (deferred): the c3_reproduced_canonical ~ -974 RED. cds1-gated c_k-derivation work: a sibling corrected anchor_slope_dc3_dq 4.66e6 -> 3.84e6 (qou-3nva/qou-kt8o) and c3_reproduced (computed FROM the slope) was not reconciled. Fix by reconciling at the producer under the cds1 c_k re-derivation; do NOT widen tolerance/re-baseline. Bean stays open for defect 1.


---

## RE-MEASURED 2026-09-12 — defect 2 FIXED; defect 1 is now COMMITTED RED ON MAIN; and **this bean's stated cause is REFUTED**. STAYING OPEN.

### Defect 2 (the mis-stamp) — fixed

`41ac6e9804a` did what its subject says. The committed witness now carries
`q0Anchor: "ambiguous"` with a real reason: *"reads BOTH pins on purpose:
`c3_reproduced_canonical` is at the muon canonical pin … while `q0_proton` /
`anchor_slope_dc3_dq` are at the proton pin."* The false `independent` stamp is
gone.

### Defect 1 (the RED) — not fixed, and WORSE than when this bean was filed

Read off `origin/main` directly, not from a working tree:

```
allPassed                     False
assertions[0]                 extraction_chain_reproduces_cache_c3
  computed  972.3619589513947   expected 0.0   tolerance 1e-08   passed False
c3_reproduced_canonical      -974.382147079536184945277477315
anchor_slope_dc3_dq           3.81298e+6
```

This bean records the RED as found in a working tree and *"reverted rather than
committed, so this bean is the only record."* **It is now committed.** A witness
whose own self-check fails, and whose `c3_reproduced_canonical` is `-974.38`
against a true `c_3 ≈ -2.02`, is sitting on main.

### 🛑 THE STATED CAUSE IS REFUTED — do not act on it

This bean says: *"a sibling corrected the slope — correctly — and `c3_reproduced`,
which is computed FROM the slope, was not reconciled."*

**`c3_reproduced_canonical` is not computed from the slope.** In
`computations/probes/qbeta_ck_basis_constrained_pslq.py` they are two
independent outputs, at **different pins**, and the producer says so in its own
comment at lines 420-421:

```python
323:   "c3_reproduced_canonical": mp.nstr(c3, 30),        # muon canonical pin
337:   "anchor_slope_dc3_dq":     mp.nstr(slope_c3, 6),   # proton pin
420: # `q0_canonical` and `c3_reproduced_canonical` (computed at the muon
421: # canonical pin) AND `q0_proton` / `anchor_slope_dc3_dq` (the proton …
```

So reconciling one to the other is **not the fix**, and an agent following this
bean's diagnosis would go rewire a dependency that does not exist.

### 🛑 And the evidence offered for it is CIRCULAR

The bean's corroboration is: *"the failing check's 'computed' value
972.3619589513947 IS the c3 shift 972.362 to ten digits: the check is measuring
exactly this discrepancy."*

That last clause is right and it is why the observation proves nothing. The
assertion is **defined** as `c3_reproduced − cache_c3` against `expected 0.0`,
so it equals the shift **by construction, under any cause whatsoever**. It
cannot discriminate the slope hypothesis from any other.

### What the arithmetic DOES establish — the regression is localised

```
c3_reproduced (now)              -974.3821470795361849453
+ failing assertion's computed   +972.3619589513947
= ────────────────────────────────────────────────────
                                   -2.020188128141484945
this bean's recorded OLD value     -2.020188128141439456
difference                          4.5e-14
```

So **the cache is correct and unchanged** at `c_3 = -2.0201881281414`, and the
**extraction chain alone** regressed, from that value to `-974.3821470795`. The
slope correction is exonerated; the cache is exonerated; the fault is in the
chain between them.

That is a strictly better starting point than this bean had: the search is one
producer's extraction path, not a cross-witness reconciliation.

### NOT FIXED HERE, and why

Repairing it means re-running the producer and either correcting the chain or
re-deriving the reproduced value — which moves a published number and, per the
2026-09-07 ask-first override, is neither a precision increase nor
corpus-fixed (the corpus currently holds a **wrong** value here; what the right
one is, is exactly what is open). Recorded so the next agent starts from the
localisation instead of the refuted hypothesis.

**Relevant context, since it may be the same arc:** AGENTS.md records that
`qbeta_ck_cache.py` extracts ONE rung by inverting the target and **refuses to
run under convention D**, while the analysis script does not — which is how
stale ladder prose survived elsewhere. Worth checking whether the chain's
regression is a convention-frame crossing before assuming an arithmetic bug.
Cross-reference `qou-54g5` (the `c_5` slot) and `qou-cds1` (the D re-derivation).
