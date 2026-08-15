---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-010-42-variable-reduction
section_title: "Variable reduction"
section_number: 4.2
pages: 17-20
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
doc_brief: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS — Motivated by the conjectured asymptotics of the Kashaev invariant, Dimofte and the first author introduced a power series associated to a suitable ideal"
---
by solving the gluing equations for the C and R-edges, and the completeness equation. The
following lemma will be used repeatedly.
Lemma 4.7. Let f1,...,f k be functions in variables x1,...,x k and fix a solution to
exp(f1) =··· = exp(fk) = 1.
Suppose that exp( fk) is of the form g(x1,...,x k−1)xk so that we can substitute xk with
1/g(x1,...,x k−1) by solving exp(fk) = 1. Then we have
det
∂(f1,...,f k)
∂(x1,...,x k)

= 1
xk
det
∂(f′
1,...,f ′
k−1)
∂(x1,...,x k−1)

(11)
where f′
i is obtained from fi by substituting xk with 1/g(x1,...,x k−1).
Proof. It follows from exp( fk) = g(x1,...,x k−1)xk that the ( k,j )-entry of the Jacobian
matrix ∂(f1,...,f k)/∂(x1,...,x k) is 1/xk for j =k, and g−1∂g/∂xj for 1≤j <k. Keeping
the last row, we make the i-row fori̸=k have the last entry 0 by employing elementary row
operations. Then the (i,j )-entry becomes
∂fi
∂xj
− xk
g
∂g
∂xj
∂fi
∂xk
= ∂fi
∂xj
− 1
g2
∂g
∂xj
∂fi
∂xk
= ∂fi
∂xj
+ ∂g−1
∂xj
∂fi
∂xk
= ∂fi
∂xj
+ ∂xk
∂xj
∂fi
∂xk
.
As the last term is equal to ∂f′
i/∂xj, we deduce Equation (11). □
18 STA VROS GAROUF ALIDIS AND SEOKBEOM YOON
Recall that the gluing equation of an edge ei ofT˚D is of the form
NX
j=1
Gij logzj +G′
ij logz′
j +G′′
ij logz′′
j = 2πi.
We denote by gi the left-hand side so that exp( gi) = 1. By rearranging the index of edges,
we may assume that the first n + 1 equations g1,...,g n+1 are for O and U-edges and the
rest, saygn+2,...,g N, are for C and R-edges. By replacing the ( n + 1)-st equationgn+1 with
gµ, the logarithm form of the completeness equation of a meridian, the 1-loop invariant is
given by (see Remark 2.2)
τ(T˚D) =± 1
2ζf+g det
∂(g1,...,g n,gµ,gn+2,...,g N)
∂(z1,...,z N)

(12)
wheref +g is the flattening ofT˚D chosen in Section 4.1.
In what follows, we solve all C and R-edge equations gn+2,...,g N as well as the complete-
ness equation gµ. This eliminates N−n shape parameters, and we may assume that those
are zn+1,...,z N by rearranging the index of shape parameters.
• Recall that a C-edge corresponds to a crossing of ˚D. Given that ˚D is given as in
Figure 11, one of E and W-corners at the crossing is non-essential, and thus the
gluing equation of the C-edge is either
zNzEzS = 1 or zNzWzS = 1.
where zX means the shape parameter at the X-corner. Employing Lemma 4.7, we
eliminate the shape parameter zS of the S-corner.
• Similarly, an R-edge corresponds to a region of ˚D, and its gluing equation is of the
form zi1··· zik = 1 where the S-corner of the topmost crossing and the N-corner
of the bottommost crossing contribute one shape parameter. Using Lemma 4.7, we
eliminate the shape parameter at the N-corner of the bottommost crossing.
• Lastly, the completeness equation for a meridian is given as z±1
i1 zi2 = 1 where zi1 and
zi2 are shape parameters placed at corners shown as in Figure 15. We eliminate the
shape parameter zi2 by employing Lemma 4.7.
...
zi1
zi2
Figure 15. A completeness equation for a meridian.
1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS 19
As mentioned earlier, the above variable reduction eliminates N−n shape parameters
zn+1,...,z N, and Lemma 4.7 implies that
det
∂(g1,...,g n,gµ,gn+2,...,g N)
∂(z1,...,z N)

= 1
zn+1··· zN
det
∂(g′
1,...,g ′
n)
∂(z1,...,z n)

(13)
where g′
i is obtained from gi by eliminating the N−n shape parameters zn+1,...,z N. A
simple calculation shows that the numbern of the remaining variables is equal to the number
of variables that are assigned to the open diagram ˚D. Namely, the matrix in the right-hand
side of Equation (13) has the same size as the matrix in (7).
Lemma 4.8. We have
det

xi
∂
∂xi

xj
∂V
∂xj

1≤i,j≤n
=±z1...z n det
∂(g′
1,...,g ′
n)
∂(z1,...,z n)

where V is the potential function of ˚D.
Proof. It is proved in [MY18, Theorem 4.1] that the system of equations xi∂V/∂xi is equiv-
alent to the system of equations g′
i. Hence we have
det
 ∂
∂xi

xj
∂V
∂xj

=± det
∂(g′
1,...,g ′
n)
∂(z1,...,z n)

det
∂(z1,...,z n)
∂(x1,...,x n)

.
If we label the indices of zi and xi from the top of the diagram ˚D to the bottom, we have
z1 =x1 and zi =xi/xi−1 or xi−1/xi for i≥ 2. A simple induction argument shows that
det
∂(z1,...,z n)
∂(x1,...,x n)

=±z1··· zn
x1··· xn
.
Combining the above two equations, we conclude the lemma. □
Lemma 4.9. We have
Ω1Ω2 =±ζ1··· ζN
ζf+g
where Ω1 and Ω2 are the normalizing functions of ˚D.
Proof. Recall that the second normalizing function Ω2 depends on a choice of the orientation
of ˚D. If we reverse the orientation of ˚D, the contribution of the left (resp., right) crossing
in Figure 6 to Ω 2 becomes (y/y′)2 (resp., (x/x′)2). Considering both orientations of ˚D, one
can define Ω 2 without an orientation choice: Ω 2 is defined as the product of x′y/xy′ for the
first crossing in Figure 5 and xy′/x′y for the second crossing. It follows that Ω 1Ω2 is given
by the product of ( x′
x− 1) and ( y
y′− 1) for the first crossing, and ( x
x′− 1) and ( y′
y− 1) for
the second crossing. From Figure 12 we easily computes that this product is equal to 1 /ζf.
This proves that Ω 1Ω2 = 1/ζf.
On the other hand, a product of any three zetas around one crossing is 1. Given that ˚D
is given as in Figure 11, we have
ζ1··· ζN =ζ1ζN = 1
z1zN
20 STA VROS GAROUF ALIDIS AND SEOKBEOM YOON
where z1 and zN are the shape parameters that appear first from the top and bottom,
respectively, of the diagram. From Remark 4.6, we deduce that z1zN is equal ζg. This
completes the proof. □
Remark 4.10. We expect that a similar lemma to the one above holds for all essential
diagrams obtained from braid closures of knots; see Appendix B.
Proof of Theorem 4.1. Combining Equations (12) and (13) together with Lemmas 4.8 and 4.9,
we obtain
τ(T˚D) =± 1
2ζf+g det
∂(g1,...,g n,gµ,gn+2,...,g N)
∂(z1,...,z N)

=±ζn+1··· ζN
2ζf+g det
∂(g′
1,...,g ′
n)
∂(z1,...,z n)

=±ζ1··· ζN
2ζf+g det

xi
∂
∂xi

xj
∂V
∂xj

=±Ω1Ω2
2 det

xi
∂
∂xi

xj
∂V
∂xj

=ω(˚D),
which concludes the proof of Theorem 4.1. □
