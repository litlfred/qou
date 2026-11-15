---
doc_id: arxiv-hep-th-0205308v2
doc_title: "WDVV Equations as Functional Relations"
section_id: sec-002-the-associativity-equations-as-cocycle-condition
section_title: "The associativity equations as cocycle conditions"
section_number: null
pages: 5-7
source_pdf: 0205308v2.pdf
source_sha256: 2de5a4f40d80174c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.96
doc_brief: "WDVV Equations as Functional Relations — 6 sections: Front matter; Introduction; WDVV and dispersionless Hirota equ"
---
We shall now derive some consequences of ([\[defc\]](#defc){reference-type="ref" reference="defc"}). For a fixed index $a$ $$d\varphi_k = dT_{ai}\,({\sf C}_a\sp{-1})\sp{i}_{\ k}$$ whence for any $b$ $$d\varphi_k = dT_{ai}\,({\sf C}_a\sp{-1})\sp{i}_{\ k}
= dT_{bj}\,({\sf C}_b\sp{-1})\sp{j}_{\ k}.$$ From these it follows that $$\label{tcct}
dT_{ai} = dT_{bj} \left({\sf C}_b^{-1}\cdot {\sf C}_a\right)^j_{\ i}
= dT_{bj}\left({\sf C}_j^{-1}\cdot {\sf C}_i\right)^b_{\ a},$$ where the last equality follows from the symmetry of the period matrices. For fixed $a$ and $b$ we may view these as giving a change of variables $$T_{ai} = T_{ai}(T_{bj}),\qquad\forall\ i , j,$$ and $$\label{tt}
{\partial T_{ai}\over\partial T_{bj}} = \left({\sf C}_b^{-1}\cdot {\sf C}_a\right)^j_{\ i}
=\left({\sf C}_j^{-1}\cdot {\sf C}_i\right)^b_{\ a}.$$ These equations may simply be viewed as the chain-rule $$\label{cv}
{\partial T_{ai}\over\partial T_{bj}} = \sum_s {\partial T_{ai}\over\partial\varphi_s}
{\partial\varphi_s\over\partial T_{bj}} = \left({\sf C}_b^{-1}\cdot {\sf C}_a\right)^j_{\ i},$$ where we understand (for fixed $b$) ${\partial\varphi_s\over\partial T_{bj}} = \left({\sf C}_b^{-1}\right)^j_{\ s}$ in terms of the change of variables $\varphi_s\leftrightarrow T_{bj}$. For future comparison we also record the identity (for fixed $a$, $b$, $c$) $$\label{3cvid}
\dfrac{\partial T_{ai}}{\partial T_{bj}}\dfrac{\partial T_{ck}}{\partial T_{ai}}
\dfrac{\partial T_{bl}}{\partial T_{ck}}
= ({\sf C}_b\sp{-1} {\sf C}_a)\sp{j}_{\ i} ({\sf C}_a\sp{-1} {\sf C}_c)\sp{i} _{\ k}
({\sf C}_c\sp{-1} {\sf C}_b)\sp{k} _{\ l}
=({\sf C}_b\sp{-1} {\sf C}_a {\sf C}_a\sp{-1} {\sf C}_c {\sf C}_c\sp{-1} {\sf C}_b)\sp{j} _{\ l}
=  \delta\sp{j} _l.$$

Thus far we have only used change of variables and the fact that the period matrix ([\[pematr\]](#pematr){reference-type="ref" reference="pematr"}) can be expressed in terms of only genus $g=N$ number of variables. Such will hold for *any* integrable system, but this does not mean the associativity equations ([\[WDVV\]](#WDVV){reference-type="ref" reference="WDVV"}) or ([\[crossmatr\]](#crossmatr){reference-type="ref" reference="crossmatr"}) must hold. Lets now see the meaning of these. From ([\[tt\]](#tt){reference-type="ref" reference="tt"}) we have $$\label{3cocy}
\dfrac{\partial T_{ai}}{\partial T_{bj}}\dfrac{\partial T_{bk}}{\partial T_{ci}}
\dfrac{\partial T_{cl}}{\partial T_{ak}}
= ({\sf C}_b\sp{-1} {\sf C}_a)\sp{j}_{\ i} ({\sf C}_c\sp{-1} {\sf C}_b)\sp{i} _{\ k}
({\sf C}_a\sp{-1} {\sf C}_c)\sp{k} _{\ l}
=({\sf C}_b\sp{-1} {\sf C}_a {\sf C}_c \sp{-1} {\sf C}_b {\sf C}_a\sp{-1} {\sf C}_c)\sp{j} _{\ l}.$$ Now from ([\[crossmatr\]](#crossmatr){reference-type="ref" reference="crossmatr"}) it follows also that the matrices of structure constants satisfy (for all $a$ and $b$) $$\label{crossinv}
{\sf C}_a\cdot {\sf C}_b^{-1} = {\sf C}_b^{-1}\cdot {\sf C}_a.$$ Substituting ([\[crossinv\]](#crossinv){reference-type="ref" reference="crossinv"}) into ([\[3cocy\]](#3cocy){reference-type="ref" reference="3cocy"}) we conclude that $$\label{cocycle}
\sum_{i,k}\
\dfrac{\partial T_{ai}}{\partial T_{bj}}\dfrac{\partial T_{bk}}{\partial T_{ci}}
\dfrac{\partial T_{cl}}{\partial T_{ak}}
= \delta\sp{j} _l.$$ Equally from ([\[cocycle\]](#cocycle){reference-type="ref" reference="cocycle"}) we deduce ([\[WDVV\]](#WDVV){reference-type="ref" reference="WDVV"}). Thus the WDVV equations are equivalent to the Hirota-like functional relations ([\[cocycle\]](#cocycle){reference-type="ref" reference="cocycle"}). The relation ([\[cocycle\]](#cocycle){reference-type="ref" reference="cocycle"}) is our main statement.
