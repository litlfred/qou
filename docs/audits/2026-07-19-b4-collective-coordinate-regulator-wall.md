# b₄ pole regulator — the collective-coordinate / moduli-volume route (honest negative)

**Date:** 2026-07-19 · **Branch:** `claude/b4-condensate-volrho-regulator-2026-07-19`
(PR #4093) · **Axis:** Δ_λ magnitude — the b₄ He4-local 4-body term ·
**Tier:** structural derivation + pre-registered candidate test (scope-(a); no fit;
nothing wired). Builds on merged #4084 (the b₄ ss-pole) and the α-magic-criticality
result (`b4_isotope_pole_approach_probe.py`, this PR).

## 0. Where this sits

#4084 established that the derived per-bond magnitude `g_reeb = 1/√(1+[2]_v²)`
sits **exactly** on the q-deformed A=4 species-symmetric (ss) determinant pole, so
the single-scalar cumulant `b₄ = −ln det(I+g_reeb·S)` **diverges** — and no standard
zero-mode regulator rescued it (the reduced determinant is anti-binding,
`he4DetReduced_gt_one_at_pole`). The α-magic-criticality probe (this PR) then showed
⁴He is the *unique* light isotope on that pole. The open object is the **finite ⁴He
magnitude** = the pole regulator, redirected to a collective-coordinate moduli volume
(`Vol·ρ`). This note records the forward test of that route, and its **negative**
outcome.

## 1. The structure (formalize-first — legitimate, derived)

A functional determinant with an exact zero mode `v₀` (here the species-symmetric
`−√(1+[2]_v²)` eigenvector) is regularized by treating `v₀` as a **collective
coordinate**: integrate the flat direction out as a **volume** factor, leaving the
**reduced determinant** `det′` (product over the nonzero eigenvalues). The regulated
cumulant is

  `b₄^reg = ln(Vol) − ½·ln(det′) + C`,

with — and this is the one exact, substrate-derived handle —

  `det′ = (1 + g·λ_ss)(1 + g)(1 − g) = 2·(1 − g²) = 1.600869…`  (exact, at `m = g_reeb`).

So the *entire* open magnitude collapses to a **single geometric input**, the
zero-mode moduli volume `Vol`. This is a genuine narrowing: not a per-partition table,
not a scalar in `(0,1/√5)`, but one volume.

## 2. The forward test (pre-registered substrate candidates; the required Vol is a diagnostic)

> **⚠ The normalization is worse than "unverified" — it contradicts the one
> established datapoint.** The test below maps the cumulant to MeV via `B ∝ b^reg`
> (log-linear), calibrated on the deuteron `b₂ = −ln(1−g²) = 0.2226`. But the corpus's
> *actual* deuteron law is `B(²H) = 5·g = 2.234` MeV — **linear** in the magnitude `g`,
> not logarithmic in a determinant (`5g / b₂ = 10.03`, not a shared map). So there is
> **no established cumulant→MeV map**: `b₄ = −ln det` (log) and the deuteron `5g`
> (linear) are different functional forms, and the "required Vol" back-out silently
> assumes a log map that the only known datapoint refutes. The diagnostic below is
> therefore **ill-posed at the normalization level**, before any Vol candidate is even
> considered. This is the load-bearing gap.

Under that (refuted) log-linear normalization, the ⁴He ratio `ρ₄` implies a required
`Vol` — an AME **back-out diagnostic**, not a wired input:

| `ρ₄` source | required `Vol` |
|---|---|
| raw `B(⁴He)/B(²H) = 12.72` | 21.47 |
| isospin-corrected `≈ 13.03` (#4084) | 23.01 |

Pre-registered substrate volume candidates (named in advance, **no census scan**):

| candidate | value | vs required |
|---|---|---|
| `Vol(4₁)` fig-8 | 2.030 | — |
| `Vol(𝓑₃)` Borromean | 7.328 | — |
| `2·Vol(𝓑₃)` | 14.66 | — |
| `[2]_v⁴` | 16.09 | — |
| `3·Vol(𝓑₃)` | 21.98 | 2.4% vs raw (not forced) |
| `e^π` | 23.14 | 0.6% vs corrected — **⚠ numerology** |
| `[2]_v⁵` | 32.22 | — |

## 3. Verdict — scope-(a) negative; do NOT wire

**The collective-coordinate moduli-volume regulator, alone, with the pre-registered
substrate candidates, does not supply a forced forward `Vol`.** Three reasons this is
a wall, not a closure:

1. **The cumulant→MeV map is not just assumed — it is refuted by the deuteron.** The
   `B ∝ b^reg` log-linear map used for the back-out contradicts the only established
   datapoint: the corpus deuteron law is `B(²H) = 5·g` (**linear** in `g`), not
   `−ln det` (log); `5g/b₂ = 10.03`. So the "required Vol ≈ 23" is computed with a
   normalization the framework's own deuteron result rules out. **Fixing the
   cumulant→MeV map is the prior, load-bearing gap** — the Vol question is downstream of
   it and cannot be posed cleanly until it is settled (and note the deuteron is
   *sub-critical* while ⁴He is *at the pole*, so any single map is a cross-regime
   extrapolation across exactly the criticality this whole line concerns).
2. **⚠ The closest match, `e^π ≈ 23.14` (0.6%), is numerology.** `e^π` has **no**
   structural derivation as a zero-mode moduli volume in this framework. It is recorded
   here **only to warn future agents off wiring it** — per the standing anti-numerology
   / critical-distance discipline (AGENTS.md), a parameter-free-looking transcendental
   near-match with no categorical origin is a red flag, not a result.
3. **`3·Vol(𝓑₃)` (2.4%) is suggestive but not forced** — the factor 3 is unmotivated,
   the miss is real, and it too rides the unverified normalization.

Consistent with the corpus's already-walled Vol routes: the naive single-link `Vol₄`
for ⁴He is refuted (`vol4_4he_snappy_falsification`), and the q-rotational inter-cluster
term is a scope-(a) negative as sole mechanism
(`2026-07-13-inter-cluster-bond-term-derive-or-refute.md`). The **permanence principle**
holds: the exact `det′ = 2(1−g²)` piece and the α-magic-criticality structure stand;
only the `Vol` input is unsupplied.

## 4. What would actually close it (for the next agent)

**First**, a derived **cumulant→MeV map** — reconcile the deuteron's linear `5g` with
the `−ln det` cumulant, or establish which is the correct observable and how a
sub-critical (deuteron) value and an at-the-pole (⁴He) value share one scale. Only then
is the Vol question well-posed. **Second**, a *derivation* of the zero-mode moduli
volume from the substrate geometry — e.g. the collective-coordinate range of the
species-symmetric condensation mode as an S³/2I-localized or coordination-graph volume —
**not** a transcendental near-match to the back-out. Until both hold, the ⁴He magnitude
is open; the honest state is: regulator *structure* derived (`b₄^reg = ln Vol − ½ ln det′`,
`det′` exact), but neither the cumulant→MeV map nor `Vol` is supplied.

Refs: probe `computations/deltalambda/b4_isotope_pole_approach_probe.py`;
#4084 `B4CumulantBarEven.lean` (`he4DetViaEig_zero_at_pole`,
`he4DetReduced_gt_one_at_pole`); attack map
`docs/audits/2026-07-18-deltalambda-attack-vector-map.md` §4a.
