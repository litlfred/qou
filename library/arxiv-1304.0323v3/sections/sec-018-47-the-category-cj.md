---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS"
section_id: sec-018-47-the-category-cj
section_title: "The Category CJ"
section_number: 4.7
pages: 61-65
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
text_source: latex
latex_prose_ratio: 0.61
latex_coverage_ratio: 0.887
---
Since   all the images of $L(a,a+N-1)$  under $\F'$  are isomorphic
to the trivial representation of $\UA$,
 we can localize  $\As/\Ss$  one step further by
using Appendix~ \ref{app:Local_tensor_categories}.

Set
\begin{equation}
L_a\seteq L(a, a+N-1)  \quad \text{and} \quad
  u_a\seteq u(a,a+N-1)\in L_a
\quad\text{for} \  a \in \Z.
\end{equation}
Then $\F(L_a)$ is isomorphic to the trivial representation of
$\UA$.

The following proposition will play a central role in the rest of this section.

\begin{prop}  Let $a,j\in\Z$ and set
\eqn
p&=&(\oep_a-\oep_{a+N},\al_j)-2\delta(a\le j\le a+N-1)\\
&=&-\delta_{j,a}-\delta_{j,a-1}-\delta_{j,a+N-1}-
\delta_{j,a+N}-2\delta(a<j<a+N-1).\eneqn
\bnum
    \item  The image of the morphism $R_{L_a, L(j)_z} \col L_a \circ L(j)_z \to
q^{p} L(j)_z \circ L_a$ is contained in
\eqn q^{p}z^{\delta({a\le j<a+N-1})}L(j)_z \circ L_a.\eneqn
\item  The image of the morphism $R_{L(j)_z, L_a } \col L(j)_z \circ L_a \to
q^{p}L_a \circ L(j)_z$ is contained in
\eqn q^{p}z^{\delta(a<j\le a+N-1)} L_a \circ L(j)_z.\eneqn
\item If $j \neq a-1,a+N $, then the morphisms
$$z^{-\delta(a\le j<a+N-1)}R_{L_a, L(j)_z}\col L_a \circ L(j)_z
\to  q^{\delta_{j,a}-\delta_{j,a+N-1}}L(j)_z \circ L_a$$
and
$$(-1)^{\delta( a < j \le a+N-1 )}z^{-\delta(a< j\le a+N-1)}R_{L(j)_z,L_a }\col
 q^{\delta_{j,a}-\delta_{j,a+N-1}}L(j)_z \circ L_a\to L_a \circ L(j)_z $$
are isomorphisms and the inverses to each other.
\item If $j=a-1$, then
we have  a commutative diagram with an exact row:
$$
\scalebox{.79}{\xymatrix@C=10ex{
0\ar[r]&{ L_a \circ L(a-1)_z\rule[-1.2ex]{0ex}{1.5ex}}
\ar[r]^-{R_{L_a, L(a-1)_z}}\ar@{^{(}->}[dr]&
q^{-1}L(a-1)_z\circ L_a\ar[r] \ar@{>->}[d]^{z^{-1}R_{L(a-1)_z, L_a}}
& q^{-1} L(a-1,a+N-1)\ar[r]&0\\
&&L_a\circ z^{-1}L(a-1)_z\,.}}
$$
\item  If $j=a+N$,
we have  a commutative diagram with an exact row:

\eqn&&\hs{-4ex}
\scalebox{.85}{\xymatrix@C=10ex{
0\ar[r]&{qL(a+N)_z \circ L_a\;\rule[-1.2ex]{0ex}{1.5ex}}\ar[r]^{qR_{L(a+N)_z,L_a}}\ar@{^{(}->}[dr]
& L_a \circ L(a+N)_z \ar[r]
\ar@{>->}[d] ^{-z^{-1}R_{L_a, L(a+N)_z}}&L(a,a+N)\ar[r]&0\\
&&qz^{-1}L(a+N)_z \circ L_a\,.} } \eneqn \ee \enprop
\Proof (i) and
(ii) immediately follow from Lemma~\ref{lem:expliciteR}.

\smallskip
\noi
(iii)\quad For any $j\in \Z$,
 set
$h_j(z)=\prod_{a\le k\le a+N-1, k\not=j}Q_{j,k}(z,0)$.
Then we can easily see  that
$$h_j(z)=\begin{cases}-z^2&\text{if $a<j<a+N-1$,}\\
(-1)^{\delta(j=a+N-1,a+N)}z&\text{if  $j=a-1,a,a+N-1,a+N$,}\\
1&\text{otherwise}
\end{cases}
$$
which can be rewritten as
$$h_j(z)=(-1)^{\delta(a < j \le a+N-1)}z^{\delta(a\le j<a+N-1)+\delta(a<j\le a+N-1)}$$
 for $j \ne a-1, a+N$.
Then Lemma~\ref{lem:ga}~  \eqref{ga6}  implies
\eq
&&
\ba{l}R_{L_a, L(j)_z}\circ R_{L(j)_z,L_a}=h_j(z)\id_{L(j)_z \circ  L_a},
\\[2ex]
 R_{L(j)_z,L_a}\circ R_{L_a, L(j)_z}=h_j(z)\id_{L_a \circ L(j)_z}.
\ea
\label{eq:RR=1}
\eneq
Hence we obtain (iii).

\medskip\noi
(iv)\quad By Lemma~\ref{lem:expliciteR}, we have
$$R_{L_a, L(a-1)_z }(u_a\tens u(a-1)_z)
=\tau_N\cdots \tau_1\bl u(a-1)_z\tens u_a\br.$$

\hs{-1ex} On the other hand, we have
$$(\tau_2\cdots\tau_N)\Bigl(\tau_N\cdots \tau_1\bl u(a-1)_z\tens u_a\br\Bigr)
=\tau_1\bl u(a-1)_z\tens u_a\br,$$ which implies
$$\Img(R_{L_a, L(a-1)_z })=R(  \oep_{a-1} - \oep_{a+N}  )\tau_1\bl u(a-1)_z\tens u_a\br.$$
 Note that we  have $\tau_1^2\bl u(a-1)_z\tens u_a\br=x_1\bl u(a-1)_z\tens u_a\br$.
 Therefore  we obtain
\eqn
&&\Ker\bl L(a-1)_z\circ L_a\to L(a-1,a+N-1)\br\\
&&\hs{2ex}=R(  \oep_{a-1} - \oep_{a+N} )x_1\bl u(a-1)_z\tens u_a\br
+R(  \oep_{a-1} - \oep_{a+N} )\tau_1\bl u(a-1)_z\tens u_a\br \\
&&\hs{2ex}=\Img(R_{L_a, L(a-1)_z }).
\eneqn
The other parts are derived from
$R_{L(a-1)_z, L_a}\circ R_{L_a,L(a-1)_z}=z \id$
which is obtained by \eqref{eq:RR=1}.

\smallskip\noi
(v) is proved similarly to (vi).
\QED

\medskip
Define an abelian group homomorphism
\begin{align*}
c_a \col \rootl_J \rightarrow \Z
\end{align*}
as
\begin{align}
    c_a(\alpha_j) \seteq (\oep_a+\oep_{a+N},\al_j)=
  \begin{cases}
0 & \text{if} \ j \neq a, a-1,a+N-1, a+N, \\
-1 & \text{if} \ j = a-1, \\
1 & \text{if} \ j = a, \\
-1 & \text{if} \ j = a+N-1, \\
1 & \text{if} \ j = a+N.
  \end{cases}
\end{align}

Then, by the preceding proposition,
we obtain a homomorphism
\eq
&&\ba{l}
z^{-\delta(a\le j < a+N-1)-\delta_{j,a+N}}
R_{L_a,L(j)_z}\col L_a\circ L(j)_z\to q^{c_a(\al_j)}
z^{-1}L(j)_z\circ L_a.
\ea\label{eq:int:shift}
\eneq
For $a,j\in\Z$, set
\eq \label{eq:faj}
&&f_{a,j}(z)=(-1)^{\delta_{j,a+N}}z^{-\delta(a\le j<a+N-1)-\delta_{j,a+N}}.
\eneq

Then we  obtain   the following corollary.
\Cor \label{cor:oldR} For any $a,j\in J$, the $R(N+1)$-module homomorphism
$$f_{a,j}(z)R_{L_a,L(j)_z}\col
L_a\circ L(j)_z\To
q^{c_a(\al_j)}z^{-1}L(j)_z\circ L_a$$
induces an isomorphism
$$f_{a,j}(z)R_{L_a,L(j)_z}\col
L_a\circ L(j)_z\To
q^{c_a(\al_j)} L(j)_z\circ L_a$$
in $\Ab/\Sb$.
\encor

\Rem
 To make Corollary~\ref{cor:oldR} hold,
it is enough to take
$$f_{a,j}(z)=cz^{-\delta(a\le j<a+N-1)-\delta_{j,a+N}}$$ for an arbitrary $c\in\cor^{\times}$.
We take $(-1)^{\delta_{j,a+N}}$ as $c$  so  that
(ii) and (iii) in Theorem~\ref{thm:L_a commutes with X} below hold.
\enrem

For $\beta\in \rtl_J^+$, we define commutative algebras
\eqn
&&  \bP_{\beta} \seteq\soplus_{\nu\in J^\beta}\cor[x_1,\ldots, x_\ell]e(\nu)\subset R(\beta), \\
&& K(\beta)\seteq\soplus_{\nu\in J^\beta}\cor[x_1^{\pm1},\ldots, x_\ell^{\pm1}]e(\nu), \text{\ and}\\
&& \KR(\beta)\seteq K(\beta)\tens_{ \bP_{\beta} }R(\beta)\supset  R(\beta),
\eneqn
where $\ell=|\beta|$.
 Set
\eqn
&&f_{a,\beta}=\sum_{\nu\in I^\beta}\prod_{k=1}^{\ell}f_{a,\nu_k}(x_k)e(\nu)
\in K(\beta)\subset \KR(\beta).
\eneqn
It belongs to the center of $\KR(\beta)$.
Hence we may consider $f_{a,\beta}$
as an $R(\beta)$-module endomorphism of
$\KR(\beta)$.

Since
$R(\beta)\simeq
\soplus_{\nu\in J^\beta}(L(\nu_1))_{z_1}\circ \cdots\circ (L(\nu_\ell))_{z_\ell}$,
we can apply the preceding proposition to study $L_a\circ R(\beta)$ and
$R(\beta)\circ L_a$.
Then Corollary~\ref{cor:oldR} yields the following proposition.

\Prop\label{prop:risom}
 For any $\beta\in\rtl_J^+$,
the $R(\oep_a-\oep_{a+N}+\beta)$-module homomorphism
$f_{a,\beta}R_{L_a, R_K(\beta)}\col L_a\circ \KR(\beta)\to
q^{c_a(\beta)}\KR(\beta)\circ L_a$
induces an isomorphism
$$L_a\circ R(\beta)\isoto q^{c_a(\beta)}R(\beta)\circ L_a$$
in $\Ab/\Sb$.
\enprop

\Proof By  Corollary~\ref{cor:oldR},   the assertion holds for
$|\beta|=1$. The general case immediately follows from this since
$\Ab/\Sb$ is a tensor category with the convolution $\circ$ as
tensor product by Proposition \ref{prop:quot tensor}. \QED


Note that the morphism
 $f_{a,\beta}R_{L_a,R(\beta)}\col L_a\circ R(\beta)\isoto q^{c_a(\beta)}R(\beta)\circ L_a$
in  $\Ab/\Sb$
commutes with the right action of $R(\beta)$.

\Lemma
Let $S$ be the automorphism of $P_J=\soplus_{a\in\Z}\Z\oep_a$
given by $S(\oep_a)=\oep_{a+N}$.
We define the bilinear form $B$ on $P_J$ by
\eq
&&B(x,y)=-\sum_{k>0}(S^kx,y)\qtext{for $x,y\in P_J$.}
\label{def:S}
\eneq
Then we have
$$c_a(x)=B(x,\oep_a-\oep_{a+N})-B(\oep_a-\oep_{a+N},x)$$
for any $x\in\rtl_J$.
\enlemma

\Proof
Set
 $\beta_a=\oep_a-\oep_{a+N}$.
Then we have
$$B(\beta_a,x)=-(\oep_{a+N},x).$$
On the other hand, $\sum_{k\in\Z}(x,S^k\beta_a)=0$ implies that
$$B(x,\beta_a)=-\sum_{k>0}(S^kx,\beta_a)
=-\sum_{k>0}(x,S^{-k}\beta_a)=\sum_{k\ge0}(x,S^k\beta_a)=(x,\oep_a).$$
\QED

For $\al\in\rtl^+_J$, set $\As_\al=R(\al)\gmod$ and
$\Ss_\al=\Ss\cap\As_\al$. Then $\Ss_\al$ is a Serre subcategory of
$\As_\al$ and we have
$\As/\Ss=\soplus_{\al\in\rtl^+_J}(\As/\Ss)_\al$, where
$(\As/\Ss)_\al=\As_\al/\Ss_\al$. Then Proposition~\ref{prop:risom}
yields an isomorphism
$$ q^{B(\beta_a,\al)} L_a\circ X\isoto  q^{B(\al,\beta_a)} X\circ L_a$$
in $\As/\Ss$  functorial in $X\in (\As/\Ss)_{\al}$.
\Def
We define the new tensor product
$\nconv\col\Ab/\Sb\times \Ab/\Sb\to\Ab/\Sb$ by
\eqn
X\nconv Y=q^{B(\al,\beta)} X\circ Y\simeq Q^{\tens B(\al,\beta)}\circ X\circ Y,
\eneqn
 where  $X\in(\Ab/\Sb)_{\al},$ $Y\in(\Ab/\Sb)_{\beta}$ and $Q=q\,\one$.
\edf Then $\Ab/\Sb$ as well as $\As/\Ss$ is endowed with a new
structure of tensor category by $\nconv$ as shown in
Appendix~\ref{app:twist}. With this tensor category structure,
Proposition~\ref{prop:risom} can be rephrased as follows.
\Lemma\label{lem:com} For any $a\in J$ and $\beta\in\rtl^+_J$, the
$\bl R(\oep_a-\oep_{a+N-1}+\beta),R(\beta)\br$- bimodule
homomorphism
$$f_{a,\beta}R_{L_a,\KR(\beta)}\col
L_a\nconv \KR(\beta)\To
\KR(\beta)\nconv L_a$$
induces an isomorphism
$$f_{a,\beta}R_{L_a,R(\beta)}\col
L_a\nconv R(\beta)\To
R(\beta)\nconv L_a$$
in $\Ab/\Sb$  which commutes
with  the right actions of $R(\beta)$.
\enlemma


\begin{theorem} \label{thm:L_a commutes with X}
The family $\{L_a\}_{a\in J}$
is a commuting family of central objects in $\As/\Ss$ \ro see
{\rm \S \ref{app:Local_tensor_categories}}\rf.
Namely,  the following statements  hold.
\bnum
\item
$L_a$ is a central object   in  $\As/\Ss$ \ro see
{\rm\S\,\ref{sec:central}}\rf; i.e., \bna
\item
$f_{a,j}(z)R_{L_a,L(j)_z}$ induces an isomorphism in $\As/\Ss$
$$R_a(X)\col L_a\nconv X\isoto X\nconv L_a$$
 functorial in  $X\in\As/\Ss$,
\item the diagram
$$\xymatrix@C=10ex
{L_a\nconv X\nconv Y\ar[r]^{R_a(X)\nconv Y}\ar[dr]_-{R_a(X\nconv Y)\hs{2ex} }&
X\nconv L_a\nconv Y\ar[d]^{X\nconv R_a(Y)}\\
& X\nconv Y \nconv L_a }
$$ commutes in $\As/\Ss$ for any $X,Y\in\As/\Ss$.
\ee
\item The  isomorphism
$R_a(L_a)\col L_a\nconv L_a\isoto L_a\nconv L_a$
coincides with $\id_{L_a\nconv L_a}$ in $\As/\Ss$.
\item
For $a,b\in\Z$,
 the  isomorphisms
\eqn
 R_a(L_b)\col L_a\nconv L_b\isoto L_b\nconv L_a \ \text{and} \ R_b(L_a)\col L_b\nconv L_a\isoto
L_a\nconv L_b
\eneqn

 in $\As/\Ss$ are  the inverses  to each other.
\ee
\enth

\medskip
\noi
\Proof (i)\,(a) follows from Lemma~\ref{lem:com} and the fact that
$L_a\nconv X\simeq\bl L_a\nconv R(\beta)\br\tens_{R(\beta)} X$
and
$X\nconv L_a\simeq\bl R(\beta)\nconv L_a\br\tens_{R(\beta)} X$.

\medskip

\noi
(i)\,(b)
\ For $\beta,\gamma\in\rootl_J^+$  ($|\beta|=\ell, |\gamma| =\ell'$),  we have
\eqn
&&\bl R(\beta) \nconv R_a(R(\gamma))\br \circ \bl R_a(R(\beta))\nconv R(\gamma)\br
\bl u_a\tensor e(\beta) \tensor e(\gamma)\br \\
&&\hs{5ex}= \bl R(\beta) \nconv R_a(R(\gamma))\br
\varphi_{\ell,N} f_{a,\beta}\bl e(\beta) \tensor u_a \tens e(\gamma)\br \\
&&\hs{5ex}=\varphi_{\ell,N} f_{a,\beta}
\bl e(\beta)\tens
\vphi_{\ell',N} f_{a,\gamma}(e(\gamma)\tensor u_a)\br\\
&&\hs{5ex}=\varphi_{\ell+\ell',N}
(f_{a,\beta}  \etens f_{a,\gamma})(e(\beta) \tensor e(\gamma) \tensor u_a)
\eneqn
and
\begin{align*}
&R_a(R(\beta)\nconv R(\gamma))(u_a \tensor e(\beta) \tensor e(\gamma))
= \varphi_{\ell+\ell',N} f_{a,\beta+\gamma} (e(\beta) \tensor e(\gamma) \tensor u_a).
\end{align*}
Since
$$f_{a,\beta+\gamma} e(\beta) \etens e(\gamma)=
(f_{a,\beta} \etens f_{a,\gamma})  e(\beta) \etens e(\gamma),$$
we obtain
$$R_a(R(\beta)\nconv R(\gamma))=\bl R(\beta) \nconv R_a(R(\gamma))\br
\cdot \bl R_a(R(\beta))\nconv R(\gamma)\br.$$

We obtain (i)\,(b) by applying
$\tens_{R(\beta)}X$ and $\tens_{R(\gamma)}Y$
for $X\in\As_\beta$ and $Y\in \As_\gamma$.




\bigskip
If $X \in (\AA /S)_\beta$, we have $R_a(X_z)|_{z=0} = R_a(X)$.
If $|\beta|=\ell$ and $x_1, \ldots, x_\ell$ act by $0$ on $X$, then we have
\begin{align*}
  R_a(X_z)(u_a \tensor x_z) = &
   f_{a,\beta}(z) R_{L_a,X_z}(u_a \tensor x_z)
\end{align*}
for $x \in X$, where $f_{a,\beta}(z) \seteq f_{a,\beta}|_{x_1=\cdots=x_\ell=z}$.

\vs{2ex}\noi
(ii)\quad
When  $X=L_a$,  we have $f_{a,\beta}(z)= z^{-(N-1)}$ and hence
$$R_a(L_a)=R_a((L_a)_z)|_{z=0}=r_{L_a,L_a}=\id_{L_a}$$
by Proposition \ref{prop:exact sequences} (i).


\smallskip\noi
(iii)\quad By (ii), we may assume that $a<b$.
It follows from Lemma \ref{lem:ga}~  \eqref{ga6}  that
$$R_{(L_b)_{z'}, (L_a)_z}\circ R_{(L_a)_z,(L_b)_{z'}}
=\prod_{ \substack{{a} \le i\le a+N-1, \\ {b} \le j\le b+N-1,\,i\not=j} }
Q_{ij}(z,z').$$

Set $\beta_a=\oep_{a}-\oep_{a+N}$
Then
$$
f_{a,\beta_b}(z'-z)\ R_{(L_a)_z,(L_b)_{z'}}
\col(L_a)_z\nconv (L_b)_{z'}\to
(L_b)_{z'}\nconv (L_a)_{z}$$
and
$$
f_{b,\beta_a}(z-z')\ R_{(L_b)_{z'},(L_a)_{z}} \col
(L_b)_{z'}\nconv (L_a)_{z}
\to (L_a)_z\nconv (L_b)_{z'}$$
specialize to
 $R_a(L_b) \colon L_a \nconv L_b \isoto L_b \nconv L_a $ and $R_b(L_a) \colon L_b \nconv L_a \isoto L_a \nconv L_b$.
 Note that $f_{a,\beta_b}(z)=\prod_{j=b}^{b+N-1} f_{a,j}(z)$.
Hence,  to prove our claim,  it is enough to show that
\eq
f_{a,\beta_b}(z'-z)f_{b,\beta_a}(z-z')
\prod_{\substack{{a} \le i\le a+N-1, \\ {b} \le j\le b+N-1,\,i\not=j}}
Q_{ij}(z,z')=1.\label{eq:ffQ}
\eneq

Set
\eqn
A(a,b)&=&\set{i}{a\le i+1\le a+N-1,\; b\le i\le b+N-1}\\
&=&\set{i}{a-1\le i\le a+N-2,\; b\le i\le b+N-1}.
\eneqn
Then we have
$$\prod_{\substack{{a} \le i\le a+N-1, \\ {b} \le j\le b+N-1,\,i\not=j}}
Q_{ij}(z,z')
=(z'-z)^{\sharp A(a,b)}(z-z')^{\sharp A(b,a)}.
$$
 Similarly,  set
$$B(a,b)=\set{i}{a\le i\le a+N,\;i\not=a+N-1,\;b\le i\le b+N-1}.$$
Then we have
$$f_{a,\beta_b}(z'-z)=
(-1)^{\delta(b\le a+N\le b+N-1)}(z'-z)^{-\sharp B(a,b)}.$$
 Therefore,  we obtain
\eqn\sharp A(a,b)-\sharp B(a,b)&=&\delta(b\le a-1\le b+N-1)-\delta(b\le a+N\le b+N-1)\\
&=&\delta(1\le a-b\le N)-\delta(1\le b-a\le N),
\eneqn
 which proves  \eqref{eq:ffQ}.
\end{proof}

By the preceding theorem, $\{(L_a, R_a)\}_{a \in J}$
forms a commuting family
of central objects in $(\AA / \Ss , \nconv)$
( \S\;\ref{app:Local_tensor_categories}).
Following Appendix \ref{app:Local_tensor_categories}, we localize $(\AA / \Ss , \nconv)$ by this commuting family.
Let us denote by  $\T'_J$
the resulting category $(\AA / \Ss)[L_a^{\nconv -1}\mid a\in J]$ .
Let $\Upsilon \colon \AA / \Ss \to \T'_J$ be the  projection functor.
We denote by $\T_J$ the tensor category
$(\As / \Ss)[L_a\simeq\one\mid a\in J]$ and by $\Xi \col
\T'_J \to \T_J$ the canonical functor (see \S\;\ref{app:graded}
and the remark below).
Thus we have a chain of  functors 
$$\As \To[\ {\mathcal Q}\ ]\As/\Ss\To[\ \Upsilon\ ] (\AA / \Ss)[L_a^{\nconv -1}\mid a\in J]
\To[\ \Xi\ ]
(\As / \Ss)[L_a\simeq\one\mid a\in J].$$

\Rem
Note that $\As$, $\As/\Ss$ and $\T'_J$ are $\rtl_J$-graded
(namely, $\T'_J$ has a decomposition $\T'_J=\soplus_{\al\in\rtl_J}(\T'_J)_\al$, etc.).
The category $\T_J$ is $\rtl_{J,N}$-graded   with
$\rtl_{J,N}\seteq\rtl_{J}/\sum_{a\in\Z}\Z\beta_a$,
 where $\beta_a=\eps_a-\eps_{a+N}$.
Note that $\rtl_{J,N}\simeq\soplus_{k=1}^{N-1}\Z\al_k$.


\enrem





\subsection{Rigidity of  the tensor categories  $\T'_J$ and $\T_J$}
In this subsection,
we will show that the tensor category $\T'_J$ is rigid;
i.e., every object in $\T'_J$ has a left dual and a right dual.
 The rigidity of  $\T_J$ follows from this fact.

Let $\ell$ be a  non-negative  integer and $a\in J$. We set
$\beta_a = \oep_a -\oep_{a+N}$ and $\gamma_a=\beta_a -\alpha_a=
\oep_{a+1}-\oep_{a+N}$.  Set
\begin{align*}
  K_\ell(a) \seteq e(\alpha_a,\gamma_a+\ell\beta_a) L_a^{\circ (\ell+1)}
\in R(\gamma_a+ \ell \beta_a) \gmod.
\end{align*}

By the shuffle lemma, we know   $$L_a^{\circ (\ell+1)} = e(\alpha_a, \gamma_a + \ell \beta_a) L_a^{\circ (\ell+1)}.$$
Hence $K_\ell(a)$ is isomorphic to $L_a^{\circ (\ell+1)}$ as a vector space.
For example, we have
$$K_0(a) \simeq L(a+1, a+N-1) \in R(\gamma_a) \gmod.$$
 Let
$$L_\ell(a) \seteq L(a)_z / z^{\ell+1} L(a)_z \in R(\alpha_a) \gmod.$$
We denote by $u_\ell(a)\in L_\ell(a)$ the image of $u(a)_z\in L(a)_z$.

\Prop \label{prop:rigid}
For $\ell\ge 0$,
let us denote by $z$
the  $R(\gamma_a+\ell \beta_a)$-module endomorphism of $K_\ell (a)$
given by the action of $x_1$ on $L_a^{\circ(\ell+1)}$.
Then we have
\bni
\item $z^{\ell+1}=0$,
\item $\Ker z = \Img z^{\ell} = R(\alpha_a, \gamma_a+\ell \beta_a)
  u_a^{\tensor (\ell+1)} \simeq K_0(a) \circ L_a^{\circ \ell}$,
\item $\Ker z^{\ell} = \Img z = R(\alpha_a, \gamma_a+ \ell \beta_a)
R(\ell \beta_a,\beta_a) u_a^{\tensor(\ell+1)} \simeq K_{\ell-1}(a) \circ L_a$.
\ee
\enprop
\Proof
Set
$u = u_a^{\tensor(\ell+1)} \in L_a^{\circ (\ell+1)}.$
Then
$$ R(\alpha_a,\gamma_a+\ell \beta_a) u  \simeq K_0(a) \circ L_a^{\circ \ell},$$
which is an irreducible $R(\gamma_a +\ell \beta_a)$-module
by Corollary~\ref{cor:irred}.
It is obvious that  $R(\alpha_a, \gamma_a + \ell \beta_a) u \subset \Ker z$.


In order to show the converse inclusion, let us prove
\begin{equation}
  \label{eq:nonzero elem in img z ell}
z^{\ell} \tau_1 \cdots \tau_{\ell N} \ u =
 (-1)^\ell (\tau_2 \cdots \tau_N) \ (\tau_{N+2} \cdots \tau_{2N}) \cdots
 (\tau_{(\ell-1) N+2} \cdots \tau_{\ell N}) \ u.
\end{equation}
If $\ell=0$, it is trivial.
Set $a(u,v) = \dfrac{u^\ell-v^\ell}{u-v}$.
Then we have
\begin{align*}
  x_1^\ell \tau_1 \tau_2 \cdots \tau_{\ell N}  \ u
&=\bl \tau_1 x_2^\ell -a(x_1,x_2)\br \tau_2 \cdots \tau_{\ell N} \ u \\
 &= \tau_1 \tau_2 \cdots \tau_N x_{N+1}^\ell \tau_{N+1} \cdots \tau_{\ell N} \ u
 - \tau_2 \cdots \tau_N a(0, x_{N+1}) \tau_{N+1} \cdots \tau_{\ell N} \ u.
\end{align*}
By induction on $\ell$, we obtain
$$x_{N+1}^\ell \tau_{N+1} \cdots \tau_{\ell N} \ u =
x_{N+1}(-1)^{\ell-1}(\tau_{N+2} \cdots \tau_{2N}) \cdots
 (\tau_{(\ell-1) N+2} \cdots \tau_{\ell N}) \ u=0,$$

\begin{align*}
  a(0,x_{N+1}) \tau_{N+1} \cdots \tau_{\ell N} \ u
  &= x_{N+1}^{\ell-1} \tau_{N+1} \cdots \tau_{\ell N} \ u \\
  &=(-1)^{\ell-1} (\tau_{N+2} \cdots \tau_{2N}) \cdots(\tau_{(\ell-1)N+2} \cdots \tau_{\ell N}) \ u,
\end{align*}
 from which we obtain  \eqref{eq:nonzero elem in img z ell}.

\smallskip
Since the right-hand side of \eqref{eq:nonzero elem in img z ell} is
a non-zero element of the simple $R(\gamma_a + \ell \beta_a)$-module
$R(\alpha_a, \gamma_a + \ell \beta_a) u$, we conclude that
$$R(\alpha_a, \gamma_a + \ell \beta_a) u \subset \Ker z \cap \Img z^{\ell}.$$

Consider the following sequence of homomorphisms
$$
 \bl \Ker z^{\ell+1} / \Ker z^{\ell} \br \stackrel{z}{\hookrightarrow}
\bl  \Ker z^{\ell} / \Ker z^{\ell-1} \br\stackrel{z}{\hookrightarrow}
\cdots
 \stackrel{z}{\hookrightarrow} \bl \Ker z^2 / \Ker z \br
 \stackrel{z}{\hookrightarrow} \Ker z.
$$
Since
$\Ker z^{\ell+1} / \Ker z^{\ell} \isoto[z^{\ell}] \Ker z \cap \Img z^\ell$,
we have
$$\dim \bl \Ker z^{k} / \Ker z^{k-1} \br \ge \dim \bl \Ker z^{\ell} / \Ker z^{\ell-1} \br \ge \dim K_0(a) \circ L_a^{\circ \ell}$$
for $1 \le k \le \ell+1$.
Because
\begin{align*}
  \dim K_0(a) \circ L_a^{\circ \ell} = \dfrac{((\ell+1)N-1) !}{(N-1)! (N!)^{\ell}}, \ \text{and} \quad
  &\dim K_\ell(a) = \dfrac{((\ell+1)N )!}{(N!)^{\ell+1}},
\end{align*}
we have
$$\dim \Ker z^{\ell+1} = \sum_{k=1}^{\ell+1} \dim \bl  \Ker z^{k} / \Ker z^{k-1} \br \ge
(\ell+1) \dim K_0(a) \circ L_a^{\circ \ell} = \dim K_\ell (a). $$
It follows that
\begin{align*}
  &K_\ell(a) = \Ker z^{\ell+1},  \\
  &\Ker z^{k} / \Ker z^{k-1} \isoto[z^{k-1}] \Ker z \ \text{for} \ 1 \le \ k \le \ell+1,  \\
  &\Ker z = \Img z^{\ell} \simeq K_0(a) \circ L_a^{\circ \ell}.
  \end{align*}
Hence we get the assertions (i) and (ii).

For (iii), observe that
\begin{align*}
\dim K_{\ell-1}(a) \circ L_a = \ell \ \dim K_0(a) \circ L_a^{\circ \ell} , \\
K_{\ell-1}(a) \circ L_a \simeq R(\alpha_a, \gamma_a + \ell \beta_a) R(\ell \beta_a , \beta_a) u.
\end{align*}
 On the other hand,
$z|_{K_{\ell-1}(a) \circ L_a}$ is induced by
$\bl z|_{K_{\ell-1}(a)} \br  \circ L_a $.
It follows that
$$R(\alpha_a, \gamma_a + \ell \beta_a) R(\ell \beta_a , \beta_a) u \subset \Ker z^{\ell}.$$
Comparing the dimensions, we have
$$R(\alpha_a, \gamma_a + \ell \beta_a) R(\ell \beta_a , \beta_a) u = \Ker z^{\ell}$$
as desired.
\QED
\Cor
There  exist  a surjective homomorphism
\eq \label{eq:rigid surj}
L_\ell(a) \circ K_\ell(a) \twoheadrightarrow L_a^{\circ (\ell+1)},
\eneq
and an injective homomorphism
\eq \label{eq:rigid inj}
 L_a^{\circ (\ell+1)}  \monoto
q^{-\ell-1} K_\ell(a) \circ L_\ell(a)
\eneq in $R\bl (\ell+1)\beta_a
\br \gmod$. \encor \Proof From Proposition \ref{prop:rigid} (i), we
have $x_1^{\ell+1}=0$ on $L_a^{\circ (\ell+1)}$. Hence we obtain
\eqref{eq:rigid surj}. Taking duals, we have by \eqref{eq:dualconv}
\eqn
 \bl L_a^{\circ (\ell+1)} \br^*  \monoto q^{(\gamma_a+\ell \beta_a, \alpha_a)} K_\ell(a)^* \circ L_\ell(a)^*.
\eneqn
Since
\eqn
\bl L_a^{\circ (\ell+1)}\br^* \simeq q^{\ell(\ell+1)} L_a^{\circ (\ell+1)}, \
 K_{\ell}(a)^* \simeq  q^{\ell(\ell+1)}K_{\ell}(a), \ \text{and} \ L_\ell(a)^*\simeq q^{-2\ell}L_\ell(a),
\eneqn
we obtain
\eqref{eq:rigid inj}.
\QED



Note that $B(\al_a,\gamma_a)=B(\al_a,\beta_a)=B(\beta_a,\beta_a)=1$.
Hence we have
\eqn &&L_a^{\nconv(\ell+1)}\simeq q^{\ell(\ell+1)/2}L_a^{\circ (\ell+1)}, \\
   &&L_\ell(a)\nconv K_\ell(a)\simeq q^{\ell+1}L_\ell(a)\circ K_\ell(a).
\eneqn
 From  \eqref{eq:rigid surj}, we have
\eqn
L_\ell(a) \nconv K_\ell(a)
 \epito   q^{\ell+1-\frac{\ell(\ell+1)}{2}}L_a^{\nconv(\ell+1)}.
\eneqn
Set
\eq \tK_\ell(a) \seteq q^{\frac{(\ell+1)(\ell-2)}{2}} K_\ell(a) \nconv L_a^{\nconv -(\ell+1)} \in \T'_J.\eneq
Then we obtain a morphism in $\T'_J$
\eqn
\eps_\ell \col L_\ell(a) \nconv \tK_\ell(a) \longrightarrow \one.
\eneqn
Similarly, from \eqref{eq:rigid inj}, we obtain a morphism
\eqn
\eta_\ell \col \one \longrightarrow \tK_\ell(a) \nconv  L_\ell(a).
\eneqn



\Th
\hfill
\bni
\item The object $\tK_\ell(a)$ is a right dual to $L_\ell(a)$
in the category $\T'_J$ and $(\eps_\ell,\eta_\ell)$ is a
quasi-adjunction  \ro see {\rm \S\;\ref{sec:A}}\rf. 
\item The category $\T'_J$  and  $\T_J$
are rigid tensor categories; i.e., every object   has a right dual
object and a left dual object. \ee \enth \Proof (i)\quad  We shall
prove it by the induction on $\ell$. By interpreting
$\tK_0(a)=L_0(a)=0$, the $\ell=0$ case  is  obvious. Assume that
$\ell>0$. By the definition, we have an exact sequence in $\AA$ \eqn
1 \longrightarrow q^{2\ell} L(a) \longrightarrow L_\ell(a)
\longrightarrow L_{\ell-1}(a) \longrightarrow 0. \eneqn

On the other hand, by Proposition \ref{prop:rigid} (ii) and (iii) we
have  an exact sequence \eq 0 \longrightarrow K_{\ell-1}(a) \circ L_a
\longrightarrow K_\ell(a) \stackrel{z^{\ell}}{\longrightarrow}
q^{-2\ell} K_0(a) \circ L_a^{\circ\ell} \longrightarrow
0.\label{eq:Kexact} \eneq Since $B(\gamma_a,\beta_a)=0$, we have
\eqn &&K_\ell(a)\nconv L_a\simeq q^\ell K_\ell(a)\circ L_a, \\
&&K_0(a) \nconv L_a^{\nconv\ell}\simeq
K_0(a) \circ L_a^{\nconv\ell}\simeq q^{(\ell-1)\ell/2}K_0(a) \circ L_a^{\circ\ell}.
\eneqn
Hence \eqref{eq:Kexact}  can be understood as
\eqn
&&0 \To q^{1-\ell}K_{\ell-1}(a) \nconv L_a \To K_\ell(a) \To[\ {z^\ell}\ ]
q^{-2\ell-(\ell-1)\ell/2} K_0(a) \nconv L_a^{\nconv\ell} \To 0.
\eneqn
Applying the functor $\nconv \bl q^{\frac{(\ell+1)(\ell-2)}{2}} L_a^{\nconv -(\ell+1)}\br $,
we have an exact sequence in $\T'_J$
\eqn
0 \longrightarrow \tK_{\ell-1}(a) \longrightarrow \tK_\ell(a) \longrightarrow q^{-2\ell}\tK_0(a)\longrightarrow 0.
\eneqn

We can easily see that the following diagrams are commutative:
\vskip 0.5em
$\scalebox{.93}{\xymatrix{
L_\ell(a) \nconv \tK_{\ell-1}(a)  \ar[r]  \ar[d]
& L_{\ell-1}(a) \nconv \tK_{\ell-1}(a) \ar[d]_{\eps_{\ell-1}} \\
L_\ell(a) \nconv \tK_\ell (a) \ar[r]^{\eps_{\ell}}
& \one \\
q^{2\ell} L(a) \nconv \tK_{\ell}(a)  \ar[r]  \ar[u]
& q^{2\ell} L(a) \nconv q^{-2\ell} \tK_0(a) \ar[u]^{\eps_0},}}
$\hs{2ex}
$
\scalebox{.93}{\xymatrix{
 \tK_{\ell-1}(a) \nconv L_{\ell-1}(a)  \ar[r]
& \tK_{\ell}(a) \nconv L_{\ell-1}(a)   \\
\one \ar[r]^{\eta_\ell} \ar[d]_{\eta_0} \ar[u]^{\eta_{\ell-1}}
&  \tK_\ell (a) \nconv  L_\ell(a) \ar[u] \ar[d]\\
q^{-2\ell} \tK_0(a) \nconv q^{2\ell} L(a) \ar[r]
& q^{-2\ell} \tK_{0}(a) \nconv L_\ell(a).
}}
$

\vskip 1em
Then the assertion follows by the induction on $\ell$ and Lemma \ref{lem:quasi adjunctions}.

\medskip

(ii) By (i), $L_\ell(a)$ has a right dual for every $a \in \Z$ and $\ell \in \Z_{\ge 0}$.
Hence an object of the form
\eqn
q^s L_{\ell_1}(a_1) \nconv \cdots \nconv L_{\ell_r} (a_r)\nconv S
\eneqn
has a right dual, where $S$ is
a tensor product of copies of  $L_a^{\nconv-1}$ ($a\in\Z)$.

Because every object $X$ in $\T'_J$ has a resolution
\eqn
P'\rightarrow P \rightarrow X \rightarrow 0,
 \eneqn
where $P'$ and $P$ are direct sums of  objects with the above form,
we conclude that $X$ also has a right dual.


Similarly, every object has a left dual.
Note that the left dual of $L(a)$ in $\T_J'$
is isomorphic to $q^{-1} L(a-N+1,a-1) \nconv L_{a-N+1}^{\nconv  -1}$.
\QED


Now we will show that the functor
$\F'\col \AA / \Ss \to \UA \smod$ factors through $\T_J$.
We need the following lemma.

\Lemma
For $b\in J$, set $V_k=V_{q^{2(b-k)}}$  $(1\le k\le N)$,
$W=V_{N}\tens V_{N-1}\tens\cdots \tens V_{1}$,
and choose an epimorphism
$\vphi\col W\to \cor$ in $\UA\smod$.
 Let
$$\Rnorm_{W,V_z}\col W\tens V_z\to V_z\tens W$$
be the R-matrix obtained by the composition of normalized R-matrices
$$V_{N}\tens\cdots \tens V_{1}\tens V_z
\To[\Rnorm_{V_1,V_z}]V_{N}\tens\cdots \tens V_{2}
\tens V_z\tens V_1\To\cdots
\To[\Rnorm_{V_N,V_z}]V_z\tens V_{N}\tens\cdots \tens V_{1},$$
and  let  $g(z)=\dfrac{q^{N-1}(z-q^{2(b-N)})}{z-q^{2(b-1)}}$.

Then we have a commutative diagram
\eq
\xymatrix{
W\tens V_z\ar[r]^{\Rnorm_{W,V_z}}\ar[d]_{\vphi\tens V_z}&V_z\tens W\ar[d]^{V_z\tens \vphi}\\
\cor\tens V_z\ar[r]^{g(z)}& V_z\tens \cor.
}\label{diag:RV}
\eneq
\enlemma
\Proof
Set $W'=V_{1}\tens V_{2}\tens\cdots \tens V_{N}$.
Then there exists a $\UA $-module homomorphism
$r\col W\to W'$ such that $\Img(r)\simeq \cor$.
 Thus   we have a commutative diagram
$$\xymatrix@C=10ex{
W\tens V_z\ar[r]^{\Rnorm_{W,V_z}}\ar[d]_{r\tens V_z}&V_z\tens W\ar[d]^{V_z\tens r}\\
W'\tens V_z\ar[r]^{\Rnorm_{W',V_z}}&V_z\tens W'.
}$$
Since $\Hom_{ \uqpg}(V_z,V_z)=\cor(z)$ and
$\Img(r)\simeq \cor$, there exists $g(z)\in \cor(z)$
such that the diagram \eqref{diag:RV}  is commutative.


Set $c_k=q^{2(b-k)}$ and
choose $\vphi$ such that
$\vphi((u_N)_{c_N}\tens\cdots\tens(u_1)_{c_1})=1$.
 Denote   by
$\Rnorm_k$  the normalized $R$-matrix
$$\Rnorm_k\col V_k\tens V_{k-1}\tens\cdots\tens V_{1}\tens V_z
\to  V_z\tens  V_k\tens V_{k-1}\tens\cdots\tens V_{1}$$
given inductively by $\Rnorm_{V_k, V_z }\cdot(V_k\tens  \Rnorm_{k-1} )$.

It is enough to show that
\eq
&& (V_z \tensor \vphi) \circ\Rnorm_N((u_N)_{c_N}\tens\cdots\tens
(u_1)_{c_1}\tens (u_1)_z)
=g(z)(u_1)_z.\label{eq:phig}
\eneq
We shall show
\eq
&&
\ba{l}\Rnorm_k\bl(u_k)_{c_k}\tens\cdots\tens
(u_1)_{c_1}\tens (u_1)_z\br\\
\hs{3ex}\in  \dfrac{q^{k-1}(z-c_k)}{z-c_1}(u_1)_z\tens (u_k)_{c_k}\tens\cdots\tens
(u_1)_{c_1}+\sum_{1<j\le N}
(u_j)_{ z }\tens  V_{k-1}\tens\cdots \tens V_{1}
\ea
\label{eq:Rk}
\eneq
by induction on $k$.
It is trivial if $k=1$. Assume that $k>1$.
Then by \eqref{eq: RV}, we have
\eqn
\Rnorm\bl(u_k)_{c_k}\tens (u_1)_z\br
&=&\dfrac{q(z-c_k)}{z-q^2c_k}(u_1)_z\tens (u_k)_{c_k}+
\dfrac{z(1-q^2)}{z-q^2c_k}(u_k)_z\tens (u_1)_{c_k}\\
&=&\dfrac{q(z-c_k)}{z-c_{k-1}}(u_1)_z\tens (u_k)_{c_k}+
\dfrac{z(1-q^2)}{z-q^2c_k}(u_k)_z\tens (u_1)_{c_k}
\eneqn
and
$$\Rnorm\bl(u_k)_{c_k}\tens (u_j)_z\br
\in \sum_{1<s\le N} (u_s)_{z}\tens V_{k}  \ \text{for}  \ j>1.$$
Hence we obtain \eqref{eq:Rk}.

 Applying $ V_z \tensor \vphi$, we obtain
$$ (V_z \tensor \vphi) \circ\Rnorm_N\bl(u_N)_{c_N}\tens\cdots\tens
(u_1)_{c_1}\tens (u_1)_z\br
\in g(z)(u_1)_z+\sum_{1<j\le N}\cor (u_j)_z,$$
 which yields  \eqref{eq:phig}.
\QED

\medskip
Now we will choose $\{c_{i,j}(u,v)\}_{i,j \in J}$ as  promised
in Remark \ref{rmk:cij}. For $r \in \Z$, set \eqn A_r(z) =
\begin{cases}
  1 & \text{if $r=0$,} \\
  q^{-r}(z+1-X(r)) & \text{otherwise,}
\end{cases}
\eneqn
where $X(r)=q^{2r}$.
 Set
\eqn
B_r(u,v)=
\begin{cases}
  1 & \quad \text{if $r \le 0$,} \\
q^{-r}(1+v)-q^r(1+u) & \quad \text{if} \ r \ge 1.
\end{cases}
\eneqn

Then, for $r \ge 1$, we have
\eq \label{eq:Br Ar}
B_r(0,z)=A_r(z) \quad \text{and} \quad  B_r(z,0)=-A_{-r}(z).
\eneq




\Th \label{thm:cij}

For $k \in \Z_{\ge 0}$ and  $i,j\in \Z$, set
\eqn
&&c_{k,0}(u,v) =
\prod_{\substack{0\le s\le k,\\s\equiv k\bmod N} }
\dfrac{B_{s}(u,v)B_{s-N}(u,v)}
{B_{s-1}(u,v)B_{s-N+1}(u,v)}, \\
&&
c_{i,j}(u,v) =\bc
 c_{ i-j,0}(u,v) & \text{for $j \le i$,}\\
c_{ j-i,0}(v,u)^{-1} & \text{for $j > i$.}\ec
\eneqn

Then the diagram \eqref{eq:Psi}  is commutative  for  the  functor $\F'\col\As/\Ss\to \UA\smod$
 and  the  commuting family of central  objects  $\{(L_a,R_a)\}_{a\in J}$. That is,
 the diagram
\eq &&\hs{2ex}
\ba{l}\xymatrix@C=8.5ex{
\F'(L_a\nconv M)\ar[d]^-{\F'(R_a(M))}\ar[r]^-\sim
&\F'(L_a)\tens\F'(M)\ar[r]^-{ g_a \tens \F'(M)}
&\cor\tens \F'(M)\ar[dr]\\
\F'(M\nconv L_a)\ar[r]^-\sim&\F'(M)\tens\F'(L_a)\ar[r]^-{\F'(M)\tens
g_a} &\F'(M)\tens  \cor  \ar[r]&\F'(M) }\ea\label{eq:1com} \eneq is
commutative  for any isomorphism $ g_a \col\F'(L_a)\isoto\cor$.
\enth

\Proof
First, one can easily check that $\{c_{i,j}(u,v)\}$ satisfies the condition \eqref{cond:cij}.
It is enough to show the commutativity of the diagram \eqref{eq:1com}
for $M=L(j)_z$. In this case, we have $\F'(M)\simeq V_\aff$.

Set $L=L(a)\circ L(a+1)\circ\cdots\circ L(a+N-1)$
and $W=\F'(L)$.
Then we have
$R_a(L(j)_z)=f_{a,j}(z)R_{L, L(j)_z}$. On the other hand,
Proposition~\ref{prop:image of tau} implies
$$\F'(R_{L, L(j)_z})=\prod_{a\le k\le a+N-1}P_{k,j}(0,z)
\Rnorm_{W,\F'(L (j)_z)}.$$
 The above lemma  implies that
$$\F'\bl R_a(L(j)_z)\br
=f_{a,j}(z)q^{N-1}\dfrac{Z-X(a)}{Z-X(a+N-1)}
\prod_{a\le k\le a+N-1}P_{k,j}(0,z)\id_{V_\aff},$$
where $ Z=z_{V}$ and $Z=X(j)(z+1)$.
Hence it is enough to show that
\eq&&f_{a,j}(z)q^{N-1}\dfrac{Z-X(a)}{Z-X(a+N-1)}
\prod_{a\le k\le a+N-1}P_{k,j}(0,z)=1.
 \label{eq:fajPkj}\eneq
Note that $P_{k,j}(0,z)=c_{k,j}(0,z)(-z)^{\delta(j=k+1)}$. Because
\eqn f_{a,j}(z)= (-1)^{\delta_{j,a+N}} z^{-\delta(a \le j <
a+N-1)-\delta_{j,a+N}}, \eneqn
it amounts to showing that
\eqn \label{eq:ck0z}&&\hs{-5ex}\ba{rcl}
\displaystyle\prod_{k=a}^{a+N-1} c_{k,j}(0,z)&=&
(-1)^{\delta(a+1\le j\le a+N -1)}q^{1-N}
\dfrac{\bl z+1-X(a-j+N-1)\br^{\delta(j\not=a+N-1)}}
{\bl z+1-X(a-j)\br^{\delta(j\not=a)}}\\
&=&
(-1)^{\delta(a < j \le a+N-1)} \dfrac{A_{a-j+N-1}(z)}{A_{a-j}(z)}\ea
\eneqn
for all $a,j \in \Z$.
Since
$ c_{i+1,j+1}(u,v)=c_{i,j}(u,v) $
for all $i,j \in \Z$,  we have only  to show that
\eqn
\displaystyle\prod_{k=a}^{a+N-1} c_{k,0}(0,z)=(-1)^{\delta(a < 0  \le a+N-1)} \dfrac{A_{a+N-1}(z)}{A_{a}(z)}
\eneqn
for all $a \in \Z$.

It is straightforward to show that 
\eqn
\displaystyle\prod_{k=a}^{a+N-1} c_{k,0}(u,v)=
\bc
\dfrac{B_{a+N-1}(u,v)}{B_a(u,v)} & \quad \text{if $a \ge 0$,}\\
\dfrac{B_{-(a+N-1)}(v,u)}{B_{-a}(v,u)} & \quad \text{if $a<1-N$,}\\
\dfrac{B_{a+N-1}(u,v)}{B_{-a}(v,u)} & \quad \text{if $1-N\le a<0$.}
\ec
\eneqn
Then by \eqref{eq:Br Ar}, we  obtain  the desired result.
\QED

\begin{comment}
If $a\ge0$, then we have
\eqn
\prod_{k=a}^{a+N-1} c_{k,0}(u,v)&=&
\prod_{k=a}^{a+N-1}
\prod_{\substack{0\le s\le k,\\s\equiv k\bmod N}}
\dfrac{B_{s}(u,v)B_{s-N}(u,v)}
{B_{s-1}(u,v)B_{s-N+1}(u,v)}\\
&=&\prod_{\substack{0\le s\le a+N-1}}
\dfrac{B_{s}(u,v)}{B_{s-1}(u,v)}\dfrac{B_{s-N}(u,v)}{B_{s-N+1}(u,v)}
=\dfrac{B_{a+N-1}(u,v)}{B_{ -1 }(u,v)}\dfrac{B_{-N}(u,v)}{B_{a}(u,v)}.
\eneqn

If $a\le 1-N$, then we have
\begin{align*}
\displaystyle\prod_{k=a}^{a+N-1} c_{k,0}(u,v)
&=\displaystyle\prod_{k=a}^{a+N-1} c_{-k,0}(v,u)^{-1}
=\Big(\displaystyle\prod_{k=-(a+N-1)}^{-a} c_{k,0}(v,u)\Big)^{-1} \\
&=\Big(\dfrac{B_{-a}(v,u)}{B_{-(a+N-1)}(v,u)}\Big)^{-1}
=\dfrac{B_{-(a+N-1)}(v,u)}{B_{-a}(v,u)}.
\end{align*}


Finally, if $1-N  <   a<0$, then
\begin{align*}
&\displaystyle\prod_{k=a}^{a+N-1}  c_{k,0}(u,v)
=\displaystyle\prod_{k=a}^{-1} c_{-k,0}(v,u)^{-1}
\prod_{k=0}^{a+N-1} c_{k,0}(u,v) \\
&=\Big(\dfrac{B_{-a-1}(v,u)}{B_{-a}(v,u)} \dfrac{B_{-a-2}(v,u)}{B_{-a-1}(v,u)}
\cdots \dfrac{B_{0}(v,u)}{B_{1}(v,u)} \Big)
\Big(\dfrac{B_{0}(u,v)}{B_{-1}(u,v)} \dfrac{B_{1}(u,v)}{B_{0}(u,v)}
\cdots \dfrac{B_{a+N-1}(u,v)}{B_{a+N-2}(u,v)} \Big) \\
&=\dfrac{B_{a+N-1}(u,v)}{B_{-a}(v,u)},
\end{align*}
as desired.
\end{comment}


Hence,  Proposition~\ref{prop:P=1} implies that
the functor $\F' \colon \As/\Ss\to\UA\smod$ factors through
$\T_J$.
Consequently, we obtain a functor $\tF\col \T_J\to \UA\smod$
such that the following diagram quasi-commutes:
\begin{equation}
 \xymatrix@C=10ex{
\As\ar[r]^-{\mathcal Q}\ar[drr]_-{\F}&\As/\Ss\ar[r]^{\Upsilon }\ar[rd]^(.55){\F'}
&\T'_J\ar[d]\ar[r]^{ \Xi  }&\T_J\ar[dl]^-{\tF}\\
&&\UA\smod\,.}
\end{equation}


Moreover, by  Proposition~ \ref{prop:abelian finite2}, we obtain
\begin{prop}
  The functor $\widetilde{\mathcal F}$ is exact.
\end{prop}
\bigskip



\subsection{The Category $\mathcal C_J$} \label{subsec:CJ}
 \hfill


Recall that $\CC_\g$ denotes the category of finite-dimensional
integrable $\UA$-modules. Let $\mathcal C_J$ be the full subcategory
of $\CC_\g$ consisting of $\UA$-modules $M$ such that every
composition factor of $M$ appears as a composition factor of a
tensor product of modules of the form $V(\varpi_1)_{q^{2s}}$ ($s\in
J$).
By the definition, $\mathcal C_J$ is abelian and is stable under
taking submodules, quotients, extensions and tensor products.
Moreover, $\shc_J$ contains $V(\varpi_i)_{(-q)^{i+2s -1}}$ for $1\le
i\le N-1$ and $s\in \Z$. Hence $\tF$ can be considered as an exact
functor
$$\tF\col \T_J\to \mathcal C_J.$$
Note that the category $\mathcal C_J$
 coincides with  the category $\mathcal C_\Z$ in \cite{HL10}.








\Lemma \label{lem:simples in A/S}
Let $\bs=\bl (a_1,b_1), \ldots, (a_r,b_r) \br$
be an ordered multisegment such that $b_k-a_k+1 \le N$ for any $1 \le k \le r$.
Let $t$ be an integer such that $1 \le t \le r$ and $b_t- a_t +1 =N$.
Let us set $\bs'=\bl (a_k,b_k) \br_{k \neq t}$, and let $M(\bs)$ and $M(\bs')$ be the simple graded $R$-modules associated with $\bs$ and $\bs'$, respectively.

Then
$M(\bs') \circ L(a_t,b_t)$ is isomorphic to $M(\bs)$
in $\AA /\Ss$ up to a grading shift.
\enlemma
\Proof
In this proof, we omit the grading shift.  Set
\begin{align*}
  &L = L(a_1,b_1) \circ \cdots \circ L(a_{t-1},b_{t-1}), \\
  &L' = L(a_{t-1},b_{t-1}) \circ \cdots \circ L(a_1,b_1), \\
  &K = L(a_{t+1},b_{t+1}) \circ \cdots \circ L(a_r,b_r), \\
  &K' = L(a_r,b_r) \circ \cdots \circ L(a_{t+1},b_{t+1}).
\end{align*}
Then $M(\bs')$ is isomorphic to the image of $L \circ K \stackrel{f'}{\to} K' \circ L'$   and
$M(\bs)$ is isomorphic to the image of $L \circ L(a_t,b_t) \circ K \stackrel{f}{\to} K' \circ L(a_t,b_t) \circ L'$.
The homomorphism $f$ is decomposed into
\eqn
L \circ L(a_t,b_t) \circ K    &\To[{\hs{3ex} \phi\hs{3ex} }] &  L \circ K \circ L(a_t,b_t) \\
&\To[{\ f' \circ L(a_t,b_t)\ }] & K' \circ L' \circ L(a_t,b_t) \\
&\To[{\hs{2ex} \psi\hs{2ex} }] & K' \circ L(a_t,b_t) \circ L'.
\eneqn
Since $L(a_t,b_t) \circ K \to K \circ L(a_t,b_t)$ and $L' \circ L(a_t,b_t) \to L(a_t,b_t) \circ L'$
are isomorphisms in $\AA /\Ss$ by Proposition \ref{prop:exact sequences}, $\phi$ and $\psi$ are also
isomorphisms in $\AA /\Ss$.
Hence $M(\bs') \circ L(a_t,b_t)$ is isomorphic to $M(\bs)$ in $\AA /\Ss$.
\QED



\Cor \label{cor:C}
If $X$ be a simple object in $\AA /\Ss$, then $X \circ L_a$ is a simple object in $\AA /\Ss$ for any $a \in \Z$.
\encor

\Prop \hfill
\bni
\item The canonical functor
$\Omega  =  \Xi \circ \Upsilon   \colon \AA/\Ss \to \T_J$ sends simple objects to simple objects.


\item $\dim_\cor \Hom_{\T_J}(X,Y) < \infty$ for any $X,Y \in \T_J$.

\item
Let us denote by  $\Irr(\T_J)$ the set of the isomorphism classes of simple objects in $\T_J$.
 Define an equivalence relation $\sim$ on $\Irr(\T_J)$ by $X \sim Y$ if and only if
$X \simeq q^c Y$ in $\T_J$ for some integer $c$.
Let $\Irr(\T_J)_{q=1}$ be a set of representatives of elements in $\Irr(\T_J) / \sim $.

Then the set $\Irr(\T_J)_{q=1}$  is isomorphic to the set of ordered multisegments
$$\bs=\bl (a_1,b_1),\ldots (a_r,b_r) \br$$ satisfying
\begin{equation} \label{eq:segments<N}
  b_k -a_k+1 <N \ \text{for any} \
    1 \le k \le r.
\end{equation}
\item The functor $\tF\col \T_J \to \mathcal C_J$ induces a bijection between $\Irr(\T_J)_{q=1}$ and $\Irr(\mathcal C_J)$, the set of isomorphism classes of irreducible objects in $\mathcal C_J$.
\ee
\enprop
\Proof
(i)  follows from Corollary \ref{cor:C} and  Proposition \ref{prop:abelian finite2}.

\medskip
\noi
(ii) follows from Lemma \ref{lem:finite Hom}.

\medskip

\noi
(iii)\quad
By (i),  every element in $\Irr(T_J)_{q=1}$ is of the form
 $[\Omega( M(\bs))]$, for some ordered multisegment $\bs=\bl (a_1,b_1),\ldots (a_r,b_r) \br$.
 By Lemma \ref{lem:simples in A/S}, we can assume that $\bs$ satisfies \eqref{eq:segments<N}.
Hence the assignment
$\bs \mapsto [\Omega(M(\bs))] \in \Irr(T_J)_{q=1}$ is surjective.

For two multisegments $\bs_1$ and $\bs_2$ satisfying \eqref{eq:segments<N},  if $\Omega(M(\bs_1)) \simeq \Omega(M(\bs_2))$ in $\T_J$
up to  grading shift, then
$\F(M(\bs_1))\simeq \F(M(\bs_2))$ in $\UA\smod$
implies
$\bs_1=\bs_2$ by Theorem~\ref{th:zero} (iii).
Thus we obtain (iii).

\medskip
(iv)\quad By (iii),  for any simple object $X$ in $\T_J$, we have $X
\simeq (\Omega \cdot\mathcal Q) (q^c M(\bs))$ for some ordered
multisegment $\bs$ satisfying \eqref{eq:segments<N} and  some
integer $c$. Then $\tF(X) = \F(M(\bs))$ is irreducible by Theorem
\ref{thm:irreducible to irreducible}.

It is known that every irreducible module in $\mathcal C_J$ can be obtained
as the head of a tensor product of the form
$$V(\varpi_{i_1})_{(-q)^{c_1}}  \tensor \cdots \tensor V(\varpi_{i_r})_{(-q)^{c_r}}
$$
for some $\{c_k \in \Z\}_{1 \le k \le r}$
such that $c_k\equiv i_k-1\mod 2$ and that $(-q)^{c_k-c_j}$ is not the zero of
$d_{V(\varpi_{j}), V(\varpi_{k})}$ for $1\le j<k\le r$.
Moreover, such a sequence $\bl (i_1,c_1),\ldots(i_r, c_r) \br$
is unique up to a permutation (Theorem~\ref{th:zero} (iii)).

Set $a_k=\dfrac{c_k-i_k+1}{2}$ and $b_k=\dfrac{c_k+i_k-1}{2}$.
 By applying a permutation,  we may assume that the
multisegment $\bl(a_1,b_1),\ldots (a_r,b_r)\br$ is ordered. Note
that $(a_j,b_j)\ge(a_k,b_k)$ implies that $(-q)^{c_k-c_j}$ is not
the zero of $d_{V(\varpi_{j}), V(\varpi_{k})}$. Then we have $$\F(
L(a_1,b_1) \circ \cdots \circ L(a_r,b_r)) \simeq
V(\varpi_{i_1})_{(-q)^{c_1}}  \tensor \cdots \tensor
V(\varpi_{i_r})_{(-q)^{c_r}}$$ and $\F(M(\bs))$ is isomorphic to the
head of $V(\varpi_{i_1})_{(-q)^{c_1}}  \tensor \cdots \tensor
V(\varpi_{i_r})_{(-q)^{c_r}}$. Hence the assignment
$\Irr(\T_J)_{q=1} \ni X \mapsto [\tF(X)] \in \Irr(\mathcal C_J)$ is
bijective. \QED


Finally, we have established   one of the main theorems  of this paper.

\Th
The exact functor $\tF\col\T_J\to \mathcal C_J$ induces  a ring  isomorphism
\begin{equation*}
\phi_{\widetilde{\mathcal F}} \col K(\T_J)/(q-1)K(\T_J) \isoto K(\mathcal C_J).
\end{equation*}
\enth
Therefore $\T_J$ may be regarded as  a
$\Z$-graded lifting of the rigid
tensor category ${\mathcal C}_{J}$.


\vskip 0.5em

Recall that the ring $K(\mathcal C_J)$ admits interesting $t$-deformations (\cite{VV02, Nak04, Her04}).
In \cite{HL11}, Hernandez and Leclerc gave a presentation of $\mathcal K_t$, one of those $t$-deformations.
For each simple object $W$ of $\mathcal C_J$, there is a distinguished element
$\chi_{q,t}(W)$ in $\mathcal K_t$,
 and the $\chi_{q,t}(W)$'s form a basis of $\mathcal K_t$
as a $\C(t^{{1/2}})$-vector space. 
Set
$y_{i,0} \seteq \chi_{q,t}(V(\varpi_1)_{q^{2i}})$ and
set $y_{i,m+1}:=\chi_{q,t}(^*W)$, if $y_{i,m}=\chi_{q,t}(W)$ ($m \in \Z$).
Then $\mathcal K_t$ coincides with the $\C(t^{{1/2}})$-algebra  generated by
$\set{y_{i,m}}{i=1,\ldots,N-1, \ m \in \Z}$ with the defining relations
\begin{align}
&\label{eq:R1}\text{for every} \ m \in \Z,  \\
&\quad\nonumber \begin{cases}
y_{i,m} y_{j,m} =y_{j,m}y_{i,m} &\text{if $j \neq i+1, i-1$,} \\
y_{i,m}^2 y_{j,m}  -(t +t^{-1}) y_{i,m} y_{j,m} y_{i,m} + y_{j,m}^2 y_{i,m}=0
&\text{if $j = i+1$ or $i-1$,}
\end{cases} \\
&\label{eq:R2}\text{for every $m \in\Z$, and every 
$i,j \in \{1,2,\ldots, N-1\}$}, \\
&\quad \nonumber y_{i,m} y_{j,m+1} = t^{-2\delta_{i,j}+\delta(i= j+1)+\delta(i= j-1)} y_{j,m+1}y_{i,m}+\delta{(i=j)}(1-t^{-2}),\\
&\label{eq:R3}\text{for every} \ p > m+1, \text{and every} \ i,j \in \{1,2,\ldots, N-1\}, \\
&\quad  \nonumber y_{i,m} y_{j,p} = t^{(-1)^{p-m} (2\delta_{i,j}-\delta(i= j+1)-\delta(i= j-1))} y_{j,p} y_{i,m}.
\end{align}

Note that 
 our generator  $y_{i,m}$ is the element
$x^{\overleftarrow Q}_{i,m-1}$ given in \cite[\S7.1]{HL11}, associated with the quiver $\overleftarrow Q \ : \ 1 \leftarrow 2 \leftarrow \cdots \leftarrow N-1$.

 Set 
$K_{\C(q^{1/2})}(\mathcal T_J)=\C(q^{1/2}) \tens_{\Z[q^{\pm 1}]}K(\mathcal T_J)$. 

\Th \label{th:def}
There is  a  $\C$-algebra isomorphism 
$\psi\colon \mathcal K_t \rightarrow K_{\C(q^{1/2})}(\mathcal T_J)$ sending
\begin{align*}
  t^{1/2} \mapsto q^{-{1/2}}, \quad  y_{i,2k} \mapsto  [L(i+kN)], \quad  y_{i,2k+1} \mapsto  [q^{-1}L(i+kN+1, i+(k+1)N-1)].
\end{align*}
\enth
\Proof
In the proof, we denote by  $Z_{i,2k}$ and $Z_{i, 2k+1}$ 
the objects $L(i+kN)$ and $q^{-1}L(i+kN+1, i+(k+1)N-1)$), respectively.
Note that $Z_{i,m+1}$ is the right dual of $Z_{i,m}$. 
We denote by $z_{i,m}\in K(\mathcal T_J)$ the element $[Z_{i,m}]$.

It is straightforward to check that $\set{z_{i,m}}{i=1\ldots,N-1, \ m \in \Z}$ satisfy the relations
\eqref{eq:R1}--\eqref{eq:R3}.
For example, we have
\begin{align*}
  &z_{i,2k} \nconv z_{i,2k+1}
  =q^{B(\eps_i-\eps_{i+1}, \eps_{i+1}-\eps_{i+N})} z_{i,2k} \circ z_{i,2k+1}
  =q( z_{i,2k} \circ z_{i,2k+1}) \\
  =&-q^2 L_{i+kN} + q^2 z_{i,2k+1}\circ  z_{i,2k} +L_{i+kN} \\
  =&(1-q^2) \one + q^{2-B(\eps_{i+1}-\eps_{i+N},\eps_{i}-\eps_{i+1})}  z_{i, 2k+1} \nconv z_{i,2k}
  =(1-q^2) \one + q^2 z_{i,2k+1} \nconv z_{i,2k},
\end{align*}
which yields the relation \eqref{eq:R2} when $i=j$ and $m=2k$.
Here, the third equality follows 
from Proposition \ref{prop:exact sequences} (vi).
The other relations can be checked similarly.


Note that we have
\eq \label{eq:generate1}
\hs{3ex}\chi_{q,t}(V(\varpi_i)_{(-q)^p}) &=& \frac{t^{-1/2}}{1-t^{-2}}
\Big( \chi_{q,t}(V(\varpi_{i-1})_{(-q)^{p-1}})  \chi_{q,t}(V(\varpi_1)_{(-q)^{p+i-1}}) \\
&& \qquad -t^{-1} \chi_{q,t}(V(\varpi_1)_{(-q)^{p+i-1}}) \chi_{q,t}(V(\varpi_{i-1})_{(-q)^{p-1}}) \Big), \nonumber
\eneq
for all $(i,p) \in \{2,\ldots,N-1\} \times \Z$ such that 
$i \equiv p+1  \mod 2$.
Indeed, if $i=2$, then it is nothing but a consequence of \cite[Proposition 5.6]{HL11}.
The other cases can be also shown by similar arguments. 
 On the other hand, 
 Proposition \ref{prop:exact sequences} (vi) implies that 
 \eq \label{eq:generate2} 
[L(a,b)] = \frac{1}{1-q^2}
\Big( [L(a,b-1)] \nconv [L(b)] 
-q [L(b)] \nconv  [L(a,b-1)] \Big),
\eneq 
for every $a, b \in \Z$ 
 with $0 < b-a+1 <N$. For such a pair $a,b \in \Z$, 
assume that there exists $k \in \Z$ such that $1+kN \le a \le b \le N-1 + kN$.
Then by comparing \eqref{eq:generate1} with \eqref{eq:generate2}  and
arguing by induction on $b-a+1$, 
 we deduce that
\eq \label{eq:fund_seg}
\psi\Big(\chi_{q,t}(V(\varpi_{b-a+1})_{(-q)^{a+b}} \Big) = q^{\frac{b-a}{2}}[L(a,b)]
\eneq 
 if $1+kN \le a \le b \le N-1 + kN$ for some $k\in\Z$.
If there is no such a $k$, then we have 
\eq
&&\text{there exists $s\in\Z$ such that $a\le sN\le b$.}\label{eq:ab}
\eneq

Recall that there is a $\C$-algebra anti-automorphism $d'$ on $\mathcal K_t$ defined by
$d'(t^{1/2})= t^{-1/2}$,
$d'\Big(\chi_{q,t}(V(\varpi_i)_{(-q)^p}) \Big)= \chi_{q,t}(V(\varpi_{N-i})_{(-q)^{p+N}})$ (\cite[\S5.7, \S7.1]{HL11}).
On the other hand, from the duality, we obtain a ring anti-automorphism $d$ on $K(\mathcal T_J)$ given by
$d(q)=q^{-1}$, $d([X])=[^*X]$ 
$(X \in \mathcal T_J)$. 
Then we have 
$d \circ \psi = \psi \circ d'$, by the definition of $\psi$.
For $a,b \in \Z$ with $0 < b-a+1 <N$ and \eqref{eq:ab}, we have
\eqn
 &&\psi\Big(\chi_{q,t}\bl V(\varpi_{b-a+1})_{(-q)^{a+b}}\br\Big) 
=\psi \Big( d'\big(\chi_{q,t}\bl V(\varpi_{N-b+a-1})_{(-q)^{a+b-N}}\br \big) \Big) \\
&=&d\Big(\psi\big(\chi_{q,t}\bl V(\varpi_{N-b+a-1})_{(-q)^{a+b-N}}\br \big) \Big) 
=d\Big( q^{\frac{N-b+a-2}{2}}L(b+1-N,a-1)\Big) \\
&=&q^{\frac{-N+b-a+2}{2}} q^{-1} L(a,b)
=q^{\frac{-N+b-a}{2}} L(a,b),
\eneqn
where the third equality comes from \eqref{eq:fund_seg}.
Hence we have $$\psi(\chi_{q,t}(V(\varpi_{b-a+1})_{(-q)^{a+b}}))\equiv [L(a,b)]$$
for every $a,b \in \Z$ with $0 < b-a+1 < N$,  where $x \equiv y$ means $x= q^{m/2} y$  for some $m \in \Z$.
 Let $\mathcal K_{\C[t^{\pm 1/2}]}$ denote
the $\C[t^{\pm 1/2}]$-subalgebra of $\mathcal K_t$ generated by 
the $\chi_{q,t}(W)$'s, 
where $W$ ranges over 
the set of the isomorphism classes of simple objects of $\mathcal C_J$.
Because  
the $[L(a,b)]$'s generate the $\Z[q^{\pm 1}]$-algebra $K(\mathcal T_J)$,
the  restriction $\tilde\psi$ of $\psi$ to $\mathcal K_{\C[t^{\pm 1/2}]}$
gives the surjective map
$$\tilde\psi\col \mathcal K_{\C[t^{\pm 1/2}]}\epito
\C[q^{\pm1/2}]\tens_{\Z[q^{\pm 1 }]}K(\mathcal T_J).$$
Since  $\tilde\psi$ gives an isomorphism 
$$\mathcal K_{\C[t^{\pm 1/2}]}/(t^{1/2}-1)\mathcal K_{\C[t^{\pm 1/2}]}\simeq
\C\otimes_{\Z}K(\mathcal C_J) \isoto \C\otimes_{\Z} 
\bl K(\mathcal T_J) /(q-1)K(\mathcal T_J))\br$$
after specializing at $t^{1/2}=1$, the homomorphism 
$\tilde\psi$, as well as $\psi$, is an isomorphism. 
\QED
