# The hecke_core symbolic-vs-numerical migration check now FAILS — and nothing noticed for four months

**Date:** 2026-08-30 · **Bean:** `qou-nro6` · **Producer:**
[`computations/substrate/hecke_core_symbolic_migration.py`](../../computations/substrate/hecke_core_symbolic_migration.py)

`hecke-core-symbolic-migration.witness.json` records that the numerical fast
path `hecke_core.py` and the symbolic module `hecke_core_symbolic.py` agree to
the floating-point floor. Two content manifests name it in their
`computation.witness` field, so it is a **maintenance contract**.

It had **no producer**. It was a frozen record of a pass on 2026-05-02, and
nothing has re-run it since. Written for `qou-nro6`, the producer's first run
**fails**.

## What the producer measures

| quantity | committed (2026-05-02) | now | verdict |
|---|--:|--:|---|
| NF basis, max abs delta | 2.78e-17 | **1.91e-16** | still at the float64 floor ✓ |
| `V_full` abs delta | **1.1155** | **3.94e-16** | *improved* — see below |
| Markov trace abs delta | 2.22e-16 | **0.1007** | **FAILS** |
| `α_EM⁻¹` abs delta | 2.84e-14 | **1.52e-06** | **FAILS** |

## The Markov trace: both paths drifted, independently

| | 2026-05-02 | now |
|---|--:|--:|
| numerical `HC.nf_tr` | 1.0299809251269565 | **1.1463376906350053** |
| symbolic `HS.nf_tr_sym` at `q₀` | 1.0299809251269 | **1.0456651474099089** |

They agreed to 2.2e-16 when the witness was written. They now differ by
**0.1007** — about 9.6 %. Neither current value is the committed one, so this
is not one path moving away from a fixed other: **both changed**.

**It is not the anchor.** The committed witness used
`q0 = 1.1099785955541805`, the CODATA-2018 muon derivation, retired by the
2026-08-22 ruling; this producer runs at the canonical proton pin. Evaluating
the *same* symbolic expression at all three candidate pins:

    proton  1.1099785827513808  ->  1.04566514740990890757
    muon-B  1.1099785955541805  ->  1.04566515371260724904
    muon-A  1.1099785955573347  ->  1.04566515371416003214

The whole pin spread is **6.3e-9**. The divergence is 0.1007 — **seven orders
of magnitude larger**. The anchor accounts for none of it.

**Nor is it the harness.** The discrepancy reproduces with two direct library
calls and no intermediary:

```python
HC.nf_tr(HC.build_atom_nf(1, 0))              # 1.1463376906350053
HS.evalf_at_q0(HS.nf_tr_sym(HS.build_atom_nf_sym(1, 0)))   # 1.04566514740991
```

Both modules read `q₀` from the same `q_parameter.q_at`, so it is not a layer
straddle either.

## `V_full` moved the other way, and that matters

The committed witness records `max_v_full_abs_delta = 1.1155` — the two paths
**did not agree** on `V_full` when the witness was written, and it was recorded
as passing anyway because no assertion covered it. It now agrees to 3.9e-16.

So the record contained a live disagreement that nobody was alerted to, in the
same file whose `allPassed: true` was the reason to trust it. That is the
argument for the producer, independent of the failure it found.

## What this does NOT establish

**Which path is right.** The numerical and symbolic modules disagree; deciding
which reflects the intended mathematics is a code-and-physics question for
whoever owns `hecke_core`, not something a provenance producer settles. This
audit says only: they used to agree, they no longer do, the pin does not
explain it, and the divergence went undetected because the check existed only
as a frozen record.

Nor does it establish **when** it broke. Both modules have changed since
2026-05-02; bisecting the divergence is separate work.

## The manifests also disagree about who produces this witness

    mba-step02-gs-reduction.ts           engine "rust",  tools/hecke-engine/src/gb_nf_reducer.rs
    e-hartree-categorical-derivation.ts  engine "sympy", computations/substrate/hecke_core.py

Two manifests, two different producers, and **neither named file mentions the
witness**. The sympy claim is closer — this is a sympy-vs-float64 comparison —
but it names the *numerical* module, only one of the two sides. Recorded, not
silently resolved: correcting a manifest is a content edit and belongs with the
author.

## Disposition

The committed witness claimed `allPassed: true` on a check that fails today.
It is **replaced with the producer's honest output**, failing assertions
included, rather than left asserting a pass that no longer holds. The producer
is committed alongside it so the next reader can re-run rather than trust.
