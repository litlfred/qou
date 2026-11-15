---
doc_id: arxiv-0911.4494v2
doc_title: "The geometry of Markov traces"
section_id: sec-004-4-a-categorified-trace
section_title: "A categorified trace"
section_number: 4
pages: 5-9
source_pdf: 0911.4494v2.pdf
source_sha256: 1ba1c79686b12d98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.966
doc_brief: "The geometry of Markov traces — We give a geometric interpretation of the Jones-Ocneanu trace on the Hecke algebra, using the equivariant cohomology of sheaves on SLn."
---
\label{sec:categorified-trace}

Let $\BD\subset\BB$ be the diagonal subgroup.  Then we can associate
to $\IC_w$ and $S_w$ bigraded vector spaces $\hc_{\BD}\!(\IC_w)$ and
$\HH^*(S_w)$, the $\BD$-equivariant cohomology and Hochschild
homology respectively.

The bigrading on $\HH^*(S_a)$ is easy to describe: one grading, which
we call the {\bf $t$-grading}, is given by the homological grading on
$\HH^*$ and one is given by the
fact that $S_a$ is a graded bimodule over polynomials, with linear
polynomials in degree 2.  For reasons of knot theory,  we follow the convention of \cite{MSV} with respect to the grading on Hochschild homology: we normalize the gradings so that the differential on Hochschild homology has bidegree $(1,1)$.

The bigrading on $\hc_{\BD}\!(\IC_w)$ is of geometric origin, but less
obvious than the algebraic grading.  What we must use is the weight
grading on cohomology.  
By previous work of the authors \cite[Theorem
1.4]{WW}, there is an isomorphism $\hc_{\BD}\!(\IC_w)\cong \HH^*(S_w)$,
which sends the $q$-grading to the usual cohomological grading and the
$t$-grading to the weight plus cohomological grading, i.e.\ that given
by the norm of the eigenvalue of Frobenius.



Thus, we let
$\mathbb{H}_{\BD}^{i;j}(G;\IC_w)$ be subspace of
$\mathbb{H}_{\BD}^{i}(G;\IC_w)$ of weight $j$. In all situations
encountered below, Frobenius will always act semi-simply via powers of our fixed $q^{\nicefrac 12}$ and hence $\mathbb{H}_{\BD}^{i;j}(G; \IC_w)$ is equal to the $q^{\nicefrac{j}{2}}$-eigenspace of $\mathbb{H}_{\BD}^{i}(G; \IC_w)$ for the action of Frobenius.










\begin{defi} \label{defi-mPs}
Given a sheaf $\F \in D^b_{\BD}(G)$, its
  {\bf mixed Poincar\'e series} is
  \begin{equation*}
    P_{\F}(q,t)=\dim_{q,t}\hc_{\BD}\!(G;\F)=\sum_{i,j}\dim\mathbb{H}_{\BD}^{i;j}(G;\F)q^{\nicefrac{i}{2}}t^{j-i}.
  \end{equation*}
\end{defi}

We will always consider equivariant mixed Poincar\'e polynomials, and only specify the group if there is danger of confusion. Note that
\begin{equation} \label{shifttwist}
P_{\F\langle -i \rangle }(q,t) = q^{\nicefrac i2} P_{\F}(q,t).
\end{equation}







As before, $\Gamma$ is a Dynkin diagram, and we let
$\Gamma'=\Gamma-\{v\}$ for a single vertex $v$, and
$\iota:\Hec_{\Gamma'}\to \Hec_{\Gamma}$ is the induced inclusion.

\begin{thm}\label{main-theorem}
  The linear extension of the function
  $\Tr_\Gamma(C_w^{\prime})=\dim_{q,t}\hc_{\BD}\!(\IC_w) =
  P_{\IC_w}(q,t)$ only depends on the root system of $G$ and is a trace on
  $\Hec_{\Gamma}$. Furthermore, for each vertex $v$, we have
\begin{align*}
\label{norm1}  \Tr_{\emptyset}(1)&=1 &
\Tr_{\Gamma}(\si_{v}\iota(a))&= -t \cdot
\Tr_{\Gamma'}(a)\\ \Tr_{\Gamma}(\iota(a))&=\frac{1+ q^{\nicefrac 12}t}{1-q}\cdot
\Tr_{\Gamma'}(a) &
\Tr_{\Gamma}(\si_{v}^{-1}\iota(a))&=q^{- \nicefrac 12}\cdot \Tr_{\Gamma'}(a)
\end{align*}
In particular, when $\Gamma=A_n$, this trace coincides with that of
Jones-Ocneanu.  Furthermore, in the case where $\Gamma=B_n,C_n,D_n$,
it is the trace $\Tr_\Gamma^{-t}$ given in
Proposition \ref{markov-B}, where $y=-t$.
\end{thm}
This establishes that this trace pulled back to the braid group provides a knot invariant (up to normalization), called the HOMFLYPT
polynomial in the type $A$ case, and an invariant of knots in the
solid torus in type $B$, by the ``cylindrical Markov theorem'' (see \cite{GL}). 

\begin{proof}[Proof of Theorem \ref{main-theorem}]
We first show that our trace only depends on the root system of
the semi-simple group $G$, and not on its root datum. To this end let
\[
\phi : \widetilde{G} \to G
\]
denote a central isogeny and set $\widetilde{B} := \phi^{-1}(B)$. We
denote by $\widetilde{\IC}_w$ the intersection cohomology
complex on $\widetilde{G}$, normalized as in Definition
\ref{def:ICnorm}. We claim there is a canonical isomorphism:
\[
\hc_{{B}_{\Delta}}(G, \IC_w) \cong \hc_{\widetilde{B}_{\Delta}}(\widetilde{G}, \widetilde{\IC}_w).
\]

First note that $(\phi^*, \phi_*)$ give an equivalence
\[
D^b_{\widetilde{B} \times \widetilde{B}}(\widetilde{G})
\stackrel{\sim}{\to} D^b_{\widetilde{B} \times B}(G)
\]
and hence the
adjunction morphism $\F \to \phi_* \phi^* \F$ is an isomorphism for any $\F \in D^b_{\widetilde{B} \times B}(G)$. It
follows that
\[
\hc_{\widetilde{B}_{\Delta}}(G, \IC_w) \stackrel{\sim}{\to}
\hc_{\widetilde{B}_{\Delta}}(\widetilde{G}, \phi^*\IC_w)
= \hc_{\widetilde{B}_{\Delta}}(\widetilde{G}, \widetilde{\IC}_w)
\]
Lastly $\hc_{\widetilde{B}_{\Delta}}(G, \IC_w) = \hc_{{B}_{\Delta}}(G,
\IC_w)$ because $K = \ker \phi$ is a finite group and our coefficients are of
characteristic zero.

Our definition yields a trace since for sheaves $\F, \F^{\prime} \in D^b_{\BB}(G)$ we have
  \begin{equation*}
    \hc_{\BD}\!(G;\F\star\F')\cong \hc_{B\times B}(G\times G;\F\boxtimes\F')\cong \hc_{\BD}\!(G;\F'\star\F).
  \end{equation*}
where the $B \times B$-action on $G \times G$ in the equation above is given by
\[
(b_1, b_2) \cdot (g_1, g_2) = (b_1g_1b_2^{-1}, b_2g_2b_1^{-1}).
\]
It follows that $\Tr_{\emptyset}(1)=1$ since if $\Gamma = \emptyset$ then $G$ is the trivial group.

It remains to verify the behaviour of our trace under an inclusion
$\iota$. To do this we give a geometric interpretation of $\iota$. 
By the above considerations we may assume that $G$ is of
adjoint type. Now let $\Delta \subset R$
denote the based root system of $(G,B,T)$.  The inclusion $\Gamma
\subset \Gamma'$ determines a based root system $\Delta' \subset R'$ with an inclusion into  $\Delta \subset R$
such that $\Delta = \Delta' \cup \{ \alpha \}$ where $\alpha$ is the
simple root corresponding to the new vertex $v$ of $\Gamma$.

Now let $G'$ denote the closed subgroup of $G$ generated by root
subgroups and cocharacters corresponding to roots in $R'$, and let
$\widetilde{G'} = G'T$. Then $G'$ is a semi-simple algebraic group
with root system $R'$ and $\widetilde{G'} \cong G' \times \Gm$,
because we have assumed that $G$ is adjoint.
If we set \[
T' := T
\cap G', \qquad \widetilde{T'} := T, \qquad B' := B \cap G'\qquad  \text{and}\qquad \widetilde{B'}
:= B \cap \widetilde{G'}
\] then $T'$ and $\widetilde{T'}$ (respectively
$B'$ and $\widetilde{B'}$) are split maximal tori (respectively Borel
subgroups) of $G'$ and $\widetilde{G'}$.

  The projection and inclusion maps
\[
 G' \stackrel{p}{\leftarrow} \widetilde{G'}
 \stackrel{i}{\hookrightarrow} G
\]
induce functors $$p^* \colon D^b_{B' \times B'}(G) \to D^b_{\widetilde{B'} \times
  \widetilde{B'}}(G')\qquad\text{ and }\qquad i_* \colon D^b_{\widetilde{B'} \times
  \widetilde{B'}}(G') \to D^b_{\widetilde{B'} \times
  \widetilde{B'}}(G).$$ We define
\begin{eqnarray*}
 \gio_* : D^b_{B' \times B'} (G') \longrightarrow & D^b_{B \times B} (G) \\
\F \longmapsto & \ind^{B \times B}_{\widetilde{B'} \times
  \widetilde{B'}}i_* p^* \F.
\end{eqnarray*}
If $w' \in W_{\Gamma'}$ and $w$ denotes its image under the natural inclusion
$W_{\Gamma'} \hookrightarrow
W_{\Gamma}$ then one has $\gio_*( \IC_{w'}) \cong \IC_w$ because
$B/\widetilde{B'}$ is isomorphic to an affine space. 
Hence $\gio_*$ categorifies the inclusion $\iota : \Hec_{\Gamma'} \to
\Hec_{\Gamma'}$ under the identifications in Theorem
\ref{thm-heckeconv}.

Now, let $P\subset G$ be the minimal standard parabolic corresponding
to $\alpha \in \Delta$. Given $\F \in D^b_{B' \times B}(G')_0$  it remains to calculate the Poincar\'e series of the cohomology groups 
\[
\hc_{B_{\Delta}}(\Cs{B}\star \gio_* \F) \cong \hc_{B_{\Delta}}(\gio_* \F)\qquad 
\text{ and }\qquad 
\hc_{B_{\Delta}}(\Cs{P}\star \gio_* \F)
\]
in terms of $\hc_{B'_{\Delta}}( \F)$. It will be easier to work instead with
$T_{\Delta}$-equivariant cohomology, which is equivalent because
$B_{\Delta}/ T_{\Delta}$ is isomorphic to an affine space.

First note that, as $\widetilde{G'} \cong G' \times \Gm$ we have, by
the K\"unneth formula,
\begin{equation}\label{eq:Gm}
\hc_{T_{\Delta}}(\gio_* \F) \cong \hc_{T'_{\Delta}} (\F) \otimes \hc_{\Gm}(\Gm)
\end{equation}
(where $\Gm$ acts trivially on $\Gm$ in the second factor).

It remains to calculate $\hc_{B_{\Delta}}(\Cs{P}\star \gio_* \F)$.
Set $Z := (\ker \alpha)^0$ and let $L = C_G(Z)$ be its centralizer in
$G$. We can write $T \cong Z \times T_{v}$, with $\Gm \cong T_v$ via
the fundamental coweight corresponding to $\alpha$ (which belongs to
the cocharacter lattice because $G$ is of adjoint type). 

Now we have a Levi decomposition $P = LU$, where $U$ denotes the
unipotent radical of $P$. Hence we have a $T \times T$-equivariant
map $P \to L$ with fibers isomorphic to affine spaces. Moreover, $H :=
L/Z$ is a semi-simple group of rank 1. It follows that we have an acyclic $T
\times T$-equivariant map
\[
P \times_{T} \widetilde{G'} \to H \times G'.
\]
Moreover, the induced conjugation actions of $Z$ (resp. $T_v$) on $H$
(resp. $G'$) are trivial.

Hence
\begin{equation} \label{eq:SL2}
\hc_{T_{\Delta}}(G, \Cs{P}\star \gio_* \F)
\cong \hc_{(T_v)_\Delta}(H)  \otimes \hc_{Z_{\Delta}}(G', \F)
\end{equation}

Taking Poincar\'e series in the equations (\ref{eq:Gm},\ref{eq:SL2}), we get the relations
\begin{gather*}
    \Tr(\iota(a))=
\dim_{q,t} \hc_{B_{\Delta}}(\gio_* \F)
=\frac{1 + q^{\nicefrac 12}t}{1-q}\Tr(a)\\
\Tr(C^{\prime}_v\iota(a)) =
\dim_{q,t}\hc_{T_{\Delta}}(G, \Cs{P}\star \gio_* \F \langle 1 \rangle)
=\frac{q^{-\nicefrac{1}{2}} + qt}{1-q}\Tr(a)
\end{gather*}
This establishes one of our conditions.  For the others, we first
observe that $\si_v=C^{\prime}_v-q^{- \nicefrac{1}{2}}$ and $\si_v^{-1}=C^{\prime}_v-q^{\nicefrac{1}{2}}$.  This shows that
\begin{align*}
  \Tr(\si_v\iota(a))&=\frac{qt -t}{1-q}\cdot \Tr(a)&\Tr(\si_v^{-1}\iota(a))& = \frac{ q^{-\nicefrac 12} -q^{ \nicefrac 12 } }{1 - q}
  
  \cdot \Tr(a)\\
  &=-t\cdot \Tr(a)&&=q^{- \nicefrac 12}\cdot \Tr(a).
\end{align*}

Finally, we must establish our claim that
\begin{equation*}
  \Tr_{B_{n+1}}(T_{n}\iota(a)) = -t \cdot \Tr_{B_n}(a)
\end{equation*}
This follows from Corollary~\ref{final}, which shows that our trace
coincides with that considered by Gomi and from \cite[\S 4.4 \& 
4.5]{Gomi} where Gomi shows that his trace corresponds to that
constructed by Geck and Lambropoulou, which has this property by \cite[Proposition 4.5]{GL}.
\end{proof}

\begin{question} The above proof uses the Gomi's algebraic calculations to deduce that our trace satisfies all the conditions in Definition \ref{markov-B} for $y = -t$. We do not know whether the extra conditions in types $B$, $C$ and $D$ have a geometric explanation.
\end{question}
