---
doc_id: arxiv-2102.00255v1
doc_title: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-3
source_pdf: 2102.00255v1.pdf
source_sha256: b63df73a9d0e1534
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.926
doc_brief: "RIGIDITY, RESIDUES AND DUALITY: OVERVIEW AND RECENT PROGRESS — In this article we explain the theory of rigid residue complexes in commutative algebra and algebraic geometry, summarizing the"
---
This article is about the {\em rigid approach to Grothendieck Duality} (GD).
We survey the main features of this approach, discussing both results that were 
already obtained, and future expected results. 
 
Throughout this article we work over a fixed base ring $\K$, which is a finite 
dimensional regular noetherian commutative ring (e.g.\ a field or the ring of 
integers $\Z$). All rings are commutative $\K$-rings, and by default they are 
essentially finite type (EFT) over $\K$.

In Section 1 we review the {\em squaring operation}. Given a ring $A$, the 
squaring operation is a functor $\opn{Sq}_{A / \K}$ from the derived category 
$\cat{D}(A)$ to itself. This is a quadratic functor, and -- unless $A$ is flat 
over $\K$ -- its construction requires the use of {\em commutative and 
noncommutative DG rings}; see \cite{Ye6}. The squaring operation has 
{\em backward functoriality} over any ring homomorphism $u : A \to B$, and 
{\em forward functoriality} when $u$ is {\em essentially \'etale}.

A {\em rigid complex} over $A$ (relative to $\K$) is a pair $(M, \rho)$, where 
$M \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$, and 
$\rho : M \iso \opn{Sq}_{A / \K}(M)$ is an isomorphism in $\cat{D}(A)$. 
There is a pretty obvious notion of {\em rigid morphism} between rigid 
complexes (see Definition \ref{dfn:235} ). This notion extends to {\em rigid 
backward morphisms} over any ring homomorphism $u : A \to B$, and to {\em rigid 
forward morphisms} when $u$ is essentially \'etale.

A {\em rigid dualizing complex} over $A$ is a rigid complex 
$(R_A, \rho_A)$ as above, such that $R_A$ is a dualizing complex over $A$ in 
the sense of \cite{RD}. This concept is discussed in Section 2. 
The ring $A$ has a rigid dualizing complex
$(R_A, \rho_A)$, and it is unique up to a unique rigid isomorphism. 
If $u : A \to B$ is a finite ring homomorphism, then there is a unique 
nondegenerate rigid backward morphism 
$\opn{tr}^{\mrm{rig}}_u : (R_B, \rho_B) \to (R_A, \rho_A)$
called the {\em rigid trace morphism}. 
If $v : A \to A'$ is an essentially \'etale ring homomorphism, then 
there is a unique nondegenerate rigid forward morphism 
$\opn{q}^{\mrm{rig}}_v : (R_A, \rho_A) \to (R_{A'}, \rho_{A'})$
called the {\em rigid \'etale-localization morphism}. The morphisms 
$\opn{tr}^{\mrm{rig}}_u$ and $\opn{q}^{\mrm{rig}}_v$
commute with each other in the appropriate sense. 

Having the rigid dualizing complex $(R_A, \rho_A)$ on every EFT $\K$-ring $A$
allows to construct the {\em twisted induction pseudofunctor}, in a
totally algebraic way (rings only, no geometry), equipped with forward and 
backward functorialities. All the material up to this point (the content of 
Sections 1-2) is in the papers \cite{Ye6} and \cite{OSY}, the latter joint 
with M. Ornaghi and S. Singh. 

Looking to the future, we plan to study a more refined object than the rigid 
dualizing complex: it is the {\em rigid residue complex} 
$(\KK_A, \rho_A)$ of a ring $A$. Given an essentially \'etale ring homomorphism 
$v : A \to A'$, there is the {\em nondegenerate rigid \'etale-localization 
homomorphism} $\opn{q}^{\mrm{res}}_{v} : \KK_{A} \to \KK_{A'}$. 
For a finite ring homomorphism $u : A \to B$ there is the {\em nondegenerate 
rigid trace homomorphism} 
$\opn{tr}^{\mrm{res}}_{u} : \KK_{B} \to \KK_{A}$. 
The latter extends to a functorial backward homomorphism 
$\opn{tr}^{\mrm{ires}}_{u} : \KK_B \to \KK_A$ 
for an arbitrary ring homomorphism $u$, called the {\em ind-rigid trace}, but 
$\opn{tr}^{\mrm{ires}}_{u}$ is only a homomorphism of graded $A$-modules.
We should stress that $\opn{q}^{\mrm{res}}_{v}$ and 
$\opn{tr}^{\mrm{res}}_{v}$ are actual homomorphisms of complexes (see Remark 
\ref{rem:295} regarding notation). 
This topic, summarized in Section 3, is planned for the paper \cite{Ye8}. 

Rigid residue complexes can be easily glued on finite type (FT) $\K$-schemes, 
and they still have the ind-rigid trace 
$\opn{tr}^{\mrm{ires}}_f : f_{*}(\KK_Y) \to \KK_X$
for an arbitrary scheme map $f : Y \to X$. The twisted induction pseudofunctor 
from Section 2 now becomes the geometric {\em  twisted inverse image 
pseudofunctor} $f \mapsto f^!$. We expect to prove the Rigid Residue Theorem
\ref{thm:1} and the Rigid Duality Theorem \ref{thm:2} for proper maps of EFT 
$\K$-schemes, thus recovering almost all the results from the original book 
“Residues and Duality” \cite{RD}, yet in a very explicit way.
This topic is covered in Section 4, and planned for the paper \cite{Ye9}. 

For every scheme $X$ the assignment $X' \mapsto \KK_{X'}$ 
is a quasi-coherent sheaf on the small \'etale site $X_{\rm{et}}$.
This implies that every finite type Deligne-Mumford (DM) $\K$-stack $\XX$ 
admits a rigid residue complex $\KK_{\XX}$. Here too we have the 
twisted inverse image pseudofunctor $f \mapsto f^!$ . For a map 
$f : \YY \to \XX$ of FT DM $\K$-stacks there is the ind-rigid trace
$\opn{tr}^{\mrm{ires}}_f : f_{*}(\KK_Y) \to \KK_X$. Under a mild 
technical condition, we expect to prove the Rigid Residue Theorem \ref{thm:10}
for proper maps of DM stacks, and the Rigid Duality Theorem \ref{thm:11} for 
such maps that are also tame. This is the content of Section 5 of the article, 
and will be written in the paper \cite{Ye10}. 

To finish the Introduction, a few words on the history of the rigid approach to 
GD. Rigid dualizing complexes were invented by M. Van den Bergh in the 1990's, 
in the noncommutative setting. This concept was imported to commutative 
algebra by J.J. Zhang and the author around 2005, where it was made functorial, 
and it was also expanded to the arithmetic setting (namely allowing a base 
ring $\K$ that is not a field). More details on the history of the topic, with 
references, can be found  in Remark \ref{rem:279}. 
Many of the ideas in this article were already mentioned in our lectures from 
2013, see \cite{Ye5}.


\medskip \noindent 
{\em Acknowledgments.}
Because this is a project spanning almost 15 years (and counting), it is 
impossible to thank all the people who had contributed to it. Therefore I shall 
only mention my collaborator James J. Zhang with whom the project began; my 
current collaborators Mattia Ornaghi and Saurabh Singh;   
Martin Olsson and Dan Edidin who assisted me in my attempts to understand 
DM stacks; and Jack Hall and Amnon Neeman who explained some of their work to 
me.  The project is currently supported by the Israel Science Foundation 
grant no.\ 824/18.
