# Lean axiom landscape — tractability triage (2026-06-03)

> Companion to the lean-discharge queue (`.beans/lean-discharge-queue.json`).
> Snapshots the current state of every `axiom` declaration in
> `content/quantum-observable-universe/lean/QOU/` and classifies them
> by tractability so future discharge sessions can target the
> low-hanging fruit instead of re-discovering the landscape.

## Headline

> **🛑 STALE AS A DESCRIPTION OF THE TREE (re-measured 2026-08-26, bean `qou-8s7o`).**
> The table below counts **77** axioms, 58 of them External. The live tree carries
> **23 axioms in total**, across every bucket
> (`scripts/lean-assumption-surface.py`; 2207 files, 0 `sorry` / 0 `sorryAx` /
> 0 `true_vacuity`, 1 `native_decide`):
>
> | area | axioms |  | area | axioms |
> |---|---|---|---|---|
> | HeckeAlgebra | 8 |  | Mathlib | 2 |
> | MathlibExt | 5 |  | AppendixSurreals / Archimedean / Hecke / IwahoriHecke | 1 each |
> | BraidKnot | 4 |  | | |
>
> So roughly two-thirds of what this document triages has since been discharged or
> removed. **Do not quote these bucket sizes as current.** The classifications
> below remain useful as a record of *how each surviving axiom was judged at the
> time*, which is exactly what the 2026-08-26 re-check tested — see
> [`2026-08-26-live-axiom-surface-recheck.md`](2026-08-26-live-axiom-surface-recheck.md),
> which also finds that a chunk of the surviving surface is **interface axioms over
> `opaque` symbols** (unprovable by construction, not blocked on Mathlib) rather
> than deep external mathematics.


| Total axioms (declarations) | 77 |
|---|---|
| **Tractable** (numerical / decidable / small concrete inequality) | **8** |
| **Algebraic** (equational, may need `ring` / `simp` / hecke relations) | 6 |
| **Structural** (existentials, `Nonempty`, `IsXxx` predicates) | 5 |
| **External / cited / deep** (Adams, Yekutieli, SDP strong duality, …) | 58 |

(Earlier `grep -c "^axiom "` returned 90 — that includes text matches in
comments / docstrings. The 77 figure is from a Python regex parser that
matches `^axiom <Name> (...) : <type>` declarations.)

## Blocker uncovered this session

**Mathlib cache host returns 403** in this container. `lake exe cache get`
fails on every download (7335/7335 attempted, 0 succeeded). This is the
same network-policy block that `release.lean-lang.org` hits for elan —
the workaround in
[`scripts/setup-lean-toolchain.sh`](../../scripts/setup-lean-toolchain.sh)
(PR #1755) bypasses it for the **toolchain** by fetching directly from
GitHub releases, but `lake exe cache get` pulls from the **Mathlib oleans
host** which is a different endpoint and remains blocked.

**Consequence:** any Lean proof attempt in this container would need to
build Mathlib from source (estimated 1-4 h on first run). Discharging
even one axiom is impractical without precompiled oleans. **Either**:
1. Fix the cache-host network policy (same shape as the toolchain
   workaround — bypass via GitHub releases or a mirror).
2. Pre-bake Mathlib oleans into the container image (Docker layer).
3. Defer all Lean-discharge work to a local environment.

See follow-up todo `infra-lean-cache-host-bypass` (added to
`.beans/lean-discharge-queue.json` in this PR).

## Tractable axioms (8) — for a working Lean environment

These are decidable inequalities, finite-sum identities, or concrete
numerical bounds. Each is plausibly 1-3 hours of work in a working
Lean environment with cached Mathlib.

| # | File | Axiom | Statement |
|---|---|---|---|
| 1 | [`Archimedean/BorromeanVolumeCatalan.lean:98`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BorromeanVolumeCatalan.lean) | `catalan_G_numerical_bounds` | `catalan_G ∈ (0.915, 0.916)` — uses `alternating_series_error_bound` (Mathlib has it) + ~50-term `norm_num` |
| 2 | [`Archimedean/BorromeanVolumeCatalan.lean:209`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BorromeanVolumeCatalan.lean) | `vol_B3_eq_8_catalan` | `vol_B3 = 8 * catalan_G` — citation-only (Adams 1985); not actually tractable, mis-classified by name keyword. **Bump to External.** |
| 3 | [`BraidKnot/CommutativeCrossingEnergy.lean:79`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/CommutativeCrossingEnergy.lean) | `ord_u_zero_trM_eq` | `ord_u_zero_trM Z N = 18·Z + 21·N + 1` — small concrete identity; should be `decide` or computable definition |
| 4 | [`BraidKnot/LpDualityHypothesisClass.lean:99`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/LpDualityHypothesisClass.lean) | `schrijver_strong_duality` | `∀ lp, lp.duality_gap = 0` — LP strong duality. **Citation-only** (Schrijver theorem); not tractable in-house. **Bump to External.** |
| 5 | [`BraidKnot/PSDFeasibilityProxy.lean:78`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/PSDFeasibilityProxy.lean) | `evenPower_necessary_for_blockPosSemidef` | Universal `PSD → eraseDup` parity. Decidable-shape but quantifies over braid words. **Moderate; may need ad-hoc induction.** |
| 6 | [`BraidKnot/QuantumDilogarithm.lean:56`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QuantumDilogarithm.lean) | `phi_q_at_zero` | `∀ q : ℝ, phi_q q 0 = 1` — boundary case of quantum dilog; may follow by `unfold + simp` if `phi_q` has a clean definition |
| 7 | [`BraidKnot/QuantumDilogarithm.lean:77`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/QuantumDilogarithm.lean) | `li2_q_at_zero` | `∀ q : ℝ, li2_q q 0 = 0` — same shape as #6 |
| 8 | [`HeckeAlgebra/MarkovTrace.lean:80`](../../content/quantum-observable-universe/lean/QOU/HeckeAlgebra/MarkovTrace.lean) | `JonesMarkovCoefficient_sum_eq_one` | `∀ n q, Σ_λ JonesMarkov(λ, q) = 1` — partition sum identity; needs the actual definition of `JonesMarkovCoefficient` to gauge difficulty |

**Net tractable after reclassification: 6** (drop #2 and #4 — both are
citation-axioms despite name patterns).

### Recommended order

For the next Lean-env session (assuming cache-403 fixed):

1. **`phi_q_at_zero` + `li2_q_at_zero`** — boundary cases; if the
   definitions unfold cleanly, these are 30-60 min wins each.
2. **`ord_u_zero_trM_eq`** — concrete arithmetic identity; should be
   `decide` if `ord_u_zero_trM` is computable.
3. **`catalan_G_numerical_bounds`** — the queue's flagship item;
   ~1-3 h, well-scoped via Mathlib's `alternating_series_error_bound`.
4. **`JonesMarkovCoefficient_sum_eq_one`** + **`evenPower_necessary`** —
   higher-risk; tackle after the easier wins.

## Algebraic axioms (6) — moderate

Equational identities (matrix commutativity, Hecke quadratic / braid
relations, central-idempotent orthogonality). May yield to `ring`,
`simp`, or expansion via the explicit Hoefsmit / Hecke relations.
Each likely 2-6 hours.

| File | Axiom | Comment |
|---|---|---|
| [`Archimedean/HeckeRep.lean:299`](../../content/quantum-observable-universe/lean/QOU/Archimedean/HeckeRep.lean) | `transferMatrix_comm_axiom` | matrix commutativity |
| [`BraidKnot/IwahoriHeckeAPI.lean:225`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/IwahoriHeckeAPI.lean) | `centralIdempotent_orthogonal_axiom` | idempotent orthogonality |
| [`HeckeAlgebra/Formal.lean:179`](../../content/quantum-observable-universe/lean/QOU/HeckeAlgebra/Formal.lean) | `heckeFormalGenerator_T_relation` | Hecke quadratic relation in formal algebra |
| [`HeckeAlgebra/Hoefsmit.lean:125`](../../content/quantum-observable-universe/lean/QOU/HeckeAlgebra/Hoefsmit.lean) | `HoefsmitMatrix_hecke_relation` | Hoefsmit-matrix Hecke relation |
| [`HeckeAlgebra/Hoefsmit.lean:139`](../../content/quantum-observable-universe/lean/QOU/HeckeAlgebra/Hoefsmit.lean) | `HoefsmitMatrix_braid_relation` | Hoefsmit-matrix braid relation |
| (+1 more) | | |

## Structural axioms (5) — research-grade

Existence claims and `IsXxx` predicates. Each requires substantive
construction. Multi-week per axiom.

## External / cited / deep (58)

The bulk — Adams 1985 hyperbolic volumes, Yekutieli non-abelian Stokes,
~~Lobachevsky-Catalan transcendental identity~~ **[discharged 2026-08-26 — see
below]**, SDP strong duality, Schrijver
LP theorem, Mathlib-pending PSD lemmas, Kashiwara crystal axioms, …
These cite established external results and / or wait for upstream
Mathlib PRs. **Discharging these is not a feasible session-scale goal.**

> **🛑 One entry in this bucket was misclassified, and the way it was
> misclassified is the point (2026-08-26).**
>
> `lobachevsky_pi_div_four_eq_half_catalan` — `Λ(π/4) = G/2` — sat here as an
> "External / cited / deep" transcendental identity for nearly three months. It
> is now a **theorem**, proved sorry-free in about twenty lines, with no new
> analysis and nothing fetched from upstream
> ([`BorromeanVolumeCatalan.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BorromeanVolumeCatalan.lean)).
>
> Everything it needed already existed. `QOU.Knot.clausen_eq_series` — in this
> repository, sorry-free — is the full Zagier series↔integral bridge
> `∫₀^θ -log(2 sin(t/2)) dt = Cl₂(θ)` on `(0, 2π)`, and Mathlib supplies both
> ingredients that bridge is built from: `integral_log_sin_zero_pi_div_two`
> (`Analysis.SpecialFunctions.Integrals.LogTrigonometric`) and
> `Analysis.Complex.AbelLimit`. The identity is three steps over those: drop the
> absolute value on `[0, π/4]`, rescale `t = 2s` onto the half-angle integrand,
> then apply the two bridges.
>
> **The lesson is about the triage method, not this axiom.** This bucket was
> populated by *reading the axioms' own docstrings*, and this one's said a proof
> "would require Mathlib's full polylogarithm machinery ... none of which is
> currently upstream". That sentence was believed rather than checked, and it
> stayed believed through at least two later revisits — including one on
> 2026-08-25 that narrowed the gap to "the Clausen integral representation" and
> re-affirmed the External classification, while the file proving exactly that
> representation had been in the tree for weeks. An axiom's docstring is a claim
> about the corpus made at the time it was written, and AGENTS.md §"Before
> declaring 'open'" says to grep the corpus instead. **The rest of this bucket
> has not been re-checked against that standard and should not be assumed
> correct.**
>
> Discharging it also made a downstream consumer unconditional:
> `WhiteheadVolume.vol_L5a1_eq_eight_lobachevsky` (`Vol(L5a1) = 8·Λ(π/4)`) was
> inheriting the axiom and now depends on `[propext, Classical.choice,
> Quot.sound]` alone.

## Cross-refs

- [`.beans/lean-discharge-queue.json`](../../.beans/lean-discharge-queue.json) — work queue (10 items, 4 still open after this PR's findings)
- [`docs/audits/2026-06-03-canonical-axis-current-fails-triage.md`](2026-06-03-canonical-axis-current-fails-triage.md) — parallel canonical-axis triage
- [`scripts/setup-lean-toolchain.sh`](../../scripts/setup-lean-toolchain.sh) — toolchain-host workaround from PR #1755 (the cache-host bypass needs the same shape)
- [PR #1755](https://github.com/litlfred/qou/pull/1755) — elan host bypass (toolchain only; cache host still blocked)
