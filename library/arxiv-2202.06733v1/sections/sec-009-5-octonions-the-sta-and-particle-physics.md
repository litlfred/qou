---
doc_id: arxiv-2202.06733v1
doc_title: "Received <day> <Month>, <year>"
section_id: sec-009-5-octonions-the-sta-and-particle-physics
section_title: "Octonions, the STA and particle physics"
section_number: 5
pages: 12-18
source_pdf: 2202.06733v1.pdf
source_sha256: e670632090447f14
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.999
doc_brief: "Received <day> <Month>, <year> — Diﬀerent ways of representing the group 푆푈(3) within a Geometric Algebra approach are explored."
---
Now, excitingly, we can start to reinterpret what we have already discussed above for the STA approach to the strong force, as a partial piece of a larger scale project for understanding the symmetries that nature may want to use. Here is a proposal:

\begin{center}
{\bf Proposal:} Nature is interested in transformations that preserve the timelike part of the STA Dirac current.
\end{center}

This is instantiated by using octonionic multiplication to represent operations upon states, since this can preserve octonionic norms, which we have said are the same thing as $J\dt\go$

This is palpably what we actually did for both the electroweak and strong force translations into the STA discussed above. For the electroweak case, we went `one further' and actually insisted the whole Dirac current was left invariant by our transformations --- this led to the $SU(2) \times U(1)$ structure.

For the strong force, then so far we can see that what we have preserved corresponds to taking just the \alert{bivector} part of $\psi$, which we wrote $F$, and demanding that

\be
\langle \go F \go F \rangle =\half\left(\go F \go F + F \go F \go\right)
\ee

be invariant --- this produced the colour forces and corresponds perfectly to what we have just been saying about preserving

\be
\half\left(\go\psi\go\psirev+\psi\go\psirev\go\right)
\ee

(note $\tilde{F}=-F$ for a bivector). Thus we must have already been doing a form of octonionic multiplication above!

Now, quite soon after quarks became established as building blocks of the Standard Model, G\"unaydin and G\"ursey\cite{gunaydin1973quark} proposed that there was a link between quark structure and the octonions. They also emphasised the role of the exceptional Lie group $G_2$ in their models, where it arises as the automorphism group of the octonions (we shall give more details about this aspect below). 

Following this, there have been many attempts to link aspects of the Standard Model to octonions, amongst them papers by Dixon (e.g.\ \cite{dixon2004division}) and Furey (e.g.\  \cite{Furey:2015tqa,Furey:2018yyy}), with these authors particularly emphasising the role of {\em chains} of octonion operators. This is a
clever technique to do with using {\em sequences} of octonions to pack in a great deal of `information' despite the relatively small size of the spaces involved. The non-associativity of the octonions is crucial to this, since then e.g.\
\begin{center}
$A(B\phi)$ for some octonions $A$ and $B$ acting on a state $\phi$
\end{center}
is {\em different} from the sequence
\begin{center}
$(AB)\phi$ also acting on $\phi$
\end{center}
The possibilities increase as we go to longer sequences, rather like a code. However, this process does not go on for ever, and as shown in the book by Conway and Smith\cite{conway2003quaternions}, 7 left multiplications or 7 right multiplications (if we build up our chains on the right instead) is the maximum we need to consider, and indeed one will be equivalent to the other (see their section 8.4, `Seven Rights can make a Left').

This means that if we consider purely left multiplications, then we should consider sequences of a maximum of 6 of these, and Furey and others (indeed it is implicit in the original G\"unaydin and G\"ursey work) show that this is isomorphic to the 6 dimensional anti-Euclidean Clifford algebra $Cl(0,6)$, i.e.\ the algebra that has all grade 1 objects squaring to $-1$, and anticommuting. That this happens we can understand quite well from the STA viewpoint. To explain this, let us look first at the example we gave above in equation (\ref{eqn:sig1-sq}) of $\sig_1 \star \sig_1$, which successfully gave $-1$.

This is {\em not} actually the type of square we are talking about here. We want to look at the action of `chains' of octonions applied at the left, so it is the application of $\sig_1$ twice which we should look at, and due to the non-associativity of the octonions, it is by no means obvious that

\be
\sig_1\star(\sig_1\star\phi) \quad \text{is equal to} \quad (\sig_1\star \sig_1) \star \phi
\ee

for a general $\phi$. Let us show, however, that this does work in this specific case, and then we will look at why it happens generally.

Let $\psi=\sigma_1$, so that $\psi_-=\sigma_1$ and $\psi_+=0$. Then using (\ref{eqn:oct-prod}), for a general Dirac spinor $\phi$, we have

\be
\sig_1 \star \phi = \phirev_-\sig_1 + \sig_1 \phirev_+
\ee

Carrying this out again, and noting now that the Pauli-even and Pauli-odd parts of $\phirev_-\sig_1 + \sig_1 \phirev_+$ are $\phirev_-\sig_1$ and $\sig_1 \phirev_+$ respectively, we get

\be
\sig_1\star(\sig_1\star\phi)=\sig_1\left(-\sig_1\phi_-\right)+\phi_+\left(-\sig_1\right)\sig_1=-\phi_--\phi_+=-\phi
\label{eqn:sig1-sq-app}
\ee

as hoped. In fact, this behaviour happens generally, since the octonions, while not associative, are what is known as an {\em alternative algebra}, which satisfies (in our STA notation)

\be
\psi\star(\psi\star\phi) =  (\psi\star \psi) \star \phi \quad \text{and} \quad (\phi\star\psi)\star \psi = \phi\star(\psi\star \psi)
\ee

for all states $\psi$ and $\phi$ in the algebra. Thus in particular, all unit elements $e_i$, $i=1,\ldots,7$ can unambiguously be described as having `square' $-1$ even when viewed in the chain sense of repeated application to the left of a state $\phi$.

In seeking to establish a correspondence with a 6d Clifford space, we also need to consider anticommutivity, and we would like to show that

\be
e_i \star \left( e_j \star \phi\right) = -e_j \star \left( e_i \star \phi\right)
\ee

for all states $\phi$, and all $i$ and $j$ from 1 to 6 with $i\neq j$. (It actually works for $i$ or $j$ equals 7 as well, but that's not needed currently.) 

The fact that the multiplication tables given above do satisfy anticommutativity, i.e.\ we have

\be
e_i \star e_j  = -e_j \star  e_i, \quad i,j=1,\ldots,7, \quad i\neq j
\ee

is not immediately relevant, due to the usual reason of non-associativity, and this time we do not have a general principle, like the alternative algebra identities, to come to our aid. However, it is fairly easy to see how this works, within the STA representation. Each of the octonion units is either Pauli-odd or Pauli-even, so we just have to consider the four possible combinations of $\theta_\pm$ and $\psi_\pm$ acting as a chain on the left of a state $\phi$.

For example, dealing with the combination which takes longest to write down, we find

\be
\theta_-\star\left(\psi_+\star\phi\right)=\psirev_+\phirev_-\theta_-+\theta_-\phirev_+\psirev_+
\ee

while

\be
\psi_+\star\left(\theta_-\star\phi\right)=\psi_+\phirev_-\theta_-+\theta_-\phirev_+\psi_+
\ee

Adding these together to form the anticommutator yields

\be
\left(\psi_++\psirev_+\right)\phirev_-\theta_-+\theta_-\phirev_+\left(\psi_++\psirev_+\right)
\ee

Now any Pauli-even non scalar quantity, i.e.\ the set $I\sig_1$, $I\sig_2$ and $I\sig_3$, is minus its own reverse, hence $\left(\psi_++\psirev_+\right)$ vanishes, as does the anticommutator, thus establishing what we wanted.

By this means, we see that $e_1$ through $e_6$, applied in chains to the left of a general state $\phi$, generate an equivalent 6d, and therefore 64 dimensional, Clifford space. It is this space, in a complexified form, which has underlain the work by Furey on linking the Standard Model with Octonions, and we see now that it is possible to represent what is happening in this space just using the STA (modulo issues about the complexification, which we return to below).

A great deal more has already been investigated and worked out by the author on this matter, and a much larger 512 dimensional space of octonionic chain states has come to light in this investigation which promises to provide a home for not just groups like $SU(3)$, $SU(2)$ and $U(1)$, which we need (in some cases in multiple copies) for the Standard Model, but for larger groups such as the exceptional group $E_8$, which has long been suspected as being highly significant in unified models of particle physics.

The details of this will be given in a separate paper (Lasenby, 2022, in preparation), and we will limit ourselves here to schematic treatments of two examples of more limited scope, and which work within just the 64 dimensional space of left-multiplication.

The first example, is of how it appears to be possible to accommodate in this space the group $SU(8)$, which we believe arises in this context as being a subgroup of the exceptional group $E_7$, which like $E_8$ has been considered several times in unified models of particle physics and string theory (e.g.\ \cite{hillmann2009generalized}). The second 
`unification', is on the use of the exceptional group $G_2$ in representing quark states. This was effectively proposed in the G\"unaydin and G\"ursey paper\cite{gunaydin1973quark}, and is in fact the first step in unification as proposed in a famous paper by Garrett Lisi, who made no connection with the octonions, but was working on the use of $E_8$ as the basic group underlying {\em all} the symmetries involved in both particle physics and gravity. The models proposed in his paper are incomplete, but the first stage, in which the much smaller exceptional group $G_2$ is used to represent both the gluons and the quarks they act upon, is fully worked out, and even though this specific group assignment is not necessarily what Nature uses, it is still of great interest to see what the approach looks like in our STA terms, and to link it with the STA approach to $SU(3)$ in Section~\ref{sect:strong-forces}.

We will start with the new approach to $SU(8)$/$E_7$, since although more complicated, the necessary states and linkages needed for the $G_2$ example become clearer if viewed in this context.


\subsection{An identification of the $SU(8)$ subgroup of $E_7$  within the 64-dimensional octonionic left multiplication space}

What we will do here is consider the full space of 64 STA states we get corresponding to the distinct chains of octonion multiplication we can carry out to the left on some initial (general) STA state $\phi$.

In seeking to interpret this in terms of a Lie algebra, we can take the operation of one state upon another as being the action of taking a {\em commutator} with that state, and we will ask for the largest set of mutually commuting states, since we can then identify this with the {\em Cartan subalgebra} of the group involved.

The notion of a Cartan subalgebra (CSA) may not be familiar to all readers, but along with several other aspects of Lie group theory, will be explained in terms of a geometric algebra approach in the Lasenby (2022) paper in preparation. Suffice to say here, that the {\em roots} of the Lie algebra are composed of eigenvalues, one for each element of the CSA, and that the whole space can be viewed as a combination of the roots and the CSA elements. The number of the latter is known as the {\em rank} of the group, and the sum of the number of roots and the rank is the dimension of the overall space.

Now the octonionic left space has the following set of 7 states arising from chains which appear to be the maximal commuting subset:

\be
\begin{gathered}
T_1=e_1 \star \left( e_2 \star \left( e_4 \star \phi\right) \right), \quad T_2=e_1 \star \left( e_5 \star \left( e_6 \star \phi\right) \right), \quad T_3=e_2 \star \left( e_3 \star \left( e_5 \star \phi\right) \right), \quad T_4=e_3 \star \left( e_4 \star \left( e_6 \star \phi\right) \right),\\
 T_5=e_1\star\left(e_2 \star \left( e_3 \star \left( e_6 \star \phi\right) \right)\right), \quad T_6=e_1\star\left(e_3 \star \left( e_4 \star \left( e_5 \star \phi\right) \right)\right), \quad T_7=e_2\star\left(e_4 \star \left( e_5 \star \left( e_6 \star \phi\right) \right)\right) 
\end{gathered}
\label{eqn:Ti-defs}
\ee

Remarkably, and definitely exciting as regards the STA approach, when expressed in terms of STA operations, these 7 states are very simple:
\be
\begin{gathered}
T_1=-\gam_0\phi\gam_0, \quad T_2=\gam_1\phi\gam_1, \quad T_3=\gam_2\phi\gam_2, \quad T_4=\gam_3\phi\gam_3,\\
 T_5=\sig_3\phi\sig_3, \quad T_6=-\sig_2\phi\sig_2, \quad T_7=-\sig_1\phi\sig_1
\end{gathered}
\ee

We see that these are the 7 distinct reflections which can be carried out using unit STA elements. Note that we can use odd elements as well since reflection in either even or odd elements preserves evenness. We do not get extra states from using any versions including $I$, however, such as trying to reflect in $I\sig_i$ or $I\gam_i$ ($i=1,2,3$), since $I$ commutes with all even elements, and we will just get a change in sign, not a new state.

We can see immediately why all these states intercommute, since although we may get sign changes when two reflecting elements are interchanged, such as interchanging $\gam_0$ and $\sig_3$, which anticommute, we will get {\em two} such sign changes due to it happening each side of $\phi$, and overall the operations will commute.

It is very nice to be able to understand how these states, $T_j$, $j=1,\ldots,7$ are singled out, in number and type, by asking that they be due to reflections in unit STA elements, which brings a geometrical flavour to what is going on, which is certainly not captured in the assignments (\ref{eqn:Ti-defs}). It is also easy to verify that these operations leave the time component of the Dirac current invariant, as required for them to be equivalent to octonionic chains.

Carrying on with understanding the states in terms of a Lie group, we will assume that the $T_j$ form the Cartan subalgebra for the group of interest, and then use them, acting via a commutator product, to act on combinations of other states in the algebra in such a way as to give eigenvalues and eigenvectors. Specifically, we are looking for states which are simultaneously eigenvectors of all the $T_j$, $j=1,\ldots,7$, and the seven eigenvalues so found will give us the root vectors in an abstract 7d space corresponding to the seven $T_j$.

We will not give the details here, but we find that the 56 states left from the original 64 when we remove the identity and the seven $T_j$, split up into 7 groups of 8 states, each of which (i.e.\ the 8 elements of a given grouping) has non-zero eigenvalues with 4 of the $T_j$. The number of ways of choosing 4 things from 7 is of course 35, but one finds that each of the $T_j$ appears a total of 4 times, in the sense of having non-zero eigenvalues, and this limits the overall number of groupings to 7, as stated.

The net effect is to give us 56 root vectors in the abstract space of the $T_j$. Since the rank is 7 and the number of root vectors is 56, we initially believed that what we have got here is a particular version of the group $E_7$, plus one additional state, which is just the identity. The group $E_7$ is normally considered to have 133 dimensions and therefore 126 roots. However, it does also have a 56 dimensional representation (e.g.\ \cite{Brown+1969+79+102}), which is used for example in string theory\cite{hillmann2009generalized}. 
Having constructed the {\em Cartan matrix} for the roots we have found, it now appears that instead we are dealing with the group $SU(8)$, which indeed has 56 root vectors and 7 CSA vectors in the adjoint representation. This is still strongly linked to $E_7$, however, since it is a subgroup of $E_7$, and the two occur together jointly as part of the foundation of {\em supergravity theories} (see e.g.\ \cite{CREMMER1979141}).

More generally, it will be very interesting to see if the larger space of `STA states' referred to above allows a representation of the full $E_8$, and how this ties in with existing Geometric Algebra techniques for analysis of $E_8$ being used by Pierre Dechant\cite{dechant20178}, which have already shone an interesting and fresh light on the root structure of $E_8$. We should also mention the work of integrating the group $E_6$ with octonions, carried out over some years by Tevian Dray and Corrine Manogue (e.g.\ \cite{Manogue_2010}), and which is another example of explicitly seeking to integrate exceptional groups, particle physics and octonions, and for which we hope there will be interesting analogues within the STA.


\subsection{The group $G_2$ and the representation of quarks and gluons via the STA}

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
