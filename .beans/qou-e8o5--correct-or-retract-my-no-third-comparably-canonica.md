---
# qou-e8o5
title: 'CORRECT OR RETRACT: my ''no third comparably-canonical anchor'' claim — Whitehead is a candidate'
status: completed
type: task
priority: high
created_at: 2026-08-07T17:10:13Z
updated_at: 2026-08-07T21:11:01Z
---

AN UNPROVED PROSE CLAIM I MADE — either prove it, scope it, or retract it.

In PR #4513 I wrote that because both corpus anchors are the maximally
symmetric member of their cell type (4_1 = 2 regular ideal tetrahedra,
B_3 = 2 regular ideal octahedra), this is "a structural reason a third
comparably-canonical anchor may not exist — making the arc's
2-equations-in-3-unknowns underdetermination FORCED rather than a gap to be
filled."

That is a strong claim and it is NOT established. What is actually known:
  - Reid (1991): 4_1 is the unique arithmetic hyperbolic KNOT. Already cited
    in-corpus. That constrains knots, not links, and arithmeticity is not the
    same property as "2 regular ideal cells".
  - The Borromean rings are one arithmetic link among others (e.g. the
    Whitehead link, already in corpus compute with invariant trace field Q(i)).
    So the "no third anchor" claim is doubtful as stated — Whitehead is an
    obvious candidate third anchor.

WHY IT MATTERS: if a third natural anchor DOES exist, it supplies a third
equation, the system stops being underdetermined, and A_omega becomes
DETERMINED rather than free. That would be the single most valuable outcome
available to this arc — it would dissolve the circularity instead of
documenting it. The claim as I wrote it discourages exactly the search that
could close the gap, which is why it needs correcting rather than leaving.

ACTION: (1) enumerate hyperbolic links with a regular-ideal-cell decomposition
and small invariant trace field (Whitehead, L6a5, the chain links); (2) check
whether any carries a corpus-meaningful particle assignment; (3) if one does,
its S value is a THIRD anchor equation and the underdetermination is over.
Retract or scope the prose claim either way.


---

## 2026-08-07 RESOLVED — and my premise was WRONG in the informative direction

This bean asked whether a third comparably-canonical anchor exists, on the
premise that finding one would "supply a third equation and the
underdetermination DISSOLVES". **That premise is false, and the correction is
worth more than the search would have been.**

### Counting: more anchors NEVER help

Each anchor contributes one equation `S_i = A·κ·(ln²q₀ − ϑ_i²)` **and one new
unknown** `ϑ_i`. So `n` anchors give `n` equations in `n + 1` unknowns (`A` plus
`n` angles) — a deficit of exactly one, **for every n**. Two anchors are not a
data shortage; twenty would be no better.

Proved in Lean, sorry-free, `AfreeThetaConstraint.exists_angle_assignment`: for
EVERY admissible `A` there is a complete angle assignment solving all `n`
equations simultaneously. `A` is never pinned at any anchor count. This
generalises `ratio_attained` from 2 anchors to n.

### So the real question is different

The only escape is an anchor whose `ϑ` is **fixed independently** — contributing
an equation with NO new unknown. Then `A = S/(κ(ln²q₀ − ϑ²))` is determined
outright.

### The corpus's one candidate is closed, on its own terms

The electron is assigned to the trefoil `3₁`, which is **non-hyperbolic**
(Vol = 0, Seifert-fibred) — so `ϑ = 0` looks forced, exactly the shape needed.
But `qbeta_t3_multiknot_binding_probe.py` (lines 107-155) already settles it:
a torus knot's Kashaev invariant has **polynomial, not exponential, growth**, so
there is **no Stokes constant** and hence no `S_e` to use. The probe's own
conclusion: "the binding formula may not apply to torus knots". Its only numbers
there are an explicitly-labelled NAIVE computation with `A_ω = 1` assumed.

So: no `S`, no equation, no escape by that route.

### Why the Whitehead idea also fails

Whitehead is hyperbolic, so its `ϑ` would be a NEW unknown — it falls under the
counting result above and cannot help, whatever its arithmetic pedigree. The
"third anchor" framing was the wrong question from the start.

### What actually would work

An anchor with an independently-fixed `ϑ`. Candidates would have to be
non-hyperbolic (to force `ϑ = 0`) yet still carry a Stokes constant — and the
trefoil analysis suggests those two requirements are in tension, since the
Stokes constant is what the exponential growth of the hyperbolic volume
supplies. That tension is the real obstruction, and it is sharper than
"we need more anchors".

Status: RESOLVED as a corrected negative. Not a search that failed — a search
that was mis-posed, now posed correctly.
