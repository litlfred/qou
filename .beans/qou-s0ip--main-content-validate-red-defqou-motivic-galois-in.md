---
# qou-s0ip
title: 'main content_validate RED: def:qou-motivic-galois-instance requires Lean and its ref names a module that does not exist'
status: todo
type: task
created_at: 2026-08-22T12:24:51Z
updated_at: 2026-08-22T12:24:51Z
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

## 2026-08-22 — I inspected the witness, and my own "just lift the numbers" claim was wrong

I told the owner the real fix was probably *"lifting existing numbers into
Lean"*, on the strength of the block carrying a `status: "verified"` computation
witness. **Having actually read the witness, that was too optimistic and I am
retracting it.**

`computations/probes/habiro-frobenius-probe.witness.json` (57 KB, computed
2026-05-03, `commitSha 610a6aa2`) contains, for **5 atoms** (p, D, T, ³He, n),
Frobenius data at **9 primes**: 2, 3, 5, 7, 11, 13, 17, 19, 23.

Three separate reasons it does not lift:

**1. The class field is total; the data is finite.**
`MotivicGaloisCharacter.frobenius_at : Nat.Primes → Mhat` is a function on
**all** primes. The witness stops at 23. Lifting it gives a partial function;
completing it to a total one means inventing values at every prime ≥ 29. That
is the invention I said I would not do, just relocated.

**2. The full-trace compatibility check FAILS, for every atom.** Per-prime
entries carry `step2_full_trace_passed: false`, and every atom's
`step2_summary` has `step2_full_trace_compatible: false`. What passes is
`all_truncated_primes_compatible: true` — the *truncated* Pochhammer version.
The top-level `step2_all_atoms_compatible: true` and the block's
`status: "verified"` both summarise the **truncated** check, not the full one.
So "verified" is narrower than it reads, and an instance built on it would
inherit that narrowing silently.

**3. The witness is flagged `auditOnly`**, pointing at
`docs/audits/2026-05-02-m-iso-l-function-handoff.md`. It is handoff material,
not a production artefact.

**What is genuinely good about it:** the values are **exact**, not float —
`frob_full_in_Z_zeta_str: "-2/3"` in `ℤ[ζ]`, with `frob_p_is_exact: true` and
`exact_via: "pochhammer_truncates_inside_data"`. So the arithmetic is liftable
in kind; it is the **coverage** and the **failing full-trace check** that block
it, not precision. That distinction matters for whoever picks this up.

### Revised options

1. **Write the real instance** — now understood to need a *closed form* for
   `frobenius_at` valid at all primes, not a table. The witness shows the
   truncation mechanism (`(u;u)_m` vanishes once `m ≥ 2p`), which is a plausible
   route to one, but deriving it is research, not transcription.
2. **Reclassify the block** so the validator stops requiring Lean for something
   genuinely unformalised. Editorial, and the honest interim.
3. **Leave red and tracked.** Still the default, and still costly — a
   permanently red gate trains everyone to ignore it, which is how the
   four-month unrun Lean CI happened.

My earlier framing made option 1 sound like an afternoon's transcription. It is
not. Option 2 remains the cheapest honest move.
