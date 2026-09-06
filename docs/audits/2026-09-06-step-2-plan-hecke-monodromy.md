# Step-2 plan: closing the stipulated curvature (cheat-sheet §2a) by monodromy

**Date:** 2026-09-06 · **Branch:** `claude/binding-gap-categorical-research-cem5tp` · **Bean:** `qou-0jcd` (see the
session ledger, parent `qou-2akx`) · **Status:** PLAN — nothing below is built;
the owner picks the options.

## 0. The decision, in one paragraph

Step 2 of the canonical chain is the only bridge from the geometric substrate to the Hecke algebra
`H_n(q)`, and it is **stipulated**: the curvature 2-form is *defined* to be the Hecke quadratic
`F(σ) = σ² − (q − q⁻¹)σ − 1`, so "flatness derives the Hecke relation" is a tautology
([cheat-sheet §2a](../canonical-derivation-cheat-sheet.md), downgraded 2026-08-25). The connection–curvature
pair the corpus names, `(∇_A q, L ∧ F⁺)`, exists only as a norm integrand inside the mass identity
(`def:mass-identity`, `mi-sw-abelianisation`, the fluid-dynamics blocks); no form, no connection and
no crossed module is defined anywhere in Lean. §2a itself names the two honest exits: *a real
multiplicative-integral construction whose curvature is computed to be the quadratic*, or *a §3b
conjecture class with the geometric step as hypothesis*. This plan lays out four options and
recommends two of them now.

Everything the 2026-09-05 arc found bears on this: C1 (§7e of the survey) showed that for a fake-flat
pair the non-abelian content of Yekutieli's 2-dim multiplicative integral is its boundary 1-holonomy
up to a central element — so Step 2 is a statement about **1-dimensional monodromy**, not about a
surface integral; and the T1/7g results show the classical (`q = 1`) shadow of every Hecke object is
permutation/component-count data, which is exactly what monodromy around a branch point supplies.

## 1. What the corpus already says (measured 2026-09-06)

| item | where | status |
|---|---|---|
| Hecke quadratic factorises, roots `q, −q⁻¹` | `QOU/Mass/HeckeStokesEigenvalues.lean:38` | proved, generic field; algebra only |
| "abelianised Cartan connection on `S_c` has curvature `F(σ)`" | `NaStokesKeystone.lean:22` docstring | **stipulated** |
| `prop:hecke-spectral-sequence` (the cited geometry) | 0 `label:` declarations in `content/` | **dangling** |
| KZ connection "flat at `q₀`", monodromy "= the `U_q(su₂)` R-matrix" | `mass-theory/lifted-crossing-locality.md:15`, `vertex-operator-dictionary.md:1,3` | prose, no construction; and it writes `q = e^{2πi/(k+2)}` — **unit modulus**, against `Im(q₀) = 0`, `q₀ ≈ 1.11` (AGENTS.md fibre-vs-observable banner) |
| Kohno–Drinfeld (KZ monodromy factors through Hecke) | `references.ts`: `kohno1987`, `drinfeld1985` | cited; not held in `library/` |
| colour cubic `X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)` | `jet-prolongation.md`, `sw_period_growth_probe.py` | root `X(z)` and its jets are the SW periods |
| its discriminant in `z` | computed 2026-09-06 (sympy, exact) | `−(16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16)`: a **reciprocal sextic**, six simple complex branch points, none real |
| local behaviour at a branch point | `NaStokesKeystone.lean` header, PR #2795 | `X^(n) ~ (z−z_k)^{1/2−n}`: a **√-branch** |

The last two rows are the classical content Step 2 has never used: around a simple branch point of a
cubic, the monodromy of the roots is a **transposition**, and on the period lattice it is a
**reflection** (Picard–Lefschetz). A reflection satisfies `σ² = 1`, i.e. `(σ − 1)(σ + 1) = 0` — the
`q = 1` specialisation of `(σ − q)(σ + q⁻¹) = 0`. So the Hecke quadratic *is* a q-deformed
branch-point monodromy relation; what is stipulated is only the deformation.

## 2. The options (six-part frame)

### A. Restate Step 2 as a §3b conjecture class — `HeckeMonodromy`

- **What it means.** A Lean `class HeckeMonodromy (n : ℕ) (q : K)` whose fields say: the framework's
  flat connection on the complement of the discriminant locus of the colour cubic has braid-group
  monodromy `ρ : B_n → H_n(q)` with each generator's image satisfying the Hecke quadratic, and the
  Markov trace of the closed loop is the framework's `tr_M`. `stokes_curvature_factors` becomes a
  *consequence* (eigenvalues of `ρ(σ_i)`), `NaStokesKeystone`'s docstring becomes a hypothesis, and
  the dangling `prop:hecke-spectral-sequence` is replaced by a real `conj:` block carrying the class.
- **What it costs.** One Lean file (class + two lemmas), one new content block, edits to two
  docstrings and the cheat-sheet status column. About half a day; no compute.
- **What it risks.** Nothing numerical moves. The chain's status column already reads 🟡 for this step;
  this makes the 🟡 formal. The downstream conditional-class propagation (§3b-cond) may require
  banners on a handful of blocks that currently read as unconditional — a currency sweep, not a
  derivation.
- **What it commits to.** That Step 2 is *conditional* until B or C closes it. Honest per AGENTS.md
  "Derive-then-check" item 8; forecloses nothing.

### B. Derive the classical shadow: Picard–Lefschetz monodromy of the colour cubic (probe + Lean)

- **What it means.** Compute, exactly, the monodromy of the three roots `X(z)` around each of the six
  branch points (high-precision analytic continuation in `mpmath`, plus the exact discriminant
  factorisation), establishing that each local monodromy is a transposition and that the global
  monodromy group is `S₃` (or a proper subgroup — measurable). Formalise the elementary half: a
  reflection's minimal polynomial is `X² − 1`, the `q = 1` specialisation of the Hecke quadratic
  (`(X−q)(X+q⁻¹)` at `q = 1`). This *derives* Step 2 at order zero and isolates the q-deformation as
  the single open hypothesis of A.
- **What it costs.** One exact probe (a few hours; the cubic is degree 3, the discriminant is degree
  6, everything is finite), one short Lean file. No new constants.
- **What it risks.** The result could be that the monodromy group is smaller than `S₃` or that the
  branch points pair up under the reciprocal symmetry in a way that changes which transpositions
  occur — either is a finding, not a failure. Nothing wired.
- **What it commits to.** A specific classical mechanism for the Hecke quadratic; if the framework's
  eventual connection is not the Gauss–Manin connection of the colour cubic, this shadow is
  irrelevant to it. That is a real possibility and is why B is paired with A, not offered alone.

### C. The q-deformation as a KZ-type connection — with a real-`q` prune first

- **What it means.** The corpus's own prose says the substrate connection is Knizhnik–Zamolodchikov
  and its monodromy the `U_q(su₂)` R-matrix; Kohno–Drinfeld is exactly the theorem that KZ monodromy
  on a configuration space factors through `H_n(q)`. Option C is to make that a construction: the
  KZ connection on the configuration space of the six branch points, its monodromy computed, and the
  Hecke quadratic read off.
- **The prune, first (formalize-first).** KZ at real level has monodromy eigenvalues of **unit
  modulus** (`q = e^{iπ/(k+2)}`-type), while the framework's `q₀ ≈ 1.11` is real and greater than one.
  So either the level is imaginary (a non-unitary KZ connection), or the substrate connection is not
  KZ. This is a one-page structural statement, checkable before any construction: it either kills
  the "flat KZ at `q₀`" prose of `lifted-crossing-locality.md` or forces it to name a non-unitary
  level. The corpus already carries the fibre-vs-observable banner saying `Im(q) = 0` only at the
  archimedean evaluation; option C would have to say precisely how a unit-modulus fibre `q`
  becomes a real observable `q₀` — the same question the `c_k` Habiro-element program faces.
- **What it costs.** The prune: one Lean lemma (`|e^{iθ}| = 1 ≠ q₀`) and one audit paragraph, an
  hour. The construction: research-scale; unknown; needs Kohno 1987 held in `library/` (not yet).
- **What it risks.** The prune may show the corpus's KZ prose is inconsistent with the real pin —
  which is a correction to two content blocks, not a loss. The construction may not exist.
- **What it commits to.** If the prune passes (imaginary level accepted), Step 2 becomes a
  representation-theory derivation with a literature model; if it fails, the "KZ" wording leaves the
  corpus and Step 2 stays a conjecture class.

### D. Do nothing

Status quo: §2a already records the stipulation; the chain's step-2 row is 🟡; route D2's `∫γ`
stays blocked because no `(α, β)` forms exist. Nothing is wrong that is not already written down.

## 3. Recommendation (judgement, not a finding)

**Do A and B now, together, in one PR; do C's prune in the same PR; leave C's construction as a
research bean.** A costs half a day and is owed regardless. B is cheap, exact and gives Step 2 its
first *derived* content — the order-zero half — in the same sense the whole 2026-09-05 arc kept
finding: the classical part is topology (a reflection), the deformation is the open part. C's prune
decides whether the corpus's KZ language survives contact with a real `q₀` before anyone spends a
week on a construction. If the owner says nothing, D holds and nothing changes.

**Blast radius.** A touches `NaStokesKeystone.lean`, `HeckeStokesEigenvalues.lean` (docstrings), the
cheat-sheet §2 table, and adds one `conj:` block; every mass and binding number is downstream of
Step 2 *nominally*, but none of them is computed *from* the geometry — they are computed from
`H_n(q)` directly — so **no witness moves**. B adds one probe and one Lean file. C's prune may
edit `lifted-crossing-locality.md` and `vertex-operator-dictionary.md`.

## 4. What this plan does not do

It does not produce the forms `(α, β)` route D2 needs for `∫γ`. Monodromy is holonomy of a
connection, and a connection with the right monodromy is what A conjectures and C would build; the
3-curvature `γ = dβ + ψ_h(α)(β)` needs `β` too, which is a further step beyond any of A–C. Recorded so
the D2 blocker is not mistaken for closed by this tranche.
