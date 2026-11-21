---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-009-3-the-coend-for-module-categories
section_title: "The (co)end for module categories"
section_number: 3
pages: 10-15
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.908
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
\label{Section:mcoends}

In this Section we recall the notion of \textit{relative (co)ends}; a tool developed in \cite{BM} in the context of representations of tensor categories, generalizing the well-known notion of (co)ends in category theory.


\medbreak
 Let $\ca$ be a  tensor category and $\Mo$ be a left $\ca$-module category. Assume that $\Ac$ is a category and $S:\Mo^{\op}\times \Mo\to \Ac$ is a functor equipped with natural isomorphisms
\begin{equation} \beta^X_{M,N}: S(M,X\triangleright N)\to S(X^*\triangleright M,N),
\end{equation}
for any $X\in \ca, M,N\in \Mo$. We shall say that $\beta$ is a \textit{prebalancing} of the functor $S$. Sometimes we shall say that it is a $\ca$-\textit{prebalancing}, to emphasize the dependence on $\ca$.

\begin{defi} The \textit{relative end} of the pair $(S,\beta)$ is an object $E\in \Ac$ equipped with dinatural transformations $\pi_M: E\xrightarrow{ . .} S(M,M)$ such that 


\begin{equation}\label{dinat:end:module:left}
\pentagonC
{S(M,M)}
{S(\mathrm{ev}_X^{op}\triangleright\mathrm{id}_M,\mathrm{id}_M)}
{S((X^*\triangleright X)\triangleright M, M)}
{S(m_{X^*,X,M}^{op} ,  \mathrm{id}_M) \vphantom{{{X^X}^X}^X}} 
{S(X^*\triangleright(X\triangleright M), M)}
{\beta^X_{X\triangleright M,M}}
{S(X\triangleright M,X\triangleright M)}
{\pi_{X\triangleright M}}
{E}
{\pi_{ M}}
\end{equation}
for any $X\in \ca, M\in \Mo$, and is universal with this property. This means that, if $\widetilde{E}\in \Ac$ is another object with dinatural transformations $\xi_M:\widetilde{E}\xrightarrow{ . .} S(M,M)$, such that they fulfill \eqref{dinat:end:module:left}, there exists a unique morphism $h:\widetilde{E}\to E$ such that $\xi_M= \pi_M\circ h $.
\end{defi}
The relative end depends on the choice of the prebalancing. We will denote the relative end as $\oint_{M\in \Mo} (S,\beta)$, or sometimes simply as $\oint_{M\in \Mo} S$, when the prebalancing $\beta$ is understood from the context.


\smallbreak
The \textit{ relative coend} of the pair $(S,\beta)$ is defined dually. This  is an object $C\in \Ac$ equipped with dinatural transformations $\pi_M:S(M,M)\xrightarrow{ . .} C$ such that


\begin{equation}\label{dinat:coen:module:left} 
\pentagonABxBCxCDxDExAE
{S(M,M)}
{S(\mathrm{id}_M,\mathrm{coev}_X\triangleright\mathrm{id}_M)}
{S(M,(X^*\otimes X)\triangleright M)}
{S(\mathrm{id}_M, m_{X,X^*,M})\vphantom{{{X^X}^X}^X}} 
{S(M,X\triangleright (X^*\triangleright M))}
{\beta^X_{M,X^*\triangleright M}}
{S(X^{*}\triangleright M,X^*\triangleright M)}
{\pi_{X^*\triangleright M}}
{C}
{\pi_M}
\end{equation}
for any $X\in \ca, M\in \Mo$, universal with this property. This means that, if $\widetilde{C}\in \Ac$ is another object with dinatural transformations  $\lambda_M: S(M,M) \xrightarrow{ . .} \widetilde{C}$ such that they satisfy \eqref{dinat:coen:module:left}, there exists a unique morphism $g:C\to \widetilde{C}$ such that $g \circ \pi_M=\lambda_M$. The relative coend will be denoted  $\oint^{M\in \Mo} (S,\beta)$, or simply as $\oint^{M\in \Mo} S$.

\medbreak


A similar definition can be made for \textit{right} $\ca$-module categories. Let $\Ac$ be a category, and $\No$ be a right $\ca$-module category endowed with a functor $S:\No^{\op}\times \No\to \Ac$ with a \textit{prebalancing}
$$ \gamma^X_{M,N}: S(M\triangleleft X, N)\to S(M, N\triangleleft {}^* X),$$
for any $M,N\in \No$, $X\in \ca$. 
\begin{defi} The \textit{relative end} for $S$ is an object $E\in \Ac$ equipped with dinatural transformations  $\lambda_N:E\xrightarrow{ .. } S(N,N)$ such that 
\begin{equation}\label{dinat:end:module:right}
\pentagonD
{S(N,N)}
{ S(\mathrm{id}_N,\mathrm{id}_N \triangleleft \,\mathrm{ev}_X)}
{S(N,N\triangleleft (X\otimes {^*}X))}
{S(\mathrm{id},\mathrm{id}\otimes m^{-1}_{N,X,{}^* X} )}
{S(N,(N\triangleleft X)\triangleleft {^*}X)}
{\gamma^X_{N,N\triangleleft X}}
{S(N\triangleleft X,N\triangleleft X)}
{\lambda_{N\triangleleft X}}
{E}
{\lambda_N}
\end{equation}
for any $N\in \No$, $X\in \ca$. We shall also denote this relative end by $\oint_{N\in \No} (S, \gamma)$.

Similarly, the \textit{relative coend} is an object $C\in \Bc$ with dinatural transformations $\lambda_N: S(N,N)\xrightarrow{ .. } C$  such that



\begin{equation}\label{dinat:coend:module:right}
\pentagonBAxBCxCDxDExAE
{S(N,N)}
{S(\mathrm{id}_N  \triangleleft\, \mathrm{coev}_X^{op},\mathrm{id}_N)}
{S(N  \triangleleft  ({^*}X\otimes  X),N)}
{S(m^{-1\,op}_{N, {^*}X, X}, \mathrm{id}_N)}
{S((N  \triangleleft  {}^*X)\triangleleft X,N )}
{\gamma^X_{N  \triangleleft  {^*}X, N}}
{S(N  \triangleleft  {^*}X,N  \triangleleft  {}^* X)}

{\lambda_{N  \triangleleft  {^*}X}}
{C}
{\lambda_N}
\end{equation}
for any $N\in \No$, $X\in \ca$. We shall also denote this relative coend by $\oint^{N\in \No} (S, \gamma)$.
\end{defi}


In the next Proposition we collect some results about the relative (co)end that will be useful.  The reader is referred to \cite[Prop. 3.3]{BM}, \cite[Prop. 4.2]{BM}.

\begin{prop}\label{compilat-r} Assume  $\Mo, \No$ are  left $\ca$-module categories, and $S, \widetilde{S}:\Mo^{\op}\times \Mo\to \Ac$ are functors equipped with $\ca$-prebalancings $$\beta^X_{M,N}: S(M,X\triangleright N)\to S(X^*\triangleright M,N),$$ $$ \widetilde{\beta}^X_{M,N}: \widetilde{S}(M,X\triangleright N)\to \widetilde{S}(X^*\triangleright M,N),$$ $X\in \ca, M,N\in \Mo$. The following assertions holds
\begin{itemize}

\item[(i)] Assume that the module ends $\oint_{M\in \Mo} (S,\beta), \oint_{M\in \Mo} (\widetilde{S},\widetilde{\beta})$ exist and have dinatural transformations $\pi, \widetilde{\pi}$, respectively. If  $\gamma:S\to \widetilde{S}$ is a natural transformation  such that 
\begin{equation}\label{gamma-ind}
 \widetilde{\beta}^X_{M,N} \gamma_{(M,X\triangleright N)}=\gamma_{(X^*\triangleright M,N)} \beta^X_{M,N},
\end{equation}
then there exists a unique map $\widehat{\gamma}: \oint_{M\in \Mo} (S,\beta)\to \oint_{M\in \Mo} (\widetilde{S},\widetilde{\beta})$ such that   $$\widetilde{\pi}_M \widehat{\gamma}= \gamma_{(M,M)} \pi_M$$ for any $M\in \Mo$. If $\gamma$ is a natural isomorphism, then  $\widehat{\gamma}$ is an isomorphism.


\item[(ii)] For any pair of $\ca$-module functors $(F, c), (G, d):\Mo\to \No,$ the functor $$\Hom_{\No}(F(-), G(-)): \Mo^{\op}\times \Mo\to \vect_\ku$$
has a canonical prebalancing  given by
\begin{equation}\label{beta-for-hom}
 \beta^X_{M,N}: \Hom_{\No}(F(M), G(X\triangleright N))\to \Hom_{\No}(F(X^*\triangleright M), G(N))
\end{equation}
$$ \beta^X_{M,N}(\alpha)= (ev_X\triangleright \id_{G(N)}) m^{-1}_{X^*,X,G(N)} (\id_{X^*}\triangleright d_{X,N}\alpha)c_{X^*,M},$$
for any $X\in \ca, M, N\in \Mo$.
There is an isomorphism $$ \Nat_{\!m}(F,G)\simeq \oint_{M\in \Mo} (\Hom_{\No}(F(-), G(-)), \beta).$$\qed
\end{itemize}
\end{prop}
The next result will be needed later. It follows from a combination of \cite[Prop. 3.3]{BM} (ii) and \cite[Lemma 3.6]{BM}.
Let $\Mo$ be a left $\ca$-module category, then $\No=\Mo^{\op}$ is a right $\ca$-module category with right action given by
$$M \triangleleft X= X^*\triangleright M.  $$
 Assume $\Ac$ is a category equipped with a functor
$$S:\No^{\op}\times \No\to \Ac,$$
together with a prebalancing
$$\beta^X_{M,N}: S(M \triangleleft X, N)\to S(M,N \triangleleft {}^*X).$$
The functor
$$\Hom_\Ac(S(-,-), U):\Mo^{\op}\times \Mo\to \vect_\ku, $$
has a natural prebalancing 
$$ \gamma^X_{M,N}:\Hom_\Ac(S(M, N\triangleleft {}^* X), U)\to \Hom_\Ac( S(M\triangleleft X, N),U),$$
$$\gamma^X_{M,N}(f)=f\circ \beta^X_{M,N}.$$
The proof of the next statement is similar to the proof of \cite[Prop. 3.3 (ii)]{BM}.
\begin{prop}\label{int-hom} If the coend  $\oint_{M\in \No} (S,\beta)$ exists, then for any object $U\in \Ac$,  the end $\oint_{M\in \Mo} \Hom_\Ac( S( -, -), U)$ exists, and there is an isomorphism
$$\oint_{M\in \Mo} \Hom_\Ac(S( -, -),U)\simeq  \Hom_\Ac( \oint^{M\in \No} (S,\beta), U).$$
Moreover, if $\oint_{M\in \Mo} \Hom_\Ac(S( -, -),U)$ exists for any $U\in \Ac$, then the coend $\oint^{M\in \No} (S,\beta)$ exists.\qed
\end{prop}

The proof of the next result is completely analogous to the proof in the case of usual coend.

\begin{lema}\label{right-exact-on-coend} Let $\Mo$ be a right $\ca$-module category, $S:\Mo^{\op}\times \Mo\to \ac$ a functor equipped with a prebalancing $\gamma$. If $F:\Ac\to \Ac'$ is a right exact functor, then there is an isomorphism
$$F(\oint^{M\in \Mo} (S,\gamma))\simeq \oint^{M\in \Mo} (F\circ S,F(\gamma)).$$\qed
\end{lema}

We shall also need the next result.
\begin{lema}\label{equivalence-on-coend} Let $\Mo, \No$ be right $\ca$-module categories and let $(J,c):\Mo\to\No$ be an equivalence of $\ca$-module categories. Assume that $S:\No^{\op}\times \No\to \ac$ is a functor equipped with a prebalancing $\beta$. The functor $S(J(-), J(-)):\Mo^{\op}\times \Mo\to \ac$ has a prebalancing $\gamma$ given by
$$\gamma^V_{M,N}=S(\id_{J(M)},c_{N,{}^*V})\beta^V_{J(M),J(N)}S(c^{-1}_{M,V},\id_{J(N)}) $$
for any $M,N\in \Mo$. There is an isomorphism
$$\oint^{M\in \Mo}  (S(J(-), J(-)),\gamma)\simeq \oint^{N\in \No}  (S,\beta).$$
\end{lema}
\pf We only sketch the proof. Let $\lambda_N:S(N,N)\to \oint^{N\in \No}  (S,\beta)$ the associated dinatural transformations. If we define $\pi_M=\lambda_{J(M)}$, for any $M\in \Mo$, one can verify that these are dinatural transformations and they satisfy \eqref{dinat:coend:module:right}. Universality of $\pi$ follows from the universality of $\lambda$ and the fact that $J$ is an equivalence of categories.
\epf
