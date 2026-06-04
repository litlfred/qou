# M_λ / Δ_λ closure landscape — consolidated map (2026-06-04)

**Audience.** Any agent asked "what can be done to close M_λ / Δ_λ?"
(the per-block mass-functor component of the per-isotope binding
formula). This doc consolidates the eight scattered audits on the gate
into one map, records what was independently re-verified on 2026-06-04,
and states which directions have a bounded in-discipline next step vs.
which are research-grade.

**One-line verdict.** The gate is in a *proven-negative* state for every
per-partition functional, not merely "unsolved." A 7th fit ansatz is
forbidden. The only object still carrying non-circular signal is the
per-vertex seminormal eigenphase as a **difference** observable (mirror
pairs / splittings), which does not yield absolute M_λ. The genuine
forward path is research-grade categorical (GAP-A-3 brane-tower level
selector / KLR–Demazure), not a compute sweep.

## The gate

The per-isotope binding-energy formula is

    B(K) = m_e · Σ_λ y_λ · χ^λ(K) · Δ_λ(K)

`y_λ` (Wenzl–Schur) and `χ^λ(K)` (Hecke character) are both **known and
substrate-derived**. The unknown is `Δ_λ(K)` — equivalently the per-block
mass component `M_λ(K)` (MeV). Knowing the binding operator `K` gives
`χ^λ(K)`, a dimensionless trace; the formula needs the **mass**, not the
character. The deuteron equation alone is 1 equation in p(6) = 11
unknowns `Δ_λ` — underdetermined.

## What is proven dead (do not re-try)

| # | Approach | Where | Status |
|---|----------|-------|--------|
| 1 | Six fit ansätze (Occam single-support, Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius, augmented Markov) | `docs/audits/2026-05-18-delta-lambda-gating-context.md` §"Closure attempts" | all FAIL; 7th forbidden |
| 2 | ρ_w (per-crystal-vertex trace) | `docs/audits/2026-05-31-rho-w-crystal-vertex-trace-design.md` | **proven identity** Δ_λ^{ρ_w} ≡ χ^λ — collapses to the character already on disk; B_D = −82.9% |
| 3 | Per-partition energy scale E₀^λ = f(λ) | `docs/audits/2026-06-01-e0-lambda-tryall-results.md` | **all 5 candidates mass-ratio-blind** (impossibility theorem below) |
| 4 | Scalar brane-level rule n_⋆ (GAP-A-3); (χ,y)-only ρ rule (GAP-A-4) | `docs/audits/2026-05-31-gap-a3-a4-feasibility-assessment.md` | proven ⊆ Δ_λ — p/n/³He are Markov-equivalent at H₃ yet split ρ∈{1,1,2} |

### The per-partition impossibility theorem (the core obstruction)

Per-partition data — `χ^λ`, `dim_q(λ)`, content-sum, ribbon twist, and
the per-vertex **seminormal eigenphases** — *discards the strand-count /
Hecke-order information that encodes the mass scale*. A per-block scale
`E₀^λ = f(λ)` is by construction the same function of λ for every
particle, so the only particle-dependent input is the per-block
structural mass `m^λ(particle)`; but the electron/proton mass ratio
(1837×) is **not** encoded in the per-partition projection — it lives in
the braid word (number of strands, crossing pattern). Any per-partition
functional is therefore mass-ratio-blind.

**Re-verified 2026-06-04** against `option-e-q-reeb-phase-probe-v4.witness.json`:
the absolute eigenphase prediction misses badly for every A≤3 atom —

| atom | variant_A_with_chi B_pred | AME | miss |
|------|---------------------------|-----|------|
| deuteron | 0.130 MeV | 2.225 | −94.1% |
| tritium | 0.061 MeV | 8.482 | −99.3% |
| helium-3 | 0.108 MeV | 7.718 | −98.6% |

(variant_B_phase_only is no better, −96.7% on D.) This is the
on-disk confirmation of the impossibility theorem, not a new attempt.

## The three documented forward directions

Per `docs/audits/2026-05-31-gap-a1-binding-k-sdp-feasibility.md`
§"upstream options":

1. **Per-block E₀^λ from substrate.** Killed for *absolute* M_λ by the
   impossibility theorem above. The one residual signal is the eigenphase
   **difference** observable: the corpus reports it closes the ³H−³He
   mirror pair to ~2% and B_D to ~−9% with 0 free parameters
   (`docs/canonical-derivation-cheat-sheet.md`; not independently
   reproduced here). That is a *difference/splitting*, not absolute
   E₀^λ — it is the only non-circular object left and the natural
   bounded next probe, with the honest expectation that it closes
   differences only.
2. **Option E / Kashiwara crystal trace ρ_w(K).** Not greenfield — the
   genuine ρ_w is defined, computed, and proven to collapse to χ^λ
   (item 2 above). A relaunch must produce a per-partition,
   q-independent, *categorical* Δ_λ candidate sharpened on paper first
   (KLR–Demazure), tied to GAP-A-3/A-4. Research-grade.
3. **Path B (Borromean tower) / GAP-A-1 binding-operator-K.** The
   binding operator K is substrate-fixable without B_AME (see below),
   but K's character ≠ K's mass, so GAP-A-1 reduces to Δ_λ. Bypassing
   Δ_λ needs a per-atom λ(K) substrate derivation — a different open
   problem. Multi-week.

## GAP-A-1 binding-K enumeration — finding (2026-06-04)

`binding_k_enumerator.py` (extended inter-nucleon generators
`{σ₃,σ₄,σ₅,σ₆,σ₇,σ₈}±` at H₉, words of length ≤ 3) for ³He:
**1596 candidates enumerated, 12 PSD-feasible** (α_gap ≤ 1e-6), ranked by
Markov-trace fingerprint to the stabilization-corrected historical
`tr_M(T_atom)` — **no B_AME in the objective**. This confirms the
operator side is substrate-derivable (as already shown for ²H, K = σ₃²
Hopf), and concretely re-establishes the **GAP-A-1 ⊆ Δ_λ** reduction:
pinning K does not pin the per-block *mass* the binding formula needs.
(The deeper L=4 search — 20 736 candidates — is the bounded extension;
it only re-confirms the reduction, so it is not load-bearing.)

## σ_theory shell N-sweep — gated by the same Δ_λ (2026-06-04)

The deferred "do the shell" / σ_theory shell N-sweep item (instrument
how predicted per-isotope **binding** converges as shell tower depth N
grows) is a **downstream consumer of this same gate**, not an
independent task:

- The shell contribution `Δ𝔪_shell = z²·Φ_q(|V̂_shell|²)·y_shell(q)·f^{λ_atom/λ_shell}`
  (`sigma_shell_characterization.py`, a deprecation-candidate) places the
  shell at Hecke level `3·A_magic` and sums over partitions
  `λ ⊢ 3·A_magic`. Each added shell N → N+1 introduces **new partitions
  λ at higher Hecke order**, and the binding it contributes needs `Δ_λ`
  at exactly those λ — the proven-dead unknown above.
- Therefore the **L2 (accuracy)** leg of a shell N-sweep on binding
  cannot be certified until Δ_λ closes; an N-sweep that uses any
  per-partition functional for the new shells inherits the
  mass-ratio-blind impossibility theorem (§"core obstruction").
- The **non-circular sub-piece that IS computable now** is the
  **difference/ODD channel**: mirror-pair binding splittings
  `ΔB = 2·B₀·sinh θ_B`, formalised this session in
  [`QOU/Mass/MassVolDensity.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/MassVolDensity.lean)
  §4 (`binding_mirror_difference_eq_sinh`, `binding_difference_odd`).
  This is the binding analogue of the eigenphase-difference observable —
  it sidesteps the absolute (even/cosh) scale the Δ_λ gate blocks.

**Verdict:** the σ_theory shell N-sweep is **gated, not a quick
instrumentation**. Pursue only the difference channel (bounded,
in-discipline); the absolute-binding N-convergence waits on the
research-grade categorical Δ_λ path below. Do not instrument the
deprecated `sigma_shell_characterization.py` for absolute binding.

## Recommendation

- **Do not** attempt a 7th per-partition fit, a fresh ρ_w compute, or an
  absolute-E₀^λ functional — all are proven dead.
- **Bounded probe (if pushing M_λ):** the eigenphase **difference**
  observable extended across more mirror pairs / mass splittings (the
  arbitrary-n HOMFLY engine in `homfly_ocneanu_trace.py` now reaches the
  needed χ^λ for any A). Honest expected outcome: closes differences,
  not absolute M_λ.
- **The real forward path is research-grade and categorical:** GAP-A-3
  (brane-tower level selector) or a KLR/Demazure crystal-limit Δ_λ
  candidate, sharpened on paper with a testable prediction beyond the
  deuteron — per the 2026-05-30 KLR-dialog relaunch criteria.

## Source audits

- `docs/audits/2026-05-18-delta-lambda-gating-context.md` (six ansätze)
- `docs/audits/2026-05-31-gap-a1-binding-k-sdp-feasibility.md` (GAP-A-1 ⊆ Δ_λ)
- `docs/audits/2026-05-31-gap-a3-a4-feasibility-assessment.md` (GAP-A-3/A-4 ⊆ Δ_λ)
- `docs/audits/2026-05-31-rho-w-crystal-vertex-trace-design.md` (ρ_w ≡ χ^λ)
- `docs/audits/2026-05-31-option-e-kashiwara-refresh-assessment.md` (Option E v6–v9 fitted)
- `docs/audits/2026-06-01-e0-lambda-substrate-derivation-options.md` (candidate ranking)
- `docs/audits/2026-06-01-e0-lambda-tryall-results.md` (5 candidates fail)
- `docs/coordination/option-e.md` (v1–v9 history)
