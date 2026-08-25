---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-008-solving-a-second-order-q-difference-equation
section_title: "Solving a second-order q-difference equation"
section_number: null
pages: 17-20
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
Recall that, for each choice of α, the resummed perturbative wave function χ(α),WKB(u; ℏ) is given
in Eq. (3.1). Equivalently, we write
χ(α),WKB(u; ℏ) = e
i
ℏs(α)
0 (x)+s(α)
1 (x)Ψ(α),WKB(X;q), (3.49)
where we have introduced the notation
Ψ(α),WKB(X;q) = exp

ϕ(α),WKB(X;q)

, (3.50)
which will be useful in the following discussion. Let us assume that the corresponding quantum
A-polynomial equation, that is,
ˆA( ˆP, ˆX,q )χ(α),WKB(u; ℏ) = 0, (3.51)
is of second order. After appropriately accounting for the correction due to the exponential prefactor
containing the functions s(α)
0,1 (x) in Eq. (3.49), the q-difference equation above becomes
Ψ(α),WKB(qX;q) +A(X)Ψ(α),WKB(X;q) +B(X)Ψ(α),WKB(q−1X;q) = 0, (3.52)
– 16 –
where A(X),B (X) are functions of X and q. Let us observe that, due to the conjectural structure
in Eqs. (3.2), (3.3), we have
υ(α)(X) = Ψ(α),WKB(qX;q)
Ψ(α),WKB(X;q) = exp

Υ(α)(X)

, (3.53)
and we can now write Eq. (3.52) in terms of the above function υ(α)(X) as
υ(X)υ(q−1X) +A(X)υ(q−1X) +B(X) = 0, (3.54)
where we have dropped the label α from the notation for simplicity. Let us further assume that ℏ is
fixed as in Eq. (3.15), that is,
q = eiℏ = e2πiP
Q, P,Q ∈ Z>0 coprime, (3.55)
and introduce the sequence of functions {υk}, k∈ Z≥0, of X and q defined by
υk =υ(q−kX). (3.56)
They satisfy the system of equations
υkυk+1 +A(q−kX)υk+1 +B(q−kX) = 0, 0≤k≤Q− 1, (3.57)
as a consequence of Eq. (3.54). We solve this system recursively, as follows. We define the sequences
{a(k)(X)} and{b(k)(X)}, k∈ Z≥0, via the relations
a(1)(X) =A(X), (3.58a)
b(1)(X) =B(X), (3.58b)
υ0υ1··· υk +a(k)(X)υk +b(k)(X) = 0, k> 1. (3.58c)
If we multiply Eq. (3.58c) by υk+1 and apply Eq. (3.57), we obtain a recursion relation which can
be written in matrix form as
a(k+1)(X)
b(k+1)(X)

=
−A(q−kX) 1
−B(q−kX) 0
a(k)(X)
b(k)(X)

, (3.59)
and it can be solved as a(Q)(X)
b(Q)(X)

=MQ(X)
−1
0

. (3.60)
Here,MQ(X) is the matrix
MQ(X) =
QY
k=1
−A(qkX) 1
−B(qkX) 0

=
M11(X)M12(X)
M21(X)M22(X)

, (3.61)
where the product is ordered from left to right as k increases. Recalling that qQ = 1, we obtain
MQ(q−1X) =
−A(X) 1
−B(X) 0

MQ(X)
−A(X) 1
−B(X) 0
−1
=
M22−AM12 A
B (M11 +AM12)− 1
B (M21 +AM22)
−BM12 M11 +AM12

,
(3.62)
– 17 –
where we have removed the explicit dependence onX for compactness. Following Eqs. (3.60), (3.62),
we find that9 a(Q)(q−1X)
b(Q)(q−1X)

=
−M22(X) +A(X)M12(X)
B(X)M12(X)

. (3.63)
Let us now define the function
Πυ =υ0υ1··· υQ−1, (3.64)
which is invariant under q-shifts. We consider Eq. (3.58c) for k =Q and, shifting X intoq−1X, we
produce the system (
υ0(Πυ +a(Q)(X)) +b(Q)(X) = 0,
υ1(Πυ +a(Q)(q−1X)) +b(Q)(q−1X) = 0. (3.65)
By substituting the expressions for a(Q)(X),a (Q)(q−1X) and b(Q)(X),b (Q)(q−1X) in terms of the
entries of the original matrix MQ(X) in Eqs. (3.60), (3.63) and then using Eq. (3.57) with k = 0,
we can rewrite the system above as
(
υ0(Πυ−M 11(X))−M 21(X) = 0,
Πυ−M 22(X)−υ0M12(X) = 0, (3.66)
or, equivalently, in the matrix form
M11(X)− Πυ M21(X)
M12(X) M22(X)− Πυ
υ0
1

=
0
0

. (3.67)
It follows straightforwardly that Πυ is an eigenvalue of the transpose matrix MQ(X)T with eigen-
vector (υ0, 1)T. Specifically, we have that
Πυ = trMQ(X)±
p
∆Q(X)
2 , (3.68)
where we have introduced
∆Q(X) = (trMQ(X))2− 4 detMQ(X), (3.69)
while detMQ(X) and trMQ(X) denote the trace and determinant of the matrix, respectively. Note
that, following Eq. (3.61), both detMQ(X) and trMQ(X) are invariant underq-shifts and so depend
on X through XQ. The function υ0 can be found, for example, using the second line of Eq. (3.66),
yielding
υ0 = Πv−M 22(X)
M12(X) =M11(X)−M 22(X)±
p
∆Q(X)
2M12(X) , (3.70)
while the functions υk, k∈ Z>0, are obtained by successively q-shifting υ0. This gives the solution
to Eq. (3.54) for all rational values of ℏ. However, we stress that, for such a solution to be consistent
with the original choice of a classical branch labeled by α, we must impose that, taking P =Q = 1,
we find
υ0 = Πυ =P (α), (3.71)
whereP (α) is the selected non-abelian solution of the classical A-polynomial at fixed X after taking
into account the corrections due to the exponential prefactor in Eq. (3.49). In this way, we remove
9There is a sign misprint in the corresponding equation in [12].
– 18 –
the sign ambiguity in Eq. (3.68) and correspondingly in Eq. (3.70). We conclude by observing that
Eq. (3.53) implies
Υ(X) = logυ0 = log
 
M11(X)−M 22(X)±
p
∆Q(X)
2M12(X)
!
, (3.72a)
φQ(X) = 1
Q log Πυ = 1
Q log
 
trMQ(X)±
p
∆Q(X)
2
!
, (3.72b)
where we have applied the relation
Πυ = exp
 Q−1X
m=0
Υ(qmX)
!
= exp (QφQ(X)) , (3.73)
which is a direct consequence of Eq. (3.46a). Again, the sign ambiguity in Eq. (3.72) is resolved by
the requirement in Eq. (3.71).
