---
doc_id: arxiv-1508.01627v4
doc_title: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS "
section_id: sec-007-32-symbols
section_title: "Symbols"
section_number: 3.2
pages: 6-7
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
toc_source: outline
text_source: latex
latex_prose_ratio: 0.895
latex_coverage_ratio: 0.962
doc_brief: "REPRESENTATION THEORY An Electronic Journal of the American Mathematical Society (Xxxx XX, XXXX) S 1088-4165(XX)0000-0 A MURNAGHAN–NAKAYAMA RULE FOR VALUES OF UNIPOTENT CHARACTERS IN CLASSICAL GROUPS"
---
[]{#subsec:symb label="subsec:symb"} We now specialise to simple groups of classical type. By Lusztig's results their unipotent characters are parameterised by so-called *symbols*. Here, a symbol is an unordered pair of finite sets of non-negative integers, usually denoted as $${\mathcal{S}}=\binom{X}{Y}=\begin{pmatrix} \la_1& \la_2& \ldots& \la_r\\
  \mu_1& \mu_2& \ldots& \mu_s\end{pmatrix}$$ with $\la_1<\la_2<\ldots<\la_r$ and $\mu_1<\mu_2<\ldots<\mu_s$ where $r,s\ge0$. Two symbols are said to be *equivalent* if one can be obtained from the other by a sequence of shift operations $${\mathcal{S}}\mapsto \begin{pmatrix} 0& \la_1+1& \la_2+1& \ldots& \la_r+1\\
  0& \mu_1+1& \mu_2+1& \ldots& \mu_s+1\end{pmatrix}$$ or by interchanging the rows $X$ and $Y$ of ${\mathcal{S}}$. The *rank* of ${\mathcal{S}}$ is by definition $${\operatorname{rk}}({\mathcal{S}})=\sum_{i=1}^r \la_i+\sum_{i=1}^s\mu_i
  -\Big\lfloor\left(\frac{r+s-1}{2}\right)^2\Big\rfloor.$$ The *defect* of ${\mathcal{S}}$ is ${\operatorname{def}}({\mathcal{S}}):=|r-s|$. Note that the rank and the defect are well-defined on equivalence classes. We will use the following notation to describe explicit symbols: $\underline{n} := \{0,1,\ldots,n\}$ and for a set $X$, a $k\in X$ and $l\notin X$ we write $X \sm k \cup l := X \sm\{k\} \cup \{l\}$.

Let $d$ be a positive integer. We say that ${\mathcal{S}}$ has a *$d$-hook* $h$ at $x\in X$ if $0\le x-d\notin X$, and similarly at $x\in Y$. Removing that $d$-hook leads to the symbol ${\mathcal{S}}\sm{h}:=\binom{X'}{Y}$ with $X'=X\sm x\cup(x-d)$ (respectively ${\mathcal{S}}\sm{h}:=\binom{X}{Y'}$ with $Y'=Y\sm x\cup(x-d)$). Attached to the hook $h$ is the sign $\eps_h:=(-1)^m$ where $m:=|\{y\in X\mid x-d<y<x\}|$ (respectively $m:=|\{y\in Y\mid x-d<y<x\}|$). We say that ${\mathcal{S}}$ has a *$d$-cohook* $c$ at $x\in X$ if $0\le x-d\notin Y$, and similarly at $x\in Y$. Removing that $d$-cohook leads to the symbol ${\mathcal{S}}\sm{c}:=\binom{X'}{Y'}$ with $X'=X\sm\{x\},Y'=Y\cup\{x-d\}$ (respectively $Y'=Y\sm\{x\},
X'=X\cup\{x-d\}$). Attached to the cohook $c$ is the sign $\eps_c:=(-1)^m$, where $m:=|\{y\in X\mid y<x\}|+|\{y\in Y\mid y<x-d\}|$ (respectively $m:=|\{y\in Y\mid y<x\}|+|\{y\in X\mid y<x-d\}|$), see [@FS86 §3] for example. Note that removing a $d$-hook or a $d$-cohook from a symbol of rank $n$ yields a symbol of rank $n-d$.

For a symbol ${\mathcal{S}}=(X,Y)$ with all entries of $X,Y$ not larger than $m$ we define the *dual symbol* ${\mathcal{S}}^\vee=(X',Y')$ where $$X'= \underline{m} \setminus \{m-x\mid x\in X\}\mbox{ and }
  Y'= \underline{m} \setminus \{m-y\mid y\in Y\}.$$

The hooks and cohooks of $S$ and $S^\vee$ are each in natural bijection such that removing hooks or cohooks commutes with the duality operation. This observation will allow us to simplify some of the later statements and proofs.
