# The monodromy Jordan structure at every rank (2026-07-19)

**Bean:** `qou-mjrd`. **Lean:** [`QOU/Machinery/HeckeMonodromyJordan.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/HeckeMonodromyJordan.lean)
— sorry-free, `lean`-direct exit 0.

## Functor-assignment brick (the `TauRhoHodgeLift` wall)

The F-construction's T2 (merged #4040) found the cover's local monodromy is
the H₂(i) Jordan-block module — by explicit Burau-at-i computation at n=3.
This file proves the same structure at EVERY rank, by pure algebra from the
merged all-ranks quadratic:

- **`monodromy_h`** — at `q = i`, `h = q − q⁻¹ = 2i`;
- **`eigenvalues_collide_at_monodromy`** — the e₊/e₋ channel eigenvalues
  `q` and `−q⁻¹` coincide at `q = i`: the merged channel pair (#4056)
  degenerates exactly at the monodromy point — the general-rank reason for
  the T4 weight singularity and the T2 non-semisimplicity;
- **`jordan_sq_zero`** — `(σ − i)² = 0` on the length-rule module of ANY
  descent structure: the nilpotent monodromy relation is universal;
- **`jordan_nilpotent_ne_zero`** — `σ ≠ i·id` (witnessed on the constant
  state at a descent point, which every inhabited structure has): the
  Jordan block is genuine — non-semisimple at every rank.

The τ-functor's domain object at the assignment point is now pinned at all
ranks: Jordan structure (this), channel degeneration (this), and
ρ-equivariance (#4059). The remaining wall content is the assignment map
onto the geometric side (whose target carries the matching structure by
T1–T3).

## Wall-1 upstream finding (recorded honestly)

Mathlib's Coxeter development (`Mathlib.GroupTheory.Coxeter.{Basic, Length,
Inversion, Matrix}` at the pinned rev) carries inversion sequences but **no
exchange/lifting property and no parabolic coset decomposition**. Deriving
the coset data of the merged braid (#4059) / far-commutation (#4081)
reductions from `CoxeterSystem` is therefore blocked on an upstream Mathlib
gap, not on this corpus — the honest disposition is to leave the coset data
as the isolated hypotheses they are (or contribute the exchange condition
to Mathlib as a separate project).

Honesty: pins DOMAIN data only; the functor's existence/naturality stay
open. Nothing wired; `1/(8π)` stays phase-4.
