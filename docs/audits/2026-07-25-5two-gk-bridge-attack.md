# 5₂ GK-bridge attack — the bar-odd channel is the ι-odd antisymmetric off-diagonal (anchor-smooth) (2026-07-25)

**Branch:** `claude/qbeta-5two-gk-bilinear-bridge-2026-07-25`.
**Milestone bean:** `qou-reat` (children `qou-o3cv`, `qou-jtii`, `qou-exes`).
**Scope:** audit only — a structural selection rule + a quantitative anchor-swing
bound. No `c_k` wired; no fit; nothing inverts `Q_β`/CODATA; comparison to
observed only.

This session attacks the **live c₃ bar-odd frontier** with a *distinct angle*
from the B-tranche, coordinated in parallel (owner relaxation 2026-07-18:
measured research-overlap on an open-outcome topic is permitted).

## 1. The wall, precisely (scout summary)

The B-tranche established the bar-odd bridge wall in three rungs
(`docs/coordination/1ppq-qbeta.md`, rows B1 / B1.2 / B1.3):

- **B1 (PR #4226).** The Stokes σ-pair population is **forced zero** on the
  real-`q` ray (at `x₀ = −ln q₀` the σ-pair sectors carry `|e^{iV₁/x₀}| = 5.5e5`,
  overshoot ×4.8e7 vs the O(1) Habiro value ⇒ integer population `n₁=n₂=0`).
  The only O(1) carrier is the real saddle σ₃ (pure phase). A 180-candidate
  pre-registered small-weight scan found no σ₃ assembly bridging to `D_odd`.
  Successor named: the GK bilinear block pairing `Z = Σ M_σσ' B_σ(q)B̃_σ'(q̃)`.
- **B1.2 (branch `claude/gk-bilinear-block-pairing`).** The naked bilinear
  `N := W₋₁(1/q)·B·W₋₁(q)ᵀ`, the dressed Stokes pair `S±`, and their odd/even
  assemblies `O = ½(S⁺−S⁻)`, `Ē = ½(S⁺+S⁻)` were confronted **entry-by-entry**
  (440 pre-registered comparisons) with the four Habiro-face targets
  `F_conv, s(F̄), D_odd, D_even` at gate 1e-6. **0 hits, 0 near-misses.**
  Verdict: no bare-entry bridge; the wall is the state-integral **dressing**
  (Gaussian `√`-prefactor + the `(q/q̃)^{1/8}` unit) **+ λ-row selection**
  (which λ-row of the block basis the Masbaum tail occupies).
- **B1.3 (branch `claude/masbaum-block-row-selection`).** The Masbaum tail
  (built as an exact `u`-series from the integer-Laurent `C_n`; **u-parity
  EVEN** — an integer-`q` series) was tested for membership in the 18-dim
  ℚ-span of the block series `H±_(j,λ)` under every scalar dressing
  `(q;q)_∞^p·q^s`, `p∈−3..3, s∈0..2` (21 exact rational solves). **None in
  span.** Verdict: the tail is a **different vector** in the Habiro module; the
  bridge needs a **module map** (descendant/derivative tower, or the cyclotomic
  expansion), *not* a row choice. Named successors: those module maps.

So the B-tranche frontier, at rung B1.3, points at **module maps that would
bring the tail into the block span** — a search for a different *vector*.

### What "state-integral dressing" and "λ-row selection" mean in the corpus

- **State-integral dressing** = the frame factors that turn the bare block
  bilinear into the Andersen–Kashaev integral value: the Gaussian `e^{−2πiv²}`
  saddle prefactor (a `√`-factor) and the chirality **unit** `R^{1/8} =
  (q/q̃)^{1/8}` (the CS/`u≠0` frame phase). These are *not* free parameters —
  they are fixed by the `4₁` `b=1` closed form (GK 1411.6062 eq 2), which A1
  used as the gate.
- **λ-row selection** = which row/block index `(j,λ)` of the 18-dim GGM block
  basis `H±_(j,λ)` the target datum occupies. B1.3 answered "none of them, as a
  single vector under scalar dressing."

## 2. This session's distinct angle

**The bar-odd home is not a vector — it is an ι-odd antisymmetric off-diagonal
*contraction*, a grade B1.2 (symmetric) and B1.3 (single vector) structurally
could not see.**

The A1 datum (`qbeta-5two-chirality-state-integral`, landed, derived two
independent ways and `4₁`-gated) already writes the frame-reduced state integral
as an explicit chirality split:

```
Ẑ = e^{−iπ/4} Z
  =  R^{1/8}·[ H⁺₁H⁻₁ ]                              (bar-EVEN / index)
  +  i·(−R^{1/8}/2)·[ β·H⁺₂H⁻₀ − β⁻¹·H⁺₀H⁻₂ ]        (bar-ODD / chirality)
```

Writing `p := H⁺₂H⁻₀`, `q := H⁺₀H⁻₂`, the bar-odd channel is the **β-graded
antisymmetric off-diagonal contraction**

```
ω(β,p,q) = β·p − β⁻¹·q .
```

Under the **amphichiral involution** `ι:(β,p,q) ↦ (β⁻¹,q,p)` (swap the
off-diagonal products; invert the cusp modulus `β↔β⁻¹`, the bar action
`τ↦−τ̄`), `ω` is **ι-odd** while the bar-even companion `s(β,p,q)=β·p+β⁻¹·q` is
**ι-even**.

This reframes the two walls: B1.2's symmetric bilinear and B1.3's single
span-vectors are **ι-even / ι-fixed objects**, and on the ι-fixed locus `ω`
*vanishes identically*. They searched `ω`'s zero locus — that is *why* they
returned nothing, structurally, independent of dressing or row.

### Formalized (Lean, sorry-free, generic field)

`content/quantum-observable-universe/lean/QOU/QBeta/BarOddAntisymOffDiagonal.lean`
(`lean`-direct exit 0):

| Declaration | Content |
|---|---|
| `omega`, `sEven` | the ι-odd contraction and its ι-even companion |
| `omega_iota_odd` | `ω(β⁻¹,q,p) = −ω(β,p,q)` — ι-oddness |
| `sEven_iota_invariant` | `s(β⁻¹,q,p) = s(β,p,q)` — the B1.2/B1.3 search grade is ι-even |
| `omega_of_iotaFixed`, `omega_zero_on_iotaFixed` | `ω=0` on the ι-fixed (= amphichiral = symmetric-search) locus — reproduces `V(4₁)_odd = 0` |
| `omega_ne_zero_imp_chiral` | a nonzero bar-odd datum **forces** a chiral knot — the structural reason the frontier needed `5₂`, not `4₁` |

Base ring is a generic `Field F`; the substrate→archimedean wall is not crossed
(no ordering, no `Real.*`, no numerical `q₀`) — §7c-clean.

## 3. The decisive number — the bar-odd home is ANCHOR-SMOOTH

Probe `computations/qbeta/qbeta_5two_barodd_antisym_offdiagonal_probe.py`
(witness `qbeta-5two-barodd-antisym-offdiagonal.witness.json`, 4/4). It consumes
**committed** A1/A2 witness data only — no state-integral re-run, no wide scan:

- **T1 ι-odd flip (probe↔Lean tie).** On the committed block products,
  `ω(β⁻¹,q,p) = −ω(β,p,q)` to 0 residual.
- **T2 antisymmetric-structure gate.** `N_odd = ½(N − Nᵀ)` of the committed A2
  assembly matrix reproduces the committed odd assembly to 1.8e-15 — the
  block-level home of the off-diagonal contraction.
- **T3 anchor-swing bound (decisive).** The committed A1 bar-odd datum `Im Ẑ`
  swings between the **muon** and **proton** `q₀` anchors by

  | quantity | swing (proton vs muon) |
  |---|---|
  | bar-odd home `Im Ẑ_odd` | **4.56 ppm** |
  | bar-even home `Re Ẑ_even` | 7.63 ppm |
  | **c₃ (target)** | **≈ 34700 ppm (3.47 %)** |

  Ratio `(c₃ swing)/(bar-odd home swing) ≈ 7.6×10³`.

The c₃ cross-anchor swing (3.47 %) is the established corpus figure
(`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`); it is
*not* re-derived here, and nothing here inverts `Q_β`/CODATA.

## 4. Verdict — scope-(a), and the residual re-localized

**Scope-(a).** The ι-odd antisymmetric off-diagonal `ω` is the
**provably-correct bar-odd HOME** that B1.2/B1.3 structurally missed (wrong
ι-grade), but it is **anchor-smooth** (≈ 4.6 ppm) while c₃ is a percent-level
swing. Therefore `ω`, *alone*, **cannot realize the c₃ swing.** This is a
scope-limited negative on the *magnitude/anchor-behavior* of this construction —
**not** a structural exclusion of the off-diagonal ingredient (which is proved
correct and permanent).

**Constraint on the B-tranche's named successors.** B1.3's module-map
successors (descendant/derivative tower, cyclotomic expansion) all move *within*
the block/Habiro basis — an anchor-smooth home. Any such object inherits the
~ppm anchor-smoothness (the same `no_anchor_invariant_realizes_swing` prune that
binds `V(5₂)_odd`, `Im 𝔏_odd`, `D_odd`). **Selecting a smoother object cannot
close a percent-level swing.** The swing must come from the anchor-**dependent**
meridian-holonomy deformation `q₀ ↦ u` — `CuspShapeBarParity`'s "open link", the
Neumann–Zagier `CVol(u) = Vol − (τ/4)u² + …` — not from a row/dressing/module
choice on the undeformed block basis.

This does **not** refute the module-map program; it bounds it: the module map
must carry an anchor-dependent (holonomy-deformation) factor, or it is
anchor-smooth and cannot be c₃. The genuinely open piece is the §4e
quantum-modularity / meridian-holonomy identification (already flagged by the
`jones-vs-stateintegral-barodd-crosscheck` witness: `Im(𝔏_odd)/bar-odd(J) ≈ 108`,
no pre-stated normalization).

## 5. What was proved vs the honest residual

- **Proved (Lean, sorry-free):** the bar-grade selection rule — the bar-odd
  channel is the ι-odd antisymmetric off-diagonal contraction; it vanishes on
  the ι-fixed/amphichiral/symmetric-search locus; a nonzero bar-odd datum forces
  chirality.
- **Measured (committed-data probe, scope-(a)):** the bar-odd home is
  anchor-smooth (4.56 ppm) — ~7600× too smooth to be the 3.47 % c₃ swing.
- **Honest residual (open):** the anchor-dependent factor. No anchor-smooth
  object — vector, symmetric bilinear, antisymmetric contraction, or scalar-
  dressed module image — realizes the swing; the missing ingredient is the
  holonomy deformation `q₀↦u`, which is exactly the open §4e quantum-modularity
  identification. Not closed this session; no fit attempted.

## 6. Artifacts

- Probe: [`computations/qbeta/qbeta_5two_barodd_antisym_offdiagonal_probe.py`](https://github.com/litlfred/qou/blob/claude/qbeta-5two-gk-bilinear-bridge-2026-07-25/computations/qbeta/qbeta_5two_barodd_antisym_offdiagonal_probe.py)
- Witness: [`computations/qbeta/qbeta-5two-barodd-antisym-offdiagonal.witness.json`](https://github.com/litlfred/qou/blob/claude/qbeta-5two-gk-bilinear-bridge-2026-07-25/computations/qbeta/qbeta-5two-barodd-antisym-offdiagonal.witness.json)
- Lean: [`content/quantum-observable-universe/lean/QOU/QBeta/BarOddAntisymOffDiagonal.lean`](https://github.com/litlfred/qou/blob/claude/qbeta-5two-gk-bilinear-bridge-2026-07-25/content/quantum-observable-universe/lean/QOU/QBeta/BarOddAntisymOffDiagonal.lean)
- Session intent: [`docs/coordination/2026-07-25-5two-gk-bilinear-bridge.md`](https://github.com/litlfred/qou/blob/claude/qbeta-5two-gk-bilinear-bridge-2026-07-25/docs/coordination/2026-07-25-5two-gk-bilinear-bridge.md)
