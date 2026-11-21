---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions"
section_id: sec-002-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
toc_source: outline
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions — We prove a new convergence condition for the activity expansion of correlation functions in equilibrium statistical mechanics"
---
Since its introduction by Mayer in the early 40s, the method of cluster expansions was—and
remains—a very important tool in equilibrium statistical mechanics. A classical application
yields the analyticity of the logarithm of the partition function for a physical system at
equilibrium by deriving a Taylor expansion in the activity or density parameter around zero.
Such results can be quite useful, for example, in the study of phase transitions or the decay
of correlations, for a vast class of models.
In 1971, Gruber and Kunz introduced in their seminal paper [12] systems of non-
overlapping geometric objects—referred to as polymers—given by subsets of a lattice. They
Communicated by Yvan Velenik.
B Leonid Kolesnikov
kolesni@math.lmu.de
1
Mathematisches Institut, Ludwig-Maximilians-Universität, Theresienstr. 39, 80333 Munich,
Germany
2
Munich Center for Quantum Science and Technology (MCQST), Schellingstr. 4, 80799 Munich,
Germany
33
Page 2 of 47
S. Jansen, L. Kolesnikov
presented a rigorous mathematical formalism in order to provide convergent cluster expan-
sions for this model. Instead of the logarithm of the partition function, they considered the
correlation functions of the system and derived convergent activity expansions by using a
system of integral equations, the so-called Kirkwood–Salsburg equations, and solving the
corresponding ﬁxed point equation on a suitable Banach space. However, in the following
years less analytical appoaches were favoured by researchers: Combinatorial proofs such
as in [3], relying on tree-graph identities [23], and inductive proofs following the idea by
Kotecký and Preiss [18] and its development in [4] by Dobrushin. The inductive method was
presented in the more general setup of abstract polymers (where the underlying space is not
necessarily a lattice, nor are the polymers necessarily given by geometric objects). Notice
that abstract polymer models are universal in the sense that a large class of classical models
can be represented as polymer models due to the combinatorial structure of the correspond-
ing partition functions (see, e.g., [11] for an application to the Ising model). Moreover, an
interesting connection with probability theory was pointed out by Scott and Sokal in [29]:
Convergence of cluster expansions in abstract polymer models is related to the Lovász Local
Lemma—better sufﬁcient conditions can provide reﬁnements of the latter (see, e.g., [2]).
In 2008, Fernández and Procacci proved a new sufﬁcient criterion in the setup of abstract
polymers improving on the result by Kotecký and Preiss. The initial proof [8] relies on
combinatorial arguments, an alternative proof via an induction à la Dobrushin [10] appeared
recently (ﬁnally, in this paper we provide an analytical proof in the spirit of Gruber–Kunz).
Overall, in the last two decades, a notable effort was made to generalize classical suf-
ﬁcient conditions in the abstract polymer setup (including the condition by Fernández and
Procacci) to hold in continuous spaces and for systems with soft-core (or even more general)
interactions, see [5, 14, 22, 24, 32].
We want to go further by employing a Kirkwood–Salsburg approach in the rather general
setup of Gibbs point processes (or, in terms of statistical mechanics, grand-canonical Gibbs
measures) deﬁned via pairwise interactions. It is well-known that—under mild additional
moment conditions, which are automatically satisﬁed for non-negative pair potentials—there
is a one-to-one correspondence between the set of those Gibbs measures and the associated
families of correlation functions (also known as factorial moment densities). In the special
caseofadiscretespaceandhard-coreinteractions,thevalueofthen-pointcorrelationfunction
is given simply by the probability to see n particles at the prescribed positions in the random
conﬁguration of particles. The correlation functions can be expanded as power series in the
activity parameter z, i.e., in the intensity of the underlying Poisson process. We denote the
Taylor expansion for the n-point correlation function in z around zero by ρn and write ρ
for the family of those expansions. In general, the series ρ need not to be convergent at all;
we are, however, interested in conditions which ensure pointwise convergence (towards the
correlation functions). Furthermore, we want to consider the more general case where the
underlying Poisson point process is inhomogeneous, i.e., where a different intensity value
may be assigned to every point in the space, the activity z is a function and the expansions
ρ are multivariate power series in z. For a rigorous introduction of Gibbs point processes
and corresponding correlation functions, see [14], but notice that here we do not assume the
interaction potential to be non-negative (unless explicitly stated).
The starting point of the paper and the central quantity to investigate are the activity
expansions ρ which we consider independently of their interpretation in term of the cor-
relation functions. Let us outline the main ideas present in the paper. The coefﬁcients of
the multivariate power series ρ are deﬁned in terms of a certain family of rooted graphs
to which we refer as multi-rooted graphs (see [14, 30]). Using the terminology from [6],
the activity expansions ρ are given by the exponential generating functions of the coloured
Cluster Expansions: Necessary...
Page 3 of 47
33
weighted combinatorial species of multi-rooted graphs with a ﬁxed set of roots. The set of all
multi-rooted graphs has an essential structural property—it is invariant under the operation
of removal of a root. Taking a multi-rooted graph and removing an arbitrary root (as well as
all edges incident to it), one gets again a multi-rooted graph on a smaller vertex set, where
every neighbour of the removed root becomes a root vertex itself. The weight of the original
graph is equal to the weight of the resulting graph times the weight of the edges removed. The
corresponding property of the generating functions is expressed by the Kirkwood–Salsburg
equations. Every possible rule for the choice of the root to remove induces a different combi-
natorial operation and therefore a different system of Kirkwood–Salsburg equations for the
generating functions.
In this work we provide a condition for absolute convergence of the activity expansionsρ in
terms of the existence of a measurable function solving a system of Kirkwood–Salsburg type
inequalities (in the case of repulsive interactions, that condition is also a necessary one). Our
main result, Theorem 2.1, is inspired by [1]; it is a slightly modiﬁed, strongly generalized
version of Claim 1 therein. The goal, however, is not only to obtain abstract conditions
which are both necessary and sufﬁcient for convergence of the cluster expansions—but also
to demonstrate how these characterizations provide a universal approach to prove model-
speciﬁc sufﬁcient conditions on different levels of generality, both in discrete and continuous
setups with repulsive interactions. A two-lane mechanism arises: On the one hand, for a
candidate family of ansatz functions ξ (given, for example, as approximations of ρ) one
can search for conditions that ensure that these functions ξ satisfy the Kirkwood–Salsburg
inequalities; on the other hand, given candidate sufﬁcient conditions, one can construct a
suitable family of ansatz functions ξ tailored to satisfy the Kirkwood–Salsburg inequalities
under these conditions.
This approach provides a unifying framework for the known conditions, but it also allows
to prove stronger results. To emphasize this possibility, we derive a new sufﬁcient condition
for absolute convergence of the activity expansions ρ in the setup of abstract polymers. In
that general setup, our condition improves on any known condition that we are aware of.
A more detailed outline of the main ideas intoduced above can be found in [16] (for the
case of non-negative pairwise interactions and without rigorous proofs).
In the further course of the paper, we investigate two particular hard-core setups as
examples—the subset polymers in Zd and hard objects in Rd. There, the sets of roots of
the multi-rooted graphs correspond to conﬁgurations of geometric objects. By breaking the
geometric objects into smaller “pieces” to which we refer as snippets, we can identify these
conﬁgurations with conﬁgurations of snippets (e.g., in the case of subset polymers we can
identify a conﬁguration of polymers with the disjoint union of monomers covering this con-
ﬁguration). Picking a root of a multi-rooted graph—the combinatorial operation underlying
the Kirkwood–Salsburg equations—corresponds to picking a snippet. Different rules to pick
a snippet in general give rise to characterizations of absolute convergence in terms of dif-
ferent Kirkwood–Salsburg inequalities. This way the latter can be tailored to a candidate
sufﬁcient condition. Thus different sufﬁcient conditions can be derived by playing both with
the choice of different systems of Kirkwood–Salsburg inequalities and the choice of different
ansatz functions satisfying these inequalities. We illustrate this mechanism by deriving some
sufﬁcient conditions for a class of hard-core interaction models, in particular for multi-type
systems of hard spheres in Rd.
The paper is organized as follows: In Sect. 2.1 we introduce the basic notation and present
the general framework. Furthermore, in Theorem 2.1 we state our main result, a character-
ization of the domain of absolute convergence for the activity expansions ρ, and use it to
recreate the classical sufﬁcient conditions by Kotecký and Preiss as well as the sufﬁcient
33
Page 4 of 47
S. Jansen, L. Kolesnikov
conditions by Fernández and Procacci in a rather general setup (see Corollaries 2.7 and 2.9,
respectively). In Sect. 2.2, the same approach is used to prove a new, improved sufﬁcient con-
dition in the setup of abstract polymers (Proposition 2.4). The proof of the proposition relies
on an auxiliary result (Lemma 2.5) which is proved in Appendix A. In the Sects. 2.3 and 2.4
we consider the special case of hard-core interactions. Both in the continuum (Sect. 2.3) and
in the discrete setup (Sect. 2.4), we provide model-speciﬁc characterizations of the conver-
gence domain, stated in Theorems 2.6 and 2.7, respectively. As an immediate consequence
of Theorem 2.7 we obtain an elementary proof of the well known Gruber–Kunz condition
(Corollary 2.8). In Sect. 3, we present a forest-graph equality and other combinatorial results
in order to prove Theorems 2.1, 2.6 and 2.7. Finally, in Sect. 4, Theorems 2.6 and 2.7 are used
to obtain practitioner-type sufﬁcient conditions for a class of hard-core interaction models,
including new sufﬁcient conditions for subset polymers in Zd (Theorem 4.1) and hard objects
in Rd (Theorems 4.2 and 4.4).
The reader interested primarily in the discrete setup of subset polymers is encouraged
to jump directly to Subsect. 2.4, its main result being the characterization of the domain of
convergence for the activity expansions ρ given by Theorem 2.7 (compare to Theorem 3.13).
The main ideas behind the proof of Theorem 2.7 in Subsect. 3.4 and behind the application
of Theorem 2.7 in Subsect. 4.1 can be transferred to the continuous setup as well.
