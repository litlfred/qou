# Fantini–Wheeler 2024 (arXiv:2410.20973) — reads the c₃-via-Borel gap onto a solved structure

**Date:** 2026-08-01. **Status:** literature finding + reframe of bean
`qou-qnnq` (and the Δ_λ / c₃-via-Borel chain). No compute, no fit, nothing
wired. **Read before further B1 / A_ω / (m,ℓ) work.**

Companion to the already-in-corpus
[`2026-07-26-extended-matrix-trivial-connection-row.md`](2026-07-26-extended-matrix-trivial-connection-row.md)
(which framed the Habiro tail as the trivial-connection row of the GGMW
extended matrix). The owner uploaded the three source PDFs to `library/`
(commit 2a7b6b9): `2410.20973v1`, `2505.00799v2`, `2601.05136v2`.

## The paper

Fantini–Wheeler, *Summability for State Integrals of hyperbolic knots*
([arXiv:2410.20973](https://arxiv.org/abs/2410.20973), 44 pp). Registered as
`fantini-wheeler2024`.

**Theorem 1.1 / 1.4.** The perturbative series `Φ_{4₁}` and `Φ_{5₂}` (the
trivial-flat-connection asymptotic series) are **Borel–Laplace summable**,
and away from Stokes rays the resummation is an **explicit `Z[q^±]`-linear
combination of Andersen–Kashaev state integrals `I_{m,ℓ}(τ)`**. There is an
algorithm (their §3.1) that produces the combination from the geometry of the
volume function `V` and the asymptotics of Faddeev's quantum dilogarithm.

## Why this is the exact object the QOU chain was missing

### 1. `(m,ℓ)` is a state-integral homology basis index — not a per-particle scalar

The state integrals `I_{m,ℓ}(τ)` are indexed by `(m,ℓ) ∈ ℤ²` and satisfy the
recursion (their eq. 14)

```
Σ_k B_k (−1)^k q^{−ℓk} I_{m+k,ℓ} = I_{m,ℓ+1} = (−1)^A q^{A+m} I_{m+A,ℓ} ,
```

so over `Q(q)` the lattice collapses to **exactly `max{A,B}` independent
integrals**. The Andersen–Kashaev integral is the `(m,ℓ)=(0,0)` member; the
full resurgent structure needs all `max{A,B}` of them.

**Reframe of the QOU "Layer-3: braid word → single `(m,ℓ)`" gap.** There is
no map from a braid word to *one* `(m,ℓ)`. The observable (a Borel–Laplace
sum) is a **Stokes-weighted `Z[q^±]`-combination over the whole `(m,ℓ)`
lattice**, which the recursion reduces to a rank-`max{A,B}` module. The
QOU probes that found "writhe → single integer" and "T4-inverted ϑ off the
lattice" were looking for a scalar where the literature object is a
finite-rank vector.

### 2. Stokes data is an **integer matrix**, not a scalar `A_ω`

Between two ray directions the Stokes automorphism is a matrix

```
S_{ϑ₁,ϑ₂}(q) ∈ GL_{max{A,B}}(Z[q^±]) ,   S_{ϑ₁,ϑ₂} S_{ϑ₂,ϑ₃} = S_{ϑ₁,ϑ₃}   (eqs. 26–27)
```

— a Kontsevich–Soibelman wall-crossing cocycle. The individual Stokes
constants `S_ω ∈ ℂ` are its entries and are **integers / Laurent polynomials
in `q`**. For the figure-eight (`4₁`, the QOU muon anchor, `(A,B)=(1,2)`) the
worked §4.1 gives concrete entries such as the series (their eq. 73)

```
4 + q + 2q² + 2q³ + 3q⁴ + 2q⁵ + 4q⁶ + 2q⁷ + 4q⁸ + 3q⁹ + ⋯
```

**Reframe of "A_ω = 3 for all winding classes."** The literature Stokes object
for these knots is a `max{A,B} × max{A,B}` integer matrix, not one constant.
The QOU assumption that a single `A_ω = 3` governs every winding class is too
coarse; this is direct support for **route 2** of bean `qou-qnnq` ("different
winding classes may carry different effective Stokes constants"). The honest
open question becomes: *which row/column of the Stokes matrix does a given
braid closure select* — not *which integer*.

### 3. The two ϑ's are different objects — the "off-lattice ϑ" was a category error

| symbol | in Fantini–Wheeler | in QOU |
|---|---|---|
| `ϑ` | direction (**ray angle**) of the Borel/Laplace ray in the `τ`-plane; Stokes rays form a peacock pattern accumulating at `arg τ = ±π/2` | — |
| `ϑ_K` | — | `Im(𝔲_K)`, the **cusp-shape** imaginary part; `V` computes the knot volume from it |

FW's `ϑ` is a *ray direction* (a Borel-plane bookkeeping angle); the QOU
`ϑ_K` is the *geometric cusp datum* that feeds the volume `V`. They are not
the same `ϑ`. The integer content of the resurgent structure lives entirely
in the **Stokes matrix**; the cusp shape `ϑ_K` is the **transcendental**
input (`V(−1/6,0) = 0.051418…·i` for `4₁`). So the QOU finding "T4-inverted
ϑ values are off the integer lattice" is **expected and consistent**, not an
obstruction: nothing in the mechanism ever asked `ϑ_K` to be an integer. This
retires the "sharpest obstruction" framing in the qnnq analysis.

### 4. Knot ↔ NZ-data dictionary (avoid the (4,1) trap)

- `4₁` (muon anchor): `(A,B)=(1,2)` → `max = 2` → 2 saddles, 2×2 Stokes matrix.
- `5₂` (saddle source; PR #4408 canonical values): `(A,B)=(2,3)` → `max = 3`
  → **3 saddles / 3 geometric flat connections** `σ₁,σ₂,σ₃`. The
  "4-character variety" in the `qou-qnnq` title is the **extended** matrix
  (3 geometric + the trivial `σ₀`), per the GGMW trivial-connection sequel.
- §4.2's worked `(A,B)=(4,1)` example (4 saddles `p₁…p₄`) is a **separate**
  knot studied in ref. [24], **not** `5₂`. Do not cite it as the 5₂ matrix.

## Sequels (also uploaded, also registered) — authors verified from the PDFs

- `mcspirit-rolen2025` — **Eleanor McSpirit & Larry Rolen** (Vanderbilt),
  [arXiv:2505.00799](https://arxiv.org/abs/2505.00799): median resummation
  recovers holomorphic quantum modular forms **given an L-function with a
  functional equation whose coefficients are the Stokes constants**
  (extending Fantini–Rella) — the recovery engine under the QOU
  Watson/median-Borel uniqueness chain. The `4₁` J-function is the worked
  example.
- `mcphail-snyder2026` — **Calvin McPhail-Snyder** (Duke),
  [arXiv:2601.05136](https://arxiv.org/abs/2601.05136): **the diagrammatic
  route, and the most direct literature realisation of the qnnq braid → data
  map.** McPhail-Snyder expresses the geometric-twist invariant
  `Zψ_N(K,ρ,µ)` (a quantization of the SL₂(ℂ) CS invariant / geometric twist
  of the Kashaev invariant) as a **sum of state integrals built directly from
  a knot diagram**: a discrete state-sum over crossings, with a **per-edge
  integer vector `k ∈ Z^E`** and a log-meridian `µ` / log-longitude `λ`
  (worked for the 5₂ Kashaev invariant). Whereas FW index the state integrals
  by Neumann–Zagier data, McPhail-Snyder attaches the integer data **to the
  diagram itself** — so a braid word (a specific crossing diagram) determines
  a specific integer state-sum, with `(µ,λ)` the cusp holonomy. This is the
  concrete combinatorial answer to "how does a braid word pick the data,"
  complementary to the NZ route. A dedicated follow-up should test whether the
  QOU braid → `(m,ℓ)`/Stokes-entry selection is exactly the McPhail-Snyder
  `k ∈ Z^E` crossing sum specialised at `q₀`.

## What this does and does NOT do (honesty scope)

**Does:** names the exact literature object (`I_{m,ℓ}` module + `Z[q^±]`
Stokes matrix), reframes the "braid → single (m,ℓ)" and "A_ω = 3" and
"off-lattice ϑ" framings as looking for the wrong *type* of object, and gives
a proved algorithm (FW §3.1) computing the resummation for `4₁`/`5₂`.

**Does NOT:** close `qou-qnnq`. The physical identification — *which braid
closure selects which entry of the `4₁`/`5₂` Stokes matrix, and how the c₃
coefficient reads off it* — is still open. Nothing here is a fit; nothing is
wired to production. A resummation *value* obtained by transcribing FW's AK
state integral is a literature reproduction, not a QOU derivation of c₃.

## Queued next steps (bean `qou-wmkb`)

1. Transcribe the AK state integral `I_{0,0}` for `5₂` (`(A,B)=(2,3)`) as the
   exact `Φ_B` target the `median_borel_resummation` probe approximates;
   cross-check numerically.
2. Formalize-first: Lean a **conditional** `BorelSummable ⇒ StateIntegral`
   bridge class (§3b-cond pattern) carrying FW Thm 1.4 as the hypothesis —
   not a claim that QOU *derives* it.
3. Reproduce the `4₁` Stokes series (eq. 73) numerically as a self-check of
   the pipeline against a published integer sequence, since `4₁` is the muon
   anchor.
4. Re-scope the `qou-qnnq` obstruction note from "ϑ off-lattice ⇒ mechanism
   suspect" to "ϑ_K transcendental (expected); open question is the
   braid → Stokes-matrix-entry selection."
