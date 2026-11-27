The idea that matter is made of knots is older than the electron. In
1858 Helmholtz proved that in an ideal fluid a vortex line is carried
along by the flow and the strength of a vortex tube does not change in
time \cite{helmholtz1858}. A closed vortex ring therefore cannot be
created, destroyed or cut by the motion of the fluid, and if it is
knotted it keeps its knot type. Tait reproduced the effect with smoke
rings, and in 1867 William Thomson, later Lord Kelvin, proposed that
atoms are vortex rings in a perfect fluid filling space, the ether
\cite{thomson1867vortexatoms}. Helmholtz's theorems supplied the
permanence of atoms, the different ways a ring can be knotted or linked
supplied the variety of chemical elements, and the vibrations of a ring
were to supply its spectral lines.

The programme drew in the leading mathematical physicists of the time.
Maxwell took it seriously, and his *Treatise* records Gauss's double
integral for the number of times one closed curve winds around another,
the linking number \cite{maxwell1873treatise2}. A periodic table of
vortex atoms needed a table of knots, and Tait set out to make one
\cite{tait1877knots}. With Thomas Kirkman and Charles Little he
classified knot diagrams up to ten crossings, and in doing so stated
the conjectures on crossing number, writhe and flypes that bear his
name. The first of these was proved a century later, in 1987,
independently by Kauffman, Murasugi and Thistlethwaite, with the Jones
polynomial \cite{jones1985} \cite{kauffman1987} \cite{murasugi1987}
\cite{thistlethwaite1987}; Menasco and Thistlethwaite proved the
flyping conjecture in 1991 \cite{menasco-thistlethwaite1991}
\cite{menasco-thistlethwaite1993}.

The vortex atom itself did not survive. The ether was given up, the
electron was found inside the atom, and by about 1900 the theory had
been abandoned; the knot tables remained and became the start of knot
theory as a branch of mathematics \cite{kragh2002vortexatom}
\cite{silver2006knotorigins} \cite{przytycki2007knothistory}. The
link between knots and physics returned in other forms. Moffatt
identified the helicity of a fluid as a measure of the knottedness of
its vortex lines \cite{moffatt1969}. Witten obtained the Jones
polynomial from a quantum field theory \cite{witten1989}. Faddeev and
Niemi found stable knotted solitons in a classical field theory
\cite{faddeevniemi1997}. Kleckner and Irvine created knotted vortex
rings in water and watched them evolve \cite{kleckner2013}, and Kedia,
Bialynicki-Birula, Peralta-Salas and Irvine constructed knotted
solutions of Maxwell's equations \cite{arxiv-1302.0342v1}. Closest to
this chapter, Joel Avrin modelled the elementary fermions by twisted
bands whose boundaries are the unknot and the trefoil, an independent
knot-to-particle dictionary \cite{avrin-2012}. Two algebraic programmes
also assign elementary particles to quantum knots or three-strand
braids: Robert J. Finkelstein mapped fermions and electroweak states
directly to irreducible $\mathrm{SU}_q(2)$ matrix elements $D^j_{mm'}$
labelled by knot crossing number, writhe, and diagram rotation
\cite{finkelstein2007,finkelstein2008}, while Sundance Bilson-Thompson
\cite{bilson-thompson2005}, Sundance Bilson-Thompson, Fotini
Markopoulou, and Lee Smolin \cite{bilsonthompson2007}, and Sundance
Bilson-Thompson, Jonathan Hackett, and Louis H. Kauffman
\cite{bilson-thompson-hackett-kauffman2009} represented first-generation
fermions and gauge bosons as framed ribbons in $B_3$ whose electric
charges are read off $\pm 2\pi$ ribbon twists in units of $e/3$. The
construction in this chapter differs from both: instead of indexing
single-particle states by $D^j_{mm'}$ matrix entries or reading electric
charge from external ribbon twists, it works in the finite-dimensional
quotient $H_3(q)$ generated from the $\mathcal{O}_q(\mathrm{SU}(2))$
braiding on $B_3$ and evaluates observables through the convention-D
Markov trace.

The braid lineage continued through division algebras. Gresnigt used
the Clifford braiding theorem of Kauffman and Lomonaco
\cite{kauffman-lomonaco-2016} to show that the complex numbers and the
quaternions carry representations of exactly the two braid groups of
the Bilson-Thompson model, the braid group $B_2$ of the twists and the
circular braid group $B_3^c$ of the ribbons \cite{gresnigt2017}. He then
identified the framed braids with the basis states of the minimal left
ideals of the complex octonions, which, following Furey
\cite{furey2016}, carry one generation of leptons and quarks under the
unbroken symmetry $SU(3)_c \times U(1)_{\mathrm{em}}$ \cite{gresnigt2018}.
Chester, Arsiwalla and Kauffman mapped the twists of the same states
onto the weight lattice of $SU(3)_c \times U(1)_{\mathrm{em}}$ and the
crossings onto chirality through the homomorphism
$B_3 \to PSL(2,\mathbb{Z})$, and observed that the model captures only
that unbroken sector \cite{chester-arsiwalla-kauffman-2025}. In these
programmes the braid acts through a group, and a deformation parameter,
where one appears, sits beside the braiding rather than in it: in
Gresnigt's review the quantum group $SU_q(3)$ is a flavour symmetry with
$q$ a root of unity \cite{gresnigt2017}, and in Finkelstein's model $q$
deforms the symmetry of the knot. Here every generator of $H_n(q)$
satisfies $\sigma_i - \sigma_i^{-1} = (q - q^{-1})\mathbf{1}$ with $q$
a formal parameter, so a particle can be a linear combination of braid
words rather than a single braid, as the four-term
[photon](#def:photon) is.

This chapter keeps the combinatorial half of that lineage and drops the
mechanical half. The vortex atom tried to derive the stability of matter
from the dynamics of a medium. Here a knot or link type is the label of
an algebraic object, a closed braid together with its word in the
Iwahori–Hecke algebra, and the question of stability becomes a question
about what is invariant under the braid and Markov moves. Naming a
construction after a particle is a convention inside the model, and the
history above motivates the choice of objects without entering any
definition or proof.
