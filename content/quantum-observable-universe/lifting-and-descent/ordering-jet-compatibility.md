**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable
universe with braiding-induced ordering $\prec_c$ on the
Hecke basis of $A$
([temporal braiding](#def:quantum-observable-universe), axiom 5).  Let $A_0 = A \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ be the recursive brane tower
([recursive brane tower](#def:recursive-brane-tower)), with
$A_{n+1} = J^1(A_n)$
([jet prolongation](#prop:jet-prolongation)).  Then:*

1. **(Extension.)** *At each level $n$, the jet prolongation
   $\ell_n \colon A_n \hookrightarrow A_{n+1}$ induces an
   admissible ordering $\prec_{n+1}$ on the Hecke basis of
   $A_{n+1}$, extending $\prec_n$: if $a, b \in A_n$ and
   $a \prec_n b$, then $\ell_n(a) \prec_{n+1} \ell_n(b)$.*

2. **(Compatibility with multiplication.)** *The ordering
   $\prec_{n+1}$ satisfies left and right compatibility:
   $a \prec_{n+1} b$ implies $c \cdot a \prec_{n+1} c \cdot b$
   and $a \cdot d \prec_{n+1} b \cdot d$ for all
   $c, d \in A_{n+1}$
   ([admissible system](#unital-groebner-bases:def:admissible-system)).*

3. **(Well-foundedness.)** *Each $\prec_n$ is well-founded:
   there are no infinite descending chains in the Hecke
   basis of $A_n$.*

4. **(Direct limit.)** *The direct limit algebra
   $\mathcal{A}_\infty = \varinjlim \mathrm{End}(A_n)$
   ([direct limit algebra](#def:direct-limit-algebra))
   carries a filtered admissible ordering
   $\prec_\infty = \bigcup_n \prec_n$: an element
   $a \in \mathcal{A}_\infty$ has a well-defined leading
   monomial $\mathrm{LM}(a)$ with respect to $\prec_\infty$,
   and the Gröbner--Shirshov reduction algorithm terminates on every
   element of $\mathcal{A}_\infty$ that belongs to some
   finite level $A_n$.*

**Consequence for time.**  The braiding-induced ordering $\prec_c$ on
$A_0$ propagates through the entire jet tower.  At every
brane level, "forward time" (Gröbner--Shirshov reduction, braiding)
and "backward time" (anti-involution, unbraiding) are
well-defined and compatible with the algebraic structure.
The arrow of time is inherited from the initial ordering
— it does not need to be re-imposed at each level.
