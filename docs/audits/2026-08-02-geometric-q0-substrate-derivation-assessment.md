# Geometric / substrate derivation of q₀ — assessment: the s5-so3 keystone does NOT yield q₀ parameter-free (structural NEGATIVE + precise gap)

**Date:** 2026-08-02 · **Branch:** `claude/geometric-q0-substrate-2026-08-02` ·
**Axis:** Subgoal-2 geometric/substrate derivation of the substrate modulus `q₀`
(owner-reversed OPEN-FOR-ALL 2026-07-11) · **Discipline:** no fit, nothing wired,
no tier change. Corpus-grep + formalize-first performed before any declaration.

## Question posed

Does the **s5-so3 keystone geometric-realization** (the WRT(S³/2I) = colored
Σ(2,3,5) / Beasley–Witten Chern–Simons localization build of the `W_λ` index)
yield the substrate modulus `q₀ ≈ 1.10997859555733471` **parameter-free** — i.e.
with *no* observable input — so that the absolute binding scale falls out? Or is
there a precise missing lemma?

## Verdict — NEGATIVE (structurally understood, not merely un-attempted)

**The s5-so3 keystone geometric realization does not, and structurally cannot as
currently constructed, yield `q₀` parameter-free.** The keystone's output is a
`q`-parametric weight *family* `W_λ(q)` (plus an integer WRT level `k`); it
contains **no equation that selects a distinguished real evaluation point** `q₀`.
`q₀` is the *archimedean evaluation point* at which the family is read — a separate
datum the keystone does not fix. The framework currently fixes it by CAL-2 (an
observable inversion), and the corpus already proves the value is
**measurement-limited** at the anchor-invariant level.

This is a **type/arena mismatch**, not a computational gap:

| Object | What it is | Fixes `q₀`? |
|---|---|---|
| Keystone geometric realization | root-of-unity WRT/Verlinde index → integer level `k` + weight family `W_λ(q) = d_q(λ)²/D²` | **No** — output is a function of `q`, evaluation-point-free |
| `q₀` | the real archimedean evaluation point `∈ ℝ_{>1}` (growth regime) at which `W_λ` is read | — |
| CAL-2 pin (current) | `(1−q₀⁻¹)² = Vol(4₁)/(m_μ/m_e)` — inverts the **observable** `m_μ/m_e` | Yes, but via an **observable input** ⇒ a calibration, not a derivation |

## Evidence chain (all corpus, verified this session)

1. **The current `q₀` "proof" inverts an observable.**
   [`observations/local-substrate-q-proof.md`](../../content/quantum-observable-universe/observations/local-substrate-q-proof.md):
   `(1 − q⁻¹)² = Vol(4₁)/(m_μ/m_e) ≈ 0.009817 ⇒ q ≈ 1.10998`. `Vol(4₁) = 2·Cl₂(π/3)`
   is geometric; **`m_μ/m_e` is a CODATA observable**. This is exactly CAL-2 — the
   calibration the discipline forbids passing off as a parameter-free derivation.

2. **The keystone realizes the weight *family*, not a value.** The
   [`s5-so3-keystone`](../coordination/s5-so3-keystone.md) open object is the
   geometric origin of `W_λ = d_q(λ)²/D²` as a colored Σ(2,3,5) WRT / `E_q(2)`
   q-Bessel q-series (2026-06-22 reframing). Its resolved pieces (defect cubic
   `144·C(n)`, Identity I Plancherel, C1/C2/C6 localization obligations, the
   framing residual `q₀^{f·c(λ)}`) are all **statements about `W_λ` as a function
   of `q`** — none is an equation `g(q₀) = 0`. Even the fully-derived electron
   block ([`2026-07-12-keystone-wlambda-q0-framing-residual.md`](2026-07-12-keystone-wlambda-q0-framing-residual.md),
   `c((3,1,1))=0 ⇒ bwS0 = d_{q₀}/D` exactly) is *evaluated at* `q₀`; it presupposes
   `q₀`, it does not produce it.

3. **The value of the self-dual locus `q*` (= `q₀`) is PROVED measurement-limited.**
   Sorry-free Lean:
   `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing` (SRigidityPrune.lean;
   no anchor-invariant fibre datum realizes the c₃ swing that pins `q*`, scope-(b))
   + `QOU.QBeta.MeasurementFloor.*` ([`MeasurementLimitedFloor.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MeasurementLimitedFloor.lean);
   the L2 gate arithmetic). Per
   [`2026-07-19-c3-q0-real-routes-closed-fibre-phase-survives.md`](2026-07-19-c3-q0-real-routes-closed-fibre-phase-survives.md):
   the c₃ swing, the Δ_λ magnitude ingredient, and the `q₀` zero `q*` are **three
   shadows of one fibre-level object whose VALUE leg is proved un-derivable below
   the experimental `Q_β` floor** and whose SHAPE leg supplies shape, never value.

4. **The natural geometric-constant guesses are refuted.** The figure-8 complex
   volume `𝔙₄₁(u)`, `u = log q₀`, has its nearest branch point at the golden ratio
   `R = 2·log φ ≈ 0.962` — an **O(1)** radius, with the anchor at `u ≈ 0.104 =
   0.108·R` deep in the interior
   ([`2026-08-01-c3-uq0-radius-golden-ratio-on-anchor-singularity-refuted.md`](2026-08-01-c3-uq0-radius-golden-ratio-on-anchor-singularity-refuted.md)).
   There is **no distinguished on-anchor geometric singularity** for `q₀` to sit
   at. The flat Yekutieli per-cell substrate closure is likewise NEGATIVE
   (cross-anchor divergence at the muon,
   [`2026-06-13-yekutieli-mp-substrate-closure-negative.md`](2026-06-13-yekutieli-mp-substrate-closure-negative.md)).

## The precise missing lemma

A genuine parameter-free geometric derivation of `q₀` would require:

> **A rule that selects the real archimedean evaluation point `q₀ ∈ ℝ_{>1}` from
> the root-of-unity keystone/WRT data (level `k` + the family `W_λ(q)`) alone, with
> NO observable input.**

No such rule exists in the corpus, and there is a proved obstruction to it at the
anchor-invariant level (evidence 3). The keystone lives at roots of unity (compact
WRT); `q₀` is real `> 1` (non-compact `E_q(2)` growth regime, 2026-06-22). The
map from "level-`k` root of unity" to "real `q₀`" is precisely the *archimedean
continuation / evaluation-point selection* — and it is not supplied by the
geometry; the framework supplies it by CAL-2.

## Formalize-first deliverable (this branch)

[`QOU/AlgebraicSubstrate/Q0GeometricSelectorTargetSpec.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/Q0GeometricSelectorTargetSpec.lean)
— sorry-free, generic `CommRing R`, §7c (no `ℝ`, no ordering), honest-`TargetSpec`
style. It **types** the finding rather than re-deriving it:

- `GeometricSubstrateData` carries the intrinsic map `Φ : R → R` (the keystone /
  `Vol_q/ℏ_q²`-type function of `q`, observable-free).
- `PinnedBy D obs q0 := (D.Φ q0 = obs)` types the CAL-2 pin: `q₀` fixed **relative
  to an external observable target** `obs`.
- `pinned_subsingleton_of_injective` — GIVEN the observable, the pin is unique
  (`Function.Injective Φ ⇒ Subsingleton`), the typed analogue of the real
  monotonicity `f(q)=(1−q⁻¹)²` ↑. This is the CAL-2 uniqueness.
- `intrinsic_data_underdetermines_q0` — WITHOUT an observable, the intrinsic data
  admits *every* value as its own pin (`PinnedBy D (Φ a) a` for all `a`), so `q₀`
  is **not a function of the keystone data alone**. This is the machine-checked
  statement of the NEGATIVE.
- `selector_interface_trivially_inhabitable` — the interface alone is content-free
  (identity `Φ` admits any `q0`): the wall is exclusively the **observable input**,
  never the interface. Mirrors
  `SelfDualLocusTargetSpec.trivial` / `TauFunctorTargetSpec.interface_alone_...`.

Nothing is wired; no `q₀` value is asserted; no fit. The Lean does not claim a
geometric selector exists — it proves the keystone data does **not** determine
`q₀`, and names the missing external datum exactly.

## Anti-laundering scope note

- This is a **type/arena structural observation** (evidence 2 + the Lean
  `intrinsic_data_underdetermines_q0`) composed with an **already-proved scope-(b)
  VALUE-leg obstruction** (evidence 3, cited not re-derived). It is **not** a new
  broad claim that `q₀` can *never* be derived by any means — only that the
  keystone-as-constructed does not yield it and that the anchor-invariant value is
  measurement-limited. The SHAPE-leg fibre program (5₂-chiral, bean `qou-3yxn`)
  remains open and may still sharpen the *family*; it does not supply the *value*.
- The honest exit is a bean stating the precise missing lemma (below), **not** a
  fabricated closure. Per §"Axiomatization is NOT a Proof", axiomatizing a `q₀`
  selector as a Lean class would not derive it.

## Bean

`GAP: parameter-free geometric selection of the archimedean evaluation point q₀`
— see the created bean for the full precise-gap statement.
