*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The torus knot $T_{2,11}$ has Seifert genus $g = 5 > 4$ and
is the **first excluded generator** — the knot that would
produce a fourth lepton generation if embeddable.  The
algebraic mechanism is the Chebyshev overflow in the
genus-filtration ideal $\mathfrak{I}_4 = (u^5)$
([genus-filtration ideal](#prop\:genus-filtration-ideal)):
the Hecke coefficient $a_{11}(u) = u^5 + 9u^4 + \cdots$
has degree $5 > 4$, so $a_{11} \in (u^5)$.

This remark traces the **consequences** of that algebraic
annihilation through the jet bundle, shell structure, and
symmetry group.

***

## 1. Algebraic survival, physical death

The torus knot $T_{2,11}$ satisfies every structural relation — it is a
valid element of the Iwahori--Hecke algebra:

| Relation          | Status   | Detail                                               |
| ----------------- | -------- | ---------------------------------------------------- |
| Hecke (J-1)       | Survives | $T_1^{11} = a_{11}(u) T_1 + a_{10}(u) \in H_2(R, q)$ |
| Frobenius (J-2)   | Survives | $\mathrm{tr}_M(T_1^{11} \cdot T_\beta) \neq 0$       |
| Jones polynomial  | Survives | $J_{T_{2,11}}(q) \neq 0$                             |
| Translation (J-4) | Survives | Lifts to all brane levels                            |

But the cohomological constraints kill it:

| Constraint          | Status     | Detail                                   |
| ------------------- | ---------- | ---------------------------------------- |
| Chebyshev overflow  | **Killed** | $\deg_u a_{11} = 5 > 4 = g(\Sigma_4)$    |
| Mass functional     | **Killed** | $\mathcal{M}(T_{(2,11)}) = 0$            |
| Harmonic projection | **Killed** | $\Pi_{\mathrm{harm}} T_{(2,11)} = 0$     |
| Hodge dual          | **Killed** | $\star[T_{2,11}] = 0$ in $H^*(\Sigma_4)$ |

The separation is clean: the Iwahori--Hecke algebra sees no genus
bound; the Chebyshev degree
([genus-filtration ideal](#prop\:genus-filtration-ideal)) is
the polynomial certificate for membership in the spectral
filter.

***

## 2. Behaviour on the jet bundle

At each brane level $n$, the level-$n$ spectral ideal
$\mathcal{I}_4^{(n)} = \{w \in H^{(n)}(q) : g(\hat{w}) > 4\}$
is preserved by jet embedding and :refterm[descent]{#descent}:

$$
  \ell_n(\mathcal{I}_4^{(n)}) \subseteq \mathcal{I}_4^{(n+1)},
  \qquad
  \mathfrak{d}_{n+1}(\mathcal{I}_4^{(n+1)}) \subseteq \mathcal{I}_4^{(n)}.
$$

The torus knot $T_{2,11}$ is **entirely descended** at every level:

$$
  \hat{\tau}_n(T_{(2,11)}^{(n+1)}) = T_{(2,11)}^{(n+1)},
  \qquad
  (1 - \hat{\tau}_n)(T_{(2,11)}^{(n+1)}) = 0.
$$

It has no transient component, contributes nothing to the
Yekutieli obstruction $\kappa_n$, and creates no new physics
at any level.

***

## 3. No :refterm[descent]{#descent} to shells

The shell structure is governed by the transfer matrix
eigenvalues $\lambda_\pm$ of $T_{\gamma e}(q)$
([shell structure eigenvalues](#prop\:shell-structure-eigenvalues)).
The torus knot $T_{2,11}$ has:

$$
  \mathcal{T}_{T_{2,11}}(q) = \mathbf{I}_{2 \times 2},
  \qquad
  F(T_{2,11}, N) = 1  \forall N.
$$

* **No shell structure**: eigenvalues $(1, 1)$ give the
  degenerate Chebyshev recurrence $\hat{V}(n) = 1$ for all $n$
  — flat, no energy separation, no sub-shells.
* **No shell-transition levels**: zero effective crossings on $\Sigma_4$,
  so it cannot push a spin-orbit level across a gap
  ([shell-transition knot](#prop\:shell-transition-knot)).
* **Null force operator**: the $(2,11)$ channel contributes the
  identity factor to the spectral decomposition — a
  multiplicative ghost.

***

## 4. No $S_{11}$ symmetry — crystallographic obstruction

The symmetry group of $T_{2,11}$ is **not** $S_{11}$ but the
dihedral group:

$$
  \mathrm{Sym}(T_{2,11})
  = \mathbb{Z}_{11} \rtimes \mathbb{Z}_2
  = D_{11}
  \qquad (\text{order } 22).
$$

* $\mathbb{Z}_{11}$: rotational symmetry (winding number $11$,
  not strand count — $T_{2,11}$ is a 2-strand braid
  $\sigma_1^{11} \in B_2$).
* $\mathbb{Z}_2$: strand swap $S_2$ from $B_2 / \langle \sigma_1^2 = 1\rangle$.

**$\mathbb{Z}_{11}$ cannot embed in $S_5$.**  The maximum
element order in $S_5$ is $6$ (cycle type $(2,3)$), and
$11 > 5$ means no element of order $11$ exists:

$$
  \mathbb{Z}_{11} \not\hookrightarrow S_5
  = \mathrm{Aut}(\Sigma_4).
$$

This is a **crystallographic obstruction at the group level**:
$11$-fold rotational symmetry is incompatible with the
$5$-sheet Bring surface, just as $5$-fold symmetry is
incompatible with a lattice
([fivefold symmetry](#rem\:fivefold-symmetry)).

| Knot       |    Cyclic sym.    | Embeds in $S_5$? | Genus $\leq 4$? |        Status       |
| ---------- | :---------------: | :--------------: | :-------------: | :-----------------: |
| $T_{2,3}$  |   $\mathbb{Z}_3$  |        Yes       |   Yes ($g=1$)   |        Embeds       |
| $T_{2,5}$  |   $\mathbb{Z}_5$  |        Yes       |   Yes ($g=2$)   |        Embeds       |
| $T_{2,7}$  |   $\mathbb{Z}_7$  |        No        |   Yes ($g=3$)   | Embeds (sym broken) |
| $T_{2,9}$  |   $\mathbb{Z}_9$  |        No        |   Yes ($g=4$)   | Embeds (sym broken) |
| $T_{2,11}$ | $\mathbb{Z}_{11}$ |      **No**      |  **No** ($g=5$) | **Doubly excluded** |

For $T_{2,7}$ and $T_{2,9}$: the cyclic symmetry exceeds
$S_5$ but the genus fits — their symmetries are *broken* on
$\Sigma_4$.  For $T_{2,11}$: **both** criteria fail.  It is
the ghost of the fourth generation — algebraically valid,
topologically null, with no shell action and no compatible
symmetry.

**Representation-theoretic refinement.**  The distinguished role
of $T_{2,3}$ and $T_{2,5}$ at the top of the embedding table
acquires a representation-theoretic origin under the weight
identification of
[prop:x5-bring-weight-identification](#prop\:x5-bring-weight-identification).
Passing to the hyperelliptic quintic $\mathcal{X}_5$ of
[thm:hyperelliptic-z5-classification](#thm\:hyperelliptic-z5-classification),
the non-trivial $\mathbb{Z}_5$-isotypical part of
$H^1(\mathcal{X}_5, \mathbb{Q})$ is exactly the 4-dim character
sum $\chi_1 \oplus \chi_2 \oplus \chi_3 \oplus \chi_4$, and the
Seifert surface of $T_{2,5}$ fills this representation
completely ($g(T_{2,5}) = 2 = \dim_{\mathbb{C}} J(\mathcal{X}_5)$),
while $T_{2,3}$ occupies a 2-dim sub-isotype.  See
[rem:weight-identification-consequences](#rem\:weight-identification-consequences)
for details.

***

## 5. Skein interaction: modified crossing relation

When $T_{2,11}$ appears as an $L_0$ intermediate in a Skein
resolution of physical knots, the spectral filter projects it
away.  The physical Skein relation on $\Sigma_4$ becomes:

$$
  q\mathcal{M}[L_+] = q^{-1}\mathcal{M}[L_-]
  \qquad\text{when } g(L_0) > 4,
$$

fusing the two crossing channels.  The $\mathbb{Z}_{11}$
symmetry of the intermediate term is confined to
$\mathcal{I}_4$ and never reaches the physical quotient.
