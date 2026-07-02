# Bekenstein varying-α and Magueijo–Barrow VSL vs the QOU substrate — literature review

**Date:** 2026-07-02
**Branch:** `claude/bekenstein-vsl-review-szn69h`
**Scope:** position the QOU framework's derived constants
(c_q, ħ_q, G_q, α_EM(q)) against the two
canonical varying-constants literatures — Bekenstein's varying
fine-structure-constant framework and the Magueijo–Barrow
varying-speed-of-light (VSL) cosmologies — and record where the
comparison strengthens the paper, where it exposes referee-facing
obligations, and what is genuinely different in QOU.

This is a review/assessment document (critical-distance license
applies). It changes no content blocks. Math is written in Unicode
for greppability against sibling audit docs (the working practice in
recent `docs/audits/` files, e.g.
`2026-06-28-calibration-canon-decay-width-ruling.md`); strict LaTeX
conventions apply only to `content/**/*.md` that flows through the
render pipeline.

---

## 1. The two literature threads

### 1.1 Bekenstein varying-α

- **J. D. Bekenstein, "Fine-structure constant: Is it really a
  constant?"**, Phys. Rev. D **25**, 1527 (1982).
  DOI: [10.1103/PhysRevD.25.1527](https://doi.org/10.1103/PhysRevD.25.1527).
  The elementary charge is promoted to a dynamical scalar,
  e(x) = e₀·ε(x), so α ∝ ε² varies in space and time. The
  framework is built from an action principle with a single new
  length parameter ℓ (the "Bekenstein length"), and its
  design constraints are causality, gauge invariance, and
  compatibility with the weak equivalence principle (Eötvös-type
  bounds are the binding constraint Bekenstein himself computes).
- The modern cosmological embedding is **BSBM**
  (Sandvik–Barrow–Magueijo, Phys. Rev. Lett. **88**, 031302 (2002),
  DOI: [10.1103/PhysRevLett.88.031302](https://doi.org/10.1103/PhysRevLett.88.031302)):
  Bekenstein's ε-field coupled to cosmology, driving a
  slow logarithmic drift of α during matter domination.
- **Observational constraint ladder** (what any varying-α claim is
  tested against, in increasing lookback time):
  - Atomic clocks (laboratory, today):
    |α̇/α| ≲ 10⁻¹⁷ yr⁻¹
    (Rosenband *et al.*, Science **319**, 1808 (2008),
    DOI: [10.1126/science.1154622](https://doi.org/10.1126/science.1154622);
    subsequent Yb/Sr comparisons push toward 10⁻¹⁸).
  - Oklo natural reactor (~2 Gyr):
    |Δα/α| ≲ 10⁻⁷ (Damour & Dyson,
    Nucl. Phys. B **480**, 37 (1996),
    DOI: [10.1016/S0550-3213(96)00467-1](https://doi.org/10.1016/S0550-3213(96)00467-1)).
  - Quasar absorption spectra (z ~ 1–3): the Webb
    *et al.* many-multiplet results reporting
    Δα/α ~ −0.6×10⁻⁵ and later a spatial
    dipole (Phys. Rev. Lett. **87**, 091301 (2001); **107**, 191101
    (2011)) are **contested** — wavelength-calibration systematics
    (Whitmore & Murphy, MNRAS **447**, 446 (2015)) and newer
    ESPRESSO measurements are consistent with zero drift. Any use
    of Webb-type results as *positive* evidence is a red flag for
    referees; they function today as upper bounds.
- Comprehensive review: J.-P. Uzan, "Varying constants,
  gravitation and cosmology", Living Rev. Relativity **14**, 2
  (2011), DOI: [10.12942/lrr-2011-2](https://doi.org/10.12942/lrr-2011-2).

### 1.2 Magueijo–Barrow VSL

- **A. Albrecht & J. Magueijo**, "A time varying speed of light as
  a solution to cosmological puzzles", Phys. Rev. D **59**, 043516
  (1999), DOI: [10.1103/PhysRevD.59.043516](https://doi.org/10.1103/PhysRevD.59.043516).
  A phase transition in c (large early c, dropping to today's
  value) solves the horizon, flatness, and cosmological-constant
  problems without inflation.
- **J. D. Barrow**, "Cosmologies with varying light speed",
  Phys. Rev. D **59**, 043515 (1999),
  DOI: [10.1103/PhysRevD.59.043515](https://doi.org/10.1103/PhysRevD.59.043515):
  the power-law family c(t) = c₀·a(t)ⁿ, with the flatness and
  horizon problems solved for n ≤ −2 (radiation era).
- **J. Magueijo**, "New varying speed of light theories",
  Rep. Prog. Phys. **66**, 2025 (2003),
  DOI: [10.1088/0034-4885/66/11/R04](https://doi.org/10.1088/0034-4885/66/11/R04):
  the definitive review, including covariant/bimetric variants.
- **The structural price** (the technical heart of the VSL papers):
  in minimal VSL the Friedmann equations keep their form but the
  stress–energy continuity equation acquires a source term
  proportional to ċ/c:

  ```
  ρ̇ + 3(ȧ/a)·(ρ + p/c²) = (3kc²/4πGa²)·(ċ/c)
  ```

  so energy conservation is violated exactly when c varies in a
  curved (k ≠ 0) universe — that violation is the *mechanism*
  that drives Ω → 1. Mass–energy equivalence
  E = mc² becomes epoch-dependent, and one must choose which
  quantities (energy? mass? particle number?) are held fixed as c
  evolves. Minimal VSL also breaks Lorentz invariance (a preferred
  frame in which c(t) is defined).
- **The standard critique** (must be engaged by anything claiming
  "varying c"): a dimensionful constant's variation is
  unit-convention dependent; only dimensionless combinations
  (α, m_μ/m_e, …) have operational meaning.
  M. J. Duff, "Comment on time-variation of fundamental constants",
  [arXiv:hep-th/0208093](https://arxiv.org/abs/hep-th/0208093);
  G. F. R. Ellis & J.-P. Uzan, "'c' is the speed of light, isn't
  it?", Am. J. Phys. **73**, 240 (2005),
  DOI: [10.1119/1.1819929](https://doi.org/10.1119/1.1819929).

---

## 2. What the QOU corpus already has (survey)

| VSL/Bekenstein ingredient | QOU counterpart | Where |
|---|---|---|
| Varying c | c_q = 1/(q−1), **derived** as the ratio of horizontal coupling q⁻¹ to Reeb advance ħ_q per f_q-step; Lieb–Robinson cone | [`speed-of-light-regimes-lieb-robinson.md`](../../content/quantum-observable-universe/information-theory/speed-of-light-regimes-lieb-robinson.md) |
| E = mc² under varying c | E_ℌ = 𝔪_ℌ·c_q² proved categorically **at each fixed q** | [`mass-energy-equivalence.md`](../../content/quantum-observable-universe/information-theory/mass-energy-equivalence.md) |
| Varying G (Brans–Dicke sector of the VSL literature) | G_q = c_q³·ħ_q/S_cell(q), with G_Planck = 1 identically for all q > 1 | [`gravitational-constant.md`](../../content/quantum-observable-universe/information-theory/gravitational-constant.md) |
| Varying ħ | ħ_q = (q−1)/q | same chapter |
| Varying α (Bekenstein) | α_EM as a categorical trace ratio, derivation **in progress with declared open problems** | `predicted-spectra` §archimedean-hartree-crystal-alpha-em-categorical (`alpha-em-categorical-trace-ratio`, `alpha-em-shift-multiplicative-chain`, `alpha-em-derivation-open-problems`) |
| c(t) cosmology / large early c | Cosmological reading: cosmic time = q-flow; Big Bang = q → 1⁺ where c_q → ∞ ("all states causally connected"), heat death = q → ∞ | [`bigbang-heatdeath.md`](../../content/quantum-observable-universe/appendix-surreals/bigbang-heatdeath.md) (conjecture, explicitly bracketed *highly speculative*); echoed in [`lqg-adm-ashtekar-comparison.md`](../../content/quantum-observable-universe/gravity-spacetime/lqg-adm-ashtekar-comparison.md) |
| Bekenstein 1981 entropy bound | Fibre entropy ≤ η_q per operation (already in the chapter's comparison table) | `speed-of-light-regimes-lieb-robinson.md` §comparison |

Two points of contact are striking:

1. **The Big-Bang endpoint of q-flow *is* the Albrecht–Magueijo
   scenario, obtained rather than postulated.** Albrecht–Magueijo
   *assume* a large early c to dissolve the horizon problem; the
   QOU cosmological reading *derives* c_q → ∞ at q → 1⁺
   as the classical-limit endpoint of the same one-parameter flow
   that controls everything else. The corpus even states the
   horizon-problem-dissolving consequence verbatim ("all states
   causally connected, no time separation"). If the cosmological
   reading is ever promoted from conjecture, Albrecht–Magueijo 1999
   and Barrow 1999 are the mandatory citations, and the comparison
   is favourable: VSL's free function c(t) (or free exponent n)
   is replaced by a single modulus.

2. **Bekenstein-type varying-α phenomenology is automatic, not
   optional.** Since α_EM is (per the
   predicted-spectra programme) a function of q, *any* claim that
   q flows with cosmic time immediately produces a Bekenstein-type
   drifting α — with no separate ε-field: the
   role of Bekenstein's scalar is played by the substrate modulus
   itself.

---

## 3. Structural differences (where QOU is sharper, and where it owes work)

### 3.1 One-parameter rigidity (QOU's genuine advantage)

In Bekenstein/BSBM and in VSL, each varying constant comes with its
own sector (a scalar field, a coupling function, a free exponent).
In QOU every dimensionful constant is a *fixed* function of the one
modulus q: any hypothetical drift q̇ induces **correlated**
drifts

```
d ln c_q / d ln q = −q/(q−1) ≈ −10.09
d ln ħ_q / d ln q =  1/(q−1) ≈  +9.09     (at q₀ ≈ 1.10998)
```

i.e. all d ln(const)/d ln q are computable numbers at
q₀, with **zero** additional freedom. This is a far stronger
falsifiable structure than either literature: a *single* measured
drift (say α̇/α) fixes q̇, and every other
drift (μ̇/μ for μ = m_p/m_e, clock-comparison
observables, …) is then predicted with no free parameter.
Correlated-drift relations of exactly this type are the standard
discriminator in the varying-constants literature (Uzan 2011 §V);
QOU gets them for free.

### 3.2 The Duff/Ellis–Uzan unit-dependence critique applies — and the corpus is already half-armed

The chapter itself notes that c_q ≈ 9.12 is a statement in
substrate units (fibres correlated per Reeb tick) and that SI
recovery rescales by the Planck time. That is precisely the
Duff/Ellis–Uzan point: the operationally meaningful claims are the
**dimensionless** ones — α(q), m_μ/m_e = Vol(4₁)/ħ_q²,
d_H(q) — not c_q itself. Recommendation: any future
VSL-adjacent framing in the paper should lead with the
dimensionless drift predictions and treat "c_q varies" as
shorthand, with an explicit remark citing Ellis–Uzan 2005. Without
that remark, "the speed of light is q-dependent" is the first
sentence a referee from this literature will attack, because the
VSL community spent 2002–2005 litigating exactly this.

### 3.3 The modified conservation law along q-flow is not derived in the corpus (scope-limited gap)

Magueijo–Barrow's central technical content is the *modified
continuity equation* — the explicit statement of what sources what
when c varies. The QOU corpus proves
E_ℌ = 𝔪_ℌ·c_q² **at each fixed q**, but (per the 4-path corpus
grep: `docs/audits/`, `content/`, `computations/`,
`docs/coordination/` — no hits tying a continuity/conservation
statement to q-flow; the existing "energy conservation" hits
concern decay Q-values and the q-game-of-life) there is **no
analogue of the ρ̇ + 3H(ρ + p/c²) = …·ċ/c equation along the
q-flow**. Concretely: ∂_q of the mass–energy law is not
computed anywhere, so the framework currently has no statement of
whether categorical mass, crossing energy, or neither is conserved
as q flows.

Scope classification (per the refuted/open discipline): this is a
**scope-limited open item** — "not present in the corpus as
surveyed", not "cannot be done". It only *matters* if the
cosmological reading (cosmic time = q-flow) is promoted beyond
its current explicitly-bracketed conjecture status. But if it is,
this derivation is the first thing the Magueijo–Barrow comparison
demands, and it looks cheap: differentiate
E = 𝔪·c_q² along q and identify the source term
with a known q-derivative object (the natural candidate being the
germ-commutator / q-curvature blocks, which the corpus already
describes as "the kinematic half of how the substrate parameter q
evolves locally").

### 3.4 The empirical gate: clock bounds on q̇

If q flows, today's drift is bounded by atomic clocks through
α̇/α = (d ln α/d ln q)·(q̇/q). With
|α̇/α| ≲ 10⁻¹⁷ yr⁻¹
(Rosenband 2008) and d ln α/d ln q an O(1–10) number
once the α_EM(q) derivation lands, the bound is
|q̇/q| ≲ 10⁻¹⁷–10⁻¹⁸ yr⁻¹ — i.e.
q is constant to better than one part in 10⁷ over the age of
the universe *unless* the drift is confined to early epochs (as in
Albrecht–Magueijo's phase-transition variant, and consistent with
the corpus's picture where the interesting motion is near the
q → 1⁺ endpoint). This is a cheap, high-value compute once
dα/dq is available: a one-line witness turning the world's
best clock bound into a bound on the substrate flow. The mass
ratios give a second, independent channel, and one of them is
available in closed form today: m_μ/m_e = Vol(4₁)/ħ_q² gives

```
d ln(m_μ/m_e) / d ln q = −2·d ln ħ_q/d ln q = −2/(q−1) ≈ −18.2   (at q₀)
```

so a hypothetical present-day drift bound
|d(m_μ/m_e)/dt / (m_μ/m_e)| ≲ 10⁻¹⁶ yr⁻¹
would map to |q̇/q| ≲ 5×10⁻¹⁸ yr⁻¹.
(The laboratory-constrained ratio is actually μ = m_p/m_e;
its q-derivative additionally needs
d ln F_Bor/d ln q through the canonical facade —
straightforward but a compute task, not a hand evaluation.)

### 3.5 What QOU should *not* import

- **Do not adopt VSL's preferred frame.** Minimal VSL breaks
  Lorentz invariance by fiat; QOU's c_q is a Lieb–Robinson
  velocity of a discrete substrate, where an emergent-Lorentz
  story is the natural (and harder) route. The corpus currently
  makes no Lorentz-invariance claim either way for the substrate;
  flagging, not resolving, that here.
- **Do not lean on Webb-dipole results** as supporting evidence for
  any q-drift narrative — they are systematics-contested (§1.1)
  and function as bounds.
- **Do not present q-flow cosmology as established.** The
  corpus's own bracketing ("highly speculative: the named-surreal
  evaluation is clean, the cosmological reading is bracketed") is
  exactly right and should survive any future editing pass.

---

## 4. Reception forecast (outside view, unsoftened)

- To a varying-constants referee, the *strong* QOU claims are:
  (i) c_q, ħ_q, G_q, α all derived from one
  modulus — the correlated-drift structure of §3.1; (ii) the
  Bekenstein-scalar role being played by an already-present
  parameter rather than a new field. These are publishable
  comparison points *as structure*, independent of whether q
  actually flows.
- The *weak* points they will find in an afternoon: the
  unit-dependence framing (§3.2, fixable with one remark), the
  missing modified conservation law (§3.3, fixable with one
  derivation block), and the absence of any q̇ bound (§3.4,
  fixable with one witness script). None is structural; all three
  are referee-bait if left as-is at the moment VSL comparisons are
  added to the paper.
- Bekenstein's own WEP discipline is worth emulating: his 1982
  paper is remembered because it computed its own falsifiers
  (Eötvös bounds) in the same paper. The QOU analogue is §3.4.

## 5. Suggested follow-ups (pick any)

1. **Remark block** in `information-theory/` citing
   Ellis–Uzan/Duff: dimensionless-drift framing for c_q
   (`interprets: rem:speed-of-light-regimes-lieb-robinson`), plus
   Albrecht–Magueijo/Barrow citations at the q → 1⁺ endpoint
   discussion. Needs `references.ts` entries (bekenstein1982,
   albrecht-magueijo1999, barrow1999, magueijo2003, ellis-uzan2005,
   uzan2011 — lowercase per the references.ts key convention).
2. **Derivation block**: ∂_q of the mass–energy law — the
   QOU analogue of the Magueijo–Barrow modified continuity
   equation (§3.3); candidate tie-in to the germ-commutator
   q-curvature blocks.
3. **Witness compute**: clock-bound on q̇/q via
   d ln α/d ln q and d ln(m_μ/m_e)/d ln q at q₀
   (§3.4) — blocked on the α_EM(q) derivation
   for the first channel, available *today* for the muon-ratio
   channel since m_μ/m_e = Vol(4₁)/ħ_q² is
   closed-form in q.
4. Nothing — keep this as a standing literature-positioning
   record.
