---
# fwr8
title: 're-baseline every ordering metric after the manifest parser fix'
status: open
type: task
priority: normal
created_at: 2026-08-10T01:50:00Z
updated_at: 2026-08-10T01:50:00Z
parent: fwr6
---
folio-assistant #99 fixed a manifest parser that hid **45 of 3498 blocks** from
`loadChapterGraph`: a `]` inside a comment truncated the `blocks: [...]` array,
and every block below it lost its position. A block with no position reads as
"not listed" and returns `pass`, and edges pointing at it are skipped — so the
detangler reported clean on material it had never looked at. The reverse also
bit: a slug quoted inside a comment counted as a real entry, shifting every later
position in its chapter by one.

**Everything measured before that fix is wrong by an unknown few.** On the same
tree the paper reads **192 with the old parser, 195 with the new one** — three
real forward references were hidden behind the truncation, and the arc's starting
figure of 274 was understated the same way.

What needs redoing, in order:

1. **Re-run `detangler-no-forward-ref` corpus-wide** and record the true count.
   Cheap; one sweep.
2. **Re-check the 45 previously-invisible blocks specifically.** They have never
   been through the forward-ref criterion at all, so any finding there is new,
   not a regression. `braids-and-knots` (16) and `climax-volume-mass` (13) hold
   most of them.
3. **Re-check the chapters where a slug-in-a-comment shifted positions** —
   `knots-particles-confinement` and `nuclear-interactions` each counted one
   phantom entry, so every distance measured in them was off by one.
4. **Correct the arc's headline figures** in `fwr1`-`fwr6` rather than leaving
   the old numbers standing as if they had been measured.

The adjudications, reviews and moves from that arc are unaffected — they turned
on reading, not on the count. Only the numbers move.
