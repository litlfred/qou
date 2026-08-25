# Branch selection: finite S₃ cover monodromy (W1) vs. the theta Birkhoff matrix of the C1 module (W2) (2026-08-01)

**Branch:** `claude/qdiff-prolongation-scaffold-2026-08-01` (PR #4449). **Feeds:** the W1
wall of the C1↔SW leg (bean `qou-d8de`). **Analysis + literature mapping. Contains a
self-correction (v2) of an earlier over-reach; see §Correction.**

## Sources (owner upload commit 715ccc8, with citation corrections)

The owner uploaded five PDFs to `library/` for this front. **Two of my earlier arXiv
IDs were wrong** and are corrected here:

- `0104249v1.pdf` is **Zudilin, "Irrationality of values of the zeta-function"** — NOT
  Sauloy (my `math/0104249` citation was wrong; unrelated to q-difference connection theory).
- `9408045v1.pdf` is **Barcelos-Neto–Dargam, "Constrained analysis of topologically
  massive gravity"** — NOT Etingof (my `hep-th/9408045` citation was wrong).
- `AFST_2007_6_16_3_665_0.pdf` = **van der Put–Reversat, "Galois theory of q-difference
  equations"**, Ann. Fac. Sci. Toulouse XVI-3 (2007) 665–718 — genuine, relevant.
- `Equations_aux_q-differences.pdf` = **Di Vizio–Ramis–Sauloy–Zhang, survey** (French) —
  genuine; carries the Birkhoff connection-matrix recipe (§3.3, p. 34).
- `Birkhoff-GeneralizedRiemannProblem-1913.pdf` = **Birkhoff 1913** — genuine.

## The DRSZ recipe (survey p. 34), stated correctly

For a **Fuchsian** q-difference system `σ_q Y = A(x) Y` with `A(0), A(∞) ∈ GLₙ(ℂ)`, the
canonical local solutions are `X^{(0)} = M^{(0)} e_{q,A(0)}` (meromorphic on `ℂ`) and
`X^{(∞)} = M^{(∞)} e_{q,A(∞)}` (on `S∖{0}`), where `M^{(•)}` is the regular part
(`σ_q M = A M A(•)⁻¹`, `M(•)=I`) and `e_{q,A}` is the q-character of the exponents (built
from `θ_q`, `e_{q,c}(qx)=c·e_{q,c}(x)`). The **Birkhoff connection matrix**

  `P(x) = (X^{(∞)}(x))⁻¹ X^{(0)}(x)`

is meromorphic on `ℂ*`, `σ_q`-invariant (**elliptic**), with **Jacobi-theta-quotient
entries** — the q-analogue of the monodromy matrix, but not complex-valued.

## Correction (v2) — two different objects; do not conflate them

An earlier version of this doc claimed the **branch-selection datum** "which sheet `Yᵢ`
continues `X`" is this theta-valued Birkhoff matrix. **That was an over-reach.** The
Birkhoff matrix is the invariant of a genuine (transcendental) q-difference **module**.
The SW **sheets are algebraic** (roots of the cubic `C_z(X)`), and they are **distinct at
the fixed points of `z↦qz`**:

- at `z=0`: `C₀(X) = (X+1)(X²+1)`, roots `{−1, i, −i}` — distinct; `disc_X C_z|₀ = −16 ≠ 0`,
  so `z=0` is **not** a branch point;
- at `z=∞`: `C(z, zw)/z³ → (w+1)(w²+1)`, so `X ~ z·{−1, i, −i}` — distinct.

Hence the sheet continuation is **locally single-valued at both fixed points**, and the
only obstruction to a global single-valued branch is the **finite covering monodromy**:
the representation `ρ : π₁(ℂ* ∖ {6 branchSextic zeros}) → S₃`, restricted to how the
`z↦qz` orbit winds around the 6 branch points. **This is finite (S₃), not theta-valued.**
The (−1)ⁿ ramification parity proved on main (`Brings.RamificationParityMonodromy`) is the
**sign character** of exactly this `ρ`.

**So the two walls carry different transcendence:**

| Wall | Object | Monodromy | Type |
|---|---|---|---|
| **W1 branch selection** | algebraic sheet cover of `C_z(X)` | `ρ : π₁ → S₃` around 6 branch pts | **finite** |
| **W2 symbol** | the C1 q-difference **module** (RSZ route-A `L1`) | Birkhoff matrix `P(x)` | **theta-valued** |

The deformation-gap transcendence (`dc₃/dq ≈ 4.7×10⁶`) and the FKV/Faddeev `Φ_b` theta
family live at the **W2/module** level (C1's connection matrix), **not** at W1. W1 is a
finite combinatorial-topological problem — more tractable than the earlier claim implied.

## Honest next steps (re-scoped)

- **W1 (finite):** compute `ρ : π₁(ℂ*∖{6 pts}) → S₃` for the color-cubic cover, and the
  `z↦qz` orbit's winding, to decide when a global single-valued branch exists. Finite;
  builds on `RamificationParityMonodromy`. This is the genuine W1 target — not theta.
- **W2 (theta):** compute the Birkhoff matrix `P(x)` of the C1 module `L1` via the DRSZ
  recipe. Caveat: RSZ route-A found `L1` is Fuchsian at `0` but **slope-½ irregular at ∞**,
  so the pure-Fuchsian recipe gives the `0`-side canonical solution; the `∞`-side needs the
  q-Gevrey/Stokes treatment (RSZ Astérisque 355). Partial (0-side) is tractable; the full
  matrix needs Stokes.

Neither is closed here. This doc corrects the object identification and re-scopes both
walls; it does **not** mark W1 closed. No new Lean; no fit; nothing wired.

-- Ref: [manuscript] docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md (W1)
-- Ref: [manuscript] library/equations-aux-q-differences/Equations_aux_q-differences.pdf (DRSZ survey §3.3, Birkhoff matrix)
-- Ref: [manuscript] library/afst-2007-6-16-3-665-0/AFST_2007_6_16_3_665_0.pdf (van der Put–Reversat, q-difference Galois)
