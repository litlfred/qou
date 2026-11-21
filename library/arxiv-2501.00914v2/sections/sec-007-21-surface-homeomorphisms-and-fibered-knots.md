---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-007-21-surface-homeomorphisms-and-fibered-knots
section_title: "Surface homeomorphisms and fibered knots"
section_number: 2.1
pages: 5-8
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.979
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
Let $h:\Sigma\to\Sigma$ be a homeomorphism of a compact oriented surface  with possibly empty boundary. By Thurston's classification \cite{thurston-diffeomorphisms}, $h$ is  isotopic rel boundary to a map $\varphi:\Sigma\to\Sigma$ such that
\begin{itemize}
\item there exists a possibly empty \emph{reducing system} $\Gamma \subset \Sigma$ consisting of a finite disjoint union of simple closed curves which is fixed setwise by $\varphi$;
\item if $S$ is a component of $\Sigma\setminus \Gamma$ and $n$ is the smallest positive integer such that $\varphi^n(S) = S$, then $\varphi^n|_S$ is freely isotopic to a periodic or pseudo-Anosov map. When $n=1,$  we  refer to  this map and $S$ as a periodic or pseudo-Anosov component of $h$ or $\Sigma \setminus \Gamma$, accordingly.
\end{itemize}
We will assume that $\Gamma$ is minimal with respect to inclusion, in which case it  is unique up to isotopy \cite[Theorem~C]{blm} and is called the \emph{canonical reducing system} for $h$. We  refer to the pair $(\varphi,\Gamma)$ as the \emph{Nielsen--Thurston form} of $h$.

We will focus hereafter on the Nielsen--Thurston forms of monodromies of fibered knots in $S^3$ and their associated \emph{closed monodromies}; we spend some time below establishing notation, terminology, and some preliminary results specific to that setting.

Let $K\subset S^3$ be a fibered knot with fiber surface $\Sigma$ and monodromy \[h:\Sigma\to \Sigma.\] Then  $\Sigma$ has one boundary component and $h$ restricts to the identity on $\partial\Sigma$. Following \cite{hkm-veering},   $h$ is said to be  \emph{right-veering} if for every properly embedded arc $\alpha \subset \Sigma$, either $\alpha$ and $h(\alpha)$ are isotopic rel boundary, or  $h(\alpha)$ is  to the right of $\alpha$ near each endpoint after these arcs are isotoped to intersect minimally. We say simply that $h$ is  \emph{veering} if either $h$ or $h^{-1}$ is right-veering.

Let $(\varphi, \Gamma)$ be the Nielsen--Thurston form of $h$. The suspension of $\Gamma$ in the mapping torus of $\varphi$ is a collection of incompressible tori in the knot complement $S^3 \setminus \nu(K)$. The complement of these tori consists of Seifert fibered pieces swept out by the periodic components of $\Sigma\setminus \Gamma$, and hyperbolic pieces swept out by the pseudo-Anosov components \cite{thurston-fiber}. 

Let  $\Sigma_0$ be the component of $\Sigma \setminus \Gamma$ containing $\partial \Sigma$; we call this the \emph{outermost} component of $\Sigma \setminus \Gamma$.  Note that  $\varphi$ fixes $\Sigma_0$ setwise, and its restriction to $\Sigma_0$ is  freely isotopic to a map  \[\varphi_0: \Sigma_0 \to \Sigma_0\] which is either periodic or pseudo-Anosov. The \emph{fractional Dehn twist coefficient} \cite{hkm-veering} \[c(h)\in \Q\]  records the amount of twisting near $\partial \Sigma$ in this free isotopy, giving a measure of how veering $h$ is.  (If $\varphi_0$ is pseudo-Anosov, then $1/c(h)$ is the \emph{degeneracy slope} \cite{gabai-oertel} of the suspension flow of $\varphi_0$.)  When the outermost component is pseudo-Anosov, we have the following \cite[\S3]{hkm-veering}:

\begin{theorem} \label{thm:fdtc-veering}
If $\varphi_0$ is pseudo-Anosov, then $h$ is veering if and only if $c(h)\neq 0$.
\end{theorem}

Moreover, using work of Gabai \cite{gabai-problems}, Kazez--Roberts showed  \cite[Theorem~4.5]{kazez-roberts} that these twist coefficients are highly constrained for monodromies of fibered knots in $S^3$: 

\begin{proposition}\label{prop:0-or-1/n}
If $K \subset S^3$ is a fibered knot with monodromy $h$, then  $|c(h)|<1$.
\end{proposition}

It follows from the discussion above that $K$ is hyperbolic if and only if  the outermost map $\varphi_0$ is pseudo-Anosov and $\Gamma = \emptyset$. In the periodic case, we have the following, cf.\ \cite[Theorem~2]{budney-jsj}:

\begin{proposition}\label{prop:periodic-cable}
If  $\varphi_0$ is periodic, then either
\begin{itemize}
\item $\Gamma = \emptyset$ and $K$ is a $(p,q)$-torus knot, or 
\item $\Gamma \neq \emptyset$ and either
\begin{itemize}
\item $K$ is a composite knot and $\Sigma_0$ is a planar surface, or
\item $K$ is a $(p,q)$-cable knot of some other knot in $S^3$ and $\Sigma_0$ has genus $g(T_{p,q})$.
\end{itemize}
\end{itemize}
In each case above, $q \geq 2$ and $\gcd(p,q) = 1$.
\end{proposition}

\begin{proof}
The first case is due to Seifert \cite{seifert}; the second is a special case of \cite[Proposition~4.2]{kazez-roberts}.  The statement of that proposition did not include the case where $K$ is composite, but  the proof allows for the possibility that a closed orbit in the mapping torus of $\phi_0$ is a meridian of $K$. In this case, Kazez--Roberts  show that $c(h) = 0$, which implies that $\phi_0$ restricts to the identity on $\partial \Sigma\subset \Sigma_0$. It then follows from \cite[Lemma~2.6]{bns}, which is  really an application of \cite[Lemma~1.1]{jiang-guo}, that $\phi_0$ is the identity on all of $\Sigma_0$.  But then the outermost piece of the JSJ decomposition of $S^3 \setminus \nu(K)$, given by the mapping torus of $\phi_0$, is simply $Y_0=\Sigma_0 \times S^1$.  From here, \cite{budney-jsj} says that $\Sigma_0$ must be a planar surface with at least three boundary components, and that  $K$ is a connected sum of the  nontrivial knots whose complements are the connected components of $(S^3\setminus \nu(K)) \setminus Y_0$.
\end{proof}

Let $\hat\Sigma = \Sigma\cup D$ be the closed surface obtained by capping off the fiber of $K$ with a disk, and let \[\hat h:\hat\Sigma\to\hat\Sigma\] be the map obtained by extending the monodromy $h$ by the identity over the capping disk $D$. We call $\hat h$  the \emph{closed monodromy} of $K$; note that its mapping torus  is $S^3_0(K)$. Let \[\hat\Sigma_0 = \Sigma_0 \cup D.\] Let $(\hat\varphi,\hat\Gamma)$ be the  Nielsen--Thurston form of $\hat h$. The Nielsen--Thurston forms of $h$ and  $\hat h$ can be very different in general (for instance, they can be freely isotopic to pseudo-Anosov and periodic maps, respectively), but this is ruled out under some mild hypotheses: 

\begin{theorem} \label{thm:rv-fill-monodromy}
If the monodromy $h$ is veering and $\Sigma_0$ is not a pair of pants, then
\begin{itemize}
\item $\hat\Gamma\subset \Gamma$ and $\varphi$ agrees with $\hat\varphi$ on $\Sigma\setminus \Sigma_0 = \hat\Sigma\setminus\hat\Sigma_0$;\vspace{1mm}
\item if $\varphi_0$ is periodic, then the pseudo-Anosov components of $\Sigma\setminus\Gamma$ and $\hat\Sigma\setminus\hat{\Gamma}$ are equal; \vspace{1mm}
\item if $\varphi_0$ is pseudo-Anosov, then $\hat\Gamma= \Gamma$ and the restriction of $\hat\varphi$ to $\hat\Sigma_0$ is freely isotopic to a pseudo-Anosov map  $\hat\varphi_0$ which agrees with   $\varphi_0$ on $\Sigma_0$ and fixes one point $p$ in $D$.
\end{itemize}
\end{theorem}

In brief, the hypothesis that $h$ is veering guarantees that if $\varphi_0$ is pseudo-Anosov then its stable and unstable invariant foliations have at least two prongs on $\partial \Sigma$. This implies that  $\Sigma_0$ caps off to a pseudo-Anosov component with one additional fixed point in the capping disk while the other components are unchanged. The hypothesis  that $\Sigma_0$ is not a pair of pants guarantees that if $\varphi_0$ is periodic then capping off preserves all pseudo-Anosov components. This theorem will be crucial for understanding  the fixed points of the pseudo-Anosov components of the closed monodromies of L-space knots and more generally ffpf knots in our proof of Theorem \ref{thm:zero-surgery-fpf}.

\begin{proof}[Proof of Theorem \ref{thm:rv-fill-monodromy}]
We first show that $\varphi_0$ extends to a map \[\hat\varphi_0: \hat\Sigma_0 \to \hat\Sigma_0\] of the same type (periodic or pseudo-Anosov) as $\varphi_0$. If $\varphi_0$ is periodic, then it rotates $\partial \Sigma$ by some rational multiple of $2\pi$, and we simply extend this rotation radially across the disk $D$ to define $\hat\varphi_0$. 

Now suppose that $\varphi_0$ is pseudo-Anosov.  By definition, this means that there is a pair of transverse singular measured  foliations $(\cF_s,\mu_s)$ and $(\cF_u,\mu_u)$ of $\Sigma_0$, called the \emph{stable} and \emph{unstable} foliations of $\varphi_0$, such that
\[ \varphi_0(\cF_s,\mu_s) = (\cF_s,\lambda^{-1}\mu_s) \quad\text{and}\quad \varphi_0(\cF_u,\mu_u) = (\cF_u,\lambda\mu_u), \]
for some real number $\lambda > 1$. The interior singularities of these foliations  have  at least 3 \emph{prongs}, and  each of these foliations has some number $n \geq 1$ of \emph{boundary prongs} ending on $\partial \Sigma \subset \partial \Sigma_0$. Since  $\varphi_0$ preserves the boundary prongs, the fractional Dehn twist coefficient of $h$ is given by  \[c(h) = k/n\] for some integer $k$; see \cite[\S3.2]{hkm-veering}. Since $h$ is veering, Theorem~\ref{thm:fdtc-veering} says that $k\neq 0$. Meanwhile, Proposition~\ref{prop:0-or-1/n} implies that $|k|<n$. It follows that $n\geq 2$. In this case,  $\varphi_0$ extends  to a pseudo-Anosov homeomorphism $\hat\varphi_0$ of $\hat\Sigma_0$, and $\cF_s$ and $\cF_u$ extend to stable and unstable foliations $\hat\cF_s$ and $\hat\cF_u$ for $\hat\varphi_0$ in which the $n$ boundary prongs extend to $n$ prongs meeting at point $p$ in $D$. The point $p$ is a singularity of these two foliations when $n\geq 3$, and a smooth point when $n=2$; see Figure \ref{fig:prongs}. Note  that $p$ is the unique fixed point of $\hat\varphi_0$  in $D$.

(For the reader interested in more details about how one extends the foliations and transverse measures over the disk $D$, we take the following easy way out: a pseudo-Anosov homeomorphism of a surface with boundary is, by definition, a map which restricts on the complement of the boundary to a pseudo-Anosov map of the corresponding punctured surface. Capping off a boundary component from this point of view corresponds simply to filling in the corresponding puncture with a point.)


\begin{figure}[ht]
\begin{tikzpicture}[every path/.style={thin}]
\foreach \i in {2,3,4} { \coordinate (center\i) at (4*\i,0); }


\begin{scope} 
{ \tikzset{every path/.style={}}
\clip (center2) circle (1.5); }
\foreach \j in {-6,...,6} { \draw[red] (center2) ++ (-2,0.3*\j) -- ++(4,0); }
\foreach \j in {-6,...,6} { \draw[blue] (center2) ++ (0.3*\j,-2) -- ++(0,4); }
\end{scope}


\begin{scope} 
{ \tikzset{every path/.style={}}
\clip (center3) circle (1.5); }
\foreach \j in {0,120,240} {
  \draw[red] (center3) -- ++(\j:2);
  \foreach \n in {2,4,...,10} {
    \draw[red] ($(center3)+(\j:2)+(\j+90:0.075*\n)$) .. controls ($(center3)+(\j+60:0.1*\n-0.1/\n)$) .. ($(center3)+(\j+120:2)+(\j:0.075*\n)$);
  }
}
\foreach \j in {60,180,300} {
  \draw[blue] (center3) -- ++ (\j:2);
  \foreach \n in {2,4,...,10} {
    \draw[blue] ($(center3)+(\j:2)+(\j+90:0.075*\n)$) .. controls ($(center3)+(\j+60:0.1*\n-0.1/\n)$) .. ($(center3)+(\j+120:2)+(\j:0.075*\n)$);
  }
}
\end{scope}


\begin{scope} 
{ \tikzset{every path/.style={}}
\clip (center4) circle (1.5); }
\foreach \j in {0,90,180,270} {
  \draw[red] (center4) -- ++(\j:2);
  \foreach \n in {3,6,...,18} {
    \draw[red] ($(center4)+(\j:2)+(\j+90:0.03*\n+0.1/\n)$) .. controls ($(center4)+(\j+45:0.1*\n-0.3/\n)$) .. ($(center4)+(\j+90:2)+(\j:0.03*\n+0.1/\n)$);
  }
}
\foreach \j in {45,135,225,315} {
  \draw[blue] (center4) -- ++ (\j:2);
  \foreach \n in {3,6,...,18} {
    \draw[blue] ($(center4)+(\j:2)+(\j+90:0.03*\n+0.1/\n)$) .. controls ($(center4)+(\j+45:0.1*\n-0.3/\n)$) .. ($(center4)+(\j+90:2)+(\j:0.03*\n+0.1/\n)$);
  }
}
\end{scope}


\foreach \i in {2,3,4} {
\draw[very thick] (center\i) circle (1.5);
\draw[black,fill=black] (center\i) circle (0.05);
}


\end{tikzpicture}
\caption{The transverse foliations $\hat\cF_s$ and $\hat\cF_u$ on $D$, in the cases where $\cF_s$ and $\cF_u$ each have $n=2,3,4$ boundary prongs.  When $n=2$ the point $p$ at the center is a smooth point of each foliation, while for $n\geq 3$ it is an $n$-pronged singular point.} \label{fig:prongs}
\end{figure}

It follows in either case that $\Gamma$ is a reducing system for $\hat h$ as well, and thus contains $\hat\Gamma$. Moreover, $\hat\varphi$ is the extension of $\varphi$ by the identity over $D$, and in particular agrees with $\varphi$ on \[\Sigma \setminus \Sigma_0 = \hat\Sigma \setminus \hat\Sigma_0,\] proving the first item of the theorem. For the other items, we analyze the difference $\Gamma \setminus \hat\Gamma$.
 
We first claim that $\Gamma\setminus \hat\Gamma$ consists of components of $\partial \hat\Sigma_0$. Indeed, $\hat\varphi$ fixes $\Gamma$ and thus $\partial \hat\Sigma_0$ setwise. It follows that $\hat\Gamma\cup \partial \hat\Sigma_0\subset \Gamma$ is also a reducing system for $\hat h,$ and hence for $h$ as well. But then the minimality of $\Gamma\subset \Sigma$ as the canonical reducing system for $h$ implies that \[\Gamma = \hat\Gamma \cup \partial \hat\Sigma_0,\] which proves our claim about $\Gamma\setminus \hat\Gamma$.

We next claim that every component of $\Gamma$ is homotopically essential in $\hat\Sigma$, and that no two components of $\Gamma$ are freely homotopic in $\hat\Sigma$. Indeed, the analogous conditions hold for $\Gamma \subset \Sigma$ by the minimality of this reducing system, and the only way this fails upon capping off is if $\hat\Sigma_0$ is a disk or an annulus;  equivalently, if $\Sigma_0$ is an annulus or a pair of pants.  Minimality of $\Gamma\subset \Sigma$ rules out the first possibility, while the second is excluded  by the hypotheses of the theorem. 

We now use these two claims to prove the rest of the theorem.   The third item follows from what we have already established if we can show that $\hat\Gamma = \Gamma$ when $\varphi_0$ is pseudo-Anosov, or equivalently if we can show that $\hat\Gamma \neq \Gamma$ implies that $\Sigma_0$ is not a pseudo-Anosov component of $\Sigma\setminus \Gamma$. 

Let us therefore assume that  $\hat\Gamma \neq \Gamma$.  Let $\hat\Sigma_1$ be the component of $\hat\Sigma\setminus \hat\Gamma$ containing $\hat\Sigma_0$. By the first claim,  this must be a proper containment, and we can write \[\hat\Sigma_1=\hat\Sigma_0 \cup S_1\cup \dots \cup S_k,\] where  $S_1,\dots,S_m$ are some components of $\Sigma\setminus \Gamma$   adjacent to $\Sigma_0$. For the third item in the theorem, it suffices to show that $\Sigma_0$ is not a pseudo-Anosov component, as discussed; for the second item, it suffices to show that none of the $S_j$ are pseudo-Anosov components. We  prove both at once.

Each $S_j$ shares some boundary component $\gamma$ with $\hat\Sigma_0$. Some power $(\hat\varphi)^n$ restricts to a map on $\hat\Sigma_1$ which is freely isotopic either to the identity or to a pseudo-Anosov map. Since  $\hat\varphi$ fixes $\Gamma$ setwise and $\gamma$ is a component of $\Gamma$, we can also assume that $(\hat\varphi)^n$ fixes  $\gamma$. But the second claim implies that $\gamma$ is homotopically essential and not boundary parallel in $\hat\Sigma_1,$ which means that $(\hat\varphi)^n|_{\hat\Sigma_1}$ is not freely isotopic to a pseudo-Anosov map; it is therefore freely isotopic to the identity. But then $(\hat\varphi)^n$ restricts to maps on $\hat\Sigma_0$ and $S_j$ which are  both freely isotopic to the identity. 

Now, the restrictions of $(\hat\varphi)^n$ and $\varphi^n$ to $S_j$ agree since  $\varphi = \hat\varphi$ outside of $D$. It follows that $\varphi^n|_{S_j}$ is freely isotopic to the identity, and hence that $S_j$ is a periodic component of $\Sigma\setminus \Gamma$.  We can also conclude that $\Sigma_0$ is a periodic component of $\Sigma\setminus \Gamma$. Indeed, if it is not then $\varphi_0$ is   pseudo-Anosov, in which case the same is true of $\hat\varphi_0$, as we showed at the beginning of the proof. This would imply that the restriction of $(\hat\varphi)^n$ to $\hat\Sigma_0$ is freely isotopic to a pseudo-Anosov map, but we have just shown that it is freely isotopic to the identity, a contradiction.
It follows that $\Sigma_0$ and $S_j$ are both periodic components of $\Sigma\setminus \Gamma$, completing the proof of the theorem.
\end{proof}

\begin{corollary} \label{cor:not-veering}
If  $K \subset S^3$ is a fibered hyperbolic knot such that  $S^3_0(K)$ is not hyperbolic, then its monodromy is not veering.
\end{corollary}

\begin{proof}
The monodromy $h:\Sigma\to \Sigma$ of $K$ is freely isotopic to a pseudo-Anosov map $\varphi_0$. In this case, $\Sigma_0 = \Sigma$ is not a pair of pants, since it has connected boundary.  Then $h$ is not veering; otherwise, Theorem \ref{thm:rv-fill-monodromy} would imply that $\hat\varphi_0$ is also pseudo-Anosov, which would imply that $S^3_0(K)$, the mapping torus of $\hat h$, is hyperbolic.
\end{proof}
