# bk-crossing-coordination arc — work-plan refresh (2026-08-19)

**Tier:** coordination (no new results claimed beyond the two lanes below). Resumes the arc
after ~5 weeks / ~26k main commits. Branch `claude/bk-crossing-coordination-woiqj3` re-baselined
onto current main (the original 8 arc commits are already merged via #3549/#3551). PR #5346.

The arc (audit `2026-07-11-bk-crossing-coordination-multiplicity.md`) established
`w_n(K) = M_n(A)·Vol_n(K)` with `Vol` the isospin carrier and `M_n(A) = z(A)·a_D^(A)`,
`z = A−1` the per-nucleon coordination number; α-cluster extension
`B(n_α) ≈ n_α·B(⁴He) + N_bonds·b_αα`. Its four open items, reviewed against current main:

## Status of the four open items (main survey)

| # | Item | Status on main | Evidence |
|---|---|---|---|
| 1 | Categorical derivation of `M = z = A−1` | **OPEN** (derivation); numerical universality **refuted at ⁴He** — `M` is regime-dependent (`A−1` in the linear-chain regime, ~2 at the doubly-magic shell) | `2026-08-02-he4-nu-sdp-decisive-2-not-3.md` (ρ_F≈2≠3); graph facts backed but Lean was unshipped |
| 2 | Magic `a_D^(A)` activation rule | **Partially closed** — activation *gate* derived, Lean sorry-free (`MilnorIndeterminacyGate`: Hopf-spectator closes, Borromean opens); `a_D^(4)≈2.52` magnitude still empirical; no A>4 period | `alpha-cluster-activation-gate.md` |
| 3a | Close-packing count for `n_α≥5` (⁴⁰Ca) | **Closed / derived** — contact-graph edge count (fcc-10 → 24 for ⁴⁰Ca), one `b_αα` predicts ²⁰Ne/²⁴Mg/⁴⁰Ca to <0.5%; ²⁰Ne geometry hand-assigned (1-bond DOF, honest caveat) | `2026-07-11-bk-coordination-degree-and-alpha-contact.md` §2 |
| 3b | Derivation of `b_αα ≈ 2.41 MeV` | **OPEN** — guarded near-match; bare-`tr_M` route dead-ended; SU(4) base scale FOREVER-GATED | `c_alpha_alpha_categorical_via_jones_markov.py`; `alpha-cluster-model-g-closure.md` |
| 4 | Deuteron explicit crossing/coordination weight | **OPEN, deepened to structural negative** — volume leg provably 0 (trefoil flat), uniform-`z` dead, `−α log μ` over-binds 27% + mis-signs diproton; **W3 wall = corpus disagrees which knot the deuteron is** | `2026-08-16-two-nucleon-sector-final-state-eight-closures.md` (PR #5256); `BlochVolumeLegFlatVanishing.lean` |

No open sibling branch/PR is currently on this arc (checked `git branch -r`, `list_pull_requests`).

## This session's two lanes (PR #5346)

- **Lane 1 ✅ (`qou-4tj9`, backs item 1) — `QOU.Mass.CoordinationBinding`, machine-verified.**
  Shipped the Lean file deferred from #3551 (the 07-11 sandbox could not build the SimpleGraph
  cone; the full `lake-cache/qou-v4-24-0` restore now carries SimpleGraph + ProofWidgets, so it
  is `lean`-direct exit 0, sorry-free): `coordination_degree` (`z=A−1` = complete-graph degree),
  `bond_count` (`C(A,2)`), `coordination_handshake`, and the conditional `BondExtensiveBinding`
  class carrying the open extensive law `B = ε·C(A,2)`.
- **Lane 2 ✅ (backs item 3b) — `b_αα` VolDensity-scaling probe, scope-(a).** The full proton
  VolDensity route (`Vol/ℏ_q²×linking_weight`) applied to the α–α interface link 7²_1 **overshoots
  `b_αα` by 259×** (H₄) — scope-(a) refutation; the AME-implied α–α density is `ρ_αα ≈ ℏ_q²` (to
  0.45%), so the α–α binding sits exactly one `ℏ_q²` rung below the rest-mass scale
  (`ρ_p = linking_weight ≈ 2.53` is O(1)). `ρ_αα = ℏ_q²` restates the match, not a derivation
  (numerology guard). Audit `2026-08-19-b-alpha-alpha-voldensity-scaling.md`.

## Prioritized next steps (post-session queue)

1. **Item 1 (deepest):** derive *why* the multiplier is `z=A−1` in the linear-chain regime but
   ~2 at the doubly-magic ⁴He shell — the regime switch `he4-nu-sdp` exposed. The
   `BondExtensiveBinding` class (Lane 1) is the slot the derived law must fill.
2. **Item 3b forward test — DONE (2026-08-21, re-scoped).** The `ρ_αα ≈ ℏ_q²` observation was
   tested and found to be the *definitional* identity `ρ/ℏ_q² = M_need` at the single-bond `M ≈ 1`
   case — corrected Lane 2's "binding is ℏ_q²-suppressed" over-claim to `ρ_binding = M·ℏ_q²`. What
   survives non-circular: mass multiplier O(1/ℏ_q²) vs binding O(1) (mass classical, binding
   O(ℏ_q²) quantum); and `M = z = A−1` in the linear-chain regime (Lane 1 tie). Audit
   `2026-08-21-binding-hbarq-rung-forward-test.md`.
3. **Rung derivation — PARTIAL (2026-08-21).** Attacked "why mass carries `linking_weight/ℏ_q²`
   and binding the bare `M`." CLOSED: the `1/ℏ_q²` is traced to the CAL-2 muon-anchor cusp factor
   (`m_μ/m_e = Vol(4₁)/ℏ_q²`, not free); the analytic dichotomy is Lean-proved sorry-free
   (`QOU.Mass.BindingMassRung`: mass = order-2 pole residue `lw`; `binding/mass = (M/lw)·ℏ_q² → 0`).
   PHYSICAL: the saturated binding fraction `B/A/m_N` rises toward ℏ_q² (0.95·ℏ_q² at ⁵⁶Fe).
   OPEN KERNEL (bean `qou-brng`): a first-principles proof that saturation is *exactly* ℏ_q² (not
   merely O(ℏ_q²)). Audit `2026-08-21-binding-mass-rung-derivation.md`.
3. **Item 2:** turn `hoefsmit-convergence-magic-shells-intro.md`'s SW-3-root magic-shell
   saturation into the `a_D^(4)≈2.52` / `ρ_F≈2` value (replace the AME read).
4. **Item 4 (W3 first):** resolve which knot the deuteron *is* (0 or 4.4 anchor) — every
   downstream weight depends on it; the committed SnapPy data says the canonical braid closure is
   flat (Vol=0). Foothold: bean `qou-fl4t` (restore the DG flattening monomial).
