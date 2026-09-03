---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-017-53-fisher-yates-algorithm
section_title: "Fisher-Yates Algorithm"
section_number: 5.3
pages: 105-110
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
doc_brief: "Concentration of Measure Techniques and Applications — 23 sections: Biographical Sketch; Acknowledgments; Abstract"
---
The Fisher-Yates algorithm is a method of obtaining a uniform random permutation
from a ﬁnite set. The algorithm was ﬁrst introduced by Fisher and Yates in [Fisher
et al., 1949]. Their original introduction of the algorithm was as a ”paper and pencil”
type algorithm for generating a random permutation of n numbers by hand. The
algorithm was ﬁrst presented as a computer algorithm by Durstenfeld [Durstenfeld,
1964] and became more widely known in a work by Knuth [Knuth, 2014].
The algorithm consists of the following four steps:
Fisher Yates Algorithm.
1) Set a counting variable j to be equal to 1. Let n denote the length of the desired
sequence. We will let L be a sequence which holds our permutation. We will begin by
letting L = (1).
2) Let m = i + 1. Pick an integer uniformly at random between 1 and m. Call this
integerk.
97
3) If k = m, then append k to the end of the list L. Otherwise, insert m into L at
positionk.
4) Increase i by 1. If i < n, then return to step 2. Otherwise, the algorithm is
complete.
To see this algorithm in action, we will do an example for n = 4. To begin with,
i = 1 and L = (1). To generate our random integers for this example, we used the
Python generator random.randint().
Iteration 1
1) i = 1 and L = 1.
2) Since m = i + 1, m = 2. Generating a random integer between 1 and 2, we get
k = 2.
3) Since k =m, we append k to the end of L, giving L = (1, 2).
4) We increase i to 2, and since i<n , we go back to step 2 for another iteration.
Iteration 2
2) i = 2, so m = 3. Generating a random number between 1 and 3, we get k = 2.
3) Since k <m, we insert m into position k in the list. This gives L = (1, 3, 2).
4) Increasing i by 1, we have i = 3, which is still less than n, so we go on for another
iteration.
Iteration 3
2) i = 3, m = 4.
3) We generate a random number between 1 and 4 and get k = 3. Since k < m, we
insert 4 into position 3, which gives L = (1, 3, 4, 2).
4) Once we increase i by 1, we notice that i = 4, and so the algorithm terminates.
We end up with L = (1, 3, 4, 2) as our random permutation. A Python code for
98
performing this algorithm on a computer is given in the appendix.
As mentioned, this algorithm shuﬄes the numbers (1 ,...,n ) uniformly, so that each
permutation is equally likely. Since we are trying to simulate a Mallows random
permutation, we have adapted this algorithm to return a permutation distributed
according to the Mallows measure.
Fisher Yates Algorithm for a Mallows Permutation.
For a permutation of length n, with Mallows parameter q, we have the following al-
gorithm to generate a Mallows distributed random permutation.
1) Begin with i = 1 and L = (1).
2) Let m = i + 1 and let k be a random integer distributed according to a geometric
distribution with probability p = 1−q.
3) Let j = 1 + ((k− 1)%m), where by %m, we mean modulo m.
4) If j = 1, append m to the end of the list L. Otherwise, insert m into L at position
m + 1−j.
5) Increment i by 1. If i<n , go back to step 2. Otherwise, the algorithm terminates.
We will not go through an example here, as this algorithm runs very similarly to
the uniform Fisher Yates algorithm. Since it may not be obvious, we will prove why
this modiﬁed algorithm generates a random permutation distributed according to the
Mallows measure.
Theorem 5.3.1. The modiﬁed Fisher Yates algorithm stated above does give a per-
mutation distributed according to the Mallows measure.
Proof. Recall that the Mallows measure is given by
Pn,q(π) = qInv(π)
Zn,q
99
where
Zn,q =
n∏
k=1
1−qk
1−q
We will prove the theorem by induction. We will start with the case n = 2. In
this case, the only possible permutations are (1 , 2) and (2, 1). Based on the Mallows
measure,
P{(1, 2)} = 1−q
1−q2
and
P{(2, 1)} = q(1−q)
1−q2
Consider our algorithm. We always start with (1). In this case, we will either be
adding 2 at the end of the permutation, or we will be inserting 2 into slot 1, giving
us (2, 1). Given the algorithm above, if j = 1, then we will get (1, 2) and if j = 2 we
have (2, 1). j = 1 only if k = 1, 3, 5,... . Using the fact that k is a geometric random
variable, we have
P{(1, 2)} = P{j = 1} = P{k is odd}
=
∞∑
i=0
(1−q)q2i
= 1−q
1−q2
as desired. On the other hand
P{(2, 1)} = P{j = 2} = P{k is even}
=
∞∑
i=0
(1−q)q2k+1
= q(1−q)
1−q2
This completes the proof of the base case.
For the inductive step, suppose that for a permutation of length n, the algorithm
100
does in fact give a permutation distributed according to the Mallows measure. In
other words, letting π be a permutation of length n, we know that
Pn,q(π) = qInv(π)
∏n
k=1
1−qk
1−q
Suppose now that π′ is the same permutation as π, except with the element n + 1
added in via the algorithm given. We need to prove that
Pn+1(π) = qInv(π)qInvn+1(π′)
∏n+1
k=1
1−qk
1−q
where Invn+1(π′) denotes the number of inversions caused by the element n + 1. We
can assume that we have run our algorithm successfully up until n and just need
to perform the last step of the algorithm to add in n + 1. In this case, i = n and
m =n + 1. Ifj = 1, we know that adding inn + 1 will cause no additional inversions,
soqInvn+1(π′) = 1. j = 1 only if k− 1 is a multiple of n + 1. Using the fact that k is a
geometric variable, we have
P{j = 1} = P{(k− 1)%(n + 1) = 0}
=
∞∑
i=0
qi(n+1)(1−q) = 1−q
1−qn+1
This implies that
Pn+1(π′) = qInv(π)
∏n+1
k=1
1−qk
1−q
as desired (since adding in the last point did not cause any additional inversions).
Now suppose that j = 2. This implies that ( k− 1)%(n + 1) = 1. This will occur
only if k =𝓁(n + 1) + 1 for some integer𝓁. If j = 2, then Invn+1(π′) = 1, since n + 1
101
will only cause an inversion with an element in the nth position. We have
P{j = 2} =
∞∑
i=0
qi(n+1)+1(1−q) = q(1−q)
1−qn+1
and in this case, we have
Pn+1(π) = qInv(π)q∏n+1
k=1
1−qk
1−q
as desired.
This pattern will continue in general. Suppose that adding in n + 1 causes I
inversions. Then, we know that it must have been added in at positionn+1−I. From
the algorithm, this means that j =I + 1. This will occur only if (k− 1)%(n + 1) =I.
In this case
P{j =I + 1} =
∞∑
i=0
qi(n+1)+I(1−q) = qI(1−q)
1−qn+1
From this, we have
Pn+1(π′) = qInv(π)qI
∏n+1
k=1
1−qk
1−q
which completes the proof.
