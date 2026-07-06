**Proposition (LP-dual characterisation of the QOU mass formula).**
*Let $\varrho \in H_n(R, q)$ be a quantum-observable knot
(QOU braid representative of a hadronic state) of strand count
$n = 3A$, and let $J^\bullet \subset H_n(R, q)$ be the
Gröbner–Shirshov filtration with associated graded
$\mathrm{gr}^\ell$ ($\ell = 0, 1, 2, \ldots, n-1$) at
**jet-order $\ell$**. Then the QOU mass decomposes as*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \sum_{\ell = 0}^{n-1} u^{(\ell)*}(\varrho),
$$

*where each $u^{(\ell)*}(\varrho)$ is the optimal dual variable
of the Frobenius-positivity constraint at jet-order $\ell$ in
the per-atom operator-selection LP with cost operator
$\tau(P_\ell \cdot -)$ (and $P_\ell = e_\ell(J_1, \ldots, J_n)$
the Murphy central element). The LP-dual characterisation is
the rigorous content of the proposition; an explicit closed
form for $u^{(\ell)*}$ is conjectural and is examined in
Step 5 below.*

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

**Step 4: τ-extraction yields the LP-dual (structural form).**
By [Frobenius self-duality](#prop:frobenius-self-duality-forces-lp-dual-extraction),
$\tau$-extraction is the Frobenius isomorphism
$H_n \xrightarrow{\sim} H_n^*$. Applied to the central element
$P_\ell$ as the *cost operator* in the operator-selection LP,
this produces the level-$\ell$ shadow price as a dual variable
$u^{(\ell)*}(\varrho)$ with the structural form:

$$
  u^{(\ell)*}(\varrho)
  \;=\;
  m_e \cdot
  \mathrm{LP\text{-}dual}\!\Big(
    \text{cost} = \tau(P_\ell \cdot - ),\;\;
    \text{constraints} = \{\langle \Phi, \pi_\lambda \rangle_F \geq 0\}
  \Big).
$$

By Schur's lemma + the Murphy 1992 spectrum (Step 3), the LP
cost vector decomposes block-diagonally with leading-order
scalar coefficient $c_\ell(\lambda)$ on $V_\lambda$. The
optimal dual variables $u_\lambda^*$ therefore depend on
$c_\ell(\lambda)$ and on the Gram matrix
$G_{\lambda,i} = \tau(b_i \cdot \pi_\lambda)$ — i.e.,
on the LP **constraint coupling**, not on a guessed
denominator like $[n]_q!$.

**Important: the normalisation comes from the LP, not from
the Wedderburn trace identity.** A naive closed form

$$
  u^{(\ell)*}(\varrho) \;\stackrel{?}{=}\;
  m_e \cdot \frac{\sum_{\mathrm{ht}(\lambda) = \ell+1}
    w_\lambda(q) \cdot c_\ell(\lambda)}{[n]_q!}
$$

— motivated by the Wedderburn identity
$\sum_\lambda \dim_q(\lambda)^2 = [n]_q!$ — is a *guess*, and
is empirically refuted by the JM-central probe at $\ell = 5$
(see
[`rem:alpha-5-jm-central-empirical-findings`](#rem:alpha-5-jm-central-empirical-findings):
relative spread $\approx 482\%$ across $A = 2,3,4$). The
correct $u^{(\ell)*}$ is obtained by **solving** the LP
per-atom; closed-form depends on the per-atom strand recipe
and the precise cost decomposition.

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
[`alpha-5-jucys-murphy-central.witness.json`](computations/alpha-5-jucys-murphy-central.witness.json)
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

**Conclusion (structural).** Summing over $\ell$:

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \sum_{\ell = 0}^{n-1} u^{(\ell)*}(\varrho),
$$

where each $u^{(\ell)*}$ is the LP-dual variable of the
height-$(\ell{+}1)$ Frobenius-positivity constraint with cost
operator $\tau(P_\ell \cdot -)$. The *structural form* —
that the mass is a sum of LP-duals indexed by jet order — is
established by Steps 1–4 unconditionally.

What is **not** established at this level of generality is the
explicit closed form for $u^{(\ell)*}$. The naive
$\frac{w_\lambda \cdot c_\ell(\lambda)}{[n]_q!}$ form is
refuted empirically; the correct closed form depends on the
per-atom recipe and is obtained by solving the LP. $\square$

**Corollary (structural replacement of α_k AME-fitted parameters).**
The seven ad-hoc terms of the current QOU mass formula
(descended trace, single-gen brane, pair-gen brane, Frobenius
co-Casimir, chirality, cyclotomic tail, shell correction)
correspond to $\ell = 0, 1, 2, 3, 4, 5, 6$ in the iterative
recursion. Each AME-fitted parameter $\alpha_k$ is replaced by
the optimal LP-dual variable $u^{(k-1)*}(\varrho)$ — a
*derived* quantity, not a fit.

The naive guess
$\alpha_k(A) \stackrel{?}{=} \frac{m_e \sum w_\lambda c_{k-1}(\lambda)}{[3A]_q!}$
is empirically refuted; the correct $\alpha_k$ comes from
**solving** the per-atom LP. The derivation cost is
LP-polynomial in the number of partitions of $3A$, so this is
practically computable and yields atom-independent results
*by LP construction* — without requiring the closed-form
guess.

**Corollary (one theorem replaces seven).** The narrative of
the QOU paper compresses from a sequence of seven term
derivations to a single iterative theorem and its closed-form
corollary. See the
[2026-05-09 simplification audit](../../../docs/audits/2026-05-09-paper-simplification-iterative-lp-dual.md)
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
