# The 5₂ bridge negatives were structurally expected: the Habiro tail lives in the trivial-connection row of the EXTENDED matrix

**Date:** 2026-07-26. **Status:** literature finding + reframe. No compute,
no wiring, no claim closed. **Read this before any further B1.x work.**

## Summary

Five parameter-free rungs (B1, B1.2, B1.3, B1.4, B1.4′) returned zero hits,
and the constraint programme then proved a quadratic degree obstruction on
the surviving family. A literature check — which should have preceded the
scans — shows **why every one of those negatives was expected on structural
grounds**, and names the object the searches were missing.

The block machinery this repo has been searching (A2's `W±_m`, the 18
`H±_{j,λ}` series, the 3×3 `B`/`A±`/`C±` matrices) comes from
Garoufalidis–Gu–Mariño, *Peacock patterns and resurgence in complex
Chern–Simons theory* ([arXiv:2012.00062](https://arxiv.org/abs/2012.00062)).
Its rows are indexed by the **geometric** boundary-parabolic SL₂(ℂ) flat
connections of the knot — for 5₂ the three σ₁, σ₂, σ₃. That is a 3×3 object.

Garoufalidis–Gu–Mariño–**Wheeler**, *Resurgence of Chern–Simons theory at
the trivial flat connection*
([arXiv:2111.04763](https://arxiv.org/abs/2111.04763), CMP 2024) describes
the resurgent structure of the trivial-connection series in terms of an
**extended** square matrix of (x,q)-series *"whose rows are indexed by the
boundary parabolic SL₂(ℂ)-flat connections, **including the trivial
one**"* — i.e. σ₀ adjoined to the geometric σ₁, σ₂, σ₃. And the Habiro side
is exactly that adjoined row: the published description records a
`(σ₀, σ₁)` entry with σ₀ the trivial representation, entries lying in
generalized Habiro rings, and *the inverted Habiro series obtained from the
Habiro cyclotomic expansion of the colored Jones polynomial*.

**So the Masbaum cyclotomic tail is, by construction, a row the 3×3
geometric block matrix does not contain.** Searching for it inside the span
of the geometric blocks — which is what B1.2 (bare bilinear entries), B1.3
(λ-row selection), B1.4 (θ-descendant tower) and B1.4′ (cyclotomic level
correspondence) all did — cannot succeed, and the uniform 0/440, 0/21,
0/63, 0/165 results are the expected signature, not a surprise.

## What this does and does not change

**Does not invalidate any landed result.** Every negative stands exactly as
recorded, and each was correctly scoped to `(a)` — "this family as-stated"
— rather than as a structural exclusion. The valuation floor
`(q;q)_n²·(q;q)_m³ ∣ c` and its quadratic degree consequence remain true
theorems; they are now understood as measuring *how far* the geometric
sub-block is from the trivial row, which is a meaningful quantity rather
than an obstruction to a bridge that was never going to be found there.

**Does change the named successor.** The B1.5 design note asks for a
level-mixing module map from the Masbaum grading into the geometric block
span. That target is the wrong one. The right object is the **extended
matrix** of GGMW: the trivial-connection row is not something to be
*derived as a combination* of geometric rows — it is an additional
fundamental solution of the same linear q-difference equation, adjoined.

**Method lesson.** The repo's corpus-grep checklist (AGENTS.md §"Before
declaring 'open'") exists to stop an agent re-deriving what the corpus
already knows. The same discipline applies one level out: **check the
literature for the structure of the object before running a wide scan over
a basis you assembled yourself.** Five rungs of parameter-free search
(~700 exact decisions) were spent confirming a structural fact available
in a 2021 abstract. The scans were honest and their negatives are real;
they were simply aimed at a sub-object that provably could not contain the
target.

## Reading list (all open-access)

| Paper | arXiv | Why it matters here |
|---|---|---|
| Garoufalidis, Gu, Mariño — *Peacock patterns and resurgence in complex Chern–Simons theory* | [2012.00062](https://arxiv.org/abs/2012.00062) ([PDF](https://arxiv.org/pdf/2012.00062)) | **The source of A2's machinery.** 3×3 geometric block matrix, Stokes automorphism, q-difference equation; treats 4₁ and 5₂ explicitly. This is the object all B1.x scans lived inside. |
| Garoufalidis, Gu, Mariño, Wheeler — *Resurgence of Chern–Simons theory at the trivial flat connection* | [2111.04763](https://arxiv.org/abs/2111.04763) ([PDF](https://arxiv.org/pdf/2111.04763)) | **The key paper.** The extended matrix including the trivial connection σ₀; Borel transform identified with state-integrals; the Habiro row. |
| Garoufalidis, Zagier — *Knots, Perturbative Series and Quantum Modularity* | [2111.06645](https://arxiv.org/abs/2111.06645) ([PDF](https://arxiv.org/pdf/2111.06645)) | Matrix invariant, Kashaev invariant, the (σ₀,σ₁) entry and the generalized-Habiro-ring entries; SL₂(ℤ) cocycle structure. |
| Crew, Fantini, Goswami, Osburn, Wheeler — *Resurgence, Habiro elements and strange identities* | [2304.07001](https://arxiv.org/abs/2304.07001) | Borel transform of series attached to **Habiro-ring elements**; resurgence proved for two torus-knot families. Directly the analytic side of the corpus's Habiro-element programme. |
| Garoufalidis, Wheeler — *Explicit classes in Habiro cohomology* | [2505.19885](https://arxiv.org/abs/2505.19885) ([PDF](https://arxiv.org/pdf/2505.19885)) | Cycle description of Habiro cohomology; q-holonomic modules as q-deformations of Picard–Fuchs; worked A-polynomial curve of 4₁. The module-map language the B1.5 note was reaching for. |
| Masbaum — *Skein-theoretical derivation of some formulas of Habiro* | [AGT 3 (2003) 537–556](https://projecteuclid.org/journals/algebraic-and-geometric-topology/volume-3/issue-1/Skein-theoretical-derivation-of-some-formulas-of-Habiro/10.2140/agt.2003.3.537.full) (DOI [10.2140/agt.2003.3.537](https://doi.org/10.2140/agt.2003.3.537)) | The `C_n` twist-knot cyclotomic coefficients the repo's `C52(n)` implements. Already cited by the compute. |

## Suggested next rung (not started)

Re-pose the bridge against the **extended** matrix rather than the
geometric sub-block: identify the σ₀ row for 5₂ from GGMW, and check the
repo's `C52`-built tail against it directly. That is a *comparison to a
published object*, not a search over a self-assembled basis — parameter-free
and decisive either way. The existing exact-series engine
(`computations/probes/qseries_exact_util.py`) and the `(★)` normalization
are both directly reusable.

Discipline unchanged: comparison to observed only; no ontological claims;
nothing wired; c₃ tier unchanged (SETTLED, #1580).

## UPDATE (same day): the corpus object is identified — `C52(n)` **is** the Habiro polynomial

Reading GGMW §4.2 (uploaded, `uploads/2111.04763v2.pdf`) turned up the
object in closed form. Equation (161):

$$H_n^{5_2}(q) \;=\; (-1)^n q^{\frac{1}{2}n(n+3)} \sum_{k=0}^{n} q^{k(k+1)} \binom{n}{k}_q$$

attributed there to Habiro [Hab02a] and **Masbaum [Mas03]** — the same
Masbaum paper the corpus's `C52(n)` implements (uploaded as
`uploads/Download.pdf`).

**Machine-exact result** (`qbeta_5two_habiro_polynomial_match_probe.py`,
4/4, integer-Laurent equality, no floats):

> `C52(n)`, read as a q-series at `q = a²`, **equals** `H_n^{5₂}(q)`
> term-by-term for `n ≤ 12` — no dressing, no monomial, nothing.

Consistently, the ratio `(★)LHS / H_n` comes out as
`q^{−(5n²+7n)/2}·(q;q)_n²`, which is *precisely* the (★) normalization,
so it cancels identically. The sorry-free `(★)` theorem is therefore a
bar-inversion statement about a **named object of the literature**, and
`prop:habiro-tail-star-identity` can now cite it as such.

### What this settles about the bridge

GGMW build the extended matrix from the Habiro polynomials by a
**2-parameter (ε,δ) deformation** (eq 165), assembled into `Q_m(ε,δ;q)`
(eq 167), whose Taylor coefficients `Q_m^{(a,b)}` in `(ε,δ)` *are* the
entries of the 6×6 matrix `J_m(q)` (eq 172).

That is a **deformation-and-expand** construction, not a change of
basis. It explains the B1.x negatives completely and finally: no linear
map into the geometric block span could ever have produced the tail,
because the tail is not a combination of those rows — it is the ε⁰δ⁰
seed of a deformation whose *higher* Taylor coefficients generate the
additional rows.

### Further structure recorded for successors (GGMW §4.1–4.4)

- For 5₂ the chain is **3×3 ⊂ 4×4 ⊂ 6×6**: geometric (σ₁,σ₂,σ₃) ⊂ plus
  trivial (σ₀) ⊂ plus two more rows. A2's machinery is the innermost 3×3
  (`J^red_m(q)`, eq 158, built from exactly the `H^{(0)}, H^{(1)}, H^{(2)}`
  the corpus calls the block series).
- The 6×6 is a fundamental solution of the **6th-order** q-difference
  equation satisfied by the *descendant* colored Jones polynomial
  (eq 164); the colored Jones itself satisfies only a 4th-order one.
- The extra 2×2 block is a matrix of **Rogers–Ramanujan** functions
  `H(q) = Σ q^{k²+k}/(q;q)_k`, `G(q) = Σ q^{k²}/(q;q)_k` (eq 180).
  GGMW state plainly: *"We do not understand the labeling of the two
  excess rows and columns"* in terms of SL₂(ℂ)-flat connections. That is
  an open problem in the literature, not a corpus gap.
- The four 5₂ asymptotic series are `Φ^{(σ_j)}`, j = 0,1,2,3 = trivial,
  geometric, conjugate, real, with `V(σ₀) = 0` and
  `Φ^{(σ₀)}(τ/2πi) = 1 + 2τ² + 6τ³ + (157/6)τ⁴ + …` (eq 191).
- **Convention flag (to verify, not asserted as an error):** GGMW's
  saddle values (eq 189) are `V₁ = 3.0241… + 2.8281…i`, `V₂ = V̄₁`,
  `V₃ = −1.1134…`, with `|Im V₁| = Vol(S³∖5₂) = 2.8281…`. The corpus's
  recorded values carry `2.8281…` in the **real** part and `V₃ =
  −2.7580990292`. Before any further cross-use of GGMW numerics, the
  corpus convention should be reconciled against eq (188)/(189)
  explicitly — this may be a deliberate `V ↦ iV` normalization, or a
  discrepancy worth catching.

### Honest note on what is still not derived

Identifying the corpus object with a published one is a *location*
result, not a closure: it does not by itself produce the odd-channel
bridge, and it wires nothing. What it buys is that the next rung is now
a concrete, published construction to follow (eqs 165–172) rather than a
search over a self-assembled basis.
