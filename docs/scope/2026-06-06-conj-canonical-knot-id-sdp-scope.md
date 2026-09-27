# Scope — `conj:canonical-knot-id-sdp` (knots-from-SDP, GAP-A-1)

**Date:** 2026-06-06
**Status:** scoping only (no execution) — research-grade, multi-session
**Block:** [`conj:canonical-knot-id-sdp`](../../folio/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md)
**Lean:** `qou:QOU.BraidKnot.helium3_uniqueness_closed`
(= `nucleus_uniqueness_closed 9`)

This is the lever the owner flagged in "are knots determined by SDP?" /
"thread 2 3" / "1 2". It is the categorical statement that the confinement
SDP **selects** the canonical knot of each light nucleus — turning the
historical hyperbolic-volume↔AME-binding match into a derivation. Closing it
(even one nucleus) makes `Vol(K)` a *derived* SDP optimum rather than a
heuristic, which is precisely what **Thread 2** (per-knot `VolDensity(K)`,
A≥3) and **Thread 4** (link-volume assignment) are blocked on.

---

## 1. What the conjecture claims

For each light nucleus `𝔥 ∈ {²H, ³H, ³He}`, the joint mass-tower confinement
SDP

```
min ‖ ρ·[tr_M(T_w) + tower(T_w) + tr_M(C_dimq)]·𝔈₀ − B_AME(𝔥) ‖²
  over T_w ∈ H_{3A}(q₀)^{GB-NF},  ρ ∈ ℤ_{>0}
  s.t. ‖T_w‖_Frob ≤ Δ_max
```

has a **unique** global minimizer `T_w⋆`, achieved at the historically
volume-matched knot:

| Nucleus | knot/link | n₀=3A | ρ | B_AME (MeV) | binding K |
|---|---|---|---|---|---|
| ²H | 6₂ (Miller) | 6 | 1 | 2.2246 | L_H (Hopf) |
| ³H | 8₁₁ | 9 | 2 | 8.4820 | 8₁₁-class link |
| ³He | L_6a4 | 9 | 2 | 7.7181 | L_6a4 |

with residual < 0.5 % of `B_AME`. The conjecture is **downstream of**
`conj:brane-tower-z-habiro` (its `uses[]`), so it is properly a conjecture
and can at most become *conditional-on-class* (§3b-cond), never an
unconditional theorem.

---

## 2. What is actually closed vs. what looks closed (read this first)

The manifest `lean.ref` points at `helium3_uniqueness_closed`, which is
**sorry-free** — but this is a *trivial-instance* closure, not a proof of the
conjecture. Three distinct layers, easy to conflate:

| Layer | Lean object | Genuinely closed? | What it proves |
|---|---|---|---|
| **Trivial shell** | `nucleus_uniqueness_closed n` | ✅ sorry-free | the **empty-constraint** SDP (`nucleusEmptySDP`: cost = `1`, `ι = Empty`) has a unique optimum — namely `Φ⋆ = 0` (`rfl`). Dimension-independent; ³He = n=9 is one case. **Says nothing about L_6a4.** |
| **Abstract bridge** | `canonical_T_w_unique_under_strict_complementarity`, `canonical_T_w_subsingleton` | ⚠ axiom-dependent | strict-complementarity ⇒ unique SDP optimum, *re-stated for Hecke elements* — but rests on `strict_complementarity_unique_axiom` (Boyd–Vandenberghe §5.5) and casts through a **non-faithful** representation (next row). |
| **Interior-case real** | `real_strict_complementarity_unique_of_dualSlack_posDef` | ✅ sorry-free | uniqueness when the dual slack `S(y)` is positive-**definite** (interior optimum). This is the *engine* the trivial shell uses (`S = 1`). |

Two structural stubs block the bridge from meaning "L_6a4 is the knot":

- **`heckeAsMatrix` is rank-1 `x ⊗ x`** (`CanonicalKnotIdSDPUniqueness.lean`
  line 52). It is PSD (proved) but **not faithful** — distinct Hecke
  elements can map to the same matrix, so "unique matrix optimum" does *not*
  yet give "unique Hecke element / unique knot." The faithful
  Wedderburn-block (Hoefsmit seminormal) representation is the open Lean port.
- **`nucleusEmptySDP` has `ι = Empty`** — no confinement constraint, cost =
  identity, optimum = `0`. The *real* ³He SDP has cost
  `‖ρ·[tr_M+tower+tr_M(C)]·𝔈₀ − B_AME‖²` and the `Δ_max` Frobenius ball;
  its optimum must be `T_{L_6a4}`, not `0`.

**Bottom line:** the conjecture's *uniqueness shape* is sorry-free on a
degenerate instance; the *substantive content* (the real SDP selects the
real knot) is open. (Trivial-skeleton lineage:
`docs/audits/_deprecated/2026-05-08-trivial-skeleton-workplan.md`.)

---

## 3. Numerical state per nucleus (substrate-only R5-full solver)

From `r5-full-canonical-knot-solver.witness.json` /
`r5_full_canonical_knot_solver.py`:

| Nucleus | canonical T_w | α⋆ | PSD-feasible at q₀? | rank in 138 KLR classes | gating |
|---|---|---|---|---|---|
| ³He | L_6a4 | 0.000 | **yes** ✅ | 24 (top 17 %) | — closest to closure |
| ²H | 6₂ | 0.891 | no (single-term cost) | 62 (top 45 %) | needs multi-term cost (T2–T6 of `thm:knot-mass-formula-unified`) |
| ³H | 8₁₁ | — | deferred | — | needs H₅ Hoefsmit (Rust `hecke-engine`) |

- **³He** — PSD-feasibility verified, α⋆=0 sits on the structural target in
  the (2,1) Wedderburn block; recovered word `(σ₁σ₂⁻¹)³` matches the
  historical SnapPy braid up to generator-sign (same KLR class). Strong
  duality `|primal − dual| ≤ 10⁻⁶` recorded.
- **²H** — single-term `B = m_e·ρ·tr_M(T_w)` does *not* make 6₂ the winner;
  multi-term wiring is the next closure step.
- **³H** — pipeline deferred on H₅ Hoefsmit seminormal.

Factorization (issue #604) splits uniqueness into:
**(a) constituent uniqueness** (each nucleon-trefoil unique at H₃(q₀)) —
*closed numerically* (`joint_tower_sdp_solver_v2.py`); and
**(b) binding-K uniqueness** (`K(𝔥) ∈ H_{3A}(q₀)` unique under joint-tower
cross-level constraints) — **open**, the categorical theorem still required.

---

## 4. Gates to substantive closure (ordered)

| # | Gate | Difficulty | Couples to |
|---|---|---|---|
| **G1** | Faithful Hecke→matrix rep (Wedderburn-block/Hoefsmit) replacing the rank-1 `heckeAsMatrix` stub | hard (Lean Hoefsmit port) | Rust `hecke-engine` Hoefsmit; Thread 3 §9.4 L-3 |
| **G2** | Non-trivial per-nucleus SDP instance (real cost + `Δ_max` ball) replacing `nucleusEmptySDP` | **moderate — tractable for ³He** | the R5-full witness |
| **G3** | Discharge `strict_complementarity_unique_axiom` (B–V §5.5) — only the *boundary/active-set* case; interior case already proved | hard (no Mathlib convex-opt) or self-contained from active-set+duals | LP/SDP dual witnesses |
| **G4** | Strict-complementarity certificate `StrictComplementarity 𝔥` from witnesses | ³He: ready (α_gap=0 + strong duality); ²H/³H: gated | §3 numerical state |
| **G5** | Binding-K uniqueness (sub-assertion b) via binding-K SDP solver mode | open | Thread 4 |
| **G6** | Proof obligations 1–3: finitude of `Δ_max`-ball candidate set; exhaustive/B&B no-smaller-residual; ρ uniqueness | moderate–hard | `prop:plancherel-weight-boundedness` |

---

## 5. De-risked entry point (the smallest substantive bite)

**G2 + G4 for ³He only.** Build the *real* ³He confinement SDP instance
(non-empty `ι`, real cost, `Δ_max` ball) and feed the **already-recorded**
R5-full witness (α_gap = 0, strong duality ≤ 10⁻⁶) as the
`StrictComplementarity ³He` certificate, consuming the **already-proved**
interior-case `real_strict_complementarity_unique_of_dualSlack_posDef`.

Why this is the de-risked bite:
- α⋆ = 0 for ³He means the optimum is at the **structural target** — if it is
  an *interior* optimum (dual slack PosDef), the proved interior-case engine
  applies directly and **G3's boundary axiom is not needed**.
- The recovered-word χ-fingerprint already matches L_6a4, so a faithful
  representation may be sidesteppable for ³He specifically (compare
  fingerprints, not full matrices) — **G1 partially deferrable**.
- It converts the trivial-instance shell into a *real ³He instance* — the
  first non-degenerate datapoint of the conjecture.

What it does **not** close: ²H/³H (need multi-term cost / H₅ Hoefsmit),
binding-K (b), and the general boundary-case axiom.

---

## 6. Coupling to Threads 2 & 4

```
conj:canonical-knot-id-sdp (this)
   │  closing ³He / ²H ⇒ Vol(K) is a DERIVED SDP optimum, not a volume-match heuristic
   ├──► Thread 2 (per-knot VolDensity, A≥3): supplies the canonical Vol(K) it needs
   ├──► Thread 2 (²H step): 6₂ closure removes the Vol(6₂) heuristic + chi-D-h6 naming-bug gate
   └──► Thread 4 (link-volume assignment): binding-K (G5) IS the per-nucleus link volume
```

Thread 2's A≥3 step and Thread 4's link-volume assignment are the *same*
open object as this conjecture's gate G5 (binding-K uniqueness). They should
be worked together, not in three separate branches.

---

## 7. Recommendation

- **Not a single-session close.** Each of G1, G3, G5 is its own multi-session
  effort; several couple to the Rust `hecke-engine` Hoefsmit port.
- **First tranche (fresh focused session):** §5's G2+G4-for-³He — real
  instance + witness certificate, riding the proved interior-case engine.
  This is the one bite with a realistic single-session payoff and a concrete
  test (the trivial shell becomes a real ³He uniqueness statement).
- **Correct the record:** the `lean.ref` "sorry-free closure" is a trivial
  shell (empty SDP, optimum 0); a future commit should add an `authorNote`
  or narrative line to the block so the green ref is not mistaken for a proof
  of the conjecture. (Filed here rather than edited inline — out of this
  scoping pass's remit.)
