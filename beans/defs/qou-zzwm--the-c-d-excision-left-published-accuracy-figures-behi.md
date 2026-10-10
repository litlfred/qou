
## 2026-10-10 — THE LABELLING FIX HAS ITSELF GONE STALE, and the stale label now says something FALSE about three published rows. FIXED.

Re-audit of the C→D migration tracker (session epic `qou-am5t`). The labelling
half landed in PR #6156 and is intact on `main` — `convention_frame_qbeta` is
there, `grep -c convention` on the L2 witness is **11** (was 0). What has
happened since is the thing this bean is *about*, one level up.

### The defect

On **2026-09-12** the Q_β / m_n / Δ_pn rows were re-scored onto the base the
owner ruled on 2026-09-08: `ε` = the Markov trace at `z_D = q³/(q²+1)`.
`per_observable_100x_status.py` does this at the `Q_pred` assignment —
`Q_pred = _ruled["_pred"]` whenever the calibration holds, and it holds. So the
published value is built **at `z_D`, which is the canonical convention**.

The convention note was not re-gated. It fires on

```python
if qbeta_convention.get("status") == "INHERITED_C":
```

and `qbeta_convention` describes **`qbeta-ck-cache.witness.json`**, not the
value the row scores. The committed witness therefore carried both notes
appended, contradicting each other inside one string:

> "INHERITS THE Q_beta CONVENTION FRAME: … the Q_beta term **was built in
> Markov convention C** … **Not reproducible under the canonical convention**"
> … "INHERITS THE RULED Q_beta BASE: … the Q_beta term **is now**
> `|tr_M(Delta_S)(z_D)|*E0` at `z_D = q^3/(q^2+1)`"

The second is current. The first is superseded and **both of its operative
clauses are false of the published row**: the value was built in D, and it is
reproducible under D — it is what the producer computes.

### Why it could never have self-cleared

The function's own docstring promises it would:

> *"Returns None when neither scope applies, so a future state in which the
> ladder is re-derived under D on an admissible functional silently drops the
> note rather than leaving a stale one."*

That promise rests on `status` eventually ceasing to be `INHERITED_C`. It
cannot. The cache is a convention-C artifact **by construction**, and
`qbeta_ck_cache.py` raises `SystemExit(2)` under D — by design, bean
`qou-ckwt` — so nothing will ever rewrite it in D and the status is pinned
forever. **The auto-drop mechanism was unreachable from the day it was
written.** That is a sharper failure than a stale number: a guard whose
author documented the right intent and keyed it on a condition that cannot
change.

### The fix, at all three sites

Gate on the **provenance of the scored value**, not on the convention of a
file the value may no longer touch — the same condition that already selects
`Q_pred`:

| site | what it emitted | now |
|---|---|---|
| `_inherited_qbeta_scope()` (m_n, Δ_pn rows) | both notes, contradictory | RULED-base note only |
| the `Q_β` row's `_conv_note` | "⚠ CONVENTION FRAME: this prediction was built in Markov convention C … UNREPRODUCIBLE under the canonical convention" | suppressed |
| the witness-level `w.add_caveat` | the same claim over all three rows | suppressed |

And `convention_frame_qbeta` now says, in the block itself, what it is about —
because read bare it still looks like a caveat on the dashboard:

```
describes                        qbeta-ck-cache.witness.json (the c_k ladder cache)
scored_rows_consume_this_cache   False
scored_rows_note                 "…built at z_D = q^3/(q^2+1) -- the canonical
                                  convention -- … They do NOT consume this C cache,
                                  so this block records the cache's frame and is
                                  NOT a caveat on those rows. What IS open is that
                                  no c_k ladder exists on an admissible base
                                  (qou-cds1)…"
```

**What is NOT weakened.** The genuinely open fact — *no `c_k` ladder exists on
an admissible base* — is stated in full by the RULED-base note and by
`qbeta_ruled_base.ladder_on_admissible_base_exists`, and `qou-cds1` is still
cited from both. Nothing about the openness is dropped; only the false claim
about which convention built the number.

### Verification: re-ran the producer, ZERO numeric fields changed

`PYTHONPATH=computations python3 -u computations/per_observable_100x_status.py`
→ **exit 0**. Headline table byte-identical: **1 / 6 SCOREABLE**, `Q_beta`
`1.668e+8` ppb / `2.139e+7×`, `m_n` `1.389e+5` / `2.718e+7×`, `Δ_pn`
`1.009e+8` / `2.327e+7×`, `m_mu` `211.2` / `970.2×`, `m_K/m_pi` `51.48` /
`0.1952×` ✓. Semantic diff of the witness (volatile keys masked) is **five
entries and all five are prose**: `caveats[0]` removed, three new
`convention_frame_qbeta` fields, and the two row notes losing their C half —
plus one trailing-space change on `rows[2]/source_witness`.

### Observed in passing, NOT mine and NOT committed

The `precision-gates.sh` preflight dirtied three audit witnesses. Two were
volatile-only. The third is a real measurement change and is recorded here
rather than buried in my commit: **`mpf-mixed-arithmetic-audit` reads
`candidates 7 → 5`, `files 4 → 3`**, dropping
`computations/binding_rotation_phase_lead.py` (2 candidates). Someone drained
those between that witness's last commit and today's tree. All three were
restored with `git checkout --` so this commit stays on its subject; whoever
owns that audit should re-run it and commit the drain on purpose.

Also: `qa-sweep` writes `test/attestations/block-qa/` into the working tree.
Removed, not committed — the derived QA corpus lives on the cat-harness
`qa-reports` branch by the owner ruling of 2026-10-04.

### Status

Staying `todo`, and the `needs-owner` tag still applies — the owner call this
bean names (re-derive the ladder under D, or keep publishing the ruled base
unladdered) is untouched and is `qou-cds1`. What is closed is the labelling
defect, now twice: once in #6156 and once here, after the thing it labels
moved underneath it.

**The lesson is this bean's own, applied to itself.** Its METHOD NOTE says
*"the single most load-bearing C artifact in the repo was invisible to the
value-based detector"*. The sequel: **a label is not a fix, it is a second
artifact that can go stale** — and this one went stale in the direction that
makes the corpus look worse than it is, by asserting three published rows are
unreproducible under the convention they are actually computed in.
