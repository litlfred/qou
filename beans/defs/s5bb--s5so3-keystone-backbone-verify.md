---
# s5bb
title: s5-so3 keystone — combinatorial backbone VERIFIED (14/14); functor IDENTIFIED, q-closure OPEN
status: completed
type: task
priority: normal
created_at: 2026-06-16T03:30:00Z
updated_at: 2026-06-21T19:39:07Z
parent: qz9k
---

User pick ("go" on the keystone all three beans reduced to: `conj:s5-so3-fiber-action`).
PR #2504.

## Result (2026-06-16) — backbone verified + stale framing corrected; pending human close

Compute: [`computations/probes/s5so3_branching_backbone_verify.py`](../computations/probes/s5so3_branching_backbone_verify.py)
(witness `s5so3-branching-backbone-verify.witness.json`, **14/14 self-checking assertions**).
Finding: [`docs/audits/2026-06-16-s5so3-keystone-backbone-verified.md`](../docs/audits/2026-06-16-s5so3-keystone-backbone-verified.md).

- **VERIFIED** (this compute): Res^{S₅}_{S₃} branchings + (1,1,1) difference; S₅↓A₅ generation
  indexing (ℓ=1→T₁ in (3,1,1); ℓ=2→H in (3,2)/(2,2,1)) with char-table orthonormality self-check;
  per-block H₃(q) Borromean chars (triv=1, sign=1, χ^{(2,1)}=2−3h⁴−h⁶) ⇒ h⁴ exclusively in (2,1).
- **CORRECTION** to the merged `#2345` synthesis doc: the functor is **IDENTIFIED** as Res^{S₅}_{S₃}
  (2026-06-13), not "awaiting". Three-tier: VERIFIED combinatorics / IDENTIFIED functor / OPEN
  q-deformed closure (the E_{(3,2)} vs E_{(3,1,1)} shift at q₀ + 210 ppb).
- **Fair critical-distance read**: the functor-resolution doc is appropriately scoped (its §4 lists
  the open obligations); the overclaim risk is only in the operator-branching §5 "closes" language.
- **Link to qkhc**: C3 confirms the q=1 χ^{(1,1,1)}(β_Bor)=1; but the c_k sign-block lead must still
  reproduce the q-holonomic argument recurrence + clear refuted-class C12 — necessary, not sufficient.
- **No q-deformed probe run** (pyhecke_native + owner gated).

## Repurpose (2026-06-16, after rebase onto +468 main commits)

Rebasing surfaced that **siblings already did the backbone** in the 468 commits:
a near-identical script `docs/audits/scripts/s5so3_branching_backbone_verify.py`,
sorry-free Lean (`s5_to_s3_restriction_dim_consistent` `cases p <;> decide`;
`restriction_functor_yields_h4_irrep` `native_decide`), and a sibling audit doc.
Per owner pick (repurpose + keep C3), PR #2504 was slimmed:
- **Deleted** my duplicate `s5so3_branching_backbone_verify.py` + witness + the
  `2026-06-16-s5so3-keystone-backbone-verified.md` finding doc (all duplicated main).
- **Kept** the one additive bit as `docs/audits/scripts/borromean_per_block_h4_localization.py`
  (per-block H₃(q): χ^{(3)}=χ^{(1,1,1)}=1 ⇒ h⁴ lives **exclusively** in (2,1)); cites the
  sibling branching script + T15 + the Lean.
- **Fixed** the corpus contradiction: added a correction banner to the merged synthesis doc
  `2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md` (its "functor open" framing was
  stale — the functor is IDENTIFIED + backbone Lean-proved on main; only the q-deformed
  closure is open).
- Confirmed (independent cross-check, no contradiction) the sibling backbone is correct.

<!-- recovered 2026-08-23 from orphaned file `s5bb--s5-so3-keystone.md` (no front-matter; invisible to the tracker) -->

## q-deformed projector-shift probe (2026-06-22, PR #2584) — REFUTED as 210 ppb mechanism

The last well-posed object the first-crack doc left open — whether **q-deformed
home-block weights** break the (2,1)/h⁴ symmetry the classical-multiplicity model
preserved — is now run via the E_λ-projected H₅ Markov trace
`T_g = y_{λ_g}^{H5}·χ^{λ_g}(ι(β_Bor))` (`pyhecke_native` v0.9.0, in-sandbox build).

- **Branching cross-check** `χ^λ(β)=Σ_ν m(ν;λ)χ_ν(β)` to **9.6e-50** (machine zero) —
  validates the Rust 5-strand χ.
- **Non-null mechanism:** δ = T_μ − T_e = **0.2075** (67% of T_μ) — the q-deformed
  weighting DOES break the symmetry classical multiplicity preserved (unlike Model A's
  cancellation). Positive structural finding.
- **But not 210 ppb:** 6–7 orders too large; not the 207× generation ratio
  (T_μ/T_e≈3.07); and **bar-MIXED** → fails the bar-even precondition.
- **Verdict:** the projector-weight object is REFUTED as the 210 ppb mechanism. The
  Markov-trace surface (multiplicity / home-block weight / projected trace) is now
  exhausted; any surviving q-closure must leave the trace-weighting entirely (e.g. a
  Reeb/Casimir geometric level functional acting before the trace — main `8f343e10`).
- Finding: `docs/audits/2026-06-22-keystone-qdeform-projector-shift.md`;
  witness `computations/keystone-qdeform-projector-shift.witness.json`.
- No fit; nothing wired. Owner closes (§4a).

## Geometric-level route consolidation (2026-06-22, PR follows) — reduced to ONE owner-gated object

Owner asked to try the geometric (Reeb-Casimir level) route. Corpus-grep shows all
THREE reducible surfaces are now closed:
1. **Eigenvalue resonance** (Casimir ℓ(ℓ+1) ↔ content sum) — REFUTED (2026-06-16 negative
   probe: non-unique ℓ=1,2, fails ℓ=3, tau multi-block).
2. **q-deformed Markov-trace projector weight** — REFUTED (#2584, this session).
3. **Contact-geometric equivariant index = W_λ** — owner-gated multi-session; the SU(3)/SO(3)
   arena is obstructed (Wu-manifold doc), redirected to a U(1)⊂SU(3) Reeb outside isotropy
   on independent spacetime⊥colour factors.

The on-main (level, chirality) Lean (`ReebChiralitySeparation.lean`, 8f343e10) gives class
SEPARATION, not a mass functional; adding chirality does not open a tractable mass probe
(tau still multi-block; (level,chirality)→mass is a fit unless geometry-derived).

**Net:** no in-session tractable probe remains — the q-closure is fully reduced to the single
owner-gated equivariant-index object. Doc: [`docs/audits/2026-06-22-keystone-geometric-level-route-reduction.md`](../docs/audits/2026-06-22-keystone-geometric-level-route-reduction.md).
No fit; nothing wired. Owner closes (§4a).

## Geometric angles + WRT + Lean (2026-06-22, PR #2591) — 4-path exploration, owner-authorized

Owner authorized all 4 geometric paths. Results:
1. **Angles (explicit)** — icosahedral conjugacy angles {0,72,120,144,180°}; SO(3)-restriction
   validated to 5e-41 with the EXACT φ=1+2cos72° pin; per-irrep Reeb phases computed.
2. **WRT/Lawrence-Zagier** — index=W_λ DISSOLVES into modular data: W_λ=d_q²/[n]_q! is the modular
   block weight d²/D² up to the fixed factor D²/[n]_q! (0.982 at n=5), gap EXPLAINED (q-dim≠f^λ).
   S³/2I is the icosahedral selector but WRT(S³/2I)=W_λ is a type mismatch (number vs family).
   Open object REFRAMED: Sasakian existence → modular-category identification (more tractable).
3. **W_λ target** — reproduced to scope-doc numbers (electron 0.29467, muon 0.20754).
4. **Lean** — `icosahedral_ell1_fivefold_char_eq_golden` (1+2cos(2π/5)=(1+√5)/2) sorry-free
   (lean-direct EXIT=0), wired into QOU.lean.

Docs: `docs/audits/2026-06-22-keystone-geometric-angles-preflight.md`. No fit; nothing wired.
Owner closes (§4a).

## Modular-category identification SETTLED (2026-06-22, PR follows)

Pursuing the WRT-reframed object (which modular category?): q_0 is REAL > 1
(|q_0|=1.11≠1, η=log q_0=0.104 real), so NOT a root of unity ⇒ NOT a compact
SU(2)_k MTC. [m]_q=sinh(mη)/sinh(η) exactly (growth/I_ν branch). The W_λ-producing
structure is the NON-COMPACT SU_q(2)→E_q(2) contraction (Hahn-Exton q-Bessel) at
generic real q_0 — ALREADY identified in the corpus (reeb-phase-qbessel doc).

This UNIFIES three framings: (1) finite Sasakian (ruled out), (2) WRT/modular block
weights, (3) here = non-compact E_q(2) contraction = the corpus's existing q-Bessel
home. Keystone's "owner-gated geometric object" is NOT differential geometry — it's
representation theory already named. Residual frontier (sharply located): the explicit
Habiro-ring WRT(S³/2I) q-series at q_0 reproducing W_λ — a concrete q-series compute,
not Sasakian existence.

Doc: docs/audits/2026-06-22-keystone-modular-category-identification.md. No fit. Owner closes (§4a).

## Habiro-WRT(S³/2I) push (2026-06-22, PR follows) — WRT q-series operational, frontier sharpened

Owner pick: push the residual frontier (Habiro-WRT(S³/2I) ↔ W_λ).
- **Formula pinned** from the literature (Lawrence-Zagier 1999 / Hikami): the Σ(2,3,5) false theta
  Ψ(q)=Σχ(n)q^{n²/120}, χ=+1 on {1,11,19,29}, −1 on {31,41,49,59} mod 60. Support = icosahedral/E₈
  data (P=30=h(E₈)). Now operational in the corpus (script + witness).
- **Regime catch:** Ψ converges only for |q|<1; substrate q₀=1.11 is OUTSIDE; its bar image
  1/q₀≈0.901 is INSIDE. Ψ(1/q₀)=2.32957704683293 (converged 50 dps). Bridge = the q↦q⁻¹ bar
  involution the whole corpus runs on; Habiro ring unifies root-of-unity + generic.
- **Type-correct verdict:** Ψ(1/q₀) is ONE manifold invariant; W_λ a λ-family → no direct equality
  (not claimed; no numerology sought). Link is structural (shared E₈/icosahedral input).
- **Sharpened frontier:** the λ-family needs the WRT TQFT with λ-COLORED insertions (colored Σ(2,3,5)
  invariants / S-matrix), not the bare closed-manifold number — a concrete rep-theoretic+q-series
  object, not differential geometry.
Doc: docs/audits/2026-06-22-keystone-habiro-wrt-s3-2i.md. No fit. Owner closes (§4a).

## λ-coloured WRT / Schur-Weyl obstruction (2026-06-22, PR #2603)

Owner pick: the λ-coloured WRT invariants. Well-anchored increment:
- **Colour-resolution computed:** the bare Σ(2,3,5) invariant splits over its 4 false-theta
  components Ψ̃₃₀^(a), a∈{1,11,19,29}: at 1/q₀ = {0.990, 0.789, 0.503, 0.048}, sum=2.3296 (×-check 1.4e-15).
- **Obstruction established (not forced):** 4 WRT colour components (SU(2)-spin index) vs 7 partitions
  / 3 physical blocks (S₅ index). 4≠7, 4≠3 ⇒ NO naive component↔W_λ bijection; impossible by counting.
  The map SU(2)-colour → S₅-block is SCHUR-WEYL duality (the colour-ℂ³/spin-ℂ² bridge, #2364), not identity.
- **Frontier now at the rep-theory core:** push SU(2)-coloured WRT data through Schur-Weyl, compare
  S₅-resolved weights to W_λ via the bar/Habiro bridge. Finitely stated; not differential geometry.
Doc: docs/audits/2026-06-22-keystone-wrt-color-schurweyl.md. No fit. Owner closes (§4a).

## Schur-Weyl SU(2) row-count push (2026-06-22, PR #2604) — spin/colour generation split

Owner pick: push SU(2)-coloured WRT through Schur-Weyl to the S₅ blocks. Exact selection rule:
GL(2)/SU(2) Schur-Weyl on (ℂ²)^⊗n yields ONLY ≤2-row partitions; ≥3-row needs SU(≥3) colour.
Applied to λ⊢5:
- SU(2)-reachable (≤2-row): {(5),(4,1),(3,2)} ↔ spins {5/2,3/2,1/2}. INCLUDES muon (3,2).
- Needs colour SU(≥3) (≥3-row): {(3,1,1),(2,2,1),...}. INCLUDES electron (3,1,1).
SHARP: muon (3,2) 2-row → spin-reachable (Poincaré WRT sector); electron (3,1,1) 3-row →
colour/SU(3) only. The lepton generations split across the spin/colour Schur-Weyl boundary —
the corpus spin-ℂ²⊥colour-ℂ³ split (#2364) AT THE GENERATION LEVEL, derived not posited.
Keystone factorises: spin sector ← S³/2I WRT; colour/≥3-row sector ← SU(3). Remaining: per-sector
numerical realisation (level-k S-matrix / SU(3) coloured invariants) via bar/Habiro. Not diff geo.
Doc: docs/audits/2026-06-22-keystone-schurweyl-su2-rowcount.md. Exact rep theory; no fit. Owner closes (§4a).

## Schur-Weyl dual-sides — deflationary capstone (2026-06-22, PR follows)

Owner pick: keep pushing (spin-sector realisation). Computed BOTH Schur-Weyl sides for the
2-row blocks of n=5: the corpus W_λ uses the HECKE (S_n-side) hook-content d_q(λ); the WRT/Poincaré
modular data is the SU(2) (V_λ-side) [2j+1]_q. They DIFFER (muon (3,2): [5]_q=5.22 vs [2]_q=2.01;
coincide only at (4,1)). So W_λ and the WRT data are Schur-Weyl DUAL — paired, NOT equal. A direct
WRT=W_λ equality is a category error; the Poincaré sphere is the icosahedral selector, the W_λ are
the dual S_n-side q-dims. No closer identity at the weight level — the deflationary terminus of the
WRT line. Arc net: genuine structural gains (Sasakian ruled out; angles+Lean φ; W_λ reproduced; WRT
operational; link=Schur-Weyl duality) but NO closure / no mass prediction. Caveats stand
(assignment-dependence; non-monotone spin/colour vs mass). Doc:
docs/audits/2026-06-22-keystone-schurweyl-dual-sides.md. No fit. Owner closes (§4a).

## Ledger reconciled (2026-06-22, trusting-dirac, PR #2610)

Reconciled docs/coordination/s5-so3-keystone.md to the 2026-06-22 state: E_q(2)/colored-WRT reframe, #2584 projector-shift refuted, the falsifiable 144*C(n)=-n(n-1)(2n-13) sub-target + the Identity-I M(n)=n(3n-1)/2 Mathlib gap (no SYT/hook-length infra; multi-session). Background-agent scoping read: safe win = Identity I (but Mathlib-blocked); full closure at real risk of being a categorical re-NAMING of W_λ (tautology), not a new mass prediction.

Escalated to owner (NOT adjudicated in ledger): (1) GATE — #2503/#2524 state the geometric-derivation gate was reversed 2026-06-19 + DG build directed, but this is not recorded in the ledger or AGENTS.md §Precision-goals (still says subgoal-2 out-of-scope without reversal); (2) C1 normalization — #2524 (open) proposes d_q^2/D^2 via Beasley-Witten CS localization on S^3/2I. Coordination note posted on #2503.

## Residual (ii) DISCHARGED — Reeb = Res^{S₅}_{S₃} Lean (2026-06-24, PR #2704, merged `83edee35`)

Residual (ii) of #2524 — the Lean formalization of the "Reeb = Res^{S₅}_{S₃}" scaffold identity —
landed sorry-free + axiom-free in `S5SO3FiberAction.lean` (`s3SignTwist`,
`restriction_intertwines_conjugation` = `Res(λ')=s3SignTwist(Res(λ))` ∀λ⊢5,
`std_irrep_conjugation_fixed` = the (2,1)/h⁴-carrier multiplicity is conjugation-fixed, capstone
`reeb_eq_restriction_scaffold [BringFiberAction]`; all three `#print axioms` = none).

- **Scope (honest):** the *algebraic* restriction-commutes-with-conjugation identity ONLY. The capstone's
  conjunct (i) still **uses** `BringFiberAction` (the geometric fibre map stays open). **NOT a keystone closure.**
- **Residual (i) (MTC-matching — pin the Beasley–Witten gauge datum on S³/2I to the Hecke `Rep U_q(sl_N)`
  blocks so the localization `W_λ = d_q²/D²` is provably OUR Hecke category's) stays owner-gated** = the live
  W_λ geometric-origin frontier.
- **210 ppb stays refuted** (keystone gives the O(1) generation skeleton, not the 2×10⁻⁷ fine shift). No fit,
  nothing wired, no tier change. Ledger `docs/coordination/s5-so3-keystone.md` + sessions-log row updated; audit
  `docs/audits/2026-06-24-keystone-reeb-restriction-lean-formalization.md`. Owner closes (§4a).

<!-- recovered 2026-08-23 from orphaned file `s5bb.md` (no front-matter; invisible to the tracker) -->

## First RAW q-closure crack (2026-06-20) — PR #2518

Owner removed the "open muon braid" objection: Bring **S₃↪S₅** gives the canonical
Hecke inclusion H₃↪H₅, so β=(σ₁⁻¹σ₂)³ lifts with strands 4,5 idle — **no fit**.
Block-projector trace `tr(E_λ ρ₅(β))=y_λ χ^λ` is basis-free ⇒ **sidesteps the
2026-06-02 multiplicity-2 nonexistence theorem** (no line chosen).
- RAW: muon(3,2)/electron(3,1,1) y·χ ratio = **3.067** — O(1), 7 orders above 210 ppb.
- ⇒ operator-valued branching is a **leading-order generation selector, not a 1e-7 knob**;
  positive evidence 210 ppb is an anchor-shift artifact.
- Compute `docs/audits/scripts/keystone_h3_h5_lift_block_shift.py` (self-check tr₅=tr₃ to f64 floor).
- q-closure still OPEN as a 210-ppb mechanism (correctly — it's an artifact). Pending human review.
