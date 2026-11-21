---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES"
section_id: sec-012-35-the-tilting-category-t-and-its-graded-counter
section_title: "The tilting category T and its graded counterpart Tgr"
section_number: 3.5
pages: 27-31
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.964
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on T."
---
\label{sub-grad}
In this subsection we discuss the 
consequences of Theorems~\ref{thm-struktursatz1} 
and~\ref{thm-struktursatz2} with respect to the 
question how the path length grading $l(\cdot)$ 
(see Definition~\ref{def-ksquiver1}) of 
Khovanov-Seidel's $\infty$-quiver algebra relates 
to the tilting category $\T$. We point out that this is non-trivial since Theorems~\ref{thm-struktursatz1} and~\ref{thm-struktursatz2} only say that 
$\T_{\lambda}(\leq \bbm)$ and $\T_{\lambda}$ are 
isomorphic to subcategories of $\pModAm$ and $\pModAi$.



Recall that, for every graded algebra $A$, there is a 
\textit{forgetful functor} 
$\mathrm{forget}\colon\ModgrA\to\ModA$ 
that forgets 
the grading. Using this 
functor, we say that an $A$-module 
$M\in\Ob(\ModA)$ is \textit{gradable} if there 
exists an $A$-module $\tilde M\in\Ob(\ModgrA)$ 
such that $\mathrm{forget}(\tilde M)=M$. Note 
that, by abuse of notation, we usually do not distinguish between $\tilde M$ and $M$.



Recall that $\Hom_{\ModA}(M,M^{\prime})$ 
consists of all (right) $A$-module 
homomorphisms $f\colon M\to M^{\prime}$ 
and $\Hom_{\ModgrA}(\tilde M,\tilde M^{\prime})$ 
consists of (right) $A$-module homomorphisms 
$\tilde f\colon \tilde M\to \tilde M^{\prime}$ as 
in~\eqref{eq-gradhom}. Hence, in the same vein as 
above, we can call an $A$-module homomorphism 
$f\colon M\to M^{\prime}$ \textit{gradable}, 
if there exists $\tilde f\colon\tilde M\to \tilde M^{\prime}$ 
such that $\mathrm{forget}(\tilde f)=f$.
Consequently, we define the following.






\begin{defn}\label{defn-gradable}
We call a (left) $\Uq$-tilting module 
$M\in\Ob(\T)$ \textit{gradable}, if $\bVi(M)$ is 
gradable viewed as a (right) $\Ai$-module. We call a 
$\Uq$-intertwiner $f\colon M\to M^{\prime}\in\Hom_{\T}(M,M^{\prime})$ 
\textit{gradable}, if $\bVi(f)\colon \bVi(M)\to \bVi(M^{\prime})$ is 
a gradable $\Ai$-module homomorphism.



We denote by $\Tgr$ the subcategory of $\T$ consisting 
of gradable $\Uq$-tilting modules and gradable 
$\Uq$-intertwiners. We use similar notations and 
conventions for $\leq\bbm$ and for fixed $\lambda$ or $\mu$.
\end{defn}



The question concerning which objects $M\in\Ob(\T)$ 
are gradable turns out to be surprisingly 
simple in our case. We note that, with respect to 
the rather complicated situation for 
graded category $\mathcal O_0^{\mathfrak{p}}$ 
discussed in e.g.~\cite[Theorem~4.1]{st2}, 
the following proposition is quite remarkable.



\begin{prop}\label{prop-grading}
All objects $M\in\Ob(\T_{\lambda}(\leq\bbm))$, 
$M\in\Ob(\T_{\lambda})$ and $M\in\Ob(\T)$ are gradable. The grading of 
each indecomposable module $\Tn{\bbi}$ is unique up to shifts.\makeqed
\end{prop}



\begin{proof}
We only prove the $\infty$ case and leave 
the other case to the reader. We start by 
considering $\lambda\in\mathcal A_0$ and 
discuss the semisimple case on the walls afterwards.




It is easy to check that, for any graded algebra 
$A$ and any two gradable $A$-modules $M$ and 
$M^{\prime}$, the direct sum $M\oplus M^{\prime}$ 
is also gradable. Thus, by Lemma~\ref{lem-tiltcat} 
part (a), it is enough to consider only the 
$\Tn{\bbi}$'s. As in the proof of the part (b) 
of Theorem~\ref{thm-struktursatz2} 
(or Theorem~\ref{thm-struktursatz1} in the finite case) 
we see that $\bVi(\Tn{\bbi})\cong {}_iP$. As discussed 
in Subsection~\ref{sub-ammod}, the ${}_iP$ can be given 
a grading coming from the path length $l(\cdot)$. 
Thus, all the $\Tn{\bbi}$'s are gradable.




On the walls: Since this is the semisimple 
case by Lemma~\ref{lem-block}, we can just 
assign to any simple $\bVi(\Tn{\mu_i})$ a 
degree by demanding that all elements of 
$\bVi(\Tn{\mu_i})$ are concentrated in 
this particular degree. Thus, all 
$\Tn{\mu_i}$ are gradable and concentrated in (up to shifts) degree zero.



The uniqueness (up to shifts) can be proven as in~\cite[Lemma~2.5.3]{bgs}.
\end{proof}



\begin{cor}\label{cor-gradings2}
We have isomorphisms of ungraded categories 
$\T_{\lambda}(\leq\bbm)\cong_{\mathrm{iso}}\Tgr(\leq\bbm)$ 
and $\T\cong_{\mathrm{iso}}\Tgr$. That is, 
also all morphisms are gradable and the gradings are unique up to a shift.\makeqed
\end{cor}



\begin{proof}
As before, for any 
two gradable $A$-homomorphisms $f$ and 
$f^{\prime}$, the direct sum $f\oplus f^{\prime}$ 
is also gradable. Thus, by Lemma~\ref{lem-tiltcat} 
part (a) again together with Proposition~\ref{prop-grading}, 
it is enough to consider only 
$\Hom_{\Uq}(\Tn{\bbi},\Tn{\bbi^{\prime}})$. 
By Corollary~\ref{cor-homspaces} we see that 
this space has a basis consisting of a subset 
of $\bbi,u_i,d_i$ and $\varepsilon_i$ (in the non-semisimple case) who are all gradable by Proposition~\ref{prop-isoofalg2}. The semisimple 
case and the uniqueness of the grading follow as 
above. This gives rise to an 
isomorphism after collapsing the grading of $\Tgr$ 
(since each object $M$ of $\T$ corresponds to objects of $\Tgr$ 
of the form $M\langle s\rangle$ for $s\in\bZ$).
\end{proof}



Using Corollary~\ref{cor-gradings2} and 
abuse of language, we do not distinguish 
between $\Uq$-tilting modules or their graded versions.
Moreover, as a consequence of 
Corollary~\ref{cor-gradings2}, we can 
choose a \textit{standard grading} 
(since it will be unique up to shifts) 
by demanding that simple $\Uq$-tilting modules 
are concentrated in degree zero and 
proceed inductively along the quiver. 
Note that, by Propositions~\ref{prop-weyl} 
and~\ref{prop-tilt} and Corollary~\ref{cor-weyl}, 
this gives inductively a graded lift of 
$\Ln{\bbi}$, $\Vn{\bbi}$ and $\dVn{\bbi}$ as well. 
This choice gives rise to the following graded 
refinements of Propositions~\ref{prop-weyl} 
and~\ref{prop-tilt} and Corollary~\ref{cor-weyl}.



\begin{prop}\label{prop-refine}
Suppose $i=al+b$ for some $a,b\in\bN$ with 
$b\leq l-2$. Set $i^{\prime}=(a+2)l-b-2$. 
Then there
exist short exact sequences
\begin{gather*}
0\longrightarrow \Ln{i}\langle+1\rangle\hooklongrightarrow\Vn{i^{\prime}}\twoheadlongrightarrow \Ln{i^{\prime}}\longrightarrow 0,
\hspace*{0.25cm}
0\longrightarrow \Ln{i^{\prime}}\hooklongrightarrow\dVn{i^{\prime}}\twoheadlongrightarrow \Ln{i}\langle-1\rangle\longrightarrow 0,
\\
0\longrightarrow \Vn{i^{\prime}}\hooklongrightarrow\Tn{i^{\prime}}\twoheadlongrightarrow \Vn{i}\langle-1\rangle\longrightarrow 0,
\hspace*{0.25cm}
0\longrightarrow \dVn{i}\langle+1\rangle\hooklongrightarrow\Tn{i^{\prime}}\twoheadlongrightarrow \dVn{i^{\prime}}\longrightarrow 0.
\end{gather*}
Moreover, all involved morphisms are degree preserving.\makeqed
\end{prop}



\begin{proof}
This follows from our choice for the grading convention 
and the degree (under the equivalence in 
Theorems~\ref{thm-struktursatz1} and~\ref{thm-struktursatz2}) 
of the morphisms in $\Hom_{\Uq}(\Tn{\bbi},\Tn{\bbi^{\prime}})$. 
To be more precise, we know that the $\Tn{\bbi}$'s will 
be, under the functor $\bVi$, 
mapped to ${}_iP$. Then for example, 
as explained in Proposition~\ref{prop-link}, the unique morphism
\[
\Tn{\bbi}\twoheadrightarrow\dVn{\bbi}\hookrightarrow\Tn{\bbiu}\leftrightsquigarrow\xymatrix{
  \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbiu};\endxy}\!\!   &  \raisebox{0.1cm}{\xy(0,0)*{\bullet};(0,-2.5)*{\scriptstyle \bbi};\endxy} \ar[l]_/-0.2em/{u_i}\\
}
\]
is of degree $1$. By our convention 
we see that moving to the left along 
the KS $\infty$-quiver always increases 
the degree (starting in degree zero for the first simple module). Thus,
\[
0\longrightarrow \dVn{i}\langle+1\rangle\hooklongrightarrow\Tn{i^{\prime}}\twoheadlongrightarrow \dVn{i^{\prime}}\longrightarrow 0.
\]
All other cases follow similarly 
and are left to the reader. Note again 
that moving to the left along the KS 
$\infty$-quiver always increases the degree, 
but, by duality, moving right decreases it.
\end{proof}



\begin{rem}\label{rem-webalg2}
As we already mentioned in 
Remark~\ref{rem-webalg} the grading induced on 
$\T$ comes from an Euler characteristic on a 
certain cobordism category associated to 
Khovanov's arc algebra $H^m$. Thus, this is 
a ``natural'' grading from the viewpoint of topology.



As we mentioned above, we think that this 
should generalize in type $\boldsymbol{\mathrm{A}}$. The degree will 
there be given by an Euler characteristic on 
a certain ``foam'' category associated to the 
$\mathfrak{sl}_n$-web algebras which generalize Khovanov's arc algebra. See for example~\cite{lqr1},~\cite{mpt},~\cite{qr1} or~\cite{tub4}. 
Or alternatively, by a grading coming from certain cyclotomic KL-R algebras in the sense of~\cite{kl5} or~\cite{rou}.
\end{rem}




We conclude this section by lifting the translation 
onto $\mathcal T^{\mu}_{\lambda}$, the translation out 
of $\mathcal T_{\mu}^{\lambda}$ and the 
translation through the wall $\Theta_s$ and $\Theta_t$ 
to their graded versions (we use the same notation for these). 
To understand our notation, recall that a category 
$\tilde{\mathcal C}$ is called a \textit{graded} 
category, if there exists a functor 
$\mathrm{deg}\colon\tilde{\mathcal C}\to\mathcal Z$ 
where we consider $\bZ$ as a category $\mathcal Z$ 
with $\Ob(\mathcal Z)=\{\bullet\}$ and 
$\End_{\mathcal Z}(\bullet)=\bZ$. In addition, there is a 
$\bZ$-action $\langle s\rangle$ on the objects 
$O\in\Ob(\tilde{\mathcal C})$, called \textit{shift} 
by $s\in\bZ$, such that a given morphism 
$f\in\Hom_{\tilde{\mathcal C}}(O,O^{\prime})$ of 
degree $d$ is of degree $d+s^{\prime}-s$ in 
$\Hom_{\tilde{\mathcal C}}(O\langle s\rangle,O^{\prime}\langle s^{\prime}\rangle)$ 
(said otherwise, 
every morphism in $\tilde{\mathcal C}$ has a degree which behaves 
additively under composition and objects can be shifted via 
$\langle s\rangle$). Moreover, denote by $\mathcal C$ the 
\textit{ungraded version}. We say a functor 
$\mathcal F\colon\mathcal C\to\mathcal D$ is gradable 
if there exists a \textit{lift} 
$\tilde{\mathcal F}\colon\tilde{\mathcal C}\to\tilde{\mathcal D}$ such that
$\mathrm{forget}\circ\tilde{\mathcal F}=\mathcal F\circ\mathrm{forget}$.
We say that $\tilde{\mathcal F}$ 
and $\tilde{\mathcal F}^{\prime}$ are the 
\textit{same up to a shift $s\in\bZ$} if there 
is a natural isomorphism\footnote{In the $2$-category 
where objects are graded categories, where morphisms 
are graded functors between these categories and 
where $2$-morphisms are graded natural transformations.} 
between $\tilde{\mathcal F}$ and $\tilde{\mathcal F}^{\prime}\langle s\rangle$.
As before, we are usually very 
careless with our distinction 
of $\tilde{\mathcal F}$ and $\mathcal F$.


\begin{cor}\label{cor-funcgrad2}
The functors 
$\mathcal T_{\lambda}^{\mu,i},\mathcal T_{\mu}^{\lambda,i},\mathcal T_{\lambda}^{\mu},\mathcal T_{\mu}^{\lambda}\in\Ob(\Endo(\T(\leq\bbm)))$
are gradable (same in the infinite case). 
Moreover, any two lifts of 
$\mathcal T_{\lambda}^{\mu,i},\mathcal T^{\lambda,i}_{\mu}$ are the same up to shifts.\makeqed
\end{cor}



\begin{proof}
This follows by Remark~\ref{rem-othermaps} 
and the fact that $\mathcal U_{i}^t$ and $\mathcal U^i_t$ are 
graded functors (similarly in the $\infty$ case). 
The statement for 
$\mathcal T_{\lambda}^{\mu}$ and $\mathcal T_{\mu}^{\lambda}$ follows now 
by~\eqref{eq-projectivefunc2}, since clearly sums of gradable, 
additive functors in an additive category are 
gradable. For the infinite case note that any sum (finite or not) 
of gradable functors is gradable and the claim 
follows from~\eqref{eq-projectivefunc2} 
and the finite case.
The uniqueness up to shifts can again be verified 
as in~\cite[Lemma 2.5.3]{bgs}, since 
$\mathcal T_{\lambda}^{\mu,i}$ and 
$\mathcal T_{\mu}^{\lambda,i}$ are 
indecomposable by Proposition~\ref{prop-profunc}. 
\end{proof}



\begin{cor}\label{cor-funcgrad1}
The functors 
$\Theta^{\lambda,i}_s,\Theta^{\lambda,i}_t,\Theta^{\lambda}_s,\Theta^{\lambda}_t\in\Ob(\Endo(\T_{\lambda}(\leq\bbm)))$ 
are 
gradable (same in the infinite case). 
Moreover, any two lifts of $\Theta^{\lambda,i}_{s\text{ or }t}$ are the same up to a 
shift.\makeqed
\end{cor}



\begin{proof}
We can use Corollary~\ref{cor-funcgrad2} 
since all 
functors involved can be obtained via sums and compositions of the functors 
$\mathcal T_{\lambda,i}^{\mu}$ and $\mathcal T^{\lambda,i}_{\mu}$. The infinite case follows as above, but using~\eqref{eq-projectivefunc} 
instead of~\eqref{eq-projectivefunc2}. 
By Proposition~\ref{lem-profuncinde} the functors $\Theta^{\lambda,i}_{s\text{ or }t}$ are 
indecomposable and the uniqueness up to shifts follows as before. 
\end{proof}


We choose the graded versions of 
$\mathcal T_{\lambda}^{\mu,i}$ and out of $\mathcal T^{\lambda,i}_{\mu}$ 
in the evident way as induced by the gradings on $\mathcal U_i^t$ or 
$\mathcal U^i_t$.
We get the following refinement of Proposition~\ref{prop-functors}.
\begin{cor}\label{cor-funcgrad3}
In the graded category $\Tgr$ we have for all 
$i\in\bN$ the following.
\begin{itemize}
\item[(a)] The functors 
$\mathcal T_{\lambda}^{\mu}$ and $\mathcal T^{\lambda}_{\mu}$ are 
well-defined (their definition gives gradable $\Uq$-tilting modules in the 
right blocks), (up to shifts) 
adjoints (left and right) and 
exact. Thus, $\Theta^{\lambda}_s$ and $\Theta^{\lambda}_t$ are exact and graded self-adjoint.
\item[(b)] We have (recalling that $\Ln{\mu_i}\cong\Tn{\mu_i}$)
\begin{gather*}
\mathcal T_{\lambda}^{\mu}(\Tn{\lambda_i})\cong\begin{cases}\Tn{\mu_{i-1}}\langle+1\rangle\oplus\Tn{\mu_{i+1}}\langle+1\rangle,  & \text{if }\mu_i>\lambda_i,\\
  \Tn{\mu_i}\oplus\Tn{\mu_i}\langle+2\rangle,  & \text{if }\mu_i<\lambda_i,\end{cases}
\\
\mathcal T^{\lambda}_{\mu}(\Tn{\mu_i})\cong\begin{cases}\Tn{\lambda_{i+1}}\langle-1\rangle,  & \text{if }\mu_i>\lambda_i,\\
 \Tn{\lambda_{i}}\langle-1\rangle,  & \text{if }\mu_i<\lambda_i.\end{cases}
\end{gather*}
\item[(c)] The dead-end relations $\Theta^{\lambda}_s(\Tn{\lambda_0})\cong0$, $\Theta^{\lambda}_s(\Tn{\lambda_1})\cong\Tn{\lambda_2}$ and $\Theta^{\lambda}_t(\Tn{\lambda_0})\cong\Tn{\lambda_1}$. Moreover, we have
\[
\Theta^{\lambda}_{s\text{ or }t}(\Tn{\lambda_i})\cong\begin{cases}\Tn{\lambda_{i-1}}\oplus\Tn{\lambda_{i+1}} ,  & \text{if }i>1\text{ is odd for }s\text{ and even for }t,\\
  \Tn{\lambda_{i}}\langle-1\rangle\oplus\Tn{\lambda_{i}}\langle+1\rangle ,  & \text{if }i>0\text{ is odd for }t\text{ and even for }s.\end{cases}
\]
\end{itemize}
Here we set $\Tn{-1}=\Tn{\lambda_{-1}}=\Tn{\mu_{-1}}=0$.\makeqed
\end{cor}



\begin{proof}
This follows directly from 
Theorem~\ref{thm-struktursatz2} 
parts (d), (f) and (g) together 
with~\eqref{eq-ufunctors} and the 
discussion in Subsection~\ref{sub-endo}, for example Lemma~\ref{lem-adjoint}.
\end{proof}



\begin{prop}\label{prop-endograd}
All functors in $\Endo(\T)$ are gradable. 
Moreover, the grading is unique up to shifts 
on the indecomposable projective functors. 
Similar for $\Endo(\T_{\lambda})$.\makeqed
\end{prop}



\begin{proof}
The uniqueness, up to shifts, of the grading on the indecomposable 
factors can be proven as before. By the Krull-Schmidt property of $\Endo(\T)$ 
(see Lemma~\ref{lem-profunc}) and the fact that any direct sum of gradable, 
additive functors in an additive category is 
gradable, it suffices to show that indecomposable 
projective functors are gradable. By 
Lemma~\ref{lem-profuncinde} these are given 
by tensoring with a $\Tn i$ for some $i\in\bN$. 
By Proposition~\ref{prop-grading} all objects 
of $\T$ are gradable and, by Lemma~\ref{lem-tiltcat} 
part (b), the category $\T$ is preserved by finite 
tensor products. Thus, the indecomposable projective functors are gradable. 
For 
$\Endo(\T_{\lambda})$ this follows from Corollary~\ref{cor-funcgrad1}.
\end{proof}



Proposition~\ref{prop-endograd} motivates 
the definition of $\Endo(\Tgrl)$ which can be 
defined in the spirit of~\eqref{eq-gradhom} (thus, using 
\textit{graded} hom-spaces of natural 
transformations). This is the same as 
saying that the category $\Endo(\Tgrl)$ is graded in the above sense.



In order to state the proposition, we write 
$\bVi\mathcal F(\Tn{\bbin})$ short for 
$\bigoplus_i\bVi\mathcal F(\Tn{\bbi})$. This 
is an $\Ai$-bimodule via pre-composition 
(right) and post-composition (left) with 
$\mathcal F(\cdot)$ or $\mathcal F^{(\prime)}(\cdot)$.



Moreover, recall that the superscript fs 
indicates that we are only considering finitely 
supported homomorphisms. We have the following 
(similar of course for $\Endo(\Tgr_{\lambda}(\leq\bbm))$).



\begin{prop}\label{prop-endograd2}
Let $\mathcal F,\mathcal F^{\prime}$ be two 
functors in $\Endo(\Tgrl)$. Then there exists 
an isomorphism of graded $\bC$-vector spaces
\[
\Hom^{\mathrm{fs}}_{\Endo(\Tgrl)}(\mathcal F,\mathcal F^{\prime})\cong \Hom^{\mathrm{fs}}_{\AipModgrAi}(\bVi\mathcal F(\Tn{\bbin}),\bVi\mathcal F^{\prime}(\Tn{\bbin})).
\]
This is an isomorphism of graded rings if $\mathcal F=\mathcal F^{\prime}$.\makeqed
\end{prop}



\begin{proof}
It 
suffices to verify the statement for the 
translation onto $\mathcal T^{\mu}_{\lambda}$, 
out of $\mathcal T_{\mu}^{\lambda}$ and the 
through the wall functors $\Theta^{\lambda}_{s\text{ or }t}$. 
By Theorem~\ref{thm-struktursatz2} part (d), (f) and (g) 
it suffices to show the statement for the corresponding $\mathcal U$'s.



Without loss of generality, we only discuss the 
``even'' case, that is, $\mathcal U^t_{\mathrm{even}}$, $\mathcal U_t^{\mathrm{even}}$ 
and $\mathcal U^{\infty}_{\mathrm{even}}$ which correspond to 
$\mathcal T^{-1}_{\lambda}$, $\mathcal T_{-1}^{\lambda}$ and 
$\Theta^{\lambda}_{s}$ respectively. Thus, by additivity, it 
suffices to show the statement for $\mathcal U^t_{i}$, 
$\mathcal U_t^{i}$ and $\mathcal U_i$ for $i>0$ even.
Fix $i$ and assume that $i\ll m$. Recall 
that Khovanov and Seidel have shown 
in~\cite[Proposition~2.9]{ks1} that 
$\pModAm$ and $\mathcal O^{\mathfrak{p}}_0$ 
for $\mathfrak{sl}_{m+1}$ and parabolic 
$\mathfrak{p}$ of type $S_1\times S_{m-1}$ 
are equivalent. Moreover, as they explain 
below~\cite[Proposition~2.9]{ks1}, 
$\mathcal U^t_{i}$, $\mathcal U_t^{i}$ and 
$\mathcal U_i$ correspond to the translation onto, out off 
and through the $i$-th wall functors.



Note now that the same holds for the graded 
version of $\mathcal O^{\mathfrak{p}}_0$ 
introduced in~\cite{st2} as Stroppel explains in~\cite[Section~1]{st1}. 
Thus, we can use~\cite[Theorem~1.12]{st1} to finish the proof in the 
``cut-off case''. Taking the inductive limit now shows the statement.
\end{proof}



\begin{cor}\label{cor-center}
There is an isomorphism of graded rings
\[
\End^{\mathrm{fs}}_{\mathrm{gr}}(\mathrm{id})\cong Z(\Ai),
\]
where $\mathrm{id}$ is the identity functor on 
$\Tgrl$, $Z(\Ai)$ is the center of 
$\Ai$ and the endomorphism ring is to be taken in $\Endo(\Tgrl)$.\makeqed
\end{cor}



\begin{proof}
From Proposition~\ref{prop-isoofalg2} 
combined with Proposition~\ref{prop-endograd2}. 
Note that we get the center $Z(\Ai)$ and not $\Ai$ 
itself because the endomorphism ring from 
Proposition~\ref{prop-isoofalg2} is as 
$\Uq$-intertwiners while the one induced from 
Proposition~\ref{prop-endograd2} is as $\AipModgrAi$-bimodule intertwiners.
\end{proof}



\begin{rem}\label{rem-grothendieck1a}
It is known 
that the split Grothendieck group 
$K_0^{\oplus}(\cdot)=K_0^{\oplus}(\cdot)\otimes_{\bZ[v,v^{-1}]}\bC$ 
(viewed as a module over $\bZ[v,v^{-1}]$ where the 
formal parameter $v$ comes for the grading) of 
$\pModgrAm$ \textit{categorifies} the Burau 
representation $\mathcal B_{m+1}$ of the 
$m+1$-strand braid group $B_{m+1}$ 
(the action of $B_{m+1}$ is induced via 
functors constructed from $\mathcal U_i$), see~\cite[Proposition~2.8 and Subsection 2.d]{ks1}. 
Using Theorem~\ref{thm-struktursatz1}, we see that the 
same is true for $\Tgrl(\leq\bbm)$, that is 
$K_0^{\oplus}(\Tgrl(\leq\bbm))\cong\mathcal B_{m+1}$ as 
$B_{m+1}$-modules. Note now that the limit therefore 
categorifies the corresponding $\infty$ version of 
the Burau representation of the braid 
group $B_{\infty}$ with $\infty$-many strands.
\end{rem}



\begin{rem}\label{rem-grothendieck1}
Fix $\mathfrak{sl}_{m+1}$ and denote 
by $\mathfrak{p}_i$ the parabolic for 
$S_i\times S_{m-i}$. Moreover, we denote 
by $\mathcal O^{\mathfrak{p}}_{\mathrm{max}}=\bigoplus_{i=0}^m\mathcal O^{\mathfrak{p}_i}_{0}$ 
the direct sum. We note that, as Bernstein-Frenkel-Khovanov 
conjectured in~\cite[Conjectures~1-4]{bfk} and Stroppel proved 
in~\cite{st3}, parabolic category 
$\mathcal O^{\mathfrak{p}}_{\mathrm{max}}$ 
for $\mathfrak{sl}_{m+1}$ (compare to Remark~\ref{rem-cato}) 
can be used to \textit{categorify} the $m+1$-strand 
Temperley-Lieb algebra $TL^v_{m+1}$. The split 
Grothendieck group $K_0^{\oplus}$ of the category 
of projective endofunctors on 
$\mathcal O^{\mathfrak{p}}_{\mathrm{max}}$ gives\footnote{The parameter $q$ in the notation of Bernstein-Frenkel-Khovanov comes from the 
grading.} $TL^v_{m+1}$. 
The Grothendieck group behaves additive, i.e.
\[
TL^v_{m+1}\cong K_0^{\oplus}(\Endo(\mathcal O^{\mathfrak{p}}_{\mathrm{max}}))\cong \bigoplus_{i=0}^mK_0^{\oplus}(\Endo(\mathcal O^{\mathfrak{p}}_{i})).
\]
Thus, $\Endo(\mathcal O^{\mathfrak{p}}_{1})$ 
gives a summand $\overline{TL}^v_{m+1}$ of $TL^v_{m+1}$ 
that corresponds to the ``next to highest weight'' 
summand of $V^{\otimes m}$ (with notation as in 
Remark~\ref{rem-webalg}), see~\cite[Section~6]{chkh}.



Thus, as explained in Remark~\ref{rem-cato}, 
by Proposition~\ref{prop-endograd2}, the same 
is true for $\Endo(\Tgrl(\leq\bbm))$. Moreover, 
it is easy to see that the embedding of categories
\[
\Endo(\Tgrl(\leq\bbm))\hookrightarrow\Endo(\Tgrl(\leq\bbmu))
\]
gives rise to an embedding
\[
\overline{TL}^v_{m+1}\cong K_0^{\oplus}(\Endo(\Tgrl(\leq\bbm)))\hookrightarrow K_0^{\oplus}(\Endo(\Tgrl(\leq\bbmu)))\cong \overline{TL}^v_{m+2}.
\]
Thus, by Proposition~\ref{prop-isoofalg2}, $\Endo(\Tgrl)$ 
governs all of them at once.
\end{rem}
