---
# qou-pdfx
title: markov_trace_axiomatic_multi_atom cross-check diverges 15.4% from a 2026-07-05 witness
status: completed
type: bug
priority: normal
created_at: 2026-09-06T10:15:33Z
updated_at: 2026-09-07T10:01:12Z
---

Surfaced by the qou-hu1f regeneration pass. Pre-existing: fails identically under both intra orderings, so NOT a consequence of the 2026-09-05 ruling.

## Measured

    atomic_proton_full (stored witness)   1.6331533774490543
    multi-atom recursive (computed now)   1.88431946725
    relative |Δ|                          0.153792      ← 15.4 %

`markov-trace-atomic-proton-full.witness.json` is dated **2026-07-05** and
carries `1.6331533774490543`. The recursive path computes `1.88431946725`,
which is the value `markov-trace-recursive.witness.json` also carries and which
`prop:markov-trace-recursive-reducer` publishes as `tr_M(σ₁⁷σ₂⁴) = 1.884319…`.

So **two of three agree and the 2026-07-05 witness is the outlier.** That is the
shape of a stale artefact, not of a live disagreement — but it is not proven,
and the probe currently reports the divergence as its own failure rather than as
the stored value being old.

## NOT the intra-ordering ruling

Confirmed by running the producer with `intra_order` forced to each value:
`char_fast_cross_check_ok` fails **identically under grouped and borromean**.
Exit code alone was misleading here — a raw-float64 gate fires under both, so
the failure had to be compared at *assertion* level to see that.

## Also carried by this producer

`⚠ raw-float64: 8 raw float64 field(s) would enter the witness` —
`.assertions[*].computed/expected/tolerance` and
`.atoms.{proton,neutron}.m_MeV_codata`. Separate hygiene defect, same file.

- [x] Establish whether `markov-trace-atomic-proton-full.witness.json` is stale.
- [x] Drain the 8 raw-float64 witness fields.

---

## Summary of Changes (2026-09-07) — stale, and the "cross-check" was never one

### The witness was stale, provably

Its own provenance says so: it records `scriptHash: d3e38be9191d`; the producer
now hashes to `ac8a24dafeee`. Not a timestamp argument — the **functional form**
changed. The stored symbolic value carries half-integer powers,

    (2*q**(41/2) + 4*q**(39/2) - … ) / (q**13 + 3*q**12 + 3*q**11 + q**10)

and the live one is a Laurent polynomial in q² over `q**7*(q**2+1)**2`. That is
the convention C → D migration, and the witness predates it.

Regenerated: **1.88431946725497502509…**, agreeing with
`markov-trace-recursive.witness.json` (`1.884319467254975`) and with
`prop:markov-trace-recursive-reducer` to every digit the latter carries. Three
live paths agree. `1.6331533774490543` was the outlier, as the bean suspected.

### The remaining failure was not a cross-check at all

Regenerating did NOT clear `matches_char_fast`. Reading it:

    char_fast_ref = 1.6334          # a literal
    ratio_to_charfast = val_at_q0 / char_fast_ref

There is **no `char_fast` function in the live tree** — the only
implementations are under `computations/_deprecated/`. So this compared a
computed convention-D value against a transcribed convention-C decimal, and
1.6334 is the same stale number the witness carried. The "15.4 % divergence"
was one defect reported twice.

`markov_trace_recursive.py` had already diagnosed the identical constant and
says it best:

> Checking a migrated value against a frozen pre-migration decimal is worse
> than not checking it, because the disagreement it reports is really agreement
> with the wrong thing.

So the assertion is **removed, not re-tuned**, following that precedent, and its
absence is recorded in the witness as
`cross_check: "none — the only available reference was a frozen convention-C
decimal"`. The ratio is still printed, labelled as historical.

### Replaced with a check that has content

An assertion-free witness would be a weaker artefact, so the slot now carries a
**live structural** check with no external reference:
`convention_d_form_has_no_half_integer_q_powers`. That is precisely the property
the migration turns on — the superseded form carried `q**(41/2)` — it is
computable here, and it fails loudly if a √q atom is ever reintroduced. Passes.

### raw-float64 drained at the source, not stringified

The gate's instruction is to carry mpmath and serialise with `fmt`, not to
stringify a float. `Q_MP` (the exact 50-digit mpf) was being `float()`-ed before
any arithmetic, so the substrate precision was gone before the values were
recorded. Now the whole chain stays in mpmath at `set_compute_dps()` and is
serialised with `fmt`:

    tr_M_proton_at_q0     1.88431946725497502509029472310815626347249744177148556611060
    rho_p_codata          974.438004175215075372613460349834371486956088579552847143258

Zero raw float64 fields remain in the witness; 1/1 assertion passes.
