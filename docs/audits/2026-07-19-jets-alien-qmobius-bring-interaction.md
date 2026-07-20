# Jets ↔ alien-calculus Δ_ω data ↔ q-Möbius kernel on Bring's surface — interaction map + leverage routes

**Date:** 2026-07-19
**Branch:** `claude/jets-alien-calc-q-mobius-yrp563`
**Beans:** milestone `qou-nxl8` (tasks `qou-hhmt` audit, `qou-4cb9` probe, `qou-mflo` coordinate)
**Status:** AUDIT (cross-link synthesis + leverage assessment). No derivation, no
number claimed, no wiring. All "open"/"refuted" language below inherits its scope
from the cited source documents; nothing new is declared open or refuted here.

## 0. Question answered

The corpus carries three chains that all touch Bring's surface: the SW **jet
tower**, the **alien-calculus datum** (`Δ_ω`, Stokes constant `A_ω`), and the
**q-Möbius (categorical Möbius) kernel** `K_q(s,t)`. This audit records how they
interact — they converge on the single object `tr_M` (the Markov trace) through
one bridge identity and one no-go theorem — and assesses two leverage questions
raised by the owner: can the interaction be used to (a) **speed up computation**,
(b) **close derivation gaps**, in particular using the recently proved Lean on
Li₂ / Cl₂ / the q-dilog (Faddeev Φ_b) stack.

## 1. The three chains and their pairwise interactions

### 1.1 Bridge equation: the alien derivative IS jet data times a Stokes constant

Écalle's bridge equation
([`ecalle-borel-resurgence-vocabulary.md`](../../content/quantum-observable-universe/appendix-surreals-archimedean/ecalle-borel-resurgence-vocabulary.md))

$$\Delta_\omega \tilde f = A_\omega\,\partial\tilde f/\partial z$$

has the **first jet** on its right-hand side: the alien derivation is
proportional to the natural jet derivation, and `A_ω` is the ratio. The Δ_ω
data on Bring's surface is therefore *measured against* the jet tower, not
independent of it. Concretely realised in
[`computations/lever1_bridge_alien_datum_probe.py`](../../computations/lever1_bridge_alien_datum_probe.py):
the even-face `A_ω = 4√2·e^{−3/8} ≈ 3.8884` is extracted against the jet EGF
`e^{x+x²/2}` (co-equational, coefficient-plane — see the framing correction in
[`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md) §0).
The odd-face `A_ω` is the **G3 keystone** and remains open (candidate integer 3
from the GGM Stokes matrix; explicitly not identified).

### 1.2 Jet exactness makes the alien sector load-bearing

[`prop:sw-classical-jet-exactness`](../../content/quantum-observable-universe/brings-surface/sw-classical-jet-exactness-proof.md)
(Lean `QOU.Brings.classical_jet_period_zero`, `classical_jet_period_ne_lw`):
every classical SW jet `λ_SW^(n) = d(X^(n−1))` on Σ is **exact** ⇒ zero residues
and zero periods at every vertical degree `n ≥ 1` ⇒ the classical jet tower
cannot realise the nonzero binding period `a_D`. The period content therefore
lives entirely in the sector the jets cannot see — the Stokes/monodromy data
detected by `Δ_ω` (leading singularity at `ω ≈ Vol(4₁)/π ≈ 0.646`). Jets and
alien data are exactly complementary on Bring's surface: formal
coefficient-plane tower vs singularity/period content. The binding jet
filtration itself is
[`conj:binding-manybody-eq-jet-filtration`](../../content/quantum-observable-universe/mass-theory/jet-filtration-binding-extensive.md).

### 1.3 The q-Möbius kernel touches both — at the diagonal and in the subtraction

Two wired contact points for `K_q(s,t)`
([`prop:mobius-energy`](../../content/quantum-observable-universe/climax-volume-mass/mobius-energy.md)):

1. **Diagonal.**
   [`lem:jones-mobius-diagonal`](../../content/quantum-observable-universe/climax-volume-mass/jones-mobius-diagonal.md)
   (Lean `QOU.Braiding.JonesMobiusDiagonal.markov_eq_mobius_contact`, sorry-free):
   the Hadamard contact term of the categorical Möbius energy is
   `C(ϱ) = tr_M(ρ(β_K)) = J_K(q)`. The same `tr_M` is what the jet filtration
   grades (§1.2) and what carries the `ω = Vol(4₁)/π` Borel singularity that
   `Δ_ω` probes (§1.1). All three chains meet at `tr_M`.
2. **Subtraction.**
   [`mobius-surreal-renormalization.md`](../../content/quantum-observable-universe/appendix-surreals/mobius-surreal-renormalization.md)
   writes the Möbius finite part as `std(I₁ − I₂)` of two `ord_ω = +1` surreals,
   and [`rem:st-is-median-resummation`](../../content/quantum-observable-universe/appendix-surreals-archimedean/st-is-median-resummation.md)
   identifies `std` with Écalle's median resummation. The q-Möbius diagonal
   excision and the lateral/median Borel selection are **one operation in two
   languages** — the citation-graph direction (resurgence blocks cite the
   `st = 𝓛^med` block, not vice versa) is already fixed there.

### 1.4 Glyph cautions (do not transfer attributes)

- The surreal `ω` in `ord_ω` (infinite ordinal) and the alien-calculus `ω`
  (Borel-plane singularity location) are **unrelated objects** sharing a glyph.
- "q-Möbius" here = the categorical Möbius two-point kernel `K_q`. The PSL₂
  Möbius action on the Bring base (`z ↦ 1/z`,
  [`rem:braid-group-action`](../../content/quantum-observable-universe/brings-surface/braid-group-action.md);
  Klein icosahedral bridge) is a **different object**; its single-`ℙ(V)` Möbius
  realization remains the open primary conjecture of
  `klein-bring-icosahedral-bridge.lean`.

## 2. Leverage route A — computation speed

Three concrete, corpus-grounded speedups follow from the interaction map. None
is wired here; each names the consumer that would benefit.

1. **Predict deep tower rungs from the alien datum instead of computing them.**
   The bridge equation determines large-order coefficients from `(A, β, S)`:
   `κ_n ~ (S/π)·Γ(n+β)/A^{n+β}`. The κ-tower probe
   ([`computations/probes/qbeta_kappa_large_order_bridge_probe.py`](../../computations/probes/qbeta_kappa_large_order_bridge_probe.py))
   already runs this forward at n ≤ 6; the **k = 31 dladder wall**
   (`qbeta-dladder-extension-singularity.witness.json`, structurally
   unresolvable by fixed-order Borel–Leroy) is precisely where exact-rung
   computation stops scaling. The alien-datum form is the *only* known
   polynomial-cost handle past the wall. Scope-(a): predictions are
   CONSISTENT-grade cross-checks, never replacements for exact rungs in
   canonical witnesses.
2. **Skip classical jet periods — they are proved zero.** Any sweep that sums
   classical (q = 1) jet-tower periods/residues on Σ can prune those terms
   structurally by `classical_jet_period_zero` instead of evaluating them.
   This is the formalize-first pattern paying compute rent: a Lean lemma as a
   dead-branch eliminator.
3. **Evaluate the Möbius diagonal via the Markov trace, not quadrature.**
   `markov_eq_mobius_contact` converts the contact term of the two-point
   kernel — an expensive singular double quadrature — into `tr_M` (Hecke
   algebra, exact, cheap via `pyhecke`/`hecke-engine`). Any future
   `E_cat`-numerics should compute `T_reg − J_K(q)`, never re-derive the
   contact term by excision limits.

## 3. Leverage route B — derivation gaps, via the recent Li₂ / q-dilog Lean

Recently proved, directly on this stack:

| Lean | Status | What it pins |
|---|---|---|
| `QOU/Knot/FigureEightVolumeSaddle.lean` (`kashaevProd_eq_sin`, `saddle_critical_point`, E3c Cl₂ global min + saddle-max corollaries; E3 COMPLETE, commit `c5bcfac9`) | sorry-free | the Kashaev sum's sin-form and the saddle at `θ = π/3` ⇒ `Vol(4₁) = 2 Cl₂(π/3)` — the *location and value* of the dominant saddle |
| `QOU/QBeta/CyclicDilogPentagon.lean` (`faddeevPhi_unique_of_pentagon`) + `MonodromyDatumRigidity.lean` (`monodromy_datum_rigidity`) | sorry-free (open input: `PentagonRigidity.uniqueUpToScalar`, no instance) | any scale-invariant readout of a Faddeev Φ_b solution is unique ⇒ `A_ω` carries **zero fitting freedom** |
| `QOU/QBeta/BorelWatsonUniqueness.lean` (`watson_uniqueness_rhp`) | sorry-free (per the 2026-07-18 currency correction) | the resummation-side uniqueness half of `st = 𝓛^med` |

How they compose against the gaps:

1. **G3 (odd-face `A_ω`).** The rigidity pair converts G3 from "search a
   function space for `z(q₀) → S`" into "verify one integer" (the GGM Stokes
   `3`) — *once* the Liouville step (`PentagonRigidity.uniqueUpToScalar`,
   doubly-periodic ⇒ constant, not in Mathlib) is proved. That step remains
   **the** formalize-first target
   ([`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md) §3);
   nothing in this audit shortcuts it, and axiomatising it would be the
   §Axiomatization-is-not-a-proof trap.
2. **The saddle Lean upgrades the Borel-action identification from numerology
   to structure.** With the saddle location/value proved, the statement "the
   contact-tower Borel action equals `Vol(4₁)/π`" has a derived *predicted*
   value; the sibling probe (`qou-4cb9`, §4) tests it against the
   C1-stabilised band. If it lands, the identification is CONSISTENT with a
   proved-saddle anchor rather than a float coincidence — a strictly better
   epistemic tier, though still not "derived" until the Riemann-sum and
   max-term bricks (beans `bca6`/`el8w-saddle`) close.
3. **The `st = 𝓛^med` identification (Watson leg now sorry-free) licenses the
   surreal side as a proof surface for renormalization identities.** The
   Möbius finite-part (`std` of an `ord_ω`-matched difference) is algebra over
   `No` — a leading-coefficient match — which is Lean-tractable in a way the
   analytic Hadamard limit is not. Candidate follow-up formalization: the
   `[ω^{+1}]I₁ = [ω^{+1}]I₂` cancellation of
   `mobius-surreal-renormalization.md` as a generic-`R` coefficient lemma
   (§7c: no archimedean content in the cancellation itself).

## 4. Probe launched alongside this audit (bean `qou-4cb9`)

`computations/probes/qmobius_contact_tower_borel_action_probe.py` — tests, at
scope-(a):

- **T1 (exact anchor):** the q-Möbius diagonal at the fundamental level —
  `⟨4₁⟩_2 = 5 = |J_{4₁}(−1)|` (determinant), tying `markov_eq_mobius_contact`
  numerically to the Kashaev tower at its base rung.
- **T2 (volume limit):** `(2π/N)·log⟨4₁⟩_N → Vol(4₁) = 2 Cl₂(π/3)` on the
  exact Kashaev sum (the E3-anchored saddle value), Richardson-extrapolated.
- **T3 (Borel action):** the contact-tower Ohtsuki ladder's action `A`
  (reusing the main-witness κ rungs with provenance) against the
  saddle-predicted `Vol(4₁)/π`, inside the C1 band `[0.6338, 0.6833]`.

Kill criterion pre-stated in the script; verdict vocabulary CONSISTENT /
NEGATIVE scope-(a), never "derived". Results land in the sibling witness JSON
and are summarised in the PR, not here (audit stays static).

## 5. Discipline

- **Corpus-grep:** all §1 links are to existing blocks/audits; the §2/§3 routes
  cite their existing probe/Lean carriers. No new open item is declared; the
  G3 open status is inherited from the 2026-07-18 audit, unchanged.
- **Anti-laundering:** §3.1 explicitly keeps the Liouville step open; the
  integer-3 identification stays falsifiable and unclaimed. §2.1 predictions
  are cross-checks, not canonical values.
- **Möbius-glyph hygiene:** §1.4 records the two collisions once; downstream
  docs should cite this section rather than re-deriving the disambiguation.
