# α_EM B2 τ-identification — attack options (the last open input to `1/(8π)`)

**Date:** 2026-07-24 · **Axis:** α_EM per-loop measure (the single load-bearing wall) ·
**Tier:** research attack-plan (no new result; develops routes) · **Discipline:**
`1/(8π)` stays a phase-4 identification; the τ-functor is NOT constructed here; no
`TauRhoHodgeLift` instance is fabricated.

## The target (what is left)

Over #4151 + #4154 the B2 per-loop wall was stripped of every linear-algebra residue:

| premise ingredient | status |
|---|---|
| positivity / PSD | **unnecessary** (#4151) |
| reality + symmetry | **discharged Markov-side** — `bilinM_isSymm` + real `q₀` (#4154) |
| **τ-identification** `W = complexify(Markov Gram at q₀)` | **the SOLE remaining open input** |

The τ-identification asserts: the α_EM loop weight `W` on `H^{1,0}(Bring)` equals the
`complexify` of the canonical Markov channel weight (the seminormal Gram) at the
substrate `q₀`, transported by the archimedean fibre functor `τ`. Discharging it
legitimately instantiates `TauRhoHodgeLift` and lands `1/(8π)`.

## The keystone fact that shrinks the problem

`H^{1,0}(Bring) = std`, the **irreducible** 4-dim standard S₅-representation
(#2701, corpus). `std` is defined over `ℚ` (real / rational type ⇒ **absolutely
irreducible over ℝ**). By **Schur's lemma**, the space of S₅-**invariant symmetric
bilinear forms** on an absolutely-irreducible real representation is
**1-dimensional**. Both candidate forms on `std` are S₅-invariant and symmetric:

- the **Hodge metric** on `H^{1,0}(Bring)` — S₅ = Aut(Bring) acts by isometries on
  the period lattice;
- the **τ-image of the Markov Gram** — *if* it is S₅-equivariant on `std`.

So (modulo the equivariance premise) they are **proportional**:
`τ(Markov Gram) = c · Hodge Gram`, `c` a scalar. This converts "construct the whole
τ-functor and prove it carries ρ to Hodge conjugation" into **"prove τ-equivariance
on one irrep + fix one scalar `c`."** That is the leverage the attack plan is built
around.

## Attack options (priority order)

### B — Schur-uniqueness reduction  **[PRIMARY — highest leverage]**
Formalize: *invariant symmetric bilinear forms on an absolutely-irreducible
representation are unique up to a scalar* (Schur). Instantiate at `std`; conclude
`τ(Markov Gram) ∝ Hodge Gram`. **Open sub-pieces after B:** (i) the τ-image is
S₅-equivariant on `std` (should follow from the Bring-automorphism action commuting
with `τ` — the seminormal form's `bilinM_rep_invariant` is the Hecke-side
equivariance); (ii) the scalar `c` (fixed by the trace/`a₀` normalization, or by one
matrix entry — Option C). **Lean core:** Schur uniqueness of invariant forms;
Mathlib has `Module.End` Schur (`LinearMap.isUnit_or_eq_zero` on irreducibles) —
adapt to the symmetric-bilinear-form space. **Honest caveat:** a *reduction*, not an
automatic closure; but a large shrink. This is NOT fabrication — it derives
proportionality from irreducibility, it does not assume the identification.

### C — Explicit numerical pin / falsification  **[SUPPORT for B]**
Compute the **Hodge Gram** of `H^{1,0}(Bring)` from the Braden–Northover period
matrix `τ₀·C` (uploaded, registered), and the **Markov Gram** on the `std` block at
`q₀` (Hoefsmit seminormal / `WenzlSchurElement`). Verify proportionality numerically
and **extract `c`**. Double duty: confirms B's proportionality *and* falsifies the
equivariance premise if they are not proportional. Concrete probe (Hecke wheel +
period matrix); anti-laundering: report the ratio, do not tune it.

### A — Wedderburn-block identification  **[SUPPORT / feeds C]**
Pin the exact Wedderburn block of `H_n(q)` carrying `std` (partition `(4,1)`, the
relevant `n`), and compute its Markov weight matrix explicitly (Hoefsmit branching).
Supplies the concrete `Markov Gram` object that B references abstractly and C
evaluates.

### E — `MarkovTrace` general-`n` instance  **[MECHANICAL — unblocks the reduction]**
`TauFunctorReduction` threads `[MarkovTrace]` with a general-`n` instance gap; land
the Ocneanu-cyclicity bricks (#4126 / #4110) to close it. Does not close the
identification, but removes a threaded hypothesis blocking the reduction's F-laws.

### D — Full τ-functor construction  **[FALLBACK — multi-session]**
Construct the archimedean fibre functor on the relevant subcategory and prove it
carries the Markov weight to the Hodge metric. The complete categorical route; needed
only if B's equivariance premise cannot be established more cheaply. Large; last
resort.

## Recommended sequencing

**B → C → A → E → D.** B is the structural near-closure (potential proportionality
theorem); C pins/falsifies the scale immediately with data already in the corpus
(Braden–Northover period + Hoefsmit); A supplies the concrete block; E is a
mechanical unblock runnable in parallel; D is the fallback if equivariance resists.

## Scope discipline (STRICT)

No τ-functor is constructed here and no `TauRhoHodgeLift` instance is registered.
Option B derives proportionality from *irreducibility* (Schur) — it does not assume
the identification (that would be laundering). The scalar `c` and the equivariance
premise are stated as the open sub-pieces, not papered over. `1/(8π)` stays phase-4.

## Cross-references

- Wall-weakening (real+symmetric, PSD unnecessary): PR #4151 (`LoopWeightRealSymmReduction.lean`)
- Markov-side discharge (symmetric form ⇒ premise): PR #4154 (`MarkovGramRealSymm.lean`), `SpechtIrreducible.bilinM_isSymm`
- `H^{1,0}(Bring) = std` irreducible: [`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md) (#2701)
- Braden–Northover period matrix `τ₀·C`: [`[braden-northover-2012]`], `BringEllipticFactor.lean`
- Schur-element / Wenzl infra: `QOU/MathlibExt/WenzlSchurElement.lean`
- B2 interface + reductions: `QOU/Archimedean/{TauRhoHodgeLiftInterface,HodgeGramLift,LiftFromReality,TauFunctorReduction}.lean`
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)

## Update 2026-07-25 — sub-piece (ii): the generator-intertwiner framing was WRONG (corrected)

**Correction of the earlier same-day claim.** An earlier version of
`TauS5EquivarianceReduction.lean` (merged in #4182) framed sub-piece (ii) as a
*generator*-level intertwiner `ρH s · P = P · ρS s` between the Hecke action and
the S₅ action on `std`, and claimed `tauImage_proportional_hodge` *reduced* (ii).
**That was wrong: the generator-intertwiner is UNSATISFIABLE at `q₀ ≠ 1`.**

- Hecke generator `σ₁` on `std` has eigenvalues `q₀,q₀,q₀,−q₀⁻¹` → trace `3q₀ − q₀⁻¹ ≈ 2.43`.
- An S₅ transposition on `std` has eigenvalues `1,−1,1,1` (fixed-points − 1) → trace `2`.
- Differing spectra ⇒ no conjugating `P` (now a sorry-free lemma
  `intertwiner_trace_eq`: an intertwiner forces `trace ρH s = trace ρS s`). `2.43 ≠ 2`.

So the old conditional was true-but-**vacuous** (per "conditional-proved ≠
premise-established") — NOT a reduction of (ii). The correct τ-correspondence is
the **Tits `*`-algebra iso** `H₅(q₀) ≅ ℂ[S₅]` on the `(4,1)` block (a
Skolem–Noether conjugator sending `σᵢ` to a *non-generator* element), which is
**not** yet formalized. Sub-piece (ii) is honestly **OPEN**.

What the (corrected) file genuinely provides, sorry-free: `invariantForm_pullback`
(true general linear algebra), `intertwiner_trace_eq` (the obstruction),
`tauImage_proportional_hodge` (general-`P` assembly, explicitly flagged as **not**
a reduction of (ii)), and — the **correct, satisfiable** reduction —
`HeckeSideS5Symmetry` + `markovGram_transports_to_hodge`: an S₅ action `ρS'` **on
the Hecke space** leaving the Markov Gram invariant, conjugate to the geometric
S₅; since `ρS'` and `ρS` share the `(4,1)` character there is **no** trace
obstruction, so this premise CAN hold. A non-vacuity probe
(`alpha_em_b2_hecke_s5_symmetry_probe.py`) exhibits `ρS'` for the actual `(4,1)`
block and verifies all four structure fields (Markov-invariance ~1e-40,
character match `trace ρS' = trace ρS` **exactly 0**) — confirming the reduction
is genuine, not vacuous. The residual open input is now the **canonical**
(q-deformation-pinned) Tits `*`-iso, `T = τ`, of which the probe's `T` is only an
arbitrary congruence representative.

**Gate (a) for `|c|` — CLOSED.** The explicit period matrix *is* in the corpus
uploads: Braden–Disney-Hogg *Bring's Curve: Old and New* ([arXiv:2208.13692](https://arxiv.org/abs/2208.13692),
Thm 2.12, citing [Riera–Rodríguez 1992](https://doi.org/10.2140/pjm.1992.154.179),
`library/arxiv-2208.13692v1/2208.13692v1.pdf` + `library/the-period-matrix-of-bring-s-curve-1hik02mwva/the-period-matrix-of-bring-s-curve-1hik02mwva.pdf`)
gives the Riemann matrix `τ_B = τ₀·M_S`, `M_S = 5·Id₄ − 𝟙` (eigenvalues `(5,5,5,1)`,
positive-definite), `τ₀ = −0.5 + 0.186676i`. So the canonical Hodge Gram is
explicit: `G_Hodge = Im(τ₀)·M_S`. `|c|` is therefore no longer gated on the period
data — it is gated **only** on the Tits `*`-iso (sub-piece ii), since `|c|` compares
the Markov-trace and principal-polarization normalizations, which live on the two
structures the Tits iso relates.

**Corrected wall state:**

| ingredient | status |
|---|---|
| Schur proportionality from commutant-scalar | PROVED (#4160) |
| (i) commutant scalar from irreducibility | PROVED (#4182, `MatrixSchurCommutant`) |
| symmetric / real type of the Markov Gram | PROVED (#4154, `MarkovGramRealSymm`) |
| sign of `c` (positive) | PROVED (Hodge+Markov both pos-def, #4182 item 2) |
| explicit Hodge Gram `Im(τ₀)·M_S` (period data) | AVAILABLE (BDH Thm 2.12 / RR92; gate (a) closed) |
| (ii) reduction structure (satisfiable) | PROVED + shown satisfiable (`HeckeSideS5Symmetry` / `markovGram_transports_to_hodge`; probe confirms non-vacuity) |
| **(ii) the CANONICAL Tits `*`-iso `T = τ`** | **OPEN** — the generator-intertwiner is obstructed (`intertwiner_trace_eq`); a satisfying `T` exists (probe), but pinning the deformation-canonical one (`= τ`) is not yet formalized |
| `|c|` magnitude | **OPEN** — gated on the canonical (ii) alone (an arbitrary congruence gives a convention-dependent scalar) |

No intertwiner / `TauRhoHodgeLift` instance for the actual τ is registered;
`1/(8π)` stays a phase-4 identification; nothing is wired.

## Update 2026-07-25 (2) — the seminormal→Young Tits deformation T(q), built explicitly

`alpha_em_b2_tits_deformation_probe.py` constructs the deformation and tests the
`*`-isometry numerically (dps=40, no fit):

- The Hoefsmit seminormal rep `ρ_H^q(σᵢ)` of `(4,1)` deforms continuously to
  Young's rep as `q→1` (σ₁ eigenvalues `q,q,q,−q⁻¹ → 1,1,1,−1`; verified across
  `q ∈ {1.0001, 1.01, 1.1, q₀}`).
- **`T(q) = diag(√(g_i(1)/g_i(q)))`** (`g_i` = the diagonal seminormal Gram
  entries) is an explicit, deformation-continuous (`→Id` at `q=1`, residual
  `3e-9`), **`*`-compatible Tits conjugator**: exact `*`-isometry
  `Tᵀ·G(q₀)·T = G(1)` (residual `4e-41`) and `T⁻¹·ρ_H^{q₀}·T` exactly
  `G(1)`-self-adjoint (residual `9e-41`). So `φ = ρ_S⁻¹ ∘ conj(T) ∘ ρ_H` is a
  genuine `*`-algebra iso `H₅(q₀) ≅ ℂ[S₅]` on the block.
- **Reconciliation with the (ii) obstruction (#4199):** `T` is *not* a
  generator-intertwiner — `T⁻¹·ρ_H^{q₀}·T` keeps the Hecke eigenvalues (gap
  `≈ |q₀−1| = 0.099` vs Young's `±1`), so `φ(σᵢ)` is a *non-generator* element of
  `ℂ[S₅]`. Both facts hold simultaneously and consistently: the Tits `*`-iso
  *exists and is `*`-compatible* (via `T`), but is an **algebra** iso, never a
  generator conjugation — exactly what `intertwiner_trace_eq` predicts.

**Net.** The **deformation half** of the canonical `τ` (Hecke `→` `q=1`
seminormal) is now explicitly constructed and `*`-isometric. The residual to
`|c|` is the **pure-S₅ alignment `U`** from the `q=1` seminormal SYT basis to the
Braden–Northover period basis (`M_S = 5·Id−𝟙`) — this needs the S₅ action *in the
period basis*, which the corpus does not record (only the Hodge Gram `M_S`
itself). So `|c|` is gated on `U` (a finite, pure-representation-theory datum),
not on the deformation. No instance registered; `1/(8π)` phase-4; nothing wired.

## Update 2026-07-25 (3) — the S₅ period alignment U built; the τ-chain CLOSES end-to-end

`alpha_em_b2_period_intertwiner_probe.py` constructs the second half of the
canonical Tits iso — the pure-S₅ alignment `U` — and closes the identification.

- **`ρ_period` derived, not fitted.** `M_S = 5·Id₄ − 𝟙` is the S₄-permutation form,
  so the period realisation of `(4,1)` is the basis `hᵢ = eᵢ − (1/5)Σe`: S₄ permutes
  `h₁..h₄`, `(4 5): h₄ ↦ −(h₁+h₂+h₃+h₄)`. Its invariant form is **exactly** `(1/5)M_S`
  (residual `0`). No extra Braden–Northover data needed beyond `M_S`.
- **`U` constructed.** The intertwiner `U·ρ_H^1(sᵢ) = ρ_period(sᵢ)·U` (exact q=1 Young
  natural rep, `a = 1/ρ`) has **nullity 1** (Schur) and intertwines to residual
  `6e-41`. It transports the q=1 seminormal Gram to `κ·M_S` exactly (residual `2e-39`).
- **END-TO-END closure:** with `T(q₀)` the deformation *-isometry (Update (2)),
  `(T·U⁻¹)ᵀ · G_Markov(q₀) · (T·U⁻¹) = c·M_S` **exactly** (residual `3e-39`). The
  τ-image of the Hecke Markov Gram at `q₀` lands proportional to the Hodge Gram `M_S`
  — the identification `τ(Markov Gram) ∝ Hodge Gram` is now **explicitly realised**
  for the `(4,1)` block by the concrete map `W = T·U⁻¹`.

**Honest scope.** This realises the identification at the representation-theory level:
the Markov and Hodge Grams ARE proportional-congruent, via a map built from the
canonical seminormal deformation (`T`) + the canonical S₅ period alignment (`U`). The
reported scalar (`c_raw ≈ 0.7158` in working normalisations) is convention-dependent;
the canonical `|c|` fixes both normalisations + the *-isometric gauge (`→1`,
`canonical_frame_c_eq_one`, #4209). What remains genuinely OPEN is the **physical**
claim that the archimedean functor `τ` *equals* this canonical `W` (i.e. that the
α_EM loop weight IS this Markov Gram) — a categorical/physics input, not a
representation-theory one. All representation-theory obstacles to the τ-identification
are now removed and everything is explicitly constructed. No instance registered;
`1/(8π)` stays phase-4; nothing wired.
