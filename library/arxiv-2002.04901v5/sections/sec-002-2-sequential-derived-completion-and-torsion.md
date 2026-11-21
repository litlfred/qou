---
doc_id: arxiv-2002.04901v5
doc_title: "Weak Proregularity, Derived Completion, Adic Flatness, and Prisms"
section_id: sec-002-2-sequential-derived-completion-and-torsion
section_title: "Sequential Derived Completion and Torsion"
section_number: 2
pages: 6-10
source_pdf: 2002.04901v5.pdf
source_sha256: f1320c4b87229215
toc_source: outline
text_source: latex
latex_prose_ratio: 0.997
latex_coverage_ratio: 0.984
doc_brief: "Weak Proregularity, Derived Completion, Adic Flatness, and Prisms — We begin by recalling the role that weak proregularity of an ideal in a commu- tative ring has in derived completion and adic"
---
\label{sec:sequential}

Here again $A$ is a commutative ring. A finite sequence 
$\aa = (a_1, \ldots, a_n)$ of elements of $A$ gives rise to several complexes 
of $A$-modules. 

We start with a single element $a \in A$. For an $A$-module $M$
we denote by 
$\opn{mult}_M(a) : M  \to M$ the endomorphism
$\opn{mult}_M(a)(m) := a \cd m$. 

Recall that the {\em Koszul complex} associated to the element $a$ is 
\begin{equation} \label{eqn:101}
\opn{K}(A; a) := \bigl( \cdots \to 0 \to A \xar{\d} A \to 0 \to  
\cdots \bigr) , 
\end{equation}
concentrated in degrees $-1$ and $0$. 
The differential is $\d := \opn{mult}_A(a)$.
For $j \geq i$ in $\N$ there is a homomorphism of complexes 
\begin{equation} \label{eqn:197}
\mu_{j, i} : \opn{K}(A; a^{j}) \to \opn{K}(A; a^{i}) , 
\end{equation}
which is the identity in degree $0$, and $\opn{mult}_A(a^{j - i})$ in degree 
$-1$. 

Now consider a sequence of elements $\bsym{a} = (a_1, \ldots, a_n)$.
The associated Koszul complex is 
\begin{equation} \label{eqn:190}
\opn{K}(A; \bsym{a}) := 
\opn{K}(A; a_1) \ot_A \cdots \ot_A \opn{K}(A; a_n) . 
\end{equation}
This is a complex of finite rank free $A$-modules, concentrated in degrees 
$-n, \ldots, 0$. For $i \in \N$ let 
$\bsym{a}^i := (a^i_1, \ldots, a^i_n)$.
The homomorphism (\ref{eqn:197}) induces a homomorphism of complexes
$\mu_{j, i} : \opn{K}(A; \bsym{a}^j) \to \opn{K}(A; \bsym{a}^i)$,
making the collection of Koszul complexes 
$\bigl\{  \opn{K}(A; \bsym{a}^i) \bigr\}_{i \in \N}$
into an inverse system.

As an aside, let us mention that the Koszul complex $\opn{K}(A; \aa)$ is a 
{\em commutative DG ring} (in the sense of \cite[Definition 3.3.4]{Ye3}), and 
there is a DG ring homomorphism $A \to  \opn{K}(A; \aa)$. 
The inverse system 
$\bigl\{  \opn{K}(A; \bsym{a}^i) \bigr\}_{i \in \N}$
is of DG $A$-rings. 

The second complex we associate to the sequence $\aa$ is the {\em infinite 
dual Koszul complex}. It is
\begin{equation} \label{eqn:151}
\opn{K}^{\vee}_{\infty}(A; \aa) := 
\lim_{i \to} \, \opn{Hom}_{A} \bigl( \opn{K}(A; \aa^i), A \bigr) .
\end{equation}
This is a complex of flat $A$-modules, concentrated in degrees 
$0, \ldots, n$. 

The DG ring homomorphisms $A \to \opn{K}(A; \aa^i)$ induce, upon dualizing and 
passage to the limit, a homomorphism of complexes 
\begin{equation} \label{eqn:205}
\opn{K}^{\vee}_{\infty}(A; \aa) \to A . 
\end{equation}
We sometimes refer to this homomorphism as the {\em augmentation} of
$\opn{K}^{\vee}_{\infty}(A; \aa)$.

The complex $\opn{K}^{\vee}_{\infty}(A; \aa)$ has an alternative description. 
For a single element $a \in A$, its infinite dual Koszul complex admits this 
canonical isomorphism 
\begin{equation} \label{eqn:191}
\opn{K}^{\vee}_{\infty}(A; a) \cong 
\bigl( \cdots \to 0 \to A \xar{\d} A_a \to 0 \to  
\cdots \bigr) , 
\end{equation}
with $A$ in degree $0$, the localized ring $A_a = A[a^{-1}]$ in degree $1$, 
and the differential $\d$ is the ring homomorphism. For a sequence 
$\bsym{a} = (a_1, \ldots, a_n)$ there is an isomorphism 
\begin{equation} \label{eqn:195}
\opn{K}^{\vee}_{\infty}(A; \aa) \cong 
\opn{K}^{\vee}_{\infty}(A; a_1) \ot_A \cdots \ot_A 
\opn{K}^{\vee}_{\infty}(A; a_n) . 
\end{equation}

The third complex associated to the sequence $\aa$ is the {\em \v{C}ech complex}
$\opn{C}(A; \aa)$. This is also a bounded complex of flat $A$-modules.
This complex is more familiar in its algebro-geometric formulation, as follows.
Let $X := \opn{Spec}(A)$, let $U_i := \opn{Spec}(A[a_i^{-1}])$ be the principal 
affine open set in $X$ defined by the element $a_i$, and let 
$U := \bigcup_i U_i \sub X$. Then $\opn{C}(A; \aa)$ is the 
\v{C}ech complex associated to the affine open covering 
$\{ U_i \}_{i = 1, \ldots, n}$ of $U$. 
So $\opn{C}(A; \aa)$ is a complex of flat $A$-modules, concentrated in 
degrees $0, \ldots, n-1$.   
Actually, $\opn{C}(A; \aa)$ has a canonical structure of noncommutative central 
DG $A$-ring, see \cite[Section 8]{PSY}, and as such it is called the {\em 
derived localization of $A$ w.r.t.\ $\aa$}. 
When $n = 1$ and $a_1 = a$ this is a familiar commutative ring:
$\opn{C}(A; a) = A[a^{-1}]$. 

There is a canonical short exact sequence of complexes of $A$-modules 
\begin{equation} \label{eqn:40}
0 \to \opn{C}(A; \aa)[-1] \to \opn{K}^{\vee}_{\infty}(A; \aa) \to A \to 0 , 
\end{equation}
in which the augmentation (\ref{eqn:205}) occurs.
For this reason, the complex $\opn{K}^{\vee}_{\infty}(A; \aa)$
can also be called the {\em augmented \v{C}ech complex}. 

There is a fourth complex of $A$-modules that's canonically associated to $\aa$.
It is the {\em telescope complex} $\opn{Tel}(A; \aa)$, which is a complex of 
countable rank free $A$-modules, concentrated in degrees $0, \ldots, n$. 
The formula for $\opn{Tel}(A; \aa)$ is elementary but a bit messy; see 
\cite[Definition 5.1]{PSY}.
There is a canonical quasi-isomorphism 
\begin{equation} \label{eqn:166}
w_{\aa} : \opn{Tel}(A; \aa) \to \opn{K}^{\vee}_{\infty}(A; \aa) . 
\end{equation}
See \cite[Lemma 5.7]{PSY}.

The complexes $\opn{K}(A; \aa)$, $\opn{K}^{\vee}_{\infty}(A; \aa)$,
$\opn{C}(A; \aa)$ and $\opn{Tel}(A; \aa)$ are all {\em defined over $\Z$}, in 
the following sense. Consider the polynomial ring $\Z[\tt]$ in the sequence of 
variables $\tt = (t_1, \ldots, t_n)$. As a special case of the constructions 
above, there are complexes of $\Z[\tt]$-modules
$\opn{K}(\Z[\tt]; \tt)$, $\opn{K}^{\vee}_{\infty}(\Z[\tt]; \tt)$,
$\opn{C}(\Z[\tt]; \tt)$ and $\opn{Tel}(\Z[\tt]; \tt)$. The sequence 
$\aa =  (a_1, \ldots, a_n)$ in $A$ determines a ring 
homomorphism $\Z[\tt] \to A$ sending $t_i \mapsto a_i$, and under this 
homomorphism we 
obtain isomorphisms 
\begin{equation} \label{eqn:164}
\begin{aligned}
A \ot_{\Z[\tt]} \opn{K}(\Z[\tt]; \tt) & \iso \opn{K}(A; \aa) 
\\
A \ot_{\Z[\tt]} \opn{K}^{\vee}_{\infty}(\Z[\tt]; \tt) & \iso 
\opn{K}^{\vee}_{\infty}(A; \aa) 
\\
A \ot_{\Z[\tt]} \opn{C}(\Z[\tt]; \tt) & \iso \opn{C}(A; \aa) 
\\
A \ot_{\Z[\tt]} \opn{Tel}(\Z[\tt]; \tt) & \iso \opn{Tel}(A; \aa)
\end{aligned}
\end{equation}
of complexes of $A$-modules.

The next definitions are based on material from several papers and the book 
[LC]. A priori they appear to have no relation to their parallels in the 
previous section, beyond the hint we have in formula (\ref{eqn:215}). 
Understanding that they are indeed what their names suggest (e.g.\ derived 
torsion in Definition \ref{dfn:195}) requires some work. Moreover, these 
definitions agree with those in Section \ref{sec:idealistic} precisely when 
{\em weak proregularity} holds. 

On the other hand, the definitions in this section have the distinct advantage 
of being rather easy to manipulate, and their ``adjunction'',  
``universality'' and ``idempotence'' features are not hard to verify, 
as explained in Remarks \ref{rem:216}, \ref{rem:217} and \ref{rem:251}.

\begin{dfn} \label{dfn:195}
Let $\aa = (a_1, \ldots, a_n)$ be a finite sequence in the ring $A$. 
The {\em sequential derived $\aa$-torsion functor}
is the functor 
\[ \opn{K}^{\vee}_{\infty}(A; \aa) \ot_A (-) : \cat{D}(A) \to \cat{D}(A) . \]
\end{dfn}

The definition makes sense: the complex 
$\opn{K}^{\vee}_{\infty}(A; \aa)$ K-flat, and hence tensoring with it respects 
quasi-isomorphisms.

A hint that this is related to torsion is this: let $\a$ be the ideal in $A$ 
generated by the sequence $\aa$. From formulas (\ref{eqn:191}) and 
(\ref{eqn:195}) it is clear that 
for an $A$-module $M$ there is a canonical isomorphism 
\begin{equation} \label{eqn:215}
\Ga_{\a}(M) \cong \opn{H}^0 \bigl( \opn{K}^{\vee}_{\infty}(A; \aa) \ot_A 
M \bigr) .
\end{equation}

Given a complex of $A$-modules $M$, let 
\begin{equation} \label{eqn:196} 
\si_{\aa, M}^{\mrm{R}} : 
\opn{K}^{\vee}_{\infty}(A; \aa) \ot_A M \to  M 
\end{equation}
be the morphism in $\cat{D}(A)$ arising from the augmentation homomorphism
$\opn{K}^{\vee}_{\infty}(A; \aa) \to A$ in (\ref{eqn:205}). 

\begin{dfn} \label{dfn:196} 
A complex $M \in \cat{D}(A)$ is called {\em derived $\aa$-torsion  
in the sequential sense} if the morphism  
$\si_{\aa, M}^{\mrm{R}}$ in (\ref{eqn:196}) is an isomorphism. 
\end{dfn}

\begin{dfn} \label{dfn:197} 
Let $\aa = (a_1, \ldots, a_n)$ be a finite sequence in the ring $A$. 
The {\em sequential derived $\aa$-adic completion functor}
is the functor 
\[ \opn{RHom}_{A} \bigl( \opn{K}^{\vee}_{\infty}(A; \aa), - \bigr) : 
\cat{D}(A) \to \cat{D}(A) . \]
\end{dfn}

The augmentation of $\opn{K}^{\vee}_{\infty}(A; \aa)$ induces, for every 
$M \in \cat{D}(A)$, a morphism 
\begin{equation} \label{eqn:200} 
\tau_{\aa, M}^{\mrm{L}} : M \to 
\opn{RHom}_{A} \bigl( \opn{K}^{\vee}_{\infty}(A; \aa), M \bigr) . 
\end{equation}

\begin{dfn} \label{dfn:201}  
A complex $M \in \cat{D}(A)$ is called {\em derived $\aa$-adically  
complete in the sequential sense} if the morphism  
$\tau_{\aa, M}^{\mrm{L}}$ in (\ref{eqn:200}) is an isomorphism. 
\end{dfn}

\begin{prop} \label{prop:200} 
Let $\aa = (a_1, \ldots, a_n)$ be a sequence in the ring $A$. 
The following are equivalent for $M \in \cat{D}(A)$.
\begin{itemize}
\rmitem{i} $M$ is derived $\aa$-adically complete in the sequential sense
(Definition \ref{dfn:201}). 

\rmitem{ii} The object 
$\opn{RHom}_A \bigl( \opn{C}(A; \aa), M \bigr)$ 
in $\cat{D}(A)$ is zero. 
\end{itemize}
\end{prop}

\begin{proof}
The exact sequence (\ref{eqn:40}) gives a distinguished triangle 
\[  \opn{C}(A; \aa)[-1] \to \opn{K}^{\vee}_{\infty}(A; \aa) \to A 
\xar{\, \triangle \, } \]
in $\cat{D}(A)$. Applying the functor 
$\opn{RHom}_A(-, M)$ to this triangle, we get a new distinguished triangle 
\[ M \xar{\tau_{\aa, M}^{\mrm{L}}}
\opn{RHom}_{A} \bigl( \opn{K}^{\vee}_{\infty}(A; \aa), M \bigr) \to 
\opn{RHom}_A \bigl( \opn{C}(A; \aa), M \bigr) \xar{\, \triangle \, } \]
in $\cat{D}(A)$. By a standard fact on distinguished triangles, the morphism 
$\tau_{\aa, M}^{\mrm{L}}$ is an isomorphism iff the object 
$\opn{RHom}_A \bigl( \opn{C}(A; \aa), M \bigr)$ is zero. 
\end{proof}

\begin{rem} \label{rem:215}
Condition (ii) in Proposition \ref{prop:200} was the definition of a {\em 
cohomologically complete complex} in \cite{KS2}, in the special case when 
$n = 1$, so that, writing $a := a_1$, we have 
$\opn{C}(A; \aa) = A[a^{-1}]$.
\end{rem}

Here is the sequential variant of Proposition \ref{prop:210}.

\begin{prop} \label{prop:215}
Let $\aa$ and $\bb$ be finite sequences of elements of $A$, and let 
$\a$ and $\b$ the ideals of $A$ generated by the sequences $\aa$ and $\bb$ 
respectively. Assume that $\sqrt{\a} = \sqrt{\b}$. Then there is a canonical 
isomorphism 
$\opn{K}^{\vee}_{\infty}(A; \aa) \cong \opn{K}^{\vee}_{\infty}(A; \bb)$
in $\cat{D}(A)$, which respects the augmentations to $A$.

Therefore the sequential derived $\aa$-torsion and $\aa$-adic completion 
functors are isomorphic to the  sequential derived $\bb$-torsion and 
$\bb$-adic completion functors, respectively. 
\end{prop}

\begin{proof}
In \cite[Theorem 6.1]{PSY} it is proved that the complexes 
$\opn{Tel}(A; \aa)$ and $\opn{Tel}(A; \bb)$
are homotopy equivalent. An inspection of the proof of 
\cite[Theorem 6.1]{PSY} shows that this homotopy equivalence is canonical, and 
it respects the augmentations of the telescope complexes to $A$ (up to 
homotopy). The quasi-isomorphism (\ref{eqn:166}) lets us translate these facts 
to isomorphisms in $\cat{D}(A)$. 
\end{proof}

\begin{rem} \label{rem:216}
The sequential derived functors are insensitive to the ring $A$, or are 
universal, in the following sense. Consider derived completion. Since there is 
the canonical quasi-isomorphism (\ref{eqn:166}), and since $\opn{Tel}(A; \aa)$ 
is a K-projective complex, the sequential derived completion of a complex $M$ 
is 
$\opn{Hom}_A \bigl( \opn{Tel}(A; \aa), M \bigr) \in \cat{D}(A)$.
However, the telescope complex is defined over $\Z$, as shown in the last 
formula in (\ref{eqn:164}). This means that when we pass to the derived 
category $\cat{D}(\Z[\tt])$ by the restriction functor, we get 
\[ \opn{Hom}_A \bigl( \opn{Tel}(A; \aa), M \bigr) \cong 
\opn{Hom}_{\Z[\tt]} \bigl( \opn{Tel}(\Z[\tt]; \tt), M \bigr) \in 
\cat{D}(\Z[\tt]) . \]
\end{rem}

\begin{rem} \label{rem:217}
The sequential derived completion and torsion functors are adjoint to each 
other, for a trivial reason. This is an easy version of {\em Greenlees-May 
Duality}. 

Once more, we present these functors using the 
telescope complex $T := \opn{Tel}(A; \aa)$, which is a bounded complex of 
free $A$-modules, canonically quasi-isomorphic to 
$\opn{K}^{\vee}_{\infty}(A; \aa)$. 
Then the sequential derived $\aa$-adic completion of a complex $M$ is 
$\opn{Hom}_A(T, M)$, and the sequential derived $\aa$-torsion of $M$ is 
$T \ot_A M$.  

An easy calculation using Hom-tensor adjunction shows that 
for for arbitrary $M, N \in \cat{D}(A)$ there is a 
canonical isomorphism 
\[ \opn{Hom}_{\cat{D}(A)} (T \ot_A M, N) \cong 
\opn{Hom}_{\cat{D}(A)}(M, \opn{Hom}_A(T,  N)) . \]
\end{rem}

\begin{rem} \label{rem:251}
Another nice property of the sequential derived completion functor is that it 
is always {\em idempotent}. Using the notation $T := \opn{Tel}(A; \aa)$
of the previous remark, the augmentation homomorphism $T \to A$ 
induces two homomorphisms of complexes 
$T \ot_A T \to T$; and according to \cite[Lemma 7.9]{PSY} these are homotopy 
equivalences. Therefore for every $M \in \cat{D}(A)$ the two morphisms 
\[ \opn{Hom}_A(T, M) \to \opn{Hom}_A(T, \opn{Hom}_A(T, M)) \]
in $\cat{D}(A)$ are isomorphisms.
\end{rem}

\begin{rem} \label{rem:220}
Positselski has a much deeper understanding of various aspects of completion 
and  derived completion, including some intermediate operations between what we 
call the idealistic and the sequential derived completions. These are 
summarized in his paper \cite{Po}, where precise references can be found.  

For instance, fix a finite sequence $\aa = (a_1, \ldots, a_n)$ in $A$.
An $A$-module $M$ that is derived $\aa$-adically complete as a 
complex (in the sequential sense) is called an {\em $\aa$-contramodule}. 
For $M \in \cat{M}(A)$ to be an $\aa$-contramodule it is necessary and 
sufficient that $\opn{Ext}^q_A(A[a_i^{-1}], M) = 0$ for all 
$q = 0, 1$ and $i = 1, \ldots, n$. 

Let $\cat{M}_{\aa \tup{-ctra}}(A)$
be the full subcategory of $\cat{M}(A)$ on the $\aa$-contramodules. 
Positselski proves that $\cat{M}_{\aa \tup{-ctra}}(A)$
is a full abelian subcategory, closed under extensions. 
Another feature of contramodules is this: a complex $M \in \cat{D}(A)$ is 
derived $\aa$-adically complete (in the sequential sense) iff all its 
cohomology modules $\opn{H}^q(M)$ are $\aa$-contramodules. 

Here is one more consequence of Positselski's methods. Let $\a$ be the ideal 
generated by $\aa$. He proves that every complex $M$ that is derived 
$\a$-adically complete in the idealistic sense is also derived 
$\aa$-adically complete in the sequential sense; but not vice versa. See 
\cite[Lemma 5.1 and Proposition 5.3]{Po}.
\end{rem}
