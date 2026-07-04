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
  4-body link requires the SDP/canonical-knot-ID at A=4, which needs B₅ Hoefsmit
  seminormal reps + the Clarabel SDP backend (`atomic-braid-recipe-4he-canonical`:
  "not yet SDP-optimum-verified at A=4; solver scope A≤3"; Clarabel unreachable
  in this sandbox).
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

The forward path is infrastructure, not a probe: implement **B₅ Hoefsmit** so the
SDP/canonical-knot-ID can run at A=4 and *select* the ⁴He link, whose volume is
then one SnapPy call away (the harness in this probe's `--live` path). That is an
owner-scoped build (Clarabel + higher Hecke reps), coordinated with the
canonical-knot-ID / SDP cluster — not an idle-time move.
