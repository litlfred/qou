# `W` is not a second axiom — self-duality is a degree-2 accident, and the five avenues measured

**Date:** 2026-09-04 · **Branch:** `claude/w-derived-from-axioms-2026-09-04`
**Bean:** `qou-j3w6` (the condition-5 decision) · epic `qou-8lxd`
**Lean:** [`QOU/QuantumObservableUniverse/VolumeFormDegree.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/VolumeFormDegree.lean) — 11 declarations, `lean`-direct exit 0, `#print axioms` at most `[propext, Quot.sound]`, no `sorryAx`, no `Classical.choice`

---

## 0. The correction that starts this

The 2026-09-03 decision frame
([`2026-09-03-eightfold-axiom-5-decision-frame.md`](2026-09-03-eightfold-axiom-5-decision-frame.md))
posed option A as *"add a second fundamental object `W`"* and priced it as an
**axiom datum** — flavour `SU(3)` postulated rather than derived. The owner's
objection is correct and it changes the frame:

> `V` was not within an axiom but derived from axioms. Need something similar
> for `W`.

Read [`def:fundamental-object`](../../content/quantum-observable-universe/quantum-universes/fundamental-object.md):

> A **fundamental object** is an object `V ∈ 𝐂` equipped with a volume form
> `ε : V ⊗ V → 𝟙` — the categorical determinant `Λ²V → 𝟙` — together with an
> adjoint coform `η : 𝟙 → V ⊗ V` satisfying the two snake identities. … Under a
> fibre functor **the volume constraint forces `rank(V) = 2`**.

Rank two is the *conclusion*. The input is a volume form. So the honest
question is not "may we postulate `W`?" but **"what does the same input give at
a different degree, and does anything in the axioms supply that degree?"**

## 1. What is now proved: the degree dichotomy

`VolumeFormDegree.lean` works with a volume form of unspecified degree `N` and
proves the bookkeeping unconditionally (integer combinatorics; no ring, no `ℝ`,
§7c-clean). The workhorse is `choose_eq_one_iff : n.choose k = 1 ↔ k = 0 ∨ k = n`,
which Mathlib lacks — it has `choose_eq_zero_iff` and no `= 1` companion — proved
here from the absorption identity `(m+1)·C(m,j) = C(m+1,j+1)·(j+1)`.

| degree `N` of `Λ^N W ≅ 𝟙` | forced rank | complementary power `≅ W^∨` | duality |
|---|---|---|---|
| `2` | `2` | `Λ¹W = W` | `W^∨ ≅ W` — **self-dual, forced** |
| `3` | `3` | `Λ²W ≠ W` | `W^∨ ≅ Λ²W` — self-duality **not** forced |

- `rank_eq_of_volumeForm` — a volume form of degree `N ≥ 1` forces `rank = N`.
  (The `N ≥ 1` excludes the vacuous `Λ⁰W ≅ 𝟙`.)
- `complementary_dim` — `dim Λ^{N-1}W = N = dim W`: the dimension shadow of the
  duality the volume form induces.
- `complementaryDegree_eq_one_iff_degree_two` — **`N − 1 = 1` iff `N = 2`.**
- `degrees_two_and_three_exclusive` — one object cannot carry both degrees.

**The consequence, and it is the point of this note.** The self-duality of the
fundamental object — which `def:fundamental-object` reads as "a *symplectic*
self-dual object, the datum that distinguishes `SL₂/SU(2)` from `GL₂`" — is not
an extra axiom and not a general feature of volume-form objects. It is *what a
volume form of degree exactly two says*, because two is the only degree at which
the complementary exterior power is the object itself.

At degree 3 the same input gives `W^∨ ≅ Λ²W`, which is the `SU(3)` relation
`𝟑̄ ≅ Λ²𝟑` — and which is exactly the **non**-self-duality that
`Sym2GateFSTrichotomy.gate_forces_complex_of_dim_three` (sorry-free) proves any
three-dimensional object must have to pass the `Sym²` gate. So the fundamental
object and the missing flavour object are **the same construction at different
degrees**, not one derived datum and one import.

What this does *not* do: construct a degree-3 object, or show the axioms supply
one. It is a specification in the sense of `qou-dwsh`, and it narrows what to
look for. Where the degree could come from is §2–§6.

## 2. Avenue 1 — "`i` arises naturally the way `q` did": **real, located, and prose-tier**

The recollection is accurate and the corpus's own framing is verbatim what was
remembered. `rem:commutative-crossing-energy`
(`climax-volume-mass/commutative-crossing-energy.md`):

> At `q = 1` the eigenvalues collapse to `(+1, −1) = ℤ₂` … We recover the
> categorical structure of the commutative limit by extracting the *square root*
> of the antisymmetric eigenvalue `λ₋ = −1`: `i = √λ₋`, `i² + 1 = 0` in `R[i]`.
> The categorical structure forces the ring extension `R[i]` … The element `i`
> is the **categorical coordinate of `ℙ(V)` in the commutative limit, mirroring
> the role of `q` in the non-commutative theory.** The construction is intrinsic
> to `R`; we assume no real or complex numbers.

Its Table 1 puts them on one line — `q ∈ End_R(𝟙)` against `i ∈ End_{R[i]}(𝟙)` —
mirroring `def:quantum-universe`'s "*it lands in `End(𝟙) ≅ R`*" exactly.
`rem:affine-chart-origin-of-i-and-q` adds the chart-transition reading: at
`q = 1` the transition degenerates to `zw = 1`, and the quarter-turn
`ρ_{π/2} = i·id_V` is the square root of the chart-swap involution.

**But the template is not discharged, and this matters for using it as a
template.** Both carriers are `remark`s with **no Lean sibling**. The one Lean
file in the arc, `categorical_coordinate_ring_universal`, has signature

```lean
theorem categorical_coordinate_ring_universal
    (S : Type*) [CommRing S] [Algebra R S]
    (qS : Sˣ) (iS : S) (hiS : iS ^ 2 = -1) : ∃! φ, …
```

`iS` and `hiS : iS² = −1` are **hypotheses**. It is the universal property of
`R[q,q^{-1}][i]/(i²+1)` *given* a square root of −1 in the target; it
structurally cannot produce one. `i_coord_sq_eq_neg_one` proves `i² = −1` by
construction (`AdjoinRoot.isRoot_root`) — a fact about the adjunction, not about
a QOU. So **"the categorical structure forces the ring extension `R[i]`" is an
undischarged prose assertion.** Do not cite `prop:categorical-coordinate-ring`
as "`i` is proved emergent in Lean".

Corpus-grep record: `docs/audits` has QA verdicts only; `computations/`,
`docs/coordination/`, `.beans/` and all four `library/` tiers are empty for the
claim (576 dirs, 552 INDEX rows; the 15 `sections/` hits for "imaginary unit" are
octonion physics using `i`, never deriving it). It is a corpus-internal
derivation with no held source. Path 0 (`corpus_search`) was **unavailable** —
the `paper-assistant` MCP failed to connect — so the standing
different-vocabulary blind spot is uncovered this run.

**A defect found on the way, reported not fixed.**
`categorical-coordinate-ring-proof.md:56,58` states `ℂ[i]/(i²+1) ≅ ℂ`; the
polynomial splits over `ℂ`, so by CRT it is `ℂ × ℂ`. Rows 1 and 3 of that
specialisations table assert a non-isomorphism. Already recorded in the block's
`.qa.json` as a reported-but-unedited math finding.

## 3. Avenue 4a — where the ambient `S³` comes from: **a live contradiction in the corpus**

Three places fix it, and they disagree.

**`rem:markov-trace-ambient-s3`** (`braids-and-knots/`, a `remark`, no Lean)
derives it downstream and then explicitly forecloses the owner's identification:

> Because closure surjects onto the links of `S³` … the ambient `S³` is thus
> constructed categorically as the target of the Alexander–Markov
> correspondence, rather than posited geometrically upstream. … This ambient
> `S³` base manifold **must not be confused with** the group manifold
> `SU(2) ≅ S³`.

**`def:reeb-bundle`** (`mass-theory/`, a `definition`, `validation: not_checked`)
states `ℛ_p = (S³ →^{π_H} 𝒮_p ≅ S², ξ_q)` and calls `S³` "**the arena where braid
words in `Bₙ` are evaluated**". That fibration `S³ → S²` *is* the Hopf
fibration, i.e. the coset projection `SU(2) → SU(2)/U(1) = ℂP¹`. The corpus
states it and never takes the step.

**`docs/audits/2026-06-28-ed-ambient-s3-gauge-embedding-wlambda-scope.md` §(i)**
takes it:

> the ambient volume-`S³` **is the gauge-group `SU(2)` itself**, fibered over the
> ED … the ambient `S³` is *built from* the gauge data … sharpens
> `rem:markov-trace-ambient-s3`.

**So the owner's question is a good one and it has surfaced an unreconciled
contradiction.** One says the two `S³`s must not be confused; the other says
they are the same object and calls the remark sharpened. **Only the remark
renders into the paper.** Two repairs are framed in §7.

Two further measurements. The audit's §(i) **mis-cites its only source** — it
attributes a sentence to `brings-surface/embeddability-closure.md` that a grep of
that file for `S^3`/`S³`/`Hopf`/`𝒮_c` does not contain; the real support is
`mass-theory/reeb-bundle.md`, which it never cites. And **`S³ = Sp(1)` is absent
from the corpus entirely** — `Sp(1)` appears in `library/` only, never in
`content/`, so the quaternionic leg of the chain is not one step away, it is not
present.

On the Haar volume form: what the corpus has under "Haar" is the Haar **state**
on `𝒪_q(SU(2))` (`c-quantum-universe.md`, `frobenius-integration.md`) — a
functional on the quantum group algebra, not a volume 3-form on the manifold.
Grep for `bi-invariant`/`biinvariant` across `content/`, `docs/`,
`computations/`: no hit connects either to a volume form on `S³`.

## 4. Avenue 4b — the tetraplectic structure: it is degree **4**, not 3

Read from `library/arxiv-math-0104104v3` (Foth–Leitner), whose `sections/` tier
is complete for this paper (no `ocr/`).

**Definition 3.1.** A tetraplectic structure on a real orientable `X` of
dimension `4m` is a four-form `ψ` with `dψ = 0` and `ψ^m` a volume form. The
quatrisson dual is `ξ ∈ Λ⁴χ(M)` with `[ξ,ξ] = 0` — the degree-4 analogue of a
Poisson bivector, introduced (the paper says so) **because `S⁴` admits neither a
symplectic nor an almost complex structure**. It is a replacement for symplectic
geometry where symplectic geometry is unavailable, not a refinement of it.

**So it supplies a volume form of degree `4m` — the full dimension — and there
is no degree-3 volume form in the source.** The one degree-3 object is Prop 4.2's
`Sp(1)`-invariant **3-vector field** `Θ = ∂_{θ₁} ∧ ∂_{θ₂} ∧ ∂_{θ₃}` on
`Sp(1) ≅ S³`, appearing as the *angular factor* of the degree-4 quatrisson
structure with the radial direction `∂_ρ` supplying the fourth leg. A 3-vector
field is a section of `Λ³TM`, the dual object to a 3-form, and it is the
left-invariant top multivector — the Haar object on `S³`. `Σ := Sp(1)ⁿ ≃ (S³)ⁿ`
is the **isotropy one quotients by** to get the flag manifold
(`Fₙ ≃ Σ\Sp(n)`), the group whose Lie algebra kills `Λ` (Prop 4.1), and the
group permuting the tetraplectic leaves (Thm 7.2). `spₙ` is used to build `Λ`
from the explicit basis.

**The corpus's own tetraplectic layer derives exactly one thing.**
`lem:bring-cone-reeb-quaternionic-twist` proves `[M_i, M_j] = 2M_k` and cyclic —
the `su(2)` relations, sorry-free. Everything else is a definition
(`validation: not_checked`), an interpretation the block itself labels
interpretive (`rem:tetraplectic-su2-gauge-reading`: *"the identification of the
Reeb `SU(2)` with a gauge symmetry … is interpretive"*), or a conjecture that
says of itself it is unbuilt (`conj:tetraplectic-sw-localisation-bridge`: *"A
bridge that is asserted, not built"*; `conj:tetraplectic-askey-localisation`:
*"No local model has been computed"*). And
`def:bring-cone-tetraplectic-structure`'s own `authorNote` concedes the headline:
*"At `m = 1` the tetraplectic condition is **vacuous** … the content in play here
is the invariance, not the tetraplectic condition."*

Two beans already close the routes out, both scope-(b) with named invariants:
**`qou-8p1f`** — the `Spin(7) → G₂ → SU(3)` degeneration is excluded by a
dimension count, `dim GL(8) = 64 < dim Λ⁴(ℝ⁸) = 70`, so no 4-form on `ℝ⁸` has an
open orbit and "generic 4-form" singles out nothing; its constructive half points
at **3-forms in dimension 7** (`G₂`, the one open-orbit case). **`qou-8p1g`** —
tetraplectic reaches `SU(2)`, not `SU(3)`, and its `m ≥ 2` escape was closed by
`computations/quaternionic_flag_su3_exclusion.py` (23/23): every Lie-algebra
homomorphism `su(3) → su(2)^k` is zero by simplicity, and `SU(3)` has no
nontrivial **real** representation below dimension 6, so nothing acts on a
quaternionic line `ℍ = ℝ⁴`.

## 5. Avenue 5 — "if `W` is affine with a volume form, does its compactification give the knot-complement `S³`?"

**Refuted, scope-(b), and by three independent obstructions.** (This section is
standard differential geometry and representation theory, inferred here; the
corpus has never posed the question — grep for `special affine`, `SL(3,ℝ)`,
`SL_3(\mathbb{R})` across `content/`, `docs/`, `.beans/` returns zero.)

1. **The structure has no content to lose.** An affine structure with parallel
   volume on `A³ ≅ ℝ³` is an `SL(3,ℝ) ⋉ ℝ³` reduction of the frame bundle, but
   `ℝ³` is contractible, so every `G`-structure on it is trivialisable. The
   reduction carries zero topological information *before* compactification; all
   of `S³`'s topology is concentrated at the point added.
2. **The volume form does not extend — and it is the very datum the question
   wants transported.** The parallel Lebesgue volume on `ℝ³` has infinite total
   mass. Under stereographic projection the round volume pulls back to
   `8(1+|x|²)^{-3}dx`, not the flat form; conversely the flat form blows up at
   `∞`.
3. **What survives is orientability alone**, and `S³` is orientable anyway.

Verdict: the compactification is a homeomorphism `A³ ∪ {∞} ≅ S³` of topological
spaces and nothing more.

**One correction to the question's own parenthetical.** `S³` *is* parallelisable
— it is a Lie group. The obstruction is not parallelisability; it is (2).

**And the decisive type obstruction, which compactification cannot touch.**
`S³ = SU(2)` does carry a natural degree-3 volume form and `su(2) ≅ Im(ℍ)` is
3-dimensional — but that object is the **adjoint**, of **real (orthogonal)
type**, and `Sym2GateFSTrichotomy.real_triple_fails_gate` (sorry-free) excludes
it *at any multiplicity*. Corroborated mechanically and independently by
`StandardModel/ColourObstruction.real_rep_selfConjugate`: a real matrix commutes
with entrywise conjugation, so `𝟑 ≅ 𝟑̄`, and colour needs `𝟑 ≇ 𝟑̄`. So this route
yields `SO(3)`; `SU(3)` is not merely unreached but excluded.

**The quaternionic move does not escape it — it is the same obstruction in new
clothing.** `two_dvd_dimOf_of_no_complex` shows quaternionic irreps contribute
even dimension, so they cannot reach 3 either; and real and quaternionic are
*precisely the two self-dual Frobenius–Schur types*, which
`gate_forces_complex_of_dim_three` excludes as a sector. Both `su(2) = Im(ℍ)`
and the `Sp(1)ⁿ` quaternionic lines wear self-duality.

Underneath all of it sits one clean invariant: **the complexification of a real
representation is always self-conjugate.** A real 3-manifold's tangent space is a
real 3-dimensional representation of whatever acts on it, so no real
3-manifold's tangent bundle — compactified, trivialised or otherwise — can carry
a non-self-dual complex 3. Compactification does not change reality type.

## 6. What the negatives leave standing — the one direction they all point

For a degree-3 volume form to deliver a **complex-type** 3-dimensional object:

1. the object must be **complex from the start** — the holomorphic tangent of a
   complex 3-fold, or a categorical `Λ³` — not the real tangent of a real
   3-manifold;
2. the volume form must be **holomorphic**: a `(3,0)`-form has structure group
   `SL(3,ℂ) ⊃ SU(3)`, whose standard `𝟑` is complex type. That is the
   Calabi–Yau setting, and it is the one place "a volume form gives you `SU(3)`"
   is actually true;
3. the dimensions then **do not land on `S³`**. A complex 3-fold has real
   dimension 6, and the natural compactification is `ℂP³` or `S⁶`.

The corpus already holds that door open, from three directions that have never
been put in one frame: `S⁶ = G₂/SU(3)` is eightfold open-problem item 3;
`qou-8p1f`'s constructive half points at 3-forms in dimension 7 (`G₂`, the unique
open-orbit case); and `qou-ko4g` proves `g2_dim_split` (`8 + 6 = 14`) while
noting the corpus has **no mention of `G₂/SO(4)` anywhere**, so the tetraplectic
`SU(2)` and colour `SU(3)` have never been put in the same frame — and `G₂` is
that frame.

**Untouched this pass:** the owner's avenues **groupoid** and **derived
categories**. Neither was searched; saying nothing about them is not a negative.

## 7. Two repairs framed for the author, not acted on

1. **The `S³` contradiction.** `rem:markov-trace-ambient-s3` says the two `S³`s
   "must not be confused"; the 2026-06-28 audit §(i) says they are the same and
   calls the remark sharpened. Only the remark renders into the paper. The
   cheapest correct move is to decide which claim the paper makes; if §(i) is
   right, the remark's last paragraph is what to rewrite, and `def:reeb-bundle`
   — not `embeddability-closure.md` — is the citation. **Default if nothing is
   done:** the paper keeps asserting a disclaimer that an audit contradicts.
2. **`W` is overloaded and the notation register does not catch it.** `W` is the
   rank-2 Hodge plane of `H¹(Bring) = 2W` (the calibration carrier) *and* the
   3-dimensional eightfold missing object. `notation-collisions.md` lists `W`
   among blocked single letters but does not separate these two. Note the "3" in
   *"the rank-2 `W`-plane's scale and modulus, plus one orthogonal class"* is
   `2 + 1`, a DOF count across two carriers — **not** a dimension of `W`, and it
   would be easy to misread as support for a 3-dimensional `W`.
