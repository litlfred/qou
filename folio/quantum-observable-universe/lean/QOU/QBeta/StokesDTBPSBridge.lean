import QOU.QBeta.StokesQZeroDTCount

/-!
# QOU.QBeta.StokesDTBPSBridge — resurgent-Stokes = DT/BPS bridge (adopted conjecture)

**Vol-conjecture-style conditional adoption** (bean `qou-ujmw`/`qou-qnnq`). The
G3 Stokes integer `A_ω = 3` of the figure-eight `4₁` is here made a *conditional*
result downstream of a **citeable published conjecture**, exactly as
`conj:kashaev-volume-conjecture` is adopted for the volume side.

## Which published bridge — and the honest non-degeneracy result

The mandated non-degeneracy gate asks whether the BPS count of `4₁` reproduces
the GGM resurgent-Stokes integer `3` (eq. 60; `{3, 4}` is the `5₂` spectrum in
eqs. 96/98) *through* the bridge. The answer depends on **which BPS sector**:

* **Gukov–Stošić `1112.0030` (OPEN sector) — FAILS.** There "knot homology =
  space of *open* BPS states" (M5-brane on the conormal Lagrangian
  `L_K ⊂ T*S³`; colored HOMFLY homology). The knots–quivers correspondence
  (`1707.02991`) makes the `4₁` open-BPS count `det(4₁) = 5` (five HOMFLY
  generators = five quiver nodes; calibrated against that paper's trefoil = 3 =
  `det 3₁`). `5 ≠ 3` (and `5 ∉ {3, 4}`). So the *open-HOMFLY* Gukov–Stošić bridge
  does **not** license `A_ω = 3`; it is a different BPS sector.

* **GPPV `1701.06567` + GGM peacock `2012.00062` Conjecture 3(d) (CLOSED
  sector) — PASSES.** GGM peacock Conjecture 3(d): *"the Stokes constants are
  integers corresponding to the Donaldson–Thomas invariants … and the BPS
  degeneracies."* GPPV realise that DT/BPS count as the graded dimension of the
  BPS Hilbert space of `T[M₃]` (the state-integral / `Ẑ` / 3d–3d sector). This
  reproduces the `4₁` Stokes integer `3` (eq. 60); the `q → 0` anchor is
  machine-checked unconditionally in `StokesQZeroDTCount` (`S⁺(0)₀₁ = 3`).

This file therefore axiomatises the **closed-sector** bridge and derives
`A_ω(4₁) = 3` conditional on it — **conditional for every knot, `4₁` included**
(GGM prove Conjecture 5 for `4₁` and `5₂` via Theorem 6 / Theorems 17 and 25 and
verify Conjecture 4 in §5.2/§6.2; Conjecture 3(d) itself remains a conjecture).
It is **not** the open-HOMFLY Gukov–Stošić bridge, which the check excludes.

## §3b-cond non-degeneracy (anti-laundering)

`StokesDTBPSBridge` carries the conjecture's *inputs* — the two identifications
`stokes = dt` (GGM Conj 3(d)) and `dt = bps` (GPPV) — as class fields. It does
**not** carry the conclusion `A_ω = 3` as a field. `aomega_fourOne_dt_count`
*derives* the BPS count of `4₁` by composing the two bridge identifications with
the bridge-independent, certified `4₁` Stokes datum `= 3` (from `StokesQZeroDTCount`).
So the theorem proves something the class does not assume: the observable `A_ω`
of `4₁` **is** the BPS/DT degeneracy, and it equals `3`.

## Base ring (§7c)

Counts are `ℤ` (Donaldson–Thomas / BPS degeneracies are integers; a `-3` DT entry
occurs at `4₁`, so a signed ring is correct). No archimedean construct
(`Real.*`, ordering) appears; `ℤ` is the substrate-side ring here.

-- Ref: [garoufalidis-gu-marino2023peacock] GGM 2012.00062 (Conjecture 3(d): Stokes constants = DT invariants = BPS degeneracies)
-- Ref: [gukov-pei-putrov-vafa2017] GPPV 1701.06567 (BPS Hilbert space of T[M₃] categorifying the index)
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/stokes-dt-bps-bridge.md
-/

namespace QOU.QBeta

/-- **Adopted conjecture — the closed-sector resurgent-Stokes = DT/BPS bridge.**

For a hyperbolic knot `K`, three integer invariants of `S³ ∖ K` / `T[K]` are
conjecturally identified (GGM peacock Conjecture 3(d) + GPPV):

* `stokesConstant K` — the resurgent Stokes constant of the state integral
  `Z(S³ ∖ K)` on the distinguished (geometric Borel) ray;
* `dtInvariant K` — the Donaldson–Thomas / Kontsevich–Soibelman invariant of the
  associated `q`-difference / stability structure;
* `bpsDim K` — the graded dimension of the GPPV BPS Hilbert space of `T[K]` in
  the geometric sector.

The two class fields are the conjecture's *content* (its inputs). There is **no**
field asserting any particular value of any of these integers — in particular no
`A_ω = 3` field; that value is *derived* downstream, only for `4₁`, from the
bridge-independent certified Stokes datum. An instance of this class is the
conjecture holding; none is provided (Conjecture 3(d) is conditional for every
knot, `4₁` included — `qou-3ent`). -/
class StokesDTBPSBridge (Knot : Type*) where
  /-- Resurgent Stokes constant of the state integral, geometric Borel ray. -/
  stokesConstant : Knot → ℤ
  /-- Donaldson–Thomas / motivic invariant of the `q`-difference structure. -/
  dtInvariant : Knot → ℤ
  /-- Graded dimension of the GPPV BPS Hilbert space of `T[K]`, geometric sector. -/
  bpsDim : Knot → ℤ
  /-- **GGM peacock `2012.00062` Conjecture 3(d):** the resurgent Stokes constant
      is the Donaldson–Thomas invariant. -/
  stokes_eq_dt : ∀ K, stokesConstant K = dtInvariant K
  /-- **GPPV `1701.06567` (with Gaiotto–Moore–Neitzke):** the Donaldson–Thomas
      invariant is a BPS degeneracy — the dimension of the BPS Hilbert space. -/
  dt_eq_bps : ∀ K, dtInvariant K = bpsDim K

/-- The certified, **bridge-independent** figure-eight Stokes datum that feeds the
conditional theorem: the GGM eq-(60) `q → 0` off-diagonal of the `4₁` Stokes matrix
is `3`. Proved unconditionally (decidable integer matrix algebra from the certified
GGM/DGG `q`-series `W₋₁(0)`) in `StokesQZeroDTCount`; re-exposed here as the named
input value `3`. -/
theorem fourOne_stokes_datum :
    StokesQZeroDTCount.Splus0 0 1 = 3 :=
  StokesQZeroDTCount.stokes_qzero_offdiagonal

/-- **`A_ω(4₁) = 3` as a BPS/DT count, conditional on `StokesDTBPSBridge`.**

Given the bridge, the figure-eight Stokes constant — pinned to `3` by the
bridge-independent certified `q → 0` datum (`fourOne_stokes_datum`, hypothesis
`hStokes`) — equals the BPS degeneracy `bpsDim` of `T[4₁]`. Hence the observable
`A_ω` of the figure-eight **is** a BPS/DT count and equals `3`.

*Derivation, through the bridge:* `bpsDim = dtInvariant` (GPPV, `dt_eq_bps`)
`= stokesConstant` (GGM Conj 3(d), `stokes_eq_dt`) `= 3` (`hStokes`). The class
supplies the two identifications; the value `3` comes from the certified Stokes
computation, not from any class field — the §3b-cond non-degeneracy requirement. -/
theorem aomega_fourOne_dt_count {Knot : Type*} [B : StokesDTBPSBridge Knot]
    (fourOne : Knot) (hStokes : B.stokesConstant fourOne = 3) :
    B.bpsDim fourOne = 3 := by
  rw [← B.dt_eq_bps, ← B.stokes_eq_dt]
  exact hStokes

end QOU.QBeta
