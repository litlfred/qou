# Obstruction A, measured: the corpus's own meson braid has Vol = 0 (2026-08-24)

**Bean:** `qou-qpj9` · **Tool:** SnapPy 3.3.2 · **Status:** measurement + prune, **no braid proposed, no mass fitted**

## What was measured

`def:categorical-meson` fixes the meson braid explicitly:

$$\mathfrak{M} = T_{01}\cdot\mathcal{L}_H\cdot T_{10} = (\sigma_0\sigma_1)^2\cdot\sigma_1\sigma_0$$

— 6 crossings on 3 strands. Nobody appears to have closed it and computed the volume. Doing so:

| object | braid | comps | Vol | solution type |
|---|---|---|---|---|
| **meson `𝔐`** | `(σ₀σ₁)²σ₁σ₀` | 1 | **0** | contains flat tetrahedra |
| `L₊` Hopf | `σ₀σ₁` | 1 | 0 | degenerate |
| `(σ₀σ₁)³` full twist | — | 3 | 0 | degenerate |
| trefoil | `σ₀³` | 1 | 0 | flat |
| Borromean | `(σ₀σ₁⁻¹)³` | 3 | 7.32772475342 | positively oriented |

The Borromean row is the control: it reproduces `2·V_oct` to 11 places, so the pipeline is sound.

**Identification via the knot group** (`determinant`, `signature` and `alexander_polynomial` all require Sage, which is absent; the fundamental group does not):

| braid | relator | group | knot |
|---|---|---|---|
| `(σ₀σ₁)²σ₁σ₀` | `aabbbbb` | `⟨a,b ∣ a²=b⁵⟩` | **T(2,5) = 5₁** |
| `σ₀⁵` | `aaaaabb` | `⟨a,b ∣ a⁵=b²⟩` | T(2,5) ✓ |
| `σ₀³` | `aabbb` | `⟨a,b ∣ a²=b³⟩` | T(2,3) ✓ |

The meson braid closes to the **cinquefoil** — the knot the corpus assigns to the **muon** — and it simplifies from 6 crossings to 5.

## Consequence

Under the volume–density mass law `m(K) = m_e · Vol(K) · ρ(K) / ℏ_q²`, the corpus's own pion braid gives **m_π = 0**. Obstruction A is therefore not a gap in a search that has not been run; it is a property of the construction already written down.

**Diagnosis.** `lepton-meson-parallel` says "the binding Hopf link introduces negative crossings via `σ⁻¹ = σ − h`". That is true in the **Hecke algebra** — `L₋` appears in the normal form with coefficient `h` — but the **braid word is entirely positive**. Negative crossings in a normal-form *coefficient* are algebra, not geometry, and volume sees only the geometry. The construction conflates the two.

## Target volumes (what any candidate must hit)

`ℏ_q² = 0.00981718645427507381` at the proton pin; `Vol·ρ = (m/m_e)·ℏ_q²`.

| meson | m [MeV] | m/m_e | **Vol·ρ needed** |
|---|---|---|---|
| π± | 139.57039 | 273.132 | **2.681392089** |
| K± | 493.677 | 966.102 | **9.484401401** |
| K⁰ | 497.611 | 973.800 | 9.559980444 |
| η | 547.862 | 1072.139 | 10.52539033 |
| D⁰ | 1864.84 | 3649.401 | **35.82684854** |
| J/ψ | 3096.900 | 6060.482 | **59.49688298** |
| η_c | 2983.9 | 5839.347 | 57.3259547 |
| *(μ, for scale)* | 105.658 | 206.768 | 2.029882787 = Vol(4₁) |

## The prune — and a correction to my own first attempt

**First attempt, WRONG.** From a deduplicated enumeration I concluded "no positive 3-braid closure is hyperbolic, so the construction must admit `σ⁻¹`". Tested directly: of **2044** positive words on `{σ₀,σ₁}` of length 2–10, **208 have hyperbolic closures**. The claim is false; the sample was deduplicated by volume and length-limited, which under-represented positive words. Recorded because it is the shape of error this corpus keeps punishing — an inference from a filtered sample, presented as structural.

**What survives, and it is sharper.** The measured minimum hyperbolic volume over positive 3-braids (length ≤ 10) is **4.851171**. The pion needs **2.681**. So *at ρ = 1* the pion's target lies **below the entire positive-braid hyperbolic spectrum**, while mixed-sign words reach 2.0299 (`4₁`, at `(σ₀σ₁⁻¹)²`) and 2.8281 (`5₂`). This is a **conditional** prune — `ρ` is the per-block density and is not 1 in general — so it constrains `(braid, ρ)` jointly, not the braid alone.

Smallest hyperbolic volumes found, 3-braid words length 3–8 (30 distinct volumes):

| Vol | comps | word |
|---|---|---|
| 2.029883213 | 1 | `[1,-2,1,-2]` (4₁) |
| 2.828122088 | 1 | `[1,1,1,2,-1,2]` (5₂) |
| 3.663862377 | 2 | `[1,1,-2,1,-2]` (Whitehead) |
| 4.059766426 | 2 | `[1,1,1,1,2,-1,2]` |
| 4.124903252 | 1 | `[1,1,1,2,-1,-1,-1,2]` |
| 7.327724753 | 3 | `[1,-2,1,-2,1,-2]` (Borromean) |

## A rigorous exclusion at the dictionary's own crossing count

The meson crossing dictionary (`lepton-meson-torus-knot-dictionary.lean`) fixes
each meson's crossing count as the sum of the two generation windings. Reading
that as the braid-word length and comparing with the maximum hyperbolic volume
attainable at that length:

| meson | dictionary crossings | max hyperbolic Vol at that length | Vol·ρ needed | verdict |
|---|---|---|---|---|
| π | `ū(3)+d(3)` = 6 | 7.32772 | 2.681 | reachable |
| K | `ū(3)+s(5)` = 8 | **12.35091** *(exhaustive)* | 9.484 | reachable |
| η/φ | `s̄(5)+s(5)` = 10 | ≥ 14.334 | 10.525 | reachable |
| **D⁰** | `c̄(5)+u(3)` = 8 | **12.35091** *(exhaustive)* | **35.827** | **short by 2.9×** |
| **J/ψ** | `c̄(5)+c(5)` = 10 | ≥ 14.334 | **59.497** | **short by ≥ 4.2×** |

**The length-8 row is exhaustive, not sampled.** All `4·3⁷ = 8748` words on
`{σ₀^{±1}, σ₁^{±1}}` of length 8 with no adjacent cancellation were enumerated;
the maximum hyperbolic volume over all of them is `12.35091`, attained at
`[1,-2,1,-2,1,-2,1,-2]`. Length 9 was likewise exhaustive (`4·3⁸ = 26244`).

So **no 3-braid word of the D meson's own dictionary length can carry its mass**,
whichever word is chosen. This is a scope-(a) exclusion — of *this length at this
density*, not of the hyperbolic mechanism — and it is independent of the
knot-vs-link question below.

**Two assumptions it rests on, both stated rather than assumed away:** that `ρ = 1`
(the per-block density is not 1 in general, and a large `ρ` would relax the
requirement proportionally), and that the dictionary's crossing count is the braid
*word length* rather than the closure's minimal crossing number. Either could
dissolve the exclusion, which is exactly why both are flagged for the author.

**Max hyperbolic volume by word length** (lengths 4–9 exhaustive; 10–18 sampled at
6000 random words each, so those rows are **lower bounds** on the true maximum):

| len | 4 | 5 | 6 | 7 | 8 | 9 | 11 | 14 | 18 |
|---|---|---|---|---|---|---|---|---|---|
| max Vol | 2.030 | 3.664 | 7.328 | 8.997 | 12.351 | 13.948 | ≥17.301 | ≥19.167 | ≥25.773 |

Growth is roughly `1.5–1.7` per letter at the top end, so on that trend D⁰ would
need `L ≈ 24` and J/ψ `L ≈ 40` — three to four times their dictionary lengths.

## Knot or link? The dictionary already decides it — and relaxing does not help

Component count of a closed 3-braid is **forced by word-length parity**. A length-`L`
word in `σ₀,σ₁` is a product of `L` transpositions in `S₃`; even `L` gives an even
permutation (identity or a 3-cycle ⇒ **1 or 3 components**), odd `L` gives a
transposition (⇒ **exactly 2 components**). Measured exhaustively, no exceptions:

| word length | 6 | 7 | 8 | 9 |
|---|---|---|---|---|
| components observed | 1, 3 | 2 only | 1, 3 | 2 only |

**The winding dictionary forces even length.** Meson crossings `= n₁ + n₂` with
`n ∈ {3,5,7}` — all odd — so the sum is **always even**. Therefore:

> **A `q̄q` meson can never close to a 2-component link at its dictionary crossing
> count.** The parity of the generation windings forbids it structurally.

So "may the meson be a link?" is not free: allowing a 2-component link means giving
up either the `n ∈ {3,5,7}` windings or the `n₁+n₂` crossing rule. One or the other,
not both.

**And relaxing to links does not rescue the heavy mesons anyway.** At the same
length the knot achieves the *higher* volume:

| len | max Vol, 1-comp | max Vol, 2-comp | max Vol, 3-comp |
|---|---|---|---|
| 6 | 5.6930 | — | 7.3277 |
| 7 | — | 8.9974 | — |
| **8** | **12.3509** | — | 10.6670 |
| 9 | — | 13.9484 | — |

At length 8 the maximum over **every** component count is `12.3509`, attained by a
**knot** (`[1,-2,1,-2,1,-2,1,-2]`); the 3-component maximum is lower. So the D-meson
exclusion above is unaffected by the relaxation — it holds over knots *and* links.

## Convention audit: which blockers are C-frame?

The parent audit is dated **2026-08-02**, before the **2026-08-15** convention-D
ruling, so its content is presumptively convention-C-frame and each blocker needs
classifying rather than inheriting.

| blocker | depends on `z`? | status |
|---|---|---|
| Route 1 — Y-junction ⇒ `B₂` abelian ⇒ `Vol = 0` | **no** — pure topology | stands, convention-independent |
| Route 2 — D-meson Frobenius–Gram LP is charm-degenerate | **YES** — the Gram matrix is built from the Markov parameter `z` | **C-frame; needs re-derivation under D** |
| winding dictionary (`crossings = n₁+n₂`) | **no** — 0 `z`-references in the Lean | stands |
| `signedWrithe` / `T₃` / `orderedContent` | **no** — 0 `z`-references in the Lean | stands |
| this document's volume + mass-target work | **no** — topology plus `q₀`; `z` never enters | stands |

**Route 2 is the one C-frame blocker**, and it is doubly dead: besides the
convention question, `MesonOperatorSelectionT3.graded_D_kaon_distinct` already
separates D̄⁰ from the kaon, which is what Route 2 concluded could not be done.
Under convention D the Gram matrix also carries the known singularity (`qou-cds2`),
so re-deriving it is not a free re-run.

**Nothing in the live obstruction routes through `z`.** `q₀` is the substrate
modulus and is convention-independent; the Markov parameter `z` is what conventions
C and D disagree about, and it appears nowhere in the volume or mass-target chain.

## 🛑 ρ is NOT a free parameter — and my "at ρ = 1" framing was misleading

Everything above was normalised at `ρ = 1`, flagged as a caveat. That was too
weak a statement: `ρ` is defined in the corpus, it is **not** 1, and there are
**two inequivalent readings** with an open RED gate between them
(`mass_vol_density.py`).

| reading | definition | value at q₀ |
|---|---|---|
| **ρ_global** | `(3q² + 4 + 3q⁻²)/4 = 5/2 + 3h²/4` — the H₄ Family-A linking-weight scalar, SU(2)-**blind** | **2.53277965639939149** |
| **ρ_per-block** | `tr_M(K, q) = Σ_λ y_λ χ^λ(β_K)` — the **knot's own Markov trace**, SU(2)-**selective** | braid-dependent, **≲ 1** (measured) |

`compare_density_readings` reports the two as differing by **≈2.378×** for the
proton and the discipline gate is **RED** — an acknowledged, untuned discrepancy
("NO fudge is applied — the discrepancy is reported, not tuned away").

**The per-block reading makes this a one-unknown problem, not a two-parameter
fit.** If `ρ = tr_M(K)`, then the braid determines *both* factors and the
constraint is a single equation:

$$\mathrm{Vol}(K)\cdot \mathrm{tr}_M(K) = (m/m_e)\cdot \hbar_q^2$$

Measured over the hyperbolic candidates (`tr_M` at H₃, proton pin):

| braid | Vol | tr_M | **Vol·tr_M** |
|---|---|---|---|
| corpus `𝔐 = (σ₀σ₁)²σ₁σ₀` | 0 | 0.6870996474 | **0** |
| `4₁` `[1,-2,1,-2]` | 2.029883 | 0.2801956423 | 0.56876443 |
| `5₂` `[1,1,1,2,-1,2]` | 2.828122 | 0.4869843458 | 1.3772512 |
| Whitehead `[1,1,-2,1,-2]` | 3.663862 | 0.6195656517 | 2.2700033 |
| Borromean `[1,-2,1,-2,1,-2]` | 7.327725 | 0.9985621638 | 7.3171887 |
| `[1,-2,1,-2,1,-2,1,-2]` (max-Vol at L=8) | 12.350906 | 0.2159008098 | 2.6665707 |

**`tr_M ≲ 1` throughout, so `Vol·tr_M ≤ Vol`: the per-block density SUPPRESSES.**

### The two readings give opposite verdicts on the D meson

| reading | Vol the D⁰ needs | max Vol at L = 8 (exhaustive) | verdict |
|---|---|---|---|
| ρ_global = 2.5328 | 35.827/2.5328 = **14.14** | 12.351 | short by **1.15×** — nearly reachable |
| ρ_per-block ≲ 1 | **≳ 35.8** | 12.351 | short by **≥ 2.9×** — firmly excluded |

So **B2's answer is gated on the corpus's own open RED gate**, not on anything I
can settle by measuring. Under the global scalar the D meson is marginal; under
the paper-canonical per-block trace it is excluded.

**Do NOT read the `Vol·tr_M = 2.6665707` row against the pion's `2.681392` (0.55 %)
as a result.** It is the nearest point of an enumerated set to a target, which is
precisely the per-state fit this document exists to avoid. It is listed because
suppressing it would be worse, not because it is evidence.

## ✅ RESOLVED from the corpus: "crossings" means BRAID WORD LENGTH

I listed this as an open author question — *"is the dictionary's crossing count
the braid word length or the closure's minimal crossing number?"* — and said it
could not be settled from the corpus. **It can. The corpus states it outright**,
in the docstring of `mesonCrossingCount`
(`lepton-meson-torus-knot-dictionary.lean`):

> *"Meson crossing count: the total crossings **in the meson braid word**
> = n₁ + n₂ where n₁, n₂ are the quark torus-knot indices."*

Braid **word**, not closure. And it is self-consistent on both sides of the
dictionary:

| object | word | word length | dictionary count |
|---|---|---|---|
| electron | `σ₀³` | 3 | `leptonTorusKnotIndex 0 = 3` ✓ |
| muon | `σ₀⁵` | 5 | `leptonTorusKnotIndex 1 = 5` ✓ |
| pion `𝔐` | `(σ₀σ₁)²σ₁σ₀` | **6** | `mesonCrossingCount 0 = 6` ✓ |

The divergence between word length and crossing number is real but does not
affect the reading: `𝔐` has word length 6 and its closure has crossing number 5,
and it is the **6** that the dictionary means.

**Consequence: the D-meson exclusion above is on the correct footing.** Comparing
the dictionary's count against the maximum hyperbolic volume attainable at that
*word length* is the right comparison, so that assumption is discharged. **`ρ` is
now the only open gate on B2.**

## ✅ B2 SETTLED: **both** ρ readings exclude the D meson — exhaustively

I claimed `tr_M ≲ 1` from six hand-picked braids and leaned the per-block verdict
on it. **That was wrong**: over all hyperbolic 3-braid words of length 8, `tr_M`
ranges over `[−0.055099, 1.438364]` — it exceeds 1 and goes negative. Generalising
from six samples, again.

Computing the product exhaustively — the quantity that actually matters — makes
the result **stronger**, and removes the dependence on the ρ ruling:

| word length | hyperbolic words (exhaustive) | `tr_M` range | **max `Vol·tr_M`** | attained at |
|---|---|---|---|---|
| 6 | 168 | `[0.052755, 1.162424]` | **7.317189** | `[1,-2,1,-2,1,-2]` (Vol 7.32772, tr_M 0.998562) |
| 8 | 2972 | `[−0.055099, 1.438364]` | **11.529406** | `[1,1,-2,-2,1,1,-2,-2]` (Vol 10.14942, tr_M 1.135967) |

Note the product's maximiser is **not** the volume's maximiser — at length 8 the
max-volume word (`Vol 12.351`) has `tr_M 0.216`, giving only `2.667`. Maximising
`Vol` and maximising `Vol·tr_M` are different problems, which is why the product
had to be computed directly rather than bounded from the two factors.

### The verdict is robust to the ρ ambiguity

| ρ reading | constraint at the D⁰'s dictionary length 8 | exhaustive max at L = 8 | verdict |
|---|---|---|---|
| **ρ_global = 2.5328** (constant) | `Vol ≥ 35.826849/2.5328 = 14.145` | `Vol` max **12.351** | **excluded, 1.15×** |
| **ρ_per-block = tr_M(K)** (braid-dependent) | `Vol·tr_M ≥ 35.826849` | `Vol·tr_M` max **11.529** | **excluded, 3.11×** |

**Both readings exclude the D meson at its own dictionary word length.** So B2 no
longer waits on the ρ ruling — the ruling changes the *margin* (1.15× vs 3.11×),
not the *verdict*. The light mesons remain comfortable: π needs 2.681 against a
length-6 maximum of 7.317; K needs 9.484 against a length-8 maximum of 11.529
(tight, at 82 % of the ceiling).

This is now an exhaustive scope-(a) exclusion over the exact quantity the mass law
uses, at the length the corpus itself assigns — not an extrapolation from a
sampled maximum, and not conditional on an unresolved density convention.

## Route 2 RE-DERIVED under convention D — and my "blocked" verdict was wrong twice

**Correction 1: the LP never needed `G⁻¹`.** I wrote that Route 2 was blocked
because "the LP requires `G⁻¹`" and under D that inverse does not exist. Reading
`prop:operator-selection-lp`, `G` enters **only** as the constraint
`Σⱼ Gᵢⱼ xⱼ ≥ 0` — a matrix-vector product. No inverse anywhere in the program.

**Correction 2: the convention-D replacement exists and is owner-approved.**
`G_PINV` is a genuine Moore–Penrose pseudo-inverse of the singular `G`, verified
here: `rank(G) = 5` of 6, `‖GPG − G‖ = 6.7e-16`, `‖PGP − P‖ = 5.6e-16`, both
`GP` and `PG` symmetric to `<6e-16`. Every remaining `G_INV` reference in the tree
is a comment or a test asserting its absence — no consumer calls it.

### What actually goes wrong, and the fix

Run naively on the full 6-dimensional space the LP **is** degenerate, but through
**LP degeneracy, not a missing inverse**: `Gv = 0` for the radical direction `v`,
so the positivity constraints are blind to `v`, and `t·v = −4.4e-16` — the
objective is blind too. The feasible polyhedron is unbounded in a direction
nothing sees, and the artificial `M_bound = 1e6` is the only thing stopping it:

| | full 6-dim | quotient (`v·x = 0`) |
|---|---|---|
| `‖x*‖` | ~5×10⁵ (at `M_bound`) | **3.130144** |
| active set | `[0]` (degenerate) | **`[0, 1, 4, 5]`** |
| `min(Gx)` | — | `0.00` (positivity tight) |

Quotienting by the radical — the repair the corpus itself prescribes — gives a
finite, non-degenerate optimum. **Route 2 is re-derivable under convention D.**

### The result, and what it does and does not fix

The program is **homogeneous** (linear objective, homogeneous `Gx ≥ 0`, only
`Σx = n_target` inhomogeneous), so `x*(n) = n · x*(1)` exactly — verified at
`n = 1, 2, 3`. The selected direction is

    x*(1) = [−0.61738763, −0.68528704, 1.85198003,
             −0.76065394,  2.05565817, −0.84430958]

> **🛑 RETRACTED 2026-08-24 — "canonical" is wrong, and so is the diagnosis
> below it.** The direction quoted here is **one vertex of at least six**, all at
> objective `0`, occurring in mirror pairs under `σ₀ ↔ σ₁`; which one a solver
> returns is a property of its pivoting rule. Nothing canonical is selected.
>
> The cause is not the radical and not convention D. `b₁ = 𝟏`, so the first row
> of `G` **is** the objective vector `t`, and the Frobenius constraint at `i = 1`
> is `t·x ≥ 0` — the objective bounded below by its own constraint. The optimum
> is therefore identically `0` for every `n`, `q` and convention, and `y₀* = 0`
> follows. `NF(𝓑₃)`, which the corpus tabulates as the optimum, is feasible but
> **not** optimal (objective `0.9986`).
>
> The braid obstruction is likewise sharper than stated below: the real,
> gauge-invariant fact is `rank ρ_std(Φ*) = 1` — singular in the standard block,
> where a braid image is invertible — not `χ_alt = 0`, which is gauge-dependent.
>
> The symbolic closed form, the lattice-membership result and the
> rank-deficiency result all **stand**, as statements about that vertex. Only
> "canonical" and the `χ_alt`-first framing fail. See
> [`2026-08-24-operator-selection-lp-objective-defect.md`](2026-08-24-operator-selection-lp-objective-defect.md).

**So the LP does select a canonical, parameter-free direction in `H₃(q)`.** That
is a real answer to "what fixes the operator".

Two things it does **not** do, both stated because they bound what has been shown:

1. **`primal_obj = 0` and `y₀* = 0` at every target.** The minimum-action operator
   is trace-free, `tr_M(Φ*) = 0`, and the net constraint's shadow price vanishes.
   The dual certificate is therefore **trivial** — the "demand pricing" reading of
   the dual carries no information here, and `n_target` is a pure scale rather
   than a selector.
2. **It selects an ALGEBRA ELEMENT, not a braid.** `Φ* ∈ H₃(q)` is a real linear
   combination of NF basis elements with negative, irrational coefficients. A
   braid word maps *into* `H₃(q)`, but the image of the braid monoid is a
   **proper subset**: not every algebra element is the image of a braid. So the
   LP does not close B3 — going from `Φ*` to a braid word is an inverse problem
   that is not generally solvable, and that gap is precisely Obstruction A.

## Is `Φ*` a braid image? Positive braids: NO. General braids: not found, not excluded.

The LP selects an algebra element; the mass law needs a braid. So the question that
decides whether the two mechanisms can meet is whether `Φ*` lies in the image of
the braid monoid.

**Positive braids — excluded, structurally.** `σᵢ² = hσᵢ + 1` with `h > 0` at
`q₀ > 1`, so every positive-braid image has **non-negative** NF coefficients.
Measured over all **8191** positive words of length 0–12: **0** had a negative
coefficient. `Φ*` has **4 negatives of 6**. So `Φ*` is not the image of any
positive braid, at any scale. Best alignment `|cos| = 0.878` at `σ₀¹¹σ₁`.

This connects directly to B1: the corpus's `𝔐 = (σ₀σ₁)²σ₁σ₀` **is** a positive
braid. That is simultaneously why it closes to a torus knot (`Vol = 0`) and why it
sits in the non-negative cone that `Φ*` is outside. **The corpus's meson braid and
the LP's canonical operator are in provably different regions of `H₃(q)`.**

**General braids — open.** With inverses admitted the sign obstruction disappears
(104,600 of 118,096 words of length ≤ 10 have a negative NF coefficient), and the
best alignment rises to `|cos| = 0.94103284`, at
`σ₀⁷ σ₁⁻¹ σ₀⁻¹ σ₀⁻¹`. **Not 1** — so no braid of length ≤ 10 maps to `Φ*`'s
direction, but 0.941 is not an exclusion either.

**What would settle it.** Braid images lie in the `ℤ[h]`-lattice spanned by the NF
basis (repeated application of `σᵢ² = hσᵢ + 1` and `σᵢ⁻¹ = σᵢ − h` keeps integer
polynomial coefficients in `h`). `Φ*` is the optimum of an LP whose data (`G`, `t`)
is exact rational in `ℚ(q)`, so `Φ*` is algebraic too — it is *not* obviously
outside the lattice, and the question cannot be closed by numerics. Deciding it is
a lattice-membership problem, and it is the sharp form of Obstruction A.

### Harness corrections made along the way, both caught by validation

1. **A first inverse test was void.** `nf_of_word(word)` takes only generator
   indices — **no sign argument** — and a two-call fallback did something undefined
   with the inverses, reporting `anyneg = 0` across 87,380 words. A braid algebra in
   which no inverse ever produces a negative coefficient is impossible, which is how
   it was caught.
2. **The right-multiplication matrices were built from the wrong words.**
   `nf_of_word([0,1])` returns slot 4, whose basis *label* is `(1,0)`: the basis
   tuples index in the reverse order to the word convention, so
   `nf_of_word(list(b_j)) ≠ e_j`. Rebuilt by first solving for the word whose NF is
   `e_j` (`{0:[], 1:[0], 2:[1], 3:[1,0], 4:[0,1], 5:[0,1,0]}`). Post-fix validation:
   **254/254** positive words of length 1–7 reproduce `nf_of_word` exactly, and both
   `σᵢσᵢ⁻¹ = 1` identities hold. The numbers above are from the validated build.

## The lattice question, correctly posed — and the radical in closed form

**First, a correction to how I framed it.** I said the next step was to decide
whether `Φ*` lies in the `ℤ[q,q⁻¹]`-lattice, and implied that was a computation.
**At a numerical `q₀` the question is vacuous**: `ℤ[q₀,q₀⁻¹]` is a countable
*dense* subring of `ℝ` for transcendental `q₀`, so every real vector is
arbitrarily well approximated and "is `Φ*` in the lattice" carries no numerical
content. The question is only meaningful **symbolically**, in `H₃(q)` over
`ℚ(q)`. Any numerical near-miss or near-hit would have been an artifact.

**The radical has a closed form.** `gram.py` records it and it is verified here:

$$v \;=\; \sum_{w} (-q^{-1})^{\ell(w)}\, T_w$$

Measured against the numerical null eigenvector of `G`: `|cos| = 1.0000000000000002`
and `‖G·v‖ = 2.63e-16`. Coefficient by coefficient, with `ℓ = (0,1,1,2,2,3)` on the
NF basis:

| `T_w` | `1` | `σ₀` | `σ₁` | `σ₀σ₁` | `σ₁σ₀` | `σ₀σ₁σ₀` |
|---|---|---|---|---|---|---|
| `(−q⁻¹)^ℓ` | 1 | −0.90091828 | −0.90091828 | 0.81165375 | 0.81165375 | −0.73123371 |
| eigenvector | 1 | −0.90091828 | −0.90091828 | 0.81165375 | 0.81165375 | −0.73123371 |

**So the radical itself IS in the lattice** — its coefficients `(−q⁻¹)^{ℓ(w)}` are
manifestly in `ℤ[q,q⁻¹]`.

### This makes the question finite and decidable

`Φ*` is pinned by six linear conditions, all with coefficients in `ℚ(q)`:

- four tight positivity constraints, the active set `[0,1,4,5]` of `Gx ≥ 0`;
- the net constraint `Σx = n_target`;
- the quotient condition `x ⊥ v`, with `v` now known in closed form.

Six equations, six unknowns, all data in `ℚ(q)` ⇒ **`Φ*(q) ∈ ℚ(q)⁶` is the
solution of an explicit linear system.** Whether it lies in `ℤ[q,q⁻¹]⁶` up to
scale is then decided by inspecting the denominators of that symbolic solution —
a finite computation, not a search.

**Not yet run.** `gram.py`'s exact path is `Fraction`-valued *at a numerical `q₀`*,
not symbolic in `q`, so the symbolic `G(q)` and `t(q)` have to be built from the
Hecke structure constants (`σᵢ² = hσᵢ + 1`, `h = q − q⁻¹`, Markov parameter
`z = q³/(q²+1)` under convention D) before the system can be solved. That is the
next concrete step, and it is algebra rather than enumeration.

## Route 2 (superseded blocker note, retained)

Route 2 (the D-meson Frobenius–Gram operator-selection) is the one C-frame blocker
identified above. It **cannot be re-derived by swapping `z`**: bean `qou-cds2`
(in-progress, high, "highest-risk item in the plan") records that under
convention D the Markov–Gram form on the **H₃(q) NF basis** — exactly the basis
the meson lives on — is **SINGULAR**, with one null direction (the row-cap one).

Measured at the proton pin: bilinear eigenvalues `−0.752702, 0, +0.752702 ×3,
+4.230339`; `det = 3.998e-17`; `cond = 4.9e16`. **numpy raises nothing** — it
returns entries up to `7.6e15` with `‖G·G_INV − I‖ = 1.64`, so a naive switch
silently corrupts every consumer of `G_INV`.

The LP requires `G⁻¹`. Under the canonical convention that inverse **does not
exist at H₃**. So Route 2's re-derivation is blocked on `qou-cds2`, which is
owned and in progress — not duplicated here.

## What this does NOT do

No braid is proposed for any meson, and **no mass check was run**. The nearest enumerated volume to the pion target is `5₂` at 5.47 % — that is *not* a result, it is the distance to the nearest point of a dense set, and selecting on it would be the per-state fit the J/ψ attack already recorded as worthless. The J/ψ and D⁰ targets (59.50, 35.83) lie far above anything reachable at these braid lengths, so the candidate space is not even bounded yet at the heavy end.

## Literature

The corpus library (332 documents) carries the volume-conjecture line — Kashaev's quantum-dilogarithm volume (`arxiv-q-alg-9601025v2`), the VC introductions (`arxiv-1002.0126v1`, `arxiv-1003.4808v2`), refined/categorified VC (`arxiv-1203.2182v1`) — but **nothing on the classification or volumes of closed 3-braids**, which is exactly the tool Obstruction A needs.

Externally the relevant results are:

- **Murasugi's classification of 3-braids** up to conjugacy, and **Birman–Menasco**'s solution of the link-type classification for closed 3-braids: a closed-3-braid link type is a single conjugacy class, except for braid index 1–2 and one unexpected infinite family of invertible links with two 3-braid axes. ([Birman–Menasco, *A note on closed 3-braids*](https://arxiv.org/pdf/0802.1072); [*Studying links via closed braids III*](https://msp.org/pjm/1993/161-1/pjm-v161-n1-p02-p.pdf))
- **Murasugi/Schreier normal form**: every 3-braid is conjugate to `Δ^{2ℓ}a^p`, `Δ^{2ℓ+1}`, `Δ^{2ℓ}ab`, `Δ^{2ℓ}(ab)²`, or `Δ^{2ℓ}a^{-p₁}b^{q₁}⋯a^{-p_r}b^{q_r}`. Hyperbolicity is characterised in terms of this form, and **volume bounds for hyperbolic closed 3-braids are expressed in its parameters** — the `r`-syllable count. ([Futer–Kalfagianni–Purcell line: *Cusp areas of Farey manifolds*](https://arxiv.org/pdf/0808.2716); [*Semi-adequate closed braids and volume*](https://arxiv.org/pdf/1406.7337))
- Structural properties of closed 3-braids: nearly fibred, unique incompressible surface. ([*Properties of closed 3-braids*](https://arxiv.org/pdf/math/0606435); [*Closed 3-braids are nearly fibred*](https://arxiv.org/pdf/math/0510243))

**These are search-result summaries, not read papers** — I did not fetch the FKP theorem statements, so the exact volume-bound constants are not quoted here and must be checked before use. `search_arxiv` returned empty for every query including "knot theory", i.e. the tool is not reaching arXiv; this came from web search instead.

**Why the normal form is the right next tool.** It replaces "search the braid space" with "solve for the syllable parameters `(ℓ, p_i, q_i)` that a target volume admits". That is a formalize-first prune of exactly the sanctioned kind — narrow the class first, then check once — rather than a scan that lands on `m_D`.

## Open question for the author

Whether the meson braid must be a **knot** (1 component) or may be a **link**. The corpus's `𝔐` closes to a knot, but `q̄q` is a two-constituent state, and the two-component hyperbolic candidates (Whitehead 3.664, and 2-component words at 4.060, 4.749, 6.138) are otherwise inaccessible. This changes the candidate space before any search, so it wants deciding first.

## 🛑 SETTLED symbolically: the LP-selected operator is NOT a braid — and integrality is not why

The previous section left Obstruction A at *"`Φ*` is an algebra element, not a
braid"*, with the natural follow-up **"could it be one?"** open. It is now
closed, symbolically and gauge-invariantly, by
[`computations/meson/operator_selection_lattice_symbolic.py`](../../computations/meson/operator_selection_lattice_symbolic.py).

### `t(q)` and `G(q)` are DERIVED, not copied

The probe does not take `TR_M` from `pyhecke.gram`. It derives the
Markov–Ocneanu–Wenzl trace from the H₃(q) **structure constants**
`C[i][j] = NF(Tᵢ·Tⱼ)` — i.e. from the Gröbner–Shirshov reduction itself —
by imposing the three defining conditions and solving the resulting linear
system:

| condition | statement |
|---|---|
| **(N)** normalisation | `t(1) = 1` |
| **(C)** cyclicity | `t(TᵢTⱼ) = t(TⱼTᵢ)` for all `i,j` |
| **(M)** Markov | `t(x·σₙ) = z·t(x)` for `x ∈ Hₙ` |

The solution is unique and comes out as
`t = [1, z, z, z², z², h z² + z]`, which is checked against the shipped
`pyhecke.gram.TR_M` — so that constant is a **verified consequence** here
rather than an input. `G(q)` is then `t(Tᵢ·Tⱼ)`, also straight from the
structure constants. The only convention-dependent input to the whole probe
is the single scalar `z = q³/(q²+1)`.

### Why this is a computation and not a search

At the optimum four positivity constraints are tight (active set `[0,1,4,5]`,
measured), so `Φ*` solves **six linear equations in six unknowns whose
coefficients are rational functions of `q`** — the four tight rows of `Gx = 0`,
the net constraint `Σx = 1`, and the quotient condition `v·x = 0`. Solving over
`ℚ(q)` rather than at a pin turns every downstream question into algebra.

Established symbolically over `ℚ(q)` (not merely at `q₀`):

| fact | value |
|---|---|
| `det G(q)` | **`0`** — the convention-D singularity of `qou-cds2`, exact over `ℚ(q)` |
| `rank G(q)` | **5** of 6 |
| `G(q)·v(q)` | **`0`** — the closed-form radical `vᵢ = (−1/q)^{ℓ(wᵢ)}` |

### `Φ*(q)` in closed form

$$x_0 = \frac{-q^3}{D},\quad x_1 = \frac{-q^4}{D},\quad x_2 = \frac{q^6+q^2+1}{D},\quad x_3 = \frac{-q^5}{D},\quad x_4 = \frac{q^7+q^3+q}{D},\quad x_5 = \frac{-q^6}{D}$$

with

$$D(q) = q^7 - q^5 - q^4 + q^2 + q + 1 = (q+1)\,(q^6 - q^5 - q^3 + q^2 + 1).$$

Evaluated at the proton pin in mpmath at 60 dps this reproduces the
numerically-solved LP direction to `4.6e-9` — the LP reference is quoted to
8 decimal places, so that is agreement, not a discrepancy.

### The lattice question: NOT the obstruction

Clearing the common denominator gives the integral representative
`Ψ(q) = D(q)·Φ*(q)` on the NF basis `[1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀]`:

$$\Psi = \bigl(-q^3,\; -q^4,\; N,\; -q^5,\; qN,\; -q^6\bigr),\qquad N = q^6+q^2+1.$$

Every entry is a polynomial in `q` with integer coefficients, so **`Φ*` lies in
the `ℤ[q,q^{-1}]`-lattice up to the single scale `D(q)`.** Braid images have
Laurent-integral NF coordinates, so integrality was a genuine candidate
obstruction — and it does **not** fire. (Note the chain structure:
`Ψ₁ = qΨ₀`, `Ψ₃ = qΨ₁`, `Ψ₅ = qΨ₃`, `Ψ₄ = qΨ₂` — the whole vector is generated
from `Ψ₀ = −q³` and `Ψ₂ = N` by multiplication by `q`.)

### The character question: this IS the obstruction

Lattice membership is *necessary*, not sufficient — the braid image is a
sub-semigroup of the lattice, not all of it. The sharp question is whether any
element of the **coset** `Φ* + span(v)` is a nonzero scalar multiple of a braid
image. The coset, not the point: on the quotient `x` is defined only modulo the
radical, so a claim about `Φ*` alone would be a gauge artifact.

Wedderburn settles it. `H₃(q) ≅ ℚ(q) ⊕ M₂(ℚ(q)) ⊕ ℚ(q)` (sym, std, alt), and a
braid word `w` of exponent sum `e` lands at

$$\chi_{\mathrm{sym}} = q^{e},\qquad \det\rho_{\mathrm{std}} = (-1)^{e},\qquad \chi_{\mathrm{alt}} = (-1/q)^{e},$$

because `σᵢ` has eigenvalues `q` and `−q^{-1}`, so `det ρ_std(σᵢ) = −1`. Hence
**every** braid word satisfies `χ_sym·χ_alt = det ρ_std`, and scaling by `c`
preserves it. Written through the left-regular determinant
(`det L = χ_sym·(det ρ_std)²·χ_alt`) that is the scale-free, exponent-free
invariant

$$F(y) \;:=\; \det L(y) \;-\; \bigl(\chi_{\mathrm{sym}}(y)\cdot\chi_{\mathrm{alt}}(y)\bigr)^{3} \;=\; 0 .$$

The probe verifies `F = 0` on braid words of both signs (including
`σ₀^{-1} = T_{σ₀} − h` and `σ₀^{-1}σ₁`) and on `c·NF(σ₀σ₁)`.

Two measured facts then close it:

1. **`χ_alt(Ψ) = 0`.** Every braid word has `χ_alt = (−1/q)^e ≠ 0`, so `Ψ`
   itself is not a nonzero scalar multiple of one. This is not a coincidence:
   `χ_alt(x) = v·x` exactly, and `v·x = 0` **is** the quotient condition.
2. **The rest of the coset fails too.** With `χ_sym(qv) = 0` — so `χ_sym` is
   constant along the coset — the invariant evaluates to a pure cubic,

   $$F(s) \;=\; -\,s^{3}\,\frac{(q^2+1)^6 (q^2-q+1)^3 (q^2+q+1)^3}{q^{6}},$$

   whose only root is `s = 0`, i.e. `Ψ` itself.

**Verdict — scope (b), structural exclusion, invariant named.** No element of
`Φ* + span(v)` is a nonzero scalar multiple of a braid image. The named
invariant is the Wedderburn identity `χ_sym·χ_alt = det ρ_std`, which holds
identically on `ℚ(q)·image(B₃ → H₃(q))` and is verified on braid words in the
probe. Per the STRICT "refuted" rule this qualifies as (b) rather than (a)
because a *proved* invariant forbids it, not because a numerical search came
back empty.

### What this does and does not say

- It does **not** refute the framework or the operator-selection program. It
  says the convention-D LP, run on the quotient, selects an algebra element
  that no braid realises.
- It **relocates** Obstruction A. The obstruction is not integrality — the
  lattice test above passes cleanly — it is the character structure, and
  specifically the fact that the quotient repair for LP degeneracy is
  *identical* to the vanishing of the alternating character.
- It **sharpens the open question** to: is the quotient the right repair? The
  radical direction `v` is the `q`-antisymmetriser; quotienting by it is what
  makes the LP non-degenerate, and it is also exactly what forbids the answer
  from being a braid. A different repair — a different gauge, a different
  objective, or a formulation that keeps the alternating channel — is where a
  braid-valued answer would have to come from. That is a live derivation
  target, not a refuted one.

## 🛑 STRONGER: Vol = 0 is forced by LENGTH, for the kaon as well as the pion

Everything above about `Vol(𝔐) = 0` was a statement about **one word**. It is
now a statement about **every** word of the relevant lengths, by exhaustive
enumeration —
[`computations/meson/positive_braid_hyperbolicity_by_length.py`](../../computations/meson/positive_braid_hyperbolicity_by_length.py).

`mesonCrossingCount` fixes the dictionary crossing counts (pion 6, kaon 8,
eta/phi 10) and its docstring says those are **braid word lengths**, so for a
positive word the candidate set is finite (`2^L` words) and the question is a
complete case check, not a search.

| L | words | hyperbolic closures | fraction | dictionary length |
|---|---|---|---|---|
| 2 | 4 | 0 | 0.0000 | |
| 3 | 8 | 0 | 0.0000 | |
| 4 | 16 | 0 | 0.0000 | |
| 5 | 32 | 0 | 0.0000 | |
| **6** | **64** | **0** | **0.0000** | **pion** (ū 3 + d 3) |
| 7 | 128 | 0 | 0.0000 | |
| **8** | **256** | **0** | **0.0000** | **kaon** (ū 3 + s 5) |
| 9 | 512 | 18 | 0.0352 | |
| 10 | 1024 | 190 | 0.1855 | eta/phi (s̄ 5 + s 5) |

Total 208 of 2044 — **reproducing exactly** the independently-measured figure
in the retraction section above, which is the cross-check that the two runs
used the same closure object.

**The first hyperbolic positive closure appears at length 9.** So for every
positive 3-braid word of length ≤ 8 the closure has `Vol = 0`, covering the
pion *and* the kaon at their dictionary lengths, exhaustively.

**Consequence.** The pion's `Vol = 0` is not a property of the particular word
`def:categorical-meson` chose — it is forced by length together with
positivity. No other positive 6-crossing word fixes the pion, and no other
positive 8-crossing word fixes the kaon. Exactly one of the following must
give:

1. the meson braid admits negative crossings **geometrically** — not merely as
   normal-form coefficients via `σ⁻¹ = σ − h`, which is the conflation
   diagnosed above;
2. the dictionary counts are not braid **word** lengths (but `mesonCrossingCount`
   says they are);
3. the mass law does not read `Vol` off the closed braid.

### Control: it is POSITIVITY, not length

Same sweep over words in `{σ₀, σ₀⁻¹, σ₁, σ₁⁻¹}`, which separates the two
candidate explanations:

| L | words | hyperbolic | fraction | min Vol | max Vol |
|---|---|---|---|---|---|
| 4 | 256 | 4 | 0.0156 | 2.0298832 | 2.0298832 |
| 5 | 1024 | 20 | 0.0195 | 3.6638624 | 3.6638624 |
| **6** | **4096** | **232** | **0.0566** | **2.0298832** | **7.3277248** |

Mixed-sign words are already hyperbolic at **length 4** (`4₁`), and at the
pion's own length 6 they give 232 hyperbolic closures spanning
`2.0298832 … 7.3277248` — a range that **brackets the pion's target
`2.681392089`** — while positive words of that same length give **0 of 64**.

So **length is not the culprit; positivity is.** Route 1 above (negative
crossings entering geometrically) is not merely one of three possibilities —
it is demonstrably available at the required length, which the other two are
not shown to be.

**This is not a result about the pion.** Bracketing a target is not hitting it,
and choosing the nearest enumerated volume is precisely the per-state fit this
document exists to avoid. What is shown is that the candidate space is
non-empty. Nothing is proposed.

### The chiral-limit reading is wrong — recorded because it is tempting

A reader will notice that `m_π = 0` is also what QCD gives in the chiral limit
— the pion is a pseudo-Goldstone, `m_π² f_π² = −2 m_q ⟨q̄q⟩` — and be tempted
to read `Vol(𝔐) = 0` as that physics rather than as a defect. **It is not.**

The same computation gives `Vol = 0` for the **kaon**, and the kaon is not a
pseudo-Goldstone of the SU(2)×SU(2) subalgebra. In Gell-Mann–Oakes–Renner's own
parametrisation the axial divergence carries the channel index only through
`W_i(c)`, and at `c = −√2` that vanishes for `i = 1,2,3` (pion) and **not** for
`i = 4…7` (kaon) or `i = 8` (eta) —
`library/behavior-of-current-divergences-undersu3su3/`, eq. (2.10) p. 2197;
the modern form is in `library/arxiv-0908.3425v1/` (Scherer, p. 27) and
`library/arxiv-hep-ph-9502366v1/` (Pich, eq. 3.27). A mechanism that zeroes the
pion *and* the kaon is not the chiral limit; it is a degeneracy of short
positive braids.

### Method note — the axis trap, which inverts this result

`snappy.Manifold("braid[…]")` builds the closed braid **together with its braid
axis**: one extra cusp, a different manifold, a larger volume.
`snappy.Link(braid_closure=w).exterior()` is the closed braid alone.

| object | `braid[…]` | `Link(braid_closure)` |
|---|---|---|
| Borromean `(σ₀σ₁⁻¹)³` | 4 cusps, 12.179299277 | **3 cusps, 7.32772475342** ✓ |
| figure-eight `4₁` | 2 cusps, 8.1195328513 | **1 cusp, 2.02988321282** ✓ |
| pion `𝔐` | 2 cusps, 4.0597664256 | **1 cusp, Vol = 0**, degenerate after 30 randomizations |

Using the `braid[…]` spec makes **54 of 64** length-6 words look hyperbolic and
would invert the table above. I built one throwaway script that way and it
reported the pion braid as hyperbolic with volume 4.0597664256 — caught only
because it contradicted a result already merged. The probe now asserts both
controls against their exact known volumes before printing anything else.

---

## Addendum 2026-08-25 — the tool is in the library, and the heavy end IS bounded

Probe: [`meson_braid_syllable_bound_probe.py`](../../computations/meson/meson_braid_syllable_bound_probe.py)
(witness `meson-braid-syllable-bound.witness.json`, 3 assertions, all passed).
Bean `qou-qpj9`.

This document's §Literature records two things. One is a caveat that has now
been discharged; the other is wrong.

> *"These are search-result summaries, **not read papers** — I did not fetch
> the FKP theorem statements, so the exact volume-bound constants are not
> quoted here and **must be checked before use**."*

> *"The corpus library (332 documents) … carries the volume-conjecture line …
> but **nothing on the classification or volumes of closed 3-braids**, which is
> exactly the tool Obstruction A needs."*

**The library does carry it.** [`library/arxiv-1406.7337v4/`](../../library/arxiv-1406.7337v4/)
is Giambrone, *Semi-Adequate Closed Braids and Volume* — **the same arXiv id
this section links** as an external web-search result it could not fetch —
sectioned and greppable. The checking-before-use is done here from the ingested
copy.

### What the paper says, read rather than summarised

| result | statement |
|---|---|
| **Thm 1.2** | for a certain A-adequate closed **3-braid** diagram, `v₈·(s−1) ≤ vol(S³∖K) < 4v₈·s` |
| **Thm 3.1** | `s = t₋(D) = #{negative syllables in β}` — read **off the original braid word** |
| **Lem 2.1(1)** | every negative exponent satisfies `rᵢ ≤ −3` |
| **Cor 1.1** | volume also bounded by the stable penultimate coefficient `β′_K` of the **colored Jones polynomial** |

`v₈ = 4·Catalan = 3.66386237671…` is the regular ideal **octahedron**, and
`2·v₈ = 7.32772475342` is this corpus's own `Vol(Borromean) = 8G` — verified as
an assertion, because the first draft of the probe wrote `v₈ = 8·Catalan` and
that assertion is what caught it. Right constant, wrong coefficient: the same
trap AGENTS.md flags for `Λ` vs `Cl₂`.

### Consequence 1 — this document's diagnosis becomes structural

Sublemma 2.1's own proof:

> *"Condition (2a), Condition (2b), and Condition (2c) of Lemma 2.1 imply that
> **β cannot be positive**. Because positive syllables of β are cyclically
> neighbored by negative syllables…"*

— and per Prop. 2.1 that neighbouring **is** Stoimenow's classification of
A-adequate closed 3-braid diagrams. So a fully positive 3-braid word is
*structurally excluded* from the family, with `s = 0`.

The corpus braid `𝔐 = (σ₀σ₁)²σ₁σ₀` is entirely positive: `s = 0`. This
document's *"length is not the culprit; positivity is"* was an empirical
diagnosis from SnapPy; it is now a structural one, and **`s` is the dial**.

*Scoping this correctly:* a positive braid is **outside** the theorem's family,
so Theorem 1.2 does not *apply* to `𝔐` and does not "predict" its measured
`Vol = 0` — it *excludes* it. Exclusion from the hyperbolic family and a
measured zero agree, which is the point, but they are not the same statement.

### Consequence 2 — the heavy end is bounded

> *"the J/ψ and D⁰ targets (59.50, 35.83) lie far above anything reachable at
> these braid lengths, so **the candidate space is not even bounded yet** at the
> heavy end."*

Inverting Thm 1.2 bounds it, and Lem 2.1(1) converts syllables into crossings
(`≥ 3` each):

| meson | `Vol·ρ` | `s` window | ≥ negative crossings |
|---|---:|:---:|---:|
| π± | 2.681 | **[1, 1]** | 3 |
| K± | 9.484 | [1, 3] | 3 |
| η | 10.525 | [1, 3] | 3 |
| D⁰ | 35.827 | [3, 10] | 9 |
| η_c | 57.326 | [4, 16] | 12 |
| J/ψ | 59.497 | **[5, 17]** | 15 |

The pion window is a **single value**: any A-adequate closed-3-braid candidate
for the pion has *exactly one* negative syllable, hence at least 3 negative
crossings — against a current corpus braid with zero and 6 positive crossings.

### Scope

**(a) necessary conditions on a candidate space.** No braid is derived,
proposed, or mass-checked; Obstruction A — a canonical, parameter-free
operation fixing the braid — is untouched and open. A candidate falling outside
Giambrone's family is not excluded by these numbers, merely uncovered by them.

Nothing else in this document is disturbed: its SnapPy measurement, the T(2,5)
identification, the axis-trap method note and the chiral-limit refutation all
stand.

### The one worth chasing next

**Cor. 1.1 bounds the volume by the colored Jones stable penultimate
coefficient** — and this framework computes colored Jones *as Markov traces*
(`J_L(q) = tr_M(ρ(β_L))`). That is a bridge from machinery the corpus already
has to a volume bound, without going through a braid word at all. Not attempted
here.

### Correction to the addendum above, same day — how narrow the family actually is

The addendum states its bounds are *"CONDITIONAL on the target braid lying in
Giambrone's family (nice + Lemma 2.1 + A-adequate)"*. That scoping is correct
and was written before the numbers. What it does **not** say is how restrictive
that family is, and the answer materially weakens the framing *"the heavy end
IS bounded"*.

**Lemma 2.1(1) requires every negative exponent to satisfy `rᵢ ≤ −3`.** The
corpus's canonical words are built from single crossings, `±1`:

| braid | negative exponents | in the family? |
|---|---|---|
| figure-eight `(σ₁σ₂⁻¹)²` — **muon**, `Vol = 2.0299` | `−1, −1` | **no** |
| Borromean `(σ₁σ₂⁻¹)³` — **proton**, `Vol = 7.3277` | `−1, −1, −1` | **no** |
| meson `𝔐 = (σ₀σ₁)²σ₁σ₀` | none | no (positive) |
| trefoil `σ₁³` | none | no (positive) |

**So the family excludes both of the framework's load-bearing hyperbolic
carriers.** The syllable windows remain valid *for the family they are stated
for*, but that family currently contains none of the corpus's own anchor
manifolds, so their physical relevance is an open question rather than an
assumption. Read the windows as *"if a candidate lies in this family, then…"*
— not as a bound on the corpus's candidate space.

**One caveat on the caveat**, in the direction that softens it: Lemma 2.1 is a
condition on a **diagram**, not on a link type. A different braid word for the
same link could in principle satisfy it. Whether `4₁` or the Borromean admit
such a word is not settled here and cannot be settled by inspecting the
canonical ones. So the honest statement is *"the corpus's canonical words are
outside the family"*, not *"these links are outside it"*.

**What this is genuinely evidence for.** There is a structural mismatch between
the framework's braid vocabulary — single crossings, `±1` exponents — and the
hypothesis of the closed-3-braid volume literature, which wants `≥ 3` same-sign
crossings per syllable. That is worth knowing before more of that literature is
imported: it tells you which theorems can apply and which cannot, and it is a
better use of the reading than the windows were.

**Retained.** Consequence 1 is unaffected: positivity excluding a braid from
the A-adequate family is a statement about *positive* words, and `𝔐` is
positive. The `v₈ = 4·Catalan` correction and its tie to the corpus Borromean
volume stand. The prior document's own results are untouched throughout.
