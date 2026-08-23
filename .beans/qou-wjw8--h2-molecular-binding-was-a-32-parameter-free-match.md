---
# qou-wjw8
title: H2 molecular binding was a +3.2% parameter-free match under convention C; under D it is -80.7%
status: todo
type: task
priority: normal
created_at: 2026-08-23T16:42:54Z
updated_at: 2026-08-23T16:42:54Z
---

MEASURED 2026-08-23 while triaging `qou-bm4i` (blocks marked `verified` whose
witness failed). This one is not a stale witness and not a wrong number in a
block — it is a **convention-frame casualty**, and it belongs with the other
convention-D re-derivation items (`qou-cds1`, `qou-102c`).

## The measurement

`prop:h2-lp-dual-binding` predicts the H₂ dissociation energy with **no fitted
parameters** — `ΔΦ₁ × E_hartree / [2]_q²`, where `E_hartree = m_e·α²`.

    convention C   4.6231 eV   vs observed D₀(H₂) = 4.478 eV    **+3.2 %**
    convention D   0.8645 eV   vs observed D₀(H₂) = 4.478 eV    **-80.7 %**

A factor of **5.35**.

## It is the convention, not the pin and not the producer

Diffing the witness parameters across the 2026-08-21 migration
(`52c68267f2` -> `e5d44bfb17`), exactly one input moves by more than ppb:

    z          0.49932033403356124  ->  0.6126880371464652     <-- C to D
    q          1.1099785955573347   ->  1.1099785827513808     (muon->proton, 11.5 ppb)
    alpha_EM, E_hartree_eV, HA, TWO_Q, E_mol_scale_eV          (all ppb)

and `0.499320334…` / `0.612688037…` are exactly `√q/(q+1)` and `q³/(q²+1)` —
the two values AGENTS.md quotes verbatim for C and D. The producer is
**byte-identical** across the migration (`git diff` on
`h2-molecular-binding.py` is empty), and the 11.5 ppb pin change cannot move an
observable by 5.35×.

Reproducible: a fresh run gives `0.864536457714344` byte-for-byte, and the
producer prints `Error = -80.7%` in its own summary.

## What this is and is NOT

It is **NOT** an argument against the 2026-08-15 ruling. D is canonical; that is
settled and not reopened here.

It IS the same situation AGENTS.md already records for the Q_β `c_k` ladder:
*"The values above are correct for C and are kept as recorded — they need
scoping, not correction. The ladder must be RE-DERIVED under D."* H₂ binding is
another C-frame result in exactly that position, and as far as I can find it is
not yet on any convention-D tranche list.

What makes it worth its own item: the `c_k` ladder is an internal precision
ladder, while this is a **direct comparison to an experimental number with no
fitted parameters**. A parameter-free 3 % match to D₀(H₂) is the kind of result
a referee would look at first, and right now the corpus contains a producer that
prints `-80.7%` while the block that cites it says nothing about the frame.

## State

* Block `status` is `failed` (set in `cd19e98ac8`) — correct, leave it.
* Witness untouched; my re-run was byte-identical and I reverted the provenance
  drift.
* The block's own claims — binding is positive, interleaved ordering optimal —
  both still PASS under D. Only the magnitude is frame-dependent.

## Next

1. Re-derive the H₂ `Φ₁` construction under `z = q³/(q²+1)` and see whether the
   5.35× is recoverable, or whether the C-frame agreement was coincidental.
2. Either way, the `.md` needs a convention-frame note like the one added to
   `rem:q-beta-c3-continuum-geometry` — a reader currently has no way to know
   the quoted physics is frame-dependent.
3. Worth a sweep: how many other observables compare against experiment through
   `z`? This one was found only because its assertion happened to be a pass/fail
   gate against a measured value.
