---
# qou-49ug
title: diproton/dineutron chi have no real producer — they are absent from the shared ATOMS registry
status: completed
type: task
priority: normal
created_at: 2026-08-16T02:44:33Z
updated_at: 2026-08-16T03:43:16Z
---


## Diagnosis — there is no mathematical obstruction, just a missing registry row

`chi-diproton-h6-at-q0-50dps.witness.json` and its dineutron twin are the last
producerless χ atoms. Their `scriptFile` currently names
`computations/regenerate_chi_atom_conventionD.py` — a **one-shot migration
script I wrote**, not a producer. It re-derived them *in place* from the file's
own `chi_lambda` values (sound, because χ is a character and carries no
convention), but that is a migration, not a derivation from the braid.

**Why they are producerless.** Both χ producers —
`chi_at_q0_via_hoefsmit_mpfr` (line 51) and `chi_at_q0_via_matrix_m_mpfr`
(line 81) — import the *same* registry, `per_irrep_pole_atom.ATOMS`, a plain
`name → (Z, N)` dict of 11 entries. `diproton` and `dineutron` are simply not
in it.

**Nothing else blocks them.** Measured, not assumed — the parabolic split the
matrix-M trace identity requires works for both, identically to the deuteron:

```
diproton   Z=2 N=0:  n=6  |left|=11  bridge=1  |right|=11   SPLITS ok
dineutron  Z=0 N=2:  n=6  |left|=11  bridge=1  |right|=11   SPLITS ok
deuteron   Z=1 N=1:  n=6  |left|=11  bridge=1  |right|=11   SPLITS ok
```

One σ₃ bridge each, which is exactly the precondition `_split_atom_braid`
enforces. The A=1 refusal that blocks proton/neutron does not apply — these are
A=2.

## How to attack

1. **Add two rows** to `per_irrep_pole_atom.ATOMS`: `"diproton": (2, 0)` and
   `"dineutron": (0, 2)`. Both producers pick them up from the shared registry;
   no producer code changes.
2. **Run `chi_at_q0_via_hoefsmit_mpfr`** for the two. That producer owns the
   `chi-{atom}-h6-at-q0-50dps.witness.json` filenames the existing witnesses
   already use, so it takes over `scriptFile` from my migration script and the
   orphan count drops.
3. **Use it as a cross-check, which is the real prize.** The hoefsmit run
   recomputes χ from the braid word, independently of the values my migration
   copied forward. If they agree, my in-place re-derivation is confirmed. If
   they disagree, the migration was wrong and two witnesses in the corpus are
   bad — a genuinely useful negative either way.

## The one thing to check FIRST

`ATOMS` is iterated by other consumers (mass tables, binding sweeps, Δ_λ
feeds). Diproton and dineutron are **unbound** systems — adding them to a
shared registry may silently pull them into sweeps that assume every entry is a
bound nucleus, and produce nonsense rows that look like predictions. Grep the
consumers of `ATOMS` before adding, and if any sweep iterates it wholesale,
prefer a separate `UNBOUND_CHANNELS` dict that the two χ producers merge in,
rather than widening `ATOMS` itself.
