---
# qou-pdfx
title: markov_trace_axiomatic_multi_atom cross-check diverges 15.4% from a 2026-07-05 witness
status: todo
type: bug
created_at: 2026-09-06T10:15:33Z
updated_at: 2026-09-06T10:15:33Z
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

- [ ] Establish whether `markov-trace-atomic-proton-full.witness.json` is stale.
      If it is, regenerate it and the cross-check resolves itself; if it is not,
      there are two live values for `tr_M(proton)` differing by 15 %.
- [ ] Drain the 8 raw-float64 witness fields.