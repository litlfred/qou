/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

# Pauli antisymmetry leaves the identical-nucleon binding channel unbound

**Formalize-first, narrowly-scoped** — the *derived* categorical half of lever 2
(the binding edge-set / occupancy question). Lean backing of the structural part
of the chirality→complete-graph result
(`docs/audits/2026-06-20-chirality-forces-complete-graph-topology.md`).

The Hecke generator satisfies `(σ - q)(σ + q⁻¹) = 0`, giving two channel
eigenvalues: the symmetric / Jones–Markov (std) channel `q`, and the
antisymmetric / alternating (Pauli) channel `-q⁻¹`. A bond contributes binding
iff its channel suppression value is a *positive sub-unity* factor `0 < f < 1`
(the strict bound test, audit §"Convention correction"). For any positive
substrate `q`, the Pauli channel value `-q⁻¹` is **negative**, so it fails the
criterion: identical-nucleon pairs (p-p, n-n), which Pauli antisymmetry forces
into this channel, are **unbound** — leaving only the p-n bonds (the bipartite /
complete graph).

## Scope (STRICT — do not over-read)

This formalizes ONLY "Pauli ⇒ identical-nucleon bonds unbound". It does **not**
claim:
- the *exact* `Z·N` p-n pair count (that occupancy selection is research-scale,
  not yet a fibre-level theorem);
- the deuteron `f_pn ≈ 0.588` magnitude (owner-gated to the s5-so3 keystone);
- a closure of the Δ_λ / binding gate (open).

The surviving p-n bonds bind via the **std-channel Markov factor**
`f_bond = c·z + d` — proved separately in `QOU/Hecke/MarkovBondFactor.lean`; the
raw eigenvalue `q` is not itself the bond factor.

**Convention D (migrated 2026-08-24), and the bound is now conditional.**  This
line read `z = √q/(q+1) ∈ (0,1)`, which is convention C, excised by the
2026-08-15 ruling in favour of `z_D = q³/(q²+1)`.  The membership is **not**
convention-neutral and the difference is not cosmetic:

* `z_C = √q/(q+1) ≤ 1/2` for **every** `q > 0` (supremum `1/2`, attained at
  `q = 1`), so `z_C ∈ (0,1)` unconditionally;
* `z_D = q³/(q²+1)` is **unbounded** (`z_D → ∞` as `q → ∞`), and `z_D < 1`
  holds exactly when `q³ < q² + 1`, i.e. `q < 1.4655712…`.

At the substrate anchor `q₀ ≈ 1.1099786` the condition is satisfied with room:
`z_D ≈ 0.6126880` (against `z_C ≈ 0.4993203`).  So the binding argument's use
of `0 < z < 1` survives the migration **at the substrate**, but it is now a
hypothesis on `q` rather than a free fact, and any downstream use at general `q`
must carry it.

Nothing in this file's Lean depends on the value: the strict bound test below is
stated for an abstract channel value `f`.

-- Ref: [leitner2026] docs/audits/2026-06-20-chirality-forces-complete-graph-topology.md ;
   docs/audits/2026-06-17-hecke-channel-chirality-binding.md
-/
import Mathlib.Tactic

namespace QOU.Hecke.PauliChannelBinding

/-- A bond contributes binding iff its channel value is a positive sub-unity
    suppression `0 < f < 1` (the strict bound test of the 2026-06-20 chirality
    audit; a non-positive value is unbound). -/
def Binds (f : ℝ) : Prop := 0 < f ∧ f < 1

/-- The antisymmetric (alternating / Pauli) channel eigenvalue of the Hecke
    generator `(σ - q)(σ + q⁻¹) = 0`. -/
noncomputable def pauliEigenvalue (q : ℝ) : ℝ := -q⁻¹

/-- For a positive substrate `q`, the Pauli channel value `-q⁻¹` is negative. -/
theorem pauliEigenvalue_neg {q : ℝ} (hq : 0 < q) : pauliEigenvalue q < 0 := by
  have hqi : 0 < q⁻¹ := inv_pos.mpr hq
  unfold pauliEigenvalue
  linarith

/-- **Pauli channel is unbound.** For positive substrate `q`, the antisymmetric
    (Pauli) channel value `-q⁻¹` fails the binding criterion `0 < f < 1` because
    it is negative. Hence identical-nucleon (p-p, n-n) bonds — forced by Pauli
    antisymmetry into this channel — do not contribute binding. This is the
    categorical backbone of the chirality→complete-graph result: only the p-n
    bonds survive. (The `Z·N` pair count and the deuteron magnitude are NOT
    claimed here — see the scope note in the file header.) -/
theorem pauli_channel_unbound {q : ℝ} (hq : 0 < q) : ¬ Binds (pauliEigenvalue q) := by
  rintro ⟨hpos, -⟩
  linarith [pauliEigenvalue_neg hq]

/-- Product identity `pauliEigenvalue q * q = -1` for nonzero `q` and unit-anchor
evaluation `pauliEigenvalue 1 = -1`. -/
theorem pauliEigenvalue_mul_q_and_at_one {q : ℝ} (hq : q ≠ 0) :
    pauliEigenvalue q * q = -1 ∧ pauliEigenvalue 1 = -1 := by
  dsimp [pauliEigenvalue]
  refine ⟨?_, by norm_num⟩
  rw [neg_mul, inv_mul_cancel₀ hq]

end QOU.Hecke.PauliChannelBinding
