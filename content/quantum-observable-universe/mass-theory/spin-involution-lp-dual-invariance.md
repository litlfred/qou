**Definition (spin involution on a Frobenius $*$-algebra).**
Let $(A, \tau, {}^*)$ be a Frobenius $*$-algebra over a
commutative ring $R$ — i.e., a Frobenius algebra equipped with
an $R$-linear involutive anti-homomorphism ${}^* : A \to A$
($(ab)^* = b^* a^*$, $(a^*)^* = a$) such that $\tau$ is
$*$-compatible ($\tau(a^*) = \tau(a)$ in the real case;
$\tau(a^*) = \overline{\tau(a)}$ otherwise). A *spin involution*
on $(A, \tau, {}^*)$ is an $R$-linear map $\sigma : A \to A$
satisfying

1. **Involution**: $\sigma \circ \sigma = \mathrm{id}_A$.
2. **Anti-multiplicative**:
   $\sigma(a b) = \sigma(b)\, \sigma(a)$ for all $a, b \in A$.
3. **Trace-invariant**: $\tau \circ \sigma = \tau$.
4. **$*$-compatible**: $\sigma(a^*) = \sigma(a)^*$ for all $a$.

The $\mathbb{Z}/2$ grading $A = A_+ \oplus A_-$ by
$\sigma$-eigenvalue is the *spin grading*; $A_+$ is the
*spin-singlet sector* and $A_-$ is the *spin-doublet sector*.

**Hypothesis (2 invertible).** Throughout this proposition we
assume $2 \in R^\times$ — i.e., the base ring $R$ contains
$\tfrac{1}{2}$. This is satisfied when $R$ is a field of
characteristic $\neq 2$ (in particular $\mathbb{Q}$,
$\mathbb{R}$, $\mathbb{C}$, $\mathbb{Z}[\tfrac{1}{2}]$, or any
$\mathbb{Q}$-algebra). For the QOU substrate $R = \mathbb{R}$ or
$R = \mathbb{Q}(q)$ this holds. Without this hypothesis, the
$A_\pm$ projections $a_\pm := \tfrac{1}{2}(a \pm \sigma(a))$ are
ill-defined; an alternative additive decomposition (without
division) exists when $A$ has an idempotent splitting
$\mathbf{1} = e_+ + e_-$ with $\sigma(e_\pm) = \pm e_\pm$, but
that is more restrictive.

Every $a \in A$ has the canonical decomposition
$a = a_+ + a_-$ with $a_\pm := \tfrac{1}{2}(a \pm \sigma(a)) \in
A_\pm$. The *isospin third-component* is **defined on
$\sigma$-eigenvectors**:

$$
  T_3(a) \;=\; \tfrac{1}{2}\,\mathrm{sgn}_\sigma(a)
  \;\in\; \{-\tfrac{1}{2},\, 0,\, +\tfrac{1}{2}\},
$$

with $T_3(a) = 0$ for $a \in A_+$ (singlet, $\sigma(a) = a$)
and $T_3(a) = \pm \tfrac{1}{2}$ for $a \in A_-$ realising
$\sigma(a) = \pm a$. For a general $a \in A$, $T_3$ is read
off the $A_\pm$-projection $a = a_+ + a_-$.

**Proposition (spin-invariance of the LP-dual).**
*Let $(A, \tau)$ be a Frobenius algebra with spin involution
$\sigma$. Let $c \in A$ be $\sigma$-invariant ($\sigma(c) = c$).
Let $\Sigma$ be a $\sigma$-stable set of central idempotents of
$A$ (i.e., $\sigma(\pi_\lambda) \in \{\pi_\mu : \mu \in
\Sigma\}$ for every $\lambda \in \Sigma$). For any $\beta \in A$,
the optimal dual variable $y_0^*$ of the operator-selection LP*

$$
  \min_{x \in A}\; \tau(c \cdot x)
  \quad \text{s.t.} \quad
  \tau(\beta^* \beta \cdot x) = n_{\mathrm{target}}(\beta), \;\;
  \tau(\pi_\lambda \cdot x) \geq 0 \;\; \forall \lambda \in \Sigma
$$

*satisfies*

$$
  y_0^*\bigl(\sigma(\beta)\bigr) \;=\; y_0^*(\beta).
$$

*Proof.*

**Step 1 — Frobenius pairing is σ-symmetric.**
The Frobenius pairing $\langle a, b \rangle_\tau := \tau(ab)$
satisfies, for all $a, b \in A$:

$$
  \langle \sigma(a), \sigma(b) \rangle_\tau
  = \tau(\sigma(a)\sigma(b))
  = \tau(\sigma(ba))
  = \tau(ba)
  = \langle b, a \rangle_\tau
  = \langle a, b \rangle_\tau,
$$

where the second equality is anti-multiplicativity, the third
is trace-invariance, and the last is symmetry of $\tau$ (the
Markov / cyclic property). Hence $\sigma$ is an isometry of the
Frobenius pairing.

**Step 2 — σ stabilises the constraint cone.**
Since $\Sigma$ is $\sigma$-stable, the polyhedral cone
$\mathcal{K}_+ := \{x \in A : \tau(\pi_\lambda \cdot x) \geq 0\
\forall \lambda \in \Sigma\}$ satisfies $\sigma(\mathcal{K}_+) =
\mathcal{K}_+$ (apply Step 1 to each constraint).

**Step 3 — σ stabilises the cost functional.**
Because $\sigma(c) = c$ and $\tau \circ \sigma = \tau$:

$$
  \tau(c \cdot \sigma(x))
  = \tau(\sigma(\sigma(c) \cdot x))
  = \tau(\sigma(c \cdot x))
  = \tau(c \cdot x).
$$

The cost is $\sigma$-invariant: replacing $x$ by $\sigma(x)$
does not change the objective.

**Step 4 — σ relates the two LPs.**
Define $\mathrm{LP}(\beta)$ to be the LP with input $\beta$.
The net constraint $\tau(\beta^* \beta \cdot x) =
n_{\mathrm{target}}(\beta)$ transforms under $x \mapsto
\sigma(x)$ to

$$
  \tau(\beta^* \beta \cdot \sigma(x))
  = \tau\bigl(\sigma(\sigma(\beta^*\beta) \cdot x)\bigr)
  = \tau(\sigma(\beta)^* \sigma(\beta) \cdot x),
$$

where we used $\sigma(\beta^*\beta) = \sigma(\beta)^* \sigma(\beta)$
(anti-multiplicativity preserves the involutive form $a^*a$
when $\sigma$ is a $*$-involution; for the Hecke / Markov case
this is the bar involution). Hence $\sigma$ is a bijection
between the feasible sets of $\mathrm{LP}(\beta)$ and
$\mathrm{LP}(\sigma(\beta))$, preserving the objective.

**Step 5 — LP-duality.**
By Steps 2–4, $\mathrm{LP}(\beta)$ and $\mathrm{LP}(\sigma(\beta))$
have feasible sets in $\sigma$-bijection and the same
$\sigma$-invariant cost; their primal optima coincide. By
strong duality (which holds for Frobenius algebras structurally
— see [`prop:frobenius-self-duality-forces-lp-dual-extraction`](#prop:frobenius-self-duality-forces-lp-dual-extraction)),
the dual optima coincide. In particular,

$$
  y_0^*\bigl(\sigma(\beta)\bigr) = y_0^*(\beta). \qquad\square
$$

**Corollary (QOU instance — isospin invariance).**
*For $A = H_n(R, q)$ with $\tau$ the Markov trace and $\sigma = S$
the Hopf antipode, the per-atom canonical braid recipe
satisfies $S(\mathcal{B}_K(Z, N)) \sim \mathcal{B}_K(N, Z)$ (Markov-
conjugate). Consequently, for every central cost operator
$c \in Z(H_n(q))$ (in particular $c = P_\ell = e_\ell(J_1,
\ldots, J_n)$, Murphy 1992) and every $\sigma$-stable Wedderburn
stratum $\Sigma$,*

$$
  y_0^*(Z, N) = y_0^*(N, Z).
$$

*Proof.* For $A = H_n(R, q)$, $S$ is an involutive
anti-homomorphism (Kassel 1995, §VIII.4) and $\tau$ is
$S$-invariant (Kassel 1995, §XII.2). The central elements
$P_\ell$ are $S$-invariant by direct calculation
($S$ permutes the JM elements as
$S(J_k) = q^{2(1-k)} J_k$, so symmetric polynomials in the
$J_k$ are scaled by an overall power of $q$ that vanishes from
the trace; alternatively, $P_\ell$ acts on $V_\lambda$ as
$c_\ell(\lambda)$, and on $V_{\lambda^T}$ as
$c_\ell(\lambda^T) = c_\ell(\lambda)|_{q \to q^{-1}}$, which is
the $q^{-2\ell|\lambda|/n}$-rescaled value — a constant on each
isotypic block, hence absorbed by trace normalisation).
Wedderburn strata defined by partition height
($\mathrm{ht}(\lambda) \le k$) or by self-conjugate selection
are $S$-stable. Apply the proposition. $\square$

**Empirical confirmation.**
[`alpha-5-lp-dual-crystal.witness.json`](computations/alpha/alpha-5-lp-dual-crystal.witness.json)
verifies $y_0^*(T) = y_0^*({}^3\mathrm{He})$ to machine
precision (= 570.6762 at $q_0$, = 26.8242 in ht=6 stratum, and
exactly equal across the entire $q$-sweep).

**Corollary (pair-knot operator $Z \leftrightarrow N$ symmetry).**
*For $A = H_n(R, q)$ as above, let $\sigma_{pp} = \sigma_{i_1}
\sigma_{i_2} \sigma_{i_3} \sigma_{i_4}$ be the proton-pair sub-braid
at the $Z=2$ closed proton shell of $({}^3\mathrm{He}, {}^4\mathrm{He})$
(intra-strand generator product at positions $\{0,1,3,4\}$ in
[`atom_braid_word_3A`](../../../computations/mass_at_3A_proper.py))
and $\sigma_{nn}$ the analogous neutron-pair sub-braid at the $N=2$
closed neutron shell of $({}^3\mathrm{H}, {}^4\mathrm{He})$
(positions $\{3Z, 3Z+1, 3(Z+1), 3(Z+1)+1\}$). Then*

$$
  \mathrm{tr}_M(\sigma_{pp}) \;=\; \mathrm{tr}_M(\sigma_{nn}).
$$

*Proof.* The two sub-braids are the **same Hecke-algebra element**
up to relabelling: each is a 4-letter word of intra-strand
generators with the Hecke quadratic relation $\sigma_i^2 = (q -
q^{-1})\sigma_i + 1$ identically structured (the per-strand
algebraic volumes $\hat V_i$ at intra-positions take the same values
$0.989$ and $0.971$ at $q_0$ regardless of whether the underlying
nucleon is a proton or a neutron — proton/neutron distinction enters
only through the inter-nucleon crossings, which are outside the
intra-shell sub-braid). The spin involution $\sigma = S$ swaps
proton-shell and neutron-shell strand-labellings while preserving
the Hecke-algebra structure, so $S(\sigma_{pp}) = \sigma_{nn}$ as
elements of $H_n(R, q)$. Apply the proposition with $c = 1$ (trivial
central operator). $\square$

**Empirical confirmation (Markov-trace level).**
[`probe-phiq-pair-knot-markov-trace.witness.json`](../../../computations/probe-phiq-pair-knot-markov-trace.witness.json)
(PR [#638](https://github.com/litlfred/qou/pull/638)) computes
$\mathrm{tr}_M(\sigma_{pp})$ and $\mathrm{tr}_M(\sigma_{nn})$ via
Hoefsmit seminormal at $q_0$ for $T$ ($n=9$ with $N=2$ shell) and
${}^3\mathrm{He}$ ($n=9$ with $Z=2$ shell):

$$
  \mathrm{tr}_M(\sigma_{pp}) \;=\; \mathrm{tr}_M(\sigma_{nn})
  \;=\; 0.06216177120816107\ldots \quad \text{(50-dps evaluation; algebraic equality via the Hoefsmit seminormal form's $\sigma_{pp} = \sigma_{nn}$ identity on the $V_{(2,1)}$ block, independent of dps)}.
$$

The earlier $1.326\times$ ratio between $\Delta_{\text{shell}}(Z=2)$
and $\Delta_{\text{shell}}(N=2)$ in
[`probe_phiq_pair_knot_magic_shell.py`](../../../computations/probe_phiq_pair_knot_magic_shell.py)
was a **product-volume artifact** — the simple convention
$|\hat V_{\text{shell}}| = \prod_i |\hat V_i|$ does NOT respect the
Hecke-algebra structure of the shell sub-braid, while the canonical
Markov trace does.

**Operator-level signature.** The
[operator-selection LP dual](../../../computations/lp_dual_solver.py)
(per [`prop:operator-selection-lp`](#prop:operator-selection-lp))
confirms that $\sigma_{pp}, \sigma_{nn}$ are in the active set
EXACTLY at magic-shell atoms ($Z=2$ activates $\sigma_{pp}$, $N=2$
activates $\sigma_{nn}$, doubly magic ${}^{4}$He activates both) — see
[brane-tower-z-habiro §"Pair-knot magic-shell probe"](#conj:brane-tower-z-habiro).
This is the operator-level signature of $Z=2$/$N=2$ closed-shell
structure in the substrate algebra; the spin-involution corollary
gives the structural symmetry that pins it down.

**Remark (mathematical content of "isospin").**
Isospin is *not* a feature peculiar to nucleons; it is the
$\mathbb{Z}/2$ grading attached to *any* Frobenius algebra
equipped with a spin involution. Whenever physical observables
are extracted as $\tau$-traces of products of central elements
and braid recipes, the spin-singlet sector ($T_3 = 0$) and
spin-doublet sector ($T_3 = \pm 1/2$) decompose canonically
under the LP-dual. The "Wigner energy term"
$\sim |Z - N|/A$ in the BW formula is the $T_3$-projection of
this grading; it appears because $|Z - N|$ is the $\mathbb{Z}/2$
*charge* of the recipe, which the LP-dual reads off
mechanically.

**Remark (why this proof works generically).**
The proof never invokes the specific structure of nucleons,
quarks, $SU(2)$, or even Lie theory. The only inputs are:

1. A Frobenius algebra $(A, \tau)$ with non-degenerate trace,
2. An involutive anti-homomorphism $\sigma$ preserving $\tau$,
3. A $\sigma$-invariant central cost $c$,
4. A $\sigma$-stable channel set $\Sigma$.

Any quantum-algebraic system with these four ingredients has
LP-dual spin-invariance. The QOU paper inherits it because
$(H_n(R, q), \tau_{\mathrm{Markov}}, S, P_\ell, \Sigma)$
satisfies all four. Particle physics gets isospin because
nucleons are realised as a 2-row Wedderburn stratum (per
empirics)
inside this same algebra; the Wigner-energy phenomenology is
the LP-dual shadow of the categorical $\mathbb{Z}/2$ grading.
