# PRE-REGISTRATION — helon battery on position colour K0 (issue #9096)

Written and pushed **before** any probe code exists. Every check below is fixed
here with its pass/fail criterion. Outcomes that differ from the stated
expectation are kept as FAIL and reported; nothing is re-registered afterwards.

## 0. Rulings in force (not tested, assumed)

- Photon: `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` ∈ H₃(q). The `σ₀σ₁` form is not used.
- Electron: `σ₀σ₁σ₀ ∈ B₃`, closure the Hopf link. Backup: trefoil `σ₀³ ∈ B₂`.
- Up quark: an unknot strand (a component of the Borromean braid `β_Bor = V³`,
  `V = σ₀σ₁⁻¹`).
- Hecke: `σ² = (q − q⁻¹)σ + 1`, `h := q − q⁻¹`. Convention D: `z_D = q³/(q²+1)`.
- No fitting, no selection against a target. Exact sympy over ℚ(q); no float.
  `q₀` is not used anywhere. The gluon is not identified or selected.

## 1. Source: what is taken from the literature

Only **Bilson-Thompson 2005**, *A topological model of composite preons*
(`library/arxiv-hep-ph-0503213v2`, corpus key `bilson-thompson2005`) is held in the
library. The two other papers named in the task (Gresnigt 2017, Chester–Arsiwalla–Kauffman
2025, given as `arxiv-1711.09011v1`, `arxiv-2501.03260v1`) are **not** in `library/`
(those IDs do not exist there; `grep -i helon library/INDEX.md` returns BT 2005 only).
They are not used. The helon data below are read from BT 2005 only.

From BT 2005 §2 (pp. 1–2, `sections/sec-001-2-the-helon-model.md`):

- helons `H₊, H₀, H₋` carry twist `+2π, 0, −2π`; a `±2π` twist is charge `±e/3`;
- assumption 3: no `H₊` and `H₋` in one braided triplet;
- ordered-triplet table, colour = position of the odd-man-out:

| colour B | colour G | colour R |
|---|---|---|
| `H₊H₊H₀` u | `H₊H₀H₊` u | `H₀H₊H₊` u |
| `H₀H₀H₊` d̄ | `H₀H₊H₀` d̄ | `H₊H₀H₀` d̄ |
| `H₋H₋H₀` ū | `H₋H₀H₋` ū | `H₀H₋H₋` ū |
| `H₀H₀H₋` d | `H₀H₋H₀` d | `H₋H₀H₀` d |

  leptons `H₊H₊H₊` e⁺, `H₀H₀H₀` ν, `H₋H₋H₋` e⁻.

From BT 2005 §3 (pp. 2–3) and Figure 1 (`images/img-p003-2.png`):

- every fermion is the same two-crossing B₃ braid, "a basic braid, like that used to plait
  hair"; charges are added as twists. Read from Figure 1 (e⁺, left panel): the first
  crossing (strands 0,1) has the left strand over, the second (strands 1,2) has the left
  strand under. Encoding **b = σ₀σ₁⁻¹** (left-over convention for `σᵢ`). Because the two
  crossings have opposite sign, the four readings `σ₀σ₁⁻¹, σ₁σ₀⁻¹, σ₁⁻¹σ₀, σ₀⁻¹σ₁` form one
  orbit under inversion and conjugation, so the choice of sign convention does not change any
  quantity tested below (checked as H0).
- C (top-to-bottom mirror) is `β ↦ β⁻¹` (BT: braid ∘ mirror deforms to the trivial braid).
  P (left-right mirror) is `σᵢ ↦ σ_{2−i}⁻¹`.
- Figure 1 places positive twists at the top, negative twists at the bottom.
- bosons: trivial braid (identity permutation); fermions: non-identity permutation.
- §3 "colour interaction": quarks are combined by stacking ("pancake"), and assumption 5
  (charge equality) requires every super-strand to carry the same total twist.

## 2. Encoding into B₃ / H₃(q) with framing

A helon fermion is a framed braid `(β, t)`: `β ∈ {b, b⁻¹, P(b), P(b)⁻¹}` and
`t : {0,1,2} → {−1, 0, +1}` the per-strand twist datum of
`appendix-standard-model/strand-twist-datum.md`, attached at the twisted end (top for
`t ≥ 0` particles, bottom for `t ≤ 0`; BT Fig. 1). Twists travel with their strand.
`Q_twist = T(t)/3`, `T = Σ tᵢ`. The Hecke image is `ρ(β) ∈ H₃(q)`, `σᵢ⁻¹ = σᵢ − h`.
Full battery: 4 leptons (e⁻, e⁺, ν, ν̄) and 4 quarks (u, ū, d, d̄) × 3 colours, each in the
two handednesses BT allows (ν, ν̄ one handedness each): 2·2 + 2 + 4·3·2 = 30 framed braids.

**Identification used for colour under K0 (a modelling choice, stated here):** helon strand
position `k ∈ {0,1,2}` ↦ K0 colour position label `k`; and for the convention-D test, colour
`k` ↦ colour basis state `e_{k+1} ∈ ℂ³`. Under K0 (PR #9059, `qcd_colour_action`) colour is
a label on positions that the braid does not move (`Ř = 1_c ⊗ Ř_f`). D residual
(PR #9059, `qcd_d_residual_symmetry`): `K_D = diag(q⁻³, q⁻¹, 0)` (support {1,2}),
residual `U_q(gl₂) × U(1)`, `U(1) = N₃`.

## 3. Checks and pass/fail criteria

**H0 encoding sanity.** (a) the four readings of b are one inversion/conjugation orbit in
B₃ (checked by permutation, writhe and equality of D-traces); (b) `b·C(b) = 1` in H₃.
PASS if both hold.

**H1 charge.** For all 30 framed braids, `Q_twist = T/3` equals BT's charge and the SM
first-generation charge (e⁻ −1, ν 0, u +2/3, d −1/3, antiparticles opposite).
PASS if 30/30. Expectation: PASS (it is BT's normalisation).

**H2 twist vs crossing charge.** `strand-twist-datum.md` names `Q_twist = Q_crossing`, with
`Q_crossing = ½ writhe` (`def:coulomb-charge`), as the falsifiable consistency.
PASS for a particle if equal. Expectation: FAIL for every charged fermion (writhe(b) = 0),
PASS for ν, ν̄. Reported per particle; it is a test of the corpus's stated consistency, not
of BT.

**H3 colour under K0, end dependence.** For each quark, colour at the twisted end
(definition) vs colour at the other end (`π_β` applied). PASS ("colour is end-independent")
if equal. Expectation: FAIL for all 24 quark braids, since `π_b` is a 3-cycle.

**H4 colour under C.** The colour index read at the twisted end is preserved by C
(`u_c ↦ ū_c`, `d_c ↦ d̄_c`). PASS if 12/12 colour pairs agree.

**H5 charge equality (BT assumption 5) for the proton `d_B + u_R + u_G` (BT §3) under K0.**
Super-strand sums per K0 position at the top end (pre-braid) and at the bottom end, for
(i) all three quarks the same handedness, (ii) mixed handedness (both mixed assignments).
PASS per case if all three position sums are equal. Expectation: (i) PASS both ends;
(ii) not predicted.

**H6 colour triplets vs the D residual.** For each colour `c`, the D weight `d_c` of `e_c`
(entry of `K_D`) at the twisted end and at the other end. Questions, each PASS/FAIL:
(a) all three colours are related by the residual (expect FAIL: colour 3 has `N₃ = 1`,
`d = 0`); (b) colours 1, 2 are related by `U_q(gl₂)` (`E₁`, `F₁` map `e₁ ↔ e₂`) (expect
PASS); (c) D-visibility of a quark is end-independent (expect FAIL: `π_b` is a 3-cycle and
moves colour 3 into {1,2}); (d) the 3-cycle colour permutation commutes with `K_D` (expect
FAIL).

**H7 D radical.** Compute the radical of the trace form `(x, y) ↦ tr_D(xy)` on H₃(q) (6×6
Gram on the `T_w` basis, Ocneanu trace at `z_D`). (a) radical dimension (expect 1, the
`(1³)` block); (b) is `ρ(b)` in the radical (expect FAIL, b is invertible and the radical is
a proper ideal); (c) the sign-character value `χ_(1³)(b)` (expect 1, so b has a nonzero
component in the radical block); (d) `tr_D(b)` exact value, recorded.

**H8 corpus electron.** (a) helon electron word b⁻¹ (or P(b)) vs ruled `σ₀σ₁σ₀`: equal in
B₃? (expect FAIL); permutations (3-cycle vs transposition); closure components (1 vs 2);
writhe (0 vs 3). (b) BT fermion criterion (non-identity permutation) applied to `σ₀σ₁σ₀`
(expect: classified fermion) and to the trefoil backup `σ₀³ ∈ B₂` (expect fermion).
Reported as agreement or conflict per item.

**H9 corpus up quark.** (a) helon up quark closure is one component, unknot (via Markov
destabilisation `σ₀σ₁⁻¹ ∼ σ₀ ∈ B₂`, closure T(2,1)) — agreement with "unknot";
(b) level: helon quark = whole 3-strand triplet, corpus up quark = one strand of
`β_Bor` — recorded as a conflict of level, not of knot type.

**H10 composition reading (pre-registered coincidence check, not evidence).** If BT's
stacking is read as vertical composition (it is not; BT stacks in layers), three same-handed
quarks give `b³ = V³ = β_Bor`. Check the word identity and the closure component count of
`b³` (expect 3, Borromean rings). Labelled a coincidence in advance.

**H11 photon terms under the BT boson criterion.** Permutations of the four photon terms
`1, σ₀, σ₁, σ₀σ₁⁻¹`. BT boson = identity permutation. Expect only `1` passes; record that the
photon's fourth term is the helon fermion braid b itself.

## 4. Scope of any negative

Every FAIL is scope (a) (this encoding, this identification) unless it rests on a proved
invariant, which is named where it does (permutation of a braid word; Schur–Weyl / ideal
argument for H7b).

## 5. Outputs

`helon_battery_probe.py`, `helon-battery.witness.json`, `RESULT.md`, in this directory.
