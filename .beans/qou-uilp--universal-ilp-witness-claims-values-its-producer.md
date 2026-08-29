---
# qou-uilp
title: universal-ilp.witness.json claims bond_HH/bond_CC that its producer cannot compute (NameError)
status: completed
type: bug
priority: normal
created_at: 2026-08-28T00:00:00Z
updated_at: 2026-08-28T20:20:23Z
---

Found running two "GAP: broken producer" beans to see whether their claims held.
Both did; this one turned out to be more than a broken run.

## The producer dies before it computes what its witness reports

`computations/universal-ilp.py` calls `apply_atom_nf` at **:191** and **:202**:

    def apply_second_H(nf):
        return apply_atom_nf(nf, 1, 0)     # LEVEL 4  — H₂ bond
    def apply_second_C(nf):
        return apply_atom_nf(nf, 6, 6)     # LEVEL 4b — C-C bond

Run it:

    NameError: name 'apply_atom_nf' is not defined. Did you mean: 'build_atom_nf'?

**It is not a typo for `build_atom_nf`.** That function exists (in
`tools/pyhecke/python/pyhecke/gram.py:994`) and takes **two** arguments
(`Z, N`); `apply_atom_nf` is called with **three** (`nf, Z, N`). Different
signature, different job — applying a second atom to an existing normal form
rather than building one. `git log -S'def apply_atom_nf'` finds **no commit
that ever defined it**, in this file or anywhere. It was never written.

So LEVEL 4 and LEVEL 4b are unimplemented, and the script aborts at the first
of them.

## But the committed witness reports both

`computations/universal-ilp.witness.json` carries:

    data.bond_HH = {"operator": "σ₁⁻¹", "crossings": 1, "tr_M": 0.43636377565005485}
    data.bond_CC = {"operator": "σ₁⁻¹", "crossings": 1, "tr_M": 2447.0123149137858}

`results['bond_HH']` is assigned on the line *after* the call that raises, so
no run of the current producer can produce either. `computedAt` is
**2026-04-14**, four and a half months ago.

This is stronger than staleness. A stale witness is one a re-run would change;
this is one a re-run **cannot** produce at all.

## Why nothing caught it

`scriptFile: null`, `scriptHash: null` — a **bare producer**, so every
provenance-keyed audit skips it. It is one of the 45 unattributed witnesses
measured under `1j39` (169 unstamped-but-resolvable, of which 124 across 120
producers are portable and 45 have no producer named). Those 45 were flagged
there as "the harder half"; this is what one of them looks like from the inside.

It is also **listed in `raw-float64-baseline.json`** — its two `tr_M` floats are
accepted as known-dirty — so the float64 ratchet does not flag it either.

## Severity, stated accurately — I over-read it first

A grep for consumers returned six files, and I nearly wrote that unreproducible
values "feed three live producers". **That was wrong.** All three Python hits
are prose:

- `klr_canonical_basis_filter.py:77` — a comment listing candidate scripts
- `binding_qhamiltonian_rotational_scale.py:12` — a docstring mention
- `r5_full_canonical_knot_solver.py:880` — the script name inside a string

and two of the three content hits cite the *definition label*, not the data.
**No code reads `bond_HH` or `bond_CC`.**

The one real dependency is
[`nuclear-interactions/universal-ilp-algorithm.ts`](../content/quantum-observable-universe/nuclear-interactions/universal-ilp-algorithm.ts):

    script:  "computations/universal-ilp.py",
    witness: "computations/universal-ilp.witness.json",

So `def:universal-ilp-algorithm` declares as its computational backing a witness
whose producer cannot regenerate it. That is a break in the paper's own audit
chain — real, and narrower than a numerical dependency.

## What to do — NOT decided here

Three routes, and picking between them needs someone who knows whether the
H₂/C-C bond levels are wanted:

1. **Implement `apply_atom_nf`.** The honest fix if those levels are still
   intended. It is real unimplemented math (apply a second atom to an existing
   NF), not a repair.
2. **Excise LEVEL 4/4b** from the producer and regenerate the witness without
   `bond_HH`/`bond_CC`. Honest if the levels were abandoned — but it deletes two
   recorded values, and they may be the only surviving record of a computation
   someone did in April.
3. **Mark the witness historical** and drop the `computation.witness` link from
   the content block, so the block does not claim reproducible backing it lacks.

Not attempting any of them: (1) is unimplemented math, (2) destroys data, and
(3) changes what a definition block claims. All three are author calls.

**Do not "fix" this by regenerating the witness.** The regeneration fails, and
a partial witness written from a failed run would be worse than the current
state — it would look fresh.


---

## RESOLVED 2026-08-28 — route 3, narrowed on measurement (PR #5923)

Took route 3 ("mark historical"), but **not** its literal wording. The bean
said to drop the `computation.witness` link. Re-reading the block, the false
claim is in **`status: "verified"`**, not in the link: `universal-ilp.witness.json`
genuinely IS the artifact the block refers to, and it is the only surviving
record of the April computation. Dropping the pointer would destroy the trail
to the data without removing any false claim.

So:

  * `content/.../universal-ilp-algorithm.ts`: `status: "verified"` to `"error"`,
    reason inline; `witness:` link KEPT.
  * `computations/universal-ilp.py`: header stating LEVEL 4/4b are unimplemented
    (`apply_atom_nf` never defined anywhere), that the run aborts before the
    witness write, that the committed witness is a HISTORICAL RECORD, and that
    re-running to "refresh" it is forbidden — a partial run would read as fresh
    while being less complete than what is committed.

Re-verified the producer's failure on a live run before editing anything:
`NameError: name 'apply_atom_nf' is not defined` at :191, raised before
`results['bond_HH']` is assigned. `run-validate.ts` exit 0.

Routes 1 (implement `apply_atom_nf` — real unimplemented math) and 2 (excise
Levels 4/4b and regenerate without the bond values) remain **author calls** and
are untouched. Nothing here forecloses either.


**Count correction (same PR).** The "Why nothing caught it" section above cites
`1j39`'s "169 unstamped-but-resolvable, 124 portable, 45 unattributed". The
**124 portable** half of that is wrong — see `1j39`; 62 of those 120 producers
already use `WitnessBuilder` and are fixed by a re-run, not by porting. This
witness's own classification is unaffected: it names no producer at all, so it
sits in the unnamed bucket either way, and no re-run can help it.
