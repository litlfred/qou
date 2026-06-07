# 3-axis (knot, partition, atom) derived-characters catalogue — work-tranche (2026-06-07)

> **Goal**: replace empirically-extracted `χ^λ(β_K)` and per-block
> Markov weights with **R-matrix-derived** values across the QOU
> knot-operator census (PR #1677), 3-axis indexed by
> `(knot K, partition λ ⊢ n_K, atom A)`. Wire derived values into
> production compute so the headline binding-energy / mass-formula
> calculations stop consuming extracted numbers where structural
> derivations are now available.
>
> Owner direction (2026-06-07): "I want all derived wired up into
> compute. 3 axis framing." This document is the work-plan; the
> linked branch is the implementation.

## Why now

Three things landed since the `[3]_q/25` thread (PR #1781/#1791/#1795/#1799):

1. **T17 (PR #1933, merged)** — first purely-categorical derivation
   of a Wedderburn character: `χ⁽²,¹⁾(β_Bor) = 2 − 3h⁴ − h⁶` from the
   R-matrix on `V⊗³`. Template for derivation.
2. **T18 (commit `b6c23f2053` on main)** — closes within-`H_3`
   categorical chain by deriving Markov normalisation `y₍₂,₁₎(0) = 1/4`.
3. **PR #1799 (merged, this thread)** — cross-anchor rigidity probe
   falsified real-q `c_3 = f(q)` Habiro forms (4.7-million-fold
   mismatch). Confirms the structural route is the *only* route.

The path forward is therefore: extend T17 + T18 systematically across
the [PR #1677 census](2026-06-01-knot-operator-census-group-actions.md)
and wire the results into production. No new fits.

## Scope

The catalogue is **three-axis**, not two:

| axis | range | source |
|------|-------|--------|
| **K** (knot operator) | 10 census entries — Unknot T(1,0), Hopf T(2,2), Trefoil T(2,3), Cinquefoil T(2,5), Borromean, Figure-eight 4₁, T(3,4), … (genus-bounded to 7 torus + Borromean/4₁ + future linked) | PR #1677 census + `brings-surface/torus-knot-generators` (χ = −6 ⇒ 7 admissible T(m,n)) |
| **λ** (partition) | λ ⊢ n_K for each `K` of strand count `n_K` | Wedderburn decomp of `H_{n_K}(q)` |
| **A** (atom / physical target) | the QOU isotope / particle the per-atom SDP routes to `(K, λ)` | `prop:operator-selection-lp` active set |

Per-cell data the catalogue stores:

| field | derivation source | purpose |
|-------|-------------------|---------|
| `chi_lambda_q` (q-polynomial) | R-matrix on `V^{⊗n_K}` (T17 template) | structural character |
| `mu_eigenvalues` | Hoefsmit seminormal form of `ρ_λ(β_K)` | feeds `k_λ` selector |
| `k_lambda` | `1` iff λ is the max-`|μ|` partition for `β_H`, else `2` (`prop:per-partition-k-lambda-rule`) | truncation order |
| `y_lambda_at_zero` | Markov normalisation derivation (T18 template) | leading Markov weight |
| `y_star_shadow_price` | per-atom SDP dual variable | confirms `(K, λ, A)` is in the active set |
| `tier` | `derived` / `cal-anchored` / `extracted` | provenance for the wire-up |

## Deliverables (multi-session)

### Phase 1 — schema + first derived entries (this PR)

- [x] Audit doc (this file) + work-plan
- [ ] Witness JSON schema for the catalogue (per-cell record + manifest)
- [ ] Python `derived_chi_catalogue.py` module skeleton with the typed
      record + lookup API
- [ ] R-matrix derivation of `χ⁽²,¹⁾(β_Bor)` reproduces T17's
      `2 − 3h⁴ − h⁶` (sanity check against the merged result)
- [ ] R-matrix derivation of `χ⁽³⁾(β_Bor)` (symmetric block — NEW
      cell, same template, first new derived entry)
- [ ] One catalogue-derived cell wired into one production compute
      site as a read-through (no behaviour change — proves the
      consumer can reach the catalogue)

### Phase 2 — broaden the K-axis (next PR)

- [ ] T(2,3) trefoil → electron rows: `χ^{(2)}` and `χ^{(1,1)}` derived
- [ ] T(2,5) cinquefoil → muon rows: same two partitions
- [ ] Figure-eight 4₁ → Higgs/pion-half rows: all three partitions of 3
- [ ] Catalogue invariant tests: `Σ_λ dim(M_λ) · χ^λ(1) = …` etc.

### Phase 3 — wire derived values into the binding pipeline

- [ ] Replace the relevant extracted `χ^λ` reads in
      `closed_form_tau_M.py` / per-atom mass-table sweep with catalogue
      reads
- [ ] Each replacement annotated with the source commit hash of the
      derivation so the witness pipeline can audit
- [ ] Failing-loud guard: if a `(K, λ, A)` site asks the catalogue for
      `tier = "derived"` and only `cal-anchored` exists, the compute
      raises — forces honest provenance reporting on the L2 dashboards

### Phase 4 — Lean side (later)

- [ ] `QOU.Machinery.DerivedCharacterCatalogue` Lean module with a
      conditional class binding each `(K, λ)` cell to its R-matrix
      derivation proof (§3b-cond pattern)
- [ ] T17's existing R-matrix theorem becomes the first instance

## Out of scope (don't re-litigate)

- Real-q `c_3 = f(q)` fits — falsified by PR #1799 (4.7M× rigidity miss).
- `U_q(sl_k)`-by-rank framing of partition coverage — superseded by the
  substrate-internal account (per-atom SDP + braid-dependent
  eigenvalue magnitudes; see corpus survey 2026-06-07 in this session's
  message thread).
- Magic-shell wiring (the L3 / D11 Wigner SU(4) gap, `magic-shell-gs-
  filtration-exploitation.md`) — eligible as a Phase-3 sub-tranche but
  not bundled with the initial catalogue cells.

## Coordination

Active sibling PRs whose scope overlaps this work:

| PR | Theme | Coordination ask |
|----|-------|------------------|
| **#1762** | 1ppQ roadmap + 5-option attack plan | This work is **a hybrid of Options B (H₃ derivation) and D (Δ_λ closure)**. Heads-up that the catalogue is the structural backbone both options need. |
| **#1839** | Residue-A kernel deepening (Lean engine + cleaner-c_k re-run) | Catalogue feeds `χ^λ` cells directly into the c_k re-run — once Phase 1 lands, #1839's clean-up uses derived rather than extracted inputs. |
| **#1942** | gap-A4 content: `prop:borromean-h4-categorical-derivation` | Borromean row of the catalogue IS this proposition's compute backing. Will cite once published. |
| **#1808** | i1762 Option-E literature import (H₃→H₄ Markov stabilisation) | Catalogue gives the H₃ side a derived foundation; Markov stabilisation extends to H₄. |
| **#1765** | habiro per-knot λ(K) Family-A | Per-knot Habiro is **complementary** — different fibre object, same `(K, A)` indexing. Cross-reference, not overlap. |
| **#1741** | wire native chi-incremental (Rust batch) | Direct consumer — when Phase 3 wires derived `χ^λ` into compute, the Rust batch path is where it lands. |
| **#1789** | nuclear-binding derivation-completeness ledger | Catalogue tier flips raise the binding ledger's "derived" count. |

Coordination comments will be posted on each sibling PR with a link
back to this PR + scope statement.

## Δ_λ-gate

- **No new fits** — every catalogue cell is either R-matrix-derived
  (T17 template), Markov-normalisation-derived (T18 template), or
  carries an explicit `cal-anchored` / `extracted` tier flag.
- **No production change in Phase 1** — wiring is read-through; behaviour
  is invariant until Phase 3.
- **Failing-loud guard** ensures that once a site CLAIMS `derived`, it
  pulls a structurally-derived value or raises.
