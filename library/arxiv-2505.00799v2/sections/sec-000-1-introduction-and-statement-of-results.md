---
doc_id: arxiv-2505.00799v2
doc_title: "Quantum Modular Forms and Resurgence"
section_id: sec-000-1-introduction-and-statement-of-results
section_title: "Introduction and statement of results"
section_number: 1
pages: 1-3
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.983
doc_brief: "Quantum Modular Forms and Resurgence — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
In a seminal 2010 paper [@zagier-quantum], Zagier defined a new type of modular object which he called a quantum modular form. This new notion was meant to capture the behavior of a collection of examples from the literature. As Zagier remarked, these objects are reminiscent of calculations in perturbative quantum field theory and quantum topology. In the past few years, quantum modular forms have appeared prominently in connection to exciting new invariants in low-dimensional topology and knot theory (e.g. [@gppv; @g-z-24; @ajk]).

In this paper, we utilize tools popularized by quantum field theory in order to unify the examples from Zagier's original paper and subsequent works under a more robust framework.

Roughly speaking, a quantum modular form is a function which is not modular, but has an obstruction to modularity which is "nice.\" In Zagier's original definition, these are not functions on the upper half-plane $\mathbb{H}$, but are rather defined on $\mathbb{P}^1(\mathbb{Q}) = \mathbb{Q} \cup \{i\infty\}$. In a typical example, the original function has no continuous extension to $\mathbb{P}^1(\mathbb{R})$, but the error to modularity extends to, for example, a $C^j$, $C^\infty$, or real-analytic function on $\mathbb{P}^1(\mathbb{R})$. However, the most mysterious example in Zagier's original paper, called $\mathbf{J}(x)$ and defined using the colored Jones polynomials of the figure-eight knot, had an obstruction to modularity which did not even extend to a continuous function. However, he included intriguing graphs of this obstruction that were suggestive of some underlying quantum modular structure.

Over the last few years, the notion of holomorphic quantum modularity introduced by Garoufalidis and Zagier [@g-z-23; @g-z-24] has given a new perspective on $\mathbf{J}(x)$. It turns out that Zagier's original function naturally embeds as one component of a matrix-valued function. When considered as a matrix, the corresponding error to modularity is $C^\infty$, clarifying the behavior of the original function's obstruction. A second development in their work was the full consideration of quantum modular forms as functions on $\mathbb{C}\backslash \mathbb{R}$ instead of $\mathbb{Q}$. In Zagier's original paper, he introduced "strong\" quantum modular forms, which to each rational number assigned a full formal power series instead of just one complex number, and noted that in each case these functions also admitted a full extension to $(\mathbb{C}\backslash \mathbb{R}) \cup \mathbb{Q}$. This extension of the original definition goes hand in hand with the connection of resurgence to their work.

Resurgence is a theory built on Borel resummation, a procedure for summing divergent series which has found a prominent foothold in quantum field theory. This was naturally connected to $\mathbf{J}(x)$ due to the deep relationship between Jones polynomials and Chern--Simons theory, first realized in [@witten]. This connection has only deepened as resurgence and modularity have informed the study of quantum invariants of knots and 3-manifolds, see e.g. [@garoufalidis; @3d-modularity; @gukov-marino-putrov; @andersen-mistegard].

This connection to resurgence naturally led to the consideration of functions defined beyond $\mathbb{Q}$ which recovered the original quantum modular form through asymptotics. This new breakthrough and similar examples inspired the introduction of matrix-valued holomorphic quantum modular forms. In keeping with modern definitions such as in [@zagiertalk], here we offer a definition in the scalar-valued case which will suit our present purposes. We define the slash operator for the weights considered in this paper in Equation [\[eqn: slash\]](#eqn: slash){reference-type="ref" reference="eqn: slash"}.

::: definition
We say that a holomorphic function $g \colon \mathbb{H} \to \mathbb{C}$ is a holomorphic quantum modular form of weight $\kappa \in \mathbb{C}$ for $\Gamma_0(N)$ if for all $\gamma =\begin{psmallmatrix} a & b \\ c & d \end{psmallmatrix} \in \Gamma_0(N)$, we have that $$h_\gamma(z):= g(z) - g|_{\kappa }\gamma(z)$$ extends to an analytic function on the cut plane $\displaystyle{\mathbb{C}_\gamma := \{ z \in \mathbb{C} : cz+d \in \mathbb{C}\backslash\mathbb{R}_{\leq 0}\}.}$
:::

While these developments gave a richer understanding of the quantum modularity of $\mathbf{J}(x)$, they did not make clear how the rest of the examples in Zagier's original paper might relate to both holomorphic quantum modularity and resurgence.

Recently, Fantini and Rella made progress on this front. In [@fantini-rella], the authors offered a number of conjectures supported by examples about how resurgence can generate holomorphic quantum modular forms given the extra data of an $L$-function with a functional equation. To describe this phenomenon, they coined the term "modular resurgence.\"

We see their work as the start of a more general program to make the connection between holomorphic quantum modularity and resurgence explicit. In this paper, we continue to investigate this connection, unifying the examples in Zagier's original paper under one umbrella. In particular, we show that well-known families of quantum modular forms can be recovered by resurgence, and that resurgence naturally gives rise to quantum modularity.
