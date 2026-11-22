# Pre-registration: ∇ from the corpus SU(2) calculus on the 3-strand states (2026-11-21)

Committed before `mn_su2_calculus_nabla_probe.py` is run.

## Source of ∇ (corpus search, this session)

The only concrete connection in the corpus is on `A = O(SU(2))` with the left-invariant calculus
`Ω¹ = span{ω₁, ω₂, ω₃}` (`connection-su2.md`), Reeb generator `ξ = ½ diag(1, −1)` and canonical
form `ω₃`, horizontal = no `ω₃` component (`reeb-su2.md`). `nablaEndo` in Lean is never
instantiated, and the nucleon weight-space files define braid generators and charges, not a
connection.

## Identification used (mine, stated so it can be rejected)

On the state space `(C²)^{⊗3}` the left-invariant vector fields act through the U_q(sl₂)
coproduct: Reeb = Cartan `ξ_tot` (`ΔH = H⊗1 + 1⊗H`), horizontal = root vectors `E, F`
(`ΔE = E⊗K + 1⊗E`, `ΔF = F⊗1 + K⁻¹⊗F`, `K = q^{H}` with `H = diag(1, −1)` per strand).
Flat connection: `𝒜 = 0`. The connection 1-form is free data in the corpus and is not chosen here.

## Tests, all exact sympy

States: every normalised vector in `W_p = (2,1)` (uud weight) and `W_n = (1,2)`, parametrised
by a generic vector with symbolic entries and the pairing `φ = ψ^T/ (ψ^Tψ)`.

- T1: horizontal expectations `φ E_tot ψ`, `φ F_tot ψ` for every state. Expected 0 (E, F shift weight).
- T2: Reeb expectation `φ ξ_tot ψ`. Expected `+1/2` (p) and `−1/2` (n), state-independent.
- T3: K-weighted Reeb matter term `tr(K ψφ ξ_tot) = w·⟨ξ⟩` and its n − p difference.
- Pass condition for the 12: a horizontal eigenvalue `μ = 12` (or ratio 12) in some state. Expected:
  impossible under the flat connection, since T1 forces `μ = 0`.

Disclosure: T1 and T2 follow from weight bookkeeping, so the outcome is anticipated. The probe
records it exactly and checks the identification is internally consistent (U_q relations).
