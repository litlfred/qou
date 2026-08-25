# Route A: RSZ Newton-polygon invariants — C1 kernel vs GGM eq 49 (2026-07-20)

**Question.** Are the two order-2 q-difference kernels
C1 `[m+2]_q·b_{m+2} = b_{m+1} + b_m` (proved q-involution/q-Borel form) and
C2 `y_{m+1} − (2−q^m)·y_m + y_{m−1} = 0` (GGM eq 49, `library/arxiv-2012.00062v3/2012.00062v3.pdf` p. 14)
equivalent as q-difference **modules** — i.e. under arbitrary GL₂ gauge with
meromorphic/formal coefficients, not just the diagonal gauges pruned in
[`2026-07-20-qlift-ggm-gauge-prune.md`](2026-07-20-qlift-ggm-gauge-prune.md)?
Reference read directly: Ramis–Sauloy–Zhang, *Local analytic classification of
q-difference equations*, Astérisque 355 (`library/arxiv-0903.0853v3/0903.0853v3.pdf`): Newton polygon
Def §2.2.1 (p. 16), invariance Thm 2.2.1, pure/fuchsian classification §2.2.2
(Lemma 2.2.3 + p. 19), formal splitting §2.2.3.1, slope filtration Thm 2.2.4.
Gauge = F ∈ GL_n(C({z})) resp. GL_n(C((z))) (§2.1.2, p. 13).

## 1. Operators in x = q^m (σ: x → qx)

With b_m = f(q^m), [k]_q = (q^k−1)/(q−1), and window shifted to m, m+1, m+2:

- **C1**: [m+2]_q = (q²x−1)/(q−1), so (×(q−1)):
  `L1 = (q²x − 1)·σ² − (q−1)·σ − (q−1)`.
- **C2** (shift m → m+1): y_{m+2} − (2−q^{m+1})y_{m+1} + y_m = 0:
  `L2 = σ² − (2 − qx)·σ + 1`.

## 2. Newton polygons by hand (RSZ §2.2.1: points (i, v₀(aᵢ)), lower hull; slopes μ = d/r)

**At x = 0** (v₀ = x-adic valuation; both a₀, a₁, a₂ have nonzero constant term for q ≠ 1):

| operator | (0, v₀(a₀)) | (1, v₀(a₁)) | (2, v₀(a₂)) | lower hull | S at 0 |
|---|---|---|---|---|---|
| L1 | (0,0) | (1,0) | (2,0) | one edge (2,0) | **{0}**, mult 2 (fuchsian) |
| L2 | (0,0) | (1,0) | (2,0) | one edge (2,0) | **{0}**, mult 2 (fuchsian) |

**At x = ∞**: local variable w = 1/x; σ: x→qx is w→w/q, so rewrite in σ̃: w→qw
(RSZ frame needs |q|>1; q₀ ≈ 1.11 ✓). Substituting and clearing denominators:

- L1 → `−(q−1)w·σ̃² − (q−1)w·σ̃ + (1−w)`: points (0,0), (1,1), (2,1).
  Point (1,1) lies above the segment (0,0)→(2,1) (mid-height ½ < 1): one edge
  (r,d) = (2,1), slope **½, mult 2** — pure isoclinic, **non-integral** slope.
- L2 → `qw·σ̃² + (1−2qw)·σ̃ + qw`: points (0,1), (1,0), (2,1). Vertex at (1,0):
  two edges (1,−1), (1,+1): slopes **{−1, +1}**, mult 1 each — two integral slopes.

(Machine cross-check of the hulls: mpmath/lower-hull script, this session, agrees.)
Module-vs-operator duality (RSZ footnote 2 p. 16, Example 2.2.2, r_{M∨}(μ)=r_M(−μ))
negates all slopes uniformly; the comparison is unaffected: −{½} ≠ −{−1,+1}.

## 3. Slopes differ at ∞ ⇒ formal inequivalence

By RSZ Thm 2.2.1(i) the Newton polygon is an invariant of the q-difference module,
and by §2.2.3.1 + Thm 2.2.4 the slope multiset with multiplicities is preserved by
any gauge F ∈ GL₂(C((w))) (a fortiori C({w})). At ∞: S(C1) = {½ (×2)} vs
S(C2) = {−1, +1}. **Disjoint** — C1 is pure non-integral, C2 is mixed integral.

## 4. Associated graded / exponent data (independent confirmations)

**At 0** both are fuchsian; the class is the similarity class of A(0) ∈ GL₂(C)
with eigenvalues taken in the fundamental annulus, i.e. mod q^ℤ (RSZ §2.2.2.1,
p. 18–19). Characteristic equations a₂(0)u² + a₁(0)u + a₀(0) = 0:

- C1: −u² − (q−1)u − (q−1) = 0 ⇒ `u² + (q−1)u + (q−1) = 0`; product u₁u₂ = q−1,
  sum = 1−q. For 1 < q < 5 the discriminant (q−1)(q−5) < 0: **complex** exponents
  (at q₀: u = −0.05499 ± 0.32704i, |u| ≈ 0.33163).
- C2: u² − 2u + 1 = (u−1)² ⇒ **double exponent 1** (unipotent; the m→−∞ limit
  y_{m+1}−2y_m+y_{m−1}=0 has constant+linear solutions).

Complex non-real exponents can never equal 1·q^k (positive real), and for real
0 < q < 1 the product q−1 < 0 forces a negative exponent, also ∉ q^ℤ. So the
**fuchsian classes at 0 differ mod q^ℤ too** — inequivalent already at 0.
Numeric check (mpmath, dps 50, q ∈ {0.9, 1.05, q₀}): log_q|u₁| = −10.578… at q₀,
never integer; and always the complex/sign obstruction above.

**Determinant module** Λ²M (rank 1, coefficient a₀/a₂ of the companion system):

- C1: det = −(q−1)/(q²x−1); at 0 the class is **q−1 mod q^ℤ**
  (log_{q₀}(q₀−1) = −21.156…, not an integer); at ∞ slope 1 = 2·½ ✓.
- C2: det = 1 — **trivial**; slope sum at ∞: −1+1 = 0 ✓.

det classes q−1 vs 1 differ mod q^ℤ (any q with q−1 ∉ q^ℤ, incl. q₀): a third
independent obstruction, since a gauge equivalence induces one of determinants.

## 5. Verdict (per AGENTS.md refuted-discipline)

**Scope-(b) structural exclusion.** C1 and C2 are **inequivalent as q-difference
modules over C((x)) and C({x}), at both local points 0 and ∞** — no gauge
F ∈ GL₂ with formal or convergent Laurent coefficients in x = q^m (at either
point) maps one to the other. Cited invariants: RSZ Astérisque 355 **Thm 2.2.1**
(Newton polygon is a module invariant) + **Thm 2.2.4** (slope filtration / gr
functor) for the ∞-slope mismatch {½,½} ≠ {−1,+1}; RSZ **§2.2.2.1** fuchsian
classification for the exponent mismatch at 0 ({complex pair} ≠ {1,1} mod q^ℤ);
determinant classes q−1 ≠ 1 mod q^ℤ. These are proved classification theorems,
not failed fits. This subsumes and strengthens the diagonal-gauge prune.

**Explicitly NOT excluded** (outside the RSZ module category):
- sequence-level gauges g_m **not** of the form g(q^m) with g meromorphic/formal
  at 0 or ∞ (arbitrary sequences carry no Newton-polygon obstruction);
- **inhomogeneous** identifications (b vs y plus a forced term — the 4₁ colored
  Jones is minimally order-2 *inhomogeneous*);
- transforms changing the module (q-Borel/q-Laplace, summation kernels, Hadamard
  products): these are **functors, not gauges** — indeed q-Borel shifts slopes,
  and C1's slope-½ vs C2's slopes {−1,+1} suggests comparing a **q-Borel/
  ramified transform of C1** with C2 as the next constructive step, rather than
  any direct gauge.

**Consequence for Route A.** The C1 q-involution kernel is *not* the GGM
descendant equation in disguise: they are genuinely distinct q-lifts of the same
classical depth-2 shadow (confluent limits agree; the q-structures differ at the
level of RSZ formal invariants). Any identification must proceed through a
slope-changing transform (q-Borel of order adjusting ½ ↦ {−1,+1}) or an
inhomogeneous/functorial correspondence — pinned as the next step.

**Discipline.** Formalize-first: the polygon computation is exact hand algebra;
mpmath used only as cross-check (hulls, exponents, non-integrality of the q-logs).
No AME data; conjecture-level status of the q-lift unchanged.
