---
doc_id: arxiv-1108.1048v3
doc_title: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS"
section_id: sec-006-3-explicit-construction-of-irreducible-modules-f
section_title: "Explicit Construction of Irreducible Modules for Finite Classical Type"
section_number: 3
pages: 17-28
source_pdf: 1108.1048v3.pdf
source_sha256: 6f2b83450ba923d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.666
latex_coverage_ratio: 0.978
doc_brief: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS — We give an explicit construction of irreducible modules over Khovanov-Lauda- Rouquier algebras R and their"
---
[]{#Sec: construction for classical type label="Sec: construction for classical type"}

In Sections [\[Sec: construction for classical type\]](#Sec: construction for classical type){reference-type="ref" reference="Sec: construction for classical type"} and [\[Sec:
final\]](#Sec:
final){reference-type="ref" reference="Sec:
final"}, we assume that $\mathfrak{A}$ is of finite classical type. We maintain the notation from Sections [\[Sec: Crystals and KLR
algs\]](#Sec: Crystals and KLR
algs){reference-type="ref" reference="Sec: Crystals and KLR
algs"} and [\[Sec: Description Nk\]](#Sec: Description Nk){reference-type="ref" reference="Sec: Description Nk"}. Our aim in this section is to present an explicit construction of irreducible $R$-modules (resp. $R^\lambda$-modules) for finite classical type using a single induction step. Let $\mathbf{B}$ be the crystal of the irreducible highest weight $U_q(\mathfrak{g})$-module $V(\Lambda_n)$ if $\mathfrak{A}$ is of type $\mathsf{A}_n$ and of $V(\Lambda_1)$ if $\mathfrak{A}$ is of type $\mathsf{B}_n, \mathsf{C}_n, \mathsf{D}_n$. We define the $1$ or $2$-dimensional irreducible $R$-module $\Delta_{(a,b)}$ for $a,b
\in \mathbf{B}$ with $a \succ b$ by using the structure of $\mathbf{B}$. Combining Proposition [\[Prop: crystal iso\]](#Prop: crystal iso){reference-type="ref" reference="Prop: crystal iso"} with some facts about the modules $\Delta_{(a,b)}$ and the descriptions of the adapted strings, we define the outer tensor product $\Delta(\mathbf{a}(v)):=
\Delta(\mathbf{a}(v);1) \boxtimes \cdots \boxtimes
\Delta(\mathbf{a}(v);n)$ of $\Delta_{(a,b)}$'s for $v \in B(\infty)$ (resp. $v \in B(\lambda)$). For $v \in B(\lambda)$, the number $\eta(v)$ of $\Delta_{(a,b)}$'s in $\Delta(\mathbf{a}(v))$ has an upper bound; i.e., $\eta(v) \le n \lambda(h),$ where $h$ is as in Lemma [\[Lem: upper bound\]](#Lem: upper bound){reference-type="ref" reference="Lem: upper bound"} below. Then, we construct a map $\Psi: B(\infty) \rightarrow \mathbb{B}(\infty)$ (resp. $\Psi^{\lambda}:
B(\lambda) \rightarrow  \mathbb{B}(\lambda)$) by taking the head of $\mathsf {Ind}
\Delta(\mathbf{a}(v))$ (Theorem [\[Thm: main theorem\]](#Thm: main theorem){reference-type="ref" reference="Thm: main theorem"}). The proof that this map is indeed a crystal isomorphism, hence is compatible with the Kashiwara operators, will be provided in the next section.

We first give a detailed description of $\mathcal{S}$ and $\mathcal{S}^\lambda$ for finite classical type with respect to the expression of $w_0 =  r_{\mathbf{s}_1} \cdots r_{\mathbf{s}_n}$ in Table [\[Tb: w0\]](#Tb: w0){reference-type="ref" reference="Tb: w0"}. Let $\triangle_{\mathsf{A}_n}$ be the triangle consisting of right justified rows of boxes with $1$ box in the first (bottom) row, $2$ boxes in the second row, $\ldots$, and $n$ boxes in the top row. Let $\triangle_{\mathsf{B}_n}$ (resp. $\triangle_{\mathsf{D}_n}$) be the triangle consisting of centered rows of boxes having $1$ box (resp. $2$ boxes) in the first row, $3$ boxes (resp. $4$ boxes) in the second row, ..., and $(2n-1)$ boxes (resp. $(2n-2)$ boxes) in the top row. Set $\triangle_{\mathsf{C}_n} = \triangle_{\mathsf{B}_n}$. When it is not necessary to specify the type, we omit the subscript and simply write $\triangle$. For $\mathbf{a} \in \mathcal{S}$, let $\triangle(\mathbf{a})$ denote the filling of the triangle $\triangle$ with entries of $\mathbf{a}$ from left to right in each row, and from bottom to top. Let $t_{ij}$ be the $j$th entry of the $i$th row in $\triangle(\mathbf{a})$ and let $\triangle(\mathbf{a})
= \{t_{ij}\}_{ 1 \le i \le n' ,\ p_i \le j \le p_i'}$, where $$\begin{aligned}
 n' &=& \begin{cases} n & \qquad \quad  (\mathsf{A}_n, \mathsf{B}_n, \mathsf{C}_n) \\
 n-1 & \quad  \qquad (\mathsf{D}_n) \end{cases} \\
 p_i &=& \begin{cases}  n+1-i & \qquad  (\mathsf{A}_n, \mathsf{B}_n, \mathsf{C}_n),\\
  n-i & \qquad (\mathsf{D}_n) \end{cases} \\
  p_i' &=& \begin{cases} n & \qquad (\mathsf{A}_n), \\
   n-1+i & \qquad  (\mathsf{B}_n, \mathsf{C}_n, \mathsf{D}_n). \end{cases} 
\end{aligned}$$ Set $t_{ij}=0$ except when $1 \le i \le n' ,\ p_i \le j \le p_i'$. For example, if $\mathbf{a}=(2,3,1,0,9,8,4,2,1) \in \mathcal{S}$ for type $\mathsf{B}_3$ and $\mathbf{a}'=(5,2,7,4,3,1,9,6,4,5,3,2) \in \mathcal{S}$ for type $\mathsf{D}_4$, then $t_{1,3}=2$ in $\triangle(\mathbf{a})$, $t_{3,4}=5$ in $\triangle(\mathbf{a}')$ and $$\triangle(\mathbf{a}) =  \newcommand, \quad \quad \ \triangle(\mathbf{a}') =  \newcommand.$$

Let $\tilde{\mathsf{c}}(t_{i,n-1}) = \sum_{k=i}^{n-1} t_{k,n-1}$,  $\tilde{\mathsf{c}}(t_{i,n}) = \sum_{k=i}^{n-1} t_{k,n}$, and $$\begin{aligned}
\label{eq:cdef}
\mathsf{c}(t_{i,j}) = \left\{
                      \begin{array}{ll}
                        \sum_{k=i}^n t_{k,j} & \hbox{if } j \le n\ (\mathsf{A}_n),\ \  j = n\ (\mathsf{B}_n), \\
                        \sum_{k=i}^n(t_{k,j} + t_{k,2n-j}) & \hbox{if } j < n\ (\mathsf{B}_n, \mathsf{C}_n), \\
                        \sum_{k=i}^{n-1} (t_{k,j} + t_{k,2n-1-j}) & \hbox{if } j < n-1\ (\mathsf{D}_n), \\
                        \sum_{k=i}^n 2t_{k,j} & \hbox{if } j = n\ (\mathsf{C}_n), \\
                        \sum_{k=i}^{n-1} (t_{k,n-1}+t_{k,n}) & \hbox{if } j=n-1,n\  (\mathsf{D}_n), \\
                        t_{i,j} + \sum_{k=i+1}^{n}(t_{k,2n-j}+t_{k,j}) & \hbox{if } j > n\ (\mathsf{B}_n, \mathsf{C}_n),\\
                        t_{i,j} + \sum_{k=i+1}^{n-1}(t_{k,2n-1-j}+t_{k,j}) & \hbox{if } j > n\  (\mathsf{D}_n).
                      \end{array}
                    \right.
\end{aligned}$$

::: proposition
[]{#Prop: S lambda label="Prop: S lambda"} Let $(\mathfrak{A}, \mathsf{P}, \Pi, \mathsf{P}^{\vee}, \Pi^{\vee})$ be a Cartan datum of finite classical type, and let $\lambda = \lambda_1 \Lambda_1 + \cdots + \lambda_n \Lambda_n \in \mathsf{P}^+$. For $\mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell}$, let $\triangle(\mathbf{a}) = \{t_{ij}\}_{ 1 \le i \le n' ,\ p_i \le j \le p_i'}$ be as above and assume $\mathsf{c}(t_{i,j})$ is as in [\[eq:cdef\]](#eq:cdef){reference-type="eqref" reference="eq:cdef"}. Then $$\begin{aligned}
(\mathsf{A}_n):\  \mathcal{S} & = \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid  t_{i,n+1-i}  \ge t_{i,n+2-i}  \ge \cdots \ge t_{i,n}\ \text{ for }1 \le i \le n \}, \\
\mathcal{S}^\lambda & = \{ \mathbf{a} \in \mathcal{S} \mid  t_{i,j} \le \lambda_j + \mathsf{c}(t_{i+1,j-1})   -2\mathsf{c}(t_{i+1,j})+  \mathsf{c}(t_{i,j+1})\\
& \qquad  \qquad \qquad \qquad  \qquad \qquad \qquad  \qquad \qquad   \text{ for }
1 \le i\le n ,\ n+1-i \le j\le n \}  \\
(\mathsf{B}_n): \ \mathcal{S} & =  \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid
2t_{i,n+1-i} \ge \ldots \ge 2t_{i,n-1} \ge t_{i,n} \ge 2t_{i,n+1} \ge  \ldots  \ge 2t_{i,n-1+i} \\
& \qquad  \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad
\text{ for } 1 \le i\le n \}, \\
\mathcal{S}^\lambda & = \{ \mathbf{a} \in \mathcal{S} \mid \  t_{i,j} \le \lambda_j + \mathsf{c}(t_{i,j+1}) -2\mathsf{c}(t_{i,2n-j})+\mathsf{c}(t_{i,2n+1-j}), \\
& \qquad  \qquad
t_{i,2n-j} \le \lambda_j + \mathsf{c}(t_{i+1,j+1}) -2\mathsf{c}(t_{i+1,j})+ \mathsf{c}(t_{i,2n+1-j}), \\
& \qquad  \qquad
t_{i,n} \le \lambda_n + 2 \mathsf{c}(t_{i,n+1})-2 \mathsf{c}(t_{i+1,n})\ \text{ for }1\le i \le n,\ n+1-i \le j < n  \}  \\
(\mathsf{C}_n):\ \mathcal{S} & = \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid t_{i,n+1-i} \ge \ldots  \ge t_{i,n} \ge  \ldots \ge t_{i,n-1+i} \ \text{ for } 1 \le i \le n \}\\
\mathcal{S}^\lambda & = \{ \mathbf{a} \in \mathcal{S} \mid \  t_{i,j} \le \lambda_j + \mathsf{c}(t_{i,j+1})-2\mathsf{c}(t_{i,2n-j})+\mathsf{c}(t_{i,2n+1-j}), \\
& \qquad \qquad
t_{i,2n-j} \le \lambda_j + \mathsf{c}(t_{i+1,j+1}) -2\mathsf{c}(t_{i+1,j})+ \mathsf{c}(t_{i,2n+1-j}), \\
& \qquad \qquad
t_{i,n} \le \lambda_n + \mathsf{c}(t_{i,n+1})-\mathsf{c}(t_{i+1,n})\ \text{ for } 1 \le i \le n,\ n+1-i \le j < n \}  \allowdisplaybreaks \\
(\mathsf{D}_n):\ \mathcal{S} &= \{ \mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell} \mid t_{i,n-i} \ge \ldots  \ge t_{i,n-2} \ge
  t_{i,n-1}, t_{i,n} \ge t_{i,n+1} \ge  \ldots  \ge t_{i,n-1+i} \\
& \qquad  \qquad  \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad
\text{ for } 1 \le i \le n-1 \}, \\
\mathcal{S}^\lambda & = \{ \mathbf{a} \in \mathcal{S} \mid \  t_{i,j} \le \lambda_j + \mathsf{c}(t_{i,j+1})-2\mathsf{c}(t_{i,2n-1-j})+\mathsf{c}(t_{i,2n-j}), \\
& \quad \quad
t_{i,2n-1-j} \le \lambda_j + \mathsf{c}(t_{i+1,j+1}) -2\mathsf{c}(t_{i+1,j})+ \mathsf{c}(t_{i,2n-j}), \\
& \quad \quad
t_{i,n-1} \le \lambda_{n-1} + \mathsf{c}(t_{i,n+1})-2\tilde{\mathsf{c}}(t_{i+1,n-1}),\\
& \quad \quad
t_{i,n} \le \lambda_n + \mathsf{c}(t_{i,n+1})-2\tilde{\mathsf{c}}(t_{i+1,n})\ \text{ for }1 \le i \le n-1,\ n-i \le j< n-1 \}.
\end{aligned}$$
:::

Let $\mathbf{B}$ be the crystal given by

  ------------------ ---------------
  $(\mathsf{A}_n)$     $\CrystalA$
  $(\mathsf{B}_n)$    $\newcommand$
  $(\mathsf{C}_n)$     $\CrystalC$
  ------------------ ---------------

  -- ----------------
       $\newcommand$
  -- ----------------

with the entries ordered by

$$\begin{aligned}
\ \ \quad(\mathsf{A}_n) \qquad \qquad &   \overline{1} \succ \overline{2} \succ \cdots \succ \overline{n+1} , \\\quad(\mathsf{B}_n)\qquad \qquad & \overline{1} \succ \overline{2} \succ \cdots \succ \overline{n} \succ 0 \succ n \succ \cdots \succ 2 \succ 1,  \\
\ \ \quad(\mathsf{C}_n) \qquad \qquad &  \overline{1} \succ \overline{2} \succ \cdots \succ \overline{n-1} \succ \overline{n} \succ {n} \succ {n-1} \succ \cdots \succ {1} ,
\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad  \\
\ \ \quad(\mathsf{D}_n) \qquad \qquad & \overline{1} \succ \overline{2} \succ \cdots \succ \overline{n-1} \succ    \overline{n}, n
\succ {n-1} \succ \cdots \succ {1} .
\end{aligned}$$ Let $$\begin{aligned}
 \label{Eq: def of overhat i}
\widehat{\imath} =  \left\{
     \begin{array}{ll}
       \overline{\imath} & \hbox{ if } 1 \le i \le n+1\ \  (\mathsf{A}_n),  \ \ 1 \le i \le n\ \ (\mathsf{B}_n,\mathsf{C}_n,\mathsf{D}_n), \\
       0 & \hbox{ if } i=n+1\ \  (\mathsf{B}_n), \\
       2n+1-i & \hbox{ if } n+1 \le i \le 2n\ \  (\mathsf{C}_n, \mathsf{D}_n), \\
       2n+2-i & \hbox{ if } n+2 \le i \le 2n+1\ \ (\mathsf{B}_n).
     \end{array}
   \right.
\end{aligned}$$

For $a,b \in \mathbf{B}$ with $a \succ b$, let $\mathbf{i}(a,b)$ be a sequence of elements in $I$ such that $a =  \tilde{f}_{\mathbf{i}(a,b)}b$, and define the irreducible graded $R$-module $$\begin{aligned}
 \label{Eq: def of nabla}
\Delta_{(a,b)} =  \tilde{f}_{\mathbf{i}(a,b)} \mathbf{1}.
\end{aligned}$$ Note that $\Delta_{(a,b)}$ in general is not a cuspidal representation given in [@HMM09; @KR09].

**Remark. ** *The set of cuspidal representations is in one-to-one correspondence with the set of positive roots, via correspondence given by the weights of the cuspidal representations. But there are some $\Delta(a,b)$'s which do not correspond to positive roots. For example, in type $\mathsf{B}_n$, the module $\Delta_{(\overline{1},1)} \in R(\sum_{i=1}^n 2\alpha_i)\text{-}  \mathsf{fmod}$ is not a cuspidal representation, since $\sum_{i=1}^n 2\alpha_i$ is not a positive root (see Example [\[Ex: example\]](#Ex: example){reference-type="ref" reference="Ex: example"}).*

The action of the KLR algebra can be described explicitly as follows.

If one of the following holds: $a \succ b$  $(\mathsf{A}_n, \mathsf{C}_n)$, either $b \succeq 0$ or $0 \succeq a$  $(\mathsf{B}_n)$, either $b \succ n-1$ or $\overline{n-1} \succ a$  $(\mathsf{D}_n)$, then the module $\Delta_{(a,b)}$ is the 1-dimensional $R$-module $\mathbb{C}v$ specified by $$x_i v = 0 , \quad \tau_j v = 0, \quad e(\mathbf{i}) v = \left\{
                                                            \begin{array}{ll}
                                                              v & \hbox{ if } \mathbf{i} = \mathbf{i}(a,b),  \\
                                                              0 & \hbox{ otherwise.}
                                                            \end{array}
                                                          \right.$$

If $a \succ 0 \succ b$ for type $\mathsf{B}_n$, then $\Delta_{(a,b)}$ is the 2-dimensional $R$-module $\mathbb{C}u \oplus \mathbb{C}v$ with $R$-action $$\begin{aligned}
x_i u &= 0, \qquad
\tau_ju = \left\{
                                \begin{array}{ll}
                                  v & \hbox{ if } j = d, \\
                                  0 & \hbox{ otherwise,}
                                \end{array}
                              \right.
 \qquad e(\mathbf{i})u = \left\{
                           \begin{array}{ll}
                             u & \hbox{ if } \mathbf{i} = \mathbf{i}(a,b), \\
                             0 & \hbox{ otherwise,}
                           \end{array}
                         \right. \\
x_iv &= \left\{
           \begin{array}{ll}
            - u & \hbox{ if } i = d, \\
             u & \hbox{ if } i = d + 1, \\
             0 & \hbox{ otherwise}
           \end{array}
         \right.
\qquad \tau_jv= 0,
 \qquad e(\mathbf{i})v = \left\{
                           \begin{array}{ll}
                             v & \hbox{ if } \mathbf{i} = \mathbf{i}(a,b), \\
                             0 & \hbox{ otherwise,}
                           \end{array}
                         \right.
\end{aligned}$$ where $d$ is an integer such that $\sigma_{d}(\mathbf{i}(a,b)) = \mathbf{i}(a,b)$.

If $a \succeq \overline{n-1}$ and $n-1 \succeq b$ for type $\mathsf{D}_n$, then the module $\Delta_{(a,b)}$ is the 2-dimensional $R$-module $\mathbb{C}u \oplus \mathbb{C}v$ given by $$\begin{aligned}
x_i u &= 0, \quad \tau_j u = \left\{
                              \begin{array}{ll}
                                \mathcal{Q}_{n,n-1}(x_{n},x_{n-1}) v & \hbox{ if } j = d, \\
                                0 & \hbox{ otherwise, }
                              \end{array}
                            \right.
\quad e(\mathbf{i})u = \left\{
                         \begin{array}{ll}
                           u & \hbox{ if } \mathbf{i} = \mathbf{i}(a, {n}) * \mathbf{i}({n}, b), \\
                           0 & \hbox{ otherwise,}
                         \end{array}
                       \right. \\
x_i v &= 0, \quad \tau_j v = \left\{
                              \begin{array}{ll}
                                u & \hbox{ if } j = d, \\
                                0 & \hbox{ otherwise, }
                              \end{array}
                            \right.
\ \ \qquad\quad\qquad\qquad \quad e(\mathbf{i})v = \left\{
                         \begin{array}{ll}
                           v & \hbox{ if } \mathbf{i} = \mathbf{i}(a, \overline{n}) * \mathbf{i}(\overline{n}, b), \\
                           0 & \hbox{ otherwise,}
                         \end{array}
                       \right.
\end{aligned}$$ where $d$ is an integer such that $\sigma_{d}(\mathbf{i}(a, n) * \mathbf{i}(n, b)) = \mathbf{i}(a, \overline{n}) * \mathbf{i}(\overline{n}, b)$. Note that $\mathcal{Q}_{n,n-1}(x_{n},x_{n-1}) = \zeta_{n,n-1} \in \mathbb{C}\setminus\{0 \}.$

It follows from the description above that, for $a,b \in \mathbf{B}$ with $a \succ b$, $$\begin{aligned}
 \label{Eq: cha of nabla}
\mathsf{ ch}\Delta_{(a,b)} = \left\{
                       \begin{array}{ll}
                         \mathbf{i}(a, n) * \mathbf{i}(n, b) + \mathbf{i}(a, \overline{n}) * \mathbf{i}(\overline{n}, b) & \hbox{ if } a \succeq \overline{n-1},\ {n-1} \succeq b\ \ (\mathsf{D}_n), \\
                           2 \mathbf{i}(a,b) & \hbox{ if } a\succ 0 \succ b\ \  (\mathsf{B}_n),\\
                         \mathbf{i}(a,b) & \hbox{ otherwise. }  \\
                       \end{array}
                     \right.
\end{aligned}$$

**Remark. ** *We see from the expression for the character in [\[Eq: cha of nabla\]](#Eq: cha of nabla){reference-type="eqref" reference="Eq: cha of nabla"} that $\Delta_{(a,b)}$ can be identified with the sequence $\mathbf{i}(a,b)$, or equivalently, with the segment of $\mathbf{B}$ between $a$ and $b$, which is another reason why we defined the Kashiwara operators in the opposite manner to [@KP10; @KL09].*

Given $\mathbf{a} \in \mathcal{S}$ (resp. $\mathbf{a} \in \mathcal{S}^\lambda$) and $i=1,\ldots,n$, let $$\begin{aligned}
 \label{Eq: nabla}
\Delta(\mathbf{a};i) = \left\{
                            \begin{array}{ll}
                              \overset{n_i}{\underset{j=n+1-i}{\boxtimes}}  \left(\Delta_{(\widehat{n+1-\imath},\ \widehat{\jmath+1})}^{\boxtimes \vartheta_{ij}}\right) &\ \ \hbox{if } \ \ 1 \le i \le n\ \  (\mathsf{A}_n,\mathsf{B}_n,\mathsf{C}_n), \\
                              \Delta_{(\overline{n-1},\ {n})}^{\boxtimes t_{1,n-1}} &\ \  \hbox{if }\ \  i=1\ \  (\mathsf{D}_n),\\
                              \Delta_{(\overline{n-1},\ \overline{n})}^{\boxtimes t_{1,n}} &\ \  \hbox{if }\ \  i= 2 \ \ (\mathsf{D}_n), \\
                              \overset{n_i}{\underset{j=n+1-i}{\boxtimes}}  \left(\Delta_{(\widehat{n+1-\imath},\ \widehat{\jmath+1})}^{\boxtimes \vartheta_{i-1,j}}\right) &\ \  \hbox{if } \ \ 3 \le i \le n \ (\mathsf{D}_n),
                            \end{array}
                          \right.
\end{aligned}$$ where $n_i= n \ \hbox{\rm for all}\ i\ \ (\mathsf{A}_n)$, $n_i = n+i\ \ (\mathsf{B}_n)$, $n_i = n-1+i\ \ (\mathsf{C}_n, \mathsf{D}_n)$, $\triangle(\mathbf{a}) = \{ t_{i,j} \}$, and

$$\begin{aligned}
 \label{Eq: theta}
\vartheta_{ij} = \left\{
                   \begin{array}{ll}
                     t_{i,j} - t_{i,j+1} & \hbox{if }\ \  j \le n_i \ \ (\mathsf{A}_n,\mathsf{C}_n),\  j \le n-2\ \  (\mathsf{B}_n),\  j \le n-3\ \ (\mathsf{D}_n), \\
                     t_{i,n-1} - \lceil \frac{t_{i,n}}{2} \rceil & \hbox{if } \ \ j=n-1\ \ (\mathsf{B}_n), \\
                     \lceil \frac{t_{i,n}}{2} \rceil - \lfloor \frac{t_{i,n}}{2} \rfloor & \hbox{if }\ \  j=n\ \ (\mathsf{B}_n), \\
                     \lfloor \frac{t_{i,n}}{2} \rfloor - t_{i,n+1} & \hbox{if } \ \ j=n+1\ \  (\mathsf{B}_n), \\
                      t_{i, n-2} -  \mathsf{max}\{ t_{i, n-1}, t_{i,n} \} & \hbox{if } \ \ j=n-2\ \ (\mathsf{D}_n), \\
                      \mathsf{max}\{ 0, t_{i,n}-t_{i,n-1} \} & \hbox{if }\ \  j=n-1\ \ (\mathsf{D}_n), \\
                     \mathsf{max}\{ 0, t_{i,n-1}-t_{i,n} \} & \hbox{if }\ \  j=n\ \ (\mathsf{D}_n), \\
                     \mathsf{min}\{ t_{i, n-1}, t_{i,n} \} - t_{i, n+1} & \hbox{if } \ \ j = n+1\  \ (\mathsf{D}_n), \\
                      t_{i,j-1} - t_{i,j} & \hbox{if } \ \ j \ge n+2\ \ (\mathsf{B}_n, \mathsf{D}_n).
                   \end{array}
                 \right.
\end{aligned}$$

For $v \in B(\infty)$ (resp. $v \in B(\lambda)$), let $\mathbf{a}(v)$ be the adapted string of $v$ with respect to the expression $w_0 = r_{\mathbf{s}_1} \cdots r_{\mathbf{s}_n}$ given in Table $\ref{Tb: w0}$. Now we are ready to state the main theorem in this section.

::: theorem
[]{#Thm: main theorem label="Thm: main theorem"} Let $(\mathfrak{A}, \mathsf{P}, \Pi, \mathsf{P}^{\vee}, \Pi^{\vee})$ be a Cartan datum of finite classical type. For $v\in B(\infty)$ (resp. $v\in B(\lambda)$), let $\mathbf{a}(v)$ be the adapted string of $v$ with respect to the expression $w_0 = r_{\mathbf{s}_1} \cdots r_{\mathbf{s}_n}$ given in Table $\ref{Tb: w0}$ and let $\Delta(\mathbf{a}(v)) = \Delta(\mathbf{a}(v);1) \boxtimes \cdots \boxtimes \Delta(\mathbf{a}(v);n)$. Then

1.  $\mathsf{ hd}\,\mathsf {Ind}\Delta(\mathbf{a}(v) )$ is irreducible.

2.  The map $\Psi: B(\infty) \longrightarrow \mathbb{B}(\infty)$ defined by $$\Psi(v) = \mathsf{ hd}\,\mathsf {Ind}\Delta(\mathbf{a}(v))  \ \ \ \text{ for } v \in B(\infty)$$ is a crystal isomorphism.

3.  The map $\Psi^\lambda: B(\lambda) \longrightarrow \mathbb{B}(\lambda)$ defined by $$\Psi^\lambda(v) = \mathsf{ hd}\,\mathsf {Ind}\Delta(\mathbf{a}(v)) \ \ \ \text{ for } v \in B(\lambda)$$ is a crystal isomorphism.
:::

Theorem [\[Thm: main theorem\]](#Thm: main theorem){reference-type="ref" reference="Thm: main theorem"} and Proposition [\[Prop: S lambda\]](#Prop: S lambda){reference-type="ref" reference="Prop: S lambda"} combine to give the following explicit description of the irreducible graded modules over $R$ and $R^\lambda$.

::: corollary
[]{#Cor: complete lists label="Cor: complete lists"} Let $(\mathfrak{A}, \mathsf{P}, \Pi, \mathsf{P}^{\vee}, \Pi^{\vee})$ be a Cartan datum of finite classical type. Then

1.  the set $$\mathcal{A} = \{ \mathsf{ hd}\mathsf {Ind}\Delta(\mathbf{a}) \mid \mathbf{a} \in \mathcal{S}  \}$$ is the complete list of all irreducible graded $R$-modules up to isomorphism and grading shift.

2.  For $\lambda \in \mathsf{P}^+$, the set $$\mathcal{A}^\lambda = \{ \mathsf{ hd}\,\mathsf {Ind}\Delta(\mathbf{a}) \mid \mathbf{a} \in \mathcal{S}^\lambda   \}$$ is the complete list of all irreducible graded $R^\lambda$-modules up to isomorphism and grading shift.
:::

In the following proposition, we give an upper bound for the number of $\Delta_{(a,b)}$'s that can occur in $\Delta(\mathbf{a}(v))$ for $v\in B(\lambda)$.

::: proposition
[]{#Lem: upper bound label="Lem: upper bound"} For $v \in B(\lambda)$, let $\eta(v)$ be the number of $\Delta_{(a,b)}$'s in the outer tensor product $\Delta(\mathbf{a}(v)) = \Delta(\mathbf{a}(v);1) \boxtimes \cdots
\boxtimes \Delta(\mathbf{a}(v);n)$. Then $\eta(v) \le n
\lambda(h)$, where $$h = \begin{cases} h_1+ \cdots + h_n & \quad  (\mathsf{A}_n), \\
 2h_1+ \cdots + 2h_{n-1} + h_n & \quad  (\mathsf{B}_n), \\
 2(h_1+ \cdots  + h_n) & \quad  (\mathsf{C}_n), \\
 2h_1+ \cdots + 2h_{n-2} + h_{n-1} + h_n & \quad  (\mathsf{D}_n). \end{cases}$$
:::

::: proof
*Proof.* Let $\mathbf{a} = \mathbf{a}(v)$ and write $\mathbf{a} =
\mathbf{a}_1 * \cdots * \mathbf{a}_n$, where $\mathbf{a}_k =
(\mathsf{a}_{k,1}, \mathsf{a}_{k,2}, \ldots, \mathsf{a}_{k,l_{k}})$ is the subsequence of $\mathbf{a}$ defined in $\eqref{Eq: subseq of
a}$. Since $\mathsf{a}_{k,1} = t_{k,n+1-k}$ if $\mathfrak{A}$ is of type $\mathsf{A}_n, \mathsf{B}_n,\mathsf{C}_n$ and $\mathsf{a}_{1,1}
= t_{1,n-1}$, $\mathsf{a}_{2,1} = t_{1,n}$, $\mathsf{a}_{k,1} =
t_{k-1,n+1-k}$ when $n \ge 3$ for type $\mathsf{D}_n$, it follows from $\eqref{Eq: nabla}$ and $\eqref{Eq: theta}$ that $$\eta(v) \le  \mathsf{a}_{1,1} + \cdots + \mathsf{a}_{n-1,1} + \mathsf{a}_{n,1} .$$ Thus, it suffices to show that $$\mathsf{a}_{1,1} + \cdots + \mathsf{a}_{n-1,1} + \mathsf{a}_{n,1} \le n \lambda(h).$$

Let $\lambda = \lambda_1 \Lambda_1 + \cdots + \lambda_n \Lambda_n$. If $n > 1$ for type $\mathsf{A}_n, \mathsf{B}_n,\mathsf{C}_n$ and $n
> 2$ for type $\mathsf{D}_n$, then using the description in Proposition [\[Prop: S lambda\]](#Prop: S lambda){reference-type="ref" reference="Prop: S lambda"}, we will obtain $$\begin{aligned}
  \label{Eq: upper bound for a1}
\mathsf{a}_{n,1} \le \lambda(h)
\end{aligned}$$ from the following inequalities:

$$\begin{aligned}
(\mathsf{A}_n): \  \mathsf{a}_{n,1} = t_{n,1} &\le \lambda_1 + t_{n,2} \le \lambda_1 + \lambda_2 + t_{n,3} \le \cdots \le \lambda_1 + \cdots + \lambda_n = \lambda(h),  \\
(\mathsf{B}_n): \  \mathsf{a}_{n,1} = t_{n,1} &\le \lambda_1 + t_{n,2} + t_{n,2n-2} - 2 t_{n,2n-1} \le \lambda_1 + \lambda_2 + t_{n,3}+ t_{n,2n-3} - t_{n,2n-2} - t_{n,2n-1} \\
& \le \quad   \cdots \quad \le \lambda_1 + \cdots + \lambda_{n-1} + t_{n,n} - t_{n,n+1} - t_{n,2n-1} \\
& \le \lambda_1 + \cdots + \lambda_{n} + t_{n,n+1} - t_{n,2n-1} \le \lambda_1 + \cdots + \lambda_{n} + \lambda_{n-1} + t_{n,n+2} - t_{n,2n-1} \\
& \le \quad  \cdots \quad \le 2\lambda_1 + 2\lambda_2 + \cdots + 2 \lambda_{n-1} + \lambda_n  = \lambda(h), \\
(\mathsf{C}_n): \  \mathsf{a}_{n,1} = t_{n,1} &\le \lambda_1 + t_{n,2} + t_{n,2n-2} - 2 t_{n,2n-1} \le \lambda_1 + \lambda_2 + t_{n,3}+ t_{n,2n-3} - t_{n,2n-2}  - t_{n,2n-1} \\
& \le \quad   \cdots \quad \le \lambda_1 + \cdots + \lambda_{n-1} + 2 t_{n,n}  - t_{n,n+1} - t_{n,2n-1}  \\
& \le \lambda_1 + \cdots + \lambda_{n-1} + 2\lambda_n + t_{n,n+1} - t_{n,2n-1}  \\
& \le \quad  \cdots \quad \le 2\lambda_1 + 2\lambda_2 + \cdots + 2
\lambda_{n-1} + 2\lambda_n  = \lambda(h),  \\
(\mathsf{D}_n): \  \mathsf{a}_{n,1} = t_{n-1,1} &\le \lambda_1 + t_{n-1,2} + t_{n-1,2n-3} - 2 t_{n-1,2n-2} \\
& \le \lambda_1 + \lambda_2 + t_{n-1,3}+ t_{n-1,2n-4} - t_{n-1,2n-3}  - t_{n-1,2n-2} \\
& \le \quad   \cdots \quad \le  \lambda_1 + \cdots + \lambda_{n-2} + t_{n-1,n-1}+ t_{n-1,n} - t_{n-1,n+1}  - t_{n-1,2n-2} \\
& \le  \lambda_1 + \cdots + \lambda_{n} + t_{n-1,n+1}  - t_{n-1,2n-2} \\
& \le \lambda_1 + \cdots + \lambda_{n} + \lambda_{n-2}+ t_{n-1,n+2}  - t_{n-1,2n-2}  \\
& \le \quad  \cdots \quad \le 2\lambda_1 + 2\lambda_2 + \cdots + 2
\lambda_{n-2} + \lambda_{n-1} + \lambda_n  = \lambda(h).
\end{aligned}$$

We proceed by induction on $n$. If $n=2$ for type $\mathsf{A}_n,
\mathsf{B}_n,\mathsf{C}_n$ or $n=3$ for type $\mathsf{D}_n$, then the assertion can be proved in the same manner as above. We assume that $n>2$ for type $\mathsf{A}_n, \mathsf{B}_n,\mathsf{C}_n$ and $n>3$ for type $\mathsf{D}_n$. Let $U_q(\mathfrak{g}_{n-1})$ be the subalgebra of $U_q(\mathfrak{g})$ generated by $e_i,f_i$ ($i \in I\setminus \{ 1 \}$) and $q^{h}\ (h\in \mathsf{P}^\vee)$, and let $\mathfrak{B}$ be the crystal obtained from $B(\lambda)$ by forgetting the $1$-arrows. Note that $U_q(\mathfrak{g}_{n-1})$ is of type $\mathsf{X}_{n-1}$ when $U_q(\mathfrak{g})$ is of type $\mathsf{X}_n$ $(\mathsf{X=A,B,C,D})$. Let $u =
 \tilde{f}_{\mathbf{s}_n}^{\mathsf{a}_n} b_\lambda$ where $\mathbf{s}_n$ is the sequence given in Table [\[Tb: w0\]](#Tb: w0){reference-type="ref" reference="Tb: w0"}, and let $\mathcal{C}$ be the connected component of $\mathfrak{B}$ containing $v$. Then $u$ is the highest weight vector of the $U_q(\mathfrak{g}_{n-1})$-crystal $\mathcal{C}$ with weight $$\mathsf{wt}(u) = \left\{
              \begin{array}{ll}
                \lambda - t_{n,1}\alpha_1 - \cdots - t_{n,n}\alpha_n & \quad (\mathsf{A}_n), \\
                \lambda - (t_{n,1}+t_{n,2n-1})\alpha_1 - \cdots - (t_{n,n-1}+t_{n,n+1})\alpha_{n-1} -  (t_{n,n})\alpha_n & \quad (\mathsf{B}_n, \mathsf{C}_n),\\
                \lambda - (t_{n-1,1}+t_{n-1,2n-2})\alpha_1 - \cdots - (t_{n-1,n-2}+t_{n-1,n+1})\alpha_{n-2} \\
\qquad \qquad \qquad \qquad\qquad \qquad \ \ \  \qquad \qquad -
t_{n-1,n}\alpha_{n-1} - t_{n-1,n-1}\alpha_{n} & \quad
(\mathsf{D}_n).
              \end{array}
            \right.$$

Now suppose that $h' = h-h_1 \ (\mathsf{A}_n)$, and $h' = h-2h_1 \ (\mathsf{B}_n, \mathsf{C}_n,
            \mathsf{D}_n)$. Then we see that $$\begin{aligned}
& \alpha_1(h') = -1,\ \alpha_2(h') = 1, \quad   \alpha_i(h') = 0\ (i=3,\ldots,n) \quad (\mathsf{A}_n), \\
& \alpha_1(h') = -2,\ \alpha_2(h') = 2, \quad \alpha_i(h') = 0\
(i=3,\ldots,n)\quad  (\mathsf{B}_n, \mathsf{C}_n, \mathsf{D}_n).
\end{aligned}$$ Proposition [\[Prop: S lambda\]](#Prop: S lambda){reference-type="ref" reference="Prop: S lambda"} implies $$\begin{aligned}
 \label{Eq:
upper bound for wt u} \mathsf{wt}(u)(h') \le \lambda(h)
\end{aligned}$$ by the following calculations: $$\begin{aligned}
(\mathsf{A}_n): \ \ \mathsf{wt}(u)(h') &= \lambda(h') + t_{n,1} - t_{n,2} \le \lambda(h), \\
(\mathsf{B}_n,\mathsf{C}_n ): \ \ \mathsf{wt}(u)(h') &= \lambda(h') + 2(t_{n,1} + t_{n,2n-1}) - 2(t_{n,2} + t_{n,2n-2}) \\
& = \lambda(h') + 2(t_{n,1} - t_{n,2} -t_{n,2n-2} + 2t_{n,2n-1}) - 2t_{n,2n-1}  \le \lambda(h), \\
(\mathsf{D}_n): \ \
\mathsf{wt}(u)(h') &= \lambda(h') + 2(t_{n,1} + t_{n,2n-2}) - 2(t_{n,2} + t_{n,2n-3}) \\
& = \lambda(h') + 2(t_{n,1} - t_{n,2} -t_{n,2n-3} + 2t_{n,2n-2}) -
2t_{n,2n-2}  \le \lambda(h) .
\end{aligned}$$ Since the adapted string of $u$ is $\mathbf{a}_1*\cdots *
\mathbf{a}_{n-1}$, we obtain by the induction hypothesis that $$\begin{aligned}
\mathsf{a}_{1,1} + \cdots + \mathsf{a}_{n-1,1} \le (n-1) \mathsf{wt}(u)(h'),
\end{aligned}$$ which yields, by $\eqref{Eq: upper bound for a1}$ and $\eqref{Eq:
upper bound for wt u}$, $$\begin{aligned}
\mathsf{a}_{1,1} + \cdots + \mathsf{a}_{n-1,1} + \mathsf{a}_{n,1}
\le (n-1) \lambda(h) + \lambda(h) = n \lambda(h).
\end{aligned}$$ ◻
:::

1em

# Proof of Theorem [\[Thm: main theorem\]](#Thm: main theorem){reference-type="ref" reference="Thm: main theorem"} {#Sec: final}

This section is devoted to a proof of Theorem [\[Thm: main theorem\]](#Thm: main theorem){reference-type="ref" reference="Thm: main theorem"}. We first give a sufficient condition for $\mathsf {Ind}\left( \Delta_{(a,b)} \boxtimes \Delta_{(c,d)}\right ) \simeq \mathsf {Ind}\left( \Delta_{(c,d)} \boxtimes \Delta_{(a,b)}\right)$ to hold (Lemma [\[Lem: commuting lemma\]](#Lem: commuting lemma){reference-type="ref" reference="Lem: commuting lemma"}). Then we extend the result in [@KP10 Lem. 4.3] for type $\mathsf{A}_n$ to the other finite classical types in Lemma [\[Lem: seq of kf\]](#Lem: seq of kf){reference-type="ref" reference="Lem: seq of kf"} below, and prove Lemma [\[Lem: gluing lemma\]](#Lem: gluing lemma){reference-type="ref" reference="Lem: gluing lemma"} which yields $\mathcal{N}_n(v) = \mathsf{ hd}\,\mathsf {Ind}\Delta(\mathbf{a}(v);n)$ for $v \in B(\infty)$. From that we can deduce $\mathcal{N}_k(v) = \mathsf{ hd}\,\mathsf {Ind}\Delta(\mathbf{a}(v);k)$ for all $k$. Using Lemma [\[Lem: sum of fi\]](#Lem: sum of fi){reference-type="ref" reference="Lem: sum of fi"}, Proposition [\[Prop: crystal iso\]](#Prop: crystal iso){reference-type="ref" reference="Prop: crystal iso"}, and Lemma [\[Lem: gluing lemma\]](#Lem: gluing lemma){reference-type="ref" reference="Lem: gluing lemma"}, we argue that the map $\Psi: B(\infty) \longrightarrow \mathbb{B}(\infty)$ is a crystal isomorphism. It then follows from the crystal embedding $\iota_\lambda: B(\lambda) \rightarrow B(\infty)\otimes T_\lambda \otimes C$ in [\[Eq: crystal embedding\]](#Eq: crystal embedding){reference-type="eqref" reference="Eq: crystal embedding"} that the map $\Psi^\lambda: B(\lambda) \longrightarrow \mathbb{B}(\lambda)$ is a crystal isomorphism too.

Given $\mathbf{i} \in I^\alpha$ and $\mathbf{j} \in
I^\beta$, a sequence $\mathbf{k}\in I^{\alpha+\beta}$ is called a *shuffle* of $\mathbf{i}$ and $\mathbf{j}$ if $\mathbf{k}$ is a permutation of $\mathbf{i} * \mathbf{j}$ such that $\mathbf{i}$ and $\mathbf{j}$ are subsequences of $\mathbf{k}$. For $X = \sum x_\mathbf{i}\ \mathbf{i}$ and $Y = \sum
y_\mathbf{j}\ \mathbf{j}$, we define $X \star Y$ by $$X \star Y = \sum_{\mathbf{k}}
x_\mathbf{i} y_\mathbf{j}    \ \mathbf{k},$$ where $\mathbf{k}$ runs over all the shuffles of $\mathbf{i}$ and $\mathbf{j}$. Suppose $M\in R(\alpha)\text{-}\mathsf{fmod}$ and $N \in R(\beta)\text{-}\mathsf{fmod}$, and assume $Q$ is a quotient (resp. $L$ is a submodule) of $\mathsf {Ind}(M \boxtimes N)$. Then $$\begin{aligned}
&\text{$ \mathsf{ ch}\big(\mathsf {Ind}(M \boxtimes N)\big) = \mathsf{ ch}(M) \star \mathsf{ ch}(N),$ } \label{Eq: shuffle 1} \\
& \text{any term of $\mathsf{ ch}Q$ (resp.\ $\mathsf{ ch}L$) is a shuffle of some $\mathbf{i} \in \mathsf{ ch}(M)$ and $\mathbf{j} \in \mathsf{ ch}(N)$.} \label{Eq: shuffle 2}
\end{aligned}$$ The quantum Serre relations $\eqref{Eq: Serre}$ imply that $$\begin{aligned}
& \mathsf{dim}(e(\ldots, i,j,\ldots) M) =   \mathsf{dim}(e(\ldots,j,i, \ldots) M) \qquad  \hspace{2.1truecm}  \text{ if } {a}_{ij} = 0, \label{Eq: Serre1}  \\
&  2 \mathsf{dim}(e(\ldots, i,j,i,\ldots) M)  \label{Eq: Serre2}  \\
& \ \ \ \  = \mathsf{dim}(e(\ldots,  i,i,j,\ldots) M)  + \mathsf{dim}(e(\ldots, j,i,i,\ldots) M) \qquad \ \  \ \text{ if } {a}_{ij} = -1,
\nonumber  \\
&\mathsf{dim}(e(\ldots,  i,i,i,j,\ldots) M)  + 3 \mathsf{dim}(e(\ldots, i,j,i,i,\ldots) M) \label{Eq: Serre3}  \\
& \ \   \ \   = \mathsf{dim}(e(\ldots, j,i,i,i,\ldots) M) + 3 \mathsf{dim}(e(\ldots, i,i,j,i,\ldots) M)  \ \, \ \text{ if } {a}_{ij} = -2,  \nonumber
\end{aligned}$$ for $M \in R\text{-}\mathsf{fmod}$.

Using the description of $\Delta_{(a,b)}$ in Section [\[Sec: construction for classical type\]](#Sec: construction for classical type){reference-type="ref" reference="Sec: construction for classical type"}, we obtain a surjective homomorphism $$\begin{aligned}
 \label{Eq: surj between nablas}
\mathsf {Ind}\left (\Delta_{(a,b)} \boxtimes \Delta_{(b,c)}\right) \twoheadrightarrow \Delta_{(a,c)}
\end{aligned}$$ for $a,b,c \in \mathbf{B}$ with $a \succ b \succ c$.

::: lemma
[]{#Lem: commuting lemma label="Lem: commuting lemma"} Let $a, b, c, d \in \mathbf{B}$ with $a \succeq c  \succ d \succeq b$. Suppose that one of the following conditions hold:

1.  $\mathfrak{A}$ is of type $\mathsf{A}_n$,

2.  $\mathfrak{A}$ is of type $\mathsf{B}_n$ and one of the following three holds:

    1.  $0 \succeq a$ and $c \ne 0$,

    2.  $b \succeq 0$ and $d \ne 0$,

    3.  $a \succeq \overline{n}$, ${n}\succeq b$ and either $c=0$ or $d=0$,

3.  $\mathfrak{A}$ is of type $\mathsf{C}_n$ and one of the following three holds:

    1.  $b \succeq \overline{n}$,

    2.  $a=c= \overline{n}$,

    3.  $a=\overline{1}$ and $c= \overline{n}$,

4.  $\mathfrak{A}$ is of type $\mathsf{D}_n$ and one of the following three holds:

    1.  $b \succeq \overline{n-1}$,

    2.  $a=c= \overline{n-1}$,

    3.  $a=\overline{1}$ and $c= \overline{n-1}$.

Then $$\mathsf {Ind}\left(\Delta_{(a, b)} \boxtimes \Delta_{(c,d)}\right) \simeq \mathsf {Ind}\left(\Delta_{(c, d)} \boxtimes \Delta_{(a,b)}\right)$$ and these modules are irreducible.
:::

::: proof
*Proof.* Let $$M =  \mathsf {Ind}\left( \Delta_{(a, b)} \boxtimes \Delta_{(c,d)}\right), \quad N = \mathsf {Ind}\left( \Delta_{(c, d)} \boxtimes \Delta_{(a,b)}\right),$$ and let $Q$ (resp. $L$) be any nonzero quotient (resp. submodule) of $M$. We will assume that $\mathbf{k}$ is a certain sequence of elements in $I$ such that $\mathbf{k} \in \mathsf{ ch}M$, $\mathbf{k} \in \mathsf{ ch}Q$, and $\mathbf{k} \in \mathsf{ ch}L$. Let $\xi_M$ (resp. $\xi_Q$, $\xi_L$) be the multiplicity of $\mathbf{k}$ in $\mathsf{ ch}M$ (resp. $\mathsf{ ch}Q$, $\mathsf{ ch}L$). If we can show that $\xi_M = \xi_Q = \xi_L$, we can conclude that $M$ is irreducible and $M \simeq N$, since $\mathsf{ ch}M = \mathsf{ ch}N$.

For type $\mathsf{A}_n$, the assertion follows from [@KP10 Lem. 4.1]. We assume that $\mathfrak{A}$ is of type $\mathsf{B}_n$. If either (i) or (ii) holds, the proof is identical to that for type $\mathsf{A}_n$. So suppose that (iii) holds. Without loss of generality, we may assume that $d=0$. Write $\mathbf{i} = \mathbf{i}(a,b) = (i,\ldots, n,n,\ldots, j)$, $\mathbf{j} = \mathbf{i}(c,d) = (p,p+1,\ldots, n-1, n)$, and let $$\mathbf{k} = (i,\ldots, p,p,p+1,p+1, \ldots, n-1,n-1,n,n,n,n-1,n-2, \ldots, j).$$ Note that $\mathbf{k}$ is a shuffle of $\mathbf{i}$ and $\mathbf{j}$. Let $l$ be the length of $\mathbf{j}$. It follows from $\eqref{Eq: cha of nabla}$ and $\eqref{Eq: shuffle 1}$ that the term $\mathbf{k}$ appears in $\mathsf{ ch}M$ with multiplicity $\xi_M  = 2 \times 2^{l-1} 3$.

By Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"} and $\eqref{Eq: cha of nabla}$, $\mathbf{i} * \mathbf{j}$ appears in the character $\mathsf{ ch}Q$ of any quotient module $Q \subseteq M$. We claim that $\mathbf{k}$ also appears in $\mathsf{ ch}Q$. Note that $a_{n, n-1}=-2$ for type $\mathsf{B}_n$.

We first assume that $p \ne n-1,n.$ By the quantum Serre relations $\eqref{Eq: Serre}$, if $j > p+1$, then $$\begin{aligned}
\mathbf{i} * \mathbf{j} =& (i,\ldots, n,n,\ldots, j, p,p+1, \ldots, n) \in \mathsf{ ch}Q , \\
\buildrel { (4.3)} \over  \Rightarrow&\ (i,\ldots,p, p+1, p, \ldots, n,n,\ldots, j, p+1, \ldots, n) \in \mathsf{ ch}Q, \\
\buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\ (i,\ldots,p, p, p+1, \ldots, n,n,\ldots, j, p+1, \ldots, n) \in \mathsf{ ch}Q.
\end{aligned}$$ If $j = p+1$, then $$\begin{aligned}
\mathbf{i} * \mathbf{j} =& (i,\ldots, n,n,\ldots, p+1, p,p+1, \ldots, n) \in \mathsf{ ch}Q , \\
\buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\ (i,\ldots, n,n,\ldots, p, p+1,p+1, \ldots, n) \in \mathsf{ ch}Q, \\
\buildrel { (4.3)} \over  \Rightarrow&\ (i,\ldots, p, p+1,p,\ldots,  n,n,\ldots, p+1,p+1, \ldots, n) \in \mathsf{ ch}Q,\\
\buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\ (i,\ldots, p, p,p+1, \ldots, n,n,\ldots, p+1,p+1, \ldots, n) \in \mathsf{ ch}Q.
\end{aligned}$$ If $j = p$, then $$\begin{aligned}
\mathbf{i} * \mathbf{j} =& (i,\ldots, n,n,\ldots, p+1, p, p,p+1 \ldots, n) \in \mathsf{ ch}Q , \\
\buildrel { (4.4)} \over  \Rightarrow&\ (i,\ldots, n,n,\ldots, p, p+1,p, p+1, \ldots, n) \in \mathsf{ ch}Q, \\
\buildrel { (4.3)} \over  \Rightarrow&\ (i,\ldots, p, p+1,p, \ldots, n,n,\ldots, p,p+1, \ldots, n) \in \mathsf{ ch}Q, \allowdisplaybreaks  \\
\buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\ (i,\ldots, p, p,p+1, \ldots, n,n,\ldots, p,p+1, \ldots, n) \in \mathsf{ ch}Q.
\end{aligned}$$ If $j < p$, then $$\begin{aligned}
\mathbf{i} * \mathbf{j} =& (i,\ldots, n,n,\ldots, j, p,p+1 \ldots, n) \in \mathsf{ ch}Q , \\
\buildrel { (4.4)} \over  \Rightarrow&\ (i,\ldots, n,n,\ldots, p+1, p,p-1, p, \ldots,j,p+1,\ldots, n) \in \mathsf{ ch}Q, \\
\buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\ (i,\ldots, n,n,\ldots, p+1, p,p, p-1, \ldots,j,p+1,\ldots, n) \in \mathsf{ ch}Q, \\
\buildrel { (4.4)} \over  \Rightarrow&\ (i,\ldots,  n,n,\ldots, p,p+1,p,p-1, \ldots,j,p+1,\ldots, n) \in \mathsf{ ch}Q,\\
\buildrel { (4.3)} \over  \Rightarrow&\ (i,\ldots, p, p+1,p, \ldots, n,n,\ldots, ,j,p+1,\ldots, n) \in \mathsf{ ch}Q,\\
\buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\ (i,\ldots, p, p,p+1, \ldots, n,n,\ldots, ,j,p+1,\ldots, n) \in \mathsf{ ch}Q.
\end{aligned}$$ Applying this argument repeatedly, we determine that $$\begin{aligned}
& \hspace{-.8truecm} (i,\ldots, p, p, \ldots,n-2,n-2, n-1, n,n, \ldots  ,j, n-1, n) \in \mathsf{ ch}Q \\
& \buildrel { \hspace{-.5truecm}(4.2),(4.3),(4.4)} \over  \Longrightarrow(i,\ldots, p, p, \ldots,n-1, n,n,n-1,n-1, \ldots  ,j,  n) \in \mathsf{ ch}Q,  \\
& \buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow\   (i,\ldots, p, p, \ldots,n-1, n,n-1,n,n-1, \ldots  ,j,  n) \in \mathsf{ ch}Q  \\
&\buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow(i,\ldots, p, p, \ldots,n-1, n-1,n,n,n-1, \ldots  ,j,  n) \in \mathsf{ ch}Q, \allowdisplaybreaks \\
& \buildrel { (4.3)} \over  \Rightarrow\  (i,\ldots, p, p, \ldots,n-1, n-1,n,n,n-1,  n, \ldots  ,j) \in \mathsf{ ch}Q, \\
&  \buildrel {\hspace{-.3truecm}(4.2),(4.5)} \over  \Longrightarrow\  \mathbf{k} = (i,\ldots, p, p, \ldots,n-1, n-1,n,n,n,n-1, \ldots  ,j) \in \mathsf{ ch}Q.
\end{aligned}$$ We suppose that $p = n-1,n$. Then, the same argument as above gives $$\mathbf{k} = (i,\ldots, n-1, n-1,n,n,n,n-1, \ldots  ,j) \in \mathsf{ ch}Q.$$

Now for any nonzero submodule $L$ of $M$, $\mathsf{ ch}L$ contains $\mathbf{j}*\mathbf{i}$ by Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"} and $\eqref{Eq: cha of nabla}$. If $a = c$, then $$\begin{aligned}
 & \mathbf{j} * \mathbf{i}  = (i,i+1, \ldots, n, i,\ldots, n,n,\ldots, j) \in \mathsf{ ch}L , \\
& \quad \  \buildrel { (4.3)} \over  \Rightarrow\ (i,i+1, i,  \ldots, n, i+1,\ldots, n,n,\ldots, j) \in \mathsf{ ch}L,  \\
& \ \  \buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow\ (i,i, i+1 ,  \ldots, n, i+1,\ldots, n,n,\ldots, j) \in \mathsf{ ch}L,   \\
 &\hspace{4.5truecm}  \vdots \\
& \ \  \buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow\ (i,i, i+1 , i+1,  \ldots, n-2,n-2, n-1, n, n-1,n,n,\ldots, j) \in \mathsf{ ch}L,    \\
& \ \  \buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow\ \mathbf{k} = (i,i, i+1 , i+1,  \ldots, n-2,n-2, n-1, n-1, n,n,n,\ldots, j) \in \mathsf{ ch}L. \allowdisplaybreaks
\end{aligned}$$ If $a \succ c$, then $$\begin{aligned}
& \mathbf{j} * \mathbf{i}  = (p, \ldots, n-1, n, i,\ldots, n,n,\ldots, j) \in \mathsf{ ch}L ,   \\
& \quad \buildrel { (4.3)} \over  \Rightarrow\ (p,  \ldots, n-1, i,\ldots, n, n-1, n,n,\ldots, j) \in \mathsf{ ch}L,  \\
& \  \buildrel {\hspace{-.3truecm}(4.2),(4.5)} \over  \Longrightarrow\ (p,  \ldots, n-1, i,\ldots, n-1, n, n,n,\ldots, j) \in \mathsf{ ch}L, \\
&\hspace{4.5truecm}  \vdots \\
& \  \buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow\ \mathbf{k} = (i,\ldots, p , p,p+1 , p+1,  \ldots, n-1,
n-1, n,n,n,\ldots, j) \in \mathsf{ ch}L. 
\end{aligned}$$ Hence, $\mathsf{ ch}L$ contains $\mathbf{k}$ in either event. From the structure of $\mathbf{k}$ we see that it occurs in $\mathsf{ ch}Q$ (resp. $\mathsf{ ch}L$) with multiplicity $\xi_Q \ge 2^{l-1} 3!$ (resp. $\xi_L \ge 2^{l-1} 3!$). Therefore, since $\xi_M =  2 \times 2^{l-1} 3$, we have $\xi_M =
\xi_Q = \xi_L$, which implies the result for type $\mathsf{B}_n$.

Now assume that $\mathfrak{A}$ is of type $\mathsf{C}_n$. If either (i) or (ii) holds, the proof is identical to that for type $\mathsf{A}_n$. We assume that (iii) holds. Write $\mathbf{i} = \mathbf{i}(a,b) = (1,2,\ldots,n,\ldots, j)$, $\mathbf{j} = \mathbf{i}(c,d) = (n,n-1,\ldots, q)$. Then $$\mathbf{k} := (1,2, \ldots, n-1, n,n,n-1,n-1, \ldots, q,q,\ldots, j).$$ is a shuffle of $\mathbf{i}$ and $\mathbf{j}$. Let $l$ be the length of $\mathbf{j}$. Then $\eqref{Eq: cha of nabla}$ and $\eqref{Eq: shuffle 1}$ imply that the term $\mathbf{k}$ appears in $\mathsf{ ch}M$ with multiplicity $\xi_M = 2^l$.

For any nonzero quotient $Q$ of $M$, $\mathsf{ ch}Q$ contains $\mathbf{i}*\mathbf{j}$ by $\eqref{Eq: cha of nabla}$ and Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"}. We claim that $\mathbf{k}$ occurs in $\mathsf{ ch}Q$ as a term. Note that $a_{n-1, n}=-2$. The quantum Serre relations $\eqref{Eq: Serre}$ and $\eqref{Eq: shuffle 2}$ imply $$\begin{aligned}
\mathbf{i}*\mathbf{j}\ = & \ \  (1,\ldots,n,\ldots,j,n,\ldots,q) \in \mathsf{ ch}Q,  \\
  \buildrel { (4.3)} \over  \Rightarrow&\  \ (1,\ldots,n-1,n,n-1,n,\ldots,j,n-1,\ldots, q) \in \mathsf{ ch}Q, \\
 \buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\  \ (1,\ldots,n-1,n,n,n-1,\ldots,j,n-1,\ldots, q) \in \mathsf{ ch}Q.
\end{aligned}$$ Continuing this reasoning gives $$\mathbf{k} = (1, \ldots, n,n, \ldots, q,q,\ldots, j) \in \mathsf{ ch}Q.$$

For any nonzero submodule $L$ of $M$, $\mathsf{ ch}L$ contains $\mathbf{j}*\mathbf{i}$ by Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"} and $\eqref{Eq: cha of nabla}$.

Then, using a similar argument, we have $$\begin{aligned}
\mathbf{j}*\mathbf{i}\ = & \ \  (n,\ldots,q,1,2,\ldots,n,\ldots,j) \in \mathsf{ ch}L, \\
\buildrel { \hspace{-.5truecm}(4.2),(4.3),(4.4)} \over  \Longrightarrow&(n,n-1,1,\ldots, n-1,n,n-1,\ldots,q,q,\ldots, j) \in \mathsf{ ch}L,   \\
\buildrel { \hspace{-.5truecm}(4.2),(4.3),(4.4)} \over  \Longrightarrow&(n,1,\ldots,n-2,n-1, n-1,n,n-1,\ldots,q,q,\ldots, j) \in \mathsf{ ch}L,  \allowdisplaybreaks\\
\buildrel {\hspace{-.3truecm}(4.2),(4.5)} \over  \Longrightarrow&\ (n,1,\ldots,n-2,n-1, n,n-1,n-1,\ldots,q,q,\ldots, j) \in \mathsf{ ch}L, \\
\buildrel { (4.3)} \over  \Rightarrow&\ (1,\ldots,n,n-1, n,n-1,n-1,\ldots,q,q,\ldots, j) \in \mathsf{ ch}L,  \\
\buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\ \mathbf{k} = (1,\ldots,n, n,\ldots,q,q,\ldots, j) \in \mathsf{ ch}L.
\end{aligned}$$ As $\mathbf{k}$ occurs in $\mathsf{ ch}Q$ (resp. $\mathsf{ ch}L$) with multiplicity $\xi_Q \ge 2^l$ (resp. $\xi_L \ge 2^l$), and since $\xi_M= 2^l$, the assertion follows from $\xi_M = \xi_Q = \xi_L$.

Lastly, we assume that $\mathfrak{A}$ is of type $\mathsf{D}_n$. If (i) holds, then the proof is identical to that for type $\mathsf{A}_n$.

Suppose that (ii) holds. Write $\mathbf{i} = \mathbf{i}(a,b) = (n,n-1,n-2, \ldots, j)$, $\mathbf{j} = \mathbf{i}(c,d) = (n,n-1,n-2,\ldots, q)$. Then $$\mathbf{k} := (n,n,n-1,n-1,n-2,n-2, \ldots, q,q, \ldots, j).$$ is a shuffle of $\mathbf{i}$ and $\mathbf{j}$. Let $l$ be the length of $\mathbf{j}$. The equations $\eqref{Eq: cha of nabla}$ and $\eqref{Eq: shuffle 1}$ imply that the term $\mathbf{k}$ appears in $\mathsf{ ch}M$ with multiplicity $\xi_M = 2^l$.

By Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"} and $\eqref{Eq: cha of nabla}$, $\mathbf{i} * \mathbf{j}$ appears in the character $\mathsf{ ch}Q$ of any quotient module $Q \subseteq M$. We will show that $\mathbf{k}$ also appears in $\mathsf{ ch}Q$. Note that $a_{n, n-2}= a_{n-2, n} = a_{n-1, n-2} = a_{n-2, n-1} = -1$ and $a_{n-1,n} = a_{n,n-1} = 0$. The quantum Serre relations $\eqref{Eq: Serre}$ imply $$\begin{aligned}
\mathbf{i}*\mathbf{j}\ = & \ \  (n,n-1,n-2\ldots,j,n,n-1,n-2,\ldots,q) \in \mathsf{ ch}Q,  \\
  \buildrel { (4.3)} \over  \Rightarrow&\  \ (n-1,n,n-2, n,\ldots,j, n-1,n-2,\ldots,q) \in \mathsf{ ch}Q, \\
   \buildrel { \hspace{-.5truecm}(4.2),(4.3),(4.4)} \over  \Longrightarrow&\  \ (n,n,n-1, n-2,\ldots,j, n-1,n-2,\ldots,q) \in \mathsf{ ch}Q, \\
  \buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\  \ (n,n,n-1, n-2,n-1\ldots,j, n-2,\ldots,q) \in \mathsf{ ch}Q, \\
    \buildrel {\hspace{-.3truecm}(4.2),(4.5)} \over  \Longrightarrow&\  \ (n,n,n-1, n-1,n-2\ldots,j, n-2,\ldots,q) \in \mathsf{ ch}Q.
\end{aligned}$$ Continuing this reasoning gives $$\mathbf{k} = (n,n,n-1,n-1,n-2,n-2, \ldots, q,q, \ldots, j) \in \mathsf{ ch}Q.$$ For any nonzero submodule $L$, since $\mathsf{ ch}L$ contains $\mathbf{j} * \mathbf{i}$ by Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"}, the same argument shows that $\mathsf{ ch}L$ contains $\mathbf{k}$. Since $\mathbf{k}$ occurs in $\mathsf{ ch}Q$ (resp. $\mathsf{ ch}L$) with multiplicity $\xi_Q \ge 2^l$ (resp. $\xi_L \ge 2^l$), the assertion follows from $\xi_M = \xi_Q = \xi_L$.

We now assume that (iii) holds. Since the proof is identical to that for type $\mathsf{A}_n$ if $b=\overline{n}$ or $b=n$, we may assume that $n-1 \succeq b$. Write $\mathbf{i} = \mathbf{i}(a,b) = (1, \ldots, n-2,n,n-1,n-2, \ldots, j)$, $\mathbf{j} = \mathbf{i}(c,d) = (n,n-1,n-2,\ldots, q)$ and $$\mathbf{k} := (1, \ldots, n-2, n,n,n-1,n-1,n-2,n-2, \ldots, q,q, \ldots, j).$$ Let $l$ be the length of $\mathbf{j}$. Then $\mathbf{k}$ is a shuffle of $\mathbf{i}$ and $\mathbf{j}$ and appears in $\mathsf{ ch}M$ with multiplicity $\xi_M = 2^l$.

For any nonzero quotient $Q$ of $M$, $\mathsf{ ch}Q$ contains $\mathbf{i}*\mathbf{j}$ by $\eqref{Eq: cha of nabla}$ and Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"}. Using the same argument as in case (ii), we obtain $$\mathbf{k} = (1, \ldots, n-2,n,n,n-1, n-1,n-2\ldots,j, n-2,\ldots,q) \in \mathsf{ ch}Q.$$

For any nonzero submodule $L$ of $M$, $\mathsf{ ch}L$ contains $\mathbf{j}*\mathbf{i}$ by Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"} and $\eqref{Eq: cha of nabla}$. By the same argument as in the $\mathsf{C}_n$ case, we have

$$\begin{aligned}
\mathbf{j}*\mathbf{i}\ = & \ \  (n,\ldots,q-1,q, 1, \ldots, n-2, n,n-1,n-2\ldots,j) \in \mathsf{ ch}L,   \\
     \buildrel { \hspace{-.5truecm}(4.2),(4.3),(4.4)} \over  \Longrightarrow&\  (n,n-1,n-2,1,\ldots, n-2,n,n-1,n-2,\ldots,q,q,\ldots, j)   \in \mathsf{ ch}L, \\
     \buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\  (n,n-1,1,\ldots,n-2,n-2,n,n-1,n-2,\ldots,q,q,\ldots, j)   \in \mathsf{ ch}L, \\
     \buildrel { (4.4)} \over  \Rightarrow&\   (n,n-1,1,\ldots,n-2,n,n-2, n-1,n-2,\ldots,q,q,\ldots, j) \in \mathsf{ ch}L, \\
     \buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\   (n,n-1,1,\ldots,n-2,n,n-1,n-2, n-2,\ldots,q,q,\ldots, j) \in \mathsf{ ch}L, \\
     \buildrel { (4.3)} \over  \Rightarrow&\   (n,1,\ldots,n-1,n-2,n-1,n,n-2, n-2,\ldots,q,q,\ldots, j) \in \mathsf{ ch}L, \\
     \buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\   (n,1,\ldots,n-2,n,n-1,n-1,n-2, n-2,\ldots,q,q,\ldots, j) \in \mathsf{ ch}L, \\
     \buildrel { (4.3)} \over  \Rightarrow&\  (1,\ldots,n,n-2,n,n-1,n-1,n-2, n-2,\ldots,q,q,\ldots, j) \in \mathsf{ ch}L, \\
     \buildrel {\hspace{-.3truecm} (4.2),(4.4)} \over  \Longrightarrow&\  \mathbf{k} = (1,\ldots,n-2,n,n,n-1,n-1,n-2, n-2,\ldots,q,q,\ldots, j) \in \mathsf{ ch}L. \\
\end{aligned}$$

Since the sequence $\mathbf{k}$ occurs in $\mathsf{ ch}Q$ (resp. $\mathsf{ ch}L$) with multiplicity $\xi_Q \ge 2^l$ (resp. $\xi_L
\ge 2^l$), by $\xi_M = 2^l$, the assertion follows from $\xi_M = \xi_Q = \xi_L$. ◻
:::

For $a,b \in \mathbf{B}$, we define $$\label{eq:delta} \delta(a\succeq b) = \left\{
                   \begin{array}{ll}
                     1 & \hbox{if } a \succeq b, \\
                     0 & \hbox{otherwise}.
                   \end{array}
                 \right.$$ In the $\mathsf{A}_n$ case, it follows from [@KP10 Lem. 4.3] that, for $d_k \in \mathbb{Z}_{\ge0}$ and $b_k \in \mathbf{B}$ with $b_1 \succ b_2 \succ \cdots \succ b_m$, $$\begin{aligned}
 \label{Eq: seq of kf for An}
 \tilde{f}_1^{t_1}  \tilde{f}_2^{t_2} \cdots  \tilde{f}_n^{t_n} \mathbf{1} \simeq \mathsf {Ind}\Big(\overset{m}{\underset{k=1}{\boxtimes}}  \Delta_{(\overline{1},b_k)}^{\boxtimes d_k}\Big),
\end{aligned}$$ where $t_i = \sum_{j=1}^m d_j \delta(\overline{\imath} \succ b_j)$ for $i=1,\ldots, n$. Next we will extend this result to the other finite classical types. We first divide the crystal $\mathbf{B}$ for types $\mathsf{B}_n, \mathsf{C}_n, \mathsf{D}_n$ into two pieces so that each part is almost the same as the crystal or the dual of the crystal for type $\mathsf{A}$. For type $\mathsf{B}_n$ (resp. $\mathsf{C}_n$, $\mathsf{D}_n$), the crystal $\mathbf{B}$ is cut at the element $0$ (resp. $\overline{n}$, $\overline{n-1}$). In the next result we give an analogue of $\eqref{Eq: seq of kf for An}$ for each part.

::: lemma
[]{#Lem: seq of kf label="Lem: seq of kf"} Let $b_k \in \mathbf{B}$, and $d_k \in \mathbb{Z}_{\ge 0}$ for $k=1, \ldots, m$. Set $$b_{\bullet} = \left\{
                   \begin{array}{ll}
                     \overline{n+1} & \qquad  (\mathsf{A}_n), \\
                     0 & \qquad (\mathsf{B}_n),\\
                     \overline{n} & \qquad (\mathsf{C}_n),\\
                     \overline{n-1} & \qquad (\mathsf{D}_n).
                   \end{array}
                 \right.$$

1.  If $b_1 \succ b_2 \succ \cdots \succ b_m \succeq b_{\bullet}$, then $$\tilde{f}_1^{t_1}  \tilde{f}_2^{t_2} \cdots  \tilde{f}_l^{t_l} \mathbf{1} \simeq \mathsf {Ind}\Big(\overset{m}{\underset{k=1}{\boxtimes}}  \Delta_{(\overline{1},b_k)}^{\boxtimes d_k}\Big) ,$$ where $l = n\  \ (\mathsf{A}_n, \mathsf{B}_n)$,  $l = n-1\ \ (\mathsf{C}_n)$,  $l = n-2\ \ (\mathsf{D}_n)$ and $t_i := \sum_{j=1}^m d_j \delta(\overline{\imath} \succ b_j)$ for $i=1,\ldots, l$.

2.  Let $$t_i = \left\{
               \begin{array}{ll}
                 \sum_{j=1}^m d_j \delta({i} \succeq b_j) & \hbox{ if } \  i=1,\ldots,n \ (\mathsf{B}_n, \mathsf{C}_n) ,\ \ i=1,\ldots,n-2\ (\mathsf{D}_n),\\
                 \sum_{j=1}^m d_j \delta(\overline{n} \succeq b_j) & \hbox{ if } \   i=n-1\ (\mathsf{D}_n),\\
                 \sum_{j=1}^m d_j \delta({n} \succeq b_j) & \hbox{ if }\  i=n\ (\mathsf{D}_n).
               \end{array}
             \right.$$ Then we have

    1.  if $b_{\bullet} \succ b_1 \succ b_2 \succ \cdots \succ b_m$ for type $\mathsf{B}_n$, then $$\tilde{f}_n^{s+t_n}  \tilde{f}_{n-1}^{t_{n-1}} \cdots  \tilde{f}_1^{t_1} \mathbf{1} \simeq \mathsf{ hd}\,\mathsf {Ind}\left( L(n^s) \boxtimes  \Big( \overset{m}{\underset{k=1}{\boxtimes}}  \Delta_{(b_{\bullet},b_k)}^{\boxtimes d_k}\Big)\right)
        \ \ \text{ for all } s \in \mathbb{Z}_{\ge0},$$ and the head occurs with multiplicity one as a composition factor of $$\mathsf {Ind}\left( L(n^s) \boxtimes  \Big( \overset{m}{\underset{k=1}{\boxtimes}}  \Delta_{(b_{\bullet},b_k)}^{\boxtimes d_k}\Big)\right),$$

    2.  if $b_{\bullet} \succ  b_m \succ b_{m-1} \succ \cdots \succ b_1$ for type $\mathsf{C}_n, \mathsf{D}_n$, then $$\tilde{f}_n^{t_n} \cdots  \tilde{f}_2^{t_2}  \tilde{f}_{1}^{t_{1}} \mathbf{1} \simeq \mathsf {Ind}\Big(\overset{m}{\underset{k=1}{\boxtimes}}  \Delta_{(b_{\bullet}, b_k)}^{\boxtimes d_k}\Big).$$
:::

::: proof
*Proof.* For $k_1, \ldots, k_n \in \mathbb{Z}_{\ge 0}$, it follows from Lemma [\[Lem: sum of fi\]](#Lem: sum of fi){reference-type="ref" reference="Lem: sum of fi"} that $$\begin{aligned}
 \tilde{f}_1^{k_1}  \tilde{f}_2^{k_2} \cdots  \tilde{f}_n^{k_n} \mathbf{1} &\simeq \mathsf{ hd}\,\mathsf {Ind}\left(L(1^{k_1}) \boxtimes \cdots \boxtimes L(n^{k_n})\right), \label{Eq: simple head 1} \\
 \tilde{f}_n^{k_n}  \tilde{f}_{n-1}^{k_{n-1}} \cdots   \tilde{f}_{1}^{k_{1}} \mathbf{1} &\simeq \mathsf{ hd}\,\mathsf {Ind}\left(L(n^{k_n}) \boxtimes \cdots \boxtimes  L(1^{k_1})\right). \label{Eq: simple head 2}
\end{aligned}$$

\(1\) When $\mathfrak{A}$ is of type $\mathsf{A}_n, \mathsf{C}_n, \mathsf{D}_n$, this can be shown in the same way as for [@KP10 Lem. 4.3].

Suppose that $\mathfrak{A}$ is of type $\mathsf{B}_n$. Note that $\Delta_{(\overline{1},b_k)}$ is one of the cuspidal representations given in [@HMM09 Sec. 6.2] and [@KR09 Sec. 8.5]. By [@KR09 Lem. 6.6], we have $N_k := \mathsf {Ind}\Delta_{(\overline{1},b_k)}^{\boxtimes d_k}$ is irreducible for $k=1, \ldots, m$. We write $\mathbf{i}(\overline{1}, b_k) = (1,2,\ldots, l_k)$ and let $$\mathbf{k}_k = (\underbrace{1,\ldots,1}_{d_k}, \underbrace{2,\ldots,2}_{d_k}, \ldots, \underbrace{l_k,\ldots,l_k}_{d_k} )$$ for $k=1,\ldots,m$. Then $\mathbf{k}_k$ appears in $\mathsf{ ch}N_k$ with multiplicity $(d_k!)^{l_k}$. Since $b_1 \succ b_2 \succ \cdots \succ
b_m$, the sequence $\mathbf{k} = \mathbf{k}_m * \cdots *
\mathbf{k}_1$ appears in $\mathsf{ ch}(\mathsf {Ind}(N_m\boxtimes \cdots \boxtimes
N_1))$ with multiplicity $(d_m!)^{l_m} \cdots (d_1!)^{l_1}$. Lemma [\[Lem: irr of induced module\]](#Lem: irr of induced module){reference-type="ref" reference="Lem: irr of induced module"} and Lemma [\[Lem: commuting
lemma\]](#Lem: commuting
lemma){reference-type="ref" reference="Lem: commuting
lemma"} imply that $\mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k \Big)
\simeq \mathsf {Ind}(N_m\boxtimes \cdots \boxtimes N_1)$ is irreducible.

Now for $\mathbf{t} := (\underbrace{1,\ldots,1}_{t_1},\underbrace{2,\ldots,2}_{t_2},\ldots, \underbrace{n,\ldots,n}_{t_n} )$, we have $e(\mathbf{t} )  \left( \mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k \Big) \right) \ne 0$. Since $\mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k \Big)$ is irreducible, it follows from Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"} that there is a surjective homomorphism $$\mathsf {Ind}(L(1^{t_1}) \boxtimes \cdots \boxtimes L(n^{t_n}))\twoheadrightarrow
\mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k \Big).$$ Therefore, $\tilde{f}_1^{t_1} \cdots  \tilde{f}_n^{t_n} \mathbf{1} \simeq \mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k \Big)$ by [\[Eq: simple head 1\]](#Eq: simple head 1){reference-type="eqref" reference="Eq: simple head 1"}.

\(2\) For this part, note that since $\Delta_{(b_{\bullet}, b_k)}$ is a cuspidal representation as in [@HMM09 Sec. 6] and [@KR09 Sec. 8], $N_k := \mathsf {Ind}\Delta_{(b_{\bullet}, b_k)}^{\boxtimes d_k}$ is irreducible by [@KR09 Lem. 6.6]. We now separate considerations according to the type.

(**Case** $\mathsf{B}_n$) When $\mathfrak{A}$ is of type $\mathsf{B}_n$, let $N = \mathsf {Ind}\Big( \Delta_{({n},b_m)}^{\boxtimes d_m} \boxtimes \cdots \boxtimes \Delta_{({n},b_1)}^{\boxtimes d_1}\Big)$. By [@KP10 Lem. 4.3], we have $\tilde{f}_{n-1}^{t_{n-1}} \cdots  \tilde{f}_{1}^{t_{1}} \mathbf{1} \simeq N.$ By $\eqref{Eq: surj between nablas}$ and Lemma [\[Lem: commuting lemma\]](#Lem: commuting lemma){reference-type="ref" reference="Lem: commuting lemma"}, for $d \in \mathbb{Z}_{\ge 0}$ we obtain $$\begin{aligned}
\mathsf {Ind}\left( L(n^d) \boxtimes  \Delta_{({n},b_k)}^{\boxtimes d} \right) & \simeq
\mathsf {Ind}\left( L(n^{d-1}) \boxtimes L(n) \boxtimes \Delta_{({n},b_k)} \boxtimes  \Delta_{({n},b_k)}^{\boxtimes d-1}\right) \\
& \twoheadrightarrow \mathsf {Ind}\left( L(n^{d-1}) \boxtimes \Delta_{(0,b_k)}  \boxtimes \Delta_{({n},b_k)}^{\boxtimes d-1}\right )
 \simeq \mathsf {Ind}\left( L(n^{d-1}) \boxtimes \Delta_{({n},b_k)}^{\boxtimes d-1} \boxtimes \Delta_{(0,b_k)}\right) \\
& \qquad \vdots \\
& \twoheadrightarrow \mathsf {Ind}\left( \Delta_{(0,b_k)}^{\boxtimes d}\right).
\end{aligned}$$ Since $t_n = d_1 + \cdots + d_m$, by the same argument as above, we have the following chain of surjective homomorphisms $$\begin{aligned}
\mathsf {Ind}\left(L(n^{s+t_n}) \boxtimes N \right)  & \twoheadrightarrow \mathsf {Ind}\left(L(n^{s+t_n-d_m}) \boxtimes \Delta_{(b_{\bullet},b_m)}^{\boxtimes d_m} \boxtimes \Delta_{({n},b_{m-1})}^{\boxtimes d_{m-1}}
\boxtimes \cdots \boxtimes \Delta_{({n},b_1)}^{\boxtimes d_1} \right) \\
& \ \quad  \simeq \mathsf {Ind}\left(L(n^{s+t_n-d_m})  \boxtimes \Delta_{({n},b_{m-1})}^{\boxtimes d_{m-1}}  \boxtimes \cdots \boxtimes \Delta_{({n},b_1)}^{\boxtimes d_1} \boxtimes \Delta_{(b_{\bullet},b_m)}^{\boxtimes d_m} \right) \\
& \twoheadrightarrow \mathsf {Ind}\left(L(n^{s+t_n-d_m-d_{m-1}})  \boxtimes \Delta_{({n},b_{m-2})}^{\boxtimes d_{m-2}}  \boxtimes \cdots \boxtimes \Delta_{({n},b_1)}^{\boxtimes d_1} \boxtimes \Delta_{(b_{\bullet},b_{m-1})}^{\boxtimes d_{m-1}} \boxtimes \Delta_{(b_{\bullet},b_m)}^{\boxtimes d_m} \right) \\
& \qquad \qquad \vdots \\
&\twoheadrightarrow \mathsf {Ind}\left(L(n^{s}) \boxtimes \Big(\overset{m}{\underset{i=1}{\boxtimes}}  \Delta_{(b_{\bullet},b_i)}^{\boxtimes d_i}\Big)\right).
\end{aligned}$$ Therefore, by Lemma [\[Lem: sum of fi\]](#Lem: sum of fi){reference-type="ref" reference="Lem: sum of fi"} and [@KL09 Lem. 3.13], we obtain $$\tilde{f}_{n}^{s+t_{n}}  \tilde{f}_{n-1}^{t_{n-1}} \cdots  \tilde{f}_{1}^{t_{1}} \mathbf{1} \simeq \mathsf{ hd}\,\mathsf {Ind}\left(L(n^{s+t_n}) \boxtimes N\right) \simeq
\mathsf{ hd}\,\mathsf {Ind}\Big(L(n^{s}) \boxtimes \Big (\overset{m}{\underset{i=1}{\boxtimes}}  \Delta_{(b_{\bullet},b_i)}^{\boxtimes d_i}\Big)\Big)$$ and this module has multiplicity one as a composition factor of $\mathsf {Ind}\Big(L(n^{s}) \boxtimes \Big(\overset{m}{\underset{i=1}{\boxtimes}}  \Delta_{(b_{\bullet},b_i)}^{\boxtimes d_i}\Big)\Big)$.

(**Case** $\mathsf{C}_n$) For type $\mathsf{C}_n$, we write $\mathbf{i}(b_{\bullet},b_j)=(n, n-1, \ldots,
n - l_j + 1)$ and let $$\mathbf{k}_k= (\underbrace{n,\ldots,n}_{d_k}, \underbrace{n-1,\ldots,n-1}_{d_k}, \ldots, \underbrace{n - l_k+ 1,\ldots,n - l_k+ 1}_{d_k})$$ for $k= 1, \ldots, m$. Then $\mathbf{k}_k$ appears in $\mathsf{ ch}N_k$ with multiplicity $(d_k!)^{l_k}$. Since $b_{\bullet} \succ b_{m} \succ b_{m-1} \succ \cdots \succ b_1$, the sequence $\mathbf{k} := \mathbf{k}_1 * \cdots * \mathbf{k}_m$ appears in $\mathsf{ ch}\,\mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k\Big)$ with multiplicity $(d_1!)^{l_1} \cdots (d_m!)^{l_m}$. It follows from Lemma [\[Lem: irr of induced module\]](#Lem: irr of induced module){reference-type="ref" reference="Lem: irr of induced module"} and Lemma [\[Lem: commuting lemma\]](#Lem: commuting lemma){reference-type="ref" reference="Lem: commuting lemma"} that $\mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k\Big)$ is irreducible.

Let $\mathbf{t} = ( \underbrace{n,\ldots,n}_{t_n}, \underbrace{n-1,\ldots,n-1}_{t_{n-1}}, \ldots, \underbrace{1,\ldots,1}_{t_{1}} ).$ Then we have $e(\mathbf{t}) \Big( \mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k\Big)\Big) \ne 0$. Since $\mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k\Big)$ is irreducible, by Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"} there exists a surjective homomorphism $$\mathsf {Ind}(L(n^{t_n}) \boxtimes \cdots \boxtimes  L(1^{t_1})) \twoheadrightarrow \mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k\Big).$$ Therefore, it follows from $\eqref{Eq: simple head 2}$ that $\tilde{f}_n^{t_n} \cdots  \tilde{f}_2^{t_2}  \tilde{f}_{1}^{t_{1}} \mathbf{1} \simeq  \mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k\Big).$

(**Case** $\mathsf{D}_n$) For $k=1,\ldots,m$, let $l_k$ be the length of $\mathbf{i}{(\overline{n-1},\overline{n})} * \mathbf{i}{(\overline{n},b_k)}$ if $\overline{n} \succ b_k$, and $l_k=1$ if $b_k = n$ or $b_k = \overline{n}$. We will show that $\mathsf {Ind}\left(\overset{m}{\underset{k=1}{\boxtimes}}  \Delta_{(b_{\bullet}, b_k)}^{\boxtimes d_k}\right)$ is irreducible for type $\mathsf{D}_n$.

First suppose that $b_{m-1} \ne {n-1}.$ Let $$\begin{aligned}
\mathbf{k}_k = \left\{
                  \begin{array}{ll}
                    (\underbrace{n-1,\ldots,n-1}_{d_k}) & \hbox{ if }  b_k = \overline{n}, \\
                    (\underbrace{n,\ldots,n}_{d_k}, \underbrace{n-1,\ldots,n-1}_{d_k}, \ldots, \underbrace{n - l_k + 1,\ldots,n - l_k + 1}_{d_k}) & \hbox{otherwise.}
                  \end{array}
                \right.
\end{aligned}$$ for $k= 1, \ldots, m$. Then $\mathbf{k}_k$ appears in $\mathsf{ ch}N_k$ with multiplicity $(d_k!)^{l_k}$. Since $b_{m} \succ b_{m-1} \succ \cdots \succ b_1$ and $b_{m-1} \ne {n-1}$, the sequence $\mathbf{k} := \mathbf{k}_1 * \cdots * \mathbf{k}_m$ appears in $\mathsf{ ch}\,\mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k\Big)$ with multiplicity $(d_1!)^{l_1} \cdots (d_m!)^{l_m}$. It follows from Lemma [\[Lem: irr of induced module\]](#Lem: irr of induced module){reference-type="ref" reference="Lem: irr of induced module"} and Lemma [\[Lem: commuting lemma\]](#Lem: commuting lemma){reference-type="ref" reference="Lem: commuting lemma"} that $\mathsf {Ind}\Big( \overset{m}{\underset{k=1}{\boxtimes}}  N_k\Big)$ is irreducible.

We now assume that $b_{m-1} = {n-1}.$ Without loss of generality, we may suppose that $b_{m} = \overline{n}.$ Since $\mathsf {Ind}(L(n-1) \boxtimes L(n)) \simeq \mathsf {Ind}(L(n) \boxtimes L(n-1))$, we have $$\mathsf {Ind}\Delta_{(\overline{n-1}, {n-1})}^{\boxtimes d_{m-1}} \boxtimes \Delta_{(\overline{n-1}, \overline{n})}^{\boxtimes d_{m}} \simeq
\mathsf {Ind}\Delta_{(\overline{n-1}, \overline{n})}^{\boxtimes d_{m}} \boxtimes \Delta_{(\overline{n-1}, {n-1})}^{\boxtimes d_{m-1}} \simeq \mathsf {Ind}\left( L\big(n^{d_{m-1} }\big) \boxtimes L\big((n-1)^{d_{m-1} + d_m}\big) \right)$$ and they are irreducible. Let $M_k = \left\{
        \begin{array}{ll}
          \mathsf {Ind}\Delta_{(b_{\bullet}, b_k)}^{\boxtimes d_k} & \hbox{ if } k \le m-2, \\
          \mathsf {Ind}\Delta_{(b_{\bullet}, b_{m-1})}^{\boxtimes d_{m-1}} \boxtimes \Delta_{(b_{\bullet}, b_{m})}^{\boxtimes d_{m}} & \hbox{ if } k=m-1,
        \end{array}
      \right.$ and set

::: center
$\mathbf{k}_k = \left\{
                  \begin{array}{ll}
                    (\underbrace{n,\ldots,n}_{d_k}, \underbrace{n-1,\ldots,n-1}_{d_k}, \ldots, \underbrace{n - \ell_k + 1,\ldots,n - \ell_k + 1}_{d_k}) & \hbox{ if }  k \le m-2, \\
                    (\underbrace{n,\ldots,n}_{d_{m-1}},\underbrace{n-1,\ldots,n-1}_{d_{m-1}+d_m}) & \hbox{ if } k = m-1.
                  \end{array}
                \right.$
:::

Then the multiplicity of $\mathbf{k}_k$ in $\mathsf{ ch}M_k$ is $(d_k!)^{l_k}$ if $k \le m-2$ and $d_{m-1}! (d_m + d_{m-1})!$ if $k = m-1$. Since $b_{\bullet} \succ b_{m} \succ b_{m-1} \succ \cdots \succ b_1$, the sequence $\mathbf{k} := \mathbf{k}_1 * \cdots * \mathbf{k}_{m-1}$ appears in $\mathsf{ ch}\left(\mathsf {Ind}(M_1\boxtimes \cdots \boxtimes M_{m-1})\right)$ with multiplicity $(d_1!)^{l_1} \cdots (d_{m-2}!)^{l_{m-2}} (d_{m-1}!) ((d_m + d_{m-1})!)$. It follows from Lemma [\[Lem: irr of induced module\]](#Lem: irr of induced module){reference-type="ref" reference="Lem: irr of induced module"} and Lemma [\[Lem: commuting lemma\]](#Lem: commuting lemma){reference-type="ref" reference="Lem: commuting lemma"} that $\mathsf {Ind}(M_1\boxtimes \cdots \boxtimes M_{m-1})$ is irreducible.

Now for $\mathbf{t} = ( \underbrace{n,\ldots,n}_{t_n}, \underbrace{n-1,\ldots,n-1}_{t_{n-1}}, \ldots, \underbrace{1,\ldots,1}_{t_{1}} ),$ we have $e(\mathbf{t})\left( \mathsf {Ind}\Big( \overset{m}{\underset{i=1}{\boxtimes}}  \Delta_{(b_{\bullet}, b_i)}^{\boxtimes d_i}\Big)\right) \ne 0$. Since $\mathsf {Ind}\left(\overset{m}{\underset{i=1}{\boxtimes}}  \Delta_{(b_{\bullet}, b_i)}^{\boxtimes d_i}\right)$ is irreducible, Lemma [\[Lem: Frobenius reciprocity\]](#Lem: Frobenius reciprocity){reference-type="ref" reference="Lem: Frobenius reciprocity"} gives a surjective homomorphism $$\mathsf {Ind}(L(n^{t_n}) \boxtimes \cdots \boxtimes  L(1^{t_1})) \twoheadrightarrow \mathsf {Ind}\left(\overset{m}{\underset{i=1}{\boxtimes}}  \Delta_{(b_{\bullet}, b_i)}^{\boxtimes d_i}\right),$$ which implies the desired conclusion $\tilde{f}_n^{t_n} \cdots  \tilde{f}_2^{t_2}  \tilde{f}_{1}^{t_{1}} \mathbf{1} \simeq  \mathsf {Ind}\left(\overset{m}{\underset{i=1}{\boxtimes}}  \Delta_{(b_{\bullet}, b_i)}^{\boxtimes d_i}\right)$ by $\eqref{Eq: simple head 2}$. ◻
:::

Recall the definition of $\widehat{\imath} \in \mathbf{B}$ from $\eqref{Eq: def of overhat i}$. Using the surjective homomorphism in $\eqref{Eq: surj between nablas}$, we can glue parts (1) and (2) of Lemma [\[Lem: seq of kf\]](#Lem: seq of kf){reference-type="ref" reference="Lem: seq of kf"} together for types $\mathsf{B}_n, \mathsf{C}_n$, and $\mathsf{D}_n$ to get the following result.

::: lemma
[]{#Lem: gluing lemma label="Lem: gluing lemma"} Let $t_i \in \mathbb{Z}_{\ge 0}$ be such that $$\begin{aligned}
& t_1 \ge t_2 \ge \cdots \ge t_{n'-1} \ge t_{n'} \ge  t_{n'+1}=0 \ \  & \qquad (\mathsf{A}_n, \mathsf{C}_n), \\
& 2t_1 \ge 2t_2 \ge \cdots \ge 2t_{n-1} \ge t_{n} \ge 2t_{n+1}\ge \cdots \ge 2t_{n'-1} \ge  t_{n'}=0 \ \  & \qquad (\mathsf{B}_n), \\
& t_1 \ge t_2 \ge \cdots \ge t_{n-2} \ge t_{n-1},t_{n} \ge t_{n+1}\ge \cdots \ge t_{n'-1} \ge  t_{n'}=0 \ \  & \qquad(\mathsf{D}_n),
\end{aligned}$$ where $n'=n\ (\mathsf{A}_n)$, $n' = 2n\ (\mathsf{B}_n)$, $n' = 2n-1\ (\mathsf{C}_n, \mathsf{D}_n)$. Set

$$\vartheta_{i} = \left\{
                   \begin{array}{ll}
                     t_{i} - t_{i+1} & \hbox{if } i \le n'\ \  (\mathsf{A}_n,\mathsf{C}_n),\ \  i \le n-2\ (\mathsf{B}_n),\ \ i \le n-3\ (\mathsf{D}_n), \\
                     t_{n-1} - \lceil \frac{t_{n}}{2} \rceil & \hbox{if } i=n-1\ \ (\mathsf{B}_n), \\
                     \lceil \frac{t_{n}}{2} \rceil - \lfloor \frac{t_{n}}{2} \rfloor & \hbox{if } i=n\qquad \  (\mathsf{B}_n), \\
                     \lfloor \frac{t_{n}}{2} \rfloor - t_{n+1} & \hbox{if } i=n+1\ \ (\mathsf{B}_n), \\
                      t_{ n-2} - \max\{ t_{n-1}, t_{n} \} & \hbox{if } i=n-2\ \ (\mathsf{D}_n), \\
                      \max\{ 0, t_{n}-t_{n-1} \} & \hbox{if } i=n-1\ \  (\mathsf{D}_n), \\
                      \max\{ 0, t_{n-1}-t_{n} \} & \hbox{if } i=n\qquad \  (\mathsf{D}_n), \\
                      \min\{ t_{ n-1}, t_{n} \} - t_{ n+1} & \hbox{if } i = n+1\  \ (\mathsf{D}_n), \\
                      t_{i-1} - t_{i} & \hbox{if } i \ge n+2\ \ (\mathsf{B}_n, \mathsf{D}_n).
                   \end{array}
                 \right.$$ Then

1.  $\mathsf{ hd}\,\mathsf {Ind}\left( \overset{n'}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{i+1})}^{\boxtimes \vartheta_{i}}\right)$ is irreducible and has multiplicity one as a composition factor of $\mathsf {Ind}\left( \overset{n'}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{i+1})}^{\boxtimes \vartheta_{i}}\right)$,

2.  $\tilde{f}_{\mathbf{i}} \mathbf{1} \simeq  \mathsf{ hd}\,\mathsf {Ind}\left ( \overset{n'}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{i+1})}^{\boxtimes \vartheta_{i}}\right)$, where $$\mathbf{i} = \left\{
                     \begin{array}{ll}
                       (\underbrace{1,\ldots,1}_{t_1}, \underbrace{2,\ldots,2}_{t_2}, \ldots, \underbrace{n,\ldots,n}_{t_n} ) & \ \  (\mathsf{A}_n), \\
                       (\underbrace{1,\ldots,1}_{t_1},  \ldots, \underbrace{n-1,\ldots,n-1}_{t_{n-1}},\underbrace{n,\ldots,n}_{t_n},
    \underbrace{n-1,\ldots,n-1}_{t_{n+1}}, \ldots, \underbrace{1,\ldots,1}_{t_{2n-1}} ) & \ \  (\mathsf{B}_n, \mathsf{C}_n), \\
                       (\underbrace{1,\ldots,1}_{t_1},  \ldots, \underbrace{n-2,\ldots,n-2}_{t_{n-2}},\underbrace{n,\ldots,n}_{t_{n-1}},
    \underbrace{n-1,\ldots,n-1}_{t_{n}}, \ldots, \underbrace{1,\ldots,1}_{t_{2n-2}} ) & \ \ (\mathsf{D}_n).
                     \end{array}
                   \right.$$
:::

::: proof
*Proof.* By Lemma [\[Lem: commuting lemma\]](#Lem: commuting lemma){reference-type="ref" reference="Lem: commuting lemma"} and $\eqref{Eq: surj between nablas}$, for $k \in \mathbb{Z}_{\ge0}$ we have $$\label{Eq: gluing}
 \begin{aligned}
\mathsf {Ind}\left(\Delta_{(\widehat{1},b)}^{\boxtimes k} \boxtimes \Delta_{(b,c)}^{ \boxtimes k}\right) & \simeq
\mathsf {Ind}\left(\Delta_{(\widehat{1},b)}^{\boxtimes k-1} \boxtimes \Delta_{(\widehat{1},b)} \boxtimes \Delta_{(b,c)}  \boxtimes  \Delta_{(b,c)}^{ \boxtimes k-1}\right) \\
& \twoheadrightarrow
\mathsf {Ind}\left(\Delta_{(\widehat{1},b)}^{\boxtimes k-1} \boxtimes \Delta_{(\widehat{1},c)} \boxtimes  \Delta_{(b,c)}^{ \boxtimes k-1}\right)\\
&\quad \  \simeq
\mathsf {Ind}\left( \Delta_{(\widehat{1},b)}^{\boxtimes k-1} \boxtimes   \Delta_{(b,c)}^{ \boxtimes k-1} \boxtimes \Delta_{(\widehat{1},c)}\right)\\
& \hspace{1.28truecm}  \vdots \\
& \twoheadrightarrow  \mathsf {Ind}\left( \Delta_{(\widehat{1},c)}^{\boxtimes k}\right),
 \end{aligned}$$ where $b \in B \ (\mathsf{A}_n)$,  $b = \widehat{n+1}\ (\mathsf{B}_n)$,  $b = \widehat{n}\ (\mathsf{C}_n)$, $b = \widehat{n-1}\ (\mathsf{D}_n)$ and $c \in \mathbf{B}$ with $b \succ c$.

(**Case** $\mathsf{A}_n$) The assertion in this case follows from Lemma [\[Lem: seq of kf\]](#Lem: seq of kf){reference-type="ref" reference="Lem: seq of kf"}.

(**Case** $\mathsf{B}_n$) For type $\mathsf{B}_n$, let $$\begin{aligned}
M(k) &=  \mathsf {Ind}\left( \Big(\overset{2n-k}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{\imath+1})}^{\boxtimes \vartheta_i} \Big) \boxtimes
 \Delta_{(\widehat{1},\widehat{n+1})}^{\boxtimes (\vartheta_{2n} + \cdots + \vartheta_{2n+1-k})} \right),  \ \ \hbox{\rm and} \\
N(k) &= \mathsf {Ind}\left( \Delta_{(\widehat{n+1}, \widehat{2n+2-k})}^{\boxtimes \vartheta_{2n+1-k}}
\boxtimes \Delta_{(\widehat{n+1}, \widehat{2n+3-k})}^{\boxtimes \vartheta_{2n+2-k}} \boxtimes \cdots \boxtimes \Delta_{(\widehat{n+1}, \widehat{2n+1})}^{\boxtimes \vartheta_{2n}} \right)
\end{aligned}$$ for $k = 1, \ldots,n$. Note that $t_n = \lceil \frac{t_{n}}{2} \rceil + \lfloor \frac{t_{n}}{2} \rfloor$, $\lceil \frac{t_{n}}{2} \rceil = \vartheta_{n} + \cdots \vartheta_{2n}$ and $\lfloor \frac{t_{n}}{2} \rfloor = \vartheta_{n+1} + \cdots +\vartheta_{2n}$. If follows from Lemma [\[Lem: seq of kf\]](#Lem: seq of kf){reference-type="ref" reference="Lem: seq of kf"} that $$M(n) \simeq  \tilde{f}_1^{t_1} \cdots  \tilde{f}_{n-1}^{t_{n-1}}  \tilde{f}_{n}^{\lceil \frac{t_{n}}{2} \rceil} \mathbf{1}, \qquad
\mathsf{ hd}N(n) \simeq  \tilde{f}_{n}^{\lfloor \frac{t_{n}}{2} \rfloor }  \tilde{f}_{n-1}^{t_{n+1}} \cdots  \tilde{f}_{1}^{t_{2n-1}}   \mathbf{1}.$$ By Lemma [\[Lem: seq of kf\]](#Lem: seq of kf){reference-type="ref" reference="Lem: seq of kf"} and [@KL09 Lem. 3.13], there is a surjective homomorphism $$\mathsf {Ind}\left( \Delta_{(\overline{1},\overline{n})}^{\boxtimes \lceil \frac{t_{n}}{2} \rceil} \boxtimes L(n^{\lceil \frac{t_{n}}{2} \rceil}) \right) \twoheadrightarrow
\mathsf {Ind}\Delta_{(\overline{1},0)}^{\boxtimes \lceil \frac{t_{n}}{2} \rceil},$$ which yields the following surjective homomorphism $$\begin{aligned}
& \mathsf {Ind}\left(  \Big( \Big (\overset{n-1}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{\imath+1})}^{\boxtimes \vartheta_i}\Big) \boxtimes  \Delta_{(\widehat{1},\widehat{n})}^{\boxtimes \lceil \frac{t_{n}}{2} \rceil} \Big)
\boxtimes \left( L(n^{\lceil \frac{t_{n}}{2} \rceil}) \boxtimes N(n) \right) \right) \\
& \  \twoheadrightarrow
\mathsf {Ind}\left(  \Big (\overset{n-1}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{i+1})}^{\boxtimes \vartheta_i}\Big) \boxtimes  \Delta_{(\widehat{1},\widehat{n+1})}^{\boxtimes \lceil \frac{t_{n}}{2} \rceil}
\boxtimes N(n) \right) \\ & \quad  \  \simeq
\mathsf {Ind}\left( \Big(\overset{n}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{\imath+1})}^{\boxtimes \vartheta_i}\Big) \boxtimes  \Delta_{(\widehat{1},\widehat{n+1})}^{\boxtimes \lfloor \frac{t_{n}}{2} \rfloor}
\boxtimes N(n) \right) \\  & \quad \  \simeq  \mathsf {Ind}(M(n) \boxtimes N(n)).
\end{aligned}$$ It follows from Lemma [\[Lem: seq of kf\]](#Lem: seq of kf){reference-type="ref" reference="Lem: seq of kf"} that $$\begin{aligned}
 \tilde{f}_1^{t_1} \cdots  \tilde{f}_{n-1}^{t_{n-1}} \mathbf{1} & \simeq
\mathsf {Ind}\left(\Big(\overset{n-1}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{i+1})}^{\boxtimes \vartheta_i}\Big) \boxtimes  \Delta_{(\widehat{1},\widehat{n})}^{\boxtimes \lceil \frac{t_{n}}{2} \rceil} \right), \\
 \tilde{f}_{n}^{t_{n} }  \tilde{f}_{n-1}^{t_{n+1}} \cdots  \tilde{f}_{1}^{t_{2n-1}}   \mathbf{1} & \simeq \mathsf{ hd}\,\mathsf {Ind}\left( L(n^{\lceil \frac{t_{n}}{2} \rceil}) \boxtimes N(n) \right).
\end{aligned}$$ Since $\varepsilon_i \left( \mathsf {Ind}\big(L(n^{\lceil \frac{t_{n}}{2} \rceil}) \boxtimes N(n)\big) \right) =0$ for $i=1,\ldots, n-1$, by Lemma [\[Lem: sum of fi\]](#Lem: sum of fi){reference-type="ref" reference="Lem: sum of fi"} we have $$\tilde{f}_{\mathbf{i}} \mathbf{1}  \simeq \mathsf{ hd}\,\mathsf {Ind}\big(M(n) \boxtimes N(n)\big),$$ and this module has multiplicity one as a composition factor of $\mathsf {Ind}\big (M(n) \boxtimes N(n)\big)$.

Now by Lemma [\[Lem: commuting lemma\]](#Lem: commuting lemma){reference-type="ref" reference="Lem: commuting lemma"} and $\eqref{Eq: gluing}$, we have the following chain of surjective homomorphisms $$\begin{aligned}
& \mathsf {Ind}(M(n) \boxtimes N(n)) \\
& \qquad \simeq \mathsf {Ind}\left( \Big( \overset{n}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{\imath+1})}^{\boxtimes \vartheta_i} \Big) \boxtimes
 \Delta_{(\widehat{1},\widehat{n+1})}^{\boxtimes (\vartheta_{2n}+\cdots + \vartheta_{n+2})}  \boxtimes
\left( \Delta_{(\widehat{1},\widehat{n+1})}^{\boxtimes \vartheta_{n+1}} \boxtimes \Delta_{(\widehat{n+1}, \widehat{n+2})}^{\boxtimes \vartheta_{n+1}} \right)
\boxtimes N(n-1) \right) \\
& \qquad \twoheadrightarrow \mathsf {Ind}\left( \Big( \overset{n}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{\imath+1})}^{\boxtimes \vartheta_i} \Big) \boxtimes
 \Delta_{(\widehat{1},\widehat{n+1})}^{\boxtimes (\vartheta_{2n}+\cdots + \vartheta_{n+2})} \boxtimes
 \Delta_{(\widehat{1},\widehat{n+2})}^{\boxtimes \vartheta_{n+1}}
\boxtimes N(n-1) \right) \\
& \qquad \quad \ \  \simeq \mathsf {Ind}(M(n-1) \boxtimes N(n-1)) \\
& \hspace{3truecm}  \vdots \\
& \qquad \twoheadrightarrow \mathsf {Ind}(M(1) \boxtimes N(1))   \simeq \mathsf {Ind}\left (\Big(\overset{2n-1}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{\imath+1})}^{\boxtimes \vartheta_i} \Big) \boxtimes
\Delta_{(\widehat{1},\widehat{n+1})}^{\boxtimes \vartheta_{2n}} \boxtimes \Delta_{(\widehat{n+1},\widehat{2n+1})}^{\boxtimes \vartheta_{2n}} \right) \\
& \qquad \twoheadrightarrow \mathsf {Ind}\left(\overset{2n}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{i+1})}^{\boxtimes \vartheta_i}\right ),
\end{aligned}$$ which completes the proof for $\mathsf{B}_n$.

(**Case** $\mathsf{C}_n$) For type $\mathsf{C}_n$, set $$\begin{aligned}
M(k) &= \mathsf {Ind}\left( \Big(\overset{n-1}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{i+1})}^{\boxtimes \vartheta_{i}}\Big) \boxtimes
\Delta_{(\widehat{1}, \widehat{n})}^{\boxtimes (\vartheta_{n} + \cdots + \vartheta_{n-1+k})} \right), \ \ \hbox{\rm and} \\
N(k) &= \mathsf {Ind}\left( \Delta_{(\widehat{n}, \widehat{k+n})}^{\boxtimes \vartheta_{k+n-1}} \boxtimes  \Delta_{(\widehat{n}, \widehat{k+n-1})}^{\boxtimes \vartheta_{k+n-2}} \boxtimes
\cdots \boxtimes \Delta_{(\widehat{n}, \widehat{n+1})}^{\boxtimes \vartheta_{n}} \right)
\end{aligned}$$ for $1 \le k \le n$. It follows from Lemma [\[Lem: seq of kf\]](#Lem: seq of kf){reference-type="ref" reference="Lem: seq of kf"} that $$M(n) \simeq  \tilde{f}_{1}^{t_{1}}  \tilde{f}_{2}^{t_{2}} \cdots  \tilde{f}_{n-1}^{t_{n-1}} \mathbf{1} , \quad \
 N(n) \simeq  \tilde{f}_{n}^{t_{n}}  \tilde{f}_{n-1}^{t_{n+1}} \cdots  \tilde{f}_{1}^{t_{2n-1}} \mathbf{1} .$$ Since $\varepsilon_i(N(n))=0$ for $i=1,\ldots, n-1$, Lemma [\[Lem: sum of fi\]](#Lem: sum of fi){reference-type="ref" reference="Lem: sum of fi"} implies $$\tilde{f}_{\mathbf{i}} \mathbf{1} \simeq \mathsf{ hd}\,\mathsf {Ind}(M(n) \boxtimes N(n))$$ and this module has multiplicity one as a composition factor in $\mathsf {Ind}\big(M(n) \boxtimes N(n)\big)$.

By Lemma [\[Lem: commuting lemma\]](#Lem: commuting lemma){reference-type="ref" reference="Lem: commuting lemma"} and $\eqref{Eq: gluing}$, we have a chain of surjective homomorphisms $$\begin{aligned}
 \mathsf {Ind}\big(M(n) \boxtimes N(n)\big) & \simeq  \mathsf {Ind}\left(  M(n-1) \boxtimes \Delta_{(\widehat{1},\widehat{n})}^{\boxtimes \vartheta_{2n-1}} \boxtimes
\Delta_{(\widehat{n},\widehat{2n})}^{\boxtimes \vartheta_{2n-1}} \boxtimes N(n-1) \right) \\
&\twoheadrightarrow  \mathsf {Ind}\left( M(n-1) \boxtimes \Delta_{(\widehat{1},\widehat{2n})}^{\boxtimes \vartheta_{2n-1}} \boxtimes N(n-1) \right) \\
&\quad \ \  \simeq \mathsf {Ind}\left( M(n-1) \boxtimes N(n-1) \boxtimes \Delta_{(\widehat{1},\widehat{2n})}^{\boxtimes \vartheta_{2n-1}} \right) \\
& \hspace{3truecm} \vdots \\
&\twoheadrightarrow  \mathsf {Ind}\left( M(1) \boxtimes N(1) \boxtimes \Delta_{(\widehat{1},\widehat{n+2})}^{\boxtimes \vartheta_{n+1}} \boxtimes \cdots
\boxtimes \Delta_{(\widehat{1},\widehat{2n})}^{\boxtimes \vartheta_{2n-1}} \right)  \allowdisplaybreaks \\
&\twoheadrightarrow  \mathsf {Ind}\left(\Big(\overset{n-1}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{\imath+1})}^{\boxtimes \vartheta_{i}}\Big) \boxtimes \Delta_{(\widehat{1},\widehat{n+1})}^{\boxtimes \vartheta_{n}} \boxtimes \cdots
\boxtimes \Delta_{(\widehat{1},\widehat{2n})}^{\boxtimes \vartheta_{2n-1}} \right)  \\
&\quad \ \  \simeq  \mathsf {Ind}\left( \overset{2n-1}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{\imath+1})}^{\boxtimes \vartheta_{i}}\right),
\end{aligned}$$ which yields $\tilde{f}_{\mathbf{i}} \mathbf{1} \simeq  \mathsf{ hd}\,\mathsf {Ind}\left ( \overset{2n-1}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{\imath+1})}^{\boxtimes \vartheta_{i}}\right).$

(**Case** $\mathsf{D}_n$) Without loss of generality, we may assume in the $\mathsf{D}_n$ case that $t_{n-1} \ge t_n$. Note that $\vartheta_{n-1} = 0$ and $\vartheta_n =  \mathsf{max}\{ t_{n-1}, t_{n} \} - \mathsf{min}\{ t_{n-1}, t_{n} \}$. Let $$\begin{aligned}
M(k) &= \mathsf {Ind}\left( \Big(\overset{n-2}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{i+1})}^{\boxtimes \vartheta_{i}}\Big) \boxtimes
\Delta_{(\widehat{1}, \widehat{n-1})}^{\boxtimes (\vartheta_{n}+ \cdots + \vartheta_{n-1+k} )} \right), \\
N(k) &= \mathsf {Ind}\left( \Delta_{(\widehat{n-1}, \widehat{k+n})}^{\boxtimes \vartheta_{k+n-1}} \boxtimes  \Delta_{(\widehat{n-1}, \widehat{k+n-1})}^{\boxtimes \vartheta_{k+n-2}} \boxtimes
\cdots \boxtimes \Delta_{(\widehat{n-1}, \widehat{n+1})}^{\boxtimes \vartheta_{n}} \right)
\end{aligned}$$ for $k = 1, \ldots, n$. It follows from Lemma [\[Lem: seq of kf\]](#Lem: seq of kf){reference-type="ref" reference="Lem: seq of kf"} that $$M(n) \simeq  \tilde{f}_{1}^{t_{1}}  \tilde{f}_{2}^{t_{2}} \cdots  \tilde{f}_{n-2}^{t_{n-2}} \mathbf{1}, \quad \
 N(n) \simeq  \tilde{f}_{n}^{t_{n-1}}  \tilde{f}_{n-1}^{t_{n}}  \tilde{f}_{n-2}^{t_{n+1}} \cdots  \tilde{f}_{1}^{t_{2n-2}} \mathbf{1}.$$ Since $\varepsilon_i(N(n))=0$ for $i=1,\ldots, n-2$, Lemma [\[Lem: sum of fi\]](#Lem: sum of fi){reference-type="ref" reference="Lem: sum of fi"} gives $$\tilde{f}_{\mathbf{i}} \mathbf{1} \simeq \mathsf{ hd}\,\mathsf {Ind}(M(n) \boxtimes N(n)),$$ and this module with multiplicity one in $\mathsf {Ind}(M(n) \boxtimes N(n))$.

Since $\Delta_{(\widehat{1},\widehat{n})}^{\boxtimes \vartheta_{n-1}} = \mathbb{C}$, Lemma [\[Lem: commuting lemma\]](#Lem: commuting lemma){reference-type="ref" reference="Lem: commuting lemma"} and [\[Eq: gluing\]](#Eq: gluing){reference-type="eqref" reference="Eq: gluing"} again give a string of surjective homomorphisms $$\begin{aligned}
 \mathsf {Ind}(M(n) \boxtimes N(n))
& \simeq  \mathsf {Ind}\left( M(n-1) \boxtimes \Delta_{(\widehat{1},\widehat{n-1})}^{\boxtimes \vartheta_{2n-1}} \boxtimes
\Delta_{(\widehat{n-1},\widehat{2n})}^{\boxtimes \vartheta_{2n-1}} \boxtimes N(n-1) \right) \\
&\twoheadrightarrow  \mathsf {Ind}\left( M(n-1) \boxtimes \Delta_{(\widehat{1},\widehat{2n})}^{\boxtimes \vartheta_{2n-1}} \boxtimes N(n-1) \right) \\
&\quad \  \simeq \mathsf {Ind}\left( M(n-1) \boxtimes N(n-1) \boxtimes \Delta_{(\widehat{1},\widehat{2n})}^{\boxtimes \vartheta_{2n-1}} \right) \\
& \hspace{3truecm} \vdots  \\
&\twoheadrightarrow  \mathsf {Ind}\left( M(1) \boxtimes N(1) \boxtimes \Delta_{(\widehat{1},\widehat{n+2})}^{\boxtimes \vartheta_{n+1}} \boxtimes \cdots
\boxtimes \Delta_{(\widehat{1},\widehat{2n})}^{\boxtimes \vartheta_{2n-1}} \right)  \allowdisplaybreaks \\
&\twoheadrightarrow  \mathsf {Ind}\left(\Big(\overset{n-2}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{\imath+1})}^{\boxtimes \vartheta_{i}}\Big) \boxtimes \Delta_{(\widehat{1},\widehat{n+1})}^{\boxtimes \vartheta_{n}} \boxtimes \cdots
\boxtimes \Delta_{(\widehat{1},\widehat{2n})}^{\boxtimes \vartheta_{2n-1}} \right)  \\
&\quad \ \simeq \mathsf {Ind}\left( \overset{2n-1}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{\imath+1})}^{\boxtimes \vartheta_{i}} \right),
\end{aligned}$$ which yields the desired result $\tilde{f}_{\mathbf{i}} \mathbf{1} \simeq  \mathsf{ hd}\,\mathsf {Ind}\left( \overset{2n-1}{\underset{i=1}{\boxtimes}}  \Delta_{(\widehat{1}, \widehat{\imath+1})}^{\boxtimes \vartheta_{i}}\right).$ ◻
:::

As an immediate consequence of this lemma we have

::: corollary
 $\mathcal{N}_n(v) = \mathsf{ hd}\,\mathsf {Ind}\Delta(\mathbf{a}(v);n) \  \text{ for } v \in B(\infty),$ where $\mathcal{N}_n(v)$ is the irreducible module given in Proposition [\[Prop: description of Nk\]](#Prop: description of Nk){reference-type="ref" reference="Prop: description of Nk"}.
:::

We now are ready to prove Theorem [\[Thm: main theorem\]](#Thm: main theorem){reference-type="ref" reference="Thm: main theorem"}.

::: proof
*Proof of Theorem [\[Thm: main theorem\]](#Thm: main theorem){reference-type="ref" reference="Thm: main theorem"}.* Let $I_{(k)} = \{ n-k+1, n-k+2, \ldots , n  \}$ for $k=1, \ldots, n$. Note that $I_{(k)} \subset I_{(k+1)}$ and $|I_{(k)}|=k$. Let $U_q(\mathfrak{g}_k)$ be the subalgebra of $U_q(\mathfrak{g})$ generated by $e_i,\ f_i\ (i\in I_{(k)})$ and $q^h\ (h \in \mathsf{P}^{\vee})$, and let $\mathfrak{B}_k$ be the crystal obtained from $B(\infty)$ by forgetting the $i$-arrows for $i \notin I_{(k)}$. It follows from Table [\[Tb: w0\]](#Tb: w0){reference-type="ref" reference="Tb: w0"} that $U_q(\mathfrak{g}_k)$ is of type $\mathsf{X}_{k}$ when $U_q(\mathfrak{g})$ is of type $\mathsf{X}_n$ ($\mathsf{X = A,B,C,D}$). Recall the definition $\mathbf{a}_i$ for $\mathbf{a} \in \mathcal{S}$ and the sequences $\mathbf{s}_k$ given in Section [\[Sec: Description Nk\]](#Sec: Description Nk){reference-type="ref" reference="Sec: Description Nk"}. Take $v \in B(\infty)$ and let $\triangle(\mathbf{a}(v)) = \{ t_{ij} \}$. If $i=1, \ldots, n$ for type $\mathsf{A}_n, \mathsf{B}_n, \mathsf{C}_n$, then $$\mathbf{a}(v)_i = (t_{i,n+1-i}, t_{i,n+2-i}, \ldots, t_{i,d_i}),$$ where $d_i = n\ \hbox{\rm for all} \ i \ \ (\mathsf{A}_n)$ and $d_i = n-1+i\ (\mathsf{B}_n, \mathsf{C}_n)$. If $i=1, \ldots, n$ for type $\mathsf{D}_n$, then $$\mathbf{a}(v)_i = \left\{
                      \begin{array}{ll}
                        (t_{1,n-1}) & \hbox{ if } i = 1, \\
                        (t_{1,n}) & \hbox{ if } i = 2, \\
                        (t_{i-1, n+1-i}, t_{i-1, n+2-i}, \ldots, t_{i-1, n-2+i}) & \hbox{ if } i = 3, \ldots, n.
                      \end{array}
                    \right.$$ Let $M_k = \mathsf {Ind}\Delta(\mathbf{a}(v);k)$ for $k=1,\ldots, n$. Then, by Proposition [\[Prop: description of Nk\]](#Prop: description of Nk){reference-type="ref" reference="Prop: description of Nk"}, Lemma [\[Lem: gluing lemma\]](#Lem: gluing lemma){reference-type="ref" reference="Lem: gluing lemma"}, and the choice of $I_{(k)}$, we obtain $$\mathcal{N}_k(v)  = \mathsf{ hd}M_k \ \ \ \text{ for } k=1,\ldots, n.$$ By the construction of $\Delta(\mathbf{a}(v);k)$ and Lemma [\[Lem:
gluing lemma\]](#Lem:
gluing lemma){reference-type="ref" reference="Lem:
gluing lemma"}, we know

1.  $\varepsilon_i( M_k ) = 0 \ \ \text{for } i\in I_{(k-1)}$,

2.  $\mathsf{ hd}M_k$ is irreducible and occurs with multiplicity one as a composition factor of $M_k$.

Therefore, by Lemma [\[Lem: sum of fi\]](#Lem: sum of fi){reference-type="ref" reference="Lem: sum of fi"} and Proposition [\[Prop: crystal iso\]](#Prop: crystal iso){reference-type="ref" reference="Prop: crystal iso"}, $$\begin{aligned}
\Phi(v) & = \mathsf{ hd}\,\mathsf {Ind}\left( (\mathsf{ hd}M_1) \boxtimes (\mathsf{ hd}M_2) \boxtimes \cdots \boxtimes (\mathsf{ hd}M_{n})\right) \\
&= \mathsf{ hd}\,\mathsf {Ind}(  M_1 \boxtimes  M_2 \boxtimes \cdots \boxtimes M_{n}) \\
&= \mathsf{ hd}\,\mathsf {Ind}\big (  \Delta(\mathbf{a}(v);1) \boxtimes \cdots \boxtimes \Delta(\mathbf{a}(v);n) \big),
\end{aligned}$$ which completes the proofs of (1) and (2).

Let $\Psi^\lambda: B(\lambda) \rightarrow \mathbb{B}(\lambda)$ be the canonical crystal isomorphism given by $\Psi^{\lambda}( \tilde{f}_{\mathbf{i}}  b_\lambda) =  \tilde{f}_{\mathbf{i}} \mathbf{1}$ for any sequence $\mathbf{i}$ of elements in $I$. Then the following diagram commutes: $$\CrystalDiagram$$ Here, $\imath_\lambda$ (resp. $\jmath_\lambda$) is the crystal embedding $\eqref{Eq: crystal embedding}$ from $B(\lambda)$ (resp. $\mathbb{B}(\lambda)$) to $B(\infty)\otimes T_\lambda \otimes C$ (resp. $\mathbb{B}(\infty)\otimes T_\lambda \otimes C$). Assume for $v\in B(\lambda)$ that $\iota_{\lambda}(v) = v' \otimes t_\lambda \otimes c$ for some $v' \in B(\infty)$, and recall that $\mathbf{a}(v) = \mathbf{a}(v')$. Let $\jmath_\lambda^{-1}$ be the inverse from ${\mathsf {im}}(\jmath_\lambda)$ to $\mathbb{B}(\lambda)$. Then $$\Psi^\lambda = \jmath^{-1}_\lambda \circ (\Psi \otimes  \mathsf{id}\otimes  \mathsf{id}) \circ \imath_\lambda,$$ which yields $$\begin{aligned}
\Psi^\lambda(v) &= \jmath^{-1}_\lambda \circ (\Psi \otimes  \mathsf{id}\otimes  \mathsf{id}) \circ \imath_\lambda(v) \\
& = \jmath^{-1}_\lambda \circ (\Psi \otimes  \mathsf{id}\otimes  \mathsf{id}) (v' \otimes t_\lambda \otimes c) \\
&= \jmath^{-1}_\lambda ( \mathsf{ hd}\,\mathsf {Ind}(\Delta(\mathbf{a}(v');1) \boxtimes \cdots \boxtimes \Delta(\mathbf{a}(v');n)) \otimes t_\lambda \otimes c) \\
&= \jmath^{-1}_\lambda ( \mathsf{ hd}\,\mathsf {Ind}(\Delta(\mathbf{a}(v);1) \boxtimes \cdots \boxtimes \Delta(\mathbf{a}(v);n)) \otimes t_\lambda \otimes c) \\
&= \mathsf{ hd}\,\mathsf {Ind}(\Delta(\mathbf{a}(v);1) \boxtimes \cdots \boxtimes \Delta(\mathbf{a}(v);n)).
\end{aligned}$$ This proves assertion (3) and concludes the proof of the main theorem (Theorem [\[Thm: main theorem\]](#Thm: main theorem){reference-type="ref" reference="Thm: main theorem"}). ◻
:::

1em

::: center
**Acknowledgments**
:::

Work on this paper was facilitated by a visit by S.-J. Kang, S.-j. Oh, and E. Park to the University of Wisconsin-Madison and by a visit by G. Benkart to the Korea Institute for Advanced Study. We express our gratitude to these institutions for their hospitality.
