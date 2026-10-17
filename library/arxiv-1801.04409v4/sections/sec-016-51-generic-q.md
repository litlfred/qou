---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-016-51-generic-q
section_title: "Generic q"
section_number: 5.1
pages: 22-22
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 1.0
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
First assume that $q$ is not a root of unity. Then for any $V\in \mathcal{C}_q$, $E|_V$ is nilpotent, since $E$ maps eigenvectors of $g$ with eigenvalue $\lambda$ to those with eigenvalue $\lambda q$. Thus, the indecomposable objects of $\mathcal{C}_q$ are $V_{m_1,m_2}$, where $m_1\ge m_2$ are integers, namely, Jordan blocks for $E$ of size $m_1-m_2+1$ containing a nonzero vector $v$ with $gv=q^{m_1}v, Ev=0$. Then $\dim V_{m_1,m_2}=q^{m_2}+...+q^{m_1}$, which is never zero, so there is no nonzero negligible objects. It is easy to see that the tensor product of $V_{m_1,m_2}$ obeys the same fusion rules as representations of $GL_{{\bold q}}(2)$ with highest weights $(m_1,m_2)$, where ${\bold q}^2=q$. From this we obtain

::: proposition
[]{#quantgl2 label="quantgl2"} One has $\overline{\mathcal{C}_q}\cong \mathop{\mathrm{Rep}}\nolimits GL_{{\bold q}}(2)$.
:::

::: proof
*Proof.* Let us construct a tensor functor $T: \mathop{\mathrm{Rep}}\nolimits GL_{{\bold q}}(2)\to \mathcal{C}_q$ such that $\bold S\circ T$ is an equivalence $\mathop{\mathrm{Rep}}\nolimits GL_{{\bold q}}(2)\to \overline{\mathcal{C}_q}$. For this purpose, consider the Hopf algebra $U_{{\bold q}}(\mathfrak{gl}_2)$ with generators $g_1,g_2,e,f$ such that $g_1,g_2$ are commuting grouplike elements and $$g_1eg_1^{-1}={\bold q}e,\ g_1fg_1^{-1}={\bold q}^{-1}f,\ 
g_2eg_2^{-1}={\bold q}^{-1}e,\ g_2fg_2^{-1}={\bold q}f,\ $$ $$[e,f]=\frac{g_1g_2^{-1}-g_2g_1^{-1}}{{\bold q}-{\bold q}^{-1}},$$ $$\Delta(e)=e\otimes g_1g_2^{-1}+1\otimes e,\ \Delta(f)=f\otimes 1+g_2g_1^{-1}\otimes f.$$ Let us realize $\mathop{\mathrm{Rep}}\nolimits GL_{{\bold q}}(2)$ as the category of finite dimensional representations of $U_{{\bold q}}(\mathfrak{gl}_2)$ on which $g_1,g_2$ act semisimply with eigenvalues being powers of ${\bold q}$. Let $J$ be the twist for $U_{{\bold q}}(\mathfrak{gl}_2)$ which acts on $v\otimes w$ by ${\bold q}^{-rs}$ when $g_1v={\bold q}^rv$ and $g_2w={\bold q}^sw$. Then the conjugated coproduct $\Delta_J(a):=J^{-1}\Delta(a)J$ of the element $e$ has the form $$\Delta_J(e)=e\otimes g_1+g_1^{-1}\otimes e.$$ Thus, setting $\bar e:=g_1e$, we have $$\Delta_J(\bar e)=\bar e\otimes g_1^2+1\otimes \bar e.$$ We therefore have an inclusion of Hopf algebras $\psi: H_q\hookrightarrow U_{{\bold q}}(\mathfrak{gl}_2)^J$ given by $\psi(g)=g_1^2$, $\psi(E)=\bar e$, which defines the desired tensor functor $T$. ◻
:::
