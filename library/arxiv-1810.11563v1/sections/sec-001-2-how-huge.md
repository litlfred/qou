---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes Leonard Susskind"
section_id: sec-001-2-how-huge
section_title: "How Huge?"
section_number: 2
pages: 5-6
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes Leonard Susskind — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to"
---
Let’s consider the space of states of K qubits and make a simple estimate of its size.
By size I don’t mean the dimensionality of the space deﬁned by the number of mutually
orthogonal vectors. I mean something more like the total number of unit vectors. It’s of
course inﬁnite but we can regulate it.
The dimension of the Hilbert space is 2 K and a general vector has the form,
|Ψ⟩ =
2K
∑
1
αi|i⟩
The α are arbitrary complex numbers. At the moment we won’t worry about normal-
izing|Ψ⟩ or dividing out the overall phase. Now let’s regulate the inﬁnities by restricting
4
eachαi to be one of m values. The total number of states is,
#states =m2K
= exp (2K logm) (2.1)
ForK = 4, m= 4 the number of states is 4, 294, 967, 296.
The logarithm of the number of states is more manageable,
log (#states) = 2K logm≈ 22. (2.2)
There are two interesting things about 2.2. The ﬁrst is how strongly it depends on K,
namely it grows as 2 K. The second is how weakly it depends on the regulator parameter
m. We’ll see this trend many times in what follows.
