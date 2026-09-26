---
# qou-8p1e
title: 'qou-8pl1/e: the colour route after the marked-pair exclusion — which premise gets dropped?'
status: todo
type: task
created_at: 2026-08-07T11:05:00Z
updated_at: 2026-08-07T12:00:00Z
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


---

## AUDIT DONE (2026-08-07) — the scoping question above is answered

`docs/audits/2026-08-07-klein-quartic-dependency-audit.md`.

**The colour section does NOT rest on the Klein quartic.** "Klein quartic" (the
curve) occurs in exactly two files, both this chapter. The ~12 other "Klein"
hits are the **Klein chart** (an affine chart on Bring, load-bearing for the
mass machinery, entirely unrelated), two are the **Klein four-group**, and
`klein-bring-icosahedral-bridge.md` — which reads like a bridge and is not one —
is Klein's **icosahedral** `A_5` solution of the Bring–Jerrard quintic.

Everything the section derives (PSL(2,7) from Fano, the irreps, Günaydin–Gürsey,
the Sym^2 gate) is octonionic and Klein-free, and both downstream consumers take
only that part. So option 1 above is **cheap**: nothing breaks.

**FRAMING CORRECTION (owner, 2026-08-07).** An earlier draft said the loss was
that colour is no longer "derived from `q_0`". Wrong: `q_0` is a *locally
observed* value and it **varies**, so colour must not depend on it. The correct
target was always the **categorical / fibre-level** substrate (Bring, `A_5`,
Hecke), which is `q`-generic. That is what the bridge was reaching for, and
that is what is lost.

**What the exclusion actually costs:** `prop:color-su3-from-g2` has an **empty
`uses[]`** and no `def:octonion-algebra` exists in the corpus. So the section
now rests entirely on an external input the corpus never defines. This promotes
**`qou-8fl1`** from "missing definition" to "the section's sole foundation,
undefined and unconstructed" — it is more urgent than its current framing says.

## The real gap, restated (supersedes the escape list above as the priority)

Not "which premise do we drop" but: **the single-fibre construction supplies
`dim V = 2`; colour needs a 3-dimensional fibre.** `RowCapObstruction.lean`
already has the Weyl arithmetic (`weylDimAlt N = N.choose 3`,
`singlet_forces_three`), so the *characterisation* of `N = 3` is DONE — do not
re-derive it. `a2-from-three-strands.md` explicitly disclaims supplying it. Every
candidate route must be judged on whether it produces a 3-dimensional fibre.

See §6 of the audit doc for the assessed routes: multi-fibre groupoid (already
named in `schur-weyl-eightfold.md` as direction 1, untouched by all of this);
Bruhat / `GL_n(F_q)` realisation of `H_n(q)`, which would make `PSL(2,7)` native
rather than imported but needs a principled reason for characteristic 2;
"tetraplectic"/4-form, assessed and rejected as a *bigger* octonionic import
(`Spin(7)`) or as the wrong group (`SU(2)`).
