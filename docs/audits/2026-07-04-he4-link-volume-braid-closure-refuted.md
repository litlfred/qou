# The ⁴He 4-body link volume is not reachable by braid closure

**Status:** FINDING (reproducible, no fit). SnapPy 3.3.2 runs in this sandbox,
lifting the "needs SnapPy" block all four θ_λ siblings carried — but the obvious
route to the ⁴He 4-body link (close the canonical braid word, take its volume)
comes back **negative**: braid closure does not reproduce the SDP binding links
at *any* A, so it cannot supply Vol₄. The bond-count back-out `Vol₄ ≈ 8.046`
stays unverified, gated on the SDP/canonical-knot-ID at A=4.

Probe: [`he4_link_volume_braid_closure.py`](../../computations/he4_link_volume_braid_closure.py)
(witness `he4-link-volume-braid-closure.witness.json`; `--live` re-verifies
against SnapPy, and matches the baked values exactly).

## Context

The linear-chain bond-count binding `B = m_e·Σ(n−1)·Vol_n`
([PR #3282](https://github.com/litlfred/qou/pull/3282), merged) reproduces ³H to
−0.16% and backs out the ⁴He 4-body link volume as `Vol₄ ≈ 8.046`
(`theta_mn_bondcount_linearchain.py`, from `residual = m_e·3·Vol₄`), flagged
"falsifiable — compare to the SnapPy volume of the ⁴He 4-component link." No
sibling ran it; SnapPy was believed unavailable.

**SnapPy 3.3.2 does install and run here** (`pip install snappy`; fig-8 =
2.0298832128 ✓). The prior blocked attempts (`_deprecated/he4-jsj-topology`,
the difference-knot probe) needed *SageMath*; link volumes need only SnapPy.

## Result — closure ≠ the binding-link assignment rule

Closing the canonical operator-valued atomic word `atom_canonical_crossings(Z,N)`
(the "averaged" inter-nucleon interface `σ_g − h/2·1` mapped to a topological
crossing — every mode +σ / −σ / drop gives the same outcome), then simplifying +
randomizing in SnapPy:

| word | closure | binding link (SDP) | match? |
|---|---|---|---|
| proton (B₃) | 2-comp, non-hyperbolic (Vol→0) | 𝓑₃ = Borromean (3-comp, 7.328) | ✗ wrong components |
| neutron (B₃) | 2-comp, non-hyperbolic | 𝓑₃ = Borromean (3-comp, 7.328) | ✗ |
| ³H (p-n-n) | **4-comp**, non-hyperbolic | 8_11 (**1-comp** knot, 8.286) | ✗ wrong link type |
| ³He (p-p-n) | **4-comp**, non-hyperbolic | L6a4 = Borromean (**3-comp**, 7.328) | ✗ |
| ⁴He (p-p-n-n) | 5-comp, non-hyperbolic | (unknown) | — |

The mismatch is **not a triangulation artifact**: the component counts are wrong
(³H closure is 4-component but 8_11 is a 1-component knot). The SDP binding links
are the outputs of the **canonical-knot-ID** map (`conj:canonical-knot-id-sdp`,
issue #604 / GAP-A-1), not the Markov closure of the operator-valued word.

## The A=4 gate (scope-(a), no fit)

- **The closure route to the ⁴He 4-body link is dead** (5-component,
  non-hyperbolic; ≠ any binding link).
- **`Vol₄ ≈ 8.046` stays an unverified bond-count back-out.** The canonical
  4-body link requires the canonical-knot-ID at A=4 (`conj:canonical-knot-id-sdp`,
  #604).

  > **Correction (2026-07-04, superseding the paragraph as first written).** The
  > first version of this bullet said the A=4 case "needs B₅ Hoefsmit seminormal
  > reps + the Clarabel SDP backend." **Both are wrong** — I was misled by a stale
  > status note in `atomic-braid-recipe-4he-canonical.derivation.json` ("B_5
  > Hoefsmit pending"). In fact: (i) **general-n Hoefsmit already exists** —
  > `hecke_characters.build_seminormal_matrices` supports any partition of any n
  > (verified at n=5: Hecke + braid relations hold), and `binding_k_solver.py`
  > (lines 20-24, 47-49) states the ³H B_5/8_11 case needs "no separate H_5
  > detour"; (ii) the binding-K evaluator is a **pure numpy/scipy algebraic
  > Wedderburn evaluation, not an SDP** (`binding_k_solver.py` lines 8-14), so
  > **Clarabel is not involved**. The A=4 link is gated on the *identification*
  > (#604), which is computable in-sandbox via the Jones polynomial of the
  > binding-K factor — not on any missing infrastructure.
- **A real A=4 tension is recorded, not resolved:** the provisional doubly-magic
  assignment `2·Vol(Borromean) = 14.655` (`binding_a3plus_*`) disagrees with the
  bond-count back-out `8.046` by ~1.82×. Both are unverified; the SDP-derived
  link is needed to adjudicate.

**Scope discipline.** This is a scope-(a) negative — *braid closure, alone, does
not reproduce the binding links*. It is **not** a refutation of the bond-count
model (whose ³H/³He predictions stand) and **not** a structural exclusion of
`Vol₄ ≈ 8.046`; that value is simply unverified until the SDP selects the A=4
link. Assigning a 4-body link by matching 8.046 would be a CAL-4 fit — out of
bounds.

## Next

The forward path is **not** an infrastructure build (see the Correction above —
general-n Hoefsmit exists, no Clarabel needed). It is a direct computation now
that SnapPy is available:

1. compute `ρ_λ(K) = ρ_λ(T_w(⁴He))·ρ_λ(constituents)⁻¹` per Wedderburn block
   `λ ⊢ 12` (existing general-n Hoefsmit, `binding_k_solver.py` machinery);
2. form the Jones polynomial `J_K(q) = Σ_λ y_λ·tr ρ_λ(K)` (the Markov trace);
3. identify `K` by matching `J_K` against the knot/link tables;
4. `Vol₄` = the hyperbolic volume of `K` (SnapPy) — compared to the `8.046`
   back-out and the `14.655` doubly-magic provisional.

Steps 1-2 realize the canonical-knot-ID (`conj:canonical-knot-id-sdp`, #604) as
a concrete Jones-polynomial identification; step 3 may resolve cleanly or land on
an ambiguous / non-tabulated `K`, in which case that ambiguity is the honest
residual. Pursued in the follow-up branch.
