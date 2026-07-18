# α_EM per-loop measure: is a count-carrying object's `Σd_i² = 8` forced by Bring topology, or fitted?

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure · **Tier:** measurement
(scope-(a) NEGATIVE on the categorical-`Σd_i²` route + a POSITIVE consolidation of
the `1/b₁` leg; no `α_k` wired; no fit; `1/(8π)` stays a phase-4 identification) ·
**Branch:** `claude/alpha-em-count-carrying-object-2026-07-18` · **Probe:**
[`alpha_em_count_carrying_object_probe.py`](../../computations/alpha_em/alpha_em_count_carrying_object_probe.py)
· **Witness:**
[`alpha-em-count-carrying-object.witness.json`](../../computations/alpha_em/alpha-em-count-carrying-object.witness.json).

## The redirect this executes (from #3889)

The per-loop measure is `1/(π·b₁) = 1/(8π)`, `b₁ = dim H¹(M_Bring) = 2g = 8`
(genus-4 Bring surface, `Jac(Bring) ~ E⁴`). #3889 confirmed the *reciprocal
`1/D` form* the torsion redirect (#3882) predicted — `S_{00} = 1/D`,
`D = √(Σd_i²)`, the RT/WRT modular-`S`-matrix total quantum dimension — but the
genuine Σ(2,3,5) icosahedral / Fibonacci MTC gives `Σd_i² = (5+√5)/2 ≈ 3.618`,
neither `8` nor `8π` (only 2 primary fields, far too few for the `b₁ = 8`
harmonic-1-form count). Its *sharpened next redirect* is this probe's exact task:

> find a count-carrying category whose total quantum dimension `Σd_i² = 8`,
> **DERIVED from the genus-4 Bring topology** (`b₁ = 8`), **NOT fitted to 8**.

## Why this is the high-risk anti-laundering case

`Σd_i² = 8` is trivially easy to **fit**: any order-8 abelian group, `ℤ₂³`,
`U(1)_8`, or "8 copies of anything" gives it. The **entire value** is whether `8`
is *forced* by the topology or *hand-picked* to match `b₁`. Per AGENTS.md
§"Axiomatization is NOT a Proof", §"Before declaring refuted" (the (a)/(b)
classification), and the Subgoal-2 "open for all but the anti-fit discipline STILL
STANDS" ruling, the honest **NEGATIVE** — no natural object forces `8` — is a
**good, preferred outcome**. Two numbers must be kept distinct throughout:

- **`2g = 8`** — the Betti number `b₁ = dim H¹`, a genuine **topological count**.
- **`|discriminant group| = 8`** — a **lattice/level** invariant that depends on
  the level and is **not** automatically `2g`.

The whole trap is conflating them. No CODATA is read; no convention is tuned
toward `8`.

## Method — enumerate the natural objects, compute `Σd_i²` exactly

The probe builds each candidate directly from the fixed Bring genus-4 data
(`g = 4`, `b₁ = 8`, `Jac ~ E⁴`, the `S₅`/`ℤ₅` action on `H¹`) and computes its
total quantum dimension in closed form, tagging the count **forced** (a topological
invariant), **fitted** (a level/group chosen to hit 8), or **relabel** (`b₁` in an
object-count costume).

### Per-candidate `Σd_i²` table

| tag | candidate | `Σd_i²` | `= 8`? | count | verdict |
|---|---|---|---|---|---|
| **A** | abelian anyonic theory of `Jac(Bring)` = discriminant form of `(H¹(ℤ), intersection)` | **1** | **no** | **FORCED** | kills the naive abelian-Jacobian route |
| **B** | level-`k` / `U(1)_k` abelian theory on `H¹` | `k` (=8 if `k=8`) | only if `k=8` | **FITTED** | level not forced (principal polarization = level 1) |
| **C** | the `2g = 8` harmonic 1-forms (`ℤ₅` `χ₁⊕χ₂⊕χ₃⊕χ₄`, each 2-dim) as `d=1` objects | **8** | yes | **RELABEL** | `= b₁` relabelled; zero new categorical content |
| **D** | Drinfeld-double / group-theoretical from `S₅` or `2I` | `|G|²` (or 8 for `ℤ₂³`) | only if `G` chosen | **FITTED** | `S₅` has no order-8 quotient; `ℤ₂³` not a Bring invariant |

### (A) — the decisive kill: the Jacobian's abelian theory gives `1`, not `8`

The photon target is `J(M) = H¹/H¹(ℤ)`, and the "abelian anyonic theory of the
Jacobian" is the **discriminant form** of the lattice `(H¹(Bring;ℤ), intersection
form)`. For a **closed oriented genus-`g` surface** the intersection (cup-product)
form is **UNIMODULAR** by Poincaré duality — the standard symplectic lattice
`⊕^g H`, `H = [[0,1],[-1,0]]`, with `det = 1`. The probe builds this Gram matrix
for `g = 4` and verifies:

- `|det Gram| = 1` (unimodular), and its integer **Smith normal form is all 1s**
  ⇒ the discriminant group `A_L = L*/L` is **trivial**, `|A_L| = 1`.

A metric/abelian anyon theory has **one simple object per discriminant-group
element**, all `d_i = 1`, so `Σd_i² = |A_L| = 1` — **NOT 8**. The count *is* forced
by topology, and the topology **forces `1`**. This is exactly the honest
distinction the task demanded: `2g = 8` is the Betti number, `|disc| = 1` is the
lattice invariant, and the abelian-anyon count is the **latter**. The naive
"abelian theory of the Bring Jacobian → `Σd_i² = 8`" route is **structurally
dead**.

### (B), (D) — reaching 8 requires a chosen level / group (fit)

- **(B)** A `U(1)_k` / rescaled-lattice (WZW abelian) theory has `k` anyons,
  `Σd_i² = k`. Hitting `8` needs level `k = 8`. But `Jac(Bring)` carries a
  **principal** polarization — the unimodular form is "level 1" — so **no level is
  forced**, least of all `8`. Choosing `k = 8` to match `b₁` is a fit.
- **(D)** A Drinfeld double `D(G)` has `Σd_i² = |G|²` — `D(ℤ₂) = 4`, `D(D₄) = 64`,
  neither `8`. The metric group `ℤ₂³` gives `8` anyons `Σ = 8`, but `ℤ₂³` is not a
  Bring invariant. `S₅` (`|S₅| = 120 = 2³·3·5`) has **no natural order-8
  quotient**; its order-8 Sylow-2 (dihedral `D₄`) is a **subgroup**, and only *one*
  of the *eight* subgroup classes giving genus-1 quotients (`S₄, A₄, D₆, D₄, S₃,
  C₆, C₂², C₄`, per #2701 / the `E⁴` decomposition). Picking the `|·| = 8` one to
  match `b₁` is a fit. `2I` (`|2I| = 120`) gives nothing of order 8 naturally.

### (C) — `Σd_i² = 8`, but it is `b₁` in a costume

Declaring the `8` harmonic 1-forms (equivalently `4` complex forms `⊕` `4`
conjugates, or the four 2-dim `ℤ₅`-isotypical characters `χ₁⊕χ₂⊕χ₃⊕χ₄` that sum
to `8`) as "`8` simple objects, each `d = 1`" gives `Σd_i² = 8` — but there is **no
fusion / braiding / modular structure**. It is literally the vector-space dimension
`dim H¹ = b₁ = 8` wearing an object-count costume. This reproduces `8` with **zero
new categorical content** — a **relabelling** of the Betti number, not a derivation
of a `Σd_i²`.

## Verdict — scope-(a) NEGATIVE on the categorical route; consolidation of `1/b₁`

**Pre-registered kill criterion (met).** Every natural object either gives
`Σd_i² ≠ 8` under a *forced* topological count (A: the unimodular-Jacobian
`|disc| = 1`), or requires *choosing* a level/group/labelling to hit `8`
(B, D — fit), or *relabels* `b₁` with no new content (C). **No natural object
FORCES `Σd_i² = 8`.**

Therefore: **`1/b₁` from a categorical `Σd_i²` is not derived.** `b₁ = 8` enters
as the **Betti number directly** — the #3834 `ζ_{Δ₁}(0) = −b₁` count — not through a
quantum-dimension sum.

**The consolidation (the honest positive).** The `1/b₁` leg is **already
DERIVED** as the plain Betti count: #3834 / #3831 proved `ζ_{Δ₁}(0) = −b₁`,
area-free (the Epstein-zeta `−1/s` residue, covolume-independent), and #2114 proved
`b₁ = 2g = 8` on the genus-4 Hodge data (sorry-free Lean `PhotonIRZeroMode`).
Re-routing the count through the `Σd_i²` of an MTC is an **unnecessary detour**: it
either reproduces `8` trivially (candidate C, a relabelling) or fails (A) / fits
(B, D). The #3889 reciprocal-`1/D` *form* was the right structural intuition for
"where a `1/(total-count)` comes from", but the count it needs is the **Betti
number the framework already has** — dressing it as a quantum-dimension sum adds no
derivational content and (worse) invites a fit.

**The remaining open item is single and archimedean.** With `1/b₁` consolidated as
the derived Betti count, the *only* genuinely open factor of the per-loop measure
`1/(π·b₁)` is the **`1/π`**: the archimedean 1-loop determinant / heat-kernel
eigenvalue normalization `4π²` (the `log(4π²)` in `ζ'_{Δ₀}(0)`, #3882), the same
heat-kernel object as the proved zero-mode measure `1/Area = 1/(12π)`. This is
consistent with the ledger's standing boundary **"`b₁` topological, π archimedean,
`[2]_q` substrate"** (PR #2114) and with #3889's own conclusion that **π is the
universal archimedean 1-loop factor, never categorical**. The per-loop measure is a
**product** of a derived topological count-reciprocal (`1/b₁`, Betti) and an
archimedean `1/π` — and the categorical `S`-matrix `Σd_i²` is **not** the home of
the count.

## Controls (all pass, witness `allPassed = true`)

- **Unimodularity ⇒ `|disc| = 1`:** `|det(⊕^4 [[0,1],[-1,0]])| = 1`; Smith normal
  form all 1s ⇒ trivial discriminant group (order 1). [Standard: the intersection
  form on `H¹` of a closed oriented surface is unimodular by Poincaré duality.]
- **`2g = 8`** for the genus-4 Bring surface.
- **Icosahedral `Σd_i² = 1 + φ² = (5+√5)/2 ≈ 3.618 ≠ 8`** (cross-check vs #3889's
  machine-validated genuine Σ(2,3,5) `S`-matrix).

## Kill criteria (pre-stated, and how they resolved)

- **Negative** if every natural object gives `Σd_i² ≠ 8` or needs a chosen
  level/group/labelling → report scope-(a) NEGATIVE, do **not** manufacture a
  fitted `8`. → **Met.** (A) forced→1; (B)/(D) fitted; (C) relabels `b₁`. Reported
  negative; nothing fitted.
- **Positive** only if a *forced* topological invariant of the Bring Jacobian is
  *independently* `8` (a genuine `Σd_i²`, not `b₁` relabelled). → **Did not
  occur** — the one forced lattice invariant (the discriminant order) is `1`.

Anti-laundering respected: no CODATA read, no convention tuned toward `8`, `2g = 8`
(Betti) kept distinct from `|disc| = 1` (lattice), controls checked against #3889's
closed forms.

## Cross-references

- #3889 `S`-matrix per-loop redirect (the immediate predecessor / this task's source): [`2026-07-18-alpha-em-smatrix-perloop-quantum-dimension.md`](2026-07-18-alpha-em-smatrix-perloop-quantum-dimension.md)
- #3882 torsion redirect ("measure lives on the S-matrix"): [`2026-07-18-alpha-em-torsion-perloop-redirect.md`](2026-07-18-alpha-em-torsion-perloop-redirect.md)
- #3870 flat-torus Maxwell (the three-axis constraint origin): [`2026-07-18-alpha-em-flat-torus-maxwell-perloop.md`](2026-07-18-alpha-em-flat-torus-maxwell-perloop.md)
- #3834 `ζ_{Δ₁}(0) = −b₁` — the area-free DERIVED Betti count (the consolidation's anchor): [`2026-07-17-alpha-em-zeta-anomaly-b1-count.md`](2026-07-17-alpha-em-zeta-anomaly-b1-count.md)
- #3612-era forcedness (`D = 8` data-selected to ~3500σ — the target, NOT read back in): [`2026-07-17-alpha-em-perloop-integer-forcedness.md`](2026-07-17-alpha-em-perloop-integer-forcedness.md)
- Bring Jacobian `E⁴` elliptic W-plane + the `S₅` subgroup-quotient table: [`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md)
- Ledger: [`alpha-em.md`](../coordination/alpha-em.md)
