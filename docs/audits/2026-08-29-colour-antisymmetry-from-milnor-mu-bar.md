# Colour antisymmetry from the Milnor invariant: a located route, not a derivation

**Date:** 2026-08-29
**Branch:** `claude/flavour-colour-separation-2026-08-29`
**Beans:** follows `qou-8pl3` gap (ii); serves eightfold open-problem items 4 and 7
**Prior work:** [`2026-08-26-flavour-colour-discriminator-search.md`](2026-08-26-flavour-colour-discriminator-search.md)

## What this is for

The discriminator search settled the negative — `no_object_gate_separates`: no
gate reading only object-level data can separate the colour and flavour triples,
which kills the whole "try another tensor construction on `V`" family. It then
located the discriminator in the **Young-symmetry channel** of `V ⊗ V ⊗ V`, and
named its own circularity in one sentence:

> Assigning colour the antisymmetric channel is an **input, not a derivation**.
> [...] So Result 2 does not establish that flavour and colour differ; it
> establishes that *if* the channel assignment is supplied, a gate can see the
> difference.

and raised the stakes:

> deriving the colour-antisymmetry constraint would settle more than the Young
> symmetriser — it would supply the one input item 4 is missing.

This note supplies a **candidate route** to that input, from an object the
corpus already carries. It does **not** claim the input is now derived; the
remaining gap is stated precisely in §4.

## 1. The corpus already has three of the four ingredients

All three are in [`borromean-quark.md`](../../content/quantum-observable-universe/observations/borromean-quark.md),
none of them added here:

1. **The three link components ARE the three colours.** "The baryon is the
   Borromean link `𝓑₃` of three unknots threaded through the color tubes
   `(r, g, b)`."
2. **`S₃` acts by permuting them.** "The `S₃` permutation symmetry acts on the
   color assignment `(r, g, b)`."
3. **`μ̄₁₂₃` is the invariant that encodes confinement.** "All three pairwise
   linking numbers vanish (the Brunnian property), while the triple Milnor
   invariant `μ̄₁₂₃ = ±1` encodes confinement."

`SecondCrossingInvariant.lean` independently names `μ̄₁₂₃` as the candidate
second crossing invariant for the same reason: on the Borromean baryon every
degree-1 invariant vanishes, so `μ̄` is the first one that does not.

## 2. The missing fourth ingredient is a standard fact, and it is in the library

**`μ̄_{ijk}` is totally antisymmetric in its indices.** Not asserted here —
[`library/0110001v3`](../../library/0110001v3/) (Mellor–Melvin, *A geometric
interpretation of Milnor's triple linking numbers*, AGT 3 (2003)) states it
outright, and derives it:

> The invariants `e_ijk` are antisymmetric in `i` and `j`. Indeed
> `e_ijk + e_jik = ... ≡ 0 (mod δ)`. It follows that `m_ijk` is totally
> antisymmetric.
>
> The familiar fact that the Milnor invariants `μ̄_ijk` are antisymmetric in the
> indices follows immediately from the theorem and the preceding remark.

Total antisymmetry in three indices is exactly the statement that `μ̄₁₂₃`
transforms in the **sign representation** of `S₃`: it is fixed by the cyclic
subgroup `A₃` and negated by every transposition.

## 3. What the four together say

The `S₃` in ingredient 2 and the `S₃` in §2 are the same group acting the same
way — permutation of the three components, which the corpus has identified with
permutation of `(r, g, b)`. So:

> **The invariant the corpus itself says encodes confinement transforms in the
> sign representation of the `S₃` the corpus itself says permutes colour.**

That is a topological fact about the Borromean link, not an import from QCD. It
is the right *shape* for the input item 7 says the chapter does not derive:
colour sitting in the totally antisymmetric channel `λ = (1³)`.

The `±` in the corpus's own `μ̄₁₂₃ = ±1` is, on this reading, not a free
orientation convention but the two elements of the sign representation.

## 4. The gap this does NOT close — stated precisely

Two different statements, and only the first is established:

| | statement | status |
|---|---|---|
| A | `μ̄₁₂₃`, an invariant of the link, transforms in the sign rep of `S₃` | **established** (§2, cited) |
| B | the physical state's **colour channel** is `λ = (1³)` | **not established** |

A is about an invariant of the configuration; B is about which Young channel of
`V ⊗ V ⊗ V` the state occupies. Getting from A to B requires the further
premise that the state's colour content is *read off* `μ̄` — that `μ̄` is not
merely an invariant which happens to be alternating, but the carrier of the
colour degree of freedom. The corpus does not currently assert that, and this
note does not assume it.

**So item 7 is not derived here, and item 4's missing input is not supplied.**
What is supplied is a candidate with its own gap named, and the gap is a single
identification rather than an open-ended search.

Recorded in this form deliberately: the prior audit's Result 2 was careful to
say "located, not established", and the same discipline applies to this one.
An argument that reached B without the identification would be the
arity-conflation failure — a statement about an invariant read as a statement
about a state.

## 5. Why this is worth pursuing anyway

- It replaces "colour antisymmetry is an input" with "colour antisymmetry
  follows from one identification", which is a strictly smaller ask.
- The object is already in the corpus and already load-bearing: `μ̄₁₂₃` is
  `SecondCrossingInvariant.lean`'s candidate for the hypercharge programme's
  missing second invariant. If the identification in §4 holds, the same object
  serves both open problems.
- It is falsifiable in the useful direction: if the framework's colour degree of
  freedom can be shown *not* to be carried by `μ̄`, the route dies cleanly and
  the search returns to the channel assignment.

## Verification

No Lean, no compute, no content block. This note asserts one mathematical fact
(§2) and cites a library source for it rather than re-deriving it, and otherwise
quotes the corpus against itself. The `S₃`-representation reading in §2 is
standard representation theory of `S₃`: the sign representation is the unique
one-dimensional representation on which transpositions act by `−1`, and total
antisymmetry in three indices is that condition.

## 6. A second, independent source of the same sign representation — and it is computed

Added later the same day. The Milnor route above reaches the sign representation
from the **Borromean** side. There is a second route, from the **Bring** side,
and unlike §2 it does not rest on a citation: it is computed, two ways, in
[`computations/probes/bring_cubic_monodromy_probe.py`](../../computations/probes/bring_cubic_monodromy_probe.py).

### 6.1 What was computed

The canonical Bring chiral cubic from the invariant ring,
`f(X, z) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`, has a monodromy
representation `π₁(ℙ¹ ∖ Δ) → S₃` permuting its three sheets. **That
representation is surjective**, so its composite with `sgn` is surjective onto
`{±1}`.

Exact, over `ℚ[z]`, no floating point:

| | fact | consequence |
|---|---|---|
| A1 | `Δ(z) = −(16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16)`, `gcd(Δ, Δ′) = 1` | six **distinct, simple** branch points — the same six the F3 figure locates numerically at residuals `~1e-15` |
| A2 | `f` has no root `az + e` over `ℂ`, the only shape a `ℂ(z)`-root can take (monic over the integrally closed `ℂ[z]`; leading terms force degree 1) | `f` irreducible over `ℂ(z)` ⇒ monodromy **transitive** |
| A3 | the depressed `p(z) = (2z² + z + 2)/3` is coprime to `Δ` | no branch point carries a **triple** root ⇒ every local monodromy is a **transposition** |
| A4 | `Δ` is squarefree of degree 6, hence not a square in `ℂ(z)` | `ℂ(z)(√Δ)` is a genuine quadratic extension |

A2 + A3 give the group: a transitive subgroup of `S₃` containing a transposition
is `S₃`. A4 reaches the same conclusion by a second, independent route and names
the character — `sgn` is cut out by the Vandermonde `√Δ`, and a loop has
`sgn = −1` exactly when it exchanges the two sheets of that double cover.

Cross-checked numerically at 50 dps (mpmath; no float64 anywhere): transport the
three sheets from a common base point `z₀ = 2` out to each branch point, once
around, and back. All six loops return transpositions and together generate
`S₃`. The loop radius is a third of the closest branch-point approach, no
segment comes within `0.108` of a branch point it does not encircle, and the
worst (step ÷ root-separation) ratio over all 21 600 continuation steps is
`0.028` — the nearest-neighbour matching is never a close call.

### 6.2 Why surjectivity is the load-bearing part

The colour coordinates span a 3-dimensional permutation representation, whose
top exterior power `Λ³` is a line carrying `det = sgn`. **Had the monodromy been
only `A₃`**, that line would be a *trivial* representation, "the antisymmetric
channel" would be indistinguishable from the trivial one, and selecting `Alt`
would carry no information at all. The computation rules that out: the Alt
isotype is a genuinely non-trivial line, acted on by `−1` on half the group.

This is the half of `prop:baryon-product-from-alt` that can be *derived* rather
than selected: not that the state sits in `Alt`, but that `Alt` is a real,
non-trivial place for it to sit.

### 6.3 The gap here is narrower than §4's — the corpus supplies the identification

> **🛑 CORRECTED below in §7. This section understates the identification.** It
> says the sheets-to-colour link is carried by a `remark`. It is carried by a
> **proposition**, and the link is now *computed* rather than read. Left standing
> as written, with the correction below it, because the understatement is the
> kind that gets quoted.

§4 named the Milnor route's gap as the premise that `μ̄` *carries* the colour
degree of freedom. The Bring route's corresponding premise — that the three
sheets are the three colour degrees of freedom — is **already asserted by the
corpus**, in [`rem:brings-qou-4tuple`](../../content/quantum-observable-universe/brings-surface/brings-qou-4tuple.md),
three times over and not added here:

> The five homogeneous coordinates `x_j` split into *spacetime* and *color*
> degrees of freedom: `x₀, x₁` spacetime, **`x₂, x₃, x₄` color**.
>
> In the color coordinates `(x₂, x₃, x₄)`, **the `S₃` permutation of the three
> sheets** yields the `SO(3)` holonomy representation.
>
> Its fibre at each point of `M_S` is the color `ℙ¹(ℂ)` **parametrised by the
> three roots of the elliptic cubic**.
>
> At the six branch points (**where color sheets merge**) [...]

So the sheets-to-colour identification is not a premise this note adds; it is
the corpus's own construction. **That does not make it derived.** The carrier is
a `remark` interpreting `def:brings-surface` — an interpretation of a
construction, at the same epistemic level as `borromean-quark`'s "the three
components ARE the three colours", and not a theorem. The honest reading is that
the identification is *supplied* rather than *established*, which is a weaker
claim than derivation and a stronger one than §4's unsupported premise.

What remains genuinely open is unchanged and is statement **B** of §4: that the
physical state occupies the `Alt³` isotype rather than the trivial or standard
one. §6 supplies the line; it does not put the state in it.

### 6.4 Two open questions this raises

1. **Are the two sign lines the same line?** §2 finds a sign representation on
   the Borromean side (Milnor `μ̄₁₂₃` under permutation of components); §6 finds
   one on the Bring side (`Λ³` of the colour coordinates under monodromy). Both
   are the sign representation of an `S₃` the corpus identifies with permutation
   of `(r, g, b)`. Whether they are the *same* `S₃` acting on the *same* three
   objects — or two different `S₃`s that happen to both be there — is not
   settled by either note. If they are the same, the two routes are one route
   with two derivations of its key step, which would be worth a great deal. If
   they are not, the corpus carries two colour `S₃`s and that is itself a
   finding.

2. **`rem:brings-qou-4tuple` says "degree 4" and "three sheets" in one
   paragraph — and Riemann–Hurwitz says which one is describing the fibre.**
   *"The branched covering `π: S → ℙ¹(ℂ)` (degree 4, six branch points)"* sits
   two sentences above *"the `S₃` permutation of the three sheets"*, and a
   degree-4 covering does not have three sheets. This was flagged as unresolved
   when §6 was first written; it is now settled, by computation rather than by
   picking the reading that suits this note (fact **A5** of the probe).

   The fibre curve is unramified over `z = ∞`: substituting `X = zY` and taking
   the leading form gives `Y³ + Y² + Y + 1`, of discriminant `−16 ≠ 0`, so the
   three sheets stay distinct there and *all* the branching is the six finite
   points. Riemann–Hurwitz, `2g − 2 = −2d + b`, then gives:

   | reading | `d` | `b` | forced genus |
   |---|---|---|---|
   | the cubic §6 computes | 3 | 6 | **1** — elliptic |
   | "degree 4, six branch points" | 4 | 6 | 0 |
   | Bring's surface (`g = 4`), trigonal | 3 | 12 | 4 |
   | Bring's surface (`g = 4`), degree 4 | 4 | 14 | 4 |

   So *no* map has degree 4, six branch points **and** genus 4: that triple is
   arithmetically impossible. The only reading consistent with both "six branch
   points" and "three sheets" is the degree-3, genus-1 cover — which is exactly
   what the same remark elsewhere calls **"the elliptic cubic"**, and whose
   three roots it says parametrise colour. The `q → 0` figure block calls the
   same object the "chiral **elliptic** fibre". Genus 1 is what "elliptic"
   means, and the computation returns it.

   **This is good news for §6, not bad:** the object whose monodromy was
   computed is the object the remark identifies with colour. What "degree 4"
   refers to — a different map, or an error — is a question for that block's
   author, and is **not** repaired here.

### 6.5 Scope

Per the (a)/(b) discipline this is a **positive** result, not a refutation: the
sign character of the Bring fibre's monodromy is non-trivial, established by two
independent exact arguments and confirmed numerically. Nothing here is a
structural exclusion of anything, and nothing here derives statement B.


## 7. The sheets ARE the colour tubes — computed, and §6.3 was too weak

Added on the same day, working the §6.4 question. The answer to *"is the
identification supplied or derived?"* is stronger than §6.3 records, and the
route to it is arithmetic rather than exegesis.

### 7.1 What §6.3 got wrong about its own strength

§6.3 cites `rem:brings-qou-4tuple` — a **remark interpreting a definition** —
and concludes the identification is "supplied rather than established". That
was the weakest carrier in the corpus, and not the one that matters.

[`prop:color-elliptic`](../../content/quantum-observable-universe/brings-surface/color-elliptic.md)
is a **proposition**, and it states the colour elliptic equation to be

$$X^3+(z+1)X^2+(z^2+z+1)X+(z^3+z^2+z+1)=0,$$

*the cubic §6 computes*, with `X = (x₂, x₃, x₄)` named in its own text as **the
colour variable**. The identification is at proposition level, in the block that
introduces the object.

### 7.2 The apparent obstacle, and why it dissolves

The colour tubes are not defined off that cubic directly.
[`def:color-tube-fibers`](../../content/quantum-observable-universe/brings-surface/color-tube-fibers.md)
defines `(r_z, g_z, b_z)` as the roots of a **different-looking** cubic,

$$\mathbf{c}^3 + (4z+1)\mathbf{c}^2 + (6z^2+3z+1)\mathbf{c} + (4z^3+3z^2+2z+1) = 0,$$

with `r_z = w₂ − z`, `g_z = w₃ − z`, `b_z = w₄ − z` in the Lagrange resolvents.
Different coefficients, different-looking curve. The colour-tube-cubic block
says it is obtained "by substituting `X = c + z`" — which is a claim, and
checkable rather than quotable.

**It checks, exactly** (fact **A6** of the probe, `sympy` over `ℚ[z]`):

| | |
|---|---|
| chiral cubic with `X = c + z` | `c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1)` |
| the corpus's colour-tube cubic | identical, coefficient by coefficient |
| `disc_c`(tube cubic) | `−(16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16)` |
| `disc_X`(chiral cubic) | **the same polynomial**, not merely a scalar multiple |

A translation of the fibre coordinate is an isomorphism at every `z`. So the two
cubics are one curve, with the same six branch points and the **same monodromy
representation**.

### 7.3 Consequence

**The three sheets whose monodromy §6 computes are `(r_z, g_z, b_z)` — the
corpus's own named colour tubes.** Not an abstract triple carrying an `S₃`
action, not a triple linked to colour by interpretation: the same three roots,
by an exact change of variable, of a curve a proposition calls the colour fibre.

So §6.2's conclusion sharpens. `Λ³` of the span of the colour tubes is a line
carrying `det = sgn`, and the monodromy acting on it is the **full `S₃`**, so
that line is non-trivial. `Alt` is a real place for the state to sit, and it is
`Alt` **of the colour coordinates**, not of a proxy for them.

### 7.4 The §6.4 question, as far as this settles it

**Both sign lines are the sign representation of an `S₃` acting on the same
three labelled objects.** Route 2's is now pinned to `{r_z, g_z, b_z}` by 7.2.
Route 1's is the `S₃` permuting the three `𝓑₃` components, which
`borromean-quark` says are "threaded through the color tubes `(r, g, b)`" — the
same three labels.

Since `sgn` is the unique one-dimensional representation of `S₃` on which
transpositions act by `−1`, any two copies of it are isomorphic. **So "the same
line" holds at the level of representation type, and the corpus carries one
colour `S₃`, not two.** That is the useful half of the §6.4 answer, and it is
the half that says the two routes are not independent evidence — they are one
route with two derivations of its key step.

**What is not settled** is whether the identification is *canonical*: whether
`μ̄₁₂₃` and the Vandermonde `√Δ` are the same function under the corpus's
identification of components with tubes, or merely two sections of isomorphic
lines. That needs the Borromean link realised inside the fibration, which
nothing here supplies. Isomorphic is not equal, and the difference is exactly
where a sign convention could hide.

### 7.5 A tension flagged, deliberately not adjudicated

`prop:color-elliptic` closes by saying the monodromy of `𝓔_z` around the
singular fibres *"recovers the holonomy generators `H₁, H₂`"*. On 2026-08-29
`main` landed `7be95242b9`, correcting `H₁H₂ = σ₁σ₂ : w ↦ (w₃,w₄,w₁,w₂)` to the
double transposition `(1 3)(2 4)` — an order-2 element of a `V₄`, acting on the
**four** Lagrange resolvents `w₁…w₄`.

Two things do not obviously fit, and both are arithmetic:

1. The monodromy computed here is `S₃`, of order 6. `|V₄| = 4` and `4 ∤ 6`, so
   `S₃` contains no `V₄`.
2. The colour triple is `{w₂, w₃, w₄}`, with `w₁ − z` the space-like shift. But
   `(1 3)(2 4)` sends `w₁ ↦ w₃`, so it does not stabilise `w₁` and does not
   restrict to a permutation of the colour triple at all.

These act on different sets — three roots versus four resolvents — so "recovers
`H₁, H₂`" needs a stated map between them, and none is given in the block.
**Adjudicated below in §8**, after reading that remark's own text.


## 8. §7.5 resolved — two findings, one of them internal to a single remark

§7.5 flagged the `H₁,H₂` tension and deliberately withheld a verdict pending
[`rem:holonomy-trefoil`](../../content/quantum-observable-universe/braids-and-knots/holonomy-trefoil.md)'s
own definition. Read, it yields two separate findings. Neither is introduced by
this branch; both are on `main`.

### 8.1 The remark contradicts itself, and needs nothing external to see it

It asserts, four sentences apart:

> The mapping `x ↦ H₁`, `y ↦ H₂` forms an isomorphism
> `π₁(S³ ∖ K_{3,2}) ≅ ⟨H₁, H₂⟩`. Thus, the monodromy group of the branched
> cover is exactly the trefoil-knot group.

and

> The composite holonomy `H₁H₂ : w ↦ (w₃,w₄,w₁,w₂)` is [...] a double
> transposition, hence an involution — and satisfies `(H₁H₂)² = id` on `SO(3)`.

**These are incompatible, by a one-line argument.** Exponent sum is a
homomorphism `B₃ → ℤ` (it is well defined because the braid relation
`σ₁σ₂σ₁ = σ₂σ₁σ₂` has exponent sum 3 on both sides). `σ₁σ₂` has exponent sum
`2 ≠ 0`, so **`σ₁σ₂` has infinite order in `B₃`**. An isomorphism carries it to
an element of infinite order, which cannot be an involution.

The `SO(3)` qualifier does not rescue it. If the relation holds only after the
2-to-1 projection `SU(2) → SO(3)`, then `(H₁H₂)² = ±1` in `SU(2)` and
`(H₁H₂)⁴ = 1`; the element is still of **finite** order, and `⟨H₁,H₂⟩` still
cannot be isomorphic to `B₃`.

So at most one of the two claims stands. Either the map is a **surjection**
rather than an isomorphism — the honest reading, since a monodromy
representation of a knot group is a quotient — or the involution claim is
wrong. The sentence *"the monodromy group of the branched cover is exactly the
trefoil-knot group"* is the one that cannot survive: the monodromy group of a
finite branched cover is finite, and `B₃` is not.

### 8.2 The bridge in `prop:color-elliptic` is unsupported as written

`prop:color-elliptic` closes: *"The monodromy of `𝓔_z` around the singular
fibres [...] recovers the holonomy generators `H₁, H₂`."* Three arithmetic
obstacles, all from the blocks' own statements:

| | |
|---|---|
| **cardinality** | `H₁,H₂` transport **four** spectral modes `w = (w₁,w₂,w₃,w₄)`. `𝓔_z` has **three** sheets. |
| **group order** | the computed monodromy is `S₃`, of order 6. `\|V₄\| = 4` and `4 ∤ 6`, so `S₃` contains no `V₄` — the composite cannot land in the computed group at all. |
| **stabiliser** | by A6 the colour triple is `{w₂,w₃,w₄}` (`r_z = w₂−z`, etc.). But `H₁H₂ : w ↦ (w₃,w₄,w₁,w₂)` sends `w₃ ↦ w₁` and `w₁ ↦ w₃`, so it **does not preserve the colour triple** and does not restrict to a permutation of the sheets. |

"Recovers" therefore needs a stated map between a four-letter action and a
three-letter one, and the block supplies none.

### 8.3 What is *not* established, kept separate

The `w_k` of `rem:holonomy-trefoil` are called "the spectral modes" and run
`w₁…w₄`; the `w_k` of `def:color-tube-coordinates` are "the Lagrange resolvents
of Bring's surface" and run `w₀…w₄`. Same symbol, overlapping indices,
**different cardinality**, and no block states they are the same objects. §8.2's
third row assumes they are — which is the reading most favourable to the
corpus, and is why that row is listed third rather than leaned on. Rows one and
two do not depend on the identification and stand regardless.

### 8.4 Scope

Per the (a)/(b) discipline: **§8.1 is a scope-(b) structural exclusion** — the
invariant is the exponent-sum homomorphism `B₃ → ℤ`, which forbids any
isomorphism onto a group in which `σ₁σ₂` is torsion. **§8.2 is scope-(a)**: the
stated bridge does not go through as written, which is a fact about the
argument, not a proof that no relation exists between the two monodromies.
