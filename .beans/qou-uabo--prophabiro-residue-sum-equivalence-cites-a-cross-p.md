---
# qou-uabo
title: prop:habiro-residue-sum-equivalence cites a cross-pipeline witness that does not exist
status: todo
type: task
created_at: 2026-08-15T23:12:20Z
updated_at: 2026-08-15T23:12:20Z
---


## What

Found as one of the three genuine orphans in `qou-a28x` — blocks quoting
high-precision values that appear in no witness anywhere.

`prop:habiro-residue-sum-equivalence` presents a cross-pipeline agreement table:

| Atom | Polynomial path | Residue path | \|rel diff\| |
|---|---|---|---|
| p (proton) | 2.1225825095 | 2.1225825095 | 0 |
| n (neutron) | 1.5893934460 | 1.5893934460 | 2.79e-16 |
| D (deuteron) | 0.1774369242 | 0.1774369242 | 0 |

with the prose:

> The cross-pipeline **witness** records, per atom, the relative difference
> between the two paths. The current run achieves: […] All differences fall
> within the relative tolerance `1e-9` — the two paths agree to machine
> epsilon. **This is direct empirical evidence for the analytic identity.**

Three problems, in increasing order of seriousness.

1. **The witness it cites is not named.** The `.ts` sidecar has no
   `computation` field at all — no script, no witness — while carrying the tag
   `computational-witness`.
2. **No live producer emits any of the three values.** The only source in the
   repo is `computations/_deprecated/build_markov_trace_assembly_chain.py`,
   whose comment reads *"50 dps gives 2.12258250945273... matching the
   upstream"*. The producer behind "the current run" has been deprecated; the
   numbers outlived it.
3. **The nearest live value is 95x outside the block's own tolerance.**
   `hecke/hecke-character-symbolic.witness.json` has
   `/results/p_total/at_q0 = 2.1225823066876800474...` against the block's
   `2.1225825095`:

       |d| = 2.028e-7      rel = 9.555e-8
       block asserts its two paths agree within 1e-9
       the gap is 95.5x that tolerance

   That is not proof the block is wrong — `p_total` may not be the same
   quantity as the polynomial path — but a proposition whose whole content is
   *"these two numbers agree to machine epsilon"* cannot be checked at all
   while the run that produced them is gone.

## What I deliberately did NOT do

**Declare `hecke-character-symbolic` on the block.** It is a different
computation (q-deformed Hecke characters via Hoefsmit seminormal matrices), and
attaching it because a nearby decimal matches would be exactly the false
attribution `qou-a28x`'s `--suggest` output warns about: a witness containing a
similar number is not the witness a block means.

## Next

1. Establish whether the polynomial path and residue path still exist as live
   producers under any name. If they do, re-run and re-record — the agreement
   claim is then checkable again.
2. If they do not, the table is an undated empirical claim from a deprecated
   pipeline and should say so, or be withdrawn.
3. Either way the block needs a `computation` block; the
   `computational-witness` tag currently promises one that is not there.

Related: `qou-a28x` (the axis and triage), `qou-ft3p` (the same shape — a cited
reproducer that emitted no witness).
