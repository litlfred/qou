---
doc_id: arxiv-1108.1048v3
doc_title: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS"
section_id: sec-006-3-explicit-construction-of-irreducible-modules-f
section_title: "Explicit Construction of Irreducible Modules for Finite Classical Type"
section_number: 3
pages: 17-44
source_pdf: 1108.1048v3.pdf
source_sha256: 6f2b83450ba923d0
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.661
doc_brief: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS — We give an explicit construction of irreducible modules ove r Khovanov-Lauda- Rouquier algebras R and their"
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
= \{t_{ij}\}_{ 1 \le i \le n' ,\ p_i \le j \le p_i'}$, where $$\begin{eqnarray*}
 n' &=& \begin{cases} n & \qquad \quad  (\mathsf{A}_n, \mathsf{B}_n, \mathsf{C}_n) \\
 n-1 & \quad  \qquad (\mathsf{D}_n) \end{cases} \\
 p_i &=& \begin{cases}  n+1-i & \qquad  (\mathsf{A}_n, \mathsf{B}_n, \mathsf{C}_n),\\
  n-i & \qquad (\mathsf{D}_n) \end{cases} \\
  p_i' &=& \begin{cases} n & \qquad (\mathsf{A}_n), \\
   n-1+i & \qquad  (\mathsf{B}_n, \mathsf{C}_n, \mathsf{D}_n). \end{cases}
\end{eqnarray*}$$ Set $t_{ij}=0$ except when $1 \le i \le n' ,\ p_i \le j \le p_i'$. For example, if $\mathbf{a}=(2,3,1,0,9,8,4,2,1) \in \mathcal{S}$ for type $\mathsf{B}_3$ and $\mathbf{a}'=(5,2,7,4,3,1,9,6,4,5,3,2) \in \mathcal{S}$ for type $\mathsf{D}_4$, then $t_{1,3}=2$ in $\triangle(\mathbf{a})$, $t_{3,4}=5$ in $\triangle(\mathbf{a}')$ and $$\triangle(\mathbf{a}) =  \newcommand, \quad \quad \ \triangle(\mathbf{a}') =  \newcommand.$$

Let $\tilde{\mathsf{c}}(t_{i,n-1}) = \sum_{k=i}^{n-1} t_{k,n-1}$,  $\tilde{\mathsf{c}}(t_{i,n}) = \sum_{k=i}^{n-1} t_{k,n}$, and $$\begin{align}
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
\end{align}$$

::: proposition
[]{#Prop: S lambda label="Prop: S lambda"} Let $(\mathfrak{A}, \mathsf{P}, \Pi, \mathsf{P}^{\vee}, \Pi^{\vee})$ be a Cartan datum of finite classical type, and let $\lambda = \lambda_1 \Lambda_1 + \cdots + \lambda_n \Lambda_n \in \mathsf{P}^+$. For $\mathbf{a} \in (\mathbb{Z}_{\ge0})^{\ell}$, let $\triangle(\mathbf{a}) = \{t_{ij}\}_{ 1 \le i \le n' ,\ p_i \le j \le p_i'}$ be as above and assume $\mathsf{c}(t_{i,j})$ is as in [\[eq:cdef\]](#eq:cdef){reference-type="eqref" reference="eq:cdef"}. Then $$\begin{align*}
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
\end{align*}$$
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

$$\begin{align*}
\ \ \quad(\mathsf{A}_n) \qquad \qquad &   \overline{1} \succ \overline{2} \succ \cdots \succ \overline{n+1} , \\\quad(\mathsf{B}_n)\qquad \qquad & \overline{1} \succ \overline{2} \succ \cdots \succ \overline{n} \succ 0 \succ n \succ \cdots \succ 2 \succ 1,  \\
\ \ \quad(\mathsf{C}_n) \qquad \qquad &  \overline{1} \succ \overline{2} \succ \cdots \succ \overline{n-1} \succ \overline{n} \succ {n} \succ {n-1} \succ \cdots \succ {1} ,
\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad  \\
\ \ \quad(\mathsf{D}_n) \qquad \qquad & \overline{1} \succ \overline{2} \succ \cdots \succ \overline{n-1} \succ    \overline{n}, n
\succ {n-1} \succ \cdots \succ {1} .
\end{align*}$$ Let $$\begin{align}
 \label{Eq: def of overhat i}
\widehat{\imath} =  \left\{
     \begin{array}{ll}
       \overline{\imath} & \hbox{ if } 1 \le i \le n+1\ \  (\mathsf{A}_n),  \ \ 1 \le i \le n\ \ (\mathsf{B}_n,\mathsf{C}_n,\mathsf{D}_n), \\
       0 & \hbox{ if } i=n+1\ \  (\mathsf{B}_n), \\
       2n+1-i & \hbox{ if } n+1 \le i \le 2n\ \  (\mathsf{C}_n, \mathsf{D}_n), \\
       2n+2-i & \hbox{ if } n+2 \le i \le 2n+1\ \ (\mathsf{B}_n).
     \end{array}
   \right.
\end{align}$$

For $a,b \in \mathbf{B}$ with $a \succ b$, let $\mathbf{i}(a,b)$ be a sequence of elements in $I$ such that $a =  \tilde{f}_{\mathbf{i}(a,b)}b$, and define the irreducible graded $R$-module $$\begin{align}
 \label{Eq: def of nabla}
\Delta_{(a,b)} =  \tilde{f}_{\mathbf{i}(a,b)} \mathbf{1}.
\end{align}$$ Note that $\Delta_{(a,b)}$ in general is not a cuspidal representation given in [@HMM09; @KR09].

**Remark. ** *The set of cuspidal representations is in one-to-one correspondence with the set of positive roots, via correspondence given by the weights of the cuspidal representations. But there are some $\Delta(a,b)$'s which do not correspond to positive roots. For example, in type $\mathsf{B}_n$, the module $\Delta_{(\overline{1},1)} \in R(\sum_{i=1}^n 2\alpha_i)\text{-}  \mathsf{fmod}$ is not a cuspidal representation, since $\sum_{i=1}^n 2\alpha_i$ is not a positive root (see Example [\[Ex: example\]](#Ex: example){reference-type="ref" reference="Ex: example"}).*

The action of the KLR algebra can be described explicitly as follows.

If one of the following holds: $a \succ b$  $(\mathsf{A}_n, \mathsf{C}_n)$, either $b \succeq 0$ or $0 \succeq a$  $(\mathsf{B}_n)$, either $b \succ n-1$ or $\overline{n-1} \succ a$  $(\mathsf{D}_n)$, then the module $\Delta_{(a,b)}$ is the 1-dimensional $R$-module $\mathbb{C}v$ specified by $$x_i v = 0 , \quad \tau_j v = 0, \quad e(\mathbf{i}) v = \left\{
                                                            \begin{array}{ll}
                                                              v & \hbox{ if } \mathbf{i} = \mathbf{i}(a,b),  \\
                                                              0 & \hbox{ otherwise.}
                                                            \end{array}
                                                          \right.$$

If $a \succ 0 \succ b$ for type $\mathsf{B}_n$, then $\Delta_{(a,b)}$ is the 2-dimensional $R$-module $\mathbb{C}u \oplus \mathbb{C}v$ with $R$-action $$\begin{align*}
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
\end{align*}$$ where $d$ is an integer such that $\sigma_{d}(\mathbf{i}(a,b)) = \mathbf{i}(a,b)$.

If $a \succeq \overline{n-1}$ and $n-1 \succeq b$ for type $\mathsf{D}_n$, then the module $\Delta_{(a,b)}$ is the 2-dimensional $R$-module $\mathbb{C}u \oplus \mathbb{C}v$ given by $$\begin{align*}
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
\end{align*}$$ where $d$ is an integer such that $\sigma_{d}(\mathbf{i}(a, n) * \mathbf{i}(n, b)) = \mathbf{i}(a, \overline{n}) * \mathbf{i}(\overline{n}, b)$. Note that $\mathcal{Q}_{n,n-1}(x_{n},x_{n-1}) = \zeta_{n,n-1} \in \mathbb{C}\setminus\{0 \}.$

It follows from the description above that, for $a,b \in \mathbf{B}$ with $a \succ b$, $$\begin{align}
 \label{Eq: cha of nabla}
\mathsf{ ch}\Delta_{(a,b)} = \left\{
                       \begin{array}{ll}
                         \mathbf{i}(a, n) * \mathbf{i}(n, b) + \mathbf{i}(a, \overline{n}) * \mathbf{i}(\overline{n}, b) & \hbox{ if } a \succeq \overline{n-1},\ {n-1} \succeq b\ \ (\mathsf{D}_n), \\
                           2 \mathbf{i}(a,b) & \hbox{ if } a\succ 0 \succ b\ \  (\mathsf{B}_n),\\
                         \mathbf{i}(a,b) & \hbox{ otherwise. }  \\
                       \end{array}
                     \right.
\end{align}$$

**Remark. ** *We see from the expression for the character in [\[Eq: cha of nabla\]](#Eq: cha of nabla){reference-type="eqref" reference="Eq: cha of nabla"} that $\Delta_{(a,b)}$ can be identified with the sequence $\mathbf{i}(a,b)$, or equivalently, with the segment of $\mathbf{B}$ between $a$ and $b$, which is another reason why we defined the Kashiwara operators in the opposite manner to [@KP10; @KL09].*

Given $\mathbf{a} \in \mathcal{S}$ (resp. $\mathbf{a} \in \mathcal{S}^\lambda$) and $i=1,\ldots,n$, let $$\begin{align}
 \label{Eq: nabla}
\Delta(\mathbf{a};i) = \left\{
                            \begin{array}{ll}
                              \overset{n_i}{\underset{j=n+1-i}{\boxtimes}}  \left(\Delta_{(\widehat{n+1-\imath},\ \widehat{\jmath+1})}^{\boxtimes \vartheta_{ij}}\right) &\ \ \hbox{if } \ \ 1 \le i \le n\ \  (\mathsf{A}_n,\mathsf{B}_n,\mathsf{C}_n), \\
                              \Delta_{(\overline{n-1},\ {n})}^{\boxtimes t_{1,n-1}} &\ \  \hbox{if }\ \  i=1\ \  (\mathsf{D}_n),\\
                              \Delta_{(\overline{n-1},\ \overline{n})}^{\boxtimes t_{1,n}} &\ \  \hbox{if }\ \  i= 2 \ \ (\mathsf{D}_n), \\
                              \overset{n_i}{\underset{j=n+1-i}{\boxtimes}}  \left(\Delta_{(\widehat{n+1-\imath},\ \widehat{\jmath+1})}^{\boxtimes \vartheta_{i-1,j}}\right) &\ \  \hbox{if } \ \ 3 \le i \le n \ (\mathsf{D}_n),
                            \end{array}
                          \right.
\end{align}$$ where $n_i= n \ \hbox{\rm for all}\ i\ \ (\mathsf{A}_n)$, $n_i = n+i\ \ (\mathsf{B}_n)$, $n_i = n-1+i\ \ (\mathsf{C}_n, \mathsf{D}_n)$, $\triangle(\mathbf{a}) = \{ t_{i,j} \}$, and

$$\begin{align}
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
\end{align}$$

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
> 2$ for type $\mathsf{D}_n$, then using the description in Proposition [\[Prop: S lambda\]](#Prop: S lambda){reference-type="ref" reference="Prop: S lambda"}, we will obtain $$\begin{align}
  \label{Eq: upper bound for a1}
\mathsf{a}_{n,1} \le \lambda(h)
\end{align}$$ from the following inequalities:

$$\begin{align*}
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
\end{align*}$$

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
            \mathsf{D}_n)$. Then we see that $$\begin{align*}
& \alpha_1(h') = -1,\ \alpha_2(h') = 1, \quad   \alpha_i(h') = 0\ (i=3,\ldots,n) \quad (\mathsf{A}_n), \\
& \alpha_1(h') = -2,\ \alpha_2(h') = 2, \quad \alpha_i(h') = 0\
(i=3,\ldots,n)\quad  (\mathsf{B}_n, \mathsf{C}_n, \mathsf{D}_n).
\end{align*}$$ Proposition [\[Prop: S lambda\]](#Prop: S lambda){reference-type="ref" reference="Prop: S lambda"} implies $$\begin{align}
 \label{Eq:
upper bound for wt u} \mathsf{wt}(u)(h') \le \lambda(h)
\end{align}$$ by the following calculations: $$\begin{align*}
(\mathsf{A}_n): \ \ \mathsf{wt}(u)(h') &= \lambda(h') + t_{n,1} - t_{n,2} \le \lambda(h), \\
(\mathsf{B}_n,\mathsf{C}_n ): \ \ \mathsf{wt}(u)(h') &= \lambda(h') + 2(t_{n,1} + t_{n,2n-1}) - 2(t_{n,2} + t_{n,2n-2}) \\
& = \lambda(h') + 2(t_{n,1} - t_{n,2} -t_{n,2n-2} + 2t_{n,2n-1}) - 2t_{n,2n-1}  \le \lambda(h), \\
(\mathsf{D}_n): \ \
\mathsf{wt}(u)(h') &= \lambda(h') + 2(t_{n,1} + t_{n,2n-2}) - 2(t_{n,2} + t_{n,2n-3}) \\
& = \lambda(h') + 2(t_{n,1} - t_{n,2} -t_{n,2n-3} + 2t_{n,2n-2}) -
2t_{n,2n-2}  \le \lambda(h) .
\end{align*}$$ Since the adapted string of $u$ is $\mathbf{a}_1*\cdots *
\mathbf{a}_{n-1}$, we obtain by the induction hypothesis that $$\begin{align*}
\mathsf{a}_{1,1} + \cdots + \mathsf{a}_{n-1,1} \le (n-1) \mathsf{wt}(u)(h'),
\end{align*}$$ which yields, by $\eqref{Eq: upper bound for a1}$ and $\eqref{Eq:
upper bound for wt u}$, $$\begin{align*}
\mathsf{a}_{1,1} + \cdots + \mathsf{a}_{n-1,1} + \mathsf{a}_{n,1}
\le (n-1) \lambda(h) + \lambda(h) = n \lambda(h).
\end{align*}$$ ◻
:::
