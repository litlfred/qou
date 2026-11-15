---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-002-12-the-main-technical-problem-convolution-in-sq
section_title: "The main technical problem: convolution in Sq"
section_number: 1.2
pages: 2-4
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.99
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
[]{#subsec:convolutioninSq label="subsec:convolutioninSq"}

Convolution of central functions $f,g\in{\mathbb{C}}({{S}}_{q})$ has a very simple structure if we write them as linear combinations of characters: if $$f(\pi)=\sum_{\lambda\vdash q}
a_\lambda \frac{\chi^{\lambda}(e) \chi^\lambda(\pi)}{q!}, \qquad
g(\pi)=\sum_{\lambda\vdash q} b_\lambda \frac{\chi^{\lambda}(e)
\chi^\lambda(\pi)}{q!}$$ then $$(f g)(\pi)=
\sum_{\lambda\vdash q} a_\lambda b_\lambda \frac{\chi^{\lambda}(e)
\chi^\lambda(\pi)}{ q!},$$ where the product $f g$ denotes a product of elements of the group algebra, i.e. the convolution of functions. However, in many cases we cannot afford the luxury of using the character expansion, for example in the case when we actually try to find the asymptotics of characters. For this reason we should find some other families of central functions on ${{S}}_{q}$ for which the convolution would have a relatively simple form.

In Section [\[subsec:definicjasigma\]](#subsec:definicjasigma){reference-type="ref" reference="subsec:definicjasigma"} we shall define such a family $\Sigma_{k_1,\dots,k_m}\in{\mathbb{C}}({{S}}_{q})$ which has a particularly simple structure: $\Sigma_{k_1,\dots,k_m}$ is (up to a normalizing factor) an indicator of the conjugacy class of permutations with a prescribed cycle decomposition $k_1,\dots,k_m$. This great simplicity has very appealing consequences: it will be very easy to evaluate functions $\Sigma$ on permutations and also it will be very simple to write any central function on ${{S}}_{q}$ as a linear combination of functions $\Sigma$ (operations which are somewhat cumbersome for characters). This object was introduced and studied by Ivanov and Kerov [@IvanovKerov1999].

A question arises how to express a product $\Sigma_{k_1,\dots,k_m}\cdot \Sigma_{l_1,\dots,l_n} \in {\mathbb{C}}({{S}}_{q})$ as a linear combination of some other normalized conjugacy class indicators $\Sigma$. This problem is very closely related to calculation of the, so called, connection coefficients [@GouldenJackson1996connection; @GouldenJacksonLatour; @Goupil1990; @Goupil1994; @GoupilSchaeffer1998]. The latter problem asks for the number of solutions of the equation $\pi_1 \pi_2 \pi_3=e$ where $\pi_1,\pi_2,\pi_3\in {{S}}_{q}$ must have a prescribed cycle structure. The formulas for the connection coefficients are available in many concrete cases, however they are not satisfactory for the purpose of this article.

### The first main result: calculus of partitions and genus expansion

It turns out that the solution to the above problem can be obtained by considering some more general objects. In Section [\[subsec:pierwszawzmiankaofppsq\]](#subsec:pierwszawzmiankaofppsq){reference-type="ref" reference="subsec:pierwszawzmiankaofppsq"} we shall define normalized conjugacy class indicators $\Sigma_{\pi}$ which are indexed no longer by sequences of integers but by partitions of finite ordered sets. We also equip partitions with an explicit multiplicative structure in such a way that $\Sigma$ becomes a homomorphism. For this reason we can in fact forget in applications about the symmetric group ${{S}}_{q}$ and perform all calculations in the partition language.

In applications we are interested in the asymptotic behavior of the contribution of various conjugacy classes when $q\to\infty$. It turns out that the order of such a contribution of $\Sigma_{\pi}$ can be read directly from the genus of a two-dimensional surface associated to the partition $\pi$; in this way our description is very similar to the genus expansion for random matrices [@Zvonkin1995matrixintegrals]. Even more striking is that the degree $q$ of the symmetric group ${{S}}_{q}$ does not enter into the multiplicative structure of partitions and therefore the calculus of partitions is able to provide statements about symmetric groups which do not depend on $q$. Another great advantage is that the moments of the Jucys--Murphy element (which are closely related to the moments of the transition measure) can be easily expressed within our calculus.

All these features make the calculus of partition and its genus expansion a perfect tool for the study of symmetric groups.

Unfortunately, one of our ultimate goals---formulas which relate characters and the moments of the transition measure---turn out to be quite involved and we need also some other tools to solve this problem. As we shall see in the following, these tools are provided by the free probability theory.
