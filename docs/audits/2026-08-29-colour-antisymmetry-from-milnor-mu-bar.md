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


## 8. §7.5 resolved — one finding stands, one is RETRACTED, and the retraction is the good news

> **⚠ This section was rewritten at 15:50Z, hours after it was first filed.**
> `main` landed [`7adab17a3d`](https://github.com/litlfred/qou/commit/7adab17a3d)
> *"revert to S3 3-cycle — braid-twist-flip V4 was the wrong def"* at 15:44Z,
> which removed the text §8.2 was built on. Filed at 15:23Z, §8.2 was correct
> about the block as it then stood and is **void** about the block as it now
> stands. It is retracted below rather than quietly edited, because a
> retraction that leaves no trace is how a stale finding gets re-derived.
>
> The ordering is recorded neutrally: this note preceded the revert by 21
> minutes. **No causal claim is made** — `qou-3nva`/`qou-htv4` were working the
> same block independently, and a sibling reaching the same conclusion from
> the other direction is the expected outcome of the parallel-work policy, not
> evidence that one caused the other.

### 8.1 `rem:holonomy-trefoil` contradicts itself — STANDS, unchanged in force

The revert did not touch the two sentences that matter. The block still says:

> The mapping `x ↦ H₁`, `y ↦ H₂` forms an isomorphism
> `π₁(S³ ∖ K_{3,2}) ≅ ⟨H₁, H₂⟩`. Thus, the monodromy group of the branched
> cover is exactly the trefoil-knot group.

and now says:

> The composite holonomy `H₁H₂` acts as a **3-cycle** in the symmetric-group
> holonomy `S₃` [...] and satisfies `(H₁H₂)³ = id` on `SO(3)`.

**The argument is unaffected, because it was never about which finite order.**
Exponent sum is a homomorphism `B₃ → ℤ` (well defined: the braid relation has
exponent sum 3 on both sides), and `σ₁σ₂` has exponent sum `2 ≠ 0`, so it has
**infinite order** in `B₃`. An isomorphism carries it to an element of infinite
order. `(H₁H₂)³ = id` makes it order 3. Before the revert the claim was order 2;
the contradiction is identical either way, and would survive any finite order.

The `SO(3)` qualifier still does not rescue it: through the 2-to-1 `SU(2) →
SO(3)` projection the element is of finite order in `SU(2)` too.

**What cannot stand is "exactly the trefoil-knot group"**: the monodromy group
of a finite branched cover is finite, and `B₃` is not. The honest repair is
**surjection**, not isomorphism — which is what a monodromy representation of a
knot group always is. Scope-**(b)**: the invariant is the exponent-sum
homomorphism, which forbids any isomorphism onto a group where `σ₁σ₂` is
torsion.

### 8.2 The `prop:color-elliptic` bridge — RETRACTED

As filed, §8.2 argued that *"recovers the holonomy generators `H₁,H₂`"* failed
three ways. **All three rested on the reverted `V₄` text, and all three are now
void:**

| filed row | status after `7adab17a3d` |
|---|---|
| cardinality: the `H`s move **four** spectral modes, `𝓔_z` has **three** sheets | **void** — the explicit four-mode formula `w ↦ (w₃,w₄,w₁,w₂)` is gone; the block now states an action on `S₃` |
| group order: `\|V₄\| = 4`, `4 ∤ 6`, so `S₃` contains no `V₄` | **void** — there is no `V₄` claim any more, and a 3-cycle *is* in `S₃` |
| stabiliser: `(1 3)(2 4)` does not preserve `{w₂,w₃,w₄}` | **void** — that permutation is no longer asserted |

§8.3's caution — that the two blocks' `w_k` differ in cardinality and no block
identifies them — is also moot, since the block no longer indexes a four-element
`w`.

### 8.3 What replaces it: the probe corroborates the corrected claim

Better than a retraction. **Fact A7**, computed from the same six loops as A1–A6:

- The six local monodromies are exactly **two distinct transpositions**,
  `(0 1)` and `(0 2)`.
- Composing two distinct ones gives `(2 0 1)` and `(1 2 0)` — **3-cycles, of
  order exactly 3**, in either order.

`rem:holonomy-trefoil` says `H₁, H₂` are the holonomies around **two distinct
branch points**, and that `H₁H₂` acts as a 3-cycle in `S₃` with `(H₁H₂)³ = id`.
Each loop in this probe *is* such a holonomy. **So the corrected block's claim
is exactly what this computation produces** — two transpositions sharing a
letter compose to a 3-cycle, and these do.

That also removes the tension `prop:color-elliptic`'s closing sentence was
flagged for: a 3-cycle sits inside the `S₃` computed here, so "recovers the
holonomy generators" is at least **consistent** with the monodromy, where the
`V₄` reading was not. It is not thereby *derived* — no map is exhibited, and
consistency is weaker than recovery — but there is no longer an arithmetic
obstruction to it. Scope-**(a)**, and the (a) is now positive rather than
negative.

### 8.4 The lesson worth keeping

§8.1 was written via exponent sum rather than "order 2", and survived a change
of the very quantity a more direct argument would have keyed on. §8.2 was
written against three specific quoted numbers and died with them. **Both were
about the same block, filed in the same hour.** When a finding can be stated
against an invariant, state it against the invariant.


## 9. §7.4 answered — isomorphic, but NOT the same section

Added 2026-09-03, five days after §8, and after
[`2026-08-30-statement-b-brunnian-isotype-exclusion.md`](2026-08-30-statement-b-brunnian-isotype-exclusion.md)
had raised the stakes on this question considerably. That note narrowed
statement B to a **single** surviving premise and identified it as this one:

> The only thing still assumed is the identification of the colour degree of
> freedom with link-invariant content, which is the same identification dg07
> §7.4 examines (canonical vs merely isomorphic — "isomorphic is not equal").

### 9.1 The answer

**The two lines are isomorphic as `S₃`-representations, and the identification
between their sections is not canonical.** The separating invariant is the
kernel of `B₃ → S₃` — the pure braid group `P₃`.

Computed exactly in
[`colour_sign_line_pure_braid_probe.py`](../../computations/probes/colour_sign_line_pure_braid_probe.py)
(permutations and reduced free-group words; no floating point, no anchor,
no `q`):

| | fact |
|---|---|
| **F2** | the Borromean rings are the closure of `(σ₁σ₂⁻¹)³`, which lies in **`B₃`** — the same braid group as the colour fibre's monodromy — and is a **pure** braid: its image in `S₃` is the identity |
| **F3** | that braid is nontrivial *as a braid*, by the faithful Artin representation `B₃ → Aut(F₃)`, so `P₃` is not collapsed |
| **F4** | it and the trivial braid share the **same `S₃` image**, hence the same sign character, while their closures — Borromean rings and 3-component unlink — are separated by `μ̄₁₂₃` (`±1` against `0`, cited) |

So the monodromy sign character **factors through `S₃`** and is therefore
constant on pure-braid closures, while `μ̄` is not. Two functions with
different level sets are not the same function, however isomorphic their
targets. Scope-**(b)**: the invariant is named, and it forbids *any* function
factoring through `S₃` from separating two pure-braid closures.

### 9.2 The arity check — F5, and it is load-bearing

The two "sections" do not begin on a common domain. The monodromy sign
character is a function of a **loop** in the base; `μ̄` is a function of a
**link**. They become comparable only by pulling both back along
`loop → braid traced by the three sheets → its closure`, and `B₃` is that
common domain. §9.1 is stated there and is unconditional there.

**What is not established:** that *this* fibration's monodromy image contains a
witnessing pair. Each local monodromy is a half-twist (the branch points are
simple — A1/A3 of the monodromy probe), but that probe records them as
**permutations, not braid lifts**, so the subgroup they generate in `B₃` is
unknown. Were the image's pure part to carry only `μ̄ = 0`, the two would agree
**vacuously** — which would not restore a canonical identification, but would
weaken the practical force of the separation. The next step is to lift the six
local monodromies to `B₃` and compute the subgroup.

Reaching §9.1 without this paragraph would be the arity conflation §4 of this
very note was written to avoid.

### 9.3 CORRECTION to §7.4

§7.4 concluded:

> **So the corpus carries one colour `S₃`, not two — the two routes are one
> route with two derivations of its key step, not independent evidence.**

**The second clause is too strong and is withdrawn.** The first stands: it is
one `S₃`, acting on one set of three objects, and A6 pins that down. But the
two routes carry **different sections** of isomorphic lines, so neither's
evidence transfers to the other and they do not fuse into a single route. What
§7.4 got right was the group; what it over-read was the identification.

### 9.4 What this does not touch

**Statement B and the Brunnian isotype exclusion are unaffected.** That
argument runs entirely on the Milnor side — Brunnian ⇒ pairwise linking
vanishes ⇒ `Sym³` empty; `μ̄` totally antisymmetric ⇒ `Std` empty — and never
invokes the monodromy line. **B-i** (`Alt³` is a non-trivial line) is likewise
untouched, being a fact about the monodromy alone. What is removed is only the
hope that the two could be fused, and with it §7.4's over-reading.

### 9.5 A corpus defect found on the way

[`binding-knots-visual-inventory`](../../content/quantum-observable-universe/knots-particles-confinement/binding-knots-visual-inventory.md)
states four braid words; **three close to the wrong number of components**:

| entry | stated word | closure | needs |
|---|---|---|---|
| gluon / Hopf link | `σ₀σ₁ ∈ B₃` | 1 | 2 |
| electron / trefoil | `σ₀σ₁σ₀ ∈ B₃` | 2 | 1 |
| Higgs / figure-eight | `σ₀σ₁⁻¹σ₀σ₁⁻¹ ∈ B₃` | **1** | 1 |
| proton / Borromean | `σ₀σ₁σ₂σ₀σ₁σ₂ ∈ B₄` | 2 | 3 |

Component count is a braid-word invariant needing no convention beyond which
generator swaps which strands, and both natural readings of the table's
0-indexing give these counts. The `Vol(𝓑₃) = 8G ≈ 7.32772475342` in the same
entry is **exactly** `2·V_oct` and is right — it is the braid words alone.

**No producer consumes any of them** (checked across `computations/`), so the
blast radius is the table's own prose and diagrams. Not repaired here: the
table is 0-indexed while much of the corpus is 1-indexed, so the fix requires
choosing a convention, which is an author call rather than a typo.


## 10. F5's braid half is closed — the image is not confined to the quotient

§9.2 left one residual: the separation is unconditional on `B₃`, but *this*
fibration's monodromy image might still meet `P₃` only trivially, in which case
the two sections would agree **vacuously**. That escape is now narrowed, by
lifting the monodromy from `S₃` to `B₃`
([`bring_monodromy_braid_lift_probe.py`](../../computations/probes/bring_monodromy_braid_lift_probe.py)).

As `z` traverses a loop, the three colour tubes trace a motion of three points
in `ℂ`; that motion **is** a braid, and the permutation §6 recorded is only its
`S₃` image. Tracking at 50 dps and reading crossings off the real-order
projection gives, for all six loops, a **half-twist of exponent sum `−1`** —
which is what theory demands at a simple branch point, so it is a check rather
than a restatement.

**6 of the 15 pairwise products land in `P₃`, and all 6 are nontrivial as
braids** (Artin representation, faithful). So the image is **not** confined to
the `S₃` quotient.

### 10.1 Two defects in the first version of that probe

Recorded because both would have produced a confident wrong answer, and one is
a discipline failure rather than a numerical one.

1. **The docstring promised a guard the code never ran** — "the permutation of
   the recorded word must equal the permutation the earlier probe computed".
   Now implemented, against independent continuation-tracking. The two readings
   label strands differently (real position vs continuation), so literal
   equality is **not** expected; equal cycle type is, and holds on all six.
2. **The base point was on the real axis.** With real `z` the cubic has real
   coefficients, so two roots are complex conjugates with **identical real
   parts**, and the real-order projection is degenerate along the whole
   outgoing segment. It showed up as `min real gap at crossing: 0.0` —
   crossings recorded where none occurred. Base point moved to `2 + i/2`; the
   gap is now `2.55e-7` and the guard asserts it is positive.

The first version's braid words are **superseded, not merely re-run**: they
were read off a degenerate projection.

### 10.2 What is still open

Whether any pure braid in the image has a closure with `μ̄ ≠ 0`. **A nontrivial
pure braid can still have `μ̄ = 0`** — nontriviality in `B₃` and non-vanishing
of a Milnor invariant are different conditions — so the vacuous-agreement
escape is narrowed, not closed. That is a Milnor computation rather than a
braid one, and neither probe does it.

Nothing here disturbs §9.1 (unconditional on `B₃`), §9.4 (statement B and the
Brunnian exclusion untouched), or §9.3's withdrawal.

---

## §11 — §10.2 closed: the monodromy image is all of `B₃`, and `μ̄` separates on it

*Added 2026-09-03. Probe:
[`computations/probes/colour_mu_bar_monodromy_probe.py`](../../computations/probes/colour_mu_bar_monodromy_probe.py) ·
witness `computations/probes/colour-mu-bar-monodromy-probe.witness.json` ·
bean `qou-dg07`.*

§10.2 left one thing open: **a nontrivial pure braid can still have `μ̄ = 0`**,
so the image's pure part being nontrivial narrowed the vacuous-agreement escape
without closing it. Closing it needed a Milnor computation. It turned out not to
need a computation over the image at all.

### 11.1 The finding

The six local monodromies lifted by
[`bring_monodromy_braid_lift_probe`](../../computations/probes/bring_monodromy_braid_lift_probe.py)
give only **two distinct elements** of `B₃`:

| element | loops | word |
|---|---|---|
| `a` | 0, 3, 4 | `σ₁⁻¹` |
| `b` | 1, 2, 5 | `σ₂σ₁⁻¹σ₂⁻¹` |

and those two already generate:

| | word in the loop lifts | reduces to |
|---|---|---|
| `σ₁` | `g₀⁻¹` | `σ₁` |
| `σ₂⁻¹` | `g₀⁻¹ g₁ g₀` | `σ₂⁻¹` |

with `g₀ = a` and `g₁ = σ₁⁻¹σ₂⁻¹σ₁`, loop 5's reduced word, which is `b`
written another way. Both reductions are verified by free reduction in the
probe, not asserted.

> **Corrected 2026-09-03.** This section first said **four distinct braid
> words**, and named loops 0, 3 as the only `a`-loops and 1, 2 as the only
> `b`-loops. Four distinct *reduced words* do appear, but two of them are the
> same *element* written differently: loop 4's `σ₂σ₁σ₂⁻¹σ₁⁻¹σ₂⁻¹` reduces to
> `σ₁⁻¹` by the braid relation, and loop 5's `σ₁⁻¹σ₂⁻¹σ₁` equals `σ₂σ₁⁻¹σ₂⁻¹`.
> **Free reduction cannot see either coincidence** — each needs a braid
> relation — so counting reduced words over-counted the group. The probe now
> decides it with the faithful Artin representation (`same_element_classes`).
>
> **Two generators is a tighter result than four, so the conclusion is
> strengthened, not weakened**, and every downstream statement in §11 is
> unchanged. The correction was contributed by the independent verification on
> PR #6458 and re-derived here before being accepted — a sibling's finding is
> not a primary source any more than a sibling's bean is.

**The two lifts also satisfy `(ab)³ = Δ⁻²`**, where `Δ = σ₁σ₂σ₁` is the half
twist and `Δ²` generates the centre of `B₃` — verified in the probe
(`full_twist_relation`). In angular order the six loops read `ababab`, so this
is the product around all six branch points, and it is the **inverse full
twist, not the identity**.

That is precisely the `B₃` lift of `rem:holonomy-trefoil`'s `(H₁H₂)³ = id`, and
it is the same fact §12.2 uses to demote that block's "isomorphism" to a
surjection: the `SU(2)` map kills the full twist. The two arrived
independently — §12.2 from reading the block against `B₃`'s centre, this from
transporting the six loops — which is worth more than either alone.

So the monodromy image contains both Artin generators, and is a subgroup of `B₃`
by construction. **The image is `B₃`**, and its pure part is all of `P₃`.

Consequently the Borromean braid `(σ₁σ₂⁻¹)³` is an element of the image — the
probe *builds* it from the loop lifts as `(g₀⁻¹ · g₀⁻¹g₁g₀)³` and checks the
reduction, rather than importing it for comparison. Its closure is Brunnian
(every pairwise linking number `0`, so the indeterminacy is `0` and `μ̄₁₂₃` is a
genuine integer) with

```
μ̄₁₂₃ = −1        against  μ̄₁₂₃ = 0  for the identity, also in the image.
```

Both are pure, so both carry sign character `+1`.

**The vacuous-agreement escape is closed**, and closed on `μ̄` itself — the
invariant §4 locates colour antisymmetry in — not on a lower one. The two colour
sign lines agree as sign characters and disagree as sections **on this
fibration**, not merely on `B₃` abstractly (§9.1).

### 11.2 The sampling route says the opposite, and it is wrong

Recorded because it is the more transferable half. Sampling the image is the
obvious way to answer §10.2 and it returns a confident negative:

- all **6 of 6** pure pairwise products of the loop words have a **nonzero**
  pairwise linking number, hence indeterminacy `1`, hence `μ̄₁₂₃ ∈ ℤ/1` — vacuous
  on every one of them;
- a radius-5 Cayley ball on the loop words (**14,801** distinct reduced words)
  contains **100** Brunnian pure elements, and **every one gives `μ̄₁₂₃ = 0`**.

Read alone, that is "the escape stands". It is a fact about **short words**: the
Borromean braid needs 12 generator-letters, so no radius-5 ball can contain it.
A negative from a finite sample bounds the sample. The probe keeps and reports
the scan for exactly this reason, labelled as corroboration rather than
evidence.

### 11.3 Two defects the self-test caught before any result existed

Both were mine, both were caught by the probe's own validation, and neither
reached a witness, an audit doc or a bean.

1. **`μ̄` was written as a sum of its three cyclic readings** —
   `ε₁₂(w₃) + ε₂₃(w₁) + ε₃₁(w₂)`. Milnor's cyclic symmetry makes those three
   **equal**, so the sum triple-counts: the Borromean self-test returned `−3`
   against the known `±1`, an exact factor of 3. The corpus already carries the
   correct single-coefficient form in
   [`gap2_he4_borromean_mu_bar.py`](../../computations/gap2_he4_borromean_mu_bar.py)
   (`mu()`: *"coeff of `X_{i₁}..X_{i_{k−1}}` in the Magnus image of `l_{i_k}`"*)
   and in the tower it cites. A corpus-grep for the summed form finds it in **no
   file but the probe's own first draft**; nothing downstream was contaminated.
2. **Cyclic agreement was then enforced unconditionally.** It holds only *modulo
   the indeterminacy* — the gcd of the pairwise linking numbers — so the fixed
   probe aborted on the first non-Brunnian closure in the image, readings
   `[0, 0, 1]`. This is the same subtlety `gap2_he4_borromean_mu_bar.py` handles
   with `welldef = (g == 0)`; the probe now matches it and enforces literal
   agreement only at zero indeterminacy.

The pattern in both: **a symmetry of an invariant is not an identity you may
apply to its representatives.** Cyclic invariance made three quantities equal
(so summing was wrong) and held only mod gcd (so equality-checking was wrong) —
opposite errors from the same misreading of the same symmetry.

### 11.4 Scope

Not scope-(a). The verdict is a proof of group membership — both Artin
generators exhibited as words in the loop lifts — plus an exact integer
computation on non-commutative power series truncated at degree 2. No floating
point, no anchor, no `q`.

What remains conditional is the **input**: the six loop words come from
`bring_monodromy_braid_lift_probe`'s numerical continuation. That probe is
guarded (adjacent-swap bound, positive real gap at every crossing, cycle type
cross-checked against independent continuation-tracking) but it is numerical.
If those six words are right, §11.1 is exact.

A further consequence worth stating separately, since it is about the Bring
fibration rather than about this arc: **the braid monodromy group of the colour
cover is the full `B₃`**, not a proper subgroup. Every question of the form
"does the image contain such-and-such a braid" collapses to "does `B₃`".

---

## §12 — three corpus fixes the arc surfaced, author-approved 2026-09-03

Recorded here rather than only in the commit, because two of the three change
what a reader is told about objects this audit reasons over.

### 12.1 `binding-knots-visual-inventory` — three wrong braid words

Three of the four stated words close to the wrong number of components.
Verified with `n_components(perm_image(w, n))` from
[`colour_sign_line_pure_braid_probe`](../../computations/probes/colour_sign_line_pure_braid_probe.py):

| entry | was | closed to | needs | now | closes to |
|---|---|---|---|---|---|
| gluon / Hopf | `σ₀σ₁ ∈ B₃` | 1 | 2 | `σ₀² ∈ B₂` | 2 ✓ |
| electron / trefoil | `σ₀σ₁σ₀ ∈ B₃` | 2 | 1 | `σ₀³ ∈ B₂` | 1 ✓ |
| Higgs / figure-eight | `(σ₀σ₁⁻¹)² ∈ B₃` | 1 | 1 ✓ | unchanged | — |
| proton / Borromean | `σ₀σ₁σ₂σ₀σ₁σ₂ ∈ B₄` | 2 | 3 | `(σ₀σ₁⁻¹)³ ∈ B₃` | 3 ✓ |

**Every crossing count is preserved** — Hopf 2, trefoil 3, Borromean 6 — so the
trefoil entry's `3·𝔈_×(q) = (3/2)(q − q⁻¹)` and the Borromean
`Vol(𝓑₃) = 8G ≈ 7.32772475342` are untouched, and no producer consumes the
words. The one entry that was already correct is the only one written in
`(σσ⁻¹)ⁿ` form; the three wrong ones were all all-positive words.

**Corrects the framing this arc gave the finding twice** — in PR #6449's body
and in a session summary — as *"needs an indexing convention choice, the block
being 0-indexed while much of the corpus is 1-indexed"*. It does not. The block
is consistently 0-indexed, both readings had already been measured to give the
same wrong counts, and the replacements are the standard words. Presenting a
mechanical fix as an open convention question is its own kind of error: it
parks work that nobody needed to decide.

### 12.2 `rem:holonomy-trefoil` — the SU(2) map is a surjection, and the braid
statement is now proved

The block asserted an **isomorphism** `π₁(S³∖K_{3,2}) →∼ ⟨H₁,H₂⟩` and supplied
its own refutation two sentences later: it states `(H₁H₂)³ = id`, while in `B₃`
the word `(σ₁σ₂)³` is the full twist and generates the infinite cyclic centre.
The map kills it, so the kernel is nontrivial.

The fix **splits the claim** rather than swapping one word, because the two
halves have opposite verdicts:

- *"the monodromy group of the branched cover is exactly the trefoil-knot
  group"* — **now proved**, by §11: the braid monodromy image is all of `B₃`,
  and `⟨x,y ∣ xyx=yxy⟩ ≅ B₃`. This was previously asserted.
- *"the mapping into `SU(2)` is an isomorphism"* — **false**; it is a surjection
  onto a proper quotient by a subgroup of the centre.

The block's `.ts` gains a `computation:` block pointing at
`colour_mu_bar_monodromy_probe` and its witness, so the newly-proved half is
traceable. A word-swap alone would have read as a retraction of a claim that
the corpus now supports *more* strongly than before.

### 12.3 `rem:brings-qou-4tuple` — the cover is degree 3

*"The branched covering `π: S → ℙ¹(ℂ)` (degree 4, six branch points)"*
contradicted *"the `S₃` permutation of the three sheets"* in the same sentence.
Riemann–Hurwitz with six simple branch points, `2g−2 = −2d + 6`:

| `d` | `g` |
|---|---|
| **3** | **1** — what `bring_cubic_monodromy_probe` A5 measured for the colour cover |
| 4 | 0 |

and Bring's own genus 4 is unreachable at any degree with only six simple
branch points. Corrected to degree 3. The likely source of the slip is the
resolvent basis `(w₁,…,w₄)`, which does supply a genuine degree-4 object —
just not this map. `χ(𝓢) = −6` in that block's Summary is the **state bundle**,
a different object, and is not in question.

### 12.4 Verification, and one defect in this section's own first draft

Pipeline validate ran clean — *"Valid — 9 issue(s)"*, none in these three
blocks (all pre-existing, mostly the documented unknown-field class). It had to
run in an **isolated worktree against a fresh `folio-assistant` clone**: the
shared clone is 338 commits behind `main` and holds 62 files of another
session's uncommitted work, so updating it in place would have destroyed that
work. The render-QA grep battery is clean on all three blocks.

The expository half of the render-QA gate caught a defect in the §12.2 text as
first written: it introduced `Δ²` for the braid full twist, colliding with
`Δ_λ`, the `Δ²g` of the μ₃ door, and the alien derivative `Δ_ω`. The symbol is
gone; the prose names the object instead. This is the notation-collision class
the gate exists for, and it was introduced by the same session that was
auditing for it.

**`qa-sweep` sidecars are NOT refreshed.** The sweep lives in the stale shared
clone and running it there would touch the sibling's tree. All three `.qa.json`
files are stale by source-hash drift and need one sweep once this lands.
