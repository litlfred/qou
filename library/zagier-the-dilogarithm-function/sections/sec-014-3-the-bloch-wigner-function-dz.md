---
doc_id: zagier-the-dilogarithm-function
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-014-3-the-bloch-wigner-function-dz
section_title: "The Bloch-Wigner function D(z)"
section_number: 3
pages: 8-10
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
doc_brief: "The Dilogarithm Function Don Zagier — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
---
and its generalizations
D
The function Li2(z), extended as above to C/integerdivide[1,∞), jumps by 2πi log|z| as
z crosses the cut. Thus the function Li 2(z)+i arg(1−z) log|z|, where arg
denotes the branch of the argument lying between −π and π, is continuous.
Surprisingly, its imaginary part
D(z)= ℑ(Li2(z)) + arg(1−z) log|z|
is not only continuous, but satisﬁes
(I) D(z) is real analytic on C except at the two points 0 and 1, where it is
continuous but not diﬀerentiable (it has singularities of typer logr there).
The above graph shows the behaviour of D(z). We have plotted the level
curves D(z)=0 , 0.2, 0.4, 0.6, 0.8, 0.9, 1.0 in the upper half-plane. The val-
ues in the lower half-plane are obtained from D(¯z)=−D (z). The maximum
of D is 1.0149 ... , attained at the point (1 +i
√
3)/2.
The function D(z), which was discovered by D. Wigner and S. Bloch
(cf. [1]), has many other beautiful properties. In particular:
(II) D(z), which is a real-valued function onC, can be expressed in terms of
a function of a single real variable, namely
D(z)= 1
2
[
D
(z
¯z
)
+D
( 1− 1/z
1− 1/¯z
)
+D
( 1/(1−z)
1/(1− ¯z)
)]
(2)
The Dilogarithm Function 11
which expressesD(z) for arbitrary complex z in terms of the function
D(eiθ)=ℑ[Li2(eiθ)] =
∞∑
n=1
sinnθ
n2 .
(Note that the real part of Li2 on the unit circle is elementary:
∞∑
n=1
cosnθ
n2 =
π2
6 − θ(2π−θ)
4 for 0≤θ≤ 2π.) Formula (2) is due to Kummer.
(III) All of the functional equations satisﬁed by Li 2(z) lose the elementary
correction terms (constants and products of logarithms) when expressed
in terms of D(z). In particular, one has the 6-fold symmetry
D(z)=D
(
1− 1
z
)
=D
( 1
1−z
)
=−D
( 1
z
)
=−D(1−z)= −D
( −z
1−z
) (3)
and the ﬁve-term relation
D(x)+ D(y)+ D
( 1−x
1−xy
)
+D(1−xy)+D
( 1−y
1−xy
)
=0, (4)
while replacing Li2 by D in the many-term relation (1) makes the con-
stantC(f) disappear.
The functional equations become even cleaner if we think of D as being
a function not of a single complex number but of the cross-ratio of four such
numbers, i.e., if we deﬁne
~D(z0,z1,z2,z3)= D
( z0−z2
z0−z3
z1−z3
z1−z2
)
(z0,z1,z2,z3 ∈ C). (5)
Then the symmetry properties (3) say that~D is invariant under even and anti-
invariant under odd permutations of its four variables, the ﬁve-term relation
(4) takes on the attractive form
4∑
i=0
(−1)i ~D(z0,..., ˆzi,...,z 4)=0 ( z0,...,z 4 ∈ P1(C)) (6)
(we will see the geometric interpretation of this later), and the multi-variable
formula (1) generalizes to the following beautiful formula:
∑
z1 ∈ f −1(a1)
z2 ∈ f −1(a2)
z3 ∈ f −1(a3)
~D(z0,z1,z2,z3)=n ~D(a0,a1,a2,a3)( z0,a1,a2,a3 ∈ P1(C)),
