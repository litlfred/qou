Two inner-product structures arise on the rigid monoidal object
$A$ of a quantum observable universe:

- **Categorical Frobenius pairing** $\mu_A : A \otimes A \to \mathbf{1}$
  induced by the rigid duality $A \cong A^\vee$
  ([Frobenius pairing exists](#prop:frobenius-pairing-exists)):
  $$
    \langle a, b \rangle_\mu
    \;=\;
    \int_A (a \otimes b)
    \;=\;
    \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \mu_A)
      \circ (\mathrm{coev}_A \otimes \mathrm{id}_A)(a \otimes b).
  $$
- **Hecke-algebra Markov-trace form** on the archimedean
  realisation $H_n(q) = \mathrm{End}_{\mathbf{C}}(A^{\otimes n})$
  ([categorical mass as Markov trace](#prop:categorical-mass-markov)):
  $$
    \langle a, b \rangle_{\mathrm{tr}_M}
    \;=\;
    \mathrm{tr}_M(\rho(a) \cdot \rho(b)),
  $$
  where $\rho : B_n \to H_n(q)^\times$ is the braid representation.

The binding-energy derivation uses both interchangeably; their
equivalence is implicit in the fibre-functor descent but has not
been made explicit.

## Statement

**Proposition (Frobenius-pairing equivalence).**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
fibre functor $\tau : \mathbf{C} \to \mathrm{Vec}_{\mathbb{Q}(q)}$
([categorical action](#def:categorical-action)) satisfying the
RJ canonical inner product condition
([RJ canonical inner product](#prop:rj-canonical-inner-product)).*

*For every $n \geq 1$ and every pair of morphisms
$a, b \in \mathrm{End}_{\mathbf{C}}(A^{\otimes n})$, the two
pairings coincide under $\tau$:*

$$
  \tau\bigl(\langle a, b \rangle_\mu\bigr)
  \;=\;
  \langle \tau(a), \tau(b) \rangle_{\mathrm{tr}_M}
  \;=\;
  \mathrm{tr}_M\bigl(\tau(a) \cdot \tau(b)\bigr).
$$

*Hence the categorical and archimedean inner products define the
same non-degenerate pairing on $\mathrm{End}_{\mathbf{C}}(A^{\otimes n})
\cong H_n(q)$.*

## Proof sketch

**(Step 1: Markov trace as descent of categorical trace.)**  By
[Jones–Markov trace](#thm:jones-markov-trace), $\mathrm{tr}_M$ on
$H_n(q)$ is the unique linear functional satisfying
$\mathrm{tr}_M(1) = 1$, cyclicity, and the Markov axiom
$\mathrm{tr}_M(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}_M(x)$.
The categorical trace on $\mathrm{End}_{\mathbf{C}}(A^{\otimes n})$
(defined via $\mathrm{ev} \circ (\mathrm{id} \otimes \mathrm{coev})$
and the Frobenius form $\int_A$) satisfies the same three axioms
under the $\mathbf{C}$-module structure.  By uniqueness, the two
traces descend to the same $\mathbb{Q}(q)$-valued functional under
$\tau$:
$$
  \tau(\mathrm{tr}_A(x)) = \mathrm{tr}_M(\tau(x))
  \quad \forall\, x \in \mathrm{End}_{\mathbf{C}}(A^{\otimes n}).
$$

**(Step 2: Frobenius pairing as bilinear-form trace.)**  By
definition of the Frobenius pairing via rigid duality:
$$
  \langle a, b \rangle_\mu
  \;=\;
  \int_A (a \otimes b)
  \;=\;
  \mathrm{tr}_A(a \cdot b^\vee),
$$
where $b^\vee$ is the rigid dual of $b$ under the self-duality
$A \cong A^\vee$ (composed with the Nakayama automorphism
$\Psi$ of [categorical mass as Markov trace](#prop:categorical-mass-markov)
§Step 2).  Under $\tau$, $b^\vee$ maps to $\tau(b)^\ast$
(complex-conjugate transpose in the unitary realisation), but
since $H_n(q)$ is self-dual Frobenius and the RJ inner product
is non-degenerate, $\tau(b)^\ast = \tau(b)$ up to basis choice.
Hence:
$$
  \tau(\langle a, b \rangle_\mu) = \tau(\mathrm{tr}_A(a \cdot b))
  = \mathrm{tr}_M(\tau(a) \cdot \tau(b))
  = \langle \tau(a), \tau(b) \rangle_{\mathrm{tr}_M}.
$$

**(Step 3: Non-degeneracy.)**  The Markov-trace form
$\langle \cdot, \cdot \rangle_{\mathrm{tr}_M}$ on $H_n(q)$ is
non-degenerate at generic $q$ because the Gram matrix of the NF
basis $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ has nonzero
determinant
([Gram matrix inverse](#prop:gram-matrix-inverse)).  This transfers
to $\mathbf{C}$ via $\tau^{-1}$, confirming non-degeneracy of
$\mu_A$.  $\square$

## Open subgoals

The proof sketch above assumes two nontrivial ingredients that
are stated but not independently proved:

1. **Nakayama = identity** on $\mathrm{End}_{\mathbf{C}}(A^{\otimes n})$.
   The categorical setup has $S^2 = \mathrm{id}$ (Yekutieli 2D
   nonabelian Stokes), so the Nakayama automorphism is trivial
   and $b^\vee \cong b$ up to basis.  A Lean proof requires the
   formal 2D-Stokes statement; currently open.

2. **RJ → Markov trace isomorphism** on each irrep block.  The
   [RJ canonical inner product](#prop:rj-canonical-inner-product)
   gives $\tau(\mathrm{tr}_A) = \mathrm{tr}_M$ per irrep $\lambda$;
   the cyclicity and Markov axioms on the RJ side are inherited
   from the rigid-monoidal trace axioms.  Full Lean proof deferred.

## Implication for the derivation chain

With this proposition the two "Frobenius pairings" used throughout
the session's computational work are equal under $\tau$.  In
particular:

- The demand-supply construction
  ([knot operator selection](#prop:knot-operator-selection) §iii)
  uses $\langle \Phi, \mathrm{dem}(K) \rangle_{\mathrm{tr}_M}$ with
  the Markov-trace form — which is the $\tau$-image of the
  categorical Frobenius pairing.
- The Gram-matrix inversion for dual-basis construction
  (`confinement-lp.py`, `sdp_moment_lift.py`) operates on
  $G_{ij} = \mathrm{tr}_M(b_i b_j)$ — the $\tau$-image of the
  Frobenius form.

No separate "categorical" implementation is required; the Markov-
trace form is the archimedean incarnation of the rigid-monoidal
pairing.

**Witness**: none at the categorical level; $\mathrm{tr}_M$ numerics
consistent with rigid pairing throughout session witness files.
