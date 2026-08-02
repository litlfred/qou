# MOC Gauss–Manin: the period map is NOT derivable from the model — and 2.6424 is tr B, not tr_M (2026-08-02)

Branch `claude/q-deformed-saddle-offsets-bdn992`. Bean qou-cog1. Follows
`2026-08-02-hodge-lift-bring-h1-model.md` (the B2 lift reduced to a single MOC
existence axiom) and `2026-08-02-alpha-em-perloop-clauses-obstruction.md`. This
records the honest verdict on whether the minimal open core (MOC) — the
holomorphic period map `Φ: q ↦ H¹(E_{τ(q)}) ⊂ H¹(Bring)` — can be *derived*
inside the explicit E⁴ Hodge model, or whether it is an irreducible categorical
input.

## Question

The B2 τ-lift audit reduced the wall to one field: does the categorical
τ-functor produce a holomorphic period map `Φ`? The MOC audit noted `Φ` lands in
a **rank-2 genus-1 sub-object** `H¹(E_{τ(q)})` — narrower than the full 8-dim
Hodge structure. Is that genus-1 reduction tractable enough to *derive* `Φ` from
the model itself?

## Answer: NO. The genus-1 reduction is still gated on the same τ-functor.

**MOC, even in the rank-2 genus-1 reduction, is NOT derivable from the model; it
genuinely requires the categorical→archimedean τ-functor as an irreducible
input.** The E⁴ model pins the *codomain* (the elliptic factor `E`, its periods
`τ₀`, the Weil real structure `c = SWAP∘conj`, the X₀(5) isogeny) completely —
but the *domain→codomain map* `Φ` is exactly the q↔period dictionary. Reducing
from genus 4 to genus 1 shrinks the target's dimension; it does **not** supply
the map. The discrete q=i shadow (Lean-proved forced) fixes a single *point
value* of `Φ` and supplies **no germ** — the discrete-shadow → continuous-map
gap is untouched by the dimensional reduction. This is the framework's
foundational open bridge (same object as the `E(q)` genus-1 Gauss–Manin
keystone); it is multi-week infra, not a single-session close, and emphatically
not a fit.

## The 2.6424 dead end: it is tr B, not tr_M

A tempting shortcut was the numerical correspondence `2.6424` — the corpus at
one point floated identifying it as the `tr_M` of an `E(q)` Gauss–Manin
monodromy, which would have given `Φ` a concrete monodromy realization. This is
a **dead end**, on two independent grounds:

1. **2.6424 is tr B — the binding-kernel trace — NOT tr_M** (the Markov trace).
   The two objects are distinct; the numerical coincidence is a mislabel. tr B
   is the trace of the binding kernel, not a Hecke Markov trace of a braid, so
   it carries no braid-monodromy content and cannot be the trace of a
   Gauss–Manin `SL₂(ℤ)` monodromy matrix.

2. **The proposed geometric identification is structurally EXCLUDED (Lean,
   sorry-free).** Even setting the mislabel aside, "2.6424 = tr_M of the E(q)
   Gauss–Manin monodromy" is impossible: a Gauss–Manin monodromy on a genus-1
   fibration is an integer matrix in `SL₂(ℤ)`, so its trace is an **integer**;
   2.6424 is not. The exclusion is Lean-proved sorry-free —
   `TrBIntegerTracePrune.no_SL2Z_realizes_trB` — so no `SL₂(ℤ)` monodromy can
   realize the value. The corpus's own proposed geometric identification is
   therefore off the table by a proved invariant (an integer-trace prune, the
   scope-(b) structural-exclusion pattern per AGENTS.md §"refuted / ruled out").

## Verdict (scope-(a) for the derivation, scope-(b) for the 2.6424 route)

- **MOC / `Φ` is not derivable from the E⁴ model** (scope-(a): no derivation
  found; the map is an irreducible categorical input, not excluded in
  principle). The genus-1 reduction narrows the codomain but leaves the
  domain→codomain map open.
- **The 2.6424 = tr_M(Gauss–Manin) shortcut is structurally excluded**
  (scope-(b): the integer-trace prune is a proved invariant, cited —
  `TrBIntegerTracePrune.no_SL2Z_realizes_trB`). Separately, 2.6424 is tr B, not
  tr_M — a mislabel that the exclusion makes moot.

## Net

The MOC survives as the single honest open wall of the B2 lift. No brick
supplies `Φ`, the genus-1 reduction does not make it derivable, and the one
concrete geometric shortcut (2.6424 as a monodromy trace) is both mislabeled and
Lean-proved-excluded. Nothing wired; no closure; `1/(8π)` stays phase-4. The
open successor is the categorical→archimedean q↔period functor itself — the
keystone `E(q)` Gauss–Manin reduction (epic `08a2`), which no single session
closes.
