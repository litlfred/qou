
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
