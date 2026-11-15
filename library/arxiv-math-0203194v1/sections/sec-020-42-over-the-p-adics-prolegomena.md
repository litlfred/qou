---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-020-42-over-the-p-adics-prolegomena
section_title: "Over the $p$-adics; prolegomena"
section_number: 4.2
pages: 47-51
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.981
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub-prolegomena}

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
