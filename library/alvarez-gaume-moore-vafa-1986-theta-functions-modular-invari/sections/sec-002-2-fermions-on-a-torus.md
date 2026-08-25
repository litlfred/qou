---
doc_id: alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari
doc_title: "Theta Functions, Modular Invariance, and Strings"
section_id: sec-002-2-fermions-on-a-torus
section_title: "Fermions on a Torus"
section_number: 2
pages: 2-4
source_pdf: alvarez-gaume-moore-vafa-1986-theta-functions-modular-invariance-and-strings.pdf
source_sha256: c99ca1cd756f7aa6
doc_brief: "Theta Functions, Modular Invariance, and Strings — We use Quillen's theorem and algebraic geometry to investigate the modular transformation properties of some quantities of interest in string"
---
In this section we will consider fermions on a torus. We label the points of the torus
by the complex quantity σ1 + τσ2, where σx and σ2 are periodic variables with
period 2π. This means that
x ~ x + 2π ~ x 4- 2πτ.
For bosonic fields defined on the torus one requires the periodic boundary
conditions:
X(σ1 + 2π, σ2) = X(σu σ2 + 2π) = X(σl9 σ2)
For fermions, we have the option of choosing periodic or antiperiodic boundary
conditions in each direction. Therefore we have four different possible boundary
conditions: (A, A), (P,A), (A,P), and (P,P)9 where P(A) stands for periodic
(antiperiodic). These are called the spin structures. So for genus 1 we have four
different spin structures.
For the torus we have chosen 2π and 2πτ to generate the lattice defining it. We
could have chosen a different basis for the same lattice, thereby obtaining the same
torus. For example the tori defined by 2π(l,τ) and 2π(l,τ + l) differ from one
another by a global diffeomorphism. To see this we simply cut the torus along the
Theta Functions, Modular Invariance, and Strings 3
σx cycle and rotate the two boundary circles relative to one another by 2π and glue
them back together. (This is called a Dehn twist, and its general form will be
discussed in Sect. 3.)
Different choices of the lattice defining the torus could be obtained by means of
2x2, invertible (unit determinant) and integral matrices acting on a basis. This is
the group SL(2, Z) which is referred to as the modular group. Under an element of
SL(2, Z), with entries α, b, c, d,
aτ + b
T~* cτ + d'
The Dehn twists about the σx and σ2 cycles correspond respectively to
Ί l\ (\
)17 Vi
and they generate SL(25Z).
Under SL(2, Z) it is easy to see that three spin structures mix, in the sense that
The (P, P) spin structure is invariant under the action of SL(2, Z). So in a sense we
have only two inequivalent spin structures. There is a simple way to characterize
each class. We consider the Dirac operator for each of the spin structures which we
label by α. Let n(ct) denote the number of zero modes of the Dirac operator for spin
structure α. Since the Dirac operator is real, there is no chiral index in two
dimensions and therefore π(α) is even. We call a spin structure even (odd) if jn(μ) is
even (odd). It is easy to see in our example of the torus that there are three even spin
structures [with n(α) = 0] (A, P), (P, A), (A, A) and one odd spin structure [with
w(α) = 2] (P,P). Under the action of global diffeomorphisms the two different
classes of spin structures cannot mix because they have different number of zero
modes for the Dirac operator. In fact more is true: All the spin structures in each
class mix under the action of global diffeomorphisms. This is true in the above
example and, as we will discuss, it continues to be true for higher genus Riemann
surfaces.
Modular transformations are important for string theories. In a string theory
we have to divide the path integral measure by the action of diffeomorphisms, and
this includes global diffeomorphisms which cannot be reached from identity.
Therefore it is necessary for the path integral measure to be invariant under global
diffeomorphisms, i.e., modular transformations (For each spin structure it should
be invariant under diffeomorphisms preserving that spin structure.)
Note that each spin structure is simply related to a particular one by changing
boundary conditions by ±1. We can in fact continuously interpolate between
various spin structures if we consider arbitrary twistings of the boundary
conditions by a phase. (For this we should allow the spinor to be complex.) So we
get a two parameter family of complex spinors on the torus defined by θ, φ:
ψ(σ1 +2π, σ2)= -e2πίθψ(σu σ2),
