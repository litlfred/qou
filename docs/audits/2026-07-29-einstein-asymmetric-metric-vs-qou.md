# Einstein's asymmetric metric tensor vs QOU

**Date:** 2026-07-29
**Branch:** `claude/qou-einstein-metric-tensor-mfrixn` (PR #4407)
**Question:** what is the relationship between QOU and Einstein's
asymmetric (non-symmetric) metric tensor?

---

## 0. Corpus status — the comparison is absent

Corpus-grep checklist (AGENTS.md §"Before declaring 'open'"), all four
paths run:

| Path | Result |
|---|---|
| `docs/audits/` | no hit for asymmetric metric / non-symmetric gravitation / NGT |
| `content/` (whole tree) | no hit; all "non-symmetric" hits are braiding, Gram matrices, Macdonald polynomials |
| `computations/` | no hit |
| `content/schema/references.ts` | no Einstein unified-field entry; the `Einstein` hits are `einstein1905` (a doc-comment example key), Bose–Einstein condensate papers, and Jacobson's *Thermodynamics of Spacetime* |

Two false friends worth naming up front, both of which would make a
careless grep look like a hit:

1. **"Moffatt" ≠ "Moffat".** [`helicity-conservation.md`](../../content/quantum-observable-universe/fluid-dynamics/helicity-conservation.md)
   cites **H.K. Moffatt**'s fluid helicity. **J.W. Moffat**'s Nonsymmetric
   Gravitational Theory — the modern descendant of Einstein's programme —
   is not in the corpus.
2. **`QOU.Torsion` is arithmetic torsion.** Per
   [`substrate-gm-torsion.md`](../../content/quantum-observable-universe/fluid-dynamics/substrate-gm-torsion.md),
   "torsion" in QOU means the roots-of-unity subgroup
   $\mu_\infty \subset \mathbb{G}_m$ that the substrate section $q$ must
   avoid. It is **not** the antisymmetric part of an affine connection —
   the torsion tensor that Einstein–Cartan and NGT use. Do not let the
   shared word bridge the two frameworks.

So this document records a comparison that did not previously exist.

---

## 1. What Einstein was doing

From 1925, and intensively from 1945 with Straus and Kaufman (and in
parallel by Schrödinger), Einstein pursued a unified field theory by
dropping the symmetry of the metric:

$$
  g_{\mu\nu} \;=\; \underbrace{g_{(\mu\nu)}}_{\text{gravitation}}
              \;+\; \underbrace{g_{[\mu\nu]}}_{\text{hoped: electromagnetism}}
$$

The hope: one geometric object on spacetime unifies gravity and
electromagnetism, with the antisymmetric part $g_{[\mu\nu]}$ playing the
role of the Maxwell field.

It failed, on grounds that are now standard:

- $g_{[\mu\nu]}$ never reproduced Maxwell's equations;
- the antisymmetric sector carries ghosts and linearization
  instabilities (Damour–Deser–McCarthy);
- the Cauchy problem is not well posed.

The programme survives only in modified form (Moffat's NGT and its
successors), and is not part of mainstream gravitational physics.

---

## 2. Where QOU carries the same split

QOU has a symmetric/antisymmetric decomposition with **the same physical
assignment Einstein wanted** — but it lives one level below spacetime, in
the braided category rather than on a metric tensor.

### 2.1 The split is forced by the Hecke relation

The braiding $c_{V,V}$ decomposes $V \otimes V = S^2_q V \oplus \Lambda^2_q V$
and acts as a scalar on each summand:

| Summand | Braiding eigenvalue | Sector |
|---|---|---|
| $S^2_q V$ (symmetric) | $+q$ | bosonic / binding |
| $\Lambda^2_q V$ (antisymmetric) | $-q^{-1}$ | fermionic / repulsive |

These are exactly the two roots of the Hecke relation
$(\sigma - q)(\sigma + q^{-1}) = 0$
([`braid-group-su2.md`](../../content/quantum-observable-universe/braids-and-knots/braid-group-su2.md)).
The split is therefore **structural, not fitted** — it is the eigenvalue
decomposition of a generator satisfying a quadratic relation.

### 2.2 The Archimedean form: $\cosh$ / $\sinh$

Writing $\lambda = \ln q$
([`crossing-energy-decomposition.md`](../../content/quantum-observable-universe/observations/crossing-energy-decomposition.md)):

$$
  q \;=\; \cosh\lambda + \sinh\lambda,
  \qquad
  q^{-1} \;=\; \cosh\lambda - \sinh\lambda .
$$

Under the mirror operation $\sigma$ (reverse every crossing), the
$\cosh$ part is invariant and the $\sinh$ part reverses sign. This is a
genuine symmetric/antisymmetric decomposition of the crossing weight,
and it is Lean-proved sorry-free
(`symmetricWeight_eq_cosh`, `antisymmetricWeight_eq_sinh`).

### 2.3 The physical assignment matches Einstein's intent

From [`crossing-energy-interpretation.md`](../../content/quantum-observable-universe/observations/crossing-energy-interpretation.md):

| Channel | Weight | Mirror | Force |
|---|---|---|---|
| Symmetric | $\cosh\lambda$ | invariant | **strong binding** |
| Antisymmetric | $\sinh\lambda$ | reverses | **Coulomb (electromagnetic)** |

> "The symmetric part binds regardless of charge. The antisymmetric part
> distinguishes charges."

And the electromagnetic coupling puts the *antisymmetric eigenvalue*
literally in the numerator
([`em-coupling-projection.md`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-projection.md)):

$$
  \alpha_{\mathrm{EM}}(q) \;=\; \frac{q^{-1}}{[9]_q \cdot [10]_q}.
$$

[`vdw-pskew-isolation-interpretation.md`](../../content/quantum-observable-universe/information-theory/vdw-pskew-isolation-interpretation.md)
makes the identification explicit: $\alpha_{\mathrm{EM}}$ is "the unique
multiple of the **antisymmetric $e_-$** coupling."

**Summary of the parallel:**

| | Einstein (1925–1955) | QOU |
|---|---|---|
| Carrier of the split | spacetime metric $g_{\mu\nu}$ | braiding $c_{V,V}$ / crossing energy |
| Symmetric part | gravitation | strong binding ($\cosh\lambda$) |
| Antisymmetric part | electromagnetism (hoped) | Coulomb / EM ($\sinh\lambda$) |
| Origin of the split | postulated (symmetry dropped) | forced (Hecke quadratic) |
| Deformation dial | none | $q$; at $q = 1$ the antisym. part vanishes identically |

QOU realizes Einstein's *intent* — antisymmetric sector carries EM —
while discarding his *mechanism*.

---

## 3. Three disanalogies (these are the load-bearing part)

### 3.1 QOU's metric is symmetric and emergent

Gravity in QOU is the **acoustic metric** of Madelung brane flow
([`madelung-acoustic-metric.md`](../../content/quantum-observable-universe/fluid-dynamics/madelung-acoustic-metric.md)):

$$
  g_{\mathrm{ac}}
  =
  \frac{\rho}{c_s}
  \begin{pmatrix}
    -(c_s^2 - v^2) & -v^T \\
    -v & \mathbf{1}
  \end{pmatrix}
$$

which is manifestly **symmetric**. There is no $g_{[\mu\nu]}$ anywhere in
QOU. The asymmetry sits strictly *upstream* of spacetime, in the
substrate algebra; spacetime and its metric are downstream, emergent, and
symmetric.

### 3.2 This is why QOU dodges Einstein's failure mode

The Damour–Deser–McCarthy ghost and instability results attack an
antisymmetric **propagating tensor field** on spacetime. QOU's
antisymmetric sector is a **braiding eigenvalue in a rigid monoidal
category** — it has no field equations, hence nothing to be unstable in.

This is a genuine structural advantage over the historical programme.
It is also a genuine limitation on the comparison: **QOU is not a rival
non-symmetric gravity theory.** It is a different kind of object, and
should not be benchmarked against NGT the way it is benchmarked against
LQG/ADM/Ashtekar in
[`lqg-adm-ashtekar-comparison.md`](../../content/quantum-observable-universe/gravity-spacetime/lqg-adm-ashtekar-comparison.md).

### 3.3 The nearest "deformed metric" is conformal, not antisymmetric

[`q-metric-contact-deformation.md`](../../content/quantum-observable-universe/fluid-dynamics/q-metric-contact-deformation.md)
does treat $q$ as a dial on a metric — interpolating the full
Levi-Civita connection to its Reeb projection along $\xi_q$. But that is
a **conformal / contact** deformation of a symmetric metric (following
Cardona–Miranda–Peralta-Salas–Presas), not the addition of an
antisymmetric part. Structurally distinct from Einstein's move.

---

## 4. Retraction — the force-carrier selection is derived, not fitted

An earlier skeptical read in this session (recorded here so the
correction is durable) suggested that $T_{2,9}$ and $T_{3,5}$ — supplying
the crossing numbers $9$ and $10$ in $\alpha_{\mathrm{EM}}$ — looked like
a free two-integer choice from an infinite torus-knot family, i.e.
fit-adjacent. **That was wrong.** The corpus derives the pair:

- The genus of a torus knot is $g(T_{m,n}) = (m-1)(n-1)/2$.
- At $g = 4$: $(m-1)(n-1) = 8$ with $\gcd(m,n) = 1$ and $2 \le m < n$ has
  **exactly two** solutions — $(m-1, n-1) = (1, 8) \Rightarrow T_{2,9}$
  and $(m-1, n-1) = (2, 4) \Rightarrow T_{3,5}$
  ([`prop:torus-knot-genus-four-unique`](../../content/quantum-observable-universe/predicted-spectra/torus-knot-genus-four-unique.md)).
- Crossing numbers follow: $c(T_{2,9}) = 9$, $c(T_{3,5}) = 10$.
- And $g = 4$ is itself forced, not chosen: Bring's surface has
  $\chi = -6$, and
  [`cohomological-embedding.md`](../../content/quantum-observable-universe/brings-surface/cohomological-embedding.md)
  §(iv) shows the QOU axioms require $T_{2,3}$ and $T_{2,9}$ to embed
  while $T_{2,11}$ must not, which "uniquely forces $g = 4$ and
  $\chi = -6$."

So $[9]_q \cdot [10]_q$ in $\alpha_{\mathrm{EM}}$ is not a free choice.
The relevant propositions carry Lean refs
(`QOU.Archimedean.torus_knot_genus_four_unique`,
`QOU.Archimedean.force_carrier_bring_uniqueness`).

### 4.1 The one soft spot that survives

The EM/strong ratio $\tanh(\ln q_0) \approx 0.104$ is reported "at the
Skein scale"
([`crossing-energy-interpretation.md`](../../content/quantum-observable-universe/observations/crossing-energy-interpretation.md)),
but that scale is never pinned to a renormalization point. Since
$\alpha \approx 0.0073$ and $\alpha_s$ runs from $\approx 0.1$ to
$\approx 1$ across accessible energies, a scale-free $0.104$ labelled
"EM/strong" is suggestive rather than falsifiable. This is a
**presentation gap, not a derivation gap** — the $\tanh(\ln q)$ identity
itself is exact and Lean-proved. Recommend either pinning the scale or
softening the claim to a ratio of channel weights without the
force-comparison gloss.

---

## 5. Formalization result — an honest negative

Formalizing the composite level (this PR) surfaced a **scope-(a)
over-claim** in `prop:crossing-energy-decomposition` claim 4.

The `.md` states the antisymmetric-to-symmetric ratio

$$
  \frac{E_{\mathrm{asym}}}{E_{\mathrm{sym}}} = \tanh(\ln q)
$$

is "independent of $\mathfrak{H}$". Working out the composite case shows
why that needs a hypothesis. For a composite with $p$ positive and $m$
negative crossings, the per-crossing weights decompose as

$$
  +q = +\cosh\lambda + \sinh\lambda,
  \qquad
  -q^{-1} = -\cosh\lambda + \sinh\lambda,
$$

so the mirror flips the sign of the $\cosh$ part but **not** the $\sinh$
part. Summing gives *different multiplicities* on the two channels:

$$
  E_{\mathrm{sym}} = (p - m)\cosh\lambda,
  \qquad
  E_{\mathrm{asym}} = (p + m)\sinh\lambda,
$$

hence

$$
  \frac{E_{\mathrm{asym}}}{E_{\mathrm{sym}}}
  = \frac{p + m}{p - m}\,\tanh(\ln q).
$$

The ratio equals $\tanh(\ln q)$ **exactly on the positive-braid locus**
$m = 0$, and is composite-dependent otherwise. A composite with two
positive and one negative crossing has ratio $3\tanh(\ln q)$
(`ratio_two_one_ne_tanh`).

**Scope classification (AGENTS.md §refuted/ruled-out):** this is
**scope (a)** — the claim as stated is over-general, not wrong. Every
worked example in the corpus (the $T_{2,3}$ table with $n_c = 3$, the
$e^-e^+$ pair) is a positive braid closure, where the identity holds
exactly. Recommended fix: add the hypothesis "for a positive braid
closure" to claim 4 rather than deleting it.

### 5.1 The same multiplicity mismatch is what makes pair creation work

The mismatch is not a defect — it is the mechanism. `pair_cancellation`
(Lean, sorry-free):

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  + \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}^{\sigma})
  = 2 E_{\mathrm{asym}}(\mathfrak{H})
$$

The symmetric (strong) channels cancel between a composite and its
mirror; the sign-blind antisymmetric (Coulomb) channels add. **This is
the sharpest formal statement of the Einstein parallel available in the
corpus:** the antisymmetric sector is exactly what survives when the
symmetric sector is cancelled by pairing.

---

## 6. Lean added by this PR

All sorry-free, over $\mathbb{R}$ (archimedean, matching the existing
file per AGENTS.md §7c). Verified `lean`-direct exit 0.

| Declaration | Content |
|---|---|
| `crossingEnergy` / `symChannel` / `asymChannel` | composite with $p$ positive, $m$ negative crossings |
| `crossingEnergy_split` | composite splits into the two channels |
| `symChannel_mirror` | mirror negates the $\cosh$ channel |
| `asymChannel_mirror` | mirror fixes the $\sinh$ channel |
| `pair_cancellation` | $\mathfrak{E}(\mathfrak{H}) + \mathfrak{E}(\mathfrak{H}^\sigma) = 2E_{\mathrm{asym}}$ |
| `ratio_positive_braid` | ratio $= \tanh(\ln q)$ on $m = 0$ |
| `ratio_general` | multiplicity factor $(p+m)/(p-m)$ |
| `ratio_two_one_ne_tanh` | concrete non-triviality witness |

---

## 7. Verdict

**There is no formal relationship** between QOU and Einstein's asymmetric
metric tensor: the programme is absent from the corpus, QOU's metric is
symmetric, and QOU's "torsion" is arithmetic rather than geometric.

**There is a real structural parallel**, and it is sharper than
coincidence: both frameworks split a bilinear structure into symmetric
and antisymmetric parts and assign electromagnetism to the antisymmetric
one. QOU differs in that (i) the split is forced by an algebraic
quadratic rather than postulated, (ii) it sits in the braided category
rather than on spacetime, and (iii) it therefore inherits none of the
ghost/Cauchy pathologies that killed Einstein's version.

The honest summary: **QOU achieves Einstein's goal by refusing his
starting point.** Einstein put the antisymmetry into the metric; QOU puts
it into the braiding and lets the metric emerge symmetric.

---

## 8. Follow-ups

1. **Amend `prop:crossing-energy-decomposition` claim 4** with the
   positive-braid hypothesis (§5). Small, mechanical; not done in this
   PR to keep the proposition edit separable from the comparison work.
2. **Pin or soften the "EM/strong ratio at the Skein scale" claim**
   (§4.1).
3. **Optional:** the `pair_cancellation` result is currently only in the
   Lean and this doc; it could be promoted to a proposition block if the
   author wants it in the narrative.
