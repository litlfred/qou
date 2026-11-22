---
doc_id: arxiv-1508.01627v4
doc_title: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS "
section_id: sec-012-42-unipotent-characters
section_title: "Unipotent characters"
section_number: 4.2
pages: 10-14
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.985
doc_brief: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS IN CLASSICAL GROUPS"
---
[]{#ssec:unipotent label="ssec:unipotent"} In the following theorem we use symbols to describe unipotent characters and refer to Section [\[subsec:symb\]](#subsec:symb){reference-type="ref" reference="subsec:symb"} for the notation.

::: thm
[]{#thm:unip label="thm:unip"} Let $G$ be one of the groups ${\operatorname{Spin}}_{2n+1}(q)$ for odd $q$ and $n \geq 3$, ${\operatorname{Sp}}_{2n}(q)$ for any $q$ and $n \geq 2$, or ${\operatorname{Spin}}^\pm_{2n}(q)$ for any $q$ and $n \geq 4$. Let $2\ne\ell{\not|}q$ be a prime such that the Sylow $\ell$-subgroups of $G$ are non-cyclic.

Let $\rho_{\mathcal{S}}$ be a unipotent character of $G$ for some symbol ${\mathcal{S}}$ and assume that $\rho_{\mathcal{S}}$ does not vanish on any regular semisimple $\ell$-singular class. Then either $\rho_{\mathcal{S}}$ is the trivial character, or the Steinberg character, or up to Alvis-Curtis duality we are in one of the following cases (as before we set $d = d_\ell(q)$, and interpret $\underline{-1}$ as the empty set):

1.  $G={\operatorname{Sp}}_{2n}(q)$ or ${\operatorname{Spin}}_{2n+1}(q)$, $d$ is odd, $n = 2d+r$ with $0\leq r < d$ and $${\mathcal{S}}= \ensuremath{\left(\begin{array}{c}{\underline{d-r-1}\sm 0 \cup d \cup 2d}\\{\underline{d-r-1}}\end{array}\right)};$$

2.  $G={\operatorname{Sp}}_{2n}(q)$ or ${\operatorname{Spin}}_{2n+1}(q)$, $d=2e$ is even, $n=2e+r$ with $0\leq r < e$ and $${\mathcal{S}}= \ensuremath{\left(\begin{array}{c}{\underline{e-r-1} \cup e}\\{\underline{e-r-1}\sm 0 \cup 2e}\end{array}\right)};$$

3.  $G={\operatorname{Spin}}_{2n}^+(q)$, $d$ is odd, $n = 2d+r$ with $0\leq r < d$ and $${\mathcal{S}}= \ensuremath{\left(\begin{array}{c}{\underline{d-r-1}\sm 0 \cup d \cup 2d}\\{\underline{d-r}}\end{array}\right)};$$

4.  $G={\operatorname{Spin}}_{2n}^+(q)$, $d=2e$ is even, $n=2e+r$ with $0\leq r \le e$ and $${\mathcal{S}}= \ensuremath{\left(\begin{array}{c}{\underline{e-r-1} \cup e}\\{\underline{e-r}\sm 0 \cup  2e}\end{array}\right)};$$

5.  $G={\operatorname{Spin}}_{2n}^-(q)$, $d$ is odd, $n = 2d+r$ with $0 < r \le d$ and $${\mathcal{S}}= \ensuremath{\left(\begin{array}{c}{\underline{d-r}\sm 0 \cup d \cup 2d}\\{\underline{d-r-1}}\end{array}\right)};$$

6.  $G={\operatorname{Spin}}_{2n}^-(q)$, $d=2e$ is even, $n=2e+r$ with $0 < r < e$ and $${\mathcal{S}}= \ensuremath{\left(\begin{array}{c}{\underline{e-r} \cup e}\\{\underline{e-r-1}\sm 0 \cup  2e}\end{array}\right)};$$

7.  $G={\operatorname{Sp}}_4(2)$, $d=2$ and ${\mathcal{S}}=\sys{0\ 1\ 2}{-}$ or $\sys{0\ 2}{1}$ (there is no regular semisimple $\ell$-singular element);

8.  $G={\operatorname{Sp}}_6(2)$, $d=2$ and ${\mathcal{S}}=\sys{0\ 1\ 3}{-}$;

9.  $G={\operatorname{Sp}}_8(2)$, $d=4$ and ${\mathcal{S}}=\sys{0\ 1}{4}$ or $\sys{1\ 4}{0}$; or

10. $G={\operatorname{Spin}}_8^-(2)$, $d=2,4$ and ${\mathcal{S}}=\sys{1\ 3}{-}$.

Conversely, all characters listed above take non-zero values on all regular semisimple $\ell$-singular classes. More precisely, in cases $G={\operatorname{Spin}}_8^-(2)$, $d=2,4$, ${\mathcal{S}}=\sys{1\ 3}{-}$ the character $\rho_{\mathcal{S}}$ has value $2$ on classes of type $(-,(2,1,1))$. In all other cases the character values are $\pm 1$.
:::

::: proof
*Proof.* (a) Our strategy is to use Corollary [\[cor:vanish\]](#cor:vanish){reference-type="ref" reference="cor:vanish"} of the Murnaghan--Nakayama formula. We consider maximal tori with $\ell$-singular regular elements which are parameterised by pairs of partitions with very few parts. For example, if for a symbol ${\mathcal{S}}$ the character $\rho_{\mathcal{S}}$ has non-zero value on regular elements in a torus of type $((\la_1),(\mu_1))$ then the Murnaghan-Nakayama formula implies that we can remove a $\la_1$-hook from ${\mathcal{S}}$ and that the resulting symbol has a $\mu_1$-cohook which after removing leaves a symbol of rank $0$.

\(b\) For groups of type $B_n$ and $C_n$ we need to consider symbols of rank $n$ with odd defect. First note that there is only one symbol of rank $0$ with odd defect, namely the defect $1$ symbol $$\sys{0}{-} = \sys{\underline{n}}{\underline{n-1}}$$ (apply the shift operation $n$ times). We will write all symbols with $2n+1$ entries, because this way we can construct all symbols of rank $n$ by adding hooks or cohooks starting from the rank $0$ symbol without the need of further shift operations. Also, we will write all symbols of non-zero defect such that the larger number of entries is in the first row.

The symbols of rank $t \leq n$ which have a $t$-hook are $\sys{\underline{n}\sm k\cup k+t}{\underline{n-1}}$ for $n+1-t \leq k \leq n$ and their dual symbols $\sys{\underline{n}}{\underline{n-1}\sm k\cup k+t}$ for $n-t\leq k\leq n-1$.

To find up to duality all symbols ${\mathcal{S}}$ of rank $n$ which have an $(n-t)$-cohook $c$ such that ${\mathcal{S}}\sm c$ has a $t$-hook, it is sufficient to take the first set of symbols of rank $t$ with a $t$-hook and to add an $(n-t)$-cohook in all possible ways (filling the gap $k$, creating new entries in the first or the second row or moving the $k+t$ entry). We get: $$\begin{aligned}
  \ensuremath{\left(\begin{array}{c}{\underline{n}\cup l+n}\\{\underline{n-1}\sm l}\end{array}\right)}&\quad (1\leq l\leq t),\\
  \ensuremath{\left(\begin{array}{c}{\underline{n}\sm k \cup k+t \cup l+n-t}\\{\underline{n-1}\sm l}\end{array}\right)}&\quad (n-t< k \leq n,\
    t< l < n,\  k-l \neq n-2t),\\
  \ensuremath{\left(\begin{array}{c}{\underline{n-1}\cup l+n-t}\\{\underline{n}\sm k \sm l \cup k+t}\end{array}\right)}&\quad
    (n-t< k \leq n,\ t \leq l \leq n, k\neq l),\\
  \ensuremath{\left(\begin{array}{c}{\underline{n-1}\cup k+n}\\{\underline{n}\sm k}\end{array}\right)}&\quad (n-t< k \leq n).
\end{aligned}$$

\(c\) We now prove the theorem for the case $B_n$, $C_n$ for $n\geq 3$ and odd $d$. Write $n = ad+r$ with $0\leq r <d$. Note that for $q=2$ or $3$ we have $d > 1$ (since $\ell \neq 2$). In our argument we will use maximal tori which by Lemma [\[lem:regelts\]](#lem:regelts){reference-type="ref" reference="lem:regelts"} contain regular $\ell$-singular elements.

First assume $r=0$ and let ${\mathcal{S}}$ be a symbol of rank $n$ such that $\rho_{\mathcal{S}}$ is non-zero on all regular semisimple $\ell$-singular classes. Then as a torus of type $((n),-)$ contains $\ell$-singular elements, ${\mathcal{S}}$ has an $n$-hook, that is (up to duality) one of $${\mathcal{S}}= \ensuremath{\left(\begin{array}{c}{\underline{n}\sm k \cup k+n}\\{\underline{n-1}}\end{array}\right)} \qquad (1\leq k\leq n).$$ Tori of type $((d),(n-d))$ also contain $\ell$-singular regular elements. Therefore ${\mathcal{S}}$ must have a $d$-hook $h$ and an $(n-d)$-cohook such that ${\mathcal{S}}\setminus h$ still has an $(n-d)$-cohook. This is only the case for $k=n$ and $k=n-d$. For $k=n$ we obtain the symbol $\sys{\underline{n-1}\cup
2n}{\underline{n-1}}$ of the trivial character. For $k = n-d$ we get the symbol $${\mathcal{S}}= \ensuremath{\left(\begin{array}{c}{\underline{n}\sm n-d \cup 2n-d}\\{\underline{n-1}}\end{array}\right)}.$$ If $a>2$ then this symbol has no $(a-1)d = (n-d)$-hook, hence $\rho_{\mathcal{S}}$ is zero on regular elements in tori of type $((n-d),(d))$. For $a=2$ we get one of the symbols shown in part (1) of the statement (after applying the inverse shift operation $n-d$ times).

Now let $r>0$ (and so $d\geq 3$). We consider tori of types $((ad),(r)) = ((n-r),(r))$ and $((d,n-d),-)$. Here we check for every symbol ${\mathcal{S}}$ listed in (b) (for $t=n-r$) if it has an $(n-r)$-hook and if we can get the rank $0$ symbol by removing a $d$-hook and an $(n-d)$-hook in both possible orders. Note that the last condition implies that ${\mathcal{S}}$ has defect one because removing hooks does not change the defect. These conditions yield in all cases relations between the parameters $k$ and $l$ and then determine $k$. The only possible symbols which remain are those of the trivial character and $${\mathcal{S}}= \ensuremath{\left(\begin{array}{c}{\underline{n}}\\{\underline{n}\sm d \sm n-r \cup n+d-r}\end{array}\right)}.$$ If $a>2$ this has no $(a-1)d$-hook and so $\rho_{\mathcal{S}}$ is zero on regular elements in tori of type $(((a-1)d),(d+r))$. For $a=2$ the dual of ${\mathcal{S}}$ is given in statement (1), that is $\sys{\underline{n-1}\sm n-d+r\cup n+r\cup
n+d+r}{\underline{n-1}}$ and applying the inverse shift operation $n-d+r$ times.

\(d\) The argument for type $B_n$, $C_n$, $n \geq 7$, and even $d=2e$, $n=ae+r$, is very similar. Pairs of partitions corresponding to tori with $\ell$-singular regular elements must now have an odd multiple of $e$ in the second part or an even multiple of $e$ in the first part. Therefore we distinguish the cases of even and odd $a$ and of $r=0$ and $r>0$. We just list the types of tori which we consider in the given order such that the arguments from (c) work with slight modifications.

$a$ even, $r=0$: $((n),-)$ and $((n-e),(e))$, and for $a>2$ also $((n-2e),(2e))$.

$a$ even, $r>0$: $((n-r),(r))$, $(-,(n-e,e))$ and $((n-e),(e))$, and for $a>2$ also $(-,((a-1)e, e+r))$.

$a$ odd, $r=0$: $((n-e),(e))$, $(-,(n))$ and $(-,(n-e,e))$, and finally to rule out a symbol of defect 3 also $((n-e,e),-)$ (if $a\leq 3$) or $((n-3e), (3e))$ (if $a>3$).

$a$ odd, $r>0$: $((n-r-e),(e+r))$, $(-,(n-r,r))$ and $((n-e),(e))$.

\(e\) The cases of type $D_n$ and ${}^2\!D_n$ can also be discussed with very similar arguments. The only symbol of rank $0$ and even defect has defect $0$ and is $\sys{-}{-} = \sys{\underline{n-1}}{\underline{n-1}}$ and so all the symbols of rank $n$ with an $n$-hook are $${\mathcal{S}}=\ensuremath{\left(\begin{array}{c}{\underline{n-1}\sm k \cup k+n}\\{\underline{n-1}}\end{array}\right)} \quad (0\leq k \leq n).$$ Here it is sufficient to consider the cases with $k\geq (n-1)/2$ in the further arguments because the remaining ones are the duals of these.

\(f\) Type $D_n$, $n\geq 7$. We list again which tori we consider in the various cases.

$d$ odd, $r=0$: $((n),-)$ and in case $d=1$ we use $((n-1, 1),-)$ and for $d\geq 3$ we use $((n-d),(d-1,1))$. For $a>2$ we also need $((n-2d),(2d-1,1))$ to rule out one possibility.

$d$ odd, $r>0$: $((n-d,d),-)$ and $((n-r,r),-)$ if $r\neq 2$ or $((n-2),(1,1))$ if $r=2$, $((d),(n-d-1,1))$.

$d=2e$ even, $n=ae$, $a$ even: $((n),-)$ and $(-,(n-1,1))$ if $e=1$ or $((n-e-1),(e,1))$ if $e>1$. For $a>2$ we also use $((n-2e),(2e-1,1))$.

$d=2e$ even, $n=ae+r$, $a$ even, $r>0$: $(-,(n-e,e))$, $((n-e-1),(e,1))$ and $((n-r,r),-)$ if $r\neq 2$ or $((n-2),(1,1))$ if $r=2$. For $a>2$ we also need $((2e),(n-2e-1,1))$.

$d=2e$ even, $n=ae$, $a$ odd: $(-,(n-e,e))$ and $((n-e,e),-)$ if $e \neq 2$ or $((n-2),(1,1))$ if $e=2$. Finally, use $((n-3e,3e),-)$ if $a > 3$. For $a=3$ we get the exception listed in (4) for the parameter $r=e$ (that is $n = 2e+r = 3e$).

$d=2e$ even, $n=ae+r$, $a$ odd, $r>0$: $(-,(n-e,e))$, $(-,(n-r,r))$, $((n-e-1),(e,1))$ and $((2e),(n-2e-1,1))$.

\(g\) Type ${}^2\!D_n$, $n\geq 7$. We list again which tori we consider in the various cases.

$d$ odd, $n=ad$: Recall that in this case we have $a\geq
3$. We use $((n-d),(d))$ and $((n-2d),(2d))$. For $a > 3$ we also use $((n-3d),(d))$ and for $a=3$ we get the exception listed in (5) for $r=d$ (that is $n = 2d+r = 3r$).

$d$ odd, $n=ad+r$, $r>0$ (and so $d\geq 3$): $((n-r),(r))$, $((d),(n-d))$ and $((d,1),(n-d-1))$. And for $a>2$ also $((2d),(n-2d))$. For $a=2$ this leads to the other exceptions listed in (5).

$d=2e$ even, $n=ae$, $a$ even: Recall that in this case we have $a\geq 4$. We use $((n-e),(e))$, $((n-2e),(2e))$ and one of $((3),(n-3))$ (if $e=1$) or $((n-3e),(3e))$ (if $e>1$) or $(-,(6,1,1))$ (if $n=8$).

$d=2e$ even, $n=ae+r$, $a$ even, $r>0$ (so $e>1$): $((n-e),(e))$ and $((n-r),(r))$. For $a>2$ we also use $((2e),(n-2e))$. For $a=2$ this leads to the exceptions listed in (6).

$d=2e$ even, $n=ae$, $a$ odd: $(-,(n))$, $((n-e),(e))$ and $((n-e-1,1),(e))$.

$d=2e$ even, $n=ae+r$, $a$ odd, $r>0$: $((n-e),(e))$, $((n-e-r),(e+r))$ and $((2e),(n-2e))$. Finally also $((r),(n-r))$ if $r\neq 2$ or $(-,(n-2,1,1))$ for $r=2$.

\(h\) For small rank $n \leq 6$ we compute the number of regular elements in all tori, and determine the values of unipotent characters on all $\ell$-singular regular semisimple classes via the Murnaghan-Nakayama formula in Theorem [\[thm:MN\]](#thm:MN){reference-type="ref" reference="thm:MN"}. This yields the extra cases in statements (7) to (10).

\(i\) The symbols given in statements (1) to (6) each contain a unique $d$-hook and a unique $2d$-hook (or a unique $e$-cohook and unique $2e$-hook, respectively). Removing these we always get the symbol of the trivial representation of the appropriate rank (and the Steinberg representation for the dual symbols). Therefore, the Murnaghan-Nakayama formula shows that the values on all regular semisimple $\ell$-singular elements are $\pm 1$. ◻
:::
