---
# ne0m
title: Formalize q-Hodge-star kernel identification to unblock lem:nsi-q-deformed-kernel
status: todo
type: task
priority: low
tags:
    - compute-wiring
    - blocked-domain
created_at: 2026-07-06T04:31:27Z
updated_at: 2026-07-06T04:31:27Z
---

Blocked: nsi_q_kernel_hard_singularity is proved sorry-free, but nsi_q_kernel_identification is an honest sorry (q-deformed commutator / q-Hodge star not formalized). A probe would only re-verify the trivial r^2-hbar^2=0 tautology, not the identification. Bean, not fabrication.

## SCOPING 2026-08-23 — the load-bearing gap is NOT the q-Hodge star

Scoped for formalisation and stopped before writing definitions. The
blocker recorded in this bean is real but is *downstream* of a more basic
one, and naming the wrong blocker sends the next agent at the wrong
object.

**The kernel claim is not type-correct as written.** The target is

    tr(Delta(gamma(s)) tensor Delta(gamma(t)))  ->  1/|gamma(s) - gamma(t)|^2

`gamma(s)` is a point in a normed space (a point on the filament in R^3).
`Delta` is a coalgebra map on the algebra A. So `Delta(gamma(s))` only
means anything given a map

    E  ->  A     (filament points -> algebra elements)

and that map does not exist anywhere in the corpus. Measured 2026-08-23:

- Every map found is algebra->algebra (`H_n(q) -> H_n(q)`: antipode S, bar
  involution) or braid-group->algebra (`B_n -> H_n(R,q)`, IwahoriHecke/Tw).
  Nothing maps SPACE into the algebra.
- The block declares exactly one dependency, `def:frobenius-pairing`
  (mba-step06). Its inputs are *Hecke normal forms* `a, b in H_n(q)`; its
  value is `<a,b>_F = tr_M(a.b)` (`QOU/Hecke/Wedderburn.lean:197`,
  `def frobPairing (a b : A) : R := MT.trace (a * b)`). Pure algebra.
- In the whole `QOU/Hecke/` and `QOU/BraidsKnots/` trees, Euclidean
  distance appears in exactly TWO files: `mobius_frobenius_kernel.lean`
  and `nsi_q_deformed_kernel.lean` — i.e. only in the *conclusions* of the
  two unproved kernel statements, never on the algebra side.

**Consequence.** The Frobenius pairing cannot produce `1/r^2` because it
has no access to `gamma` at all. The distance dependence has to enter
through the missing embedding, so that embedding — not the q-Hodge star —
is the object that has to be defined first and is where the metric content
actually lives. Formalising the q-Hodge star without it would still leave
the statement unstatable.

**Also: the .md pins nothing.** The content block is two sentences and one
display equation. There is no definition of Delta, no q-Hodge star, no
explicit K_FH. So "define it faithfully from the manuscript" is not
available either — there is nothing to be faithful to beyond the words.
This is why both beans say do not fabricate: any concrete K_FH an agent
writes down would be invented, and the limit would then be a theorem about
the invention.

**Recommended next step (NOT taken here):** decide whether the embedding
`E -> A` is (a) a real piece of the framework that is simply unwritten, in
which case it needs an owner-level statement of what it is, or (b) evidence
that the kernel blocks are informal-by-nature and should be re-scoped as
conjecture/prose rather than carried as theorem-shaped sorries. That is a
framework question, not a Lean question.

Scoped alongside `ne0m`, whose block `nsi_q_deformed_kernel.lean` is the
same pattern and the same missing object.

