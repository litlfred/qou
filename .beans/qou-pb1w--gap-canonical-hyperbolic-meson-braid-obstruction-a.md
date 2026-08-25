---
# qou-pb1w
title: 'GAP: canonical hyperbolic meson braid (Obstruction A) — the corpus braid is Vol=0'
status: completed
type: task
priority: normal
created_at: 2026-08-24T19:24:22Z
updated_at: 2026-08-24T21:23:18Z
---

## Measured, not asserted: the corpus's meson braid closes to T(2,5) with Vol = 0

Full analysis: `docs/audits/2026-08-24-meson-braid-obstruction-a-measured.md`.

`def:categorical-meson` fixes `𝔐 = (σ₀σ₁)²·σ₁σ₀` (6 crossings, 3 strands). Closed
and measured in SnapPy 3.3.2: **1 component, Vol = 0, "contains flat tetrahedra"**.
Knot group relator `aabbbbb` = `⟨a,b | a² = b⁵⟩` ⇒ **T(2,5) = 5₁**, the cinquefoil
— the knot the corpus assigns to the MUON. Control: Borromean `(σ₀σ₁⁻¹)³`
reproduces `2·V_oct = 7.32772475342` to 11 places, so the pipeline is sound.

**So under `m(K) = m_e·Vol(K)·ρ(K)/ℏ_q²` the corpus's own pion braid gives
m_π = 0.** Obstruction A is a property of the construction already written down,
not a gap in an unrun search.

**Diagnosis.** `lepton-meson-parallel` says the binding Hopf link "introduces
negative crossings via σ⁻¹ = σ − h". True in the HECKE ALGEBRA — `L₋` appears in
the normal form with coefficient `h` — but the BRAID WORD is entirely positive.
Negative crossings in a normal-form coefficient are algebra; volume sees only
geometry. The construction conflates the two.

## Targets (ℏ_q² = 0.00981718645427507381, proton pin)

    Vol·ρ needed = (m/m_e)·ℏ_q²
      π±  2.681392089      K±  9.484401401     K⁰  9.559980444
      η  10.52539033       D⁰ 35.82684854      J/ψ 59.49688298
      η_c 57.3259547       (μ: 2.029882787 = Vol(4₁), the anchor)

## A correction to my own first prune

I first concluded "no positive 3-braid closure is hyperbolic, so the construction
must admit σ⁻¹". **FALSE** — of 2044 positive words of length 2–10, **208** have
hyperbolic closures. My sample was deduplicated by volume and length-limited,
under-representing positive words. An inference from a filtered sample, presented
as structural: the error class this corpus keeps punishing.

**What survives is sharper.** Minimum hyperbolic volume over positive 3-braids
(len ≤ 10) is **4.851171**; the pion needs **2.681**. So *at ρ = 1* the pion lies
BELOW the whole positive-braid hyperbolic spectrum, while mixed-sign words reach
2.0299 (`4₁`) and 2.8281 (`5₂`). CONDITIONAL prune — `ρ` is not 1 in general — so
it constrains `(braid, ρ)` jointly, never the braid alone.

## Next tool: the Murasugi/Schreier normal form (formalize-first)

Every 3-braid is conjugate to `Δ^{2ℓ}a^p`, `Δ^{2ℓ+1}`, `Δ^{2ℓ}ab`, `Δ^{2ℓ}(ab)²`,
or `Δ^{2ℓ}a^{-p₁}b^{q₁}⋯a^{-p_r}b^{q_r}`, and hyperbolic-closure volume bounds are
expressed in the syllable count `r` (Futer–Kalfagianni–Purcell). That converts
"search the braid space" into "solve for `(ℓ, p_i, q_i)` admitting a target
volume" — narrow first, check once. The corpus library carries the
volume-conjecture line but NOTHING on closed-3-braid classification; that is the
literature gap. FKP constants are NOT quoted — search-result summaries only, the
papers were not fetched, and `search_arxiv` is returning empty for every query
(tool failure, not absence of literature).

## Blocking question for the author (decide BEFORE any search)

Must the meson braid close to a **knot** or may it be a **link**? `𝔐` closes to a
knot, but `q̄q` is a two-constituent state, and the 2-component hyperbolic
candidates (Whitehead 3.664; words at 4.060, 4.749, 6.138) are otherwise
inaccessible. This changes the candidate space before a single volume is compared.

**NO braid proposed and NO mass checked.** Nearest enumerated volume to the pion
is `5₂` at 5.47 % — the distance to the nearest point of a dense set, not a
result; selecting on it would be the per-state fit the J/ψ attack already recorded
as worthless.


## The heavy end IS bounded — and at the dictionary's own length, D⁰ is excluded

I recorded the heavy end as "not yet bounded". It bounds, and the answer is a hard
no at the crossing count the corpus itself assigns.

    meson  dict crossings   max Vol @ that length   Vol·ρ needed   verdict
    π      3+3 = 6          7.32772                 2.681          reachable
    K      3+5 = 8          12.35091 (EXHAUSTIVE)   9.484          reachable
    η/φ    5+5 = 10         >= 14.334               10.525         reachable
    D⁰     5+3 = 8          12.35091 (EXHAUSTIVE)   35.827         SHORT by 2.9x
    J/ψ    5+5 = 10         >= 14.334               59.497         SHORT by >=4.2x

**Length 8 is EXHAUSTIVE, not sampled** — all `4·3⁷ = 8748` words on
`{σ₀^±1, σ₁^±1}` with no adjacent cancellation; max hyperbolic volume over all of
them is `12.35091`, attained at `[1,-2,1,-2,1,-2,1,-2]`. Length 9 likewise
(`4·3⁸ = 26244`).

**So no 3-braid word of the D meson's own dictionary length can carry its mass,
whichever word is chosen.** Scope-(a): of *this length at this density*, not of
the hyperbolic mechanism.

Max hyperbolic Vol by word length (4–9 exhaustive; 10–18 sampled, 6000 seeded
random words each ⇒ those are **lower bounds**, not maxima):

    len   4     5     6     7     8      9      11     14     18
    Vol   2.030 3.664 7.328 8.997 12.351 13.948 ≥17.30 ≥19.17 ≥25.77

Growth ≈1.5–1.7 per letter at the top, so on that trend D⁰ needs `L ≈ 24` and
J/ψ `L ≈ 40` — 3–4× their dictionary lengths.

### Two assumptions this rests on — both are author questions, not conclusions

1. **`ρ = 1`.** The per-block density is not 1 in general; a large `ρ` relaxes the
   requirement proportionally and could dissolve the exclusion outright.
2. **Dictionary crossings = braid WORD LENGTH**, rather than the closure's minimal
   crossing number. The corpus's own `𝔐` has word length 6 and closure crossing
   number 5, so the two genuinely differ.

Either could dissolve it. That is why they go to the author rather than into a
verdict — and it is the difference between a prune and an over-claim.

## ✅ CLOSED 2026-08-24 — the LP-selected operator is provably not a braid

Settled symbolically over `ℚ(q)`, not by search. Probe:
[`computations/meson/operator_selection_lattice_symbolic.py`](../computations/meson/operator_selection_lattice_symbolic.py).

**Lattice — NOT the obstruction.** `Ψ = D·Φ* = (−q³, −q⁴, N, −q⁵, qN, −q⁶)`
with `N = q⁶+q²+1`, `D(q) = q⁷−q⁵−q⁴+q²+q+1 = (q+1)(q⁶−q⁵−q³+q²+1)`. Every
entry is a polynomial with integer coefficients, so `Φ*` lies in the
`ℤ[q,q⁻¹]`-lattice up to one scale. Integrality was a genuine candidate
obstruction and it does not fire.

**Character — this IS the obstruction.** In `H₃(q) ≅ ℚ(q) ⊕ M₂(ℚ(q)) ⊕ ℚ(q)`
every braid word of exponent sum `e` sits at `χ_sym = qᵉ`,
`det ρ_std = (−1)ᵉ`, `χ_alt = (−1/q)ᵉ`, so it satisfies the scale-free,
exponent-free identity `χ_sym·χ_alt = det ρ_std`. Two facts close it:
`χ_alt(Ψ) = 0` — because `χ_alt(x) = v·x` **is** the quotient condition — and
along the coset the invariant is `F(s) = −s³·(q²+1)⁶(q²−q+1)³(q²+q+1)³/q⁶`,
whose only root is `s = 0`. So **no element of `Φ* + span(v)` is a nonzero
scalar multiple of a braid image.** Quantified over the coset deliberately: on
the quotient `x` is defined only modulo the radical, so a claim about the point
alone would be a gauge artifact.

Scope (b) per the STRICT refuted rule, invariant named. `t(q)` and `G(q)` are
derived from the H₃(q) structure constants (normalisation + cyclicity + Markov),
not copied from `pyhecke` — the shipped `TR_M` is a verified consequence there.

**Follow-on: `qou-v7qj`.** The repair for LP degeneracy and the condition
forbidding a braid answer are the same condition. Whether the quotient is the
right repair is the live question; this bean does not answer it.
