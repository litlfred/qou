# q-regime map — coordination note for sibling agents

**Date:** 2026-06-08
**Originating PRs:** #1999 (phase transitions + H₂O), #2002 (optical fibre / 1D QOU)
**Purpose:** the owner asked where the substrate parameter `q` hits a
"big behaviour change" as it moves away from the working point. This doc
maps the **known** regime boundaries, marks the **under-explored** ones,
and records the **coordination decision** so siblings don't duplicate or
contradict. Owner decision (2026-06-08): **build at q₀; defer the upper-q
sweep to a follow-up; document here for coordination.**

## 1. The working point

`q₀ = 1.1099785955541805` (50-dps), real, `q₀ > 1`. This is the
confined-hadronic regime. All PR #1999 (H₂O, phase predictions) and
PR #2002 (optical fibre) content is evaluated **here** unless explicitly
flagged otherwise. Observable-level constraint: `Im(q₀) = 0`
(`lusztig_q_0_imaginary_part_zero`) — real masses require real q at the
archimedean level (AGENTS.md fibre-vs-observable banner).

## 2. Known regime boundaries (documented in the corpus)

| regime | range of effective q | what happens | source |
|--------|----------------------|--------------|--------|
| Confined hadronic | `q > 1` (incl. q₀) | smooth elliptic fibre, color confined (S₅-invariant only), stable baryons/mesons | [`golden-ratio-degeneration.md`](../../content/quantum-observable-universe/observations/golden-ratio-degeneration.md) |
| Intermediate | `q_gold < q < 1` | smooth fibre, partial confinement, unstable resonances | same |
| **Critical (lower)** | `q = q_gold = 1/φ² ≈ 0.382` | elliptic fibre degenerates (nodal); S₅ color symmetry **breaks**; QGP onset | `rem:golden-ratio-degeneration`, `rem:deconfinement-golden-threshold` |
| Deconfined QGP | `q < q_gold` | degenerate fibre, free quarks, no stable hadrons | same |
| Anyonic / MTC | `q = e^{2πi/k}` (unit circle, **fibre-level**) | KLR algebra truncates to a Modular Tensor Category of non-abelian anyons | `conj:root-of-unity-mtc-truncation`, `conj:hecke-anyonic-substrate` |

`s := √q`; the boundary `q_gold` is the root of `s² + s − 1 = 0`
(`s = 1/φ ≈ 0.618`, `q_gold = 1/φ² ≈ 0.382`). This is the **lower**
real-q transition — the only sharp real-q boundary the corpus pins.

Speed of light runs as `c_q = 1/(q−1)`
([`information-speed-of-light.md`](../../content/quantum-observable-universe/information-theory/information-speed-of-light.md)):
`q → 1⁺ ⇒ c → ∞`; `q → ∞` (Big Bang) `⇒ c → 0` (fibres informationally
isolated). So **raising q lowers the information speed** — the seam to
the optical-fibre PR #2002 (a bounded 1D channel is a high-effective-q,
low-c regime).

## 3. The under-explored boundary (owner's open question) — DEFERRED

The owner asked about the **upper** side: real `q` rising from q₀≈1.11
toward candidate special values

- golden ratio `φ ≈ 1.618`,
- golden ratio squared `φ² ≈ 2.618`,
- silver ratio `δ_S = 1+√2 ≈ 2.414`,

and whether a "big behaviour change" (e.g. 3d→2d anyonic reduction,
extreme-q / linear-system limit) sits there.

**Status: genuinely open.** Corpus-grep finds the *lower* transition
(`q_gold`) and the *unit-circle* anyonic regime, but **no real-q upper
boundary** is pinned. Candidate hypotheses to test in the follow-up
(NOT in #1999/#2002):

1. **No sharp upper transition** — the confined regime extends smoothly
   for all real `q > 1`, and the only "behaviour change" upward is the
   `q → ∞` Big-Bang fibre-isolation limit (`c_q → 0`).
2. **A bar-symmetric image of q_gold** — under `q ↦ q⁻¹` the lower
   boundary `q_gold ≈ 0.382` maps to `1/q_gold = φ² ≈ 2.618`. If the
   physics is bar-symmetric at the fibre level, `q = φ²` would be the
   upper mirror of the QGP onset. **This is the cleanest formalize-first
   candidate** — testable from the existing `golden-ratio-degeneration`
   discriminant by applying the bar involution.
3. **Anyonic only on the unit circle** — the 3d→2d anyonic reduction is
   a *fibre-level* (complex-q, `|q|=1`) phenomenon, not a real-q>1
   transition; the real-q axis stays hadronic. (Consistent with the
   fibre-vs-observable distinction.)

## 3b. The metallic-ratio / involution hierarchy (owner refinement, 2026-06-08)

The owner observed that the **bar involution `q ↦ q⁻¹`** (Hecke
skew-symmetry) already relates `q<1` to `q>1`, so the special-q points
form an involution-symmetric hierarchy, and that the metallic ratios
(golden, silver, …) tied to roots of unity are the natural rungs. The
precise structure:

**Metallic ratios = real `q>1` with integer Hecke scalar.** The Hecke
generator satisfies `σ² = (q−q⁻¹)σ + 1`; the structural scalar is
`q − q⁻¹`. The metallic ratio `δ_n` (positive root of `x²−nx−1=0`) is the
unique `q>1` with `q − q⁻¹ = n`:

| n | δ_n | value | `q−q⁻¹` | role |
|---|-----|-------|---------|------|
| 1 | golden φ | 1.6180 | 1 | first rung above q₀ |
| 2 | silver 1+√2 | 2.4142 | 2 | |
| 3 | bronze (3+√13)/2 | 3.3028 | 3 | |

So the upper-q hierarchy is **the ladder where the Hecke braiding scalar
becomes integral** — structurally motivated, not arbitrary. *(Provable;
proof block `prop:metallic-q-hierarchy` on PR #1999.)*

**Involution.** `q ↦ q⁻¹` sends `δ_n ↦ 1/δ_n` (`= δ_n − n`), pairing each
real rung `>1` with its `<1` mirror; the unit circle `|q|=1` is the fixed
locus. The Hecke generator's two eigenvalues `q` and `−q⁻¹` make
`δ_n ↦ −1/δ_n` the eigenvalue-conjugate root of `x²−nx−1`.

**Roots of unity — golden is the unique join.** On `|q|=1` the relevant
scalar is `q+q⁻¹ = 2cosθ` (Temperley–Lieb loop / quantum dimension).
`φ = 2cos(π/5) = [2]_q` at `q=e^{iπ/5}` — the Fibonacci-anyon dimension
(pentagon, 5-fold). So **golden lies on BOTH ladders**: real-metallic
(`q−q⁻¹=1`) and root-of-unity (`q+q⁻¹=φ`). Silver maps to the octagon
(8-fold) geometrically but `δ_S>2`, so it is *not* a `2cos(π/k)` quantum
dimension — the root-of-unity tie is special to golden.

**Substrate position.** `q₀ − q₀⁻¹ = 0.2091 < 1`, so q₀ sits *below*
golden: **golden is the first metallic resonance above the substrate**,
then silver, then bronze. The owner's "golden first, then silver" is
correct.

**Relation to the corpus `q_gold`.** The existing deconfinement
`q_gold=1/φ²≈0.382` is a `√q`-golden condition (`s²+s−1=0`, `s=√q`),
**distinct** from this metallic-q ladder (`q−q⁻¹=n`); its involution image
is `φ²≈2.618` (between silver and bronze), itself *not* a metallic ratio.
Keep the two structures separate.

**Updated recommended probes (follow-up):**
1. **PROVE** the metallic characterization (`q−q⁻¹=n ⟺ q=δ_n`, q>1) + the
   involution pairing + `φ=2cos(π/5)` — elementary, Lean-able; anchors the
   whole hierarchy. *(In progress on PR #1999.)*
2. Test whether a physical structural transition actually occurs at `q=φ`
   (first rung): does the confinement filtration `J^ℓ(q)` reorganize as
   `q−q⁻¹` crosses 1?
3. Bar-involution check on the corpus `q_gold` discriminant (former
   hypothesis 2) — independent of the metallic ladder; pins/refutes `φ²`
   as the upper mirror of the QGP onset.

## 4. Coordination decisions (binding for siblings)

- **#1999 + #2002 build at q₀** (real, confined). No content in either PR
  asserts an upper-q transition.
- The upper-q map is a **separate follow-up branch**
  (`claude/q-upper-bound-regime-<ymd>` when opened); this doc is its
  scoping seed.
- Siblings touching the q phase diagram (`golden-ratio-degeneration`,
  `root-of-unity-mtc-truncation`, anyonic-substrate, or any
  optical-fibre "linear/extreme-q" framing) should **cite this doc** and
  flag conflicts here rather than re-deriving the regime table.
- The bar-symmetry candidate (`q = φ²` as upper mirror of `q_gold`) is
  **unclaimed** — first sibling to probe it should post intent on #1999.
