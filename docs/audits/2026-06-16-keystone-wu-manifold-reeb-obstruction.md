# Deriving the keystone Wu-manifold step catches a flaw: the "spatial-SO(3) Reeb on SU(3)/SO(3)" is obstructed

**Date:** 2026-06-16
**Branch:** `claude/keystone-wu-manifold-reeb-obstruction-2026-06-16`
**Status:** derivation-attempt correction to the keystone scope doc; verified (structural), no fabrication.
**Discipline:** formalize-first + critical-distance (attempting the derivation surfaces and corrects a flaw in
the proposed path).

## Context

`conj:s5-so3-fiber-action` was reduced this session to one open differential-geometry problem (keystone ledger):
does the colour Sasakian's equivariant index reproduce the Ocneanu weights `W_λ`? The scope doc
([`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md`](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md))
proposed the arena is an **SU(3)/SO(3)-homogeneous (Wu-manifold) Sasakian with the colour Reeb in the spatial
`SO(3)_colour`**. Attempting to *derive* this immediately exposes a flaw.

## The obstruction (verified — `scripts/keystone_wu_manifold_reeb_obstruction.py`, exit 0)

On the homogeneous space `SU(3)/SO(3) = G/H` (G = SU(3) acting by left translation, H = SO(3) the **isotropy**;
dim = 8−3 = 5, odd):

- A **Reeb vector field is nowhere-zero** (it generates the contact flow).
- The isotropy `H = SO(3)` **fixes the basepoint** `o = eH`; any one-parameter subgroup of `H` acts by left
  translation fixing `o`, so its **Killing field vanishes at `o`**.
- Hence an `SO(2) ⊂ SO(3)(=isotropy)` Killing field is **zero at `o`** — it **cannot** be a Reeb field.

**So the "spatial-SO(3)_colour Reeb on SU(3)/SO(3)" framing conflates the isotropy `SO(3)` (which is quotiented
out and fixes the basepoint) with an *acting* symmetry.** The resolution direction is obstructed as stated.

## What the derivation must do instead (re-opened, honest)

- The Reeb must be a **`U(1) ⊂ SU(3)` that is NOT in the isotropy `SO(3)`** (so its Killing field is nowhere-zero
  on `SU(3)/SO(3)`).
- One must then re-derive **which `U(1)`** is the colour Reeb, and **how the icosahedral `A₅ ⊂ SO(3)`** (the
  generation chirality structure) relates to that Reeb — they are now in *different* subgroups of `SU(3)`, so the
  clean "A₅ acts as the icosahedral rotation on the Reeb sphere" picture must be re-established or abandoned.
- Only then does the **equivariant-index = `W_λ`** computation make sense. This is genuine differential geometry
  (regular vs irregular Sasakian on a specific 5-manifold + an equivariant-index computation), **multi-session,
  not derivable in-session** without geometry tooling/references.

## Honest verdict on "derive the keystone geometry"

Full derivation is **not** achievable in-session — it is the irreducible research core. But the attempt was not
empty: it **caught a real flaw** in the proposed path (the isotropy-vs-acting conflation), which would have
mis-aimed the construction. The corrected open obligation is now: *find the nowhere-zero `U(1) ⊂ SU(3)` Reeb
(outside the isotropy), reconcile it with `A₅ ⊂ SO(3)`, and compute its equivariant index against `W_λ`.* This
supersedes the scope doc's "spatial-SO(3) Reeb" wording.

## Cross-references

- `docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md` — the scope doc (resolution direction corrected here)
- `docs/coordination/s5-so3-keystone.md` — keystone ledger (open object)
- `docs/audits/2026-06-16-s5so3-markov-weighting-sasakian-scope.md` — the W_λ target + Boothby-Wang compatibility
- `scripts/keystone_wu_manifold_reeb_obstruction.py` — this obstruction (exit 0)
