**Conjecture (force-carrier knot/link dichotomy).**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe whose
substrate is supported on a host Riemann surface $\Sigma$.  A
**force-carrier** in $\mathrm{End}_R(A)$ — i.e., a categorical
mediator between vortex morphisms
([categorical action](#def:categorical-action)) — has its
underlying topological object classified as follows:*

| Mediator type | $H_1(\Sigma)$ role | Topological object |
|---------------|-------------------|--------------------|
| **Saturating** ($g(K) = g(\Sigma)$) | single saturating generator | **1-component** torus *knot* |
| **Sub-saturating** ($g(K) < g(\Sigma)$) | linked pair generates $H_1$ | **2-component** torus *link* |

*Equivalently: an unbroken-symmetry mediator (massless gauge
boson) is realised as a knot saturating its host's homology; a
broken-symmetry mediator (massive gauge boson, Higgs scalar) is
realised as a 2-component link with non-trivial linking number,
on a host whose genus exceeds that of the link's components by
exactly $1$.*

### Proof sketch (U2)

**Step 1 — saturating mediators are knots.**
For Bring's surface $\Sigma_4$ (genus $4$), the saturating force-
carrier sector
([force-carrier Bring uniqueness](#prop:force-carrier-bring-uniqueness))
is exactly $\{T_{2,9}, T_{3,5}\}$ — the two genus-$4$ torus knots.
$\gcd(2,9) = \gcd(3,5) = 1$, so each is a **single-component**
knot. The saturation condition $g(K) = g(\Sigma_4) = 4$ forces
both. By Riemann–Hurwitz on the $S_5$-quotient of $\Sigma_4$, the
sub-orbit structure of these knots under $S_5\times\langle\hat
\tau\rangle$ generates the symplectic homology lattice
$H_1(\Sigma_4, \mathbb{Z}) \cong \mathbb{Z}^{8}$.  No multi-
component link is needed; a 1-component saturator suffices.

**Step 2 — sub-saturation requires multiple components.**
Suppose $K$ is a torus knot with $g(K) < g(\Sigma)$, embedded as
a force-carrier on $\Sigma$. Then $H_1(\Sigma) \cong \mathbb{Z}^{2g(\Sigma)}$
exceeds the $\mathbb{Z}^{2g(K)}$-image of $K$'s longitudinal
classes, leaving $2(g(\Sigma) - g(K))$ generators unaccounted for.

For a $\ell$-component torus link $L = K_1 \sqcup \cdots \sqcup
K_\ell$, the total Seifert-surface complement has
$H_1(\Sigma \setminus \nu(L), \mathbb{Z}) \cong
\mathbb{Z}^{2g(L) + 2(\ell - 1)}$ — each additional component
adds **two** classes (longitude + meridian) via the standard
Wirtinger presentation of the link group.

**Step 3 — saturating 2-component links live on a host one
genus higher than the link's Seifert genus.**
For a 2-component link $L$ with Seifert genus $g(L)$, saturation
of $H_1(\Sigma)$ requires
$$
  2g(L) + 2 \cdot (2 - 1) = 2g(\Sigma),
  \quad \text{i.e.,} \quad
  g(\Sigma) = g(L) + 1.
$$
Hence a 2-component link with genus $k - 1$ saturates a host of
genus $k$.

**Step 4 — application to $T(2, 2k)$.**
$T(2, 2k)$ has $\gcd(2, 2k) = 2$, so it is a 2-component link.
Its Seifert genus is $g(T(2, 2k)) = k - 1$.  By Step 3, its
saturating host has genus $k$.

| $k$ | $T(2, 2k)$ | $g(T(2,2k))$ | host genus |
|----:|-----------:|-------------:|-----------:|
| 2 | $T(2, 4)$ | 1 | $\Sigma_2$ |
| 3 | $T(2, 6)$ | 2 | $\Sigma_3$ |
| 4 | $T(2, 8)$ | 3 | $\Sigma_4$? — **collision with Bring** |

**Step 5 — handling the genus-$4$ collision.**
Step 4 predicts that $T(2, 8)$ would saturate a genus-$4$ host —
but Bring's genus-$4$ slot is already exhausted by
$\{T_{2,9}, T_{3,5}\}$.  *Resolution:* the host of $T(2, 8)$ is
**not** Bring.  Two genus-$4$ Riemann surfaces can be inequivalent
as $\hat\tau$-equivariant covers: Bring is the $S_5$-symmetric
genus-$4$ surface, and there exist $S_5$-asymmetric genus-$4$
surfaces (e.g., curves of genus $4$ with smaller automorphism
group) that can host a 2-component link without saturation
collision.  The Higgs sector lives on **one such asymmetric
genus-$4$ host**.

For $T(2, 4)$ and $T(2, 6)$, the hosts are genus-$2$ and
genus-$3$ respectively — distinct from Bring and from each other.
This corresponds to **three independent algebraic curves**
$\Sigma_2^W, \Sigma_3^Z, \Sigma_4^H$ as the natural hosts of $W$,
$Z$, $H$.

**Step 6 — broken symmetry ⟺ link structure.**
Topologically, the Higgs mechanism corresponds to *linking*
between the gauge boson and the eaten Goldstone:
- pre-EWSB: gauge boson = single-component loop in
  $\mathbf{Rep}(SU(2)_L \times U(1)_Y)$;
- post-EWSB: gauge boson + Goldstone = two-component link
  with linking number $\mathrm{lk} = 1$ (one Goldstone "thread"
  per broken generator).

Hence broken-symmetry mediators are **2-component links**.  This
is the topological dual of the Higgs mechanism: the gauge boson
acquires mass by being linked to a Goldstone thread; the linking
number is the Higgs charge.

The unbroken EM survivor $\gamma$ has no Goldstone thread (it
generates the unbroken $U(1)_{em}$); it remains a 1-component
object — and matches the Bring-saturated photon
identification within $\{T_{2,9}, T_{3,5}\}$
([alpha-em-categorical-trace](#prop:alpha-em-categorical-trace)).
$\square$

### Status

**Open as a derivable proposition.** The argument above is
structurally complete but currently relies on:

1. A categorical formulation of the Higgs mechanism in
   $\mathbf{Rep}$-language — open content gap (Step 6 above
   is the topological **interpretation**, not a categorical
   derivation).
2. The classification of $S_5$-asymmetric genus-$4$ Riemann
   surfaces and their compatibility with the
   [adelic substrate](#def:adelic-substrate) — open.
3. The Riemann–Hurwitz correspondence for sub-saturating
   2-component links — Step 3 uses Wirtinger / Seifert classical
   results which are standard but not yet content-blocked in QOU.

**To promote to `proposition`:**
- Author the categorical Higgs mechanism block.
- Author the genus-$4$ asymmetric-host classification.
- Cite Wirtinger / Seifert classical results explicitly with
  Lean-formalised analogs (deferred to research-level
  formalisation).

### Downstream consequence (closing U2 of NV-1)

If this conjecture holds, the structural premise (U2) of
[`conj:electroweak-higgs-torus-link-triplet`](#conj:electroweak-higgs-torus-link-triplet)
("force-carriers are 2-component links not knots") is upgraded
from a structural premise to a **derived consequence** of:
- the Higgs mechanism (broken symmetry → linking),
- the saturating-host-genus formula $g(\Sigma) = g(L) + 1$.

This is the principal value of the conjecture: it converts (U2)
from a free input into a derivable consequence.
