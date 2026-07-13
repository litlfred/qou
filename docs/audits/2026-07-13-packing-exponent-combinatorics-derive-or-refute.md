# The A^{−1/3} packing-energy exponent as pure-MeV combinatorics: derive-or-refute (R4-a) — all three corpus combinatorial classes REFUTED symbolically; the exponent is an empirical import, now precisely located

**Date:** 2026-07-13 · **Branch:** `claude/mass-binding-errors-9zqpal` ·
**Type:** FINDING (reproducible, no fit, nothing wired). R4-a — the attack on
the re-scoped GAP 2 of the parent audit
[`2026-07-13-pion-radius-and-vol-to-radius-gaps.md`](2026-07-13-pion-radius-and-vol-to-radius-gaps.md):
`R = λ̄_π·A^{1/3}` is *identically* `E_pack(A) = m_π·A^{−1/3}` (probe-verified
there to 40 digits), so the honest gap is why the per-pair Coulomb **energy**
unit of the 8-pair benchmark formula
`split = (3/5)·α·Δ[Z(Z−1)]·m_π/A^{1/3}`
([`2026-07-13-mirror-split-continuum-em-derivation-attempt.md`](2026-07-13-mirror-split-continuum-em-derivation-attempt.md),
0.985 ± 0.069) scales as `m_π·A^{−1/3}` — a pure energy/combinatorics
question with no geometry transport owed.

Probe: [`computations/deltalambda/packing_exponent_combinatorics_probe.py`](../../computations/deltalambda/packing_exponent_combinatorics_probe.py)
(witness [`packing-exponent-combinatorics.witness.json`](../../computations/deltalambda/packing-exponent-combinatorics.witness.json),
8/8 assertions pass, exit 0; symbolic prune in sympy, data comparison in
mpmath on the continuum-EM probe's exact 8-pair data path). Formalize-first
(compute-author §3.3): the candidate classes were pruned **symbolically
before** the data comparison; the numerical shape test was run because it is
cheap and decisive. Corpus-grep run first
(`A^{1/3} | A^{-1/3} | cbrt | cube root | third root | packing | coordination
number | extensivity` over `computations/ docs/audits/`): the bond-extensivity
and coordination audits
([`2026-07-11-bond-extensivity-equal-weight-coordination.md`](2026-07-11-bond-extensivity-equal-weight-coordination.md),
[`2026-07-11-mnk-coordination-graph-body-order-tower.md`](2026-07-11-mnk-coordination-graph-body-order-tower.md),
[`2026-07-11-bk-coordination-degree-and-alpha-contact.md`](2026-07-11-bk-coordination-degree-and-alpha-contact.md))
carry the coordination-count combinatorics consumed below; no prior
A-cube-root derivation exists anywhere in the corpus.

## The target

The per-proton-pair Coulomb energy in the A-nucleon link:

$$ E_{\rm pair}(A) \;=\; \tfrac{3}{5}\,\alpha\; m_\pi\, A^{-1/3}. $$

`3/5·α` (model factor × derived α_EM) and `m_π` (CAL-3) are accounted for in
the benchmark's decomposition table; the open factor is the **`A^{−1/3}`
dilution law**. Question: does any corpus combinatorial object produce it?

## Candidate table

| candidate class | structural content | symbolic result | verdict |
|---|---|---|---|
| **(a) energy equipartition over the bond-count tower** — a CAL-3 quantum per bond/channel, distributed over the Lean-proved chain combinatorics (`QOU/Mass/LinearChainBondCount.lean`): `(A−1)` bonds, `C(A,2) = A(A−1)/2` pairs/sub-chains, cluster measure `(A−1)A(A+1)/6`; also the coordination counts of the 𝓑_K audits (`z = A−1` vertex degree, contact graphs, kissing-bounded linear growth) | **structural invariant (the prune):** every one of these counts is a **polynomial in A**, and equipartition of a fixed quantum over a polynomial count gives asymptotic exponent `lim ln(count)/ln A = deg` — an **integer**. sympy-verified: bonds → **1**, pairs → **2**, cluster measure → **3**. The natural combinatorial decays are `1/(A−1) ~ A^{−1}`, `2/A(A−1) ~ A^{−2}`, `~A^{−3}` — never `A^{−1/3}`. Data confirm: ln-scatter 0.72 / 1.54 vs 0.077 for `A^{−1/3}` | **NEGATIVE — structurally excluded *for this class*** (cited invariant: integer asymptotic degree of polynomial counts). The `A^{−1/3}` does **not** come from chain/coordination combinatorics. Scope note: the exclusion is of *equipartition over polynomial counts*; a count raised to the ⅓ power (`Vol^{1/3}`, `count^{−1/3}`) is not excluded — but the ⅓ there is imported from 3-dimensional sphere packing, i.e. geometry, which is exactly what this attack was not allowed to use |
| **(b) Milnor / LCS filtration depth** — order-n Milnor invariants at depth ~A; normalization of the lower-central-series tower | the free-Lie/Witt dimensions `dim L_n(k) = (1/n)·Σ_{d\|n} μ(d)k^{n/d} ~ k^n/n` (verified n ≤ 12, k = 2: `n·dim/2^n → 1`). The normalizations available at depth n are: **harmonic `1/n`** (exponent −1), **exponential `k^n`**, and **factorial** (`(n!)^{1/n} ~ n/e` — linear, with a Stirling `√(2πn)` tail giving *half*-integer corrections; sympy limit `(n!)^{1/n}/(n/e) = 1`). No cube-root normalization exists in the tower | **NEGATIVE.** The LCS/Massey depth structure carries exponents from {−1, half-integers, exponentials} — a third-integer is not among them |
| **(c) q-deformed dimension route** — `[A]_q` or A-th-root structures in the Hecke tower | `[A]_q` at the substrate `q₀ ≈ 1.10998 > 1` is **exponential**: `ln[A]_q/A → ln q` (sympy, verified at q = 11/10); `[A]_q^{−1/3} = e^{−A·ln q₀/3 + …}` is exponential-class, not a power law. `[A]_{q=1} = A` exactly — the power law appears only where the deformation vanishes, so the route *imports* the exponent rather than producing it. **Corpus cube-root census** (the enumeration the task demanded): the η-descent **cbrt branch points** (`qbeta-eta-singularity`, O-zeros), the **ζ₃ root-of-unity** Pochhammer values (`qbeta-habiro-wenzl-tower-zeta-n`, `(−1)^{1/3}` terms), **`[3]_q!/q³`** in `F_Bor`, and the meson strategy-J near-match `(m_μ/m_e)^{1/3}` (non-canonical). Every one is a **fixed index 3** (3 colors / 3-component Borromean / level-3 root of unity) — none is an A-th root or an `A^{1/3}` object | **NEGATIVE.** Numerically the exponential decay fails the shape test at 3.7× the `A^{−1/3}` scatter (0.283 vs 0.077) even over the mild A = 3–39 window (only ~1.25 e-folds) |
| **(d) null hypothesis** — `A^{1/3}` is the empirical nuclear saturation-radius law and the framework has no combinatorial cube root of A | follows from (a)–(c) | **STANDS.** The exponent is an **empirical import**, now precisely located: it is the *sole* non-framework factor of `E_pair = (3/5)·α·m_π·A^{−1/3}` (with the `3/5` uniform-sphere model factor its companion). The framework's fixed "3"s (colors, Borromean components, CAL count) would source a cube root only via an *undeclared* "3 colors ↔ 3 spatial dimensions" identification, which the corpus does not make |

## Probe numbers (nothing tuned; all candidates pre-named)

Shape test — scatter of `ln[split_AME/((3/5)·α·ΔZZ·m_π·f(A))]`
(scale-invariant, coefficient-free) on the 8 T_z mirror pairs, plus the
implied coefficient:

| dilution law f(A) | ln-scatter | implied coeff |
|---|--:|--:|
| **A^{−1/3}** (saturation law) | 0.077 | **0.983** |
| A^{−1/4} | **0.040** | 0.791 |
| A^{−2/5} | 0.127 | 1.169 |
| A^{−1/2} | 0.206 | 1.516 |
| 1/(A−1) (chain-bond equipartition) | 0.725 | 4.97 |
| 2/A(A−1) (sub-chain equipartition) | 1.538 | 33.5 |
| [A]_{q₀}^{−1/3} (q-dimension) | 0.283 | 1.203 |
| A⁰ (no dilution) | 0.209 | 0.413 |

**Discrimination power (honest):** the measured effective exponent is
**p\* = 0.252 ± 0.020** (OLS over 8 pairs, A = 3–39): `1/4` at **0.1σ**,
`1/3` at **4.1σ**, `2/5` at 7.4σ. So the data's *shape*, taken alone, does
**not** prefer `A^{−1/3}` — it mildly prefers `A^{−1/4}` (this is the
parent audits' known monotone 0.86 → 1.07 ratio trend, quantified). Two
essential caveats: **(i)** σ is the OLS-internal error of 8 points (6 dof);
correlated systematics — the uniform-sphere `3/5`, the omitted exchange /
self-energy Coulomb corrections, Nolen–Schiffer CSB — carry their own
A-dependence and are absorbed into p\*, so the measurement constrains the
**effective exponent of this construction**, not the radius law per se
(standard nuclear physics attributes exactly this light-A softening to those
corrections, on top of the saturation `A^{1/3}`). **(ii)** The **joint**
(shape + coefficient) reading is different: the coefficient-1 property of
the pion-Compton unit holds **only at p = 1/3** (measured 0.983; at
p = 1/4 the same unit needs 0.791 — a new underived number). Neither
reading is a derivation of the exponent.

Pre-registration note: one witness threshold was amended after first run —
the `[A]_q₀^{−1/3}` failure was first registered as absolute ln-scatter
> 0.5, which overstated the exponential's decay over the finite window; the
shipped assertion is the relative test (> 2× the `A^{−1/3}` scatter;
measured 3.7×). The symbolic refutation (exponential class) is unaffected.
Recorded here per the honesty discipline.

## Classification

**NEGATIVE (derive-or-refute: refuted), with the null (d) standing.**
Scope-(a) phrasing per the STRICT refutation rule, with one legitimate
structural exclusion:

- **Class (a) — structural exclusion within its class** (the (b)-type
  citation: equipartition of a fixed quantum over *polynomial* counts has
  integer asymptotic exponent; sympy-verified degrees 1/2/3). This does
  **not** exclude combinatorial objects *composed with* a cube root — it
  excludes the cube root *arising from* the counting.
- **Classes (b), (c) — scope-(a) negatives:** the LCS/Witt normalizations
  and the q-dimension tower, *as the sole producers*, do not yield a
  third-integer exponent. (A future object combining them with a genuinely
  3-graded structure is not excluded — none currently exists in the corpus.)
- **The honest bottom line:** the framework currently has **no combinatorial
  object producing a cube root of A**. `A^{−1/3}` remains an **empirical
  import** — the nuclear saturation-radius law — now precisely located as
  the single non-framework factor of the per-pair Coulomb energy unit. This
  sharpens the parent's GAP 2 from "underived scaling" to "one named
  empirical exponent + evidence that the corpus's combinatorics cannot
  supply it from chain/LCS/q-dimension structure."

Nothing wired: no production change, no tier change, no content-block edit.

## Closure paths (for the next agent)

1. **The cusp/link-family geometric route** (the parent's carrier): the
   canonical A-component nuclear link family (SDP knot-ID at H₁₂) with
   cusp count ∝ A would make "per-cusp volume constancy" (Borromean value
   exactly 2) a falsifiable prediction, and the ⅓ would then enter as
   genuine 3-dimensional cusp-torus packing — *geometry declared as
   geometry*, not laundered through combinatorics.
2. **Derive the correction spectrum, not the exponent:** the measured
   p\* = 0.252 ± 0.020 is `1/3` **plus** the omitted corrections'
   A-dependence. A framework derivation of the exchange/surface correction
   (the same object owed for the `3/5` replacement — parent audit item 3)
   would *predict* the effective-exponent softening; matching
   p\* ≈ 0.25 without tuning would convert this audit's sharpest datum
   from a caveat into a cross-check.
3. **The "3 = colors" identification, if ever attempted, must be declared:**
   the corpus's fixed-3 objects (ζ₃, `[3]_q!`, 3-component Borromean, η cbrt
   branch) could source a cube root only through an explicit
   "3 colors ↔ 3 spatial dimensions" postulate. That is a new axiom-level
   identification, not a derivation — flag it as such if pursued.

## Files

- probe: [`computations/deltalambda/packing_exponent_combinatorics_probe.py`](../../computations/deltalambda/packing_exponent_combinatorics_probe.py) (new)
- witness: [`computations/deltalambda/packing-exponent-combinatorics.witness.json`](../../computations/deltalambda/packing-exponent-combinatorics.witness.json) (new, audit-only, 8/8 pass)
- this audit: `docs/audits/2026-07-13-packing-exponent-combinatorics-derive-or-refute.md`
- context consumed (unchanged):
  [`2026-07-13-pion-radius-and-vol-to-radius-gaps.md`](2026-07-13-pion-radius-and-vol-to-radius-gaps.md) (parent),
  [`2026-07-13-mirror-split-continuum-em-derivation-attempt.md`](2026-07-13-mirror-split-continuum-em-derivation-attempt.md),
  [`../coordination/binding-scale-is-hyperbolic-volume.md`](../coordination/binding-scale-is-hyperbolic-volume.md),
  [`2026-07-11-bond-extensivity-equal-weight-coordination.md`](2026-07-11-bond-extensivity-equal-weight-coordination.md),
  [`2026-07-11-mnk-coordination-graph-body-order-tower.md`](2026-07-11-mnk-coordination-graph-body-order-tower.md),
  [`2026-07-11-bk-coordination-degree-and-alpha-contact.md`](2026-07-11-bk-coordination-degree-and-alpha-contact.md),
  [`computations/deltalambda/mirror_split_continuum_em_probe.py`](../../computations/deltalambda/mirror_split_continuum_em_probe.py) (data path reused)
