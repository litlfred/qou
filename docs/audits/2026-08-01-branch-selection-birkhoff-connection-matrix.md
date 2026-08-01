# Branch selection on Σ is the Birkhoff connection matrix — transcendental, theta-valued (2026-08-01)

**Branch:** `claude/qdiff-prolongation-scaffold-2026-08-01` (PR #4449). **Feeds:** the W1
wall of the C1↔SW leg (bean `qou-d8de`). **Analysis + literature mapping — converts the
"which sheet continues X" wall into a cited transcendental invariant; no new Lean here.**

## The wall, localized

The five W1 Lean bricks on #4449 reduce the q-difference prolongation `D_q` on the color
spectral curve `Σ = {C_z(X)=0}` to a single obstruction. From
`ColorCurveQPartials.qPartialZ_on_curve`: on `Σ`, the q-shift defect is
`Δ_q^z C(X,z) = C_{qz}(X)`, and from `ColorCurveSheets.defect_eq_shifted_sheet_product`
it factors as `(X−Y₁)(X−Y₂)(X−Y₃)` over the three sheets `Yᵢ` of `C_{qz}`. So a genuine
`D_q` must **select which sheet `Yᵢ` continues `X`** under `z ↦ qz`, single-valuedly and
globally.

## What the literature says this object is

The three sheets of `Σ` are the solution space of a **rank-3 first-order q-difference
system** whose characteristic polynomial is `C_z(X) = [1]_z X³ + [2]_z X² + [3]_z X + [4]_z`
(the q-integer form, `ColorCurveQIntegerForm`). "Which sheet continues `X`" is the
**monodromy** of this q-difference module — and for q-difference equations the monodromy
is not a homotopy representation but the **Birkhoff connection matrix** `P(x)` relating the
canonical solution bases at `0` and `∞`:

- **van der Put–Singer** (LNM 1666, 1997): the difference-Galois group *is* this monodromy;
  a single-valued algebraic branch would require a **trivial/reducible** Galois action.
- **Sauloy** (Ann. ÉNS 36, 2003; [math/0104249](https://arxiv.org/abs/math/0104249)) and
  **Birkhoff** (1913): the connection matrix `P(x)` is `q`-elliptic (`P(qx)=P(x)`), so its
  entries live on the elliptic curve `ℂ*/qℤ`.
- **Etingof** ([hep-th/9408045](https://arxiv.org/abs/hep-th/9408045)): the entries of
  `P(x)` are explicit **Jacobi theta quotients** `θ(·)/θ(·)`.
- **Ramis–Sauloy–Zhang**, Astérisque 355 (`uploads/0903.0853v3.pdf`): the local wild part
  (slopes / q-Gevrey Stokes) at the ramified singularities — already used in the corpus
  for the C1/GGM slope comparison (`2026-07-20-qlift-routeA-rsz-invariants.md`,
  `ThetaSlopeArithmetic.lean`).

## Consequence — the wall is transcendental *by theorem*, not by difficulty

The connection matrix is **generically transcendental** (theta-valued): a single-valued
*algebraic* branch selection exists only on the measure-zero locus where `P(x)` degenerates
to a scalar/permutation. So:

- The branch datum `D_q` needs is **not a rational function** of `(X,z)` — it is a
  theta-valued connection matrix. This is why the calculus/algebra approach (the five
  bricks) *localizes* but cannot *close* W1.
- **This matches the deformation-gap audit** (`2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md`):
  the `dc₃/dq ≈ 4.7×10⁶` near-singularity and the excluded smooth deformation are the
  *same* transcendence — the `z(q₀)` argument map is the evaluation of a theta-valued
  connection datum, not an algebraic one.
- It also **connects to existing repo theta structure**: the FKV/Faddeev `Φ_b` modular
  double (`FaddeevModularDouble`, `PhiBProd*`) is built from exactly these Jacobi theta
  quotients. The branch-selection connection matrix and the Faddeev theta are the same
  transcendental family — a genuine structural link between the A_ω leg and the c₃ wall.

## Honest status update (per "conditional-proved ≠ premise-established")

W1's residual is **not** "open geometry of unknown type." It is a **specific, cited
transcendental invariant**: the Birkhoff connection matrix of the rank-3 q-difference module
on `Σ`, with theta-quotient entries. What remains is *formalization/derivation* of that
matrix — a theta-function computation, not an algebraic one — and it is honestly beyond a
Lean session (Mathlib has no q-difference module / Birkhoff-connection theory). This does
**not** mark W1 closed; it upgrades the wall from "open" to "transcendental invariant,
literature-identified," and pins the exact object.

**Next honest step (if resumed):** compute the connection matrix `P(x)` for the specific
rank-3 module of `C_z(X)` symbolically (theta quotients, via Sauloy's Fuchsian recipe), and
check whether its degeneration locus meets the substrate `q₀` — the q-difference analog of
the RSZ route-A slope computation, one level up (connection matrix, not just Newton polygon).

-- Ref: [manuscript] docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md (W1)
-- Ref: [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (local q-difference classification)
