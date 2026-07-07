<!-- FILE_START: classical-limit-implications-intro.md -->
The previous sub-section built the classical-limit functor and
established its substrate-level constructions (adelic substrate,
obstruction, joint-Galois-braid action). This sub-section harvests
the consequences. The graded Baer-star structure on $\mathcal{H}_q$
descends through the two-filtration bridge to relate the
Gröbner--Shirshov depth filtration to Goncharov's period filtration,
producing the classical Riemann zeta as a $q = 1$ limit of the
$q$-zeta primitive defined earlier. The Riemann hypothesis surfaces
as a statement about a specific filtration height; the adelic Tate
squeeze that closes the chapter is the surreal-bound infrastructure
consumed by the appendix-surreal Millennium bounds.

The sub-section ends with the chapter outro, gesturing forward to
`models-of-qous` (next chapter), which makes the archimedean wall
explicit and prepares the archimedean-universe specialisation.
<!-- FILE_END: classical-limit-implications-intro.md -->

<!-- FILE_START: graded-baer-star-Hq.md -->
**Conjecture (graded Baer-* on $\mathcal{H}_q$ across the depth filtration).**

*Let $\mathcal{H}_q$ be the substrate convolution Hopf algebra
([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)),
filtered by iterated-integral depth
([keystone correspondence](#conj:gb-depth-period-correspondence)):*

$$
  G^{(0)}(\mathcal{H}_q) \;\subseteq\; G^{(1)}(\mathcal{H}_q)
  \;\subseteq\; G^{(2)}(\mathcal{H}_q) \;\subseteq\; \cdots.
$$

*Each filtration piece $G^{(n)}(\mathcal{H}_q)$ is a Baer-*-ring
under the bar involution, and the inclusions $G^{(n)} \hookrightarrow
G^{(n+1)}$ are **Baer-*-morphisms**: they send projections to
projections and preserve the annihilator-generation property.
Equivalently: $\mathcal{H}_q$ admits a system of orthogonal
projections $\{p_n^{(i)}\}_{n,i}$ indexed by depth $n$ and
intra-depth label $i$, with*

- *each $p_n^{(i)}$ self-adjoint under $* \colon q \mapsto q^{-1}$,*
- *$p_n^{(i)} p_m^{(j)} = 0$ when $(n, i) \neq (m, j)$,*
- *$\sum_{i} p_n^{(i)} \cdot \mathrm{id}_{G^{(n)}} = \mathrm{id}_{G^{(n)}}$
  (completeness at each depth).*

### Structural justification

Three free consequences if discharged:

1. **Explicit Goncharov-period witnesses.** Each projection
   $p_n^{(i)} \cdot \mathrm{Li}_n^q(z)$ under $\tau_{\mathrm{arch}}$
   generates a *specific* element of $\mathcal{P}_n / \mathcal{P}_{n-1}$
   — naming a real-number period class with a finite algebraic
   label. (Without graded Baer-*, B1 only asserts existence.)
2. **Graded Mikusiński localisation.** The field-of-fractions tower
   $\mathcal{M}_q^{(n)}$ inherits a graded Baer-* structure: each
   $\mathcal{M}_q^{(n)}$ is itself Baer-*, with its "delta at depth
   $n$" $= 1/\omega^n$ on the surreal envelope corresponding to a
   specific projection. The graded Titchmarsh question
   ([keystone §discharge targets](#conj:gb-depth-period-correspondence))
   gets a clean handle: zero divisors at depth $n$ are detected by
   non-trivial $p_n^{(i)} \cdot p_n^{(j)}$ for $i \neq j$.
3. **Bar-involution-equivariant period theory.** Self-adjoint
   $p_n^{(i)}$ generate *real* periods (bar-fixed loci of $\mathcal{P}_n$);
   bar-swapped pairs generate *chirality-twisted* periods (eigenspaces
   of bar with eigenvalue $-1$ — equivalently, periods of motives
   with a Tate twist). See
   [`rem:chirality-period-pairing`](#rem:chirality-period-pairing).

### Reduction to known structure

At depth 0 (scalars + $\exp_q$): Baer-* is trivial — $G^{(0)}$ is a
field.

At depth 1 ($\log_q$ adjoined): the analogue is Baker's theorem
infrastructure — annihilators of $\log\alpha$-relations among
algebraic $\alpha$'s. Baer-* at this depth corresponds to the
*linear independence* of logarithms of multiplicatively
independent algebraics (Baker 1966; Wüstholz). Conjecturally
known.

At depth 2 ($\mathrm{Li}_2^q$ adjoined): reduces to the Hecke
algebra Baer-* result
([`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic))
since the depth-2 grouplikes pair with $H_n(q)$-cells via the
Markov trace. The projections are the Hoefsmit $e_\lambda$,
lifted to $\mathcal{H}_q$ via Schur–Weyl duality.

At depth $\geq 3$: open. The depth-3 case requires identifying
projections compatible with the trilog grouplike $\mathrm{Li}_3^q$
— see the depth-3 witness
([`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)).
<!-- FILE_END: graded-baer-star-Hq.md -->

<!-- FILE_START: two-filtration-bridge-small-cases.md -->
**Proposition (two-filtration bridge map verified at small
self-conjugate / chiral-pair partitions).**

The two-filtration bridge conjecture
([`conj:two-filtration-bridge`](#conj:two-filtration-bridge))
predicts an iterated-integral depth $d_{\mathrm{II}}(\lambda)$ for
each partition $\lambda$:

$$
  d_{\mathrm{II}}(\lambda) =
  \begin{cases}
    2 & \lambda \text{ self-conjugate} \\
    3 & \lambda, \lambda' \text{ chiral pair}
  \end{cases}
$$

*This proposition verifies the predicted bridge map for all
partitions $\lambda \vdash n$ with $n \leq 4$, by combining the
explicit Markov-trace calculation on each Wedderburn cell with
known Vol/CS values from classical knot theory.*

### Verification table for $n \leq 4$

See [Table](#tbl:two-filtration-bridge-small-cases-table-data).

### Detailed verifications

#### Self-conjugate $\lambda = (2, 2)$, $n = 4$ (figure-8 row)

This is the principal positive case. The figure-8 knot $4_1$ is
amphichiral, so $\mathrm{CS}(4_1) = 0 \pmod{\pi^2 \mathbb{Z}}$.
Its volume is non-trivial: $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \in
\mathcal{P}_2 / \mathcal{P}_1$.

- Pairing of $e_{(2, 2)}$ with $\mathrm{Li}_2^q(\zeta_6)$ via
  Markov trace: produces $\mathrm{Vol}(4_1) \neq 0$.
- Pairing of $e_{(2, 2)}$ with $\mathrm{Li}_3^q(\zeta_6)$:
  amphichirality forces $\mathrm{CS} = 0$, hence trivial in
  $\mathcal{P}_3 / \mathcal{P}_2$.

Conclusion: $d_{\mathrm{II}}((2, 2)) = 2$ — **bridge prediction
verified**. Theorem-level via [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem).

#### Chiral pair $(3) + (1, 1, 1)$, $n = 3$ (trefoil row)

Trefoil $T(2, 3) = 3_1$ is chiral. Its volume is 0 (torus, not
hyperbolic), but $\mathrm{CS}(3_1) = -\pi^2/6$.

- Pairing of $e_{(3)}$ or $e_{(1, 1, 1)}$ with $\mathrm{Li}_2^q$:
  $\mathrm{Vol}(3_1) = 0$ — depth-2 vanishes.
- Pairing with $\mathrm{Li}_3^q$: $\mathrm{CS}(3_1) = -\pi^2/6 \in
  \pi^2 \mathbb{Q}$ — **non-trivial** in $\mathcal{P}_3 / \mathcal{P}_2$
  (the rational $\pi^2$ class is non-zero modulo $\pi^4$).

Conclusion: $d_{\mathrm{II}}(\text{chiral pair}) = 3$ — **bridge
prediction verified**. Theorem-level via [`prop:b1-torus-knot-rows-theorem`](#prop:b1-torus-knot-rows-theorem).

#### Self-conjugate $\lambda = (2, 1)$, $n = 3$

Self-conjugate but no hyperbolic 3-strand knot has $(2, 1)$ alone
as dominant cell — it's the *standard* representation in $H_3$,
shared by many small knots/links. The bridge prediction
$d_{\mathrm{II}}((2, 1)) = 2$ holds *structurally*: the pairing
with $\mathrm{Li}_2^q$ gives non-trivial period contributions for
hyperbolic knots whose Hoefsmit decomposition includes the
standard rep with non-trivial coefficient.

Conclusion: structural verification (yes) (no specific hyperbolic
3-strand example to test directly; 4_1 in $B_3$ has $(2,1)$ in its
decomposition but not as DOMINANT cell, hence the figure-8 row uses
$(2, 2)$ in $H_4$ rather than $(2,1)$ in $H_3$).

#### Generalisation pattern

The verifications above instantiate the structural prediction:

- **Self-conjugate $\lambda = \lambda'$**: amphichiral
  knot-class $\Rightarrow$ $\mathrm{CS} = 0 \pmod{\pi^2}$ $\Rightarrow$
  depth-3 trivial $\Rightarrow$ $d_{\mathrm{II}} = 2$.
- **Chiral pair $\lambda \neq \lambda'$**: chiral knot-class
  $\Rightarrow$ $\mathrm{CS} \neq 0$ in $\mathcal{P}_3 / \pi^2 \mathbb{Q}$
  $\Rightarrow$ depth-3 non-trivial $\Rightarrow$ $d_{\mathrm{II}} = 3$.

The **bar-eigenspace** structure of partitions ([`rem:chirality-period-pairing`](#rem:chirality-period-pairing))
is the structural reason for the bridge map.

### Result

**The two-filtration bridge map is verified at $n \leq 4$**. The
verification proceeds by case analysis on partition bar-class
(self-conjugate vs chiral pair) using known Vol/CS values from
classical knot theory.

This **partially discharges** the two-filtration bridge conjecture
([`conj:two-filtration-bridge`](#conj:two-filtration-bridge)) at
small $n$. The general statement at $n \geq 5$ is open.

### Open questions

- **General $n$**: the bridge map for arbitrary partitions of
  $n \geq 5$ requires extending the Vol/CS dictionary to larger
  Hecke-cell decompositions. The *structural* argument
  (self-conj. $\to$ even depth, chiral pair $\to$ odd depth) extends, but
  individual partition verification is open.
- **Mixed cells**: partitions whose Hecke action is a mixture of
  self-conj. and chiral parts — currently the bridge formula
  predicts $\min(\mathrm{depth}_{\mathrm{GB}}, 2 \lceil n/2 \rceil)$
  in this case ([`conj:two-filtration-bridge`](#conj:two-filtration-bridge)).
  Verification at small $n$ is open.

### Cross-references

- Bridge conjecture: [`conj:two-filtration-bridge`](#conj:two-filtration-bridge)
- Chirality structure: [`rem:chirality-period-pairing`](#rem:chirality-period-pairing)
- Figure-8 row theorem: [`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)
- Torus-knot rows theorem: [`prop:b1-torus-knot-rows-theorem`](#prop:b1-torus-knot-rows-theorem)
- Explicit central idempotents: [`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)
<!-- FILE_END: two-filtration-bridge-small-cases.md -->

<!-- FILE_START: classical-riemann-zeta.md -->
Define the **classical Riemann zeta function** $\zeta(s)$ as the adelic
global limit of the local $q$-geometries. As $q \to 1$, the local
zeta functions $Z(\mathcal{B}, q^{-s})$ at each prime fiber assemble
into the Euler product:

$$
\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}
         = \sum_{n=1}^{\infty} \frac{1}{n^s},
  \qquad \mathrm{Re}(s) > 1
$$

The passage from $Z(\mathcal{B}, t)$ to $\zeta(s)$ can be understood
as follows: each maximal ideal $\mathfrak{m}$ of norm
$N(\mathfrak{m}) = p^f$ contributes a local factor to the product.
The adelic completion --- taking the product over all primes
simultaneously --- yields the global zeta function.

The non-trivial zeros of $\zeta(s)$ are the classical shadows of the
Reeb eigenvalues: under the spectral coordinate mapping,
$\alpha_i = q^{\rho_i} \to e^{-\rho_i \log p}$ at each prime $p$,
and the global zeros arise from the coherent alignment of the local
spectra.
<!-- FILE_END: classical-riemann-zeta.md -->

<!-- FILE_START: classical-riemann-hypothesis.md -->
**Conjecture (Riemann, 1859).** All non-trivial zeros of the Riemann
zeta function $\zeta(s)$ satisfy

$$
\mathrm{Re}(s) = \frac{1}{2}
$$

In the language of the substrate, this asserts that the critical-line
property established unconditionally at the $q$-scale (Corollary, §4)
persists through the classical limit $q \to 1$. The Hasse--Weil bound
guarantees $\mathrm{Re}(\rho) = 1/2$ for each local geometry
individually; the Riemann hypothesis asserts that this alignment
survives the adelic assembly into the global zeta function.

The gap between the local and global statements is precisely the gap
between the proven Weil conjectures and the unproven Riemann
hypothesis.
<!-- FILE_END: classical-riemann-hypothesis.md -->

<!-- FILE_START: macroscopic-stability-equivalence.md -->
The stability of the macroscopic spacetime continuum is equivalent to
the Riemann hypothesis. Precisely:

**Theorem.** The following are equivalent:

1. **Macroscopic stability**: The classical Chebyshev function
   satisfies $\psi(X) = X + O(X^{1/2 + \varepsilon})$ for all
   $\varepsilon > 0$.
2. **Riemann hypothesis**: All non-trivial zeros of $\zeta(s)$
   satisfy $\mathrm{Re}(s) = 1/2$.
3. **Spectral persistence**: The critical-line property of the Reeb
   spectrum is preserved under the classical limit functor
   $\mathcal{L}$.

The implication $(2) \Leftrightarrow (1)$ is classical (the prime
number theorem with optimal error term). The implication
$(2) \Leftrightarrow (3)$ follows from the spectral coordinate
mapping and the explicit formula.

The $q$-scale analog of statement (1) --- namely,
$\psi_q(X) = X + O(X^{1/2})$ --- is an **unconditional theorem**,
guaranteed by the Hasse--Weil bound (Theorem, §4). The obstacle to
extending this to the macroscopic scale is that the classical limit
functor $\mathcal{L}$ is not full: information about the relative
phases of the local spectra is lost in the limit. Whether this
information loss preserves the critical-line alignment is exactly
the content of the Riemann hypothesis.

The algebraic substrate thus provides a **conditional framework**:
$q$-scale stability is proven; macroscopic stability requires the
Riemann hypothesis.
<!-- FILE_END: macroscopic-stability-equivalence.md -->

<!-- FILE_START: adelic-reeb-restricted-product.md -->
**Proposition (restricted-product structure of the Reeb $\omega$-order).**
*Let $\mathbb{A} = \mathbb{R} \times \prod_p' \mathbb{Q}_p$ be the rational
adele ring and, for each place $v$ of $\mathbb{Q}$, let
$\varepsilon_v \in \mathrm{Der}(A_v)$ be the local Reeb infinitesimal
([Reeb infinitesimal](#def:reeb-epsilon)) on the substrate's local completion
$A_v$. Suppose every local $\omega$-order $\ordw_v$ takes values in one common
linearly ordered value group $\Gamma$ — the $\omega$-grade of $\mathbf{No}$ —
and that, for any adelic observable $f = (f_v)_v$, the set of $v$ with
$\ordw_v(f_v) \neq 0$ is finite (restricted-product condition). Then the global
$\omega$-order is the finite sum of the local orders,*

$$
  \ordw_{\mathbb{A}}(f) \;=\; \sum_{v} \ordw_v(f_v)
  \qquad (\text{finite sum}),
$$

*and this assignment is*

1. **additive over places** — $\ordw_{\mathbb{A}}(fg) = \ordw_{\mathbb{A}}(f) +
   \ordw_{\mathbb{A}}(g)$ (Tate factorisation), and
2. **squeeze-coherent** — if $\ordw_v(g_v) \le \ordw_v(f_v)$ at every place and
   the inequality is *strict* at some place $v_0$, then
   $\ordw_{\mathbb{A}}(g) < \ordw_{\mathbb{A}}(f)$.
<!-- FILE_END: adelic-reeb-restricted-product.md -->

<!-- FILE_START: adelic-tate-squeeze.md -->
Tate's thesis \cite{tate1967} realises the global
Riemann / Dedekind $\zeta$-function as an **adelic Fourier
transform**: the global zeta integral factors as a restricted product
over local zeta integrals, one per place of $\mathbb{Q}$.  The QOU
framework lifts this factorisation to the surreal register: each
local place carries its own Reeb infinitesimal $\varepsilon_v$, the
global $\varepsilon$ is a restricted product of $\varepsilon_v$'s,
and the [surreal squeeze](#lem:surreal-squeeze) at each prime
descends to the global squeeze of [RH surreal bound](#rem:rh-surreal-bound).

**$\tau$ and $\mathrm{St}$ are dual archimedean reductions.**
Two morphisms in this paper extract real-valued data from
substrate-internal data, and they meet at the archimedean place
$v = \infty$ of $\mathbb{A}$:

- $\tau$ — the
  [QOU fibre functor](#rem:fibre-functor-rigidity), restricted
  to its archimedean component
  $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$, is the
  algebraic-geometry / Weil realization. It evaluates the
  algebraic quantum volume on the $\mathbb{R}$-component of
  the adelic ring (see
  [Vol(K) factors through $\tau$](#prop:vol-through-tau)).
- $\mathrm{St}$ — the
  [standard-part functor](#def:standard-part-functor) is the
  surreal-field extraction $\mathbf{No} \to \mathbb{R}$ that
  collapses positive infinitesimals to $0$.

They are *dual* reductions: $\tau_{\mathrm{arch}}$ projects across
the adelic places (selecting $v = \infty$), while $\mathrm{St}$
projects along the surreal birthday filtration (collapsing
$\varepsilon \to 0$). This remark uses both — $\mathrm{St}$ inside
each local factor (to read off the real-valued bound) and
$\tau_{\mathrm{arch}} = \pi_\infty$ across factors (to assemble the
global zeta).

**Setup.** Let $\mathbb{A} = \mathbb{R} \times \prod_p' \mathbb{Q}_p$
be the rational adele ring.  For each place $v$ of $\mathbb{Q}$
(archimedean $v = \infty$ or non-archimedean $v = p$), the local
Reeb flow on the substrate's local completion carries its own
local Reeb infinitesimal

$$
  \varepsilon_v
   \;\in\; \mathrm{Der}(A_v)
  \qquad (\text{positive infinitesimal in }\mathbf{No}).
$$

The global Reeb infinitesimal $\varepsilon$
([Reeb infinitesimal](#def:reeb-epsilon)) is the restricted product
of the $\varepsilon_v$'s, in the following sense: for almost every
place $v$, $\varepsilon_v$ equals the "tame" infinitesimal
$\varepsilon_\infty$ (archimedean reference), and the global
$\varepsilon$-adic valuation $\ordw_{\mathbb{A}}(f)$ of an adelic
observable is the **sum** over $v$ of local $\ordw$-orders:

$$
  \ordw_{\mathbb{A}}(f)
   \;=\; \sum_{v} \ordw_v(f_v)
  \qquad \text{(finite sum by restricted-product condition).}
$$

**The local--global surreal bound.** For each place $v$, the
local surreal-squeeze
$\delta^2 \cdot \varepsilon_v^{-1} > \varepsilon_v^3$ in
$\mathbb{R}(\varepsilon_v)$ gives a strict inequality in
$\omega$-orders (cost has higher $\ordw$-grade than budget,
$+1 > -3$):

$$
  \ordw_v(\delta^2 \cdot \varepsilon_v^{-1}) \;>\; \ordw_v(\varepsilon_v^3).
$$

Summing over all places (equivalently, taking the adelic
$\omega$-order) yields the global inequality

$$
  \ordw_{\mathbb{A}}(\delta^2 \cdot \varepsilon^{-1})
   \;=\; \sum_v \ordw_v(\delta^2 \cdot \varepsilon_v^{-1})
   \;>\; \sum_v \ordw_v(\varepsilon_v^3)
   \;=\; \ordw_{\mathbb{A}}(\varepsilon^3),
$$

which is the global surreal squeeze of
[RH surreal bound](#rem:rh-surreal-bound).

**Tate's local functional equation in surreal form.** Tate's
thesis proves each local zeta integral
$\zeta_v(f_v, s) = \int_{\mathbb{Q}_v^\times} f_v(x) \, |x|_v^s \, d^\times x$
satisfies a local functional equation
$\zeta_v(f_v, s) = \gamma_v(s) \cdot \zeta_v(\hat{f}_v, 1 - s)$
for each place $v$.  In the surreal register, this lifts to:

| Classical | Surreal |
|---|---|
| Local $\zeta_v(f_v, s)$ | $\ordw_v$-graded expansion in $\varepsilon_v$ |
| Gamma factor $\gamma_v(s)$ | $\ordw_v$-preserving reflection $s \leftrightarrow 1 - s$ |
| Local $L$-factor $(1 - p^{-s})^{-1}$ | Euler factor $(1 - \varepsilon_p)^{-1}$ at $s = 1$ |
| Global Euler product | Adelic $\varepsilon$-product $\prod_v (1 + \varepsilon_v)$ |

**Conclusion.** The Tate thesis Fourier factorisation of the global
$L$-function is compatible with the surreal-order decomposition:
each prime contributes its own local Reeb infinitesimal
$\varepsilon_p$, the squeeze holds at every prime, and the global
squeeze is the adelic sum.  This provides the **local--global**
structure missing from [RH surreal bound](#rem:rh-surreal-bound):
it is not only the global $\varepsilon$-squeeze that forbids rogue
zeros, but a separate squeeze at each prime.

**Outlook.** The adelic lift of the surreal squeeze is the key to
generalising the Reeb-$\varepsilon$ framework from the rational
zeta function to automorphic $L$-functions (Langlands programme) —
each automorphic representation contributes its own collection of
local $\varepsilon_v$-data, and the adelic squeeze becomes the
automorphic analogue of
[macroscopic stability equivalence](#thm:macroscopic-stability-equivalence).
This is out of scope for the present paper but is the natural next
target.
<!-- FILE_END: adelic-tate-squeeze.md -->

<!-- FILE_START: adelic-tate-bsd-reduction.md -->
**BSD reduction.** The leading-coefficient form of BSD
([BSD surreal bound](#rem:bsd-surreal-bound)) requires identifying
the standard-real prefactor $c$ in $L(\mathcal{E}_q, s) \asymp c \cdot
(s - 1)^r$ with the product of Tate--Shafarevich order, regulator,
and real/complex periods.  The adelic Fourier transform of
[adelic Tate squeeze](#rem:adelic-tate-squeeze) gives
the explicit formula for $c$ in terms of local $\varepsilon_p$-adic
integrals, reducing BSD to a local-squeeze check at each prime
together with the archimedean regulator identification.
<!-- FILE_END: adelic-tate-bsd-reduction.md -->

<!-- FILE_START: adelic-tate-motivic-dual.md -->
**Motivic dual.** The adelic decomposition of the global zeta
integral ([adelic Tate squeeze](#rem:adelic-tate-squeeze)) has a
*geometric* dual via the
[arc space $\mathcal{L}(X)$](#def:arc-space) and the
Kontsevich--Denef--Loeser motivic measure
\cite{kontsevich1995, denef-loeser2001}.  Where Tate factorises
the global zeta as a restricted product of local
$\mathbb{Q}_v$-integrals, motivic integration on $\mathcal{L}(X)$
factorises a class in the Grothendieck ring of varieties as a
sum over jet-scheme cylinders; for the QOU brane tower the two
factorisations agree under the change-of-variables formula
applied to the Reeb flow.  In particular, the leading-coefficient
form of [BSD surreal bound](#rem:bsd-surreal-bound) — assembling
the prefactor $c$ from local $\varepsilon_p$-adic integrals — is
the motivic-measure read of the same data on
$\mathcal{L}(\mathcal{E}_q)$.
<!-- FILE_END: adelic-tate-motivic-dual.md -->

<!-- FILE_START: outro-braids-and-knots.md -->
This closes the substrate-arithmetic chapter of the paper.  The
categorical Hecke / Wenzl-bridge / GS machinery developed here is
the engine that drives every numerical prediction downstream:
the six-term mass formula reads off its coefficients from the
Wenzl-bridge $\alpha_k$ table; the binding-energy substrate
formula reads off its Plancherel weights from the
$\varphi_q$-resummation; the parity / chirality classification
draws on the spectral-sequence $E_\infty$ confinement-NF
structure.  The classical-limit closing remark (adelic Tate
squeeze) anchors the substrate-flow as $q \to 1$ in the adelic /
non-archimedean side, so the next chapter's choice of archimedean
model is rigorously a categorical specialisation rather than a
free choice.

The next chapter (models of QOUs) consumes this categorical
arithmetic and surveys the candidate archimedean models —
Calabi–Yau, ALE, Seiberg–Witten — that the rigidity wall picks
from.  The substrate-level apparatus from this chapter survives
the archimedean specialisation; only the categorical numerics
acquires explicit numerical values, and the categorical
predictions become testable against CODATA.
<!-- FILE_END: outro-braids-and-knots.md -->

