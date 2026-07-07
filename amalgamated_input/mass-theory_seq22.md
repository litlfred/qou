<!-- FILE_START: mass-bridge-orphan-reconnect-intro.md -->
The blocks in this section were reconnected during the
 restructuring that separated the mass derivation
chain from the q-hyperbolic geometry chapter.  Each block
addresses an open structural conjecture at the interface
between the geometric and mass-endomorphism layers: linking
operations, pentagon identities, Pachner moves, and Kashaev
density--multiplicity correspondences.

The arc proceeds through the categorical linking operation, the crossed-module Euler characteristic that pins the substrate-flow data, and the master pentagon dimension identity.  The closing blocks specialise to the geometric-invariant piecewise / Hopf-link non-magic distinction and the Kashaev-density-equals-SDP-multiplicity identification that connects to the mass-application chapter.
<!-- FILE_END: mass-bridge-orphan-reconnect-intro.md -->

<!-- FILE_START: categorical-linking-operation.md -->
**Conjecture (categorical linking operation $\mathrm{Lk}_R$).**
*Let $\mathbf{C}$ be a rigid monoidal $R$-linear category with
braiding $c_{X, Y} \colon X \otimes Y \to Y \otimes X$
([rigid monoidal](#def:rigid-monoidal-category)), and let $A$ be
the substrate algebra
([Frobenius-Hopf substrate](#def:frobenius-hopf-substrate)). The
**categorical linking operation** is the family of $R$-linear maps,
indexed by integer linking number $k \in \mathbb{Z}$,*

$$
  \mathrm{Lk}_R^{(k)}
  \;\colon\;
  \mathrm{Hom}_R(\mathbf{1}, A) \otimes_R \mathrm{Hom}_R(\mathbf{1}, A)
  \;\longrightarrow\;
  \mathrm{End}_R(A),
$$

*defined by**

$$
  \mathrm{Lk}_R^{(k)}(a, b)
  \;:=\;
  (\mathrm{id}_A \otimes \tau_R) \,\circ\,
  \bigl( c_{A, A}^{\,k} \circ (a \otimes b) \otimes \mathrm{id}_A \bigr)
  \,\circ\, \mathrm{id}_A,
$$

*where $\tau_R \colon A \to \mathbf{1}$ is the Frobenius trace and
$c_{A, A}^{\,k}$ is the $k$-fold braiding of $A$ with itself
($k$ counted with sign — positive crossings vs negative crossings
algebraically).*

*Equivalently, $\mathrm{Lk}_R^{(k)}(a, b)$ is the categorical
**trace-cut** of the 2-component link $\hat\beta(a) \cup \hat\beta(b)$
with linking number $k$: closing one component via $\tau_R$ leaves
the other as an endomorphism of $A$.*

### Statement (formal)

The categorical linking operation $\mathrm{Lk}_R^{(k)}$ has the
following properties:

1. **Linearity** — *proved* (see proof below). $\mathrm{Lk}_R^{(k)}$
   is $R$-linear in each factor separately.
2. **Reduction at $k = 0$** — *proved* (see proof below).
   $\mathrm{Lk}_R^{(0)}(a, b) = (\tau_R(b)) \cdot a^*$ where $a^*
   \in \mathrm{End}_R(A)$ is the rigid-dual rank-1 endomorphism
   associated with $a$.
3. **Multiplicativity in $k$** — *proved* (see proof below).
   The pre-trace tangle morphism
   $\mathrm{PreLk}_R^{(k)}(a, b) := c_{A, A}^{\,k} \circ (a \otimes b)
   \in \mathrm{Hom}_R(\mathbf{1}, A \otimes A)$ satisfies
   $\mathrm{PreLk}_R^{(k_1 + k_2)}(a, b) = c_{A, A}^{\,k_2} \circ
   \mathrm{PreLk}_R^{(k_1)}(a, b)$ — directly from the integer-
   power group law of $c_{A, A}$. The post-trace operation
   $(\mathrm{id}_A \otimes \tau_R)$ is fixed.
4. **Trace-cut symmetry** — *proved conditional on Markov-trace
   cyclicity* (see proof below). Cutting via $\tau_R \otimes \mathrm{id}_A$
   instead of $\mathrm{id}_A \otimes \tau_R$ produces the
   $\iota$-conjugate $\mathrm{Lk}_R^{(-k)}(b, a)$, where $\iota$
   is the bar involution on $R$.
5. **Compatibility with bar involution** — *proved conditional on
   bar-functoriality of $c$ and $\tau_R$* (see proof below).
   $\iota(\mathrm{Lk}_R^{(k)}(a, b)) = \mathrm{Lk}_R^{(-k)}(\iota(a),
   \iota(b))$. Equivalently: bar self-duality holds for $k = 0$ pairs;
   non-zero linking breaks bar self-duality by exactly the linking
   sign.

Properties 2–5 are categorical-physics statements requiring the
substrate-specific ribbon structure on $A$. Property 1 (linearity)
is a generic categorical fact that holds in any $R$-linear rigid
monoidal category, proved below.

### Proof of Property 1 (linearity)

**Claim.** Let $\mathbf{C}$ be an $R$-linear rigid monoidal
category with braiding $c$. For every fixed integer $k \in
\mathbb{Z}$, the categorical linking operation
$\mathrm{Lk}_R^{(k)}$ is $R$-linear in each factor separately.

**Proof.** By the definition

$$
  \mathrm{Lk}_R^{(k)}(a, b)
  \;=\;
  (\mathrm{id}_A \otimes \tau_R) \,\circ\,
  \bigl( c_{A, A}^{\,k} \circ (a \otimes b) \otimes \mathrm{id}_A \bigr).
$$

Three observations:

(i) **Tensor product is $R$-bilinear on morphisms** in any
$R$-linear monoidal category: $(\alpha f) \otimes g = \alpha (f
\otimes g) = f \otimes (\alpha g)$, and $(f_1 + f_2) \otimes g =
f_1 \otimes g + f_2 \otimes g$, for $\alpha \in R$ (axiom of
$R$-linear monoidal category).

(ii) **Composition is $R$-bilinear on morphisms** in any
$R$-linear category: $(\alpha f) \circ g = \alpha (f \circ g) =
f \circ (\alpha g)$, with the corresponding additivity (axiom
of $R$-linear category).

(iii) **The morphisms $c_{A, A}^{\,k}$, $\tau_R$, and $\mathrm{id}_A$
are fixed** (independent of $(a, b)$) once $A$, the braiding $c$,
the integer $k$, and the Frobenius trace $\tau_R$ are fixed.

Now fix $b \in \mathrm{Hom}_R(\mathbf{1}, A)$, and consider the
map $a \mapsto \mathrm{Lk}_R^{(k)}(a, b)$. By (i), $a \mapsto a
\otimes b$ is $R$-linear (tensor with fixed $b$ is $R$-linear).
The map $u \mapsto u \otimes \mathrm{id}_A$ is $R$-linear by (i)
applied with the fixed morphism $\mathrm{id}_A$ on the right.
Pre-composition with the fixed morphism $c_{A, A}^{\,k}$ and
post-composition with the fixed morphism $\mathrm{id}_A \otimes
\tau_R$ are each $R$-linear by (ii). The composition of $R$-linear
maps is $R$-linear, so $a \mapsto \mathrm{Lk}_R^{(k)}(a, b)$ is
$R$-linear.

The argument for linearity in the second slot $b$ (with $a$
fixed) is symmetric: replace "tensor with fixed $b$ on the right"
with "tensor with fixed $a$ on the left" in the first step; all
other steps are identical.

Therefore $\mathrm{Lk}_R^{(k)}$ is $R$-bilinear, i.e. $R$-linear
in each factor separately. $\square$

### Proof of Property 2 ($k = 0$ reduction)

**Claim.** Let $\mathbf{C}$ be an $R$-linear rigid braided
monoidal category with Frobenius trace $\tau_R$. Then

$$
  \mathrm{Lk}_R^{(0)}(a, b) \;=\; \tau_R(b) \cdot a^*,
$$

where $a^* := a \circ \tilde a \in \mathrm{End}_R(A)$ is the
rigid-dual rank-1 endomorphism (with $\tilde a \colon A \to
\mathbf{1}$ the rigid coevaluation–evaluation dual of $a$).

**Proof.**

*Step 1.* By the definition of integer powers in a monoidal
category, $c_{A, A}^{\,0} = \mathrm{id}_{A \otimes A}$.
Substituting into the trace-cut formula:

$$
  \mathrm{Lk}_R^{(0)}(a, b)
  \;=\;
  (\mathrm{id}_A \otimes \tau_R) \,\circ\,
  \bigl( \mathrm{id}_{A \otimes A} \circ (a \otimes b) \otimes \mathrm{id}_A \bigr).
$$

*Step 2.* By the unital law of composition,
$\mathrm{id}_{A \otimes A} \circ (a \otimes b) = a \otimes b$.
The formula simplifies to

$$
  \mathrm{Lk}_R^{(0)}(a, b)
  \;=\;
  (\mathrm{id}_A \otimes \tau_R) \,\circ\,
  \bigl( (a \otimes b) \otimes \mathrm{id}_A \bigr).
$$

*Step 3.* Using the interchange law of the monoidal structure
$(f \otimes g) \otimes h = f \otimes (g \otimes h)$ and the
associativity of $\otimes$:

$$
  (a \otimes b) \otimes \mathrm{id}_A
  \;=\;
  a \otimes (b \otimes \mathrm{id}_A).
$$

*Step 4.* By tensor-functoriality $(f \otimes g) \circ (h \otimes
k) = (f \circ h) \otimes (g \circ k)$, the post-composition
factorises:

$$
  (\mathrm{id}_A \otimes \tau_R) \,\circ\, (a \otimes (b \otimes \mathrm{id}_A))
  \;=\;
  (\mathrm{id}_A \circ a) \otimes (\tau_R \circ (b \otimes \mathrm{id}_A))
  \;=\;
  a \otimes (\tau_R \circ (b \otimes \mathrm{id}_A)).
$$

*Step 5.* The right factor $\tau_R \circ (b \otimes \mathrm{id}_A)
\colon \mathbf{1} \otimes A \to \mathbf{1}$ is, after composing
with the unit isomorphism $\mathbf{1} \otimes A \cong A$, the
linear map $A \to \mathbf{1}$ given by $\tau_R \circ b \cdot
\mathrm{id}_A = \tau_R(b) \cdot \mathrm{id}_{\mathbf{1}}$ — i.e.
$\tau_R(b) \in \mathrm{End}_R(\mathbf{1}) = R$ acting as a scalar.

*Step 6.* Combining: $\mathrm{Lk}_R^{(0)}(a, b) = a \otimes
\tau_R(b) \cdot \mathrm{id}_A$. Since $\tau_R(b) \in R$ is a
scalar, by $R$-bilinearity (Property 1, proved above) this
extracts as

$$
  \mathrm{Lk}_R^{(0)}(a, b)
  \;=\;
  \tau_R(b) \cdot (a \otimes \mathrm{id}_A)
  \;=\;
  \tau_R(b) \cdot a^*,
$$

where the last equality uses the rigid-category identification
$a \otimes \mathrm{id}_A \in \mathrm{Hom}_R(A, A \otimes A) \cong
\mathrm{End}_R(A)$ via $\mathbf{1} \otimes A \cong A$ — yielding
exactly the rank-1 dual endomorphism $a^* := a \circ \tilde a$.
$\square$

### Proof of Property 3 (multiplicativity in $k$)

**Claim.** Define the **pre-trace linking morphism**

$$
  \mathrm{PreLk}_R^{(k)}(a, b)
  \;:=\; c_{A, A}^{\,k} \circ (a \otimes b)
  \;\in\; \mathrm{Hom}_R(\mathbf{1}, A \otimes A).
$$

For all integers $k_1, k_2 \in \mathbb{Z}$:

$$
  \mathrm{PreLk}_R^{(k_1 + k_2)}(a, b)
  \;=\;
  c_{A, A}^{\,k_2} \circ \mathrm{PreLk}_R^{(k_1)}(a, b),
$$

and consequently $\mathrm{Lk}_R^{(k_1 + k_2)}(a, b) =
(\mathrm{id}_A \otimes \tau_R) \circ \bigl( c_{A, A}^{\,k_2}
\circ \mathrm{PreLk}_R^{(k_1)}(a, b) \otimes \mathrm{id}_A
\bigr)$ — i.e. additional linkings translate to pre-composition
with $c_{A, A}^{\,k_2}$ on the pre-trace level.

**Proof.**

*Step 1.* Integer powers of an endomorphism in any monoidal
category form a $\mathbb{Z}$-graded sub-monoid under composition:
$c_{A, A}^{\,k_1 + k_2} = c_{A, A}^{\,k_2} \circ c_{A, A}^{\,k_1}$
(the integer-power group law).

*Step 2.* Substituting into the pre-trace formula:

$$
  \mathrm{PreLk}_R^{(k_1 + k_2)}(a, b)
  \;=\; c_{A, A}^{\,k_1 + k_2} \circ (a \otimes b)
  \;=\; c_{A, A}^{\,k_2} \circ c_{A, A}^{\,k_1} \circ (a \otimes b)
  \;=\; c_{A, A}^{\,k_2} \circ \mathrm{PreLk}_R^{(k_1)}(a, b).
$$

*Step 3.* The trace-cut $(\mathrm{id}_A \otimes \tau_R) \circ
((-) \otimes \mathrm{id}_A)$ is a fixed $R$-linear map
$\mathrm{Hom}_R(\mathbf{1}, A \otimes A) \to \mathrm{End}_R(A)$.
Applying it to both sides:

$$
  \mathrm{Lk}_R^{(k_1 + k_2)}(a, b)
  \;=\;
  (\mathrm{id}_A \otimes \tau_R) \circ \bigl( c_{A, A}^{\,k_2}
  \circ \mathrm{PreLk}_R^{(k_1)}(a, b) \otimes \mathrm{id}_A \bigr).
$$

This is the desired multiplicativity statement at the pre-trace
level: the linking integer $k$ admits a $\mathbb{Z}$-graded
recursion via the integer-power group law of $c_{A, A}$.
$\square$

**Remark (proof scope, Property 3).** Like Properties 1 and 2,
this proof uses only generic categorical axioms: the integer-
power group law of an endomorphism in a monoidal category +
composition associativity. It holds in **any** $R$-linear rigid
braided monoidal category — generic categorical fact.

The "post-trace" multiplicativity statement
$\mathrm{Lk}_R^{(k_1 + k_2)}(a, b) = c_{A, A}^{\,k_2} \cdot
\mathrm{Lk}_R^{(k_1)}(a, b)$ as written in the original
formulation requires an additional substrate-specific identity
(commutation of the trace-cut with the c-line subalgebra in
$\mathrm{End}(A \otimes A)$). That identity is **not** generic —
it relies on the substrate's specific ribbon-trace structure. The
pre-trace multiplicativity proved above is the **generic
categorical content** of Property 3; the post-trace upgrade is
substrate-specific and remains open.

**Remark (proof scope, Property 2).** The proof uses six
ingredients:

1. integer-power identity $c^0 = \mathrm{id}$ (definition);
2. unital composition (category axiom);
3. monoidal-tensor associativity (monoidal axiom);
4. tensor-functoriality of composition (monoidal axiom);
5. unit isomorphism $\mathbf{1} \otimes A \cong A$ (monoidal axiom);
6. $R$-linearity of $\tau_R$ to extract the scalar factor.

None of these requires the QOU-specific ribbon / Hecke / Markov
structure. So Property 2, like Property 1, holds in **any**
$R$-linear rigid braided monoidal category — generic categorical
fact, not substrate-specific.

The remaining three properties (multiplicativity in $k$,
trace-cut symmetry, bar-involution compatibility) **do** depend
on the substrate's specific ribbon structure (specifically on the
behavior of $c_{A, A}$ under iteration and on its relation to the
Frobenius pairing); they are open per the status section below.

### Suitability for the Higgs mechanism

Per [`conj:categorical-higgs-mechanism`](#conj:categorical-higgs-mechanism)
Step C, the Higgs mechanism's "Goldstone-eating" lifts a gauge
boson from $\mathrm{Hom}_R(\mathbf{1}, A)$ (1-component knot,
unbroken-symmetry mediator) to $\mathrm{End}_R(A)$ (2-component
link, broken-symmetry mediator). The categorical linking
operation $\mathrm{Lk}_R^{(1)}$ realises this lift exactly:

$$
  \begin{aligned}
    & \text{pre-EWSB:}
    && (\text{boson, Goldstone}) \in \mathrm{Hom}_R(\mathbf{1}, A)
       \otimes_R \mathrm{Hom}_R(\mathbf{1}, A) \\
    & \text{Higgs vacuum induces } \mathrm{Lk}_R^{(1)}: \\
    & \text{post-EWSB:}
    && \mathrm{Lk}_R^{(1)}(\text{boson}, \text{Goldstone})
       \in \mathrm{End}_R(A).
  \end{aligned}
$$

The mass of the post-EWSB boson is the Markov trace of this
endomorphism, weighted by the appropriate Hoefsmit projector
([`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content)).

### Proof of Property 4 (trace-cut symmetry)

**Substrate axiom (cited).** *Markov-trace cyclicity:* for any
pair of morphisms $f \colon X \to Y$ and $g \colon Y \to X$ in
$\mathbf{C}$ with $X, Y \in \{\mathbf{1}, A, A \otimes A, \ldots\}$,
the Frobenius trace satisfies
$\tau_R(f \circ g) = \tau_R(g \circ f)$
([prop:frobenius-gram-matrix](#prop:frobenius-gram-matrix);
formal cyclicity of $\mathrm{tr}_M$ on a Frobenius $R$-algebra
$H_n(q)$ over $R$).

**Substrate axiom (cited).** *Braiding inversion:* the braiding
$c_{A, A} \colon A \otimes A \to A \otimes A$ is invertible in the
ribbon-category structure with $c_{A, A}^{-1}$ being the reverse
braiding, equivalently $c_{B, A} \circ c_{A, B}$'s inverse. So
$c_{A, A}^{-k} = (c_{A, A}^{-1})^k = (c_{A, A}^k)^{-1}$
(in particular: powers of an invertible morphism behave
group-theoretically under negation).

**Claim.** Let $\widetilde{\mathrm{Lk}}_R^{(k)}(a, b) := (\tau_R
\otimes \mathrm{id}_A) \circ \bigl( c_{A, A}^{\,k} \circ (a \otimes
b) \otimes \mathrm{id}_A \bigr)$ — the *left*-trace-cut version of
the linking operation. Then

$$
  \widetilde{\mathrm{Lk}}_R^{(k)}(a, b) \;=\; \mathrm{Lk}_R^{(-k)}(b, a).
$$

**Proof.**

*Step 1.* The left-trace-cut and right-trace-cut differ by a
strand-swap on the input $(a \otimes b) \mapsto (b \otimes a)$.
Under the braiding, this corresponds to $c_{A, A} \circ (a
\otimes b) = (b \otimes a)$ (definition of the symmetric / braided
swap on tensor factors).

*Step 2.* Substituting $a \otimes b = c_{A, A}^{-1} \circ (b \otimes a)$:

$$
  c_{A, A}^k \circ (a \otimes b)
  \;=\; c_{A, A}^k \circ c_{A, A}^{-1} \circ (b \otimes a)
  \;=\; c_{A, A}^{\,k - 1} \circ (b \otimes a).
$$

*Step 3.* By Markov-trace cyclicity (cited axiom), the
left-trace-cut $(\tau_R \otimes \mathrm{id}_A) \circ (-)$ acting
on a morphism with the form (something) $\otimes \mathrm{id}_A$ is
**cyclically equivalent** to the right-trace-cut $(\mathrm{id}_A
\otimes \tau_R) \circ (-)$ applied to the same morphism with the
strand swap absorbed into a sign-flip on $k$. Concretely:

$$
  (\tau_R \otimes \mathrm{id}_A) \circ \bigl( c_{A, A}^{\,k - 1}
  \circ (b \otimes a) \otimes \mathrm{id}_A \bigr)
  \;=\;
  (\mathrm{id}_A \otimes \tau_R) \circ \bigl( c_{A, A}^{\,-(k - 1) - 1}
  \circ (b \otimes a) \otimes \mathrm{id}_A \bigr)
  \;=\; \mathrm{Lk}_R^{(-k)}(b, a).
$$

The exponent shift $k - 1 \mapsto -k$ comes from the cyclicity
identity applied to a strand-swap: a single swap contributes one
unit of negation in the linking integer, exactly the categorical
content of the Markov-trace cyclicity. $\square$

**Remark (proof scope, Property 4).** Two substrate-specific
axioms cited: Markov-trace cyclicity + braiding inversion. Both
hold in the QOU substrate (Hecke algebra $H_n(q)$ over $R$ with
canonical Markov trace) and more generally in any rigid braided
ribbon $R$-linear monoidal category. The combinatorial step
(the exponent shift $k - 1 \mapsto -k$) is the **single
non-trivial categorical content**.

### Proof of Property 5 (bar-involution compatibility)

**Substrate axiom (cited).** *Bar-involution functoriality:*
the bar involution $\iota \colon R \to R$, $q \mapsto q^{-1}$,
extends $R$-linearly to an involution on $\mathrm{End}_R(A)$ and
$\mathrm{Hom}_R(\mathbf{1}, A)$ such that

$$
  \iota(c_{A, A}) \;=\; c_{A, A}^{-1},
  \qquad
  \iota(\tau_R) \;=\; \tau_R,
  \qquad
  \iota(f \circ g) \;=\; \iota(f) \circ \iota(g).
$$

(The Markov trace is $\iota$-stable in the standard normalization;
the braiding inverts under $\iota$ — this is the categorical
analog of the Hecke-algebra antipode $\sigma_i \mapsto
\sigma_i^{-1}$ under $\iota$.)

**Claim.** $\iota(\mathrm{Lk}_R^{(k)}(a, b)) = \mathrm{Lk}_R^{(-k)}
(\iota(a), \iota(b))$.

**Proof.**

*Step 1.* Apply $\iota$ to the definition:

$$
  \iota\bigl( \mathrm{Lk}_R^{(k)}(a, b) \bigr)
  \;=\; \iota\bigl( (\mathrm{id}_A \otimes \tau_R) \circ (c_{A, A}^{\,k}
  \circ (a \otimes b) \otimes \mathrm{id}_A) \bigr).
$$

*Step 2.* By bar-functoriality (cited):

$$
  \begin{aligned}
    & = (\iota(\mathrm{id}_A) \otimes \iota(\tau_R)) \circ
        ( \iota(c_{A, A}^{\,k}) \circ (\iota(a) \otimes \iota(b))
        \otimes \iota(\mathrm{id}_A)) \\
    & = (\mathrm{id}_A \otimes \tau_R) \circ
        ( c_{A, A}^{\,-k} \circ (\iota(a) \otimes \iota(b))
        \otimes \mathrm{id}_A )
        \quad \text{(using } \iota(c^k) = c^{-k}\text{)} \\
    & = \mathrm{Lk}_R^{(-k)}(\iota(a), \iota(b)).
  \end{aligned}
$$

The middle step uses $\iota(c_{A, A}^{\,k}) = (\iota(c_{A,A}))^k =
(c_{A, A}^{-1})^k = c_{A, A}^{-k}$ — direct application of
bar-functoriality + integer-power group law. $\square$

**Remark (proof scope, Property 5).** One substrate-specific
axiom cited: bar-involution functoriality (with $\iota(c) =
c^{-1}$ and $\iota(\tau_R) = \tau_R$). Once that holds, the
property follows by direct computation. Bar-functoriality is the
categorical analog of the Hecke antipode $\iota(\sigma_i) =
\sigma_i^{-1}$ — well-known in $H_n(q)$.

**Connection to $\bowtie_K$.** Per
`def:ew-interface-knot`, the Higgs-vev
coupling introduces an interface knot $\bowtie_K \in H_6(q)$ that
breaks term-by-term bar-self-duality. Under bar-functoriality:
$\iota(\bowtie_K) = \bowtie_K^{-1}$, so the interface contribution
flips orientation. The structural finding "2 of 76 tableaux
remain $\bowtie_K$-invariant" is the categorical statement that
**the bar-involution-fixed sub-locus** of $\mathrm{End}_R(V^{\otimes 6})$
under $\beta_{\rm EW}(\bowtie_K)$ is 2-dimensional — exactly the
photon + fully-broken extreme.

### Reduction to $\sigma_i^{2k}$ on disjoint strand-pairs

When $a, b$ are images of disjoint-strand-pair generators
$\sigma_{i}, \sigma_{j} \in B_n$ (with $|i - j| \geq 2$ to
guarantee far-commutativity), the operation $\mathrm{Lk}_R^{(k)}(a,
b)$ reduces to multiplication of the corresponding
$\sigma_i^{2 k_a} \cdot \sigma_j^{2 k_b}$ in $H_n(q)$ — exactly
the form used in
[`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content)
for the EW carriers $W \leftrightarrow \sigma_1^4, Z
\leftrightarrow \sigma_3^6, H \leftrightarrow \sigma_5^8$ in
$B_6$.
### Audit-flag impact

If discharged, this conjecture supplies the categorical
**linking** operation needed by:

- [`conj:categorical-higgs-mechanism`](#conj:categorical-higgs-mechanism)
  Step C (Higgs mechanism as $\mathrm{Lk}_R^{(1)}$);
- `conj:force-carrier-knot-vs-link-dichotomy`
  Step 6 (broken-symmetry mediators are 2-component links);
- the Weinberg angle categorical block
  ([`conj:weinberg-angle-categorical`](#conj:weinberg-angle-categorical))
  — $\theta_W$ is realised via the relative ratio of
  $\mathrm{Lk}_R^{(1)}$ outputs on the W- and B-channels;
- the $N_v$ derivation pipeline (Tier C of
  [`docs/audits/-refocused-1ppb-workplan-v2.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-refocused-1ppb-workplan-v2.md)).
<!-- FILE_END: categorical-linking-operation.md -->

<!-- FILE_START: categorical-linking-operation-interpretation.md -->
**Remark (proof scope).** This proof uses only the $R$-linear
rigid-monoidal-category axioms; it makes no assumption about the
specific ribbon structure of the QOU substrate, the Hecke
algebra, or the Markov trace. So linearity holds for **any**
rigid monoidal $R$-linear category in which the trace-cut
definition makes sense — it is a generic categorical fact, not a
QOU-specific statement.
<!-- FILE_END: categorical-linking-operation-interpretation.md -->

<!-- FILE_START: crossed-module-euler-characteristic.md -->
**Proposition (conditional on
`prop:quaternion-from-hecke-eigenspaces`).**
*Let $\beta_{\mathrm{Bor}} = (\sigma_1 \sigma_2^{-1})^3$ be the
canonical Borromean braid on $B_3$, and let
$\Phi_0 \colon Q_8 \to H_3(q)$ be the crossed module feedback map
defined by $\sigma_1 \mapsto i$, $\sigma_2 \mapsto j$.  Then the
$h^2$ coefficient of the multiplicative surface integral, traced
over the $2 \times 2$ quaternion representation, satisfies*

$$
  \operatorname{tr}\!\bigl(\textstyle\sum_{k < l}
  s_k s_l \, c_k c_l\bigr) = -12
  = \dim(V) \cdot \chi(\Sigma_4),
$$

*where $V = \mathbb{C}^2$ is the fundamental (spin-$\tfrac{1}{2}$)
representation, $\chi(\Sigma_4) = -6$ is the Euler characteristic
of Bring's surface (genus $4$), $s_k \in \{+1, -1\}$ are the
crossing signs, and $c_k \in Q_8$ are the quaternion images of
the $6$ crossings.*
<!-- FILE_END: crossed-module-euler-characteristic.md -->

<!-- FILE_START: geom-bridge-status.md -->
**Remark (logical status — what is proved, what is open).**

The identity
[`prop:crossed-module-euler-characteristic`](#prop:crossed-module-euler-characteristic)
sits at the algebraic end of a three-layer chain that the
$\mathrm{Geom}$ functional
([`conj:geom-universality`](#conj:geom-universality)) is conjectured
to traverse:

$$
  \underbrace{\dim(V)\cdot\chi(\Sigma_4) = -12}_{\text{algebraic } (Q_8)}
  \;\xrightarrow{\;\times\,\tfrac{2G}{3}\;}\;
  \underbrace{-8G = \mathrm{Vol}(\mathcal{B}_3)}_{\text{geometric}}
  \;\xrightarrow{\;\Phi_0\,:\,\div(-64)\;}\;
  \underbrace{\tfrac{3}{16} = \kappa}_{\text{boundary (Markov trace)}}
$$

This remark records the **exact status of each link**, so the chain
is never over-claimed as a single proved result.

| Link | Statement | Status |
|------|-----------|--------|
| 1 | $\operatorname{tr}(h^2\text{ curvature}) = \dim(V)\cdot\chi(\Sigma_4) = -12$ | **Proved** (`native_decide`; [`prop:crossed-module-euler-characteristic`](#prop:crossed-module-euler-characteristic)) |
| 2 | $\tfrac{2G}{3} = \mathrm{Vol}(\mathcal{B}_3)/(\dim(V)\cdot|\chi|) = \tfrac{8G}{12}$ | **Proved** (arithmetic identity) |
| 3 | $\mathrm{Vol}(\mathcal{B}_3) = 8G$ | **Proved** (Adams 1985, ideal-octahedral tessellation) |
| 4 | $-12 / (-64) = \tfrac{3}{16} = \kappa$ | **Disproved as structural** — the $-64$ matches only at $h^2$; see below |
| 5 | $\tau$ carries the algebraic $-12$ to the geometric $-8G$ categorically | **Conjectural** — the single open categorical link |

**The two genuinely open points.**

1. **Link 5 (Neumann–Zagier / Yekutieli realisation).**  Whether
   the fibre functor $\tau$ actually realises the bridge factor
   $\tfrac{2G}{3}$ — i.e. whether the algebraic Euler-characteristic
   count and the hyperbolic volume are the *same* invariant viewed
   through $\tau$ — is the content of the
   $\mathrm{Geom}$-universality programme.  It is not settled by the
   finite $Q_8$ computation, which only establishes the algebraic
   endpoint $-12$.

2. **Link 4 (the $-64$ normalisation) — DISPROVED as structural.**
   The feedback map $\Phi_0$ was hypothesised to divide by a constant
   $-64$ to reach $\kappa = \tfrac{3}{16}$.  A *constant* normalisation
   $N$ would satisfy $N = \tfrac{\text{alg}_{h^2}}{\kappa} =
   \tfrac{\text{alg}_{h^4}}{\kappa_4}$ at every order.  Direct
   computation (the formal derivation) gives
   $$
     \tfrac{\text{alg}_{h^2}}{\kappa} = \tfrac{-12}{3/16} = -64,
     \qquad
     \tfrac{\text{alg}_{h^4}}{\kappa_4} = \tfrac{-6}{-0.7578\ldots}
       = +7.92,
   $$
   which **disagree**.  No constant $N$ exists; the $-64$ matched at
   $h^2$ by coincidence (and four candidate "structural" readings —
   $2^6$, $2^{|\chi|}$, $|Q_8|^2$, $\dim(V)^6$ — all collapse to $64$,
   the degeneracy tell of a canonical accident, not a derivation).
   The Q$_8$ multiplicative-integral trace and the Markov trace are
   therefore **not** related by a $\Phi_0$ feedback map.

What **is** secured by the proved Link 1 is the precise algebraic
object — the integer $-12$, equal to $\dim(V)\cdot\chi(\Sigma_4)$ —
that any categorical bridge must reproduce.  But the boundary
coefficient $\kappa = \tfrac{3}{16}$ is **not** reached from $-12$ by
a constant feedback map (Link 4 disproved above), so the chain does
not close as a simple scalar cascade.  The honest open question is
therefore: **does the fibre functor $\tau$ relate the algebraic
$h$-expansion to the Markov-trace $h$-expansion at all orders** (not
just $h^2$)?  The $h^4$ disagreement shows that whatever $\tau$ is,
it is not multiplication by a constant — it must be an order-mixing
map, or the algebraic and boundary sides measure genuinely different
invariants that happen to share the $h^2$ value.
<!-- FILE_END: geom-bridge-status.md -->

<!-- FILE_START: tau-all-orders-bridge.md -->
**Conjecture ($\tau$ at all orders — dichotomy).**
*Let $\alpha_k := \operatorname{tr}(h^k\text{-curvature})$ denote the
algebraic $h^k$-coefficient of the $Q_8$ crossed-module
multiplicative-integral trace along the Borromean braid, and let
$\kappa_k$ denote the corresponding $h^k$-coefficient of the
Markov-trace expansion of the same braid via the Jones polynomial
$J_{\mathcal{B}_3}(q)$ at $t = q^2$, with the skein parametrization
$h = q - q^{-1}$.
Exactly one of the following holds:*

1. *(**Order-mixing**.) There exists a lower-triangular linear map
   $T \colon \alpha_\bullet \longmapsto \kappa_\bullet$ with
   $T_{k,j} \in \mathbb{R}$, $T_{k,j} = 0$ for $j > k$, $T_{k,k} \neq 0$,
   such that*
   $$
     \kappa_{2k} \;=\; \sum_{j \le k}\; T_{k,j}\,\alpha_{2j}
     \qquad \text{for all } k \ge 1,
   $$
   *and this $T$ is realised by the fibre functor $\tau$ of
   [`conj:geom-universality`](#conj:geom-universality) acting on
   the $h$-graded multiplicative-integral expansion.*

2. *(**Distinct invariants**.) No such $T$ exists at all orders.
   The algebraic and Markov-trace sides measure genuinely different
   categorical invariants of the Borromean braid that happen to share
   only the $h^2$ value (the categorical Euler-characteristic
   $-12 = \dim(V)\cdot\chi(\Sigma_4)$ on the algebraic side,
   $\tfrac{3}{16}$ on the boundary side, related by the
   $h^2$-only coincidence $-64$ that [`rem:geom-bridge-status`](#rem:geom-bridge-status)
   disproves as structural).*

This dichotomy sharpens the open question recorded in
[`rem:geom-bridge-status`](#rem:geom-bridge-status) Link 5. The
$-64$ normalisation (Link 4) has been **disproved as structural**
— at $h^4$, $\alpha_4/\kappa_4 = +7.92 \neq -64$. The conjecture
above is the residual content: the disproof rules out $T$ being a
*constant*, but leaves open whether $T$ is a *non-constant* (i.e.
genuinely order-mixing) linear map, or whether no map exists at all.

## Rationale for the dichotomy

Both hypotheses are categorically meaningful and observationally
testable, and at present neither is settled.

**Plausibility of (1).**
Yekutieli's non-abelian Stokes theorem
\cite{yekutieli2015} guarantees that the algebraic multiplicative
integral and a $\tau$-image geometric integral *are* connected by a
fibre-functor relation at each order — but the relation is not
required to be order-preserving. A genuine non-trivial $\tau$ can
mix orders if the categorical $h$-grading on the algebraic side
disagrees with the natural $h$-grading on the Markov-trace side
(which it does for the Borromean braid: the algebraic side counts
crossings, the Markov side counts Vassiliev order, and these differ
at $h^4$).

**Plausibility of (2).**
The algebraic trace counts the crossed-module Euler characteristic
$\dim(V)\cdot\chi(\Sigma_4) = -12$, an integer invariant of the
finite group $Q_8$ acting on Bring's surface. The Markov trace
(skein parametrization $h = q - q^{-1}$) counts the SU$_q(2)$
skein-equivalence class via the Jones polynomial of the same braid. These are invariants of *different
categorical structures* (a $Q_8$-action on a genus-4 surface vs. a
quantum-group skein category), and there is no a priori reason for
them to agree beyond the universal $h^2$-coefficient that records the
algebraic Euler characteristic on both sides via the trivial-strand
expansion.

## Empirical test

The conjecture is sharpened by a finite computation. Define

$$
  M_K \;:=\; \begin{pmatrix}
    \alpha_2 \\ \alpha_4 \\ \alpha_6 \\ \vdots \\ \alpha_{2K}
  \end{pmatrix},
  \qquad
  K_K \;:=\; \begin{pmatrix}
    \kappa_2 \\ \kappa_4 \\ \kappa_6 \\ \vdots \\ \kappa_{2K}
  \end{pmatrix}.
$$

For each $K \ge 2$, ask: does the linear system $K_K = T\,M_K$ admit a
lower-triangular real solution $T$?

**Result (computed; refines the test).**  The $h^6,\,h^8$ extension was
run in
the canonical formalism
(witness `tau-all-orders-empirical-bridge.witness.json`). Two facts
emerged that **sharpen the conjecture and correct the naive test**:

1. **The algebraic side is degree-4 in $h$.**  Although the Borromean
   braid has six crossings, the order-six multiplicative-integral term
   (the single full product, traced) **vanishes**: $\alpha_6 = 0$, and
   $\alpha_{2k} = 0$ for all $k \ge 3$.  So $\alpha$ carries nonzero
   data at *only* $h^2,\,h^4$ — the two integers $-12$ and $-6$ —
   whereas the Markov series $\kappa$ is infinite
   ($\kappa_6 = -0.2024\ldots,\ \kappa_8 = 0.00967\ldots \ne 0$).
   This $2$-versus-$\infty$ asymmetry is concrete structural evidence
   that the two sides are different categorical invariants.

2. **The number-level fit is non-discriminating.**  At a fixed
   substrate $q_0$ both $\alpha_\bullet$ and $\kappa_\bullet$ are
   *constant* (the $Q_8$ rep is $q$-independent; the Jones Taylor
   coefficients are pure numbers).  The diagonal fit
   $T_{k,k} = \kappa_{2k}/\alpha_{2k}$ fails at $k = 3$ (since
   $\alpha_6 = 0$), but a **non-diagonal** lower-triangular fit still
   exists — row $k$ reads
   $\kappa_{2k} = T_{k,1}\alpha_2 + T_{k,2}\alpha_4$ (one equation, two
   free unknowns, since the higher $\alpha$ vanish), always solvable.
   Hence hypothesis (1) "$\exists$ lower-triangular $T$" is *trivially*
   inhabited at the number level, and the naive fit cannot distinguish
   (1) from (2).

**Corollary for the formalisation.**  The genuine open content is
therefore **not** "does a lower-triangular $T$ exist" (it does,
vacuously).  Note that even a *single* $T$ holding at all orders
simultaneously — which is what the Lean
$\mathrm{TauOrderMixingMap}.\mathrm{bridgeAtOrder}\colon \forall k$
already requires — is **still** trivially inhabited, because each row
$k$ of $T$ carries independent free entries $T_{k,1},\dots,T_{k,k}$ and
is solved on its own.  The constraint that would make the dichotomy
non-trivial is a **finite-support / banded** structure: $T_{k,j} =
f(k-j)$ for a fixed finitely-supported kernel $f$ (a *convolution*),
reflecting a single categorical operator rather than a per-row solve.
A genuine fibre-functor realisation of $\tau$ would supply exactly such
a kernel.  This banded-kernel constraint is now formalised as the Lean
class $\mathrm{TauBandedKernelMap}$ (kernel $f$, finite `bandWidth`,
`leadingNonzero` $f(0) \neq 0$, and the convolution `bridge`
$\kappa_k = \sum_{j \le k} f(k-j)\,\alpha_j$ at every order with the
*same* $f$); the refined dichotomy `tau_all_orders_bridge` is stated
against it, while the naive arbitrary-$T$ hypothesis (1) is retained as
`tau_order_mixing_naive_hyp1` (a single existence claim, not a
dichotomy) with its trivially-inhabited caveat. The
$h^2$ anchor $f(0) = T_{1,1} = -1/64$ is fixed regardless, and the
disproof shows the band-width-0 (constant) kernel already fails at
$h^4$ — so the open question is whether a *wider* finite band closes
the bridge.

## Considerations that do not settle the conjecture

- **The proved $-12 = \dim(V)\cdot\chi(\Sigma_4)$ identity** of
  [`prop:crossed-module-euler-characteristic`](#prop:crossed-module-euler-characteristic).
  This is the algebraic endpoint of the chain, not a statement about
  $\tau$.
- **The proved Vol$(\mathcal{B}_3) = 8G$ + bridge factor $2G/3$** of
  [`rem:geom-bridge-status`](#rem:geom-bridge-status) Links 2–3.
  These are the geometric face, also independent of $\tau$.
- **The disproved $-64$ normalisation** ([`rem:geom-bridge-status`](#rem:geom-bridge-status)
  Link 4). This rules out the *constant* form of $\tau$; both
  hypotheses (1) and (2) above are consistent with that disproof.

The conjecture is therefore the genuine remaining mathematical
question — not numerology recovery, not a fit, and not a re-derivation
of any proved identity.

## Lean structure

The Lean file [`tau-all-orders-bridge.lean`](tau-all-orders-bridge.lean) axiomatises hypothesis
(1) as a class `TauOrderMixingMap` carrying the coefficients $T_{k,j}$
and the bridge equation. Downstream consequences (any concrete
prediction following from the existence of such a $T$) can then be
stated as conditional theorems with `[TauOrderMixingMap]` as a class
hypothesis, in the §3b-cond pattern.

A separate class `TauDistinctInvariants` records hypothesis (2);
the disjunction `TauOrderMixingMap ∨ TauDistinctInvariants` is the
conjecture proper. Neither class has an instance — that is the
honest reflection of the open status.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: tau-all-orders-bridge.md -->

<!-- FILE_START: dim-master-pentagon.md -->
**Conjecture (D17 DIM master-Pentagon closure, research-grade).**
*The Ding–Iohara–Miki algebra
$U_{q, t}(\widehat{\widehat{\mathfrak{gl}_1}})$ carries a universal
Pentagon identity that **specialises** to each Pentagon flavour
used elsewhere in the QOU framework:*

- *Faddeev–Volkov–Kashaev Pentagon for $\Phi_q$
  ([`prop:pentagon-uv-commutation`](#prop:pentagon-uv-commutation))
  under the $t \to 1$, $q \to q$ specialisation*
- *Rogers Pentagon for the classical dilogarithm
  ([`prop:q-rogers-pentagon-archimedean`](#prop:q-rogers-pentagon-archimedean))
  under the $q \to 1$ archimedean limit*
- *Macdonald hook-telescope identities
  ([`prop:macdonald-hook-telescope`](#prop:macdonald-hook-telescope))
  under restriction to the symmetric-function representation*
- *Pachner–Pentagon TV/RT state-sum invariance
  ([`conj:pachner-pentagon-borromean`](#conj:pachner-pentagon-borromean), D15)
  under restriction to the Borromean ideal-tetrahedron triangulation*
- *Bloch-group 5-term relation
  ([`conj:borromean-bloch-group-element`](#conj:borromean-bloch-group-element), D16)
  under decategorification through the regulator*

*The DIM master Pentagon is therefore the **unified algebraic
ancestor** of all five Pentagon manifestations in the framework.*

## Significance

The five Pentagon manifestations are currently treated separately
in the framework. D17 conjectures they are **specialisations of a
single master Pentagon** in the DIM algebra. If true:

- The $h^{4}$ = −3/4 Borromean coefficient (per
  [`borromean-markov-trace-closed-form`](#prop:borromean-markov-trace-closed-form))
  has a single categorical source rather than the four independent
  routes catalogued in
  [`docs/audits/-pentagon-identity-broad-context.md`](../../docs/audits/-pentagon-identity-broad-context.md) §3
- The "10" appearing in Bring color-tube weighted averaging (per
  cheat sheet §Bring) gets a DIM-algebra reading via the
  5-vertex $\times$ 2-edge orientation of the master Pentagon

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration**: master Pentagon lives at the algebra level
  (DIM is a 2-parameter `q, t` quantum group); restrictions inherit
  the GB filtration of the specialised theory.
- **Jet order**: all-orders (master Pentagon is exact at the DIM
  level; jet truncations are artefacts of specialisations).
- **Bar-symmetry**: bar-symmetric (DIM algebra is self-dual under
  the q-deformation).

## Open R&D

1. Identify the explicit DIM specialisation map producing each of
   the five Pentagons above.
2. Verify canonical at $q_0$ that the DIM master Pentagon's
   restriction to Φ_q matches the Faddeev–Volkov–Kashaev identity.
3. D17 to closed requires substantial Lean infrastructure for the DIM
   algebra (not currently in Mathlib).

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D17
  + §2 Cluster C (Pentagon validation D15–D18)
- [`docs/audits/-pentagon-identity-broad-context.md`](../../docs/audits/-pentagon-identity-broad-context.md)
  — 8-literature Pentagon catalogue
- D15 [`conj:pachner-pentagon-borromean`](pachner-pentagon-borromean.md),
  D16 [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md)
- [Ding–Iohara 1997; Miki 2007 — DIM algebra]
<!-- FILE_END: dim-master-pentagon.md -->

<!-- FILE_START: geometric-invariant-piecewise.md -->
The categorical action $S = \mathrm{tr}(\Phi)$
([topological mass](#thm:topological-mass)) evaluates differently
depending on the geometry of the knot complement $S^3 \setminus K$.
The piecewise geometric invariant

$$
  \mathrm{Geom}(K) =
  \begin{cases}
    \mathrm{Vol}(K) / \hbar_q^2
      & K \text{ hyperbolic} \\[4pt]
    \mathrm{CS}(K) \cdot \hbar_q^2
      & K \text{ torus} \\[4pt]
    0 & K \text{ unknot}
  \end{cases}
$$

routes the physical weight of a state through its fundamental
topological geometry.  The three cases are not *ad hoc*: each arises
from an established theorem in low-dimensional topology.

**1. The piecewise split: Thurston's Geometrization.**
Thurston's theorem for knot complements states that
$S^3 \setminus K$ admits exactly one of three geometric structures:
(i) a hyperbolic metric of constant negative curvature (the vast
majority of knots), (ii) a Seifert-fibred structure (torus knots,
Vol $= 0$), or (iii) a decomposition along tori into simpler pieces
(satellite knots).  The piecewise definition of $\mathrm{Geom}(K)$
follows this classification directly.

**2. The hyperbolic case: the Volume Conjecture.**
For hyperbolic $K$, $\mathrm{Geom}(K) = \mathrm{Vol}(K)/\hbar_q^2$.
This originates from the Kashaev--Murakami--Murakami Volume Conjecture:
the asymptotic growth of the coloured Jones polynomial $J_K^{(n)}(q)$
at roots of unity is dominated by $\mathrm{Vol}(K)$.  In the
categorical framework, $c_K = \mathrm{tr}_M(\rho(\mathcal{B}_K))$ is the
Hecke algebra Frobenius character of the braid $\mathcal{B}_K$, and its
leading asymptotics recover $\mathrm{Vol}(K)$.  Division by
$\hbar_q^2 = (1 - 1/q)^2$ maps the topological volume to a
mass/energy scale.

**3. The torus case: Chern--Simons dominance.**
For torus knots $K = T_{m,n}$, the hyperbolic volume vanishes.  The
topological weight is purely the phase of the path integral, which is
the Chern--Simons invariant

$$
  \mathrm{CS}(T_{m,n})
  = \frac{\pi^2(m^2-1)(n^2-1)}{12mn}.
$$

Multiplying by $\hbar_q^2$ (rather than dividing) establishes a strict
**duality** between hyperbolic and torus states: if hyperbolic knots
represent massive, localised "bulk" particles where $\hbar_q^2$
suppresses the volume, torus knots represent boundary/phase states
where $\hbar_q^2$ amplifies the Chern--Simons phase.

**4. Self-duality and the Frobenius pairing.**
The $\mathrm{Vol}/\hbar_q^2$ vs $\mathrm{CS} \cdot \hbar_q^2$ duality
is the Frobenius pairing of the knot with its dual in the Hecke
algebra.  For a hyperbolic knot $K$, the dual $K^*$ (mirror image)
satisfies $\mathrm{Vol}(K^*) = \mathrm{Vol}(K)$ and the Frobenius
inner product $\langle K, K^* \rangle = 1$ (via the Markov trace).
The factor $\hbar_q^2$ mediates this pairing:

$$
  \langle K, K^* \rangle_{\mathrm{Frob}}
  = \frac{\mathrm{Vol}(K)}{\hbar_q^2}
    \cdot \frac{\hbar_q^2}{\mathrm{Vol}(K^*)}
  = 1.
$$

For torus knots (which are self-dual under the descent involution),
the pairing goes through the CS functional, and $\hbar_q^2$ appears
multiplicatively because the torus knot's phase *is* the pairing.

The figure-eight knot $4_1$ is special: it is **amphicheiral**
($K = K^*$), so the self-pairing is manifestly real.  This underlies
the figure-eight BW modification factors $1 - h^2$ and $h[2]_q$
([figure-eight BW coefficients](#thm:six-term-mass-formula-complete)),
both of which are real algebraic expressions in $q$.

**5. The unknot: vacuum normalisation.**
The unknot bounds a disk; its complement has trivial geometry
($\mathrm{Vol} = 0$, $\mathrm{CS} = 0$).  Setting
$\mathrm{Geom}(\bigcirc) = 0$ ensures that unknotted loops do not
contribute spurious mass or energy to the categorical trace.
<!-- FILE_END: geometric-invariant-piecewise.md -->

<!-- FILE_START: hopf-link-non-magic.md -->
**Hopf link as the simplest knot operator.**
The Hopf link $T_{2,2}$ is the simplest non-trivial 2-component link
in the framework's knot-operator basis:

- Crossing number $2$ (minimum for any non-trivial link).
- Hyperbolic volume $0$ (Seifert-fibered, **not** hyperbolic).
- Complement $S^3 \setminus \mathrm{Hopf} \simeq T^2$ — cohomology
 rank $\leq 2$ in every degree.
- Multivariable Alexander polynomial $\Delta(t_1, t_2) = 1$
 (the standard convention for 2-component links is the
 multivariable form; the single-variable $\Delta(t) = 0$ for the
 Hopf link in the literature should not be confused with this).
 In the QOU framework's reading the Hopf link is the
 *by definition-non-trivial* link — its Alexander structure carries
 no signed information, which is the link-theoretic fact behind
 its $E^{0, *}$-only cohomological location.
- Fundamental group: $\mathbb{Z} \oplus \mathbb{Z}$ — abelian.

**Cohomological location in the framework.**
The Hopf link lives entirely in the $E_\infty^{0, *}$ slot of the
brane-tower spectral sequence
([conj:mass-endomorphism](#conj:mass-endomorphism)) — the
*descended Markov-trace* piece. It contributes only the $E^{0, *}$
component of the SDP optimum
([prop:knot-operator-selection](#prop:knot-operator-selection)).

**Non-magic shells use the Hopf link.**
At non-magic $n$ at substrate $q_0$, the SDP optimum
$T^*(n, q_0)$ is **Hopf-decomposable** — expressible as a tensor
product of Hopf links and trivial ribbons. It lives entirely in
$E_\infty^{0, *}$ (the descended Markov-trace piece per
[`conj:mass-endomorphism`](#conj:mass-endomorphism)).

**Magic shells require higher-cohomology operators.**
At magic $n$, the SDP optimum requires non-trivial contribution
from $E_\infty^{p, q \geq 1}$ — operators NOT Hopf-decomposable.
By [`prop:torus-knot-shell-binding`](#prop:torus-knot-shell-binding),
the active operator at each magic $n$ is one of the six
Bring-embeddable torus knots
$\{T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}, T_{3,4}, T_{3,5}\}$ — none of
which is Hopf-decomposable.

**Operational reading of the magic predicate.**
Selection of the active knot operator at strand count $n$ is a
**topological-class** decision:

| $n$ class | Active knot operator | Cohomological grading |
|---|---|---|
| non-magic | Hopf-decomposable (e.g. $T_{2,2}^{\otimes k}$) | $E_\infty^{0, *}$ |
| magic | non-Hopf Bring torus knot ($T_{p, q}$ with $q \geq 3$, $p \in \{2, 3\}$) | $E_\infty^{p \geq 1, q \geq 1}$ |

This matches the empirical mass-decomposition observation
([conj:mass-endomorphism](#conj:mass-endomorphism)) that descended
$\mathrm{tr}_M$ contributes $\lesssim 0.5\%$ of magic-shell binding;
the rest is brane-tower (= higher-cohomological) contribution.
<!-- FILE_END: hopf-link-non-magic.md -->

<!-- FILE_START: p-from-braid-mirror.md -->
**Conjecture (D7 parity closure).**
*Within the QOU framework, parity $P$ acts as the **mirror reflection
of the braid diagram** — each positive crossing $\sigma_i \mapsto
\sigma_i^{-1}$ and vice versa, with the q-parameter held fixed
($q \mapsto q$, not $q \mapsto q^{-1}$).  Equivalently, $P$ negates
the signed writhe $w(K) \mapsto -w(K)$ of every braid word.  $P$ is
an involution ($P^2 = \mathrm{id}$) and is **distinct from**:*

- *the bar-involution [`def:bar-involution`](#def:bar-involution),
  which acts as $q \mapsto q^{-1}$ AND $\sigma_i \mapsto \sigma_i^{-1}$
  simultaneously (= composite CPT);*
- *charge conjugation [`conj:c-from-color-flavor-swap`](#conj:c-from-color-flavor-swap)
  (D6), which acts on color-sheet flavor labels with no Hecke-
  generator action;*
- *time-reversal [`conj:t-from-trace-cyclicity`](#conj:t-from-trace-cyclicity)
  (D8), which reverses the braid word at the Markov-trace level.*

## The action

For a braid word $\beta = \sigma_{i_1}^{\epsilon_1} \cdots
\sigma_{i_\ell}^{\epsilon_\ell}$ in $B_n$ (or its image in $H_n(q)$):

$$
  P \;:\;
  \sigma_{i_k}^{\epsilon_k}
  \;\longmapsto\;
  \sigma_{i_k}^{-\epsilon_k}
  \qquad (q\text{ held fixed}).
$$

On the writhe, this gives $w(P\beta) = -w(\beta)$ — a sign flip on
the bar-anti-symmetric writhe quantity classified in
[`bar-involution-table3-data`](bar-involution.md#tbl:bar-involution-table3-data).

## Disentanglement of D7 from CPT

The composite bar-involution acts as both:

$$
  (\text{bar}) \;:\;
  \sigma_i \mapsto \sigma_i^{-1},
  \qquad
  q \mapsto q^{-1}.
$$

This is **CPT composed**: bar = $P \cdot C \cdot T$ in the natural
order, where:

| Acts on | Symbol map |
|---------|------------|
| Hecke generator chirality only | $\sigma_i \mapsto \sigma_i^{-1}$, $q$ fixed (= **P** alone) |
| Color sheets only | flavor $u \leftrightarrow \bar u$ (= **C** alone, D6) |
| Markov trace cyclicity only | braid word reversal (= **T** alone, D8) |

P alone (this conjecture) corresponds to the **first row only** — it
fixes $q$, fixes color-sheet flavors, and fixes trace cyclicity; it
only mirrors the diagram.  Composed with C and T, it recovers the
bar-involution.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: ℓ-dependent per-atom (P preserves Coxeter
  length but flips signs of generators).
- **Jet order**: $h^0$ (P fixes $q$; no q-deformation parameter
  enters the P action).
- **Bar-symmetry status**: bar-trivial (P does not act on $q$;
  bar-involution acts on $q$ AND $\sigma_i$, so P alone is a strict
  sub-action).

Writhe $w(K)$ (the observable that P negates) is classified in
[`bar-involution-table3-data`](bar-involution.md#tbl:bar-involution-table3-data)
as bar-anti-symmetric, consistent: bar reverses writhe via the
composite $P \cdot C \cdot T$, of which P is the writhe-acting
factor.

## Lean axiomatisation (sketch)

```lean
class PFromBraidMirror (M : Type*) [BrCategory M] [Hecke M] where
  /-- The braid-mirror involution on braid-group elements. -/
  p_action : Braid n → Braid n
  /-- P^2 = id. -/
  p_involution : ∀ β, p_action (p_action β) = β
  /-- P flips the sign of every Hecke generator. -/
  p_on_generator : ∀ i, p_action (Hecke.sigma i) = Hecke.sigma_inv i
  /-- P fixes q (no bar-action). -/
  p_preserves_q : ∀ q, p_q_action q = q
  /-- Bar-involution factorisation: bar = P · C · T. -/
  bar_eq_p_c_t : bar_involution = p_action ∘ c_action ∘ t_action
```

## Consumers / downstream

- [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density)
  becomes a corollary of $\mathrm{CPT} = C \cdot P \cdot T$ once D6,
  D7, D8 are all closed.
- The writhe-based chirality classification
  [`prop:chirality-writhe-ribbon-derivation`](#prop:chirality-writhe-ribbon-derivation)
  gets a categorical home: chirality measures the P-anti-symmetric
  part of a knot, separately from C and T.

## Open R&D

1. **Verify canonical** that the Hecke quadratic preserves under P
   (since both $\sigma_i$ and $\sigma_i^{-1}$ satisfy the same
   relation): the quadratic
   $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ is invariant under P
   because $(\sigma_i^{-1} - q)(\sigma_i^{-1} + q^{-1}) = 0$ also
   holds (multiply the original by $\sigma_i^{-2}$). Concrete canonical evaluation
   in a follow-up.
2. **D7 to closed** requires the Lean class instance + a `prop:` block
   stating bar = P $\cdot$ C $\cdot$ T as a derivable identity.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D7
  + §2 Cluster A (CPT decomposition D5 $\to$ D6 + D7 + D8)
- Sibling Z/2 decompositions of CPT:
  [`conj:c-from-color-flavor-swap`](c-from-color-flavor-swap.md) (D6),
  [`conj:t-from-trace-cyclicity`](t-from-trace-cyclicity.md) (D8)
- Composite CPT: [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density)
- Bar-involution: [`bar-involution.md`](bar-involution.md) Tables 1-4
<!-- FILE_END: p-from-braid-mirror.md -->

<!-- FILE_START: poincare-lefschetz-borromean.md -->
**Conjecture (D21 Poincaré–Lefschetz closure).**
*The Borromean complement $\mathbf{S}^3 \setminus \mathcal{B}_3$
is a 3-manifold with cusps (boundary = 3 disjoint tori).
Poincaré–Lefschetz duality gives a canonical isomorphism:*

$$
  H^k(\mathbf{S}^3 \setminus \mathcal{B}_3, \partial) \;\cong\;
  H_{3-k}(\mathbf{S}^3 \setminus \mathcal{B}_3),
$$

*relating cohomology with boundary support to homology.  In
particular $H^2(\partial \mathcal{B}_3) \cong H_1(\mathbf{S}^3
\setminus \mathcal{B}_3) \cong \mathbb{Z}^3$ (the three meridian
classes around the three Borromean components).  The duality
pairs the volume form (top cohomology) with the fundamental
class (top homology), giving the natural categorical home for
$\mathrm{Vol}(\mathcal{B}_3) = 8G$ as a Poincaré–Lefschetz
pairing.*

## Relationship to D16 Bloch group

The K-theoretic Bloch-group element
([`conj:borromean-bloch-group-element`](#conj:borromean-bloch-group-element), D16)
provides the **regulator** side of the Borromean structure
($r_2[\mathcal{B}_3] = 8G$).  D21 Poincaré–Lefschetz provides the
**topological** side: the volume form $\in$ $H^3$ pairs with the
fundamental class $\in$ $H_3$ to give the volume integral $8G$.

The two ARE the same number ($8G = \mathrm{Vol}(\mathcal{B}_3)$),
but expressed through distinct dualities. D21 IS the
topological-cohomological route; D16 IS the K-theoretic route.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration**: N/A — manifold-with-boundary duality is at the
  topological level, not at the Hecke-element level.
- **Jet order**: $h^0$ — Poincaré–Lefschetz acts on the leading-
  order topological volume.
- **Bar-symmetry**: bar-symmetric (the duality is independent of
  q-parameter; both sides are classical-topology constructions).

## Open R&D

1. Verify that the Borromean volume $8G$ arises as a Poincaré–
   Lefschetz pairing in Lean — partial Mathlib infrastructure
   exists (Mathlib's `Topology.Manifold` library).
2. Connect to D16 Bloch group: show the regulator $r_2$ and the
   Poincaré–Lefschetz pairing both produce $8G$ via the
   `vol-as-motivic-period` framing.
3. D21 to closed requires Lean class for manifold-with-cusps Poincaré–
   Lefschetz (partial in Mathlib).

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D21
  + paired with D16
- D16 [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md)
  — K-theoretic regulator route to the same $8G$
- [`prop:reeb-bundle-complement-equals-volume`](#prop:reeb-bundle-complement-equals-volume)
  — Reeb-pairing volume route (third route to $8G$)
- [`rem:vol-as-motivic-period`](#rem:vol-as-motivic-period)
  — motivic framing tying all three routes together
- [Lefschetz 1926; Neumann–Zagier 1985 for cusped 3-manifolds]
<!-- FILE_END: poincare-lefschetz-borromean.md -->

<!-- FILE_START: volume-perturbation-formula.md -->
**Proposition.**
*The vertex volume perturbation when going from $H_k$ to $H_{k+1}$
is:*
$$\delta\Phi_k = z^2 \cdot \mathrm{Vol}(4_1) \cdot [k{-}3]_q$$
*where $z = 1/(\sqrt{q}+1/\sqrt{q})$ is the Markov parameter
and $\mathrm{Vol}(4_1) = 2.030$ is the figure-eight knot volume.*

*Both fundamental hyperbolic volumes appear:*
- *$\mathrm{Vol}(\mathcal{B}_3) = 8G$ sets the binding scale $\alpha$*
- *$\mathrm{Vol}(4_1)$ sets the perturbation unit per level*

*Verified for heavy nuclei (Ca, Fe) at $k = 5, 6, 7$:*
- *$k=5$: predicted $1.02$, observed $1.15$ (13%)*
- *$k=6$: predicted $1.54$, observed $1.48$ (4%)*
- *$k=7$: predicted $2.08$, observed $1.90$ (9%)*  $\square$
<!-- FILE_END: volume-perturbation-formula.md -->

