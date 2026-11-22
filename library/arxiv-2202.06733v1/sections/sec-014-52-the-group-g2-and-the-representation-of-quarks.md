---
doc_id: arxiv-2202.06733v1
doc_title: "Received <day> <Month>, <year>"
section_id: sec-014-52-the-group-g2-and-the-representation-of-quarks
section_title: "The group G2 and the representation of quarks and gluons via the STA"
section_number: 5.2
pages: 15-18
source_pdf: 2202.06733v1.pdf
source_sha256: e670632090447f14
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 1.0
doc_brief: "Received <day> <Month>, <year> — Diﬀerent ways of representing the group 푆푈(3) within a Geometric Algebra approach are explored."
---
\label{sect:G2-and-quarks}

Turning to the other example we want to consider, the most direct way to approach this that we have found, starts from the 7 groups of 8 states each just discussed. Each group of 8 itself breaks into two groups of 4, distinguished by the mutual commutation of each of the 4 elements in a given split. One of these two subgroups (we are using `group' and `subgroup' in a non-technical way at this point, just to indicate a collection of objects) contains $e_i\star\phi$ and this happens for each of the 7 sets of 8, $i=1,\ldots,7$. We label the three remaining states in the $i$'th subgroup

\be
J_{1i}, \quad J_{2i}, \quad J_{3i}
\ee

and from what has already been said, all three mutually commute for a given $i$. Note calling these objects $J$'s is motivated by the fact that for $i=7$, then the differences between the three $J$'s match the differences between the $J_1$, $J_2$ and $J_3$ defined above in the context of the STA approach to $SU(3)$ in equation (\ref{eqn:hats-def}), i.e.\ we have

\be
J_{17}-J_{27}=\hat{J}_1-\hat{J}_2, \quad J_{27}-J_{37}=\hat{J}_2-\hat{J}_3, \quad J_{37}-J_{17}=\hat{J}_3-\hat{J}_1
\label{eqn:J-diffs}
\ee

This is important, since in the next step we indeed use differences between the $J$'s to define the quantities which are the generators of what we interpret as $G_2$. Specifically, we define 14 quantities $F_i$ and $M_i$ via

\be
F_i = \half\left(J_{1i}-J_{2i}\right), \quad M_i = {\textstyle \frac{\sqrt{3}}{6}}\left(\left(J_{1i}-J_{3i}\right)+\left(J_{2i}-J_{3i}\right)\right) = {\textstyle \frac{\sqrt{3}}{6}}\left(J_{1i}+J_{2i}-2J_{3i}\right)
\ee

Using equation (\ref{eqn:J-diffs}) in conjunction with the relationships to the Gell-Mann matrices given in equation (\ref{eqn:lambda-defs}), we can see immediately that we can identify $F_7$ with the generator $\lambda_3$ and $M_7$ with $\lambda_8$.

We will not go through the details here, but more generally, by comparing their STA effects, we find the identifications

\be
F_1 \leftrightarrow \lambda_7, \quad F_2 \leftrightarrow \lambda_5, \quad F_3 \leftrightarrow \lambda_6, \quad F_4 \leftrightarrow \lambda_2, \quad F_5 \leftrightarrow \lambda_1, \quad F_6 \leftrightarrow \lambda_4, \quad F_7 \leftrightarrow \lambda_3
\ee
and we have already said $M_7\leftrightarrow\lambda_8$. Thus we have all 8 $SU(3)$ generators present, along with another 6 new generators, the $M_i$, $i=1,\ldots,6$. The total 14 is the set of generators of the exceptional group $G_2$.

Now remarkably, although there is a very different starting point in terms of our 7 groups of 8 elements, the position we have just reached with $G_2$ is the same picture as already found by G\"unaydin and G\"ursey in 1973, when considering an octonionic model for quarks\cite{gunaydin1973quark}. Indeed, we have adopted their notation of $F$ and $M$ for the $SU(3)$ and (additional) $G_2$ generators, and they also use $J$ for the elements from which everything is assembled, though this choice was made independently in the current work.

However, as well as the starting point in terms of the organisation of states being different, we have the advantage here of being able to represent everything concretely in terms of the STA. We know this already for the $F_i$, since these are just the $\lambda$'s, and it is of interest to find expressions for the $J_{ki}$ themselves, since we can then form both the $F$'s and $M$'s from them via differences. To give an example, the $J_{k2}$, $k=1,2,3$ differences can be formed as follows:

\be
J_{12}-J_{22}=\phi I\sig_2 - I\sig_2 \phi, \quad J_{22}-J_{32}=I\sig_2 \left(\phi-\gam_0\phi\gam_0\right), \quad J_{32}-J_{12}=\phi I\sig_2 - I\sig_2 \gam_0\phi\gam_0
\ee

These are very simple, and are revealing in terms of how they involve $-I\sig_2$, which is the second octonion unit, and show how this quantity enters the second grouping of 8 states.

More generally, we can think of the $J_{ki}$ as corresponding to `rotations' amongst the unit octonions which will preserve the $i$'th one, whilst inducing rotations in pairs in the rest. It is in this sense $G_2$ arises as the {\em automorphism group} of the octonions. The restriction to {\em differences} of the $J$'s in doing this cuts out the 7 possible additional generators

\be
N_i = J_{1i}+J_{2i}+J_{3i}, \quad i=1,\ldots,7
\ee

in an exactly analogous way as $U(3)$ was restricted to $SU(3)$ by the condition on the $\alpha$'s given in equation (\ref{eqn:alpha-restriction}) above. As discussed in \cite{gunaydin1973quark}, the combination of the 14 $G_2$ generators and the additional $N_i$ generators just listed, yields 21 generators in total, which we can identify as the special orthogonal group of rotations in 7d space, $SO(7)$, which is known as a subgroup of $E_7$, tying in with our interpretation of what the full space of the left chains is.

To validate the identification of the group $G_2$, we need to show that as well as having 14 generators, it has rank two, and with a root diagram matching that expected. This brings us into contact with the approach used by Garrett Lisi\cite{Lisi:2007gv}.
Lisi does not consider octonions, and instead the important constructs are the Lie algebra elements treated in an abstract way, with their actions on one another being carried out via Lie brackets, and with the quantum numbers of the associated particles being `weights' within the root system of various exceptional Lie groups. We will only give brief details here, and will limit ourselves to just one example, but this will indicate how we can give a concrete version of this process, within the octonionic chain setup, and therefore also within the STA.

The example we use is the starting point of Lisi's study, which is about using $SU(3)$ to describe the gluons of the colour force, which is of course standard, but then as discussed in Section~2.1 of \cite{Lisi:2007gv}, using the 6 extra dimensions which $G_2$ introduces relative to the $SU(3)$ algebra which is embedded within it, to describe the quarks themselves. In particle physics notation, these are in a $\boldmath{3} + \bar{\boldmath{3}}$ `triplet' plus `anti-triplet' state.

Since everything (in this approach) is expressed in terms of the root vectors, we need to specify the Cartan subalgebra we are going to use. For this we need to have available all the commutation relations between our 14 generators (the $F_i$ and $M_i$ for $i=1,\ldots,7$), and we will list these in the more detailed publication to follow. However, this shows that the maximal size of a commuting subset is 2, which correctly corresponds to the rank of $G_2$. Here we will identify $F_7$ and $M_7$ as the CSA, since these work for both $SU(3)$ and the full $G_2$. So we need to find the simultaneous eigenvectors, using sums of the remaining 12 generators, and their asssociated eigenvalues (the Lie group `weights') under commutation with $F_7$ and $M_7$.

At this point we find a difference with what we are apparently able to do in term of forming combinations of states, and what Lisi, Furey and others are able to do, which relates to the question of whether we need to admit a commuting unit scalar imaginary into our system.

So far we have used only STA elements in everything we have done, apart from the first discussion of $SU(3)$ in Section~\ref{sect:first-su3}. The STA does not include a scalar imaginary $i$, but we have nevertheless been able to reach a long way into study of the octonionic chains, and also the groups $E_7$ and $G_2$, and this is perhaps remarkable in itself.

Other authors, e.g. Furey\cite{Furey:2015tqa,Furey:2018yyy}, bring in $i$ at the very beginning of their work, for example in the definitions of the $SU(3)$ elements, and Lisi brings in $i$ to his work at this point in his Section~2.1 in forming `complex' combinations of $SU(3)$ elements, of the form (in Gell-Mann matrix terms) $\lambda_2\pm i \lambda_1$, $\lambda_5\pm i \lambda_4$ and $\lambda_7\pm i \lambda_6$. The point about these combinations (6 of them), is that they are able to be simultaneous eigenvectors of the matrix equivalents of our two CSA elements, namely of $\lambda_3$ and $\lambda_8$. Without forming complex combinations, and treating each generator individually, one finds that one in any case needs imaginary eigenvalues, so again an $i$ has to be apparently introduced.

We can avoid this to some extent in our approach, by working with {\em ordered pairs} of states, which we can conveniently represent via a row vector, so for example, the 6 states just described would be

\be
\begin{pmatrix} F_4, & \pm F_5 \end{pmatrix}, \quad \begin{pmatrix} F_2, & \pm F_6 \end{pmatrix}, \quad \begin{pmatrix} F_1, & \pm F_3 \end{pmatrix}
\label{eqn:six-gluon-states}
\ee


Taking the simplest example, let us consider the action of the CSA elements $F_7$ and $M_7$ on the first of these pairs of states. Writing e.g.\

\be
F_7 \begin{pmatrix} F_4, & F_5 \end{pmatrix} \quad \text{to mean}  \quad \half\begin{pmatrix}  [F_7,F_4], & [F_7,F_5] \end{pmatrix}
\ee

where $[\ ,\ ]$ is the commutator, then we find

\be
F_7 \begin{pmatrix} F_4, & F_5 \end{pmatrix} = \begin{pmatrix} F_4, & F_5 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} , \quad F_7 \begin{pmatrix} F_4, & -F_5 \end{pmatrix} =- \begin{pmatrix} F_4, & -F_5 \end{pmatrix}\begin{pmatrix} 0 & -1\\  1 & 0 \end{pmatrix} , \quad \text{and} \quad M_7 \begin{pmatrix} F_4, & \pm F_5 \end{pmatrix} =0
\label{eqn:eigenvec-example}
\ee

This translates through, in Garrett Lisi's terms, to the pair $\begin{pmatrix} F_4, & \pm F_5 \end{pmatrix}$ being simultaneous eigenvectors of $\lambda_3$ and $\lambda_8$ (our $F_7$ and $M_7$ respectively), with weights in the 2d root space of $(1,0)$ and $(-1,0)$. To state this further in a particle context, we note that Lisi would identify $\begin{pmatrix} F_4, & F_5 \end{pmatrix}$ as an anti-red green gluon and $\begin{pmatrix} F_4, & -F_5 \end{pmatrix}$ as a red anti-green gluon. We can then continue with the other two pairs of states in (\ref{eqn:six-gluon-states}) and similarly, via equations like (\ref{eqn:eigenvec-example}), find their root vector weights in the 2d CSA of $F_7$ and $M_7$, and these match exactly with those found for the various gluon states in Lisi.

While implemented in a novel fashion, what we are looking at here is at an abstract level just the usual aspects of $SU(3)$ in relation to the colour force. What Lisi does next is to suggest identifying the remaining 6 generators of $G_2$ with the quark states themselves. He does not give explicit details of this identification, but just works out the weights of the corresponding root vectors in the CSA space.

In our terms, we can give an explicit version of this as follows. We define three quark states, $q_1$, $q_2$, $q_3$, along with three anti-quark states, $\bar{q}_1$, $\bar{q}_2$, $\bar{q}_3$ via the ordered pairs

\be
q_1 = \begin{pmatrix} M_3, & M_1 \end{pmatrix}, \quad \bar{q}_1 = \begin{pmatrix} M_3, & -M_1 \end{pmatrix}, \quad q_2 = \begin{pmatrix} M_2, & -M_6 \end{pmatrix}, \quad \bar{q}_2 = \begin{pmatrix} M_2, & M_6 \end{pmatrix}, \quad q_3 = \begin{pmatrix} M_5, & -M_4 \end{pmatrix}, \quad \bar{q}_3 = \begin{pmatrix} M_5, & M_4 \end{pmatrix}
\label{eqn:quark-states}
\ee


The interactions of the gluons with the quarks are then represented by the actions of the $F_1$, \ldots, $F_7$ and $M_7$ $SU(3)$ generators with these quark states, carried out as usual by commutators. The particular combinations in (\ref{eqn:quark-states}) are each eigenvectors of what we can call the `hypercharge' operator, which in the current context turns out to be the operator

\be
Q=\frac{1}{2}\left(\frac{1}{\sqrt{3}}M_7 + F_7\right)
\ee

Using the multiplication properties of the $F$'s and $M$'s, we find the corresponding eigenvalues are (respectively) $+2/3$ and $-2/3$ for $q_1$ and $\bar{q}_1$; $-1/3$ and $+1/3$ for $q_2$ and $\bar{q}_2$ and $1/3$ and $-1/3$ for for $q_3$ and $\bar{q}_3$, which fits in well with their identification as quark states. Note looking at the eigenvalues w.r.t.\ $F_7$ and $M_7$ individually, we find that these line up precisely to give the remaining 6 roots in the root diagram of $G_2$, as stated by Lisi, confirming that in the STA version we are indeed working with $G_2$.

Additionally we can consider the action of the remaining $F$'s on these 6 $M$ states. We find that the combinations given in (\ref{eqn:six-gluon-states}), identified as gluon states, move the quarks around within the three $q_i$ and within the three $\bar{q_i}$ states, though do not mix them. This again corresponds well to what we would expect for a `triplet' and `anti-triplet' set of quark states being acted upon, so overall we have a concrete representation of the gluon and quark states, and their interactions, all expressible within the STA. However, as we have seen, this is modulo questions about whether we in fact need a commutative scalar imaginary $i$ to make this work.

Addressing this, it might be possible to argue that equation (\ref{eqn:eigenvec-example}) is just a way of organising our knowledge about the algebraic relations satisfied by the $F_i$ and $M_i$, which have all been worked out (ultimately in the STA), without any importation of a scalar unit imaginary $i$. This is a possible way of thinking, but on the other hand, one way of introducing complex numbers is precisely via introducing ordered pairs of real numbers, along with a way of flipping between the two states of a pair, as in the matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$. Thus it could be argued that we do indeed need to introduce what is effectively a `tensor product' of the octonionic chain states with the complex numbers $\mathbb{C}$, precisely as hypothesised at the beginning of e.g.\ the work by Cohl Furey. We will return to this question in the more detailed work to follow, and propose a slightly different resolution of the question there. In the meantime, we reiterate that it is only for the `packaging' of the octonionic STA states into pairs that we currently need constructions like (\ref{eqn:eigenvec-example}), and this has happened right at the end of our developments, rather than being an intrinsic part of the beginning.
