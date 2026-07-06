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
— isolates the signed interface crossings `⋈_K`, precisely where the sign lives.

## Defect form `ε(β_K)−ε(β_K^vac)` (bean `p7l6`) — the defect STRUCTURE fixes the sign

The vacuum characters were already committed: `atom-chi-rust-{K}.witness.json`
carries both `data.atom` (`include_inter=True` = β_K) and `data.free`
(`include_inter=False` = β_K^vac). So the defect is directly computable,
parameter-free ([`rho_k_counit_defect_form.py`](../../computations/rho_k_counit_defect_form.py)):

| isotope | counit defect `Σ(χa−χf)` | ratio | trM defect `Σy(χa−χf)` | ratio | sign |
|---|---|---|---|---|---|
| D | −30.29 | 6.96 | −0.595 | 0.137 | **neg** |
| T | −709.7 | 42.8 | −0.804 | 0.048 | **neg** |
| ³He | −820.0 | 54.3 | −0.841 | 0.056 | **neg** |
| ⁴He | −28488 | 514 | −0.912 | 0.017 | **neg** |

**The defect structure robustly fixes the SIGN.** Every defect variant is
**negative for all four isotopes** — the bound atom reads lower than the free
vacuum, exactly the binding sign the *absolute* `ε(β_D)` (positive) got wrong. The
sign is carried by the interface difference, **structurally** — no vortex-writhe
hack needed. This is the counit hypothesis' durable contribution.

**But no standard per-block weight closes the magnitude.** Deuteron defect weight
sweep (target −4.3533, tol 1) — all negative, none within tol:

| Δ_λ | defect value | `|miss|` |
|---|---|---|
| `1/y_λ` (counit) | −30.29 | 25.9 (explodes) |
| `1` (trM mass defect) | −0.595 | 3.76 (collapses, A-flat) |
| `1/dim_q` (co-Casimir) | −0.072 | 4.28 (collapses) |
| `sgn(w₀)·f^λ` (Option-E) | **−2.404** | **1.95** (closest) |

Across isotopes the counit-defect ratio *explodes* with A (7→515), the trM-defect
*collapses* (0.14→0.017, nearly A-flat). The right Δ_λ interpolates between these
and remains open — but the **sign is now solved by the defect structure**, which is
the piece the six prior ansätze (all tested on absolute or interface objects, all
positive/wrong-sign) were missing.

**Only sign-definite weights preserve the consistent sign.** The counit (`1/y_λ`)
and trM (`1`) defects are negative for **all four** isotopes; the Option-E weight
`sgn(w₀)·f^λ`, despite being closest *at the deuteron* (−2.40), carries its own
sign structure and is **incoherent across isotopes** — ratio pred/target = 0.55
(D), **−0.22 (T)**, **−0.24 (³He)**, 1.12 (⁴He), i.e. *wrong sign* for T and ³He.
So Option-E-defect is **not** a magnitude lead; its deuteron closeness was
coincidental. The magnitude closure requires a **positive** (sign-definite) weight
whose A-scaling tracks binding — counit over-amplifies high blocks (explodes with
A), trM/co-Casimir under-amplify (collapse, A-flat), and no standard weight lands
between. This is the open GAP-A frontier; a fitted interpolating exponent would be
the barred seventh ansatz and is **not** taken.

## Literature calibration (lit search, 2026-07-04)

- **The vortex twist `q^{2·content(λ)}` is FULLY STANDARD** — the sl_N ribbon-twist
  / second-Casimir eigenvalue (Reshetikhin–Turaev; Turaev, *Quantum Invariants*;
  Casimir factor, arXiv:1407.3754). The "character is writhe-blind, framing lives
  in a separate scalar" split is textbook. The bar-odd sinh writhe `q^w−q^{-w}` is
  a correct synthesis of standard facts (bar = mirror = writhe-flip). The
  disjoint-product LR character formula `χ^λ(β₁⊗β₂)=Σ c^λ_{μν}χ^μχ^ν` is standard
  (Macdonald; Ram, IMRN 1997).
- **Naming caveat (honest):** the *genuine* Hecke-algebra counit is a **single**
  1-dim character (`σ_i↦q` or `↦−q⁻¹`), **not** `Σ_λ χ^λ`. The object used here
  (`Σ_λ χ^λ` = inverse-Gram-weighted trace = Frobenius–Schur square-root count at
  `q=1`) is a **novel repackaging of a classical object**, internally coherent as
  "the TQFT counit against the handle element `ω=G⁻¹𝟙`", but it should be *stated*
  that way — "counit" as written will draw referee objections. (Recorded so the
  corpus does not overclaim standardness.)
- **The binding-from-Hecke-trace mechanism is genuinely unclaimed** — nearest
  precedents (Skyrme nuclei-as-solitons; Bilson-Thompson particles-as-braids)
  compute quantum numbers, not binding via traces. No prior support, no prior
  refutation.

## Net for the counit thread

Owner hypothesis (counit was missed): **confirmed and productive.** It surfaced a
genuinely-untried functional and — via the **defect structure** — a **robust,
parameter-free resolution of the binding SIGN** that all six prior ansätze lacked.
The remaining open piece is the **magnitude** (the Δ_λ per-block weight), now
sharply posed: find the weight interpolating counit-defect (explodes) and
trM-defect (collapses), with Option-E-defect (~2×) the current best. Scope-(a)
throughout; nothing wired; the sign mechanism is the durable win.

## Provenance

- Probe + witness: `computations/rho_k_h3a_counit_canonical_integral.py` →
  `rho-k-h3a-counit-canonical-integral.witness.json`.
- Anchor: `rho-k-h3a-co-casimir.witness.json` (target, per-λ y_λ/χ^λ/dim_q).
- Counit definition: `qbeta-counit-transition.md`,
  `lean/QOU/Interactions/qbeta_counit_vs_trace.lean`.
