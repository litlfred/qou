# Scope — the full-Hecke geometric `W_λ` index (the s5-so3 keystone's remaining open object)

**Date:** 2026-06-24
**Status:** scoping only — a **multi-session / multi-PR research frontier**, owner-gated by the
2026-06-19 narrow reversal (keystone geometric `W_λ` construction). Deliberately **not** attempted as a single build; this doc lays out the program, its falsifiable targets, and what is already foreclosed, so the (hard) geometric work starts from a single coherent map.
**Triggering result:** the Step-1 gate ([#2717](https://github.com/litlfred/qou/pull/2717)) **refuted the SU(2)/WRT(S³/2I) sub-route** (coverage: ≥3-row blocks incl. the electron `(3,1,1)` are outside the GL₂ Schur–Weyl image; value: `d_q=[2j+1]_q` only on the standard rep `(n−1,1)`). Machine-checked in [`Su2SchurWeylForeclosure.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/Su2SchurWeylForeclosure.lean). So the index must live on the **full-Hecke side**.

## The object

Find an `S¹`-equivariant (Reeb) index on a geometric realization of the **full Hecke arena**
whose evaluation at the substrate `q₀` reproduces the q-Plancherel weight family
`W_λ = d_q(λ)²/[n]_q!` (`d_q` the `S_n` q-hook dimension). "Full Hecke" = the principal
specialization / `d→∞` limit (no finite colour `ℂ^N`), per the arena correction #2406.

## What is already established (build on; do NOT re-derive)

| Ingredient | Status | Source |
|---|---|---|
| **Mechanism**: `W_λ` as MTC Plancherel measure `d_q²/D²` from Beasley–Witten Seifert–CS localization on `S³/2I` (Reeb = Seifert `S¹`) | proposed, reduction to published framework | [#2524](https://github.com/litlfred/qou/pull/2524) |
| `Reeb = Res^{S₅}_{S₃}` Lean identity (sorry-free) | landed | #2704 |
| **Identity I** `M(n)=n(3n−1)/2` = `binom(n,2)+n²`: (A) per-partition proved ∀n; (B) Plancherel mean conditional on 2 named axioms | landed | [#2634](https://github.com/litlfred/qou/pull/2634)/[#2655](https://github.com/litlfred/qou/pull/2655)/[#2709](https://github.com/litlfred/qou/pull/2709) |
| **Selection-rule values** `a_D^(n)=lw(n−1)`, `lw(c)=(1/(c+1))Σ_{λ⊢c+1}dim_q`; depth-2 recurrence `R=x²−τx+1`, `τ(q₀)=2.6424` | algebraic side closed | #2612 / [#2488](https://github.com/litlfred/qou/pull/2488) |

## Foreclosed sub-routes (do NOT re-walk — all (b) structural exclusions)

- **SU(2)/WRT(S³/2I) modular data** — misses ≥3-row blocks; value-match only on `(n−1,1)` (#2717, `Su2SchurWeylForeclosure.lean`).
- **Finite colour-SU(N) / higher-colour multiplicity** `m_d(λ)` — support + conjugation-asymmetry mismatch ∀d (#2608/#2406).
- **Compact Sasakian / compact MTC** — `q₀≈1.110 > 1` is not a root of unity (#2398/modular-category-id).
- **Reeb eigenvalue resonance**, **q-deformed projector-weight shift** (210 ppb) — refuted (#2584; resonance-probe-negative).

## Falsifiable targets the index MUST hit (q₀-free where noted)

1. **Defect cubic (q₀-free, Lean-proved):** `144·C(n) = −n(n−1)(2n−13)`, with the **exact sign flip at n=7** (`WLambdaDefectClosedForm.lean`). The index's 2nd heat-kernel coefficient must equal this cubic for every `n`.
2. **`a_D = lw` (selection-rule = SW-period):** the SW-prolonged period must equal the rule value `lw(c)` (#2488); this is the geometric-origin identification, **functional-level** (same `W_λ` family), not a ~8% number-match (#2608).
3. **Deuteron `f_pn` bracket:** any index reproducing `W_λ` must land `f_pn ∈ (0.39479, 0.66067)` (the AME-exact `0.58776` is strictly bracketed by the algebraic `W_(2,1)`; #2503/#2528 consumer).
4. **Conjugation symmetry** `W_λ = W_{λ'}` (Plancherel; #2608/C2-involution Lean) — any candidate index must be transpose-symmetric.
5. **Normalization is a non-target:** per-block ratios within fixed `n` are normalization-invariant (`d_q²/[n]_q!` vs `d_q²/D²` differ by a global factor); only the total `Z(n)` (the defect) is the fixed content (#2717). Do not "fit" a per-block absolute value.

## Phased program (each phase = its own PR, formalize-first, falsifiable-per-step)

| Phase | Deliverable | Depends on | Risk |
|---|---|---|---|
| **G1** | Pin the **gauge datum** (group + level) on `S³/2I` so the Beasley–Witten RT weight is the Hecke `Rep U_q(sl_N)` principal specialization (not a finite `N`) — #2524 residual (i) | #2524 | high (owner-gated DG) |
| **G2** | Compute the equivariant index's **2nd heat-kernel coefficient** symbolically; **gate** against target (1) `144·C(n)` incl. the n=7 sign flip | G1 | decisive refute-or-confirm |
| **G3** | Identify the **`a_D=lw` period** map (target 2) from the Seifert `S¹` monodromy on the prolonged Picard–Fuchs system | G1, #2488 | medium |
| **G4** | Cross-check targets (3) `f_pn` bracket and (4) conjugation symmetry on the realized weights | G2/G3 | low |

## (d) The Bring/Jacobian elliptic-fibre sub-lead — *coordinate, do not duplicate; numerology-guarded*

[#2710](https://github.com/litlfred/qou/pull/2710) (merged, character theory, exact) established `Jac(Bring) ≅ E⁴` and that the rank-2 W-plane is the **elliptic curve `E = Bring/S₄`**. [#2722](https://github.com/litlfred/qou/pull/2722) flags `tr B = f([2]_q)` as the recurrence-kernel target (`τ=2.6424`). A concrete geometric sub-route for **G1/G3**:

- Identify the **q-family `E(q)`** of the W-plane elliptic fibre from the `S³/2I` Seifert fibration (the icosahedral quotient acting on `Bring`).
- Verify its **Gauss–Manin monodromy trace** equals `τ(q₀)=2.6424` (the depth-2 recurrence kernel, #2488), as a *second* anchor beside the defect cubic.

> **Numerology guardrail (STRICT, per the no-fit / no-7th-ansatz rule).** `τ=2.6424` and the Lawrence–Zagier `Ψ(1/q₀)=2.32958` are **single numbers**; matching one geometric scalar to one algebraic scalar is **not** a derivation (the `W_λ` target is a *λ-family*). This sub-lead is admissible only if it produces the **whole `(n−1,1)`-extended family / the defect cubic functionally**, not a one-number coincidence. Treat as a structural hypothesis to formalize (the monodromy *operator*, not its trace value), never a fit. #2710 is a probe (no Lean); the formalization is open.

## Discipline & honest framing

- **This is rigor/frontier work, not a new prediction.** A Beasley–Witten/RT *reduction* gives `W_λ` a categorical *name*; the outside-view tautology risk (the "geometric origin" being the harmonic analysis of the same `SU_q(2)` the framework already postulates) is real and flagged in the ledger. Closing G2 against the defect cubic is the falsifiable content that would distinguish derivation from re-description.
- No fit anywhere; `q₀` only as evaluation point; the no-7th-fit-ansatz rule stands.
- Every phase lands with `lean`-direct / witnessed verification; `sorry` (if staged) carries `-- Ref:` to this doc.

## Cross-references

- [#2717](https://github.com/litlfred/qou/pull/2717) — the Step-1 gate that forecloses the SU(2) sub-route (this program's trigger).
- [`Su2SchurWeylForeclosure.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/Su2SchurWeylForeclosure.lean) — the foreclosure, machine-checked.
- [#2524](https://github.com/litlfred/qou/pull/2524) (mechanism), [#2488](https://github.com/litlfred/qou/pull/2488) (selection rule), [#2710](https://github.com/litlfred/qou/pull/2710)/[#2722](https://github.com/litlfred/qou/pull/2722) (Bring/Jacobian).
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — keystone ledger.
- [`docs/scope/2026-06-19-keystone-dg-construction-attack-plan.md`](2026-06-19-keystone-dg-construction-attack-plan.md) — #2503's attack plan (this program is its post-Step-1 continuation).
