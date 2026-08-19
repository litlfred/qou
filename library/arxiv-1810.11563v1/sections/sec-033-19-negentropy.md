---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes Leonard Susskind"
section_id: sec-033-19-negentropy
section_title: "Negentropy"
section_number: 19
pages: 67-69
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes Leonard Susskind — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to"
---
it to be minus the entropy. We’ll need to be a little more precise. Suppose we have a
certain amount of energy available, and also suppose the entropy of the system is S. The
system may be out of equilibrium, in which case S will be less than the maximal entropy
(consistent with that amount of energy). The negentropy is the diﬀerence between the
maximum entropy and the actual entropy,
negentropy = Smax− S
Negentropy is the room for entropy to grow. Whenever negentropy is non-zero, some
amount of work can be extracted, but in doing the work one must expend negentropy.
When all the negentropy is used up a system will be in thermal equilibrium, and no
further work can be extracted.
I explained in Lecture I that complexity is a lot like entropy, not the usual entropy
of a quantum system but the entropy of an auxiliary classical system. The auxiliary
66
system describes the motion of a state-vector in Hilbert space, or the motion of the time-
development operator U(t) on SU (2K). It is natural to ask whether there is a concept
analogous to negentropy that represents a resource, and for what purpose is it a resource?
19 Negentropy
Let’s begin with some examples of negentropy. Consider a box of gas composed of n
classical particles. The microstate of the box is deﬁned by n points in the phase space of
a single particle. The macrostate can be described thermodynamically in terms of a much
smaller number of thermodynamic variables including entropy. If the entropy is maximal
(subject to some constraint) then the gas is in equilibrium and the negentropy is zero. No
work can be extracted.
Now suppose we have two thermodynamically identical boxes of gas, where each box
is in thermal equilibrium. Let’s also assume the microstates are uncorrelated except for
the fact that they are macroscopically similar. See ﬁgure 34
Figure 34
The entropy of either box is Smax and the total entropy is 2Smax. Moreover the maxi-
mum total entropy is also 2Smax. It follows that the negentropy is zero and no work can
be be extracted.
Now let’s compare that with another example involving the same two boxes, each in
equilibrium, but this time the microstates are identical as illustrated in ﬁgure 35 .
Figure 35
67
Each box is in equilibrium but the combined system has much less entropy than the
previous example. In fact the total entropy is exactly the same as for the individual boxes,
S(total) = Smax
Smax(total) = 2 Smax
Negentropy = Smax (19.83)
In other words the high degree of correlation between the microstates gives rise to ne-
gentropy, a resource which in principle can be exploited to do a signiﬁcant amount of
work.
Exercise: Design a machine to extract work from this setup.
Then patent it.
