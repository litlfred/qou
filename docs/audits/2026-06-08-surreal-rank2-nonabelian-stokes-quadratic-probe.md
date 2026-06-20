# Surreal keep-or-purge — the rank-2 obstruction probe (non-abelian-Stokes quadratic term)

**Date:** 2026-06-08
**Branch:** `claude/vigilant-fermat-SROph`
**Status:** formalize-first structural probe. No fit, no numerical search yet —
this doc *prunes the hypothesis class* before any search, per AGENTS.md
§"Formalize-first probe discipline".

## Question

The owner asked whether the surreal-number apparatus earns its keep, with the
decision criterion: *can it prove (or materially advance) the keystone
`conj:gb-depth-period-correspondence`, and does it give "non-trivial surreal
interactions" we can track to make bounds/obstructions?* The owner's sharpening:
the candidate interactions come from **the quadratic terms of the non-abelian
Stokes / categorical action**, not the linear holonomy.

## TL;DR verdict

1. **The keystone's proof program is already substantial and is surreal-FREE.**
   Depth-2 is a theorem via Bloch–Suslin
   ([`prop:depth-2-identification-bloch-suslin`](../../content/quantum-observable-universe/appendix-surreals/depth-2-identification-bloch-suslin.md));
   `n ≤ 4` is verified via Markov trace + Vol/CS + bar-symmetry
   ([`prop:two-filtration-bridge-small-cases`](../../content/quantum-observable-universe/stochastic-mechanics/two-filtration-bridge-small-cases.md));
   a **full** proof of depth ≥ 3 *is* Goncharov's motivic conjecture
   `K_5^ind ≅ 𝔅_3` (open 25+ yrs). So "prove the keystone ⟹ keep surreals"
   rests on a false premise: the proof does not use surreals.

2. **So the real keep-test is not "prove the keystone" — it is "does QOU have a
   genuine rank-≥2 (infinite-value-group) obstruction that the rank-1
   `ε = (q−1)`-adic line over `ℝ` cannot express?"** Surreals (a Hahn field
   whose value group contains infinite elements) are necessary only there.

3. **Two regimes are rank-1 (surreal-free); the owner's quadratic-term lead is
   the first genuine rank-≥2 candidate.** See the ladder below.

## The scale-rank ladder (the decisive classification)

Two physical "scales" can appear in a QOU obstruction:

- **δ (deformation):** `ε = q − 1`, infinitesimal as `q → 1`. Surreal id
  `ε ↔ 1/ω`.
- **γ (geometric):** hyperbolic volume / Möbius energy / Coxeter length
  `ℓ(K)` / crossing number — quantities that **diverge** as brane complexity
  grows. Surreal id: infinite surreals `ω, ω², …`.

The **rank of the value group** = number of ℚ-independent valuation directions.
A single `ε`-adic valuation over `ℝ` (i.e. `ℝ((ε^ℚ))`) is **rank 1** and sees
only finite `ε`-powers; it cannot express `ε^a · γ^b` for an *independent* `γ`,
nor an infinite exponent `ε^ω`.

| Regime | Scales | Tied or independent? | Value-group rank | Surreal needed? |
|---|---|---|---|---|
| **Kashaev / Volume Conj.** `J_N ~ exp(N·Vol/2π)` | `ε ~ 2πi/N`, `Vol` | **TIED**: `q = e^{2πi/N}` ⇒ `ε·ω ≈ const`; `Vol` is a real coefficient | 1 | **No** — `Vol` is the real `std`-limit `lim (2π/N) log|J_N|` |
| **NS surreal bound** `Δ_q ≍ ε³` vs `Z_q ≍ ε^{−4/3}` ([`ns-surreal-bound.md`](../../content/quantum-observable-universe/fluid-dynamics/ns-surreal-bound.md)) | both pure `ε`-powers | same `ε`-axis | 1 | **No** — `ord_ω` compare = comparing real exponents `3` vs `−4/3` |
| **★ Categorical-action quadratic / GS tower** → `ε^ℓ`, `ℓ → ω` | `ε` (per-event) × `ℓ(K)` (event count) | **INDEPENDENT**: `ε` is the `q→1` scale; `ℓ` is set by knot geometry, not by `q` | ≥ 2 / infinite | **Candidate YES** — see below |

The first two rows are *why* the existing "surreal bounds" are removable: every
one of them is single-axis (`ε` only), hence rank-1, hence a re-description of an
ordinary real asymptotic. One structural observation ("all current surreal
bounds are finite-`ε`-power, single-axis") kills the broad "surreals are
essential" hypothesis — the formalize-first payoff.

## The owner's lead: the quadratic term is the rank-≥2 locus

**Linear vs quadratic.** The *linear/abelian* part of a surface holonomy is
`∫F` — area × curvature, a single scale, rank-1 (`Vol` enters as a coefficient).
The **quadratic** part is where two independent scales multiply.

**Where it lives in QOU.** The canonical action
([`qou-canonical-action.md:25-53`](../../content/quantum-observable-universe/quantum-observable-universes/qou-canonical-action.md))
has the **gauge term**

```
  ∫_A  tr_A( F_∇  ∧_q  ⋆_q  F_∇ ),        F_∇ = ∇² = dα + [α,α].
```

This is **quadratic in curvature**, and `F` itself carries the non-abelian
quadratic `[α,α]` (the gauge-covariant `d_α β = dβ + [α,β]`,
`NonAbelianStokes.lean:300-305`).

**Algebraic realization = Hecke-quadratic events.** Under the
C-action → Yekutieli non-abelian Stokes → Hecke chain, this quadratic content
becomes the **Hecke-quadratic relation events**

```
  T_w · T_i = (q − q^{-1}) · T_w + T_{w s_i}
```

fired during GB-NF reduction. Each event is a **GS-filtration level-mixing
event**, propagating `J^ℓ/J^{ℓ+1}` content down into `J^{ℓ-1}/J^ℓ` — the
"quadratic-form-coming-up-from-below"
([`piece1-gb-nf-quadratic-events.md:19-21`](2026-05-05-piece1-gb-nf-quadratic-events.md)).
Its coefficient is

```
  q − q^{-1} = (1+ε) − (1+ε)^{-1} = 2ε − ε² + …  ≈ 2ε,
```

so **each quadratic event carries one factor of the deformation scale `ε`**.

**The compounding.** The event count is **word-specific and grows with knot
complexity** `ℓ(K)` (`piece1` table: trefoil 2, Borromean 6, proton word 12,
`σ₁²⁰` 19, …). Compounding `ε` over the GS tower gives a quantity of order

```
  (q − q^{-1})^{#events}  ~  ε^{ℓ},        ℓ = ℓ(K) → ω   (the tower limit).
```

`ε^ω = (1/ω)^ω = ω^{−ω} = exp(−ω log ω)` is a **surreal exp-log element**: its
exponent `ω` is infinite, so it is **not** in the rank-1 Hahn field
`ℝ((ε^ℚ))`. It lives in `No` — which, by the Conway normal form, is realised as
Hahn series with real coefficients and **surreal** exponents (`Σ rᵢ ε^{aᵢ}`,
`aᵢ ∈ No`) — exactly the structure surreals provide and the rank-1 `ε`-adic-`ℝ`
line `ℝ((ε^ℚ))` does not.

**This is genuinely independent (not Kashaev-tied):** `ε` is the `q→1`
deformation scale; `ℓ(K)` is the Coxeter length / crossing number, a
*geometric/combinatorial* size set by the knot, not by `q`. Nothing ties
`ε^ℓ` to a constant. So the value group acquires an **infinite generator** — the
first rank-≥2 / infinite-rank candidate in QOU.

## The decisive probe (formalize-first — state before searching)

The candidate is **not yet** a confirmed surreal necessity, because there is a
real-analysis escape:

- **If** the only thing QOU needs from the `ε^ℓ` tower is its **convergent real
  value** (a `std`-limit / radius of convergence `|ε| < R`), then the tower sums
  to a real number and **rank-1 `ℝ` suffices — purge/​re-scope**.
- **If** QOU needs the **infinite-order tail `ε^ω` as an algebraic obstruction
  class** — a class invisible to *every* finite jet order, that must be
  compared/manipulated as an element — then `ℝ((ε^ℚ))` cannot express it and a
  **surreal / infinite-value-group Hahn field is necessary — keep**.

**Probe target (the place a "perpetual" tail would already live):**

1. [`motivic-perpetual-obstruction.md`](../../content/quantum-observable-universe/lifting-and-descent/motivic-perpetual-obstruction.md)
   — an obstruction that *persists at all orders* is, by definition, an `ε^ω`
   tail. Prime test case.
2. [`kummer-filtration-obstruction.md`](../../content/quantum-observable-universe/lifting-and-descent/kummer-filtration-obstruction.md)
   and the GS spectral-sequence collapse
   ([`spectral-sequence-collapse.md`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.md)):
   does the sequence collapse at a **finite** page (⇒ finite `ε`-order ⇒ rank-1)
   or only "in the limit" (⇒ `ε^ω` tail ⇒ surreal)?
3. Production stake — the **jet-tower / Hecke-convergence / Q_β `c_k`
   truncation ladder** (`jet-tower-convergence.md`, `hecke-convergence-bound.md`;
   `Q_β = Q_base · Π(1 + c_k u^k)`, `u = b·ℏ_q²`). These are the production
   towers whose convergence the surreal grading would track. **Caveat
   (AGENTS.md):** the `c_k` ladder is a *truncation order*, not a wire/un-wire
   gate — surreals would **track** its convergence, never **derive** `c_k`.

**Formal statement to settle the probe (Lean target, conditional `class`):**

> Let `T = Σ_{ℓ<ω} a_ℓ(K) · ε^ℓ` be the GS-tower trace of the quadratic gauge
> term, `a_ℓ` the level-`ℓ` Markov weight. **Claim to decide:** the QOU
> obstruction attached to `T` is determined by `std(T) ∈ ℝ` (rank-1) **iff** the
> GS spectral sequence degenerates at a finite page `E_r`, `r < ω`. Equivalently:
> a non-degenerate (perpetual) page ⇒ an `ε^ω` class ⇒ surreal-necessary.

Lean is currently unbuildable in-sandbox (elan release server firewalled — the
`release.lean-lang.org` parse error in the session log); per AGENTS.md
formalize-first this probe is discharged as a **rigorous symbolic argument
first**, Lean `class` stub to follow when the cache-restore path
(`lake-cache/qou-*`) is available.

## RESOLUTION — the finite-page check, settled (2026-06-08, same day)

The decisive check is answered by two existing blocks. They live in **two
different towers**, and necessity resolves cleanly.

### Tower 1 — mass / Markov-trace / GS filtration → collapses at **E₁** (finite)

[`prop:spectral-sequence-collapse`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.md):
for semisimple `H_n(R,q)` (generic `q`), `HH^k(A,A)=0 ∀k≥1` (Whitehead), so the
GB-filtration spectral sequence **collapses at E₁** — *"no higher-page
differentials `d_r` (`r≥1`) need ever be computed — they all vanish"* — with
`E_∞ = Z(A) = ⊕_{λ⊢n} R·e_λ`, a **finite** sum over partitions of `n`.

⇒ The mass-side quadratic tower is **finite-order in `ε`**. The `ε^ℓ → ε^ω`
worry is **refuted for production**: the event count grows along the *reduction
trajectory*, but the graded object the trace sees collapses at E₁ to the finite
centre. **Rank-1, surreal-free. No mass prediction can require surreals.**

### Tower 2 — lifting / Yekutieli–Kummer / volume → genuinely **perpetual** (infinite)

[`conj:motivic-perpetual-obstruction`](../../content/quantum-observable-universe/lifting-and-descent/motivic-perpetual-obstruction.md)
+ [`prop:cs-evaluation-faithfulness`](../../content/quantum-observable-universe/predicted-spectra/cs-evaluation-faithfulness.md):
`κ_n ≠ 0` at **every** level `n ∤ χ(A)`, and `Vol(K) = Σ_n Φ_n(K)` with every
grade `Φ_n ≠ 0`. **This is the genuine `ε^ω` candidate** — an all-orders,
infinite-grading obstruction the `ε`-adic `ℝ` line cannot package finitely.

**But the value is real.** `cs-evaluation-faithfulness` records that **Mostow
rigidity ensures `Σ_n Φ_n` converges** to the real `Vol(K)`. So the infinitude
lives in the **grading** (infinitely many non-zero `ℕ`-indexed grades), **not in
the value** (a convergent real). The transcendence content — *"no finite
polynomial absorbs infinitely many independent contributions"* — is a statement
over `ℝ` + an `ℕ`-grading, not an assertion that needs an `ε^ω` algebraic element.

### Verdict — language, not essential (but narrowing-worthwhile)

| Tower | Structure | Rank | Surreal status |
|---|---|---|---|
| Mass / Markov / GS | collapses at **E₁** (finite) | 1 | not needed (trivially) |
| Lifting / volume | perpetual `κ_n≠0 ∀n`, **Mostow-convergent** | ∞-graded, real value | **language** — `ε^ω` is the clean *bookkeeping* of "perpetual", not a forced element |

**No confirmed surreal *necessity*.** The one genuine infinite structure narrows
*beautifully* to a single `ε^ω` / `No` statement — *"the obstruction is the
depth-`ω` tail"* replaces *"`κ_n ≠ 0` for all `n`"* — which is exactly the
**worthwhile narrowing** the owner's criterion rewards. Mostow convergence means
nothing *forces* an `ε^ω` element that `ℝ` + `ℕ`-grading cannot already express.

### Consequence for keep/purge

- **Keep — on narrowing value, not necessity.** Surreals are the *language* that
  collapses the perpetual-obstruction tower (and the depth filtration) to clean
  graded statements; they are not load-bearing for any theorem (E₁ collapse +
  Mostow convergence remove the necessity).
- **Purge would lose no theorem**, but would lose the narrowing language for the
  transcendence program. Per the owner's criterion, **keep + re-scope as the
  ledger** is the right call.
- The `ε^ω`-as-perpetual-obstruction identity is itself **the cleanest new
  ledger row** surreals buy: state it as a `remark` interpreting
  `conj:motivic-perpetual-obstruction` (depth-`ω` tail = the all-levels `κ_n`).

## Cross-references

- Keystone: [`conj:gb-depth-period-correspondence`](../../content/quantum-observable-universe/mass-theory/gb-depth-period-correspondence.md)
- Quadratic events: [`2026-05-05-piece1-gb-nf-quadratic-events.md`](2026-05-05-piece1-gb-nf-quadratic-events.md)
- Non-abelian Stokes wiring: [`2026-06-01-qhyperbolic-nonabelian-stokes-wiring.md`](2026-06-01-qhyperbolic-nonabelian-stokes-wiring.md)
- Canonical action: [`qou-canonical-action.md`](../../content/quantum-observable-universe/quantum-observable-universes/qou-canonical-action.md)
- E₁ collapse (mass tower finite): [`prop:spectral-sequence-collapse`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.md)
- Perpetual obstruction (volume tower infinite): [`conj:motivic-perpetual-obstruction`](../../content/quantum-observable-universe/lifting-and-descent/motivic-perpetual-obstruction.md), [`prop:cs-evaluation-faithfulness`](../../content/quantum-observable-universe/predicted-spectra/cs-evaluation-faithfulness.md)
- Surreal exp-log literature: Kuhlmann–Matusiński (arXiv:1203.4538, in `uploads/`); Berarducci–Mantova (arXiv:1503.00315).
