---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-016-33-framed-moduli-spaces
section_title: "Framed moduli spaces"
section_number: 3.3
pages: 32-32
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.901
latex_coverage_ratio: 1.0
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson– Thomas theory for Jacobi algebras and"
---
[]{#framedSec label="framedSec"} Framed moduli spaces will play a central role in what follows. Their cohomology provides an approximation to the cohomology of $\mathfrak{M}^{\upzeta\mathop{\mathrm{-ss}}}$, in a way which we will make precise in Section [\[cohaDT\]](#cohaDT){reference-type="ref" reference="cohaDT"}.

Let $\mathbf{f}\in\mathbb{N}^{Q_0}$ be a dimension vector (called the framing vector). We form a new quiver $Q_{\mathbf{f}}$ by setting $Q_{\mathbf{f}}=(Q_0\sqcup\{\infty\}, Q_1\sqcup \{\upbeta_{i,l_i}\colon \infty \to i \mid i\in Q_0, \hbox{ }1\le l_i\le \mathbf{f}_i \})$. Given a stability condition $\upzeta$ for $Q$, and a slope $\upmu\in(-\infty,\infty)$ we extend $\upzeta$ to a stability condition $\upzeta^{(\upmu)}_{\mathbf{f}}$ for $Q_{\mathbf{f}}$ by picking $\upzeta^{(\upmu)}_{\mathbf{f},\infty}\in\mathbb{H}_+$ so that $$-\Re e(\upzeta^{(\upmu)}_{\mathbf{f},\infty})/\Im m(\upzeta^{(\upmu)}_{\mathbf{f},\infty})=\upmu+\epsilon$$ for sufficiently small $\epsilon>0$, and picking $|\upzeta_{\mathbf{f},\infty}^{(\upmu)}|\gg 0$.

A $\mathbb{C} Q_{\mathbf{f}}$-module $\uprho$ with $\dim(\uprho)_{\infty}=1$ and $\dim(\uprho|_{\mathbb{C}Q})\in \Uplambda^{\upzeta}_{\upmu}$ is $\upzeta^{(\upmu)}_{\mathbf{f}}$-semistable if and only if the underlying $\mathbb{C} Q$-module is $\upzeta$-semistable, and for every $\mathbb{C}Q_{\mathbf{f}}$-submodule $\uprho'\subset \uprho$ such that $\dim(\uprho')_{\infty}=1$, the underlying $\mathbb{C} Q$-module of $\uprho'$ has slope strictly less than $\upmu$. A $\upzeta^{(\upmu)}_{\mathbf{f}}$-semistable $\mathbb{C}Q_{\mathbf{f}}$-module is automatically $\upzeta^{(\upmu)}_{\mathbf{f}}$-stable, and we write $\mathcal{M}^{\upzeta}_{\mathbf{f},\mathop{\mathrm{\mathbf{d}}}}$ for the fine moduli space of $\upzeta^{(\upmu)}_{\mathbf{f}}$-semistable $\mathbb{C} Q_{\mathbf{f}}$-modules of dimension $(1,\mathop{\mathrm{\mathbf{d}}})\in\mathbb{N}\times\Uplambda_{\upmu}^{\upzeta}$. The moduli space $\mathcal{M}_{\mathbf{f},\mathop{\mathrm{\mathbf{d}}}}^{\upzeta}$ is smooth.

::: remark
In fact $G_{\mathop{\mathrm{\mathbf{d}}}}$ acts freely on the smooth variety $$\label{Ydef}
Y_{\mathbf{f},\mathop{\mathrm{\mathbf{d}}}}^{\upzeta}\colonequals X(Q_{\mathbf{f}})^{\upzeta_{\mathbf{f}}^{(\upmu)}\mathop{\mathrm{-ss}}}_{(1,\mathop{\mathrm{\mathbf{d}}})},$$ and $\mathcal{M}_{\mathbf{f},\mathop{\mathrm{\mathbf{d}}}}^{\upzeta}$ is the quotient.
:::

We denote by $$\uppi\hspace{0.05em}_{\mathbf{f},\mathop{\mathrm{\mathbf{d}}}}^{\upzeta}\colon\mathcal{M}^{\upzeta}_{\mathbf{f},\mathop{\mathrm{\mathbf{d}}}}\rightarrow \mathcal{M}^{\upzeta\mathop{\mathrm{-ss}}}_{\mathop{\mathrm{\mathbf{d}}}}$$ the map given by forgetting the framing. It is a proper map, since the other two maps in the diagram $$\xymatrix{
\mathcal{M}^{\upzeta}_{\mathbf{f},\mathop{\mathrm{\mathbf{d}}}}\ar@/^1pc/[rr]\ar[r]_-{\uppi\hspace{0.05em}^\upzeta_{\mathbf{f},\mathop{\mathrm{\mathbf{d}}}}}&\mathcal{M}_{\mathop{\mathrm{\mathbf{d}}}}^{\upzeta\mathop{\mathrm{-ss}}}\ar[r]_-{q^\upzeta_{\mathop{\mathrm{\mathbf{d}}}}}&\mathcal{M}_{\mathop{\mathrm{\mathbf{d}}}}
}$$ are, as they are GIT quotient maps. For $\mathop{\mathrm{\mathbf{d}}}\in\Uplambda_{\upmu}^{\upzeta}$ we may alternatively extend $\mathop{\mathrm{\mathbf{d}}}$ to a dimension vector for $Q_{\mathbf{f}}$ by setting $\mathop{\mathrm{\mathbf{d}}}_{\infty}=0$. There is an obvious isomorphism $X(Q_{\mathbf{f}})_{(0,\mathop{\mathrm{\mathbf{d}}})}^{\upzeta_{\mathbf{f}}^{(\upmu)}\mathop{\mathrm{-ss}}}\cong X(Q)_{\mathop{\mathrm{\mathbf{d}}}}^{\upzeta\mathop{\mathrm{-ss}}}$.
