---
doc_id: arxiv-1508.01627v4
doc_title: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS "
section_id: sec-011-41-non-unipotent-characters
section_title: "Non-unipotent characters"
section_number: 4.1
pages: 9-10
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.975
doc_brief: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS IN CLASSICAL GROUPS"
---
[]{#ssec:nonunipotent label="ssec:nonunipotent"}

We first deal with non-unipotent characters, and afterwards examine in more detail the unipotent characters.

::: thm
[]{#thm:non-unip label="thm:non-unip"} Let $G$ be one of the groups ${\operatorname{Spin}}_{2n+1}(q)$ for odd $q$ and $n \geq 3$, ${\operatorname{Sp}}_{2n}(q)$ for any $q$ and $n \geq 2$, or ${\operatorname{Spin}}^\pm_{2n}(q)$ for any $q$ and $n \geq 4$. Let $2\ne\ell{\not|}q$ be a prime such that the Sylow $\ell$-subgroups of $G$ are non-cyclic. Then any non-unipotent irreducible complex character of $G$ vanishes on some $\ell$-singular regular semisimple element, except for the two cases $G=C_2(2)={\operatorname{Sp}}_4(2)$ and $G=C_4(2)={\operatorname{Sp}}_8(2)$.

The group ${\operatorname{Sp}}_4(2)\cong{\mathfrak{S}}_6$ contains no $3$-singular regular semisimple elements. It has three non-trivial irreducible characters which do not vanish on any $3$-singular class, the unipotent character $\sys{0 1 2}{-}$ and the two characters of degree $10$ (belonging to Lusztig series of type $A_1(q)\times (q+1)$).

The group ${\operatorname{Sp}}_8(2)$ has only one $5$-singular regular semisimple class and there are $15$ irreducible characters which do not vanish on this class. There is only one non-trivial character which does not vanish on any $5$-singular class, the unipotent character $\sys{0 1}{4}$.
:::

::: proof
*Proof.* We use the following facts from Deligne--Lusztig theory. The irreducible characters of $G$ are partitioned into Lusztig series which are parameterised by semisimple conjugacy classes of the dual group $G^*$. If $s \in G^*$ is semisimple then the values of characters in the Lusztig series of $s$ on semisimple elements $t \in G$ are linear combinations of values of Deligne--Lusztig characters on $t$ which belong to types of tori which occur in the connected centraliser of $s$ in ${\mathbf{G}}^*$. In particular Deligne--Lusztig characters corresponding to a maximal torus $T$ of $G$ vanish on regular semisimple classes which do not intersect $T$, see e.g. [@LMS13 Prop. 6.4].

Since ${\mathbf{G}}$ is simply-connected the dual group ${\mathbf{G}}^*$ has trivial center so that non-unipotent characters are in Lusztig series of non-central elements.

We show the theorem by listing in each case a set of types of maximal tori which contain regular $\ell$-singular elements by Lemma [\[lem:regelts\]](#lem:regelts){reference-type="ref" reference="lem:regelts"} and which cannot all occur in any proper centraliser. We have described these subgroups together with the types of tori they contain in Lemma [\[lem:maxred\]](#lem:maxred){reference-type="ref" reference="lem:maxred"}. Note that for ${\mathbf{G}}$ of type $B_n$ the dual group is of type $C_n$ (we need to apply Lemma [\[lem:maxred\]](#lem:maxred){reference-type="ref" reference="lem:maxred"} for type $C_n$ and consider tori with regular elements in type $B_n$); the same remark holds with $B_n$ and $C_n$ interchanged.

Let $d=d_\ell(q)$ and write $n = ad+r$ with $0 \leq r < d$ for odd $d$ and $n = ae+r$ with $0 \leq r < e$ for even $d=2e$, $a\geq 2$, as explained above.

Recall that for odd $d$ a torus of type $(\la,\mu)$ contains $\ell$-singular elements if and only if some part of $\la$ is a positive multiple of $d$. For even $d=2e$ a torus of type $(\la,\mu)$ contains $\ell$-singular elements if and only if $\mu$ contains an odd multiple of $e$ or $\la$ contains an even multiple of $e$.

We collect the tori we consider in Table [1](#tab:non-unip){reference-type="ref" reference="tab:non-unip"}.

[]{#tab:non-unip label="tab:non-unip"}

::: {#tab:non-unip}
  type              $d$    $a$    $r$   tori
  --------------- ------- ------ ------ -------------------------------------------------------------------------------------------
  $C_n$,$B_n$       odd    any    $0$   $((n),-)$, $((n-d),(d))$, and $((n-d),(1,d-1))$ if $d>1$
  $C_n$,$B_n$       odd    any    $>0$  $((n-r),(r))$, $((n-r-d),(d+r))$, $((n-r-d),(d+r-1, 1))$
  $D_n$             odd    any     0    $((n),-)$, $((n-1,1),-)$ if $d=1$, or $((n-d),(d-1,1))$ if $d>1$
  $D_n$             odd    any    $>0$  $((n-d-r, d+r),-)$, $((n-r,r),-)$ if $r \neq 2$, or $((n-2),(1,1))$ if $r=2$
  $^2D_n$$(^*)$     odd    any     0    $((n-d),(d))$, $((d),(n-d))$, $((n-d-1,d),(1))$ if $d>1$
  $^2D_n$           odd    any    $>0$  $((n-r),(r))$, $((n-d-r),(d+r))$, $((n-d-r,1),(d+r-1))$
  $C_n$,$B_n$      $=2e$   even   $0$   $((n),-)$, $((n-e),(e))$, $(-,(n-e-1,e,1))$ if $e>1$
  $C_n$,$B_n$      $=2e$   even   $>0$  $((n-r),(r))$, $(-,(n-e,e))$, $(-,(n-e-1,e,1))$ if $r\neq 1$
  $C_n$,$B_n$      $=2e$   odd    $0$   $(-,(n))$, $(-,(n-e,e))$, $((n-e-1),(e,1))$ if $e>1$
  $C_n$,$B_n$      $=2e$   odd    $>0$  $(-,(n-r,r))$, $((n-r-e),(r+e))$, $((n-r-e),(r+e-1,1))$
  $D_n$            $=2e$   even   $0$   $((n),-)$, $((n-e-1),(e,1))$ if $(n,e) \notin
                                        \{(4,1),(6,3)\}$, or $((n-e-2),(e,2))$ otherwise
  $D_n$            $=2e$   even   $>0$  $(-,(n-e,e))$, $((n-1,1),-)$ if $r=1$, $((n-r),(r-1,1))$ if $r>1$
  $D_n$$(^*)$      $=2e$   odd    $0$   $(-,(n-e,e))$, $(-,(n-2e,2e))$, $((1), (n-2e, 2e-1))$ if $e>1$, $((2e),(e-1,1)$ if $n=3e$
  $D_n$            $=2e$   odd    $>0$  $(-,(n-r,r))$, $(-,(n-e,e))$, $((1),(n-r,r-1))$ if $r>1$
  $^2D_n$          $=2e$   even   $0$   $((n-e),(e))$, $((n-2e),(2e))$, $((n-2e, 2e-1),(1))$ if $e>1$
  $^2D_n$          $=2e$   even   $>0$  $((n-r),(r))$, $((n-e),(e))$, $((n-r,1),(r-1))$ if $r>1$
  $^2D_n$          $=2e$   odd    $0$   $(-,(n))$, $((n-e),(e))$, $((n-e,1),(e-1))$ if $e>1$
  $^2D_n$          $=2e$   odd    $>0$  $((n-e-r),(e+r))$, $(-,(n-r,r-1,1))$ if $r>1$, $((1),(n-1))$ if $r=1$

  : Tori needed in the proof of Theorem [\[thm:non-unip\]](#thm:non-unip){reference-type="ref" reference="thm:non-unip"}
:::

A few additional remarks are in order. In the two cases marked with $(^*)$ in the table we need to rule out the possibility that the given tori all lie in a subgroup of type $D_d + D_{n-d}$ or $D_e + D_{n-e}$, respectively. Such a subgroup stabilises a decomposition of the orthogonal space on which $G$ acts into two non-degenerate subspaces. In the first case one of these subspaces must be of minus- and the other of plus-type. So the corresponding finite subgroups are of type ${}^2\!D_d+D_{2d}$ or $D_d+{}^2\!D_{2d}$, each of these only contains one of the types of tori, $((d),(n-d))$ or $((n-d),(d))$. The argument for the second case is similar, there both subspaces must be of minus-type or both of plus-type.

It remains to check for which groups one of the tori given in Table [1](#tab:non-unip){reference-type="ref" reference="tab:non-unip"} does not contain regular elements. Note that for $q=3$ we have $d > 2$ because $\ell \neq 2$, and for $q=2$ we have $d > 1$. Furthermore, when $r>0$, we have $d\geq 3$ or $e \geq 2$, respectively. This implies that only the following cases need an extra consideration:

$C_2(2)$ with $e=1$: this is the first exception mentioned in the statement.

$B_4(q)$ with $q=3$ and $e=2$: We compute that for $q=3$ the torus of type $((1),(1,2))$ contains regular element. So, we can argue with tori of types $((4),-)$ and $((1),(1,2))$.

$C_4(q)$ with $q=3$ and $e=2$: In this case the torus of type $((2),(2))$ in $C_4(3)$ contains regular elements. Here we can argue with tori of types $((4),-)$ and $((2),(2))$ by checking that the dual group (adjoint of type $B_4(3)$) does not contain a semisimple element whose centraliser contains tori of both types.

For $C_4(2)$ and $e=2$ (and so $\ell = 5$) only tori of type $((4),-)$ contain $\ell$-singular regular elements. This leads to the second exception mentioned in the statement.

${}^2\!D_4(2)$ with $e=1$: Here, the maximal tori containing $\ell$-elements all have conjugates inside a subgroup of type $D_1+D_3$. We can apply the argument from above: the tori of types $((1),(3))$ and $((3),(1))$ cannot both occur in the same rational form of such a subgroup. ◻
:::
