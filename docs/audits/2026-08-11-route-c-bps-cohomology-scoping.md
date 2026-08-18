# Route C in depth — categorifying the A_ω DT count as chirality-graded BPS cohomology (2026-08-11)

Scoping memo for the forward leg (`qou-rtec`), written after Route A's
scalar-exhaustion result forced the pivot. This is a **research-programme map with
a concrete corpus-grounded entry point** — not a derivation. It states the target
object precisely, the machinery, a milestone ladder (labelled provable-now vs
research), and the QOU-specific lever that makes the entry concrete: *the required
chirality-refined count is the categorification of the corpus's own bar-involution
(q↔q⁻¹) decomposition.*

## 0. Why a scalar cannot work (the settled premise)

`Driver14CharacterVarietyDTMenu.no_scalar_matches_chirality_split_datum`
(sorry-free) proves the `5₂` DT datum is a genuine 2-element **set** `{3,4}`
(chirality-split: `4∈S⁺`, `3∈S⁻`), so no single-valued invariant per knot equals
it. Route A found the sharpest scalar (`R1`: `#connections = A-poly L-degree`,
hits the `dtMax` vector `(3,4)`) and it too falls to this obstruction. The count
is therefore inherently a **graded / set-valued** object. Route C builds that
object.

## 1. The target object

The DT count `A_ω(K)` is the graded dimension of a **BPS cohomology**
`H_BPS(T[K])` — the fivebrane BPS Hilbert space of the DGG theory `T[K]` in the
**closed** (state-integral / GPPV `Ẑ`) sector. Precisely, in the GGM peacock
picture the Stokes matrix `S(K)` is a matrix indexed by boundary-parabolic
`SL₂(ℂ)` flat connections `{σᵢ}`, and

  `A_ω = ` (a distinguished off-diagonal entry of `S`) ` = Ω_DT(σᵢ,σⱼ) = dim H_BPS(σᵢ,σⱼ)`,

a **pairwise, chirality-refined** count (for `4₁`, amphichirality collapses `S⁺,S⁻`
so the `2×2` block hides the refinement; `5₂` is chiral, `3×3`, and the two
Stokes matrices `S⁺(0)`, `S⁻(0)` carry `4` and `3` respectively). So the object to
build is not a number but a **`{S⁺,S⁻}`-graded (chirality-graded) family of
vector spaces**, and the DT spectrum is the multiset of its dimensions.

## 2. The machinery (CoHA / BPS cohomology)

- **Cohomological Hall algebra** (Kontsevich–Soibelman 2010): for a quiver `Q`
  with potential `W`, `H = ⊕_d H^•(𝔐_d, φ_W)` (vanishing cohomology of the
  representation moduli twisted by the potential's vanishing cycle), with a
  Hall-type convolution product.
- **Integrality / BPS cohomology** (Davison–Meinhardt): `H` is free
  super-commutative on a subspace `BPS_• = ⊕_d BPS_d`, and the numerical DT
  invariant is `Ω_d = dim BPS_d` (χ of the BPS cohomology). This is the theorem
  that makes "DT count = dim of a vector space" precise for quivers-with-potential.
- **Knot ⇒ (Q,W):** the DGG 3d–3d dictionary attaches to a triangulated
  `M = S³∖K` a symplectic/quiver datum from its Neumann–Zagier gluing; the BPS
  states of `T[M]` are the DT invariants of that category. **Caveat (load-bearing,
  already learned):** this is the **closed** sector. The **open**-HOMFLY
  knots–quivers correspondence (KRSS) counts `det(K)` (`=5` for `4₁`, `∉{3,4}`)
  and is the WRONG sector — do not use it (recorded in
  `2026-08-02-aomega-conditional-gukov-stosic-bps-bridge.md`).

## 3. The QOU-internal lever — chirality = the bar-involution

**This is the entry point that makes Route C corpus-grounded rather than generic.**
The chirality split `{S⁺,S⁻}` that the scalar-exhaustion forces is, on the QOU
side, the **bar-involution `q ↦ q⁻¹`** — the corpus's pervasive bar-even / bar-odd
decomposition:

| | bar-even face | bar-odd face |
|---|---|---|
| involution eigenspace | `q↦q⁻¹` fixed | `q↦q⁻¹` anti-fixed |
| corpus role | Vol / mass (`4₁`, amphichiral) | `Q_β` / decay (`Φ_b`) |
| Stokes side | `S⁺`-type | `S⁻`-type |
| landed infra | `c1-ggm-bar-parity-faces` (`DoorVParityNoIdentity`, validated), the even/odd Ohtsuki tower parity rule (`OhtsukiTowerBarParity`) | same |

For the **amphichiral** `4₁` the bar-involution is an isomorphism `S⁺≅S⁻`, so the
two DT integers coincide into one `2×2` block — exactly why `4₁` alone cannot
separate scalar-from-spectrum. For the **chiral** `5₂` the involution is
non-trivial, `S⁺≇S⁻`, and the DT spectrum splits `4∈S⁺`, `3∈S⁻`. **So the
required chirality-graded object is the bar-graded (bar-even ⊕ bar-odd) piece of
the categorified count**, and the QOU-internal Milestone 3 (below) becomes:
*show the bar-parity Wedderburn decomposition of the Hecke/Markov data
categorifies to the two Stokes columns.* This ties Route C to landed corpus
infrastructure (the whole even/odd bar-parity programme) instead of to a generic
CoHA computation.

## 4. Milestone ladder (labelled)

- **M0 — reframe the count through the bar-grading (PROVABLE NOW, Lean).**
  Restate `no_scalar_matches_chirality_split_datum` as: the DT datum factors
  through a `ℤ/2`-graded (bar-even ⊕ bar-odd) object; a scalar is the `ℤ/2`-trivial
  shadow. Formalize the bar-involution action on the certified Stokes matrices
  `S⁺(0),S⁻(0)` (already `Fin n → Fin n → ℤ` in `StokesQZeroDTCount` /
  `FiveTwoDTSpectrumSplit`) and prove the split is the bar-eigenspace
  decomposition. **Bounded, sorry-free-achievable; the concrete first step.**
- **M1 — the closed-sector (Q,W) for `4₁`,`5₂` (compute + literature).** Write the
  quiver-with-potential (or the DGG symplectic datum) of the closed sector whose
  DT spectrum is `{3,4}`, from the NZ gluing of the 2- and 3-tetrahedron
  triangulations. Partly in the literature (DGG mirror curve); the QOU value-add
  is deriving the NZ data from the Bring embedding (Route E overlap).
- **M2 — the BPS cohomology (compute, heavy but finite).** For that small `(Q,W)`
  compute `BPS_d` (Davison–Meinhardt) and check `dim` reproduces `{3,4}` with the
  bar/chirality grading. Feasible for 2–3-node quivers symbolically.
- **M3 — the QOU-internal bridge (OPEN research programme).** Express `(Q,W)` /
  `H_BPS` directly from the QOU Hecke `H_n(q)` Wedderburn data + Markov trace +
  Bring embedding, bar-graded — a **categorified AJ / Hecke→BPS formula**. This is
  the genuinely literature-open theorem (categorification of DT for the knot
  category); it is not a session and must not be claimed until it produces a
  derivation `F`, per the anti-laundering rule.

## 5. Recommendation

Start at **M0**: formalize the bar-involution action on the certified Stokes
matrices and prove the `{3,4}` split is its bar-eigenspace decomposition. It is
bounded, Lean-achievable now, converts the "no scalar" obstruction into a positive
structural statement (the count *is* the bar-graded object), and it is the honest,
non-laundering first brick of Route C — connecting the DT split to the corpus's
own bar-parity programme rather than importing a generic CoHA. M1–M2 are compute
milestones for a follow-up; M3 is the research horizon. Tracked in `qou-rtec`
(forward) + a new `qou-rtm0` (the M0 brick).

Nothing here derives `A_ω`; `A_ω=3` remains certified-as-GGM-DT-count,
conditionally adopted. Route C's promise is to replace *import* with *derivation*
— and its first honest step is M0.

## 6. M3 executed (2026-08-18, PR #5275) — reframed, sharpened, still open

M3's framing in §4 above ("build the CoHA / express `(Q,W)`, `H_BPS` from Hecke
data") is **superseded by M2's own result** and is retained above only as the
historical rung. M2 proved the spectrum would be *abelian*: every Borel ray
distinct, trivial plethystic, all multiplicities `1`. A direct sum of
one-dimensional spaces carries no information beyond **which rays exist** — so
categorifying it is nearly content-free, and M3's real target is to **derive the
index set `Ω`**. Sharper, and more tractable.

### `H_Ad` — the hypothesis, and what it is NOT

`H_Ad`: the knot-**independent** core of the index set is the weight set of the
adjoint representation of `𝔰𝔩₂`. With `x = m²`, `Ad` has eigenvalues `(x,1,x⁻¹)`,
so `χ_Ad(x) = x + 1 + x⁻¹ = s(x)` exactly and `χ_Ad(1) = 3 = dim 𝔰𝔩₂`. Mechanism
(not a numerology pick): the Borel singularities are differences of complex
volumes of flat connections, whose deformation theory is governed by
`H¹(M, Ad ρ)` — the adjoint local system is the *canonical* coefficient object.
QOU-side, `Ad ≅ Sym²V` = the partition-`(2)` Wedderburn block of `H₂(q)`.

### The R1 discrimination — the finding that matters

`H_Ad` is **not** a re-description of Route A's surviving `R1` reading. Using the
certified chirality split (`4₁` amphichiral ⇒ `(S⁺,S⁻) = (3,3)`; `5₂` chiral ⇒
`(4,3)`):

| reading | projection | `4₁` | `5₂` |
|---|---|---|---|
| `R1` (#boundary-parabolic connections = A-poly `L`-degree) | `dtMax` | 3 | 4 |
| `H_Ad` core (`s(1) = dim 𝔰𝔩₂`) | `dtMin` | 3 | 3 |

Different halves of the same datum — and the **pair** reconstructs the 2-element
set `{3,4}`. That is **not** in tension with
`Driver14CharacterVarietyDTMenu.no_scalar_matches_chirality_split_datum`, which
excludes *one* scalar equalling a 2-set, not two scalars naming it between them.
This is the sharpest positive structural statement Route C has produced.

### Two things that make it thinner than it sounds

1. **The support is ONE observation.** `4₁`'s amphichirality collapses `dtMin`
   onto `dtMax`, so `4₁` supplies no evidence for `H_Ad` independent of `R1`.
   Everything rests on `S⁻(5₂) = 3`.
2. **A rival survives — `H_floor`.** Take the core to be the `{0, g, ḡ}` triple
   that *every* hyperbolic knot carries, i.e. `R1`'s own universal floor, with no
   `𝔰𝔩₂` anywhere. Its core is also `3`, so it imposes identical constraints and
   makes identical predictions; its Chern–Simons values `{0, +𝔙, −𝔙}` even supply
   a palindromic 3-element grading, so the shape screen cannot arbitrate. **The
   certified data cannot separate `H_Ad` from `H_floor`.** Only the grading
   *variable* could — meridian `x = m²` (`H_Ad`) vs Chern–Simons value
   (`H_floor`). GGM's `s(x)` is written in the meridian variable, which *weakly*
   favours `H_Ad`; "weakly" is the honest word.

### Two corrections this work forced, recorded at source

- **`R1` does not fail knot-independence.** An earlier note in the M3 probe said
  it did. Retracted: `R1` hits the `dtMax` vector `(3,4)` **exactly** (§5 of the
  attack-options audit); its *proved* failure is single-valuedness against a
  set-valued datum. Conflating the two failure modes hides the `dtMin`/`dtMax`
  complementarity entirely.
- **"`5₂` has one extra flat connection" IS `R1`.** That was proposed as the
  completion of `H_Ad`; it is `R1` verbatim, so the completion *composes two
  imported readings* rather than deriving anything from Hecke data. It must not
  be presented as a derivation.

### Where M3 now stands

**Open, with a named rival.** The live question is no longer "find the extra `5₂`
ray" (that is `R1`) but **separate `H_Ad` from `H_floor`**. Two routes: (a) a
*third* knot — a hyperbolic `K` with more than 3 boundary-parabolic connections
whose `s(x)` core stays `x+1+x⁻¹` breaks `H_floor` and leaves `H_Ad` standing
(GGM covers `4₁`/`5₂`; Gu–Mariño-type data on `6₁`/`7₂` would decide); (b) show
the QOU-side `Ad ≅ Sym²V` reproduces the *meridian* grading, which `H_floor` has
no route to.

Artifacts: `QOU.QBeta.AdjointIndexSetM3` (core `Int`, `lean`-direct exit 0,
sorry-free), `computations/probes/aomega_m3_adjoint_index_set.py` (7/7, four
adversarial). Bean `qou-m3ad`. Nothing wired; `A_ω = 3` remains
certified-as-GGM-DT-count, conditionally adopted.
