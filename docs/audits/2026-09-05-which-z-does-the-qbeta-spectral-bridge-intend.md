# Which `z` does `prop:q-beta-spectral-bridge` intend?

**Bean:** `qou-i229`, feeding `qou-cds1`. **Date:** 2026-09-05.
**Probe:** `the_qbeta_bridge_table_and_its_witness_compute_different_z_probe.py` (6/6).

## Answer: **D**, `z = q³/(q²+1)`. It is an owner ruling, not a judgement call.

The two values are not rival readings of one definition. They are the corpus's
two *registered trace conventions*, and one of them has been excised.

| | `z` | `z(q₀)` | registry status |
|---|---|---|---|
| **C** | `1/(q^{1/2}+q^{-1/2})` | `0.49932033418…` | **EXCISED 2026-08-09** |
| **D** | `q³/(q²+1)` | `0.61268803714…` | **PRODUCTION** |

`rem:markov-z-reconciliation` names it outright: *"The parameter
`z_m = 1/(q^{1/2}+q^{-1/2}) = √q/(1+q)` is **convention C** … The **mass** and
**binding** channels are registered as **convention D**, `z_D = q³/(q²+1)`, in
both their definitional and production layers, following the owner ruling of
2026-08-09 that excised convention C for those channels."*

And for this channel specifically, `docs/coordination/trace-convention-registry.md`:

> `qbeta-decay` — definitional **D**, owner ruling 2026-08-15 *("convention D is
> convention. excise convention C")*; and **C is now structurally excluded**.
> Production **C**. Status **agreed-migration-pending** (bean `qou-cds1`).

**So the proposition states the excised convention.** The published table follows
it faithfully; the producer already computes D. The question has an answer on
the books, and what is missing is execution.

## 🛑 This retracts what I said last turn

I wrote that *"for once the compute has drifted from the stated definition rather
than content lagging compute"*. **Backwards.** The compute migrated to the ruled
convention and the proposition was left behind — the ordinary C→D content lag
that `qou-5pgl` exists for. I reached the wrong conclusion by treating the
proposition as the definition of record without checking whether its convention
was still current, which is the exact question the registry exists to answer.

Worth noting the producer is in fact *ahead* of the registry's own row: that row
still lists production as **C** for this channel, citing
`qbeta_utils.markov_parameter`, `qbeta_ck_sseries_exact_rational` and
`ZBarParity.lean`. `q_beta_spectral_bridge_witness.py` is not among them and has
already moved to D.

## There is a structural argument too, not only the ruling

The reconciliation block gives one, and it involves no anchor and no ppm figure.
In convention D the two crossing loop values satisfy

```
z₋ = 1/(q(q²+1)),    z·z₋ = 1/[2]_q²,    a² = z/z₋ = q⁴
```

so they multiply to the inverse square of the quantum dimension and the Ocneanu
framing parameter is the **monomial** `a = q²` — which is what makes D the
`sl₂` point. Convention C satisfies neither: its `z₋` mixes half-integer and
integer powers of `q` in one unfactorable numerator, with no monomial framing
ratio. Both are admissible traces (`tr_M(1) = 1` in each); the block's own
phrase is that this is *"not convention C being invalid; it is convention C
being structureless."*

## Options

### A — migrate the proposition and its table to D ✅ recommended, with a caveat on scope

**For.** It executes a ruling already made rather than making a new one. It
removes an excised convention from a *definitional* block. It closes the 21 %
divergence between the table and its producer. And the structural argument above
means it is not merely a preference.

**Against.** The `𝔔_β` MeV figures move by ~0.05 MeV, and those are compared
against experiment, so the migration has a visible consequence that wants
checking rather than assuming. More importantly, this block is one part of a
scoped migration (`qou-cds1`, "re-derive the qbeta `c_k` ladder under D"):
migrating it alone leaves the channel half-migrated, the registry row still
wrong, and the three named production files still on C.

### B — revert the producer to C

**For.** Restores agreement immediately, and matches the registry's stated
production status for the channel.

**Against.** It reinstates a convention excised by owner ruling — a regression,
not a fix. It contradicts the structural argument. And it would have to be
re-reverted when `qou-cds1` lands, so it buys agreement at the cost of doing the
work twice.

### C — leave both, document only

**For.** No risk of pre-empting `qou-cds1`. The divergence is now documented and
the block's false provenance sentence corrected, so nothing is hidden.

**Against.** It leaves a 21 % disagreement between a published table and the
producer it cites, and an excised convention in a definitional block.

## Recommendation

**A, executed inside `qou-cds1` rather than as a one-off** — the ruling is made,
the migration is scoped, and this block is one of its members.

**The safe step available now is C-plus-labelling:** state in the proposition
that its `z` is convention C, that D is the ruled convention, and that the
migration is tracked. That is precedent in this corpus — `df13e845cee` did
exactly this for the `q₀` pins ("*label the pins honestly*"), deliberately
labelling rather than recomputing, and it is what let today's sweep identify
those figures at all. **Labelling an out-of-date convention is cheap, reversible
and loses nothing; migrating one block of a tracked multi-block migration is
none of those.**

## One thing rides along and should be settled in the same pass

The **pin** differs too: the producer is on the proton anchor, the table on the
muon pin A. That is a separate axis from the convention and neither implies the
other — but a migration pass that fixes `z` and leaves the pin straddling would
produce a table that is right in convention and wrong in anchor. `qou-i229`
holds the pin half.
