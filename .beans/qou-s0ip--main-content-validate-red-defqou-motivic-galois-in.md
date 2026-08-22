---
# qou-s0ip
title: 'main content_validate RED: def:qou-motivic-galois-instance requires Lean and its ref names a module that does not exist'
status: completed
type: task
priority: normal
created_at: 2026-08-22T12:24:51Z
updated_at: 2026-08-22T20:59:03Z
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

## Resolved 2026-08-22 — option 2 (reclassify), branch `claude/s0ip-motivic-galois-reclassify-2026-08-22`

Owner picked option 2. `definition()` → `conjecture()`, label
`def:qou-motivic-galois-instance` → `conj:`, dangling `lean.ref` dropped.

**Measured, unpiped:** `main @ 4e34404aab` → `✗ Invalid — 52 issue(s)`, exit 1,
**11** `✗`. After → `✗ Invalid — 51 issue(s)`, exit 1, **10** `✗`. Set-diff of the
error lines: exactly one removed (this bean's), **none introduced**.

`main` is still red, for reasons that have nothing to do with this bean — see
the mpo finding below. The bean's own claim ("29 issues, exactly one ✗") was
true on `cc6a0b09`; main has degraded to 52/11 since.

### Two corrections to this bean's own diagnosis

1. **"The class has one field, so an instance is *writable* with no proof
   burden" — right fact, and it argues harder than the bean realised.** Any
   total `Nat.Primes → Mhat` inhabits `MotivicGaloisCharacter`, so an instance
   would *assert nothing*. Writing one is not merely under-motivated, it is the
   placeholder-carrier defect `qou-ffwk` spent this batch removing, one level up.
   That is now the recorded reason option 1 is not the "real fix".
2. **The witness cannot be "lifted", and not for the reason I gave earlier.**
   The block's formula `Frob_p = f(u)|_{u=ζ_{2p}}` *is* total in `p`, so
   "9 primes vs a total function" was the wrong objection. The real gap is that
   `f(u)` — the Habiro cyclotomic expansion — is not formalised. Separately, the
   witness's per-atom `step2_full_trace_compatible: false` with
   `n_primes_data_exhausted: 0` means full-trace compatibility was **never
   reached**, not reached-and-failed. Compatible where checked; open beyond.
   Recorded verbatim in the block's `caveat` authorNote.

### Incidental finding — `motivic-perpetual-obstruction` is the real reason main is red

Not this bean; filed separately. `lifting-and-descent/motivic-perpetual-obstruction.ts`
calls `theorem()` with label `conj:motivic-perpetual-obstruction`. The schema
requires `thm:` for `theorem()`, so the **block fails to import**, its label
never registers, and every consumer of `conj:motivic-perpetual-obstruction`
goes unresolved — 7 of main's 10 remaining `✗`. Introduced by
`1d3988bc31 docs(motivic): rewire 15 downstream blocks — conjecture → theorem`,
which promoted the builder and left the label behind. Both Lean files
(`MotivicPerpetualObstruction.lean`, `MotivicPerpetualObstructionFromTrace.lean`)
are **sorry-free**, so the promotion is mathematically justified and the fix is
to finish the rename, not revert it: 9 label sites across 7 authored files.
