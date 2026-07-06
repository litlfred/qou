# q-heat-kernel / q-Bessel as the keystone geometric realization — lead + precheck (2026-06-20)

**Branch:** `claude/kind-ptolemy-acladr`
**Status:** LEAD (not a closure). Owner-seeded direction + one formalize-first precheck.
**Discipline:** corpus-grep first (the q-Bessel infra already exists); formalize-first
(cheap structural check before any owner-gated DG); critical-distance.

## The owner's lead

Use a **q-heat kernel** and the **q-Bessel equation of the second kind** as the analytic
engine for the keystone's open *geometric realization* — the object whose S¹-equivariant
index reproduces the q-Plancherel weights `W_λ = d_q(λ)²/[n]_q!`
([`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md), the single open
object). Plus a follow-up: the second-kind solution carries a "quadratic action" usable as a
**mass/binding correction** (queued as a separate exploration bean — see below).

## Why this is on-axis (not an archimedean re-pitch)

1. **An equivariant index *is* a heat-kernel supertrace** (McKean–Singer:
   `ind_{S¹}(D) = Str(g·e^{-tD²})`, `t→0`). So a q-heat kernel is literally the analytic
   object the keystone names — the `keystone-plancherel-target-clarification` audit already
   flagged `d_q²/[n]!` as *"the natural object for an equivariant-index / heat-kernel argument."*
2. **The q-Bessel infra is already in the corpus** (do NOT re-walk it):
   [`2026-06-13-reeb-phase-qbessel-identification.md`](2026-06-13-reeb-phase-qbessel-identification.md)
   establishes Hahn–Exton q-Bessel = `E_q(2)` matrix coefficients (Vaksman–Korogodsky 1989,
   Koelink 1994), satisfying a **second-order q-difference equation** with three-term
   contiguity, and the `SU_q(2)→E_q(2)` contraction = little-q-Jacobi → q-Bessel. The c_k
   ladder kernel was already identified as the q-Bessel q-difference operator (#1839/#1880).
   The NEW step here is connecting that infra to the **keystone q-Plancherel target**, which
   the 2026-06-13 audit did not address (it was about the Q_β c_k tower).
3. **"Second kind" is the orbifold-fixed-point choice.** The `2I` icosahedral action has fixed
   points → orbifold singularities; Atiyah–Bott localizes the index there, and the radial heat
   kernel near a cone tip picks the **second (singular) solution** of the q-Bessel q-difference
   equation. Specifying second kind is the correct boundary behaviour, not a free choice.

## The formalize-first precheck (run, this PR)

[`scripts/keystone_qbessel_plancherel_precheck.py`](scripts/keystone_qbessel_plancherel_precheck.py)
(exit 0) checks the **necessary structural preconditions** for `W_λ` to be a heat-kernel /
equivariant-index measure at `q_0 = 1.10997858`, `λ ⊢ 5` (balanced quantum integers,
q-hook-length q-dimensions):

| Precondition | Result |
|---|---|
| **P2** conjugation symmetry `W_λ = W_{λ'}` (Plancherel / Hodge-★ hallmark an index must respect) | ✅ **PASS** (exact) |
| **P3** reproduces the published audit table (`keystone-plancherel-target-clarification`) | ✅ **PASS** (max diff 4.6e-6, audit rounded to 5 dp) |
| **P1** probability measure `Σ_λ W_λ = 1` | ⚠️ **FAIL** — `Σ = 0.98222` |

**The P1 finding is real, not a bug:** the audit's *own* table sums to 0.98223 too. So the
form `d_q²/[n]_q!` as written is **sub-normalized by ~1.78% at q_0** — it is NOT a probability
measure. (`Σ_λ d_q(λ)² = [n]_q!` is a *false* identity at generic real `q>1`; it holds only at
`q→1` where `d_q→dim` and `[n]_q!→n!`.)

## What the precheck means for the lead

- **Not refuted.** The shape + the conjugation symmetry an equivariant index must respect are
  present (P2, P3). The q-Bessel/heat-kernel route survives the cheap gate.
- **Sharpened.** A genuine index realization must *also* reproduce the **q-partition-function**
  `Z = Σ_λ d_q²/[n]! = 0.98222` as the heat-kernel trace (equivalently, use the Z-normalized
  measure `W_λ/Z`). The **mass defect `1 − Z = 0.0178`** is now a concrete geometric quantity
  the construction must explain — a sharper target than "reproduce W_λ."
- **Open below this (owner-gated DG, unchanged):** (a) the radial-part identity — is the
  q-Bessel (2nd-kind) orthogonality measure proportional to `W_λ` at the partition points? and
  (b) does a manifold carrying the spatial-SO(3) Reeb S¹ exist whose transverse heat kernel has
  that radial part, with `W_λ = W_{λ'}` arising from a Hodge-★ / Poincaré-duality symmetry
  rather than as an input.

## Corpus-grep trail (what already exists vs what is new)

- **Exists** (do not re-walk): the q-Bessel = `E_q(2)` identification, the J_ν (rotation) / I_ν
  (growth) dichotomy, the c_k q-difference-kernel = q-Bessel-operator finding — all in the
  2026-06-13 audit + `QOU/QBeta/{ReebTowerJacobiAnger,QBesselContiguityRecurrence}.lean`.
- **New** (this lead): the bridge from that infra to the **keystone q-Plancherel
  geometric-realization** target; the precheck's sub-normalization finding; the **second-kind /
  quadratic-action → binding-correction** direction (queued, not in the existing J/I audit).

## References (all already in `content/schema/references.ts`)

- `vaksman-korogodsky-1989` — *q-analogues of Bessel functions = E_q(2) matrix coefficients*,
  Soviet Math. Dokl. **39** (1989) 173–177.
- `koelink-1994` — *The quantum group of plane motions and the Hahn–Exton q-Bessel function*,
  Duke Math. J. **76** (1994) 483–508, doi:10.1215/S0012-7094-94-07617-0. (The q-Bessel
  **second-order q-difference equation**.)
- `koelink-swarttouw-1994` — *On the zeros of the Hahn–Exton q-Bessel function*, J. Math. Anal.
  Appl. **186** (1994) 690–710, doi:10.1006/jmaa.1994.1330. (q-Hankel transform / orthogonality.)
- `koornwinder1990` — *Orthogonal polynomials in connection with quantum groups*, NATO ASI C
  **294**, Kluwer, 1990, 257–292. (SU_q(2)→E_q(2) contraction → q-Bessel.)
- `gasper-rahman` — *Basic Hypergeometric Series*, 2nd ed., CUP 2004,
  doi:10.1017/CBO9780511526251. (q-Bessel normalization.)

Note: Noumi–Mimachi and Vaksman–Soibelman (quantum-sphere harmonic analysis) are the adjacent
classical-template sources; they are not yet in `references.ts` — add via the `ref()` builder if
the lead advances to content.
