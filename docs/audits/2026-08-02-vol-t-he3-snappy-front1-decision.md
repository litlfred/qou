# Front-1 decision point: Vol(T), Vol(³He) of the actual braid closures — `ρ=tr_M` radial handle refuted under every volume reading (scope-a)

**Date:** 2026-08-02 · **Beans:** qou-0g4z / qou-g5fm (front 1 of the C_knot attack menu), qou-afkd ·
**PR:** #4610 (branch `claude/vol-t-he3-snappy-2026-08-02`) · **Parent:** #4603 · **Axis:** Δ_λ / binding
magnitude · **Discipline:** 0-fit, formalize-first, scope-(a); nothing wired.

## The question #4603 left open

PR #4603 refuted the radial ansatz `C_knot = Vol(K)·ρ(K)/ℏ_q²` with `ρ = tr_M` **under the assumption
`Vol(T)=Vol(³He)`** (mirror knots): `C_knot(T)/C_knot(³He)=1.35` (>1) vs `tr_M(T)/tr_M(³He)=0.50` (<1),
anti-correlated. It flagged one open question that decides the survivor: **is `Vol(T)` actually equal to
`Vol(³He)`?** The two braids differ (`tr_M(T)=0.104 ≠ tr_M(³He)=0.207`), so mirror-knot equality was only
an assumption. This PR computes the volumes.

## The braid words (H₉, 9-strand)

`β_T = atom_braid_word_3A(1,2)`, `β_³He = atom_braid_word_3A(2,1)` (`computations/mass_at_3A_proper.py`;
producer of the `chi-{tritium,helium-3}-h9` witnesses via `per_irrep_pole_atom.py`). Each nucleon owns 3
strands; crossings come in three types from `atom_canonical_crossings`:

- `sigma` = σ_g (positive crossing, genuine topological)
- `sigma_inv` = σ_g⁻¹ (negative crossing, genuine)
- `averaged` = σ_g − h/2·1 — a **Hecke-algebra element** (the p-n / color interfaces), **not** a
  topological crossing.

T (order p,n,n) and ³He (order p,p,n) are genuinely different words (16σ/12σ⁻¹/7avg vs 18σ/10σ⁻¹/7avg;
distinct interface signs: T has p-n(avg)+n-n(σ⁻¹), ³He has p-p(σ)+p-n(avg)).

## Method

SnapPy 3.3.2. Closure built with `snappy.Link(braid_closure=…)` (σ_g→+ (g+1), σ_g⁻¹→−(g+1)); the
`averaged` Hecke crossings have no single topological representative, so each is taken under three
definite conventions (avg→+, avg→−, avg→drop) and robustness is checked. Hyperbolicity: a closure counts
as hyperbolic iff SnapPy finds a triangulation with all tetrahedra positively oriented (with
`ManifoldHP.verify_hyperbolicity` as non-gating confirmation). **Pipeline validated in-run**: fig-8 →
2.02988, Borromean → 7.32772, trefoil (torus) → 0.

## Reading 1 — the literal mass-braid H₉ closures are NON-HYPERBOLIC

| K | avg→+ | avg→− | avg→drop |
|---|---|---|---|
| T (4–5 comp) | degenerate, Vol=0 | degenerate, Vol=0 | degenerate, Vol=0 |
| ³He (4–5 comp) | degenerate, Vol=0 | degenerate, Vol=0 | degenerate, Vol=0 |

Under **every** convention, SnapPy finds no positively-oriented triangulation after aggressive
retriangulation + randomization — the trefoil/torus-link signature. So **`Vol(T)=Vol(³He)=0`
(degenerate)**. A zero volume annihilates the handle: `Vol·ρ/ℏ_q² ≡ 0`, which cannot equal the nonzero
`C_knot≈3–4`. The mass-braid closure carries **no** hyperbolic volume, so it cannot be the radial handle
**regardless** of the T-vs-³He comparison. (This is consistent with the framework's actual mass compute,
which uses the *per-block Borromean* `Vol(𝓑₃)=7.328` — a per-nucleon constant — not the full-nucleus
mass-braid closure volume.)

## Reading 2 — the corpus binding links are hyperbolic but UNEQUAL

The corpus's per-nucleus hyperbolic volumes are the SDP binding links
(`computations/binding_link_volumes.py`), SnapPy-verified here:

| K | binding link | Vol |
|---|---|---|
| T | 8₁₁ | **8.2863168** |
| ³He | L6a4 = Borromean | **7.3277248** (= 8·Catalan) |

**`Vol(T)/Vol(³He) = 1.131` — UNEQUAL, T bigger.** So "mirror nuclei ⇒ equal Vol" is false here too, and
the asymmetry runs in the direction #4603's C_knot needs. Re-running the mirror test with the true
volumes (`C_knot(T)/C_knot(³He) = (Vol(T)·ρ(T))/(Vol(³He)·ρ(³He))`, ℏ_q² cancels, 0-fit):

| ratio | value | side of 1 |
|---|---|---|
| C_knot(T)/C_knot(³He) | 1.350 | **>1** |
| tr_M(T)/tr_M(³He) | 0.504 | <1 |
| Vol(T)/Vol(³He) | 1.131 | >1 |
| **radial pred = Vol·tr_M** | **0.570** | **<1** |
| ratio-of-ratios (=1 iff holds) | **2.37** | — |

The volume asymmetry is real and in the right direction but **far too weak** (1.13×) to flip `tr_M`'s
wrong-direction ratio (0.50): the radial prediction stays on the **opposite side of unity** from
`C_knot`. Residual **2.37×**, anti-correlated.

## Verdict — `ρ=tr_M` refuted under every volume reading (scope-a)

- **Reading 1** (literal mass-braid closure): `Vol≡0` (non-hyperbolic) ⇒ handle identically 0.
- **Reading 2** (corpus binding link, hyperbolic, unequal): the true volume asymmetry does not rescue
  the ansatz — 2.37× anti-correlated residual.

This **strengthens** #4603: it was not the equal-Vol assumption that killed `ρ=tr_M` — the ansatz fails
with the true volumes too. **The only surviving door is a DERIVED density `ρ ≠ tr_M`** whose T/³He ratio
exceeds `~2.1` (so that `Vol·ρ` ratio > 1) — and it must be *derived*, never a `ρ` reverse-engineered
from `C_knot` (that is a fit, forbidden to wire). `ρ = tr_M` is off the table.

**Honest scope.** scope-(a): this refutes the specific density `ρ = tr_M` in the radial handle. It does
**not** exclude the radial handle with a different derived density, nor claim a *proved* topological
invariant forbidding the mass-braid closures from being hyperbolic (the non-hyperbolicity is a robust
SnapPy computation across conventions, not a Lean-proved (b)-exclusion). `free_parameters = 0`;
`B_AME` enters only through the fixed master-formula `C_knot` values; nothing wired; no fit.

## Machine-checked (Lean, sorry-free, lean-direct)

`content/quantum-observable-universe/lean/QOU/MassTheory/VolTHe3RadialHandle.lean`:

- `radial_ratio_general` — with distinct volumes, `C_knot(T)/C_knot(³He) = (V_T·ρ_T)/(V_He·ρ_He)`
  (only ℏ_q² cancels; generic field).
- `degenerate_vol_kills_handle` — `Vol(K)=0 ⇒ C_knot ≠ Vol·ρ/h` for nonzero `C_knot` (Reading 1).
- `binding_link_vol_ratio_gt_one` / `binding_link_pred_ratio_lt_one` / `cknot_ratio_gt_one` — the
  witnessed ratios (Reading 2) straddle 1.
- `mirror_test_excludes_rho_trM_true_vol` — the radial ansatz at the true binding-link volumes implies
  `False`.
- `rho_trM_radial_handle_refuted_every_reading` — capstone.

## Files

- `computations/deltalambda/vol_t_he3_snappy_probe.py`
- `computations/deltalambda/vol-t-he3-snappy.witness.json`
- `content/quantum-observable-universe/lean/QOU/MassTheory/VolTHe3RadialHandle.lean`

## Where front 1 goes next

`ρ = tr_M` is dead. The radial handle survives only with a **derived** `ρ ≠ tr_M` (survivor 1 of #4603)
whose T/³He ratio > ~2.1 under the binding-link volumes — the natural candidate is the per-block-vs-global
density reconciliation (`mass_vol_density.compare_density_readings`), which must be *derived*, not fitted.
The mass-braid-closure hyperbolic volume is off the table (degenerate).
