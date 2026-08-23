---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-021-141-the-epidemic-model
section_title: "The Epidemic Model"
section_number: 14.1
pages: 45-49
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
The best source of conﬁrmation of theC =V hypothesis is to perturb the evolution of the
black hole, and see if the correspondence between GR and quantum circuits continues to
hold. For example we may allow some time-dependent perturbations to the CFT Hamilto-
nian and calculate the eﬀect on the black hole geometry. At the same time we may study
the eﬀects of time-dependent perturbations on the complexity of a quantum circuit. By
comparing the two we can conﬁrm the complexity-volume correspondence. In this context
so-called precursor operators are a useful tool.
Let us consider an operator of the form,
W (t) =eiHtWe−iHt =U†(t)WU (t) (14.45)
in the Schrodinger picture. HereH is some all-to-all k-local Hamiltonian acting on a system
of K qubits and W is some single qubit unitary operator. With no loss of generality we
can take W to act on the ﬁrst qubit. The complexity of W is 1. We write that in the
form,
C(0) = 1. (14.46)
44
The object of our investigation is C(t)—the complexity of W (t) as a function of time. By
deﬁnitionC(t) is the minimum number of gates that it takes to construct W (t).
Let us ﬁrst consider the analogous problem for a quantum circuit composed of gates.
To that end we replace the evolution operator e−iHt by a product of gates with the usual
parallel architecture illustrated in ﬁgure 21. I’ll write it in the form,
U(t) =gngn−1....g1. (14.47)
The precursor operator becomes
W (t) =g†....g†
n−1g†
n W gngn−1....g1. (14.48)
One might be tempted to ascribe a complexity of (2 n + 1) to W (t). This however is an
overestimate. While it is true that the circuit in 14.48 has 2 n + 1 gates the deﬁnition of
complexity requires us to ﬁnd the minimal circuit that prepares W (t).
By assumption W is a very small perturbation on the system of K qubits in that it
only aﬀects the ﬁrst qubit. For all other qubits W acts as the unit operator. Let’s ﬁrst
examine the case in which W is just the unit operator, W = 1. In that case all the gates
in 14.48 cancel and the complexity is exactly zero.
In the case where W⁄= 1 many gates still cancel. To illustrate the cancelation consider
the circuit in ﬁgure 22. The operator W acts between two sub-circuits which are mirror
images of each other as in 14.48.
Figure 22: Circuit for a precursor
Start at W and let us work our way toward the right. We will say that W infects the
qubit that it acts on (colors it blue). Each time an infected (blue) qubit interacts with an
uninfected (white) qubit it infects it. The result is a growing epidemic in which eventually
all qubits are infected. On the left side there is a mirror image epidemic. The growth of
45
the epidemic is shown in ﬁgure 23.
Figure 23: Each infected (blue) qubit infects each each qubit that it interacts with. The
epidemic grows until all qubits are infected.
Notice that any gate involving uninfected qubits can cancel a mirror image gate on the
other side. The result, after canceling all un-infected gates, is shown in ﬁgure 24.
Figure 24: Uninfected gates cancel with their mirror images.
Evidently the minimum number of gates needed to prepare the precursor is less then
the total number of gates in ﬁgure 22. Let us quantitatively estimate it.
Suppose the circuit has evolved to the right by n steps and at that stage the epidemic
has size s(n). Then the average number of new infections that result in the next step is
easy to compute. It is given by,
∆s = (K−s)s
K− 1
The shift by one unit in the denominator can be ignored,
∆s = (K−s)s
K . (14.49)
46
We can replace this by a diﬀerential equation
ds
dτ = (K−s)s
K (14.50)
which is easily integrated,
s = Keτ
K +eτ. (14.51)
This “epidemic function” 16 governs the size of the precursor operator.
Equation 14.51 can written,
s
K = eτ−τ∗
1 +eτ−τ∗
(14.52)
where τ∗ is the scrambling time expressed in circuit time units.
τ∗ = logK (14.53)
The size s(τ) has the following properties: For small τ 14.53 grows exponentially,
s(τ)≈eτ (small τ) (14.54)
For largeτ the size saturates when all qubits become infected,
s(τ)→K. (14.55)
and
s
K→ 1. (14.56)
At the scrambling time a rather sharp crossover takes place and the size jumps rapidly to
its saturation value K.
16Also known as the logistic function.
47
