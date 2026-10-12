# Where a surface term could come from: the lit, and non-abelian Stokes unpacked

**Date:** 2026-08-30 · **Beans:** `qou-edt7`, `qou-brng` · **Scope: (a)** — nothing
derived, nothing refuted, nothing wired.

## 0. A correction first: the framework now HAS a surface term

Six commits ago I wrote that isolating the extensive term needs a derived surface
term "which the framework does not have". **That was true when written and is now
stale.** `QOU.Mass.SaturationPeakStructure` landed on `main` at 14:28 today
(`3109e09818`, sibling session, `qou-brng` R3), sorry-free, for the shape

    f(u) = a_V − a_S/u − a_C·u²,   u = A^(1/3)

with `perNucleon_lt_volume` (the curve never attains `a_V`), `volume_gap` (the
deficit is exactly `a_S/u + a_C·u²`) and rising/falling branch theorems.

**But it does not close the gap I named, and says so itself** (file docstring,
line 49): *"Nothing here derives `a_V`, `a_S` or `a_C`."* It is a theorem about
the SHAPE, valid for every parameter choice. So the surface term's **coefficient**
is exactly as open as before — which is the thing a derivation would have to
supply.

One interaction with my own last commit worth recording: that shape is smooth and
has a single interior maximum, whereas the measured N=Z fraction **dips** at A=6
(0.579) and is still below ⁴He at A=8 (0.767). A smooth volume−surface−Coulomb
curve cannot produce that dip. So the light-nucleus structure which IS the
extensive term is precisely what the smooth shape misses.

## 1. The literature — the exact paper is already held

`library/arxiv-1007.1250v4/` is **Amnon Yekutieli, "Nonabelian Multiplicative
Integration on Surfaces"** — the paper the canonical derivation chain cites at
step 2. Full text, pages 3–137, **261 KB, and greppable**.

**Ingestion note (worth a fix):** the whole body sits in ONE section file named
`sec-000-0-introduction.md`, with only a references stub beside it. The sectioner
did not split it. So a search for a mid-paper theorem hits a file called
"Introduction", and a reader checking the section list sees two entries and may
conclude the paper is a stub. It is not — the text is all there.

Also relevant: `library/arxiv-math-ph-0012035v3/` carries non-abelian Stokes
sections directly (operator formalism, higher-dimensional forms, 2D Yang–Mills).

## 2. Unpacking non-abelian Stokes: what actually pops out

> **🛑 CORRECTION (2026-09-06, bean `qou-h7w4`, PR #6936).** The reading below — that the bad
> set is "counted by the singularities of the map defining the surface", with `|bad(k)| ≤ m` for
> `m` the singular points of `σ` — is Yekutieli's **1-dimensional** string case (held text
> `library/arxiv-1007.1250v4/sections/sec-000-0-introduction.md:2280`), imported here into the
> 2-dimensional one. In 2-dim the kite map `τ : I² → X` is **linear by definition** (Def 4.1.1,
> `:3278`) and has no singular points; Def 4.4.12 (`:3964`) makes an index good **iff the
> connection forms `α|Zᵢ`, `β|Zᵢ` are smooth**; and Lemma 4.4.13's proof (`:3969-3976`) covers
> *the singular locus of α and of β* by `m` segments `Zⱼ`, setting `a₀ := 2m` and
> `a₁ := 2·Σ len(Zⱼ)` — a **length**, not a count. So the bad set is the singular locus of the
> **connection**, not of the surface parametrization; smooth forms give `a₀ = a₁ = 0` and no
> surface term of any size; and the corpus has no `(α, β)` as forms at all (`qou-20bk`: *"Step
> 2's curvature is stipulated, not a form"*). The bulk/boundary **split** described below is
> real; its attribution to the surface map is not. What survives is formalised in
> `QOU/Mass/StokesSingularCountAffine.lean`: Euler bounds the 1-skeleton of *any* cell
> decomposition below by `2 − χ = 9A + 1`, so **if** the forms' singular locus runs along one
> (hypothesis H1, not currently dischargeable) the Stokes term renormalises the volume coefficient.
> The text below is left as written, as the record of the reading being corrected.


The construction integrates a pair `(α, β)`, `α ∈ Ω¹⊗g`, `β ∈ Ω²⊗h`, over a
*kite* `(σ, τ)` — a 1-simplex and a 2-simplex — valued in a Lie crossed module
`(G, H, Ψ, Φ)`. The multiplicative integral is a limit of Riemann products over
refinements.

**The convergence estimate splits into two terms with different counting**
(p. ~8050 of the held text):

    ‖log MI(α,β|σ,τ) − RS_k‖ ≤ c₀(H)·[ 8^k·(½)^{4k}·ϵ⁴·c₁₀(α,β)
                                     + (a₂·4^k + a₀)·(½)^{3k}·ϵ³·c₆(α,β) ]
                                 └─ good ─┘        └──── bad(τ,k) ────┘

and the bad set is bounded (Def. 4.4.12 / Lemma 4.4.13) by

    |bad(τ,k)| ≤ a₀(α,β,Z) + a₁(α,β,Z)·2^k

**That is a bulk/boundary split, in the construction itself, not by analogy.**
The good term is counted by 2-cells — an AREA count. The bad term grows as `2^k`
against the `4^k` of a 2-dimensional refinement: **one dimension down**, a
perimeter count. The two also carry different powers of the scale, `ϵ⁴` vs `ϵ³`.

**What the bad set IS** (the 1-dimensional case states it most plainly, p. ~2280):
an index is *good* if the map restricted to that cell is **linear and injective**;
otherwise *bad*. And

    |bad(k)| ≤ m,  m = the number of SINGULAR POINTS of the map σ
    if σ is linear, bad(k) = ∅

So the correction term is counted by **the singularities of the map defining the
surface** — a finite, integer, geometric quantity, vanishing exactly when the
surface is non-singular.

## 3. What this does and does not give

> **🛑 CORRECTION (2026-09-06, `qou-h7w4`).** "`a_S` … proportional to a count of singularities
> of the spanning surface … an integer knot invariant … checkable against the N=Z chain" inherits
> the §2 misreading. The count is of the *connection's* singular locus (`a₀ = 2m`); the other
> constant `a₁` is a length; both vanish for smooth forms. The prediction is therefore **not
> checkable** until `(α, β)` exist as forms — it is conditional on H1 of
> `StokesSingularCountAffine.lean`, and under H1 the count is bounded below by Euler (`≥ 9A + 1`),
> i.e. affine in `A`, i.e. a volume-coefficient renormalisation rather than an `A^(−1/3)` term.
> "Does not give a magnitude" below stands, and is now the weaker of the two limitations.


**Gives — a falsifiable structural prediction.** If the framework's surface term
arises this way, then `a_S` is not a free parameter: it should be proportional to
a **count of singularities of the spanning surface** of the nuclear braid closure
— an integer knot invariant. That is checkable against the N=Z chain and is not
an ansatz; it is what the construction forces.

**Does not give — a magnitude.** `a₀`, `a₁`, `a₂`, `c₆`, `c₁₀` are constants
"depending only on `α`, `β`": they appear in **inequalities**, as bounds. A
coefficient cannot be read off a bound. This is the same shape-without-magnitude
wall the whole arc keeps hitting, and honesty requires saying that unpacking
Stokes does not by itself break it.

## 4. The standing constraint on this route — read before pursuing it

`fsh-guts/deprecated/computations/yekutieli-purged/README.md`: the Yekutieli per-cell
curvature extension `λ_Y = λ_A − G·h²` was **PURGED from production**
(2026-05-24, `71d674da1`), because the S₄↓S₃ half-symmetric projection bijection
gave **κ = +0.5** rather than the expected `−G`, falsifying the claim that the
per-cell curvature accounts for the linking-weight correction.

**Precision matters here.** What was purged is **one ansatz built on the theorem**,
not the theorem. The reanimation policy is explicit: this stays deprecated
*"unless a Lean-proved categorical derivation of the Yekutieli per-cell correction
lands (with a positive bijection result, not κ = +0.5)"*, coordinated with the
canonical-watcher through the Rule-14 escalation.

So this route is **permitted and gated**, not forbidden — and the gate is exactly
the standard a derived `a_S` would have to meet anyway.

## 5. Honest status

Scope-(a). No mechanism is proposed, no number is derived, nothing is wired. What
changed: the surface term's *shape* is now a theorem on `main` but its
*coefficient* is not derived; the on-point source is held and greppable; and
non-abelian Stokes, unpacked, supplies a bulk/boundary split whose boundary term
is counted by surface singularities — which is a testable prediction about what
`a_S` should be proportional to, and not yet a value for it.
