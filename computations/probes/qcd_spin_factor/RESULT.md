# RESULT: a spin factor separate from colour (beans `qou-ni4b`, `qou-bwwr`; issue #9058)

Pre-registration `PREREGISTRATION-spin-factor.md` (commit `2abaa8ed425`, pushed before any code).
Probe `qcd_spin_factor_probe.py` and its output `qcd_spin_factor_probe.out.json` (commit `c3f1b05557a`).
**34/37 checks pass.** 5 of them are post-hoc and are labelled `posthoc` in the JSON. The 3 FAILs
are the P1 prediction exactly as it was worded (below). All arithmetic is exact: sympy over
ℚ(p, r, q), `Fraction`, and integer Laurent polynomials. No float64 is used, and q₀ is not used at all.

Each strand carries W = C^N_colour ⊗ C²_spin. Colour is the Jimbo U_p(gl_N) and spin is the Jimbo
U_r(gl₂); p = 1 and r = 1 are the classical swaps. At generic p and r, the four products
Π^c_a ⊗ Π^s_b span the commutant on W⊗W, so P1 enumerates **every** strand-wise colour-and-spin
symmetric Hecke braiding.

## P1: spin as the extra factor. The obstruction persists.

All 16 assignments λ_ab ∈ {q, −q⁻¹} were computed. Each was checked at (p, r) ∈ {(1,1), (1,r), (p,1),
(p,r)} and at N = 2, 3, 4. The method is seminormal H₃ irreps followed by a lex Gröbner basis
with p > r > q. It was cross-checked against the explicit 216-dimensional operator at three
rational points.

| member class | braids for real q > 1? | Gröbner / tie result (N = 3; N = 4 identical) |
|---|---|---|
| transported (Ř → ±P_c⊗P_s), 2 members | **no, at any p, r** | elimination ideal ∩ ℚ[q] ∋ q²(q²−1)²(q²+1)³(q⁴+q²+1), so q ∈ {±1, ±i, primitive 3rd/6th roots}. With p = r = 1 it is (q²−1)²(q²+1). |
| colour-fixed, Ř = 1_c ⊗ Ř_s (K0-type) | yes | needs r = ±q^{±1}: (q²−r²)(q²+1)(q²r²−1) |
| spin-fixed, Ř = Ř_c ⊗ 1_s | yes | needs p = ±q^{±1} |
| scalar ±q^{±1}·1 | yes, trivially | 0 |
| mixed (one of the four λ differs), 12 members | **no real solution in the tie set** | the components with q generic need p² ± p + 1 = 0, i.e. [3]_{±p} = 0, a non-semisimple root-of-unity colour parameter. At N = 2 there is also a tie [2]_q = [2]_p[2]_r (Temperley–Lieb on singlet ⊗ singlet). |

**Claim (scope b inside the enumerated class).** A Hecke braiding on C^N ⊗ C² that commutes
strand-wise with U_p(gl_N) ⊗ U_r(gl₂) and carries colour and spin together (q → 1 limit ±P)
exists only at q ∈ {±1, ±i, ζ₃, ζ₆}. The invariant is the elimination ideal above. In particular
it does not exist at any real q > 1. Spin does not rescue the sibling K4 result. This was expected,
because spin C² is the same algebra as the nucleon flavour C² of `qcd_colour_action`.

**The three FAILs.** The pre-registration predicted that every member braiding at generic q is
colour-fixed, spin-fixed or scalar. That is false as worded once p and r are left free: the mixed
members at p a primitive 3rd or 6th root of unity, and the N = 2 tie, both braid at generic q. A
post-hoc refinement passes. It ties (p, r) to q within {±1, ±q, ±q⁻¹}, and there the transported
and mixed members braid for no tie. A post-hoc correction of a second kind: the first run used
Gröbner order (q, p, r), which could not separate the q-generic components. Its "generic" column
was wrong, and the code now records this.

## P2: a spin-only twist, derived (and what it costs)

On C²_spin ⊗ C²_isospin, all three of the following satisfy the braid relation (n = 3, exact):

| | per-strand braiding | Hecke? | full twist Δ²_n (n = 3, 4) | deuteron − singlet factor s·i′ − s′·i |
|---|---|---|---|---|
| D | Ř_s(q) ⊗ P_I (Deligne; isospin classical and transported) | **no**: (T²−q²)(T²−q⁻²) = 0 | **Δ²_s ⊗ 1_I** | q¹⁰ − q⁶ = q⁶(q²−1)(q²+1) |
| F | Ř_s(q) ⊗ 1_I (K0-type; isospin at fixed position) | yes | **Δ²_s ⊗ 1_I** | q¹⁰ − q⁶ |
| Y | Ř_s(q) ⊗ Ř_I(q) (one braided category) | no | Δ²_s ⊗ Δ²_I | 0 (`symmetric_twist_no_split`) |

Δ²_s acts on a two-row shape λ as q^{2c(λ)}. This was checked by the minimal polynomial and by
weight-space traces for n = 2..6. It agrees with the Lean `contentSum_four_two` = 5 and
`contentSum_three_three` = 3. The full twist is θ², not the Keystone θ, so the split is
q¹⁰ − q⁶ and not the Lean `six_strand_spin_twist_split`'s q⁵ − q³.

**What is established.** `θ_I = 1` (the open hypothesis of `TwistedChannelSplitting`) is
**derived, not assumed**, in two constructions. In D the classical full twist is the identity
permutation. In F the isospin is not braided at all. Each carries a price:
- D is not Hecke on the combined strand (four eigenvalues ±q^{±1}).
- In F the isospin does not move with the strand.

By P1, a Hecke braiding that transports both factors does not exist at real q > 1. So a
derived spin-only twist and a combined strand that is both transported and Hecke do not occur
together in the searched class.

**Pre-declared side result.** Take the q-trace on the spin factor and the ordinary trace on a
classical isospin factor. The *untwisted* isotypic traces are Tr(K P_λ) = f^λ[2S+1]_q and
Tr P_λ = f^λ(2S+1). They already split the channels:
deuteron − singlet = **45 (q − q⁻¹)²**. So the classical-isospin route also breaks the
equal-trace premise of the Pauli lock (`qou-7zob`). This is reported, not proposed as a mechanism.

## P3: no (2s)² − 1/3 split. MISS (scope a)

(i) **Covariance (exact, N = 3, W⊗W).**
- The colour-charge background a⊗1 and the Zeeman background 1⊗σ_z commute with every member.
- The chromomagnetic background a⊗σ_z (colour charge × 2s_z, the Nielsen–Hughes spin coupling)
  commutes only with λ_SS = λ_AA, λ_SA = λ_AS (Ř ∈ span{1, P_c⊗P_s}) at p = r = 1.
- At generic p or r it commutes only with scalars. The pre-registered wording "nothing" was
  imprecise, because the identity always commutes. The check was reworded to "only scalars",
  and that version passes.
- Combined with P1: **no non-scalar Hecke braiding in the class is chromomagnetically covariant
  at real q > 1.** The coupling that produces the paramagnetic term needs colour and spin to be
  transported together, and only q = 1 allows that.

(ii) **Susceptibilities at q = 1, N = 2, 3, 4, all S_n channels for n ≤ 3.**
- The answer does not depend on the Cartan direction.
- For n = 1, κ = 0.
- **No channel has an N-independent κ.** The acceptance clauses (2) and STRONG both fail as
  predicted.
- Post-hoc: in every channel χ_chromo = χ_charge = χ_Zeeman, so κ = 1 − χ_Zeeman is only a
  Zeeman average and not a separate diamagnetic piece. The pre-registered κ diagnostic carries
  no information beyond χ_Zeeman.
- For n = 2: κ(Sym²W) = −(2N+3)/(2N+1) and κ(Λ²W) = −(2N−3)/(2N−1).

**Post-hoc coincidence, not a hit.** κ(Λ²W) = −1/3 at N = 2 only. It is −3/5 at N = 3 and −5/7
at N = 4, so it is N-dependent. This joins 2/N and 1 − 1/N in the list of traps.

## Implications

1. The spin factor gives what `TwistedChannelSplitting` lacked: `θ_I = 1` follows from the
   isospin being classical (D) or unbraided (F). The deuteron–singlet split is then
   q⁶(q²−1)(q²+1) per unit block trace, and it vanishes at q² = 1.
2. In every case the factor that carries the twist is the one that is *not* transported with
   colour, or the combined strand is not Hecke. In the enumerated class, "spin moves with colour",
   "Hecke at real q > 1" and "chromomagnetic coupling" cannot hold together.
3. Nothing here produces the Nielsen–Hughes −1/3. Its usual origin, the Landau-ladder
   Euler–Maclaurin term (4·B₂(½) = −1/3), needs an orbital factor that a finite strand algebra
   does not have. That is an expectation stated in the pre-registration, **not** a proved exclusion.

## Not established / not formalised

- Spin braidings outside the U_r(gl₂)-commutant, super (gl(m|n)) gradings, coideal or twisted
  symmetries, and n > 3.
- Whether the derived twist of D or F is the framework's spin twist. That is a modelling decision.
- The full-tower (all n) version.
- No Lean. The identities that arose were either `ring`-level (45([3]_q − 3) = 45(q−q⁻¹)²,
  (a⊗b)² = a²⊗1 when b² = 1) or 216-dimensional Gröbner results that have not been reduced to a
  small statement. Neither met the bar for a genuinely proved identity.
- No gluon is identified or selected. Step 4 of def:derived-atom stays open.
- `scripts/precision-gates.sh --changed`: the RED lines are the pre-existing dirty audit witnesses
  in the worktree, which were not touched or committed. This probe writes no witness.
