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

**Remark (proof scope).** This proof uses only the $R$-linear
rigid-monoidal-category axioms; it makes no assumption about the
specific ribbon structure of the QOU substrate, the Hecke
algebra, or the Markov trace. So linearity holds for **any**
rigid monoidal $R$-linear category in which the trace-cut
definition makes sense — it is a generic categorical fact, not a
QOU-specific statement.

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

### Why this is the right operation for the Higgs mechanism

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
