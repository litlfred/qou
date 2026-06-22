
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
owner-gated equivariant-index object. Doc: `docs/audits/2026-06-22-keystone-geometric-level-route-reduction.md`.
No fit; nothing wired. Owner closes (§4a).
