**Conjecture (force-carrier knot/link dichotomy — categorical form).**
*Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a quantum observable
universe with substrate algebra $A$ over the categorical
coefficient ring $R$ ($q \in R$ generic, **not a root of unity in
$R$** — note $q = 1$ IS a root of unity, hence excluded). Every
mediator (force-carrier object) has a categorical type
determined by the topological component count of its closed-braid
representative:*

| Mediator type | Topological object | Categorical type |
|---------------|--------------------|--------------------------|
| **Unbroken-symmetry mediator** (e.g. photon) | 1-component torus *knot* | image factors through $\mathrm{Hom}_R(\mathbf{1}, A)$ via the Markov-trace closure |
| **Broken-symmetry mediator** (e.g. $W^\pm, Z, H$) | $d$-component torus *link*, $d \geq 2$ | image lives in $\mathrm{End}_R(A^{\otimes (d - 1)})$ with $d-1$ residual operator-strands |

*The categorical content is the **component-count factorisation**
of the topological-categorical correspondence: a $d$-component
closure carries $d - 1$ "operator strands" beyond the single
trace strand, hence sits in $\mathrm{End}_R$ rather than
$\mathrm{Hom}_R(\mathbf{1}, -)$. The Higgs mechanism's
"eating of Goldstones" is identified with this categorical
linking: one Goldstone thread per broken generator becomes one
operator-strand, lifting the boson from $\mathrm{Hom}_R(\mathbf{1},
A)$ to $\mathrm{End}_R(A)$.*

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

**Step 4 — embeddability is sufficient; saturation is not
required (path-α-Bring refinement, 2026-05-05).**
$T(2, 2k)$ has $\gcd(2, 2k) = 2$, so it is a 2-component link
with Seifert genus $g(T(2, 2k)) = k - 1$. The earlier draft of
this proof (commits prior to 2026-05-05) demanded **saturation**
$g(T(2, 2k)) = g(\Sigma) - 1$, which forced separate hosts for
$T(2,4), T(2,6), T(2,8)$ at genera $2, 3, 4$ and led to a
collision with Bring at $k = 4$.

The categorical content of the dichotomy does **not** require
saturation. By
[`prop:torus-embeddable-complete`](#prop:torus-embeddable-complete),
every $T(2, 2k)$ with $k - 1 \leq g(\Sigma)$ embeds in $\Sigma$.
Bring's genus-$4$ Seifert fiber accommodates **all** of $T(2, 4),
T(2, 6), T(2, 8)$ alongside the saturating
$\{T_{2,9}, T_{3,5}\}$. So the entire EM + EW carrier set lives
on a **single** host (Bring), and the categorical knot/link
distinction reduces to the topological component count alone.

| $k$ | $T(2, 2k)$ | $g(T(2,2k))$ | embeds on Bring? | role |
|----:|-----------:|-------------:|:----------------:|------|
| 2 | $T(2, 4)$ | 1 | ✓ | $W^\pm$ |
| 3 | $T(2, 6)$ | 2 | ✓ | $Z$ |
| 4 | $T(2, 8)$ | 3 | ✓ | $H$ |

The host-distinctness assumption from the earlier draft is
**dropped**; see audit
[`docs/audits/2026-05-05-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-05-path-alpha-bring-refinement.md).

**Step 5 — categorical placement in $\mathrm{End}_R(A)$.**
Once the host is fixed (Bring), the categorical content of the
dichotomy is *not* a host-arithmetic statement; it is a
**Wedderburn-block** statement on $\mathrm{End}_R(A)$ for $A$
the substrate algebra over $R$.

A 1-component knot $\hat\beta \in B_n$ closes to a single
Markov-trace strand: under Schur–Weyl
$\mathrm{End}_R(V^{\otimes n}) \cong \bigoplus_{\lambda \vdash n}
M_{f_\lambda}(R)$, the image of the closure is a **scalar in $R$**
on each Wedderburn block (the Markov trace value). It carries no
operator-strand content; it factors through
$\mathrm{Hom}_R(\mathbf{1}, A)$.

A 2-component link $\hat\beta$ closes to **two** Markov-trace
strands. Under the same Schur–Weyl decomposition, its image on
each Wedderburn block is a $f_\lambda \times f_\lambda$ matrix
acting non-trivially on the seminormal basis (Hoefsmit form):
$\sigma_1^{2k}$ in $H_n(q)$ for $n \geq 3$ has *seminormal*
eigenvalues $q^{2 c(b)}$ where $c(b)$ is the cell content of basis
element $b$ in $V_\lambda$
([Hoefsmit 1974](#references)). For different $k$, the eigenvalue
$q^{2k}$ picks out **different** Hoefsmit basis elements — the
$W$, $Z$, $H$ projectors live in **different** rank-1 idempotents
of $\mathrm{End}_R(A)$, distinguished by cell-content data
$(\lambda, c)$.

This **respects** the $\mathrm{End}_R(A)$ Wedderburn decomposition:
distinct EW carriers $T(2, 2k)$ pick out distinct $(\lambda, c)$
slots whenever $n \geq 3$, even though they all collapse to the
same 2-dim minimal-polynomial structure of $\sigma_1$ inside
$H_2(q)$.

The audit
[`docs/audits/2026-05-05-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-05-path-alpha-bring-refinement.md)
flags this: the H_2(q)-only formulation of
[`conj:weak-spectral-completeness`](#conj:weak-spectral-completeness)
is dimensionally inconsistent (six rank-1 projectors cannot live
in a 2-dim algebra). The honest categorical content is the
$n \geq 3$ formulation outlined here.

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
([`rem:alpha-em-categorical-trace`](#rem:alpha-em-categorical-trace)).
$\square$

### Status

**Open as a derivable proposition.** The argument above is
structurally complete in its **categorical** form (path-α-Bring
refinement, 2026-05-05) but currently relies on:

1. A categorical formulation of the Higgs mechanism in
   $\mathbf{Rep}$-language — open content gap (Step 6 above
   is the topological **interpretation**, not a categorical
   derivation).
2. The Hoefsmit cell-content identification of $W, Z, H$
   inside $\mathrm{End}_R(A)$ for $A$ the multi-strand
   substrate — i.e. concrete $(\lambda_W, c_W)$,
   $(\lambda_Z, c_Z)$, $(\lambda_H, c_H)$ assignments at some
   minimum strand count $n \geq 3$. This replaces the earlier
   "asymmetric-genus-$4$-host" gap.
3. The Wirtinger / Seifert combinatorial input for Step 3
   (component-count vs $H_1$ rank) — standard but not yet
   content-blocked in QOU.

**To promote to `proposition`:**
- Author the categorical Higgs mechanism block.
- Author the **Hoefsmit cell-content identification** for the EW
  triplet inside $\mathrm{End}_R(A)$ — minimum $n \geq 3$, with
  concrete $(\lambda, c)$ data per carrier. This is what
  resolves the $\mathrm{End}_R(A)$-decomposition issue flagged
  in the audit.
- Cite Wirtinger / Seifert classical results explicitly with
  Lean-formalised analogs (deferred to research-level
  formalisation).

### Downstream consequence (closing U2 of NV-1)

If this conjecture holds, the structural premise (U2) of
[`conj:electroweak-higgs-torus-link-triplet`](#conj:electroweak-higgs-torus-link-triplet)
("EW force-carriers are 2-component links not knots") is upgraded
from a structural premise to a **derived consequence** of:

- the **categorical component-count factorisation** (Step 5):
  $d$-component closure ⟹ $d - 1$ residual operator-strands ⟹
  image in $\mathrm{End}_R(A^{\otimes (d-1)})$;
- the Higgs mechanism interpreted as **categorical linking**
  (Step 6): each broken generator pulls in one Goldstone thread,
  lifting the boson from $\mathrm{Hom}_R(\mathbf{1}, A)$ to
  $\mathrm{End}_R(A)$.

This is the principal value of the conjecture: it converts U2
from a free input into a derivable consequence. The
**host-distinctness** version of U2 (used in the prior draft) is
no longer required and has been retired with the path-α-Bring
refinement.

### What this changes downstream

- [`conj:electroweak-higgs-torus-link-triplet`](#conj:electroweak-higgs-torus-link-triplet):
  U2 is now purely categorical (link vs knot, not host distinct).
  (refined 2026-05-05).
- [`conj:weak-spectral-completeness`](#conj:weak-spectral-completeness):
  the H_2(q)-only formulation is dimensionally inconsistent;
  needs lift to $\mathrm{End}_R(A)$ with $n \geq 3$ Hoefsmit
  cell-content data (flagged in audit).
- [`prop:weak-symmetric-normalization`](#prop:weak-symmetric-normalization):
  the closed form $\mathcal{N}_{\rm sym}(q) = q^6 (1+q^2+q^4)/3$
  is currently the **trace-side** Plancherel partition (Fix B
  reading); its derivation as a true Wedderburn-orthogonal
  Plancherel weight requires the Hoefsmit lift.
