---
doc_id: arxiv-2202.06733v1
doc_title: "Received <day> <Month>, <year>"
section_id: sec-013-51-an-identification-of-the-su8-subgroup-of-e7-w
section_title: "An identification of the SU(8) subgroup of E7 within the 64-dimensional octonionic left multiplication space"
section_number: 5.1
pages: 14-15
source_pdf: 2202.06733v1.pdf
source_sha256: e670632090447f14
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 1.0
doc_brief: "Received <day> <Month>, <year> — Diﬀerent ways of representing the group 푆푈(3) within a Geometric Algebra approach are explored."
---
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
