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
archimedean level (CLAUDE.md fibre-vs-observable banner).

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

**Recommended first probe (when the follow-up opens):** apply the bar
involution to the `q_gold` discriminant (hypothesis 2) — it's a one-line
structural check that either pins `φ²` as the upper mirror or refutes it,
per the formalize-first discipline. Do this *before* any q-sweep scan.

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
