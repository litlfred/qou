# Pre-registration: a Yukawa-type pairing of the Higgs vacuum with doublet strands (route Y)

Bean `qou-99qc`. Written 2026-11-21 before the Lean was compiled and before any number was
evaluated. Companion Lean:
`folio/quantum-observable-universe/lean/QOU/QuarkState/YukawaVacuumPairing.lean`.

## Question (owner, Carl, 2026-11-21: route Y)

PR #8676 (`HyperchargeGradingNoGo.lean`, `total_eq_iff`) proved that a per-strand energy χ gives
`E(n⊗ν) − E(p⊗e⁻) ≠ 0` only if `χ(q,d) + χ(ℓ,u) ≠ χ(q,u) + χ(ℓ,d)`: a strand-TYPE × FLAVOUR
interaction. Every function of the conserved totals (T³, Y, Q) has none. The Standard Model gets
such an interaction from Yukawa couplings after electroweak symmetry breaking. The corpus has the
Higgs vacuum as a point/copoint `ϱ : 𝟙 → X`, idempotent `e_H`, residual `1 − e_H`, `tr e_H = 1`
(`HiggsVacuumResidual.lean`, owner ruling 2026-11-20) but no action of it on a doublet strand.
Build the minimal pairing and say what the corpus forces.

## Arms and expected outcomes (stated before computing)

1. **Unbroken-symmetry constraint.** Any per-strand energy operator that commutes with the unbroken
   grading on the doublet (`K = diag(q^{n_u}, q^{n_d})`, `n_u ≠ n_d`, `q` not a root of unity) is
   diagonal in the weight basis. A rank-1 idempotent that commutes with it is a weight projector
   `P_u` or `P_d`; so `e_H` restricted to a doublet is a weight projector and `1 − e_H` the other.
   Expected: forced, generic field.
2. **`tr e_H = 1` forces the vev slot to have grading weight 0.** For the pivotal trace
   `Tr(K ·)` with `K = diag(q^{n_u}, q^{n_d})`, `tr(P_s) = q^{n_s}`; on an ordered field with
   `q > 1` this is 1 iff `n_s = 0`. With the bare `K = q^{2T³}` (`n = ±1`) no slot has weight 0, so
   the owner's `tr e_H = 1` cannot hold on an un-shifted doublet: the Higgs doublet needs a
   hypercharge shift putting one slot at charge 0. Expected: forced (given that the trace is the
   pivotal trace of the unbroken grading — a premise, named).
3. **Type-blind pairings give zero split.** Every construction in which quark and lepton strands are
   the same object and the vacuum acts by ONE morphism — (a) spectator `id ⊗ e_H` then trace over
   the Higgs strand (expected: the identity, flavour-blind), (b) any `K`-invariant bilinear pairing
   with the vev, (c) compression of the `U_q(gl₂)`-invariant `a·1 + b·Ř` by the vev — gives an
   energy depending on flavour only, hence split 0 by `total_eq_iff`. Expected for (c), vev in the
   `d` slot: `E = diag(a, a + b·q)` (u/d asymmetric, gap `b·q`), but type-blind.
4. **Charge selection rule (the one candidate that is NOT type-blind).** A bilinear pairing
   `Φ ⊗ V → 𝟙` invariant under the unbroken `U(1)_em` grading `q^{3Q}`, with the vev of charge 0,
   vanishes on every strand slot of nonzero charge. Its induced energy is supported on neutral
   slots only: an indicator `[Q_s = 0]`, which is not linear in the charge and so escapes #8676.
   With the Standard-Model charges (u 2/3, d −1/3, ν 0, e⁻ −1) and premise L, only `(ℓ,u) = ν` is
   neutral; expected split = `y_ν` (one free magnitude), positive (n⊗ν side carries it). This gives
   energy to ν, the OPPOSITE of the Standard Model, where the 3-point Yukawa vertex with a
   right-handed singlet makes e⁻ massive and ν massless. The strand model has no right-handed
   singlet, so the 3-point vertex is not available.
5. **General diagonal energy.** Per type `t`, energies `a_t` on the vev slot, `b_t` on the other:
   split = `(a_q − b_q) − (a_ℓ − b_ℓ)`. Four free parameters, one combination enters.

## What will NOT be done

* No Yukawa coupling, `y_ν`, `a_t`, `b_t` or energy scale is fitted, chosen or tuned to `Q_β`.
* If no magnitude is forced, no MeV number is produced. A dimensionless split under a stated
  normalisation (idempotent energy operator, eigenvalue 1) may be reported with its `q`-dependence
  and its value at the proton `q₀` (70 dps), with CODATA `Q_β` quoted for comparison only.
* No selection between the arms by how close a number lands.

## Readings kept labelled

* **L** (lepton = 4th doublet strand, ν in `T³ = +½`): the four-strand states of #8676 apply.
* **¬L** (lepton not a doublet strand): the strand-level split is undefined; only the object-level
  statement of arm 4 (the vev pairs with neutral objects only) survives.
