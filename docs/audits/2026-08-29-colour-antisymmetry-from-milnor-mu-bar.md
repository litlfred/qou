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
