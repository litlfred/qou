---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-011-12-motivation
section_title: "Motivation"
section_number: 1.2
pages: 20-23
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
All the current continuous space nuclear QMC calculations (such as GFMC and
AFDMC) are performed within the framework of DMC. Due to the nature of DMC,
when we perform ground state calculations, the operators will typically be sandwiched
between the trial wave function ΨT and the ground state wave function Φ0. Therefore,
DMC based methods can accurately calculate the ground state expectation values of
the operators which commute with the Hamiltonian, e.g., the ground state energy E0
itself. However, if the operators do not commute with the Hamiltonian, the ground state
expectation values cannot be obtained without tradeoﬀ 8 . In fact, there are a lot of
operators which do not commute with the Hamiltonian, such as the root-mean-square
(rms) radius, the particle number density, response functions, etc. Therefore, if we
want to accurately calculate the ground state properties beyond the energy itself, we
8Diﬀusion based QMC methods typically use a technique called ‘future walking’ (Hammond et al.
(1994)) or ‘forward walking’ (Runge (1992); Casulleras and Boronat (1995); Samaras and Hamer
(1999)) to deal with operators which do not commute with H. This technique is sensitive to the
quality of the trial wave function ΨT .
10
may want to use methods other than DMC.
Path integral Monte Carlo (PIMC) method (Ceperley (1995)) can be a natural
choice for such calculations. Unlike DMC methods, in PIMC, the operator can indeed be
sandwiched easily between the ground states. So, whether the operator commutes with
the Hamiltonian or not, we can always naturally calculate its ground state expectation
value. This is the most attractive feature of PIMC.
There were important applications of PIMC in calculating the properties of con-
densed Helium atoms (Ceperley (1995)) before. There are also PIMC calculations
of nuclei on the lattice (Lee (2009); Epelbaum et al. (2012)). However, there are no
PIMC with the realistic NN potentials such as Argonne potential or ChEFT potentials
to calculate the properties of any nuclei in continuous space time before this work.
PIMC Total Imaginary time 
GFMC walker 
PIMC walker 
t=  t= 0
GFMC Total Imaginary time 
Figure 1.1: Illustration of a GFMC walker and a PIMC walker.
One of the main reasons is that continuous space PIMC calculations can be
computationally expensive (even more expensive than GFMC). As illustrated in Fig.
1.1, for a PIMC walker, just like in the path integral, we need to separate the total
imaginary time of the path into N slices, insert a complete basis at each slice, and
form a bead which contains the spatial conﬁguration of the nucleus. Computing the
beads one by one will be more and more time consuming as N increases, especially
considering that the realistic nuclear interactions contain spin and isospin structure.
As a rough estimation, the amount of work a PIMC walker does is about N times more
11
than a GFMC walker does. However, due to the nature of DMC, a GFMC walker needs
to evolveN/2 steps to reach τd which is half of the total imaginary time τ a PIMC
walk does, in order to project out the ground state. Besides, for a given amount of
computation time, the GFMC walkers can be more uncorrelated with each other than
PIMC walkers. That is to say, PIMC actually needs more than twice the computation
time to have equally uncorrelated walkers as GFMC walkers. So, overall the cost of a
PIMC walker can be more than twice the cost of a GFMC walker. Therefore PIMC
can be more expensive than GFMC. The storage space a PIMC walker requires is also
N times bigger than a GFMC walker, because the conﬁgurations of all the nucleons
in the nucleus at each of N beads need to be stored.
Nonetheless, ever since the early nuclear QMC simulation such as GFMC performed
in 1987 (Carlson (1987)), in the last more than three decades, human beings have
witnessed an impressive increase in supercomputers’ power. A typical CRAY system in
the 1980s could do about 109 ﬂoating point operations per second (FLOPS) (Chodosh
(2017)), and today’s most powerful supercomputer Fugaku 9 can do more than 10 17
FLOPS. With a magnitude of 10 8 increase in computing power as well as the better
understanding of NN interaction such as those from ChEFT, we have seen more and
more ChEFT based GFMC and AFDMC calculations (Lynnet al. (2014); Gezerlis et al.
(2014); Lynn et al. (2017); Lonardoni et al. (2018a,b)). Therefore, we will naturally
ask, what can PIMC do in nuclear physics?
The motivation of this work is to show that (as a benchmark test to begin with),
it is now possible to perform a reliable continuous space PIMC calculation of light
nuclei, by using modern realistic NN interactions (particularly the chiral interaction).
9As of June 2020 (Wikipedia contributors (2020b)), the most powerful supercomputer in the world
is Fugaku (peak performance is around 0.54 exaFLOPS) which is installed at RIKEN Center for
Computational Science in Kobe, Japan. It is preceded by the Summit (peak performance is around
0.2 exaFLOPS) which is located at the Oak Ridge National Laboratory in Tennessee, USA.
12
