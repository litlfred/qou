Each NF basis element of $H_3(q)$ carries a definite writhe
$w$ --- the total number of positive crossings in its braid word:

| Basis | Braid word | Writhe $w$ |
|:---:|:---|:---:|
| $\gamma = \mathbf{1}$ | (empty) | $0$ |
| $\sigma_0$ | $\sigma_0$ | $1$ |
| $\sigma_1$ | $\sigma_1$ | $1$ |
| $L_+ = \sigma_0\sigma_1$ | $\sigma_0\sigma_1$ | $2$ |
| $L_- = \sigma_1\sigma_0$ | $\sigma_1\sigma_0$ | $2$ |
| $e^- = \sigma_0\sigma_1\sigma_0$ | $\sigma_0\sigma_1\sigma_0$ | $3$ |

A colored photon $\gamma_i = \mathbf{1} + \varphi_0\sigma_0
+ \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ therefore
carries content at writhe $0$, $1$, $1$, and $2$.  The coefficient
$\varphi_{01}$ is the **writhe-$2$ content** of the photon: the
amount of Hopf link dressing (twist) it carries.

## When does writhe change?

Tracking the input writhe (sum of the two factors' writhes)
against the output writhe through all 36 entries of the
$T_{1,0}$ multiplication table
([Table L.1](#rem:knot-operator-basis-table)) reveals a sharp
dichotomy.

**Writhe is preserved** when the two factors involve different
generators or when the Yang--Baxter relation applies:

| Product | Input $w$ | Output | Rule |
|:---|:---:|:---|:---|
| $\sigma_0 \cdot \sigma_1 = L_+$ | $2$ | $w = 2$ | Different strands: concatenate |
| $\sigma_1 \cdot \sigma_0 = L_-$ | $2$ | $w = 2$ | Different strands: concatenate |
| $\sigma_1 \cdot L_+ = e^-$ | $3$ | $w = 3$ | Yang--Baxter ($\sigma_1\sigma_0\sigma_1 = e^-$) |
| $L_+ \cdot \sigma_0 = e^-$ | $3$ | $w = 3$ | Yang--Baxter ($\sigma_0\sigma_1\sigma_0 = e^-$) |

In these products, the crossings never collide on the same
strand.  The braid relations (R-III) rearrange strands without
changing crossing count or sign.  Writhe passes through unchanged.

**Writhe drops** when the Hecke relation fires on same-strand
collision:

| Product | Input $w$ | Output (NF) | Writhe content |
|:---|:---:|:---|:---|
| $\sigma_0 \cdot \sigma_0$ | $2$ | $h\sigma_0 + \gamma$ | $w = 1$ and $w = 0$ |
| $\sigma_1 \cdot \sigma_1$ | $2$ | $h\sigma_1 + \gamma$ | $w = 1$ and $w = 0$ |
| $\sigma_0 \cdot L_+$ | $3$ | $h L_+ + \sigma_1$ | $w = 2$ and $w = 1$ |
| $L_+ \cdot \sigma_1$ | $3$ | $h L_+ + \sigma_0$ | $w = 2$ and $w = 1$ |
| $L_+ \cdot L_+$ | $4$ | $L_- + h e^-$ | $w = 2$ and $w = 3$ |

The pattern is consistent: same-strand collision always reduces
writhe.  Two crossings on the same strand partially annihilate
via $\sigma_i^2 = h\sigma_i + \mathbf{1}$.

## The Hecke relation writes and unwrites exactly once

The Hecke relation $\sigma_i^2 = h\sigma_i + \mathbf{1}$ (where
$h = q - q^{-1}$) is a single-step writhe reduction.  It takes
a writhe-$2$ collision ($\sigma_i^2$) and produces exactly two
terms:

- A writhe-$1$ term ($h\sigma_i$): one crossing survives,
  weighted by the Hecke amplitude $h$.
- A writhe-$0$ term ($\mathbf{1}$): both crossings annihilate
  completely, returning the identity.

Each application of the Hecke relation removes exactly one
crossing.  You cannot unwrite two crossings in a single Hecke
step --- the relation is degree-$2$ and produces outputs at
degrees $1$ and $0$, a drop of exactly $1$ and $2$ respectively.

For composite products, the Hecke relation applies iteratively:

- $\sigma_0 \cdot L_+ = \sigma_0^2\sigma_1$: the Hecke relation
  fires once on $\sigma_0^2$, giving
  $(h\sigma_0 + \mathbf{1})\sigma_1 = h L_+ + \sigma_1$.
  Input writhe $3$, output at $2$ and $1$.

- $L_+ \cdot L_+ = (\sigma_0\sigma_1)^2$: the Hecke relation
  fires twice (once on each $\sigma_i^2$ that arises in the
  expansion), giving $L_- + he^-$.
  Input writhe $4$, output at $2$ and $3$.

## Can writhe change without being observable?

No.  Every writhe reduction leaves an observable trace in the NF
decomposition.  When $\sigma_i^2$ reduces, the output is a
**sum** of two terms at different writhe levels.  Both terms
appear in the NF with nonzero coefficients.  There is no
"silent" writhe change --- the Hecke relation always produces
both the reduced-writhe term ($\mathbf{1}$) and the
partially-reduced term ($h\sigma_i$).

Concretely: if two co-polarized photons collide
($\varphi_0\psi_0 \neq 0$), the output has both
$\varphi_0\psi_0\gamma$ (writhe dropped to $0$) and
$\varphi_0\psi_0 h\,\sigma_0$ (writhe dropped to $1$).
Both contributions are visible in the NF.  The writhe
reduction is always a branching event, never a clean
substitution.

This connects to the Reidemeister analysis
([Reidemeister mass invariance](#prop:reidemeister-mass-invariance)):
R-I moves (which change writhe by $\pm 1$) change the binding
energy.  The Hecke relation is the algebraic encoding of this
--- writhe reduction always has an energetic cost, visible as
the $h$-weighted splitting between the two output terms.

## When does writhe not change?

Writhe is preserved in exactly three situations:

1. **One factor is the identity** ($\mathbf{1}$): the identity
   transmits everything unchanged.  No crossings interact.

2. **The two generators act on different strands**
   ($\sigma_0 \cdot \sigma_1$ or $\sigma_1 \cdot \sigma_0$):
   the crossings live in non-overlapping planes and simply
   concatenate.  This is topologically a poke move (R-II) that
   adds crossings without collision.

3. **The Yang--Baxter relation applies**
   ($\sigma_1\sigma_0\sigma_1 = \sigma_0\sigma_1\sigma_0$):
   three crossings rearrange by strand-sliding (R-III) without
   any crossing being created or destroyed.  The writhe is
   $3$ on both sides.

In all three cases, no $\sigma_i^2$ subword appears in the
product, so the Hecke relation never fires.  The crossings
pass through each other or rearrange without annihilating.

## Summary: writhe as a regular isotopy invariant

| Algebra operation | Reidemeister move | Writhe | Observable? |
|:---|:---|:---:|:---:|
| $\sigma_0 \cdot \sigma_1$ (different strands) | R-II (poke) | Preserved | --- |
| Yang--Baxter ($\sigma_i\sigma_j\sigma_i = \sigma_j\sigma_i\sigma_j$) | R-III (slide) | Preserved | --- |
| Hecke ($\sigma_i^2 = h\sigma_i + \mathbf{1}$) | Writhe reduction | Drops by $1$, $2$ | Always (branching into two terms) |

Writhe is a **regular isotopy invariant** (preserved by R-II
and R-III) but not a knot invariant (changed by the Hecke
relation, which encodes same-strand crossing collision).  Every
writhe change is observable as a splitting of the output into
terms at different writhe levels.
