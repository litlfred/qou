---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-020-41-toy-example
section_title: "Toy example"
section_number: 4.1
pages: 18-18
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 1.0
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
Let us have a look on the main result (Theorem and Definition [\[theo:main\]](#theo:main){reference-type="ref" reference="theo:main"}) for the simplest nontrivial case of $n=2$. This will give us a heuristical insight into the problems which we shall encounter in the proof.

As we shall see in the following, the proof of the equivalence [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"} and [\[eq:faktoryzacja4\]](#eq:faktoryzacja4){reference-type="eqref" reference="eq:faktoryzacja4"} is very easy, therefore the main difficulty is to show the equivalence of the conditions [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"}, [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"}, [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"}. For simplicity, we shall concentrate on the implications in only one direction [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"}$\implies$[\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"}$\implies$[\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"}.

The condition [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"} for $n=2$ requires that $k(\Sigma_{l_1},\Sigma_{l_2})$ should not grow too fast. The identity $$\begin{gathered}
\label{eq:problemy} k(\Sigma_{l_1},\Sigma_{l_2})=\chi(\Sigma_{l_1}
\Sigma_{l_2})-\chi(\Sigma_{l_1}) \chi(\Sigma_{l_2}) =\\
\chi(\Sigma_{l_1} \Sigma_{l_2}-\Sigma_{l_1}\bullet \Sigma_{l_2})+
\big[ \chi(\Sigma_{l_1} \bullet \Sigma_{l_2}) - \chi(\Sigma_{l_1})
\chi(\Sigma_{l_2}) \big]
\end{gathered}$$ shows that there are three reasons why $k(\Sigma_{l_1},\Sigma_{l_2})$ is non-zero:

1.  []{#diff:1 label="diff:1"} the difference $\Sigma_{l_1} \Sigma_{l_2}-\Sigma_{l_1}\bullet
    \Sigma_{l_2}$ is non-zero. We need to estimate the conjugacy classes contributing to this difference.

2.  []{#diff:2 label="diff:2"} there are $q^{\underline{l_1}} q^{\underline{l_2}}$ summands which contribute to $\chi(\Sigma_{l_1}) \chi(\Sigma_{l_2})$ while there are only $q^{\underline{l_1+l_2}}$ summands which contribute to $\chi(\Sigma_{l_1} \bullet\Sigma_{l_2})$. Under the simplifying assumption that $\chi(\pi_1 \pi_2)\approx \chi(\pi_1) \chi(\pi_2)$ the second summand in [\[eq:problemy\]](#eq:problemy){reference-type="eqref" reference="eq:problemy"} is therefore of order $$(q^{\underline{l_1+l_2}}-q^{\underline{l_1}} q^{\underline{l_2}}) \chi(\pi_1
    \pi_2).$$ We need to find an estimate for $(q^{\underline{l_1+l_2}}-q^{\underline{l_1}} q^{\underline{l_2}})$.

3.  []{#diff:3 label="diff:3"} every summand contributing to $\chi(\Sigma_{l_1})
    \chi(\Sigma_{l_2})$ is equal to $\chi(\pi_1 \pi_2)$ while every summand contributing to $\chi(\Sigma_{l_1,l_2})$ is equal to $\chi(\pi_1) \chi(\pi_2)$. We need to find an estimate for $(\chi(\pi_1 \pi_2)-\chi(\pi_1) \chi(\pi_2))$.

The difficulty caused by [\[diff:3\]](#diff:3){reference-type="eqref" reference="diff:3"} can be very easily overcome: it is basically the condition [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"}. Our proof of the main result will be therefore divided into two parts; each devoted to one of the remaining difficulties.

Note that the second summand in [\[eq:problemy\]](#eq:problemy){reference-type="eqref" reference="eq:problemy"} can be written as $$k^{\bullet}(\Sigma_{l_1},\Sigma_{l_2})=\chi(\Sigma_{l_1} \bullet \Sigma_{l_2}) - \chi(\Sigma_{l_1})
\chi(\Sigma_{l_2});$$ in other words the proof of the proof of the implication [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"}$\implies$[\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"} is equivalent to overcoming the difficulty [\[diff:2\]](#diff:2){reference-type="eqref" reference="diff:2"} and the proof of the implication [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"}$\implies$[\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"} is equivalent to overcoming the difficulty [\[diff:1\]](#diff:1){reference-type="eqref" reference="diff:1"}.
