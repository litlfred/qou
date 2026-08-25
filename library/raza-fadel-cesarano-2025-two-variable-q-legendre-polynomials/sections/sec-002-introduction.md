---
doc_id: raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials
doc_title: "Two-variable q-Legendre polynomials"
section_id: sec-002-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf
source_sha256: da8c1204e84d019c
doc_brief: "Two-variable q-Legendre polynomials — 12 sections: Aligarh Muslim University , Aligar; University of Lahej, 73560 Lahej, ; Introduction"
---
The operational techniques were utilized to create some spe cial polynomials and new
families of special polynomials with several applications in applied sciences, providing versa-
tile and easy-to-understand solutions to boundary value pr oblems. It has also resulted in the
establishment of new computer languages, such as umbral cal culus and symbolic interpreta-
tion. G. Dattoli et. al. [4] used operational formalism to de ﬁne 2-variable Legendre polynomi-
als, which have drawn the attention of several mathematicia ns due to their wide applications
in various ﬁelds of mathematics and physics (see, for exampl e, [5, 18, 28, 32]).
The Legendre polynomials Sn(x, y) and Rn(x, y)/n! are deﬁned [4] by means of the follow-
ing generating functions:
eytC0(− xt2) =
∞
∑
n=0
Sn(x, y) tn
n! (1)
and
C0(xt) C0(− yt) =
∞
∑
n=0
Rn(x, y)
n!
tn
n! . (2)
Quantum calculus is a relatively subﬁeld in the realm of scie ntiﬁc study. This area is a
generalization of ordinary calculus for the case where q → 1− exists. It has been demonstrated
that it is helpful in the investigation of various problems, which arise in various branches
УДК 517 .589
2020 Mathematics Subject Classiﬁcation: 33C45, 05A30, 11B83.
© Raza N., Fadel M., C. Cesarano, 2025
On 2-variable q-Legendre polynomials: the view point of the q-operational technique 15
of the sciences, mathematics, statistics, quantum mechani cs and quantum physics. Recently ,
several researchers, working in the ﬁeld of q-special functions, introduced and studied several
q-special functions and their characteristics (see, for exa mple, [2, 12, 19, 25, 29, 30]).
In this quick recap, we take a look at a few deﬁnitions and nota tions associated with the
quantum calculus [7].
The q-factorial is deﬁned as
[n]q! =





n
∏
k=1
[k]q, 0 < q < 1, n ≥ 1,
1, n = 0.
The two q-exponential functions are deﬁned as:
eq(x) =
∞
∑
n=0
xn
[n]q! , 0 < q < 1, (3)
and
Eq(x) =
∞
∑
n=0
q(2
n) xn
[n]q! , 0 < q < 1,
which satisfy the following rule
eq(x)Eq(− x) = 1. (4)
We recall some identities of q-derivatives:
ˆDq,x xn = [ n]qxn− 1, (5)
ˆDq,xeq(α x) = α eq(α x), (6)
ˆDq,x( f (x)g(x)) = f (x) ˆDq,x g(x) + g(qx) ˆDq,x f (x). (7)
The theory of q-Bessel function was studied by many mathematicians and phy sicists. This
theory grew to include two variables and generalized q-Bessel functions. The most well-
known forms are two related q-Bessel functions J1
n(x; q) and J2
n(x; q) [15]. The q-Bessel function
J1
n(x; q) is introduced and studied by F.H. Jackson [17]. Later, W. Hah n and H. Exton cre-
ated a third form of q-Bessel function [8, 9, 14], which is studied by T .H. Koornwi nder and
R. Swarttouw [22]. Recently , M. Fadel et. al. [10] presented new properties and characterize
q-Bessel functions of the ﬁrst kind.
The series deﬁnition of q-Bessel functions of the ﬁrst kind qBF Jn(x; q) is given [27] by
Jn(x; q) = 1
(q; q)n
∞
∑
k=0
(− 1)k(
x/2
) n+2k
(q; q)k(qn+1; q)k
=
∞
∑
k=0
(− 1)k(
x/2
) n+2k
[n + k]q![k]q! , (8)
which converges absolutely for |x|< 2.
The series deﬁnition of nth order q-Tricomi Bessel functions is deﬁned [27] by
Cn,q(x) = 1
(q; q)n
∞
∑
k=0
(− 1)k xk
(q; q)k(qn+1; q)k
=
∞
∑
k=0
(− 1)k xk
[k]q![n + k]q! , (9)
which converges absolutely for all values of x.
