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

### The meridian grading is derived (route (b), same PR)

The one discriminator Part 2 named — the grading *variable* — is now supplied on
the `H_Ad` side from QOU-native Schur–Weyl data. The shape-`(2)` **semistandard**
Young tableaux over `{1,2}` are `{11, 12, 22}`, and their `m`-weights are
`(2, 0, −2)` — exactly **twice** the adjoint `x`-exponents `(1, 0, −1)`, i.e.
precisely `x = m²`. So `s(x) = x + 1 + x⁻¹` is the character of `S^{(2)}(ℂ²)` in
the **meridian** variable, read off Young-tableau combinatorics with nothing
fitted, and the three weights are distinct (so M2's `sMultiplicities = [1,1,1]`
becomes combinatorial rather than asserted).

**Scope (a), stated plainly:** this gives `H_Ad` a mechanism `H_floor` lacks. It
does **not** exclude `H_floor` — "one hypothesis has a derivation the other
lacks" is weaker and different from "the other is refuted".

**Third correction, forced by doing this.** `Ad` is the Schur–Weyl **partner** of
the partition-`(2)` Hecke block, *not* the block: `#SYT((2)) = 1` (the `H₂(q)`
block is one-dimensional) while `#SSYT((2)) = 3` (the partner `S^{(2)}(ℂ²)` on the
`U_q(𝔰𝔩₂)` side of `V^{⊗2} ≅ ⨁_λ S^λ(V) ⊗ M_λ`). Earlier text in the Lean
docstring, the probe docstring and the bean all said "the partition-`(2)`
Wedderburn block of `H₂(q)`" — a conflation of the two sides of Schur–Weyl
duality, corrected at all three sources, with both dimensions now *derived* in
Lean from the weakly- vs strictly-increasing filling conditions.

### Part 4 — the remainder is derived from the trace field, and it is `H_floor`'s win

Part 1 forced the `5₂` remainder to be `1` and said any completion "must derive
it independently". `H_floor` **does**, from arithmetic already sitting in the
corpus. Garoufalidis–Zagier (`library/arxiv-2111.06645v3/2111.06645v3.pdf` §2.1, glyph-verified)
give `P_K`, the boundary-parabolic `SL₂(ℂ)` representations, for three knots:

| `K` | reduced trace algebra | real | pairs | `\|P_K\|` | core | remainder |
|---|---|---|---|---|---|---|
| `4₁` | `ℚ(√−3)` (imag. quadratic) | 0 | 1 | 3 | 3 | **0** |
| `5₂` | cubic, disc `−23`, sig `(1,1)` | 1 | 1 | 4 | 3 | **1** |
| `(−2,3,7)` | `ℚ(ξ) × ℚ(η)`, `η` totally real | 1+3 | 1 | 7 | 3 | **4** |

`|P_K| = 3, 4, 7` reproduces `R1`'s `(4₁,5₂) ↦ (3,4)` **from a source independent
of the A-polynomial** and extends it to a third knot. And the remainder is the
count of **real embeddings** of the reduced trace algebra: `4₁`'s trace field is
imaginary quadratic and has none (remainder 0); `5₂`'s disc `−23` cubic has
exactly one — GZ even name it, the root with zero imaginary part (remainder 1).

**This counts against `H_Ad`, not for it.** `H_floor` now explains the number `3`,
*predicts* the remainder, and does so with no `𝔰𝔩₂` anywhere. `H_Ad`'s surviving
distinct content is the Part-3 meridian **grading**, which `H_floor` says nothing
about. Read them as answering different questions — `H_floor`: why that many;
`H_Ad`: why that polynomial — rather than as rivals for one.

**Retraction — route (a) as previously stated is wrong.** The earlier text said a
knot with *more* than 3 boundary-parabolic connections would break `H_floor`. It
would not: `H_floor`'s core is the universal **floor** `{σ₀, g, ḡ} = 3` for every
hyperbolic knot, exactly as `H_Ad`'s is `dim 𝔰𝔩₂ = 3`. No third knot separates
them at the core — now *proved* on all three (`core_is_three_on_all_three`). What
a third knot actually buys: (i) a second non-degenerate data point against the
one-observation problem, and (ii) a **one-sided** falsification test of `H_Ad`'s
*polynomial* claim — if a rank-6 knot's Stokes entries are not built from
`x+1+x⁻¹`, `H_Ad` breaks while `H_floor`, which makes no polynomial claim, cannot.

**Literature status (measured, not assumed).** All 371 corpus PDFs were text-
extracted and swept; 47 mention "Stokes". GGM 2012.00062 and GGMW 2111.04763 treat
**only** `4₁` and `5₂` — GGMW §1.4 is literally "Illustration with the two
simplest hyperbolic knots"; every `6₁`/`7₂` string in both is a page number.
Garoufalidis–Zagier 2111.06645 covers `(−2,3,7)` but for *perturbative series and
quantum modularity*, with two occurrences of "Stokes" and no Stokes matrices. So
**no `q→0` Stokes matrix for a third hyperbolic knot exists in the corpus**, and
the `(−2,3,7)` count `7` stands as a *prediction* of `R1`/`H_floor`, not a check.

### Where M3 now stands

**Open, with a named rival.** The live question is no longer "find the extra `5₂`
ray" (that is `R1`) but **separate `H_Ad` from `H_floor`**. Route (b) — derive the
meridian grading from Schur–Weyl — is delivered above. Route **(a)** is what
remains: a *third* knot. A hyperbolic `K` with more than 3 boundary-parabolic
connections whose `s(x)` core stays `x+1+x⁻¹` would break `H_floor` (whose core
*is* the connection floor by construction) and leave `H_Ad` standing. GGM covers
`4₁` and `5₂` only, so this is a **literature ask, not a compute**: published
`q→0` Stokes constants for a third hyperbolic knot (Gu–Mariño-type data on `6₁` /
`7₂`). The second remaining piece is unchanged — the extra `5₂` ray is `R1`, so a
genuine derivation still needs that ray to come out of the Hecke side.

Artifacts: `QOU.QBeta.AdjointIndexSetM3` (core `Int`, `lean`-direct exit 0,
sorry-free), `computations/probes/aomega_m3_adjoint_index_set.py` (13/13, four
adversarial). Bean `qou-m3ad`. Nothing wired; `A_ω = 3` remains
certified-as-GGM-DT-count, conditionally adopted.

## 7. The third knot was in the corpus (2026-08-19) — and my §6 sweep was too narrow

§6 closed by saying the remaining test needed *"a source **outside** the 371
uploads, i.e. real outbound search"*. That operational conclusion was **wrong**,
and the reason is a methodology defect worth naming.

### What §6 got right, and what it got wrong

The §6 sentence *"no `q→0` Stokes matrix for a third hyperbolic knot exists in
the corpus"* is **still accurate** — nothing retracts it. But the sweep behind it
keyed on the string **"Stokes"**, and that is far narrower than the question. The
paper that carries the third knot's grading — Garoufalidis–Zagier, *Knots and
Their Related q-Series*, SIGMA 19 (2023) 082 (`uploads/2304.09377v2.pdf`) — says
"Stokes" **exactly once**, so it ranked below thirty other files and was never
opened. It is not obscure: it is the sequel `[44]` that `2111.06645` **announces
in its own abstract**, and I had already quoted that abstract in §6.

Lesson, stated generally: **a corpus sweep keyed on the vocabulary of the answer
you expect will miss the paper that answers in different words.** The §6 sweep
looked for resurgence vocabulary; the data arrived in quantum-modularity
vocabulary.

### The near-miss that makes the guard load-bearing

GZ §3.5 reports, for `(−2,3,7)`, *"a new phenomenon … the weight spaces have
higher multiplicity"* — weights with dimensions summing to `r = 6`, one of them
of dimension **4**. That reads as precisely the rank-6, non-multiplicity-free
refutation of `H_Ad` that §6 asked for.

**It is not, and the two objects must not be conflated.** The graded object has
total `r` — which is **2** for `4₁` — while `s(1) = 3`; and `4₁`'s weight set is
`{−1/2, +1/2}`, two elements against `s(x)`'s three. Different objects, so the
higher multiplicity does not bear on `H_Ad`'s polynomial claim. This is the
`da-arity-conflation` failure mode, and it was one inference away from retiring a
hypothesis on the strength of an unrelated grading.

### Erratum in the source, adjudicated

Three statements in GZ §3.5 describe the same grading:

| statement | dimensions |
|---|---|
| prose: *"weights 0, 1 and 2 with dimensions 1, 4 and 1"* | `(1, 4, 1)` |
| explicit decomposition `W₀ = ⟨H₀,H₃,H₄,H₅⟩`, `W₁ = ⟨H₁⟩`, `W₂ = ⟨H₂⟩` | `(4, 1, 1)` |
| `ε`-degrees `(δ₀…δ₅) = (0,1,2,0,0,0)`; weight vector `(−1,0,1,−1,−1,−1)` | `(4, 1, 1)` |

Two independent internal statements against one: **the prose transposes its
first two dimensions.** Both readings total `6`, so a sum-check cannot catch it —
the same shape as the GGM eq-(200) `q¹` erratum adjudicated earlier in this arc.

### What is genuinely new

**The Part-4 signature formula is corroborated on a third knot.** GZ's ranks are
`r = 2, 3, 6` — stated outright in `2111.06645` §2.1 and recovered independently
in `2304.09377` §3.4 from the q-series counts `4, 6, 12 = 2r`. Part 4's rule
gives `r = (real embeddings) + 2·(complex pairs) = 2, 3, 6`, and `r = |P_K| − 1`,
the non-trivial boundary-parabolic representations. Three knots, three distinct
values, three routes, one answer.

**`W₀` is an `S₃` representation whose blocks are partitions of 3.** GZ: the
`SL₂(ℤ)` action is the identity on `W₁`, `W₂` and has kernel `Γ(2)` on `W₀`, so
`W₀` carries a representation of `S₃ = Γ/Γ(2)`, decomposing as *"the
2-dimensional irreducible representation of `S₃` and two copies of the trivial
representation"* — i.e. `(2,1) ⊕ (3)^{⊕2}`, dimension `2 + 1 + 1 = 4`.

`S₃`-irreps are indexed by partitions of `3`, the **same Wedderburn indexing the
QOU Hecke programme uses at `q = 1`** — so the third knot's modular structure
lands in the corpus's own language without being put there. And one block is
**absent**: the **sign** representation has multiplicity `0`. Under the standard
identification the sign block is the bar-odd one, so the `Γ/Γ(2)` action on the
level-2 part carries no sign component — a chirality-flavoured asymmetry, sitting
on the same involution that grades the DT split.

### The absence is FORCED — and its scope is one knot

The paragraph above originally read *"observed, not derived"*. That was too weak
in one direction and too strong in the other; both are corrected here.

**Too weak: the absence has a mechanism.** `χ(W₀) = [4, 2, 1]` on the classes
`(e, transpositions, 3-cycles)` of sizes `(1, 3, 2)`. That is exactly
`[3, 1, 0] + [1, 1, 1]` — the character of the **permutation module on 3 points**
plus a trivial. Characters determine complex representations up to isomorphism,
so `W₀ ≅ ℂ[X] ⊕ ℂ` for a 3-element `S₃`-set `X`. And a 3-point permutation module
of `S₃` contains **no** sign component:

  `⟨χ_perm, χ_sign⟩ = (1·3·1 + 3·1·(−1) + 2·0·1)/6 = 0`,

a general fact with nothing knot-specific in it; a trivial summand contributes
`0` to sign multiplicity, so adding any number of them cannot create one. The
missing sign block is therefore **forced by the shape of `W₀`**, not a
coincidence awaiting interpretation.

**Too strong: it is a one-knot statement.** GZ introduces the level as *"a new
phenomenon"* arising at `(−2,3,7)`, which has `N = 2`; `4₁` and `5₂` have
`N = 1`, so `ρ` factors through the **trivial** quotient — there is no finite
group acting, hence no sign block there to be absent. The *mechanism* is general
(any permutation-type module); the *instantiation* is single-instance among these
three knots, by construction. Both halves are stated together in the Lean and the
probe so neither can be quoted alone.

**What stays interpretive.** That `X` is geometrically the three cusps of `Γ(2)`
(equivalently the three non-zero 2-torsion classes) is the standard
`Γ/Γ(2) ≅ S₃` picture, but GZ does not say `W₀` realizes it and nothing here
claims so. The character identity is proved; the geometric reading is not.

Nothing is wired.

Artifacts: `QOU.QBeta.GZThirdKnotRankGrading` (core `Int`, sorry-free, no
`sorryAx`), `computations/probes/gz_third_knot_rank_grading.py` (12/12). Bean
`qou-gz37`.

### Re-sweep executed — the vocabulary bias hid more than one paper

The lesson above was tested rather than asserted. Re-running the 371-PDF sweep on
**structural** vocabulary (knot names, `pretzel`, `weight space`, `Galois orbit`,
`trace field`, `quantum modularity`, `boundary-parabolic`, `level of a knot`,
`A-polynomial`) instead of `Stokes` matches **94** files and ranks them very
differently. It surfaced a **second** confirmed miss:

> `uploads/ki6c.pdf` — Ohtsuki–Yokota, *On the asymptotic expansions of the
> Kashaev invariant of the knots with 6 crossings* (`6₁`, `6₂`, `6₃`, with the
> volume conjecture proved for them). It contains the string "Stokes" **zero**
> times, so it was structurally invisible to the original sweep.

**Honest yield, so this is not oversold.** `ki6c` does **not** close the open
items. It treats the perturbative side (asymptotic expansions of the Kashaev
invariant) via the **single geometric critical point**, not the full set of
boundary-parabolic representations — so it yields no `|P_K|` for the 6-crossing
knots — and it carries no Stokes matrices. What it does establish is that the
vocabulary bias cost this arc *at least two* papers, from one cause. Other
unopened high-rankers: `1511.05628`, `2412.04241`, `1303.5278`.

### Dimofte–Garoufalidis §6: the signature inputs confirmed, and Part 4's hypothesis named

The re-sweep also surfaced `uploads/1511.05628v1.pdf` (Dimofte–Garoufalidis,
*Quantum Modularity and Complex Chern–Simons Theory*), which §6 states trace
fields in the **signature notation `[r₁, r₂]`** — the exact input Part 4's rule
consumes — for five knots:

| knot | minimal polynomial | `[r₁,r₂]` | disc |
|---|---|---|---|
| `4₁` | `x² − x + 1` | `[0, 1]` | `−3` |
| `5₂` | `x³ − x² + 1` | `[1, 1]` | `−23` |
| `6₁` | `x⁴ − 2x³ + x² + 3x + 1` | `[0, 2]` | `257` |
| `(−2,3,−3) = (−2,3,9)` | `x⁵ − x⁴ + x³ + 2x² − 2x + 1` | `[1, 2]` | `23·733` |
| `(−2,3,7)` | *same trace field as* `5₂` | `[1, 1]` | `−23` |

**Confirmation.** Part 4 read `4₁ ↦ (0,1)` and `5₂ ↦ (1,1)` off GZ's prose; DG
states the same two in type notation. Two sources, identical inputs.

**Part 4's silent hypothesis, now named.** The rule needs
`r = #embeddings of A_K^red`, and `A_K^red ⊇ F_K` with equality **iff** `K` has no
boundary-parabolic representations outside its trace field. Part 4 used
`A_K^red`; DG tabulates `F_K`. They coincide at `4₁` and `5₂`, so **Part 4's
two-knot agreement did not establish which one the rule needs** — and `(−2,3,7)`
settles it: its trace field is `5₂`'s (3 embeddings) while the measured rank is
`6`, because `P_K` acquires a second Galois orbit over the totally real `ℚ(η)`.
The hypothesis has to be stated, not assumed.

**Two conditional predictions.** Under `A_K^red = F_K`: `6₁` has `r = 4`,
`|P_K| = 5`; `(−2,3,9)` has `r = 5`, `|P_K| = 6`. Falsifiable, unverified (no
corpus source gives these ranks), and false if either knot behaves like
`(−2,3,7)`.

**A guarded non-inference.** DG's Table 2 has a column headed "Level"
(`4₁ ≤7`, `6₁ ≤3`, …). That is the **Chern–Simons level** `k` with `ζ^k = 1` —
their abstract says so — **not** GZ's level `N` from Part E. Reading `6₁ ≤ 3` as
"`6₁` has level 3" would manufacture the fourth level-`>1` knot the open question
asks for, out of an unrelated quantity. **Third instance of this conflation trap
in this arc**; recorded so it is not walked into a fourth time.
