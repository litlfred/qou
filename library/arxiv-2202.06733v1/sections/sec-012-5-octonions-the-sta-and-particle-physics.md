---
doc_id: arxiv-2202.06733v1
doc_title: "Received <day> <Month>, <year>"
section_id: sec-012-5-octonions-the-sta-and-particle-physics
section_title: "Octonions, the STA and particle physics"
section_number: 5
pages: 12-14
source_pdf: 2202.06733v1.pdf
source_sha256: e670632090447f14
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 1.0
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
