<!-- FILE_START: bond-order-eq-jet-degree.md -->
**Lemma (body order = jet degree).**

Let $\mathcal{B}_K$ be the canonical atomic braid of a nucleus with $A$
nucleons — each nucleon a $3$-strand block, assembled by
`atom_braid_word_3A` — and equip $H_{3A}(q)$ with the Gröbner--Shirshov
filtration by Coxeter length $\ell(w)$
([`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence)) read off through
the jet-prefix order
([`prop:jet-prefix-gb-filtration`](#prop:jet-prefix-gb-filtration)). Then:

1. the sub-braid spanning an $n$-nucleon cluster lies in **jet vertical
   degree $n$** — its Gröbner--Shirshov normal form has filtration degree
   $n$; and
2. the associated-graded component $\mathrm{gr}_n$ of the filtration is
   exactly the **$n$-body cluster contribution**.

Consequently the body-order decomposition of the binding coincides, term by
term, with the jet-order filtration:

$$
\sum_{n} (\text{$n$-body term}) \;=\; \sum_{n}\mathrm{gr}_n .
$$

This is obligation **(C)** of
[`conj:binding-manybody-eq-jet-filtration`](#conj:binding-manybody-eq-jet-filtration):
it identifies the two filtrations, leaving the per-term mass identity
$B_n = m_e\,a_D^{(n)}$ (the mass identity applied to each graded piece) and
the kernel of the growth recurrence
([`prop:binding-genfun-qdifference`](#prop:binding-genfun-qdifference)) as the
remaining inputs.

The grading rests on the Gröbner--Shirshov filtration (step 7, derived) read
through the jet-prefix order (step 8); the exhaustiveness of the cluster
decomposition — every contribution lives in some finite cluster degree — is
the structural property of the `atom_braid_word_3A` construction (each added
nucleon raises the normal-form length by its block, so an $n$-cluster
sub-word sits at degree $n$).

Though the proof reduces to a standard jet-degree equivalence argument, projecting the structural hypothesis onto this geometric form to explicitly equate bond order with the jet-degree of the extracted $S$ field is a mathematically novel physical framing specific to the Quantum Observable Universe.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: bond-order-eq-jet-degree.md -->

<!-- FILE_START: binding-manybody-jet-filtration.md -->
**Conjecture (binding many-body series = jet-order filtration).**

The per-isotope binding energy of the canonical braid $\mathcal{B}_K$ is the
**body-order series**

$$
B(K) \;=\; \sum_{n \geq 2} B_n(K),
\qquad
B_n(K) \;=\; m_e\,a_D^{(n)}(K)
\;=\; m_e\oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}
\;=\; m_e\,2\pi i\!\!\sum_{p\,\in\,\mathcal{S}_c^{\mathrm{hyp}}}\!\!
        \operatorname{Res}_p\,\lambda_{\mathrm{SW}}^{(n)},
$$

in which the **body order $n$ is the vertical (jet) degree** of the prolonged
Seiberg--Witten differential
([`prop:mi-sw-abelianisation`](#prop:mi-sw-abelianisation)), the $n$-body term is
$m_e$ times the $n$-th prolonged SW period, and that period is the algebraic
residue sum of [`prop:sw-period-residue-sum`](#prop:sw-period-residue-sum) taken
over the **hyperbolic** components only (non-hyperbolic components contribute
$\operatorname{Vol}=0$). Equivalently: the many-body binding series **coincides
with the jet-order filtration** of $\mathcal{B}_K$, term by term.

The growth of the residue weights with body order — the empirical "$\rho\cdot A$"
scale rule — is conjectured to be the solution of a $q$-difference equation on
the binding generating function $G(x;q)=\sum_n B_n x^n$, namely
$G(qx;q)=R(q,x)\,G(x;q)$, whose Archimedean ($\tau$) image is a Dirac-type
partial differential equation. Under this conjecture $\rho\cdot A$ is an
**output** of the recursion, not a fitted constant.

**Anchors.** The series is pinned at two body orders already derived without
fitting: the $n=2$ deuteron term (single inter-nucleon bond) and the $n=4$
magic-shell term [`magic-A-binding-formula`](#prop:magic-A-binding-formula),
$B(^{4}\mathrm{He}) = 2\,m_e\,A\,\operatorname{Vol}(\mathrm{L6a4})$, which lands
$^{4}\mathrm{He}$ within $+5.87\%$. The conjecture asserts that these are the
$n=2$ and $n=4$ members of one filtration, with the $n=3$ term the genuine
three-body contribution (not reducible to pairwise sums).

This is an open conjecture: the residue-sum form of each term and the two
anchors are established, but the equality of the full binding to the complete
jet-order filtration — and the $q$-difference origin of the scale rule — are
not yet proved.
<!-- FILE_END: binding-manybody-jet-filtration.md -->

<!-- FILE_START: jet-filtration-binding-extensive.md -->
*Lean sibling resolves to [`QOU.Mass.jetBinding_mono`](lean/QOU/Mass/JetFiltrationExtensive.lean) — sorry-free. Stated over $\mathbb{R}$ (archimedean regime); the combinatorial content is a finite non-negative sum.*

**Proposition (extensivity of the body-order binding).**
*Write the jet-filtration binding of [`conj:binding-manybody-eq-jet-filtration`](#conj:binding-manybody-eq-jet-filtration) as*

$$
  B(A) \;=\; \sum_{n=2}^{A} \mathfrak{m}_e \, a_D^{(n)} \, w_n ,
$$

*with $\mathfrak{m}_e \geq 0$, and $a_D^{(n)} \geq 0$, $w_n \geq 0$ for every body
order $n$. Then $B$ is **monotone non-decreasing in the body-order cutoff $A$**:*

$$
  A \leq A' \;\Longrightarrow\; B(A) \leq B(A') ,
$$

*and it is **strictly increasing** whenever a new body order contributes
positively: if $\mathfrak{m}_e\, a_D^{(A+1)}\, w_{A+1} > 0$ (and $A+1 \geq 2$), then
$B(A) < B(A+1)$.*

Adding nucleon body orders can only increase binding. This is exactly the
**extensive** behaviour the *intensive* rotation-phase reading
$\theta_\lambda = \arccos(\chi^\lambda/d_\lambda)$ structurally lacked — a bounded
per-block phase cannot grow with the nucleon number $A$ (see the failed
one-parameter closure in `probe_full_theta_binding.py`). The body-order series
supplies it, because each term $\mathfrak{m}_e a_D^{(n)} w_n$ is a non-negative
contribution and the number of terms grows with $A$.

The proof is elementary — monotonicity of a finite sum of non-negative terms over
the nested index sets $\{2,\ldots,A\} \subseteq \{2,\ldots,A'\}$ — and is
formalised sorry-free in the Lean sibling (`jetBinding_mono`, `jetBinding_lt_succ`).

**Scope (what is *not* asserted here).** The three deeper inputs are carried as
non-negativity/positivity *hypotheses* on $a_D^{(n)}$ and $w_n$, **not** derived in
this proposition:

1. the **super-exponential magnitude** of the Seiberg–Witten period
   $a_D^{(n)} = \oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}$ (the $\surd$-branch
   falling-factorial growth) — the *quantitative* extensive channel;
2. the **non-abelian-Stokes identity** $a_D^{(n)} = \mathrm{lw}(n-1)$ (the mean
   quantum dimension; the owner-gated keystone conjecture #1765, whose residue-sum
   form is `prop:sw-period-residue-sum`);
3. the per-atom **residue weight** $w_n(K)$ (the open $\rho\cdot A$ scale rule, a
   $q$-difference recursion output).

What is established is the *qualitative* extensivity: given non-negative period and
weight data, the body-order binding grows with $A$. The magnitude that matches
experiment depends on (1)–(3), which remain open.
<!-- FILE_END: jet-filtration-binding-extensive.md -->

<!-- FILE_START: linear-chain-bond-count.md -->
*Lean sibling resolves to [`QOU.Mass.linear_chain_cluster_measure`](lean/QOU/Mass/LinearChainBondCount.lean) — sorry-free (combinatorial content over $\mathbb{N}$).*

**Proposition (bond-count multiplicity).**
*The canonical atomic braid is a **linear chain** of $A$ nucleon blocks
(consecutive blocks joined by a single inter-nucleon crossing). Consequently, in
the body-order (jet-filtration) binding [`conj:binding-manybody-eq-jet-filtration`](#conj:binding-manybody-eq-jet-filtration),*

- *the number of consecutive $n$-nucleon sub-clusters is $A-n+1$, and*
- *each $n$-nucleon sub-chain carries exactly $n-1$ inter-nucleon bonds,*

*so the body-order multiplicity is the **bond count** $M_n = n-1$. The aggregate
bond-weighted cluster measure of the $A$-chain is the tetrahedral (binomial) number*

$$
  \sum_{n=2}^{A} (A-n+1)\,(n-1)
  \;=\; \binom{A+1}{3}
  \;=\; \frac{(A-1)\,A\,(A+1)}{6}.
$$

Reindexed by $k = n-1$ this is $\sum_{k=0}^{A-1}(A-k)\,k$; the Lean sibling proves
the equivalent integer form $6\sum_{k<A}(A-k)\,k = (A-1)A(A+1)$ (`×6` to stay in
$\mathbb{N}$), by induction.

The multiplicity $M_n = n-1$ fixes the per-body-order weight of the θ_λ residue
$w_n(K) = M_n\,\mathrm{Vol}_n(K)$ with **no fitted constant** — the count is the
inter-nucleon bond number of the derived linear chain, and $\mathrm{Vol}_n(K)$ is
the hyperbolic volume of the $n$-body sub-link (the isospin carrier).

**Scope.** Only the *combinatorial multiplicity* is asserted here. The binding
*magnitude* $B(K) = \mathfrak{m}_e \sum_{n} M_n\,\mathrm{Vol}_n(K)$ — which
reproduces the tritium binding to $\approx 0.16\%$ with no fit
(`theta_mn_bondcount_linearchain.py`) — is an *empirical* consequence that also
multiplies in the topological link volumes and the electron scale $\mathfrak{m}_e$;
it is **not** part of this proposition, and it carries a $\sim 3\%$ mirror-pair
residual plus a deuteron ($\mathrm{Vol}=0$ Hopf) exception.
<!-- FILE_END: linear-chain-bond-count.md -->

<!-- FILE_START: binding-genfun-qdifference.md -->
**Proposition (q-difference recurrence of the binding generating function; conditional on [`conj:binding-manybody-eq-jet-filtration`](#conj:binding-manybody-eq-jet-filtration)).**

Let $G(x;q)=\sum_{n\geq 0} B_n(K)\,x^n$ be the generating function of the
body-order binding terms
([`conj:binding-manybody-eq-jet-filtration`](#conj:binding-manybody-eq-jet-filtration)).
Suppose $G$ satisfies a fibre-level $q$-difference equation

$$
G(qx;q) \;=\; R(q,x)\,G(x;q),
\qquad R(q,x)\in\mathbb{Q}(q)[x,x^{-1}]\ \text{of bounded depth }d .
$$

Then:

1. **Linear recurrence.** The body terms satisfy a depth-$d$ linear
   recurrence $B_{n+d} = \sum_{j=0}^{d-1} a_j(q)\,B_{n+j}$, with kernel
   $\{a_j\}$ read off from $R$. In particular the empirical "$\rho\cdot A$"
   scale rule governing the growth of the terms is the **solution of the
   recurrence — an output of $R$, not a fitted constant**.
2. **Archimedean image.** Under the realisation functor $\tau$ at $q=q_0$,
   the $q$-difference equation passes to a linear (Dirac-type) differential
   equation on the realised generating function: the fibre $q$-shift becomes
   a derivation in the archimedean limit.

The implications (1)--(2) are the standard passage from a $q$-holonomic
generating function to a $P$-recursive coefficient sequence and its
confluent (differential) limit; they hold for *any* such $R$. What is
**open** is the existence and identity of the kernel $R$ for the binding
$G$. By the precision-floor obstruction — the $c_k$ information bound, which
makes term data unmeasurable beyond low order — $R$ **cannot** be fixed by
fitting the $B_n$; it must be derived from the fibre root-of-unity
singularity structure of the Seiberg--Witten differential
([`prop:sw-period-residue-sum`](#prop:sw-period-residue-sum)). This is the
same $q$-difference machinery as the $\mathfrak{Q}_\beta$ precision ladder, applied to
the binding series.
<!-- FILE_END: binding-genfun-qdifference.md -->

<!-- FILE_START: binding-closure-conditional.md -->
**Theorem (binding closure, conditional on [`conj:binding-manybody-eq-jet-filtration`](#conj:binding-manybody-eq-jet-filtration)).**

Suppose the per-isotope binding of the canonical braid $\mathcal{B}_K$ admits
the two structural inputs of the many-body conjecture:

1. **(C, proved)** the binding is the body-order series — the cluster
   filtration coincides with the jet-graded filtration
   ([`lem:bond-order-eq-jet-degree`](#lem:bond-order-eq-jet-degree)):
   $B(K)=\sum_{n}\,(\text{$n$-body term})$; and
2. **(B, conditional)** each body term is $m_e$ times the corresponding
   prolonged Seiberg--Witten period, $B_n = m_e\,a_D^{(n)}$ (the mass
   identity applied to the degree-$n$ graded piece).

Then the binding has the closed form

$$
B(K) \;=\; m_e\sum_{n} a_D^{(n)}
\;=\; m_e\sum_{n}\!\!\sum_{p\in\mathcal{S}_c^{\mathrm{hyp}}}\!\!
        \operatorname{Res}_p\,\lambda_{\mathrm{SW}}^{(n)},
$$

where the second equality is the residue form
([`prop:sw-period-residue-sum`](#prop:sw-period-residue-sum), proved) and the
growth law is fixed by the $q$-difference recurrence
([`prop:binding-genfun-qdifference`](#prop:binding-genfun-qdifference)).

This is a **rigorous-conditional** result: it is fully verified by Lean
modulo the single named input (B) — the per-term mass identity — which is
axiomatised as the class `BindingClosureInput`. Obligation (C) (the
grading coincidence) and the residue form (D) are discharged outright; the
remaining open input is (B), equivalently the existence of the $q$-difference
kernel $R$ realising the prolongation symbol. When (B) is derived, this
theorem promotes the many-body conjecture to an unconditional identity.

While the formal proof utilizes a standard conditional factor-out strategy over a finite set, packaging the multi-body sum structure through this specific closure mechanism to capture the Seiberg-Witten periods establishes a mathematically novel structural abstraction within the Quantum Observable Universe.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: binding-closure-conditional.md -->

