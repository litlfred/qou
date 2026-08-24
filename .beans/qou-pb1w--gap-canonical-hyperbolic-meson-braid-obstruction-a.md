---
# qou-pb1w
title: 'GAP: canonical hyperbolic meson braid (Obstruction A) — the corpus braid is Vol=0'
status: todo
type: task
priority: normal
created_at: 2026-08-24T19:24:22Z
updated_at: 2026-08-24T19:25:19Z
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
