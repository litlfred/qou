---
doc_id: arxiv-2004.04939v1
doc_title: "BRAID GROUP ACTION ON THE MODULE CATEGORY OF"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2004.04939v1.pdf
source_sha256: 59a06f9f7d97cad2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.883
doc_brief: "BRAID GROUP ACTION ON THE MODULE CATEGORY OF — Let g0 be a simple Lie algebra of type ADE and let U ′ q(g) be the corre- sponding untwisted quantum aﬃne algebra."
---
The monoidal category $\catC_\g$ of  finite-dimensional representations of a quantum affine algebra $\uqpg$ has been extensively investigated because of its rich structure. 
Among various approaches,  Nakajima (\cite{Nak04}), Varagnolo-Vasserot (\cite{VV03}), and Hernandez (\cite{Her04})  studied $t$-deformations of the Grothendieck ring of $\catC_\g$. 
These $t$-deformations are interesting, because they provide a way to calculate the $q$-character of simple representations. 
There is  a full subcategory $\catC^0_\g$ of $\catC_\g$, introduced by Hernandez and Leclerc in \cite{HL10},   which contains an essential information 
on $\catC_\g$ but  has a smaller set of the classes of simple modules. 

The Grothendieck ring of  $\catC^0_\g$ is isomorphic to the polynomial ring in countably many variables, while that of $\catC_\g$ is the one in  uncountably many variables.
For the cases where $\g$ is one  of  untwisted ADE types, a $t$-deformation  $\Kt(\g)$ of the Grothendieck ring of $\catC^0_\g$, called the \emph{quantum Grothendieck ring},  
was investigated from a ring theoretic point of view in \cite{HL13}.
It turns out that the $\C(t^{1/2})$-algebra $\Kt(\g)$ has an interesting presentation: there is  a set of generators consisting of a countable infinite number of copies of Drinfeld-Jimbo generators of a half  of the quantum group $U_t (\g_0)$,  and they satisfy the quantum Serre relations in a copy, $t$-boson relations between adjacent copies,  and $t$-commutation relations between  non-adjacent copies. 
This presentation reflects the following feature of the category   $\catC_\g^{0}$: 
for each choice of a Dynkin quiver $Q$ with an additional data,  they defined
a monoidal subcategory $\catC_Q$ of $\catC_\g^{0}$ such that  the quantum Grothendieck ring of $\catC_Q$ is isomorphic to the half  $U^-_t (\g_0)$ of the quantum group $U_t (\g_0)$, and  all the fundamental representations in  $\catC_\g^{0}$ can be obtained from those in $\catC_Q$ by taking 
functors $\D^m$ ($m\in\Z$).
Here $\D$ is the contravariant
functor taking the right dual.
 


One of  main results of this paper is that there exists an action of the braid group $B(\g_0)$ of type $\g_0$ on the quantum Grothendieck ring $\Kt(\g)$ (Theorem~\ref{thm: braid group action}).
Since we give the action explicitly, the braid relations  can be checked by the presentation of $\Kt(\g)$. 
Recall that the blocks of the category $\catC_\g^0$ is parameterized by the root lattice of $\g_0$ and the tensor product is compatible with the addition on the root lattice (\cite{KKOP20}).
It turns out that the action of  the generators $\brd_i$ of $B(\g_0)$ on $\Kt(\g)$ correspond to the reflections with respect to the simple roots $\al_i$ on the root lattice. 
Indeed, the action of $\brd_i$ is related with Saito's reflection functor
as seen in  Theorem~\ref{Saito}.

We conjecture that the braid group action can be lifted to the action on the monoidal category $\catC_\g^0$.

We show that it is the case when $\g$ is of  type $A_{N-1}^{(1)}$. 
A key point of view is the use of a rigid monoidal category $\T_N$ which is constructed out of the category $\catA$ of finite-dimensional graded modules over the quiver Hecke algebra $R^{A_\infty}$ of type $A_\infty$ (\cite{KKK18A}).
It is a certain localization of $\catA$ and  
there is a monoidal functor $\F_N$ from $\T_N$ to $\catC^0_{A_{N-1}^{(1)}}$ which sends simple objects to simple objects. Moreover this functor induces an isomorphism between the Grothendieck ring  
$K(\T_N)$ and the quantum Grothendieck ring $\Kt(A_{N-1}^{(1)})$.
It is summarized by the diagram
$$K(\T_N)\isoto \Kt(A_{N-1}^{(1)})\To[\ {t=1}\ ] K(\catC^0_{A_{N-1}^{(1)}}).$$
Hence  the category $\T_N$ can be understood as a \emph{graded lift} of $\catC^0_{A_{N-1}^{(1)}}$ as a rigid monoidal category.

We  show that there is a family of monoidal autofunctors  $\{\Refl_i\}_{1\le i \le N-1}$ on the category  $\T_N$ which recover the action of the braid group $B(A_{N-1})$ under the  isomorphism between $K(\T_N)$  and $\Kt({A^{(1)}_{N-1}})$ (Theorem \ref{thm: reflection functors}, Theorem \ref{thm:functors recover the action}).
There is a  general procedure, developed in \cite{KP},  to construct monoidal functors between the  categories of modules over quiver Hecke algebras, and a similar procedure can be applied for the category $\T_N$. 
This is a main advantage in working on the category $\T_N$ rather than the category $\catC^{0}_{A_{N-1}}$.

Finally we  provide several consequences of 
the existence of such functors $\Refl_i$. 
For a simple object $L$ which belongs to an orbit of $L(i)$ 
for some $i$ under the action $B(A_{N-1})$, 
one can define an automorphism $s_L$ which has similar properties
with the automorphisms $s_i$ (Theorem \ref{thm: reflection by root modules}). 
Moreover $s_{L(i)}$ coincides with $s_i$.

\smallskip
This paper is an announcement whose details will appear elsewhere.
