# Δ_λ-gate unblock — three-lever status after disciplined execution (2026-06-23)

**Branch:** `claude/bold-mendel-5994kg` · **PR #2612**
**Status:** progress report. **No closure manufactured, no fit, no fabrication.**
Each lever separates the *genuinely-derived* part from the *genuinely-gated* part.
Triaged by three parallel state-mappers (main was +116 commits, keystone active
today), then the tractable formalize-first step executed per lever.

This is the constructive companion to
[`2026-06-23-over-zealous-binding-closure-review.md`](2026-06-23-over-zealous-binding-closure-review.md):
that doc stopped *over-claiming closed*; this one is careful not to *over-claim
derived*.

---

## Lever 1 — fibre kernel `R(q,x)` / the keystone "matrix M": **collapsed to one scalar gate**

**Starting framing:** "the open input is the owner-gated Bring prolongation
matrix `M` (Picard–Fuchs / Gauss–Manin / monodromy) — a differential-geometry
construction."

**Found state (already in the corpus, proved):** `M` is **not** an open 8×8
DG object. It is structurally reduced to a **2×2 matrix with `det = 1`**, so the
kernel is

$$ R(q,x) = x^2 - \tau\,x + 1, \qquad \tau = \operatorname{tr} B \ \text{(single unknown)}. $$

- **depth = 2** — S₅/A₅ Schur decomposition `H¹(Ω¹)|_{A₅} = 2·G`
  (`s5_bring_hodge_depth.py`, 3/3 machine-checked) + Griffiths transversality.
- **det = 1** — symplectic polarisation, `prop:sl2-prolongation-recurrence`
  (sorry-free Lean).
- The recurrence is then `a_{n+2} = τ·a_{n+1} − a_n`.

**Machinery — validated, runs today:**
- [`substrate/sl2_tau_solver.py`](../../computations/substrate/sl2_tau_solver.py)
  self-validates on the torus periods: `τ = (P₁+P₃)/P₂ = 2cosh(2η₀)` exact, the
  `det=1` recurrence holds on all windows.
- [`substrate/unified_tau_odd_partner_solve.py`](../../computations/substrate/unified_tau_odd_partner_solve.py)
  runs the **binding** τ-solve and **PASSES** on the selection-rule anchors:

  | period | value | source | status |
  |---|---|---|---|
  | `a_D^(2)` | `1` | c=1 muon/knot | exact ∀q |
  | `a_D^(3)` | `(q+1)²/(3q)` | c=2 Hopf-link | **PREDICTION** (the gate) |
  | `a_D^(4)` | `(3q²+4+3q⁻²)/4` (Family-A) | c=3 proton/Borromean | derived |

  ⇒ `τ(q₀) = 2.6424`, `a_D^(5) = 5.3556` (odd-partner), recurrence consistent to 50 dps.

**The single remaining gate (precise, checkable, NOT owner-gated DG):** confirm
the c=2 value is the actual #1765 selection-rule value
`λ(L=Hopf) = (1/3)·Σ_{λ⊢3} dim_q`. The same rule is **confirmed** at c=1
(`(1/2)Σ_{λ⊢2} dim_q = 1`) and c=3 (`(1/4)Σ_{λ⊢4} dim_q = (3q²+4+3q⁻²)/4`, a
sorry-free Lean identity in `_li_2_q_util`). So the lever reduces to **one scalar
check**: does `(1/3)Σ_{λ⊢3} dim_q = (q+1)²/(3q)`? If yes,
`thm:binding-closure-conditional` becomes **unconditional**. If no, the c=2 anchor
is corrected and τ refined.

**Now done (post-rebase, 2026-06-23).** After rebasing onto main (+119), the
#1765 selection-rule blocks + the canonical q-hook `dim_q`
(`phase5_n8_dim_q_table`) are in tree. The c=2 check is **confirmed
derivation-tight** (no fabrication):
[`binding_selection_rule_tau_closure.py`](../../computations/binding_selection_rule_tau_closure.py)
computes all three τ-anchors as ONE rule `lw(c)=(1/(c+1))·Σ_{λ⊢c+1} dim_q` via
the canonical `dim_q` — `lw(1)=1`, `lw(2)=(q+1)²/(3q)` (the former gate),
`lw(3)=(3q²+4+3q⁻²)/4` (Family-A, **bit-for-bit** = production
`linking_weight_family_a`) — and they satisfy the proved depth-2 det=1
recurrence (`τ(q₀)=2.6424`, `a_D⁵=5.3556`). Wired both ways: **MASS** (`lw(c)` is
the VolDensity linking weight, `mba-step09a`) and **BINDING** (`a_D^(n)=lw(n−1)`
→ kernel `R`, `mba-step09b`).

**Residual (open, honest):** the geometric↔algebraic identification
`a_D^(n)=lw(n−1)` — that the SW prolonged period *equals* the selection-rule
value (#1765). The *algebraic* side (the rule's values + the recurrence) is
closed; the SW-period identification is not. Did NOT construct the Bring matrix
`M` (keystone actively worked on main — coordinate).

**Net:** lever 1 went from "owner-gated DG matrix M" → "one rule, confirmed via
the canonical `dim_q`, satisfying the proved recurrence," sole residual the
SW-period↔selection-rule identification.

---

## Lever 2 — binding edge-set / occupancy: **derived categorical half formalized**

The chirality→complete-graph result (RMS 6.19, zero-parameter,
`2026-06-20-chirality-forces-complete-graph-topology.md`) has a *derived*
categorical half and a *research-scale* half. The derived half is now Lean:

- **Delivered:** [`QOU/Hecke/PauliChannelBinding.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/PauliChannelBinding.lean)
  (sorry-free, lean-direct exit 0): the antisymmetric (Pauli) Hecke eigenvalue
  `-q⁻¹` is `< 0` for `q > 0`, so it fails the binding criterion `0 < f < 1` —
  identical-nucleon (p-p, n-n) bonds, forced by Pauli antisymmetry into this
  channel, are **unbound**. This is *why* only the p-n bonds survive.

- **Still gated (honest):** the *exact* `Z·N` p-n pair count is research-scale
  (not yet a fibre-level theorem — it is the best-fitting occupancy among
  candidates, not categorically forced); the deuteron `f_pn ≈ 0.588` magnitude is
  owner-gated to the s5-so3 keystone. Static integer bond graphs are refuted.

---

## Lever 3 — universal-ρ normalisation: **the ratio is a ρ-free prediction; the scale is gated**

The q-Reeb model `B(K) = ρ·S(K)`, `S = Σ_λ y_λ dim_λ |Δθ_λ|`. The key separation:

- **Delivered (genuine no-fit prediction):**
  [`binding_reeb_ratio_rho_free.py`](../../computations/binding_reeb_ratio_rho_free.py)
  → [witness](../../computations/binding-reeb-ratio-rho-free.witness.json). The
  A=3 mirror **ratio** is ρ-INDEPENDENT — `B(³H)/B(³He) = S(³H)/S(³He)` (ρ
  cancels): predicted `1.1173` vs AME `1.0990` = **+1.67%, no fit, no free
  parameter**. This is a real substrate prediction, **not** post-hoc.

- **Still gated (honest):** the **absolute** scale `ρ ≈ 18.5 MeV/rad` is *fitted*
  (`ρ_need = B_AME/S`, CAL-4-gated). Deriving a *per-λ* `ρ_λ` from one total
  binding is exactly the underdetermined Δ_λ gate (six ansätze failed). A
  numerical scan for `ρ = f(substrate)` would be numerology and is not run.

---

## Cross-cutting

None of the three manufactured a closure. The Δ_λ / per-isotope binding gate
**remains open** (`precision-goals.md`: 3/7 L2 met). What changed:

| lever | before | after (this session) |
|---|---|---|
| 1 | "owner-gated DG matrix M" | **one rule confirmed via canonical `dim_q`** (c=2 derivation-tight); proved recurrence holds; wired to mass + binding; residual = SW-period↔rule ID |
| 2 | "static graphs refuted; occupancy open" | Pauli→pp/nn-unbound **formalized** (sorry-free); Z·N count still research-scale |
| 3 | "ρ≈18.5 fitted; 1.7% post-hoc" | A=3 **ratio** is a ρ-free **prediction** (1.67%); absolute ρ still CAL-4-gated |

## Cross-references

- [`2026-06-23-over-zealous-binding-closure-review.md`](2026-06-23-over-zealous-binding-closure-review.md) — the framing-rescope companion.
- [`docs/workplans/2026-06-06-deriving-bring-M-abelianisation-scalar.md`](../workplans/2026-06-06-deriving-bring-M-abelianisation-scalar.md) — the M→2×2→τ reduction.
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — the keystone open object (active).
- [`2026-06-22-charge-slambda-reeb-phase-crack.md`](2026-06-22-charge-slambda-reeb-phase-crack.md) — the q-Reeb phase A=3 result.
