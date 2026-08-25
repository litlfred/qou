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


## OPTION-2 ANSWERED 2026-08-23 — the connection is NOT determinate, and CS is excluded BY THE FRAMEWORK

Follow-up to the scoping note above, which asked whether the missing
`E -> A` is (a) a real unwritten piece or (b) evidence these blocks are
informal. Answer: **(a), but the route that would have made it tractable is
closed.**

### Correction to my own scoping note

That note says "no such map exists in the corpus". **Too strong.** The
interface exists and is canonical-chain-sanctioned:

    -- QOU/Mathlib/NonAbelianStokes.lean:49
    structure LieValuedOneForm (M G : Type u) where
      eval : M -> M -> G          -- two points of M |-> a group element

Exactly the shape `K_FH(q; s, t)` needs. My greps keyed on
`def .*(embed|toAlgebra|...)` and `E -> A`, and missed it because it is a
structure FIELD named `eval` — the same name-gate blindness as the
CONCLUSION_FIELD miss in the vacuity detector. Recorded as a correction, not
deleted: the diagnosis (a metric-carrying map is what is missing) stands; the
claim of total absence was wrong.

Its status: an "abstract carrier" by its own docstring, and its ONLY instance
corpus-wide is `punitInstance` (NonAbelianStokes.lean:108) — the qou-6dzi /
PUnit defect. The slot exists and has never carried anything.

### Why the Chern-Simons route is closed

The tractable attack was to identify the connection with the Chern-Simons
connection: its two-point function has magnitude exactly `1/|x-y|^2`, the
Mobius kernel on the nose, and its Wilson loops give Jones, which is the
chain the framework already runs on. `witten1989` is cited in references.ts
as "the bridge between QFT and knot theory used throughout the QOU braid /
WRT material".

**The framework rejects this in writing.**
`models-of-qous/categorical-action-vs-chern-simons.md`:

- "The bulk categorical action does not recover classical Chern-Simons."
- "(Here A_cl is a g-valued connection 1-form on a 3-manifold M, DISTINCT
  from the QOU observable object A in C.)"
- CS "enters the framework separately as a geometric knot invariant for
  non-hyperbolic torus knots."

Pursuing the CS identification would not merely be fitting — it would
contradict an existing content block.

### And the base connection is a free input anyway

`def:categorical-q-connection` reads "Let nabla be a categorical connection
on A", then defines
`nabla_q = q^-1 nabla + (1 - q^-1)(iota_xi nabla) Theta_A`, with
`nabla_q = nabla` at `q = 1`. So nabla is universally quantified;
`prop:categorical-connection-exists` / `-unique` pin it only up to gauge, with
no formula anywhere. The `q -> 1` limit of any kernel built from `nabla_q` is
therefore the classical kernel built from nabla — and getting `1/r^2` out
means CHOOSING nabla to produce it. That is the fit vta3 forbids.

### The deeper reason it cannot work

`predicted-spectra/three-knot-jet-order-independence.md`: "The coloured-Jones
invariant J_K(q) acts as the holonomy of the categorical connection,
parallel-transported along the SUBSTRATE q-DEFORMATION PATH on
S = P x_G CP^1."

The framework transports along the **q-direction**, on the state fibre — not
along the filament in R^3. A connection whose holonomy is J_K(q) in q-space
has no two-point Euclidean data to give. `1/|gamma(s)-gamma(t)|^2` cannot come
from it, whatever nabla is chosen.

### Disposition

- Option 1 (instantiate Stokes with a CS connection): **DROPPED.** Excluded by
  the framework, not merely unsupported.
- Option 3 (formalise the classical Mobius / Freedman-He-Wang side,
  independent of the q-side): **live and safe.** It also unblocks
  `mobius_energy_nonneg`, whose `energy_classical` is an opaque field today.
- These beans stay open on the strength of the interface slot existing — but
  the next agent should NOT go looking for a connection to instantiate it
  with. That search is closed.
