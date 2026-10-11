---
doc_id: arxiv-hep-th-0001202v2
doc_title: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees"
section_id: sec-015-6-prospects
section_title: "Prospects"
section_number: 6
pages: 17-19
source_pdf: 0001202v2.pdf
source_sha256: b2e3e22ea3d51c0b
doc_brief: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees — The renormalization of quantum ﬁeld theory twists the antipode of a non- cocommutative Hopf algebra"
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.989
---
In this paper, we were content to study the bigrading of the Hopf algebra of undecorated [@BK1; @BK2] rooted trees, by the number of nodes and a degree of primitivity analyzed by iterations of the coproduct. The extension of this bigrading to the decorated [@Over; @DR2] case is the obvious next step, in our plan to decode the rich structure of mature quantum field theory. The present work makes it clear that the key feature will be the nontriviality of $C:=B_+\circ B_-\not=B_-\circ B_+={\rm id}$. In the undecorated case, we have shown that the bifiltration of the Hopf algebra is obtained by adjoining the single-node tree to the bifiltration of the kernel of $C$. The proof of this lies in the powerful generalization ([\[Vk\]](#Vk){reference-type="ref" reference="Vk"}) of the concept of natural growth, which diagonalizes ([\[Ukm\]](#Ukm){reference-type="ref" reference="Ukm"}). First results for the commutator $[B_+,B_-]=C-{\rm id}$ of the decorated Hopf algebra of full quantum field theory were recently given in [@shuffle]. These increase our hopes that it will not take another 50 years to complete the characterization of the intricate interrelation of combinatorics *and* analysis that makes quantum field theory possible. We firmly believe that further elucidation of its structure has much to offer for wide areas of both physics and mathematics.

This study began during the workshop *Number Theory and Physics* at the ESI in November 1999, where we enjoyed discussions with Pierre Cartier, Werner Nahm, Ivan Todorov and Jean-Bernard Zuber. Work with Alain Connes at the IHES supports the present paper. System management by Chris Wigglesworth enabled accumulation of crucial data, which Neil Sloane's `superseeker` helped us to decode.

# Appendix: asymptotic enumerations

Here we consider inequalities inferred from Tables 3 and 4 and show that they persist at large weights, thanks to the upper bound $c<3$ on the Otter constant [@Otter].

Asymptotically, the number of rooted trees is given by $$r_n={c^n n^{-3/2}}(b+O(1/n))
\label{asy}$$ with Otter constants that we evaluated in [@BK1]:

       b = 0.43992401257102530404090339143454476479808540794011
             98576534935450226354004204764605379862197779782334...
       c = 2.95576528565199497471481752412319458837549230466359
             65953504724789059647331395749510866682836765813525...

The asymptotic fraction of trees assigned to primitivity $k$ in the filtration of Table 4 is $$f_k:=\lim_{n\to\infty} {P_{n,k}\over r_n}=
\left(1-{1\over c}\right)^{k-1}{1\over c}
\label{fk}$$ while the asymptotic fraction of forests in Table 3 is $$g_k:=\lim_{n\to\infty} {H_{n,k}\over r_{n+1}}=\frac{k f_k}{c}
=\left(1-{1\over c}\right)^{k-1}{k\over c^2}\,.
\label{gk}$$ These follow by using [@BK1] $|1-R(x)|^2=O(1-c x)$, near $x=1/c$. Numerically, $$\begin{aligned}
g_1&=&
0.1144616788557279695\ldots\\
g_2&=&
0.1514735822429146084\ldots\\
g_3&=&
0.1503401379409753267\ldots\\
g_4&=&
0.1326357110750687024\ldots\\
g_5&=&
0.1097026887662558145\ldots\\
g_6&=&
0.0871054456752243543\ldots\\
g_7&=&
0.0672417311397409555\ldots\\
g_8&=&
0.0508484386279160206\ldots\\
g_9&=&
0.0378509630072558308\ldots
\end{aligned}$$ with $k=2$ giving the largest fraction of forests at large $n$. This was not apparent until $n=28$, where we found that $H_{28,2}=20\,716\,895\,918$ exceeds $H_{28,3}=20\,710\,700\,277$.

The asymptotic results establish inequalities ([\[keq2\]](#keq2){reference-type="ref" reference="keq2"},[\[kgt2\]](#kgt2){reference-type="ref" reference="kgt2"}) at large $n$, where it is sufficient that $c<3$. Amusingly, this upper bound and the condition $R(1/c)=1$ produce a rather tight lower bound $$c=\exp\left(\sum_{k>0}{R(c^{-k})\over k}\right)
>\exp\left(1+\sum_{k>1}{1\over(3^k-1)k}\right)>2.943
\label{lower}$$ from the rather loose lower bound $R(x)\ge R_{\rm ladder}(x)=x/(1-x)$.
