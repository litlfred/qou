# Pre-registration: do the photon's colour weights separate the neutron from the proton?

Bean `qou-99qc`. Owner 2026-11-21 chose both: (1) build n and p from the four-term photon
`γ(φ₀,φ₁,φ₀₁) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` with different colour weights, as photon-pair
products generalising `V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)`, with `(φ₀,φ₁)` from the solution set of
PR #8634 (`FactorsBorromean`); (2) redo the γγ + reading-3 selection of PR #8636 with `φ`
symbolic. Written 2026-11-21 BEFORE any number in this directory was computed.

## Fixed inputs (no choice is tuned later)

* Photon: `def:photon` (owner ruling). The `σ₀σ₁` fourth term is not used anywhere.
* The 8-point set: all `(φ, ψ) ∈ ℂ⁶` with `γ(φ)γ(ψ) = β_Bor` (#8634), re-solved at the
  proton pin `q₀` (`qou_substrate.constants.Q_50_DIGIT_STR`), 70 dps, every candidate
  re-substituted into all six equations. The #8634 sample `h = 1/2, 2/9` counts are
  reproduced first as a control.
* Reading 3: `χ_λ(X) ≥ 0` on every block with `y_λ > 0`, convention D (`z = q³/(q²+1)`,
  so `y_(1³) = 0`), whole word `X`.
* Traces, every one reported for every element:
  - one-term quantum trace `T₁(X) = Tr(K^{⊗3} ρ(X))/[2]³` (= Ocneanu trace at `z_D`);
  - D1 = A split `ε_p(X) = q·tr_{W_p}(X)/[2]³`, `ε_n(X) = q⁻¹·tr_{W_n}(X)/[2]³`;
  - label C `ε_C(X) = tr(T₋T₊X)/tr(T₋T₊)` (#8632);
  - SCORED two-term covariant all-pairs connected term (`two_term_covariant_all_pairs_qtrace`);
  - adjacent `Q₁₂+Q₂₃` connected insertion — LABELLED, non-covariant comparison, not scored.

## Assignment rules (named; none chosen against data)

* **R-pt** (the owner's literal instruction): the proton's pair is point `i` of the
  8-point set, the neutron's pair is point `j`; all 64 `(i, j)`.
* **R-maj**: a flavour carries one photon; `X_p = γ(w_u)γ(w_d)`, `X_n = γ(w_d)γ(w_u)`
  (the doubly-occurring flavour first). All `(w_u, w_d)` from the 16 photon factors of the
  8 points.
* **R-free**: all 256 products `γ(w)γ(w')` of those 16 photons, as a table; any other
  n/p rule is a choice of two rows of it.

## Predictions (priors, stated before computing)

* **P1 (scope b, definitional).** Under R-pt `X_n = X_p = β_Bor` for every `(i, j)`, so
  every functional above agrees and the n − p difference is 0 to all orders in `q − 1`.
* **P2 (scope b).** Every functional above except the adjacent insertion is a linear form
  in `(χ_(3)(X), χ_(2,1)(X))` (the operators `K^{⊗3}`, `T₋T₊`, `Q_pair` commute with the
  `H₃` action). Characters are cyclic, so under R-maj all of them agree for n and p for
  every `(w_u, w_d)`, whether or not `X_n = X_p`.
* **P3 (scope b).** `Q_pair = Q₁₂+Q₂₃+Q₁₃` is a scalar on each weight space (0 on `W_p`,
  `−1/3` on `W_n`), so the scored connected two-term term is 0 for EVERY element, hence for
  every `φ`, not only on `V³`.
* **P4.** Reading 3 on the whole word is flavour-blind and, for one photon, depends on
  `(φ₀, φ₁)` only through `φ₀ + φ₁`; on a pair it is two inequalities in six real
  unknowns with non-empty interior (it contains `φ = ψ = 0`). So it cannot force the
  colour weights to a finite set, and cannot force them differently for u and d.
  On the 8-point set it is all-or-nothing (every point has the same product).
* **P5 (prior, ~50 %).** Some of the 6 non-Borromean points are non-real at `q₀`; a
  non-real colour weight makes `χ ≥ 0` meaningless, so those points are not admissible
  for reading 3.
* **P6 (prior, low confidence).** The adjacent (non-covariant) insertion differs between
  `γ(a)γ(b)` and `γ(b)γ(a)`; if it does, the difference is reported with its `q → 1` order
  and is not promoted.

## Corpus question

Does the corpus assign colour weights to flavour? Searched before computing: `def:photon`
(`predicted-spectra/photon.md`), `quark-antiquark-production.md` ("independent color
weights"), `pn-averaging-uniqueness.md` ("choosing that weight is open"), and the
`bring_color_weighted` p/n convention (an interface factor `z − h(1/2 − δ/4)`, not the
photon weights). Prior: no assignment exists, so any n/p split through colour weights is a
new assignment needing an owner ruling.
