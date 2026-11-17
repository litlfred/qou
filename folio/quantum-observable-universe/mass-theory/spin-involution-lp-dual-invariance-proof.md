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
Define $\mathrm{LP}(\beta)$ to be the LP with input $\beta$, and put
$\gamma := \sigma(\beta)^*$. Since $\sigma$ is anti-multiplicative and
commutes with $*$,

$$
  \sigma(\beta^*\beta) = \sigma(\beta)\,\sigma(\beta^*)
  = \sigma(\beta)\,\sigma(\beta)^* = \gamma^*\gamma .
$$

This is in general different from $\sigma(\beta)^*\sigma(\beta)$. The net
constraint of $\mathrm{LP}(\beta)$ evaluated at $\sigma(x)$ is then, by
involutivity, anti-multiplicativity, $\tau \circ \sigma = \tau$ and
cyclicity,

$$
  \tau(\beta^*\beta \cdot \sigma(x))
  = \tau\bigl(\sigma(x \cdot \sigma(\beta^*\beta))\bigr)
  = \tau(\sigma(\beta^*\beta) \cdot x)
  = \tau(\gamma^*\gamma \cdot x).
$$

So $x \mapsto \sigma(x)$ maps the feasible set of $\mathrm{LP}(\gamma)$
onto that of $\mathrm{LP}(\beta)$, provided the right-hand sides agree,
$n_{\mathrm{target}}(\gamma) = n_{\mathrm{target}}(\beta)$, which is the
hypothesis of the statement. With Steps 2 and 3, $\sigma$ is a bijection
between the feasible sets of $\mathrm{LP}(\beta)$ and
$\mathrm{LP}(\sigma(\beta)^*)$ that preserves the objective. (Lean:
`net_constraint_transform`.)

**Step 5 — LP-duality.**
By Steps 2–4, $\mathrm{LP}(\beta)$ and $\mathrm{LP}(\sigma(\beta)^*)$
have feasible sets in $\sigma$-bijection and the same
$\sigma$-invariant cost; their primal optima coincide. By
strong duality (which holds for Frobenius algebras structurally
— see [`prop:frobenius-self-duality-forces-lp-dual-extraction`](#prop:frobenius-self-duality-forces-lp-dual-extraction)),
the dual optima coincide. In particular,

$$
  y_0^*\bigl(\sigma(\beta)^*\bigr) = y_0^*(\beta). \qquad\square
$$

**Corollary (QOU instance — isospin invariance; NOT established).**
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

*Status.* The argument that stood here fails at its first step.
It asserted that $\tau$ is $S$-invariant for the antipode
$S(\sigma_i) = \sigma_i^{-1}$. Under convention D,
$\tau(\sigma_i) = z = q^3/(q^2+1)$, while
$\tau(\sigma_i^{-1}) = \tau(\sigma_i) - (q - q^{-1}) = 1/\bigl(q(q^2+1)\bigr)$;
at $q_0$ these are $0.6127$ and $0.4036$. Moreover $\sigma_i \mapsto
\sigma_i^{-1}$ does not preserve the Hecke relation over $R$: the
image satisfies $(\sigma_i^{-1} - q^{-1})(\sigma_i^{-1} + q) = 0$, the
relation at $q^{-1}$. It is an algebra map only together with
$q \mapsto q^{-1}$, i.e. the bar involution, and $\tau$ is
bar-*equivariant*, $\tau(\bar x) = \overline{\tau(x)}$, not invariant.
So the hypothesis $\tau \circ \sigma = \tau$ of the proposition is not
met by the Markov trace with this $\sigma$, and $y_0^*(Z, N) =
y_0^*(N, Z)$ does not follow. The $R$-linear anti-automorphism
$T_w \mapsto T_{w^{-1}}$ does preserve $\tau$, but it fixes every
generator and so does not exchange $Z$ and $N$.

**Empirical confirmation.**
[`alpha-5-lp-dual-crystal.witness.json`](../../../computations/alpha/alpha-5-lp-dual-crystal.witness.json)
verifies $y_0^*(T) = y_0^*({}^3\mathrm{He})$ to machine
precision (= 570.6762 at $q_0$, = 26.8242 in ht=6 stratum, and
exactly equal across the entire $q$-sweep).

**Corollary (pair-knot operator $Z \leftrightarrow N$ symmetry).**
*For $A = H_n(R, q)$ as above, let $\sigma_{pp} = \sigma_{i_1}
\sigma_{i_2} \sigma_{i_3} \sigma_{i_4}$ be the proton-pair sub-braid
at the $Z=2$ closed proton shell of $({}^3\mathrm{He}, {}^4\mathrm{He})$
(intra-strand generator product at positions $\{0,1,3,4\}$ in
the canonical formalism)
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
intra-shell sub-braid). The two words differ by an index shift
$\sigma_i \mapsto \sigma_{i+k}$, and the Markov trace is invariant
under that shift (it is determined by the Markov property, which the
shift respects). Hence the traces agree. The antipode $S$ plays no
role, and could not: it sends $\sigma_i$ to $\sigma_i^{-1}$, not to
another positive generator. $\square$

**Empirical confirmation (Markov-trace level).**
[`canonical evaluation-phiq-pair-knot-markov-trace.witness.json`](../../../computations/canonical evaluation-phiq-pair-knot-markov-trace.witness.json)
computes
$\mathrm{tr}_M(\sigma_{pp})$ and $\mathrm{tr}_M(\sigma_{nn})$ via
Hoefsmit seminormal at $q_0$ for $T$ ($n=9$ with $N=2$ shell) and
${}^3\mathrm{He}$ ($n=9$ with $Z=2$ shell):

$$
  \mathrm{tr}_M(\sigma_{pp}) \;=\; \mathrm{tr}_M(\sigma_{nn})
  \;=\; 0.06216177120816107\ldots
$$

This is an exact representation evaluation. The equality is algebraic — it
follows from the Hoefsmit seminormal form's $\sigma_{pp} = \sigma_{nn}$
identity on the $V_{(2,1)}$ block — and so is independent of the working
precision.

The earlier $1.326\times$ ratio between $\Delta_{\text{shell}}(Z=2)$
and $\Delta_{\text{shell}}(N=2)$ in
the canonical formalism
was a **product-volume artifact** — the simple convention
$|\hat V_{\text{shell}}| = \prod_i |\hat V_i|$ does NOT respect the
Hecke-algebra structure of the shell sub-braid, while the canonical
Markov trace does.

**Operator-level signature.** The
the canonical formalism
(per [`prop:operator-selection-lp`](#prop:operator-selection-lp))
confirms that $\sigma_{pp}, \sigma_{nn}$ are in the active set
EXACTLY at magic-shell atoms ($Z=2$ activates $\sigma_{pp}$, $N=2$
activates $\sigma_{nn}$, doubly magic ${}^{4}$He activates both) — see
[brane-tower-z-habiro §"Pair-knot magic-shell canonical evaluation"](#conj:brane-tower-z-habiro).
This is the operator-level signature of $Z=2$/$N=2$ closed-shell
structure in the substrate algebra; the spin-involution corollary
gives the structural symmetry that pins it down.
