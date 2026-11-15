---
doc_id: arxiv-0804.0917v1
doc_title: "Composition-Diamond Lemma for Modules ∗"
section_id: sec-006-universal-enveloping-module-for-a-sabinin-algebr
section_title: "Universal enveloping module for a Sabinin algebra"
section_number: null
pages: 11-16
source_pdf: 0804.0917v1.pdf
source_sha256: 887fbd8be47a2781
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.513
doc_brief: "Czechoslovak Mathematical Journal — 19 sections: Page 1; Page 2; Page 3"
duplicate_of: "czechmathj-60-2010-1-4"
---
In this section, we deal with the universal enveloping module for a Sabinin algebra.

::: definition
*([@pe]) A vector space $V$ is called a Sabinin algebra if it is endowed with multilinear operation $\langle;\rangle$: for any $x_1,x_2,\cdots,x_m,y,z\in V$ and any $m\geq0$, $$\langle x_1,x_2,\cdots,x_m;y,z\rangle$$ satisfying the identities $$\begin{aligned}
&& \langle x_1,x_2,\cdots,x_m;y,
z\rangle =-\langle x_1,x_2,\cdots,x_m;z,y\rangle,\\
&& \langle x_1,x_2,\cdots, x_r,a,b,x_{r+1},\cdots,x_m; y,z\rangle
-\langle x_1,x_2,\cdots, x_r,b,a,x_{r+1},\cdots,x_m; y,z\rangle\\
&& \ \  \ \ \ +\sum_ {k=0}^ {r}\sum_ {\alpha}\langle
x_{\alpha_1},\cdots,x_{\alpha_k},\langle
x_{\alpha_{k+1}},\cdots ,x_{\alpha_r};a,b\rangle,\cdots,x_m;y,z\rangle =0,\\
&& \sigma_{x,y,z}(\langle x_1,x_2,\cdots, x_r,x; y,z\rangle+\sum_
{k=0}^ {r}\sum_ {\alpha}\langle
x_{\alpha_1},\cdots,x_{\alpha_k};\langle x_{\alpha_{k+1}},\cdots
,x_{\alpha_r};y,z\rangle,x\rangle) =0,
\end{aligned}$$ where $\alpha$ runs the set of all bijections of the type $\alpha:\
\{1,2,\cdots,r\}\rightarrow \{1,2,\cdots,r\},\ i\mapsto \alpha_i,\
\alpha_1<\alpha_2<\cdots<\alpha_k,\ \alpha_{k+1}<\cdots<\alpha_r,\
r\geq0,\ \sigma_{x,y,z}$ denotes the cyclic sum by $x,y,z$.*
:::

Let $X=\{a_i|i\in \Lambda\}$ be a totally ordered basis of $V$. We define the deg-lex order on $X^*$. Let $\Delta: \ V\rightarrow
V\otimes V$ be a linear map which satisfies: $\Delta(a_i)=1\otimes
a_i+a_i\otimes 1, \ (Id\otimes\Delta)\Delta=(\Delta\otimes Id)\Delta
\mbox{ (coassociative)}\ \mbox{\ and \ if }\  \tau\Delta=\Delta \
\mbox{\ then }\  \tau(x\otimes y)=y\otimes x \ \mbox{
(cocommutative)}$. It is customary to write $\Delta(x)=\sum
x_{(1)}\otimes x_{(2)}$.

Let $T(V)$ be the tensor algebra over $V$ endowed with its natural structure of cocommutative Hopf algebra, that is, $V\subseteq
Prim(T(V))$ (the primitive element of $T(V)$). Let $\langle;\rangle:
T(V)\bigotimes V \bigotimes V\rightarrow V$ be a map. Then we may write the definition of a Sabinin algebra very shortly as $$\begin{aligned}
&&\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \langle x;a,
b\rangle =-\langle x;b,a\rangle,\\
&&\\
 &&\ \ \ \ \ \langle x[a,b]y;
c,e\rangle
+\sum\langle x_{(1)}\langle x_{(2)};a,b\rangle y; c,e\rangle=0,\\
&&\\
&&\ \ \ \ \ \sigma_{a,b,c}(\langle xc; a,b\rangle+\sum\langle
x_{(1)};\langle x_{(2)};a,b\rangle,c\rangle) =0,
\end{aligned}$$ where $[a,b]=ab-ba$.

::: definition
*([@pe]) Let $(V,\langle;\rangle)$ be a Sabinin algebra. Then $$\widetilde{S}(V)=T(V)/span\langle xaby-xbay+\sum x_{(1)}\langle
x_{(2)};a,b\rangle y|x,y\in T(V),a,b\in V\rangle$$ is called the universal enveloping module for $V$.*
:::

Since $T(V)\simeq k\langle X\rangle$ as $k$-algebras, we can view $\widetilde{S}(V)$ as a right $k\langle X\rangle$-module: $$\widetilde{S}(V)=mod\langle X|I\rangle_{k\langle X\rangle},$$ where $I=\{xab-xba+\sum x_{(1)}\langle x_{(2)};a,b\rangle|x\in
X^*,a>b, \ a,b\in X\}.$

Then we have the following theorem.

::: theorem
[]{#t7.1 label="t7.1"} Let $I$ be as above. Then $I$ is the Gröbner-Shirshov basis in $mod\langle X\rangle_{k\langle X\rangle}$.
:::

**Proof:** There are two kinds of compositions: $w_1=xabc\
(a>b>c) \ \mbox{ and } \ w_2=ucdvab\ (c>d,a>b)$. Denote by $$\begin{aligned}
f_1&=&xabc-xacb+\sum(xa)_{(1)}\langle (xa)_{(2)};b,c\rangle,\\
f_2&=&xab-xba+\sum x_{(1)}\langle x_{(2)};a,b\rangle,\\
f_3&=&ucdvab-ucdvba+\sum(ucdv)_{(1)}\langle
(ucdv)_{(2)};a,b\rangle,\\
f_4&=&ucd-udc+\sum u_{(1)}\langle u_{(2)};c,d\rangle.
\end{aligned}$$ Then $$\begin{aligned}
(f_1,f_2)_{w_1}&=&xabc-xacb+\sum x_{(1)}a\langle
x_{(2)};b,c\rangle+\sum
x_{(1)}\langle x_{(2)}a;b,c\rangle\\
&&-xabc+xbac-\sum x_{(1)}\langle
x_{(2)};a,b\rangle c\\
&\equiv&-xcab+\sum x_{(1)}\langle x_{(2)};a,c\rangle b+\sum
x_{(1)}a\langle
x_{(2)};b,c\rangle+\sum x_{(1)}\langle x_{(2)}a;b,c\rangle\\
&&+xbca-\sum x_{(1)}b\langle x_{(2)};a,c\rangle -\sum x_{(1)}\langle
x_{(2)}b;a,c\rangle-\sum x_{(1)}\langle x_{(2)};a,b\rangle c\\
 &\equiv&\sum x_{(1)}c\langle x_{(2)};a,b\rangle+\sum
x_{(1)}\langle
x_{(2)}c;a,b\rangle+\sum x_{(1)}\langle x_{(2)};a,c\rangle b\\
&&+\sum x_{(1)}a\langle x_{(2)};b,c\rangle+\sum x_{(1)}\langle
x_{(2)}a;b,c\rangle -\sum x_{(1)}\langle x_{(2)};b,c\rangle a\\
&&-\sum x_{(1)}b\langle x_{(2)};a,c\rangle-\sum x_{(1)}\langle
x_{(2)}b;a,c\rangle-\sum x_{(1)}\langle x_{(2)};a,b\rangle c\\
&\equiv&\sum x_{(1)}\langle x_{(2)}a;b,c\rangle+\sum x_{(1)}\langle
x_{(2)};\langle x_{(3)};b,c\rangle,
a\rangle+\sum x_{(1)}\langle x_{(2)}b;c,a\rangle\\
&&+\sum x_{(1)}\langle x_{(2)}c;a,b\rangle +\sum x_{(1)}\langle
x_{(2)};\langle x_{(3)};c,a\rangle, b\rangle \\
&&+\sum x_{(1)}\langle x_{(2)};\langle x_{(3)};a,b\rangle,
c\rangle\\
&\equiv&0
\end{aligned}$$ since $\sigma_{a,b,c}(\langle xc; a,b\rangle+\sum\langle
x_{(1)};\langle x_{(2)};a,b\rangle,c\rangle) =0$.

$$\begin{aligned}
(f_3,f_4)_{w_2}&=& ucdvab-ucdvba+\sum u_{(1)}v_{(1)}\langle
u_{(2)}cdv_{(2)};a,b\rangle+\sum u_{(1)}cv_{(1)}\langle
u_{(2)}dv_{(2)};a,b\rangle\\
&&+\sum u_{(1)}dv_{(1)}\langle u_{(2)}cv_{(2)};a,b\rangle+\sum
u_{(1)}cdv_{(1)}\langle
u_{(2)}v_{(2)};a,b\rangle\\
&&-ucdvab+udcvab-\sum
u_{(1)}\langle u_{(2)};c,d\rangle vab\\
&\equiv&-udcvba+\sum u_{(1)}\langle u_{(2)};c,d\rangle vba+\sum
u_{(1)}v_{(1)}\langle u_{(2)}cdv_{(2)};a,b\rangle\\
&&+\sum u_{(1)}cv_{(1)}\langle u_{(2)}dv_{(2)};a,b\rangle+\sum
u_{(1)}dv_{(1)}\langle u_{(2)}cv_{(2)};a,b\rangle\\
&&+\sum u_{(1)}cdv_{(1)}\langle u_{(2)}v_{(2)};a,b\rangle
+udcvba-\sum u_{(1)}v_{(1)}\langle
u_{(2)}dcv_{(2)};a,b\rangle\\
&&-\sum u_{(1)}cv_{(1)}\langle u_{(2)}dv_{(2)};a,b\rangle-\sum
u_{(1)}dv_{(1)}\langle u_{(2)}cv_{(2)};a,b\rangle\\
&&-\sum u_{(1)}dcv_{(1)}\langle u_{(2)}v_{(2)};a,b\rangle+\sum
u_{(1)}v_{(1)}\langle u_{(2)}\langle u_{(3)};c,d\rangle
v_{(2)};a,b\rangle\\
&&+\sum u_{(1)}\langle u_{(2)};c,d\rangle
v_{(1)}\langle u_{(3)}v_{(2)};a,b\rangle-\sum u_{(1)}\langle u_{(2)};c,d\rangle vba\\
 &\equiv&\sum u_{(1)}v_{(1)}\langle
u_{(2)}[c,d]v_{(2)};a,b\rangle+\sum u_{(1)}[c,d]v_{(1)}\langle
u_{(2)}v_{(2)};a,b\rangle\\
&&+\sum u_{(1)}v_{(1)}\langle u_{(2)}\langle u_{(3)};c,d\rangle
v_{(2)};a,b\rangle+\sum u_{(1)}\langle u_{(2)};c,d\rangle
v_{(1)}\langle u_{(3)}v_{(2)};a,b\rangle\\
 &\equiv&\sum(u_{(1)}[c,d]+u_{(1)}\langle
u_{(2)};c,d\rangle)v_{(1)}\langle u_{(3)}v_{(2)};a,b\rangle\\
&&+\sum u_{(1)}v_{(1)}\langle u_{(2)}[c,d]v_{(2)};a,b\rangle+\sum
u_{(1)}v_{(1)}\langle u_{(2)}\langle u_{(3)};c,d\rangle
v_{(2)};a,b\rangle\\
&\equiv&0
\end{aligned}$$ since $\langle x[a,b]y; c,e\rangle +\sum\langle x_{(1)}\langle
x_{(2)};a,b\rangle y; c,e\rangle=0$.

Hence, $I$ is a Gröbner-Shirshov basis in $mod\langle
X\rangle_{k\langle X\rangle}$.  $\square$

: From the above proof, we know that for $\widetilde{S}(V)=mod\langle X|I\rangle_{k\langle X\rangle}$, the minimal Gröbner-Shirshov basis is\
$G=\{xab-xba+\sum x_{(1)}\langle x_{(2)};a,b\rangle|x=a_{i_1}\cdots
a_{i_n}(i_1\leq \cdots\leq i_n,\ n\geq0),a>b, \
 a,b\in X\}$.

  

Now, by Lemma [\[l3.5\]](#l3.5){reference-type="ref" reference="l3.5"} and Theorem [\[t7.1\]](#t7.1){reference-type="ref" reference="t7.1"}, we can easily get the following theorem.

::: theorem
*([@pe], Poincare-Birkhoff-Witt) Let $\{a_i|i\in \Lambda\}$ be a totally ordered basis of $V$. Then $\{a_{i_1}\cdots a_{i_n}|i_1\leq i_2\leq\cdots \leq i_n,\
n\geq0\}$ is a basis of $\widetilde{S}(V)$.*
:::

: The authors would like to express their deepest gratitude to Professor L. A. Bokut for his kind guidance, useful discussions and enthusiastic encouragement. We also thank Professor J. M. Perez-Izquierdo for some remarks.
