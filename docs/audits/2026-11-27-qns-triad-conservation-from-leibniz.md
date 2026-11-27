# q-NS triad energy conservation, derived from the Leibniz rule

Date: 2026-11-27. Bean `qou-q3dc`. Owner route: "q-Clebsch–Gordan coefficients"
(card, taken as the recommended option).

Lean: `folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_triad_derivation.lean`.
The file is sorry-free and passes `lean -DautoImplicit=false -s 65536` with exit 0.
`#print axioms` reports only `propext, Classical.choice, Quot.sound`.

## What changed

PR #9537 assumed the triad-wise energy conservation `TriadCoeff.conserve`. It is
now a theorem for the advection term of the q-NS system:

| Lean | Statement |
|---|---|
| `transport_skew` | `τ(u · X u) = 0` for a derivation `X` with `τ ∘ X = 0` (Leibniz: `X(u²) = 2u Xu`) |
| `transport_skew_pair` | `τ(f · X g) + τ(g · X f) = 0` |
| `qField` | The corpus field `q⁻¹∇ + (1 − q⁻¹)(ι_ξ∇)Θ` is a derivation by construction |
| `qField_div_free` | It is divergence-free when both of its parts are |
| `modalD_skew` | The modal couplings `Dₙₚᵣ = τ(eₙ Xₚ eᵣ)/τ(eₙ²)` satisfy `wₙDₙₚᵣ + wᵣDᵣₚₙ = 0` |
| `ofTransportSkew`, `advectionTriad` | Symmetrising pairwise skewness gives the cyclic Kraichnan identity, so the advection's couplings form a `TriadCoeff` |
| `parseval` | `τ(u²) = ∑ wₙ aₙ²` for `τ`-orthogonal modes |
| `transfer_eq_advection` | The Galerkin transfer equals the `n`-th modal coordinate of `X_v u` |
| `skew_of_diag` | A modal bilinear form that vanishes on the diagonal is skew |

## Hypotheses that remain

- **Selection rule `hsel`.** The couplings vanish off the fusion rule. This is
  the generic-`q` Clebsch–Gordan rule for `SU_q(2)`. It is not derived here.
- **Incompressibility `hdiv`.** This is the corpus constraint `δ_q v = 0`,
  applied to each transport mode.
- **Commutative algebra with a trace.** This covers the archimedean
  realisation. It does not cover the noncommutative `O_q(SU(2))` picture.
  There, by a standard fact not used in any proof here, the Haar state is not
  a trace: it is twisted by a modular automorphism. So the step
  `τ(X(u²)) = 2τ(u Xu)` can fail, and energy conservation would need a twisted
  Leibniz rule. Whether it holds in that picture is open.
- **The numerical coupling values** (`q`-Clebsch–Gordan or `6j` coefficients).
  These are not computed.

## Part A

Part A remains open. The triad model is now tied to the corpus nonlinearity
everywhere except the four points above. Part A over `advectionTriad` is
therefore a genuine conjecture about the infinite-mode system (bean `qou-q3dc`).

## Follow-up, same day: the noncommutative case

Owner route, next step "twisted Leibniz on `O_q(SU(2))`" (card, recommended
option taken). Lean:
`folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_triad_noncomm.lean`
(sorry-free, `lean -DautoImplicit=false -s 65536` exit 0, axioms
`propext, Classical.choice, Quot.sound`).

**Finding: the commutative-trace hypothesis was not needed.** For any linear
functional `φ` on a noncommutative algebra, and any linear `X` with the
untwisted Leibniz rule and `φ ∘ X = 0`:

- `φ(u·Xu) + φ(Xu·u) = φ(X(u²)) = 0`, so `φ(u²)` is conserved along `u̇ = Xu`
  (`transport_skew_nc`);
- the energy only sees the symmetrised form `B(f,g) = (φ(fg) + φ(gf))/2`, and
  `X` is `B`-skew (`symForm_skew`);
- couplings taken against `B` give a conserving `TriadCoeff`
  (`advectionTriadNc`), Parseval holds for `B`-orthogonal modes (`parsevalNc`),
  and the transfer is the advection (`transfer_eq_advection_nc`).

The Haar state's modular twist `h(ab) = h(bσ(a))` therefore does not obstruct
energy conservation. It only makes `φ` non-symmetric, and the energy ignores
the antisymmetric part. For self-adjoint `u`, `h(u*u) = h(u²)`.

**Non-vacuity on a non-tracial state.** If `φ(ab) = φ(bσ(a))` and `σc = c`,
the inner derivation `f ↦ cf − fc` satisfies both hypotheses
(`innerDer_div_free_of_kms`). On `O_q(SU(2))` the modular automorphism
`nuAlgEquiv` fixes `αδ`, `δα` and `βγ` (`nuAlgEquiv_fixes_cartan`).

**The gap moves.** It is no longer traciality. It is whether the q-NS
transport `∇_q` acts on `O_q(SU(2))` as an *untwisted* derivation. The
quantum-group derivations are usually twisted, `X(fg) = Xf·g + σ'(f)·Xg`, and
then `φ(X(u²)) = φ(Xu·u) + φ(σ'(u)·Xu)` is not a symmetric combination. Not
established here.
