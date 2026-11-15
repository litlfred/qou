---
# qou-s0ip
title: 'main content_validate RED: def:qou-motivic-galois-instance requires Lean and its ref names a module that does not exist'
status: completed
type: task
priority: normal
created_at: 2026-08-22T12:24:51Z
updated_at: 2026-08-23T20:27:09Z
---


## Diagnosis 2026-08-22 — precise, and deliberately not patched

`bun run scripts/run-validate.ts` on `main @ cc6a0b09` exits **1**:
`✗ Invalid — 29 issue(s)`, with exactly **one** `✗` error:

```
✗ [qou-motivic-galois-instance]: Definition "def:qou-motivic-galois-instance"
  requires Lean formalization. Expected sibling file:
  mass-endomorphism/qou-motivic-galois-instance.lean
  (or Lake-tree resolution from lean.ref
   "qou:QOU.LiftingDescent.QOUInstance.qouMotivicGaloisChar")
```

Verified pre-existing by stashing unrelated work. It was 28 issues on
2026-08-21 and 29 on 2026-08-22; the extra is a warning, the error is the same
one. **`main` has been red for at least a day.**

### What is actually missing

- `QOU.LiftingDescent.QOUInstance` — **no such module** anywhere.
- `qouMotivicGaloisChar` — **no such declaration** anywhere.
- No co-located sibling `qou-motivic-galois-instance.lean`.
- **No declaration carries the block's `\label`**, so the label test that fixed
  `thm:su2-emergence`, `def:ns-regular-qou` and `prop:descent-eigenspaces`
  finds nothing here. This is genuinely unformalised, not mis-referenced.

It errors rather than warns only because the block is a `definition(...)`, and
the validator requires Lean for definitions. The ~33 other unformalised refs on
`qou-2u26` are advisory because their builders do not.

### Why it was not patched

The target class **does** exist: `QOU.LiftingDescent.MotivicGaloisCharacter`
(`lean/QOU/LiftingDescent/MotivicGaloisCharacter.lean:60`), with exactly one
field, `frobenius_at : Nat.Primes → Mhat` — pure **data**, no propositional
obligation. So an instance is *writable* with no proof burden.

That is precisely why writing one here would be wrong. Supplying
`frobenius_at` means inventing the Habiro → Frob_p map, which is substrate
content only the author has. And the class's own docstring records that its
propositional field was removed in 2026-08-12 because *"encoding it as a class
field forced every instance to either prove it or launder an axiom"*.
Fabricating the data field now would be the same laundering wearing a different
hat — the defect `qou-ffwk` has spent this whole batch removing.

Creating a co-located stub to silence the validator would be the same error.

### Options, for an owner call

1. **Write the real instance** — needs the Habiro → Frobenius map. The block
   already carries a *verified* computation witness
   (`computations/probes/habiro_frobenius_probe.py`), so the data may already
   exist in numeric form and only need lifting into Lean.
2. **Reclassify the block.** If nothing is defined yet, `definition(...)` may be
   the wrong builder; a kind that does not require Lean would make the validator
   honest rather than silenced. This changes what the corpus claims about the
   block's status, so it is an editorial call.
3. **Leave red and track here.** Costly: a permanently red gate trains everyone
   to ignore it, which is how the four-month unrun Lean CI happened
   (`.claude/skills/local/prepare-merge.md`).

Option 1 is the real fix; option 2 is the honest interim; option 3 is what is
happening by default.

## Resolved 2026-08-23 — option 2 taken (owner call)

`definition()` → `conjecture()`, `def:` → `conj:qou-motivic-galois-instance`,
on branch `claude/n1dj-volume-iso-reading-2026-08-22` (`db42bed7a4`).

    run-validate  52 → 51 issues — one removal, zero additions

The `✗` this bean names is gone. `lean-file-exists` has `appliesTo:
["definition"]` and nothing else, which is why this one block errored while
~33 comparably unformalised refs only warn.

### Also carried

- `interprets` / `uses` retargeted on `ex:…-per-cell` and `rem:…-verification`.
- QA sidecar identity fields: `label`, `kind`, and the `paths.lean` /
  `source_hashes.lean` / `source_hashes.lean_statement` keys, which pointed at
  the `.lean` deleted on 2026-08-12. Verdict `field_hash` entries left alone —
  they are meant to go stale and force re-review.
- The dangling `lean.ref` and the `axiom` tag, each dropped into an authorNote
  rather than deleted silently.
- Two claims in `rem:…-verification` that had been false since 2026-08-12: a
  live link to the deleted `.lean` describing an `almost_everywhere_nontrivial`
  field removed from the class that same day, and "the perpetual obstruction
  becomes an unconditional theorem" stated as present fact when it is
  conditional on an instance that does not exist.

### Why conjecture is the honest kind, not just the un-gated one

The bean's option 2 was conditioned on "if nothing is defined yet". Something
*is* defined — in prose: `Frob_p = f(u)|_{u = ζ_2p} ∈ ℤ[ζ_2p]`, one prime at a
time. But `MotivicGaloisCharacter` wants a single `frobenius_at : Primes →
Mhat`, so the content of the claim is that those per-prime evaluations cohere
into one `Mhat`-valued function. The remark argues that structurally from the
Habiro theorem and does not prove it. So the block is a claim, not a
construction — `conjecture` is right on the mathematics, not only on the gate.

### Option 1 remains open, and is closer than this bean assumed

`habiro_frobenius_probe.py` is a **verified** computation with a witness, so
the numeric side of `frobenius_at` exists. What is missing is the lift into
Lean plus the coherence argument — not the data.

### One thing this bean got wrong

It recorded main as having "exactly one `✗` error". As of `origin/main`
`797db0ebf7`, main has **five**: this one plus four orphan QA sidecars
(`qbeta-fmap-structural-form`, `q-clt-jsj-mass-scaling`,
`q-beta-c3-continuum-geometry`, `spectral-decomposition-qvalue-interpretation`),
31 issues total. Those four are not on this branch and are not this bean's
scope, but "main is red for one reason" is no longer true.
