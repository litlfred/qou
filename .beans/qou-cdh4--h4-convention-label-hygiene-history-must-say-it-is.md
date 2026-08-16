---
# qou-cdh4
title: 'H4 (hygiene): convention-label hygiene — history must say it is history'
status: in-progress
type: task
priority: low
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-16T03:11:27Z
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
