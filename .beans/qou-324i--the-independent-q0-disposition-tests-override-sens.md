---
# qou-324i
title: The `independent` q0 disposition tests override-sensitivity, not q0-independence — 7 false positives
status: todo
type: task
priority: normal
created_at: 2026-08-22T20:27:28Z
updated_at: 2026-08-23T08:32:24Z
---

Found on `qou-1c4y` / PR #5464 while re-measuring after #5457 merged (`238fc79f6e`).
Sibling territory: bean `qou-o922`, PR #5477.

## The test and what it actually measures

A producer is dispositioned `q0Anchor: independent` when its output is
**byte-identical under `QOU_Q0_ANCHOR=muon` vs `=proton`**, taken as proof that
it never reads q₀.

That environment variable only reaches q₀ resolution that goes **through
`q_parameter`**. So the test measures *override-sensitivity*, and
override-sensitivity coincides with q₀-independence **only when q₀ arrives via
`q_parameter`**. Two paths defeat it:

1. **A hardcoded q₀ literal.** An env var cannot change a string constant.
2. **A direct read of `q-pinning-50-digit.witness.json`.** Never consults
   `q_parameter`, so the override is not in the path.

Both produce byte-identical output under either anchor **while being
hard-pinned to muon.**

## Measured (post-#5457, on main)

    37   witnesses stamped q0Anchor: independent
     9   still carry muon digits in the file
     6   producer has a HARDCODED muon q0 literal
     1   producer reads the pinning witness directly
     2   neither — value inherited from an upstream input

So **7 of 9 are provably not q₀-independent.** Worked example —
`qbeta/qbeta_c3_rung_structure_analysis.py:74`:

```python
Q0_MP_PIN = "1.1099785955573347198997632204832250266562084087802"   # muon
...
q0_mp = mp.mpf(Q0_MP_PIN)          # "Numerical check at q_0"
```

Its witness records `q_0 = 1.1099785955573347198997` under the primary pin key
while asserting `independent`. The label says the producer does not use q₀; the
data block says it evaluated at the muon one.

The six hardcoded: `markov_identity_symbolic_probe`,
`probe_he4_magic_baryeven_prune`, `qbeta_c3_rung_structure_analysis`,
`qbeta_habiro_f_from_shape_collapse`, `qbeta_rung1_div25_framing_squared_test`,
`z2bn_tau_derivation_probe`. Direct-read: `lambda_scale_substrate_probe`.
Inherited: `chirality_topology_binding_probe`, `fitted_labelled_canonical_audit`.

## Scope — what is NOT claimed

- **The drain is good work and the `save()` carry-forward fix is correct.** This
  is a blind spot in one criterion, not a reason to revert anything.
- **28 of the 37 `independent` labels are untouched** by this — they carry no
  muon digits and nothing here disputes them.
- **A hardcoded literal is not automatically wrong.** A probe may legitimately
  pin a specific q₀ for a stability check. The defect is the **label**: calling
  it `independent` records the opposite of what the producer does, and hides it
  from every subsequent pin audit.

## Suggested strengthening

Make the disposition require BOTH the env-override invariance **and** a source
check: no q₀-shaped literal (`1.10997858` / `1.10997859`), and no direct read of
the pinning witness. My `computations/audits/q0_hardcoded_pin_audit.py` already
does the literal half (strips comments/docstrings via `tokenize`), and
`q0_muon_population_partition.py` on #5464 does the direct-read half.


## ANSWERED (2026-08-23) — it IS the Markov parameter, measured

I recorded above that I would not claim `load_q_50dps`'s z is *the* Markov
parameter without a corpus read or an owner call. Measurement settles it.

The defining Markov property `tr_M(T_w) = z^{ℓ(w)}` was tested against both
conventions at the proton pin:

    max|tr_M - z_D^l| = 2.5391265e-50    (holds, to the arithmetic floor)
    max|tr_M - z_C^l| = 0.12606583       (fails)

and `tr_M(T_1) = 0.61268803714647 = z_D` exactly. Corroborated by naming: of
the 24 callers that bind the z return, `pentagon_reduction_li2q.py` calls it
`z_markov` and `e0_lambda_composite.py` calls it `ZMARK`.

So `load_q_50dps` returns **z_C in the Markov role**, under a canonical-D
regime, with 24 consumers. The convention-C detector misses it because it is a
**tuple-element return** — the blind spot this bean records.

Full diagnosis in `qou-rh31`. Fix belongs with the convention-D tranche
(`qou-cds1`/`qou-cds2`), not a q₀-pin PR; and some consumers may use the z in a
pair-weight role (`compute_t2_t3_from_vols`: `T3 = z²·Σ_{i<j}`) rather than the
Markov role, so a per-consumer read is still required before changing it.


## 🛑 CORRECTION + the real cause (2026-08-23): it is `mpf(1)`, not the tuple return

I wrote above — and told #5514 — that the convention-C detector misses
`load_q_50dps` **because it is a tuple-element return**. That is **wrong**.
The site is an ordinary assignment (`z = mpf(1)/...`), and the scan already
covers assignments named `z`. Retracted.

**The real cause is the numerator.** `is_c_form` accepted only a bare literal:

    1 / (mp.sqrt(q0) + mp.sqrt(qi))        -> True
    1.0 / (mp.sqrt(q) + mp.sqrt(qi))       -> True
    mpf(1) / (mp.sqrt(q) + mp.sqrt(qi))    -> FALSE
    mp.mpf(1) / (mp.sqrt(q) + mp.sqrt(q_inv)) -> FALSE

**And `mpf(1)` is how the corpus is REQUIRED to write it.** The NO-FLOAT64
discipline mandates carrying `mpmath.mpf` rather than a bare Python literal.
So **complying with the precision rule made a site invisible to the convention
rule** — one house rule blinding another. That is a much better taxonomy entry
than the one I first gave.

## Measured

Fix is a 20-line `_is_unit_numerator()` predicate, used by `is_c_form` and
`is_c_form_reciprocal`. Selftest **53/53** (3 new `mpf(1)` fixtures).

    ACTIONABLE convention-C sites:  1  ->  31

Enumerated all 43 scan rows by hand: every one is
`1/(sqrt(q) + sqrt(q_inv))` or `1/(sqrt(q) + 1/sqrt(q))` — convention C
exactly — and the `DELIB` rows are correctly excluded as labelled comparisons
(`z_C`, `zC`, `z_c`). **No false positives found.** Several are named outright:
`Z_MARK`, `z_mark`, `z_markov`, `z_m`.

So the corpus believed it had **one** actionable C site and has **31**.

Note the standing AGENTS.md posture was already right about this and should
stay: *"treat the remaining C surface as UNMEASURED rather than clear."* A
clean detector run was never evidence the surface was clear, and this is the
fourth spelling found by a detector written to catch the previous blind spot.
