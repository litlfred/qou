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

### Phase 1 — schema + first derived entries ✅ DONE

All items landed in PR #1952. Schema + lookup API + first 3 Borromean
cells (independently re-derived via R-matrix, cross-validates T17 from
PR #1933) + read-through consumer demo.

### Phase 2 — broaden the K-axis ✅ DONE

12 cells across 5 knots: Borromean, Figure-eight, Hopf (diquark),
Trefoil (electron), Cinquefoil (muon). Schema migrated to Laurent-in-q
canonical form.

### Phase 3 — production isotope sweep ✅ DONE

Rust-backed sweep via `pyhecke_native.chi_q_via_gp`. 715 derived cells
through A=6 (p, n, D, T, ³He, ⁴He, ⁵Li, ⁶Li). A=7+ tractable offline.
Failing-loud guard wired (`DerivedChiCatalogue.lookup_derived`).

### Phase 3 optimisations ✅ DONE (multi-tier)

- **GIL release** on `chi_q_via_gp` — `py.allow_threads` patch in
  `pyhecke_native v0.9.0` (locally built + verified 2.87× on 4 cores).
- **Auto-detect parallel backend** (`derived_chi_catalogue_parallel.py`)
  — threads when GIL released, processes fallback otherwise.
- **Tier 4** — `mn_chi_q` lru_cache memoize.
- **Tier 3** — bar-conjugate symmetry, verified 100% on 348 pairs,
  wired into sweep (1.9× speedup, 176/176 cross-verified).
- **Tier 2** — M_n disk cache, pre-filled for n ∈ {3, 6, 9, 12, 15}
  (37,935 entries, 3 MB).
- **Tier 1** — LR / parabolic factorisation: audit doc landed
  ([`2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`](2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md));
  full implementation requires deuteron-base + recursive multi-bridge
  cases (follow-up; estimated 1-2 sessions for Phase 1.1).

Full audit roadmap:
[`2026-06-07-pyhecke-native-gil-release-patch.md`](2026-06-07-pyhecke-native-gil-release-patch.md).

### Phase 4 — Lean side ✅ DONE (first instance)

- [x] `QOU.Machinery.DerivedCharacterCatalogue` Lean module registered in
      `QOU.lean` (was an orphan — imported nowhere, so CI never built it).
- [x] `IsRMatrixDerived` upgraded from an opaque `True` marker to a genuine
      §3b-cond conditional class over `{R : Type*} [Field R]` (§7c — the
      Kauffman Laurent needs `q⁻¹`, so `Field` not `CommRing`): real
      `R → R` character fields (`storedChi`, `rmatrixChi`) + a real equality
      `Prop` (`agrees`).
- [x] T17's existing R-matrix theorem is the first instance:
      `borromeanTwoOneBaryonChi_eq_t17` proves the stored Kauffman Laurent
      equals T17's h-form at `q²` by reusing the proven
      `chi21_borromean_qform_eq_hform`. Borromean instance fully discharged
      (no `sorry`). The form-lemmas were generalised from `ℚ` to
      `{R} [Field R]` in the same pass.
- [ ] Remaining cells (Trefoil, Cinquefoil, Hopf, Figure-eight, A≥4
      isotopes) get instances — follow-up; each is a `field_simp; ring`
      identity against its own published character.

**Note — witness-filename split (2026-06-07).** Verifying the Phase-3
sweep on a fresh container surfaced a collision: both
`derived_chi_catalogue_build.py` (342-cell catalogue + T17/Schur-Weyl
cross-check, consumed by `DerivedChiCatalogue.load()`) and
`derived_chi_catalogue_sweep.py` (715-cell production sweep) wrote
`derived-chi-catalogue.witness.json`, clobbering each other. The sweep now
writes `derived-chi-catalogue-sweep.witness.json`; the build file is
unchanged so consumers are unaffected.

**Bottleneck (long-compute discipline).** The full `--max-A 6` sweep is
715 cells in ≈232 s wall; ⁶Li (B₁₈, 385 partitions, 195 `chi_q_via_gp`
calls) dominates at ≈222 s. A≥7 is offline-only without further Tier-1
factorisation.

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
