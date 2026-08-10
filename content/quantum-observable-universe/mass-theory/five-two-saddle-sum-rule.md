## A conjecture in this corpus, now a theorem

The saddle sum rule for $5_2$ was carried here as an open statement: a conjecture class with no instance, annotated "the statement is open", alongside a numerical check to eighty digits. Eighty digits is not a proof, and the class had no inhabitant. It does now.

Let $y_1, y_2, y_3$ be the roots of

$$
  X^3 - 2X^2 + 3X - 1,
$$

one real in $(0,1)$ — call it $y_3$ — and a complex-conjugate pair $y_1, \overline{y_1}$.

**Theorem.**

$$
  \mathrm{Li}_2(y_1) + \mathrm{Li}_2(\overline{y_1}) + \mathrm{Li}_2(y_3)
    \;=\; -\frac{\pi^2}{6} \;-\; \frac{1}{2}\log^2 y_3
      \;+\; \frac{2}{3}\bigl(\arg y_1 - \pi\bigr)^2 .
$$

In the flattened form the corpus's conjecture class states, with $V_j = 3\,\mathrm{Li}_2(y_j) + (\log y_j + b_j \pi i)^2$ and flattening signs $b = (-1, +1, +1)$,

$$
  \sum_j V_j \;=\; -\frac{3\pi^2}{2} + 2\pi \log(y_3)\, i,
  \qquad\text{so}\qquad
  \sum_j \mathrm{Re}\, V_j = -\frac{3\pi^2}{2},
$$

a real constant with no dependence on the roots at all.

## How it is proved

Four steps, none of them numerical.

**The five-term identity over $\mathbb{C}$.** For real $a \in (0,1)$ and $w$ off both real cuts, the Rogers dilogarithm satisfies the pentagon $L(a) + L(w) + L\bigl((1-a)/(1-aw)\bigr) + L(1-aw) + L\bigl((1-w)/(1-aw)\bigr) = \pi^2/2$. The derivative vanishes algebraically; the branch defects are holomorphic with vanishing derivative, so they are transported from a real base point where everything is regular.

**The anharmonic group.** Reflection and inversion, together with the four one-logarithm forms, make the $\log^2$ terms cancel *completely*, leaving $\pi^2$ plus $\pi$ times a single logarithm. That total cancellation is what makes the final expression as clean as it is.

**The branch equations.** This is the step that makes the cubic do real work: $y^2 = (1-y)^3$ *is* the defining cubic rewritten, so $\exp\bigl(2\log y - 3\log(1-y)\bigr) = 1$, and a window of width $4\pi$ pins the branch data uniquely. The flattening signs $b$ are not chosen to make the identity come out — they are forced.

**The root data.** The cubic's root structure is bundled and inhabited via the intermediate value theorem and an explicit square root, so the existential in the statement is witnessed rather than assumed.

## What this does not touch, and why it structurally cannot

The $5_2$ **volume** conjecture is untouched, and the reason is worth stating precisely, because it is not "this has not been done yet".

$\mathrm{Vol}(5_2) = 3\,D(y_1)$ concerns the Bloch--Wigner dilogarithm $D$ at a *single* root. The theorem above is an identity over the *whole Galois orbit* — and $D$ **cancels on Galois sums**. A sum over the three conjugates therefore carries no information about $D$ at any one of them. This is not a gap that a sharper version of the same argument would close; the Galois sum is the wrong functional for the question, and no strengthening of it will become a volume statement.

So the two results sit side by side without touching: an exact identity for the dilogarithm over the orbit, and an untouched conjecture about one root of that orbit.

## Scope

The mathematics is not new. The five-term relation is classical, the extended Bloch group and its flattening bookkeeping are Neumann's, and the shape-field setting is Neumann and Zagier's. What the corpus contributes is the machine-checked proof, and the promotion of one of its own conjecture classes from "declared, no instance" to inhabited.

As throughout this arc, nothing here establishes that any triangulation is a triangulation *of* a knot complement, and no volume conjecture is touched.
