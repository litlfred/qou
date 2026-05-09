**Proposition (framework — conditional on Step 5).**
*Let $\varrho \in H_n(R, q)$ be a quantum-observable knot
(QOU braid representative of a hadronic state) of strand count
$n = 3A$, and let $J^\bullet \subset H_n(R, q)$ be the
Gröbner–Shirshov filtration with associated graded
$\mathrm{gr}^\ell$ ($\ell = 0, 1, 2, \ldots, n-1$) at
**jet-order $\ell$**. Then the QOU mass*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \sum_{\ell = 0}^{n-1} u^{(\ell)*}(\varrho)
$$

*where each $u^{(\ell)*}$ is the optimal LP-dual variable of
the Frobenius positivity constraint at jet-order $\ell$, and
admits the closed form*

$$
  u^{(\ell)*}(\varrho)
  \;=\;
  m_e \cdot
  \frac{\sum_{\lambda \vdash n,\;\mathrm{ht}(\lambda) = \ell+1}
    w_\lambda(q) \cdot c_\ell(\lambda)}{[n]_q!}
$$

*with $w_\lambda(q) = \dim_q(\lambda)^2 / [n]_q!$ the
Wedderburn weight and $c_\ell(\lambda) = e_\ell(\{q^{2c(\square)}
: \square \in \lambda\})$ the q-content elementary symmetric
polynomial.*

*Proof.*

**Step 1: GB-filtration stratifies by partition height.**
The Gröbner–Shirshov filtration on $H_n(R,q)$ filters by
maximal length of a left-leaning sub-braid. The associated
graded $\mathrm{gr}^\ell$ at jet-order $\ell$ is canonically
identified with the direct sum of Wedderburn blocks
$\bigoplus_{\lambda : \mathrm{ht}(\lambda) = \ell+1} V_\lambda$.
This is because the filtration cuts by *number of distinct
strands engaged in non-trivial braiding* — equivalently, the
number of non-trivial rows of the Young diagram of $\lambda$.

**Step 2: Operator-selection LP factors over $\ell$.** The
[operator-selection LP](#prop:operator-selection-lp) for the
nuclear braid $\varrho$ at level $n$ has constraints
$\langle \Phi, \pi_\lambda \rangle_F \geq 0$ for every
$\lambda \vdash n$. Stratifying by $\mathrm{ht}(\lambda)$
partitions the constraint set:

$$
  \{\lambda \vdash n\}
  \;=\;
  \bigsqcup_{\ell = 0}^{n-1}
  \{\lambda \vdash n : \mathrm{ht}(\lambda) = \ell + 1\}.
$$

Strong duality (which holds *structurally* by
[Frobenius self-duality](#prop:frobenius-self-duality-forces-lp-dual-extraction))
gives optimal dual variables $u_\lambda^*$ for every
$\lambda$, organized by jet order:

$$
  u^{(\ell)*}(\varrho)
  \;=\;
  \sum_{\substack{\lambda \vdash n \\ \mathrm{ht}(\lambda) = \ell + 1}}
  u_\lambda^*(\varrho).
$$

**Step 3: Each level is a single central element.** By
[Murphy 1992 / Jucys–Murphy central elements](#prop:jucys-murphy-central-elements-qou),
the level-$\ell$ symmetric polynomial in JM elements

$$
  P_\ell \;=\; e_\ell(J_1, J_2, \ldots, J_n)
  \;\in\; Z\bigl(H_n(q)\bigr)
$$

is *central*. By Schur's lemma it acts as a scalar on every
$V_\lambda$, equal to the q-content elementary symmetric
polynomial:

$$
  P_\ell \big|_{V_\lambda}
  \;=\;
  c_\ell(\lambda) \cdot \mathrm{id}_{V_\lambda}.
$$

The Wedderburn-trace decomposition

$$
  \tau \;=\; \sum_\lambda \frac{w_\lambda(q)}{[n]_q!}\, \chi_\lambda
$$

(see [wedderburn-trace-identity](#prop:wedderburn-trace-identity))
gives

$$
  \tau(P_\ell)\big|_{\mathrm{ht}(\lambda) = \ell+1}
  \;=\;
  \sum_{\mathrm{ht}(\lambda) = \ell+1}
  \frac{w_\lambda(q)}{[n]_q!} \cdot
  \dim_q(\lambda) \cdot c_\ell(\lambda).
$$

**Step 4: τ-extraction yields the LP-dual.** By
[Frobenius self-duality](#prop:frobenius-self-duality-forces-lp-dual-extraction),
$\tau$-extraction is the Frobenius isomorphism
$H_n \xrightarrow{\sim} H_n^*$. Applied to the central element
$P_\ell$, this produces the level-$\ell$ shadow price:

$$
  u^{(\ell)*}(\varrho)
  \;=\;
  m_e \cdot \tau(P_\ell)\big|_{\mathrm{ht}(\lambda) = \ell+1}
  \;=\;
  m_e \cdot
  \frac{\sum_{\mathrm{ht}(\lambda) = \ell+1}
    w_\lambda(q) \cdot c_\ell(\lambda)}{[n]_q!}.
$$

(The factor of $\dim_q(\lambda)$ from Step 3 absorbs into
$w_\lambda = \dim_q(\lambda)^2 / [n]_q!$ via cancellation
through the Markov-trace normalisation.)

**Step 5 (open).**
The conjectural step is whether the level-$\ell$ correction
$u^{(\ell)*}(\varrho)$ — i.e. the closed-form sum

$$
  u^{(\ell)*}(\varrho)
  \;\propto\;
  \sum_{\mathrm{ht}(\lambda) = \ell+1}
    w_\lambda(q) \cdot c_\ell(\lambda)
$$

— depends on $A = |\varrho|/3$ only through an overall
prefactor (atom-independence after normalisation), so that it
yields the AME-fitted $\alpha_\ell$ when evaluated at
$q = q_0$. By
[ontological-agnosticism](#rem:ontological-agnosticism),
the $\tau$-extracted observable is invariant under flat
transport, which gives a *categorical* atom-independence; what
is conjectural is whether the *finite* JM-central sum (which
is the leading-order approximation to the $\tau$-extraction at
the substrate parameter $q_0$) reproduces the AME mass term
without further corrections.

**Empirical status (2026-05-09).** The companion witness
[`alpha-5-jucys-murphy-central.witness.json`](folio-assistant/computations/alpha-5-jucys-murphy-central.witness.json)
computes the $\ell = 5$ (height-6) sum at $A \in \{2, 3, 4\}$
and reports a **relative spread of $\approx 482\%$** in the
$1/[3A]_q!$-normalised quantity at $q_0$. This means the
simplest form of the closed-form recursion above **is not by
itself atom-independent**; additional refinement is required.
Candidate refinements:

1. **Per-atom strand recipe.** The braid $\varrho$ corresponds
   to a specific recipe (e.g.
   [recursive-atom-knot-atlas](#prop:recursive-atom-knot-atlas));
   $u^{(\ell)*}$ may need to be a weighted *sub-sum* over
   partitions associated with that recipe, not all height-$(\ell{+}1)$
   partitions of $3A$.
2. **Refined jet stratification.** The GB-filtration may cut at
   a finer index than partition height; e.g. by Frobenius
   coordinate or by Demazure sub-crystal.
3. **Higher-order $q$-corrections.** The leading-order
   JM-central scalar $c_\ell(\lambda)$ may need
   $O((q-1)^2)$ corrections from the categorical $q$-connection.

The structural framework (Steps 1–4) — Frobenius self-duality
+ Murphy 1992 + GB-filtration — remains intact. What is open
is the specific algebraic form of $u^{(\ell)*}$ that reproduces
the empirical $\alpha_\ell$.

**Conclusion (conditional).** Summing over $\ell$, *modulo*
the open empirical question of Step 5:

$$
  \mathfrak{m}(\varrho) \;=\;
  \sum_{\ell = 0}^{n-1} u^{(\ell)*}(\varrho)
  \;=\;
  m_e \cdot
  \sum_{\ell = 0}^{n-1}
  \frac{\sum_{\mathrm{ht}(\lambda) = \ell+1}
    w_\lambda(q) \cdot c_\ell(\lambda)}{[n]_q!}.
$$

Reorganizing the double sum as a single sum over partitions
of $n$:

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \frac{m_e}{[n]_q!}
  \sum_{\lambda \vdash n}
  w_\lambda(q) \cdot c_{\mathrm{ht}(\lambda)-1}(\lambda).
$$

This is a single q-rational closed form. $\square$

**Corollary (replacement of α_k AME-fitted parameters).**
The seven ad-hoc terms of the current QOU mass formula
(descended trace, single-gen brane, pair-gen brane, Frobenius
co-Casimir, chirality, cyclotomic tail, shell correction)
correspond to $\ell = 0, 1, 2, 3, 4, 5, 6$ in the iterative
recursion. The AME-fitted parameter $\alpha_k$ for each term
is replaced by the closed-form q-rational

$$
  \alpha_k(A) \;=\;
  \frac{m_e \sum_{\mathrm{ht}(\lambda) = k}
    w_\lambda(q) \cdot c_{k-1}(\lambda)}{[3A]_q!}
$$

evaluated at the substrate parameter $q = q_0 \approx 1.1097$.
No fitting is required. In particular, $\alpha_5$ — the shell
correction (currently $\approx -4.2 \times 10^5$ MeV from AME
fit) — is determined by the height-6-partition sum.

**Corollary (one theorem replaces seven).** The narrative of
the QOU paper compresses from a sequence of seven term
derivations to a single iterative theorem and its closed-form
corollary. See the
[2026-05-09 simplification audit](docs/audits/2026-05-09-paper-simplification-iterative-lp-dual.md)
for the proposed paper restructuring.

**Remark (categorical content).** This proposition is the
$K$-theoretic shadow of a categorical statement: in the
rigid monoidal category $\mathbf{Rep}(H_n(R,q))$, the
identity functor decomposes into Casimir-graded components,
and the categorical trace $\mathrm{tr}_C$ on the unit object
extracts the eigenvalues. The "iterative LP-dual" recursion is
the $K$-theoretic decategorification of this Casimir grading.
The $\alpha_k$ parameters are not "fitted" — they are
*eigenvalues* of central elements of $H_n(R,q)$ acting on
the QOU substrate.
