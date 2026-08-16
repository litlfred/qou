---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-037-106-equivalence-of-spectral-networks
section_title: "Equivalence of spectral networks"
section_number: 10.6
pages: 68-70
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Given a nondegenerate spectral network W we have constructed a corresponding non-
abelianization map ΨW. It is natural to ask how this map depends on W.
We can get some intuition by remembering previous results about the case K = 2. In
that case, as already mentioned in §5.7,W determines an ideal triangulation T (W) of C
32Actually this universal bundle does not quite exist owing to subtleties involving the center of GL(K);
but its bundle of endomorphisms does exist, which is all we will use below.
– 66 –
up to isotopy. T (W) does not change if we vary W by an isotopy (while holding Σ ﬁxed).
Moreover, the map Ψ W in this case only depends on T (W). So we ﬁnd that Ψ W is an
isotopy invariant ofW.
We now extend this discussion to general K. We begin by deﬁning a notion of equiv-
alence between nondegenerate spectral networks. Our experience from the case K = 2
suggests that equivalence should at least include isotopy. In fact, for K > 2 it will be
natural to allow even some moves which are not isotopies. Given two nondegenerate spec-
tral networksW andW′, an equivalence betweenW andW′ is a one-parameter family of
path-lifting rules F(·,t ) to coverings Σ(t), such that:
E1. F (·, 0) = F(·,W) and F(·, 1) = F(·,W′).
E2. For any point ˜z on ˜C and pair 0 ≤ t1≤ t2≤ 1, there exists a formal sum of paths
R(˜z,t 1,t 2), such that for any path ℘ from ˜z1 to ˜z2 we have
F(℘,t 2) =R(˜z1,t 1,t 2)F(℘,t 1)R(˜z2,t 1,t 2)−1. (10.26)
The point of this deﬁnition is that if W andW′ are connected by an equivalence then we
have
ΨW = ΨW′. (10.27)
(The meaning of the equal signs in (10.26), (10.27) has to be clariﬁed in case the coverings
Σ(t) vary with t: in this case we identify the diﬀerent coverings using the “Gauss-Manin”
parallel transport induced by the family {Σ(t)}.)
One natural way of getting an equivalence is to consider a 1-parameter family of
nondegenerate spectral networksW(t) and takeF(·,t ) = F(·,W(t)). In this caseR(˜z,t 1,t 2)
is a product, with one factor of the form (1 + ∑
ν∈Sc(t) Xa(ν)) for each t with t1≤ t≤ t2
such that z lies on anS-wallpc(t) inW(t).
Here are some examples of equivalences:
M1. An isotopy. This is a one-parameter family of spectral networks W(t) subordinate to
coverings Σ(t), such that the Σ(t) vary continuously in the obvious sense (in particular
the branch points move continuously), each wall pc varies by isotopy, and the joints
zµ move continuously. The combinatorics ofW(t) do not change during an isotopy.
ij
jk
ij
jk
ik
ij
jk
jk
ij
Figure 43. Crossing at a defect: an equivalence which relates two non-isotopic spectral networks.
M2. A crossing at a defect. This is a family W(t) which implements a move as illustrated
in Figure 43. Here the combinatorics of the network do change at the critical value
t =tc. Nevertheless the family gives an equivalence.
– 67 –
ij
jk
ik
ij
jk
jk
ij
ij
jk
ij
jk
ij
jk
Figure 44. Bubble: an equivalence which relates two non-isotopic spectral networks.
ij
ji ij
(ij)kj
ki
kj
(ij) (ij)
kj kj
kj kjij ij
ji jiij ij
ki ki
Figure 45. Branch point traversal: an equivalence which relates two non-isotopic spectral networks.
M3. A bubble. This is a family W(t) which implements a move as illustrated in Figure 44.
M4. A traversal of a branch point . This is a family W(t) which implements a move as
illustrated in Figure 45. The member W(tc) strictly speaking is not quite a spectral
network according to our deﬁnition, because of the extra kj lines passing through
the branch point; nevertheless one can deﬁne F(·,tc) by a straightforward extension
of our rules, and after so doing, E1, E2 above are obeyed.
All of these equivalences really occur in practice, e.g. in families Wϑ as ϑ varies. We
emphasize that these equivalences are not the jumps ofWϑ which we studied in§6.2: those
jumps generally connect spectral networks which are inequivalent in our sense.
