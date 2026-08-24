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
