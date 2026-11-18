---
doc_id: arxiv-math-0408078v2
doc_title: "A basis for the full Homfly skein of the annulus"
section_id: sec-010-notation
section_title: "Notation"
section_number: null
pages: 12-13
source_pdf: 0408078v2.pdf
source_sha256: b632eb5e9b7a1753
toc_source: outline
doc_brief: "A basis for the full Homfly skein of the annulus — A basis, denoted {Qλ,µ}, for the full Homﬂy skein of the annulus C was introduced in [18], where λ and µ are partitions of integers n and p into k"
---
Notation
The entries in each matrix are drawn from sequences such as h = {hn}, y∗=
{y∗
n}, R = {Rn} with integer subscripts. On any given row the subscripts
either increase in steps of 1 along the row, (a standard row), or decrease in
steps of 1, (a starred row). The subscript for every entry of the matrix is
then determined by knowing which rows are starred, and the subscripts to
be used in the ﬁrst column.
We shall always use matrices in which the starred rows are the ﬁrst k∗
rows, followed by k standard rows. The column vector v of subscripts to be
used for the ﬁrst column will be called the index vector for the matrix.
The matrices used have the further restriction that in any given column
the entries in the starred rows are drawn from some ﬁxed sequence, h, R, for
example, while all entries in the standard rows of a given column again come
from some ﬁxed sequence.
By way of example the 8×8 matrix M below has entries in such a format.
M =












a∗
3
a∗
2
a∗
1
b0
b−1
c∗
−2
c∗
−3
c∗
−4
a∗
5
a∗
4
a∗
3
b2
b1
c∗
0
c∗
−1
c∗
−2
a∗
4
a∗
3
a∗
2
b1
b0
c∗
−1
c∗
−2
c∗
−3
a−1
a0
a1
d2
c3
c4
c5
c6
a1
a2
a3
d4
c5
c6
c7
c8
a2
a3
a4
d5
c6
c7
c8
c9
a1
a2
a3
d4
c5
c6
c7
c8
a0
a1
a2
d3
c4
c5
c6
c7












.
In M the ﬁrst 3 rows are starred and the index vector is
v =












3
5
4
−1
1
2
1
0












The complete matrix M can be recovered, given v, once the sequences to
be used in the starred and standard rows are known.
This information is given by the template matrix, in this case
a∗
a∗
a∗
b
b
c∗
c∗
c∗
a
a
a
d
c
c
c
c

.
12
In general the template matrix is the 2×(k∗+k) matrix giving the sequences
from which the starred and standard entries in each column are drawn.
As a further notational simpliﬁcation we use the symbol ⊣in the template
matrix to indicate that the same sequence is repeated, and the symbol · · ·
where the choice of sequence is unimportant. We label a column or columns
in the template as necessary to show where a repetition ends.
With this notation the template matrix for M can be written
 
4
↓
a∗
⊣
b
b
c∗
⊣
a
⊣
d
c
⊣
!
and the complete matrix M with index vector v can then denoted simply by
M =
 
4
↓
a∗
⊣
b
b
c∗
⊣
a
⊣
d
c
⊣
!
v
.
