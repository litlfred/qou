---
doc_id: arxiv-2409.09372v4
doc_title: "MARKOV TRACES ON DEGENERATE CYCLOTOMIC HECKE ALGEBRAS DEKE ZHAO Dedicated to Professor Yingbo Zhang on the occasion of her 80th birthday"
section_id: sec-003-4-non-normalized-markov-traces
section_title: "Non-normalized Markov traces"
section_number: 4
pages: 10-13
source_pdf: 2409.09372v4.pdf
source_sha256: b7eed67ec102ab3d
doc_brief: "MARKOV TRACES ON DEGENERATE CYCLOTOMIC HECKE ALGEBRAS DEKE ZHAO Dedicated to Professor Yingbo Zhang on the occasion of her 80th birthday — LetH n(u) be the degenerate cyclotomic Hecke algebra with"
---
In this section we construct aC(u)–linear function onH n(u) by using the standard bases and show
it constitutes a non-normalized Markov trace, thereby proving Theorem 1.5 from the introduction.
The following easy verified fact will be useful.
Lemma 4.1.For integers1≤k≤m−1andn≥1, we have
Jk
n+1sn =s nJk
n +
k−1X
i=0
Jk−1−i
n+1 Ji
n.
Proof.Apply induction onkandk= 1 follows by applying Eq. (1.3). Assume that it holds fork−1≥1.
Fork,
Jk
n+1sn =J k−1
n+1(snJn + 1)
=

snJk−1
n +
k−2X
i=0
Jk−2−i
n+1 Ji
n

Jn +J k−1
n+1
=s nJk
n +
k−2X
i=0
Jk−2−i
n+1 Ji+1
n +J k−1
n+1
=s nJk
n +
k−1X
i=0
Jk−1−i
n+1 Ji
n.
The proof is completed. □
Lemma 4.2.Define the bimodule map
ψn :H n(u)⊗Hn−1(u)Hn(u)⊕
m−1M
i=0
Hn(u)

→H n+1(u)
by
a⊗b⊕
m−1M
i=0
ai

7→as nb+
m−1X
i=0
aiJi
n+1.
Thenψ n is anH n(u)-bimodule isomorphism.
Proof.Analogous to Lemma 3.1’s proof using standard basis arguments.□
Givenz,y 1,...,y m−1∈C(u), we inductively define aC(u)-linear function Tr onH ∞(u) as follows.
Assume Tr is defined onH n(u). Forx∈H n+1(u) decomposed via Lemma 4.2 as
x=ψ n

a⊗b⊕
m−1M
k=0
αkJk
n+1

,
10
we define
(4.3) Tr(x) :=z·Tr(ab) + Tr(α 0) +
m−1X
k=1
Tr(Jk
n+1)Tr(αk),
where Tr(1) = 0 and Tr(Jk
n+1) determined by:
(M4) Tr(hsnJk
nsn) = Tr(Jk
n)Tr(h) for allh∈H n(u) and for all 1≤k≤m−1;
(M5) Tr(Jk
1 ) =y k for allk= 1,...,m−1.
Let us remark that (M4) and Lemma 4.1 show that
Tr(Jk
n+1) = Tr(Jk
n) +
k−1X
i=0
Tr(Ji
nJk−1−i
n+1 sn)
for 1≤k≤m−1,n= 1,2,....
Proposition 4.4.TheC(u)–linear functionTrsatisfies
(M1) Tr(sn) =zfor alln≥1;
(M3) Tr(xsny) =z·Tr(xy)for allx,y∈H n(u);
(M4’) Tr(snJk
nsn) = Tr(Jk
n)for1≤k≤m−1and for alln≥1.
Proof.(M1, M3) follows directly from Eq. (4.3) via bimodule structure, while (M4’) is immediate from
(M4). □
Remark4.5.This trace construction specializes to the Brundan–Kleshchev traceτ BK through parameter
specialization, analogous to [9, Lemma 4.3]. The non-normalized condition Tr(1) = 0 distinguishes it
from the normalized Markov traces while preserving essential conjugation properties.
We now show that theC(u)–linear function Tr defined by Eq. (4.3) is a trace onH ∞(u), i.e.,
Tr(αβ) = Tr(βα) for allα,β∈H ∞(u).
Our approach follows arguments parallel to those in Section 3.
Lemma 4.6.For anyx,y∈H n(u)and1≤k≤m−1,
Tr(xJk
n+1y) = Tr(Jk
n+1)Tr(xy).
Proof.Letw∈S n be expressed in Jones normal form:
w= (s i1si1−1···s k1)(si2si2−1···s k2)···(s irsir−1···s kr),
where 0< i 1 <···< i r < n, 0< k1 <···< k r≤n−1, andi j≥k j for allj. By Eq. (1.4), we may
assume thaty=J a1
1 ···J an
n w′sn−1, where 0≤a i≤m−1 andw ′∈S n−1.
Applying Lemma 2.3(ii, iii) for commutation relations:
Tr(xJk
n+1y) = Tr(xJk
n+1Ja1
1 ···J an
n w′sn−1)
= Tr(xJa1
1 ···J an
n w′sn−1Jk
n+1) (Lemma 2.3)
= Tr(xy)Tr(Jk
n+1).
It completes the proof. □
Lemma 4.7.For sllx,y∈H n(u),
Tr(xsnysn) = Tr(snxsny).
In particular, for all1≤k≤m−1,
Tr(Jk
nsnsn−1sn) = Tr(snJk
nsnsn−1).
Proof.The second equality follows from the first by takingx=J k
n andy=s n−1. We establish the first
equality through case by case analysis:
Case 1.x,y∈H n−1(u):
Tr(xsnysn) = Tr(xy) = Tr(snxsny).
Case 2.x∈H n−1(u),y=αs n−1βwhereα,β∈H n−1(u), or vice versa:
Tr(xsnysn) = Tr(xα(snsn−1sn)β) = Tr(snxsny).
Case 3.x=αs n−1β,y=δs n−1γwhereα,β,δ,γ∈H n−1(u):
Tr(xsnysn) = Tr(αsn−1βδ(snsn−1sn)γ) =z 2 Tr(αβδγ),
Tr(snxsny) = Tr(α(snsn−1sn)βδsn−1γ) =z 2 Tr(αβδγ).
11
Case 4.x∈H n−1(u),y=αJ ℓ
n whereα∈H n−1(u) and 1≤ℓ≤m−1, or vice versa:
Tr(xsnysn) = Tr(xαsnJℓ
nsn) = Tr(Jℓ
n)Tr(xα),
Tr(snxsny) = Tr(xαJℓ
n) = Tr(Jℓ
n)Tr(xα).
Case 5.x=αJ ℓ
n,y=βJ k
n whereα,β∈H n−1(u) and 1≤k,ℓ≤m−1:
Tr(xsnysn) = Tr(αβJℓ
nsnJk
nsn) = tr(Jk
n)tr(Jℓ
n)Tr(αβ),
Tr(snxsny) = Tr(αsnJℓ
nsnJk
nβ) = tr(Jℓ
n)Tr(Jk
n)Tr(αβ).
Case 6.x=αs n−1β,y=γJ ℓ
n whereα,β,γ∈H n−1(u), or vice versa:
Tr(xsnysn) = Tr(αsn−1βγsnJℓ
nsn) =zTr(J ℓ
n)Tr(αβγ),
Tr(snxsny) = Tr(αsnsn−1snβγJℓ
n) =zTr(J ℓ
n)Tr(αβγ).
All cases demonstrate the required equality, thus completing the proof.□
Lemma 4.8.For anyh n∈H n(u),1≤i≤n−1, and1≤k≤m−1,
Tr(hnsnsn−1···s iJk
isn) = Tr(snhnsnsn−1···s iJk
i ),
Tr(hnsnsn−1···s iJk
it) = Tr(thnsnsn−1···s iJk
i ).
Proof.For thefirst equality, we have
Tr(hnsnsn−1···s iJk
isn) = Tr(hnsnsn−1snsn−2···s iJk
i )
=zTr(h nsn−2···s iJk
i ).
For Tr(snhnsnsn−1···s iJk
i ), we apply the case by case analysis:
Case 1. hn∈H n−1(u):
Tr(snhnsnsn−1···s iJk
i ) = Tr(hnsn−1···s iJk
i )
=zTr(h nsn−2···s iJk
i ).
Case 2. hn =αs n−1βwhereα,β∈H n−1(u):
Tr(snhnsn···s iJk
i ) = Tr(αsnsn−1snβsn−1···s iJk
i )
=z 2 Tr(αβsn−2···s iJk
i )
=zTr(h nsn−2···s iJk
i ).
Case 3. hn =αJ ℓ
n whereα∈H n−1(u),1≤ℓ≤m−1:
Tr(snhnsn···s iJk
i ) = Tr(α(snJℓ
nsn)sn−1···s iJk
i )
=zTr(J ℓ
n)Tr(αsn−2···s iJk
i )
=zTr(h nsn−2···s iJk
i ).
Thus, the first equality holds.
Second Equality:By induction onn. It is trivial forn= 1. Assume it is true forn≥1. Forn+ 1,
we have
Tr(hn+1sn+1···s iJk
it) =zTr(h n+1sn···s iJk
it) (by (M3))
=zTr(th n+1sn···s iJk
i ) (inductive hypothesis)
= Tr(thn+1sn+1···s iJk
i ).
This completes the proof. □
Lemma 4.9.For anyh n∈H n(u),i= 1,...,n, and1≤k≤m−1, we have
Tr(hnJk
n+1t) = Tr(th nJk
n+1),
Tr(hnJk
n+1si) = Tr(s ihnJk
n+1).
Proof.Thanks to Lemma 2.4(vi),
Tr(hnJk
n+1t) = Tr(Jk
n+1)Tr(hnt) = Tr(Jk
n+1)Tr(thn) = Tr(thnJk
n+1),
where the second equality follows by the induction argument onn. Thus the first equality holds.
Now we show the second equality holds. Fori= 1,...,n−1,
Tr(hnJk
n+1si) = Tr(Jk
n+1)Tr(hnsi) = Tr(Jk
n+1)Tr(sihn) = Tr(sihnJk
n+1),
where the middle equality uses the induction hypothesis Tr(h nsi) = Tr(sihn).
12
Now Lemma 4.1 and Eq. (4.3) show
Tr(hnJk
n+1sn) =zTr(h nJk
n) +
k−1X
i=0
Tr(hnJi
nJk−1−i
n+1 ).
On the other hand, ifh n∈H n−1(u) thens nhn =h nsn and Lemma 4.1 shows
Tr(snhnJk
n+1) =zTr(h nJk
n) +
k−1X
i=0
tr(hnJi
nJk−1−i
n+1 ).
Ifh n =αs n−1β∈H n(u) whereα,β∈H n−1(u), then
Tr(snαsn−1βJk
n+1) = Tr(α(snJk
n+1)sn−1β)
=zTr(αJ k
nsn−1β) +
k−1X
i=0
Tr(αJi
nJk−1−i
n+1 sn−1β)
=zTr(h nJk
n) +
k−1X
i=0
Tr(hnJi
nJk−1−i
n+1 ),
where the last equality follows by an induction argument.
Ifh n =αJ ℓ
n∈H n(u) whereα∈H n−1(u) and 1≤ℓ≤m−1, then
Tr(snαJℓ
nJk
n+1) = Tr(α(snJk
n+1)Jℓ
n)
=zTr(αJ k+ℓ
n ) +
k−1X
i=0
Tr(αJi
nJk−1−i
n+1 Jℓ
n)
=zTr(h nJk
n) +
k−1X
i=0
Tr(hnJi
nJk−1−i
n+1 ).
Thus Tr(hnJk
n+1sn) = Tr(snhnJk
n+1) holds in all cases. It completes the proof.□
We are ready to show Tr is a trace function onH ∞(u).
Theorem 4.10.For alla,b∈H ∞(u),
Tr(ab) = Tr(ba).
Proof.We verify Tr(ax) = Tr(xa) inductively. Assume it holds for alla,b∈H n(u). Fora,b∈H n+1(u),
it suffices to check whenbis a generators i (1≤i≤n) ort, that is,
(∗) Tr(at) = Tr(ta) and Tr(as i) = Tr(sia) for 1≤i≤n.
Thanks to Theorem 2.6, we only need to check that Eq. (∗) holds whenais an element of the four forms
(I)—(IV): Ifais an element of form (I), i.e.,a=h n∈H n(u), then the induction hypothesis gives
Tr(hnt) = Tr(thn) and Tr(hnsi) = Tr(sihn) fori= 1,...,n−1.
Further Proposition 4.4(M3) shows
Tr(asn) =zTr(a) = Tr(s na).
Ifais an element of forms (II)—(IV), the assertion follows directly form Lemmas 4.7, 4.8, and 4.9.□
Now we can prove Theorem 1.5 in Introduction.
Proof of Theorem 1.5.(M1), (M3)–(M5) follow directly by Eq. (4.3) and (M2) follows by applying The-
orem 4.10. Note that having proved the existence, the uniqueness of Tr follows immediately. Indeed
Theorem 2.6 shows that Tr(x) can be clearly computed inductively using rules (M1)–(M4) for any
x∈H n+1(u). □
