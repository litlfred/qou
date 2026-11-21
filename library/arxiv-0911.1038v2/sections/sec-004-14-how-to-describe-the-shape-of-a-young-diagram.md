---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-004-14-how-to-describe-the-shape-of-a-young-diagram
section_title: "How to describe the shape of a Young diagram?"
section_number: 1.4
pages: 3-4
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.674
latex_coverage_ratio: 0.952
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
A natural question arises: *how to choose parameters which describe the shape of a Young diagram in the most convenient way?* A very interesting answer for this question was proposed by Biane [@Biane1998] who for a (generalized) Young diagram $\lambda$ defined a family of parameters $R_2^{\lambda},R_3^{\lambda},\dots$, called *free cumulants* of $\lambda$.

The original definition of free cumulants of $\lambda$ given by Biane is quite involved (free cumulants of a Young diagram are Speicher's *free cumulants* [@NicaSpeicher2006] --- related to Voiculescu's *free probability theory* [@VoiculescuDykemaNica1992] --- of Kerov's *transition measure* [@Kerov1993] of the Young diagram $\lambda$), but it has an advantage that it is very explicit and allows an algorithmic computation of free cumulants in terms of the *shape* of a Young diagram.

From the results of Biane [@Biane1998] one can show the very surprising fact that for any integer $k\geq 1$ and any Young diagram $\lambda$ the values of the normalized character on dilations of $\lambda$ $$\mathbb{N} \ni s \mapsto \Sigma_k^{s\lambda}$$ are given by a polynomial function of degree (at most) $k+1$. Furthermore, the leading coefficient is equal to one of the free cumulants: $$\label{eq:biane}
R_{k+1}^{\lambda}=[s^{k+1}] \Sigma_k^{s\lambda} =
\lim_{s\to\infty} \frac{\Sigma^{s\lambda}_{k}}{s^{k+1}}.$$ From the perspective of the Biane's work [@Biane1998] this is a highly nontrivial and very interesting result: it shows that free cumulants (which are viewed as concrete, algorithmically computable quantities) describe the first-order asymptotics of characters. For the purposes of this article we can reverse the optics and take [\[eq:biane\]](#eq:biane){reference-type="eqref" reference="eq:biane"} as a convenient (even if somewhat abstract) definition of free cumulants.
