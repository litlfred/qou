# Statement B narrowed: the Brunnian structure excludes Sym³ and Std, leaving only Alt³

**Date:** 2026-08-30
**Branch:** `claude/colour-statement-b-brunnian-2026-08-30`
**Beans:** follows `qou-dg07`; the second half of eightfold open-problem item 7
**Builds on:** [`2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md`](2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md) (§4, §7.4) and PR #6074 (B-i: Alt³ is a non-trivial line, from the computed S₃ monodromy)

## The question this addresses

B-i (PR #6074) derived the *first* half of `prop:baryon-product-from-alt`'s
former "SELECTS the Alt isotype": that **Alt³ is a genuinely non-trivial sign
line** — the colour-tube cubic's monodromy is the full S₃, so the sign character
is surjective onto {±1} and Alt³ is not indistinguishable from the trivial
isotype.

The *second* half — **statement B** — is whether the physical baryon **occupies**
Alt³ rather than the trivial (Sym³) or standard (Std) isotype. The dg07 audit
§4 left this an unsupported input:

> Getting from A to B requires the further premise that the state's colour
> content is *read off* μ̄ … The corpus does not currently assert that.

and named the failure mode to avoid: an "argument that reached B without the
identification would be the arity-conflation failure — a statement about an
invariant read as a statement about a state."

This note does **not** claim to close statement B. It **shrinks** it: two of the
three isotypes are shown to have **provably vanishing** leading link-invariant
content for the Brunnian configuration, so Alt³ is not *selected among three live
options* — it is the *only non-empty channel*. What remains is a single, clearly
isolated premise, strictly smaller than §4's.

## The three isotypes and their leading link-invariant content

The colour degree of freedom is the S₃-module `V ⊗ V ⊗ V` on the three colour
sheets, decomposing as

$$
  \mathrm{Sym}^3 \;\oplus\; \mathrm{Alt}^3 \;\oplus\; \mathrm{Std}^{\oplus 2}
  \qquad (\text{trivial} \oplus \text{sign} \oplus \text{standard}).
$$

The baryon is the **Borromean link** `𝓑₃(ν_r, ν_g, ν_b)`
([`borromean-quark.md`](../../content/quantum-observable-universe/observations/borromean-quark.md)),
whose defining property the corpus states outright:

> All three pairwise linking numbers vanish (the **Brunnian** property), while
> the triple Milnor invariant `μ̄₁₂₃ = ±1` encodes confinement.

The lowest-order link invariants sort by their S₃ transformation, so we can ask
which isotype each populates.

### Sym³ (trivial) — provably empty

The permutation-invariant (trivial-isotype) content at the lowest order is the
**symmetric functions of the pairwise linking numbers** `lk(i,j)`. The Brunnian
property is exactly `lk(i,j) = 0` for all pairs. So every trivial-isotype leading
invariant vanishes: a Brunnian link carries **no symmetric linking content** to
distinguish it from the unlink. There is no Sym³ leading invariant to place the
state in.

### Std (standard, mixed symmetry) — provably empty

At the next order the invariant is Milnor's triple linking number `μ̄_{ijk}`.
For a Brunnian link the pairwise invariants vanish, so `μ̄_{ijk}` is
well-defined with **no indeterminacy**, and (Mellor–Melvin,
[`library/0110001v3`](../../library/0110001v3/)) it is **totally antisymmetric**
in its three indices. Totally antisymmetric under S₃ means:

- the 3-cycles (the subgroup A₃) act **trivially**: `μ̄_{ijk} = μ̄_{jki} = μ̄_{kij}`;
- every transposition acts by **−1**: `μ̄_{ijk} = −μ̄_{jik}`.

That is precisely the **sign character** of S₃ (A₃ → +1, transpositions → −1).
Consequently the space of triple invariants is **one-dimensional** — a single
independent value `μ̄₁₂₃`, spanning the sign line. There is **no second,
mixed-symmetry triple invariant**, so the Std isotype (which is 2-dimensional and
would require independent mixed-symmetry content) has **no leading invariant**
either.

### Alt³ (sign) — non-empty

`μ̄₁₂₃ = ±1 ≠ 0` is the confinement invariant, and it *is* the sign-line
generator. Alt³ is the one isotype with non-vanishing leading link-invariant
content.

## What is derived, and the one premise that remains

| claim | status |
|---|---|
| Alt³ is a non-trivial sign line | **derived** (B-i, S₃ monodromy, PR #6074) |
| Sym³ leading invariant content vanishes for the baryon | **derived** — Brunnian ⇒ all `lk(i,j) = 0` |
| Std leading invariant content vanishes for the baryon | **derived** — the sole triple invariant `μ̄` is pure-sign (Mellor–Melvin), so no mixed-symmetry triple invariant exists |
| the baryon **occupies** Alt³ | **forced modulo one premise** (below) |

The residual premise: **the baryon's colour wavefunction is carried by the
link's leading invariants** — i.e. the colour content is the invariant content,
not independent data laid on top of it. Given that premise, occupation of Alt³ is
**forced**, because the invariants that could place the state in Sym³ or Std
**provably vanish** for a Brunnian link.

This is strictly smaller than the dg07 §4 premise. §4 needed "the state's colour
content is *read off* μ̄" while conceding Alt³ was merely *one* of three symmetry
types the state *could* have — leaving open the worry that μ̄ "happens to be
antisymmetric." That worry is now gone: the other two channels are **not
coincidentally unoccupied, they are provably empty**. The only thing still
assumed is the identification of the colour degree of freedom with link-invariant
content, which is the same identification dg07 §7.4 examines (canonical vs merely
isomorphic — "isomorphic is not equal").

## Scope (per the refuted/ruled-out discipline)

The Sym³ and Std exclusions are **scope-(b) structural exclusions**, each backed
by a proved invariant, not scope-(a) numerical negatives:

- **Sym³**: excluded by the Brunnian identity `lk(i,j) = 0` (a topological
  invariant, the corpus's own confinement condition).
- **Std**: excluded by the total antisymmetry of `μ̄_{ijk}` (Milnor / Mellor–
  Melvin), which forces the triple-invariant space to be the 1-dimensional sign
  line — a dimension/representation-count bound, the permitted kind of (b).

Nothing here derives that the *state vector* sits in Alt³ independently of the
invariant identification; that identification is the named residual, and claiming
occupation without it would be the arity-conflation the dg07 audit warns against.
This note is a **positive** result: it removes two of the three options by proof,
and isolates the one remaining premise.

## Suggested formalization (follow-up)

A Lean lemma would close the representation-theoretic half mechanically: for the
S₃ action on `V^{⊗3}`, a totally antisymmetric tensor lies in the sign isotype
and has **zero** projection onto the trivial and standard isotypes
(`π_Sym(t) = 0`, `π_Std(t) = 0` when `σ·t = sgn(σ) t`). Combined with the
topological inputs (Brunnian ⇒ pairwise = 0; μ̄ totally antisymmetric, cited),
this would make the Sym³/Std exclusion a checked statement rather than a prose
argument. The existing
[`baryon-product-from-alt.lean`](../../content/quantum-observable-universe/predicted-spectra/baryon-product-from-alt.lean)
already carries `signCharacter` and the Vandermonde identity; the projector
lemma extends it. Not done here — flagged so the next pass can pick it up.
