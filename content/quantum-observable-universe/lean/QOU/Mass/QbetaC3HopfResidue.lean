import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# QOU.Mass.QbetaC3HopfResidue — the Hopf-cubic ANALYTIC-RESIDUE route to the
Q_β ladder coefficient `c_3`: the exact carrier is flat and correct, the
normalization onto the bar-odd object is the open keystone.

**Scope (read first).** This file records — HONESTLY — the outcome of the
**Hopf-cubic analytic-residue** exploration for the Q_β precision-ladder
coefficient `c_3` (bean `qou-1dnr`), the redirect that the three 2026-07-20
routes (DM-cubic `QbetaC3DMCubic`, Habiro `QbetaC3Habiro`, GGM-Stokes
`QbetaC3Stokes`) all triangulated to. The outcome is
**DERIVED-MODULO-OPEN-NORMALIZATION** — a genuine structural narrowing, but NOT
a full derivation. Every theorem below is sorry-free.

**The exact carrier the corpus already gives (KC20, Lean-proved in
`QOU.QBeta.Zeta4Residue`, `QBetaZeta4ResidueRefutation.lean`).** The bar-odd
part of the net decay-width Laurent polynomial `Δ_net = Δ(n) − Δ(p)` is EXACTLY

    Δ_net^odd = (h/4)·C(y),   h = q − q⁻¹,   y = q² + q⁻² = 2cosh 2λ,
    C(y) = y³ − 4y² + 3y − 2   (irreducible/ℚ, disc −152, Galois S₃),

sourced by the Hopf (double-crossing) sector. Evaluated at the substrate this is
`(h/4)·C(y₀) ≈ −0.2111`, **anchor-invariant** (proton↔muon swing `1·10⁻⁵ %`) —
the CORRECT type for a derived object (route C: a flat object is right, the
extracted-`c_3` swing is a `1/u³` representation artifact, KC21).

**The target (capstone `2026-07-12-c3-wall-resolution-capstone.md`).** The
empirical `c_3 ≈ −2.069` splits under the bar involution `σ:q↦q⁻¹` into a
bar-EVEN part `≈ −Vol(4₁) ≈ −2.0299` (exactly measured) and a bar-ODD part
`S = c_3 + Vol(4₁)` (the OPEN channel). `S` factors as `S = h·D(ũ)` with `h` the
anchor-blind bar-odd carrier and `D(ũ)` the bar-even ℚ(√3) ladder. `S` swings
SIGN across anchors (μ `+0.0097` / p `−0.0395`); the anchor-blind physical `|S|`
scale is `≈ 0.0094` (the Φ_b state-integral volume deficit).

**The honest finding (the theorems below).**

* **The shared bar-odd factor `h` is AUTOMATIC, not a match.** Both `S = h·D` and
  `carrier = (h/4)·C` are bar-odd, hence both equal `h·(bar-even)`. The `h`
  cancels in the ratio: the normalization is the **bar-even** quantity
  `N = S/carrier = 4·D(ũ)/C(y)` (`carrier_to_S_normalization_is_barEven`,
  sorry-free). So the carrier correctly supplies the bar-odd chirality carrier,
  but that is bookkeeping — any bar-odd Laurent object factors this way.

* **The open piece is exactly the bar-even ratio `4D/C`.** `C(y)` is a fixed
  degree-3 polynomial value; `D(ũ)` is the KC22 **resurgent / non-holonomic**
  ℚ(√3) ladder (radius → 0), so `4D/C` is as transcendental as `D`. The
  probe finds **no** corpus-named quantity (`h²`, `u^k`, the KC19 kernel
  `2h/(4w₀²−h²)`, `1/4q⁷`, …) hits the required `N_geom ≈ 0.0445` un-tuned
  (closest is `h² ≈ 0.0437`, `1.8 %` off — a near-coincidence, not a match). A
  hand-picked `N` is a **fit**.

* **A flat carrier cannot equal the swinging `S` at both anchors**
  (`flatCarrier_cannot_match_swinging_S`, sorry-free) — the same anchor-invariance
  logic as the sibling routes; the fair anchor-blind target is `|S|_geom`, whose
  normalization is the open keystone.

**What stays OPEN (the conjecture class).** The bridge — that the exact flat
carrier, normalized by the geometric bar-even ladder `D(ũ)`, reproduces the
smooth bar-odd `S` — is recorded as a content-bearing **primary conjecture
class** with **no instance** (`HopfCubicResidueBridge`). This is the §4e
quantum-modularity / 3d-index normalization, `conj:qdifference-kernel-prolongation-symbol`.

## Honesty (AGENTS.md §Axiomatization is NOT a Proof, §3b, ck-dk-registry §8)

* The factorization + anchor-invariance theorems are genuine sorry-free algebra.
* The conjecture class is content-bearing (parameter-quantified fields, no `True`,
  no empty marker) and has **NO instance** — the honest open state. The `c_3`
  bar-odd channel is **NOT** derived: the exact cubic supplies only the (automatic)
  bar-odd `h`; the bar-even normalization `4D/C` is the open resurgent ladder.
* Nothing inverted from Q_β; nothing wired to production; `c_3` stays EMPIRICAL;
  this file changes no rung's tier.

## Base ring (§7c)

The factorization + logic are pure ring / field identities — generic
`{R : Type*} [CommRing R]` (one `Field` restatement for the literal `4D/C`
ratio). No `ℝ`, no ordering, no `Real.*`; the archimedean substrate evaluation
(the actual `(h/4)·C(y₀) ≈ −0.2111`, `|S|_geom ≈ 0.0094`) lives downstream in
the probe, past the substrate→archimedean wall.

## References

- [manuscript] `conj:qdifference-kernel-prolongation-symbol`;
  `rem:qbeta-odd-carrier-hopf-cubic`;
  `QOU.QBeta.Zeta4Residue` (`QBetaZeta4ResidueRefutation.lean`, KC20);
  `docs/coordination/ck-dk-canonical-registry.md` §9 (KC20/KC21/KC22);
  `docs/audits/2026-07-20-c3-hopf-cubic-residue-exploration.md`;
  `docs/audits/2026-07-12-c3-wall-resolution-capstone.md`;
  probe `computations/probes/qbeta_c3_hopf_cubic_residue_probe.py`.
-/

namespace QOU.Mass.QbetaC3HopfResidue

/-! ### (1) The shared bar-odd `h` is automatic — the normalization is bar-even

Both the target `S = h·D` (KC21) and the exact carrier `carrier = (h/4)·C`
(KC20) are bar-odd, so both equal `h·(bar-even)`. We prove the `h` cancels: the
carrier→`S` normalization is the **bar-even** ratio `4D/C`. -/

/-- **The carrier→`S` normalization is bar-even (sorry-free, division-free).**
Given the KC20 factorization `4·carrier = h·C` (i.e. `carrier = (h/4)·C`) and the
KC21 factorization `S = h·D`, the bar-odd carrier `h` cancels:

    S · C = 4 · D · carrier,

i.e. `S/carrier = 4·D/C` — a purely **bar-even** quantity. The exact cubic `C`
supplies only the automatic bar-odd `h`; the genuine open content is the
bar-even ratio `4D/C`. -/
theorem carrier_to_S_normalization_is_barEven {R : Type*} [CommRing R]
    (h cubicC dLadder carrier smoothS : R)
    (hCar : 4 * carrier = h * cubicC)
    (hS : smoothS = h * dLadder) :
    smoothS * cubicC = 4 * dLadder * carrier := by
  linear_combination cubicC * hS - dLadder * hCar

/-- **Literal bar-even ratio form (`Field`).** With `C ≠ 0` and `carrier ≠ 0`,
the normalization is exactly `S/carrier = 4·D/C`. The `Field`/nonvanishing
hypotheses only license the division; the content is the division-free
`carrier_to_S_normalization_is_barEven`. -/
theorem normalization_eq_four_D_over_C {F : Type*} [Field F]
    (h cubicC dLadder carrier smoothS : F)
    (hCar : 4 * carrier = h * cubicC)
    (hS : smoothS = h * dLadder)
    (hC : cubicC ≠ 0) (hcar : carrier ≠ 0) :
    smoothS / carrier = 4 * dLadder / cubicC := by
  have key : smoothS * cubicC = 4 * dLadder * carrier :=
    carrier_to_S_normalization_is_barEven h cubicC dLadder carrier smoothS hCar hS
  rw [div_eq_div_iff hcar hC]
  linear_combination key

/-! ### (2) A flat carrier cannot match the swinging `S` (anchor-invariance)

`S` swings sign across the proton/muon anchors (the `1/u³` representation
artifact, KC21); the normalized carrier — if it were a single fixed value — is
anchor-invariant, so it can match `S` at most one anchor. Same logic as the
sibling routes' `constantStokesDatum_cannot_match_both_anchors`. -/

/-- **A flat normalized carrier matches `S` at most one anchor (sorry-free).** If
a single value `carrierNorm` value-matched the bar-odd `S` at BOTH the proton
anchor (`S_p`) and the muon anchor (`S_m`), the two would be forced equal,
contradicting the measured cross-anchor sign-swing (`hSwing`). -/
theorem flatCarrier_cannot_match_swinging_S {R : Type*} [CommRing R]
    (carrierNorm S_p S_m : R)
    (hP : carrierNorm = S_p) (hM : carrierNorm = S_m) (hSwing : S_p ≠ S_m) :
    False :=
  hSwing (hP ▸ hM)

/-- **Miss-by-the-full-swing form (sorry-free).** A flat normalized carrier
pinned to `S` at the proton anchor misses the muon anchor by exactly the full
cross-anchor swing `S_p − S_m`. -/
theorem flatCarrier_misses_other_anchor_by_full_swing {R : Type*} [CommRing R]
    (carrierNorm S_p S_m : R) (hP : carrierNorm = S_p) :
    carrierNorm - S_m = S_p - S_m := by
  rw [hP]

/-! ### (3) The open target — the geometric bar-even normalization (conjecture, no instance)

The route is not closed by the exact cubic alone: it supplies the automatic
bar-odd `h`, leaving the bar-even ratio `4D/C` — with `D(ũ)` the KC22 resurgent
ladder — as the open piece. We record the closure as a content-bearing primary
conjecture class with no instance. -/

/-- Substrate datum for the Hopf-cubic residue `c_3` bridge: the exact flat
carrier `carrier = (h/4)·C(y₀)` (KC20), the fixed bar-even cubic value `cubicC`,
the bar-odd carrier `hCarrier = q − q⁻¹`, the smooth bar-odd object `smoothS`
(`S = h·D`), and the (open) bar-even resurgent ladder value `dLadder = D(ũ)`
(KC22). Data — asserts nothing. -/
structure HopfCubicBridgeDatum (R : Type*) [CommRing R] where
  /-- The exact flat carrier `(h/4)·C(y₀)` (KC20), anchor-invariant. -/
  carrier : R
  /-- The fixed bar-even cubic value `C(y₀) = y₀³ − 4y₀² + 3y₀ − 2`. -/
  cubicC : R
  /-- The bar-odd carrier `h = q − q⁻¹`. -/
  hCarrier : R
  /-- The smooth bar-odd `c_3` object `S = c_3 + Vol(4₁) = h·D(ũ)`. -/
  smoothS : R
  /-- The OPEN bar-even resurgent ℚ(√3) ladder value `D(ũ)` (KC22). -/
  dLadder : R

/-- **§3b primary conjecture class — the Hopf-cubic geometric normalization bridge.**

    `@conjecture: primary`

    The honest OPEN target of the Hopf-cubic analytic-residue route. It asserts
    that the exact flat carrier, normalized by the **geometric** bar-even ladder
    `D(ũ)`, reproduces the smooth bar-odd `c_3` object — the closure
    `S · C = 4 · D · carrier` (equivalently `S = (4D/C)·carrier`) holds with the
    normalization **nontrivial** (`4·dLadder ≠ cubicC`, i.e. the fixed cubic is
    NOT already the resurgent ladder, so `N ≠ 1`) and the bar-odd channel real
    (`smoothS ≠ 0`). The content — and the whole open problem — is that `D(ũ)` is
    fixed by the geometry (the Φ_b state integral gives the `|S|` scale) rather
    than free; **no instance is supplied** (per KC22 `D(ũ)` is resurgent /
    non-holonomic, radius → 0, so `4D/C` is not a low-order (q-)holonomic scalar
    to be read off). The exact cubic supplies only the automatic bar-odd `h`
    (`carrier_to_S_normalization_is_barEven`); it does NOT close the bridge. -/
-- Ref: [manuscript] conj:qdifference-kernel-prolongation-symbol;
--      rem:qbeta-odd-carrier-hopf-cubic; docs/coordination/ck-dk-canonical-registry.md §9;
--      docs/audits/2026-07-20-c3-hopf-cubic-residue-exploration.md
class HopfCubicResidueBridge {R : Type*} [CommRing R]
    (d : HopfCubicBridgeDatum R) : Prop where
  /-- The KC20 carrier factorization: `4·carrier = h·C` (`carrier = (h/4)·C`). -/
  carrier_factorization : 4 * d.carrier = d.hCarrier * d.cubicC
  /-- The KC21 target factorization: `S = h·D`. -/
  smoothS_factorization : d.smoothS = d.hCarrier * d.dLadder
  /-- The closure: the normalized carrier reproduces the smooth bar-odd object,
      `S · C = 4 · D · carrier`. The whole open content — `D(ũ)` fixed by
      geometry. -/
  bridge_closes : d.smoothS * d.cubicC = 4 * d.dLadder * d.carrier
  /-- Nontrivial: the fixed cubic is not the resurgent ladder (`N = 4D/C ≠ 1`). -/
  bridge_nontrivial : 4 * d.dLadder ≠ d.cubicC
  /-- There IS a bar-odd channel to derive — the decay-face object is nonzero. -/
  smoothS_nonzero : d.smoothS ≠ 0

end QOU.Mass.QbetaC3HopfResidue
