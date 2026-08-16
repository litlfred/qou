# Forward-pointing `interprets` edges — nine relocations, three questions

Generated 2026-08-16. Bean `qou/0sq1`. **Nothing here is relocated.** One
listing-order slip was fixed; the rest are author decisions, grouped so there
are three questions rather than nine.

A remark or example placed **before** the block it interprets asks the reader to
follow an interpretation of something they have not met. `interprets` became an
editorial edge on 2026-08-15 (folio-assistant `i8ad`), which made these visible
for the first time.

**`detangler-no-forward-ref` does not count them.** It builds its own `uses`-only
adjacency, so these are real forward references outside the gate. Widening the
gate would move it from 195 to about 205 — a number five merged PRs were
measured against — so that remains a separate decision. Nothing below depends on
it: these are wrong for the reader whether or not a gate counts them.

## Fixed: the one listing-order slip

`rem:collatz-parity-to-divisor` declares `interprets: "prop:collatz-contact-boundary"`
and was listed **immediately before** it, both in `appendix-surreals §15`.
Adjacent, one section, nothing else depending on the order — a slip rather than
a structural question. Swapped.

## The remaining nine, grouped

Every one crosses a **section** boundary, so each is a relocation that changes
what a chapter argues in what order. That is not a tooling decision.

### Question 1 — three remarks about a proposition one section later

| gap | remark | section |
|---|---|---|
| 22 | `rem:groebner-nf-computation` | `predicted-spectra §13` Hadron half-life and Gröbner NF |
| 18 | `rem:kummer-shell-closure` | `predicted-spectra §13` |
| 17 | `rem:nf-computation-strategy` | `predicted-spectra §13` |

All three interpret **`prop:shell-closure-normal-form`**, which sits in
`predicted-spectra §14` *Atomic shells: construction foundations*.

One decision covers all three: either the proposition moves up into §13, or the
three remarks move down into §14. The fact that §13 is titled for Gröbner NF and
§14 for "construction foundations" suggests the foundation is meant to come
first — but that is exactly the judgement to make rather than assume.

### Question 2 — two remarks about a proposition fourteen sections later

| gap | remark | section |
|---|---|---|
| 180 | `rem:q-deformed-double-slit` | `observations §3` Double-slit experiment |
| 117 | `rem:w-boson-mass-discrepancy` | `observations §8` Terminal resolution and the $W$-boson discrepancy |

Both interpret **`prop:local-substrate-q`**, in `observations §17` *Proton Radius
and Gravity Tests*. These are the two largest gaps in the corpus by this
measure.

A proposition two named experiments depend on, placed after both, is the shape
the detangler arc has spent five PRs removing. The obvious reading is that
`prop:local-substrate-q` belongs early in the chapter — but moving a block
across fourteen sections is a real editorial act.

### Question 3 — three singles

| gap | block | interprets | across |
|---|---|---|---|
| 153 | `rem:mass-tower-syt-cells` | `rem:mass-endomorphism-jet-tower` | `mass-theory §24 → §33` |
| 53 | `rem:archimedean-calabi-yau` | `thm:descartes` | `brings-surface §9 → §14` |
| 13 | `ex:brings-surface` | `def:brings-surface` | `brings-surface §2 → §4` |
| 7 | `rem:information-paradox-incompleteness` | `rem:hawking-radiation` | `information-theory §11 → §12` |

The last of these is the mildest and the clearest in principle: **an example
placed before the definition it exemplifies**. `ex:brings-surface` sits in §2
*Physical regimes and limiting context* while `def:brings-surface` is in §4
*Bring's surface as a QOU*. An example in a scene-setting section may be
deliberate — introducing the object informally before defining it — which is
precisely why it is listed here rather than moved.

## How to re-derive

```sh
bun run scripts/interprets-graph-questions.ts
```

Prints both this list and the editorial cycles, with the field carrying each
leg.
