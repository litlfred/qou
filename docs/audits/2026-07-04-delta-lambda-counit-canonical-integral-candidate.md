# Δ_λ counit / canonical-integral candidate — genuinely untried, parameter-free-refuted on sign, magnitude-correct (vortex lead)

**Date:** 2026-07-04 · **Axis:** Δ_λ per-isotope binding closure (GAP-A), deuteron anchor
· **Tier:** structural-exact (parameter-free categorical weight; decidable sign refutation)
· **Verdict:** **scope-(a) — the counit alone is refuted on sign; NOT excluded as an ingredient.**

## Origin

Owner question (2026-07-04): *is the counit coming from the categorical action /
Frobenius pairing, and did the canonical mass-binding derivation just miss it?*
This audit answers it: **yes, the counit was genuinely missed** in the Δ_λ
program — and testing it is decisive.

## The candidate (parameter-free, categorical)

On `H_n(q)` the unique non-degenerate Frobenius **trace** is the Markov trace
`tr_M(β)=⟨β,𝟙⟩_G` — the closed-loop / static-mass reading. The **counit** is the
distinct canonical functional `ε(β)=⟨β,ω⟩_G` with `ω=G⁻¹𝟙` the canonical integral
([`qbeta-counit-transition.md`](../../content/quantum-observable-universe/particle-interactions/qbeta-counit-transition.md)).
In the central-idempotent basis the Markov Gram is diagonal with entries `∝ y_λ`,
so `ω=G⁻¹𝟙` weights block λ by `1/y_λ`:

$$\boxed{\;\Delta_\lambda^{\text{counit}} = 1/y_\lambda\;}\qquad(\text{parameter-free — not a fit}).$$

Because this cancels the `y_λ` in `B/m_e = Σ_λ y_λ χ^λ Δ_λ`, the sum collapses to
the un-Markov-weighted character sum `ε(β_D)=Σ_λ χ^λ(β_D)`.

## Genuinely distinct from all six refuted ansätze (confirmed)

Corpus-grep (both the whole-tree checklist and a dedicated agent sweep) confirms
`Δ_λ=1/y_λ` / `ω=G⁻¹𝟙` is **none** of the six:

| refuted ansatz | its Δ_λ | = counit? |
|---|---|---|
| Frobenius co-Casimir | `1/dim_q(λ)` | no (`dim_q ≠ y_λ`) |
| Demazure-fibre | `y_λ·D_w/D_{w₀}` | no |
| LP-Plancherel | LP dual, cost `1/dim_q` | no |
| LP-Frobenius | LP dual, cost `|χ^λ|` | no |
| crystal-graph | `s_λ(1,q,…,q^{n-1})` | no |
| **augmented Markov** | uniform `Δ_λ=−11.21` (binding **∝ y_λ**) | **opposite** of `1/y_λ` |

The counit otherwise appears in the corpus **only** in the Q_β β-decay transition
work — never as a per-partition binding weight. So it is a legitimately new,
parameter-free candidate (the Δ_λ gate bars *fit-based* proposals; this is derived).

## Result at the deuteron (decidable, no optimization)

Reading the committed anchor data
([`rho-k-h3a-co-casimir.witness.json`](../../computations/rho-k-h3a-co-casimir.witness.json),
n=6, 11 partitions, `Σ_target=−4.35337·m_e`,
[`rho_k_h3a_counit_canonical_integral.py`](../../computations/rho_k_h3a_counit_canonical_integral.py)):

| reading | value | note |
|---|---|---|
| `tr_M` (mass) `Σ y_λ χ^λ` | `+0.38829` | the loop/mass functional |
| co-Casimir `Σ y_λ χ^λ/dim_q` | `+0.14496` | refuted (wrong sign, 30× small) |
| **counit `Σ_λ χ^λ(β_D)`** | **`+4.92668`** | **right magnitude, wrong sign** |
| target | `−4.35337` | negative (binding = mass defect) |

- **Magnitude:** `|4.927|` vs `|4.353|` = **13%** — the **first parameter-free
  candidate in the correct regime** (co-Casimir was 30× too small).
- **Sign:** `+4.927 > 0 > −4.353` — **wrong**, the *same vortex-blind failure* as
  the co-Casimir. This is **basis-normalization-independent** (the Gram constant
  only rescales `|Σ|`; it cannot flip the sign).
- **Gate:** does **not** close. A fitted `c=−0.884` would close it, but that is
  precisely the barred **seventh fit-based ansatz** — not taken.

## Scope (STRICT) — (a), not (b)

Per AGENTS.md §"Before declaring refuted": this is a **scope-(a) negative** — the
counit *alone*, parameter-free, does not reproduce the deuteron (wrong sign; 13%).
It is **not** a structural exclusion of the counit as an *ingredient*. No proved
invariant forbids it; on the contrary the magnitude proximity is evidence it is
close to the right structure.

## The lead this exposes (concrete, non-fitted)

Both the co-Casimir and the counit are **character-sum** functionals, both land
**positive**, both are diagnosed **vortex-blind** — the negative target sign lives
in the **vortex (Hopf / L±) content** that character sums drop (cf.
[`neutron-qvalue-symbolic.md`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md):
"the L₊/L₋ (Hopf) content cancels between the two nucleons at single wrap"). The
sharp, testable hypothesis is therefore **counit + vortex content** — the counit
supplies the correct magnitude, the inter-nucleon Hopf/L± content supplies the
sign. Next steps: (1) add the deuteron interface Hopf/L± content to the counit and
re-test the sign; (2) check whether the 13% is systematic by evaluating the counit
at ⁴He. Both are parameter-free.

## Provenance

- Probe + witness: `computations/rho_k_h3a_counit_canonical_integral.py` →
  `rho-k-h3a-counit-canonical-integral.witness.json`.
- Anchor: `rho-k-h3a-co-casimir.witness.json` (target, per-λ y_λ/χ^λ/dim_q).
- Counit definition: `qbeta-counit-transition.md`,
  `lean/QOU/Interactions/qbeta_counit_vs_trace.lean`.
