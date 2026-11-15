---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry"
section_id: sec-013-4-abelian-periods-as-algebraic-integrals
section_title: "Abelian periods as algebraic integrals."
section_number: 4
pages: 47-53
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.987
---
\begin{abst}
 We discuss periods of abelian varieties. Their $p$-adic counterparts 
 live naturally in Fontaine's ring $\matheur{B}_{\mathrm{dR}}$. We present 
 Colmez' construction of abelian $p$-adic periods, which relies on 
 $p$-adic integration and reflects as closely as possible the complex
 picture.
 




 We also deal with the concrete evaluation of elliptic $p$-adic periods.
\end{abst}


\subsection{Over $\C$.}\label{sub-complex-integ}

Let $A$ be an abelian variety over $\C$ of dimension $g$, 
and $\omega_1,\ldots,\omega_g$ a basis of invariant differential forms.






Let $\Lambda$ be the image of the map
\begin{equation*}
 \iota:\mathrm{H}_1(A(\C),\Z)\rightarrow \C^g\; ;\;\; \gamma\mapsto
 \left(\int_{\gamma}\omega_i\right)_i.
\end{equation*}
One has a canonical isomorphism 
\begin{equation*}
\C^g/\Lambda\stackrel{\sim}{\longrightarrow}A(\C).
\end{equation*}
Let us denote the projection $\C^g\rightarrow A(\C)$ by $\mathrm{pr}$.
For any differential one-form $\omega$ of the second kind, one can 
consider a primitive function $f_{\omega}$
of $\mathrm{pr}^{\ast}\omega$; it is meromorphic (univalued) on 
$\C^g$, because all residues of $\omega$ are $0$ by definition, and
it is unique up to addition of an arbitrary constant.
Then $f_{\omega}(z_1+z_2+z_3)-f_{\omega}(z_1+z_2)-f_{\omega}(z_1+z_3)
+f_{\omega}(z_1)$ defines a periodic function on $(\C^g)^3$, hence
induces a meromorphic function on $A(\C)^3$, which we denote by
$F^3_{\omega}$.
Note that the function $F^3_{\omega}$ can also be defined purely
algebraically by the following conditions:
\begin{itemize}
\item $F^3_{\omega}(z_1,0,z_3)=F^3_{\omega}(z_1,z_2,0)=0$.
\item $dF^3_{\omega}=m^{\ast}_{123}\omega-m^{\ast}_{12}\omega
-m^{\ast}_{13}\omega+m^{\ast}_1\omega,$
\end{itemize}
where $m_{123}$ is the addition $A^3\rightarrow A$ sending 
$(z_1,z_2,z_3)$ to $z_1+z_2+z_3$, etc.
For $\gamma\in\mathrm{H}_1(A(\C),\Z)$ the value
$f_{\omega}\bigl(i(\gamma)+a\bigr)-f_{\omega}(a)$ 
does not depend on $a\in\C^g$ ($a$ being chosen so that
$i(\gamma)+a$ and $a$ are not poles of $f_{\omega}$),
and one has the equality
\begin{equation*}
f_{\omega}\bigl(i(\gamma)+a\bigr)-f_{\omega}(a)=
\int_{\gamma}\omega,
\end{equation*}
which describes the period pairing 
\begin{equation*}
\mathrm{H}^1_{\mathrm{dR}}(A)
\times\mathrm{H}_1(A(\C),\Z)\longrightarrow\C
\end{equation*}
(or equivalently, the isomorphism
$\mathrm{H}^1_{\mathrm{dR}}(A)\otimes\C
\stackrel{\sim}{\rightarrow}
\mathrm{H}^1_{\mathrm{B}}(A(\C),\Z)\otimes\C$.)
Here $\mathrm{H}^1_{\mathrm{dR}}(A)$ denotes the first \emph{algebraic}
de Rham cohomology group of $A$, which coincides with the group of 
differential forms of the second kind modulo exact forms.


\subsection{Over the $p$-adics; prolegomena}\label{sub-prolegomena}

If we try to translate this into the $p$-adic setting, one has to face
at once the problem: what is \emph{integration over a loop}?

\begin{para}\label{para-padic-int-1}
 One tentative way is via Berkovich's theory, where loops do exist.  Let us for
 instance consider the Legendre elliptic curve $X_z$. Viewed as a
 $p$-adic space, for $z \in \matheur{D}(0,1^-)\setminus \lbrace 0 \rbrace$
 ($p\neq 2$), this is a Tate curve: $X_z^{\mathrm{an}} \simeq
 {\C}_p^{\times}/q^{\Z}$. The canonical differential
 $\omega_{\mathrm{can}}$ inherited from ${\C}_p^{\times}$ and
 $\frac{dx}{y}$ are proportional:

 \begin{equation*}
 \omega_{\mathrm{can}}=\Theta(z).\frac{dx}{y} \;\text{ with }\;
 1/\Theta(z)=\sqrt{-1}F\Bigl(\frac{1}{2},\frac{1}{2},1;z\Bigr).
 \end{equation*}

 The basic element $\gamma$ of $\mathrm{H}_1(X_z^{\mathrm{an}},{\Z})$
 can be identified with the generator $q$ of $q^{\Z}$, and it is natural
 to set $\int_{\gamma}\omega_{\mathrm{can}}=\int_{0}^q \frac{dt}{t}=
 \log(q)$ (choosing a branch of the $p$-adic logarithm). One then has

 \begin{equation*}
 \omega_2^{(p)}:=\int_{\gamma}^{(p)}\frac{dx}{y} =
 \sqrt{-1}F\Bigl(\frac{1}{2},\frac{1}{2},1;z\Bigr)\log(q).
 \end{equation*}
 This formula, as well as
 \begin{align*}
 & \sqrt{q} =
 \frac{z}{16}
 e^{\frac{F^{\ast}(\frac{1}{2},\frac{1}{2},1;z)}
         {F(\frac{1}{2},\frac{1}{2},1;z)}}\\
 \biggl( & \text{with }F^{\ast}\Bigl(\frac{1}{2},\frac{1}{2},1;z\Bigr)
  = 4\sum_{n>0}\binom{2n}{n}^2 \biggl(\sum_1^{2n} \frac{(-1)^{m-1}}{m}\biggr) 
 \Bigl(\frac{z}{16}\Bigr)^n\biggr)
 \end{align*}
 are the same as those encountered in the complex situation. This leaves
 the open problem: how can one construct ``the other period''
 $\omega_1^{(p)}$, \ie the $p$-adic analogue of
 $\omega_1=2\pi\sqrt{-1}F(\frac{1}{2},\frac{1}{2},1;z)$, since the
 corresponding loop is missing?
\end{para}

\begin{para}\label{para-padic-int-2}
 One simple tentative answer would be to replace the topological
 covering ${\C}_p^{\times}\rightarrow X_z^{\mathrm{an}}$ by other \'etale
 coverings. Natural candidates for this purpose are \'etale coverings of
 order $p^n$, especially those corresponding to torsion points of order
 $p^n$ which are close to the origin.  Let $\zeta_{p^n}$ be a $p^n$th
 root of unity in ${\C}_p^{\times}$ and let $x_n$ be its image in
 $X_z^{\mathrm{an}}$. In the corresponding complex case, taking
 $\zeta_{p^n}=e^{2i\pi/{p^n}}$ would give the right answer
 $p^n\int_{0}^{x_n}\frac{dx}{y}=\omega_1$.  In the $p$-adic case, we get
 instead $p^n\int_{0}^{x_n}\frac{dx}{y}=0$.  Indeed, already in the case
 of the multiplicative group, we have
 $p^n\int_{1}^{\zeta_{p^n}}\frac{dt}{t}=p^n \log(1+(\zeta_{p^n}-1))=0\,$  
 $p$-adically: in other words, $2i\pi$ ``\emph{is missing}''.
\end{para}

\begin{para}[{\itshape Riemann-Shnirelman sums.}]
 It is appropriate to evoke here Shnirel\-man's approach to integration over loops,
 indeed one of the earliest works in $p$-adic analysis. This
 is an adaptation to the $p$-adic case of the computation of integrals by
 Riemann sums
 \begin{align*}
  \frac{1}{2i\pi}\int_{C(a,r)} f(z)dz & = \int_0^1 f(a+re^{2i\pi\theta})
   re^{2i\pi \theta}d\theta
   & = \,\lim_{m\to \infty}\frac{1}{m}\sum_{\zeta^m=1}f(a+r\zeta) r\zeta.
 \end{align*}
 Now, let $a, r \in \C_p$ and let $f$ be a $\C_p$-valued function
 on the circumference
 $C(a,|r|)$.  Let us denote the limit
 \begin{equation*}
  \lim_{m\to \infty}\frac{1}{m}\sum_{\zeta^m=1} f(a+r\zeta).r\zeta 
 \end{equation*}
 symbolically
 by $\int_{C(a,r)} f(z)dz$. For better convergence, Shnirelman actually
 restricted the
 limit to those integers $m$ prime to $p$. In the case of an analytic
 function $f$ on $C(a,|r|)$, this restriction is unnecessary (one can even
 take $m=p^k$) and one has the following analogue
 of Cauchy's theorem of residues (\cf \cite[app.]{paascorw})

 \begin{lem}
  Assume that $f$ is a meromorphic function on $\matheur{D}(a,|r|^+)$,
  and that its poles $z_1,\ldots, z_{\nu}$ all lie in
  $\matheur{D}(a,|r|^-)$. Then $\int_{C(a,r)} f(z)dz$ exists and equals
  $\sum \Res_{z_i} f$.
 \end{lem}

 In the (trivial) special case $f = 1/z$, we get
 $\int_{C(0,1)}dz/z =1$ (not $0$ as
 in \ref{para-padic-int-2}!), but $2i\pi$ is still missing.
\end{para}

\begin{para}
 Actually, there is no way to remedy this if one remains in $\C_p$.  A
 deeper reason for that, due to Tate, is that while
 $\Gal({\ovl{\Q}}_p/{\Q}_p)$ acts on the inverse system of $p^n$th
 roots of unity ($n \geq 0$) through the cyclotomic character $\chi$,
 there is no element $(2i\pi)_p$ in $\C_p$ such that $g((2i\pi)_p)=\chi
 (g) (2i\pi)_p$ for every $g \in \Gal({\ovl{\Q}}_p/{\Q}_p)$.

 \noindent It turns out that $(2i\pi)_p$ is in a sense the only
 ``missing piece'': there is a good theory of $p$-adic periods (due to
 J.M. Fontaine, W. Messing \cite{ppapec}, G. Faltings) which lives in
 some ${\Q}_p$-algebra 
 isomorphic to $\C_p[[(2i\pi)_p]]$, and which we shall now describe in the
 case of abelian varieties.
\end{para}


\subsection{The Fontaine ring $\matheur{B}_{\mathrm{dR}}$.}
\begin{para}
 {\itshape The ring $\matheur{R}$.\ }\index{000R@$\matheur{R}$}
 Let $\mathcal{O}_{\C_p}$ be the ring of
 integers of $\C_p$, \ie $\{x \in \C_p$, $|x|_p \leq 1\}$.  Let us set
 \begin{equation*}
  \matheur{R}:=\underset{x\mapsto x^p}{\limproj}
   \OO_{\C_p},
 \end{equation*}
 \ie $\matheur{R}$ is the set of all series
 $\left(x^{(n)}\right)_{n\in\N}$
 such that $\left(x^{(n+1)}\right)^p=x^{(n)}$.
 This is in fact a ring of characteristic $p$ with 
 \begin{equation*}
  \left(\bigl(x^{(n)}\bigr)+\bigl(y^{(n)}\bigr)\right)^{(n)}=
   \lim_{m\rightarrow\infty}\left(x^{(n+m)}+y^{(n+m)}\right)^{p^m}
 \end{equation*}
 and
 \begin{equation*}
  \left(\bigl(x^{(n)}\bigr)\cdot\bigl(y^{(n)}\bigr)\right)^{(n)}=
   x^{(n)}\cdot y^{(n)}.
 \end{equation*}
 Let $\mathrm{W}(\matheur{R})$ be the Witt ring with coefficients in
 $\matheur{R}$. for $x\in \matheur{R}$, let $[x]$ denote the Teichm\"uller
 representative in $\mathrm{W}(\matheur{R})$.
\end{para}

\begin{para}
 {\itshape The ring $\matheur{B}^+_{\mathrm{dR}}$.\ }
 \index{000bdr+@$\matheur{B}^+_{\mathrm{dR}}$}
 To any element 
 $(x_0,x_1,\ldots,x_n,\ldots)=\sum p^n[x^{p^{-n}}_n]$ in
 $\mathrm{W}(\matheur{R})$, we associate
 \begin{equation*}
 \theta((x_n))=\sum^{\infty}_{n=0}p^nx^{(n)}_n.
 \end{equation*}
 This defines a surjective homomorphism
 $\theta\colon\mathrm{W}(\matheur{R})\rightarrow \OO_{\C_p}$,
 whose kernel is principal.
 It extends to a homomorphism $\theta:
 \mathrm{W}(\matheur{R})\left[\frac{1}{p}\right]\rightarrow\C_p$,
 and $\matheur{B}^+_{\mathrm{dR}}$ is defined as the $(\Ker\theta)$-adic 
 completion
 \begin{equation*}
 \matheur{B}^+_{\mathrm{dR}} :=\lim_{\longleftarrow}
 \mathrm{W}(\matheur{R})\textstyle{\left[\frac{1}{p}\right]}
 \Big/(\Ker\theta)^n.
 \end{equation*}
 By continuity, $\theta$ further extends to a homomorphism $\theta\colon
 \matheur{B}^+_{\mathrm{dR}}\rightarrow\C_p$.
 Then $\matheur{B}^+_{\mathrm{dR}}$ is a complete discrete valuation
 ring with maximal ideal $\Ker\theta$ and residue field $\C_p$.
 Moreover, the Galois group $\Gal(\ovl{\Q_p}/\Q_p)$ acts on 
 $\matheur{B}^+_{\mathrm{dR}}$ in such a way that $\theta$ is equivariant 
 with respect to this Galois action,
 \begin{equation*}
  \Gr^{\bp}\matheur{B}^+_{\mathrm{dR}}\simeq \bigoplus_{r\in \N}\C_p(r),
 \end{equation*}
 where $\Gr^{\bp}$ refers to the filtration by the powers of
 $\Ker\theta$, and where the ``twist'' $(r)$ indicates that the 
 $\Gal(\ovl{\Q_p}/\Q_p)$-action is twisted by the $r$th power of the
 cyclotomic character.

 It turns out that $\matheur{B}^+_{\mathrm{dR}}$ contains naturally a copy of
 ${\ovl{\Q}}_p$ (which $\theta$ maps isomorphically to ${\ovl{\Q}}_p \subset
 \C_p$). More precisely, P. Colmez \cite{lnasddb} has shown that
 $\matheur{B}^+_{\mathrm{dR}}$ is the separated \emph{completion} of
 ${\ovl{\Q}}_p$ with respect to the topology defined by taking
 $\Bigl(p^n\mathcal{O}^{(k)}_{{\ovl{\Q}}_p}\Bigr)_{n,k}$ as a basis of
 neighborhoods of $0$, where $\mathcal{O}^{(k)}_{{\ovl{\Q}}_p}$ denotes
 the subring of ${\ovl{\Z}}_p$ defined inductively as
 \begin{equation*}
 \mathcal{O}^{(0)}_{{\ovl{\Q}}_p}
  ={\ovl{\Z}}_p,\;\mathcal{O}^{(k)}_{{\ovl{\Q}}_p}
  =\Ker\Bigl(d: \mathcal{O}^{(k-1)}_{{\ovl{\Q}}_p}
  \rightarrow
  \Omega^1_{\mathcal{O}^{(k-1)}_{{\ovl{\Q}}_p}/{\Z}_p}\otimes
  {\ovl{\Z}}_p\Bigr).
 \end{equation*}
 It is easy to deduce from this description that
 $\matheur{B}^+_{\mathrm{dR}}$ contains $\widehat{{\Z}_p^{\mathrm{ur}}}$.
\end{para}

\begin{para}
 {\itshape Some remarkable elements of $\matheur{B}^+_{\mathrm{dR}}$.}
 For any $x \in \matheur{B}^+_{\mathrm{dR}}$ such that $|\theta(x)-1|_p< 1$,
 the series $\log(x) = - \sum_{n>0} \frac{(1-x)^n}{n}$ converges in
 $\matheur{B}^+_{\mathrm{dR}}$.  In particular, let $\underline {z} =
 (\ldots,z^{(1)},z^{(0)})$ be an element of $\matheur{R}$ such that $z^{(0)}\in
 {\ovl{\Z}}_p$ or $\widehat{{\Z}_p^{\mathrm{ur}}}$.  Then one can define the
 element \index{000Log@Log}
 $\Log \udl{z} = \log
 \bigl(\frac{z^{(0)}}{[\udl{z}]}\bigr)$\footnote{we follow Colmez' sign 
 convention; Fontaine's $\LOG$ is $\log - \Log$.
 }.
 Note that $\theta(\Log \underline{z})=0$. 

 In the special case where each
 $z^{(n)}=\zeta_{p^n}$ is a primitive $p^n$th root of unity,
 $\Log(\ldots, \zeta_{p^n}, \ldots,1)$ is the element $(2i\pi)_p$ 
 \index{0002ipp@$(2i\pi)_p$}
 we were looking for. This is a generator of $\Ker \theta$, and 
 $\Gal({\ovl{\Q}}_p/{\Q}_p)$ acts on it through the cyclotomic character;
 in other words, we have a $\Gal({\ovl{\Q}}_p/{\Q}_p)$-equivariant
 isomorphism

 \begin{equation*}
 \Gr^{\bp}\matheur{B}^+_{\mathrm{dR}}\;\simeq\; {\C}_p[(2i\pi)_p].
 \end{equation*}
 
 Note that another choice of $(\ldots, \zeta_{p^n},
 \ldots,1)$ changes $(2i\pi)_p$ by multiplication by a unit in ${\Z}_p$.
 Similarly,
 up to addition of an element of $(2i\pi)_p{\Z}_p$, $\Log\;\underline
 {z}\;$ depends only on
 $z^{(0)}$; it is sometimes simply denoted by $\Log\;z^{(0)}$.

 By choosing a double embedding of ${\ovl{\Q}}$ into $\C$ and
 ${\ovl{\Q}}_p$,
 one obtains a canonical element $(2i\pi)_p$, attached to the sequence
 $(\ldots, e^{2i\pi/{p^n}},\ldots,1)$. Similarly, if $z^{(0)}\in
 {\ovl{\Q}}$, then $\Log z^{(0)}$ is 
 well-defined up to addition of an element of $(2i\pi)_p{\Z}$.
\end{para}


\subsection{Colmez' construction of abelian $p$-adic periods.}

Let $A$ be an abelian variety defined over a $p$-adic local field
$K$. The Fontaine-Messing $p$-adic period pairing is a pairing

\begin{equation*}
\int^{(p)}\;:\;\mathrm{H}^1_{\mathrm{dR}}(A) \otimes T_p(A_{\ovl{K}})
 \longrightarrow \matheur{B}^+_{\mathrm{dR}}
\end{equation*}
where $T_p(A_{\ovl{K}}) = \varprojlim \Ker([p^n]: A_{\ovl{K}}\rightarrow
A_{\ovl{K}})$ is the Tate module (a ${\Z}_p$-module of rank $2\dim A$
with $\Gal({\ovl{K}}/K)$-action).

We present Colmez' construction, which is parallel to \ref{sub-complex-integ}.

Let $\omega$ be a differential form on $A$ of second kind, and
$F_{\omega}^3$ the function on $A^3$ determined as in
\ref{sub-complex-integ}.  Then:
\begin{pro}[{\cite[4.1]{ppdva}}]
There exists a locally meromorphic function $F_{\omega}$ on 
$A(\matheur{B}_{\mathrm{dR}})$, unique up to constant, such that:

\begin{enumerate}
 \renewcommand{\theenumi}{\arabic{enumi}}
 \item $dF_{\omega}=\omega$.
 \item $F_{\omega}(z_1+z_2+z_3)-F_{\omega}(z_1+z_2)-
       F_{\omega}(z_1+z_3)+F_{\omega}(z_1)=F^3_{\omega}(z_1,z_2,z_3)$.
 \item If $\omega=dF$, then $F_{\omega}=F$.
\end{enumerate}

\noindent
Moreover, if $\alpha\colon A_1\rightarrow A_2$ is a morphism of abelian 
varieties and $\omega$ is a differential form of second kind on
$A_2$, then $F_{\alpha^{\ast}\omega}=\alpha^{\ast}F_{\omega}$.
\end{pro}

Note that the function $F_{\omega}$ is \emph{not} multivalued; this
fact comes from the following lemma specific to the $p$-adic case:

\begin{lem}[{\cite[4.3]{ufdpplpdvaamc}}]
For any neighborhood $V$ of $0$ in $A(\matheur{B}_{\mathrm{dR}}^+)$, there
exists an open subgroup $U$ of $A(\matheur{B}_{\mathrm{dR}}^+)$ contained in 
$V$ such that $A(\matheur{B}_{\mathrm{dR}}^+)/U$ is a torsion group.
\end{lem}

Take a proper model $\mathscr{A}$ of $A$ over $\OO_{K}$.
Let $\gamma=(\cdots,u_n,\cdots,u_2,u_1=0)\in\mathrm{T}_p(A_{\ovl{K}})$ 
with each $u_n\in\mathscr{A}(\OO_{\C_p})$, and choose
$a_n\in\mathscr{A}(\matheur{B}^+_{\mathrm{dR}})$ so that neither
$a_n$ nor $a_n+_A\widehat{u}_n$ is close to a pole of $\omega$.
For suitable liftings 
$\widehat{u}_n\in\mathscr{A}(\matheur{B}^+_{\mathrm{dR}})$ of 
$u_n$ (\ie $\theta(\widehat{u}_n)=u_n$), the following holds. 

\begin{thm}[{\cite[5.2]{ufdpplpdvaamc}}]
The limit 
\begin{equation*}
 \oint^{(p)}_{\gamma}\omega \;:=\;
 \lim_{n\rightarrow\infty}p^n\bigl(F_{\omega}(a_n)-F_{\omega}
 (a_n+_A\widehat{u}_n)\bigr)
\end{equation*}
converges to an element in $\matheur{B}^+_{\mathrm{dR}}$, and it defines
a non degenerate bilinear pairing
\begin{equation*}
 \oint^{(p)}\;:\;
 \mathrm{H}^{1}_{\mathrm{dR}}(A)\otimes
 \mathrm{T}_p(A_{\ovl{K}})\longrightarrow\matheur{B}_{\mathrm{dR}}^+,
\end{equation*}
compatible with the Galois action and the filtrations.
\end{thm}

\begin{rem}
 On composing the period pairing $\int^{(p)}$ with $\theta$, one gets a
 bilinear map $\mathrm{H}^1_{\mathrm{dR}}(A) \otimes T_p(A_{\ovl{K}})
 \longrightarrow \C_p$ which sends $\Omega^1(A)\subset
 \mathrm{H}^1_{\mathrm{dR}}(A)$ to $0$.  This degenerate pairing
 describes ``half'' of the (Hodge)-Tate-Raynaud decomposition
 \begin{equation*}
  \mathrm{H}^1_{\mathrm{et}}(A_{\ovl{K}},{\Q}_p)\otimes {\C}_p \simeq
   \Omega^1(A)\otimes
   {\C}_p(-1) \oplus \mathrm{H}^1(\mathcal{O}(A))\otimes {\C}_p
 \end{equation*}
 of $\Gal({\ovl{K}}/K)$-modules.
\end{rem}



\subsection{Some computations of elliptic $p$-adic periods.}
\label{sub-computation}

\begin{para}{\itshape Tate elliptic curves.\ }
In this case, $T_p(A_{\ovl{K}})$ sits in an exact sequence 
\begin{equation*}
 0\rightarrow {\Z}_p(1)\rightarrow T_p(A_{\ovl{K}}) \rightarrow
  {\Z}_p \rightarrow 0.
\end{equation*}
Let us take for $\gamma_1$ the image of $(2i\pi)_p \in {\Z}_p(1)$ in
$T_p(A_{\ovl{K}})$, and for $\gamma_2$ any lifting of $1 \in {\Z}_p$.
For concreteness, let $A=X_z$ be in Legendre form as in
\ref{para-padic-int-1}.  Let $\eta \in \mathrm{H}^1_{\mathrm{dR}}$
satisfy $\an{\omega,\eta}=1$ (\eg $\frac{xdx}{4y}$).  We set
$\omega^{(p)}_i=\int^{(p)}_{\gamma_i}\omega,
\eta^{(p)}_i=\int^{(p)}_{\gamma_i}\eta$.  Then one has the ``Legendre
relation''
\begin{equation*}
\omega^{(p)}_1\eta^{(p)}_2-\eta^{(p)}_1\omega^{(p)}_2=(2i\pi)_p
\end{equation*}
and the formulas (\cf \cite{pbl}, \cite{get})
\begin{equation*}
\frac{\omega^{(p)}_1}{(2i\pi)_p} = \sqrt{-1}F\Bigl(\frac{1}{2},
\frac{1}{2},1;z\Bigr) = 1/\Theta(z), \;\; \omega^{(p)}_2 =
\sqrt{-1}F\Bigl(\frac{1}{2},\frac{1}{2},1;z\Bigr) \Log q
\end{equation*}
(compare with the complex case in \ref{para-tate-para}, and also
\cite[p.406]{f2}).  Note that the ``period'' we found in
\ref{para-padic-int-1} by integration along the Berkovich loop is
 \emph{not} a Fontaine-Messing period (there is a $\log$ instead of
 $\Log$).
\end{para}

\begin{para}{\itshape Elliptic curves with ordinary reduction.\ }
We now assume that $z\in {\Z}_p^{\mathrm{ur}}$ and that $A=X_z$ has good
ordinary reduction (with the notation of \subsecref{sub-dwork-hyper},
this means that $z(1-z)h_p(z)\neq 0$).  Again, $T_p(A_{{\ovl{\Q}}_p})$
sits in an exact sequence (\cite[A.2.4]{alraec})
\begin{equation*}
0\rightarrow {\Z}_p \gamma_1\rightarrow
T_p(A_{{\ovl{\Q}}_p}) \rightarrow T_p(A\;\mathrm{mod}\, p) \rightarrow 0.
\end{equation*}
 Then one still has the formula $\Theta(z)=
\frac{(2i\pi)_p}{\omega^{(p)}_1}$, where $\Theta(z)\in
\widehat{{\Z}_p^{\mathrm{ur}}}$ is the Tate constant discussed in
\ref{para-tate-para} (compare \cite{pbl}, \cite[4.3]{itoecwcm}).  In
particular, $\frac{\omega^{(p)}_1}{(2i\pi)_p}$ is given by the
evaluation at $z$ of ``the'' extension of
$F(\frac{1}{2},\frac{1}{2},1;?)$ discussed in \subsecref{sub-serre-tate-para}.

\noindent On the other hand, let $\gamma_2 \in T_p(A_{{\ovl{\Q}}_p})$ be
such that the Weil pairing $\an{\gamma_1,\gamma_2}\in {\Z}_p(1)={\Z}_p
(2i\pi)_p$ is the chosen generator $(2i\pi)_p$. Then one has the
``Legendre relation'', and $\omega^{(p)}_2 = \omega^{(p)}_1\cdot\frac{{\Log
\;q}}{{(2i\pi)_p}}$, where $q\in \widehat{{\Z}_p^{\mathrm{ur}}}$ denotes
here the so-called {\it Dwork(-Serre-Tate) parameter} of $A$ introduced
in \ref{para-dwork-para}.  If $q=1$, \ie when $A$ is the \emph{canonical
lifting} of $A\pmod{p}$, then one can choose $\gamma_2\;$ such the
corresponding value of ${\Log 1}$ is $0$, and then $\omega^{(p)}_2 =0.$
\end{para}
