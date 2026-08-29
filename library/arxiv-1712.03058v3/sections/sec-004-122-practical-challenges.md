---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to"
section_id: sec-004-122-practical-challenges
section_title: "Practical challenges"
section_number: 1.2.2
pages: 4-5
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
doc_brief: "Iterated filtering methods for Markov process epidemic models Theresa Stocks1 1Department of Mathematics, Stockholm University, Sweden This manuscript is a preprint of a Chapter to appear in the Handb"
---
In principle, the optimization problem in (1) looks rather straightforward,
however, there are a number of challenges in practice. Firstly, the evalu-
ation of L can be diﬃcult because the function might not be available in
closed form. Secondly, even if evaluation is possible, it might be very hard to
derive the ﬁrst and higher order derivatives of L analytically or even numer-
ically which are needed for numerical optimization methods, cf. Nocedal and
Wright (1999). In this case we need derivative-free optimizers. Those op-
timizers might impose other problems, for example when the likelihood can
only be approximated stochastically, e.g. by Monte Carlo methods (Robert
and Casella, 2004). In that case standard deterministic derivative-free opti-
mizers fail. All the problems mentioned above occur for the model class at
hand because the likelihood is a complex integral. In the following sections we
will give more rigorous details about the problem and introduce a method
which gets around these challenges. The problems mentioned arise in the
speciﬁc setting of our model formulation. In addition, there are some other
general challenges with likelihood-based inference in a statistical context.
Usually, the point estimate we obtain from maximum likelihood estimation
is not very meaningful by itself unless we also quantify the uncertainty of
CHAPTER 1. ITERATED FILTERING METHODS FOR POMP
4
the estimate. One way to solve this problem in a likelihood setting is to con-
struct conﬁdence intervals for the parameters by e.g. calculating the proﬁle
log-likelihood for each parameter of interest and invert Wilks’ likelihood ratio
test to get the desired intervals (Wilks, 1938). Another very common chal-
lenge is that often there exist multiple local maxima and the optimization
algorithm can get stuck in one of these and not return the global maximum.
It is therefore important to use a wide range of starting values for the nu-
merical algorithm in order to improve chances that the global maximum is
reached.
Moreover, it might very well happen that the maximum is not
unique because the surface of the likelihood function has ridges.
In that
case conﬁdence intervals are a good way to quantify the parameter range. In
the following, we introduce and formulate the likelihood of partially observed
Markov processes and explain how to tackle all of the issues mentioned above.
1.3
Inference for partially observed Markov
processes (POMP)
In the literature partially observed Markov processes are also known as hid-
den state space models or stochastic dynamical systems. The main assump-
tion is that at discrete points in time we observe some noisy aspect of the
true underlying Markov process which is itself often continuous in time. In
