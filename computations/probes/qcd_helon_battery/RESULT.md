# RESULT — helon battery on position colour K0 (issue #9096)

> **Owner ruling 2026-11-22 (Ruling 111, `docs/coordination/owner-rulings.md`):** The helon is kept as a fallback only and is **not** adopted; the standing rulings (electron $\sigma_0\sigma_1\sigma_0 \in B_3$, up quark as an unknot strand) are unchanged.

- Pre-registration: `PREREG.md`, commit `3221839d006`, pushed before any probe code.
- Probe: `helon_battery_probe.py`. Witness: `helon-battery.witness.json`.
- Exact sympy over ℚ(q) (Hecke, traces) and ℚ(t) (reduced Burau, faithful on B₃).
  No float. `q₀` is not used. No gluon is identified or selected.
- **14/25 checks pass.** Of the 24 pre-registered checks, 23 came out as pre-registered.
  The one that did not is H5(i), kept as a FAIL. One post-hoc check (H5-post) is labelled.

## Source

Only Bilson-Thompson 2005 (`library/arxiv-hep-ph-0503213v2`, key `bilson-thompson2005`) is
held. The two other papers named in the task (Gresnigt 2017, Chester–Arsiwalla–Kauffman 2025)
are **not** in `library/` and were not used. The helon table is BT §2 (pp. 1–2). The braid is
read from BT Fig. 1 (p. 3, the "plait" braid): **b = σ₀σ₁⁻¹**, writhe 0. Its four sign/order
readings form one orbit under inversion and conjugation, so no result depends on the reading
(H0a).

**The helon fermion braid is the photon's fourth term.** `b = σ₀σ₁⁻¹ = V`, and the cube is the
corpus Borromean core `V³ = β_Bor` (H10, H11).

## Verdict per particle

All 30 framed braids: e⁺, e⁻ (two handednesses each), ν, ν̄ (one each), and u, ū, d, d̄ × 3
colours × 2 handednesses.

| particle | Q_twist = T/3 (H1) | = ½ writhe (H2) | K0 colour end-independent (H3) | D-visibility end-independent (H6c) | corpus ruling (H8/H9) |
|---|---|---|---|---|---|
| e⁻ | −1 ✓ | ✗ (writhe 0) | n/a | n/a | **conflict**: σ₁σ₀⁻¹ / σ₀⁻¹σ₁ ≠ σ₀σ₁σ₀ in B₃ |
| e⁺ | +1 ✓ | ✗ | n/a | n/a | conflict (same) |
| ν, ν̄ | 0 ✓ | ✓ | n/a | n/a | no ruling |
| u (×3 colours ×2) | +2/3 ✓ | ✗ | ✗ 0/6 | 2/6 | knot type agrees (unknot); **level conflicts** |
| ū | −2/3 ✓ | ✗ | ✗ 0/6 | 2/6 | as u |
| d | −1/3 ✓ | ✗ | ✗ 0/6 | 2/6 | no ruling |
| d̄ | +1/3 ✓ | ✗ | ✗ 0/6 | 2/6 | no ruling |

## Findings

1. **Charge (H1, pass 30/30).** `Q_twist = T/3` reproduces BT's and the SM first-generation
   charges. This is BT's own normalisation, and `strand-twist-datum.md` adopts it, so the pass
   is a consistency check of the encoding, not evidence.

2. **Twist charge vs crossing charge (H2, 2/30).** Every helon fermion has writhe 0, so the
   halved-writhe `Q` of `def:coulomb-charge` is 0 for all of them. The consistency
   `Q_twist = Q` that `strand-twist-datum.md` names as the falsifiable test therefore fails
   for every charged fermion and holds only for ν, ν̄. Scope (a): this encoding. The
   coulomb-charge block itself already says the identification of `Q` with electric charge is
   not established.

3. **K0 colour is end-dependent (H3, 0/24).** The braid's permutation is a 3-cycle,
   `π_b = (0→2, 1→0, 2→1)`. Under K0 colour is a fixed position label, and a twist moves with
   its strand. So a helon quark's colour read at the top and at the bottom differ by that
   3-cycle for every quark. Scope (b) for this braid family: the invariant is the permutation
   of `b`, which is a 3-cycle in each reading. Colour under K0 is well defined only after an
   end is chosen.

4. **C preserves colour (H4, 6/6).** This holds by construction, because C is a top–bottom
   reflection.

5. **Proton charge equality (BT assumption 5) under K0 (H5): the pre-registered expectation
   was wrong.**
   - BT's own check sums the ordered triplets of `d_B + u_R + u_G` to (1,1,1). It reads u at
     the top and d at the bottom, which mixes the two ends.
   - With twists carried along strands to a common end (K0 positions fixed), the sums are
     unequal at both ends in all 8 handedness assignments (H5(i), H5(ii)).
   - **Post-hoc (H5-post):** if every table is read at the top, the top sums are equal 8/8 and
     the bottom sums 2/8. The two that pass are those where d has the same permutation as the
     u's (d from one panel of Fig. 1, u from the other).
   - So under K0, charge equality fixes a relation between the quarks' braid permutations
     that BT does not state. Scope (a).

6. **Convention-D residual (H6).** Identification: colour position k ↦ `e_{k+1} ∈ ℂ³`, with
   `K_D = diag(q⁻³, q⁻¹, 0)`.
   - The three colours are **not** all related by the residual `U_q(gl₂) × U(1)`. Colours 1
     and 2 form a `U_q(gl₂)` doublet (`E₁`, `F₁`). Colour 3 is a singlet with `N₃ = 1` and
     D weight 0, so D does not see it.
   - The braid's 3-cycle does not commute with `K_D`. So D-visibility is end-dependent for 16
     of 24 quark braids: a quark that is D-visible at one end is invisible at the other.
   - Which colour is switched off is a free basis choice (PR #9059, R3). This probe uses {1,2}
     and flags that as a selection. The 8/24 count does not depend on it, because a 3-cycle
     moves exactly one colour into and one out of the dead slot.

7. **D radical (H7).**
   - The radical of `(x,y) ↦ tr_D(xy)` on H₃(q) has dimension 1 and spans the sign block
     `(1³)`: `r σᵢ = −q⁻¹ r`.
   - No helon braid lies in it. Scope (b): `ρ(b)` is invertible and the radical is a proper
     ideal.
   - `χ_(1³)(b) = (−q⁻¹)(−q) = 1`, so every helon braid has a nonzero component in the block
     that D kills.
   - `tr_D(b) = q²/(q²+1)² = z_D² − h z_D`. This is the photon's `φ₀₁` coefficient in the
     sibling's D-trace data, as it must be, since the term is the same element.

8. **Electron (H8): conflict.**
   - The helon electron is `b⁻¹` or `P(b)⁻¹`: a 3-cycle, closure 1 component (unknot),
     writhe 0.
   - The ruled electron `σ₀σ₁σ₀` is a transposition, closure the Hopf link (2 components),
     writhe 3. They are unequal in B₃ (reduced Burau).
   - The trefoil backup `σ₀³ ∈ B₂` also differs, since it lives in B₂ and has writhe 3.
   - BT's fermion criterion (non-identity permutation) does classify `σ₀σ₁σ₀` and `σ₀³` as
     fermions. That is information for the open statistics question of the electron (issue
     #8822); it is not a derivation.

9. **Up quark (H9): knot type agrees, level conflicts.**
   - The helon up quark closes to the unknot: by Markov destabilisation `σ₀σ₁⁻¹ ∼ σ₀ ∈ B₂`,
     the closure is T(2,1).
   - The helon quark is a whole three-strand triplet. The ruled up quark is a single strand
     of `β_Bor`.

10. **Composition coincidence (H10, labelled in advance).** If BT's layered stacking were
    read as vertical composition, three same-handed quarks would give `b³ = V³ = β_Bor`: 3
    components, pairwise linking 0. BT stacks in layers, not by composition. Not evidence.

11. **Photon under BT's boson criterion (H11).** Only the `1` term has identity permutation.
    `σ₀`, `σ₁` and `σ₀σ₁⁻¹` are fermion-type under BT. The fourth term is literally BT's
    fermion braid.

## Conflicts with corpus rulings (summary)

- Electron: BT 3-cycle unknot (writhe 0) vs ruled `σ₀σ₁σ₀` Hopf link (writhe 3). Direct
  conflict.
- Up quark: unknot in both, but a triplet in BT vs one strand in the corpus.
- Photon: BT photon is the trivial braid with untwisted helons. The ruled photon has three
  non-identity-permutation terms, one of which is the BT fermion braid.
- K0: BT colour is end-dependent under K0, and BT's proton charge equality needs a
  permutation-matching condition BT does not state.

No ruling is changed. These are reported, not acted on.

## Scope

- Every FAIL is scope (a) (this encoding, this identification), except where an invariant is
  named:
  - H3: the permutation of `b` is a 3-cycle;
  - H7b: invertible ∉ proper ideal;
  - H6a: `N₃` is central in the residual and `e₃` spans an invariant line.
- Not done: Gresnigt 2017 and Chester et al. 2025 (not held); higher generations (BT gives no
  explicit braids); the gluon; any Lean formalisation.

## Verification

`python3 -u helon_battery_probe.py` gives `SUMMARY 14/25`. `scripts/precision-gates.sh --changed`
was run; see the PR comment for its output.
