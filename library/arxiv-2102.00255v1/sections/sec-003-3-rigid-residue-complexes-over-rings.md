---
doc_id: arxiv-2102.00255v1
doc_title: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS"
section_id: sec-003-3-rigid-residue-complexes-over-rings
section_title: "Rigid Residue Complexes over Rings"
section_number: 3
pages: 9-11
source_pdf: 2102.00255v1.pdf
source_sha256: b63df73a9d0e1534
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.959
doc_brief: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS — In this article we explain the theory of rigid residue complexes in commutative algebra and algebraic geometry, summarizing the"
---
\label{sec:rrr-rings}


Now we enter the zone of "anticipated results": many of the results still
only have sketchy proofs, and should therefore be regarded with caution. Such a 
theorem will be labeled {\bf Theorem$^{\bsym{(*)}}$}.

Recall that we are still working in $\cat{Rng} \eftover \K$, where $\K$ is a 
regular noetherian base ring.
If $L \in \cat{Rng} \eftover \K$ is a field, then its rigid dualizing 
complex $R_L$ must be isomorphic to $L[d]$ for some integer $d$. We define the 
{\em rigid dimension} of $L$ to be
$\opn{rig{.}dim}_{\K}(L) := d$.

\begin{exa}
If the base ring $\K$ is a field, then 
$\opn{rig{.}dim}_{\K}(L) = \opn{tr{.}deg}_{\K}(L)$, the transcendence degree.
On the other hand, for $\K = \Z$ and $L = \mbb{F}_p$ we have
$\opn{rig{.}dim}_{\Z}(\mbb{F}_p) = -1$.
\end{exa}

Now take an arbitrary $A \in \cat{Rng} \eftover \K$. 
For a prime ideal $\p \sub A$, with residue field $\bsym{k}(\p)$,
we define 
$\opn{rig{.}dim}_{\K}(\p) := \opn{rig{.}dim}_{\K}(\bsym{k}(\p))$.
The resulting function
$\opn{rig{.}dim}_{\K} : \opn{Spec}(A) \to \Z$
has the expected property: it drops by $1$ if $\p \sub \mfrak{q}$ is an 
immediate specialization of primes. 
The function $\opn{rig{.}dim}_{\K}$ is bounded, since 
$\opn{Spec}(A)$ is finite dimensional. 
See \cite[Theorem 13.3.3]{Ye7}.

For any $\p \in \opn{Spec}(A)$ we denote by $J(\p)$ the injective hull of the
$A_{\p}$-module $\bsym{k}(\p)$. This is an indecomposable injective $A$-module. 
According to the Matlis classification, every injective $A$-module is a direct 
sum, often infinite, of such modules $J(\p)$.
See \cite[Section 13.2]{Ye7} for a detailed discussion, and Remark 
\ref{rem:260} on the possible functorial properties of $J(\p)$.  

The following  definition is a refinement of the 
concept of {\em residual complex} from \cite{RD}. 

\begin{dfn} \label{dfn:250}
A {\em rigid residue complex} over $A$ relative to $\K$ is a rigid
dualizing complex {\em $(\mcal{K}_A, \rho_A)$} of this special sort: 
for every $d \in \Z$ there is an isomorphism of $A$-modules
\[ \mcal{K}_A^{-d} \cong 
\bigoplus_{\substack{ \p \, \in \, \opn{Spec}(A) \\  
\opn{rig{.}dim}_{\K} \mspace{-2mu}(\p) \, = \, d }}  J(\p) \ . \]
\end{dfn}
 
Recall the category of rigid complexes $\cat{D}(A)_{\mrm{rig} / \K}$ from 
Definition \ref{dfn:231}.

\begin{dfn} \label{dfn:251}
A {\em morphism of rigid residue complexes} 
$\phi : (\mcal{K}_A, \rho_A) \to (\mcal{K}'_A, \rho'_A)$
is a homomorphism 
$\phi : \mcal{K}_A \to \mcal{K}'_A$ in $\cat{C}_{\mrm{str}}(A)$, 
such that 
$\opn{Q}(\phi) : (\mcal{K}_A, \rho_A) \to (\mcal{K}'_A, \rho'_A)$
is a morphism in $\cat{D}(A)_{\mrm{rig} / \K}$.
We denote by $\cat{C}(A)_{\mrm{res} / \K}$
the category of rigid residue complexes. 
\end{dfn}

Note the unusual {\em mixed nature} of this definition: a morphism $\phi$ 
in $\cat{C}(A)_{\mrm{res} / \K}$ is literally is homomorphism of complexes, but 
the condition it must satisfy is in the derived category.  

\begin{thm}[\cite{Ye7}, \cite{OSY}] \label{thm:125}
Let $A$ be an EFT $\K$-ring. The ring $A$ has a rigid residue complex 
$(\KK_A, \rho_A)$ and it is unique, up to a unique isomorphism in 
$\cat{C}(A)_{\mrm{res} / \K}$. 
\end{thm}

This theorem is not actually stated in either of these references, yet it is 
easily proved by combining several results from them (Theorem \ref{thm:120} 
above, proved in \cite{OSY}, and \cite[Theorems 13.3.15 and 13.3.17]{Ye7}).

Let us now mention several important functorial properties of 
rigid residue complexes.

\begin{thmstar}[\cite{Ye8}] \label{thm:126}
 Suppose $v : A \to A'$ is an essentially \'etale homomorphism of EFT 
$\K$-rings. There is a unique nondegenerate forward homomorphism 
$\opn{q}^{\mrm{res}}_{v} : \mcal{K}_A \to \mcal{K}_{A'}$
in $\cat{C}_{\mrm{str}}(A)$, called the {\em rigid \'etale-localization 
homomorphism}, such that 
$\opn{Q}(\opn{q}^{\mrm{res}}_{v}) : 
(\KK_A, \rho_A) \to (\KK_{A'}, \rho_{A'})$
is the rigid \'etale-localization morphism $\opn{q}^{\mrm{rig}}_{v}$
from Theorem \tup{\ref{thm:242}}.
\end{thmstar}
 
\begin{corstar}[\cite{Ye8}] \label{cor:125}
The assignment $A' \mapsto \KK_{A'}$ extends uniquely to a quasi-coherent 
sheaf on the small \'etale site of $\opn{Spec}(A)$. 
\end{corstar}
 
This corollary will be crucial when we get to DM stacks. 

\begin{thmstar}[\cite{Ye8}] \label{thm:130} 
Suppose $u : A \to B$ is a finite homomorphism of EFT $\K$-rings. 
There is a unique nondegenerate backward homomorphism 
$\opn{tr}^{\mrm{res}}_{u} : \mcal{K}_B \to \mcal{K}_{A}$
in $\cat{C}_{\mrm{str}}(A)$, called the {\em rigid trace homomorphism}, such 
that 
$\opn{Q}(\opn{tr}^{\mrm{res}}_{u}) : 
(\KK_B, \rho_B) \to (\KK_{A}, \rho_{A})$
is the rigid trace morphism $\opn{tr}^{\mrm{rig}}_{u}$
from Theorem \tup{\ref{thm:241}}.
\end{thmstar}
 
The uniqueness implies that the rigid trace is functorial on finite 
homomorphisms. 

\begin{thmstar}[\cite{Ye8}] \label{thm:131}
Suppose we are given a finite ring homomorphism $u : A \to  B$ and
an essentially \'etale ring homomorphism $v : A \to A'$.
Define the ring $B' := A' \ot_A B$, and the homomorphisms 
$u' : A' \to B'$ and $w : B \to  B'$ as in Theorem \tup{\ref{thm:240}}, which 
are finite and essentially \'etale, respectively. Then the diagram 
\[ \UseTips \xymatrix @C=6ex @R=5ex {
\KK_A
\ar[d]_{\opn{q}^{\mrm{res}}_{v}}
&
\KK_B
\ar[l]_{\opn{tr}^{\mrm{res}}_u}
\ar[d]^{\opn{q}^{\mrm{res}}_{w}}
\\
\KK_{A'}
&
\KK_{B'}
\ar[l]_{\opn{tr}^{\mrm{res}}_{u'}}
} \]
in $\cat{C}_{\mrm{str}}(A)$ is commutative. 
\end{thmstar}

\begin{thmstar}[\cite{Ye8}] \label{thm:132}
For every homomorphism $u : A \to  B$ in $\cat{Rng} \eftover \K$
there is a unique backward homomorphism of graded $A$-modules 
$\opn{tr}^{\mrm{ires}}_{u} : \mcal{K}_B \to \mcal{K}_{A}$,
called the {\em ind-rigid trace homomorphism}, satisfying these conditions: 
\begin{itemize} 
\item[$\triangleright$] If $u$ is a finite homomorphism, then 
$\opn{tr}^{\mrm{ires}}_{u} = \opn{tr}^{\mrm{res}}_{u}$,
the rigid trace from Theorem \tup{\ref{thm:130}}. 

\item[$\triangleright$] The ind-rigid trace $\opn{tr}^{\mrm{ires}}_{u}$ 
commutes with the rigid \'etale-localizations $\opn{q}^{\mrm{res}}_{v}$ from 
Theorem \tup{\ref{thm:126}}.
 
\item[$\triangleright$] Functoriality: 
$\opn{tr}^{\mrm{ires}}_{u_2 \circ u_1} = \opn{tr}^{\mrm{ires}}_{u_1} \circ \,
\opn{tr}^{\mrm{ires}}_{u_2}$. 
\end{itemize} 
\end{thmstar}

\begin{rem} \label{rem:299}
If $u : A \to B$ is not finite, then usually the ind-rigid trace 
$\opn{tr}^{\mrm{ires}}_{u}$ is not a morphism in $\cat{C}_{\mrm{str}}(A)$, 
i.e.\ it does not commute with the differentials. This same behavior already 
occurred for the trace in \cite[Section VI.4]{RD}. See the Rigid Residue 
Theorem \ref{thm:1} for the case of a proper map of schemes. 
\end{rem}
 
Observe that the rigid auto-duality functor $\opn{D}^{\mrm{rig}}_A$ from 
(\ref{eqn:130}) now becomes 
\[ \opn{D}^{\mrm{rig}}_A = \opn{Hom}_{A}(-, \KK_A) \ : \
\cat{D}^{}_{\mrm{f}}(A)^{\mrm{op}} \to \cat{D}^{}_{\mrm{f}}(A) .  \]
This means that the twisted induction pseudofunctor $\opn{TwInd}$ gets a lot 
more structure from the results of this section. 

A ring homomorphism $v : A \to A'$ is called {\em faithfully \'etale} 
if it is \'etale and faithfully flat. In other words, if the map of affine 
schemes $\opn{Spec}(A') \to \opn{Spec}(A)$ is \'etale and surjective. 
 

\begin{thmstar}[\'Etale Codescent, \cite{Ye8}] \label{thm:133}
Suppose $v : A \to A'$ is a faithfully \'etale ring homomorphism.
Let $A'' := A' \ot_A A'$, and let $w_1, w_2 : A' \to A''$ be the two inclusions.
Then for every integer $i$ the sequence of $A$-module homomorphisms
\[ \KK^i_{A''} 
\xar{ \opn{tr}^{\mrm{ires}}_{w_{\scalesubsub{2}}} - 
\opn{tr}^{\mrm{ires}}_{w_{\scalesubsub{1}}} \, } 
\KK^i_{A'} \xar{ \opn{tr}^{\mrm{ires}}_{v} \, } \KK^i_A \to 0 \]
is exact. 
\end{thmstar}
 
We have not encountered any similar result in the literature. For us this 
theorem will be required for producing ind-rigid traces for maps of DM 
stacks.

\begin{rem} \label{rem:295}
A few words on notation. In Section \ref{sec:RRD-rings} we used the
notation $\opn{tr}^{\mrm{rig}}_{u}$ and $\opn{q}^{\mrm{rig}}_{v}$
for the rigid trace and rigid \'etale-localization morphisms, respectively,
which are morphisms between dualizing complexes in $\cat{D}(A)$.
We use the modified notation $\opn{tr}^{\mrm{res}}_{u}$ and 
$\opn{q}^{\mrm{res}}_{v}$ for the corresponding homomorphisms between rigid 
residue complexes in $\cat{C}_{\mrm{str}}(A)$. 
They are related as follows: 
$\opn{tr}^{\mrm{rig}}_{u} = \opn{Q}(\opn{tr}^{\mrm{res}}_{u})$
and
$\opn{q}^{\mrm{rig}}_{v} = \opn{Q}(\opn{q}^{\mrm{res}}_{v})$,
where $\opn{Q} : \cat{C}_{\mrm{str}}(A) \to \cat{D}(A)$ 
is the categorical localization functor. 
\end{rem}

\begin{rem} \label{rem:260}
It is important to mention that the indecomposable injective $A$-module $J(\p)$ 
is unique only up to isomorphism, and without added structure such an 
isomorphism cannot be made unique or "canonical". To see this, note that 
the automorphism group of $J(\p)$
is the group of invertible elements 
${\what{A}_{\p}}^{\, \times}$ of the complete local ring $\what{A}_{\p}$, and 
the  subgroup of $\what{A}_{\p}^{\, \times}$ consisting of the elements 
congruent to $1$ modulo $\p$ (usually a huge subgroup) acts trivially on the 
submodule $\kk(p) \sub J(\p)$. This implies that there is nothing canonical 
about the embedding $\kk(\p) \inj J(\p)$.

There are ways to enhance $J(\p)$ with some extra structure. 
In our context, the rigid residue complex 
$(\mcal{K}_{A_{\p}}, \rho_{A_{\p}})$ of $A_{\p}$ (relative to $\K$) has the 
property that the $A_{\p}$-module $\KK_{A_{\p}}^{-d}$, where 
$d := \opn{rig{.}dim}_{\K}(\p)$, is isomorphic to $J(\p)$, by Definition 
\ref{dfn:250}. A more global way to "rigidify" $J(\p)$ is to consider the 
$A$-module $\Ga_{\p}(\KK_{A}^{-d})$, the $\p$-torsion submodule of 
$\KK_{A}^{-d}$. The forward functoriality 
$\opn{q}^{\mrm{res}}_{v} : \KK_{A} \to \KK_{A_{\p}}$,
which is associated to the localization ring homomorphism $v : A \to A_{\p}$,
induces an isomorphism 
$\Ga_{\p}(\KK_{A}^{-d}) \iso \KK_{A_{\p}}^{-d}$. 
According to Theorems \ref{thm:126}, \ref{thm:130} and \ref{thm:131}, the 
modules $\KK_{A_{\p}}^{-d}$ and $\Ga_{\p}(\KK_{A}^{-d})$
are functorial, in two directions, in the rings $A_{\p}$ and $A$ respectively. 
Thus these are "canonical incarnations" of $J(\p)$. 

Other ways to obtain "canonical incarnations" of $J(\p)$ are using {\em local 
duality} -- this is implicit throughout \cite{RD}; or using coefficient fields 
and higher completions (see e.g.\ \cite{Ye1} and \cite{Ye2}). 
\end{rem}
