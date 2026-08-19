# Can the octonions be recovered from the genus-4 Bring surface? — structural analysis

**Date:** 2026-07-12
**Branch:** `claude/meridian-exceptional-divisor-znxqcn`
**Question (owner):** QOU sits on Bring's genus-4 surface `Σ₄` with the bar
involution and `S₅ = Aut(Σ₄)` symmetry (three distinguished colour `S₃`
sub-sectors). Can the **octonions `𝕆`** be recovered from this data — the way
Szangolies' "Standard Model Symmetry and Qubit Entanglement" (`library/5s032x/5S032X.pdf`)
gets the SM gauge group from a preferred *imaginary* direction in `𝕆`?

**Verdict.** The *direct* route — an `S₅`-equivariant octonion structure on
`H¹(Σ₄) ≅ ℝ⁸` — is **excluded** (scope-(b), two independent invariants,
Lean-backed). But the **colour `SU(3) ⊂ G₂ = Aut(𝕆)`** piece — the
Günaydin–Gürsey "fix an imaginary unit → colour `SU(3)`" mechanism, the same
one Szangolies uses — **is** carried by QOU's three colour `S₃` sub-sectors.
Full `𝕆` is reachable only via the icosahedral `A₅ → E₈ → integral-octonion`
(McKay) route, which QOU already touches but has not built.

---

## The real hook

Genus `4` ⇒ `H¹(Σ₄; ℝ)` has dimension `2g = 8 = dim 𝕆`, and there is a bar
involution to play the role of octonion conjugation. The coincidence is genuine,
which is why the question is worth a rigorous answer rather than a dismissal.

## Task 1 — the direct `S₅`-equivariant octonion structure is excluded

Two independent invariants both kill it.

**Argument A — fixed-point (Lean-backed).** Any algebra automorphism of a unital
algebra fixes the identity `1`. So a group `G` acting on `𝕆` by algebra
automorphisms fixes `1 ≠ 0`; the real line `ℝ·1` is a trivial `G`-subrepresentation,
i.e. `𝕆` as a `G`-module **always contains a nonzero invariant**. But `Σ₄ / S₅ ≅ ℙ¹`
has genus `0` (Bring's curve is the `S₅`-Galois cover of the line cut by the first
three power sums in `ℙ⁴`), so there are **no `S₅`-invariant holomorphic
differentials**, hence `(H¹(Σ₄))^{S₅} = 0`. A module with no nonzero invariant
cannot be `𝕆` with `S₅` acting by automorphisms. Formalised sorry-free:
`QOU.BringsSurface.OctonionObstruction.no_fixed_unit`
([`OctonionInvariantObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/BringsSurface/OctonionInvariantObstruction.lean)),
generic (no associativity — so it applies to the non-associative `𝕆` — no `ℝ`; §7c).

**Argument B — dimension count (quotient-independent).** The imaginary octonions
`Im 𝕆` are `7`-dimensional and `G₂`-irreducible. For an `S₅`-equivariant octonion
structure, `Im 𝕆` would be a `7`-dimensional `S₅`-representation. But the
irreducible dimensions of `S₅` (partitions of 5) are exactly `{1, 4, 5, 6}` —
**there is no `7`**. So `Im 𝕆` cannot carry an irreducible `S₅` action; the octonion
symmetry must break `S₅`. Independent of Argument A's quotient claim.

Together: `H¹(Σ₄) ≇ 𝕆` as an `S₅`-module. This is a **scope-(b) structural
exclusion** (fixed-point / dimension invariants), not a failed numerical probe.

**The involution does not rescue it.** Octonion conjugation splits `𝕆 = ℝ·1 ⊕ Im 𝕆`
as `1 ⊕ 7`; the bar involution on `H¹(Σ₄)` (a genus-4 curve with no `S₅`-invariant
line) has no such fixed `1`-line to match, and `H¹` as an `S₅`-module is `4 ⊕ 4`
(two copies of a 4-dim irrep — the "`2W`" W-plane), not `1 ⊕ 7`.

## Task 2 — probe the colour `S₃` sub-sectors (Route B)

Per [`symmetric-quotient-colour.md`](../../content/quantum-observable-universe/braids-and-knots/symmetric-quotient-colour.md),
the three `S₃ ⊂ S₅` are the images of three `B₃ ↠ S₃` quotients, one per **colour
sector `𝔯, 𝔤, 𝔟`** — i.e. they encode **colour `SU(3)`**, *not* Spin(8) triality.
(An earlier chat framing called them "triality"; that was wrong — triality permutes
three distinct `8`-dim reps `8_v/8_s/8_c`, whereas genus-4 `H¹` supplies a single
`ℝ⁸`.)

Colour `SU(3)` **is** the octonion-relevant structure, and precisely via the
mechanism Szangolies uses (**Günaydin–Gürsey**, *Quark structure and octonions*,
J. Math. Phys. 14 (1973)):

* `G₂ = Aut(𝕆)` (dim 14); the stabiliser of a **preferred imaginary unit**
  (a "complex direction") is `SU(3) ⊂ G₂` (dim 8), with `G₂/SU(3) ≅ S⁶` (dim 6).
* Under this `SU(3)`, the imaginary octonions branch `7 = 1 ⊕ 3 ⊕ 3̄` — a
  colourless unit plus a colour **triplet** and **anti-triplet**. The three colours
  `𝔯, 𝔤, 𝔟` are exactly this `3`.

So QOU's colour `SU(3)` and the octonionic colour `SU(3) ⊂ G₂` are the **same
subgroup, via the same "fix an imaginary direction" step** as Szangolies. That is a
real, specific alignment — the octonionic *colour* structure is latent in QOU.

**But it is only the `SU(3)` piece, not the full product.** Recovering `𝕆` needs the
whole `G₂`/Fano structure; colour gives the `SU(3) ⊂ G₂` sub-part (the `1 ⊕ 3 ⊕ 3̄`
of the `7`), leaving the `6`-dim coset `G₂/SU(3) = S⁶` (the part where `3` and `3̄`
mix under the full `G₂` but not under `SU(3)`) unaccounted. Colour alone does not
close the octonion multiplication.

## Synthesis

| Target | Status from genus-4 QOU data |
|---|---|
| `S₅`-equivariant full `𝕆` on `H¹(Σ₄)` | **excluded** (Task 1, two invariants, Lean) |
| Colour `SU(3) ⊂ G₂ = Aut(𝕆)` | **present** (Task 2 — the three colour `S₃`'s = Günaydin–Gürsey octonion colour) |
| Full `𝕆` (the `G₂`/Fano product) | **open**; only via icosahedral `A₅ → E₈ → integral octonions` (McKay), or by extending colour `SU(3)` to `G₂` |

The natural *surface* home of the full octonion product is **genus 3** — the Klein
quartic, `Aut = PSL(2,7)` (order 168) = the Fano-plane / octonion-multiplication
symmetry, which *does* have a `7`-dim irrep. Genus-4 Bring (`S₅`, order 120) is the
**icosahedral / `A₅`** world; the `A₅ → E₈` McKay correspondence, with the E₈ lattice
= Coxeter's ring of integral (Cayley) octonions, is the route by which octonions
*are* reachable from QOU's icosahedral fingerprint
([`IcosahedralCharacterGoldenRatio`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/IcosahedralCharacterGoldenRatio.lean),
the golden-ratio degeneration) — at the **lattice** level, not as a product on `H¹`.

## Critical distance (standing red-team license)

- "8 dims + exceptional-looking symmetry ⇒ octonions" is textbook seductive-pattern
  territory. Getting an `8`-dim `S`-module is trivial; getting `𝕆` (verified:
  normed, alternative, `G₂` automorphisms, Fano product) is the whole content. The
  Task-1 obstruction is the **formalize-first invariant that prunes the direct route
  now** — no wide search needed; `S₅`-equivariant `𝕆` is dead on fixed-point +
  dimension grounds.
- **"Recovered" bar:** exhibit the bilinear product (via McKay/E₈, or by extending
  colour `SU(3)` to `G₂`) and *prove* it is `𝕆`. Colour `SU(3)` matching the
  Günaydin–Gürsey embedding is a genuine partial recovery (the colour piece); it is
  **not** the full algebra, and should not be reported as "octonions recovered."

## Recommended next steps (neither done here)

1. **McKay/E₈ route (safest, theorem-backed):** build `E₈` from the icosahedral
   `A₅` degeneration and identify the E₈ lattice with integral octonions. Recovers
   `𝕆` at the lattice level.
2. **Colour → `G₂` extension:** determine whether the `6`-dim coset `G₂/SU(3) = S⁶`
   (the missing `3 ⊕ 3̄` mixing) is realised anywhere in the genus-4 / Bring-cone
   data. If so, colour `SU(3)` promotes to full `G₂ = Aut(𝕆)`.

## Colour, and what octonion multiplication actually needs (the `ℂ → ℍ → 𝕆` ladder)

The colour triplet `ℂ³` on which `SU(3)` acts is built from a **single complex
structure**: fixing an imaginary unit `e` (`e² = -1`), left-multiplication `L_e`
is a complex structure (`L_e² = -1`) on the orthogonal `6`-space, making it `ℂ³`.
So — as the owner put it — "you just need complex multiplication." Precisely:

1. **`ℂ` (the colour atom):** one complex structure `j` (`j² = -1`) gives ordinary
   *commutative* complex multiplication `(a + bj)(c + dj) = (ac − bd) + (ad + bc)j`.
   Proved: `complex_mul_from_sqrt_neg_one` (any `CommRing`; §7c).
2. **`ℍ` (the "rotate across `i, j, k`" step):** two *anti-commuting* complex
   structures `i, j` produce `k = ij` with `k² = -1`. Proved: `rotate_ijk_sq` (any
   `Ring`) — and the proof **uses associativity**, which is exactly why this rung
   is `ℍ` (associative), electroweak `SU(2)`.

**Where the intuition stops.** `𝕆` is one more Cayley–Dickson doubling
`(a,b)(c,d) = (ac − d̄b, da + bc̄)`, and it is **non-associative** — the associator
`(x,y,z) := (xy)z − x(yz)` is nonzero. "Rotation" is associative reassociation
(`rotate_ijk_sq` literally re-brackets `i(ji)j = (ij)(ij)`), so it can *never*
produce a nonzero associator. It reaches `ℍ` (SU(2)), not `𝕆` (colour
`SU(3) ⊂ G₂`). **The missing ingredient for octonion multiplication is the
non-associative doubling itself — not a further rotation.** Colour `SU(3)` is the
subgroup of `G₂` that fixes the preferred imaginary unit; the `6`-dim coset
`G₂/SU(3) = S⁶` is precisely the freedom to *rotate which unit is preferred*, and
that motion is the non-associative part colour alone does not see.

(Mathlib has `Quaternion` but no octonions, so the `𝕆` rung is stated, not built;
the two associative rungs `ℂ, ℍ` are formalised sorry-free.)

## The categorical route: non-associativity as a pentagon (3-cocycle) deformation

The owner's framing — *"the non-associative doubling deforms the pentagon, like
deforming commutative to non-commutative; a categorical deformation"* — is exactly
right, and it names the mathematically-correct route to octonion multiplication.

A monoidal category has **two** independent coherence constraints; deforming each
is a different physics:

| deform | constraint | coherence law | deformation datum | algebraic home |
|---|---|---|---|---|
| commutative → non-commutative | braiding `c_{V,W}` | **hexagon** (Yang–Baxter) | R-matrix / quasitriangular `R` | quantum groups — **QOU's Hecke engine** |
| associative → **non-associative** | associator `α_{V,W,X}` | **pentagon** (Mac Lane) | 3-cocycle / Drinfeld associator `Φ` | **quasi-Hopf algebras** |

**The pentagon identity *is* the 3-cocycle condition.** A non-trivial but
pentagon-coherent associator is a class in `H³`. This is precisely the octonions:

- **Albuquerque & Majid, "Quasialgebra structure of the octonions," J. Algebra
  220 (1999) 188–224** ([arXiv:math/9802116](https://arxiv.org/abs/math/9802116);
  `albuquerque-majid1999`). The octonions are the **twisted group algebra**
  `𝕆 = ℝ_F[(ℤ/2)³]`: the group algebra of `(ℤ/2)³` (its `8` elements index the
  units `e₀,…,e₇`), made non-associative by a sign 2-cochain `F` that is **not a
  2-cocycle** (`dF ≠ 0`). Octonion non-associativity **is** the pentagon-cochain
  defect `dF`. (`dF` is cohomologically trivial as a 3-cochain — see the Cohomology
  note below; the nontrivial `H³` class Albuquerque–Majid identify is the *category*
  associator `ω` of `Vect_{(ℤ/2)³}^ω`, in which `𝕆` becomes associative.)
- **Drinfeld, "Quasi-Hopf algebras," Leningrad Math. J. 1 (1990) 1419–1457**
  (`drinfeld1985` in the corpus flags the 1985 quantum-groups note; this is the
  distinct 1989/90 quasi-Hopf paper). A quasi-Hopf algebra carries an associator
  `Φ ∈ H^{⊗3}` satisfying the **pentagon**; its representation category is monoidal
  with that `Φ`. This is the general "deform the associator" framework —
  the associativity-side twin of the quasitriangular `R` (which QOU already uses).
- **Majid, Foundations of Quantum Group Theory, CUP 1995** (`majid1995`, already
  cited) — cochain twists, monoidal categories, the `Vect_G^ω` (pointed) picture.
- Context: **Baez, "The Octonions," Bull. AMS 39 (2002) 145–205** (the `(ℤ/2)³`
  grading); **Etingof–Gelaki** on pointed fusion categories `Vect_G^ω`,
  `ω ∈ H³(G, k^×)` — the octonion category is `Vect_{(ℤ/2)³}^ω`.

**Where QOU already stands.** QOU carries pentagon structure —
`QOU.BraidsAndKnots.PachnerPentagonBorromean`,
`QOU.BraidKnot.QRogersPentagonArchimedean`,
`QOU.QuantumBloch.PentagonUvCommutation` — but as pentagon *coherence* (a trivial /
strict associator), **not** a deformed one. QOU deformed the **braiding** (hexagon
→ the Hecke/quantum-group engine); the octonions need deforming the **orthogonal**
constraint, the **associator** (pentagon → the `(ℤ/2)³` 3-cocycle). So the
categorical route to `𝕆` is: **put a `(ℤ/2)³` grading on QOU's substrate and turn
on the Albuquerque–Majid 3-cocycle associator.** This is the categorical
counterpart of the lattice `A₅ → E₈ → integral-octonion` (McKay) route above.

**Mechanism, formalised.** For any 2-cochain twist `e_a·e_b = F(a,b)·e_{a+b}`, the
associator `α = dF` **automatically satisfies the pentagon** because `d² = 0` —
this is why a graded twist breaks strict associativity while keeping coherence.
Proved sorry-free: `assoc_pentagon`
([`PentagonTwistAssociator.lean`](../../content/quantum-observable-universe/lean/QOU/BringsSurface/PentagonTwistAssociator.lean)),
generic additive grading + phase group (§7c).

**The concrete octonion cocycle, machine-verified.** The octonion multiplication
associator on `(ℤ/2)³` is the `𝔽₂` **determinant** (trilinear alternating form)
`φ(a,b,c) = det₂[a b c]` — the sign rule "`−` on `𝔽₂`-independent triples." This is
not a guess: building `𝕆` by Cayley–Dickson (`ℝ→ℂ→ℍ→𝕆`) and reading off the basis
signs, the index law is XOR (`(ℤ/2)³`) and the associativity defect equals `det₂`
**exactly as a cochain** (`168` of `512` triples non-associate). Sorry-free in
[`OctonionCocycle.lean`](../../content/quantum-observable-universe/lean/QOU/BringsSurface/OctonionCocycle.lean):
* `det3_is_3cocycle` — `φ` satisfies the pentagon, verified exhaustively over all
  `8⁴ = 4096` tuples (kernel `decide`, ~38 s). A genuine, pentagon-coherent group
  3-cocycle.
* `det3_nonzero` — the deformation fires: on `e₁, e₂, e₄`, `φ = 1 ≠ 0`
  (non-associativity).
* `det3_cyclic_invariant` — the associator is invariant under the coordinate
  3-cycle `cyc ∈ GL(3, 𝔽₂)`. This is the machine-checked generator of the
  general fact `det3(g·a, g·b, g·c) = det(g)·det3(a,b,c) = det3(a,b,c)` for
  **every** `g ∈ GL(3, 𝔽₂) ≅ PSL(2,7)` (order 168), since `det g = 1` over `𝔽₂`
  — the Fano-plane / Klein-quartic symmetry of the octonion product realised on
  the `(ℤ/2)³` sign structure (see Investigation 2 below).

**Cohomology — correcting an earlier over-claim in this audit.** An earlier draft
flagged "`[φ] ≠ 0` in `H³`" as a remaining gap. That was a **category error**,
caught by the Cayley–Dickson check: `φ` is a **coboundary** `φ = dF` (it equals the
coboundary of the octonion sign cochain, exactly), so `[φ] = 0` in
`H³((ℤ/2)³; ℤ/2)` — the multiplication associator is cohomologically **trivial**,
and there is *nothing to prove there*. Non-associativity is `φ ≠ 0` **as a cochain**
(`F` is not a 2-cocycle), not an `H³` phenomenon; the gauge `e_a ↦ λ_a e_a` changes
`F` by `dλ` and leaves `φ = dF` fixed, so `𝕆` is non-associative under *every*
rescaling despite `[φ] = 0`. (The nontrivial `H³` class of Albuquerque–Majid 1999
is the *category* associator `ω` making `𝕆` associative in `Vect_{(ℤ/2)³}^ω` — a
distinct object from the multiplication associator, not claimed here.)

## Investigations (while awaiting review) — is `𝕆` useful for the mass/binding formulas?

The user asked the natural follow-up: does the octonion structure supply
**additional symmetry** the mass and binding formulas can use? Two leads were
probed. One is a clean formal win; the other is an honest **scope-(a) negative**
(per AGENTS.md §"Before declaring refuted"). Neither wires to production.

### Investigation 1 — octonion signs vs the `Δ_λ` mixed-sign pattern (scope-(a) NEGATIVE)

**The lead.** The Track-A blocker (AGENTS.md §Δ_λ gate) needs a **mixed-sign**
per-partition weight `Δ_λ = sgn(w₀^{S_{λ'}})·dim` — `n=3`: `1+/2−`; `n=6`:
`6+/5−` — and the six closure ansätze all failed. The octonion associator `det3`
is *also* a sign structure (`(-1)^φ`, `168/512` triples negative). Could the
octonion/triality signs supply the missing chirality?

**Result: no — the index sets do not align, and there is no canonical map.**

- **`Δ_λ` is indexed by partitions `λ ⊢ n`** (Wedderburn blocks of `H_n(q)`);
  its sign is `sgn(w₀^{S_{λ'}})`, the longest-element sign of the *conjugate*
  Young subgroup. This is an `S_n`-representation-theoretic datum.
- **`det3`'s sign is indexed by ordered triples `(a,b,c) ∈ ((ℤ/2)³)³`** — the
  octonion *grading group*, not a partition set. Its sign is `𝔽₂`-linear
  dependence, an `GL(3,𝔽₂)`-datum.
- There is **no canonical bijection or functor** partitions `λ ⊢ n → (ℤ/2)³`
  triples: `|{λ ⊢ 3}| = 3`, `|{λ ⊢ 6}| = 11`, neither matches the `8` grading
  classes or the `168`-strong non-associating set; the symmetry groups (`S_n`
  vs `GL(3,𝔽₂) ≅ PSL(2,7)`) are unrelated for `n ≠ 7` (and even `S_7 ⊅ PSL(2,7)`
  as the relevant action). The `det3` chirality is `GL(3,𝔽₂)`-**invariant**
  (Investigation 2), whereas `Δ_λ` is *not* `S_n`-invariant — it transforms by
  `sgn` — so a symmetry-respecting map would have to trade an invariant for a
  sign-character, which cannot be canonical.

**Scope discipline.** This is a **scope-(a)** negative: the octonion sign
structure, *as-is, alone*, does not supply the `Δ_λ` chirality — the index sets
are misaligned and no canonical map exists. It is **not** a scope-(b) structural
exclusion: no proved invariant forbids *some* future construction that routes
octonion signs through an `S_n`-equivariant intermediary (e.g. via the `n=6`
Bring `S₅ ↪ S₆` triality, which *is* an exceptional coincidence). That would be
a genuinely different object; this probe only measures that the naive
identification fails. Recorded so a later agent does not re-run the naive map.

### Investigation 2 — colour `SU(3)` and the Fano / `PSL(2,7)` symmetry (formal win + honest gap)

**What is established.** The colour `SU(3) ⊂ G₂ = Aut(𝕆)` (Günaydin–Gürsey:
`7 = 1 ⊕ 3 ⊕ 3̄` under `SU(3)`) is present on the genus-4 substrate via the three
colour `S₃` subgroups of `Aut(Σ₄) = S₅` (§ colour section above). The **discrete
skeleton** of the full `G₂` symmetry is now machine-checked: `det3` — the
octonion associator — is invariant under `GL(3,𝔽₂) ≅ PSL(2,7)` (order 168, the
Fano-plane / Klein-quartic automorphism group), with the `cyc` 3-cycle generator
proved in `det3_cyclic_invariant` and the general statement following from
`det(g) = 1` over `𝔽₂`. `PSL(2,7)` is exactly the automorphism group of the Fano
plane that indexes the octonion multiplication table, so this is the honest
discrete tie between QOU's `(ℤ/2)³` sign structure and the octonion product.

**The remaining gap (honest).** The step from colour-`SU(3)` to the **full,
continuous** `G₂` needs the `6`-dimensional coset `S⁶ = G₂/SU(3)` — the extra
real-octonion generators beyond the `SU(3)` sub-block. Formalising that requires
a **real-octonion / `G₂` Lie-group** infrastructure that Mathlib does **not**
currently provide (no `Octonion`, no `G₂` as a Lie group; only the abstract
`CayleyDickson`/`QuaternionAlgebra` at the algebra level, without the compact
exceptional-group facts). So the continuous `G₂` step is **not formalisable
today** without building that infra from scratch — out of scope for this
analysis. What is proved is the discrete `PSL(2,7)` symmetry of the sign cocycle;
the continuous completion is flagged as a Mathlib-gap, not claimed.

**Net answer to the user's question.** Octonions supply a *real additional
symmetry* — the colour `SU(3) ⊂ G₂`, with its discrete `PSL(2,7)` skeleton now
machine-checked — which is genuinely relevant to the **colour** sector. They do
**not** (Investigation 1) supply the `Δ_λ` binding chirality by any naive map.
So the honest use is: **octonions organise colour, not binding signs.** Any
mass/binding payoff would route through the colour `SU(3)` representation content
(`3 ⊕ 3̄`), not through the octonion sign structure directly — and that route is
already partly present in QOU via the three colour `S₃`'s, without needing the
non-associative product.

## Formalisation

- [`OctonionInvariantObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/BringsSurface/OctonionInvariantObstruction.lean)
  — `no_fixed_unit` (the Task-1 obstruction kernel) + `exists_nonzero_invariant`
  (associative-case illustration). Sorry-free, generic (§7c).
- [`ColourComplexStructure.lean`](../../content/quantum-observable-universe/lean/QOU/BringsSurface/ColourComplexStructure.lean)
  — `complex_mul_from_sqrt_neg_one` (colour atom, `ℂ`) + `rotate_ijk_sq` (the
  `i, j, k` rotation, `ℍ`, proof uses associativity). Sorry-free, generic (§7c).
- [`PentagonTwistAssociator.lean`](../../content/quantum-observable-universe/lean/QOU/BringsSurface/PentagonTwistAssociator.lean)
  — `assoc_pentagon`: the twist associator `dF` satisfies the pentagon (`d²=0`),
  the mechanism of the categorical route. Sorry-free, generic (§7c).
- [`OctonionCocycle.lean`](../../content/quantum-observable-universe/lean/QOU/BringsSurface/OctonionCocycle.lean)
  — the concrete octonion associator `det3` on `(ℤ/2)³`: `det3_is_3cocycle`
  (pentagon-coherent, `decide` over `8⁴`) + `det3_nonzero` (non-associativity
  fires) + `det3_cyclic_invariant` (the `PSL(2,7)`/Fano symmetry witness,
  Investigation 2). Sorry-free.

### The `𝔤₂ = Der(𝕆)` dimension, now machine-verified

The `G₂ = Aut(𝕆)` claim invoked throughout (Task 2, Investigation 2, Synthesis)
is now rigorously grounded in the corpus at the Lie-algebra level:

- [`OctonionDerivations.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/OctonionDerivations.lean),
  [`OctonionDerivationsBound.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/OctonionDerivationsBound.lean),
  [`OctonionDerivationsUpperBound.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/OctonionDerivationsUpperBound.lean)
  — `octonion_derivation_dim : dim Der(𝕆) = 14`, fully sorry-free (PRs #3717, #3734).
  Since `Der(𝕆) = Lie(Aut(𝕆))`, this is the infinitesimal `dim Aut(𝕆) = dim G₂ = 14`
  underpinning the `G₂` invocations above — no longer only cited-external.
- [`OctonionDerivationProperties.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/OctonionDerivationProperties.lean)
  — `derivation_annihilates_one : D ∈ Der𝕆 → D 1 = 0`, the **infinitesimal shadow of
  `no_fixed_unit`** (Task-1 Argument A): differentiating `φ_t(1) = 1` gives `D 1 = 0`.
  So every derivation preserves the splitting `𝕆 = ℝ·1 ⊕ Im 𝕆`, acting (as the
  14-dimensional `𝔤₂`) on the 7-dimensional `Im 𝕆` where `G₂` is irreducible — the
  exact `1 ⊕ 7` structure Argument B / the involution discussion turn on. Sorry-free.
