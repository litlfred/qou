---
# qou-g94g
title: 'per_irrep_pole_atom_crystal: pole_u off by exactly one at the first atom'
status: todo
type: bug
created_at: 2026-09-06T10:15:38Z
updated_at: 2026-09-06T10:15:38Z
---

Surfaced by the qou-hu1f regeneration pass. Pre-existing: fails identically under both intra orderings.

## Measured

    proton (Z=1, N=0, n=3, |word|=11, |partitions|=3)
      ord_min  = -18    (λ_min = (2,1))
      pole_u   = 18     expected = 19     MISMATCH

**Off by exactly one, at the very first atom**, and the probe stops there
(`--continue-on-mismatch` overrides). An off-by-one at the first case usually
means an index convention rather than a numerical drift, which is worth
checking before anything more expensive.

## NOT the intra-ordering ruling

`asserted_atoms_match_closed_form_shift` fails **identically under grouped and
borromean**. Established at assertion level, because a witness-environment gate
fires under both orderings and masks the exit code.

## Also carried by this producer

  * `⚠ raw-float64: 4 fields` — `.assertions[0].{computed,expected,tolerance}`
    and `.data.atoms[0].elapsed_sec`.
  * `⚠ environment: downgraded python 3.12.3 → 3.11.15` in this container. The
    witness on disk was produced under 3.12.3; regenerating here would weaken
    its provenance record, so it was NOT committed by the pass that found this.

- [ ] Check the `pole_u` vs `ord_min` index convention before assuming a
      numerical cause — `18` against an expected `19` on the first atom.
- [ ] Drain the 4 raw-float64 witness fields.