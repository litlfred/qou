---
doc_id: arxiv-math-9806163v1
doc_title: "arXiv:math/9806163v1 [math.CO] 30 Jun 1998"
section_id: sec-003-13-the-braid-group
section_title: "The Braid Group"
section_number: 1.3
pages: 6-9
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.953
---
.1in []{#sec-prelim label="sec-prelim"} The braid group of type $A$, $\mathcal{B}_n(A)$, can be defined algebraically by generators $\tilde{\sigma}_1,\tilde{\sigma}_2, \ldots, \tilde{\sigma}_{n-1}$ and relations $$\tilde{\sigma}_i\tilde{\sigma}_j=\tilde{\sigma}_j\tilde{\sigma}_i \ \ \ \ \mbox{if  $\  |i-j|>1$}, \label{eq:BR1}$$ $$\tilde{\sigma}_i\tilde{\sigma}_{i+1}\tilde{\sigma}_i=\tilde{\sigma}_{i+1}\tilde{\sigma}_i\tilde{\sigma}_{i+1} \ \ \ \mbox{if $\  1\leq i\leq n-2$} \label{eq:BR2}$$ Similarly we can define the braid group of type $B$, $\mathcal{B}_n(B)$, by generators $t, \sigma_1,\sigma_2, \ldots, \sigma_{n-1}$ and defining relations given by equations ([\[eq:BR1\]](#eq:BR1){reference-type="ref" reference="eq:BR1"}) and ([\[eq:BR2\]](#eq:BR2){reference-type="ref" reference="eq:BR2"}) and $$\label{eq:BR3}
\sigma_1t\sigma_1t=t\sigma_1t\sigma_1$$ $$\label{eq:BR4}
t\sigma_i=t\sigma_i \ \ \ \  \mbox{if  $\ i>1$}.$$ Below we illustrate the generator $\tilde{\sigma}_i \in \mathcal{B}_n(A)$, the full-twist $\Delta_3^2 \in \mathcal{B}_3(A)$, and the generators $t, \sigma_i \in \mathcal{B}_n(B)$.

::: picture
(400,140)(0,0) (40,30)(0,0)90 (38,122)1 (45,75) (50,75) (55,75) (65,75)(-1,6)7.5 (75,30)(-1,6)6 (57,122)i (60,30)(1,6)15 (73,122)i+1 (80,75) (85,75) (90,75) (95,30)(0,0)90 (95,122)n (60,20)$\tilde{\sigma}_i$ (155,110)(-1,5)2 (151,122)1 (165,110)(-1,5)2 (161,122)2 (175,109)(-1,5)2 (171,122)3 (150,105)(6,1)25 (165,83)(-1,5)4 (175,82)(-1,5)4 (155,83)(-1,5)4.3 (145,78)(6,1)30 (170,60)(-1,5)3 (160,61)(-1,5)3 (150,60)(-1,5)3.8 (145,56)(6,1)25 (150,30)(-1,5)5 (160,30)(-1,5)4 (170,30)(-1,5)4 (155,20)$\Delta_3^2$ (240,87)(0,0)33 (237,122)1 (216,82)(4,1)24 (216,82)(2,-1)10 (232,75)(2,-1)10 (242,30)(0,0)41 (250,30)(0,0)90 (247,122)2 (255,75) (260,75) (265,75) (270,30)(0,0)90 (267,122)n (245,20)$t$ (330,30)(0,0)90 (327,122)1 (335,75) (340,75) (345,75) (355,75)(-1,6)7.5 (340,122)i (350,30)(1,6)15 (353,122)i+1 (365,30)(-1,6)6 (370,75) (375,75) (380,75) (385,30)(0,0)90 (383,122)n (350,20)$\sigma_i$ (200,0)Figure 3
:::

In general, the full-twist $\Delta_f^2$ in $f$ strings, is an element in the center of $\mathcal{B}_f(A)$. Algebraically, $\Delta_f^2 =(\tilde{\sigma}_{f-1}\ldots\tilde{\sigma}_1)^f$. We now define a map from the generators of $\mathcal{B}_n(B)$ into $\mathcal{B}_{f+n}(A)$. We call the map $\tilde{\rho}_{f,n}$, and we define the image of the generators of $\mathcal{B}_n(B)$ as follows: $\tilde{\rho}_{f,n}(t)=\Delta_f^{-2}\Delta_{f+1}^2$ and $\tilde{\rho}_{f,n}(\sigma_i)=\tilde{\sigma}_{f+i}$ for $i=1,\ldots,n$. Pictorially, we have the following:

::: picture
(400,140)(0,0) (120,100)(0,0)25 (130,100)(0,0)25 (135,110) (140,110) (145,110) (150,103)(0,0)22 (162,99)(0,0)26 (108,88)(5,1)54 (120,40)(0,0)46 (130,40)(0,0)47 (108,88)(2,-1)10 (135,60) (140,60) (145,60) (150,40)(0,0)50 (152,69)(2,-1)10 (162,40)(0,0)24 (145,30)$\Delta^{-2}_f\Delta_{f+1}^2$ (118,127)$1$ (128,127)$2$ (147,127)f (157,127)f+1 (200,40)(0,0)85 (175,40)(0,0)85 (185,60) (190,60) (195,60) (185,110) (190,110) (195,110) (176,127)f+2 (198,127)f+n (25,106)(0,0)19 (0,94)(2,1)25 (0,94)(2,-1)10 (15,87)(2,-1)10 (25,40)(0,0)42 (33,40)(0,0)85 (38,60) (43,60) (48,60) (38,110) (43,110) (48,110) (52,40)(0,0)85 (21,127)$1$ (31,127)$2$ (50,127)$n$ (60,85)(1,0)40 (75,90)$\tilde{\rho}_{f,n}$ (30,30)$t$ (250,40)(0,0)85 (255,85) (260,85) (265,85) (270,124)(1,-6)6 (270,40)(1,6)14 (279,80)(1,-6)7 (284,85) (289,85) (294,85) (299,40)(0,0)85 (310,85)(1,0)30 (315,90)$\tilde{\rho}_{f,n}$ (248,127)1 (268,127)i (277,127)i+1 (297,127)n (270,30)$\sigma_i$ (350,40)(0,0)85 (355,85) (360,85) (365,85) (365,124)(1,-6)6 (365,40)(1,6)14 (375,80)(1,-6)7 (385,85) (390,85) (395,85) (404,40)(0,0)85 (402,127)f+n (348,127)1 (373,127)f+i+1 (358,127)f+i (375,30)$\tilde{\sigma}_{f+i}$ (200,5)Figure 4
:::

::: proposition
[]{#prop:rep1 label="prop:rep1"} Let $n,f\in \mathbb{N}$ and $\tilde{\rho}_{f,n}$ be as defined above for the generators of $\mathcal{B}_n(B)$. Then $\tilde{\rho}_{f,n}$ is a well-defined group homomorphism.
:::

It suffices to prove that $\tilde{\rho}_{f,n}$ preserves the relations of $\mathcal{B}_n(B)$. It is convenient to express $\tilde{\rho}_{f,n}(t)=\tilde{\sigma}_f\ldots\tilde{\sigma}_2\tilde{\sigma}_1^2\tilde{\sigma}_2\ldots\tilde{\sigma}_f$. Relations ([\[eq:BR1\]](#eq:BR1){reference-type="ref" reference="eq:BR1"}),([\[eq:BR2\]](#eq:BR2){reference-type="ref" reference="eq:BR2"}) and ([\[eq:BR4\]](#eq:BR4){reference-type="ref" reference="eq:BR4"}) follow immediately from the definition of $\tilde{\rho}_{f,n}$ and the definition of $\mathcal{B}_n(A)$. To show that ([\[eq:BR3\]](#eq:BR3){reference-type="ref" reference="eq:BR3"}) holds we will use the commuting property of the full-twist. $$\sigma_{f+1}\Delta_{f+1}^2\Delta_f^{-2}\sigma_{f+1}\Delta_{f+1}^2\Delta_f^{-2} = \Delta_{f+2}^2\Delta_{f+1}^{-2}\Delta_{f+1}^2\Delta_f^{-2} \\ = \Delta_{f+1}^{2}\Delta_f^{-2}\sigma_{f+1}\Delta_{f+1}^{2}\Delta_f^{-2}\sigma_{f+1}.$$ It might be easier to see that this relation holds from the picture, see figure 5. This completes the proof. $\Box$ .08in

::: picture
(400,150)(0,0) (80,117)(0,0)28 (80,87)(0,0)21 (80,50)(0,0)28 (85,140) (90,140) (95,140) (100,121)(0,0)24 (100,90)(0,0)22 (100,50)(0,0)31 (110,123)(0,0)22 (120,121)(0,0)24 (65,110)(5,1)55 (85,100) (90,100) (95,100) (110,88)(0,0)26 (65,110)(2,-1)10 (112,97)(2,-1)10 (122,50)(0,0)42 (65,80)(5,1)45 (85,65) (90,65) (95,65) (65,80)(2,-1)10 (102,67)(2,-1)10 (112,50)(0,0)12 (137,50)(0,0)95 (142,90) (147,90) (152,90) (157,50)(0,0)95 (78,147)1 (98,147)f (104,147)f+1 (118,147)f+2 (135,147)f+3 (155,147)f+n (57,40)$\tilde{\sigma}_{f+1}\Delta_f^{-2}\Delta_{f+1}^2\tilde{\sigma}_{f+1}\Delta^{-2}_f\Delta_{f+1}^2$ (180,90)$=$ (230,117)(0,0)28 (235,140) (240,140) (245,140) (250,121)(0,0)24 (260,119)(0,0)26 (270,86)(0,0)59 (215,110)(5,1)45 (230,83)(0,0)24 (235,100) (240,100) (245,100) (250,87)(0,0)24 (215,110)(2,-1)10 (252,97)(2,-1)10 (274,50)(0,0)8 (215,75)(5,1)55 (230,50)(0,0)23 (235,65) (240,65) (245,65) (250,50)(0,0)26 (215,75)(2,-1)10 (264,63)(2,-1)10 (262,87)(0,0)4 (262,50)(0,0)29 (287,50)(0,0)95 (292,90) (297,90) (302,90) (307,50)(0,0)95 (228,147)1 (248,147)f (254,147)f+1 (268,147)f+2 (283,147)f+3 (306,147)f+n (215,40)$\Delta_f^{-2}\Delta_{f+1}^2\tilde{\sigma}_{f+1}\Delta^{-2}_f\Delta_{f+1}^2\tilde{\sigma}_{f+1}$ (175,5)Figure 5
:::

::: cor
The representations $\rho_{f,n}$ can be extended in a natural way to representations of the corresponding braid group algebras.
:::

# Hecke Algebra of type $B_n$

In this context, we will mean by the Hecke algebra $H_n(q,Q)$ of type $B_n$ the free complex algebra with 1 and generators $t, g_1, g_2, \ldots, g_{n-1}$ and parameters $q,Q \in \mathbb{C}$ with defining relations

1.     $g_{i}g_{i+1}g_{i}=g_{i+1}g_{i}g_{i+1}$    for $i=1,2, \ldots, n-2$;

2.     $g_{i}g_{j}= g_{j}g_{i}$,    whenever $\mid i-j \mid \geq 2$;

3.     $g_i^2 = (q-1)g_i +q$     for $i=1,2, \ldots, n-1$;

4.     $t^2 = (Q-1)t +Q$;

5.     $tg_1tg_1=g_1tg_1t$;

6.     $tg_i=g_it$      for $i \geq 2$.

Note that for $q=1$ and $Q=1$, (H3) and (H4) become $g_i^2=1$ and $t^2=1$, respectively. In this case the generators satisfy exactly the same relations as a set of simple reflections of the hyperoctahedral group, $\mathcal{H}_n$. It is known that $H_n(q,Q)\cong \mathbb{C}\mathcal{H}_n$ (the group algebra of $\mathcal{H}_n$) if $q$ is not a root of unity and $Q\neq -q^s$ for $-n<s<n$. $\mathbb{C}\mathcal{H}_n$ is semisimple since it is a finite complex group algebra. This implies that $H_n(q,Q)$ is semisimple for generic values of $q$ and $Q$. Furthermore the simple modules are in 1-1 correspondence with double partitions. Their decomposition rule and their dimensions are the same as for $\mathcal{H}_n$. \[See Bourbarki, Groups et algebres de Lie IV, V, VI\] Hoefsmit, in [@h], has written down explicit irreducible representations of $H_n(q,Q)$ for each pair of Young diagrams. This demonstrates that dimension over $\mathbb{C}(q,Q)$ of $H_n(q,Q)$ is $2^nn!$. Let $V_{(\alpha,\beta)}$ be an $H_n(q,Q)$ module then we have the following restriction rule: $$V_{(\alpha,\beta)}{\Big|}_{H_{n-1}(q,Q)}\cong \bigoplus_{(\alpha,\beta)'\subset(\alpha,\beta)}V_{(\alpha,\beta)'},$$ where $(\alpha,\beta)'$ is the double partition obtained from $(\alpha,\beta)$ by subtracting one from one of the parts. This isomorphism follows from the bijection $t^{(\alpha,\beta)}\rightarrow t^{(\alpha,\beta)'}$ of $T_{(\alpha,\beta)}$ and $\bigcup_{(\alpha,\beta)'\subset (\alpha,\beta)}T_{(\alpha,\beta)'}$, where $t^{(\alpha,\beta)'}$ is the pair of standard tableaux obtained by removing the box containing $n$. Moreover, $\pi^{(n)}=\bigoplus_{(\alpha,\beta)\vdash n}\pi_{(\alpha,\beta)}$ is a faithful representation of $H_n(q,Q)$. Note that (H1) and (H2) are the defining relations for the braid group $\mathcal{B}_n(A)$. So representations of $H_n(q,Q)$ also yield in particular representations of $\mathcal{B}_n(A)$. Obviously we also obtain representations of the braid group of type $B$. The Hecke algebras satisfies the following embedding of algebras $H_0\subset H_1 \subset H_2 \subset \cdots$ We shall denote $$H_{\infty}(q,Q):= \bigcup_{n \geq 0}{H_n(q,Q)}$$ Observe that (H3) and (H4) imply that $t$ and $g_i$ have at most 2 eigenvalues each, hence also at most 2 projections corresponding to these eigenvalues. *Right and Double Coset Representatives* The fact that $q$ is invertible in $\mathbb{C}(q,Q)$ implies that the generators $g_i$ are also invertible in $H_n(q,Q)$. In fact, the inverse of the generators is given by $$g_i^{-1} = q^{-1}g_i + (q^{-1}-1)1 \in H_n(q,Q)$$ This implies that the following element is well-defined in $H_n(q,Q)$: $t_i^{'}=g_i\cdots g_1tg_1^{-1} \cdots g_i^{-1}$. We use this elements to define the set $\mathcal{D}_n$ as a subset of $H_n(q,Q)$. If $n=1$, we let $\mathcal{D}_1 := \{1,t\}$. For $n\geq 2$ we have $$\mathcal{D}_n:=\{1,g_{n-1},t^{'}_{n-1}\}.$$ Also the set of right coset representatives of $H_{n-1}(q,Q)$ in $H_n(q,Q)$ is given as follows: $$\mathcal{R}_n :=\{ 1,\ t'_{n-1},\  g_{n-1}g_{n-2}\ldots g_{n-k},\  g_{n-1}g_{n-2}\ldots g_{n-k}t'_{n-k-1} \ (1\leq k\leq n-1)\}.$$ Note that $\mathcal{R}_1 = \{1,t\}$. The elements $\{ r_1r_2\ldots r_n| r_i \in \mathcal{R}_i\}$ form a $\mathbb{C}(q,Q)$-basis of $H_n(q,Q)$, see [@gl].
