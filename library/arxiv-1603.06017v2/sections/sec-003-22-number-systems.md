---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-003-22-number-systems
section_title: "Number Systems"
section_number: 2.2
pages: 4-6
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
example, the automaton in Figure 2.1 accepts binary representations of numbers. In a moment we will extend our deﬁnition
of automata to
¡
Q,q0,F,δ,S1,S2,...,Sn
¢
, where the Sj are number systems and concealed in them are alphabets ΣSj among
other things.
2.2
Number Systems
In any course on theory of computation, it is customary to talk about the representations of the objects an algorithm/Turing
machine takes as inputs. At the core of Walnut are automata taking natural numbers as inputs, and doing various computa-
tions on them, so ﬁxing a representation for natural numbers is essential. We could limit ourselves to binary representations.
However, there are many interesting automata accepting representations in number systems other than the binary one. So
we are going to deﬁne, in general terms, the concept of a number system. Walnut allows number systems to be deﬁned and
used (with a few restrictions to the general deﬁnition below).
Deﬁnition 2 (number systems). A number system S is a 3-tuple (ΣS,RS,[]S) of alphabet ΣS ⊇{0,1}, language RS ⊂Σ∗
S of valid
representations containing 0∗and at least one of 0∗1 or 10∗, and decoding function []S : RS →N that assigns integers to every
word in RS and for which []S(w) is usually written as [w]S. The decoding function has the following additional properties:
• [z]S = 0 if and only if z ∈0∗
• [1]S = 1
• For all w ∈RS, either zw ∈RS and [zw]S = [w]S for all z ∈0∗, or wz ∈RS and [wz]S = [w] for all z ∈0∗. The former is
called an msd number system and the latter is called an lsd number system2.
• For all positive n ∈N, there exists w ∈RS for which [w]S = n and w[0]̸ = 0 if S is msd or w[|w|−1]̸ = 0 if S is lsd. The
word w, if unique, is called the canonical encoding of n in S, and is sometimes denoted by (n)S. We let (0)S = ϵ.
The addition relation +S ⊂R3
S is deﬁned such that (x, y,z) ∈+S if and only if x, y,z are of the same length and [x]S = [y]S +[z]S.
The equality relation =S⊂R2
S is deﬁned such that (x, y) ∈=S if and only if x and y are of the same length and [x]S = [y]S.
The less than relation is deﬁned as <S⊂R2
S for which (x, y) ∈<S if and only if x and y are of the same length and [x]S < [y]S.
We adopt the in-order notation for +S, =S, and <S, i.e., we write x = y +S z, x =S y, and x <S y as opposed to the more
cumbersome (x, y,z) ∈+S, (x, y) ∈=S, and (x, y) ∈<S respectively. It follows from the deﬁnition that for all n ∈N, the set of
representations of n in S, deﬁned by {w : [w]S = n} is non-empty.
2msd and lsd are short for most-signiﬁcant-digit-ﬁrst and least-signiﬁcant-digit-ﬁrst, respectively. However, it should not be taken literally in this
deﬁnition, as one could deﬁne msd number systems (in the sense deﬁned here), with no direct correspondence to the notion of most-signiﬁcant-digit-ﬁrst
representation.
4
For example, the most-signiﬁcant-digit binary system, denoted by msd_2, is deﬁned by ({0,1},{0,1}∗,[]msd_2) where
[w]msd_2 =
|w|−1
X
i=0
[w[i]]msd_22|w|−i−1,
e.g., [001001]msd_2 = 0·25 +0·24 +1·23 +0·22 +0·21 +1·20 = 9. For msd_2, we are very fortunate to have simple automata
computing all of its important aspects, namely, valid representations Rmsd_2, the addition relation +msd_2, the equality
relation =msd_2, and the less-than relation <msd_2. See Figures 2.2,2.3,2.4, and 2.5 respectively.
Figure 2.2: Automaton computing Rmsd_2
Figure 2.3: Automaton computing +msd_2
Figure 2.4: Automaton computing =msd_2
Figure 2.5: Automaton computing <msd_2
5
We can deﬁne the least-signiﬁcant-digit-ﬁrst binary system, denoted by lsd_2, in a similar way. In fact, we can deﬁne
msd_n and lsd_n for all n ≥2, and for all of them, there are simple automata computing valid representations, addition,
equality, and less-than relations. In fact we can deﬁne the following:
Deﬁnition 3 (number systems in Walnut). Number systems for which the automata for representations, addition, equality,
and less-than exist, and equality is the same as word equality, i.e., x =S y if and only if x = y, are exactly the type of number
systems one can deﬁne and use in Walnut. Note that the alphabet of a number system is restricted to ﬁnite subsets of Z due
to the same restriction on automata in Walnut.
In addition to base-n number systems, Walnut has a built-in deﬁnition for the Fibonacci number system.
The most-signiﬁcant-digit-ﬁrst Fibonacci system, denoted by msd_ﬁb, is deﬁned by ({0,1},0∗(ϵ | 1)(0 | 01)∗,[]msd_ﬁb)
where
[w]msd_ﬁb =
|w|−1
X
i=0
[w[i]]msd_ﬁbF|w|−i−1,
where Fi is the i’th Fibonacci number given by F0 = 1,F1 = 2, and Fi = Fi−1 +Fi−2 for i ≥2. For example, [001001]msd_ﬁb =
0 · F5 + 0 · F4 + 1 · F3 + 0 · F2 + 0 · F1 + 1 · F0 = 6. The set of valid representations is exactly the set of binary words avoiding
consecutive 1s. The avid reader might want to verify that msd_ﬁb is a number system. There are automata computing all
major aspects of msd_ﬁb. For example, here is the automaton accepting Rmsd_ﬁb3:
Figure 2.6: Automaton computing Rmsd_ﬁb
In cases, where an automaton’s inputs are representations of integers in some number system, which by far are the most
important type of automata in Walnut, we would like to signify these number systems instead of the input alphabets. For
example, we might write
¡
Q,q0,F,δ,S1,S2,...,Sn
¢
to mean
¡
Q,q0,F,δ,ΣS1,ΣS2,...,ΣSn
¢
. It should be understood that in these
cases, if for a word w input πj (w) is not a valid representation in Sj, it does not mean that the automaton’s behavior is not
deﬁned for w. This just means that w is, by default, not going to get accepted. The behaviors of both automata and automata
with output that are taking representations of numbers in some number systems as inputs are deﬁned for all words (even
those not representing numbers in the given number systems).
2.3
