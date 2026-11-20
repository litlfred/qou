---
# qou-cdh4
title: 'H4 (hygiene): convention-label hygiene — history must say it is history'
status: todo
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-10v9
---

Parent: `qou-cdx1`.

## Scope (measured 2026-08-15)

| surface | count |
|---|---|
| deliberately C-named producer sites (labelled comparisons) | **9** |
| C-marker occurrences in `ck-dk-canonical-registry.md` | **16** |
| C-marker occurrences in `kernel-constraints-registry.json` | **5** |

## Rule

A reference to convention C is **fine** and should stay when it is history, a
comparison, or an audit *of* C. It must say so: *"convention C (excised
2026-08-09 / re-affirmed 2026-08-15)"*.

## The trap this tranche must not fall into

From `qou-emyt`: the `gram-inverse-unqualified` detector cleared on *"some
convention is named nearby"* — so relabelling a block to D made a still-false
`G⁻¹` claim **pass**. Relabelling became a way to silence the detector. The rule
was split (`gram-inverse-under-d`, critical) because **naming the convention you
are wrong under is worse than naming none.**

So: label, do not relabel-to-silence. If a claim is false under D, H4 is not the
tranche that fixes it — that is `qou-cds2`.

## Verification

`content/pipeline/trace-convention-audit.ts` (selftest 10/10) must stay clean,
and `gram-inverse-under-d` must stay at zero.


---

## Progress 2026-08-16 — producer sites labelled; one content finding deliberately LEFT RED

**Done: the 4 unlabelled producer sites.** Of the 10 deliberately-C-named sites,
6 already carried an excision label. The 4 that did not now say *convention C
(excised 2026-08-09 / re-affirmed 2026-08-15)* and say **why the excised value
is still present** — each is a comparison arm, and deleting it would delete the
thing being compared:

- `markov_z_fibre_rank_bar_covariance_probe.py:119` — also flags that its
  `binding + 8 corpus sites` attribution was already stale when written (the
  binding channel moved to D on 2026-08-09). Left as recorded history rather
  than re-counted: re-inventorying is `qou-cdh3`, and a fresh count in a probe
  comment would only go stale again.
- `markov_z_full_bar_condition_probe.py:97` — its result is *why the ruling
  reads as it does* (`bar(z) = z − h` holds for `z_D`, fails for bar-even `z`).
- `ocneanu_param_from_fibre_dimension.py:169` — an audit *of* C: it confirms the
  C weights the corpus once quoted are the ones `z_C` actually produces, which
  is what makes C-era numbers recognisable wherever they survive.
- `probe3qrv_zpin.py:69` — the point is that `z_C` is **not** a root of
  `y_(1³) = 0` while `z_D` is.

Verification held: `trace-convention-audit.ts` selftest **17/17** (the bean says
10/10 — stale count, not a stale rule), producer audit **50/50**, the
deliberately-C-named bucket still reads 10 and ACTIONABLE still reads 4.

## The content finding I did NOT label — and why that is the point

`trace-convention-audit.ts` reports, pre-existing on `main`:

```
FAIL  prf:interface-knot-markov-z   c-value-unlabelled @ md:56  (x2)
```

The value is `0.49932033` — `z_C` to eight figures. The deuteron row has
`p₊=1, p₋=0`, so its "predicted `z^{p₊}(z−h)^{p₋}`" column **is** `z`, and the
whole table is convention-C.

**Labelling it would clear the detector and leave a live C-frame claim
standing** — the exact `qou-emyt` trap this bean is written to avoid. So it
stays red. H4 labels history; it does not launder a live claim into history.

**Root cause, and it is not a labelling one.** The block states it computed
"using `pyhecke_native`", and `qou-j6il` is the trap where the installed
`pyhecke_native.so` returns `markov_z(q₀) = 0.4993203341836945` — `z_C` —
while its Rust source (`tools/hecke-engine/src/gram.rs:75`) reads D. This table
is a **published downstream consequence of that stale binary**. `qou-j6il` is
marked **completed**: the binary was fixed and the numbers it had already
written into the corpus were never regenerated. Closing a trap does not close
its published consequences.

Belongs to `qou-9xla` (producer missing for this block's 4 atoms) / `qou-cdh3`
(regeneration), not here. Recorded rather than touched.

## Remaining in H4

The two registries — 16 C-marker occurrences in `ck-dk-canonical-registry.md`,
5 in `kernel-constraints-registry.json`. Not started.


## Registries: already labelled — measured, not assumed

The bean scopes 16 C-marker occurrences in `ck-dk-canonical-registry.md` and 5
in `kernel-constraints-registry.json`. Re-measured 2026-08-16: **26 and 3**
(the counts drifted; the surfaces are the same). Both are **already compliant**:

- **`ck-dk-canonical-registry.md`** — 12 markers lack a per-line label, and
  *all 12 sit inside §9g or §9h*, which now carry the `🛑 SUPERSEDED IN PART`
  banner and scope note added by `qou-cdh1`. A section-level label satisfies the
  rule for its section; adding 12 per-line labels would be noise, and noise that
  reads like relabel-to-silence.
- **`kernel-constraints-registry.json`** — all 3 (KC13, KC21, KC22) already
  carry `CONVENTION NOTE 2026-08-15 (registry 9g)` with correct C-scoping. No
  edit needed.

**One real staleness fixed** (§9g scope-(a)): the paragraph said settling the
channel — *"derive C, derive D (and re-derive the ladder), or register
`disputed`"* — **"is bean `qou-b3nk`"**. The third option happened and the owner
ruling then settled the convention, so the sentence described an open question
that is closed. Corrected **additively**: `qou-b3nk` is a sibling's
`in-progress` bean, so it is named and left intact rather than repointed; a
note records that the convention is settled (D, channel
`agreed-migration-pending`) and that the *derivation* half is `qou-cds1`.

Validators after: trace registry `PASS (0 errors, 23 warnings)`;
`kernel_constraints_registry_validate.py --lint-docs --strict` unchanged at
`22 rows, 0 errors, 9 warnings → FAIL`, byte-identical to `origin/main`.

**H4 status:** producer sites done (4 labelled, 6 already were), registries done.
The one open item is deliberately open — `prf:interface-knot-markov-z` stays red
rather than be laundered, root-caused above to the `qou-j6il` stale binary.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8328, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-16: "H4(qou-cdh4): registries were already labelled — and one sentence describing a closed question as open"). The work may be partly or fully done. Read the bean before you close it.
