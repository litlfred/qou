# qou-qnnq: internal derivation of `A_ω = 3` — sharpening the target to the q-exact symmetry constant

**Date:** 2026-08-02 · **Bean:** `qou-qnnq` (G3 Stokes keystone, internal-derivation leg) ·
**Branch:** `claude/fibre-observable-functor-integer-2026-08-02` · **PR:** #4554 ·
**Tier:** synthesis + formalize-first (Lean, sorry-free) · **Scope:** (a);
nothing fitted; nothing wired; L2 unchanged; no tier change.

## One-line verdict

**Structurally-open (scope-(a)).** No QOU categorical driver supplies a short
structural argument that *forces* the figure-eight Stokes integer `A_ω = 3`
internally. This PR advances the frontier in three honest, non-laundering ways —
(i) a **target sharpening** (below), (ii) a new sorry-free Lean brick connecting
the two existing G3 bricks at the q→0 base point, (iii) a precisely named missing
ingredient — without deriving `3` from the 13 drivers, and without axiomatizing
or fitting it.

## Corpus-first frontier (grep-verified — unchanged from `qou-ujmw`)

Corpus-grep run (`A_omega|A_ω|tau.?functor|fibre.?to.?observable|13 driver|reduced
stokes|W_?-?1|DT.?count|symmetry constant` across `docs/audits docs/coordination
content computations`). The frontier is exactly as `qou-ujmw`
([`2026-08-01-ujmw-aomega-dt-index-derivation.md`](2026-08-01-ujmw-aomega-dt-index-derivation.md))
left it — this PR does **not** re-declare a closed item open:

1. **`A_ω = 3` is a DT/3d-index count, not an assumed value.** GGM Conjecture 4 (a
   *theorem* for `4₁`) identifies the Stokes constants with the rotated 3d-index /
   DT–BPS invariants of `T[4₁]`. The full off-diagonal spectrum is the **pair
   `{3,4}`** (GGM eq 98). Certified through q⁴⁰⁰; q→0 anchor Lean-proved in
   `StokesQZeroDTCount.lean` (`S⁺(0)=[[1,3],[0,1]]`, off-diagonal 3), reduced to the
   single input `W₋₁(0)=[[0,-2],[1,1]]`.
2. **The distinguished reading is the symmetry constant `(S₁₂+S₂₁)/S₁₁`** (`3bp8`
   §4): R1 (raw entry) is excluded by the ϑ-reality bound `A ≥ 2.054`
   (`ThetaRealityBound.lean`); R3 is truncation-invariant and exact
   (`StokesSymmetryConstant.symmetryConstant_const`, sorry-free).
3. **The `3`-from-`disc(ℚ(√−3))=−3` shortcut is refuted, scope-(a)** — a `4`
   co-occurs in the DT spectrum, so a single-scalar discriminant cannot be "the DT
   invariant" ([`2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`](2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md)).
   Single-knot count-matching (`#boundary-parabolic connections = 3`, `π/3` dihedral,
   braid index 3 / crossing number 4) is a **coincidence trap** unless shown *across
   knots* AND *structurally forced* (`5₂`'s geometric block is `3×3`, different).
4. **Internal derivation of `3` from the QOU drivers is OPEN** (`qou-qnnq`,
   `qou-ujmw`). This is the open leg the task targets.

## What this PR adds

### A. Target sharpening — the physics integer is a q-exact structure constant, not a resurgent tail

The genuinely new observation, and the reason it redirects the search:

- The corpus's `A_ω` is the **symmetry-constant** reading R3 (`3bp8` §4), and by
  `StokesSymmetryConstant.symmetryConstant_const` (sorry-free) that reading is
  **q-independent** — its value is *forced* by the GGM symmetry `S₁₂+S₂₁ = 3·S₁₁`
  (eq 65), not observed asymptotically.
- A q-independent quantity **equals its own q→0 limit.** So the entire value of the
  physics-relevant integer is carried by the **decidable** q→0 matrix `S⁺(0)`, which
  `StokesQZeroDTCount.lean` already certifies. There is **no resurgent tail** in the
  integer target: the Gevrey-1 factorial divergence and Borel–Stokes analysis
  (drivers 8/12) govern the *anchor-blind smooth `Im 𝔙 ≈ 0.055`* and the c₃-odd
  *magnitude* — **not** the integer `A_ω`.

**Consequence for the internal-derivation search.** The target collapses to a single
decidable datum:

> Derive `S⁺(0)₁₂ = 3` (equivalently `W₋₁(0)`, equivalently the q→0 3d-index/DT
> count of `4₁`) from a QOU categorical object — a Hecke `H₃` / Wedderburn / Bring
> quantity — **at the semiclassical anchor**, with no resummation.

This is a *simpler and more falsifiable* target than "derive the DT count via the
resurgent Ohtsuki tower": it is an algebraic/combinatorial fact about the q→0 3d
index, and the natural driver home is the **crystal `q→0` limit (driver 13)** and
the **hexagonal/Lobachevsky volume constants (driver 11, `Vol(4₁)=2·Cl₂(π/3)`)**, not
the CS-asymptotics resurgence (driver 12).

The new Lean brick
[`StokesSymmetryConstantQZero.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesSymmetryConstantQZero.lean)
(sorry-free, `lean`-direct exit 0) records exactly this: it discharges the abstract
`symmetryConstant_const` hypothesis at the base point with the concrete certified
`Splus0`, proving the symmetry-constant reading is **exactly 3** at q→0
(`eq65_holds_qzero`, `det_qzero`, `symmetry_reading_qzero`). It is scrupulously
labeled **not** an internal derivation of `3`.

### B. Why the internal derivation still does not close — and the precise missing ingredient

The sharpening removes the *resurgence* obstruction but leaves the *categorical
formula* obstruction, which is the genuine wall:

- The only established route from a QOU object to the q→0 DT count is **numerically
  identical to GGM/GHHR's state-integral computation**: the q→0 3d index
  `Ind_{4₁}(q)` is built from the tetrahedron-index gluing (Neumann–Zagier) data of
  `4₁`'s 2-tetrahedron triangulation. Recomputing it "internally" via the QOU colored
  Jones / state integral **is** re-importing GGM, not a categorical shortcut.
- Every proposed *shortcut* to the integer is either the **refuted disc route** (§3
  above; killed by the co-occurring `4`) or an **unverified single-knot coincidence**
  (§3; fails the cross-knot test the anti-numerology guard requires).

**Precise missing ingredient (the honest gap).** A *combinatorial / categorical
formula* for the q→0 3d-index DT count of a knot in terms of its QOU Hecke/Bring data
(Wedderburn multiplicities of `H_n(q)`, Markov-trace data, Bring embedding) that (i)
reproduces `S⁺(0)₁₂ = 3` for `4₁` **and** (ii) reproduces the companion entry `4` /
survives the cross-knot test on `5₂` (whose block is `3×3`). This is an **open
problem in the categorification of DT / 3d-index invariants** — open in the
DT/state-integral literature itself, not merely a QOU wiring gap. Until such a formula
exists, `A_ω = 3` is *certified as GGM's DT count* (imported, proven-for-`4₁`) but
**not internally derived**.

### C. A tentative re-scoping worth recording (NOT a claim, NOT a derivation)

One subtlety the sharpening exposes, flagged as an **open question** only. The
disc-refutation (§3) targeted the DT *spectrum* `{3,4}`; the physics target is the
narrower symmetry *constant* `3` (a single structure constant, eq 65). Whether the
narrowing re-admits a scalar internal invariant for the symmetry constant
specifically — one that need not reproduce the `4` — is **not resolved here** and
**must not be asserted**: it is subject to the same cross-knot test (does `5₂`'s
symmetry constant match the same scalar rule?), which is unchecked. Recorded as a
question on the bean, not a result.

## Verdict classification (per task rubric)

- **PROVED (sorry-free, Lean, `lean`-direct exit 0):** `StokesSymmetryConstantQZero`
  — the symmetry constant reads exactly `3` at q→0, connecting the two existing G3
  bricks. This is a *formalization step*, not a derivation of `3`.
- **REDUCED (not fully derived):** the internal-derivation target is sharpened from
  "derive the DT count via resurgence" to "derive the decidable q→0 3d-index count
  `S⁺(0)₁₂=3` from Hecke/Bring data (drivers 11/13)".
- **STRUCTURALLY-OPEN (scope-(a)), needs X:** X = a categorical formula for the q→0
  DT count from QOU Hecke/Bring data reproducing `{3,4}` across knots. Currently the
  only route is numerically identical to importing GGM's state integral; that is
  certification, not internal derivation.

## PROVED vs ASSUMED/IMPORTED (explicit separation)

| Statement | Status | Source |
|---|---|---|
| `S⁺(0)=[[1,3],[0,1]]`, off-diag `3` | PROVED (Lean, decidable) | `StokesQZeroDTCount` — but from imported `W₋₁(0)` |
| symmetry const `(S₁₂+S₂₁)/S₁₁ = 3` at q→0 | PROVED (Lean, this PR) | `StokesSymmetryConstantQZero` — from imported `Splus0` |
| symmetry const q-independent | PROVED (Lean, conditional) | `StokesSymmetryConstant.symmetryConstant_const` |
| `A_ω = 3` is the `4₁` DT/3d-index count | **IMPORTED** (GGM Conj 4, theorem for `4₁`) | GGM 2012.00062 |
| `{3,4}` is the DT spectrum | **IMPORTED** | GGM eq 98 |
| `3` derived from QOU's 13 categorical drivers | **OPEN** — not proved, not assumed | `qou-qnnq` |

Nothing here is fitted, axiomatized, or wired to production. Q_β stays c₂-only in
production (canonical-mass guardrail).

## Beans

- **`qou-qnnq`** (existing) — internal derivation of the integer `A_ω = 3` from the
  QOU categorical drivers. Updated with the target sharpening (§A): the target is the
  decidable q→0 3d-index count (drivers 11/13), not the resurgent tail; and the
  tentative symmetry-constant re-scoping question (§C).

## Cross-references

- Lean: [`StokesSymmetryConstantQZero.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesSymmetryConstantQZero.lean) (new),
  [`StokesQZeroDTCount.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesQZeroDTCount.lean),
  [`StokesSymmetryConstant.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesSymmetryConstant.lean).
- Audits: [`2026-08-01-ujmw-aomega-dt-index-derivation.md`](2026-08-01-ujmw-aomega-dt-index-derivation.md),
  [`2026-08-01-fibre-to-observable-bridge-verdict.md`](2026-08-01-fibre-to-observable-bridge-verdict.md),
  [`2026-08-01-3bp8-entirety-and-channel-correctness.md`](2026-08-01-3bp8-entirety-and-channel-correctness.md),
  [`2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`](2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md),
  [`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md).
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
- AGENTS.md §"Axiomatization is NOT a Proof"; §"Before declaring open/refuted"; §"Strict Lean Discipline".

-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062 (eq 60/65/98, Thm 9)
-- Ref: [manuscript] docs/audits/2026-08-01-ujmw-aomega-dt-index-derivation.md
