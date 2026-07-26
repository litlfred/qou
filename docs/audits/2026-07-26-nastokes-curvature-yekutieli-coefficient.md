# Is the −π²/3 Part-B shift the non-abelian surface-ordering curvature of the Yekutieli multiplicative integral? — investigating `lem:yekutieli-leading-coefficient`

**Date:** 2026-07-26 · **Branch:** `claude/dilog-nastokes-curvature-2026-07-26` · PR #4357 ·
**Beans:** qou-tw5z (this note), qou-zbcj (secondary conjecture) ·
**Tier:** honest open-research finding — **no fit, no scan, nothing wired to production**.

## The question (from the coordination ledger, 2026-07-26 owner insight)

The owner's na-Stokes insight — "limits need to follow na-Stokes, which I guess is
path-ordered exponential" — resolves MQ1 (iterated vs joint ordering) on physical
grounds: a holonomy / `𝒫exp` is intrinsically ordered, so the physical limit is the
**iterated** one proved sorry-free in #4343 (`wp1_bulk_tendsto` then `wp1_outer_tendsto`,
[`DilogPartBIteratedLimit.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/DilogPartBIteratedLimit.lean)).

The ledger then flagged a **"concrete lead"** for MQ2/MQ3: that the −π²/3 Part-B shift
might be the *non-abelian surface-ordering curvature/commutator term* of the
multiplicative integral, and that
[`lem:yekutieli-leading-coefficient`](../../content/quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md)
("the Yekutieli obstruction = the leading Chebyshev coefficient") "already has a corpus
handle" — so "the MQ2/MQ3 target is to show that coefficient evaluates to −π²/3."

This note investigates that lead. **Verdict: the lead is a misidentification. The
leading Chebyshev coefficient is `1`, a discrete `H²` topological obstruction integer;
it cannot and does not equal −π²/3. And in the sector where −π²/3 actually appears
(the scalar τ-shadow), the corpus's own Lean proves the surface-ordering curvature term
*vanishes*. So the curvature = −π²/3 identification is `no-match`. The na-Stokes
*ordering selection* (MQ1) is separately sound (`structural-partial`).**

## 1. What `lem:yekutieli-leading-coefficient` actually states and computes

Statement (`.md`): for `T_{2,p}` at level `n = g+1 = 5`, the Yekutieli obstruction
`κ(T_{2,p}) ∈ H²(𝓢, 𝓑)` equals the leading Chebyshev coefficient `c_{(p−1)/2} = 1`;
hence `κ ≠ 0` for `q ≠ 1`.

The Lean triple
([`yekutieli_leading_coefficient.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/yekutieli_leading_coefficient.lean))
makes precise what the "leading Chebyshev coefficient" is:

- **The genus-filtration basis is the MONIC Chebyshev recurrence** `monicCheb`
  (`p₀ = 1`, `p₁ = X`, `p_{n+2} = X·p_{n+1} − p_n`). `monicCheb_monic` proves it monic
  of degree `n`. Therefore `leadingChebyshev S p = (monicCheb S ((p−1)/2)).leadingCoeff = 1`
  outright (`leadingChebyshev_eq_one`, sorry-free).
- **The obstruction's genus coordinate** is `κ_raw = q⁻¹(1 − q⁻¹) · w · ν`
  (the `d_q²` curvature, `prop:categorical-dq-squared`), with `w = 5` the top Seifert
  weight and `ν` the `q`-wedge — **unit-normalised to `1`** by the class field
  `raw_normalised` in `YekutieliStokesNormalisation`.
- The main lemma **derives** `obstructionCoord = leadingChebyshev = 1`.

**So the coefficient computes to exactly `1`.** It is:
- a **discrete integer / `H²` obstruction class** — a *topological* non-vanishing
  certificate ("does the 5th Seifert cycle lift? no"),
- **degree/genus-filtration data** (a Chebyshev *leading coefficient*, i.e. a monic
  normalisation), and
- **parameter-free**: there is no series, no limit, no `q`-evaluation left in it — it is
  identically `1` (the monicity of the basis). The `q`-dependence lives only in the *raw*
  `κ_raw = q⁻¹(1−q⁻¹)·5·ν`, whose role is to certify `≠ 0` at `q ≠ 1`, and which is
  normalised away.

### Does it (or a natural multiple/limit) evaluate to −π²/3, −π²/6, ζ(2), or a dilog value?

**No.** The coefficient is `1`; no multiple of a fixed `1` is a transcendental, and
there is no limit to take (it is constant in every variable). The only object with any
`q`-content is `κ_raw = q⁻¹(1−q⁻¹)·5·ν` — a **rational function** in `q` times an
*undetermined geometric factor* `ν`. It is not a transcendental, and setting it to
−π²/3 would require freely tuning `ν` (a fit, not a derivation). There is no structural
map from a monic leading coefficient / `H²` integer to `ζ(2)`.

**Classification of the direct "coefficient = −π²/3" reading: `no-match`.** The
ledger's lead conflates two objects living in different categories of the framework's
own fibre-vs-shadow taxonomy:

| Object | Type | Value | Sector |
|---|---|---|---|
| `κ(T_{2,p})` = leading Chebyshev coeff (this lemma) | discrete `H²` obstruction / genus-degree | `1` | topological, `q`-algebraic |
| −π²/3 Part-B shift | archimedean transcendental limit `= −2ζ(2) = −2·Li₂(1)` | `−π²/3` | analytic, τ-shadow at the cusp |

## 2. Where −π²/3 actually comes from — and why it is an *abelian* dilog value, not a commutator

The −π²/3 is fully accounted for by the **sorry-free** archimedean bricks, with no
curvature/commutator anywhere:

- **W-P1** (`wp1_outer_tendsto x`, #4343): the iterated bulk limit is
  `Li₂(x) − π²/6`, the OUTER `ρ→1⁻` Abel limit `Li₂(ρ) → π²/6 = Li₂(1)`
  (`tendsto_LiTwo_nhdsWithin_lt_one`, sorry-free).
- **W-P2** (`euler_tail_asymptotic`,
  [`DilogPartBEulerTail.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/DilogPartBEulerTail.lean)):
  the Euler / Dedekind-eta tail `→ π²/6 = ζ(2)`.
- **Total:** `(Li₂(x) − π²/6) − π²/6 = Li₂(x) − π²/3` (consistent with the 2026-07-17
  pole-cancellation audit's regularized `Li₂(x) − π²/3`).

So structurally **−π²/3 = −2ζ(2) = two boundary/cusp `Li₂(1)` contributions** — one from
the W-P1 Abel/left-continuity limit at the cusp, one from the W-P2 tail. Both are
**values of the ordinary (abelian) dilogarithm at 1**. `Li₂` *is* the classical abelian
regulator (`−∫ log(1−t)/t dt`); the corpus states this explicitly
([`yekutieli-quantum-li.md`](../../content/quantum-observable-universe/q-geometric-langlands/yekutieli-quantum-li.md):
"This structure is purely abelian";
[`algebraic-geometric-dilog-equivalence.md`](../../content/quantum-observable-universe/mass-theory/algebraic-geometric-dilog-equivalence.md):
`τ_arch(Φ_n) → D(z) = Vol_hyp`, the abelian Bloch–Wigner regulator).

### The corpus's own Lean proves the surface-ordering curvature *vanishes* in this sector

The Part-B sum is the scalar `τ`-shadow `Φ_n = ∏(1−xqᵏ)⁻¹ ∈ ℝ` — a product of
**commuting scalars**. Three independent corpus facts show the non-abelian
surface-ordering term is *not* what produces −π²/3 here:

1. **`holonomy_perm`** ([`YekutieliIntegration.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/YekutieliIntegration.lean),
   sorry-free): in a `CommMonoid` the path-ordered holonomy is **permutation-invariant** —
   "the path-ordering collapses … the classical limit where Yekutieli's non-abelian
   Stokes reduces to ordinary (abelian) Stokes and the surface-ordering is irrelevant."
   The scalar `Φ_n` lives in the commutative `ℝ`; its ordering defect is *identically
   zero*. A commutator term cannot appear in a commutative product.
2. **`mi-sw-abelianisation`** ([`.md`](../../content/quantum-observable-universe/brings-surface/mi-sw-abelianisation.md)):
   the non-abelian MI restricted to the exceptional `ℙ¹` **abelianises** to the
   Seiberg–Witten period `|a_D^{(n)}|`. The archimedean shadow is by construction the
   *abelian* period, not a commutator defect.
3. **`germ-commutator-q-curvature`** ([`.lean`](../../content/quantum-observable-universe/quantum-observable-universes/germ-commutator-q-curvature.lean)):
   the genuine curvature = commutator identity `[δq₁, δq₂] = F_q` lives over a
   **non-commutative `Ring R`** — the *fibre* level (Hecke `σ_i`, germ algebra `A/𝔪_p²`).
   This is the same fibre-vs-observable split as the `Im(q)` banner: non-commutativity is
   fibre-level; the observable τ-shadow is abelian.

**Classification of "−π²/3 = non-abelian surface-ordering curvature/commutator term":
`no-match` (in the scalar sector where −π²/3 lives) / at best `numerical-coincidence`.**
The value −π²/3 is an *abelian* dilog boundary constant `−2·Li₂(1)`; the surface-ordering
commutator term in that (commutative) sector is provably `0`. Calling −π²/3 "the
non-abelian curvature/anomaly" is a category error: it would require the term to live at
the non-commutative *fibre* level, but −π²/3 is computed in the commutative *shadow*.

A *fibre-level* commutator story (lift `Φ_n` to the non-commutative Hecke holonomy and
compute its genuine curvature defect) is **not done in the corpus** and is **not**
supplied by `lem:yekutieli-leading-coefficient` (which measures genus-filtration degree,
an orthogonal invariant). Whether some fibre-level commutator independently evaluates to
−π²/3 is an untested, separate, hard open question — but it is *not* what the "leading
Chebyshev coefficient" lead offered, and it cannot be read off the scalar Part-B sum.

## 3. What *is* sound: the ordering selection (MQ1)

The owner's core insight — that a `𝒫exp` is intrinsically ordered, so the physical limit
is iterated, not joint — is **`structural-partial`** and corpus-supported:
`YekutieliIntegration.holonomy` is `List.prod` (ordered by construction);
`holonomy_perm` shows the joint/symmetric limit is legal *only* in the abelian
degeneration. So the ordering *selection* is principled. It is **not yet Lean-proved**
that the specific scalar `Φ_n` *is* the Yekutieli MI of the specific `𝐂`-connection with
the `(ρ then q)` refinement order (bean qou-zbcj) — that identification is the honest
remaining conjectural bridge, and it is the *hypothesis* (not the conclusion −π²/3) that
a conditional class may axiomatize.

## 4. Honest bottom line

| Sub-claim | Classification | Evidence |
|---|---|---|
| na-Stokes selects the **iterated** ordering (MQ1) | `structural-partial` | `holonomy` = ordered `List.prod`; `holonomy_perm` (joint legal only if abelian); not Lean-proved for the specific `Φ_n` |
| "leading Chebyshev coefficient = −π²/3" (the ledger lead) | **`no-match`** | coefficient is `1` (monic normalisation / `H²` integer); a discrete topological invariant, not a transcendental |
| "−π²/3 = non-abelian surface-ordering curvature/commutator" | **`no-match`** (scalar sector) | −π²/3 = −2·Li₂(1), an *abelian* dilog constant; `holonomy_perm` ⇒ ordering defect = 0 in the commutative τ-shadow; commutator lives at the *fibre* level (`germ-commutator-q-curvature`) |
| some *fibre-level* commutator = −π²/3 | **untested / open** | would need lifting `Φ_n` to the non-commutative Hecke holonomy; not in corpus; not provided by this lemma |

**The −π²/3 is derived (sorry-free, #4343 + euler-tail) as an abelian dilog cusp value,
not as a non-abelian curvature anomaly.** The na-Stokes picture correctly *selects the
ordering*; it does *not* supply a curvature *value*, and the `lem:yekutieli-leading-coefficient`
handle is a misidentification. This is an honest negative on the MQ2/MQ3 curvature lead;
the MQ1 ordering selection stands as principled-but-not-yet-formalised, and is the honest
target of the conditional class (bean qou-zbcj) — which axiomatizes the *ordering
identification* (hypothesis) and derives the value from the proved bricks, **never** the
reverse.

*No fit. No scan. Nothing wired to production. The block `lem:yekutieli-leading-coefficient`
and its status are unchanged by this note.*
