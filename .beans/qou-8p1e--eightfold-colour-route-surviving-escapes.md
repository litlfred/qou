---
# qou-8p1e
title: 'qou-8pl1/e: the colour route after the marked-pair exclusion — which premise gets dropped?'
status: todo
type: task
created_at: 2026-08-07T11:05:00Z
updated_at: 2026-08-07T11:05:00Z
---

Parent: `qou-8pl1`. Successor to `qou-8p1b`, which closed with a **scope-(b)
structural exclusion**: under the chapter's own three premises the
Bring -> Klein degeneration cannot happen, because `S_4` has no orbit of size
`<= 2` on `P^2` and the pinch necessarily supplies an `S_4`-stable pair of
marked points (`s4_marked_pair_obstruction.py`).

Repairing the *argument* is no longer enough. The colour route now has to give
up one of its own premises **explicitly**, and say which. The four options,
with what each costs:

1. **Hyperelliptic target.** Drop (H3). The obstruction genuinely does not
   apply — a hyperelliptic genus-3 curve's canonical map is 2:1 onto a conic,
   so `Aut` does not act through `PGL_3` in the relevant way, and
   `y^2 = x^8 + 14x^4 + 1` has `|Aut| = 48` containing `S_4`. **Cost: the
   Klein quartic is not hyperelliptic.** Taking this escape means the colour
   route no longer lands on Klein, and everything downstream that used
   `PSL(2,7)` and the Fano plane has to be re-derived or abandoned. Check what
   actually depends on Klein specifically before spending effort here.
2. **Multi-node or separating pinch.** Drop (H1). Changes the genus
   bookkeeping — the chapter's own `g_arith = 4 -> g_geom = 3` chain says one
   node — so the chain has to be rewritten, and the new bookkeeping stated.
3. **Non-faithful `S_4` on the normalization.** Drop (H2). But "S_4 survives
   the pinch and embeds in `Aut`" is the bridge premise; dropping it discards
   the mechanism the section is built on.
4. **Abandon the colour route's Bring -> Klein step** and reach `PSL(2,7)` /
   the Fano plane some other way, if it is reachable at all.

## Do this first (cheap, and it scopes the rest)

Audit what in the corpus actually **depends on the Klein quartic specifically**,
as opposed to on `PSL(2,7)` or the Fano plane abstractly. If little does,
option 1 is cheap and the exclusion is not costly. If the whole colour section
rests on Klein, this is a significant structural problem for that section and
should be labelled as such rather than left as a repair note.

## Still open and independent of all this

Classify the `S_4`-invariant 1-cycles on the Bring surface up to the `S_5`
action (`H_1(Sigma_4, Z)` has rank 8). The exclusion constrains the *target*;
nothing yet is known about which cycles the *source* even offers, and
different invariant cycles may pinch differently.
