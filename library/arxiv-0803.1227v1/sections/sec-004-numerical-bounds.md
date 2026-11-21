---
doc_id: arxiv-0803.1227v1
doc_title: "Linear programming bounds for unitary space time codes"
section_id: sec-004-numerical-bounds
section_title: "Numerical bounds"
section_number: null
pages: 7-9
source_pdf: 0803.1227v1.pdf
source_sha256: cf72e0fcdc7f3ddf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 1.0
doc_brief: "Linear programming bounds for unitary space time codes — The linear programming method is applied to the space Un(C) of uni- tary matrices in order to obtain bounds for codes relative to the"
---
Numerical programs give accurate approximations of the best linear programming bounds over a large interval of validity, not covered by the bounds proved in Section IV. The following curves plot the linear programming bound on the diversity functions as a function of the cardinality of the code. The programs optimize the choice of a polynomial in the variables $(\cos\theta_1,\dots,\cos\theta_n)$, with degree at most equal to some parameter $D$. Increasing $D$ gives accurate results over a wider range of values for the diversity functions, but also increase the computational time. We use $D=19$ for $n=2$ and $D=13$ for $n=3$. ![image](U2SUM_ROS.eps){width="6.2cm"}\
![image](U2PROD_ROS.eps){width="6.2cm"}\
![image](U3SUM_ROS.eps){width="6.2cm"}\
![image](U3PROD_ROS.eps){width="6.2cm"}\
The Tables I and II compare the linear programming bounds for the dimensions $2$ and $3$ with the previous results of [@RECITE] and [@ROSEN] and show an improvement in all cases.

These tables give upper bounds for the diversity when the cardinality $N$ is fixed. All entries except the ones of the last line (LP $d_\Pi$) are concerned with the diversity sum. The second line tabulates the bounds settled in [@RECITE], obtained using Coxeter upper bounds. The two bounds of [@ROSEN] were obtained using sphere volume computations.

            N              24       48       64       80
  --------------------- -------- -------- -------- --------
   bounds in [@RECITE]   0.6746   0.6193   0.5969   0.5799
       B1 [@ROSEN]       0.7598   0.6603   0.6131   0.5932
       B2 [@ROSEN]       0.7794   0.6734   0.6235   0.6026
      LP $d_\Sigma$      0.6547   0.5797   0.5488   0.5254
       LP $d_\Pi$        0.5730   0.4989   0.4711   0.4504

  : $n=2$

            N             100      120      128      1000
  --------------------- -------- -------- -------- --------
   bounds in [@RECITE]   0.5632   0.5499   0.5452  
       B1 [@ROSEN]       0.5578   0.5425   0.5347   0.3270
       B2 [@ROSEN]       0.5654   0.5496   0.5415   0.3285
      LP $d_\Sigma$      0.4999   0.4816   0.4753   0.2964
       LP $d_\Pi$        0.4301   0.4144   0.4089   0.2574

  : $n=2$

         N           24       48       64       80
  --------------- -------- -------- -------- --------
   LP $d_\Sigma$   0.7178   0.6939   0.6797   0.6692
    LP $d_\Pi$     0.6431   0.5942   0.5752   0.5628

  : $n=3$

\

         N          100      120      128      1000
  --------------- -------- -------- -------- --------
   LP $d_\Sigma$   0.6598   0.6532   0.6511   0.5586
    LP $d_\Pi$     0.5482   0.5369   0.5332   0.4330

  : $n=3$

Moreover, concerning the diversity product, both our numerical results and analytic results (compare ([\[DEG2SUM\]](#DEG2SUM){reference-type="ref" reference="DEG2SUM"}) and ([\[DEG2PROD\]](#DEG2PROD){reference-type="ref" reference="DEG2PROD"})) show a large gap between the bounds for diversity sum and diversity product, in favor of the diversity product. This is worth to point out since in previous publications bounds for the diversity product were essentially deduced from the trivial inequality $\Sigma \Nu \ge \Pi \Nu$ and hence appear to be weak.
