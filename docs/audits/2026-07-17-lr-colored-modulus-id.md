# Keystone — the Lawrence–Rozansky colored-modulus identification for Σ(2,3,5)

**Date:** 2026-07-17 · **Axis:** s5-so3 keystone geometric `W_λ` (Subgoal-2, open for all,
2026-07-11) · **Branch:** `claude/lr-colored-modulus-2026-07-17` ·
**Front 2** of [`2026-07-17-three-front-attack-specs.md`](2026-07-17-three-front-attack-specs.md) §2 ·
**No fit; no physics claim; does not close the gate. Scope-(a) negative.**

## Context — the deferred open step this closes

The McKay `2I ↔ Ê₈` value-map probe
([`2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md`](2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md),
[`keystone_mckay_e8_valuemap.py`](../../computations/probes/keystone_mckay_e8_valuemap.py))
**derived** the value map `d_q(λ) = [mark]_q` (the McKay Coxeter mark's q-integer) but **deferred**
the colored Lawrence–Rozansky amplitude itself — verbatim: *"the colored Lawrence–Rozansky amplitude
(deferred — formula not rigorously pinned this pass)."* The s5-so3 ledger records the honest refocus
after the framing-is-phase result (#3703): *"the open object is the modulus identification
`|S_{0λ}^{Σ(2,3,5)}| = d_ζ/D` (the deferred colored-Lawrence–Rozansky compute), NOT the framing."*

Front 2 closes that deferred compute: pin the genuine colored `Σ(2,3,5)` S-matrix and test the
modulus identification

$$
|S_{0\lambda}^{\Sigma(2,3,5)}(\zeta)| \;=?=\; d_\zeta(\lambda) / D(\zeta)
$$

at fibre roots of unity `ζ_N`, with the colours mapped by `McKay(2I ↔ Ê₈) ∘ (A₅ ⊂ S₅)` and the
values on the E₈ **marks** (`[e]_q` on the exponents was refuted). `d_ζ(λ)` is the Hecke q-dimension
of the `S₅` block; the four conjugation classes carry marks `{1,4,5,6}` with values
`[1]_ζ, [4]_ζ, [5]_ζ, [5]_ζ+1` (the split electron block `(3,1,1)` is `[5]_ζ+1`, **not** `[6]_ζ`).

## Method — reuse the machine-validated Hikami machinery, add the colour insertion

Probe [`keystone_lr_colored_modulus_probe.py`](../../computations/probes/keystone_lr_colored_modulus_probe.py)
/ [witness](../../computations/probes/keystone-lr-colored-modulus.witness.json). It transcribes the
Hikami machinery already validated in
[`keystone_valuemap_genuine_smatrix_s013.py`](../../computations/probes/keystone_valuemap_genuine_smatrix_s013.py)
— the `τ_N` Gauss sum (eq. 2.11), `φ(2,3,5)=181/30` (eq. 2.12), the odd character `χ^{(ℓ)}` (eq. 3.1),
the Eichler-integral limit (eq. 4.2), the exact finite-N Theorem 10 (eq. 5.5) and the genuine
flat-connection S-matrix (eq. 3.8) — and adds the colour-`α` insertion on the order-5 (icosahedral /
`A₅`) exceptional fibre: the `p₃=5` numerator factor `sin(nπ/(5N))` is replaced by `sin(nπα/(5N))`
(the `SU(2)` Wilson line on the icosahedral fibre; `ℓ₃=α` in eq. 3.8).

**GATE 0 (pre-registered, must pass before any conclusion).** The colour insertion at `α=1` must
reproduce the bare `τ_N(Σ(2,3,5))` to machine zero, and the bare Theorem-10 identity must hold —
jointly re-validating the transcription chain. The colored `τ_N` is written as an **independent code
path** so the `α=1` agreement is a genuine cross-check, not a shared-code tautology.

## Results

**GATE 0 — PASS.** `φ(2,3,5) = 6.0333… = 181/30` ✓. `|τ_N^{(α=1)} − τ_N^{bare}| = 0` exactly at
`N=3,5,7` (independent code path). Bare Theorem-10 residual `|LHS−RHS| ≈ 2.6–5.6 × 10⁻³⁹` at
`N=3,5,7`. The transcription chain is re-validated; the modulus conclusion is licensed.

**INDEPENDENCE — D=2 collapse confirmed.** `D(2,3,5) = (p₁−1)(p₂−1)(p₃−1)/4 = 2`. The colored
vacuum-row moduli `|S_{0λ}|` over the order-5 colour `α`:

| `α` | `|S_{0,α}|` |
|--:|--:|
| 1 | 0.52573111 |
| 2 | 0.85065081 |
| 3 | 0.85065081 |
| 4 | 0.52573111 |

The fibre Weyl reflection `α ↔ 5−α` folds `α=4 → 1` and `α=3 → 2` at the modulus
(`|S_{0,4}|=|S_{0,1}|`, `|S_{0,3}|=|S_{0,2}|`, both machine-zero). So there are exactly **2
independent** colored components — the golden-ratio icosahedral / Fibonacci pair, ratio
`0.85065.../0.52573... = 1.61803… = φ`. **The McKay-labelled coloring does NOT escape the D=2
collapse.**

**CONJUGATION-MODULUS — respected (kill criterion does not fire).** `|S_{0λ}| = |S_{0λ'}|` holds
(`α ↔ 5−α`), i.e. the D=2 pair is conjugation-blind, consistent with the `W_{λ'}=W_λ` requirement.
The failure is purely the D=2 collapse, not a conjugation violation.

**SPLIT-NODE — value map uses `[5]_ζ+1`, not `[6]_ζ` (kill criterion does not fire).** At `N=6,7,11`
the electron block `d_q((3,1,1)) = [5]_ζ+1` exactly, and `[5]_ζ+1 ≠ [6]_ζ` (distinct), matching the
McKay-derived split signature.

**MODULUS IDENTIFICATION — ratio mismatch at every N.** The geometry offers only the single ratio
`φ` between its two independent components; the McKay-marked target `d_ζ(λ)/D(ζ)` is a 4-vector whose
self-normalized ratios vary with `N` and never contain `φ`:

| `N` | target self-ratios (marks value map) | geometric D=2 ratio | `min|φ−tgt|` | holds? |
|--:|---|--:|--:|:-:|
| 5 | (1, 1, 0, 1) | 1.6180 | 0.6180 | False |
| 6 | (1, 1.7321, 1, 2) | 1.6180 | 0.1140 | False |
| 7 | (1, 2.2470, 1.8019, 2.8019) | 1.6180 | 0.1839 | False |
| 11 | (1, 3.2287, 3.5133, 4.5133) | 1.6180 | 1.6107 | False |

(At `N=5`, `[5]_ζ = 0` — root-of-unity degeneracy of the muon block.) The identification holds at no
`N`.

## Verdict — scope-(a) negative

The genuine colored Lawrence–Rozansky vacuum row of `Σ(2,3,5)` has exactly **2 independent moduli**
(the golden-ratio icosahedral pair). The McKay-labelled coloring on the order-5 fibre does **not**
escape the D=2 collapse — the fibre Weyl reflection `α ↔ 5−α` folds `α=4 → 1`, `α=3 → 2` at the
modulus. So the identification `|S_{0λ}| = d_ζ(λ)/D` against the 4-class McKay-marked target (marks
`{1,4,5,6}`, values `[1], [4], [5], [5]+1`) is **vacuous**: two geometric components cannot carry a
four-class family, and the ratio-vector mismatches at every `N`. This **re-derives the s013
refutation**, now explicitly at the McKay-colored level (s013 established the D=2 golden vacuum row
against the bare `bwS0` ratios; this probe attaches the McKay colour labels to the order-5 fibre and
shows the labels fold under the same Weyl reflection).

Following the STRICT (a)/(b) discipline: this is a **scope-(a) negative** — *this specific geometric
object (the colored `Σ(2,3,5)` flat-connection S-matrix), alone, does not carry the four-class
`d_ζ/D` family as-is.* It is **not** a structural exclusion of the `W_λ` measure: the rep-theory
value map `d_q(λ) = [mark]_q` is correct and conjugation-blind; what fails is its **lift to four
independent GEOMETRIC amplitude moduli** — the `Σ(2,3,5)` geometry supplies only D=2. The s013 verdict
already noted the escape hatch: *"a larger geometric family (more exceptional fibres ⇒ larger D, or
genuinely colored knot-complement blocks) would be required."* That remains the open direction.

**Evidence, not proof.** The Lean `loc_matches` gate closes only via a positive derivation; this
compute supplies a sharp, quantified negative against one candidate geometric carrier. No fit; no
constant wired to production; the archimedean `q₀`-continuation residual (the #3681 Habiro/Stokes
carriers) is orthogonal and unchanged.

## Cross-references

- Reuse anchor: [`keystone_valuemap_genuine_smatrix_s013.py`](../../computations/probes/keystone_valuemap_genuine_smatrix_s013.py)
  ([audit](2026-07-02-keystone-valuemap-genuine-smatrix.md)) — the machine-validated Hikami S-matrix.
- Value map: [`keystone_mckay_e8_valuemap.py`](../../computations/probes/keystone_mckay_e8_valuemap.py)
  ([audit](2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md)) — `d_q(λ)=[mark]_q`, the deferred
  amplitude this probe takes up.
- Colored family: [`keystone_colored_sigma235_wrt.py`](../../computations/probes/keystone_colored_sigma235_wrt.py)
  — the E₈-exponent-indexed colored support; the `[e]_q` (exponent) refutation.
- Framing: [`2026-07-12-keystone-wlambda-framing-is-phase.md`](2026-07-12-keystone-wlambda-framing-is-phase.md)
  (#3703) — the honest refocus onto this modulus identification.
- Ledger: [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md).
- Bib: `lawrence-zagier-1999`, `hikami2005brieskorn` added to
  [`content/schema/references.ts`](../../content/schema/references.ts).
