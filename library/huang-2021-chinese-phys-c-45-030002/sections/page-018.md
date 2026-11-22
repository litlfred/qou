---
doc_id: huang-2021-chinese-phys-c-45-030002
doc_title: "The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures"
section_id: page-018
section_title: "Page 18"
section_number: null
pages: 18-18
source_pdf: Huang_2021_Chinese_Phys._C_45_030002.pdf
source_sha256: 1dd3329ed87476c8
toc_source: undetermined
doc_brief: "The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures — 343 sections: Page 1; Page 2; Page 3"
---
Chinese Physics C
Vol. 45, No. 3 (2021) 030002
We deﬁne the diagonal weight matrix W by its ele-
ments wi
i = 1/(dqidqi). The solution of the least-squares
method leads to a very simple construction:
tKWK|m⟩= tKW|q⟩.
(4)
The normal matrix A = tKWK is a square matrix of
order M, positive-deﬁnite, symmetric and regular and
hence invertible [26]. Thus the vector |m⟩for the ad-
justed masses is:
|m⟩= A−1 tKW|q⟩
or
|m⟩= R|q⟩.
(5)
The rectangular (M,Q) matrix R is called the response
matrix.
The diagonal elements of A−1 are the squared er-
rors on the adjusted masses, and the non-diagonal ones
(a−1)ν
µ are the coeﬃcients for the correlations between
masses mµ and mν. Values for correlation coeﬃcients
for the most precise nuclides are given in Table B of
Part II. Starting from Ame2012 [24, 25], we now give on
the website of the Amdc [27] the full list of correlation
coeﬃcients, allowing any user to perform exact calcula-
tion of any combination of masses.
One of the most powerful tools in the least-squares
calculation described above is the ﬂow-of-information
matrix, discovered in 1984 [28].
This matrix allows to
trace back the contribution of each individual piece of da-
tum to each of the parameters (here the atomic masses).
The Ame uses this method since 1993.
The ﬂow-of-information matrix F is deﬁned as fol-
lows:
K, the matrix of coeﬃcients, is a rectangular
(Q,M) matrix. The transpose of the response matrix tR
is also a (Q,M) rectangular one. The (i,µ) element of F
is deﬁned as the product of the corresponding elements
of tR and of K.
In Ref. [28], it is demonstrated that
such an element represents the “inﬂuence” of datum i
on parameter (mass) mµ. A column of F thus represents
all the contributions brought by all data to a given mass
mµ, and a line of F represents all the inﬂuences given
by a single piece of data. The sum of inﬂuences along a
line is the “signiﬁcance” of that datum. It has also been
proven [28] that the inﬂuences and signiﬁcances have all
the expected properties, namely that the sum of all the
inﬂuences on a given mass (along a column) is unity,
that the signiﬁcance of a datum is always less than unity
and that it always decreases when new data are added.
The signiﬁcance deﬁned in this way is exactly the quan-
tity obtained by squaring the ratio of the uncertainty on
the adjusted value over that of the input one, which was
the recipe used before the discovery of the F matrix to
calculate the relative importance of data.
A simple interpretation of inﬂuences and signiﬁcances
can be obtained in calculating, from the adjusted masses
and Eq. 2, the adjusted data:
|q⟩= KR|q⟩.
(6)
The ith diagonal element of KR represents then the con-
tribution of datum i to the determination of qi (same
datum): this quantity is exactly what is called above the
signiﬁcance of datum i. This ith diagonal element of KR
is the sum of the products of line i of K and column i
of R. The individual terms in this sum are precisely the
inﬂuences deﬁned above.
The ﬂow-of-information matrix F, provides thus in-
sight on how the information from datum i ﬂows into
each of the masses mµ.
The ﬂow-of-information matrix cannot be given in
full in a printed table. It can be observed along lines,
displaying for each datum, the nuclides inﬂuenced by
this datum and the values of these inﬂuences. It can be
observed also along columns to display for each primary
mass all contributing data with their inﬂuence on that
mass.
The ﬁrst display is partly given in the table of input
data (Table I) in column ‘Signf.’ for the signiﬁcance of
primary data and ‘Main inﬂ.’ for the largest inﬂuence.
Since in the large majority of cases only two nuclides are
concerned in each piece of data, the second largest in-
ﬂuence could easily be deduced. It is therefore not felt
necessary to give a table of all inﬂuences for each primary
datum.
The second display is given in Part II, Table II for
the up to three most important data with their inﬂuence
in the determination of each primary mass.
4.4
Consistency of data
The
system
of
equations
being
largely
over-
determined (Q >> M) oﬀers the evaluator several inter-
esting possibilities to examine and judge the data. One
might for example examine all data for which the ad-
justed values deviate signiﬁcantly from the input ones.
This helps to locate erroneous pieces of information. One
could also examine a group of data in one experiment
and check if the uncertainties assigned to them in the
experimental paper were not underestimated.
If the precisions dqi assigned to the data qi were in-
deed all accurate, the normalized deviations vi between
adjusted qi (Eq. 6) and input qi data, vi = (qi −qi)/dqi,
would be distributed as a Gaussian function of standard
deviation σ = 1, and would make χ2:
χ2 =
Q
∑
i=1
(qi −qi
dqi
)2
or
χ2 =
Q
∑
i=1
v2
i
(7)
equal to Q−M, the number of degrees of freedom, with
a standard deviation of
√
2(Q−M).
One can deﬁne as above the normalized chi, χn (or
‘consistency factor’ or ‘Birge ratio’): χn =
√
χ2/(Q−M)
for which the expected value is 1±1/
√
2(Q−M).
030002-17
