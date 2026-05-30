# Census-knot audit (2026-05-29)

## What I found

Two separate paths in production are using **census knot labels** without
deriving them from the canonical braid `β(Z,N)`. These are independent of
each other and independent of the canonical `binding_canonical` Δtr path.

### Census-lookup path 1: hardcoded SnapPy registries (triplicated)

The same three census braid words appear hardcoded in **three** files —
the same `[Z,N] → SnapPy census knot` map, copy-pasted:

| file | lines | hardcoded census braid |
|------|-------|-----------------------|
| `binding_k_solver.py` | 105, 117, 129 | `6_2`, `8_11`, `L6a4` |
| `binding_k_enumerator.py` | 90, 107, 124 | same |
| `rho_prefactor_structural_verifier.py` | 81 (`REGISTRY_B3` block) | same |

Workplan-flagged (this PR's workplan, line 73): "binding-K registry's
braid words are census-hardcoded, not derived." The workplan reframed
Barrier-1 around this but did not fix the triplication.

**Status:** these registries are **not on the canonical-mass-table
production path** — `binding_canonical` builds the braid from
`atom_braid_word_3A(Z,N)` (the derived per-nucleon construction in
`mass_at_3A_proper.py:254`). So the census triplication has not
contaminated the production mass numbers. But it has **contaminated the
binding-K research path** the workplan is built on top of.

### Census-lookup path 2 (subtler): the "Vol(K_bind)=8G" assumption

`binding_endomorphism_deuteron.py` derives `B(D) = m_e · Vol(K_bind) · Δtr`
and obtains +0.19% by plugging in `Vol(K_bind) = 8G = Vol(Borromean)`.
**8G itself is a derived knot invariant** (Catalan/dilog identity).
But the **assumption that K_bind(D) = Borromean link** is *not* derived
from β(D); it is an identification — the only "derivation" is the
numerical agreement (+0.19%).

So even the cleanest "derived" binding case is one labelled volume away
from the canonical braid. Across the 7 atoms, my Vol = 8G·f
factorization treats the same way: Vol_*assumed*_universal = 8G; the
nuclide-dependence absorbed into a scalar f. **`f` is `Vol(actual
K_bind(Z,N)) / 8G` in disguise** — I never computed `Vol(actual)`
directly because:

- **SnapPy is not installed** in this container.
- The repo's volume machinery is **specific to 4_1 and Borromean** (constants
  `vol_4_1 = 2·Cl₂(π/3)`, `vol_borromean = 8G`); there is no
  `Vol(closure(arbitrary_braid_word))` function.
- The canonical braid `atom_braid_word_3A(Z,N)` outputs `(c, d, gen_idx)`
  triples (Hecke-element factors), not pure braid generators
  `{±σ_i}`. The closure → SnapPy step requires a separate pure-braid
  extraction that does not exist.

### What the AME-extracted f is, then

Given the above:
- **Δtr** is derived (canonical β(Z,N) at H_{3A}, no census).
- **f = B_AME / (m_e · 8G · Δtr)** is then literally
  **`Vol(K_bind(Z,N)) / 8G`** under the universal-Borromean
  assumption — i.e. the gap between AME binding and the
  assumed-Borromean prediction, normalised.
- f's structural patterns (Z·N near-fit for D/6Li/7Li, A=3 mirror = κ_Coulomb,
  ⁴He bonus 2.07) are real signals **about that gap**. They are
  candidates for what the actual Vol(K_bind(Z,N))/8G must look like, not
  derivations of it.

## What this means for Barrier-1

The genuine Barrier-1 question is **not** "what is f(Z,N)?" — that's a
proxy. The genuine question is:

> **Compute `Vol(closure(canonical β(Z,N)))` for the 7 atoms directly,
> without census labels.**

If that volume matches `8G · f_AME` within compute tolerance, the
Borromean-class universal-8G assumption holds and the f-extraction is
*equal to* the canonical knot volume — Barrier-1 is solved.

If it doesn't match, the universal-8G framing is wrong; the actual
K_bind(Z,N) is a different link family at each atom. Either outcome is
real progress; we currently have no evidence either way.

## Blockers to the genuine derivation

To compute `Vol(closure(β(Z,N)))` I would need at least one of:

1. **SnapPy** installed (`pip install snappy` — not in this container).
2. A pure-braid-word extraction from `atom_braid_word_3A` (it emits Hecke
   factors `(c, d, gen)`, not raw σ_i / σ_i⁻¹).
3. An alternative volume route (e.g. the Yokota volume formula, the
   Cheeger–Chern–Simons functional) implemented locally.

None of these are blockers to merge — they are research blockers to
**deriving f**, which is the open Barrier-1 question.

## Recommendations (action items, not landed)

- **A**. Install SnapPy in the CI/dev environment (1 line in setup);
  enable `Vol(closure(β))` directly for the canonical braid.
- **B**. Refactor the 3 census-registry files
  (`binding_k_solver.py`, `binding_k_enumerator.py`,
  `rho_prefactor_structural_verifier.py`) to consume
  `atom_braid_word_3A(Z,N)` — single source of truth, no copy-pasted
  SnapPy literals. The census labels can stay as **annotations** on the
  derived word (for human discoverability) but must not be the source.
- **C**. Add a `Vol_closure(braid_word, q=q₀)` function — either via
  SnapPy (preferred) or via the Hoste–Zheng / hyperbolic-gluing route
  already cited in the cheat sheet.
