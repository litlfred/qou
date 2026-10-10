---
# qou-xwet
title: canonical-mass-table-extended.witness.json is CLOBBERED by low_isotope_mass_table.py -- and B_2H_AME_MeV is pinned POSITIONALLY over the shifting row set
status: completed
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T22:43:14Z
updated_at: 2026-10-04T15:15:36Z
---

Found 2026-08-15 on the post-merge reorientation pass (PR #4961 landed; this was
surfaced while diagnosing the raw-float64 ratchet's second REGRESSED entry,
`canonical-mass-table-extended` 24 -> 26).

## Two producers, one fixed output path

`canonical_mass_table_extended.py` writes to a **fixed** filename -- its own
docstring says so (lines 33-34: "The witness output filename is fixed by
WitnessBuilder (`canonical-mass-table-extended.witness.json`)"). Its
`DEFAULT_ATOMS` covers nine nuclides, p through 7Li.

`low_isotope_mass_table.py::run_canonical()` **invokes that producer as a
subprocess** with a restricted atom set:

    cmd = [sys.executable, "-u", HERE/"canonical_mass_table_extended.py",
           "--atoms", ",".join(LOW_ISOTOPE_ATOMS),   # p,n,D,T,3He
           ...]

Because the output path is fixed and ignores `--atoms`, that subprocess
**overwrites the canonical witness with a five-row table**. The wrapper then
reads it back, projects A <= 3 (now the whole file), writes its own
`low-isotope-mass-table.witness.json`, and leaves the truncated canonical
witness on disk. Whoever runs the low-isotope table last wins.

That is what commit `204c5c4e38` committed (and `708ce844cf` before it). Neither
commit body mentions the canonical table; both are about the low-isotope one.
The canonical table silently lost 4He, 5Li, 6Li and 7Li.

## The consequence: a positional pin over a row set another producer rewrites

`content/values/registry.ts:607-616` pins

    B_2H_AME_MeV   "AME experimental binding energy of deuterium (2H)"
    witnessFile:   computations/canonical-mass-table-extended.witness.json
    witnessPath:   data.rows.2.B_AME_MeV        <-- POSITIONAL

`canonical_mass_table_extended.py:94-110` already knows this is fragile and says
so ("Do NOT reorder this list without also updating content/values/registry.ts
... A (Z, N)-keyed lookup would be more robust; tracked as a follow-up"). The
comment guards against *reordering the list*. It does not guard against a second
producer rewriting the row set.

Measured, per committed version of the witness:

    sha         date        nrows  rows[2]        B_AME_MeV
    d27b002745  2026-06-15    5    Z1 N1 A2  D    2.22456589   correct
    defd22787d  2026-06-22    7    Z2 N1 A3  3He  7.71804132   WRONG NUCLIDE
    0a7913c432  2026-06-29    7    Z2 N1 A3  3He  7.71804132   WRONG NUCLIDE
    b8eb7d9e66  2026-07-18    7    Z2 N1 A3  3He  7.71804132   WRONG NUCLIDE
    2d2502f4d1  2026-08-09    7    Z2 N1 A3  3He  7.71804132   WRONG NUCLIDE
    b7430e1b88  2026-08-15    7    Z2 N1 A3  3He  7.71804132   WRONG NUCLIDE
    1af7d4b7a0  2026-08-15    7    Z2 N1 A3  3He  7.71804132   WRONG NUCLIDE
    708ce844cf  2026-08-15    5    Z1 N1 A2  D    2.2245662    correct (by accident)
    204c5c4e38  2026-08-15    5    Z1 N1 A2  D    2.2245662    correct (by accident)

For eight weeks `B_2H_AME_MeV` resolved to **3He's** binding energy, 3.47x the
deuteron's, under a description naming deuterium. It was restored **by the
clobber**, not by a fix -- the p and n rows returning at indices 0 and 1 pushed
the deuteron back to index 2.

## Honest severity

**Nothing rendered wrong.** `B_2H_AME_MeV` is registered but has **zero**
consumers: grep across `content/` finds it only in `registry.ts` itself. So this
was a wrong number *available* to render, never one that reached the paper. Say
it that way -- do not upgrade it to "the paper carried a wrong deuteron binding
energy for two months", which is not what happened.

What IS live is the mechanism, and it is entirely unguarded: a positional
witness pin over a row set that a *different* producer silently rewrites, with
no ordering assertion anywhere and no consumer to notice. The current state is
also materially worse than the comment describes -- the canonical table is
missing 4He and every A >= 5 row it claims to cover.

## What a fix looks like

1. **Key the pin by nuclide, not position.** `registry.ts` should select the row
   with `Z == 1 && N == 1`, or the producer should emit a `rows_by_nuclide`
   map. The producer's own comment already proposes this and calls it "more
   robust"; it is now load-bearing rather than cosmetic.
2. **Stop the clobber.** `low_isotope_mass_table.py` must not drive the canonical
   producer through a shared fixed output path. Either give the canonical
   producer a `--witness-name` / output-path argument so the low-isotope run
   writes elsewhere, or have the wrapper snapshot-and-restore the canonical
   witness, or drop the subprocess call and project from the committed witness.
3. **Assert the invariant.** The producer declares a row order in a comment;
   make it an assertion at emit time so a restricted `--atoms` run cannot
   silently ship as the canonical table.
4. **Regenerate the canonical witness at full DEFAULT_ATOMS** so 4He and the
   A >= 5 rows come back. Cheap: the committed run records durationMs 597.

## Do not conflate with the neighbours

- `qou-7loj` is a *different* defect in the same file (nucleon rows sourced from
  the deprecated Vol/rho witness, +2.89%). Note the current p row reads
  938.2720894 with err_ppb -0.0029, i.e. CODATA-matching -- so 7loj's specific
  +2.89% symptom is NOT present at HEAD and that bean may itself want re-checking.
  Not closed here: verifying the whole chain is its own job.
- `qou-5h7z` is about `low-isotope-mass-table.witness.json` being a
  pre-convention-D artifact. Different file, different problem.
- The raw-float64 24 -> 26 that led me here is a *symptom*: the five surviving
  rows all have populated err fields (5 rows x 5 fields + 1 floor = 26) whereas
  the seven-row version had nulls in the A >= 5 rows. Draining the f64 without
  fixing the row set would paper over this.


## Consumer-side guard LANDED (2026-08-15), plus a second dead pin it found

 — nothing validated ANY of the
69 witness pins in registry.ts before this; `witnessPath` appeared nowhere in the
repo outside registry.ts itself. Checks: E-missing-file, E-unresolvable,
E-null-value, E-nuclide-drift, W-positional. Self-test replays the incident (3He
at index 2 -> drift detected; current D at index 2 -> clean).

Live result: 68 pins parsed, 1 positional (B_2H_AME_MeV, nuclide identity
currently CORRECT), 1 error.

### The error is a SECOND dead pin, unrelated to the clobber

    rho_q -> derived_50_digit.rho_q  in  q-pinning-50-digit.witness.json

That key does not exist. `derived_50_digit` holds H_A, hbar_q, hbar_q_sq, q,
q_inv, s_skein, two_q, z_markov — no rho_q, and the string 'rho' appears nowhere
in the file. The entry is a normal live entry (sits beside z_markov), not a
needsReview stub.

The ONLY witness in the tree that defines "rho_q" is
`computations/_deprecated/brane-tower-finite-laurent.witness.json`.

**Not repointed, deliberately.** Aiming a live pin at a deprecated witness would
be worse than leaving it dead, and 'Hecke trace density rho_q' does not by itself
say WHICH rho is meant — the notation register warns that rho is overloaded
(rho_K, rho_F, per-block density, and varrho the vortex). Picking one would be a
guess wearing a pin. Owner call: delete the entry, or point it at a live producer
once one emits the intended quantity.

### Severity, stated honestly for both

Neither B_2H_AME_MeV nor rho_q is consumed by a `:val[...]` directive anywhere in
content/ — grep confirms zero. So neither has ever rendered: the eight-week 3He
substitution and this dead pin were both latent. The validator's value is that it
now catches them, and would catch the day someone starts using one.

### Still open on this bean

  1. regenerate canonical-mass-table-extended at full DEFAULT_ATOMS (needs
     pyhecke_native; absent in the sandbox that found this)
  2. repoint B_2H_AME_MeV from data.rows.2 to a nuclide key (needs 1 first, since
     the key does not exist in the committed witness yet)
  3. resolve or delete the rho_q pin (owner call)
  4. wire the validator into scripts/precision-gates.sh or an equivalent preflight


## CORE FIX COMPLETE (2026-08-15, PR #5165)

All four items closed except the rho_q owner call.

  1. DONE  canonical witness regenerated at full DEFAULT_ATOMS -- 5 -> 9 rows,
           4He / 5Li / 6Li / 7Li restored. And my 'needs a provisioned run'
           claim was WRONG TWICE: compute-author §0.1 says do not declare a
           compute blocked on pyhecke_native (pip install ./tools/pyhecke-native
           -> 0.9.0 in ~1 min, matching the committed witness), and the full
           9-atom run takes ~5 SECONDS wall, not 45 minutes. Provisioned first
           per the §0.1 STRICT note, so the environment block came through
           byte-identical -- zero provenance stripped.
  2. DONE  B_2H_AME_MeV repointed to data.rows_by_nuclide.D.B_AME_MeV. Producer
           emits a nuclide-keyed view (scalars only -- mirroring whole records
           doubled the file 68 -> 133 KB; the projection costs 8 KB). registry.ts
           now has ZERO positional pins.
  3. OPEN  rho_q -- owner call, unchanged. Only _deprecated/ defines it.
  4. BLOCKED on 3: wiring the validator into precision-gates.sh would make the
           gate red for a defect I cannot resolve.

BONUS, not on the original bean: the file was drained 24 -> 0 raw float64 at the
producer. This HAD to ride here rather than land after -- restoring rows would
otherwise have pushed it 26 -> 34, i.e. the correctness fix would have deepened
a red. Causes were three float() downcasts (B_AME table, CODATA reference,
derived err_* columns) plus paper_hard_floor_ppb as 780.0 rather than 780. The
err columns now carry float + _str twins per the qou-ftuv shadow rule. Ratchet
regressions 2 -> 1; only rho-k remains.

Validator extended to check nuclide identity on KEYED pins too, not only
positional ones -- otherwise it would verify nothing once this migration
finished. Negative control reproduces the historical bug verbatim.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: 74e7bdb5cc "record the completed fix"; 5 main commits
