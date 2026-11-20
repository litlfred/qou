## Proof

Recall the definition from the statement block: for a confined
particle $\mathfrak{H}$,

$$
  \Delta_{\mathrm{cat}}(\mathfrak{H})
  \;=\;
  B_{\mathrm{AME}}(\mathfrak{H})
  \;-\;
  m_e \cdot \rho \cdot \bigl|\tau(\beta_{\mathfrak{H}})\bigr|,
$$

where $B_{\mathrm{AME}}$ is the tabulated experimental binding,
$m_e$ and $\rho$ are fixed calibration constants, and
$\tau \colon \mathrm{End}_{\mathbf{C}}(A^{\otimes n}) \to \mathbb{C}_q$
is the canonical Markov trace. An *operator-volume convention* is a
rule for evaluating the divergent brane tower
$\sum_i \Phi_q(z_i)$ attached to $\mathfrak{H}$; it prescribes
(i) which tower summands enter and with what weights or depths, and
(ii) which operator data feed the tower argument. The only
quantity in the definition of $\Delta_{\mathrm{cat}}$ that could
conceivably depend on such a rule is $\tau(\beta_{\mathfrak{H}})$.
The proof factors into three steps.

**Step 1: uniqueness of the Markov trace.**  For $H_n(q)$ at
generic $q$, the functional satisfying M1 (cyclicity), M2 (the
Markov axiom
$\mathrm{tr}^{(n)}(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}^{(n-1)}(x)$
with the framework parameter $z = q^{3}/(q^{2}+1)$, **convention D**), and M3
($\mathrm{tr}(1) = 1$) is unique
([Markov-trace uniqueness](#prop:markov-trace-frobenius-selection);
Jones \cite{jones1987}, Wenzl \cite{wenzl1988}). Consequently any
two evaluation routes that compute a functional obeying M1–M3 —
seminormal-form evaluation, recursive Markov peeling, or the Wenzl
bridge — return the *same* value $\tau(\beta)$ on any given braid
$\beta$, and in particular the same magnitude $|\tau(\beta)|$.

**Step 2: every probed convention factors through the same
categorical trace.**  Each of the six brane-tower convention
families probed in
[Brane tower lives in the $z$-Habiro ring](#conj:brane-tower-z-habiro)
§"Surviving claims after closure attempts" is, by its defining
prescription, a regularization of the divergent analytic $\Phi_q$
tower. Case by case:

1. *Scalar uniform-$k$* truncates the tower at a fixed depth $k$;
   it acts only on the tower index set.
2. *$\ell n_0 + k$* is a level-selection variant of the same
   truncation; again only the tower index set changes.
3. *Per-eigenvalue operator-valued* replaces the scalar tower
   argument with the eigenvalue-resolved operator argument; the
   trace functional applied to the categorical factor still
   satisfies M1–M3.
4. *Multiplicity / Type-B-fold* reweights tower summands by
   folded-crystal multiplicities; the fold acts on the index set of
   the tower, not on the trace functional.
5. *Pair-knot product-volume* substitutes pair-knot composite
   volumes for per-generator volumes inside the tower argument.
6. *Pair-knot Markov-trace* evaluates the pair-knot composite by a
   trace functional satisfying M1–M3, which by Step 1 coincides
   with the canonical trace on the composite element.

In every case the convention's output factors as a
convention-dependent tower regularizer composed with one and the
same categorical evaluation: none of the six prescriptions modifies
the functional applied to $\beta_{\mathfrak{H}}$, which in each
family obeys M1–M3 and therefore, by Step 1, equals the canonical
Markov trace. The conventions differ only in how the divergent
tower — a quantity that does not appear in the definition of
$\Delta_{\mathrm{cat}}$ — is regularized.

**Step 3: convention-independence of $\Delta_{\mathrm{cat}}$.**
Let $c$ and $c'$ be any two probed conventions. By Steps 1 and 2,
the categorical factor computed under either convention is the
canonical value, so
$|\tau(\beta_{\mathfrak{H}})|_c = |\tau(\beta_{\mathfrak{H}})|_{c'}$.
The remaining ingredients $B_{\mathrm{AME}}(\mathfrak{H})$, $m_e$,
and $\rho$ make no reference to the convention. Substituting into
the defining formula,

$$
  \Delta_{\mathrm{cat}}(\mathfrak{H})\big|_{c}
  \;=\;
  \Delta_{\mathrm{cat}}(\mathfrak{H})\big|_{c'},
$$

so $\Delta_{\mathrm{cat}}(\mathfrak{H})$ depends only on the
categorical-trace invariant $\tau(\beta_{\mathfrak{H}})$ and is
strictly invariant under the choice of operator-volume convention.
$\square$

## Falsifiable predictions

1. **Convention-independence of $\Delta_{\mathrm{cat}}({}^3\mathrm{He})$.**
   Compute $|\tau(\beta_{{}^3\mathrm{He}})|$ via Hoefsmit seminormal
   (per-eigenvalue), via the recursive symbolic Markov peel, and via
   the Wenzl bridge at 50 dps.  All three
   should give the same $|\tau|$ to 50 dps; the resulting
   $\Delta_{\mathrm{cat}}$ should be atom-dependent but
   convention-independent.

2. **Convention-dependent regularizer dominates the brane-tower
   variation.**  The non-categorical brane-tower regularization
   contributions vary by orders of magnitude across the six canonical evaluation
   families — but their *difference from* $|\tau|$ is the same
   non-categorical regularizer.  The structural gap
   $\Delta_{\mathrm{cat}}$ should be the same across all probed
   conventions, on each atom separately.

3. **Magic-shell decomposition.**  $\Delta_{\mathrm{cat}}(Z, N)$
   should decompose as
   $\Delta_{\mathrm{cat}}(Z, N) = \Delta_0(A) + \mathbb{1}_{Z \in \mathrm{magic}} \cdot \Delta_p + \mathbb{1}_{N \in \mathrm{magic}} \cdot \Delta_n$
   with $\Delta_p = \Delta_n$ (the Z$\leftrightarrow$N symmetry constraint).  This
   is the precise content of
   the magic-shell stabilization conjecture.
