# Observer intent, outer automorphisms, non-CA intents, test particles

Date: 2026-11-27. Branch `claude/observer-intent-out-2026-11-27`.
Source: owner AI-chat discussion 2026-11-25..27 (lines 956–1179 of the project's
`owner-discussion-2026-11-25-to-27.md`), which is **unverified chat text**. This audit
checks each claim and formalises what is honest.

Lean added (both sorry-free, `lean`-direct exit 0, `#print axioms` shows no `sorryAx`):

- `QOU/Core/HeckeGoldmanIwahori.lean` — presented `H_n(R,q)` and the involution θ.
- `QOU/Core/IntentHolonomy.lean` — gauge and flux intents on closed-walk holonomy.

The photon throughout is `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` (owner ruling 2026-11-20).

## Verdict summary

| # | Claim in the discussion | Verdict | Evidence |
|---|---|---|---|
| 1a | At a character of a semisimple Hecke fibre, `𝔪/𝔪² = 0`, so `def:observation`'s `A/𝔪_p²` jet is empty | **Correct**, already proved | `PhotonJet.sub_eq_smul_sq` (σ − q ∈ I² when [2]_q ≠ 0) |
| 1b | The sign `ε ∈ {±1}` is too coarse; intent should be a direction in `W₁ = span{σ₀, σ₁, σ₀σ₁⁻¹}` | **Correct as critique**; proposal below | `observation.md` carries only ε |
| 1c | `[q₁′(p), q₂′(p)]` of scalars is 0; must be operator valued | **Correct**; already handled by `ObservationParallelogram` over a noncommutative `R`, which with `R = H_n` and `δqᵢ = wᵢ` gives `F_q = [w₁, w₂]` exactly | `germ-commutator-q-curvature.lean` |
| 1c′ | Use `exp(w)` in the h-adic completion | **Needs repair**: `exp(w)` converges h-adically only for `w ∈ h·H_n[[h]]` and needs `ℚ ⊆ R`. For `w ∈ W₁` itself it does not converge | standard |
| 1d | Trace preservation is automatic for `[w₁, w₂]` | **Half right.** Any trace kills a *Lie* commutator, and conjugation `ψ ↦ e^w ψ e^{−w}` preserves every trace. The *group* commutator `e^{w₁}e^{w₂}e^{−w₁}e^{−w₂}` is not traceless, and the open-probe action `ψ ↦ e^w ψ` does not preserve the trace | algebra |
| 1e | `𝔤₅ = [W₁,W₁] + W₁` is the "5-dim traceless Lie algebra" in `H₃` | **Wrong.** `H₃ ≅ K ⊕ K ⊕ M₂(K)` (dim 6, centre dim 3), so `[H₃, H₃] = 𝔰𝔩₂` has dim **3**. The kernel of one trace is 5-dim but is not the commutator space | Wedderburn |
| 2a | θ(σᵢ) = −σᵢ⁻¹ is an automorphism of `H_n(R,q)` | **Proved**, generic `CommRing R`, `q·q′ = 1`, every n | `GoldmanIwahori.theta`, `theta_theta` |
| 2b | θ is not inner (moves ε₊ = q to −q⁻¹) | **Proved** for n ≥ 2, `q + q⁻¹ ≠ 0` | `theta_not_inner`, `trivialChar_theta_gen` |
| 2c | θ does not preserve `tr_D` for n ≥ 3 | **Stronger than stated**: fails already at n = 2. A trace with `t σ = z` is θ-invariant at σ iff `2z = h`; at `z = q³/(q²+1)` this forces `q⁴ = −1` | `trace_theta_invariant_iff`, `convD_theta_forces` |
| 2d | GNVW index of the strand shift on `TL_∞` is `δ = q + q⁻¹` | **Not established; misattributed.** The fusion-chain index is Jones–Lim (Corey Jones, Junhwi Lim, arXiv:2309.10961), not "Jones–Corey–lim". It needs a *unitary fusion category* (finitely many simples). At generic real `q₀ ≈ 1.11`, `Rep U_q(𝔰𝔩₂)` is not fusion, so the theorem does not apply. Their Prop 4.1 gives `Ind(shift) = dim X` for the one-site shift of the *fusion spin chain* (local operator algebra), which is a different object from `σᵢ ↦ σᵢ₊₁` on `H_∞`. Plausible analogy, not a theorem here | paper read 2026-11-27 |
| 2e | `Pic(B∖pt)[2] ≅ (ℤ/2)⁸`, Rosenberg–Zelinsky + Steinitz gives 255 trace-preserving outer classes of `TL₃(𝒪(U)) ≅ 𝒪(U) ⊕ M₂(𝒪(U))` | **Correct as algebra over ℂ** (`Pic(B∖pt) ≅ J(B)`, `J[2] = (ℤ/2)^{2g}`; Steinitz `L⊕L ≅ 𝒪⊕L²`; `Out(M₂(R)) ≅ Pic(R)[2]`; automorphisms of an Azumaya algebra preserve the reduced trace). **But** it uses the *algebraic curve* `B` and its ring of functions, which QOU does not otherwise use as an observable base; over `ℚ` the rational 2-torsion is smaller. Not formalised (Mathlib lacks Rosenberg–Zelinsky) | literature |
| 2f | Cellular version on Bring's `{5,4}` complex: locally inner / globally inner ↠ `H¹(T, R^×)`, giving 255 classes | **False for the constant sheaf.** For a constant sheaf of algebras on a connected complex, a global section of `Inn` is one inner automorphism, so the quotient is trivial; equivalently `H¹(T,Z^×) → H¹(T,A^×) = Hom(π₁, A^×)/conj` is injective on central characters, so `δ` has trivial image. The honest cellular statement is about **flat connections**, not algebra automorphisms: flux intents `U ↦ z^ω U` modulo gauge intents are classified by the class of ω (`flux_coboundary_is_gauge`, `flux_not_gauge`); with `z = −1`, `b₁ = 8` gives `2⁸ − 1 = 255` non-gauge classes, provided a class function separates `W` from `−W` (e.g. a trace with `tr W ≠ 0`, char ≠ 2) | Lean + argument |
| 2g | "Non-trivial trace-preserving outer automorphisms ⇔ `H¹ ≠ 0`" | **Not an equivalence.** Counterexample over a point: `K × K` with `t(a,b) = (a+b)/2` and the swap. True only in the scoped form: for `TL_n(K)` with `tr_D` at generic q, Skolem–Noether gives trivial trace-preserving `Out` when no two blocks of equal size have equal trace weight (at n = 6 two blocks have size 5, but their `tr_D` weights differ generically) | counterexample |
| 3 | Flux-threading intent `Φ_{ω,z}` is not a CA of radius < half-systole at any confinement level | **Overclaimed.** The Lean shows the flux intent is not a *gauge* intent (any radius, local or global). Locality plays no role. A one-edge flux (radius 0) also changes the systole holonomy, so "changes a holonomy" does not certify "not a CA". A correct theorem needs the CA class restricted to curvature-preserving gates (`dω = 0` on every face); stated as an open target | `IntentHolonomy.lean` header |
| 4 | Test-particle references | see table below | |

Related open work: PR #9428 (`NonabelianStokesTrace.lean`) proves the same telescoping
`gaugeHol_eq` for path-indexed labels; `IntentHolonomy` adds the flux side and the
coboundary lemma. Its probe measured `dim ker Δ₁ = 8` and vertex-graph systole 6 on Bring,
which is what item 2f/3 needs for "255".

## Proposed `def:intent` (prose change NOT applied; owner decides)

Current `def:observation` (`quantum-observable-universes/observation.md`) makes an
observation a pair `(𝔒, ε)` with `𝔒` a section of `Ad(J¹𝒮)`. Proposal:

> **Intent.** Let `R` be a commutative ring containing `ℚ`, `H_n = H_n(R[[h]], q)` with
> `h = q − q⁻¹`, and `W₁ = span{σ₀, σ₁, σ₀σ₁⁻¹}`. An *intent* at a locus `p` is a pair
> `(w_p, δq_p)` with `w_p ∈ h·W₁[[h]]` (the probe direction) and `δq_p ∈ R` (the
> substrate deformation). It acts on closed states by `ψ ↦ e^{w_p} ψ e^{−w_p}`, which
> preserves every trace. Two intents at `p` have discrepancy
> `[w₁, w₂] + O(h³)`, the q-curvature of `rem:two-observer-parallelogram`.
> When `R ⊆ ℝ`, measurement intents have `δq_p ≥ 0`, and `ħ_q = 1 − q⁻¹` is monotone in q.

What changes: ε is replaced by a direction; the 1-jet `A/𝔪²` (zero at a character) is
replaced by the h-adic first-order space; the parallelogram identity is the existing
Lean instantiated at `R = H_n`. What is **not** included, by the no-empirics rule: the
DEC viscosity `ν_q`, "locks into one of 8 attractors", Landauer erasure, and Turing
machines. Those are physical readings, not theorems.

## Test particles (discussion lines 1156–1179)

| Reference | Real? | What it buys QOU | Action |
|---|---|---|---|
| Souriau, *Structure des systèmes dynamiques* (1970); evolution space, leaves of `ker dθ`; Mathisson–Papapetrou–Dixon | Real, standard | A clean statement: given a presymplectic form `ω = dθ`, trajectories are the characteristic leaves of `ker ω`. Useful only if QOU's contact form on the Reeb bundle is made presymplectic on an evolution space. No algebraic leverage on `H_n` | Cite if a test-particle section is written; do not ingest now |
| Majid & Simão, *Quantum Jet Bundles*, arXiv:2202.03067 (v4 2023; Lett. Math. Phys. 2023) | Real. Verified: order ≥ 3 jets need a torsion-free, **flat** connection whose generalised braiding obeys the **braid relations** (Lemma 3.5, Thm 3.6); example `ℂ(S₃)` with 3-dim `Ω¹` | The best match: an independent source for "higher jets force braid relations" and for a 3-dim first-order space over `S₃` (cf. dim `W₁` = 3). Caveat: their jets are bimodules over a base algebra, and they need flatness, while QOU's intents produce curvature | **Ingest** into `library/` (recommended) |
| Caianiello, maximal acceleration (1980s) | Real, but physics with an empirical bound `A_max = 2mc³/ħ` | Nothing for the formal side; an empirical prediction, excluded from proofs | Skip |
| Nonlinear Ehresmann connections on `TM` | Real, standard | Generic; adds no algebraic content | Skip |

## Open targets (not claimed)

1. A non-CA theorem with the CA class defined as curvature-preserving local gates.
2. The fusion-chain index at a root of unity where `Rep U_q(𝔰𝔩₂)` truncates to a fusion
   category, if the GNVW route is wanted.
3. `QOU/Core/Intent.lean` is not imported by `QOU.lean`, so a default build skips it.
