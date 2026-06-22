
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
