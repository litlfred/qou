---
# qou-8p1e
title: 'qou-8pl1/e: the colour route after the marked-pair exclusion — which premise gets dropped?'
status: in-progress
pr: 8200
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-colour
created_at: 2026-08-07T11:05:00Z
updated_at: 2026-10-10T13:49:31Z
parent: qou-8lxd
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


---

## 🛑 STALE CLAIM — `prop:color-su3-from-g2` does NOT have an empty `uses[]` (verified 2026-10-10)

This bean asserts the block carries no dependency edge. Measured on this branch at
`folio/.../braids-and-knots/color-su3-from-g2.ts:23`:

    uses: ["def:octonion-algebra"],

and the three comment lines immediately above it record the discharge explicitly:

    // def:octonion-algebra was authored 2026-08-29 (beans qou-7arp / qou-8fl1);
    // the NOTE that used to sit here, recording its absence, is discharged.
    // It sits immediately above this block in sec:color-algebra, so the edge
    // reads backward.

So the gap this bean names was **closed on 2026-08-29**. The same stale claim is
carried by `qou-8p1x`, `qou-8p1e` and `qou-8p1h`, i.e. three beans repeating one
fact that a fourth bean (`qou-8fl1`) had already fixed — the cross-bean staleness
pattern this front's epic (`qou-8lxd`) records: **read the beans a bean cites AND
the beans that cite it before working it.**

**A residual, and it is a different defect:** that comment says the edge *"reads
backward"* — `def:octonion-algebra` sits immediately above the block it is cited
from in `sec:color-algebra`. That is a forward-reference/ordering question for the
detangler arc, not an absent-edge question, and it is NOT what this bean claims.
Recorded, not filed: it changes a block's position, so it is an owner call.

Also verified: `qou-8p1x`'s route sub-beans **`qou-8p1i` and `qou-8p1j` are both
`scrapped`**, so any item here gated on either is gated on an abandoned route.
`qou-8p1h` in particular is blocked on nothing live.

Provenance: cross-session read-only pre-read of the 15 open `8f-colour` beans
(`/mnt/project-files/eightfold/8f-colour-preread.md`), confirmed on this branch at
`37bdbeef6b3` rather than taken on trust — the pre-read states its own path checks
were run partly against `main` at a different commit.

## Progress (2026-11-16, PR #8200)
- [x] Formalized `nodalGeometricGenus`, `surfaceHomologyRank`, and `nodal_genus_bookkeeping_and_imaginary_split` in `folio/quantum-observable-universe/lean/QOU/Eightfold/TauAnchoredRatioChiralBraidWritheAndSpectralCubicPowerSums.lean` + 50-dps mpmath witness (`qou_8p1e_nodal_genus_bookkeeping_and_imaginary_split`) in PR #8200 (`ec7070e7f1b47f4548cd7f98fc2a7948b28854b0`).
