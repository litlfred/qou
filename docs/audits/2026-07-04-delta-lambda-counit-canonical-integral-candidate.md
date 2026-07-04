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

## Isotope systematics (bean `qei4`) — the deuteron 13% is coincidental; the error scales with A

Evaluating the counit `Σ_λ χ^λ(β_K)` on all four light isotopes using the
committed `χ^λ` witnesses (`atom-chi-rust-{d,t,3he,4he}`, zero free parameters,
[`rho_k_counit_isotope_systematics.py`](../../computations/rho_k_counit_isotope_systematics.py)):

| atom | interfaces `C(A,2)` | counit `Σχ^λ` | target `−B/mₑ` | `|Σχ|/|target|` | sign |
|---|---|---|---|---|---|
| D | 1 | +4.929 | −4.353 | **1.13** | wrong |
| T | 3 | +27.06 | −16.60 | **1.63** | wrong |
| ³He | 3 | +44.99 | −15.10 | **2.98** | wrong |
| ⁴He | 6 | +150.36 | −55.37 | **2.72** | wrong |

**Two corrections to the deuteron-only view:**

1. **The 13% match was coincidental.** The magnitude ratio is **not fixed** — it
   grows from 1.13 (D) to 2.7–3.0 (He), spread 2.6×. So the counit is not "one
   constant away" from closing; it over-predicts progressively for heavier nuclei.
   The sign is systematically wrong for all four. **Counit alone is refuted across
   the mass range**, more decisively than the deuteron suggested.
2. **But the error scales with A** — and so does the inter-nucleon **interface
   count** (D:1 pair, T/³He:3, ⁴He:6). The A-growing discrepancy is exactly what a
   missing **interface-vortex (Hopf/L±)** contribution would produce. This keeps
   the counit+vortex direction alive, now with a concrete **A-scaling signature**:
   the vortex correction should grow ~ with the number of nucleon pairs.

## Counit + vortex (bean `vr93`) — mechanism CONFIRMED, closure NOT achieved

Both the co-Casimir and the counit are **character-sum** functionals — class
functions, hence **writhe-averaged / sign-blind**. The negative binding sign lives
in the **framing (writhe) content** they drop. The *derived* vortex weight is the
Kauffman ribbon framing factor
([`chirality-writhe-ribbon-derivation.md`](../../content/quantum-observable-universe/mass-theory/chirality-writhe-ribbon-derivation.md)):
`Θ_λ^{w/2}=q^{w·c(λ)}`, `c(λ)=Σ(col−row)` (content sum), which breaks the self-dual
`c(λ)+c(λ')=0` symmetry that keeps the plain sum sign-blind. The counit+vortex
functional `ε_vortex(β_D)=Σ_λ χ^λ(β_D)·q^{w·c(λ)}`
([`rho_k_counit_vortex_writhe_probe.py`](../../computations/rho_k_counit_vortex_writhe_probe.py)):

| writhe w | `ε_vortex` | sign | `|miss|` |
|---|---|---|---|
| −2 | −9.98 | neg | 5.62 |
| −1 | −1.19 | neg | 3.16 |
| 0 (plain counit) | +4.93 | pos | 9.28 |
| +1 (interface writhe) | +19.0 | pos | 23.4 |
| +4 (chirality-block deuteron w) | +977.6 | pos | 982 |

- **CONFIRMED:** a *negative* writhe flips the sum negative — the derived ribbon
  framing supplies exactly the sign the class-function character sum drops. The
  counit+vortex hypothesis is mechanistically substantiated.
- **NOT closed parameter-free:** no derived *integer* writhe reproduces −4.353 (it
  sits between w=−1 and w=−2, near w≈−1.5), and the framework's *actually-derived*
  writhes give the **wrong sign** entirely (interface +1 → +19; chirality-block
  +4 → +978). Hitting the target needs a non-integer effective writhe — a fit,
  **barred**. (Consistent with `chirality-writhe-ribbon-derivation.md` itself,
  which records the naive ribbon ansatz refuted at the deuteron over 8 variants —
  the culprit flagged as the algebraic-vs-topological writhe convention.)

**The one principled untested object.** The framework's binding is a **mass
defect** `B = M(bound) − ΣM(free) < 0`, so the natural functional is the *defect*
`ε(β_D) − ε(β_D^{vac})`, which — via the exact interface factorization
`β_K = β_K^{vac}·⋈_K` ([`interface-knot-markov-z.md`](../../content/quantum-observable-universe/mass-theory/interface-knot-markov-z.md))
— isolates the single **bar-odd pn interface crossing** `⋈_D` (`p₊=1`), precisely
where the sign lives. The counit probe used the *absolute* `ε(β_D)`; the defect
form is untested (needs `χ^λ(β_D^{vac})`, the disjoint p·n vacuum character,
obtainable from the canonical `closed_form_tau_M` formalism). This is the sharp,
parameter-free next test of the counit+vortex direction — and the most-correct
object surfaced by this investigation.

## Provenance

- Probe + witness: `computations/rho_k_h3a_counit_canonical_integral.py` →
  `rho-k-h3a-counit-canonical-integral.witness.json`.
- Anchor: `rho-k-h3a-co-casimir.witness.json` (target, per-λ y_λ/χ^λ/dim_q).
- Counit definition: `qbeta-counit-transition.md`,
  `lean/QOU/Interactions/qbeta_counit_vs_trace.lean`.
