# Geom(K) uniqueness + `conj:hyperbolic-volume-transcendence` fate

**Date:** 2026-06-07
**Goal arm:** geom-universality formalization (`Geom(K)` ∃! uniqueness) + the
fate of `conj:hyperbolic-volume-transcendence` (keep / purge).
**PRs:** #1931 (Lean ∃!), #1935 (decision + scope note).

## Scope map (§2)

| PR | Branch | Owns | Primary file(s) | Overlap | Dependency | Cherry-pick |
|----|--------|------|-----------------|---------|------------|-------------|
| #1931 | `claude/geom-uniqueness-2026-06-06` | Lean `∃!` existence+uniqueness of `Geom(K)`; Prop-with-data fix on `GeomFullFunctorial` | `particle-interactions/geom-universality.lean` (+3) | additive | independent | — |
| #1935 | `claude/fervent-euler-oGp4I` | conjecture-fate decision + scope note | `predicted-spectra/hyperbolic-volume-transcendence.md` | additive (different file) | independent | the single commit → #1931 if a one-PR rollup is wanted |

Classification: **(additive, independent, optional cherry-pick)** — different
files, same theme. No conflict.

## Verdict (the question at #1931's tail)

- `conj:hyperbolic-volume-transcendence` is **external**, not framework-internal:
  a special case of the Kontsevich–Zagier and Grothendieck period conjectures
  (Tier-C in [`docs/audits/2026-05-09-conjecture-closure-tractability.md`](../audits/2026-05-09-conjecture-closure-tractability.md)).
  Even irrationality of a *single* hyperbolic 3-manifold volume is open.
- **QOU cannot close it** — but #1931's
  `conj:three-knot-jet-order-independence` gives the sharper *QOU-attackable*
  reduction (a finite per-order Gröbner–Shirshov independence computation +
  an open QOU-native surreal bridge lemma), alongside the
  `rem:yekutieli-transcendence-shadow` tower route. Both relocate the
  difficulty; neither closes it.
- **Decision: KEEP** as a reference (external + QOU path-forward + weak version
  suffices). Not a prerequisite — per `rem:formal-chain-transcendence` the
  predictions live over ℤ[q,q⁻¹] and need only the *proved* numerical
  distinctness of the volumes. Documented as a "Scope" note on the conjecture.

## Coordination (§3, §5)

- Intent posted on #1931: [pull/1931#issuecomment-4640945213](https://github.com/litlfred/qou/pull/1931#issuecomment-4640945213).
  Dropped my conflicting `.lean` docstring edit — #1931 owns `geom-universality.lean`
  and its real `∃!` supersedes my tweak against the old `True` stub.
- #1935 review triage (consolidated comment on #1935):
  - Copilot — **accept**: `Scope:` colon heading + inline gloss of the
    conditional-class convention.
  - Gemini — **reject-with-reason**: `#label` → `./file.md` would break the
    repo's `[text](#label)` → `\hyperref[label]` convention (all blocks render
    into one document); kept `#label` (consistent with every sibling block).
  - CI `Content pipeline` failure — GitHub Actions **billing** pattern (3 s,
    log 404, local `validate` exit 0). `[skip-ci: billing]`.

## main watch (§8a / §8c)

- `origin/main` is **10 commits ahead** of branch base; **none touch
  `predicted-spectra/` or `particle-interactions/`** → no conflict, no rebase
  needed for #1935 (it merges cleanly — different files). main-side changes are
  skill/doc *modifications* (compute-author, lean-proof-review, proof-gap-audit,
  proof-triage, witnessed-values, production-vs-exploratory-discipline) — infra,
  non-overlapping with this doc PR.

## Resolution

- **Author chose option 2 (2026-06-07): fold into #1931.** The scope note on
  `hyperbolic-volume-transcendence.md` + this ledger now ride on
  `claude/geom-uniqueness-2026-06-06` (single PR #1931, alongside the Lean
  `∃!` and the jet-order reduction `conj:three-knot-jet-order-independence`).
  #1935 closed as superseded; its branch retains the original commits.

## Lean gap-closing progress (2026-06-07, appended)

The reduction `conj:three-knot-jet-order-independence` is now **formalized**
in [`QOU.Archimedean.JetOrderIndependence`](../../content/quantum-observable-universe/lean/QOU/Archimedean/JetOrderIndependence.lean)
(verified sorry-free, `lake env lean` EXIT 0). It is the §3b-cond conditional
theorem `hyperbolicVolumeIndependence_of_reduction` deriving the deep
`HyperbolicVolumeIndependence` from two QOU-native inputs. What moved from
"open" to "proved":

| Sub-claim | Before | After |
|---|---|---|
| Surreal bridge (composition) | monolithic `shadow_vanishes` axiom | **proved** `transport_shadow_vanishes` (I2 ∘ I3) |
| (I1) uniformity in jet order | open | **proved** `transport_uniform_bound` (C = 0) |
| (I2) physical-holonomy shadow → 0 | — | named conjectural input (was inside the monolith) |
| (I3) monodromy shadow → 0 | — | named conjectural input |
| GB independence at base order N=3 | open | **proved + witnessed** `jetOrder3_certificate` (∏ pivots = 1/16 ≠ 0, real Markov-trace data) |

Net: the conjectural surface shrank from one opaque axiom to **two physical
vanishing inputs (I2, I3)** + the **per-order GB certificate for N > 3**
(same finite determinant test). The base order is no longer "pending the
witness": `jet_order_pivots.py` computes the h-jet expansion of the
framework's *own* canonical Markov traces `tr_M(4₁/5₂/𝓑₃)` about q=1,
finds jet-Jacobian rows `(1/4,−1,55/16)`, `(1/2,0,−1/16)`, `(1,0,0)` with
elimination determinant `1/16 ≠ 0`, and wires the LU pivots `(1/4,2,1/8)`
into `jetPivots` — so the base-order certificate is now **witnessed real
data**, not representative (`jet-order-pivots.witness.json`). The surreal bound is framed geometrically as parallel
transport of the categorical connection on the projective state fibre
`ℂP¹` as `q` deforms toward the root-of-unity limit (I1 uniformity /
I2 archimedean-projection / I3 monodromy-separation). Cross-ref:
[`2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md`](../audits/2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md)
(the GB-filtration / jet-order bookkeeping this certificate instantiates).

**Derivation-gap status:** `prop:geom-universality` (the `Geom(K)` volume
form feeding `VolDensity(K, q₀)` at canonical-chain step 9a) now has a
sorry-free `∃!` well-definedness backing; its transcendence dependency is
reduced (not closed) per the table above. This does **not** touch the
separate, still-open step-9a per-knot `VolDensity(K)` *wire-up* gap (cheat
§9 row 1) — that is a production-migration bug, orthogonal to the
well-definedness leg settled here.
