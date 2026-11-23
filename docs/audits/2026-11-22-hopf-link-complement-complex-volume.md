# The Hopf-link complement has zero complex volume (gate `qou-c9fh`)

Date: 2026-11-22. Thread "Work the volume conjecture beans" (wave-2 bean drain).
Lean: [`QOU/Archimedean/HopfLinkComplexVolume.lean`](../../folio/quantum-observable-universe/lean/QOU/Archimedean/HopfLinkComplexVolume.lean).

## The question

[`2026-08-07-two-row-projection-is-the-pairwise-cap.md`](2026-08-07-two-row-projection-is-the-pairwise-cap.md)
§4 set a gate: *"verify `CS` of the Hopf-link complement is nonzero and well-defined. The
complement is `T² × I`, a degenerate Seifert case, and `CS` may be `0` or only defined
modulo a period there. If `CS(Hopf) = 0`, this resolution dies immediately."*

## The answer: 0, for structural reasons

Let `M = S³ ∖ Hopf ≅ T² × (0,1)`. Then `π₁(M) = ℤ²`.

1. **Volume.** `M` is Seifert-fibred, so its simplicial volume is `0`, and
   `|Vol(ρ)| ≤ v₃·‖M‖ = 0` for every representation `ρ : π₁(M) → PSL₂(ℂ)`
   ([thurston1978] ch. 6, [gromov1982]).

2. **Complex volume of a boundary-parabolic representation.** If `ρ` sends a generator to a
   nontrivial unipotent `U_b = [[1,b],[0,1]]` (`b ≠ 0`), then everything in the image
   commutes with `U_b`, and a determinant-one matrix commuting with `U_b` is
   `±[[1,c],[0,1]]` (Lean: `commute_unipotent_iff`, `eq_pm_unipotent_of_commute`). So `ρ`
   factors through `±P`, `P` the unipotent subgroup. The complex volume `Vol + i·CS` of a
   decorated boundary-unipotent `ρ` is read off its fundamental class
   `[ρ] ∈ H₃(SL₂(ℂ), P)` and is independent of the decoration
   ([garoufalidis-thurston-zickert2011] §4.1, §6.1, §7). When `ρ` factors through `P`
   the class is the image of a class in `H₃(P, P) = 0`, so the complex volume is `0`.
   (The `±` is the usual `PSL₂` versus `SL₂` bookkeeping and does not change this.)

3. **Chern–Simons for any representation, product boundary trivialisation.** A flat
   connection on `T² × I` is gauge-equivalent to the pullback `π^*a` of a flat connection
   on `T²`, since holonomy determines it and `π₁(T² × I) = π₁(T²)`. Then
   `CS(π^*a) = π^*(cs(a))`, and at every point this is an alternating 3-form on the
   2-dimensional tangent space of `T²`, composed with `dπ`. Such a form is zero (Lean:
   `alternating_three_eq_zero_of_finrank_two`, `pullback_alternating_three_eq_zero`).

## Scope

**(b), structural.** The invariants are: the centraliser computation (proved), the vanishing
of alternating 3-forms in dimension 2 (proved), `H₃(P, P) = 0` with the functoriality of the
fundamental class (cited), and Gromov–Thurston (cited). The topological identification
`S³ ∖ Hopf ≅ T² × (0,1)` is standard and cited, not formalised.

A nonzero value can only come from choosing a boundary trivialisation other than the product
one, or a non-canonical normalisation of `CS` on a manifold with boundary. Either would be a
convention picked by hand, and picking it to reproduce a measured number would be a fit.

## Consequence

By the gate's own wording, the reading in which the deuteron is "carried entirely on the
`CS` axis" of some `F(Vol, CS)` is closed. This note says nothing about the deuteron's
binding energy or any other measured quantity: no physical number enters the argument or
the Lean file. The `Vol(𝓑₃)` substitution in `binding_link_volumes.py` stays as the
2026-08-07 audit left it (called unjustified there).
