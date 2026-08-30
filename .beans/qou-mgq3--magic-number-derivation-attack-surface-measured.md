---
# qou-mgq3
title: 'Magic-number derivation: measured attack surface, and the two walls'
status: todo
type: task
priority: high
created_at: 2026-08-30T00:00:00Z
updated_at: 2026-08-30T00:00:00Z
---

Follows `qou-pz4m` (delta2-Phi is a parity test). That bean closed a route;
this one maps what is left, measured rather than surveyed.

## The problem decomposes, and the split is the whole game

Standard Mayer-Jensen filling, recomputed here:

| magic | closed by | 2j+1 |
|---|---|---|
| 2, 8, 20 | 1s1/2, 1p1/2, 1d3/2 | 2, 2, 4 |
| 28, 50, 82 | 1f7/2, 1g9/2, 1h11/2 | 8, 10, **12** |
| 126 | 3p1/2 | 2 |

**{2, 8, 20} are pure 3D-harmonic-oscillator closures** — cumulative
(N+1)(N+2) gives 2, 8, 20 and then 40, 70, 112. Many level schemes produce
them; they are cheap and NOT discriminating.

**{28, 50, 82, 126} require spin-orbit inversion.** This is already a proved
scope-(b) exclusion in the corpus and must not be re-attacked:
`docs/audits/2026-07-06-q-deformed-ho-spin-orbit-magic-numbers-assessment.md`
§2 — a *scalar* (q-)oscillator has state space L^2(R^3) with no C^2 factor, so
no operator `s` exists in its algebra and an l.s term is identically absent
from its spectrum. The q-deformation buys the orbit-orbit (l^2) term and the
*cluster* ladder 2, 8, 20, 40, 58, 92; it cannot buy the nuclear one.

**So the single question worth asking is: where do spin-1/2 and l.s come from
in the braid substrate?** Everything else is either already available or
already excluded.

## Wall 1 — the LP dual does not discriminate ANY nucleus at H_3

Measured on `computations/all-nuclides-sdp-admissibility.witness.json`
(3558 nuclides, canonical t=TR_M, G=gram_matrix(), no fit):

- `lp_active_count` takes **exactly one distinct value, 1**, over all 2221
  nuclides with a solvable dual.
- the active channel set is **the same singleton for every one of them**:
  `{gamma}`.

So the H_3 operator selection is flat, not merely magic-blind: there is no
shadow-price structure to change at a magic number, because there is no
per-nucleus structure at all. The witness's own finding says it — *"the
H_3-local operator selection just scales with A ... per-nucleus binding
richness must live in the tower / Delta_lambda"*. Any "does the dual change at
magic Z" probe run at H_3 will return a flat line and answer nothing.

## Wall 2 — the two highest magic numbers are not reachable

Same witness. f64 `build_atom_nf` overflows for **1337/3558 (37.6 %)**, and the
cut is at **A >= 163**:

    Z=  2   8/  8 isotopes have an LP dual
    Z=  8  18/ 18
    Z= 20  29/ 29
    Z= 28  35/ 35
    Z= 50  42/ 42
    Z= 82   0/ 43     <-- none
    Z=126   0/  0

**Z = 50 is the last testable magic number on this path.** Z = 82 is entirely
unreachable and Z = 126 has no rows at all. Reaching them needs the mpfr native
path, which the witness flags as the required infra.

The LR route hits its own wall earlier — `active-set-lr-scaling-profile.witness.json`
gives active tuples 35, 406, 3997, 32070, 229497 for A = 2..6, i.e. ~x7 per
nucleon. A = 8 is ~1e7 and A = 40 (Ca-40) is not in the same universe. The
multi-LR enumeration caps around A = 6-8.

## What the convolution is

`prop:categorical-fourier-transform-exists`: F intertwines the **q-convolution**
with the pointwise product on irreducibles (Peter-Weyl over
R_q = Z[q,q^-1]). `categorical-laplace-transform.md` pins it further — the
convolution is the **mate of the comultiplication Delta_q on H_q**, and that
uniquely characterises L. `q-resolvent.md` works in "the convolution algebra
H_q".

So the convolution is Delta_q-mate on the shuffle algebra, and on characters it
is the tensor product, i.e. **LR fusion**. That is exactly the operation
`conj:diagrammatic-double-magic-lr-fusion` conjectures is *rigid* (multiplicity
one, single self-conjugate nu) at doubly-magic (Z,N). **The convolution and the
magic-number conjecture are the same object**, which is the connection worth
exploiting. Its knot-operator realisation (connected sum? satellite? cabling?)
is NOT established in the corpus — I did not find a block identifying it, and
that is an open item rather than a measured absence.

## Attack options, ranked

1. **Spin-orbit from framing (best).** The ingredients exist and are
   unconnected: `def:q-angular-momentum` = [j]_q[j+1]_q (the SU_q(2) Casimir,
   `climax-volume-mass/q-angular-momentum.lean`), `def:strand-twist-datum` (the
   per-strand integer ribbon twist T(t), `appendix-standard-model`), and the
   writhe-derived isospin. A q-deformed l.s = (twist) . (q-angular-momentum)
   coupling is the missing Mayer-Jensen ingredient. Formalize-first: state the
   coupling, check it reproduces the 1f7/2 inversion at 28 BEFORE any sweep.
   Caution: `strand-twist-datum.md` is explicit that T(t) is a **free label**,
   not read off the ribbon structure, and does not yet descend under
   stabilisation - so a coupling built on it inherits the label's freedom.
   That is the thing to fix first, not to paper over.
2. **Move the LP off H_3.** Wall 1 says the dual is flat at H_3. Re-pose the
   operator selection at the level where the shell lives and re-ask whether the
   active set opens up at magic Z. This is the direct form of "does the shadow
   price structure change" and it has never been run anywhere but H_3.
3. **A_5 branching.** `a5-so3-branching.witness.json` +
   `a5-orbital-degeneracy-fracture` give SO(3) restricted to the icosahedral
   A_5: dims 1,3,3',4,5, max 5. With spin doubling the largest irreducible
   multiplet is 10, so **the 1h11/2 level (12) that closes 82 cannot be an
   A_5 irreducible**. Not fatal (accidental multiplet coincidence is allowed)
   but it is a sharp, cheap, checkable constraint that nobody has stated.
4. **Deprecated-producer archaeology (cheap).** `shell_closure_compute.py` is
   in `_deprecated/` yet is the only thing that reproduces the published table.
   Either restore it with a witness or retire its numbers.

## Explicitly NOT to re-attack

- l.s from a scalar q-oscillator. Proved scope-(b), see above.
- delta2-Phi at any q in (1, phi). 49-point sweep, `qou-pz4m`: Z=20 and Z=2 are
  local maxima at no sampled q.
