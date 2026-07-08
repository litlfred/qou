<!-- FILE_START: surreal-construction-grading-intro.md -->
Conway's construction grades the surreals by birthday. This section connects the grading to the brane-tower level filtration.
<!-- FILE_END: surreal-construction-grading-intro.md -->

<!-- FILE_START: birthday-grading.md -->
The birthday grading provides a coarse depth gauge for morphisms in surreal-enriched categories. It stratifies formal parameters into nested levels of infinitesimal and transfinite resolution. Statements with hom-coefficients of birthday $< \omega$ involve only dyadic rationals. Birthday-$\leq \omega$ statements include limit reals and first-order infinitesimals. Birthday $> \omega$ statements use named infinities like $\omega$ or transseries terms like $\log \omega$.

Let $K$ be a real-closed field extending $\mathbb{R}$ (typically $K = \mathbf{No}$, Conway's surreal numbers). Every element $x \in \mathbf{No}$ has a canonical birthday $b(x) \in \mathrm{Ord}$. This is the least ordinal stage at which $x$ is constructed in Conway's recursive $\{L \mid R\}$ presentation. Equivalently, $b(x)$ is the length of the sign-sequence representation for $x$:

$$
  b(0) = 0, \qquad b(n) = n \text{ for } n \in \mathbb{N}, \qquad b(\omega) = \omega, \qquad b(1/2) = 2, \qquad b(\pi) = \omega, \qquad b(\varepsilon) = \omega.
$$

The birthday function refines the archimedean norm. Distinct reals $x, y \in \mathbb{R} \subset \mathbf{No}$ have $b(x), b(y) \leq \omega$. The elements $\varepsilon$, $\omega$, and $\omega^2$ have progressively larger birthdays.

Consider the substrate parameter $q = 1 + \varepsilon$ for an infinitesimal $\varepsilon \in \mathbf{No}$ with $b(\varepsilon) = \omega$. Its sign sequence $(+, -, -, -, \ldots)$ has length $1 + \omega = \omega$. The associated parameters resolve as follows:
- $c_q = 1/(q - 1) = 1/\varepsilon = \omega$ has birthday $\omega$.
- $\hbar_q = (q-1)/q = \varepsilon(1 + \varepsilon)^{-1}$ has birthday $\omega$.
- $d_H(q) = (2q-1)^2/q^3 = (1 + 2\varepsilon)^2(1 + \varepsilon)^{-3}$ has birthday $\omega$.

Expressions rational in $q$ evaluated at $q = 1 + \varepsilon$ remain in the birthday-$\leq \omega$ stratum, embedding into the Laurent-series field $\mathbb{R}(\!(\varepsilon)\!)$. The standard-part map distinguishes between finite and infinitesimal within this stratum. The birthday alone does not, as limit reals like $\pi$ also have birthday $\omega$.

Let $\mathbf{C}$ be a $K$-linear category. A birthday grading on $\mathbf{C}$ is an ordinal-indexed filtration of each hom-space:

$$
  \mathrm{Hom}_{\mathbf{C}}(X, Y)_{\leq \alpha} = \bigl\{ f \in \mathrm{Hom}_{\mathbf{C}}(X, Y) : \text{every coefficient of } f \text{ has birthday} \leq \alpha \bigr\}.
$$

This filtration satisfies three properties:
1. **Exhaustiveness**: $\bigcup_\alpha \mathrm{Hom}_{\mathbf{C}}(X, Y)_{\leq \alpha} = \mathrm{Hom}_{\mathbf{C}}(X, Y)$.
2. **Composition**: If $f \in \mathrm{Hom}(X,Y)_{\leq \alpha}$ and $g \in \mathrm{Hom}(Y,Z)_{\leq \beta}$, then $g \circ f \in \mathrm{Hom}(X,Z)_{\leq \alpha \oplus \beta}$ (where $\oplus$ is the natural sum of ordinals).
3. **Monoidality**: If $\mathbf{C}$ is monoidal, $f \otimes g \in \mathrm{Hom}(X \otimes X', Y \otimes Y')_{\leq \alpha \oplus \beta}$.

The sub-category defined by $b(f) \leq \omega$ forms the archimedean-coefficient sub-category. Its morphisms have coefficients that are real numbers or bounded infinitesimals. For $\mathbf{C} = \mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ with $q \in \mathbb{R} \subset \mathbf{No}$, this recovers $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}_q(2))$. The arithmetic of $\mathbf{No}$ restricted to birthday $\leq \omega$ coincides with $\mathbb{R}$ exactly on the archimedean part.

The relaxed axioms ([infinitesimal Frobenius](#conj:infinitesimal-frobenius)) allow corrections of the form $\mathrm{id} + O(\varepsilon)$. These corrections live at birthday $\leq \omega$ but are distinguished from the classical $\mathrm{id}$ by having a non-zero standard part for the $\varepsilon$-coefficient.
<!-- FILE_END: birthday-grading.md -->

<!-- FILE_START: hoefsmit-is-surreal-construction.md -->
The Hoefsmit seminormal form ([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)) diagonalises the Iwahori--Hecke algebra $H_n(q)$ acting on $V^{\otimes n}$ along a tower of Young--Jucys--Murphy elements indexed by standard tableaux. At each step, a Hecke generator $\sigma_i$ splits a tableau-vector into two eigencomponents:
- the **symmetric** ($q$-eigen) component, corresponding to the tableau where boxes $i$ and $i+1$ lie in the same row;
- the **antisymmetric** ($-q^{-1}$-eigen) component, corresponding to the tableau where they lie in the same column.

This is structurally identical to Conway's recursive surreal construction.

Let $\mathrm{Tab}(\lambda)$ denote the set of standard tableaux of shape $\lambda$, viewed as the vertex set of a tree $\mathcal{T}_n$ whose edges record the Young--Jucys--Murphy ordering. Let $\mathbf{No}_{= n}^{\mathrm{dy}}$ denote the set of dyadic surreals of birthday exactly $n$ (equivalently, sign sequences of length $n$). The number of two-rowed standard tableaux of size $n$ is $\binom{n}{\lfloor n/2 \rfloor}$; the number of dyadic surreals of birthday exactly $n$ is $2^n$. The map below is an injective embedding, not a bijection of forests.

There is a canonical injective embedding

$$
  \Phi : \bigsqcup_{\lambda \vdash n,\, \ell(\lambda) \leq 2} \mathrm{Tab}(\lambda) \hookrightarrow \mathbf{No}_{\leq n}^{\mathrm{dy}}
$$

such that:
1. The empty tableau at $n = 0$ and the singleton tableau at $n = 1$ both map to $0$. For $n \geq 2$, the one-row tableau $(n)$ maps to a non-zero value determined by its sign sequence.
2. Each YJM-edge $t \to t'$ in the tableau forest corresponds to a unique sign-sequence extension $s \to s\!\cdot\! +$ (symmetric channel) or $s \to s\!\cdot\! -$ (antisymmetric channel). The sign sequence of a size-$n$ tableau has length $n - 1$.
3. The birthday $b(\Phi(t))$ is bounded by the length of the sign sequence (i.e., by $n - 1$). Surreals in the image are of birthday $\leq n - 1$. The complement of the image in $\mathbf{No}_{\leq n}^{\mathrm{dy}}$ consists of non-tableau dyadic rationals.

This identification has several immediate consequences. The sign-sequence braid invariant is well-defined and lives in $\mathbf{No}_{\leq c(\beta)}^{\mathrm{dy}}$ for a braid $\beta$ of crossing number $c(\beta)$. Birthday refines crossing number: $b(\mathrm{surr}(\beta, t)) \leq c(\beta)$, with equality for reduced braids. The Hoefsmit factorisation equals the Conway construction: the closed formula for $\rho_\lambda(\sigma_i)$ as a $2 \times 2$ matrix in YJM coordinates is exactly the recursive surreal recipe $x = \{x^- \mid x^+\}$, with the eigenvalue ratio $q : -q^{-1}$ determining the position of $x$. The Jones polynomial $J_K(q)$ can be re-expressed as a weighted sum over surreal sign sequences ([Jones polynomial birthday refinement](#conj:jones-birthday)). Finally, knot complexity acquires an honest ordinal-valued refinement: knots of unbounded crossing number live at birthdays approaching $\omega$.

This is the central observation of the appendix. We already use the Hoefsmit seminormal form as the algebraic-combinatorial backbone of the paper. We show that this same backbone is a literal instance of Conway's surreal-number construction. The surreal lift of QOU is not a new structure; it is a different language for what Hoefsmit already provides.
<!-- FILE_END: hoefsmit-is-surreal-construction.md -->

<!-- FILE_START: sign-sequence-of-braid.md -->
A surreal number $x \in \mathbf{No}$ admits a canonical sign-sequence presentation: a function $s_x : \alpha \to \{+, -\}$ for some ordinal $\alpha = b(x)$. The sequence encodes Conway's $\{L \mid R\}$ construction step-by-step: at stage $\beta < \alpha$, $s_x(\beta) = +$ means "$x$ is the rightmost option", and $s_x(\beta) = -$ means "leftmost option".

Hecke generators have two eigenvalues, $q$ (symmetric channel) and $-q^{-1}$ (antisymmetric channel) ([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)). This binary choice at each level is exactly the sign-sequence data, providing a canonical functor from braid words to surreals.

Let $V$ be the fundamental representation of $\mathrm{SU}_q(2)$ and let $\beta = \sigma_{i_1}^{\epsilon_1} \cdots \sigma_{i_k}^{\epsilon_k}$ be a braid word in $B_n$. The Hecke representation $\rho_n : B_n \to H_n(q)$ sends each $\sigma_i^{\pm 1}$ to $\sigma_i^{\pm 1}$. Choose a standard tableau $t$ of shape $\lambda \vdash n$ with $\ell(\lambda) \leq 2$. The Hoefsmit seminormal vector $v_t \in S_\lambda$ at $t$ is an eigenvector of every Young--Jucys--Murphy element. The braid $\beta$ acts on $v_t$ by successively decomposing $\rho(\sigma_{i_j}^{\epsilon_j})\, v_{t_j}$ into symmetric and antisymmetric components, and recording $s_j = +$ for the symmetric component and $s_j = -$ for the antisymmetric. The resulting sign sequence $s = (s_1, \ldots, s_k)$ defines a finite-birthday surreal $\mathrm{surr}(\beta, t) := \mathrm{Gonshor}(s) \in \mathbf{No}$, where $\mathrm{Gonshor}: \{+, -\}^* \to \mathbf{No}$ is the canonical sign-sequence-to-surreal map.

For each fixed standard tableau $t$, the assignment $\mathrm{surr}(-, t) : B_n \to \mathbf{No}$ is a multiplicative monoid map: $\mathrm{surr}(\beta_1 \beta_2, t)$ is computed by first applying $\beta_2$'s sign sequence at $t$ to obtain $t'$, then concatenating with $\beta_1$'s sign sequence at $t'$. Changing the tableau permutes the sign sequence by a Young--Jucys--Murphy permutation. We quotient by this action to obtain a tableau-independent functor $\widetilde{\mathrm{surr}} : B_n \longrightarrow \mathbf{No} / \sim$.

The sign sequence has length equal to the crossing number $c(\beta)$, so $b(\mathrm{surr}(\beta, t)) \leq c(\beta)$. Equality holds when the braid is reduced. This cleanly refines the crossing-number invariant by an ordinal-valued quantity.

The sign sequence carries strictly more information than the crossing number: it records which eigenchannel is chosen at each crossing. Distinct braids with the same crossing number generally give distinct surreals. Surrealisation is a stronger braid invariant valued in $\mathbf{No} / \sim$. It is the precise sense in which "Hoefsmit seminormal form is the surreal $\{L \mid R\}$ construction". It refines the Jones polynomial ([Jones polynomial birthday refinement](#conj:jones-birthday)) and places knot complexity on a transfinite scale.
<!-- FILE_END: sign-sequence-of-braid.md -->

<!-- FILE_START: jones-birthday.md -->
The Jones polynomial $J_K(q) \in \mathbb{Z}[q^{\pm 1/2}]$ is the Markov trace $\mathrm{tr}_M(\rho_n(\beta))$ of the Hecke representation of any braid word $\beta$ whose closure is the oriented link $K$. The Markov trace is computed by summing contributions from every standard tableau $t$ of every two-rowed shape $\lambda \vdash n$.

By [Hoefsmit-is-surreal-construction](#prop:hoefsmit-is-surreal-construction), each tableau $t$ corresponds to a finite-dyadic surreal $\Phi(t) \in \mathbf{No}$ of birthday $\leq n$. This suggests that the Jones polynomial admits a birthday refinement: a finer invariant that records contributions stratified by the birthday of the underlying surreal sign sequence.

**Conjecture.** There exists a refinement $\widetilde{J}_K \in \mathbb{Z}[q^{\pm 1/2}]^{\mathrm{Ord}}$ satisfying:
1. **Recovery of Jones**: $\sum_\alpha \widetilde{J}_K(\alpha) = J_K(q)$.
2. **Birthday locality**: $\widetilde{J}_K(\alpha)$ depends only on tableau contributions of YJM depth $\leq \alpha$.
3. **Strict refinement**: there exist knots $K_1, K_2$ with $J_{K_1}(q) = J_{K_2}(q)$ but $\widetilde{J}_{K_1} \neq \widetilde{J}_{K_2}$.

If (3) holds, $\widetilde{J}_K$ is a strictly stronger invariant than the Jones polynomial, contradicting the classical view that all braid-word information is collapsed by the Markov trace.

The Jones polynomial loses information due to Markov-trace averaging and tableau-shape averaging. The birthday refinement preserves the trace-type averaging but stratifies by YJM depth, a finer invariant than the shape. Contributions from early symmetric channels are separated from contributions from late symmetric channels. Precedents exist: Khovanov homology categorifies the Jones polynomial and is strictly stronger. The birthday refinement exposes previously hidden tableau-level data.

To prove the conjecture, we must produce two knots with identical Jones polynomials and distinct birthday refinements. To disprove it, we must show that the YJM-depth filtration of any tableau contributes only via its endpoint (the shape $\lambda$). We propose testing the Conway--Kinoshita pair $(11n34, 11n42)$.

The conjecture remains open. The Hoefsmit eigenchannel data is explicit, so the refinement is computable. A direct computational attack involves computing $\widetilde{J}_K$ for $11n34$ and $11n42$. For each YJM-extension path $\pi$ of length 11, compute the Hoefsmit matrix product, convert to a sign sequence, and compute the Gonshor surreal. Aggregate contributions by $b(\mathrm{Gonshor}(\pi))$ to yield $\widetilde{J}_K$. If $\widetilde{J}_{11n34} \neq \widetilde{J}_{11n42}$, the conjecture is established. This requires Hoefsmit matrix entries for $H_{11}(q)$, the `gonshor` map, and a script computing matrix products along YJM paths. Falsification requires proving the Hoefsmit-trajectory sum factors through the YJM endpoint.
<!-- FILE_END: jones-birthday.md -->

